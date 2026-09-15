#!/usr/bin/env python3
"""Regenerate worlds/pahc/build/GRAVITY-INDEX.md from records/pahc/gravity/*.md.

Usage: python3 worlds/pahc/build/generate_gravity_index.py
"""
import pathlib
import re
import sys

REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))

from engine.m1.loader import load_world_records
from engine.m1.schemas import RELATION_INVERSE

# Cross-strand status (Article 21) is authored prose inside each record's own
# description field (not a structured YAML field this schema defines), so it
# cannot be mechanically extracted the way classification/canon_cells/confidence
# can. Restated here as a hardcoded summary, sourced directly from Doc_04
# Section 3's own Cross-Strand Gravity Summary table - the same technique
# already used below for the not-advanced candidate.
AUTHOR_GRAVITY_RISK = {
    "pahc.gravity.authority-consolidation": "Yes (flagged at generation) - the Strand A/monarchical resolution rests overwhelmingly on Ignatius alone",
    "pahc.gravity.translocal-network": "No significant single-voice dependency",
    "pahc.gravity.state-pressure": "Moderate - Pliny is the clearest single direct description, but Tacitus/Suetonius/Ignatius corroborate independently",
    "pahc.gravity.martyrdom-meaning": "High (flagged at generation) - exactly two data points, both Strand A",
    "pahc.gravity.boundary-drawing": "High (flagged at generation) - substantively developed by exactly one voice",
    "pahc.gravity.liturgical-practice": "Moderate - three independent voices, though Justin's fuller account carries its own over-generalization risk",
}

CROSS_STRAND = {
    "pahc.gravity.authority-consolidation": "Force cross-strand confirmed; specific resolution strand-bound (Strand A: single office; Strand B: plural college)",
    "pahc.gravity.translocal-network": "Cross-strand confirmed (Rome via 1 Clement; Antioch/Asia Minor via Ignatius and Polycarp)",
    "pahc.gravity.state-pressure": "Cross-strand confirmed via Strand B (Rome, Tacitus/Nero) and Strand A (Antioch/Asia Minor, Ignatius's own arrest); Pliny's Bithynia-Pontus material corroborates but is a third data point, not a third strand",
    "pahc.gravity.martyrdom-meaning": "Strand-bound (Strand A only) - both data points are Strand A; no Strand B equivalent developed anywhere in this world's evidentiary base",
    "pahc.gravity.boundary-drawing": "Strand-bound (Strand A only)",
    "pahc.gravity.liturgical-practice": "Cross-strand confirmed - Strand A (Ignatius) and Strand B (Justin), plus the Didache's separate single-community witness",
}

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
            "specifically. Doc_04's own correction, carried here: this finding does not "
            "'reinforce' Doc_03's independent 'house church' lexicon open item as a second, "
            "convergent line of evidence - both draw on the identical underlying fact (no "
            "Registry row for the household-code texts), verified twice by different methods "
            "(a Repetition test here; a vocabulary lookup there), not two separately-derived "
            "confirmations. Not a claim that households were unimportant to how these "
            "communities met - a claim that this world's own evidentiary base, as built, cannot "
            "independently establish it as a gravity rather than an imported modern "
            "historiographical frame."
        ),
        "note": (
            "No gravity record exists for this candidate (this schema has no 'did not reach "
            "gravity status' record type) - logged here instead. This is NOT the schema's real "
            "route for a permanent record of the finding: an honest_limit record is, and this "
            "world's F5-E canon cell (material remains / how historians know about daily life) "
            "is currently uncovered - a future honest_limit or contested_claim record for that "
            "cell should cite this finding directly rather than leaving it only in this "
            "generated index."
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
        "`python3 worlds/pahc/build/generate_gravity_index.py` after any gravity change. "
        "Companion to Doc_04 (Gravity Discovery), re-derived from the approved "
        "`CiC_W1_Doc04_Gravity_Discovery_FINAL.md` under the new records regime.",
        "",
        "## Candidate table",
        "",
        "| id | classification | canon_cells | formation_confidence | cross-check flag | Author Gravity risk (Doc_04) | source count |",
        "|---|---|---|---|---|---|---|",
    ]
    for gid in ids:
        r = gravs[gid]
        srcs = {s["source_id"] for s in r.get("sources") or []}
        cc_flag = "Yes" if r["confidence"]["divergence_note"] else "clean"
        lines.append(
            f"| {gid} | {classification(r['name'])} | {', '.join(r['canon_cells']) or '-'} "
            f"| {r['confidence']['formation_confidence']} | {cc_flag} "
            f"| {AUTHOR_GRAVITY_RISK.get(gid, '(not recorded)')} | {len(srcs)} |"
        )

    lines += ["", "## By classification", ""]
    for cls in ("PRIMARY", "SUPPORTING", "TENSIONAL"):
        members = [gid for gid in ids if classification(gravs[gid]["name"]) == cls]
        lines.append(f"- **{cls}:** " + (", ".join(members) if members else "(none)"))
    lines.append(
        "- **Did not reach gravity status:** "
        + ", ".join(c["name"] for c in NOT_ADVANCED)
        + " (see Section 'Not advanced' below)"
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

    lines += ["", "## Cross-strand status (Article 21)", ""]
    for gid in ids:
        lines.append(f"- **{gid}**: {CROSS_STRAND.get(gid, '(not recorded)')}")

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
                "Matrix never named an opposing-pole gravity for this candidate — the closest candidate, "
                "state-pressure (G03), was carried as a related cell across four review rounds before "
                "Doc_04's own round 5 found no textual grounding for it anywhere and corrected it to "
                "\"No demonstrated relationship,\" a correction this gravity-level finding still follows "
                "(unchanged). Doc_08 (approved and re-derived into records at Step 6) proposes, as its own "
                "new synthesis rather than an inherited Doc_04 finding, that state-pressure and "
                "boundary-drawing converge on a shared formative lesson at the level of lived experience "
                "(Section 4, Connection 5) — this is now realized as a schema edge at the FORCE level "
                "(pahc.gravity.boundary-drawing → pahc.force.state-pressure, associated-with), disclosed "
                "in both records' own bodies as Doc_08's interpretive extension. It remains, by design, "
                "not a tension-with relation and not a gravity-level G03↔G05 edge: Doc_04's own "
                "gravity-level correction is not reopened by this later, differently-grained finding."
            )

    lines += ["", "## Not advanced (tested, did not reach gravity status)", ""]
    for c in NOT_ADVANCED:
        lines.append(f"### {c['name']}")
        lines.append(f"- **Generated from:** {c['generated_from']}")
        lines.append(f"- **Author Gravity risk:** {c['author_gravity_risk']}")
        lines.append(f"- **Why not advanced:** {c['why_not_advanced']}")
        lines.append(f"- **Note:** {c['note']}")
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
