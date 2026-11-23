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

## Third pass: what it was about (2026-11-23)

Written to `Card.pass2.json` (copy of `council-of-ephesus-431.card.json`, every other field word for word). Brief compared with `council-of-ephesus-431.brief.v3.txt` by `diff`: new explanations at paras 3, 11 and 13; cuts at paras 5, 7, 11; "of Antioch" dropped after first naming. No quotation added or dropped (the four quoted spans are unchanged), so `quotationOriginals` is unchanged.

### Edits

1. `briefReferences`, new entry after the John's-sentence entry (item 7, para 11: "The curses damned anyone who denied Mary was Mother of God or split Christ in two; Nestorius's answering curses condemned making God and man one nature"). New text: "Cyril's anathemas I to III and Nestorius's answering anathemas I to III, in the English edition of the canons, Nestorius's as collected in Latin by Marius Mercator: Cyril's condemn anyone who will not confess the Holy Virgin the Mother of God, or who divides the one Christ; Nestorius's condemn saying that God and man are one and the same in nature." Evidence: `cic/texts/npnf214_seven-ecumenical-councils.xml` 16294-16303, 16306-16318 (I), 16652-16677 (II, III of Cyril), 16660-16667, 16680-16688 (Nestorius's II, III).
2. `briefReferences`, new entry after the Canon VII entry (item 11, para 13: "his accusers charged that he said grace only forgives past sins and shows what to do"). New text: "The council of Carthage of 418, Canons CXI and CXII, in the English edition of the canons: the canons anathematize anyone who says that grace avails only for the remission of past sins, or that it helps only by revealing the commandments. The brief gives this as the charge of his accusers, not as what Pelagius taught." Evidence: same file, 36418-36421, 36504-36507, 36522-36527.
3. `briefReferences` (Canon VII / Celestine entry), old "and Rome's determinations against Pelagius, Caelestius and their followers are upheld" → new "and Rome's determinations against Pelagius are upheld". The brief no longer says "his followers" or names Caelestius. Evidence: brief para 13.
4. `briefReferences` (John and his bishops entry), old "cut off from communion and priestly power, the final sentence left to Celestine." → new "cut off from communion and priestly power." The brief no longer says the final sentence went to Rome (para 11 diff).
5. `decided`, new entry after the Canon VII entry (item 10's occasion, sent to the card): "The occasion of Canon VII was a rival statement of how God's Son became man, brought to the council by the presbyter Charisius of Philadelphia. The decree calls it an impious formula composed by Theodore of Mopsuestia (the decree; Canon VII)." Evidence: ACTS 18150-18153 ("the impious formula composed by Theodore of Mopsuestia, and given to the same holy Synod at Ephesus by the Presbyter Charisius, of Philadelphia"), 18171-18173 ("the Exposition introduced by the Presbyter Charisius concerning the Incarnation of the Only-Begotten Son of God").
6. `decided`, new entry after the Pelagius entry (the canons' positive claim on grace, sent to the card): "The council of Carthage in 418, which condemned Pelagius and Celestius, anathematized anyone who says that grace avails only for the remission of past sins, and not for assistance against committing sins in the future. It also anathematized anyone who says that grace helps only by revealing the commandments, and not so that we are able to do what we know we should do. Its own claim is that grace helps people not to sin and to do what they know they should (Canons CXI and CXII, in the English edition of the canons)." Evidence: ACTS 36418-36421 (heading), 36504-36507, 36522-36527. It does not say Ephesus upheld Carthage's canons; the letter to Celestine upholds Rome's determinations (ACTS 18748-18755).
7. `decided`, new entry after John's assembly's sentence (outline "added to his last letter to Nestorius," cut, to the card): "Cyril subjoined his twelve anathemas to his epistle to Nestorius (the epistle, in the acts)." Evidence: ACTS 15964-15965 (heading "The Epistle of Cyril to Nestorius with the XII. Anathematisms"), 16286 ("we have subjoined to our epistle"). "Last" is left out: the held text does not say it.
8. `uncertain`, after "Whether Nestorius taught...": "Nestorius's answering anathemas are held only in the Latin of Marius Mercator, an opponent of his. That they are Nestorius's own is widely accepted." Evidence: outline item 7 (Widely Accepted); ACTS 16306 ("Found best in Migne's edition of Marius Mercator").
9. `uncertain`, next: "What Pelagius himself meant by grace is contested. That the council of Carthage in 418 charged what its canons say is documented. His own answers, as Augustine reports them, claim God's help: that a man is able to be without sin and to keep the commandments of God, if he wishes, and that God is the helper of free will whenever it chooses good." Evidence: outline item 11 (Documented / Contested); `cic/texts/npnf105_augustine-anti-pelagian-writings.xml` 10383, 9524.
10. `sources.writtenLater`, new entry: "On the Proceedings of Pelagius, in the Anti-Pelagian Writings", Augustine of Hippo, English translation, `cic/texts/npnf105_augustine-anti-pelagian-writings.xml`, because edit 9 cites it.

### Skipped

- Item 2 (Mother of Christ, para 3): the existing `briefReferences` entry on Socrates VII.32 and the Bazaar already says it, and `issue` already holds it (BH 6908-6961 re-read: consistent).
- "His followers" and "final sentence to Rome": already on the card (`decided`, Pelagius entry and John's cutting-off entry).
- "Read the emperor's letter" (Candidian beat): `attended` already has Candidian reading the emperor's instructions.
- "Peace two years later", "over the protest of the emperor's officer": `knownFor` and `attended` already hold them.
- Item 8 (the three named heresies): left out of the brief, no card instruction.
- `quotationOriginals`: no change (no span added or dropped).
- Percival's summary of Pelagius (ACTS 18018-18036): the outline marks it not used.
- Fresh_Read_About_Applied has no card correction beyond the above.

### Validator

`node tools/validate-census.mjs --skip-quotes` on a scratch copy of the census with this card and the new brief in place: 0 errors (no errors for this entry).

## Card check applied (2026-11-23)

`Card_Check_About.md` (FIX, two changes), applied word for word: `decided[6]` "which condemned Pelagius and Celestius" → "held against the heresy of Pelagius and Caelestius"; `uncertain[7]` "held only in the Latin" → "held in the Latin".

## Fourth pass: no modern opinion (2026-11-23)

Starting card: `Card.pass3.json`, unchanged. Every field not listed here is word for word.

1. `uncertain`, new entry 16 (the commissioner's month). Old: none. New: Hefele has him arrive "at the beginning of August", called universally admitted; Driver and Hodgson list the arrival under August; both modern judgments; Count John's own Latin report gives no month. Evidence: HEF 4932-4935; Driver and Hodgson chronology, lines 1125-1141; Mansi, tomus 4, 123607-123661 (re-read).
2. `uncertain`, new entry 17 (the dissolution). Old: none. New: Driver and Hodgson say September; Hefele has Cyril reach Alexandria on 30 October 431; the dissolving lines of the edict carry no date. Evidence: Driver and Hodgson lines 262-270; HEF 6203-6207; Mansi, tomus 5, 80115-80129.
3. `uncertain`, new entry 18 (the year of the peace). Old: none. New: Hefele's reckoning from a Latin sermon "probably of the year 433", Tillemont's March 433, the date's slight weight; Driver and Hodgson list 433. Evidence: HEF 7580-7590; Driver and Hodgson lines 1248-1251, 1338-1341.
4. `uncertain`, new entry 19 (the condition). Old: none. New: Hefele's "conditio sine qua non" is his reading; Cyril's letter to Donatus says what he required. Evidence: HEF 7222-7226; Mansi, tomus 5, 35298-35355.
5. `uncertain`, new entry 20 (who refused). Old: none. New: the editors' chronology (Theodoret, Andrew, Alexander, Zeugma in 433) marked as their reckoning; Theodoret's own undated letter. Evidence: Driver and Hodgson lines 1269-1274, 1324-1344; npnf203 37983-38012.
6. Wigram's verdict and Badger's readings: already in `uncertain` (entries 6 and 14), credited and marked as modern; no change.
7. `briefReferences[12]` (commissioner). Old: "Hefele, vol. 3, giving the new commissioner's report ... Hefele's English of the emperor's edict dissolving the council." New: Count John's own Latin report (Mansi, tomus 4) and Hefele's English of it, the same facts, and the edict in Latin (Mansi, tomus 5). Evidence: brief paragraph on the commissioner; M4 123609-123647; M5 80117-80128.
8. `briefReferences[13]` (peace). Old: "the confession of 433 ...; Hefele calls that the condition of communion." New: year and Hefele's condition dropped; Cyril's letter to Donatus added. Evidence: brief ("which Cyril wrote he had required"); M5 35298-35303, 35345-35355.
9. `briefReferences[14]` (Theodoret). Old: "Driver and Hodgson's chronology of the letters of 433: ..." New: Theodoret's own letter to Nestorius. Evidence: brief; npnf203 37998-38011.
10. `briefReferences`, Wigram entry and Badger entry: removed; the brief no longer tells either.
11. `briefReferences`, new last entry: Barhadbeshabba (chapter list; the corner of a church, gold and blows), credited as that church's later history and a hostile charge. Evidence: brief's last paragraph; BB 31905-31911, 34040-34055.
12. `sources`: no change (Mansi 4 and 5, npnf203, Barhadbeshabba and Pusey already there).
13. `quotationOriginals`: no change. The brief quotes four spans, the card has four entries, and no span's words changed.

Validator: `node tools/validate-census.mjs --skip-quotes` on a scratch copy of the census with this card and brief in place: 0 errors for this entry.
