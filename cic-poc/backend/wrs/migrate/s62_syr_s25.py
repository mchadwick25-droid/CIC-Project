"""S6.2/Syriac - S2.5-equivalent: gravities + forces + FEC conversion.

- 12 gravity records: 6 confirmed (C1-C6, Doc_04 SS2's per-candidate
  six-test prose - which, UNLIKE ALX, carries every candidate's full
  grid and the complete SS3 matrix in prose; the Gravity_Index.xlsx
  audit rides close-out) + 6 not-advanced (Doc_04 SS1, the
  not-advanced-kept-as-records rule).
- 13 force records (Doc_08 SS3's six-cell matrix): three layers
  condensed-verbatim with citations; Layer 4 is THIS step's authoring
  (elaboration, or considered stasis for 1B-2 and 1B-3 - Doc_08's own
  'held steadily' findings); connections[] = Doc_08 SS4's eight named
  cross-cell connections, mirrored; force->gravity tracing lives
  verbatim in layer_formation_impact (the Desert S2.5 rationale).
- FEC conversion (CO-P2-04): the S2.4 FEC parkings become typed
  gravity_links on 6 of 9 stories (first link's note = full FEC
  verbatim). THREE stories' FECs name NO gravity - syrstory002 (archive-
  memory character), syrstory006 (cites FORCE 1A-2, its own Round-1
  correction away from over-claiming), syrstory008 (excluded-legend
  documentation) - their FECs stay body-parked, DECLARED; the S2.8
  chunk view must render FEC from the body parking for these three.
- syrcore001.gravities closed at the 6 confirmed (FLAG-023 reader).

Layer-4 stasis considered at exactly 2 (1B-2 qyama held; 1B-3
Diatessaron held in-window - its transformation is 3B-2's own story).
"""
import re
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
sys.path.insert(0, str(HERE))

from source_rows_from_doc02 import emit_record
from s62_syr_s23 import read_record, write_record

OUT = BACKEND / "wrs" / "records" / "syriac_world"
WID = "syriac-edessa-nisibis"
D4 = "Doc_04_Gravity_Discovery.md (read in full this step)"

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
 G("syrgrav001",
   "Symbolic/Typological Theological Method - raza/shrara (C1)", "Primary",
   {"repetition": ("PASS - recurs across Ephrem's madrashe, prose "
                   "refutations, and biblical commentaries (Doc_02 SS2) and "
                   "in Aphrahat's typological Christ-figuration (lighter); "
                   "multiple evidence streams (Doc_04 C1)."),
    "dependency": ("PASS - the substrate other claims about Ephrem's "
                   "'doctrinal method' depend on; C3's rhetoric draws on "
                   "this same hermeneutic (Doc_04 C1)."),
    "formation": ("PASS - directly shapes how participants encountered "
                  "doctrine: through symbol and type rather than syllogism "
                  "(Doc_01 SS4; Doc_02 SS3; Doc_04 C1)."),
    "explanatory": ("PASS - explains the madrasha genre-choice, the "
                    "exegetical commentaries, and both authors' OT "
                    "approach (Doc_04 C1)."),
    "persistence": ("PASS - across Ephrem's whole corpus (350s-373) and "
                    "Aphrahat's earlier Demonstrations (336/7-345) - the "
                    "bulk of the window (Doc_04 C1)."),
    "interaction": ("PASS - reinforces C3 (same typological logic deployed "
                    "polemically) and C5 (the Diatessaron read through this "
                    "method) (Doc_04 C1, SS3).")},
   ("Documented for Ephrem's own textual practice; Widely Accepted for "
    "Aphrahat's lighter parallel - aligned, no divergence to flag. Author "
    "Gravity moderate-high: the fullest articulation (hayla kasya) is "
    "substantially Brock's synthesis of Ephrem specifically; tested as an "
    "Ephrem-anchored gravity with a genuinely attested lighter Aphrahat "
    "parallel, never as equally weighted (Doc_04 C1)."),
   [{"type": "reinforcing", "target_id": "syrgrav002",
     "note": "Doc_04 SS3: Ephrem's ascetic-teacher voice (Doc_02 SS3) expresses the raza/shrara method."},
    {"type": "reinforcing", "target_id": "syrgrav003",
     "note": "Doc_04 SS3: the same typological logic deployed polemically."},
    {"type": "reinforcing", "target_id": "syrgrav005",
     "note": "Doc_04 SS3: the Diatessaron read through this same method."}],
   ["srcSYR001", "srcSYR002", "srcSYR007", "srcSYR010", "srcSYR029"],
   ("S6.2/SYR S2.5-equivalent gravity record (2026-07-28) from " + D4 +
    ". Forces-connection (Doc_04 C1): INTENSIFIED under the doctrinal-"
    "rivalry pressure (sharper, more explicitly polemical in the Prose "
    "Refutations and Contra Haereses) - held, deployed more pointedly; "
    "never fractured. See syrforce1B1/syrforce2A2.")),
 G("syrgrav002",
   "Covenanted Ascetic Life - qyama / bnay-bnat qyama / Ihidaya (C2)", "Primary",
   {"repetition": ("PASS - Aphrahat Dem 6 (direct) + the Ihidaya material "
                   "(both authors, directly; Doc_03 1.7) (Doc_04 C2)."),
    "dependency": ("PASS - the world's cultural/institutional scope is "
                   "partly defined by this institution; Doc_02 SS7's "
                   "missing-voices analysis depends on it (Doc_04 C2)."),
    "formation": ("PASS - directly organized lived practice: vow-taking, "
                  "town-resident celibacy, communal identity distinct from "
                  "desert monasticism (Doc_04 C2)."),
    "explanatory": ("PASS - explains the ascetic-clerical register of the "
                    "surviving corpus and the structural absence of "
                    "lay/ordinary voices (Doc_04 C2)."),
    "persistence": ("PASS - from Aphrahat's earliest Demonstrations "
                    "(336/7) onward within the window (Doc_04 C2)."),
    "interaction": ("PASS - reinforces C1 and (Round 2) RESHAPES C4: the "
                    "qyama's charismatic/ascetic leadership is itself one "
                    "of the two authority-legitimation pathways at stake; "
                    "C2xC6 honestly no-relationship (the persecution "
                    "record centers on the episcopal hierarchy, no "
                    "evidence qyama members were targeted as a group) "
                    "(Doc_04 C2, SS3).")},
   ("Documented for BOTH remaining evidentiary streams - the direct "
    "result of Round 2's narrowing, which EXCLUDED the Ephrem-personal-"
    "choir-leadership claim from this candidate's evidentiary basis "
    "entirely (its primary attestation - Jacob of Serugh; the Vita "
    "Ephraemi - is 6th-century, outside the 200-410 boundary; recorded "
    "in Section 1 as not-advanced, syrgrav010). 'Now cleanly earned "
    "rather than borrowed from an attached weaker claim' (Doc_04 C2)."),
   [{"type": "reinforcing", "target_id": "syrgrav001",
     "note": "Mirror of syrgrav001's edge (Doc_04 SS3)."},
    {"type": "reshaping", "target_id": "syrgrav004",
     "note": ("Doc_04 SS3 (Round 2 upgrade): the qyama order's own "
              "charismatic/ascetic leadership is an alternative authority-"
              "legitimation pathway to episcopal consecration - part of "
              "C4's own plurality.")}],
   ["srcSYR010", "srcSYR013", "srcSYR032", "srcSYR033"],
   ("S6.2/SYR S2.5-equivalent gravity record (2026-07-28) from " + D4 +
    ". Forces-connection (Doc_04 C2): NO forces-dynamic manufactured - "
    "the gravity HELD steadily as a stable institutional form across the "
    "window; 'not every gravity is forces-reactive.' See syrforce1B2 "
    "(stasis Layer 4).")),
 G("syrgrav003",
   "Heresiological Self-Definition Against Named Rivals - Bardaisan, Marcion, Mani (C3)", "Supporting",
   {"repetition": ("PASS within Ephrem's corpus specifically - Prose "
                   "Refutations, Contra Haereses, and the madrasha "
                   "genre-choice itself (adopted partly to out-compete "
                   "Bardaisan's and Mani's own madrashe, per Brock) "
                   "(Doc_04 C3)."),
    "dependency": ("PASS - Doc_01's Bardaisan clearance test and Strand "
                   "Determination depend on this boundary-work being real "
                   "(Doc_04 C3)."),
    "formation": ("PASS - orthodoxy understood not as abstract position "
                  "but as defined against specific, named, locally-known "
                  "rivals (Doc_04 C3)."),
    "explanatory": ("PASS - explains the Prose Refutations' existence, the "
                    "triad's recurring co-mention, and the world's "
                    "Bardaisan floor-proximity (Doc_04 C3)."),
    "persistence": ("PARTIAL PASS - persists within Ephrem's own lifetime "
                    "and corpus; NOT demonstrated as persisting world-wide "
                    "across the full 200-410 span (the 373-410 inventory "
                    "does not surface it) (Doc_04 C3)."),
    "interaction": ("PASS - reinforces C1; competes with the hypothetical "
                    "'ignore heterodox neighbors' alternative the record "
                    "shows was not taken; C3-C6 honestly no-relationship "
                    "(different registers and regions) (Doc_04 C3).")},
   ("Documented that Ephrem wrote against this triad; Widely Accepted "
    "that this shaped his genre-choice (Brock). Author Gravity HIGH: "
    "almost entirely Ephrem's own corpus (Ruani: 'the founder of Syriac "
    "heresiology outright'); Aphrahat never engages the triad by name. "
    "Tested as an Ephrem-specific gravity - the clearest regional/author "
    "concentration in Doc_04, kept below Primary for exactly that reason "
    "(Doc_04 C3)."),
   [{"type": "reinforcing", "target_id": "syrgrav001",
     "note": "Mirror of syrgrav001's edge (Doc_04 SS3)."}],
   ["srcSYR002", "srcSYR007", "srcSYR014", "srcSYR023"],
   ("S6.2/SYR S2.5-equivalent gravity record (2026-07-28) from " + D4 +
    ". Forces-connection (Doc_04 C3): exists BECAUSE OF the external "
    "pressure of real rival movements; INTENSIFIED under it (sustained "
    "genre-spanning campaigns); Ephrem's death (373) is where the record "
    "ends, not a documented fracture point. See syrforce2A2.")),
 G("syrgrav004",
   "Authority-Structure Ambiguity - Charismatic-Teacher Standing vs. Episcopal Legitimacy (C4)", "Tensional",
   {"repetition": ("PASS - recurs across Doc_01's Strand Determination, "
                   "the Persian succession material (multi-see but "
                   "severely disrupted incl. the twenty-year vacancy), and "
                   "the unresolved Aphrahat-status question (Doc_04 C4)."),
    "dependency": ("PASS - Doc_01's strand-singular conclusion explicitly "
                   "rests on bracketing this question (Doc_04 C4)."),
    "formation": ("FAIL, carried forward openly (Round 2 correction, "
                  "never smoothed into a nominal pass): the evidence "
                  "speaks to modern reconstruction difficulty, not to how "
                  "the ambiguity was actively lived - consistent with, "
                  "not disqualifying for, the Tensional classification "
                  "(Doc_04 C4)."),
    "explanatory": ("PASS - explains why Strand Determination could not "
                    "resolve cleanly and why Aphrahat's own title remains "
                    "a live question (Doc_04 C4)."),
    "persistence": ("PASS - across the documented Persian succession's "
                    "full span (280s-410) and Aphrahat's career: a "
                    "sustained condition, not a momentary gap (Doc_04 "
                    "C4)."),
    "interaction": ("PASS - RESHAPED BY C6 (the twenty-year vacancy is a "
                    "product of persecution-era disruption) and by C2 "
                    "(the qyama pathway is part of the plurality) (Doc_04 "
                    "C4, SS3).")},
   ("THE clearest intentional divergence in Doc_04: underlying facts "
    "Widely Accepted to Documented (multi-see structure; Aphrahat "
    "unresolved; the vacancy); how the ambiguity functioned as a LIVED "
    "organizing reality Contested/Inferential-Thin. Named explicitly, "
    "not resolved by upgrading (Doc_04 C4). Step-5 open item: find lived "
    "evidence if any exists rather than let the classification "
    "substitute for it."),
   [{"type": "reshaping", "target_id": "syrgrav002",
     "note": "Mirror of syrgrav002's edge - DIRECTION: C2 reshapes C4 (this record is the reshaped side; the enum carries no inverse, the note does - ALX C2-T4 pattern) (Doc_04 SS3)."},
    {"type": "reshaping", "target_id": "syrgrav006",
     "note": ("Doc_04 SS3: persecution reshaped the succession's own "
              "continuity - the vacancy as documented fracture.")}],
   ["srcSYR010", "srcSYR042", "srcSYR051"],
   ("S6.2/SYR S2.5-equivalent gravity record (2026-07-28) from " + D4 +
    ". Forces-connection (Doc_04 C4): the Persian succession's continuity "
    "FRACTURED under Shapur II's persecution (the twenty-year vacancy "
    "after Barba'shmin - independently documented, not inferred). "
    "Two-road causal profile per Doc_07 SS3 carried at syrforce2B1: "
    "substantially forced (Persian side) vs not-clearly-forced "
    "(Aphrahat's own status ambiguity).")),
 G("syrgrav005",
   "The Diatessaron as Normative Harmonized Gospel (C5)", "Supporting",
   {"repetition": "PASS - attested in both Aphrahat and Ephrem, independently (Doc_04 C5).",
    "dependency": ("PASS - Ephrem's whole Commentary depends on the text's "
                   "normative status; the later transition is only a "
                   "meaningful boundary because normativity preceded it "
                   "(Doc_04 C5)."),
    "formation": ("PASS - the Gospel encountered as a single harmonized "
                  "text, a materially different formation experience than "
                  "the post-410 world (Doc_04 C5)."),
    "explanatory": ("PASS - explains the Commentary's unusual textual "
                    "investment and why the shift to the separated "
                    "Gospels counts as a real world-transition (Doc_04 "
                    "C5)."),
    "persistence": ("PASS, BOUNDED - attested 330s-340s (Aphrahat) "
                    "through the 360s-370s (Ephrem's Commentary); "
                    "understood to end at/near the 410 boundary - "
                    "appropriate, not a weakness (Doc_04 C5)."),
    "interaction": ("PASS - reinforces C1; stands in a documented "
                    "'ending' relationship with the world's own boundary "
                    "(Doc_04 C5, SS3).")},
   ("Documented for the Diatessaron's use and content in-window; "
    "Contested for the vernacular name's own dating (Doc_03 1.6, the "
    "syrlex006 CT) - a separate, narrower issue that does not undercut "
    "the classification (Doc_04 C5)."),
   [{"type": "reinforcing", "target_id": "syrgrav001",
     "note": "Mirror of syrgrav001's edge (Doc_04 SS3)."}],
   ["srcSYR009", "srcSYR010", "srcSYR011", "srcSYR028"],
   ("S6.2/SYR S2.5-equivalent gravity record (2026-07-28) from " + D4 +
    ". Forces-connection (Doc_04 C5): HELD steadily throughout the "
    "window; its supersession (early 5th c., under/after Rabbula) is the "
    "world's own closing transition, not a mid-window forces-response. "
    "See syrforce1B3 (stasis Layer 4) and syrforce3B2.")),
 G("syrgrav006",
   "Endurance Under State Persecution as a Formation Ideal (C6)", "Supporting",
   {"repetition": ("PASS within the Persian-context stream - Dem 5 ('On "
                   "Wars'), Dems 21-23 (344-345, during active "
                   "persecution), and the multi-decade martyrological "
                   "record (Doc_04 C6)."),
    "dependency": ("PASS - Doc_02's framing of Aphrahat's 'defensive, "
                   "apologetic register' depends on this pressure being "
                   "real and sustained (Doc_04 C6)."),
    "formation": ("PASS - directly shaped Aphrahat's pastoral address; "
                  "Doc_02 names it as shaping 'the Persian side of this "
                  "world as reconstructed here' (Doc_04 C6)."),
    "explanatory": ("PASS - explains the tone shift between Aphrahat's "
                    "earlier and later Demonstrations and the twenty-year "
                    "vacancy as structural consequence (Doc_04 C6)."),
    "persistence": ("PASS within the Persian stream - the persecution "
                    "spans the 340s through the 370s (Doc_04 C6)."),
    "interaction": ("PASS - reshapes C4 (via the vacancy); two honest "
                    "no-relationship findings (C3, C5 - different "
                    "registers and regions) (Doc_04 C6, SS3).")},
   ("Widely Accepted to Documented for the persecution and its "
    "succession effects; Widely Accepted for its shaping of Aphrahat's "
    "text. Author Gravity HIGH: almost entirely Aphrahat/Persian-side - "
    "the second-clearest regional concentration after C3, kept "
    "Supporting for the same structural reason (Doc_04 C6)."),
   [{"type": "reshaping", "target_id": "syrgrav004",
     "note": ("Doc_04 SS3: persecution reshaped the succession's own "
              "continuity (the vacancy).")}],
   ["srcSYR010", "srcSYR042", "srcSYR046"],
   ("S6.2/SYR S2.5-equivalent gravity record (2026-07-28) from " + D4 +
    ". Forces-connection (Doc_04 C6): this gravity IS ITSELF the "
    "community's organizing response to Sasanian persecution - the most "
    "direct force-to-gravity relationship in the document; INTENSIFIED "
    "through the 340s while the surrounding episcopal structure "
    "FRACTURED; the endurance ideal itself persisted past the acute "
    "crisis (Tomarsa's restoration; the 410 toleration). See "
    "syrforce2A1.")),
]

NOT_ADVANCED = [
 ("syrgrav007", "Source-record asymmetry / silenced voices (not advanced)",
  ("Doc_04 SS1: characterizes a limitation of the evidence base itself - "
   "what is missing from the record - not an organizing commitment the "
   "community centered its own formation on. Remains load-bearing for "
   "the Affirmative Duty (Article 20).")),
 ("syrgrav008", "Edessa's Roman-administered political status (not advanced)",
  ("Doc_04 SS1: background/force context (an external political fact), "
   "not an internal organizing commitment - carried into the "
   "forces-connection notation (syrforce1A1) instead.")),
 ("syrgrav009", "The Diatessaron-to-Peshitta transition itself (not advanced)",
  ("Doc_04 SS1: a temporal/textual-transition event at the world's own "
   "closing edge, not a sustained organizing gravity within the window; "
   "the Diatessaron's normative use IS tested (C5/syrgrav005); the "
   "transition is syrforce3B2's story.")),
 ("syrgrav010", "Ephrem's personal leadership of the bnat qyama choirs (not advanced; Round 2)",
  ("Doc_04 SS1 (Round 2): real and worth naming, but its primary "
   "attestation (Jacob of Serugh's 6th-c. panegyric; the 6th-c. Vita "
   "Ephraemi) falls OUTSIDE the 200-410 boundary - later "
   "reception-history, excluded from C2's own evidentiary basis "
   "entirely, belonging to Doc_09 (told as syrstory007 with the "
   "later-attribution frame). Any future document must preserve this "
   "exclusion rather than quietly reintroducing the claim as in-window "
   "fact (Doc_04 SS5).")),
 ("syrgrav011", "Ephrem's attested clerical office - deacon (not advanced; Round 2)",
  ("Doc_04 SS1 (Round 2): real and well-sourced (Jerome, De Viris "
   "Illustribus 115: 'deacon of the church of Edessa') - but it "
   "functions as a comparandum data point WITHIN C4's analysis (one "
   "figure's personal standing), not a community-wide practice or "
   "commitment.")),
 ("syrgrav012", "Formation-narrative/civic memory - Doctrina Addai, Chronicle of Edessa (not advanced; Round 2)",
  ("Doc_04 SS1 (Round 2): Doc_02 SS5 frames these as this world's own "
   "foundation myth and archival record respectively, not attested "
   "organizing practices - the Doctrina's historical claims are "
   "explicitly non-historical per Doc_01. Their story-repository homes "
   "are syrstory004 and syrstory002.")),
]

D8 = "Doc_08_Forces_Document.md"

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
 F("syrforce1A1",
   "Edessa as Roman-Administered, Culturally Distinct Frontier Periphery Amid a Plural Local Religious Milieu (Force 1A-1)",
   "1A - Initiating / External",
   ("Osroene a Roman client kingdom from c. 132 BCE moving to full "
    "provincialization (Abgar IX's execution under Caracalla c. 213; "
    "annexation 214); Edessa inside the Roman system yet "
    "linguistically/culturally Aramaic-Syriac; the religious ecology "
    "genuinely plural - paganism, a significant Jewish community, "
    "Marcionite Christianity, Bardaisan's own following at Abgar VIII's "
    "court. Confidence: Widely Accepted (political facts); DMR for the "
    "'Roman-administered periphery' characterization (Doc_08 1A-1 L1)."),
   ("A community that came to hold its own shrara as something spoken, "
    "sung, and argued in Aramaic - not needing Greek's categorical "
    "apparatus because the raza already bound word to reality; formed "
    "among neighbors who were not distant heresiarchs but people one "
    "could meet in the street. [Reported-Experience Status: the world "
    "left no text on its own political-administrative situation; this "
    "rendering is the document's own, grounded in Doc_01 SS4/SS7 and "
    "Doc_02 SS8] (Doc_08 1A-1 L2)."),
   ("The initiating condition for TWO confirmed gravities at once: raw "
    "material for C1 (doctrine in Aramaic raza/shrara form) and C3 "
    "(self-definition against locally-present rivals from the outset, "
    "not after the fact) (Doc_08 1A-1 L3; SS5 C1/C3 entries)."),
   {"elaboration": (
     "The initiating plurality never resolved into a settled backdrop - it "
     "became the ongoing condition itself: the same rivals present at "
     "origin persisted as living presences requiring career-spanning "
     "response (Connection 1), so that by the horizon's end the "
     "periphery's plural milieu existed inside the ecology as its "
     "boundary-work (C3), no longer merely around it (S2.5 Layer-4 "
     "authoring from Doc_08 SS4 Connection 1).")},
   [{"type": "continues-as", "target_id": "syrforce2A2",
     "note": ("Doc_08 SS4 Connection 1: the initiating condition and the "
              "ongoing pressure are the same force continuing, not two "
              "unrelated facts.")}],
   ["srcSYR021", "srcSYR023", "srcSYR035"]),
 F("syrforce1A2",
   "The Roman-Persian Mesopotamian Frontier as a Bifurcated Political Origin Condition (Force 1A-2)",
   "1A - Initiating / External",
   ("The world's scope spans two polities from origin: Roman "
    "Osroene/Edessa and (from 224) Sasanian Persia; Nisibis a third, "
    "unstable position - contested through the 3rd c., Roman from 298 "
    "(Peace of Nisibis), ceded to Persia 363. Confidence: Widely "
    "Accepted (political facts); DMR for one-world-not-two (Doc_08 "
    "1A-2 L1)."),
   ("The same qyama, the same harmonized Gospel, the same reading by "
    "raza belonged to people who addressed very different rulers and "
    "very different immediate dangers - a shared formation logic "
    "carried across a political line its participants did not choose. "
    "[Reported-Experience Status: the document's own synthetic "
    "rendering; no surviving text names 'living under two empires'] "
    "(Doc_08 1A-2 L2)."),
   ("The single most consequential initiating force for the asymmetric "
    "later history: the structural precondition for Ephrem's "
    "doctrinal-rivalry concentration (C3) vs Aphrahat's "
    "persecution-endurance concentration (C6), the differing boundary "
    "logics, and the two differing ending fates (Doc_08 1A-2 L3)."),
   {"elaboration": (
     "The bifurcation's condition changed by working itself out: what "
    "began as a geographic fact became, decades later, the shape of "
    "the world's own ending - a Persian-side institutional "
    "consolidation under external recognition and a Roman-side "
    "scriptural-transmission shift, 'not one uniform ending "
    "experienced identically by both anchor contexts' (S2.5 Layer-4 "
    "authoring from Doc_08 SS4's cross-cell pattern reading).")},
   [{"type": "structural-precondition-for", "target_id": "syrforce2A1",
     "note": ("Doc_08 SS4 Connection 2: the bifurcation is the "
              "precondition for the Persian context's distinctive "
              "exposure to state persecution - an asymmetric "
              "ongoing-force experience produced by the initiating "
              "geographic condition.")}],
   ["srcSYR021", "srcSYR035", "srcSYR004"]),
 F("syrforce1B1",
   "Inherited Commitment to Symbolic/Typological Theological Method over Greek Categorical Argument (Force 1B-1)",
   "1B - Initiating / Internal",
   ("Theological expression took poetic, exegetical, symbolic form from "
    "the earliest attested voices - Ephrem's primary vehicle hymnody, "
    "not treatise; Brock's documented argument: raza is bound to shrara "
    "and carries the truth's 'hidden power.' Confidence: DMR that this "
    "characterizes the world's method generally; Documented for "
    "Ephrem's own practice (Doc_08 1B-1 L1)."),
   ("A raza is not a sign chosen by convention; to read Scripture or "
    "creation rightly is to perceive connections already woven into the "
    "world by its Maker. [Documented for Ephrem's corpus; the "
    "'inherited disposition present from the earliest period' claim is "
    "the document's own synthesis at DMR] (Doc_08 1B-1 L2)."),
   ("The direct seed of C1 (Primary). Later intensifies under "
    "doctrinal-rivalry pressure rather than remaining static (Doc_08 "
    "1B-1 L3)."),
   {"elaboration": (
     "Changed in degree though not in kind: under Force 2A-2's "
     "sustained pressure the method sharpened into explicitly polemical "
     "form (Prose Refutations, Contra Haereses) - an initiating "
     "internal commitment measurably intensified by a later external "
     "force acting on it (S2.5 Layer-4 authoring from Doc_08 SS4 "
     "Connection 4).")},
   [{"type": "intensified-by", "target_id": "syrforce2A2",
     "note": ("Doc_08 SS4 Connection 4 (mirror): ongoing rivalry "
              "intensified the inherited method.")}],
   ["srcSYR001", "srcSYR029"]),
 F("syrforce1B2",
   "Early Institutional Commitment to the Qyama Covenant-Order (Force 1B-2)",
   "1B - Initiating / Internal",
   ("The bnay/bnat qyama first clearly attested in Aphrahat's "
    "Demonstration 6 (337) - addressed as already established, needing "
    "correction more than founding, so the institution predates its own "
    "attestation by an unestablished margin. Confidence: Widely "
    "Accepted (existence, ascetic-communal character); "
    "Inferential/Thin for how much earlier than 337 (Doc_08 1B-2 L1)."),
   ("To take the qyama is to stand for a promise that does not end - a "
    "lifelong undertaking lived among one's own kin rather than in "
    "flight from them. [Documented core per Dem 6; the early-origin "
    "claim is the document's own inference from the 'already "
    "established' framing] (Doc_08 1B-2 L2)."),
   ("The direct seed of C2 (Primary). Doc_04 found NO forces-connection "
    "showing this gravity shifting under pressure within the window - "
    "it held steadily; C2's own force-relationship, honestly, is this "
    "single initiating one (Doc_08 1B-2 L3)."),
   {"stasis": True},
   [{"type": "supplies-plurality-of", "target_id": "syrforce2B1",
     "note": ("Doc_08 SS4 Connection 8: the qyama's charismatic, "
              "vow-based standing is itself one of the authority-"
              "legitimation pathways making up the ambiguity's own "
              "plurality (C2 reshaping C4) - a gravity-to-gravity "
              "relationship carried as a connection between the forces "
              "that respectively initiate and sustain those gravities.")}],
   ["srcSYR010", "srcSYR013"]),
 F("syrforce1B3",
   "Early Adoption of the Diatessaron as the Normative Harmonized Gospel (Force 1B-3)",
   "1B - Initiating / Internal",
   ("Tatian's Diatessaron (c. 172) the standard lectionary text early "
    "enough to be the shared narrative spine both authors attest "
    "independently; normative until displaced by the Peshitta in the "
    "early 5th c. Confidence: Documented (normative use in-window); "
    "Contested for downstream particulars (Dura-Europos identification; "
    "original language) (Doc_08 1B-3 L1)."),
   ("The Gospel, encountered in this world, is not four witnesses held "
    "in tension but one unbroken story. [Documented use per both "
    "authors; the inhabited-experience framing is the document's own "
    "rendering] (Doc_08 1B-3 L2)."),
   ("The direct seed of C5 (Supporting). No forces evidence shows it "
    "shifting within the window; its supersession is the world's own "
    "closing transition (Doc_08 1B-3 L3)."),
   {"stasis": True},
   [{"type": "bookends-with", "target_id": "syrforce3B2",
     "note": ("Doc_08 SS4 Connection 7: the same textual choice that "
              "gave the world its earliest scriptural shape is the one "
              "whose supersession marks the transmission-level break - "
              "beginning and ending as bookends of a single "
              "textual-transmission arc.")}],
   ["srcSYR009", "srcSYR010", "srcSYR011"]),
 F("syrforce2A1",
   "Sasanian State Persecution Under Shapur II (Force 2A-1)",
   "2A - Ongoing / External",
   ("Intensifying from the 340s through the 370s: the 'Great Massacre' "
    "(c. 344-345); Simeon bar Sabbae (traditional 341, Kosinski/Burgess "
    "argue c. 344 - a live dispute carried at full strength); Shahdost; "
    "Barba'shmin followed by the roughly twenty-year primatial vacancy; "
    "Milles of Susa, Acepsimas, Mareas, Bicor, roughly twenty other "
    "bishops and 250 clergy. Confidence: Widely Accepted to Documented; "
    "Contested at exact dates (Doc_08 2A-1 L1)."),
   ("Aphrahat writes his later Demonstrations into a community that has "
    "already watched its bishops die and does not know how many more it "
    "will watch die - pastoral address to people deciding in their own "
    "bodies whether the promises are strong enough. A twenty-year "
    "silence follows Barba'shmin's death. [The vacancy's outward fact "
    "Documented; its lived interior not attested and not invented] "
    "(Doc_08 2A-1 L2)."),
   ("The most direct force-to-gravity connection in the document: C6 IS "
    "the community's organizing response to this force; it also "
    "FRACTURES C4 (the vacancy as documented fracture of the "
    "succession) (Doc_08 2A-1 L3)."),
   {"elaboration": (
     "The force's own arc completes outside itself: it produced the "
     "endurance ideal (C6), fractured the succession (C4), and its "
     "cessation under Yazdegerd I (399) is what makes the 410 "
     "consolidation possible - the Ending cell as the resolution-point "
     "of this Ongoing force's own history (S2.5 Layer-4 authoring from "
     "Doc_08 SS4 Connections 3 and 5).")},
   [{"type": "structurally-preconditioned-by", "target_id": "syrforce1A2",
     "note": "Doc_08 SS4 Connection 2 (mirror)."},
    {"type": "fractures", "target_id": "syrforce2B1",
     "note": ("Doc_08 SS4 Connection 3: the twenty-year vacancy is a "
              "direct, documented instance of this force fracturing the "
              "authority structure (and through it C4) - the clearest "
              "single forces-to-gravity causal chain in the document.")},
    {"type": "resolved-by", "target_id": "syrforce3A1",
     "note": ("Doc_08 SS4 Connection 5 (mirror): the toleration is "
              "intelligible only against the persecution it ends.")}],
   ["srcSYR042", "srcSYR046", "srcSYR048"]),
 F("syrforce2A2",
   "Sustained Doctrinal Rivalry from Bardaisan's Circle, Marcion's Currents, and Manichaean Missionary Activity (Force 2A-2)",
   "2A - Ongoing / External",
   ("Bardaisan's following persisted in Edessa roughly two centuries "
    "after his death (154-222; Rabbula moved against it 411-435; "
    "adherents still attested in the 7th-8th c.); Marcionite "
    "Christianity and, from the 3rd c., Manichaean missionary activity "
    "occupied the same milieu throughout. The Prose Refutations and "
    "Contra Haereses attest sustained career-spanning engagement. "
    "Confidence: Documented (the refutations); Widely Accepted (the "
    "genre-shaping claim) (Doc_08 2A-2 L1)."),
   ("A hearer of Ephrem's refutations encounters Bardaisan, Marcion, "
    "and Mani not as textbook heresiarchs but as real, remembered "
    "neighbors; holding the faith rightly is an active, ongoing act of "
    "telling truth apart from a plausible-sounding neighbor. "
    "[Documented; substantially one figure's own rhetorical achievement "
    "rather than an even world-wide practice - preserved, not "
    "smoothed] (Doc_08 2A-2 L2)."),
   ("Sustains and INTENSIFIES C1 (the method sharpened polemically) and "
    "directly produces C3 (concentrated in Ephrem's corpus and the "
    "Roman/Edessene context) (Doc_08 2A-2 L3)."),
   {"elaboration": (
     "Under this pressure the inherited method's condition changed in "
     "degree (not kind) - sharpened into explicit polemic - and the "
     "genre itself became part of the contest (madrashe answering "
     "madrashe on the rivals' own ground); the boundary the rhetoric "
     "constructed became the world's own orthodox/heretic line "
     "(Ruani: constructive, not merely descriptive) (S2.5 Layer-4 "
     "authoring from Doc_08 2A-2 L2/L3 + Doc_02 SS3).")},
   [{"type": "continuation-of", "target_id": "syrforce1A1",
     "note": "Doc_08 SS4 Connection 1 (mirror)."},
    {"type": "intensifies", "target_id": "syrforce1B1",
     "note": ("Doc_08 SS4 Connection 4: the method sharpened into "
              "explicitly polemical form under this pressure.")}],
   ["srcSYR007", "srcSYR002", "srcSYR014", "srcSYR023"]),
 F("syrforce2B1",
   "The Persistent, Unresolved Authority-Structure Ambiguity (Force 2B-1)",
   "2B - Ongoing / Internal",
   ("More than one channel of teaching and communal authority without "
    "clean subordination: ordained episcopal office (real but fragile - "
    "Papa bar Aggai's primacy fiercely contested by Miles of Susa and "
    "Aqib-Alaha c. 315; the two-decade vacancy); the qyama's vowed "
    "charismatic-ascetic standing; Aphrahat's textual-exegetical "
    "authority with his own office unresolved. Confidence: Widely "
    "Accepted to Documented (facts); Contested/Inferential-Thin (lived "
    "functioning) - the C4 divergence carried forward (Doc_08 2B-1 "
    "L1)."),
   ("A practitioner received formation from more than one authority "
    "pathway at once - text, office where it held, vowed example - "
    "without a settled hierarchy resolving final say. "
    "[Reported-Experience Status; Doc_04's own Formation-test FAIL "
    "carried honestly] (Doc_08 2B-1 L2)."),
   ("Effectively coextensive with C4 itself (Tensional) - the named "
    "exception to the force/gravity distinction: a persistent "
    "unresolved condition, not an organized response. TWO distinct "
    "causal profiles preserved per Doc_07 SS3: substantially forced "
    "(Persian side, via 2A-1's fracture) and not-clearly-forced "
    "(Aphrahat's own status) (Doc_08 2B-1 L3)."),
   {"elaboration": (
     "The condition persisted under its own continued absence of "
     "resolution until resolved from OUTSIDE: the 410 Synod supplied, "
     "under state recognition, the settled structure the world's own "
     "resources never produced across its whole span - which is "
     "precisely what makes 410 a genuine ending (S2.5 Layer-4 "
     "authoring from Doc_08 3B-1 L3 + SS5 C4 arc).")},
   [{"type": "fractured-by", "target_id": "syrforce2A1",
     "note": "Doc_08 SS4 Connection 3 (mirror)."},
    {"type": "plurality-supplied-by", "target_id": "syrforce1B2",
     "note": "Doc_08 SS4 Connection 8 (mirror)."},
    {"type": "resolved-by", "target_id": "syrforce3B1",
     "note": ("Doc_08 SS5 C4 arc: sustained by this force, resolved "
              "only by the externally-brokered consolidation.")}],
   ["srcSYR010", "srcSYR042", "srcSYR051"]),
 F("syrforce2B2",
   "Transmission - Who Carried This World's Material Forward, Under What Conditions, With What Selection Effects (Force 2B-2)",
   "2B - Ongoing / Internal (Transmission dimension)",
   ("Ephrem survives principally through BL Add. 14571 (519 CE) with "
    "Beck's CSCO editions as the authenticity baseline (incl. the "
    "Epiphany-hymns inauthenticity argument from Nisibis's combined "
    "Nativity-Baptism feast); 'Ephraem Graecus' largely later "
    "pseudonymous composition (Amar). Aphrahat survives far more "
    "thinly: BL Add. 17182 (474/510 CE; Dems 11-12 absent from the "
    "witness), BL Add. 14619; only Dem 6 reached Georgian (via "
    "Armenian, misattributed to Hippolytus), nineteen homilies in "
    "Armenian misattributed to 'Jacob of Nisibis.' Confidence: "
    "Documented (witnesses, dates, methodology); Widely Accepted (the "
    "selection-effect interpretation) (Doc_08 2B-2 L1)."),
   ("To sing Ephrem's madrashe in the bnat qyama choir, hymn after "
    "hymn, service after service, is itself a way this world carried "
    "its own teaching forward - not a scribal act set apart from "
    "worship. Nothing comparable is available for Aphrahat's side: a "
    "stated absence, not filled with invented texture. [The "
    "choir-performance reapplication at DMR confidence] (Doc_08 2B-2 "
    "L2)."),
   ("Directly responsible for what can and cannot now be "
    "reconstructed: the dominance effect (Ephrem's voice risks "
    "standing in for the whole world) and the structural silences "
    "(ordinary lay believers, the bnat qyama's own unmediated voice, "
    "independent Jewish testimony, enslaved persons) - transmission "
    "favored the institutionally-embedded clerical-ascetic teacher "
    "(Doc_08 2B-2 L3)."),
   {"elaboration": (
     "The selection effects hardened over time into the evidence base "
     "itself: what survived became 'the world' as any later "
     "reconstruction can know it - the dominance effect is the "
     "transmission force's own product, and the record store built "
     "from it must carry the silences as named absences (Doc_02 SS7; "
     "the Affirmative-Duty ground syrgrav007 preserves) (S2.5 Layer-4 "
     "authoring from Doc_08 2B-2 L3 + SS6).")},
   [],
   ["srcSYR003", "srcSYR008", "srcSYR030"]),
 F("syrforce3A1",
   "Yazdegerd I's Accession and Formal Toleration of Christianity, 399 CE (Force 3A-1)",
   "3A - Ending/Transforming / External",
   ("Yazdegerd I's accession (399) marked the Persian church's first "
    "formal state toleration, after Qayyoma's stable patriarchate "
    "(377-399) and before Isaac's (399-410) culminating in the 410 "
    "Synod. Confidence: Widely Accepted (the policy shift); "
    "Contested/Inferential-Thin (exact succession dates - "
    "chronicle-derived, hagiographically inflected) (Doc_08 3A-1 L1)."),
   ("The record does not narrate the transition from persecution to "
    "toleration from the inside - no text captures what it meant to "
    "find the killing had stopped. [Reported-Experience Status: the "
    "inward reception is not attested and not supplied] (Doc_08 3A-1 "
    "L2)."),
   ("The precondition without which the institutional consolidation "
    "could not occur: the necessary hinge between persecution (2A-1) "
    "and the world's own ending; does not itself directly reshape any "
    "confirmed gravity (Doc_08 3A-1 L3)."),
   {"elaboration": (
     "A hinge force: its whole significance is what it made possible - "
     "the cessation created the condition the 410 Synod then filled; "
     "the world's ending runs through this gate rather than being "
     "worked by it (S2.5 Layer-4 authoring from Doc_08 3A-1 L3 + SS4 "
     "Connection 5).")},
   [{"type": "resolution-point-of", "target_id": "syrforce2A1",
     "note": "Doc_08 SS4 Connection 5: the Ending cell is the resolution-point of the Ongoing cell's own force."},
    {"type": "makes-possible", "target_id": "syrforce3A2",
     "note": ("Doc_08 3A-1 L3: the persecution regime's cessation is "
              "what makes the Synod possible at all.")}],
   ["srcSYR042"]),
 F("syrforce3A2",
   "The 410 Synod of Seleucia-Ctesiphon, Brokered by Marutha of Maiperqat Under Sasanian State Recognition (Force 3A-2)",
   "3A - Ending/Transforming / External",
   ("The Synod (410), convened under Isaac with Sasanian recognition, "
    "formally organized Persian Christianity into a structured church "
    "with metropolitan provinces - the institutional-structural change "
    "Doc_01 adopts as the world's own ending point. Marutha, Roman "
    "bishop of Maiperqat, Arcadius's envoy to Yazdegerd I, secured the "
    "permission; Bar Hebraeus credits him with advising the "
    "Roman-metropolitan template. Confidence: Widely Accepted to "
    "Documented (Synod, outcome, Marutha's role); DMR (the specific "
    "template-advice claim - single later chronicle source) (Doc_08 "
    "3A-2 L1)."),
   ("No surviving voice narrates receiving this change from within - "
    "what it meant to move from a church whose primatial seat had "
    "stood empty twenty years to one formally organized under a "
    "recognized head. [A stated absence, not an inhabited rendering] "
    "(Doc_08 3A-2 L2)."),
   ("The single force that most directly ends this world's own "
    "formation logic: it supplies, from outside and under state "
    "recognition, the settled episcopal structure the world's own "
    "internal ambiguity (C4) never produced across its 200-410 span "
    "(Doc_08 3A-2 L3)."),
   {"elaboration": (
     "An External Ending force producing an Internal one: the "
     "externally-brokered structure became the successor community's "
     "own internal constitution - the world's characteristic "
     "unresolvedness did not dissolve, it was superseded, and what "
     "follows is a different world (S2.5 Layer-4 authoring from "
     "Doc_08 SS4 Connection 6).")},
   [{"type": "made-possible-by", "target_id": "syrforce3A1",
     "note": "Doc_08 3A-1 L3 (mirror)."},
    {"type": "produces", "target_id": "syrforce3B1",
     "note": ("Doc_08 SS4 Connection 6: the External Ending force "
              "produces, or at minimum makes possible, the Internal "
              "one - sequential, not independent.")}],
   ["srcSYR042", "srcSYR051"]),
 F("syrforce3B1",
   "Institutional Consolidation Resolving the Authority-Structure Ambiguity (Force 3B-1)",
   "3B - Ending/Transforming / Internal",
   ("The Synod's metropolitan organization is external; its internal "
    "correlate: the world's own authority ambiguity does not appear to "
    "have been resolved from within its own resources at any point in "
    "the window - resolved, if at all, only by the externally-brokered "
    "structure. Confidence: DMR - the document's own synthetic "
    "connection, flagged as such and named the single most "
    "interpretively load-bearing judgment in Doc_08, most warranting "
    "outside scholarly scrutiny (Doc_08 3B-1 L1, SS5)."),
   ("No surviving text narrates the ambiguity as a problem awaiting "
    "the Synod's resolution - that connection is the document's own "
    "reading. [No Layer 2 content is attested at all; the absence is "
    "named rather than filled] (Doc_08 3B-1 L2)."),
   ("If this reading is sound, C4's decades-long unresolvedness is "
    "itself part of what makes the externally-brokered 410 resolution "
    "a genuine ending rather than a cosmetic label change - consistent "
    "with Doc_01's institutional-structural-change criterion for the "
    "boundary (Doc_08 3B-1 L3)."),
   {"elaboration": (
     "The world's most distinctive internal condition (C4) ends not by "
     "resolving but by being superseded - the Tensional gravity's arc "
     "(fractured by 2A-1, sustained by 2B-1, resolved by 3A-2/3B-1) is "
     "the second-strongest force-gravity cohesion in Doc_08 precisely "
     "because it is traceable across all three temporal phases (S2.5 "
     "Layer-4 authoring from Doc_08 SS5).")},
   [{"type": "produced-by", "target_id": "syrforce3A2",
     "note": "Doc_08 SS4 Connection 6 (mirror)."},
    {"type": "resolves", "target_id": "syrforce2B1",
     "note": "Doc_08 SS5 C4 arc (mirror of syrforce2B1's resolved-by)."}],
   ["srcSYR042"]),
 F("syrforce3B2",
   "Transmission in Ending - The Diatessaron-to-Peshitta Transition and the Later Legendary Accretion Around Ephrem (Force 3B-2)",
   "3B - Ending/Transforming / Internal (Transmission dimension)",
   ("The Diatessaron's two-century normative use ended with the "
    "Peshitta displacement in the early 5th c. - traditionally "
    "credited to Rabbula (411-435), though Voobus argues the "
    "Peshitta's composition predates his episcopate (promoter, not "
    "originator; Contested). The Syriac Diatessaron itself survives "
    "only in fragments and citations - genuine transmission loss. "
    "Separately: the Ephrem legend material (choir leadership; the "
    "Vita) is 6th-century, outside the boundary, excluded from C2 at "
    "Doc_04. Confidence: Widely Accepted (timeline); Contested "
    "(Rabbula's role); Documented (the 6th-c. legend dating) (Doc_08 "
    "3B-2 L1)."),
   ("Within its own window this world experienced the Diatessaron as "
    "an unbroken single story, not a text on the verge of replacement "
    "- the anxiety of impending supersession is NOT part of the "
    "inhabited experience. [A negative finding, stated to avoid "
    "inventing anticipatory anxiety; Documented absence] (Doc_08 3B-2 "
    "L2)."),
   ("Explains two recoveries and losses: why C5's textual anchor is "
    "not directly recoverable (its transmission mechanism was itself "
    "superseded at the close), and why legendary material about "
    "Ephrem emerges in exactly the following century - a successor "
    "community actively reshaping this world's memory for its own "
    "formational needs (the choir-leading, more fully monasticized "
    "Ephrem) (Doc_08 3B-2 L3)."),
   {"elaboration": (
     "Transmission acted twice at the close: it dissolved the world's "
     "own scriptural anchor (the Diatessaron surviving only through "
     "indirect witnesses) and simultaneously began MANUFACTURING a "
     "new past (the legendary Ephrem) - the world's after-life "
     "reshaped by the same force that failed to carry its text "
     "forward; syrstory007/008 tell exactly this accretion with the "
     "correction attached (S2.5 Layer-4 authoring from Doc_08 3B-2 "
     "L3 + SS6).")},
   [{"type": "bookends-with", "target_id": "syrforce1B3",
     "note": "Doc_08 SS4 Connection 7 (mirror)."}],
   ["srcSYR011", "srcSYR028", "srcSYR045", "srcSYR059"]),
]

# FEC -> gravity_links (CO-P2-04): story -> list of gravity ids; first
# link's note carries the FULL FEC verbatim (extracted from the body
# parking), later links a short pointer note.
FEC_LINKS = {
    "syrstory001": ["syrgrav002"],
    "syrstory003": ["syrgrav004"],
    "syrstory004": ["syrgrav004"],
    "syrstory005": ["syrgrav006"],
    "syrstory007": ["syrgrav001", "syrgrav002", "syrgrav003"],
    "syrstory009": ["syrgrav001", "syrgrav002", "syrgrav005"],
    # syrstory002 / 006 / 008: FEC names NO gravity (archive-memory
    # character / force 1A-2 / excluded-legend documentation) - links
    # deliberately absent, FEC stays body-parked, S2.8 view falls back.
}

FEC_RE = re.compile(
    r"\[Formation Ecology Connection - parked at the S2\.4-equivalent.*?\]\s*(.*?)(?=\n\n\[|\Z)",
    re.S)


def main():
    for rec, body in GRAVITIES:
        emit_record(rec, body, OUT / "gravity" / f"{rec['id']}.md")
    for gid, name, reason in NOT_ADVANCED:
        rec = {"world_id": WID, "record_type": "gravity",
               "schema_version": 1, "jobs": [5], "register": "etic",
               "review_state": "draft", "id": gid, "name": name,
               "classification": "not-advanced"}
        emit_record(rec, ("S6.2/SYR S2.5-equivalent not-advanced record "
                          "(2026-07-28; the rule's second non-empty "
                          "extension after ALX). " + reason),
                    OUT / "gravity" / f"{gid}.md")
    for rec in FORCES:
        emit_record(rec, ("S6.2/SYR S2.5-equivalent force record "
                          "(2026-07-28) from Doc_08 (three layers "
                          "condensed-verbatim with citations; Layer 4 is "
                          "THIS step's authoring - elaboration or "
                          "considered stasis). connections[] = Doc_08 SS4 "
                          "cross-cell links, mirrored; force->gravity "
                          "tracing lives verbatim in "
                          "layer_formation_impact (Desert S2.5 "
                          "rationale)."),
                    OUT / "force" / f"{rec['id']}.md")
    # FEC -> gravity_links
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
    # world_core gravities
    core_path = OUT / "world_core" / "syrcore001.md"
    front, body = read_record(core_path)
    front["gravities"] = [g[0]["id"] for g in GRAVITIES]
    write_record(core_path, front, body)
    print(f"wrote {len(GRAVITIES)} confirmed + {len(NOT_ADVANCED)} "
          f"not-advanced gravities, {len(FORCES)} forces, "
          f"{len(FEC_LINKS)} stories linked, core updated")


if __name__ == "__main__":
    main()
