# syr Atlas story pass: review round 1, 2026-10-17

Reviewer: Opus 5.5, site-editing thread, with three independent Opus reviews that did not draft the text. Scope: the participant-facing text this pass changes on the Syriac Edessa and Nisibis Atlas card and tradition page.

## What changed

- `Build/worlds/syr/surface/world_front/syr.front.syriac-edessa-nisibis.md`
  - `skim.tile.text`: rewritten without "this world", contrast framings or claims no record supports.
  - `orientation.story`: 8 units, 588 words before and 640 after. The project lead read and approved it.
  - `orientation.documented_stories`: 3 entries became 10, in date order. The three existing teasers are rewritten.
  - `orientation.highlights`: 30 notes on people, terms, councils and places (new field). Places cite Pleiades 658457 (Edessa), 874623 (Nisibis), 893976 (Ctesiphon) and 511268 (Nicaea), checked 2026-10-17.
- `records/syr/story/*.md`: a `telling` on all ten story records. The project lead read and approved all ten.

## Checks

| Check | Method | Result |
|---|---|---|
| Story, tile, teaser and note claims | Every sentence traced to its `grounded_in` records and, for quotes, numbers, names and sequence, to the vendored source. An independent rigor and craft review, then a targeted recheck | Pass after fixes (below) |
| Telling claims | Each telling read against its record and the vendored source. An independent review, then the targeted recheck | Pass after fixes (below) |
| Decision 24 | Quotation marks hold only exact `modern_rendering` words | Pass |
| `use_note.not_for` | Read per record. The Basil legend may be told only with its correction, which the teaser and telling carry | Pass |
| Highlight ids and kinds | Every `grounded_in` id resolves; kinds are person, term, council or place | Pass |
| Readability | `engine.m10.cli regate syr --base origin/main`; tellings scored by hand with `gates.grade_text` | PASS. Tellings FK 5.4 to 7.9, FRE 63.0 to 82.3, no sentence over 25 words |
| Records gate | `engine.m10.cli records syr` | PASS |
| Empty tails | The project lead's ruling, 2026-10-17 | Applied to story, tile, teasers, notes and tellings |

## Findings fixed

1. Claims in the old story that no record supports are cut: Syriac as close to Jesus' own language; Ephrem as the greatest hymn-writer; Ephrem and Aphrahat preaching from the harmony for the whole period; a teacher's word mattering as much as an office; Nisibis remembering its bishops as its fathers; Ephrem turning Bardaisan's hymn-forms against his followers; Persia's church receiving one structure for the first time in 410; the aphorism ending.
2. Simeon bar Sabbae: the story and telling now follow Sozomen. There is no tax-collector refusal, and he is not "first" of the bishops killed (item 35).
3. The roll-and-vine teaser said only the Syriac Paradise records the dreams. Gwynn's prolegomena give them from other sources. It now says they appear in the Syriac Paradise but not in the Greek Palladius.
4. The choirs telling's inversion line ("The very music that had carried error became the carrier of the faith") is cut.
5. The Basil telling stated a disputed identification as settled. It now attributes it to modern scholars.
6. Hedges are placed beside the claims they qualify (the flood line's originality, the Abgar legend, the roll-and-vine attribution). Empty tails are cut, people are introduced at first mention, and unclear pronouns are fixed.

## Recordings

Voice `9iUwwAQbShIkp628a5fO`, model `eleven_v4`, speed 1, tempo 1, stability 0.7, similarity 0.75, style 0, speaker boost on, read from the run's printed settings. The project lead approved a sample of story unit 1 (515 characters, 250 credits). Full run: the story and ten tellings, 14,122 characters, 6,848 credits. Durations by ffprobe: story 4 min 17 s; tellings 45 s to 93 s. The M9 check then found two telling lines the horizon and voice gates reject: roll-and-vine dated Palladius to 420, after the window closes, and the Basil quote's "this world's wisdom" read as outside talk. Both were fixed (the date dropped, the quote given as reported speech) and the two tellings re-recorded: 2,269 characters, 1,100 credits.

## Left open

- Story records whose own text disagrees with the source (item 35).
- Other world_front sections, and the Jacob of Nisibis voice (item 36).
- The readability gate does not score tellings (item 37).

Verdict: PASS.
