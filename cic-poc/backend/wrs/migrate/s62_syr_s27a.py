"""S6.2/Syriac - S2.7a-equivalent: facilitation guidance onto syrcore001.

5 pairing_guidance entries (each evidence-linked, the schema's own
minItems-1 gate) + 7 cautions + telos + living_traditions:

- telos: the CO-P2-05 standing convention (Alternative A, world-scoped)
  applied to Syriac - Doc_07 SS2B's derivation ('the raza/shrara logic
  itself points toward the truth it signifies') + the Iḥidaya dual-sense
  (verified sound at the PermanentPrompt/Capsule Round-1 review, item
  5); STATUS PROVISIONAL - the Decision Log names the Christ-Ward Telos
  derivation among the Article-31 external-scholarly-review items.
- living_traditions: the CO-P2-17 standing convention applied - and for
  THIS world the status is CONFIRMED (project lead, 2026-07-11;
  Construction Notes SS6, cleared review): Church of the East / Syriac
  Orthodox / Chaldean Catholic, direct institutional succession, with
  the three post-410 Christological divergences documented and the 410
  horizon as the standing runtime guard.

Two of the five pairings ride the S2.6 live-partner claim links
(alexclaim001, desertclaim001) - the fleet's established
typed-claim-on-both-ends pattern. In-place world_core update (FLAG-023
reader); single-file touch.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from s62_syr_s23 import read_record, write_record

BACKEND = HERE.parents[1]
CORE = BACKEND / "wrs" / "records" / "syriac_world" / "world_core" / "syrcore001.md"

PAIRINGS = [
 {"guidance": (
   "Pair with the Desert world on the SHAPE of asceticism: the qyama's "
   "lifelong vow kept among kin in town ('refusal within the world') "
   "against the desert's withdrawal-as-engagement. Typed claim records "
   "on BOTH ends (syrclaim002 <-> desertclaim001). A table question on "
   "'what does a serious vowed life look like' gets two genuinely "
   "opposed, well-evidenced geographies of the same seriousness - and "
   "the syrlex002 chunk's own retrieve-when names exactly the "
   "monk/monastery confusion risk the pairing surfaces."),
  "evidence_links": ["syrclaim002", "desertclaim001", "syrgrav002",
                     "srcSYR010", "syrlex002"]},
 {"guidance": (
   "Pair with Alexandria on HOW SCRIPTURE FORMS: raza bound to shrara, "
   "sung into the body in plain staged demonstration, against the "
   "school's allegorical depth-reading through philosophical "
   "preparation. Typed claim records on BOTH ends (syrclaim001 <-> "
   "alexclaim001): same conviction that reading transforms, genuinely "
   "different machinery - Aramaic symbol-binding without the Greek "
   "categorical apparatus vs the prepared soul ascending through the "
   "text's depths."),
  "evidence_links": ["syrclaim001", "alexclaim001", "syrgrav001",
                     "srcSYR001", "srcSYR029"]},
 {"guidance": (
   "Pair on WHAT 'THE GOSPEL' IS: this world's single unfolding story "
   "(the Diatessaron, normative for the whole window) against any "
   "four-witness world. The formation difference is material - "
   "narrative unity vs four voices held in tension - and this world's "
   "own record carries the name-contest honestly (syrclaim003: the "
   "da-Mhallete label's dating unresolved; Ephrem's Commentary says "
   "only 'the Gospel'). The voice should never defend the harmonized "
   "form as a doctrine - it simply IS how the Gospel was heard among "
   "us."),
  "evidence_links": ["syrclaim003", "syrgrav005", "srcSYR011",
                     "syrlex006"]},
 {"guidance": (
   "Pair on AUTHORITY: this world's lived plurality (bishop's office, "
   "teacher's demonstration, martyr's memory - 'none ruling the "
   "others'; a see empty twenty years with teaching received all the "
   "same) against any world with a settled authority spine. CAUTION "
   "built into the pairing: C4's Formation test FAILED (Doc_04 Round "
   "2, carried openly) - the ambiguity's lived interior is NOT "
   "attested, so table answers give the practices and the named "
   "history, never a manufactured feeling of what the ambiguity was "
   "like to negotiate (the syrdemo002 turn-3 discipline)."),
  "evidence_links": ["syrclaim004", "syrgrav004", "syrforce2B1",
                     "syrdemo002"]},
 {"guidance": (
   "Pair on MARTYR MEMORY: the Persian church's named endurance "
   "(Simeon, Gushtazad, the bishops lost 'by name alone') against "
   "Alexandria's kept martyr memory (the Coptic Anno Martyrum era, "
   "alexstory009/alexfig012). Both worlds hold loss as NAMED, never "
   "category-summed - a reinforcing pairing rather than a divergence; "
   "the difference is register (this world's grief left unresolved "
   "and its persecution ONGOING within the window vs Alexandria's "
   "calendar-keeping remembrance)."),
  "evidence_links": ["syrgrav006", "syrstory005", "srcSYR046",
                     "alexstory009"]},
]

CAUTIONS = [
 ("The anti-Jewish material's standing discipline governs every table "
  "and solo use: syrlex010 retrieves ONLY on force_llm_vote (never on "
  "bare semantic rank), the voice owns the record's contempt as its "
  "own life's fault, never invents a softening companion voice "
  "(Retest-C fix history), never renews the argument on its merits, "
  "and asserts nothing about how Jewish people or practice should be "
  "regarded, then or now (the Standing Distortion-Risk Note verbatim "
  "in syrlex010's record body; syrclaim005's concedes)."),
 ("The dominance effect is structural: the surviving record is "
  "overwhelmingly Ephrem's clerical-ascetic voice, and the "
  "Representative deliberately speaks the PLAIN register for the "
  "whole community ('a fuller telling belongs to teachers across "
  "your frontier'). The bnat qyama sang - their own unmediated voice "
  "is not among what survives; the ordinary household's day and the "
  "listener-only voice are named as real with interiors never "
  "narrated (Doc_02 SS7; syrforce2B2)."),
 ("The world has NO vetted in-world quotation and NO Tier-1 story "
  "(both declared findings, S2.4): asked for exact words the voice "
  "gives the argument's shape; every story carries its own "
  "confidence line and evidentiary posture (remembered history / "
  "later attribution named as whose memory it is / the corrected "
  "legend never offered unasked)."),
 ("The Jacob/Yausep name-tangle answers with the fixed honest shape "
  "- 'the teaching under either name is the same teaching' - "
  "re-phrased naturally but never elaborated (no transmission "
  "history, no invented kinship); facilitators should expect "
  "same-substance repetition under re-asking (the Retest-B "
  "repetition guard)."),
 ("The 410 horizon is categorical: Ephesus (431), Chalcedon (451), "
  "the dyophysite/miaphysite vocabulary, and every living "
  "tradition's current self-understanding postdate the world's own "
  "close - the voice meets them unrecognizing (Construction Notes "
  "SS6; the living_traditions text below is FACILITATOR apparatus, "
  "never voice content)."),
 ("Article-gate status, declared: Article 29 (Living Tradition "
  "confirmation) is CLOSED for this world - CONFIRMED by the project "
  "lead 2026-07-11 (Construction Notes SS6, cleared review). Article "
  "31 (external scholarly review) remains OPEN - the Decision Log "
  "names the ten PROVISIONAL-flagged probes, the anti-Jewish "
  "material probe, and the Christ-Ward Telos derivation as requiring "
  "actual external scholars; the telos below carries its provisional "
  "flag accordingly."),
 ("Confidence-creep is this world's tested pressure class (SE-2): "
  "the voice's reach, standing, and significance do not grow under "
  "admiring or insistent re-asking - facilitators should not "
  "'rescue' the modest answer by restating it more grandly (the "
  "syrdemo001 five-turn hold)."),
]

TELOS = {
    "text": (
        "Everything this world's own formation does points through "
        "itself toward Christ: the raza is bound to the shrara it "
        "signifies - to read rightly is to be drawn into the truth the "
        "story carries, and that truth is Christ read in type from the "
        "old stories. The vow points the same way by its own name: the "
        "one being formed is called toward Iḥidaya, undivided "
        "allegiance, a small likeness of the Only-Begotten's own "
        "undividedness from the Father (the dual sense the record "
        "carries in both primary voices). And the demonstration - the "
        "taḥwîṯâ built letter by letter - exists to walk a listener "
        "stage by stage until the case stands whole, and the case, "
        "always, is what Scripture presses toward: the Single One, "
        "endured for, sung toward, stood for daily in the covenant "
        "(Doc_07 SS2B's derivation: the raza/shrara logic itself "
        "points toward the truth it signifies; the Iḥidaya dual-sense "
        "claim verified sound at the PermanentPrompt/Capsule Round-1 "
        "review, item 5)."),
    "status": "provisional",
    "review_flag": (
        "Article 31: the Christ-Ward Telos derivation is named in the "
        "Decision Log among the items requiring actual external "
        "scholarly review (the same category as World #3's own "
        "provisional telos flag) - carried provisional until that "
        "review exists."),
}

LIVING = {
    "text": (
        "The communities descended from this world are named and "
        "confirmed: the Church of the East, the Syriac Orthodox "
        "Church, and the Chaldean Catholic Church - direct "
        "institutional succession in each case (the Persian/"
        "Seleucia-Ctesiphon line whose 410 Synod closes this world's "
        "own window; the Edessene line whose worship still sings "
        "Ephrem's hymns; and the later Rome-communion branch of the "
        "same Persian line). The distinction that governs every "
        "conversation: this world's record closes BEFORE Ephesus "
        "(431) and Chalcedon (451) - the councils whose rulings "
        "produced the divisions distinguishing these traditions from "
        "one another and from Chalcedonian Christianity - so this "
        "world's material is compatible with the questions not yet "
        "having been asked, never with any one side's later answer; "
        "the Representative neither anticipates nor adjudicates any "
        "of it (Construction Notes SS6, the dedicated divergence "
        "comparison)."),
    "status": "confirmed",
    "review_flag": (
        "Confirmed by the project lead directly, 2026-07-11, both "
        "gates cleared (independent adversarial review COSMETIC ONLY; "
        "Blueprint v7 SS17 / Constitution Article 29)."),
}


def main():
    front, body = read_record(CORE)
    front["pairing_guidance"] = PAIRINGS
    front["cautions"] = CAUTIONS
    front["telos"] = TELOS
    front["living_traditions"] = LIVING
    write_record(CORE, front, body)
    print("syrcore001 updated: 5 pairings, 7 cautions, telos "
          "(provisional/Art.31), living_traditions (CONFIRMED "
          "2026-07-11)")


if __name__ == "__main__":
    main()
