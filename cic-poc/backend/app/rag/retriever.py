"""RAG retriever with Retrieve-When / Do-Not-Retrieve-When logic."""

from dataclasses import dataclass, field
from pathlib import Path

from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_openai import ChatOpenAI

from app.config import settings
from app.rag.batch_evaluate import Candidate, evaluate_batch, partition_tier1_short_circuit
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

    def retrieve(
        self,
        query: str,
        conversation_context: str = "",
        k: int = 3,
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
        # Initial semantic search
        docs_with_scores = self.vector_store.similarity_search_with_score(query, k=k * 2)
        candidate_docs = [doc for doc, _score in docs_with_scores]

        # Tier 1 candidates that also rank among the closest semantic matches
        # retrieve deterministically, without an LLM vote - see
        # partition_tier1_short_circuit for why. Everything else still goes
        # through the LLM's Retrieve-When / Do-Not-Retrieve-When judgment.
        auto_retrieve_docs, llm_vote_docs = partition_tier1_short_circuit(
            candidate_docs, conversation_context, label_key="term"
        )

        decisions_by_id: dict[int, tuple[bool, str]] = {
            id(doc): (
                True,
                "Tier 1 (this world's own declared center of gravity) and among the closest "
                "semantic matches to the question - retrieved without an LLM vote.",
            )
            for doc in auto_retrieve_docs
        }

        if llm_vote_docs:
            candidates = [
                Candidate(
                    label=doc.metadata.get("term", "unknown"),
                    retrieve_when=doc.metadata.get("retrieve_when", ""),
                    do_not_retrieve_when=doc.metadata.get("do_not_retrieve_when", ""),
                    tier=doc.metadata.get("tier", 1),
                )
                for doc in llm_vote_docs
            ]
            decisions = evaluate_batch(
                self.filter_llm,
                candidates,
                query,
                conversation_context,
                item_noun="lexicon entry",
                extra_instruction=(
                    "A Retrieve-When condition naming a topic or theme is satisfied when the question "
                    "would naturally lead a representative formed in this world to reach for that term "
                    "as part of how they characteristically answer it - not only when the participant's "
                    "own wording literally names the term. Still SKIP when the term is only tangentially "
                    "related, or genuinely belongs to a different topic than what is being asked."
                ),
            )
            decisions_by_id.update(
                {id(doc): decision for doc, decision in zip(llm_vote_docs, decisions)}
            )

        filtered_docs = []
        reasoning_parts = []
        evaluations = []

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
    ) -> tuple[str, list[Citation], list[RetrievalEvaluation]]:
        """
        Get formatted context string, citations, and the retrieval audit trail
        for the representative's response.

        This is the main entry point for RAG-augmented responses. The returned
        citations identify which source documents (per the lexicon's Key Sources)
        back the retrieved context, for display in the UI. The evaluations cover
        every lexicon file considered for this turn - retrieved or skipped, and
        why - for auditing what the representative's answer actually drew on.
        """
        result = self.retrieve(query, conversation_context)

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
            context_parts.append(doc.metadata.get("content", doc.page_content))
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
