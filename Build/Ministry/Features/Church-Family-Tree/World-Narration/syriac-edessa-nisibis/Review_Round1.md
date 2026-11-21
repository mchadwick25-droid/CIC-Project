# Review, round 1: syriac-edessa-nisibis

| Piece | Verdict | Grade | Ease (names out) | Findings |
|---|---|---|---|---|
| story | REVISE | 9.1 | 67.3 | 1 PRE-EXISTING |
| legacy | PASS | 9.1 | 62.1 | 1 MINOR |
| abgar-addai-legend | REVISE | 7.9 | 80.3 | 1 BLOCKING, 1 MINOR |
| basil-legend | PASS | 8.0 | 71.9 | none |
| choirs-tradition | PASS | 8.8 | 70.6 | 1 MINOR |
| edessa-flood-201 | PASS | 6.6 | 78.4 | 2 MINOR |
| ephrem-famine-death | REVISE | 7.4 | 78.4 | 1 BLOCKING |
| ephrem-roll-and-vine | PASS | 6.9 | 82.7 | none |
| jacob-deliverance | PASS | 8.6 | 74.2 | none |
| jacob-nicaea | PASS | 8.2 | 69.6 | 1 MINOR |
| qyama-morning | PASS | 8.7 | 68.3 | none |
| simeon-martyrdom | PASS | 8.4 | 70.4 | none |

All 12 pass the hard limits (`python -m engine.m1.profile_readability`, 0 failing). Five pieces score under grade 8; each was read by ear and none is flat.

## Quotes

| Piece | Span | Record | Source file, line | Result |
|---|---|---|---|---|
| story | "One day, my brothers, I picked up a pearl." | syr.quote.a-pearl-upon-the-palm (and two siblings) | cic/texts/npnf213_gregory-great-ephraim-syrus-aphrahat.xml, 21794-21795 | modern_rendering; supported |
| simeon-martyrdom | "As time went on, the Christians grew in number. ... priests and deacons." | syr.quote.symeon-and-usthazanes | cic/texts/npnf202_socrates-sozomen-ecclesiastical-histories.xml, 28873-28875 | modern_rendering; supported |
| edessa-flood-201 | "And they destroyed the temple of the church of the Christians." | syr.quote.the-temple-of-the-church-of-the-christians; syr.quote.chronicle-flood-line | cic/texts/chronicle-of-edessa_cowper.txt, 53 | Cowper verbatim (records' `text`), not modern_rendering; may stand, plain sense given by the narrator |
| edessa-flood-201 | "More than two thousand men were killed ... the sound of mourning." | syr.quote.the-temple-of-the-church-of-the-christians | cic/texts/chronicle-of-edessa_cowper.txt, 53 | modern_rendering; supported |
| ephrem-famine-death | "Then trust me," / "See, on your behalf I appoint myself to take in and care for the needy." | syr.quote.palladius-hospitaller | cic/texts/palladius_lausiac-history_clarke1918.txt, 471 | modern_rendering; supported |
| jacob-deliverance | "he called down no other curse on them than that mosquitoes and gnats should be sent against them." | syr.quote.theodoret-gnats | cic/texts/npnf203_theodoret-jerome-gennadius-rufinus.xml, 11174-11175 | modern_rendering; supported |

Every span is identical to the original's. No BLOCKING-QUOTE.

## Patterns

- Over-joining. Twice the rewrite joined sentences that were not choppy into long ones (ephrem-famine-death, 46 words, blocking; edessa-flood-201, 33 words, minor). The ruling allows joining only where the original is choppy.
- "These churches" stands in for "this world" in story, legacy, abgar-addai-legend and jacob-nicaea. It is third person and holds on the world page; it leans on that page for its sense.
- The one PRE-EXISTING finding (story: "Ephrem's hymns show" the choirs) is the kind the choirs piece already gets right: later accounts are the witness.
