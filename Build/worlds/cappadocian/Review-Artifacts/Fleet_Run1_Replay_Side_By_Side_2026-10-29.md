# cappadocian: fleet graded run 1, six-question replay, side by side (29 October)

## Scope

- **New answers.** `engine/m3/reports/fleet-graded-run-1/replay/cappadocian.json`. Live test "fleet graded run 1", package `packages/cappadocian/2026-10-28T03-49-28Z`, which is the registry pin. Voice: Sonnet 4.5. Safety and reader calls: Haiku 4.5. It is one conversation of six questions.
- **Older answers.** `engine/m4/reports/live-turn-report-cappadocian-2026-10-13-eleven-world-test.json` (13 October eleven-world test). That is older data, from a different format and engine. It is read for comparison only and is not scored.
- **Method.** The same method as `Build/worlds/lpc/Review-Artifacts/Run3_Access_And_Craft_Review_2026-10-28.md` and the rubric in `Build/worlds/lpc/build/lpc_Probe_Results.md`. There are four criteria: Rigor, Accessibility, Craft and Focus. P1 is wrong, invented, misleading or damaged, and it makes the row FAIL. P2 is small and fixable, and a row with only P2s is PASS with that criterion graded `concern`. Each fix is at the source: a record, a caution or an engine item.
- **Checked.** For each turn: the shipped text, citations, `reply_shape` (placed and removed), grounding verdicts, `output_defects`, `figures_used` and `answer_record_fallback`. Claims were checked against `cappadocian.dw.who-was-jesus`, `dw.want-to-believe`, `dw.how-it-reached-us`, `dw.confession-not-a-vote`, `dw.macrina-and-its-cost`, `story.macrina-deathbed`, `story.doxology-stand`, `force.thaumaturgan-inheritance`, `gravity.triune-confession`, `figure.eupsychius` and `figure.macrina`, and world_core cautions 1-3.
- **Quotes.** Both placed quotes match their records' `modern_rendering` exactly. This was checked by a normalised script compare and by reading them side by side. Each quote's `not_for` was checked against its lead-in and the sentences around it.
- **Readability.** `engine.m1.gates.grade_text` was run on each reply. Every voice turn clears FK 10 and FRE 60 (FK 5.9-7.7, FRE 67-79).
- **Not done.** No model call and no git command. No data dated before 27 October was used except the 13 October answers named above.

## Grades (new answers)

| # | Question | Result | Rigor | Access | Craft | Focus | Fabrication |
|---|---|---|---|---|---|---|---|
| 1 | Who is Jesus? | PASS | pass | concern | pass | pass | no |
| 2 | What did he do? | FAIL | fail | pass | fail | fail | no |
| 3 | What word did your people use...? | NOT SCORED | - | - | - | - | n/a |
| 4 | Why did your people believe this? | PASS | pass | concern | concern | pass | no |
| 5 | Tell me about someone who lived this out. | PASS | pass | concern | pass | pass | no |
| 6 | What would you want me to understand...? | PASS | concern | concern | concern | concern | no |

**1. Who is Jesus? (PASS).** A faithful reading of `dw.who-was-jesus`. It covers "fully what the Father is", the font formula, becoming god by grace with the gap never closing, ransom and physician, the poor as his image, and the resurrection. The Nyssa quote is placed with its record's own `means` as the lead-in, and it is named as Gregory of Nyssa's. Its not_for clauses hold: there is no pantheism, and the ransom line comes from the witness, not the quote.
- P2 access: a 9-sentence paragraph runs into a 10-sentence quote, and the lead-in sentence is 35 words.
- P2 engine: the figure card for "Gregory" resolves to Gregory of Nazianzus, though the text says "Gregory of Nyssa's Catechetical Oration".

**2. What did he do? (FAIL).** The first paragraph is right, but it repeats turn 1 almost word for word. Then: "He also met a rival claim head-on. We said that was the real presumption."
- **P1 misleading.** "He" can only be read as Jesus, so Jesus is made to answer a fourth-century rival teacher.
- **P1 damaged.** The engine removed the sentence naming Eunomius ("words attributed without a quote record"), so "that" points to nothing.
- **P1 focus.** Half the answer is then the Basil-against-Eunomius ant letter, which `dw.want-to-believe` holds for the question of wanting to believe. It does not answer what Jesus did.
- The quote matches. P2 rigor: it is given flatly as Basil's, but the record carries authorship as Contested, because the same passage stands in Nyssa's Against Eunomius.
- **Fix (engine).**
  - A removal that leaves a pronoun or "that" without its referent should trigger a redraft, not ship the rest (the same item as lpc E1).
  - `dw.want-to-believe` and the ant quote are offered on every turn of this conversation. Offers should be scored again against each new question rather than carried forward.

**3. What word did your people use...? (NOT SCORED).** The safety read failed (`safety_unread_turn`, `degraded: true`). A fixed Facilitator line went out, and the voice was never called, so there is no answer to grade.
- Engine item: the run records no cause for the failure, and the question was never answered. Log the cause, and re-run this question.

**4. Why did your people believe this? (PASS).** Three reasons, each grounded: the font formula as charter (`dw.how-it-reached-us`), the Wonderworker's line (`force.thaumaturgan-inheritance`, with the seventeen-to-seventeen story kept as "the country told it this way"), and the doxology (`story.doxology-stand`). The "stand or fall together" line is `gravity.triune-confession`'s. Nothing is invented, and it does not claim that Basil plainly called the Spirit God.
- P2 access: "doxology" is used before it is explained.
- P2 rigor and clarity: "a line of bishops behind him" reads as bishops before him. The force says the line came from his mission.
- P2 craft: a tidy summary closer ("So we believed because...").

**5. Tell me about someone who lived this out. (PASS).** Macrina, faithful to `dw.macrina-and-its-cost`, `story.macrina-deathbed` and caution 3. It names the Teacher, the betrothed and the resurrection reasoning, Annisa, the plank and the dialogue. It ends on "every word attributed to her reaches you through her brother's pen". It puts no quoted words in her mouth.
- P2 access: one 34-word sentence (the Annisa sentence).

**6. What would you want me to understand that I haven't asked? (PASS).** The material is right: received faith, the psalms forming the singer, the Wonderworker, the Forty, and Eupsychius under Julian, inside the window and as caution 2 states it.
- P2 focus: most of the first paragraph repeats turn 4 (font, "we did not vote", the line of bishops), in a question that asks for what has not been covered.
- P2 rigor: "martyrs cold in the ground one generation back" shipped although grounding marked it `withhold`. It also sits oddly beside "well inside our own years".
- P2 craft: "not an idea we chose from a menu" is modern idiom, and "with the door still open" is an unclear closer.
- P2 access: an 8-sentence paragraph.

## Side by side with the older answers (13 October, older data, read qualitatively)

| # | Older answer (13 Oct) | New answer (29 Oct) | New is |
|---|---|---|---|
| 1 | Short and clear. It glossed homoousios and hypostasis and gave becoming god by grace. No quote. | The same substance from the same witness, plus Nyssa's own words on why God was born among us. It is longer, and its first block is heavy. | same |
| 2 | Answered the question: physician, ransom, becoming god by grace, the poor as Christ. | Starts well, then turns to Eunomius, with a "He" that now points at Jesus and an orphaned "that". | worse |
| 3 | Answered with eusebeia, a real and well-explained word. But it tacked on a Spirit-ranking quote that is not about eusebeia. | No answer: the safety read failed and the Facilitator line went out. | worse |
| 4 | Font, song and unwritten customs, well put. But it ended on Nyssa's incarnation quote as if it were "the faith our teachers handed down", a misplaced quote. | Font, the Wonderworker's line and the doxology, all grounded, with no misplaced quote. | better |
| 5 | Macrina, close to the record, and it kept the cost (no see, no pulpit). | Macrina, close to the record, with the brother's-pen limit kept. It drops the cost line, which the question did not ask for. | same |
| 6 | New ground: the confession that could not be finished, and a movement hardening. But it ended broken, on a stray quotation mark ("What we handed on was not mastery. \""). | Complete and grounded, but it mostly repeats turn 4. | better |

**Overall.** About even. The new run is cleaner where it answers: no misplaced quotes, a properly attributed primary-source quote, and no broken ending. But it loses two answers. One is a removal that leaves Jesus answering Eunomius. The other is a question that never reached the voice. Repetition across turns is new and noticeable (turns 1-2 and turns 4-6). What changed in the system between the two runs is not known here, so this describes only the texts.

## Findings to fix

- **P1, E1 (engine).** Post-draft removal leaves pronoun and "that" residue (turn 2). Redraft when the removed sentence carries the referent.
- **P1, engine.** Offered records are carried across turns (`dw.want-to-believe` and the ant quote on every turn). Score offers again against each question.
- **Engine.** The safety read failed on turn 3 with no recorded cause. Log the cause and re-run the question.
- **P2, R-1 (engine).** Witness sentences recur word for word across turns (turns 1-2 and 4-6). This is the lpc repetition item.
- **P2 (engine).** The figure match on "Gregory" picks Nazianzus when the text names Nyssa. Prefer the qualified name in the text.
- **P2 (record).** In `force.thaumaturgan-inheritance`, say that the line of bishops follows from the mission, so "behind him" cannot be read as before him. Also gloss "doxology" in the voice's terms.
- **P2 (engine).** A `withhold` verdict shipped in turn 6. This is the same item as lpc E3.

NEW: PASS 4, FAIL 1, NOT SCORED 1 of 6; versus older: better 2, same 2, worse 2
