# rzg Atlas story pass: review round 1, 2026-10-17

Reviewers: Opus 5.5, site-editing thread, and independent Opus 5.5 subagents that had not drafted or authored the text (a full check of the story, teasers and highlights; a check for add-on tails across the pass; a full check of the tellings). Scope: the participant-facing text this pass changes on the Zurich and Geneva Atlas card and tradition page.

## What changed

- `Build/worlds/rzg/surface/world_front/rzg.front.the-reformed-cities-zurich-and-geneva.md`
  - `orientation.story`: 12 units, about 1,200 words, became 9 units, 641 words, under five minutes aloud. The project lead approved it.
  - `orientation.documented_stories`: the three existing stories stay, in date order, with teasers reworded to their records.
  - `orientation.highlights`: 26 notes on people, terms, councils and places (new field). Zurich, Geneva and Strasbourg cite Pleiades; Savoy has no usable entry and gives no modern location.
- `records/rzg/story/*.md`: a `telling` on all three story records, authored by Opus. The project lead approved them.
- Recordings of the story and the three tellings, after the project lead approved a sample by ear: 6,629 characters, 3,214 credits.

## Checks

| Check | Method | Result |
|---|---|---|
| Story claims | Each sentence traced to its unit's `grounded_in` records, not to the old text | Pass after fixes (below) |
| Telling claims | Each telling read against its story record | Pass |
| Quotes | Zwingli's last words against `rzg.quote.zwinglis-last-words` and the vendored Myconius text | Pass |
| Hedges | Myconius not on the battlefield; reported words; what he was told | Kept |
| `use_note.not_for` | Read per record | Respected |
| Places | Live Pleiades JSON, 2026-10-17 | Pass |
| Readability | `engine.m10.cli regate rzg --base origin/main` | PASS |
| Records gate | `engine.m10.cli records rzg` | PASS |

## Findings fixed

1. The old story called the reforms "five years apart"; the records date them 1519 and 1536. Not repeated (Open_Gaps entry 71).
2. The Consensus Tigurinus question gave two options on the same side of `rzg.contested.zwinglis-remembrance-vs-negotiated-consensus`; later removed as a tail.
3. "Calvin shaped it at Geneva" made Calvin shape Zwingli's work, against `rzg.core` `horizon`. Now "Zwingli began Zurich's reform, and John Calvin later shaped Geneva's".
4. Infant baptism for the whole city was the council's position; `rzg.witness.why-the-children-too` gives it as the reform's own. Now "Zwingli's side".
5. "Did not trust a letter" rested only on `modern_contrast`. Removed.
6. "Mocked the gathering in advance" rested on no claim field. Now the record's "tinker's day" (Open_Gaps entry 71).
7. Highlights: the Consensus "signed by Zurich and Calvin" is now "agreed by Zurich and Geneva"; "bread and cup" is now "bread and wine"; Savoy's "its Prince-Bishop" is now "the Prince-Bishop".
8. The project lead's ruling, "remove all the add on tails that dont say anything": the Myconius source note, the open-question line, "no blow from outside" and an aphoristic opener are removed.

## Left open

- "Five years apart" in the tile and core horizon, and "in advance" in the Hegenwald figure record (Open_Gaps entry 71).
- Other world_front sections and the body note (Open_Gaps entry 72).

Verdict: PASS.
