"""B-5 (S2.1), lpc equivalent: Latin Pastoral-Congregational Christianity
(`lpc`) gravity + force records.

WHAT THIS SCRIPT DOES. Converts this world's already-built, already-reviewed
Gravity Discovery (Doc_04_Gravity_Discovery.md, Approved to proceed with
escalation items carried open) and Forces Document (Doc_08_Forces_Document.md,
Approved to proceed with portfolio-level items carried open) into
record-native `gravity` and `force` records under records/lpc/gravity/ and
records/lpc/force/, per the live schema (engine/m1/schemas.py) and gate
battery (engine/m1/gates.py). This is the direct lpc equivalent of
Build/worlds/don/scripts/wb_don_s25.py's own B-5 pass -- its MECHANICAL-
vs-AUTHORED docstring discipline and RELATION_PAIRS closed-graph technique
both carried over directly. TYPE_PROPERTIES/COMPLETION_REQUIRED for gravity
and force are unchanged from what don's script used
(name/description/manifestations/classification;
name/kind/description/manifestations/matrix_cell), checked directly against
engine/m1/schemas.py and engine/m1/gates.py rather than assumed from don's
own script -- no schema drift found.

WHAT lpc'S OWN Doc_04/Doc_08 CONFIRM, checked directly rather than assumed
from a prior summary of either document:
  - Doc_04 §4 (Classification Summary) confirms EIGHT classified candidate
    gravities: PRIMARY -- Candidate 1 (Pastoral Office as Flock-Keeping),
    Candidate 2 (Penitential Discipline), Candidate 3 (Collegial Communion
    Preserved), Candidate 6 (Sacramental/Ordination Validity); SUPPORTING --
    Candidate 4 (Preaching and Catechesis), Candidate 5 (Conciliar Authority
    Theory), Candidate 7 (Grace and Human Incapacity); TENSIONAL --
    Candidate 8 (Confessor-Authority vs. Episcopal-Regulated Peace). Doc_08
    §1 uses the short labels G1-G8 for these eight in Doc_04's own order and
    with Doc_04's own classifications -- this script follows Doc_08's own
    G1-G8 notation throughout, both in id slugs and in this docstring, and
    states once, here, that G1-G8 map one-to-one onto Doc_04's Candidate
    1-8 (never a re-numbering or a re-classification of this script's own).
  - Doc_08 §3/§9 confirms SEVENTEEN identified forces across the six-cell
    matrix (1A: 2, 1B: 3, 2A: 4, 2B: 5, 3A: 1, 3B: 2 = 17), cross-checked
    directly against lpc_Force_Index.md §1's own Master Force Table (same
    17 force IDs, same cells, same confidence tiers) before this script was
    written. This script builds all 17.

lpc_Force_Index.md IS READ FOR ITS DERIVED TABLES ONLY, PER OG-3'S OWN
DISCLOSED GAP. Open_Gaps_Tracking.md OG-3 discloses that gen_force_index.py
(the Index's own generator, a different script from this one) has findings
against it never independently re-reviewed. This script therefore treats the
Index's own derived tables (§1 Master Force Table, §3 By Connected Gravity,
§4 Cross-Cell Connection Map) as a cross-check against Doc_08's own prose --
useful precisely because the generator computes each relation from Doc_08's
own text mechanically and both this script and the generator were checked to
agree -- but every RELATION_PAIRS edge below was verified against Doc_08 §4
and §5's own prose directly, not copied from the Index alone, and every
gravity classification/six-test finding below is drawn from Doc_04's own
prose directly, never from the Index (which does not cover gravities' own
six-test results at all -- only forces).

INPUTS, mapped to OUTPUTS, precisely:
  - Doc_04_Gravity_Discovery.md §1-§2 (Candidate Generation; candidates
    considered and not advanced), §3 (Per-Candidate Testing, all eight
    subsections read in full), §4 (Classification Summary), §5 (Article 21
    Status Check -- this world's own strand-singular, phase-testing
    substitute discipline), §6 (Interaction Matrix), §7 (Open Items) -> the
    8 `gravity` records below, one per classified candidate (G1-G8, Doc_04's
    Candidate 1-8). classification is copied directly from Doc_04 §4's own
    summary table (never re-derived, including Candidate 5's own
    project-lead-ruled Supporting status, carried exactly as Doc_04 states
    it -- see G5's OWN JUDGMENT CALL below); description carries each
    candidate's own six-test verdict, Confidence/Gravity Cross-Check result,
    and forces-connection summary, condensed from Doc_04's own prose.
  - Doc_08_Forces_Document.md §1 (World Identification; the confirmed
    gravity spine), §2 (Preliminary Forces Identification), §3 (the
    six-cell matrix, all seventeen forces read in full, all three layers
    each), §4 (Cross-Cell Connections, all fourteen named connections plus
    the one deliberate non-connection at 2A-2), §5 (Forces-and-Gravities
    Synthesis, both the gravity-by-gravity list and the Cross-Strand
    Gravity Note), §7 (Confidence Assessment), §9 (Completion Certification)
    -> the 17 `force` records below, one per force identified at §3.
    matrix_cell is copied directly from each force's own cell heading
    (1A/1B/2A/2B/3A/3B -- the schema enum's six fixed codes; Doc_08's own
    prose label for cells 3A/3B, "Ending-Transforming," is carried in this
    record's own body text, never in the matrix_cell field itself, which
    the schema fixes to the shorter code); kind is derived mechanically
    from the cell (1A/1B -> initiating, 2A/2B -> ongoing, 3A/3B -> ending).
    description carries each force's own Layer 1 (Historical Event), Layer
    2 (World's Own Experience), and Layer 3 (Formation Impact) content in
    full, condensed from Doc_08's own prose.
  - Build/worlds/lpc/scripts/wb_lpc_s21.py's own emitted lpc.source.* id list (207
    ids, cross-checked against records/lpc/source/ directly via
    /tmp/lpc_row_to_source.txt, a Registry-row -> record-id map built by
    reading every source record's own external_ids.lpc_source_registry_row
    this session, not guessed) -> sources[] on every gravity/force record
    below, resolved to the specific Registry row(s) Doc_04/Doc_08 actually
    cite as that candidate's or force's own evidentiary base. Doc_04/Doc_08
    themselves are this world's own governing analytical documents, not
    vendored sources -- every citation to them lives in each record's own
    description/body text as "(Doc_04 §3.1)" etc., never in sources[].
    lpc_Force_Index.md is likewise never cited in sources[] (it is not a
    source record and, per OG-3, its own generator is disclosed-unreviewed)
    -- read only as the cross-check named above.

THREE DISCLOSED EMPTY-SOURCES CASES, matching don's own F3A-2/F3B-1
precedent of disclosing rather than forcing an unearned citation:
  - Force 1A-2 (the standing legal condition of an unlicensed religion):
    Doc_08 cites Doc_01 §2 and Doc_02 §5 -- both this world's own governing
    analytical documents, not a vendored Registry row -- for a background
    legal condition, not a claim this world's own corpus directly narrates.
  - Force 1B-3 (the inherited Latin theological vocabulary): Doc_08 cites
    Doc_01 §6-§7 and Doc_02 §2's own "Tertullian disclosure." Tertullian's
    own corpus is Registry row 29, Boundary Status EXCLUDED (wb_lpc_s21.py's
    own docstring: "credited with forging" this world's own theological
    vocabulary "without Tertullian himself being this world's own voice") --
    no lpc.source.tertullian-* record exists, confirmed directly against
    records/lpc/source/ before writing this force's own record, and none is
    invented here to supply one.
  - Force 2B-3 (the illegal-to-established shift) and Force 3B-2
    (Transmission -- the 133-year silence): both rest on a fact ABOUT this
    world's own Registry (a structural/legal condition's own placement
    judgment at 2B-3; the Registry's own dated-row gap at 3B-2), not a
    citable vendored text making a claim -- sources[] is left empty rather
    than attaching an unearned citation to a claim about structure or
    silence itself.

MECHANICAL vs AUTHORED, field by field -- the same split don's own script
states for itself, applied here:
  - id, world_id, record_type, schema_version, status, register, canon_cells:
    MECHANICAL. register="etic" throughout, matching don's own precedent and
    pahc.gravity.boundary-drawing/pahc.force.boundary-drawing's own
    register="etic" -- gravity/force are this world's own analytical build
    documents converted to record-native form, not first-person emic voice.
    Confirmed directly against engine/m1/gates.py this session: gravity and
    force are named in neither gate_voice_perspective's own PERSPECTIVE_
    FIELDS nor gate_no_build_attribution's own ATTRIBUTION_FIELDS (both now
    live in engine/m1/spoken_fields.py, checked there directly), so freely
    naming "Doc_04 §3.1," "the project lead's ruling," or an ISO date inside
    these records' own prose -- all of which Doc_04/Doc_08 themselves do
    throughout -- is not a gate risk here the way it would be in a term or
    story record's own voice-scoped fields. world_id="latin-pastoral-
    congregational-christianity", matching every lpc record built at B-1/B-2.
    canon_cells=[] throughout, unchanged from every prior lpc step.
  - name, classification (gravity) / name, kind, matrix_cell (force):
    MECHANICAL -- classification and matrix_cell copied directly from
    Doc_04 §4 and each force's own Doc_08 §3 cell heading, never
    re-derived; kind mechanically follows matrix_cell per the cell-to-kind
    mapping stated above.
  - description: AUTHORED, condensed from Doc_04 §3's six-test verdicts
    (gravity) or Doc_08 §3's three-layer entries (force), carrying the
    actual argument rather than a pointer back to either document.
  - manifestations[]: AUTHORED, drawn only from concrete, already-vendored
    facts, named events, and direct quotations Doc_04/Doc_08 themselves
    quote or cite by locus -- never a fresh translation or a fact from this
    session's own outside historical knowledge.
  - confidence.formation_confidence: AUTHORED per record, copied from each
    candidate's own Confidence/Gravity Cross-Check result (Doc_04 §3.x) or
    each force's own §7 confidence tier (Doc_08), never re-derived. Where
    Doc_04/Doc_08 name a genuine split across tiers (G3, G5; force 2B-3),
    this record carries the MORE CONSERVATIVE applicable tier as its own
    top-line rating, with the full split named explicitly in
    divergence_note, never smoothed into one unqualified number --
    matching don's own D-A/F3B-1 precedent for the identical shape of
    finding.
  - confidence.verification_state: AUTHORED, held to verified-via-authority
    throughout (never verified-direct) -- this script relies on Doc_04's
    and Doc_08's own already-completed, independently-reviewed (11 rounds
    and 8 rounds respectively) six-test/three-layer assessments, not on
    this session re-opening the raw vendored primary texts itself.
  - confidence.divergence_note: AUTHORED per record, always populated
    (never null) -- satisfies gate_confidence_crosscheck by construction
    (Documented + null divergence_note + not-verified-direct is the one
    combination that gate rejects, and this script never emits it).
  - confidence.citation_specificity / evidentiary_weight: AUTHORED per
    record from Doc_04/Doc_08's own stated evidentiary texture ("A" where
    the candidate's/force's own primary loci sit at Registry Confidence A;
    "B" where Doc_04 itself states the specific loci relied on sit at
    Registry Confidence B). evidentiary_weight is "load-bearing" throughout
    except Candidate 5 (Conciliar Authority Theory), carried as "contested"
    -- the one candidate whose own six-test profile is narrow throughout,
    whose classification required a project-lead ruling rather than the
    document's own verdict, and whose Confidence/Gravity Cross-Check
    divergence Doc_04 itself carries forward as an open item (§7 item 1) --
    "contested" states that reality plainly rather than filing it as
    load-bearing like the other seven.
  - sources[]: AUTHORED per record, resolved to the specific lpc.source.*
    ids (from B-1's own 207-record set, cross-checked against
    records/lpc/source/ directly via each record's own external_ids.
    lpc_source_registry_row) that Doc_04 §1/§3 or Doc_08 §3 actually cite
    as that candidate's or force's own evidentiary base. Three forces have
    no specific lpc.source.* grounding either document names -- see THREE
    DISCLOSED EMPTY-SOURCES CASES above.
  - relations[]: MECHANICAL, built entirely by relations_for() from
    RELATION_PAIRS -- see RELATIONS below.

RELATIONS -- THREE DISTINCT EDGE SETS, ALL SYMMETRIC associated-with, ALL
BUILT FROM ONE MASTER PAIR-LIST (RELATION_PAIRS), matching wb_don_s25.py's
own closed-graph discipline exactly:
  1. GRAVITY <-> GRAVITY (Doc_04 §6, the Interaction Matrix): every pair
     Doc_04 §6 marks Reinforcing, Competing, or Reshapes/Reshaped-by --
     a "demonstrated relationship" in that section's own terms -- becomes
     one associated-with edge. Verified directly by reading every one of
     the matrix's 8x8 cells this session: 15 such pairs exist (G1-G2, G1-G3,
     G1-G4, G1-G5, G1-G6, G1-G8, G2-G3, G2-G4, G2-G6, G2-G7, G2-G8, G3-G5,
     G3-G6, G4-G7, G5-G6); every other cell reads "No demonstrated
     relationship in this world's own Native record" and is NOT encoded as
     an edge, matching don's own T1<->T2 precedent -- unlike don's Doc_04,
     lpc's own §6 does not single out any one "no relationship" pair as its
     own separately-stated finding (its own closing paragraph discloses the
     pattern in aggregate: "Candidates 5, 7, and 8 each show several such
     cells, honestly recorded rather than filled in to avoid a thin-looking
     row"), so no gravity record below carries a dedicated "NO
     RELATIONSHIP NAMED" paragraph the way don.gravity.principled-refusal-
     vs-pragmatic-recourse and don.gravity.purity-rigor-vs-institutional-
     reception both do for their own mutual absence -- there being no
     single such pair Doc_04 itself flags as a finding in its own right.
     The R/C/X-equivalent label (Reinforcing/Competing/Reshapes) is not a
     schema-typed axis (RELATION_TYPES has no such value); it is carried in
     each gravity's own description prose instead.
  2. GRAVITY <-> FORCE (Doc_08 §5's own "Gravity-by-Gravity Force
     Connections," cross-checked against lpc_Force_Index.md §3's own "By
     Connected Gravity" table -- both name the identical 29 edges,
     independently verified against each other before this script was
     written, including G4's own force-set expansion from Doc_08 §5's
     prose set-reference "in truth every force in Cell 2A," which the
     Index's own §3 note states it expands mechanically rather than
     leaving as an unexpanded pointer): every force a gravity's own record
     lists as connected becomes one associated-with edge. Exactly three
     forces (2B-3, 2B-5, 3B-2) carry NO gravity connection at all, per
     Doc_08 §5's own gravity-by-gravity list and lpc_Force_Index.md §1's
     own "Connected Gravities: --" entries for exactly these three rows,
     confirmed directly rather than assumed: 2B-3 is a real force Doc_04
     itself declined to advance as a gravity in its own right (§2's "state
     coercive capacity" discussion), and 2B-5/3B-2 are the two dedicated
     Transmission-dimension forces, which Doc_08 §5 itself states are
     "cross-cutting rather than gravity-specific" -- matching don's
     F2B-2/F3B-2 precedent for the identical transmission-dimension
     disposition exactly. [CORRECTED, same session.] An earlier draft of
     this paragraph wrongly folded in 1A-2 and 1B-3, claiming five forces
     with no gravity connection rather than three. Both do connect: 1A-2
     to G1 (Pastoral Office), 1B-3 to G4 (Preaching and Catechesis) --
     confirmed directly in both this script's own RELATION_PAIRS and the
     compiled records themselves, neither of which was ever wrong; only
     this explanatory paragraph was. 1A-2 and 1B-3 do, separately, carry
     empty sources[] (along with 2B-3 and 3B-2) -- see the SOURCES
     paragraph below for that distinct, correctly-stated set, which this
     paragraph's earlier draft appears to have conflated with the
     gravity-connection set above.
  3. FORCE <-> FORCE (Doc_08 §4, the fourteen actually-connected Cross-Cell
     Connections; the table's own fifteenth row, 2A-2 -> none, is a
     DELIBERATE NON-CONNECTION Doc_08 itself names as a finding -- "the
     plague connects to no other force in this matrix" -- and is NOT
     encoded as an edge, the direct lpc-world analogue of don's own T1<->T2
     absence-naming, stated in Force 2A-2's own body text rather than
     silently omitted): every actually-named connection becomes one
     associated-with edge, direction and character (produces/enables/
     triggers/activates/intensifies/shapes/inverts-into/reacts-to/is-the-
     sole-instance-of/continues/coincides-with-does-not-cause) carried in
     each force's own description prose, not in the relation type --
     RELATION_TYPES's directional pairs were considered and rejected for
     the identical reason don's own docstring gives: several of Doc_08's
     own fourteen connections state something other than a strict
     precondition (2B-4 -> 3B-2 is stated as "is the sole instance of";
     3A-1 -> 3B-1 is explicitly "coincides with, does not cause"), and
     forcing all fourteen into one directional shape would overclaim
     precision Doc_08's own prose does not uniformly support.

G5'S OWN JUDGMENT CALL, STATED HERE RATHER THAN SOFTENED IN THE RECORD
ITSELF. Candidate 5 (Conciliar Authority Theory) is the one gravity in this
world whose classification Doc_04 itself did not reach on its own six-test
evidence: "Alone among the eight candidates, this line does not record this
document's own verdict on the evidence" (Doc_04 §3). It is classified
Supporting by a ruling outside Doc_04's own six-test evidence, after
repeated re-classification across several review rounds and a named
gapped-formation precedent instructing the build to stop revising it
further (Doc_04 §7 items 7-8). This script carries that classification
exactly as Doc_04 states it -- "supporting", not re-derived, not upgraded,
not downgraded -- and states the ruling's own provenance in the record's own
body text rather than presenting the classification as this document's own
settled six-test verdict, which Doc_04 explicitly says it is not. The
record's own confidence.formation_confidence is carried at the more
conservative "Inferential-Thin" tier (the organizing-breadth claim, thin
across the whole world at one locus per bishop over more than a century,
per Doc_04 §5's own "thin across the span, not bounded within it" finding)
rather than at "Documented" (which covers only the two formulas' own bare
existence, per Doc_04 §3's own Cross-Check), with the full split named in
divergence_note -- this is the one gravity record below where the
top-line/divergence-note split carries real weight rather than being a
formality.

WHAT THIS SCRIPT DOES NOT DO: assign canon_cells; touch records/lpc/{source,
world_core,term,story,figure,quote}/ or Build/worlds/lpc/scripts/wb_lpc_s24.py
(existing B-1/B-2 records are read only, for their own lpc.source.* ids;
story/figure/quote are Part 3, in independent review by a separate agent,
untouched); build lpc.contested_claim.*/voice_craft/demonstration/
doctrinal_witness/honest_limit/ambient records (later parts); declare
relations[] from any gravity/force record to any lpc.story.*/lpc.figure.*/
lpc.quote.*/lpc.term.* record (don's own B-4 docstring already established
this closed-graph discipline for exactly this reason -- doubly warranted
here, since lpc's own story/figure/quote records are still in-flight,
independent review and this script must not create a dependency on ids that
review could still change); run the M2 compiler; register `lpc` in
records/worlds.yaml; touch gen_force_index.py or lpc_Force_Index.md (OG-3's
own disclosed gap belongs to that script, not this one, and this script
reads the Index only as a cross-check -- see above).
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
# relations_for() below, "associated-with" throughout (see this script's own
# docstring for why the Reinforcing/Competing/Reshapes label and each cross-
# cell connection's own direction/character are carried in prose instead).
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
# GRAVITIES (8) -- Doc_04 §3, classification per §4's own summary table.
# ===========================================================================

def build_gravities() -> None:
    emit_gravity(
        G1, "Pastoral Office as Territorial Flock-Keeping [PRIMARY]",
        "primary",
        "Doc_04 §3 Candidate 1: PRIMARY, passes all six tests strongly. Repetition: recurs across "
        "every primary-source stream for both bishops and both phases without interruption -- both "
        "formation narratives, both phases' own crisis correspondence and sermon corpora. Dependency: "
        "Candidate 2 (penitential discipline) is exercised by a bishop holding this office; Candidate "
        "4 (preaching/catechesis) is this office's own primary activity; Candidate 5 (conciliar "
        "authority) is a theory about who legitimately holds it; Candidate 6 (sacramental validity) is "
        "a question about who legitimately holds it. Formation: Doc_01 §1's own Core Identity states "
        "this world's formation logic is 'pastoral and sacramental before it is juridical' -- the "
        "whole catechetical and penitential apparatus exists because a bishop is personally answerable "
        "for a bounded flock. Explanatory: explains why Cyprian's crisis correspondence exists at all, "
        "why Augustine's sermon corpus is so large, and why both bishops' own accounts of coming to "
        "office are independently attested and treated as formation-significant. Persistence: visible "
        "in both Carthage and Hippo, across both phases, in both bishops' own words. Interaction: "
        "reinforces Candidates 2, 3, 4, 6, 8; reinforced weakly by Candidate 5; no independently "
        "demonstrated relationship with Candidate 7. CONFIDENCE/GRAVITY CROSS-CHECK: Documented -- "
        "both bishops' own accounts of holding and exercising this office are directly quoted and "
        "independently re-verified across Doc_01's nine review rounds (the 256 preface; Letters XXXI "
        "and CCXIII; Pontius's own narrative). Possidius's Vita (Registry row 192) is NOT counted "
        "toward this Cross-Check -- Doc_02 §2/§4 both disclose it has not been read this session "
        "beyond the Megalius-consecration identification, so this candidate's Documented rating stands "
        "on Pontius, the two Letters, and the 256 preface alone, a citation correction rather than a "
        "classification change. No divergence. FORCES-CONNECTION (Doc_08 §5): the most densely "
        "force-connected gravity in this world, matching Doc_05 §9.1's own finding that it is the "
        "ecological hub -- connected to 1A-2 (the standing legal condition an office with no external "
        "enforcement is held together by personal bond), 1B-2 (how a man comes to hold it), 1A-1 and "
        "2A-1 (answerability made acute by the flock's own failure and the bishop's own test), 2A-2 "
        "(a pressure the bishop shares rather than adjudicates), 3A-1 (the bond ends when he does).",
        [
            "\"it is the shepherd that is chiefly wounded in the wound of his flock\" (Force 1A-1's "
            "own Layer 2, Doc_08 §3)",
            "Cyprian's own accounts of holding and exercising this office at the 256 Council preface, "
            "and in Letters XXXI and CCXIII",
            "Pontius's own narrative of Cyprian's conduct as bishop (Registry row 7)",
        ],
        conf("A", "verified-via-authority", "load-bearing", "Documented",
             "Doc_04 §3 Candidate 1: no divergence. Evidence reaches Documented -- both bishops' own "
             "accounts of holding and exercising this office are directly quoted and independently "
             "re-verified across Doc_01's nine review rounds; Possidius's Vita (Registry row 192) is "
             "explicitly excluded from this Cross-Check per Doc_02 §2/§4's own disclosed limitation "
             "that it has not been read this session beyond the Megalius-consecration identification "
             "-- a citation correction, not a classification change."),
        src("lpc.source.cyprian-epistles",
            "lpc.source.cyprian-seventh-council-of-carthage",
            "lpc.source.pontius-life-and-passion-of-cyprian"),
        "Re-derived from the approved Doc_04 §3 (Candidate 1), cross-checked against Doc_04 §4's own "
        "Classification Summary and §6's own Interaction Matrix. relations[] carries the "
        "gravity<->gravity edges (G2, G3, G4, G5, G6, G8) and the gravity<->force edges (1A-1, 1A-2, "
        "1B-2, 2A-1, 2A-2, 3A-1) named in this record's own description above.",
    )

    emit_gravity(
        G2, "Penitential Discipline: the Reintegration of the Failed [PRIMARY]",
        "primary",
        "Doc_04 §3 Candidate 2: PRIMARY. Repetition: passes strongly, recurring in De Lapsis (Row 2), "
        "the Epistles' own lapsed correspondence (Row 1), Pontius's narrative (Row 7), and Doc_02 §5's "
        "own liturgical-evidence disclosure. Author Gravity risk flagged at generation: the "
        "Cyprian-phase evidence is multi-locus and independently corroborated, but the candidate's own "
        "cross-phase claim rests on Cyprian's own single phase passing. Dependency: passes strongly -- "
        "Candidate 8 (confessor-authority tension) exists only because this gravity exists; this "
        "gravity's own resolution (readmission, not permanent exclusion) models Candidate 3's logic at "
        "the individual-believer level. Formation: passes strongly -- the paradigm formation-shaping "
        "practice in this world's own record. Explanatory: passes strongly -- explains the "
        "Novatianist schism (rigorist refusal to readmit), the Felicissimus schism (a laxer rival "
        "readmission practice), and Candidate 8. PERSISTENCE -- TESTED RATHER THAN ASSUMED, PER "
        "DOC_01 §8 ITEM 7'S OWN BINDING INSTRUCTION: passes for Cyprian's own phase directly; for "
        "Augustine's own phase, THE LEAN DOES NOT FULLY SURVIVE AS THIS SAME GRAVITY PERSISTING UNDER "
        "ITS OWN NAME. Doc_02's own record shows no Augustine-phase text organized around a "
        "'lapsed'-equivalent crisis at the same acute, empire-wide scale; the closest analogues "
        "(Donatist schism-temptation, ordinary catechized sin) are real but are tested and classified "
        "as their own distinct gravities, Candidates 6 and 7, not as this gravity's own direct "
        "continuation. What survives across the phase boundary is a family resemblance, not the same "
        "gravity restated. Interaction: reinforces Candidates 1, 3, 4, 6; reshaped by Candidate 7 (not "
        "this gravity's own continuation); competes with Candidate 8. CONFIDENCE/GRAVITY CROSS-CHECK: "
        "Documented for Cyprian's own conduct and correspondence, directly quoted and re-verified "
        "across Doc_01's nine rounds; of the loci this rests on, the De Lapsis locus (Row 2) sits at "
        "Registry Confidence B, the Epistles and Pontius loci (Rows 1, 7) at A. No divergence for the "
        "Cyprian-phase gravity. FORCES-CONNECTION (Doc_08 §5): directly is Doc_01 §6's own Ongoing/"
        "Internal cell content -- connected to 1A-1 (creates its subject matter), 1B-1 (the organized "
        "church without which a regulated process could not have been run), 2B-1 (the recurring "
        "contest it answers), 2B-2 (the rival claim it was built against). Its own second-phase "
        "persistence is qualified rather than assumed (Doc_08 §3 Force 2B-1's own Layer 3): the "
        "concern does not continue under its own name; what survives is a family resemblance toward "
        "G6 and G7, tested and classified separately -- this gravity's own force-connection therefore "
        "stays first-phase-grounded.",
        [
            "De Lapsis, Cyprian's own founding treatise of the penitential controversy (Registry row 2)",
            "the Novatianist schism (rigorist refusal to readmit the lapsed) and the Felicissimus "
            "schism (a laxer rival readmission practice), both explained by this gravity",
            "the confessors' own competing claim to grant peace, which this gravity's own regulated "
            "process was built against (Force 2B-2)",
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
        "Re-derived from the approved Doc_04 §3 (Candidate 2). relations[] carries the "
        "gravity<->gravity edges (G1, G3, G4, G6, G7, G8) and the gravity<->force edges (1A-1, 1B-1, "
        "2B-1, 2B-2) named above -- 2B-1's own asymmetric family-resemblance finding (first-phase, "
        "toward G6, not toward G7) is discussed at G6's own record below, per Doc_08 §5's own G6 entry.",
    )

    emit_gravity(
        G3, "Collegial Communion Preserved Despite Disagreement [PRIMARY]",
        "primary",
        "Doc_04 §3 Candidate 3: PRIMARY. Repetition: passes strongly, recurring at the 256 preface "
        "(Row 4, 'neither does any of us set himself up as a bishop of bishops... every bishop... has "
        "his own proper right of judgment'), throughout On Baptism (Row 13 -- Augustine arguing at "
        "length against Cyprian's own specific ruling while never treating him as outside communion), "
        "and in Letter 185's own pastoral-corrective register (Row 12). Dependency: passes strongly -- "
        "Doc_01 §5's own Article 3 coherence argument for this world's own coherence across the "
        "century-gap is built directly on this gravity: what a bishop does when he disagrees is work "
        "to preserve communion, or break communion and build a rival, parallel hierarchy. Candidate 6 "
        "(sacramental validity) is the specific doctrinal question on which this gravity is tested "
        "hardest. Formation: passes -- shapes how both bishops conduct disagreement; neither breaks "
        "fellowship over the sharpest doctrinal disputes in this world's own record, with no "
        "counter-instance in either bishop's own corpus. Explanatory: passes strongly -- explains why "
        "Augustine's own extensive, respectful engagement with a bishop he disputes reads as filial "
        "argument rather than repudiation, and this world's own boundary against Donatism directly. "
        "Persistence: passes -- attested in both phases, through both bishops' own conduct, not "
        "merely a shared word. Interaction: reinforces Candidates 1, 2, 5, 6. CONFIDENCE/GRAVITY "
        "CROSS-CHECK -- DIVERGENCE FLAGGED, NOT RESOLVED, PER CF V7.4'S OWN RULE: the underlying "
        "primary-source facts (the 256 preface's own words; On Baptism's own extensive argument) "
        "reach Documented, directly quoted and re-verified across Doc_01's nine rounds; the SYNTHESIS "
        "-- that these facts constitute one named, cross-phase gravity, rather than two separate "
        "historical facts -- is this document's own reasoning, at Widely Accepted rather than "
        "Documented confidence. Flagged rather than resolved, and this record carries the more "
        "conservative tier (Widely Accepted) as its own top-line rating rather than smoothing the "
        "split away. FORCES-CONNECTION (Doc_08 §5): every force connected to this gravity is a force "
        "that TESTED it rather than produced it -- 1B-1 (colleagues who can assemble and already "
        "disagree), 2A-3 (tested at its hardest edge, and holds), 2B-4 (tested across the century "
        "gap, and holds). This gravity is this world's own adaptive rule, stress-tested three times "
        "from three directions.",
        [
            "the 256 Council preface's own words: \"neither does any of us set himself up as a bishop "
            "of bishops... every bishop... has his own proper right of judgment\" (Registry row 4)",
            "Augustine arguing at length against Cyprian's own specific rebaptism ruling throughout On "
            "Baptism (Registry row 13), while never treating him as outside communion",
            "Letter 185's own pastoral-corrective register toward the Donatist schism (Registry row 12)",
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
        "Re-derived from the approved Doc_04 §3 (Candidate 3). relations[] carries the "
        "gravity<->gravity edges (G1, G2, G5, G6) and the gravity<->force edges (1B-1, 2A-3, 2B-4) "
        "named above.",
    )

    emit_gravity(
        G4, "Preaching and Catechesis as Primary Formation Mode [SUPPORTING]",
        "supporting",
        "Doc_04 §3 Candidate 4: SUPPORTING. Passes Repetition, Formation, and Persistence cleanly; "
        "passes Dependency, Explanatory, and Interaction only narrowly, because the evidence shows "
        "this gravity functions as the medium other gravities are taught through rather than an "
        "independently organizing force -- the same honest, narrower-pass shape Imperial-Juridical's "
        "own Doc_04 reports for a structurally comparable candidate. Repetition: recurs in the Sermons "
        "(Row 19), the Tractates on John (Row 21), the catechetical works (Rows 15, 18), and Cyprian's "
        "own De Dominica Oratione (Row 5). Dependency: passes narrowly -- Candidate 1 depends on this "
        "as its own primary activity, but this document finds no other candidate depending on "
        "preaching/catechesis the way they depend on Candidates 1-3; it functions more as the medium "
        "through which the other gravities are taught and enforced. Formation: passes strongly -- "
        "direct, textbook formation content, the explicit subject of the catechetical works and the "
        "stated purpose of both bishops' own preaching corpora. Explanatory: passes narrowly -- "
        "explains HOW formation happens more than WHY any particular crisis occurred. Persistence: "
        "passes -- attested in both phases, in both bishops' own words. Interaction: passes narrowly "
        "-- reinforces Candidates 1, 2, 7; no independently demonstrated relationship with Candidates "
        "3, 5, 6, 8. CONFIDENCE/GRAVITY CROSS-CHECK: Documented for existence and basic content, per "
        "Doc_02 §8's own bracket; the specific loci sit at Registry Confidence B. No divergence. "
        "FORCES-CONNECTION (Doc_08 §5): connected to 1B-3 (the vernacular register it needs), and IN "
        "TRUTH EVERY FORCE IN CELL 2A (2A-1, 2A-2, 2A-3, 2A-4), since this gravity is the channel "
        "through which external pressure reaches an ordinary believer -- the mechanism Doc_08 §4's own "
        "first finding depends on and §5 names as this world's characteristic response: crisis "
        "metabolized into teaching. 2A-2 (the plague) is the clearest single case: it generated no "
        "gravity and no practice, only a treatise, produced entirely through this gravity's own medium.",
        [
            "the Sermons (Registry row 19) and Tractates on John (row 21), Augustine's own vast "
            "preaching and exegetical corpus",
            "the catechetical works (Registry rows 15, 18) explicitly addressed to converts and "
            "catechumens",
            "De Mortalitate, Cyprian's own treatise answering the plague of c. 249-262 (Registry row "
            "5) -- a pressure that produced teaching, through this gravity, rather than structure",
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
        "Re-derived from the approved Doc_04 §3 (Candidate 4). relations[] carries all three of "
        "Doc_04 §6's own Interaction Matrix edges for Candidate 4 (Reinforcing with G1, Reinforcing "
        "with G2, Reinforcing with G7) -- G1 and G2 were already captured as edges when this "
        "script processed those rows earlier, so G7 is the only edge this record's own row newly "
        "contributes, not the only gravity-level relationship G4 has in total -- and the "
        "gravity<->force edges (1B-3, 2A-1, 2A-2, 2A-3, 2A-4, "
        "the last four an expansion of Doc_08 §5's own prose set-reference 'every force in Cell 2A', "
        "cross-checked against lpc_Force_Index.md §3's own identical expansion) named above.",
    )

    emit_gravity(
        G5, "Conciliar Authority Theory (Egalitarian vs. Hierarchical) [SUPPORTING]",
        "supporting",
        "Doc_04 §3 Candidate 5: the one gravity in this world whose classification Doc_04 itself did "
        "not reach on its own six-test evidence -- 'Alone among the eight candidates, this line does "
        "not record this document's own verdict on the evidence' (Doc_04 §3). Classified SUPPORTING "
        "BY A RULING OUTSIDE DOC_04'S OWN SIX-TEST EVIDENCE, after repeated re-classification "
        "across several review rounds and a named gapped-formation precedent instructing the build to "
        "stop revising it further (Doc_04 §7 items 7-8). Author Gravity risk flagged at generation: "
        "each pole is attested within each bishop's own single locus. Repetition: passes narrowly and "
        "locally -- Cyprian's egalitarian formula recurs once, at length, in the 256 preface (Row 4); "
        "Augustine's hierarchical formula recurs internally within On Baptism (Row 13, 'plenary' 31 "
        "times) but is not independently restated in a second Augustine-authored work drawn on here. "
        "Dependency: passes narrowly -- Doc_01's own strand-singular finding is the one place in this "
        "world's construction record that depends on this axis at all. Formation: DOES NOT CLEARLY "
        "PASS -- this document finds no evidence that ordinary believers, catechumens, or most clergy "
        "in either phase were formed by, or even aware of, this specific theoretical question. "
        "Explanatory: passes narrowly -- explains the specific shape of the Cyprian/Stephen rebaptism "
        "dispute and Augustine's own extended argument against Cyprian's ruling, but no other, "
        "independent aspect of the wider ecology. PERSISTENCE: DOES NOT PASS AT THE WORLD LEVEL, on a "
        "disclosed search bound rather than an unqualified absence -- within what this document has "
        "validly read, there is no evidence either bishop's theory was independently visible outside "
        "the one locus each is drawn from. THIN ACROSS THE SPAN, NOT BOUNDED WITHIN IT (Doc_04 §5's "
        "own distinction from Candidate 7's phase-boundedness): visible in both phases, at one locus "
        "each, 'between two bishops at two moments separated by over a century.' Interaction: passes "
        "narrowly -- interacts demonstrably with Candidates 1 (weakly), 3, and 6. CONFIDENCE/GRAVITY "
        "CROSS-CHECK -- DIVERGENCE FLAGGED, NOT RESOLVED: evidence for the EXISTENCE of both formulas, "
        "in their own words, reaches Documented; the evidential support for their ORGANIZING BREADTH "
        "does not reach the same level, this candidate's six-test profile being narrow at best -- CF "
        "V7.4: 'gravity strength and evidential confidence are distinct properties that can diverge.' "
        "Carried forward at Doc_04 §7 Open Item 1 as unresolved, and NOT reopened by the 411 Gesta "
        "(unread; §7 Open Item 6) or by nine further review rounds (§7 Open Item 8, a sixth attempt at "
        "a cleaner classification, whose own argument Doc_04 records rather than pursues). "
        "FORCES-CONNECTION (Doc_08 §5): THE WEAKEST FORCE-CONNECTION IN THE MATRIX, and Doc_08 says so "
        "rather than padding it -- connected to 1B-1 (the conciliar setting), 2A-3 (the Donatist "
        "appeal that supplies the occasion), 2B-4 (the engagement itself), but 'every force touching "
        "G5 touches it through a third party's citation of a text, not through a pressure on the "
        "world's own practice' -- consistent with Doc_04's own finding that no evidence shows the "
        "question reached ordinary formation. Doc_08 §5 quotes the Forces Framework directly: 'a "
        "gravity that cannot be connected to the forces acting on the world is a gravity whose ecology "
        "is incomplete.' Carried, not resolved.",
        [
            "the 256 Council preface's own egalitarian formula, \"neither does any of us set himself "
            "up as a bishop of bishops\" (Registry row 4)",
            "Augustine's own hierarchical formula in On Baptism II.3, invoking \"the authority of "
            "plenary Councils\" (Registry row 13, the word occurring 31 times within the treatise)",
            "a ruling outside Doc_04's own six-test evidence, classifying this candidate Supporting after "
            "Doc_04's own six-test assessment did not reach a verdict on the evidence (Doc_04 §3, §7 "
            "items 7-8)",
        ],
        conf("B", "verified-via-authority", "contested", "Inferential-Thin",
             "Doc_04 §3 Candidate 5: divergence flagged, not resolved -- the sharpest such divergence "
             "in this document. Existence of both formulas, in their own words, reaches Documented "
             "(directly quoted and re-verified across Doc_01's nine rounds); the evidential support "
             "for their ORGANIZING BREADTH does not reach the same level, this candidate's six-test "
             "profile being narrow throughout and Persistence failing at world level on a disclosed "
             "search bound -- carried at the more conservative Inferential-Thin tier as this record's "
             "own top-line rating rather than the bare-existence Documented tier, per this candidate's "
             "own 'thin across the span, not bounded within it' finding (Doc_04 §5). The classification "
             "itself (Supporting) rests on a ruling outside this document's own six-test evidence, not "
             "this document's own six-test verdict -- carried exactly as Doc_04 §3 states this, neither upgraded nor "
             "downgraded here."),
        src("lpc.source.cyprian-seventh-council-of-carthage",
            "lpc.source.augustine-on-baptism-against-the-donatists"),
        "Re-derived from the approved Doc_04 §3 (Candidate 5), matching this record's own body text "
        "to Doc_04 §5's careful distinction between this candidate and Candidate 7 (phase-bound) "
        "rather than collapsing the two Persistence failures into one shape. relations[] carries the "
        "gravity<->gravity edges (G1, G3, G6) and the gravity<->force edges (1B-1, 2A-3, 2B-4) named "
        "above. See this script's own docstring, 'G5'S OWN JUDGMENT CALL,' for why this record states "
        "the project-lead-ruling provenance directly rather than presenting Supporting as this "
        "document's own settled verdict.",
    )

    emit_gravity(
        G6, "Sacramental and Ordination Validity Across the Boundary of the Church [PRIMARY]",
        "primary",
        "Doc_04 §3 Candidate 6: PRIMARY. Repetition: passes strongly, recurring in the Epistles' own "
        "rebaptism correspondence (Row 1), the 256 Council's own ruling (Row 4), and On Baptism in "
        "full (Row 13, argued 'at book length') -- not confined to one locus the way Candidate 5 is, "
        "argued across two independent bishops' own extended treatments, decades apart. Dependency: "
        "passes strongly -- Candidate 3 is tested at its hardest specifically because this question "
        "exists (the two bishops reach opposite conclusions here while Candidate 3 still holds); "
        "Candidate 8 is a structurally adjacent question about who may legitimately grant standing "
        "within the community. Formation: passes -- directly shapes practice; Cyprian's own rebaptism "
        "requirement is an operative pastoral policy, Augustine's own contrary ruling determines "
        "whether Donatist clergy are received back in their own orders or re-ordained. Explanatory: "
        "passes strongly -- explains the entire Stephen/Cyprian rupture, is the central subject of a "
        "whole Augustine treatise, and explains why the Donatists themselves could appeal to Cyprian's "
        "own authority for their own rebaptism doctrine. Persistence: passes -- the question persists "
        "even as the answer changes, itself evidence of the question's own centrality. Interaction: "
        "reinforces Candidates 1, 2, 3, 5. CONFIDENCE/GRAVITY CROSS-CHECK: Documented -- both "
        "positions directly quoted and independently re-verified across Doc_01's nine rounds (On "
        "Baptism I.1.2; the 256 preface; Book III ch. 2 §2). No divergence. FORCES-CONNECTION (Doc_08 "
        "§5): directly connected to the Ongoing/External force of the Donatist schism (2A-3), which "
        "makes it institutionally urgent rather than a question about individual converts; re-opened "
        "across the century gap by 2B-4 (Augustine's own engagement with Cyprian's conciliar acts); "
        "and connected to 2B-1 (the recurring contest over the failed member), Doc_04 §6 finding "
        "Cyprian reasoning about both consistently -- an ASYMMETRIC relation Doc_08 §5 itself examines "
        "at length: Candidate 2 relates to this gravity as 'Reinforcing... both are boundary/"
        "reintegration questions Cyprian reasons about consistently,' a first-phase relation, while "
        "Candidate 2 relates to Candidate 7 as 'Reshaped by... not 2's own continuation.' This "
        "gravity's own claim on Force 2B-1 is therefore independent and first-phase, and does not rest "
        "on the phase-two family resemblance that runs toward G7 instead.",
        [
            "the 256 Council's own rebaptism ruling (Registry row 4)",
            "On Baptism, Against the Donatists in full, argued at book length (Registry row 13, "
            "citing I.1.2 and Book III ch. 2 §2)",
            "the Epistles' own rebaptism correspondence, the Stephen/Cyprian rupture (Registry row 1)",
        ],
        conf("A", "verified-via-authority", "load-bearing", "Documented",
             "Doc_04 §3 Candidate 6: no divergence. Both positions directly quoted and independently "
             "re-verified across Doc_01's nine review rounds (On Baptism I.1.2; the 256 preface; Book "
             "III ch. 2 §2)."),
        src("lpc.source.cyprian-epistles",
            "lpc.source.cyprian-seventh-council-of-carthage",
            "lpc.source.augustine-on-baptism-against-the-donatists"),
        "Re-derived from the approved Doc_04 §3 (Candidate 6), with the 2B-1 asymmetry independently "
        "re-verified against Doc_08 §5's own G6 entry, which examines and confirms it at length, "
        "rejecting an argument that had removed the connection on a symmetry that does not "
        "exist. relations[] carries the gravity<->gravity edges (G1, G2, G3, G5) and the "
        "gravity<->force edges (2A-3, 2B-1, 2B-4) named above.",
    )

    emit_gravity(
        G7, "Grace and Human Incapacity [SUPPORTING]",
        "supporting",
        "Doc_04 §3 Candidate 7: SUPPORTING -- organizes a significant, extremely well-evidenced "
        "portion of the ecology (Augustine's own phase specifically) but does not extend across this "
        "world's own full span the way Candidates 1, 2, 3, 6 do. Author Gravity risk flagged at "
        "generation: the entire evidentiary base is one voice (Augustine) within one evidence stream "
        "(the anti-Pelagian corpus, Row 23), disclosed here rather than discovered as a concern after "
        "testing, precisely because the density of the evidence could otherwise read as breadth. "
        "Repetition: passes strongly, and by a wide margin the most textually dense candidate on this "
        "list -- 1,798 raw occurrences of 'grace' within Row 23's own thirteen works alone. Dependency: "
        "passes narrowly -- this document finds no other candidate depending on this gravity resolving "
        "one way or the other; real, heavily attested, but structurally freestanding. Formation: "
        "passes strongly for Augustine's own phase specifically -- a direct, sustained "
        "catechetical/polemical formation project across thirteen dedicated works. Explanatory: passes "
        "for Augustine's own phase (explains the anti-Pelagian corpus's own existence and scale) but "
        "does not extend backward to Cyprian's own phase -- the Pelagian controversy postdates Cyprian "
        "by over a century. Persistence: FAILS TO PASS AT THE WORLD LEVEL (no Cyprian-phase evidence "
        "identified) but passes strongly within Augustine's own phase specifically -- a real temporal "
        "boundary, not a gap in the search. Interaction: passes narrowly -- reshapes Candidate 2 (a "
        "related but distinct Augustine-phase question, not that gravity's own continuation); "
        "reinforces Candidate 4. CONFIDENCE/GRAVITY CROSS-CHECK: Documented for the corpus's own "
        "existence and scale, directly vendored and independently swept by Doc_03; Documented for "
        "existence and basic content per Doc_02 §8's own bracket, the specific loci sitting at "
        "Registry Confidence B. No divergence for the Augustine-phase gravity itself. "
        "FORCES-CONNECTION (Doc_08 §5): SINGLE-FORCE-ORIGIN, a real finding rather than thin analysis "
        "-- connected to 2A-4 (Manichaeism/Pelagianism as live rival systems, which produces this "
        "gravity directly and entirely) and 3B-1 (the corpus outliving the world, carrying this "
        "gravity out of it). The forces analysis independently reproduces the Author Gravity shape "
        "Doc_04 flagged at generation: one external pressure, one corpus, one phase.",
        [
            "the anti-Pelagian corpus, thirteen works occasioned by a live controversy, 1,798 raw "
            "occurrences of \"grace\" within its own bounds (Registry row 23)",
            "Augustine's own refusal of Pelagian anthropology's claim that a believer's own moral "
            "effort is sufficient without grace (Doc_01 §6)",
        ],
        conf("B", "verified-via-authority", "load-bearing", "Documented",
             "Doc_04 §3 Candidate 7: no divergence for the Augustine-phase gravity itself. Documented "
             "for the corpus's own existence and scale, directly vendored and independently swept by "
             "Doc_03; per Doc_02 §8's own bracket, the specific loci relied on sit at Registry "
             "Confidence B. Persistence fails at the world level -- no Cyprian-phase evidence "
             "identified -- a real temporal boundary named directly rather than a confidence gap."),
        src("lpc.source.augustine-anti-pelagian-corpus"),
        "Re-derived from the approved Doc_04 §3 (Candidate 7). relations[] carries the "
        "gravity<->gravity edges (G2, G4) and the gravity<->force edges (2A-4, 3B-1) named above.",
    )

    emit_gravity(
        G8, "Confessor-Authority vs. Episcopal-Regulated Peace [TENSIONAL]",
        "tensional",
        "Doc_04 §3 Candidate 8: TENSIONAL. Author Gravity risk flagged at generation: the evidence "
        "base is essentially one Registry row (1) read through one lexicon entry. Two genuinely "
        "distinct poles: (a) confessors -- survivors of interrogation under persecution -- issuing "
        "written requests, on the strength of their own confession, that named lapsed persons be "
        "received back, an informal claim to grant peace; (b) Cyprian's own regulated, episcopally-"
        "controlled penitential process, built specifically to answer that competing claim. "
        "Repetition: passes as a persistent tension rather than a resolved position -- visible in "
        "Epistles XX-XXI (the confessors' own informal, first-person exercise of this claimed "
        "authority) and, in managed/regulated form, throughout De Lapsis and Cyprian's own penitential "
        "correspondence. Dependency: passes -- Candidate 2 exists in the shape it does specifically "
        "because an informal, competing claim to grant peace already existed and had to be regulated, "
        "not invented from nothing. Formation: passes -- shapes how Cyprian himself has to keep "
        "re-asserting episcopal authority over reconciliation throughout his own crisis "
        "correspondence, rather than legislating it once and being done. Explanatory: passes -- "
        "explains why De Lapsis and the lapsed-crisis Epistles argue so insistently for episcopal "
        "control over readmission, a level of insistence Candidate 2's own existence alone does not "
        "fully explain without this tension behind it. Persistence: passes as a persistent, unresolved "
        "counter-pressure specifically within the Cyprian-phase crisis window, rather than as a "
        "broadly world-organizing force in its own right -- the Tensional classification's own "
        "defining character, not a failure. Interaction: competes with Candidate 2; reinforces "
        "Candidate 1. CONFIDENCE/GRAVITY CROSS-CHECK: Documented for both poles' existence (Epistles "
        "XX-XXI's own first-person confessor correspondence; De Lapsis's own regulating argument); of "
        "the two loci, the Epistles (Row 1) sit at Confidence A and De Lapsis (Row 2) at B. No "
        "divergence -- the tension itself, not a confidence gap, is the finding. FORCES-CONNECTION "
        "(Doc_08 §5): held, rather than resolved, under the Initiating/External force that creates "
        "confessors as a category with any claim to authority at all -- connected to 1A-1 (the Decian "
        "persecution, which is what creates confessors as a class), 2A-1 (the Valerianic persecution, "
        "which confirms rather than reshapes this tension and ends the phase in which it is attested), "
        "2B-2 (the confessors' own claim itself). Phase-one-bound on a positive check -- all three "
        "connected forces are phase-one forces, and no Augustine-phase confessor-authority material is "
        "identified anywhere in this world's own corpus, confirming the bound rather than straining it.",
        [
            "\"thousands of certificates were daily given, contrary to the law of the Gospel\" "
            "(Force 2B-2's own Layer 1, quoting Cyprian directly, Doc_08 §3)",
            "Epistles XX-XXI, the confessors' own informal, first-person written requests granting "
            "peace to the lapsed (Registry row 1)",
            "De Lapsis's own regulating argument for episcopal control over readmission (Registry row 2)",
        ],
        conf("A", "verified-via-authority", "load-bearing", "Documented",
             "Doc_04 §3 Candidate 8: no divergence -- the tension itself, not a confidence gap, is the "
             "finding. Documented for both poles' existence; of the two loci, the Epistles (Registry "
             "row 1) sit at Confidence A and De Lapsis (row 2) at B, carried here as the record's own "
             "top-line citation_specificity of A on the strength of the primary confessor-voice locus."),
        src("lpc.source.cyprian-epistles",
            "lpc.source.cyprian-de-lapsis"),
        "Re-derived from the approved Doc_04 §3 (Candidate 8). relations[] carries the "
        "gravity<->gravity edges (G1, G2) and the gravity<->force edges (1A-1, 2A-1, 2B-2) named "
        "above.",
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
        "Doc_08 Cell 1A, Force 1A-1. LAYER 1 -- HISTORICAL EVENT: the first systematically enforced, "
        "empire-wide persecution, administered through certificates recording that the holder had "
        "sacrificed. It did not principally demand renunciation; it demanded a documented act of "
        "compliance, obtainable by performing the sacrifice or by paying to have it recorded. "
        "Documented -- Doc_01 §2; Doc_02 §1; the crisis correspondence itself (Registry row 1, "
        "Confidence A) and De Lapsis (row 2, Confidence B). LAYER 2 -- WORLD'S OWN EXPERIENCE: not an "
        "attack from outside so much as a table emptied one certificate at a time. The demand reached "
        "each person singly and left the congregation sorted into those who had stood and those who "
        "had not -- and both were still ours, still in the room. \"[I]t is the shepherd that is "
        "chiefly wounded in the wound of his flock.\" LAYER 3 -- FORMATION IMPACT: this force created "
        "the category the entire penitential system exists to process. There were no lapsed before "
        "there was a certificate to obtain, and no confessors with a claim on anything before there "
        "was an interrogation to survive. It produces G2 directly and G8 as G2's own counter-pressure; "
        "it intensifies G1, since a bishop's answerability becomes acute precisely when his people "
        "fail; and it generates this world's own densest crisis vocabulary -- the lapsed, "
        "reconciliation, confessor, and the certificates of both kinds. CROSS-CELL CONNECTIONS (Doc_08 "
        "§4): -> Force 2B-1 (produces) -- the Decian edict creates the category of the failed member "
        "the ongoing internal contest is about; without this force there is no 2B-1. -> Force 2B-2 "
        "(produces) -- the same edict creates confessors as a class with a claim; 2B-2 has no "
        "claimants without it. <- Force 2A-1 (reacted to by) -- the Valerianic persecution repeats "
        "this test on a community that has by then built a discipline for it.",
        [
            "the libelli, certificates recording that the holder had sacrificed, obtainable by "
            "performing the sacrifice or by paying to have it recorded",
            "\"[I]t is the shepherd that is chiefly wounded in the wound of his flock\" (Cyprian, "
            "quoted directly at Doc_08 Force 1A-1 Layer 2)",
        ],
        conf("A", "verified-via-authority", "load-bearing", "Documented",
             "Doc_08 §3 Force 1A-1: Documented, attested across Doc_01's own founding-boundary "
             "reasoning and Doc_02 §1, corroborated by the crisis correspondence (Registry row 1, "
             "Confidence A) and De Lapsis (row 2, Confidence B); no divergence flagged for this "
             "force's own bare occurrence."),
        src("lpc.source.cyprian-epistles",
            "lpc.source.cyprian-de-lapsis"),
        "Re-derived from the approved Doc_08 §3 Force 1A-1 (Cell 1A, Initiating/External). "
        "relations[] carries the gravity<->force edges (G1, G2, G8) and the force<->force edges "
        "(2B-1, 2B-2, 2A-1) named above.",
    )

    emit_force(
        F1A2, "The Standing Legal Condition of an Unlicensed Religion in Romanized Provincial North "
              "Africa",
        "initiating", "1A",
        "Doc_08 Cell 1A, Force 1A-2. LAYER 1 -- HISTORICAL EVENT: through the whole of this world's "
        "first phase, Christianity held no legal standing in a Romanized provincial society with real "
        "underlying Punic and, inland, Berber populations. Persecution was episodic; the exposure was "
        "continuous. Widely Accepted -- Doc_01 §2 (Cultural Environment; Historical Pressures); "
        "Doc_02 §5. LAYER 2 -- WORLD'S OWN EXPERIENCE: a bishop could be taken and was. The office "
        "carried no protection and the community no recourse; what it had was each other, and "
        "whatever a man was willing to do for the people in his charge while he still could. LAYER 3 "
        "-- FORMATION IMPACT: this condition is why G1 develops as personal answerability rather than "
        "as jurisdiction -- an office with no external enforcement is held together by the bond "
        "between one man and one congregation. It is also the condition whose removal in the second "
        "phase Doc_04 §2 tested as a candidate gravity and declined to advance, finding nothing in "
        "this ecology organizes around the shift itself. Named here as a force precisely because it is "
        "not a gravity: it shaped what the office could be without becoming something the ecology "
        "organizes around. CROSS-CELL CONNECTIONS (Doc_08 §4): -> Force 1B-2 (shapes) -- an office "
        "with no legal protection is one a sensible man declines, which is why the acclamation pattern "
        "has to override reluctance. -> Force 2B-3 (inverts into) -- the standing condition of "
        "illegality is precisely what the illegal-to-established shift removes; the same fact appears "
        "at both ends of the matrix with opposite sign.",
        [
            "the continuous legal exposure of an unlicensed religion across a Romanized provincial "
            "society with real underlying Punic and Berber populations, against which persecution was "
            "only episodic",
        ],
        conf("B", "verified-via-authority", "load-bearing", "Widely Accepted",
             "Doc_08 §3 Force 1A-2: Widely Accepted -- Doc_01 §2 (Cultural Environment; Historical "
             "Pressures) and Doc_02 §5, a background legal condition rather than a claim any single "
             "vendored Registry row directly narrates; no lpc.source.* record is cited for it in "
             "Doc_08's own text, and none is invented here to supply one."),
        [],
        "Re-derived from the approved Doc_08 §3 Force 1A-2 (Cell 1A, Initiating/External). "
        "relations[] carries the gravity<->force edge (G1) and the force<->force edges (1B-2, 2B-3) "
        "named above. sources[] is deliberately empty -- see this script's own docstring, THREE "
        "DISCLOSED EMPTY-SOURCES CASES.",
    )

    emit_force(
        F1B1, "An Already-Organized Carthaginian Church Capable of Sustained Collective Response",
        "initiating", "1B",
        "Doc_08 Cell 1B, Force 1B-1. LAYER 1 -- HISTORICAL EVENT: Cyprian inherited a community large "
        "and structured enough to hold real internal factions and to convene councils of dozens of "
        "bishops at short notice. Documented -- Doc_01 §6; the councils themselves (Registry row 4); "
        "the Felicissimus material in the Epistles (row 1). LAYER 2 -- WORLD'S OWN EXPERIENCE: not a "
        "gathering that had to be built but one already standing, with its own men of weight, its own "
        "quarrels, and its own capacity to meet and decide together. LAYER 3 -- FORMATION IMPACT: this "
        "is the precondition for G3 -- collegial communion preserved despite disagreement requires "
        "colleagues who can actually assemble and who already disagree. It also makes G2's regulated "
        "penitential process possible -- an unorganized community could not have run one -- and "
        "supplies G5 with the conciliar setting in which both its formulas are eventually spoken. "
        "CROSS-CELL CONNECTIONS (Doc_08 §4): -> Force 1B-2 (enables) -- a church organized enough to "
        "hold factions is organized enough to elect over a faction's opposition. -> Force 2B-4 "
        "(enables) -- councils that met and left acts are what Augustine later reads and argues with.",
        [
            "councils of dozens of bishops convened at short notice (Registry row 4, the 256 Council)",
            "the Felicissimus schism, a real internal faction the church was already organized enough "
            "to hold (Registry row 1)",
        ],
        conf("A", "verified-via-authority", "load-bearing", "Documented",
             "Doc_08 §3 Force 1B-1: Documented -- Doc_01 §6; the councils themselves (Registry row 4) "
             "and the Felicissimus material in the Epistles (row 1); no divergence flagged for this "
             "force's own bare occurrence."),
        src("lpc.source.cyprian-seventh-council-of-carthage",
            "lpc.source.cyprian-epistles"),
        "Re-derived from the approved Doc_08 §3 Force 1B-1 (Cell 1B, Initiating/Internal). "
        "relations[] carries the gravity<->force edges (G2, G3, G5) and the force<->force edges "
        "(1B-2, 2B-4) named above.",
    )

    emit_force(
        F1B2, "Congregational Acclamation Overriding a Reluctant Convert's Preference",
        "initiating", "1B",
        "Doc_08 Cell 1B, Force 1B-2. LAYER 1 -- HISTORICAL EVENT: Cyprian, a trained rhetorician "
        "converted in middle life, was elected bishop by the acclamation of the Carthaginian people "
        "within roughly two to three years of conversion, over the recorded opposition of five "
        "presbyters. The pattern recurs in the second phase at both of Augustine's offices: he was "
        "seized into the presbyterate at Hippo in 391 against his wishes, and at the episcopate "
        "Possidius's Vita ch. VIII records Valerius announcing his intention to the bishops present, "
        "the whole Hippo clergy, and all the people; those who heard rejoiced and clamoured eagerly "
        "for it; Augustine refused the episcopate while his own bishop lived; and, persuaded by "
        "transmarine and African precedent, he yielded under compulsion and constraint. "
        "Documented -- Epistle XXXIX (row 1); Pontius (row 7, Confidence "
        "A); Possidius's Vita chs. IV and VIII (row 192); Doc_01 §2. LAYER 2 -- WORLD'S OWN EXPERIENCE: "
        "\"your suffrage and God's judgment,\" set against a faction's \"ancient venom.\" A deacon who "
        "knew him put it from outside: \"by the judgment of God and the favour of the people, he was "
        "chosen to the office of the priesthood and the degree of the episcopate while still a "
        "neophyte.\" LAYER 3 -- FORMATION IMPACT: this force gives G1 its characteristic "
        "two-directional shape -- a bishop answerable to the people who placed him as well as for "
        "them. A caution carried directly rather than smoothed: the pattern is attested through "
        "different figures and different words, not one recurring term -- but at the same office in "
        "both phases. CROSS-CELL CONNECTIONS (Doc_08 §4): <- Force 1A-2 (shaped by) -- an office with "
        "no legal protection is one a sensible man declines, which is why the acclamation pattern has "
        "to override reluctance. <- Force 1B-1 (enabled by) -- a church organized enough to hold "
        "factions is organized enough to elect over a faction's opposition.",
        [
            "\"your suffrage and God's judgment\" (Cyprian's own words on his election, Doc_08 Force "
            "1B-2 Layer 2)",
            "\"by the judgment of God and the favour of the people, he was chosen to the office of the "
            "priesthood and the degree of the episcopate while still a neophyte\" (a deacon's own "
            "outside account, Doc_08 Force 1B-2 Layer 2)",
            "Possidius, Vita Augustini ch. VIII: Valerius's own announcement, and Augustine's own "
            "refusal and yielding \"under compulsion and constraint\" (Registry row 192)",
        ],
        conf("A", "verified-via-authority", "load-bearing", "Documented",
             "Doc_08 §3 Force 1B-2: Documented -- Epistle XXXIX (Registry row 1); Pontius (row 7, "
             "Confidence A); Possidius's Vita chs. IV and VIII (row 192); Doc_01 §2. The pattern is "
             "attested through different figures and different words at the same office in both "
             "phases, a caution carried directly in this force's own Layer 3 rather than smoothed "
             "into one uniform recurring term."),
        src("lpc.source.cyprian-epistles",
            "lpc.source.pontius-life-and-passion-of-cyprian",
            "lpc.source.possidius-vita-augustini-weiskotten1919"),
        "Re-derived from the approved Doc_08 §3 Force 1B-2 (Cell 1B, Initiating/Internal). "
        "relations[] carries the gravity<->force edge (G1) and the force<->force edges (1A-2, 1B-1) "
        "named above.",
    )

    emit_force(
        F1B3, "The Inherited Latin Theological Vocabulary",
        "initiating", "1B",
        "Doc_08 Cell 1B, Force 1B-3. LAYER 1 -- HISTORICAL EVENT: North African Latin Christianity "
        "possessed, before this world begins, a vigorous local literary culture and the Latin "
        "theological vocabulary Tertullian is credited with forging. Widely Accepted -- Doc_01 §6, §7; "
        "Doc_02 §2 (the Tertullian disclosure). LAYER 2 -- WORLD'S OWN EXPERIENCE: the words were to "
        "hand. What had to be argued could be argued in the language the people in the assembly "
        "already spoke. LAYER 3 -- FORMATION IMPACT: enables G4 -- preaching and catechesis as the "
        "primary formation mode presupposes a vernacular theological register capable of carrying the "
        "content. PROPORTIONALITY NOTE (Doc_08 §8): treated briefly. This force is real and enabling "
        "but is not contested, not phase-specific, and does not shape any gravity's own content -- "
        "only its medium. No cross-cell connection is named for this force in Doc_08 §4.",
        [
            "the pre-existing Latin theological vocabulary Tertullian is credited with forging, "
            "available to this world's own bishops without needing to be invented",
        ],
        conf("B", "verified-via-authority", "load-bearing", "Widely Accepted",
             "Doc_08 §3 Force 1B-3: Widely Accepted -- Doc_01 §6, §7; Doc_02 §2's own Tertullian "
             "disclosure. Tertullian's own corpus is Registry row 29, Boundary Status EXCLUDED (this "
             "world's own construction begins after Tertullian; his vocabulary is inherited, not this "
             "world's own voice) -- no lpc.source.tertullian-* record exists to cite, and none is "
             "invented here to supply one."),
        [],
        "Re-derived from the approved Doc_08 §3 Force 1B-3 (Cell 1B, Initiating/Internal). "
        "relations[] carries the gravity<->force edge (G4) named above. sources[] is deliberately "
        "empty -- see this script's own docstring, THREE DISCLOSED EMPTY-SOURCES CASES.",
    )

    emit_force(
        F2A1, "Recurring Persecution After Decius -- the Valerianic Persecution (257-258)",
        "ongoing", "2A",
        "Doc_08 Cell 2A, Force 2A-1. LAYER 1 -- HISTORICAL EVENT: renewed imperial persecution under "
        "Valerian, under which Cyprian was exiled and then martyred in 258. Documented -- Doc_01 §2; "
        "the Acta Proconsularia within Registry row 194. LAYER 2 -- WORLD'S OWN EXPERIENCE: the thing "
        "had not finished with us. The man who had spent seven years deciding what to do with those who "
        "failed the first test was himself taken by the second, and did not fail it. LAYER 3 -- "
        "FORMATION IMPACT: confirms rather than reshapes G1 and G8 -- it closes the first phase by "
        "demonstrating, in the person of the bishop who regulated the lapsed, what the confessors' own "
        "credential had been about. It also ends the first phase's own documentary record, which is "
        "why G2 and G8 are attested only within it. CROSS-CELL CONNECTION (Doc_08 §4): -> Force 1A-1 "
        "(reacts to) -- the Valerianic persecution repeats the Decian test on a community that has now "
        "built a discipline for it.",
        [
            "Cyprian's own exile and martyrdom under Valerian in 258 (the Acta Proconsularia, "
            "Registry row 194)",
        ],
        conf("A", "verified-via-authority", "load-bearing", "Documented",
             "Doc_08 §3 Force 2A-1: Documented -- Doc_01 §2; the Acta Proconsularia within Registry "
             "row 194; no divergence flagged for this force's own bare occurrence."),
        src("lpc.source.cyprian-opera-spuria-vita-pontius-acta-proconsularia-csel3-pars3"),
        "Re-derived from the approved Doc_08 §3 Force 2A-1 (Cell 2A, Ongoing/External). relations[] "
        "carries the gravity<->force edges (G1, G4, G8) and the force<->force edge (1A-1) named above.",
    )

    emit_force(
        F2A2, "Epidemic Disease -- the Plague of c. 249-262",
        "ongoing", "2A",
        "Doc_08 Cell 2A, Force 2A-2. LAYER 1 -- HISTORICAL EVENT: a severe, well-attested pandemic "
        "running through Carthage across Cyprian's episcopate, addressed directly in De Mortalitate. "
        "Documented -- Doc_01 §2; Registry row 5. LAYER 2 -- WORLD'S OWN EXPERIENCE: a pressure no "
        "discipline could sort. The persecution at least asked a question a person could answer "
        "rightly or wrongly; this asked nothing and took the faithful and the lapsed alike. LAYER 3 -- "
        "FORMATION IMPACT: this is the clearest case in this world of a pressure that produced "
        "teaching rather than structure. It generated no gravity and no practice; it generated a "
        "treatise -- the sharpest single illustration of the mechanism Doc_08 §4 names as this world's "
        "characteristic response: crisis metabolized into formation content through G4. DELIBERATELY "
        "ISOLATED, NAMED RATHER THAN SILENTLY OMITTED (Doc_08 §4): this force connects to no other "
        "force in this matrix -- 'not a weak entry: it is this world's clearest case of a pressure "
        "that produced formation content without producing formation structure, and the Cross-Cell "
        "Connection Principle is better served by recording the absence than by manufacturing a "
        "link.' This is NOT encoded as a relations[] entry -- see this script's own docstring for why "
        "an examined absence and an omitted edge would otherwise read identically.",
        [
            "De Mortalitate, Cyprian's own treatise directly addressing the plague of c. 249-262 "
            "(Registry row 5)",
        ],
        conf("A", "verified-via-authority", "load-bearing", "Documented",
             "Doc_08 §3 Force 2A-2: Documented -- Doc_01 §2; Registry row 5; no divergence flagged for "
             "this force's own bare occurrence."),
        src("lpc.source.cyprian-minor-pastoral-treatises"),
        "Re-derived from the approved Doc_08 §3 Force 2A-2 (Cell 2A, Ongoing/External). relations[] "
        "carries only the gravity<->force edges (G1, G4) named above -- deliberately NO force<->force "
        "edge, per Doc_08 §4's own explicit 'deliberately isolated' finding for this force, named "
        "rather than silently applied, matching don's own F3A-2/2A-2-equivalent precedent for a "
        "disclosed non-connection.",
    )

    emit_force(
        F2A3, "The Donatist Schism",
        "ongoing", "2A",
        "Doc_08 Cell 2A, Force 2A-3. LAYER 1 -- HISTORICAL EVENT: dominant across large parts of North "
        "African Christian life for most of the century between the two phases, and a continuing live "
        "pastoral problem throughout Augustine's episcopate. Documented -- Doc_01 §2; Doc_02 §1; "
        "Registry rows 12, 13. LAYER 2 -- WORLD'S OWN EXPERIENCE: not strangers and not heretics of a "
        "foreign kind, but a church in the same towns, with its own bishop in the same see, claiming "
        "to be the only true one -- and appealing, for its central practice, to our own first bishop's "
        "own ruling. LAYER 3 -- FORMATION IMPACT: the force with the most consequential reach in the "
        "second phase. It makes G6 institutionally urgent rather than a question about individual "
        "converts; it tests G3 at its hardest edge, and G3 holds; it supplies G5's entire occasion, "
        "since the Donatists' own appeal to Cyprian's conciliar acts is what obliged Augustine to "
        "argue against a predecessor he could not disown; and it is the external pressure behind the "
        "coercion doctrine Doc_01 insists be held at three phases rather than compressed. CROSS-CELL "
        "CONNECTIONS (Doc_08 §4): -> Force 2B-4 (triggers) -- the Donatists' own appeal to Cyprian's "
        "conciliar acts is what prompts Augustine to read them; external prompt, internal act. -> "
        "Force 2B-3 (activates) -- a rival communion is what makes the newly available state capacity "
        "worth using, the occasion of the three-phase coercion development.",
        [
            "the Donatists' own appeal to Cyprian's conciliar acts and rebaptism authority for their "
            "own central practice (Registry rows 12, 13)",
            "a rival bishop claiming the same see, the same towns, throughout Augustine's own episcopate",
        ],
        conf("A", "verified-via-authority", "load-bearing", "Documented",
             "Doc_08 §3 Force 2A-3: Documented -- Doc_01 §2; Doc_02 §1; Registry rows 12, 13; no "
             "divergence flagged for this force's own bare occurrence."),
        src("lpc.source.augustine-correction-of-the-donatists",
            "lpc.source.augustine-on-baptism-against-the-donatists"),
        "Re-derived from the approved Doc_08 §3 Force 2A-3 (Cell 2A, Ongoing/External). relations[] "
        "carries the gravity<->force edges (G3, G4, G5, G6) and the force<->force edges (2B-4, 2B-3) "
        "named above.",
    )

    emit_force(
        F2A4, "Manichaeism and Pelagian Anthropology as Live Rival Systems",
        "ongoing", "2A",
        "Doc_08 Cell 2A, Force 2A-4. LAYER 1 -- HISTORICAL EVENT: Manichaeism, an organized rival "
        "system Augustine belonged to for roughly nine years before his conversion and a recurring "
        "target thereafter; the Pelagian controversy of the 410s-420s, occupying a thirteen-work "
        "corpus. Documented -- Doc_01 §2, §6; Registry rows 22, 23. LAYER 2 -- WORLD'S OWN EXPERIENCE: "
        "two ways of accounting for a person that a bishop had to answer from the pulpit, because the "
        "people in front of him had heard them. LAYER 3 -- FORMATION IMPACT: produces G7 directly and "
        "entirely -- the anti-Pelagian corpus is this world's single densest textual object, 1,798 raw "
        "occurrences of grace within its own bounds. THE MANICHAEAN HALF IS NAMED AND NOT DEVELOPED, on "
        "a disclosure carried from Doc_04 §7 item 4: it was never independently tested as its own "
        "candidate gravity because Doc_03's own discovery pass had not surfaced a specific enough term "
        "to test against. Proportionality note: that is a stated limit, not a judgement that the "
        "Manichaean pressure was slight. CROSS-CELL CONNECTION (Doc_08 §4): -> Force 3B-1 (produces) "
        "-- the anti-Pelagian corpus this force generates is the largest single component of the "
        "inheritance at 3B-1.",
        [
            "Manichaeism, an organized rival system Augustine belonged to for roughly nine years "
            "before his conversion (Registry row 22)",
            "the thirteen-work anti-Pelagian corpus, 1,798 raw occurrences of \"grace\" within its own "
            "bounds (Registry row 23)",
        ],
        conf("A", "verified-via-authority", "load-bearing", "Documented",
             "Doc_08 §3 Force 2A-4: Documented -- Doc_01 §2, §6; Registry rows 22, 23. The Manichaean "
             "half is named and not developed as its own candidate gravity, per Doc_04 §7 item 4 -- a "
             "stated limit rather than a judgement that the Manichaean pressure was slight, and this "
             "record does not treat that limit as a confidence divergence in the Pelagian half's own "
             "Documented rating."),
        src("lpc.source.augustine-anti-manichaean-corpus",
            "lpc.source.augustine-anti-pelagian-corpus"),
        "Re-derived from the approved Doc_08 §3 Force 2A-4 (Cell 2A, Ongoing/External). relations[] "
        "carries the gravity<->force edges (G4, G7) and the force<->force edge (3B-1) named above.",
    )

    emit_force(
        F2B1, "The Recurring Contest Over How to Treat the Failed Member",
        "ongoing", "2B",
        "Doc_08 Cell 2B, Force 2B-1. LAYER 1 -- HISTORICAL EVENT: the lapsed under Cyprian; ordinary "
        "post-baptismal sin and schism-tempted believers under Augustine. Documented -- Doc_01 §6's "
        "own Ongoing/Internal cell; Registry rows 1, 2, 12, 13. LAYER 2 -- WORLD'S OWN EXPERIENCE: the "
        "question that would not go away -- what do you owe someone who is yours and has failed? A "
        "church that takes everyone back the same afternoon has no door; one that takes no one back "
        "has no Master. LAYER 3 -- FORMATION IMPACT: G2 is this force's direct product in the first "
        "phase. Its second-phase persistence is QUALIFIED RATHER THAN ASSUMED, per Doc_04's own "
        "Persistence test: the concern does not continue under its own name, and what survives is a "
        "family resemblance to G6 and G7, tested and classified separately. This force therefore "
        "connects to G2 and to G6 -- both FIRST-PHASE relations -- and NOT to G7. The asymmetry is "
        "Doc_04 §6's own, not this document's: Candidate 2 relates to Candidate 6 as 'Reinforcing... "
        "both are boundary/reintegration questions Cyprian reasons about consistently,' within the "
        "first phase, while Candidate 2 relates to Candidate 7 as 'Reshaped by... not 2's own "
        "continuation.' The phase-two afterlife is therefore a family resemblance toward G7, not a "
        "force-connection, which is why this force's own list does not carry G7 and its single-force "
        "origin toward G2/G6 stands. CROSS-CELL CONNECTIONS (Doc_08 §4): <- Force 1A-1 (produced by) "
        "-- the Decian edict creates the category of the failed member this contest is about. <- Force "
        "2B-2 (intensified by) -- the confessors' own parallel system is why the internal contest had "
        "to be settled by a formal process rather than by episcopal say-so.",
        [
            "the lapsed under Cyprian; ordinary post-baptismal sin and schism-tempted believers under "
            "Augustine (Registry rows 1, 2, 12, 13)",
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
        "Re-derived from the approved Doc_08 §3 Force 2B-1 (Cell 2B, Ongoing/Internal). relations[] "
        "carries the gravity<->force edges (G2, G6) and the force<->force edges (1A-1, 2B-2) named "
        "above -- deliberately NOT G7, per this force's own asymmetric family-resemblance finding "
        "above.",
    )

    emit_force(
        F2B2, "The Confessors' Claim to Grant Peace",
        "ongoing", "2B",
        "Doc_08 Cell 2B, Force 2B-2. LAYER 1 -- HISTORICAL EVENT: survivors of interrogation issued "
        "written requests that named lapsed persons be received back -- in Cyprian's own words, "
        "\"thousands of certificates were daily given, contrary to the law of the Gospel.\" Documented "
        "-- Registry row 1 (Confidence A). LAYER 2 -- WORLD'S OWN EXPERIENCE: I stood before the "
        "magistrate and did not deny Him, and I say this man may come back. -- And the peace of the "
        "church is not any man's to give out of his own suffering, however real. Both in earnest; that "
        "is the difficulty. LAYER 3 -- FORMATION IMPACT: this force is G8, the Tensional gravity, and "
        "it is also why G2 takes the insistent, repeatedly-restated form it does. The penitential "
        "process was not legislated into a vacuum but built against a working parallel system already "
        "circulating documents at scale. PHASE-BOUND, and the bound was established by a check rather "
        "than assumed: twenty stem occurrences of \"confessor\" across all eight vendored Augustine "
        "volumes, none in this sense. CROSS-CELL CONNECTIONS (Doc_08 §4): <- Force 1A-1 (produced by) "
        "-- the same edict creates confessors as a class with a claim; this force has no claimants "
        "without it. -> Force 2B-1 (intensifies) -- the confessors' own parallel system is why the "
        "internal contest had to be settled by a formal process rather than by episcopal say-so.",
        [
            "\"thousands of certificates were daily given, contrary to the law of the Gospel\" "
            "(Cyprian's own words, Registry row 1, quoted directly at Doc_08 Force 2B-2 Layer 1)",
        ],
        conf("A", "verified-via-authority", "load-bearing", "Documented",
             "Doc_08 §3 Force 2B-2: Documented -- Registry row 1, Confidence A; no divergence flagged "
             "for this force's own bare occurrence. Phase-bound on a positive check (twenty stem "
             "occurrences of 'confessor' across all eight vendored Augustine volumes, none in this "
             "sense), not assumed from silence."),
        src("lpc.source.cyprian-epistles"),
        "Re-derived from the approved Doc_08 §3 Force 2B-2 (Cell 2B, Ongoing/Internal). relations[] "
        "carries the gravity<->force edges (G2, G8) and the force<->force edges (1A-1, 2B-1) named "
        "above.",
    )

    emit_force(
        F2B3, "The Illegal-to-Established Shift in the Office's Political Capacity",
        "ongoing", "2B",
        "Doc_08 Cell 2B, Force 2B-3. LAYER 1 -- HISTORICAL EVENT: between the phases, the office moved "
        "from holding no legal standing to being able to solicit state action against a rival "
        "communion. Documented for the external change itself; CONTESTED for the one element that is "
        "genuinely disputable -- the placement of this force's consequence as internal rather than "
        "external, which follows Doc_01 §6's own sketch and is named here as that document's own "
        "judgement rather than this one's. Its external driver is the standing condition at 1A-2, "
        "inverted. LAYER 2 -- WORLD'S OWN EXPERIENCE: what a bishop could do had changed, though what "
        "a bishop was had not. Cyprian never asked the magistrate for anything; a century and a third "
        "later the magistrate could be asked, and eventually was. LAYER 3 -- FORMATION IMPACT: Doc_04 "
        "§2 TESTED THIS AS A CANDIDATE GRAVITY AND DECLINED TO ADVANCE IT, finding nothing in this "
        "ecology organizes around the shift itself -- it changes the instruments available to a "
        "bishop, not the thing a bishop is. Doc_07 §2E reaches the same conclusion from the "
        "ethical/legal side. Carried here as a real force with a deliberately bounded formation "
        "impact, per the Proportionality Principle. CROSS-CELL CONNECTIONS (Doc_08 §4): <- Force 1A-2 "
        "(inverted from) -- the standing condition of illegality is precisely what this shift removes; "
        "the same fact appears at both ends of the matrix with opposite sign. <- Force 2A-3 (activated "
        "by) -- a rival communion is what makes the newly available state capacity worth using.",
        [
            "Cyprian never asking the magistrate for anything, against Augustine's own later "
            "recourse to state action against the Donatist schism a century and a third afterward",
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
        "Re-derived from the approved Doc_08 §3 Force 2B-3 (Cell 2B, Ongoing/Internal). No "
        "gravity<->force edge -- Doc_08 §5's own gravity-by-gravity list and lpc_Force_Index.md §1's "
        "own 'Connected Gravities: --' both confirm this force connects to no classified gravity, "
        "consistent with Doc_04 §2's own decision not to advance the underlying shift as a candidate. "
        "relations[] carries the force<->force edges (1A-2, 2A-3) named above. sources[] is "
        "deliberately empty -- see this script's own docstring, THREE DISCLOSED EMPTY-SOURCES CASES.",
    )

    emit_force(
        F2B4, "Augustine's Engagement with Cyprian's Conciliar Acts",
        "ongoing", "2B",
        "Doc_08 Cell 2B, Force 2B-4. LAYER 1 -- HISTORICAL EVENT: Augustine read, argued with, and "
        "overturned the 256 Council's own ruling on rebaptism, in On Baptism, Against the Donatists. "
        "Documented -- Registry rows 4, 13. LAYER 2 -- WORLD'S OWN EXPERIENCE: a predecessor who is "
        "ours, whom we do not disown, and who decided this wrongly. \"[E]ven of the plenary Councils, "
        "the earlier are often corrected by those which follow them.\" LAYER 3 -- FORMATION IMPACT: "
        "the only force in this matrix that carries this world's own formation logic across its own "
        "133-year silence, and Doc_07 §3A finds the crossing is textual rather than successive. It "
        "produces G5's second formula, tests G3 across the gap, and re-opens G6. THE PLACEMENT "
        "JUDGEMENT, EXAMINED RATHER THAN INHERITED: Doc_01 §6 places this force in the Internal column "
        "while flagging that the engagement was prompted by the Donatists' own citation of Cyprian -- "
        "an external prompt for an internal act. Doc_08 confirms the placement and states the reason: "
        "the reading, the argument, and the conclusion are this world's own acts; the prompt "
        "determines only the timing. CROSS-CELL CONNECTIONS (Doc_08 §4): <- Force 1B-1 (enabled by) "
        "-- councils that met and left acts are what Augustine later reads and argues with. <- Force "
        "2A-3 (triggered by) -- the Donatists' own appeal to Cyprian's conciliar acts is what prompts "
        "Augustine to read them. -> Force 3B-2 (is the sole instance of) -- this force is the only one "
        "in this matrix that carries formation logic across the 133-year silence recorded at 3B-2; the "
        "crossing is textual and is attested twice, the second instance (Possidius quoting Cyprian's "
        "De Mortalitate) not itself a force in this matrix.",
        [
            "\"[E]ven of the plenary Councils, the earlier are often corrected by those which follow "
            "them\" (Augustine, On Baptism, quoted directly at Doc_08 Force 2B-4 Layer 2)",
            "Augustine reading, arguing with, and overturning the 256 Council's own rebaptism ruling "
            "(Registry rows 4, 13)",
        ],
        conf("A", "verified-via-authority", "load-bearing", "Documented",
             "Doc_08 §3 Force 2B-4: Documented -- Registry rows 4, 13; no divergence flagged for this "
             "force's own bare occurrence. The internal-versus-external placement is examined and "
             "confirmed rather than inherited silently: the prompt (the Donatists' own citation of "
             "Cyprian) is external, but the reading, argument, and conclusion are this world's own "
             "internal acts, per Doc_08's own stated reason."),
        src("lpc.source.cyprian-seventh-council-of-carthage",
            "lpc.source.augustine-on-baptism-against-the-donatists"),
        "Re-derived from the approved Doc_08 §3 Force 2B-4 (Cell 2B, Ongoing/Internal). relations[] "
        "carries the gravity<->force edges (G3, G5, G6) and the force<->force edges (1B-1, 2A-3, "
        "3B-2) named above.",
    )

    emit_force(
        F2B5, "Transmission -- Survival on the Institutionally Dominant Side, Through a "
              "19th-Century Translation Apparatus",
        "ongoing", "2B",
        "Doc_08 Cell 2B, Force 2B-5 -- the Transmission dimension this cell is required to address "
        "explicitly (Doc_08 §9 completion certification), synthesized fully at Doc_08 §6. LAYER 1 -- "
        "HISTORICAL EVENT: both anchor figures' writing survives in unusually full form; each was, by "
        "the time of writing or of later transmission, on the institutionally dominant and eventually "
        "canonized side of every dispute he engaged. This build's actual access is narrower than "
        "that: the working corpus is the 19th-century Ante-Nicene and Nicene and Post-Nicene Fathers "
        "English translation projects, with critical Latin editions vendored but far less used. "
        "Documented for the survival pattern and for the composition of this build's own corpus. "
        "Named transmission agents: the Catholic institutional manuscript tradition; the ANF/NPNF "
        "editors and translators; and the vendoring decisions of this build itself. LAYER 2 -- "
        "WORLD'S OWN EXPERIENCE: this world was acutely conscious of transmission and acted on it. "
        "Cyprian assembles his own correspondence into a dossier and forwards it -- \"these thirteen "
        "letters sent forth at various times declare to you, which I have transmitted to you.\" He "
        "knows his letters are read beyond their addressee, and experiences textual corruption "
        "directly: receiving a letter whose \"matter, and even the paper itself, gave me the idea that "
        "something had been taken away, or had been changed from the original,\" he returns it for "
        "collation. A century and a third later the same consciousness takes a different form: "
        "Augustine, near the end of his life, sets out to review his own works \"with a certain "
        "judicial severity,\" and to mark what displeases him \"as with a censor's pen\" -- a "
        "deliberate act of curating what would outlast him. What this world could not experience is "
        "the part that happened later: the Catholic institutional tradition's own selection, and a "
        "19th-century translation programme. LAYER 3 -- FORMATION IMPACT: three effects. First, the "
        "record is full and single-angled at once -- this world's own asymmetry is not hostile "
        "mediation, but the near-total absence of any non-episcopal voice. Second, the 19th-century "
        "editorial apparatus is interleaved with the text and has repeatedly been read as the world's "
        "own voice -- this build has eight documented local instances of the defect. Third, "
        "translation shapes discovery, not only accuracy: a headword sweep in the original language "
        "cannot find a term a corpus only ever names in translation. CROSS-CELL CONNECTION (Doc_08 "
        "§4): -> Force 3B-2 (continues) -- the same transmission pattern operates in both cells; 3B-2 "
        "is this force's own effect on the span rather than on the content.",
        [
            "Cyprian's own dossier of thirteen letters, \"sent forth at various times... which I have "
            "transmitted to you\" (Registry row 1)",
            "a suspect letter Cyprian returns for collation, because \"the paper itself gave me the "
            "idea that something had been taken away, or had been changed from the original\" "
            "(Registry row 1)",
            "Augustine's Retractationes, reviewing his own life's work \"with a certain judicial "
            "severity\" and marking what displeases him \"as with a censor's pen\" (Registry row 209, "
            "a Latin-only witness, this build's own English rendering)",
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
        "Re-derived from the approved Doc_08 §3 Force 2B-5 (Cell 2B, Ongoing/Internal; Transmission "
        "dimension). relations[] carries only the force<->force edge (3B-2) named above -- "
        "deliberately no gravity<->force edge, per Doc_08 §5's own explicit 'cross-cutting, not "
        "gravity-specific' disposition for this force (matching don.force.transmission-hostile-"
        "manuscript-tradition's own identical disposition), named rather than silently applied.",
    )

    emit_force(
        F3A1, "The Vandal Invasion (from 429) and the Siege of Hippo",
        "ending", "3A",
        "Doc_08 Cell 3A, Force 3A-1. LAYER 1 -- HISTORICAL EVENT: the Vandals crossed from Spain in "
        "429 and besieged Hippo in the final months of Augustine's life; he died on 28 August 430. A "
        "near-contemporary Gallic chronicler independently records the death under that year. "
        "Documented -- Registry row 203. (Row 203 also records the Vandal capture of Carthage under "
        "439 -- a different city, nine years later, and no part of this world's own end-boundary.) "
        "LAYER 2 -- WORLD'S OWN EXPERIENCE: an army on the road while the bishop lay dying inside the "
        "walls, with the people he was answerable for still in the city. LAYER 3 -- FORMATION IMPACT: "
        "this force closes the world on the same register that opened it -- external, violent pressure "
        "on ordinary congregational life -- the second of Doc_01 §2's own two grounds for the 430 "
        "boundary. It terminates the attested life of G1: the bond between this bishop and this flock "
        "ends when he does. CROSS-CELL CONNECTION (Doc_08 §4): -> Force 3B-1 (coincides with, does not "
        "cause) -- the invasion closes the world; the corpus outlives it, named as coincidence rather "
        "than causation -- the inheritance was secured by copying, not by the siege.",
        [
            "the siege of Hippo, beginning 429, in the final months of Augustine's life",
            "Augustine's own death on 28 August 430, independently recorded by a near-contemporary "
            "Gallic chronicler (Registry row 203)",
        ],
        conf("A", "verified-via-authority", "load-bearing", "Documented",
             "Doc_08 §3 Force 3A-1: Documented -- Registry row 203, a near-contemporary Gallic "
             "chronicle independently recording Augustine's death under 430; no divergence flagged "
             "for this force's own bare occurrence."),
        src("lpc.source.prosper-epitoma-chronicon-mommsen1892"),
        "Re-derived from the approved Doc_08 §3 Force 3A-1 (Cell 3A, Ending/External). relations[] "
        "carries the gravity<->force edge (G1) and the force<->force edge (3B-1) named above.",
    )

    emit_force(
        F3B1, "The Corpus Outliving the World",
        "ending", "3B",
        "Doc_08 Cell 3B, Force 3B-1. LAYER 1 -- HISTORICAL EVENT: Augustine's theological output, "
        "produced under this world's own pastoral pressures, became the foundational inheritance of "
        "the subsequent Western theological tradition far beyond this world's own close. Widely "
        "Accepted -- Doc_01 §6. LAYER 2 -- WORLD'S OWN EXPERIENCE (Reported-Experience Status, "
        "Constitution Article 17; Forces Framework §3 -- reported as the world's own self-"
        "understanding, not assessed for historical accuracy): not experienced as an ending -- but not "
        "experienced as nothing, either. A bishop writing against a live error writes for the people in "
        "front of him and for the case at hand, not for a tradition he expects to found. Yet this world "
        "did take its own corpus seriously as a thing that would stand after it: Cyprian gathers and "
        "forwards his own letters as a body of work; Augustine, at the end, goes back through "
        "everything he has written and corrects it (the Retractationes, Registry row 209, a Latin-only "
        "witness). A man who revises his life's work has understood that the work will be read when he "
        "cannot answer for it -- what he has not understood, and what no one in this world could, is "
        "which of it would matter, or to whom. LAYER 3 -- FORMATION IMPACT: the transformation is real "
        "and runs outward rather than inward. G7 in particular outlives its own ecology -- a gravity "
        "Doc_04 finds structurally freestanding within this world becomes load-bearing for traditions "
        "that follow it. This is the one force whose formation impact lands mostly outside the world's "
        "own boundaries, which is why it sits in the Ending row rather than the Ongoing one. CROSS-CELL "
        "CONNECTIONS (Doc_08 §4): <- Force 2A-4 (produced by) -- the anti-Pelagian corpus generated by "
        "that force is the largest single component of this inheritance. <- Force 3A-1 (coincides "
        "with, does not cause) -- the invasion closes the world; the corpus outlives it, named as "
        "coincidence rather than causation.",
        [
            "Augustine's own theological corpus, becoming \"the foundational inheritance of the "
            "subsequent Western theological tradition\" (Doc_01 §6)",
            "Augustine's Retractationes, reviewing his own life's work near the end of it (Registry "
            "row 209)",
        ],
        conf("B", "verified-via-authority", "load-bearing", "Widely Accepted",
             "Doc_08 §3 Force 3B-1: Widely Accepted -- Doc_01 §6. Layer 2 carries the Reported-"
             "Experience Status marker (Constitution Article 17; Forces Framework §3): reported as the "
             "world's own self-understanding, not assessed for historical accuracy; confidence "
             "calibration applies to the historical-event layer only, which this record's own "
             "top-line rating reflects."),
        src("lpc.source.knoll-augustine-retractationes-csel36"),
        "Re-derived from the approved Doc_08 §3 Force 3B-1 (Cell 3B, Ending/Internal). relations[] "
        "carries the gravity<->force edge (G7) and the force<->force edges (2A-4, 3A-1) named above.",
    )

    emit_force(
        F3B2, "Transmission: an Unevenly Attested Span and a 133-Year Silence",
        "ending", "3B",
        (
            "Our closing decades are much better attested than our opening ones. Between Cyprian's years "
            "and Augustine's lies a silence of roughly 133 years, counted from Cyprian's martyrdom to "
            "Augustine's ordination. A group of our texts stands at the very start of it. They were "
            "written at and just after Cyprian's martyrdom. They are the record of his trial, the life "
            "written by his deacon Pontius, and two accounts of other martyrs. No source fixes their "
            "order. They belong to Cyprian's time, and they do not fill the silence. After them, none of "
            "our sources carries on Cyprian's voice. None gives a bishop's ordinary pastoral or "
            "congregational voice, or a congregation's voice, that continues his.\n\n"
            "Some of our texts are dated in those years. One is Optatus of Milevis, writing against the "
            "Donatists. Another is a set of documents from the Donatist quarrel under Constantine. None "
            "of them carries on Cyprian's voice, and we draw on none of them for a claim. Other texts "
            "fall in those years too. They are canons from Carthage councils, early writings of Augustine "
            "from before he was ordained, and laws of the Theodosian Code from before 391. We use them "
            "for other purposes, never to fill the gap. This is a fact about our record, and it can be "
            "checked against our sources.\n\n"
            "Augustine does not receive Cyprian through a chain of teachers who knew him. He receives a "
            "set of council acts and letters, reads them, and argues with them. He treats a predecessor's "
            "ruling as a document to weigh, not a custom to continue. The inheritance was therefore "
            "received as text rather than carried as living memory. Cyprian was a predecessor met on a "
            "page, weighed, answered, and never able to answer back. And the gap was not felt as a gap. "
            "Someone formed in either period did not know our world had a documentary silence in it.\n\n"
            "This has three effects. First, continuity across the gap runs through texts, not through a "
            "line of successors. Augustine's reading of Cyprian's council acts is the one thing of ours "
            "that carries it across. Nothing else we have found does. The crossing is attested twice. The "
            "second case is Possidius quoting Cyprian's De Mortalitate.\n\n"
            "Second, those years are well documented, but almost entirely through Donatist sources, not "
            "ours. So we must take care at that edge. The silence is not simply missing evidence. The "
            "temptation is to fill it from that other record, and we do not let ourselves do that.\n\n"
            "Third, some concerns belong to one period only, and that reflects our record as well as our "
            "world. Penitential discipline and the confessor-versus-bishop tension are attested only in "
            "Cyprian's years. Grace and human incapacity appears only in Augustine's. We confirmed each "
            "of these limits by looking for it in our sources, not by inferring it from silence.\n\n"
            "This is the same pattern that let both men's writings survive on the dominant side. Here it "
            "shapes the span of the record rather than its content."
        ),
        [
            "the roughly 133-year gap between Cyprian's martyrdom (258) and Augustine's ordination "
            "(391), at whose very start stand the texts written at and just after the martyrdom (the "
            "Acta Cypriani, Pontius's Life, and two martyr acts, rows 231 and 232) that belong to "
            "Cyprian's phase and do not fill it, and after which no source supplies a bishop's ordinary "
            "pastoral or congregational voice, or a congregation's voice, that continues Cyprian's; the "
            "Registry texts dated inside the gap that this world names (Optatus of Milevis, rows 27, 64 "
            "and 264, and the appendix documents, row 265) are drawn on for no claim",
            "Augustine reading and arguing with Cyprian's own council acts and letters as a text to be "
            "weighed, not a custom carried by living memory",
        ],
        conf("A", "verified-via-authority", "load-bearing", "Documented",
             (
               "Doc_08 §3 Force 3B-2: Documented as a fact about the record itself, checkable against the "
               "Registry rows and the vendored files they name. The 133 years run from Cyprian's martyrdom "
               "(258) to Augustine's ordination (391), as Doc_01 fixes them. The texts written at and just "
               "after Cyprian's martyrdom stand at the very start of that span: the Acta Cypriani (rows "
               "41, 194, 231 no. 13 and 232 no. XI), Pontius's Life (rows 7, 40, 194 and 205), and the "
               "two martyr acts of rows 231 and 232. They belong to Cyprian's phase and do not fill the "
               "silence, and no source fixes their order. From them to Augustine's ordination, no source supplies a bishop's "
               "ordinary pastoral or congregational voice, or a congregation's voice, that continues "
               "Cyprian's. The Registry texts dated inside the span include Optatus of Milevis (rows 27, "
               "64 and 264) and the appendix documents (row 265); none continues Cyprian's voice, and this "
               "world draws on none of them for a claim. The licensed exceptions are named at Doc_02 §7. "
               "Layer 2's own sentence on how the inheritance was received carries the Reported-Experience "
               "Status marker (Constitution Article 17; Forces Framework §3): reported as the world's own "
               "self-understanding, not assessed for historical accuracy."
             )),
        [],
        "Re-derived from the approved Doc_08 §3 Force 3B-2 (Cell 3B, Ending/Internal; Transmission "
        "dimension). relations[] carries only the force<->force edges (2B-4, 2B-5) named above -- "
        "deliberately no gravity<->force edge, matching Force 2B-5's own identical disposition. "
        "sources[] is deliberately empty -- this force's own evidentiary base is a fact about the "
        "absence of any Registry source supplying a bishop's ordinary pastoral or congregational voice in an interval, not a citable vendored text making a claim; "
        "see this script's own docstring, THREE DISCLOSED EMPTY-SOURCES CASES.",
    )


def main() -> None:
    build_gravities()
    build_forces()
    print(f"Wrote {len(WRITTEN)} records:")
    for p in WRITTEN:
        print(f"  {p}")


if __name__ == "__main__":
    main()
