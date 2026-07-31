"""S6.2/HAL - S2.5-equivalent: gravities + forces + FEC conversion.

- 10 gravity records: 6 confirmed (Doc_04 SS2's per-candidate six-test
  prose + SS3's classification table + SS4's interaction matrix, all
  read in full this step) + 4 not-advanced (Doc_04 SS1's three
  considered-and-not-advanced candidates PLUS G5-Jerome, which Doc_04
  SS3 subsumes into G1 as a named sub-component, not a seventh gravity
  - recorded so the subsumption is queryable, the SYR not-advanced
  extension pattern).
- 12 force records (Doc_08's six-cell matrix). NOTE, DECLARED: Doc_08
  has NO force 3B-1 - Cell 3B contains only the required transmission
  entry, which carries the doc's own number 3B-2; the numbering gap is
  Doc_08's own and is kept, not repaired. Three layers condensed with
  citations; Layer 4 is THIS step's authoring (elaboration - no stasis
  entries in this world: every HAL force has documented dynamics);
  connections[] = Doc_08 SS2's four named cross-cell connections plus
  the index's link columns, mirrored; force->gravity tracing lives
  verbatim in layer_formation_impact (the Desert S2.5 rationale).
- FEC conversion (CO-P2-04): the S2.4 FEC parkings become typed
  gravity_links on 9 of 12 stories. THREE stories' FECs name NO
  Doc_04 gravity - halstory08 ('the formation-logic tension', not a
  gravity), halstory09 ('the formation-narrative dimension'), and
  halstory10 ('the formation-logic gravity' - VOCABULARY VARIANCE,
  DECLARED: the chunk calls halcore001's formation_logic a 'gravity',
  but Doc_04 confirms no such gravity; the FEC is linked to nothing
  rather than force-fit, and the variance is recorded in the S2.5
  checkpoint + FLAGS). Their FECs stay body-parked; the S2.8 chunk
  view must render FEC from the body parking for these three (the SYR
  three-unlinked precedent).
- halcore001.gravities closed at the 6 confirmed (FLAG-023 reader).
- Gravity interaction edges mirror Doc_04 SS4's matrix exactly,
  including the Round-1-corrected G5(M)-G6 reshaping cell and the
  three no-demonstrated-relationship pairs (G1-G2, G2-G4, G2-G6 -
  absent here BY THE MATRIX'S OWN FINDING, not omission).
- G2's confidence note carries Doc_04's own correction verbatim in
  substance: the three letters are one author's one genre, NOT
  independent attestation; the real corroborator class (senatorial-
  renunciation social history) is the unnamed aggregate whose named
  standard work (Brown 2012) is the S2.1b miss -> pre-freeze re-sweep.
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
sys.path.insert(0, str(HERE))

from source_rows_from_doc02 import emit_record
from s62_hal_s23 import read_record, write_record

OUT = BACKEND / "wrs" / "records" / "hieronymian_world"
WID = "hieronymian-ascetic-literary"
D4 = "hal_Doc_04_Gravity_Discovery.md (read in full this step)"


def G(id_, name, cls, tests, crosscheck, inter, srcs, body):
    rec = {"world_id": WID, "record_type": "gravity", "schema_version": 1,
           "jobs": [5], "register": "etic", "review_state": "draft",
           "sources": [{"source_id": s} for s in srcs],
           "id": id_, "name": name, "classification": cls}
    if tests:
        rec["six_tests"] = {k: {"verdict": v} for k, v in tests.items()}
    if crosscheck:
        rec["confidence_crosscheck"] = crosscheck
    if inter:
        rec["interaction"] = inter
    return rec, body


GRAVITIES = [
 G("halgrav001",
   "Hebraica veritas - Hebrew-based textual authority (G1)", "Primary",
   {"repetition": ("PASS - recurs across Jerome's prefaces, his "
                   "commentaries, and the Augustine correspondence - "
                   "multiple evidence streams (Doc_04 G1)."),
    "dependency": ("PASS, strong - the Vulgate project, the community's "
                   "Hebrew-study practice, and the Augustine/Oea "
                   "controversy all depend on this principle (Doc_04 G1)."),
    "formation": ("PASS, but ASYMMETRIC, flagged for Doc_05 "
                  "proportionality - shapes Jerome's scholarly identity "
                  "directly; shapes the women's engagement only indirectly "
                  "(as dedicatees/patrons, not practitioners - no source "
                  "attests any of the four women studying Hebrew) (Doc_04 "
                  "G1)."),
    "explanatory": ("PASS, strong - explains the Vulgate project, the "
                    "Augustine dispute, and Jerome's self-presentation as "
                    "scholarly authority (Doc_04 G1)."),
    "persistence": ("PASS - from the Rome period (Damasus-commissioned "
                    "Gospel revision) through the full Bethlehem period to "
                    "the early-400s Augustine correspondence (Doc_04 G1)."),
    "interaction": ("PASS - reinforces G3 (funding) and G4 (disputes by "
                    "letter); competes with the wider Latin Septuagint "
                    "consensus (external); reshaped by G6 (Doc_04 G1, "
                    "SS4).")},
   ("THE FLAGGED DIVERGENCE, carried not dissolved (Doc_04 SS3, Round-1 "
    "correction): the principle's ATTESTATION (that Jerome held it, that "
    "it produced a real translation artifact) is Widely-Accepted-to-"
    "Documented and independently clears the Primary threshold; the "
    "CONTENT-level confidence (whether its claims / Jerome's Hebrew "
    "fluency are correct) is separately Contested per Williams. Author "
    "Gravity HIGH: the principle's articulation survives almost entirely "
    "in Jerome's own voice; its contestedness is independently attested "
    "(Augustine), its content is not."),
   [{"type": "reinforcing", "target_id": "halgrav003",
     "note": "Doc_04 SS4: G3 funds G1 - the women's patronage makes the Hebrew study and translation project materially possible."},
    {"type": "reinforcing", "target_id": "halgrav004",
     "note": "Doc_04 SS4: G1's disputes are conducted by letter (the Augustine correspondence)."},
    {"type": "reinforcing", "target_id": "halgrav005",
     "note": "Doc_04 SS4: same textual-authority logic (the Doc_01 SS4 'same underlying currency' finding)."},
    {"type": "reshaping", "target_id": "halgrav006",
     "note": ("Doc_04 SS4 - DIRECTION: G6 reshapes G1 (this record is "
              "the reshaped side; the enum carries no inverse, the note "
              "does - ALX C2-T4 pattern): the Augustine dispute "
              "tests/pressures the principle.")}],
   ["srcHAL001", "srcHAL023", "srcHAL009", "srcHAL013"],
   ("S6.2/HAL S2.5-equivalent gravity record (2026-07-31) from " + D4 +
    ". Forces-connection (Doc_04 SS5): INTENSIFIED by the Augustine "
    "dispute (an external force testing and sharpening rather than "
    "dissolving it); TRANSFORMED at 3B-2 (loses its real-time defense "
    "mechanism at Jerome's death - from live, actively-defended project "
    "to fixed, undefended text). See halforce2A2/halforce3B2.")),
 G("halgrav002",
   "Voluntary ascetic self-impoverishment - wealth renunciation as "
   "formation practice (G2)", "Primary",
   {"repetition": ("PASS, on the CORRECTED basis (Doc_04 Round 2): "
                   "attested for Paula, Eustochium, Fabiola across Epp. "
                   "108, 22, 77 - but these are one author's texts in one "
                   "idealizing genre, NOT independent attestation; the "
                   "pattern's actual corroboration is the independent "
                   "social-historical scholarship on senatorial "
                   "renunciation (Doc_02 SS6), not the letter count."),
    "dependency": ("PASS, strong - the Bethlehem foundation's funding, "
                   "the pilgrim hospice, and Fabiola's Roman hospital all "
                   "depend on this practice (Doc_04 G2)."),
    "formation": ("PASS, strong - arguably the strongest Formation-test "
                  "result of any candidate for the women's half of the "
                  "ecology: the central content of their own asceticism "
                  "(Doc_04 G2)."),
    "explanatory": ("PASS, strong - explains the funding structure (G3), "
                    "the hospice, the hospital, and the family resistance "
                    "(Doc_02 SS7.2) (Doc_04 G2)."),
    "persistence": ("PASS - from pre-382 Rome (Marcella's household) "
                    "through the full 382-420 span (Doc_04 G2)."),
    "interaction": ("PASS - reinforces G3 (it IS the source of the wealth "
                    "G3 redirects) and G5-M (Marcella's independent "
                    "position rests partly on it); competes with "
                    "conventional senatorial marriage-and-inheritance "
                    "expectations (external). THINNEST interaction "
                    "profile of any candidate (three no-relationship "
                    "cells: G1, G4, G6) - noted, not concealed: its role "
                    "is genuinely foundational/enabling rather than "
                    "interactive (Doc_04 G2, SS4).")},
   ("Widely Accepted - with Doc_04's own Round-1 correction carried: "
    "multiply attested across three letters BY ONE AUTHOR IN ONE "
    "IDEALIZING GENRE; the actual independent corroboration is the "
    "social-historical scholarship on senatorial patronage/renunciation "
    "(Doc_02 SS6) - the class whose named standard work (Brown 2012) is "
    "this migration's S2.1b relative-recall miss, routed to the "
    "pre-freeze re-sweep."),
   [{"type": "reinforcing", "target_id": "halgrav003",
     "note": "Doc_04 SS4: G2 is the source of the wealth G3 redirects - foundational, not merely interactive."},
    {"type": "reinforcing", "target_id": "halgrav005",
     "note": "Doc_04 SS4: Marcella's independent household standing rests partly on her own unmarried, propertied position - itself a form of this practice."}],
   ["srcHAL001", "srcHAL017", "srcHAL020"],
   ("S6.2/HAL S2.5-equivalent gravity record (2026-07-31) from " + D4 +
    ". Forces-connection (Doc_04 SS5): HELD/INTENSIFIED across the "
    "384-385 Rome crisis and the relocation - the practice continues and "
    "if anything deepens after the crisis rather than being abandoned; "
    "tested by the pagan-aristocratic backlash (2A-1) without "
    "diminishing. See halforce1A1/halforce2A1.")),
 G("halgrav003",
   "Patronage as the operative authority structure (G3)", "Primary",
   {"repetition": ("PASS - attested in Doc_01 SS3.3/SS8.1 and "
                   "independently in Rebenich's and Cain's scholarship as "
                   "the interpretive frame for Jerome's whole career arc "
                   "(Doc_04 G3)."),
    "dependency": ("PASS, strong - Jerome's travel, Hebrew study, and the "
                   "entire Bethlehem foundation depend on it (G1 depends "
                   "on G3 for material possibility); the hospice and "
                   "hospital (G2) are themselves patronage acts (Doc_04 "
                   "G3)."),
    "formation": ("PASS, strong - shapes the entire community's authority "
                  "self-understanding (Doc_01 SS5.3): the clearest "
                  "Primary-level Formation-test result (Doc_04 G3)."),
    "explanatory": ("PASS, strong - explains why Jerome's authority is "
                    "precarious (the 384-385 crisis) and why the women "
                    "hold real, not merely supportive, ecological weight "
                    "(Doc_04 G3)."),
    "persistence": ("PASS - across the entire 382-420 span and both "
                    "geographic poles (Doc_04 G3)."),
    "interaction": ("PASS - reinforces G1, G2; competes with episcopal/"
                    "territorial authority as a rival mode (the Doc_01 "
                    "SS8.1 differentiation axis); reshapes G5-M (the same "
                    "logic operating from independent wealth - Doc_01 SS4, "
                    "carried with care) (Doc_04 G3, SS4).")},
   ("Widely Accepted - independent scholarly consensus (Rebenich, Cain: "
    "genuinely independent of Jerome's own account for the interpretive "
    "frame, even where specific financial mechanics rest on his "
    "account). The strongest overall six-test result and the strongest "
    "bipolar-holding candidate (Doc_04 SS3)."),
   [{"type": "reinforcing", "target_id": "halgrav001",
     "note": "Mirror of halgrav001's edge (Doc_04 SS4)."},
    {"type": "reinforcing", "target_id": "halgrav002",
     "note": "Mirror of halgrav002's edge (Doc_04 SS4)."},
    {"type": "reinforcing", "target_id": "halgrav004",
     "note": "Doc_04 SS4: the patronage relationships are maintained by letter across the bipolar geography."},
    {"type": "reshaping", "target_id": "halgrav005",
     "note": ("Doc_04 SS4: G3's logic reshapes how G5-M's independent "
              "authority is best understood - same underlying currency, "
              "different position (Doc_01 SS4; direction: G3 reshapes "
              "G5-M, this record is the reshaping side).")},
    {"type": "reshaping", "target_id": "halgrav006",
     "note": ("Doc_04 SS4 - DIRECTION: G6 reshapes G3 (this record is "
              "the reshaped side): controversy threatens/tests the "
              "network G3 depends on.")}],
   ["srcHAL015", "srcHAL010", "srcHAL001"],
   ("S6.2/HAL S2.5-equivalent gravity record (2026-07-31) from " + D4 +
    ". Forces-connection (Doc_04 SS5 + Doc_08 corrected row): SHIFTED in "
    "form - from Rome-based, clerically-entangled patronage to a more "
    "insulated Bethlehem-based arrangement - specifically under 2A-4 "
    "(the clerical-reputational precarity culminating in the 384-385 "
    "crisis), NOT under the pagan backlash (Doc_08's Round-1 "
    "correction); not fractured. Paula's material funding chain did not "
    "fail during the crisis - it is what carried the relocation. See "
    "halforce2A4.")),
 G("halgrav004",
   "Letter-writing (epistula) as the primary medium of formation and "
   "community-maintenance across distance (G4)", "Supporting",
   {"repetition": ("PASS, trivially strong - the overwhelming majority of "
                   "Doc_02's entire source base is epistolary - WITH the "
                   "evidentiary-circularity flag: this result is partly an "
                   "artifact of the source base itself being letters "
                   "(Doc_04 G4)."),
    "dependency": ("PASS - G1's Augustine dispute, G5-M's known exercise "
                   "(though the practice itself was partly in-person, per "
                   "Ep. 127), and Rome/Bethlehem cohesion all depend on "
                   "the medium (Doc_04 G4)."),
    "formation": ("PASS - directly shapes how spiritual direction and "
                  "instruction were delivered (Ep. 22; the dedicated "
                  "commentaries) (Doc_04 G4)."),
    "explanatory": ("PASS, strong - explains how a geographically bipolar "
                    "community maintained coherence at all (Doc_04 G4)."),
    "persistence": "PASS - visible across the entire span (Doc_04 G4).",
    "interaction": ("PASS - reinforces G1, G3, G5-M, G6; uniformly "
                    "'reinforcing', never competing or reshaping - an "
                    "enabling medium, not a force in tension (Doc_04 "
                    "G4).")},
   ("Widely Accepted for the medium's use. SUPPORTING, on the CORRECTED "
    "rationale (Doc_04 Round 1): not the invented 'reinforcing-only "
    "Interaction is weaker' criterion (which was also inconsistently "
    "applied), but (a) the evidentiary-circularity flag on the "
    "Repetition result, and (b) G4's character as an enabling MEDIUM "
    "through which the Primary gravities operate rather than an "
    "independent force generating its own formation content - a "
    "functional distinction, not an Interaction-test technicality."),
   [{"type": "reinforcing", "target_id": "halgrav001",
     "note": "Mirror of halgrav001's edge (Doc_04 SS4)."},
    {"type": "reinforcing", "target_id": "halgrav003",
     "note": "Mirror of halgrav003's edge (Doc_04 SS4)."},
    {"type": "reinforcing", "target_id": "halgrav005",
     "note": ("Doc_04 SS4: PARTIAL - Marcella's authority is exercised "
              "partly in person, per Ep. 127, not solely by letter; the "
              "partiality is the matrix's own qualifier, kept.")},
    {"type": "reinforcing", "target_id": "halgrav006",
     "note": "Doc_04 SS4: G6's disputes are conducted partly by letter (the Augustine correspondence)."}],
   ["srcHAL001", "srcHAL023"],
   ("S6.2/HAL S2.5-equivalent gravity record (2026-07-31) from " + D4 +
    ". Forces-connection (Doc_04 SS5 + Doc_08 corrected row): "
    "INTENSIFIED as a direct consequence of the 385 relocation itself "
    "(2A-4's crisis made the separation, and the separation made "
    "letter-writing newly indispensable); sustained continuously via "
    "2B-2 (the praefatio/epistula transmission apparatus). See "
    "halforce2A4/halforce2B2.")),
 G("halgrav005",
   "Independent female exegetical authority - Marcella's practiced "
   "recognition (G5-Marcella)", "Tensional",
   {"repetition": ("WEAK/SINGLE-SOURCE PASS for Marcella's specific "
                   "instance - attested in exactly one source (Ep. 127); "
                   "isolating her instance from Jerome's is itself a "
                   "framing choice, not a neutral test (Doc_04 SS2's "
                   "methodological caveat, kept attached)."),
    "dependency": ("PARTIAL - narrowly dependency-linked (the Roman "
                   "clergy's specific disputes), not shown to be depended "
                   "upon by other ecological dimensions the way G1/G3 are "
                   "(Doc_04 G5)."),
    "formation": ("PARTIAL - the evidence shows her EXERCISING recognized "
                  "authority, not clear evidence of it FORMING others' "
                  "practice beyond the specific clergy who consulted her "
                  "(Doc_04 G5)."),
    "explanatory": ("PASS, with the circularity noted - explains why "
                    "Doc_01's strand-tension exists at all (the candidate "
                    "explains a tension the candidate itself creates) "
                    "(Doc_04 G5)."),
    "persistence": ("WEAKER PASS - real but shorter and single-attested "
                    "window: 385 (Jerome's departure creates the space) "
                    "to her 410 death (Doc_04 G5)."),
    "interaction": ("PASS - reinforces G1 and relates to G3 exactly as "
                    "Doc_01 SS4 established (same underlying logic, "
                    "different position - not a rival authority "
                    "structure); reshaped by G6 (the Round-1-corrected "
                    "cell) (Doc_04 G5, SS4).")},
   ("Contested - FAILS the Primary threshold under the Cross-Check, and "
    "THIS (not the bipolar-geography result, withdrawn as a non-sequitur "
    "for that question) is the basis on which Doc_01 Open Issue #7 was "
    "resolved: a difference in KIND cannot be affirmatively established "
    "on Contested, single-source, post-mortem, self-vindicating "
    "evidence; Ep. 127 read closely actively supports 'same underlying "
    "currency, different position' (she disputed his answers 'to "
    "learn'; Cain: the letter partly serves Jerome's own vindication). "
    "The strand-singular finding is NOT reopened; the counter-current "
    "is real and the ecology cannot be honestly described without it - "
    "precisely a Tensional gravity. Bipolar-geography: fails (Rome-only) "
    "- relevant to this classification only. Doc_04's proportionality "
    "check on this outcome is carried in Doc_05, not resolved here."),
   [{"type": "reinforcing", "target_id": "halgrav001",
     "note": "Mirror of halgrav001's edge (Doc_04 SS4)."},
    {"type": "reinforcing", "target_id": "halgrav002",
     "note": "Mirror of halgrav002's edge (Doc_04 SS4)."},
    {"type": "reshaping", "target_id": "halgrav003",
     "note": ("Mirror of halgrav003's edge - DIRECTION: G3 reshapes "
              "G5-M (this record is the reshaped side) (Doc_04 SS4).")},
    {"type": "reinforcing", "target_id": "halgrav004",
     "note": "Mirror of halgrav004's edge (partial - partly in person) (Doc_04 SS4)."},
    {"type": "reshaping", "target_id": "halgrav006",
     "note": ("Mirror of halgrav006's edge - DIRECTION: G6 reshapes "
              "G5-M (this record is the reshaped side); the "
              "Round-1-CORRECTED cell: Marcella is a named addressee of "
              "Jerome's anti-Rufinus polemic, and Ep. 127 partly serves "
              "his Origenist-controversy vindication (Cain) - "
              "controversy reshapes how her commemorated authority is "
              "deployed and remembered (Doc_04 SS4).")}],
   ["srcHAL001", "srcHAL012", "srcHAL010"],
   ("S6.2/HAL S2.5-equivalent gravity record (2026-07-31) from " + D4 +
    ". Forces-connection (Doc_04 SS5): HELD through the 385 departure - "
    "the very event that creates the space for the independent Roman "
    "role; FRACTURED at Marcella's 410 death (the Gothic sack) - an "
    "ending-force directly terminating this gravity's Rome-based "
    "expression, consistent with the final-decade Bethlehem "
    "concentration. See halforce1B1/halforce2A4/halforce3A1. The "
    "record-store home of this gravity's evidentiary core is "
    "halstory07 (single most Author-Gravity-constrained story) and "
    "hallex11 (the tension-with edge to hallex06).")),
 G("halgrav006",
   "Controversy/textual-doctrinal dispute as formation-shaping pressure "
   "(G6)", "Supporting",
   {"repetition": ("PASS - three independent controversy-clusters: the "
                   "Rufinus/Origenist material, the Augustine "
                   "correspondence, the Pelagian attack (Doc_04 G6)."),
    "dependency": ("PASS, strong - the community's self-definition "
                   "(against Origenism, against the Septuagint "
                   "traditionalists, against the Pelagian mob) depends "
                   "heavily on these disputes (Doc_04 G6)."),
    "formation": ("PASS - shapes Jerome's combative self-presentation "
                  "directly; shapes the women's formation chiefly through "
                  "the 416 attack, a shared formation-shaping event for "
                  "the whole community (Doc_04 G6)."),
    "explanatory": ("PASS, strong - explains major turning points across "
                    "the whole span (393-403 rupture; 416 violence; the "
                    "ongoing Augustine dispute) (Doc_04 G6)."),
    "persistence": "PASS - visible across nearly the entire span, 393 onward (Doc_04 G6).",
    "interaction": ("PASS - reshapes G1 (the Augustine dispute is a "
                    "direct test of the Hebrew-veritas principle) and G3 "
                    "(the Origenist rupture conducted through, and "
                    "threatening, the patronage network) (Doc_04 G6, "
                    "SS4).")},
   ("Documented (the events occurred) to Contested (the substance of the "
    "disputes, per adversarial sourcing). Supporting: organizes "
    "significant portions of the ecology but functions WITHIN the "
    "context the Primary gravities establish - a pressure ON G1/G3, not "
    "an independent organizing force generating its own formation "
    "practice. This classification is SETTLED at Doc_04 SS3 (the SS5 "
    "forces-notation explicitly does not reopen it - the Round-1 "
    "correction); Doc_08 carries the narrower compilation point: "
    "G6-as-gravity is the ecology's organized response to the "
    "controversy FORCES (2B-1, 3A-2), not identical with them."),
   [{"type": "reshaping", "target_id": "halgrav001",
     "note": ("Doc_04 SS4: G6 tests/pressures G1 via the Augustine "
              "dispute (this record is the reshaping side).")},
    {"type": "reshaping", "target_id": "halgrav003",
     "note": ("Doc_04 SS4: G6 threatens/tests the network G3 depends on "
              "(this record is the reshaping side).")},
    {"type": "reinforcing", "target_id": "halgrav004",
     "note": "Mirror of halgrav004's edge (Doc_04 SS4)."},
    {"type": "reshaping", "target_id": "halgrav005",
     "note": ("Doc_04 SS4, the Round-1-corrected cell: controversy "
              "reshapes how Marcella's commemorated authority is "
              "deployed and remembered (this record is the reshaping "
              "side).")}],
   ["srcHAL005", "srcHAL007", "srcHAL009", "srcHAL016"],
   ("S6.2/HAL S2.5-equivalent gravity record (2026-07-31) from " + D4 +
    ". Forces-connection (Doc_04 SS5, corrected notation): "
    "HELD/INTENSIFIED under both the Origenist rupture (393-403, which "
    "G6 itself organizes and explains) and the 416 attack (an "
    "ending-adjacent external force absorbed by an already-established "
    "organizing pattern rather than generating a new one). See "
    "halforce2B1/halforce3A2.")),
]

NOT_ADVANCED = [
 ("halgrav007",
  "Hospitality/pilgrim-hospice practice - xenodochium (not advanced)",
  ("Doc_04 SS1: considered and not advanced as an independent candidate "
   "- on the Repetition and Dependency tests it functions as an "
   "EXPRESSION of G2 (wealth redirection), not a distinct organizing "
   "force; folded into G2's discussion. This is also why 'Xenodochium' "
   "in the chunks' Related-Terms lines has no term record (the S2.3 "
   "never-built-partner declaration).")),
 ("halgrav008",
  "Hebrew-language study as a discrete practice (not advanced)",
  ("Doc_04 SS1: merged into G1 - the practice (Jerome's Hebrew study) "
   "and the principle (Hebraica veritas) are not evidenced as separable "
   "in this world's own sources; the Contested status on Jerome's "
   "actual fluency (Doc_01 SS9 Open Issue #2) applies to both "
   "equally.")),
 ("halgrav009",
  "Monastic daily-life structure - horarium (not advanced)",
  ("Doc_04 SS1: rests on Dominant-Modern-Reconstruction-level inference "
   "from a single source (Doc_01 SS9 Open Issue #5) - too thin to test "
   "as an organizing gravity rather than a downstream consequence of "
   "G2/G3. This is the same evidence judgment behind halstory10's "
   "Absent Story Note (no horarium supplied, honest brevity when "
   "asked).")),
 ("halgrav010",
  "Jerome's exegetical authority - G5-Jerome (not separately "
  "classified; subsumed into G1)",
  ("Doc_04 SS3: passes all six tests but is NOT a seventh gravity - "
   "Doc_01 SS4 and Doc_04's own testing show Jerome's exegetical "
   "authority is not evidentially separable from his textual-authority "
   "project (G1); tracked as a named sub-component of G1. Recorded "
   "here so the subsumption is queryable (the SYR not-advanced "
   "extension pattern), never as a live gravity.")),
]

D8 = "hal_Doc_08_Forces_Document.md"


def F(id_, name, cell, l1, l2, l3, l4, conns, srcs):
    rec = {"world_id": WID, "record_type": "force", "schema_version": 1,
           "jobs": [1, 5], "register": "etic", "review_state": "draft",
           "sources": [{"source_id": s} for s in srcs],
           "id": id_, "name": name, "six_cell_position": cell,
           "layer_historical_event": l1,
           "layer_worlds_own_experience": l2,
           "layer_formation_impact": l3,
           "layer4": l4}
    if conns:
        rec["connections"] = conns
    return rec


FORCES = [
 F("halforce1A1",
   "Roman aristocratic ascetic movement predating this world's own "
   "bounded span (Force 1A-1)",
   "1A - Initiating / External",
   ("A senatorial-class ascetic movement among Roman Christian women, "
    "already active by the 360s-370s (Marcella's household), predating "
    "Jerome's 382 arrival. Confidence: Widely Accepted (existence); "
    "Dominant Modern Reconstruction (specific dating of functioning "
    "household status) (Doc_08 1A-1 L1)."),
   ("A household already gathered around fasting, plain dress, and "
    "study before the scholar from the East ever arrived - a movement "
    "this world's own participants understood themselves as joining and "
    "extending, not founding from nothing (Doc_08 1A-1 L2, "
    "From-Within)."),
   ("Established the social and devotional template (renunciation as "
    "aristocratic Christian practice) that this world's whole formation "
    "ecology (G2) presupposes and extends (Doc_08 1A-1 L3)."),
   {"elaboration": (
     "The initiating template never remained mere backdrop: what began "
     "as an existing movement became the world's own recruiting ground "
     "and legitimacy claim - the household Jerome joined in 382 already "
     "had two decades of its own practice to extend, which is why 1B-1 "
     "(Marcella's prior initiative) is this force's internal "
     "counterpart rather than its echo (S2.5 Layer-4 authoring from "
     "Doc_08 1A-1 + 1B-1's paired framing).")},
   [],
   ["srcHAL001", "srcHAL017", "srcHAL019"]),
 F("halforce1A2",
   "Jerome's arrival in Rome with papal-adjacent scholarly credentials "
   "(Force 1A-2)",
   "1A - Initiating / External",
   ("Jerome arrives in Rome 382 as secretary/scriptural adviser to Pope "
    "Damasus I, possessing classical rhetorical/grammatical training "
    "and biblical scholarship. Confidence: Widely Accepted (Doc_08 "
    "1A-2 L1)."),
   ("A trained scholar arriving with exactly the philological "
    "competence the Aventine circle had lacked (Doc_08 1A-2 L2, "
    "From-Within)."),
   ("Generated G1 and G3 directly - without this convergence, no "
    "Hebrew-based translation project and no patronage-authority "
    "structure exist in this world (Doc_08 1A-2 L3)."),
   {"elaboration": (
     "The arrival's structural weight shows in what it seeded on BOTH "
     "temporal sides: forward into the ongoing Augustine dispute (the "
     "credentials made the translation project, the project made the "
     "dispute) and into the precarity that ended the Rome period (the "
     "same papal adjacency that opened the door was the single point "
     "of failure 2A-4 records) - one initiating force feeding both a "
     "gravity's growth and its later crisis (S2.5 Layer-4 authoring "
     "from Doc_08 SS2 Connection 1 + the 1A-2 -> 2A-4 index link).")},
   [{"type": "generates", "target_id": "halforce2A2",
     "note": ("Doc_08 SS2 Connection 1 (first leg): the arrival "
              "(initiating) generates the ongoing Augustine dispute - "
              "the throughline runs 1A-2 -> 2A-2 -> 3B-2.")},
    {"type": "exposes-to", "target_id": "halforce2A4",
     "note": ("Doc_08 index: 1A-2 -> 2A-4 (reciprocal link added at "
              "Round 2) - the papal-adjacent standing the arrival "
              "conferred is the same standing whose precarity 2A-4 "
              "records.")}],
   ["srcHAL001", "srcHAL014", "srcHAL015"]),
 F("halforce1B1",
   "Marcella's household reading practice, pre-Jerome (Force 1B-1)",
   "1B - Initiating / Internal",
   ("Marcella's personal ascetic conversion (via exposure to "
    "Athanasius's Roman exile, per Ep. 127) dates to the 340s; her "
    "household's transition to a functioning multi-woman formation "
    "site is best placed 360s-370s. Confidence: Dominant Modern "
    "Reconstruction (dating) (Doc_08 1B-1 L1)."),
   ("A widow who had already chosen, on her own initiative, the "
    "discipline that later became this world's shared practice - "
    "before any outside teacher named or systematized it for her "
    "(Doc_08 1B-1 L2, From-Within)."),
   ("The internal seed from which G2 and, specifically, G5-Marcella "
    "both grow - Marcella's own prior initiative is the "
    "internal-origin counterpart to Jerome's external arrival (1A-2) "
    "(Doc_08 1B-1 L3)."),
   {"elaboration": (
     "The initiative's arc is the matrix's cleanest single line: "
     "internal origin, persisting on its own terms (NOT routed through "
     "the praefatio/epistula apparatus - her authority was exercised "
     "in person; Doc_08's Round-1 correction), until severed DIRECTLY "
     "by an external ending force entirely outside this world's "
     "control (the 410 sack) - internal initiative, externally "
     "severed, no intervening transmission mechanism required (S2.5 "
     "Layer-4 authoring from Doc_08 SS2's corrected connection).")},
   [{"type": "severed-by", "target_id": "halforce3A1",
     "note": ("Doc_08 SS2 (corrected): 1B-1 -> 3A-1 DIRECT - the "
              "initiative persists on its own terms until terminated "
              "by the sack; the original routing through 2B-2 was "
              "wrong (the apparatus is Jerome's Bethlehem output, not "
              "Marcella's in-person Roman standing).")}],
   ["srcHAL001", "srcHAL012"]),
 F("halforce2A1",
   "Pagan aristocratic backlash and the wider Roman senatorial culture "
   "(Force 2A-1)",
   "2A - Ongoing / External",
   ("A resilient pagan senatorial culture (the Symmachus circle, the "
    "Altar of Victory controversy) coexisting with and resisting "
    "Christian ascetic renunciation throughout the 380s-390s. "
    "Confidence: Widely Accepted (general pattern) (Doc_08 2A-1 L1)."),
   ("A world in which choosing renunciation invited real social "
    "judgment from one's own class - the mockery and suspicion of "
    "neighbors who read the choice as a betrayal of family and rank, "
    "not admiration (Doc_08 2A-1 L2, From-Within)."),
   ("Pressed directly on the boundary structure - made the "
    "renunciation-boundary genuinely costly to cross, not merely "
    "symbolically so. LIMITED to its own genuinely pagan-aristocratic "
    "content per Doc_08's Round-1 correction: the 384-385 crisis "
    "effects that were mis-filed here belong to 2A-4 "
    "(clerical-reputational precarity, a different force and a "
    "different register - intra-Christian accusation, not pagan "
    "mockery) (Doc_08 2A-1 L3, corrected)."),
   {"elaboration": (
     "The force's ecological work is boundary-pricing: it never "
     "breached or reshaped G2 (which held/intensified straight "
     "through), but it kept the cost of crossing real for the entire "
     "Roman period - the resistance that makes halstory02's public "
     "blame legible and hal_lex03's 'seen to renounce' a social fact "
     "rather than a phrase (S2.5 Layer-4 authoring from Doc_08 2A-1 + "
     "the G2 synthesis row).")},
   [],
   ["srcHAL014", "srcHAL015"]),
 F("halforce2A2",
   "The Jerome-Augustine correspondence and the wider Latin "
   "scriptural-authority debate (Force 2A-2)",
   "2A - Ongoing / External",
   ("Ongoing exchange (Ep. 112 = Augustine's Ep. 75, and related "
    "letters) contesting the Hebrew-based translation's abandonment of "
    "the Septuagint's received authority; concretely tested in the Oea "
    "'ivy/gourd' incident (Jonah 4:6). Confidence: Documented (Doc_08 "
    "2A-2 L1)."),
   ("A running argument, carried by letter across a real distance, "
    "with a respected fellow scholar who would not simply concede the "
    "point (Doc_08 2A-2 L2, From-Within)."),
   ("Directly shaped G1's conceptual structure - the Hebraica veritas "
    "commitment was articulated and refined specifically IN RESPONSE "
    "TO this ongoing external contest (Doc_08 2A-2 L3)."),
   {"elaboration": (
     "The contest is constitutive, not incidental: the principle's "
     "surviving articulation (the prefaces, the Ep. 112 exchange) is "
     "argument-shaped because it was argued - remove this force and "
     "G1's own textual form is different; which is why the throughline "
     "runs on to 3B-2 (when the sole arguer died, the "
     "argued-in-real-time character is what ended) (S2.5 Layer-4 "
     "authoring from Doc_08 SS2 Connection 1, second and third "
     "legs).")},
   [{"type": "generated-by", "target_id": "halforce1A2",
     "note": "Doc_08 SS2 Connection 1 (mirror of the first leg)."},
    {"type": "shapes-reception-recorded-at", "target_id": "halforce3B2",
     "note": ("Doc_08 SS2 Connection 1 (third leg): the dispute shapes "
              "how the project's eventual, uncontrolled transmission "
              "will be received - origin to unresolved legacy.")}],
   ["srcHAL009"]),
 F("halforce2A3",
   "Egyptian/Palestinian monastic movement as ongoing institutional "
   "template (Force 2A-3)",
   "2A - Ongoing / External",
   ("The Nitrian ascetic communities (Ep. 108's attested encounter "
    "with Bishop Isidore and an unnamed monastic multitude) provided "
    "an ongoing organizational and devotional model this world drew on "
    "throughout its span. Confidence: Widely Accepted (general "
    "influence); Documented (the Nitria encounter) (Doc_08 2A-3 L1)."),
   ("A pattern of desert withdrawal and communal discipline, witnessed "
    "firsthand on the founding journey, carried back and adapted - not "
    "copied wholesale, but genuinely formative of how this world "
    "understood what a monastic community should look like (Doc_08 "
    "2A-3 L2, From-Within)."),
   ("Shaped Organizational Ecology and the monasterium duplex pattern, "
    "while producing a distinctly Latin-literary variant rather than a "
    "copy. NOT directly gravity-anchored - organizational context "
    "(Doc_08's corrected index row: the G6 link was removed; the two "
    "views now agree) (Doc_08 2A-3 L3)."),
   {"elaboration": (
     "The template's limit is its most instructive feature: the "
     "desert-withdrawal model this world adapted is precisely what the "
     "416 attack demonstrates was never fully insulating - even a "
     "community modeled on desert isolation remained reachable by "
     "organized local violence; and the household's own literary "
     "answer to the template (the Vita Malchi/Hilarionis romances, "
     "halstory09) shows adaptation running through GENRE, not just "
     "organization (S2.5 Layer-4 authoring from Doc_08 SS2's "
     "2A-3/3A-2 connection + halstory09's FEC).")},
   [{"type": "shapes-context-of", "target_id": "halforce3A2",
     "note": ("Doc_08 SS2: the desert-isolation model 2A-3 supplied is "
              "what 3A-2's violence proved permeable.")}],
   ["srcHAL001"]),
 F("halforce2A4",
   "Clerical-reputational precarity of Rome-based papal-adjacent "
   "standing, with the 384-385 crisis as its sharpest instance (Force "
   "2A-4)",
   "2A - Ongoing / External",
   ("An ongoing structural exposure - Jerome's Rome-period standing "
    "depended on the continued personal favor of Pope Damasus I (a "
    "patron of a different KIND than Paula's material funding). Acute "
    "in 384: Blaesilla's death from ascetic excess generated public "
    "accusation against Jerome specifically; Damasus's death that "
    "December removed the protection; resulting clerical hostility "
    "drove the August 385 departure. Confidence: Documented (the "
    "sequence); Inferential/Thin (any formal conciliar 'synod' - not "
    "asserted). ADDED at Doc_08 Round 1 (HIGH-1): this world's central "
    "transforming event had NO force entry and was mis-filed under "
    "2A-1 (Doc_08 2A-4 L1)."),
   ("Favor held at one man's pleasure, and gone the moment that man "
    "was gone - a kind of standing this world's own central scholar "
    "had, and then, within a single year, did not (Doc_08 2A-4 L2, "
    "From-Within)."),
   ("THIS force (not 2A-1): shifted G3 from Rome-centered to "
    "Bethlehem-centered; made the 385 relocation - and thus G4's "
    "intensification - necessary; created the Rome vacancy that gave "
    "G5-Marcella's standing room to be exercised. Explicitly "
    "distinguished from Paula's material funding chain, which did NOT "
    "fail during the crisis and is what carried Jerome through "
    "relocation rather than into destitution (Doc_08 2A-4 L3, "
    "corrected per Round 1 + Doc_07 Round 2)."),
   {"elaboration": (
     "One force, three gravities moved in one year: G3 shifted its "
     "center, G4 became newly indispensable, G5-M received its "
     "operating space - the matrix's clearest demonstration that this "
     "world's authority structure had no institutional buffer against "
     "relational rupture; its structural parallel with the Origenist "
     "rupture (2B-1: one patron's protection lost / one friend's "
     "alliance lost) is a PATTERN, not a coincidence (S2.5 Layer-4 "
     "authoring from Doc_08 SS2's parallel-structure connection).")},
   [{"type": "exposed-by", "target_id": "halforce1A2",
     "note": "Doc_08 index (mirror): the standing 1A-2 conferred is the standing this force prices."},
    {"type": "structurally-parallel-with", "target_id": "halforce2B1",
     "note": ("Doc_08 SS2 (corrected): both show authority vulnerable "
              "through RELATIONSHIP and REPUTATION rather than office - "
              "a patron's protection lost (2A-4), a friend's alliance "
              "lost (2B-1); different registers (clerical-reputational "
              "vs intra-Christian doctrinal), same structural "
              "exposure.")}],
   ["srcHAL001", "srcHAL014", "srcHAL010"]),
 F("halforce2B1",
   "Origenist controversy (Force 2B-1)",
   "2B - Ongoing / Internal",
   ("Theological dispute over Origen's teachings, c. 393-403, "
    "rupturing Jerome's friendship with Rufinus and his relationship "
    "with Bishop John of Jerusalem. Confidence: Documented "
    "(occurrence); Contested (relative doctrinal vs personal/political "
    "weight - the CT tag) (Doc_08 2B-1 L1)."),
   ("A former friend and fellow translator becoming the fiercest of "
    "opponents; a doctrinal inheritance this world had absorbed "
    "without quite noticing, suddenly requiring urgent, public "
    "renunciation (Doc_08 2B-1 L2, From-Within)."),
   ("Anchors G6; reshapes G1 and G3 directly (Pammachius and Marcella "
    "named addressees of Jerome's polemic) (Doc_08 2B-1 L3)."),
   {"elaboration": (
     "The controversy's inner mechanism is the relational-rupture "
     "pattern 2A-4 established, replayed inside the community: "
     "authority resting on trust and alliance, broken by the loss of "
     "one relationship - and conducted THROUGH the patronage network "
     "(the polemic's own addressees are patrons), so the dispute "
     "threatened the very structure that carried it (S2.5 Layer-4 "
     "authoring from Doc_08 SS2 + 2B-1 L3).")},
   [{"type": "structurally-parallel-with", "target_id": "halforce2A4",
     "note": "Doc_08 SS2 (mirror of the parallel-structure connection)."}],
   ["srcHAL005", "srcHAL007", "srcHAL016"]),
 F("halforce2B2",
   "The praefatio and epistula apparatus as the community's own "
   "internal transmission mechanism (Force 2B-2; required Transmission "
   "entry)",
   "2B - Ongoing / Internal (Transmission dimension)",
   ("Jerome's extensive corpus of translation prefaces and letters, "
    "produced continuously throughout the 382-420 span, functioning as "
    "the primary vehicle by which this world transmitted its scholarly "
    "and formation content both within itself (Rome to Bethlehem) and "
    "outward. Confidence: Documented (Doc_08 2B-2 L1)."),
   ("Every finished piece of translation labor accompanied by its own "
    "defense, sent onward to the very household whose funding and "
    "whose questions had occasioned it (Doc_08 2B-2 L2, From-Within)."),
   ("The internal transmission mechanism underlying G4 and, "
    "critically, the vehicle by which this world's CONTENT (G1) "
    "actually reached its own dispersed community and, eventually, a "
    "wider readership - its own named force per the Transmission "
    "Specificity Principle, not folded into the letter-writing gravity "
    "(Doc_08 2B-2 L3)."),
   {"elaboration": (
     "The apparatus's defining property - visible only from the "
     "ending - is that it had exactly ONE practitioner: every preface "
     "argued fresh, in one voice, with no successor attested anywhere "
     "in the record; the mechanism's strength (real-time defense, "
     "book by book) and its fragility (a single point of failure) "
     "were the same fact, which is what 3B-2 records the realization "
     "of (S2.5 Layer-4 authoring from Doc_08 2B-2 + 3B-2's sharpened "
     "L1).")},
   [{"type": "mechanism-lost-at", "target_id": "halforce3B2",
     "note": ("Doc_08 index: 2B-2 -> 3B-2 - the mechanism this force "
              "sustains is what 3B-2 records the loss of.")}],
   ["srcHAL023", "srcHAL001", "srcHAL003"]),
 F("halforce3A1",
   "The 410 Gothic sack of Rome (Force 3A-1)",
   "3A - Ending-or-Transforming / External",
   ("Alaric's forces sack Rome, 24 August 410; Marcella dies from "
    "resulting injuries/deprivation, her Aventine household destroyed "
    "as a site of the wider network. Confidence: Widely Accepted (via "
    "Jerome's Ep. 127; no independent corroboration) (Doc_08 3A-1 "
    "L1)."),
   ("Soldiers demanding treasure at the door of a household that had "
    "already given its treasure away years before (Doc_08 3A-1 L2, "
    "From-Within - the Round-2-corrected rendering, with the "
    "meta-statement about the record removed)."),
   ("Fractures G5-Marcella; ends the Rome-based pole's independent "
    "center of gravity; the single clearest ending-force in this "
    "world's own bounded span (Doc_08 3A-1 L3)."),
   {"elaboration": (
     "An ending that is also a structural revelation: the bipolar "
     "geography this world had maintained by letter for twenty-five "
     "years became unipolar in one event, and the final decade's "
     "Bethlehem concentration is this force's direct product - the "
     "world's own record marks the moment in an epitaph (halstory05) "
     "whose genre-shaped irony the record store carries with the "
     "genre named (S2.5 Layer-4 authoring from Doc_08 3A-1 L3 + "
     "halstory05's caution).")},
   [{"type": "severs", "target_id": "halforce1B1",
     "note": "Doc_08 SS2 (mirror): internal initiative, externally severed, directly."}],
   ["srcHAL001"]),
 F("halforce3A2",
   "The 416 Pelagian mob attack on the Bethlehem monastery (Force "
   "3A-2)",
   "3A - Ending-or-Transforming / External",
   ("Violent attack on the monastery, buildings burned, at least one "
    "death reported; Jerome's own account (letter to Riparius) notably "
    "vague on specifics. Cell placement CORRECTED at Doc_08 Round 2: "
    "moved from 3B (Internal) to 3A (External), deferring to the "
    "actor-origin criterion already established in Doc_04 SS5 and "
    "Doc_06 entry 9. Confidence: Documented (occurrence); "
    "Inferential/Thin (details) (Doc_08 3A-2 L1)."),
   ("A theological argument that had, until then, stayed on paper, "
    "arriving instead as fire at the community's own door (Doc_08 "
    "3A-2 L2, From-Within - Round-2-corrected rendering)."),
   ("Anchors G6 alongside Origenism; an ending-adjacent external "
    "force absorbed by an already-established organizing pattern "
    "rather than generating a new one. The world's own prior "
    "doctrinal position-taking is part of why this force found this "
    "target - retained as a genuine secondary observation that does "
    "not override the actor-origin classification. NO CT tag for "
    "Pelagianism (Doc_08's completed reasoning): an acknowledged "
    "internal uncertainty ('theological conviction and local "
    "grievance') is not a Contested Tradition without an identifiable "
    "external scholarly contest to point to - unlike Origenism's "
    "named, ongoing doctrinal-vs-political literature (Doc_08 3A-2 "
    "L3 + CT decision)."),
   {"elaboration": (
     "The attack closes the arc the desert template opened: a "
     "community organized on a withdrawal model proved reachable by "
     "organized violence, and the record's own restraint about the "
     "particulars (names, numbers, losses - never filled in) becomes "
     "part of the formation content itself: halstory04 tells the "
     "vagueness as honesty, not as gap (S2.5 Layer-4 authoring from "
     "Doc_08 SS2's 2A-3 connection + halstory04's own frame).")},
   [{"type": "context-shaped-by", "target_id": "halforce2A3",
     "note": "Doc_08 SS2 (mirror): the isolation model this violence proved permeable."}],
   ["srcHAL001"]),
 F("halforce3B2",
   "Loss of the praefatio-defense mechanism at the death of its sole "
   "practitioner (Force 3B-2; required Transmission entry - Doc_08's "
   "Cell 3B contains ONLY this entry; there is no force 3B-1, the "
   "numbering is Doc_08's own)",
   "3B - Ending-or-Transforming / Internal (Transmission dimension)",
   ("The transmission apparatus (2B-2) had exactly one practitioner "
    "throughout this world's entire span: Jerome himself. No successor "
    "scholar, editor, or defender of the method is attested anywhere "
    "in this world's own record. At his death (420), this was the "
    "concrete cessation of the specific mechanism by which this world "
    "had continuously argued for and adjusted its own "
    "textual-authority claims in real time - not a generic 'the "
    "makers died' observation. Confidence: Documented (no successor "
    "named - an absence, not an inference); Inferential/Thin (the "
    "counterfactual) (Doc_08 3B-2 L1, Round-1-sharpened)."),
   ("Every book so far had come with its own defense, argued fresh "
    "against whoever objected. After the last preface, no one "
    "remained who could write the next one in the same voice, "
    "answering the same way (Doc_08 3B-2 L2, From-Within)."),
   ("Marks the transformation of G1 from a live, actively-defended "
    "project into a fixed, undefended text whose subsequent reception "
    "(the gradual, uneven displacement of the Vetus Latina) proceeds "
    "without the real-time-defense mechanism that had shaped it - a "
    "concrete transmission-mechanism ending, the direct "
    "internal-transmission counterpart to 3A-1's external ending "
    "force (Doc_08 3B-2 L3)."),
   {"elaboration": (
     "The ending inverts the world's founding irony: a project whose "
     "whole method was contest ('the Vulgate' as later ages know it "
     "is the UNCONTESTED text of a church that no longer remembers "
     "the arguments) - hallex02's anachronism guard and this force "
     "are the same fact seen from opposite ends of the timeline, "
     "which is why the record store keeps the project's in-window "
     "name-lessness and this force's mechanism-loss in the same "
     "world (S2.5 Layer-4 authoring from Doc_08 3B-2 L3 + hallex02's "
     "distortion risk).")},
   [{"type": "records-loss-of", "target_id": "halforce2B2",
     "note": "Doc_08 index (mirror): the mechanism 2B-2 sustains."},
    {"type": "reception-shaped-by", "target_id": "halforce2A2",
     "note": "Doc_08 SS2 Connection 1 (mirror of the third leg)."}],
   ["srcHAL023", "srcHAL002", "srcHAL010"]),
]

# FEC -> gravity_links (CO-P2-04): story -> gravity ids; first link's
# note carries the FULL FEC verbatim, later links a pointer note.
FEC_LINKS = {
    "halstory01": ["halgrav003"],
    "halstory02": ["halgrav003"],
    "halstory03": ["halgrav001", "halgrav004"],
    "halstory03a": ["halgrav006", "halgrav001", "halgrav003"],
    "halstory04": ["halgrav006"],
    "halstory05": ["halgrav005"],
    "halstory06": ["halgrav002"],
    "halstory07": ["halgrav005"],
    "halstory11": ["halgrav001", "halgrav004"],
    # halstory08 (formation-logic TENSION - not a Doc_04 gravity),
    # halstory09 (formation-narrative DIMENSION), halstory10 ('the
    # formation-logic gravity' - the chunk's vocabulary variance,
    # declared: halcore001.formation_logic is not a Doc_04 gravity):
    # links deliberately absent, FEC stays body-parked, S2.8 view
    # falls back to the parking.
}

FEC_RE = re.compile(
    r"\[Formation Ecology Connection - parked at the S2\.4-equivalent"
    r".*?\]\s*(.*?)(?=\n\n\[|\Z)", re.S)


def main():
    for rec, body in GRAVITIES:
        (OUT / "gravity").mkdir(exist_ok=True)
        emit_record(rec, body, OUT / "gravity" / f"{rec['id']}.md")
    for gid, name, reason in NOT_ADVANCED:
        rec = {"world_id": WID, "record_type": "gravity",
               "schema_version": 1, "jobs": [5], "register": "etic",
               "review_state": "draft", "id": gid, "name": name,
               "classification": "not-advanced"}
        emit_record(rec, ("S6.2/HAL S2.5-equivalent not-advanced record "
                          "(2026-07-31; the rule's third non-empty "
                          "extension after ALX/SYR). " + reason),
                    OUT / "gravity" / f"{gid}.md")
    for rec in FORCES:
        (OUT / "force").mkdir(exist_ok=True)
        emit_record(rec, ("S6.2/HAL S2.5-equivalent force record "
                          "(2026-07-31) from " + D8 + " (three layers "
                          "condensed with citations; Layer 4 is THIS "
                          "step's authoring). connections[] = Doc_08 SS2 "
                          "cross-cell links + index columns, mirrored; "
                          "force->gravity tracing lives verbatim in "
                          "layer_formation_impact (Desert S2.5 "
                          "rationale)."),
                    OUT / "force" / f"{rec['id']}.md")
    for sid, gids in FEC_LINKS.items():
        path = OUT / "story" / f"{sid}.md"
        front, body = read_record(path)
        m = FEC_RE.search(body)
        assert m, sid
        fec = m.group(1).strip()
        links = [{"gravity_id": gids[0], "note": (
            "CO-P2-04: the chunk's Formation Ecology Connection, verbatim "
            "(the S2.4 parking, converted at S2.5): " + fec)}]
        for g in gids[1:]:
            links.append({"gravity_id": g, "note": (
                "Named in the same FEC (full text on this record's first "
                "gravity link).")})
        front["gravity_links"] = links
        write_record(path, front, body)
    core_path = OUT / "world_core" / "halcore001.md"
    front, body = read_record(core_path)
    front["gravities"] = [g[0]["id"] for g in GRAVITIES]
    write_record(core_path, front, body)
    print(f"wrote {len(GRAVITIES)} confirmed + {len(NOT_ADVANCED)} "
          f"not-advanced gravities, {len(FORCES)} forces, "
          f"{len(FEC_LINKS)} stories linked (3 declared unlinked), "
          f"core updated")


if __name__ == "__main__":
    main()
