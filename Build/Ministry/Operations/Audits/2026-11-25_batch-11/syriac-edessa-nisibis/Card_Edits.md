# Card edits: Syriac Christianity (`syriac-edessa-nisibis`, tradition)

Card: `syriac-edessa-nisibis.card.json`. A tradition has no `card` field, so the card file holds the census entry's card fields, as `Card.existing.json` does, in the same order. `why` and `relationsSummary` are left word for word in the card file; their changes are listed under **Entry fields** for release. The entry has no `teaser`. Every other field not listed here is word for word from `Card.existing.json`. Three new keys follow at the end: `uncertain`, `briefReferences`, `quotationOriginals`.

**Format note.** `tools/validate-census.mjs` sets key lists only for a person's `card` and a council, and checks a tradition's quotations nowhere. So `sources` keeps the census's tradition form (`work`, `type`, `note`, `url`), with `file` added where the card cites one. `quotationOriginals` uses the person-card keys. Checked: a scratch census copy outside the repository, with these fields at the top of the entry, the brief as `longDescription`, and the Entry-field changes below, gives 0 errors and the same 4 warnings as the live census (`node tools/validate-census.mjs <copy>`). I re-read each `printed` at its lines with the validator's fold rule, and every quoted span in the card's prose against the files the card cites. All pass.

## Clearly wrong (card fields)

1. `voices[2]` (Tatian).
   - Old: "and these Syriac communities read his harmony as their standard Gospel text for two centuries afterward."
   - New: "and Edessa's later founding story pictures its people hearing his harmony read."
   - Evidence: the brief, "Edessa's later founding story pictures its people hearing the Diatessaron read". Outline Do not say (line 145): not "across the span"; beat 1: "No old line places it at Nisibis or across the span" (Addai 65 is the only old witness; `Review.md` B2).
2. `voices[4]` (Jacob).
   - Old: "one chronicle places it in 338, the year of the first siege, another has him still at his post in 350."
   - New: "the Chronicle of Edessa places it in 337 or 338, while Theodoret's history has him still at his post through a siege."
   - Evidence: Chronicle 17, `chronicle-of-edessa_cowper.txt` 77 ("In the year 649, died Mar Jacob"; 649 = 337/338, Source Sheet E4). Theodoret II.26, `npnf203` 11124-11177, has him alive and praying, with no year. The 350 is Gwynn's (`npnf213` 11229-11231), and outline Do not say bars it. No held line makes 338 "the first siege": Ephrem gives only "our third peril" (13839-13840).
3. `voices[5]` (daughters of the covenant).
   - Old: "The daughters of the covenant sang this tradition's hymns in every church that had them. Not one line composed by one of them survives; everything known of their voices—their vows, their singing, their service—was written by men."
   - New: "The daughters of the covenant were women vowed to God for life. Not one line composed by one of them survives; everything known of them, even the words Aphrahat gives one of them to say, was written by men."
   - Evidence: outline Do not say, "Women of the covenant sang Ephrem's hymns in his own day → not held in an old source" (Sozomen's "choirs", 32088, sang Harmonius's verses); and "serving in the church" → leave out (`Review.md` B3). New words: the brief ("men and women vowed to God for life"; "Aphrahat gives her the words to answer"); Source Sheet E2 ("no word written by a daughter of the covenant survives ... every line about them is a man's").
4. `legacy`, paragraph 1.
   - Old: "All of them still sing Ephrem's hymns, and each counts this tradition as a root."
   - New: "All of them still sing Ephrem's hymns."
   - Evidence: batch header, the Syriac Orthodox line is Inferential-Thin and "stays off the story and the card"; outline Links. The sentence names that church among the three.
5. `legacy`, paragraph 2.
   - Old: "the Gospel harmony these communities had read for two centuries"
   - New: "the Gospel harmony Edessa's later founding story pictures these communities reading"
   - Evidence: as edit 1.
6. `sources`, Eusebius note.
   - Old: "(as a document Eusebius himself accepted, which this Christian tradition's own record does not)"
   - New: "(as a document Eusebius himself accepted)"
   - Evidence: this tradition's own Doctrine of Addai tells the Abgar story as its own (the card's Addai note; Source Sheet section 5; `addai_doctrine-of-addai.txt`).
7. `sources`, Chronicle of Edessa note.
   - Old: "its year-201 flood entry is the earliest hard evidence of a Christian community at Edessa."
   - New: "its year-201 flood entry is its first mention of a church in the city."
   - Evidence: `Review.md` B1 and outline Do not say ("the first sure sign of a church there" → leave out, a modern judgment). Source Sheet S1: entry 8 is the chronicle's first mention of a church in the city (entries 1-7, lines 39-51, name none).

## New (card fields)

8. `legacy`: a new last paragraph, from outline What came of it 3 and 4 ("Card").
   - "The name of the covenant lasted. The acts of the synod of 410 use it in the king's grant, and in the sixth century John of Ephesus still writes of women becoming "readers and daughters of the covenant." Edessa also kept the memory of Persia's martyrs: Sozomen says some sixteen thousand were known by name, with a multitude beyond counting, and that the people of Edessa took great care over their names."
   - Evidence: Chabot 16165-16166; John of Ephesus, `john-ephesus_lives-eastern-saints-po17_brooks1923.txt` 14152; Sozomen II.14, `npnf202` 29190-29196.
9. `sources`: `file` added to the eight old works the card cites (Aphrahat and the Nisibene Hymns, both `npnf213`; Eusebius `npnf201`; the Chronicle; Addai; Theodoret `npnf203`; Sozomen `npnf202`; Palladius). Nine old works added, each with its file: Ephrem's Prose Refutations (Mitchell); Ephrem's Nativity, Epiphany and Pearl hymns (`npnf213` 17505, 20028, 21773; outline Leave out: "card"); Parisot's Latin Aphrahat; Socrates III.22; Barhadbeshabba (Scher); the Persian martyr acts (Braun); the Synod of Isaac in Chabot; John of Ephesus (Brooks); Tatian's Address to the Greeks (Ryland, `anf02` 5513). Titles and translators are from the file headers. The three modern works move to `modernWorks` (edit 14).
10. `uncertain` (new), the items the outline and reviews send to the card:
    - a. Jacob at the siege: Cut first 1 and 9 (Theodoret 11124-11177: the dammed Mygdonius, the walls built up again, the prayer in the church, the tower and the gnats; Ephrem, Hymn XIII, 14774-14787; Chronicle 77).
    - b. The siege's year: Cut first 20 and Do not say (13839-13840).
    - c. The flood's year: `Trust_Second.md` S1 and `Review.md` MINOR (Chronicle 53; translator's notes, 368, "A.D. 202", and 272, "Dionysius places this flood in A.D. 216").
    - d. The king's reasons: Cut first 3 and 28 (Sozomen 28873-28877, 28889-28899; Braun 1571-1575).
    - e. The one-story Gospel's only witness: beat 1 and Do not say (Addai 65; Phillips's note 219).
    - f. The covenant in 410: beat 6 and Do not say (Chabot 16165-16166; note 16179-16180).
    - g. Ephrem's birthplace: Cut first 19 (Sozomen 32050-32051).
11. `briefReferences` (new): nine lines, one for each run of the brief, with the lines it draws on. The cut details the outline sends to the card are carried in them at their lines: the tower, the torches, the palace and the sleepers (Cut first 24, 25, 29; Chronicle 53); Tatian born in Assyria and a hearer of Justin (21; `anf02` 7460, `npnf201` 26368); Eusebius's "still in the hands of some" (7; 26479); one letter for each letter of the alphabet, and the years 648 and 655 (4, 8; 28554-28561); "mounds and weapons and waves" and the third peril (27, 20; 13746-13751, 13839-13840); Aphrahat's taunt (10; 27416-27419); Bardaisan's Entities in empty Space (23; 606-608); deacon of Edessa and June (22; Palladius 471, Chronicle 103); the eleventh year, the prisoners, Marutha the go-between, the capital (16, 18, 15, 17; Chabot 16155, 16159-16166, 16226-16229, 16410-16416); one bishop to a city and the shared feasts (30, What came of it 2; 16519-16534, 17741-17742); Nisibis's rank and Hosea, third to sign (6; 17714-17746, 17856-17861). Each was re-read at its lines.
12. `quotationOriginals` (new): one entry for each of the brief's five quoted spans, each `modern` copied exactly from the brief.
    - Q2, the daughter's answer: `printed` Johnston, `npnf213` 25950-25953. The outline renders from the English, with "my bridegroom" after Parisot's *Sponsus meus* (Latin, 18130-18134, checked by the fold rule; it is a translation, not the original, so it is named in `uncertain`, not as `original`).
    - Q1, the refrain: `printed` Stopford, `npnf213` 13733-13734.
    - Q3, their fast and their faith: `printed` Mitchell, 1205.
    - "prays with Satan.": `printed` 1205, "he who prays with the Manichaeans prays with Satan". Three words, so `secondReading` "checked at card".
    - The king's grant, "the priests, the leaders and all the holy covenant": `printed` Chabot's French, 16165-16166. Rendered from the French ("les prêtres, les chefs et toute la sainte alliance"); I checked it clause by clause and it matches. The Syriac is misread scan text, so no `original` is given.
    - No `secondReading` is set for the four spans of six words or more.

## Entry fields (for release)

13. `why`.
    - Old: "This is the church that sang its teaching rather than argued it in treatises - Ephrem's hymns carried its doctrine, and men and women bound themselves to a covenant of celibacy and service inside the ordinary congregation, not apart from it."
    - New: "This is the church that sang its teaching in hymns - Ephrem's hymns carried its doctrine, and men and women bound themselves to a covenant to live unmarried and holy for God."
    - Evidence: the brief says "In his prose writings Ephrem answered three rival teachers by name", and its Aphrahat writes letters, so "rather than argued it in treatises" contradicts it. "Service" and "inside the ordinary congregation, not apart from it" are barred by Do not say ("serving in the church"; "They lived at home with their families": not held). New words from the brief ("to live unmarried and holy for God").
14. `modernWorks` (new on the entry). The three modern works in the card's `sources` move here and are removed from `sources`:
    - `{"title": "Bardesanes and Bardesanites", "author": "John Arendzen", "year": "1907", "publisher": "Robert Appleton Company (The Catholic Encyclopedia, vol. 2)", "url": "https://www.newadvent.org/cathen/02293a.htm", "note": "Background on the Edessan philosopher-poet whose cosmology Ephrem's own hymns were written to refute."}`. Note and URL word for word; the author and year are from the article's own citation at that URL.
    - `{"title": "Bardaisan of Edessa: Philosopher or Theologian?", "author": "Ute Possekel", "year": "2006", "publisher": "Zeitschrift für Antikes Christentum 10.3", "note": "Bardaisan's teaching, and whether to read him as a philosopher or a theologian."}`. The old note said what the article argues ("The strongest non-hostile modern reconstruction; ... likely diverges from bodily resurrection"), which Part 1 bars, so the new note says what it covers.
    - `{"title": "The Luminous Eye: The Spiritual World Vision of Saint Ephrem the Syrian", "author": "Sebastian Brock", "year": "1992", "publisher": "Cistercian Studies 124", "note": "Ephrem's way of reading Scripture and nature through symbols."}`. The old note praised the author; the new note is the source sheet's line on what it covers.
    - The outline's modern tools (Who tells it, Modern): `{"title": "Introductory Dissertation: Ephraim the Syrian and Aphrahat the Persian Sage (Nicene and Post-Nicene Fathers, second series, 13)", "author": "J. Gwynn", "year": "1898", "note": "The lives and works of Ephrem and Aphrahat, and the notes that date Aphrahat's letters."}`; `{"title": "Introduction to Aphraatis Sapientis Persae Demonstrationes", "author": "I. Parisot", "year": "1894", "note": "Aphrahat's names for the men and women vowed to God, among them sons of the covenant."}`; `{"title": "Notes to Synodicon orientale ou Recueil de synodes nestoriens", "author": "J.-B. Chabot", "year": "1902", "note": "The meaning of son and daughter of the covenant in the acts of the Persian synods."}`; `{"title": "Notes to The Doctrine of Addai, the Apostle", "author": "George Phillips", "year": "1876", "note": "The manuscript reading Diatessaron in the founding story."}`.
    - Rights: the four tools are prints before 1931, held in `cic/texts/`. The three moved works are listed only as further reading, with nothing quoted.
15. `relationsSummary`.
    - Old: "Its see of Nisibis passed into the Church of the East. The Syriac Orthodox Church also counts it as a root. Syriac translators ..."
    - New: "Its see of Nisibis passed into the Church of the East. Syriac translators ..."
    - Evidence: as edit 4.

## Flagged, not changed

- **Entry texts (Open-Gaps 416, rebuilt in this batch):** `entry.summary` has "They lived in town with their families" (Do not say: not held). `entry.tile` has "Preachers used it for as long as this Christian tradition lasted" (Do not say: across the span), "serving their own congregation instead of leaving for the desert" (Do not say), and Simeon and the twenty-year vacancy (the continued-as story's own). Topic and alias notes repeat "inside the ordinary congregation". These are for the entry-text rebuild, not this card.
- **Modern opinion stated as content (Part 1):** `legacy` paragraph 2, "historians dispute whether he caused it or only presided over a shift already under way"; `voices[6]`, "341 by the traditional count, with some historians arguing for 344 instead". Both removed after the check (edits 16 and 17). Rabbula's years "(411–435)" are held (Chronicle 145, 161) and stay.
- `sources`, the Bardaisan note and the Arendzen note say Ephrem's hymns were written to answer Bardaisan. The brief has his prose answer all three, and Sozomen has his hymns answer the songs of Bardaisan's son (32085-32103). This is not clearly contradicted, so it is left.
- Not carried: Ephrem as a "single one" sharing Christ's title (outline Leave out). It rests on Syriac the Library does not hold readably and on modern works, and Part 1 keeps a claim resting only on modern work off the card.

## Not found (left in place)

- `voices[0]`: deacon "first at Nisibis" (the title is held only for Edessa, Palladius 471); "hundreds of hymns".
- `voices[1]`: "between 336 and 345" and the twenty-third letter's date (the NPNF selection holds XXII.25 only).
- `voices[3]`: "at the court of King Abgar the Great"; his later tradition rejecting him over the resurrection of the body.
- `voices[4]`: "from about 309"; "a signatory at the Council of Nicaea in 325".
- `voices[6]`: Simeon's trial, the gifts, the sun, the twenty-year vacancy (the continued-as story's sources).
- `floorNote`: "his own later tradition repudiated".
- `legacy`: the three churches worshiping in Syriac today; the Peshitta (the only held mention, `anf09` 1914-1920, is a modern introduction); Rabbula's part in the change; the missions to India and Tang China; the Arabic translators; the school of Nisibis "around 490".
- `relationsSummary`: the translators' line.

## Changes after the grade fixes

The brief changed after the card was written (`Grade2_Fixes_Applied.md`, `Grade3_Fixes_Applied.md`). Its five quoted spans are unchanged: each `quotationOriginals` entry matches its span in the final brief, and each `printed` was re-read at its file and lines (`npnf213` 25950-25953 and 13733-13734; Mitchell 1205, twice; Chabot 16165-16166). The cuts in `Fixes_Grade2.md` and `Fixes_Grade3.md` all go to Leave out; none goes to the card.

From `Card_Check.md` (FIX):

16. `voices[6]`: " The year itself is disputed: 341 by the traditional count, with some historians arguing for 344 instead." removed (check fix 1; Braun 1302-1305 give no year of death).
17. `legacy` paragraph 2: "; historians dispute whether he caused it or only presided over a shift already under way" removed, ending the sentence at "with the change." (check fix 2).
18. `sources`, Tatian, The Diatessaron, `note`: "used as the standard gospel text in Syriac churches for centuries." becomes "which Edessa's later founding story pictures its people hearing read." (check fix 3; as edits 1 and 5).
19. `sources`, Nativity, Epiphany and Pearl hymns, `note`: "not drawn on by the story." becomes "in The Pearl he sees in a pearl 'mysteries pertaining to the Kingdom.'" (the card's JSON carries the inner marks as double quotes) (check fix 4; `npnf213` 21795, re-read).
20. Entry field `modernWorks`, Brock: `"year": "1985"` becomes `"year": "1992"` in edit 14 (check fix 5). Rabbula's years come off Not found (held, Chronicle 145, 161).

From the final brief (paragraph 9, "A Roman envoy, a bishop who made peace between East and West, came to a later Persian king. Through his work, the king ordered ..."):

21. `sources`, Socrates: `work` "Socrates, Ecclesiastical History III.22" becomes "Socrates, Ecclesiastical History III.22, VII.8"; `note` adds "; and the bishop Maruthas, sent by the Roman emperor on a mission to the king of the Persians." Evidence: `npnf202` 19135-19141 (re-read); Source_Sheet line 131; outline beat 6.
22. `briefReferences`, the synod line: "Marutha the go-between of peace between East and West (lines 16226-16229)" becomes "the grant coming about in the time of Mar Isaac (lines 16168-16169), through the work of the bishop Marutha, the go-between of peace and concord between East and West (lines 16227-16230), and of the bishops of the Romans (lines 16236-16237)". Line 16226 is blank, and "l'Orient et l'Occident" stands at 16230. A new last sentence: "Socrates, Church History VII.8 (lines 19135-19141, 19174-19176): the Roman emperor sends Maruthas, bishop of Mesopotamia, on a mission to the king of the Persians, who then lets him build churches wherever he wishes." Each re-read at its lines; Source_Sheet lines 130-131.
23. `uncertain`, new last item: why the later king changed course. The acts credit Isaac's time, Marutha's work and the Roman bishops (16168-16169, 16227-16230, 16236-16237); Socrates has the emperor send him (19135-19141); no old line gives the king's own reason, and the acts leave open whether East and West mean the empires or the churches (Source_Sheet line 130; `Fixes_Grade3.md`; outline beat 6, "never the two empires"). Socrates's wonders stay off (Contested, Leave out).

Nothing the final brief dropped was on the card: "the three of them" and the one-bishop clause left the brief before the card was written, and the one-bishop rule stays as a card item (Cut first 30). Checked again: a scratch census copy outside the repository with these fields and the final brief gives 0 errors and the same 4 warnings. The entry texts are in `Entry_Texts.md`.
