# S1-01 free measures (no model call)

Run 2026-10-29 by the engine thread. Scripts: `request_size.py`, `saved_scores.py` in this folder. The live-path baseline run itself did not complete (see the ledger); these are the measures that need no API.

## What the live path sends the voice, per world (reader stubbed)

The stub reader returns the probe as its one ask and kind "other"; the real reader would restate the ask, so offered records can differ. Tokens are characters divided by 4.

| World | Cached system chars (about tokens) | User message chars, mean (max) | Directive chars, mean | Offered records, mean | Offered quotes, mean | Probes with no ground |
|---|---|---|---|---|---|---|
| alx | 75,961 (18,990) | 10,718 (15,603) | 1,756 | 13.0 | 3.0 | 0 |
| cappadocian | 120,924 (30,231) | 11,643 (24,295) | 1,407 | 9.0 | 1.6 | 0 |
| desert | 76,787 (19,196) | 13,274 (19,012) | 2,425 | 11.8 | 3.6 | 0 |
| don | 161,274 (40,318) | 15,830 (24,129) | 1,100 | 10.5 | 0.8 | 0 |
| gallic | 148,401 (37,100) | 13,220 (17,727) | 1,992 | 10.8 | 3.5 | 0 |
| hal | 70,415 (17,603) | 8,815 (10,900) | 1,776 | 11.4 | 3.2 | 0 |
| ijc | 68,330 (17,082) | 10,256 (16,097) | 1,623 | 10.4 | 2.4 | 0 |
| lpc | 102,190 (25,547) | 14,674 (35,036) | 1,781 | 10.0 | 3.6 | 1 |
| pahc | 69,628 (17,407) | 10,997 (14,564) | 1,661 | 10.6 | 2.5 | 0 |
| rzg | 59,044 (14,761) | 9,004 (17,885) | 1,186 | 8.1 | 1.0 | 0 |
| syr | 73,779 (18,444) | 9,721 (12,685) | 1,843 | 10.8 | 3.1 | 0 |
| witt | 132,281 (33,070) | 11,876 (16,250) | 1,560 | 9.5 | 1.9 | 0 |

## Shipped answers of fleet graded run 1, per world (admission path, 28 probes each; rzg attempt 2)

| World | Words, mean (max) | Over 220 words | FK grade, mean | FRE, mean | FRE below 60 | Build talk or raw tags | Horizon flags |
|---|---|---|---|---|---|---|---|
| alx | 281 (844) | 18 | 7.1 | 70.7 | 2 | 0 | 0 |
| desert | 277 (544) | 24 | 7.9 | 68.8 | 4 | 2 | 0 |
| don | 290 (492) | 21 | 6.6 | 75.9 | 0 | 0 | 1 |
| gallic | 359 (684) | 26 | 7.1 | 74.5 | 1 | 1 | 0 |
| hal | 262 (429) | 21 | 7.6 | 69.3 | 3 | 0 | 0 |
| ijc | 252 (592) | 15 | 7.8 | 66.9 | 4 | 0 | 0 |
| lpc | 233 (841) | 10 | 6.5 | 74.0 | 1 | 2 | 0 |
| pahc | 242 (622) | 15 | 6.7 | 73.5 | 1 | 0 | 0 |
| rzg | 226 (329) | 17 | 8.7 | 63.7 | 9 | 2 | 0 |
| syr | 228 (414) | 15 | 6.3 | 74.2 | 1 | 2 | 0 |
| witt | 266 (375) | 19 | 6.5 | 73.8 | 0 | 1 | 0 |

Across the 308 answers: 201 run past the 220-word ceiling of the live concision directive (65%); 10 carry build talk or raw tags; 1 horizon flag. Readability sits inside the target except rzg (FRE 63.7, 9 answers below 60).

## Limits

- Word counts and readability are on admission-path answers, which skip the length directive; the live path asks for 120 to 220 words, so these numbers are an upper bound on length, not a live measure.
- The build-talk scan is a short phrase list, not the full leak classifier; the horizon scan is the engine's own check_horizon.
- Not measurable without the API: the reader's output, the live directive's effect on drafts, cost per shippable answer, and the voice-call error from the failed sample.
