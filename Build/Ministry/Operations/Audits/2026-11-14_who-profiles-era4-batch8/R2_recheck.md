# R2 recheck: era 4 batch 8

Round 2, a targeted recheck by a fresh Opus agent that had not seen the drafting or the earlier rounds, at full effort. Because the briefs were tightened under Mark's length ruling, it rechecked all six briefs in full as well as every round 1 fix. Given as the reviewer wrote it.

## Era 4 Who batch 8, round 2 recheck

**Scope.** I rechecked all six profiles (eadburga-of-thanet, abbess-bugga, yahya-ibn-said-of-antioch, elias-of-nisibis, adam-jingjing, al-baladhuri): the brief, the card, the audio script and the records.json entry for each, plus the README. I edited no files.

**Method.**
- **Reading.** I read CLAUDE.md, Who_Profile_Pattern.md (the 14-point checklist and the outside-witness section), R1_review.md (parts A, B and C) and R1_changes.md. I used batch 6 R2_recheck.md as the format model.
- **Diffs.** I ran `git diff --word-diff 25e64e06 HEAD` on the batch. For al-Baladhuri I compared against his first commit, c10503d0.
- **Briefs.** I reread all six briefs in full, sentence by sentence. For each sentence I opened the cited lines and read them in context. That covered:
  - Kylie, the Bollandists (AASS3), PL96, PL103, Plummer, Duchesne and Migne's Alcuin.
  - Malech/Wylie, Yule/Cordier, Assemani's volume 3 part 2 (the Syriac lines, l.36628-36795) and Budge.
  - PO18 (the preface, and the Jerusalem story at l.50312-50530) and Macler (l.612-620, l.13205-13320).
  - Elias's Chronography (ELI l.86-125, 205-216, 8462-8474, 8564-8603, 8826-8860), Bar Hebraeus, Assemani's volume 3 part 1 (l.46180-46218), Mai (l.392-400, 7360-7520, 8405-8430, 16340-16365), Chabot's Synodicon (l.1728-1738) and Kugener (l.20043-20050).
  - Hitti (l.170-182, 620-680, 725-792, 900-930, 4440-4600, 4793, 7900-7945, 8126-8175).
- **Cards and records.** I checked every new or changed card string and records entry the same way.
- **Quotes.** I checked every quotation in the briefs and cards against its file by script, whitespace-, hyphen- and punctuation-tolerant. All match. The one exception is Bugga's closing line, which spans a page break and running head (BONI l.2451-2459), as the records note.
- **Scores.** I rescored the briefs with `engine.m1.gates.grade_text`, measured sentence lengths by script, and rescored every replacement wording below.
- **Audio.** Each script equals its brief with `[calmly] ` at the start and `[warmly] ` at the start of the last paragraph. There are only two tags per script.
- **Writing.** I found no "not X but Y" or "X, not Y" contrast, no "never" contrast, no rhetorical question, no aphorism and no colon-reveal in the narrator's prose. American spelling holds; "honoured" appears only inside a quotation.

---

### Round 1 findings

| R1 finding | Status | Note |
|---|---|---|
| A-B1 | RESOLVED | AASS3 l.126368-126371, vi Kal. Jan. The card dates, the "Her years" item and the records all give 27 December with the year garbled. |
| A-B2 | RESOLVED | BONI l.3133-3166. Brief: "would not urge it strongly … going seemed better … and Boniface agreed." |
| A-B3 | RESOLVED | Letter VIII is now used in the card title, the records and the Eadburga contested side. The OCR heading "14 VII" is noted. |
| A-B4 | RESOLVED | "Another letter". |
| A-B5 | PARTLY | Both sides are now named, but the Kircher half misreads Assemani, and "Adam" is ambiguous right after the deacon Adam. See R2-B1. |
| A-M1 | RESOLVED | BONI l.4482-4483. |
| A-M2 | RESOLVED | "at Wenlock" (BONI l.3441-3443). |
| A-M3 | RESOLVED | The card now says the note guesses the poem's subject and states the building as fact. |
| A-M4 | RESOLVED | Both thesis openers are gone. |
| A-M5 | RESOLVED | PL103 l.93285-93289 is in the records, the contested_claim, the card item and the sources. |
| A-M6 | RESOLVED | BONI l.795. |
| A-M7 | RESOLVED | "Her greeting names her". |
| A-M8 | RESOLVED | "Ethelbert the Second" in the brief, the card's place and traces[1]. "Had met Boniface there". |
| A-M9 | PARTLY | "They" is gone, but "He and his church" now follows "Lul, who followed Boniface at Mainz", so "He" can be heard as Lul. The card's remembered[2] still has "they". See R2-M2. |
| A-M10 | RESOLVED | The old-age paragraph comes before Ethelbert's, and no false sequence is left. |
| A-M11 | PARTLY | "Of Thanet" is rightly dropped, but the brief now leaves "Abbess Eadburga" with no identifier. See R2-M1. The card items are fixed. |
| A-M12 | RESOLVED | ALC l.115017-115023. |
| A-M13 | RESOLVED | The brief has "Kylie takes her for the same woman", and the card has its own item. |
| A-M14 | RESOLVED | YULE l.3000-3001. |
| A-M15 | RESOLVED | The I-sz' sentence is cut, and nothing is left dangling. |
| A-M16 | RESOLVED | "Held" is gone from the brief and the uncertain items. "Held in" stays in keyWorks, which is the convention on approved cards. |
| A-M17 | PARTLY | Kircher is placed (MAL l.14226-14228 supports "published … in Latin"). Chorepiscopus is glossed only through Kircher's two renderings. "Papas" is still unexplained. See R2-M4. |
| A-M18 | RESOLVED | |
| A-M19 | NOT RESOLVED (fix misreads its source) | Kircher's "Constituit tabulam hanc Papa" is the seventh item in Assemani's list of Kircher's errors. Using it as support for Adam inverts Assemani. See R2-B1. The "Malech's English" half is resolved. |
| A-M20 | RESOLVED | |
| A-M21 | RESOLVED | The punctuation now follows MAL l.13574-13575. |
| E-B1 | RESOLVED | ELI l.8465-8473, 8576-8583. |
| E-B2 | PARTLY | Mai's tract III is now used as Elias's own words. But the brief calls the inheritance rules "Elias's rules". In fact they are the catholicos Elias I's rules, which Elias of Nisibis gathered. The card says Ebedjesu "tells readers to follow his rulings". Both misread MAI l.7395-7412. See R2-B3. |
| E-M1 | PARTLY | Chabot and Macler are added, and the Library header is gone as a side. But "soon after" is now credited to Assemani, who says only "after". See R2-B4. |
| E-M2 | RESOLVED (card) | PO2 l.20047-20048. The brief gives only Brooks's date. See R2-M6. |
| E-M3 | RESOLVED | The witness is attached. Cutting the "void" sentence leaves nothing dangling. |
| E-M4 | RESOLVED | |
| E-M5 | RESOLVED | ELI l.1, 8830. |
| E-M6 | RESOLVED | |
| E-M7 | RESOLVED | The contested_claim is deleted and the card item reworded. |
| E-M8 | RESOLVED | |
| E-M9 | RESOLVED | |
| E-M10 | RESOLVED | ELI l.8473. |
| E-M11 | RESOLVED | |
| E-M12 | RESOLVED | |
| E-M13 | RESOLVED | MAL l.1133-1137. |
| Y-M1 | RESOLVED | "Basil II". A separate fault in the same sentence is R2-B2. |
| Y-M2 | RESOLVED | |
| Y-M3 | RESOLVED | PO18 l.44601-44604. |
| Y-M4 | PARTLY | Schlumberger is now placed, but "history of Byzantium in that age" has no antecedent for "that age". See R2-M5. |
| Y-M5 | RESOLVED | PO18 l.50321-50323, 50388-50395, 50446-50447. |
| Y-M6 | RESOLVED | |
| Y-M7 | RESOLVED | PO18 l.44790-44793. |
| R-M1 | RESOLVED | |
| R-M2 | RESOLVED | The README repeats the R2-B4 wording. |
| C-B1 | RESOLVED | BAL l.7926-7938. The Nubia material is gone from the brief, the card and the records. |
| C-M1 | RESOLVED | |
| C-M2 | RESOLVED | |
| C-M3 | RESOLVED | |
| C-M4 | PARTLY | The paragraph moved, but "Years later" now follows the who-line, which ends on his death in 892. See R2-M7. |
| C-M5 | RESOLVED | BAL l.729-747. |
| C-M6 | RESOLVED | The new sentence has an ambiguous "he". See R2-M9. |
| C-M7 | RESOLVED | |
| C-M8 | RESOLVED | BAL l.4534. "Christians" is supported by l.4793. |
| C-M9 | RESOLVED | BAL l.674, 742. |
| C-M10 | RESOLVED | The item is dropped. |
| C-M11 | RESOLVED | |
| C-M12 | RESOLVED | |
| C-M13 | RESOLVED | |
| C-M14 | RESOLVED | |

---

### New findings

**R2-B1 (adam-jingjing, brief para 9; card uncertain[3]; records contested_claim "Who set up the stone", Adam side: Kircher's error used as a witness, and "Adam" is ambiguous). Blocking.**
- **What the brief says.** "The stone names a second Adam, a deacon, son of the priest Jazedbuzid. In Assemani's reading of the Syriac, Jazedbuzid set the stone up. Cordier writes that Adam erected it, and Assemani says Kircher read it the same way."
- **What the source says.**
  - ASS2 l.36746-36747 opens a numbered list: "Kirkerius tam in Prodromo, quam in Sina illustrata, in hujus Jazedbuzidi dignitate, patre, patria, & gestis plurimum hallucinatur." (Kircher, in both his books, is badly mistaken about this Jazedbuzid's rank, father, homeland and deeds.)
  - The list runs Primo … Sexto, Septimo. The reading the brief uses is the seventh item, l.36777-36783: "Septimo, pro voce Syriaca … ipse ubique legit Papa, & hunc tabulam illam lapideam erexisse affirmat: Constituit tabulam hanc Papa."
  - Assemani reports this reading as one of Kircher's errors. He does not report it as a rival reading of the stone.
  - Kircher's own English, as Malech prints it, has Jazedbuzid set the tablet up (MAL l.14162-14165).
- **Why it misleads.**
  - The brief gives a listener two witnesses for Adam, where the evidence gives one, Cordier.
  - "Cordier writes that Adam erected it" comes straight after the deacon Adam is introduced, so it can be heard as the deacon. YULE l.3000 says "Adam (King-tsing)".
- **Fix, brief para 9** (365 words, FK 7.20, Flesch 67.71):
  > The stone names a second Adam, a deacon, son of the priest Jazedbuzid. In the Syriac, as Assemani reads it and as Malech gives Kircher's reading, Jazedbuzid set the stone up. Cordier writes that King-tsing erected it.
- **Fix, card uncertain[3]:** "Who set up the stone. The Syriac, in Assemani's Latin and in Kircher's reading in Malech, says the priest Jazedbuzid set it up. Cordier says King-tsing erected it. Assemani lists among Kircher's errors a reading in which the Papa set it up."
- **Fix, records:** take Kircher off the Adam side. Add a claim: "Kircher once read the Papa as setting up the tablet; Assemani lists this among Kircher's errors (ASS2 l.36746-36783)." Remove the Kircher sentence from the A-M19 line in R1_changes' reasoning if it is reused.

**R2-B2 (yahya-ibn-said-of-antioch, brief para 11 and card legacy.remembered[1]: a campaign told as the whole war). Blocking.**
- **What the brief says.** "Yet only lately, he writes, has Yahya's chronicle shown that the emperor Basil II's Bulgarian war lasted four whole years."
- **What the source says.**
  - Schlumberger, in Macler's note, speaks of "toute cette … campagne de Bulgarie qui … dura, nous le savons depuis peu, grâce à la Chronique de Yahia, quatre années entières" (MAC l.13276-13293).
  - He dates that campaign from "l'hiver de 990 à 991" to "les premiers mois de l'année 995" (MAC l.13306-13314).
  - Stepanos's chapter heading reads "Une expédition de l'empereur Vasil dans le pays des Bulgares" (MAC l.13211-13212).
- **Why it is wrong.** "The emperor Basil II's Bulgarian war" is heard as his whole Bulgarian war, which lasted decades. The source means one campaign.
- **Fix, brief:** "Yet only lately, he writes, has Yahya's chronicle shown that one campaign of the emperor Basil II in Bulgaria lasted four whole years." With the R2-M5 fix this comes to 370 words, FK 7.38, Flesch 67.12.
- **Fix, card remembered[1]:** "Schlumberger says that only lately, through Yahya's chronicle, has it been known that one campaign of the emperor Basil II in Bulgaria, from about 991 to 995, lasted four whole years."

**R2-B3 (elias-of-nisibis, brief para 9; card legacy.remembered[1] and keyWorks[2]: whose rules, and who told readers to follow them). Blocking.**
- **What the files say.**
  - Brief: "Ebedjesu of Soba, which is Nisibis, copied Elias's rules for dividing inheritances into a book of canons."
  - Card remembered[1]: "Ebedjesu of Soba calls him a most exact and sharp-minded man, and tells readers to follow his rulings on inheritance."
- **What the source says.**
  - MAI l.7395-7407: the patriarch Elias's treatise is the "lucidissimam lampadem". Then "adeo ut etiam religiosissimo Eliae Sobensi, viro … accuratissimo et acutissimo visum fuerit praecipere, ut, omissis ceteris … tractatibus, omnes … hanc unam sequerentur semitam". So it is Elias of Nisibis who tells readers to follow the patriarch's treatise alone.
  - MAI l.7409-7412: "definitiones illas describam, quas … Elias Sobensis … collegit ex opere … Eliae patriarchae". The rules are the patriarch's; Elias of Nisibis gathered them.
  - Elias's own words confirm it: "praedictum Eliae tractatum huic meae lucubrationi velut fundamentum subieci" (l.7506-7508), and "Collegi itaque canones decretorios" (l.8414-8415).
- **Why it is wrong.** The brief makes the rules Elias of Nisibis's own. The card turns Ebedjesu's report of Elias's advice into Ebedjesu's advice about Elias.
- **Fix, brief para 9:** use the sentences given with R2-B4 below.
- **Fix, card remembered[1]:** "Ebedjesu of Soba calls him a most exact and sharp-minded man, who told all lovers of truth to follow the catholicos Elias I's treatise on inheritance alone."
- **Fix, card keyWorks[2]:** "… Ebedjesu copied Elias's preface, and the rules on inheritance he gathered from the catholicos Elias I, into his collection of canons, held in Angelo Mai's Latin."
- **Fix, records:** in the MAI claim, add "(the definitions Elias of Soba collected from the patriarch Elias's work, l.7409-7412)".

**R2-B4 (elias-of-nisibis, brief para 9; card dates and uncertain[2]; records contested_claim "When he died"; README "Corrections": "soon after" credited to Assemani). Blocking.**
- **What the files say.** "Assemani and J.-B. Chabot take him to have died soon after." The card says "put his death soon after 1049". The records side reads "Soon after 1049: Assemani …".
- **What the source says.**
  - Assemani, ASS1 l.46200-46202: "Obiit … post eiusdem Eliae primi obitum, hoc est, post annum Graecorum 1360". That says after, with no "soon".
  - Mai's note, MAI l.7483, also says only "post obitum".
  - Only Chabot says "peu de temps après" (SYN l.1733-1734).
- **Why it matters.** The quantifier is stronger than the source. Assemani's "after 1049" does not conflict with Macler's "about 1056", so the contest as told is overstated.
- **Fix, brief para 9, with R2-B3** (368 words, FK 6.20, Flesch 71.91):
  > Elias gathered rules on inheritance from a work of the catholicos Elias I. Ebedjesu of Soba, which is Nisibis, copied them into his book of canons. In his preface, Elias prays for the soul of Elias I, who died in 1049. Assemani puts the metropolitan's death after that. J.-B. Chabot says he died soon after. Frédéric Macler puts his death at about 1056.
- **Fix, card dates:** "Joseph Assemani puts his death after 1049, J.-B. Chabot soon after it; Frédéric Macler gives about 1056."
- **Fix, card uncertain[2]:** "… Assemani puts his death after that, and Chabot soon after. Macler gives about 1056."
- **Fix, records sides:** "After 1049: Assemani, from the preface (ASS1 l.46200-46216; MAI l.7454-7458, 7483)"; "Soon after 1049: Chabot (SYN l.1733-1735)"; "About 1056: Macler (MAC l.617-618)".
- **Fix, README:** the same change in "Elias's death year".

**R2-M1 (abbess-bugga, brief para 11: a common name with no identifier; checklist 8).**
- **Problem.** "report a belief that Bugga was Abbess Eadburga under another name". Several Eadburgas are in the Library (the README's names list). With "of Thanet" rightly dropped, this one is not placed.
- **Source.** AASS3 l.126350-126371: the Bollandists' Eadburga is the one Boniface wrote to about the vision.
- **Fix:** "… report a belief that Bugga was another name of Abbess Eadburga, to whom Boniface wrote about a vision." This comes to 372 words. If room allows, keep "They give her the same death day." (378 words). Otherwise leave the day to the card's uncertain[2], which carries it.

**R2-M2 (abbess-bugga, brief para 11 and card legacy.remembered[2]: who kept the day).**
- **Brief.** "Bregwin … later wrote to Lul, who followed Boniface at Mainz. He and his church kept …" The nearest antecedents for "He" are Lul and Boniface.
- **Source.** PL96 l.69812 "celebramus" is Bregwin's "we".
- **Fix, brief:** "Bregwin and his church, he wrote, kept the burial day of an abbess named Bugga, 27 December."
- **Fix, card:** "… wrote to Lul at Mainz that his own church kept the burial day …"

**R2-M3 (eadburga-of-thanet, brief para 1: "he added").** In letter XIV the thanks for books and vestments comes before the request, not after it (BONI l.3914-3922). Fix: "She had often eased his distress already, he said, with gifts of books and vestments." The word count stays at 350.

**R2-M4 (adam-jingjing, brief para 7: "papas" is left unexplained; checklist 4).** The A-M17 remainder. No source in the Library glosses it as "father". Assemani (ASS2 l.33004-33007) treats "Papas" as a title in these churches, from which the bishops' titles were formed. Either cut "and papas of China", since Yule's "Bishop and Pope" follows two sentences later, or write "and papas of China, a title these churches gave their clergy, Assemani says". This is optional if the coordinator judges Yule's "Pope" enough of a gloss.

**R2-M5 (yahya-ibn-said-of-antioch, brief para 11 and card remembered[0]: "in that age" has no antecedent).** The paragraph before ends on his birth and death. Fix: "Gustave Schlumberger's history of Byzantium in the tenth century". This follows PO18's own footnote on his "épopée byzantine à la fin du dixième siècle" (l.44383-44384), and adds no words.

**R2-M6 (elias-of-nisibis, brief para 3: only one side of a recorded contest).** The brief gives "E. W. Brooks … dates [it] to 1019" with Brooks named. The records carry "When he wrote the Chronography" as contested, against Kugener's 1008 (PO2 l.20047-20048). The claim is not told as settled, and the card gives both sides. If length allows, add "M.-A. Kugener dates it to 1008." Otherwise accept this as it stands.

**R2-M7 (al-baladhuri, brief para 5: "Years later" now follows his death in 892).** This came from the C-M4 move: the paragraph now opens straight after the who-line. BAL l.8146-8148 reads "When 'Umar ibn-'Abd-al-'Aziz became caliph, the Christians complained …". Fix: "When 'Umar ibn 'Abd al-'Aziz became caliph, the Christians complained, and he ordered the part taken from their church returned. The Muslims of the city objected."

**R2-M8 (al-baladhuri, brief para 3: "his life" and then "He was", right after Hitti).** "Philip Hitti … draws his life from al-Fihrist … He was Ahmad ibn Yahya …". Both pronouns can be heard as Hitti. BAL l.736 reads "From these sources we learn that …". Fix: "… draws on al-Fihrist and the lives by Yakut and al-Kutubi. From these, he writes, al-Baladhuri was Ahmad ibn Yahya ibn Jabir, a native of Baghdad of Persian descent."

**R2-M9 (al-baladhuri, brief para 9 and card uncertain[2]: "as he says himself").** This follows "He says al-Baladhuri tries …", where "He" is Hitti. BAL l.629-630: al-Baladhuri "himself acknowledges". Fix: "Sometimes, as al-Baladhuri says himself, he pieces reports together into one account."

With R2-M7 to R2-M9 applied, the al-Baladhuri brief comes to 368 words, FK 7.75, Flesch 65.55.

---

### Checks that pass, beyond the table
- **Bugga.** Paras 1 to 9 hold against BONI l.2432-2481, 2862-2950, 3118-3190, 5275-5290 and 6030-6066. "Heavier sorrows" is a fair telling of "more numerous and pressing sorrows".
- **Eadburga.** Paras 3 to 9 hold. Leoba's "four lines" are counted at BONI l.4555-4561.
- **Yahya.** The Jerusalem paragraph holds against PO18 l.50440-50510, and the plan, revisions and closing hold against l.44590-44806.
- **Elias.** Paras 1 to 7 and para 11 hold against ELI and BH3. "Our beloved brother" is at ELI l.8848.
- **al-Baladhuri.** The Damascus terms are "if he enters therein" (BAL l.7932-7938), which "promised" does not overstate. Najran, the 'Umar exchange, al-Ghutah, Gottheil, Yakut and al-Mas'udi all match.
- **Other new witnesses.** PL103 (l.93285-93289), Macler (l.617-618), Kugener, Chabot's Synodicon, Hitti l.7926-7938 and Mai's codex note (l.16354-16360) are read correctly in the records and cards. The exception is the two Mai and Assemani points above (R2-B3, R2-B4).
- **Pronouns.** I found no other pronoun whose antecedent shifted in the tightening, no story cut off and no turning point dropped.

### Scores

Current files, then the same briefs with the fixes above applied.

| Brief | Words | FK | Flesch | Longest sentence | After fixes: words / FK / Flesch | Blocking | Minor |
|---|---|---|---|---|---|---|---|
| eadburga-of-thanet | 350 | 6.46 | 71.64 | 25 (closing quotation) | 350 / 6.43 / 71.89 | 0 | 1 |
| abbess-bugga | 368 | 8.22 | 63.15 | 24 | 372 / 8.35 / 62.53 | 0 | 2 |
| yahya-ibn-said-of-antioch | 366 | 7.28 | 67.53 | 25 | 370 / 7.38 / 67.12 | 1 | 1 |
| elias-of-nisibis | 365 | 6.20 | 72.47 | 24 | 368 / 6.20 / 71.91 | 2 | 1 |
| adam-jingjing | 367 | 7.26 | 67.32 | 24 | 365 / 7.20 / 67.71 | 1 | 1 |
| al-baladhuri | 363 | 7.66 | 66.72 | 23 | 368 / 7.75 / 65.55 | 0 | 3 |

Every brief passes `grade_text` before and after the fixes. No card sentence is over 25 words. After any edit, the audio scripts must be rebuilt from the briefs.

### Count
- **Round 1 findings, 73 in all:**
  - Resolved: 62.
  - Partly resolved: 10 (A-B5, A-M9, A-M11, A-M17, E-B2, E-M1, E-M2 in the brief only, Y-M4, C-M4, C-M6 by a new ambiguity).
  - Not resolved: 1 (A-M19, whose fix misreads Assemani).
- **New blocking: 4.**
  - R2-B1: Adam, Kircher's error used as a witness.
  - R2-B2: Yahya, one campaign told as Basil II's whole Bulgarian war.
  - R2-B3: Elias, the inheritance rules and Ebedjesu's advice misread.
  - R2-B4: Elias, "soon after" credited to Assemani.
- **New minor: 9.** R2-M1 to R2-M9.

**Files reviewed** (under /home/user/CIC-Project/Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era4/batch8/):
- the six `<id>.brief.txt` files
- the six `<id>.card.json` files
- the six scripts in `audio/<id>.audio.txt`
- records.json
- README.md

The round 1 files are /home/user/CIC-Project/Build/Ministry/Operations/Audits/2026-11-14_who-profiles-era4-batch8/R1_review.md and R1_changes.md.
