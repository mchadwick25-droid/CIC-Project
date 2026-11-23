# Pelagius: card edits

Card: `pelagius.card.json`, from `Card.existing.json`. Every field not listed here is word for word. `briefLength` is not written (the census allows no such key). `secondReading` is left out on all three quotations (each is six words or more); release sets it.

## New

1. **`quotationOriginals`** (new key, three entries, one per quoted span in the brief).
   - Riches passage. Modern: the brief's span "But spiritual riches ... from you and in you." Printed: Warfield's English, `cic/texts/npnf105_augustine-anti-pelagian-writings.xml` lines 1281-1282. The Latin (Migne PL 30 811-817; PL 33 62414-62419; Goldbacher 4490-4496) is held only in damaged prints, so the card prints the English alone and says so in `uncertain`.
   - Food and poison. Modern: the brief's span "'These good things can only be in you' ... wholly poison." Printed: Latin, `cic/texts/augustine_epistulae-critical_goldbacher-csel57-pars4.txt` lines 4513-4515, read with Migne PL 33 62421-62424 (the other held print; it too is damaged, "ex u\"). The eight scan faults in those three lines are listed in `tools/quote_scan_readings.json` (added: possnnt, boua, ni.i, optinie, uerissiine, piane, oinniuo, uirns). No English print of this letter passage is held.
   - Zosimus. Modern: "Is there any passage in which God's grace or help has been left out?" Printed: Latin, `cic/texts/collectio-avellana_epistulae-imperatorum-pontificum-v1-lat_guenther1895.txt` lines 11229-11230 (clean print; line-end hyphen "praeter-/missum"; second print Mansi vol. 4 35654-35656).
2. **`briefReferences`** (new key, 17 entries), one for each source the brief draws on. Each is checked against the brief's sentences and the cited lines. No quotation marks.
3. **`sources.about`**, nine entries added after the existing five, so that the quotations and references cite files the card holds: Letter 188 (PL 33 and Goldbacher), Zosimus (Collectio Avellana), the emperor's order of 30 April 418 (Mansi vol. 4), Prosper's Epitoma Chronicon, Marius Mercator, the Carthage canons and the Ephesus letter (NPNF series 2, vol. 14), Cassian On the Incarnation I.3 (NPNF series 2, vol. 11), Bede II.19 (Giles).
4. **`tools/quote_scan_readings.json`**: eight readings appended for Goldbacher lines 4513-4515 (see 1). Nothing else in that file changed.

## Sent to the card by the outline, review and fresh read

New entries added at the end of the list, nothing existing moved.

| Field | New words | Evidence |
|---|---|---|
| `legacy.traces` | Augustine answered the book on nature without naming him; Timasius and Jacobus put it in his hands | NPNF105 10294-10295 (friendly relation, name left out), 10299 ("his former disciples"); outline Cut first 4 |
| `legacy.traces` | A letter from Rome to the Irish in Bede's History: "again springs up among you", "abolished these two hundred years" | `bede_ecclesiastical-history-english-people_giles1903.txt` lines 5395-5426 and following (quotes stand in the print); outline "Leave out" (Rome's letter to the Irish) |
| `uncertain` | Augustine first heard his name at Rome with praise; glimpsed him once or twice; notes on Paul's letters, not held | NPNF105 10285-10286, 4627; Source sheet S3, E2; outline Cut first 1, 2, 5 |
| `uncertain` | Letters produced at Diospolis; "God is its helper whenever it chooses good" | NPNF105 10276, 9524; outline Cut first 11 |
| `uncertain` | Zosimus: a layman; slandered by Heros and Lazarus | AVELL 11233-11234, 11277-11278; NPNF105 9491 (Heros and Lazarus, Gaul); outline Cut first 6, 10 |
| `uncertain` | The letter to Demetrias written at her mother's request; ascribed by others to Julian (Bede) and Caelestius; shown to be Pelagius's by On the Grace of Christ | PL30 157-160 (petente sancta matre ... jubente), 66-81 (Migne's Monitum); outline Cut first 8, 9, 14 |
| `uncertain` | Mercator's Syrian Rufinus | MERC 6998-7005; outline "Leave out" |
| `uncertain` | "hound of Albion (Pelagius)" in Fremantle's summary; the bracket is Fremantle's | `npnf206_jerome-principal-works.xml` 47929-47936 (Commentary on Jeremiah, heading at 47870); Source sheet S1; outline "Leave out" |
| `uncertain` | Julian of Eclanum and eighteen Italian bishops deposed | NPNF105 942 (Warfield); outline "Leave out" |

## Clearly wrong

None found. The existing card agrees with the brief and with the held sources I re-read (Warfield 880, 905, 920, 928, 942; Fremantle 1729; Gennadius ch. 43; Augustine 4627, 10270, 10381, 11255). The validator accepts every quotation in the existing card.

## Not found, left in place

None.

## Not carried to the card

Outline items I could not re-read in a held print within this pass, so they are not written: Faustus of Riez on grace, Constantius of Lyon's "Pelagius the author" (the held OCR of the Vita Germani did not match on search), Vincent of Lérins (his held line names Caelestius, not Pelagius), the Lives of David (late legend). Connections to other entries are left out as told.

## Second pass (2026-11-23)

### Checker changes

1. FIX 1, `quotationOriginals[0]` (riches passage): applied word for word (Latin print at PL30 814-817, the English kept as `englishPrinted`, `englishFile`, `englishLines`, new `uncertain`).
2. FIX 2, `quotationOriginals[1].printed`: opening quotation mark restored. Applied word for word.

### Scan readings to add

For `tools/quote_scan_readings.json` (not edited here):

```json
{"file": "cic/texts/pelagius_epistula-ad-demetriadem-lat_migne.txt", "lines": "815", "scan": "poterii", "reads": "poterit", "kind": "OCR misread"},
{"file": "cic/texts/pelagius_epistula-ad-demetriadem-lat_migne.txt", "lines": "815", "scan": "in bis", "reads": "in his", "kind": "OCR misread"},
{"file": "cic/texts/pelagius_epistula-ad-demetriadem-lat_migne.txt", "lines": "816", "scan": "caeleris", "reads": "caeteris", "kind": "OCR misread"}
```

### Items added from the outline

| Field | Exact text | Evidence |
|---|---|---|
| `legacy.traces` | Bede, writing in 731, calls him "a Briton" who spread "far and near" the infection of his doctrine against the assistance of God's grace. | `bede_ecclesiastical-history-english-people_giles1903.txt` 919-920; outline Links, card only (bede-of-jarrow) |
| `legacy.traces` | Vincent of Lérins, in 434, asks who before "that profane Pelagius" gave free will so much strength "as to deny the necessity of God's grace to aid it towards good in every single act". | `npnf211_sulpitius-severus-vincent-lerins-cassian.xml` 13960-13963 and 14011-14018 (Commonitorium ch. 24); outline Who tells it, later witnesses |
| `legacy.traces` | Faustus of Riez, about 474, begins the list of chapters of his book On Grace with the view of Pelagius, who denied grace, which he says must first be destroyed. | `faustus-riez_de-gratia-and-collected-works_engelbrecht1891.txt` 3644-3646 (OCR chapter heading); outline Links, card only (faustus-of-riez) |
| `legacy.traces` | Constantius of Lyon, about 480, in his Life of Germanus, sets two sides of a public dispute against each other: on one side divine authority, on the other human presumption; on one side Pelagius as author, on the other Christ. Bede copies the passage. | `constantius-lyon_vita-germani_levison1920.txt` 2830-2834; Bede `...giles1903.txt` 1469-1473; outline Links, card only (constantius-of-lyon) |
| `sources.about` | Faustus, On Grace; Constantius, Life of Germanus; Vincent, Commonitorium (three entries) | the files above, so each cited file is in `sources` |

### Skipped

- Items 1, 2, 4, 5, 6, 8, 9, 10, 11 and 14 of the Cut first list, the Rome-to-the-Irish letter, Julian and the eighteen bishops, the dating disputes, the Jerome Dialogue note, Prosper, Mercator and Gennadius: already on the card from the first pass.
- Review 4 (Britain 429) and Review 5 (letters read at Diospolis): the brief still tells the first, and the card already holds the second.
- `paulinus-of-milan` (accused Caelestius): the outline cites only NPNF105 10287, which says Caelestius came before a tribunal and does not name Paulinus.
- The Lives of David: the outline gives no line, calls it late legend, and the Source Sheet says Leave out.
- Outline Cut first 3, 7, 12, 13: marked Leave out, not for the card.

### Validator

`node tools/validate-census.mjs --skip-quotes` on a scratch census with this card: the only errors for `pelagius` are `secondReading` absent on the three quotations (release sets it). The `printed` error on the riches passage clears once the three scan readings above are in the readings file.
