# Card edits: The Latin Apologists (`latin-apologists`, tradition)

Card written: `latin-apologists.card.json`, from `Card.existing.json`. Every field not listed below is word for word. File abbreviations as in `Source_Sheet.md` (ANF3, ANF4, ANF6, ANF7, NPNF2-1, NPNF2-3, NPNF2-6, NPNF1-3, MinLat, ArnLat, JerChron, Monc3, LactLat, Mansi 8). Each cited line was re-read in its file.

**For release, placement.** As with `montanism-the-new-prophecy`, a tradition has no `card` key, and `tools/validate-census.mjs` runs `checkCard` and `checkQuotes` only for a person or a council. The new fields `uncertain`, `sources` (`ownWords` and `about`, in the `cyril-and-methodius` form), `briefReferences` and `quotationOriginals` are written in the card format; where they live on a tradition entry is release's call. `why`, `teaser` and `relationsSummary` sit in the card file because `Card.existing.json` carries them; their changes are entry fields (below).

**Validator.** A scratch census outside the repository, with the card merged into the entry, the brief as `longDescription` and the Entry-field changes below, gives 629 movements, 736 edges, 0 errors (`--skip-quotes`; the full run was killed for memory). The same four new fields were then run as a person card: every `printed` and `englishPrinted` stands at its lines, each `modern` matches its span in the brief, and all three spans are covered. The only errors were the expected ones (person-only keys, and `secondReading` not yet set).

## Clearly wrong (corrections)

| # | Field | Old words | New words | Evidence |
|---|---|---|---|---|
| 1 | sourcing | also survives complete | also survives | Jerome: six books On ecstasy and "many small works, which are not extant" (NPNF2-3 40510-40516). |
| 2 | sourcing | Tertullian's own dates, roughly 197 to 220, are the best anchored of the set. | Tertullian's own time, the reigns of Severus and Caracalla by Jerome's account, is the best anchored of the set. | 197 rests on an editor's reckoning (ANF3 1443-1446; Outline, Do not say "in 197"). Jerome: "flourished chiefly in the reign of the emperor Severus and Antoninus Caracalla" (NPNF2-3 40498-40499). |
| 3 | floorNote | the census's own Montanism entry states plainly that the New Prophecy | the census's own Montanism entry states that, by Tertullian's account and Hippolytus's for most of them, the New Prophecy | The live Montanism floorNote now reads "by his account, and Hippolytus's for most of them, it held the same doctrine as the churches that condemned it" (world-census.json, montanism-the-new-prophecy), on Hippolytus, ANF05 13127-13138. |
| 4 | voices[0] | who opened the whole enterprise in 197, forged most of the Latin vocabulary of Christian argument, and grew | who wrote his Apology at Carthage around 200 and grew | Jerome puts him after Victor and Apollonius (NPNF2-3 40494-40495); 197 an editor's date (ANF3 1443-1446); the coined vocabulary a modern claim (Outline, Do not say; Kit Part 1, Rigor). The brief: "At Carthage around 200, Tertullian ... in his Apology". |
| 5 | voices[1] | gives the pagan side the better speech | gives the pagan side its full case | "The better speech" is a modern judgment the brief no longer makes (approved brief: "gives the other side the better speech"); in the dialogue Caecilius is "beaten" and yields (ANF4 19475-19508). Outline beat 1: "Minucius ... gives the pagan the full case" (ANF4 17582-17690). |
| 6 | legacy | The Latin vocabulary of Christian argument was made here. Tertullian coined most of the technical words Western Christians still use for the Trinity and the sacraments, and left lines | (new sentences, see New, legacy) ... Tertullian left lines | Coined vocabulary: modern claim, out of story and card (Outline, Do not say and "On the slate's ..."; Kit Part 1, Rigor); the brief no longer makes it. |
| 7 | legacy | ; the Western habit of thinking about God, the church, and the sacraments in legal and forensic categories owes a great deal to a man trained as an advocate. | . | A modern judgment (Kit Part 1, Rigor); "Tertullian the lawyer" is a Do not say (only "well versed in the laws of the Romans", NPNF2-1 10272). |
| 8 | legacy | Minucius Felix gave the West its model for the apologetic dialogue and preserved, inadvertently, the most complete record of what educated Romans actually said against the church. Arnobius is now read mostly by historians of Roman religion, who need him precisely because he described in detail the thing he was trying to demolish. | (removed) | Modern judgments, and claims the brief no longer makes (approved brief: "the fullest surviving statement", "the most detailed account of Roman religious practice"). Kit Part 1: short texts may not repeat them. |
| 9 | documentedStories[0].text | Lactantius gives no name, only that he was of high rank | Lactantius gives no name; Eusebius says he was of high rank | Lactantius has only "A certain person" (ANF7 10174); the rank is Eusebius's, "not obscure but very highly honored with distinguished temporal dignities" (NPNF2-1 43834-43835). |
| 10 | documentedStories[0].sources | the Barnes line | removed to `documentedStories[0].modernWorks` (Entry fields) | Role: a modern work under `sources` moves to modernWorks. |

## New

- **legacy** (new sentences, before the kept "Tertullian left lines ..." and "And Lactantius' Latin ..."): Lactantius's judgments of Minucius (ANF7 4470), of Tertullian's eloquence (ANF7 4472: "skilled in literature of every kind; but in eloquence he had little readiness") and of the Apology as answering accusers only (ANF7 4565-4571), What came of it 1; Eusebius quoting the Apology from a Greek translation, "well versed in the laws of the Romans" (NPNF2-1 10272, 10304), What came of it 6; Jerome naming the four together (NPNF2-6 16477-16480, 16704-16721), What came of it 2, and his style verdicts, "rugged and uncouth", "a flow of eloquence worthy of Tully", "lengthy and unequal" (NPNF2-6 14107-14116), What came of it 3; the list under Gelasius's name setting the four authors' works among the apocrypha (Mansi 8 17220, 17222, 17233, 17301), What came of it 5. Told without quotation marks; "Cicero" for Tully, the same man.
- **uncertain** (fourteen items; what the outline, review and fresh read send to the card):
  1. Minucius's date (Outline, Do not say; sheet §6: ANF7 4470-4472, NPNF2-3 40491, 40644).
  2. Arnobius's date, Lives against Chronicle (Fresh_Trust 21, Fresh_Trust_Second 21; NPNF2-3 41022-41025, JerChron 45066), with his "almost three hundred years" (Leave out: card; ANF6 39891).
  3. The conversion story rests on Jerome alone (Who tells it; JerChron 45066-45076).
  4. The pupil link rests on Jerome alone (NPNF2-3 41033-41035; NPNF2-6 16713-16716).
  5. The charges in full, Fronto, and Tacitus for the ass's head (Cut first 6 and 13; Leave out: card; ANF4 17582-17690, 18998-19004; ANF3 10078-10082).
  6. Caecilius's own words of yielding (Cut first 16; ANF4 19492-19508).
  7. Whom the monthly gift kept (Cut first 4 and 10; ANF3 3895-3907).
  8. Justin and Marcion (Cut first 1, 2 and 9; ANF3 43160-43163, 22609-22612).
  9. Arnobius on the world gone to ruin, and his question on burned writings and broken-up meetings (Cut first 3, 11 and 17; ANF6 39480-39515, 48676-48690). Kept apart from Nicomedia, with no cause named.
  10. Lactantius on Scripture's plain speech and fit heralds (Cut first 5 and 18, Ending 2; ANF7 4456).
  11. Lactantius's few pupils at Nicomedia (Cut first 12; NPNF2-3 41035-41038).
  12. Commodian (Leave out: card; NPNF2-3 42424-42432).
  13. Augustine on three persons, naming no writer (What came of it 4; NPNF1-3 8211-8227).
  14. The list's attribution, Gelasius or Hormisdas, disputed (What came of it 5; Source_Sheet Library sweep).
- **quotationOriginals** (three; one per quoted span in the brief; each six words or more, so no `secondReading`):
  1. Q1: `printed` MinLat 826-827, "latebrosa et lucifuga natio, in publicum muta, in angulis garrula"; `englishPrinted` ANF4 17588-17589; `uncertain` names Halm's note at MinLat 862-863 (manuscript "lucifugax"). Clean print.
  2. Q2: the original is in two scanned prints. `printed` Monc3 21713-21718, as the scan reads ("ah", "religionein"); `uncertain` names those slips and Fotheringham's print, JerChron 45070-45076 ("ncque", "ptetatts"), which confirms the words. Confirmed by a second held print, so the Latin is printed. No `englishPrinted`: the only English, ANF6 39073-39077, is partial and says "visions", which the outline bars.
  3. Q3: `printed` ArnLat 1132-1135; `englishPrinted` ANF6 40667-40670. Clean print.
  Each rendering was checked clause by clause against its Latin: nothing added but Q2's joining "So".
- **sources**: `ownWords` MinLat, ANF4, ANF3, ArnLat, ANF6, LactLat, ANF7; `about` NPNF2-3, NPNF2-6, JerChron, Monc3, NPNF2-1, NPNF1-3, Mansi 8. Every file a quotation cites is listed.
- **briefReferences**: thirteen lines, one per run of the brief, each with the lines the outline cites for it.

## Entry fields

| Field | Old | New | Evidence |
|---|---|---|---|
| why | A Carthaginian convert named Tertullian had to invent Latin words for the Trinity and the sacraments just to defend his faith, coining terms like trinitas, persona, and substantia. The argument he opened ran a further century, through Minucius Felix's dialogue giving pagan objections their fullest voice, to Lactantius, who wrote his own defense in the middle of persecution and later tutored the emperor's son. | A Carthaginian convert named Tertullian defended his faith in Latin, answering the charges against Christians in his Apology to the governors who judged them. Others made the same case: Minucius Felix, in a dialogue in which a pagan friend states the case against them, and, a century after Tertullian, Lactantius, who wrote his own defense in the middle of persecution. | Coining: modern (Do not say). "The argument he opened ... through Minucius": puts the Octavius after Tertullian (Do not say; Lactantius names Minucius first, ANF7 4470-4472) and makes Tertullian the founder (NPNF2-3 40494-40495). "Fullest voice" and the tutoring: claims the brief no longer makes (Kit Part 1); the imperial-church link is Inferential-Thin (slate). Convert: ANF3 2710-2712 ("Once these things were with us, too, the theme of ridicule"). Apology to the governors: ANF3 1448-1453. A century: Severus and Caracalla to Diocletian (NPNF2-3 40498-40499, 41033-41035). |
| teaser | A Carthaginian lawyer invented the Latin words for the Trinity while defending Christians against Roman slander - and the argument he opened ran a further century, through Rome, Numidia, and the emperor's own new capitals. | A Carthaginian convert defended Christians against Roman slander in Latin, and others made the same case at Rome, at Sicca, and at Nicomedia, within sight of the emperor's palace. | "Lawyer": Do not say. Invented words, "opened": as above. "Numidia": Jerome says "Sicca in Africa" (NPNF2-3 41022-41023). "Capitals": the plural brings in Trier, which no held line names (Jerome: "in Gaul", NPNF2-3 41052-41054) and the brief does not tell. The palace: ANF7 10161. |
| relationsSummary | It includes Tertullian, whose Latin apologetic writing opened the tradition and gave it its vocabulary before the other authors continued it. Its clearest link to the later imperial church runs through Lactantius, who wrote his own defense during persecution and then tutored the son of the emperor who ended it. | It includes Tertullian, whose defense of the Christians, the Apology, Lactantius later said had pleaded their cause in full. | As above for "opened" and vocabulary; the imperial-church link is Inferential-Thin and stays out (slate; Outline, Links). ANF7 4569: "Tertullian fully pleaded the same cause in that treatise which is entitled the Apology". The first sentence is unchanged. |
| dates | c. 197-320 | c. 200-320 | 197: an editor's date (Do not say); "around 200" (Outline, Setting; NPNF2-3 40498-40499). |
| start | 197 | 200 | As above. |
| end | 320 | not changed | No held source gives an end year; the outline says the record gives no end. Flagged for Mark, as for Montanism. |
| region | Carthage; Rome and Ostia; Sicca in Numidia; Nicomedia and Trier | Carthage; Rome and Ostia; Sicca in Africa; Nicomedia | Outline, Setting (NPNF2-3 41022-41023, 41037-41038). Trier: no held line; the brief does not tell it. |
| longDescription | the approved brief | `latin-apologists.brief.txt`, final newline removed | The finished brief. |
| modernWorks (new) | none | Halm 1867, Reifferscheid 1875, Brandt and Laubmann 1890, Fotheringham 1923, Monceaux 1905, each with a note on what it covers | Outline, Who tells it ("modern editions; clarify the texts"; Monceaux "finds the text"); Source_Sheet, Modern works. Title, publisher and year from each file's header. All public domain by date (`CORPUS-USE.md`). Bryce and Campbell and Harnack are left out: the sheet marks them "not used". |
| documentedStories[0].modernWorks (new) | none | `{"title": "Constantine and Eusebius", "author": "T. D. Barnes", "year": "1981", "publisher": "Harvard", "note": "Chronology of the edicts."}` | Moved from `documentedStories[0].sources`, where it read `{"work": "T. D. Barnes, Constantine and Eusebius (Harvard, 1981)", "type": "reference", "note": "Chronology of the edicts."}`; note word for word. A citation only. |

## Not found (left in place)

- sourcing: the word counts; "thirty-two works"; "Three of the five are barely datable" (only two are then named).
- relationsSummary: "a generation later and never as coherent a body".
- voices[0] "trained rhetorician"; voices[3] "acrostic verse that does not scan" and "scholars have placed anywhere between the third century and the fifth" (the NPNF note to Gennadius, NPNF2-3 42424-42426, gives 250 to about 350); voices[4] "the fullest of the Latin defenses" and "the emperor who ended it". Its tutoring is held (NPNF2-3 41052-41054), so it stays, though the outline keeps it out of the story.
- legacy: "lines that entered common Christian speech"; "the Renaissance called him the Christian Cicero and printed him before it printed most of the Fathers". The 1465 printing is found: Brandt, CSEL 27 (`lactantius_de-opificio-de-ira-carmina-lat_brandt-csel27-1.txt` 1795-1802), the Subiaco edition of 1465, "the first book in Italy" made by Gutenberg's art to bear its year.
- documentedStories[0].text: ‘not merely tortured but roasted’ (ANF7 10174 reads "not only tortured, but burnt alive"; the Latin is not held); "their books surrendered, their assemblies forbidden"; "Lactantius lost his post"; "in old age". The `when` is found: the Terminalia (ANF7 10152) in the eighth consulship of Diocletian (ANF7 10161).
- people: `year` 205 (Minucius) and 250 (Commodian): no held source gives them, and the outline gives the Octavius no year. 295 (Arnobius) is the NPNF editor's note (NPNF2-3 41021). Display years, flagged with `end`.

## For the checker or Mark

- legacy keeps "most famously that the blood of Christians is seed". It is not a quotation, but the slate bars that line as a quote in this batch (tertullian-s-voice). Left as it stands; flagged.
