# alx fleet graded run 1, six-question replay (29 October): grades and side-by-side

## Verdict

**Revise.** Four of six answers pass with small defects. Two fail.

- **Q2 (What did he do?)** retells Clement's story of John and the young robber, and adds a detail no record or source holds: "He called the young man by name." The young man is unnamed in the record and in Clement. The story also answers a question about Jesus with a story about John.
- **Q5 (someone who lived this out)** gives a vague sketch of Clement, a figure the record marks as not narratable. The engine cut the three sentences that held his teaching. What shipped is two sentences the grounding net marked "withhold", plus an invented line: "That was not popular with everyone."

At its best the voice is clear and its own. Q3 (logikos) holds the contested part as contested, and Q6 names the record's literate bias without being asked.

## Scope and checks

- **Run.** Fleet graded run 1, replay, 29 October. Package `packages/alx/2026-10-28T03-49-20Z` (the current registry pin). Voice: Sonnet 4.5. One conversation of six questions; each later turn replays the earlier ones.
- **Read in full.** All six shipped `voice_event.text` answers, their citations, `reply_shape.placed` and `removed`, and the grounding verdicts. No turn went to the Facilitator. `output_defects` is empty and `answer_record_fallback` is null in all six.
- **Quotes.** The three placed quotes (clement-new-song, athanasius-made-god, appointed-by-the-fathers-to-be-read) match their `modern_rendering` exactly, checked by script. Each lead-in was read against its `not_for`.
- **Records.** Claims checked against `repository.json`, the world_core cautions 1-5 in `prompt.txt`, and the not_for lists of every cited record. The John story was also checked against the vendored Clement text (`cic/texts/anf02_...clement-alexandria.xml`, Quis Dives 42).
- **Readability.** `engine.m1.gates.grade_text` on each shipped reply. Sentence and paragraph counts by script, with placed quotations left out of sentence length.
- **Truncation.** Two methods: every reply ends on closing punctuation, and no reply has `degraded` or `degraded_by_net` set. No truncation.
- **Older data.** `engine/m4/reports/live-turn-report-alx-2026-10-13-eleven-world-test.json` (13 October, package `2026-10-13T19-47-30Z`) is older data from a different engine and format. It is read qualitatively only and is not scored.
- No model was called. No git command was run. Only this file and its `.counts.json` were written.

## Readability (new answers)

| Q | Words | FK | FRE | Longest own sentence | Over 25 | Sentences per paragraph |
|---|---|---|---|---|---|---|
| 1 | 231 | 7.4 | 73.2 | 36 | 1 | 2, 7 |
| 2 | 207 | 4.4 | 85.3 | 24 | 0 | 1, 4, 12 |
| 3 | 154 | 6.4 | 73.4 | 32 | 2 | 3, 3, 5 |
| 4 | 169 | 6.7 | 71.5 | 34 | 1 | 5, 7 |
| 5 | 117 | 6.0 | 77.6 | 26 | 1 | 2, 3, 3 |
| 6 | 301 | 7.3 | 68.1 | 30 | 1 | 1, 6, 7, 1, 1, 1 |

All six clear FK 10 and FRE 60.

## Grades (new answers)

Criteria: Rigor, Accessibility, Craft, Focus. `pass`, `concern` (P2: small, fixable) or `fail` (P1: wrong, invented, misleading or damaged). A row with only P2s is PASS.

| Q | Question | Result | Rigor | Access | Craft | Focus | Fabrication | Notes |
|---|---|---|---|---|---|---|---|---|
| 1 | Who is Jesus? | PASS | pass | concern | concern | pass | no | Logos come in flesh, from alx.dw.jesus; the New Song quote matches and its lead-in is fair. Nicaea and homoousios are placed in "our last years", as alx.dw.was-jesus-god says; within the 400 horizon. P2 craft: "He meant that... By that we meant that..." stacks two glosses; the engine cut the Athanasius line ("second placed quote"). P2 access: a 36-word sentence on Arius and Nicaea. |
| 2 | What did he do? | FAIL | fail | concern | concern | fail | yes (small) | Opening is right (Athanasius quote matches; "doctor entering the sickness" is the record's). P1 invented: "He called the young man by name." The record's absent_detail says the young man is unnamed; in Clement, John asks to be led to "your captain" and calls him "my son". "The bandits took him" is true to Clement but not in the record. Three story sentences shipped marked "withhold" (proper noun, no tag). P1 focus: the question is about Jesus; half the answer is a story about John. P2: a 12-sentence paragraph; "not to punishment, but to restoration" is a stock turn. The record's not_for is kept: the bishop's careless watch and the cost of return are both there. |
| 3 | A word I might not know | PASS | pass | concern | pass | pass | no | Logikos, from alx.term.logikos, with its own false-friend handled ("not because it is clever"). The contested cosmology is held as contested, and Origen is left unnamed, as the term's plain_meaning does. "Damaged... never destroyed" matches alx.term.eikon. P2 access: a 32-word sentence. |
| 4 | Why did your people believe this? | PASS | pass | concern | concern | pass | no | Witnesses and courage, from alx.dw.resurrection, without claiming proof (not_for kept). Received, not invented, from alx.force.apostolic-tradition. P2 craft: "He meant love for the Holy Word, and for the teacher who showed him the Word." is an orphan: the engine cut the Gregory lead-in, so "He" has no one to point to. P2 access: a 34-word sentence. |
| 5 | Someone who lived this out | FAIL | fail | pass | fail | fail | yes (small) | P1 damaged: the engine cut three sentences (the bee, the rich, philosophy as schoolmaster) for citing unplaced quotes. What remains is "That is what Clement himself became: a teacher whose wisdom was visible in how he loved both truth and the people he taught" (withheld, 17% grounded) after "lived this out in how he taught" (withheld, 0%). alx.figure.clement is `narratable: false` ("almost nothing of his life" survives). P1 invented: "That was not popular with everyone." No record says so. The marriage line is true to alx.limit.marriage. Nobody is shown living anything out. |
| 6 | What I haven't asked | PASS | concern | concern | concern | pass | no | Strong: the literate bias of the record, stated plainly (caution 1, alx.gravity.learning-community-tension). The Arsinoite villages line fits alx.story.arsinoite-conference. The 367 quote matches. P2 rigor: "everyone could hear the Shepherd read" goes beyond a quote about books "appointed... to be read by those who newly join us", and the quote's own divergence_note says to use it inside a transmission claim (withheld at 8% grounded). P2 access and craft: "the breadth channel" is build vocabulary; the lead-in lists the books, then the quote lists them again. |

## Side by side with the older test (13 October, older data)

| Q | Older answer (13 Oct) | New answer (29 Oct) | New is | Why |
|---|---|---|---|---|
| 1 | Short and clear: Logos in flesh, Athanasius "made man that we might be made God" in paraphrase. No quote placed. | Same core, plus the New Song quote and Nicaea's word, kept in its time. | Better | More of the world's own voice and sources, with the pre-Nicene and Nicene layers kept apart. Small P2s. |
| 2 | On topic: healing from within, death as doctor, resurrection, "He came to remake us." | Opens well, then turns to the John story with an invented detail. | Worse | The older answer answered the question. The new one drifts to John and adds a fact. |
| 3 | "ho Christos" (a word most readers know), then the New Song quote, which was also used again later. | Logikos, explained against its false friend, with the contested part held open. | Better | A real world-word, more distinctive, and it holds the contest. |
| 4 | Apostles' courage and the martyrs; one stray quotation mark left in the text. | Same argument, plus tradition received; one orphan sentence ("He meant love..."). | Same | Same substance. Each has one small piece of damage. |
| 5 | Gregory's own story of being taught by Origen; it did not move it to Alexandria. | A thin, partly invented sketch of Clement after the engine's cuts. | Worse | The older answer showed a person living it. The new one shows no one and adds a line. |
| 6 | Water, bread and scripture reached everyone; the school reached the few; God as teacher. | The same point, made more plainly about what the record can and cannot show, plus the 367 quote. | Same | Clearer on the record's limits, but the quote is stretched and "breadth channel" leaks in. |

**Overall.** This world looks about the same as in the older test: two answers better, two the same, two worse. The new answers are more grounded in the records and closer to the world's own words. In both failures, story or figure material is retold loosely or cut into fragments. What changed in the system between the two runs is not known to this review; only the text is described here.

## Findings and fixes at the source

**P1**

- **Story retold beyond its record (Q2).** Engine: a story told by the voice should be checked against its record's `telling` and `absent_detail`, as the lpc run-3 review asked (E3). A "withhold" verdict on a story sentence that names its subject should hold the sentence for a grounded redraft, not ship it. Record: add to `alx.story.john-young-robber` the not_for "naming the young man or having John call him by name".
- **A non-narratable figure made into a portrait, after cuts (Q5).** Engine: when cuts remove the sentences that carried an answer, redraft or hold back (lpc E1). Uncited specific claims marked "withhold" should not ship. Retrieval: "someone who lived this out" should reach a narratable story (alx.story.gregory-formation, alx.story.plague-nursing, alx.story.potamiaena), not alx.figure.clement, which is `narratable: false`.

**P2**

- **Orphans from cuts (Q1, Q4).** Engine (E1): an orphaned announcement or pronoun left by a removal should trigger a redraft.
- **Quote stretched (Q6).** Record: add to `alx.quote.appointed-by-the-fathers-to-be-read` the not_for "a claim about what the whole community heard read".
- **Build vocabulary (Q6).** "breadth channel" is the voice's own; the prompt's gravity wording should give it a plain phrase to use instead.
- **Unresolvable citation (Q6).** The grounding net met `alx.core.thinness`, which does not exist. Engine: the tag list offered to the voice should hold only real ids.
- **Long sentences and one long paragraph (Q1-Q4).** Paragraph rule in the prompt and a paragraph measure in `engine/m7/turn_readability.py` (lpc A1).

NEW: PASS 4, FAIL 2, NOT SCORED 0 of 6; versus older: better 2, same 2, worse 2
