# Rendering Review: rzg quote records, batch 1 (6 records)

- **Reviewer:** Opus 5.5 (independent; did not draft or render any of these records)
- **Date:** 2026-11-03
- **Subject:** the `text` and `modern_rendering` of 6 `rzg.quote` records.

## Method

Each record's `text` is compared against the vendored file in `cic/texts/` named by its source record's `edition` field, at the locus lines. Line-end hyphens are rejoined and whitespace folded. A word that differs only by an OCR letter error ("onr" for "our") counts as present. "..." in a record marks an elision and is checked as one. Each `modern_rendering` is checked clause by clause against the edition text, then against `use_note.not_for` (no `divergence_note` is set on these six). Sentence length is counted by hand in words, splitting at full stops.

Files read: `schaff_second-helvetic-confession-heidelberg-catechism_1919.txt`, `zwingli_selected-works_jackson1901.txt`, `calvin_institutes-christian-religion-vol3_beveridge1845.txt`, `calvin-zurich-pastors_consensus-tigurinus-mutual-consent-sacraments_beveridge1844.txt`, `zwingli_latin-works-correspondence-vol1_jackson1912.txt`.

## Results
**6 records: 6 PASS, 0 FAIL (0 P1, 0 P2).**

| Record id (rzg.quote.…) | Edition text at (file, lines) | Text check | Rendering check | Verdict |
|---|---|---|---|---|
| christ-the-mirror-of-election | cic/texts/schaff_second-helvetic-confession-heidelberg-catechism_1919.txt, lines 667 and 684-685 | pass (elisions mark dropped "and what God has decreed..." and "therefore,"; "[our]" is in the edition, OCR "onr") | "out of Christ" as "apart from Christ" is accurate; both elisions kept; longest 15 | PASS |
| mass-not-a-sacrifice | cic/texts/zwingli_selected-works_jackson1901.txt, lines 4564-4568 | pass | all clauses: once, forever, sure and valid, all the faithful, not a sacrifice, remembrance and assurance; longest 18 | PASS |
| seniors-selected-from-the-people | cic/texts/calvin_institutes-christian-religion-vol3_beveridge1845.txt, lines 2830-2832 | pass | "seniors" as "elders" and "bishops" as "pastors" avoid misleading modern senses; Calvin uses the titles interchangeably (line 2810); longest 13 | PASS |
| signs-and-things-signified | cic/texts/calvin-zurich-pastors_consensus-tigurinus-mutual-consent-sacraments_beveridge1844.txt, lines 768-770 | pass | distinguish / "as we ought" / do not separate the reality from the signs, all kept; trailing elision kept; longest 22 | PASS |
| taught-better-from-scripture | cic/texts/zwingli_selected-works_jackson1901.txt, lines 4487-4492 | pass (elision marks dropped "and I offer to protect and conquer with the said articles,") | all clauses incl. "called inspired by God", "not now correctly understood", "only from said Scriptures"; longest 19 | PASS |
| zwinglis-last-words | cic/texts/zwingli_latin-works-correspondence-vol1_jackson1912.txt, lines 1592-1593 | pass | both sentences rendered; "it is true" kept; the "It was reported" frame (line 1584) sits outside the quote and is carried by `speaker_or_author`; longest 12 | PASS |

## Failed renderings: corrected text

None. All six renderings meet the bar.
