#!/usr/bin/env python3
"""Regenerate world-build-docs/pahc/GRAVITY-INDEX.md from records/pahc/gravity/*.md.

Usage: python3 world-build-docs/pahc/generate_gravity_index.py
"""
import pathlib
import re
import sys

REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))

from engine.m1.loader import load_world_records
from engine.m1.schemas import RELATION_INVERSE

# G06 (household as basic unit) was tested per the approved Doc_04 and did
# NOT reach gravity status - logged here rather than silently dropped,
# since the schema has no record type for a rejected candidate.
NOT_ADVANCED = [
    {
        "name": "Household (oikos) as Basic Social/Meeting Unit",
        "generated_from": "Secondary scholarship (Meeks, Gehring, Balch, MacDonald); Doc_01's household-as-replicated-cell framing",
        "author_gravity_risk": "Severe, confirmed rather than resolved by testing",
        "why_not_advanced": (
            "Rests almost entirely on secondary scholarly reconstruction, not primary-voice "
            "attestation. The classic household-code texts (Colossians, Ephesians, 1 Peter) are "
            "none of them among this world's six primary voices and have no source row in this "
            "world's registry at all. Fails Repetition within the Native primary-voice set "
            "specifically. Not a claim that households were unimportant to how these communities "
            "met - a claim that this world's own evidentiary base, as built, cannot independently "
            "establish it as a gravity rather than an imported modern historiographical frame."
        ),
    }
]


def classification(name: str) -> str:
    m = re.search(r"\[([A-Z]+)", name)
    return m.group(1) if m else "?"


def main():
    recs = load_world_records("pahc")
    gravs = {k: v for k, v in recs.items() if v["record_type"] == "gravity"}
    ids = sorted(gravs)

    lines = [
        "# pahc Gravity Index",
        "",
        "**GENERATED from records/pahc/gravity/ — do not hand-edit.** Regenerate with "
        "`python3 world-build-docs/pahc/generate_gravity_index.py` after any gravity change. "
        "Companion to Doc_04 (Gravity Discovery), re-derived from the approved "
        "`CiC_W1_Doc04_Gravity_Discovery_FINAL.md` under the new records regime.",
        "",
        "## Candidate table",
        "",
        "| id | classification | canon_cells | formation_confidence | cross-check flag | single-source risk |",
        "|---|---|---|---|---|---|",
    ]
    for gid in ids:
        r = gravs[gid]
        srcs = {s["source_id"] for s in r.get("sources") or []}
        risk = "YES (" + next(iter(srcs)).replace("pahc.source.", "") + ")" if len(srcs) == 1 else f"no ({len(srcs)} sources)"
        cc_flag = "Yes" if r["confidence"]["divergence_note"] else "clean"
        lines.append(
            f"| {gid} | {classification(r['name'])} | {', '.join(r['canon_cells']) or '-'} "
            f"| {r['confidence']['formation_confidence']} | {cc_flag} | {risk} |"
        )

    lines += ["", "## By classification", ""]
    for cls in ("PRIMARY", "SUPPORTING", "TENSIONAL"):
        members = [gid for gid in ids if classification(gravs[gid]["name"]) == cls]
        lines.append(f"- **{cls}:** " + (", ".join(members) if members else "(none)"))
    lines.append(
        "- **Did not reach gravity status:** "
        + ", ".join(c["name"] for c in NOT_ADVANCED)
        + " (see Section 'Not advanced' below — no record exists for this candidate, per schema)"
    )

    lines += ["", "## Interaction matrix (gravity × gravity)", ""]
    header = "| |" + "|".join(gid.replace("pahc.gravity.", "") for gid in ids) + "|"
    lines.append(header)
    lines.append("|---" * (len(ids) + 1) + "|")
    rel_map = {gid: {rel["target"]: rel["type"] for rel in (gravs[gid].get("relations") or [])} for gid in ids}
    for row_id in ids:
        cells = [f"**{row_id.replace('pahc.gravity.', '')}**"]
        for col_id in ids:
            if row_id == col_id:
                cells.append("—")
            else:
                cells.append(rel_map[row_id].get(col_id, "no demonstrated relationship"))
        lines.append("| " + " | ".join(cells) + " |")

    isolated = [
        gid for gid in ids
        if not any(rel_map[gid].values()) and not any(gid in rel_map[o] for o in ids if o != gid)
    ]
    lines += [
        "",
        "**Isolated-candidate check:** "
        + (
            "none — every classified gravity has at least one demonstrated relationship to another, "
            "avoiding the signal the Framework names as a candidate list built from impression rather "
            "than evidence."
            if not isolated
            else "FLAGGED: " + ", ".join(isolated)
        ),
    ]

    lines += ["", "## Confidence/Gravity Cross-Check flags", ""]
    for gid in ids:
        r = gravs[gid]
        if r["confidence"]["divergence_note"]:
            lines.append(f"- **{gid}** ({classification(r['name'])}): {r['confidence']['divergence_note']}")

    lines += ["", "## tension-with coverage", ""]
    tensional = [gid for gid in ids if classification(gravs[gid]["name"]) == "TENSIONAL"]
    for gid in tensional:
        tw = [rel["target"] for rel in (gravs[gid].get("relations") or []) if rel["type"] == "tension-with"]
        if tw:
            lines.append(f"- {gid}: tension-with {', '.join(tw)}")
        else:
            lines.append(
                f"- {gid}: no tension-with relation recorded. This world's own Doc_04 Interaction "
                "Matrix never named an opposing-pole gravity for this candidate (its tension is with "
                "the state of the evidence, not a rival organizing force this world's own gravity set "
                "contains) — flagged for human review per the experimental tension-coverage gate's own "
                "discipline, not resolved by inventing a relation."
            )

    lines += ["", "## Not advanced (tested, did not reach gravity status)", ""]
    for c in NOT_ADVANCED:
        lines.append(f"### {c['name']}")
        lines.append(f"- **Generated from:** {c['generated_from']}")
        lines.append(f"- **Author Gravity risk:** {c['author_gravity_risk']}")
        lines.append(f"- **Why not advanced:** {c['why_not_advanced']}")
        lines.append("")

    lines += ["## Relation reciprocity check (mechanical)", ""]
    bad = []
    for gid, r in gravs.items():
        for rel in r.get("relations") or []:
            tgt = rel["target"]
            inv = RELATION_INVERSE[rel["type"]]
            if tgt in gravs:
                back = any(x["type"] == inv and x["target"] == gid for x in gravs[tgt].get("relations") or [])
                if not back:
                    bad.append((gid, rel["type"], tgt))
    lines.append(
        "All gravity-to-gravity relations reciprocate."
        if not bad
        else "NON-RECIPROCAL: " + str(bad)
    )

    lines += ["", "---", "<!-- generated by generate_gravity_index.py -->", ""]

    out = pathlib.Path(__file__).resolve().parent / "GRAVITY-INDEX.md"
    out.write_text("\n".join(lines))
    print(f"wrote {out} | gravities: {len(gravs)} | isolated: {len(isolated)} | non-reciprocal: {len(bad)}")


if __name__ == "__main__":
    main()
