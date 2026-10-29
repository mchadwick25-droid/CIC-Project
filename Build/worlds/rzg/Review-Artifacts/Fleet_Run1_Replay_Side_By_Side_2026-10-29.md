# rzg fleet graded run 1, six-question replay (29 October): grades and side-by-side

## Verdict

**Revise.** Four of six answers pass with small defects. Two fail.

- **Q2 (What did he do?)** makes Jesus the one who chose the saved: "what he did before any of it: he chose, by God's own free will and before the world began, who would be saved." The cited record (`rzg.witness.one-thing-not-in-dispute`) says "God's own free choice". It speaks of who is chosen "in him", not of Christ's own act. The answer then never says what his death did. The older answer gave the cross and the Supper. Calvin does call Christ the author of election in one place (Institutes III.22.7), but no record here says so. As an answer to "what did he do", it misleads.
- **Q3 (a word I might not know)** fails the project's per-turn reading floor: FRE 56.3, under 60 (`engine.m7.turn_readability` reports it as failed). It also states the Consistory's weekly meetings flat, though the world's own thinness statement rates that detail Confidence E until the 1541 Ordinances are acquired.

The voice is steady and plain. It names what is distinct about this world (election held as comfort, not threat; Christ as the mirror) and what it does not have (no chain of memory to Christ). No claim goes past 1650. The one placed quote is used as its record intends.

## Scope and checks

- **Run.** Fleet graded run 1, replay, 29 October. Package `packages/rzg/2026-10-28T03-51-19Z`. Voice: Sonnet 4.5. One conversation of six questions.
- **Read in full.** All six shipped `voice_event.text` answers, their citations, `reply_shape.placed` and `removed`, and the grounding verdicts. No turn went to the Facilitator. `output_defects` is empty and `answer_record_fallback` is null in all six.
- **Quotes.** The one placed quote (`rzg.quote.seniors-selected-from-the-people`) matches its `modern_rendering` exactly, checked by script. Its lead-in was read against its `not_for` (discipline was not clergy-only, and elders did not act apart from pastors). Both are kept.
- **Records.** Claims checked against `repository.json`, the world_core cautions in `prompt.txt`, `records/worlds/rzg.yaml` (thinness statement), and the not_for lists of every cited record.
- **Readability.** `engine.m7.turn_readability.report_turns` and `engine.m1.gates.grade_text` on each shipped reply. Sentence and paragraph counts by script.
- **Truncation.** Two methods: every reply ends on closing punctuation, and no reply has `degraded` or `degraded_by_net` set. No truncation.
- **Older data.** `engine/m4/reports/live-turn-report-rzg-2026-10-13-eleven-world-test.json` (13 October, package `2026-10-13T20-51-19Z`) is older data from a different engine and format. It is read qualitatively only and is not scored.
- No model was called. No git command was run. Only this file and its `.counts.json` were written.

## Readability (new answers)

| Q | Words | FK | FRE | Longest own sentence | Over 25 | Sentences per paragraph |
|---|---|---|---|---|---|---|
| 1 | 169 | 6.5 | 76.0 | 24 | 0 | 4, 4, 3 |
| 2 | 157 | 7.0 | 72.9 | 35 | 1 | 4, 3, 3 |
| 3 | 132 | 8.1 | **56.3** | 20 | 0 | 4, 2, 5 |
| 4 | 160 | 8.7 | 64.0 | 26 | 1 | 4, 5 |
| 5 | 139 | 7.9 | 60.8 | 29 | 1 | 4, 4, 3 |
| 6 | 175 | 6.7 | 77.8 | 47 | 1 | 5, 1, 4 |

Q3 fails the FRE 60 floor. Q5 clears it by 0.8. Paragraphs are short throughout, which is better than most worlds.

## Grades (new answers)

Criteria: Rigor, Accessibility, Craft, Focus. `pass`, `concern` (P2: small, fixable) or `fail` (P1: wrong, invented, misleading or damaged). A row with only P2s is PASS.

| Q | Question | Result | Rigor | Access | Craft | Focus | Fabrication | Notes |
|---|---|---|---|---|---|---|---|---|
| 1 | Who is Jesus? | PASS | pass | pass | pass | pass | no | What the whole church says, then what is distinct: election in him, Christ the mirror, all from rzg.witness.one-thing-not-in-dispute and its not_for (no distinct Christology). The creed sentence shipped untagged ("withhold"), but it is the shared creed. Text, not memory, from rzg.witness.what-we-have-of-christ. |
| 2 | What did he do? | FAIL | fail | concern | concern | fail | no | P1 misleading: "what he did before any of it: he chose... who would be saved" makes election Christ's own act. The cited record says God's free choice, of who is chosen in him. P1 focus: nothing on what his death did. P2 rigor: the life summary ("taught, healed... appeared to his followers") shipped as "withhold". P2 craft: the mirror line repeats Q1. P2 access: a 35-word sentence. |
| 3 | A word I might not know | FAIL | concern | fail | pass | pass | no | Consistory, from rzg.term.consistory; Zurich had no such body; the 1555 independence matches rzg.gravity.council-led-authority-vs-consistorial-independence. The tension is held open. The Calvin quote matches and keeps its not_for. P1 access: FRE 56.3, below the floor of 60. P2 rigor: "meeting weekly" is cited to rzg.term.excommunication, which does not hold it; the yaml rates the weekly operation Confidence E. "Censures" is not explained. |
| 4 | Why did your people believe this? | PASS | concern | concern | pass | pass | no | Two plain reasons: Scripture taught it, and only a ground outside the self can hold. The first fits rzg.term.predestination-election (Zwingli works through Romans). The second fits the mirror teaching of the Second Helvetic Confession. P2 rigor: the Romans sentence and "the only place a mind could finally rest" shipped as "withhold"; "before the world began" is closer to Ephesians than Romans. P2 access: a 26-word sentence; one 5-sentence paragraph. |
| 5 | Someone who lived this out | PASS | concern | pass | concern | concern | no | Bullinger, 1531-1575, Kappel, the Second Helvetic Confession and 1549, all in the records (rzg.core..., rzg.term.confession-of-faith, rzg.source.second-helvetic-confession). P2 rigor: "longer than anyone else in our record" and "without changing its shape" (withheld) are uncited judgments. P2 focus: a career summary, not a life shaped by election; the world has no Tier 2-4 stories, so a thin answer is expected. P2 craft: "What he lived out was steadiness" is a tidy closer. |
| 6 | What I haven't asked | PASS | concern | concern | concern | pass | no | Text, not memory, and Zwingli's rule to be taught better only from Scripture, from rzg.witness.what-we-have-of-christ; Calvin and Farel at Zurich, from rzg.story.calvins-journey-to-zurich. P2 craft: the first paragraph repeats Q1 almost word for word, and 1549 repeats Q5. P2 rigor: "Both cities tested their own teaching against the text" is a gloss; the story says Calvin judged they already agreed. P2 access: a 47-word sentence. |

## Side by side with the older test (13 October, older data)

| Q | Older answer (13 Oct) | New answer (29 Oct) | New is | Why |
|---|---|---|---|---|
| 1 | The same content in one 12-sentence block, plus a line on what was contested (the Supper, who belongs). | The same content in three short paragraphs. | Better | Same words and the same care, but much easier to read. |
| 2 | Without sin, punishment borne, one sacrifice, risen; then the Supper, neither sacrifice repeated nor body confined. | Life summary, then election as Christ's own act, then the mirror again. | Worse | The older answer said what he did, from the records. The new one shifts election onto Christ and leaves out the cross. |
| 3 | Providence, in one long block, with one unsupported line on Zurich's "briefer, pastoral" form. | Consistory, distinctive and with a matching quote, but under the reading floor. | Same | More distinctive and better laid out, but it fails FRE 60 and states the weekly meeting flat. |
| 4 | Election from Scripture, standing on God not self, Bolsec in 1551, in one long block. | Two clear reasons in two paragraphs, no Bolsec. | Same | Clearer, a little thinner. Neither invents. |
| 5 | Calvin: arrival in 1536, exile, recall in 1541, the Institutes, 1549, then an honest limit. | Bullinger: the long pastorate, the Second Helvetic Confession, 1549. | Same | Both are career summaries from the records. The older one ended on an honest limit; the new one ends on a tidy closer. |
| 6 | The triple refusal (Rome, Wittenberg, the Anabaptists within), with the city's later use of force named plainly. | Text, not memory (a repeat of Q1), then 1549 (a repeat of Q5). | Worse | The older answer gave something new and hard. The new one repeats earlier turns. |

**Overall.** This world looks slightly worse than in the older test: one answer better, three the same, two worse. Layout and plainness are clearly better. The new conversation repeats itself, and one answer moves a doctrine onto the wrong subject. What changed in the system between the two runs is not known to this review; only the text is described here.

## Findings and fixes at the source

**P1**

- **Election made Christ's own act (Q2).** Record: add to `rzg.witness.one-thing-not-in-dispute` the not_for "a claim that election was Christ's own act, or that it is what he did, in place of his death and rising". Retrieval: "what did he do" should reach `rzg.witness.one-supper-two-poles` and the shared confession, as the older answer did. This witness is about who is chosen.
- **Under the reading floor (Q3).** Engine (fleet run 1 A1): the m3 harness should run `engine.m7.turn_readability` on each shipped turn and fail the turn on a hard fail. Record: give `rzg.term.consistory` a plainer form of "censures" and "discipline body". Uncited "meeting weekly": the grounding net should hold a specific claim cited to a record that does not hold it.

**P2**

- **Repetition across turns (Q1, Q2, Q6).** Engine (lpc R-1): a conversation-level check for sentences already shipped.
- **"Withhold" sentences ship (Q2, Q4, Q5).** Engine (lpc E3): hold them for a grounded redraft.
- **Long lead-in sentences (Q2, Q6).** Sentence rule in the prompt.

NEW: PASS 4, FAIL 2, NOT SCORED 0 of 6; versus older: better 1, same 3, worse 2
