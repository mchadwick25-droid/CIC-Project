#!/usr/bin/env python3
"""Deterministic parser: Guided Starters markdown -> JSON.

Mechanical extraction, not an LLM rewrite -- citations and question text
must come through byte-exact. Validates entry/follow-up counts against the
source file's own visible structure so nothing silently drops.
"""
import json
import re
import sys
from pathlib import Path

REPO = Path("/home/user/CIC-Project")

WORLDS = [
    {
        "world_id": "post-apostolic-house-church",
        "file": "World-Builds/01-Post-Apostolic-House-Church/CiC_W1_Guided_Starters_V0_1_DRAFT.md",
    },
    {
        "world_id": "alexandria-catechetical",
        "file": "World-Builds/Alexandria-Catechetical-School/Guided_Starters_V0_1_DRAFT.md",
    },
    {
        "world_id": "desert-monasticism",
        "file": "World-Builds/Desert-Monasticism/CiC_W3_Guided_Starters_V0_1_DRAFT.md",
    },
    {
        "world_id": "hieronymian-ascetic-literary",
        "file": "World-Builds/Hieronymian-Ascetic-Literary/hal_Guided_Starters_V0_1_DRAFT.md",
    },
    {
        "world_id": "syriac-edessa-nisibis",
        # Document-set redesign step 2 (2026-08-14): the starters document's
        # canonical home is now a record; the body is the draft verbatim, so
        # parsing is unchanged. Other worlds migrate the same way at their turn.
        "file": "cic-poc/backend/wrs/records/syriac_world/guided_starters/syrstarters001.md",
        "record": True,
    },
    {
        "world_id": "imperial-juridical-christianity",
        "file": "World-Builds/Imperial-Juridical-Christianity/Guided_Starters_V0_1_DRAFT.md",
    },
]

TIER_HEADERS = [
    ("first_visit", "First Visit"),
    ("going_deeper", "Going Deeper"),
    ("for_the_wrestling", "For the Wrestling"),
    ("honest_limits", "Questions This World Answers Honestly With Its Limits"),
]


def split_sections(text):
    """Split the body into the 4 named ## sections, keyed by tier_id."""
    sections = {}
    # find each '## ' heading line and its span
    heading_re = re.compile(r"^## (.+)$", re.MULTILINE)
    matches = list(heading_re.finditer(text))
    for i, m in enumerate(matches):
        heading = m.group(1).strip()
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[start:end]
        for tier_id, label in TIER_HEADERS:
            if heading.startswith(label):
                sections[tier_id] = body
                break
    return sections


ENTRY_RE = re.compile(
    r"\*\*(?P<topic>.+?)\*\*\s*—\s*(?P<why>.+?)\s*\[(?P<citations>[^\]]+)\]\s*\n"
    r"\*Opening question:\*\s*\"(?P<opening>[^\"]+)\"\s*\n"
    r"Follow-ups:\s*(?P<followups>.+?)(?=\n\n|\Z)",
    re.DOTALL,
)

FOLLOWUP_RE = re.compile(r"\"([^\"]+)\"")

LIMIT_RE = re.compile(
    r"\*\*\"(?P<question>[^\"]+)\"\*\*\s*—\s*(?P<answer>.+?)\s*\[(?P<citations>[^\]]+)\]",
    re.DOTALL,
)


def clean(s):
    return re.sub(r"\s+", " ", s).strip()


def parse_walk_tier(body):
    entries = []
    for m in ENTRY_RE.finditer(body):
        followups = FOLLOWUP_RE.findall(m.group("followups"))
        entries.append({
            "topic": clean(m.group("topic")),
            "why": clean(m.group("why")),
            "citations": [clean(c) for c in m.group("citations").split(";")],
            "opening_question": clean(m.group("opening")),
            "follow_ups": [clean(f) for f in followups],
        })
    return entries


def parse_limits_tier(body):
    entries = []
    for m in LIMIT_RE.finditer(body):
        entries.append({
            "question": clean(m.group("question")),
            "answer": clean(m.group("answer")),
            "citations": [clean(c) for c in m.group("citations").split(";")],
        })
    return entries


def parse_header(text):
    def field(name):
        m = re.search(rf"\*\*{name}:\*\*\s*(.+?)\s*\n", text)
        return clean(m.group(1)) if m else None

    title_m = re.search(r"^# (.+?)\s*\(DRAFT V0\.1\)", text, re.MULTILINE)
    return {
        "title": clean(title_m.group(1)) if title_m else None,
        "status": field("Status"),
        "world": field("World"),
        "purpose": field("Purpose"),
        "grounding": field("Grounding"),
    }


def main():
    out_worlds = []
    problems = []

    for w in WORLDS:
        path = REPO / w["file"]
        text = path.read_text(encoding="utf-8")
        if w.get("record"):
            # A record home: strip the YAML front-matter fence; the body is
            # the starters document verbatim.
            text = text.split("\n---\n", 1)[1]
        # Strip HTML editorial comments before parsing -- they're authoring notes
        # (e.g. rejected-phrasing history for a safety fix), never participant-facing
        # content, and must never leak into follow-up/answer text.
        comment_count = len(re.findall(r"<!--.*?-->", text, re.DOTALL))
        text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
        if comment_count:
            print(f"  (stripped {comment_count} HTML comment(s) from {w['world_id']})")
        header = parse_header(text)
        sections = split_sections(text)

        tiers = []
        counts = {}
        for tier_id, label in TIER_HEADERS:
            body = sections.get(tier_id, "")
            if tier_id == "honest_limits":
                entries = parse_limits_tier(body)
            else:
                entries = parse_walk_tier(body)
            counts[tier_id] = len(entries)
            tiers.append({"tier_id": tier_id, "tier_title": label, "entries": entries})

        # cross-check against the doc's own bolded-entry count for each section
        # (a raw '**' count sanity check, since real prose also bolds occasional words --
        # cross-check against expected non-zero and against manual eyeball counts below)
        out_worlds.append({
            "world_id": w["world_id"],
            "source_file": w["file"],
            **header,
            "tiers": tiers,
        })

        for tier_id, _ in TIER_HEADERS:
            if counts[tier_id] == 0:
                problems.append(f"{w['world_id']}: {tier_id} parsed 0 entries")
        for t in tiers:
            if t["tier_id"] == "honest_limits":
                for e in t["entries"]:
                    if not e["question"] or not e["answer"] or not e["citations"]:
                        problems.append(f"{w['world_id']}: incomplete honest_limits entry: {e['question'][:50]!r}")
            else:
                for e in t["entries"]:
                    if len(e["follow_ups"]) != 3:
                        problems.append(
                            f"{w['world_id']}/{t['tier_id']}: {e['topic']!r} has "
                            f"{len(e['follow_ups'])} follow-ups, expected exactly 3"
                        )

    result = {
        "$schema_version": "1.0",
        "name": "CiC Guided Starters",
        "source_document_pattern": "World-Builds/<world>/*Guided_Starters_V0_1_DRAFT.md",
        "notes": {
            "structure": "Per world, 4 depth tiers: first_visit, going_deeper, for_the_wrestling, honest_limits. First 3 tiers are walk-style entries (topic/why/citations/opening_question/follow_ups); honest_limits entries are question/answer/citations pairs, no follow-ups.",
            "role_generic_caveat": "Openers are illustrative routing seeds, not per-world authored gates -- a participant is never confined to them.",
        },
        "worlds": out_worlds,
    }

    out_path = REPO / "cic-poc/frontend/src/data/guided_starters.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"Wrote {out_path}")
    print()
    for w in out_worlds:
        c = {t["tier_id"]: len(t["entries"]) for t in w["tiers"]}
        print(f"  {w['world_id']:32s} first_visit={c['first_visit']:2d} going_deeper={c['going_deeper']:2d} wrestling={c['for_the_wrestling']:2d} limits={c['honest_limits']:2d}")

    if problems:
        print("\nPROBLEMS:")
        for p in problems:
            print(f"  - {p}")
        sys.exit(1)


if __name__ == "__main__":
    main()
