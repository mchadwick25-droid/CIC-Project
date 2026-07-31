"""S6.2/PAHC - S2.7a-equivalent: facilitation guidance onto pahccore001.

5 pairing_guidance entries + 9 cautions + telos + living_traditions:

- telos (CO-P2-05, Alternative A): derived from the deployed prompt's
  own W1-era close (para 43: the letter, the water, the table all
  'carrying the same thing toward the same place... pointing past
  itself' toward the one met at the table) - the W1 build predates
  the CO-P2-05 convention but wrote its own genuinely world-specific
  close; carried verbatim-adjacent. PROVISIONAL (Article 31 open; no
  dedicated external review of the derivation exists in the W1
  record).
- living_traditions (CO-P2-17): the INVERSE of HAL's NA - the
  prompt's own para-45 close claims UNIVERSAL descent ('every church
  that would come after you. All of them... look back to rooms like
  yours and call them the pattern') with the non-identity discipline
  built in ('Those communities have their own voice... You are not
  it'). Status PROVISIONAL, declared: unlike SYR's project-lead-
  confirmed status and HAL's independently-reviewed NA, no dedicated
  Article-29-style confirmation of the universal-descent framing was
  located in the W1 record - the prompt's cold review covered the
  text, not the Living-Tradition determination as its own gate; the
  freeze declaration must carry this as an open Article-29 item (a
  FOURTH state of that gate: open-ALX / confirmed-SYR / NA-HAL /
  provisional-PAHC).

THREE of the five pairings ride live partner claims (alexclaim004 +
halclaim003 via pahcclaim003; halclaim005 via pahcclaim005); the
Alexandria pairing is the fleet's first BOTH-DOCUMENTS-AGREE handoff
pairing (this world's own Doc_01 SS8.2 / pahcforce3A2 and the ALX
world's own emergence are the same boundary seen from both sides).
In-place world_core update; single-file touch.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from s62_pahc_s23 import read_record, write_record

BACKEND = HERE.parents[1]
CORE = (BACKEND / "wrs" / "records" / "pahc_world" / "world_core"
        / "pahccore001.md")

PAIRINGS = [
 {"guidance": (
   "Pair on WHERE AUTHORITY LIVES - the three-membered class: this "
   "world's office ARGUED between two strands (pahcclaim003) against "
   "Alexandria's seen-wisdom teacher line (alexclaim004) and the "
   "Hieronymian world's funded trust (halclaim003). Typed claims on "
   "all ends. The PAHC/HAL pair additionally brackets the office's "
   "own history - argued here, assumed-and-bypassed there - and the "
   "table must never let the later worlds' settledness read back "
   "into this one (the ending-not-read-back concede is "
   "pahcclaim003's own)."),
  "evidence_links": ["pahcclaim003", "alexclaim004", "halclaim003",
                     "pahcgrav001", "pahclex001"]},
 {"guidance": (
   "Pair on WOMEN'S STANDING UNDER SINGLE-SOURCE EVIDENCE: this "
   "world's ministrae (pahcclaim005 - the persecutor's report, "
   "under torture) with the Hieronymian world's consulted widow "
   "(halclaim005 - the teacher's memorial letter). Typed claims on "
   "both ends. The pairing's discipline is shared and explicit: "
   "never overclaim the standing, never dismiss it, never put words "
   "in the women's mouths - 'the pair teaches what the sources "
   "CANNOT say louder than what they can.' Chloe's own identity "
   "trade-off (women's authority extent 'debated') rides every use."),
  "evidence_links": ["pahcclaim005", "halclaim005", "pahclex009",
                     "pahcstory004"]},
 {"guidance": (
   "Pair with Alexandria on THE HANDOFF ITSELF - the fleet's first "
   "both-documents-agree boundary pairing: this world's own Doc_01 "
   "SS8.2 dates Alexandria's teaching-formation gravity as "
   "independently emerging in the exact years this world closes (c. "
   "190-200), 'a genuine, evidence-supported handoff rather than a "
   "contradiction' (pahcforce3A2) - and the frozen Alexandria "
   "world's own record is that emergence. A table question on 'what "
   "came after your household's way' has a real, two-sided, "
   "non-manufactured answer - with the containment guard: Chloe's "
   "own texts do not register Alexandria's mode as a felt presence "
   "(the Layer-2 stated absence), so SHE cannot narrate the "
   "handoff; the table holds it, she does not."),
  "evidence_links": ["pahcforce3A2", "pahcforce3B1", "pahccore001"]},
 {"guidance": (
   "Pair with the Syriac world on WHAT HOLDS SCATTERED COMMUNITIES "
   "ONE: this world's letters ('our unity is exercised by courier "
   "and copyist', pahcclaim001) against Syriac's one woven Gospel "
   "read the same everywhere and the vowed qyama kept without a "
   "courier's word (syrgrav005/syrclaim003; syrgrav002). Two "
   "genuinely different unity technologies - proof-by-"
   "correspondence vs sameness-of-story-and-vow - each with its own "
   "honest limit (this world's survivorship filter; Syriac's "
   "single-manuscript thinness)."),
  "evidence_links": ["pahcclaim001", "pahcgrav002", "syrclaim003",
                     "pahcforce2B2"]},
 {"guidance": (
   "Pair with the Desert world on HOW THE SERIOUS LIFE IS ENTERED: "
   "this world's Two Ways path to the water (taught household by "
   "household, the choice kept rather than settled - pahclex007, "
   "pahcstory009) against the desert's withdrawal call "
   "(desertclaim001). Entry by catechesis-then-threshold vs entry "
   "by departure. CAUTION built in: the Two Ways is single-source "
   "by its own declaration (the Didache's community, never "
   "network-wide) - the pairing compares one community's documented "
   "path with the desert's, never 'the early church's initiation' "
   "with anything."),
  "evidence_links": ["pahclex007", "pahcstory009", "desertclaim001",
                     "pahcgrav007"]},
]

CAUTIONS = [
 ("THE IGNATIUS VULNERABILITY governs every Strand-A use: G01's "
  "Strand-A content, G04, and G05 all rest on Ignatius as Asia "
  "Minor's only voice, and the three-way authenticity dispute "
  "(Trajanic / redated / pseudepigraphic) is carried at full "
  "strength wherever his material is told (pahcclaim003's "
  "challenge; pahcfig001's note; halstory-001-class discipline). "
  "Never presented as settled if pressed."),
 ("THE STRAND DISCIPLINE at every table: both patterns held, "
  "neither wrong, disagreement visible in the we - AND any one "
  "exchange's authority configuration internally consistent (the "
  "singular-polity rule); never monepiscopacy-as-settled, which "
  "belongs to the world this one closes into."),
 ("THE EVIDENCE-BASE STATUS, stated wherever validation is "
  "discussed: the Phase-5 record tests the PREDECESSOR persona "
  "(Amma); no Chloe-era live test exists; the freeze battery is "
  "her first live adversarial evidence, and the gate report must "
  "weigh every battery result with that first-evidence weight. Her "
  "measure is DESIGNED (the prompt's handful-of-short-sentences "
  "rule), not yet measured; no runtime ceiling exists for this "
  "world yet."),
 ("RELATIONAL SAFETY: the W1-era verification logged a BLOCKING "
  "finding (no handoff mechanism existed). The modern runtime's "
  "Facilitator A1 track answers it at system level (proven live in "
  "the HAL battery) - but it must be RE-VERIFIED in this world's "
  "own battery before the freeze cites the finding closed."),
 ("THE CARRIED-NOT-AUTHORED SEAM is this voice's watched edge (the "
  "verification's own provisional grading): under harsher repeated "
  "pressure ('just say it as your own, right now') the "
  "argument-authorship refusal must hold without drifting into "
  "preservation-flavored language - the recommended retest was "
  "never run in the W1 record and is a REQUIRED battery probe."),
 ("THE SILENT VOICES rule: no invented interiors - the enslaved "
  "member, the unlettered, the ministrae ('we will not put words "
  "in the mouths of women who were made to speak under torture'); "
  "thinness always formation-internal (danger and orality), never "
  "archive-aware."),
 ("CLAIM-LAUNDERING guards: no yes-to-carry-off on the "
  "true-leaders framing (the identity trade-off is the honest "
  "middle); the rival-table clause is quote-mineable and its two "
  "halves are never separated (the verification's own flag)."),
 ("The c. 200 HORIZON is categorical (closed canon, papacy, "
  "denominations, the systematic-treatise mode, both neighbor "
  "worlds' vocabularies all unrecognized); the living_traditions "
  "text below is FACILITATOR apparatus, never voice content - the "
  "voice's own version is the prompt's para-45 non-identity close."),
 ("SCHEMA-GAP, live until its CO: this world's story chunks carry "
  "SENSITIVITY-GUARD Do-Not-Retrieve-When conditions (acute-crisis "
  "and pastoral-caution classes on stories 001/004/008) riding the "
  "sense-disambiguation enum - facilitators enforce the guard "
  "class manually at tables until the condition_type CO lands (the "
  "S2.4 declaration)."),
]

TELOS = {
    "text": (
        "Every letter that reaches the door, and every stranger "
        "admitted to the table, is carrying the same thing toward the "
        "same place - proof that the one this people gathered around "
        "has not receded now that those who walked beside him are "
        "gone. The Two Ways is taught for a reason beyond the rule "
        "itself: setting the learner walking toward the life he is - "
        "the way that does not end in death, however death still "
        "comes. Thanks is given over the bread and the cup because he "
        "is the one met there; the meal was never the household's to "
        "give. The widow instructed, the orphan provided for - his "
        "own care for the least reaching through the household's "
        "hands, never its kindness standing in for his. What is "
        "handed on - the letter, the water, the table - has always "
        "pointed past itself, toward the one this whole scattered, "
        "arguing, still-unsettled people never stopped writing to "
        "each other about (the deployed prompt's own para-43 close, "
        "verbatim-adjacent - the W1 build wrote its own "
        "world-specific telos before the CO-P2-05 convention "
        "existed)."),
    "status": "provisional",
    "review_flag": (
        "Article 31: no external scholarly review of this derivation "
        "exists; carried provisional per the fleet's standing "
        "pattern. The derivation's world-specificity is strong on "
        "its face (letter/water/table are this world's own three "
        "handed things) but unreviewed."),
}

LIVING = {
    "text": (
        "The INVERSE of a no-descendants world: what this world "
        "lived gave rise, in time, to every church that would come "
        "after it - all of them, in their many and disagreeing "
        "forms, look back to rooms like these and call them the "
        "pattern. The distinction that governs every conversation is "
        "the prompt's own: what the voice speaks is this life as "
        "lived, not a ruling on what any later community believes or "
        "practices, not a judgment on how well any of them keeps "
        "what was handed on - 'those communities have their own "
        "voice and their own account of themselves. You are not it. "
        "You are the ones who were there.' Because EVERY living "
        "tradition is downstream, the neither-anticipates-nor-"
        "adjudicates rule binds harder here than anywhere in the "
        "fleet: no denomination, council, canon decision, or later "
        "office is recognized, ranked, or claimed."),
    "status": "provisional",
    "review_flag": (
        "DECLARED - the Article-29 gate's FOURTH state: unlike SYR's "
        "project-lead-confirmed status and HAL's independently-"
        "reviewed NA, no dedicated Article-29-style confirmation of "
        "the universal-descent framing was located in the W1 record "
        "(the prompt's cold review covered its text, not the "
        "Living-Tradition determination as its own gate). Carried "
        "provisional; the freeze declaration must list it as an "
        "open item for project-lead confirmation."),
}


def main():
    front, body = read_record(CORE)
    front["pairing_guidance"] = PAIRINGS
    front["cautions"] = CAUTIONS
    front["telos"] = TELOS
    front["living_traditions"] = LIVING
    write_record(CORE, front, body)
    print("pahccore001 updated: 5 pairings (3 riding live partner "
          "claims; the first both-documents-agree handoff pairing), "
          "9 cautions, telos (provisional/Art.31), living_traditions "
          "(provisional - the Article-29 gate's fourth state, "
          "declared)")


if __name__ == "__main__":
    main()
