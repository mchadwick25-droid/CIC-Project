# alx Atlas story pass: review round 1, 2026-10-17

Reviewers: fresh Opus 5.5 subagents, none of them the drafter. Sonnet 5.5 drafted the story, teasers and highlight notes; Opus 5.5 authored the tellings. Scope: the participant-facing text this pass changes on the Alexandria Atlas card and tradition page. Evidence was the records under `records/alx/` and the Pleiades gazetteer only.

## What changed

- `Build/worlds/alx/surface/world_front/alx.front.alexandria-catechetical.md`
  - `orientation.story`: 12 units, about 1,070 words, became 10 units, 622 words, about four minutes aloud. The project lead approved it, and ruled that the closing unit on missing women's voices stays out.
  - `orientation.documented_stories`: 3 entries became 9, in date order. Six are added. Three existing entries had dates or teasers the records do not support ("c. 205", "c. 255", a dash aside, "a city that had shown them little kindness"); they now follow the records.
  - `orientation.highlights`: 29 notes on people, terms, the council and places (new field).
- `records/alx/story/*.md`: a `telling` on the nine card stories. The project lead approved all nine.

## Checks

| Check | Method | Result |
|---|---|---|
| Story claims | Each sentence traced to the wording of its `grounded_in` records, not to the old story | Pass after fixes (below) |
| Telling claims | Each telling read against its story record's `text`, `absent_detail`, `use_note`, `divergence_note`, tier justification and body | Pass after fixes (below) |
| Hedges and attributions | "Eusebius tells us", "Eusebius alone tells", "the tradition says", "later tradition", "scholars disagree" | Kept, in place |
| `use_note.not_for` | Read per record | Respected after fixes |
| Places | Pleiades 727070, 678401, 736948, 511268, 599612, 857177 | Match the notes |
| Add-on endings | Project lead's ruling: no closing line that only comments or says what does not survive | None left |
| Readability | `engine.m10.cli regate alx --base origin/main` | PASS |
| Records gate | `engine.m10.cli records alx` | PASS after one fix (below) |

## Findings fixed

Old story, not carried forward because the records say otherwise: Clement's bee teacher named as Pantaenus by Clement (only Eusebius names him); Athanasius "forty-six years" unattributed; Didymus visited "for decades" and holding "the whole of Scripture"; a "moral sense" layer; Gregory "later a bishop"; the plague letter's "practice the whole city could see"; Potamiaena's death told as fact.

Round 1 (full review):
1. Unit 1 said the faith was "built around teaching"; `alx.core.alexandria` gives two channels. Rewritten.
2. Unit 2 dropped "learning" from the four things the Logos makes one movement (`alx.gravity.logos-unity`). Restored.
3. "A line of teachers" overstated `alx.contested.didaskaleion-institution`; the formal-school dispute is now scoped to before Origen.
4. The teacher-student bond as the main way "people" were formed broke `alx.gravity.learning-formation` not_for. Now scoped to readers.
5. Didymus's books "lost apart from fragments" conflicts with `alx.core.alexandria`. Now "most of his books" in the telling; logged in OG-29.
6. The Potamiaena telling stated the pitch plainly. Now "the tradition says".
7. The martyrdom thread had been lost in the cut. Restored from `alx.gravity.martyrdom-contemplative-tension` and `alx.force.persecution`.

Round 2 (targeted recheck): the new martyrdom line said martyrdom alone reached non-readers, which clashed with unit 1; no record calls Decius emperor; the Nepos lines could be read as Nepos being persuaded; "three ancient writers" implied no others describe Didymus. All fixed.

Round 3 (after the add-on ruling): the vision and the promise in the Potamiaena telling needed the tradition's attribution in place; the Arsinoite telling needed to say Nepos's book is lost; the daring-deed telling stated Eusebius's motive as fact; the Didymus telling over-attributed "so he told me"; the plague telling ended on the pagan contrast, which sharpens it; repeated openers; an unclear pronoun in the Leonides teaser; "In the school" stated the institution as fact. All fixed.

Round 4 (targeted recheck): the scholars' doubt moved after the Demetrius paragraph so the act stays under Eusebius's attribution; four wording fixes for reading aloud. Verdict: approved to proceed.

Records gate: "The tradition says he told them why." ended on a bare question word; now "the reason".

## Left open

- Five record disagreements (OG-29).
- Other world_front sections keep tells and "this world" wording (OG-30).
- Two tellings run under 120 words (Origen and Demetrius, Didymus) because their records are thin; they are not padded.

Verdict: PASS.
