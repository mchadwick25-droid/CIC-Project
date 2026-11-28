# Card edits: Pamphilus of Caesarea (`pamphilus-of-caesarea`)

A full new card (batch header, "The card"), written to `pamphilus-of-caesarea.card.json` beside this file. Built under "A new card": every field sourced afresh from `Source_Sheet.md` (rows S, E, X, I, L, D, M), `Outline.md` at its lines, or the final brief `pamphilus-of-caesarea.brief.txt` (after `Fresh_Read.md` and `Fresh_Applied.md`). The starting card (`Card.existing.json`) was a pointer only. Every cited line below was re-read in its file. Short names as in the source sheet: EUS, EUS-ed, GRK, JER, JER-ed, JERL, JER6, APL, APM, PHOT, SOC, CHR, ISID, THEO (all under `cic/texts/`); also PHOTM = `photius_opera-t2-contra-manichaeos-mystagogia-epistolae-pg102-grc-lat_migne1860.txt`, ORJ = `origen_commentarii-in-evangelium-joannis-tomus2-grc_lommatzsch1832.txt`, ANF6 = `anf06_gregory-thaumaturgus-dionysius-julius-africanus-methodius-arnobius.xml`.

Readability of the card's running text (short description, knownFor, datesNote, placeNote, key works, legacy, open questions, timeline headlines, lines and notes), on a plain file outside the repository:
`pamphilus-card-text.txt: 3313 words, grade 9.3 (names out 8.1), reading ease names out 67.1, 16.8 words a sentence, 0.4 joining words per 100, 25% short sentences, longest sentence 41 words - pass`

Census validator (`tools/validate-census.mjs --skip-quotes`) on a census copy outside the repository, with this card, the brief as `longDescription` and a placeholder `secondReading` on the three quotations: 0 errors. Every `printed` passes the validator's own wording check at its file and lines. The card's prose carries no quotation marks. The full quote check reports only what release makes: the brief's three renderings need listings in `tools/quote_renderings.json`, and the four old listings for this entry no longer stand.

## Correction found on re-reading (clearly wrong in the starting card and the source sheet)

Photius's hostile verdict ("not a refutation of the charges against Origen for the most part, but rather supports the accusation") and the list of fifteen charges stand in codex 117, which Photius heads "Read an anonymous work defending Origen and his abominable writings, in five volumes", relying "chiefly ... upon Pamphilus the martyr and Eusebius" (PHOT 11360-11378). The Defense of Pamphilus and Eusebius is codex 118 (PHOT 11437). The starting card's item "Photius's view of the Defense" and Source_Sheet D8, E9 (last bullet) and X6 give them to the Defense. On the card they are now told as the anonymous work's (open question "Another book and another apology"). The outline's Leave out line (Outline line 106) sends them to the card, and they go there, credited rightly.

## Fields kept from the starting card

| Field | Kept wording | Evidence |
|---|---|---|
| `otherNames` | "Pamphilus the Martyr", "Pamphilus the presbyter" | SOC 14029 ("Pamphilus Martyr"); ISID 13131; JER 42476; JER 40958-40959 ("Pamphilus the presbyter") |
| `role` | as it stood | S1 (EUS 43036-43038); E2, E3; E10 (EUS 47067-47074) |
| `keyWorks[0..2].title` | as they stood | E7, E9; E2; E3 |
| `legacy.traces` | the Hebrew Matthew and six volumes line; the library destroyed and the two bishops (with "The second recovered many works and left an inventory") | JER 39359-39361, 54979-54980; JER 49618-49621 (Jerome's letter to Marcella, in Rufinus) |
| `legacy.remembered` | the shared-possessions and inheritance line | E1, EUS 47075-47079; GRK 24837-24840; sent to the card by Fresh_Read finding 6 and Outline Beat 1 (line 37) |
| `uncertain` | "The manner of his death" (without the governor's name and the twelve), "His birthplace and family" (without McGiffert), "How much he copied" (first sentence), "The end of Jerome's passage", "The text of the Defense" | D6, E10; S7; E3; E3 (JERL 58494-58497, 58506-58507); I2, E9 (JER 51386-51388) |
| `sources.ownWords` | both items, title, file, language, date | APL, APM; `disputed` shortened, below |
| `sources.about` | Eusebius Greek (GRK), Jerome Latin (JERL), Letter 84 (JER6), Socrates (SOC), the Acts Exposition (ANF6) | files re-read at the lines cited on the card |

## Changed or new, field by field

**`knownFor`.** Old: "Presbyter of the church at Caesarea in Palestine who gathered a library ... Jailed in the Great Persecution, he worked from prison with Eusebius on a Defense of Origen, and was put to death about 310." New: "Presbyter, an elder and priest of the church, at Caesarea in Palestine, who built a library for his church and, Jerome says, copied most of Origen's works with his own hand. In the persecution he was tortured, held two whole years in prison and put to death about 310. Eusebius says the two friends wrote a Defense of Origen together." Why: "from prison" with Eusebius is Photius's alone (Outline line 10, 72, 120; E7); presbyter glossed where first met (X1); "Great Persecution" is not the record's name. Evidence: brief paragraph 2, word for word in substance.

**`shortDescription`** (new): "Pamphilus was a presbyter, an elder and priest of the church, at Caesarea on the coast of Roman Palestine, who built a library for his church and, Jerome says, copied most of Origen's works by hand. He was put to death for his faith about 310, after two years in prison, and his friend Eusebius says the two of them wrote a Defense of Origen together." Evidence: brief paragraph 2; Outline essence (line 5).

**`datesNote`.** Old: McGiffert's reckonings (Nov. 307 to April 308; 310 against the common 309), Jerome's catalog 392 or 393, Rufinus 397. New: the working from the old sources' clues (Header, "Dates from the sources' own clues"): the nineteenth year of Diocletian, in April (EUS 45892-45911; 303 Widely Accepted, S3); prison in the fifth year after the Nones of November (EUS 46620-46697, MP 7.1-4); death after two whole years, on the fourteenth before the Kalends of March (EUS 47106-47107, 47132-47133; S4), so about 310 (S3, D3); Jerome's "in the persecution of Maximinus" (JER 40969-40970); the catalog in the fourteenth year of Theodosius (JER 38785). Removed: McGiffert's dates (M1) and 397 (JER-ed 45085, an editor's).

**`placeNote`.** Old ended "A report as late as Photius has him study at Alexandria under Pierius; McGiffert thinks his teacher more probably Achillas". New ends "Photius, writing more than five centuries later, says he studied at Alexandria under Pierius". Why: McGiffert's view is modern (M5, D4). "Imprisoned" → "held in prison". Evidence: S1, S2, S7, D4 (PHOT 11506-11507).

**`keyWorks[0].about`.** New: what the book is (X6), to whom (E8, APL 14112-14115, with confessors glossed, X5), how it is made (E9, APL 14262-14273), its first argument (E9, APL 14208-14215, narrated), six books (PHOT 11437-11438), the first in Rufinus's Latin (I2), joint work (E7). Removed: "397" (editor), "the editors differ" (M5).

**`keyWorks[1].about`.** Removed McGiffert's "rich in copies of Scripture" (M3). New: E2 (EUS 36890-36894; JER 49608-49618, "sought out all through the world").

**`keyWorks[2].about`.** Old "wrote, about 392"; new adds "these were still kept in the library at Caesarea" (JER 40960-40962) and drops the year here (it is in `datesNote`). Photius: PHOT 11510-11512.

**`legacy.traces`.** Changed: line 1 drops McGiffert's "owes a large part of the materials of his history" (M3; Outline line 83). Line on Rufinus and Jerome: "About 401" → "About ninety years after Pamphilus died", as the brief says; heretic glossed (X7); "as a heretic" from JER 51456-51458 ("follow out the heretic"). Line on the surname: McGiffert's "after Pamphilus's death" and the Letter 84 translator's "Eusebius Pamphili" removed (E11; Outline line 93); new: Photius, codex 13 (PHOT 2113-2115, I7). New lines: Jerome on the copies Palestine read (I6a, JERL 35093-35100; Outline line 46, card by the recount); Isidore (I1, ISID 13131-13136; Cut first 1, card), with Pisistratus glossed (E2).

**`legacy.remembered`.** Changed: "of that time" → "of his time" (EUS 46696-46697). The Life line narrowed to what the brief tells (JER 51429-51437). New: "most eloquent man, of truly philosophical life" and the school (S1, S2, EUS 43036-43045; Cut first 5, card); the chief gate (EUS 47276-47278; Outline Ending 2, not used in the story); the Syriac chronicle and Theophanes (I5, CHR 3726-3728, 3747; THEO 107185); Photius's Mystagogia (I7, PHOTM 27836-27846). Socrates kept in substance (I3, SOC 10542-10547). Removed: McGiffert's "chiefly celebrated for the library" (M3). Not used: "counted worthy of apostolic grace and number" (Cut first 6, Leave out).

**`uncertain`.** Rewritten item by item:
- "His life rests on one friend": kept, last clause tightened.
- "Who wrote the Defense": "about 392 or 393" → "in 392 or 393" (JER 38785); "in 397" removed (editor); "Letter 84 of 400" → "his Letter 84" (date is an editor's); the "About 401 to 402" half split off as "Jerome's later charge", dated by Jerome's own count, "ten years ago" (JER 53975-53981). Evidence: D1 (JER 40968-40969; JER 45146-45147; JER6 19399-19431; JER 50156-50167, 50207-50210; JER 51379-51402, 54979-54980).
- "More on who wrote the Defense" → "The other old witnesses on the Defense": McGiffert, Fremantle and Lightfoot removed (M5; check item 1); the Letter 84 translator's note removed. Kept: Socrates (SOC 10544-10546, 14029-14030), Photius (PHOT 11437-11442), Jerome's two counts (JER 51383-51384; JER6 19408-19410).
- "Whether Eusebius was in prison with him": McGiffert and the Syriac chronicle removed from it; new: E7, D2 (PHOT 11438-11439; EUS 36973-36976).
- New "Friend or teacher": EUS 46694-46695; JER 40958-40959 ("patron"); CHR 3726-3728 (Outline line 74, 120; L2).
- "The year of his death": McGiffert's notes, Martianay, the Jerome volume's "Died 309", the ANF notice and "the census gives 307 to 310" removed (M1). New: the old sources' own counts and the plain statement that they do not settle the year (S3, S4, D3).
- "Where he studied": the ANF notice and McGiffert removed (M6, D4). New: Photius (PHOT 11506-11507) and the longer form's schooling at Berytus (GRK 24841-24844).
- "The manner of his death": "the governor Firmilian" and the twelve moved to the timeline.
- "How much he copied": editors' reading replaced by the sheet's own (E3: "Manu ejus: in his hand; the sentence's subject is Pamphilus").
- "Copies of the Bible": Lightfoot and Taylor no longer named (I6, M4; check item 1); kept as notes reported by editors, not counted (Outline line 109).
- "Other writings": Gennadius added (D5, JER 42476; Outline line 107, card); "meaning astrologers" is the plain sense (JER-ed 45087-45112, a tool for the word). Acts Exposition kept (D7; ANF6 16915-16917).
- "Photius's view of the Defense" → "Another book and another apology": corrected (above).
- New "Whose command the money-changers are": Outline line 23 ("Not told: card, both credited"); ORJ 8726-8731; GRK 8552-8553; APL 14155-14157; Review MINOR 13.

**`sources.ownWords`.** `disputed` on both: "modern editors read it as joint work" removed (M5).

**`sources.about`.** Moved to Modern works, word for word (under Entry fields): "Prolegomena and notes to the Church History and the Martyrs of Palestine" (McGiffert) and "Introductions and notes to Jerome and Rufinus" (Fremantle). Changed titles: Eusebius English adds VII.1 (EUS 39162-39163) and the MP introduction and chapter 4; Jerome English adds the letter to Marcella and Gennadius 17 (author "Jerome, Rufinus of Aquileia and Gennadius of Marseilles"); Jerome Latin drops "with Martianay's notes" (the card uses none); Photius adds codex 13; the chronicle is the Maronite Chronicle, Latin of J.-B. Chabot (CHR 2756-2760; Guidi edited the volume). New, each a file the card cites: PHOTM, ISID, THEO, ORJ.

**`briefSources`** (new): EUS; JER; JERL (Quotes 1 and 3 rendered from it); APL and APM (Quote 2); PHOT (codex 118, "in prison").

**`briefReferences`.** All thirteen old items replaced, one per strand the brief tells, in its order. Removed as no longer told: "The story's about eighty years"; the "not settling doctrine" passage; the Life and the twelve counted like apostles; McGiffert's notes (late 307, February 310, Eusebius much with him in prison, the library as his source); McGiffert, Fremantle and Lightfoot as "the modern editors"; Jerome's Letter 84 and the authorship dispute (the brief does not tell it).

**`quotationOriginals`.** One entry for each of the brief's three quoted spans, in its order, each `modern` the brief's words exactly. Quote 1: printed English JER 51433-51437 (the Latin, JERL 31259-31264, is a damaged single scan, so the English stands alone). Quote 2: printed Latin APL 14153-14158 (no English held; APM 42029-42035 agrees, with "si quis", which the brief's "If anyone" follows); APL's "sed. tantum modo" is given as "sed tantum modo", the stray stop being a scan mark the validator's folding ignores. Quote 3: printed English JER 40966-40968 (Latin JERL 58494-58497, damaged single scan). Removed, as the brief no longer quotes them: "jointly", the "not pronouncing them as a final verdict" passage, "is said to have written", "since they think a martyr praised him". No `secondReading` (all three are six words or more).

**`timeline`** (new; eight periods, built after the brief from the source sheet, outline and card; every line's reference names the work, file and lines, and every note names its file): early life and the presbyter (S7, D4, S1, S2, E1); the books (E2, E3, E4, I6a); the arrest (S3, E5; witness Eusebius); the Defense (E7, E8, E9, E9a; witness the Defense); the death (E10, S4, S5; witness Eusebius; the young man and Seleucus from Cut first 2 and Leave out "card if any"); the Life and the name (E11, E2); the Latin quarrel (D1, I2); later centuries (I3, D5, I1, I5, E7). Not on it, as the outline marks them Leave out: the confessors lamed with hot irons (Cut first 3), the twelve counted like the apostles (Cut first 6), the bodies left four days (E10), the Egyptians' trial scene.

## Entry fields (for release; the entry itself is not edited)

- **`dates`.** Old: "307-310". New: "died c. 310". Why: the years rest on editors' reckonings (M1; Outline line 120); the brief and Setting give "about 310" (Outline line 14). `start`, `end` and `activeYear` (307, 310, 309) only place the entry on the map and stay.
- **`why`.** Old: "He was jailed in 307 and put to death for his faith in 309 or 310." New: "He was jailed in the persecution and put to death for his faith about 310, after two years in prison." Same evidence as `dates`. The rest stands (E2, E3; JER 41076-41077).
- **`teaser`.** Old: "Caesarea in Palestine, c. 307 to 310 CE: a presbyter and book collector, put to death for his faith, whose defense of Origen Eusebius of Caesarea calls joint work and Jerome denies him." New: "Caesarea in Palestine, about 310 CE: a presbyter who gathered a library and copied Origen's books by hand, put to death for his faith, whose Defense of Origen Eusebius says the two wrote together." Why: dates as above; Jerome first listed it under Pamphilus's name and only later denied it (D1), which the brief does not tell. It says no more than `knownFor` and the brief.
- **`relationsSummary`.** Old: "... He is said to have studied at Alexandria. ... The Library shelves his Apology with them." New: "... Photius, writing centuries later, says he studied at Alexandria. ... The Library shelves his Defense of Origen with them." Why: the report is Photius's alone, late (D4); "Apology" alone is barred (Outline line 90; X6).
- **`voices`.** "Apology for Origen" → "Defense of Origen" (item 1); "the Apology" → "the Defense" (item 3). Same reason.
- **`sourcing`.** Each "Apology" → "Defense of Origen" (first) or "Defense" (after). Same reason. No conflict otherwise.
- **`legacy`.** "Two later worlds in the Library name him." is builder's wording for a visitor; "Eusebius's Apology" → "Eusebius's Defense of Origen". The two quoted spans stand verbatim (EUS 44790-44791; JER 53981-53982). Listed as a conflict for release: "calls him a copyist" says less than the card (JER 40958-40962) but does not contradict it.
- **`modernWorks`** (new; none is cited as a source on the card; each the outline used to clarify an old text or find one; all pre-1931 and held in `cic/texts/`, rights lines in each file's header):
  - {"title": "Prolegomena and notes to the Church History and the Martyrs of Palestine", "author": "Arthur Cushman McGiffert", "year": "1890", "note": "The translator's introduction and notes to Eusebius's Church History and Martyrs of Palestine, on their manuscripts, dates and readings."} (moved from the card's `sources.about`, word for word)
  - {"title": "Introductions and notes to Jerome and Rufinus", "author": "William Henry Fremantle", "year": "1892", "note": "The editor's introductions and notes to Jerome's Lives of Illustrious Men and Apology and to Rufinus's writings on the Defense of Origen."} (moved from the card's `sources.about`, word for word)
  - {"title": "Eusebius Werke, Zweiter Band: Die Kirchengeschichte, Zweiter Teil: Die Bücher VI bis X", "author": "Eduard Schwartz and Theodor Mommsen (ed.)", "year": "1908", "note": "The Greek text of Church History VI to X and of both forms of the Martyrs of Palestine."}
  - {"title": "S. Pamphili martyris Apologia pro Origene (Origenis Opera omnia, tomus XXIV)", "author": "C. H. E. Lommatzsch (ed.)", "year": "1846", "note": "Rufinus's Latin of Book I of the Defense, with the Delarues' notes on its readings."}
  - {"title": "Patrologia Graeca 17: Origenis opera omnia, tomus VII", "author": "J.-P. Migne (ed.)", "year": "1857", "note": "A second printing of Rufinus's Latin of the Defense, with Delarue's introduction."}
  - {"title": "Patrologia Latina 23: Sancti Eusebii Hieronymi opera omnia, tomus secundus", "author": "J.-P. Migne (ed.), after Dominique Martianay", "year": "1883", "note": "Jerome's Latin of the Lives of Illustrious Men, with the Greek of Sophronius, and of the Apology against Rufinus."}
  - {"title": "The Library of Photius, volume 1", "author": "J. H. Freese (tr.)", "year": "1920", "publisher": "Society for Promoting Christian Knowledge", "note": "English translation of Photius's book notices, among them his notices of the Defense of Origen."}
- **`longDescription`**: the final brief, final newline removed (release).
- `major` stays false; no new census entry is needed.

## Claims not found

None. Every kept or new claim stands on a line cited above. "303" for the nineteenth year of Diocletian rests on the source sheet's Widely Accepted rating (S3); "a historian of the fifth century" for Socrates, "in the ninth century" for Theophanes and Photius, and "about three centuries later" for Isidore rest on the source sheet's witness list (lines 25-27).

## Left for the checker

- The codex 117 correction, above: the card departs from Source_Sheet D8, E9 and X6 on the file's own lines.
- The three quotations carry no `secondReading`, as the role says; the validator needs one before release. None is under six words, so none is "checked at card".
