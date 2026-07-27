"""S2.8 - chunk views: regenerate today's deployment chunk formats from records.

Pass 1 SS3.9: every deployment artifact becomes a named view over the
record set. These two views reproduce the lexicon-chunk and story-chunk
file formats the runtime ingests today (app/rag via scripts/index_*.py),
writing into a STAGING directory - deployed files are untouched until all
three S2.8 parities are green (blueprint S2.8 swap rule).

Known non-round-trip classes (each classified, never silent, in
render_parity.py):
- Tags line: no schema home (S2.9 CO candidate) -> defect class.
- Related Terms: view renders only record-backed relations; chunk lists
  partner terms with no Desert chunk/record (S2.9 CO) -> defect class.
- Do-Not-Retrieve-When retired classes (cross-world guard): dropped by
  Pass 1's own retirement of the condition class -> intended-change.
- Story "Formation Ecology Connection": no record home (FLAG-004) ->
  defect class.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
RECORDS = BACKEND / "wrs" / "records" / "desert_world"
STAGING = HERE / "staging" / "desert_world"

EF_MARKER = "Chunk Ecological Function (verbatim, absorbed per FLAG-002): "


def load_records(subdir: str) -> dict[str, dict]:
    out = {}
    for p in sorted((RECORDS / subdir).glob("*.md")):
        rec = yaml.safe_load(p.read_text(encoding="utf-8").split("---\n")[1])
        out[rec["id"]] = rec
    return out


def _ef_text(term: dict) -> str:
    """Ecological Function, recovered verbatim from the FLAG-002 parking."""
    for edge in term.get("field_relations", []):
        note = edge.get("note", "")
        if EF_MARKER in note:
            return note.split(EF_MARKER, 1)[1].strip()
    return ""


def _related_terms(term: dict, terms: dict[str, dict]) -> str:
    """Record-backed Related Terms only (partner terms with no record are
    an S2.9 CO; the diff classifies the shortfall)."""
    seen, names = set(), []
    for edge in term.get("field_relations", []):
        tid = edge.get("target_id")
        if tid and tid in terms and tid not in seen:
            seen.add(tid)
            # chunk Related Terms use the bare term name (before any gloss),
            # with no spaces around slashes (deployed style)
            names.append(terms[tid]["term"].split(" (")[0].replace(" / ", "/"))
    return ", ".join(names)


def render_lexicon_chunk(term: dict, terms: dict[str, dict]) -> str:
    r = term.get("retrieval", {})
    rw = "; ".join(r.get("retrieve_when", []))
    dnrw_items = [c["text"] for c in r.get("do_not_retrieve_when", [])]
    dnrw = "; ".join(dnrw_items) if dnrw_items else "—"
    distortion = f"{term.get('modern_hearing', '')} {term.get('distortion_risk', '')}".strip()
    key_sources = " ".join(
        s.get("author_gravity_note", "").strip()
        for s in term.get("sources", []) if s.get("author_gravity_note"))
    lines = [
        "---",
        f"Term: {term['term']}",
        "World-Code: desert",
        f"Tier: [{r.get('tier', '')}]",
        f"Aliases: {', '.join(term.get('aliases', []))}",
        f"Related Terms: {_related_terms(term, terms)}",
        f"Retrieve-When: {rw}",
        f"Do-Not-Retrieve-When: {dnrw}",
        "---",
        "",
        f"**Quick Meaning:** {term.get('quick_meaning', '')}",
        "",
        f"**World Meaning:** {term.get('world_meaning', '')}",
        "",
        f"**Ecological Function:** {_ef_text(term)}",
        "",
        f"**Distortion Risk:** {distortion}",
        "",
        f"**Key Sources:** {key_sources}",
    ]
    return "\n".join(lines) + "\n"


def render_story_chunk(story: dict) -> str:
    r = story.get("retrieval", {})
    rw = "; ".join(r.get("retrieve_when", []))
    dnrw_items = [c["text"] for c in r.get("do_not_retrieve_when", [])]
    dnrw = "; ".join(dnrw_items) if dnrw_items else "—"
    srcs = story.get("sources", [])
    confidence = srcs[0].get("author_gravity_note", "") if srcs else ""
    source_line = ""
    for s in srcs[1:]:
        note = s.get("author_gravity_note", "")
        if note.startswith("Source line (chunk): "):
            source_line = note[len("Source line (chunk): "):]
    # voice_surface = telling-formula + " Usage guidance (chunk, verbatim): " + usage
    usage = ""
    vs = story.get("voice_surface", "")
    m = re.search(r"Usage guidance \(chunk, verbatim\): (.*)", vs, re.S)
    if m:
        usage = m.group(1).strip()
    parts = [
        "## Retrieval Front-Matter",
        "",
        "```",
        f"Story-Title:    {story['title']}",
        "World-Code:     desert",
        f"Tier:           {story['narrative_tier']['tier']}",
        f"Confidence:     {confidence}",
        f"Source:         {source_line}",
        f"Retrieve-When:  {rw}",
        f"Do-Not-Retrieve-When: {dnrw}",
        "```",
        "",
        "---",
        "",
        "## Story Text",
        "",
        story.get("text", ""),
        "",
        "---",
        "",
        "## Tier Justification",
        "",
        story["narrative_tier"].get("justification", ""),
        "",
        "---",
        "",
        "## Usage Guidance",
        "",
        usage,
    ]
    return "\n".join(parts) + "\n"


DEPLOYED_LEX = BACKEND / "data" / "desert_world" / "lexicon_chunks"
DEPLOYED_STORY = BACKEND / "data" / "desert_world" / "story_chunks"


def deployed_name(rid: str, deployed_dir: Path) -> str:
    for p in deployed_dir.glob("*.md"):
        if p.stem.split("_")[0] == rid:
            return p.name
    raise FileNotFoundError(f"no deployed chunk for {rid}")


def main() -> None:
    terms = load_records("term")
    stories = load_records("story")
    lex_out = STAGING / "lexicon_chunks"
    story_out = STAGING / "story_chunks"
    lex_out.mkdir(parents=True, exist_ok=True)
    story_out.mkdir(parents=True, exist_ok=True)
    for rid, t in terms.items():
        name = deployed_name(rid, DEPLOYED_LEX)
        (lex_out / name).write_text(render_lexicon_chunk(t, terms),
                                    encoding="utf-8")
    for rid, s in stories.items():
        name = deployed_name(rid, DEPLOYED_STORY)
        (story_out / name).write_text(render_story_chunk(s),
                                      encoding="utf-8")
    print(f"staged {len(terms)} lexicon + {len(stories)} story chunks -> {STAGING}")


if __name__ == "__main__":
    main()
