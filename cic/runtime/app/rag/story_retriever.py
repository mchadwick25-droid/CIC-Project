"""RAG retriever for story chunks (Doc_09), mirroring LexiconRetriever's
Retrieve-When / Do-Not-Retrieve-When logic against the story schema."""

from dataclasses import dataclass, field

from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_openai import ChatOpenAI

from app.config import settings
from app.rag.pipeline import STORY_SPEC, run_retrieval
from app.rag.retrieval_mode import TURN, RetrievalMode
from app.rag.retriever import Citation, RetrievalEvaluation
from app.rag.sections import (VOICE_APPARATUS_STORY_SECTIONS,
                              excise_sections)
from app.rag.source_registry import resolve_references
from app.rag.story_indexer import StoryIndexer


@dataclass
class StoryRetrievalResult:
    """Result of a story retrieval operation."""

    documents: list[Document]
    reasoning: str
    evaluations: list[RetrievalEvaluation] = field(default_factory=list)


class StoryRetriever:
    """
    Retrieves relevant story chunks based on conversation context.

    Uses the same Retrieve-When / Do-Not-Retrieve-When metadata pattern as
    the lexicon retriever, applied to story chunks instead of terms.
    """

    def __init__(self, vector_store: FAISS | None = None, world_id: str = "syriac-edessa-nisibis"):
        self.indexer = StoryIndexer()
        self.world_id = world_id

        if vector_store:
            self.vector_store = vector_store
        else:
            try:
                vector_store_path = settings.get_story_vector_store_path(world_id)
                self.vector_store = self.indexer.load_index(vector_store_path)
            except Exception:
                world_config = settings.get_world_config(world_id)
                self.vector_store = self.indexer.index_stories(world_config.story_chunks_path)
                self.indexer.save_index(self.vector_store, settings.get_story_vector_store_path(world_id))
        self._hybrid = None

        if settings.mock_llm:
            from app.mock_llm import MockChatModel

            self.filter_llm = MockChatModel()
        elif settings.llm_provider == "anthropic":
            from langchain_anthropic import ChatAnthropic

            self.filter_llm = ChatAnthropic(
                model="claude-haiku-4-5-20251001",
                anthropic_api_key=settings.anthropic_api_key,
            )
        elif settings.llm_provider == "bedrock":
            from app.bedrock_llm import make_bedrock_llm

            self.filter_llm = make_bedrock_llm(settings.bedrock_monitoring_model_id)
        else:
            self.filter_llm = ChatOpenAI(
                model="gpt-4o-mini",
                openai_api_key=settings.openai_api_key,
            )

    def candidate_search(self, query: str, k: int):
        """S3.2: hybrid candidate generation - see LexiconRetriever."""
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
    ) -> StoryRetrievalResult:
        """
        Retrieve relevant story chunks for a query.

        A lower default k than the lexicon retriever - stories are longer and
        a representative should draw on at most one or two per turn, not
        pepper an answer with narrative.

        mode: see app/rag/retrieval_mode.py. Identical semantics to
        LexiconRetriever.retrieve, and now literally the same code path
        (app/rag/pipeline.py) rather than a second copy of it.
        """
        k = STORY_SPEC.default_k if k is None else k
        # S3.2: hybrid BM25+dense candidate search (see app/rag/hybrid.py)
        docs_with_scores = self.candidate_search(query, k)
        candidate_docs = [doc for doc, _score in docs_with_scores]

        result = run_retrieval(
            spec=STORY_SPEC,
            mode=mode,
            candidate_docs=candidate_docs,
            query=query,
            conversation_context=conversation_context,
            k=k,
            exclude_ids=exclude_ids,
            filter_llm=self.filter_llm,
            evaluation_cls=RetrievalEvaluation,
        )

        return StoryRetrievalResult(
            documents=result.documents,
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

        Citations here carry the story's front-matter Source field (which the
        Usage Guidance requires the representative to name when telling the
        story), enriched with any resolved Source Registry rows it references.
        mode: see app/rag/retrieval_mode.py.
        """
        result = self.retrieve(query, conversation_context,
                               exclude_ids=exclude_ids, mode=mode)

        if not result.documents:
            return "", [], result.evaluations

        context_parts = ["## Retrieved Story Context\n"]
        citations = []

        for doc in result.documents:
            title = doc.metadata.get("story_title", "Unknown")
            tier = doc.metadata.get("tier", "")
            confidence = doc.metadata.get("confidence", "")
            source = doc.metadata.get("source", "")

            context_parts.append(f"### {title} (Tier {tier})\n")
            if confidence:
                context_parts.append(f"Confidence: {confidence}\n")
            # S3.1: body from metadata["content"]; see retriever.py
            # StoryIndexer already strips Tier Justification, Source
            # Identification and Final Assembly Instruction at INDEX time, so
            # those are absent from metadata["content"] on any freshly built
            # store. This strip runs at SERIALIZATION time instead, which is
            # what lets it take effect on stores built before it existed -
            # no re-index required - and keeps the lexicon and story paths
            # applying the same rule from the same place.
            body = doc.metadata.get("content", doc.page_content)
            body = excise_sections(body, VOICE_APPARATUS_STORY_SECTIONS)
            context_parts.append(body)
            context_parts.append("\n---\n")

            if source:
                citations.append(
                    Citation(
                        term=title,
                        key_sources=source,
                        source_file=doc.metadata.get("source_file", ""),
                        registry=resolve_references(self.world_id, source),
                    )
                )

        return "\n".join(context_parts), citations, result.evaluations
