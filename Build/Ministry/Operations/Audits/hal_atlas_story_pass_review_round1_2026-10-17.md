# hal Atlas story pass: review round 1, 2026-10-17

Reviewers: fresh Opus 5.5 subagents, none of them the drafter. Sonnet 5.5 drafted the story, teasers and highlight notes; Opus 5.5 authored the tellings. Scope: the participant-facing text this pass changes on the Bethlehem Circle Atlas card and tradition page. Evidence was the records under `records/hal/` and the Pleiades gazetteer only.

## What changed

- `Build/worlds/hal/surface/world_front/hal.front.hieronymian-ascetic-literary.md`
  - `orientation.story`: 11 units, about 1,150 words, became 9 units, 691 words. The project lead approved it.
  - `orientation.documented_stories`: 3 entries became 9, in date order. Three existing entries carried wording no record supports and now follow the records.
  - `orientation.highlights`: 17 notes on people, terms and places (new field).
- `records/hal/story/*.md`: a `telling` on the nine card stories. The project lead approved all nine.

## Checks

| Check | Method | Result |
|---|---|---|
| Story claims | Each sentence traced to the wording of its `grounded_in` records, not to the old story | Pass after fixes (below) |
| Telling claims | Each telling read against its story record's `text`, `absent_detail`, `use_note`, `divergence_note`, tier justification and body | Pass after fixes (below) |
| Hedges and attributions | "Jerome writes", "Jerome reports", "as Jerome heard it", "in Jerome's telling", "the account says", "historians think" | Kept, in place |
| `use_note.not_for` | Read per record | Respected after fixes |
| Places | Pleiades 423025, 687856, 865014139, 344456, 305090 | Match the notes |
| Add-on endings | Project lead's ruling: no closing line that only comments or says what does not survive | None left |
| Readability | `engine.m10.cli regate hal --base origin/main` | PASS after one fix (below) |
| Records gate | `engine.m10.cli records hal` | PASS |

## Findings fixed

Old story, not carried forward because the records say otherwise: "No one here held church office" (Jerome was a presbyter); "eldest daughter"; "All Rome noticed"; Jerome teaching Blaesilla the fasting; the Tiber crowd as fact; "never to return"; Marcella's death "in a church that had become a refuge" and "Rome's last independent center"; the Oea congregation "rioted"; Augustine agreeing "with every point"; Paula's fortune paying for everything as fact; the Pelagian quarrel as the circle's "oldest" fight.

Round 1, story: Paula's fortune was stated as fact and is now Jerome's account; a commentary line on authority was replaced by the record's fact that Jerome was a presbyter under the bishop of Jerusalem; Marcella's answers now come "as if they came from him or someone else" (`hal.quote.recourse-to-marcella`); Augustine's concession restored; "the bishop" disambiguated as the bishop of Oea; the house quote follows `hal.quote.house-destroyed`; the Cicero dream card dated about 374.

Round 1, tellings: Paula's greeting at Bethlehem, the causal framing of Damasus's death, Marcella's second thanksgiving and Paula's fortune were stated as fact and are now attributed; two sentences could be heard as misattributing an act; the Rufinus telling's repeated openings.

Round 2 (targeted recheck): Paula's fortune in the Bethlehem telling; "detestable" to match the record; "not from herself"; the Marcella note matched to the story's hedge. All fixed.

Readability gate: one story unit scored FRE 59.7; "had declined to name" became "would not name", matching the record's "left untold the name".

## Left open

- Five record disagreements (OG-24), including Paula's acknowledgment placed at the opening of her telling.
- Other world_front sections keep tells and "this world" wording (OG-25).

Verdict: PASS.
