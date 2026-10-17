# witt Atlas story pass: review round 1, 2026-10-17

Reviewers: Opus 5.5, site-editing thread, and independent Opus 5.5 subagents that had not drafted or authored the text (a full check of the story, card and highlights; a targeted recheck of the fixes; a full check of the tellings; and a check for add-on tails across the whole pass). Scope: the participant-facing text this pass changes on the Wittenberg Atlas card and tradition page.

## What changed

- `Build/worlds/witt/surface/world_front/witt.front.lutheran-wittenberg-and-its-congregations.md`
  - `orientation.story`: 12 units, about 1,170 words, became 12 units, 645 words, under five minutes aloud. The project lead approved it, and approved the changes after the tails review.
  - `orientation.documented_stories`: 3 entries became 10, in date order. Seven episodes cut from the story are added. Existing teasers are reworded to their records.
  - `orientation.highlights`: 25 notes on people, terms, councils and places (new field). Mainz, Worms and Augsburg cite Pleiades; Wittenberg and the Wartburg have no Pleiades entry and give no modern location.
- `records/witt/story/*.md`: a `telling` on the ten stories shown on the card, authored by Opus. The project lead approved them.

## Checks

| Check | Method | Result |
|---|---|---|
| Story claims | Each sentence traced to its unit's `grounded_in` records, not to the old text | Pass after fixes (below) |
| Telling claims | Each telling read against its story record's `text`, `absent_detail`, `use_note` and `divergence_note` | Pass after fixes (below) |
| Quotes | Checked against record text | Pass |
| Hedges and attributions | Table Talk memory, "a tradition says", Walter's memory, the ballad's own voice, the catechism's prescriptive "was to" | Kept |
| `use_note.not_for` | Read per record | Respected |
| Places | Live Pleiades JSON, 2026-10-17 | Pass |
| Readability | `engine.m10.cli regate witt --base origin/main` | PASS |
| Records gate | `engine.m10.cli records witt` | PASS |

## Findings fixed

1. The old story said the first hymn-book held four hymns. `witt.story.speratus-hymn-under-the-window` says eight, four of them Luther's.
2. The old story had Luther before "the Emperor and the princes" at Worms. The record says the Electors.
3. "No surviving source" overclaimed where the records say only that the library does not hold the visitation protocols, the Marburg Articles or other words of Katharina's. Reworded, then removed as tails.
4. "Made right with God" leaned to one side of `witt.contested.justification-accounted-and-made`. Now AC IV's "freely justified for Christ's sake, through faith".
5. Tellings: the Walter telling placed the Torgau trip on the Mass's day; the catechism telling told prescribed confession words as events; "no other witness survives" and "the only martyr-song we have" overclaimed; "Bacon calls it no more than tradition" put words in Bacon's mouth. All corrected.
6. The Marburg break, rated Inferential-Thin, is no longer narrated (Open_Gaps OG-74). "Here I stand" and the door posting are no longer narrated; the records' cautions bar stating either as fact, and nothing now states them.
7. The project lead's ruling, "remove all the add on tails that dont say anything": closing source notes leave the story, teasers, tellings and notes. At his direction the story keeps one line that scholars disagree about the 1543 treatise's later effect.

## Left open

- The recordings wait on the project lead's approval of a sample.
- The Speratus telling runs 92 words because its record is short; it is not padded.
- Other world_front sections keep "this world" wording (Open_Gaps OG-75).

Verdict: PASS.
