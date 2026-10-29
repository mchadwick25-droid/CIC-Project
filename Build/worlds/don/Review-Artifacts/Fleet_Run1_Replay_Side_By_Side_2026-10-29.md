# don: fleet graded run 1, six-question replay, side by side (29 October)

## Scope

- **New answers.** `engine/m3/reports/fleet-graded-run-1/replay/don.json`. Live test "fleet graded run 1", package `packages/don/2026-10-28T03-49-46Z`, which is the registry pin. Voice: Sonnet 4.5. Safety and reader calls: Haiku 4.5. It is one conversation of six questions.
- **Older answers.** `engine/m4/reports/live-turn-report-don-2026-10-13-eleven-world-test.json` (13 October eleven-world test). That is older data, from a different format and engine. It is read for comparison only and is not scored.
- **Method.** The same method as `Build/worlds/lpc/Review-Artifacts/Run3_Access_And_Craft_Review_2026-10-28.md` and the rubric in `Build/worlds/lpc/build/lpc_Probe_Results.md`. There are four criteria: Rigor, Accessibility, Craft and Focus. P1 is wrong, invented, misleading or damaged, and it makes the row FAIL. P2 is small and fixable, and a row with only P2s is PASS with that criterion graded `concern`. Each fix is at the source: a record, a caution or an engine item.
- **Checked.** For each turn: the shipped text, citations, `reply_shape`, grounding verdicts, `output_defects`, glosses and offers. Claims were checked against `don.dw.who-jesus-was-among-us`, `dw.the-books-they-came-for`, `dw.the-creed-we-shared`, `dw.not-a-death-wish`, `witness.one-formation-aim`, `term.ecclesia`, `story.passio-donati-sermon`, `story.passio-marculi` and `contested.augustine-precipice-charge`, and world_core cautions 1, 2, 5, 6 and 8.
- **Quotes.** No quote record was placed in any turn. The bishops' words at the 411 conference come as reported speech from `dw.who-jesus-was-among-us`'s own text, as that record's tension asks ("reported sense rather than as a quotable clause").
- **Readability.** `engine.m1.gates.grade_text` was run on each reply. Every turn clears FK 10 and FRE 60 (FK 4.3-6.9, FRE 70-85).
- **Not done.** No model call and no git command. No data dated before 27 October was used except the 13 October answers named above.

## Grades (new answers)

| # | Question | Result | Rigor | Access | Craft | Focus | Fabrication |
|---|---|---|---|---|---|---|---|
| 1 | Who is Jesus? | PASS | pass | concern | pass | pass | no |
| 2 | What did he do? | FAIL | pass | concern | concern | fail | no |
| 3 | What word did your people use...? | FAIL | fail | pass | pass | pass | no |
| 4 | Why did your people believe this? | PASS | pass | pass | concern | pass | no |
| 5 | Tell me about someone who lived this out. | PASS | concern | concern | concern | pass | no |
| 6 | What would you want me to understand...? | FAIL | fail | pass | concern | concern | no |

**1. Who is Jesus? (PASS).** Strong, and true to `dw.who-jesus-was-among-us`. It gives the shared creed, says "the quarrel was never about who Christ is", and has the bishop of Constantina refusing the judge's chair. It ends on the world-hates-it verse: "The church the world listened to... belonged to the world." The 279-bishop count is left out, which is right, since the number is a contested count.
- P2 access: the reported speech of the bishop of Constantina is one 41-word sentence.

**2. What did he do? (FAIL).** **P1 focus: the question is never answered.** The voice recites `dw.the-books-they-came-for` almost whole. It covers the books surrendered under the edict, Cyprian's line, and no eyewitnesses. It ends: "On how we knew the resurrection happened, we will not manufacture an answer." Nothing is said about what Jesus did, died or was raised for. The word "him" slides between Jesus and Cyprian ("They reached us...", "His letters"). Every sentence is true to its record.
- P2 craft: the last line narrates a refusal of a question nobody asked.
- P2 access: one 32-word sentence.
- **Fix (record).** Add "participant asks what Jesus did" to the `retrieve_when` of `dw.who-jesus-was-among-us`, whose last paragraph already answers it ("We left no treatise on what his death meant..."). Add the same to `dw.the-creed-we-shared` ("who died and was raised").
- **Fix (engine).** The voice tagged `the-books-they-came-for`, which was not among this turn's offered records. Retrieval and the grounding net should not let an un-offered record carry a whole answer to a different question.

**3. What word did your people use...? (FAIL).** Ecclesia, explained well from `term.ecclesia`: no neutral word, two rival bodies, town by town.
- **P1 wrong.** "Where it came from is the Latin word for an assembly." Ecclesia is a Greek word (ekklesia, assembly) that Latin borrowed. No record states an origin. The sentence is grounded only 40%, and it shipped as `ok`.
- **Fix (record).** Add the word's origin to `don.term.ecclesia`, in the voice's terms: a Greek word for the assembly, taken into Latin by the church.
- **Fix (engine).** This is the same item as lpc E3. A low-ground specific claim, such as an etymology, should be held for a grounded redraft and not shipped.
- P2 rigor: "They said it of themselves too" shipped as `withhold`. It is true.

**4. Why did your people believe this? (PASS).** It answers with the world's own mechanism: suffering as the mark, the yearly graveside reading, the twelfth-of-March account of soldiers taking a Carthage basilica (`story.passio-donati-sermon`; no year is given, so caution 5 holds), walking to one font, and living under a hostile state.
- P2 craft: a stock "not X but Y" turn ("That was not history being remembered. That was the communion being formed again"), and it shipped although grounding marked it `withhold`.

**5. Tell me about someone who lived this out. (PASS).** Marculus, from `story.passio-marculi` and `dw.not-a-death-wish`. It gives Novapetra, the cup, crown and palm, before dawn, the gentle fall and the bright cloud. The marvels are framed as "the account" and "the tradition says", and no year is given (caution 6).
- P2 rigor: "after a day of fasting" is more exact than the record ("while he fasted there", over four days).
- P2 rigor: "he was thrown from the cliff" is the Passio's own telling, which `contested.augustine-precipice-charge` keeps open. The flat sentence would be safer as "the account says".
- P2 craft: "The cliff is the last four days of his story" is a garbled sentence copied from `dw.not-a-death-wish`'s text. "That is the Christ we carried..." repeats turn 1.
- P2 access: one 34-word sentence.
- **Fix (record).** Rewrite that sentence in `dw.not-a-death-wish` (for example, "He was held four days at the cliff").

**6. What would you want me to understand that I haven't asked? (FAIL).**
- **P1 misleading, against a record's not_for.** It opens "We held one conviction, seen from four sides". `don.witness.one-formation-aim` gives this as "A modern reading of our record sees one conviction here... Nothing we wrote that survives puts it that way." Its not_for bars "a claim that the Donatists themselves described these as one conviction". The voice dropped the frame and states a modern synthesis as the community's own self-description.
- The two strains that follow are correct, and caution 8 holds: Maximianist clergy received back, and recourse to the state three times.
- P2 focus and craft: the third paragraph repeats turn 4 almost word for word (font, grave, state).
- **Fix (record).** Put the hedge inside the sentence the voice is likely to lift. For example: "We never named it as one conviction. Seen from here, though, purity, the washing, the memory of our martyrs and our refusal of the state went together." Alternatively, mark the witness etic.
- **Fix (engine).** Test each shipped sentence that cites a record against that record's not_for. This is the same as lpc E5, widened from quote lead-ins to witness text.

## Side by side with the older answers (13 October, older data, read qualitatively)

| # | Older answer (13 Oct) | New answer (29 Oct) | New is |
|---|---|---|---|
| 1 | The chair refusal and the creed. But it stated "two hundred and seventy-nine of us... stood for three days" flatly, and the record gives that count as the later editors' and contested. | The same core, without the count, plus the world-hates-it verse. | better |
| 2 | Answered: "He died and was raised". It said honestly that no one wrote down what the death accomplished, and gave the martyr pattern. | Talks about the books instead, and never says what he did. | worse |
| 3 | Ecclesia, with the right origin ("straight from the Greek, through Latin... the assembly") and the refusal to call the rival Catholic. | Ecclesia, well explained, but with the wrong origin ("the Latin word for an assembly"). | worse |
| 4 | Answered "why believe Jesus is who he is" by repeating turn 1 (chair, 279, three days). | Answers from the world's own life: suffering, the graveside reading, the font, the state. | better |
| 5 | Marculus, almost the same text, with the same garbled "cliff is the last four days" line. | Marculus, almost the same text. | same |
| 6 | New ground: Bagai and the readmitted bishops, and charges of forced baptism, kept as charges. It ended on an unasked "So yes, you could come back to us". | States a modern synthesis as the community's own words, then repeats turn 4. | worse |

**Overall.** Slightly worse than the older test. The new run is stronger on turns 1 and 4, where it speaks from the world's own practice and drops a contested number. But it fails three of six: one question goes unanswered, one word's origin is wrong where the older answer had it right, and one record's not_for is broken. Repetition across turns is new (turns 1, 4, 5 and 6). What changed in the system between the two runs is not known here, so this describes only the texts.

## Findings to fix

- **P1 (record and engine).** Turn 2 is unanswered. Widen `retrieve_when` on `dw.who-jesus-was-among-us` and `dw.the-creed-we-shared`, and stop un-offered records from carrying an answer.
- **P1 (record and engine).** Turn 3's etymology is wrong. Add the origin to `term.ecclesia`, and hold low-ground specific claims (lpc E3).
- **P1 (record and engine).** Turn 6 breaks `witness.one-formation-aim`'s not_for. Put the hedge in the liftable sentence, and check cited witness text against not_for (lpc E5, widened).
- **P2 (record).** Rewrite the garbled "The cliff is the last four days of his story" in `dw.not-a-death-wish`.
- **P2 (engine).** Witness sentences recur across turns (lpc R-1). Two `withhold` sentences shipped (turns 3 and 4).

NEW: PASS 3, FAIL 3, NOT SCORED 0 of 6; versus older: better 2, same 1, worse 3
