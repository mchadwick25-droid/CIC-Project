# Round-2 targeted recheck, set 2 (Bede, Constantine, Grotius)

Reviewer: Opus, independent. This is a targeted recheck. It covers the round-1 findings (review/R1_set2.md), every new or changed claim in each brief, and every claim on each card.
Method: cited lines read with sed -n or grep -n. Quotes checked with a whitespace-normalized exact-substring test (XML tags stripped). Files are under /home/user/CIC-Project/cic/texts/.
Abbreviations: BH = bede_ecclesiastical-history-english-people_giles1903.txt; RB = roman-breviary_bute1908.txt; RM = roman-missal_england1843.txt; AL = alcuin_opera-omnia-letters_migne-pl100-101_1863.txt; LO = apology-for-lollard-doctrines_todd1842.txt; E = npnf201_eusebius-church-history-life-of-constantine.xml; S = npnf202_socrates-sozomen-ecclesiastical-histories.xml; L = anf07_lactantius-apostolic-constitutions-didache-liturgies.xml; Z = zachariah-rhetor_chronicle_hamiltonbrooks1899.txt; G = grotius_defence-of-the-catholic-faith-satisfaction-of-christ_foster1889.txt; C = calder_memoirs-of-simon-episcopius_1838.txt; D = synod-of-dort_articles-with-history-of-events_scott1831.txt; BX = baxter_reliquiae-baxterianae_sylvester1696.txt.

Every replacement brief below was scored with score.py. The drafted versions sit in the reviewer's scratch folder at /tmp/claude-0/-home-user-CIC-Project/6d98dab9-13d8-521f-bb4d-c1b444ee38ce/scratchpad/r2check/ (bede.txt, con.txt, gro.txt). Nothing in C/ was edited.

---

## Bede of Jarrow — REVISE

Score as drafted: words 278, FK 8.6, FRE 68.6, in band.
Quotes: "I always took delight in learning, teaching, and writing." MATCH (BH:15428-15429). "lest, when I come to the gates of the kingdom of heaven, there should be none to open them" MATCH (BH:8204-8206).

Round-1 findings:
- R1-1 (Ceolwulph): resolved (BH:117-121).
- R1-2 (impartial historian): resolved (BH:6985-6991).
- R1-3 (Easter quarrel explained): resolved. Colman and John (BH:7984-7993), Wilfrid for Rome and Peter (BH:8003-8010), Hilda for the Scots (BH:7966-7967), the keys question and "We do" (BH:8195-8203), Colman back to Scotland (BH:8232) all check out. "Whitby" is supported by the running head "SYNOD OF WHITBY" (BH:8013) and BH:10952.
- R1-4 (ending): partly resolved. The death is now told as two plain facts, which suits a single unsigned notice that is not disputed (BH:15610-15617). But the new legacy ending brings in a new fidelity fault (finding 1), and the card handles the death badly (finding 4).

1. BLOCKING — the closing sentence misreports the Missal prayer and blurs two calendars. The brief says: "its Missal prays that God enlightened his church through the learning of blessed Bede." The collect (RM:34727-34731) reads: "O God, who hast enlightened thy church by the learning of blessed Bede, thy Confessor and Doctor, mercifully grant that we thy servants may be always enlightened by his wisdom, and assisted by his merits." The enlightening is named as something God has already done. What the prayer asks for is that the faithful be enlightened by Bede's wisdom. The brief turns the address into the petition. There is a second problem. "Rome keeps Bede's feast on the twenty-seventh of May, and its Missal..." ties the Missal to the 27 May feast (RB:1935). This Missal is an English translation for the laity (RM:1-4), and it sets Bede's Mass on 29 October, among English saints such as Paulinus, Wilfrid and John of Beverley (RM:5300-5320, 34723). The ending is also still a bare notice. Two real later witnesses are in the Library and missing. About the year 800 (AL:9436-9442, "Anno 800", sending the books against Felix to Charlemagne), Alcuin twice cites "beatus Beda presbyter" on Acts in his books against Felix (AL:12017-12018, Acts 10; AL:13850-13852, Acts 20; also on the Song of Songs, AL:10320). The entry's own legacy field also wanted the Lollard tract. The notes say it was not found, but it is at LO:4924 and LO:6031 (see finding 3).
   Replacement for the last paragraph:
   "About the year 800, Alcuin, writing against the bishop Felix, turned twice to blessed Bede the priest for his reading of the Acts of the Apostles. Rome came to keep his feast on the twenty-seventh of May. A Roman Missal printed in English in 1843 prays to God, who enlightened his church "by the learning of blessed Bede," that his servants may always be enlightened by his wisdom."
   The quoted words "by the learning of blessed Bede" sit whole on RM:34728 (MATCH). Do not quote "enlightened thy church", because the file hyphenates it across a line ("en-/lightened"). Optional trim for length: "...naming his helpers; one of them searched the archives in Rome for letters of Pope Gregory." Whole brief with both changes: words 317, FK 8.6, FRE 68.4, no failures. That is long against the 200–270 guide. The cut can go elsewhere, but the legacy beat should stay.

2. BLOCKING (minor) — card key_works, "On the Times": "where he argues against the Irish Easter." The file says only that in De Temporibus he "most manifestly proved" Aidan's Easter wrong (BH:6985-6989). "Irish" is a gloss from memory, and elsewhere the file and card say "Scots". Replacement "about": "his book on reckoning time, where, he says, he proved Aidan's way of keeping Easter wrong".

3. STANDARD — the card's legacy_traces hold no legacy. Item 1 is the aftermath of Whitby (Colman, Tuda, Eata, Cedd; BH:8230-8268). Item 2 is Bede's own list of his books (BH:15433-15545). Neither shows anyone taking up his work. Item 1 also says "Roman Easter" where the file says "Catholic Easter" (BH:8230-8236). Replacement:
   - "About the year 800, Alcuin, in the books against Felix of Urgel that he sent to Charlemagne, cites blessed Bede the priest on the Acts of the Apostles and on the Song of Songs."
   - "Much later an English Lollard tract still leans on Bede: the signs of miracles, it says with him and with Gregory, were needed only at the church's beginning, as we water plants until they have taken root and then stop."
   Sources: AL:9436-9442, 10319-10321, 12017-12018, 13850-13852; LO:6031-6034 ("þus seiþ Bede, and rehersiþ Gregor... as we watteren plantis til þey han ben rotid"). Add both to written_about: Alcuin, "Books against Felix" (Latin, date "about 800", AL); and "An Apology for Lollard Doctrines" (author: anonymous Lollard writer, Middle English, date null, LO).

4. STANDARD — the card's legacy_remembered and uncertain go against Mark's card rulings and the witness rule.
   (a) legacy_remembered item 1 repeats the Missal misreport. Replacement: "Rome honors him. Its Breviary keeps Bede the Venerable on the twenty-seventh of May as Confessor and Doctor of the Church, and an English Roman Missal of 1843 calls on God, who enlightened his church by the learning of blessed Bede."
   (b) legacy_remembered item 2 is not how any tradition remembers Bede. It is Bede's own bias, and "only as opponents" overstates one passage, which says "for the most part" (BH:15174-15178). Remove it here; the uncertain line below carries it.
   (c) uncertain item 1 copies the brief word for word. Mark ruled that the card repeats the caveat in its own words and then adds detail. Replacement: "Bede means to be fair but does not hide his side. He praises Aidan's peace, humility and care for the poor while rejecting his Easter, and even defends him: Aidan kept it on the Lord's day, for faith in the resurrection, not on the fourteenth moon like the Jews, as some falsely imagine. Of the Britons he writes that most of them, through innate hatred, oppose the English and the appointed Easter." (BH:6985-7029, 15174-15178.)
   (d) uncertain item 2 names "the Giles edition" and says "the pupil's own account is not in the edition." That is talk about the edition and the Library, an editor standing in as the witness, and a caveat the brief does not carry. Replacement: "Bede's own account of his life stops in his fifty-ninth year, while he was still at work. The story of his last hours was written by his pupil Cuthbert." (BH:15432-15434, 15612-15614.)
   In written_about, "unsigned editor" may stay as a source entry. It is a source listing, not a witness.

---

## Constantine the Great — REVISE

Score as drafted: words 292, FK 8.1, FRE 67.5, in band.
Quotes: the baptism sentence MATCH (E:67792-67794). "Conquer by this" MATCH (E:61205). "your fellow-servant" MATCH (E:64593-64594). "of the same essence," MATCH (S:2951-2952, curly quotes in the file).

Round-1 findings:
- R1-1 (shields): resolved. Shields are Lactantius's only (L:10620); the prayer and the vision on the march are Eusebius's (E:61185-61207, 61274-61277).
- R1-2 (typo, notes): resolved.
- R1-3 (battle, edict): resolved (L:10622-10628, L:10684-10690).
- R1-4 (Arius; one Eusebius): resolved (S:2060-2095). The homoousios gloss is new and slips (finding 3).
- R1-5 (Crispus placement; Jordan): resolved as asked. See finding 4 on whether Crispus belongs in the audio at all.

1. BLOCKING — a contested point is told as settled on the card, and the card leaves out the dispute the Library holds. Card known_for: "...and was baptized near his death." The Syriac chronicle under Zachariah's name says that "Eusebius has failed to give an accurate account and Socrates has missed the truth (for the king was not baptized at the end of his life, as he wrote, since the story of his conversion by Silvester is also preserved in writing and in pictures at Rome...)" (Z:950-976). The census lists this as the disputed point (entries.json, sourcing). The notes say the chronicle was "not in the files I used; dropped", but it is vendored. The brief keeps "Eusebius says", which is acceptable for the audio. The card states it as fact and has no uncertain line on it.
   - known_for replacement: "Roman emperor who, with Licinius, gave Christians freedom of worship, and who called the bishops to the council at Nicaea."
   - uncertain item 2 replacement: "Not everyone accepted Eusebius's account of the baptism. A Syriac chronicle that goes under Zachariah's name says Eusebius got it wrong: the emperor was not baptized at the end of his life, it says, since the story of his conversion by Silvester is kept in writing and in pictures at Rome. Pagans told yet another story, that he turned Christian to be cleansed after the killing of his son Crispus, and Sozomen calls it an invention." (Z:950-976; S:26628-26651.)
   - Add to written_about: {"title": "The Syriac Chronicle known as that of Zachariah of Mitylene", "author": "compiler writing under Zachariah's name", "date": null, "language": "English translation", "file": "cic/texts/zachariah-rhetor_chronicle_hamiltonbrooks1899.txt"}.

2. BLOCKING (minor) — "He put off baptism until he was dying, Eusebius says, hoping for the Jordan." Eusebius does not say Constantine put it off. "Postponement" comes from the bracketed editor's note (E:67762-67764, "[These words seem to prove... His postponement of baptism...—Bag.]"). What Eusebius gives is that, convinced his life was ending, he sought purification (E:67748-67752), and Constantine's own words, "long hoped for" and "I had thought to do this in the waters of the river Jordan" (E:67792-67796). Replacement: "Only when he knew he was dying, Eusebius says, did he seek baptism. He had hoped to receive it in the Jordan."

3. STANDARD (precision) — "and explained it as no division in God." The emperor explained that "the Son did not subsist from the Father either by division or abscission" (S:3052-3056). "No division in God" can be heard as denying any distinction between Father and Son, which is the opposite error. This is the "don't trade the idea for a simpler one" rule. Replacement: "and explained that the Son did not come from the Father by any dividing or cutting off."

4. STANDARD — the brief still has no "what remained" beat. It ends at the baptism, and the coordinator's shape asks major figures for a concrete legacy. The Library carries one plainly: his burial in the Church of the Apostles, where "it became the custom to deposit the remains of subsequent Christian emperors... and here bishops, likewise, were buried" (S:30690-30700). Make room by cutting the pagan Crispus story from the audio. It is the weakly attested vivid story the guidance sends to the card, and replacement 1 puts it there.
   Replacement for paragraph 2: "Maxentius was driven into the Tiber at the broken bridge, Lactantius says. Soon Constantine and Licinius met at Milan and decreed that Christians and all others should be free to follow the religion each thought best, and that the churches' meeting places be given back." (L:10622-10628, 10684-10720.)
   Replacement for paragraph 4: "Only when he knew he was dying, Eusebius says, did he seek baptism. He had hoped to receive it in the Jordan. Near Nicomedia he told the bishops, "The time is arrived which I have long hoped for, with an earnest desire and prayer that I might obtain the salvation of God." His body was carried to Constantinople and laid in the Church of the Apostles. Sozomen says later Christian emperors were buried there too, and bishops as well."
   Also split the colon sentence in paragraph 1: "...years later and under oath. At midday a cross of light..."
   Whole brief with findings 2–4: words 316, FK 8.6, FRE 66.5, no failures. A first try without the split scored FK 10.2, so keep the split.

5. STANDARD — card uncertain item 1 copies the brief nearly word for word and adds nothing, against Mark's ruling. Replacement: "The two early tellings of the sign do not agree: Eusebius has a cross of light in the sky and then a dream, Lactantius a dream alone. Eusebius adds that at dawn Constantine called in workers in gold and precious stones to make the sign as a standard, and that he saw it with his own eyes." (E:61280-61290.)

The rest of the card checks out: the letter to Alexander and Arius (E:63875, 63903, 63932); one day for Easter (E:64607-64609); the five who refused (S:2945-2955); "having regard to peace" (S:3104); the fifty copies (E:5587-5592); "first of all sovereigns... regenerated... in a church dedicated to the martyrs" (E:67823-67826); Sozomen's verdict (S:30668); the Jews line (E:64620). The Helenopolis line reads "received the imposition of hands with prayer" in the file (E:67762), which is fine.

---

## Hugo Grotius — REVISE

Score as drafted: words 241, FK 8.9, FRE 61.8, in band.
Quote: "that sin should not be thought of less importance, if so many great sins should be remitted without an example." MATCH (G:6853-6855; an OCR mark "_" before "that" is not text). The clause sits outside the Aelianus quotation marks (G:6851-6853), so it is Grotius's own.

Round-1 findings:
- R1-1 (witnesses misnamed): resolved. The king's words are given as Le Vassor's (C:6215-6238), and Cross's arrest date is gone.
- R1-2 ("him"): resolved.
- R1-3 (modern writers as story witnesses): resolved in the audio. Foster and Calder are gone. Mosheim stays, with his admission (D:4581-4583), as round 1 allowed. But Foster and Calder come back as witnesses on the card (finding 4).
- R1-4 (date without year): resolved, dropped.

1. BLOCKING — card uncertain item 2: "The name governmental theory for his view comes from Foster, the treatise's nineteenth-century translator, not from Grotius." The file shows this is false. Foster quotes Professor Crawford, 1874, already "commenting upon the governmental theory of the Atonement" (G:14063-14066), so the name came before Foster's 1889 work. The true part is that Grotius's own chapters (G:2471-12478) never use the word. Replacement: "Grotius himself never calls his view the governmental theory. The name came later, and he speaks instead of God acting as ruler."

2. BLOCKING (minor, misleading) — card legacy_remembered item 2: "Richard Baxter... published The Grotian Religion Discovered, at the invitation of Thomas Pierce, who was defending Grotius." Baxter's "at the Invitation of Mr. Thomas Pierce" is wry. He wrote it "in answer to" Pierce, whose "principal business was to defend Grotius" (BX:10548-10552). The card makes it sound as if Pierce asked for the book. Replacement: "Richard Baxter wrote against him in The Grotian Religion Discovered, in answer to Thomas Pierce, whose chief aim was to defend Grotius."

3. STANDARD (ear) — "Remonstrants" is never explained, and "Then the Remonstrants fell" is abrupt: who fell, and how? The file gives both plainly. Grotius was "advocate-fiscal of Holland", and the quarrel was "upon the points of grace and predestination" (C:6216, 6222-6225). Prince Maurice's party "at length prevailed, and the men who sat at the helm of government, were cast into prison. Olden-Barneveldt, a man of wisdom and gravity, whose hairs were grown grey in the service of his country, lost his life on the public scaffold" (D:4574-4580).
   Replacement for the first two sentences: "Hugo Grotius, a lawyer in the service of Holland, was in England on business for the East India Company. The Remonstrants, the Arminian side in the Dutch quarrel over grace and predestination, chose him to plead their cause there."
   Replacement for paragraph 3: "Then Prince Maurice's party won the struggle for power, and the men who had led the government were thrown into prison. Barneveldt, grown grey in his country's service, died on the scaffold, and Grotius was condemned to prison for life, though Mosheim says he does not know on what charge. Grotius escaped when his wife sent him out in a chest that usually carried books."
   Whole brief with both changes: words 284, FK 9.4, FRE 60.9, no failures. FRE is near the floor, so do not lengthen further.

4. STANDARD — modern writers are back as witnesses on the card, and uncertain does not follow Mark's ruling.
   (a) uncertain item 1 names Calder ("Calder, who writes for the Remonstrants, says... a story he calls too well known to repeat") for a story the brief tells plainly and nobody disputes. Calder is no witness to it, as round 1 already found. Replacement, in its own words with added detail: "Why Grotius was condemned is not clear. Mosheim, who tells of the sentence, says the pretext and the charges are unknown to him. Hoogerbeets, the pensionary of Leyden, was imprisoned with him." (D:4581-4583; C:9831.)
   (b) legacy_traces item 3: "Foster thinks Jonathan Edwards read Grotius..." Foster is the witness here. Also, the Edwards meant is the one at New Haven, "the chief formulator of the doctrine... during his settlement in New Haven" (G:1954-1964). A listener will hear the elder Edwards of Northampton. "Tillotson led a school" overstates "stands first in ecclesiastical rank among this school" (G:1285). Replacement: "In England, Archbishop Tillotson stood first among the Arminians who largely took up his theory. In New England, Jonathan Edwards, then a pastor at New Haven, may have read him, since Grotius's example of Zaleucus turns up in Edwards's third sermon on the atonement, and Samuel Hopkins took up the governmental idea completely." (G:1281-1285, 1954-1966, 2017-2021; Zaleucus in Grotius at G:6377-6432.)
   (c) legacy_remembered item 3: "In Holland, Foster writes, Grotius fell under the ban..." Replacement, told directly: "In Holland, once the Arminians were condemned at Dort, he shared the ban laid on them, and even as a commentator he was often met with prejudice and hostility." (G:754-760.)

The key-work titles are fair, and no card note is needed. "On the Truth of the Christian Religion" is near Burnet's own 1692 English, "his Book of the truth of the Christian Religion" (burnet_discourse-of-the-pastoral-care_1692.txt:7262-7264). "On the Law of War and Peace" is a literal rendering of "De Jure Belli et Pacis" (baxter_autobiography...lloyd-thomas1925.txt:16330, OCR "Juve"), and Foster confirms the subject, "his work upon international law" (G:1270-1272). The notes should keep saying where the Latin title comes from. Other card claims check out: ten chapters and Leyden 1617 (G:364, header); Heidegger and Turretin (G:790-860); Limborch's "the supreme Lord may remit of his own right when he chooses" (G:1145-1146). One soft spot: the plainest "God may forgive without satisfaction" is Curcellaeus, following Episcopius (G:1052-1060). The Episcopius and Limborch line is defensible, but "Curcellaeus and Limborch" would be more exact.

---

## Verdicts
- Bede of Jarrow: REVISE. 2 blocking (1 a misreported liturgical prayer, 1 minor), 2 standard. All round-1 findings resolved except the ending.
- Constantine the Great: REVISE. 2 blocking (1 a contested baptism told as settled on the card, 1 minor), 3 standard. All round-1 findings resolved.
- Hugo Grotius: REVISE. 2 blocking (1 a false claim on the card about where the "governmental theory" name came from, 1 a misleading reading of Baxter), 2 standard. All round-1 findings resolved in the audio.
All quotations MATCH. All three drafts and all three replacement briefs score in band.
Note for the coordinator (not a finding): all three cards give key_works as {title, about} objects, while REVISE.md's schema shows plain strings. They are at least consistent with each other; build_page.py should accept whichever is meant.
