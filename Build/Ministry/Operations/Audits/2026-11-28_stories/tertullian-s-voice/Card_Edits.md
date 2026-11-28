# Card edits: Tertullian

Card: `tertullian-s-voice.card.json` (starting card: the `card` of `tertullian-s-voice` in `cic-website/data/world-census.json`). Checked on a copy of the census (card inserted, `longDescription` set to the brief) with `node tools/validate-census.mjs`. Only release-owned errors remain: `secondReading` absent on the four quotations of six words or more that are new or changed (Quote 1a, 1b, 3a, 3b); the three `tools/quote_renderings.json` listings of the old brief (old Quote 1a, 1b, Praxeas 12) that no longer stand; and the four new quotation spans, which release lists as renderings. No other error names the entry.

Sheet items: S, E, T, I, D in `Source_Sheet.md`; Outline = `Outline.md`; Review = `Review.md`; Revision = `Revision.md`.

## 1. New

| Field | Old | New | Evidence |
|---|---|---|---|
| quotationOriginals, Quote 1a | modern began "Then let the truth..." | the brief's words, "Let the truth reach your ears at least by the hidden road of silent writing."; Thelwall printed, ANF3 1457-1459; English alone | brief para 1; Outline Quotes 1; T1; E1 |
| quotationOriginals, Quote 1b | "One thing only she asks for now..." | "For now, she longs for one thing: not to be condemned unknown."; ANF3 1463-1465; English alone | brief para 1; Outline Quotes 1 |
| quotationOriginals, Quote 2a, 2b, 2c | same three | unchanged (modern, printed, lines, `secondReading` "same", Latin on 2c: OEH2 2289) | brief para 4 matches old spans word for word; ANF3 21744-21751 re-read |
| quotationOriginals, Quote 3a (new) | Praxeas 12 span | "The root and the tree are two things, but joined. ..."; printed ANF3 51561-51564; original KRO 12221-12224 | brief para 6; Outline Quotes 3; T6 |
| quotationOriginals, Quote 3b (new) | none | "The Spirit is third from God and the Son, as the fruit from the tree is third from the root."; printed ANF3 51568-51569; original KRO 12227, first clause only, since KRO misreads sicut as siout (Oehler, OEH2 43592-43594, reads it cleanly) | brief para 6; T6 |
| quotationOriginals, Cyprian | "Give me the master." | "Give me the master," (brief's span, four words, `checked at card`); JER 40505, JERL 55625 | brief para 8; Revision M1 |
| briefSources (new) | none | seven old sources the brief draws on | Stage Two Kit 1.2 |
| shortDescription (new) | none | two sentences, from the heart | Stage Two Kit 1.1; brief paras 2 |
| timeline (new) | none | 14 periods, each line with a reference; dates only for the Apology (about 197, Widely Accepted), Lactantius (about 305 to 310), Jerome (about 393), Augustine (about 428), Vincent (434) | Stage Two Kit 2; E1 to E9, T1 to T6, I2 to I8; census documented stories (The Chaplet 1: ANF3 7680 ff.; To Scapula 5: ANF3 8882-8890) |
| keyWorks | three works | unchanged | brief paras 2, 4, 6 |
| briefReferences | 11 entries | 8 entries rewritten to the brief paragraph by paragraph: Apology 1 and 50; Prescription 15, 19, 21, 36, 37, 38 (38 new: ANF3 21805-21818); Praxeas 1, 2, 8, 11, 12 (8 and 11 new: KRO 12221-12229, 12465, 12497-12498); On Modesty 1 and 21; Jerome 53; Augustine 86 | brief; Outline beats |
| uncertain | 15 items | rewritten: see section 3 | |
| sources.about | five modern works, no Theophilus | Theophilus, To Autolycus II.15, ANF2 8991-8993, added | replaces the editor's note as the support for the older Greek word; ANF2 8993 |

## 2. Clearly wrong or contradicted by the finished brief

| Field | Old words | New words | Evidence |
|---|---|---|---|
| knownFor | "put the Latin words trinitas, persona and substantia to work for God as one substance in three persons" | "said in Latin how God is one and yet three, with the Latin words trinitas, persona and substantia in his text" | "put to work" and "became the church's words" rest on the census and editors only (T5, I1); brief para 2, 6; Outline "Not in the heart" |
| knownFor | "He later took up the strict New Prophecy" | "Later in life he took up the strict New Prophecy, ... and wrote against the bishops." with a gloss of the New Prophecy and of the Tertullianists and heretics | Review B1 (JERL 55626-55629, usque ad mediam aetatem); Kit Part 1 (explain it) |
| quotation 1 uncertain | "This sentence comes in chapter 1" kept on 1b | kept; 1a gets a note that the Latin has liceat and Thelwall frames it as what the judges cannot forbid | OEH1 11253-11261 (damaged); ANF3 1457-1459 |
| uncertain, Why he turned | Augustine "says he went over to the Phrygians..." as a reason, with Jerome | Jerome the only motive; Augustine's because says why he counted Tertullian a heretic; "after middle life" | Review B2, B1; AUG 2868-2873; JERL 55626-55629 |
| uncertain, Cyprian's words | (kept) | added: no held source says they met | Outline Do not say ("Cyprian's teacher") |
| briefReferences, Apology | "the brief puts the book at about 197, as Monceaux does" | "...a year that is Widely Accepted" | Kit Part 1 (a modern work is never named for a date) |
| briefReferences, Apology 40 | listed as brief reference | dropped from briefReferences (the brief no longer tells the crowd's cry); kept in the timeline | brief |
| briefReferences, Novatian, Lactantius, Vincent, "Eusebius, Church History II.2", "World census" | listed | dropped: the brief no longer uses them (kept in timeline, legacy, uncertain) | Revision; brief |

## 3. The standard (Part 1, the layout)

| Field | Old | New | Evidence |
|---|---|---|---|
| Field order | knownFor first | shortDescription, knownFor, otherNames, datesNote, placeNote, role, timeline, keyWorks, legacy, uncertain, sources, briefSources, briefReferences, quotationOriginals | Stage Two Kit 1 |
| datesNote | Monceaux's dates for the Apology, Prescription, turn, Praxeas, Modesty; Nöldechen's and the NPNF note's birth and death; McGiffert, Mosheim, Kaye on the Apology | Jerome's three statements; the Apology about 197 Widely Accepted; other years "modern reconstructions, not given" | Part 1 (modern work is a tool); Outline Do not say (a year for the Prescription, turn, Praxeas, Modesty); S2, E9 |
| uncertain, sources | "McGiffert's guess ... is an editor's" | clause removed | modern view as card content |
| uncertain, trained in the law | McGiffert, Sanday, Monceaux views; the jurist hypothesis | Eusebius's words; his books use court language; no old source says he practiced | S5; Outline Do not say ("He was a lawyer") |
| uncertain, From whom he withdrew | Coxe's and Monceaux's readings | the old sources do not say whether Carthage or Rome; Augustine's later break | D6; Part 1 |
| uncertain, His office | Monceaux, McGiffert | Jerome alone | E6; Outline Leave out |
| uncertain, First in Latin | the census's "first major Christian author"; Coxe's and Wallis's dates for the Octavius | "Foremost": Jerome, Vincent, Augustine together, Widely Accepted; Jerome names Victor and Apollonius before him | Outline essence; D4; JERL 55610-55613; VIN 13555-13557; AUG 2827-2828 |
| uncertain, The Latin words | census's "invented ... sacramentum"; Sanday; Coxe's note on Theophilus; Kaye on the Athanasian Creed | words stand in his text; "coined" is a modern claim; Greek word older (Theophilus, ANF2 8991-8993); Nicaea not said | T5; I1 |
| uncertain, Praxeas and the bishop's edict | Coxe: probably Victor; Monceaux: Callistus | the old sources held do not name either bishop; both disputed | E7, E8 |
| uncertain, What is probably his last surviving book | Monceaux 217 to 222, "very probably the last" | replaced by "When the books were written": modern years left out; On Modesty after the turn by Jerome and by its own appeal to the new prophets | E8a; Outline Do not say ("His last book") |
| uncertain, Novatian | Harnack's "not borne out" | Jerome's judgment only | Outline What came 2 ("give no modern doubt"); I2 |
| uncertain, The Passion of Perpetua and Felicitas | Coxe's guess | removed (outline: Leave out) | Outline Leave out |
| uncertain, Vincent's verdict | "Mansi puts it at about 496" | date and author disputed | I6 |
| uncertain, The quoted Latin | the Praxeas 12 print difference (tenea and etsi) | Latin status of the Apology, Prescription (English alone, heir line with Latin), Praxeas 8 (Kroymann, Oehler agrees) | Part 1 (damaged scan); T6 |
| uncertain, The governors (new) | none | rulers who sat as judges, not emperors | Outline Words to explain; ANF3 1448-1452 |
| uncertain, Foremost (new) | none | see above | Outline |
| legacy.traces | Benson's praise and table; Harnack; "became the Latin church's words ... Sanday" | Jerome on Cyprian; Jerome on Novatian; Augustine on the followers | Part 1; Outline; I2, I3, I5 |
| legacy.remembered | Lactantius, Augustine, Vincent, Jerome (keen character) | kept; Jerome's "chief of the Latin writers" added to the Jerome item | JER 40492-40495 |
| sources.about | Monceaux, Harnack, Benson, Sanday, Coxe's note on Theophilus | moved out to modernWorks (below); Theophilus added | Kit Part 1 |

## 4. Entry fields (for release, after the final check)

- **longDescription:** the brief, final newline removed.
- **modernWorks (new list)**, each moved word for word from the card's old `sources.about` or named in the outline, one line on what it covers, none a witness:
  - Histoire littéraire de l'Afrique chrétienne, vol. 1; Paul Monceaux; 1901. Covers his life and the order of his books.
  - Geschichte der altchristlichen Litteratur, Chronologie, vol. 2; Adolf Harnack; 1904. Covers the dating of early Christian writings, his among them, and Jerome's report on Novatian.
  - Cyprian: His Life, His Times, His Work; Edward White Benson; 1897. Covers Cyprian's life and his borrowings from Tertullian.
  - Editor's preface (Sanday), in Nicene and Post-Nicene Fathers, second series, vol. 9; Sanday. Covers the beginnings of Latin theology and its terms.
  - Editor's note on Theophilus of Antioch, in Ante-Nicene Fathers, vol. 2; A. Cleveland Coxe. Covers the early use of the word Trinity.
  - Translator's notes to Church History II.2, in Nicene and Post-Nicene Fathers, second series, vol. 1; McGiffert; 1890. Covers Tertullian's life and the dating of the Apology.
  - Editor's and translators' notes, in Ante-Nicene Fathers, vol. 3 (Coxe, Holmes and others). Cover the Apology's date, the Prescription's legal terms and Against Praxeas.
- **why:** old "first major Christian author to write in Latin ... invented them - trinitas, persona, substantia, sacramentum ... Trained as an advocate ... in his later years ... called him simply 'the master'" contradicts the brief and the Do not say list (first, coined, advocate, later years). New: "Tertullian was the foremost early writer of the faith in Latin, around the year 200. At Carthage he wrote the Apology, defending Christians before Rome's governors, and the Prescription, claiming the Scriptures for the churches the apostles founded. In Against Praxeas he said in Latin how God is one and yet three. Later in life he joined the New Prophecy, a strict movement whose prophets said the Holy Spirit spoke anew through them, and wrote against the bishops. Jerome reports that Cyprian, a generation on, read him every day and would ask for the master."
- **relationsSummary:** old "opened the entire tradition of Latin Christian argument that the Latin apologists carried on" is a claim the brief does not make. New: "Told within The Case Made in Latin, which holds his Apology. Jerome says Cyprian read him every day."
- **teaser:** old "a trained rhetorician's mind ... forced to invent the Latin words the West has argued in ever since" (modern, not in the brief). New: "Carthage, around the year 200: the foremost early writer of the faith in Latin, who pleaded for the Christians before Rome's governors, then joined a strict prophetic movement and wrote against the bishops."
- **legacy:** old "He gave Latin its words for the Trinity", "never made a saint" (ruled out), "owes a great deal to him", "No community descends from him". New: "Augustine says his followers, the Tertullianists, lasted at Carthage down to his own day, dwindling to a few, who crossed to the Catholic church and handed over their basilica. Jerome says Cyprian read him every day, and calls Novatian's On the Trinity a sort of epitome of his work. Augustine says many of his works, most eloquently written, are still read."
- **dates:** "c. 197-220" has no old source for 220. Suggest "From about 197"; `start`, `end`, `activeYear` stay for the map.
- **voices:** "probably a trained rhetorician" (not held; E5/S5) and "from roughly 197 to 220" conflict; second voice, "ask for the volume", adds a word Jerome's Latin does not have (Da magistrum, JERL 55625). Suggested: "Tertullian of Carthage, the tradition is one man: a convert writing in Latin at Carthage from about 197" and "Cyprian of Carthage, not a follower: Jerome reports through two people that Cyprian read Tertullian every day and would often say give me the master".
- **documentedStories (flag only, not this thread's content):** The Chaplet text says "Many Christians, he reports, condemned the man"; the book says "whether on the part of Christians I do not know" (ANF3 7680 ff.). Dates c. 211 and 212 and "already leaning toward the New Prophecy" rest on modern dating.

## 5. Claims not found

None left in place unsupported. Removed as resting only on a modern work (see section 3), none contradicted by an old source: McGiffert's conversion guess; Coxe's reading of the withdrawal; Monceaux's dates and Callistus; the jurist hypothesis; Harnack on Novatian; Coxe and Wallis on the Octavius; Kaye on the Athanasian Creed; Coxe on Perpetua.
