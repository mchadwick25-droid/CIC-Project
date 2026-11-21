# Card check: Eusebius of Caesarea

Card checker, batch 7 (2026-11-20), under `Card_Check_Prompt.md`. I wrote none of this card. Read: `eusebius-of-caesarea.brief.txt`, `eusebius-of-caesarea.card.json`, `Card_Edits.md`, `Card.existing.json` (identical to the census `card` for `eusebius-of-caesarea`), `Outline.md`, and each cited line in its file. Originals are ruled under `Build/Ministry/Operations/Audits/2026-11-19_batch-6/Batch_Originals_Ruling.md`. Greek was checked by hand, letter by letter, against the file's code points.

**Verdict: FIX** (eleven changes below).

## 1. Each edit is justified

- **`uncertain[0]`, the correction.** Justified. McGiffert (EUS 1540-1541) gives "accused of sacrificing" to Athanasius, "Contra Arian. VIII. 1". That passage is §8 of the Defence Against the Arians, inside the encyclical of the council of Egypt, §§3-19 (ATH 21991-21996; Robertson's table, ATH 21662-21663). The words stand at ATH 22308-22309: "accused by our confessors of sacrificing to idols". The old quote was McGiffert's own paraphrase in quotation marks and named the wrong speaker. The new wording is verbatim and names the writers.
- **`legacy.traces[2]` to `[5]`.** Each holds at its lines: EUS 6965-6969; EUS 31104-31106, 9212-9214, 19446-19452, 19555-19556; SOC 1858-1868 and GRK 26043-26056; EUS 44268-44272 and EUS-ed 1569-1572. Trace 5 is sent to the card by Review.md section 1.
- **`uncertain[3]` to `[10]`.** Each holds at its lines (EUS 6937-6952; EUS 43460-43480; EUS 2158-2162, SOC 2971-2978, ATH 26780-26786; SOC 4708-4711, 4752-4760; EPI 44478-44479, EUS-ed 2556-2558, HEF2 1790; GRK 28009-28017, HEF2 1826-1834; EUS 60653-60663, SOC 1862-1866, EUS 67217-67226; ATH 57219-57221, SOC 6916-6921, Philostorgius 88-89, HEF2 1104-1108, 1124-1129). One clause in `uncertain[9]` is not supported (FIX 2).
- **`sources`.** Each added file is cited by a statement on the card.
- **`briefReferences`, fourteen entries.** Each draws on a passage the brief uses. Some parts name what the brief does not tell (FIX 3 to 11).
- **`quotationOriginals`, seven entries.** Each `modern` stands word for word in the brief. Each `printed` stands verbatim at its file and lines. Every cited file is in `sources`.

## 2. Nothing else moved

A field-by-field diff against `Card.existing.json` shows only the listed changes: `uncertain[0]` and the additions at the ends of `legacy.traces`, `uncertain`, `sources.ownWords` and `sources.about`, plus the new `briefReferences` and `quotationOriginals`. Every other field is word for word and in order.

## 3. Originals

- **[0] HE I.1.4.** English alone. HE I in Greek is not held. Correct.
- **[1] HE VIII.2.1: LEAVE OUT, as the card does.** Schwartz's Greek (GRK 13615-13620) has faults with no confirming print: "xcÜ'", "προσευχτηρίων", "οἴχους", "xci", "αὐὖὐ-τοῖς", "χἀχεῖσε χρυπταζομένους". Rufinus's Latin is a translation, and it cannot confirm Greek letters. The outline's Greek (Outline 66) is a reconstruction.
- **[2], [3] Epiphanius 68.8: LEAVE OUT, as the card does.** The Greek (EPI 44590-44604) has "καϑέξζῃ", "μον", "iv", "ovre", with no other held print. Petavius's Latin is a translation. McGiffert's English stands alone.
- **[4] "of one being": KEEP the original, with one code-point fix (FIX 1).** McGiffert prints ὁμοούσιος cleanly at EUS 2091. The card's form has υ with tonos (U+03CD), but the file has υ with oxia (U+1F7B). They are the same letter and accent, but the card should copy the page's code points.
- **[5] "not without inquiry": KEEP.** "οὐκ ἀνεξετάστως" is clean at SOCG 7520 and matches the file code point for code point. The apparatus (SOCG 7536-7541, two columns interleaved) reads that the clause up to ἀνεξετάστως "deest" in the text of the Geneva edition and in Stephanus. So the note's "two older printings leave the clause out" is right. The outline's "damaged OCR" (Outline 69) refers to the line, not this span.
- **[6] "accused": English alone, correct.** The Migne Greek reads "χατηγορεῖτο" (ATHG 61820), with χ for κ and no confirming print.

**FIX 1.** `quotationOriginals[4].original`. Old: `ὁμοούσιος` (U+1F41 U+03BC U+03BF U+03BF **U+03CD** U+03C3 U+03B9 U+03BF U+03C2). New: `ὁμοούσιος` copied from EUS 2091 (U+1F41 U+03BC U+03BF U+03BF **U+1F7B** U+03C3 U+03B9 U+03BF U+03C2).

## 4. Clearly wrong, new on the card

**FIX 2.** `uncertain[9]`. Rufinus says Maximus was "effosso oculo et poplite succiso" (GRK 28010-28011): his eye was put out and the back of his knee was cut, so he was hamstrung. He did not lose a knee. Hefele (HEF2 1827-1830) mentions only the eye.
- Old: `who had lost an eye and a knee`
- New: `who had lost an eye and been hamstrung`

## 5. References

These parts name things the brief does not tell, so they come out. A name that identifies something the brief does tell (Acacius, Euphration, Tertullian, Trajan) stays.

**FIX 3.** `briefReferences[0]`. The brief does not tell the earlier writers' fragments.
- Old: `his plan, the first to try the path, the earlier writers' fragments, the passages he gathered.`
- New: `his plan, the first to try the path, the passages he gathered.`

**FIX 4.** `briefReferences[3]`. The brief does not call him the most illustrious martyr. It tells the prison and the death (EUS 46692-46699).
- Old: `Martyrs of Palestine 7 and 11: Pamphilus, his dearest friend, the most illustrious of the martyrs of the time.`
- New: `Martyrs of Palestine 7 and 11: Pamphilus, his dearest friend, cast into prison, and his martyrdom.`

**FIX 5.** `briefReferences[4]`. The brief gives no years for his election or for the end of the History.
- Old: `bishop soon after the persecution, between about 311 and 318; the History finished about 324, most of it after the persecution;`
- New: `bishop soon after the persecution; most of the History written after the persecution;`

**FIX 6.** `briefReferences[5]`. The brief does not tell the vision, or where he saw Constantine. I.28 stays as the source of "knew him as emperor".
- Old: `Constantine seen in Palestine at the senior emperor's right hand; the vision told under oath;`
- New: `Constantine seen as a young man; what the emperor told him himself;`

**FIX 7.** `briefReferences[6]`. The brief does not say the creed was read before the emperor.
- Old: `his church's creed read before the emperor, the added word,`
- New: `his church's creed read, the added word,`

**FIX 8.** `briefReferences[7]`. The brief does not tell the creed sent home, or the excuse to his church.
- Old: `Socrates I.8: he held aloof for a short time, then signed and sent his people the creed. Athanasius, Defence of the Nicene Definition 3: he had denied the day before, then signed and excused himself to his church.`
- New: `Socrates I.8: he held aloof for a short time, then signed. Athanasius, Defence of the Nicene Definition 3: he had denied the day before, then signed.`

**FIX 9.** `briefReferences[9]`. The brief does not say who accused him.
- Old: `the charge that Eusebius was accused by the confessors of sacrificing to idols.`
- New: `the charge that Eusebius was accused of sacrificing to idols.`

**FIX 10.** `briefReferences[10]`. The brief names neither Paphnutius nor Maximus, and does not say Rufinus added books.
- Old: `Rufinus, Church History X.18: Paphnutius and Maximus of Jerusalem at Tyre, with no word of Eusebius. Rufinus, prologue: the Church History put into Latin, and Books X and XI added.`
- New: `Rufinus, Church History X.18: a like scene at Tyre, with no word of Eusebius. Rufinus, prologue: the Church History put into Latin.`

**FIX 11.** `briefReferences[12]`. The brief does not tell Trajan's reply.
- Old: `Pliny the Younger's letter to Trajan with Trajan's reply, taken from Tertullian.`
- New: `Pliny the Younger's letter to Trajan, taken from Tertullian.`

**References that remain:** [1], [2], [8], [11] and [13] as they stand, and [0], [3] to [7], [9], [10] and [12] as fixed.

## 6. Census rules

The card uses only allowed keys and has no `briefLength`. It has seven entries for the brief's seven quoted spans, and none extra. No `briefReferences` entry has quotation marks. No audit, review or ruling is named. Spelling is American. "Defence" stands only in NPNF's printed titles, which the census already uses. No entry has a `secondReading`, since all seven spans are new.

## 7. Not found, and anything else left in

- The writer listed nothing as not found. I agree that `knownFor`'s "first history of the church" rests on his own claim with McGiffert's endorsement (EUS 6934-6952), and `uncertain[3]` now credits it.
- The Hefele vol. 1 point (Arius naming Eusebius) is optional, and leaving it off is right.
- Nothing else on the card is clearly wrong.
