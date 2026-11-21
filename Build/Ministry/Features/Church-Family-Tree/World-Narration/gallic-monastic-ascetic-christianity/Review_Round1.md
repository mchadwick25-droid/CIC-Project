# Review Round 1: gallic-monastic-ascetic-christianity

The reviewer read each rewrite against its original, its sheet and the grounding records, and checked the cited passages in `cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml`. Scores are from `python -m engine.m1.profile_readability`, and all 12 pass the hard limits.

| Piece | Verdict | Grade | Ease (names out) | Findings |
|---|---|---|---|---|
| story | PASS | 7.7 | 75.3 | 1 MINOR |
| legacy | PASS | 7.6 | 75.8 | none |
| docstory-gallic.story.brictio-in-the-courtyard | REVISE | 8.7 | 70.0 | 1 BLOCKING |
| docstory-gallic.story.death-of-martin-at-condate | PASS | 6.6 | 80.8 | none |
| docstory-gallic.story.discharge-before-caesar | PASS | 6.5 | 79.3 | 1 MINOR |
| docstory-gallic.story.election-at-tours | PASS | 8.7 | 68.8 | none |
| docstory-gallic.story.germanus-scruple-at-morning-service | PASS | 7.3 | 81.0 | none |
| docstory-gallic.story.honoratus-and-the-island | PASS | 7.7 | 77.3 | none |
| docstory-gallic.story.raising-of-the-catechumen | REVISE | 6.7 | 79.4 | 1 BLOCKING |
| docstory-gallic.story.the-angel-and-the-twelve-psalms | PASS | 7.1 | 77.0 | none |
| docstory-gallic.story.the-cloak-at-amiens | PASS | 7.5 | 75.9 | none |
| docstory-gallic.story.trier-and-the-ithacian-communion | PASS | 8.9 | 71.3 | none |

Nine pieces score under grade 8. On the listener read, none of them is flat or reads as a children's book, so this is not a finding.

## Quotes

The world holds one quoted span.

| Piece | Span | Quote record | Source |
|---|---|---|---|
| brictio-in-the-courtyard | "Come here, Brictio, come here, Brictio." | gallic.quote.brictio-called-by-demons-on-the-rock (the span stands in its modern_rendering) | npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 5294-5295: "'Come hither, Brictio, come hither, Brictio.'" |

## Pattern

In two pieces, the rewrite replaced the world's own "we" or "us" with a named group that the source does not hold.

- In raising-of-the-catechumen, "used to tell us" became "told Martin's household". The source, line 1013, has only "was wont to relate".
- In brictio-in-the-courtyard, "the one we all knew" became "the one his household all knew". The source, line 5291, has "which you all know", which is Gallus speaking to his listeners in the Dialogues.

Where the source does name who heard, the rewrite got it right. In death-of-martin-at-condate, the witnesses "have testified to us", where "us" is Sulpitius, and the rewrite has "told Sulpitius". In trier, "his own household" is the record's own phrase. The fix in the revision is to name a recipient only when the source names one, and otherwise to say "used to tell" with no listener.

No piece had a PRE-EXISTING finding.
