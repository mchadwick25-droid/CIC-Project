"""RAG retriever with Retrieve-When / Do-Not-Retrieve-When logic."""

from dataclasses import dataclass, field

from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_openai import ChatOpenAI

from app.config import settings
from app.rag.indexer import LexiconIndexer
from app.rag.pipeline import LEXICON_SPEC, run_retrieval
from app.rag.retrieval_mode import TURN, RetrievalMode
from app.rag.sections import (KEY_SOURCES_MARKERS, QUICK_MEANING_MARKERS,
                              excise_section, truncate_at)
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
        k: int | None = None,
        exclude_ids: set[str] | None = None,
        mode: RetrievalMode = TURN,
    ) -> RetrievalResult:
        """
        Retrieve relevant lexicon entries for a query.

        Args:
            query: The participant's message or question
            conversation_context: Recent conversation history for context
            k: Number of documents to retrieve (defaults to the spec's k)
            exclude_ids: S3.3 session exclusion set, honoured only in modes
                that allow it
            mode: WHY this retrieval is running - see app/rag/retrieval_mode.py.
                TURN (the default, and every turn-time caller) applies the
                Do-Not-Retrieve-When guards and the session exclusion set.
                ADJUDICATION does neither: it asks what the record contains,
                not what should surface to a participant right now.

        Returns:
            RetrievalResult with filtered documents and reasoning
        """
        k = LEXICON_SPEC.default_k if k is None else k
        # Initial candidate search - S3.2: hybrid BM25+dense RRF with R8
        # one-hop expansion (see candidate_search / app/rag/hybrid.py)
        docs_with_scores = self.candidate_search(query, k)
        candidate_docs = [doc for doc, _score in docs_with_scores]

        # Everything from session exclusion through the guard vote and the
        # decision/audit loop is shared with StoryRetriever - see
        # app/rag/pipeline.py for why it lives in one place now.
        result = run_retrieval(
            spec=LEXICON_SPEC,
            mode=mode,
            candidate_docs=candidate_docs,
            query=query,
            conversation_context=conversation_context,
            k=k,
            exclude_ids=exclude_ids,
            filter_llm=self.filter_llm,
            evaluation_cls=RetrievalEvaluation,
        )

        return RetrievalResult(
            documents=result.documents,
            terms=[doc.metadata.get("term", "") for doc in result.documents],
            reasoning=result.reasoning,
            evaluations=result.evaluations,
        )

    def get_context_for_response(
        self,
        query: str,
        conversation_context: str = "",
        exclude_ids: set[str] | None = None,
        mode: RetrievalMode = TURN,
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
        mode: see app/rag/retrieval_mode.py - TURN for a live turn,
        ADJUDICATION for source-fed judging of a turn already spoken.
        """
        result = self.retrieve(query, conversation_context,
                               exclude_ids=exclude_ids, mode=mode)

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
            body = truncate_at(body, KEY_SOURCES_MARKERS)
            # S5.3 (R7): for migrated worlds the quick_meaning of EVERY
            # term already rides the cached prefix - per-turn retrieval
            # narrows to the DEEP body, so the duplicated Quick Meaning
            # section is stripped from the serialized chunk. Fail-open:
            # unmigrated worlds keep the full body exactly as before.
            #
            # excise_section (app/rag/sections.py) knows BOTH of this
            # codebase's section conventions. The hand-rolled strip that
            # used to sit here searched only for a following "##" to find
            # where the section ended, so on a world whose chunks carry no
            # "##" at all and open with Quick Meaning - Desert - "no ##
            # found" read as "nothing follows this section" and the whole
            # lexicon body was discarded, leaving only the front-matter
            # block. Papnoute was generating with zero retrieved lexicon
            # content: an Article 5 grounding failure, live, in all 18 of
            # Desert's terms.
            try:
                from app.graph.repair_classifier import _migrated_world_ids
                if self.world_id in _migrated_world_ids():
                    body = excise_section(body, QUICK_MEANING_MARKERS)
            except Exception:
                pass
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
