#!/usr/bin/env python3
"""Regenerate Build/worlds/pahc/build/FORCES-INDEX.md from records/pahc/force/*.md.

Usage: python3 Build/worlds/pahc/build/generate_forces_index.py
"""
import pathlib
import re
import sys

REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))

from engine.m1.loader import load_world_records
from engine.m1.schemas import RELATION_INVERSE

# Six-cell placement is authored prose (each force's own [1A - ...] name
# suffix and its section heading in the approved Doc_08), not a structured
# YAML field this schema defines - restated here as a hardcoded map, the
# same technique already used in generate_gravity_index.py for information
# the schema itself cannot carry.
CELL_MAP = {
    "pahc.force.roman-mediterranean-world": "1A",
    "pahc.force.neronian-persecution": "1A",
    "pahc.force.apostolic-testimony-inheritance": "1B",
    "pahc.force.two-ways-catechetical-inheritance": "1B",
    "pahc.force.state-pressure": "2A",
    "pahc.force.contemporary-rival-movements": "2A",
    "pahc.force.authority-consolidation": "2B",
    "pahc.force.transmission-network": "2B",
    "pahc.force.martyrdom-meaning": "2B",
    "pahc.force.boundary-drawing": "2B",
    "pahc.force.systematic-theological-mode-elsewhere": "3A",
    "pahc.force.alexandria-emergence": "3A",
    "pahc.force.monepiscopacy-consolidation": "3B",
    "pahc.force.selective-canonization": "3B",
}

CELL_QUESTIONS = {
    "1A": "What external conditions made this particular form of Christianity possible, necessary, or urgent at its origin?",
    "1B": "What internal commitments, convictions, or inherited traditions gave this world its earliest distinctive shape from within?",
    "2A": "What external forces required this community's continuous response and adaptation throughout its active life?",
    "2B": "What internal forces sustained this community from within, generated its characteristic internal tensions, and shaped how it transmitted itself?",
    "3A": "What external forces brought this world's distinct form to an end or transformed it into something different?",
    "3B": "What internal forces fractured this community, generated successor movements, or led to the dissolution of its characteristic form?",
}

# The four "this gravity IS this force" identity pairs - carried here
# explicitly so the index states the identity rather than presenting these
# as four more ordinary force<->gravity edges. Attribution is not uniform:
# Doc_08 Section 5 states the identity explicitly in prose only for G03
# ("This gravity IS Force 2A-1 itself, per Doc_04's own framing"); for G01,
# G04, G05 the identity is instead carried by the "(G01)"/"(G04)"/"(G05)"
# tags on Doc_08 Section 3's own Cell-2B force headings, not by a Section 5
# sentence.
IDENTITY_PAIRS = {
    "pahc.force.state-pressure": "pahc.gravity.state-pressure",
    "pahc.force.authority-consolidation": "pahc.gravity.authority-consolidation",
    "pahc.force.martyrdom-meaning": "pahc.gravity.martyrdom-meaning",
    "pahc.force.boundary-drawing": "pahc.gravity.boundary-drawing",
}

# Doc_08 Section 4's Named Cross-Cell Connections (six total) - authored
# prose linking two forces to each other directly. Only Connection 6 is
# realized below as a genuine bidirectional force-to-force relations[]
# edge; the other five are realized instead as force->gravity edges (see
# the gravity-connection cross-reference section), so the NARRATIVE label
# ("Connection 2", etc.) is restated here for traceability to Doc_08, not
# because the schema already carries all six as force<->force edges - the
# generated output below reports which of the six actually are.
NAMED_CONNECTIONS = [
    ("Connection 1", "pahc.force.neronian-persecution", "pahc.force.authority-consolidation",
     "eyewitness-generation loss is the direct generative condition for authority's own ongoing internal contest"),
    ("Connection 2", "pahc.force.state-pressure", "pahc.force.martyrdom-meaning",
     "the single most directly and explicitly evidenced connection in this entire matrix - martyrdom IS the meaning-making response to state pressure"),
    ("Connection 3", "pahc.force.contemporary-rival-movements", "pahc.force.boundary-drawing",
     "Ignatius's anti-docetic argument exists as a direct response to the live presence of rival teaching in his own regional field"),
    ("Connection 4", "pahc.force.roman-mediterranean-world", "pahc.force.transmission-network",
     "the same infrastructure and koine that made the correspondence network possible at its origin is the physical condition for every later transmission event"),
    ("Connection 5", "pahc.force.state-pressure", "pahc.force.boundary-drawing",
     "this build's own new synthesis, not an inherited Doc_04 finding - disclosed as an interpretive extension, not manufactured as settled fact"),
    ("Connection 6", "pahc.force.systematic-theological-mode-elsewhere", "pahc.force.monepiscopacy-consolidation",
     "two of three converging lines of evidence for the same closing boundary - a systematized succession-argument mode emerging in adjacent regions and monepiscopacy's own internal consolidation are two faces of the same underlying transition"),
]

# Transmission Specificity Principle (Doc_08 Cell 2B/3B's own governing
# note): both transmission-dimension forces must name real mechanisms, not
# an undifferentiated "tradition" - checked here mechanically against each
# record's own manifestations, since the schema has no dedicated field for
# "is this specific enough."
TRANSMISSION_FORCES = ["pahc.force.transmission-network", "pahc.force.selective-canonization"]


def cell_of(name: str) -> str:
    """Parse the six-cell tag directly from a force's own `[nX - kind/side]`
    name suffix, so CELL_MAP (which duplicates this by hand for readability
    in the six-cell matrix section) can be checked against the record's own
    text rather than trusted blind - catches drift if a record is edited or
    added without updating CELL_MAP."""
    m = re.search(r"\[(\d[AB]) -", name)
    return m.group(1) if m else "?"


def main():
    recs = load_world_records("pahc")
    forces = {k: v for k, v in recs.items() if v["record_type"] == "force"}
    gravs = {k: v for k, v in recs.items() if v["record_type"] == "gravity"}
    ids = sorted(forces)

    missing_cell = [fid for fid in ids if fid not in CELL_MAP]
    cell_drift = [
        fid for fid in ids
        if fid in CELL_MAP and cell_of(forces[fid]["name"]) != CELL_MAP[fid]
    ]

    lines = [
        "# pahc Forces Index",
        "",
        "**GENERATED from records/pahc/force/ — do not hand-edit.** Regenerate with "
        "`python3 Build/worlds/pahc/build/generate_forces_index.py` after any force change. "
        "Companion to Doc_08 (Forces), re-derived from the approved "
        "`CiC_W1_Doc08_Forces_Document.md` under the new records regime.",
        "",
        f"**Total force records:** {len(ids)} (matches Doc_08's own count of 14 as of this "
        "generation - if this number ever reads otherwise, Doc_08 and this world's own force "
        "records have diverged and that divergence needs resolving, not silently updating this line).",
    ]
    if missing_cell:
        lines.append(f"**UNPLACED (no six-cell assignment in this index's own map):** {', '.join(missing_cell)}")
    if cell_drift:
        lines.append(f"**CELL_MAP DRIFT (hardcoded map disagrees with the record's own name suffix):** {', '.join(cell_drift)}")

    lines += ["", "## Six-cell matrix", ""]
    for cell in ("1A", "1B", "2A", "2B", "3A", "3B"):
        members = [fid for fid in ids if CELL_MAP.get(fid) == cell]
        lines.append(f"### Cell {cell} — {CELL_QUESTIONS[cell]}")
        lines.append("")
        for fid in members:
            r = forces[fid]
            cc = ", ".join(r["canon_cells"]) or "-"
            identity = IDENTITY_PAIRS.get(fid)
            id_note = f" — **IS** `{identity}`" if identity else ""
            lines.append(
                f"- **{fid}**{id_note} (`{r['confidence']['formation_confidence']}`, canon_cells: {cc})"
            )
        lines.append("")

    lines += ["## Gravity-connection cross-reference (force → gravity)", ""]
    for fid in ids:
        r = forces[fid]
        targets = [rel["target"] for rel in (r.get("relations") or []) if rel["target"] in gravs]
        identity = IDENTITY_PAIRS.get(fid)
        parts = []
        if identity:
            parts.append(f"IS {identity}")
        if targets:
            parts.append("associated-with " + ", ".join(targets))
        lines.append(f"- **{fid}**: " + ("; ".join(parts) if parts else "no gravity connection declared"))

    lines += ["", "## Force-to-force connections (Doc_08 Section 4, Named Cross-Cell Connections)", ""]
    for label, a, b, note in NAMED_CONNECTIONS:
        a_ok = a in forces
        b_ok = b in forces
        rel_ok = a_ok and b_ok and any(
            rel["type"] == "associated-with" and rel["target"] == b
            for rel in (forces[a].get("relations") or [])
        )
        status = "declared" if rel_ok else "NOTE ONLY (not a schema relations[] edge on both records)"
        lines.append(f"- **{label}** ({a} ↔ {b}) — {status}: {note}")

    lines += ["", "## Transmission Specificity check (Cells 2B/3B)", ""]
    for fid in TRANSMISSION_FORCES:
        if fid not in forces:
            lines.append(f"- **{fid}**: MISSING")
            continue
        r = forces[fid]
        manifestations = r.get("manifestations") or []
        named = [m for m in manifestations if any(
            marker in m for marker in ("Polycarp", "Codex", "Ignatius", "Bryennios", "Ussher", "Vossius",
                                        "Pearson", "Simonides", "Athanasius", "Irenaeus", "Origen", "Clement of Alexandria")
        )]
        lines.append(
            f"- **{fid}**: {len(named)}/{len(manifestations)} manifestations name a specific person, "
            "manuscript, or institution rather than an undifferentiated 'tradition' - "
            + ("passes the Transmission Specificity Principle." if named else "FLAGGED: no named mechanism found.")
        )

    lines += ["", "## Confidence summary (each force's own Doc_08 Section 3 Layer-1 confidence tag)", ""]
    lines.append(
        "Note: Doc_08 Section 7 groups forces into two broad tiers (Documented/Widely-Accepted vs. "
        "Dominant-Modern-Reconstruction); it does not itself state a per-force value at the "
        "five-level granularity below. Where a force's own Section 3 Layer-1 tag names a split "
        "(e.g. \"Documented that X; Contested that Y\"), this build's own rule - applied but not "
        "written down in Doc_08 itself - is to set formation_confidence to whichever half of the "
        "split does the record's actual interaction/dependency work, the same Confidence/Gravity "
        "Cross-Check discipline used throughout the gravity records."
    )
    lines.append("")
    lines.append("| id | formation_confidence | verification_state | cross-check flag |")
    lines.append("|---|---|---|---|")
    for fid in ids:
        r = forces[fid]
        cc_flag = "Yes" if r["confidence"]["divergence_note"] else "clean"
        lines.append(
            f"| {fid} | {r['confidence']['formation_confidence']} | {r['confidence']['verification_state']} | {cc_flag} |"
        )

    lines += ["", "## Identity pairs (\"this gravity IS this force\")", ""]
    lines.append(f"- **pahc.force.state-pressure** IS **pahc.gravity.state-pressure** — per Doc_08 Section 5's own explicit framing (\"This gravity IS Force 2A-1 itself\").")
    for fid, gid in IDENTITY_PAIRS.items():
        if fid == "pahc.force.state-pressure":
            continue
        lines.append(f"- **{fid}** IS **{gid}** — per Doc_08 Section 3's own force heading naming this gravity directly, not a Section 5 sentence (Section 5 lists this force's connected gravities but does not restate the identity in prose).")
    lines.append(
        "- Not identity-paired but ending-stage RESOLUTION of a Cell-2B identity force: "
        "**pahc.force.monepiscopacy-consolidation** resolves (does not continue) "
        "**pahc.gravity.authority-consolidation** / **pahc.force.authority-consolidation**'s own defining tension."
    )

    lines += ["", "## Relation reciprocity check (mechanical, every edge touching a force record)", ""]
    bad = []
    # Scans BOTH directions - every relation on every pahc record (not force
    # records alone) whose source or target is a force - so a gravity->force
    # edge with no force-side reciprocal is caught here too, not just the
    # force->gravity direction. gate_reciprocity (engine/m1/gates.py) already
    # covers the full record set every gate run; this is a force-scoped
    # restatement of that same check, not a separate weaker one.
    for rid, r in recs.items():
        for rel in r.get("relations") or []:
            tgt = rel["target"]
            if rid not in forces and tgt not in forces:
                continue
            inv = RELATION_INVERSE[rel["type"]]
            if tgt in recs:
                back = any(x["type"] == inv and x["target"] == rid for x in recs[tgt].get("relations") or [])
                if not back:
                    bad.append((rid, rel["type"], tgt))
    lines.append(
        "All relations touching a force record reciprocate (both directions checked: force->gravity "
        "and gravity->force)."
        if not bad
        else "NON-RECIPROCAL: " + str(bad)
    )

    lines += ["", "---", "<!-- generated by generate_forces_index.py -->", ""]

    out = pathlib.Path(__file__).resolve().parent / "FORCES-INDEX.md"
    out.write_text("\n".join(lines))
    print(f"wrote {out} | forces: {len(forces)} | unplaced: {len(missing_cell)} | non-reciprocal: {len(bad)}")


if __name__ == "__main__":
    main()
