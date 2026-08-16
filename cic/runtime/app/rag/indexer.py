"""Indexer for lexicon chunks - creates FAISS vector store."""

import re
import sys
from dataclasses import dataclass
from pathlib import Path

from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

from app.config import settings
from app.rag.embeddings import get_shared_embeddings
from app.rag.sections import (KEY_SOURCES_MARKERS, QUICK_MEANING_MARKERS,
                               extract_section)


def _null_sentinel(value: str) -> str:
    """S3.3 (Pass 1 R5): typed-null handling - an em-dash/dash sentinel in a
    condition field means 'no condition', and must parse to empty so every
    truthiness check downstream (no-conditions fast path, vote gating)
    treats it as the null it is, instead of as one-character condition
    text."""
    return "" if value.strip() in {"—", "–", "-"} else value


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
    force_llm_vote: bool = False
    quick_meaning: str = ""


class LexiconIndexer:
    """Indexes lexicon chunks into a FAISS vector store."""

    def __init__(self):
        # Shared across every world's indexer - see app/rag/embeddings.py
        # for why (this used to load its own separate copy every time).
        self.embeddings = get_shared_embeddings()

    def parse_front_matter(self, text: str) -> dict[str, str]:
        """Parse the retrieval front-matter from a lexicon file.

        Handles two conventions: fenced (front-matter inside a ``` code block,
        as Syriac/PAHC use) and plain (front-matter between the first two "---"
        lines at the top of the file, YAML-style, as Desert Monasticism uses).
        """
        front_matter = {}

        match = re.search(r"```\n(.*?)\n```", text, re.DOTALL)
        if match:
            block = match.group(1)
        else:
            parts = text.split("---", 2)
            if len(parts) < 3:
                return front_matter
            block = parts[1]

        lines = block.strip().split("\n")
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
                current_key = key.strip().lower().replace("-", "_").replace(" ", "_")
                current_value = [value.strip()]
            elif current_key and line.strip():
                # Continuation of previous value
                current_value.append(line.strip())

        # Save last key-value
        if current_key:
            front_matter[current_key] = " ".join(current_value).strip()

        return front_matter

    def parse_key_sources(self, content: str) -> str:
        """Extract the Key Sources section text, if present.

        Handles both the "## Key Sources" heading convention (Syriac/PAHC,
        content follows on later lines) and the inline "**Key Sources:**"
        bold-label convention (Desert Monasticism, content follows on the
        same line) - via app/rag/sections.py, which is now the single place
        those two conventions are described. This function's own copy of the
        boundary rule was correct; the retriever's parallel copy was not, and
        one shared primitive is what stops those two drifting apart again.
        """
        return extract_section(content, KEY_SOURCES_MARKERS)

    def parse_quick_meaning(self, content: str, fallback: str) -> str:
        """Extract the Quick Meaning section (S3.1 / Pass 1 R1).

        Handles both the "## Quick Meaning" heading convention (fenced
        front-matter worlds - the convention the old parallel parser in
        main.py silently dropped for 4 of 6 worlds) and the inline
        "**Quick Meaning:**" bold-label convention. Falls back to a
        truncated snippet of the entry's own content so the field is
        never empty (same contract main.py's tooltip needs).
        """
        text = extract_section(content, QUICK_MEANING_MARKERS)
        if text:
            return text
        snippet = " ".join(fallback.split())
        return snippet[:220].rsplit(" ", 1)[0] + "…" if len(snippet) > 220 else snippet

    def parse_lexicon_file(self, file_path: Path) -> LexiconEntry:
        """Parse a single lexicon file into a LexiconEntry."""
        content = file_path.read_text(encoding="utf-8")
        front_matter = self.parse_front_matter(content)
        key_sources = self.parse_key_sources(content)

        # Extract content after front-matter (everything after the ---)
        content_parts = content.split("---", 2)
        main_content = content_parts[2] if len(content_parts) > 2 else content

        # Parse list fields - handles both comma-separated ("SC, RT") and
        # bracket-separated ("[AS] [TC] [RT]") tag conventions
        def parse_list(value: str) -> list[str]:
            if not value:
                return []
            if "," in value:
                return [item.strip() for item in value.split(",")]
            bracketed = re.findall(r"\[([^\]]+)\]", value)
            if bracketed:
                return bracketed
            return [value.strip()]

        def parse_aliases(value: str) -> list[str]:
            """Parse the Aliases field, which is hand-written prose that can mix
            quoted English glosses (themselves containing commas, e.g. "mystery,")
            with bare transliterated terms, semicolon-separated sub-groups, and
            parenthetical asides - a naive comma-split shatters the quoted glosses
            into broken fragments (e.g. '"mystery' / '" "symbol"...'). Extract
            quoted phrases first, then split what's left on standard separators.
            """
            if not value:
                return []

            aliases = []

            # Quoted glosses first (may themselves contain a comma before the
            # closing quote, e.g. "mystery," "symbol" - two separate phrases)
            quoted = re.findall(r'"([^"]*)"', value)
            for phrase in quoted:
                cleaned = phrase.strip(" ,")
                if cleaned:
                    aliases.append(cleaned)

            # Remaining bare tokens: strip out the quoted spans already captured,
            # then split on the usual separators. A segment carrying a
            # parenthetical qualifier (e.g. "illumination (baptismal)") is
            # dropped WHOLE, never reduced to its bare head - the qualifier is
            # the author's own signal that the bare form is unsafe as an alias
            # for this term (it collides with another term's namespace), so
            # silently emitting it defeats the reason it was written qualified.
            remainder = re.sub(r'"[^"]*"', "", value)
            for chunk in re.split(r"[;,/]", remainder):
                if "(" in chunk or ")" in chunk:
                    continue
                cleaned = chunk.strip(" /")
                if len(cleaned) > 1:
                    aliases.append(cleaned)

            return aliases

        tier_raw = front_matter.get("tier", "1").strip("[]").strip()

        main_content = main_content.strip()
        return LexiconEntry(
            # An ambient chunk titles itself Ambient-Title instead of Term;
            # the title fills the same retrieval-surface slot.
            term=front_matter.get("term", "")
                 or front_matter.get("ambient_title", ""),
            world_code=front_matter.get("world_code", "syr"),
            tier=int(tier_raw) if tier_raw.isdigit() else 1,
            tags=parse_list(front_matter.get("tags", "")),
            aliases=parse_aliases(front_matter.get("aliases", "")),
            related_terms=parse_list(front_matter.get("related_terms", "")),
            retrieve_when=_null_sentinel(front_matter.get("retrieve_when", "")),
            do_not_retrieve_when=_null_sentinel(front_matter.get("do_not_retrieve_when", "")),
            content=main_content,
            source_file=file_path.name,
            key_sources=key_sources,
            force_llm_vote=front_matter.get("force_llm_vote", "").strip().lower().startswith("true"),
            quick_meaning=self.parse_quick_meaning(content, main_content),
        )

    def create_documents(self, entries: list[LexiconEntry]) -> list[Document]:
        """Convert lexicon entries to LangChain documents for indexing."""
        documents = []

        for entry in entries:
            # S3.1 / Pass 1 R1: embed the RETRIEVAL SURFACE - the fields
            # authors actually write for retrieval - not the chunk body.
            # Before this change the body was embedded and the model's
            # 256-token window truncated 94.4% of all 162 chunks (measured:
            # truncation_report_2026-07-27.json; the R1 surface maxes at
            # ~183 tokens, zero truncation). Retrieve-When enters the
            # embedded text for the first time. The body stays as payload
            # in metadata["content"] - consumers read it from there.
            searchable_text = f"""
Term: {entry.term}
Aliases: {', '.join(entry.aliases)}
Related: {', '.join(entry.related_terms)}
Retrieve when: {entry.retrieve_when}
Quick meaning: {entry.quick_meaning}
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
                "force_llm_vote": entry.force_llm_vote,
                "quick_meaning": entry.quick_meaning,
                "content": entry.content,
            }

            documents.append(Document(page_content=searchable_text, metadata=metadata))

        return documents

    def index_lexicon(self, lexicon_path: Path | None = None) -> FAISS:
        """Index all lexicon files and create FAISS vector store."""
        if lexicon_path is None:
            lexicon_path = settings.lexicon_chunks_path

        # Parse all lexicon files - plus the sibling ambient_chunks
        # directory where a world has one (Native-Ambient texture,
        # redesign step 5, 2026-08-14). Ambient chunks share the fenced
        # front-matter format and ride the SAME index and retrieval path:
        # no new per-turn calls, and the chunk's own Register line and
        # Voice Rule travel inside its content payload.
        chunk_files = sorted(lexicon_path.glob("*.md"))
        ambient_dir = lexicon_path.parent / "ambient_chunks"
        if ambient_dir.is_dir():
            chunk_files += sorted(ambient_dir.glob("*.md"))
        entries = []
        for file_path in chunk_files:
            entry = self.parse_lexicon_file(file_path)
            entries.append(entry)
            # Some terms contain native-script characters (e.g. Syriac) the
            # Windows console's default cp1252 encoding can't represent -
            # printing them directly crashed indexing with a bare
            # UnicodeEncodeError, silently swallowed by the startup
            # try/except and leaving that world's lexicon retrieval broken
            # on every subsequent request (it kept retrying and re-crashing
            # rather than ever completing). errors="replace" keeps this
            # purely informational print from ever taking down indexing.
            safe_term = entry.term.encode(
                sys.stdout.encoding or "utf-8", errors="replace"
            ).decode(sys.stdout.encoding or "utf-8")
            print(f"Parsed: {file_path.name} -> {safe_term}")

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
