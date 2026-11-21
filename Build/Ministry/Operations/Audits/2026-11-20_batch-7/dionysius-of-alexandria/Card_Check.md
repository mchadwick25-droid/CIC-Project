# Card check: Dionysius of Alexandria

Card checker, batch 7 (2026-11-20), under `Card_Check_Prompt.md`. I wrote none of this card. Read: `dionysius-of-alexandria.brief.txt`, `dionysius-of-alexandria.card.json`, `Card_Edits.md`, `Card.existing.json` (identical to the census `card` for `dionysius-of-alexandria`), `Outline.md`, and each cited line in its file. Originals are ruled under `Build/Ministry/Operations/Audits/2026-11-19_batch-6/Batch_Originals_Ruling.md`. Greek was checked by hand.

**Verdict: FIX** (eight changes below).

## 1. Each edit is justified

- **`datesNote`, the clause added.** Justified. McGiffert's note at EUS 41900-41903 says both versions of the Chronicle put the death in the eleventh year of Gallienus, August 263 to August 264. The Chronicle line (CHRON 44268-44269) has Maximus ordained. Where two held sources differ, the card credits both (Mark, 2026-11-19).
- **`legacy.remembered[3]`, `[4]`.** These hold at ATH 29521-29526 and BAS 23716-23719.
- **`uncertain[5]` to `[8]`.** These hold at EUS 37654-37659 and 40397-40400; EUS 41555-41557; EUS 41118-41124; ATH 29268-29269, 29286-29292, 30043-30050; NPNF3 45362-45375, 53615-53618, 53655-53657; BAS 23712-23721. Rufinus's date (397) is the heading at NPNF3 45218.
- **`sources.about`, four entries added.** Each is cited by a statement on the card.
- **`briefReferences`, fifteen entries.** Each draws on a passage the brief uses. Some parts name what the brief does not tell (FIX 3 to 9).
- **`quotationOriginals`, three entries.** Each `modern` stands word for word in the brief. Each `printed` stands verbatim at its file and lines. Every cited file is in `sources`.

## 2. Nothing else moved

A field-by-field diff against `Card.existing.json` shows only the listed changes: the `datesNote` clause, and the additions at the ends of `legacy.remembered`, `uncertain` and `sources.about`, plus the new `briefReferences` and `quotationOriginals`. Every other field is word for word and in order.

## 3. Originals, and which English each entry prints

**No Greek is printed. That is right.** The only held Greek, Schwartz's (EUS-GR), is a damaged scan with no confirming print:
- Quote 1 (EUS-GR 5829-5831) has "iq! ©" for ἐφ᾿ ὃ, "ἀνέχραγον", "μὲ", "xci" and "χεφαλὴν".
- The plague quote (10378-10380) has "εὐ-σέθειαν" and "δοχεῖν".
- The Revelation quote (10978-10981) has "xci" and "οὐχ ἀντερῶ".

The Greek words that the `uncertain` notes rely on are clean in the scan, read by hand: τι χρηστὸν ἐργάσασϑαι, ἀπάγοντάς, ὡς καὶ τοῦ ϑανάτου, τὴν γραφὴν Ἰωάννου (no word for "one"), ἀντερῶ (future), ϑεο-πνεύστου and συναινῶ. So, as with Polycarp in batch 6, the notes may say in English where the rendering follows the Greek.

**The rule for `printed`.** The modern spans are the researcher's renderings of the Greek, which cannot be printed. So `printed` is a held English print of the same span, and it stands alone. Two English prints are held, McGiffert's (EUS) and Salmond's (ANF6). Each entry prints the one the modern span most nearly follows, and its `uncertain` credits the other and says where the modern follows the Greek instead. Printing an English the modern does not follow would suggest that the modern renders that English.

- **[0] The rescue plea: print McGiffert, as the card does.** The modern follows McGiffert in "leave us alone" and "cut off my head themselves"; Salmond has "strike off my head". The note credits Salmond and the Greek, and says the Greek is broken at "why they had come". KEEP.
- **[1] The Revelation judgment: print Salmond (FIX 1).** The modern follows Salmond at four points: "the writing of a John", "the work of some holy", "so easily" and "that this was the apostle". McGiffert has "the work of one John", "a holy and inspired man", "readily" and "that he was". It follows McGiffert only in "agree", where the Greek συναινῶ backs it.
- **[2] The plague letter: print McGiffert, as the card does.** The modern follows McGiffert in "strong faith" and "seemed". Salmond has "steadfast faith" and "appeared to come in nothing beneath". The note is right except on "even" (FIX 2).

**FIX 1.** `quotationOriginals[1]`, these keys:
- `printed`. Old: `Therefore that he was called John, and that this book is the work of one John, I do not deny. And I agree also that it is the work of a holy and inspired man. But I cannot readily admit that he was the apostle, the son of Zebedee, the brother of James,` New: `That this person was called John, therefore, and that this was the writing of a John, I do not deny. And I admit further, that it was also the work of some holy and inspired man. But I could not so easily admit that this was the apostle, the son of Zebedee, the brother of James,`
- `work`. Old: `Eusebius, Church History VII.25.7, quoting Dionysius, On Promises, tr. McGiffert` New: `Dionysius, On Promises, Book 2, in Eusebius, Church History VII.25.7, tr. S. D. F. Salmond`
- `file`. Old: `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` New: `cic/texts/anf06_gregory-thaumaturgus-dionysius-julius-africanus-methodius-arnobius.xml`
- `lines`. Old: `41453-41457` New: `8119-8124`
- `uncertain`. Old: `Salmond's English (Extant Fragments and Letters, lines 8119-8125) reads "the writing of a John, I do not deny" and "the work of some holy and inspired man"; McGiffert has "the work of one John". The modern "the writing of a John" follows Salmond and the Greek, which has no word for "one". "I will not dispute" follows the Greek verb, which is future, "I will not speak against", where both prints say "I do not deny"; "inspired by God" renders the one Greek word the prints give as "inspired".` New: `McGiffert's English (Church History VII.25.7, lines 41453-41457) reads "the work of one John" and "I agree also that it is the work of a holy and inspired man". The modern "the writing of a John" follows Salmond and the Greek, which has no word for "one"; "I agree" follows McGiffert and the Greek. "I will not dispute" follows the Greek verb, which is future, "I will not speak against", where both prints say "I do not deny"; "inspired by God" renders the one Greek word the prints give as "inspired".`

Checked: the new `printed` stands verbatim at ANF6 8119-8124 (the line break falls inside "That this / person"). ANF6 is in `sources.ownWords`, and the Salmond title page is at ANF6 7636-7641.

**FIX 2.** `quotationOriginals[2].uncertain`. Salmond's "this very form of death" does render the Greek καί. Only McGiffert leaves it out.
- Old: `The modern "even" follows the Greek, which has a word for "even" there that neither print renders;`
- New: `The modern "even" follows the Greek, which has a word for "even" there; McGiffert leaves it out, and Salmond gives it as "this very form";`

## 4. References

These parts name things the brief does not tell, so they come out. A name that identifies something the brief does tell (Germanus, Taposiris, Pentapolis) stays.

**FIX 3.** `briefReferences[0]`. The brief does not name Heraclas.
- Old: `took charge of the school at Alexandria after Heraclas;`
- New: `took charge of the school at Alexandria;`

**FIX 4.** `briefReferences[2]`. The brief does not say the edicts are lost.
- Old: `the edicts of Decius, early in 250, are lost; the aim was`
- New: `the edicts of Decius, early in 250; the aim was`

**FIX 5.** `briefReferences[5]`. The brief does not tell the hearing or Cephro. It tells only the second persecution.
- Old: `Church History VII.11.3-13: his hearing before Aemilianus under Valerian and the sending to Cephro in Libya.`
- New: `Church History VII.11.3-13: the second persecution, under Valerian.`

**FIX 6.** `briefReferences[6]`. The brief does not tell the earlier rejections, or the thought and words. It tells the Greek.
- Old: `some before him had rejected the Revelation; he would not reject it; the thought, words and Greek of the Revelation against the Gospel and letter of John;`
- New: `he would not reject the Revelation; its Greek against the Gospel and letter of John;`

**FIX 7.** `briefReferences[8]`. The brief does not tell the Chronicle's eleventh year. It stays on the card in `datesNote`, and the Chronicle stays in `sources`.
- Old: `Church History VII.28.3: died in the twelfth year of Gallienus after seventeen years as bishop; McGiffert's note puts the death in the eleventh year in both versions of the Chronicle. Chronicle, in Jerome's Latin: Maximus ordained to the Alexandrian church in the eleventh year.`
- New: `Church History VII.28.3: died in the twelfth year of Gallienus after seventeen years as bishop.`

**FIX 8.** `briefReferences[14]`. The brief does not tell the claim that things were inserted.
- Old: `the Arians' use of his books, and the claim of insertion.`
- New: `the Arians' use of his books.`

**References that remain:** `[1]`, `[3]`, `[4]`, `[7]` and `[9]` to `[13]` as they stand, and the rest as fixed.

## 5. Census rules

The card uses only allowed keys and has no `briefLength`. It has three entries for the brief's three quoted spans, and none extra. No `briefReferences` entry has quotation marks. No audit, review or ruling is named. Spelling is American in the new text ("defense", "neighbors", "honorably"). "Defence" and "Refutation and Defence" are existing printed titles. No entry has a `secondReading`, since all three spans are new.

## 6. Not found, and anything else left in

- **"a century later" (`legacy.remembered[1]`): stands.** Robertson dates the Defence about 352, with a query. That is about ninety years after Dionysius's death, so "a century" is a round figure. No held source contradicts it, and the brief says "nearly a century later" of the same Arian claim.
- Nothing else on the card is clearly wrong.
