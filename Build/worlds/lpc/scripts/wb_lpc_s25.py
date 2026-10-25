"""Latin Pastoral-Congregational Christianity (`lpc`): gravity and force records.

Converts this world's Gravity Discovery (Doc_04_Gravity_Discovery.md) and Forces Document
(Doc_08_Forces_Document.md) into record-native `gravity` and `force` records under
records/lpc/gravity/ and records/lpc/force/, per the schema in engine/m1/schemas.py and the
gates in engine/m1/gates.py. It uses the same method as
Build/worlds/don/scripts/wb_don_s25.py: the MECHANICAL versus AUTHORED field split and the
RELATION_PAIRS closed-graph technique. The required fields are the same as don's:
name, description, manifestations, classification for gravity; name, kind, description,
manifestations, matrix_cell for force.

WHAT THE TWO DOCUMENTS FIX
  - Doc_04 §4 (Classification Summary) classifies eight candidate gravities. PRIMARY:
    Candidate 1 (Pastoral Office as Flock-Keeping), 2 (Penitential Discipline), 3 (Collegial
    Communion Preserved), 6 (Sacramental/Ordination Validity). SUPPORTING: Candidate 4
    (Preaching and Catechesis), 5 (Conciliar Authority Theory), 7 (Grace and Human
    Incapacity). TENSIONAL: Candidate 8 (Confessor-Authority vs. Episcopal-Regulated Peace).
    Doc_08 §1 labels them G1-G8 in Doc_04's order, so G1-G8 map one to one onto Candidates
    1-8. This script uses the G1-G8 labels in ids and comments, and never renumbers or
    reclassifies.
  - Doc_08 §3 and §9 identify seventeen forces across the six-cell matrix (1A: 2, 1B: 3,
    2A: 4, 2B: 5, 3A: 1, 3B: 2). lpc_Force_Index.md §1 lists the same 17 force ids, cells and
    confidence tiers. This script builds all 17.

lpc_Force_Index.md is a cross-check only. Open_Gaps_Tracking.md OG-3 records that
gen_force_index.py, the Index's generator, has findings that have not been independently
re-reviewed. The Index's derived tables (§1 Master Force Table, §3 By Connected Gravity, §4
Cross-Cell Connection Map) serve as a check on Doc_08's prose. Every RELATION_PAIRS edge
comes from Doc_08 §4 and §5 directly, and every gravity classification and six-test finding
comes from Doc_04 directly. The Index does not cover gravities' six-test results at all.

INPUTS and OUTPUTS
  - Doc_04 §1-§2 (Candidate Generation; candidates considered and not advanced), §3
    (Per-Candidate Testing), §4 (Classification Summary), §5 (Article 21 Status Check, this
    world's strand-singular, phase-testing substitute), §6 (Interaction Matrix), §7 -> the 8
    `gravity` records, one per classified candidate. classification is copied from Doc_04
    §4's summary table and never re-derived, including Candidate 5's Supporting status
    (see G5 below). description carries each candidate's six-test verdict, its
    Confidence/Gravity Cross-Check result, and its forces-connection summary.
  - Doc_08 §1 (World Identification; the confirmed gravity spine), §2 (Preliminary Forces
    Identification), §3 (the six-cell matrix: all seventeen forces, three layers each), §4
    (Cross-Cell Connections: fourteen named connections and the one deliberate
    non-connection at 2A-2), §5 (Forces-and-Gravities Synthesis), §7 (Confidence
    Assessment), §9 (Completion Certification) -> the 17 `force` records. matrix_cell is
    copied from each force's cell heading (1A, 1B, 2A, 2B, 3A, 3B, the schema's six fixed
    codes). Doc_08's prose label for cells 3A and 3B, "Ending-Transforming", stays in the
    record body, not in matrix_cell. kind follows the cell: 1A and 1B are initiating, 2A and
    2B are ongoing, 3A and 3B are ending. description carries each force's Layer 1
    (Historical Event), Layer 2 (World's Own Experience) and Layer 3 (Formation Impact).
  - The lpc.source.* ids emitted by Build/worlds/lpc/scripts/wb_lpc_s21.py (207 ids, each
    mapped from its external_ids.lpc_source_registry_row) -> sources[] on each gravity and
    force record, resolved to the Registry rows Doc_04 and Doc_08 cite as that candidate's
    or force's evidentiary base. Doc_04, Doc_08 and lpc_Force_Index.md are not vendored
    sources and are never cited in sources[]. Citations to Doc_04 and Doc_08 sit in each
    record's description and body, for example "(Doc_04 §3.1)".

TWO CASES OF EMPTY sources[]
  - Force 1A-2 (the standing legal condition of an unlicensed religion): Doc_08 cites
    Doc_01 §2 and Doc_02 §5, this world's own governing documents and not a vendored
    Registry row, for a background legal condition that this world's corpus does not narrate
    directly.
  - Forces 2B-3 (the illegal-to-established shift) and 3B-2 (Transmission, the 133-year
    silence) rest on a fact about this world's own Registry (a placement judgment at 2B-3;
    the dated-row gap at 3B-2), not on a vendored text that makes a claim.
  Force 1B-3 (the inherited Latin theological vocabulary) cites only Letter CCIX §3, for its
  Punic sentence. Doc_08 cites Doc_01 §6-§7 and Doc_02 §2's "Tertullian disclosure" for the
  rest. Tertullian's corpus is Registry row 29, Boundary Status EXCLUDED (see
  wb_lpc_s21.py). No lpc.source.tertullian-* record exists, and none is invented.

MECHANICAL and AUTHORED fields
  - id, world_id, record_type, schema_version, status, register are mechanical.
    register is "etic" throughout, as in don and in pahc.gravity.boundary-drawing and
    pahc.force.boundary-drawing: these are analytical build documents in record form, not
    first-person emic voice. Neither gate_voice_perspective's PERSPECTIVE_FIELDS nor
    gate_no_build_attribution's ATTRIBUTION_FIELDS (both in engine/m1/spoken_fields.py)
    names gravity or force, so these records may cite "Doc_04 §3.1" in their prose, as
    Doc_04 and Doc_08 do. world_id is "latin-pastoral-congregational-christianity".
  - canon_cells comes from CANON_CELLS and is [] for any record not listed.
  - name and classification (gravity), name, kind and matrix_cell (force) are mechanical,
    as described above.
  - description is authored: Doc_04 §3's six-test verdicts (gravity) or Doc_08 §3's
    three-layer entries (force), condensed and carrying the argument, not a pointer back.
  - manifestations[] is authored from concrete, vendored facts, named events and direct
    quotations that Doc_04 and Doc_08 quote or cite by locus. It never adds a fresh
    translation or an outside historical fact.
  - confidence.formation_confidence is authored per record from each candidate's
    Confidence/Gravity Cross-Check (Doc_04 §3.x) or each force's §7 tier (Doc_08). Where the
    documents name a split across tiers (G3, G5, force 2B-3, force 3B-2), the record carries
    the more conservative tier as its top-line rating and states the split in
    divergence_note.
  - confidence.verification_state is `verified-via-authority` throughout, never
    verified-direct. The records rest on the completed, independently reviewed six-test
    and three-layer assessments, not on a fresh reading of the vendored primary texts.
  - confidence.divergence_note is always populated, so gate_confidence_crosscheck is
    satisfied (Documented with a null divergence_note and no verified-direct is the one
    combination it rejects).
  - confidence.citation_specificity and evidentiary_weight are authored from Doc_04's and
    Doc_08's own evidentiary texture. citation_specificity is "A" where the primary loci sit
    at Registry Confidence A, and "B" where Doc_04 states that the loci relied on sit at
    Confidence B. evidentiary_weight is `load-bearing` throughout except Candidate 5, which
    is `contested`: its six-test profile is narrow throughout, its classification rests on a
    decision made outside the six-test evidence, and Doc_04 §7 item 1 carries its
    Confidence/Gravity divergence forward.
  - sources[] is authored: the lpc.source.* ids that Doc_04 §1 and §3 or Doc_08 §3 cite for
    the candidate or force. A source id may carry its own locus (see src()).
  - relations[] is built by relations_for() from RELATION_PAIRS, OTHER_TYPE_EDGES_FIRST and
    OTHER_TYPE_EDGES_LAST.

RELATIONS
Every edge is an associated-with edge, except that a demonstration edge is `illustrated-by`.
RELATION_PAIRS lists each gravity and force edge once, and both directions are derived from
it.
  1. Gravity to gravity (Doc_04 §6, the Interaction Matrix). Each pair that Doc_04 §6 marks
     Reinforcing, Competing, or Reshapes is one edge. Fifteen pairs exist (G1-G2, G1-G3,
     G1-G4, G1-G5, G1-G6, G1-G8, G2-G3, G2-G4, G2-G6, G2-G7, G2-G8, G3-G5, G3-G6, G4-G7,
     G5-G6). Every other cell reads "No demonstrated relationship in this world's own Native
     record" and is not an edge. Doc_04 §6 names no single "no relationship" pair as a
     finding of its own. Its closing paragraph records the pattern in aggregate, so no
     gravity record carries a dedicated "no relationship named" paragraph. The label
     Reinforcing, Competing or Reshapes is not a schema relation type, so each gravity's
     description carries it in prose.
  2. Gravity to force (Doc_08 §5, "Gravity-by-Gravity Force Connections", which matches
     lpc_Force_Index.md §3). Each force that a gravity lists as connected is one edge. G4's
     force set expands Doc_08 §5's prose reference "every force in Cell 2A", as the Index's §3
     does. Exactly three forces carry no gravity connection: 2B-3, 2B-5 and 3B-2. Doc_04 §2
     declined to advance the shift behind 2B-3 as a gravity, and 2B-5 and 3B-2 are the two
     Transmission-dimension forces, which Doc_08 §5 calls "cross-cutting rather than
     gravity-specific". Forces 1A-2 and 1B-3 do connect, to G1 and G4. They have empty
     sources[], which is a separate matter (see above).
  3. Force to force (Doc_08 §4). The fourteen connected pairs are edges. The fifteenth row,
     2A-2 to none, is a deliberate non-connection that Doc_08 states ("the plague connects
     to no other force in this matrix"). It is not an edge and is stated in Force 2A-2's
     body. The direction and character of each connection (produces, enables, triggers,
     activates, intensifies, shapes, inverts into, reacts to, is the sole instance of,
     continues, coincides with without causing) sit in each force's description, not in the
     relation type. The directional relation types would overclaim: Doc_08 states 2B-4 to
     3B-2 as "is the sole instance of" and 3A-1 to 3B-1 as "coincides with, does not cause".
  4. Edges to records of other types (doctrinal_witness, honest_limit, demonstration,
     contested_claim) come from OTHER_TYPE_EDGES_FIRST and OTHER_TYPE_EDGES_LAST. G1, G2, G3,
     G4, G6 and G7 each carry three edges to the sermon quote records that wb_lpc_s24.py emits, as the
     inverse of the edges those quotes declare.

G5 (CONCILIAR AUTHORITY THEORY)
Candidate 5 is the one gravity whose classification Doc_04 does not reach on its own
six-test evidence: "Alone among the eight candidates, this line does not record this
document's own verdict on the evidence" (Doc_04 §3). Its Supporting class rests on a
decision made outside the six-test evidence, and Doc_04 §7 items 7-8 record a precedent
that stops further revision of it. The script carries "supporting" exactly as Doc_04
states it, neither upgraded nor downgraded, and the record's body says the classification is
not a six-test verdict. confidence.formation_confidence is the more conservative
"Inferential-Thin": the organizing-breadth claim is thin across the whole world, at one
locus per bishop over more than a century (Doc_04 §5, "thin across the span, not bounded
within it"). "Documented" covers only the bare existence of the two formulas (Doc_04 §3's
Cross-Check). divergence_note states the split, and here it carries real weight.

NOT DONE HERE: assigning canon_cells beyond CANON_CELLS; touching records/lpc/{source,
world_core,term,story,figure,quote}/ or wb_lpc_s24.py (existing records are read only, for
their lpc.source.* ids); building contested_claim, voice_craft, demonstration,
doctrinal_witness, honest_limit or ambient records; declaring relations[] from a gravity or
force record to any lpc.story.*, lpc.figure.* or lpc.term.* record (this keeps
the relation graph closed, as don's B-4 script does); running the M2 compiler; registering
`lpc` in records/worlds/; touching gen_force_index.py or lpc_Force_Index.md.
"""
from __future__ import annotations

from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[3]  # .../CIC-Project
RECORDS_ROOT = REPO_ROOT / "records" / "lpc"

WORLD_ID = "latin-pastoral-congregational-christianity"
SCHEMA_VERSION = 2

WRITTEN: list[str] = []

# ---------------------------------------------------------------------------
# Gravity ids (Doc_08's own G1-G8 short labels for Doc_04's Candidate 1-8)
G1 = "lpc.gravity.pastoral-office-flock-keeping"
G2 = "lpc.gravity.penitential-discipline"
G3 = "lpc.gravity.collegial-communion-preserved"
G4 = "lpc.gravity.preaching-and-catechesis"
G5 = "lpc.gravity.conciliar-authority-theory"
G6 = "lpc.gravity.sacramental-ordination-validity"
G7 = "lpc.gravity.grace-and-human-incapacity"
G8 = "lpc.gravity.confessor-authority-vs-episcopal-peace"

# Force ids (Doc_08 §3's own force IDs)
F1A1 = "lpc.force.decian-persecution-libelli-system"
F1A2 = "lpc.force.standing-legal-condition-unlicensed-religion"
F1B1 = "lpc.force.organized-carthaginian-church"
F1B2 = "lpc.force.congregational-acclamation-overriding-preference"
F1B3 = "lpc.force.inherited-latin-theological-vocabulary"
F2A1 = "lpc.force.valerianic-persecution"
F2A2 = "lpc.force.plague-of-cyprian"
F2A3 = "lpc.force.donatist-schism"
F2A4 = "lpc.force.manichaeism-and-pelagian-anthropology"
F2B1 = "lpc.force.recurring-contest-failed-member"
F2B2 = "lpc.force.confessors-claim-to-grant-peace"
F2B3 = "lpc.force.illegal-to-established-shift"
F2B4 = "lpc.force.augustine-engagement-cyprian-conciliar-acts"
F2B5 = "lpc.force.transmission-institutionally-dominant-side"
F3A1 = "lpc.force.vandal-invasion-siege-of-hippo"
F3B1 = "lpc.force.corpus-outliving-the-world"
F3B2 = "lpc.force.transmission-asymmetric-span-133-year-silence"

# RELATION_PAIRS: the whole closed relation graph across gravity and force
# records, each edge listed once as (a, b) -- both directions derived by
# relations_for() below, "associated-with" throughout. The Reinforcing/Competing/Reshapes
# label and each cross-cell connection's direction and character are carried in prose
# (see the module docstring).
RELATION_PAIRS: list[tuple[str, str]] = [
    # --- 1. GRAVITY <-> GRAVITY (Doc_04 §6 Interaction Matrix; 15 edges) ---
    (G1, G2), (G1, G3), (G1, G4), (G1, G5), (G1, G6), (G1, G8),
    (G2, G3), (G2, G4), (G2, G6), (G2, G7), (G2, G8),
    (G3, G5), (G3, G6),
    (G4, G7),
    (G5, G6),

    # --- 2. GRAVITY <-> FORCE (Doc_08 §5 Gravity-by-Gravity Force
    # Connections, cross-checked against lpc_Force_Index.md §3; 29 edges) ---
    (G1, F1A1), (G1, F1A2), (G1, F1B2), (G1, F2A1), (G1, F2A2), (G1, F3A1),
    (G2, F1A1), (G2, F1B1), (G2, F2B1), (G2, F2B2),
    (G3, F1B1), (G3, F2A3), (G3, F2B4),
    (G4, F1B3), (G4, F2A1), (G4, F2A2), (G4, F2A3), (G4, F2A4),
    (G5, F1B1), (G5, F2A3), (G5, F2B4),
    (G6, F2A3), (G6, F2B1), (G6, F2B4),
    (G7, F2A4), (G7, F3B1),
    (G8, F1A1), (G8, F2A1), (G8, F2B2),

    # --- 3. FORCE <-> FORCE (Doc_08 §4 Cross-Cell Connections; 14 edges --
    # 2A-2's own deliberate non-connection is NOT here; see this force's
    # own body text) ---
    (F1A1, F2B1),          # produces
    (F1A1, F2B2),          # produces
    (F1A2, F1B2),          # shapes
    (F1A2, F2B3),          # inverts into
    (F1B1, F1B2),          # enables
    (F1B1, F2B4),          # enables
    (F2A1, F1A1),          # reacts to
    (F2A3, F2B4),          # triggers
    (F2A3, F2B3),          # activates
    (F2A4, F3B1),          # produces
    (F2B2, F2B1),          # intensifies
    (F2B4, F3B2),          # is the sole instance of
    (F2B5, F3B2),          # continues
    (F3A1, F3B1),          # coincides with, does not cause
]



# Canon cells per record; a record not listed carries none.
CANON_CELLS: dict[str, list[str]] = {
    G1: ["F3-I"],
    G2: ["F4-I"],
    G3: ["F3-T"],
    G4: ["F2-I"],
    G5: ["F1-I"],
    G6: ["F6-I"],
    G7: ["F1-T"],
    G8: ["F6-I"],
    F1A1: ["F4-I"],
    F1A2: ["F3-I"],
    F1B1: ["F3-I"],
    F1B2: ["F3-I"],
    F1B3: ["F2-I"],
    F2A1: ["F5-P"],
    F2A2: ["F5-I"],
    F2A3: ["F6-T"],
    F2A4: ["F1-T"],
    F2B1: ["F4-I"],
    F2B2: ["F6-I"],
    F2B4: ["F6-I"],
    F2B5: ["F2-E"],
    F3A1: ["F5-I"],
    F3B2: ["F2-E"],
}

# Edges from a gravity or force record to records of other types (doctrinal_witness,
# honest_limit, demonstration, contested_claim, quote), as (type, target). OTHER_TYPE_EDGES_FIRST edges
# come before the pair-derived edges and OTHER_TYPE_EDGES_LAST edges after them.
OTHER_TYPE_EDGES_FIRST: dict[str, list[tuple[str, str]]] = {
    G1: [
        ("associated-with", "lpc.witness.answerability-as-ground"),
    ],
    G2: [
        ("illustrated-by", "lpc.demo.road-back-examined"),
        ("associated-with", "lpc.witness.answerability-as-ground"),
        ("associated-with", "lpc.witness.confessor-claim-vs-regulated-peace"),
    ],
    G3: [
        ("associated-with", "lpc.witness.communion-over-separation"),
    ],
    G5: [
        ("associated-with", "lpc.limit.411-gesta-unread"),
        ("associated-with", "lpc.witness.tradition-tested-by-apostolic-warrant"),
    ],
    G6: [
        ("illustrated-by", "lpc.demo.font-twice-answered"),
    ],
    G7: [
        ("associated-with", "lpc.contested.grace-pelagius-characterization"),
        ("associated-with", "lpc.witness.violence-commanded-not-cruel"),
    ],
    G8: [
        ("associated-with", "lpc.witness.confessor-claim-vs-regulated-peace"),
    ],
    F2B3: [
        ("associated-with", "lpc.contested.compel-coercion-development"),
    ],
}

OTHER_TYPE_EDGES_LAST: dict[str, list[tuple[str, str]]] = {
    G1: [
        ("associated-with", "lpc.quote.ye-belong-to-my-care"),
        ("associated-with", "lpc.quote.stewards-and-future-bishops"),
        ("associated-with", "lpc.quote.good-works-the-comfort-of-our-dangers"),
    ],
    G2: [
        ("associated-with", "lpc.quote.bind-him-justly"),
        ("associated-with", "lpc.quote.reprove-and-forgive-the-surgeons-knife"),
        ("associated-with", "lpc.quote.peter-the-sick-man-and-the-physician"),
    ],
    G3: [
        ("associated-with", "lpc.quote.one-good-shepherd-not-many"),
        ("associated-with", "lpc.quote.apart-in-heart-united-in-body"),
        ("associated-with", "lpc.quote.going-out-without-violating-unity"),
    ],
    G4: [
        ("associated-with", "lpc.quote.the-creed-first-then-the-prayer"),
        ("associated-with", "lpc.quote.let-your-creed-be-a-mirror"),
        ("associated-with", "lpc.quote.the-sermon-and-the-readings-are-daily-bread"),
    ],
    G6: [
        ("associated-with", "lpc.witness.baptism-traced-to-the-apostles"),
        ("associated-with", "lpc.quote.the-branch-cut-from-the-vine"),
        ("associated-with", "lpc.quote.pardon-through-a-wicked-clergyman"),
        ("associated-with", "lpc.quote.consider-who-was-there"),
    ],
    G7: [
        ("associated-with", "lpc.quote.two-hear-one-scorns-one-rises"),
        ("associated-with", "lpc.quote.what-is-done-by-you-he-does-in-you"),
        ("associated-with", "lpc.quote.no-one-has-the-love-of-god-from-himself"),
    ],
}


def relations_for(rid: str) -> list[dict]:
    out = [{"type": t, "target": target} for t, target in OTHER_TYPE_EDGES_FIRST.get(rid, [])]
    for a, b in RELATION_PAIRS:
        if a == rid:
            out.append({"type": "associated-with", "target": b})
        elif b == rid:
            out.append({"type": "associated-with", "target": a})
    out += [{"type": t, "target": target} for t, target in OTHER_TYPE_EDGES_LAST.get(rid, [])]
    return out


def conf(cite, verify, weight, formation, divergence):
    assert divergence is not None, (
        "every gravity/force record's own divergence_note is authored and populated, never "
        "null"
    )
    return {
        "citation_specificity": cite,
        "verification_state": verify,
        "evidentiary_weight": weight,
        "formation_confidence": formation,
        "divergence_note": divergence,
    }


def src(*entries):
    """Each entry is a source id, or an (id, locus) pair that replaces the default locus."""
    default_locus = ("see this record's own body text for the specific locus "
                     "Doc_04/Doc_08 cite")
    return [{"source_id": e if isinstance(e, str) else e[0],
             "locus": default_locus if isinstance(e, str) else e[1],
             "license": "public-domain"} for e in entries]


def _write(record_type: str, rid: str, payload: dict, body: str) -> None:
    out_dir = RECORDS_ROOT / record_type
    out_dir.mkdir(parents=True, exist_ok=True)
    front = yaml.safe_dump(payload, sort_keys=False, allow_unicode=True, width=100)
    text = f"---\n{front}---\n{body.strip()}\n"
    path = out_dir / f"{rid}.md"
    path.write_text(text, encoding="utf-8")
    WRITTEN.append(str(path))


def emit_gravity(rid, name, classification, description, manifestations, confidence, sources, body):
    payload = {
        "id": rid,
        "world_id": WORLD_ID,
        "record_type": "gravity",
        "schema_version": SCHEMA_VERSION,
        "status": "draft",
        "register": "etic",
        "canon_cells": CANON_CELLS.get(rid, []),
        "confidence": confidence,
        "sources": sources,
        "relations": relations_for(rid),
        "name": name,
        "description": description,
        "manifestations": manifestations,
        "classification": classification,
    }
    _write("gravity", rid, payload, body)


def emit_force(rid, name, kind, matrix_cell, description, manifestations, confidence, sources, body):
    payload = {
        "id": rid,
        "world_id": WORLD_ID,
        "record_type": "force",
        "schema_version": SCHEMA_VERSION,
        "status": "draft",
        "register": "etic",
        "canon_cells": CANON_CELLS.get(rid, []),
        "confidence": confidence,
        "sources": sources,
        "relations": relations_for(rid),
        "name": name,
        "kind": kind,
        "description": description,
        "manifestations": manifestations,
        "matrix_cell": matrix_cell,
    }
    _write("force", rid, payload, body)


# ===========================================================================
# GRAVITIES (8) -- Doc_04 §3, classification per §4's own summary table.
# ===========================================================================

def build_gravities() -> None:
    emit_gravity(
        G1, "Pastoral Office as Territorial Flock-Keeping",
        "primary",
        "This is the concern everything else in this world turns on. A bishop is personally "
        "answerable for a bounded flock, and much of the rest of the world flows from that.\n"
        "\n"
        "It recurs in every primary source, for both bishops and both phases. It appears in both "
        "bishops' stories of coming to office. It appears in the crisis letters of both phases. It "
        "appears in Cyprian's letters and treatises. It appears in Augustine's sermons.\n"
        "\n"
        "Other concerns in this world depend on it. A bishop who holds this office carries out "
        "penitential discipline. Preaching and catechesis are the main work of the office. "
        "Conciliar authority is a theory about who holds the office by right. Sacramental validity "
        "asks the same thing. This world's formation is pastoral and sacramental before it is "
        "legal. All the teaching and penance exists because a bishop answers for his flock in "
        "person.\n"
        "\n"
        "It explains why Cyprian's crisis letters exist at all. It explains why Augustine's sermon "
        "collection is so large. It explains why both bishops' accounts of coming to office are "
        "attested separately. They are treated as formative. It shows in Carthage and in Hippo, in "
        "both phases, in the bishops' own words. It reinforces penitential discipline and "
        "collegial communion. It reinforces preaching and catechesis. It reinforces sacramental "
        "validity and the confessor tension. Conciliar authority reinforces it only weakly. No "
        "link with grace and human incapacity has been shown.\n"
        "\n"
        "The evidence is solid. Accounts of holding and using this office are quoted directly and "
        "checked. They are the preface to the Council of 256, Augustine's Letters XXXI and CCXIII, "
        "and Pontius's narrative. Possidius's Life of Augustine is not counted in this rating, "
        "though it has since been read in full. So the rating rests on Pontius, the two letters, "
        "and the 256 preface alone.\n"
        "\n"
        "It is the concern most closely tied to the forces acting on the world. In law, "
        "Christianity was an unlicensed religion. So the office has no outside enforcement. A "
        "personal bond holds it together. The congregation's acclamation shows how a man comes to "
        "hold the office. The Decian and Valerianic persecutions make a bishop's duty to his flock "
        "acute. They work through the flock's own failure and the bishop's own test. The plague is "
        "a pressure the bishop shares. He does not judge it. The Vandal invasion and the siege of "
        "Hippo mark where the bond ends. It ends when the bishop does.",
        [
            "\"it is the shepherd that is chiefly wounded in the wound of his flock\" (Cyprian, "
            "De Lapsis)",
            "Cyprian's own account of holding and exercising this office at the 256 Council "
            "preface; Augustine's own account in Letters XXXI and CCXIII",
            "Pontius's narrative of Cyprian's conduct as bishop",
        ],
        conf("A", "verified-via-authority", "load-bearing", "Documented",
             "Doc_04 §3 Candidate 1: no divergence. Evidence reaches Documented -- both bishops' "
             "own accounts of holding and exercising this office are directly quoted and "
             "independently re-verified. Possidius's Vita (Registry row 192) is not part of this "
             "Cross-Check and is not counted toward it."),
        src("lpc.source.cyprian-epistles",
            "lpc.source.cyprian-seventh-council-of-carthage",
            "lpc.source.pontius-life-and-passion-of-cyprian"),
        "Taken from Doc_04 §3 (Candidate 1), cross-checked against Doc_04 §4's own Classification "
        "Summary and §6's own Interaction Matrix. relations[] carries the gravity<->gravity edges "
        "(G2, G3, G4, G5, G6, G8) and the gravity<->force edges (1A-1, 1A-2, 1B-2, 2A-1, 2A-2, "
        "3A-1) named in this record's own description above.",
    )

    emit_gravity(
        G2, "Penitential Discipline: the Reintegration of the Failed",
        "primary",
        "How the church took back its failed members sat near the center of this world's life. "
        "This concern asks what happens to someone who gave way under persecution. Its answer is "
        "to take that person back, not shut that person out for good.\n"
        "\n"
        "It recurs strongly: in De Lapsis, in the letters about the lapsed, in Pontius's "
        "narrative, and in the world's liturgical evidence. One more limit belongs here. "
        "Cyprian's phase has several independent sources that support each other. But the claim "
        "that this concern spans both phases rests on Cyprian's phase alone.\n"
        "\n"
        "Other concerns in this world depend on it. The confessor tension exists only because "
        "this one does. Its answer for one believer is to take that person back, not shut that "
        "person out for ever. That mirrors, at a smaller scale, the logic of collegial communion. "
        "It is the model way of shaping believers in this world's record. It explains two "
        "schisms. The Novatianists refused to readmit the lapsed at all. The Felicissimus schism "
        "offered an easier rival road back. It also explains the confessor tension.\n"
        "\n"
        "Whether it continues into Augustine's phase was checked directly, not assumed. It holds "
        "directly for Cyprian's phase. For Augustine's phase, the case for continuity does not "
        "fully survive. It does not hold as this same concern under its own name. No text we "
        "tested from Augustine's phase is built around a crisis like that of the lapsed, at the "
        "same acute, empire-wide scale. We have not tested the sermons now in scope.\n"
        "\n"
        "The closest parallels are real: the pull toward the Donatist schism, and the ordinary "
        "sin of catechized believers. Those were tested. They proved to be concerns of their own: "
        "sacramental validity, and grace and human incapacity. They are not its direct "
        "continuation. Between the phases there is a family resemblance, not the same concern "
        "restated.\n"
        "\n"
        "It reinforces pastoral office, collegial communion, preaching and catechesis, and "
        "sacramental validity. Grace and human incapacity reshapes it without continuing it. It "
        "competes with the confessor tension.\n"
        "\n"
        "The evidence is solidly attested for Cyprian's own conduct and letters, which are "
        "directly quoted and checked. The De Lapsis passage carries the lower citation grade (B). "
        "The Epistles and Pontius passages carry the higher grade (A). None of it runs short of "
        "evidence for Cyprian's phase.\n"
        "\n"
        "It is itself this world's ongoing internal pressure. Four forces connect to it. The "
        "Decian persecution created its subject matter. The organized Carthaginian church made a "
        "regulated process possible at all. It answers the recurring contest over the failed "
        "member. It was built against a rival claim, the confessors' claim to grant peace. Its "
        "life in the second phase is qualified, not assumed: the concern does not continue under "
        "its own name. So its ties to the forces stay rooted in the first phase.",
        [
            "De Lapsis, Cyprian's founding treatise of the penitential controversy",
            "the Novatianist schism (a rigorist refusal to readmit the lapsed) and the "
            "Felicissimus schism (a laxer rival route back), both explained by this concern",
            "the confessors' competing claim to grant peace, which the regulated penitential "
            "process was built to answer",
        ],
        conf("A", "verified-via-authority", "load-bearing", "Documented",
             "Doc_04 §3 Candidate 2: no divergence for the Cyprian-phase gravity. Evidence reaches "
             "Documented for Cyprian's own conduct and correspondence; of the loci relied on, the De "
             "Lapsis locus (Registry row 2) sits at Confidence B, the Epistles and Pontius loci (rows "
             "1, 7) at A. The Persistence test, tested rather than assumed per Doc_01 §8 item 7, finds "
             "the lean toward an Augustine-phase continuation does NOT survive under this gravity's "
             "own name -- what survives is a family resemblance toward Candidates 6 and 7, its own "
             "distinct finding named at Doc_04 §3 and §5, not a confidence divergence but a scope "
             "finding carried here for completeness."),
        src("lpc.source.cyprian-epistles",
            "lpc.source.cyprian-de-lapsis",
            "lpc.source.pontius-life-and-passion-of-cyprian"),
        "Taken from Doc_04 §3 (Candidate 2). relations[] carries the gravity<->gravity edges (G1, "
        "G3, G4, G6, G7, G8) and the gravity<->force edges (1A-1, 1B-1, 2B-1, 2B-2) named above "
        "-- 2B-1's own asymmetric family-resemblance finding (first-phase, toward G6, not toward "
        "G7) is discussed at G6's own record below, per Doc_08 §5's own G6 entry.",
    )

    emit_gravity(
        G3, "Collegial Communion Preserved Despite Disagreement",
        "primary",
        "Few things mattered more to this world than staying in communion despite real "
        "disagreement. Bishops here disagree, sometimes sharply. But they work to keep communion "
        "rather than break it and build a rival hierarchy.\n"
        "\n"
        "The pattern recurs across both phases. Cyprian's preface to the Council of 256 states it "
        "directly: \"neither does any of us set himself up as a bishop of bishops... every "
        "bishop... has his own proper right of judgment.\" Augustine's On Baptism argues at length "
        "against Cyprian's own ruling on rebaptism. Yet it never treats him as outside communion. "
        "Letter 185 takes the same tone with the Donatist split: a pastor's tone, meant to "
        "correct.\n"
        "\n"
        "Our own case for this world's coherence across the century between its two bishops rests "
        "on this concern. A bishop who disagrees has two paths. He can work to keep communion, or "
        "he can break it and set up a parallel hierarchy. Both bishops take the first path. Over "
        "rebaptism, the sharpest dispute between them, neither breaks fellowship with a fellow "
        "bishop. The fight over grace went another way. African councils condemned what the "
        "Pelagians taught. So the concern has a scope. It governs disagreement over practice "
        "among bishops in communion. It does not reach teaching a council judged heresy.\n"
        "\n"
        "This explains why Augustine's long, respectful argument with a bishop he disputes reads "
        "as a son arguing with a father, not a rejection. It also explains where this world draws "
        "its line against Donatism. The pattern shows in both phases, in how both bishops act, not "
        "just in a shared word. It supports four other concerns: the pastor's office, the "
        "discipline of penance, the weight of councils, and whether a sacrament is valid. That "
        "last question is where it is tested hardest.\n"
        "\n"
        "The confidence split is named, not resolved. The facts beneath it are well attested. The "
        "256 preface's own words and On Baptism's long argument are directly quoted and checked. "
        "But to read them as one concern across both phases, not two separate facts, is our own "
        "reading. That reading stands at Widely Accepted. The record carries this more cautious "
        "rating rather than hide the split.\n"
        "\n"
        "Every force linked to this concern tested it rather than created it. The organized church "
        "at Carthage gave it colleagues who could meet and who already disagreed. The Donatist "
        "schism tested it at its hardest edge. Augustine's reading of Cyprian's council acts "
        "tested it across the century gap. This world's own bishops kept it each time. It is this world's own way of "
        "adapting, tested three times from three directions.",
        [
            "Cyprian's preface to the Council of 256: \"neither does any of us set himself up as "
            "a bishop of bishops... every bishop... has his own proper right of judgment\"",
            "Augustine arguing at length against Cyprian's rebaptism ruling throughout On "
            "Baptism, while never treating him as outside communion",
            "Letter 185's pastoral, corrective tone toward the Donatist schism",
        ],
        conf("A", "verified-via-authority", "load-bearing", "Widely Accepted",
             "Doc_04 §3 Candidate 3: divergence flagged rather than resolved. The underlying "
             "primary-source facts (the 256 preface's own words; On Baptism's own extensive argument) "
             "reach Documented, directly quoted and re-verified across Doc_01's nine rounds; the "
             "SYNTHESIS naming these facts one cross-phase gravity, rather than two separate "
             "historical facts, is this document's own reasoning at Widely Accepted confidence -- this "
             "record carries the more conservative tier as its own top-line rating rather than "
             "smoothing the split away, per Doc_04 §4's own Classification Summary: 'the one-gravity "
             "synthesis itself Widely Accepted, not upgraded.'"),
        src("lpc.source.cyprian-seventh-council-of-carthage",
            "lpc.source.augustine-correction-of-the-donatists",
            "lpc.source.augustine-on-baptism-against-the-donatists"),
        "Taken from Doc_04 §3 (Candidate 3). relations[] carries the gravity<->gravity edges (G1, "
        "G2, G5, G6) and the gravity<->force edges (1B-1, 2A-3, 2B-4) named above.",
    )

    emit_gravity(
        G4, "Preaching and Catechesis as the Primary Mode of Formation",
        "supporting",
        "This concern is real too, though its reach is narrower than the others'. It is the means "
        "by which this world's other central concerns are taught. It does not organize the world "
        "by itself. It clearly recurs, shapes believers, and lasts across both phases. But its "
        "links to other concerns, and what it explains, are narrower.\n"
        "\n"
        "It recurs in Augustine's sermons and his Tractates on John, in the works written to teach "
        "those preparing for baptism, and in Cyprian's book on the Lord's Prayer. The pastor's "
        "office depends on it as its main task. But nothing else leans on it the way three "
        "concerns do: the pastor's office, the discipline of penance, and keeping communion. It is "
        "the channel through which those concerns are taught and enforced.\n"
        "\n"
        "Its power to shape believers is strong and direct. That is what the works for those "
        "preparing for baptism are about, and it is the stated aim of both bishops' preaching. It "
        "explains how people were formed more than why any one crisis came. It shows in both "
        "phases, in both bishops' own words. It supports three concerns: the pastor's office, the "
        "discipline of penance, and grace and human incapacity. No link has been shown with four "
        "others: keeping communion, the weight of councils, whether a sacrament is valid, and the "
        "confessors' claim.\n"
        "\n"
        "The evidence is solid for the existence and basic content of these texts. The specific "
        "passages carry the lower citation grade (B), but that is not a thin spot in the "
        "evidence.\n"
        "\n"
        "It depends on a shared language to teach in: the Latin words for the faith that this "
        "world inherited. It also connects to every outside pressure that kept bearing on the "
        "world. These are the Valerianic persecution, the plague, the Donatist split, and the "
        "rival teachings of the Manichees and the Pelagians. This concern is the channel through "
        "which outside pressure reaches an ordinary believer. That is how this world tends to "
        "respond: it turns crisis into teaching. The plague is the clearest case. It produced no "
        "new concern and no new practice, only a treatise, and that treatise came entirely through "
        "preaching and teaching.",
        [
            "the Sermons and Tractates on John: Augustine's vast body of preaching and scripture "
            "commentary",
            "the catechetical works, written explicitly for converts and catechumens",
            "De Mortalitate, Cyprian's treatise answering the plague of c. 249-262: a pressure "
            "that produced teaching, not new structure",
        ],
        conf("B", "verified-via-authority", "load-bearing", "Documented",
             "Doc_04 §3 Candidate 4: no divergence. Documented for existence and basic content, per "
             "Doc_02 §8's own bracket ('the existence and basic content of the major primary texts "
             "named at §1'); the specific loci this candidate rests on sit at Registry Confidence B, "
             "not A -- carried here as the record's own top-line citation_specificity rather than "
             "smoothed to A."),
        src("lpc.source.cyprian-minor-pastoral-treatises",
            "lpc.source.augustine-on-the-catechising-of-the-uninstructed",
            "lpc.source.augustine-creedal-catechetical-works",
            "lpc.source.augustine-sermons-on-selected-lessons",
            "lpc.source.augustine-tractates-on-john-and-related-exegesis"),
        "Taken from Doc_04 §3 (Candidate 4). relations[] carries all three of Doc_04 §6's own "
        "Interaction Matrix edges for Candidate 4 (Reinforcing with G1, Reinforcing with G2, "
        "Reinforcing with G7) -- G1 and G2 appear as edges on their own records, so G7 is the "
        "only edge this record's own row adds, not the only gravity-level relationship G4 has in "
        "total -- and the gravity<->force edges (1B-3, 2A-1, 2A-2, 2A-3, 2A-4, the last four an "
        "expansion of Doc_08 §5's own prose set-reference 'every force in Cell 2A', cross-checked "
        "against lpc_Force_Index.md §3's own identical expansion) named above.",
    )

    emit_gravity(
        G5, "Conciliar Authority Theory: Egalitarian vs. Hierarchical",
        "supporting",
        "This is one of this world's real concerns, though an unusual one to weigh. That two "
        "competing theories of conciliar authority existed, in each bishop's own words, is "
        "solidly attested. Whether they organized much of the world is a separate question, "
        "and the evidence for that is far thinner. We treat this as a secondary concern, "
        "disclosed as genuinely uncertain rather than settled.\n"
        "\n"
        "The concern names two competing theories of conciliar authority. Cyprian's is "
        "egalitarian. In the preface to the Council of 256 he says no bishop sets himself up "
        "as \"a bishop of bishops.\" Augustine's is hierarchical. In On Baptism he appeals to "
        "\"the authority of plenary Councils,\" and the word \"plenary\" occurs 31 times in that "
        "treatise.\n"
        "\n"
        "A real limit sits here too. Both theories recur beyond their main source, but only in "
        "bishops' writing. Cyprian's formula appears at length in the 256 preface. He states "
        "the same freedom of each bishop in his letters to Jubaianus and Magnus, and in the "
        "letter he and his council sent to Stephen. Augustine's theory recurs within On Baptism. He also speaks of plenary Councils "
        "in two of his letters, Letter 43, section 19, and Letter 54, section 1. Those two "
        "passages were found and were not weighed in the six tests.\n"
        "\n"
        "Its reach is narrow in every direction. Only one finding depends on it: that the "
        "world forms a single strand. There is no evidence that ordinary believers, "
        "catechumens, or most clergy in either phase were shaped by this question. Some did "
        "hear it. Presbyters, deacons and a large part of the congregation were present in 256 "
        "when Cyprian stated his formula. It explains the shape of the rebaptism dispute between Cyprian and "
        "Stephen, and Augustine's long argument against Cyprian's ruling. It explains nothing "
        "else in the wider world. It connects clearly with collegial communion and sacramental "
        "validity, and weakly with pastoral office.\n"
        "\n"
        "It does not carry across the whole world. Each theory is still one bishop writing to "
        "other bishops or to his own correspondents. Nothing shows either one at work, or "
        "disputed, among ordinary clergy. This is a limit of the search so far, not a "
        "proven absence. It runs thin across the whole span, not confined to one phase. It "
        "appears in both phases, in a bishop's writing each time -- two bishops, at two moments "
        "separated by over a century. That sets it apart from grace and human incapacity, "
        "which belongs to one phase only.\n"
        "\n"
        "The uncertainty here is disclosed, not resolved. That both formulas exist, in their "
        "own words, is solidly attested. The evidence that they organized much of the world is "
        "much weaker. How central a concern is, and how confident we can be in the evidence, "
        "are two separate things, and here they diverge. So the record stays cautious about "
        "how central this is. We do not ask the 411 Gesta, the proceedings of that year, to "
        "settle it. They have not been read in full.\n"
        "\n"
        "Of everything in this world, this concern connects least to the forces acting on it. "
        "It links to the council setting of the organized Carthaginian church. It links to the "
        "Donatist appeal that supplied the occasion, and to Augustine's engagement with "
        "Cyprian's conciliar acts. But each of these reaches it only through someone quoting a "
        "text, not through pressure on how the church actually lived. That fits the finding "
        "that the question never reached ordinary formation.\n"
        "\n"
        "A concern this loosely connected to the pressures acting on the world leaves our own "
        "picture of that world incomplete here. That gap is carried, not resolved.",
        [
            "Cyprian's egalitarian formula in the preface to the Council of 256: \"neither does any "
            "of us set himself up as a bishop of bishops\"",
            "Augustine's hierarchical formula in On Baptism II.3, invoking \"the authority of "
            "plenary Councils\" (the word \"plenary\" occurs 31 times in the treatise)",
        ],
        conf("B", "verified-via-authority", "contested", "Inferential-Thin",
             "Doc_04 §3 Candidate 5: divergence flagged, not resolved. Existence of both "
             "formulas, in their own words, reaches Documented (directly quoted and re-verified); "
             "the evidential support for their ORGANIZING BREADTH does not reach the same level, "
             "this candidate's six-test profile being narrow throughout and Persistence failing "
             "at world level on a disclosed search bound -- carried at the more conservative "
             "Inferential-Thin tier as this record's own top-line rating rather than the "
             "bare-existence Documented tier, per this candidate's own 'thin across the span, not "
             "bounded within it' finding (Doc_04 §5). The classification itself (Supporting) is "
             "set by override rather than by this document's own six-test verdict -- carried "
             "exactly as Doc_04 §3 states this, neither upgraded nor downgraded here."),
        src("lpc.source.cyprian-seventh-council-of-carthage",
            "lpc.source.augustine-on-baptism-against-the-donatists"),
        "Taken from Doc_04 §3 (Candidate 5). The body follows Doc_04 §5 in keeping this candidate "
        "distinct from Candidate 7 (phase-bound) rather than collapsing the two Persistence "
        "failures into one shape. relations[] carries the gravity-to-gravity edges (G1, G3, G6) "
        "and the gravity-to-force edges (1B-1, 2A-3, 2B-4) named above. The Supporting class "
        "rests on a decision made outside the six-test evidence, and is not presented as a "
        "settled verdict of the tests.",
    )

    emit_gravity(
        G6, "Sacramental and Ordination Validity Across the Boundary of the Church",
        "primary",
        "Few questions mattered more to this world than this one. Is a baptism or an ordination "
        "given outside the church's boundary valid? The two bishops answer it in opposite ways.\n"
        "\n"
        "It comes up again and again: in Cyprian's letters on rebaptism, in the ruling of the "
        "Council of 256, and all through Augustine's On Baptism, a whole book on the question. "
        "Unlike conciliar authority, it is not thin. Two separate bishops argue it at length, more "
        "than a century apart.\n"
        "\n"
        "Other concerns in this world lean on it. Collegial communion is tested hardest here, "
        "because the two bishops reach opposite answers and still stay in communion. The confessor "
        "tension is a close cousin of it: it asks who may grant standing in the church.\n"
        "\n"
        "It shapes practice directly. Cyprian's demand for rebaptism is a working pastoral rule. "
        "Augustine's opposite ruling decides whether Donatist clergy come back in their own orders "
        "or are ordained again. It explains the whole dispute between Stephen and Cyprian. "
        "Augustine wrote a whole treatise on it. It also explains why the Donatists could cite "
        "Cyprian himself for their rebaptism.\n"
        "\n"
        "The question lasts across both phases, even as the answer changes. That in itself shows "
        "how much it mattered. It strengthens pastoral office, penitential discipline, collegial "
        "communion, and conciliar authority.\n"
        "\n"
        "Both sides are well grounded. Each is quoted and checked: On Baptism I.1.2, the 256 "
        "preface, and Book III, chapter 2. Neither side runs short of evidence.\n"
        "\n"
        "The Donatist schism, a steady push from outside, makes the question urgent for the church "
        "as a whole, not just for single converts. Augustine's reading of Cyprian's council acts "
        "reopens it across the century gap. It also ties to the recurring contest over the failed "
        "member, because Cyprian reasons about both questions in the same way.\n"
        "\n"
        "That last link runs one way only. In the first phase, the discipline of penance "
        "strengthens this concern, since both ask about the boundary and about coming back. But "
        "penance relates to grace and human incapacity in a different way: that later concern "
        "reshapes it rather than carrying it on. So this record's tie to the contest over the "
        "failed member is its own, and it belongs to the first phase. It does not rest on the "
        "later family likeness, which runs toward grace and human incapacity instead.",
        [
            "the Council of 256's ruling on rebaptism",
            "On Baptism, Against the Donatists in full, argued at book length (citing I.1.2 and "
            "Book III, chapter 2)",
            "the Epistles' correspondence on rebaptism, and the dispute between Stephen and "
            "Cyprian",
        ],
        conf("A", "verified-via-authority", "load-bearing", "Documented",
             "Doc_04 §3 Candidate 6: no divergence. Both positions directly quoted and "
             "independently re-verified (On Baptism I.1.2; the 256 preface; Book III ch. 2 §2)."),
        src("lpc.source.cyprian-epistles",
            "lpc.source.cyprian-seventh-council-of-carthage",
            "lpc.source.augustine-on-baptism-against-the-donatists"),
        "Taken from Doc_04 §3 (Candidate 6), with the 2B-1 asymmetry independently re-verified "
        "against Doc_08 §5's own G6 entry, which examines and confirms it at length: the "
        "connection is real, not the symmetry it might appear to be. relations[] carries the "
        "gravity<->gravity edges (G1, G2, G3, G5) and the gravity<->force edges (2A-3, 2B-1, "
        "2B-4) named above.",
    )

    emit_gravity(
        G7, "Grace and Human Incapacity",
        "supporting",
        "This concern is real, but it does not run nearly as wide as the others. It organizes a "
        "large and very well attested part of the world, but only in Augustine's phase. It does "
        "not span the whole world the way pastoral office, penitential discipline, collegial "
        "communion, and sacramental validity do.\n"
        "\n"
        "It comes with a real limit, and it should be said plainly rather than left for a reader "
        "to find later. Nearly all the evidence comes from one voice, Augustine, in one body of "
        "work, the anti-Pelagian corpus. So much evidence could easily be taken for breadth.\n"
        "\n"
        "No concern in this world has more text behind it. The word \"grace\" occurs 1,798 times "
        "in the thirteen anti-Pelagian works alone. Those works form a long project of teaching "
        "and argument, prompted by a live dispute. In them Augustine refuses a claim he sets out "
        "as the Pelagian one: that a believer's own moral effort is enough without grace. Whether "
        "Pelagius himself held it in that form is disputed.\n"
        "\n"
        "It is real and heavily attested, but it stands on its own. Nothing else in this world "
        "depends on how it is resolved. It explains why the anti-Pelagian corpus exists and why it "
        "is so large. But the controversy does not reach back to Cyprian. It came more than a "
        "century after him.\n"
        "\n"
        "So it does not span the whole world as a concern. Cyprian states the theme in passing. "
        "His Testimonies say \"we must boast in nothing, since nothing is our own\" (III.4), and "
        "Augustine later quoted those words against the Pelagians. But nothing in Cyprian's phase "
        "organizes formation around it. Within Augustine's phase it is strong. It reshapes "
        "penitential discipline by raising a related but distinct question in Augustine's phase. "
        "It is a separate question, not a continuation of that concern. It reinforces preaching "
        "and catechesis.\n"
        "\n"
        "The corpus's existence and scale are solidly attested. It is held in this project's own "
        "library and has been checked independently. The specific passages relied on carry the "
        "lower citation grade (B). Within Augustine's own phase, that carries no confidence gap of "
        "its own.\n"
        "\n"
        "It has a single origin among the forces, and that is a real finding, not thin analysis. "
        "Manichaeism and Pelagianism, as live rival systems, produced it directly and entirely. "
        "The survival of Augustine's writings beyond the world carries it out of the world. The "
        "forces analysis thus confirms the caution flagged at the start: one outside pressure, one "
        "corpus, one phase.",
        [
            "the anti-Pelagian corpus: thirteen works prompted by a live controversy, with 1,798 "
            "raw occurrences of \"grace\"",
            "Augustine's refusal of a view he sets out as the Pelagian one, that a believer's own "
            "moral effort is enough without grace",
        ],
        conf("B", "verified-via-authority", "load-bearing", "Documented",
             "Doc_04 §3 Candidate 7: no divergence for the Augustine-phase gravity itself. Documented "
             "for the corpus's own existence and scale, directly vendored and independently swept by "
             "Doc_03; per Doc_02 §8's own bracket, the specific loci relied on sit at Registry "
             "Confidence B. Persistence fails at the world level -- Cyprian states the theme in "
             "passing (Testimonia III.4), but no Cyprian-phase evidence of it organizing formation "
             "is identified -- a real temporal boundary named directly rather than a confidence gap."),
        src("lpc.source.augustine-anti-pelagian-corpus"),
        "Taken from Doc_04 §3 (Candidate 7). relations[] carries the gravity<->gravity edges (G2, "
        "G4) and the gravity<->force edges (2A-4, 3B-1) named above, plus one contested_claim "
        "edge (lpc.contested.grace-pelagius-characterization).",
    )

    emit_gravity(
        G8, "Confessor Authority vs. Episcopally Regulated Peace",
        "tensional",
        "This is a tension in this world, not a settled concern. Two real pressures pull against "
        "each other, and neither wins. One limit comes first: the evidence rests mainly on one "
        "source, Cyprian's letters, read through one term in this world's lexicon.\n"
        "\n"
        "The first side is the confessors. These were Christians who held firm when questioned "
        "under persecution. Because of that, they wrote notes asking that named lapsed people be "
        "taken back. This was an informal claim to grant peace. The second side is Cyprian's own "
        "process of penance. The bishop ran it and controlled it. He built it to answer that "
        "rival claim.\n"
        "\n"
        "The tension keeps coming back. Letters XX and XXI show the confessors using this claimed "
        "power themselves, in their own words. De Lapsis and Cyprian's letters on penance show "
        "his answer. Penance has the shape it does because a rival claim to grant peace already "
        "existed. That claim had to be brought under order. The discipline was not invented from "
        "nothing.\n"
        "\n"
        "The tension shapes how Cyprian acts. In his crisis letters he must keep restating the "
        "bishop's power over taking people back. He cannot settle it once. That is why De Lapsis "
        "and the letters on the lapsed press so hard on the bishop's control. Penance alone does "
        "not explain how hard they press.\n"
        "\n"
        "The tension lasts only through Cyprian's crisis years. In those years it is a steady "
        "pressure that is never resolved. It does not organize the world as a whole. That is what "
        "makes it a tension, and it is not a failure. It competes with penance and supports the "
        "pastoral office.\n"
        "\n"
        "Both sides are well attested. The confessors' own letters, XX and XXI, and the argument "
        "of De Lapsis show both sides in their own words. The letters carry the higher citation "
        "grade (A) and De Lapsis the lower (B). Neither side lacks evidence. The tension itself "
        "is the finding.\n"
        "\n"
        "The forces around it hold the tension in place. The Decian persecution put confessors in "
        "one congregation on a mass scale. Their claim was not new: Tertullian, in On Modesty, "
        "already tells of sinners who ask confessors for peace. The Valerianic persecution kept "
        "the tension as it was, and it ended the phase in which the tension appears. The "
        "confessors' claim is itself a force. All three forces belong to the first phase. A "
        "search of the texts tested here found no confessor-authority material from Augustine's "
        "phase. The sermons now in scope have not been searched for it. On the texts tested, the "
        "tension belongs to the first phase alone.",
        [
            "Cyprian's complaint that \"thousands of certificates were daily given, contrary to "
            "the law of the Gospel\"",
            "Epistles XX-XXI, the confessors' own informal, first-person written requests "
            "granting peace to the lapsed",
            "De Lapsis, Cyprian's argument for the bishop's control over readmission",
        ],
        conf("A", "verified-via-authority", "load-bearing", "Documented",
             "Doc_04 §3 Candidate 8: no divergence -- the tension itself, not a confidence gap, is the "
             "finding. Documented for both poles' existence; of the two loci, the Epistles (Registry "
             "row 1) sit at Confidence A and De Lapsis (row 2) at B, carried here as the record's own "
             "top-line citation_specificity of A on the strength of the primary confessor-voice locus."),
        src("lpc.source.cyprian-epistles",
            "lpc.source.cyprian-de-lapsis"),
        "Taken from Doc_04 §3 (Candidate 8). relations[] carries the gravity<->gravity edges (G1, "
        "G2) and the gravity<->force edges (1A-1, 2A-1, 2B-2) named above.",
    )


# ===========================================================================
# FORCES (17) -- Doc_08 §3, one per force identified across the six-cell
# matrix. matrix_cell copied from each force's own cell heading; kind
# mechanically follows the cell (1A/1B -> initiating, 2A/2B -> ongoing,
# 3A/3B -> ending).
# ===========================================================================

def build_forces() -> None:
    emit_force(
        F1A1, "The Decian Persecution and the *libelli* System (250)",
        "initiating", "1A",
        "The Decian persecution was the first empire-wide persecution to be enforced in a "
        "planned way. It worked through certificates recording that the holder had sacrificed. "
        "It did not mainly demand that Christians give up their faith. It demanded a recorded "
        "act of compliance. A person could get one by performing the sacrifice, or by paying "
        "to have it recorded. This is documented in Cyprian's crisis correspondence, which "
        "carries the higher citation grade (A), and in his De Lapsis, which carries the lower "
        "grade (B).\n"
        "\n"
        "It was felt less as an attack from outside than as a table emptied one certificate at "
        "a time. The demand reached each person alone. It sorted the congregation into those "
        "who had stood and those who had not. Both groups still belonged, still in the room. "
        'In Cyprian\'s words, "[I]t is the shepherd that is chiefly wounded in the wound of his '
        'flock."\n'
        "\n"
        "This force made common the group that the whole penitential system exists to deal "
        "with. In one year, many lapsed and many confessors stood in one congregation. The "
        "certificate was a new way to fall. The pattern was not new, though. Tertullian, in On "
        "Modesty, already tells of sinners who ask imprisoned martyrs for peace. So the force "
        "produced two things at once. One was the ongoing contest over members who had failed, "
        "and the discipline for restoring them. The other was the confessors' rival claim to "
        "grant peace, which pushes against it.\n"
        "\n"
        "It also sharpened the bishop's answerability, which is sharpest when his people fail. "
        "And it gave this world its densest crisis vocabulary: the lapsed, reconciliation, "
        "confessor, and the certificates of both kinds.\n"
        "\n"
        "The later Valerianic persecution repeated this test. By then the community had built "
        "a discipline to meet it.",
        [
            "the libelli: certificates recording that the holder had sacrificed, obtainable by "
            "performing the sacrifice or by paying to have it recorded",
            '"[I]t is the shepherd that is chiefly wounded in the wound of his flock" (Cyprian)',
        ],
        conf("A", "verified-via-authority", "load-bearing", "Documented",
             "Doc_08 §3 Force 1A-1: Documented, attested across Doc_01's own founding-boundary "
             "reasoning and Doc_02 §1, corroborated by the crisis correspondence (Registry row 1, "
             "Confidence A) and De Lapsis (row 2, Confidence B); no divergence flagged for this "
             "force's own bare occurrence."),
        src("lpc.source.cyprian-epistles",
            "lpc.source.cyprian-de-lapsis"),
        "Taken from Doc_08 §3 Force 1A-1 (Cell 1A, Initiating/External). relations[] carries the "
        "gravity<->force edges (G1, G2, G8) and the force<->force edges (2B-1, 2B-2, 2A-1) named "
        "above.",
    )

    emit_force(
        F1A2, "The Standing Legal Condition of an Unlicensed Religion in Romanized Provincial North "
              "Africa",
        "initiating", "1A",
        "Throughout this world's first phase, Christianity had no legal standing. It lived in a "
        "Romanized provincial society with real underlying Punic populations and, inland, Berber "
        "ones. Persecution came and went, but the exposure never stopped. This picture is widely "
        "accepted.\n"
        "\n"
        "It meant that a bishop could be taken, and was. The office carried no protection, and "
        "the community had no recourse. What it had was each other, and whatever a man would do "
        "for the people in his charge while he still could.\n"
        "\n"
        "This condition is why the pastoral office grew as personal answerability rather than as "
        "jurisdiction. An office with nothing outside to enforce it is held together by the bond "
        "between one man and one congregation.\n"
        "\n"
        "In the second phase, the condition was removed. We considered whether that shift was "
        "itself one of this world's own central concerns, but nothing in this world organizes "
        "around the shift itself. It is named here as a force precisely because it is not one of "
        "those central concerns. It shaped what the office could be without becoming something "
        "the world organizes around.\n"
        "\n"
        "An office with no legal protection is one a sensible man declines. That is why "
        "congregations had to override a chosen man's reluctance by acclamation. The same fact "
        "also appears at both ends of this world with opposite sign. The later shift from illegal "
        "to established religion removes exactly this condition.",
        [
            "the continuous legal exposure of an unlicensed religion in a Romanized provincial "
            "society with real underlying Punic and Berber populations; persecution came only in "
            "episodes",
        ],
        conf("B", "verified-via-authority", "load-bearing", "Widely Accepted",
             "Doc_08 §3 Force 1A-2: Widely Accepted -- Doc_01 §2 (Cultural Environment; Historical "
             "Pressures) and Doc_02 §5, a background legal condition rather than a claim any single "
             "vendored Registry row directly narrates; no lpc.source.* record is cited for it in "
             "Doc_08's own text, and none is invented here to supply one."),
        [],
        "Taken from Doc_08 §3 Force 1A-2 (Cell 1A, Initiating/External). relations[] carries the "
        "gravity<->force edge (G1) and the force<->force edges (1B-2, 2B-3) named above. "
        "sources[] is deliberately empty. Doc_08 cites two of this world's own governing "
        "documents, not a vendored source, for a background legal condition that this world's "
        "corpus does not narrate directly.",
    )

    emit_force(
        F1B1, "An Already-Organized Carthaginian Church Capable of Sustained Collective Response",
        "initiating", "1B",
        "Cyprian took over a church big enough to hold real factions inside it. It could also call "
        "councils of dozens of bishops. This is documented, in the councils themselves and in what "
        "Cyprian's letters say about Felicissimus.\n"
        "\n"
        "From the inside, this was not a gathering that had to be built. It was already standing, "
        "with its own men of weight, its own quarrels, and its own ability to meet and decide "
        "together.\n"
        "\n"
        "Because it was organized, bishops who disagreed could still keep communion. That needs "
        "colleagues who can meet, and who already disagree. It also made a ruled process of "
        "penance possible. A loose community could not have run one. And it gave both formulas of "
        "conciliar authority the councils they speak about.\n"
        "\n"
        "A church organized enough to hold factions could also carry an election against a faction "
        "that opposed it. And the councils that met and left written acts are what Augustine later "
        "read and argued with.",
        [
            "councils of dozens of bishops, including the council of 256",
            "the Felicissimus schism, a real internal faction the church was already organized "
            "enough to hold",
        ],
        conf("A", "verified-via-authority", "load-bearing", "Documented",
             "Doc_08 §3 Force 1B-1: Documented -- Doc_01 §6; the councils themselves (Registry row 4) "
             "and the Felicissimus material in the Epistles (row 1); no divergence flagged for this "
             "force's own bare occurrence."),
        src("lpc.source.cyprian-seventh-council-of-carthage",
            "lpc.source.cyprian-epistles"),
        "Taken from Doc_08 §3 Force 1B-1 (Cell 1B, Initiating/Internal). relations[] carries the "
        "gravity<->force edges (G2, G3, G5) and the force<->force edges (1B-2, 2B-4) named above.",
    )

    emit_force(
        F1B2, "Congregational Acclamation Overriding a Reluctant Convert's Preference",
        "initiating", "1B",
        "Cyprian was a trained rhetorician who converted in middle life. Within roughly two to "
        "three years of his conversion, the people of Carthage elected him bishop by acclamation. "
        "Five presbyters are recorded as opposing him. He called it \"your suffrage and God's "
        "judgment,\" set against a faction's \"ancient venom.\" A deacon who knew him described "
        "it from outside: \"by the judgment of God and the favour of the people, he was chosen to "
        "the office of the priesthood and the degree of the episcopate while still a neophyte.\"\n"
        "\n"
        "The pattern recurs in the second phase, at both of Augustine's offices. In 391 he was "
        "seized into the presbyterate at Hippo against his wishes. For the episcopate, "
        "Possidius's Vita, chapter VIII, records the scene. Valerius announced his intention to "
        "the bishops present, the whole Hippo clergy, and all the people. Those who heard "
        "rejoiced and clamoured eagerly for it. Augustine refused the episcopate while his own "
        "bishop lived. Then, persuaded by precedent from overseas and from Africa, he yielded "
        "under compulsion and constraint.\n"
        "\n"
        "The evidence is documented. It comes from Cyprian's Epistle XXXIX, from Pontius, and "
        "from Possidius's Vita, chapters IV and VIII.\n"
        "\n"
        "This force gives the pastoral office its two-way shape. A bishop answers to the people "
        "who placed him, as well as for them. One caution is kept rather than smoothed over. The "
        "pattern is attested through different people and in different words, not through one "
        "recurring term. But it appears at the same office in both phases.\n"
        "\n"
        "Two conditions shaped it. An office with no legal protection is one a sensible man "
        "declines, so the acclamation had to override reluctance. And a church organized enough "
        "to hold factions was organized enough to elect a bishop over a faction's opposition.",
        [
            "\"your suffrage and God's judgment\" (Cyprian's own words on his election)",
            "\"by the judgment of God and the favour of the people, he was chosen to the office "
            "of the priesthood and the degree of the episcopate while still a neophyte\" (the "
            "outside account of a deacon who knew him)",
            "Possidius, Vita Augustini ch. VIII: Valerius's announcement, and Augustine's refusal "
            "and his yielding \"under compulsion and constraint\"",
        ],
        conf("A", "verified-via-authority", "load-bearing", "Documented",
             "Doc_08 §3 Force 1B-2: Documented -- Epistle XXXIX (Registry row 1); Pontius (row 7, "
             "Confidence A); Possidius's Vita chs. IV and VIII (row 192); Doc_01 §2. The pattern is "
             "attested through different figures and different words at the same office in both "
             "phases, a caution carried directly in this force's own Layer 3 rather than smoothed "
             "into one uniform recurring term."),
        src("lpc.source.cyprian-epistles",
            "lpc.source.pontius-life-and-passion-of-cyprian",
            ("lpc.source.possidius-vita-augustini-weiskotten1919",
             "Vita Augustini ch. VIII, \"under compulsion and constraint he yielded and accepted "
             "the ordination\" -- verified directly against "
             "cic/texts/possidius_vita-augustini_weiskotten1919.txt, lines 2142-2143 (the phrase "
             "is hyphenated across a line wrap in the source file -- \"under com-\" then "
             "\"pulsion and constraint\")"),
        ),
        "Taken from Doc_08 §3 Force 1B-2 (Cell 1B, Initiating/Internal). relations[] carries the "
        "gravity<->force edge (G1) and the force<->force edges (1A-2, 1B-1) named above.",
    )

    emit_force(
        F1B3, "The Inherited Latin Theological Vocabulary",
        "initiating", "1B",
        "Before this world begins, North African Latin Christianity already had a vigorous local "
        "literary culture, along with a Latin theological vocabulary that Tertullian is credited "
        "with forging. This is widely accepted.\n"
        "\n"
        "The words were already to hand. What had to be argued could be argued in Latin, the "
        "church's own language of preaching. Latin was not every hearer's tongue, though. For one "
        "country town, Augustine looked for a bishop who knew Punic.\n"
        "\n"
        "This made preaching and catechesis possible as the main way of forming people, since that "
        "depends on a theological language able to carry the content.\n"
        "\n"
        "The force is treated briefly, in proportion to its weight. It is real and enabling. But "
        "it is not contested and not tied to one phase. It does not shape what the world's central "
        "concerns say, only the medium they are said in. No link to any other force is named for "
        "it.",
        [
            "the Latin theological vocabulary Tertullian is credited with forging, already "
            "available to this world's bishops without needing to be invented",
        ],
        conf("B", "verified-via-authority", "load-bearing", "Widely Accepted",
             "Doc_08 §3 Force 1B-3: Widely Accepted -- Doc_01 §6, §7; Doc_02 §2's own Tertullian "
             "disclosure. Tertullian's own corpus is Registry row 29, Boundary Status EXCLUDED (this "
             "world's own construction begins after Tertullian; his vocabulary is inherited, not this "
             "world's own voice) -- no lpc.source.tertullian-* record exists to cite, and none is "
             "invented here to supply one."),
        src(("lpc.source.augustine-general-correspondence",
             "Letter CCIX §3, a Punic-speaking bishop sought for Fussala ('acquainted with the "
             "Punic language') -- verified directly against "
             "cic/texts/npnf101_augustine-confessions-letters.xml, lines 54466-54469")),
        "Taken from Doc_08 §3 Force 1B-3 (Cell 1B, Initiating/Internal). relations[] carries the "
        "gravity<->force edge (G4) named above. sources[] cites only Letter CCIX §3, for the "
        "Punic sentence. The Tertullian corpus is excluded from this world, so no Tertullian "
        "source record exists to cite, and none is invented.",
    )

    emit_force(
        F2A1, "Recurring Persecution After Decius -- the Valerianic Persecution (257-258)",
        "ongoing", "2A",
        "Imperial persecution returned under Valerian. Cyprian was exiled and then martyred in "
        "258. This is documented, including in the Acta Proconsularia.\n"
        "\n"
        "The thing had not finished with them. The man who had spent seven years deciding what to "
        "do with those who failed the first test was taken by the second. He did not fail it.\n"
        "\n"
        "This persecution confirms two of the world's concerns rather than reshaping them: the "
        "pastoral office, and the tension between confessors and bishops. It closes the first "
        "phase by showing what the confessors' credential had been about. It shows this in the "
        "person of the bishop who had regulated the lapsed. It also ends the first phase's "
        "written record. That is why penitential discipline and the confessor tension are "
        "attested only within that phase.\n"
        "\n"
        "The Valerianic persecution repeats the Decian test on a community that has now built a "
        "discipline for it.",
        [
            "Cyprian's own exile and martyrdom under Valerian in 258, recorded in the Acta "
            "Proconsularia",
        ],
        conf("A", "verified-via-authority", "load-bearing", "Documented",
             "Doc_08 §3 Force 2A-1: Documented -- Doc_01 §2; the Acta Proconsularia within Registry "
             "row 194; no divergence flagged for this force's own bare occurrence."),
        src("lpc.source.cyprian-opera-spuria-vita-pontius-acta-proconsularia-csel3-pars3"),
        "Taken from Doc_08 §3 Force 2A-1 (Cell 2A, Ongoing/External). relations[] carries the "
        "gravity<->force edges (G1, G4, G8) and the force<->force edge (1A-1) named above.",
    )

    emit_force(
        F2A2, "Epidemic Disease -- the Plague of c. 249-262",
        "ongoing", "2A",
        "A severe, well-attested pandemic ran through Carthage while Cyprian was bishop. He "
        "addressed it directly in his treatise De Mortalitate. The plague is documented.\n"
        "\n"
        "It was a pressure no discipline could sort. Persecution at least asked a question a "
        "person could answer rightly or wrongly, but the plague asked nothing -- it took the "
        "faithful and the lapsed alike.\n"
        "\n"
        "This is the clearest case in this world of a pressure that produced teaching rather than "
        "structure. It created no lasting concern the world organizes around, and no practice. It "
        "produced a treatise. That makes it the sharpest example of how this world typically "
        "responded to crisis: by turning it into teaching, through preaching and catechesis.\n"
        "\n"
        "This force is deliberately left unconnected to any other force in this world. That is "
        "not a weakness in the entry. It is the clearest case of a pressure that shaped what was "
        "taught without shaping how the church was built. Recording that absence honestly is "
        "better than inventing a link.",
        [
            "De Mortalitate, Cyprian's own treatise directly addressing the plague of c. 249-262",
        ],
        conf("A", "verified-via-authority", "load-bearing", "Documented",
             "Doc_08 §3 Force 2A-2: Documented -- Doc_01 §2; Registry row 5; no divergence flagged for "
             "this force's own bare occurrence."),
        src("lpc.source.cyprian-minor-pastoral-treatises"),
        "Taken from Doc_08 §3 Force 2A-2 (Cell 2A, Ongoing/External). relations[] carries only "
        "the gravity<->force edges (G1, G4) named above -- deliberately NO force<->force edge, "
        "per Doc_08 §4's own explicit 'deliberately isolated' finding for this force, named "
        "rather than silently applied, matching don's own F3A-2/2A-2-equivalent precedent for a "
        "disclosed non-connection.",
    )

    emit_force(
        F2A3, "The Donatist Schism",
        "ongoing", "2A",
        "The Donatist church was dominant across large parts of North African Christian life for "
        "most of the century between the two phases. It was still a live problem for the pastor "
        "all through Augustine's time as bishop. This is documented.\n"
        "\n"
        "The Donatists were not strangers to this world, and not heretics of a foreign kind. They "
        "were a church in the same towns, with its own bishop in the same see, claiming to be the "
        "only true church. For their central practice, they appealed to a ruling by Cyprian, this "
        "world's own first bishop.\n"
        "\n"
        "In the second phase, no force had more far-reaching effects. It made one question urgent "
        "for the whole church, not just for single converts: is a sacrament given outside the "
        "church real? It tested, at the hardest edge, whether disagreement had to mean a split. "
        "Augustine's answer to Cyprian shows it did not.\n"
        "\n"
        "It is also the whole reason Augustine argued about the authority of councils at all. The "
        "Donatists' appeal to Cyprian's conciliar acts obliged him to argue against a predecessor "
        "he could not disown. That prompt came from outside, but the reading and the argument were "
        "Augustine's own.\n"
        "\n"
        "Finally, it was the outside pressure behind Augustine's teaching on coercion. That "
        "teaching has to be held in its three phases, not compressed into one. A rival communion "
        "is what made the state's newly available power worth using.",
        [
            "the Donatists' appeal to Cyprian's conciliar acts and his authority on rebaptism, in "
            "support of their own central practice",
            "a rival bishop claiming the same see, in the same towns, throughout Augustine's "
            "episcopate",
        ],
        conf("A", "verified-via-authority", "load-bearing", "Documented",
             "Doc_08 §3 Force 2A-3: Documented -- Doc_01 §2; Doc_02 §1; Registry rows 12, 13; no "
             "divergence flagged for this force's own bare occurrence."),
        src("lpc.source.augustine-correction-of-the-donatists",
            "lpc.source.augustine-on-baptism-against-the-donatists"),
        "Taken from Doc_08 §3 Force 2A-3 (Cell 2A, Ongoing/External). relations[] carries the "
        "gravity<->force edges (G3, G4, G5, G6) and the force<->force edges (2B-4, 2B-3) named "
        "above.",
    )

    emit_force(
        F2A4, "Manichaeism and Pelagian Anthropology as Live Rival Systems",
        "ongoing", "2A",
        "Two rival systems pressed on this world. The first was Manichaeism, an organized system "
        "that Augustine belonged to for roughly nine years before his conversion. It remained a "
        "recurring target for him afterward. The second was Pelagian teaching about human nature. "
        "The controversy over it ran through the 410s and 420s, and it fills a corpus of thirteen "
        "works. Both are documented.\n"
        "\n"
        "These were two ways of accounting for a person that this world had to reckon with. A "
        "bishop had to answer them from the pulpit, because the people in front of him had heard "
        "them.\n"
        "\n"
        "This force directly and entirely produces the world's teaching on grace and human "
        "incapacity. The anti-Pelagian writings are this world's single densest body of text, "
        "with 1,798 raw occurrences of \"grace\" within their bounds. They are also the largest "
        "single part of the inheritance that outlived the world.\n"
        "\n"
        "The Manichaean half is named here but not developed. We never tested it on its own as "
        "one of this world's own central concerns, because our own vocabulary study had not "
        "turned up a term specific enough to test. That is a stated limit of the analysis, not a "
        "judgement that the Manichaean pressure was slight.",
        [
            "Manichaeism, an organized rival system Augustine belonged to for roughly nine years "
            "before his conversion",
            "the thirteen-work anti-Pelagian corpus, with 1,798 raw occurrences of \"grace\" "
            "within its bounds",
        ],
        conf("A", "verified-via-authority", "load-bearing", "Documented",
             "Doc_08 §3 Force 2A-4: Documented -- Doc_01 §2, §6; Registry rows 22, 23. The Manichaean "
             "half is named and not developed as its own candidate gravity, per Doc_04 §7 item 4 -- a "
             "stated limit rather than a judgement that the Manichaean pressure was slight, and this "
             "record does not treat that limit as a confidence divergence in the Pelagian half's own "
             "Documented rating."),
        src("lpc.source.augustine-anti-manichaean-corpus",
            "lpc.source.augustine-anti-pelagian-corpus"),
        "Taken from Doc_08 §3 Force 2A-4 (Cell 2A, Ongoing/External). relations[] carries the "
        "gravity<->force edges (G4, G7) and the force<->force edge (3B-1) named above.",
    )

    emit_force(
        F2B1, "The Recurring Contest Over How to Treat the Failed Member",
        "ongoing", "2B",
        "Under Cyprian, the contest was over the lapsed. Under Augustine, it was over ordinary "
        "sin after baptism, and over believers tempted by schism. The contest is documented in "
        "both periods.\n"
        "\n"
        "This was the question that would not go away, felt from inside: what do you owe someone "
        "who is yours and has failed? A church that takes everyone back the same afternoon has no "
        "door. One that takes no one back has no Master.\n"
        "\n"
        "In the first phase, this contest directly produced the church's penitential discipline. "
        "In that same phase, it also links to the question of valid sacraments and ordination "
        "outside the church. Both are questions of boundary and return, and Cyprian reasons about "
        "them in the same way.\n"
        "\n"
        "That the contest lasts into the second phase is a qualified claim, not an assumed one. "
        "The concern does not continue under its own name. What survives is a family resemblance "
        "to two other concerns that were tested on their own: sacramental validity, and grace and "
        "human incapacity. The debate over grace reshapes the old concern but does not continue "
        "it. So the later link is a resemblance, not a direct connection. This force connects to "
        "penitential discipline and sacramental validity, both in the first phase. It does not "
        "connect to grace.\n"
        "\n"
        "The Decian edict made failed members common, and this contest is about them. The "
        "confessors' own parallel system sharpened it. That rival system meant a formal process "
        "had to settle the contest, not the bishop's word alone.",
        [
            "the lapsed under Cyprian; ordinary post-baptismal sin and schism-tempted believers "
            "under Augustine",
        ],
        conf("A", "verified-via-authority", "load-bearing", "Documented",
             "Doc_08 §3 Force 2B-1: Documented -- Doc_01 §6's own Ongoing/Internal cell; Registry rows "
             "1, 2, 12, 13. The second-phase persistence toward G7 is qualified rather than assumed, "
             "per Doc_04's own Persistence test for Candidate 2 -- named directly here as a scope "
             "finding, not a confidence divergence, and worked out at length by Doc_08 §5's own G6 "
             "entry, cross-checked against Doc_04 §6's own asymmetric Interaction Matrix cells."),
        src("lpc.source.cyprian-epistles",
            "lpc.source.cyprian-de-lapsis",
            "lpc.source.augustine-correction-of-the-donatists",
            "lpc.source.augustine-on-baptism-against-the-donatists"),
        "Taken from Doc_08 §3 Force 2B-1 (Cell 2B, Ongoing/Internal). relations[] carries the "
        "gravity<->force edges (G2, G6) and the force<->force edges (1A-1, 2B-2) named above -- "
        "deliberately NOT G7, per this force's own asymmetric family-resemblance finding above.",
    )

    emit_force(
        F2B2, "The Confessors' Claim to Grant Peace",
        "ongoing", "2B",
        "People who survived interrogation without denying their faith issued written requests "
        "that named lapsed persons be received back. In Cyprian's own words, \"thousands of "
        "certificates were daily given, contrary to the law of the Gospel.\" This is documented.\n"
        "\n"
        "Both sides spoke in earnest, and that was the difficulty. One side said: I stood before "
        "the magistrate and did not deny Him, and I say this man may come back. The other "
        "answered: the peace of the church is not any man's to give out of his own suffering, "
        "however real.\n"
        "\n"
        "This force is the one tension of its kind in this world's record: the confessors' "
        "authority set against the peace that the bishop regulates. It also explains why the "
        "penitential discipline takes such an insistent, often-restated form. Penance was not "
        "made in a vacuum. It was built against a working parallel system that already circulated "
        "documents on a large scale. That parallel system is why the contest over the lapsed had "
        "to be settled by a formal process, not by a bishop's word alone.\n"
        "\n"
        "The Decian edict made confessors a large class with a claim. The force belongs to "
        "Cyprian's phase alone. That limit rests on a check, not on an assumption from silence. "
        "The stem \"confessor\" appears twenty times across all eight Augustine volumes in the "
        "project's library, and never in this sense.",
        [
            "\"thousands of certificates were daily given, contrary to the law of the Gospel\" "
            "(Cyprian's own words)",
        ],
        conf("A", "verified-via-authority", "load-bearing", "Documented",
             "Doc_08 §3 Force 2B-2: Documented -- Registry row 1, Confidence A; no divergence flagged "
             "for this force's own bare occurrence. Phase-bound on a positive check (twenty stem "
             "occurrences of 'confessor' across all eight vendored Augustine volumes, none in this "
             "sense), not assumed from silence."),
        src("lpc.source.cyprian-epistles"),
        "Taken from Doc_08 §3 Force 2B-2 (Cell 2B, Ongoing/Internal). relations[] carries the "
        "gravity<->force edges (G2, G8) and the force<->force edges (1A-1, 2B-1) named above.",
    )

    emit_force(
        F2B3, "The Illegal-to-Established Shift in the Office's Political Capacity",
        "ongoing", "2B",
        "Between the two phases, the bishop's office changed its legal position. At first it had "
        "no legal standing at all. Later it could ask the state to act against a rival communion.\n"
        "\n"
        "The outside change itself is documented. One element is contested: not whether the shift "
        "happened, but whether its consequence belongs among the world's inner forces or its "
        "outside pressures. Placing it as an inner force follows a judgement we made earlier, not "
        "a settled finding.\n"
        "\n"
        "The shift is the old condition of illegality turned upside down, the same fact appearing "
        "at both ends of the story with the opposite sign. What a bishop could do had changed, "
        "though what a bishop was had not -- Cyprian never asked the magistrate for anything, and "
        "a century and a third later, the emperors could be asked, and eventually were.\n"
        "\n"
        "We considered whether the shift itself was one of this world's own central concerns. It "
        "is not, because nothing in this world actually organizes itself around the shift. It "
        "changes the tools a bishop has, not what a bishop is. A separate look from the ethical "
        "and legal side reached the same conclusion. So it is kept as a real force, with an impact "
        "deliberately limited in proportion to its weight. A rival communion, the Donatist church, "
        "is what made the new state power worth using.",
        [
            "Cyprian never asking the magistrate for anything, set against Augustine's later "
            "recourse to state action against the Donatist schism a century and a half afterward",
        ],
        conf("A", "verified-via-authority", "load-bearing", "Documented",
             "Doc_08 §3, §7 Force 2B-3: Documented for the external change itself. Carries a "
             "CONTESTED secondary element, named at Doc_08 §7 rather than only in its own summary: not "
             "the fact of the shift, but its placement as an internal rather than external force, "
             "which follows Doc_01 §6's own judgement and is stated here as that document's rather "
             "than this one's. Doc_04 §2 declined to advance this as its own candidate gravity, "
             "finding nothing in this ecology organizes around the shift itself -- a classification "
             "finding, not a confidence divergence, carried here for completeness."),
        [],
        "Taken from Doc_08 §3 Force 2B-3 (Cell 2B, Ongoing/Internal). No gravity<->force edge -- "
        "Doc_08 §5's own gravity-by-gravity list and lpc_Force_Index.md §1's own 'Connected "
        "Gravities: --' both confirm this force connects to no classified gravity, consistent "
        "with Doc_04 §2's own decision not to advance the underlying shift as a candidate. "
        "relations[] carries the force<->force edges (1A-2, 2A-3) named above, plus one "
        "contested_claim edge (lpc.contested.compel-coercion-development). sources[] is "
        "deliberately empty. This force rests on a judgment about where a legal condition sits, "
        "not on a vendored text that makes a claim.",
    )

    emit_force(
        F2B4, "Augustine's Engagement with Cyprian's Conciliar Acts",
        "ongoing", "2B",
        "Augustine read the ruling on rebaptism made by Cyprian's council of 256, and argued at "
        "length that it was wrong. He did this in On Baptism, Against the Donatists. The "
        "engagement is documented.\n"
        "\n"
        "From inside this world, Cyprian was a predecessor who belonged to them. They did not "
        "disown him, and yet he had decided this question wrongly. Augustine gave the principle "
        "that let him say so: \"[E]ven of the plenary Councils, the earlier are often corrected by "
        "those which follow them.\"\n"
        "\n"
        "No other force carries as much of the world's formation logic across the 133 years "
        "between the two phases, which this build has assessed as a silence in the world's "
        "pastoral voice (Contested). It is also the only one in which this world itself reads and "
        "answers Cyprian's council acts. The crossing happens through texts, not through a line of "
        "living successors. It happens more than once. Possidius quotes Cyprian's De Mortalitate. "
        "Augustine also cites Cyprian on grace against the Pelagians.\n"
        "\n"
        "This engagement produces the second of the world's two accounts of what councils can "
        "decide: Augustine's view that later councils correct earlier ones. It tests, across the "
        "long gap, whether communion can hold despite disagreement. It also reopens the question "
        "of whether sacraments are valid outside the church's boundary.\n"
        "\n"
        "The Donatists prompted it by citing Cyprian for themselves, so the prompt came from "
        "outside. But the reading, the argument, and the conclusion were this world's own acts. "
        "The outside prompt decided only the timing. For that reason it counts as an internal "
        "force.\n"
        "\n"
        "It also depended on an earlier condition. Cyprian's councils met and left written acts, "
        "and those acts are what Augustine later read and argued with.",
        [
            "\"[E]ven of the plenary Councils, the earlier are often corrected by those which "
            "follow them\" (Augustine, On Baptism, Against the Donatists)",
            "Augustine reading the rebaptism ruling of Cyprian's council of 256 and arguing at "
            "length that it was wrong",
        ],
        conf("A", "verified-via-authority", "load-bearing", "Documented",
             "Doc_08 §3 Force 2B-4: Documented -- Registry rows 4, 13; no divergence flagged for this "
             "force's own bare occurrence. The internal-versus-external placement is examined and "
             "confirmed rather than inherited silently: the prompt (the Donatists' own citation of "
             "Cyprian) is external, but the reading, argument, and conclusion are this world's own "
             "internal acts, per Doc_08's own stated reason."),
        src("lpc.source.cyprian-seventh-council-of-carthage",
            "lpc.source.augustine-on-baptism-against-the-donatists"),
        "Taken from Doc_08 §3 Force 2B-4 (Cell 2B, Ongoing/Internal). relations[] carries the "
        "gravity<->force edges (G3, G5, G6) and the force<->force edges (1B-1, 2A-3, 3B-2) named "
        "above.",
    )

    emit_force(
        F2B5, "Transmission: Survival on the Institutionally Dominant Side, Through a "
              "19th-Century Translation Programme",
        "ongoing", "2B",
        "The writings of both Cyprian and Augustine survive in unusually full form. Both were kept "
        "by the church that later became the canonical one. That church kept Cyprian even where it "
        "judged him wrong, on rebaptism.\n"
        "\n"
        "This project's actual access is narrower. It works mainly from the 19th-century English "
        "translation series, the Ante-Nicene Fathers and the Nicene and Post-Nicene Fathers. It "
        "also holds critical Latin editions, but uses them far less. Both the survival pattern and "
        "the make-up of this working corpus are documented. The named agents of transmission are "
        "the Catholic institutional manuscript tradition, the editors and translators of those two "
        "series, and this project's own choices about which texts to hold.\n"
        "\n"
        "This world was acutely aware of transmission and acted on it. Cyprian gathered his own "
        "letters into a dossier and sent it on: \"these thirteen letters sent forth at various "
        "times declare to you, which I have transmitted to you.\" He knew his letters were read "
        "beyond the person they were written to. He also met textual corruption directly. One "
        "letter's \"writing and the matter, and even the paper itself, gave me the idea that "
        "something had been taken away, or had been changed from the original.\" He sent it back "
        "to be checked against the original.\n"
        "\n"
        "Some 170 years on, the same awareness took a new form. Near the end of his life, "
        "Augustine set out to review his own works \"with a certain judicial severity.\" He marked "
        "what displeased him \"as with a censor's pen.\" It was a deliberate act of shaping what "
        "would outlast him.\n"
        "\n"
        "What this world could not experience is what came later: the Catholic tradition's own "
        "selection of texts, and a 19th-century translation programme.\n"
        "\n"
        "This has three effects. First, the record is full and one-sided at the same time. Its "
        "imbalance does not come from hostile filtering. It comes from the near-total absence of "
        "any voice other than a bishop's. Second, the 19th-century editors' material is woven into "
        "the text. It has repeatedly been mistaken for the world's own voice, and this project has "
        "documented eight local cases. Third, translation shapes what can be found, not only how "
        "accurately it reads. A search of original-language headwords cannot find a term that the "
        "corpus only ever names in translation.\n"
        "\n"
        "The same pattern continues across the silence between the two phases. There it shapes the "
        "span of the record rather than its content.",
        [
            "Cyprian's own dossier of thirteen letters, \"sent forth at various times... which I "
            "have transmitted to you\"",
            "a suspect letter Cyprian sends back to be checked against the original, because its "
            "\"writing and the matter, and even the paper itself, gave me the idea that something "
            "had been taken away, or had been changed from the original\"",
            "Augustine's Retractationes, reviewing his own works \"with a certain judicial "
            "severity\" and marking what displeases him \"as with a censor's pen\" (our own corpus "
            "holds no complete English translation of it, and none of this passage; this English "
            "is our own rendering)",
        ],
        conf("A", "verified-via-authority", "load-bearing", "Documented",
             "Doc_08 §3 Force 2B-5: Documented for the survival pattern and for the composition of "
             "this build's own corpus. This world was acutely conscious of transmission and acted on "
             "it in its own voice (Cyprian's own dossier and collation practice; Augustine's own "
             "Retractationes); what it could not experience -- the Catholic institutional tradition's "
             "own selection and the 19th-century translation programme -- is named directly rather "
             "than narrated from inside, per Doc_08 §8's own Reported-Experience discipline."),
        src("lpc.source.cyprian-epistles",
            "lpc.source.knoll-augustine-retractationes-csel36"),
        "Taken from Doc_08 §3 Force 2B-5 (Cell 2B, Ongoing/Internal; Transmission dimension). "
        "relations[] carries only the force<->force edge (3B-2) named above -- deliberately no "
        "gravity<->force edge, per Doc_08 §5's own explicit 'cross-cutting, not gravity-specific' "
        "disposition for this force (matching "
        "don.force.transmission-hostile-manuscript-tradition's own identical disposition), named "
        "rather than silently applied.",
    )

    emit_force(
        F3A1, "The Vandal Invasion and the Siege of Hippo (430)",
        "ending", "3A",
        "The Vandals crossed from Spain into Africa in the late 420s; the chronicles disagree on "
        "the year, and Prosper's enters the crossing under 427. In 430 they besieged Hippo. Augustine fell ill in the "
        "third month of the siege, and he died on 28 August 430 -- a date Prosper, a near-contemporary "
        "chronicler writing in Gaul, independently records. This is documented. Prosper also records the "
        "Vandal capture of Carthage under 439, a different city, nine years later, and no part of "
        "where this world ends.\n"
        "\n"
        "This was an army on the road while the bishop lay dying inside the walls, with the "
        "people he answered for still in the city.\n"
        "\n"
        "This force closes the world the same way it opened, with violent pressure from outside "
        "on ordinary congregational life -- the second of the two reasons for ending this world "
        "in 430. It also ends the recorded life of the pastoral office here: the bond between "
        "this bishop and this flock ends when he does.\n"
        "\n"
        "The invasion coincides with the survival of the world's writings, but it does not cause "
        "it. The invasion closes the world, and the writings outlive it. The inheritance was "
        "secured by copying, not by the siege.",
        [
            "the siege of Hippo, begun in 430, in whose third month Augustine fell ill",
            "Augustine's own death on 28 August 430, independently recorded by Prosper, a "
            "near-contemporary chronicler writing in Gaul",
        ],
        conf("A", "verified-via-authority", "load-bearing", "Documented",
             "Doc_08 §3 Force 3A-1: Documented -- Registry row 203, a near-contemporary Gallic "
             "chronicle independently recording Augustine's death under 430; no divergence flagged "
             "for this force's own bare occurrence."),
        src(("lpc.source.prosper-epitoma-chronicon-mommsen1892",
             "Epitoma Chronicon entry 1295, 'Gens Wandalorum ab Hispania ad Africam transit', "
             "entered under the consuls of 427 -- cic/texts/prosper_chronica-minora-1-lat_mommsen1892.txt, "
             "lines 54069 and 54126"),
            ("lpc.source.possidius-vita-augustini-weiskotten1919",
             "Vita Augustini ch. XXIX, 'in the third month of the siege he succumbed to fever' -- "
             "cic/texts/possidius_vita-augustini_weiskotten1919.txt, lines 4146-4148")),
        "Taken from Doc_08 §3 Force 3A-1 (Cell 3A, Ending/External). relations[] carries the "
        "gravity<->force edge (G1) and the force<->force edge (3B-1) named above.",
    )

    emit_force(
        F3B1, "The Corpus Outliving the World",
        "ending", "3B",
        "Augustine's theological writing grew out of this world's own pastoral pressures. Long "
        "after the world closed, it became the foundational inheritance of the later Western "
        "theological tradition. This is widely accepted.\n"
        "\n"
        "What follows is the world's own self-understanding. It is reported as such and not "
        "assessed for historical accuracy. This outcome was not felt as an ending, but it was not "
        "felt as nothing either. A bishop writing against a live error writes for the people in "
        "front of him and the case at hand. He does not write for a tradition he expects to "
        "found.\n"
        "\n"
        "Yet this world did take its own writings seriously as something that would stand after "
        "it. Cyprian gathered thirteen of his own letters and sent them to Rome, to give account "
        "of what he had done. At the end, Augustine went back through his books one by one and "
        "corrected them, in the Retractationes. He did not reach his letters and sermons. Our own "
        "corpus holds no English translation of that work. A man who revises his own books knows "
        "they will be read when he cannot answer for them. What he could not know, and what no one "
        "in this world could know, was which of it would matter, or to whom.\n"
        "\n"
        "The change is real, but it runs outward, not inward. Augustine's teaching on grace and "
        "human incapacity outlives its own setting most of all -- within this world that teaching "
        "stands on its own, but for the traditions that follow, it becomes load-bearing. This is "
        "the one force whose impact lands mostly outside the world's own boundaries, which is why "
        "it counts as an ending force, not an ongoing one.\n"
        "\n"
        "The anti-Pelagian writings are the largest single part of this inheritance. The Vandal "
        "invasion closes the world at the same moment, but it does not cause this outcome -- the "
        "two coincide, and one does not produce the other.",
        [
            "Augustine's theological corpus, which became the foundational inheritance of the "
            "later Western theological tradition",
            "Augustine's Retractationes, reviewing his own books near the end of his life, though "
            "not his letters and sermons (our own corpus holds no English translation of it)",
        ],
        conf("B", "verified-via-authority", "load-bearing", "Widely Accepted",
             "Doc_08 §3 Force 3B-1: Widely Accepted -- Doc_01 §6. Layer 2 carries the Reported-"
             "Experience Status marker (Constitution Article 17; Forces Framework §3): reported as the "
             "world's own self-understanding, not assessed for historical accuracy; confidence "
             "calibration applies to the historical-event layer only, which this record's own "
             "top-line rating reflects."),
        src("lpc.source.knoll-augustine-retractationes-csel36"),
        "Taken from Doc_08 §3 Force 3B-1 (Cell 3B, Ending/Internal). relations[] carries the "
        "gravity<->force edge (G7) and the force<->force edges (2A-4, 3A-1) named above.",
    )

    emit_force(
        F3B2, "Transmission: an Unevenly Attested Span and a 133-Year Silence",
        "ending", "3B",
        "This world's closing decades are much better attested than its opening ones. Between its "
        "two phases lies a silence of roughly 133 years, from Cyprian's martyrdom to Augustine's "
        "ordination. No surviving voice continuous with Cyprian's ordinary pastoral mode, from "
        "within this world's boundary, that this build has assessed dates from within that gap. "
        "Nine tractatus in Morin 1917, one titled in a manuscript as a sermon of Optatus of "
        "Milevis, are not yet assessed. Some texts in our own source catalogue do date from it or "
        "record its events, such as Optatus's polemic, the council canons and imperial law, and "
        "none of them is that voice. The silence claim is contested for that reason. The uneven "
        "attestation is a documented fact about the record itself, and anyone can check it "
        "against the catalogue.\n"
        "\n"
        "Augustine does not receive Cyprian through a chain of teachers who knew him. He receives "
        "a set of council acts and letters, reads them, and argues with them. He treats a "
        "predecessor's ruling as a document to weigh, not a custom to continue. The inheritance "
        "was therefore received as text rather than carried as living memory. (That sentence "
        "reports how the world understood itself. It is not a judgment of historical accuracy.) "
        "Cyprian was a predecessor met on a page, weighed, answered, and never able to answer "
        "back. And the gap was not felt as a gap. Someone formed in either phase did not know "
        "their world had a documentary silence in it.\n"
        "\n"
        "This has three effects. First, continuity across the gap runs through texts, not through "
        "a line of successors. Augustine's reading of Cyprian's council acts carries the most "
        "across. It is not the only crossing. Possidius quotes Cyprian's book on dying, and "
        "Augustine cites Cyprian on grace against the Pelagians.\n"
        "\n"
        "Second, the gap is richly attested, but by sources that belong to Donatism's territory, "
        "not this world's. So the silence calls for discipline at the boundary; it is not simply "
        "missing evidence. The temptation is to fill it from that other world, and we do not let "
        "ourselves do that.\n"
        "\n"
        "Third, concerns that belong to one phase only reflect the record as well as the world. "
        "Penitential discipline and the confessor-versus-bishop tension are attested only in the "
        "first phase. The concern with grace and human incapacity shapes only the second. Each of these limits "
        "was confirmed by a positive check, not inferred from silence.\n"
        "\n"
        "This is the same pattern that let both men's writings survive on the dominant side. Here "
        "it shapes the span of the record rather than its content.",
        [
            "the roughly 133-year gap between Cyprian's martyrdom (258) and Augustine's "
            "ordination (391), from which no ordinary-pastoral voice of this world that this "
            "build has assessed survives",
            "Augustine reading and arguing with Cyprian's own council acts and letters as a text "
            "to be weighed, not a custom carried by living memory",
        ],
        conf("A", "verified-via-authority", "load-bearing", "Contested",
             "Doc_08 §3 Force 3B-2: the silence claim is Contested -- no surviving voice "
             "continuous with Cyprian's ordinary-pastoral mode, from within this world's "
             "boundary, that this build has assessed dates from within the 133-year gap. Nine "
             "tractatus in Morin 1917 are not yet assessed (OG-54). The uneven attestation of the "
             "span is Documented, a fact about the record checkable against the Registry. Layer "
             "2's own sentence on how the inheritance was received carries the "
             "Reported-Experience Status marker (Constitution Article 17; Forces Framework §3): "
             "reported as the world's own self-understanding, not assessed for historical "
             "accuracy."),
        [],
        "Taken from Doc_08 §3 Force 3B-2 (Cell 3B, Ending/Internal; Transmission dimension). "
        "relations[] carries only the force<->force edges (2B-4, 2B-5) named above -- "
        "deliberately no gravity<->force edge, matching Force 2B-5's own identical disposition. "
        "sources[] is deliberately empty -- this force's own evidentiary base is the absence, so far "
        "as assessed, of this world's own pastoral voice in an interval, not a citable vendored "
        "text making a claim.",
    )


def main() -> None:
    build_gravities()
    build_forces()
    print(f"Wrote {len(WRITTEN)} records:")
    for p in WRITTEN:
        print(f"  {p}")


if __name__ == "__main__":
    main()
