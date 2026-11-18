# Council profiles, eras 1 and 2: review round 1 (2026-11-14)

**Scope.** Nine major-council profiles in `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/`: era 1, `councils-of-rome-and-carthage-251` (approved by Mark as the worked example, reviewed lightly); era 2, `council-of-arles-314`, `council-of-nicaea-325`, `council-of-sardica-343`, `councils-of-ariminum-and-seleucia-359`, `first-council-of-constantinople-381`, `conference-of-carthage-411`, `council-of-ephesus-431`, `council-of-chalcedon-451`. For each: the brief, the entry, the audio script and the era's `records.json`.

**Standard.** `Council_Profile_Pattern.md` (C1 to C8) with `Who_Profile_Pattern.md` checklist items 1 to 9, 11 and 13.

**Method.**
- Every quotation in every brief and entry was searched in the vendored files under `cic/texts/` with the tag-stripped, whitespace-tolerant `findq.py`, and the key ones were read in context, notes included, for writer, book and side.
- The factual sentences of each brief were checked against the lines cited in `records.json`: dates, counts, who did what, and every "lost", "only" or "no source" claim. `cic/texts/` was searched for counter-evidence where a draft says something is not held.
- People verdicts were checked against every Who scan (`Build/Ministry/Operations/Audits/2026-11-1*_who-scan-*/Who_Scan_*.md`, the supplement included). Every person id was checked against the Who-profile cards and `cic-website/data/world-census.json`. Every tradition id was checked against the census, with its dates and its people.
- Prose was read for the Who checklist item 4 faults. Sentence lengths were counted.
- Readability was scored with `engine.m1.gates.grade_text`. Each audio script was compared character for character with its brief plus `[calmly]` at the start and `[warmly]` before the last paragraph.
- No model calls, no network calls, no paid services. No draft was edited.

**Result in one line.** All nine pass the gates: readability, length and audio. Every quotation is in its file, word for word. No finding is blocking. Six substantial findings across five councils need a fix before the profiles are approved to proceed.

## Per-council table

| Council | Words | FK | FRE | Audio = brief | Verdict |
|---|---|---|---|---|---|
| councils-of-rome-and-carthage-251 | 399 | 7.49 | 63.48 | yes | PASS |
| council-of-arles-314 | 398 | 7.76 | 60.11 | yes | PASS |
| council-of-nicaea-325 | 398 | 7.85 | 60.69 | yes | PASS WITH FIXES |
| council-of-sardica-343 | 400 | 7.70 | 60.64 | yes | PASS |
| councils-of-ariminum-and-seleucia-359 | 399 | 8.37 | 60.41 | yes | PASS WITH FIXES |
| first-council-of-constantinople-381 | 399 | 7.87 | 60.90 | yes | PASS WITH FIXES |
| conference-of-carthage-411 | 400 | 7.86 | 61.50 | yes | PASS WITH FIXES |
| council-of-ephesus-431 | 399 | 7.74 | 60.40 | yes | PASS |
| council-of-chalcedon-451 | 398 | 7.37 | 63.96 | yes | PASS WITH FIXES |

Five of the briefs score between 60.1 and 60.7 for reading ease, just over the line. A fix that adds words should be scored again.

## Quotations

Every quoted phrase in the nine briefs and entries was found in a vendored file. Two strings in quotation marks are glosses, not quotations: "Spirit-fighters" (CON-4) and, in the Ariminum brief, "of one substance" and "of like substance" as English for Acacius's Greek terms (ARI-5). One entry quote comes from a file the entry does not list: "the things done at Chalcedon" (CHA-5). All attributions read correctly in context. Two pairs are worth noting as correct:
- "He was the whole tribunal" and "Who was judge? Cyril" are both Nestorius's own lines, 14 lines apart in `nestorius_bazaar-of-heracleides_driver-hodgson1925.txt` (l.8631-8632, 8645). The brief gives them as two quotes, which is acceptable.
- Petilian's "gladly" stand (Carthage 411) is in the Latin: "non erubescimus, non veremur, non evitamus, te residente, vir nobilis, libenter adsistere" (`mansi_…tomus-4…txt` l.13211-13214).

---

## councils-of-rome-and-carthage-251 (approved worked example; light review)

Quotes, dates and attributions hold. The Who verdicts match the era 1 scan (Cyprian WHO, Cornelius STORY, Novatian WHO, Dionysius of Alexandria WHO).

**ROM-1. Minor.** One sentence runs 27 words: "The next year, by Hefele's dating, when a new persecution seemed near, the African bishops went further and offered peace to all who had kept on repenting." Fix (optional, since this is the approved example): split after "near".

## council-of-arles-314

**ARL-1. Minor.** Text: "What survives comes from the winning side. It is the bishops' letter to Silvester, bishop of Rome, and Constantine's letters." The canons also survive. They are held in Latin (`bruns_canones-apostolorum…` l.7805-8013, cited in records for canons 1, 8 and 13), and the entry's own `record` says "The full canons survive in Latin". Fix: "It is the bishops' letter to Silvester, bishop of Rome, with their canons, and Constantine's letters."

**ARL-2. Minor.** Text: "led by Marinus, bishop of Arles." The held English letter gives names only: "To the most beloved Pope Silvester: Marinus, Acratius, Natalis, …" (`optatus_against-the-donatists.txt` l.7113). The `absent_details` entry agrees: "The English letter to Silvester gives names only. The sees come from Hefele." Fix: "led by Marinus, whom Hefele takes as bishop of Arles". Or leave it and accept the see as Hefele's, already credited for the sees in the next sentence.

**ARL-3. Minor.** One sentence of 26 words: "His opponents, later called Donatists, said that the bishop who ordained him, Felix of Aptunga, had handed over the Scriptures to be burned in the persecution." Fix (optional): end the sentence after "Felix of Aptunga" and start a new one.

## council-of-nicaea-325

**NIC-1. Substantial (C3; pattern "How a council differs", 3).** Text (brief): "Arius's own letters survive only in books by his opponents. The council's letter says he taught 'that there was a time when he was not.'" The entry's `issue` says the same. The pattern requires the condemned party's position "in its own words where the Library holds them". The Library holds Arius's own letter to Eusebius of Nicomedia in English, in Theodoret, Church History I.4 (`npnf203_theodoret-jerome-gennadius-rufinus.xml` l.6000-6046): "that before He was begotten, or created, or purposed, or established, He was not" (l.6043-6044); "We are persecuted, because we say that the Son has a beginning" (l.6045-6046). The brief says his letters survive and then tells his teaching through the council that condemned him. Fix: give Arius's teaching in his own words from Theodoret I.4, marked as kept by Theodoret, an opponent. Keep the council's letter as the second witness, which also meets the two-witness rule. Add the letter to `sources.fromThoseThere` (or a new group line) and a claim to `records.json`. Rescore the brief after the change.

**NIC-2. Minor (item 7).** Text: "Eustathius says a statement from Arius's party was torn up 'in the sight of all.'" Eustathius speaks of "the formulary of Eusebius" and "the Eusebian gang" (`npnf203` l.6390-6396). Which Eusebius he meant is a `contested_claim` in records ("Whose statement was torn up"). "Arius's party" stays inside what Eustathius says, so this is not wrong, and the entry's `uncertain` carries the dispute. Fix: none required. Optionally, "a statement from the party of Eusebius".

## council-of-sardica-343

**SAR-1. Minor (C4).** Text: "Socrates of Constantinople and Sozomen date it to 347." They give a consulship, not a year. The entry's own `datesNote` says so: "give the consulship of Rufinus and Eusebius, which their editors take as 347". The records claim reads the same ("Socrates II.20 … the consulship of Rufinus and Eusebius, taken as 347", npnf202 l.6831-6835). Fix: "Socrates of Constantinople and Sozomen date it by a consulship that their editors take as 347."

**SAR-2. Minor (C4).** Text: "Athanasius went home in 346." The year comes from the index to the Easter letters as Robertson gives it (records: "Robertson, from the index to the Easter letters (npnf204 l.5140-5147)"). No witness is named in the brief. Fix: "and Athanasius went home in 346, by the index to his Easter letters."

## councils-of-ariminum-and-seleucia-359

**ARI-1. Substantial (C1, C3, item 6).** Two linked errors about who wrote the record.
- Brief: "The council's own acts are lost, apart from letters and decrees kept by the Nicene side, who also wrote the histories. The other side speaks through its creeds, which they copied." The next paragraph uses Philostorgius, "a follower of Eunomius of Cyzicus", who was not Nicene. So "who also wrote the histories" is contradicted by the brief itself. The other side also speaks in more than its creeds. The entry's `record` says Hilary's dossier "also holds a letter of the Arian party at Ariminum". Acacius's declaration at Seleucia is held in English (`npnf202` l.9300-9330, Socrates II.40), and so is Maximinus's statement to Augustine (records, `augustine pl42` l.54499-54501).
- Entry `uncertain[0]`: "The Homoian side speaks in its creeds; its one historian, Philostorgius, survives only in a hostile summary." Philostorgius was a Eunomian (Anomoean), not a Homoian. The entry's own `record` says "A follower of Eunomius, so of the opposite side". The entry lists `anomoean-eunomian-christianity` as Condemned by these councils ("the synod at Constantinople deposed Aetius from the diaconate"). The census's Homoian row says the same: "In 360 a Homoian council at Constantinople deposed Aetius … Philostorgius wrote from the side of Eunomius." Calling him the Homoian side's historian puts a witness on the wrong side.

Fix: brief, "kept by the Nicene side, who wrote most of the histories. The other side speaks through its creeds and Acacius's statement, which the Nicene writers copied." Entry, "The Homoian side speaks in its creeds and in Acacius's statement. Philostorgius, a Eunomian historian hostile to both sides, survives only in a hostile summary." Keep the `absent_details` note that the Latin letter of the Arian party was not read.

**ARI-2. Minor (item 1).** Text: "Socrates of Constantinople says the town was chosen so its name would pass for Nicaea." Socrates says they held a synod at Nice, "giving it the name of the general council, in this way attempting to deceive the more simple by the similarity of names" (`npnf202` l.8946-8953). He does not say the town was chosen for that. Sozomen gives the same story as "the account given by some parties" (l.34079-34087). Fix: "Socrates of Constantinople says they used its name to pass the creed off as that of Nicaea."

**ARI-3. Minor (items 8, 9).** Text: "Jerome of Strido" (brief; entry `people` and `record`). The held file spells the place Stridon (`npnf206_jerome-principal-works.xml` l.702, 975). The Who scan row, the profile id `jerome` and the census use "Jerome". Fix: "Jerome" throughout, with a place only if needed ("Jerome, writing at Antioch").

**ARI-4. Minor (C4).** Text: "In the winter of 359, at Ariminum in Italy, …" Sulpicius gives winter and "the seventh month" (`npnf211` l.11336-11339). The year depends on Hefele's May opening, as the records claim says ("the year is reckoned from Hefele's May opening"). Since the councils' year is attested by consulate (`datesNote`), this is low risk. Fix (optional): "In the winter after the council opened, at Ariminum in Italy, …"

**ARI-5. Minor (item 2).** Text: "rejected both 'of one substance' and 'of like substance.'" Acacius's text reads "the terms homoousion and homoiousion … we reject the first two" (`npnf202` l.9322-9327). The quotation marks hold English glosses, not his words. Fix: drop the marks ("rejected both the words for 'one substance' and 'like substance'") or quote the text.

## first-council-of-constantinople-381

**CON-1. Substantial (items 1, 7; C8).** Text: "Before the bishops gathered at Constantinople in 381, Gregory of Nazianzus gave up his see. 'Farewell, my throne, envied and perilous height,' he told them." Heard aloud, "Before the bishops gathered" reads as time: he resigned before the council met. The oration is titled "The Last Farewell in the Presence of the One Hundred and Fifty Bishops" (`npnf207_cyril-jerusalem-gregory-nazianzen.xml` l.40106-40110). The records claim says he "gave his farewell before the hundred and fifty bishops". The brief's sixth paragraph then tells the same resignation again, mid-council: "Some bishops, chiefly from Egypt, objected to Gregory as the city's bishop, and he withdrew." So the listener hears two resignations, in the wrong order. Fix: open on the scene, "At Constantinople in 381, Gregory of Nazianzus stood before the bishops of the council and gave up his see." In paragraph 6, tie the withdrawal back to it ("… objected to Gregory as the city's bishop. That was when he withdrew, with the farewell he gave them.").

**CON-2. Minor (item 7).** Text: "Meletius of Antioch led them at first and died while they sat." Who presided is a `contested_claim` in records: Hefele has Meletius, then Gregory, then Nectarius; Sozomen VII.7 has Timothy, Meletius and Cyril leading the Nicene party; Van Espen and Hergenröther disagree on later presidents. That Meletius led first is the least disputed part, and the brief does not say who followed him. Fix: "Meletius of Antioch led them at first, by Hefele's reading, and died while they sat."

**CON-3. Substantial (C7; Who-scan contradiction).** Entry `people`: `{"name": "Timothy of Alexandria", "verdict": "NOT SCORED", …}`. The supplement scan has scored him: "| Timothy of Alexandria | bishop 380-385 … | LISTED | Own work (Canonical Answers) | … No. Eleven short canonical answers; no life held." (`Build/Ministry/Operations/Audits/2026-11-12_who-scan-supplement/Who_Scan_Supplement.md` l.123). NOT SCORED is only for people no scan has scored. Fix: set the verdict to LISTED, with no id.

**CON-4. Minor (item 2).** Text: "the Pneumatomachi or 'Spirit-fighters,'". The canon reads "the Semi-Arians or Pneumatomachi" (`npnf214` l.13969-13976). "Spirit-fighters" is not in the file, and the quotation marks claim it is. Fix: "the Pneumatomachi, the 'fighters against the Spirit'" only if a held line uses it. Otherwise drop the marks: "the Pneumatomachi, those who fought against the Spirit's full divinity".

**CON-5. Minor (C4).** Text: "Around the year 600, Gregory the Great of Rome counted this council among four that he compared to the four Gospels." The held lines give no date (Percival's introduction, `npnf214` l.13240-13242; Hefele's excursus, l.15082, 15141-15144). Fix: drop the date ("Later, Gregory the Great of Rome counted …") or date it from a held line of Gregory's own letter in `npnf212`.

**CON-6. Minor (item 6; pattern 3, two witnesses).** Text: "Their view reaches us only through opponents. Gregory put their question in an oration: …" The brief names one witness for the Pneumatomachian teaching. The entry has a second, the synod of 382 (records: "Synodal letter of 382 … npnf214 l.15250-15256"). Fix: "Their view reaches us only through opponents, chiefly Gregory and the bishops' letter of the next year."

## conference-of-carthage-411

**CAR-1. Substantial (C2; item 1).** Text: "The full record survives in Latin, each speech signed by its speaker. It breaks off on the third day." The two sentences contradict each other: the record is not full. Masson's preface: "tertiae cognitionis magna pars, quae hic deficit, necessario inde petenda est" (`mansi_…tomus-4…txt` l.1443-1446). The `absent_details` and the entry's `uncertain[0]` say "The acts survive but break off in the third session." Fix: "The record survives in Latin, each speech signed by its speaker, but it breaks off in the third session."

**CAR-2. Minor (item 9).** Text: "It breaks off on the third day" and "Only on the third day did the debate reach the old records about Caecilian". The sessions were 1, 3 and 8 June (`datesNote`), so "the third day" can be heard as 3 June, which was the second session. Fix: "the third session" or "the third meeting" in both places.

**CAR-3. Minor (item 8).** Text: "Emeritus of Caesarea" (brief and entry `people`). Caesarea here is the city in Mauretania, and the Who scan row reads "Emeritus of Caesarea (Mauretania)". A listener will take Caesarea in Palestine. Fix: "Emeritus of Caesarea in Mauretania" at first mention in the brief, and the scan's name in `people`.

## council-of-ephesus-431

**EPH-1. Minor (C4, item 7).** Text: "With his own bishops, forty-three by Hefele's count, he deposed Cyril and Memnon". The 43 comes from the signed sentence of John's assembly, which is held (records; the entry's `record`, Mansi tomus 5). Cyril's council calls them "a little more than thirty" (`npnf214` l.17711-17712). The records hold this as a `contested_claim`. Fix: "With his own bishops, forty-three by their signed sentence and 'a little more than thirty' by Cyril's council, he deposed …" Watch the word count (399).

**EPH-2. Minor (C1, C2).** Text: "The minutes we have are those of Cyril's council, which he led. Nestorius told his side in exile, in a book that survives only in Syriac." The documents of John's assembly also survive, in Latin (entry `record`: "The Eastern bishops' own documents, in Latin. On John's side"). The entry's `uncertain[0]` says so, so the brief's caveat and the entry's disagree. Fix: add "John of Antioch's assembly left its own documents too."

**EPH-3. Minor (item 7; census fit).** Entry `traditions`, `persian-church-of-the-east-early`, Affected: "It never received Ephesus. W. A. Wigram … says it neither accepted nor formally rejected the council …" The flat opening "It never received Ephesus" settles a `contested_claim` (Badger: the Easterns were cut off by the decree of Ephesus, `badger v1` l.7672-7683; Wigram: no corporate action). Barhadbeshabba, near 600, belongs to the census row `the-church-of-the-east-under-persia` (424-651), not to the early row (c. 300-451). Fix: open with Wigram's words, not the flat claim. Either move the Barhadbeshabba clause to an Affected line for `the-church-of-the-east-under-persia` or cut it.

**EPH-4. Minor.** One sentence of 28 words: "Over the protest of the emperor's officer, Count Candidian, they opened the council on 22 June, by the dating of Charles Joseph Hefele, the historian of the councils." Fix: split after "Candidian".

## council-of-chalcedon-451

**CHA-1. Substantial (pattern 1, "later narrative … with its writer named and, where a held source gives it, when"; C1).** Text: "The council's own minutes survive. The losing side tells its story in a Syriac chronicle known as that of Zachariah of Mitylene." Nothing tells the listener that this is a later compilation. It follows straight after the minutes and can be heard as a record of the time. The held source gives the dating: Book III is drawn from Zachariah's Greek history, which ended in 491, and the Syriac compiler is another man (records: "Hamilton and Brooks, introduction (zachariah l.300-318)"). The entry's `record` says the same. Fix: "The losing side tells its story in a later Syriac chronicle, known as that of Zachariah of Mitylene, built on a Greek history that ran to 491."

**CHA-2. Minor (item 1; C5).** Text: "his successor Marcian and the empress Pulcheria called a new council." The Definition names "the command of … Marcian and Valentinian" (`npnf214` l.20190-20194). Pulcheria's part is Hefele's, and Zachariah credits Leo's exertion (records `contested_claims`, "Who brought the council about"). The entry's `calledBy` sets this out correctly. Fix: "his successor Marcian called a new council, with the empress Pulcheria, Hefele says, at his side."

**CHA-3. Minor (C3).** The brief gives the losing side's verdict on the council (Zachariah's "tore into ten thousand rents"), but not its teaching in its own words. Dioscorus's own line is held in the acts: "I receive 'the of two;' 'the two' I do not receive" (`npnf214` l.19255-19256). The entry already quotes it, and the brief's paraphrase of Eutyches is sourced, so this is not wrong. Fix (optional): use Dioscorus's line in paragraph 4, marked as kept in the winners' minutes.

**CHA-4. Minor (sources).** The entry's `traditions` note for `syriac-orthodox-west-syriac-christianity` quotes Severus of Antioch, "the things done at Chalcedon". The quote is verbatim (`severus-of-antioch_select-letters-book6-part2_brooks1904.txt` l.1349-1350, 1518; also `…part1_brooks1903.txt` l.7867). Neither Severus file is in the entry's `sources`. Fix: add the Severus letters to `sources.writtenLater`.

**CHA-5. Minor (item 8).** Text: "and deposed Flavian, the bishop who had condemned him." There is no place at first mention. Flavian of Antioch (d. 404) is a namesake. The entry's `people` has "Flavian of Constantinople". Fix: "deposed Flavian, bishop of Constantinople, who had condemned him." Two sentences also run 26 and 29 words: "It restored Eutyches …" and "Evagrius of Epiphania, a historian on Chalcedon's side, quotes Priscus …". Split the second after "Priscus, who was in the city".

---

## Checks that passed across all nine

- **C1.** Every `record` entry has a kind. Partisan witnesses are marked in the note, except Philostorgius's side (ARI-1).
- **C2.** Lost acts are said once and early in Rome/Carthage, Arles, Nicaea, Ariminum and Constantinople. Held acts are named first at Carthage 411, Ephesus and Chalcedon.
- **C4.** Every count has a named witness. Hefele's months and days are credited to him by name in every brief. The exceptions are the minor items SAR-1, SAR-2, ARI-4 and CON-5.
- **C5.** `issue`, `decided` and `outcome` are kept apart in every entry. Failed or rejected outcomes are told as such: Sardica's split, Ariminum's repudiation, Rome's refusal of Constantinople's canon 3, Leo's annulment of canon 28, Armenia's refusal.
- **C6.** The creeds and the definition are told as acts of the meeting, with drafter, signers and refusers where held: Eusebius's creed and the one added word at Nicaea; Valens and Ursacius at Ariminum; the Session V pressure at Chalcedon.
- **C7.** Every entry has `kind` `major-council` and `kindLabel` "Major council". Every person id resolves to a Who card or a census row. Every tradition id is in the census. Verdicts match the scans except Timothy of Alexandria (CON-3).
- **C8 and item 11.** All briefs are 400 words or fewer and pass `grade_text`.
- **Item 3.** No invented feeling, scene or speech was found. The scene details were checked against Eusebius (Nicaea), Ossius's letter (Sardica), Sulpicius (Ariminum), Cyril's Latin letter home (Ephesus), the Gesta (Carthage) and the acts (Chalcedon).
- **Item 4.** No rhetorical "not X but Y" contrasts. The Constantinople hit is inside a quoted canon. The Rome/Carthage hit ("Hope was not to be 'wholly denied to the lapsed,' but their penance would be long") states the decision itself, and Mark has approved that brief. Colons appear only to introduce quotations. No rhetorical questions in the narrator's voice; the three hits are quotations. No tail lines. Each close ends on a sourced fact.
- **Item 13.** All nine audio scripts equal the brief with `[calmly]` at the start and `[warmly]` before the last paragraph, and with no other tags.

## Counts

| Council | Blocking | Substantial | Minor |
|---|---|---|---|
| councils-of-rome-and-carthage-251 | 0 | 0 | 1 |
| council-of-arles-314 | 0 | 0 | 3 |
| council-of-nicaea-325 | 0 | 1 | 1 |
| council-of-sardica-343 | 0 | 0 | 2 |
| councils-of-ariminum-and-seleucia-359 | 0 | 1 | 4 |
| first-council-of-constantinople-381 | 0 | 2 | 4 |
| conference-of-carthage-411 | 0 | 1 | 2 |
| council-of-ephesus-431 | 0 | 0 | 4 |
| council-of-chalcedon-451 | 0 | 1 | 4 |
| **Total** | **0** | **6** | **25** |

Round 2 should be a targeted recheck of the six substantial findings, and of any minor fix taken. Rescore each brief whose text changes.
