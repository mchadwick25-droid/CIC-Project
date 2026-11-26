# Card edits: Alexandrian Christianity (`alexandria-catechetical`)

Starting card: `Card.existing.json` (the census entry's card fields; a tradition has no `card` field). New card: `alexandria-catechetical.card.json`. Brief: `alexandria-catechetical.brief.txt` (final after `Grade2_Fixes_Applied.md`). Every field and item not listed below is word for word, in the same order: `why`, `sourcing`, `floorNote`, `relationsSummary`, `voices` and `people` are unchanged. The new keys (`uncertain`, `quotationOriginals`) come at the end. File keys (E-en, E-gr, Cl, Ph, Soc, GN, Ath, HP) are those of `Source_Sheet.md`; line numbers are file lines in `cic/texts/`.

## How a tradition's card is shaped here

As in this batch's other tradition cards: `tools/validate-census.mjs` has no card for a tradition (`checkCard` refuses a `card` on anything but a person, and `checkQuotationOriginals` runs only for persons and councils). So the card file keeps the entry's own fields; `sources` keeps the page's format (`work`, `type`, `note`, `url` where held) with `file` added to each item; `quotationOriginals` follows `cyril-and-methodius`; `uncertain` is a list. A tradition page home and a validator check for `uncertain` and `quotationOriginals` do not exist yet (for release).

## Quotations

The brief has five quoted spans. They make three quotations, since the narrator breaks Clement's and Dionysius's each once ("that is, to those who cannot read"; "he wrote"). Each quotation has one entry whose `modern` is its spans joined, the form the validator reads as one entry ("A quotation the text breaks around 'he says' or an ellipsis is one entry"). Each `modern` is the outline's rendering and the brief's words. All three run six words or more (25, 18 and 14), so none carries `secondReading`, and none is "checked at card". If the checker counts "Faith is taught without letters" (5 words) as a quotation of its own, it would need its own entry with "checked at card"; I read it as half of one quotation, as Outline Cut first 10 and Quote 2 do.

A scratch check (the validator's `fold` and its four held-text forms, tags and notes stripped) finds each `printed` and `original` at its lines, each file in `sources`, and each `modern` among the brief's quoted runs.

1. **Herais.** `printed` (English): E-en 32918-32925, "And of women, Herais … died while yet a catechumen, receiving baptism by fire, as Origen himself somewhere says." (endnote 1798 stands between "Herais" and "died"; re-read). `original`: E-gr 1613-1614, as the scan prints it ("xci", "“Hoais", "χατηχουμένη"; re-read, Greek checked by hand: καὶ γυναικῶν δὲ Ἡραΐς ἔτι κατηχουμένη τὸ βάπτισμα, ὥς πού φησιν αὐτός, τὸ διὰ πυρὸς λαβοῦσα, τὸν βίον ἐξελήλυθεν). The English confirms the damaged Greek, so the original is carried (role: a damaged scan prints its English alone "unless another held print confirms the reading"). `uncertain` names the scan faults and "he himself" = Origen (Outline, Quote 1).
2. **Clement.** `printed`: Cl 26369-26372, from "And faith is the possession" to "a spiritual book." (re-read; the outline's 26369-26371 stops before the line holding "is called love—a spiritual book", which is 26372). Clement's Greek is not held (Source_Sheet, file keys), so the English stands alone. `uncertain`: the brief gives the sentence's last two clauses; "rude" rendered "unpolished" (Outline, Quote 2).
3. **Dionysius.** `printed`: E-en 41368-41369, "if the reason given satisfied us, we were not ashamed to change our opinions and agree with others" (re-read). `original`: E-gr 10734-10735, given as the validator joins a line-end hyphen ("αἰδού- / σμεροι" read as "αἰδούσμεροι"). Greek checked by hand: μήτε, εἰ λόγος αἱροίη, μεταπείθεσθαι καὶ συνομολογεῖν αἰδούμενοι; the scan's "cíooi" is αἱροίη, whose variants Schwartz's apparatus gives at E-gr 10750 ("24 αἴροι EBD …"), and the "they" variant of the governing verb stands at E-gr 10747 ("ἐποιοῦντο"). `uncertain` carries both, and that "we" is Dionysius and the believers together (Outline, Quote 3; Do not say, "Dionysius changed his mind").

## Card fields

1. **legacy, paragraph 2 (clearly wrong: a modern claim; and new, What came of it 1).**
   Old: "Basil of Caesarea and Gregory of Nazianzus studied his books. The two are credited with a book of pieces from his work, the Philocalia."
   New: "Basil of Caesarea and Gregory of Nazianzus studied his books. A fifth-century church historian, Socrates, says they drew from them \"the right interpretation of the sacred Scriptures.\" Gregory sent a friend \"the volume of the Philocalia of Origen,\" a book of passages from his work that opens with chapters on Scripture and how to read it."
   Evidence: the joint editing is the editor's heading (GN 47442-47443) and the editors' prolegomena, modern (Source_Sheet F2, Modern works); Kit Part 1, Rigor: an identification only a modern work makes stays out of the card. Soc 13913-13915 ("procured Origen's works, and drew from them the right interpretation of the sacred Scriptures"); GN 47450-47451 ("we send you the volume of the Philocalia of Origen"); Ph 14-18 (contents: I. Of the Inspiration of the Divine Scripture; II. That the Divine Scripture is closed up and sealed …) and Ph 76. Outline, What came of it 1 ("Card"). The editor's date "about 382" is not used (Outline).

2. **legacy, new paragraph 3 (new: What came of it 3).**
   Old: (none; inserted between paragraphs 2 and 3)
   New: "The school ran on. In Eusebius's own day, Achillas, a presbyter, or elder, of Alexandria, \"was placed over the school of the sacred faith.\""
   Evidence: E-en 43201-43204 ("Achillas, who had been appointed a presbyter in Alexandria … He was placed over the school of the sacred faith"); Outline, What came of it 3 ("Card"); Source_Sheet C18. "presbyter, or elder": the brief's gloss.

3. **legacy, paragraph on the monks (clearly wrong: a modern opinion stated on the card).**
   Old: "One modern reading finds Origen's ideas in Antony's letters. But Athanasius of Alexandria shows him as a boy raised at home by Christian parents, a boy who would not be taught to read."
   New: "In his Life of Antony, Athanasius of Alexandria shows the monk as a boy raised at home by Christian parents, a boy who would not be taught to read."
   Evidence: the only support for the desert link is modern (Rubenson; Source_Sheet E, last item; Outline, Leave out); Kit Part 1, Rigor ("never used for its opinion"); role check 1 ("No modern opinion … is stated as content anywhere on the card"). The modern work goes to `modernWorks` (Entry fields). With the sentence gone, "him" had no antecedent, so "In his Life of Antony" and "the monk" name him. Ath 31215-31223 ("as they were Christians he also was reared in the same Faith … brought up with his parents, knowing nought else but them and his home … he could not endure to learn letters"). "Whether the tradition also fed Egypt's monks is still argued." stays (the census edge is Contested).

4. **legacy, last paragraph (new: Outline, Leave out, History of the Patriarchs legend → "card").**
   Old ends: "Yet the same book honors Dionysius of Alexandria as patriarch."
   New adds: "It also tells a legend of how he came to the faith: a pagan philosopher, he bought some of Paul's letters from an old widow, read them, and was baptized."
   Evidence: HP 11712-11734 ("formerly a worshipper of idols … and a philosopher … an aged widow, holding in her hand a book containing some of the epistles of saint Paul … Wilt thou buy this from me?"), HP 11884-11890 ("gave him the complete epistles of Paul. And Dionysius read them … Demetrius received Dionysius, and baptized him"). Late legend (Source_Sheet F5): told as a legend.

5. **sources[0] Stromata, sources[1] De Principiis (file added).** `file`: Cl (anf02) and `cic/texts/anf04_tertullian4-minucius-felix-commodian-origen1-2.xml` (holds De Principiis). Work, type, note and url word for word.

6. **sources[2] Eusebius, Book VI, note (clearly wrong: a modern opinion; and new: Cut first and Leave out items).**
   Old: "The source of the traditional picture of Alexandria as one continuous school with a succession of appointed heads — the very account modern scholars now question."
   New: "The source of the traditional picture of Alexandria as one continuous school with a succession of appointed heads; Clement's and Origen's own surviving words describe teachers and pupils, never a head's office. It tells of Origen's pupils who were put to death under Severus, among them Heraclides, still a catechumen, and Hero, just baptized. When the bishop, Demetrius, put the instruction in Origen's hands alone, Origen gave up teaching grammar, which he thought did not fit with training in the faith. Men and women alike came to study with him. He taught the gifted geometry, arithmetic and then the philosophers, and the less learned the basics, saying both would help them understand Scripture. It keeps a letter in which Alexander, a bishop of Jerusalem who had known them, calls Pantaenus and Clement \"master.\" And it quotes the charge of Porphyry, a pagan philosopher who wrote against the Christians, that such readers \"boast that the plain words of Moses are enigmas,\" and that Origen took the figurative reading of the Greek mysteries and applied it to the Jewish Scriptures. Eusebius answers that Porphyry lies when he says Origen came over from the pagans, since his parents had taught him the faith."
   Evidence, sentence by sentence: the old-source side of the debate replaces the modern one (Source_Sheet H, first item; B1). Cut first 12: E-en 32914-32916. Cut first 7: E-en 32796-32813 ("entrusted to him alone by Demetrius … considered the teaching of grammatical science inconsistent with training in divine subjects"). Cut first 6: E-en 33201-33203 ("with women as well as men"). Cut first 2 and 9: E-en 34818-34843. Cut first 1 (Alexander's line): E-en 34353-34356 ("Pantænus, the truly blessed man and master, and the holy Clement, my master"); Outline: "do not say he studied in Alexandria" (it does not). Porphyry (Outline, Leave out: "Card, in its own content"): E-en 34962-34982 ("boast that the plain words of Moses are enigmas"), 35122-35124 ("Becoming acquainted through them with the figurative interpretation of the Grecian mysteries, he applied it to the Jewish Scriptures"), 35189-35198 ("in the third book of his work against the Christians … plainly utters a falsehood … when he says that he went over from the Greeks … the doctrine of Christ was taught to Origen by his parents"); Source_Sheet E and H. `file` added: E-en.

7. **sources[3] Bardy (moved).** Removed from the card's `sources`, word for word as it stood; it goes to the entry's `modernWorks` (Entry fields 3). Role: "a modern work now listed under the card's `sources` moves there word for word".

8. **sources, new items (the old sources the brief and card draw on; each with `file`).**
   - **Eusebius, Church History, Book V** (E-en). Note carries Cut first 8 and the rest of Cut first 1: E-en 28488, 28537-28539, 28561-28576 ("a school of sacred learning … established there in ancient times, and as we have been informed … Pantænus … educated in the philosophical system of those called Stoics"); "about 180": E-en 28467-28476 (the first year of Commodus; Source_Sheet B1, Widely Accepted). "a school of Greek philosophers": Source_Sheet E's gloss for Stoics. Told as Eusebius's report ("he was told").
   - **Eusebius, Church History, Book VII** (E-en). The brief's Beat 4 and ending (E-en 41287-41381). Cut first 5: E-en 41312-41316 ("his extensive psalmody, with which many of the brethren are still delighted"). Cut first 11: E-en 41379-41381 ("expressed their gratification at the conference, and at the spirit of conciliation and harmony which all had manifested"). Leave out, Dionysius's vision ("card"): E-en 39552-39577 ("I examined the works and traditions of the heretics … a certain brother among the presbyters restrained me … a vision sent from God … Read everything which thou canst take in hand"); a wonder, kept in his voice ("Dionysius says"). Achillas: E-en 43201-43204.
   - **Eusebius, Books VI and VII, Greek, ed. Schwartz** (E-gr). The originals of Quotes 1 and 3 (E-gr 1613-1614, 10734-10735).
   - **Clement, The Instructor** (Cl). D1 (Cl 18711-18729) and D2 (Cl 19998-19999), the brief's Beat 1; Quote 2. Cut first 10 ("The card keeps the full passage"): Cl 26366-26370 ("It is said, I have not learned letters; but if thou hast not learned to read, thou canst not excuse thyself in the case of hearing, for it is not taught. And faith is the possession not of the wise according to the world, but of those according to God"), told in the note in plain words.
   - **Origen, Philocalia, tr. Lewis** (Ph). The brief's three senses (Ph 76); its opening chapters (Ph 14-18).
   - **Socrates, Church History, Book IV** (Soc). Edit 1 (Soc 13913-13915, chapter 26 "Of Basil of Cæsarea, and Gregory of Nazianzus", Soc 13856); Didymus (Soc 13797-13816; Source_Sheet F3, "for the card", already in `voices`).
   - **Gregory of Nazianzus, Letter 115** (GN 47438, 47450-47451). Edit 1.
   - **Athanasius, Life of Antony** (Ath 31215-31223). Edit 3.
   - **History of the Patriarchs, part 1** (HP 10942-10943 "books full of lies"; 11706-11710; 11712-11734; 11884-11890). Edit 4 and the existing last paragraph. No compiler named: the attribution to Severus is the editor's (Source_Sheet, Modern works).

9. **uncertain (new: the fuller qualifications the outline and sheet hold).** Three items:
   - Whether there was one school: Source_Sheet B1 ("as we have been informed"), H, first item; Outline, essence ("'school' as Eusebius's word, Contested as an institution"). Eusebius names the head in each generation: E-en 28637-28645, 33040-33044, 36330-36339, 36552-36559.
   - What Nepos taught: Source_Sheet C13, H ("Nepos's teaching survives only in his opponents' words"); Outline, Who tells it ("book lost").
   - The three days: Source_Sheet C17, H ("Dionysius's account … is his own, of his own success"); Outline, Beat 4 ("Eusebius gives no year") and Do not say ("no source dates the visit to his years as bishop").

Every Cut first item marked "card" is on the card: 1 (Alexander in the Book VI note; Stoics in Book V), 2, 6, 7, 9 and 12 (Book VI note), 5 and 11 (Book VII note), 8 (Book V note), 10 (Instructor note). Items 3, 13 and 14 are marked Leave out. The outline's Leave out items marked "card" are on it: Porphyry (Book VI note), Dionysius's vision (Book VII note), the History of the Patriarchs legend (edit 4), Didymus as a late head (already in `voices`). What came of it 1 and 3: edits 1 and 2. Opening 2 (the boy Origen and his father, "for the card or Leave out") is left out: it is Origen's own story and no card field fits it. Fixes_Grade2's cuts 1c and 1d ("→ card") were withdrawn by Recheck_Grade2 (MINOR 2) and stayed in the brief, so they are not added. Fixes.md M14 ("stays on the card") refers to What came of it items 1 and 2: item 1 is edit 1, item 2 is told in the brief.

## Entry fields

For release to apply once the checker passes them. Release also sets `longDescription` from the brief.

1. **legacy, sources, uncertain, quotationOriginals:** edits 1 to 9 above and Quotations. These live on the entry; the card file holds them.
2. **relationsSummary (Kit Part 1: a modern judgment on the card).**
   Old: "A contested influence on Desert Monasticism, real at one disputed point and denied as a general continuation; scholarship parent of the Bethlehem Circle"
   New: "A contested influence on Desert Monasticism; scholarship parent of the Bethlehem Circle"
   Evidence: "real at one disputed point and denied as a general continuation" states a modern reading (Rubenson, on the census edge) as content; the held old sources tested do not carry the link (Ath 31215-31223, 32982-32984; Source_Sheet E, last item; Outline, Leave out). The role says to leave connections to other entries out for now; this changes no connection, only the wording, and the checker may hold it back on that ground.
3. **modernWorks (new).** The works the outline used to read its old texts (Source_Sheet, Modern works; Outline, Who tells it), the moved Bardy item, and Rubenson (Source_Sheet: "Modern works list only"):

```json
[
 {"title": "Aux origines de l'École d'Alexandrie", "author": "Gustave Bardy", "year": "1932", "note": "The 1932 study that first argued, against Eusebius's tidy succession-list, that Alexandria's teaching looked more like a sequence of private Christian tutors than one formal institution — the opening move in a scholarly debate that remains unsettled today."},
 {"title": "Nicene and Post-Nicene Fathers, second series, 1: Eusebius, Church History, Life of Constantine", "author": "Arthur Cushman McGiffert (tr.)", "year": "1890", "note": "English translation of Eusebius's Church History, with notes on its dates, names and sources."},
 {"title": "Eusebius Werke, zweiter Band: Die Kirchengeschichte, zweiter Teil (Die griechischen christlichen Schriftsteller)", "author": "Eduard Schwartz and Theodor Mommsen (ed.)", "year": "1908", "note": "The Greek text of Books VI to X of Eusebius's Church History, with the manuscripts' readings, and Rufinus's Latin beside it."},
 {"title": "The Philocalia of Origen", "author": "George Lewis (tr.)", "year": "1911", "publisher": "T. & T. Clark, Edinburgh", "note": "English translation of the Philocalia, the book of passages chosen from Origen's works."},
 {"title": "Ante-Nicene Fathers 2: Fathers of the Second Century", "author": "Alexander Roberts and James Donaldson (ed.); William Wilson (tr. of Clement)", "year": "1885", "note": "English translations of Clement of Alexandria's Instructor and Miscellanies, among other works."},
 {"title": "Nicene and Post-Nicene Fathers, second series, 2: Socrates, Sozomenus: Church Histories", "author": "A. C. Zenos (tr. of Socrates)", "year": "1890", "note": "English translation of Socrates's Church History, with notes."},
 {"title": "Nicene and Post-Nicene Fathers, second series, 4: Athanasius, Select Works and Letters", "author": "Archibald Robertson (ed.)", "year": "1892", "note": "English translations of Athanasius's works, among them the Life of Antony."},
 {"title": "Nicene and Post-Nicene Fathers, second series, 7: Cyril of Jerusalem, Gregory Nazianzen", "author": "Charles Gordon Browne and James Edward Swallow (tr. of Gregory)", "year": "1894", "note": "English translation of Gregory of Nazianzus's orations and letters, with the editors' headings and notes."},
 {"title": "History of the Patriarchs of the Coptic Church of Alexandria, part 1 (Patrologia Orientalis 1)", "author": "B. Evetts (ed. and tr.)", "year": "1904", "note": "The Arabic text of the History of the Patriarchs, with an English translation and the editor's notes."},
 {"title": "The Letters of St. Antony", "author": "S. Rubenson", "note": "A study of the letters ascribed to Antony."}
]
```

   Held details: Lewis's publisher and year from the file's header (Ph 3-5); Evetts from HP's header; Browne and Swallow at GN 22257-22264; Wilson at Cl 54282; Zenos at Soc 479. Rubenson's year is given on the sheet only as "1990/1995", so it is left out. Not added: Jackson (npnf208, 1895), which the sheet names only for a claim about the Philocalia, not as a tool the outline used.
4. **why:** no change (see Not found).
5. **teaser:** the entry has none; nothing to change.

## Conflicts

- **Bardy's note.** The role moves it "word for word", and check 1 asks that a `modernWorks` note say "what it covers, never what it argues". The note as it stands says what Bardy argued. Kept word for word as the role says; if the checker rules for check 1, a note in the form of the others would be: "A study of the early history of Christian teaching at Alexandria."
- **Source_Sheet, Modern works:** Browne and Swallow's and Jackson's claim that Basil and Gregory edited the Philocalia together is marked "Card only, credited to them". Check 1 and Kit Part 1 keep a modern identification off the card, so it is not on the card; it was the claim edit 1 removed.
- **Didymus (voices[4], unchanged).** "no surviving primary account actually says so" stands against Rufinus, who studied with him: Didymus became "scholae ecclesiasticae doctor", the church school's teacher, approved by Athanasius (E-gr 29902-29903, Rufinus's Latin History XI.7). "doctor" is teacher, not head, so the voice is not clearly wrong; left in place for the checker to weigh. Rufinus's line is not on the source sheet.

## Not found (left in place)

- why: "confident that Greek philosophy could serve Christ rather than threaten him" is near Origen's own reason for teaching the philosophers (E-en 34818-34843; C9, E-en 35259-35270) but no held line says it so; "a method that shaped how much of the church has read the Bible ever since".
- sourcing: "school-institution question is live scholarship"; that no public-domain English of Clement's fullest treatment of marriage and the body has been made.
- floorNote: Origen's speculations, "his bishop condemned his ordination, not his doctrine", "around 399–400", the council three centuries later (no held line on the sheet; the Origen story's ground).
- voices[0]: Pantaenus "converted from Stoicism" (Eusebius says only "educated in the philosophical system of those called Stoics", E-en 28571-28576). "the true, the Sicilian bee" stands at Cl 27493.
- voices[2]: Origen "the first Christian to attempt a systematic account of the faith".
- voices[4]: Didymus "lost his sight at four" (Socrates says "at a very early age", Soc 13810-13812); "taught in Alexandria for decades"; that none of the Tura books has been translated into English.
- voices[5]: Potamiaena "a young woman"; "her story, never her own words".
- legacy, paragraph 1 (whole); paragraph 2, "He set the standard for taking seriously the languages they were first written in" and "Ambrose and Jerome read him closely too, even when they were careful about saying so".
- sources[1] note: "condemned by a church council three centuries after Origen's death".
- Bardy: the 1932 date and the title are not held (Source_Sheet: "Not held").

## Validator

A scratch copy of the census, kept outside the repository, with this card merged into the entry, the brief as `longDescription` and the `modernWorks` above: `node tools/validate-census.mjs <copy> --skip-quotes` gives 629 movements, 736 edges, 10 eras, 0 errors, 4 warnings, all on other entries (short names). The full run with the quote check was stopped by the machine for memory before it finished. As above, the validator checks no tradition's `quotationOriginals` or prose quotes, so the quotation check is the scratch fold check under Quotations.
