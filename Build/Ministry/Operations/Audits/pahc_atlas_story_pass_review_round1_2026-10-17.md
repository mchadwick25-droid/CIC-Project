# pahc Atlas story pass: review round 1, 2026-10-17

Reviewer: Opus 5.5, site-editing thread, with three independent Opus reviews that did not draft the text. Scope: the participant-facing text this pass changes on the House Churches Atlas card and tradition page.

## What changed

- `Build/worlds/pahc/surface/world_front/pahc.front.post-apostolic-house-church.md`
  - `skim.tile.text`: rewritten. It now says households, drops Rome "asking for" the elders back, and drops "this world" and a dash aside.
  - `orientation.story`: 8 units of 917 words became 8 units of 642 words, under five minutes aloud. The project lead read and approved it.
  - `orientation.documented_stories`: 3 entries became 10, in date order. Seven episodes cut from the story are added. The three existing teasers are rewritten.
  - `orientation.highlights`: 22 notes on people, terms and places (new field). Places cite Pleiades 658381, 550893, 570182, 501482 and 981512, checked 2026-10-17.
- `records/pahc/story/*.md`: a `telling` on the ten stories shown on the card. The project lead read and approved all ten.

## Checks

| Check | Method | Result |
|---|---|---|
| Story, tile, teaser and note claims | Every sentence traced to its `grounded_in` records and, for quotes, numbers and attributions, to the vendored source in `cic/texts/`. Two passes: a fact-check, then a fresh rigor and craft review | Pass after fixes (below) |
| Telling claims | Each telling read against its record and the vendored source. Two passes, as above | Pass after fixes (below) |
| Decision 24 | Quotation marks hold only exact `modern_rendering` words | Pass. Two quotes remain, from `pahc.quote.first-concerning-the-cup` and `pahc.quote.two-female-slaves-who-were-called-deaconesses` |
| `use_note.not_for` | Read per record | Respected after the Justin fix (below) |
| Highlight ids and kinds | Every `grounded_in` id resolves; kinds are person, term or place | Pass |
| Readability | `engine.m10.cli regate pahc --base origin/main`; tellings scored by hand with `gates.grade_text` (OG-34) | PASS. Tellings FK 5.7 to 8.6, FRE 64.5 to 78.7, no sentence over 25 words |
| Records gate | `engine.m10.cli records pahc` | PASS |
| Schema | `engine.m9.cli check` | Clean |
| Empty tails | The project lead's ruling, 2026-10-17: cut closing sentences that say nothing new | Applied to story, tile, teasers, notes and tellings |

## Findings fixed

1. The project lead caught "Christians met in ordinary homes". The core record says "communities gathering in households". The tile carried the same error as "ordinary houses". Both now say households, and "house to house" became "from one household to the next".
2. The tile said Rome's letter asked for the elders back. 1 Clement 44 argues only that such men cannot justly be removed, and OG-27 and OG-29 had already removed this claim.
3. The story quoted Pliny in the old translation, then dropped "nothing but", which reversed his point. It now quotes the modern rendering in full.
4. Story unit 7 said the gospel "does not teach this", which read as losing nerve. Martyrdom of Polycarp 4 says the gospel does not teach giving oneself up.
5. Hedges restored: letters "under Ignatius's name"; one bishop "becoming the dominant pattern" by 200; the gathering at Polycarp's bones as a hope; "legitimate teaching and practice" per the round 3 ruling; the state's danger always present while incidents came and went.
6. The Pliny telling put the torture of the two women before the account of the meetings. It now follows the letter. The record's own text still has the old order (OG-33).
7. The Quintus telling said the letter names Quintus before praising Polycarp, and that Polycarp spent his last days at the country house. Both now follow the source (OG-33).
8. The Justin telling said "what we do", claiming Justin's Roman order for the whole tradition, against `use_note.not_for`. It now says "what his community at Rome does".
9. Every old-translation quote in the tellings is now a modern rendering or plain reported speech.
10. Smaller fixes: the Domitian date follows `use_note.years`; the Polycarp teaser says "put to death"; first mentions of Ignatius, Polycarp, Justin and Tacitus are introduced; unclear pronouns in four teasers; build wording ("the sources", "carried at full strength") removed.

11. A targeted recheck after the recording found that the Quintus telling said the letter tells of him "first". Germanicus comes first, in chapter 3. It also found empty tails left in six tellings. Those six were fixed, an independent reviewer re-confirmed them, and they were re-recorded. The fix had cut the Nero telling's only single-episode line, which the reviewer blocked. That line is restored.

## Recordings

Voice `1gkXJMvrzBWAwt0XqBaa`, model `eleven_v3`, speed 1.12, tempo 1.15, stability 0.35, similarity 0.93, style 0, speaker boost on, read from the run's printed settings. The project lead approved a sample of story unit 1 (281 characters, 136 credits). Full run: story and ten tellings, 15,480 characters, 7,505 credits. Re-record of six tellings: 5,923 characters, 2,872 credits. Durations by ffprobe: story 4 min 9 s; tellings 47 s to 97 s.

## Left open

- Six story records' own text disagrees with the source (OG-33).
- The readability gate does not score tellings (OG-34).
- Other world_front sections and a stale body note (OG-35).

Verdict: PASS.
