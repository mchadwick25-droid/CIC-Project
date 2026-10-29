# witt fleet graded run 1, six-question replay (29 October): grades and side-by-side

## Verdict

**Revise.** Five of six answers pass with small defects. One fails.

- **Q5 (someone who lived this out)** is damaged. The engine removed the Large Catechism warning about the poor man at the door, because the voice typed it as its own quotation. What shipped points to that missing text: "Here is what the program itself shows. That is not gentle language." and "the poor man". Nobody is named, although the records hold named people, such as the Brussels martyrs, whom the older answer used well.
- **Repetition across the conversation.** The creed's redemption lines come in Q1 and again in Q2. The justification sentence ("This is the center of our whole teaching") comes in Q2 and again in Q3. This is P2, but it is the run's main craft weakness.

The voice is plain and confessional, as it should be. It keeps the founder's complaint as testimony, not as a parish report (Q6), as `witt.dw.cold-and-careless-among-us` requires. No claim goes past the 1580 horizon. No held 1525 line is misquoted.

## Scope and checks

- **Run.** Fleet graded run 1, replay, 29 October. Package `packages/witt/2026-10-28T04-40-35Z`. Voice: Sonnet 4.5. One conversation of six questions.
- **Read in full.** All six shipped `voice_event.text` answers, their citations, `reply_shape.placed` and `removed`, and the grounding verdicts. No turn went to the Facilitator. `output_defects` is empty and `answer_record_fallback` is null in all six.
- **Quotes.** The two placed quotes (second-article-of-the-creed, the-sword-is-at-your-throats) match their `modern_rendering` exactly, checked by script. Q2 repeats creed lines without quotation marks and cites the quote record for them.
- **Records.** Claims checked against `repository.json`, the world_core cautions in `prompt.txt` (held 1525 lines only, nothing of 1543, no borrowed Strasbourg voice), and the not_for lists of every cited record.
- **Readability.** `engine.m1.gates.grade_text` on each shipped reply. Sentence and paragraph counts by script, with placed quotations left out.
- **Truncation.** Two methods: every reply ends on closing punctuation, and no reply has `degraded` or `degraded_by_net` set. No truncation.
- **Older data.** `engine/m4/reports/live-turn-report-witt-2026-10-13-eleven-world-test.json` (13 October, package `2026-10-13T20-15-56Z`) is older data from a different engine and format. It is read qualitatively only and is not scored.
- No model was called. No git command was run. Only this file and its `.counts.json` were written.

## Readability (new answers)

| Q | Words | FK | FRE | Longest own sentence | Over 25 | Sentences per paragraph |
|---|---|---|---|---|---|---|
| 1 | 359 | 5.6 | 79.6 | 32 | 1 | 4, 3, 3 |
| 2 | 173 | 4.9 | 83.7 | 29 | 2 | 6, 4, 3 |
| 3 | 148 | 5.0 | 79.2 | 23 | 0 | 8, 5 |
| 4 | 204 | 8.0 | 70.5 | 44 | 3 | 3, 7, 1 |
| 5 | 139 | 7.2 | 71.3 | 26 | 1 | 5, 2, 2 |
| 6 | 384 | 5.7 | 81.7 | 31 | 3 | 6, 4, 2, 1, 2 |

All six clear FK 10 and FRE 60.

## Grades (new answers)

Criteria: Rigor, Accessibility, Craft, Focus. `pass`, `concern` (P2: small, fixable) or `fail` (P1: wrong, invented, misleading or damaged). A row with only P2s is PASS.

| Q | Question | Result | Rigor | Access | Craft | Focus | Fabrication | Notes |
|---|---|---|---|---|---|---|---|---|
| 1 | Who is Jesus? | PASS | pass | concern | concern | concern | no | Truly God and truly man, from witt.dw.truly-god-and-truly-man; the Second Article quote matches. P2 craft: the first sentence, the quote and the second paragraph say the same thing three times. P2 focus: "None of us knew anyone who saw him" answers a question not asked (true to witt.dw.how-the-promise-reached-us). P2 access: a 32-word sentence. |
| 2 | What did he do? | PASS | concern | pass | concern | pass | no | Redemption, then justification, from witt.term.justification ("accounted" and "made" righteous, as its plain_meaning says). P2 rigor: "He took our place under God's judgment" is not in the cited record's text. P2 craft: the creed lines repeat Q1, here unquoted; "That is what he did, and why he came" shipped as "withhold". |
| 3 | A word I might not know | PASS | pass | concern | concern | pass | no | Testament as a gift left by someone about to die, from witt.term.promise-and-testament; presence "in and under", no theory of the how, the heated iron, all from witt.term.sacrament-of-the-altar. The engine removed a typed Augsburg quote with no residue. P2 craft: the justification paragraph repeats Q2 word for word. P2 access: an 8-sentence paragraph. |
| 4 | Why did your people believe this? | PASS | concern | concern | concern | concern | no | Scripture as judge, and Augsburg II on inborn sin, faithful to witt.dw.born-in-sin-fed-at-the-table. P2 rigor: the second reason ("No one had to teach a child to be selfish... The Law exposed it, and the Gospel answered it") is in no record; two sentences shipped as "withhold". The child line is a modern idiom. P2 focus: "this" after Q3 was the Supper and justification; the answer turns to original sin. P2 access: a 44-word sentence quoting the confession. |
| 5 | Someone who lived this out | FAIL | fail | pass | fail | fail | no | P1 damaged: the engine removed the voice's typed quotation of the poor-man warning, and the reply still points to it ("Here is what the program itself shows. That is not gentle language."; "opened the door to the poor man"). P1 focus: no one is shown living anything out. The opening limit is true to witt.limit.record-thinnest, but the records hold named people the question could reach: witt.story.brussels-martyrs, witt.story.return-and-the-eight-sermons, witt.story.household-and-kate-on-prayer. |
| 6 | What I haven't asked | PASS | concern | concern | concern | concern | no | The founder's complaint kept as testimony, with no parish report beside it (1522, 1529, Katharina's table question), faithful to witt.dw.cold-and-careless-among-us and its not_for. The sword quote matches and its lead-in is accurate. P2 rigor and focus: a 1525 warning to the princes is set in an answer about coldness of faith, outside the quote's retrieve_when (the Peasants' War). It is not tied to anything, so it is out of context rather than misused. P2 access: three sentences over 25 words; the reply is 384 words. |

## Side by side with the older test (13 October, older data)

| Q | Older answer (13 Oct) | New answer (29 Oct) | New is | Why |
|---|---|---|---|---|
| 1 | One short paragraph: truly God and truly man, "my Lord", Christ the one Mediator. | The same, plus the whole Second Article quote and an unasked line about witnesses. | Same | Same substance. The new one is better sourced but says the same thing three times. |
| 2 | Redemption and its cost, then the judgment at the end. Short and on topic. | Redemption, then justification, then the creed again. | Same | Both are faithful. The new adds justification but repeats Q1. |
| 3 | Buße (repentance) and the first thesis, well explained, then an unrelated Augsburg quote on original sin attached at the end. | Testament and the Supper, then justification (a repeat of Q2). | Better | No misplaced quote. Testament is a real world-word and is explained well. |
| 4 | The Word from outside, real presence, faith alone; ends with the whole creed quote attached after a colon. | Scripture as judge, then original sin, with a modern-sounding second reason. | Worse | The older answer stayed on what "this" was. The new one turns to original sin and gives a reason no record holds. |
| 5 | The Brussels martyrs of 1523 and Luther's ballad, with an honest note on what the song adds. | An honest limit, then text that points to a quote the engine removed. | Worse | The older answer named real people from the record. The new one is damaged and names no one. |
| 6 | The founder's complaint as testimony, the eight sermons of 1522, Katharina's question. | The same complaint and question, without the eight sermons, plus a long 1525 quote out of context. | Worse | The older answer held together. The new one adds 120 words that do not belong. |

**Overall.** This world looks somewhat worse than in the older test: one answer better, two the same, three worse. The doctrine is still right and plainly said. But the new conversation repeats itself, and quotes are cut or placed out of context. What changed in the system between the two runs is not known to this review; only the text is described here.

## Findings and fixes at the source

**P1**

- **Removed quote leaves the reply pointing at nothing (Q5).** Engine (lpc E1): when the voice types a quotation that a quote record holds (`witt.quote.the-poor-man-who-comes-to-you`), the engine should place the record or redraft, not delete it and ship the rest. Retrieval: "someone who lived this out" should offer a story (`witt.story.brussels-martyrs` and the others above) ahead of `witt.limit.record-thinnest`.

**P2**

- **Repetition across turns (Q1-Q3).** Engine (lpc R-1): a conversation-level check that rewrites a sentence already shipped in an earlier turn, for term and witness text as well as stories.
- **Quote out of context (Q6).** Engine (lpc E5): placement should check the turn against the quote's `retrieve_when`. The sword quote is for questions about the princes in 1525.
- **Reasons no record holds (Q4).** Engine (lpc E3): sentences marked "withhold" should be held for a grounded redraft.
- **Long sentences (Q4, Q6).** Paragraph and sentence rules in the prompt; a paragraph measure in `engine/m7/turn_readability.py` (lpc A1).

NEW: PASS 5, FAIL 1, NOT SCORED 0 of 6; versus older: better 1, same 2, worse 3
