# Early pass 2 (2026-10-31)

The same 106 questions as early pass 1, run again after PR #1386 (the voice may place no quote when none answers the ask). Records-only, no metered model call. Pass 2 is an early pass, not the Stage 4 proof. It is one run. The drafts are new drafts by different helpers, so some of every change below is draft-to-draft variation.

Work directory outside the repository. Safety and reader replies were reused from pass 1 (the change does not touch them). 106 voice drafts, 21 second drafts and 1 third draft came from the net's regeneration. Sheet: `runs/early-pass-2/sheet.csv`.

## Scoring tool, pass 1 → pass 2

| Measure | Pass 1 | Pass 2 |
|---|---|---|
| Quotes placed, all 106 | 83 | 35 |
| Sealed 28 | 25 | 8 |
| Other 72 | 56 | 26 |
| Fit traps (6) | 2 | 1 |
| Story sentences placed | 139 | 111 |
| Distinct stories placed | 16 | 14 |
| Mean words, sealed 28 | 247.0 | 188.7 |
| Mean words, other 72 | 192.3 | 152.4 |
| Cuts, sealed 28 | 8 | 4 |
| Orphan flags, other 72 | 2 | 4 |
| Reading grade, sealed / other | 6.8 / 6.3 | 7.3 / 6.9 |
| Reading ease, sealed / other | 75.1 / 76.8 | 73.2 / 74.8 |
| Voice set aside (fit traps) | 0 | 1 |

## Fit step on what was placed

| | Placed | Fits | Partly | Off the point | Would keep | Would drop |
|---|---|---|---|---|---|---|
| Pass 1 | 99 | 27 | 29 | 43 | 53 | 46 |
| Pass 2 | 49 | 29 | 17 | 3 | 44 | 5 |

## Sentence judging, a sample

One judge (citation-recall, fixed evidence pack), the same in-plan judge for both passes. A random sample stratified by question group (sealed, other, fit trap) and by whether the sentence introduces a quote, seed 20261031. Pass 1: 121 of 503 (rounding gave one more than 120). Pass 2: 120 of 474. Pass 1 verdicts are the existing fixed-pack verdicts for those sentences.

| | Sample | Not supported | Rate | 95% interval |
|---|---|---|---|---|
| Pass 1 | 121 | 13 | 10.7% | 5.2% to 16.3% |
| Pass 2 | 120 | 15 | 12.5% | 6.6% to 18.4% |

The intervals overlap almost entirely. This shows no difference in the not-supported rate. The error margin is wide. 464 of the 474 pass-2 sentences are new text, so every pass-2 sentence needed judging.

## Spot check, 10 answers, one reader

Ten answers drawn at random (seed 20261031) from pass 2: q006, q010, q027, q031, q032, q040, q049, q066, q094, q098. One reader, from the question, the shipped answer and the full text of the cited records.

- Pass 10, fail 0.
- Fit of what was placed: fits 2, partly 4, nothing placed 4.
- Answers the question asked: yes 4, partly 6.
- Rigor: pass 5, weak 5. Accessibility: pass 10. Craft: pass 8, weak 2. Focus: pass 9, weak 1.
- Fabrication: none 4, minor 6, serious 0.

Pass 1's reader columns came from two readers and a third on splits over all 106 answers, so these ten are not comparable with them. `still_works` is still blank: the run files do not show a mark, hover or click-through working.

## The 43 off-point placements in pass 1: causes

Two readers sorted the 43. Both gave 8 forced by the quote rule and 18 other. They gave 17 each where a better record exists in the world, and between them named a better record for 18 questions. All 18 named records exist. In 13 of the 18 the named record was not in the offered set; in 2 it was offered and not used; in 3 both kinds were named. A third read of the 22 named candidates against their questions: the best candidate fits in 4 questions (2 of them already offered, 2 needing wider retrieval), fits partly in 9 (7 needing wider retrieval), and no candidate fits in 5. Wider retrieval clearly fixes 2 of 43 and might improve 7 more.

## Not done, and cautions

- The fit-trap group has 6 questions, too few to read.
- No full reader pass and no verifier or third read, by Mark's pacing ruling (Decision-Log entry 41).
- The production fit judge is not wired in (metered); the fit-step drops above are reported, not applied.
