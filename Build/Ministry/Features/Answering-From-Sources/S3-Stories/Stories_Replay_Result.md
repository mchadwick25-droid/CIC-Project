# Stage 3 stories: replay of story handling in the saved drafts

Free: no model call. Run 2026-10-29 by the engine thread with `story_bench.py` (same saved drafts and method as S1-L2; cappadocian saved no draft). Evidence is rebuilt the way the run built it, so offers can differ on the live path.

## Numbers today

| World | Stories in record | Probes offered a story | Story sentences in drafts | Placed by code | Story sentences cut | Shipped as the voice's own wording | Of those, restate their record |
|---|---|---|---|---|---|---|---|
| alx | 9 | 21 of 28 | 11 | 0 | 0 | 7 | 6 |
| desert | 12 | 24 of 28 | 42 | 1 | 29 | 12 | 5 |
| don | 12 | 27 of 28 | 18 | 0 | 0 | 18 | 15 |
| gallic | 15 | 27 of 28 | 55 | 0 | 0 | 49 | 31 |
| hal | 12 | 25 of 28 | 19 | 0 | 0 | 15 | 6 |
| ijc | 11 | 24 of 28 | 32 | 0 | 0 | 29 | 17 |
| lpc | 7 | 19 of 28 | 11 | 0 | 0 | 11 | 9 |
| pahc | 15 | 26 of 28 | 19 | 0 | 0 | 18 | 12 |
| rzg | 3 | 14 of 28 | 10 | 0 | 0 | 9 | 3 |
| syr | 10 | 25 of 28 | 9 | 0 | 0 | 7 | 5 |
| witt | 12 | 23 of 28 | 9 | 0 | 0 | 8 | 6 |
| **All** | 118 | 255 of 308 | 235 | 1 | 29 | 183 | 115 |

## What it shows

- A story is on offer in 255 of 308 answers (83%), 534 offers in all. Stories are a large part of what the evidence gives the voice.
- Only desert places stories by code (its world flag). There the voice retold stories in its own words 28 times and the engine cut every one (reason: tells an offered story without placing it); one story was placed by code in 28 answers. The directive that tells the voice not to retell was not sent in this run, so this may fall on the live path; that needs the API to measure.
- In the ten other worlds the voice tells stories in its own words and nothing checks them as stories: 171 sentences shipped that way. By a word-overlap rule (at least 60% of a sentence's content words appear in its record's telling), 110 of those 171 restate their record and the rest are not shown to. Overlap is not proof of faithfulness; it only bounds the unchecked share.
- Cut story sentences: 29 (28 of them desert). Orphan flags in the 8 drafts that lost one: 4.
- Not measurable here: the inline mark, hover and click-through on screen, and tier and confidence reaching the card (a frontend and card-data check for the change order).

## The numbers the stage 3 stories change order must move

1. Stories marked inline in the text: today 1 placed by code in 308 answers, 0 inline marks counted outside desert's placement.
2. Stories told from a reviewed record only (a reviewed telling, or a bound and verified retelling): today at most 115 of 183 voiced story sentences (63%) are even word-overlap restatements of their record; nothing verifies them.
3. Stories cut by the current gates: 29 sentences (28 desert), and their orphans (4 flags in 8 drafts).
4. Faithfulness of a shortened or reshaped telling (Mark's refinement of 2026-10-29: shortened or reshaped is allowed if the heart and source context hold, nothing added, B2 readable, at conversation length, a direct example for the question): events kept and nothing added, on each reviewed telling and on a human-read sample for Mark. The target is Mark's to set; the replay cannot produce this number because no shortened tellings exist yet.

## Limits

- Word overlap is a screen, not a faithfulness test. The human-read sample and the bound-sentence verify are what would test it.
- The live voice call is unproven in this environment, so the live-path effect on story retelling is unmeasured.
