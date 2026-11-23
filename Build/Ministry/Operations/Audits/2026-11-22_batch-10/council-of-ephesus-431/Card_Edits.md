# Card edits: Council of Ephesus (431)

Card: `council-of-ephesus-431.card.json`, from `Card.existing.json`. Everything not listed here is word for word as before.

## Corrections (2)

1. `uncertain[5]`, on the Church of the East. Old: "says they never accepted it, never formally rejected it, and were never asked to;". New: "says they had not accepted it, nor formally rejected it, and had never been asked to;". Evidence: Wigram, `cic/texts/wigram_introduction-to-the-history-of-the-assyrian-church-100-640_1910.txt` lines 9271-9274 ("had certainly not accepted Ephesus ... nor had they formally rejected it ... nor had they ever been asked to do either"); the brief's Wigram sentence ("had not accepted this council, nor formally rejected it ... never been asked to do either").
2. `record[6]`, Wigram. Old: "Argues that it never accepted or formally rejected Ephesus." New: "Argues that it had not accepted Ephesus, nor formally rejected it." Same evidence.

## New: quotationOriginals (4, one per quoted span in the brief)

3. Nestorius, "Who was judge? Cyril. ...": printed English, Driver and Hodgson, `nestorius_bazaar-of-heracleides_driver-hodgson1925.txt` 8645-8647. Syriac not held; Nau's French of the same Syriac (`nestorius_livre-d-heraclide-de-damas-fra_nau1910.txt` 7137-7139) checked and named in `uncertain`. No `secondReading` (six words or more).
4. Candidian, "I warned you of this ...": printed Lupus's Latin in the same Bazaar file, 7767-7768; Driver and Hodgson's English from the Syriac as `englishPrinted`, 7821-7822; Mansi tomus 5 lines 76917-76919 (damaged scan) named in `uncertain` as the second print. No `secondReading`.
5. "by persuasion and force" (under six words): printed Hefele, `hefele_history-of-the-councils-v3-431-451_clark1883.txt` 4977-4978; `secondReading` "checked at card"; English only, noted.
6. The confession of 433: printed Pusey's English, `cyril-alexandria_three-epistles-grc-eng_pusey1872.txt` 5217-5222. English alone: the Greek (Pusey 3519-3525, Hefele 7243-7245) is in two damaged prints, and a clean Greek failed the validator's check against the lines in a trial, so it is not printed. No `secondReading`.

## New: briefReferences (16 lines) and sources

7. `briefReferences` added: 16 lines, no quotation marks, each line from the sheet's lines re-read in the files.
8. `sources` added: `fromThoseThere`, Letter CLII (`npnf203_theodoret-jerome-gennadius-rufinus.xml`, 36836-36880); `writtenLater`, Evagrius (`evagrius-scholasticus_ecclesiastical-history_walford1846.txt`, 1303-1307, 1331-1345) and Badger vols. 1 and 2 (`badger_nestorians-and-their-rituals-v1_1852.txt` 7676-7681, `-v2_1852.txt` 5921-5929).

## New: items the outline sent to the card (appended at the end of each field)

9. `attended`, three: Candidian's four-day request and Hefele on its being disregarded (`nestorius_bazaar...` 7804-7813, 929-948; Hefele 2997-3002); Hefele's 126 and 34 (Hefele 3054-3068); the legates' confirmation at Session III (ACTS 17615-17625, 17657-17659 in `npnf214_seven-ecumenical-councils.xml`).
10. `decided`, two: Canon VIII on Cyprus (ACTS 18395-18427); the Messalians (ACTS 18769-18803).
11. `outcome`, five: the emperor's edict on the Orientals and the eight delegates (Hefele 6189-6196; `nestorius_bazaar...` 1178-1185); the 433 formula as the one given the emperor at Ephesus (Hefele 7156-7161; Bazaar 1144-1153); John's letter on Nestorius's deposition, Maximian, Hefele's "condition", the twelve anathemas unmentioned (Hefele 7463-7477, 7222-7226; Bazaar 1323-1325); Cyril's opening of the letter of peace (ACTS 19428-19430); Zeugma and Theodoret (Bazaar 1271-1273, 1326-1343).
12. `record`, three: Candidian's protest; the Eastern bishops' report (Letter CLII, 36836-36880); Evagrius.
13. `uncertain`, six: why John was late, with Evagrius and the sixty-eight bishops (ACTS 18574-18599; Hefele 2933-2941, 2992-2997; Evagrius 1303-1307); what Candidian did (ACTS 17826-17834; Letter CLII editor's note; Bazaar 8625-8657); the torches (Mansi tomus 4 109151-109189; Hefele 3273-3291); Barhadbeshabba on signatures (`po09_barhadbeshabba...` 34044-34056; ACTS 15818-15830); Badger on the rites and Sleewa's account of 1332 (Badger v2 5921-5969); Chalcedon's letter to the Easterns as the letter of peace (ACTS 19395-19415, 20256-20262).

## Claims not found

None left in place that I could not support. The validator's remaining errors on this entry are the three `secondReading` verdicts and the three modern renderings, which release adds from the second readings.

## Scan readings to add

For `tools/quote_scan_readings.json`, file `cic/texts/hefele_history-of-the-councils-v3-431-451_clark1883.txt`, each with `"kind": "OCR misread"`:
- line 7244: `πύριον` reads `κύριον`
- line 7244: `ἀσυγχύτευ ἱνώσεως` reads `ἀσυγχύτου ἑνώσεως`
- line 7244: `ὁμολογοῦμεν τὸν` reads `ὁμολογοῦμεν τὴν`
- line 7245: `διοτόκον` reads `θεοτόκον`

## Second pass (2026-11-23)

### The checker's changes

1. `quotationOriginals[3]` (the confession of 433): `original`, `originalFile` (Hefele) and `originalLines` "7243-7245" added, and its `uncertain` note changed as worded: applied word for word. The four scan readings are listed above. Item 6 above no longer holds.
2. `quotationOriginals[2]` `uncertain` (Quote 3, "by persuasion and force"): applied word for word.
3. `briefReferences` entry 4 (message from two of John's metropolitans removed) and entry 14 ("and the order of Ephesus kept" removed): applied word for word.
4. `attended`, four items (the two metropolitans' message; Nestorius's word that he would appear; the acclamations and Philip on Peter; Candidian at John's assembly), `decided`, one item ("with many tears"), and the `calledBy` addition on the edict's order: applied word for word.

### Items added from the outline

- `attended`: "Socrates of Constantinople says Cyril made some delay and did not arrive until near Pentecost, and that Juvenal of Jerusalem arrived five days after Pentecost (Socrates, Church History VII.34)." Outline Cut first 1 (credit to Socrates for Cyril's arrival). Evidence: `cic/texts/npnf202_socrates-sozomen-ecclesiastical-histories.xml` lines 20886-20890 (Chapter XXXIV, line 20874).
- `outcome`: "Barhadbeshabba's history also gives a chapter as a reply to the accusations of the impious Cyril, by which the good deeds of saint Nestorius will be known (in Nau's French)." Outline Cut first 2 ("pious and a saint"). Evidence: `cic/texts/po09_barhadbeshabba-ecclesiastical-history-part2-and-others-fra_1913.txt` lines 31910-31911 (chapter title XXI, the scan reads "saint Xestorius").

### Skipped

- Every other "to the card" item (fifty bishops, Celestine's earlier condemnation, Candidian as protector, two hundred signatures, Pelagius upheld, Cyril home and Maximian, the 433 offer to the emperor, Chalcedon's order, the counts, John's horses, Evagrius, the sixty-eight, the torches, the envoys, Capreolus, Canon VIII, the Messalians, the eight delegates, the emperor's edict, the signatures charge, Badger, Sleewa, Socrates's order, retreat and date, Candidian's alleged starving): the card already holds each (see items 9 to 13 above and the starting card).
- Items the checker already worded: skipped as step 1 covers them.
- Chalcedon's condemnation of those refusing the name Mother of God: marked an optional clause, not "to the card".

### Validator

`--skip-quotes` against a scratch copy of the census with this card in place: no errors for this entry.
