# Card check: Clement of Alexandria (`clement-of-alexandria`)

Check pass on `clement-of-alexandria.card.json` and `Card_Edits.md`, against the final brief, `Outline.md`, `Review.md`, `Fresh_Read.md`, `Source_Sheet.md`, `Card.existing.json` and every cited file at its lines. No entry file (the census entry exists). Nothing was edited.

## Verdict

**FIX.** Fourteen exact changes below. None touches the brief or a quotation.

## What was checked

1. **Edits and fields against evidence.** Every timeline line, headline and note, and every `knownFor`, `shortDescription`, `datesNote`, `placeNote`, `keyWorks`, `legacy` and `uncertain` text, was re-read at its cited file and lines. All hold except the items under Fixes. No modern opinion, date or identification is stated as content. McGiffert's dates, the Clement VIII report, Wilson's "Most likely Pantaenus", Fremantle's 397 and "190–203", NP3's "Born about 160, died about 217" and Freese's notes are all kept off the card. The items Outline line 122 sends to the card are all handled (datesNote, the McGiffert `uncertain` items and `remembered` line, the Coxe/Wilson credit, `dates`, the Latin of Letter 70). Every Cut first item marked Card is on the card (1, 2, 4, 5, 6, 8, 9, 11, 12). Leave out's S4/D2, T14/T15/I5 and D7 are on it. **Missing:** Leave out's T18 (disputed books, Tatian, the Jewish writers), marked "card", and Links/L8 (Tatian, "card"). See F7.
2. **Kept fields word for word.** `otherNames`, `role`, `keyWorks[0].title`, `keyWorks[1].title`, `legacy.traces` "His Stromata keep words from the letters of Valentinus.", `legacy.remembered[0]`, `sources.ownWords[0]` and the Jerome Lives 38 and Letter 70 (Fremantle) items in `sources.about` match `Card.existing.json` exactly. Nothing unlisted moved.
3. **`briefReferences`.** Each of the fifteen names something the brief tells. The removed items (Pantaenus named, "bare faith alone", "around the year 200", Wilson's note) are rightly gone.
4. **Census rules.** The validator ran on a census copy kept outside the repository (card in place, brief as `longDescription`, placeholder `secondReading` on the three long quotations), with `--skip-quotes`: 0 errors. Every key is allowed. There are six `quotationOriginals` for the six quoted spans in the brief, and none for a dropped span. Each `printed` is verbatim at its lines: ANF2 27489-27492 (footnote left out), 32107, 27890-27893; EUS 33614, 34354; JERL 35367-35368. `englishPrinted` is verbatim at JER 16634-16636. The Greek `original` "τὸν ἱερὸν Κλήμεντα" stands at EUSG 3050 (checked by hand). EUSG 2403 reads "μαχαρίου", a damaged scan, so the English rightly stands alone. Q3 is rendered from the held Latin, and the card carries it. Every cited file is in `sources`. No audit is named. American spelling is used.
5. **"Checked at card."** "us, the simple," is the printed English word for word (ANF2 32107). "the blessed presbyter." is the printed English (EUS 33614). "the holy Clement," renders ἱερὸν as holy, and McGiffert's print agrees (EUS 34354; EUSG 3050). All three pass.
6. **Not found / clearly wrong.** None was listed as not found, and none was found. The items left wrong are F1, F2, F9 and F10.
7. **Entry fields.** `teaser` = `knownFor` and holds against the brief. `dates` "late 2nd-early 3rd c." follows the Setting (Outline line 16), and `start`/`end`/`activeYear` stay. Each `modernWorks` note says what the work covers. The list is incomplete; see F14.
- **Readability** (re-run on the same running text, on a plain file outside the repository): `clement-card-text.txt: 1958 words, grade 8.8 (names out 6.6), reading ease names out 74.7, 15.1 words a sentence, 0.3 joining words per 100, 27% short sentences, longest sentence 40 words - pass`

## Fixes (field, old text, new text)

**F1. `timeline[2].when`.** The period heading dates the whole period, but Eusebius dates only the first book of the Miscellanies (EUS 33080-33086). The period also holds the Exhortation, the Instructor and the Outlines, which no source dates. That is a date moved onto the wrong event.
- Old: `In the reign of Severus, by Eusebius's dating of the first book`
- New: `Date unknown; Eusebius dates the first book of the Miscellanies to the reign of Severus`

**F2. `timeline[0].lines[1].text`.** Clement gives no names (ANF2 27483-27487), and the next line's note says so.
- Old: `He names teachers in Greece, in southern Italy and in the East,`
- New: `He tells of teachers in Greece, in southern Italy and in the East,`

**F3. `timeline[2].lines[4].text`.** "Answers" leans on the line before it. Stromata I.5 (ANF2 27885-27893) is not set against the masks passage (VI.10) in the source.
- Old: `He answers that God is the cause of all good things,`
- New: `He writes that God is the cause of all good things,`

**F4. `timeline[2].lines[8].text`, and `briefReferences[7]`.** "These teachings" has no referent when the line is read alone (ANF2 52954-52962: "those who invented the heresies").
- Old (timeline): `He writes that the founders of these teachings arose in the time of the emperor Hadrian,`
- New: `He writes that the founders of the teachings he opposed arose in the time of the emperor Hadrian,`
- Old (briefReferences[7]): `Stromata VII.17: the founders of these teachings arose under Hadrian.`
- New: `Stromata VII.17: the founders of the teachings he opposed arose under Hadrian.`

**F5. `timeline[2].lines[11].text`.** "Judaizers" is named without the explanation Part 1 requires, and the held lines give no plain gloss that is not a judgment.
- Old: `and one against the Judaizers dedicated to the bishop Alexander.`
- New: `and one dedicated to the bishop Alexander.`

**F6. `timeline[2].lines[12].text`.** "The disputed books" is unexplained (EUS 34275-34278: "all canonical Scripture, not omitting the disputed books").
- Old: `he gives short accounts of all of Scripture, the disputed books too.`
- New: `he gives short accounts of all of Scripture, even the books whose place in it was disputed.`

**F7. `timeline[2].lines`: add a line after `lines[11]`** (the line on Eusebius's list of his other books). This is Leave out T18 and Link L8, both marked "card" (EUS 34128-34129, 34152-34153, 34182-34199).
- New line: `{"when": "Date unknown", "text": "Eusebius says that in these books he also cites books whose place in Scripture was disputed, names Tatian's Discourse to the Greeks, and refers to Jewish writers, among them Philo and Josephus.", "reference": "Eusebius, Church History VI.13.6-7, cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml lines 34128-34199"}`

**F8. `timeline[3].lines[0].text`.** "The Thebaid" is unexplained. The source's "from Egypt and all Thebais" (EUS 32430-32431) is all Egypt, as Outline Beat 5 gives it.
- Old: `believers from Egypt and all the Thebaid are brought to Alexandria`
- New: `believers from all over Egypt are brought to Alexandria`

**F9. `timeline[5].lines[0].text` and `legacy.traces[3]`.** The cited Preparation IV.16 passage (PE 10836-10919) is on human sacrifice, not on the mysteries (PE 10790-10850).
- Old (both): `on the pagan mysteries into his Preparation for the Gospel`
- New (both): `on the pagan mysteries and on human sacrifice into his Preparation for the Gospel`

**F10. `timeline[5].lines[1].reference`.** In Holl, "Κλήμης τε, (ὃν" stands at 33699 and "φασί τινες … Ἀθηναῖον" at 33700.
- Old: `lines 32964-32966, 33697-33699`
- New: `lines 32964-32966, 33699-33700`

**F11. `sources.about[0].title`.** The timeline cites Church History V.9 (EUS 28467-28469).
- Old: `Church History, Book 5 chapters 10 and 11; Book 6 chapters 1, 3, 6, 11, 13 and 14`
- New: `Church History, Book 5 chapters 9, 10 and 11; Book 6 chapters 1, 3, 6, 11, 13 and 14`

**F12. `briefSources[0].title`.** The brief's "guide" gloss draws on Instructor I.7 (`briefReferences[3]`).
- Old: `The Stromata (Miscellanies), in Ante-Nicene Fathers vol. 2`
- New: `The Stromata (Miscellanies) and The Instructor, in Ante-Nicene Fathers vol. 2`

**F13. `briefSources`: add after the Eusebius Greek item.** `briefReferences[1]` cites Jerome's Lives 38 for the brief's "presbyter".
- New item: `{"title": "Lives of Illustrious Men, chapter 38", "author": "Jerome", "file": "cic/texts/npnf203_theodoret-jerome-gennadius-rufinus.xml"}`

**F14. Entry `modernWorks` (under Entry fields in `Card_Edits.md`): add.** The outline used Migne's editions (Who tells it; M6) and ANF1 (Outline lines 8, 63, 93) to clarify old texts. The card's `sources` name Holl's and Fotheringham's editions, as they name Schwartz's and Hilberg's, which are listed. All five are pre-1931 and held. The Holl item is the census's existing wording, word for word.
- `{"title": "Patrologia Graeca, vol. 83", "author": "J.-P. Migne (ed.)", "year": "1864", "note": "Greek and Latin edition of works of Theodoret of Cyrrhus, among them the Compendium of Heretical Fables."}`
- `{"title": "Patrologia Latina, vol. 23", "author": "J.-P. Migne (ed.)", "year": "1883", "note": "Latin edition of works of Jerome, among them the Lives of Illustrious Men."}`
- `{"title": "Epiphanius, erster Band: Ancoratus und Panarion haer. 1-33 (Die griechischen christlichen Schriftsteller 25)", "author": "Karl Holl (ed.)", "year": "1915", "publisher": "J. C. Hinrichs, Leipzig", "note": "The Greek text of the Ancoratus and of Panarion 1 to 33, with notes on the text, the biblical allusions and the date of the Panarion."}`
- `{"title": "Eusebii Pamphili Chronici canones, Latine vertit, adauxit, ad sua tempora produxit S. Eusebius Hieronymus", "author": "John Knight Fotheringham (ed.)", "year": "1923", "note": "The Latin text of Jerome's version of Eusebius's Chronicle."}`
- `{"title": "The Apostolic Fathers, Justin Martyr, Irenaeus (Ante-Nicene Fathers, volume 1)", "author": "Alexander Roberts and James Donaldson (eds.), with notes by A. Cleveland Coxe", "year": "1885", "note": "English translation of Irenaeus's Against Heresies, among other works."}`

The `Card_Edits.md` note "The card's `sources` listed no modern work, so none moves" stands.
