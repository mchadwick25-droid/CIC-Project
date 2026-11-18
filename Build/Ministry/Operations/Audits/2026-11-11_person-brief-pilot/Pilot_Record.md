# Person-brief pilot, 2026-11-11

Ten person briefs (census `longDescription`, kind "person") were rewritten to Mark's standard for person briefs (Decision-Log entry "Person briefs: 60 to 120 seconds, personal and theological", 2026-11-11). Each also has a filled person card. Nothing in the census or on the site changed. These are pilot drafts for Mark's review.

Review artifact: https://claude.ai/artifact/AyVVxVF7SmNexs7MJRXDXL

## Process
- Drafting: Sonnet subagents, one scratch directory per group. Working briefs are `BRIEF.md`, `REVISE.md`; the reviewer's method is `REVIEW.md`.
- Review: Opus adversarial review. Round 1 was full; rounds 2 and 3 were targeted rechecks. Every claim was checked against the vendored file lines, and every quotation was compared character for character. All ten cleared at round 3, inside the three-round cap. The review files are in `reviews/`.
- After round 3, three changes were applied without a further round:
  - two exact one-line card swaps the round-3 reviewer prescribed (Gregory of Nyssa's Theosebeia line; Gregory of Nazianzus's Gennadius line);
  - one wording tweak on the Athanasius card that the round-3 reviewer offered as optional ("a country house of his near the New River");
  - the Origen card's first "uncertain" line, which the round-3 reviewer offered as optional and which now names On First Principles.
- Mark's rulings applied during the pilot:
  - the levels of Scripture go back into Origen's brief;
  - no brief may run past 120 seconds;
  - the card continues the brief's story, and its "uncertain" field restates the caveat in its own words;
  - Legacy and the named-by-other-traditions material merge into one section, and the card ends with Sources in two groups.
- Readability: `engine/m7/turn_readability.py` (`score_turn`). Estimated seconds assume 150 words a minute.

## Figures
| Person | Words | Est. seconds | FK | FRE | Current words | Current FK |
|---|---|---|---|---|---|---|
| origen | 299 | 120 | 8.7 | 60.4 | 99 | 6.4 |
| athanasius-of-alexandria | 299 | 120 | 8.2 | 65.5 | 107 | 6.5 |
| john-chrysostom | 296 | 118 | 8.6 | 62.5 | 112 | 5.0 |
| gregory-of-nyssa | 300 | 120 | 8.8 | 64.8 | 117 | 5.4 |
| gregory-of-nazianzus | 278 | 111 | 8.7 | 61.9 | 121 | 6.6 |
| ephrem-the-syrian | 269 | 108 | 8.4 | 66.9 | 58 | 4.6 |
| methodius-of-olympus | 222 | 89 | 8.1 | 61.9 | 141 | 6.6 |
| constantine-the-great | 299 | 120 | 8.6 | 67.1 | 123 | 6.8 |
| bede-of-jarrow | 298 | 119 | 9.3 | 65.8 | 114 | 6.3 |
| hugo-grotius | 282 | 113 | 9.4 | 60.8 | 104 | 7.2 |

All ten are inside the band (FK 8 to 10, FRE at least 60), with no failures.

## Recording
- Approved run: "CFT person pilot 2026-11-11".
- Voice: David Baker, fxnZk29PIJ3WKEC9MDEo.
- Model and format: eleven_multilingual_v2, mp3_44100_64.
- Settings: {"stability":0.95,"similarity_boost":0.68,"style":0,"use_speaker_boost":true}, passed explicitly and printed on each call. The logs are in `recording/`.

| Clip | Characters sent | character-cost header | Duration |
|---|---|---|---|
| origen | 1,734 | 841 | 120.4 s |
| athanasius-of-alexandria | 1,675 | 812 | 121.9 s |
| methodius-of-olympus | 1,254 | 608 | 88.8 s |
| Total | 4,663 of the 5,500 cap | 2,261 | |

- Subscription balance (characters used of 600,000): 199,409 before the first call and 216,355 after the last. Another worker was recording stories at the same time, so this run's own spend is the header total.
- Athanasius runs 1.9 s past the 120-second ceiling. At this narrator's pace, 300 words comes to just over two minutes, so about 290 words is the safe ceiling.
- The clips are pilot clips. They are on the review artifact only, not on the site, in the manifests, or in this repository.

## Open points for Mark
- The word ceiling for a 120-second brief, given David Baker's pace: about 290 words.
- The card template, judged across all ten: the field order, the Legacy parts, and Sources in two groups.
