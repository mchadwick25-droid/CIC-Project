# Card check: Origen (`origen`)

Checker did not write the card. I read `CLAUDE.md` ("Trust and source fidelity"), Kit Part 1, the person kit, the role, the four era 1 Header sections, the brief, `Outline.md`, `Fresh_Read.md`, `Fresh_Applied.md`, `origen.card.json`, `Card_Edits.md`, `Card.existing.json` and the census entry. I re-read every timeline line and headline at its cited file and lines. Card running text scorer (plain file outside the repository): `card_text.txt: 3054 words, grade 9.7 (names out 7.6), reading ease names out 71.7, 17.6 words a sentence, 0.4 joining words per 100, 14% short sentences, longest sentence 36 words - pass`.

## Verdict: FIX

Six changes, each exact below. Everything not named here passes. That covers the timeline lines and headlines against their lines, the three `printed` spans (PHIL 74; EUS 35122-35124; A9 24729-24732, verbatim), the keys, `briefReferences`, the kept fields and the readability line.

## Fixes

**1. `legacy.remembered`: Evagrius left off on a wrong ground (check 1).** The outline sends "the rest of the 553 dispute (Evagrius, the special anathemas, Hefele): card" (Leave out). `Card_Edits.md` drops Evagrius because the Walford English is a damaged scan. But a readable Greek print is held: `cic/texts/evagrius-scholasticus_historia-ecclesiastica-grc_bidez-parmentier1898.txt`, IV.38, lines 17551-17618. I read it by hand. It has the monks' petitions κατὰ τῶν Ὠριγένους τοῦ καὶ Ἀδαμαντίου δογμάτων (17551-17552), and Ἀναφορὰ ... πρὸς Ἰουστινιανὸν παρὰ τῆς συνόδου μετὰ τὰς γενομένας παρ' αὐτῆς ἐκβοήσεις κατὰ Ὠριγένους καὶ τῶν τὰ αὐτὰ ἐκείνῳ πεπλανημένων (17588-17593). It also has Τούτοις συνέζευξαν καὶ τὰ κεφάλαια τὰ ὅσα πρεσβεύειν οἱ τὰ Ὠριγένους δοξάζοντες ἐδιδάχθησαν (17615-17617). The Walford English agrees where it can be read (9620-9647: "exclamations against Origen", "they appended a statement of the heads"). "Special anathemas" is not his wording, so the line gives what he says.
- After the remembered line "About three centuries after his death, a council at Constantinople named Origen in its eleventh anathema, ...", insert:
  "The church historian Evagrius Scholasticus says that monks petitioned the council against Origen's teachings. He says the council sent the emperor Justinian a report after crying out against Origen and those who shared his errors, and attached chapters setting out what Origen's followers had been taught to hold."
- `sources.about`, new entry after "Anathemas of the Fifth Council": `{"title": "Church History, Book IV, chapter 38", "author": "Evagrius Scholasticus", "date": null, "language": "Greek", "file": "cic/texts/evagrius-scholasticus_historia-ecclesiastica-grc_bidez-parmentier1898.txt"}`
- Entry `modernWorks`, add: `{"title": "The Ecclesiastical History of Evagrius with the Scholia", "author": "J. Bidez and L. Parmentier (eds.)", "year": "1898", "publisher": "Methuen, London", "note": "Greek text of Evagrius's Church History, which tells of the council at Constantinople and its acts on Origen."}`

**2. `uncertain` 12: a modern work named outside `modernWorks` (check 1).**
- Old: "Whether Origen's name stood in the council's eleventh anathema from the first is a question raised by modern scholars, not by the old sources used here. Hefele's History of the Councils, under Modern works, sets it out."
- New: "Whether Origen's name stood in the council's eleventh anathema from the first is a question raised by modern scholars, not by the old sources used here."

**3. `uncertain` 8: the Jerome half dropped as "not found", but it is held (check 6).** Jerome, Apology against Rufinus III.36, `cic/texts/npnf203_theodoret-jerome-gennadius-rufinus.xml` lines 56003-56011: "You say that you cut off anything that was offensive and replaced it by what was better. I have represented things just as they stood in the Greek." A held line supports this wording, so it may be kept. Without it the open question has one witness only.
- Old: "We read On First Principles mostly in Rufinus of Aquileia's Latin. Rufinus says in his preface that wherever he found anything on the Trinity contrary to what Origen taught elsewhere, he left it out or set it down in words that agree with the rule of faith."
- New: "We read On First Principles mostly in Rufinus of Aquileia's Latin. Rufinus says in his preface that wherever he found anything on the Trinity contrary to what Origen taught elsewhere, he left it out or set it down in words that agree with the rule of faith. Jerome, who made his own translation, says Rufinus cut out what gave offense, while he himself set the books down just as they stood in the Greek."
- `sources.about`: leave "Preface to Job; Against John of Jerusalem" (npnf206) as it is, and add `{"title": "Apology against Rufinus, Book III", "author": "Jerome", "date": null, "language": "English translation", "file": "cic/texts/npnf203_theodoret-jerome-gennadius-rufinus.xml"}`

**4. `uncertain` 7: a modern identification (check 6).** Eusebius names only "Gallus" (EUS 39146-39163), and the datesNote says "Gallus".
- Old: "Eusebius of Caesarea says Origen died in the time of the emperor Trebonianus Gallus, at sixty-nine."
- New: "Eusebius of Caesarea says Origen died in the time of the emperor Gallus, at sixty-nine."

**5. Timeline notes that bring in a new witness with no reference (card standard: every line with its reference).** The Hebrew note already carries one. Give the others theirs:
- Decius line, note. Old: "Jerome says Decius was mad against the religion of Philip, whom he had killed." New: "Jerome says Decius was mad against the religion of Philip, whom he had killed (Lives of Illustrious Men 54; cic/texts/npnf203_theodoret-jerome-gennadius-rufinus.xml lines 40576-40579)."
- Ordination line, note. Old: "Jerome says he was going to Athens for the churches of Achaia, with a church letter; Photius, summarizing Pamphilus, says he went without his bishop's permission." New: "Jerome says he was going to Athens for the churches of Achaia, with a church letter (Lives of Illustrious Men 54; cic/texts/npnf203_theodoret-jerome-gennadius-rufinus.xml lines 40532-40538); Photius, summarizing Pamphilus, says he went without his bishop's permission (Library 118; cic/texts/photius_library-v1_freese1920.txt lines 11480-11484)."
- Death line, note. Old: "Photius says Pamphilus and others wrote that he died a martyr at Caesarea under Decius." New: "Photius says Pamphilus and others wrote that he died a martyr at Caesarea under Decius (Library 118; cic/texts/photius_library-v1_freese1920.txt lines 11449-11454)."

**6. Epiphanius timeline note: a judgment no source makes.** Eusebius tells no incense story, so "against Eusebius's account" is the card's own verdict.
- Old: "A hostile account written more than a century after his death, against Eusebius's account."
- New: "A hostile account written more than a century after his death."

## Rulings asked for

- **The four "not found" claims.**
  - (a) Evagrius on "special anathemas": the "not found" is wrong in its ground. A readable Greek print is held, and the outline sends Evagrius to the card. Carry it as his own content (Fix 1).
  - (b) "Jerome said Rufinus changed it": held at NP3 56003-56011. Restore it (Fix 3).
  - (c) Entry `legacy`, Jerome "later called his teachings poison": held. Jerome, Apology against Rufinus III.25, NP3 55572-55576, speaks of "Origen's poisoned dish" in Rufinus's translation of Περὶ Ἀρχῶν. III.36, NP3 56014-56015, has "the subtle errors of Origen, and make known the poison of the heretics". The entry line stands, and no conflict with the card.
  - (d) Entry `why`, "wrote on almost every book of the Bible": not found. I searched EUS, NP3, J6 and PHO. The proposed new `why` drops it, and that change passes.
- **The proposed entry `floorNote`.** The conflict is real. Anathema XI (N14 23852-23860) curses Origen "as well as their impious writings" among the heretics. It does not condemn "his bolder ideas". The proposed text passes as written: "His own faith is not in question here. His books were attacked long after his death, and about three centuries later a church council named him, with his writings, among the heretics."
- **Porphyry's quotation in English alone.** This is correct. The only held Greek witness of HE VI.19.8 is Schwartz-Mommsen (EUSG 3594-3602). That is a damaged scan ("μυστηρίο)ν", "τρύπον", "ταις Ιουδαϊχαῖς"). I searched the whole of `cic/texts/` for Κορνούτου and found no other Greek print. McGiffert's notes give only the name Κορνοῦτος (35122), and Harnack's Chronologie (1904, line 2045) gives German only. So no `original` is given, and `uncertain` 13 says so plainly.

## Other entry fields

- `dates` "3rd c.", `teaser`, `why`, `relationsSummary`: these pass as proposed.
- `modernWorks`: passes as proposed. Hefele's note says what the book covers, not what it argues. Add the Bidez-Parmentier entry (Fix 1).
- `voices` and `sourcing`: no conflict.
