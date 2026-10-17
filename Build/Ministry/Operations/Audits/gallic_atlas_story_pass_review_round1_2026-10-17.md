# gallic Atlas story pass: review round 1, 2026-10-17

Reviewer: Opus 5.5, site-editing thread. Scope: the participant-facing text this pass changes on the Gallic Atlas card and tradition page.

## What changed

- `Build/worlds/gallic/surface/world_front/gallic.front.gallic-monastic-ascetic-christianity.md`
  - `orientation.story` goes from 11 units and 1,655 words to 8 units and 659 words, about 4 minutes aloud. The project lead approved it.
  - `orientation.documented_stories` goes from 2 entries to 10. Eight episodes are added, including the cloak at Amiens. The two existing teasers no longer have dash asides.
  - `orientation.highlights` is new: 25 notes. Eleven places cite Pleiades.
- `records/gallic/story/*.md`: a `telling` on each of the ten card stories. The project lead approved all ten.

## Checks

| Check | Method | Result |
|---|---|---|
| Story claims | Each sentence traced to a current unit or its records | Pass after three fixes (below) |
| Telling claims | Each read against its story record and `use_note.not_for` | Pass. Details the record does not support were left out and listed |
| Hedges and attributions | Sulpitius, Gallus, Cassian and Hilary named as sources; miracles kept as testimony | Kept |
| Highlight notes | Ids resolve; places cite Pleiades; "probably" used where Pleiades or the record is uncertain | Pass |
| Readability | `engine.m10.cli regate gallic --base origin/main` | PASS. The Arles note was simplified |
| Records gate | `engine.m10.cli records gallic` | PASS |
| AI tells | Read against `records/syr/demonstration/syr.demo.room-for-doubt.md` | None found in the changed text |

## Findings fixed

1. The draft said Martin asked for his discharge "around 360". The record gives no year. It now says "while he served under Julian, then Caesar".
2. The draft said "a crowd the record puts at two thousand buried him". The record says almost two thousand monks are said to have gathered. Corrected.
3. Honoratus "was made bishop of Arles" now reads "later became bishop". The figure record carries his episcopate. The island story's `not_for` bars telling it from the sermon.
4. Two teasers, "Martin Asks Caesar for His Discharge" and "Martin Yields Once", had dash asides and failed the reading gate. Both were rewritten.

## Left open

- Some cut details have no story record: Martin going to Hilary of Poitiers, Cassian's eight faults, Vincent's purpose in writing, and Faustus of Riez. They stay in the records and are not on the card.
- Other world_front sections still say "this world" and use dash asides. These are `voices`, `floor_note`, `legacy`, `relations_summary`, `sourcing`, `read_first` and `who_speaks`.

Verdict: PASS.
