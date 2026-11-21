# Card check: Origen

Batch 7, 2026-11-20. Independent checker; I wrote neither the brief nor the card. This card was approved before the kit. Its research is `Build/Ministry/Operations/Audits/2026-11-16_eight-standard-v1/drafts/origen.refs.md`, and the brief changed only at B1 and B2 in `Revision.md`. Files are under `cic/texts/` unless noted.

**Verdict: FIX** (7 changes, below).

## 1. Each edit justified

- **legacy.remembered[3], Hefele (npnf214 23864-23905): justified.** Hefele names Halloix, Garnier, Basnage, Walch "and others" (23864). He keeps the name chiefly because the Roman copy of the acts has it (23888-23891).
- **uncertain[0], Rufinus's admission (npnf203 47040-47046): the source holds, but the cut misleads (FIX 1).**
  - The quotation stops at "rule of faith". The page goes on: "which the writer again and again lays down."
  - It also drops the scope: "Wherever ... we find erroneous definitions of the Trinity".
  - With both cut, "them" has nothing to refer to, and Rufinus seems to admit changing the book at large, to fit the church's rule. In fact he says he changed passages on the Trinity, to fit the rule Origen himself lays down.
- **briefReferences[12], Decius (npnf201 37484-37495): justified.** The source has "bonds and bodily tortures" (37489) and "for many days with his feet stretched four spaces in the stocks" (37491). It matches the brief's new paragraph 5.

## 2. Nothing else moved

I diffed the card against `Card.existing.json`. Apart from the three listed edits, every field is word for word and in order. The old `briefReferences[12]` to `[16]` move down one place because the new entry goes in before them.

## 3. References

Each entry was checked against the brief. Six name, or quote, what the brief does not tell (FIX 2 to 7):

- **[0], [1], [10], [15]: quotation marks on words that are not in the brief.**
  - "tenth year"
  - McGiffert's "Take heed ..."
  - "the labour-loving Origen" (also British spelling outside the printed field)
  - "the Defense which we have composed in his behalf"
- **[13]: the Rufinus caveat.** The brief does not mention Rufinus.
- **[14]: "On the Resurrection".** The brief says only that Methodius "wrote against him".

After the fixes, all 18 entries remain, in order: Severus; the letter; the father's death; the eighteenth year; Caesarea; Jerome on Hebrew and Tyre; the Hexapla; the Job preface; the three senses; the Philocalia; Athanasius; Gregory and Athenodorus; Decius; souls before bodies; Methodius; Pamphilus and Eusebius; 553; and the census tradition.

## 4. Census rules

- Keys are allowed, and there is no `briefLength`.
- There are two entries for the brief's two quoted spans, and no extra.
- Both `printed` wordings stand at their lines: npnf201 32562, and npnf204 28650-28652, with the note between "labour-loving" and "Origen".
- Both files are in `sources`.
- Both `secondReading` values ("same") are copied from `quotation-originals.json`.
- No audit is named. "Defence of the Nicene Definition" is Robertson's printed title (npnf204 26384), so it may stand. The `briefReferences` quotation marks and the British spelling are covered by FIX 2, 3 and 4.

## 5. Originals, and the ruling on each printed form

The card gives no `original`, and none is needed. There is no outline, and the refs file, (d), says that both spans are renderings of the vendored English (`renderings/eight`). So check 5 does not apply.

For the coordinator, I checked the held Greek by hand:

- **Eusebius VI.2.6** (Schwartz 970-971): "ἔπεχε μὴ δι ἡμᾶς ἄλλο τι φρονήσῃς-". The δι has lost its elision mark, and the "-" is the closing quotation mark.
- **Athanasius**: the Greek word, φιλοπόνου, is printed in the NPNF note itself (npnf204 28650).

If either Greek were ever added, the Eusebius line would need a held print to confirm δι᾽. None is held, so it would be left out.

## 6. "Not found" and anything left wrong

The card claims none not found. `briefReferences[13]`'s "the only form in which we read it" also overstates the case: the Philocalia, which the card cites, keeps parts of On First Principles in Greek. FIX 5 removes that clause with the rest of the Rufinus part.

## Fixes

**FIX 1.** `uncertain[0]`
- Old: `We read On First Principles mostly in Rufinus of Aquileia's Latin, and Jerome said Rufinus changed it. Rufinus says in his preface: "we have either left them out as passages which had been falsified or inserted, or else have changed the expression in accordance with the rule of faith."`
- New: `We read On First Principles mostly in Rufinus of Aquileia's Latin, and Jerome said Rufinus changed it. Rufinus says in his preface that where he found erroneous definitions of the Trinity, "we have either left them out as passages which had been falsified or inserted, or else have changed the expression in accordance with the rule of faith which the writer again and again lays down."`

**FIX 2.** `briefReferences[0]`
- Old: `Eusebius, Church History VI.1-2, tr. A. C. McGiffert: Severus's persecution, believers of Egypt brought to Alexandria, many dying, Origen's father among those arrested. The year 202 is the edition's reckoning from Eusebius's "tenth year" of Severus.`
- New: `Eusebius, Church History VI.1-2, tr. A. C. McGiffert: Severus's persecution, believers of Egypt brought to Alexandria, many dying, Origen's father among those arrested. The year 202 is the edition's reckoning from Eusebius's tenth year of Severus.`

**FIX 3.** `briefReferences[1]`
- Old: `Eusebius, Church History VI.2.3-6, tr. McGiffert: Origen's longing for martyrdom, his mother hiding his clothes, the letter to his father: "Take heed not to change your mind on our account."`
- New: `Eusebius, Church History VI.2.3-6, tr. McGiffert: Origen's longing for martyrdom, his mother hiding his clothes, the letter to his father not to change his mind on their account.`

**FIX 4.** `briefReferences[10]`
- Old: `Athanasius, On the Decrees of the Council of Nicaea 27, ed. Archibald Robertson: the Son always with the Father; Athanasius, defending Nicaea, calls on "the labour-loving Origen" as a witness.`
- New: `Athanasius, On the Decrees of the Council of Nicaea 27, ed. Archibald Robertson: the Son always with the Father; Athanasius, defending Nicaea, calls on Origen as a witness.`

**FIX 5.** `briefReferences[13]`
- Old: `Origen, On First Principles, tr. Crombie (Rufinus's Latin): souls before bodies. Rufinus's Latin is the only form in which we read it, and Rufinus says he changed passages.`
- New: `Origen, On First Principles, tr. Crombie (Rufinus's Latin): souls before bodies.`

**FIX 6.** `briefReferences[14]`
- Old: `Jerome, Lives of Illustrious Men 83, tr. Richardson: Methodius wrote On the Resurrection against Origen.`
- New: `Jerome, Lives of Illustrious Men 83, tr. Richardson: Methodius wrote against Origen.`

**FIX 7.** `briefReferences[15]`
- Old: `Jerome, Lives of Illustrious Men 75, tr. Richardson: Pamphilus of Caesarea's defense of Origen. Eusebius, Church History VI.23, tr. McGiffert: "the Defense which we have composed in his behalf".`
- New: `Jerome, Lives of Illustrious Men 75, tr. Richardson: Pamphilus of Caesarea's defense of Origen. Eusebius, Church History VI.23, tr. McGiffert: the Defense he composed for Origen, with Pamphilus in McGiffert's note.`
