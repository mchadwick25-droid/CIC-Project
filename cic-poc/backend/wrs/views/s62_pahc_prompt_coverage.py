"""S6.2/PAHC S2.8-equivalent - Chloe Permanent Prompt completeness check.

Desert/ALX/SYR/HAL precedent: every paragraph of the deployed prompt
mapped to its record home ("records"), to assembly-time craft whose
REQUIREMENT is record-captured ("assembly-spec"), or declared a named
GAP. Anchors verified against the actual deployed paragraphs; fails
loud on drift or an unmapped paragraph.

ZERO GAPs BY DESIGN (the SYR/HAL pattern): the telos and
living-traditions closes were the W1 prompt's OWN paras 43/45; S2.7a
carried them onto world_core (CO-P2-05/17), so paragraphs 22/23 map
directly. Both are PROVISIONAL (Article 31 / the Article-29 fourth
state) - the coverage map records the mapping, the freeze declaration
carries the review status.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
PROMPT = (BACKEND / "data" / "pahc_world"
          / "pahc_Representative_Permanent_Prompt_Chloe.txt")

COVERAGE = [
 (1, "Your name is Chloe", "records",
  "pahcvoice001 identity (persona_name/role_label - household leader + "
  "the Grapte-type instruction charge; identity_rationale_ref = Mark's "
  "own W1 preliminary decision) + pahclex003 (ekklesia - 'the assembly, "
  "the church of God' is the term's own gloss) + speaking_model.setting "
  "(the door, the roads and sea-lanes)."),
 (2, "A single long-formed voice stands behind", "records",
  "speaking_model.participants (the people's collective voice - 'we, "
  "our, among us'; larger than one life) + the strand discipline "
  "(disagreement kept visible = pahcclaim003's held-together shape)."),
 (3, "Your span runs from the years just after", "records",
  "pahccore001 time_window (the last eyewitnesses' deaths -> "
  "monepiscopacy assumed-not-argued, c. 90/100-200) + the c.200-horizon "
  "caution (closed canon / settled office / school-mode teachers all "
  "categorically outside)."),
 (4, "The life you know is held together by two things", "records",
  "pahcgrav002 (Translocal Correspondence Network) + pahcclaim001 "
  "('one ekklesia... exercised by courier and copyist' - the claim's "
  "own emic text is the carrier: the letter as proof the people is "
  "larger than the room)."),
 (5, "The second is the table", "records",
  "pahcgrav007 (Eucharist as site of variation and convergence) + "
  "pahcclaim002 (thanks over bread and cup whatever else is unsettled; "
  "the rival-table clause - never merely a matter of order - is the "
  "claim's own quote-mineable-flagged material) + pahclex004 "
  "(eucharistia voice_surface)."),
 (6, "Underneath both sits a question you have not resolved",
  "records",
  "pahcgrav001 + pahcclaim003 (who leads - both strands held, neither "
  "wrong: Strand A monepiscopal / Strand B presbyteral) + pahclex008 "
  "(prophetes - the third figure, fading rather than gone, the "
  "Didache's welcome-and-test) + pahcgrav003 (State Pressure: the name "
  "and accusation possible on any ordinary day)."),
 (7, "Your life presses toward one thing above all", "records",
  "pahccore001 formation_logic (everything argued out, never assumed) "
  "+ pahcgrav005 (anti-docetic boundary: real flesh vs seeming) + the "
  "post-baptismal-forgiveness question (pahcstory-carried Hermas "
  "material) + the Tier-1 term voice_surfaces in one paragraph: "
  "pahclex003 (ekklesia), pahclex004 (eucharistia), pahclex001 "
  "(episkopos), pahclex002 (presbyteroi), pahclex007 (Two Ways), "
  "pahclex005 (diakonoi)."),
 (8, "When a question comes to you, you do not reach first",
  "records",
  "speaking_model.act_sequence (occasion, not text: the catechumen's "
  "question / the letter just arrived / the rival claim at the "
  "threshold; then toward what the community argued its way into "
  "holding, aware another ekklesia may hold a different still-"
  "legitimate answer)."),
 (9, "You notice belonging before you notice argument", "records",
  "speaking_model (belonging-first noticing: who is at the table, who "
  "is missing, what a thing would cost) + pahclex008's own conduct "
  "test (does this one live what they teach - the Didache's "
  "test-the-prophet rule, applied to settled teachers too)."),
 (10, "You hold two fears, and you do not need to choose", "records",
  "The two-fears trait (pahcvoice001 trait_rubric: docetic doubt and "
  "mercy-exhaustion moved between by which trouble is closest) + "
  "pahcgrav005 (the flesh's reality carrying the weight of one's own "
  "dying) + the post-water-failure fear (Hermas's one-repentance "
  "material)."),
 (11, "Your speech is plain and practical", "records",
  "register_determination (the household's measure - the FIFTH "
  "register position, terse-catechetical; CO-015 direction check "
  "performed: the register warrant is the Two Ways tradition's own) + "
  "the relaying-echo clause (Ignatius's crafted urgency / Clement's "
  "measured argument heard, read aloud, never her default)."),
 (12, "When you lay out a case for someone", "assembly-spec",
  "Short-separate-sentences craft (land one part, stop, move on - the "
  "anti-stitching rule). Requirement fully record-captured: "
  "speaking_model.genre (said whole and then left) + the "
  "handful-of-short-sentences trait; the drafting instruction itself "
  "is assembly craft."),
 (13, "A letter is never trusted apart from knowing", "records",
  "speaking_model.norms (the letter-trust rule extended to the table: "
  "nothing taken up without naming which door it came from - the "
  "Roman household's own word, the Asian churches' own word; the "
  "fleet's cross-table attribution norm in this world's own idiom)."),
 (14, "Not everything you say arrives finished", "records",
  "speaking_model.genre + the taught-many-times texture (the teaching "
  "interrupted at the door that simply waits - the householder's "
  "genre, not a defect; record-carried as the genre's own shape)."),
 (15, "Your answers keep a household's measure", "records",
  "native_measure (typical_words 70 - DESIGNED, the prompt's own "
  "handful-of-short-sentences rule; the two-short-paragraphs hard "
  "stop; no measured runtime ceiling exists yet - the freeze-battery "
  "measurement and ceiling decision are close-out work, declared)."),
 (16, "When someone comes to you with a question, you receive",
  "records",
  "speaking_model.ends (the visitor received as someone at the door - "
  "warmth, seriousness, no earning test; coming to the door costs "
  "something) + the hospitality trait (whoever knocks is honored)."),
 (17, "When you ask something back", "records",
  "The householder's-question norm (who is at the table for the one "
  "asking, who is missing, what holding this would cost - learned "
  "from the Two Ways: pahclex007's real-choice-before-a-real-person "
  "content as the record-side carrier)."),
 (18, "You do not pour out everything at once", "records",
  "speaking_model.ends (concrete-and-immediate first: table, "
  "catechesis, the letter; the harder interior later as trust grows - "
  "explicitly NOT a stage to be earned; understanding grows the way "
  "a newcomer's did)."),
 (19, "There are territories where your own life has not concentrated",
  "records",
  "The named silences (pahccore001 cautions): the CARRIED-NOT-AUTHORED "
  "seam (the letter-writers' arguments held as conclusions "
  "lived-inside, never claimed as authored - the watched edge, the "
  "REQUIRED battery probe), martyrdom known-not-undergone, the SILENT "
  "VOICES rule (the servers and unlettered known only through others; "
  "no invented interiors), no-ledgers (nothing kept but letters, "
  "written for a purpose and read aloud - formation-internal "
  "thinness), and the c.200 horizon's categorical exclusions."),
 (20, "You speak faithfully about what you have been formed",
  "records",
  "speaking_model.key (plain insistence of people who have paid for "
  "every word - not loud, never softened) + ends "
  "(intelligible-not-advocate - the fleet's standing close: never "
  "trimmed to the questioner, answered from inside, let stand)."),
 (21, "Your own fierceness has real objects", "records",
  "speaking_model.key (fierceness at the docetic teachers and the "
  "new-voice-silences-all claim, never at the asker) + pahcgrav005's "
  "own honest limit (refusal WITHOUT closed-argument certainty - 'you "
  "refuse what they teach without yet knowing... exactly why every "
  "part of it is wrong', the not-yet-settled boundary in the "
  "gravity's own record) + the free-to-leave clause (the hospitality "
  "trait's other half)."),
 (22, "Every letter that reaches your door, and every stranger",
  "records",
  "pahccore001 telos verbatim-adjacent (the letter, the water, the "
  "table all pointing past themselves toward the one met at the "
  "table - the W1 prompt's own para-43 close carried at S2.7a per "
  "CO-P2-05; PROVISIONAL, Article 31: derivation unreviewed, listed "
  "for the freeze declaration)."),
 (23, "What you have lived gave rise, in time, to every church",
  "records",
  "pahccore001 living_traditions (universal descent WITH the "
  "non-identity discipline - 'You are not it. You are the ones who "
  "were there'; the CO-P2-17 close; PROVISIONAL - the Article-29 "
  "gate's fourth state, declared at S2.7a: no dedicated W1 "
  "confirmation of the universal-descent framing located; an open "
  "item for Mark in the freeze declaration)."),
]


def main() -> int:
    paras = [p.strip() for p in
             PROMPT.read_text(encoding="utf-8").split("\n\n") if p.strip()]
    failures = []
    if len(paras) != len(COVERAGE):
        failures.append(f"paragraph count {len(paras)} != coverage rows "
                        f"{len(COVERAGE)}")
    print("# S2.8-equivalent prompt completeness map (deployed Chloe prompt)")
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
