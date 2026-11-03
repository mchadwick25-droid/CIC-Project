# Schema change order: an optional reading card on quote and story records

Named schema change order. `engine/m1/schemas.py` sets `additionalProperties: false`, so a quote or story record cannot carry a new field until this order lands. It rests on Decision-Log 75, which approved the V7 direction for a controlled test, not as architecture. The plan is `../V7-Controlled-Test/Test_Plan.md` §4 and the spec is `../V7-Controlled-Test/Specs/V4a_Reading_Card_Field.md`. The test uses cards on alx only.

Mark's words, 2026-11-03 (entry 75): reading cards keep four things apart. They are what the primary source says, what historians conclude about it, what it contributes to understanding the world, and what is disputed, uncertain or unrepresentative.

## What changes

One optional field, `reading_card`, on the `quote` and `story` record types. It is an object, and it takes no field beyond these:

| Line | Type | Holds |
|---|---|---|
| `setting` | string | Who wrote or said it, to whom, on what occasion. |
| `source_says` | string | What the passage says at this point in the author's argument. |
| `historians_conclude` | object: `text` (string), `confidence` | What historians conclude about it. `confidence` is one of the five levels: Documented, Widely Accepted, Dominant Modern Reconstruction, Contested, Inferential-Thin. Both keys are required. |
| `contributes` | string | What it adds to understanding the world: belief, practice, or how the community lived its faith. |
| `whose_view` | string | Whose position this is and how widely it was shared, with the reason. |
| `open` | string | What is disputed, uncertain or unrepresentative. |
| `reads_differently_today` | string | The modern-lens note, rewritten so the voice can say it. |
| `complicated_by` | array of record ids | The records that qualify it, only where they exist. |
| `sources` | object: line name to string | For each line present, the source id and locus, or the construction document and section, that supports it. Its keys are only the seven lines above. |

Every line is optional. Existing records validate unchanged without the card.

The card carries its own `setting` line. The quote's existing structured `setting` (`said_by`, `to_whom`, `occasion`, `answers`) stays as it is and may be filled separately. Stories have no `setting` field, so the card's line serves both types the same way.

## The rules

- **Every line names its source.** A line with no entry in `sources` is a finding. A line that cannot be traced to its named source is left out, never written. Review checks each source.
- **`whose_view` is prose, not a rank.** There is no scale, score or enum. An influential author is not the community, and a common practice is not universal agreement. The line says whose view it is and why it was or was not widely shared.
- **Short.** The text lines together run to 120 words or fewer. Record ids and citations do not count.
- **`complicated_by` ids must exist** among the world's records or the fleet records.

## What goes with it

1. **Schema** (`engine/m1/schemas.py`): `reading_card` on `quote` and `story`, as in the table. The five confidence levels are kept once, as `FORMATION_CONFIDENCE_LEVELS`, and the envelope's `formation_confidence` uses the same list.
2. **Gate** (`engine/m1/gates.py`, `gate_reading_card`): a present line without a source, an empty line, a confidence outside the five levels, a `complicated_by` id that does not resolve, and a card over 120 words are each a finding. It runs only on a record that has a card. It is not registered in `GATES`, because `validation/gates-report.json` lists `GATES` and is baked into every package manifest; registering it would stale every pinned package. `engine/m9/enforce.py` runs it under `m1:reading-card`, and its findings take waivers like any other.
3. **Compile** (`engine/m2/builders.py`): `reading_card` joins `_PACKAGE_STRIPPED_FIELDS`. No package and no production turn sees it. No prompt, capsule, chunk or retrieval path reads it. A test compiles alx with cards on a quote and a story and finds every compiled file byte-equal, `prompt.txt` and `repository.json` among them.
4. **Test-time access** (`engine/m4/reading_cards.py`): `load_reading_context(records_dir, world)` reads each quote and story record's card and `modern_lens_note` straight from the record files. Only the V7 test harness calls it.

## What it does not do

- No record is written by this order. The 35 alx cards are written under Spec V4b: Opus authors them blind to the A and B answers, and an Opus review checks them under the build cycle's capped rounds.
- No change to `render.yaml`, the turn path, or any package. No other world gets cards.
- It is not an architecture decision. Whether cards ever reach production is decided after the V7 results.

## Done when

The schema accepts the card on quotes and stories and rejects it elsewhere; a card missing a line's source, over 120 words, or naming a missing record fails the gate; compiling alx with a card leaves the package byte-equal; the loader returns a fixture record's card and lens note. Tests cover each. The fleet gates are unchanged on every world.
