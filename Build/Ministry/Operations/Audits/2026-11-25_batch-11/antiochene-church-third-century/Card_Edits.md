# Card edits: The Church of Antioch in the Third Century

Card: `antiochene-church-third-century.card.json`. A tradition has no `card` field, so the card file holds the census entry's card fields, as `Card.existing.json` does, in the same order. `why`, `relationsSummary`, `teaser` and `documentedStories` are left word for word in the card file; their changes are listed under **Entry fields** for release. Every other field not listed here is word for word from `Card.existing.json`. Four new keys follow at the end: `uncertain`, `sources`, `briefReferences`, `quotationOriginals`.

**Format note for the checker and release.** `tools/validate-census.mjs` sets key lists only for a person's `card` and a council. It sets none for a tradition, and it checks a tradition's quotations nowhere (`checkQuotes` runs for persons and councils only). So `sources` takes the form the census already uses for traditions (a list of `work`, `type`, `note`), with `file` added so that each quotation's file is cited. `quotationOriginals` uses the person-card keys. Checked: a scratch census copy outside the repo, with these fields at the top level of the entry, the brief as `longDescription` and the Entry-field changes for `modernWorks`, gives 0 errors with `node tools/validate-census.mjs <copy> --skip-quotes`. `python tools/list_second_readings.py <folder>` finds all 3 spans, each READ BLIND. I re-checked each `printed` and `original` against its lines with the validator's fold rule. All three `printed` pass. Both Greek `original`s pass once the two scan readings below are in place.

## Clearly wrong (card fields)

1. `voices[0]` (Paul of Samosata).
   - Old: "bishop of Antioch and Palmyrene official, deposed for teaching that Christ was a man indwelt by the Word,"
   - New: "bishop of Antioch, deposed on the charge of refusing to confess that the Son of God came down from heaven,"
   - Evidence: only an editor's note makes him Zenobia's official (McGiffert, note at E-Eng 42105-42116); the letter gives only the title ducenarius (E-Eng 42103-42110, C2). Outline Do not say: "Paul was Zenobia's official". The Word-indwelling teaching was in the old text and is gone from the brief. The bishops' charge is that he "is unwilling to acknowledge that the Son of God has come down from heaven" (E-Eng 42173-42175; E-Gk 11903-11904, οὐ βούλεται συνομολογεῖν). The brief's sentence: "When their own bishop was charged with refusing to confess that the Son of God came down from heaven...". Part 1: no identification that only a modern work makes may go on the card.
2. `voices[1]` (Malchion).
   - Old: "and drafted the letter that deposed him"
   - New: "and, by Jerome's account, drafted the letter that deposed him"
   - Evidence: Eusebius says the pastors prepared it "by common consent" (E-Eng 41993-41994). Jerome alone names Malchion (Thdt 40908-40911). The old sources differ, so the card credits each (Part 1, fault 1). Outline Do not say: "Malchion wrote the letter". Right: "Jerome alone names Malchion (M3): card".
3. `voices[4]` (Aurelian).
   - Old: "settled the dispute by asking which claimant Italy recognized"
   - New: "settled the dispute by ordering the church's house given to those to whom the bishops of Italy and Rome wrote"
   - Evidence: E-Eng 42324-42327; E-Gk 12118-12120 (τούτοις νεῖμαι προστάττων τὸν οἶκον, οἷς ἂν οἱ κατὰ τὴν Ἰταλίαν καὶ τὴν Ῥωμαίων πόλιν ἐπίσκοποι τοῦ δόγματος ἐπιστέλλοιεν). Brief: "he ordered that the house go to the side the bishops of Italy and Rome wrote to." Do not say: "Aurelian asked who was in communion with Rome".
4. `sourcing`.
   - Old: "Malchion's synodal letter"
   - New: "the synodal letter"
   - Evidence: as edit 2. The same sentence already calls it "the collective act of a council". Jerome's attribution moves to `uncertain` (edit 9c).
5. `legacy`: the last three sentences removed, one added.
   - Old: " The Antiochene way of reading Scripture, carried by Diodore, Theodore of Mopsuestia and Chrysostom, may also go back to Lucian's work on the text. No ancient source draws that line. If it does, this century began two things the next four centuries spent arguing about."
   - New: " Paul's own followers kept a church of their own: the council of Nicaea ruled that the "Paulianists" who came over to the Catholic Church must be rebaptized, and that their clergy found blameless be rebaptized and ordained again."
   - Evidence, removal: the census rates the link to the Antiochene exegetes Inferential-Thin. The slate says it "stays out", the outline's Do not say bars it, and Source Sheet Impact 5 rates it Inferential-Thin. Part 1: a claim the outline rates Inferential-Thin stays out of the story and the card. The "If it does" sentence depends on it.
   - Evidence, addition: outline, What came of it 3, "For the card"; Nicaea canon 19, `npnf214` 5296-5306: "Concerning the Paulianists who have flown for refuge to the Catholic Church, it has been decreed that they must by all means be rebaptized; and if any of them who in past time have been numbered among their clergy should be found blameless and without reproach, let them be rebaptized and ordained".

## New (card fields)

6. `quotationOriginals`: one entry for each of the brief's three quoted spans, each `modern` copied exactly from the brief. No `secondReading` is set, since every span runs six words or more.
   - Q1, the Easter psalms. `printed`: McGiffert, E-Eng 42165-42168. `original`: Schwartz's Greek, E-Gk 11896-11900, printed as the scan reads it, with `uncertain` naming its faults (uir, veo, 77, xai). The reading is confirmed by Rufinus (E-Gk 11951-11955, "in medio ecclesiae") and McGiffert. Greek checked by hand against the rendering: παύσας ὡς δὴ νεωτέρους καὶ νεωτέρων ἀνδρῶν συγγράμματα / ἐν μέσῃ τῇ ἐκκλησίᾳ τῇ μεγάλῃ τοῦ πάσχα ἡμέρᾳ ψαλμῳδεῖν γυναῖκας παρασκευάζων / ὧν καὶ ἀκούσας ἄν τις φρίξειεν. It matches.
   - Q3, Lucian's answer. `printed`: Fronton du Duc's Latin, Chrys 15435-15440 (the Greek is not legible in the held scan, and no English is held). `uncertain` says so, and notes the stray full stop after "ille". Checked against the rendering clause by clause: it matches.
   - Q2, Arius's farewell. `printed`: Jackson, Thdt 6063-6064 (the endnote inside the span is left out). `original`: Epiphanius's Greek, Epiph-Gk 45744-45746, as the scan reads it, with `uncertain` naming "iv" (ἐν), the note mark "5" and the stray line. The reading is confirmed by Jackson. Greek checked by hand: Ἐρρῶσθαί σε ἐν κυρίῳ εὔχομαι, μεμνημένον τῶν θλίψεων ἡμῶν, Συλλουκιανιστά. It matches.
   - **Scan readings for release to add** (`tools/quote_scan_readings.json`, if the card is ever checked by rule): `eusebius_werke-...schwartz-mommsen1908.txt` line 11897, scan "10 »τοὺς", reads "»τοὺς" (a margin line number); `epiphanius_panarion-haer-48-69-...oehler1860.txt` line 45745, drop, lines_held ["ec - 2 -"] (scan marks between two lines of text).
7. `sources` (new): twelve old works, one for each file the card cites: E-Eng, E-Gk, Thdt (Theodoret I.1-4 and Jerome's Lives 71, 77), Epiph-Gk, Philost, Chrys, Soz, Ath, Hil, Bas, Nic, JerChr. Each title and translator comes from the source sheet's abbreviation list (lines 7-19), and each note from what the card uses it for.
8. `briefReferences` (new): twelve lines, one for each run of the brief, with the lines it draws on. These are the outline's beats and the source-sheet rows S1, S3, T1, T2, G3, G5-G7, C3, C4, M1, M2, M5, M6, A1, L2, L3, L4, L5, L6, L11, Ar1-Ar3, each re-read at its lines. One correction to the sheet: Ar3 (Thdt 5278-5283) is Theodoret Book 1, chapter 1, not chapter 2.
9. `uncertain` (new), the items the outline sends to the card:
   - a. Date of the last synod (D1): Eusebius places it in Aurelian's reign (E-Gk 11548-11550, καθ' ὃν after Αὐρηλιανῷ; E-Eng 41913-41940); Jerome's Chronicle places it beside Gallienus XIII-XIIII (JerChr 44280-44287). The editor's 268 is not given.
   - b. Number of bishops (D2): Eusebius "a great many" (E-Eng 41936-41940); Athanasius "the seventy" (Ath 58995); Hilary "Eighty bishops" (Hil 9772-9773).
   - c. Who wrote the letter (D4): E-Eng 41993-41994; Thdt 40908-40911.
   - d. Why the council refused homoousios (D3; What came of it 2): Ath 58970-58981, 59053-59057; Hil 9607-9611; Bas 27366-27368. Each is credited, and none is told as fact.
   - e. The bishops' other charges: Cut first 3, 4 and 6 and Ruled 1 and 2 (C1, C2, C7, C8 with its qualifier, C9 with its reason). Sources: E-Eng 42084-42110, 42178-42201, 42203-42245. "ducenarius, an imperial official's title" is the clarification only (McGiffert's note; outline Words to explain).
   - f. Dionysius of Alexandria's letter (Cut first 1; G1, G2): E-Eng 41840-41851, 42032-42042.
   - g. Domnus (Cut first 7; M6): E-Eng 42274-42314.
   - h. Aurelian's ruling "most equitably" (Ruled 4; A1): E-Eng 42326. This is McGiffert's English for αἰσιώτατα, so the words in quotation marks are the cited file's own.
   - i. Jerome's copies of Lucian's Scriptures (Ruled 5; L1): Thdt 40995-40998.
   - j. Philostorgius's list of the pupils' sees (Cut first 2; L6, L7): Philost 138, 178.
   - k. Lucian's creed (D6; L14): Soz 31022-31035.

## Entry fields (for release; not edited in the card file)

10. `why`, clearly wrong in four places:
    - "In 268, a council of bishops at Antioch deposed Paul of Samosata." becomes "A council of bishops at Antioch deposed Paul of Samosata." Evidence: D1. Eusebius sets the final synod under Aurelian, and Jerome near Gallienus's thirteenth and fourteenth years. 268 is an editor's reckoning (E-Eng 41936-41951), and Do not say bars any year.
    - "He taught that Christ was a man the Word had come to dwell in, rather than the Word made flesh." becomes "The bishops wrote that he said Jesus Christ was from below, and Eusebius says he held that Christ was by nature an ordinary man." Evidence: this is the brief's own sentence (T1, T2). The old claim is gone from the brief, and Paul's own teaching is Contested.
    - "The bishops found his conduct just as troubling, including" becomes "The bishops also wrote against his conduct, including". Evidence: the letter says that, since he is outside the faith, it is not necessary "that we should pass judgment upon his practices" (E-Eng 42079-42084), and "we think it unnecessary to demand of him an explanation of these things" (42262-42269).
    - "He would not leave until the emperor Aurelian retook the city in 272. Aurelian settled the matter by asking which claimant was in communion with the bishops of Italy and Rome." becomes "He would not leave the church's house until the emperor Aurelian was petitioned. Aurelian settled the matter by ordering the house given to the side the bishops of Italy and Rome wrote to." Evidence: A1. Do not say: no source puts the victory before the petition, and Aurelian did not ask who was in communion with Rome. The retaking is gone from the brief.
11. `teaser`: "the bishop of the greatest city in the East" becomes "the bishop of Antioch". Evidence: Do not say, "the greatest city of the Roman East": no held line. The phrase is gone from the brief.
12. `relationsSummary`: "Paul of Samosata taught adoptionism and Sabellius taught modalism." becomes "Paul of Samosata was charged with making Christ an ordinary man, and Sabellius taught modalism." Evidence: "adoptionist" was in the old text and is gone from the brief. It is a later label told as Paul's own teaching, which is Contested (T1, the word "common man" being Eusebius's). Part 1 does not allow it unexplained.
13. `modernWorks` (new on the entry): `{"title": "Notes to Eusebius, Church History", "author": "Arthur Cushman McGiffert", "year": "1890", "note": "Explains the words ducenarius and secretum in the bishops' letter."}`. Evidence: outline Who tells it (McGiffert's notes clarify ducenarius and secretum), and source sheet Modern works. Rights: an 1890 print, held as `npnf201`. The sheet's other modern works (Bardy, Loofs, Hefele and others) were set aside and used for nothing, so they are not listed.
14. `documentedStories[0]`: the modern work in its `sources` moves word for word to a new `documentedStories[0].modernWorks`. Remove `{"work": "Rowan Williams, Arius: Heresy and Tradition, rev. ed. (Eerdmans, 2002)", "type": "reference", "note": "On the ‘Lucianist’ connection and its limits."}` from `sources` and add `{"title": "Arius: Heresy and Tradition, rev. ed.", "author": "Rowan Williams", "year": "2002", "publisher": "Eerdmans", "note": "On the ‘Lucianist’ connection and its limits."}`. This was checked in the scratch census copy, with 0 errors.

## Flagged, not changed

- `documentedStories[0].text` is a narrated text of its own. It says Chrysostom preached "three generations later"; the brief says "Two generations later". It also gives "7 January 312" and "nine years", which the outline's Do not say bars as not held in old text, and a revision "used across the Greek East for centuries", which is not in the sheet. A fix to that text is a batch of its own, so it is left for Mark or the release to decide.
- `people[1].year` 268 (Malchion) rests on the editor's dating (D1). No held source gives a year to put in its place, so it is left in place.
- `sourcing`: "Serapion's fragments fall just before this window" conflicts with the entry's own dates (c. 190-312) and Serapion's year 191. No held source decides it, so it is left in place.

## Not found (left in place)

- `sourcing`: "about three thousand words".
- `voices[2]`: "martyr in 312". The old sources say only "under Maximinus".
- `voices[3]`: Serapion "bishop about 191 to 211" (outside this story's sources).
- `voices[4]`: "in 272". Jerome's Chronicle sets Zenobia's defeat near Antioch in Aurelian's second year (JerChr 44052-44054), but no number is held.
- `legacy`: "Eastern bishops who were not Arians".
- `relationsSummary`: "Aetius, the first Anomoean teacher".
