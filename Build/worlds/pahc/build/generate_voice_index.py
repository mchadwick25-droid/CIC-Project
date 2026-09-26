#!/usr/bin/env python3
"""Regenerate Build/worlds/pahc/build/VOICE-INDEX.md from
records/pahc/voice_craft/*.md and records/pahc/demonstration/*.md.

Usage: python3 Build/worlds/pahc/build/generate_voice_index.py
"""
import pathlib
import sys

REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))

from engine.m1.loader import load_world_records
from collections import Counter


REQUIRED_CENTER_CELLS = ["C-I", "C-E", "C-P", "C-T"]
REQUIRED_IDENTITY_COLLISION = Counter(["F6-P", "F6-P", "F6-T"])


def check_required_set(demos):
    """Returns (lines, missing) - missing is non-empty iff the spec's own
    required demonstration set (SS4.3 step 5c: center cells first, the
    identity-collision cells, honest limits in voice, one lament exchange)
    is not actually satisfied by what is on disk. Selects by `tags` and
    `canon_cells` - the record's own data - never by filename substring,
    so a rename cannot silently empty a required row."""
    missing = []

    center_present = {c for r in demos.values() for c in (r.get("canon_cells") or [])
                       if c in REQUIRED_CENTER_CELLS}
    center_missing = [c for c in REQUIRED_CENTER_CELLS if c not in center_present]
    if center_missing:
        missing.append(f"center cell(s) not demonstrated: {', '.join(center_missing)}")

    ic_demos = {k: r for k, r in demos.items() if "identity-collision" in (r.get("tags") or [])}
    ic_cells = Counter(c for r in ic_demos.values() for c in (r.get("canon_cells") or [])
                        if c in ("F6-P", "F6-T"))
    for cell, needed in REQUIRED_IDENTITY_COLLISION.items():
        have = ic_cells.get(cell, 0)
        if have < needed:
            missing.append(f"identity-collision {cell}: need {needed}, have {have}")

    honest_limit_demos = {k: r for k, r in demos.items() if "honest-limit" in (r.get("tags") or [])}
    if not honest_limit_demos:
        missing.append("no honest-limit-in-voice demonstration (tags: [honest-limit])")

    lament_demos = {k: r for k, r in demos.items() if "lament" in (r.get("tags") or [])}
    if not lament_demos:
        missing.append("no lament exchange (tags: [lament])")

    lines = []
    lines.append(f"- **Center cells covered:** {', '.join(sorted(center_present)) or 'NONE'} "
                 f"of {', '.join(REQUIRED_CENTER_CELLS)} (spec requires center cells first)")
    lines.append(f"- **Identity-collision demonstrations:** {len(ic_demos)} "
                 f"({', '.join(sorted(ic_demos))}) - spec requires F6-P x2, F6-T x1 before any world opens")
    lines.append(f"- **Honest-limit-in-voice demonstration(s):** {', '.join(sorted(honest_limit_demos)) or 'NONE'}")
    lines.append(f"- **Lament exchange(s):** {', '.join(sorted(lament_demos)) or 'NONE'}")
    if missing:
        lines.append("")
        lines.append("**MISSING (required set not satisfied):**")
        for m in missing:
            lines.append(f"- {m}")
    else:
        lines.append("")
        lines.append("- Required set complete - see \"Checked and found sound\" pattern: this line only "
                     "renders when the check above actually passed, not by default.")

    return lines, missing, ic_demos, honest_limit_demos, lament_demos


def main():
    recs = load_world_records("pahc")
    craft = {k: v for k, v in recs.items() if v["record_type"] == "voice_craft"}
    demos = {k: v for k, v in recs.items() if v["record_type"] == "demonstration"}

    lines = [
        "# pahc Voice Index",
        "",
        "**GENERATED from records/pahc/voice_craft/ and records/pahc/demonstration/ — "
        "do not hand-edit.** Regenerate with "
        "`python3 Build/worlds/pahc/build/generate_voice_index.py` after any change. "
        "Companion to the Representative voice build step "
        "(Build/reference/Redesign-Spec/CiC-Program-Spec.md SS4.3 step 5).",
        "",
        f"**Totals:** {len(craft)} voice_craft, {len(demos)} demonstration.",
        "",
        "## Required-set check", "",
    ]

    check_lines, missing, ic_demos, honest_limit_demos, lament_demos = check_required_set(demos)
    lines += check_lines
    lines.append("")

    lines += ["## voice_craft", ""]
    for cid in sorted(craft):
        r = craft[cid]
        lines.append(f"### {cid}")
        lines.append(f"- **identity:** {r['identity']}")
        lines.append("- **flavor_notes:**")
        for n in r.get("flavor_notes") or []:
            lines.append(f"  - [{n.get('segment')}/{n.get('tag')}] {n.get('note')}")
        lines.append("- **characteristic_concerns:**")
        for c in r.get("characteristic_concerns") or []:
            lines.append(f"  - {c}")
        lines.append(f"- **guard:** {r['guard']}")
        lines.append("")

    lines += ["## Demonstrations", ""]
    for did in sorted(demos):
        r = demos[did]
        cc = ", ".join(r.get("canon_cells") or []) or "-"
        tags = ", ".join(r.get("tags") or []) or "-"
        lines.append(f"### {did}")
        lines.append(f"- **canon_question_id:** {r.get('canon_question_id')}")
        lines.append(f"- **canon_cells:** {cc}")
        lines.append(f"- **tags:** {tags}")
        for turn in r.get("exchange") or []:
            lines.append(f"  - **{turn['speaker']}:** {turn['text']}")
        lines.append("")

    lines += ["", "---", "<!-- generated by generate_voice_index.py -->", ""]

    out = pathlib.Path(__file__).resolve().parent / "VOICE-INDEX.md"
    out.write_text("\n".join(lines))
    status = "MISSING items - see file" if missing else "required set complete"
    print(f"wrote {out} | voice_craft: {len(craft)} | demonstration: {len(demos)} "
          f"| identity-collision: {len(ic_demos)} | {status}")
    if missing:
        sys.exit(1)


if __name__ == "__main__":
    main()
