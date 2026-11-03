# CP.9 cross-world re-test, 2026-11-02: results

Settings were frozen before any run (`Frozen.md`). Arms: A the old engine's saved answers; B the current engine without the passage offer; C the current engine with the passage offer (and the C5 split ids in lpc's catalogue). 28 sealed questions per world, helpers standing in for every model call, no spend. One Opus reader per world rated the 84 answers blind (A, B, C shuffled together, seed 20261102). Per-world files: `<world>/rate_*_items.json` (what the reader saw), `rate_*_key.json` (which arm), `rate_*_rated.json` (the ratings), `<world>/<arm>/` (voice drafts, reads, rewrites, re-reads, final answers). `unblinded.json` holds every rating with its arm. `helper_notes.md` lists what the helpers reported about their own work.

## Whole set, 28 questions per world

Answers the question yes/partly/no; depth rich/adequate/thin/flat; accuracy ok/tier 3/tier 2/tier 1.

| World | Arm | Answers yes/partly/no | Depth r/a/t/f | Plain | Speaks as the community | Accuracy ok/t3/t2/t1 |
|---|---|---|---|---|---|---|
| lpc | A | 18/10/0 | 10/13/5/0 | 25 | 25 | 13/9/4/2 |
| lpc | B | 19/6/3 | 3/19/3/3 | 24 | 24 | 22/3/3/0 |
| lpc | C | 15/8/5 | 3/14/6/5 | 25 | 19 | 22/2/4/0 |
| alx | A | 26/2/0 | 20/8/0/0 | 26 | 26 | 11/11/6/0 |
| alx | B | 15/6/7 | 2/13/7/6 | 27 | 28 | 14/6/8/0 |
| alx | C | 20/6/2 | 1/20/5/2 | 27 | 28 | 16/9/3/0 |
| syr | A | 26/1/1 | 16/11/1/0 | 27 | 23 | 19/7/2/0 |
| syr | B | 17/10/1 | 2/19/6/1 | 23 | 26 | 16/9/3/0 |
| syr | C | 18/5/5 | 4/18/2/4 | 27 | 26 | 13/10/5/0 |
| rzg | A | 24/4/0 | 17/10/1/0 | 28 | 28 | 15/9/3/1 |
| rzg | B | 11/13/4 | 2/13/11/2 | 27 | 26 | 18/3/7/0 |
| rzg | C | 12/12/4 | 3/14/9/2 | 26 | 25 | 18/2/8/0 |

## Strata

Seeded = the question's reader-named sub-question had passages offered in arm C. lpc: 5 seeded (q012, q017, q018, q022, q028); rzg: 4 (q014, q018, q022, q028); alx and syr: 0 (no passage passes the lens: every seed is file-level only). C5-touching: lpc 3, alx 2, syr 2, rzg 2.

| World | Stratum | Arm | Answers yes/partly/no | Depth r/a/t/f | Accuracy ok/t3/t2/t1 |
|---|---|---|---|---|---|
| lpc | seeded (5) | A | 3/2/0 | 1/4/0/0 | 3/2/0/0 |
| lpc | seeded (5) | B | 4/1/0 | 1/4/0/0 | 3/2/0/0 |
| lpc | seeded (5) | C | 3/1/1 | 2/1/1/1 | 3/1/1/0 |
| lpc | not seeded (23) | A / B / C | 15/8/0 ; 15/5/3 ; 12/7/4 | 9/9/5/0 ; 2/15/3/3 ; 1/13/5/4 | 10/7/4/2 ; 19/1/3/0 ; 19/1/3/0 |
| rzg | seeded (4): too few to read | A / B / C | 3/1/0 ; 1/3/0 ; 2/2/0 | 2/2/0/0 ; 0/2/2/0 ; 1/3/0/0 | 1/2/1/0 ; 3/0/1/0 ; 2/0/2/0 |
| rzg | not seeded (24) | A / B / C | 21/3/0 ; 10/10/4 ; 10/10/4 | 15/8/1/0 ; 2/11/9/2 ; 2/11/9/2 | 14/7/2/1 ; 15/3/6/0 ; 16/2/6/0 |
| alx, syr | not seeded (28) | see the whole-set rows | | | |
| lpc C5 (3) | A / B / C | 2/1/0 ; 2/1/0 ; 2/0/1 | 1/1/1/0 ; 0/2/1/0 ; 1/1/0/1 | 1/2/0/0 ; 2/1/0/0 ; 2/0/1/0 |
| alx C5 (2) | A / B / C | 2/0/0 ; 0/1/1 ; 2/0/0 | 2/0/0/0 ; 0/0/1/1 ; 0/2/0/0 | 0/2/0/0 ; 0/1/1/0 ; 1/1/0/0 |
| syr C5 (2) | A / B / C | 2/0/0 ; 0/2/0 ; 2/0/0 | 2/0/0/0 ; 0/0/2/0 ; 0/2/0/0 | 1/1/0/0 ; 1/1/0/0 ; 2/0/0/0 |
| rzg C5 (2) | A / B / C | 2/0/0 ; 1/1/0 ; 1/1/0 | 2/0/0/0 ; 1/1/0/0 ; 0/2/0/0 | 2/0/0/0 ; 1/1/0/0 ; 1/1/0/0 |

## Noise floor

In alx and syr, arms B and C had the same offer (no passages), so their difference is helper noise: answers "yes" 15 against 20 in alx, 17 against 18 in syr. In the unseeded questions of lpc it was 15 against 12, and in rzg 10 against 10. On net counts the spread is about five questions on "yes", so a move of three on one count is inside the noise.

Per question the noise is larger. With identical inputs, the alx ratings of B and C differ on the answers-the-question label for 8 of 28 questions, on depth for 11 and on accuracy for 14; syr differs on 7, 10 and 9. No single-question rating is used as evidence.

## What happened to the offered passages

lpc: 9 passages offered over the 5 seeded questions; the helpers' drafts bound no sentence to any of them (0 of 9 used). rzg: 5 passages offered over 4 seeded questions; 6 passage-bound sentences in 2 questions, none struck by the read. The offer did not change the lpc answers because it was not used; the rzg answers used it twice.

## Success rule, per world (set before the run)

- lpc: the passage offer was not tested. The helpers' drafts bound none of the 9 offered passages, and five seeded questions are under any floor that could show an effect. The unseeded stratum moved from 15 to 12 on "yes", which is inside the helper noise.
- rzg: too few to read (4 seeded questions, under the floor of 5).
- alx, syr: no passage was offered; no test of the offer. They are the controls and show the noise floor above.
- Depth: the old engine (A) carries more in every world, rich 10 to 20 against 1 to 4 in the new arms. The writer differs (a live model for A, helpers for B and C), so this shows direction, not size.
- Answers the question: "yes" is 18 to 26 of 28 for A against 11 to 20 for B and C. In lpc, B scored 19 against A's 18, so the old engine does not lead there.
- Accuracy is mixed. Tier 1 is 0 in B and C against 3 in A (lpc 2, rzg 1). Tier 2 summed over the four worlds is 15 for A, 21 for B and 20 for C. The baseline run the day before gave 1 tier 2 answer across the four worlds for a nearly identical engine, so most of the tier 2 swing is the reader, and one-reader accuracy ratings cannot be compared between runs.

## Limits (read before using the numbers)

- One run per world, one Opus reader per world (the alx and syr readers finished in about 90 seconds with 7 to 8 tool calls, so their accuracy checks were light), helper-written drafts, reads and rewrites; the old engine's writer differs, which confounds voice, plainness and depth most.
- Several helpers were stopped by an API safeguard and redid their work; some drafted from part of their ground; one lpc draft omitted material (see `helper_notes.md`). One lpc arm-B draft (q013) was written from the arm-C answer. One re-read list was run by two helpers.
- Only 9 of 112 questions across the two seeded worlds had a passage offered, and the lens rule offers nothing in alx and syr until their shelf rows are narrowed. The re-test therefore measures how the engine meets an unorganised shelf more than it measures the passage offer.
- The fitting-record-in-the-offer column promised in `Frozen.md` was not run; not done.
- In lpc the passages sat last in each offer (positions 12 to 14 of 13 to 15 entries), and several helpers read only part of their ground, so they never saw them.

## Corrections, 2026-11-03

An independent Opus read re-counted every table from the raw rating files; the tables are exact. These statements in the first version were wrong or overstated and are corrected above: "lpc: not met" (read as "passages do not help"; the offer was not tested); "tier 2 similar" (15, 21, 20); "the old engine still answers better in every world" (lpc "yes" 19 for B against 18 for A); "more than helper noise" for the 15 to 12 move; and the noise floor, which holds for net counts and not for single questions. The retrieval relevance measure in `relevance-measure/` (18 of 159 passages rated "yes") used keyword search only, removed the known-good passages, kept the top 3 and showed raters the first 170 words of each passage; it is a floor for the weakest search and not a verdict on search.
