# Early pass on the 106 questions: report

An early records-only pass, not the Stage 4 proof (Decision-Log 35, `Change_Order_Early_Pass.md`). lpc, shadow only, free, in-plan: no metered call. Voice drafts, classifications, judge reads and reader scores were made by Claude Code helpers. The model behind the judges, the readers and the drafts is the same vendor, so agreement among them is not independent evidence. Sealed probes appear by id only. The scoring sheet is `runs/early-pass-1/sheet.csv`; every number below comes from the run files behind it.

## What ran

106 questions answered, none left unanswered: 28 sealed probes (group A), 72 others, 6 fit traps (group K). 16 revision drafts followed the 106 first drafts. Context for the voice came from line windows around each record's cited lines, not from Stage 2.

## Machine measures

| | Sealed probes (28) | Others (72) | Fit traps (6) |
|---|---|---|---|
| Sentences cut by the net | 8 | 28 | 0 |
| Orphan flags | 1 | 2 | 0 |
| Answers with a quote placed | 25 | 56 | 2 |
| Lead-ins repaired | 3 | 1 | 0 |
| Stories placed whole | 1 | 13 | 2 |
| Mean words | 247.0 | 192.3 | 160.7 |
| Mean FK grade / reading ease | 6.8 / 75.1 | 6.3 / 76.8 | 6.1 / 77.9 |

Beside the earlier baseline on the same 28 sealed probes (cuts 45, orphan flags 13, words 233, FK 6.5, reading ease 74.0): 8 cuts, 1 orphan flag, 247 words, FK 6.8, reading ease 75.1. This is not like for like. The baseline was a live voice on the saved fleet drafts; here the voice is in-plan helpers answering to a different directive, on lpc only.

Stories: 16 answers placed a story whole; 13 at short length, 1 at medium, 2 at full. (The sheet's `stories_placed` column counts shipped story sentences, not stories.)

## The fit step

99 placed quotes and stories judged: 27 fit, 29 fit partly, 43 off the point, none unreadable. The fit step would keep 53 and drop 46. Many of the drops are placements the draft directive required ("place one quote") where the helpers reported that no offered quote fit.

## Judge steps against the gates

503 draft sentences bound to a record: the gates kept 462 and withheld or removed 41.

**Correction.** An earlier version of this section said 100 of the 462 kept sentences were not supported. That figure was overstated. The judges' evidence pack left out fields the voice is shown (a world-core record's horizon, thinness, cautions and living traditions; a story's tellings and absent_detail), so judges and readers marked sentences unsupported when the support sat in those fields. The pack was fixed in PR #1383 and all 503 sentences were judged again, free and in plan, with the fixed pack. Both judges ran again; a third blind read settled the 19 sentences where they split (two of three).

| Gate decision | Old pack: supported | Old pack: not supported | Fixed pack: supported | Fixed pack: not supported |
|---|---|---|---|---|
| Kept (462) | 362 | 100 | 404 | 58 |
| Withheld or removed (41) | 28 | 13 | 31 | 10 |

So with the fixed pack, 58 gate-kept sentences are labelled not supported, and 31 of the 41 the gates withheld are labelled supported. The 58 have not been read for kind (the Representative's own framing lines against real overreach).

**What does not carry over.** The held-out judge numbers (recall 0.885, false alarms 3.3% and 9.1%) were measured with the old pack, against gold labels made with the old pack. On 30 gold items bound to world-core and story records (13 labelled unsupported), the fixed-pack judges flagged 7 of 13 where the old-pack judges flagged 12 and 13. Six of the gold-unsupported items were read: in five, both judges quote a field the old pack hid that states the sentence; in one, only the verifier does. The gold labels on these record types are therefore suspect, not the new judges. On 30 control items bound to other record types, nothing changed. Until those gold items are re-labelled, the held-out numbers are not established for world-core and story records.

## Blind readers (two of three agree)

Two blind reads of every answer; a third on the 64 answers where they split on 117 cells. One cell had three different marks and is `unresolved` on the sheet.

- Pass 95, fail 11 (sealed probes 5, others 6, fit traps 0).
- Serious fabrication: 0. Minor: 35.
- Answers the question asked: yes 70, partly 31, no 5.
- Fit of the placed quote or story to the question: fits 34, partly 36, off point 25, nothing placed 10, unresolved 1.
- Rigor weak 34. Focus fail 7, weak 46. Accessibility, craft: almost all pass.

`still_works` is blank. The run files do not show a mark, hover or click-through working.

## What broke

- The voice helpers' file reader cut the shared system file at line 427 of 616, so the first 106 drafts never saw the later witnesses, gravities and stories. All 106 were redrafted with the whole file. The first attempt is kept outside the repo.
- The first reader packets cut record text and left several record types empty. All reads were redone on corrected packets.
- The context window cut any cited span over 450 words and added nothing around it (found by the Opus review of the fit step). Fixed; 13 fit judgments and 10 calibration pairs were rejudged; one fit verdict changed and the calibration did not.
- The guard added for `ctx.` tags let a typed quotation through uncited. It was a fix on a fix; removed. No draft in this run used a `ctx.` tag.
- q086 ("Just answer yes or no") ships an empty answer, reproducibly, although the voice's draft was a plain decline. Cause: the answerer ignored the engine's set-aside flag; fixed in PR #1382 (OG-122, OG-125).
- Not run: the three replay benches that read the fleet-graded-run format (`S1-L2/bench.py`, `S3-Stories/story_bench.py`, `S1-01-free/saved_scores.py`) and `engine/m7/standing_measure.py`; the sheet carries the same measures for this run.
