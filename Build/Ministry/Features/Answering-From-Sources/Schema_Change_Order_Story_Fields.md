# Schema change order: optional story fields for reviewed tellings

Status: approved by Mark, 2026-10-29 (choice box, direct). It is the named schema change order that the Stage 3 order (`Stage3_Change_Order.md`) and the proposal (section 14, decision 12) require before any story record uses a new field, because `engine/m1/schemas.py` sets `additionalProperties: false` and rejects an unknown field.

Mark's rulings, 2026-10-29: three fixed lengths (short, medium, and the existing full `telling`); targets short about 90 words and medium about 160, tested on the real lpc stories first and reported to Mark if they do not fit, never changed without him; `heart` and `narrative_tier` are carried as data only, with no display change (hover and tier display wait for the layout phase).

## What changes

Four optional fields on the `story` record type in `engine/m1/schemas.py`. Existing story records validate unchanged without them; the existing `telling` stays the full telling.

| Field | Type | Meaning |
|---|---|---|
| `heart` | string | One or two plain sentences: what the story is about and why it was kept. Reviewed against the full record. |
| `events` | array of objects | The story's events in order. Each object: `line` (string, a short plain statement of the event), `rests_on` (string, the place in `text` it rests on), `essential` (boolean, true where the story fails without it). `additionalProperties: false`. |
| `telling_short` | string | A reviewed telling that keeps every essential event and the heart. About 90 words. |
| `telling_medium` | string | A reviewed telling that keeps every event. About 160 words. |

Schema text (added beside `telling` in the `story` properties):

```python
"heart": {"type": "string"},
"events": {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "line": {"type": "string"},
            "rests_on": {"type": "string"},
            "essential": {"type": "boolean"},
        },
        "required": ["line", "rests_on"],
        "additionalProperties": False,
    },
},
"telling_short": {"type": "string"},
"telling_medium": {"type": "string"},
```

## What goes with it

1. **Spoken-field registry** (`engine/m1/spoken_fields.py`): declare `telling_short` and `telling_medium` as `evidence-head` spoken fields beside `telling`, and `heart` as data the voice may read, so the existing readability gate and every list built from the registry cover them. `events` is build-side and is not spoken.
2. **Gates**, run only on a record that has the new fields. They are folded into the existing `narratability` gate (`engine/m1/gates.py`), not registered as a new gate, because registering a gate changes `validation/gates-report.json` in every built world's package and would force a re-pin of all of them:
   - Readability of each telling at the existing spoken-prose bar.
   - Length: each telling at or under its target plus a 15% tolerance; an over-target telling is a finding, not edited. The 15% is a working figure for Mark to confirm or change.
   - Nothing added: every name, place and number in a telling also appears in `text` or in `events`.
   - Events: each has a non-empty `line` and `rests_on`, and a record with a shorter telling has at least one event marked `essential`. That every essential event is covered by each telling is confirmed by the Opus review and Mark's reading, not by the gate.
3. **Placement** (`engine/m4/story_placement.py`): the marker takes a length (full by default), the offer line lists the lengths a story has with their word counts, and code places the chosen reviewed telling word for word. A story without the new fields places as today. This is a separate code change after this order lands.
4. **Card data** (`engine/m4/citation_cards.py`): a story card also carries `heart` and the length told, as data. `narrative_tier` and `means` are already carried. No display change.

## What it does not do

- No record is rewritten by this order. lpc's seven stories get the new fields under their own authoring step (Opus writes, a second Opus pass reviews against the full record, Mark reads about 20 tellings once they exist).
- No display change, no hover or tier display, no layout.
- No live retelling. A retelling fitted to one question stays a stage 4 step under the bound-draft path.
- No gate is retired and no other world is touched.

## Done when

1. The schema and the registry accept the four fields, a story without them validates unchanged, and a story with a malformed `events` entry is rejected. Tests cover each.
2. The gates in item 2 pass on a fixture story with the fields and fail on one with an over-length telling, an added name, and an uncovered essential event.
3. `python -m engine.m1` gates stay green on all built worlds, and `engine/m9` confinement stays green.
4. The commentary check on files changed shows no new commentary.

## For Mark

Approve this order. The lengths are fixed by your ruling; the targets are tested on the real lpc stories first and reported to you if they do not fit.
