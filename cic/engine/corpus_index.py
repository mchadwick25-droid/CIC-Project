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
_DIV/_TITLE/_TAG/_unescape regexes already handle nested tag structures
correctly (a naive tag-strip truncates against nested <note><p
class="endnote">...</p></note> structures - see cic/texts/README.md's
anf01 entry). Where this module's needs diverge from corpus_structure.py's
own (it reports word COUNTS per section; this needs the actual TEXT and
the file's own id= attribute, neither of which outline() keeps), the walk
itself stays the same shape.

WHAT COUNTS AS A PASSAGE UNIT. For ThML/XML files: every div's own direct
text - the span between where it opens and the next div marker of ANY
level, matching exactly what corpus_structure.py's `words` field already
measures per section (not `subtree_words`). A leaf div's "own text" is
everything in it, since nothing follows before its next sibling; a
container div's "own text" is whatever prose sits before its first child
(often little or nothing) - both are correct, and a near-empty container
row is harmless in FTS5, just unlikely to match anything.

PLAIN-TEXT FILES (no div markup): split on the file's own heading lines,
falling back to paragraphs where it has none. A heading line is a short,
uppercase-only line naming a structural division - "LETTER I.", "SESSION
IV.", "CANONS AND DECREES" - the plain-text analogue of an XML volume's
own `<div title=...>`. Deliberately no fixed vocabulary ("CHAPTER",
"LETTER", ...): this corpus spans letters, sermons, conciliar acts,
chronicles and catechisms, each with its own heading words, so the check
is on SHAPE (short, all-caps, no lowercase) rather than a word list.

A real heading names its own moment once, or a couple of times (a table
of contents entry plus the body heading) - a candidate line recurring
often across a volume is page furniture instead: CCEL/archive.org scans
print a running title on every page, frequently with a page number
appended or prepended that differs page to page ("COUNCIL OF TRENT. XV"
/ "XVI HISTORY OF THE COUNCIL OF TRENT" on facing verso/recto pages).
`_heading_lines()` strips a leading or trailing page-number token before
counting repeats, so both forms of the same running header collapse to
the same key and both get filtered - confirmed against
council-of-trent_canons-and-decrees_waterworth1848.txt, whose own running
header this way was caught and excluded rather than fragmenting the
volume into one unit per page.

A file with no real headings at all (many of this corpus's continuous
Latin critical-edition texts have none) falls back to one unit per
blank-line-delimited paragraph - finer-grained than the single whole-file
blob this used to return, the same reason ThML volumes get one unit per
div rather than one per file.

Every plain-text unit's `locus` is `line<N>`, the 1-based line its own
first line sits on - not a synthetic index, so a hit is directly
navigable back to the source file. NO TEXT IS LOST by this split: the
heading-unit and paragraph-unit ranges each partition the file's own text
completely (every byte belongs to exactly one unit, including the
heading line's own words, which stay in the unit's `text` in addition to
its `title`) - proven directly in tests_corpus_index.py by reassembling
every unit's text and diffing it, whitespace-normalized, against the
whole file.

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

# Plain-text heading detection (no div markup to key off). Shape-based, not
# a fixed word list - see the module docstring's own "PLAIN-TEXT FILES"
# section for why.
_HEADING_MAX_CHARS = 100
_HEADING_MAX_WORDS = 12
_HEADING_ROMAN_ONLY = re.compile(r"^[IVXLCDM]+$")
_HEADING_WORD_PUNCT = ".,:;()[]-–—'\""
_LEADING_NUMERAL_TOKEN = re.compile(r"^([IVXLCDM]+|\d+)\b[.,:;)\]\-]*\s*")
_TRAILING_NUMERAL_TOKEN = re.compile(r"\s*[.,:;(\[\-]*\b([IVXLCDM]+|\d+)$")
# A real heading names its own moment once, or a couple of times (a table
# of contents entry plus the body heading itself); a candidate recurring
# more often than this across one volume is a running header/footer, not
# a structural boundary.
_RUNNING_HEADER_MIN_REPEATS = 3


def _is_heading_candidate(line: str) -> bool:
    s = line.strip()
    if not s or len(s) > _HEADING_MAX_CHARS:
        return False
    if any(c.islower() for c in s):
        return False
    if not any(c.isalpha() for c in s):
        return False
    words = s.split()
    if len(words) > _HEADING_MAX_WORDS:
        return False
    stripped_words = [w.strip(_HEADING_WORD_PUNCT) for w in words]
    # At least one real word: 3+ characters, containing a letter (not a
    # bare page-locator number or number range - an index page is exactly
    # where those show up, "704-709, 711"), and not a bare roman-numeral
    # page number sitting alone on its own line ("XVI" with nothing else).
    return any(len(w) >= 3 and any(c.isalpha() for c in w) and not _HEADING_ROMAN_ONLY.match(w)
               for w in stripped_words)


def _heading_dedup_key(line: str) -> str:
    s = re.sub(r"\s+", " ", line.strip().upper())
    s = _LEADING_NUMERAL_TOKEN.sub("", s)
    s = _TRAILING_NUMERAL_TOKEN.sub("", s)
    return s.strip()


def _heading_lines(text: str) -> list[tuple[int, str]]:
    """(0-based line index, whitespace-normalized heading text) for every
    real heading line in `text` - heading-candidate lines minus running
    headers/footers. Internal whitespace (OCR justification often spaces a
    heading's own words several characters apart) is collapsed the same
    way a unit's own `text` field already collapses it, so `title` and the
    start of that unit's `text` read as the same string, not two different
    spacings of it."""
    lines = text.split("\n")
    candidates = [(i, re.sub(r"\s+", " ", ln.strip())) for i, ln in enumerate(lines) if _is_heading_candidate(ln)]
    counts: dict[str, int] = {}
    for _, heading_text in candidates:
        key = _heading_dedup_key(heading_text)
        counts[key] = counts.get(key, 0) + 1
    return [(i, heading_text) for i, heading_text in candidates
            if counts[_heading_dedup_key(heading_text)] <= _RUNNING_HEADER_MIN_REPEATS]


def _heading_units(text: str) -> list[dict] | None:
    """Heading-delimited units, or None when `text` has no real headings at
    all (the caller then falls back to _paragraph_units). Each unit's text
    runs from its own heading line (inclusive - the heading is real, printed
    prose, not markup, so it stays in `text` as well as `title`) up to the
    next heading line; whatever precedes the first heading becomes its own
    untitled unit, so nothing in the file is left out of every unit."""
    heads = _heading_lines(text)
    if not heads:
        return None

    # Offsets must come from the same split _heading_lines() itself used
    # (text.split("\n")) to index its own heading lines against, not
    # str.splitlines() - splitlines() also breaks on \x0c (form feed) and
    # several other line-boundary characters, which this OCR'd corpus
    # carries as real page-break artifacts (one volume alone has 549). A
    # form feed makes splitlines() produce a different, longer line list
    # than split("\n"), so offsets built from it drift out of step with
    # the heading indices and attach headings to the wrong text.
    lines = text.split("\n")
    offsets = [0] * (len(lines) + 1)
    pos = 0
    for i, ln in enumerate(lines):
        offsets[i] = pos
        pos = min(pos + len(ln) + 1, len(text))
    offsets[len(lines)] = len(text)

    units = []
    first_line_idx = heads[0][0]
    if first_line_idx > 0:
        preamble = re.sub(r"\s+", " ", text[0:offsets[first_line_idx]]).strip()
        if preamble:
            units.append({"locus": "line1", "title": "", "apparatus": False, "text": preamble})

    for k, (line_idx, heading_text) in enumerate(heads):
        start = offsets[line_idx]
        stop = offsets[heads[k + 1][0]] if k + 1 < len(heads) else len(text)
        unit_text = re.sub(r"\s+", " ", text[start:stop]).strip()
        if not unit_text:
            continue  # only possible if the heading itself is blank, which _is_heading_candidate excludes
        is_apparatus = bool(cs._APPARATUS.match(heading_text) or cs._BARE_APPENDIX.match(heading_text))
        units.append({
            "locus": f"line{line_idx + 1}",
            "title": heading_text,
            "apparatus": is_apparatus,
            "text": unit_text,
        })
    return units


def _paragraph_units(text: str) -> list[dict]:
    """Fallback for a plain-text file with no usable heading structure at
    all: one unit per blank-line-delimited paragraph, addressed by the
    1-based line its own first line sits on. No `title` - a paragraph
    names nothing the way a heading does."""
    lines = text.split("\n")
    units = []
    para_start = None
    para_lines: list[str] = []

    def flush(start_line_no):
        unit_text = re.sub(r"\s+", " ", " ".join(para_lines)).strip()
        if unit_text:
            units.append({"locus": f"line{start_line_no}", "title": "", "apparatus": False, "text": unit_text})

    for i, line in enumerate(lines):
        if line.strip():
            if para_start is None:
                para_start = i + 1
            para_lines.append(line)
        else:
            if para_lines:
                flush(para_start)
            para_start, para_lines = None, []
    if para_lines:
        flush(para_start)
    return units


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
        # No div markup - a plain-text volume (or, in principle, an XML
        # file with none of its own div markers). Split on headings, or
        # paragraphs where there are none of those either.
        text = cs._strip_tags_if_markup(path, raw)
        units = _heading_units(text)
        if units is not None:
            return units
        units = _paragraph_units(text)
        if units:
            return units
        # Truly empty or whitespace-only file - nothing to split.
        return [{"locus": "whole-file", "title": path.stem, "apparatus": False, "text": text.strip()}]

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
    """Ranked FTS5 search. With `entry`, the entry's corpus-map file set is
    applied inside the query (`file IN (...)` alongside MATCH), so bm25
    ranking and LIMIT run only over that world's own passages."""
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
