# Card edits: Pontius the Deacon

Batch 12, 2026-11-27. A full new card, built under the card role's "A new card" and the batch header: every field sourced afresh from `Source_Sheet.md`, `Outline.md` at its cited lines, or the final `pontius-the-deacon.brief.txt`. `Card.existing.json` (the same as the census `card` today) is a pointer only; each field kept from it is listed below with its evidence. Short names (VE, VL, HAR, JE, JL, KNOPF, EP, BEDE, AASS, VSB) are the source sheet's; every cited line was re-read in its file for this card.

Checks run (outside the repository, in a scratch folder for this story): `tools/validate-census.mjs` on a census copy holding this card and the final brief, with a renderings copy listing the brief's new renderings and `secondReading` set to "same" in the copy only for the three long quotes: no error for `pontius-the-deacon`. `python -m engine.m1.profile_readability` on a plain file of the card's running text: 1964 words, grade 6.6 (names out 5.8), reading ease names out 79.5, 14.4 words a sentence, longest sentence 35 words, pass (grade under 8 noted).

## Card fields

### otherNames: kept

`["Pontius"]`. Evidence: JE 40833 ("Pontius, deacon of Cyprian"); JL 57618.

### knownFor: kept word for word

"Deacon of Cyprian of Carthage, who shared his exile and wrote the Life and Passion of Cyprian." Evidence: JE 40833–40835 (deacon, sharing his exile, left a volume on his life and death); brief, paragraph 2 ("After Cyprian's death, Pontius wrote The Life and Passion of Cyprian").

### shortDescription: new

"Pontius, a deacon of Cyprian of Carthage, went with his bishop into exile at Curubis in 257 and was with him on his last night in 258. After Cyprian's death he wrote The Life and Passion of Cyprian, so that later readers would have his example."
Evidence: outline essence (E2, E4, E6; JL 57618 for the office); KNOPF 4823–4836 (exile to Curubis, 257 from the consuls); VE 28181–28184 (the last night); brief, paragraph 2 ("so that later readers would have his example").

### datesNote: changed

Old: "Shared Cyprian's exile; Cyprian died in 258"
New: "Went into exile with Cyprian in 257, and was with him on the night before his death on 14 September 258. The court record of Cyprian's hearings gives the days, and the consuls it names give the years. Pontius wrote his book after the death. No old source gives the year of the book, or of his own birth or death."
Evidence: KNOPF 4823–4825 (30 August, consuls of 257), 4857 (Ides of September, consuls of 258), 4955–4956 (14 September); outline Setting (years from the consuls, Widely Accepted; "No year for the book: 259 is a scholars' reckoning"); VE 27692–27695 (written after the death); E12 (no source for his death). The date working is shown, per the header's "Dates from the sources' own clues".

### placeNote: changed

Old: "Carthage"
New: "Carthage, in Roman Africa, where Cyprian was bishop; Curubis, the town where they lived in exile"
Evidence: outline Setting, Place (S2; CEN); KNOPF 4825, 4835–4836; VL 41011–41012. "A small town on the coast", which the brief says, rests only on Benson (BEN 27288–27290, modern, clarifies the place), so the card's own text leaves it out and Benson goes to `modernWorks`.

### role: kept word for word

"Deacon and biographer". Evidence: JE 40833–40835.

### keyWorks: about changed

Old about: "Cyprian's conversion, his care in the plague, his exile and his death"
New about: "a short book, written after Cyprian's death for people who had heard him, so that later readers would have his example. It tells his life from the time his faith began, his care for everyone in a plague, his exile and his dream at Curubis, and his suffering and death as a martyr. It never gives its author's name"
Evidence: VE 27672–27677, 27692–27695 (short, for later readers, for his hearers); VE 27701–27708 ("from the beginning of his faith"; the brief's "where Cyprian's faith began", Review B3); VE 27991–27992 (good done to all); VE 28044–28089 (exile, dream); outline Words to explain, passion; E1 (no name). Title kept.

### legacy: rebuilt

Removed, old traces: "The Cheltenham list of 359 sets the Life at the end of Cyprian's works, and Harnack counts 23 manuscripts that hold it." The list's text is not held and its date is a modern reckoning (Review B4; outline Do not say, B4); the count is Harnack's (HAR 264). Both are claims the brief no longer makes; Harnack and von Soden go to `modernWorks`.
Removed, old remembered: "Adolf Harnack, in 1913, called it the oldest Christian biography that survives." A modern claim (outline Do not say; I6).
Removed, old remembered: "Jerome of Strido calls the Life "a notable volume."" Replaced by the fuller line below.

New traces:
- "The Life was copied with Cyprian's own writings." Brief, paragraph 8; outline What came 1 (I1; VSB 4159–4161; HAR 260–264; Widely Accepted).
- "Bede copied Jerome's sentence on Pontius and his book into his chronicle, and the Roman calendar of saints repeats its words." BEDE 23904–23909; AASS 196819–196822 (outline What came 3, card).

New remembered:
- "Jerome, in his catalog of Christian writers, names Pontius, Cyprian's deacon, as the author, and calls the Life "a notable volume"." JE 40833–40835; JL 57618–57622; brief, paragraphs 2 and 8. The quoted words stand at JE 40834.
- "Later calendars of saints keep Pontius's day at Carthage, on 8 March." AASS 196261–196266, 196815–196818 (I4; late legend, known through AASS).

### uncertain: rebuilt

Every old item is replaced. The old items that stated a modern opinion, date or identification as content are removed under the card checker's rule and the header's "Modern works on the cards"; the works that hold those views are listed in `modernWorks` by what they cover. Removed: Hartel's "commonly attributed" heading as a witness (item 1); Coxe's and Richardson's unsourced notes on his death, the second a year only a modern note gives (item 3); Ritschl's and Benson's views on the gardens, not in the source sheet (item 4); Harnack's view of Jerome's tradition, the 1922 handbook's report, and Dessau's identification with Corssen's answer, a contested identification held only as DEL and SHK report it (item 5); the debate over the kind of book, Harnack, Monceaux, Corssen, Reitzenstein, Delehaye (item 6); Reitzenstein's and Delehaye's views on the eyewitness (item 7); Harnack's judgment of the dream's reading (item 8); the reasons Delehaye, Harnack and Monceaux give for the silences (item 10); Harnack's inference that Pontius saw Cyprian's deeds but not from the start (item 11); Monceaux, Harnack, Delehaye and von Soden on whether Pontius knew the court record (item 12); Benson's and Delehaye's judgments of his style (item 13). Items 1, 9, 11, 12 and 14 survive in part, reworded below.

New items, each with its evidence:
1. "The witnesses. Almost all that is known of Pontius comes from his own book, which praises his bishop throughout. Jerome's one sentence adds his name and his office." Outline Who tells it; brief, paragraph 2; I2.
2. "The author's name. The Life never names its author or gives his office. Jerome is the one old witness that its author was Pontius, Cyprian's deacon. The heading By Pontius the Deacon, in the English translation, is its editors' title." E1 (the absence checkable in VE 27657–28303; JL 57618–57622); source sheet head on VE 27661. From old item 1 and old item 5's first two sentences.
3. "Jerome's date. Jerome's catalog runs to the fourteenth year of the emperor Theodosius. The English translation's note prints that year as 492. Another note in the same volume has Theodosius named emperor in January 379, so the year is about 392, some 130 years after Cyprian's death." JE 38785 (the text and its note "a.d. 492"); JE 15402–15403 ("On Jan. 19, 379 he nominated Theodosius Augustus"); E1. From old item 14, with the line in the volume now named.
4. "Where Pontius was. The Life puts him with Cyprian in exile at Curubis and on the night after his arrest. It does not say that he saw the execution." VE 28055–28059, 28181–28184; outline Do not say ("Pontius watched him die" → "the book puts him with Cyprian on the last night"). From old item 7's first sentence.
5. "The day of the dream. The first day at Curubis is the day Cyprian had the dream. The Life does not say when he told it." VL 41012–41016, 41082–41083; outline Do not say (B1); Review B1.
6. "A year to the day. ..." VE 28098–28102, 28112–28114; E5 Check ("the day Cyprian reached Curubis is given by no old source"); D4. From old item 8's first sentence.
7. "The delay. ..." VE 28074–28078 (to arrange his property); VE 28124–28129 (church business, the poor); KNOPF 4854–4857 (as had been shown to him; outline Quotes section, card in narration); D3. From old item 8's second sentence. Outline Cut first 20 and 26 send these here.
8. "The young man in the dream. Cyprian calls him a young man of more than human size. The Life does not call him an angel." VL 41016–41017 ("iuueuis ultra / modum hominis", that is *iuuenis*); E4; outline Do not say.
9. "The last withdrawal. ..." VE 28142–28149; EP 17370–17375, 17383–17385; D2. Old item 9 corrected: its "so that he would not be taken to Utica" and "a bishop should confess in his own city" become the letter's own order of events and reason, as Review B2 put them right in the brief.
10. "His sources. ..." VL 40333–40364; HAR 558–559; AASS 196801–196803; VE 27710–27712; D5. From old item 11, Harnack's inference removed.
11. "What the book leaves out. The Life says nothing of the councils of bishops Cyprian led, or of his quarrel with the bishop of Rome over whether a washing given outside the church counted as baptism. No old source says why." E10 (absence checkable in VE 27657–28303); the gloss of the quarrel from Cyprian's letters, EP 14138–14139 and 15430–15433, as the sibling outline gives it (`cyprian-of-carthage/Outline.md`, Words to explain and Beat 5). Outline Leave out sends it to the card. From old item 10, the modern reasons removed.
12. "The court record. ..." VE 28002–28004; KNOPF 4820–4958. From old item 12's first sentence.
13. "His own end. ..." E12; AASS 196815–196824 (outline What came 3, Leave out: "the calendars' crown ... card, marked late"). From old item 3, the unsourced modern notes removed.

### sources

Kept word for word: `ownWords` VE and VL; `about` Jerome, Lives of Illustrious Men, 68 (JE); Letters, 81 (EP); The Proconsular Acts of Cyprian (KNOPF).
Added to `ownWords`: "Vita Cypriani (Latin, in Adolf Harnack's print of Hartel's text, 1913)", HAR, Latin. It is the file of the original for the dream quote (HAR 1309–1313), and the second print that confirms VL at every quote (outline Quotes). The book's commentary goes to `modernWorks`.
Added to `about`: Jerome, De viris illustribus, 68, Latin (JL), the file of "egregium volumen"; Bede, Greater Chronicle (BEDE), for the legacy and timeline lines; Acta Sanctorum, March vol. 1, 8 March (AASS), for the calendars.
Moved out of `sources.about` to the entry's `modernWorks` (see Entry fields): Harnack (1913), Delehaye (1921), Monceaux (1902), Benson (1897), Schanz, Hosius and Krüger (1922).

### briefReferences: rebuilt

Removed, as naming what the brief no longer tells: the Harnack line (the Cheltenham list of 359, "the oldest Christian biography"); "he begins at Cyprian's baptism and passes over what came before it" (Review B3); the chapters 10 and 11 line (what he leaves out, the councils, the baptism quarrel, "his one marvel"); "Harnack finds this unconvincing"; "Monceaux and Delehaye on the kind of book"; "Jerome and the editors' notes ... no early source says how or when Pontius died"; "Benson: Curubis, a small coast town"; "World census, Latin Pastoral-Congregational Christianity: his tradition" (not an old source; the brief does not name the tradition).

New, each tied to the brief's sentences:
1. Acts in Knopf, the 257 hearing, the Roman rites, exile to Curubis: brief paragraph 1; KNOPF 4823–4836.
2. Life 12, the willing exile and the wish: brief paragraph 1; VE 28055–28059.
3. Jerome 68, the name and office; his catalog's end: brief paragraph 2; JE 40833–40835, 38785.
4. Life 12, the dream: brief paragraphs 3 and 4; VE 28055–28084.
5. Life 13, the day as a year, the very day of the year: brief paragraphs 4 and 5; VE 28098–28102, 28112–28114.
6. Acts, the gardens, the arrest, the sentence, the death: brief paragraph 5; KNOPF 4854–4857, 4901–4910, 4955–4956.
7. Life 14 and 15 with Letter 81: brief paragraph 5; VE 28142–28149, 28181–28184; EP 17370–17375.
8. Life 1, why he wrote: brief paragraph 6; VE 27672–27685.
9. Life 2 and 11, his choices and the court record: brief paragraph 7; VE 27701–27708, 28002–28004.
10. The manuscripts, as reported: brief paragraph 8; VSB 4159–4161; HAR 260–264.
11. Jerome 68, "a notable volume": brief paragraph 8; JE 40834.
12. Life 19, the last lines: brief paragraph 9; VE 28294–28303.

### quotationOriginals: rebuilt to the brief's six quoted spans

The brief's renderings changed since the old card (batch 7 wording), so each long entry carries the brief's new modern words and no `secondReading` (release sets it from the second readings). Each `printed` and `original` was re-read at its lines.

1. "a willing exile": kept from the old card (printed VE 28057 "a voluntary exile"; original VL 41015 "exulem uoluntarium"); `secondReading` changed from "same" to "checked at card" (three words).
2. The dream, "For he held his hand ... that was to come.": modern changed to the brief's. Old printed "with hand expanded ..." → new printed "For, with hand expanded and flattened like a blade, ... sentence of my passion." (VE 28071–28074; the brief's quote now opens on "For", *enim*). Original kept (HAR 1309–1313, with the listed scan reading at 1311; VL 41025–41029 reads the same, outline Quote 2). `uncertain` changed: old "Passion in the English translation means the martyr's suffering and death, so the modern wording says martyrdom, and spata is a sword, so the modern wording says sword blade." → new "Passion in the English translation means the martyr's suffering and death, so the modern wording says martyrdom. Spata is a sword, so the modern wording says sword blade, and the usual punishment is the sword stroke of execution. Hartel's Latin reads the same words." (outline Quote 2, "Stands behind it"; E4 Explain it).
3. Why he wrote, "I have decided to write down a few things, briefly. ...": modern changed to the brief's. Printed (VE 27673–27677), original (VL 40267–40270, with the listed scan reading at 40269) and `uncertain` kept word for word (outline Quote 1 holds each point).
4. "these things I pass over": new. Printed VE 27707, the same words; original VL 40331 "illa praetereo" (outline Quotes; E9). "checked at card" (five words).
5. "a notable volume": new. Printed JE 40834; original JL 57621–57622 "egre- / gium volumen" (I2). "checked at card" (three words).
6. The last lines, "Shall I grieve ... remained behind.": modern changed to the brief's. Printed (VE 28297–28303) and original (VL 41405–41410, with the listed scan reading at 41409) kept. `uncertain` changed: old "... Harnack's print sets a colon after sententia, where Hartel's Latin has a full stop, so that the words point forward to the joy and the grief, and the modern wording follows that. ..." → new "The Latin in hac me fuisse sententia means that I was of this mind. The English translation reads it as it was my intention to be his companion. Harnack's print sets a colon after sententia, where Hartel's Latin has a full stop, so that the words point forward to the joy and the grief. The modern wording, this was how I felt, holds both readings. The English translation has I must triumph in his victory, where the modern wording says his victory must be celebrated. Harnack's print and the Acta Sanctorum print read the same words." (outline Quote 3, "Stands behind it"; E11; HAR 1808–1813; AASS 196780–196790).

### briefSources: new

The old sources the brief draws on: VE (author Pontius the Deacon, as Jerome names him); VL; the Proconsular Acts (KNOPF); Cyprian, Letter 81 (EP); Jerome, Lives of Illustrious Men 68 (JE). Evidence: brief paragraphs 1–9; outline Who tells it.

### timeline: new

Seven periods, built after the brief from the source sheet, outline, census entry and card. Every line's reference (work, file and lines) is in the line; each was re-read.

1. **257, Into exile at Curubis with Cyprian.** The hearing and the order (KNOPF 4823–4827; date from the court record's day and consuls, note given); Cyprian's answer and the exile (KNOPF 4828–4836); the willing exile and the wish (VE 28055–28059; VL 41013–41015); the place, imagined and as it was (VE 28032–28036, 28044–28051; Cut first 1, card); the whole world one home (VE 28014–28016; Cut first 2 and outline Quotes, card, in narration).
2. **257, the first day at Curubis, Cyprian's dream of his sentence.** Witness at the head: Cyprian's own words, as Pontius gives them (outline Who tells it). The young man and the court (VE 28055–28065; wonder note); the tablet and the sign (VE 28065–28074; Cut first 31 and 32 detail, here); the delay, the judge's face, the fingers (VE 28074–28084; Cut first 12, 24 and 30 detail, here); waking glad, yet trembling (VE 28084–28089; Cut first 27, card).
3. **257 to 258, The year Pontius saw in the dream.** The day as a year (VE 28095–28102); the delay for church business and the poor (VE 28124–28136; Cut first 26, card); everyone knew his death was near (VE 28114–28117; Cut first 6, card); called back and at his gardens, as had been shown to him (KNOPF 4850–4857; Cut first 20, card); the messenger from Rome's bishop, by role (VE 28137–28139; Cut first 4, card; outline Do not say, "Pope Xistus").
4. **September 258, Cyprian's last days, and the last night.** The friends' offers (VE 28142–28149; Cut first 29's "of high rank" goes to the card); Cyprian's letter (EP 17370–17384); the arrest on 13 September (KNOPF 4857–4873; date note); the last night (VE 28181–28184; VL 41246–41248); the officer's dry clothes and Cyprian's answer, in narration (VE 28218–28226; outline Leave out and "For the card"); the one-line trial in new words from VL 41310, not Wallis's English (VE 28227–28230; VL 41309–41310; Cut first 22, card); the sentence (KNOPF 4901–4910; outline Explain it); Pontius's reading of it as prophecy (VE 28231–28239; Cut first 5, card); the death (KNOPF 4955–4956), with Pontius's "very day" in the note (VE 28112–28114).
5. **After 258, the year not given: Pontius writes the Life.** Witness at the head: Pontius, in his own book. His hearers' longing and his pressure on both sides (VE 27692–27700; Cut first 7 and 19, card); the forebears, the catechumens glossed, people not yet born (VE 27677–27682; Cut first 33, card; Words to explain); much to teach even apart from it (VE 27682–27685; Cut first 35, card); his aim (VE 27672–27677); his start (VE 27701–27708); what he was there for and what he learned of earlier things (VL 40333–40364; Cut first 8, card; D5 note); the estates (VE 27715–27741; Cut first 9, card); the earlier withdrawal, in his voice (VE 27905–27910; Cut first 15, card); the plague (VE 27958–27962, 27990–27992; Cut first 23, card); many things left out (VE 27976–27978; Cut first 10, card); the court record (VE 28002–28004); the book's end (VE 28294–28303).
6. **About 392, Jerome names the author.** JE 40833–40835; JL 57618–57622; date note from JE 38785 and 15402–15403 (Cut first 28, card).
7. **Later, Copied and kept.** The copying (VSB 4159–4161; HAR 260–264; note that the manuscripts are not held); Bede (BEDE 23904–23909; Cut first 11, card); the calendars and the crown, marked late (AASS 196261–196266, 196815–196824; Cut first 11 and Leave out, card). No year is given for Bede: the source sheet's "about 725" has no held line.

## Outline items sent to the card, and where they are

Every Cut first item marked **Card** is on the card: 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 15, 19, 20, 22, 23, 26, 27, 28, 33, 35 (timeline; 20 and 26 also in `uncertain`). Leave out items marked card: the soldier's dry clothes (timeline, period 4); the silence on the councils, Rome and the baptism quarrel (`uncertain` 11); the calendars' crown (timeline, period 7, and `uncertain` 13); Harnack's doubt about the dream and the modern debates over the kind of book, its date, the eyewitness, the court record and his style (`modernWorks`, by what each covers, never in the card's text). Words to explain: catechumens (timeline, period 5, glossed). Quotes section: "the whole world is one home" and "as had been shown to him" (timeline and `uncertain` 7, in narration, no quotation marks); the one-line trial (timeline, period 4, in new words). "For the card, not the story": Bede, the Roman calendar, Harnack, Delehaye, Monceaux, von Soden and Benson (`modernWorks`).

Not put on the card, by the header's rule on modern works (no modern opinion, date or identification as content; speculative or argued work left out): Dessau's identification of the author with a magistrate at Curubis, and Corssen's answer (contested identification, the works not held); Coxe's note that Pontius is said to have died a martyr, and Richardson's "Died about 260" (modern, unsourced, a year only modern notes give); Rigault's criticism (AASS 196852–196866); the manuscript count of 23 and the date 359 for the list (modern reports; the list's text not held). Monceaux's claimed gap between the plague and the exile (MON 11129–11131), a modern claim.

The Review and the Fresh read send nothing else to the card. Fresh read MINOR 2 (the bishop who confesses in his own city) is answered on the card by `uncertain` 9 and the timeline's letter line, which give the letter's reason in full.

## Claims not found

None. Every claim on the card stands on a cited line.

## Entry fields

For release to apply once the checker passes; the entry itself is not edited here.

1. **modernWorks (new).** Each modern work the outline used to clarify an old text or find one, and the five modern works moved from the card's `sources.about` word for word (title, author, and date as year):
   - {"title": "Das Leben Cyprians von Pontius: Die erste christliche Biographie", "author": "Adolf Harnack", "year": "1913", "note": "Hartel's Latin text of the Life with Harnack's changes, a German commentary on each chapter, and a study of its manuscripts, its date and its author."} (moved; HAR)
   - {"title": "Les passions des martyrs et les genres littéraires", "author": "Hippolyte Delehaye", "year": "1921", "note": "A study of the old accounts of the martyrs by kind, with a chapter on the Life of Cyprian and how it compares with them."} (moved; DEL)
   - {"title": "Histoire littéraire de l'Afrique chrétienne, vol. 2: Saint Cyprien et son temps", "author": "Paul Monceaux", "year": "1902", "note": "A literary history of Christian Africa; this volume covers Cyprian and his time, with a section on the Life and what it tells and leaves out."} (moved; MON)
   - {"title": "Cyprian: His Life, His Times, His Work", "author": "Edward White Benson", "year": "1897", "note": "A life of Cyprian in English, with notes on the places of his exile and death, among them the town of Curubis on the coast."} (moved; BEN)
   - {"title": "Geschichte der römischen Litteratur, Teil 3", "author": "Martin Schanz, Carl Hosius and Gustav Krüger", "year": "1922", "note": "A handbook of Latin literature from Hadrian to Constantine, with a section on the Life and a report of the scholarship on it to 1922."} (moved; SHK)
   - {"title": "Die cyprianische Briefsammlung: Geschichte ihrer Entstehung und Ueberlieferung", "author": "Hans von Soden", "year": "1904", "note": "A study of the manuscripts and old lists of Cyprian's letters and works, which records the Life copied with them."} (new; VSB, used for I1)
   - {"title": "S. Thasci Caecili Cypriani Opera Spuria (CSEL 3, part 3)", "author": "Wilhelm Hartel (ed.)", "year": "1871", "note": "The Latin edition of the works once ascribed to Cyprian, among them the Life and the court record of his hearings and death."} (new; VL, an edition, also in the card's sources)
   - {"title": "Hippolytus, Cyprian, Caius, Novatian (Ante-Nicene Fathers, volume 5)", "author": "Ernest Wallis (tr.)", "year": "1886", "note": "English translation of Cyprian's works and of the Life, with the American editor's notes."} (new; VE, a translation, also in the card's sources)
   - {"title": "Theodoret, Jerome, Gennadius, Rufinus (Nicene and Post-Nicene Fathers, second series, volume 3)", "author": "Ernest Cushing Richardson (tr.)", "year": "1892", "note": "English translation of Jerome's Lives of Illustrious Men, with notes."} (new; JE, a translation, also in the card's sources)
   - {"title": "Ausgewählte Märtyrerakten", "author": "Rudolf Knopf (ed.), third edition by Gustav Krüger", "year": "1929", "note": "The Latin court record of Cyprian's two hearings and death, with other early accounts of martyrs."} (new; KNOPF, an edition, also in the card's sources)
   - {"title": "Acta Sanctorum, Martii tomus primus", "author": "The Bollandists", "year": "1865", "note": "The saints of the first eight days of March, with a notice on Pontius for 8 March that prints parts of the Life and quotes the Roman calendar of saints."} (new; AASS, also in the card's sources)
   The volume titles of VE and JE are given from the files' own front matter as the census gives other volumes of the series; release checks them against each file's head.
2. **dates.** Old "c. 258" → new "257-258". The old sources fix his exile from 257 (KNOPF 4823–4836, by the consuls) and the last night in 258 (KNOPF 4857; VE 28181–28184), and nothing else of his life; the book's year is not given. `start` and `end` only place the entry and need no change, unless release sets `start` to 257 to match.
3. **regions: conflict.** The entry lists "Mediterranean", "Africa" and "Asia Minor". Nothing in the outline's Setting or the sources places Pontius in Asia Minor (S2: Carthage and Curubis). Proposed: ["Mediterranean", "Africa"].
4. **teaser:** kept. "Deacon of Cyprian of Carthage, who shared his exile and wrote the Life and Passion of Cyprian." It says no more than `knownFor` and the brief.
5. **major, toldWithin, atlasId, placeLabel, modernCountries:** no change. The entry exists, so no new entry file is written.

No other entry field (`voices`, `legacy`, `why`, `sourcing`) exists on this entry, so there is no other conflict.
