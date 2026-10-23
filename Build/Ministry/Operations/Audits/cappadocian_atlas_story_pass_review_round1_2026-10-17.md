# cappadocian Atlas story pass: review round 1, 2026-10-17

Reviewers: fresh Opus 5.5 subagents, none of them the drafter. Sonnet 5.5 drafted the story, teasers and highlight notes; Opus 5.5 authored the tellings. Scope: the participant-facing text this pass changes on the Cappadocia Atlas card and tradition page. Evidence was the records under `records/cappadocian/` and the Pleiades gazetteer only.

## What changed

- `Build/worlds/cappadocian/surface/world_front/cappadocian.front.cappadocian-trinitarian.md`
  - `orientation.story`: 11 units, about 1,330 words, became 11 units, 700 words. The project lead approved it.
  - `orientation.documented_stories`: 3 entries became 10, in date order. Three existing teasers were rewritten; their old wording carried claims no record supports.
  - `orientation.highlights`: 24 notes on people, terms, councils and places (new field).
- `records/cappadocian/story/*.md`: a `telling` on the ten card stories. The project lead approved all ten.

## Checks

| Check | Method | Result |
|---|---|---|
| Story claims | Each sentence traced to the wording of its `grounded_in` records, not to the old story | Pass after fixes (below) |
| Telling claims | Each telling read against its story record's `text`, `absent_detail`, `use_note`, `divergence_note`, tier justification and body | Pass after fixes (below) |
| Hedges and attributions | "As Basil's friend Gregory told it", "by his own account", "the tradition says", "is remembered" | Kept, in place |
| `use_note.not_for` | Read per record | Respected after fixes |
| Places | Pleiades 628949, 629035, 1001924, 511268, 648647, 520998 | Match the notes |
| Add-on endings | Project lead's ruling: no closing line that only comments or says what does not survive | None left |
| Readability | `engine.m10.cli regate cappadocian --base origin/main` | PASS |
| Records gate | `engine.m10.cli records cappadocian` | PASS |

## Findings fixed

Old story, not carried forward because the records say otherwise: "at evening prayer"; a "rented" house; Gregory resigning "almost at once"; Gregory "never fully forgave" Basil and "no water" at Sasima; Theodosius establishing the faith "by law"; the family calling the charge against Gregory of Nyssa invented (it was Basil); "hostile governors"; Basil "a young priest"; Emmelia building the chapel; "planks"; Basil's answers to Modestus without a hedge.

Round 1, story: "the churches of Cappadocia" overstated the core record and was narrowed; Modestus's threats were stated as fact and are now Gregory's telling, in the story, the card and the Modestus note; the Forty of Sebaste teaser stated the lake and the bath as fact; the Macrina note said her words survive in her brother's writing, against `cappadocian.limit.whose-voice-we-lack` `not_for`; the council's order of events in 381; the tail "Scholars still debate his reasons"; a highlight that could never show because it sat inside a longer phrase.

Round 1, tellings: the Valens telling put the cause of the unexecuted exile outside Gregory's attribution; the Epiphany scene, Gregory's reasons for resigning and his view of the capital were stated as fact; unclear antecedents in the Sasima and Macrina tellings; a meaning line in Forty of Sebaste; an add-on ending in the Athens telling.

Round 2 (targeted recheck): Basil's reply to Modestus was flat in the story and teaser; the Modestus note stated the threat as fact; two wording fixes. All fixed.

## Left open

- Five record disagreements (OG-49).
- Other world_front sections keep tells and "this world" wording (OG-50).

Verdict: PASS.
