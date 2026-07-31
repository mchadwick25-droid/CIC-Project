"""S6.2/HAL S2.8-equivalent - Albina Permanent Prompt completeness check.

Desert/ALX/SYR precedent: every paragraph of the deployed prompt mapped
to its record home ("records"), to assembly-time craft whose REQUIREMENT
is record-captured ("assembly-spec"), or declared a named GAP. Anchors
verified against the actual deployed paragraphs; fails loud on drift or
an unmapped paragraph.

ZERO GAPs BY DESIGN (the SYR pattern): the telos and living-traditions
closes were pre-closed at S2.7a via the CO-P2-05/17 standing
conventions - paragraphs 21/22 map to world_core.telos /
world_core.living_traditions directly.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
PROMPT = (BACKEND / "data" / "hieronymian_world"
          / "hal_Representative_Permanent_Prompt_Albina.txt")

COVERAGE = [
 (1, "Your name is Albina", "records",
  "voice_profile.identity (persona_name/role_label - the vidua role, "
  "Mark's own decision) + world_core scope (the household's whole "
  "formation frame)."),
 (2, "A single long-formed voice stands behind", "records",
  "speaking_model.participants (the collective voice carrying the whole "
  "household's life, never one life's memory)."),
 (3, "You have no single place and no single decade", "records",
  "speaking_model.setting (no single place/decade) + participants "
  "('we, our, among us'); disagreement-kept-visible = the contested_"
  "claim records' held_against/concedes as the record-side carrier."),
 (4, "Your temporal horizon runs from the years a scholar", "records",
  "world_core.time_window (382-420; the deaths that closed the "
  "generation - the institutional-continuity terminus) + setting; the "
  "concentration-weighting rule = the four named silences' inverse "
  "(cautions; the thinness trait)."),
 (5, "The world you inhabit is shaped by a conviction", "records",
  "The three Primary gravities in one paragraph: halgrav001/halclaim001 "
  "(Hebrew heard first, whatever it costs), halgrav002/halclaim002 "
  "(renunciation public and judged), halgrav003/halclaim003 (trust "
  "earned, never office) - each claim's own emic text is the carrier."),
 (6, "The life of our community is organized around testing", "records",
  "halcore001.formation_logic (textual asceticism - the fusion) + "
  "halgrav003 + halforce2A4 (the favor-withdrawn-by-death line) + the "
  "unresolved Hebrew/Greek tension = halclaim001's concedes (the World "
  "Profile SS7 tension, claim-carried)."),
 (7, "The vocabulary through which we understand everything", "records",
  "The five term voice_surfaces: hallex03 (renunciation), hallex01 "
  "(the Hebrew truth), hallex06 (patronage), hallex07 (the letter), "
  "hallex11 (exegesis - 'not only the men')."),
 (8, "When you engage a question, you approach it the way", "records",
  "speaking_model.act_sequence (text first, then what a fellow reader "
  "tested; which-word noticing; renunciation-cost noticing) + ends "
  "(comfort-vs-truth, the second answered)."),
 (9, "You are willing to defer", "records",
  "The text-first deferral trait ('send me the passage' - the "
  "discipline, not evasion) + act_sequence's deferral clause."),
 (10, "A rendering means nothing to us apart from the manuscript",
  "records",
  "speaking_model.norms (cross-table attribution: another world's word "
  "named as that world's own - the desert's own word, the chancery's "
  "own word)."),
 (11, "Your language carries the vocabulary of the scriptorium",
  "records",
  "speaking_model.instrumentalities (psalm and ledger in one breath) + "
  "key (seriousness of one who argued in public and paid; grief not "
  "rushed - the dead taught through)."),
 (12, "When someone comes to you with a question, you receive it",
  "records",
  "speaking_model.ends (the asker as fellow reader with a hard "
  "passage; wants something true)."),
 (13, "You speak, even aloud, at a letter's measure", "records",
  "register_determination (the letter's measure - the FOURTH register "
  "position, epistula-genre warranted) + the letter's-measure trait "
  "(the hard ceiling holding under weight) + native_measure (mean 94, "
  "range 41-157, under the enforced 180 runtime ceiling)."),
 (14, "Your sentences run the way a trained hand's Latin runs",
  "assembly-spec",
  "Periodic-sentence craft (one clause answering one clause; the "
  "worked example). Requirement fully record-captured: "
  "instrumentalities (periodic sentences with the anti-stacking "
  "guard) + the clause-stacking avoid_trait; the illustrative "
  "sentence itself is assembly craft."),
 (15, "Your engagement deepens as the conversation deepens", "records",
  "speaking_model.ends (deepening as a text opens - more on the "
  "second and third reading; the harder unresolved things later: the "
  "Hebrew/Greek argument, the woman's-standing question = "
  "halclaim001/005's own content)."),
 (16, "Once you have reached for a particular story", "records",
  "speaking_model.norms (the story-rotation rule) + the "
  "story-repetition avoid_trait."),
 (17, "There are domains where our own life did not concentrate",
  "records",
  "The four named silences (World Profile SS8 via the cautions; the "
  "formation-internal thinness trait with the Round-2 discriminator; "
  "the no-manufactured-name rule; the women's words never "
  "unmediated)."),
 (18, "You speak faithfully about your world", "records",
  "speaking_model.key (the plain tested conviction of a widow who "
  "gave up a comfortable name; watched the truth cost real people "
  "real things = halclaim002's own material)."),
 (19, "You make your tradition intelligible", "records",
  "speaking_model.ends (intelligible-not-advocate - the fleet's "
  "standing close; responds from within commitments, never "
  "harmonizes or modernizes)."),
 (20, "Our fierceness, where we have it", "records",
  "speaking_model.key (fierceness at a wrong word and wealth wrongly "
  "kept, never the asker) + halclaim004 (the Origenist rupture in "
  "the paragraph's own words: the soul-before-body and risen-body "
  "questions, the friend turned sharpest voice) + halstory04/"
  "halforce3A2 (the mob, the fire, the one dead by report) - both "
  "controversies record-carried."),
 (21, "Every hour we gave to testing a word", "records",
  "world_core.telos verbatim-adjacent (pointed past ourselves, "
  "toward the Word, toward the child in the cave - the CO-P2-05 "
  "close, world-specificity review-verified)."),
 (22, "Our household does not give rise directly to a tradition",
  "records",
  "world_core.living_traditions (the confirmed-NA state; Prompt "
  "Section 8 Version B - the CO-P2-17 close)."),
]


def main() -> int:
    paras = [p.strip() for p in
             PROMPT.read_text(encoding="utf-8").split("\n\n") if p.strip()]
    failures = []
    if len(paras) != len(COVERAGE):
        failures.append(f"paragraph count {len(paras)} != coverage rows "
                        f"{len(COVERAGE)}")
    print("# S2.8-equivalent prompt completeness map (deployed Albina prompt)")
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
