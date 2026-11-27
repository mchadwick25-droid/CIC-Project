# Card check H: Danubian Latin Christianity, Modalist Monarchianism, the Bardaisanite current (2026-11-27)

Independent check pass (`Brief-Kit/roles/card.md`, "The check pass"), under `Header.md` in this folder and `Stage-Two-Kit/Kit.md` sections 1 to 3. The checker wrote none of these cards. The briefs are thin and stay as they are; each card was checked only against what is held. Each shortDescription phrase, each `uncertain` item and every timeline line was opened at its cited lines in `cic/texts/`, with editors' notes read apart from the text. No writer's "checked by script" mark was taken on trust. The three short descriptions were re-scored with `python -m engine.m1.profile_readability`: grade 9.1, 8.7 and 9.4, all passing. Each is far simpler than the Montanism example. Short names follow each card's `Card_Edits`.

| Card | Verdict | Blocking | Minor |
|---|---|---|---|
| `danubian-latin-christianity` | FIX | 0 | 6 |
| `modalist-monarchianism` | FIX | 0 | 4 |
| `bardaisanite-current` | FIX | 1 | 6 |

---

## 1. `danubian-latin-christianity`: FIX

### What holds

- **shortDescription.** Each phrase stands on its held line: "Victorinus, bishop of Pettau" (N3 40945; PL23 58328), his commentaries (N3 40946-40950), "At the last he received the crown of martyrdom" (N3 40950-40951), "Ursacius, Valens, and one Germinius ... from Pannonia" (N4 56370-56373), and "these men produced a paper ... demanded that it should be preferred to every Council" (N4 56610-56615). Tested: "a creed that called the Son like the Father" is the creed's own wording as Athanasius prints it ("the Son is like the Father in all things", N4 56660). The report that Valens and Ursacius pushed it does not rest on their opponent alone. Socrates also says "Ursacius and Valens said that all former draughts of the creed ought to be considered as set aside, and the last alone, which had been prepared at their late convention at Sirmium" (N2 8512-8515). So it may be told plainly. There is no negative, contrast or dash, and it does not open on a placeholder. Each man is named by what he was then, and the text is clear read once.
- **Timeline.** Apart from the findings below, every line holds at its lines. The acts are named on each line. The wonders are in the act's voice (2.9, 2.10). Athanasius's mockery stays his (3.5, N4 56427-56435), and Probus's charge stays his (2.7, RUI 44518-44520, a question with "dicuntur"). No editor's year is used: not the note's "303, died 304" (N3 40945), Ruinart's 304, "a.d. 347" (N4 24735) or Kauffmann's 381. 351 is worked from Socrates's "after the consulate of Sergius and Nigrinian" (N2 7859-7860), and 359 from the consuls of the dated creed (N4 56619-56621). 392 is worked from the fourteenth year of Theodosius (N3 38784-38785). The working is shown on each line. Line 1.4 reads the Latin rightly ("propter gentes, quae seruierint Antichristo", VIC 9540-9541), and so does line 5.3 (VIC 7400-7406 against 7365-7371).
- **Shown dates.** "4th c." passes the date rule. The first dated events, "sub Diocletiano et Maximiano" (RUI 44304, 44491), are Widely Accepted as early in the 4th century, and the council of Aquileia is placed in "imperator noster Gratianus"'s reign (KAU 14744). 250 and 400 rest on no held line. The change is marked.
- **briefSources.** All five files exist. The brief quotes nothing, so there is no `quotationOriginals`.
- **uncertain.** Items 1, 2 and 5 hold at their lines (N3 40945-40951; VIC 4178-4195, 4223-4224; N3 42591-42607, PAU 6651-6669, 7110-7115).
- **Modern works.** Haussleiter, Migne, Ruinart, Kauffmann and Hartel are all editions. Four of the notes say what each covers. The Kauffmann note is fixed below (D6).
- **Menu.** Every section is filled or plainly marked. Timeline is the new field. People and stories come from census `people` (5), `voices` (4) and `documentedStories` (1). Kind's own section: nothing held (`entry` is null on the census). Connections come from `relationsSummary`. Legacy and today come from `legacy`, `livingEvidence` and period 5. Open questions are `uncertain`. Sources are `briefSources`, with Modern works kept apart.

### Findings

**D1. Timeline period 2, line 4, `text`: MINOR.** Read alone, the line makes the act contradict itself. The act gives Irenaeus's own reason: he cites Christ's word, and owns no one beside God.
- Old: "The act of Irenaeus says that Probus later asked Irenaeus whether he had a wife, children or parents, and Irenaeus said he had none. He told Probus that his children had the same God he had, who was able to save them."
- New: "The act of Irenaeus says that Probus later asked Irenaeus whether he had a wife, children or parents, and Irenaeus said he had none, citing Christ's word that whoever loves them more than him is not worthy of him. He told Probus that his children had the same God he had, who was able to save them."
- Support: RUI 44358-44363 ("Qui diligit patrem, aut matrem, aut uxorem, aut filios ... super me, non est me dignus ... nullum praesentem absque eo se nosse, atque habere fatebatur"), 44364-44365.

**D2. `uncertain`, item 3: MINOR.** This is not an open question in the source. The act itself explains the answer (D1), so the item presents the act's point as a doubt.
- Old: "Irenaeus's family. In the act, his children and the women of his house plead with him, yet later he tells Probus he has no wife, children or parents."
- New: (item removed)
- Support: RUI 44358-44363.

**D3. `uncertain`, item 4: MINOR.** The heading asks who led the quarrel, but the text never answers it. "The one text of theirs" is also wrong, because the dated creed is their paper too (N4 56610-56615). Socrates, who is not their opponent, holds their lead as well.
- Old: "Who led the quarrel. Athanasius, an opponent, gives the creeds and letters of Valens, Ursacius and Germinius, and judges them as foes of Christ. Their own letter to Julius is the one text of theirs this card draws on."
- New: "Who led the quarrel. Athanasius, who opposed Valens, Ursacius and Germinius, gives their creeds and calls them foes of Christ. Socrates, writing in the 5th century, also tells that Ursacius and Valens had the creed of Sirmium read at Ariminum. Their own words survive in their letter to Julius, which Athanasius keeps."
- Support: N4 56365-56373, 56427-56445 ("such foes of Christ are they"); N2 8510-8516; N4 24712-24738.

**D4. Timeline period 4, line 1, `text`: MINOR.** "They" can be read as Ambrose's side. Palladius says "nos", meaning his own side, with his own fellow bishops absent.
- Old: "The minutes of Aquileia record Palladius telling Ambrose and his side that it was their doing that the council was not a general and full one, and that with their fellow bishops absent they could not judge on the faith. Asked who those bishops were, Palladius answered the eastern bishops."
- New: "The minutes of Aquileia record Palladius telling Ambrose and his side that it was their doing that the council was not a general and full one. With his own fellow bishops absent, he said, his side could not judge on the faith. Asked who those bishops were, Palladius answered the eastern bishops."
- Support: KAU 14724-14727 ("absentibus consacerdotibus nostris nos de fide diiudicare non possumus"), 14728-14729.

**D5. Timeline period 5, lines 1 and 4: MINOR.**
- Line 1, `reference`: Anatolius is named only outside the cited range. Old: "Jerome, Letter to Anatolius, the preface to his revision, cic/texts/victorinus_opera-lat_haussleiter-csel49-1916.txt lines 4178-4193". New: "Jerome, Letter to Anatolius, the preface to his revision, cic/texts/victorinus_opera-lat_haussleiter-csel49-1916.txt lines 4178-4193; Anatolius named, line 4227". Support: VIC 4227 ("Anatoli carissime").
- Line 4, `text`: the cited English says "for neophites", and its first book is on candidates for baptism. The card's "for those preparing for baptism" goes past the cited line. Old: "Gennadius writes that Niceas, bishop of the city of Romatia, wrote six books of instruction in plain language for those preparing for baptism, among them books on faith in one sovereign, on the creed and on the Passover lamb." New: "Gennadius writes that Niceas, bishop of the city of Romatia, wrote six books of instruction in simple and clear language. The first tells how those who seek baptism ought to act, and others are on faith in one sovereign, on the creed and on the Passover lamb." Support: N3 42594-42597 ("composed, in simple and clear language, six books of Instruction ... How candidates who seek to obtain grace of baptism ought to act"), 42603-42607.

**D6. `modernWorks`, Kauffmann `note`: MINOR.** "Homoian" is a modern label, and "Paris" does not appear in the file header or at KAU 515-521. The writer offered to shorten this note.
- Old: "The Latin notes of Homoian bishops in the margins of a Paris manuscript, among them Maximinus's work against Ambrose with the minutes of the council of Aquileia, with a German commentary."
- New: "Latin notes written in the margins of a manuscript of Ambrose, among them Auxentius's letter on Wulfila and Maximinus's work against Ambrose with the minutes of the council of Aquileia, with a German commentary."
- Support: KAU header lines 3-11 (title, "Auxentius's own letter, with Kauffmann's own German editorial apparatus and commentary"); KAU 515-521 ("am rande einiger blätter des ersten buches von Ambrosius"); KAU 14683-14744.

---

## 2. `modalist-monarchianism`: FIX

### What holds

- **shortDescription.** Each phrase stands on its held line: "one Noetus, who was a native of Smyrna" (A5 23116-23118), "Christ was the Father Himself, and that the Father Himself was born, and suffered, and died" (A5 23142-23144), Epigonus "his minister and pupil ... during his sojourn at Rome" (A5 13280-13283), and Against Noetus and Against Praxeas. There is no negative, contrast or dash, and it does not open on a placeholder. Tested: "taught that Christ is the Father himself" is told as fact, and only Hippolytus gives it of Noetus. The second sentence says the teaching reaches us through its opponents, but a reader meets the bare claim first (M1). "His pupils" is plural, but Hippolytus names one pupil who went to Rome (M1).
- **Timeline.** Apart from the findings below, every line holds at its lines. The charges stay in Hippolytus's voice (2.3-2.7) and in Tertullian's (3.1-3.3). Eusebius quotes the letter of Dionysius (4.2, HE 39512-39520). Line 4.4 gives Dionysius of Rome's own words (N4 28529-28535). The Greek of Epiphanius is read rightly (PAN 30236-30252, 30299-30317), and so are Basil's letters (BAS 37231-37238, 37532-37542). "About 201" is worked from "about the ninth year of the reign of Severus" (HE 32209-32210), with the working shown. No editor's year is used: not 130, 245 or 375 (A5 23126-23138), and not 375 for Basil (BAS 37205).
- **Shown dates.** "c. 200 to 4th c." passes. It starts at Zephyrinus, about 201 from Eusebius's clue, and ends with Epiphanius and Basil, both Widely Accepted for the 4th century. Noetus's "not very long ago" (A5 23125-23126) cannot be narrowed. 190 and 270 rest on no held line. The change is marked.
- **briefSources.** All three files exist. On Heresies 36 (AUG 1715-1717) and 41 (AUG 1745-1765) are at the lines given. The brief quotes nothing.
- **uncertain.** Items 1, 2, 4, 5 and 6 hold at their lines. Item 2: A5 13280-13282 against 15528-15531. Item 4: A3 51037-51038; AUG 1754-1756 ("in Africa fuisse dicuntur"). Item 5: BAS 37231; A5 13610-13612. Item 6: AUG 1747-1748, 1760-1763 ("liquido invenire non potui").
- **Modern works.** Holl and Migne are editions, and each note says what the edition covers. Heine is rightly left out.
- **Menu.** Every section is filled or plainly marked, as in the writer's table. `entry` is null on the census.

### Findings

**M1. shortDescription: MINOR.** Put the witness first, and give Rome the one pupil Hippolytus names. The new text scores grade 9.4 (names out 6.2) with reading ease 81.7. That is simpler than the current text, and the point about opponents' books stays in `uncertain` 1.
- Old: "Noetus of Smyrna taught that Christ is the Father himself, who was born, suffered and died, and his pupils carried the teaching to Rome. Hippolytus and Tertullian wrote against it, and what it taught comes to us in their books."
- New: "Hippolytus reports that Noetus of Smyrna taught that Christ is the Father himself, who was born, suffered and died. A pupil of Noetus brought the teaching to Rome, and Hippolytus and Tertullian wrote against it."
- Support: A5 23116-23118, 23142-23144; A5 13280-13283 ("Epigonus becomes his minister and pupil, and this person during his sojourn at Rome disseminated his godless opinion"); A3 51037-51038, 51095-51097.

**M2. Timeline period 2, line 7, `text`: MINOR.** These are words Hippolytus puts in Callistus's mouth ("says (Callistus)"). "Gives Callistus's own words" lends them a certainty that a hostile report does not carry.
- Old: "Hippolytus gives Callistus's own words: he would not profess belief in two Gods, Father and Son, but in one."
- New: "Hippolytus quotes Callistus as saying he would not profess belief in two Gods, Father and Son, but in one."
- The rest of the line is unchanged. Support: A5 13855-13857 ("'For,' says (Callistus), 'I will not profess belief in two Gods, Father and Son, but in one'").

**M3. `uncertain`, item 3: MINOR.** "His rival" leans on the modern view of a rivalry for the see. The writer's own note says no held line gives that.
- Old: "Callistus. Hippolytus, his rival at Rome, charges that Callistus backed the teaching and then put Sabellius out to clear himself."
- New: "Callistus. Hippolytus, who opposed him at Rome, charges that Callistus backed the teaching and then put Sabellius out to clear himself."
- The rest of the item is unchanged. Support: A5 13816-13820 ("He acted thus from apprehension of me"), 13837-13839 ("'Ye are Ditheists'").

**M4. Timeline period 6, line 1, `text`: MINOR.** "Difficile ab aliquo sciuntur" means few know of the Noetians, which is different from "hard to find".
- Old: "The Noetians are hard to find, he says, but the Sabellians are on many people's lips."
- New: "Few people know of the Noetians, he says, but the Sabellians are on many people's lips."
- Support: AUG 1751-1752 ("Noetiani enim difficile ab aliquo sciuntur: Sabelliani autem sunt in ore multorum").

---

## 3. `bardaisanite-current`: FIX

### What holds

- **shortDescription.** Each phrase stands on its held line. Edessa: PAN 26327-26328. In Syriac: HE 26633-26637. "By our freedom each as he chooses": A8 68441-68443. The friend who wrote it down: A8 67908-67912, 68878-68879. The songs: N13 11241-11247 for Bardaisan, N2 32085-32089 for Harmonius. Ephrem's answer in the same meters: N2 32094-32103; N3 15063-15065. Tested: "He and his son Harmonius made songs" joins two witnesses, Ephrem for the father and Sozomen and Theodoret for the son. Neither excludes the other, and the clash over who came first stays in `uncertain` 4. There is no negative, contrast or dash, and it does not open on a placeholder. It is clear read once, at grade 9.4.
- **Timeline.** Apart from the findings below, every line holds at its lines. Ephrem's charges stay in his voice (3.1-3.5), and period 3 is headed by him. Eusebius's "never wholly washed off the filth" stays his (1.4, HE 26652-26657). Epiphanius's ship is his (1.7, PAN 26490-26493). Sozomen's "it is related" is kept (4.2). Both conversions are right: Tammuz of 465 of the Greeks falls in 154 (CH 49), and Haziran of 684 in 373 (CH 103). Each line shows its working and never uses Cowper's own "154 A.D." as the source. No editor's year is used: not 155, 172, 200, 216, 223 or 350 (N3 15060-15061, 40139; N13 11186, 11231; HE 26645-26650).
- **Shown dates.** "Late 2nd to 4th c." passes. Eusebius sets the writing in Marcus Aurelius's reign (HE 23032-23036, 26525-26526), which is Widely Accepted for the later 2nd century, and Ephrem died in 373 (CH 103). 180 and 400 rest on no held line. The change is marked.
- **briefSources.** All four files exist. The brief quotes nothing.
- **uncertain.** Items 1, 2, 4 and 5 hold at their lines. Item 1: HE 26652-26657, N3 40141-40142 against PAN 26326-26330, 26497. Item 2: A8 68441-68443 against MIT 606-608, N13 11261-11272. Item 4: N13 11241-11247 against N2 32085-32089, N3 15060-15062. Item 5: A5 12057-12058; PE 17926-17928; N3 40139; PAN 26326-26328.
- **Menu.** Every section is filled or plainly marked. People come from `bardaisan-of-edessa`, Philip and Ephraim, with `voices` (3) and the story. `entry` is null on the census.

### Findings

**B1. Timeline period 1, `headline`: BLOCKING.** "Is born at Edessa" stands on no held line. The Chronicle gives only the date ("Bardesanes was born", CH 49), Epiphanius places him "of those who lived in Edessa", and the card's own `uncertain` 5 shows the witnesses differ on his people. A birthplace the sources do not give is stated as fact.
- Old: "Bardaisan is born at Edessa, writes in Syriac against Marcion's followers and on fate, and is named among the schools of Valentinus"
- New: "Bardaisan is born, writes in Syriac against Marcion's followers and on fate, and is named among the schools of Valentinus"
- Support: CH 49; HE 26633-26644; A5 9656-9663.

**B2. Timeline period 1, `when`: MINOR.** The birth in 154 falls before the late 2nd century.
- Old: "In Bardaisan's lifetime, late in the 2nd century". New: "In Bardaisan's lifetime, in the 2nd century".
- Support: CH 49; HE 23032-23036, 26525-26526.

**B3. Timeline period 1, line 6, `when`, and `uncertain`, item 3: MINOR.** Epiphanius names the emperor himself: Antoninus "not the one called Pius, but Verus". His date therefore agrees with Eusebius's Marcus Aurelius, "also called Antoninus" (HE 23034-23035), so "an emperor Antoninus" understates him.
- Line 6 `when`. Old: "in the times of the emperor Antoninus, Epiphanius says". New: "in the times of Antoninus Verus, Epiphanius says".
- `uncertain` 3. Old: "His dates. The Chronicle of Edessa gives his birth in the year 465 of the Greeks. Eusebius places him in the reign of Marcus Aurelius, and Epiphanius in the times of an emperor Antoninus." New: "His dates. The Chronicle of Edessa gives his birth in the year 465 of the Greeks. Eusebius places him in the reign of Marcus Aurelius, and Epiphanius in the times of Antoninus Verus, not the one called Pius."
- Support: PAN 26407-26409 ("ἄχρι τῶν χρόνων Ἀντωνίνου Καίσαρος, οὐ τοῦ Εὐσεβοῦς καλουμένου, ἀλλὰ τοῦ Οὐήρου"); HE 23032-23036.

**B4. Timeline period 3, `when`: MINOR.** "At Edessa" is not on a held line for Ephrem's attacks. Hymn 51 is one of the Nisibene Hymns (N13 11189), and Sozomen calls Ephrem "a native of Nisibis" (N2 32051). Sozomen puts him at Edessa only shortly before his death (N2 32138-32140).
- Old: "At Edessa, in the 4th century". New: "In the 4th century".
- Support: N13 11188-11272; MIT 604-608, 917; CH 103.

**B5. Timeline period 1, line 8, and period 2, line 5, `note`: MINOR.** Two textual doubts are left silent.
- Line 1.8 has no note. Hippolytus's spelling varies, and the card takes the name as Bardaisan's. New `note`: "Hippolytus's text spells the name Bardesianes, or Ardesianes in Miller's text, lines 9660-9662." Support: A5 9660-9662.
- Line 2.5 has no note. The word "readings" is the translator's emended reading. New `note`: "The translator marks the word for readings as uncertain, lines 68971-68974." Support: A8 68971-68974 ("But what is meant is not clear").

**B6. `modernWorks`, Gifford `note`: MINOR.** This volume is the English only. Its file header says "The Greek is gifford1903 tomus I".
- Old: "An English translation of Eusebius's Preparation for the Gospel, with the Greek extract from Bardaisan's dialogue in Book VI, chapter 10."
- New: "An English translation of Books I to IX of Eusebius's Preparation for the Gospel, among them the extract from Bardaisan in Book VI, chapter 10."
- Support: PE header lines 1, 9 ("Gifford's introduction, then his English of Books I-IX ... The Greek is gifford1903 tomus I").

---

Nothing else was edited. Nothing was committed.
