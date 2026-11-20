# Card check: Councils of Carthage and Rome on the lapsed (251)

Card checker, batch 7, 2026-11-20, per `Card_Check_Prompt.md`. A council: the starting record is the census entry's `council` object, `Card.existing.json` (identical to the census). Checked `councils-of-rome-and-carthage-251.card.json` against it, `Card_Edits.md`, the brief, the outline and the held files. Short names as in `Card_Edits.md` (ANF, EP, EUS, SOC, NIC, HEF), plus EUSG = Schwartz's Eusebius VI-X, SOCG1 and SOCG2 = Hussey's Socrates, `socrates_historia-ecclesiastica-tomus1-grc-lat_hussey1853.txt` and `-tomus2-`.

**Verdict: FIX** (three changes, below), and four scan readings to list.

## 1. Each edit is justified

- `issue[4]` to `[7]`: ANF 30195-30206 ("thousands of certificates were daily given"), ANF 30382-30393 (the confessors' letter); ANF 33693-33708 with EP 7882-7884; ANF 32420-32430, 33484-33503; ANF 32589-32600. All hold.
- `decided[4]` to `[6]`: ANF 33514-33519, 33780-33785 ("there is no confession in the place of the departed"), 33962-33970. All hold.
- `outcome[2]` to `[4]`: SOC 14099-14101; NIC 3769-3777; HEF 6498-6502 and 6580-6586, ANF 34752-34753 ("that pseudo-bishop, constituted by a few"). All hold.
- `uncertain[5]` to `[11]`: SOC 14066-14071 against ANF 33626-33631 (both credited); HEF 6436 ("reconciled immediately") against ANF 33780-33782 ("in the meantime"); SOC 14088-14090, EUS 38264-38268, 38292-38294; HEF 6309-6360; ANF 33449-33457, 33831-33835; NIC 4503-4509, HEF 6375-6376; EUS 38138-38145, 38838-38883. All hold, and each difference is credited.
- `sources`: three added, each cited by an entry or a reference. Source items carry only the council keys (title, author, language, file).
- Clearly wrong: none claimed, and I found none.

## 2. Nothing else moved

Diffed field by field. Only additions: `issue[4]` to `[7]`, `decided[4]` to `[6]`, `outcome[2]` to `[4]`, `uncertain[5]` to `[11]`, `sources.fromThoseThere[2]` and `[3]`, `sources.writtenLater[4]`, `briefReferences`, `quotationOriginals`. Every existing field is word for word, including `rivers`, `record` and `traditions`.

## 3. References

Remaining after the fix: (1) On the Lapsed 8; (2) Ep. 55.14; (3) Letters 20 and 23; (4) Letter 43; (5) Letter 55, chs. 4 to 6, 17 and 23; (6) Letter 55, ch. 12; (7) Letter 59, ch. 9; (8) Socrates IV.28; (9) Eusebius VI.43; (10) Letter 57; (11) Hefele; (12) canon 8. No quotation marks in any.

One part names something the brief does not tell: [2], the confessors' terms, "to all whose conduct since their fall satisfied him". The brief says only that confessors were handing out written pardons granting peace. FIX 1. What the revision cut from the brief ("After Easter", "Within a year") is named in no reference.

## 4. Census rules

Keys allowed (council list); no `briefLength`. Ten quoted spans in the brief, ten entries, each `modern` the brief's span exactly; no stale entry. Every `printed` and `original` stands at its lines; every cited file is in `sources` (after FIX 3, the new Greek file too). The one quotation in the card's prose ("a large number of bishops,") stands in a cited file. No audit, review or ruling named. American spelling ("offense" is Zenos's printed word; "rumor", "favorable").

## 5. Originals (ruled against `2026-11-19_batch-6/Batch_Originals_Ruling.md`; Greek checked by hand)

- **[0] "persecutio est haec alia" (EP 5953), [1] "cum disciplina pariter et misericordia temperatam" (EP 5968), [2] "temperamentum salubri moderatione librauimus" (EP 7584-7585), [3] "ut nec in totum ... ne plus desperatione deficerent" (EP 7585-7586), [9] "hoc in tempore ... ad aciem damus." (EP 8721-8724): KEEP as they stand.** Clean TEI text.
- **[4] "examinarentur causae et uolontates et necessitates singulorum" (EP 7590-7610): KEEP as it stands.** The footnote and page break between "causae" and "et" are tagged notes, set aside by the check. "uolontates" is the edition's own spelling, not a scan fault: the text is a typed TEI file, not OCR.
- **[5] Socrates IV.28 (SOCG2 4372-4377): KEEP, with four readings; the card leaves it out, so FIX 2.** The outline renders this quote from Hussey's Greek. The page's faults:
  - "35" after "δέχεσθαι" (4372): the margin line number, a stray mark.
  - ", - ^ ER A5 , L4" (4375): a scanned row of accents set between two lines, no part of the text.
  - "kai" (4376) for καὶ, and "avy-" / "εχωρεῖν" (4376-4377) for συγ-χωρεῖν. These need a held print, and one is held: Socrates gives the same formula in his own Greek of Book I, chapter 10, in the same edition, cleanly, "τοῦ δυνα-μένου καὶ ἐξουσίαν ἔχοντος συγχωρεῖν ἁμαρτήματα" (SOCG1 9909-9910). Zenos's English points to that parallel itself ("Cf. I. 10.", SOC 14085). That confirms both words letter for letter. Valesius's Latin (SOCG2 4402) and Zenos confirm only the sense.
  - The mark after "μυστήρια" (4373) prints as `"`. It may be a note mark or a raised stop, and the page does not settle which, so the wording below leaves it out. The check folds punctuation, so nothing turns on it.
  - The rest is clean: μὴ δέχεσθαι τοὺς ἐπιτεθυκότας εἰς τὰ μυστήρια ἀλλὰ προτρέπειν μὲν αὐτοὺς εἰς μετάνοιαν, τὴν δὲ συγχώρησιν ἐπι-τρέπειν Θεῷ, τῷ δυναμένῳ καὶ ἐξουσίαν ἔχοντι συγχωρεῖν ἁμαρτήματα. The note's three claims about the Greek (the mysteries, the two words for able and power, the plural sins) all rest on clean words.
- **[6] "strangers" (EUS 38294) and [7] "with the medicines of repentance" (EUS 38299): English alone, as the card has it.** Both are McGiffert's wording unchanged, so the outline does not render them from the Greek. In any case [7]'s Greek is faulty ("μετα-νοἷας φαρμάχοις", EUSG 6700-6701). Rufinus's Latin, named in both notes, is clean at EUSG 6774-6776.
- **[8] "to the present day" (SOC 14060-14061): English alone.** Rendered from Zenos.

Each reading was applied in the validator's way and the Greek then checked with its folding: it stands. For `tools/quote_scan_readings.json`:

```json
{
 "file": "cic/texts/socrates_historia-ecclesiastica-tomus2-grc-lat_hussey1853.txt",
 "lines": "4372",
 "scan": "μὴ δέχεσθαι 35",
 "reads": "μὴ δέχεσθαι",
 "kind": "line number run into the line"
},
{
 "file": "cic/texts/socrates_historia-ecclesiastica-tomus2-grc-lat_hussey1853.txt",
 "lines": "4375",
 "scan": ", - ^ ER A5 , L4",
 "drop": true,
 "kind": "scanned accent row set between the lines",
 "lines_held": [", - ^ ER A5 , L4"]
},
{
 "file": "cic/texts/socrates_historia-ecclesiastica-tomus2-grc-lat_hussey1853.txt",
 "lines": "4376",
 "scan": "kai ἐξουσίαν ἔχοντι avy-",
 "reads": "καὶ ἐξουσίαν ἔχοντι συγ-",
 "kind": "OCR misread (Latin letters for Greek); the same formula in Hussey's Book I, chapter 10 prints καὶ ἐξουσίαν ἔχοντος συγχωρεῖν (socrates_historia-ecclesiastica-tomus1-grc-lat_hussey1853.txt, lines 9909-9910)"
},
{
 "file": "cic/texts/socrates_historia-ecclesiastica-tomus2-grc-lat_hussey1853.txt",
 "lines": "4377",
 "scan": "εχωρεῖν ἁμαρτήματα",
 "reads": "χωρεῖν ἁμαρτήματα",
 "kind": "OCR misread; the same formula in Hussey's Book I, chapter 10 prints συγχωρεῖν ἁμαρτήματα (socrates_historia-ecclesiastica-tomus1-grc-lat_hussey1853.txt, line 9910)"
}
```

## 6. Not found, and anything clearly wrong left in

- Existing `issue[3]`, Cornelius "would receive the lapsed after penance", citing Socrates and Eusebius: it holds. Eusebius gives the Rome decree to heal the fallen "with the medicines of repentance" (EUS 38296-38299). Socrates's different report is credited in the new `uncertain[5]`.
- Existing `datesNote`: it holds. HEF gives the months, and no source of the time does.
- Nothing else clearly wrong was found.

## FIX

**FIX 1.** `briefReferences[2]`
- Old: `Cyprian, Letter to the clergy at Rome (Letter 20 in Hartel's Latin): thousands of papers of pardon given each day without examination. Letter of the confessors to Cyprian (Letter 23): peace granted to all whose conduct since their fall satisfied him.`
- New: `Cyprian, Letter to the clergy at Rome (Letter 20 in Hartel's Latin): thousands of papers of pardon given each day without examination. Letter of the confessors to Cyprian (Letter 23): peace granted.`

**FIX 2.** `quotationOriginals[5]`: add the Greek, and replace the note.
- Add: `"original": "μὴ δέχεσθαι τοὺς ἐπιτεθυκότας εἰς τὰ μυστήρια ἀλλὰ προτρέπειν μὲν αὐτοὺς εἰς μετάνοιαν, τὴν δὲ συγχώρησιν ἐπιτρέπειν Θεῷ, τῷ δυναμένῳ καὶ ἐξουσίαν ἔχοντι συγχωρεῖν ἁμαρτήματα."`, `"originalFile": "cic/texts/socrates_historia-ecclesiastica-tomus2-grc-lat_hussey1853.txt"`, `"originalLines": "4372-4377"`.
- `uncertain` old: `The modern wording follows the Greek where it differs from the print: sacred rites for the mysteries (the rite meant is the Lord's Supper), who is able and has the power for the Greek's two words, and sins for the Greek's plural. The Greek is held only in a damaged scan, so it is not printed here.`
- `uncertain` new: `The modern wording follows the Greek where it differs from the print: sacred rites for the mysteries (the rite meant is the Lord's Supper), who is able and has the power for the Greek's two words, and sins for the Greek's plural.`

**FIX 3.** `sources.writtenLater`: append
```json
{
 "title": "Church History, Book IV, chapter 28 (Greek, with Valesius's Latin, ed. Robert Hussey)",
 "author": "Socrates of Constantinople",
 "language": "Greek",
 "file": "cic/texts/socrates_historia-ecclesiastica-tomus2-grc-lat_hussey1853.txt"
}
```
(FIX 2 and FIX 3 go together, with the four readings above. The two Latin-letter faults rest on Socrates's own parallel formula, not on a second print of this sentence. If the coordinator does not accept a parallel in the same edition as confirmation, leave the Greek out and keep the note as it stands.)
