# Acclamation Force: Readability Rewrite Review (2026-10-25)

- **Record:** `records/lpc/force/lpc.force.congregational-acclamation-overriding-preference.md`, field `description`
- **Generator:** `Build/worlds/lpc/scripts/wb_lpc_s25.py`, `build_forces()`, the F1B2 `emit_force` call
- **Branch:** `claude/lpc-acclamation-readability-2026-10-25`, uncommitted diff against `0a0290ec`
- **Scope:** Decision 8B readability rewrite of the first two paragraphs only. Paragraphs 3 to 5 are unchanged.
- **Reviewer:** independent adversarial review, Opus. No model API called.

## What was checked

1. **Facts against the vendored sources.**
   - Cyprian, Ep. XXXIX, `cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml`. Lines 32369-32373 give "malignity and treachery of certain of the presbyters" and "that ancient venom against my episcopate, that is, against your suffrage and God's judgment". Line 32403 gives "Those five presbyters".
   - Pontius, Life of Cyprian §5, lines 27817-27821: "by the judgment of God and the favour of the people, he was chosen to the office of the priesthood and the degree of the episcopate while still a neophyte". Line 27844 adds "Some resisted him".
   - Possidius, Vita IV, `cic/texts/possidius_vita-augustini_weiskotten1919.txt` lines 1803-1820. Valerius "was bishop in the Catholic church at Hippo". Augustine was seized "while he wept freely".
   - Possidius, Vita VIII, lines 2124-2143. The announcement was made "to the bishops who happened at that time to be present, and to all the clergy of Hippo and to all the people". All who heard "rejoiced and clamored" for it. He refused "since his bishop was still living". Examples were brought "from the churches across the sea as well as in Africa". He yielded "under compulsion and constraint" (Latin: *compulsus atque coactus succubuit*).
   - Timing comes from `records/lpc/figure/lpc.figure.cyprian.md`: converted c. 246; elected "between roughly July 248 and April 249". The world core gives "c. 246-249". "Roughly two or three years later" is supported.
   - "Valerius, the bishop of Hippo" is confirmed by Vita IV, and by Vita VIII's "the bishop Valerius".
   - "Five presbyters are recorded as opposing him" is unchanged from the old text, and matches the figure and world-core records. It rests on Ep. XXXIX's "five presbyters" joined to the "ancient venom against my episcopate". The rewrite did not introduce it.
2. **Nothing added, dropped or softened.** Each clause of the old paragraphs 1 and 2 was compared with the new text. Every claim survives, including "roughly", the episcopate = suffrage + God's judgment link, the 391 seizure, the three audiences, the refusal, both sets of examples, and the compelled yielding. "Certain presbyters" replaces "a faction's", which is closer to Cyprian's own words. "The same way" (Pontius) is a fair comparison, since both name God's judgment and the people's part.
3. **Writing bar** (`engine/m7/turn_readability.py (score_turn)`, whole field):
   - The old field scored FK 8.9 and FRE 54.7, and failed.
   - The new field scores FK 7.5 and FRE 64.6, and passes. It is flagged `below_floor` because FK is under 8.
   - Rewritten paragraph 1 scores FK 6.3 and FRE 73.5. Rewritten paragraph 2 scores FK 7.9 and FRE 63.1.
   - The longest sentence has 24 words.
   - No AI tells were found.
4. **Hidden quotations.** No run of source words is used verbatim at a length that hides a quotation. The longest shared runs are short, common phrases: "God's judgment", "all the people" and "the bishops present". "Compelled and constrained" renders *compulsus atque coactus* in different English from the ANF. All three quotations now sit only in `manifestations` and `sources.locus`, where they remain quoted.
5. **Generator parity.** The string literal in `wb_lpc_s25.py` is identical to the record's parsed `description`. The YAML moved from a `>-` block to a single-quoted scalar. That is a serializer choice with no effect on content.

## Findings

| # | Grade | Finding | Recommendation |
|---|---|---|---|
| 1 | P2 | Paragraph 2 calls the source "Possidius's Life, chapter VIII". Paragraph 3 (unchanged) calls it "Possidius's Vita, chapters IV and VIII". One field now names the same work two ways. | Use one name in both places. "Life" fits the reading bar, but paragraph 3 is out of scope, so either revert to "Vita" in paragraph 2 or note it for the next pass. |
| 2 | P2 | "Ancient venom" became "old hatred". The fact is kept, but the source's own image, poison, is lost. The world-voice standard asks that distinctive imagery survive. | Optional: use "old poison" or "old venom". Neither should move the score much. |
| 3 | P2 | "Trained rhetorician" became "trained public speaker". A rhetor was a professional teacher and orator of rhetoric. "Public speaker" is slightly narrower. The figure record still says "trained rhetorician". | Optional: use "trained teacher of public speaking", or accept as is. |
| 4 | P2 | The whole field scores FK 7.5, under the grade-8 floor. This is reported, not a failure, and CLAUDE.md says too simple is not the risk. Paragraph 1 alone scores FK 6.3. | No change required. If finding 2 or 3 is taken, the field gains a little grade. |
| 5 | P2 (note, out of scope) | Unchanged paragraphs 3 and 5 still score FRE 52.9 and 39.5 on their own. Only the whole field is gated, and it passes. | No action in this change. Log it if paragraph-level scoring is ever applied to records. |

There are no P1 findings. Every fact checks out against the vendored text. Nothing was added, dropped or softened. The field passes the gate.

## Verdict

**Approved to proceed.** All findings are P2. Findings 1 to 3 are optional wording improvements and do not block this change.
