"""RAG retriever with Retrieve-When / Do-Not-Retrieve-When logic."""

from dataclasses import dataclass
from pathlib import Path

from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_openai import ChatOpenAI

from app.config import settings
from app.rag.indexer import LexiconIndexer


@dataclass
class RetrievalResult:
    """Result of a retrieval operation."""

    documents: list[Document]
    terms: list[str]
    reasoning: str


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
        if settings.llm_provider == "anthropic":
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

        # Filter based on Retrieve-When / Do-Not-Retrieve-When
        filtered_docs = []
        reasoning_parts = []

        for doc, score in docs_with_scores:
            term = doc.metadata.get("term", "unknown")
            retrieve_when = doc.metadata.get("retrieve_when", "")
            do_not_retrieve_when = doc.metadata.get("do_not_retrieve_when", "")

            # Use LLM to evaluate retrieval conditions
            should_retrieve, reason = self._evaluate_retrieval(
                term=term,
                query=query,
                conversation_context=conversation_context,
                retrieve_when=retrieve_when,
                do_not_retrieve_when=do_not_retrieve_when,
            )

            if should_retrieve:
                filtered_docs.append(doc)
                reasoning_parts.append(f"Retrieved '{term}': {reason}")

                if len(filtered_docs) >= k:
                    break
            else:
                reasoning_parts.append(f"Skipped '{term}': {reason}")

        terms = [doc.metadata.get("term", "") for doc in filtered_docs]

        return RetrievalResult(
            documents=filtered_docs,
            terms=terms,
            reasoning="\n".join(reasoning_parts),
        )

    def _evaluate_retrieval(
        self,
        term: str,
        query: str,
        conversation_context: str,
        retrieve_when: str,
        do_not_retrieve_when: str,
    ) -> tuple[bool, str]:
        """
        Evaluate whether to retrieve a document based on its conditions.

        Returns (should_retrieve, reasoning).
        """
        # If no conditions specified, use default retrieval
        if not retrieve_when and not do_not_retrieve_when:
            return True, "No conditions specified, using semantic match"

        prompt = f"""You are evaluating whether to retrieve a lexicon entry for a conversation.

Term: {term}

Participant's message: {query}

Recent conversation context: {conversation_context}

RETRIEVE-WHEN conditions (retrieve if ANY match):
{retrieve_when or "None specified"}

DO-NOT-RETRIEVE-WHEN conditions (skip if ANY match):
{do_not_retrieve_when or "None specified"}

Evaluate whether this entry should be retrieved.
Respond with exactly one line: "RETRIEVE: <brief reason>" or "SKIP: <brief reason>"
"""

        response = self.filter_llm.invoke(prompt)
        result = response.content.strip()

        if result.upper().startswith("RETRIEVE"):
            reason = result.split(":", 1)[1].strip() if ":" in result else "Matched conditions"
            return True, reason
        else:
            reason = result.split(":", 1)[1].strip() if ":" in result else "Did not match conditions"
            return False, reason

    def get_context_for_response(
        self,
        query: str,
        conversation_context: str = "",
    ) -> str:
        """
        Get formatted context string for the representative's response.

        This is the main entry point for RAG-augmented responses.
        """
        result = self.retrieve(query, conversation_context)

        if not result.documents:
            return ""

        context_parts = ["## Retrieved Lexicon Context\n"]

        for doc in result.documents:
            term = doc.metadata.get("term", "Unknown")
            context_parts.append(f"### {term}\n")
            context_parts.append(doc.page_content)
            context_parts.append("\n---\n")

        return "\n".join(context_parts)
