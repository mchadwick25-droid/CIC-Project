# Rendering Review: gallic quote records, batch 3 (28 records)

- **Reviewer:** Opus 5.5 (independent; did not draft or render any of these records)
- **Date:** 2026-11-03
- **Subject:** the `text` and `modern_rendering` of 28 `gallic.quote` records.

## Method

Every record's `text` was checked against the vendored edition `cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml` at the file lines its `sources[].locus` names. The edition lines were read directly; a script then stripped `<note>…</note>` blocks and all other tags, rejoined line-end hyphens, unescaped entities, folded curly and straight quotation marks, and folded whitespace including U+00A0. Each `text` (split at "..." where it marks an elision) was then tested for a verbatim match, and the tight span was found by narrowing to the first line holding the quote's first word and the last line holding its last word. Any miss was re-read by eye at the raw lines.

Each `modern_rendering` was read clause by clause against the edition passage, and checked against the record's `confidence.divergence_note` and `use_note.not_for`. Sentence lengths were counted by script (split at sentence-final punctuation, words counted by whitespace) and every sentence over 22 tokens was recounted by hand, leaving dashes out of the count.

## Results

**28 records: 26 PASS, 2 FAIL (1 P1, 1 P2).**

| Record id (gallic.quote.…) | Edition text at (file, lines) | Text check | Rendering check | Verdict |
|---|---|---|---|---|
| martin-if-christ-bore-with-judas | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 5330-5339 | pass | all clauses; "rather injured the man who uttered them" kept; "presbyterate" as priesthood; longest 21 | PASS |
| martin-imagined-soldiers-speech | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 2438-2453 | pass | all clauses of the speech; standard, declining years, "good, O Lord, is thy will" kept; longest 20 | PASS |
| martin-kept-the-virtues-of-a-monk | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 1123-1125 | pass | "objects and virtues of a monk" as aims and virtues; longest 13 | PASS |
| martin-offers-to-stand-unarmed | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 842-863 | pass | all clauses; conditional recast as question with the same sense; "who can doubt" kept as Sulpitius's; longest 25 | PASS |
| martin-on-the-christ-with-wounds | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 1809-1813 | pass | second sentence runs to 29 words | FAIL P2 |
| martin-power-present-catechumen-raising | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 995-1000 | pass | all clauses; "perceiving … that power was present" as sensed, waiting kept; longest 15 | PASS |
| martin-raises-the-catechumen | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 977-1007 | pass | all clauses; "as it were" kept; "ejaculations" as cries of prayer; longest 21 | PASS |
| martin-rebukes-the-devil-and-dies | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 2474-2484 | pass | witness frame "those who were there have told us" kept; "as if" kept; longest 21 | PASS |
| martin-refuses-the-donative | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 827-842 | pass | all clauses; donative as bonus payment; reason for discharge kept; longest 22 | PASS |
| martin-sackcloth-and-ashes-reply | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 2464-2466 | pass | both clauses; longest 13 | PASS |
| massilians-clung-to-their-views | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 15767-15770 | pass | "perhaps" kept; editor's voice unchanged; longest 19 | PASS |
| no-others-than-bishops | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 1938-1941 | pass | "very few" and "were reported" kept; longest 25 | PASS |
| no-steady-tradition-from-antiquity | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 1176-1178 | pass | "he said" frame kept; "scruples" as doubts of conscience; longest 15 | PASS |
| nobles-forced-down-afterwards-made-bishops | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 1153-1155 | pass | all clauses; "numbers of these" as many of them; longest 15 | PASS |
| not-an-author-but-a-keeper | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 13769-13774 | pass | every paired antithesis kept; fragments mirror the source's own; longest 25 | PASS |
| not-i-but-the-grace-of-god-with-me | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 25038-25044 | pass | all three Apostle quotations kept; longest 22 | PASS |
| one-substance-three-persons | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 13059-13060 | pass | both halves exact; longest 9 | PASS |
| paphnutius-accused-and-the-book-found | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 43018-43039 | pass | all clauses; "never happened since" kept; σειρά as seira; longest 21 | PASS |
| paphnutius-asks-for-a-plan-of-repentance | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 43040-43058 | pass | all clauses to the elision; stated fear kept; longest 23 | PASS |
| paphnutius-bubalis-and-the-brothers-envy | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 43004-43012 | pass | all clauses; Joseph simile kept; longest 24 | PASS |
| paphnutius-lay-the-same-foundation | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 43079-43084 | pass | both sentences; "if we want to attain" kept; longest 19 | PASS |
| paphnutius-the-brother-hides-his-own-book | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 43012-43018 | pass | all clauses; "as if" with a clean conscience kept; longest 21 | PASS |
| paphnutius-the-thief-possessed-and-healed | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 43058-43079 | pass | all clauses; Isidore's unfailing gift kept; reserved cure kept; longest 24 | PASS |
| perfection-not-gained-without-grace | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 25167-25170 | pass | "not my own opinion, but that of the elders" kept; "these" = human efforts per line 25166; longest 15 | PASS |
| pope-stephen-no-innovation | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 12527-12528 | pass | both clauses; longest 14 | PASS |
| postumianus-you-have-conquered-all-the-eremites | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 4103-4107 | FAIL | vocative "O Gaul" and the frame "said Postumianus" dropped, following the defective `text` | FAIL P1 |
| private-fancy-be-he-a-bishop | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 14271-14275 | pass | all clauses to the cut; every rank kept; longest 16 | PASS |
| private-fancy-of-his-own | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 14271-14278 | pass | all clauses; "lest" as otherwise; "utmost peril" kept; longest 19 | PASS |

## Failed renderings: corrected text

**martin-on-the-christ-with-wounds** (FAIL P2). The second sentence runs to 29 words, past the limit. "Come back" also adds a return the edition does not state; the edition says only "come".

Corrected rendering:

> The Lord Jesus did not foretell that he would come dressed in purple, with a glittering crown on his head. I will not believe that Christ has come unless he appears in the look and form in which he suffered. He would also have to show openly the marks of his wounds from the cross.

**postumianus-you-have-conquered-all-the-eremites** (FAIL P1). The edition at lines 4103-4105 reads: "You have conquered, O Gaul," said Postumianus, "you have conquered, although certainly not me…". The record's `text` joins the first and second "you have conquered" into one, with no elision mark, and drops the vocative and the speech frame. The `text` is therefore not verbatim, and the rendering, built from it, loses who is speaking and to whom.

Corrected rendering:

> "You have conquered, O Gaul," said Postumianus. "You have conquered - though certainly not me. On the contrary, I am a supporter of Martin. I have always known and believed all these things about that man. But you have conquered all the hermits and anchorites."
