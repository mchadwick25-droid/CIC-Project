# Card edits: The Roman Church in the Third Century

Starting card: `Card.existing.json` (the census entry's card fields; a tradition has no `card` field). New card: `roman-church-third-century.card.json`. Brief: `roman-church-third-century.brief.txt`. Every field and item not listed below is word for word, in the same order. The new keys (`uncertain`, `sources`, `quotationOriginals`) come at the end.

## How a tradition's card is shaped here (for the checker and release)

`tools/validate-census.mjs` has no card for a tradition: `checkCard` refuses a `card` on anything but a person, and `checkQuotationOriginals` and the quotation check run only for persons and councils. So the card file keeps the tradition entry's own fields, and these choices were made:

- `sources`: the tradition entry's own top-level list, in the format the tree page already shows (`work`, `type`, `note`), with `file` added to each item so the checker can tie each quotation to a cited file. The page ignores `file`.
- `quotationOriginals`: the `cyril-and-methodius` format, at the top level. Nothing on the tradition page reads it yet, and the validator does not check it for a tradition. A scratch check (same fold as the validator's `wordingFault`, tags stripped) finds each `printed` and `englishPrinted` at its lines, each file among `sources`, and each `modern` one of the brief's three quoted spans.
- `uncertain`: a list, as on a person card. The tradition page does not show it yet.
- Each documented story's modern work moves to that story's own `modernWorks`, which `checkModernWorks` allows.

For release: a page home for a tradition's `uncertain` and `quotationOriginals`, and a validator check of them, do not exist yet.

A scratch copy of the census, with this card merged into the entry and the brief as `longDescription`, was run through `node tools/validate-census.mjs` (result under "Validator" at the end).

## Quotations

The brief quotes three spans; each has one entry. All three run six words or more, so none carries `secondReading`.

1. **Q1.** Modern and printed: "I will not profess belief in two Gods, Father and Son, but in one." `anf05_hippolytus-cyprian-caius-novatian.xml` 13856-13857 (re-read: "(Callistus), “I will not profess belief in two Gods, Father and / Son, but in one."). The outline gives 13855-13857; the words stand on 13856-13857. The Greek is not held (Source_Sheet, H), so the English stands alone, as its `uncertain` says.
2. **Q2.** Printed (Latin): `cyprian_epistulae-lat_hartel1871-csel3-tei.txt` 1129-1133, "quos quidem separatos a nobis non dereliquimus ... peiores efficiantur." English printed: `anf05...xml` 28856-28860, "these, however, we did not abandon ... they should become worse." Both re-read.
3. **Q3.** Printed (Latin): `cyprian_epistulae...txt` 6825-6828, "magnus fraternitatis concursus factus ... fuissent liberati." English printed: `anf05...xml` 33011-33016, "a great concourse of the brotherhood was assembled ... of the dungeon." The outline gives 33011-33015; the last words, "of the dungeon", stand on 33016. Its `uncertain` keeps the outline's note on *fraternitas* and *concursus* (Outline, Quotes, Q3).

## Card fields

1. **why (claims the brief no longer makes).**
   Old: "Hippolytus was a learned presbyter who thought him wrong on every count. He set himself up as a rival bishop. He also wrote a Refutation."
   New: "Hippolytus was a presbyter who thought him wrong on every count. He also wrote a Refutation."
   Evidence: the approved-before-the-kit brief called him "a learned presbyter" and said he was "eventually functioning as a rival bishop"; the finished brief makes neither claim ("Hippolytus, a writer of that time who withstood two of Rome's bishops and lost"). Review B2: no old source calls him learned (only the NPNF editor's note, E 35651-35652). Outline, Do not say: "learned teacher" for Hippolytus; "Hippolytus was a rival bishop" is "Not said in the held old texts used here". Kit Part 1: the short texts may not repeat a claim the brief no longer makes. "presbyter" stays: the list of 354 calls him "Yppolitus presbyter" (`liber-pontificalis...duchesne1886.txt` 66805-66807).

2. **teaser (the same claims).**
   Old: "a learned rival who called himself bishop instead"
   New: "a rival who withstood him"
   Evidence: as edit 1. "withstood": Hippolytus, "reproved and withstood him" (`anf05...xml` 13627-13633); brief, "withstood two of Rome's bishops".

3. **sourcing (the same claim).**
   Old: "written by a man who claimed the see against its bishop"
   New: "written by a man who withstood its bishops"
   Evidence: as edits 1 and 2. Kit Part 1, Rigor: an identification only a modern work makes stays out of the card. (`sourcing` is not one of the short texts the role names; the checker may hold this edit back.)

4. **voices[1] (the same claims).**
   Old: "Hippolytus - the learned presbyter who opposed him, set himself up as rival bishop, and wrote nearly everything we know about it"
   New: "Hippolytus - the presbyter who opposed him and wrote nearly everything we know about it"
   Evidence: as edit 1. (As with edit 3, `voices` is not a named short text; the checker may hold it back.)

5. **legacy (new: What came of it, which the outline sends to the card).**
   Old ends: "... than any other surviving book."
   New adds: "In the 260s, after believers from Alexandria accused their own bishop before him, Dionysius of Rome wrote against both Sabellius, who said that the Son is the Father, and those who preached three Gods. Athanasius later quoted the letter against the Arians. Eusebius says the Roman custom of sending gifts to churches in every city lasted down to the persecution of his own day, and Basil says Dionysius of Rome sent men to ransom captive believers of the church of Caesarea in Cappadocia."
   Evidence: Outline, What came of it 2 and 3 ("For the card"). R1, `npnf204_athanasius-select-works-letters.xml` 28529-28534 ("he blasphemously says that the Son is the Father, and the Father the Son, but they in some sort preach three Gods"); R2, 29876-29880 ("went up to Rome; and they spoke against him in the presence of his namesake Dionysius the Bishop of Rome. And he, upon hearing it, wrote simultaneously against the partisans of Sabellius and against those who held the very opinions for uttering which Arius was cast out"); R3, `npnf201...xml` 25094-25101 ("the practice of the Romans which has been retained down to the persecution in our own days"; "to send contributions to many churches in every city"); R4, `npnf208_basil-letters-select-works.xml` 28629-28634 ("sent men to ransom our brethren from captivity"). "the 260s": Outline, What came of it 2 (R2's dating is the outline's; the old texts set it in Dionysius of Rome's time).

6. **documentedStories[0].text (clearly wrong: a held source contradicts it).**
   Old: "the unions of senatorial women with slaves and freedmen"
   New: "the unions of senatorial women with slaves or free men"
   Evidence: `anf05...xml` 13936, "whether a slave or free". Hippolytus says free, not freed. "senatorial" is listed below as not found.

7. **documentedStories[1].text (clearly wrong: the quoted words are not in the letter).**
   Old: "so that everyone could ‘be found ready’"
   New: "so that the brotherhood might be ‘strengthened and prepared for the spiritual conflict’"
   Evidence: the close of Cyprian's letter to Successus (ANF LXXXI), `anf05...xml` 41197-41199: "that everywhere, by their exhortation, the brotherhood may be strengthened and prepared for the spiritual conflict". "be found ready" does not stand in the letter; the file has it only in another letter (33787).

8. **documentedStories[0].sources and [1].sources (moved: modern works).**
   Removed, word for word as they stood: `{"work": "Allen Brent, Hippolytus and the Roman Church in the Third Century (Brill, 1995)", "type": "reference", "note": "On the rivalry and the reliability of the Refutation."}` and `{"work": "Candida Moss, The Myth of Persecution (HarperOne, 2013)", "type": "reference", "note": "On the growth of the Lawrence legend from the bare record of Sixtus."}`.
   Added: each story's `modernWorks`, the same words split into `title`, `author`, `year`, `publisher` and `note`. Evidence: the role ("a modern work now listed under the card's `sources` moves there word for word"); Source_Sheet, Library sweep ("Brent 1995, Moss 2013 ... modern, for the card's Modern works list at most"). Neither is held, so neither has a `url`.

9. **uncertain (new: what the outline sends to the card).** Five items:
   - What Callistus meant, and Hippolytus's charge that he made the Father suffer with the Son. Outline, Cut first 8 ("for the card"); Source_Sheet C6, X3; `anf05...xml` 13861-13869.
   - Who led the split of 251. Outline, Do not say ("Novatus from Africa ... card"); Source_Sheet N4, N4b, X1; `npnf201...xml` 38265-38270; `liber-pontificalis...txt` 66825-66827.
   - The year Callistus became bishop. Outline, Setting and Do not say; Source_Sheet X8; LibCat 66797, E 35480-35482.
   - Fabian's dove, his coming from the country, the people's cry. Outline, Cut first 6 ("for the card"); Source_Sheet P3, X4; `npnf201...xml` 36508-36526. Kept in Eusebius's voice as a report (Kit Part 1, a wonder).
   - Natalius's visions, the angels and his welts. Outline, Cut first 27 ("for the card"); Source_Sheet Z3, Z4; `npnf201...xml` 32252-32274. Kept in the writer's voice.

10. **sources (new: the old sources the brief and the card draw on).** Nine items, each with `file`. Each note says what the source holds, and carries the outline's remaining "for the card" items at their source:
    - Hippolytus, Refutation IX (`anf05...xml`): the brief's beats on Zephyrinus and Callistus (C1a 13725-13751; C3 13816-13819; C4 13819-13822; Z6 13553-13554, 13280-13285; Q1; C7 13873-13882; C8 13882-13888; C10 13899-13909; C12 13923-13938; C13 13938-13951). For the card: Smyrna (Cut first 22; Z6), Zephyrinus's two sayings (Cut first 7, 20; Z8 13619-13625), the cemetery (Cut first 24; C2 13802-13806), Paul's word and "so that sinners stay in the church" (Cut first 18, 29; C10), bishops not removed and twice-married clergy (Cut first 9; C9 13889-13897), the Catholic Church (Cut first 26; C14 13951-13953).
    - Hippolytus, Against Noetus (`anf05...xml` 23728-23732): the brief's "Hippolytus spoke of one God but two persons" (C6a).
    - Eusebius, Church History (`npnf201...xml`): V.28, the brief's opening (Z1 32190-32193, Z2 32216-32219 and 32244-32246, Z4 32267-32274); for the card, the cobbler and Victor (Cut first 19), the salary (Cut first 28), Zephyrinus's date (Cut first 23; S1 32209-32211). VI.20, the witness (35447-35449). VI.29, Fabian's election (36508-36526). VI.34 and VI.39, Philip and Decius (36995-36996, 37413-37416). VI.43, Cornelius's count, the split and the synod (38265-38299, 38565-38621); for the card, the orders by name (Cut first 31; N3) and the bishop received as a layman (Cut first 3; N5 38536-38540). IV.23, Rome's giving (R3). Chapters checked against the file's chapter divisions.
    - Eusebius, Greek (Schwartz): N3 (E-Gk 6919-6923), P3 (4930-4937).
    - Hartel's Latin letters (`cyprian_epistulae...txt`): Letter 8 (Q2; "Some gave way", CyL 1127-1129; "Rome's clergy", CyL 1235); for the card, people called back from sacrificing (Cut first 15; D3 1126-1127), widows, bedridden and prisoners (Cut first 10; D4 1141-1172), the dying penitent (D4), the burial of martyrs (Cut first 14; D4). Letter 49 (Q3; the confessors' return); for the card, the presbyters and five bishops (Cut first 11; N7 6785-6795), the people told (Cut first 12; N7), the confessors' confession (Cut first 25; N9 6829-6837), Maximus and the rest (Cut first 13; N10 6867-6869). Letter 55; for the card, Cornelius through every office and his election (Cut first 1, 16; N1 7673-7679) and his sitting in the chair (Leave out, "card"; N2 7715-7719).
    - The same letters in English (`anf05...xml`): Letter 25, the confessors in prison (Cut first 5; D6 31009-31013); Letter 30, the brief's "Rome went without a bishop" (D7 31706-31713).
    - The list of 354 (`liber-pontificalis...txt`): Fabian's regions and buildings (Cut first 2; P4 66818-66821).
    - Athanasius (`npnf204...xml`) and Basil (`npnf208...xml`): edit 5.

Every Cut first item marked "for the card" is now on the card, in `uncertain` or a `sources` note: 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 22, 23, 24, 25, 26, 27, 28, 29, 31. The outline's Leave out items marked "card at most" (Caius and the apostles' trophies) are already in `voices`.

## Entry fields

For release to apply once the checker passes them. Release also sets `longDescription` from the brief.

1. **why:** edit 1 above.
2. **teaser:** edit 2 above.
3. **relationsSummary:** no change. "The church of Rome after its house-church years, from about 200. The Novatian schism of 251 began inside it." agrees with the brief.
4. **sourcing, voices, legacy, documentedStories:** edits 3 to 8 above. These live on the entry; the card file holds them.
5. **uncertain, sources, quotationOriginals:** new on the entry, edits 9, 10 and Quotations above.
6. **documentedStories[0].modernWorks and documentedStories[1].modernWorks:** edit 8.
7. **modernWorks (new):** the printed editions and translations the outline used to read its old texts (Source_Sheet, abbreviations):

```json
[
 {"title": "Ante-Nicene Fathers 5: Fathers of the Third Century: Hippolytus, Cyprian, Caius, Novatian", "author": "Alexander Roberts and James Donaldson (ed.); J. H. MacMahon and R. E. Wallis (tr.)", "year": "1886", "note": "English translations of Hippolytus's Refutation of All Heresies and Against Noetus, and of Cyprian's letters with those of the Roman clergy and of Cornelius, with the editors' notes."},
 {"title": "Nicene and Post-Nicene Fathers, second series, 1: Eusebius, Church History", "author": "Arthur Cushman McGiffert (tr.)", "year": "1890", "note": "English translation of Eusebius's Church History, with notes on its dates, names and sources."},
 {"title": "S. Thasci Caecili Cypriani Opera omnia, part 2: the letters (Corpus Scriptorum Ecclesiasticorum Latinorum 3.2)", "author": "Wilhelm von Hartel (ed.)", "year": "1871", "note": "The Latin text of Cyprian's letters, among them the Roman clergy's letters and Cornelius's, with notes on the readings."},
 {"title": "Eusebius Werke, zweiter Band: Die Kirchengeschichte (Die griechischen christlichen Schriftsteller)", "author": "Eduard Schwartz and Theodor Mommsen (ed.)", "year": "1908", "publisher": "J. C. Hinrichs, Leipzig", "note": "The Greek text of Eusebius's Church History, with Rufinus's Latin beside it."},
 {"title": "Le Liber pontificalis: texte, introduction et commentaire, tome premier", "author": "Louis Duchesne (ed.)", "year": "1886", "note": "Includes the list of Rome's bishops from the Chronograph of 354, with the editor's years for its consulships."},
 {"title": "Nicene and Post-Nicene Fathers, second series, 4: Athanasius, Select Works and Letters", "author": "John Henry Newman and Archibald Robertson (tr.)", "year": "1892", "note": "English translations of Athanasius's works, among them those that quote Dionysius of Rome's letter."},
 {"title": "Nicene and Post-Nicene Fathers, second series, 8: Basil, Letters and Select Works", "author": "Blomfield Jackson (tr.)", "year": "1895", "note": "English translation of Basil's letters, with notes."}
]
```

Not added: the modern studies the source sheet says were "used only to find old texts" (Duchesne, Harnack, Koch, Benson, Poschmann, Bardenhewer). The sheet names authors only; the Library holds several volumes for most of them, and the sheet does not say which was used. They are left for the checker or the researcher to name, not guessed.

## Not found (left in place)

- why: "grave sin after baptism" (Hippolytus speaks of sins of the body and of a bishop's "sin unto death", 13873-13897; no held line says "after baptism"); "Almost by accident, it preserves more about second- and third-century religious movements than any other surviving book" (a judgment no old source makes). Also "two questions", where the brief tells three quarrels (not contradicted: Callistus did lead through these two).
- legacy: "That is the answer the Western church kept"; "Hippolytus wrote his Refutation to discredit Callistus" (the book is against all the heresies; Book IX against Callistus); the closing sentence, as in `why`. The legacy also asks a question only to answer it (Kit Part 1, Craft); not an edit this role makes.
- voices: Dionysius of Rome "bishop 259-268" and "the clearest doctrinal statement the Roman see made in this century".
- documentedStories[0]: "on Zephyrinus' death the church elected him" (Hippolytus says only that he "obtained" the post, 13816-13819; Outline, Do not say); "the church's cemetery on the Appian Way" (the road is an editor's note, 13805-13806); "readmitted Christians who had committed adultery after baptism" (Hippolytus: "sensual pleasures", 13873-13875); "senatorial women"; "What Hippolytus records as scandal, a later church would recognize as pastoral policy — the first known bishop ..." and "a noblewoman’s union with a poor Christian"; "exiled to the same Sardinian mines under Maximinus and died there" (the list of 354 says deported to Sardinia in 235, 66805-66808, with no mines and no death); "Rome venerates both as saints"; caveat, "administered the catacomb that bears his name is generally accepted".
- documentedStories[0].sources: Tertullian, "usually taken to be Callistus’" (Source_Sheet X2: the identification is modern and Contested).
- documentedStories[1]: Xistus "had been bishop for less than a year, and had spent it repairing the breach with Carthage"; "seized while presiding in one of the underground burial galleries on the Appian Way"; Damasus's inscription (not held: Source_Sheet, Library sweep); Lawrence "executed four days later"; Cyprian "arrested within the month".

## Validator

The scratch census (this card merged into the entry, the brief as `longDescription`) through `node tools/validate-census.mjs`: 629 movements, 736 edges, 10 eras, 0 errors, 4 warnings, all on other entries (short names). As said above, the validator checks no tradition's `quotationOriginals`, so that pass proves the keys break nothing; the quotation check is the scratch fold check under "How a tradition's card is shaped here". The entry-level `modernWorks` above was not in the scratch run.

## Changes after the grade fixes

The brief changed after this card was written (`Grade_Fixes_Applied.md`, `Grade2_Fixes_Applied.md`, `Grade3_Fixes_Applied.md`). The card now applies every correction in `Card_Check.md` (FIX) and follows the final brief.

### From `Card_Check.md`, applied as given

1. **legacy:** "Athanasius later quoted the letter against the Arians." becomes "Athanasius later quoted the letter against the Arians, who held that the Son of God was a creature." (Ath 28469.)
2. **documentedStories[0].text:** "to manage the church’s cemetery on the Appian Way, and on Zephyrinus’ death the church elected him." becomes "to manage the church’s cemetery, and on Zephyrinus’ death he became bishop." (H 13804-13806, 13816-13819.)
3. **documentedStories[0].text:** "he readmitted Christians who had committed adultery after baptism; he recognized as marriages the unions of senatorial women with slaves or free men;" becomes "he said he forgave all their sins, sins of sensual pleasure among them; he let women of rank count a companion, slave or free, as a husband;" (H 13873-13875, 13934-13938.)
4. **documentedStories[0].text:** the sentence "What Hippolytus records as scandal, ... as a marriage." removed.
5. **documentedStories[0].text:** "Hippolytus was eventually exiled to the same Sardinian mines under Maximinus and died there;" becomes "Hippolytus was eventually exiled to Sardinia, in 235;" (LibCat 66805-66808.)
6. **documentedStories[0].caveat:** the sentence "That Callistus was a former slave and administered the catacomb that bears his name is generally accepted." removed.
7. **documentedStories[0].sources[1].note:** becomes "A hostile witness to an edict on readmitting adulterers, by a bishop it does not name."
8. **documentedStories[1].text:** "had been bishop for less than a year, and had spent it repairing the breach" becomes "had spent his time as bishop repairing the breach" (E 41758; LibCat 66908-66911.)
9. **documentedStories[1].text:** "underground burial galleries on the Appian Way where" becomes "underground burial galleries where" (H 41184-41186.)
10. **documentedStories[1].text:** "He was himself arrested within the month." removed.
11. **voices[5]:** becomes "Dionysius of Rome - bishop from 259, whose letter against Sabellian and tritheist readings, written into the controversy with his Alexandrian namesake, Athanasius later quoted" (LibCat 66915-66917.)
12. **why** and **legacy:** the sentence on second- and third-century religious movements removed from each.

Each cited line was re-read in its file. These claims leave the "Not found" list above: "the church elected him", the Appian Way (both stories), "adultery after baptism", "senatorial women", the "pastoral policy" sentence, the Sardinian mines and death, the catacomb caveat, "usually taken to be Callistus’", "less than a year", "arrested within the month", "259-268", "the clearest doctrinal statement", and the closing sentence of `why` and `legacy`.

### From the final brief

13. **why (a claim the brief no longer makes).** Old: "Callistus, a former slave once sent to the Sardinian mines, became bishop of Rome." New: "Callistus, a former slave, became bishop of Rome." Evidence: the brief now says only "Callistus, who had been a slave" (paragraph 3). The mines are Leave out (`Fixes_Grade2.md` cut a; Outline, Cut first 24), and Kit Part 1 bars a short text from repeating a claim the brief no longer makes. The first documented story keeps the mines, as Hippolytus tells them.
14. **sources, Hartel Letters 8, 49 and 55, note (what the brief now says).** "Letter 49: Cornelius to Cyprian on the confessors' return; they came" becomes "Letter 49: Cornelius to Cyprian on the confessors' return; they said they had been deceived; they came". Evidence: the brief, "the confessors who had sided with Novatian came back, saying they had been deceived". CyL 6748 with 6776, "circumuentos se esse / adfirmarunt"; CyL 6831-6832, "circumuenti sumus perfidia et loquacitate captiosa"; H 32980-32981, "they affirmed that they had been deceived" (ANF Letter 45, already in `sources`). Re-read.

No other field changes:

- **Quotations.** The final brief quotes the same three spans, word for word. Each `modern` matches the brief; each `printed` and `englishPrinted` was re-read at its lines (H 13856-13857; CyL 1129-1133 with H 28856-28860; CyL 6825-6828 with H 33011-33016) and passes the fold check, each file in `sources`. Nothing is added or removed.
- **"To the card" in the grade fixes.** Outline, Cut first 24 now sends only the cemetery to the card, which the Hippolytus `sources` note already carries ("Callistus set over the church's cemetery"). Cut first 27 now sends only Natalius's welts, which `uncertain` ("Natalius's return") already carries. That item also names the visions and the angels' scourging, which the brief now tells in the same writer's voice ("A writer of his day says ..."), so it agrees with the brief and stays. Every other cut in `Fixes_Grade.md`, `Fixes_Grade2.md` and `Fixes_Grade3.md` is Leave out.
- **The rest of the new wording** ("early in the 200s", "fed more than fifteen hundred widows and poor", "sacrifice to the gods", "but the church sided with them", "out of the church", "a woman of rank") is already covered by the `sources` notes (Eusebius V.28 and VI.43; Hippolytus Book IX) and contradicts nothing on the card.

### Entry fields after the grade fixes

- **why:** Card_Check FIX 12 and edit 13 above, on top of edit 1.
- **legacy, voices, documentedStories:** Card_Check FIX 1 to 12, as above.
- **sources:** edit 14.
- **longDescription:** release sets it from the final brief.
