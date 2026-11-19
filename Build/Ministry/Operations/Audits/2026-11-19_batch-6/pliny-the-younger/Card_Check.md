# Card check: Pliny the Younger

Card checker, batch 6, 2026-11-19, per `Card_Check_Prompt.md`. Checked: `pliny-the-younger.card.json` against `Card.existing.json` (the same as the census `card`), `Card_Edits.md`, the brief, the outline and the held files. Library short names as in `Card_Edits.md` (ML, EU, TE, TL, JC).

**Verdict: FIX** (four changes, below).

## 1. Each edit is justified

- **uncertain[1]**: justified. ML 2758–2819 prints Letters 10.96 and 10.97 in Latin, "ed. C FW Müller" (ML 2760); no other Pliny text is in `cic/texts/`. The old "holds no edition of Pliny" was contradicted by a held file. Only the first sentence changed.
- **sources**: justified. Mirbt (ownWords), Oehler's Tertullian and Jerome's Chronicle (about) are each cited by a `quotationOriginals` entry or drawn on by the brief.
- **briefReferences** and **quotationOriginals**: new, checked below.

## 2. Nothing else moved

Diffed field by field. Only `uncertain`, `sources`, `briefReferences` and `quotationOriginals` differ; inside `uncertain` only item 1, and inside `sources` only the three additions. Every other field is word for word.

## 3. References

Remaining, after the fix below: nine lines, one per brief paragraph 1–9: (1) Letters 10.96, never attended a trial; (2) McGiffert's note and Mirbt's dates; (3) the questions, the threat, led away, citizens to Rome, Tertullian and Eusebius on the outcome; (4) the list and the test; (5) the worship and the two women; (6) every age and rank, the temples, room for repentance; (7) Trajan's reply; (8) Tertullian's Apology 2; (9) Eusebius, Jerome, McGiffert. No quotation marks.

One part names something the brief does not tell: "a friend of Trajan" (the brief says only "a man of letters"). FIX 1.

## 4. Census rules

Keys allowed; no `briefLength`. Seven quoted spans in the brief, seven entries, each `modern` the brief's span exactly (Tertullian's two spans, split by the narrator's sentence, as two entries). Every `printed` and `original` stands at its file and lines, and every cited file is in `sources`. No audit, review or ruling named ("ruling" in the card is Trajan's). American spelling. `secondReading` is absent on all seven: correct, as all are new.

## 5. Originals

The outline renders Quotes 1, 2 and 3 from held Latin (Outline, Quotes: ML 2777–2779; ML 2811, 2816; TL 11728–11730). The card gives the Latin only for the second half of Quote 3 and for "our age". The other three fail only on scan faults in the held files. FIX 2–4, each with its reading for `tools/quote_scan_readings.json`. Each was checked against the file with the validator's folding and the readings applied: all three stand.

Scan faults:
- ML line 2777: scan `minatus ;  15` (the margin line number "15" run into the line); reads `minatus ;`.
- ML line 2814: the running head `6  Das  altrömische  Taufbekenntnis.  —  Das  Jüngere  „apostolische"  Symbol.` set inside Trajan's sentence, between "deferantur" (2811) and "et" (2816); dropped.
- ML line 2816: scan `argiiantur`; reads `arguantur`.
- TL line 11728: scan `0  sententiam` (zero for the letter O); reads `O  sententiam`.

```json
{
 "file": "cic/texts/mirbt_quellen-zur-geschichte-des-papsttums-3e-aufl-deu-lat_1911.txt",
 "lines": "2777",
 "scan": "minatus ;  15",
 "reads": "minatus ;",
 "kind": "margin line number run into the line"
},
{
 "file": "cic/texts/mirbt_quellen-zur-geschichte-des-papsttums-3e-aufl-deu-lat_1911.txt",
 "lines": "2814",
 "scan": "Das  altrömische  Taufbekenntnis.",
 "drop": true,
 "kind": "running head and page number",
 "lines_held": [
  "6  Das  altrömische  Taufbekenntnis.  —  Das  Jüngere  „apostolische\"  Symbol."
 ]
},
{
 "file": "cic/texts/mirbt_quellen-zur-geschichte-des-papsttums-3e-aufl-deu-lat_1911.txt",
 "lines": "2816",
 "scan": "argiiantur",
 "reads": "arguantur",
 "kind": "OCR misread"
},
{
 "file": "cic/texts/tertullian_quae-supersunt-t1-apologetica-lat_oehler1853.txt",
 "lines": "11728",
 "scan": "0  sententiam",
 "reads": "O  sententiam",
 "kind": "OCR misread"
}
```

## 6. Not found, and anything clearly wrong left in

`Card_Edits.md` lists nothing as not found. Its reason for leaving out the three Latin texts (the margin "15", the page head and "argiiantur", the "0") is right as a diagnosis, but the remedy is the readings above, not the omission. Nothing else clearly wrong was found.

## FIX

**FIX 1.** `briefReferences[1]`
- Old: `McGiffert's note: a man of letters and a friend of Trajan, governor of Bithynia from 110 or 111. Mirbt dates the two letters 111 to 113; the story says around the year 112.`
- New: `McGiffert's note: a man of letters, governor of Bithynia from 110 or 111. Mirbt dates the two letters 111 to 113; the story says around the year 112.`

**FIX 2.** `quotationOriginals[0]` (Those who confessed ...): add after `"lines": "19471-19476"`
- Old: (no `original`, `originalFile`, `originalLines`)
- New:
```json
"original": "Confitentes iterum ac tertio interrogavi, supplicium minatus; perseverantes duci iussi. Neque enim dubitabam, qualecumque esset quod faterentur, pertinaciam certe et inflexibilem obstinationem debere puniri.",
"originalFile": "cic/texts/mirbt_quellen-zur-geschichte-des-papsttums-3e-aufl-deu-lat_1911.txt",
"originalLines": "2777-2779"
```
Needs the ML 2777 reading.

**FIX 3.** `quotationOriginals[1]` (They are not to be hunted out ...): add after `"lines": "19526-19527"`
- Old: (no `original`, `originalFile`, `originalLines`)
- New:
```json
"original": "Conquirendi non sunt: si deferantur et arguantur, puniendi sunt",
"originalFile": "cic/texts/mirbt_quellen-zur-geschichte-des-papsttums-3e-aufl-deu-lat_1911.txt",
"originalLines": "2811-2816"
```
Needs the ML 2814 and 2816 readings.

**FIX 4.** `quotationOriginals[3]` (What a ruling, confused by necessity!): add after `"lines": "1583-1585"`
- Old: (no `original`, `originalFile`, `originalLines`)
- New:
```json
"original": "O sententiam necessitate confusam!",
"originalFile": "cic/texts/tertullian_quae-supersunt-t1-apologetica-lat_oehler1853.txt",
"originalLines": "11728"
```
Needs the TL 11728 reading.

FIX 2–4 add new Latin beside an unchanged English and modern wording, so the spans stay "awaiting second reading" as `Card_Edits.md` lists them.
