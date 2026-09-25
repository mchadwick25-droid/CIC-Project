#!/usr/bin/env python3
"""Full-text search over cic/texts/ - cic/texts/INDEX.sqlite.

WHY. corpus_probe.py already says it plainly in its own docstring: a
builder's tool, not a runtime path. This is that same idea pushed one step
further - up to now finding a passage inside a 181MB, 64-file corpus has
meant grep (exact-string only, no ranking, no snippet) or opening a file
and reading it. SQLite's FTS5 gives phrase search, ranking, and a snippet
around the match, entirely offline, no server, no dependency this sandbox
can't already satisfy.

REUSES corpus_structure.py's OWN PARSING, DELIBERATELY. That module's
_DIV/_TITLE/_TAG/_unescape regexes already worked through the real bugs
this kind of parsing hits - cic/texts/README.md's anf01 entry documents
catching a naive tag-strip truncating text against nested <note><p
class="endnote">...</p></note> structures, live, before anything was
committed. Re-deriving that from scratch here would risk repeating a
mistake this project already paid to fix once. Where this module's needs
diverge from corpus_structure.py's own (it reports word COUNTS per
section; this needs the actual TEXT and the file's own id= attribute,
neither of which outline() keeps), the walk itself stays the same shape.

WHAT COUNTS AS A PASSAGE UNIT. For ThML/XML files: every div's own direct
text - the span between where it opens and the next div marker of ANY
level, matching exactly what corpus_structure.py's `words` field already
measures per section (not `subtree_words`). A leaf div's "own text" is
everything in it, since nothing follows before its next sibling; a
container div's "own text" is whatever prose sits before its first child
(often little or nothing) - both are correct, and a near-empty container
row is harmless in FTS5, just unlikely to match anything. For plain-text
files with no div markup at all: one whole-file unit, the same fallback
outline() already established for this exact case.

CANONICAL ADDRESS. cic:<filename>:<locus>, matching WORKS.yaml and
cic/corpus-map/README.md's "Canonical addresses" section. <locus> is the
div's own id= attribute where the file supplies one (stable across a
re-export the way a computed position never is), or "whole-file" for
plain text.

BOUNDARY WITH THIS PROJECT'S OWN DISCIPLINE ON INTERPRETIVE WORK. This
index returns LOCATIONS, ranked by keyword match - it has no concept of
quote-worthiness, story tier, or glossary relevance, and adds none. A hit
is a place to go read, not a decision about what matters there; that
judgment stays where this project's methodology already puts it, inside
a specific world's own build thread. corpus_probe.py already draws this
same line for its own, cruder ranking; this module draws it the same way.

Usage:
  python cic/engine/corpus_index.py --build              # (re)build cic/texts/INDEX.sqlite
  python cic/engine/corpus_index.py "invisible church"   # search
  python cic/engine/corpus_index.py "logismoi" --entry desert-monasticism
  python cic/engine/corpus_index.py "logismoi" --limit 5
"""
from __future__ import annotations

import argparse
import re
import sqlite3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import corpus_structure as cs  # noqa: E402  (reuses _DIV, _TITLE, _TAG, _unescape, _strip_tags_if_markup - see docstring)

REPO_ROOT = Path(__file__).resolve().parents[2]
TEXTS_DIR = REPO_ROOT / "cic" / "texts"
MAP_DIR = REPO_ROOT / "cic" / "corpus-map"
DB_PATH = TEXTS_DIR / "INDEX.sqlite"

_ID = re.compile(r'\bid="([^"]*)"')


def passage_units(path: Path) -> list[dict]:
    """Every passage unit in one file: address, title, apparatus flag, text.
    Mirrors corpus_structure.outline()'s own marker-walk, extended to keep
    the id= attribute and the actual text span instead of just a count."""
    raw = path.read_text(encoding="utf-8", errors="replace")
    marks = []
    for m in cs._DIV.finditer(raw):
        title_m = cs._TITLE.search(m.group("attrs"))
        id_m = _ID.search(m.group("attrs"))
        marks.append((m.start(), m.end(),
                      cs._unescape(title_m.group(1)) if title_m else "",
                      id_m.group(1) if id_m else None))

    if not marks:
        text = cs._strip_tags_if_markup(path, raw).strip()
        return [{"locus": "whole-file", "title": path.stem, "apparatus": False, "text": text}]

    units = []
    for i, (_, end, title, div_id) in enumerate(marks):
        stop = marks[i + 1][0] if i + 1 < len(marks) else len(raw)
        text = re.sub(r"\s+", " ", cs._TAG.sub(" ", raw[end:stop])).strip()
        if not text:
            continue  # a pure-container div with nothing of its own - not a searchable unit
        is_apparatus = bool(cs._APPARATUS.match(title.strip()) or cs._BARE_APPENDIX.match(title.strip()))
        units.append({
            "locus": div_id or f"pos{i}",  # pos<i> is a last-resort fallback, not expected
            "title": title.strip(),
            "apparatus": is_apparatus,
            "text": text,
        })
    return units


def build(db_path: Path = DB_PATH) -> tuple[int, int]:
    """(Re)builds the index from scratch - cheap enough (64 files) that
    incremental update isn't worth the complexity; matches texts_registry.py
    and corpus_structure.py's own always-regenerate-fresh convention."""
    if db_path.exists():
        db_path.unlink()
    conn = sqlite3.connect(db_path)
    conn.execute("""
        CREATE VIRTUAL TABLE passages USING fts5(
            address, file UNINDEXED, title, text,
            apparatus UNINDEXED, tokenize='porter unicode61'
        )
    """)
    n_files = 0
    n_units = 0
    for path in cs.volumes():
        n_files += 1
        for u in passage_units(path):
            address = f"cic:{path.name}:{u['locus']}"
            conn.execute(
                "INSERT INTO passages (address, file, title, text, apparatus) VALUES (?, ?, ?, ?, ?)",
                (address, path.name, u["title"], u["text"], int(u["apparatus"])),
            )
            n_units += 1
    conn.commit()
    conn.close()
    return n_files, n_units


def files_for_entry(entry_id: str) -> set[str] | None:
    """Filenames assigned to one census entry, from its corpus-map bucket -
    None if the bucket doesn't exist, so callers can distinguish "no such
    entry" from "entry exists but nothing assigned yet." """
    bucket = MAP_DIR / f"{entry_id}.yaml"
    if not bucket.exists():
        return None
    import yaml
    data = yaml.safe_load(bucket.read_text(encoding="utf-8")) or {}
    return {w["source_file"] for w in (data.get("works") or []) if w.get("source_file")}


def search(query: str, entry: str | None = None, limit: int = 10, db_path: Path = DB_PATH) -> list[dict]:
    """Scoped search applies the world's own file set INSIDE the query (a
    `file IN (...)` clause alongside the MATCH), not as a filter after a
    capped fleet-wide fetch. The earlier shape ran the bm25-ranked fetch
    first, capped at limit*5 hits across the WHOLE corpus, and only then
    dropped everything outside scope - so a world whose own texts rank
    below other worlds' texts for a given query could lose every one of
    its real hits before scoping ever saw them ("chalice" --entry hussite
    returned "no matches" at the default limit despite Hussite Wars
    containing the word 13 times, and only appeared at --limit 200). With
    scope applied inside the query, ranking and LIMIT operate only over
    the real candidate set, so the requested limit means what it says."""
    if not db_path.exists():
        raise SystemExit(f"{db_path} does not exist yet - run with --build first")
    scope = None
    if entry:
        scope = files_for_entry(entry)
        if scope is None:
            raise SystemExit(f"no corpus-map bucket for entry {entry!r} "
                             f"(checked {MAP_DIR / (entry + '.yaml')})")
        if not scope:
            return []  # a real bucket with nothing assigned yet - nothing to search, not an error
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    if scope is None:
        sql = ("SELECT address, file, title, apparatus, "
               "snippet(passages, 3, '[', ']', '...', 12) AS snip, "
               "bm25(passages) AS score "
               "FROM passages WHERE passages MATCH ? ORDER BY score LIMIT ?")
        params = (query, limit)
    else:
        placeholders = ", ".join("?" * len(scope))
        sql = ("SELECT address, file, title, apparatus, "
               "snippet(passages, 3, '[', ']', '...', 12) AS snip, "
               "bm25(passages) AS score "
               f"FROM passages WHERE passages MATCH ? AND file IN ({placeholders}) "
               "ORDER BY score LIMIT ?")
        params = (query, *sorted(scope), limit)
    rows = conn.execute(sql, params).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("query", nargs="?", help="FTS5 query (phrases in double quotes, AND/OR/NOT supported)")
    ap.add_argument("--build", action="store_true", help="(re)build cic/texts/INDEX.sqlite")
    ap.add_argument("--entry", help="scope results to one corpus-map census entry (e.g. desert-monasticism)")
    ap.add_argument("--limit", type=int, default=10)
    args = ap.parse_args(argv)

    if args.build:
        n_files, n_units = build()
        print(f"built {DB_PATH}: {n_files} file(s), {n_units} passage unit(s)")
        if not args.query:
            return 0

    if not args.query:
        ap.error("a query is required unless using --build alone")

    hits = search(args.query, entry=args.entry, limit=args.limit)
    if not hits:
        print("no matches")
        return 0
    for h in hits:
        flag = " [apparatus]" if h["apparatus"] else ""
        print(f"{h['address']}{flag}")
        print(f"  {h['title']}")
        print(f"  {h['snip']}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
