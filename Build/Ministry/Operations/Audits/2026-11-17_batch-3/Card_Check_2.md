# Card check 2: batch 3 (2026-11-17)

Checker for Process.md step 6 and `roles/card.md`. Three cards, each compared with its `.original.card.json`: the Third Council of Toledo, the Council of Chalcedon and Pachomius. Every quotation's modern wording was matched against the finished brief. Every printed wording was re-read at its file and lines in `cic/texts/`, by eye and by an exact-string script (whitespace and line breaks joined, markup removed). Each card was also run through `tools/validate-census.mjs` in a scratch copy of the census, with the brief as `longDescription` and a placeholder `secondReading`. In the changed list fields (`sources`, and Pachomius's `uncertain`) the pre-existing items were compared and are word for word, in their order, with nothing removed. `secondReading` is not judged here.

The "quotation not found verbatim" errors the validator gives for the modern renderings are release work (`tools/quote_renderings.json`), not card faults. They are not counted below.

Result: 3 FIX (Toledo, Chalcedon, Pachomius).

---

## third-council-of-toledo-589: FIX

- `briefLength` "about 3 minutes 20 seconds": justified. It is new, and the brief is 501 words.
- `sources.writtenLater`, Paul of Mérida (PL 80): justified. It is the file Q3 cites. The seven existing entries, and the other two groups, are untouched.
- `briefReferences` (9): justified. Each is new from the brief. Lines opened bear them out (ACTS 36590-36600, 36661-36662, 36900-36901, 36980-36987, 37255-37258, 37680-37681, 38033-38307, Saragossa 34271-34324, Seville 59276-59282; Mommsen 20313-20317, 20406-20410; Isidore 119220-119224; Dalton 17394; PL 80 12066-12071).
- `quotationOriginals` (8): all eight modern wordings match the brief exactly, and the brief has eight quotations. The key shape passes. Printed wordings verbatim, OCR kept: Q1 ACTS 36661-36662, Q2 Mommsen 20314-20316, Q3 PL 80 12068-12070, Q4 ACTS 36900-36901, Q5 ACTS 36981-36986, Q6 Mommsen 20408-20409, Q7 ACTS 37680-37681.
- **Fault, Q8** ("our people's new conversion", ACTS 37255-37258). Line 37258 begins "- nostrae". The printed wording drops the "- " without saying so, where every other entry keeps the file's marks. **Correction:** set `printed` to `"ut propter roborandam gentis - nostrae novellam conversionem"`. Add after `lines`: `"uncertain": "The \"- \" at the start of line 37258 is a scan mark, not in the print."`
- Left in place, `issue[1]` "nostram catholicam fidem": **upheld**. Migne's John of Biclaro, a card source, reads "ad nostram catholicam fidem" (PL 72, 64853-64854). Mommsen's apparatus says the manuscripts read the same and he emends to "a nostra catholica fide" (Mommsen 20210). The card quotes the manuscripts' text as printed. It is not wrong.
- Left in place, `attended[1]` "Two places in the printed text are damaged": **upheld as not found**. The signature list (ACTS 38033-38307) has one damaged place, Frosclus's see (38210, "Frosclus5?..... episcopus"). A search of the acts (36500-38320) for other gaps found none. A claim without found support is not wrong under `roles/card.md`, so it stays. Log it in the world's gaps record as "Toledo III signatures: second damaged place not found (card check, 2026-11-18)".

## council-of-chalcedon-451: FIX

- `briefLength` "about 3 minutes 45 seconds": justified. The brief is 561 words.
- `sources.writtenLater`, four new items (Evagrius Greek, Severus Select Letters VI part 1, the History of the Patriarchs, Michael the Syrian tome 2): justified. Each is a file that a quotation or its `uncertain` cites. The eight existing entries, and the other two groups, are untouched.
- `briefReferences` (15): justified. Spot-checked: npnf214 19159-19167, 20160-20178, 20286-20292; Perry 23843-23845; Ormanian 2502-2512; Synodicon 36950-36951; Walford 3408-3420.
- `quotationOriginals` (13): every modern wording matches the brief exactly. The key shape passes. These printed wordings are verbatim at their lines: Q1 19254-19260, Q2 20000, Q3 20002-20003, Q5 20170-20171, Q6 20172-20173, the Definition (Evagrius 5244-5246; Percival 20286-20292, with the endnote left out), Priscus (Evagrius 5396-5398, with the noise line left out and noted; Walford 3394-3395), Evetts 34869-34870 and 35109-35110, Severus 720-722, Zachariah 2181-2183 and 2375-2376.
- **Fault 1, the Anatolius entry** (`quotationOriginals[3]`, Mansi 7, 9802-9819). In the scan, the Latin column shares each line with the garbled Greek column. The printed wording is spliced with "..." and does not stand at those lines, so the census check rejects it ("does not stand in ... lines 9802-9819"). **Correction:** set `printed` to `"Propter fidem non eff"` and `lines` to `"9807"`. Replace `uncertain` with: `"Latin column, OCR as printed (long s read as f: \"eff\" for est). The speaker line is \"Anatolius reverendi(fimus archiepifcopus Con-\" (9802) and \"ftantinopolis dixit: *\" (9807). The sentence runs on across 9808-9819, each line shared with the garbled Greek column: \"damnatus Diofcorus , fed quia excommuni-\", \"cationem fecit domino archiepifcopo Leoni,\", \"& tertio vocatus ett, & noh venit, & ideo\", \"damnatus eft.\" (\"fed\" for sed, \"ett\" for est, \"noh\" for non). The brief's \"not for the faith\" renders \"Propter fidem non ... damnatus\". The refusers' chronicle quotes the same saying: \"Not for the faith is Dioscorus deposed\" (Zachariah III.1, tr. Hamilton and Brooks, cic/texts/zachariah-rhetor_chronicle_hamiltonbrooks1899.txt, 2321-2324)."`
- **Fault 2, the missing entry.** This is the batch's Q7, "two natures", the officials' order to add it (`Second_Reading_Key_2.md`). **Correction:** insert this after the "We believe as Leo" entry:
  ```json
  {
   "modern": "two natures",
   "printed": "Add then to the definition, according to the judgment of our most holy father Leo, that there are two natures in Christ united unchangeably, inseparably, unconfusedly.",
   "work": "The imperial judges to the bishops, Session V, tr. Percival",
   "file": "cic/texts/npnf214_seven-ecumenical-councils.xml",
   "lines": "20175-20178"
  }
  ```
- **Fault 3, the two terms.** The census check needs an entry for every double-quoted span in the brief. The key's note that "from two" and "in two natures" are "covered by Q1 and Q8" does not meet that rule. Q1 holds 'from two' in single quotes, inside a different span, and Q8's wording is the whole sentence. The validator reports both terms as having no entry. Nicaea sets the precedent: it gives terms their own entries ("of one being", "from God"). **Correction:** insert both after the "two natures" entry, before the Definition:
  ```json
  {
   "modern": "from two",
   "printed": "Dioscorus acknowledged that he accepted the expression “of two natures,”",
   "work": "The imperial judges, Session V, tr. Percival",
   "file": "cic/texts/npnf214_seven-ecumenical-councils.xml",
   "lines": "20166-20167",
   "uncertain": "A term, not a saying: the brief's \"from two\" is the formula ἐκ δύο (19256), which Percival gives as \"of two\"."
  },
  {
   "modern": "in two natures",
   "printed": "ἐν δύο φύσεσιν",
   "work": "The Definition of Chalcedon, Session V, as Evagrius copies it, Ecclesiastical History II.4, Greek, ed. Bidez and Parmentier",
   "file": "cic/texts/evagrius-scholasticus_historia-ecclesiastica-grc_bidez-parmentier1898.txt",
   "lines": "5245",
   "englishPrinted": "must be confessed to be in two natures,",
   "englishFile": "cic/texts/npnf214_seven-ecumenical-councils.xml",
   "englishLines": "20288-20289",
   "uncertain": "A term, not a saying: the Definition's formula. On the Greek of the acts, which reads ἐκ δύο, see the Definition's entry and Hefele (npnf214, 20361-20370)."
  }
  ```
  With faults 1 to 3 corrected, the scratch run gives no errors for this card other than the rendering listings. Card_Edits should list the three added entries as new and give the count as 16.
- Left in place, `traditions[0]` "Leo's legates presided over the votes": **upheld**. In Session IV the imperial judges put the question and called for the votes (npnf214 20123-20132), and the brief has the officials running the council. But the Latin of the acts has Leo command the legates "to preside in his place" (20033-20037), and the legates lead the sentence at Session III. Who presided is disputed, not clearly wrong.
- Left in place, `uncertain[3]` "The Greek text of the definition now reads 'of two natures'": **upheld**. Hefele, as Percival prints him, says "The present Greek text has ἐκ δύο φύσεων" and the old Latin "in duabus naturis" (npnf214 20361-20366). Evagrius's ἐν δύο (5245) does not contradict a statement about the acts' Greek.
- Left in place, `issue[4]` (Zachariah, Theodoret to preside): upheld. It is in the chronicle (2272-2276).

## pachomius: FIX

- `briefLength` "about 3 minutes 10 seconds": justified. The brief is 479 words.
- `sources.about`, seven new items: justified. Each is a file the brief or a quotation draws on. The three existing `about` entries and the `ownWords` entry are untouched. (Card_Edits says "after the four already there". There are three in `about` and four in all. This is a slip in the log, not in the card.)
- `briefReferences` (16): justified. Spot-checked: Amélineau 5182-5183; Acta 86626-86633; Palladius 405; Jerome PL 23 4335-4342; Ardo PL 103 30903-30911; Robertson npnf204 5641-5645; Cassian npnf211 18519-18531.
- `uncertain[0]`, "through his Coptic and Greek Lives," inserted: justified as a correction. The held Lives (Amélineau's Bohairic Life; Cardon's Latin of the Greek Life in the Acta Sanctorum) contradict "otherwise ... through Palladius ... and through Sozomen". The brief rests on them. Seven words were added, and the rest of the item is word for word. The other three items are unchanged.
- `quotationOriginals` (3): the modern wordings match the brief exactly, and the key shape passes. The printed wordings are verbatim with the OCR kept: Amélineau 5145-5146 and 6247-6248, Acta 86630-86633.
- **Fault 1, the missing entry.** The brief has four quotations (`Second_Reading_Key_2.md`, Q4), and the card has three. "the monks of Tabenna" has no entry, and the census check reports it. **Correction:** append:
  ```json
  {
   "modern": "the monks of Tabenna",
   "printed": "some from that of the monks of Tabenna,",
   "work": "John Cassian, Institutes IV.1, tr. Edgar C. S. Gibson",
   "file": "cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml",
   "lines": "18531"
  }
  ```
- **Fault 2, `datesNote`.** It reads "Born about 292, died 348 (George Schodde; Ernest Cushing Richardson's note to Gennadius)", and the brief has "346 or 348". **Ruling: correct it.** The attribution is true: Schodde 136 says "died in 348" and Richardson says "died 348" (npnf203 42254). But a held source contradicts the year itself. Robertson has "died on May 9, 346" (npnf204 5643-5644), which is now a card source. The Source_Sheet rates the year Contested, and the outline rules out "died in 348" as fact. Given alone, one side of a contested date reads as settled, against the finished brief. **Correction, fewest words:** `"Born about 292, died 348 (George Schodde; Ernest Cushing Richardson's note to Gennadius) or 346 (Archibald Robertson)"`. This adds four words and keeps each date with its own authority. List it in Card_Edits under "Clearly wrong", with Robertson npnf204 5643-5644 as the evidence.
- Left alone, `legacy.traces` (the women's house "across the river") and the verbatim items: upheld as Card_Edits gives them.
