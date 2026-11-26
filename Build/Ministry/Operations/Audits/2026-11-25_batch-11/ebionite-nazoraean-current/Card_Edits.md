# Card edits: The Ebionites and Nazoraeans (`ebionite-nazoraean-current`, tradition)

Card: `ebionite-nazoraean-current.card.json`. A tradition has no `card` key, so the card file holds the census entry's card fields, in the order of `Card.existing.json`. `why`, `relationsSummary` and `teaser` are left word for word in the card file; their changes are listed under **Entry fields** for release. Every other field not listed here is word for word. Four new keys follow at the end: `uncertain`, `sources`, `briefReferences`, `quotationOriginals`. The existing card has no `sources` and the entry has no `modernWorks`, so both are new. File keys are those of `Source_Sheet.md` (ANF1, JusG, ANF3, ANF4, ANF5, ANF9, HE, HEg, Pan, VI, PL23, JP, AugE, CSEL34, AugF, PL42), with `npnf209` for Hilary.

**Format and validator.** `sources` uses the `cyril-and-methodius` form (`about` only: nothing these communities wrote survives whole, and the gospel they used is held only in Jerome's quotations, which the outline's Do not say bars calling their own book). `tools/validate-census.mjs` checks a tradition's quotations nowhere, so two scratch copies of the census were run, both outside the repository:
- The card fields on the entry, with the brief as `longDescription`: `node tools/validate-census.mjs <copy> --skip-quotes`, 0 errors, the same 4 warnings as the live census.
- The new fields as a person card on a test entry, so `checkQuotationOriginals` and the quote check run: every `printed`, `englishPrinted` and `original` stands at its lines, every quoted span in the card's prose stands in a cited file, and all six brief spans are covered. The errors left are the ones release clears: `secondReading` not yet set on the four spans of six words or more, the brief's three renderings (Q1, Q2, Q3) not yet listed in `tools/quote_renderings.json`, and the test entry's own meta counts.
The two quoted spans in `legacy` were checked the same way by hand (VI 16163, npnf209 16941).

## Clearly wrong (card fields)

1. `floorNote`.
   - Old: "Because nothing survives from these communities themselves,"
   - New: "Because nothing written by these communities survives whole,"
   - Evidence: `Source_Sheet.md` head note (line 29): "Nothing written by these communities survives whole ... Their own words reach us only as quotations made by opponents: their gospel (F), and the charges they made (B5)". Symmachus's renderings survive in Jerome (JP 7541, 7553); the gospel they used survives in Jerome's quotations (PL23 48133-48136). The brief: "Their own books are lost".
2. `voices[0]` (modern view stated as content; Outline Do not say, "'Ebion, their founder' / 'Ebion never existed' → Neither ... the second is modern"; Source Sheet C5).
   - Old: "a supposed founder most scholars now think never existed — invented to explain a group name that in fact meant simply 'the poor'."
   - New: "a founder Tertullian, Hippolytus and Epiphanius name, while Origen says the group's name meant 'poor' in Hebrew."
   - Evidence: ANF3 21552-21554 ("the other, Hebion"); ANF5 12273-12274 ("Cerinthus and Ebion"); Pan 25230 ("Ἐβίων, ἀφ᾽ οὗπερ Ἐβιωναῖοι"); Origen, ANF4 34025-34026 ("“Ebion” signifying “poor” in Hebrew"), 39118-39119. The old "in fact meant simply" told Origen's reading as fact; the new words credit it.
3. `legacy`, sentence 2 (Outline Do not say: "They died out" / "were absorbed into the church or Judaism" → Augustine, "very small", "still continues").
   - Old: "They disappear from the record by roughly the fifth century, absorbed into the wider church or back into Judaism or simply gone, and the gospel material"
   - New: "Jerome wrote in 404 that the Nazoraeans were still a sect among the Jews in all the synagogues of the East, and Augustine, about 400, that their number was very small but the sect still continued; the gospel material"
   - Evidence: CSEL34 23235-23237 and AugE 33602-33605 (the brief's last paragraph); AugF 6787 ("Their number is now very small, but the sect still continues"), PL42 27450-27456. Augustine is Outline Ending 1, sent to the card by Cut first 7 (the length ruling). "About 400" is the outline's (Ending 1).
4. `legacy`, sentence 4 removed (modern judgment stated as content, Kit Part 1, Rigor; a claim the brief no longer makes: the approved text's "The first Christians were Jews").
   - Old: " They are the standing reminder that Christianity began inside Judaism, and that the separation of the two was slower, later and far more contested than a tidy account allows."
   - New: "" (removed)
   - Evidence: no held source makes the judgment; the brief tells none of it.

## New (card fields)

5. `legacy`: a new last paragraph, from Outline What came of it 1 and 3 and Words to explain ("Origen's columns": card).
   - "Their books passed through the hands of the writers who opposed them. Origen set Symmachus's Greek version beside the other Greek versions of the Hebrew Scriptures in his book of columns, and Jerome used his renderings. Jerome copied the gospel the Nazoraeans used, and says he put it into Greek and Latin. Later writers made Ebion a byword for those who held Christ only a man: Damasus's creed condemns Photinus "renewing the heresy of Ebion", and Hilary calls Photinus "the Ebion of our day.""
   - Evidence: HE 34446-34464, HEg 3215-3218 (G1); JP 7541, 7553 (G4); PL23 48161-48162, 48081-48083 (F5, F7); VI 16163-16164; npnf209 16941 (I3). The columns clause is the one `Fresh_Read.md` cut from the brief because no held line says why; the card says only what was done. The first sentence is the outline's Connection ("the writers who called them heretics were also the ones who kept and used their books").
6. `uncertain` (new), sixteen items, each the item the outline, review or a read sends to the card:
   - a. What they believed about Jesus: Outline The heart ("Contested on Christ"), Cut first 6 (E6), Leave out (E5, E9, E12); Source Sheet E2-E12 (ANF1 43299-43300, 50651-50654; ANF4 53648-53653; HE 18561-18564, 18586-18599; ANF5 12247-12256; Pan 26607, 25023-25026; CSEL34 23272-23275; PL42 1337-1347).
   - b. One people or two: Outline Do not say (J); Pan 12578; HE 18581-18582; CSEL34 23229-23237; AugF 6787.
   - c. Their names: Source Sheet J ("The name"); Words to explain ("the poverty of their Law", cut from the brief by `Craft_Pass_Shape.md`, given here in Origen's own words); ANF4 39116-39121, 34023-34025; HE 18514-18516; C5 as edit 2; Pan 24952-24955.
   - d. Their gospel: Cut first 4c (B3, ANF1 33537), Cut first 5 (Jerome's "as most maintain", JP 45240-45242), What came of it 2 (Eusebius, HE 18159-18160, 18230-18232, 18627), Leave out (F3, F4: Pan 26376-26378, 26666-26668); F2 (Pan 25170-25173); F7 (PL23 48155-48163). The Ebionites' gospel quotations are given in the narrator's words, since the Greek is a damaged print with no English held.
   - e. The baptism scene: Leave out ("card"), What came of it 2; JP 45243-45247.
   - f. Justin's terms: Cut first 13 (B1c, B1d; ANF1 19915-19930; JusG 2167-2179); "through weak-mindedness" (ANF1 19916; JusG 2167), from `Trust_Shape_Second.md` ("The condescension could go on the card"), so the welcome keeps its force.
   - g. Their charge against Paul: Cut first 15 and Leave out ("card, in full"); Pan 26737-26745; HE 18606-18608; ANF4 53781-53783.
   - h. Neither side: Cut first 16 (B12); Pan 24968-24971.
   - i. The Sabbath and the Lord's day: Cut first 1 (B10); HE 18726-18729. The editor's note that it may mean one kind only (HE 18729-18752) is modern and is not carried.
   - j. Food: Cut first 2 (B9); ANF9 31918-31922.
   - k. The prophets: Source Sheet J ("Prophets": card); ANF1 33538-33540; Pan 24955-24968, 26886-26890.
   - l. Where they lived: Cut first 3 and 4b; A9, A10, A11, A13 (Pan 25026-25029, 26876-26879; PL23 48161-48162).
   - m. A beginning at Pella: Cut first 8 (H2, "Card"); H1, H3; HE 15291-15294; Pan 25029-25034, 25335-25345. "Beyond the Jordan" glosses Peraea (A14, Widely Accepted). "The only witness" is the slate's and the sheet's ("single witness", H2).
   - n. Symmachus and Juliana: Cut first 4 and 4d; G1-G3 (HE 34446-34464, 34736-34771; HEg 3215-3218, 3305-3314; VI 40559-40561). Who Juliana was beyond this (G5, Palladius via a modern note) is not carried.
   - o. Epiphanius on the Ebionites' life: Leave out ("card"; B13-B16, E9 and the Circuits of Peter); Pan 26879-26882, 26596-26603, 25331-25332, 26527-26533, 26673, 26732-26734.
   - p. Jerome on John's Gospel: What came of it 5 and Leave out ("card; late"); VI 39566-39572.
   - Not carried: Justin's chapter 48, the tale of Count Joseph, the Clementine romances, Aristo and the Testaments (Leave out, not card); "morning, noon and evening" and Cut first 4e, 11, 12, 14 (Leave out).
7. `sources` (new): eighteen old works in `about`, each with its file, title and print from the file headers and `Source_Sheet.md`'s key table: Justin (JusG; ANF1), Irenaeus (ANF1), Tertullian (ANF3), Origen (ANF4; ANF9), Hippolytus (ANF5), Eusebius (HE; HEg), Epiphanius (Pan), Jerome (VI; PL23; JP; CSEL34; AugE), Augustine (AugF; PL42), Hilary (npnf209). Every file a quotation cites is among them.
8. `briefReferences` (new): seven lines, one for each paragraph of the brief, with the lines each draws on. Each was re-read at its lines.
9. `quotationOriginals` (new): one entry for each of the brief's six quoted spans, each `modern` copied exactly from the brief.
   - Q1, Justin's answer: `printed` the Greek, JusG 2166-2167, as the outline renders it; `englishPrinted` ANF1 19913-19915. Greek checked by hand: Εἰσίν / there are some; ἀπεκρινάμην, ὦ Τρύφων / I answered, Trypho; μηδὲ κοινωνεῖν ὁμιλίας ἢ ἑστίας / not even to share company or a hearth; τοῖς τοιούτοις / with such people; τολμῶντες / who dare; οἷς ἐγὼ οὐ σύναινός εἰμι / I do not agree with them. Nothing added. `uncertain` carries the file's CC BY-SA 4.0 attribution and the two glosses the outline gives (Quote 1).
   - "as if it were the house of God": `printed` ANF1 33542-33543; `original` the Latin in Holl's notes, Pan 24980-24981 ("quasi sit domus dei"). Eight words, read blind, so no `secondReading`.
   - "an apostate from the Law": `printed` ANF1 33537-33538; `original` Pan 24117 ("apostatam eum legis"). Five words: `secondReading` "checked at card". Rendering, original and print agree ("him an apostate of the law"; "an apostate from the law").
   - "poor": `printed` ANF4 39118-39119 ("for Ebion signifies “poor” among the Jews"). One word: "checked at card". No Greek is held (Outline Words to explain).
   - Q3, the bread given to James: `printed` the Latin, PL23 48133-48136, verbatim with its scan fault (ἃ for a); `englishPrinted` VI 39337-39340. The Latin is a damaged scan; Richardson's English confirms the reading clause by clause (outline Quote 3), so the Latin is printed, with the fault and "brought" for tulit named in `uncertain`. Checked by hand: tulit panem et benedixit, ac fregit / took bread and blessed it and broke it; et dedit Jacobo Justo / gave it to James the Just; Frater mi, comede panem tuum / My brother, eat your bread; quia resurrexit Filius hominis a dormientibus / for the Son of Man has risen from among those who sleep.
   - Q2, Jerome's verdict: `printed` the Latin, CSEL34 23272-23275 (clean); `englishPrinted` AugE 33605-33609. Checked clause by clause: it matches; the subject is "Nazaraeos", 23237.
   - No `secondReading` is set for the four spans of six words or more.

## Entry fields (for release)

10. `why` (clearly wrong, as edit 1; and Justin and Jerome wrote of them in their own day, Source Sheet B1, A11-A12: "contemporary").
    - Old: "Not one word survives from these communities in their own voice - everything known of them comes through later writers who disagreed with each other"
    - New: "Nothing written by these communities survives whole - everything known of them comes through other writers who disagreed with each other"
    - Evidence: as edit 1; the brief, "we meet them only through other church writers".
11. `teaser` (contradicts the brief and Do not say: "lived in Palestine and Syria from Justin's day"; the census `dates` reach the first century only through Epiphanius's Pella beginning, Outline The heart).
    - Old: "Palestine and Syria, roughly the first through fourth centuries — Jewish followers of Jesus who never stopped keeping the Law, and whose own words have not survived"
    - New: "Known to church writers from the second century to about 400, and placed by the later ones in Syria and beyond the Jordan — Jewish followers of Jesus who never stopped keeping the Law, and whose own books have not survived"
    - Evidence: the brief, "Church writers wrote of them from Justin's day to about 400, and the later ones place them in Syria and beyond the Jordan"; "Their own books are lost".
12. `relationsSummary` (modern judgment stated as content, Kit Part 1; the brief no longer makes it).
    - Old: "These communities are the clearest evidence that Christianity began inside Judaism. Modern Messianic Jewish movements"
    - New: "Modern Messianic Jewish movements"
13. `peopleNote` (modern view stated as content; Outline Do not say, "Ebion never existed": modern).
    - Old: "Their founder, Ebion, is most likely a name later writers made up."
    - New: "Tertullian, Hippolytus and Epiphanius name a founder, Ebion."
    - Evidence: as edit 2.
14. `modernWorks` (new on the entry). None is listed in the card. The outline's tools (Who tells it, "Modern"; Source Sheet A3, A5, A14):
    - `{"title": "Epiphanius, Ancoratus und Panarion, volume 1: Ancoratus and Panarion haer. 1-33 (Die griechischen christlichen Schriftsteller 25)", "author": "Karl Holl (ed.)", "year": "1915", "publisher": "J. C. Hinrichs, Leipzig", "note": "The Greek text of Epiphanius's chapters on the Nazoraeans and the Ebionites, with the Latin of Irenaeus in its notes."}`
    - `{"title": "Eusebius Werke, volume 2, part 2: Die Kirchengeschichte, books VI-X, with Rufinus's Latin (Die griechischen christlichen Schriftsteller 9.2)", "author": "Eduard Schwartz and Theodor Mommsen (eds.)", "year": "1908", "publisher": "J. C. Hinrichs, Leipzig", "note": "The Greek of Eusebius on Symmachus, Juliana and Origen's columns."}`
    - `{"title": "Epistulae, letters 1-123 (Corpus scriptorum ecclesiasticorum latinorum 34)", "author": "Alois Goldbacher (ed.)", "year": "1895-1898", "publisher": "F. Tempsky, Prague and Vienna", "note": "The Latin of Jerome's letter of 404 to Augustine."}`
    - `{"title": "Patrologia Latina 23: Jerome, works, part 1", "author": "J.-P. Migne (ed.)", "year": "1883", "note": "The Latin of Jerome's Lives of Illustrious Men and Dialogue against the Pelagians."}`
    - `{"title": "Patrologia Latina 42: Augustine, works", "author": "J.-P. Migne (ed.)", "year": "1886", "note": "The Latin of Augustine's Against Faustus and On Heresies."}`
    - `{"title": "Justin, Dialogue avec Tryphon", "author": "Georges Archambault (ed.)", "year": "1909", "publisher": "Alphonse Picard, Paris", "url": "https://creativecommons.org/licenses/by-sa/4.0/", "note": "The Greek text of the Dialogue, held as the Perseus Project's digital edition under a Creative Commons Attribution-ShareAlike 4.0 license."}`
    - `{"title": "Notes to Eusebius, Church History (Nicene and Post-Nicene Fathers, second series, 1)", "author": "Arthur Cushman McGiffert", "year": "1890", "note": "The date of the History and the place of Pella beyond the Jordan."}`
    - `{"title": "Notes to Irenaeus, Against Heresies (Ante-Nicene Fathers 1)", "author": "Alexander Roberts and James Donaldson (eds.)", "year": "1885", "note": "The date of Irenaeus's work."}`
    - `{"title": "Notes to Jerome, Lives of Illustrious Men (Nicene and Post-Nicene Fathers, second series, 3)", "author": "Ernest Cushing Richardson", "year": "1892", "note": "The places and names in Jerome's chapters on James and Matthew."}`
    - Rights: all are prints before 1931, held in `cic/texts/`; the Archambault file's digital edition is CC BY-SA 4.0, and its attribution goes with Q1 (edit 9). The publisher and series lines come from the file names and headers; the Migne publisher is not in the file and is left out.

## Flagged, not changed

- **Timeline fields** (`dates` "1st-4th c.", `start` 70, `end` 400, `region` "Palestine, Syria", `placeLabel`, `placeQualifiers`): the outline says the first century rests only on Epiphanius's Pella beginning (one late hostile witness; slate: his voice only, no census change), no held witness says "Palestine" for them, and no witness gives an end (Jerome, 404, "usque hodie"; Augustine, "still continues"). Setting timeline years for a span the sources give this loosely is Mark's call (precedent: the Montanism card check, FIX 4).
- **Craft in short texts** (left, since no source contradicts them): `floorNote` ends on a dash and a "not X but Y" turn ("— an open question about the evidence, not a settled answer about their doctrine"); `legacy` "What they left behind is a question rather than an institution" is the same turn.
- **Modern events, no held source:** the Messianic Jewish comparison in `legacy` and `relationsSummary`. It claims no descent, which agrees with the census and the outline's Do not say.
- The census `longDescription` is replaced by the brief at release.

## Not found (left in place)

- `why`: "long after most of the church had moved on"; "honoring James, the brother of Jesus" (the nearest held lines are Epiphanius's report that the Ebionites once prized virginity for James's sake, Pan 25331-25332, and the James scene in the gospel Jerome quotes, F6; neither says they honored him).
- `legacy`: "No community descends from them" (the census `livingEvidence` only; the outline: no held source).
- `voices[0]`: "No leader of these communities is named in any source they produced themselves" (true as an absence, since no such source survives; not stated in a held line).
