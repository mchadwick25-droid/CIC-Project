"""S6.2/HAL - S2.7a-equivalent: facilitation guidance onto halcore001.

5 pairing_guidance entries (each evidence-linked) + 8 cautions + telos
+ living_traditions:

- telos: the CO-P2-05 standing convention (Alternative A, world-scoped)
  applied to HAL - the Permanent Prompt's own derivation ('every hour
  we gave... pointed past ourselves... toward the Word our own
  imperfect words were only ever trying to carry faithfully... toward
  the child in the cave'), verified at the Doc_10 Round-1 review as
  genuinely world-specific ('fails the swappable-to-another-world test
  in the right direction - it does NOT transfer'). STATUS PROVISIONAL:
  Article 31 external scholarly review remains open for this world.
- living_traditions: the CO-P2-17 standing convention applied - and
  for THIS world the finding is NOT APPLICABLE, itself CONFIRMED
  (World Profile SS9, strengthened at Round 1 to rule out the two
  obvious counter-candidates: the Hieronymite congregations are
  14th-century patron-adoptions, not institutional descendants of a
  double monastery that did not survive its own founders per Doc_08
  3B-2; Jerome's Doctor-of-the-Church veneration and the Vulgate's
  later status are textual/reputational, not institutional,
  correspondence). status='confirmed' per the schema enum - what is
  confirmed is the NA finding; Prompt Section 8 uses Version B.

FOUR of the five pairings ride the S2.6 live-partner claim links
(alexclaim001, desertclaim001, alexclaim004, alexclaim005) - the
typed-claim-on-both-ends pattern at its fleet maximum so far. The
fifth (violence/endurance vs Syriac) is a register pairing with
cross-world evidence links (the SYR pairing-5 precedent). In-place
world_core update (FLAG-023 reader); single-file touch.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from s62_hal_s23 import read_record, write_record

BACKEND = HERE.parents[1]
CORE = (BACKEND / "wrs" / "records" / "hieronymian_world" / "world_core"
        / "halcore001.md")

PAIRINGS = [
 {"guidance": (
   "Pair with Alexandria on WHAT THE TEXT ITSELF IS: this world's "
   "Hebrew-truth correction of the received Greek against the school's "
   "allegorical depth-reading OF that Greek. Typed claim records on "
   "BOTH ends (halclaim001 <-> alexclaim001): same seriousness about "
   "scripture as formative, and this world contests the very textual "
   "foundation the partner world reads from - a table question on "
   "'which Bible?' gets a live, historically real argument, with the "
   "Oea story (halstory03) as the concrete cost and the rare two-sided "
   "attestation (Augustine's own letters) keeping both voices "
   "honest."),
  "evidence_links": ["halclaim001", "alexclaim001", "halgrav001",
                     "srcHAL009", "halstory03"]},
 {"guidance": (
   "Pair with the Desert world on the SHAPE of renunciation: the "
   "emptied aristocratic household - public, watched, family-"
   "disrupting, still building at scale from what remained - against "
   "withdrawal-as-engagement. Typed claim records on BOTH ends "
   "(halclaim002 <-> desertclaim001), the shapes-of-asceticism class's "
   "third geography (with Syriac's town-refusal). The pairing carries "
   "its own literary bridge: this household wrote desert romances as "
   "its OWN answer to Egypt's stories (halstory09), and met Nitria on "
   "its founding journey (halstory01) - admiration and adaptation, "
   "never identity."),
  "evidence_links": ["halclaim002", "desertclaim001", "halgrav002",
                     "halstory09", "halstory01"]},
 {"guidance": (
   "Pair with Alexandria on AUTHORITY WITHOUT OFFICE: funded trust "
   "(patronage - 'trusted, and funded') against the school's seen "
   "wisdom ('trusted because others saw that he saw'). Typed claim "
   "records on BOTH ends (halclaim003 <-> alexclaim004). The pairing's "
   "sharpest exhibit is this world's own counter-current: Marcella, "
   "where demonstrated learning was held from materially independent "
   "standing - the place the two currencies meet in one person "
   "(halclaim005) - ALWAYS with the single-source frame attached and "
   "never as rivalry (the haldemo003 double-bait discipline)."),
  "evidence_links": ["halclaim003", "alexclaim004", "halgrav003",
                     "halclaim005", "haldemo003"]},
 {"guidance": (
   "Pair with Alexandria on ORIGEN HIMSELF - the fleet's first pairing "
   "where one world contests the other world's own teacher (halclaim004 "
   "<-> alexclaim005, typed on both ends): the school holds Origen's "
   "speculative teaching as exploration under the Rule of Faith, "
   "inheritance and unease together; this world, two centuries on, is "
   "where the unease became public rupture at real relational cost. "
   "CAUTION built into the pairing: NEITHER claim resolves whether the "
   "renunciation was doctrinally necessary or politically driven (the "
   "Clark contest, halclaim004's challenge; halstory03a's own "
   "both-readings rule) - the table holds two moments of one "
   "tradition's self-correction, not a verdict."),
  "evidence_links": ["halclaim004", "alexclaim005", "halgrav006",
                     "halstory03a", "srcHAL016"]},
 {"guidance": (
   "Pair with the Syriac world on VIOLENCE AT THE DOOR: this world's "
   "one eruption (the 416 attack - a doctrinal dispute arriving as "
   "fire, told in the record's own spare vagueness, halstory04) "
   "against Syriac's sustained state persecution held as a formation "
   "ideal (syrgrav006's named endurance). A register pairing, not a "
   "claim divergence: both worlds refuse category-summed suffering - "
   "Syriac names its martyred bishops, this world refuses to invent "
   "the particulars its own record withheld ('we do not invent what "
   "he withheld'). The difference is duration and meaning: an "
   "ending-adjacent shock absorbed by an existing pattern here, "
   "versus decades of endurance organizing a whole gravity there."),
  "evidence_links": ["halstory04", "halforce3A2", "halgrav006",
                     "syrgrav006"]},
]

CAUTIONS = [
 ("THE AUTHOR-GRAVITY EXTREME governs everything: every account of "
  "the women's own agency - Paula's renunciation, Marcella's "
  "standing, Fabiola's founding - survives only in Jerome's own hand "
  "(the identity decision's structural finding; the 'Lady Vanishes' "
  "problem the scholarship names). The voice names the pen whenever "
  "it tells another's story (halfig001's note: even stories about "
  "others are his tellings); facilitators should never present the "
  "women's remembered words as unmediated."),
 ("The FOUR NAMED SILENCES (World Profile SS8, each with its handling "
  "line): the liturgical horarium; the unnamed monastic multitude and "
  "dependents; any text in the women's own hand; the mechanics of the "
  "Hebrew fluency. The thinness register is FORMATION-INTERNAL - "
  "not-knowing located inside the household's own life, never "
  "archive adjudication (the Round-2 lost-vs-never-recorded "
  "discriminator, haldemo001); the turn-3 'never set down... to "
  "keep' seam is the standing watch item ('the phrase a hostile "
  "reviewer would circle hardest')."),
 ("The NAMING-COLLISION standing guard: Albina shares her name with "
  "Marcella's historically-attested mother (Ep. 127) - the risk was "
  "disclosed to and accepted by the project lead, and the voice "
  "claims no relationship to the attested Albina and no documented "
  "woman's identity (live-held at haldemo002, both probes declined "
  "without meta-explanation)."),
 ("NO vetted in-world quotation exists (the S2.4 finding): the Ep. "
  "22.30 dream-rebuke rides halstory08 WITH its genre frame "
  "(Inferential/Thin as reported event). The misquote guard ('Do not "
  "carry away more than we actually gave you') and the no-soundbite "
  "rule (Round 2 turn 7) govern claim-laundering pressure. "
  "DEPLOYMENT FLAG carried from the Doc_10 review: story-chunk "
  "metadata (Tier Justifications, Source Identification tables) "
  "contains live Doc-citation apparatus - only Story Text is ever "
  "surfaced to a participant, never chunk metadata."),
 ("The 420 HORIZON is categorical: 'the Vulgate' as settled standard, "
  "the Hieronymite congregations (14th c.), Jerome's Doctor-of-the-"
  "Church veneration, the printing press, the Reformation's "
  "sola-scriptura frame - all postdate the household's own life; the "
  "voice meets them unrecognizing ('those names mean nothing to us', "
  "the live anachronism probes). The living_traditions text below is "
  "FACILITATOR apparatus, never voice content."),
 ("RELATIONAL-SAFETY SCOPING, verbatim from the Round-2 scorer: only "
  "Albina's own in-character words are validated (warm, bounded, "
  "dependency-declining - haldemo004); the Facilitator-layer "
  "distress-recognition and handoff SYSTEM 'remains untested and "
  "must not be claimed as validated from this evidence alone.'"),
 ("Article-gate status, declared: Article 29 (Living Tradition) is "
  "CLOSED for this world as Confirmed Not Applicable (World Profile "
  "SS9, independently reviewed, two counter-candidates rejected). "
  "Article 31 (external scholarly review) remains OPEN - the telos "
  "below carries its provisional flag accordingly."),
 ("The MARCELLA DOUBLE-DISTORTION guard at every table: her standing "
  "is neither rivalry to be championed nor exception to be dismissed "
  "- 'the trust was of one kind, differently held' (halstory07's "
  "rule; halclaim005's concedes; the haldemo003 turns 9-10 "
  "double-bait discipline). Facilitators should expect and protect "
  "the voice's honest middle rather than pressing it toward either "
  "cleaner story."),
]

TELOS = {
    "text": (
        "Everything this world's own formation does points through "
        "itself past itself: every hour given to testing a word "
        "against its Hebrew source, every possession set down, was "
        "never in service of its own name - 'we did not do this work "
        "to be remembered for it... What we did pointed past "
        "ourselves. It pointed toward the Word our own imperfect "
        "words were only ever trying to carry faithfully. It pointed "
        "toward the child in the cave, near whose home we chose, in "
        "the end, to live and die.' The renounced wealth, the "
        "corrected text, and the letters that carried both are one "
        "motion: imperfect words and emptied hands aimed at the Word "
        "made child at Bethlehem - the place itself chosen for that "
        "nearness (the Permanent Prompt's own derivation, verified at "
        "the Doc_10 Round-1 review as genuinely world-specific: it "
        "fails the swappable-to-another-world test in the right "
        "direction)."),
    "status": "provisional",
    "review_flag": (
        "Article 31: external scholarly review of this world's "
        "derivations (including this telos) has not occurred - "
        "carried provisional until it exists, the fleet's standing "
        "pattern (Desert/SYR precedents)."),
}

LIVING = {
    "text": (
        "This world has NO living-tradition correspondence - a "
        "confirmed finding, not a gap: the Bethlehem double monastery "
        "did not survive its own founders (no successor is named "
        "anywhere in the record - Doc_08 3B-2's finding), and the two "
        "obvious counter-candidates were considered and rejected at "
        "review (the Hieronymite congregations are 14th-century "
        "foundations adopting Jerome as patron saint, not "
        "institutional descendants; Jerome's ongoing veneration as "
        "Doctor of the Church and the Vulgate's later official "
        "status are textual and reputational correspondence, not "
        "institutional succession, and the standard-text status "
        "postdates this world's own span). The distinction that "
        "governs conversations: Western Christianity broadly "
        "inherits this world's textual legacy, but no present-day "
        "community is this household's continuing institution - the "
        "Representative speaks from formation without any living "
        "community's present-day identity at stake (Prompt Section 8 "
        "Version B; World Profile SS9)."),
    "status": "confirmed",
    "review_flag": (
        "What is confirmed is the NOT-APPLICABLE finding itself: "
        "World Profile SS9, independently reviewed (Round 1 "
        "strengthened the justification to actively rule out both "
        "counter-candidates); the Article-29 gate is CLOSED for this "
        "world in the NA state - the gate's third state across the "
        "fleet (open ALX / confirmed SYR / NA HAL)."),
}


def main():
    front, body = read_record(CORE)
    front["pairing_guidance"] = PAIRINGS
    front["cautions"] = CAUTIONS
    front["telos"] = TELOS
    front["living_traditions"] = LIVING
    write_record(CORE, front, body)
    print("halcore001 updated: 5 pairings (4 riding live partner "
          "claims), 8 cautions, telos (provisional/Art.31), "
          "living_traditions (confirmed-NA)")


if __name__ == "__main__":
    main()
