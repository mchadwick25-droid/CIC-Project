"""RAG retriever with Retrieve-When / Do-Not-Retrieve-When logic."""

from dataclasses import dataclass, field
from pathlib import Path

from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_openai import ChatOpenAI

from app.config import settings
from app.rag.batch_evaluate import (Candidate, _evaluable_negative_condition,
                                     evaluate_negative_conditions)
from app.rag.indexer import LexiconIndexer
from app.rag.source_registry import resolve_references


@dataclass
class Citation:
    """A citation to a source document backing a retrieved lexicon entry."""

    term: str
    key_sources: str
    source_file: str
    registry: list[dict] = field(default_factory=list)


@dataclass
class RetrievalEvaluation:
    """A record of whether a candidate lexicon entry was retrieved and why.

    Covers every document the retriever considered for a query, not just the
    ones that made it into the response's context - this is the audit trail
    for "what files were accessed" behind a given answer.
    """

    term: str
    source_file: str
    retrieved: bool
    reason: str


@dataclass
class RetrievalResult:
    """Result of a retrieval operation."""

    documents: list[Document]
    terms: list[str]
    reasoning: str
    evaluations: list[RetrievalEvaluation] = field(default_factory=list)


class LexiconRetriever:
    """
    Retrieves relevant lexicon entries based on conversation context.

    Uses the Retrieve-When / Do-Not-Retrieve-When metadata to filter
    results intelligently.
    """

    def __init__(self, vector_store: FAISS | None = None, world_id: str = "syriac-edessa-nisibis"):
        self.indexer = LexiconIndexer()
        self.world_id = world_id

        if vector_store:
            self.vector_store = vector_store
        else:
            # Try to load existing index for this world
            try:
                vector_store_path = settings.get_vector_store_path(world_id)
                self.vector_store = self.indexer.load_index(vector_store_path)
            except Exception:
                # Index doesn't exist, create it
                world_config = settings.get_world_config(world_id)
                self.vector_store = self.indexer.index_lexicon(world_config.lexicon_chunks_path)
                self.indexer.save_index(self.vector_store, settings.get_vector_store_path(world_id))
        self._hybrid = None

        # LLM for retrieval filtering
        if settings.mock_llm:
            from app.mock_llm import MockChatModel

            self.filter_llm = MockChatModel()
        elif settings.llm_provider == "anthropic":
            from langchain_anthropic import ChatAnthropic

            self.filter_llm = ChatAnthropic(
                model="claude-haiku-4-5-20251001",
                anthropic_api_key=settings.anthropic_api_key,
            )
        else:
            self.filter_llm = ChatOpenAI(
                model="gpt-4o-mini",
                openai_api_key=settings.openai_api_key,
            )

    def candidate_search(self, query: str, k: int):
        """S3.2 candidate generation: BM25+dense weighted-RRF fusion with
        R8 one-hop related-terms expansion (app/rag/hybrid.py). Built
        lazily so retriever construction stays cheap; returns the same
        (doc, score) contract the old similarity_search_with_score call
        supplied, truncated to the same k*2 candidate budget."""
        from app.rag.hybrid import HybridSearcher
        if self._hybrid is None:
            self._hybrid = HybridSearcher(self.vector_store)
        return self._hybrid.search(query, k)[: k * 2]

    def retrieve(
        self,
        query: str,
        conversation_context: str = "",
        k: int = 3,
        exclude_ids: set[str] | None = None,
    ) -> RetrievalResult:
        """
        Retrieve relevant lexicon entries for a query.

        Args:
            query: The participant's message or question
            conversation_context: Recent conversation history for context
            k: Number of documents to retrieve

        Returns:
            RetrievalResult with filtered documents and reasoning
        """
        # Initial candidate search - S3.2: hybrid BM25+dense RRF with R8
        # one-hop expansion (see candidate_search / app/rag/hybrid.py)
        docs_with_scores = self.candidate_search(query, k)
        candidate_docs = [doc for doc, _score in docs_with_scores]

        # S3.3 (Pass 1 R4): the ID-keyed session exclusion set - chunks
        # already surfaced this session are dropped deterministically at
        # candidate stage, with an audit-trail entry each. Replaces the
        # substring already_discussed proxy (broken on composite labels).
        excluded_evals = []
        if exclude_ids:
            kept = []
            for doc in candidate_docs:
                stem = Path(doc.metadata.get("source_file", "")).stem
                if stem in exclude_ids:
                    excluded_evals.append(RetrievalEvaluation(
                        term=doc.metadata.get("term", "unknown"),
                        source_file=doc.metadata.get("source_file", ""),
                        retrieved=False,
                        reason="Session exclusion set: already surfaced "
                               "this session (deterministic ID match).",
                    ))
                else:
                    kept.append(doc)
            candidate_docs = kept

        # S3.4 (Pass 1 R6): relevance is decided by the local cross-encoder,
        # deterministically - the batched LLM relevance vote (and the tier-1
        # short-circuit that existed to protect tier-1 terms from that
        # vote's batch dilution) are both gone. The ONE remaining LLM call
        # judges only Do-Not-Retrieve-When guards, and only when a
        # relevance-kept candidate actually carries an evaluable one.
        from app.rag.cross_encoder import score_candidates, threshold_for

        scores = score_candidates(query, candidate_docs)
        rel_threshold = threshold_for(query)
        # S3.4: selection order is the cross-encoder's ranking (its
        # ordering is reliable even where its absolute score is not -
        # see cross_encoder.py); the fused candidate list stays the
        # audit-trail order
        candidate_docs = [d for _s, d in sorted(
            zip(scores, candidate_docs), key=lambda x: -x[0])]
        scores = sorted(scores, reverse=True)
        decisions_by_id: dict[int, tuple[bool, str]] = {}
        guarded_docs = []
        for rank, (doc, score) in enumerate(zip(candidate_docs, scores)):
            # A candidate the cross-encoder itself ranks inside the final
            # k is never hard-dropped on absolute score: the model's
            # ordering is reliable where its absolute calibration is not
            # (measured - deep-thematic must-docs score in the noise band
            # on clean queries yet rank top). The threshold prunes only
            # beyond-window noise, which also bounds the guard-vote batch.
            if score < rel_threshold and rank >= k:
                decisions_by_id[id(doc)] = (
                    False,
                    f"Cross-encoder relevance {score:.2f} below threshold "
                    f"{rel_threshold} - not relevant to this turn.",
                )
            elif _evaluable_negative_condition(
                    doc.metadata.get("do_not_retrieve_when", "")):
                guarded_docs.append(doc)
            else:
                decisions_by_id[id(doc)] = (
                    True,
                    f"Cross-encoder relevance {score:.2f} - retrieved "
                    f"(no evaluable guard).",
                )

        if guarded_docs:
            candidates = [
                Candidate(
                    label=doc.metadata.get("term", "unknown"),
                    retrieve_when=doc.metadata.get("retrieve_when", ""),
                    do_not_retrieve_when=doc.metadata.get("do_not_retrieve_when", ""),
                    tier=doc.metadata.get("tier", 1),
                )
                for doc in guarded_docs
            ]
            decisions = evaluate_negative_conditions(
                self.filter_llm,
                candidates,
                query,
                conversation_context,
                item_noun="lexicon entry",
            )
            decisions_by_id.update(
                {id(doc): decision for doc, decision in zip(guarded_docs, decisions)}
            )

        filtered_docs = []
        reasoning_parts = []
        evaluations = list(excluded_evals)  # session-exclusion audit entries

        for doc in candidate_docs:
            should_retrieve, reason = decisions_by_id[id(doc)]
            term = doc.metadata.get("term", "unknown")
            source_file = doc.metadata.get("source_file", "")

            evaluations.append(
                RetrievalEvaluation(
                    term=term,
                    source_file=source_file,
                    retrieved=should_retrieve,
                    reason=reason,
                )
            )

            if should_retrieve and len(filtered_docs) < k:
                filtered_docs.append(doc)
                reasoning_parts.append(f"Retrieved '{term}': {reason}")
            elif should_retrieve:
                reasoning_parts.append(f"Retrieved but over limit '{term}': {reason}")
            else:
                reasoning_parts.append(f"Skipped '{term}': {reason}")

        terms = [doc.metadata.get("term", "") for doc in filtered_docs]

        return RetrievalResult(
            documents=filtered_docs,
            terms=terms,
            reasoning="\n".join(reasoning_parts),
            evaluations=evaluations,
        )

    def get_context_for_response(
        self,
        query: str,
        conversation_context: str = "",
        exclude_ids: set[str] | None = None,
    ) -> tuple[str, list[Citation], list[RetrievalEvaluation]]:
        """
        Get formatted context string, citations, and the retrieval audit trail
        for the representative's response.

        This is the main entry point for RAG-augmented responses. The returned
        citations identify which source documents (per the lexicon's Key Sources)
        back the retrieved context, for display in the UI. The evaluations cover
        every lexicon file considered for this turn - retrieved or skipped, and
        why - for auditing what the representative's answer actually drew on.
        exclude_ids: the S3.3 session exclusion set (chunk-id stems already
        surfaced this session), applied deterministically at candidate stage.
        """
        result = self.retrieve(query, conversation_context, exclude_ids=exclude_ids)

        if not result.documents:
            return "", [], result.evaluations

        context_parts = ["## Retrieved Lexicon Context\n"]
        citations = []

        for doc in result.documents:
            term = doc.metadata.get("term", "Unknown")
            context_parts.append(f"### {term}\n")
            # S3.1: page_content is now the retrieval surface; the chunk
            # body rides in metadata["content"] (fallback keeps old
            # indexes readable until every store is rebuilt)
            body = doc.metadata.get("content", doc.page_content)
            # S5.2 (Pass 1 §5.1): the Key-Sources apparatus never enters
            # generation context - the lexicon side's equivalent of the
            # story indexer's voice-unsafe-section strip. The apparatus
            # stays in metadata (the citation chip's source) and Levels
            # 2/3; only the voice-safe body is serialized.
            for marker in ("## Key Sources", "**Key Sources:**",
                           "**Key Sources**"):
                idx = body.find(marker)
                if idx != -1:
                    body = body[:idx].rstrip()
                    break
            context_parts.append(body)
            context_parts.append("\n---\n")

            key_sources = doc.metadata.get("key_sources", "")
            if key_sources:
                citations.append(
                    Citation(
                        term=term,
                        key_sources=key_sources,
                        source_file=doc.metadata.get("source_file", ""),
                        registry=resolve_references(self.world_id, key_sources),
                    )
                )

        return "\n".join(context_parts), citations, result.evaluations
