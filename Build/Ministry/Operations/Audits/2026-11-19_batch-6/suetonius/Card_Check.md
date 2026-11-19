# Card check: Suetonius

Card checker, batch 6, 2026-11-19, per `Card_Check_Prompt.md`. Checked: `suetonius.card.json` against `Card.existing.json` (the same as the census `card`), `Card_Edits.md`, the brief, the outline and the held files. Short names as in `Card_Edits.md` (ROL, THF, NT-E, TERT-L, TERT-E, LAC-E).

**Verdict: FIX** (three changes, below).

## 1. Each edit is justified

- **sources.about**, three added (Acts 18 in NT-E; Apology 3 in TERT-L and TERT-E): justified. Each is cited by a `quotationOriginals` entry.
- **briefReferences**, nine lines: each checked against its cited lines (ROL 25903–25912, 28696–28704, 205–240, 318–324, 25869–25875; NT-E 88521–88524; TERT-E 1712–1716; TERT-L 12505–12514). Files named only here (Lactantius, Mirbt, Schanz) need not be in `sources`.
- **quotationOriginals**, six entries: checked below.
- Clearly wrong: none claimed, and I found none.

## 2. Nothing else moved

Diffed field by field. Only `sources` (three additions after the existing entry), `briefReferences` and `quotationOriginals` differ. Every other field is word for word.

## 3. References

Remaining, after the fix below: (1) Claudius 25.4 between Ilium and the German envoys; (2) Nero 16.2, 19.3, 38; (3) Rolfe's introduction: published 120, Pliny, Hadrian; (4) Rolfe's note on Chrestus; (5) Thomson and Forester's preface and notes; (6) Acts 18:1–2; (7) Tertullian, Apology 3, with Oehler's note; (8) Lactantius on the change of a letter; (9) Mirbt and Schanz printing both lines. No quotation marks.

One part names something the brief does not tell: Nero 19.3's "some deserving of praise" (the brief tells only "beyond criticism"). FIX 1.

## 4. Census rules

Keys allowed; no `briefLength`. Six quoted spans, six entries, each `modern` the brief's span exactly. Every `printed`, `original` and `englishPrinted` stands at its file and lines, and every cited file is in `sources`. No audit, review or ruling named. American spelling outside printed wording. `secondReading` absent on all six: correct, as all are new.

## 5. Originals

The outline renders Quote 3, Tertullian, from Oehler's Latin (Outline, Quotes 3). The card leaves the Latin out because the scan is damaged. It fails only on scan faults, so FIX 3 adds it with three readings. Two corrections to the line numbers on the way: the sentence stands at TERT-L **12454–12456**, not 12453–12455 as `Card_Edits.md` and the outline give it (12453 is "ledicum aut inpudicum? ...", and "penes vos), de suavitate ... conpositum est" is on 12456).

The Nero English (entry 3) is cut to "the Christians, ..." because of a scan fault at ROL 28523. With a reading, Rolfe's whole sentence stands. FIX 2.

Each reading was applied in the validator's way and the wording then checked with its folding: both stand.

Scan faults:
- ROL line 28523: scan `inflicted a`; reads `inflicted on`.
- TERT-L line 12454: scan `*Chrestia  •` (the line-end hyphen read as a bullet); reads `*Chrestia-`.
- TERT-L line 12455: scan `Dus*`; reads `nus`.
- TERT-L line 12456: scan `"pcnes`; reads `"penes`.

```json
{
 "file": "cic/texts/suetonius_lives-of-the-caesars-loeb_rolfe1914.txt",
 "lines": "28523",
 "scan": "inflicted a",
 "reads": "inflicted on",
 "kind": "OCR misread"
},
{
 "file": "cic/texts/tertullian_quae-supersunt-t1-apologetica-lat_oehler1853.txt",
 "lines": "12454",
 "scan": "*Chrestia  •",
 "reads": "*Chrestia-",
 "kind": "OCR misread of the line-end hyphen"
},
{
 "file": "cic/texts/tertullian_quae-supersunt-t1-apologetica-lat_oehler1853.txt",
 "lines": "12455",
 "scan": "Dus*",
 "reads": "nus",
 "kind": "OCR misread"
},
{
 "file": "cic/texts/tertullian_quae-supersunt-t1-apologetica-lat_oehler1853.txt",
 "lines": "12456",
 "scan": "\"pcnes",
 "reads": "\"penes",
 "kind": "OCR misread"
}
```

## 6. Not found, and anything clearly wrong left in

`Card_Edits.md` lists nothing as not found. Its reason for the cut Nero English and the missing Tertullian Latin (scan faults not yet listed) is right as a diagnosis; the remedy is the readings above. Nothing else clearly wrong was found.

## FIX

**FIX 1.** `briefReferences[1]`
- Old: `Lives of the Caesars, Nero 16.2, tr. Rolfe: punishment of the Christians, set between the limit on cooked food in the taverns and the end of the chariot drivers' diversions. Nero 19.3: these acts are some beyond criticism, some deserving of praise. Nero 38: Nero set fire to the city.`
- New: `Lives of the Caesars, Nero 16.2, tr. Rolfe: punishment of the Christians, set between the limit on cooked food in the taverns and the end of the chariot drivers' diversions. Nero 19.3: these acts are some beyond criticism. Nero 38: Nero set fire to the city.`

**FIX 2.** `quotationOriginals[2]` (Punishments were inflicted on the Christians ...)
- `englishPrinted`, old: `the Christians, a class of men given to a new and mischievous superstition.`
- New: `Punishment was inflicted on the Christians, a class of men given to a new and mischievous superstition.`
- `englishLines`, old: `28524-28525`; new: `28523-28525`.
Needs the ROL 28523 reading.

**FIX 3.** `quotationOriginals[5]` (And even when you wrongly say 'Chrestianus' ...): add after `"lines": "1713-1716"`
- Old: (no `original`, `originalFile`, `originalLines`)
- New:
```json
"original": "Sed et cum perperam Chrestianus pronuntiatur a vobis (nam nec nominis certa est notitia penes vos), de suavitate vel benignitate conpositum est.",
"originalFile": "cic/texts/tertullian_quae-supersunt-t1-apologetica-lat_oehler1853.txt",
"originalLines": "12454-12456"
```
Needs the three TERT-L readings. The entry's `uncertain` stays as it is.

FIX 2 and 3 change no modern wording, so the spans stay "awaiting second reading" as `Card_Edits.md` lists them.
