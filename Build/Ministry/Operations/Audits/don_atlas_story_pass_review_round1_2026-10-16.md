# don Atlas story pass: review round 1, 2026-10-16

Reviewer: Opus 5.5, site-editing thread. Scope: the participant-facing text this pass changes on the Donatist Atlas card and tradition page.

## What changed

- `Build/worlds/don/surface/world_front/don.front.donatism.md`
  - `orientation.story`: 13 units, 1,888 words, became 9 units, 672 words, under five minutes aloud. The project lead read and approved it. He asked for "from around 311", which covers the record's "311 or 312".
  - `orientation.documented_stories`: 3 entries became 9, in date order. Six episodes cut from the story are added. Three existing teasers lose their dash asides.
  - `orientation.highlights`: 28 notes on people, terms, councils and places (new field).
- `records/don/story/*.md`: a `telling` on the nine stories shown on the card. Under decision 24 the card shows and plays a story's modern telling, never its `text`. The project lead read and approved all nine.

## Checks

| Check | Method | Result |
|---|---|---|
| Story claims | Each sentence traced to a current story unit or its `grounded_in` record | Pass after one fix (below) |
| Telling claims | Each telling read against its story record's `text`, `absent_detail`, `use_note` and `divergence_note` | Pass after two fixes (below) |
| Hedges and attributions | "as Optatus tells it", "the account says", "reportedly", the Passio's testimony framing | Kept in every telling |
| `use_note.not_for` | Read per record | Respected |
| Highlight notes | Every `grounded_in` id resolves. Each note read against its records | Pass after edits (below) |
| Readability | `engine.m10.cli regate don --base origin/main` | PASS. Ten notes and five teasers were simplified to clear FRE 60 |
| Records gate | `engine.m10.cli records don` | PASS |
| AI tells | Read against `records/syr/demonstration/syr.demo.room-for-doubt.md` | None found in the changed text |

## Findings fixed

1. Story unit 2 said the rival party made Majorinus bishop "beside" Caecilian. `don.story.lucilla-affair` says "in Caecilian's place". Corrected, and the project lead was told.
2. The `conference-of-carthage-411` telling had Petilian say "how could we refuse?". The record's sense is refusing to stand, so it now reads "how could we refuse to stand?".
3. The `tyconius-condemnation` telling said his opponents "had left something real". The record says they "separated themselves from something real". Corrected.
4. Highlights:
   - "Nicene faith" ended in a "not doctrine" turn. Rewritten as plain statements.
   - "The emperor later" was narrowed to "The emperor".
   - Added "Optatus Gildonianus" so his name is not marked as Optatus of Milevis.
   - The Cirta and Aptungi notes now cite the Monceaux source records for their modern locations.
   - A Bagai clause cited an 1894 study that has no source record, so it was removed.

## Left open

- Modern locations for Carthage, Numidia, Bagai, Cebarsussi, Novapetra and Vegesela wait for a gazetteer. The environment's network policy blocks pleiades.stoa.org. No location is filled in from memory.
- Other world_front sections keep the tells and "this world" wording that this pass did not touch: `voices` and their hedges, `floor_note`, `legacy`, `relations_summary`, `sourcing`, `read_first` and `who_speaks`. Several also fail the readability gate at the base.

Verdict: PASS.
