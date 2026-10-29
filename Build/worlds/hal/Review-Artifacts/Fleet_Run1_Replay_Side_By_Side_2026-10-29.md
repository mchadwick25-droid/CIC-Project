# hal: fleet graded run 1, six-question replay, side by side (29 October)

## Verdict

Albina's voice is distinctive and mostly faithful. The cave, the feeding trough, Paula's journey and the community's own failures all come from the records, in plain words.

Three answers fail:

- **Answer 1** uses a name from after the window: "the translation labor later called the Vulgata". That wording is in the record itself.
- **Answer 2** replaces the question with an assistant-style choice between "what Jesus did, or what Jerome did". It then answers with a quote about Paula.
- **Answer 4** says the apostles' writings were corrected "against the Greek and the Hebrew - the Hebraica veritas". That misstates the world's signature principle.

## Scope and method

- **New (today's code).** `engine/m3/reports/fleet-graded-run-1/replay/hal.json`, live test "fleet graded run 1". Package `packages/hal/2026-10-28T04-11-39Z`, which matches the registry pin. Voice: Sonnet 4.5. Safety and reader calls: Haiku 4.5. One conversation of six questions. Every turn went to the voice.
- **Older data.** `engine/m4/reports/live-turn-report-hal-2026-10-13-eleven-world-test.json` (13 October). It comes from a different engine and a different format, so it is read for what the text says and is not scored.
- **Method.** The method of `Build/worlds/lpc/Review-Artifacts/Run3_Access_And_Craft_Review_2026-10-28.md` and the rubric of `Build/worlds/lpc/build/lpc_Probe_Results.md` are used here. Each answer is graded on four criteria: Rigor, Accessibility, Craft and Focus.
  - P1 means wrong, invented, misleading or damaged. Any P1 makes the row FAIL.
  - P2 means small and plainly fixable. A row with only P2s is PASS, with the weak criterion graded `concern`.
  - Each fix is placed at the source: a record, a caution or an engine item.
- **Checked.**
  - Claims were checked against `records/hal/`: `hal.dw.jesus`, `hal.dw.record`, `hal.dw.church-failure`, `hal.term.monachus`, `hal.term.matrona`, `hal.term.origenism`, `hal.term.pelagianism`, `hal.story.journey-to-bethlehem`, `hal.story.ciceronian-dream` and `hal.demo.born-again`.
  - Claims were also checked against the eight world_core cautions in `compiled/prompt.txt`.
  - The two placed quotes (`hal.quote.eyes-of-faith`, `hal.quote.hail-bethlehem`) were checked by script against `compiled/quotes.json`. Both match.
- **Not done.** No model was called and no git command was run. Only this file and its `.counts.json` were written.

## Grades (new answers)

| # | Question | Result | Rigor | Access | Craft | Focus | Fabrication |
|---|---|---|---|---|---|---|---|
| 1 | Who is Jesus? | FAIL | fail | concern | pass | pass | no |
| 2 | What did he do? | FAIL | concern | pass | fail | fail | no |
| 3 | What word did your people use...? | PASS | concern | concern | pass | concern | no |
| 4 | Why did your people believe this? | FAIL | fail | concern | pass | pass | no |
| 5 | Tell me about someone who lived this out. | PASS | concern | concern | concern | pass | no |
| 6 | What would you want me to understand...? | PASS | pass | concern | concern | pass | no |

Readability is FK 6.2 to 8.3 and FRE 67.3 to 77.8 on all six. Answers 1 and 3 are each one block of 9 sentences, and answers 4, 5 and 6 each open with an 8-sentence paragraph.

### Notes per answer

1. **Who is Jesus?** This follows `hal.dw.jesus` almost line for line, and it is strong writing in the world's own image.
   - P1: "the translation labor later called the Vulgata" is knowledge from after the window. Caution 5 says the name "belongs to later centuries". The phrase is in `hal.dw.jesus`'s own `text`, so the voice is reading it from the record.
   - P2 access: one 9-sentence block.
   - The engine removed a Paula lead-in whose quote did not match, and left no residue.
2. **What did he do?**
   - P1 craft and focus. The reply opens "The question 'what did he do' could mean what Jesus did, or what Jerome did, or what action some other man took. We will answer for Jesus first." It closes "If you are asking what Jerome did ... tell us and we will answer that." Jerome was not named in turn 1, so there was nothing to choose between. This is assistant cadence spoken in the world's voice, and all three sentences were marked `withhold` and shipped.
   - What follows restates turn 1 (born poor, died, rose). The placed quote is Paula's "eyes of faith" vision, which is about her devotion and not about what Jesus did. The lead-in keeps the quote's not_for, because it is devotional sight, not literal sight.
   - The second quote (hail-bethlehem) was removed cleanly.
3. **What word...?** "Monachus" is faithful to `hal.term.monachus`, including its limit: "no surviving letter names one of them".
   - P2 rigor: "Jerome led them, we know that much, and they copied books and prayed the hours" shipped uncited. It presents daily life as known, against caution 7 ("never call it Documented").
   - P2 rigor: the Greek etymology and the names "Eustochium ... Marcella and Fabiola" also shipped uncited. They are true, but they are not tagged.
   - P2 focus: asked for a word "I might not know", the voice picks one it calls "close to the modern word".
   - P2 access: one 9-sentence block.
4. **Why did your people believe this?**
   - P1 rigor: "The apostles' writings came down to us ... and we spent our lives correcting them word by word against the Greek and the Hebrew - the Hebraica veritas". `hal.dw.record` says something different: "The Gospels were revised against the Greek. The Old Testament was translated from the Hebrew." The voice applies the Hebrew principle to the apostles' writings. That is wrong, and it misstates the world's central term.
   - The quote matches, and its lead-in keeps the not_for ("puts in her mouth" means these are not Paula's own words).
   - P2 access: the sentences run to 39 and 36 words.
5. **Someone who lived this out.** Paula, from `hal.term.matrona`, `hal.term.vidua`, `hal.story.journey-to-bethlehem` and `hal.term.epitaphium`. The children on the shore, the double monastery and 404 all match.
   - P2 craft: the reply ends "One other voice spoke of her." That is residue. The engine removed the Palladius quote that the line was introducing.
   - P2 rigor: "gave away her fortune until her own relatives objected" is supported only by `hal.demo.born-again`, and it is tagged to `hal.dw.jesus`, which does not hold it.
   - P2 access: an 8-sentence paragraph.
6. **What I haven't asked.** This is faithful to `hal.dw.church-failure`, `hal.term.origenism` and `hal.term.pelagianism`. "Fellow Christians" as the attackers is in the record, and no casualties are invented.
   - P2 craft and access: "the oath he swore in that dream" refers to a dream this conversation never told. The engine removed the sentence that set it up. The point itself is supported by `hal.story.ciceronian-dream`.
   - P2 craft: "We also broke ourselves" is unclear.

## Findings

### P1

**H1. A name from after the window, in the record (record).**
- Where: answer 1. The older test had the same phrase.
- Fails against: caution 5.
- Fix (record):
  - Remove "- the translation labor later called the Vulgata" from `hal.dw.jesus`'s `text`.
  - Search the other hal voiced texts for "Vulgat" and remove it there as well.
  - Card text that the Facilitator speaks may keep "later called the Vulgate".
- Fix (engine): the horizon check should catch "later called" and similar phrases.

**H2. The voice invents a choice between readings and makes an assistant offer (engine; record gap).**
- Where: answer 2.
- Fails against: Craft (no AI tells), Focus.
- Fix:
  - Engine. Resolve "he" against the prior turn's subject, which was Jesus.
  - Engine. An output check should catch replies that open by discussing what the question could mean, or that close with "tell us and we will answer". The lpc laundering-1 offer was the same pattern.
  - Record. `hal.dw.jesus` says nothing about Jesus' life between the birth and the cross. The build should decide whether to author a short witness on how this world spoke of his life and teaching, or an honest limit. The world's own call texts (the rich young man, leaving one's nets) are candidates, to be verified against the vendored Jerome letters.

**H3. Hebraica veritas applied to the apostles' writings (record and engine).**
- Where: answer 4. The older test made the same conflation.
- Fails against: Rigor.
- Fix (record): in `hal.dw.record`, add the not_for "a claim that the apostles' writings or the Gospels were corrected against the Hebrew".
- Fix (engine): the grounding net passed the sentence because it shares words with its record. It should also test it against the record's not_for. This is the same item as lpc E5.

### P2

- **E3. Uncited specific claims shipped (engine).** Six `withhold` sentences shipped, in answers 2, 3, 5 and 6. The fix is lpc E3.
- **Residue (engine, lpc E1).** "One other voice spoke of her." (answer 5) and "that dream" (answer 6).
- **A1. Paragraph length (prompt and engine).** Two 9-sentence blocks and three paragraphs of 8 sentences. The fix is lpc A1.
- **Caution 7 (record).** In `hal.term.monachus`, add the not_for "stating the men's daily work and prayer schedule as known".

## Side by side with the older test (13 October, older data, read qualitatively)

| # | Older answer did | New answer does | New vs older |
|---|---|---|---|
| 1 | Almost the same text, including "later called the Vulgata". | The same, in shorter sentences. | Same. |
| 2 | It answered: he redeemed us by his death, was born poor, lived as a teacher, called people to follow him (the rich young man, the disciples who left their nets), was crucified and rose. | It offers a choice between Jesus and Jerome, restates turn 1, places a Paula quote, and closes with an offer. | Worse. |
| 3 | "Hebraica veritas", the world's own signature term. It was vivid, and the Oea riot over one word in Jonah is in the records (`hal.figure.augustine`). | "Monachus", a near-modern word, with uncited daily-life claims. | Worse. The weaker choice of word, and less grounded. |
| 4 | Writings, worship and the land; the same Hebrew conflation; it closed on an argument ("people do not empty their houses for a lie"). | Writings, worship and the land; the same conflation; a matching quote added. | Same. |
| 5 | Paula, faithfully told. It closed honestly: "Her own letters were not kept." | Paula, faithfully told, with more detail. It closes on the broken line "One other voice spoke of her." | Worse. The same substance, but a damaged ending in place of an honest limit. |
| 6 | Grief that was held as faithful: Marcella beaten by soldiers, the old answers and the tears kept together. | Failures and controversies, from the records. "That dream" is never set up. | Same. Both are honest and grounded, and they choose different hard truths. |

**Overall.** In this text hal looks somewhat worse than in the older test. The old defects (the Vulgata name and the Hebrew conflation) are still there. Two answers that worked before now do not: answer 2 has lost its direct answer, and answer 5 ends on residue. What changed in the system between the two runs is not known to this review. These comparisons rest only on the text.

NEW: PASS 3, FAIL 3, NOT SCORED 0 of 6; versus older: better 0, same 3, worse 3
