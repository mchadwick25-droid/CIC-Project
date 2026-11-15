# R2 review: era 4 batch 9

Round 2, a targeted recheck of the round 1 fixes, by two fresh Opus agents that had not seen the drafting or round 1, at full effort. Part 1 covers John of Damascus, Theodore the Studite, Cyril and Methodius and Clement of Ohrid. Part 2 covers Antony and Theodosius of the Kyiv Caves, Anskar, Rimbert and the rest of the README. Each part is given as its reviewer wrote it.

## R2 review, Part 1: john-of-damascus, theodore-the-studite, cyril-and-methodius, clement-of-ohrid, and the README on these four

A targeted recheck by a fresh reviewer, at full effort. I edited no repo file. I read every round 1 finding for these four (R1_review.md Parts A and B), R1_changes.md, and `git diff c6bd9d01 HEAD` for the batch. Then I reopened each cited source line in context and read every changed sentence as new text.

## Mechanical checks (re-run)

| Brief | Words | FK | Flesch | Audio script |
|---|---|---|---|---|
| john-of-damascus | 405 | 7.24 | 68.61 | exact match |
| theodore-the-studite | 404 | 7.21 | 68.70 | exact match |
| cyril-and-methodius | 406 | 7.05 | 69.29 | exact match |
| clement-of-ohrid | 366 | 6.07 | 73.06 | exact match |

- All four pass `engine.m1.gates.grade_text`. All are within length: majors and pairs at most about 405, Clement about 365.
- Audio: each `audio/<id>.audio.txt` equals its brief, with `[calmly] ` at the start and `[warmly] ` at the start of the last paragraph only. I checked this by script.
- Quotations, checked verbatim against the files:
  - "Anathema to Mansur, who has an evil name and Saracen opinions!" matches NPNF14 l.39468-39469.
  - "we fall down and worship not the material but that which is imaged." matches NPNF9 l.36281-36282, where the file runs on with a colon.
  - "copied it out, and established it in his own monastery." matches CROSS l.11871-11872, where the file runs on.
  - "The Slavs rejoiced to hear the greatness of God extolled in their native tongue." matches CROSS l.7899-7900.
  - All four pass.
- Long sentences: Theodore has three of 26 words. Two are unchanged from round 1, and the Testament sentence is R2-M3 below. John has one of 26 words (the forged letter), unchanged. None is over 26.
- Batch-wide file hygiene (R2-M1 below): round 1 removed the trailing newline from every `*.card.json` and from `records.json`. Batch 8 cards end in a newline. All the files still parse as JSON.

With my proposed brief changes applied together, I scored the results on scratch copies:
- Theodore: 407 words, FK 7.08, Flesch 68.96.
- Cyril and Methodius: 406 words, FK 7.11, Flesch 68.87.
- Clement: 369 words, FK 6.10, Flesch 73.03.

---

## john-of-damascus

**Verdict: passes with minor fixes.** A-B1 is applied and correct. PG100 l.92459-92460 opens the speech ("ex imo suspirans Pater ait"). The John passage at l.92531-92537 falls inside it. The speech closes at l.92547-92549 ("His pluribusque aliis ... sermonibus a beatissimo Stephano dictis"). So "Stephen the Younger tells the monks ... he says" now gives the words to the right speaker, in the brief, the card and the records. A-M1, A-M2 and A-M4 to A-M8 are applied, and each matches its source:
- A-M1: THEO l.75291 has "Mansur aviti nominis".
- A-M2: "the bibliographer" and "the scholar" are added, and "the emperor" replaces the ambiguous "Leo".
- A-M5: PG94 l.37215 has "Damasci natalis".
- A-M6: PG94 l.4596-4599 has "ipso fatente Suida".
- A-M7: THEO l.75282-75284 has "ob eloquii sanctitatisque ... gratiam".
- A-M8: PG94 l.32111-32113 has "anno Christi 750. quo Germanus solio detrusus est".
- A-M10: PG97 l.497-499 has "ita ejus testimonium eludit ut orationem illam posse suppositam esse dicat. Quae quam levia sint facile apparet".

A-M3 matches PG94 l.31104-31109: "monasticae vitae nomen dedisse, atque in clerum Hierosolymitanum accensitum fuisse, sub primis temporibus Leonis Isauri imperatoris".

**A-M9 not taken (acceptable).** The brief drops Salmond's condition that the image brings the passion back to mind. The quoted words stand as written, and the compression adds nothing the source lacks. The brief is at 405 words.

**A-M11 and A-M13 (README) are applied. A-M12 is not done. See R2-B1.**

**R2-M2 (card `uncertain[2]`: Theophanes' word widened, and Le Quien made to agree with a reading he does not give).**
- Text: "Theophanes says Mansur was his grandfather's name, and Fabricius and Le Quien agree."
- Source:
  - Theophanes, THEO l.75291 (Goar): "et Mansur aviti nominis". Anastasius, l.121038: "pro Mansur, quod est avitum nomen ejus". "Avitum" means ancestral. Only Fabricius reads it as the grandfather's: PG94 l.570-571, "Assentior tamen Theophani, qui ... Mansur ... quod avus ejus ita diceretur".
  - Le Quien, PG94 l.30617-30619, says the family's name: "quod ejus progenitoribus ac toti familiae proprium fuit".
  - The brief and `otherNames` both say "his family's name". The card should not narrow Theophanes' word here.
- Replacement: "Theophanes calls Mansur an ancestral name; Fabricius reads it as his grandfather's name, and Le Quien as the family's own name."
- Records: in the contested claim "Mansur: family name or insult", change "Fabricius agrees" to "Fabricius reads it as the grandfather's name".

**R2-M3 is in Theodore. R2-M4 (card `dates`: process language on a participant card).**
- Text: "the held scan prints the second year as 750, but his clause ties it to Germanus's fall."
- "The held scan" is the build's own vocabulary, in the status-announcement register (Style Guide 1.11). A listener or reader does not know what it is.
- Source: PG94 l.32111-32113, "Quod quidem praestitit anno Christi 750. quo Germanus solio detrusus est a Leone".
- Replacement: "Le Quien's printed text reads 750 for the second, but ties it to the year Leo drove Germanus out."

---

## theodore-the-studite

**Verdict: one blocking finding (R2-B2). Otherwise passes with minor fixes.** T-B1's facts are right, but its wording needs a writing fix (R2-M3). The other round 1 fixes check out:
- T-M1: PG99 l.18788-18789, "elocutio ... semper ... differt; sed tamen res narratae vix variant".
- T-M2: l.20523-20527, "Simulans enim se ad calidas aquas ... fruendas pergere, Prusam ... venit".
- T-M3: CROSS l.11866-11872.
- T-M5: l.27066-27067 and l.27097, "Tempus est ut loquatur, et non sileat qui loqui quoquomodo potest, cum instet haeresis adversus ... veritatem latrans".
- T-M7: l.3743-3753.
- The steward Joseph matches l.5639-5640 and l.20305-20306 ("Josephus quidam presbyter, et ejusdem sanctissimae Magnae Ecclesiae oeconomus").
- The brother Joseph is the archbishop of Thessalonica at l.5655.

**T-M4 (the brief keeps "the restored priest Joseph") is acceptable.** Joseph was both priest and steward (l.20305-20306). The card names the office he was restored to. The brief and the card are separate texts.

**R2-B2 (card `uncertain[2]` and the records side: Fabricius's "death" changed to "fall").**
- Text (card): "and Fabricius puts it the year after Constantine VI's fall." Records: "Fabricius: the year after Constantine VI's fall (PG99 l.358-359)".
- Source: PG99 l.358-359, "sed mox anno proximo post Constantini mortem magno cum honore revocatus ab Irene, et abbas Studio praefectus fuit". Fabricius says death, not fall.
- This error came in with round 1's own fix wording (T-M8 proposed "fall"). A fall and a death are different events, and Fabricius names the death.
- Replacement (card): "The Sirmond chronology gives 798, and Fabricius puts it the year after Constantine VI's death. Philipp Meyer gives 789, but cites the same chronology."
- Replacement (records side): "Fabricius: the year after Constantine VI's death, \"anno proximo post Constantini mortem\" (PG99 l.358-359)".

**R2-M3 (brief para 5 and card `keyWorks[1]`: T-B1's new wording has a loose "that").**
- Brief text: "In his Testament Theodore told the abbot after him to own no slave, a man made in God's image; that, like marriage, was for laymen only."
- Card text: "own no slave, a man made in God's image, since that, like marriage, is for laymen only".
- Heard aloud, "that" follows "a man made in God's image", so it can sound as if the man, and not owning him, is "for laymen only". The sentence is also 26 words.
- Source: PG99 l.155226-155230, "Non possidebis servum, nec tuos in usus, nec proprii monasterii, nec denique ad agros, hominem qui ad Dei imaginem factus est: hoc enim solis saecularibus concessum est, sicut nuptiae."
- Replacement (brief, +3 words): "In his Testament Theodore told the abbot after him to own no slave, a man made in God's image. Only lay people might own one, as only they might marry."
- Replacement (card): "own no slave, a man made in God's image, since owning slaves, like marriage, is allowed only to lay people;" Keep the rest of the field as it is.
- Budget trim, para 6 (-1): "The third came when he stood against the emperor Leo V's ban on images." becomes "The third came when he opposed the emperor Leo V's ban on images."
- Result: 407 words, FK 7.08, Flesch 68.96.

**R2-M5 (card `legacy.traces[1]`: the T-M6 wording leaves "the first five" with no noun, and names "the abbot" twice).**
- Text: "Philipp Meyer says Athanasios the Athonite took his commands to the abbot, with slight changes, from the part of Theodore's Testament addressed to the abbot, the first five almost word for word."
- Source: MEYER l.1042-1047, "Diese hat Athanasios mit geringen Abänderungen aus dem Abschnitt ἐντολαὶ τῷ καθηγουμένῳ der διαθήκη des Studiten übernommen. Und zwar stimmen Can. 1—5 des Theodoros fast wörtlich mit den Eingangsworten bei Athanasios." Meyer means Theodore's canons 1 to 5 and Athanasios's opening words.
- Replacement: "Philipp Meyer says Athanasios the Athonite took his commands to the abbot, with slight changes, from Theodore's Testament, and that Theodore's first five commands match Athanasios's opening words almost word for word."

**R2-M6 (card `legacy.traces[2]`: "a Joseph" hides an identification that Fabricius reports).**
- Text: "Fabricius, quoting Nikephoros Kallistos, says Theodore and a Joseph, both of Stoudios, wrote Lenten canons for their monastery."
- Source: PG99 l.832, "Theodorum Studitam et Josephum (episcopum Thessalonicensem), ejus fratrem, laudat Codinus". Then l.836, from Nikephoros Kallistos: "Theodorus et Josephus Studitae ... proprio Studiorum monasterio tradiderunt". Fabricius, after Codinus, takes this Joseph to be Theodore's brother.
- T-M4's "a Joseph" avoids a mix-up with the steward. But it drops a held identification and leaves a bare "a Joseph" with no context.
- Replacement: "Fabricius, quoting Nikephoros Kallistos, says Theodore and Joseph, both of Stoudios, wrote Lenten canons for their monastery; after Codinus, he takes this Joseph to be Theodore's brother."

**R2-M7 (card `uncertain[0]`: Mai's "vix" lost).**
- Text: "Mai says the two tell the same events in different words."
- Source: PG99 l.18788-18789, "Proemium quidem totum novum est: elocutio in reliquis semper ab illa edita Vita differt; sed tamen res narratae vix variant." The events hardly vary. Mai does not say they are the same, and he says the prologue is wholly new.
- Replacement: "Mai says the prologue is wholly new and the wording always differs, but the events hardly vary."

---

## cyril-and-methodius

**Verdict: one blocking finding (R2-B3). Otherwise passes with minor fixes.**

- **C-B1** is applied and correct. THEINER l.99-104 has the dedication to Strossmayer, "BOSNENSI SEU DIACOVENSI ET SIRMIENSI EPISCOPO". l.157-160 has "solemnia in memoriam millenariam ... quam hoc anno Ecclesia celebrat, vix opportunius et sanctius peragere ... potuisti".
- **C-B2** is applied and correct. LUTZOW l.1418-1422: "The German governors seized the Archbishop Methodius, and delivered him as prisoner to his enemies the German bishops", in its 870 context (l.1406-1407). R2-M10 below makes one small correction.
- **C-B3** is applied. GIN l.13641-13664 has "vilescere fecit cuncto populo ex parte missas". The hedge is back. R2-M9 below fixes the phrasing.
- The other fixes check out:
  - C-M2: GIN l.1589-1592, "Machwerk eines griechischen Schismatikers".
  - C-M3: GIN l.13797-13800, "Unde iam litteris nostris, per Paulum episcopum Anconitanum tibi directis prohibuimus". The 879 letter restates the ban's terms, so "repeated" is fair.
  - C-M4: GIN l.11422-11424 and l.12220-12221.
  - C-M5: GIN l.13976-13979, "evangelium latine legatur et postmodum sclavinica lingua translatum ... adnuncietur".
  - C-M6: GIN l.11490-11492, "ad monasterium suum reduceret".
  - C-M7: GIN l.12320-12322.
  - C-M8.
  - C-M9: GIN l.12538-12539. Ginzel's l.6198-6206 restores "sexies" from Šafařík's edition and the manuscripts.
  - C-M11.

**C-M10 not taken (acceptable).** The brief says only "A Life of Methodius says God revealed the Slavonic letters", with no time attached, so it says nothing false about when.

**R2-B3 (brief para 2: C-M1's new wording gives Gauderich the Bollandists' time).**
- Text: "He trusts it, and follows the Bollandists in tracing it to Gauderich of Velletri, a bishop of their own time."
- The nearest plural before "their" is "the Bollandists". Heard aloud, the sentence says Gauderich lived in the Bollandists' time, the seventeenth century. The pre-round-1 text had "the brothers' own time". The fix wording brought the error in.
- Source: GIN l.1457-1460, "dass dieser Bericht von dem Bischofe Gauderich oder Gaudentius von Velletri herrühre, der ein Zeitgenosse der Slawenapostel" (a contemporary of the Slav apostles).
- Replacement (+1 word): "He trusts it, and follows the Bollandists in tracing it to Gauderich of Velletri, a bishop of the brothers' own time."

**R2-M8 (brief para 5: C-M6's new clause has no verb for its condition).**
- Text: "Methodius asked to take his body back to their monastery, as their mother had tearfully begged if one died abroad."
- "had tearfully begged if one died abroad" leaves out what she begged.
- Source: GIN l.11490-11492, "mater cum multis lacrymis obtestata est, ut si aliquem ex nobis, antequam reverteremur, obiisse contingeret, defunctum fratrem frater vivens ad monasterium suum reduceret".
- Replacement (+1): "Methodius asked to take his body back to their monastery, as their mother had tearfully begged, should one die abroad."

**R2-M9 (brief para 6: C-B3's "in part" set off by commas reads choppily).**
- Text: "With newly invented Slavonic letters, it says, he cheapened the Latin Masses, in part, in the eyes of all the people."
- Source: GIN l.13641-13664, "vilescere fecit cuncto populo ex parte missas".
- Replacement (-1): "With newly invented Slavonic letters, it says, he partly cheapened the Latin Masses in the eyes of all the people."
- With R2-B3, R2-M8 and R2-M9 applied: 406 words, FK 7.11, Flesch 68.87.

**R2-M10 (card `uncertain[5]`, the prison: "his bishops" where the Life says "all the bishops").**
- Text: "The Life of Methodius says the enemy of the Moravian king and all his bishops sent him to Swabia".
- Source: GIN l.12326-12327, "incitavit cor hostis Moravici regis cum omnibus episcopis contra nos". The Life says "all the bishops" and does not make them anyone's.
- Replacement: "The Life of Methodius says the enemy of the Moravian king and all the bishops sent him to Swabia and held him two and a half years."

**R2-M11 (card `uncertain[4]` now contradicts the C-M9 fix in `dates`).**
- Text: "The day Methodius died. The Life gives 6 April 885."
- The card's `dates` now says, correctly, that the Life gives the year 6393 from the creation and that Ginzel works it out as 885 (GIN l.12538-12539, l.6198-6206).
- Replacement: "The day Methodius died. The Life gives 6 April, in the year Ginzel works out as 885. Ginzel reports that Wattenbach thought a death on so high a feast suspicious, and defends the date."

**R2-M12 (card `uncertain[0]`: C-M1's new clause is awkward).**
- Text: "which the Bollandists, as Ginzel follows them, think very probably the work of Gauderich of Velletri".
- Source: GIN l.1456-1459, "machen es sehr wahrscheinlich".
- Replacement: "which the Bollandists, and Ginzel after them, think very probably the work of Gauderich of Velletri".

---

## clement-of-ohrid

**Verdict: passes with minor fixes.**

- **K-B1** is applied and correct. PG111 l.243-245: "ANONYMUS. Vita S. Clementis ... (exstat tom. CXXVI, in appendice ad Theophylactum, cui a nonnullis tribuitur)". l.36942-36948: "CIRCA MEDIUM SECULUM X".
- **K-B2** is applied.
- **K-B3** is applied and correct. PG126 l.100258-100267 dates the burial ("repositum est, Julii mensis vigesimo septimo die ... anno sexies millesimo quadringentesimo vigesimo quarto"). PG126 l.96726 and GIN l.1680 give 916 as the year of death. 6424 from the creation runs from September 915 to August 916, so 27 July is in 916.
- The other fixes check out:
  - K-M1: PG126 l.96785-96788 and l.96734, "Justinianae primae totiusque Bulgariae".
  - K-M3: GIN l.1690-1691, "additum esse videtur".
  - K-M4.
  - K-M5: PG126 l.99241-99243 and l.99268-99270.
  - K-M6.
  - K-M7.
  - K-M8: l.98417-98419, "canticis tertiae horae decantatis, psalmorum prosequebantur carmen".
  - K-M9.

**K-M2 is only partly fixed (R2-M13).**

**R2-M13 (brief para 5: the monastery still sounds later than the bishopric).**
- Text: "At Ohrid, while Boris still lived, he built a monastery, and a church that later became the archbishop's seat."
- The sentence still follows the bishopric and the sermons. "While Boris still lived" does not settle the order, because Boris was alive after Symeon made Clement bishop. The Life's point is "before he took the see".
- Source: PG126 l.99596-99600, "Deposuerat haec omnia in monasterio, quod in Achride construxerat, adhuc superstite beatissimo Borise, priusquam Velitzae episcopatum suscepisset". l.99604-99606: "proprium aedificare monasterium, cui etiam alteram adjecit ecclesiam, quae postea archiepiscopatus sedes constituta est". The Life gives no time for the church.
- Replacement (+1): "He had built a monastery at Ohrid before he became bishop, and added a church that later became the archbishop's seat." The card and records keep "while Boris still lived".

**R2-M14 (brief para 2: one "it" for two things in K-B1's new sentence).**
- Text: "Migne's editors leave it to the reader in one volume, and in another date it to about the middle of the tenth century."
- The first "it" is the question of who wrote the Life. The second is the Life itself.
- Source: PG111 l.36942-36948.
- Replacement (+1): "Migne's editors leave it to the reader in one volume, and in another date the Life to about the middle of the tenth century."
- With R2-M13 and R2-M14 applied: 369 words, FK 6.10, Flesch 73.03. That is within "about 365".

**R2-M15 (card `legacy.traces[0]`: K-M5's sentence parses badly).**
- Text: "The Life says he had 3,500 picked pupils, ordained readers, subdeacons, deacons and priests from among them, and in each district gave orders to 300 of them."
- "pupils, ordained readers" reads as "pupils who were ordained readers", and the sentence then changes its subject.
- Source: PG126 l.99241-99243, "Habens quosdam ex aliis delectos in unaquaque dioecesi non paucos, ad tria enim millia et quingentos numerabantur". l.99268-99270: "Ex illis lectores, subdiaconos, diaconos, et presbyteros ordinat. In unaquaque dioecesi trecentis jussa dabat discipulis".
- Replacement: "The Life says he had 3,500 picked pupils. From them he ordained readers, subdeacons, deacons and priests, and in each district he gave orders to 300 of them."

**R2-M16 (brief para 1: "the Third Hour" is not explained; optional).**
- Text: "They sang the Third Hour's hymns, then the psalms."
- A general listener does not know that the Third Hour is one of the fixed hours of prayer.
- Replacement, if the budget allows (+3, which brings the brief to 372 with R2-M13 and R2-M14): "They sang the hymns of the Third Hour of prayer, then the psalms."

**A note on R1_changes.md, not a finding on the profile.** It says the trims "who longed to talk with them" and "gave him houses at Devol" were cut. The brief still has both. Only "daily" and "and places to rest at Ohrid" were cut. The audit trail is slightly wrong, and the brief is correct.

---

## README statements on these four

**R2-B1 (README, "John of Damascus, the live entry" and "The river counts change": an Open-Gaps entry the README cites does not exist).**
- Text: "the difference is logged in Open-Gaps, "Era 4 Who batch 9" (2026-11-15), for the census fix." The river-count paragraph makes the same claim.
- Check: I searched `Build/Ministry/Features/Church-Family-Tree/Open-Gaps.md` for "batch 9", "batch9" and "Damasc". The only hits are the era 4 scan's WANTED line (l.2150) and the batch plan line (l.3163). No entry "Era 4 Who batch 9" exists. R1_changes says the entry "is written with this batch", but it is not in the tree at HEAD (83d3b04e).
- CLAUDE.md requires every known gap to be in the tracking file. A README that says a gap is logged when it is not breaks that rule. This repeats A-M12, which is still open.
- Fix: write the Open-Gaps entry "Era 4 Who batch 9" (2026-11-15) before the batch merges. It should carry the John census-year difference (census 730, against Le Quien's 730 for the second speech, printed 750, and Fabricius's post-743 for the Dialectica) and the river re-count. Or, until it exists, change both README sentences to "is to be logged in Open-Gaps".

**R2-M17 (README, "Majors and lengths": the range is stale).**
- Text: "Their briefs run 404 to 405 words".
- Cyril and Methodius is at 406.
- Replacement: "Their briefs run 404 to 406 words".

**R2-M18 (README, "Who the sources are", Cyril and Methodius: terms not brought in line with the brief and card).**
- Text: "The Italian Legend, which Johann Ginzel follows the Bollandists in tracing to Gauderich of Velletri; the Life of Methodius, which Ernst Dümmler takes as a pupil's and Ginzel calls a Greek schismatic's work".
- Source: GIN l.1456-1459, "sehr wahrscheinlich"; l.1589-1592, "Machwerk".
- Replacement: "The Italian Legend, which the Bollandists, and Ginzel after them, think very probably Gauderich of Velletri's; the Life of Methodius, which Ernst Dümmler takes as a pupil's and Ginzel, who writes against the Greek schism, calls a schismatic's concoction".

The README's other statements on these four check out:
- The two census rows and the quotation (A-M11).
- The 750 note (A-M13).
- The Theodore Lives, now "hardly differ in what they tell".
- Clement and PG 111, the Monitum correction (PG126 l.96731-96745, "Sed judicium penes Lectorem sit"), and the burial-date correction.
- The Panteleimon note.
- Mark's Clement ruling, as relayed.

**R2-M1 (batch-wide hygiene).** All seven `*.card.json` files and `records.json` now end without a final newline. They ended with one before round 1, and batch 8's cards do. Restore the trailing newline when the fixes are written.

---

## Summary

- Blocking: R2-B1 (README: the Open-Gaps entry it cites is missing), R2-B2 (Theodore: Fabricius's "mortem" given as "fall"), and R2-B3 (Cyril and Methodius: "their own time" makes Gauderich a contemporary of the Bollandists). R2-B2 and R2-B3 came in with round 1's own fix wording.
- Minor: R2-M1 to R2-M18. By profile:
  - Batch-wide: R2-M1.
  - John: R2-M2 and R2-M4.
  - Theodore: R2-M3 and R2-M5 to R2-M7.
  - Cyril and Methodius: R2-M8 to R2-M12.
  - Clement: R2-M13 to R2-M16. R2-M16 is optional.
  - README: R2-M17 and R2-M18.

## Files and ranges opened

- CLAUDE.md (in context); `Build/Ministry/Features/Church-Family-Tree/Who_Profile_Pattern.md` (whole); `Build/Ministry/Operations/Audits/2026-11-15_who-profiles-era4-batch9/R1_review.md` l.1-450; `R1_changes.md` (whole).
- Batch: `README.md`; the brief, card and audio files for all four ids; `records.json` (diff and entries for the four); `git diff c6bd9d01 HEAD` for the batch folder. Batch 8 cards (trailing bytes only).
- `Build/Ministry/Features/Church-Family-Tree/Open-Gaps.md` (grep for batch 9, batch9, Damasc; tail); `Decision-Log.md` (grep).
- cic/texts:
  - `nikephoros-cp_opera-with-vita-stephani-iunioris-pg100-grc-lat_migne1860.txt` l.92455-92465, 92495-92552.
  - `john-damascus_opera-omnia-t1-with-vita-pg94-grc-lat_migne1860.txt` l.550-580, 612-622, 4584-4600, 7262-7296, 31098-31112, 32105-32116, 37212-37217.
  - `theophanes-confessor_chronographia-pg108-grc-lat_migne1863.txt` l.75270-75292, 121034-121042; grep Mansur.
  - `theodore-abu-qurrah_opuscula-with-andrew-crete-malalas-pg97-grc-lat_migne1860.txt` l.490-500; grep Hodius.
  - `npnf214_seven-ecumenical-councils.xml` l.39468-39469.
  - `npnf209_hilary-poitiers-john-damascus.xml` l.36275-36283.
  - `theodore-studite_opera-omnia-pg99-grc-lat_migne1860.txt` l.355-362, 826-840, 3590-3606, 3736-3755, 5562-5567, 5630-5645, 5710-5728, 18780-18792, 20303-20310, 20515-20530, 27060-27075, 155215-155245; grep Josephus, presbyter, "veritatem latrans".
  - `athos-monasteries_haupturkunden-fur-die-geschichte-der-athoskloster-ger-grc_meyer1894.txt` l.1038-1050.
  - `russian-primary-chronicle_cross1930.txt` l.7899-7902, 11862-11878.
  - `ginzel_geschichte-der-slawenapostel-cyrill-und-method-deu-lat_1861.txt` l.1452-1470, 1676-1692, 6185-6206, 11395-11426, 11484-11492, 12318-12362, 12532-12542, 13780-13810, 13960-13990.
  - `lutzow_bohemia-historical-sketch_1920.txt` l.1405-1432.
  - `theiner_vetera-monumenta-slavorum-meridionalium-v1-lat_1863.txt` l.97-106, 120-127, 150-162.
  - `theophylact-ohrid_opera-t4-with-vita-clementis-pg126-grc-lat_migne1864.txt` l.96718-96750, 99236-99275, 99594-99608, 100225-100268.
  - `nicholas-mystikos_epistolae-with-eutychius-alexandrinus-pg111-grc-lat_migne1863.txt` l.241-247, 36940-36948.
- Scripts: `engine.m1.gates.grade_text` and word and sentence counts on the four briefs and on scratch copies with the proposed changes; an audio-versus-brief comparison; JSON parse and trailing-byte checks.

---

## R2 review, era 4 batch 9: Part 2 (Kyiv pair, Anskar, Rimbert, README)

Targeted recheck of round 1 Part C, at full effort. No repo file was edited. Suggested brief replacements were test-applied to scratch copies only (`r2p2/` in the scratchpad) to check word counts and grades.

**Abbreviations.** CROSS = `cic/texts/russian-primary-chronicle_cross1930.txt`; PAT = `cic/texts/kievan-caves-paterik_paterik-kievskago-pecherskago-monastyria-chu_abramovich1911.txt`; MOUR = `cic/texts/mouravieff_history-of-the-church-of-russia_blackmore1842.txt`; ROB = `cic/texts/rimbert_anskar-the-apostle-of-the-north_robinson1921.txt`; WAITZ = `cic/texts/rimbert_vita-anskarii-accedit-vita-rimberti-lat_waitz1884.txt`; ADAM = `cic/texts/adam-bremen_gesta-hammaburgensis-ecclesiae-pontificum-lat_schmeidler1917.txt`; ANNBERT = `cic/texts/prudentius-troyes_annales-bertiniani_waitz1883.txt`; OP = `cic/texts/olavus-petri_samlade-skrifter-v1-swe_hesselman1914.txt`; PG111 = `cic/texts/nicholas-mystikos_epistolae-with-eutychius-alexandrinus-pg111-grc-lat_migne1863.txt`; PG126 = `cic/texts/theophylact-ohrid_opera-t4-with-vita-clementis-pg126-grc-lat_migne1864.txt`; CENSUS = `cic-website/data/world-census.json`.

## Re-run checks

| Brief | Words | FK | Flesch | Pass |
|---|---|---|---|---|
| antony-and-theodosius-of-the-kyiv-caves | 405 | 5.77 | 73.46 | yes |
| anskar | 405 | 6.09 | 77.84 | yes |
| rimbert | 365 | 5.97 | 80.32 | yes |

- **Audio.** All seven `audio/<id>.audio.txt` equal their briefs with `[calmly] ` at the start and `[warmly] ` at the start of the last paragraph only (scripted paragraph rebuild, exact match, two tags each).
- **Quotations.** Every quotation in my three briefs and cards matches its file, OCR noise allowed: CROSS l.11777 ("Oh Lord, strengthen me in this place"), l.11859-11861 ("Who among you ... your prior", running head and stray quote mark inside), l.12665-12666 ("Change not ..."), l.11843-11846 ("Many monasteries ..."); ROB l.2651-2653 ("cloakf"), l.4325-4328 (the old man), l.5557-5560 ("Were I worthy ..."), l.3747-3748 (the decree), l.240-243 ("the inspiring example ...").
- **Not-taken items in my part.** C-K-M8 was applied on the card only; the brief still says "Nestor's Life of Theodosius" with no identifier, inside a 26-word sentence. Leaving it is not acceptable now that a cut exists that pays for it (R2-M2).

---

## antony-and-theodosius-of-the-kyiv-caves

**Verdict: two blocking findings (R2-B1, R2-B2), both introduced by round 1's fix wording. Otherwise the round 1 fixes hold, with minor fixes.** C-K1's new `uncertain` item and contested claim are in place; C-K-M1, C-K-M2, C-K-M5 and C-K-M7 read right against the sources.

**R2-B1 (card `knownFor`, new in round 1: a contested point told as settled).**
- Text: "Antony, made a monk on Mount Athos, lived in a cave on a hill outside the city, and the brothers who gathered to him chose Theodosius as prior on his word."
- "On his word" is the Chronicle's account. Nestor's Life has the brothers choose Theodosius themselves and then tell Antony, who blessed him. Cross sets out the difference. The card's `uncertain` list and the records do not carry it, so the card's headline tells one side as settled. It also skips Barlaam, so "the brothers who gathered to him chose Theodosius" reads as the first choice of prior.
- Sources: CROSS l.11849-11852: "the brethren held a council, and then once more visited the ancient Antonius with the request that he should designate them a new prior." PAT l.2093-2097 (Life, ch. 16): "братия ... събравшеся, изволениемь всѣхъ, възвѣстиша преподобному Антонию, блаженнаго отца нашего Феодосиа игуменомь себѣ нарекоша ... Преподобный же призвавъ святого Феодосиа, благословивъ его на игуменьство" (OCR-normalised). CROSS l.4635-4637: "the brethren themselves, after unanimously choosing Theodosius as Barlaam's successor, notified Antonius of their action."
- Fix, `knownFor`: "The founders of the Caves monastery of Kyiv. Antony, made a monk on Mount Athos, lived in a cave on a hill outside the city. Theodosius became prior of the brothers who gathered there and gave the house the rule of the Studion monastery of Constantinople."
- Fix, `uncertain`, a new item after "When Theodosius became a monk": "Who chose Theodosius as prior. The Chronicle says the brothers asked Antony for a new prior and he named Theodosius. Nestor's Life says the brothers chose him themselves and told Antony, who blessed him. S. H. Cross points out the difference."
- Fix, records `contested_claims`: add `{"claim": "Who chose Theodosius as prior", "sides": ["Chronicle: the brothers asked Antony, who named Theodosius (CROSS l.11849-11862)", "Nestor's Life: the brothers chose him and told Antony, who blessed him (PAT l.2091-2097); Cross notes the difference (CROSS l.4635-4637)"]}`.
- The brief's para 5 tells the Chronicle's version under "The Chronicle says", so it is attributed. I accept it there, as round 1 accepted "by Nestor's account" for the move above ground.

**R2-B2 (brief para 11, new in round 1: "the two princes" names the wrong pair).**
- Text: "In 1073 Svyatoslav drove his brother Izyaslav out of Kyiv. Nestor says the two princes invited Theodosius to dinner".
- The only two princes the listener has just heard are Svyatoslav and Izyaslav, so the sentence says Izyaslav, the man driven out, invited Theodosius. The two in Nestor are the brothers who drove him out. The Chronicle names them as Svyatoslav and Vsevolod. The next sentence's "the prince's brother" is then ambiguous too.
- Sources: PAT l.3586-3590: "двоима братома брань сътворити на единаго старийшаго ихъ брата ... князя Изяслава ... И онѣмь пришедшимь въ градъ той, посылають же по блаженнаго отца нашего Феодосиа, зовуще того прийти к нимъ на обѣдъ". CROSS l.12527-12528: "Svyatoslav and Vsevolod united against Izyaslav. The latter left Kiev". CROSS l.12530-12531: "Svyatoslav was the instigator of his brother's expulsion".
- Fix: "In 1073 Svyatoslav and Vsevolod drove their brother Izyaslav out of Kyiv. Nestor says the two princes invited Theodosius to dinner, and Theodosius would not go to what he called Jezebel's table. He wrote to Svyatoslav that his brother's blood cried out to God against him, as Abel's had against Cain." (The letter goes to the one on the throne, PAT l.3612-3622, "единому сѣдшу на столѣ ... епистолию велику зѣло".) Same fix in records: "Svyatoslav and Vsevolod drive out Izyaslav (6581/1073)".

**R2-M1 (brief para 9, new in round 1: "sent him away" reverses Svyatoslav's part).**
- Text: "Later Izyaslav grew angry with Antony, and Prince Svyatoslav sent him away by night to Chernigov".
- Source: CROSS l.12855-12857: "Izyaslav returned from Poland, and was angry with Antonius on account of Vseslav, so that Svyatoslav caused Antonius to escape by night to Chernigov." Svyatoslav protected him; "sent him away" sounds like a banishment.
- Fix: "Later Izyaslav grew angry with Antony, and Prince Svyatoslav helped him escape by night to Chernigov, where he dug another cave." Records: change the gloss "(Svyatoslav sent him away)" to "(Svyatoslav helped him escape)".

**R2-M2 (brief paras 3 and 5: round 1's length trim shifted a meaning, and C-K-M8 left half done).**
- Para 5 text: "His prior sent him home to Rus, as an example to other monks." Source: CROSS l.11766-11767: "he bade him return to Rus ... that many other monks might spring from his example." The source means more men would become monks through him; "an example to other monks" means a model for monks already there.
- Para 3 text: "Their story is told in the Russian Primary Chronicle, which Sylvester, prior of Saint Michael's, says he wrote in 1116, and in Nestor's Life of Theodosius." This is 26 words, and Nestor has no identifier (checklist 8; PAT l.1249-1250: "Списано Нестеромъ, мнихомъ того-же Печерьскаго монастыря").
- Fix, para 3: "Their story is told in the Russian Primary Chronicle, which Sylvester, prior of Saint Michael's, says he wrote in 1116. Nestor, a monk of the Caves, tells it in his Life of Theodosius."
- Fix, para 5: "His prior sent him home to Rus, so that others might follow his example."
- To pay for both, cut para 9's "No source used here gives the year he died." The card says it twice (`dates` and `uncertain[3]`).
- With R2-B2 and R2-M1, the brief tested at **405 words, FK 5.89, Flesch 72.61** (scratch copy `r2p2/kyiv.txt`). If the coordinator would rather keep the honest limit in the brief, apply R2-B2, R2-M1 and the para 5 fix alone: 407 words.

**R2-M3 (card `uncertain`, "Who built the monastery above ground": Nestor's site is not Izyaslav's hill).**
- Text: "Nestor's Life says Theodosius built them and moved the brothers there in 1062."
- "Them" points back to the church, cells and palisade on the hill Izyaslav gave. Nestor has Theodosius find a new site near the cave. Sources: PAT l.2158-2164: "Тогда бо великый Феодосие обрѣте мѣсто чисто, недалече отъ печеры ... възгради церковь на мѣстѣ томь ... и оградивъ, поставивъ кѣлии многы, и тогда преселися отъ печеры съ братиею на мѣсто то, в лѣто 6570" (OCR-normalised). CROSS l.4637-4639: "selected a location not far from the old crypt, where he built a large church".
- Fix: "Who built the monastery above ground. The Chronicle says the brothers under Barlaam, the first prior, built the church, cells and palisade on the hill Prince Izyaslav gave them. Nestor's Life says Theodosius found a site near the cave, built a church, a fence and many cells there, and moved the brothers in 1062. S. H. Cross points out the difference."

**R2-M4 (card `legacy.remembered[1]`, round 1's rewording: order reversed, and the prince's thought made a fact).**
- Text: "In Nestor's Life, Theodosius tells Svyatoslav that a monk must rebuke a prince for the salvation of his soul. Svyatoslav came to the monastery and said he had not dared to come while the prior was angry with him."
- In the Life the prince speaks first, and he says he did not dare come *thinking* Theodosius was angry. Theodosius's answer has two halves. Source: PAT l.3692-3696: "се, отче, не дръзнухъ прити к тобѣ, помышляа, егда гнѣваяся на мя ... Но се подобаеть намъ обличати и глаголати вамъ, еже на спасение души, и вамъ лѣпо есть послушати того".
- Fix: "In Nestor's Life, Svyatoslav comes to the monastery and says he had not dared to come, thinking the prior was angry with him. Theodosius answers that monks must rebuke princes for the salvation of the soul, and that princes should listen."

**R2-M5 (card `role`, round 1: "its" points to the cave).**
- Text: "Monks and founders: Antony, hermit of the cave; Theodosius, its prior".
- Fix: "Monks and founders: Antony, hermit of the cave; Theodosius, prior of the monastery".

**R2-M6 (card `uncertain`, last item, round 1: "on that ground" gives Mouravieff a reason he does not state).**
- Text: "A. N. Mouravieff, on that ground, calls Nestor an eyewitness."
- Source: MOUR l.1616-1622: "The annalist Nestor ... was an eye-witness of the life and actions of Theodosius, when he established the Lavra, and entered himself into its retirement in the seventeenth year of his age". Mouravieff states both together and cites nothing.
- Fix: "A. N. Mouravieff, who also has Nestor enter at seventeen, calls him an eyewitness of Theodosius's life." Records, the "Nestor's knowledge" side: "Mouravieff: an eyewitness, who entered at seventeen (MOUR l.1616-1622); the Paterik's seventh discourse, headed as Nestor's, has its writer received at seventeen (PAT l.1239-1241)".

Checked and passing: C-K-M1 (CROSS l.11797-11799, l.11849-11852); C-K-M2 "prior" throughout (CROSS l.11861, l.12657); C-K-M5 (PAT l.1038-1039, l.1230-1233, l.1239-1241); C-K-M7 (PAT l.1034); the card's 1462/1406 and tonsure items (PAT l.1683-1686, 6540 = 1032); 6570 = 1062.

---

## anskar

**Verdict: passes. N-B1 and N-B2 are fixed correctly. Minor fixes only.** Para 7 now gives both sides with their witnesses, keeps Waitz's "videtur" as "thinks", and keeps Adam's "ut aiunt" (ANNBERT l.2176-2181, l.2203; ADAM l.5452-5455). The card's sack item keeps Robinson's "probably" (ROB l.2665-2667) and Steinberg's 845 (STEIN l.3710). The birth now reads as Robinson states it (ROB l.1292-1295), and the records match. N-M1 to N-M8 read right against ROB l.2140-2170, 4322-4328, 5555-5560, 5588-5589, 236-243 and 3746-3748.

**R2-M7 (brief para 7: Adam of Bremen has no context in the brief; optional).**
- Text: "Adam of Bremen put the sack in the emperor Louis's last year, as others told it."
- This is Adam's only mention in the brief. A listener does not know he wrote two centuries later (ADAM l.3551-3557: begun soon after Adalbert's death, books 1-2 perhaps 1074).
- Fix: "Writing in the 1070s, Adam of Bremen put the sack in the emperor Louis's last year, as others told it." To pay for it, "became his friend and counselor, and won leave" becomes "became his friend, and won leave" (the card keeps the counselor). Tested: 407 words, FK 6.07, Flesch 78.12. Take it only if the coordinator accepts 407.

**R2-M8 (card `dates`, round 1: "moved at Bremen").**
- Text: "8 September, sometimes given, was the day his body was moved at Bremen."
- Source: ROB l.1293-1294: "the date of the translation of his body to the church of St. Peter, at Bremen".
- Fix: "8 September, sometimes given, was the day his body was moved to Saint Peter's church at Bremen."

**R2-M9 (card `legacy.remembered[1]`, round 1: "Danish" and "debate" go past the source).**
- Text: "In the Swedish debate of 1527 and 1528, the Danish Carmelite Paulus Helie said the Swedes had left the faith Ansgar preached, and Olavus Petri answered that they kept it."
- Source: OP l.858-863: "Detta sändebref, som är dateradt 1527 ... kom icke i Olavus Petris händer förrän den 10 maj 1528 ... till Paulum Helie af karmeliters orden i Danmark". The source says "of the Carmelite order in Denmark", and the exchange is two letters, not a debate.
- Fix: "In 1527 Paulus Helie, a Carmelite in Denmark, wrote that the Swedes had left the faith Ansgar preached. Olavus Petri answered in 1528 that they kept it."

**R2-M10 (card `legacy.traces[2]`, round 1: Robinson reports the Corvey line and quotes Adam).**
- Text: "Robinson quotes the Corvey chronicle for 936, that the faith Anskar and his helpers preached in Sweden was well nigh extinct, and Adam of Bremen, that among the Danes some small part of it remained."
- Source: ROB l.802-806: "the author of the Chronicon Corbeiensis for the year 936 ... states that the Christian religion which Anskar, Rimbert, Gautbert, and Nithard had preached was well nigh extinct"; l.820-823: Adam, in quotation marks, "some small part of the Christianity that had been planted by Anskar had remained".
- Fix: "Robinson cites the Corvey chronicle for 936: the faith that Anskar, Rimbert, Gautbert and Nithard preached in Sweden was well nigh extinct. He also quotes Adam of Bremen, that among the Danes \"some small part of the Christianity that had been planted by Anskar had remained\"." If the colon reads as a reveal, use "Robinson cites the Corvey chronicle for 936, which says the faith ..." instead.

---

## rimbert

**Verdict: one blocking finding (R2-B3), introduced by round 1's fix to R-M4. R-B1, R-M1 to R-M3 and R-M5 are fixed, with two wording fixes.** The new brief sentences ("she began to sing psalms aloud", WAITZ l.5244-5245; "Once, the Life of Rimbert says, he asked", WAITZ l.4611-4632) are right. "He" in para 13 follows para 11's Rimbert.

**R2-B3 (card `uncertain[3]`, last sentence, and records: Robinson's argument misstated).**
- Text: "Robinson also doubts the Life of Rimbert's rule that every most faithful disciple is Rimbert, since one such disciple says Mass while Rimbert was still a deacon; he thinks that one is Erimbert."
- Robinson does not doubt the rule. He doubts Klippel's use of it for one priest, whom the Life of Anskar calls Anskar's "most intimate associate", not a "most faithful disciple". The records' contested claim makes the same error ("Whether every 'most faithful disciple' ... is Rimbert"; "Robinson: one, who says Mass ...").
- Sources: ROB l.4240-4241 (ch. 27): "while the priest* was standing by the altar and was blessing the sacred mysteries"; l.4250: "this same priest, who was his most intimate associate"; l.4269-4277: "Klippel identifies this priest, who is described as sibi in omnibus familiarissimus, with Rimbert ... He deduces this from the statement in the Vita Rimberti, chap. ix ... It would appear however, that at this time Rimbert was still in deacon's orders, and therefore could not have celebrated Mass ... It is more likely that the priest referred to is Erimbert."
- Fix, card: "Robinson also notes that G. H. Klippel, going by that rule, takes the priest who said Mass with Anskar on his second Swedish journey to be Rimbert. Robinson thinks that priest more likely Erimbert, since Rimbert was then still a deacon."
- Fix, records `contested_claims`: claim "Whether the priest in the Life of Anskar, chapter 27, is Rimbert"; sides "G. H. Klippel, applying the Life of Rimbert's 'most faithful disciple' rule: Rimbert (ROB l.4269-4272; WAITZ l.4790-4800)" and "Robinson: more likely Erimbert, since Rimbert was then a deacon (ROB l.4272-4277)".

**R2-M11 (card `keyWorks[0]`, round 1's R-M5 wording reads as though Robinson addressed the Life).**
- Text: "addressed to the monks of Corbie, near Amiens, by Robinson; Adam of Bremen says New Corbey."
- Sources: ROB l.1164-1170: "i.e. Corbeja antiqua, which is situated about four miles from Amiens ... Adam of Bremen incorrectly identifies this Corbey with the New Corbey"; ADAM l.6202: "ad fratres cenobii direxit Novae Corbeiae".
- Fix: "written with a fellow disciple, the Life of Rimbert says, and addressed to the monks of Corbie. Robinson takes this to be the old Corbie near Amiens; Adam of Bremen says New Corbey. Georg Waitz says nearly all agree it was written at Hamburg before 876. It is used here in Waitz's Latin and C. H. Robinson's English"

**R2-M12 (card `uncertain[1]`, round 1's R-B1 wording: "points the death passage to" is loose and awkward).**
- Text: "Bernhard Schmeidler's margin points the death passage to the Life of Rimbert's twenty-fourth chapter, which the copy used here lacks, and he cites the Annals of Corvey for 888."
- Source: ADAM l.6779-6784: margin "V. Rimb. c. 21" at the illness and "V. Rimb. c. 24" at "depositio est III idus Iunii"; l.6826: "Ann. Corb. 888". The chapter 24 mark sits at the burial day, not the whole passage.
- Fix: "Bernhard Schmeidler's margin sets the burial day beside the Life of Rimbert's twenty-fourth chapter, which the copy used here lacks. For 888 he cites the Annals of Corvey."

---

## README.md

**Verdict: one blocking finding (R2-B4), in round 1's D-B1 rewrite of the river counts. The Clement and Kyiv-placement notes are accurate, with minor fixes.**

**R2-B4 (para "The river counts change": the census's own Who row for Humbert contradicts what the README says the census shows).**
- Text: "By the census lanes, Greek East & Orthodoxy era 4 held five majors by first tradition (...), or six with Humbert of Silva Candida, whose only era 4 tradition is the Macedonian-era Byzantine church. John of Damascus, Theodore, and Cyril and Methodius make it eight. ... The re-score counted Humbert in the Latin West for era 4 (Rescore.md, "Major proposals"), and so gave ten and eleven; the difference is logged in Open-Gaps".
- Mapping each era 4 major's card traditions to CENSUS movements confirms round 1's arithmetic: Latin West has 9 with an era 4 tradition (Bede, Boniface, Aidan, Hild, Adomnán, Alcuin, Dhuoda, Nennius, Hincmar), and Greek East has 5 by first tradition (Martin I, Maximus, Photius, Athanasios, Symeon), plus Humbert by his second. Humbert's traditions are Latin Papal (era 5, Latin West) and Macedonian (era 4, Greek East).
- But the census also has Humbert's own Who row, and that row is what puts him on the map: `{"id": "humbert-of-silva-candida", "era": "4", "kind": "person", "toldWithin": "latin-papal-church-gregorian", "laneLabel": "Latin West & Catholicism", "start": "1054"}`. Every other era 4 major's person row agrees with its first card tradition. The data release that settled these placings is logged as closed (Open-Gaps l.3431 and l.3436: "closed by data release 43. Card traditions settled as named"). So the re-score's ten Latin West majors (Rescore.md l.73) match the live census. Calling them an error, and logging that in Open-Gaps, records a census fact as a mistake.
- "Make it eight" is also ambiguous after "or six with Humbert": 5 + 3 = 8 by first tradition, but 6 + 3 = 9.
- Fix (whole paragraph): "**The river counts change.** By the census's own Who rows, Greek East & Orthodoxy era 4 held five majors (Martin I, Maximus, Photius, Athanasios, Symeon), and John of Damascus, Theodore, and Cyril and Methodius make eight. Latin West & Catholicism held ten, Humbert of Silva Candida among them, and Anskar makes eleven. Antony and Theodosius go on the map in era 5 (below), so they do not count here. Humbert's row sits in the Latin West at 1054, though his Latin Papal tradition is an era 5 entry; his only era 4 card tradition is the Macedonian-era Byzantine church. Counted by era 4 card traditions instead, Greek East holds nine and Latin West ten. Which rule counts is for the map build slice (Open-Gaps, "Map Who build slice: caps, major mark, placement", 2026-11-11). The map shows five per river, and which five is Mark's choice. The re-score proposed for Greek East: Maximus, John of Damascus, Theodore the Studite, Photius, and Cyril and Methodius."
- The Open-Gaps entry for this batch should then log the counting-rule question for the map build slice, not a re-score error.

**R2-M13 ("Card traditions", round 1's D-M4 applied one step too far).**
- Text: "The re-score places them in Kievan Rus' Christianity (about 988 to 1054)."
- CENSUS gives that movement's dates as "988-1054", with no "c.". Only the Cyrillo-Methodian ("c. 863-916") and Scandinavian ("c. 826-1104") entries carry it.
- Fix: "(988 to 1054)".

**R2-M14 ("Majors and lengths": counts no longer match the files).**
- Text: "Their briefs run 404 to 405 words ... at 365 and 366 words."
- `wc -w` now gives john 405, theodore 404, cyril-and-methodius 406, Kyiv 405, anskar 405; rimbert 365, clement 366. Clement's 366 is over the 365 limit the sentence names.
- Fix: write the final counts once Part 1's fixes land, e.g. "Their briefs run 404 to 406 words, about 2:30", and either bring Clement to 365 or say "365 and 366 words, at or one word over the limit".

**R2-M15 ("Who the sources are", Antony and Theodosius: the list of differences after R2-B1, and which text holds which side).**
- Text: "... and Nestor's Life of Theodosius in the Caves Paterik ... Where the two differ (Antony's journeys, Theodosius's tonsure year, who built the monastery above ground, the source of the Studite rule) ..."
- Antony's journeys come from the Paterik's seventh discourse (PAT l.1041-1112), headed as Nestor's but not the Life, which begins at PAT l.1249. The choice of Theodosius (R2-B1) is a further difference.
- Fix: "**Antony and Theodosius.** The Russian Primary Chronicle (Sylvester's colophon of 1116), in Cross's English, and the Caves Paterik, whose base text is the redaction of 1462, with Nestor's Life of Theodosius and a founding account headed as Nestor's. Where the Chronicle and the Paterik differ (Antony's journeys, Theodosius's tonsure year, who chose him as prior, who built the monastery above ground, the source of the Studite rule), the card gives both. It also gives the Chronicle's two accounts of where Antony ended his life."

**R2-M16 (records the README relies on that are not yet in the repo).**
- The README cites Open-Gaps, "Era 4 Who batch 9" (2026-11-15) twice. No such entry is on the branch (`grep "batch 9" Open-Gaps.md` finds nothing). R1_changes says it "is written with this batch". It must exist before merge, worded per R2-B4.
- "Mark's active-year rule ('Best-known dated act')" is in quotation marks but appears in no repo file. The Decision-Log's ruling (l.2016-2040, "Map Who ... where they sit") says only that "each name sits at the point matching the dates the person was active". Either cite the coordinator's relayed question in the batch's Decision-Log entry, or drop the quotation marks: "by Mark's rule that a name sits at the dates the person was active (Decision-Log, 'Map Who: how many names, which names, and where they sit', 2026-11-11)".
- Mark's Clement ruling ("Keep as Who, dispute told (Recommended)") is recorded only in this README so far. It needs its Decision-Log entry with the batch.

**Checked and passing.**
- The Clement note (l.25, l.32). PG126 l.96729-96746 has the Monitum reporting Miklosich and ending "Sed judicium penes Lectorem sit". PG111 l.243-244 has "ANONYMUS. Vita S. Clementis ... cui a nonnullis tribuitur", and l.36942-36947 has "ANONYMI VITA S. CLEMENTIS ... CIRCA MEDIUM SECULUM X". "Ascribed to Theophylact only by some" is a fair rendering of "a nonnullis".
- The Kyiv era 5 placing (l.48). CENSUS era 4 runs 622-1054 and era 5 runs 1054-1300. 1062 = 6570 is Nestor's date for the move (PAT l.2162), so 1062 puts the pair in era 5 under the "dates the person was active" ruling. The README rightly calls it Nestor's act. The 1462 Paterik's 1032 tonsure and Vladimir-era stay are inside 988-1054 (PAT l.1683-1686, l.1040-1041, l.1094-1096).
- The language section's "Two brief quotations cross a scan mark" now matches (ROB l.2652, CROSS l.11859-11860).
- John of Damascus's two census rows: `melkite-arabic-christianity` people entry (year 730, `held` pointer only) and `iconophile-byzantine-monasticism` (year 730, the NPNF quotation, l.36233-36234).

---

## Files and ranges opened

- CROSS l.4625-4690, 11735-11870, 12525-12545, 12640-12672, 12845-12866.
- PAT l.1036-1043, 1092-1100, 1214-1228, 1236-1256, 1680-1687, 2088-2185, 3580-3640, 3660-3700.
- MOUR l.1610-1625 (grep "eye-witness", "seventeenth").
- ROB l.236-244, 664-680, 796-826, 1160-1172, 1292-1301, 2138-2172, 2645-2670, 3744-3749, 4236-4280, 4322-4332, 5548-5600, 5760-5768 (grep "claim", "Klippel", "intimate").
- WAITZ l.2010-2020, 5400-5425. ANNBERT header, l.2170-2206. ADAM l.3548-3560, 5436-5500, 6196-6210, 6776-6790, 6822-6828. STEIN grep 845.
- OP l.850-880, 17015-17040. PG111 l.238-248, 36938-36950. PG126 l.96722-96750.
- CENSUS: `eras`; every era 4 and 5 movement's `era`, `laneLabel`, `dates`; every `kind: person` row for the era 4 majors; the `people` lists for the batch 9 names.
- Era 4 batch 1-9 READMEs (major lines) and all era 4 major cards' `tradition`; Rescore.md l.60-80, l.56, l.100, l.145; Open-Gaps l.2177-2186, l.3431-3436; Decision-Log l.2016-2045.
- Batch 9: the three briefs, cards, audio scripts and records entries; README; R1_review.md Part C and the README sections of Parts A and B; R1_changes.md; `git diff c6bd9d01 HEAD` for the batch folder.
