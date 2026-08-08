"""Voice Rebuild Phase 0.2 - the build-time apparatus leak gate.

Scans every lexicon and story chunk's SERIALIZED body - the same text
app/rag/retriever.py's get_context_for_response and app/rag/
story_retriever.py actually hand to a Representative, not the raw file -
for internal build-process language that should never reach generation.

Reuses the real parsing methods (LexiconIndexer.parse_lexicon_file,
StoryIndexer.parse_story_file) and the shared section primitives
(app.rag.sections.truncate_at/excise_section - the exact functions
retriever.py itself calls) rather than a third independent
reimplementation of front-matter parsing, per sections.py's own stated
rule ("the fix is not a fourth copy"). The indexer classes are
instantiated via object.__new__ to skip their normal __init__ (which
eagerly loads the shared HuggingFace embedding model) - parsing never
touches self.embeddings, only the FAISS-building methods this gate
never calls do.

Two tiers, per Design §2 Layer 5 / Blueprint 0.2:

  HARD-FAIL - unambiguous apparatus that must never ship: a Final
  Assembly Instruction block reaching the model at all (should be
  impossible after Phase 0.2's sections.py/story_indexer.py fixes -
  this gate is what catches a REGRESSION, not what fixes today's known
  cases, which are already closed at the source); template/builder-
  process references (L4-Templates, "per Template", "No brackets or
  builder notes remain"); and gravity-analysis vocabulary (gravity N,
  Doc_/Force references, Tensional/Primary/Supporting gravity)
  specifically INSIDE Ecological Function / Formation Ecology
  Connection bodies - the two fields Phase 2 authors fresh under Mark's
  2026-08-08 scope decision (extend the prose-style license to these
  fields), so this is exactly where a rewrite backsliding into
  apparatus vocabulary must be caught before it ships.

  REPORT-ONLY - Usage Guidance content (deliberately serialized; the
  story indexer's own documented policy, since it also carries real
  anti-fabrication instruction no chunk can lose) and any apparatus-
  pattern hit outside the sections above (background signal for Phase 2
  authoring passes, never a build blocker).

Run: python wrs/gates/leak_gate.py [--data-dir <path>]
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
sys.path.insert(0, str(BACKEND))

from app.rag.indexer import LexiconIndexer  # noqa: E402
from app.rag.sections import (KEY_SOURCES_MARKERS, QUICK_MEANING_MARKERS,  # noqa: E402
                              TRAILING_APPARATUS_MARKERS, excise_section,
                              truncate_at)
from app.rag.story_indexer import StoryIndexer  # noqa: E402

WORLD_DIRS = {
    "desert_world": "desert-monasticism",
    "pahc_world": "post-apostolic-house-church",
    "syriac_world": "syriac-edessa-nisibis",
    "alexandria_world": "alexandria-catechetical",
    "imperial_juridical_world": "imperial-juridical-christianity",
    "hieronymian_world": "hieronymian-ascetic-literary",
}

# HARD-FAIL, unrestricted (never voice-safe anywhere in a serialized body):
_HARD_FAIL_ANYWHERE = re.compile(
    r"Final Assembly Instruction|L4-Templates|per Template|"
    r"Completed per `|No brackets or builder notes remain|CT tag (?:not )?applied",
    re.I)

# HARD-FAIL, scoped: gravity/Doc_/Force apparatus is only disallowed
# inside the two fields Phase 2 authors fresh under the license.
_HARD_FAIL_SCOPED_SECTIONS = ("Ecological Function", "Formation Ecology Connection")
_HARD_FAIL_SCOPED_PATTERN = re.compile(
    r"\bgravity \d|\bgravit(?:y|ies) [A-Z]?\d|\bG0\d\b|Doc_0\d|Force \d[A-C]|"
    r"\bTensional\b|\bPrimary grav|\bSupporting grav", re.I)

# REPORT-ONLY: the Research-stage leak audit's own refined apparatus
# pattern class (leak_audit_instrument.py's APPARATUS regex), reused
# per Blueprint 0.2 - the parts not already promoted to hard-fail above,
# for background visibility outside the hard-fail scope.
_REPORT_ONLY_PATTERN = re.compile(
    r"\bStrand [A-C]\b|\bC\d\b(?= \()|\bCT\b(?:\s+(?:tag|Contest))?|"
    r"Contest Type|Reciprocity Note|\bFLAG-\d+|builder(?:'s)? note|"
    r"\bTier[- ][123]\b|\bcandidate\b.{0,80}\btest(?:ed|ing)\b|"
    r"Construction Framework|Source Ecology", re.I | re.S)


def _section_of(text: str, pos: int) -> str:
    head = None
    for m in re.finditer(r"^##+ (.+)$|^\*\*([^*]+):\*\*", text[:pos], re.M):
        head = m.group(1) or m.group(2)
    return head or "(top)"


def _serialized_lexicon_bodies(lex: LexiconIndexer, data_dir: Path):
    for wdir, wid in WORLD_DIRS.items():
        for f in sorted((data_dir / wdir / "lexicon_chunks").glob("*.md")):
            entry = lex.parse_lexicon_file(f)
            body = truncate_at(entry.content, KEY_SOURCES_MARKERS)
            # Migrated-world Quick Meaning excision, exactly as
            # app/rag/retriever.py's get_context_for_response applies it -
            # all six worlds are migrated as of the Voice Rebuild.
            body = excise_section(body, QUICK_MEANING_MARKERS)
            yield f"{wdir}/{f.name}", body


def _serialized_story_bodies(story: StoryIndexer, data_dir: Path):
    for wdir, wid in WORLD_DIRS.items():
        for f in sorted((data_dir / wdir / "story_chunks").glob("*.md")):
            entry = story.parse_story_file(f)
            yield f"{wdir}/{f.name}", entry.content


def scan(data_dir: Path) -> dict:
    lex = object.__new__(LexiconIndexer)
    story = object.__new__(StoryIndexer)

    hard_fail = []
    report_only = []

    def classify(file_id: str, body: str):
        for m in _HARD_FAIL_ANYWHERE.finditer(body):
            hard_fail.append({
                "file": file_id, "section": _section_of(body, m.start()),
                "pattern": "unambiguous_apparatus", "match": m.group(0)})
        for section in _HARD_FAIL_SCOPED_SECTIONS:
            start = body.find(f"## {section}")
            if start == -1:
                start = body.find(f"**{section}")
            if start == -1:
                continue
            end = body.find("\n## ", start + 1)
            end = len(body) if end == -1 else end
            for m in _HARD_FAIL_SCOPED_PATTERN.finditer(body[start:end]):
                hard_fail.append({
                    "file": file_id, "section": section,
                    "pattern": "gravity_apparatus_in_insight_field",
                    "match": m.group(0)})
        for m in _REPORT_ONLY_PATTERN.finditer(body):
            report_only.append({
                "file": file_id, "section": _section_of(body, m.start()),
                "pattern": "background", "match": m.group(0)})

    for file_id, body in _serialized_lexicon_bodies(lex, data_dir):
        classify(file_id, body)
    for file_id, body in _serialized_story_bodies(story, data_dir):
        classify(file_id, body)

    return {"hard_fail": hard_fail, "report_only": report_only}


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--data-dir", default=str(BACKEND / "data"))
    args = p.parse_args()

    result = scan(Path(args.data_dir))
    hf, ro = result["hard_fail"], result["report_only"]

    print(f"# Apparatus leak gate\n\nHARD-FAIL: {len(hf)}  |  report-only: {len(ro)}\n")
    if hf:
        print("## HARD-FAIL (must fix before this world ships)\n")
        for v in hf:
            print(f"- {v['file']} [{v['section']}] {v['pattern']}: {v['match']!r}")
    if ro:
        by_file = {}
        for v in ro:
            by_file.setdefault(v["file"], 0)
            by_file[v["file"]] += 1
        print(f"\n## report-only: {len(by_file)} files carry background apparatus "
              f"language (not build-blocking; Phase 2 authoring signal)")

    if hf:
        print(f"\n**GATE FAILED** - {len(hf)} hard-fail hit(s).")
        return 1
    print("\n**GATE PASSED** - no hard-fail apparatus in any serialized chunk body.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
