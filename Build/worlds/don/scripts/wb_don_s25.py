"""B-5 (S2.1): Donatism (don) gravity + force records.

WHAT THIS SCRIPT DOES. Converts this world's already-built, already-reviewed
Gravity Discovery (Doc_04_Gravity_Discovery.md, 3 independent adversarial
review rounds, Approved to proceed) and Forces Document (Doc_08_Forces_
Document.md, 2 independent adversarial review rounds, Approved to proceed)
into record-native `gravity` and `force` records under records/don/gravity/
and records/don/force/, per the live schema (engine/m1/schemas.py) and gate
battery (engine/m1/gates.py). This is B-5 of the 9-step record-native build
pipeline (B-1 through B-9); B-1 (41 sources + world_core), B-1a
(search_record), B-2/B-3 (21 term records), and B-4 (9 story, 16 figure, 4
quote records) are already done and committed. Read Build/worlds/don/
scripts/wb_don_s21.py, wb_don_s22_s23.py, and wb_don_s24.py in full before
this script was written (not touched by it, not re-run by it) for the
docstring/code-pattern discipline this script follows, and
records/pahc/gravity/pahc.gravity.boundary-drawing.md +
records/pahc/force/pahc.force.boundary-drawing.md (read in full this
session) as the one real, complete, fleet-precedent worked example of these
two record types: gravity and force are deliberately SEPARATE,
cross-referencing records, never one record covering both, and the six-test
(gravity) / three-layer (force) discipline lives as prose inside the
free-text `description` field -- `classification` (gravity) and
`matrix_cell` (force) are the only structured axes the live schema actually
provides (engine/m1/schemas.py TYPE_PROPERTIES, confirmed by direct read this
session, not assumed from a prior summary).

WHY THIS WORLD'S OWN RECORD SET IS SHAPED DIFFERENTLY FROM PAHC'S. pahc's own
worked example is a 1:1 twin: one Tensional gravity and one force describing
the identical phenomenon at a different grain (2B, ongoing/internal), tied
together explicitly in each record's own body text. Donatism's own Doc_04/
Doc_08 do not have that shape -- Doc_04 confirms EIGHT classified gravities
(4 Primary, 2 Supporting, 2 Tensional) and Doc_08 confirms THIRTEEN forces
across all six matrix cells, connected to those eight gravities in a
many-to-many pattern (Doc_08 SS5's own "Gravity-by-Gravity Force Connections"
and its inverted "By Connected Gravity" table), not a one-force-per-gravity
mirror. This script therefore builds 8 `gravity` records and 13 `force`
records, cross-referenced by a full relations[] graph built from three
distinct sources named in Doc_04/Doc_08 themselves (see RELATION_PAIRS
below), rather than pairing each gravity with one twin force.

**CORRECTION APPLIED, per this step's own launch instruction to check
directly rather than trust a prior summary.** Doc_04 SS3.4's own Dependency
test for G4 reads: "PASS (strong), but reveals Supporting rather than Primary
status" -- G4's Supporting classification rests on the DEPENDENCY test
specifically (the parallel hierarchy has no independent formative content of
its own once G1/G2/G3 are removed), not on Formation (Formation itself PASSES
at "moderate" strength, per the same subsection, for a different reason: it
"shapes which bishop one answers to... but does not itself generate a
distinct formative practice-cluster"). This world's own Decision Log records
that a Representative Phase Seven review chain (`don_Decision_Log.md`, the
"Round 6" entry under Phase Seven, 2026-09-08/09) once misattributed this
same classification to Formation grounds and was corrected back to
Dependency -- this script verified Doc_04's own SS3.4 text directly (not the
Decision Log's summary of the correction, and not Phase Seven's own document)
before writing G4's own record, and every reference to this ground below
cites Doc_04 SS3.4 by section, matching the corrected, current reasoning.

**A SECOND GRAVITY, NOT NAMED IN THIS STEP'S OWN LAUNCH BRIEF, CONFIRMED
DIRECTLY AGAINST DOC_04 AND BUILT HERE.** This step's own launch brief lists
G1, G2, G3, G4, G5, T1, T2 as "everything built so far" and explicitly warns
this list "may be incomplete." Checked directly against Doc_04 SS1, SS3.5,
and SS4 (the Classification Summary and its own required index table): Doc_04
classifies EIGHT candidates, not seven -- D-A (Circumcellion/*Agonistici*
character and scale) is confirmed **Supporting, scope-qualified to the
Numidian regional sub-ecology** (Doc_04 SS3.5, SS4), a genuine classified
gravity that Doc_08 SS5's own inverted table and Force Index both carry
alongside G1-G5/T1/T2 ("All eight of this world's own classified gravities...
connect to at least one identified force," Doc_08 SS5). D-B (Tyconius's own
hermeneutics) and D-C (the Numidian native-social-protest substrate) were
tested and NOT advanced, or deliberately not tested (Doc_04 SS2, SS4) -- this
script does not build gravity records for either, matching Doc_04's own
disposition exactly.

INPUTS, mapped to OUTPUTS, precisely:
  - Doc_04_Gravity_Discovery.md SS1 (Candidate Generation table), SS3
    (Per-Candidate Testing, all eight subsections read in full), SS4
    (Classification Summary and its own required index table), SS5
    (Cross-Voice Test, this world's own declared Article 21 substitute for a
    strand-singular world), SS6 (Interaction Matrix), SS7 (Open Items) ->
    the 8 `gravity` records below (G1, G2, G3, G4, G5, D-A, T1, T2), one
    record per classified candidate. classification is copied directly from
    Doc_04 SS4's own summary (never re-derived); description carries each
    candidate's own six-test verdict, Confidence/Gravity Cross-Check result,
    Cross-Voice Test result (where Doc_04 SS5 applies it), and forces-
    connection summary, condensed from Doc_04's own prose, not merely
    pointing back at it.
  - Doc_08_Forces_Document.md Section 3 (the six-cell matrix, all thirteen
    forces read in full, all three layers each), Section 4 (Cross-Cell
    Connections, all eight named connections), Section 5 (Forces-and-
    Gravities Synthesis, both the gravity-by-gravity list and the inverted
    Force Index table), Section 7 (Confidence Assessment), Section 9 (Force
    Index companion table) -> the 13 `force` records below, one per force
    identified in Section 3. matrix_cell is copied directly from each
    force's own cell heading (1A/1B/2A/2B/3A/3B); kind is derived
    mechanically from the cell (1A/1B -> initiating, 2A/2B -> ongoing,
    3A/3B -> ending), matching the schema's own three-value enum exactly.
    description carries each force's own Layer 1 (Historical Event), Layer 2
    (World's Own Experience), and Layer 3 (Formation Impact) content in
    full, condensed from Doc_08's own prose, per this step's own instruction
    that "a force record that merely gestures at Doc_08's reasoning is
    inadequate."
  - Build/worlds/don/scripts/wb_don_s21.py's own emitted don.source.*
    id list (41 ids, cross-checked against records/don/source/ directly, not
    guessed) -> sources[] on every gravity/force record below, resolved to
    the specific vendored primary/secondary source(s) Doc_04/Doc_08 actually
    cite as that candidate's or force's own evidentiary base. Doc_04/Doc_08
    themselves are this world's own governing analytical documents, not
    vendored sources -- every citation to them lives in each record's own
    description/body text as "(Doc_04 SS3.1)" etc., never in sources[].

RELATIONS -- THREE DISTINCT EDGE SETS, ALL SYMMETRIC associated-with, ALL
BUILT FROM ONE MASTER PAIR-LIST (RELATION_PAIRS), matching wb_don_s24.py's
own closed-graph discipline exactly (one list, both directions derived by
relations_for(), so every edge is reciprocated by construction rather than by
hand-checking each record afterward -- gate_reciprocity is exactly where a
one-directional gap is easiest to introduce, per this step's own launch
brief, and this is the mechanical guard against it):
  1. GRAVITY <-> GRAVITY (Doc_04 SS6, the Interaction Matrix): every pair
     Doc_04 SS6 marks R (reinforcing), C (competing), or X (reshaping) --
     "a demonstrated relationship" in that section's own words -- becomes one
     associated-with edge. The R/C/X label itself is not a schema-typed
     axis (RELATION_TYPES has no reinforcing/competing/reshaping value); it
     is carried in each gravity's own description prose instead, matching
     pahc.gravity.boundary-drawing's own precedent of stating relationship
     character in prose while relations[] carries only the fact of
     connection.
  2. GRAVITY <-> FORCE (Doc_04 SS3's own per-candidate "Forces-connection"
     bullets, cross-checked against Doc_08 SS5's "Gravity-by-Gravity Force
     Connections" and its own inverted "By Connected Gravity" table --
     both name the identical 25 edges, independently verified against each
     other before this script was written): every force a gravity's own
     record lists as connected becomes one associated-with edge.
  3. FORCE <-> FORCE (Doc_08 Section 4, the eight named Cross-Cell
     Connections; Connection 7 names two forces jointly producing a third,
     so it contributes two edges): every named connection becomes one
     associated-with edge, direction (which Doc_08's own arrow states)
     carried in each force's own description prose, not in the relation
     type -- RELATION_TYPES's directional pairs (precondition-for/
     enabled-by) were considered and rejected for this edge set: several of
     Doc_08's own eight connections state a "converge on"/"the same
     mechanism operating at two phases" relationship rather than a strict
     precondition, and forcing all eight into one directional shape would
     overclaim precision Doc_08's own prose does not uniformly support.

NO-RELATIONSHIP PAIR NAMED, NOT SILENTLY OMITTED. Doc_04 SS6's own Interaction
Matrix states explicitly: "T1 <-> T2 (-, no demonstrated relationship)...
naming this absence explicitly is itself a finding, not an oversight." This
is NOT encoded as a relations[] entry (relations[] has no typed way to assert
absence-of-relationship; a missing edge and a checked, explicit non-
relationship both read identically in that array as "nothing declared"). Per
this step's own launch instruction not to let a Doc_04-explicit non-
relationship silently read as an unexamined gap, both don.gravity.
principled-refusal-vs-pragmatic-recourse (T1) and don.gravity.purity-rigor-
vs-institutional-reception (T2)'s own description text states this explicit
finding directly, citing Doc_04 SS6 by name.

MECHANICAL vs AUTHORED, field by field:
  - id, world_id, record_type, schema_version, status, register, canon_cells:
    MECHANICAL. register="etic" throughout -- gravity/force are this world's
    own analytical build documents converted to record-native form, not
    first-person community voice (matching pahc.gravity.boundary-drawing's
    and pahc.force.boundary-drawing's own register="etic" exactly). Neither
    record type is scoped by gate_voice_perspective's own _PERSPECTIVE_FIELDS
    (checked directly against engine/m1/gates.py: only term/story/ambient/
    doctrinal_witness/honest_limit are listed) or by gate_no_build_
    attribution's own _ATTRIBUTION_FIELDS (same check, same result) -- so
    "this world"/"the world's own" phrasing, freely used throughout Doc_04
    and Doc_08's own prose, is not a gate risk here the way it would be in a
    story or term record's own voice-scoped fields. canon_cells=[]
    throughout, unchanged from every prior step's own note.
  - name, classification (gravity) / name, kind, matrix_cell (force):
    MECHANICAL -- classification and matrix_cell copied directly from
    Doc_04 SS4 and each force's own Doc_08 SS3 cell heading, never
    re-derived; kind mechanically follows matrix_cell per the cell-to-kind
    mapping stated above.
  - description: AUTHORED, condensed from Doc_04 SS3's six-test verdicts
    (gravity) or Doc_08 SS3's three-layer entries (force), carrying the
    actual argument rather than a pointer back to either document, per this
    step's own launch instruction.
  - manifestations[]: AUTHORED, drawn only from concrete, already-vendored
    or already-verified-in-this-build facts and quotations (Petilian's and
    Donatus's own quoted words, already independently re-verified for
    wb_don_s24.py's own quote records; the Deo laudes acclamation; named
    dated events Doc_04/Doc_08 themselves state) -- never a fresh
    translation or a fact from this session's own outside historical
    knowledge.
  - confidence.formation_confidence: AUTHORED per record, copied from each
    candidate's own Confidence/Gravity Cross-Check result (Doc_04 SS3.x) or
    each force's own Section 7 confidence tier (Doc_08), never re-derived.
    D-A's own THREE-tier split (existence Documented; self-designation
    Augustine-reported; character at most Dominant Modern Reconstruction,
    Doc_04 SS3.5) is carried at the single most conservative applicable
    tier for this record's own top-line rating -- Dominant Modern
    Reconstruction, matching the classification's own scope-qualification
    ground (character/scale, not bare existence) -- with the full three-
    tier split named explicitly in divergence_note, never smoothed into an
    unqualified single rating. Force 3B-1 (institutional attrition) is the
    one force this document itself (Doc_08 SS7, "Forces at Inferential/Thin
    Level") splits between Documented (bare occurrence) and Inferential-Thin
    (specific shape) -- carried here at Inferential-Thin, its own more
    conservative tier, with the same two-tier split named in divergence_note.
  - confidence.verification_state: AUTHORED, held to verified-via-authority
    throughout (never verified-direct) -- this script relies on Doc_04's and
    Doc_08's own already-completed, independently-reviewed (3 rounds and 2
    rounds respectively) six-test/three-layer assessments, not on this
    session re-opening the raw vendored primary texts itself, matching the
    same distinction wb_don_s24.py's own docstring already draws for its own
    non-quote, non-Emeritus records.
  - confidence.divergence_note: AUTHORED per record, always populated
    (never null) -- every one of these 21 records has a real, specific,
    citable divergence or convergence finding worth naming (this satisfies
    gate_confidence_crosscheck by construction: Documented + null
    divergence_note is the one combination that gate rejects, and this
    script never emits that combination).
  - confidence.citation_specificity / evidentiary_weight: AUTHORED per
    record from Doc_04/Doc_08's own stated evidentiary texture (A where a
    specific text/locus grounds the claim directly; B where the grounding is
    Doc_04/Doc_08's own already-completed synthesis of several such loci;
    "load-bearing" throughout, since every classified gravity and identified
    force is, by Doc_04/Doc_08's own express finding, organizing/formative
    content, not corroborating or illustrative material).
  - sources[]: AUTHORED per record, resolved to the specific don.source.*
    ids (from B-1's own 41-record set, cross-checked against
    records/don/source/ directly) that Doc_04 SS1/SS3 or Doc_08 SS3 actually
    cite as that candidate's or force's own evidentiary base. Two forces
    (3A-2, the Vandal capture; 3B-1, institutional attrition) have no
    specific don.source.* grounding either document names -- both are named
    as a disclosed gap in that force's own body text (sources: []) rather
    than forcing an unearned citation onto either record.
  - relations[]: MECHANICAL, built entirely by relations_for() from
    RELATION_PAIRS -- see "RELATIONS" above.

WHAT THIS SCRIPT DOES NOT DO: assign canon_cells; touch records/don/{source,
world_core,term,story,figure,quote,search_record}/ (existing B-1/B-1a/B-2/
B-3/B-4 records are read only, for their own don.source.* ids, never
edited); build don.contested_claim.* records (a later step); build gravity
records for D-B or D-C, both tested and not advanced at Doc_04 SS2/SS4;
declare relations[] from any gravity/force record to any don.story.*/
don.figure.*/don.quote.*/don.term.* record (B-4's own docstring already
established this closed-graph discipline for exactly this reason -- this
world's own gravity/term/figure connections stay in prose, in each existing
record's own body text, not retrofitted here); run the M2 compiler; register
`don` in records/worlds.yaml (B-9).
"""
from __future__ import annotations

from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[2]  # .../cic-project
RECORDS_ROOT = REPO_ROOT / "records" / "don"

WORLD_ID = "don"
SCHEMA_VERSION = 2

WRITTEN: list[str] = []

# ---------------------------------------------------------------------------
# Gravity ids
G1 = "don.gravity.ministerial-purity"
G2 = "don.gravity.rebaptism-boundary-marking"
G3 = "don.gravity.martyr-cult-identity"
G4 = "don.gravity.parallel-institutional-hierarchy"
G5 = "don.gravity.refusal-of-imperial-legitimacy"
DA = "don.gravity.circumcellion-agonistici"
T1 = "don.gravity.principled-refusal-vs-pragmatic-recourse"
T2 = "don.gravity.purity-rigor-vs-institutional-reception"

# Force ids
F1A1 = "don.force.diocletianic-persecution-traditio-demand"
F1B1 = "don.force.cyprianic-rigorist-inheritance"
F1B2 = "don.force.felix-accusation-majorinus-consecration"
F2A1 = "don.force.oscillating-imperial-policy"
F2A2 = "don.force.macarian-repression"
F2B1 = "don.force.sustained-purity-rebaptism-practice"
F2B2 = "don.force.transmission-hostile-manuscript-tradition"
F2B3 = "don.force.martyr-cult-confessor-memory"
F2B4 = "don.force.maximianist-fracture"
F3A1 = "don.force.conference-of-carthage-verdict"
F3A2 = "don.force.vandal-capture-of-carthage"
F3B1 = "don.force.institutional-attrition"
F3B2 = "don.force.transmission-caecilianist-victory"

# RELATION_PAIRS: the whole closed relation graph across gravity and force
# records, each edge listed once as (a, b) -- both directions derived by
# relations_for() below, "associated-with" throughout (the one symmetric
# relation type; see this script's own docstring for why the R/C/X label,
# and the connection's own directional arrow, are carried in prose instead).
RELATION_PAIRS: list[tuple[str, str]] = [
    # --- 1. GRAVITY <-> GRAVITY (Doc_04 SS6 Interaction Matrix; 15 edges,
    # excluding T1<->T2, explicitly "no demonstrated relationship" per that
    # same section and named in prose only, not here) ---
    (G1, G2), (G1, G3), (G1, G4), (G1, G5), (G1, T2),
    (G2, G4), (G2, G5), (G2, T2),
    (G3, G4), (G3, G5),
    (G4, G5), (G4, T2),
    (G5, T1),
    (DA, G5), (DA, T2),

    # --- 2. GRAVITY <-> FORCE (Doc_04 SS3 Forces-connection bullets, cross-
    # checked against Doc_08 SS5's own gravity-by-gravity list and inverted
    # Force Index table; 25 edges) ---
    (G1, F1B1), (G1, F1B2), (G1, F2B1), (G1, F2B4),
    (G2, F1B1), (G2, F2A1), (G2, F2B1),
    (G3, F1A1), (G3, F2A2), (G3, F2B3), (G3, F3B2),
    (G4, F1B2), (G4, F2B4), (G4, F3A1), (G4, F3A2), (G4, F3B1),
    (G5, F2A1), (G5, F3A1), (G5, F3A2),
    (DA, F2A1), (DA, F2B4),
    (T1, F1B2), (T1, F2A1), (T1, F2B4),
    (T2, F2B4),

    # --- 3. FORCE <-> FORCE (Doc_08 Section 4 Cross-Cell Connections; 9
    # edges -- Connection 7 names two forces jointly producing a third,
    # contributing two edges) ---
    (F1A1, F2A2),          # Connection 1
    (F1B2, F2B1),          # Connection 2
    (F1B2, F2A1),          # Connection 3
    (F2A2, F2B3),          # Connection 4
    (F2A1, F2B4),          # Connection 5
    (F2B4, F3A1),          # Connection 6
    (F3A1, F3B1),          # Connection 7a
    (F3A2, F3B1),          # Connection 7b
    (F2B2, F3B2),          # Connection 8
]


def relations_for(rid: str) -> list[dict]:
    out = []
    for a, b in RELATION_PAIRS:
        if a == rid:
            out.append({"type": "associated-with", "target": b})
        elif b == rid:
            out.append({"type": "associated-with", "target": a})
    return out


def conf(cite, verify, weight, formation, divergence):
    assert divergence is not None, (
        "B-5 house rule: every gravity/force record's own divergence_note is authored and "
        "populated, never null -- see this script's own docstring"
    )
    if formation == "Documented":
        assert verify == "verified-direct" or divergence is not None, (
            "would trip gate_confidence_crosscheck: Documented + null divergence_note requires "
            "verified-direct"
        )
    return {
        "citation_specificity": cite,
        "verification_state": verify,
        "evidentiary_weight": weight,
        "formation_confidence": formation,
        "divergence_note": divergence,
    }


def src(*ids):
    return [{"source_id": i, "locus": "see this record's own body text for the specific locus "
                                       "Doc_04/Doc_08 cite", "license": "public-domain"} for i in ids]


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
        "canon_cells": [],
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
        "canon_cells": [],
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
# GRAVITIES (8) -- Doc_04 SS3, classification per SS4's own summary table.
# ===========================================================================

def build_gravities() -> None:
    emit_gravity(
        G1, "Ministerial Purity / Traditor-Free Sacramental Validity [PRIMARY]",
        "primary",
        "Doc_04 SS3.1: PRIMARY, 6/6 tests PASS (strong). Repetition: recurs across Doc_01 SS1/SS5, "
        "Doc_02 SS1 (the founding accusation against Felix of Aptungi; Augustine's On Baptism "
        "devoting seven books to it; Petilian's own quoted rebaptism-theology argument, Registry "
        "row 12), Doc_03's Tier-1 Traditor/Traditio and Purity entries. Dependency: rebaptism (G2) "
        "is this doctrine's enacted logic; the parallel hierarchy (G4) exists because an impure "
        "ordination line had to be replaced; the Maximianist affair's (T2) entire significance is "
        "that it tests this doctrine's own internal consistency. Formation: the stated ground of "
        "communal legitimacy itself (Doc_01 SS1: clerical purity as the ground of sacramental "
        "validity). Explanatory: explains the schism's 311/312 origin, the refusal to reunite under "
        "imperial pressure, and the Maximianist paradox's own specific shape. Persistence: live "
        "311/312 through the 411 Conference. Interaction: reinforces G2 and G4; reshaped by T2. "
        "CONFIDENCE/GRAVITY CROSS-CHECK -- consistent, one flagged divergence: the doctrine's "
        "existence and centrality is Documented (Petilian's own quoted words, Registry row 12, "
        "converging with the Maximianist affair's own independent logic); the specific "
        "argumentative shape -- precisely how the Donatist side reasoned from traditio to invalid "
        "ordination to invalid sacrament -- reaches this document substantially through Augustine's "
        "own refutation (Doc_02 SS1's Author Gravity finding). This divergence is named, not "
        "resolved by treating Augustine's paraphrase as a Donatist self-statement. CROSS-VOICE TEST "
        "(Doc_04 SS5, this world's own declared Article 21 substitute for a strand-singular world): "
        "passes with the same qualification -- existence is cross-voice attested (Petilian), "
        "argumentative texture remains hostile-mediated; this convergence with the Cross-Check "
        "finding is itself a form of corroboration. INTERACTION MATRIX (Doc_04 SS6): R "
        "(reinforcing) with G2 (the organizing spine -- G1 doctrinal ground, G2 its enacted rite), "
        "G3 (martyrdom read as proof the purity claim is sincerely held), G4 (the parallel "
        "hierarchy exists to embody an unbroken traditor-free ordination line), and G5 (Doc_01 "
        "SS1's own Core Identity ties the two: the movement claims to be pure against a rival it "
        "regarded as traditor-tainted and, from 312, state-favored). X (reshaping) with T2: the "
        "Maximianist reception-without-reordination precedent directly reshapes G1's own internal "
        "consistency, and Augustine turns this reshaping into his central argument against Donatist "
        "rebaptism logic. FORCES-CONNECTION (Doc_04 SS3.1, Doc_08 SS5): grounded by 1B-1 (the "
        "Cyprianic rigorist inheritance, sharpened by the traditio accusation) and 1B-2 (the Felix/"
        "Majorinus founding rupture); sustained ongoing by 2B-1; reshaped without fracturing by "
        "2B-4 (the Maximianist fracture).",
        [
            "Petilian of Constantina, quoted by Augustine: \"For what we look to is the conscience "
            "of the giver, to cleanse that of the recipient\" (don.quote.petilian-conscience-of-the-"
            "giver; Augustine, Answer to the Letters of Petilian, Book II, Chapter 3)",
            "the traditio accusation against Felix of Aptungi, bishop who consecrated Caecilian, "
            "collapsing under a forger's own confession at the Acta Purgationis Felicis (314)",
            "Augustine devoting seven full books (On Baptism, Against the Donatists) to refuting "
            "this doctrine's own rebaptism logic",
        ],
        conf("A", "verified-via-authority", "load-bearing", "Documented",
             "Core doctrine's existence and centrality is Documented (Petilian's own quoted words, "
             "Registry row 12, converging with the Maximianist affair's own independent logic, "
             "per Doc_04 SS3.1); the specific argumentative texture -- exactly how the traditio-to-"
             "invalid-sacrament reasoning proceeds -- reaches this document substantially through "
             "Augustine's own refutation (Doc_02 SS1's Author Gravity concentration), a divergence "
             "Doc_04 SS3.1 names rather than smooths over."),
        src("don.source.petilian-of-constantina-letters-quoted",
            "don.source.augustine-answer-to-letters-of-petilian",
            "don.source.augustine-on-baptism-against-donatists",
            "don.source.optatus-appendix-of-documents",
            "don.source.cyprian-on-the-unity-of-the-church"),
        "Re-derived from the approved Doc_04 SS3.1 (G1), cross-checked against Doc_04 SS4's own "
        "index table and Doc_04 SS6's Interaction Matrix and Doc_04 SS5's Cross-Voice Test. "
        "relations[] carries the gravity<->gravity edges (G2, G3, G4, G5, T2) and the gravity<->"
        "force edges (1B-1, 1B-2, 2B-1, 2B-4) named in this record's own description above; the "
        "R/C/X character of each gravity<->gravity edge and the specific role of each connected "
        "force are stated in prose here rather than in the relation type, matching pahc."
        "gravity.boundary-drawing's own precedent.",
    )

    emit_gravity(
        G2, "Rebaptism as Boundary-Marking Practice [PRIMARY]",
        "primary",
        "Doc_04 SS3.2: PRIMARY, 6/6 tests PASS (strong). Repetition: Doc_02 SS1 (On Baptism, "
        "Answer to the Letters of Petilian, both substantially devoted to this practice); Doc_01 "
        "SS1/SS3 (\"rebaptism as the rite that marks who truly belongs\"). Dependency: membership "
        "status depends on it; the Council of Carthage 419 canons on receiving Donatist clergy "
        "(Registry row 13) depend on it; the Maximianist reception-without-rebaptism precedent (T2) "
        "depends on rebaptism being the operative norm it departs from. Formation: the literal "
        "liturgical act of entry and re-entry, the most concretely enacted, individually experienced "
        "marker of belonging this world's record documents. Explanatory: explains why the movement "
        "drew sustained imperial legal attention (rebaptizing Catholics was itself a targeted legal "
        "offense) and the specific content of the 411 Conference's own concerns. Persistence: "
        "attested from origin through the 411 Conference; Doc_01 SS2 additionally names Gregory the "
        "Great's 590s correspondence bearing on Donatist rebaptism specifically in Numidia -- now "
        "partially vendored (Registry row 54, corrected 2026-09-08) and directly confirming "
        "rebaptism as a live Donatist practice in Numidia through 592, though this document does not "
        "extend that into a claim about the practice's own scale or character at that date beyond "
        "the letters' own words. Interaction: reinforces G1 (its doctrinal ground); reshaped by T2; "
        "the specific target of G5's own imperial legislative attention. CONFIDENCE/GRAVITY "
        "CROSS-CHECK -- consistent, no significant divergence: the bare fact of the practice is "
        "Documented, attested directly and repeatedly in Augustine's own primary text and "
        "corroborated by Petilian's own quoted argument. CROSS-VOICE TEST (Doc_04 SS5): passes -- "
        "the practice is argued FOR in Petilian's own quoted words (Registry row 12), not merely "
        "characterized by hostile opponents; corroboration from within the hostile text's own "
        "quotation of a Donatist voice, the same qualification as G1. INTERACTION MATRIX (Doc_04 "
        "SS6): R with G4 (the hierarchy administers and enforces rebaptism at institutional scale) "
        "and G5 (rebaptism of Catholics is the specific practice successive imperial edicts name and "
        "target); X (reshaping) with T2 (directly tested and complicated by the Maximianist "
        "reception precedent, as with G1). FORCES-CONNECTION (Doc_04 SS3.2, Doc_08 SS5): grounded "
        "by 1B-1 (the same Cyprianic doctrinal ground G1 shares, not 1B-2, which grounds G4's own "
        "institutional form rather than G2's own enacted rite directly); sustained ongoing by 2B-1 "
        "(G2's own enacted, ongoing form); interacts directly with 2A-1 (oscillating imperial "
        "policy, the direct target of successive edicts naming rebaptism specifically).",
        [
            "Augustine, On Baptism, Against the Donatists -- seven books devoted substantially to "
            "this one practice",
            "Petilian of Constantina's own quoted rebaptism-theology argument (Registry row 12)",
            "Gregory the Great's letter to Columbus, bishop of Numidia (592), reporting an inquiry "
            "into a bishop \"corrupted\" into permitting Donatist rebaptism",
        ],
        conf("A", "verified-via-authority", "load-bearing", "Documented",
             "The bare fact of the practice is Documented (Doc_04 SS3.2), resting on the vendored "
             "Optatus/Augustine corpus and Petilian's quoted words; the Gregory correspondence "
             "(Registry row 54) is also vendored and directly confirms rebaptism as a live Donatist "
             "practice in Numidia as late as 592, but is not needed to establish the bare-practice "
             "claim itself, which the 4th/5th-century corpus already documents directly -- this "
             "document does not extend the Gregory material into a scale or character claim beyond "
             "the letters' own words (Doc_04 SS3.2's own Persistence-test discussion)."),
        src("don.source.augustine-on-baptism-against-donatists",
            "don.source.augustine-answer-to-letters-of-petilian",
            "don.source.petilian-of-constantina-letters-quoted",
            "don.source.gregory-great-epistolae-selectae-turchi",
            "don.source.code-of-canons-african-church-419"),
        "Re-derived from the approved Doc_04 SS3.2 (G2). relations[] carries the gravity<->gravity "
        "edges (G4, G5, T2) and gravity<->force edges (1B-1, 2A-1, 2B-1) named above.",
    )

    emit_gravity(
        G3, "Martyr-Cult Identity / \"Church of the Martyrs\" [PRIMARY]",
        "primary",
        "Doc_04 SS3.3: PRIMARY, 6/6 tests PASS (strong to very strong) -- this world's own least "
        "Author-Gravity-encumbered Primary. Repetition (very strong): Doc_02 SS4 (the Passio "
        "Marculi, Macrobius's own letter to the Carthage congregation on Isaac and Maximianus, and "
        "the newly-integrated Passio Donati sermon -- three distinct Donatist-voiced or -authored "
        "texts); SS5 (the Deo laudes acclamation, independently attested epigraphically at Bagai and "
        "elsewhere); Step0 SS1's own disclosure naming this \"this world's own distinctive strength "
        "among the nine confirmed worlds.\" Dependency: the community's own self-legitimation "
        "narrative (a persecuted church is thereby a true one) draws directly on this; the liturgical "
        "calendar is organized around it; G1's own credibility as a lived, not merely asserted, "
        "purity claim rests partly on having concretely suffered for it. Formation: liturgical "
        "commemoration, preached anniversary sermons, and communal memory-making are the most "
        "directly formative, repeatedly-enacted practices this world's record documents. Explanatory: "
        "explains the specific liturgical vocabulary (Deo laudes, anniversaria commemoratio) and the "
        "durability of textual production after each persecution episode. Persistence (very strong): "
        "textually attested across nearly the entire construction window, from the sermon (Monceaux's "
        "dating: 317 events, c. 320 composition -- the earliest Donatist-authored text in this "
        "world's entire vendored corpus) through the Macarian-era Passiones (347-348). Interaction: "
        "reinforces G1 and G5; the specific bishops martyred (a bishop of Sicilibba wounded, the "
        "bishop of Advocata killed) tie directly to G4. CONFIDENCE/GRAVITY CROSS-CHECK -- consistent, "
        "and the strongest evidentiary base of the four Primaries: this gravity's core reality is "
        "Documented on grounds substantially independent of Optatus's and Augustine's own hostile "
        "framing -- three separate Donatist-voiced or -authored texts plus non-textual epigraphic "
        "corroboration (stone, no literary mediation at any point) converge on it. Of the four "
        "Primary gravities, this is the one whose specific evidentiary texture, not merely its bare "
        "existence, escapes the hostile-mediation problem qualifying G1 and G5. CROSS-VOICE TEST "
        "(Doc_04 SS5): passes most cleanly of all four Primaries -- the one gravity in this document "
        "substantially attested IN the Donatist-voiced or non-mediated record itself, not merely "
        "corroborated by a fragment of it. INTERACTION MATRIX (Doc_04 SS6): R with G1, G4, and G5 "
        "(all named above under each of those gravities' own entries). FORCES-CONNECTION (Doc_04 "
        "SS3.3, Doc_08 SS5): rooted in 1A-1 (the Diocletianic persecution, the deep root of this "
        "world's own persecution-memory); the direct trigger of 2A-2 (the Macarian repression, "
        "producing the two best-attested Passiones); sustained ongoing by 2B-3 (the annual "
        "commemorative practice); and, per the Transmission dimension, tied to 3B-2 -- this "
        "gravity's own textual survival IS substantially this world's own surviving voice, per "
        "Doc_01 SS5's own \"small independently-surviving remainder\" finding.",
        [
            "the Deo laudes / Bagai acclamation, \"Praise to God\" (don.quote.deo-laudes-"
            "acclamation; CIL VIII 17732, epigraphic, no manuscript mediation)",
            "Marculus's cliff-top vision of a cup, a crown, and a palm before his death at "
            "Novapetra (don.story.passio-marculi)",
            "the annual reading, every twelfth of March, of the Passio Donati at the martyrs' own "
            "grave (don.story.passio-donati-sermon)",
        ],
        conf("A", "verified-via-authority", "load-bearing", "Documented",
             "This gravity's core reality is Documented on grounds substantially independent of "
             "Optatus's and Augustine's own hostile framing -- three separate Donatist-voiced or -"
             "authored texts plus non-mediated epigraphy converge on it (Doc_04 SS3.3); this is "
             "named as a positive, deliberate finding, not merely an absence of a caveat -- of the "
             "four Primary gravities, this is the one whose specific evidentiary texture escapes "
             "the hostile-mediation problem qualifying G1 and G5."),
        src("don.source.passio-marculi",
            "don.source.passio-isaac-et-maximiani",
            "don.source.passio-donati-sermon",
            "don.source.deo-laudes-acclamation-cil8",
            "don.source.monceaux-histoire-litteraire-tome5"),
        "Re-derived from the approved Doc_04 SS3.3 (G3). relations[] carries the gravity<->gravity "
        "edges (G1, G4, G5) and gravity<->force edges (1A-1, 2A-2, 2B-3, 3B-2) named above.",
    )

    emit_gravity(
        G4, "Parallel Institutional Hierarchy [SUPPORTING -- integrating/institutional center]",
        "supporting",
        "Doc_04 SS3.4: SUPPORTING (integrating/institutional center), 6/6 tests PASS -- **the "
        "Dependency test is specifically what reveals Supporting rather than Primary status, not "
        "the Formation test** (verified directly against Doc_04 SS3.4's own text this session, "
        "correcting a misattribution to Formation grounds that a Representative Phase Seven review "
        "round once introduced and this world's own Decision Log records as fixed -- see this "
        "script's own docstring). Repetition: Doc_01 SS2 (\"two rival bishoprics from the outset... "
        "the contest replicated town-for-town\"); SS3 (\"the parallel episcopal hierarchy are this "
        "world's most recurring formative material\"). DEPENDENCY -- PASS (strong), BUT REVEALS "
        "SUPPORTING STATUS: the Maximianist internal fracture is only possible because a complex "
        "hierarchy with its own councils and disciplinary machinery already exists; the specific "
        "shape of the 411 Conference (279 against 286 bishops seated) and the property/basilica "
        "disputes depend on there being two complete, rival institutional claimants -- BUT, removed "
        "from G1/G2/G3, the hierarchy has no independent formative content of its own: it is the "
        "structure WITHIN WHICH purity, rebaptism, and martyr-commemoration operate, not itself a "
        "distinct thing participants experience formation THROUGH the way they experience rebaptism "
        "or martyr-liturgy. Formation -- PASS (moderate): shapes which bishop one answers to and "
        "which basilica one attends, but does not itself generate a distinct formative practice-"
        "cluster beyond what G1/G2/G3 already supply -- this is Doc_04's own separate, weaker-"
        "graded Formation finding, distinct from the Dependency finding that actually grounds the "
        "Supporting classification. Explanatory: explains the precise mechanics of the Maximianist "
        "affair and the exact bishop-count precision of the 411 Conference's own record. Persistence: "
        "\"town for town,\" sustained 311/312 through 439 and beyond (institutional attrition, not "
        "extinction). Interaction: the institutional condition that makes G1/G2's enforcement and "
        "G3's liturgical commemoration operate at the scale of a complete rival church; the "
        "Maximianist fracture (T2) emerges from within it. CONFIDENCE/GRAVITY CROSS-CHECK -- "
        "consistent: the bare institutional fact is Documented to an unusually high degree even by "
        "this world's own hostile-source standards -- Optatus, Augustine, and the imperial/conciliar "
        "record all agree it happened, down to precise bishop counts. Individual bishops' own "
        "conduct and motives remain hostile-mediated, but the institutional fact of parallel "
        "hierarchy itself carries no comparable Author Gravity risk. CROSS-VOICE TEST (Doc_04 SS5): "
        "passes on the bare institutional fact, which even hostile sources do not dispute reporting; "
        "individual bishop characterizations remain hostile-mediated. INTERACTION MATRIX (Doc_04 "
        "SS6): R with G1, G2, G3, G5 (each named under that gravity's own entry above); X (reshaping) "
        "with T2 -- the Maximianist fracture is an event internal to this hierarchy's own conciliar "
        "machinery, and could not exist without G4's own institutional complexity to fracture "
        "within. FORCES-CONNECTION (Doc_04 SS3.4, Doc_08 SS5): the institutional expression of "
        "G1's own founding logic at 1B-2; an internal force operating within, and testing, its own "
        "conciliar machinery at 2B-4; acted on directly as a legal-institutional target at 3A-1 "
        "(the 411 Conference verdict); its own contesting power removed at 3A-2 (the Vandal "
        "capture); and the specific limit on what this construction can claim about its own later "
        "life is named at 3B-1 (institutional attrition, ending precisely where the vendored record "
        "does, not where the movement itself actually ended).",
        [
            "the successive Carthage primates Majorinus -> Donatus -> Parmenian -> Primian "
            "(don.figure.majorinus, don.figure.donatus, don.figure.parmenian, don.figure.primian)",
            "279 Donatist against 286 Catholic bishops seated at the 411 Conference of Carthage "
            "(corrected 2026-09-09 from an earlier, unverified 284 figure; Doc_02 SS1)",
            "a rival consecration replicated \"town for town\" against the Caecilianist hierarchy, "
            "sustained 311/312 through 439",
        ],
        conf("A", "verified-via-authority", "load-bearing", "Documented",
             "The bare institutional fact -- two complete, rival hierarchies existed and contested "
             "the same sees -- is Documented to an unusually high degree even by this world's own "
             "hostile-source standards (Optatus, Augustine, and the imperial/conciliar record all "
             "agree, down to precise bishop counts at the 411 Conference; Doc_04 SS3.4); individual "
             "bishops' own conduct and motives (e.g. Optatus Gildonianus's characterization) remain "
             "hostile-mediated and are not carried at this same confidence."),
        src("don.source.optatus-against-donatists",
            "don.source.optatus-appendix-of-documents",
            "don.source.gesta-collationis-carthaginiensis"),
        "Re-derived from the approved Doc_04 SS3.4 (G4), with the Dependency-not-Formation "
        "classification ground independently re-verified against Doc_04 SS3.4's own text this "
        "session (see this script's own docstring for the correction this applies). relations[] "
        "carries the gravity<->gravity edges (G1, G2, G3, G5, T2) and gravity<->force edges (1B-2, "
        "2B-4, 3A-1, 3A-2, 3B-1) named above.",
    )

    emit_gravity(
        G5, "Refusal of Imperial/State Religious Legitimacy [PRIMARY]",
        "primary",
        "Doc_04 SS3.7: PRIMARY, 6/6 tests PASS (Persistence qualified by T1). Repetition: Doc_01 "
        "SS3 (named as a preliminary candidate: \"resistance to state-backed religious coercion as a "
        "lived, recurring experience\"); SS5's Historical Pressures (Constantine's coercive measures "
        "316-321; Julian's 361 toleration; sustained legal suppression from the 405 Edict) and "
        "Historical Catalysts (Rome 313 and Arles 314, both ruling against the Donatist party and "
        "both rejected rather than accepted as legitimate verdicts; the 411 Conference). Dependency: "
        "G3's own martyrs die specifically because of this refusal; Doc_01 SS2's own 439 ending-"
        "boundary is defined by this refusal's own object -- the Roman-imperial, Catholic-aligned "
        "adjudicating power -- being removed; G4's own recurring legal jeopardy stems from the same "
        "refusal. Formation: living under recurring legal jeopardy while refusing to concede the "
        "state's own authority to adjudicate legitimacy is a lived communal stance across "
        "generations. Explanatory: explains why the 313/314 rulings were rejected rather than "
        "accepted, and the recurring pattern of imperial legislative attention. PERSISTENCE -- PASS, "
        "WITH THE SAME QUALIFICATION T1 EXISTS TO NAME: Doc_01 SS5 itself states the pattern "
        "\"remains refusal-under-pressure on balance... not an absolute refusal at every point\" -- "
        "three specific, documented turns to the same imperial machinery (313, 361, the 390s) "
        "qualify an otherwise dominant, sustained pattern; not a Persistence failure (the dominant "
        "pattern holds across the whole window), but the specific qualification T1 names and tests "
        "as its own Tensional gravity. Interaction: reinforces G3 and G2; interacts with G4; "
        "directly qualified by T1; interacts narrowly with D-A. CONFIDENCE/GRAVITY CROSS-CHECK -- "
        "consistent, one flagged divergence matching G1's own pattern: the recurring historical "
        "episodes themselves are Documented, cross-corroborated even by hostile sources reporting "
        "and justifying their own side's actions; the specific interpretive frame -- that these "
        "episodes together constitute a principled refusal rather than an unconnected series of "
        "grievances -- rests partly on this document's own synthesis of Doc_01 SS5, corroborated by "
        "one direct, hostile-mediated quotation of the Donatists' own voice: Donatus's own reported "
        "retort, \"Quid est imperatori cum ecclesia?\" (\"What has the emperor to do with the "
        "church?\" -- independently re-verified against Optatus, Against the Donatists, Book III). "
        "CROSS-VOICE TEST (Doc_04 SS5): passes with the same qualification as G1 and G2 -- Donatus's "
        "own quoted retort is a direct utterance attributed to a Donatist voice, though it reaches "
        "this document through Optatus's own hostile narrative frame. INTERACTION MATRIX (Doc_04 "
        "SS6): R with G1, G2, G3, G4 (each named under that gravity's own entry); R with T1 (the "
        "same evidentiary base viewed from two angles -- T1 is G5's own internal qualification, "
        "named separately because it meets the Tensional-gravity bar in its own right); narrow R "
        "with D-A (the direct object of specific imperial legislation, CTh 16.5.52, itself part of "
        "G5's own evidentiary base). FORCES-CONNECTION (Doc_04 SS3.7, Doc_08 SS5): sustained "
        "throughout by 2A-1 (oscillating imperial policy, the direct external pressure T1 tests); "
        "pressed to its sharpest test, together with 3A-2, at 3A-1 (the 411 Conference verdict) -- "
        "the two jointly, per Doc_04 SS3.7's own words, \"the most direct forces-connection of any "
        "gravity in this document,\" removing the specific power this gravity is defined in refusal "
        "of and closing this world's own construction window.",
        [
            "Donatus's own reported retort: \"Quid est imperatori cum ecclesia?\" (\"What has the "
            "emperor to do with the church?\", don.quote.donatus-quid-est-imperatori; Optatus, "
            "Against the Donatists, Book III)",
            "the Council of Rome (313) and the Council of Arles (314), both ruling against the "
            "Donatist party and both rejected rather than accepted as legitimate verdicts",
            "the Vandal capture of Carthage (439), removing the Roman-imperial, Catholic-aligned "
            "adjudicating power this refusal is defined against (Doc_01 SS2)",
        ],
        conf("A", "verified-via-authority", "load-bearing", "Documented",
             "The recurring historical episodes themselves (313/314 rulings and their rejection, "
             "the Macarian repression, the 405 Edict, the 411 Conference) are Documented, cross-"
             "corroborated even by hostile sources reporting their own side's actions; the specific "
             "interpretive frame -- that these episodes together constitute a principled refusal "
             "rather than an unconnected series of grievances -- rests partly on this document's "
             "own synthesis, though corroborated by Donatus's own directly-quoted retort (Doc_04 "
             "SS3.7); this divergence is named rather than smoothed over, the same pattern G1's "
             "own core/argumentative-texture split follows."),
        src("don.source.optatus-against-donatists",
            "don.source.codex-theodosianus-book-16",
            "don.source.boyd-ecclesiastical-edicts-theodosian-code"),
        "Re-derived from the approved Doc_04 SS3.7 (G5), tested after the two Tensional gravities "
        "per Doc_04's own stated ordering (T1 is G5's own directly-dependent internal qualification "
        "and reads most clearly once T1 is already on the record). relations[] carries the "
        "gravity<->gravity edges (G1, G2, G3, G4, T1, D-A) and gravity<->force edges (2A-1, 3A-1, "
        "3A-2) named above.",
    )

    emit_gravity(
        DA, "Circumcellion / *Agonistici* Character and Scale "
            "[SUPPORTING, scope-qualified -- Numidian regional sub-ecology only]",
        "supporting",
        "Doc_04 SS3.5: SUPPORTING, scope-qualified to the Numidian regional sub-ecology -- "
        "confirmed only there, NOT confirmed ecology-wide. Repetition: PASS on recurrence, with a "
        "caveat -- recurs in Optatus, Augustine, Boyd's corroborating history, and imperial "
        "legislation, but all evidentiary weight beyond bare existence and self-designation is "
        "hostile-mediated; even the agonistici self-designation term itself reaches this record "
        "only through Augustine's own report (Doc_03's own sharpened finding M2). Dependency: FAILS "
        "ecology-wide; PARTIAL PASS regionally -- G1/G2/G3/G4 do not structurally depend on this "
        "phenomenon for their own operation at the world level; confined to Numidia specifically, "
        "the Maximianist suppression's own reported Circumcellion involvement does trace through "
        "this same channel, though still hostile-mediated rather than independently confirmed. "
        "Formation: FAILS ecology-wide; PASSES regionally -- Doc_01 SS2 names Numidia specifically "
        "as this group's origin and associated region; nothing extends that formative reach to "
        "Carthage, Cirta, or Hippo. Explanatory: FAILS ecology-wide; PARTIAL PASS regionally -- "
        "explains some specific imperial legislative attention (CTh 16.5.52) and some Maximianist-"
        "affair detail, both narrowly regional or episode-specific. Persistence: FAILS for ecology-"
        "wide claims; PASSES for the Numidian sub-ecology specifically. Interaction: PASS -- "
        "interacts with G5 (the direct target of specific imperial legislation) and with T2 "
        "(reported involvement in the Maximianist suppression). CONFIDENCE/GRAVITY CROSS-CHECK -- "
        "DIVERGENT ACROSS THREE, NOT TWO, EVIDENTIARY TIERS, the sharpest such divergence in Doc_04: "
        "bare existence is Documented on independent imperial legislative attestation, directly "
        "confirmed against the law's own text (CTh 16.5.52, vendored 2026-09-07); the agonistici "
        "self-designation term itself reaches this record only through Augustine's own report -- "
        "reliable reportage, but not evidentially on par with the genuinely independent existence "
        "claim; character, scale, and typical conduct are at most Dominant Modern Reconstruction "
        "(Shaw's corrective reading), and Doc_04 does not adopt Frend's fuller acceptance of the "
        "hostile portrait as settled (Doc_03 SS4's own CT contest). A candidate this evidentially "
        "divided should not be classified Primary or ecology-wide Supporting regardless of how "
        "vividly the hostile sources describe it -- exactly the discipline this cross-check exists "
        "to enforce. CROSS-VOICE TEST (Doc_04 SS5): the one candidate that most clearly FAILS a "
        "strict cross-voice standard for anything beyond bare existence and self-designation -- no "
        "Donatist-voiced or non-mediated text corroborates the group's character, scale, or typical "
        "conduct; this is precisely the \"artificially confirmed\" risk the Cross-Voice Test exists "
        "to catch, and it is the direct evidentiary basis for not classifying this candidate as an "
        "ecology-wide gravity. INTERACTION MATRIX (Doc_04 SS6): narrow R with G5 (the direct object "
        "of CTh 16.5.52, itself part of G5's own evidentiary base) and narrow R with T2 (the "
        "Maximianist suppression's own reported, hostile-mediated Circumcellion involvement, not "
        "treated as independently confirming this candidate's own character). No clean forces-"
        "connection is assertable beyond what the hostile record itself supplies, which Doc_04 does "
        "not treat as settled. FORCES-CONNECTION (Doc_04 SS3.5, Doc_08 SS5): the direct object of "
        "2A-1 (the imperial legislation naming the group by name); tied to 2B-4 (the Maximianist "
        "suppression's own reported Circumcellion involvement).",
        [
            "Codex Theodosianus 16.5.52, a distinct silver fine set for the group by name -- "
            "independently attested existence outside hostile polemic",
            "the self-designation term \"agonistici\" itself, reaching this record only through "
            "Augustine's own report, its specific source passage in Augustine's corpus unidentified",
        ],
        conf("B", "verified-via-authority", "contested", "Dominant Modern Reconstruction",
             "This gravity's own confidence genuinely splits across three tiers, not one, and this "
             "record carries the most conservative applicable tier (Dominant Modern Reconstruction) "
             "as its own top-line rating rather than smoothing the split into a single number: bare "
             "existence is Documented (independent imperial legislative attestation, CTh 16.5.52); "
             "the agonistici self-designation term is reliable-but-Augustine-reported, not "
             "independently attested; character, scale, and typical conduct are at most Dominant "
             "Modern Reconstruction on Shaw's corrective reading against Frend's older, fuller "
             "acceptance of the hostile portrait (Doc_04 SS3.5, the sharpest Confidence/Gravity "
             "Cross-Check divergence in that document)."),
        src("don.source.codex-theodosianus-book-16",
            "don.source.boyd-ecclesiastical-edicts-theodosian-code",
            "don.source.optatus-against-donatists"),
        "Re-derived from the approved Doc_04 SS3.5 (D-A). This gravity was NOT named in this "
        "step's own launch brief's list of 'everything built so far' -- confirmed directly against "
        "Doc_04 SS1, SS3.5, SS4 as a genuine, classified (Supporting, scope-qualified) gravity, and "
        "against Doc_08 SS5's own inverted table, which carries it alongside G1-G5/T1/T2 as one of "
        "'all eight of this world's own classified gravities' (see this script's own docstring). "
        "relations[] carries the gravity<->gravity edges (G5, T2) and gravity<->force edges (2A-1, "
        "2B-4) named above.",
    )

    emit_gravity(
        T1, "Principled Refusal vs. Pragmatic Recourse to Imperial Power [TENSIONAL]",
        "tensional",
        "Doc_04 SS3.6: TENSIONAL. Two genuinely distinct poles with real institutional separation: "
        "(a) the movement's own ideological stance that the state has no standing to adjudicate who "
        "the true church is, voiced directly in Donatus's own reported retort, \"Quid est imperatori "
        "cum ecclesia?\" (independently re-verified against Optatus, Against the Donatists, Book "
        "III); (b) the movement's own repeated, documented turns to that same imperial machinery for "
        "its own advantage at three specific, named points across the window: the 313 petition to "
        "Constantine via Anulinus's relatio; the 361 petition to Julian for restoration of "
        "confiscated basilicas; the 390s invocation of existing imperial and proconsular anti-"
        "heretical legislation against its own Maximianist dissidents (all three named in Doc_01 "
        "SS5). Institutional separation is real: three distinct, documented acts at three distinct "
        "moments, not an abstract inconsistency. Tests: Repetition PASS (three separate instances); "
        "Persistence PASS (spans the whole window, 313 to the 390s); Interaction PASS (directly "
        "qualifies G5). Confidence: each of the three instances is independently Documented on its "
        "own historical terms (Anulinus's relatio is part of Optatus's own vendored Appendix of "
        "Documents; the Maximianist-era legal invocation is corroborated in Augustine's own primary "
        "text). The characterization of the tension as \"principled refusal against pragmatic "
        "exception,\" rather than simple incoherence, is Doc_04's own synthesis of Doc_01 SS5's "
        "language (\"the pattern remains refusal-under-pressure on balance... not an absolute "
        "refusal at every point\") -- a defensible reading, not itself independently attested as the "
        "Donatists' own self-description of the tension. FORCES-CONNECTION (Doc_04 SS3.6): spans "
        "Cells 1B through 2B rather than sitting in a single cell -- the 313 Anulinus relatio falls "
        "at the same founding-dispute moment as Cell 1B's own rigorist rupture; the 361 Julian "
        "petition and the 390s invocation both belong to the sustained ongoing period, Cells 2A "
        "(external, oscillating imperial policy) and 2B (internal, the Maximianist fracture). That "
        "this tension's own forces-connection spans two periods rather than sitting in one is itself "
        "part of what makes it a genuine Tensional gravity, not a single-episode inconsistency "
        "(confirmed rather than redecided by Doc_08 SS5: \"the clearest case in this document of a "
        "gravity whose own forces-connection genuinely spans multiple cells\"). INTERACTION MATRIX "
        "(Doc_04 SS6): R with G5 (the same evidentiary base viewed from two angles -- T1 is G5's own "
        "internal qualification, named separately because it meets the Tensional-gravity bar in its "
        "own right, not merely a caveat folded into G5's prose). **NO DEMONSTRATED RELATIONSHIP WITH "
        "T2** -- Doc_04 SS6 states this explicitly: \"These two tensions operate on different axes "
        "(external state relations versus internal disciplinary consistency) and no evidence in this "
        "world's record connects them directly; naming this absence explicitly is itself a finding, "
        "not an oversight.\" This absence is named here, in this record's own prose, precisely "
        "because relations[] has no typed way to assert a checked non-relationship -- an omitted "
        "edge and an examined absence would otherwise read identically.",
        [
            "the 313 petition to Constantine, forwarded through the governor Anulinus's own relatio "
            "(Optatus, Appendix of Documents)",
            "the 361 petition to Julian for restoration of confiscated basilicas",
            "the 390s invocation of existing imperial and proconsular anti-heretical legislation "
            "against the movement's own Maximianist dissidents",
        ],
        conf("A", "verified-via-authority", "load-bearing", "Documented",
             "Each of the three named instances (313, 361, the 390s) is independently Documented on "
             "its own historical terms (Doc_04 SS3.6); the characterization of the tension as "
             "'principled refusal against pragmatic exception,' rather than simple incoherence, is "
             "Doc_04's own synthesis of Doc_01 SS5's language, not itself independently attested as "
             "the Donatists' own self-description of the tension -- this divergence is named, not "
             "smoothed over."),
        src("don.source.optatus-against-donatists",
            "don.source.optatus-appendix-of-documents",
            "don.source.augustine-answer-to-letters-of-petilian"),
        "Re-derived from the approved Doc_04 SS3.6 (T1), tested surfacing G5's own Persistence per "
        "Doc_04 SS1's own generation note. relations[] carries the gravity<->gravity edge (G5) and "
        "gravity<->force edges (1B-2, 2A-1, 2B-4) named above. The explicit Doc_04 SS6 finding of "
        "NO demonstrated relationship with T2 is named in this record's own description and body "
        "text, not encoded as a relations[] entry -- see this script's own docstring.",
    )

    emit_gravity(
        T2, "Purity-Rigor vs. Institutional Reception (the Maximianist precedent) [TENSIONAL]",
        "tensional",
        "Doc_04 SS3.6: TENSIONAL. Two genuinely distinct poles with real institutional separation: "
        "(a) the stated, absolute logic that schismatic or invalidly-ordained clergy require "
        "rebaptism and reordination (G1/G2); (b) the mainstream Donatist party's own actual practice "
        "toward the Maximianist clergy on their return -- reception into office and communion "
        "WITHOUT repeating either ordination or baptism, a fact Augustine directly and repeatedly "
        "quotes from primary Donatist-adjacent material and turns into his single central argument "
        "against the Donatists' own rebaptism logic (Doc_02 SS1, verified against On Baptism and "
        "Answer to the Letters of Petilian). Institutional separation is real: a specific, named, "
        "historically bounded episode (the 393 Maximianist schism and its 394 Bagai condemnation and "
        "reception) with its own documentary record (the Bagai and Cebarsussi sentences), not an "
        "abstract inconsistency. Tests: Repetition PASS; Dependency PASS (G1's own internal "
        "coherence is what this tension specifically tests); Interaction PASS (directly reshapes "
        "G1). Confidence: Documented -- the most rigorously and repeatedly directly-quoted internal "
        "tension in this world's entire vendored corpus (Registry rows 3, 4, 47). FORCES-CONNECTION "
        "(Doc_04 SS3.6): Cell 2B -- Doc_01 SS5's own six-cell sketch names the Maximianist fracture "
        "(393-398) there explicitly, as an internal-ongoing pressure internal to G4's own conciliar "
        "machinery, not one imposed by any external force. Doc_08 SS5 confirms this is this "
        "gravity's own single connected force (2B-4), the narrowest connection count of any "
        "classified gravity in either document -- Doc_08 SS9 Open Items item 2 is explicit that "
        "this is not itself a confidence-divergence signal (unlike D-A's own scope-qualification): "
        "T2 is a tightly-scoped, single-episode Tensional gravity whose entire evidentiary base is "
        "the Maximianist affair, so a single connected force is exactly what its own narrow scope "
        "predicts, not a gap. INTERACTION MATRIX (Doc_04 SS6): X (reshaping) with G1 (the "
        "Maximianist reception-without-reordination precedent directly reshapes G1's own internal "
        "consistency; Augustine turns this exact reshaping into his central argument), G2 (as with "
        "G1, directly tested and complicated), and G4 (an event internal to this hierarchy's own "
        "conciliar machinery, which could not exist without G4's own institutional complexity to "
        "fracture within); narrow R with D-A (the Maximianist suppression's own reported Circumcellion "
        "involvement, itself hostile-mediated and not treated as independently confirming D-A's own "
        "character). **NO DEMONSTRATED RELATIONSHIP WITH T1** -- Doc_04 SS6 states this explicitly, "
        "and it is named here for the identical reason stated in T1's own record: these two tensions "
        "operate on different axes (external state relations versus internal disciplinary "
        "consistency) and no evidence in this world's record connects them directly; naming this "
        "absence is itself a finding, not an oversight, and is not encoded as a relations[] entry "
        "for the same reason T1's own record states.",
        [
            "the mainstream Donatist party's own council at Bagai (394) receiving the Maximianist "
            "clergy back without repeating either ordination or baptism",
            "Augustine, quoting the Cebarsussi and Bagai sentences directly, turning the reception "
            "into his single central argument against Donatist rebaptism logic",
        ],
        conf("A", "verified-via-authority", "load-bearing", "Documented",
             "Documented -- the most rigorously and repeatedly directly-quoted internal tension in "
             "this world's entire vendored corpus (Registry rows 3, 4, 47; Doc_04 SS3.6), resting on "
             "no single voice or thin evidence stream."),
        src("don.source.augustine-on-baptism-against-donatists",
            "don.source.augustine-answer-to-letters-of-petilian",
            "don.source.augustine-letter-51-to-crispinus"),
        "Re-derived from the approved Doc_04 SS3.6 (T2), tested surfacing G1's own internal "
        "consistency per Doc_04 SS1's own generation note. relations[] carries the gravity<->gravity "
        "edges (G1, G2, G4, D-A) and the gravity<->force edge (2B-4) named above. The explicit Doc_04 "
        "SS6 finding of NO demonstrated relationship with T1 is named in this record's own "
        "description and body text, not encoded as a relations[] entry -- see this script's own "
        "docstring and don.gravity.principled-refusal-vs-pragmatic-recourse's own matching note.",
    )


# ===========================================================================
# FORCES (13) -- Doc_08 SS3, one per force identified across the six-cell
# matrix. matrix_cell copied from each force's own cell heading; kind
# mechanically follows the cell (1A/1B -> initiating, 2A/2B -> ongoing,
# 3A/3B -> ending).
# ===========================================================================

def build_forces() -> None:
    emit_force(
        F1A1, "The Diocletianic Persecution (303-305) and the *traditio* Demand",
        "initiating", "1A",
        "Doc_08 Cell 1A, Force 1A-1. LAYER 1 -- HISTORICAL EVENT: the general persecution of "
        "Christians under Diocletian and his colleagues (303-305) included a specific demand that "
        "clergy surrender scripture and sacred vessels to the persecuting authorities for "
        "destruction. Documented -- attested across Doc_01's own founding-boundary reasoning and "
        "corroborated by the specific traditio accusations Optatus's own Appendix of Documents "
        "preserves (the Acta Purgationis Felicis, 314; Doc_02 SS1). LAYER 2 -- WORLD'S OWN "
        "EXPERIENCE: the persecutor did not merely ask for property; he asked for the scriptures "
        "themselves, and what a minister did in that moment was not incidental to his own standing "
        "afterward. A hand that gave up what it was charged to guard cannot be trusted, later, to "
        "give what it claims to give -- this is not a judgment reached after the fact but the "
        "conviction this world's own founders held to be simply true of what had happened. LAYER 3 "
        "-- FORMATION IMPACT: this force is the deep root of both G1 (Ministerial Purity) and G3 "
        "(Martyr-Cult Identity) -- it produces the traditor accusation G1's whole doctrine turns on, "
        "and establishes the pattern of persecution-as-formative-test the later, better-attested "
        "Macarian repression (Force 2A-2) repeats and intensifies. Without this force, this world's "
        "own central sacramental-validity question would have no occasion to arise. CROSS-CELL "
        "CONNECTION (Doc_08 Section 4, Connection 1): -> Force 2A-2 (Macarian repression) -- the "
        "earlier, empire-wide persecution establishes the pattern the later, specifically Macarian "
        "repression repeats and intensifies; both feed the same martyr-cult formation (G3), the "
        "second at far greater documented intensity than the first.",
        [
            "the specific demand that clergy surrender scripture and sacred vessels for destruction "
            "(303-305)",
            "the Acta Purgationis Felicis (314), the formal proceeding that traces the traditio "
            "accusation back to this same persecution's own demand",
        ],
        conf("A", "verified-via-authority", "load-bearing", "Documented",
             "Attested across Doc_01's own founding-boundary reasoning and corroborated by the "
             "specific traditio accusations Optatus's own Appendix of Documents preserves (Doc_08, "
             "Force 1A-1, Layer 1); no divergence flagged for this force's own bare occurrence."),
        src("don.source.optatus-appendix-of-documents"),
        "Re-derived from the approved Doc_08 Force 1A-1 (Cell 1A, Initiating/External). relations[] "
        "carries the gravity<->force edge (G3) and the force<->force edge (2A-2, Connection 1) "
        "named above.",
    )

    emit_force(
        F1B1, "The Cyprianic Rigorist Inheritance",
        "initiating", "1B",
        "Doc_08 Cell 1B, Force 1B-1. LAYER 1 -- HISTORICAL EVENT: Cyprian of Carthage's third-"
        "century rebaptism theology -- that baptism outside the true church is no baptism at all, a "
        "position he held against Pope Stephen -- was this world's own direct doctrinal and "
        "institutional inheritance, not an invention at 311/312 (Doc_01 SS6). Documented as this "
        "world's own founding logic; Cyprian's antecedent status (neither a Donatist voice nor a "
        "neutral outside source, but the authority both sides argued FROM) is independently measured "
        "in the vendored corpus map, which records Augustine's own On Baptism naming Cyprian 306 "
        "times (Doc_02 SS1). LAYER 2 -- WORLD'S OWN EXPERIENCE: this is not a new teaching this "
        "world invented to justify itself. It is the same conviction the whole North African church "
        "already held -- that a baptism given outside the one true church washes nothing -- "
        "sharpened now, under real pressure, to answer a question Cyprian himself never had to ask: "
        "what happens when the minister giving the baptism has himself surrendered the scriptures. "
        "LAYER 3 -- FORMATION IMPACT: this force grounds both G1 and G2 directly -- the doctrine and "
        "its enacted rite are a sharpening of an inherited position, not a departure from one, which "
        "is why this world's own founders could hold their position as fidelity rather than novelty. "
        "No cross-cell connection is named for this force in Doc_08 Section 4.",
        [
            "Cyprian of Carthage's own rebaptism theology against Pope Stephen, applied now to "
            "clergy suspected of traditio",
            "Augustine's On Baptism naming Cyprian 306 times -- an independently measured citation-"
            "frequency finding, not this document's own impression",
        ],
        conf("A", "verified-via-authority", "load-bearing", "Documented",
             "Documented as this world's own founding logic; Cyprian's antecedent status is "
             "independently measured in the vendored corpus map's own citation-frequency finding "
             "(306 occurrences), not asserted from impression (Doc_08, Force 1B-1, Layer 1)."),
        src("don.source.cyprian-on-the-unity-of-the-church",
            "don.source.cyprian-epistles",
            "don.source.augustine-on-baptism-against-donatists"),
        "Re-derived from the approved Doc_08 Force 1B-1 (Cell 1B, Initiating/Internal). relations[] "
        "carries the gravity<->force edges (G1, G2) named above.",
    )

    emit_force(
        F1B2, "The Felix of Aptungi *Traditio* Accusation and the Rival Consecration of Majorinus "
              "(311/312)",
        "initiating", "1B",
        "Doc_08 Cell 1B, Force 1B-2. LAYER 1 -- HISTORICAL EVENT: Caecilian was consecrated bishop "
        "of Carthage by Felix of Aptungi, who was accused of being a traditor; the rigorist party "
        "responded with the rival consecration of Majorinus (311/312), succeeded from c. 313 by "
        "Donatus, from whom the movement's name derives. Documented as the schism's own specific "
        "founding-rupture event (Doc_01 SS2). Optatus's own petition text shows this world's earliest "
        "institutional act -- its own appeal to Constantine through the governor Anulinus, "
        "forwarding the movement's own petition -- arising at this identical moment, not decades "
        "after it. LAYER 2 -- WORLD'S OWN EXPERIENCE: a man consecrated by a hand that had "
        "surrendered the scriptures cannot be a true bishop, and a communion that accepts him has, "
        "by that acceptance, ceased to be trustworthy on the one question that matters most. The "
        "rival consecration was not a power grab; it was the only response that took the traditio "
        "accusation seriously. LAYER 3 -- FORMATION IMPACT: this force is the specific institutional "
        "trigger for G4 -- a traditor-tainted line had to be replaced with a clean one, and this "
        "consecration is where that replacement begins. It is also the founding moment of T1's own "
        "earliest instance -- the movement turning to the same imperial machinery it would spend the "
        "rest of its history refusing to recognize as having standing over it, present at the very "
        "founding of the refusal itself. CROSS-CELL CONNECTIONS (Doc_08 Section 4): -> Force 2B-1 "
        "(Connection 2) -- the founding rupture produces the ongoing enacted rite: rebaptism as a "
        "repeated, individually-experienced practice is the institutional life of the traditio "
        "accusation, sustained across the whole window rather than a single founding act. -> Force "
        "2A-1 (Connection 3) -- this world's own earliest turn to state adjudication (the 313 "
        "Anulinus relatio) arises at the identical founding moment as the schism itself, not decades "
        "into it, establishing from the very start the pattern of occasional pragmatic recourse to "
        "imperial power Force 2A-1 documents across the whole window and T1 tests as its own "
        "Tensional gravity.",
        [
            "Felix of Aptungi's traditio accusation, later overturned at the Acta Purgationis "
            "Felicis (314) under a forger's own confession",
            "the rival consecration of Majorinus (311/312), succeeded c. 313 by Donatus, from whom "
            "the movement's name derives",
            "the 313 petition to Constantine, forwarded through the governor Anulinus's own relatio",
        ],
        conf("A", "verified-via-authority", "load-bearing", "Documented",
             "Documented as the schism's own specific founding-rupture event (Doc_01 SS2); Optatus's "
             "own petition text independently shows the 313 Anulinus relatio arising at this same "
             "moment, not decades after it (Doc_08, Force 1B-2, Layer 1)."),
        src("don.source.optatus-against-donatists",
            "don.source.optatus-appendix-of-documents"),
        "Re-derived from the approved Doc_08 Force 1B-2 (Cell 1B, Initiating/Internal). relations[] "
        "carries the gravity<->force edges (G1, G4, T1) and the force<->force edges (2B-1, "
        "Connection 2; 2A-1, Connection 3) named above.",
    )

    emit_force(
        F2A1, "Oscillating Imperial Religious Policy",
        "ongoing", "2A",
        "Doc_08 Cell 2A, Force 2A-1. LAYER 1 -- HISTORICAL EVENT: imperial religious policy toward "
        "this world oscillated across its whole window: the Council of Rome (313, under Pope "
        "Miltiades, convened at Constantine's own order) and the Council of Arles (314) both ruled "
        "against the Donatist party; Constantine's own coercive measures (316-321) failed in "
        "practice and were reversed; Julian granted toleration in 361, including restoration of "
        "confiscated basilicas; sustained legal suppression resumed from the 405 Edict of Unity "
        "through the 411 Conference of Carthage and its aftermath. Documented (Doc_01 SS2). LAYER 2 "
        "-- WORLD'S OWN EXPERIENCE: the emperor's own favor swung back and forth across this whole "
        "span -- coercion, then toleration, then suppression again -- and this world held itself "
        "steady through all of it on one conviction: what has the emperor to do with the church? "
        "The state's own recognition, or its withdrawal of recognition, never settled who the true "
        "church was; it was simply a condition this world had to live formed inside, whichever way "
        "it turned. LAYER 3 -- FORMATION IMPACT: this force sustains G5 throughout the window and is "
        "the direct external pressure T1 tests -- this world's own three qualifying turns to "
        "imperial machinery (313, 361, the 390s) each occur at precisely the moments this "
        "oscillation briefly offered something to gain. It is also the specific target of G2's own "
        "enacted rite: successive imperial edicts name rebaptism directly as a legal offense, and "
        "D-A is likewise the direct object of specific imperial legislation (Codex Theodosianus "
        "16.5.52). CROSS-CELL CONNECTIONS (Doc_08 Section 4): <- Force 1B-2 (Connection 3) -- this "
        "world's own earliest turn to state adjudication arises at the founding-dispute moment "
        "itself, establishing the pattern this force sustains across the whole window. -> Force "
        "2B-4 (Connection 5) -- the mainstream party's own invocation of existing imperial and "
        "proconsular anti-heretical legislation against its own Maximianist dissidents in the 390s "
        "is this world's own internal use of the identical external legal machinery this force names "
        "across the whole window -- the same oscillating policy operating, here, as an instrument "
        "this world's own actors reach for against their own internal rivals.",
        [
            "the Council of Rome (313) and the Council of Arles (314), both ruling against the "
            "Donatist party",
            "Julian's 361 toleration edict, restoring confiscated basilicas",
            "the 405 Edict of Unity, resuming sustained legal suppression through the 411 Conference",
        ],
        conf("A", "verified-via-authority", "load-bearing", "Documented",
             "Documented (Doc_01 SS2; Doc_08, Force 2A-1, Layer 1); the oscillation itself -- "
             "coercion, then toleration, then suppression again -- is stated as fact throughout the "
             "vendored corpus, not this document's own reconstruction of an underlying trend."),
        src("don.source.codex-theodosianus-book-16",
            "don.source.boyd-ecclesiastical-edicts-theodosian-code"),
        "Re-derived from the approved Doc_08 Force 2A-1 (Cell 2A, Ongoing/External). relations[] "
        "carries the gravity<->force edges (G2, G5, D-A, T1) and the force<->force edges (1B-2, "
        "Connection 3; 2B-4, Connection 5) named above.",
    )

    emit_force(
        F2A2, "The Macarian Repression (347-348)",
        "ongoing", "2A",
        "Doc_08 Cell 2A, Force 2A-2. LAYER 1 -- HISTORICAL EVENT: imperial commissioners Paul and "
        "Macarius enforced unification on this world by direct, sometimes lethal coercion (347-348). "
        "Documented, corroborated in this world's own vendored voice: the Passio Marculi and "
        "Macrobius's own letter to the Carthage congregation on the deaths of Isaac and Maximianus "
        "(Doc_01 SS5; Doc_02 SS4). LAYER 2 -- WORLD'S OWN EXPERIENCE: this was not persecution "
        "suffered alongside the rival, as the Diocletianic terror had been; this was suffering "
        "inflicted specifically BY that same rival's own instigation, through the emperor's own "
        "commissioners. The dead this repression produced are not remembered as casualties of a "
        "general disaster; they are remembered as this world's own martyrs, proved true by what the "
        "rival's own favored power did to them. LAYER 3 -- FORMATION IMPACT: this is the direct "
        "trigger for the two best-attested Passiones (G3's own core textual evidence) and "
        "intensifies rather than merely tests this world's own martyr-cult identity -- each new "
        "persecution episode generates new commemorative text production, a pattern this document "
        "can trace directly (this repression produces two texts in close succession; the earlier, "
        "less-attested persecution under Leontius and Ursacius produces the commemorative sermon). "
        "CROSS-CELL CONNECTIONS (Doc_08 Section 4): <- Force 1A-1 (Connection 1) -- the earlier, "
        "empire-wide persecution establishes the pattern this later, specifically Macarian "
        "repression repeats and intensifies. -> Force 2B-3 (Connection 4) -- the repression is the "
        "direct trigger for new commemorative text production: the two best-attested Passiones "
        "follow it in close succession, converting an acute persecution episode into an ongoing "
        "liturgical practice.",
        [
            "the deaths of Isaac and Maximianus, recorded in Macrobius's own letter to the Carthage "
            "congregation (don.story.macrobius-letter-isaac-maximianus)",
            "Marculus's death at the cliff of Novapetra (don.story.passio-marculi)",
        ],
        conf("A", "verified-via-authority", "load-bearing", "Documented",
             "Documented, and corroborated in this world's own vendored voice specifically -- the "
             "Passio Marculi and Macrobius's own letter, not only the hostile Optatus/Augustine "
             "record (Doc_01 SS5; Doc_02 SS4; Doc_08, Force 2A-2, Layer 1)."),
        src("don.source.passio-marculi",
            "don.source.passio-isaac-et-maximiani"),
        "Re-derived from the approved Doc_08 Force 2A-2 (Cell 2A, Ongoing/External). relations[] "
        "carries the gravity<->force edge (G3) and the force<->force edges (1A-1, Connection 1; "
        "2B-3, Connection 4) named above.",
    )

    emit_force(
        F2B1, "Sustained Purity Doctrine and Rebaptism Practice as Founding Logic",
        "ongoing", "2B",
        "Doc_08 Cell 2B, Force 2B-1. LAYER 1 -- HISTORICAL EVENT: the purity doctrine (G1) and its "
        "enacted rite (G2) operated as this world's own established, contested institutional pattern "
        "from 311/312 through the 411 Conference. Documented, attested both in Augustine's own "
        "primary text (not merely characterized) and in Petilian's own quoted argument (Doc_04 "
        "SS3.1, SS3.2). LAYER 2 -- WORLD'S OWN EXPERIENCE: to belong here was to have been washed "
        "again, deliberately, by a hand of unbroken standing -- not a repetition of something "
        "already valid but the first true baptism a person ever received. This was not a doctrine "
        "held quietly; it was lived, daily, in the concrete choice of which minister's hands to "
        "receive from. LAYER 3 -- FORMATION IMPACT: this is this world's own central, continuously "
        "operating internal force -- it sustains G1 and G2 across the entire window and is what the "
        "Maximianist affair (Force 2B-4) specifically tests, without fracturing. CROSS-CELL "
        "CONNECTION (Doc_08 Section 4, Connection 2): <- Force 1B-2 -- the founding rupture produces "
        "the ongoing enacted rite: rebaptism as a repeated, individually-experienced practice is the "
        "institutional life of the traditio accusation, sustained across the whole window rather "
        "than a single founding act.",
        [
            "the concrete, daily, individually-experienced choice of which minister's hands to "
            "receive rebaptism from",
        ],
        conf("A", "verified-via-authority", "load-bearing", "Documented",
             "Documented, attested both in Augustine's own primary text (not merely characterized) "
             "and in Petilian's own quoted argument (Doc_08, Force 2B-1, Layer 1, citing Doc_04 "
             "SS3.1, SS3.2)."),
        src("don.source.augustine-on-baptism-against-donatists",
            "don.source.petilian-of-constantina-letters-quoted"),
        "Re-derived from the approved Doc_08 Force 2B-1 (Cell 2B, Ongoing/Internal). relations[] "
        "carries the gravity<->force edges (G1, G2) and the force<->force edge (1B-2, Connection 2) "
        "named above.",
    )

    emit_force(
        F2B2, "Transmission -- Survival Through the Hostile Party's Own Manuscript Tradition",
        "ongoing", "2B",
        "Doc_08 Cell 2B, Force 2B-2 -- the Transmission dimension this cell is required to address "
        "explicitly (Doc_08 SS9 completion certification), synthesized fully at Doc_08 Section 6. "
        "LAYER 1 -- HISTORICAL EVENT: nearly all textual material currently vendored for this world "
        "passed through Catholic hands (Optatus, Augustine) before reaching this document -- the "
        "eventually-victorious party's own literature, preserved by institutions with every reason "
        "to preserve it. Documented, and named as this world's own central evidentiary problem "
        "throughout Doc_01 and Doc_02 (Doc_01 SS5, Cell 2B; Doc_02 SS1). LAYER 2 -- WORLD'S OWN "
        "EXPERIENCE: this world's own record does not show its own actors reflecting on this "
        "condition directly -- no surviving Donatist chronicle of Arles, no surviving Donatist "
        "administrative account of the Macarian repression exists, only the martyr-cult narrative "
        "response to it. This is a genuine absence, not a filled silence: whatever this world "
        "understood itself to be doing when its own texts were produced, its own understanding of "
        "how those texts would or would not survive is not recoverable from what remains. LAYER 3 -- "
        "FORMATION IMPACT: this transmission pattern is the specific mechanism behind this world's "
        "own Author Gravity concentration -- Petilian's own quoted words survive only because "
        "Augustine needed them in front of a reader to refute them, a preservation mechanism "
        "selecting for refutability, not fairness. It is what makes the small independently-"
        "surviving remainder (Tyconius's Liber Regularum, the martyr texts, the epigraphy) this "
        "document's own single most valuable evidentiary category, connected fully at Doc_08 "
        "Section 6. NOT CONNECTED TO A SPECIFIC GRAVITY, DISCLOSED RATHER THAN OMITTED: Doc_08's own "
        "Force Index (Section 9) carries \"--\" for this force's own Connected Gravities column, and "
        "Section 5 states plainly that this force and its own ending-phase counterpart (3B-2) \"are "
        "the required transmission entries, which this document treats as cross-cutting rather than "
        "gravity-specific\" -- this record's own relations[] therefore carries no gravity<->force "
        "edge for this force, matching that disclosed absence exactly, not a gap this script failed "
        "to notice. CROSS-CELL CONNECTION (Doc_08 Section 4, Connection 8): -> Force 3B-2 -- the "
        "pattern established during the ongoing phase (survival through the hostile party's own "
        "quotation and refutation) becomes definitive and irreversible once the Caecilianist "
        "party's institutional victory is complete: the same mechanism operating throughout the "
        "window is what locks in, at the ending, exactly which small remainder of this world's own "
        "voice survives independently of it.",
        [
            "Petilian's own words, surviving only because Augustine needed them in front of a "
            "reader in order to refute them, clause by clause",
            "the absence of any surviving Donatist chronicle of Arles or Donatist administrative "
            "account of the Macarian repression",
        ],
        conf("A", "verified-via-authority", "load-bearing", "Documented",
             "Documented, and named as this world's own central evidentiary problem throughout "
             "Doc_01 and Doc_02 (Doc_08, Force 2B-2, Layer 1), independently corroborated by the "
             "corpus map's own manuscript-tradition finding (Doc_02 SS6)."),
        src("don.source.augustine-answer-to-letters-of-petilian"),
        "Re-derived from the approved Doc_08 Force 2B-2 (Cell 2B, Ongoing/Internal; Transmission "
        "dimension). relations[] carries only the force<->force edge (3B-2, Connection 8) named "
        "above -- deliberately no gravity<->force edge, per Doc_08's own explicit 'cross-cutting, "
        "not gravity-specific' disposition for this force, named rather than silently applied.",
    )

    emit_force(
        F2B3, "Martyr-Cult and Confessor Memory Sustaining Identity",
        "ongoing", "2B",
        "Doc_08 Cell 2B, Force 2B-3. LAYER 1 -- HISTORICAL EVENT: the annual commemoration of "
        "martyrs at the grave, and the growing body of martyr texts this practice produced, operated "
        "as an ongoing, repeated formative practice throughout this world's active life. Documented "
        "(Doc_02 SS4; Doc_04 SS3.3). LAYER 2 -- WORLD'S OWN EXPERIENCE: to gather at a martyr's "
        "grave, on the day appointed, and hear the account read again is not to remember something "
        "finished. It is to be shown, again, what this world already believes itself to be -- the "
        "church that suffers, and goes on suffering, and is proved true by it. LAYER 3 -- FORMATION "
        "IMPACT: this force sustains G3 continuously and is the mechanism by which Force 2A-2's own "
        "acute persecution episode is converted into lasting formation -- a single repression event "
        "becomes a permanent liturgical fact through this ongoing practice. CROSS-CELL CONNECTION "
        "(Doc_08 Section 4, Connection 4): <- Force 2A-2 -- the repression is the direct trigger for "
        "new commemorative text production, converting an acute persecution episode into an ongoing "
        "liturgical practice.",
        [
            "the annual reading of the Passio Donati sermon, every twelfth of March, at the "
            "martyrs' own grave (\"in solemni et anniversaria commemoratione\")",
        ],
        conf("A", "verified-via-authority", "load-bearing", "Documented",
             "Documented (Doc_02 SS4; Doc_04 SS3.3; Doc_08, Force 2B-3, Layer 1) -- resting on the "
             "least Author-Gravity-encumbered evidentiary base of any force in this document, per "
             "Doc_08 Section 7's own Confidence Assessment."),
        src("don.source.passio-donati-sermon",
            "don.source.deo-laudes-acclamation-cil8"),
        "Re-derived from the approved Doc_08 Force 2B-3 (Cell 2B, Ongoing/Internal). relations[] "
        "carries the gravity<->force edge (G3) and the force<->force edge (2A-2, Connection 4) "
        "named above.",
    )

    emit_force(
        F2B4, "The Internal Maximianist Fracture (393-398)",
        "ongoing", "2B",
        "Doc_08 Cell 2B, Force 2B-4. LAYER 1 -- HISTORICAL EVENT: the deacon Maximian broke from "
        "the mainstream Donatist hierarchy in 393 over disciplinary and procedural grievances "
        "against Primian, bishop of Carthage; a council at Cebarsussi elected Maximian a rival "
        "primate; the mainstream party's own much larger council at Bagai (394) condemned the "
        "Maximianists and, over 394-398, suppressed them -- invoking existing imperial and "
        "proconsular anti-heretical legislation against its own dissidents, and receiving the "
        "Maximianist clergy back afterward without repeating either ordination or baptism. The "
        "affair's consequences remain live in Augustine's own writing as late as c. 405-406 and are "
        "pressed again at the 411 Conference. Documented, attested directly in Augustine's own "
        "quotation of the Cebarsussi and Bagai sentences (Doc_01 SS4; Doc_05 SS4) -- the longest and "
        "most detailed Layer 1 in Doc_08, matching its own status as this world's own most richly "
        "and directly attested internal episode (Doc_08 Section 8, Proportionality Principle). "
        "LAYER 2 -- WORLD'S OWN EXPERIENCE: this world's own councils judged its own dissidents by "
        "the same conciliar authority that governs everything else in this world's own institutional "
        "life -- and when those same councils received the Maximianist clergy back, they did not "
        "repeat the rebaptism this world otherwise insists on. This world's own record states this "
        "plainly, in the same texts that state the doctrine at its most absolute, and does not treat "
        "the two facts as canceling each other. LAYER 3 -- FORMATION IMPACT: this is the direct "
        "engine of T2 -- the most rigorously and repeatedly directly-quoted internal tension in this "
        "world's entire vendored corpus -- and reshapes, without fracturing, G1's own internal "
        "consistency. It also supplies T1's own third qualifying instance (the 390s invocation of "
        "imperial legislation against its own dissidents) and is the specific event Force 3A-1 (the "
        "411 Conference) presses again. CROSS-CELL CONNECTIONS (Doc_08 Section 4): <- Force 2A-1 "
        "(Connection 5) -- the mainstream party's own invocation of existing imperial and proconsular "
        "anti-heretical legislation against its own Maximianist dissidents in the 390s is this "
        "world's own internal use of the identical external legal machinery Force 2A-1 names across "
        "the whole window. -> Force 3A-1 (Connection 6) -- the fracture's own consequences remain "
        "live in Augustine's own writing as late as c. 405-406 and are pressed again, one final "
        "time, at the 411 Conference itself -- an internal-ongoing force whose resolution is not "
        "complete until the ending-external force's own verdict.",
        [
            "the council at Cebarsussi (393) electing Maximian a rival primate",
            "the council at Bagai (394), condemning the Maximianists and later receiving their "
            "clergy back without reordination or rebaptism",
            "Augustine's own direct quotation of the Cebarsussi and Bagai sentences, still live in "
            "his writing as late as c. 405-406",
        ],
        conf("A", "verified-via-authority", "load-bearing", "Documented",
             "Documented, attested directly in Augustine's own quotation of the Cebarsussi and "
             "Bagai sentences (Doc_01 SS4; Doc_05 SS4; Doc_08, Force 2B-4, Layer 1) -- the longest "
             "and most detailed Layer 1 treatment in Doc_08, proportional to its own status as this "
             "world's own most richly attested internal episode."),
        src("don.source.augustine-letter-51-to-crispinus",
            "don.source.augustine-on-baptism-against-donatists"),
        "Re-derived from the approved Doc_08 Force 2B-4 (Cell 2B, Ongoing/Internal). relations[] "
        "carries the gravity<->force edges (G1, G4, T1, T2, D-A) and the force<->force edges (2A-1, "
        "Connection 5; 3A-1, Connection 6) named above.",
    )

    emit_force(
        F3A1, "The 411 Conference of Carthage's Verdict and the Penal Legislation That Followed",
        "ending", "3A",
        "Doc_08 Cell 3A, Force 3A-1. LAYER 1 -- HISTORICAL EVENT: the imperially-convened 411 "
        "Conference of Carthage, Marcellinus presiding, seated 279 Donatist against 286 Catholic "
        "bishops (corrected 2026-09-09 from an earlier, unverified 284 figure; Doc_02 SS1) and ruled "
        "against the Donatist party; the verdict was followed by sustained penal legislation. "
        "Documented (Doc_01 SS2). Emeritus of Caesarea and the other Donatist bishops present are "
        "recorded, per the Gesta Collationis Carthaginiensis, speaking at length on their own side "
        "of the exchange, and that text itself is now vendored (Registry row 55, corrected "
        "2026-09-08), so their own words on the verdict itself are now directly readable in this "
        "world's own corpus, though not yet read into a specific claim by Doc_08. LAYER 2 -- "
        "WORLD'S OWN EXPERIENCE: this world's own record does not preserve a direct account of how "
        "its own participants received this specific verdict. What this world's own broader record "
        "does state is that a council's verdict, even one this large and formally convened, is not "
        "what settles who the true church is -- the same conviction this world has held throughout "
        "the window, applied here to its own sharpest test yet. LAYER 3 -- FORMATION IMPACT: this "
        "force presses G5 to its sharpest test and directly reshapes G4, which now bears the "
        "verdict's own legal-institutional consequences. It is also where Force 2B-4's own "
        "Maximianist consequences are pressed again, one last time, before the window closes. "
        "CROSS-CELL CONNECTIONS (Doc_08 Section 4): <- Force 2B-4 (Connection 6) -- the fracture's "
        "own consequences remain live as late as c. 405-406 and are pressed again, one final time, "
        "at the 411 Conference. -> Force 3B-1 (Connection 7, together with Force 3A-2) -- both "
        "ending-external forces compound rather than act independently: the Conference's own "
        "verdict and penal legislation press this world's institutional life for nearly three "
        "decades before the Vandal capture removes the enforcing power altogether -- the internal "
        "attrition Force 3B-1 documents is the cumulative effect of both, not either alone. OPEN "
        "ITEM NAMED, NOT SMOOTHED OVER (Doc_08 Section 5, 'Where Forces Analysis Surfaced Gaps'): "
        "this world's own Donatist-voiced account of receiving this verdict is now recoverable in "
        "principle (the Gesta is vendored) but has not yet been read into a specific claim -- a real, "
        "currently-open integration task, not resolved by this record.",
        [
            "279 Donatist against 286 Catholic bishops seated (corrected 2026-09-09 from an earlier, "
            "unverified 284 figure)",
            "Emeritus of Caesarea speaking at length on the Donatist side of the exchange "
            "(don.figure.emeritus, don.quote.emeritus-magno-argumento)",
        ],
        conf("A", "verified-via-authority", "load-bearing", "Documented",
             "Documented (Doc_01 SS2; Doc_08, Force 3A-1, Layer 1); the bishop count itself is a "
             "corrected figure (279/286, not the earlier unverified 284) named explicitly rather "
             "than silently updated."),
        src("don.source.gesta-collationis-carthaginiensis",
            "don.source.migne-pl11-collatio-carthaginiensis",
            "don.source.optatus-appendix-of-documents"),
        "Re-derived from the approved Doc_08 Force 3A-1 (Cell 3A, Ending/External). relations[] "
        "carries the gravity<->force edges (G4, G5) and the force<->force edges (2B-4, Connection 6; "
        "3B-1, Connection 7a) named above.",
    )

    emit_force(
        F3A2, "The Vandal Invasion (429) and Capture of Carthage (439)",
        "ending", "3A",
        "Doc_08 Cell 3A, Force 3A-2. LAYER 1 -- HISTORICAL EVENT: the Vandal invasion of Roman "
        "North Africa, begun in 429, culminated in the capture of Carthage in 439 -- \"the removal "
        "of the Roman-imperial, Catholic-aligned adjudicating power this world's entire refusal-of-"
        "imperial-legitimacy pattern is defined against,\" in Doc_01's own stated terms. Documented "
        "(Doc_01 SS2). LAYER 2 -- WORLD'S OWN EXPERIENCE: this world's own record does not preserve "
        "its own participants' interpretation of this ending -- the community's own account of what "
        "the Vandal conquest meant is not recoverable from surviving sources. LAYER 3 -- FORMATION "
        "IMPACT: this force, together with Force 3A-1's own verdict and penal legislation, is what "
        "Doc_04 SS3.7 names as \"the most direct forces-connection of any gravity in this document\" "
        "-- jointly, the two remove the specific power G5 is defined in refusal of, and their "
        "combined effect is what closes this world's own construction window. It does not end the "
        "underlying two-party contest, which the record shows continuing under different political "
        "conditions well past 439, into Gregory the Great's 590s correspondence -- a fact not "
        "treated as resolved by this force, only as marking where this world's own construction "
        "window itself ends. CROSS-CELL CONNECTION (Doc_08 Section 4, Connection 7, together with "
        "Force 3A-1): -> Force 3B-1 -- both ending-external forces compound rather than act "
        "independently: the internal attrition Force 3B-1 documents is the cumulative effect of "
        "both this force and Force 3A-1, not either alone. NO SPECIFIC DON.SOURCE.* GROUNDING NAMED, "
        "DISCLOSED RATHER THAN FORCED: neither Doc_04 nor Doc_08 cites a specific vendored Donatist-"
        "world primary source for the Vandal capture itself (a background historical fact this "
        "world's own construction-window boundary is defined against, per Doc_01 SS2, rather than a "
        "claim this world's own corpus directly documents) -- sources[] is left empty rather than "
        "attaching an unearned citation.",
        [
            "the Vandal capture of Carthage (439), the specific point Doc_01 SS2 names as this "
            "world's own construction-window close",
        ],
        conf("A", "verified-via-authority", "load-bearing", "Documented",
             "Documented (Doc_01 SS2; Doc_08, Force 3A-2, Layer 1); this world's own record does "
             "not preserve any participant interpretation of this ending, named directly at Layer 2 "
             "rather than an inference offered in its place."),
        [],
        "Re-derived from the approved Doc_08 Force 3A-2 (Cell 3A, Ending/External). relations[] "
        "carries the gravity<->force edges (G4, G5) and the force<->force edge (3B-1, Connection "
        "7b) named above. sources[] is deliberately empty -- see this record's own body text.",
    )

    emit_force(
        F3B1, "Institutional Attrition Under Sustained Legal Pressure",
        "ending", "3B",
        "Doc_08 Cell 3B, Force 3B-1. LAYER 1 -- HISTORICAL EVENT: this world's own institutional "
        "life underwent sustained attrition under legal pressure and property confiscation across "
        "the ending phase, though it was not extinguished within this world's own construction "
        "window; the movement's own later history, continuing past 439 under Vandal and then "
        "Byzantine rule, is attested only by the record falling silent, not by any surviving "
        "Donatist voice narrating its own decline (Doc_01 SS2, SS7 item 8; Doc_02 SS7). LAYER 2 -- "
        "WORLD'S OWN EXPERIENCE: this world's own record does not preserve a direct account of what "
        "this attrition felt like from inside. LAYER 3 -- FORMATION IMPACT: this force is what "
        "Doc_01 SS7 item 8 explicitly binds a future compilation to record honestly -- a real, "
        "later, more gradual decline, not smoothed into a sudden ending at 439. It is the specific "
        "reason this document's own confidence about G4's own institutional continuity ends "
        "precisely where the vendored record does, not where the movement itself actually ended. "
        "CROSS-CELL CONNECTION (Doc_08 Section 4, Connection 7): <- Force 3A-1 and Force 3A-2 -- "
        "both ending-external forces compound rather than act independently: the Conference's own "
        "verdict and penal legislation press this world's institutional life for nearly three "
        "decades before the Vandal capture removes the enforcing power altogether -- this force's "
        "own attrition is the cumulative effect of both, not either alone. TWO-TIER CONFIDENCE, "
        "NAMED EXPLICITLY (Doc_08 Section 7, Section 9 Open Items item 3): this is the one force in "
        "Doc_08 carrying two different confidence levels for two different claims about itself -- "
        "the bare fact of attrition under sustained legal pressure is Documented; the SPECIFIC SHAPE "
        "of that decline (its pace, its regional variation, its lived texture) is Inferential-Thin, "
        "since the vendored record itself falls silent before that specific shape can be traced. "
        "This record carries the more conservative, specific-shape tier (Inferential-Thin) as its "
        "own top-line rating, with the bare-occurrence Documented tier named in divergence_note "
        "rather than smoothed together. NO SPECIFIC DON.SOURCE.* GROUNDING NAMED, DISCLOSED RATHER "
        "THAN FORCED: this force's own evidentiary base is the ABSENCE of a specific record (the "
        "movement's own later history \"attested only by the record falling silent\"), not a "
        "citable vendored text -- sources[] is left empty rather than attaching an unearned "
        "citation to a claim about silence itself.",
        [
            "the movement's own later history, continuing past 439 under Vandal and then Byzantine "
            "rule, attested only by the vendored record falling silent",
        ],
        conf("A", "verified-via-authority", "load-bearing", "Inferential-Thin",
             "This force's own bare occurrence (institutional attrition under sustained legal "
             "pressure) is Documented; its SPECIFIC SHAPE (pace, regional variation, lived texture) "
             "is Inferential-Thin, since the vendored record falls silent before that shape can be "
             "traced -- Doc_08 Section 7 and Section 9 Open Items item 3 both name this as the one "
             "force in that document carrying two different confidence levels for two different "
             "claims about itself, and this record carries the more conservative, specific-shape "
             "tier as its own top-line rating rather than smoothing the two together."),
        [],
        "Re-derived from the approved Doc_08 Force 3B-1 (Cell 3B, Ending/Internal). relations[] "
        "carries the gravity<->force edge (G4) and the force<->force edges (3A-1, 3A-2, Connection "
        "7) named above. sources[] is deliberately empty -- see this record's own body text.",
    )

    emit_force(
        F3B2, "Transmission -- the Caecilianist Party's Own Institutional Victory Determines What "
              "Survives",
        "ending", "3B",
        "Doc_08 Cell 3B, Force 3B-2 -- the Transmission dimension this cell is required to address "
        "explicitly (Doc_08 SS9 completion certification), synthesized fully at Doc_08 Section 6. "
        "LAYER 1 -- HISTORICAL EVENT: the Caecilianist party's eventual institutional victory "
        "determined what got copied. Donatist literature survives almost entirely as quotation "
        "embedded inside its own refutations (Optatus, Augustine), with a small independently-"
        "surviving remainder -- Tyconius's Liber Regularum, the Passio Marculi, the Passio Isaac et "
        "Maximiani, the commemorative sermon -- and a material/epigraphic record (the Deo laudes "
        "acclamation) that survived largely because it was never textual to begin with. Documented "
        "(Doc_01 SS5, Cell 3B). LAYER 2 -- WORLD'S OWN EXPERIENCE: not recoverable from surviving "
        "sources -- this world's own participants left no account of what they understood "
        "themselves to be preserving as their own institutional position weakened, or of what they "
        "expected would or would not survive them. LAYER 3 -- FORMATION IMPACT: this is the single "
        "most consequential force shaping what this entire construction can and cannot know. G3's "
        "own textual survival IS substantially this world's own surviving voice -- precisely because "
        "the martyr texts and the epigraphy sit partly or wholly outside the manuscript channel this "
        "force otherwise controls. CROSS-CELL CONNECTION (Doc_08 Section 4, Connection 8): <- Force "
        "2B-2 -- the pattern established during the ongoing phase (survival through the hostile "
        "party's own quotation and refutation) becomes definitive and irreversible once the "
        "Caecilianist party's institutional victory is complete: the same mechanism operating "
        "throughout the window is what locks in, at the ending, exactly which small remainder of "
        "this world's own voice survives independently of it.",
        [
            "Tyconius's Liber Regularum, surviving specifically because of its own influence on "
            "Augustine's De doctrina christiana III (a transmission mechanism Doc_02 SS2 explicitly "
            "does not resolve, and does not need to resolve)",
            "the Deo laudes acclamation, transmitted by stone itself, requiring no manuscript "
            "custodian at all",
        ],
        conf("A", "verified-via-authority", "load-bearing", "Documented",
             "Documented (Doc_01 SS5, Cell 3B; Doc_08, Force 3B-2, Layer 1); this world's own "
             "participants left no account of what they understood themselves to be preserving as "
             "their own institutional position weakened -- named directly at Layer 2 as a genuine "
             "absence, not an inference offered in its place."),
        src("don.source.tyconius-liber-regularum",
            "don.source.passio-marculi",
            "don.source.passio-isaac-et-maximiani",
            "don.source.deo-laudes-acclamation-cil8"),
        "Re-derived from the approved Doc_08 Force 3B-2 (Cell 3B, Ending/Internal; Transmission "
        "dimension). relations[] carries the gravity<->force edge (G3) and the force<->force edge "
        "(2B-2, Connection 8) named above.",
    )


def main() -> None:
    build_gravities()
    build_forces()
    print(f"Wrote {len(WRITTEN)} records:")
    for p in WRITTEN:
        print(f"  {p}")


if __name__ == "__main__":
    main()
