# R3 review: era 4 batch 9

Round 3, the last round under the cap, a targeted recheck of the round 2 fixes and a final read of each brief and card, by two fresh Opus agents that had not seen the drafting or the earlier rounds, at full effort. Part 1 covers John of Damascus, Theodore the Studite, Cyril and Methodius and Clement of Ohrid. Part 2 covers Antony and Theodosius of the Kyiv Caves, Anskar, Rimbert, the rest of the README and Open-Gaps 269. Each part is given as its reviewer wrote it.

## R3 review, Part 1: john-of-damascus, theodore-the-studite, cyril-and-methodius, clement-of-ohrid, the README on these four, and Open-Gaps 269 on them

Round 3 is the last round under the cap. It was done by a fresh Opus reviewer at full effort, and no repo file was edited. I read CLAUDE.md, `Who_Profile_Pattern.md`, R2_review.md Part 1, R1_changes.md, R2_changes.md and `git diff 83d3b04e 9c58b577` for the four profiles, the README, `records.json` and Open-Gaps. I reopened each cited line in context and read every changed sentence as new text. I also read each brief and card once more as finished text.

**Summary: no blocking finding. 17 minor findings (R3-M1 to R3-M17).** One of them, R3-M2, is a round 2 fix that R2_changes.md reports as applied but that is missing from `records.json`.

## Mechanical checks (re-run)

| Brief | Words | FK | Flesch | Audio script |
|---|---|---|---|---|
| john-of-damascus | 405 | 7.24 | 68.61 | exact match |
| theodore-the-studite | 405 | 7.02 | 69.19 | exact match |
| cyril-and-methodius | 406 | 7.11 | 68.87 | exact match |
| clement-of-ohrid | 369 | 6.10 | 73.03 | exact match |

- All four pass `engine.m1.gates.grade_text`. All are within length: about 405 for majors and pairs, and about 365 for Clement.
- Audio: I rebuilt each script by code. Each is the brief with `[calmly] ` at the start and `[warmly] ` at the start of the last paragraph only, and there are exactly two tags in each file.
- Each card parses as JSON and ends in a newline, so R2-M1 is applied.
- Every quotation in quotation marks was reopened in its file and is verbatim:
  - "Anathema to Mansur, who has an evil name and Saracen opinions!" is NPNF14 l.39468-39469.
  - "we fall down and worship not the material but that which is imaged." is NPNF9 l.36281-36282. The file runs on with a colon.
  - "copied it out, and established it in his own monastery." is CROSS l.11871-11872. The file runs on with "to govern".
  - Card: "The Slavs rejoiced to hear the greatness of God extolled in their native tongue." is CROSS l.7899-7900.
- Sentences over 25 words in the briefs are all unchanged from round 2 and were accepted there. The longest is John's forged-letter sentence, at 26 words.

---

## john-of-damascus

**Verdict: passes, with three minor points.**

Round 2 fixes checked against their sources:
- **R2-M2, card `uncertain[2]`.** Applied, and right. Theophanes (Goar) l.75291 has "Mansur aviti nominis", and Anastasius l.121040 has "quod est avitum nomen ejus". Fabricius, PG94 l.566-568, has "Assentior tamen Theophani, qui ... Mansur ..., quod avus ejus ita diceretur". Le Quien, PG94 l.30617-30619, has "cognomen Arabicum Mansur, quod ejus progenitoribus ac toti familiae proprium fuit". The new sentence gives each man his own reading. **The records half of R2-M2 was not applied: see R3-M2.**
- **R2-M4, card `dates`.** The process word "held scan" is gone. The new wording makes a claim the scan cannot support: see R3-M1.
- **A-M9 left not taken.** This is acceptable. The brief's "When we see the image of Christ's crucifixion" drops Salmond's condition that the image brings the passion back to mind ("when we have not the Lord's passion in mind ... His saving passion is brought back to remembrance", l.36279-36281). The quoted words stand as written, and the frame adds nothing that the file lacks.

Read once more as finished text, the brief and card carry no blocking error.

**R3-M1 (card `dates`: R2-M4's new wording says the printed page reads 750, while `records.json` says the 750 is an OCR error).**
- Text: "Le Quien's printed text reads 750 for the second, but ties it to the year Leo drove Germanus out."
- Source: PG94 l.32113-32115: "Quod quidem praestitit anno Christi 750. quo Germanus solio de- / irusus est a Leone". `records.json` (john-of-damascus claims) has "anno Christi 750 [OCR for 730] quo Germanus solio detrusus est". Fabricius, PG94 l.1290-1297, puts the second speech "post Germanum in exsilium" and before "Christi 730".
- Only an OCR text is held. It cannot show what Le Quien's printed page reads, and the records treat the figure as a misread 3. The card should describe the copy used here, in the card's own "used here" register, and should not make a claim about the printed page.
- Replacement: "Le Quien dates the first two speeches on the images to 727 or 728 and to 730. For the second, the copy used here reads 750, but Le Quien ties it to the year Leo drove Germanus out."
  - This replaces the text from "Le Quien dates the first two speeches" to "drove Germanus out." Keep the rest of the field as it is.

**R3-M2 (`records.json`, contested claim "Mansur: family name or insult": the records half of R2-M2 was not applied).**
- Text: "Theophanes: the ancestral name (THEO l.75289-75291, l.121040); Fabricius agrees, the insult being Constantine's twist into Manzeros (PG94 l.552-578); Le Quien: the family's name (PG94 l.30617-30619)"
- R2_changes.md says "R2-M2, R2-M4 (John). Fixed as worded." The card was fixed. The records still say "Fabricius agrees", which is the narrowing R2-M2 found.
- Source: PG94 l.566-568, "quod avus ejus ita diceretur".
- Replacement: "Theophanes: the ancestral name (THEO l.75289-75291, l.121040); Fabricius reads it as the grandfather's name, the insult being Constantine's twist into Manzeros (PG94 l.552-578); Le Quien: the family's name (PG94 l.30617-30619)"

**R3-M3 (`records.json` and Open-Gaps 269: the line range for the 750 misses the line that carries it).**
- Records witness: "PG94 l.32109-32113; THEO l.73562, l.73735-73739". Open-Gaps 269: "PG 94 l.32109-32113".
- Source: the year and Germanus are at l.32114-32115 ("praestitit anno Christi 750. quo Germanus solio de- / irusus est a Leone"). The sentence begins at l.32111 ("Alteram / posthac composuit").
- Replacement, in both places: "l.32111-32115". In the records, also change the claim at "PG94 l.32054-32064, l.32106-32111" to "PG94 l.32054-32068, l.32111-32115". The "hoc anno 727, aut subsequenti 728" passage runs to l.32066-32068.

---

## theodore-the-studite

**Verdict: passes, with four minor points.**

Round 2 fixes checked against their sources:
- **R2-B2.** Applied, and right, in the card and the records. PG99 l.358-359: "sed mox anno proximo post Constantini mortem magno cum honore revocatus ab Irene, et abbas Studio praefectus fuit".
- **R2-M3, brief para 5.** Right. PG99 l.155226-155230: "Non possidebis servum ... hominem qui ad Dei imaginem factus est: hoc enim solis saecularibus concessum est, sicut nuptiae."
  - "Only lay people might own one, as only they might marry" says what the Latin says. The loose "that" is gone.
  - The card's "since owning slaves, like marriage, is allowed only to lay people" is right too.
  - The two trims are sound. Theophanes l.87175 has "monachi ad septingentos usque sub Theodoro militantes", which fits "counts up to 700 monks under him". "Sunday 11 November 826" keeps the date.
- **R2-M5, card `legacy.traces[1]`.** The facts are right. MEYER l.1042-1047: "Ermahnungen für den Hegumenos. Diese hat Athanasios mit geringen Abänderungen aus dem Abschnitt ἐντολαὶ τῷ καθηγουμένῳ der διαθήκη des Studiten übernommen. Und zwar stimmen Can. 1—5 des Theodoros fast wörtlich mit den Eingangsworten bei Athanasios." The sentence is 33 words: see R3-M4.
- **R2-M6, card `legacy.traces[2]`.** The facts are right. PG99 l.831-832: "Theodorum Studitam et Josephum (episcopum Thessalonicensem), ejus fratrem, laudat Codinus, Origg. C Pol." Then l.836-837 gives Nikephoros Kallistos: "Theodorus et Josephus Studitae ... proprio Studiorum monasterio tradiderunt". The sentence is 34 words, and "Codinus" is a bare name: see R3-M5.
- **R2-M7, card `uncertain[0]`.** Right. PG99 l.18788-18789: "Proemium quidem totum novum est: elocutio in reliquis semper ab illa edita Vita differt; sed tamen res narratae vix variant."
- **T-M4 left not taken** (the brief keeps "the restored priest Joseph"). This is acceptable. PG99 l.20305-20306 has "Josephus quidam presbyter, et ejusdem sanctissimae Magnae Ecclesiae oeconomus".

Read once more as finished text, the brief and card carry no blocking error. The rest of what I rechecked is right:
- The flogging and the ten monks: l.20541-20542, "cum decem aliis monasterii notabilioribus, Thessalonicam exsulem".
- Prusa: l.20523-20527.
- Theodote: l.20517-20518.
- The Studite rule at Kyiv: CROSS l.11866-11872.

**R3-M4 (card `legacy.traces[1]`: 33 words in one sentence).**
- Text: "Philipp Meyer says Athanasios the Athonite took his commands to the abbot, with slight changes, from Theodore's Testament, and that Theodore's first five commands match Athanasios's opening words almost word for word."
- Source: MEYER l.1042-1047, as above.
- Replacement: "Philipp Meyer says Athanasios the Athonite took his commands to the abbot, with slight changes, from Theodore's Testament. Theodore's first five commands, Meyer says, match Athanasios's opening words almost word for word."

**R3-M5 (card `legacy.traces[2]`: 34 words, and "after Codinus" names a writer with no context).**
- Text: "Fabricius, quoting Nikephoros Kallistos, says Theodore and Joseph, both of Stoudios, wrote Lenten canons for their monastery; after Codinus, he takes this Joseph to be Theodore's brother."
- Source: PG99 l.831-832, "laudat Codinus, Origg. C Pol." Codinus's work is the Origins of Constantinople. The bracketed "(episcopum Thessalonicensem)" is Fabricius's gloss on Codinus's Joseph.
- Replacement: "Fabricius, quoting Nikephoros Kallistos, says Theodore and Joseph, both of Stoudios, wrote Lenten canons for their monastery. Citing Codinus's Origins of Constantinople, he takes this Joseph to be Theodore's brother, the bishop of Thessalonica." Keep the Allatius sentence that follows.

**R3-M6 (card `uncertain[3]`: "they say" reads as the card's own hedge).**
- Text: "The Sirmond Life says she was related to him, they say;"
- Source: PG99 l.10266-10267: "Theodoten nomine, et genere, ut ferunt, patri propinquam". The "ut ferunt" belongs to the Life.
- Replacement: "The Sirmond Life says she was related to him, as people reported;" Keep the rest of the item.

**R3-M7 (brief para 3: Fabricius gets no context at his first mention in this text).**
- Text: "He was born in the city in 759, by Johann Fabricius's count."
- The Pattern says an identifier is needed for "any name a general listener would not know". John's brief gives "The bibliographer Johann Fabricius" (A-M2), and the brief and the card are separate texts.
- Replacement (same 12 words; 405 words, FK 7.14, Flesch 68.34): "The bibliographer Johann Fabricius dates his birth in the city to 759."

---

## cyril-and-methodius

**Verdict: passes, with two minor points.**

Round 2 fixes checked against their sources:
- **R2-B3.** Right. GIN l.1456-1460: "von dem Bischofe Gauderich oder Gaudentius von Velletri herrühre, der ein Zeitgenosse der Slawenapostel". Ginzel's own trust follows at l.1466-1469: "die verlässlichste Kunde, welche man in Rom aus dem Munde der Slawenapostel selbst schöpfte". So "He trusts it, and follows the Bollandists" holds.
- **R2-M8.** Right. GIN l.11490-11492: "mater cum multis lacrymis obtestata est, ut si aliquem ex nobis, antequam reverteremur, obiisse contingeret, defunctum fratrem frater vivens ad monasterium suum reduceret".
- **R2-M9.** Right. GIN l.13641-13664: "vilescere fecit cuncto populo ex parte missas et evangelia ecclesiasticumque officium illorum, qui hoc latine celebraverunt". "Partly cheapened the Latin Masses in the eyes of all the people" keeps the hedge.
- **R2-M10.** Right. GIN l.12326: "incitavit cor hostis Moravici regis cum omnibus episcopis".
- **R2-M11.** Right. GIN l.12538-12539 has "sexta die mensis Aprilis ... sexies millesimo trecentesimo nonagesimo tertio".
- **R2-M12.** Right.
- **C-M10 left not taken.** This is acceptable. "A Life of Methodius says God revealed the Slavonic letters to the Philosopher" puts no time on the revelation.

Read once more as finished text, the brief and card carry no blocking error. I rechecked these lines:
- 30 December: GIN l.11298, "III. Calendarum Januariarum".
- The rib like a star, the head and the anchor: l.11313-11330.
- Forty days and 14 February: l.11478-11479, "post quadraginta dies ... sexto decimo Kalendas Martias".
- The consecration: l.11470-11471.
- Rastislav's request: l.11394-11401.
- John VIII on the three languages: l.13974-13976.

**R3-M8 (`records.json`, contested claim "The day of Methodius's death": the R2-M11 correction was not carried into the records).**
- Text: "Life of Methodius and Ginzel: 6 April 885 (GIN l.12536-12541, 6170-6205)"
- Source: GIN l.12538-12539, which gives 6 April in A.M. 6393. Ginzel works it out as 885 at l.6198-6206. The card now says this.
- Replacement: "Life of Methodius: 6 April, A.M. 6393 (GIN l.12536-12541); Ginzel works the year out as 885 and defends the date (GIN l.6170-6205)"

**R3-M9 (brief paras 2 and 4: Ginzel and Dümmler get no context at first mention).**
- Text: "The finding is told in what Johann Ginzel calls the Italian Legend." and "Ernst Dümmler thought a pupil of Methodius wrote it soon after his death."
- This is the same Pattern point as R3-M7. A general listener does not know who either man is. "Ginzel, who writes against the Greek schism" comes two paragraphs after Ginzel's first mention.
- Replacements, applied together (406 words, FK 7.39, Flesch 67.74):
  - "The finding is told in what the historian Johann Ginzel calls the Italian Legend."
  - "The historian Ernst Dümmler thought a pupil of Methodius wrote it soon after his death."
  - For length, para 3: "Rastislav, prince of Moravia, sent to the emperor for a teacher. His people had left their idols, he said, but had no teacher." becomes "Rastislav, prince of Moravia, asked the emperor for a teacher, since his people had left their idols but had none."
    - Source for the merged sentence: GIN l.11396-11401, "nuntians hoc, quod populus suus ab idolorum quidem cultura recesserat ... verum doctorem talem non habent ... rogare se ut talem hominem ad partes illas dirigat". The merge also removes the doubled "teacher".
  - For length, para 2: "a bishop of the brothers' own time" becomes "a bishop of the brothers' time", which is the card's wording.

---

## clement-of-ohrid

**Verdict: passes, with two minor points.**

Round 2 fixes checked against their sources:
- **R2-M13.** Right. PG126 l.99596-99600: "Deposuerat haec omnia in monasterio, quod in Achride construxerat, adhuc superstite beatissimo Borise, priusquam Velitzae episcopatum suscepisset". l.99604-99606: "proprium aedificare monasterium, cui etiam alteram adjecit ecclesiam, quae postea archiepiscopatus sedes constituta est".
  - "He had built a monastery at Ohrid before he became bishop, and added a church" says what the Life says.
  - The brief names only one see, so "before he became bishop" is not ambiguous.
- **R2-M14.** Right. PG111 l.36940-36948 has "VITA S. CLEMENTIS ... CIRCA MEDIUM SECULUM X".
- **R2-M15.** Right. PG126 l.99241-99243 and l.99269-99270: "Ex illis lectores, subdiaconos, diaconos, et presbyteros ordinat. In unaquaque dioecesi trecentis jussa dabat discipulis".

Read once more as finished text, the brief and card carry no blocking error. I rechecked these lines:
- The prison and the earthquake: PG126 l.98425-98446.
- Belgrade, and Boris's longing to talk with them: l.98960-98971 and l.99006-99008, "Ardens desiderium habebat quotidie cum eis colloquendi".
- The seven years: l.99302, "Jam octavus erat annus".
- Symeon as first king: l.99307-99308.
- "Bulgariae linguae Clemens primus constituitur episcopus": l.99370-99372.
- The priests and Greek: l.99549-99552.
- The plea to Symeon and his reply: l.100125-100155.
- The Triodion: l.100238-100242.
- The closing prayer: l.100505-100506.
- Theophylact's death in 1107: l.96739.

**R3-M10 (brief para 1: leaving R2-M16 "not taken" is not acceptable; "the Third Hour" is an undefined term).**
- Text: "They sang the Third Hour's hymns, then the psalms."
- The Pattern lists "undefined technical terms" as a checklist failure. A listener does not know that the Third Hour is one of the set hours of prayer, and "for length" is not a reason to keep a fault when a trim can pay for the fix. The source has "canticis tertiae horae decantatis" (PG126 l.98437-98438).
- Replacement: "They sang the hymns of the Third Hour of prayer, then the psalms."
- For length, para 4: "Boris sent Clement to teach in Kutmichevitsa, and gave him houses at Devol." becomes "Boris sent Clement to teach in Kutmichevitsa." The card's `place` keeps "with houses at Devol".
- Result: 367 words, FK 6.03, Flesch 73.36.

**R3-M11 (brief para 2: Miklosich and Ginzel get no context at first mention; optional, and it costs length).**
- Text: "Franz Miklosich argued that ..." and "Johann Ginzel thinks Theophylact reworked older notes."
- This is the same Pattern point as R3-M7 and R3-M9, but it is weaker here, because "argued" and the next sentence's "Migne's editors" set both men among the scholars.
- Replacement, if wanted: "The scholar Franz Miklosich argued that ..." and "The historian Johann Ginzel thinks ..." With R3-M10, the brief is 371 words, FK 6.13, Flesch 72.94. If 371 is judged too far over "about 365", leave R3-M11 and take R3-M10 alone.

---

## README statements on these four

**R3-M12 ("Majors and lengths": the range is stale after round 2).**
- Text: "Their briefs run 404 to 406 words, about 2:30"
- Theodore is now 405 (R2-M3 trims). The five majors are at 405, 405, 406, 405 and 405.
- Replacement: "Their briefs run 405 to 406 words, about 2:30"

**R3-M13 ("John of Damascus, the live entry": the README gives Theophanes a year that the records give as A.M. 6221, 729/30).**
- Text: "Le Quien ties it to Germanus's fall, which Theophanes puts in 730"
- Source: Theophanes, under the heading "A. M. 6221" (THEO l.73562), at l.73735-73739: "Porro Germanum ... patriarchali solio dejecit". `records.json` has "which Theophanes places in A.M. 6221 (729/30)".
- Replacement: "Le Quien ties it to Germanus's fall, which Theophanes puts in the year of the world 6221 (729/30)"

The README's other statements on these four check out:
- The two census rows. In `cic-website/data/world-census.json`, both John of Damascus person rows have the year 730, Iconophile quotes `npnf209` l.36233-36234, and Melkite has a `held` pointer.
- The Theodore Lives.
- Cyril and Methodius's sources (R2-M18 applied).
- Clement and Patrologia Graeca 111.
- The re-score corrections for these four.
- The names and ids.

---

## Open-Gaps 269, the items on these four

The entry exists, so R2-B1 is closed. Checked against the batch files:
- **John's census year.** It is right on the census rows, the quotation and the Fabricius date. PG94 l.942-943: "cum praefixa epistola ad Cosmam, Majumae jam episcopum, adeoque scripta post a. c. 743". The line range needs fixing: see R3-M3.
- **Clement's ruling.** It matches the README.
- **Re-score corrections.** They match the README for John, Theodore and Clement. For Cyril and Methodius, one is missing: see R3-M16.
- **Library items.**
  - It is right that there is no English of the image speeches, and that Mansi tomi 12-13 are not held. Mansi 10, 11 and 14 onward are.
  - It is right that there is no Life of Constantine, no Slavonic Life of Methodius and no work by Clement. Ginzel holds only the Latin of the Life of Methodius.
  - "the Short Life ascribed to Demetrios Chomatenos" rests on no held line. Chomatenos appears in PG126 only as a variant witness to Theophylact's letters, at l.17923-19667. As a want, it is acceptable.

**R3-M14 (river counting rule: "with" reads as "including").**
- Text: "Greek East & Orthodoxy era 4 now holds eight majors (five before, with John of Damascus, Theodore, and Cyril and Methodius) and Latin West & Catholicism eleven (ten, with Anskar)."
- "five before, with John ..." can be read as five that already included John.
- Replacement: "Greek East & Orthodoxy era 4 now holds eight majors (five before, and three more with John of Damascus, Theodore, and Cyril and Methodius) and Latin West & Catholicism eleven (ten before, and Anskar)."

**R3-M15.** This is the line range for the 750, given in R3-M3.

**R3-M16 (re-score corrections: one of the README's Cyril and Methodius corrections is missing).**
- README text: "No held line names Methodius's jailer or calls him "of Sirmium"."
- Open-Gaps 269 has the Salzburg and Industriae tuae locations, but not this.
- Replacement: after "Industriae tuae at l.13878-13982", add "; no held line names Methodius's jailer or calls him "of Sirmium"".

**R3-M17 (the entry cites a Decision-Log entry that does not exist yet).**
- Text: "Decision-Log, "Who profiles, era 4 batch 9" (2026-11-15)."
- I searched `Decision-Log.md` for "batch 9". The only hit is the batch plan (l.3163).
- Handover.md lists this entry as step 4 of what is left. This is the same kind of fault as R2-B1. It is not blocking if the entry is written before the merge, as planned.
- Fix: write the Decision-Log entry before the merge, or change the citation to "Decision-Log (entry to be written)".

---

## Not-taken findings, judged

| Finding | Judgment |
|---|---|
| A-M9 (John: Salmond's condition) | Acceptable |
| T-M4 (Theodore: "priest Joseph" in the brief) | Acceptable |
| C-M10 (Cyril and Methodius: the time of the revelation) | Acceptable |
| R2-M16 (Clement: the Third Hour) | Not acceptable. See R3-M10, which pays for the fix with a trim. |

## Files and ranges opened

- CLAUDE.md (in context); `Build/Ministry/Features/Church-Family-Tree/Who_Profile_Pattern.md` (whole).
- `Build/Ministry/Operations/Audits/2026-11-15_who-profiles-era4-batch9/`: R2_review.md l.1-284; R1_changes.md and R2_changes.md (whole); Handover.md (whole).
- `git diff 83d3b04e 9c58b577` (word diff) for the four briefs and cards, `records.json` and Open-Gaps.
- Batch 9: the four briefs, cards and audio scripts; the `records.json` entries for the four ids; README.md (whole).
- `Build/Ministry/Features/Church-Family-Tree/Open-Gaps.md` l.3508-3523; `Decision-Log.md` (grep "batch 9").
- `cic-website/data/world-census.json`: the John of Damascus person rows; the era 4 `kind: person` rows by lane.
- cic/texts:
  - `john-damascus_opera-omnia-t1-with-vita-pg94-grc-lat_migne1860.txt` l.562-575, 936-946, 1280-1300, 30612-30622, 32050-32070, 32104-32116 (grep for 7xx dates).
  - `theophanes-confessor_chronographia-pg108-grc-lat_migne1863.txt` l.73562, 73720-73742, 73923-73990, 75278-75292, 87155-87177, 121034-121042 (grep "A. M. 62", "Germanus", "septingent").
  - `npnf214_seven-ecumenical-councils.xml` l.39466-39470.
  - `npnf209_hilary-poitiers-john-damascus.xml` l.36279-36283.
  - `theodore-studite_opera-omnia-pg99-grc-lat_migne1860.txt` l.355-360, 826-840, 6860-6892, 10266-10267, 18784-18790, 20515-20545, 155222-155232 (grep "aiunt", "Theodot").
  - `athos-monasteries_haupturkunden-fur-die-geschichte-der-athoskloster-ger-grc_meyer1894.txt` l.1038-1048.
  - `russian-primary-chronicle_cross1930.txt` l.7896-7901, 11862-11873.
  - `ginzel_geschichte-der-slawenapostel-cyrill-und-method-deu-lat_1861.txt` l.1440-1480, 11288-11330, 11392-11426, 11455-11493, 12322-12330, 12532-12542, 13636-13666, 13955-13980.
  - `theophylact-ohrid_opera-t4-with-vita-clementis-pg126-grc-lat_migne1864.txt` l.98405-98450, 98960-99010, 99238-99272, 99285-99312, 99365-99400, 99535-99608, 100110-100170, 100195-100245, 100500-100508 (grep "1107", "Chomat", "Belgrad", "Simeon").
  - `nicholas-mystikos_epistolae-with-eutychius-alexandrinus-pg111-grc-lat_migne1863.txt` l.36940-36949.
  - A file listing of cic/texts for Mansi, Cyril, Methodius and Clement holdings; grep for "Chomaten" across cic/texts.
- Scripts: `engine.m1.gates.grade_text` and word counts on the four briefs, and on scratch strings with the R3-M7, R3-M9, R3-M10 and R3-M11 replacements; the audio-versus-brief rebuild; JSON parse and trailing-byte checks; a sentence-length scan.

---

## R3 review, era 4 batch 9: Part 2 (Kyiv pair, Anskar, Rimbert, the rest of the README, Open-Gaps 269 items)

Round 3, the last round under the cap. A fresh Opus reviewer, full effort. No repo file was edited. Suggested brief replacements were test-applied to a scratch copy only (`r3p2/anskar.txt` in the scratchpad).

**Abbreviations.** CROSS = `cic/texts/russian-primary-chronicle_cross1930.txt`; PAT = `cic/texts/kievan-caves-paterik_paterik-kievskago-pecherskago-monastyria-chu_abramovich1911.txt`; MOUR = `cic/texts/mouravieff_history-of-the-church-of-russia_blackmore1842.txt`; ROB = `cic/texts/rimbert_anskar-the-apostle-of-the-north_robinson1921.txt`; WAITZ = `cic/texts/rimbert_vita-anskarii-accedit-vita-rimberti-lat_waitz1884.txt`; ADAM = `cic/texts/adam-bremen_gesta-hammaburgensis-ecclesiae-pontificum-lat_schmeidler1917.txt`; OP = `cic/texts/olavus-petri_samlade-skrifter-v1-swe_hesselman1914.txt`; CENSUS = `cic-website/data/world-census.json`; OG = `Build/Ministry/Features/Church-Family-Tree/Open-Gaps.md`; DL = `Build/Ministry/Features/Church-Family-Tree/Decision-Log.md`.

**Count.** 1 blocking (a close-out record, not a content error in any brief or card), 12 minor. No blocking content error remains in the three briefs or cards.

## Re-run checks

| Brief | Words | FK | Flesch | Pass |
|---|---|---|---|---|
| antony-and-theodosius-of-the-kyiv-caves | 405 | 5.89 | 72.61 | yes |
| anskar | 405 | 6.09 | 77.84 | yes |
| rimbert | 365 | 5.97 | 80.32 | yes |

The other four, for the README's numbers: john 405, theodore 405, cyril-and-methodius 406, clement 369.

- **Audio.** All seven `audio/<id>.audio.txt` equal their briefs, rebuilt by script with `[calmly] ` at the start and `[warmly] ` at the start of the last paragraph only. Exact match on all seven.
- **Quotations.** Every quotation in quotation marks in my three briefs and cards matches its file (script, whitespace- and hyphen-tolerant, then by eye). CROSS l.11777 "Oh Lord, strengthen me in this place"; l.12662-12663 "Change not ..."; l.11843-11846 "Many monasteries ..."; ROB l.4325-4329 (the old man, split at "It is good for us,"); l.5557-5560 "Were I worthy ..."; l.3747-3748 (decree); l.820-823 "some small part ..."; l.240-243 "the inspiring example ...". The two misses are the scan marks the README names: ROB l.2652 "cloakf", and CROSS l.11853-11860, where a running head (l.11856) and a stray quote mark ("Let him be ‘your prior", l.11860) sit inside "Who ... your prior". The words are otherwise exact.
- **Round 2 fixes in my part, checked in context.** R2-B1 (Kyiv `knownFor` neutral; new `uncertain` item and contested claim): right against CROSS l.11849-11861 and PAT l.2091-2097 ("възвѣстиша преподобному Антонию ... Преподобный же призвавъ святого Феодосиа, благословивъ его": the "venerable one" is Antony, just named). R2-B2 (Svyatoslav and Vsevolod): right against CROSS l.12527-12531 and PAT l.3586-3590; the letter goes to the one "сѣдшу на столѣ" (PAT l.3606-3619), whom the Chronicle names as Svyatoslav. R2-M1 "helped him escape": CROSS l.12855-12857 "Svyatoslav caused Antonius to escape by night to Chernigov". R2-M2 "so that others might follow his example": CROSS l.11765-11766 "that many other monks might spring from his example". R2-M3 to R2-M6: right against PAT l.2158-2164, PAT l.3692-3696, MOUR l.1616-1622. R2-M8: ROB l.1293-1294. R2-M9: OP l.858-863 ("dateradt 1527 ... 10 maj 1528 ... Paulum Helie af karmeliters orden i Danmark"). R2-M10: ROB l.802-806, 816-820. R2-B3: right in substance against ROB l.4269-4277, but its wording leaves a dangling "that rule" (R3-M3). R2-M11: ROB l.1164-1170, ADAM l.6202. R2-M12: in substance right against ADAM l.6779-6784, 6826, but the new wording reverses the relation (R3-M4). R2-B4 and R2-M13 to R2-M16 in the README: see below.

---

## antony-and-theodosius-of-the-kyiv-caves

**Verdict: passes. Round 2's two blocking fixes are right. Two minor card fixes.** Read once more as finished text against CROSS l.11740-11880, 12520-12700, 12845-12862, 13331-13402, 15045-15058 and PAT l.1028-1042, 1160-1252, 1312-1320, 1648-1672, 2086-2100, 3584-3660, 9098-9205. Every sentence of the brief has its source, and nothing contested is told as settled. The brief tells the Chronicle's choice of Theodosius under "The Chronicle says", and the 1062 move under "by Nestor's account". It does not say where Antony died.

**R3-M1 (card `uncertain[7]`, last sentence: 37 words, two claims joined by a semicolon).**
- Text: "The Paterik heads its founding account as Nestor's, and there the writer says Theodosius received him at seventeen; A. N. Mouravieff, who also has Nestor enter at seventeen, calls him an eyewitness of Theodosius's life."
- Source, unchanged in substance: PAT l.1236-1241 ("придох же азъ к нему, худый и недостойный рабъ Нестерь и пріатъ мя, тогда, ми лѣт сущу 17", OCR-normalised); MOUR l.1616-1622.
- Fix: "The Paterik heads its founding account as Nestor's, and there the writer says Theodosius received him at seventeen. A. N. Mouravieff, who also has Nestor enter at seventeen, calls him an eyewitness of Theodosius's life."

**R3-M2 (card `uncertain[0]`: "beside it" places the 1406 copy wrongly, and it is another redaction).**
- Text: "D. I. Abramovich prints an older copy of 1406 beside it."
- Source: PAT l.162-166: "Въ Приложенія къ изданію входятъ: 1. Арсеніевская редакція Кіево-Печерскаго Патерика по списку ... 1406" (OCR-normalised). The 1406 copy is in the appendices, and it is the Arsenian redaction, not an older copy of the 1462 text. The records already say "the Arsenian copy of 1406 in the appendix".
- Fix: "D. I. Abramovich prints the older Arsenian redaction, from a copy of 1406, in an appendix."

---

## anskar

**Verdict: passes. Round 2's card fixes are right. Two minor points.** Read once more as finished text against ROB l.796-826, 1288-1300, 2135-2226, 2635-2705, 3800-3856, 4292-4362, 5548-5562, and the Waitz, ANNBERT and ADAM lines round 2 cites. Para 7's two sides keep Waitz's "thinks" and Adam's "as others told it". "Friend and counselor" is fair to ROB l.3826-3832 ("to make use of his advice and to treat him in every respect as a friend").

**R3-M5 (card `legacy.remembered[1]`: "Ansgar" in the narrator's own words; one term for one thing).**
- Text: "In 1527 Paulus Helie, a Carmelite in Denmark, wrote that the Swedes had left the faith Ansgar preached."
- The card's name is Anskar. "Ansgar" is listed under `otherNames` as the Swedish form, and OP l.872-875 spells it "Ansgars", but this is the narrator speaking, so the form should be the card's own. No quotation marks are involved.
- Fix: "In 1527 Paulus Helie, a Carmelite in Denmark, wrote that the Swedes had left the faith Anskar preached."

**R3-M6 (brief para 7: R2-M7 "not taken". Leaving it is acceptable, but a fix exists at 405 words).**
- Text: "Adam of Bremen put the sack in the emperor Louis's last year, as others told it."
- This is Adam's only mention in the brief. Without a time, a listener cannot weigh him against the Annals of Saint-Bertin, which are of the time (the pattern's "no statements that have no context"). The card gives his time ("writing in the 1070s"), but the card is a separate text. Round 2 left it out because its fix took the brief to 407 words. The version below stays at 405 and also moves one passive sentence to active voice.
- Source for the time: ADAM l.3551-3557, as round 2 cited (books 1-2 perhaps 1074); the card already says "writing in the 1070s". For the Job line: ROB l.2697-2699 "he repeated again and again the words of Job".
- Fix (three replacements, applied together; tested at **405 words, FK 6.09, Flesch 77.84**, scratch `r3p2/anskar.txt`):
  - "His Life was written by Rimbert, his disciple and successor, with help from a fellow disciple." becomes "Rimbert, his disciple and successor, wrote his Life with help from a fellow disciple."
  - "Adam of Bremen put the sack in the emperor Louis's last year, as others told it." becomes "Writing in the 1070s, Adam of Bremen put the sack in the emperor Louis's last year, as others told it."
  - "Anskar said again and again the words of Job:" becomes "Anskar kept repeating the words of Job:"
  - Rebuild `audio/anskar.audio.txt` from the brief.

---

## rimbert

**Verdict: passes on facts. Round 2's R2-B3 fix is right in substance, but its wording leaves "that rule" with nothing to point to (R3-M3). One further wording fix (R3-M4).** Read once more as finished text against WAITZ l.4521-4560, 4608-4634, 5395-5423, ROB l.1140-1172, 2392-2402, 4225-4285 and ADAM l.6198-6204, 6774-6790, 6822-6828. "In Flanders" rests on ROB l.2398 and WAITZ l.1832 ("in Flandria"). "Three days later" is WAITZ l.4626 "tertia vero die transacta".

**R3-M3 (card `uncertain[3]`, round 2's fix: "that rule" has no antecedent in the card).**
- Text: "Robinson also notes that G. H. Klippel, going by that rule, takes the priest who said Mass with Anskar on his second Swedish journey to be Rimbert. Robinson thinks that priest more likely Erimbert, since Rimbert was then still a deacon."
- Round 1's sentence named the rule ("the Life of Rimbert's rule that every most faithful disciple is Rimbert"). Round 2 replaced that sentence, but its "that rule" was written as though the rule were still stated. Nothing in this card states it; only the brief does (para 4), and the brief and card are separate texts. A card reader cannot tell what rule is meant.
- Source: ROB l.4269-4277: "Klippel identifies this priest ... with Rimbert ... He deduces this from the statement in the Vita Rimberti, chap. ix., in quo videlicet libro ubicunque commemoratio fit cujusdam fidissimi discipuli ejus ... ipsum sciat fuisse Rimbertum. It would appear however, that at this time Rimbert was still in deacon's orders, and therefore could not have celebrated Mass ... It is more likely that the priest referred to is Erimbert." WAITZ l.4790-4800 has the same statement.
- Fix (replace those two sentences): "The Life of Rimbert says that wherever the Life of Anskar speaks of a most faithful disciple, it means Rimbert. Going by that rule, Robinson notes, G. H. Klippel takes the priest who said Mass with Anskar on his second Swedish journey to be Rimbert. Robinson thinks that priest more likely Erimbert, since Rimbert was then still a deacon."

**R3-M4 (card `uncertain[1]`, round 2's fix: the relation is reversed).**
- Text: "Bernhard Schmeidler's margin sets the burial day beside the Life of Rimbert's twenty-fourth chapter, which the copy used here lacks."
- The margin note ("V. Rimb. c. 24") is printed beside Adam's burial day. The sentence says the margin places the burial day beside the chapter.
- Source: ADAM l.6780-6783: "F. Rimb. c. 24. positio est III idus Iunii. Sepultus est extra basilicam sancti Petri" (OCR as printed), continuing "Cuius de-" from l.6781.
- Fix: "Beside the burial day, Bernhard Schmeidler's margin cites the Life of Rimbert's twenty-fourth chapter, which the copy used here lacks."

---

## README.md (the rest, with the river counts and the Kyiv placing)

**Verdict: R2-B4's rewrite is right. The counts match the census and the card traditions. The Kyiv era 5 placing is accurately reported. Four minor fixes.**

**River counts, re-checked.**
- CENSUS `kind: "person"` rows, era 4, for every era 4 major: Greek East & Orthodoxy has Martin I, Maximus, Photius, Athanasios and Symeon, five. Latin West & Catholicism has Bede, Boniface, Aidan, Hild, Adomnán, Alcuin, Dhuoda, Nennius, Hincmar and Humbert (`humbert-of-silva-candida`, `laneLabel` "Latin West & Catholicism", `start` 1054, `toldWithin` "latin-papal-church-gregorian"), ten.
- The majors are the batch 1, 2, 4, 5 and 7 READMEs' marks; batches 3, 6 and 8 have none. The other batch 2 majors (Benjamin I, Jacob of Edessa, Timothy I, Dionysius, Gregory of Narek) and Alopen sit in other rivers.
- With this batch, John of Damascus (Melkite Arabic, Iconophile, both Greek East era 4), Theodore (Iconophile) and Cyril and Methodius (Cyrillo-Methodian, Greek East era 4) make eight. Anskar (Scandinavian Conversion, Latin West era 4) makes eleven. Rimbert and Clement are not major.
- By era 4 card traditions: Humbert's card has "The Latin Papal Church (Gregorian Reform to Innocent III)" (era 5) and "The Byzantine Imperial Church (Macedonian Era)" (era 4, Greek East). That gives Greek East 5 + 1 + 3 = 9 and Latin West 9 + 1 = 10. Maximus's second tradition, Latin African Christianity under Byzantium, is era 3, in the Africa river, so it does not move him. The README's 8 and 11, and 9 and 10, are right.

**Kyiv era 5 placing, re-checked.** CENSUS: `kievan-rus-christianity` era 4, "988-1054"; `kievan-rus-christianity-1054-1240` era 5. Era 5 runs 1054-1300. 1062 is 6570 in Nestor's Life (PAT l.2162-2164). The paragraph's account of what falls on each side of 1054 is right: CROSS l.11740-11787, PAT l.1119 (the brothers gather after Yaroslav's death in the founding account too), PAT l.1683-1686. The DL ruling (l.2016-2040) says only that a name sits "at the point matching the dates the person was active". The README now gives "Best-known dated act" as the coordinator's relay, as R2-M16 asked.

**R3-M7 ("Majors and lengths": stale count).**
- Text: "Their briefs run 404 to 406 words, about 2:30".
- `wc -w`: john 405, theodore 405 (it was 404 before round 2's R2-M3), cyril-and-methodius 406, Kyiv 405, anskar 405.
- Fix: "Their briefs run 405 to 406 words, about 2:30".

**R3-M8 ("Antony and Theodosius are the worker's call": one sentence of 49 words with two nested asides).**
- Text: "The coordinator ruled (2026-11-15; Mark may overrule), by the active-year rule Mark set, which the coordinator relayed as "Best-known dated act" (Decision-Log, "Map Who: how many names, which names, and where they sit", 2026-11-11), that they go on the map in era 5 and the 1054-1240 tradition."
- As placed, the citation also reads as though the DL holds the phrase "Best-known dated act", which it does not (DL l.2016-2040).
- Fix: "The coordinator ruled (2026-11-15; Mark may overrule) that they go on the map in era 5 and the 1054-1240 tradition. The ruling applies Mark's rule that a name sits at the dates the person was active (Decision-Log, "Map Who: how many names, which names, and where they sit", 2026-11-11). The coordinator relayed that rule as "Best-known dated act"."

**R3-M9 ("Who the sources are", Antony and Theodosius: three of the five differences are not Chronicle against Paterik).**
- Text: "Where the Chronicle and the Paterik differ (Antony's journeys, Theodosius's tonsure year, who chose him as prior, who built the monastery above ground, the source of the Studite rule), the card gives both."
- The Paterik holds both sides of three of these. Its founding account, headed as Nestor's, agrees with the Chronicle on who chose Theodosius (PAT l.1219-1223: "кто таковь есть въ васъ, якоже блаженный Феодосій ... Да будеть вамъ игуменъ"), on who built the monastery (PAT l.1169-1170: "Игуменъ же и братія заложиша церковь велику и монастырь"), and on Michael and the Studite rule (PAT l.1230-1233). Only Nestor's Life differs (PAT l.2091-2097, 2158-2164, 2170-2176). The card and records already state it this way.
- Fix: "Where the accounts differ (Antony's journeys, Theodosius's tonsure year, who chose him as prior, who built the monastery above ground, the source of the Studite rule), the card gives both. On the last three, the Paterik's founding account agrees with the Chronicle, and Nestor's Life differs."

**R3-M10 ("Language and quotations": the Cross range and the second scan mark).**
- Text: "Two brief quotations cross a scan mark in their files, and the words are otherwise exact: a footnote mark in Robinson's "cloakf" (l.2652), and a running head inside Cross's "Who ... among you" (l.11855-11860)."
- "Who" is at CROSS l.11853, and the quotation also crosses a stray quote mark at l.11860 ("Let him be ‘your prior."). "Two brief quotations" can also be read as "two short quotations".
- Fix: "Two quotations in the briefs cross scan marks in their files, and the words are otherwise exact: a footnote mark in Robinson's "cloakf" (l.2652), and in Cross's "Who ... your prior" (l.11853-11860) a running head and a stray quote mark before "your"."

Checked and passing: the opening and the batch 10 split; the "Names and ids" list; "Card traditions" (the census names and dates, with "(988 to 1054)" now matching CENSUS); "Corrections to the re-score" for Antony and Theodosius and for Rimbert (ROB l.2398-2400; WAITZ l.1832-1833; WAITZ l.5395-5423 ends in chapter 23); the Anskar and Rimbert source lines; the file table.

---

## Open-Gaps 269 (my items: the river counts, the Kyiv pair, Rimbert, Anskar, and the entry's own cross-references)

**R3-B1 (close-out record: the entry cites a Decision-Log entry that does not exist; this blocks merge, not a content point).**
- Text (OG l.3516): "Source: `Build/Ministry/Operations/Audits/2026-11-15_who-profiles-era4-batch9/`; Decision-Log, "Who profiles, era 4 batch 9" (2026-11-15)."
- `grep -n "batch 9" DL` finds only l.3163, the re-score's batch plan. The batch's entry is not on the branch. It is also where R2_changes (R2-M16) says Mark's Clement ruling and the coordinator's Kyiv placing are to be recorded. This is a stale cross-reference (Style Guide 1.10), the same kind as round 2's R2-B1 for the Open-Gaps entry.
- Fix: write DL "Who profiles, era 4 batch 9" (2026-11-15) before merge. It should carry Mark's pick for Clement, "Keep as Who, dispute told (Recommended)" (relayed by the coordinator, 2026-11-15); the coordinator's five major marks; the Kyiv era 5 placing with active year 1062 (Mark may overrule); and the batch 10 split.
- Related: the entry's first sentence says the seven profiles "are approved to proceed". That is true only once this round closes with no blocking point left open. If any blocking point goes to Mark, change it to "are held, with [the open point] before Mark".

**R3-M11 (river-count bullet: the asides read as the wrong counts).**
- Text: "By the census Who rows, Greek East & Orthodoxy era 4 now holds eight majors (five before, with John of Damascus, Theodore, and Cyril and Methodius) and Latin West & Catholicism eleven (ten, with Anskar)."
- "(ten, with Anskar)" reads as ten *including* Anskar, and "(five before, with John ...)" reads as five *including* John. The three Greek East additions and Anskar also have no census Who rows yet; they are counted by their cards.
- Fix: "By the census Who rows, Greek East & Orthodoxy era 4 held five majors and Latin West & Catholicism ten. John of Damascus, Theodore, and Cyril and Methodius make the Greek East eight, and Anskar makes the Latin West eleven."
- The rest of the bullet (nine and ten by era 4 card traditions; Humbert's row; five per river; owner) is right (CENSUS; OG l.2177-2183).

**R3-M12 (re-score corrections bullet: one README correction missing).**
- Text: "Antony and Theodosius: no held line gives Antony's death year."
- The README's corrections list has a second item for the pair: "The Paterik's base text begins only partway into its seventh discourse." That bears on the re-score row's line pointers into the Paterik (Rescore.md l.146), so the re-score's next revision needs it too.
- Fix: "Antony and Theodosius: no held line gives Antony's death year, and the Paterik's base text begins only partway into its seventh discourse."

Checked and passing: the Kyiv bullet (coordinator's call, active year 1062, second tradition's span), against CENSUS and PAT l.1040-1041, 1094-1096, 1683-1686. The Rimbert Library item: WAITZ ends at l.5422-5423, in chapter 23, and the records' absent detail agrees. The Turholt correction: WAITZ l.1832.

---

## Not-taken items in my part

- **R2-M7 (Anskar, Adam's time).** Leaving it was acceptable at the time, since the only fix on offer cost two words over the cap. R3-M6 gives a 405-word version, so it should now be taken.
- **R1 Part C.** Nothing else was left untaken. C-K-M8 was completed in round 2, and the brief now carries Nestor's identifier.

---

## Files and ranges opened

- CROSS l.4380-4390, 4494-4680 (grep "Nestor"), 11740-11880, 12520-12560, 12640-12700, 12845-12862, 13331-13402, 15045-15060, 15090-15110 (grep "Sylvester", "6624").
- PAT l.104-114, 160-175, 378-384, 1028-1042, 1160-1252, 1312-1320, 1648-1675, 2086-2100, 2171, 3584-3660, 9098-9205, 15185-15192 (grep "чадо", "Василев", "Курск", "латин", "Ефрем", "Изяслав", "1462", "1406").
- MOUR l.1612-1622.
- ROB l.796-826, 1140-1172, 1288-1300, 2135-2226, 2392-2402, 2635-2705, 3800-3856, 4225-4285, 4292-4362 (grep "Birka", "assembly"), 5548-5562 (grep "Klippel").
- WAITZ l.1828-1834, 4521-4560, 4608-4634, 5395-5423.
- ADAM l.6198-6204, 6774-6790, 6822-6828 (grep "Flandr", "Novae Corbeiae").
- OP l.852-880.
- CENSUS: `eras`; every movement's `name`, `era`, `laneLabel`, `dates` for the traditions on the era 4 major cards; every era 4 `kind: "person"` row; the `people` lists searched for the seven names.
- Era 4 batch 1-9 READMEs (major lines); the `tradition` of every era 4 major card (batches 1, 2, 4, 5, 7).
- OG l.2177-2190, 3482-3522. DL l.2016-2045, l.3163 (grep "batch 9", "Best-known dated act"). Rescore.md l.81-82, 100, 124-125, 146.
- Batch 9: the three briefs, cards, audio scripts and records entries; README; all seven briefs and audio scripts for the counts and the audio check; R1_changes.md, R2_review.md (Part 2), R2_changes.md; `git diff 83d3b04e 9c58b577` for the batch folder and OG.
- Mechanical: `engine.m1.gates.grade_text` and `wc -w` on all seven briefs; the audio rebuild compare; a quotation script over my three briefs and cards.
