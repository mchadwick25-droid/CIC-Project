# Calibration of the brief measures, 2026-11-24

Mark asked how success is measured ("fidelity to quotes may be important, but its not whole picture") and to test the measures on finished work before any rewrite. This folder holds that test.

## The set

Twelve finished pieces Mark had already judged, given codes P01 to P12 in a random order (`pieces/`). `KEY.json` maps each code to its source and to Mark's verdict before the test. No reader saw the key.

- Judged good: Tacitus as approved by ear (2026-11-19), the Basil and Epiphanius references, the Lutheran Wittenberg narration.
- Judged bad: fix batch 1's Tacitus, Jerome and Catholic Church of the ancien régime; the Post-Apostolic house church entry summary; the Priscillian draft Mark heard.
- Between: live Rufinus, live Ulfila, the Kongo tradition brief.

## Run 1 (`run1/`)

Five listener personas (scholar, pastor, first-time visitor, someone re-evaluating faith, AI skeptic) read without the sources and counted faults and ranked the pieces. A source reader (`reader_C.md`) spot-checked three claims per piece and the quotes.

- The listeners agreed with each other and with Mark at both ends. They disagreed with his verdicts on five pieces: they ranked fix batch 1's Jerome and Tacitus and the Priscillian draft high, and the approved Tacitus and Wittenberg low.
- All five flagged the Priscillian accusation Mark named, but ranked the piece high anyway.
- The source reader's quote check reported most quotes "not found", because the quotes are modern renderings. That check belongs to the census validator.

## Mark's blind reading

Mark read four pieces without labels (`BLIND_MAP.json`): the two Tacitus versions in random order, Jerome, and Wittenberg.

- Tacitus: "A is better, the drama is real, no added lines." A was fix batch 1's rewrite (P03); B was the version approved on 2026-11-19 (P12). On the date: "the exact date after comes out if its not clear."
- Jerome: "opening sentance doesnt make sense, he was in the the desert when?" Against Letter 125.12, the opening also softens Jerome's "the promptings of sin and the natural heat of my blood" to "his restless mind".
- Wittenberg: "it doesnt make sense as its not a clean sentence."
- Then: "there are two things that are essential, it has to remain faithful to the sources, even when summarizing, no added assumptions, that is trust, and it has to be crafted well or people will not listen", and "so the scholor test knows the texts (has them to reference)".

## Run 2 (`run2/`)

Two scholars with the sources open checked every sentence (about 400), marking each held, summary holds, softened, assumption added, modern only or not found. The first-time visitor and the AI skeptic counted craft faults, with three added checks: opening orientation, unclean sentences, and summaries keeping their force.

- The trust gate caught Jerome's softening. It found 2 non-holding sentences in the Tacitus Mark preferred, both editors' dates, against 9 in the other. It found no invented drama.
- Both listeners caught Jerome's missing when and where.
- Every piece failed the trust gate as written, the references included. All twelve predate the rules of 2026-11-24. In about 400 sentences there was one added assumption and nothing invented. The faults were 9 softened summaries and 59 modern-only claims, at least 13 of them dates.
- The unclean-sentence count flagged 6 to 12 sentences in nearly every piece and did not separate Wittenberg from the references. It needs tightening.

Then Mark, on dates: "a, settled dates plainly."
