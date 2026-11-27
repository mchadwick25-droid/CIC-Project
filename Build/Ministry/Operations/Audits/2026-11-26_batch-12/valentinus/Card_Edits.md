# Card edits: Valentinus (`valentinus.card.json`)

A full new card, built under the role's "A new card". The starting card (`Card.existing.json`, the same as the census `card` now) was a pointer only. Each field below gives its evidence: Source_Sheet rows (S, E, I, D, with their files and lines), the outline at its cited lines, or the brief's sentence. Files are under `cic/texts/`. Every cited line was re-read in its file for this card. Keys follow the `polycarp-of-smyrna` card; `secondReading` is left out of all three quotations (each runs six words or more), so release sets it.

## Fields kept word for word from the starting card

| Field | Kept text | Evidence |
|---|---|---|
| `role` | "Teacher and founder of a school" | S3 (διδασκαλεῖον, IR 31519–31520); brief "At Rome he founded a school, a circle of students around a teacher." |
| `uncertain[0]` | "Almost everything known of him comes from his opponents: … chiefly Clement's." | I3; brief "almost everything known of Valentinus comes from men who wrote against him." |
| `uncertain[4]` | "Tertullian places him at Rome under Bishop Eleutherus. Irenaeus places him from Hyginus to Anicetus, earlier." | D1; E3 (TE 21335–21339); S1 (IR 39968–39970). Also outline Cut first 4, sent to the card. |
| `uncertain[8]` | "That he was taught by Theudas, a pupil of Paul, is his followers' claim, as Clement reports it." | S5 (CL 52962–52967); outline Leave out: "card". |
| `legacy.remembered[3]`, first sentence | "Tertullian calls him \"the disciple of Platonism.\"" | TE 21333. |
| `legacy.remembered[5]` | "Hippolytus of Rome says Valentinus claimed to have seen a newborn child who told him he was the Word." | E13 (HIP 10054–10059; WEN 13128–13132); outline Leave out: "card, in Hippolytus's voice". |
| `keyWorks[1].about`, first clause | "known only from a passage Clement of Alexandria quotes in his Stromata, Book 4" | E8 (CL 39090–39093). |
| `sources.about`: Kroymann Latin entry | word for word | KR. |
| `quotationOriginals[1]`: `work`, `uncertain`, `original`, `originalFile`, `originalLines` | word for word | KR 9633–9653 (checked against the scan readings); E2. |
| `quotationOriginals[0].work`, `uncertain` | word for word | CL 34289–34303; Clement's Greek not held (sheet, files). |

## Fields changed or new

| Field | Old | New | Evidence |
|---|---|---|---|
| `knownFor` | "A teacher at Rome who broke with the church and founded a school that taught a heaven of divine powers in pairs." | "A teacher at Rome in the middle of the second century who founded a school. By his opponents' accounts, it taught a heaven of divine powers in pairs." | The break is now one witness's (brief "Of the writers near his time, Tertullian alone says he broke with the church."; D3; Review B3); "By his opponents' accounts" and the century, brief paragraphs 1 and 3. |
| `shortDescription` | none | written fresh, two sentences | Brief paragraphs 1, 3 and 5 ("At Rome he founded a school…", "By his opponents' accounts…", "Those words survive because Clement…"). |
| `datesNote` | "At Rome from about the time of Bishop Hyginus to Bishop Anicetus" | four sentences: no year of birth or death; Irenaeus's Hyginus, Pius, Anicetus; the reign of Antoninus, mid-century; Tertullian's Eleutherus | S1 (IR 39968–39971), S2 (CL 52956–52959; TE 21332–21335; mid-century Widely Accepted), D1, E15. No modern year (McGiffert's years, S1, left out). |
| `placeNote` | "Rome" | "Rome, where he taught and founded his school. No early source we hold says where he was born." | S1, S3, S4; outline Setting ("Where he was born: not told"). |
| `keyWorks[0]` Letters `about` | "known only from passages Clement of Alexandria quotes in his Stromata, Book 2" | adds the three letters' content: the heart as an inn; the angels' terror at Adam; to Agathopus on Jesus's eating | E7 (CL 34289–34303), E11 (CL 32722–32735, "in an epistle"), E12 (CL 36157–36161, "Epistola ad Agathopodem", Latin). Outline Leave out: E11 "card". The letter to Agathopus lies in Book 3, so "Book 2" is dropped. |
| `keyWorks[1]` A sermon `about` | ends "…Book 4" | adds what it says | E8; brief paragraph 6. |
| `keyWorks[2]` A psalm | none | new | E10 (HIP 9787–9802; WEN 12707–12740); outline Leave out: "card"; D6 (damaged text). |
| `legacy.traces` | the Tertullian list of students | nine lines: Ptolemy and the others (Tertullian); the two branches and the two positions on Jesus's body (Hippolytus); "now nowhere" and Axionicus; Justin's Valentinians; Origen and Heracleon; Eusebius on Bardaisan and Ambrose; the Gospel of Truth title; the 1945 finding; no community today | I1 (KR 9655–9666; TE 43117–43128; HIP 9640–9666; WEN 12542–12556; OR 23165–23169; EUS 26652–26658, 34813–34815); E1 (IR 19254–19256); I4 (IR 41174–41178); I3 (census tradition); census tradition `legacy`. Outline Cut first 1 and 2, Beat 5 (positions to the card), Leave out (Ambrose and Origen, Gospel of Truth: card), What came of them, "Who keeps him today: card only". |
| `legacy.remembered[0]` | "Irenaeus of Lyon says he adapted the principles of the Gnostic teaching to his own school." | gloss added ("that of people who claimed a special knowledge"), and Irenaeus's five books with "a bud from that of Valentinus" | Kit Part 1, Explain it; outline Words to explain (Gnostic); S3; I2 (IR 29871–29873, 50552–50554). |
| `legacy.remembered[1]` | none | Irenaeus's one God, maker of heaven and earth | E4 (IR 31390–31392); I2 Defended. |
| `legacy.remembered[2]` | none | Clement's answer: saved by nature, commandments useless, apart from the Savior, "it is not Christ who has abolished death" | E8, E9 (CL 39095–39100, 39123–39125, 40954–40960); outline Cut first 6, card. |
| `legacy.remembered[3]` | the Platonism line | adds Against the Valentinians and Justin among those who wrote against such teachers in their lifetime | I2; TE 43159–43163. |
| `legacy.remembered[4]` | none | Hippolytus's Pythagoras and Plato charge | E6 (HIP 9124–9129); outline Cut first 5, card. |
| `legacy.remembered[6]` | none | Polycarp at Rome turned many from Valentinus and Marcion | I2 (IR 39869–39873); outline Leave out: card. |
| `uncertain[1]` | "The teaching of paired divine powers is described by two opponents… as the American edition's note on his Book 6 shows. The division of people by nature is reported by Irenaeus and Clement, of his followers. The story of the lost bishopric is Tertullian's alone." | "What is his and what is his school's…" | D4, E5, E6. The old line rested on a modern editor's note, which is no witness (Kit Rigor), and its Irenaeus claim on nature is not found in the sheet. The bishopric now sits in `uncertain[5]`. |
| `uncertain[2]` | none | Why pairs: the school's "love is not love…" | E6 (HIP 9170–9174); outline Cut first 3, card; Do not say (not Valentinus's own). The starting card's quotation entry for this line is dropped, since the brief no longer quotes it. |
| `uncertain[3]` | none | The fall, as Irenaeus gives it | E4 (IR 31529–31543); outline Do not say ("Sophia", "The lesser maker was evil"). |
| `uncertain[5]` | none | The break: one witness near his time, two reasons, no city, year or rival | D2, D3, E2, E3; Review B3; brief paragraph 4. |
| `uncertain[6]` | none | Epiphanius's Cyprus report; no death held | E15 (HOLL 29802–29807); D5; outline Leave out, card. |
| `uncertain[7]` | "No early source we hold says where he was born." | adds Epiphanius's doubtful Egypt and Alexandria report | S4 (HOLL 28939–28947); outline Leave out, card. |
| `uncertain[9]` | none | The sermon's "Valentinian" and the clause left out | E8 (CL 39090–39096, 58379); outline Quote 3; D6. |
| `uncertain[10]` | none | "as yet nowhere" against nusquam iam | I1 (KR 9663; TE 43124); outline Do not say. |
| `uncertain[11]` | none | The Gospel of Truth: who wrote it not held | I4. |
| `uncertain[12]` | none | The psalm's damaged text | E10 (WEN 12738–12740). |
| `uncertain[13]` | none | The second man of the Eastern branch, Ardesianes in Wendland's text | I1 (WEN 12554, 12607; HIP 9658–9661); outline Do not say. No identification is stated. |
| `uncertain[14]` | none | The vision is a wonder in one witness | E13. |
| `sources.ownWords` | one entry, "Books 2 and 4" | Clement entry widened to "Books 2, 3, 4 and 6" and "a book"; Hippolytus English and Wendland Greek added for the psalm | E7, E8, E11, E12; E10. |
| `sources.about` | Irenaeus, Hippolytus, Tertullian, Kroymann, Clement | titles widened to the chapters used; added Justin (English, and Archambault Greek), Wendland Greek, Origen, Eusebius, Epiphanius (Holl Greek), Jerome | Each file is cited by a card line: IR, JU, WEN, OR, EUS, HOLL, `npnf203_theodoret-jerome-gennadius-rufinus.xml` 40494–40499 (Tertullian at Carthage, outline Setting). |
| `briefSources` | none | six old sources the brief draws on | The brief's quotes and credits: CL, IR, TE, KR, HIP; Jerome for "writing at Carthage early in the next century". |
| `timeline` | none | seven periods, 37 lines, each with file and lines | All rows of the sheet the outline uses, in order; "Date unknown" or the record's own phrase where no date is held (Stage Two Kit 2.3). |
| `briefReferences` | seven lines | ten lines | Rebuilt for the brief as it stands. Dropped: "Hippolytus, Refutation VI.29: the Father alone and all love" (the brief no longer tells it); "The ANF editor dates the book not earlier than 207" (a modern date, Kit Rigor). Added: the inn image, the reign of Antoninus, Jerome on Tertullian, Prescription 13, the Irenaeus prefaces. |
| `quotationOriginals[0]` | modern "It is unclean, the home of many demons…", printed from "being unclean", lines 34300–34302 | modern now the brief's whole Quote 1; printed from "So fares it with the heart…", lines 34298–34302; `secondReading` left out | Brief paragraph 5; CL 34298–34302. |
| `quotationOriginals[1]` | modern "Valentinus had hoped to become a bishop, for he was able in mind and in speech…" | the brief's Quote 2 word for word; lines 43109–43113; `secondReading` left out | Brief paragraph 4; TE 43109–43113; KR 9633–9653. |
| `quotationOriginals[2]` | "love is not love unless there is something to love." | removed | The brief no longer quotes it. |
| `quotationOriginals[2]` (new) | "death may die in you" | the brief's whole Quote 3; printed CL 39090–39093; `secondReading` left out | Brief paragraph 6; E8. The starting entry's short span is gone from the brief. |

## Entry fields (for release, after the checker)

- `teaser`: "A teacher at Rome who broke with the church and founded a school that taught a heaven of divine powers in pairs." → "A teacher at Rome in the middle of the second century whose school, by his opponents' accounts, taught a heaven of divine powers in pairs." The break is one witness's, and the brief now credits it (brief paragraph 3; D3; Review B3).
- `modernWorks` (new; the outline's "Modern, each a tool", only those it used to clarify a text; all printed before 1931):
  - {"title": "Fathers of the Second Century: Hermas, Tatian, Athenagoras, Theophilus, and Clement of Alexandria (Ante-Nicene Fathers, volume 2)", "author": "Alexander Roberts and James Donaldson (ed.), William Wilson (tr. of Clement)", "year": "1885", "note": "English translation of Clement's Stromata, with notes that give Grabe's corrections of the Greek, among them the word presence in Valentinus's letter on the heart."}
  - {"title": "Hippolytus Werke, dritter Band: Refutatio omnium haeresium (Die griechischen christlichen Schriftsteller 26)", "author": "Paul Wendland (ed.)", "year": "1916", "publisher": "J. C. Hinrichs, Leipzig", "note": "The Greek text of the Refutation, with an apparatus that records the manuscript readings, among them the damaged words of Valentinus's psalm and the name in the Eastern branch."}
  - {"title": "Epiphanius, erster Band: Ancoratus und Panarion haer. 1-33 (Die griechischen christlichen Schriftsteller 25)", "author": "Karl Holl (ed.)", "year": "1915", "publisher": "J. C. Hinrichs, Leipzig", "note": "The Greek text of Panarion 31, with notes that give the Greek of Irenaeus on Valentinus's years at Rome and set Epiphanius's reports beside it."}
  - Not listed: McGiffert's years for the bishops and the ANF editor's date for Against the Valentinians (each a claim of its own, outline "Modern"). The starting card's `sources` held no modern work, so none moves.
- No `why` or `relationsSummary` on the entry; nothing to change.

## Conflicts and not found

- Entry `regions` holds "Asia Minor": not found in any held line on Valentinus (S1 gives Rome only). Not changed; for release to judge.
- The tradition entry `valentinian-and-other-gnostic-christianities` (not this entry; flagged, not touched): its `why` says Valentinus was "an Alexandrian teacher who came to Rome around 136" and taught "a divine spark… trapped", each a line the outline's Do not say forbids (S4, S1, E-rows). The card does not repeat them.
- From the starting card, not carried: "The division of people by nature is reported by Irenaeus" (not found in the sheet's held lines); "as the American edition's note on his Book 6 shows" (a modern note, no witness).

Scorer (`python -m engine.m1.profile_readability`, card running text, outside the repository): `2255 words, grade 7.6 (names out 5.4), reading ease names out 81.6, 14.0 words a sentence, 0.8 joining words per 100, 23% short sentences, longest sentence 33 words - pass (note: grade 7.6 is under 8: the listener read checks it is not flat)`

Validator (`tools/validate-census.mjs --skip-quotes` on a census copy outside the repository, with this card and the brief as `longDescription`): the only errors are the three missing `secondReading` values, which release sets. The full quote check runs out of memory in this container; every quoted span in the card's prose was checked by hand-run script against its cited files and found.
