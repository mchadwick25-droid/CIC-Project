# Card check: Hermas

Card checker, batch 6, 2026-11-19, per `Card_Check_Prompt.md`. Checked: `hermas.card.json` against `Card.existing.json` (the same as the census `card`), `Card_Edits.md`, the brief, the outline, the sheet and the held files. Short names as in `Source_Sheet.md` (HE, MUR-L, MUR-E, TERT, TERT-L, IREN).

**Verdict: FIX** (five changes, below), and two scan readings to list.

## 1. Each edit is justified

- **uncertain**, one item added at the end: the Rhoda variant stands at HE 648–652 (text and Crombie's note) and HE 591–605 (Vat. and Lips.). "Rhoda" for Crombie's "Rhode" follows the outline (Names).
- **sources.about**, five added (Routh's Latin, Irenaeus, Clement, Athanasius, Jerome): justified. Routh and Irenaeus are cited by quote entries; the other three by `briefReferences`.
- **briefReferences**, thirteen lines: checked below.
- **quotationOriginals**, six entries: checked below.
- Clearly wrong: none claimed, and I found none.

## 2. Nothing else moved

Diffed field by field. Only `uncertain` (one item after the existing four), `sources` (five after the existing three), `briefReferences` and `quotationOriginals` differ. Every other field is word for word.

## 3. References

Remaining, after the fixes below: (1) Vision 1.1, Rhoda and the Tiber; (2) Vision 2, the book, the fixed day, the Church; (3) Vision 3, the tower, the stones, the rich; (4) Vision 5, the shepherd; (5) Commandment 4.3; (6) Similitude 10.2, the ending; (7) Irenaeus 4.20.2; (8) Clement, *Stromata* 2.13; (9) Eusebius 3.3; (10) the Muratorian Canon; (11) Tertullian, *On Modesty* 1 and 20; (12) Athanasius, Festal Letter 39; (13) Jerome, *Illustrious Men* 10. The only quotation marks are around "the Scripture declared", verbatim in the brief.

Three parts name things the brief does not tell:
- (3) "built on the water": the brief has only "a tower being built". FIX 1.
- (10) "while his brother Pius was bishop of Rome": the brief never names Pius or the brother. FIX 2.
- (13) "read publicly in some churches of Greece": the brief tells only that the Latin West had almost forgotten it; its "Some churches read it aloud" rests on Eusebius 3.3, line (9). FIX 3.

## 4. Census rules

Keys allowed; no `briefLength`. Six quoted spans in the brief, six entries, each `modern` the brief's span exactly. Every `printed` and `englishPrinted` stands at its file and lines, and every cited file is in `sources`. No audit, review or ruling named. American spelling outside printed wording ("favours" is Tertullian's English, verbatim). `secondReading` absent on all six: correct, as all are new.

One wording copies a scan fault: the Muratorian Latin `printed` carries "publieari" (MUR-L 22082), and its `uncertain` names the scan to explain it. Routh prints "publicari" (the outline and the sheet read it so). With a reading listed, the true word stands and the note on the scan goes. FIX 4.

## 5. Originals

Quotes from the *Shepherd* are rendered from Crombie's English; its Greek and Latin are not held (Outline, Quotes). The Muratorian quote is rendered from Routh's Latin, and the card carries it, with the English beside it.

The Tertullian phrase is not. The sheet holds Tertullian in Latin and renders from it (`Source_Sheet.md`, "Original language"; I6: "illo apocrypho Pastore moechorum", TERT-L 74596–74597), and the outline lists TERT-L among its sources. The brief's "the Shepherd of adulterers" follows the Latin "Pastore moechorum"; the English puts "apocryphal" inside the phrase. `Card_Edits.md` leaves the Latin out because the scan reads "moecbomm". That is a scan fault only, so FIX 5 adds the Latin with a reading, and adds TERT-L to `sources`, since the entry cites it.

Each reading was applied in the validator's way and the wording then checked with its folding: both stand.

Scan faults, for `tools/quote_scan_readings.json`:
- MUR-L line 22082: scan `sed publieari)`; reads `sed publicari)`.
- TERT-L line 74597: scan `moecbomm`; reads `moechorum`.

```json
{
 "file": "cic/texts/apologists-fragmentary_reliquiae-sacrae-vol1-lat-grc_routh1846.txt",
 "lines": "22082",
 "scan": "sed publieari)",
 "reads": "sed publicari)",
 "kind": "OCR misread (e for c)"
},
{
 "file": "cic/texts/tertullian_quae-supersunt-t1-apologetica-lat_oehler1853.txt",
 "lines": "74597",
 "scan": "moecbomm",
 "reads": "moechorum",
 "kind": "OCR misread"
}
```

## 6. Not found, and anything clearly wrong left in

`Card_Edits.md` lists nothing as not found, and notes that Origen's own words calling the book inspired are not held, only Crombie's report of them (HE 516–523); the existing item says no more than that report, so it stays. Its line correction for the Muratorian Latin (22081–22084, not the sheet's 22077–22083) is right. The existing claims it re-read hold, and none contradicts the brief. Nothing else clearly wrong was found.

## FIX

**FIX 1.** `briefReferences[2]`
- Old: `Vision 3, chapters 2 to 6: the tower built on the water, the stones set aside that can still be built in if their owners repent before it is finished, and the round stones of the rich that must be cut square, turned on Hermas himself.`
- New: `Vision 3, chapters 2 to 6: the tower, the stones set aside that can still be built in if their owners repent before it is finished, and the round stones of the rich that must be cut square, turned on Hermas himself.`

**FIX 2.** `briefReferences[9]`
- Old: `The Muratorian Canon, in Routh's Latin and the English of the Ante-Nicene Fathers: written very recently, while his brother Pius was bishop of Rome; to be read, but not made public in church to the people, nor placed among the prophets or the apostles.`
- New: `The Muratorian Canon, in Routh's Latin and the English of the Ante-Nicene Fathers: written very recently; to be read, but not made public in church to the people, nor placed among the prophets or the apostles.`

**FIX 3.** `briefReferences[12]`
- Old: `Jerome, Lives of Illustrious Men 10: read publicly in some churches of Greece, almost unknown among the Latins.`
- New: `Jerome, Lives of Illustrious Men 10: almost unknown among the Latins.`

**FIX 4.** `quotationOriginals[4]` (So it ought indeed to be read ...). Needs the MUR-L 22082 reading.
- `printed`, old: `Et ideo legi eum quidem oportet, se publicare ( for. sed publieari) vero in ecclesia populo, neque inter prophetas completum (for. completos) numero, neque inter apostolos, in finem temporum potest.`
- New: `Et ideo legi eum quidem oportet, se publicare ( for. sed publicari) vero in ecclesia populo, neque inter prophetas completum (for. completos) numero, neque inter apostolos, in finem temporum potest.`
- `uncertain`, old: `The manuscript reads "se publicare"; the rendering follows the editors' correction "sed publicari", which this scan prints as "publieari". The brief quotes the first part of the sentence; the rest says the book cannot be placed among the prophets or the apostles.`
- New: `The manuscript reads "se publicare"; the rendering follows the editors' correction "sed publicari". The brief quotes the first part of the sentence; the rest says the book cannot be placed among the prophets or the apostles.`

**FIX 5.** Needs the TERT-L 74597 reading.
- `quotationOriginals[5]` (the Shepherd of adulterers): add after `"lines": "9330-9331"`
  - Old: (no `original`, `originalFile`, `originalLines`)
  - New:
```json
"original": "illo apocrypho Pastore moechorum",
"originalFile": "cic/texts/tertullian_quae-supersunt-t1-apologetica-lat_oehler1853.txt",
"originalLines": "74596-74597"
```
- `sources.about`: add at the end, after the Jerome entry
  - Old: (no entry for TERT-L)
  - New:
```json
{
 "title": "On Modesty, chapter 20, in Latin (ed. Franz Oehler)",
 "author": "Tertullian of Carthage",
 "date": "1853",
 "language": "Latin",
 "file": "cic/texts/tertullian_quae-supersunt-t1-apologetica-lat_oehler1853.txt"
}
```

None of the fixes changes modern wording, so the six spans stay "awaiting second reading" as `Card_Edits.md` lists them.
