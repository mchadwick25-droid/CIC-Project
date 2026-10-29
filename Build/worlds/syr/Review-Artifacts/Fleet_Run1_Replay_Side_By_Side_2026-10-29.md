# syr: fleet graded run 1, six-question replay, side by side (29 October)

## Verdict

Yausep is the most even of the three replays. Five answers are faithful and distinctive: the Ihidaya, Sheol, the Physician and the sung teaching. Both placed quotes match their records. Ephrem is held to caution 9: the choirs rest on "later accounts".

One answer fails. Asked what it would want the participant to understand, the voice tells the Abgar legend well. Then it speaks the record's modern scholarly note as its own words ("Scholarship reads the whole account as a later claim..."). It closes on a claim no record holds: "we knew the difference between the story we loved and the ground we actually stood on." That gives a fourth-century church a modern critical view of its own founding story.

## Scope and method

- **New (today's code).** `engine/m3/reports/fleet-graded-run-1/replay/syr.json`, live test "fleet graded run 1". Package `packages/syr/2026-10-28T03-51-22Z`, which matches the registry pin. Voice: Sonnet 4.5. Safety and reader calls: Haiku 4.5. One conversation of six questions. Every turn went to the voice.
- **Older data.** `engine/m4/reports/live-turn-report-syr-2026-10-13-eleven-world-test.json` (13 October). It comes from a different engine and a different format, so it is read for what the text says and is not scored.
- **Method.** The method of `Build/worlds/lpc/Review-Artifacts/Run3_Access_And_Craft_Review_2026-10-28.md` and the rubric of `Build/worlds/lpc/build/lpc_Probe_Results.md` are used here. Each answer is graded on four criteria: Rigor, Accessibility, Craft and Focus.
  - P1 means wrong, invented, misleading or damaged. Any P1 makes the row FAIL.
  - P2 means small and plainly fixable. A row with only P2s is PASS, with the weak criterion graded `concern`.
  - Each fix is placed at the source: a record, a caution or an engine item.
- **Checked.**
  - Claims were checked against `records/syr/`: `syr.dw.jesus`, `syr.dw.physician`, `syr.term.ihidaya`, `syr.story.ephrem-famine-death`, `syr.story.choirs-tradition` and `syr.story.abgar-addai-legend`.
  - Claims were also checked against the ten world_core cautions in `compiled/prompt.txt`.
  - The two placed quotes (`syr.quote.ephrem-only-begotten-dwelling`, `syr.quote.nativity-this-is-the-day`) were checked by script against `compiled/quotes.json`. Both match.
- **Not done.** No model was called and no git command was run. Only this file and its `.counts.json` were written.

## Grades (new answers)

| # | Question | Result | Rigor | Access | Craft | Focus | Fabrication |
|---|---|---|---|---|---|---|---|
| 1 | Who is Jesus? | PASS | pass | pass | concern | pass | no |
| 2 | What did he do? | PASS | pass | concern | pass | pass | no |
| 3 | What word did your people use...? | PASS | pass | pass | pass | pass | no |
| 4 | Why did your people believe this? | PASS | concern | pass | concern | pass | no |
| 5 | Tell me about someone who lived this out. | PASS | concern | pass | concern | pass | no |
| 6 | What would you want me to understand...? | FAIL | fail | pass | fail | pass | no |

Readability is FK 5.1 to 7.4 and FRE 67.8 to 79.4 on all six. No paragraph runs past 7 sentences, and no sentence of the voice's own runs past 31 words. This is the best-paced of the three replays.

### Notes per answer

1. **Who is Jesus?** This is faithful to `syr.dw.jesus` and `syr.term.ihidaya`, and the quote matches.
   - P2 craft: the sentence before the quote says what the quote then says.
   - P2 craft: the tidy closer "We sang him more than we defined him." is uncited and coined.
2. **What did he do?** He broke death's rule, he healed, and he fulfilled the prophets. This is all from `syr.dw.jesus` and `syr.dw.physician`, and it answers the question. The engine removed a quotation the voice had typed itself, and left no residue.
   - P2 access: "The Persian sage" (Aphrahat) is never named or introduced. The phrase comes from the record's own "The sage".
3. **What word...?** Ihidaya, from `syr.term.ihidaya`. The voice keeps the false_friend: the ihidaye "did not leave for the desert. They stayed in town". This is clear and in the world's own voice.
4. **Why did your people believe this?** Received preaching, scripture fulfilled (the quote matches), the harmony read in worship, and the Physician.
   - P2 rigor: "We did not need to see him ourselves. The healing we saw in our own people was enough." This is uncited. It turns the record's "That was our experience of him, sung in our hymns" into healings the community watched happen. Three nearby sentences were marked `withhold` and shipped.
   - P2 craft: the woman in tears "past every watching eye" appears in turns 2, 4 and 5.
5. **Someone who lived this out.** Ephrem. The deacon at Nisibis and the move to Edessa follow caution 9. "Later accounts say the daughters of the covenant sang them" follows `syr.story.choirs-tradition`. The famine story is attributed to Palladius and Sozomen.
   - P2 rigor: "Ephrem preached that same truth - that everyone else carried wounds". The line "only One was without wound" is Aphrahat's in `syr.dw.physician`. The engine removed the Aphrahat sentence, so his teaching now sits under Ephrem's name.
   - P2 rigor: "Palladius and Sozomen, two early writers" drops the record's point that they wrote "a generation and more after his death". "He lived that openness himself" then states the tradition as his life, which leans against caution 9.
6. **What I haven't asked.** The legend is told as "our story, never as our history", as caution 2 requires.
   - P1 misleading: "What I would want you to understand is this: we knew the difference between the story we loved and the ground we actually stood on." No syr record says the community doubted the legend. `syr.story.abgar-addai-legend` notes only that the core of the correspondence is attested in this window by Eusebius. The voice gives the world a modern judgment of its own founding story.
   - P1 voice: "None of it is history. The king's own coinage stayed pagan. ... Scholarship reads the whole account as a later claim written backward". This is the record's `absent_detail`, an outside scholarly note, spoken in the world's "we". The project's rule is that a Representative's hedges are the world's own, and generic academic framing belongs to the Facilitator.
   - P2 craft: "What I would want" breaks the collective "we".

## Findings

### P1

**S1. Etic absent_detail voiced as the community's own knowledge (record and engine).**
- Where: answer 6.
- Fails against: Rigor (it claims a critical self-awareness that no record holds), voice-itself (the hedge is etic, not the world's own), and caution 2's intent (tell the legend "as how the community saw itself").
- Fix (record):
  - Rewrite `syr.story.abgar-addai-legend`'s `absent_detail` in two parts.
  - The first part is something the voice can say, in the world's own terms. For example: "We cannot show you the king's letter from his own days. The story comes to us long after him."
  - Move the coinage and the scholarly verdict to `modern_contrast` or a Facilitator-only field.
  - Add the not_for "a claim that the community itself doubted or disbelieved the legend".
- Fix (engine): text from `absent_detail` and `modern_contrast` should not be voiced word for word as "we". An output check should catch "Scholarship", "scholars" and "historians" in a Representative turn. The lpc R2 item is the same kind of defect.

### P2

- **E1 residue: misattribution after a removal (engine).** In answer 5, Aphrahat's line ends up under Ephrem's name. This is the lpc E1 item: a removal that changes who said something should trigger a redraft.
- **E3. Uncited claims shipped (engine).** Seven `withhold` sentences shipped, in answers 2 to 5. The one that matters is "The healing we saw in our own people was enough" (answer 4). The fix is lpc E3.
- **R-1. Repetition (engine).** "The woman who came to him in tears, past every watching eye" appears in three of the six turns. The fix is lpc R-1.
- **Unnamed epithet (record).** `syr.dw.physician` says "The sage". Name him once in the text ("Aphrahat, the Persian sage"), so the voice can introduce him.

## Side by side with the older test (13 October, older data, read qualitatively)

| # | Older answer did | New answer does | New vs older |
|---|---|---|---|
| 1 | The same content: Ihidaya, Sheol and the Physician. | The same, with the Ephrem quote placed (it repeats the sentence before it). | Same. |
| 2 | Death's rule broken, Death trembling in the hymns, healing and parables, followers sent out, the crucifixion, Sheol. It was fuller, but partly uncited. | Death's rule broken, the Physician, prophecy fulfilled. It is fully grounded, and the cross is not named. | Same. Each gains on one side: the older was fuller, the new is better grounded. |
| 3 | Ihidaya, clearly explained. | Ihidaya, plus the covenant members and the point that they were not hermits (the record's false_friend). | Better. |
| 4 | Scripture fulfilled (the same quote), one good God against Marcion's people, teaching carried in song. It was strong and distinctive. | Received preaching, the same quote, the Physician, and an uncited "healing we saw in our own people". | Worse. |
| 5 | Ephrem, but it stated as "what we can show you from his own years" that the women's choirs sang his hymns. Caution 9 says that rests on later accounts. | Ephrem, with "Later accounts say..." for the choirs. A small misattribution after a removal. | Better. |
| 6 | The silence of the women, the enslaved and ordinary households, stated plainly in the world's voice. This was a model honest limit. | The Abgar legend, then a modern scholarly verdict in the community's mouth. | Worse. |

**Overall.** In this text syr looks about the same as in the older test. It is better on cautions (answers 3 and 5) and worse on two answers where the voice reaches past its records (answers 4 and 6). What changed in the system between the two runs is not known to this review. These comparisons rest only on the text.

NEW: PASS 5, FAIL 1, NOT SCORED 0 of 6; versus older: better 2, same 2, worse 2
