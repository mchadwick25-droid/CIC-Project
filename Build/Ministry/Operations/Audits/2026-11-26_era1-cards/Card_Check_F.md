# Card check F: Ebionite / Nazoraean Current, Novatianism, Anatolian Church in the Third Century (2026-11-26)

Independent check pass (`Brief-Kit/roles/card.md`, "The check pass"), under `Header.md` in this folder (the short-description rulings, "The card standard", "Dates from the sources' own clues", "Modern works on the cards") and `Stage-Two-Kit/Kit.md` sections 1 to 3. The checker wrote none of these cards. Every timeline line of the three layouts (33, 27 and 24 lines) was opened at its cited lines in `cic/texts/`, with tags stripped and editors' notes read apart from the text. No writer's "checked by script" mark was taken on trust. For the Ebionites, `uncertain` (16) and `quotationOriginals` (6) were compared by script with the batch-11 card: word for word on both, and the batch-11 brief equals the census `longDescription`. Novatianism and Anatolia have no batch-11 folder, so each `uncertain` item was checked at its lines. A census copy outside the repository with all three layouts merged (`dates` included) gives, with `node tools/validate-census.mjs <copy>`: 1 error without the proposed scan reading (the Ebionite Q6 `printed`), 0 errors and the 4 standing shortName warnings with it. Short names as in each card's `Card_Edits`.

| Card | Verdict | Blocking | Minor |
|---|---|---|---|
| `ebionite-nazoraean-current` | FIX | 0 | 5 |
| `novatianism` | FIX | 1 | 5 |
| `anatolian-church-third-century` | FIX | 1 | 3 |

---

## 1. `ebionite-nazoraean-current`: FIX

### What holds

- **shortDescription.** Each phrase stands on its held line: the Ebionites (ANF1 33534); the Nazoraeans (Pan 24398-24399; CSEL34 23237); Jews who held Jesus the Christ (Pan 25166-25167; ANF4 39119-39121, "those Jews who have received Jesus as Christ are called by the name of Ebionites"); the Law of their fathers kept (ANF4 39113-39116); circumcision (ANF1 33540-33541); the Sabbath (HE 18726-18727); the food laws (ANF9 31918-31922). Every held witness reports this alike, so it may be told plainly. "Later church writers placed them" holds: "placed" keeps the report in its witnesses' voice, and "later" is true, since Justin, Irenaeus and Origen give no place and the places come from Epiphanius (Pan 25026-25029, 26876-26879) and Jerome (PL23 48161-48162). It does not settle whether they were one people or two. No negative, contrast, dash or placeholder opening. Grade 9.6 (names out 7.5), ease 76.2, simpler than the Montanism example (grade 17.5).
- **Timeline.** Apart from the findings below, every line holds at its lines. The Pella beginnings belong to Epiphanius alone (Pan 25029-25034, "ἐκεῖϑεν γὰρ ἡ ἀρχὴ γέγονε"; 25335-25345). The sources' differences on Jesus stand side by side (lines 11, 14, 19, 25, 32). Opponents' words stay in their voices (Origen's "poor in understanding", ANF4 34023-34026; the charge against Paul, Pan 26737-26745; Jerome's "nec Iudaei sunt nec Christiani", CSEL34 23275). Line 29 reads Jerome's Latin rightly ("describendi facultas fuit", PL23 48162-48163) where the English has "described". 392 is worked from Jerome's "fourteenth year of the Emperor Theodosius" (VI 38784-38785), with the working shown on lines 4 and 29. 404 is Widely Accepted (Source_Sheet A8). No editor's year is used (no 70, 181, 324, 375 or 428).
- **Shown dates.** "mid-2nd c. to after 404" passes the date rule and Mark's clue ruling. The start is Justin, Widely Accepted for the middle of the 2nd century (ANF1 19893-19905). Tested, "after 404" holds. Jerome writes in 404 that the sect exists "usque hodie", to this day (CSEL34 23235), so it was still there in 404 and its end, which no source gives, falls later. This is the form `Card_Check_E.md` N1 set. Augustine's "the sect still continues" (AugF 6787, about 400) comes earlier and adds nothing past 404. The change from "1st-4th c." is marked.
- **briefSources.** All nine files exist. They cover every `quotationOriginals` file, `originalFile` (Pan) and `englishFile` (VI, AugE) included.
- **uncertain** (16) and **quotationOriginals** (6). Word for word the batch-11 card's, and none contradicts the brief. Each `printed`, `original` and `englishPrinted` passes the validator at its lines. The two spans "checked at card" are correct. "an apostate from the Law" matches "apostatam eum legis" (Pan 24117) and "he was an apostate from the law" (ANF1 33537-33538). "poor" matches "Ebion signifies “poor”" (ANF4 39118-39119).
- **The proposed scan reading** (`ebionite_quote_scan_drop_entry.json`) is right against the held file. CSEL34 23237 ends the text proper ("... qui credunt in"), and 23272 resumes it ("Christum filium dei natum ..."). Lines 23238-23271 hold only blank lines and 24 non-blank lines: the parallel-passage note (23239), the apparatus (23241-23263), the page number "304" (23266) and the running head "S. Aureli Augustini" (23269). The entry's `lines_held` equals those 24 lines, trimmed, in order, which is the test at `tools/validate-census.mjs` lines 545-547. Its `scan` stands in the range. The text lines at either end are left untouched. It overlaps no other reading for this file (the only one is at line 6524). Its `kind` names what the lines are. Without it, Q6 fails ("does not stand in ... lines 23237-23275"). With it, the run is clean. Release may add it as it stands.
- **Modern works.** The nine batch-11 works are editions and translators' notes, each note saying what it covers. None is the source of a claim on the card.
- **Menu.** Every section is filled from a real field or plainly marked. People and stories: nothing held (census `people` empty, no documented story). Kind's own sections: nothing held. Sources: the short list. Modern works: held for release.

### Findings

**E1. Timeline period 4, lines 2 and 3, `when`: MINOR.** "In Origen's last years" stands on no held line, and the over-sixty age drops Eusebius's own hedge, "as they say". Line 3 also carries no reference for its date.
- Line 2 old `when`: "in Origen's last years, when he was over sixty". New: "when Origen was, as some said, over sixty".
- Line 3 old `when`: "in Origen's last years". New: "when Origen was, as some said, over sixty".
- Line 3 `reference`, old: "Origen, Against Celsus V.61, cic/texts/anf04_tertullian4-minucius-felix-commodian-origen1-2.xml lines 53648-53653". New: "Origen, Against Celsus V.61, cic/texts/anf04_tertullian4-minucius-felix-commodian-origen1-2.xml lines 53648-53653; his age, Eusebius, Church History VI.36, cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml lines 37093-37105".
- Support: HE 37093-37094 ("Origen, being, as they say, over sixty years old"), 37103-37105 ("He also at this time composed a work of eight books in answer to that entitled True Discourse").

**E2. Timeline period 4, line 6, `reference`: MINOR.** The cited lines name the versions but not their setting side by side. That stands further on in the same chapter.
- Old: "Eusebius, Church History VI.16, cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml lines 34446-34464". New: "Eusebius, Church History VI.16, cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml lines 34446-34464, 34715-34719".
- Support: HE 34715-34719 ("he divided them into sections, and placed them opposite each other ... an edition of Aquila and Symmachus and Theodotion with the Septuagint").

**E3. Timeline period 2, line 1: MINOR.** Justin's own hedge is dropped. Trypho at once takes up his "in my opinion", and the next line depends on it.
- Old text: "Justin tells Trypho, a Jew, that a man who knows Jesus is the Christ and still keeps the Law of Moses will be saved, if he does not press it on non-Jewish believers."
- New text: "Justin tells Trypho, a Jew, that in his opinion a man who knows Jesus is the Christ and still keeps the Law of Moses will be saved, if he does not press it on non-Jewish believers."
- Support: ANF1 19899-19908 ("In my opinion, Trypho, such an one will be saved"; "Why then have you said, ‘In my opinion, such an one will be saved’").

**E4. Timeline period 7, line 2, `reference`: MINOR.** The `when` "392" has no working on this line, and each line must stand alone.
- Old: "Jerome, Lives of Illustrious Men 2, cic/texts/npnf203_theodoret-jerome-gennadius-rufinus.xml lines 39327-39340; Latin, cic/texts/jerome_opera-pl23-part1-with-regula-pachomii-lat_migne1883.txt lines 48081-48084, 48126-48136".
- New: "Jerome, Lives of Illustrious Men 2, cic/texts/npnf203_theodoret-jerome-gennadius-rufinus.xml lines 39327-39340; Latin, cic/texts/jerome_opera-pl23-part1-with-regula-pachomii-lat_migne1883.txt lines 48081-48084, 48126-48136; the year, cic/texts/npnf203_theodoret-jerome-gennadius-rufinus.xml lines 38784-38785, is a conversion from the fourteenth year of Theodosius, counting his reign from 379".
- Support: VI 38784-38785 ("until the fourteenth year of the Emperor Theodosius").

**E5. Timeline period 1, headline: MINOR.** The headline names only lines 1-2. Ebion (line 3) and John's Gospel against the Ebionites (line 4) are also in this period.
- Old: "Later writers tell of a church at Pella, and Epiphanius sets both groups' beginnings there".
- New: "Later writers tell of beginnings at Pella, of a teacher, Ebion, and of John writing against the Ebionites".
- Support: HE 15291-15296; Pan 25029-25034, 25335-25345, 25230; ANF3 21552-21554; ANF5 12273-12274; VI 39566-39572.

---

## 2. `novatianism`: FIX

### What holds

- **shortDescription.** Each phrase stands on its held line: at Rome, a presbyter (VI 40887, "Novatianus, presbyter of Rome"; SOC 14061-14062). Socrates says that "on being afterwards elevated to the episcopacy" he led the separated church (SOC 14082-14084). He is named by what he was when he broke away. The name the church gave itself comes from HE 38268-38270, "call themselves Cathari", with the editor's "καθαροί, 'pure'", and from NIC 3769. The rest stands at its lines too: shut out those who had sacrificed (SOC 14088-14089, "not admit to the sacred mysteries those who had sacrificed"); Constantinople (SOC 9089-9091); Phrygia (SOC 14060-14061). Tested, "left their pardon to God" holds. These are the words of the Novatian rule itself: Novatus's letter to the churches as Socrates quotes it ("leave the pardoning of their offense to God", SOC 14088-14090), and the Novatian bishop Acesius before Constantine ("not to expect remission from the priest, but from God", SOC 3714-3716). The brief says the same ("God might forgive apostasy, but the church could not presume to"). Eusebius's hostile "as if there was no longer for them a hope of salvation" (HE 38265-38268) stays in his voice on line 8 and in `uncertain` 3. No negative, contrast, dash or placeholder opening. Grade 9.6 (names out 7.4), ease 76.8: simpler than the Montanism example.
- **Timeline.** Apart from the findings below, every line holds at its lines. Opponents' charges stay in their voices. Cornelius tells of the forced laying on of hands and the oath (HE 38518-38534, 38761-38774). Eusebius gives "no hope" (38265-38268). Cyprian gives the bribery (ANF5 33980-33985). Socrates's sources are named: the very old man (SOC 3721-3728) and the Paphlagonian peasant (9113-9115). The names Novatus and Novatian stand side by side (lines 4, 10, `uncertain` 1).
- **Shown dates.** "c. 251 to after 438" passes. The start is worked from the Chronicle's first year of Gallus and Volusianus (JerChron 43960-43973), and Gallus's accession in 251 is Widely Accepted. The end was tested. Paul dies "on the 21st of July, under the same consulate", the sixteenth of Theodosius (SOC 21469-21471, 21488-21492), so 438, a conversion from the consulate as in `Card_Check_E.md`. Marcian then succeeds him (SOC 21521-21535), and Socrates says the discipline is kept "even to the present day" (SOC 14060). So the church goes on past 438. The change from "c. 251-400s" is marked, and `end` 400 is rightly flagged, not edited.
- **briefSources.** All six files exist. The brief has no quoted span, so there is no `quotationOriginals`.
- **uncertain.** Items 1, 3, 4, 6 and 7 stand at their lines (HE 38265-38270; SOC 14061-14090, 3690-3716, 14132-14133, 15291, 15349-15366; NIC 3768-3770; VI 40887-40891; JerChron 43969-43973).
- **Modern works.** Four editions held in `cic/texts/` (Fausset, Hussey, Hartel, Fotheringham). Each note says what the edition covers. Van Dam and Gregory are rightly left for Mark.
- **Menu.** Every section is filled or marked. People and stories: four people and two documented stories. Kind's own sections: nothing held. Sources: the short list. Modern works: proposed.

### Findings

**N1. Timeline period 1, line 1: BLOCKING.** The line gives a motive the source does not give. In "ob odium eorum in Christianos persecutionem mouet", "eorum" is the two Philips: Decius persecuted the Christians out of hatred for the Philips. As written, "them" reads as the Christians. Eusebius's own History says the same as the Chronicle.
- Old text: "Eusebius's Chronicle, in Jerome's Latin, says that Decius, after killing the two Philips, father and son, began a persecution of the Christians, out of hatred for them."
- New text: "Eusebius's Chronicle, in Jerome's Latin, says that Decius killed the two Philips, father and son, and, out of hatred for them, began a persecution of the Christians."
- Support: JerChron 43895-43899 ("Decius cum Philippos patrem et filium interfecisset ob odium eorum in Christianos persecutionem mouet"); HE 37413-37414 ("On account of his hatred of Philip, he commenced a persecution of the churches").

**N2. Timeline period 1, line 1, and period 2, line 6, `reference`: MINOR.** Each year is called a conversion, but the working is not shown (Mark's clue ruling; compare `Card_Check_E.md` M4).
- Period 1 line 1, old tail: "the year is a conversion from the Chronicle's first year of Decius". New tail: "the year is a conversion from the Chronicle's first year of Decius, counting his reign from 249".
- Period 2 line 6, old tail: "the year is a conversion from the Chronicle's first year of Gallus". New tail: "the year is a conversion from the Chronicle's first year of Gallus and Volusianus, counting their reign from 251".
- Support: JerChron 43890-43899 (Decius's reign and his first year), 43913-43916 and 43960-43973 (Gallus and Volusianus; their first year). The two accession years are Widely Accepted.

**N3. `uncertain` item 2: MINOR.** "Only Cornelius ... tells it" is contradicted by two held lines. Cyprian and Socrates also say how Novatian was made bishop. Only the three country bishops and the tenth hour are Cornelius's alone.
- Old: "How he was made bishop. Only Cornelius, his rival, tells it: three country bishops brought to Rome and forced, at the tenth hour, to lay hands on him. Novatian's own account of it is not held."
- New: "How he was made bishop. Only Cornelius, his rival, tells of three country bishops brought to Rome and forced, at the tenth hour, to lay hands on him. Cyprian says he was made bishop by bribery, by the hands of deserters. Socrates says bishops who shared his views raised him to the office. Novatian's own account of it is not held."
- Support: HE 38518-38534; ANF5 33980-33985 ("strives by bribery to be made an adulterous and extraneous bishop by the hands of deserters"); SOC 14082-14084 ("elevated to the episcopacy by such bishops as entertained similar sentiments").

**N4. `uncertain` item 5: MINOR.** Socrates quotes Novatian's own letter to the churches (timeline period 4, line 1), so On the Trinity and the confessors' letter are not the only words of his party that are held.
- Old: "Their own words. Of Novatian's party, only his On the Trinity and the confessors' short letter are held in their own words. The confessors' letter was written after they had left him."
- New: "Their own words. Of Novatian's party, only his On the Trinity and the confessors' short letter are held whole in their own words. Socrates quotes a few lines of Novatian's letter to the churches. The confessors' letter was written after they had left him."
- Support: ANF5 60470-60472, 33288-33301; SOC 14086-14090 (the letter's words, in quotation marks in the print).

**N5. Timeline period 5, headline: MINOR.** "An emperor" leaves out Theodosius's law (line 6), and one emperor is not what the period holds.
- Old: "An emperor and a council deal with the Cathari, and soldiers come to Mantinium".
- New: "Constantine and Theodosius rule on the Novatians, Nicaea receives their clergy, and soldiers come to Mantinium".
- Support: HE 66068-66080; NIC 3768-3779; SOC 9103-9113, 15349-15366.

**N6. Timeline period 6, line 1: MINOR.** Two phrases go past the source. Socrates hedges the Phrygians' temper ("appear"), and he says the circus and theater are not much esteemed, not that people rarely go.
- Old text: "Socrates writes that the strict discipline of the Novatian church is kept to his own day in Phrygia and Paphlagonia, where, he says, people are temperate and rarely go to the circus or the theater."
- New text: "Socrates writes that the strict discipline of the Novatian church is kept to his own day in Phrygia and Paphlagonia, where, he says, people seem more temperate than others and care little for the circus or the theater."
- Support: SOC 14060-14061, 14109-14115 ("the Phrygians appear to be more temperate than other nations"; "nor are the sports of the circus and theatrical exhibitions in much estimation among them even to the present day").

---

## 3. `anatolian-church-third-century`: FIX

### What holds

- **Timeline.** Apart from the findings below, every line holds at its lines. The Address (ANF6 2855-2869), Eusebius on the brothers (HE 36568-36571, 36679-36684, 40580-40588, 41838-41874), Jerome (VI 40775-40793, 41095-41105), Gregory of Nyssa's seventeen (PG46 66355-66366, the city allotted to him, "ἀποκληρώσας αὐτῷ τὴν πόλιν"), the canons (ANF6 1980-2246), the Banquet (29838-29900, "Arete ... the daughter of Philosophia" at 29897-29899 in the text, not the note; 34172-34180), Socrates (SOC 18141-18154) and Basil (BAS 37060-37065, 14657-14691, 37308-37323) all stand. The wonders are kept in their witnesses' voices (Jerome, line 6; Basil, line 22). The two seventeens are given to their tellers. Jerome's two reports of Methodius's death stand side by side. Line 15 tells the eleventh canon as the letter has it. No editor's year is used (no 240, 254-258, 259-267, 311 or 312).
- **Shown dates.** "3rd to early 4th c." passes the date rule. The start is Origen at Caesarea and Gallienus (HE 36568, 40566-40588), the 3rd century Widely Accepted. The end is the outer limit of Jerome's two reports, "at the end of the recent persecution or ... in the reign of Decius and Valerianus" (VI 41102-41105). With the persecution's end in the early 4th century Widely Accepted, the sources allow no more than that. The change from "c. 240-312" is marked, and `start` and `end` are rightly flagged, not edited.
- **briefSources.** All four files exist. Basil and Socrates are rightly left out: the brief does not draw on them.
- **uncertain** (7). Each item stands at its lines, in its witness's voice (HE 36679-36684; VI 40781-40783; ANF6 2135-2136, 2227-2246; BAS 14657-14660; PG46 66362-66366; VI 40789-40793, 41095-41105; SOC 18151-18154).
- **Modern works.** One edition, Migne's PG 46, its note saying what it covers. Van Dam is rightly left for Mark.
- **Menu.** Every section is filled or marked. People and stories: three people and one documented story. Kind's own sections: nothing held. Sources: the short list. Modern works: proposed.

### Findings

**A1. shortDescription, first sentence: BLOCKING.** "Wrote rules for his churches" stands on no held line. The Canonical Letter answers another bishop's questions about "your country", and sends him Euphrosynus to deal with him "in accordance with our model here". The card's own headline (period 3) says "for a church", and the writer's own note grants that the letter answers another bishop. "A pupil of Origen" also names Gregory by what he no longer was when he was a bishop (Mark, "they were not monks when they left").
- Old: "In Pontus, Gregory, a pupil of Origen, was a bishop and wrote rules for his churches after a raid by the Goths. In Lycia, Methodius, bishop of Olympus, wrote the Banquet, where ten virgins praise chastity."
- New: "In Pontus, Gregory, who had studied with Origen, was a bishop and wrote rules for a church after a raid by the Goths. In Lycia, Methodius, bishop of Olympus, wrote the Banquet, where ten virgins praise chastity."
- Support: HE 36679-36684 ("Remaining with him five years ... honored with a bishopric in the churches of Pontus"); ANF6 2005-2006 ("most holy father"), 2135-2141 ("the Boradi and Goths"; "we have sent to you our brother ... Euphrosynus ... in accordance with our model here"), 2151-2153 ("in your country"), 2166-2168 ("forgetting that they were from Pontus"); VI 41095-41098; ANF6 29844-29855. Scored: grade 9.5 (names out 6.7), ease 80.1: pass.

**A2. Timeline period 1, line 2, `reference`: MINOR.** The cited range ends before the five years and the bishoprics.
- Old: "Eusebius, Church History VI.30, cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml lines 36568-36584". New: "Eusebius, Church History VI.30, cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml lines 36568-36571, 36679-36684".
- Support: HE 36679-36684 ("Finding them deeply interested in Greek and Roman learning ... Remaining with him five years ... both of them were honored with a bishopric in the churches of Pontus").

**A3. Timeline period 3, line 6: MINOR.** "A council of bishops" goes past the letter. Gregory writes of "the saints assembled in council".
- Old text: "Gregory writes of those who joined the raiders, forgetting they were men of Pontus and Christians, and killed their own people and showed the raiders roads and houses. They are barred even from hearing the Scriptures in church until a council of bishops decides."
- New text: "Gregory writes of those who joined the raiders, forgetting they were men of Pontus and Christians, and killed their own people and showed the raiders roads and houses. They are barred even from hearing the Scriptures in church until the saints, met in council, decide."
- Support: ANF6 2166-2178 ("until some common decision about them is come to by the saints assembled in council, and by the Holy Spirit antecedently to them").

**A4. Timeline period 4, line 5, `when`: MINOR.** "The last persecution" reads Jerome's word as a judgment of his own. He writes "the recent persecution", as the line's own text has it.
- Old: "at the end of the last persecution, or under Decius and Valerian". New: "at the end of the recent persecution, or under Decius and Valerian".
- Support: VI 41102-41105 ("At the end of the recent persecution or, as others affirm, in the reign of Decius and Valerianus").
