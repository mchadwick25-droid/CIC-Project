# Card check: Novatian

Card checker, batch 7, 2026-11-20, per `Card_Check_Prompt.md`. Checked `novatian.card.json` against `Card.existing.json` (identical to the census `card`), `Card_Edits.md`, the brief, the outline and the held files. Short names as in `Card_Edits.md` (ANF, EP, EUS, SOC, ANF6, NIC, JER, AMB, HARN), plus EUSG = Schwartz's Eusebius VI-X and SOCG = `socrates_historia-ecclesiastica-tomus1-grc-lat_hussey1853.txt`.

**Verdict: FIX** (ten changes, below), and three scan readings to list.

## 1. Each edit is justified

- `legacy.traces[1]` to `[5]`: NIC 3769-3777; SOC 19289-19294; ANF 33992-33998 and 38450-38455; ANF 32586-32597; JER 40886-40897 and HARN 22497-22499 ("bis auf zwei spurlos verschwunden"). All hold.
- `legacy.remembered[2]`: EUS 38926-38928. Holds.
- `uncertain[6]` to `[17]`: re-read at the cited lines. All hold except two, FIX 9 and FIX 10.
- `sources`: Ep. 30 in Latin with `disputed` (allowed key), and nine `about` items, each cited by an entry or a reference.
- Clearly wrong: none claimed. I found two in the new prose (FIX 9, FIX 10) and one in a quote note (FIX 6).

## 2. Nothing else moved

Diffed field by field. Only additions: `legacy.traces[1]` to `[5]`, `legacy.remembered[2]`, `uncertain[6]` to `[17]`, `sources.ownWords[1]`, `sources.about[3]` to `[10]`, `briefReferences`, `quotationOriginals`. Every existing field is word for word.

## 3. References

Remaining after the fixes: (1) Ep. 51.5, Novatian the writer; (2) Ep. 30, the wait, the dying, the doors; (3) Eusebius VI.43, oaths, three bishops, the refusal, McGiffert's notes; (4) the communion-table oath; (5) the sixty bishops and the name Cathari; (6) Dionysius's letter; (7) Cyprian Epp. 51 and 72; (8) Socrates I.10 and I.13; (9) Sozomen I.22; (10) canon 8; (11) Socrates VII.11; (12) Socrates IV.28, Coxe, Wallis, Harnack; (13) Jerome 70 and Harnack; (14) census. No quotation marks in any.

Parts that name something the brief does not tell:
- [1] "since Fabian's death": the brief says only that Rome had no bishop. FIX 1.
- [2] "by the tenth hour". FIX 2.
- [7] "Socrates says no other writer recorded it (SOC 3722-3727)", and "Novatian presbyter": the brief says only "an old man". FIX 3.
- [11] "under Valerian": cut from the brief in revision (v1 had it; the brief now says "a later persecution"). FIX 4.
- [12] Jerome's "sort of epitome of Tertullian's work" and the survival under Tertullian's name: the brief tells neither. FIX 5.

## 4. Census rules

Keys allowed; no `briefLength`. Four quoted spans in the brief, four entries, each `modern` the brief's span exactly. The span cut in revision ("Let them come to the threshold...") has no entry: correct. Every `printed` and `original` stands at its lines; every cited file is in `sources` (after FIX 7, the new Greek file too). Every quotation in the card's prose stands verbatim in a cited file. No audit, review or ruling named. American spelling ("defense"). No `secondReading`: correct, all four are new.

## 5. Originals (ruled against `2026-11-19_batch-6/Batch_Originals_Ruling.md`; Greek checked by hand)

- **[0] "pulsent sane fores, sed non utique confringant." (EP 4222): KEEP as it stands.** Clean TEI text.
- **[1] Dionysius (EUSG 7362-7365): LEAVE OUT, as the card does.** "axzov" and "Exam" (for the words the outline restores as ἄκων and ἑκών) have no confirming print: no other held print has this Greek, and Rufinus's Latin and both English prints confirm the sense, not the letters. The same lines have further faults ("οὐπὲρ", "διαχόψαι", "ἢν", "οὐχ", "ἕνεχεν", "Evexev"). The English stands alone. But the entry's note names the two restored Greek words, supplying from knowledge what the page does not print; and it says "The Greek addresses Novatus", which the held Greek contradicts: Schwartz prints "Νοουατιανῷ" (EUSG 7362, clean), and his apparatus gives it from BD and Jerome, with forms of Novatus in other manuscripts (M "ναουάτω", ER "νανάτω", EUSG 7391-7392). Both forms credited: FIX 6. "ἔδει" in the note is clean on the page and stays.
- **[2] καθαροί (EUS 38270): KEEP as it stands.** McGiffert's own note, clean XML. Nominative plural, "pure": right.
- **[3] the ladder (SOCG 9912-9913): KEEP, with three readings; the card leaves it out, so FIX 7.** The outline renders from the Greek, and the page's Greek is clean apart from three stray marks:
  - "᾿Ακέσιεΐ": the "ΐ" is the footnote mark f. The apparatus prints "f Ἀκέσινε C." (SOCG 9925), the note on this word.
  - "ao" at the end of line 9912: the margin line number 20. The page numbers its lines in fives (the "15" at 9907 is five lines above).
  - "φοὐρανόν": a stray letter. Οὐρανόν carries its own breathing, which the print sets only on a word's first letter, so the φ is no part of the word, and alone it is no word.
  - Every other letter is right: θὲς ὦ ᾿Ακέσιε κλίμακα, καὶ μόνος ἀνάβηθι εἰς τὸν οὐρανόν. Valesius's Latin on the page (SOCG 9934-9935, "Pone scalam, Acesi, et in coelum solus ascende") follows it word by word, a translation that confirms the sense.
  - With the original printed, the note's claim that the scan is "too damaged to print" no longer holds, and its Greek is now the `original`. The file goes into `sources`.
  - The third mark is the one judgment call. If the coordinator rules the φ is not plainly stray, leave the Greek out and take FIX 7's `uncertain` alone; it no longer names the Greek either way.

Each reading was applied in the validator's way and the Greek then checked with its folding: it stands. For `tools/quote_scan_readings.json`:

```json
{
 "file": "cic/texts/socrates_historia-ecclesiastica-tomus1-grc-lat_hussey1853.txt",
 "lines": "9912",
 "scan": "᾿Ακέσιεΐ",
 "reads": "᾿Ακέσιε",
 "kind": "OCR set a footnote mark into the word (note f, line 9925)"
},
{
 "file": "cic/texts/socrates_historia-ecclesiastica-tomus1-grc-lat_hussey1853.txt",
 "lines": "9912",
 "scan": "εἰς τὸν ao",
 "reads": "εἰς τὸν",
 "kind": "line number run into the line"
},
{
 "file": "cic/texts/socrates_historia-ecclesiastica-tomus1-grc-lat_hussey1853.txt",
 "lines": "9913",
 "scan": "φοὐρανόν",
 "reads": "οὐρανόν",
 "kind": "stray letter before a word that carries its own breathing"
}
```

## 6. Not found, and anything clearly wrong left in

`Card_Edits.md` lists nothing not found, and I found nothing wrong in the existing card. Its omission of Hefele's "until the fifth century" is right, since the brief does not need it.

## FIX

**FIX 1.** `briefReferences[1]`
- Old: `Letter of the Roman clergy, Cyprian Epistle 30: no bishop since Fabian's death, the case of the lapsed to wait for a bishop and a council (ANF 31709-31722), the dying who repented to be helped (ANF 31820-31827), and the line about knocking at the doors (EP 4222; ANF 31758-31759).`
- New: `Letter of the Roman clergy, Cyprian Epistle 30: no bishop, the case of the lapsed to wait for a bishop and a council (ANF 31709-31722), the dying who repented to be helped (ANF 31820-31827), and the line about knocking at the doors (EP 4222; ANF 31758-31759).`

**FIX 2.** `briefReferences[2]`
- Old: `the three simple bishops, drunk and sick by the tenth hour (EUS 38518-38533)`
- New: `the three simple bishops, drunk and sick (EUS 38518-38533)`
- (The rest of the entry is unchanged.)

**FIX 3.** `briefReferences[7]`
- Old: `Socrates, Church History I.10: Constantine and Acesius at Nicaea, the creed and the Easter date, the old rule from Decius's day, and the ladder (SOC 3685-3721). Socrates says no other writer recorded it (SOC 3722-3727). Book 1, chapter 13: Auxanon, a very aged Novatian presbyter who went to Nicaea with Acesius (SOC 3855-3857).`
- New: `Socrates, Church History I.10: Constantine and Acesius at Nicaea, the creed and the Easter date, the old rule from Decius's day, and the ladder (SOC 3685-3721). Book 1, chapter 13: Auxanon, a very aged man who went to Nicaea with Acesius (SOC 3855-3857).`

**FIX 4.** `briefReferences[11]`
- Old: `Socrates, Church History IV.28: the rule, and the martyrdom under Valerian (SOC 14069-14090, 14132-14144).`
- New: `Socrates, Church History IV.28: the rule, and the martyrdom (SOC 14069-14090, 14132-14144).`
- (The rest of the entry is unchanged.)

**FIX 5.** `briefReferences[12]`
- Old: `Jerome, Lives of Illustrious Men 70: Novatian's writings, and On the Trinity as a sort of epitome of Tertullian's work (JER 40886-40897). Harnack on the book's date and its survival under Tertullian's name (HARN 22497-22551).`
- New: `Jerome, Lives of Illustrious Men 70: Novatian's writings (JER 40886-40897). Harnack on the book's date (HARN 22497-22551).`

**FIX 6.** `quotationOriginals[1].uncertain`
- Old: `The modern wording follows the Greek, which the one held print gives in a scan too damaged to print here; it garbles the two words for unwilling and willing (ἄκων, ἑκών), whose sense Rufinus's Latin and both English prints confirm. "One ought" follows ἔδει. Salmond's English (Ante-Nicene Fathers, vol. 6) reads "If you were carried on against your will, as you say, you will show that such has been the case by your voluntary retirement", and "it would have been but dutiful to have suffered any kind of ill, so as to avoid rending the Church of God". The Greek addresses Novatus; Salmond's note says Jerome gives Novatianus. Both readings kept.`
- New: `The modern wording follows the Greek, which the one held print gives in a scan too damaged to print here; it garbles the two words for unwilling and willing, whose sense Rufinus's Latin and both English prints confirm. "One ought" follows ἔδει. Salmond's English (Ante-Nicene Fathers, vol. 6) reads "If you were carried on against your will, as you say, you will show that such has been the case by your voluntary retirement", and "it would have been but dutiful to have suffered any kind of ill, so as to avoid rending the Church of God". Both English prints address Novatus. Schwartz's Greek addresses Novatian (Νοουατιανῷ), and his notes give forms of Novatus from other manuscripts; Salmond's note says Jerome gives Novatianus. Both readings kept.`

**FIX 7.** `quotationOriginals[3]`: add the Greek, and replace the note.
- Add: `"original": "θὲς ὦ ᾿Ακέσιε κλίμακα, καὶ μόνος ἀνάβηθι εἰς τὸν οὐρανόν."`, `"originalFile": "cic/texts/socrates_historia-ecclesiastica-tomus1-grc-lat_hussey1853.txt"`, `"originalLines": "9912-9913"`.
- `uncertain` old: `The modern wording follows Socrates's Greek (θὲς ὦ Ἀκέσιε κλίμακα, καὶ μόνος ἀνάβηθι εἰς τὸν οὐρανόν), which the one held print gives in a scan too damaged to print here. Sozomen's retelling in the same English edition reads "take a ladder and ascend alone to heaven". Both readings kept.`
- `uncertain` new: `The modern wording follows Socrates's Greek. Sozomen's retelling in the same English edition reads "take a ladder and ascend alone to heaven". Both readings kept.`

**FIX 8.** `sources.about`: append
```json
{
 "title": "Church History, Book 1, chapter 10 (Greek, with Valesius's Latin, ed. Robert Hussey)",
 "author": "Socrates of Constantinople",
 "date": null,
 "language": "Greek",
 "file": "cic/texts/socrates_historia-ecclesiastica-tomus1-grc-lat_hussey1853.txt"
}
```
(FIX 7 and FIX 8 go together. If the φ ruling is overruled, apply only FIX 7's `uncertain` and drop FIX 8.)

**FIX 9.** `uncertain[13]` (Ambrose makes a fourth witness)
- Old: `What his rule held is told three ways.`
- New: `What his rule held is told four ways.`
- (The rest of the entry is unchanged.)

**FIX 10.** `uncertain[15]` (HARN 22550-22554: "Wann er gestorben ist, weiß man nicht sicher. Sokrates (IV, 28) will wissen..."; Harnack reports the claim, he does not make it)
- Old: `Harnack says the same, and that the martyr acts current in the sixth century were forged.`
- New: `Harnack reports the same, says it is not known for certain when he died, and says the martyr acts current in the sixth century were forged.`
- (The rest of the entry is unchanged.)
