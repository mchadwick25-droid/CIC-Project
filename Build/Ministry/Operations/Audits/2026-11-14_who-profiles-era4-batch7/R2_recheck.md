# R2 recheck: era 4 Who batch 7

Round 2 of at most three. It is a targeted recheck by a fresh Opus agent that had not seen the drafting, round 1 or the fixes, at full effort. It covers all seven profiles, `records.json` and the README.

## Scope

The seven ids in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era4/batch7/`: `symeon-the-new-theologian` (major, cap 2:30), `niketas-stethatos`, `cedd-and-chad`, `elipandus-of-toledo-and-felix-of-urgell`, `paul-the-deacon`, `paulus-emeritanus`, `pisentius-of-coptos-and-john-the-elder`, with each `.brief.txt`, `.card.json`, `audio/<id>.audio.txt`, its `records.json` entry, and `README.md`. Length is not flagged here: the pairs run 2:24 to 2:28 pending a coordinator call, and each card's `briefLength` matches its brief.

## Method

Reviewer: independent Opus, first sight of these files. I edited no profile file. I made no git write and no web, paid or model call, and used local reads and scripts only. Inputs: `CLAUDE.md` in full, the review brief, `R1_review.md` parts A and B, `R1_changes.md`, era 4 batch 5's `R2_recheck.md` for form, `Who_Profile_Pattern.md`, the Decision-Log Who entries of 2026-11-12 to 2026-11-14, and the fix diff `git diff 11e9fd88 HEAD` over the batch folder (11e9fd88 is the drafts commit, the parent of d27451b7 "round 1 part A fixes"; 28f9dee0 carries part B and the R1 files). The working tree is clean for this folder.

Short names follow R1: PG152, PHIL2, PG94, PAISIUS, NIL, WILL, CLARKE, GILES, PLUMMER, AASS-M3, PL96, ALC, FEROTIN, FOULKE, DALTON, PL80, BUDGE13, CRUM. Every changed sentence and card string was treated as a new claim and opened again in its vendored file with 15 to 60 lines around it, folding OCR noise, hyphen breaks and Migne's two columns. Absence searches across all of `cic/texts/` (file names and text): Patrologia Graeca 120, Symeon and Niketas files, Agobard and his book against Felix, PL 104, "Georg Waitz", "Lowther", and the Life of Pisentius for every "year" and "indiction". Brief fixes below were scored on scratch copies in `/tmp/claude-0/-home-user-CIC-Project/c61097dc-d787-5983-8ed0-252e6ba75c23/scratchpad/fixR2/`.

## Mechanical checks (all seven)

A script confirmed that each audio file equals its brief with `[calmly] ` at the start and `[warmly] ` at the start of the last paragraph. No tag is in any brief or card. `records.json` and all seven cards load as JSON; `records.json` holds exactly the seven ids. Every card keeps the batch's field order, with empty fields absent (Cedd and Chad has no `keyWorks`).

| Profile | Words | Time @162 | FK | Flesch | `briefLength` | Longest brief sentence |
|---|---|---|---|---|---|---|
| symeon-the-new-theologian (major) | 404 | 2:30 | 7.62 | 66.19 | about 2 minutes 30 seconds | 24 |
| niketas-stethatos | 354 | 2:11 | 8.87 | 62.79 | about 2 minutes 15 seconds | 26 (P4, the Humbert reply) |
| cedd-and-chad (pair) | 389 | 2:24 | 6.38 | 74.94 | about 2 minutes 30 seconds | 27 twice (P1 Lent, unchanged, ends in a quote; P4 Theodore, new: R2-M4) |
| elipandus-of-toledo-and-felix-of-urgell (pair) | 399 | 2:28 | 6.74 | 73.92 | about 2 minutes 30 seconds | 26 (P6, the Agobard sentence) |
| paul-the-deacon | 363 | 2:14 | 5.95 | 75.40 | about 2 minutes 15 seconds | 24 |
| paulus-emeritanus | 348 | 2:09 | 6.23 | 75.55 | about 2 minutes | 23 |
| pisentius-of-coptos-and-john-the-elder (pair) | 399 | 2:28 | 6.20 | 78.78 | about 2 minutes 30 seconds | 32 (P4, mostly quotation, unchanged) |

All pass `grade_text` (FK 10 or below, Flesch 60 or above), and the figures match `R1_changes.md`. Each `briefLength` fits its brief; Paulus Emeritanus at 348 words reads "about 2 minutes", as Antony of Choziba (348) and John of Nikiu (352) do in batch 5. Niketas has the thinnest Flesch margin (62.79).

Quotations: all 18 double-quoted strings in the briefs (Cedd and Chad 7, Paul the Deacon 3, Pisentius and John 8) and the one in a card (Pisentius `dates`, "this fifth year") occur verbatim, whitespace- and hyphen-tolerantly, in a cited held file: GILES, FOULKE (the new "to us, although decayed." spans l.11211-11213 with a footnote mark) and BUDGE13 ("this fifth year", l.18571). Symeon, Niketas, Elipandus and Felix, and Paulus carry no quotation marks; their Greek and Latin are told in modern words. No British spelling in narrator text ("honour" stands only inside a Budge quotation).

---

## 1. R1 findings

### Symeon the New Theologian

| Finding | Status | Evidence |
|---|---|---|
| A-B1 (ordination) | RESOLVED | PHIL2 l.23054-23085: "Ἔλεγε δὲ καὶ τοῦτο, ὡς περί τινος ἄλλου, ἑαυτὸν ὑποκρύπτων ... ὅτε με ἐχειροτόνουν, καὶ τὴν εὐχὴν τοῦ ἱερέως ὁ Μητροπολίτης ἔλεγε ... ἁπλοῦν μὲν καὶ ἀνείδεον, πλὴν ὡς φῶς". The passage stands among the numbered chapters and reports his saying in the third person, so "In a passage printed with his chapters ... he tells it" is fair. PG152 l.19615-19632: Combefis's "a Nicolao Chrysoberge patriarcha" and the forty-eight years, with the Life's Greek that he told it "as of another". The reworded P1 ("simple and formless, as light"; "names the patriarch Nicholas Chrysoberges as his ordainer"; "Niketas says" on the forty-eight years) is sound. P4's "born blind" sentence cut; card `uncertain` 2, the records claim and the contested claim are in. |
| A-B2 (the close) | RESOLVED | PG152 l.20368-20378. The mockers ask "Τίς δὲ Θεὸν εἶδεν", so the worker's "saw God before" gives the pronoun its right referent. "he thinks" for οἶμαι keeps the hedge in Symeon's mouth. |
| A-B3 (false absence) | RESOLVED | NIL l.3139-3146 ("якоже глаголеть Симеонъ Новый Богословъ"); PHIL2 l.69890-69930, the simpler-Greek George story. No PG 120 file is held. |
| A-M1, A-M2 | RESOLVED | "a monk of Studios, Symeon called the Pious"; "blotted out on the icon" (l.20270, "oblini"). |
| A-M3 | RESOLVED | "could well suspect" (l.20222, "Potuit ... suspectum habere"). |
| A-M4 | RESOLVED | Short form, "Combefis adds judgments of his own." No process narration left. |
| A-M5 | RESOLVED | "hard to read and run to 152 or 153" (PHIL2 l.23040-23046). |
| A-M6 | RESOLVED | "Combefis reckons from the Life that he lived on into the time of the patriarch Alexius" (l.20233-20237, "videatur vixisse"); "reckons" keeps his "videatur". |
| A-M7 | WITHDRAWN in R1 | Not counted. |
| A-M8 | RESOLVED | CLARKE l.4250-4256, "He was tried for heresy on other counts"; the file is dated 1925 and its preface signs Lowther. |
| A-M9 | RESOLVED | PAISIUS l.9101-9104. |
| A-M10 | RESOLVED | "the Jesuits Henschen and Papebroch, the Bollandists" (l.19540-19541, "in suo Martio"). The shorter form is right: the given names are not in the line. |
| A-M11 | RESOLVED, with R2-M1 | PG152 l.29300-29305, "Symeonem notat ejusque discipulos". Calecas is bare at first mention. |

### Niketas Stethatos

| Finding | Status | Evidence |
|---|---|---|
| A-B4 | RESOLVED | PG94 l.13686-13708: "Hoc etiam tempore Pectoratus sermonem ... edidit", then "Putaverim ego ... post discessum Humberti". "reasons that" in brief and card; records tagged Inferential-Thin. |
| A-B5 | RESOLVED, with R2-M3 | PAISIUS l.10202-10220 ("Святаго же Никиты Стифата точно двадесять и двѣ главы, а цѣлая въ насъ ... не обрѣтается") and l.10486-10494 (old Slavonic, "части нѣкоторыя"). The R1 wording's "his house" can be heard as Paisius's. |
| A-M12, A-M13, A-M14 | RESOLVED | WILL l.14766-14767, 14809-14810, 14805-14807. |
| A-M15 | PARTLY | The variant is now stated, but "which Will takes for a slip" misreads him. See R2-M2. |
| A-M16 | RESOLVED | "Humbert of Silva Candida" at first mention in brief and card. |
| A-M17 | RESOLVED | WILL l.24280-24306: "quod totis viribus tueri conatus est Nicetas Pectoratus, hoc est ab anno circiter 1050 ad 1100". |
| A-M18 | RESOLVED | "The reply calls him ..."; Isaiah 65:20 in WEB l.45163, in the records. |
| A-M19, A-M20 | RESOLVED | WILL l.12261; records sides split between Will and Combefis. |
| Worker's cuts | SOUND | The Gregory of Sinai sentence stays on the card (`legacy.traces` 1). With the thesis sentence gone, P5 opens on Le Quien; after P1's recantation the paragraph still reads as a question of whether it held. |

### Cedd and Chad

| Finding | Status | Evidence |
|---|---|---|
| A-M21 | RESOLVED, with R2-M4 | "of the Deiri" (GILES l.7568); "Aidan of Lindisfarne"; "Wilfrid of Ripon"; "Theodore of Tarsus, the new archbishop" (GILES l.8759); Egbert placed (l.9128-9131). The Theodore wording lifts its sentence to 27 words. |
| A-M22 | RESOLVED | l.7589-7591. |
| A-M23 | NOT RESOLVED: the card fix is wrong | "the monastery Cedd founded, his brother Cynebil built" rests on Giles's ambiguous "he there built" (l.7641-7643). Bede's preface says the monastery "was built by them", Cedd and Ceadda (l.202-204), and the Latin runs on to Cedd. See R2-B1. |
| A-M24 | RESOLVED | Chad's consecration now opens `uncertain`. |
| A-M25 | RESOLVED | AASS-M3 l.32745-32746, "S. Cedda ... anno [DCLXIV] mortuus" (OCR "nCrXIiV"). |

### Elipandus of Toledo and Felix of Urgell

| Finding | Status | Evidence |
|---|---|---|
| B-B1 | RESOLVED | ALC l.24319-24324 ("adhuc vivens nonnullos docuerit") and l.24380-24384 ("ad finem usque vitae suae pristinis suis erroribus adhaesisse schedula ab ipso scripto relicta prodidit, ut idem Agobardus testatur"). Brief, card `uncertain` 5 and records all agree. No Agobard file is held. |
| B-B2 | RESOLVED | PL96 l.72204-72208 ("testimonia sanctorum Patrum ... Toleto deservientium ... In missa de Coena Domini"); FEROTIN l.25281-25296. |
| B-B3 | RESOLVED | Four letters in PL 96; the Spanish bishops' letter in PL 101. |
| B-B4 | RESOLVED | The fifty-years sentence is gone; the records note gives the OCR reading. |
| B-B5 | RESOLVED | Frankfurt now "where the council condemned the teaching". |
| B-M1 | RESOLVED | Both splits in; P2 and P7 have no sentence past 25 words. |
| B-M2, B-M3 | RESOLVED | "pretense"; "proved wrong" (ALC l.18664, "veraciter convictus"). |
| B-M4 | RESOLVED | ALC l.25282-25291, "Certe anno 800, quo Alcuinus ... scripsit". |
| B-M5 to B-M9 | RESOLVED | "Pope Hadrian I"; one term "the Frankish annals"; Antonio (PL96 l.70124-70137: "ob ignorantiam ... sub jugo Saracenorum" without a hedge, then "contagione forsan"); Madrisi placed (ALC l.25295-25296, "editorem Operum S. Paulini Aquileiensis"); "with Madrisi places his death". |
| B-M10 | RESOLVED | Letter III claim split; four witness lines added. |
| B-M11 | DONE, for the coordinator | The Antiphrasius sentence moved to the card (`remembered` 2); 399 words; `briefLength` "about 2 minutes 30 seconds". The README's account of the call is R2-M8. |

### Paul the Deacon

| Finding | Status | Evidence |
|---|---|---|
| B-B6 | RESOLVED | DALTON l.26793, "Paul the Deacon (Paul Warnefrid, deacon of Friuli)"; Dalton added to `sources.about`. |
| B-M12 | RESOLVED, with R2-M5 | FOULKE l.810-815. The split leaves the second sentence without Foulke. |
| B-M13, B-M14 | RESOLVED | "Pope Gregory the Great"; P1 split. |
| B-M15 | RESOLVED | "to us, although decayed." verbatim (l.11211-11213). |
| B-M16, B-M17 | RESOLVED | `dates` without Bethmann; "Duke Arichis and Adelperga" (l.503-504). |
| B-M18 | RESOLVED | "Georg Waitz, who completed Bethmann's edition" (FOULKE l.165-168; the given name is held elsewhere, e.g. the Kauffmann Auxentius file). |
| B-M19 | RESOLVED | Two contested claims added. |
| Worker's cuts | SOUND | The wolf shot and the Metz history: the card keeps Metz (`legacy.traces` 2); the brief's story still runs from the wolf to the ash tree. |

### Paulus Emeritanus

| Finding | Status | Evidence |
|---|---|---|
| B-B7 | RESOLVED | The 1638/1658 item is gone; the records note gives the OCR reading. |
| B-M20 to B-M25 | RESOLVED | The P1 split ("He had led the boy" keeps the Lord as subject); "only" dropped; "Most of the rest"; "He notes that ... and that Paul does not name Stephen" now ties the reason to Tamayo; "scornful readers", "set down what was true"; "Masona's own time". |

### Pisentius of Coptos and John the Elder

| Finding | Status | Evidence |
|---|---|---|
| B-B8 | RESOLVED | BUDGE13 l.18571 "of this fifth year [of the Indiction]". A search of the whole Life for "year" and "indiction" finds no other dating, so "John gives only" holds. Card `uncertain` 1 and 2 now agree. |
| B-M26 | RESOLVED | "writes his disciple, John the Presbyter" (title, l.15724-15731). |
| B-M27 | RESOLVED, with R2-M6 | One vessel, then "them" for the vessels John found full (l.17232-17240, "I found them filled with water up to their brims"). R1's wording drops Pisentius's "I think". |
| B-M28 | RESOLVED | "Some things John only heard, and he says so." |
| B-M29 | RESOLVED, reworded | Told in modern words, "he cried out, in the words of the great John of Constantinople, that he loved the life of peaceful contemplation" (l.16726-16731). Sound: it keeps the borrowing and avoids altering Budge's spacing inside quotation marks. |
| B-M30 | RESOLVED | l.18596-18598, "three incidents ... which find no mention in our manuscript". |
| B-M31 | RESOLVED | "bishop of Coptos in Upper Egypt" in P1; the P2 sentence cut. |

### README and batch-wide

| Finding | Status | Evidence |
|---|---|---|
| A-M26 | RESOLVED | Every `briefLength` matches its brief (table above). |
| A-M27 | RESOLVED | "at the start of the last paragraph". |
| B-B9 | RESOLVED, with R2-M7 | The false absence is gone. "letters to him" settles an identity the card leaves open. |
| B-M32, B-M33 | RESOLVED | "389 to 399 words", recounted after the fixes; the window line now covers his consecration and the Persian years. |

---

## 2. New findings

### Blocking

- **R2-B1 BLOCKING (`cedd-and-chad` card `knownFor`; items 1 and 7; introduced by the A-M23 fix; a misread told as settled).** "Lastingham, the monastery Cedd founded, his brother Cynebil built, and Chad ruled after him." The claim rests on Giles's "Cynebil readily complied, and when the time of fasting and prayer was over, he there built the monastery" (GILES l.7641-7643), where "he" can be Cedd or Cynebil. Bede's own preface settles it the other way: "we learned from the brethren of the monastery, which was built by them, and is called Lastingham", "them" being Cedd and Ceadda (GILES l.197-204). The Latin runs on with Cedd as subject: "Cui cum ille libenter adquiesceret, expleto studio ieiuniorum et orationis, fecit ibi monasterium ... ubi educatus erat", and the next sentence's "Qui" is Cedd, who held the see and the monastery (PLUMMER l.20999-21004). No records claim stands behind the Cynebil clause. Fix, `knownFor` first sentence: "Two English brothers whom Bede tells together, through Lastingham, the monastery Cedd founded and Chad ruled after him." (This is the draft wording and the README's.)

### Minor

- **R2-M1 MINOR (`symeon-the-new-theologian` card `legacy.remembered` 2; item 8).** "Manuel Calecas" is bare at his only mention. The held volume is his (PG152 header: "Manuelis Calecae ordinis Fratrum Praedicatorum"), and the note is on his attack on the Palamite monks (l.29294-29305). Fix: "In a note, Combefis reads the deluded monks that Manuel Calecas, a Dominican who wrote against the Palamites, attacks as Symeon and his disciples."
- **R2-M2 MINOR (`niketas-stethatos` card `dates`; item 1; from the A-M15 fix).** "Some copies read the eleventh year, which Will takes for a slip." Will says the opposite of a slip: "Quod in aliis exemplis, Anno undecimo ... legitur, id non forte factum est, sed errore chronologico. Multi enim legationem ad a. 1053 referunt" (WILL l.14797, 14832; OCR "1653"). It was no accident but a dating error. Fix: "Some copies read the eleventh year. Will puts this down to an error in dating, since many placed the embassy in 1053." Records: add "(Will: 'non forte factum est, sed errore chronologico', l.14797, 14832)" to the recantation claim.
- **R2-M3 MINOR (`niketas-stethatos` card `legacy.traces` 2; item 4; from the A-B5 wording).** "A monk on Athos told him that his house held only twenty-two in Greek" lets "his house" be heard as Paisius's. The monk speaks of his skete, "въ насъ" (PAISIUS l.10172-10174, 10217-10219). Fix: "Paisius Velichkovsky translated his three hundred chapters into Slavonic. A monk in a skete on Athos told him the skete held only twenty-two in Greek, and Paisius says the older Slavonic had only parts of the three hundreds." Records claim: "only twenty-two chapters in Greek in his skete".
- **R2-M4 MINOR (`cedd-and-chad` brief P4; item 4; from the A-M21 fix).** "When Theodore of Tarsus, the new archbishop, told him he had not been properly consecrated, Chad offered to resign, "for I never thought myself worthy of it."" runs 27 words, up from 23. Fix: "Theodore of Tarsus came as the new archbishop. When he told Chad he had not been properly consecrated, Chad offered to resign, "for I never thought myself worthy of it."" (GILES l.8882-8888; the quotation unchanged.) Scored with R2-B1 left to the card: 392 words, about 2:25, FK 6.18, Flesch 75.61; `briefLength` unchanged.
- **R2-M5 MINOR (`paul-the-deacon` brief P3; items 1 and 5; from the B-M12 split).** "Foulke says he taught Greek there. By the king's order he gathered a book of the church fathers' sermons, perhaps begun at court and finished at Monte Cassino." The second sentence now stands in the narrator's voice; the order, the content and the "perhaps" are Foulke's (FOULKE l.808-812: "the collection and revision of the homilies of the fathers of the church which he made by order of the king, and which was possibly commenced about this time"). Fix: "By the king's order, Foulke adds, he gathered a book of the church fathers' sermons, perhaps begun at court and finished at Monte Cassino." Scored: 365 words, about 2:15, FK 5.95, Flesch 75.52.
- **R2-M6 MINOR (`pisentius-of-coptos-and-john-the-elder` brief P1; item 1; a hedge dropped, from the B-M27 wording).** "Pisentius told John there was water in one of the vessels". Pisentius says "'I think there is water in the water-vessels, in one of them which we have forgotten.'" (BUDGE13 l.17231-17233). The "I think" makes what follows a wonder to John; without it Pisentius knows beforehand. Fix: "When their water ran out, Pisentius said he thought there was water in one of the vessels, which they had forgotten." Scored: 400 words, about 2:28, FK 6.20, Flesch 78.81.
- **R2-M7 MINOR (README, "The pairs"; from the B-B9 wording).** "beside letters to him among the Epiphanius papers". The card says the letters are "to and from a bishop of that name" and that "Crum warns that not every Pesenthius in them is the bishop" (CRUM l.24825, 30810, 30956). Fix: "for Pisentius it is the main one, beside letters to and from a bishop of his name among the Epiphanius papers, the synaxaries and Abu Salih."
- **R2-M8 MINOR (README, opening paragraph).** "That pairs may run to the 2:30 cap, which stays a cap and not a target, is the coordinator's call (2026-11-14), which Mark may overrule." `R1_changes.md` says the worker asked the coordinator; this review's brief says the call is pending; the Decision Log holds no such entry. The README reports as made a call that is not yet on record. Fix, until the call is logged: "The worker has asked the coordinator (2026-11-14) to let pairs run to the 2:30 cap, which stays a cap and not a target. The call is pending, and Mark may overrule it." Once it is logged, cite the Decision-Log entry instead.

---

## 3. Each brief read whole

- **Symeon.** The new P1 reads cleanly: Symeon's telling first, Niketas's naming of the ordainer second, both placed. "he thinks" in P7 reads as Symeon's. No new fault.
- **Niketas.** With the thesis line gone, P5 rests on Le Quien's reasoning and the Latin writer, and is clear after P1. No new fault.
- **Cedd and Chad.** One new long sentence (R2-M4). The card's opening line is R2-B1.
- **Elipandus and Felix.** P3's two sentences now keep the prayers as Elipandus quoted them. P6 places Froben before the Agobard report and the 800 letter. P7's "Yet Alcuin, he wrote, now hunted him" keeps the complaint in Elipandus's mouth (PL96 l.71926-71934). No new fault.
- **Paul the Deacon.** R2-M5 only. The closing quotation now carries "although decayed", which the next line of Paul's text needs.
- **Paulus Emeritanus.** "He notes that" ties Stephen to Tamayo. No new fault.
- **Pisentius and John.** R2-M6 only. "a repeating count that does not fix the year" defines the indiction plainly.

## 4. Not findings

- Symeon card `uncertain` 2 calls the Philokalia passage "Symeon's own telling". The passage reports his words in the third person ("Ἔλεγε ... φησί"), and the words inside it are his first person; "own telling" is fair.
- The Elipandus Agobard sentence (26 words) and the Niketas Humbert sentence (26) sit at the ~25 mark, as batch 5's 26-word sentences did.
- Pisentius `"this fifth year",` puts the comma outside the quotation mark, where the same brief puts commas inside. It keeps the quoted words exact; spoken audio is unaffected.
- "Egbert, an English monk who had lived in Ireland with Chad in their youth" holds: Bede says they led a monastic life together "when both were youths, in Ireland" (GILES l.9128-9131).
- The Niketas card's Martène sentence: "dates him" follows "that writer", and Martène dates the writer, not Niketas (WILL l.24283-24286, 24303-24304).
- The Symeon `keyWorks` 2 list of three witnesses names three real, held sources; it is an enumeration, not a rhetorical triad.

---

## 5. Verdicts

| Profile | R1 findings | New blocking | New minor | Verdict |
|---|---|---|---|---|
| Symeon the New Theologian | 13 of 13 resolved (A-B1 to A-B3, A-M1 to A-M6, A-M8 to A-M11; A-M7 withdrawn in R1) | 0 | 1 (R2-M1; card only) | NOT CLEAR until R2-M1 is applied |
| Niketas Stethatos | 10 of 11 resolved; A-M15 partly | 0 | 2 (R2-M2, R2-M3; card and records only) | NOT CLEAR until R2-M2 and R2-M3 are applied |
| Cedd and Chad | 4 of 5 resolved; A-M23's card fix wrong | 1 (R2-B1) | 1 (R2-M4) | NOT CLEAR |
| Elipandus of Toledo and Felix of Urgell | 16 of 16 resolved (B-M11 done, for the coordinator) | 0 | 0 | CLEAR, subject to the coordinator's length call |
| Paul the Deacon | 9 of 9 resolved | 0 | 1 (R2-M5) | NOT CLEAR until R2-M5 is applied |
| Paulus Emeritanus | 7 of 7 resolved | 0 | 0 | CLEAR |
| Pisentius of Coptos and John the Elder | 7 of 7 resolved | 0 | 1 (R2-M6) | NOT CLEAR until R2-M6 is applied; also subject to the length call |
| README.md | 5 of 5 resolved (A-M26, A-M27, B-B9, B-M32, B-M33) | 0 | 2 (R2-M7, R2-M8) | NOT CLEAR until R2-M7 and R2-M8 are applied |

**Totals.** R1 had 73 findings (14 blocking, 59 minor). 71 are resolved (B-M29 reworded soundly; B-M11 done and left to the coordinator), 1 is partly resolved (A-M15) and 1 is not (A-M23, whose card fix R1 supplied and which was taken as worded). The worker's length cuts in Niketas and Paul the Deacon are sound. Round 2 found 1 new blocking finding (R2-B1) and 8 new minor ones (R2-M1 to R2-M8). Five of the nine come from fix wordings R1 supplied. Every quotation in the briefs and cards still matches its vendored file, all seven briefs pass `grade_text` before and after the fixes, and every audio file equals its brief plus tags. Every brief fix must be carried into the audio.

Round 2 is the second of the three review rounds the cap allows on each profile. Cedd and Chad is not approved to proceed until R2-B1 is fixed and independently rechecked. The other fixes are small and named string by string, and a targeted round 3 on the changed strings should be enough.
