# Card edits: Basil of Caesarea

Starting card: `Card.existing.json` (the `card` field of `basil-of-caesarea` in `cic-website/data/world-census.json`, copied before work). New card: `basil-of-caesarea.card.json`. Brief: `basil-of-caesarea.brief.txt`. Every field not listed below is word for word.

A scratch copy of the census, with the brief as `longDescription`, this card, the `modernWorks` below and the entry-field changes below, passes `node tools/validate-census.mjs` with its full quotation check: 0 errors (4 warnings, all on other entries).

## Quotations

The brief keeps the same three quotations, word for word, as the starting card's `quotationOriginals`. No entry changed. Each cited line re-read in its file:

- Quote 1: `npnf208_basil-letters-select-works.xml` 39133-39135, "Then once upon a time, / like a man roused from deep sleep, I turned my eyes to the marvellous / light of the truth of the Gospel". Holds.
- Quote 2: `basil_opera-omnia-pg31-grc-lat_migne1857.txt` 72547-72549, Greek checked by hand: "Τίνα οὖν ἀπονίψεις ; τίνα θεραπεύσεις ; τίνος / ἔσχατος ἔσῃ, αὐτὸς καθ᾽ ἑαυτὸν διάγων ;" (whom then will you wash; whom will you care for; behind whom will you be last, living by yourself). "Feet" stands only in the sentence before (72546-72547, "ἕνιψε τοὺς πόδας τῶν μαθη-/τῶν"). Clarke's English, `basil_ascetic-works-longer-shorter-rules_clarke1925.txt` 13460-13464, holds as printed. The rendering matches the Greek.
- Quote 3: `npnf208_basil-letters-select-works.xml` 33483-33485, "As we were baptized, so / we profess our belief.  As we profess our belief, so also we offer / praise." Holds.

All three run six words or more, so each keeps its `secondReading` as it stood and none is "checked at card".

## Card fields

1. **knownFor (clearly wrong: a year only a modern editor gives, stated as fact).**
   Old: "Bishop of Caesarea in Cappadocia from 370."
   New: "Bishop of Caesarea in Cappadocia."
   Evidence: the year is Jackson's chronology (`npnf208...xml` 685-689, editor; Source_Sheet B1). The outline's Setting says it is "Told in no sentence, since only modern editors give them", and its Do not say has "Bishop from 370" → no year. Kit Part 1, Rigor: a date that rests on one editor's reckoning stays out of the story and the card. The brief says only "As its bishop". The year stays on the card in `datesNote`, credited to Jackson.

2. **legacy.traces[0] (new: the brief's source for Rufinus's Latin).**
   Old: "Gennadius says Rufinus put works of Basil into Latin. Fremantle lists first among Rufinus's works the Rule of St. Basil, put into Latin at Pinetum for the abbot Urseius in 397 or 398."
   New: the same, then "Rufinus's own preface to his Latin Rule says that the abbot Urseius asked him to turn the work into Latin, and that it gives the rules for monks of Basil, bishop in Cappadocia, which he set down as answers to the monks who questioned him."
   Evidence: `benedict-aniane_concordia-regularum-with-ardo-vita-pl103-lat_migne1851.txt` 40460-40512 (Outline I1), especially 40471 "poposcisti ut hoc opus in Latinum verterem" and 40486-40489 "sancti Basilii Cappadoci:e episcopi ... ins!tuta mona-/chorum; que interrogantibus s: monachis velut / Sancli cujusdam juris responsa slatuit, protuli" (OCR as printed). Brief: "Rufinus put his works, his rules for monks among them, into Latin."

3. **legacy.traces, new item after the Photius trace (new: the outline sends it to the card).**
   New: "Gregory of Nyssa, in a letter to his brother Peter that opens his books against Eunomius, says that when Basil died the controversy with Eunomius passed to him, and that he wrote in part to defend Basil's good name against Eunomius's abuse."
   Evidence: Outline, What came of them 2 and Cut first 14 ("his brother carrying on his answer to Eunomius ... I6 for the card"). `npnf205_gregory-nyssa-dogmatic-treatises.txt` 2787-2793 ("When our saintly Basil fell asleep, and I received the legacy of Eunomius' controversy ... spent the chief part of his energy in laboriously-written abuse of our father in God"), 2808-2810 ("It was not right to leave undefended the reputation of our noble saint").

4. **legacy.remembered, the rival-bishop item (new: Sasima, which the outline sends to the card).**
   Old ends: "... a cause of pain which even time has not obliterated."
   New adds: "Socrates says Gregory was first made bishop of Sasima, one of the cities of Cappadocia."
   Evidence: Outline, Cut first 15 and Beat 4 ("Sasima named by Socrates, `npnf202...xml` 21065-21066"); the file at 21065-21066: "Gregory was first made bishop of / Sasima, one of the cities of Cappadocia, but was afterwards transferred".

5. **legacy.remembered, new last item (new: the outline sends it to the card).**
   New: "Sozomen says Basil was a great admirer of Ephrem the Syrian and was astonished at his learning."
   Evidence: Outline, Leave out ("his admiration of Ephrem: card"). `npnf202_socrates-sozomen-ecclesiastical-histories.xml` 32065-32067 (Sozomen 3.16): "Basil, who was subsequently bishop / of the metropolis of Cappadocia, was a great admirer of Ephraim, and / was astonished at his erudition."

6. **sources.about (new: two files the card now cites).**
   Added after Gregory of Nyssa's Life of Macrina: `{"title": "Against Eunomius, with his letter to his brother Peter, in Nicene and Post-Nicene Fathers, second series, vol. 5", "author": "Gregory of Nyssa", "language": "English translation", "file": "cic/texts/npnf205_gregory-nyssa-dogmatic-treatises.txt", "date": null}`. Evidence: edit 3.
   Added after Rufinus's Church History: `{"title": "Preface to his Latin Rule of Saint Basil, for the abbot Urseius, in Patrologia Latina 103", "author": "Rufinus of Aquileia", "language": "Latin", "file": "cic/texts/benedict-aniane_concordia-regularum-with-ardo-vita-pl103-lat_migne1851.txt", "date": null}`. Evidence: edit 2; Outline I1 and Who tells it (Rufinus).

7. **sources.about (moved: three modern works, to the entry's `modernWorks`).**
   Removed from the card, word for word as they stood: Hefele, "A History of the Councils of the Church, vol. 2 (tr. H. N. Oxenham)", 1876; Morison, "St. Basil and His Rule", 1912; Gwynn, "Ephrem the Syrian, introduction and notes, in Nicene and Post-Nicene Fathers, second series, vol. 13". Evidence: the role ("a modern work now listed under the card's `sources` moves there word for word"); Outline, Who tells it, lists all three as modern. No card quotation cites their files; `uncertain` still names their claims, each credited.

8. **briefReferences[0] (new: the opening's added clauses).**
   Old ends: "... written in self-defense against Eustathius of Sebaste."
   New adds: "The same letter, lines 39105-39113: the slanderers sullying his name among the brethren; lines 39133-39137: the uselessness of the wisdom of this world."
   Evidence: brief, "against men who, he wrote, were spreading lies about him" and "the learning of this world"; `npnf208...xml` 39108-39112 ("my slanderers ... sullying my reputation among the brethren"), 39135-39137 ("the uselessness of 'the wisdom of the princes of this world'"); Outline, Opening 1.

9. **briefReferences[1] (removed: a thing the brief no longer tells).**
   Old: "... he read in the gospel of selling goods and sharing with the poor, and went looking for monks."
   New: "... he read in the gospel of selling goods and sharing with the poor."
   Evidence: brief paragraph 3 ("In his own telling, he read in the gospel of selling goods and sharing with the poor") no longer says he went looking for monks (Outline, Cut first 16). The search for monks stays in `legacy.remembered`.

10. **briefReferences[4] (removed and new: the bishops and the speech).**
    Old: "... the rival bishop who blocked his road with armed men, and the new bishops of Nyssa and Sasima. The speech is Gregory's, in praise."
    New: "... the province divided, the rival bishop who claimed part of his churches and blocked his road with armed men, and the new bishops for the province. The speech is Gregory's, in Basil's memory."
    Evidence: brief: "When the province was divided, a rival bishop claimed part of his churches and once blocked his road with armed men. Basil answered by making more bishops for the province, Gregory says" and "Gregory of Nazianzus says in his speech in Basil's memory". The brief names neither Nyssa nor Sasima, and no longer calls the speech praise. `npnf207...xml` 42569-42603 (Or. 43.58), 42609-42611 (43.59).

11. **briefReferences[5] (new: the charge).**
    Old: "Letter 94, to the governor Elias, placed in 372: whom it harms ..."
    New: "Letter 94, to the governor Elias, placed in 372: his accusers, and what harm the government suffers from him; whom it harms ..."
    Evidence: brief, "His accusers had won over the governor, and Basil wrote to ask what harm the state suffered from him"; `npnf208...xml` 29990-29991 ("come off worse than my accusers"), 30010-30011 ("what harm the government suffers from me?").

12. **briefReferences[6] (new: the book's answer).**
    Added before "Letter 159.2": "On the Holy Spirit 27, lines 14165-14170: the answer from baptism, that they must teach him not to baptize as he received, or not to believe as he was baptized, or not to give glory as he believed."
    Evidence: brief, "He answered in a book, On the Holy Spirit, that the church already baptized new believers in the name of the Father, the Son and the Holy Spirit together"; `npnf208...xml` 14165-14170 ("Him who is numbered with Them at Baptism ... either not to baptize as we have received, or not to believe as we were baptized, or not to ascribe glory as we have believed"); Outline, Beat 6.

13. **briefReferences[7] (removed and new: the impact paragraph).**
    Old: "First Council of Constantinople, 381: the Spirit worshipped and glorified with the Father and the Son, in the tree's own entry. Fremantle's note on Rufinus: the Rule put into Latin in 397 or 398. Benedict's Rule, ch. 73: Basil's Rule as an example of good living. Canon 20 of the Second Council of Nicaea, 787: the double monasteries still standing."
    New: "First Council of Constantinople, 381: the Spirit worshipped and glorified with the Father and the Son, in the tree's own entry; the creed's text in The Seven Ecumenical Councils, lines 13393-13396. Rufinus's preface to his Latin Rule, for the abbot Urseius, and Gennadius 17: his works, the rules for monks among them, put into Latin. Benedict's Rule, ch. 73: Basil's Rule as an example of good living."
    Evidence: brief, "declared in its creed that the Spirit is worshipped and glorified with the Father and the Son" (`npnf214...xml` 13393-13396, "who with the Father and the Son together is worshipped and glorified"); "Rufinus put his works, his rules for monks among them, into Latin", with no year (Outline, Do not say: the year is Fremantle's), from Rufinus's preface (edit 2) and Gennadius (`npnf203...xml` 42466-42471); the brief no longer tells the council of 787 (Outline, Cut first 17). The council of 787 stays on the card in `knownFor` and `legacy.traces`.

## Entry fields

For release to apply once the checker passes them. Release also sets `longDescription` from the brief.

1. **modernWorks (new key; place it before `card`).** The outline's modern works used to read or find the old texts (Who tells it), the three moved from the card's sources among them (card edit 7). All are vendored in `cic/texts/` as public domain by date, under the Library's rights rules (`Build/worlds/_cross-world/CORPUS-USE.md`). Each title and author is as its file or the card gives it; years only where the file or outline holds one.
   ```json
   [
    {"title": "Letters and Select Works (Nicene and Post-Nicene Fathers, second series, vol. 8)", "author": "Blomfield Jackson (tr.)", "year": "1895", "note": "English translation of Basil's letters, On the Holy Spirit and the Hexaemeron, with the translator's chronology and notes."},
    {"title": "The Ascetic Works of Saint Basil", "author": "W. K. L. Clarke (tr.)", "year": "1925", "publisher": "Society for Promoting Christian Knowledge", "note": "English translation of the Longer and Shorter Rules, with an introduction and notes."},
    {"title": "The Life of St. Macrina", "author": "W. K. Lowther Clarke (tr.)", "year": "1916", "publisher": "Society for Promoting Christian Knowledge", "note": "English translation of Gregory of Nyssa's life of his sister, with an introduction."},
    {"title": "Cyril of Jerusalem, Gregory Nazianzen (Nicene and Post-Nicene Fathers, second series, vol. 7)", "author": "Charles Gordon Browne and James Edward Swallow (tr.)", "year": "1894", "note": "English translation of Gregory of Nazianzus's orations, among them his funeral speech for Basil."},
    {"title": "Patrologia Graeca, vol. 31", "author": "J.-P. Migne (ed.)", "year": "1857", "note": "Greek and Latin edition of works of Basil, among them the Longer Rules."},
    {"title": "Patrologia Graeca, vol. 36", "author": "J.-P. Migne (ed.)", "year": "1858", "note": "Greek and Latin edition of Gregory of Nazianzus's orations 27 to 45, among them the funeral speech for Basil."},
    {"title": "Eusebius Werke, vol. 2, part 2: Die Kirchengeschichte, with the Latin of Rufinus", "author": "Eduard Schwartz and Theodor Mommsen (ed.)", "year": "1908", "note": "Edition of Rufinus's Latin Church History, whose book 11 tells of Basil."},
    {"title": "Notes on Rufinus, in Nicene and Post-Nicene Fathers, second series, vol. 3", "author": "W. H. Fremantle", "note": "Introduction to Rufinus's life and works, with a list of his translations."},
    {"title": "Ephrem the Syrian, introduction and notes, in Nicene and Post-Nicene Fathers, second series, vol. 13", "author": "Gwynn", "note": "Introduction and notes to Ephrem the Syrian, with a chronology of his time."},
    {"title": "The Rule of Saint Benedict", "author": "Francis Aidan Gasquet (tr.)", "year": "1925", "note": "English translation of Benedict's Rule, with an introduction."},
    {"title": "The Rule of St. Benedict", "author": "D. Oswald Hunter Blair (ed. and tr.)", "year": "1907", "note": "Latin text of Benedict's Rule with an English translation and notes."},
    {"title": "The Seven Ecumenical Councils (Nicene and Post-Nicene Fathers, second series, vol. 14)", "author": "Henry R. Percival (ed.)", "note": "English translation of the councils' creeds and canons, among them the creed of 381 and the canons of 787."},
    {"title": "A History of the Councils of the Church, vol. 2 (tr. H. N. Oxenham)", "author": "Karl Joseph von Hefele", "year": "1876", "note": "History of the church councils from 326 to 429, from their documents."},
    {"title": "St. Basil and His Rule", "author": "E. F. Morison", "year": "1912", "note": "Study of Basil's rules for monks and their place in early monasticism."}
   ]
   ```
   Evidence: Outline, Who tells it (Jackson, Clarke, Browne and Swallow, Migne PG 31 and PG 36, Schwartz and Mommsen, Fremantle, Gwynn, Gasquet and Hunter Blair, Percival, Hefele, Morison). Years and publishers from the file headers (`basil_ascetic-works...clarke1925.txt`, `gregory-nyssa_life-of-macrina_clarke1916.txt`, the two Migne files, `eusebius_werke...schwartz-mommsen1908.txt`, the two Benedict files, `hefele...1876.txt`, `morison...1912.txt`) or the outline (Jackson 1895; Browne and Swallow 1894). Names inside the NPNF files: Jackson `npnf208` 476; Browne and Swallow `npnf207` 22257, 22264; Fremantle `npnf203` 695, 43997; Gwynn `npnf213` 10425; Percival `npnf214` 410.

2. **why (a year only an editor gives; a claim the brief no longer makes).**
   Old: "Basil was bishop of Caesarea in Cappadocia from about 370. ... A council in 787 told double monasteries to keep his rule, and later churches call him "the Great"."
   New: "Basil was bishop of Caesarea in Cappadocia. ... In the sixth century Benedict of Nursia pointed his monks to Basil's rule as an example of good living, and later churches call him "the Great"."
   Evidence: the year is Jackson's (card edit 1); the brief no longer tells the council of 787, and tells instead "In the sixth century Benedict of Nursia closed his own Rule by pointing his monks to Basil's as an example of good living."

3. **relationsSummary (a claim the brief no longer makes).**
   Old: "... He made his brother and his friend bishops, and the friend resented it for years."
   New: the sentence removed. The field reads: "Told within the Cappadocians, with his brother Gregory of Nyssa and his friend Gregory of Nazianzus. He wrote On the Holy Spirit against those who ranked the Spirit below the Father and the Son."
   Evidence: the brief tells only "Basil answered by making more bishops for the province, Gregory says", naming neither the brother nor the friend nor the hurt (Outline, Do not say: the brother's bishopric is not this story; Cut first 15).

4. **teaser (a claim the brief no longer makes).**
   Old: "Caesarea in Cappadocia, c. 329 to 379 CE: a bishop who defended the Spirit's place beside the Father and the Son, and wrote a rule for monks that a council and Benedict still named."
   New: "Caesarea in Cappadocia, fourth century CE: a bishop who defended the Spirit's place beside the Father and the Son, and wrote a rule for monks that Benedict still named."
   Evidence: the brief no longer gives a year of death ("He died in 378 or 379" is gone; Outline, Do not say), and gives the time as "in the fourth century"; it no longer tells the council of 787.

## Not found

- `placeNote`, "The monastery on the river Iris in Pontus": no old source held names the Iris for Basil's own community. Basil's Letter 14 describes the place and its river without a name (`npnf208...xml` 23988-24006); the Iris is in Jackson's chronology (`npnf208...xml` 600-605) and Clarke's introduction (`gregory-nyssa_life-of-macrina_clarke1916.txt` 78). The outline rates it Widely Accepted (Setting; Source_Sheet E7). Left in place.

## Left as they stand

- The card's credited modern dates and views (`datesNote`; `keyWorks` "placed in"; `legacy.traces` Fremantle; `legacy.remembered` Jackson's 358; `uncertain` Hefele, Morison, Jackson) are each credited to their editor. The outline sends them to the card (Who tells it; Leave out), as the `cyril-and-methodius` card does with its editors.
- Entry `legacy` and `voices` are not among the fields this role lists. The entry `voices` line "whom he made bishop of Sasima" stands on Or. 43.59 and Socrates, and the card does not contradict it.
