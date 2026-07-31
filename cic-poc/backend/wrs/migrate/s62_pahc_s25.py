"""S6.2/PAHC - S2.5-equivalent: gravities + forces + FEC conversion.

- 7 gravity records, id-aligned to the world's own G-numbering
  (pahcgrav001=G01 ... pahcgrav007=G07; pahcgrav006=G06 not-advanced):
  6 classified (G02/G07 Primary; G01/G03/G04 Supporting; G05
  Tensional) + G06 'did not reach gravity status' - the fleet's
  strongest not-advanced writeup (the household-code texts have no
  Registry row; one fact verified twice by different methods).
- STRAND SCOPING CARRIED (the strand-plural world's own gravity
  feature): G04/G05 are Strand-A-bound; G01's FORCE is cross-strand
  while its RESOLUTION is strand-bound; the Ignatius-vulnerability
  linkage (G01-Strand-A content, G04, G05 all rest on Ignatius as
  Asia Minor's only voice) recorded on all three.
- The Interaction Matrix's FINAL seven-round state mirrored exactly:
  ONE plain Reinforcing (G01-G02, the only genuinely multi-voice
  pair), NINE '(inferential)' cells, FIVE no-demonstrated-relationship
  cells (each absent BY THE MATRIX'S OWN FINDING, with Doc_04's cited
  negations where given - G04-G07's explicit dies-natalis negation;
  G03-G07's 'No demonstrated connection to G03'). The reshaping cell
  (G02-G03) typed with its direction note.
- 14 force records (pahcforce1A1..3B2) from the W1 Doc_08. TWO
  structural declarations: (a) FOUR FORCES ARE GRAVITIES BY THE DOC'S
  OWN STATEMENT (2A-1=G03 'this candidate IS one of the primary
  forces'; 2B-1=G01; 2B-3=G04; 2B-4=G05) - the W1-era doc predates
  the force/gravity separation discipline; both record types kept
  with identity cross-notes both ways, nothing invented to separate
  them. (b) the External-definition CORRECTION carried on 3A-1/3A-2
  (External = outside the six-primary-voice evidentiary network, NOT
  geographic - the doc's own withdrawn-and-recorrected rule).
- Connections: Doc_08 SS4's six named cross-cell connections mirrored
  with typed pairs; Connection 5 carries its own-synthesis disclosure
  verbatim in the note (Doc_07 SS2D's interpretive extension, never
  an inherited finding).
- FEC -> gravity_links (CO-P2-04) on 11 of 13 stories. TWO declared
  unlinked BY THEIR OWN FECs: pahcstory009 ('not itself evidence for
  a confirmed Doc_04 gravity') and pahcstory013 ('not classified as
  direct evidence for either named gravity specifically') - FECs
  stay body-parked, the S2.8 chunk view falls back (the HAL 08/09/10
  precedent, here with the chunks' own explicit not-direct-evidence
  statements).
- pahccore001.gravities closed at the 6 classified.
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
sys.path.insert(0, str(HERE))

from source_rows_from_doc02 import emit_record
from s62_pahc_s23 import read_record, write_record

OUT = BACKEND / "wrs" / "records" / "pahc_world"
WID = "post-apostolic-house-church"
D4 = "CiC_W1_Doc04_Gravity_Discovery_FINAL.md (read in full this step)"
D8 = "CiC_W1_Doc08_Forces_Document.md (read in full this step)"

IGN_VULN = ("THE IGNATIUS VULNERABILITY (Doc_04 SS3, round-1 explicit "
            "linkage): this gravity rests on Ignatius as Asia Minor's "
            "ONLY evidentiary voice - the open third-Asia-Minor-profile "
            "item is exactly the new evidence that could move it; "
            "carried unresolved, never manufactured.")


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
 G("pahcgrav001",
   "Authority Consolidation - the episkopos/presbyteros/diakonos "
   "question (G01)", "Supporting",
   {"repetition": ("PASS, strongly - recurs across every primary voice "
                   "in the Registry and Doc_02's dedicated Institutional "
                   "Evidence section (Doc_04 G01)."),
    "dependency": ("PASS, strongly - liturgical presidency (G07), "
                   "disciplinary authority (1 Clement's whole Corinthian "
                   "intervention), and boundary rhetoric (G05) all depend "
                   "on how this resolves (Doc_04 G01)."),
    "formation": ("PASS - shapes who is obeyed, who administers rites, "
                  "how disputes are resolved (Doc_04 G01)."),
    "explanatory": ("PASS, strongly - explains why the corpus itself is "
                    "largely letters about authority disputes (Doc_04 "
                    "G01)."),
    "persistence": ("PASS with the carried caveat: visible in both "
                    "regions across the whole window, but its SPECIFIC "
                    "SHAPE changes across that span - part of what makes "
                    "it live, not settled (Doc_04 G01)."),
    "interaction": "PASS - see the matrix (relationships with every classified candidate)."},
   ("SUPPORTING BY THE CROSS-CHECK'S OWN RULE (reclassified from "
    "Primary at round 1 - the fleet's clearest disclosure-is-not-"
    "reclassification correction): the coarse claim (authority required "
    "active organizing) is Widely Accepted, but no separable "
    "non-trivial claim survives once the Contested Strand-A content is "
    "set aside - 'the specific content that actually does this "
    "gravity's interaction and dependency work... is exactly the "
    "Contested part.' Cross-strand status split and carried: the FORCE "
    "is cross-strand confirmed; the RESOLUTION is strand-bound (Strand "
    "A single office / Strand B plural interchangeable college - both "
    "recorded, neither collapsed). " + IGN_VULN),
   [{"type": "reinforcing", "target_id": "pahcgrav002",
     "note": ("THE MATRIX'S ONE PLAIN REINFORCING CELL - genuinely "
              "multi-voice on both sides (1 Clement's Strand-B "
              "intervention traveling the network; Ignatius's Strand-A "
              "letters doing the same), distinguished at round 5 from "
              "the shared-single-passage pattern and citation-tightened "
              "at round 7 (a synthesis of G01's Dependency bullet + "
              "G02's generation basis, not one verbatim sentence).")},
    {"type": "reinforcing", "target_id": "pahcgrav003",
     "note": "Doc_04 matrix: Reinforcing (inferential) - the shared Ignatius imprisonment-rhetoric anchor."},
    {"type": "reinforcing", "target_id": "pahcgrav004",
     "note": "Doc_04 matrix: Reinforcing (inferential) - Ignatius deploys his impending martyrdom as an argument FOR his authority program."},
    {"type": "reinforcing", "target_id": "pahcgrav005",
     "note": "Doc_04 matrix: Reinforcing (inferential) - the obey-the-bishop program tied directly to anti-docetic argument (G05's own Dependency line)."},
    {"type": "reinforcing", "target_id": "pahcgrav007",
     "note": "Doc_04 matrix: Reinforcing (inferential) - the bishop-presided eucharist (single-source Ignatius anchor)."}],
   ["srcPAHCP02", "srcPAHCP03", "srcPAHCP04", "srcPAHCP05", "srcPAHCP01",
    "srcPAHCP06"],
   ("S6.2/PAHC S2.5-equivalent gravity record (2026-07-31) from " + D4 +
    ". Force identity declared: this gravity IS Force 2B-1 "
    "(pahcforce2B1) - the W1 doc's own framing; see that record. "
    "Forces: generated directly by the eyewitness-generation loss "
    "(1A-2, Connection 1); intensifies under state pressure.")),
 G("pahcgrav002",
   "Translocal Correspondence Network (G02)", "Primary",
   {"repetition": "PASS, strongly, across both regions - three independent voices/events (Doc_04 G02).",
    "dependency": ("PASS, strongly - G01's translocal claims are "
                   "EXERCISED THROUGH this network; doctrinal/memory "
                   "consolidation depends on letters circulating; "
                   "Doc_02's own primary-voice set is largely "
                   "explainable by what entered and survived the "
                   "network (Doc_04 G02)."),
    "formation": "PASS - produces the felt belonging to something larger than the local assembly (Doc_04 G02).",
    "explanatory": "PASS, strongly - arguably explains the shape of Doc_02 itself (Doc_04 G02).",
    "persistence": "PASS across all three named regions (Doc_04 G02).",
    "interaction": "PASS - see the matrix."},
   ("The strongest confidence footing of any candidate: Widely "
    "Accepted/Documented that these letters exist and were exchanged "
    "this way; NO significant single-voice dependency - the one "
    "candidate independently attested by voices from BOTH strands "
    "behaving the same way. Cross-Check clean. Cross-strand "
    "confirmed."),
   [{"type": "reinforcing", "target_id": "pahcgrav001",
     "note": "Mirror of pahcgrav001's plain-Reinforcing edge (the matrix's one multi-voice cell)."},
    {"type": "reshaping", "target_id": "pahcgrav003",
     "note": ("Doc_04 matrix: Reshaping (inferential) - DIRECTION: G03 "
              "reshapes G02 (this record is the reshaped side): "
              "'Ignatius relies on the network precisely because he is "
              "under guard' - a single-episode anchor, labeled "
              "inferential at round 4.")},
    {"type": "reinforcing", "target_id": "pahcgrav004",
     "note": "Doc_04 matrix: Reinforcing (inferential) - martyr-narrative transmission travels this channel."}],
   ["srcPAHCP02", "srcPAHCP03", "srcPAHCP04"],
   ("S6.2/PAHC S2.5-equivalent gravity record (2026-07-31) from " + D4 +
    ". Forces: 1A-1 supplies the material/linguistic precondition; "
    "2B-2 is the same mechanism as selection filter ('not a neutral "
    "pipe'); 1A-2's eyewitness loss is what makes correspondence-based "
    "unity NECESSARY at all (Doc_08 SS5).")),
 G("pahcgrav003",
   "State Pressure / Legal Precarity (G03)", "Supporting",
   {"repetition": "PASS - four separate outside/hostile witnesses plus Ignatius's own corpus (Doc_04 G03).",
    "dependency": ("PASS, strongly - G04 is essentially the internal "
                   "response to this force; G01's urgency partly "
                   "depends on it; institutional silence is best "
                   "explained by it (Doc_04 G03)."),
    "formation": "PASS - shapes risk calculus, willingness to gather, to recant or not (Doc_04 G03).",
    "explanatory": "PASS, strongly (Doc_04 G03).",
    "persistence": ("PASS with the honest caveat carried whole: the "
                    "evidenced episodes are geographically and "
                    "temporally SCATTERED, not one continuous policy - "
                    "'local, unpredictable legal exposure'; the "
                    "underlying vulnerability persistent, the incidents "
                    "intermittent (Doc_04 G03; the Doc_08 instruction "
                    "to preserve this against any constant-persecution "
                    "framing)."),
    "interaction": "PASS - see the matrix."},
   ("SUPPORTING by the round-2 reclassification (the same test that "
    "moved G01): the six-test work is done by the generalized "
    "cross-episode synthesis - exactly the Contested layer; the "
    "Documented core alone (one governor, one province, one episode) "
    "carries none of it. Cross-strand corrected at round 3: confirmed "
    "via Strand B (Rome/Tacitus) + Strand A (Ignatius's arrest); "
    "Bithynia-Pontus corroborates but IS NOT A STRAND (Pliny's "
    "material is a third data point, not a third strand)."),
   [{"type": "reinforcing", "target_id": "pahcgrav001",
     "note": "Mirror (inferential - the imprisonment-rhetoric anchor)."},
    {"type": "reshaping", "target_id": "pahcgrav002",
     "note": "Mirror of pahcgrav002's edge - this record is the reshaping side (the under-guard reliance)."},
    {"type": "reinforcing", "target_id": "pahcgrav004",
     "note": ("Doc_04 matrix: Reinforcing (inferential) - dual-sourced "
              "in both candidates' own Dependency/Forces language "
              "('G04 is essentially the internal response to this "
              "force' / 'this gravity IS the meaning-making response "
              "to G03') - the round-5 grounding re-check sustained "
              "this against the reviewer's overstatement claim, logged "
              "not silently resolved.")}],
   ["srcPAHCP07", "srcPAHCP08", "srcPAHCP09", "srcPAHCP10", "srcPAHCP03"],
   ("S6.2/PAHC S2.5-equivalent gravity record (2026-07-31) from " + D4 +
    ". Force identity declared: this gravity IS Force 2A-1 "
    "(pahcforce2A1) - 'this candidate IS one of the primary forces "
    "named in Doc_01 SS7', the doc's own words; see that record.")),
 G("pahcgrav004",
   "Martyrdom as Formation-Shaping Meaning-Response (G04; Strand A "
   "only)", "Supporting",
   {"repetition": ("WEAK relative to G01-G03 - exactly two data points "
                   "(Ignatius's own voice; the Martyrdom of Polycarp), "
                   "both Strand A (Doc_04 G04)."),
    "dependency": ("Real but narrower than it appears: runs mostly INTO "
                   "G01/G05 (his martyrdom reinforcing his claims); the "
                   "dies-natalis commemoration 'belongs more to what "
                   "this world hands off to World #2/#7' than to G07 "
                   "(Doc_04 G04)."),
    "formation": ("'CLEARLY formation-shaping for the specific "
                  "individuals in the record' - the verdict that earns "
                  "Supporting at the narrow grain; far less certain for "
                  "the ordinary member (Doc_04 G04)."),
    "explanatory": ("Explains Ignatius's own rhetoric well; does not "
                    "explain Strand B at all - no comparable "
                    "martyr-piety in 1 Clement or Hermas (Doc_04 "
                    "G04)."),
    "persistence": "FAILS the broad bar - two individuals' experience, not regions/communities/streams (Doc_04 G04).",
    "interaction": "PASS - see the matrix."},
   ("'The clearest case in this document of the Cross-Check doing its "
    "job': vivid, quotable, easy to over-read - and Supporting, not "
    "Primary, because the narrow claim ('shaped these two specific "
    "people's own self-presentation') reaches 'Clearly' - "
    "Documented-level on its own terms - while representativeness is "
    "Contested/Inferential-Thin. This is the REUSABLE "
    "Supporting-vs-Tensional criterion's anchor case (vs G05). "
    "Strand-bound: Strand A only - an absence of evidence, not a "
    "confirmed absence (the Doc_04 SS6 re-test instruction if Strand-B "
    "evidence ever develops). " + IGN_VULN),
   [{"type": "reinforcing", "target_id": "pahcgrav001",
     "note": "Mirror (inferential)."},
    {"type": "reinforcing", "target_id": "pahcgrav002",
     "note": "Mirror (inferential - transmission of the martyr narrative)."},
    {"type": "reinforcing", "target_id": "pahcgrav003",
     "note": "Mirror (inferential, dual-sourced - the meaning-making response)."},
    {"type": "reinforcing", "target_id": "pahcgrav005",
     "note": "Doc_04 matrix: Reinforcing (inferential) - martyrdom deployed in the anti-docetic argument."}],
   ["srcPAHCP03", "srcPAHCP16"],
   ("S6.2/PAHC S2.5-equivalent gravity record (2026-07-31) from " + D4 +
    ". Force identity declared: this gravity IS Force 2B-3 "
    "(pahcforce2B3). G04-G07 'No demonstrated relationship' rests on "
    "an EXPLICIT NEGATION (the dies-natalis hands-off sentence), cited "
    "at round 7 - not an omission.")),
 G("pahcgrav005",
   "Boundary-Drawing Against Contemporary Rival Movements - "
   "anti-docetic polemic (G05; Strand A only)", "Tensional",
   {"repetition": "WEAK - essentially one voice (Ignatius) within the Native Registry (Doc_04 G05).",
    "dependency": ("Some - the obey-the-bishop program tied directly to "
                   "anti-docetic argument, but the dependency runs "
                   "mostly one direction (Doc_04 G05)."),
    "formation": ("'Plausible for Ignatius's own direct addressees; "
                  "unestablished more broadly' - NEVER reaching the "
                  "'Clearly' G04 reaches at the same narrowest scope: "
                  "the exact textual ground of the Tensional "
                  "classification (Doc_04 G05, round-4 "
                  "strengthening)."),
    "explanatory": "Explains Ignatius's own rhetoric; not Strand B (Doc_04 G05).",
    "persistence": "FAILS broadly - not attested outside Ignatius within the Native set (Doc_04 G05).",
    "interaction": "PASS - see the matrix."},
   ("TENSIONAL by the reusable criterion (grounded at round 4): no "
    "level of grain, coarse or fine, clears the bar G04 clears at its "
    "narrow end - 'Plausible', never 'Clearly'. The underlying "
    "phenomenon (a real, live, unsettled boundary against Marcionite/"
    "Valentinian/proto-docetic neighbors) is exactly what Tensional is "
    "for: the pressure that keeps this world from reading as "
    "already-settled orthodoxy. Strand-bound (Strand A only). "
    + IGN_VULN),
   [{"type": "reinforcing", "target_id": "pahcgrav001",
     "note": "Mirror (inferential)."},
    {"type": "reinforcing", "target_id": "pahcgrav004",
     "note": "Mirror (inferential)."},
    {"type": "reinforcing", "target_id": "pahcgrav007",
     "note": ("Doc_04 matrix, the round-6 catch: G07's own Dependency "
              "bullet names this same eucharist-boundary passage as "
              "'simultaneously a G01 and G05 move' - the second half "
              "of a sentence five rounds had read only for its G01 "
              "half.")}],
   ["srcPAHCP03"],
   ("S6.2/PAHC S2.5-equivalent gravity record (2026-07-31) from " + D4 +
    ". Force identity declared: this gravity IS Force 2B-4 "
    "(pahcforce2B4). The G03-G05 cell is 'No demonstrated "
    "relationship' (the round-5 catch - carried unexamined through "
    "four prior rounds); Doc_07 SS2D's proposed G03/G05 convergence "
    "is DISCLOSED OWN-SYNTHESIS (Connection 5), never an inherited "
    "finding.")),
 G("pahcgrav006",
   "Household (oikos) as Basic Social/Meeting Unit (G06 - did not "
   "reach gravity status)", "not-advanced",
   None, None, None,
   [],
   ("S6.2/PAHC S2.5-equivalent not-advanced record (2026-07-31; the "
    "rule's fourth extension, and the fleet's strongest not-advanced "
    "writeup) from " + D4 + ": G06 rests almost entirely on secondary "
    "scholarship (Meeks, Gehring, Balch, MacDonald) discussing "
    "household-code texts (Colossians, Ephesians, 1 Peter) that have "
    "NO Registry row in this world at all - Repetition fails within "
    "the Native primary-voice set. 'Not a claim that households were "
    "unimportant... a claim that this document's own evidentiary "
    "base cannot independently establish it as a gravity rather than "
    "an imported modern historiographical frame.' The finding "
    "CONFIRMS, via an independently-run test, the same underlying "
    "gap Doc_03's house-church item found by a different method - "
    "one fact verified twice, not two convergent lines (the round-1 "
    "wording correction carried). Doc_04 SS6 item 2: treat both as "
    "ONE question.")),
 G("pahcgrav007",
   "Liturgical Practice (Eucharist) as Site of Variation and "
   "Convergence (G07)", "Primary",
   {"repetition": ("PASS, strongly - three independent voices, "
                   "cross-regional (the Didache, Ignatius, Justin) "
                   "(Doc_04 G07)."),
    "dependency": ("PASS - communal boundary-marking depends on it "
                   "(the one-eucharist instruction 'simultaneously a "
                   "G01 and G05 move', Philadelphians 4 per Doc_03's "
                   "corrected citation); basic gathering structure "
                   "depends on it (Doc_04 G07)."),
    "formation": "PASS, strongly - the central recurring communal ritual (Doc_04 G07).",
    "explanatory": ("PASS, strongly - explains the real variation in "
                    "the evidence itself (cup-before-bread vs "
                    "institution-narrative forms) and why Doc_02 "
                    "needed the diversity-first calibration (Doc_04 "
                    "G07)."),
    "persistence": "PASS across all three regions (Doc_04 G07).",
    "interaction": ("PASS - two of five demonstrated (G01, G05, both "
                    "inferential): thinner than earlier drafts "
                    "claimed, corrected at rounds 4-6 and tracked "
                    "honestly; classification rests on six-test/"
                    "Cross-Check results, not matrix connectivity "
                    "(Doc_04 SS6 item 9).")},
   ("PRIMARY by the set-aside-the-Contested-layer test: the "
    "Documented content (a shared ritual independently attested in "
    "related but non-identical forms by three separated voices) is "
    "what earns Dependency/Explanatory/Formation - unlike G01/G03, "
    "the Contested which-form-is-representative layer is not what "
    "the work depends on. One acknowledged soft spot (round 4): the "
    "G01-link imports one small, stated interpretive step. "
    "Cross-strand confirmed (Strand A Ignatius, Strand B Justin, "
    "plus the Didache's separate single-community witness)."),
   [{"type": "reinforcing", "target_id": "pahcgrav001",
     "note": "Mirror (inferential - the bishop-presided eucharist anchor)."},
    {"type": "reinforcing", "target_id": "pahcgrav005",
     "note": "Mirror of pahcgrav005's round-6-caught edge (the same clause's G05 half)."}],
   ["srcPAHCP01", "srcPAHCP03", "srcPAHCP06"],
   ("S6.2/PAHC S2.5-equivalent gravity record (2026-07-31) from " + D4 +
    ". 'No demonstrated connection to G03' is G07's OWN explicit "
    "statement (confirming, not defaulting, that matrix cell). "
    "Forces: fused with 2B-1/2B-4 in Strand A (worship and belonging "
    "one act).")),
]


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


EXT_NOTE = ("[External per the doc's own CORRECTED rule (Step-9 note, "
            "re-argued after cold review withdrew the geographic "
            "reading): External = generated outside the six-primary-"
            "voice evidentiary network, regardless of location.] ")

FORCES = [
 F("pahcforce1A1", "The Roman Imperial Mediterranean World (1A-1)",
   "1A - Initiating / External",
   ("One road-and-sea infrastructure, one Greek koine, one collegia "
    "social repertoire connecting Antioch/Syria, Asia Minor, and Rome "
    "into a navigable network by the late 1st c.; Ignatius's guarded "
    "journey the clearest single proof it could carry sustained "
    "contact. Confidence: Well-established/Documented (Doc_08 1A-1 "
    "L1)."),
   ("A letter written in Antioch could be read in Smyrna or Rome "
    "without translation; the world beyond one ekklesia's room was "
    "one connected reach - a sister letter felt like proof of "
    "belonging, not news from elsewhere (Doc_08 1A-1 L2)."),
   ("The material precondition for G02; the same roads carried "
    "Ignatius under guard - the infrastructure enabling ordinary "
    "correspondence also carried the most intensive formation case "
    "(Doc_08 1A-1 L3)."),
   {"elaboration": (
     "The enabling condition never becomes a story of its own - the "
     "doc's SS4 close reads 1A-1 as bracketing condition for the "
     "whole axis, not a separate tale; its work is that every other "
     "force presupposes a world where letters arrive (S2.5 Layer-4 "
     "authoring from Doc_08 SS4's pattern paragraph).")},
   [{"type": "enables", "target_id": "pahcforce2B2",
     "note": ("Doc_08 SS4 Connection 4: the same infrastructure and "
              "koine are the physical/linguistic condition for every "
              "later transmission event.")}],
   ["srcPAHCP03"]),
 F("pahcforce1A2",
   "The Neronian Persecution and the Deaths of Peter and Paul, c. "
   "64-68 (1A-2)",
   "1A - Initiating / External",
   ("Tacitus's fire-scapegoating account; Brown's standard "
    "periodization keying the sub-apostolic age to the apostles' "
    "deaths under Nero; 1 Clement writing of those deaths as already "
    "past. Confidence: Widely Accepted (the passage) / Contested (a "
    "discrete named-group persecution - Shaw/Jones) / DMR (the "
    "Petrine/Pauline martyrdom periodization) (Doc_08 1A-2 L1)."),
   ("The people who had walked with the founder were dying, and no "
    "one could simply point to someone who had been there anymore; "
    "what replaced direct witness was ARGUMENT - continuity claimed, "
    "urgently, because the last living link running out was close "
    "enough to be felt (Doc_08 1A-2 L2)."),
   ("The single most direct trigger of the world's defining formation "
    "logic - the urgency behind G01, and the generative condition of "
    "the whole argued-not-inherited character (Doc_08 1A-2 L3)."),
   {"elaboration": (
     "The world's entire arc is this force working itself out: the "
     "SS4 close names one axis running from this loss through the "
     "argued decades to the settlement that closes the world - the "
     "initiating crisis IS the world's character, not its backdrop "
     "(S2.5 Layer-4 authoring from Doc_08 SS4).")},
   [{"type": "generates", "target_id": "pahcforce2B1",
     "note": ("Doc_08 SS4 Connection 1: the eyewitness-generation "
              "loss is the direct generative condition of G01's "
              "ongoing contest.")}],
   ["srcPAHCP08", "srcPAHCP02"]),
 F("pahcforce1B1", "The Apostolic Testimony Inheritance (1B-1)",
   "1B - Initiating / Internal",
   ("The inherited conviction that legitimate teaching must trace to "
    "apostolic testimony - scripture read alongside living testimony, "
    "not against a closed canon; received from the apostolic "
    "generation directly. Confidence: Widely Accepted (presence); the "
    "transmission mechanism less securely documented (Doc_08 1B-1 "
    "L1)."),
   ("What had been handed down by the apostles was the measure "
    "against which everything else was tested - the inherited ground "
    "a community stood on, even while arguing over exactly what "
    "standing on it required (Doc_08 1B-1 L2)."),
   ("What makes the eyewitness loss a CRISIS at all rather than a "
    "neutral fact - and the ground of the world's own temporal "
    "assumption: an urgency of transmission before the last direct "
    "witnesses are gone (Doc_08 1B-1 L3)."),
   {"elaboration": (
     "The inheritance and the loss are one mechanism seen from two "
     "cells: 1B-1 supplies the measure, 1A-2 removes its living "
     "anchor, and G01 is what a community does when the measure "
     "must now be argued (S2.5 Layer-4 authoring from Doc_08 1B-1 "
     "L3 + SS5 G01 row).")},
   [{"type": "sets-terms-of", "target_id": "pahcforce2B1",
     "note": ("Doc_08 SS5 G01 row: the inherited commitment makes "
              "apostolic continuity THE terms of the authority "
              "contest, rather than wealth or learning.")}],
   ["srcPAHCP02", "srcPAHCP03"]),
 F("pahcforce1B2", "The Two Ways Catechetical Inheritance (1B-2)",
   "1B - Initiating / Internal",
   ("The Didache's opening instructional schema, independently "
    "paralleled in the Doctrina Apostolorum and Barnabas 18-20 - "
    "evidence the schema circulated more widely than the Didache's "
    "own redaction, though the Didache itself is plausibly one "
    "(likely Syrian) community's document. Confidence: Documented "
    "(the schema's existence/use) / Inferential-Thin (network-wide "
    "adoption) (Doc_08 1B-2 L1)."),
   ("Before the water, two ways lay open - and which one a person "
    "walked was a live, continuing choice, not a nature settled once; "
    "a tool for shaping a new member, adaptable to occasion, issued "
    "from no center (Doc_08 1B-2 L2)."),
   ("Grounds the world's own understanding of the person - someone at "
    "a live moral fork - and supplies the entry-point logic of the "
    "whole formation arc; never generalizable network-wide (maximal "
    "Author-Gravity risk, the single-manuscript base) (Doc_08 1B-2 "
    "L3)."),
   {"elaboration": (
     "The record store carries the same cap at every layer: the "
     "term (pahclex007), the story (pahcstory009), and this force "
     "all hold the single-community boundary the chunk itself draws "
     "- the Barnabas parallel stays outside the defined source set "
     "at all three (S2.5 Layer-4 authoring; the S2.1b watch item's "
     "force-side).")},
   [],
   ["srcPAHCP01"]),
 F("pahcforce2A1", "State Legal Precarity (2A-1 = G03)",
   "2A - Ongoing / External",
   ("Pliny 10.96-97 the earliest Roman administrative document on "
    "Christians, showing no prior standing law; Trajan forbidding "
    "seek-out; Tacitus and Suetonius corroborating scattered earlier "
    "episodes; Decius's empire-wide persecution safely after the "
    "close. Confidence: Documented (the letter) / Contested (one "
    "standing condition vs intermittent exposure) (Doc_08 2A-1 L1)."),
   ("A name could be given, an accusation made, a choice demanded - "
    "without warning, without knowing in advance whether it would "
    "happen to you. Not constant terror; near enough that a member "
    "organized some real part of their emotional life around it "
    "(Doc_08 2A-1 L2)."),
   ("Sustains G04 as its direct internal answer; plausibly explains "
    "the near-total institutional self-documentation silence; and - "
    "Doc_07 SS3's finding - its very UNEVENNESS, never severe enough "
    "to force one strand's answer onto the other, is a condition of "
    "the two-strand plurality persisting (Doc_08 2A-1 L3)."),
   {"elaboration": (
     "FORCE IDENTITY DECLARED: this force IS gravity G03 "
     "(pahcgrav003) by the doc's own statement - the W1-era "
     "force/gravity overlap kept as identity with cross-notes, not "
     "separated by invention (S2.5 structural declaration).")},
   [{"type": "generates", "target_id": "pahcforce2B3",
     "note": ("Doc_08 SS4 Connection 2 - 'the most directly and "
              "explicitly evidenced cross-cell connection in this "
              "entire matrix': G04 IS the meaning-making response to "
              "G03.")},
    {"type": "converges-with", "target_id": "pahcforce2B4",
     "note": ("Doc_08 SS4 Connection 5 - DISCLOSED OWN-SYNTHESIS "
              "(Doc_07 SS2D's interpretive extension, carried with "
              "its disclosure verbatim): doctrinal and legal boundary-"
              "holding rehearsed as one continuous kind of refusal "
              "for a Strand A member - NOT an inherited Doc_04 "
              "finding (that matrix cell reads No demonstrated "
              "relationship).")}],
   ["srcPAHCP07", "srcPAHCP08", "srcPAHCP09"]),
 F("pahcforce2A2",
   "Contemporary Rival Movements - Marcion, Valentinian/Gnostic "
   "Christianity, Montanism (2A-2)",
   "2A - Ongoing / External",
   (EXT_NOTE +
    "Marcion's break/arrival c. 144; Valentinus in Rome c. 136 into "
    "the 150s-160s with documented branch split; Montanism's "
    "archaeologically corroborated Phrygian origin (start disputed "
    "157-172), mature concern by 177. All geographically overlapping "
    "this world's three core regions in the same decades. Confidence: "
    "Documented (existence/overlap) / Contested (precise dates) "
    "(Doc_08 2A-2 L1)."),
   ("Not distant errors safely elsewhere - near, contemporary, "
    "undefeated neighbors teaching in the same cities, sometimes "
    "drawing from the same communities; a boundary that had to be "
    "actively argued and held, letter after letter (Doc_08 2A-2 "
    "L2)."),
   ("The external condition G05 answers - Ignatius's anti-docetic "
    "argument exists because these rivals pressed close (Doc_08 2A-2 "
    "L3)."),
   {"elaboration": (
     "The corrected External rule was forged ON this force: its "
     "rivals operated inside two of the three core regions, so "
     "External cannot be geographic - it names communities outside "
     "the six-voice evidentiary network; 3A-1/3A-2 follow the same "
     "rule one cell later (S2.5 Layer-4 authoring from the Step-9 "
     "definitional note).")},
   [{"type": "generates", "target_id": "pahcforce2B4",
     "note": "Doc_08 SS4 Connection 3: the boundary response exists because the rivals existed."}],
   ["srcPAHCP03"]),
 F("pahcforce2B1", "Authority Consolidation (2B-1 = G01)",
   "2B - Ongoing / Internal",
   ("1 Clement's interchangeable episkopos/presbyteros for a plural "
    "college and Hermas's plural presiding presbyters beside "
    "Ignatius's explicit threefold program - two mutually exclusive, "
    "contemporaneous, regionally-differentiated answers to one "
    "organizational question. Confidence: Widely Accepted (the live "
    "question) / Contested (Strand A's monarchical content) (Doc_08 "
    "2B-1 L1)."),
   ("In one community obedience to a single bishop was the very "
    "shape of unity - strings tuned into one sound; in another a "
    "council of presbyters was ordinary, sufficient oversight; and "
    "the same man (Polycarp) could be addressed as bishop while "
    "naming himself one of the presbyters (Doc_08 2B-1 L2)."),
   ("The clearest institutional expression of the defining formation "
    "logic - office argued for, not assumed; fused with G07 in "
    "Strand A (the bishop's eucharist as worship and belonging in "
    "one) (Doc_08 2B-1 L3)."),
   {"elaboration": (
     "FORCE IDENTITY DECLARED: this force IS gravity G01 "
     "(pahcgrav001); the record store keeps both views with "
     "cross-notes (S2.5 structural declaration).")},
   [{"type": "generated-by", "target_id": "pahcforce1A2",
     "note": "Doc_08 SS4 Connection 1 (mirror)."},
    {"type": "terms-set-by", "target_id": "pahcforce1B1",
     "note": "Doc_08 SS5 G01 row (mirror): the inheritance sets the contest's terms."}],
   ["srcPAHCP02", "srcPAHCP03", "srcPAHCP05"]),
 F("pahcforce2B2",
   "Transmission - The Correspondence Network as Carrier and Filter "
   "(2B-2)",
   "2B - Ongoing / Internal (Transmission dimension)",
   ("Named mechanisms, not undifferentiated tradition: Polycarp's "
    "requested forwarding; 1 Clement via Codex Alexandrinus (a leaf "
    "lost) and Hierosolymitanus (1056 - also ~90% of the Didache, "
    "undiscovered until 1873); Ignatius's middle recension "
    "authenticated only through a two-century critical dispute; "
    "Hermas an eclectic patchwork with the Simonides forgery-adjacent "
    "complication. Confidence: Documented (manuscript facts) / "
    "Inferential-Thin (the selection mechanisms) (Doc_08 2B-2 L1)."),
   ("A letter was copied and carried because a sister ekklesia asked, "
    "or because it answered a dispute worth keeping - decided "
    "community by community, occasion by occasion (Doc_08 2B-2 L2)."),
   ("The texts that survived best had institutional backing or "
    "apologetic value to later, more secure generations - the "
    "world's most vulnerable material was structurally less likely "
    "to survive regardless of prevalence: the network 'determined "
    "which portions of this world's own self-understanding are "
    "recoverable today at all - a selection effect, not a neutral "
    "pipe' (Doc_08 2B-2 L3)."),
   {"elaboration": (
     "G02 and this force are one mechanism at two angles - lived "
     "practice and survival filter; every Author-Gravity and "
     "missing-voice finding in this migration is downstream of this "
     "force's operation (S2.5 Layer-4 authoring from Doc_08 SS5 G02 "
     "row + SS6).")},
   [{"type": "enabled-by", "target_id": "pahcforce1A1",
     "note": "Doc_08 SS4 Connection 4 (mirror)."},
    {"type": "continues-as", "target_id": "pahcforce3B2",
     "note": ("The same filter at the ending: selective canonization "
              "is this force's later-stage instance (Doc_08 3B-2 L3: "
              "'one further, later-stage instance of the same "
              "structural filter').")}],
   ["srcPAHCP04", "srcPAHCP02", "srcPAHCP01", "srcPAHCP05"]),
 F("pahcforce2B3",
   "Martyrdom as Formation-Shaping Meaning-Response (2B-3 = G04)",
   "2B - Ongoing / Internal",
   ("Exactly two data points within the Native base, both Strand A: "
    "Ignatius's food-for-wild-beasts self-presentation and the "
    "Martyrdom of Polycarp's bone-collection and dies natalis. "
    "Confidence: Documented at the narrowest scope (these two "
    "individuals) / Contested-Inferential-Thin beyond (Doc_08 2B-3 "
    "L1)."),
   ("For the one awaiting arrest, the exposure could turn toward "
    "eager anticipation rather than dread; for the community "
    "receiving him, gathering annually at a leader's tomb to mark "
    "his death as birth carried his example into ongoing life "
    "(Doc_08 2B-3 L2)."),
   ("Sustains and intensifies in direct proportion to 2A-1; begins "
    "organizing time itself around a death-as-birth event - though "
    "that belongs more to what this world hands off than to what "
    "its own liturgy yet organizes around (Doc_08 2B-3 L3)."),
   {"elaboration": (
     "FORCE IDENTITY DECLARED: this force IS gravity G04 "
     "(pahcgrav004) - and its Strand-A-only scope is a fact about "
     "EVIDENCE, not established absence: the re-test instruction "
     "rides both records (S2.5 structural declaration).")},
   [{"type": "generated-by", "target_id": "pahcforce2A1",
     "note": "Doc_08 SS4 Connection 2 (mirror) - the matrix's most explicitly evidenced connection."}],
   ["srcPAHCP03", "srcPAHCP16"]),
 F("pahcforce2B4",
   "Boundary-Drawing Against Contemporary Rivals (2B-4 = G05)",
   "2B - Ongoing / Internal",
   ("Ignatius's anti-docetic argument across several letters - "
    "substantively developed by exactly one voice within the Native "
    "streams. Confidence: Documented (that he argues it) / "
    "Inferential-Thin (representativeness beyond his addressees) "
    "(Doc_08 2B-4 L1)."),
   ("A rival teaching denying the body's real suffering felt near "
    "enough to argue against at length; refusing a rival's eucharist "
    "and holding the bishop's own were the same act - belonging and "
    "boundary never two decisions (Doc_08 2B-4 L2)."),
   ("Grounds the world's ontological commitment that the body's "
    "reality is load-bearing; the least evidentially secured "
    "confirmed gravity - and for exactly that reason the clearest "
    "demonstration that even the boundary was actively defended, "
    "not inherited already-drawn (Doc_08 2B-4 L3)."),
   {"elaboration": (
     "FORCE IDENTITY DECLARED: this force IS gravity G05 "
     "(pahcgrav005); the Connection-5 convergence with legal "
     "precarity carries its own-synthesis disclosure everywhere it "
     "appears (S2.5 structural declaration).")},
   [{"type": "generated-by", "target_id": "pahcforce2A2",
     "note": "Doc_08 SS4 Connection 3 (mirror)."},
    {"type": "convergence-proposed-with", "target_id": "pahcforce2A1",
     "note": "Doc_08 SS4 Connection 5 (mirror; the disclosed own-synthesis)."}],
   ["srcPAHCP03"]),
 F("pahcforce3A1",
   "A Systematic, Succession-Argument Theological Mode Emerging in "
   "Adjacent Regions (3A-1)",
   "3A - Ending-or-Transforming / External",
   (EXT_NOTE +
    "Irenaeus's Adversus Haereses (c. 180, Gaul) making the first "
    "explicit four-Gospel apostolic-succession argument; Tertullian's "
    "Apologeticus (197, Carthage) inaugurating the confident Latin "
    "apologetic corpus - both arguing FROM succession as secured "
    "rather than still-argued. Confidence: Well-established (the "
    "texts) / DMR (the new-mode characterization, the project's own "
    "comparative reading) (Doc_08 3A-1 L1)."),
   ("This world's own texts show no awareness of encountering a "
    "secured, systematized succession as settled fact - the "
    "recoverable felt experience is of a still-argued, still-urgent "
    "question; how a member in the final years met the newer mode is "
    "not recoverable (Doc_08 3A-1 L2)."),
   ("Marks the point at which the defining tension becomes "
    "resolved-in-direction rather than actively argued - the closing "
    "boundary, precisely because arguing rather than inheriting was "
    "this world's defining character (Doc_08 3A-1 L3)."),
   {"elaboration": (
     "The world ends by definition, not defeat: a formation logic "
     "that has settled elsewhere is what closes a world whose "
     "character WAS the arguing - 'this world could not, by its own "
     "defining character, survive its own authority question "
     "actually being resolved' (S2.5 Layer-4 authoring from Doc_08 "
     "3B-1 L3, which this force twins).")},
   [{"type": "twins-with", "target_id": "pahcforce3B1",
     "note": ("Doc_08 SS4 Connection 6: two faces of the same "
              "transition from argued to settled - not independent "
              "events.")}],
   ["srcPAHCP15"]),
 F("pahcforce3A2",
   "The Emergence of a Neighboring, Distinct Formation World - "
   "Alexandria (3A-2)",
   "3A - Ending-or-Transforming / External",
   (EXT_NOTE +
    "The Step 0 Conclusion independently dates World #2 (Alexandrian "
    "catechetical, teaching-relationship formation logic) to c. "
    "190-254; the two worlds' ranges overlap only at this world's "
    "closing edge (c. 190-200). Confidence: Documented per the Step 0 "
    "Conclusion's own dating (Doc_08 3A-2 L1)."),
   ("Not recoverable - this world's core-region texts do not register "
    "Alexandria's emerging mode as a felt presence within its own "
    "lifetime (Doc_08 3A-2 L2; the absence stated, never filled)."),
   ("A genuine, evidence-supported HANDOFF rather than a "
    "contradiction - a different formation logic emerging in a "
    "different region at the precise moment this world's own is "
    "closing (Doc_08 3A-2 L3)."),
   {"elaboration": (
     "The fleet's own architecture mirrors this force: the migrated "
     "Alexandria world (frozen) is this handoff's other side - the "
     "pairing guidance at S2.7a can hold the two worlds' own "
     "documents' agreeing boundary (S2.5 Layer-4 authoring from "
     "Doc_01 SS8.2 + the fleet state).")},
   [],
   ["srcPAHCP06"]),
 F("pahcforce3B1",
   "Monepiscopacy's Consolidation as the Dominant Emerging Pattern "
   "(3B-1)",
   "3B - Ending-or-Transforming / Internal",
   ("Earliest in Antioch/western Asia Minor via Ignatius; latest in "
    "Rome, where Lampe's fractionated reading finds no monarchical "
    "bishop possibly before Victor I (189-199); by c. 200 "
    "single-bishop governance dominant even in Rome. Confidence: "
    "Well-established (the general pattern, Sullivan/Lampe) / "
    "Contested (the precise Roman dating) (Doc_08 3B-1 L1)."),
   ("Not recoverable as one unified experience - the texts record no "
    "moment of resolution, only the gradual, regionally uneven "
    "disappearance of the plural-college alternative as a live "
    "option; where sources are silent on how a Strand B member "
    "experienced it, no experience is constructed (Doc_08 3B-1 "
    "L2)."),
   ("The internal dissolution of the world's characteristic form - "
    "the RESOLUTION (not continuation) of G01's defining tension; "
    "one of the three convergent closing fronts (Doc_08 3B-1 L3)."),
   {"elaboration": (
     "The strand-plural world ends when its plurality does: the "
     "record store's own strand note (pahccore001 body) and this "
     "force are the same finding at open and close (S2.5 Layer-4 "
     "authoring).")},
   [{"type": "twinned-by", "target_id": "pahcforce3A1",
     "note": "Doc_08 SS4 Connection 6 (mirror)."}],
   ["srcPAHCS05", "srcPAHCP03"]),
 F("pahcforce3B2",
   "Transmission at the Ending - Selective Canonization (3B-2)",
   "3B - Ending-or-Transforming / Internal (Transmission dimension)",
   ("Later transmission favored texts supporting the settlement: "
    "Ignatius preserved and eventually authenticated through two "
    "centuries of criticism precisely because of later canonical "
    "importance; 1 Clement folded into Codex Alexandrinus; Hermas - "
    "cited as scripture by Irenaeus/Clement/Origen, in Sinaiticus - "
    "later excluded by Athanasius; the Didache gone from circulation "
    "for ~18 centuries. Confidence: Documented (survival facts) / "
    "Inferential-Thin (the causal claim, the doc's own synthesis) "
    "(Doc_08 3B-2 L1)."),
   ("Not recoverable - no source registers awareness of its own "
    "eventual selective transmission; a judgment available only in "
    "retrospect, not attributed to the world's self-understanding "
    "(Doc_08 3B-2 L2)."),
   ("The direct mechanism behind Strand B's thinness in the modern "
    "evidentiary base (Hermas above all) independent of its own-time "
    "prevalence - the Affirmative-Duty disclosure's later-stage "
    "instance (Doc_08 3B-2 L3)."),
   {"elaboration": (
     "The migration itself works downstream of this force: every "
     "strand-asymmetry this record store carries (Strand B's "
     "thinner base; the Didache's single manuscript) is this "
     "force's product, named as such rather than treated as the "
     "world's own shape (S2.5 Layer-4 authoring from Doc_08 SS6 + "
     "the Affirmative Duty).")},
   [{"type": "continuation-of", "target_id": "pahcforce2B2",
     "note": "Mirror: the same structural filter, later stage."}],
   ["srcPAHCP01", "srcPAHCP02", "srcPAHCP03", "srcPAHCP05"]),
]

# FEC -> gravity_links (chunk FECs name G-ids; G0n -> pahcgrav00n)
FEC_LINKS = {
    "pahcstory001": ["pahcgrav002", "pahcgrav004", "pahcgrav005"],
    "pahcstory002": ["pahcgrav002", "pahcgrav001"],
    "pahcstory003": ["pahcgrav002"],
    "pahcstory004": ["pahcgrav003"],
    "pahcstory005": ["pahcgrav001", "pahcgrav003"],
    "pahcstory006": ["pahcgrav007"],
    "pahcstory007": ["pahcgrav001"],
    "pahcstory008": ["pahcgrav004"],
    "pahcstory010": ["pahcgrav007"],
    "pahcstory011": ["pahcgrav007", "pahcgrav001", "pahcgrav005"],
    "pahcstory012": ["pahcgrav001", "pahcgrav007", "pahcgrav002"],
    # pahcstory009 ('not itself evidence for a confirmed Doc_04
    # gravity') and pahcstory013 ('not classified as direct evidence
    # for either named gravity specifically'): UNLINKED BY THEIR OWN
    # FECs - body-parked, S2.8 view falls back (the HAL precedent
    # with the chunks' own explicit statements).
}

FEC_RE = re.compile(
    r"\[Formation Ecology Connection - parked at the S2\.4-equivalent"
    r"[^\]]*\]\s*(.*?)(?=\n\n\[|\Z)", re.S)


def main():
    (OUT / "gravity").mkdir(exist_ok=True)
    for rec, body in GRAVITIES:
        emit_record(rec, body, OUT / "gravity" / f"{rec['id']}.md")
    (OUT / "force").mkdir(exist_ok=True)
    for rec in FORCES:
        emit_record(rec, ("S6.2/PAHC S2.5-equivalent force record "
                          "(2026-07-31) from " + D8 + " (three layers "
                          "condensed with citations; Layer 4 authored). "
                          "connections[] = Doc_08 SS4's six named "
                          "cross-cell connections + SS5 rows, mirrored; "
                          "the four force=gravity identities and the "
                          "corrected External rule declared in the "
                          "migrator's docstring and the records "
                          "themselves."),
                    OUT / "force" / f"{rec['id']}.md")
    for sid, gids in FEC_LINKS.items():
        path = OUT / "story" / f"{sid}.md"
        front, body = read_record(path)
        m = FEC_RE.search(body)
        assert m, sid
        fec = m.group(1).strip()
        j = fec.find("\n\n[Source Identification")
        if j >= 0:
            fec = fec[:j].strip()
        links = [{"gravity_id": gids[0], "note": (
            "CO-P2-04: the chunk's Formation Ecology Connection, verbatim "
            "(the S2.4 parking, converted at S2.5): " + fec)}]
        for g in gids[1:]:
            links.append({"gravity_id": g, "note": (
                "Named in the same FEC (full text on this record's first "
                "gravity link).")})
        front["gravity_links"] = links
        write_record(path, front, body)
    core_path = OUT / "world_core" / "pahccore001.md"
    front, body = read_record(core_path)
    front["gravities"] = ["pahcgrav001", "pahcgrav002", "pahcgrav003",
                          "pahcgrav004", "pahcgrav005", "pahcgrav007"]
    write_record(core_path, front, body)
    print(f"wrote {len(GRAVITIES)} gravities (6 classified + G06 "
          f"not-advanced), {len(FORCES)} forces, {len(FEC_LINKS)} "
          f"stories linked (2 declared unlinked by their own FECs), "
          f"core updated")


if __name__ == "__main__":
    main()
