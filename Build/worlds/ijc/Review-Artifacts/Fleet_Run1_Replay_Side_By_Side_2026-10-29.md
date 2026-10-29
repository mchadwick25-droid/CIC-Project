# ijc: six-question replay, fleet graded run 1 (29 October), side by side with the older 13 October answers

## Scope

- **New replay.** `engine/m3/reports/fleet-graded-run-1/replay/ijc.json`. Live test "fleet graded run 1". Package `packages/ijc/2026-10-28T03-50-07Z`. Voice: Sonnet 4.5. Safety and reader calls: Haiku 4.5. One conversation of six questions. All six went to the voice (`voice_with_directive`).
- **Older answers.** `engine/m4/reports/live-turn-report-ijc-2026-10-13-eleven-world-test.json` (package `2026-10-13T21-04-09Z`). This is older data, from a different format and a different engine. It is read only for what the text does. It is not scored.
- **Method.** As `Build/worlds/lpc/Review-Artifacts/Run3_Access_And_Craft_Review_2026-10-28.md` and `Build/worlds/lpc/build/lpc_Probe_Results.md`. Four criteria: Rigor, Accessibility, Craft, Focus. P1 is wrong, invented, misleading or damaged, and makes the row FAIL. P2 is small and plainly fixable. Each fix is at the source: a record, a caution or an engine item.
- **Checks.** Every shipped sentence was read against its cited records and against the ijc world_core horizon (312-451, closing at Chalcedon). The cited records are `ijc.dw.jesus`, `ijc.dw.received-not-seen`, `ijc.limit.jesus-to-you`, `ijc.term.homoios`, `ijc.demo.argued-about`, `ijc.story.emperor-penance` and `ijc.story.emperor-builds-another-basilica`. The two placed quotes, `ijc.quote.chalcedon-definition` and `ijc.quote.leo-tome-each-form`, match their `modern_rendering` exactly, checked by script. `cic/texts/` was searched for the details in Q5 that the records do not hold.
- **Readability.** Scored with `engine.m1.gates.grade_text`. The per-turn gate is FK 10 or under and FRE 60 or over. A turn past it is graded an Accessibility `fail`.
- **Not done.** No model was called. No git command was run. Only this file and its `.counts.json` were written.

## Readability

| Q | Words | FK | FRE | Longest own sentence | Sentences over 25 | Sentences per paragraph |
|---|---|---|---|---|---|---|
| 1 | 255 | 6.9 | 72.3 | 28 | 1 | 4, 7 |
| 2 | 246 | 6.4 | 79.9 | 31 | 2 | 3, 4, 3 |
| 3 | 159 | 8.5 | 62.5 | 28 | 1 | 6, 4 |
| 4 | 132 | 9.1 | **59.3** | 20 | 0 | 1, 7 |
| 5 | 174 | 8.9 | **54.9** | 35 | 2 | 9, 4 |
| 6 | 151 | 7.7 | 69.0 | 35 | 1 | 4, 4, 1 |

## Grades (new replay)

| Q | Question | Result | Rigor | Access | Craft | Focus | Fabrication | Basis |
|---|---|---|---|---|---|---|---|---|
| 1 | Who is Jesus? | PASS | pass | concern | concern | pass | no | Nicaea's words, Leo, and the Chalcedon definition placed whole. Chalcedon is the window's closing event, so it is in horizon. The honest limit from `ijc.limit.jesus-to-you` is very good: "Our record has the church's public words about Jesus, not its private ones". P2 craft: "This was not ornament." is uncited filler. P2 access: a 7-sentence paragraph. |
| 2 | What did he do? | PASS | pass | pass | concern | pass | no | The Leo quote, set to the question: what each nature did, and that one Christ hungered, wept and rose. It ends with an honest limit (no Galilee narratives) and "we could not add to it" (`ijc.dw.received-not-seen`). P2 craft: "So one Mediator could die in one nature and not die in the other" and the creed line repeat Q1 word for word. |
| 3 | A word I might not know | PASS | pass | concern | concern | pass | no | Homoios, from `ijc.term.homoios` and `ijc.demo.argued-about`. Constantius II and Valens. The exiles ran the other way. The losing side is known mostly through its victors. Faithful. P2 craft: "the Son is like the Father, as scripture says... and went no further" is said twice. "For roughly two decades of our own window" is build vocabulary. "the outcome went the other way than it finally did" is clumsy. A demonstration's lines are recited as the answer (`recited_demonstration: true`). |
| 4 | Why did your people believe this? | FAIL | pass | fail | concern | pass | no | **P1 accessibility:** FRE 59.3, under the per-turn floor of 60. The margin is small. The cause is a dense paragraph of council names (Nicaea, Constantinople, Ephesus, Chalcedon) with none explained. Content is faithful to `ijc.dw.received-not-seen`: the legate, not the bishops, recites the chain, as its not_for requires. P2 craft: "We guarded the testimony we received, and could not add to it" repeats Q2. |
| 5 | Someone who lived this out | FAIL | fail | fail | concern | concern | no | **P1 rigor: details not in the record.** "a riot broke out over an imprisoned charioteer" and "prostrate, confessing the sin of David, and Ambrose answering that since he had followed David in guilt, he should follow David in repentance" are in neither `ijc.story.emperor-penance` nor any ijc record. They are not in the vendored texts either. The record has the riot killing a general, Theodoret's "it is said" seven thousand, Ambrose's letter, and the later scene of purple laid aside and weeping. So a reported speech of Ambrose ships with no source. I believe both details come from Sozomen and Theodoret, so I do not mark it a fabrication, but nothing in the build supports them. **P1 accessibility:** FRE 54.9. P2 craft: "Here he held the emperor to it" has no clear "he" (a sentence was removed). P2 rigor: "the emperor, who had ordered the council that defined who Christ is" is loose for 381. P2 focus: a penance story for "lived this out" (the received faith) is a stretch. |
| 6 | What I haven't asked | PASS | pass | pass | concern | pass | no | The main fight was inside the church, and the empire backed the losing side. Then Constantine's 330 basilica, faithful to `ijc.story.emperor-builds-another-basilica` ("rather than send soldiers"). P2 craft: the engine removed Ammianus's quote, so "a pagan historian wrote his own verdict on what the prize was worth" announces a verdict that never comes. "That is not our own voice judging us." is an orphan line. The first paragraph repeats Q3. |

## Findings and fixes

**P1**

- **I1. Out-of-record detail in a story telling (engine and record), Q5.** The voice added a cause and a speech that `ijc.story.emperor-penance` does not hold. The grounding net passed them as tagged to that story. Fix:
  - Engine: grounding should test a story-tagged sentence's proper nouns and reported speech against the story's own `text` and `telling`, not only its tags. A reported speech with no record should be held.
  - Record: if the build wants Theodoret's David exchange, vendor Theodoret V.17 and Sozomen VII.25 and verify the line. Then add it to the story with its later-telling caveat. If not, add an `absent_detail` to the story saying the record does not give the riot's cause or the words at the door.
- **I2. Readability gate breached (engine), Q4 and Q5.** Two turns ship under FRE 60. Fix (engine): the per-turn gate should hold or redraft a turn below the floor, not ship it. Council names should also get the in-text gloss that `ijc.term.*` already carries.

**P2**

- **Repetition (engine).** "one Mediator could die in one nature", "could not add to it", and the homoios paragraph each ship twice in the six turns. Same as LPC R-1.
- **Orphaned announcements (engine).** Q6's pagan historian, and Q5's "Here he held the emperor to it". Same as LPC E1 residue.
- **Build vocabulary (record).** "our own window" in Q3 comes from `ijc.term.homoios` or `ijc.demo.argued-about`. Remove it from the text the voice speaks. Same as LPC F22.

## Side by side: older (13 Oct) and new (29 Oct)

| Q | Older answer (13 Oct, older data) | New answer (29 Oct) | New vs older |
|---|---|---|---|
| 1 | Nicaea, Leo, "We wrote definitions the way people write what they are prepared to be exiled over". Sound and short. | The same, plus the Chalcedon definition placed and an honest limit on private devotion. | **Better.** Fuller and honest about what the record lacks. |
| 2 | It opens "That is what our creed says he did", pointing at nothing, then recites the chain of faith. It never says what he did. | Leo's account of what each nature did, and an honest limit on the Gospel narratives. | **Better.** It now answers the question. |
| 3 | Homoousios. It never names the word at the start ("The Nicene word that binds..."). The history is right. | Homoios, named and explained. Same history, some repetition. | **Same.** |
| 4 | Why: if the Son is not truly God, what he gives is not God's to give. The Leo quote and the salvation stakes. A real reason. | Received testimony and the chain at Chalcedon. Nearly the older Q2's text, and under the FRE floor. | **Worse.** The older answer gave a reason. The new one gives a pedigree. |
| 5 | Leo, the Tome at Chalcedon, and the refusal of Canon 28. All in horizon (the window closes on that rejection) and grounded. | Theodosius's penance, with a cause and a speech not in the record, and under the FRE floor. | **Worse.** |
| 6 | Exile ran both ways with the emperor, "and we used it". An honest limit: almost every voice is a bishop or court. | The same first point, then a second point whose evidence the engine removed, ending on an orphan. | **Worse.** Less complete. |

**Overall.** Worse than the older test, by a little. The new run fixes the older Q2, which did not answer, and handles honest limits better in Q1 and Q2. But Q4 to Q6 are weaker. They show repetition, a story padded with details from outside the record, two turns under the readability floor, and an orphaned ending. What changed in the system between the two runs is not known to me. This compares only the text.

NEW: PASS 4, FAIL 2, NOT SCORED 0 of 6; versus older: better 2, same 1, worse 3
