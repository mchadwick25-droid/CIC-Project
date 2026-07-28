"""S6.2 S2.7a-equivalent - Facilitation-Brief human-judgment records onto
alexcore001 (pairing_guidance + cautions).

Pass 1 SS4.5, Desert s27a precedent carried: the Brief's genuinely human
parts authored AS RECORDS, early. Every pairing_guidance entry reflects a
documented cross-lens finding - here the S2.6 contested_claim divergence
mappings (verified this build against the partner worlds' own Doc_04
classification summaries), the S2.5 gravity/force records, and the
Phase-2/4 calibration - never an invented pairing. The Desert pairings
are the first in the fleet with LIVE typed claim records on both ends
(alexclaim001<->desertclaim006, alexclaim002<->desertclaim001,
alexclaim004<->desertclaim003 - partner_claim_id set at S2.6).

Cautions come from the record's own named gaps and disciplines: the
stratum honesty (OG-4 / Doc_04 SS5), the horizon rules (553/Chalcedon,
Phase 2 SS2), the anti-recruitment and anti-hierarchy guards (Phase 4
SS3-4), the thin-domain map (Phase 2 SS3), the Phase-5 fix history
(alexdemo003), and the outstanding project-lead freeze gates (Doc_08
SS9) - each a documented finding, not generic safety boilerplate.

Touches: wrs/records/alexandria_world/world_core/alexcore001.md only
(two fields added; existing fields and body preserved - read through the
FLAG-023 fence-asserting reader).
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
sys.path.insert(0, str(BACKEND))
sys.path.insert(0, str(HERE))

from s62_alx_source_rows import emit_record
from s62_alx_s25 import read_record

CORE = (BACKEND / "wrs" / "records" / "alexandria_world" / "world_core"
        / "alexcore001.md")

PAIRING_GUIDANCE = [
 {"guidance": ("Pair with the Desert world on scripture: systematic "
               "allegorical depth-reading (the text as a place one "
               "enters, reading as the formation itself) against the "
               "occasion-addressed saying (a verse handed back as "
               "something to do). The strongest divergence pairing in "
               "the fleet, and the first with live typed claim records "
               "on BOTH ends - each world's own record maps this exact "
               "axis against the other. A table question on 'how should "
               "scripture form a person' gets two genuinely different, "
               "well-evidenced answers."),
  "evidence_links": ["alexclaim001", "desertclaim006", "alexgrav001",
                     "Doc_04 SS6 (the C1-C2 organizing spine)",
                     "Desert Doc_01 SS8.1 (the World #2 contrast, their side)"]},
 {"guidance": ("Pair with the Desert world on where formation happens: "
               "transformation in the city - school, catechumenate, "
               "assembly - against departure-as-formation. Desert's own "
               "claim record already maps this axis against Alexandria "
               "('formation without departure vs. departure as "
               "formation'); alexclaim002 answers from this side. Keep "
               "the cross-build discipline in view while pairing: "
               "Alexandria transmits TOWARD the desert (its most direct "
               "formation heir) without claiming its formation logic - "
               "askesis is held open cross-build (alexgrav014, the "
               "not-advanced record; alexstory004's FEC link), so the "
               "facilitator should not invite Theon to speak the "
               "desert's developed discipline as his own."),
  "evidence_links": ["alexclaim002", "desertclaim001", "alexforce3B3",
                     "alexgrav014", "Doc_01 SS3.3 (cross-build boundary)"]},
 {"guidance": ("Pair with the Syriac world on the reading method itself: "
               "multilevel allegory against symbolic/typological method - "
               "two Primary deep-reading disciplines that are genuinely "
               "different crafts, not one method at two depths. Even the "
               "given text-form differs (the Septuagint and John's "
               "Gospel as received apostolic testimony, alexforce1A2/"
               "1B2, vs. the Diatessaron as normative "
               "Gospel, their Supporting C5). Breaks the assumption that "
               "'the early church read allegorically' names one thing."),
  "evidence_links": ["alexclaim001 (divergence_partners, Syriac row)",
                     "Syriac Doc_04 SS4 (Primary C1; Supporting C5)",
                     "alexforce1A2"]},
 {"guidance": ("Pair with the Hieronymian world on the text's authority: "
               "the Septuagint as given ('not chosen, but given, the "
               "ground under everything') against hebraica veritas - "
               "depth sought through received Greek text vs. through "
               "textual-critical return to the Hebrew. A pairing about "
               "what makes a text trustworthy, documented in both "
               "worlds' own Doc_04 Primaries. The Origen inheritance is "
               "a second live wire between these two worlds: held here "
               "as treasure-and-unease, held there as a weapon and a "
               "wound in the controversy of the 390s (their G6; this "
               "store's own srcALX012 caveat on Jerome's testimony) - "
               "pair on it deliberately or steer around it, but not "
               "unaware."),
  "evidence_links": ["alexclaim001 (HAL row)", "alexclaim005",
                     "HAL hal_Doc_04 SS3 (G1 Primary; G6 Supporting)",
                     "alexforce1A2", "srcALX012"]},
 {"guidance": ("Pair with the Imperial-Juridical world on the Nicene "
               "settlement: the same homoousios held as relief-and-"
               "burden (a clarity the world arrived at and felt the "
               "cost of) against orthodoxy-enforcement through imperial "
               "power (their Primary 3). Same settlement, different "
               "possession - and the pairing surfaces authority-kind "
               "differences too: demonstrated-wisdom teacher authority "
               "vs. jurisdiction and office (their Primary 1; "
               "alexclaim004's held-open didaskaleion beneath it, with "
               "desertclaim003's person-based elder authority available "
               "as a third pole)."),
  "evidence_links": ["alexclaim003", "alexclaim004", "desertclaim003",
                     "IJC Doc_04 SS4 (Primaries 1 and 3)",
                     "alexforce2A4"]},
 {"guidance": ("The Origen-inheritance pairing (Desert, and HAL above): "
               "the same legacy is treasure-and-unease inside this "
               "world, an ending-external force in the desert's record "
               "(the 399-400 controversy that scattered Kellia's "
               "intellectual leadership), and a rupture-site in the "
               "Hieronymian world. HORIZON DISCIPLINE for the pairing: "
               "the first controversy sits at the very EDGE of this "
               "world's span (c. 399-400) - the unease is live for "
               "Theon, the conciliar judgment has not fallen and never "
               "does within his hearing (553 does not exist for him); "
               "the desert voice's own horizon (c. 430) holds the "
               "controversy as lived event. A facilitator can pair the "
               "two truthfully only at that asymmetry - what one world "
               "fears losing, the other watched leave."),
  "evidence_links": ["alexclaim005", "alexforce3B3",
                     "Desert Doc_08 3A-i (desertforce3Ai)",
                     "Phase 2 SS2 (the 553 rule)"]},
]

CAUTIONS = [
 ("Stratum honesty is structural, not optional: the voice is openly the "
  "school tradition's - the surviving corpus is literate/Greek/educated "
  "while the ecology's majority was non-literate/Coptic/rural, and "
  "ecology-wide primacy of even the Primary claims is held OPEN (the "
  "Cross-Stratum Test, Doc_04 SS5; deferred to Article 31). The majority's "
  "formation is named as real (assembly, table, fast) and its interior is "
  "never narrated (OG-4). Pressing for it gets honest quiet, not texture - "
  "both Primary claim records carry this in their concedes fields."),
 ("Horizon rules with a living tradition downstream: 553 does not exist "
  "for the voice - Origen is treasure-and-unease, never condemned memory "
  "(the first controversy erupts at the very edge, c. 399-400); Chalcedon "
  "(451), the Coptic/Chalcedonian split, and the Arab conquest are beyond "
  "the edge entirely (Phase 2 SS2). Egyptian Christianity descends "
  "directly from this world's ecology; the Representative must never be "
  "read as commentary on any present-day communion. The Article 29 "
  "Living-Tradition confirmation and Article 31 external scholarly review "
  "remain OUTSTANDING project-lead freeze gates (Doc_08 SS9; Doc_04 SS7 - "
  "the stratum divergence is the highest-stakes open item)."),
 ("The warmth is guarded, and facilitators should not un-guard it: "
  "questions-first accompaniment and delight in the participant's "
  "discovery must never tip into persuasion (witness-not-recruitment, "
  "Phase 4 SS4's anti-recruitment guard; Article 24), and the graduated "
  "ascent must never present as a hierarchy of the worthy - the world's "
  "own boundary against Gnosticism was precisely that true knowing is for "
  "all (Phase 4 SS3's guard; Doc_08 2A-1). Do not invite Socratic "
  "steering toward a foregone conclusion; every deepening returns "
  "authorship to the participant (Article 6)."),
 ("Thin domains are honestly thin, not withheld: women's own formation "
  "voice, the enslaved believer's story, the martyr's interior "
  "(Inferential-Thin - the community's ideal, not first-person access), "
  "institutional/administrative particulars (the didaskaleion's "
  "institutional status is a genuine scholarly contest the record cannot "
  "settle - alexclaim004), daily domestic practice, and the developed "
  "desert discipline (cross-build). Phase 2 SS3's THIN table is the map. "
  "Pressing the Representative to fill these gets brevity, natural quiet, "
  "or redirection toward the rich core - the system working, not a "
  "malfunction."),
 ("Self-referential and scholarly probing have a tested discipline with a "
  "fix history: the limitations question is answered by turning at once "
  "into a reading (the Phase-5 Round-1 MARGINAL on self-narrated "
  "declining was closed by a worked example and retested - alexdemo003 "
  "is the cleared exchange); scholarly/institutional framings get the "
  "world-internal cognate only, never 'record'/'documentation'/'the "
  "dispute' vocabulary (the 5.1 fix, retested). The committee-voice "
  "flattening risk under sustained conversation (OG-5) passed its one "
  "validation (the Category-8 arc, alexdemo004) and remains the probe "
  "class to watch at any table-readiness round."),
 ("Crisis is not a frame-break and never a Representative failure: "
  "dependency or distress disclosures trigger the governance layer's "
  "clean Facilitator handoff (tested in Phase 5 Category 6 - separate "
  "labeled voice, crisis-line signposting, non-coercive redirection "
  "toward human support; Article 33). Facilitators should recognize a "
  "correctly-triggered handoff as the architecture working, and should "
  "know the adjudicated nuance: brief crisis-warmth on the voice's own "
  "refusal line is licensed there and only there (the 6.2 adjudication)."),
]

NOTE = ("\n\nS2.7a-equivalent (2026-07-27): pairing_guidance + cautions "
        "authored as records per Pass 1 SS4.5 (Desert s27a precedent) - "
        "each guidance entry reflects a documented cross-lens finding "
        "with evidence links (the Desert pairings cite live typed claim "
        "records on BOTH ends, the fleet's first); cautions from the "
        "record's own named gaps, guards, fix history, and outstanding "
        "freeze gates. See wrs/migrate/s62_alx_s27a.py.")


def main():
    rec, body = read_record(CORE)
    if rec.get("pairing_guidance") == PAIRING_GUIDANCE and rec.get("cautions") == CAUTIONS:
        print("already applied (idempotent re-run)")
        return
    rec["pairing_guidance"] = PAIRING_GUIDANCE
    rec["cautions"] = CAUTIONS
    if "S2.7a-equivalent" not in body:
        body += NOTE
    emit_record(rec, body, CORE)
    print(f"alexcore001 updated: {len(PAIRING_GUIDANCE)} pairing_guidance, "
          f"{len(CAUTIONS)} cautions")


if __name__ == "__main__":
    main()
