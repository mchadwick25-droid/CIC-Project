# ijc Atlas story pass: review round 1, 2026-10-17

Reviewers: Opus 5.5, site-editing thread, and an independent Opus 5.5 subagent that had not drafted or authored the text. Scope: the participant-facing text this pass changes on the Imperial Church Atlas card and tradition page.

## What changed

- `Build/worlds/ijc/surface/world_front/ijc.front.imperial-juridical.md`
  - `orientation.story`: 11 units, about 1,500 words, became 8 units, 662 words, under five minutes aloud. The project lead read and approved it, then approved the corrected text below.
  - `orientation.documented_stories`: 3 entries became 10, in date order. Seven episodes cut from the story are added. The three existing teasers lose their dash asides and contrast setups.
  - `orientation.highlights`: 35 notes on people, terms, councils and places (new field). Place locations cite Pleiades.
- `records/ijc/story/*.md`: a `telling` on the ten stories shown on the card, authored by Opus. Under decision 24 the card shows and plays a story's modern telling, never its `text`. The project lead read and approved all ten.

## Checks

| Check | Method | Result |
|---|---|---|
| Story claims | Each sentence traced to its unit's `grounded_in` records, not to the old text | Pass after fixes (below) |
| Telling claims | Each telling read against its story record's `text`, `absent_detail`, `use_note` and `divergence_note` | Pass after fixes (below) |
| Quotes | Every quoted wording matched to the quote record's `modern_rendering` | Pass |
| Hedges and attributions | "Eusebius tells", "he said", "it is said", "the session record has them crying out", Augustine's memory | Kept, after the fixes below |
| `use_note.not_for` | Read per record | Respected |
| Places | Live Pleiades JSON for all seven places, 2026-10-17 | Pass. Callinicum carries Pleiades' "may be identical" |
| Readability | `engine.m10.cli regate ijc --base origin/main` | PASS |
| Records gate | `engine.m10.cli records ijc` | PASS |
| Independent review | Fresh Opus subagent, verifying only against repo records and Pleiades, never from memory | 7 blocking, 6 craft, 5 minor; all fixed |

## Findings fixed

1. The old story placed Callinicum (388) "two years earlier" than the 386 standoff. Corrected.
2. The old story said Leo's letter went to Chalcedon in his place. The record says his legates went and his letter was read. Corrected.
3. The old story told the 386 standoff with no legal basis. `ijc.story.vigil-in-basilica` says the court acted under a law of January 386, and its `not_for` forbids "force and no legal pretext". The story names the law; the telling also carries that one edition dates it a year earlier.
4. Independent review, blocking:
   - The story dated the council that deposed Athanasius to 341. Only Julius's letter carries that date. Corrected in the story and the Athanasius note.
   - "Earliest surviving voice of Rome's claim" dropped the window. `ijc.quote.julius-custom` `not_for` rules out "the earliest ever". Now "from these years".
   - The Altar of Victory note said the altar was put back "more than once". The record says once. Now the record's sentence.
   - The Homoian note called the word Greek, which no record says. Now "From homoios, meaning like".
   - Constantine's vision was told as fact. Now "he said".
   - The Milan guard "ready to die" was told as the narrator's fact. Now Augustine's memory.
5. Independent review, craft: very short sentences merged; spoken quotes given quotation marks; "in the record", "neither is ranked", "we tell the two accounts side by side", "the printed edition" and "from our own age" removed; Canon 28's "fathers" glossed as "earlier bishops", per the quote record; "both claims" named; Callinicum says plainly that Ambrose used his power to shield the people who set the fire; Bishop John and Milan notes follow their sources.
6. The project lead's ruling, "remove all the add on tails that dont say anything": closing source caveats and summary lines are removed from the story, eight tellings and two notes. Hedges that qualify a specific claim stay in place.

## Left open

- The recordings of the new story and the ten tellings wait on the project lead's approval of a sample.
- Other world_front sections keep "this world" wording (Open_Gaps entry 40).

Verdict: PASS.
