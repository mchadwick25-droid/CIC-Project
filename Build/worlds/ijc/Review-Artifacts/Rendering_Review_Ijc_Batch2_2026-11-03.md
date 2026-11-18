# Rendering Review: ijc quote records, batch 2 (19 records)

- **Reviewer:** Opus 5.5 (independent; did not draft or render any of these records)
- **Date:** 2026-11-03
- **Subject:** the `text` and `modern_rendering` of 19 `ijc.quote` records.

## Method

Each record's `sources[].locus` was mapped to its vendored edition file in `cic/texts/` (anf07, npnf111, npnf201, npnf202, npnf203, npnf210, npnf211, npnf212, npnf214). Where the locus gives no line numbers, the passage was found by searching a distinctive phrase. A script read each file, blanked `<note>` elements and all tags, decoded entities, folded whitespace (including U+00A0), folded curly and straight quotation marks, and dropped the stray space that tag removal leaves before punctuation. It then searched for the record's `text`, split at each "..." elision, in order, and recorded the first and last line of the match. The raw lines at each span were also read directly, to see what each elision and each bracket covers.

Each rendering was read clause by clause against the edition text. Sentence lengths were counted by script (split at sentence-final punctuation, words counted as letter/digit runs) and checked by hand where a quoted speech sits inside a narrative frame. Each rendering was also checked against the record's `confidence.divergence_note` and `use_note.not_for`. For the bracket rule, the only bracketed supplements in these texts are the editor's "[from heaven]" and "[we believe]" in the Nicene Creed.

## Results

**19 records: 18 PASS, 1 FAIL (1 P1, 0 P2).**

| Record id (ijc.quote.…) | Edition text at (file, lines) | Text check | Rendering check | Verdict |
|---|---|---|---|---|
| lactantius-dream | cic/texts/anf07_lactantius-apostolic-constitutions-didache-liturgies.xml, lines 10620-10620 | pass | all clauses; "cipher" becomes "monogram"; "thus" kept as "like this"; longest 23 | PASS |
| leo-rome-apostles | cic/texts/npnf212_leo-great-gregory-great.xml, lines 20998-21003 | pass | all clauses; "such glory, that..." result kept with "So"; head of the world tied to Peter's See; longest 17 | PASS |
| leo-sinner-be-glad | cic/texts/npnf212_leo-great-gregory-great.xml, lines 14508-14510 | pass | "in that" carried by colon; "gentile" kept; longest 10 | PASS |
| leo-things-secular | cic/texts/npnf212_leo-great-gregory-great.xml, lines 9079-9083 | pass | all clauses; "as we desire" kept; "clemency's rule" becomes "merciful rule"; longest 19 | PASS |
| leo-tome-each-form | cic/texts/npnf212_leo-great-gregory-great.xml, lines 5365-5381 | pass | all clauses; "humility" becomes "lowliness"; "co-operation" becomes "working together"; "form" kept; longest 22 | PASS |
| let-the-ancient-customs-prevail | cic/texts/npnf214_seven-ecumenical-councils.xml, lines 3405-3409 | pass | all clauses; appeal stays to custom; "jurisdiction"/"privileges" become "authority"/"rights"; longest 22 | PASS |
| milan-edict | cic/texts/anf07_lactantius-apostolic-constitutions-didache-liturgies.xml, lines 10684-10684 | pass | both emperors named; "it seemed to us" kept on both points; trailing elision kept; longest 25 | PASS |
| nicene-creed | cic/texts/npnf214_seven-ecumenical-councils.xml, lines 2408-2418 | pass | all clauses; both editor brackets kept bracketed; added "we believe"/"He is"/"He was" are grammatical only; "quick" becomes "living"; longest 19 | PASS |
| no-power-but-of-god | cic/texts/npnf111_chrysostom-homilies-acts-romans.xml, lines 53973-53991 | pass | all clauses; "it may be said" kept as "someone may ask"; rulers-in-general distinction kept; longest 25 | PASS |
| nothing-further-can-it-add | cic/texts/npnf214_seven-ecumenical-councils.xml, lines 20106-20118 | pass | all clauses; elided gloss is the editor's "(fidei regulam in the Latin Acts)"; Leo's title kept; longest 23 | PASS |
| peter-has-spoken | cic/texts/npnf214_seven-ecumenical-councils.xml, lines 19996-20000 | pass | all acclamations; "Anathema" becomes "Cursed be he"; frame plus first acclamation 26, the acclamation itself 12 | PASS |
| secular-ruler-ecclesiastical-cause | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 11652-11660 | pass | all clauses; "He maintained" kept as "He held" on both points; Treves becomes Trier; longest 23 | PASS |
| sin-is-not-done-away-but-by-tears | cic/texts/npnf210_ambrose-select-works-letters.xml, lines 44159-44166 | pass | all clauses; "Who alone can say" kept as "alone can say"; "penitence" becomes "repentance"; longest 25 | PASS |
| socrates-damasus-election | cic/texts/npnf202_socrates-sozomen-ecclesiastical-histories.xml, lines 14203-14214 | pass | all clauses; non-doctrinal cause kept; no figure added; longest 21 | PASS |
| sozomen-thessalonica-law | cic/texts/npnf202_socrates-sozomen-ecclesiastical-histories.xml, lines 40613-40626 | pass | all clauses; historian's "made known by this law" and "enacted" frames kept; longest 24 | PASS |
| the-reading-of-all-the-documents | cic/texts/npnf203_theodoret-jerome-gennadius-rufinus.xml, lines 3288-3292 | pass | all clauses; "vulgar cries" becomes "cries of a mob"; "Suffer" becomes "Allow"; frame plus speech 26, the speech itself 15 | PASS |
| the-rewards-of-virginity-the-merits-of-widowhood | cic/texts/npnf210_ambrose-select-works-letters.xml, lines 45073-45079 | pass | all clauses; ranking kept; "conjugal modesty" becomes "chaste married life"; longest 23 | PASS |
| the-rudiments-of-the-creed | cic/texts/npnf212_leo-great-gregory-great.xml, lines 5140-5151 | pass | all clauses; the dropped footnote sits after "born again"; "rudiments" becomes "basics"; longest 25 | PASS |
| vc-conquer-by-this | cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml, lines 61203-61208 | pass | time of day and inscription moved outside "He said that", so they read as the narrator's own claims; longest 23 | FAIL P1 |

## Failed renderings: corrected text

**vc-conquer-by-this.** In the edition, the hour ("about noon, when the day was already beginning to decline") and the inscription both sit inside Constantine's report: "He said that ... he saw ...". The rendering moves both into new sentences ("This was about noon ..."; "It bore the inscription ..."). Those sentences have no "he said", so they now read as Eusebius stating the details himself. This drops the reported-speech frame for a vision the record's own `not_for` presents as Constantine's later telling.

Corrected rendering:

> He said that he saw with his own eyes the victory sign of a cross of light in the sky, above the sun. He said this was about noon, when the day was already beginning to decline. The sign, he said, bore the inscription, "Conquer by this." At this sight he himself was struck with amazement. So was his whole army, which followed him on this expedition and witnessed the miracle.
