# Card edits: Suetonius

A full new card (batch header, "The card"), written to `suetonius.card.json`. Every field is sourced afresh. The starting card (`Card.existing.json`) was a pointer only; each field kept from it is listed with its evidence. Short names for files are those of `Source_Sheet.md` (ROL, THF, NT-E, TERT-C, TERT-E, TERT-O, LAC-L, LAC-E, BEDE, JER-E, JEP-E, EUS, SCH, MIR, RUI); TAC = `cic/texts/tacitus_annals-15-44_church-brodribb1876.txt`. Every cited line was re-read in its file for this card.

Validator: a copy of the census outside the repository, with this card and the final brief as `longDescription`, passes `node tools/validate-census.mjs` with 0 errors. For that run only, the three 6-word-or-longer quotations were given a placeholder `secondReading`, and a copy of `tools/quote_renderings.json` listed the brief's four renderings (below). Neither copy is in the repository.

Readability (`python -m engine.m1.profile_readability` on a plain file of the card's running text, outside the repository; references left out):
`card_text.txt: 1390 words, grade 7.1 (names out 5.5), reading ease names out 78.4, 13.0 words a sentence, 0.7 joining words per 100, 32% short sentences, longest sentence 34 words - pass (note: grade 7.1 is under 8: the listener read checks it is not flat)`

## Fields

**otherNames.**
- Kept: "Gaius Suetonius Tranquillus". ROL 149 (Rolfe's introduction, the name as printed); the three parts stand in Suetonius's father's name, ROL 34517–34518 ("pater meus Suetonius Laetus"), Tertullian's "Suetonium Tranquillum" (TERT-C 920) and Jerome's "Tranquillus".
- New: {"name": "Tranquillus", "note": "the name Jerome uses for him"}. JER-E 38773–38775; JEP-E 9227; JEP-E 46325.

**label.** Kept: "Outside witness". Slate shape; `kinds/person.md`.

**knownFor.** Kept word for word. Claudius 25.4 (ROL 25843–25844, "Iudaeos impulsore Chresto assidue tumultuantis Roma expulit"); Nero 16.2 (ROL 28454–28460, among the acts "sub eo"; Nero 19.3, ROL 28653–28654, "in unum contuli" his acts). "Chrestus" in quotes stands in ROL 25908. The brief's own claims are the same.

**shortDescription.** New, written fresh: "Suetonius was a Roman scholar who wrote the lives of Rome's rulers from Julius Caesar to Domitian. In them, two short lines tell of Jews driven from Rome under Claudius for rioting at the urging of Chrestus, and of punishments laid on the Christians under Nero." Brief, paragraphs 1–2 and 5; Outline, essence (E1, E3, S5).

**datesNote.**
- Old: "Born about 69 or about 77; dismissed by Hadrian about 121"
- New: "No old source gives the year of his birth or his death. He says he was a young man twenty years after Nero's death, so about 88. His lives end with Domitian, who died in 96, so he wrote after that. He later ran the emperor Hadrian's letters."
- Why: clearly wrong under the date rule. 69 and 77 are Mommsen's and Macé's reckonings (S2, ROL 155–157: Contested, modern reckonings); 121 is Rolfe's from Septicius's term (S4, ROL 233–235: Dominant Modern Reconstruction). The outline bars "born in 69 or 77" and "dismissed in 121" (Do not say). The new note works from the sources' clues (Header, "Dates from the sources' own clues"): Nero 57.2, ROL 32023–32025 ("post viginti annos adulescente me"), in the chapter after Nero's death, with Nero's death in 68 Widely Accepted (S6); the book ends with Domitian, who died in 96 (S5, Widely Accepted); Hadrian's letters, SCH 6074–6075 ("Suetonio Tranquillo epistularum magistro"), the brief's paragraph 3.

**placeNote.** Kept: "Rome". S7; both lines (E1, E3).

**role.** Kept: "Roman biographer". The Lives (S5, X1).

**keyWorks.**
- Kept: Lives of the Caesars, word for word. ROL 323–324 and the held text, from The Deified Julius (ROL 918) to Domitian (ROL 36065).
- New: On Illustrious Men, "lives of Rome's men of letters, which survive only in part. Jerome followed its example for his short lives of Christian writers". ROL 262–264 (the title "On Illustrious Men (in the field of literature)"); ROL 320–322 (only the Lives "has come down to us entire, or nearly so"); JER-E 38773–38779; JEP-E 9227–9234 (R5). Outline Cut first 2 sends Jerome to the card.

**legacy.**
- Removed: the one `remembered` line, "John Rolfe, his translator, says Tertullian of Carthage drew on Suetonius's work about the public shows. Rolfe adds that the influence of Suetonius is seen in the form of the Life of Ambrose by Paulinus, Ambrose's secretary." Why: each half is a modern claim given as content (R6: "MODERN claims. Card only" as modern works, never as the card's own text; Header, "Modern works on the cards"; Kit Part 1, "A modern work is a tool, never a witness"). Tertullian's use is now told from his own words (below). The Paulinus point rests on Rolfe and Kaniecka alone and is not told.
- New `traces`:
  1. Bede, about 725, the Claudius line almost in Suetonius's words, without Chrestus, in Claudius's ninth year, joined to Acts by "quod et Lucas refert". BEDE 23216–23217; BEDE 18402 ("AD A. DCCXXV"). Outline R1, "What came of it" 1; brief paragraph 8.
  2. Jerome's short lives of Christian writers, up to the fourteenth year of Theodosius, following Tranquillus. JER-E 38773–38785. Outline R5, Cut first 2.
  3. Jerome's chronicle preface, from Tranquillus. JEP-E 46321–46325. Outline Leave out ("Jerome's Chronicle drawing on Tranquillus (R5): card").
- New `remembered`:
  1. Tertullian names Suetonius twice: the games (TERT-C 919–920; TERT-E 6789–6791) and Nero's dreams (TERT-C 21023–21025; TERT-E 18756–18759); he never cites the line on the Christians (R4; Do not say). Outline Cut first 3.
  2. Tertullian and Lactantius on "Chrestians" and "Chrestus", neither naming Suetonius. TERT-C 3904–3905; LAC-L 16813–16814 (R3). Outline Cut first 4 (Lactantius to the card).
  3. Ruinart, monk of Saint-Germain-des-Prés, died 1709 (RUI 789–792), answering Dodwell's dissertation printed at Oxford in 1684 (RUI 2295–2298); the Jews read as including Christians (RUI 3126–3129); the edict judged from the list (RUI 3153–3158). Given as his reading; "Suetonius names no such order" from E3. Outline Leave out (Ruinart, card); batch header ruling ("Ruinart (1689) goes to the card"). The year 1689 is not given: the held print is the 1859 reprint and does not give it (Outline Leave out); the card dates his reading only by its clues.

**uncertain.** Each item stands alone.
- Removed: "Rolfe and the notes to Thomson and Forester's edition both read "Chrestus" as Christ. ..." Why: a modern identification given as content (D1: Contested; the readings are Rolfe's and the 1909 editors'). Replaced by item 1 below, from the old sources.
- Removed: "Thomson and Forester translate "one Chrestus." Rolfe notes that the Latin has no word for "one" here, and takes that as a sign that Christ is meant." Why: the second sentence is Rolfe's modern reading. The fact about the Latin goes to item 3 and stays in the quotation's own `uncertain`.
- Removed: "The Thomson and Forester notes cite Luke, in Acts 18:2, for the expulsion of the Jews by Claudius. They add that Dio Cassius says he only forbade their meetings." Why: modern notes as the card's content. Replaced by items 4 and 6, from Acts, Dio's print and Bede.
- Removed: "Rolfe reports two dates for his birth: 77, from Mommsen, and 69, from Macé, which Rolfe thinks somewhat more probable. The Thomson and Forester preface puts it late in the reign of Vespasian." Why: modern dates (S2), barred from the card by the date rule. Rolfe's introduction is listed under Modern works instead.
- Kept word for word: "Suetonius blames Nero for the great fire, but his notice of the Christians does not mention it." E5: ROL 30503–30507 (Nero 38); ROL 28458–28460 (Nero 16.2).
- New:
  1. Who Chrestus was. E1 (ROL 25843–25844); X3 and D2 ("close in sound to Christus"); LAC-L 16813–16814; TERT-C 3904–3905; R3 (neither names him). Outline Do not say: never "a misspelling".
  2. Chrestus as a name: EUS 50626–50627, 50640 ("Constantine Augustus to Chrestus ... bishop of Syracuse"). Outline Leave out ("The bishop of Syracuse named Chrestus (D2): card").
  3. All the Jews: E1 (no "all" or "one"); D4: NT-E 88523 ("all the Jews").
  4. Driven out, or barred from meeting: Acts NT-E 88523–88524; Dio in MIR 2512–2516, badly damaged; the reading is the source sheet's, Inferential-Thin, matching the sense reported in THF 20377–20378 (D3). Outline Leave out ("Dio's report ... Card, with the disagreement stated"). Told as uncertain, in plain words, with no quote, since the Greek is held only in a damaged print.
  5. The year: D5; BEDE 23216 ("Nono regni sui anno").
  6. The same event: D6; BEDE 23217 ("quod et Lucas refert").
  7. The punishment under Nero: E3 (no number, charge or kind); E4 (ROL 28653–28654, 28700–28702); no law named (Outline Do not say, the edict).
  8. Superstition: X7 and the brief's gloss; ROL 25849–25850 ("Druidarum religionem apud Gallos"), the fresh read's note.
  9. Suetonius names the Christians only in the life of Nero: E6.
  10. The dismissal: S4, SCH 6074–6076 and ROL 239–241 (Spartianus, written long after: ROL 158–160). Outline Cut first 1 (the dismissal and its reason to the card), kept to its own words; D8.
  11. Pliny the Younger: S3 and N1 (the letters are not held). The slate makes Pliny a link only; connections are left out for now.

**sources.**
- `ownWords`: both kept word for word (ROL, THF).
- `about`, kept word for word: Acts 18 (NT-E); Apology 3, Latin, Oehler (TERT-O); Apology 3, English (TERT-E). The Apology stays because the card's quotation note names it (R3, TERT-O 12453–12456, TERT-E 1712–1716).
- `about`, moved out: "The Life and Works of Suetonius (introduction)", John C. Rolfe. A modern work; it moves word for word to the entry's `modernWorks` (Entry fields).
- `about`, new: Tertullian, To the Nations 1.3, On the Shows 5, On the Soul 44, Latin (TERT-C) and English (TERT-E); Lactantius, Divine Institutes 4.7, Latin (LAC-L) and English (LAC-E); Jerome, Lives of Illustrious Men, preface (JER-E); Jerome, Letter 47 and the preface to the Chronicle (JEP-E); Bede, Greater Chronicle 287 (BEDE); Eusebius, Church History 10.5.21 (EUS); Spartianus, Life of Hadrian 11.3, as printed in SCH 6074–6076; Dio, Roman History 60.6, as printed in MIR 2512–2516, marked badly damaged; Tacitus, Annals 15.44 (TAC, the brief's sentence on Tacitus); Ruinart, Acta martyrum, preface (RUI). Each is cited by a field of the card.

**briefSources.** New: the old sources the brief draws on: Suetonius (ROL), Acts 18 (NT-E), Tertullian (TERT-C), Lactantius (LAC-L, the plain sense of anointing in paragraph 6), Bede (BEDE), Spartianus (SCH, the post in paragraph 3), Tacitus (TAC, paragraph 6).

**briefReferences.** Rebuilt to the brief as it now stands.
- Removed: "John C. Rolfe, The Life and Works of Suetonius: the Lives of the Caesars, published in 120 ...", "Rolfe's note on Claudius 25.4 ...", "Lives of the Twelve Caesars, tr. Alexander Thomson ... preface and notes 335 and 528 ...", "Carl Mirbt, source book ... and Schanz, Hosius and Krüger ...". The brief tells none of these (Pliny, 120, Rolfe's readings, "how little", the source books), and each is modern.
- Removed: "Tertullian, Apology 3, Latin ed. Franz Oehler ...". The brief now quotes To the Nations 1.3 (Outline Q3).
- Changed: Claudius 25.4 and Nero 16.2 to the brief's wording (old Troy, the theater; "severely punished and put down", beans and greens, the chariot drivers).
- Changed: Acts 18:1–2 to the brief's wording.
- Changed: Lactantius to 4.7.5–7, adding the holy oil and "the Anointed" (LAC-L 16816–16830; LAC-E 3163, 3177), which the brief's paragraph 6 now draws on.
- New: Otho 10.1, Nero 57.2, Domitian 12.2 (S1); Spartianus 11.3 (S4); Tertullian, On the Shows 5, On the Soul 44, To the Nations 1.3, with the ANF note on chrestos (TERT-E 9208–9210); Bede 287 (R1); Tacitus, Annals 15.44 (TAC 68).

**quotationOriginals.** One entry for each quoted span in the brief (seven).
1. Q1, "He drove out of Rome the Jews who kept rioting at the urging of Chrestus." New modern wording, the brief's exactly. `printed`, `work`, `englishPrinted` and its lines kept from the old entry: ROL 25843–25844 (Latin), ROL 25907–25909 (English). `uncertain` kept word for word (E1). The old `secondReading` is dropped: the wording changed and release sets it.
2. "Chrestians" (brief paragraph 2). New. TERT-E 9206 ("you call us “Chrestians”"); original TERT-C 3905 ("Chrestiani  pronuntiamur"). Under six words: "checked at card".
3. "Chrestus" (brief paragraph 2). New. LAC-E 3163; original LAC-L 16813–16814. The complaint about Christ's name is Lactantius's (Outline essence, R3). "checked at card".
4. Q2, "Punishments were laid on the Christians, a kind of people holding a new and harmful superstition." New modern wording, the brief's. `printed`, `work`, `englishPrinted` and lines kept: ROL 28458–28460; ROL 28523–28525 (the scan's "inflicted a" is listed in `tools/quote_scan_readings.json` as "inflicted on"). `uncertain` changed: old "For maleficae Rolfe has "mischievous" and the Thomson and Forester English "impious"; their note takes the word to suggest witchcraft. The modern English says "harmful"." New "For maleficae Rolfe has "mischievous" and the Thomson and Forester English "impious". The modern English says "harmful". The Latin has no verb with Nero as its subject: punishments were laid on the Christians, under him." Why: the witchcraft reading is the 1909 note's own (X8: Inferential-Thin), a modern reading; the grammar is E3 and the outline's Do not say. `secondReading` dropped (release).
5. "Christian" (brief paragraph 6). New. TERT-E 9204 ("The name <i>Christian</i>"); original TERT-C 3903 ("Christianum"). "checked at card".
6. "the anointed one" (brief paragraph 6). New. LAC-E 3177 ("we call Him Christ, that is, the Anointed"); original LAC-L 16830 ("nos eum Christum nuncupamus, id est unctum"). "checked at card".
7. Q3, "You say it wrong, and call us 'Chrestians', for you are not even clearly sure of the name itself. Even so, it rings of sweetness or goodness." New. `printed` TERT-C 3904–3907, verbatim, with the print's vertical strokes and double spaces as the file holds them (the census check folds them; joining "no|minis" would not stand in the file); `englishPrinted` TERT-E 9205–9208. `uncertain` new: the rendering is from the Latin; the strokes are the print's; the Apology 3 parallel and the ANF's added "the name you hate" (TERT-E 1714; TERT-O 12453–12456 has "nec nominis certa est notitia").
- Removed: the Acts entry ("because Claudius had commanded all the Jews to depart from Rome,"), "beyond criticism.", "how little" and the Apology 3 entry. The brief no longer quotes any of them.

**timeline.** New, seven periods, every line with its reference (file and lines) after the point.
1. Under Claudius: E2 (ROL 25904–25907, 25909–25916), E1 (ROL 25843–25844), D6 (NT-E 88521–88524). "In the first century": Outline Setting (S6).
2. Under Nero: E3 (ROL 28454–28462), E4 (ROL 28653–28656), E5 (ROL 30503–30507). Witness named at the head.
3. His own life: S1 (ROL 34517–34519; 32023–32025; 40104–40107), S5 (ROL 918, 36065), S4 (SCH 6074–6076), with the late witness noted on its line. The Domitian line keeps only the plain fact of his youth at a hearing (Outline Leave out).
4. About 200, and later: R4 (TERT-C 919–920, 21023–21025), R3 (TERT-C 3903–3907; LAC-L 16813–16830). "About 200" is the brief's; Lactantius's line is "Date unknown", since no held line fixes it.
5. In the fourteenth year of Theodosius: R5 (JER-E 38773–38785, the record's own phrase; JEP-E 46321–46325, "Date unknown").
6. About 725: R1 (BEDE 23216–23217; BEDE 18402).
7. Between 1684 and 1709: R2 (RUI 2295–2300, 3126–3129, 3153–3158, 789–792). The range is worked from the clues: he answers a dissertation printed in 1684 and died on 27 September 1709.

## Not found

None. Every kept claim was found in a held line.

## Entry fields

- **dates.** Old: "born c. 69 or c. 77; dismissed c. 121". New: "young man c. 88; wrote after 96". Why: the old years are modern reckonings (S2, S4), and the brief's date rule governs shown `dates` (Kit Part 1, Rigor; Stage Two Kit 3). Evidence as for `datesNote`. `start`, `end` and `activeYear` only place the entry on the map and are left as they are.
- **teaser.** No change. It is the card's `knownFor`, which the brief supports (above).
- **regions.** A conflict, for release to judge: the entry lists "Mediterranean" and "Asia Minor". Nothing in the sheet, outline or brief places Suetonius or either line in Asia Minor; both lines are set in Rome (S7). The card does not use it.
- **modernWorks.** New (the entry has none). Each is a work the outline used to clarify an old text or find one (Outline, Who tells it, "Modern"); all are printed before 1930 and held in `cic/texts/` (`Build/worlds/_cross-world/CORPUS-USE.md`).
  1. Moved word for word from the card's `sources.about`: {"title": "The Life and Works of Suetonius (introduction)", "author": "John C. Rolfe", "year": "1914", "note": "Rolfe's introduction to his Loeb Suetonius, on what is known of Suetonius's life and works, with the modern reckonings of his birth and his dismissal."}
  2. {"title": "Suetonius (Loeb Classical Library), two volumes", "author": "John C. Rolfe (tr.)", "year": "1914", "publisher": "William Heinemann, London; The Macmillan Co., New York", "note": "Ihm's Latin text of the Lives of the Caesars with an English translation and notes, among them notes on the Claudius and Nero passages."}
  3. {"title": "The Lives of the Twelve Caesars", "author": "Alexander Thomson (tr.), revised by T. Forester", "year": "1909", "publisher": "George Bell & Sons, London", "note": "English translation of the Lives, with a preface on Suetonius's life and notes on the Claudius and Nero passages."}
  4. {"title": "Quellen zur Geschichte des Papsttums und des römischen Katholizismus, third edition", "author": "Carl Mirbt (ed.)", "year": "1911", "publisher": "J. C. B. Mohr (Paul Siebeck), Tübingen", "note": "A source book whose first documents print the Latin of both lines, with Dio's Greek on Claudius and the Jews."}
  5. {"title": "Geschichte der römischen Litteratur, part 3: Die Zeit von Hadrian 117 bis auf Constantin 324, third edition", "author": "Martin Schanz, Carl Hosius and Gustav Krüger", "year": "1922", "publisher": "C. H. Beck, Munich", "note": "A history of Roman literature whose section on Suetonius prints both lines among the testimonies and quotes the Latin on his dismissal."}
  6. {"title": "Tertulliani quae supersunt omnia, volume 1", "author": "Franz Oehler (ed.)", "year": "1853", "publisher": "T. O. Weigel, Leipzig", "note": "Latin text of Tertullian's Apology and other works, with notes that set the Chrestianus passage beside Suetonius's Claudius."}
  7. {"title": "Tertulliani Opera, part 1 (Corpus scriptorum ecclesiasticorum latinorum 20)", "author": "August Reifferscheid and Georg Wissowa (ed.)", "year": "1890", "publisher": "F. Tempsky, Prague and Vienna; G. Freytag, Leipzig", "note": "Latin text of Tertullian's To the Nations, On the Shows and On the Soul, among other works."}
  8. {"title": "Lactanti Divinae institutiones (Corpus scriptorum ecclesiasticorum latinorum 19)", "author": "Samuel Brandt and Georg Laubmann (ed.)", "year": "1890", "publisher": "Gerold and Tempsky, Vienna", "note": "Latin text of the Divine Institutes, with notes that set the Chrestus passage beside Tertullian."}
  9. {"title": "Latin Christianity: Its Founder, Tertullian (Ante-Nicene Fathers, vol. 3)", "author": "S. Thelwall and Peter Holmes (tr.)", "year": "1885", "note": "English translations of Tertullian's works, with a note on the Greek chrestos, pleasant and good."}
  10. {"title": "Fathers of the Third and Fourth Centuries: Lactantius and others (Ante-Nicene Fathers, vol. 7)", "author": "William Fletcher (tr.)", "note": "English translation of Lactantius's Divine Institutes, with notes on Chrestus and on the Greek chrestos, kind, gentle, good."}
  11. {"title": "Chronica minora, vol. 3 (Monumenta Germaniae historica, Auctores antiquissimi 13)", "author": "Theodor Mommsen (ed.)", "year": "1898", "publisher": "Weidmann, Berlin", "note": "Latin text of Bede's greater chronicle, with the editor's marginal references to its sources."}
  12. {"title": "Theophili episcopi Antiocheni ad Autolycum libri tres (Corpus apologetarum Christianorum saeculi secundi 8)", "author": "Johann Karl Theodor von Otto (ed.)", "year": "1861", "publisher": "Friedrich Mauke, Jena", "note": "Greek text of Theophilus with a Latin translation and notes, one of which gathers the Chrestianus and Chrestus passages of Tertullian and Lactantius."}
  13. {"title": "Carthage romaine", "author": "Auguste Audollent", "year": "1901", "publisher": "Albert Fontemoing, Paris", "note": "A history of Roman Carthage, with a note on the Chrestianus passages in Tertullian."}
  - Left out: Duchesne (1907), Bell (1924), Malech (1910), Kaniecka (1928) and Foxe's margin. The outline used them only for claims of their own (readings, dates, influence), not to clarify or find an old text (Outline, Who tells it; R6, R7, R8).

## For release (not card fields)

- `tools/quote_renderings.json`: the three old `suetonius` listings name wordings the brief no longer has. The brief's renderings to list are Q1, Q2, Q3 and "the anointed one" (LAC-L 16830), each with its second reading.
- Q1, Q2 and Q3 carry no `secondReading`; release sets it from the second readings.
