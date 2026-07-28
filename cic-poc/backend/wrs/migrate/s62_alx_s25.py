"""S6.2 S2.5-equivalent - Alexandria gravity + force records, FEC conversion,
world_core close.

Gravities: Doc_04's nine confirmed (C1-C5, T1-T4) plus the six not-advanced
candidates (three Formation Dynamics D-A/D-B/D-C; Logikos L-1, Askesis L-2,
Restoration L-3) per the schema's "not-advanced kept as required records"
rule - Alexandria is the first world where that rule has a non-empty
extension. Six-test keys are Doc_04's own names (CO-P2-02). C1-C5 verdicts
condensed-verbatim from Doc_04 SS3.1-3.5; T1-T4 are carried at summary
verdict in Doc_04 SS3.6 with the full explicit grid in the companion
Gravity_Index.xlsx Candidates sheet - that grid is ABSORBED here (verdict
cells verbatim) ahead of the companion-index deletion, as are the four
tension-pair matrix cells (T1-T2, T1-T3, T2-T3, T2-T4 R) and C3-C5 R that
the Doc_04 SS6 prose summary does not itemize (SS6's own scope note: "Full
pairwise coverage (the companion Gravity_Index.xlsx carries this as a
grid; prose summary here)").

interaction[] is built from a single PAIRS list so every edge is emitted
with its mirror by construction: R -> reinforcing both ways (symmetric);
X -> reshaping both ways, matching the grid's symmetric X cells, with the
honest direction of reshaping stated in the notes (the gate treats
reshaping as linkage-reciprocal, and the mutual typing is grid-faithful,
not invented); C/X -> competing with the schema's changes_to/at notation
(the notation the schema comment names as "the Alexandria changes_to/at
notation" - its first use).

Forces: Doc_08's eighteen entries (1A-1..3, 1B-1..3, 2A-1..4, 2B-1..3,
3A-1..2, 3B-1..3 - including both numbered transmission forces), three
layers condensed-verbatim with citations, plus the NEW Layer 4
(elaboration or considered stasis). connections[] carries force<->force
cross-cell links only (Doc_08 SS4's force-to-force rows, each mirrored);
force->gravity tracing lives verbatim in layer_formation_impact - the
Desert S2.5 rationale carried: a gravity record cannot type a back-edge to
a force (interaction[] is enum-typed gravity-to-gravity), and Doc_08 SS5's
synthesis table stays renderable as a view from the Layer-3 texts.

FEC conversion (CO-P2-04): the ten S2.4 story-body parkings convert to
typed gravity_links[] - first link's note holds the Formation Ecology
Connection verbatim; later links point back to it. Story004's FEC names NO
confirmed gravity by design (it marks the cross-build boundary the build
holds open, Doc_01 SS3.3); it links to alexgrav014 (Askesis, not-advanced,
whose index row is exactly that held-open cross-build entry) so the FEC
still renders - declared in the checkpoint artifact, not smuggled.

world_core: alexcore001.gravities -> the NINE confirmed ids only. The six
not-advanced records exist in the store but are not the world's gravities
(Doc_04 SS4 classifies them "not a gravity"/"Formation Dynamic") - the
deliberate divergence from Desert, where all ten candidates classified.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
sys.path.insert(0, str(BACKEND))
sys.path.insert(0, str(HERE))

import yaml
from s62_alx_source_rows import emit_record

OUT = BACKEND / "wrs" / "records" / "alexandria_world"

COMMON_G = {"world_id": "alexandria-catechetical", "record_type": "gravity",
            "schema_version": 1, "jobs": [5], "register": "etic",
            "review_state": "draft",
            "sources": [{"source_id": "srcALX001"}, {"source_id": "srcALX002"},
                        {"source_id": "srcALX003"}]}


def T(rep, dep, form, expl, pers, inter):
    # CO-P2-02: keys are Doc_04's own test names
    return {"repetition": {"verdict": rep},
            "dependency": {"verdict": dep},
            "formation": {"verdict": form},
            "explanatory": {"verdict": expl},
            "persistence": {"verdict": pers},
            "interaction": {"verdict": inter}}


def T_INDEX(row, basis, pers, inter):
    """T1-T4: Doc_04 SS3.6 carries summary verdicts; the full explicit
    grid is the Gravity_Index Candidates row (all six cells PASS),
    absorbed here. Persistence and Interaction carry the SS3.6/SS6
    substance the prose does state per-tension."""
    cite = (f"PASS - Gravity_Index Candidates row {row} (the full explicit "
            f"six-test grid, absorbed at S2.5); Doc_04 SS3.6 basis: {basis}")
    return {"repetition": {"verdict": cite},
            "dependency": {"verdict": cite},
            "formation": {"verdict": cite},
            "explanatory": {"verdict": cite},
            "persistence": {"verdict": "PASS - " + pers},
            "interaction": {"verdict": "PASS - " + inter}}


NOT_CARRIED = ("Not carried (Gravity_Index Candidates cell '-', absorbed at "
               "S2.5): testing stopped at the decisive criterion")


def T_NA(**cells):
    """Not-advanced candidates: the index's own cell values verbatim;
    '-' cells recorded as not-carried, not fabricated."""
    out = {}
    for k in ("repetition", "dependency", "formation", "explanatory",
              "persistence", "interaction"):
        out[k] = {"verdict": cells.get(k, NOT_CARRIED)}
    return out


GRAVITIES = [
 dict(id="alexgrav001", name="Scripture as Deep Formative Reality (C1)",
      classification="Primary",
      six_tests=T(
       "PASS (strong) - recurs across Streams 1, 2, 3, 4, 5; four partly-independent figures (Clement, Origen, Didymus, Athanasius); all three phases (Doc_04 SS3.1).",
       "PASS (strong) - the teaching tradition, the hermeneutical habit, catechetical formation, the worship-lectionary, and the Rule of Faith all collapse without Scripture as the formative instrument (Doc_04 SS3.1).",
       "PASS (strong) - Scripture read at depth is HOW participants are shaped: the reader is transformed by the reading, not merely informed (Doc_04 SS3.1).",
       "PASS - explains the allegorical habit, the learning tradition, the worship shape, and the boundary disputes (largely disputes over READING) (Doc_04 SS3.1).",
       "PASS (strong) - all three phases; at Nicaea it ACQUIRES a doctrinal-witness dimension (Scripture as ground of the homoousian argument) - an inflection, not a fracture (Doc_04 SS3.1).",
       "PASS (strong) - the primary VEHICLE of C2, C3, C4, C5 (reinforcing/instrumental; Doc_04 SS3.1, SS6)."),
      confidence_crosscheck="CONSISTENT, with two flagged divergences (Doc_04 SS3.1): core claim ('Scripture is deeply formative') Widely Accepted - carried by Stream 4 and by the non-Origen evidence WITHIN the literate stratum (Clement earlier, Athanasius/Didymus later); the systematized multilevel allegorical method is Origen-concentrated, capped at Dominant Modern Reconstruction for any ecology-wide method claim (Discipline One). STRATUM DIVERGENCE: confirmed Primary for the literate-attested ecology only; ecology-wide primacy held OPEN, not asserted (SS5, the Cross-Stratum Test - the declared Article-21 substitute; deferred to Article 31 external review)."),
 dict(id="alexgrav002", name="Transformation of the Soul Toward God (C2)",
      classification="Primary",
      six_tests=T(
       "PASS (strong) - Streams 4, 2, 3, 1, 12; three figures, all phases (Doc_04 SS3.2).",
       "PASS (strong) - a gravity in its own right, not the mere aggregate outcome of the others: the ACTIVE process (how the soul is changed), distinct from Theosis (the endpoint); the ascetic-prayer disciplines, the catechumenate's staged progression, and the purification->illumination->union language all depend on it (Doc_04 SS3.2).",
       "PASS (strong) - it IS formation named as such (Doc_04 SS3.2).",
       "PASS - explains why learning, worship, and Scripture-reading are FORMATIVE rather than merely instructive (Doc_04 SS3.2).",
       "PASS (strong) - all phases; at Nicaea the mechanism SHIFTS from a contemplative-ascent frame toward an Incarnation-grounded one (under Arian pressure) - more theologically robust, more communally accessible (Doc_04 SS3.2).",
       "PASS (strong) - reinforcing/instrumental pairing with C1, the organizing spine (Doc_04 SS3.2, SS6)."),
      confidence_crosscheck="CONSISTENT, divergences flagged (Doc_04 SS3.2): core conviction ('formation is transformation toward God') Widely Accepted (corroborated Clement->Athanasius + catechetical tradition + Stream 12 post-325); the contemplative-ascent mechanism is Origen-concentrated -> DMR. Its practice-cluster is the URBAN contemplative-ascetic-prayer set (Clement's Paedagogus, Origen's On Prayer, the catechumenal structure); the intensified desert versions are EXCLUDED (Discipline Two). Stratum divergence as for C1: literate-attested confirmed, ecology-wide held open."),
 dict(id="alexgrav003", name="Divine Pedagogy (C3)", classification="Supporting",
      six_tests=T(
       "PASS - Streams 2, 4, 5, 1 (Doc_04 SS3.3).",
       "PASS but reveals Supporting, not Primary status: removed while C1 and C2 remain, the practices persist but lose their EXPLANATORY GROUND - a meta-framework (God teaches through Scripture, catechesis, suffering), not an independent organizing force (Doc_04 SS3.3).",
       "PASS (Doc_04 SS3.3).",
       "PASS - it is the explanatory framework for the Primaries, not for phenomena of its own (Doc_04 SS3.3).",
       "PASS - all phases; at Nicaea the channel shifts teacher-mediated -> bishop-mediated (Doc_04 SS3.3).",
       "PASS (Doc_04 SS3.3)."),
      confidence_crosscheck="CONSISTENT (Doc_04 SS3.3): core Widely Accepted; Origen's systematic form DMR. Doc_04's own scope note carried: classified Supporting on its RELATIONSHIP TO THE PRIMARIES; any downstream 'always-present' salience is a Doc_05/deployment matter, not a re-classification - no Primary-equivalent status by the back door."),
 dict(id="alexgrav004", name="Logos-Centered Unity (C4)", classification="Supporting",
      six_tests=T(
       "PASS - across ~all streams (Doc_04 SS3.4).",
       "PASS - without it the ecology fragments into four disconnected domains (Doc_04 SS3.4).",
       "PASS (Doc_04 SS3.4).",
       "PASS (Doc_04 SS3.4).",
       "PASS - major homoousian inflection at Nicaea: the settlement gives the integrating center more secure theological ground against the Arian account (holds, does not fracture) (Doc_04 SS3.4).",
       "PASS - the super-integrator: R to C1, C2, C3, C5 (Doc_04 SS3.4, SS6)."),
      confidence_crosscheck="CONSISTENT (Doc_04 SS3.4): integrating-center function Widely Accepted (all three figures); Origen's specific Logos COSMOLOGY DMR. Classified Supporting DESPITE 6/6 PASS, on the principled practice-cluster criterion: the Logos produces no distinct practice-cluster of its own - it is the theological center that makes the other gravities cohere into one ecology rather than four activities (Supporting-type-(b): the integrating center)."),
 dict(id="alexgrav005", name="Learning-Formation Integration (C5)", classification="Supporting",
      six_tests=T(
       "PASS with caveats on temporal distribution (Doc_04 SS3.5).",
       "PASS within the school period only (Doc_04 SS3.5).",
       "PASS within the school period only (Doc_04 SS3.5).",
       "PASS within the school period only (Doc_04 SS3.5).",
       "PARTIAL PASS - assessed first, the critical test: strongly operative early/mid (c. 150-254) but significantly attenuated in the late horizon - a persistence FAILURE for the full-horizon ecology-wide claim, a pass for the school-period claim; major Nicaea inflection (teacher-authority -> bishop-authority) (Doc_04 SS3.5).",
       "PASS within the school period only (Doc_04 SS3.5, SS6)."),
      confidence_crosscheck="CONSISTENT (Doc_04 SS3.5): Widely Accepted for the early/mid school-tradition claim; DMR for any ecology-wide claim; Inferential-Thin across non-literate/Coptic/rural believers. The SHARPEST strength/confidence divergence in Doc_04 - apparently strong, but a persistence failure past c. 300 and the most Author-Gravity-vulnerable of all (Doc_02 names it the most Clement/Origen-concentrated). The one gravity notated as receding/fracturing under later forces (the Origen-Demetrius disruption, the Arian-era shift toward doctrinal-episcopal formation)."),
 dict(id="alexgrav006", name="Teacher-Bishop Authority Tension (T1)", classification="Tensional",
      six_tests=T_INDEX("T1",
       "poles are the teacher's authority (demonstrated wisdom) vs. the bishop's (office/succession); institutional separation is real (Pantaenus/Clement teaching alongside the episcopate; Didymus alongside Athanasius); Eusebius screen applied - re-grounded onto structural coexistence, NOT the Eusebius-mediated Origen-Demetrius episode (retained as illustration, not foundation); tests PASS on the structural evidence.",
       "persists across the horizon; at Nicaea the tension becomes more asymmetric, bishop-pole dominant (Doc_04 SS3.6, SS6 temporal note).",
       "R with C5 (the teacher-authority pole IS the school-formation C5 names) and with T2, T3 (grid cells, absorbed) (Doc_04 SS6 + Gravity_Index Interaction Matrix)."),
      confidence_crosscheck="Widely Accepted (structural); the Origen-Demetrius specifics DMR/HIGH-risk (Doc_04 SS3.6). Eusebius screen carried: confirmation rests on the structural coexistence evidence; the mid-horizon episode is illustration only (Doc_04 SS7)."),
 dict(id="alexgrav007", name="Learning-Community (School-Breadth) Tension (T2)", classification="Tensional",
      six_tests=T_INDEX("T2",
       "poles are the depth-formation available to the school-tradition student vs. the breadth-formation of the whole worshipping community (population separation); the ECOLOGICAL form of the stratum-bias problem - the ecology itself held the tension the evidence now makes hard to see from the community side.",
       "persists across the horizon; at Nicaea becomes more asymmetric (community-breadth pole growing dominant under episcopal formation) (Doc_04 SS3.6, SS6 temporal note).",
       "X with C5 (C5 attenuates precisely because it IS the authority-side of T2 becoming more asymmetric); R with T1, T3, T4 (grid cells, absorbed) (Doc_04 SS6 + Gravity_Index Interaction Matrix)."),
      confidence_crosscheck="The school pole Widely Accepted; the community pole Inferential-Thin (Doc_04 SS3.6) - the community pole is the held-open majority gap (SS5: Doc_05 must reconstruct the majority's formation as a NAMED GAP, not fill it)."),
 dict(id="alexgrav008", name="Speculative-Freedom vs Doctrinal-Boundary (T3)", classification="Tensional",
      six_tests=T_INDEX("T3",
       "poles are the tradition's speculative daring (Origen) vs. its boundary-drawing (homoousios, the anti-Origenist reaction); practice/institutional separation across time; Eusebius screen applied - the mid-horizon instance (Origen-Demetrius) is HIGH-risk and thin, so confirmation is deliberately SHIFTED to the late-horizon evidence (the homoousian boundary, the Origenist controversy), well-attested and independent of Eusebius; PASS on that basis.",
       "persists; crystallizes at Nicaea, boundary pole dominant (Doc_04 SS3.6, SS6 temporal note).",
       "X with C2 (the homoousian/Arian pressure of the boundary pole reshapes C2's mechanism); R with C4 (the homoousian settlement re-grounds the integrating center); R with T1, T2 (grid cells, absorbed) (Doc_04 SS6 + Gravity_Index Interaction Matrix)."),
      confidence_crosscheck="Late-horizon Widely Accepted (Eusebius-independent); mid-horizon HIGH-risk/thin (Doc_04 SS3.6). The world's relationship to Origen (inheritance and unease held together within the horizon, Doc_01 SS9) is a WORLD-LEVEL feature recorded as a property of the ecology, NOT a Representative instruction (Doc_04 SS3.6, carried verbatim)."),
 dict(id="alexgrav009", name="Martyrdom-as-Formation vs Contemplative-Ascent (T4)", classification="Tensional",
      six_tests=T_INDEX("T4",
       "poles are the martyr's witness (Streams 8; Leonides, the Decian and Diocletianic persecutions, the Coptic martyrological tradition) vs. contemplative ascent (Streams 1, 4); practice/population separation; martyrdom is the ONE confirmed formation mode not limited to the literate stratum, but its interior is Tier-3 hagiography / Coptic martyrology, held at Inferential-Thin.",
       "persists while persecution lasts; at Nicaea (persecution ending in Egypt) the martyrdom pole RECEDES to episodic/memory form (Doc_04 SS3.6, SS6).",
       "C changing to X with C2 (competing formation modes; after Nicaea T4 recedes - reshaping toward memory); R with T2 (grid cell, absorbed) (Doc_04 SS6 + Gravity_Index Interaction Matrix)."),
      confidence_crosscheck="Contemplative pole Widely Accepted; martyr interior Inferential-Thin (Doc_04 SS3.6). Cross-stratum note carried: the martyr pole is the one gravity evidence that plausibly crosses strata (SS5) - the whole community's formation mode, interior unnarratable."),
 # ---- not-advanced (Gravity_Index Candidates rows D-A/D-B/D-C, L-1/L-2/L-3, absorbed) ----
 dict(id="alexgrav010", name="Participation<->Perception Dynamic (D-A; Formation Dynamic, not a gravity)",
      classification="not-advanced",
      six_tests=T_NA(repetition="(described) - Gravity_Index Candidates D-A, absorbed at S2.5.",
                     dependency="FAIL (independent) - the decisive criterion: it is the MECHANISM of the C1<->C2 pairing, not an organizer (Doc_04 SS4; Gravity_Index D-A)."),
      confidence_crosscheck="Mechanism of the C1<->C2 pairing, not an organizer (Gravity_Index D-A; Doc_04 SS6: 'the Participation<->Perception dynamic is the MECHANISM of this pairing'). Author-Gravity: Origen-concentrated (flagged at generation)."),
 dict(id="alexgrav011", name="Theosis as Horizon (D-B; Formation Dynamic, not a gravity)",
      classification="not-advanced",
      six_tests=T_NA(repetition="(attested) - Gravity_Index Candidates D-B, absorbed at S2.5; the decisive finding: not an organizer (horizon-concept) (Doc_04 SS4)."),
      confidence_crosscheck="Widely Accepted (urban trio); the Evagrian developed form is desert-attributed and EXCLUDED (Discipline Two) (Gravity_Index D-B). The eschatological dimension of C2 - the endpoint, where C2 is the active process (Doc_04 SS3.2, SS4)."),
 dict(id="alexgrav012", name="Individual-Communal Integration (D-C; Formation Dynamic, not a gravity)",
      classification="not-advanced",
      six_tests=T_NA(interaction="No pole separation (a polarity within each believer, not a tension between populations) - the decisive criterion for Tensional status. Placement note: Doc_04 SS4 carries this as the candidate's six-test-verdict cell (the pole-separation criterion is defined at SS3.6); the Gravity_Index D-C row carries the same finding in its Cross-Stratum cell - both absorbed, neither invented."),
      confidence_crosscheck="Integrated by the ecology (catechumenate, assembly), not held as a tension (Gravity_Index D-C; Doc_04 SS4: 'Formation Dynamic (integrated)')."),
 dict(id="alexgrav013", name="Logikos / Rational Nature (L-1; not a gravity)",
      classification="not-advanced",
      six_tests=T_NA(dependency="FAIL (independent) - the decisive criterion (Doc_04 SS4; Gravity_Index L-1)."),
      confidence_crosscheck="Anthropological presupposition OF the gravities, not one of them (Gravity_Index L-1; Doc_04 SS4). Author-Gravity: Origen-adjacent. A governed CT term (Doc_03/Doc_06) whose term record is a separate S2.9 decision - this gravity-candidate record is not that term record."),
 dict(id="alexgrav014", name="Askesis / Asceticism (L-2; not a gravity - urban supporting practice)",
      classification="not-advanced",
      six_tests=T_NA(dependency="Not confirmed (urban only) - the decisive criterion: the developed form is desert-attributed and held open cross-build (Doc_04 SS4, SS7; Gravity_Index L-2)."),
      confidence_crosscheck="Urban practice Widely Accepted; developed form desert-attributed, held open (cross-build) (Gravity_Index L-2). Doc_04 SS7 carried: Alexandria has NOT claimed Askesis/Theosis-developed/the ascetic-technical vocabulary as its own; no ecology-wide Alexandrian gravity rests on the desert cluster."),
 dict(id="alexgrav015", name="Restoration (L-3; not a gravity - dimension of C2)",
      classification="not-advanced",
      six_tests=T_NA(dependency="Folds into C2 - the decisive criterion (Doc_04 SS4; Gravity_Index L-3)."),
      confidence_crosscheck="Restorative character of C2, not independent (Gravity_Index L-3); the restorative conviction Widely Accepted, SEPARABLE from Apokatastasis (Doc_04 SS7: 'Restoration stands as a term'). Author-Gravity: Origen-adjacent."),
]

# ---- interaction matrix: one PAIRS row -> both directional edges ----
# (a, b, type, note_ab, note_ba); type "R" / "X" / "C/X".
# Grid cells verbatim from Gravity_Index Interaction Matrix (absorbed);
# prose-named cells cite Doc_04 SS6.
G = {"C1": "alexgrav001", "C2": "alexgrav002", "C3": "alexgrav003",
     "C4": "alexgrav004", "C5": "alexgrav005", "T1": "alexgrav006",
     "T2": "alexgrav007", "T3": "alexgrav008", "T4": "alexgrav009"}

GRID_ONLY = ("Gravity_Index Interaction Matrix grid cell (absorbed at S2.5; "
             "Doc_04 SS6's prose summary does not itemize this cell - the "
             "grid is the declared full pairwise coverage).")

PAIRS = [
 ("C1", "C2", "R",
  "Doc_04 SS6: the organizing spine - Scripture is the primary vehicle THROUGH WHICH transformation operates; transformation is WHAT the reading is for. Where both are present and mutually reinforcing, 'the ecology is operating normally'; where only one is present, it is under strain (the governing frame for Doc_05). The Participation<->Perception dynamic (alexgrav010) is the mechanism of this pairing.",
  "(mirror - the organizing spine, Doc_04 SS6.)"),
 ("C1", "C3", "R",
  "Doc_04 SS6: Divine Pedagogy explains WHY Scripture forms.",
  "(mirror, Doc_04 SS6.)"),
 ("C1", "C4", "R",
  "Doc_04 SS6: Scripture is where the Logos is named and encountered; the Logos is the ground that makes Scripture formative.",
  "(mirror; C4 as super-integrator, Doc_04 SS6.)"),
 ("C1", "C5", "R",
  "Doc_04 SS6: the school is a SCHOOL OF SCRIPTURE.",
  "(mirror, Doc_04 SS6.)"),
 ("C2", "C3", "R",
  "Doc_04 SS6: the framework that makes transformation progressively intelligible.",
  "(mirror, Doc_04 SS6.)"),
 ("C2", "C4", "R",
  "Doc_04 SS6: the Logos is what the soul is transformed INTO THE LIKENESS OF.",
  "(mirror; C4 as super-integrator, Doc_04 SS6.)"),
 ("C2", "C5", "R",
  "Doc_04 SS6: learning serves transformation (wisdom is both a stage and evidence of it).",
  "(mirror, Doc_04 SS6.)"),
 ("C2", "T3", "X",
  "Doc_04 SS6 X cell; the reshaping runs T3->C2: the homoousian/Arian pressure of T3's boundary pole reshapes C2's mechanism (contemplative-ascent -> Incarnation-grounded). This edge is the symmetric grid cell's mirror-half; direction stated here, not re-typed.",
  "Doc_04 SS6 X cell, reshaping direction T3->C2: the boundary pole's pressure reshapes C2's mechanism at Nicaea."),
 ("C2", "T4", "C/X",
  "Doc_04 SS6 (T4<->C2 'C->X'): martyrdom and contemplative-ascent compete as formation modes; after Nicaea T4 recedes (reshaping toward memory). First use of the schema's changes_to/at notation.",
  "Doc_04 SS6 (T4<->C2 'C->X'): the two competing pictures of a completed formed life; post-Nicaea the martyrdom pole recedes to memory - competition reshaped."),
 ("C3", "C4", "R",
  "Doc_04 SS6: C4 is the explanatory ground for C3 (super-integrator).",
  "(mirror, Doc_04 SS6.)"),
 ("C3", "C5", "R", GRID_ONLY, "(mirror - " + GRID_ONLY + ")"),
 ("C4", "C5", "R",
  "Doc_04 SS6: C4 super-integrator - R to C1, C2, C3, C5.",
  "(mirror, Doc_04 SS6.)"),
 ("C4", "T3", "R",
  "Doc_04 SS6: the homoousian settlement (T3's boundary pole) is the same event that re-grounds C4's integrating center.",
  "(mirror, Doc_04 SS6.)"),
 ("C5", "T1", "R",
  "Doc_04 SS6: the teacher-authority pole is the school-formation that C5 names.",
  "(mirror, Doc_04 SS6.)"),
 ("C5", "T2", "X",
  "Doc_04 SS6 X cell; the reshaping runs T2->C5: C5 attenuates precisely because it IS the authority-side of T2 becoming more asymmetric. Symmetric grid cell's mirror-half; direction stated, not re-typed.",
  "Doc_04 SS6 X cell, reshaping direction T2->C5: the tension's post-Nicene asymmetry is what attenuates C5."),
 ("T1", "T2", "R", GRID_ONLY + " Shared substrate: Doc_08 2B-2 carries both tensions as one ongoing internal force.",
  "(mirror - " + GRID_ONLY + ")"),
 ("T1", "T3", "R", GRID_ONLY, "(mirror - " + GRID_ONLY + ")"),
 ("T2", "T3", "R", GRID_ONLY, "(mirror - " + GRID_ONLY + ")"),
 ("T2", "T4", "R", GRID_ONLY, "(mirror - " + GRID_ONLY + ")"),
]

TYPE_MAP = {"R": "reinforcing", "X": "reshaping"}


def build_interactions():
    edges = {gid: [] for gid in G.values()}
    for a, b, t, note_ab, note_ba in PAIRS:
        if t == "C/X":
            extra = {"changes_to": "reshaping",
                     "at": "Nicaea (325) - persecution ends in Egypt; the martyrdom pole recedes to episodic/memory form (Doc_04 SS3.6, SS6)"}
            edges[G[a]].append({"type": "competing", "target_id": G[b],
                                "note": note_ab, **extra})
            edges[G[b]].append({"type": "competing", "target_id": G[a],
                                "note": note_ba, **extra})
        else:
            typ = TYPE_MAP[t]
            edges[G[a]].append({"type": typ, "target_id": G[b], "note": note_ab})
            edges[G[b]].append({"type": typ, "target_id": G[a], "note": note_ba})
    return edges


COMMON_F = {"world_id": "alexandria-catechetical", "record_type": "force",
            "schema_version": 1, "jobs": [1, 5], "register": "etic",
            "review_state": "draft",
            "sources": [{"source_id": "srcALX001"}, {"source_id": "srcALX002"},
                        {"source_id": "srcALX003"}, {"source_id": "srcALX009"}]}

FORCES = [
 dict(id="alexforce1A1", name="The Philonic Inheritance (Force 1A-1)",
      six_cell_position="1A - Initiating / External",
      layer_historical_event="Philo of Alexandria (c. 20 BCE-50 CE) had already produced, in this same city, a synthesis of Jewish Scripture and Greek philosophy - allegorical reading through Platonic categories, and a Logos as cosmic mediator: the standing intellectual environment the Christian ecology was born into. Confidence: Widely Accepted (Runia 1993; van den Hoek 1988) (Doc_08 1A-1 L1).",
      layer_worlds_own_experience="The way of reading was as ready-to-hand as the Greek the community prayed and read in; the words for a Word who mediates between God and the world were already given, waiting. And when the community named the Word who had BECOME FLESH, those given words were put to a use they had never had before - the reading it had received now opened onto the One who had entered the world it read about (Doc_08 1A-1 L2).",
      layer_worlds_own_experience_cite=None,
      layer_formation_impact="The initiating condition of the Intellectual/Interpretive ecology and of Logos-Centered Unity (C4) - the ecology inherited its grammar rather than inventing it (Doc_08 1A-1 L3; SS4: 1A-1 + 1B-2 converge to produce C4 - neither force alone sufficient).",
      layer4={"elaboration": "The inherited grammar's condition changed by being taken up: what had been the city's standing intellectual environment became the constitutive architecture of a different community's formation - the given words permanently re-purposed around the Word made flesh, so that by the horizon's end the Philonic inheritance existed inside the ecology as its own theological ground, no longer merely around it (S2.5 Layer-4 authoring from Doc_08 1A-1 L2/L3)."},
      connections=[
        {"type": "converges-with", "target_id": "alexforce1B2",
         "note": "Doc_08 SS4: 1A-1 + 1B-2 converge to produce Logos-Centered Unity (C4) - the inherited Logos-grammar + its Johannine christological identification; neither alone sufficient."}]),
 dict(id="alexforce1A2", name="The Jewish Scriptural Inheritance - the Septuagint (Force 1A-2)",
      six_cell_position="1A - Initiating / External",
      layer_historical_event="The Greek Old Testament, produced in Alexandria (3rd-2nd c. BCE), was the ecology's primary formative text - received from outside, carrying Jewish interpretive questions. Confidence: Widely Accepted (Doc_08 1A-2 L1).",
      layer_worlds_own_experience="The Scriptures were simply THERE, in the tongue the city spoke, already the place where God was to be met - not chosen, but given, the ground under everything (Doc_08 1A-2 L2).",
      layer_formation_impact="The initiating textual condition of Scripture as Deep Formative Reality (C1) - there was a deep text to be read before there was a way of reading it (Doc_08 1A-2 L3; SS4: 1A-2 + 1B-2 converge to produce C1 - a deep text + the Word who speaks through it).",
      layer4={"elaboration": "The given text's condition changed from inheritance to organizing instrument: what arrived as the city's Jewish Scriptures became the lectionary, the school's curriculum, and - at Nicaea - the ground of the homoousian argument itself (C1's acquired doctrinal-witness dimension), the received book now bearing the weight of the community's whole formation and its drawn confession (S2.5 authoring from Doc_08 1A-2 L3 + Doc_04 SS3.1)."},
      connections=[
        {"type": "converges-with", "target_id": "alexforce1B2",
         "note": "Doc_08 SS4: 1A-2 + 1B-2 converge to produce C1 - a deep text + the Word who speaks through it."}]),
 dict(id="alexforce1A3", name="The Platonic Philosophical Environment - Middle Platonism (Force 1A-3)",
      six_cell_position="1A - Initiating / External",
      layer_historical_event="At the world's initiating moment (Clement arrives c. 180; Origen's peak c. 220s-230s), the sophisticated philosophical environment was Middle Platonism - Numenius, Albinus, and the shared Alexandrian teacher Ammonius Saccas - an account of the soul's graduated ascent to the highest reality that the school tradition formed itself alongside and against. (The same Platonic current MATURED into Plotinian Neoplatonism - Plotinus c. 204-270, Porphyry c. 234-305 - which becomes the ongoing rival at 2A-2.) Confidence: Widely Accepted (Doc_08 1A-3 L1, incl. its F3 chronology correction).",
      layer_worlds_own_experience="Here were others who took the soul's ascent to the highest reality with full seriousness, who spoke of purification and of a return to the One - close enough to be recognized as fellow-seekers, and yet reaching an ascent with no Word made flesh at its end (Doc_08 1A-3 L2).",
      layer_formation_impact="The initiating condition that made philosophical engagement constitutive rather than optional; sets up the ongoing philosophical challenge (2A-2). Also the philosophical environment C4 integrates against (Doc_08 1A-3 L3; SS5 C4 row, the F1-corrected connection).",
      layer4={"elaboration": "The initiating substrate itself changed character within the horizon: the fellow-seekers' current matured into an articulate institutional rival (2A-2), so the same external factor the world formed itself alongside became the one it had to say its difference from plainly - an initiating condition that did not stay initial (S2.5 authoring from Doc_08 1A-3 L1/L3 + SS4's 'matures into' row)."},
      connections=[
        {"type": "matures-into", "target_id": "alexforce2A2",
         "note": "Doc_08 SS4: the same external factor as environment (initiating) becoming an articulate rival (ongoing)."}]),
 dict(id="alexforce1B1", name="The Apostolic Formation Tradition (Force 1B-1)",
      six_cell_position="1B - Initiating / Internal",
      layer_historical_event="The inherited apostolic practices - baptism, Eucharist, catechesis, Scripture heard as formative address, shared communal life - received as the apostolic deposit, not invented in Alexandria. Confidence: Widely Accepted (Doc_08 1B-1 L1).",
      layer_worlds_own_experience="These were what had been handed down: the washing that made new, the shared bread, the teaching of those coming in - not the community's own devising but the faith received, to be kept and passed on whole (Doc_08 1B-1 L2).",
      layer_formation_impact="The initiating internal ground of Transformation-of-the-Soul (C2) and of the whole-community formation channel - the channel that reaches the non-literate majority: sacraments and shared life form before, and without, any school (Doc_08 1B-1 L3; SS4: 1B-1 + 1B-3 converge to produce C2 and C5; SS5 T2 row: the whole-community channel is T2's community pole).",
      layer4={"stasis": True,
              "elaboration": "Stasis, considered and meant: the deposit persisted unchanged as the whole-community channel across all three phases - and that unchangingness is the load-bearing fact. It is the robust channel (2B-3 Mechanism Two rides on it), the one formation path requiring no literacy and no teacher-student relationship, and the ecology's only reach into the majority the sources cannot see (OG-4). Nothing in the world's conditions reorganized it; everything else reorganized around it (S2.5 authoring from Doc_08 1B-1 L3 + SS7)."},
      connections=[
        {"type": "converges-with", "target_id": "alexforce1B3",
         "note": "Doc_08 SS4: 1B-1 + 1B-3 converge to produce Transformation (C2) and Learning-Formation Integration (C5) - received practice + the impulse to genuine knowing."}]),
 dict(id="alexforce1B2", name="The Johannine Logos Theology (Force 1B-2)",
      six_cell_position="1B - Initiating / Internal",
      layer_historical_event="John's Gospel identified the cosmic Logos with the one who became flesh; received as apostolic testimony, but Alexandria built its theological architecture on it more fully than any other community. Confidence: Widely Accepted (Doc_08 1B-2 L1).",
      layer_worlds_own_experience="The Word through whom all was made had entered flesh - and this was not one truth among many but the hinge on which everything turned, the given from which the whole of reading and worship and formation could be understood (Doc_08 1B-2 L2).",
      layer_formation_impact="The initiating internal ground of Logos-Centered Unity (C4) and of Scripture as Deep Formative Reality (C1) - the Logos is who Scripture speaks (Doc_08 1B-2 L3; SS4 convergences with 1A-1 and 1A-2).",
      layer4={"elaboration": "The hinge-conviction's condition changed from freely-held to boundary-defended: under the Neoplatonic rivalry its incarnate specificity had to be said plainly (2A-2), and under the Arian contest it was confessed within a drawn line (homoousios) - the same given truth, held at the end of the horizon with a precision and a cost it did not begin with (S2.5 authoring from Doc_08 1B-2 L3 + 2A-2/2A-4 L3)."},
      connections=[
        {"type": "converges-with", "target_id": "alexforce1A1",
         "note": "(mirror; Doc_08 SS4 - produces C4.)"},
        {"type": "converges-with", "target_id": "alexforce1A2",
         "note": "(mirror; Doc_08 SS4 - produces C1.)"},
        {"type": "intensified-by", "target_id": "alexforce2A2",
         "note": "(mirror of 2A-2's intensifies edge; Doc_08 SS4: forces the incarnate-Logos specificity into sharper articulation.)"}]),
 dict(id="alexforce1B3", name="The Formation Impulse Toward Genuine Knowledge of God (Force 1B-3)",
      six_cell_position="1B - Initiating / Internal",
      layer_historical_event="The conviction that Christian life meant genuinely KNOWING God - encountering divine reality through formation, not merely holding right beliefs - attested in Clement's Stromateis and Origen. Confidence: Widely Accepted for the school tradition; the impulse's presence in the broader community is Dominant Modern Reconstruction (Doc_08 1B-3 L1).",
      layer_worlds_own_experience="To believe was only the beginning; the soul was made to KNOW God, to be changed by that knowing, to go on being drawn deeper because the One it sought could not be exhausted (Doc_08 1B-3 L2).",
      layer_formation_impact="The initiating internal ground of the Transformation (C2) and Learning-Formation-Integration (C5) gravities, of the Divine Pedagogy conviction (C3 - God is always teaching the soul toward this knowing), and of the SPECULATIVE-FREEDOM pole of T3 (Doc_08 1B-3 L3; SS5 C3 and T3 rows - two of the three F-corrected added connections).",
      layer4={"elaboration": "The impulse's condition changed from open road to bounded road: what began as an unbounded drawing-deeper crystallized into T3's speculative-freedom pole, and after Nicaea it operated within a drawn confession - still the same impulse (the One it sought could not be exhausted), now exercised under boundary-maintenance it had not known at the founding (S2.5 authoring from Doc_08 1B-3 L3 + 2A-4 L2/L3)."},
      connections=[
        {"type": "converges-with", "target_id": "alexforce1B1",
         "note": "(mirror; Doc_08 SS4 - produces C2 and C5.)"}]),
 dict(id="alexforce2A1", name="The Gnostic Challenge, c. 150-300 CE (Force 2A-1)",
      six_cell_position="2A - Ongoing / External",
      layer_historical_event="Valentinian and Basilidean movements shared formal features with the school tradition - teachers, sophisticated Scripture engagement, gnosis claims - and were the ecology's most sustained early/mid-horizon boundary challenge. Confidence: Widely Accepted (Doc_08 2A-1 L1).",
      layer_worlds_own_experience="Here were rivals who spoke the same words - knowledge, Scripture, the soul's ascent - and meant something the community could not accept: a knowing for a secret few, a rejecting of the body and its Maker. The nearness was the danger; the community had to say what TRUE knowing was, and that it was for all (Doc_08 2A-1 L2).",
      layer_formation_impact="Pressed the ecology to build a POSITIVE account of formation available to the whole community (not an elite) - shaping the Knowledge/Gnosis vocabulary, the Flesh/Sarx vs Body/Soma distinction, and the Learning-Community tension T2 (formation owed to all, not only the school) (Doc_08 2A-1 L3; SS4 row).",
      layer4={"elaboration": "The challenge receded by the late horizon, but its pressure left permanent deposits: the reclaimed gnosis vocabulary, the formation-for-all account, and the boundary habit of saying what true knowing is - conditions the world kept after the rival that forced them had faded, so that the ecology's answer outlived the question's askers (S2.5 authoring from Doc_08 2A-1 L3; the vocabulary deposits are the S2.3 term records' own attested senses)."},
      connections=[]),
 dict(id="alexforce2A2", name="The Neoplatonic Philosophical Challenge, c. 200-350 CE (Force 2A-2)",
      six_cell_position="2A - Ongoing / External",
      layer_historical_event="As Neoplatonism matured under Plotinus and Porphyry it became an articulate institutional rival - schools, teacher-student structure - offering ascent without Incarnation, sacraments, or community. Confidence: Widely Accepted (Doc_08 2A-2 L1).",
      layer_worlds_own_experience="The fellow-seekers of the ascent had become a rival school, and the difference had to be said plainly: the ascent the community knew ran through a Word who had come DOWN, through flesh and sacrament and shared life - not the soul climbing alone (Doc_08 2A-2 L2).",
      layer_formation_impact="Sharpened the Christological specificity of Logos-Centered Unity (C4) - the descending, incarnate Logos, against the philosophers' impersonal One (Doc_08 2A-2 L3; SS4: intensifies 1B-2 / C4).",
      layer4={"elaboration": "The rivalry's product outlasted its occasion: the descending-Logos specificity it forced into articulation became a permanent feature of the world's confession (carried into the homoousian settlement), while the rival school itself persisted past the horizon - the world's conditions changed not by the rival's defeat but by what answering it built (S2.5 authoring from Doc_08 2A-2 L3 + 2A-4 L3)."},
      connections=[
        {"type": "matured-from", "target_id": "alexforce1A3",
         "note": "(mirror of 1A-3's matures-into edge; Doc_08 SS4.)"},
        {"type": "intensifies", "target_id": "alexforce1B2",
         "note": "Doc_08 SS4: forces the incarnate-Logos specificity into sharper articulation."}]),
 dict(id="alexforce2A3", name="Episodic Persecution, c. 165-311 CE (Force 2A-3)",
      six_cell_position="2A - Ongoing / External",
      layer_historical_event="Antonine, Severan, Decian (249-251), and Diocletianic (303-311) persecutions; the Decian and Diocletianic most formation-significant. Origen was imprisoned and tortured under Decius; his father Leonidas was martyred under Septimius Severus. Confidence: Widely Accepted / Documented (the persecutions as events) (Doc_08 2A-3 L1).",
      layer_worlds_own_experience="The threat, when it came, was not first a danger to be survived but the moment of testing - when what formation had built in the soul was either equal to the ultimate choice or was not; and the one who chose death over denial showed, in a moment, what the long forming had been for (Doc_08 2A-3 L2).",
      layer_formation_impact="Intensified the MARTYRDOM pole of T4 and gave it explicit formation literature (Origen's Exhortation to Martyrdom); reinforced Divine Pedagogy C3 (God teaching through suffering). Stratum note: martyrdom is the one formation mode reaching every stratum; its interior is Tier-3 hagiography - Inferential-Thin (Doc_08 2A-3 L3, carrying Doc_04 T4).",
      layer4={"elaboration": "The force ended within the horizon: with persecution's end in Egypt (the Diocletianic, 303-311, the last - Doc_08 2A-3 L1) the moment of testing ceased to be structurally available, and the martyrdom pole of T4 receded to episodic and memory form - the one formation mode that had reached every stratum surviving thereafter as remembered witness (the Coptic martyrological tradition, Doc_04 SS3.6 T4; the martyr-era reckoning attested as alexstory009's occasion) rather than as live possibility (S2.5 authoring from Doc_08 2A-3 L3 + Doc_04 SS3.6 T4)."},
      connections=[]),
 dict(id="alexforce2A4", name="The Arian Controversy, c. 318-381 CE - highest formation impact (Force 2A-4)",
      six_cell_position="2A - Ongoing / External",
      layer_historical_event="Arius (c. 256-336) taught the Son as the highest creature ('there was when he was not'); the controversy produced Nicaea (325), the homoousios, and Athanasius's decades of Nicene defense (bishop 328-373, exiled five times). Confidence: Widely Accepted (Doc_08 2A-4 L1).",
      layer_worlds_own_experience="This time the danger was not from outside but from within - brothers contesting the very confession of the Word, so that what had been held loosely now had to be held within a drawn line. The settlement was relief and burden at once: the Word confessed of one substance, and the freedom to explore now bounded (Doc_08 2A-4 L2).",
      layer_formation_impact="Forced the Transformation gravity's (C2) INCARNATION-GROUNDED configuration into dominance (promoting an already-available account, not creating one); crystallized the DOCTRINAL-BOUNDARY pole of T3; began the boundary shift from external to internal threat (Doc_08 2A-4 L3; SS4 row).",
      layer4={"elaboration": "The drawn line became a standing condition: after Nicaea the world's formation operates inside a confessed boundary - C2's mechanism Incarnation-grounded, T3's boundary pole dominant, the threat-direction permanently turned inward - the highest-impact reorganization of conditions any ongoing force produced within the horizon (S2.5 authoring from Doc_08 2A-4 L2/L3 + 3B-2 L3)."},
      connections=[]),
 dict(id="alexforce2B1", name="Scripture as Deep Formative Reality operating as ongoing internal force (Force 2B-1)",
      six_cell_position="2B - Ongoing / Internal",
      layer_historical_event="The continuous organization of the whole formation life around Scripture as the primary formative instrument - attested by the scale of Clement's, Origen's, and the liturgy's engagement. Confidence: Widely Accepted (the ecology-wide METHOD claim is DMR - Origen-concentrated) (Doc_08 2B-1 L1).",
      layer_worlds_own_experience="The text was never a thing one could finish. Every genuine reading opened a depth the last had not reached, because the Word who speaks through it is always more than any hearing has received - so the forming was never done, and the reader went on being drawn in (Doc_08 2B-1 L2).",
      layer_formation_impact="Sustains the first Primary gravity (C1) throughout the horizon; the ongoing force that keeps the ecology organized around reading-at-depth (Doc_08 2B-1 L3; SS5 C1 row: produced by 1A-2 + 1B-2, sustained by 2B-1, carried onward by 2B-3/3B-3).",
      layer4={"stasis": True,
              "elaboration": "Stasis as the finding: the ongoing organization around reading-at-depth persisted unchanged across the whole horizon - the Nicaea inflection (Scripture acquiring its doctrinal-witness dimension) ADDED a register without reorganizing the practice ('an inflection, not a fracture', Doc_04 SS3.1). Continuity is what this force contributes; the changes belong to the forces that pressed on it (S2.5 authoring from Doc_08 2B-1 L3 + Doc_04 SS3.1)."},
      connections=[]),
 dict(id="alexforce2B2", name="The Teacher-Bishop / Learning-Community Tension as ongoing internal force (Force 2B-2)",
      six_cell_position="2B - Ongoing / Internal",
      layer_historical_event="The continuously operative tension between authority grounded in recognized wisdom (the teacher) and authority grounded in apostolic office (the bishop) - and, socially, between the depth the school offers the few and the breadth owed to the whole community. The Origen-Demetrius episode (c. 230s) is its most documented acute expression. Confidence: Widely Accepted as a structural tension; the Origen-Demetrius details are DMR (Eusebius-mediated; HIGH Author-Gravity noted at Layer 1, not carried into Layer 2) (Doc_08 2B-2 L1).",
      layer_worlds_own_experience="Two things were true at once and could not be made one: the teacher who could be trusted because others saw that he saw, and the bishop who held the office handed down from the apostles; and beneath it, the knowing that the depth the school could give the few was not the way most of the community was being formed. Both were real; neither could be given up (Doc_08 2B-2 L2).",
      layer_formation_impact="The ongoing internal force underlying BOTH the Teacher-Bishop (T1) and Learning-Community (T2) tensional gravities (Doc_08 2B-2 L3; SS5 T1 row: 'is 2B-2').",
      layer4={"elaboration": "The tension's condition changed direction without resolving: the Origen-Demetrius rupture (3B-1) and the post-Nicene reconfiguration (3B-2) drove both of its faces toward the office/whole-community poles, so that what had been a productive, unstable coexistence ended the horizon as a settled asymmetry - held, but no longer level (S2.5 authoring from Doc_08 2B-2 L3 + 3B-1/3B-2 L3)."},
      connections=[]),
 dict(id="alexforce2B3", name="Transmission, Ongoing / Internal - a named force (Force 2B-3)",
      six_cell_position="2B - Ongoing / Internal (Transmission Specificity Principle)",
      layer_historical_event="How the ecology passed itself on within the horizon, through three mechanisms of differing robustness. Mechanism One - the teacher-student formation relationship: the interpretive tradition passed only through the relationship that produces perceptual capacity, genuinely transmissible only through accompaniment that opens the student's own seeing (the Pantaenus->Clement->Origen line carried it across three generations). Mechanism Two - the sacramental practices: baptism, Eucharist, the liturgical and Paschal calendar, passed through ongoing communal practice - MORE ROBUST, needing no teacher-student relationship, sustained by the bishop's governance. Mechanism Three - the Rule of Faith and (later) the Nicene Creed: passed as formal memory - more precise and more brittle. Confidence: Widely Accepted (the mechanisms; succession particulars DMR / Eusebius-mediated) (Doc_08 2B-3 L1).",
      layer_worlds_own_experience="The teacher who had truly received also knew the giving could fail - that the one before him might hear the words and not begin to SEE, might carry the school's learning without the depth that had produced it; the most irreplaceable thing he carried was the very thing no method could hand over, only the slow relationship that might or might not open the eyes (Doc_08 2B-3 L2, Reported-Experience Status).",
      layer_formation_impact="Transmission is a force shaping what survives: the interpretive capacity (most valuable, most fragile) vs. the sacramental practice (robust, reaching all) vs. the creed (precise, brittle) - the survivorship pattern that determines what the after-life of the world looks like (-> 3B-3). Carries C1 and C5 onward (Doc_08 2B-3 L3; SS5 C1/C5 rows, the F1-corrected connections).",
      layer4={"elaboration": "The differential itself is the condition change: as the horizon closed, the three mechanisms' unequal robustness hardened into the world's survivorship pattern - the fragile relationship-borne capacity already failing where the robust sacramental and brittle creedal channels held - so the ongoing force's own structure became the ending force's story (S2.5 authoring from Doc_08 2B-3 L3; the 'becomes' of SS4)."},
      connections=[
        {"type": "becomes", "target_id": "alexforce3B3",
         "note": "Doc_08 SS4: the ongoing mechanisms' survivorship pattern becomes the after-life story."}]),
 dict(id="alexforce3A1", name="The Chalcedonian Fracture, 451 CE - distal, anticipatory pressure (Force 3A-1)",
      six_cell_position="3A - Ending / External",
      layer_historical_event="Chalcedon's two-natures definition split Egyptian Christianity into Chalcedonian and non-Chalcedonian (Miaphysite/Coptic) streams - a permanent communal fracture. Outside the c. 400 horizon; its ANTICIPATORY pressure (the pattern of unresolved doctrinal controversy) is felt within it. Confidence: Widely Accepted / Documented for the event; the pre-400 anticipatory pressure is DMR (Doc_08 3A-1 L1).",
      layer_worlds_own_experience="(Reported-Experience Status; the world within its horizon did not yet know this fracture:) the community knew only that contest over the confession, once begun, did not simply resolve - that a line drawn to defend the faith could also divide those who confessed it (Doc_08 3A-1 L2, incl. its F5 register correction).",
      layer_formation_impact="The eventual external fracture that ends this world's form (into Coptic and Chalcedonian streams) - the boundary the horizon deliberately stops before (Doc_08 3A-1 L3; Doc_01 SS2.3).",
      layer4={"stasis": True,
              "elaboration": "Stasis within the world's own window, considered: the fracture acts past the boundary; inside it there is only the learned pattern that drawn lines do not simply resolve - no in-window condition change is traceable to this force beyond that anticipation, and none is invented (S2.5 authoring from Doc_08 3A-1 L1/L2)."},
      connections=[]),
 dict(id="alexforce3A2", name="The Arab Conquest of Egypt, 641 CE - distal terminal force (Force 3A-2)",
      six_cell_position="3A - Ending / External",
      layer_historical_event="The conquest ended the institutional infrastructure that had sustained the ecology - Greek-speaking cultural dominance, the episcopal and school-sustaining environment. Confidence: Widely Accepted (Doc_08 3A-2 L1).",
      layer_worlds_own_experience="Not applicable: this force lies two and a half centuries beyond the world's own horizon; the world had no lived experience of it, so no Layer 2 is written - a deliberate proportionality exception, not an omission; the force is named only to give the transmission story its terminus (Doc_08 3A-2 L2, the stated exception).",
      layer_formation_impact="Brief, per Proportionality: the distal terminus of the after-life the transmission force (3B-3) traces - where the institutional carriers of the world's inheritance finally gave way (Doc_08 3A-2 L3).",
      layer4={"stasis": True,
              "elaboration": "Stasis within the world's own window: a wholly distal terminus; no in-window condition change - recorded exactly as Doc_08 scopes it, terminus and nothing more (S2.5 authoring)."},
      connections=[
        {"type": "terminus-of", "target_id": "alexforce3B3",
         "note": "(mirror of 3B-3's terminates-at edge; Doc_08 SS4: the internal transmission story ends where the external institutional infrastructure gave way.)"}]),
 dict(id="alexforce3B1", name="The Origen-Demetrius Conflict and Its Aftermath, c. 230s CE (Force 3B-1)",
      six_cell_position="3B - Ending / Internal",
      layer_historical_event="The Teacher-Bishop tension reaching acute institutional expression: Origen departed for Caesarea (c. 231-234), Demetrius condemned the irregular ordination, and the school tradition's most productive period was disrupted. Confidence: Widely Accepted as structural fact (the conflict occurred and produced disruption); the specific details are DMR (Eusebius-mediated, HIGH Author-Gravity - flagged at Layer 1 only) (Doc_08 3B-1 L1).",
      layer_worlds_own_experience="When the teacher and the office came to open conflict, the one whose seeing the school most prized was sent away, and a fruitfulness the community had known was broken - a wound within the household, not an attack from outside it (Doc_08 3B-1 L2).",
      layer_formation_impact="Reconfigured the Teacher-Bishop tension (T1) from a productive, unstable balance toward the office-pole; began the attenuation of Learning-Formation Integration (C5) (Doc_08 3B-1 L3; SS4 row).",
      layer4={"elaboration": "The rupture's condition change proved irreversible within the horizon: the balance never returned to level - T1's office-pole tilt and C5's attenuation both date from here, and the school's most productive configuration (teacher-led, speculative, integrated) never re-formed in Alexandria after it (S2.5 authoring from Doc_08 3B-1 L3 + 3B-2 L3)."},
      connections=[]),
 dict(id="alexforce3B2", name="The Post-Nicene Authority Reconfiguration, c. 325-400 CE (Force 3B-2)",
      six_cell_position="3B - Ending / Internal",
      layer_historical_event="The Nicene period made the bishop of Alexandria the enforcer of conciliar Christological orthodoxy across Egypt - a new doctrinal-boundary scope, with exile, letter-networks, and synods as instruments; Athanasius's Festal Letters paradigmatic. Confidence: Widely Accepted (Doc_08 3B-2 L1).",
      layer_worlds_own_experience="Authority now meant not only the office handed down but the drawn confession it was charged to guard, and to enforce across all the churches of Egypt; the teacher's kind of standing receded before it (Doc_08 3B-2 L2).",
      layer_formation_impact="Completed the Teacher-Bishop (T1) and Learning-Community (T2) asymmetries toward the office/whole-community poles; ATTENUATED/TERMINATED Learning-Formation Integration (C5) as an active organizing force; crystallized the doctrinal-boundary pole of T3 (Doc_08 3B-2 L3; SS4 row).",
      layer4={"elaboration": "The terminal internal condition change of the world's own form: episcopal-doctrinal formation became the organizing frame - T1 and T2 settled asymmetric, C5 ceased as an active organizer, T3's boundary pole crystallized - so the school-shaped ecology's distinctive configuration closed from within even as its Primaries (C1, C2) held (S2.5 authoring from Doc_08 3B-2 L3 + Doc_04 SS4/SS6)."},
      connections=[]),
 dict(id="alexforce3B3", name="Transmission, Ending / Internal - a named force (Force 3B-3)",
      six_cell_position="3B - Ending / Internal (Transmission Specificity Principle)",
      layer_historical_event="What passed beyond the horizon, what was lost, and what was transformed. TRANSMITTED: to Eastern Christianity broadly - the Nicene confession, the theosis horizon, the allegorical-Christological reading; to the Desert Christianity world (its most direct formation heir) - the impulse toward genuine knowledge of God, the contemplative-ascent model, the ascetic vocabulary [cross-build: the desert's world-attribution held open, Doc_01 SS3.3; Alexandria transmits toward it without claiming its formation logic]; to the Cappadocian synthesis - the Origen inheritance plus the Nicene settlement, held with more caution. LOST: the teacher-student formation relationship as the PRIMARY transmission mechanism (the most significant loss - the fragile-because-irreplaceable capacity of 2B-3 Mechanism One); and the school tradition's confident philosophical synthesis, worn down under boundary-maintenance pressure. TRANSFORMED: the Origen inheritance - transmitted but under contest, generating the Origenist controversies and the eventual conciliar condemnation of specific propositions (pre-existence, apokatastasis, grades of rational natures), yet never wholly suppressed. Confidence: Widely Accepted (the broad transmission lines; specific succession claims DMR) (Doc_08 3B-3 L1).",
      layer_worlds_own_experience="What the community had built most carefully - the opening of a student's sight through the long relationship - was precisely what it could not guarantee would outlast it; and the teacher whose perception it treasured passed on under a shadow, carried forward and loved and, in part, set outside the line (Doc_08 3B-3 L2, Reported-Experience Status).",
      layer_formation_impact="The transmission force determines the world's after-life: the robust sacramental and creedal inheritance survives; the fragile interpretive capacity is the great loss; the Origen inheritance is the great transformation - the ending-internal force that closes the world's own form. T3's site is here: the Origen transmission-under-contest (Doc_08 3B-3 L3; SS5 T3 row). Carries C1 and C5 onward/into loss (SS5, F1-corrected).",
      layer4={"elaboration": "The after-life fixed as condition: beyond the horizon the world exists as its robust remainders (creed, sacrament, the allegorical-Christological reading in other hands), its named loss (the relationship-borne interpretive capacity), and its contested treasure (the Origen inheritance, carried forward and loved and, in part, set outside the line) - the closing condition every later inheritor, the Desert world first among them, actually received (S2.5 authoring from Doc_08 3B-3 L1/L3)."},
      connections=[
        {"type": "became-from", "target_id": "alexforce2B3",
         "note": "(mirror of 2B-3's becomes edge; Doc_08 SS4.)"},
        {"type": "terminates-at", "target_id": "alexforce3A2",
         "note": "Doc_08 SS4: the internal transmission story ends where the external institutional infrastructure gave way."}]),
]

# ---- FEC -> gravity_links (CO-P2-04). First id = the FEC-verbatim link. ----
FEC_DELIM_START = "[Formation Ecology Connection"
BACK_NOTE = ("Named in this story's Formation Ecology Connection - full text "
             "on the first gravity_links note (CO-P2-04).")
STORY_LINKS = {
    "alexstory001": ["alexgrav005", "alexgrav001", "alexgrav002"],
    "alexstory002": ["alexgrav001", "alexgrav005"],
    "alexstory003": ["alexgrav009", "alexgrav003"],
    "alexstory004": ["alexgrav014"],  # cross-build boundary -> Askesis (not-advanced), declared
    "alexstory005": ["alexgrav002", "alexgrav009"],
    "alexstory006": ["alexgrav004"],
    "alexstory007": ["alexgrav005", "alexgrav006"],
    "alexstory008": ["alexgrav006", "alexgrav008"],
    "alexstory009": ["alexgrav009"],
    "alexstory010": ["alexgrav003", "alexgrav005", "alexgrav001", "alexgrav002"],
}

CONVERT_NOTE = ("\n\nS2.5-equivalent (2026-07-27): the parked Formation Ecology "
                "Connection converted to typed gravity_links[] (CO-P2-04 - FEC "
                "verbatim on the first link's note); see wrs/migrate/s62_alx_s25.py.")


def read_record(path: Path):
    """Front/body split via partition on the closing fence. NOT the Desert
    s25 `split("\\n---", 2)` shape, whose parts[2] never existed - the
    world_core body loss FLAG-023 documents. Asserts both fences exist."""
    txt = path.read_text(encoding="utf-8")
    assert txt.startswith("---\n"), f"{path}: no opening fence"
    front, sep, body = txt[4:].partition("\n---\n")
    assert sep, f"{path}: no closing fence"
    return yaml.safe_load(front), body.strip()


def convert_fec(story_path: Path):
    rec, body = read_record(story_path)
    rid = rec["id"]
    assert rid in STORY_LINKS, f"{rid}: no gravity_links mapping"
    if "gravity_links" in rec:  # idempotent re-run: already converted
        assert FEC_DELIM_START not in body, f"{rid}: links AND parking both present"
        return rid, len(rec["gravity_links"])
    i = body.find(FEC_DELIM_START)
    assert i >= 0, f"{rid}: FEC parking not found"
    parked = body[i:]
    j = parked.find("] ")
    assert j > 0, f"{rid}: FEC delimiter close not found"
    fec_text = parked[j + 2:].strip()
    assert len(fec_text) > 100, f"{rid}: FEC text suspiciously short"
    new_body = body[:i].rstrip() + CONVERT_NOTE
    assert new_body != body, f"{rid}: body unchanged (verified-replace discipline)"
    links = [{"gravity_id": STORY_LINKS[rid][0], "note": fec_text}]
    for gid in STORY_LINKS[rid][1:]:
        links.append({"gravity_id": gid, "note": BACK_NOTE})
    rec["gravity_links"] = links
    emit_record(rec, new_body, story_path)
    return rid, len(links)


G_BODY = ("S6.2 S2.5-equivalent gravity record (2026-07-27) from Doc_04 "
          "(per-candidate testing SS3.1-3.6, index table SS4, Cross-Stratum "
          "Test SS5, interaction matrix SS6 - all read in full) + the "
          "Gravity_Index.xlsx Candidates and Interaction Matrix sheets, "
          "absorbed here verbatim ahead of the companion-index deletion "
          "(T1-T4's full explicit six-test grid and the five matrix cells "
          "the SS6 prose does not itemize live only in that index). Six-test "
          "keys per CO-P2-02. The six not-advanced candidates are recorded "
          "per the 'not-advanced kept as records' rule (first non-empty "
          "extension of that rule); they are NOT listed in "
          "world_core.gravities - Doc_04 SS4 classifies them 'not a "
          "gravity'/'Formation Dynamic'.")

F_BODY = ("S6.2 S2.5-equivalent force record (2026-07-27) from Doc_08 (three "
          "layers condensed-verbatim with citations; Layer 4 is THIS step's "
          "authoring - elaboration or considered stasis). connections[] = "
          "force<->force cross-cell links only (Doc_08 SS4), mirrored; "
          "force->gravity tracing lives verbatim in layer_formation_impact "
          "(Desert S2.5 rationale carried - see the script docstring).")


def main():
    interactions = build_interactions()
    for g in GRAVITIES:
        rec = {**COMMON_G, **g}
        if g["id"] in interactions and interactions[g["id"]]:
            rec["interaction"] = interactions[g["id"]]
        emit_record(rec, G_BODY, OUT / "gravity" / f"{g['id']}.md")
    for f in FORCES:
        f = {k: v for k, v in f.items() if v is not None and k != "layer_worlds_own_experience_cite"}
        emit_record({**COMMON_F, **f}, F_BODY, OUT / "force" / f"{f['id']}.md")

    converted = [convert_fec(OUT / "story" / f"{rid}.md")
                 for rid in sorted(STORY_LINKS)]

    wc_path = OUT / "world_core" / "alexcore001.md"
    rec, body = read_record(wc_path)
    rec["gravities"] = [g["id"] for g in GRAVITIES
                        if g["classification"] != "not-advanced"]
    assert len(rec["gravities"]) == 9
    old = ("gravities[] deliberately empty until the S2.5-equivalent authors "
           "the gravity records; ")
    new = ("gravities[] populated at the S2.5-equivalent (the nine confirmed "
           "Doc_04 gravities C1-C5/T1-T4; the six not-advanced candidates are "
           "recorded in the store but are not the world's gravities); ")
    if new not in body:  # idempotent re-run guard
        assert old in body, "alexcore001 body anchor not found (verified-replace discipline)"
        body = body.replace(old, new)
    emit_record(rec, body, wc_path)

    print(f"wrote {len(GRAVITIES)} gravity ({sum(1 for g in GRAVITIES if g['classification'] != 'not-advanced')} confirmed + "
          f"{sum(1 for g in GRAVITIES if g['classification'] == 'not-advanced')} not-advanced) + {len(FORCES)} force records; "
          f"FEC converted on {len(converted)} stories "
          f"({sum(n for _, n in converted)} gravity_links); world_core.gravities -> 9 confirmed ids")


if __name__ == "__main__":
    main()
