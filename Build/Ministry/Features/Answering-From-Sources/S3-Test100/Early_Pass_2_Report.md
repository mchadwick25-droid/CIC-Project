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

## The app check, three answers

The real frontend against the real engine API, with the recorded pass-2 model replies standing in for the model (no model call; the stand-in server lives outside the repository). Three answers on lpc: q035, q040, q044. On each, the quote carries a mark after it; hovering shows a card naming the source (for q040: "Minor treatises, grouped: An Address to Demetrianus, Exhortation to Martyrdom, To Demetrianus"); clicking opens a panel with the quote, the source work and its locus. The `still_works` column is filled for those three rows.

Seen and not changed: the click-through panel for a quote is titled "Where this story comes from"; its sources are shown as plain text paths (file and lines), not links; two of the three answers logged a React duplicate-key console warning; no frontend shows `leadin_support`. The engine does put it on the quote's element in the API response (checked on q035: a lead-in whose details are supported carries it; one with an unsupported detail is replaced by "In today's English, X says:").

## Reading to the acceptance bar, 30 answers

One Opus reader, 30 pass-2 answers drawn at random (seed 20261031; sealed 8, other 20, fit traps 2), reading each against its cited records and against the world's shelf. The bar is Mark's: no serious fabrication, no claim a scholar would call wrong or unsupported by the shelf; minor wording drift is acceptable.

- Serious 2, acceptable 28. No invented fact, quotation or speaker in any of the 30.
- Both serious findings are statements of absence that the shelf contradicts. q065: "no text a woman wrote survives from our two cities" drops the record's limit to the world's own years (246 to 430); the Passion of Perpetua (Carthage, 203), on the shelf, says she wrote her own account. q084: "We have no sermon of our own on those opening lines to give you" is wrong: Augustine's Tractate I on John, on the shelf, is a sermon on John 1:1 to 5.
- One acceptable answer carries the same kind of claim, q042: "What we cannot give you is the words of the creed as said at Hippo or Carthage", although the shelf holds creed wording (Cyprian quotes Carthage's baptismal question; an Augustinian sermon on the creed). Left acceptable because it is worded as a limit and the sermon's authorship is doubtful.
- One reader, 30 answers: the rate is wide (2 of 30 is about 7 percent; the 95 percent interval is roughly 1 to 22 percent). It is a reading, not a measurement.

