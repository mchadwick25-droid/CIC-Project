# Stage 3 Change Order: the quote door and the stories door, proved on lpc

Approved by Mark, 2026-10-29 (choice box, direct; version 4 of the draft, as written here). Decision-Log entry 15 on branch `claude/stage1-decision-log-stories` records the approval. Live-path numbers do not wait for a working live voice call: they are measured on the saved drafts and the 100-question lpc test now, and live at stage 4.

## Scope

Engine and data path only. No layout, styling or screen redesign: screen layout is dealt with after the system works, and layout improvements are a later item, not part of this order. Anything new (a story's inline position, a quote's card data) reaches the screen as data through the existing display, not a new design.

## What changes

Quote door:
- The voice marks a quote by record or span id. Code inserts the reviewed rendering and writes the lead-in that names the speaker from the record. The model never types a quotation.
- A rendering is never presented as the source's words. The card shows three labelled layers: the spoken modern rendering, the edition words with translator and date, and the original's locus where held. The voice frames it in speech ("in today's English, he says").
- Open question, not approved: whether the quote card may carry the edition words. Today a quote card carries the spoken rendering and the source reference and no original wording, and a test asserts it. Mark has left this undecided; the rule and its test stay as they are until the coordination thread brings it back when the quote door is ready to build and is blocked on it.
- Every spoken rendering gets full review before it can be spoken (proposal decision 7, ruled yes), and renderings are written by Opus, in plan and not by API (decision 2d, ruled yes).

Stories door:
- Only a reviewed story record tells a story in the voice. Nothing is invented. The index may show the source division on the card for reading; the voice never retells from the passage.
- Each story record carries reviewed tellings at more than one length and a plain statement of its heart, reviewed against the full record. The voice picks the fit for the question. A shortened or reshaped telling is allowed if the heart and source context hold, nothing is added, it reads at B2 and conversation length, and it is a direct example that answers the question (Mark, 2026-10-29).
- A live retelling fitted to one question runs only under the bound-draft path (stage 4): each sentence bound to the record sentence it rests on and verified. If it fails, the voice falls back to a reviewed telling.

## Before it starts

- Stage 2 (Library additions) done on lpc. Not done; it is the Library thread's next priority. Free work on this order proceeds meanwhile.

## The numbers it must move

Baselines come from the free replay of the 308 saved drafts of fleet graded run 1 (`S1-L2/S1-L2_Result.md`, `S3-Stories/Stories_Replay_Result.md`, `S1-01-free/S1-01_Free_Measures.md`). The lpc figures are lpc's 28. The replay ceiling is what code placement reached on the same drafts; it is not a live result. The test is 100 lpc questions (Mark, 2026-10-29).

Quotes: the quote door passes on lpc if, on the 100 lpc questions, there are fewer cut sentences and fewer orphan flags than today, more quotes placed by code, and readability and answer length are no worse. Mark also reads the 30-draft fit sample.

| Measure | All 11 worlds today | lpc today | Replay ceiling (all / lpc) | Target |
|---|---|---|---|---|
| Answers with a quote placed by code | 39 of 308 | 4 of 28 | 124 / 10 | More than today |
| Sentences cut because the lead-in did not name its speaker | 81 | 8 | 4 left | Counted in total cuts |
| Quotations typed by the voice and cut | 42 | 15 | 42 (unchanged) | Counted in total cuts |
| All cuts, and orphan flags (heuristic) | 297 and 85 | 45 and 13 | 203 and 52 / 39 and 13 | Fewer cuts and fewer orphan flags than today |
| Words per answer | 265 | 233 | 290 (all) | No worse than today |
| Readability (Flesch-Kincaid grade / reading ease, mean) | about 7.1 / 71 | 6.5 / 74.0 | not measured | No worse than today |

Stories:

| Measure | All worlds today | lpc today | Target |
|---|---|---|---|
| 1. Stories marked inline in the text | 1 placed by code in 308 answers (desert only) | 0 of 28 | All of them (100%) |
| 2. Stories told from a reviewed record only | at most 115 of 183 voiced story sentences restate their record by a word-overlap screen; nothing verifies them | 9 of 11 | 100% from a reviewed record |
| 3. Story sentences cut by the current gates | 29 (28 on desert) | 0 | No target set; reported |
| 3a. Orphan flags in drafts that lost a story sentence | 4 in 8 drafts | 0 | No target set; reported |
| 4. Faithfulness of a shortened or reshaped telling | cannot be measured yet; no shortened tellings exist | | Every event kept and nothing added. Zero tolerance for added content. |

Faithfulness is measured on each reviewed telling and on a human-read sample of about 20 retellings for Mark.

## Three-level transparency, kept

Binding (Mark, 2026-10-29): highlighted or marked text in the answer; hover for brief context; click for the full page with links to the source references and the source documents. Nothing a reader has today is removed: lexicon highlighting with hover and click-through, the citation marker with its sourcing links, and access to the vendored texts behind every cited sentence. A placed quote and a told story each get the same three levels, with the click-through linking to the source span and its vendored document.

First-task finding (code read, 2026-10-29; see `S3-Stories/Transparency_Path_Check.md`): stories do not sit under one end-of-answer marker. The engine places a story's mark inline at the end of its telling run, and the app shows an inline mark, a hover (title, source, a plain confidence phrase) and a click (source list). A story drops to the end references only when an answer carries more marks than the cap allows (stories drop before quotes). What is dropped before the screen: a story card carried no brief meaning and no narrative tier (the records have both; the engine never read the tier); the hover shows only the formation-confidence phrase, not the record's other confidence fields; and the click shows a source list, not a page for the full story.

Still-works check (done-when): on lpc, today's lexicon highlight with hover and click-through, and the citation marker with its sourcing links, work exactly as they do now on the changed path. For one answer with a placed quote and one with a told story, the response carries the data for the inline mark, the brief context, and the full-page link to the source reference and vendored document, and the existing display shows what it already can. A mark, hover, click-through or source link that works today and stops working fails the stage.

## Rules that stay

- The new path runs in shadow beside the cut step, the silence check and the withheld-claim rule. No gate is retired; retiring one is a later change order with its numbers.
- No production change and no world rebuild until lpc proves it. Each other world is switched on by its own change order with its own number and sample.
- A world that fails a number stays on the old path, the failure goes in that world's `Open_Gaps_Tracking.md`, and it is registered as a dated waiver in the accepted-open list.
- Everything the voice speaks meets the B2 standard, renderings included.

## Done when

1. Each number above is measured on 100 lpc questions, on the live path, and reported beside its baseline.
2. The still-works check passes.
3. Every rendering and every telling used on lpc has passed full review, and Mark has read the human sample of about 20 retellings and the 30-draft quote fit sample.
4. Failures, if any, are entered as the rules above require.

## Later, not in this order

Screen layout and styling improvements for the inline story mark, the quote card and the three levels. Mark has said there are several, and they come after the system works.
