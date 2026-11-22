# Card edits: Apollinaris of Laodicea (`apollinaris-of-laodicea`)

Existing card `Card.existing.json` (equal to the census card) kept word for word. No existing statement was found clearly wrong, so every edit below is an addition. Written to `apollinaris-of-laodicea.card.json`. Checked with `tools/validate-census.mjs` on a scratch copy of the census with the card and brief set in. The only errors are the ones the release step clears: no `secondReading` on the four quotations (each is six words or more, left out as instructed), and the brief's four modern quotations not yet listed in `tools/quote_renderings.json`. Every cited wording stands in its lines. Short names are those of `Source_Sheet.md`.

## Clearly wrong

None. The existing claims were checked against held lines, among them Gregory's "most grievous item of all" (GNAZ 44510-44513, held), Lietzmann on Sozomen's credibility and on the grammar (LIETZ 2573-2575, 7726-7740, held), Sozomen's "it is said" (SOZ-ENG 39073-39083) and the Roman council's date (SOZ-ENG 39033-39035). Nothing in the card contradicts the brief.

## New

- **`sources.about` titles extended** (nothing else in the lines changed): Sozomen 6.22 (SOZ-ENG 38725-38731); Theodoret 5.37 (THDT 18040-18046); the Second Council of Constantinople (553), anathema 11 (COUNC 23852-23856).
- **`sources.about`, nine entries added:** Athanasius, Tome to the Antiochenes (ATH 60170-60173); Epiphanius, Panarion 77 (EPIPH-PG42 48853-48966); Rufinus, Church History 11.20 (RUF 30635-30653); Basil, Letters 263 and 265 (BAS 43311-43314, 43445-43447); Philostorgius (PHIL 472); Vincent of Lérins (VINC 12904-12944); Theodosian Code 16.5 (CTH 7075-7080, 7126); Hefele vol. 3 (HEF3 876-893); Pusey's Cyril, with his notes (PUSEY 1251-1299).
- **`legacy.traces`, eight added:** Socrates on his later followers' Trinity (SOC-ENG 9961-9964; E3); Theodoret's returned followers and Theodotus of Antioch (THDT 15476-15482, 18040-18046; I3, the outline's What came of them 2); the laws of 383, 384, 388 and 397 (CTH 7075-7080, 7126; E13); the statement of faith to Jovian (LIETZ 12943-12949, 12986-12988; HEF3 876-893); Cyril in 429 and Leontius (LIETZ 4714-4719; PUSEY 1279-1299; I1); Hefele's watchword (HEF3 886-893); Justinian's charge and who "they" are (LIETZ 5718-5723, 5752-5764; I2); 553 (COUNC 23852-23856; I5, the outline's What came of them 4).
- **`legacy.remembered`, seven added:** the father and son and their offices (SOC-ENG 9930-9938; SOZ-ENG 39066-39067; S1, cut-first item 1); the first expulsion under Theodotus (SOZ-ENG 39052-39070; E1, Leave out); Sozomen's ranking beside Athanasius (SOZ-ENG 38725-38731; cut-first item 4); Epiphanius (EPIPH-PG42 48853-48857, 48959-48966; E7); Basil (BAS 43311-43314, 43445-43447; E9, card only); Philostorgius (PHIL 472; E3, card only); Vincent of Lérins (VINC 12904-12944; I4, cut-first item 5).
- **`uncertain`, nine added:** Rufinus on where the teaching began (RUF 30635-30638; Do not say); Rufinus's two stages (RUF 30638-30646; SOC-ENG 9957-9961; cut-first item 3); Vitalius, two accounts (THDT 15538-15539; SOZ-ENG 39006-39020; cut-first item 2); when he became bishop (ATH 60170-60173; LIETZ 823-835); the date of Jerome's lectures (LIETZ 3460-3464); Julian's works dated 362 (LIETZ 497-499) and Hierapolis (SOZ-ENG 36720-36722); who wrote the statement to Jovian and who put the names on (LIETZ 4151-4157, 5752-5753, 5764; HEF3 876-893; PUSEY 1251-1277, 1296-1299; Do not say); Epiphanius held only in a damaged scan (EPIPH-PG42; LIETZ 3498-3499; VINC 12906-12910; E7); the books destroyed, not burned (LIETZ 4133-4160; Do not say).
- **`briefReferences`:** eight lines, one for each part of the brief, with its source. No quotation marks.
- **`quotationOriginals`:** four, one for each quoted span.
  - Fragment 81: printed from LIETZ 11480-11481, the Greek, checked by hand against the rendering ("complete" for τέλειος; φησί, Gregory's, noted and left out). No English print is held.
  - Sozomen's songs: printed from SOZ-ENG 39027-39028, the English alone, since the Greek (SOZ-GRC 13406-13414) is a damaged scan.
  - One nature of God the Word made flesh: printed from LIETZ 12986-12987, the Greek, checked by hand.
  - Justinian: printed from LIETZ 5754-5756, the Greek, checked by hand ("they" are his opponents; ὡς given as because).
- **Left out of the card:** the scene at Antioch in 381 (THDT 15485-15506), Gregory's letter to Nectarius (already carried by the existing uncertain line), Epiphanius's report of exile (not checked in the Greek), the Apollinarian bishop at Nazianzus, the conference with the Severians (damaged scan), Alypius, Socrates's argument for the classics (all on the outline's Leave out and not sent to the card), `label`, `briefLength`, `secondReading` and connections.

## Not found

Nothing in the existing card was left unsupported. One date differs between held sources and is stated as each gives it: the sheet puts Leontius of Byzantium in the sixth century, and Pusey's preface (PUSEY 1251-1277) places him at the beginning of the seventh. The card follows Pusey's wording for what Pusey says and names no century of its own.
