# Card edits: Thomas Cranmer

Batch 8, 2026-11-21. The card is new, so every field is listed with its evidence. Files are under `cic/texts/` except where marked. Names: COX Cranmer's Miscellaneous Writings and Letters (Cox, 1846); FOXE8 and FOXE7 Foxe's Acts and Monuments, vols. 8 and 7; KET the Prayer Books of 1549 and 1552; CLAY the book of 1559; PERK Perkins; NEW Newman. Every cited line was re-read in its file. Where the researcher's sheet gave a line number a few lines off, the number below is the one read (for example the letter to Cromwell is COX 32930-32961, and the birth is COX 422).

## Fields

| Field | Evidence |
|---|---|
| `otherNames` | "Thomas Cranmerus": COX 52206; "Dr. Cranmer": FOXE8 1164. |
| `knownFor` | The brief, paragraphs 1-3, 6-8; COX 23869-23871 (sentence), COX 666-669 and KET 1701-1705 (the books); FOXE8 7516-7519 (hand); CLAY 441-444, 485-488 (1559). |
| `datesNote` | Birth: COX 422, FOXE8 963 and 980-981. Waltham: FOXE8 1122-1124, COX 438. Consecration: COX 463-464. Sentence: COX 23869-23871, COX 468-469. 1549: COX 595-598. Tower, attainder, Oxford, condemnation, the two bishops: COX 705-717. Stripped of rank, burning: COX 744-748; the register COX 52206-52209. |
| `placeNote` | COX 422-424, 438, 23799-23803, 706; FOXE8 7118-7120, 7482-7484; COX 52208-52209 (outside the north wall). |
| `role` | COX 463-464; COX 666-669; the brief, paragraph 1. |
| `keyWorks` 1 | KET 1627-1647, 1696-1705, 13353-13371, 16017-16023; COX 666-669; COX 53461 (preface attributed to him). |
| `keyWorks` 2 | COX 17419, 17506, 17553-17564. |
| `keyWorks` 3 | COX 23797-23811, 23869-23871; COX 32930-32961, 32998. |
| `legacy.traces` 1-4 | CLAY 441-444, 485-488; the tree's entry for the English Reformation (`legacy`; not a file in `cic/texts/`); COX 491-492, 32975-32977, and the tree's Tyndale entry; COX 599-602. |
| `legacy.remembered` 1-6 | FOXE8 7544-7551; FOXE8 7552-7558; FOXE8 7529-7537 (the friar); PERK 44201-44205; COX 419-420; NEW 10433-10436. |
| `uncertain` 1 | FOXE8 7516-7527; PERK 44212; COX 52303-52312; the tree's entry (the eyewitness letter). |
| `uncertain` 2 | COX 52089-52092, 52125-52128, 52182-52191, 52358-52362; register COX 52202-52212; Sampson COX 52214-52219; chronicle COX 52402-52407; FOXE8 7394-7412. |
| `uncertain` 3 | FOXE8 7403-7404; PERK 44206-44212. |
| `uncertain` 4 | FOXE8 6924-6934; FOXE8 7394-7399. |
| `uncertain` 5 | COX 51905-51912, 51919-51922, 51931-51933, 52017-52029, 52044-52046; FOXE8 7009-7023; COX 52292-52297. |
| `uncertain` 6 | FOXE8 7029-7033; COX 42719-42728. |
| `uncertain` 7 | FOXE7 45576-45581; the tree's documented story (not a file in `cic/texts/`). |
| `uncertain` 8 | KET 1627-1647; COX 53456-53462, 666-669; the tree's entry (`voices`). |
| `uncertain` 9 | KET 13353-13371; the sheet's note that the 1549 Act is not held. |
| `uncertain` 10 | COX 519-522; FOXE8 7544-7548; COX 647-653. |
| `uncertain` 11 | COX 32930-32961, 32975-32977, 491-494. |
| `uncertain` 12 | COX 23797-23811, 23869-23871; FOXE8 1122-1124, 1163-1168, 1231-1233; COX 438, 487-489, 461-464. |
| `uncertain` 13 | COX 17553-17564, 599-602. |
| `uncertain` 14 | The tree's entry for the English Reformation (`documentedStories`, `voices`, `legacy`). |
| `uncertain` 15 | COX 426-431, 455-458. |
| `sources` | One entry for each file the card cites. |
| `briefReferences` | One line for each paragraph of the brief. |

## Quoted spans

| Span in the brief | Entry | Status |
|---|---|---|
| "For many years the service ... built up by it." | COX 48899-48901 | awaiting second reading |
| "like a Christmas game," | COX 17555 | checked at card |
| "My hand did wrong when it wrote against my heart. ... burned first." | FOXE8 7403-7404 | awaiting second reading |
| "unworthy right hand" | FOXE8 7524 | checked at card |
| "Lord Jesus, receive my spirit." | FOXE8 7526 | checked at card |

Each `modern` is the brief's wording exactly (taken from the brief file by pattern, including the comma inside the second span). No `secondReading` is written for the two long ones.

## Conflicts and claims to check

1. **The hand speech cannot pass the line check as it stands.** The Foxe scan reads "oflended" and "pimished" and runs marginal notes ("seth the" at the start of 7403, "pope, as" at the start of 7404) into the sentence. The `printed` text gives the corrected readings. Perkins (PERK 44210) prints "offended" cleanly; for "punished" he prints a damaged form ending "unifhed" (PERK 44211), so that reading is confirmed only in part, and Perkins copies Foxe. The validator needs readings in `tools/quote_scan_readings.json` for the two words and a drop for the two marginal fragments; I did not edit that file. If the card checker holds that "punished" is not confirmed, the entry loses its printed wording and the span has no original, since no other held print of the speech exists.
2. **The preface.** The brief's span is printed from Cox's print (COX 48899-48901), because in Ketley's print a footnote and a page heading stand inside the sentence (KET 1631-1643), as with any line check across them. The words are the same. The preface is unsigned; the brief says "the preface", not Cranmer by name.
3. **The tree's entry for the English Reformation** (the starting list for a new person) differs from the held sources in four places, all in `uncertain` 14: "signed six recantations" (the bishop's book prints six papers, whose authorship is disputed); "chief architect of the Book of Common Prayer" (the sources say he led its making); "watched Ridley and Latimer burn from the roof of his prison" (no held source; Foxe says the reverse at that moment, FOXE7 45576-45581); the King James Bible beside the Prayer Book (outside his work). Its "burned at Oxford in 1556" holds.
4. **Not found:** that Foxe's text of the scene has no named informant (the sheet says so; I could not check a whole volume, so the card does not say it). The year of his second marriage: the scan of Cox reads "153^" (COX 455), so the card gives no year. That Foxe's 1563 is the first English edition is in the tree's entry, not in a held file; the card says only "Foxe". The sheet's claim that Cox's note names the Bible as "Thomas Matthew" holds (COX 32975-32977).
5. **The year of death in Cox's scan reads 1550 (COX 747);** the bishop's register gives 1556 (COX 52206-52209). The card uses 1556 and says so.
6. **Credited, not told as fact:** Foxe for the hand, the choice put to him, the morning and the queen's motive; the bishop's printed book and register for the submissions and the public withdrawal; Cox, an admiring editor, for the 1552 revision and the rising's outcome; Tyndale's share is the editors' finding.
7. **Not on the card:** Foxe's verdict and the friar's reading of the fire are in `legacy.remembered`; the pope's foot and the earl's spaniel, the Ely handshake and the bowls beyond one clause are Foxe's colour and are not on the card; Lady Jane Grey is not named.
