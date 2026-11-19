# Card check: Josephus

Card checker, batch 6, 2026-11-19, per `Card_Check_Prompt.md`. Checked: `josephus.card.json` against `Card.existing.json` (the same as the census `card`), `Card_Edits.md`, the brief, the outline, the sheet and the held files. Short names as in `Card_Edits.md` (JW, OMG).

**Verdict: FIX** (one change, below), and five scan readings to list.

## 1. Each edit is justified

- **uncertain**, one item added at the end: Chabot's note stands at `michael-the-syrian_chronique-tome1-livres-i-vii-fra_chabot1899.txt` 11208–11209; the header gives Chabot and 1899. "Théodore" for the file's "Th." is supported: held files name him in full (Delehaye 1921; Bréhier, *Revue des études grecques* 16 and 17). "Nothing held after 1899" matches sheet section 6 and Mark's ruling.
- **sources.about**, four added (Origen's Greek, *Against Celsus*, Jerome's Latin, Chabot): justified. OMG is cited by Quote 7; the other three by `briefReferences` or the new `uncertain` item.
- **briefReferences**, nine lines: checked below.
- **quotationOriginals**, eight entries: checked below.
- Clearly wrong: none claimed, and I found none.

## 2. Nothing else moved

Diffed field by field. Only `uncertain` (one item after the existing six), `sources` (four after the existing four), `briefReferences` and `quotationOriginals` differ. Every other field is word for word.

## 3. References

Remaining, after the fix below: (1) War 3: Jotapata, the cave, the promise, the prayer, the lots, the prediction; (2) War 4 and 5: freed in 69, the call to surrender in 70; (3) Life: the Jews' wish to punish him, the Romans' charge, the emperors' favor, the closing words; (4) Antiquities 18 and 20: about 93, John, the passage on Jesus, James; (5) Suetonius, Vespasian 5; (6) Origen, *Against Celsus* 1.47 and *Commentary on Matthew* 10.17; (7) Eusebius 1.9, 1.11 and 3.5; (8) Jerome, *Illustrious Men* 13; (9) McGiffert's notes to 1.11 and 2.23. Every quotation mark stands around words verbatim in the brief.

One part names something the brief does not tell: "both sides' charge of "treachery"". The brief tells that the Jews wanted him punished and that the Romans blamed his treachery; it does not say the Jews charged treachery (nor does Life, JW 5338–5342). FIX 1.

"Finished in the thirteenth year of Domitian" stays: it is the source's own dating of the brief's "about 93".

## 4. Census rules

Keys allowed; no `briefLength`. Eight quoted spans in the brief, eight entries, each `modern` the brief's span exactly. Every cited file is in `sources`. No audit, review or ruling named. American spelling outside printed wording. `secondReading` absent on all eight: correct, as all are new.

Each `printed` was re-read at its lines. Six stand as they are. Two stand only past scan faults:

- **Quote 4** (JW 81405–81409). Line 81406 reads "call hima / man". The page reads "call him a man". Without a reading the census check fails on this entry.
- **Quote 7** (OMG 3731–3733). The card gives the sheet's reading (I2) of the Greek. The scan differs in four places, each a scan fault: a footnote marker set inside the span, a wrong accent and a semicolon for a comma, a wrong accent on Ἰησοῦν, ἣ for ἧ, and χ for κ in Ἰακώβῳ. The census check folds Greek letters away, so it would pass this entry anyway; the readings are listed so the wording is recorded as it truly stands. The card's θ for the edition's ϑ is the same letter under the check's folding, and is accepted. The accent and comma in "ἐστιν," are the sheet's reading; they cannot be confirmed without the page image.

Scan faults, for `tools/quote_scan_readings.json`:
- JW line 81406: scan `hima`; reads `him a`.
- OMG line 3731: scan `τὸ 4) ϑαυμαστόν ἔστιν;`; reads `τὸ ϑαυμαστόν ἐστιν,`.
- OMG lines 3731–3732: scan `Ἴη- \nσοῦν`; reads `Ἰησοῦν`.
- OMG lines 3732–3733: scan `ἣτ- \nτον`; reads `ἧττον`.
- OMG line 3733: scan `᾿Ιαχώβῳ`; reads `Ἰακώβῳ`.

```json
{
 "file": "cic/texts/josephus_works-antiquities-wars-life_whiston1859.txt",
 "lines": "81406",
 "scan": "hima",
 "reads": "him a",
 "kind": "OCR misread (two words run together)"
},
{
 "file": "cic/texts/origen_commentarii-in-evangelium-matthaei-tomus3-grc-lat_lommatzsch1834.txt",
 "lines": "3731",
 "scan": "τὸ 4) ϑαυμαστόν ἔστιν;",
 "reads": "τὸ ϑαυμαστόν ἐστιν,",
 "kind": "footnote marker set inside the span, with an OCR misread accent and a comma read as a semicolon"
},
{
 "file": "cic/texts/origen_commentarii-in-evangelium-matthaei-tomus3-grc-lat_lommatzsch1834.txt",
 "lines": "3731-3732",
 "scan": "Ἴη- \nσοῦν",
 "reads": "Ἰησοῦν",
 "kind": "OCR misread accent, with the line-end hyphen"
},
{
 "file": "cic/texts/origen_commentarii-in-evangelium-matthaei-tomus3-grc-lat_lommatzsch1834.txt",
 "lines": "3732-3733",
 "scan": "ἣτ- \nτον",
 "reads": "ἧττον",
 "kind": "OCR misread accent, with the line-end hyphen"
},
{
 "file": "cic/texts/origen_commentarii-in-evangelium-matthaei-tomus3-grc-lat_lommatzsch1834.txt",
 "lines": "3733",
 "scan": "᾿Ιαχώβῳ",
 "reads": "Ἰακώβῳ",
 "kind": "OCR misread (χ for κ, breathing set apart)"
}
```

## 5. Originals

Quote 7 is rendered from Origen's Greek (Outline, Quotes 3), and the card carries the Greek as `printed`, with the Ante-Nicene English beside it. The other quotes are rendered from Whiston's English; the Greek of Josephus is not held. Jerome's Latin and Chabot's French are paraphrased, not quoted. Nothing is missing.

## 6. Not found, and anything clearly wrong left in

`Card_Edits.md` lists nothing as not found. Its diagnosis of the Quote 4 scan fault is right; the remedy is the reading above. The existing items it re-read hold, and none contradicts the brief ("more than a century later" and the brief's "a century and a half later" agree). Nothing else clearly wrong was found.

## FIX

**FIX 1.** `briefReferences[2]`
- Old: `Life, in Whiston's English: both sides' charge of "treachery", the emperors' favor at Rome, and his closing words, "let others judge of my character."`
- New: `Life, in Whiston's English: the Jews' wish to punish him and the Romans' charge of "treachery", the emperors' favor at Rome, and his closing words, "let others judge of my character."`

FIX 1 changes no modern wording, so the eight spans stay "awaiting second reading" as `Card_Edits.md` lists them.
