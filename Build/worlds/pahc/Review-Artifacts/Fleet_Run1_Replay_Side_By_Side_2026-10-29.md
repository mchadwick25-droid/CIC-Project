# pahc: fleet graded run 1, six-question replay, side by side (29 October)

## Verdict

Chloe holds up well on five of the six questions. Every claim in those five answers is in the records. Nothing came from after 200. Both placed quotes match their records word for word.

One answer is broken. Asked "What did he do?" (meaning Jesus), the reply opens on Justin's road to belief. The engine had removed the sentence that named Justin, so "he" now reads as Jesus. A reader is told that Jesus "had already gone looking through other philosophies".

## Scope and method

- **New (today's code).** `engine/m3/reports/fleet-graded-run-1/replay/pahc.json`, live test "fleet graded run 1". Package `packages/pahc/2026-10-28T03-51-09Z`, which matches the registry pin. Voice: Sonnet 4.5. Safety and reader calls: Haiku 4.5. One conversation of six questions. Every turn went to the voice, and none went to the Facilitator.
- **Older data.** `engine/m4/reports/live-turn-report-pahc-2026-10-13-eleven-world-test.json` (13 October, eleven-world test). It comes from a different engine and a different format, so it is read for what the text says and is not scored.
- **Method.** The method of `Build/worlds/lpc/Review-Artifacts/Run3_Access_And_Craft_Review_2026-10-28.md` and the rubric of `Build/worlds/lpc/build/lpc_Probe_Results.md` are used here. Each answer is graded on four criteria: Rigor, Accessibility, Craft and Focus.
  - P1 means wrong, invented, misleading or damaged. Any P1 makes the row FAIL.
  - P2 means small and plainly fixable. A row with only P2s is PASS, with the weak criterion graded `concern`.
  - Each fix is placed at the source: a record, a caution or an engine item.
- **Checked.**
  - Every cited sentence was checked against its record in `records/pahc/`, against the ten world_core cautions in `compiled/prompt.txt`, and against the not_for lines of the quotes used.
  - The two placed quotes were checked by script against `compiled/quotes.json` (`modern_rendering`). Both match.
  - Grounding verdicts, `reply_shape.removed` and `output_defects` were read for every turn.
  - Readability was measured with `engine.m1.gates.grade_text`.
- **Not done.** No model was called and no git command was run. Only this file and its `.counts.json` were written.

## Grades (new answers)

| # | Question | Result | Rigor | Access | Craft | Focus | Fabrication |
|---|---|---|---|---|---|---|---|
| 1 | Who is Jesus? | PASS | pass | concern | concern | pass | no |
| 2 | What did he do? | FAIL | fail | pass | fail | fail | no |
| 3 | What word did your people use...? | PASS | pass | concern | pass | pass | no |
| 4 | Why did your people believe this? | PASS | pass | pass | concern | pass | no |
| 5 | Tell me about someone who lived this out. | PASS | pass | concern | concern | pass | no |
| 6 | What would you want me to understand...? | PASS | concern | pass | concern | pass | no |

Readability is FK 5.9 to 8.7 and FRE 63.7 to 78.5 on all six. The paragraph rule (1 to 4 sentences) is broken in five of the six. Access is graded `concern` only for a paragraph of 8 or more sentences, a sentence of over 30 words in the voice's own words, or a term used before it is explained.

### Notes per answer

1. **Who is Jesus?** This is faithful to `pahc.witness.who-was-jesus`. The Ignatius quote matches `pahc.quote.ignatius-truly-born`, and the not_for lines are kept: the voice does not call "truly" a formula the whole network shared.
   - P2 craft: the voice says the "truly" chain in its own words and then the quote says it all again, so the answer runs the same list twice.
   - P2 craft: "born and raised and put to death" puts "raised" before the death, so it reads as "brought up", not risen.
   - P2: "the Father's own life reached us" was marked `withhold` (uncited) and shipped. It is a small step past the record.
   - P2 access: the thanksgiving sentence runs to 36 words.
2. **What did he do?** P1, damaged and misleading.
   - The engine removed "Justin recalls that after an old man's words..." because it was tagged to a quote that was not placed. The reply now opens "Before that, he had already gone looking through other philosophies. He turned the old man's words over in his mind...". After turn 1, "he" is Jesus.
   - The retrieval was also wrong. `pahc.witness.coming-to-belief` answers "how did someone come to believe", not what Jesus did.
   - The last sentence repeats turn 1's list ("he ate and drank, he was persecuted under Pilate...").
   - The question is never really answered.
3. **What word...?** This is faithful to `pahc.term.ekklesia`, `pahc.term.hetaeria` and `pahc.term.eucharistia`. Justin's order (reading, sermon, prayer) matches `pahc.story.justin-sunday-gathering`. The Didache order matches `pahc.story.didache-eucharist`, and the voice keeps it to one community, as caution 5 and the story's absent_detail require.
   - P2 access: the Didache sentence runs to 47 words, with a dash and three "about" phrases.
4. **Why did your people believe this?** This answers from `pahc.witness.how-we-know` and `pahc.force.neronian-persecution`. The Justin quote matches, and the voice keeps its not_for ("not typical"): "But that is one man's account".
   - P2 craft: "We do not have the same account from someone without what he had" is word for word from turn 2.
   - P2 craft: the lead-in sums up the quote just before the quote gives it.
5. **Someone who lived this out.** Polycarp is told from `pahc.story.martyrdom-of-polycarp`, and the voice says plainly that this is his own community's memory and that no outside witness confirms it. The letter details (presbyters and deacons; "Polycarp and the presbyters with him"; Ignatius calls him bishop) match `pahc.force.authority-consolidation`.
   - P2 access: the second paragraph has 8 sentences.
   - P2 craft: the tidy closer "That is the man: he led without claiming the title..." turns one letter's salutation into a statement about his character. "We should say this plainly" repeats turn 2's opening.
6. **What I haven't asked.** This is faithful to `pahc.witness.what-we-never-settled` and `pahc.limit.ordinary-majority`. Both leadership patterns are held open (caution 2).
   - P2 rigor: "That disagreement was not a side matter. It shaped everything about ... whether a letter from another church carried weight because one man vouched for it or because a council did." The grounding net marked this `withhold` (25% grounded) and it shipped. No record says it, and "everything" overclaims.

## Findings

### P1

**E1. A removal leaves a pronoun with the wrong referent, and the reader picks the wrong record (engine; record gap).**
- Where: answer 2.
- Fails against: Rigor (it states that Jesus searched other philosophies), Focus and Craft.
- Fix:
  - Engine. A removal that takes out the sentence that names the subject should trigger a redraft or hold the reply back, not ship the rest. This is the same item as lpc E1.
  - Engine. The reader should resolve "he" in a follow-up question against the prior turn's subject (Jesus) before it picks records.
  - Record. No pahc record answers "what did Jesus do" beyond the death-and-resurrection chain. The build should decide between two options:
    - Author a witness on what these communities said Jesus did and taught. Candidates are the Didache's "teaching of the Lord" (the Two Ways) and 1 Clement 13's "words of the Lord Jesus which he spoke, teaching". Verify both against the vendored ANF texts first.
    - Author an honest limit that says no narrative of his days survives in the world's own voices. The older answer said this, and said it well.

### P2

- **R-1. Repetition (engine).** Turn 2's closing pair of sentences returns word for word in turn 4. Turn 1's list returns in turn 2. "We should say (this) plainly" opens a paragraph in turns 2 and 5. The fix is the conversation-level repeat check (lpc R-1).
- **E3. An uncited claim shipped (engine).** In answer 6, a `withhold` sentence shipped. The fix is the same as lpc E3: hold a `withhold` sentence for a grounded redraft.
- **A1. Paragraph and sentence length (prompt and engine).** There are paragraphs of 6 to 8 sentences, and sentences of 36 and 47 words (answers 1 and 3). The fix is lpc A1.
- **Quote doubling (engine).** In answers 1 and 4 the voice says a quote's content just before placing it. Placement should drop a lead-in that sums up the quote it introduces.

## Side by side with the older test (13 October, older data, read qualitatively)

| # | Older answer did | New answer does | New vs older |
|---|---|---|---|
| 1 | It gave a short, accurate creed: truly man, crucified, raised. It added that no surviving writer explained how calling Jesus God fits with calling the Father God, and then the chain of handing-down. | It places the Ignatius quote in full, but says the same list twice. | Same. The new answer has a verbatim source but more repetition. The older one was tighter and said more. |
| 2 | It answered the question. It gave what Ignatius pressed (ate, drank, suffered, died, rose) and the memoirs read aloud. Then it said honestly that "a narrative of his days among us ... is not what survives in our own voices." | It opens on Justin with "he" left pointing at Jesus, then repeats turn 1. | Worse. The older answer was right and honest. The new one is damaged. |
| 3 | It explained ekklesia, then placed an unrelated Justin quote (on Socrates and Heraclitus as "Christians") as if it were about the word. | It covers three words clearly from their records. No quote is misused. | Better. |
| 4 | It said "the apostles said they had seen it", then placed the Ignatius "truly" quote, which does not answer "why". One very long paragraph. | It gives the handed-down chain, the loss of eyewitnesses, and a fitting Justin quote with its limit stated. It repeats one line from turn 2. | Better. |
| 5 | It told Polycarp, but added that the man who led him to the stake "regretted it afterward". No pahc record holds that. | It tells Polycarp faithfully, says plainly whose memory it is, and adds his own letter. | Better. Nothing is invented. |
| 6 | It gave the leadership split and the silent majority. It added "Not God's nature, not what scripture meant", which overclaims. | The same two points, closer to the record's words. It carries one uncited overclaim ("It shaped everything"). | Same. |

**Overall.** In this text pahc looks better than in the older test. The older answers had a misused quote (3), an off-question quote (4) and an invented detail (5). The new answers have none of these. The new run's one serious defect is answer 2. What changed in the system between the two runs is not known to this review. These comparisons rest only on the text.

NEW: PASS 5, FAIL 1, NOT SCORED 0 of 6; versus older: better 3, same 2, worse 1
