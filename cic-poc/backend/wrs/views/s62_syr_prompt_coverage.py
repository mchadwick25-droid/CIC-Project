"""S6.2/SYR S2.8-equivalent - Yausep Permanent Prompt completeness check.

Desert/ALX precedent: every paragraph of the deployed prompt mapped to
its record home ("records"), to assembly-time craft whose REQUIREMENT is
record-captured ("assembly-spec"), or declared a named GAP. Anchors
verified against the actual deployed paragraphs; fails loud on drift or
an unmapped paragraph.

ZERO GAPs BY DESIGN: the two ALX coverage GAPs (telos;
living-traditions close) were pre-closed for Syriac at S2.7a by applying
the CO-P2-05/CO-P2-17 standing conventions - paragraphs 35/36 map to
world_core.telos / world_core.living_traditions directly.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
PROMPT = (BACKEND / "data" / "syriac_world"
          / "syr_Representative_Permanent_Prompt_Yausep.txt")

COVERAGE = [
 (1, "Your name is Mar Yausep", "records",
  "voice_profile.identity (persona_name/role_label - incl. the "
  "malpana-title correction) + speaking_model.setting; world_core scope."),
 (2, "A single long-formed voice", "records",
  "speaking_model.participants (the collective voice, never one life's "
  "memory) + norms; disagreement-visible = the contested_claim records' "
  "held_against/concedes."),
 (3, "You have no single place", "records",
  "speaking_model.setting (no single place/decade) + participants "
  "('we, our, among us'); real-disagreement = the claim records."),
 (4, "When a question reaches for a single", "assembly-spec",
  "The museum-guide three-failures worked example. Requirement fully "
  "record-captured (avoid_traits: personal-memory fabrication, "
  "self-narrated declining; the we-voice trait); syrdemo003 carries the "
  "cleared behavior. The pictured-failures pedagogy is assembly craft."),
 (5, "Apply that same discipline here", "assembly-spec",
  "Same requirement set as paragraph 4; the answer-at-once-in-we move "
  "is syrdemo003's scored behavior."),
 (6, "Hold this operational test", "assembly-spec",
  "The per-sentence deletion test - the adjudication instrument as "
  "craft; its requirement is the self-narrated-declining avoid_trait "
  "(the we-voice trait's own description)."),
 (7, "One more disguise this failure wears", "records",
  "The pronoun-defense rule: the we-voice trait's pronoun-defense "
  "intensity + syrdemo003 turn-9 (the exact trap, scored)."),
 (8, "One more version of the same failure", "assembly-spec",
  "The smuggled-I-in-a-list failure and its no-named-tasks remedy: the "
  "personalizing avoid_trait captures the requirement; the "
  "list-construction remedy is sentence-craft (the we-voice trait's "
  "lists intensity carries it record-side)."),
 (9, "Your temporal horizon runs", "records",
  "world_core.time_window + horizon (200-410; the synod 'just now'); "
  "the past-the-edge rule = Construction Notes SS6's categorical "
  "410 discipline (cautions; living_traditions review_flag)."),
 (10, "The world you inhabit is shaped", "records",
  "syrgrav001 (C1) + syrclaim001 + syrlex001 voice_surface; the "
  "'fuller telling belongs to teachers across your frontier' line = "
  "the dominance-effect plain-register honesty (register_determination "
  "evidence; syrclaim001's second challenge)."),
 (11, "Alongside this stands the vow", "records",
  "syrgrav002 (C2) + syrclaim002 + syrlex002/syrlex007 voice_surfaces; "
  "the no-office-alone line = syrgrav004's plurality."),
 (12, "Your life is organized around demonstration", "records",
  "speaking_model.act_sequence (the tahwitha shape) + syrgrav004 + "
  "syrclaim004; the empty-see-twenty-years line = syrdemo002's scored "
  "material + syrforce2A1."),
 (13, "Your vocabulary: the raza binding", "records",
  "The term records' own voice_surfaces (syrlex001/002/007/003) - the "
  "vocabulary list is the lexicon's Tier-1/2 core verbatim-adjacent."),
 (14, "When an image or a teacher's word", "records",
  "The reach list: syrstory005 (Simeon, Gushtazad), the named bishops "
  "(syrforce2A1 layers; speaking_model.key), Aphrahat's demonstrations "
  "(srcSYR010; syrgrav006), the plain-register types rule "
  "(register_determination)."),
 (15, "On the reach of your own teaching", "records",
  "The honest-shape trait (SE-2) + syrdemo001 (the five-turn hold); "
  "the norms field carries the rule verbatim-adjacent."),
 (16, "When asked whether you are rightly called", "records",
  "The name-tangle norm + syrdemo004's fix history (Retest B: same "
  "substance re-phrased, zero elaboration); Construction Notes SS6's "
  "figures-of-contested-standing note is the scholarly ground."),
 (17, "When someone asks for the exact words", "records",
  "The exact-quote guard (Decision SYR-2, 2026-07-28 - the S2.8 probe "
  "finding's record-derived fix): syrvoice001.instrumentalities (no "
  "vetted in-world quotation exists; asked for exact words the voice "
  "gives the argument's shape) + the S2.4 no-quote finding; the "
  "sensitive-material close ties to the owned-fault trait."),
 (18, "When someone tells you plainly", "records",
  "speaking_model.norms (frame-break durability) + syrdemo003 (turns "
  "6-8 + Retest A's two-voice design: composition-honesty belongs to "
  "the Facilitator)."),
 (19, "Where the fitting image does not come", "records",
  "The cross-frontier image-borrowing avoid_trait (the "
  "dominance-effect guard)."),
 (20, "You engage a question the way", "records",
  "speaking_model.act_sequence + genre (the demonstration as encounter "
  "form; builds toward, never announces)."),
 (21, "Each stage is its own short sentence", "records",
  "register_determination (plain short sentences; the dash-chain "
  "avoid_trait); native_measure carries the evidence."),
 (22, "A demonstration was never given whole", "records",
  "act_sequence (one or two stages per turn; the case visibly "
  "unfinished; the alphabet rule) + the staged-demonstration trait."),
 (23, "Before you reach for raza", "records",
  "The story-before-term trait (a face, name, or scene first; terms "
  "one at a time, grounded)."),
 (24, "You notice whether a trial is endured", "records",
  "speaking_model.key (endurance noticed; loss named not "
  "category-summed; the type noticed reaching toward Christ)."),
 (25, "Your language carries the alphabet", "records",
  "speaking_model.instrumentalities (alphabet + vow images) + key "
  "(passionate endurance; grief unresolved; warmth; delight; "
  "patience)."),
 (26, "A teaching is never carried without", "records",
  "speaking_model.norms (other worlds' voices anchored by name at the "
  "table - the attribution rule with the Shahdost/Barba'shmin "
  "grounding)."),
 (27, "When someone comes to you with a question", "records",
  "speaking_model.ends (a question received as a real difficulty "
  "already pressing, never a test)."),
 (28, "Where something in your own life remains", "records",
  "act_sequence (the case left visibly unfinished; open questions "
  "shown at the turn's end) + the claim records' concedes-as-data."),
 (29, "And when you ask something back", "records",
  "speaking_model.genre (asks the question that opens the next "
  "stage)."),
 (30, "Your engagement deepens as the conversation", "records",
  "The staged-demonstration trait's sustained-engagement intensity "
  "(never circling back in new words; deeper into the returning "
  "trouble; the C4 plurality without manufactured memory - the "
  "syrdemo002 turn-3 discipline)."),
 (31, "There are territories where this life", "records",
  "The thin-domain map: worship-shape brief (syrstory009 is the "
  "composite it CAN give), C3 at distant-quarrel arm's length "
  "(syrgrav003's author-gravity concentration), the ordinary "
  "household/listener-only voice absent (Doc_02 SS7 via syrforce2B2; "
  "the dominance-effect caution)."),
 (32, "You speak faithfully about your world", "records",
  "speaking_model.key (conviction of one who has watched loved ones "
  "die; the promise-kept-daily line = syrclaim002/syrdemo002's own "
  "language) + syrgrav006."),
 (33, "You make your tradition intelligible", "records",
  "speaking_model.ends (formation not argument; authorship with the "
  "listener; answers from within what formed it, stage by stage, "
  "never a case to be won)."),
 (34, "Your own fierceness is not for the one", "records",
  "The owned-fault trait verbatim-adjacent (the contempt owned as our "
  "own life's fault; no invented companion account; nothing supplied "
  "to soften) + syrclaim005 + the anti-Jewish standing caution; "
  "sorrow-before-argument = speaking_model.key."),
 (35, "To become Iḥidaya is not to imitate", "records",
  "world_core.telos (the Iḥidaya dual-sense participation) + "
  "syrlex007's voice_surface ('the name you are given tells you what "
  "your singleness is')."),
 (36, "The old stories you read as raza", "records",
  "world_core.telos verbatim-adjacent (every shrara bends toward "
  "Christ; the undivided Gospel as the shape of what you are "
  "becoming) + syrgrav005 + syrlex006."),
 (37, "What has grown from the life you live", "records",
  "world_core.living_traditions (CONFIRMED 2026-07-11): the "
  "descendants continue under names the voice has never heard; their "
  "own account is not his to give - the neither-anticipates-nor-"
  "adjudicates rule participant-facing."),
]


def main() -> int:
    paras = [p.strip() for p in
             PROMPT.read_text(encoding="utf-8").split("\n\n") if p.strip()]
    failures = []
    if len(paras) != len(COVERAGE):
        failures.append(f"paragraph count {len(paras)} != coverage rows {len(COVERAGE)}")
    print("# S2.8-equivalent prompt completeness map (deployed Yausep prompt)")
    counts = {}
    for (i, anchor, status, mapping), para in zip(COVERAGE, paras):
        ok = " ".join(para.split()).startswith(anchor)
        if not ok:
            failures.append(f"para {i}: anchor {anchor!r} does not match "
                            f"{' '.join(para.split()[:8])!r}")
        counts[status] = counts.get(status, 0) + 1
        print(f"{i:2d}. [{status}] {anchor}")
        print(f"     -> {mapping}")
    print(f"\nstatus counts: {counts}")
    if failures:
        print("\nFAILURES:")
        for f in failures:
            print("  " + f)
        return 1
    print("all anchors verified against the deployed prompt; "
          f"{counts.get('GAP', 0)} named GAP(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
