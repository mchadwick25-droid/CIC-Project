# desert Atlas story pass: review round 1, 2026-10-17

Reviewer: Opus 5.5, site-editing thread, with independent Opus reviews that did not draft the text. Scope: the participant-facing text this pass changes on the Desert monasticism Atlas card and tradition page, and the placed story tellings.

## What changed

- `Build/worlds/desert/surface/world_front/desert.front.desert-monasticism.md`
  - `skim.tile.text`: rewritten without "this world", contrast framings or claims no record supports.
  - `orientation.story`: 629 words before and 637 after. The project lead read and approved it.
  - `orientation.documented_stories`: 3 entries became 10, in date order. The three existing teasers are rewritten. The burial title now reads "Buried Where Only Two Men Knew", and the angel story reads "Pachomius, the Angel and the Brass Tablet". `kellia-day` (a reconstruction with no telling) and `virgin-who-hid-athanasius` (its record forbids dating it on a card) stay off the card.
  - `orientation.highlights`: 28 notes on people, terms, councils and places (new field). Places cite Pleiades with `url` and `verified_on`.
- `records/desert/story/*.md`: fixes to ten existing tellings and a new Amma Sarah telling. Desert has `story_placement` on, so these tellings are spoken word for word in live conversations. The project lead approved every change and chose the framed Sarah telling, 2026-10-17. The `antony-secret-burial` telling was clean and is unchanged.

## Checks

| Check | Method | Result |
|---|---|---|
| Story, tile, teaser and note claims | Every sentence traced to its `grounded_in` records and, for quotes, numbers, names and sequence, to the vendored source. An independent rigor and craft review, then a targeted recheck | Pass after fixes (below) |
| Telling claims | Each telling read against its record and the vendored source by an independent review | Pass after fixes (below) |
| Decision 24 | Quotation marks hold only exact `modern_rendering` words | Pass after fixes |
| Highlight ids and kinds | Every `grounded_in` id resolves; kinds are person, term, council or place | Pass |
| Readability | `engine.m10.cli regate desert --base origin/main`; tellings scored by hand with `gates.grade_text` | PASS. Tellings FK 3.0 to 7.3, FRE 71.8 to 93.2, no sentence over 25 words |
| Records gate | `engine.m10.cli records desert` | PASS |
| Empty tails | The project lead's ruling, 2026-10-17 | Applied to story, tile, teasers, notes and tellings |

## Findings fixed

1. Claims in the old story that no record supports are cut: a second gift "weeks later", land given "that same day", "no fixed hours of prayer for everyone" (Cassian gives a fixed twelve psalms), a marketplace beside the cells at Kellia, Pachomius's "first" community with a written rule, and an editorial line about "a correction that was probably right".
2. The Cassian line now says what he says. The monks felt Theophilus's Easter letter went against Scripture, which they took to give God a human form.
3. The old burial teaser had Antony say "not even you". The Life of Antony says no one but the two men knew.
4. Tellings: five quotations in older translations replaced with the exact `modern_rendering` of their quote records (Pachomian rule superscription, Antony in the tombs, Arsenius, Moses, Sarapion). The tomb attack is kept as Athanasius's account, and Pachomius's seven thousand as "some seven thousand". Cassian's "after our image" restored. Sentences over 25 words split, a colon reveal removed, and an unclear pronoun fixed.
5. Amma Sarah: "brethren" became "brothers", and the telling now frames the saying with her `bridge_line` and the record's own `modern_contrast`, so the lone saying cannot be misread.

## Recordings

Voice `A9evEp8yGjv4c3WsIKuY`, model `eleven_v4`, speed 1, tempo 1, stability 0.75, similarity 0.75, style 0, speaker boost on, the existing Desert settings in `cic-website/audio/worlds/manifest.json`, read from the run's printed settings. The project lead approved a sample of story unit 1 (484 characters, 235 credits). Full run: the story and the ten card stories, 13,772 characters, 6,679 credits. Durations by ffprobe: story 4 min 27 s; tellings 21 s to 98 s.

## Left open

- Other world_front sections (gaps OG-35).
- The readability gate does not score tellings (gaps OG-35).

Verdict: PASS.
