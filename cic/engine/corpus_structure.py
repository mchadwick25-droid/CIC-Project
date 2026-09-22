#!/usr/bin/env python3
"""The corpus's structural outline - what works are in which volume, and where.

WHY THIS EXISTS. The assignment job (BRIEF-corpus-assignment-thread.md) is
primarily a parsing exercise, and the thing being parsed is
176 MB of CCEL ThML across 46 volumes, several of them 5-6 MB. Nothing can
read that directly. What the job actually needs is not the text but the
SHELF: which works sit in which volume, under which author section, how long
each is. That is mechanically derivable from the markup, and this derives it.

`corpus_authors.py` already reads `<DC.Creator>` and `<div1 title=...>` for
attribution, and stops there because attribution is all it needed. One level
down is where the works are, and the level differs by volume family - which
is itself a finding, not a nuisance:

    ANF   div1 = AUTHOR section  ("CLEMENT OF ALEXANDRIA")
          div2 = WORK            ("The Stromata")
    NPNF  div1 = WORK or front matter ("Four Discourses Against the Arians")
          div2 = chapter, or in npnf208 an individual LETTER (405 of them)

So this reports the tree with word counts and lets the reader judge, rather
than asserting a rule that is wrong for half the corpus. A section carrying
380,000 words is a body of work; one carrying 300 is a preface.

APPARATUS IS MARKED, NOT DROPPED. Title pages, prefaces, prolegomena, indexes
and editorial notes are flagged `apparatus` and kept. Dropping them would hide
the fact that npnf204's "Prolegomena" is tens of thousands of words of
nineteenth-century biography sitting in the same volume as Athanasius' own
text - exactly the confusion that had corpus_probe ranking a contents page top
for desert's Christology.

    python cic/engine/corpus_structure.py                    # every volume, outline
    python cic/engine/corpus_structure.py npnf204            # one volume
    python cic/engine/corpus_structure.py --json > out.json  # machine-readable
    python cic/engine/corpus_structure.py --write            # cic/texts/STRUCTURE.md
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
TEXTS_DIR = REPO_ROOT / "cic" / "texts"

_DIV = re.compile(r'<div(?P<level>[1-3])\b(?P<attrs>[^>]*)>')
_TITLE = re.compile(r'\btitle="([^"]*)"')
_TAG = re.compile(r"<[^>]+>")

# Front matter and editorial apparatus. These are real sections with real word
# counts - some very large - and calling them works would be wrong.
_APPARATUS = re.compile(
    r"^(title page|second title page|editorial preface|preface|prolegomena|"
    r"introductory (note|notice)|translator'?s? (preface|note)|contents|"
    r"table of contents|index|indexes|indices|general index|bibliograph|"
    r"chronological table|genealogical tables?|errata|advertisement|"
    r"elucidations?|addenda|memoir|biographical synopsis)\b", re.I)

# `appendix` needs its own rule. Matching it as a prefix marked
# Pseudo-Tertullian's *Against All Heresies* and npnf214's Trullan canonical
# appendix as editorial matter - both ancient texts that CCEL merely shelves
# under an "Appendix" heading. Two workers on the 2026-08-26 assignment run
# caught it by eye and assigned them anyway. So an appendix is apparatus only
# when the title is JUST that word (plus numbering or punctuation); an
# appendix that names a work is a work.
_BARE_APPENDIX = re.compile(r"^appendix\b[\s.:;,–—-]*(?:[ivxl]+|\d+)?[\s.:;,]*$", re.I)


def _unescape(text: str) -> str:
    for entity, char in (("&amp;", "&"), ("&lt;", "<"), ("&gt;", ">"),
                         ("&quot;", '"'), ("&apos;", "'")):
        text = text.replace(entity, char)
    return text


def outline(path: Path, max_level: int = 2) -> list[dict]:
    """Sections down to `max_level`, each with the word count of its OWN text.

    Word counts are per span-between-markers, so a div1's `words` is the prose
    before its first div2, not the whole subtree. `subtree_words` carries the
    total. Both matter: the first says how much sits directly under a heading,
    the second says how big the work is.
    """
    raw = path.read_text(encoding="utf-8", errors="replace")
    marks = []
    for m in _DIV.finditer(raw):
        title_match = _TITLE.search(m.group("attrs"))
        marks.append((m.start(), m.end(), int(m.group("level")),
                      _unescape(title_match.group(1)) if title_match else ""))

    if not marks:                                  # a plain .txt with no markup
        words = len(_TAG.sub(" ", raw).split())
        return [{"level": 0, "title": path.stem, "words": words,
                 "subtree_words": words, "apparatus": False, "path": "1"}]

    sections = []
    for i, (_, end, level, title) in enumerate(marks):
        stop = marks[i + 1][0] if i + 1 < len(marks) else len(raw)
        sections.append({"level": level, "title": title.strip(),
                         "words": len(_TAG.sub(" ", raw[end:stop]).split())})

    # subtree_words: a section owns every following section deeper than it.
    for i, sec in enumerate(sections):
        total = sec["words"]
        for nxt in sections[i + 1:]:
            if nxt["level"] <= sec["level"]:
                break
            total += nxt["words"]
        sec["subtree_words"] = total

    # A dotted path ("2.3") so an assignment can name a locus precisely.
    trail: list[int] = []
    for sec in sections:
        depth = sec["level"]
        if len(trail) >= depth:
            trail = trail[:depth]
            trail[depth - 1] += 1
        else:
            trail = trail + [1] * (depth - len(trail))
        sec["path"] = ".".join(str(n) for n in trail)
        sec["apparatus"] = bool(_APPARATUS.match(sec["title"])
                                or _BARE_APPENDIX.match(sec["title"]))

    return [s for s in sections if s["level"] <= max_level]


def suspect_apparatus(path: Path, factor: int = 10, floor: int = 20_000) -> list[dict]:
    """Apparatus sections whose subtree dwarfs their own text - probably
    containers, possibly mismarked.

    `npnf209` nests every one of Hilary's works under a div1 titled "Title
    Page", so the subtree rule reports ~300k words of real text as apparatus.
    `npnf204`'s Prolegomena has the same shape - near-zero own text, a huge
    subtree - and IS apparatus all the way down.

    Nothing in the markup separates the two: the difference is whether the
    children are editorial, and only a reader can say. So this reports the
    shape and refuses to guess, which is how the assignment run's workers
    actually caught it.
    """
    return [s for s in outline(path, max_level=3)
            if s["apparatus"] and s["subtree_words"] > floor
            and s["subtree_words"] > factor * max(s["words"], 1)]


def body_words(path: Path) -> tuple[int, int]:
    """(words outside apparatus, apparatus words) for the whole file.

    Computed at full depth and subtracting whole apparatus SUBTREES, because
    an apparatus section's own `words` is near zero when its content hangs off
    children - a Prolegomena carrying four words directly and 90,000 in its
    chapters would otherwise read as negligible.
    """
    full = outline(path, max_level=3)
    apparatus = 0
    skip_above = None
    for sec in full:
        if skip_above is not None and sec["level"] > skip_above:
            continue
        skip_above = None
        if sec["apparatus"]:
            apparatus += sec["subtree_words"]
            skip_above = sec["level"]
    total = sum(s["words"] for s in full)
    return max(total - apparatus, 0), apparatus


def volumes() -> list[Path]:
    return sorted(p for p in TEXTS_DIR.iterdir() if p.suffix in (".xml", ".txt"))


def render(paths: list[Path], max_level: int = 2) -> str:
    out = ["# Corpus structure - what is in each volume, and how big\n"]
    out.append(
        "Generated by `cic/engine/corpus_structure.py` from each file's own ThML `<div>` "
        "markup. Nothing here is supplied from outside the files.\n")
    out.append(
        "**Read the level, not the label.** In the ANF volumes `div1` is an *author section* "
        "and `div2` is a *work*; in most NPNF volumes `div1` is a work and `div2` is a chapter "
        "(and in `npnf208`, an individual letter). Word counts are the reliable signal: a "
        "section carrying 380,000 words is a body of work, one carrying 300 is a preface.\n")
    out.append(
        "Sections matching front-matter and editorial patterns are marked *(apparatus)* and "
        "kept rather than dropped - `npnf204`'s Prolegomena is tens of thousands of words of "
        "nineteenth-century biography sitting in the same file as Athanasius' own text, and "
        "hiding that is how a contents page ends up ranked top for a Christology query.\n")
    for path in paths:
        secs = outline(path, max_level)
        body, apparatus = body_words(path)
        out.append(f"\n## `{path.name}`\n")
        out.append(f"{len(secs)} section(s) to level {max_level} · "
                   f"~{body:,} words of text · ~{apparatus:,} words of apparatus\n")
        for s in suspect_apparatus(path):
            out.append(f"> ⚠ `{s['path']}` **{s['title'] or '—'}** is marked apparatus but carries "
                       f"{s['subtree_words']:,} words in its subtree against {s['words']:,} of its "
                       f"own. It may be a container holding real works rather than editorial "
                       f"matter — read it before skipping it.\n")
        out.append("| path | lvl | words | subtree | section |")
        out.append("|---|---:|---:|---:|---|")
        for s in secs:
            label = (s["title"] or "—").replace("|", "\\|")
            if s["apparatus"]:
                label = f"*{label}* (apparatus)"
            out.append(f"| `{s['path']}` | {s['level']} | {s['words']:,} | "
                       f"{s['subtree_words']:,} | {label} |")
    return "\n".join(out) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="python cic/engine/corpus_structure.py")
    parser.add_argument("volume", nargs="*", help="filename or prefix; default all")
    parser.add_argument("--level", type=int, default=2, help="deepest div level to report (default 2)")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--write", action="store_true", help="write cic/texts/STRUCTURE.md")
    args = parser.parse_args(argv)

    paths = volumes()
    if args.volume:
        wanted = tuple(args.volume)
        paths = [p for p in paths if p.name.startswith(wanted) or p.name in wanted]
        if not paths:
            print(f"no volume matching {args.volume}", file=sys.stderr)
            return 1

    if args.json:
        print(json.dumps({p.name: outline(p, args.level) for p in paths}, indent=2))
        return 0

    text = render(paths, args.level)
    if args.write:
        (TEXTS_DIR / "STRUCTURE.md").write_text(text, encoding="utf-8")
        print(f"wrote {TEXTS_DIR / 'STRUCTURE.md'} ({len(paths)} volume(s))")
        return 0
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
