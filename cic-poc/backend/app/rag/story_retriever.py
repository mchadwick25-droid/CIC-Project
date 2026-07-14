"""RAG retriever for story chunks (Doc_09), mirroring LexiconRetriever's
Retrieve-When / Do-Not-Retrieve-When logic against the story schema."""

from dataclasses import dataclass, field

from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_openai import ChatOpenAI

from app.config import settings
from app.rag.batch_evaluate import Candidate, evaluate_batch, partition_tier1_short_circuit
from app.rag.retriever import Citation, RetrievalEvaluation
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
        k: int = 2,
    ) -> StoryRetrievalResult:
        """
        Retrieve relevant story chunks for a query.

        A lower default k than the lexicon retriever - stories are longer and
        a representative should draw on at most one or two per turn, not
        pepper an answer with narrative.
        """
        docs_with_scores = self.vector_store.similarity_search_with_score(query, k=k * 2)
        candidate_docs = [doc for doc, _score in docs_with_scores]

        # Tier 1 stories (tied to this world's own central formation theme)
        # that also rank among the closest semantic matches retrieve
        # deterministically, without an LLM vote - see
        # partition_tier1_short_circuit for why.
        auto_retrieve_docs, llm_vote_docs = partition_tier1_short_circuit(
            candidate_docs, conversation_context, label_key="story_title"
        )

        decisions_by_id: dict[int, tuple[bool, str]] = {
            id(doc): (
                True,
                "Tier 1 (tied to this world's own central formation theme) and among the closest "
                "semantic matches to the question - retrieved without an LLM vote.",
            )
            for doc in auto_retrieve_docs
        }

        if llm_vote_docs:
            candidates = [
                Candidate(
                    label=doc.metadata.get("story_title", "unknown"),
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
                item_noun="story",
                extra_instruction=(
                    "A story does not need to be directly asked for - RETRIEVE it whenever it would "
                    "genuinely illustrate the point at hand, the way a teacher reaches for a concrete "
                    "memory to ground an abstract point. Still SKIP when the connection is only "
                    "topically adjacent, when this exact story was already told earlier in the "
                    "conversation, or when telling it would crowd out actually answering the question."
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
            title = doc.metadata.get("story_title", "unknown")
            source_file = doc.metadata.get("source_file", "")

            evaluations.append(
                RetrievalEvaluation(
                    term=title,
                    source_file=source_file,
                    retrieved=should_retrieve,
                    reason=reason,
                )
            )

            if should_retrieve and len(filtered_docs) < k:
                filtered_docs.append(doc)
                reasoning_parts.append(f"Retrieved '{title}': {reason}")
            elif should_retrieve:
                reasoning_parts.append(f"Retrieved but over limit '{title}': {reason}")
            else:
                reasoning_parts.append(f"Skipped '{title}': {reason}")

        return StoryRetrievalResult(
            documents=filtered_docs,
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

        Citations here carry the story's front-matter Source field (which the
        Usage Guidance requires the representative to name when telling the
        story), enriched with any resolved Source Registry rows it references.
        """
        result = self.retrieve(query, conversation_context)

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
            context_parts.append(doc.page_content)
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
