# Card check: Hippolytus of Rome

Checker, batch 6, 2026-11-19, per `Card_Check_Prompt.md`. Card: `hippolytus-of-rome.card.json`, against `Card.existing.json` (identical to the census `card`), `hippolytus-of-rome.brief.txt` and `Card_Edits.md`.

## Verdict: FIX (two changes, and two scan readings)

## 1. Each edit is justified

All edits are additions.
- sources.about, Duchesne's *Liber pontificalis* (1886): holds the list of bishops (LP 66805-66808) and Damasus's verse (LP 109159-109166) that spans 5 to 8 quote. Justified.
- sources.about, Duchesne's *Histoire ancienne* I: DUH 11722-11731 (Damasus identified the split with Novatian's; Hippolytus's books "disparut bientôt de l'horizon romain", the clergy of the next generation writing Latin). Justified.
- sources.about, Harnack's *Chronologie* II: HAR 11870-11874 (Batiffol's doubts on the authorship), 11879-11889 (no split under Callistus), 11912 (rival bishop). Justified. Card_Edits also gives it for "death on the island (HAR 11976-11979)"; Harnack does not say that (see FIX 1).
- briefReferences and quotationOriginals: new, checked below.

## 2. Nothing else moved

A field-by-field diff against the starting card shows only `sources.about` grown from three entries to six (the first three word for word), and `briefReferences` and `quotationOriginals` added. Every other field is word for word.

## 3. References

None names a thing the brief no longer tells. Two name a person the brief leaves unnamed in an event it does tell: Zephyrinus (references 2 and 4; the brief's "the bishop of the day") and Noetus (reference 3; the brief's "A teacher from Smyrna"). I leave both, as naming the source's actor in a told event.

All eight remain, one for each paragraph: the ark (Refutation IX.7); dates, Greek, the charges, the exile of 235, the rival-church views; *Against Noetus* 1 and 7; Callistus's past and McGiffert's "true at its base but greatly overdrawn" judgment; the charges, high-priesthood, rival bishop, Portus, Batiffol, after 222, Greek philosophy; Sardinia, 13 August and the death (FIX 1); the lost books, Mount Athos 1842, 1851 under Origen's name, the doubters; Damasus's verse, the confusion of two splits, census `novatian`. No quotation marks.

## 4. Census rules

Allowed keys only; no `briefLength`. Eight quoted spans in the brief, eight entries, each `modern` the brief's span exactly. Every cited file is in `sources`. No audit, review or ruling named. American spelling ("harbor"); the French title "Église" is a title.

Seven `printed` wordings stand at their lines (HIP 13909-13912, 23442-23450, 13640-13641, 1130; LP 66807, 66808, 109166). The eighth, span 7, does not, for two reasons:

- **A scan fault.** LP 109160 reads `presbyter in scismk SEMPER MANSISSE XOvali.` for "presbyter in scisma semper mansisse Novati". These are only scan faults. Entries for `tools/quote_scan_readings.json`, line 109160 of `cic/texts/liber-pontificalis_texte-introduction-commentaire-t1-lat-fra_duchesne1886.txt`:

```json
[
 {
  "file": "cic/texts/liber-pontificalis_texte-introduction-commentaire-t1-lat-fra_duchesne1886.txt",
  "lines": "109160",
  "scan": "scismk",
  "reads": "scisma",
  "kind": "OCR misread"
 },
 {
  "file": "cic/texts/liber-pontificalis_texte-introduction-commentaire-t1-lat-fra_duchesne1886.txt",
  "lines": "109160",
  "scan": "XOvali",
  "reads": "Novati",
  "kind": "OCR misread"
 }
]
```

- **Not a scan fault: the card's printed wording.** LP 109159 prints `Hippolytus fertur PREMERENT CuM IVSSA Tyranni`. Duchesne prints the stone's surviving letters in capitals, with V for U, and the editors' restorations in lower case (Source_Sheet I3). The card's "iussa" is not what the page prints, and the check does not fold V into U, so span 7 fails even with the two readings. FIX 2 gives the line as printed. With FIX 2 and the two readings it stands in LP 109159-109160 (checked with the validator's fold).

The two other quotation marks in the kept fields ("greatly overdrawn," "over another church," "quite worthless.") stand in EUS. `secondReading` is absent on all eight, as the step order has it (step 7).

## 5. Originals

Spans 1 to 4 render the ANF English; the outline says the Greek of the *Refutation* and *Against Noetus* is not held. Spans 5 to 8 give Duchesne's Latin as `printed`, the original itself. Nothing missing.

## 6. Not-found claims, and anything clearly wrong left in

The card lists none not found; the kept fields' lines in Card_Edits check out where I re-read them (EUS 35449, 35521, 35663; LP 66807-66808). One new statement is wrong:

- Reference 6, "McGiffert and Harnack: he probably died on the island." McGiffert says so (EUS 35698-35700, "highly probable that both he and Pontianus died in the mines there"). Harnack does not: "Hippolyt ist entweder auf Sardinien gestorben oder bald darauf in Rom", either on Sardinia or soon after at Rome (HAR 11978-11979; the scan reads "^Sardinien" and "Kom^"). FIX 1.

Kept, not ruled wrong: quotationOriginals[6]'s work, "as restored by de Rossi", follows the outline; Duchesne cites de Rossi's edition of the verse (LP 109007-109009).

## The fixes, as exact JSON changes

**FIX 1.** `briefReferences[5]`
- Old: "The book of 354, ed. Theodor Mommsen, and the same list in Duchesne's Liber pontificalis: Pontianus and Hippolytus deported to Sardinia, the unhealthy island, in 235; the calendar of martyrs: both kept on 13 August. McGiffert and Harnack: he probably died on the island."
- New: "The book of 354, ed. Theodor Mommsen, and the same list in Duchesne's Liber pontificalis: Pontianus and Hippolytus deported to Sardinia, the unhealthy island, in 235; the calendar of martyrs: both kept on 13 August. McGiffert: he probably died on the island; Harnack: there or soon after at Rome."

**FIX 2.** `quotationOriginals[6].printed` (passes once the two readings above are listed)
- Old: "Hippolytus fertur premerent cum iussa tyranni presbyter in scisma semper mansisse Novati."
- New: "Hippolytus fertur PREMERENT CuM IVSSA Tyranni presbyter in scisma SEMPER MANSISSE Novati."
