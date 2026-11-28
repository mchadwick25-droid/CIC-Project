# Card edits: Lactantius (`lactantius`)

This is a full new card (batch header, "The card"), written to `lactantius.card.json` beside this file. It was built under "A new card". Every field is sourced afresh from `Source_Sheet.md` (rows S, E, I, D, Q-src), `Outline.md` at its lines, or the final brief `lactantius.brief.txt` (after `Fresh_Read.md` and `Fresh_Applied.md`). The starting card (`Card.existing.json`, the same as the census `card` today) was a pointer only. Every cited line below was re-read in its file. Short names follow the source sheet: AN, DI-L, DI-L3, TE, JE, JC, JL, JLL, EU, AU, LU, CA, MI, MO, SH. Two files not on the sheet's list: SO = `npnf202_socrates-sozomen-ecclesiastical-histories.xml` (Outline line 76), and the chapter numbers of the ANF edition, checked from its `title` attributes.

Line corrections against the sheet, found on re-reading:
- AN 4505 and 4513 (the judge) are in ANF chapter V.2, not V.3.
- AN 575 and 584 are ANF Book I chapter 1, and AN 556 is the ANF Preface (Brandt I.1.8).
- The *Persecutors* dating clues are at AN 10501 (Galerius's edict, "the eighth consulship of Galerius, and the second of Maximin Daia") and AN 10680–10682 (the edict of Milan, "while he and Constantine were consuls for the third time").

**Readability** of the card's running text (short description, knownFor, datesNote, placeNote, key works, legacy, open questions, timeline headlines, lines and notes), run on a plain file outside the repository:
`lactantius-card-text.txt: 2881 words, grade 9.3 (names out 7.8), reading ease names out 71.7, 18.2 words a sentence, 0.6 joining words per 100, 19% short sentences, longest sentence 44 words - pass`

**Census validator.** I ran `tools/validate-census.mjs --skip-quotes` on a census copy outside the repository. The copy had this card, the brief as `longDescription`, and a placeholder `secondReading` on the four long quotations. Result: 0 errors. The validator checked every `printed` and `englishPrinted` at its file and lines. The card's prose holds no quotation marks.

I also ran the full check. It gives five errors, all expected until release:
- Two brief renderings (Quote 1 and Quote 3) still need listings in `tools/quote_renderings.json`.
- Three old listings for this entry no longer stand in the brief.

## Fields kept from the starting card

| Field | Kept wording | Evidence |
|---|---|---|
| `otherNames[0]` | "Firmianus" | JE 41033; TE 11177–11179 (S1) |
| `keyWorks[*].title` | "Divine Institutes"; "On the Workmanship of God"; "On the Deaths of the Persecutors" | AN 538 ff., 9302, 9971 |
| `keyWorks[1].about`, first sentence | "a short book on the making of man, addressed to Demetrianus, which Jerome calls On the work of God or the creation of man." | JE 41050–41051; AN 9302–9310 |
| `legacy.traces` (Calvin) | word for word | CA 7254–7256, 10121–10123 (I6) |
| `legacy.remembered` (Chronicle; millennium) | word for word | JC 44984–44986, TE 11241–11243 (Q-src 4); JE 39882–39885 (I1) |
| `sources.ownWords[0]`, `[3]`, `[4]`, `[5]` | word for word | AN, DI-L, DI-L3, TE |
| `sources.about` (Vetera testimonia; Calvin) | word for word | TE 11171 ff.; CA |

## Changed or new, field by field

**`otherNames[1]`.**
- Old: "L. Caecilius Firmianus". This is Monceaux's full name, from inscriptions (S1; MO 28686–28688), a modern reconstruction.
- New: `{"name": "Lucius Caecilius Firmianus Lactantius", "note": "the fullest form in the book titles of some copies of the Divine Institutes"}`.
- Evidence: DI-L 131 ("L. Caecilii, Firmiani Lactantii", a very late hand), 5452–5454 ("LACTANTII CAECILII FIRMIANI"), 32648 ("L CAECILI FIRMIANI LACTANCI"). These are the Fresh_Read's Do-not-say evidence.

**`knownFor`.** The old text named the *Persecutors* as "which most scholars hold his" (a modern opinion) and used "rhetoric" with no gloss. The new text is the brief's essence.
- "from Africa, Jerome says": Do not say, Outline line 153.
- Teaching at Nicomedia in Bithynia in 303: brief paragraph 2.
- The Institutes and religion that cannot be forced: brief paragraph 2.
- Crispus "in extreme old age": brief paragraph 8; JE 41051–41054.

**`shortDescription`** (new). Drawn from brief paragraph 2, and from Do not say line 151 ("the city where the emperor Diocletian kept his palace").

**`datesNote`.**
- Removed: every year from Monceaux, Schanz and Fletcher (290, 305/306, 307–311, 314, 316, 317, 325, Trier). Under Part 1 and the header's "Modern works on the cards", these stay off the card (Setting, Outline line 30; D5).
- New: no birth or death year held. "303" is worked from Eusebius's "nineteenth year of the reign of Diocletian" (EU 43460–43461), Widely Accepted (S6). The books describe the persecution (AN 4487, 4899). Crispus: JE 41051.
- Kept off, as Leave out: Jerome's placing in Diocletian's reign (Cut first 14) and the Chronicle's placing at the year Crispus was made Caesar (Cut first 9).

**`placeNote`.**
- Removed: Monceaux's Cirta and Mascula, and Fletcher's Firmum (D5; Do not say "born in Africa").
- New: from Africa (JE 41038–41041). Nicomedia and Bithynia, with the outline's glosses (Setting line 31; Words to explain, line 37). The palace: S5 (EU 43982–43983, 70323–70325). "Jerome names no city": E12.
- The Banquet "in Africa" moved to `uncertain` (D4).

**`role`.**
- Old: "Teacher of Latin rhetoric at Nicomedia; Christian writer in Latin".
- New: "Teacher of Latin public speaking at Nicomedia; Christian writer in Latin".
- Why: the outline's plain word for rhetoric (Words to explain, line 36; S4).

**`keyWorks[0].about`.**
- The title gloss: E7, AN 569; brief paragraph 6.
- Book I: AN 1007–1009, with the Fresh_Read's Do not say "had once been men". The Sibyls: AN 692, 700, with the outline's gloss (line 41; Cut first 1 to card).
- Books II to IV: the ANF book titles at AN 1280, 2219, 2987; AN 575, 584.
- Book V: AN 5140, 5158. "On justice" is left off (Cut first 15, Leave out).
- Book VI: AN 5254.
- Book VII: AN 6648 (Cut first 10 to card; gloss at line 42).
- The address to Constantine: E10, D3, given as disputed with no modern names (Do not say line 157).
- Removed: Quote 2's first-person content and the eyewitness lines, now in the timeline. Also removed: the Tertullian/Cyprian line (now in the timeline) and the governor line.

**`keyWorks[1].about`.** The first sentence is kept. Monceaux's dating and his "cry of a man who had just lost his school" are removed (E9: his inference, not carried). New second sentence: AN 9310 and TE 3608 (Cut first 3 to card).

**`keyWorks[2].about`.**
- Now opens with the disputed authorship and the one copy's name (brief paragraph 8; D1).
- Contents: AN 9975–9987, 10223, 10462–10505, 10620, 10680–10690, 10712 (Leave out line 182; Cut first 17 to card).
- "Held in English only" was wrong: MI 4790–4796 holds chapter 48 in Latin (sheet, line 17). Corrected to "in English, … and its chapter 48 … in Latin".

**`legacy.traces`.**
- New, Lucifer: I2; LU 15818–15820, 16934–16942; DI-L3 35546–35550. The Arian gloss is SO 2096 (Outline line 76). This is What came 2, the brief's own wording, without quotation marks.
- Augustine, Sibyls: reworded to the outline's "brought them in bit by bit" (I3, AU 35552–35555).
- New, Augustine, gold of Egypt: I3, AU 51718–51722 (What came, To the card, line 78).
- Edicts: rewritten from the old McGiffert line (a modern note) to the book's own text. AN 10486 and AN 10684, with MI 4795–4796 for the Latin (I4, card).
- Calvin: kept.
- Removed as modern judgments only: Monceaux's "most exact … very partisan" and his "rarely named … read in the Middle Ages" (I4, I6; Leave out line 189).

**`legacy.remembered`.**
- Letter 58.
  - Old: "wishes he had been as ready to teach Christian doctrines as to pull down those of others".
  - New: "wishes he could have built up the faith as easily as he tore down that of others".
  - Evidence: JLL 27050–27052, *potuisset … facile*; Do not say line 172.
  - "Tully, meaning Cicero" stays (Cut first 20 to card).
- Letter 84: the Holy Spirit charge is explained in Jerome's own terms (JL 19203–19209; Cut first 7 and 22 to card), and "Gentiles" becomes "pagans".
- New, Letter 70: JL 16719–16721 (I1).
- Gelasius list.
  - Old: "A list later credited to Pope Gelasius … whether Gelasius wrote the list is disputed".
  - New: the heading's credit to Gelasius and the second copy under Hormisdas, with no modern verdict (I5; TE 11463–11486).
- Chronicle and millennium: kept.

**`uncertain`.** Twelve items, each from a sheet row. Every modern name and view is removed: Monceaux, Schanz, Brandt's dates for the address, McGiffert, Fletcher's Trier, the "Christian Cicero" and the editor's "Died 325".
1. One witness: Who tells it (Outline line 139); AN 4487.
2. Birthplace: S2; Do not say line 153.
3. Banquet: D4; TE 11186–11187 against JPL 59051–59052.
4. Name: S1, D1, and the Fresh_Read's tie, sent to the card (Fresh_Read line 69): DI-L 131, 5452–5454, 32648. "Lucius Caecilius" stands in MO 28684, the modern report of the one manuscript (D1).
5. Conversion: S8; AN 4567.
6. Whether he saw: E1; Do not say line 150.
7. Authorship: D1; JE 41047.
8. Palace fire: D2; AN 10185; EU 43982–43984, 70323–70325.
9. The address: D3; DI-L 286–289.
10. The two writers: E4. The Hierocles and Porphyry identifications are left off (Do not say line 155).
11. Crispus: E12.
12. Death: E12.

**`sources`.**
- `ownWords[1].disputed`: "most scholars hold the book Lactantius's" (a modern opinion) becomes "whether the book is Lactantius's is disputed".
- New `ownWords` item: *Persecutors* 48 in Latin (MI).
- `about`:
  - The Jerome Lives title widens to chapters 18, 79, 80 and 95 (JE 39882, 41022, 41266).
  - The Chronicle `date` changes from "about 380" (a modern reckoning) to null.
  - Jerome's letters now include 70.
  - New: Letter 58 in Latin (JLL), Lucifer (LU) and Socrates (SO).
  - The Eusebius title drops "and McGiffert's notes".
  - The Augustine title adds On Christian Teaching, Book 2.
- Moved to the entry's `modernWorks`, word for word (Entry fields below): the Coxe and Fletcher preface item, Monceaux and Schanz.

**`briefSources`** (new). The old sources the brief draws on: AN (Institutes; the *Persecutors* dream), DI-L, EU (the edict), JE 80, JL 58 and 84, JLL 58, JC, LU, SO.

**`briefReferences`.** Replaced with one item for each strand the brief tells, in the brief's order. Removed because the brief no longer tells them:
- the *Persecutors* 12–15 scenes and the fire;
- the Book I to VII summary with the six thousand years;
- Galerius's edict and the edict of Milan;
- Donatus and the families, and the dating by Monceaux and Schanz;
- Augustine;
- the McGiffert and Monceaux notes;
- V.4's three motives (Cut first 18).

**`quotationOriginals`.** One entry for each of the five quoted spans in the brief, in order. Each `printed` is Brandt's Latin, the text the outline renders from (Outline lines 83–97), with Fletcher's English as `englishPrinted`.
- Removed: the V.4 "Spurred on …" entry and the Chronicle "most eloquent" entry, which the brief no longer quotes.
- Q1, V.11.15: DI-L 24576–24579; AN 4899. The `uncertain` holds the rendering notes from Outline line 89. No `secondReading`.
- "the temple of God was overthrown.": DI-L 22775; AN 4487. Six words, so no `secondReading`.
- "by force and tortures.": DI-L 26072; AN 5136. `"checked at card"`.
- "in my presence, and to my grief,": DI-L 23206; AN 4567. No `secondReading`.
- Q3, V.19.22: DI-L 26240–26242; AN 5158. The `uncertain` holds the notes from Outline line 97. No `secondReading`.

**`timeline`** (new). Six periods, built after the brief from the sheet, the outline and the card. Every line names the work, the file and the lines.
1. **Date unknown.** S1–S4 and JE 41022–41041 (Cut first 2, 12 and 21 to card; Arnobius by name, Leave out line 186 to card).
2. **303.** E1–E5. The *Persecutors* scenes go to the card (Leave out line 182). The man in Phrygia (AN 4897) is marked "not said to be seen". The philosopher's dining is Cut first 13 to card.
3. **During and after the persecution.** E6–E8 and E10. The learned scorn of Scripture is Cut first 6 to card. Quote 2 and its aim are Cut first 24 to card, narrated from AN 556 and DI-L 191–209, with no quotation marks, since the rendering is not listed. The address is D3, and the Workmanship is E9.
4. **311 to 313.** E11. The years are worked from the consulships the book names (AN 10501, 10680–10682).
5. **Extreme old age.** E12 (Crispus's death is Cut first 23 to card) and the Chronicle's praise (Q-src 4). Jerome's list of books, with On persecution, is Leave out line 188 to card.
6. **After his death.** I1–I6. The Lucifer exile is Cut first 11 to card, glossed as the outline asks. "About 392" is worked from Jerome's own "fourteenth year of the Emperor Theodosius" (JE 38785). "Sixteenth century" for Calvin is Widely Accepted.

## Items sent to the card, and where they are

- Cut first, marked card. Each is on the card:
  - 1: `keyWorks[0]`, the timeline, `legacy.traces`
  - 2: timeline 1
  - 3: `keyWorks[1]`, timeline 3
  - 6, 10 and 24: timeline 3
  - 7 and 22: `legacy.remembered`, timeline 6
  - 11: timeline 6
  - 12, 13 and 21: timelines 1 and 2
  - 17: `keyWorks[2]`, timeline 4
  - 20: `legacy.remembered`
  - 23: timeline 5
- Leave out, marked card. Each is on the card: the *Persecutors* scenes, the address, the Banquet in Africa, the Grammarian, letters and lost books, Arnobius, On persecution, the Gelasian list, Calvin, Augustine's gold of Egypt, and the man in Phrygia.
- Leave out items that stay off the card, as marked:
  - Cut first 4 (Peter and Paul), 5 (philosophy destroys itself), 8 (Latin letters), 9 (the Chronicle's year), 14 (Diocletian's reign), 15 (the book on justice), 16 (the will sentence), 18 (the three motives) and 19 (Lucifer's pamphlet title, which appears only as the cited work in `sources` and references).
  - The Middle Ages and Renaissance line is Monceaux's judgment only (I6).
  - The "Coprianus" jibe goes to the Cyprian card (Leave out line 190).
- What came, To the card (Outline line 78): I3, I4, I5 and I6 are on it.
- Fresh_Read: the name tie between Lucius Caecilius and Lactantius is in `uncertain` item 4. The outline notes on Gaul and Sardinia are outline matters, not card matters.

## Claims not found

None on the card. Every claim on the card stands at its cited lines.

In the census entry (not edited), one claim was not found. The `legacy` sentence "A letter in his collected letters calls Lactantius 'an ancient doctor of the Church.'" is not in the held Calvin file (CA), and I found no other held source for it. I left it in place, and it is listed here.

## Entry fields (for release; the entry itself is not edited)

- **`teaser`.**
  - Old: "Nicomedia and Gaul, c. 303 to 325 CE: a teacher of Latin rhetoric who turned to writing when his pupils were few, and addressed his defense of the faith to Constantine."
  - New: "Nicomedia and Gaul, from 303 CE: a teacher of Latin public speaking who answered the Great Persecution with the Divine Institutes, holding that religion cannot be forced."
  - Why: the address to Constantine is disputed (D3; Do not say line 157), so it contradicts the card. 325 is an editor's year (D5).
  - The new teaser says no more than `knownFor` and the brief.
- **`why`.**
  - Old last sentence: "His Divine Institutes open with an address to Constantine."
  - New last sentence: "He answered the Great Persecution with the Divine Institutes, arguing the faith to educated pagans."
  - Why: D3, and the brief paragraph 2. The rest stands (JE 41035–41038).
  - Also: "taught rhetoric" becomes "taught Latin public speaking" (Words to explain). The sentence "Jerome says he was called to Nicomedia in the reign of Diocletian" carries Cut first 14 (Leave out), so it becomes "Jerome says he was called to Nicomedia." (JE 41035).
- **`floorNote`.**
  - Old: "He wished Lactantius had been as ready to teach Christian doctrine as to pull down other men's."
  - New: "He wished Lactantius could have built up Christian doctrine as easily as he pulled down other men's."
  - Why: Review B2; JLL 27050–27052.
- **`legacy`.**
  - Old: "He adds a wish that Lactantius had been as ready to teach Christian doctrines as to pull down those of others."
  - New: "He adds a wish that Lactantius could have built up Christian doctrine as easily as he pulled down that of others."
  - Same evidence as `floorNote`. The "ancient doctor" sentence is listed under Claims not found.
- **`dates`.**
  - Old: "c. 303-325".
  - New: "from 303".
  - Why: 325 is the NPNF editor's insertion and Fletcher's belief (S1, D5). `start`, `end` and `activeYear` only place the entry on the map and stay.
- **`relationsSummary`, `voices`, `sourcing`, `informalName`, `region`:** no conflict with the card. No change.
- **`modernWorks`** (new). Each work clarified an old text for the outline or the sheet. All are pre-1931 historical editions, translations or reference histories. The first three are moved from the card's `sources.about`, with title and author word for word.
  - `{"title": "Preface and notes to Lactantius, in Ante-Nicene Fathers, vol. 7 (A. Cleveland Coxe; William Fletcher's Introductory Notice)", "author": "A. Cleveland Coxe and William Fletcher", "year": "1886", "note": "The English translation of the Divine Institutes, On the Workmanship of God and Lord Hailes' On the Deaths of the Persecutors, with the editors' notes."}`
  - `{"title": "Histoire littéraire de l'Afrique chrétienne, volume 3, chapter on Lactance", "author": "Paul Monceaux", "year": "1905", "note": "A literary history of Christian Africa; its chapter on Lactantius reports the manuscripts of his books and the ancient notices of him."}`
  - `{"title": "Geschichte der römischen Litteratur, part 3, sections 752 to 762", "author": "Martin Schanz, Carl Hosius and Gustav Krüger", "year": "1922", "note": "A history of Latin literature; these sections cover Lactantius's works and their manuscripts."}`
  - `{"title": "L. Caeli Firmiani Lactanti Opera omnia, part 1: Divinae institutiones et Epitome (Corpus scriptorum ecclesiasticorum Latinorum 19)", "author": "Samuel Brandt (ed.)", "year": "1890", "note": "The Latin text of the Divine Institutes, with the readings of the manuscripts and the sources Lactantius drew on."}`
  - `{"title": "L. Caeli Firmiani Lactanti Opera omnia, part 2.1 (Corpus scriptorum ecclesiasticorum Latinorum 27.1)", "author": "Samuel Brandt (ed.)", "year": "1893", "note": "The Latin text of On the Workmanship of God and On the Anger of God, with the ancient witnesses to Lactantius."}`
  - `{"title": "Eusebius: Church History, Life of Constantine, Oration in Praise of Constantine (Nicene and Post-Nicene Fathers, Second Series, volume 1)", "author": "Arthur Cushman McGiffert (tr.)", "year": "1890", "note": "English translation of the Church History and of Constantine's Oration to the Assembly of the Saints."}`
  - `{"title": "Eusebii Pamphili Chronici canones, Latine vertit, adauxit, ad sua tempora produxit S. Eusebius Hieronymus", "author": "John Knight Fotheringham (ed.)", "year": "1923", "note": "The Latin text of Jerome's version of Eusebius's Chronicle."}`
  - `{"title": "Sancti Eusebii Hieronymi Epistulae, part 1 (Corpus scriptorum ecclesiasticorum Latinorum 54)", "author": "Isidor Hilberg (ed.)", "year": "1910", "note": "The Latin text of Jerome's Letters 1 to 70."}`
  - `{"title": "Luciferi Calaritani opuscula (Corpus scriptorum ecclesiasticorum Latinorum 14)", "author": "Wilhelm Hartel (ed.)", "year": "1886", "note": "The Latin text of Lucifer of Cagliari's pamphlets to the emperor Constantius."}`
  - `{"title": "Quellen zur Geschichte des Papsttums und des römischen Katholizismus, third edition", "author": "Carl Mirbt (ed.)", "year": "1911", "note": "A collection of source texts; it prints the Latin of the edict of Milan from On the Deaths of the Persecutors 48."}`
