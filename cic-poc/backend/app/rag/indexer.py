"""Indexer for lexicon chunks - creates FAISS vector store."""

import re
from dataclasses import dataclass
from pathlib import Path

from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings

from app.config import settings


@dataclass
class LexiconEntry:
    """Parsed lexicon entry with front-matter and content."""

    term: str
    world_code: str
    tier: int
    tags: list[str]
    aliases: list[str]
    related_terms: list[str]
    retrieve_when: str
    do_not_retrieve_when: str
    content: str
    source_file: str
    key_sources: str


class LexiconIndexer:
    """Indexes lexicon chunks into a FAISS vector store."""

    def __init__(self):
        # Using local sentence-transformers model - no API key required
        self.embeddings = HuggingFaceEmbeddings(
            model_name="all-MiniLM-L6-v2",
            model_kwargs={"device": "cpu"},
            encode_kwargs={"normalize_embeddings": True},
        )

    def parse_front_matter(self, text: str) -> dict[str, str]:
        """Parse the retrieval front-matter from a lexicon file."""
        front_matter = {}

        # Find the code block with front-matter
        match = re.search(r"```\n(.*?)\n```", text, re.DOTALL)
        if not match:
            return front_matter

        lines = match.group(1).strip().split("\n")
        current_key = None
        current_value = []

        for line in lines:
            # Check if this is a key-value line
            if ":" in line and not line.startswith(" "):
                # Save previous key-value if exists
                if current_key:
                    front_matter[current_key] = " ".join(current_value).strip()

                # Parse new key-value
                key, value = line.split(":", 1)
                current_key = key.strip().lower().replace("-", "_")
                current_value = [value.strip()]
            elif current_key and line.strip():
                # Continuation of previous value
                current_value.append(line.strip())

        # Save last key-value
        if current_key:
            front_matter[current_key] = " ".join(current_value).strip()

        return front_matter

    def parse_key_sources(self, content: str) -> str:
        """Extract the '## Key Sources' section text, if present."""
        if "## Key Sources" not in content:
            return ""

        remaining = content.split("## Key Sources", 1)[1]

        # Section ends at the next heading or separator
        end_markers = ["\n---", "\n## "]
        end_pos = len(remaining)
        for marker in end_markers:
            pos = remaining.find(marker)
            if pos > 0 and pos < end_pos:
                end_pos = pos

        return remaining[:end_pos].strip()

    def parse_lexicon_file(self, file_path: Path) -> LexiconEntry:
        """Parse a single lexicon file into a LexiconEntry."""
        content = file_path.read_text(encoding="utf-8")
        front_matter = self.parse_front_matter(content)
        key_sources = self.parse_key_sources(content)

        # Extract content after front-matter (everything after the ---)
        content_parts = content.split("---", 2)
        main_content = content_parts[2] if len(content_parts) > 2 else content

        # Parse list fields
        def parse_list(value: str) -> list[str]:
            if not value:
                return []
            return [item.strip() for item in value.split(",")]

        return LexiconEntry(
            term=front_matter.get("term", ""),
            world_code=front_matter.get("world_code", "syr"),
            tier=int(front_matter.get("tier", "1")),
            tags=parse_list(front_matter.get("tags", "")),
            aliases=parse_list(front_matter.get("aliases", "")),
            related_terms=parse_list(front_matter.get("related_terms", "")),
            retrieve_when=front_matter.get("retrieve_when", ""),
            do_not_retrieve_when=front_matter.get("do_not_retrieve_when", ""),
            content=main_content.strip(),
            source_file=file_path.name,
            key_sources=key_sources,
        )

    def create_documents(self, entries: list[LexiconEntry]) -> list[Document]:
        """Convert lexicon entries to LangChain documents for indexing."""
        documents = []

        for entry in entries:
            # Create searchable text combining term, aliases, and content
            searchable_text = f"""
Term: {entry.term}
Aliases: {', '.join(entry.aliases)}
Related: {', '.join(entry.related_terms)}

{entry.content}
"""

            metadata = {
                "term": entry.term,
                "tier": entry.tier,
                "tags": entry.tags,
                "aliases": entry.aliases,
                "related_terms": entry.related_terms,
                "retrieve_when": entry.retrieve_when,
                "do_not_retrieve_when": entry.do_not_retrieve_when,
                "source_file": entry.source_file,
                "key_sources": entry.key_sources,
            }

            documents.append(Document(page_content=searchable_text, metadata=metadata))

        return documents

    def index_lexicon(self, lexicon_path: Path | None = None) -> FAISS:
        """Index all lexicon files and create FAISS vector store."""
        if lexicon_path is None:
            lexicon_path = settings.lexicon_chunks_path

        # Parse all lexicon files
        entries = []
        for file_path in sorted(lexicon_path.glob("*.md")):
            entry = self.parse_lexicon_file(file_path)
            entries.append(entry)
            print(f"Parsed: {file_path.name} -> {entry.term}")

        # Create documents
        documents = self.create_documents(entries)
        print(f"Created {len(documents)} documents for indexing")

        # Create FAISS vector store
        vector_store = FAISS.from_documents(documents, self.embeddings)
        print("FAISS vector store created")

        return vector_store

    def save_index(self, vector_store: FAISS, path: Path | None = None) -> None:
        """Save the FAISS index to disk."""
        if path is None:
            path = settings.vector_store_path

        path.mkdir(parents=True, exist_ok=True)
        vector_store.save_local(str(path))
        print(f"Index saved to {path}")

    def load_index(self, path: Path | None = None) -> FAISS:
        """Load a FAISS index from disk."""
        if path is None:
            path = settings.vector_store_path

        return FAISS.load_local(
            str(path),
            self.embeddings,
            allow_dangerous_deserialization=True,
        )
