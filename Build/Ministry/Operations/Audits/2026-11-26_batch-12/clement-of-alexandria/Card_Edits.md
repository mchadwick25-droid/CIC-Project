# Card edits: Clement of Alexandria (`clement-of-alexandria`)

A full new card (batch header, "The card"), written to `clement-of-alexandria.card.json` beside this file. Built under "A new card": every field sourced afresh from `Source_Sheet.md` (rows cited S, E, T, I, D, M), `Outline.md` at its lines, or the final brief `clement-of-alexandria.brief.txt`. The starting card (`Card.existing.json`, identical to the census `card` today) was a pointer only. Every cited line below was re-read in its file. Short names as in the source sheet: ANF2, EUS, EUSG, NP3, JER, JERL, PE, CHR, HO (Holl), THD, PHO, ANF1 (all under `cic/texts/`).

Line corrections against the source sheet, found on re-reading: the Greek of "the holy Clement" stands at EUSG 3050 (sheet: within 3044-3052); Eusebius VI.6 in the Greek stands at EUSG 1839-1843 (sheet: 1840-1841); the Exhortation line on idolatrous images is chapter 6.

Readability of the card's running text (short description, knownFor, datesNote, placeNote, key works, legacy, open questions, timeline headlines, lines and notes), on a plain file outside the repository:
`clement-card-text.txt: 1958 words, grade 8.8 (names out 6.6), reading ease names out 74.7, 15.1 words a sentence, 0.3 joining words per 100, 27% short sentences, longest sentence 40 words - pass`

Census validator (`tools/validate-census.mjs --skip-quotes`) on a census copy outside the repository, with this card and the brief as `longDescription`, and a placeholder `secondReading` on the three long quotations: 0 errors. Every quoted span in the card's prose and every `printed`, `original` and `englishPrinted` was checked separately against its file and lines with the validator's folding: all found. The full quote check was not run here (the brief's own quotations need their listings in `tools/quote_renderings.json`, which release makes; the census's nine old listings for this entry will no longer match the new brief).

## Fields kept from the starting card

| Field | Kept wording | Evidence |
|---|---|---|
| `otherNames` | "Titus Flavius Clement" | EUS 33869-33870, Eusebius VI.13.1: "Titus Flavius Clement's Stromata" (T9) |
| `role` | "Teacher and presbyter" | S1 (EUS 33614; NP3 40249-40250); S3 (EUS 33040-33043) |
| `keyWorks[0].title`, `keyWorks[1].title` | "Exhortation to the Greeks"; "The Instructor" | T11, T12, T13 (EUS 33985-34004) |
| `legacy.traces` | "His Stromata keep words from the letters of Valentinus." | T16, ANF2 34289-34291; brief: "He copied words from Valentinus's own letters into his book in order to answer them." |
| `legacy.remembered` | "Alexander of Jerusalem called him \"the blessed presbyter, a man virtuous and approved.\"" | EUS 33614 (E15); Alexander as bishop at Jerusalem, EUS 33505-33521 |
| `sources.ownWords[0]` | title, file and language as they stood | ANF2 (Source_Sheet line 6) |
| `sources.about` | the Jerome Lives 38 and Letter 70 (Fremantle) items, word for word | NP3 40245-40279; JER 16475-16642 |

## Changed or new, field by field

**`knownFor`.** Old: "Presbyter and teacher at Alexandria, who held that Greek philosophy prepared the way for Christ and taught Origen." New: "Presbyter, an elder of the church, and teacher at Alexandria, who held that Greek philosophy prepared the way for Christ; Eusebius says Origen was among his pupils." Why: Origen is told only as Eusebius says it (batch header, slate; brief: "Eusebius of Caesarea, writing about a century later, says Origen was among his pupils"; E7, EUS 33043-33044, 33079-33080). Presbyter glossed where first met (Outline line 21; S1). "Prepared the way" kept: ANF2 27893-27894, "Philosophy, therefore, was a preparation, paving the way".

**`shortDescription`** (new): "Clement was a Christian teacher and a presbyter, an elder of the church, at Alexandria in Egypt, late in the second century and into the third. He wrote that Greek philosophy may have been given to the Greeks to bring them to Christ, as the Law of Moses brought the Hebrews." Evidence: brief paragraph 2 ("Alexandria in Egypt became Clement's own city, late in the second century and into the third. There he taught, and he served as a presbyter, an elder of the church"); Quote 2, ANF2 27890-27893, with Clement's "Perchance" kept as "may have been" (Outline line 89); the Law given through Moses, ANF2 31207-31208 (Outline line 25).

**`datesNote`.** Old: "Writing about 190 to 202; last heard of about 212". New: "No old source gives the year of his birth or of his death. The first book of his Miscellanies counts the years to the death of the emperor Commodus, in 192, so Eusebius dates it to the reign of Severus. Jerome says he flourished under Severus and his son Antoninus. Alexander's letter to Origen, the last word of him, gives no year." Why: the old years rest only on McGiffert (M1; Outline line 122), which Part 1 keeps off the card. Evidence: E17; S6 (ANF2 30602-30604; EUS 33079-33086); Commodus's death in 192 is Widely Accepted (Outline line 16); S8 (NP3 40278-40279); E16 (EUS 34330-34356).

**`placeNote`.** Old: "Alexandria; later with the imprisoned bishop Alexander, and at Antioch". New: "Alexandria, in Egypt, where he was trained, taught and served as a presbyter; later with the bishop Alexander, then in prison, at a place no source names; and Antioch, in Syria, whose church received the letter he carried for Alexander". Why: the prison's place is not given (E14; Outline line 17, 84), and the old wording could be read as placing the prison; Antioch is where the letter went, not a stay the sources tell. Evidence: S2, S3, S1; E14, E15 (EUS 33597-33617); Outline Setting, line 17 ("Antioch, in Syria, receives the letter he carries").

**`keyWorks[0].about`.** Old: "a call to leave the old gods". New: "a call to the Greeks to leave their idols for the Word, Christ, whom he calls the New Song". Evidence: T11, ANF2 15279-15282 ("he has been called by me the New Song"), ANF2 17079 ("fill up life with idolatrous images"); Outline line 27.

**`keyWorks[1].about`.** Old: "three books on how a Christian should live". New: "three books on Christ, the Word, as the Instructor who leads the children, with rules for behavior and conduct". Evidence: T12, ANF2 19937-19946 ("the Instructor, who leads the children"); EUS 34004 ("three books"); PHO 11116-11117 ("rules for behaviour and conduct").

**`keyWorks[2]`.** Old title "Stromata", about "\"Gnostic Notes on the True Philosophy,\" on faith, knowledge and Greek learning". New title "Miscellanies (Stromata)", about "eight books of notes, patched together, he said, passing from one thing to another. Eusebius says they treat Scripture, quote the Greek writers wherever they seemed useful, and answer false teachers". Why: the brief names the book "the Miscellanies"; "Gnostic" stood unexplained (Outline line 78). Evidence: T8, ANF2 37560-37563; T9, EUS 33866-33870, 34114-34126.

**`legacy.traces`.** Old first line "Jerome of Strido, in his Lives of Illustrious Men, says Origen was his pupil." New: "Eusebius of Caesarea says Origen was among his pupils, and Jerome that Origen is known to have been his disciple." (E7; E8, NP3 40277-40278; census name "Jerome"). New lines: "Jerome says Origen, imitating his example, wrote ten books of Miscellanies that compare the views of Christians and of philosophers." (I2, JER 16636-16640; Outline line 46, Jerome's claim credited); "Eusebius copied passages of his Exhortation to the Greeks on the pagan mysteries into his Preparation for the Gospel, calling him \"the admirable Clement\"." (I3, PE 4946-4951, 10834-10837, 10919; Outline Cut first 1, to the card); "About two centuries after him, Jerome answered a critic who charged him with defiling the church by quoting pagan books. He named Christian writers who had done the same, Clement among them." (I2, JER 16477-16480, 16626-16629; brief's last paragraph).

**`legacy.remembered`.** Removed: "Arthur McGiffert, who translated Eusebius of Caesarea, notes that he was long honored as a saint, and that Pope Clement the Eighth removed his name from the list because his teaching was suspected." (modern only, M1; Outline line 85 and 122). New lines: Alexander's "the holy Clement, my master and benefactor" (E16, EUS 34354-34355); Jerome's "in my judgment the most learned of men" and his question (I2, JER 16628-16636); Jerome's Chronicle (I6, S7, CHR 43374-43377); Epiphanius (I7, HO 32964-32966); Theodoret (I4, THD 27950-27952, 29659-29661); Photius (I5, PHO 11084-11085, 11105-11106, 11132-11133, 11163). All sent to the card by Outline line 48.

**`uncertain`.** All four old items replaced. Old 1 ("Little of his life is known beyond his own books, a few chapters of Eusebius of Caesarea and one of Jerome of Strido.") becomes "The witnesses", worded on D5 and the brief ("In Eusebius's account, which holds most of what is told of his life"). Old 2 (the "Sicilian bee") becomes "The hidden teacher": "Sicilian bee" stood unexplained; same facts, E2, E3, E4, D1 (EUS 28697-28704, 33981-33983). Old 3 and old 4 are removed as McGiffert's claims (M1; Outline line 122); old 3's sound part, that Eusebius names no one among those driven away, stays as "Leaving Alexandria" (E10, D3, EUS 32670-32673). New items: "Taking over the teaching" (S3, S4, D2); "Origen as a pupil" (E7; EUS 33043-33050; EUSG 1839-1843 and apparatus 1883-1885; Outline line 92); "Birth and death" (E17; D7, HO 33697-33699); "The persecution" (E9, E11, E12, Outline lines 41, 72, 87); "The groups he answered" (T1, T2, T17; Irenaeus, ANF1 30761-30763, Outline lines 8, 93; Cut first 4 sends "bare faith alone" to the card); "Alexander" (E14; EUS 33505-33521; Outline line 84); "The Outlines" (T15, D4, PHO 11105-11106; Outline line 103).

**`sources.about`.** Eusebius English: title widened to "Book 5 chapters 10 and 11; Book 6 chapters 1, 3, 6, 11, 13 and 14" (VI.1 added, E9). New items, each a file the card cites: Eusebius's Greek (EUSG), Alexander's letters (EUS 33597-33617, 34330-34356), Jerome's Latin of Letter 70 (JERL), Jerome's Chronicle (CHR), Eusebius's Preparation (PE), Epiphanius's Panarion (HO), Theodoret's Compendium (THD), Photius's Library (PHO), Irenaeus, Against Heresies I.6.2 (ANF1).

**`briefSources`** (new): Stromata (ANF2); Eusebius, Church History with Alexander's letters (EUS); Eusebius's Greek of VI.6 (EUSG, for "among his pupils"); Jerome, Letter 70 in Latin (JERL, Quote 3) and in Fremantle's English (JER).

**`briefReferences`.** All sixteen old items replaced, one per strand the brief tells, in its order. Removed as no longer told: Eusebius V.11 naming Pantaenus; Wilson's note (the note is Coxe's, Outline line 122, and is not used); "bare faith alone" and the vine; Stromata I.21 "around the year 200"; Eusebius VI.6 "Origen his pupil" with Jerome's Lives (Jerome's Lives now only for "presbyter").

**`quotationOriginals`.** One entry for each of the brief's six quoted spans, in its order. Removed: "in my judgment the most learned of men", "Is learning missing…", "bare faith alone", "whatever has been well said" (the brief no longer quotes them).
- Q1, Stromata I.1: printed ANF2 27489-27492 (the footnote in the line is an editor's note, left out). `uncertain` on "first in power", from Eusebius's English quoting Clement, EUS 28756-28757 (Outline line 50). No `secondReading` (six words or more).
- "us, the simple,": ANF2 32107. `"checked at card"`.
- Q2, Stromata I.5: printed ANF2 27890-27893. `uncertain`: "guide" for "schoolmaster", from Clement's own sense, ANF2 19937-19938, and Paul's word, marked at 27893 (Outline line 26, 51); the Law, ANF2 31207-31208. The old note's credit to Wilson is dropped (Outline line 122). No `secondReading`.
- "the blessed presbyter.": EUS 33614. The Greek (EUSG 2403) is a damaged scan ("μαχαρίου"), so the English stands alone. `"checked at card"`.
- "the holy Clement,": EUS 34354; original "τὸν ἱερὸν Κλήμεντα", EUSG 3050, checked by hand (legible in the scan; McGiffert's English confirms). `"checked at card"`.
- Q3, Jerome Letter 70.4: rendered from the Latin (Outline line 52), so `printed` is the Latin, JERL 35367-35368, with Fremantle's English as `englishPrinted`, JER 16634-16636. The old "(no Latin held)" was wrong (Outline line 122). No `secondReading`.

**`timeline`** (new; six periods, built after the brief from the source sheet, outline and card; every line's reference names work, file and lines):
1. Date unknown, "Searching for teachers, and rest in Egypt" (Clement): E1, E2, E3 (note: Eusebius's judgment, E4), E5.
2. "In the time of the emperors Commodus and Severus", "Trained, teaching and serving as a presbyter at Alexandria" (Eusebius): S2 with V.9's Commodus (EUS 28467-28469); S3 (note: Jerome, S4/D2); E7 (note: the Greek reading); S1 (note: Alexander's word).
3. "In the reign of Severus, by Eusebius's dating of the first book", "The Miscellanies and his other books" (Clement): S6, T8, T1, T2, T3, T5, T17 (note: Irenaeus), T16, T19, T11, T12, T13, T14.
4. "Under the emperor Severus, by Eusebius's account; Clement's own words undated", "Persecution, and martyrs every day": E9, E10 (note: Clement not named), E11 (note: not tied to Severus, Outline line 87), E13, E12.
5. "Date unknown; when the church at Antioch had a new bishop", "With Alexander, a bishop in prison" (Alexander): E14 (note: no reason or place; Cappadocia and Jerusalem, EUS 33505-33521), E15, E16 (note: the last word of him).
6. "After his time", "Read, copied and judged by later writers": I3, I7, I6, E8 with S8, I2, I4, I5. The gaps ("about a century", "about 175 years", "about two centuries", "about 250 years", "about 650 years") are the source sheet's own (rows I3-I7, D5).
Not on the timeline: the faith-and-knowledge lines (T6, T7; Outline line 106, they need "gnostic"); the river of truth (T4); McGiffert's dates and the Clement VIII report (M1).

## Entry fields (for release; the entry itself is not edited)

- **`teaser`.** Old: "Presbyter and teacher at Alexandria, who held that Greek philosophy prepared the way for Christ and taught Origen." New: "Presbyter, an elder of the church, and teacher at Alexandria, who held that Greek philosophy prepared the way for Christ; Eusebius says Origen was among his pupils." Same evidence as `knownFor`; it says no more than `knownFor` and the brief.
- **`dates`.** Old: "c. 190-212". New: "late 2nd-early 3rd c." Why: 190 and 212 are McGiffert's reckoning (M1; Outline line 122); the brief and Setting give "late in the second century and into the third" (Outline line 16). `start`, `end` and `activeYear` (190, 212, 202) only place the entry on the map and stay.
- **`modernWorks`** (new; none is cited on the card; each the outline used to clarify an old text):
  - {"title": "Fathers of the Second Century: Hermas, Tatian, Athenagoras, Theophilus, and Clement of Alexandria (Ante-Nicene Fathers, volume 2)", "author": "William Wilson (tr.), with notes by A. Cleveland Coxe", "year": "1885", "note": "English translation of Clement's Exhortation, Instructor and Miscellanies, with the editor's notes on words such as pedagogue."}
  - {"title": "Eusebius: Church History, Life of Constantine, Oration in Praise of Constantine (Nicene and Post-Nicene Fathers, Second Series, volume 1)", "author": "Arthur Cushman McGiffert (tr.)", "year": "1890", "note": "English translation of the Church History, with notes on its manuscripts and readings."}
  - {"title": "Eusebius Werke, Zweiter Band: Die Kirchengeschichte, Zweiter Teil: Die Bücher VI bis X", "author": "Eduard Schwartz (ed.)", "year": "1908", "note": "The Greek text of Books 6 to 10 of the Church History, with the readings of the manuscripts."}
  - {"title": "Jerome: The Principal Works of St. Jerome (Nicene and Post-Nicene Fathers, Second Series, volume 6)", "author": "W. H. Fremantle (tr.)", "year": "1893", "note": "English translation of Jerome's letters, Letter 70 among them."}
  - {"title": "Sancti Eusebii Hieronymi Epistulae, pars I: Epistulae I-LXX (Corpus Scriptorum Ecclesiasticorum Latinorum, volume 54)", "author": "Isidor Hilberg (ed.)", "year": "1910", "note": "The Latin text of Jerome's first seventy letters, with the readings of the manuscripts."}
  - {"title": "Eusebius, Preparation for the Gospel, Books 1 to 9", "author": "Edwin Hamilton Gifford (tr.)", "year": "1903", "note": "English translation of the Preparation, which copies passages of Clement's Exhortation."}
  - {"title": "The Library of Photius, volume 1", "author": "J. H. Freese (tr.)", "year": "1920", "publisher": "Society for Promoting Christian Knowledge", "note": "English translation of Photius's book notices, among them three of Clement's works."}
  All are pre-1931 and held in `cic/texts/` (rights lines in each file's header). The card's `sources` listed no modern work, so none moves.
- **`longDescription`**: the final brief, final newline removed (release).
- No `why`, `relationsSummary`, `sourcing`, `voices` or `legacy` field is on the entry, so no conflict with the card.

## Claims not found

None. Every kept or new claim stands on a line cited above. "In Syria" for Antioch and Commodus's death in 192 rest on the outline's Setting (lines 16-17), as Widely Accepted.

## Left for the checker

- The three quotations under six words carry `"checked at card"`; their renderings are verbatim English spans of the printed lines.
- The three long quotations carry no `secondReading`, as the role says; the validator needs one before release.
