"""Indexer for story chunks (Doc_09) - creates a FAISS vector store.

Story chunks share the same Retrieve-When / Do-Not-Retrieve-When retrieval
pattern as lexicon chunks, but a different front-matter schema (Story-Title
instead of Term, no Tags, a Confidence field, and a single-line Source
citation instead of a discrete Key Sources section) and a looser formatting
convention - the Syriac world wraps front-matter in a "## Retrieval
Front-Matter" header and fenced code block, the PAHC world does not.
"""

import re
import sys
from dataclasses import dataclass
from pathlib import Path

from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings

from app.config import settings


@dataclass
class StoryEntry:
    """Parsed story chunk with front-matter and content."""

    story_title: str
    world_code: str
    tier: int
    confidence: str
    source: str
    retrieve_when: str
    do_not_retrieve_when: str
    content: str
    source_file: str
    force_llm_vote: bool = False


class StoryIndexer:
    """Indexes story chunks into a FAISS vector store."""

    def __init__(self):
        # Using local sentence-transformers model - no API key required
        self.embeddings = HuggingFaceEmbeddings(
            model_name="all-MiniLM-L6-v2",
            model_kwargs={"device": "cpu"},
            encode_kwargs={"normalize_embeddings": True},
        )

    def parse_front_matter(self, text: str) -> tuple[dict[str, str], str]:
        """Parse the retrieval front-matter from a story file.

        Returns (front_matter_dict, remaining_content). Handles both the
        fenced-and-headered Syriac convention and the bare PAHC convention.
        """
        # Fenced convention: front-matter lives inside a ``` code block.
        fenced_match = re.search(r"```\n(.*?)\n```", text, re.DOTALL)
        if fenced_match:
            front_matter_block = fenced_match.group(1)
            remaining = text[fenced_match.end():]
        else:
            # Bare convention: front-matter is every line up to the first
            # "---" separator (which precedes "## Story Text").
            parts = text.split("---", 1)
            front_matter_block = parts[0]
            remaining = parts[1] if len(parts) > 1 else ""

        front_matter = {}
        current_key = None
        current_value = []

        for line in front_matter_block.strip().split("\n"):
            if ":" in line and not line.startswith(" ") and re.match(r"^[A-Za-z][\w\s-]*:", line):
                if current_key:
                    front_matter[current_key] = " ".join(current_value).strip()
                key, value = line.split(":", 1)
                current_key = key.strip().lower().replace("-", "_")
                current_value = [value.strip()]
            elif current_key and line.strip():
                current_value.append(line.strip())

        if current_key:
            front_matter[current_key] = " ".join(current_value).strip()

        return front_matter, remaining.strip()

    # Sections stripped before a chunk's content ever reaches the
    # Representative's own prompt - construction-record material (why a
    # tier/citation was assigned, how sources were reconciled) that exists
    # to help a human author or reviewer, not to be voiced. Left in place,
    # this is exactly where chunks tend to name modern scholars and live
    # academic disputes by name (e.g. "the Shaw/Jones dispute"), directly
    # contradicting this project's own "no meta-awareness of scholarship"
    # principle - confirmed present in pahcstory005 and pahcstory013.
    # "Usage Guidance" is deliberately NOT stripped here: it also carries
    # real anti-fabrication instructions (e.g. "must never narrate
    # Peregrinus himself") that the Representative does need: any
    # meta-scholarship language inside that section is fixed at the
    # chunk-authoring level instead, case by case.
    _VOICE_UNSAFE_SECTIONS = ("## Tier Justification", "## Source Identification")

    def _strip_voice_unsafe_sections(self, text: str) -> str:
        """Remove construction-record-only sections from Representative-facing content."""
        for heading in self._VOICE_UNSAFE_SECTIONS:
            start = text.find(heading)
            if start == -1:
                continue
            next_heading = text.find("\n## ", start + len(heading))
            end = next_heading if next_heading != -1 else len(text)
            text = text[:start] + text[end:]
        return text.strip()

    def parse_story_file(self, file_path: Path) -> StoryEntry:
        """Parse a single story chunk file into a StoryEntry."""
        content = file_path.read_text(encoding="utf-8")
        front_matter, remaining = self.parse_front_matter(content)

        return StoryEntry(
            story_title=front_matter.get("story_title", ""),
            world_code=front_matter.get("world_code", ""),
            tier=int(front_matter.get("tier", "0") or "0"),
            confidence=front_matter.get("confidence", ""),
            source=front_matter.get("source", ""),
            retrieve_when=front_matter.get("retrieve_when", ""),
            do_not_retrieve_when=front_matter.get("do_not_retrieve_when", ""),
            content=self._strip_voice_unsafe_sections(remaining),
            source_file=file_path.name,
            force_llm_vote=front_matter.get("force_llm_vote", "").strip().lower().startswith("true"),
        )

    def create_documents(self, entries: list[StoryEntry]) -> list[Document]:
        """Convert story entries to LangChain documents for indexing."""
        documents = []

        for entry in entries:
            searchable_text = f"""
Story: {entry.story_title}
Tier: {entry.tier}
Confidence: {entry.confidence}

{entry.content}
"""

            metadata = {
                "story_title": entry.story_title,
                "tier": entry.tier,
                "confidence": entry.confidence,
                "source": entry.source,
                "retrieve_when": entry.retrieve_when,
                "do_not_retrieve_when": entry.do_not_retrieve_when,
                "source_file": entry.source_file,
                "force_llm_vote": entry.force_llm_vote,
            }

            documents.append(Document(page_content=searchable_text, metadata=metadata))

        return documents

    def index_stories(self, story_chunks_path: Path | None = None) -> FAISS:
        """Index all story chunk files and create FAISS vector store."""
        if story_chunks_path is None:
            story_chunks_path = settings.story_chunks_path

        entries = []
        for file_path in sorted(story_chunks_path.glob("*.md")):
            entry = self.parse_story_file(file_path)
            entries.append(entry)
            # See indexer.py's identical fix - native-script characters in a
            # title can crash this purely informational print on Windows'
            # cp1252 console, silently breaking indexing for that world.
            safe_title = entry.story_title.encode(
                sys.stdout.encoding or "utf-8", errors="replace"
            ).decode(sys.stdout.encoding or "utf-8")
            print(f"Parsed: {file_path.name} -> {safe_title}")

        documents = self.create_documents(entries)
        print(f"Created {len(documents)} story documents for indexing")

        vector_store = FAISS.from_documents(documents, self.embeddings)
        print("Story FAISS vector store created")

        return vector_store

    def save_index(self, vector_store: FAISS, path: Path) -> None:
        """Save the FAISS index to disk."""
        path.mkdir(parents=True, exist_ok=True)
        vector_store.save_local(str(path))
        print(f"Story index saved to {path}")

    def load_index(self, path: Path) -> FAISS:
        """Load a FAISS index from disk."""
        return FAISS.load_local(
            str(path),
            self.embeddings,
            allow_dangerous_deserialization=True,
        )
