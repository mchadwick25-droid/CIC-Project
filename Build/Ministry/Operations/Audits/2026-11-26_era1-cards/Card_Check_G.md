# Card check G: Roman Palestine before Constantine, Third-Century Rome, Third-Century Antioch (2026-11-27)

Independent check pass (`Brief-Kit/roles/card.md`, "The check pass"), under `Header.md` in this folder (the short-description rulings, "The card standard", "Dates from the sources' own clues", "Modern works on the cards") and `Stage-Two-Kit/Kit.md` sections 1 to 3. The checker wrote none of these cards. Every timeline line of the three layouts (36, 53 and 44 lines) was opened at its cited lines in `cic/texts/`, with tags stripped and editors' notes read apart from the text. No writer's "checked by script" mark was taken on trust. For Rome and Antioch, `uncertain` and `quotationOriginals` were compared by script with the batch-11 cards, and each batch-11 brief equals its census `longDescription`. A census copy outside the repository with all three layouts merged (`dates` included) gives, with `node tools/validate-census.mjs <copy>`: 2 errors without the proposed scan readings (the two Antioch Greek `original` fields), 0 errors and the 4 standing shortName warnings with them. Short names as in each card's `Card_Edits`; Lib = `liber-pontificalis_texte-introduction-commentaire-t1-lat-fra_duchesne1886.txt`.

| Card | Verdict | Blocking | Minor |
|---|---|---|---|
| `palestinian-church-pre-constantinian` | FIX | 1 | 9 |
| `roman-church-third-century` | FIX | 0 | 5 |
| `antiochene-church-third-century` | FIX | 0 | 5 |

---

## 1. `palestinian-church-pre-constantinian`: FIX

### What holds

- **shortDescription.** Each phrase stands on a held line. Origen taught at Caesarea (E 36568-36571). Pamphilus was a presbyter (E 47072-47074) and gathered the library (VI 39360-39361, 40958-40962; E 36890-36893). He was put to death at Caesarea (VI 40969-40970). Eusebius was his friend (VI 41076-41077) and wrote the Martyrs of Palestine (E 45924-45925). The coast rests on the brief, and also on E 46450 (the sea threw the body out "before the gates of the city"). No negative, contrast, dash or placeholder opening. Each man is named by what he was then. On "simpler": it is far simpler than the Montanism example (grade 17.5, one 38-word sentence). The 11.7 grade comes from the names (7.9 names out), so it passes Mark's grade ruling. One phrase fails "clear heard once" (P1).
- **Timeline.** Apart from the findings below, every line holds at its lines. Period 4 rests on Eusebius alone and names him once at its head. The wonder of Apphianus's body stays in his voice (line 29, with its note). No editor's year is used: no 212, 216, 306 or 310, and the documented story's "2 April 306" and "16 February 310" are not used. About 231 is worked from Eusebius's tenth year of Alexander (E 36330-36331; 35554-35556), and 303 from the nineteenth year of Diocletian (E 45893). "309 or 310" holds. Tested: the two-year imprisonment (E 47106-47107) after Pamphilus was jailed in the fifth year (E 46622-46624, 46694-46705) could narrow it to 310. But that count depends on how Eusebius reckons his years, and he is inconsistent: Apphianus is dated to the third year, Theodosia to the fifth, both on 2 April. So the range the clues allow stands. Line 8's "Antoninus, who followed Macrinus" is Jerome's own clue (VI 40745-40747), and Jerome's Latin Chronicle "legationis industriam ... suscipiente Iulio Africano" (JerChron 43627-43630) supports "led the embassy".
- **Shown dates.** "early 3rd to early 4th c." passes the date rule. The start is Widely Accepted for Alexander's coming and Origen's first stay (E 33426-33532, 35303-35322), and Jerome's "after Macrinus" places Africanus there. The end, the easing after the seventh year (E 47405-47408), is Widely Accepted for the early 4th century. 185 and 312 rest on no held line. The change is marked.
- **briefSources.** All three files exist. The card has no quotation, so no `quotationOriginals`, as the brief quotes nothing.
- **uncertain** (6, new). Each holds at its lines in its witness's voice: E 36330-36334 and VI 40589-40591 (1); E 47119-47134, 46750-46751, 47406, VI 40969-40970 (2); E 36883-36894, 47082-47084, VI 39359-39361, 40958-40968 (3); VI 40745-40748, JerChron 43627-43633 (4); ANF4 35069-35070, 35150-35151, which give Agnomon and Bassus (5); E 46438-46451 (6). Item 3 has a wording fault (P10).
- **Modern works.** Fotheringham's 1923 edition of Jerome's Chronicle is an edition, and its file header confirms the title, editor, year and publisher. Its note says what it covers.
- **Menu.** Every section is filled or marked. People and stories: census `people` (4), `voices` (5), `documentedStories` (3), as listed. Kind's own sections: nothing held (no `entry`). Connections: `relationsSummary` and edges. Legacy and today: `legacy`, `livingEvidence`. Open questions: `uncertain`. Sources: `briefSources`. Modern works: proposed.

### Findings

**P1. shortDescription: MINOR.** "In the persecution" fails "clear heard once". It names no persecution, so it leans on knowledge the visitor lacks. Here is a simpler replacement on held lines, with every name and claim kept. It scores grade 10.5 (names out 6.4), reading ease 83.2, 38 words.
- Old: "At Caesarea, on the coast of Roman Palestine, Origen taught, and the presbyter Pamphilus gathered a library of Christian books. In the persecution Pamphilus was put to death there, and his friend Eusebius wrote down how the martyrs of Palestine died."
- New: "At Caesarea, on the coast of Roman Palestine, Origen taught and the presbyter Pamphilus gathered a library. Pamphilus was put to death there for his faith, and his friend Eusebius wrote down how the martyrs of Palestine died."
- Support: E 36568-36571; E 47072-47074; VI 39360-39361, 40958-40962; VI 40969-40970 ("put to death at Caesarea in Palestine"); E 47194-47195 ("manifested an unchangeable zeal for the faith"); VI 41076-41077; E 45924-45925; E 46450.

**P2. Timeline period 4, line 30, `text`: BLOCKING.** The line gives the wrong count. Eusebius says twelve in all, with Pamphilus as their leader, so twelve died, not twelve plus Pamphilus.
- Old: "Eusebius writes that twelve were martyred with Pamphilus, a man thrice dear to him and the only presbyter at Caesarea among them. Pamphilus shared his goods with the needy and was devoted to the Scriptures."
- New: "Eusebius writes that Pamphilus, a man thrice dear to him, died with others, twelve in all, and was the only presbyter at Caesarea among them. Pamphilus shared his goods with the needy and was devoted to the Scriptures."
- Support: E 47066-47074 ("of those who finished their course with him. They were twelve in all ... Of these the leader and the only one honored with the position of presbyter at Caesarea, was Pamphilus").

**P3. Timeline period 4, `headline`: MINOR.** "His household" overstates. Only Porphyry was of his household. Seleucus was a soldier-confessor, and the rest were fellow prisoners.
- Old: "The persecution comes to Caesarea, and Apphianus, Pamphilus and his household die". New: "The persecution comes to Caesarea, and Apphianus, Pamphilus and his companions die".
- Support: E 47069 ("those who finished their course with him"); 47201 ("one of the household servants of Pamphilus"); 47247-47248.

**P4. Timeline period 4, line 32, `text`: MINOR.** The question "if they would now obey" was put to Pamphilus and his companions after the Egyptians had been dealt with. "The same single answer" is also unclear on its own.
- Old: "Eusebius writes that the five Egyptians were brought before the judge with Pamphilus and his companions, and that each of them gave the same single answer when asked if they would now obey."
- New: "Eusebius writes that on that day the five Egyptians were brought before the judge with Pamphilus and his companions. Asked if they would now obey, Pamphilus and his companions each gave only one answer, their last confession."
- Support: E 47127-47134; 47186-47198 ("he proceeded against Pamphilus and his companions ... asked them if they would now obey. And receiving from every one of them only this one answer, as their last word of confession in martyrdom").

**P5. Timeline period 3, `when`: MINOR.** "Before the persecution of Diocletian" stands on no held line. Eusebius met Pamphilus in Agapius's time, and no line dates Agapius, the copying or the Apology before 303.
- Old: "Before the persecution of Diocletian, date unknown". New: "In Pamphilus's lifetime, date unknown".
- Support: E 42996-43046; VI 40958-40970.

**P6. Timeline period 3, line 20, `text`: MINOR.** "He came to know Pamphilus" can be read as Agapius. Eusebius writes "we became acquainted".
- Old: "Eusebius writes that while Agapius was bishop of Caesarea, he came to know Pamphilus, an eloquent man of philosophic life and a presbyter there. He says he wrote a separate work on Pamphilus's life, his school and his trials."
- New: "Eusebius writes that he came to know Pamphilus while Agapius was bishop of Caesarea, and calls him an eloquent man of philosophic life and a presbyter there. He says he wrote a separate work on Pamphilus's life, his school and his trials."
- Support: E 42996-43046 ("In his time we became acquainted with Pamphilus, that most eloquent man, of truly philosophical life, who was esteemed worthy of the office of presbyter in that parish").

**P7. Timeline period 2, line 15, `text` and `reference`: MINOR.** Origen asks the question in scorn, and his next sentence answers it, so "He asks whether" softens his force.
- Old text: "Origen answers Africanus at length, saying his few days in Nicomedia left him little time. He asks whether the churches should throw out the copies of Scripture in use among them and ask the Jews for copies free from forgery."
- New text: "Origen answers Africanus at length, saying his few days in Nicomedia left him little time. He asks, in scorn, whether the churches must throw out the copies of Scripture in use among them and coax the Jews for copies free from forgery, as if Providence had not cared for the churches."
- Old reference: "Origen, Letter to Africanus, cic/texts/anf04_tertullian4-minucius-felix-commodian-origen1-2.xml lines 35131-35147,  35244-35250". New: "Origen, Letter to Africanus, cic/texts/anf04_tertullian4-minucius-felix-commodian-origen1-2.xml lines 35131-35147, 35244-35254".
- Support: ANF4 35244-35254 ("And, forsooth, when we notice such things, we are forthwith to reject as spurious the copies in use in our Churches ... and to coax the Jews ... free from forgery! Are we to suppose that that Providence which in the sacred Scriptures has ministered to the edification of all the Churches of Christ, had no thought for those bought with a price").

**P8. Timeline period 2, line 12, `reference`: MINOR.** Athenodorus, "his brother", stands at line 36676, outside the cited lines.
- Old: "Eusebius, Church History VI.30, cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml lines 36568-36571,  36679-36684". New: "Eusebius, Church History VI.30, cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml lines 36568-36571, 36676, 36679-36684".
- Support: E 36676 ("and his brother ... Athenodorus").

**P9. `reference` fields, spacing: MINOR.** Eight references carry a double space after a comma between line ranges (lines 12, 15, 17, 18, 25, 27, 29, 32). In each, replace ",  " with ", ". P7 and P8 already give lines 15 and 12 in full.

**P10. `uncertain` item 3: MINOR.** "Are not held" is the project's word, not a visitor's.
- Old: "Eusebius's three books on the life of Pamphilus, where he listed it, are not held."
- New: "Eusebius's three books on the life of Pamphilus, where he listed it, are not among the texts this card draws on."
- Support: E 36889-36893, 47082-47084 (the three books named); no held file carries them.

---

## 2. `roman-church-third-century`: FIX

### What holds

- **shortDescription.** Each phrase stands on its held line: H 13672-13674 (a slave), 13816-13819 (bishop after Zephyrinus), E 35447-35449 (Hippolytus "has left writings"), H 13873-13875 (the charge), E 37413-37414 and CyL 1126-1127 (Decius, the forced sacrifice), E 38272-38299 (sixty bishops, the fallen healed "with the medicines of repentance"). Hippolytus's charge stays in his voice ("said"), as the header requires. 251 is Widely Accepted. No negative, contrast, dash or placeholder opening. Clear on one reading. Grade 10.0 (names out 8.6), 45 words in two sentences: simpler than the Montanism example.
- **Timeline.** Apart from the findings below, every line holds at its lines. Every Callistus charge in period 2 is in Hippolytus's voice, with the period's witness note. Wonders stay with their witnesses: the angels (line 4), the dove (line 26, "tells it as a report", E 36508 "They say"). The sources' differences stand side by side: Callistus's years (Eusebius, E 35477-35482, against the list, Lib 66797-66799; the second print at Lib 66686 agrees on "ann. V m. II d. X"), and the split of 251 (E 38265-38270 against Lib 66825-66827). The consular years 235 and 250 are worked from the list's consuls (Lib 66807, 66819-66820). No editor's year is used.
- **Shown dates.** "c. 201 to late 3rd c." passes the date rule and the clue ruling. 201 is worked from "about the ninth year of the reign of Severus" (E 32210-32211). The end is Eusebius's placing of the letter to Dionysius of Rome in Aurelian's reign (E 41936-41954, 41993-42001), Widely Accepted for the late 3rd century. The change is marked.
- **briefSources.** All four files exist. They cover every `quotationOriginals` file (H, CyL; H as `englishFile`).
- **uncertain.** Items 1, 3, 4 and 5 are word for word the batch-11 card's. The writer's change to item 2 is right. The words "lifted up with arrogance against these persons, as if there was no longer for them a hope of salvation" are Eusebius's own narrative (E 38265-38268), placed before Cornelius's letter, which begins at 38380. Cornelius's own words give only the confessors ("using as a cloak for his rebellion those confessors who had adhered to him from the beginning", E 38383-38387). The new item still agrees with the brief.
- **quotationOriginals** (3). Word for word the batch-11 card's. Each `printed` and `englishPrinted` stands at its lines (by script, and passed by the validator). None is under six words.
- **Modern works.** Hartel (1871), Schwartz and Mommsen (1908) and Duchesne (1886) are editions. Titles, editors, years and places match the file headers. Each note says what it covers.
- **Menu.** People and stories: census `people` (Caius, `hippolytus-of-rome`, Cornelius, Dionysius of Rome), `voices` (6), `documentedStories` (2). Kind's own sections: nothing held. The rest as listed.

### Findings

**R1. Timeline period 2, line 10, `text` and `reference`: MINOR.** Hippolytus's chief charge against Callistus's past is left out: that he made away with money deposited with him. So is the reason Hippolytus gives for the synagogue disturbance, a wish to meet death. The header names this enemy's charge, and it belongs in the witness's voice.
- Old text: "Hippolytus writes that Callistus was a household slave of Carpophorus, a believer in the emperor's household. After Callistus caused a disturbance in a synagogue on the Sabbath, he says, the city prefect Fuscianus had Callistus scourged and sent to a mine in Sardinia."
- New text: "Hippolytus writes that Callistus was a household slave of Carpophorus, a believer in the emperor's household, and charges that he made away with money that widows and brothers had deposited with him. Later, he says, Callistus caused a disturbance in a synagogue on the Sabbath, hoping to meet death, and the city prefect Fuscianus had him scourged and sent to a mine in Sardinia."
- Old reference: "Hippolytus, Refutation of All Heresies IX, cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml lines 13672-13674,  13690,  13726-13751". New: "Hippolytus, Refutation of All Heresies IX, cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml lines 13672-13690, 13725-13751".
- Support: H 13683-13686 ("entrusted to him not a few deposits by widows and brethren ... Callistus, however, made away with all"); 13725 ("planned an artifice by which he hoped to meet death"); 13726-13751.

**R2. Timeline period 6, line 2, `when` and `reference`: MINOR.** By Mark's clue ruling, the list of bishops gives the year. It sets Xistus's death in the consulship of Tuscus and Bassus, on the eighth of the Ides of August, which is the day Cyprian gives. The conversion is the same as for 235 and 250 on this card.
- Old `when`: "under Valerian, on the eighth day of the Ides of August". New: "258, in the consulship of Tuscus and Bassus, on the eighth day of the Ides of August".
- Old reference: "Cyprian, Letters 81 in the English numbering, tr. Wallis, cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml lines 41156-41186; Xistus as bishop of Rome, Eusebius, Church History VII.27, cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml lines 41758-41759". New: "Cyprian, Letters 81 in the English numbering, tr. Wallis, cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml lines 41156-41186; Xistus as bishop of Rome, Eusebius, Church History VII.27, cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml lines 41758-41759; the year, the list of Rome's bishops in the Chronograph of 354, ed. Duchesne, cic/texts/liber-pontificalis_texte-introduction-commentaire-t1-lat-fra_duchesne1886.txt lines 67074-67076, is a conversion from the consuls the list names".
- Support: Lib 67074-67076 ("Xystus ... usque Tusco et Basso [258], et passus est VIII id. aug."); the second print, Lib 66908-66909, agrees; H 41184-41185.

**R3. Timeline period 6, line 3, `note` (new) and `reference`: MINOR.** The old sources differ here, and the card says so elsewhere (line 12). Eusebius's eleven years for Xistus stand against the list's figure. Paul's becoming bishop also stands outside the cited lines.
- `note`, old: none. New: "The list of Rome's bishops in the Chronograph of 354 gives Xistus two years, eleven months and six days."
- Old reference: "Eusebius, Church History VII.27, cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml lines 41758-41785". New: "Eusebius, Church History VII.27, cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml lines 41758-41785, 41835-41836".
- Support: Lib 67074 ("Xystus ann. II mens. XI d. VI"), 66908; E 41835-41836 ("received that episcopate").

**R4. Timeline period 1, line 6, `text`: MINOR.** "Churchman" is not at the cited lines. Eusebius writes "a very learned man".
- Old: "Eusebius writes that Caius, a learned churchman, held a dialogue at Rome under Zephyrinus with Proclus, who argued for the Phrygian heresy, as Eusebius calls the New Prophecy."
- New: "Eusebius writes that Caius, a very learned man, held a dialogue at Rome under Zephyrinus with Proclus, who argued for the Phrygian heresy, as Eusebius calls the New Prophecy."
- Support: E 35451-35457 ("a dialogue of Caius, a very learned man, which was held at Rome under Zephyrinus, with Proclus, who contended for the Phrygian heresy").

**R5. `reference` fields, spacing: MINOR.** Eight references carry ",  " (a double space) between line ranges. In each, replace ",  " with ", ". R1 already gives line 10 in full.

---

## 3. `antiochene-church-third-century`: FIX

### What holds

- **shortDescription.** Each phrase stands on its held line: Paul made bishop (E 41835-41836), the bishops' many meetings (E 41894-41899), cut off for his teaching (E 41936-41954), Lucian a presbyter of Antioch put to death for his confession (VI 40995-41001; E 48018-48023), "fellow-Lucianist" (Thdt 6063-6064, the batch-11 outline's gloss "a pupil of Lucian"). "In Roman Syria" rests on the brief. No negative, contrast, dash or placeholder opening. Grade 10.4 (names out 8.8), simpler than the Montanism example. One phrase is unclear (A1).
- **Timeline.** Apart from the findings below, every line holds at its lines. Period 4 rests on the bishops' letter, named once at its head, and each charge is in its writers' voice. The two placings of the last meeting stand side by side: Aurelian's reign, E 41936-41937, and the Chronicle's thirteenth and fourteenth years, JerChron 44278-44287. So do the two accounts of who wrote the letter (E 41993-41997; VI 40904-40911) and the three later reasons on homoousion. "Dictating" in line 15 follows the Greek ὑπαγορεύων in E-Gk, where McGiffert has "reciting". About 260 is worked from the Chronicle's seventh year (JerChron 44185-44187, 44213-44215). No editor's 264, 268, 269, 272 or 312 is used, and Zenobia is never given as the cause of the ruling.
- **Shown dates.** "late 2nd to early 4th c." passes the date rule. Serapion is Widely Accepted for the late 2nd century (E 30535-30562). Lucian's death under Maximinus is Widely Accepted for the early 4th (E 48018-48023; VI 40999-41000). The change is marked.
- **briefSources.** All seven files exist. They cover every `quotationOriginals` file, `originalFile` included.
- **uncertain** (12) and **quotationOriginals** (3). Word for word the batch-11 card's. None contradicts the brief. Each `printed` stands at its lines. The renderings match their originals: the aorist παύσας against the present παρασκευάζων (Q1); the Latin of Q2; the Greek of Q3. Item 5's "Hilary says" is held from batch 11 and maps across as it stands under the header. The timeline line is corrected at A4.
- **The proposed scan readings** (`antiochene_quote_scan_readings.json`) are right against the held files. E-Gk line 11897 reads "10 »τοὺς uir εἰς τὸν κύριον ...". The 10 is Schwartz's margin numbering in fives, and line 11900 opens "15". The reading "»τοὺς" removes only that number. No other reading exists for this file. Epiph-Gk line 45745 holds only "ec - 2 -" (trailing space), so `lines_held` equals its trimmed content, which is the test at `tools/validate-census.mjs` lines 545-547. Lines 45744 and 45746 carry the text on either side. It overlaps none of the other readings for this file (43852, 45736, 45737, 45738). Without the readings the run shows the two Greek `original` errors. With them it is clean. Release may add both as they stand.
- **Modern works.** Schwartz and Mommsen, Oehler, Migne PG 50 and Fotheringham are editions. Each note says what it covers.
- **Menu.** People and stories: census `people` (Serapion, Malchion), `voices` (5), `documentedStories` (1). Kind's own sections: nothing held. The rest as listed.

### Findings

**A1. shortDescription: MINOR.** "Bishops met many times over their bishop" reads, on one hearing, as the bishops' own bishop. It scores grade 10.5 (names out 8.9), 45 words.
- Old: "In Antioch, in Roman Syria, bishops met many times over their bishop, Paul of Samosata, and put him out of the church for what he taught about Christ. Later Lucian, a presbyter of Antioch, died for his faith, and Arius called himself his pupil."
- New: "In Antioch, in Roman Syria, bishops met many times over the bishop there, Paul of Samosata, and put him out of the church for what he taught about Christ. Later Lucian, a presbyter of Antioch, died for his faith, and Arius called himself his pupil."
- Support: E 41835-41836 ("received that episcopate", of Antioch, 41783-41785); E 41894-41899; 41936-41954.

**A2. Timeline period 7, line 8, `text` and `reference`: MINOR.** The reason is not Hilary's own. He gives it as the second reason in the letter he answers. Only the eighty bishops are in his own voice.
- Old text: "Hilary of Poitiers writes that the fathers who condemned Paul rejected the word homoousion, because Paul had used it to teach that God was single and undivided. He says eighty bishops once rejected it."
- New text: "Hilary of Poitiers, answering a letter that set out reasons against the word homoousion, writes that its second reason was that the fathers who condemned Paul rejected the word, because Paul had used it to teach that God was single and undifferentiated. He says himself that eighty bishops once rejected it."
- Old reference: "Hilary, On the Councils 81, 86, tr. Watson, cic/texts/npnf209_hilary-poitiers-john-damascus.xml lines 9607-9611,  9772-9773". New: "Hilary, On the Councils 81, 86, tr. Watson, cic/texts/npnf209_hilary-poitiers-john-damascus.xml lines 9594-9611, 9772-9773".
- Support: Hil 9594-9611 ("Your letter on the meaning of ὁμοούσιον ... The second reason that you added was that our fathers, when Paul of Samosata was pronounced a heretic, also rejected the word ὁμοούσιον, on the ground that ... he had taught that He was single and undifferentiated"); 9772-9773 ("Eighty bishops once rejected it").

**A3. Timeline period 4, line 1, `text`: MINOR.** "Took" softens the bishops' charge. They write "extorts", as `uncertain` item 6 has it.
- Old: "The bishops write that Paul, once poor, grew rich on what he took from the brothers, promising for a reward to help people in trouble and then deceiving them."
- New: "The bishops write that Paul, once poor, grew rich on what he extorted from the brothers, promising for a reward to help people in trouble and then deceiving them."
- Support: E 42084-42101 ("through those things which he extorts from the brethren").

**A4. Timeline period 2, line 1, `reference`: MINOR.** "Paul of Samosata received the office" stands at 41835-41836, after the editor's note, outside the cited lines.
- Old: "Eusebius, Church History VII.27, cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml lines 41758-41785". New: "Eusebius, Church History VII.27, cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml lines 41758-41785, 41835-41836".
- Support: E 41835-41836 ("received that episcopate").

**A5. `reference` fields, spacing: MINOR.** Four references carry ",  " (a double space) between line ranges. In each, replace ",  " with ", ". A2 already gives line 8 of period 7 in full.
