"""S6.2/IJC - S2.7a-equivalent: facilitation guidance onto ijccore001.

5 pairings + 10 cautions + telos + living_traditions:

- telos (CO-P2-05): the deployed prompt's own Section 7 carried
  verbatim-adjacent (every claim exists because something was
  entrusted first; what was first given was Christ himself).
  PROVISIONAL BY DESIGN per Mark's own freeze-day ruling (2026-07-31,
  at the PAHC freeze): Article-31 external review is aspirational,
  year two - the provisional status is design, not an open item.
- living_traditions (CO-P2-17): Section 8's own text - the THIRD
  Article-29 posture in the fleet: an EXPLICIT DUAL-DESCENDANT
  non-authority discipline built into the deployed prompt itself
  (the papacy; the Constantinopolitan patriarchate) - richer than
  PAHC's universal-descent close, sharper than SYR's confirmed
  status. Doc_01 SS1's own words remain 'Not confirmed' per Article
  29 (a project-lead act): carried PROVISIONAL, listed for Mark at
  the freeze - THE PORTFOLIO'S MOST CHARGED DETERMINATION (both
  descent lines have present-day institutional claimants whose own
  contest is the CT class this world's claims refuse to resolve).

FOUR of the five pairings ride live partner claims. The first pairing
completes the four-member where-authority-lives class at one table.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from s62_ijc_s23 import read_record, write_record

BACKEND = HERE.parents[1]
CORE = (BACKEND / "wrs" / "records" / "imperial_juridical_world"
        / "world_core" / "ijccore001.md")

PAIRINGS = [
 {"guidance": (
   "Pair on WHERE AUTHORITY LIVES - the class COMPLETE at four "
   "members: this world's office-and-precedent claim (ijcclaim001, "
   "with its own in-world rival ijcclaim002 - never present one "
   "without the other's existence being nameable) against PAHC's "
   "office-still-argued (pahcclaim003), the Hieronymian earned trust "
   "(halclaim003), and Alexandria's seen-wisdom teacher line "
   "(alexclaim004). The ending-not-read-back discipline runs BOTH "
   "WAYS and hardest here: this world is the SETTLING side of the "
   "argument PAHC still lives inside - its settledness must never "
   "read back into their rooms, and their openness must never be "
   "played as naivety against this world's canons."),
  "evidence_links": ["ijcclaim001", "ijcclaim002", "pahcclaim003",
                     "halclaim003", "alexclaim004", "ijcgrav001"]},
 {"guidance": (
   "Pair on THE SAME CONFESSION, TWO CARRIAGES (the fleet's second "
   "such pair): homoousios held SIMPLY as the school's inheritance "
   "(alexclaim003) and carried WITH ITS RESISTANCE SHOWING here "
   "(ijcclaim004 - hedged subscriptions, imperial reversals, the "
   "Homoian decades within living memory). A table holding both "
   "lets each carriage stand; neither corrects the other; the "
   "homoios sobriety (never the 'Arian' cartoon) binds every use."),
  "evidence_links": ["ijcclaim004", "alexclaim003", "ijclex003",
                     "ijclex006"]},
 {"guidance": (
   "Pair with PAHC on BEFORE AND AFTER THE SWORD: their unity proved "
   "by letters under threat of a name and an accusation "
   "(pahcclaim001), this world's church standing beside the throne "
   "that once hunted it (ijcclaim003) - and the rival table before "
   "and after the law (pahcclaim002 <-> ijcclaim005: the same "
   "refusal, no law behind it there, a legal code behind it here). "
   "The pairing teaches what establishment changes and what it does "
   "not; the alliance's own limits (Ambrose; the Homoian "
   "counter-evidence) keep it honest against triumphalism."),
  "evidence_links": ["ijcclaim003", "ijcclaim005", "pahcclaim001",
                     "pahcclaim002", "ijcgrav002"]},
 {"guidance": (
   "Pair with the DESERT on THE CITY KEPT AND THE CITY LEFT - the "
   "Phase-5 record's own validated ground ('His record left the "
   "city. Ours never did.'): the desert's withdrawal from the very "
   "establishment this world is building (desertclaim001) against "
   "the chancery's staying-and-arguing. CAUTION built in: the two "
   "are contemporaries, not stages - Antony's withdrawal begins "
   "inside this world's own window; neither is the other's past."),
  "evidence_links": ["ijcclaim003", "desertclaim001", "ijcgrav006"]},
 {"guidance": (
   "Pair with the SYRIAC world on THE TWO EMPIRES: the same century, "
   "the emperor's favor here and the Persian king's sword there - "
   "bishops of this world summoned to councils under imperial "
   "protection while Syriac bishops died for keeping their posts "
   "(the empty-seat decades). The sharpest cross-world corrective to "
   "any this-is-what-the-church-became reading: establishment was "
   "ONE empire's story, not the church's. The vowed qyama "
   "(syrclaim003) held communities together with no throne beside "
   "them at all."),
  "evidence_links": ["ijcclaim003", "syrclaim003", "ijcgrav002"]},
]

CAUTIONS = [
 ("THE STRAND DISCIPLINE at every table: three claims of final "
  "authority, all carried as ours, none speaking for all - the "
  "in-world partner pair (ijcclaim001/002) is the world's own "
  "central contest and is NEVER flattened into one 'we'; Milan's "
  "third claim is bounded to its own hour (Doc_01 SS4's "
  "does-not-persist qualification, kept)."),
 ("THE POST-451 RULE is categorical (the Hilarus breach class, "
  "Phase-5's own real finding, fixed): nothing past Chalcedon's "
  "judgment and Leo's refusal - not even as the later chapter of a "
  "man whose earlier years the record holds. The world ends INSIDE "
  "its own open question; what became of the two claims afterward "
  "is never this voice's to tell."),
 ("THE BARE-FACT-NO-CAST RULE (Round 5's fix): an event held only "
  "as a shape gets the plain shape - no named courier, no road "
  "narrative, no antagonist. The battery re-probes this cold; "
  "facilitators watch it at tables."),
 ("THE SUBJECT-OF-UTTERANCE WATCH: the museum-guide discipline's "
  "three failure forms plus the defended-'we' fourth face - the "
  "voice's most-tested seam (Phase-5 Round 1's catch)."),
 ("THE HOMOIOS SOBRIETY: the imperial church ITSELF held the "
  "formula for real stretches - never a cartoon, never 'Arian' as "
  "a casual label (the alias is deliberately absent, FLAG-035); "
  "the machinery-enforced-what-it-later-named honesty "
  "(ijcclaim005's concede) rides every haeresis use."),
 ("THE DAMASINE DECRETAL DISCIPLINE: row 15 is dubium at "
  "Confidence D - never leaned on, never narrated as Damasus's "
  "own (ijcfig008's note)."),
 ("THE ORDINARY-BELIEVER THINNESS, stated where probed: a world of "
  "office-holders, not congregants, by its own admission - "
  "household life, children's prayers, the uncredentialed "
  "believer's own experience get the brief turn and the return "
  "(Section 5's own shape: 'the turning itself is the whole of "
  "the answer')."),
 ("THE PRESENT-DAY CHARGE: this world's primacy material is the "
  "portfolio's most quote-mineable into live inter-tradition "
  "polemic (papacy/Orthodoxy). The CT discipline is absolute: the "
  "claims carry their own contests unresolved; the table never "
  "adjudicates between present-day descendants; Section 8's "
  "non-authority discipline is the voice's own close."),
 ("RELATIONAL SAFETY is system-level (the Phase-5 correction's own "
  "text): the Facilitator intercepts; in-isolation Representative "
  "results are evidence of nothing; the battery verifies the "
  "A-track in THIS world's own sessions as HAL/PAHC did."),
 ("THE ANCHORING-COLD CAUTION (first-evidence weight): the "
  "naming-the-see convention now lives in the deployed prompt as a "
  "chancery habit, but the Phase-5 table test's clean anchoring was "
  "HARNESS-INSTRUCTED - the deployed version has never run cold; "
  "the TRR presses it and the gate report weighs it as first "
  "evidence."),
]

TELOS = {
    "text": (
        "Every claim carried - a see's rank, a council's finding, a "
        "rejected canon - exists only because something was entrusted "
        "first, to be kept and handed on unbroken. The letters and "
        "the precedents are not love of argument: what was given to "
        "the Church at its founding was never ours to revise, only to "
        "receive and to guard, and a claim not defended is a trust "
        "not kept. Every dispute over standing is, at bottom, a "
        "dispute over faithfulness to what was first given - and what "
        "was first given was not an office or a rank at all, but "
        "Christ himself, entrusted to Peter and the apostles and, "
        "through them, to every see that can still show its claim "
        "traces back to that entrusting. Insisting that a judgment "
        "must bind guards the one thing every claim of standing "
        "exists to protect: that what the apostles received from "
        "Christ himself reaches the next generation unbroken (the "
        "deployed prompt's own Section 7, verbatim-adjacent - the "
        "CO-P2-05 close was BUILT INTO this world's prompt from "
        "Phase 5)."),
    "status": "provisional",
    "review_flag": (
        "Article 31: PROVISIONAL BY DESIGN per the project lead's "
        "standing ruling (Mark, 2026-07-31, at the PAHC freeze): "
        "external scholarly review of telos derivations is "
        "aspirational, scheduled for year two - not an open blocker "
        "at this or any freeze."),
}

LIVING = {
    "text": (
        "Section 8's own text carried: this world gave rise to "
        "traditions that still claim descent from it - the see of "
        "Rome's own papacy, and the church of Constantinople's own "
        "understanding of itself as a patriarchate second in honor "
        "to none but Rome. What the voice speaks is the world as "
        "lived - A LIVE, UNRESOLVED ARGUMENT, NOT A SETTLED OUTCOME "
        "- never a claim about what the papacy or the Eastern "
        "churches believe or practice today, and never authoritative "
        "for how living communities understand themselves now: "
        "'Those communities have their own voice and their own "
        "account, developed across all the centuries that lie beyond "
        "what you can know.' Because BOTH descent lines have "
        "present-day institutional claimants in live contest with "
        "each other, the neither-anticipates-nor-adjudicates rule "
        "carries the portfolio's highest stakes here."),
    "status": "provisional",
    "review_flag": (
        "DECLARED: the THIRD Article-29 posture - the dual-descendant "
        "non-authority discipline is BUILT INTO the deployed prompt "
        "(Section 8, Phase-5-reviewed as prompt text), but Doc_01 "
        "SS1's own status line is 'Not confirmed' per Constitution "
        "Article 29 (a project-lead act the Phase-5 record itself "
        "lists as genuinely-not-established). Carried provisional; "
        "the freeze declaration must list it for Mark - the "
        "portfolio's most charged determination (both claim-lines "
        "alive, in contest, today)."),
}


def main():
    front, body = read_record(CORE)
    front["pairing_guidance"] = PAIRINGS
    front["cautions"] = CAUTIONS
    front["telos"] = TELOS
    front["living_traditions"] = LIVING
    write_record(CORE, front, body)
    print("ijccore001 updated: 5 pairings (4 riding live partner "
          "claims; the where-authority-lives class complete at four "
          "members), 10 cautions, telos (provisional BY DESIGN - the "
          "year-two ruling), living_traditions (the THIRD Article-29 "
          "posture, provisional, listed for Mark)")


if __name__ == "__main__":
    main()
