# R1 review: era 4 batch 6

Round 1, the full checklist review, by two fresh Opus agents that had not seen the drafting, at full effort. Part A covers Agathon, John III, Isaac and Simon I. Part B covers Alexander II, Michael I, Joseph I, Severus ibn al-Muqaffa and the README. Each part is given as its reviewer wrote it.

## Era 4 Who batch 6, round 1 review: PART A

**Scope.** agathon-of-alexandria, john-iii-of-samannud, isaac-of-alexandria, simon-i-of-alexandria: brief, card, audio script, and records.json entries.

**Method.** I read CLAUDE.md, Who_Profile_Pattern.md (14-point checklist), the batch README, and the approved Benjamin I brief and card for calibration. I re-read every quotation against its vendored file. I opened the cited lines for each brief sentence and card string and read them in context. I diffed each audio script against its brief and checked tag placement. I ran grade_text on each brief and checked sentence lengths by script. I searched for missed witnesses in Michael the Syrian, Abu Salih, Assemani, John of Nikiu (Charles) and Renaudot.

**Files opened (cic/texts/).** PO5 = chronicle-of-seert_..._scher-dib1910.txt (Evetts's History, l.330-2540, 4495-4540). SEV = severus-al-muqaffa_..._evetts1904.txt (l.137-170, 45520-45715, 45955-46150). REN = renaudot_..._1713.txt (l.986, 11515-11565, 11950-12200, 12458-12782, 13760-13772, 18600-18612). BAS1 = synaxaire-arabe-jacobite_po1-... (l.19345-19415). PO11 = synaxaire-arabe-jacobite_po11-... (Porcher's Mina, l.21200-21566, 22985-23200, 23905-23966, 24072-24132, 25600-26035). PO17 = john-ephesus_lives-eastern-saints-po17_brooks1923.txt (Basset 24 Abib, l.58400-58505). BUD1 = ethiopian-synaxarium_...-v1-... (l.13525-13580, 16476-16545). BUD2 = ...-v2-takhshash-yakatit_... (l.1262-1295). BUDM = ...-v2-v4-microform_... (l.42745-42825). ABU = abu-salih_... (l.8285-8420, 10736-10760, 11270-11375). JN = john-nikiu_chronicle_charles1916.txt (l.175-186). MS2 = michael-the-syrian_chronique-tome2-... (l.34605-34615, 36335-36352, 36640-36655).

**Quotations.** Every quotation in the four briefs and cards matches its file word for word, allowing for OCR noise. The OCR differences: SEV l.46143 "I he sinner Agatbon" (page break after "as for me,"). PO5 l.1011-1017 "tliings tliat", "wliat I can- not pcrform". PO5 l.928-929 "Ghrist". PO5 l.959 "tliey". PO5 l.1592 "Danicl". PO5 l.1597 "coun'ry". PO5 l.2120-2121 "no other- wise". The one problem with quotation marks is Isaac's "Maurotania" (A-M17).

**Audio.** All four scripts equal their brief once `[calmly] ` (line 1) and `[warmly] ` (start of the last paragraph) are removed. Tags appear nowhere else. Checklist item 13 passes for all four.

---

### agathon-of-alexandria

**Verdict: passes with minor fixes. No blocking finding.**

**A-M1 (brief, para 6: who "writes" the quote).** "Eusèbe Renaudot ... calls that account a fable under Agathon's name. Early in it he writes: ..." The nearest antecedent of "he" is Renaudot. Heard aloud, the quote briefly seems to be Renaudot's. That is a witness coming loose from its claim. Evidence: the words are Agathon's, SEV l.46143-46144. Fix: "Early in the account, Agathon writes: ..."

**A-M2 (brief, para 6: Renaudot not marked as partisan; checklist 6).** The brief calls Renaudot "a Catholic scholar" but does not say he writes against this church. The approved Benjamin I brief marks him ("calls their line heretical"). Evidence: REN l.18609 "ab Patriarchis hæreticis" (said of these patriarchs among others). REN l.11546-11563: he says the account was "a Coptitis recentioribus inventa" ("invented by later Copts") to give the new monastery standing. Fix (two sentences): "Eusèbe Renaudot was a Catholic who wrote a Latin history of these patriarchs in 1713. He calls their line heretical, and he calls that account a fable under Agathon's name." (REN l.986 "nos Catholici" supports "Catholic"; see A-M32.)

**A-M3 (brief, paras 4-5: "Chalcedonian" is never explained; checklist 4).** A general listener does not know the word. Benjamin's brief explains it. Evidence: PO5 l.346-347 calls the council "the impure Chalcedonian Council", so the History shows that Agathon's church refused it. Fix: after "Then a Chalcedonian named Theodore paid Yazid ...", add: "The Chalcedonians held to the council of Chalcedon, which Agathon's church refused."

**A-M4 (brief, para 4: Yazid with no context; checklist 4 and 8).** "paid Yazid, son of Muawiyah" does not say who Yazid is. Evidence: PO5 l.452-453 "went to Damascus to the leader of the Muslims, whose name was Yazid, son of Muawiyah". Fix: "paid Yazid, son of Muawiyah, the Muslim ruler at Damascus, for power over Alexandria and Mareotis."

**A-M5 (brief, para 1: "no one" for "the heretics").** "He passed for a carpenter, so that no one would stop him at their doors." The source names who might stop him. Evidence: SEV l.45705-45707 "that the heretics might not hinder him, and that so he might find a means of entering the houses". Fix: "He passed for a carpenter, so that his opponents would not stop him at the doors of the faithful." ("Opponents" keeps the History's point without taking over its word "heretics" in the narrator's voice.)

**A-M6 (brief, para 5: his years told from one side; checklist 7).** "after seventeen years, the History says." records.json has a contested_claim: seventeen (PO5 l.702; BAS1 l.19411), nineteen (BUD1 l.13575; REN l.12018-12019), sixteen (Makrizi in REN l.12021-12022). The witness is named and the card gives the other counts, so this is not told as settled. Still, the pattern tells disputes in place. Fix: "Agathon died on the 16th of the Coptic month Babah, after seventeen years, the History says. The Ethiopic Synaxarium gives nineteen."

**A-M7 (card, legacy.traces[0]: "Agathon would not make John a bishop").** The History does not say Agathon refused. Evidence: PO5 l.642-645 "some of the people prayed him to ordain John bishop over Upper Egypt, and others suggested some other see. But God was reserving him for his gentleness like David, that he might accomplish for him what had been promised in the vision." Fix: "A vision named John of Samannud to him as his successor, the History says. Some asked Agathon to make John a bishop of Upper Egypt, but God was keeping him for the throne."

**A-M8 (card, legacy.traces[1]: something that happened in his days, filed as a trace).** "In his days ... the church of Saint Macarius was built" sits under "What traces to them", which suggests he built it. Evidence: PO5 l.503 "In the days of Abba Agathon was built the church", with no agent named. Fix: move it to "uncertain", or reword: "The History dates the church of Saint Macarius to his days, without saying who built it. The brothers grew so many that they built cells near the Marsh."

**A-M9 (card, legacy.traces[2]: common name; checklist 8).** "He ordained Simon, the later patriarch, a priest". Fix: "He ordained Simon I of Alexandria, the later patriarch, a priest, says the History's life of Simon." (PO5 l.1548-1550; BAS1 has no Simon here, but PO17 l.58430ff "Anbä Agathon l'ordonna prêtre" agrees.)

**A-M10 (card, legacy.remembered[2]: whose face).** "A woodcutter struck a tree the patriarch stood under, and the axe flew back into his face." As written it can read as the patriarch's face. Evidence: ABU l.11312, 11334-11335 "the patriarch Agatho was standing under the tree, and when the woodcutter struck it with his axe, the axe flew back into his face. Thereupon the governor was afraid". Fix: "A woodcutter, sent by the governor, struck a tree the patriarch stood under. The axe flew back into the woodcutter's face." (ABU l.11311-11312: "The governor of the town ... wished to cut it down".)

**A-M11 (card, uncertain[5]: the captives hedged past what the line says).** "It is not clear whether it means the captives he freed." The line follows directly on the freeing. Evidence: PO5 l.411 "he bought them and set them free. But they", then l.441-442 "were followers of the impure and heretical sects, known as the Gaianites ... and as the Barsanuphians." Fix: "The captives. The History adds that those he freed were Gaianites and Barsanuphians, sects outside his church."

**Scores.** 348 words, about 2 minutes 10 seconds. FK 7.60, Flesch 66.28. Passes. Card sentences are all 25 words or fewer.

---

### john-iii-of-samannud

**Verdict: passes with minor fixes. No blocking finding.**

**A-M12 (brief, para 5: two answers merged into one).** "In Holy Week Samad kept lowering his price, to ten thousand in the end. 'The only things that I can dispose of are my garments which are upon my body,' John answered. 'I will not promise what I cannot perform.'" Both lines are set after the ten thousand. In the source the first answers fifty thousand and the second answers ten thousand. Evidence: PO5 l.1009-1016 "I will yield to thee fifty thousand denarii ... The saintly patriarch answered ... 'The only things that I can dispose of are my garments which are upon my body'. After that Samad did not cease to lower his demands until he reached ten thousand denarii. So the patriarch said to him: 'I will not promise what I cannot perform'." Fix: "Samad came down to fifty thousand. 'The only things that I can dispose of are my garments which are upon my body,' John answered. Samad kept lowering his price, to ten thousand in the end. 'I will not promise what I cannot perform,' John said."

**A-M13 (brief, para 4: break in time and an unsupported "soon").** The Theodore paragraph comes between the two halves of the Holy Week story and goes back in time, which breaks the story's flow (checklist 10). "Soon" is also not in the History. Evidence: PO5 l.717-726 "But at last the Lord took vengeance on Theodore ... Thus he died an evil death. And his son was appointed governor". This falls at the start of John's time, before Abd al-Aziz came. Renaudot has "paulo post" (REN l.12084), but the brief credits the History. Fix: move the paragraph so it comes before the Holy Week story, after para 3. Reword: "Theodore, the Chalcedonian governor of Alexandria who had harassed Agathon, died of dropsy, the History says. His son became governor and was like a son to John." "Chalcedonian" is still unexplained. Add: "The Chalcedonians held to the council of Chalcedon, which John's church refused." (PO5 l.346-347.)

**A-M14 (card, uncertain[3]: "Theodore's son" with no context; checklist 4).** The card never introduces Theodore. Fix: "Theodore's son. The History says the son of Theodore, the Chalcedonian governor of Alexandria, followed him and loved John like a son. Renaudot adds that he was a Jacobite, which Evetts's English does not say." (PO5 l.718-721; REN l.12086-12087 "diversæ fidei, nam erat Jacobita".)

**A-M15 (card, uncertain[6]: what the bishops "said", and a common name).** "After his death some bishops said he had named the deacon George." The bishops planned to say this to the Amir if he objected. The History treats it as a pretext. Evidence: PO5 l.1318-1323 "they agreed that they should promote the deacon George, who was a native of Sakha ... without consulting the Amir Abd al-Aziz. For they said: 'If he is angry with us or murmurs, we will tell him that Abba John ... commanded us that this man should sit in his place'". Fix: "Whom he named. After his death some bishops chose George, a deacon of Sakha. They planned to tell the Amir that John had named him. The Amir found from the documents that he had named Isaac, the History says."

**A-M16 (card, uncertain[1]-[2]: one item split in two, and the second has no heading).** Item [2] ("Eusèbe Renaudot ... gives the answer as not even a hundred drachmas") continues item [1] ("The sum.") but stands alone with no heading, unlike every other item. Fix: merge them. "The sum. The History has the Amir demand a hundred thousand denarii. In B. Evetts's English, John answers that he has not a hundred thousand drachmae of it. Eusèbe Renaudot, a Catholic scholar writing in Latin in 1713, gives the answer as not even a hundred drachmas." (PO5 l.910-911, 924-925; REN l.12096-12097.)

**Who-line.** See A-M27.

**Scores.** 351 words, about 2 minutes 10 seconds. FK 5.99, Flesch 77.13. Passes. The one brief sentence over 25 words is the closing quote (26 words, mostly quotation). Card sentences are all 25 words or fewer.

---

### isaac-of-alexandria

**Verdict: two blocking findings (Porcher's view misstated; Nau's witnesses swapped). Otherwise minor.**

**A-B1 (brief, para 2, and card, uncertain[1]: Porcher's judgment overstated, with an "X, not Y" contrast).** Brief: "Mina's editor, E. Porcher, says the Life was written to edify, not as history." Card: "E. Porcher ... says it was written to edify, not as history." Porcher says something narrower. The Life is not a historical work as people understand one today, and its author's aim was to edify. In the same notice he offers it to readers so they can check the History's facts against it. Evidence: PO11 l.21232-21236 "Il ne faut pas chercher dans cette Vie une œuvre historique, telle qu'on la conçoit de nos jours. Le but de l'auteur est l'édification des lecteurs, ou des auditeurs, qui étaient bien loin de nos préoccupations scientifiques modernes". PO11 l.21203-21205: "documents coptes parallèles, qui leur permettront d'en contrôler les données historiques". "Not as history" drops "as conceived today" and turns his qualified view into a flat one. That misstates a named witness. The sentence is also an "X, not Y" contrast (checklist 4) and leads with a role ("Mina's editor"). Fix, brief: "E. Porcher, who edited Mina's Life, says it was written to edify. It is not history as we would write it today, he says." Fix, card uncertain[1]: "E. Porcher, who edited Mina's Life, says its aim was to edify. It is not a work of history as history is written today, he says."

**A-B2 (card, uncertain[6]: Nau's reckoning credited to the wrong sources).** "F. Nau ... gives three and a half years from another source. From weekdays in Mina he reckons 684 to 687, and doubts those weekdays himself." Only one weekday is from Mina, the Sunday consecration (cited to the Life, "infra, p. [57]"). The Tuesday death is from Peter ibn Rahib. The three and a half years come from the Arabic Synaxarium (P.O. III, 268, which Porcher's notice identifies as the Synaxarium at 9 Hatour, l.21210-21211). Evidence: PO11 l.21278-21284 "ou trois ans et demi, P. O., III, 268. — Si Isaac a été ordonné un dimanche 8 Kihak ... infra, p. [57], ce ne peut être qu'en 68[OCR '68%'] ou 690. S'il est mort un mardi neuf Hatour (5 nov.), cf. Pierre ibn Rahib, loc. cit., ce ne peut être qu'en 687 ou 692 ; il aurait donc été patriarche de 684 à 687 ... mais les jours de la semaine sont-ils authentiques? — [F. N.]". Fix: "His years. F. Nau, in a note to Porcher's edition, cites three and a half years from the Arabic Synaxarium. He takes a Sunday consecration from Mina and a Tuesday death from Peter ibn Rahib, and reckons 684 to 687. He doubts those weekdays himself." Records: the Nau claim's witness string should add Peter ibn Rahib, as Nau cites him, and the Synaxarium as his source for three and a half years.

**A-M17 (brief, para 5: quotation marks round a form not in the file).** "Mina names the kings of Makuria and of 'Maurotania'." The held text is French, "le roi de Maurotanie" (PO11 l.25629, 25636). The README keeps quotation marks for held English, and "Maurotania" is an English form. Fix: "Mina names the kings of Makuria and of a land he calls Maurotania." (Same for the card's uncertain[4], which quotes "Maurotania".)

**A-M18 (brief, para 5: tense).** "He has the apostles Peter and Mark walk beside Isaac until the Amir was afraid." The tenses do not match, and "until" is not what Mina says: the king saw them and fear seized him. Evidence: PO11 l.25893-25900 "marchant avec lui, tout de lumière; il fut dans une grande stupeur, et la crainte le saisit"; l.26019-26021 the king: "J'ai vu deux hommes marchant avec toi". Mina calls Abd al-Aziz "le roi" (l.23915-23916, "Le nom de ce roi-là était Abd-el-Aziz, et on l'appelait encore l'Émir"), so "the Amir" is right. Fix: "In Mina, the apostles Peter and Mark walk beside Isaac, and the Amir sees them and is afraid."

**A-M19 (brief, para 3: Meneson left out; "eparch" not explained).** "trained as a secretary in the service of the eparch George." Isaac was placed with a kinsman who served George. Evetts does not put Isaac in George's service. Evidence: PO11 l.21560-21564 "le mirent entre les mains d'un de leurs parents, nommé Meneson, administrateur (chartularius) au service de Georges, qui était éparque au pays d'Égypte, afin que le jeune Isaac devînt secrétaire (notarius), auprès de lui." Fix: "Mina says Isaac was a clerk before he was a monk. His parents placed him with a kinsman, Meneson, who served George, the governor of Egypt, to train as a secretary." ("Éparque au pays d'Égypte" supports "governor of Egypt" and avoids the undefined term.)

**A-M20 (card, uncertain[2]: two witnesses merged).** "Porcher says he was a monk of Saint Macarius who became bishop of Pchati after John of Nikiu." "Pchati" comes from the manuscript title. Porcher says he succeeded John of Nikiu. Evidence: PO11 l.21246-21248 (Porcher: "Mina, lequel devint évêque comme lui, succédant à Jean de Nikiou"); l.21324-21327 (title: "Abba Mina, le très pieux évêque de la ville de Pchati"). Fix: "Who Mina was. The Life's title calls him bishop of Pchati. Porcher says he was a monk of Saint Macarius who followed John of Nikiu as bishop. Porcher gives no date for the Life."

**A-M21 (card: "Hatur" and "Athor" for one month; checklist 9).** The dates field has "the 2nd of the Coptic month Hatur, Mina on the 9th". legacy.remembered[0] has "the 9th of Athor". Fix in remembered[0]: "Mina's Life was read as a sermon on his feast, the 9th of Hatur. E. Porcher reports this from a note on its manuscript."

**A-M22 (missed witness, the scene's archbishop; optional card line).** The brief's "An archbishop" is honest to Mina. Budge's Ethiopic, however, tells the same scene and names him. Evidence: BUD1 l.16502-16512 "in those days Abba JOHN the archbishop was seeking for a learned man to be his disciple and his scribe ... ISAAC made mistakes in his writing wittingly". This changes no brief claim. If it is used, it goes in "uncertain": "The archbishop in the letter story. Mina does not name him. Budge's Ethiopic tells the same story of Abba John."

**Scores.** 346 words, about 2 minutes 10 seconds. FK 7.43, Flesch 67.43. Passes. Card sentences are all 25 words or fewer.

---

### simon-i-of-alexandria

**Verdict: passes with minor fixes. No blocking finding.**

**A-M23 (brief, para 1, and card, place: "near Alexandria" credited to the History).** "John, head of a monastery near Alexandria" sits in a paragraph credited to the History. The History names the monastery but does not place it. The synaxaria place it: PO17 l.58431-58432 "au couvent où se trouve le corps de saint Sévère, à l'ouest d'Alexandrie"; BUDM l.42751 "the monastery to the west of the city of Alexandria". The History has PO5 l.1472 "John, the Hegumen in the Monastery of Az-Zajaj, which is called in Greek To Enaton". "John" is also a common name (checklist 8). Fix, brief: "John, head of the monastery of Az-Zajaj, was handsome, and the Amir agreed to make him patriarch." Fix, card place: "Born in the East, the History says. Brought up at the monastery of Az-Zajaj, and buried there. The synaxaria place it west of Alexandria."

**A-M24 (brief, para 5: only the bishop's hands and feet).** "the caliph Abd al-Malik had the new bishop's hands and feet cut off." Three men were maimed. Evidence: PO5 l.2020-2027 "ordained him bishop for him, and ordained two priests for him ... they brought the three others bound to Abd al-Malik ... he cut off their hands and feet". Fix: "the caliph Abd al-Malik had the hands and feet of the new bishop and his two priests cut off."

**A-M25 (brief, para 5: the night trial left with no outcome; checklist 10).** The brief ends the India story on Simon's answer, and the next paragraph is his last illness. The listener never learns that he was cleared. Evidence: PO5 l.2178-2192 (the Indian priest is found on the second day; "Abd al-Aziz performed for Abba Simon what he had promised, by sparing for his sake Theodore and the Indian priest; for he had learnt that there was no deceit" [in him]). Fix, after the quote: "Two days later the Indian priest was found, and the Amir saw that Simon had told the truth."

**A-M26 (brief, para 4: poisoning outcome and poisoners' fate told from the History alone; checklist 7).** Records hold contested_claims on both. Elmacinus has a fourth dose kill him (REN l.12476-12478 "quarto ... obiisse"). Budge and Renaudot have the priests exiled (BUDM l.42820-42821; REN l.12545-12546). The History is named for the episode, and the card gives the rest, so this is not told as settled. A short in-place clause is still owed. Fix, after "and the priests were set free": "The Ethiopic Synaxarium says they were sent into exile."

**A-M27 (who-line late, John III and Simon; checklist 10).** The pattern puts the who-line "within the first few sentences". In John III's brief it is sentence 8 (para 3). In Simon's it is sentence 10 (para 3), although para 2 gives "a Syrian, from the East". Both open on strong scenes, so this is a judgment call. Fix for Simon, at the start of para 2: "Simon I of Alexandria was a Syrian, from the East." Then drop "Simon I of Alexandria was patriarch from 689 to 701, in the heading of B. Evetts ..." down to "Evetts heads his life 689 to 701. He translated the History, a later Arabic history of the Coptic church."

**A-M28 (brief, para 3: "a later life" is vague).** "John the deacon, who wrote a later life in the History". Fix: "John the deacon, who wrote the History's life of Michael I, says Simon's archdeacon George wrote the history of these years." (PO5 l.4501-4506.)

**A-M29 (card, uncertain[4]: a missed witness on the cups).** "The History has his cup poisoned twice before the figs. Basset's synaxarium and Budge's Ethiopic have three times." Renaudot's retelling of the History also has three. Evetts's English has two, so manuscripts of the History differ. Evidence: REN l.12467-12470 "nihil mali passus est, etiamsi iterum & tertio infusum illi eodem modo venenum fuisset", with "Ita rem Severus narrat" at l.12475-12476. Fix: "The cups. B. Evetts's English of the History has his cup poisoned twice before the figs. Renaudot's reading of the History, Basset's synaxarium and Budge's Ethiopic have three times."

**A-M30 (card, legacy.remembered[0]-[1]: "sorcerers", and a line that says nothing).** remembered[0] says "the sorcerers burned". The History, Basset and the brief say magicians ("les magiciens", PO17; "magicians", PO5 l.1787-1799). remembered[1] says "Its account of the poisoning differs from the History's", which gives no content (checklist 4). Fix: "sorcerers" becomes "magicians". remembered[1]: "The Ethiopic Synaxarium, in E. A. Wallis Budge's English, keeps him on the 24th of Hamle. It has him sick for four days, and the priests sent into exile." (BUDM l.42791-42792, 42820-42821.)

**Scores.** 347 words, about 2 minutes 10 seconds. FK 6.07, Flesch 75.29. Passes. Card sentences are all 25 words or fewer.

---

### records.json (all four)

**A-M31 (confidence tag on Evetts's view).** Each profile's last claim, "from the seventh century its lives are, in B. Evetts's view, contemporary biographies", is tagged Widely Accepted. It is one scholar's judgment, held here only in his own notice (SEV l.150-156). By the pattern's Confidence section, that is Dominant Modern Reconstruction, which names who reconstructs it. Fix: retag as "Dominant Modern Reconstruction".

**A-M32 (no witness for "Catholic").** The Agathon, John III and Simon cards call Renaudot "a Catholic scholar", and the Agathon brief does too. No claim carries a witness for it. Evidence: REN l.986 "nos Catholici a majoribus tradita religiose observamus". Fix: add a claim, "Renaudot writes as a Catholic: 'nos Catholici'", witness REN l.986.

**A-M33 (variants not in contested_claims).** The cards list source disagreements that have no contested_claim behind them. Agathon: the fleet sum (7,000 denarii in PO5 l.493; 7,000 dinars a year in BAS1; 700 dinars in BUD1 l.13547-13548). Simon: the cups (two in PO5 l.1742-1746; three in REN, BAS, BUDM). John III: the drachmae answer (PO5 l.924-925; REN l.12096-12097). Fix: add a contested_claim for each, with the sides as given here.

Witnesses otherwise match their claims. Every line cited above was opened. The absent_details are honest: I found no held line naming the writers of the lives of Agathon or Simon, no held Arabic Synaxarium notice for 1 Kiahk or for Hatur, and no held line joining Mina to the Mennas of PO5 l.1874-1876. Michael the Syrian (MS2 l.34611, 36346, 36649-36651) adds nothing beyond the order of succession, which the cards already carry.

---

### Count

- **Blocking: 2.** A-B1 and A-B2, both in isaac-of-alexandria.
- **Minor: 33.** A-M1 to A-M33. Agathon 11, John III 5, Isaac 6, Simon 8 (A-M27 also covers John III), records 3.

| Profile | Words | FK | Flesch | Blocking | Minor |
|---|---|---|---|---|---|
| agathon-of-alexandria | 348 | 7.60 | 66.28 | 0 | 11 |
| john-iii-of-samannud | 351 | 5.99 | 77.13 | 0 | 5 (+A-M27) |
| isaac-of-alexandria | 346 | 7.43 | 67.43 | 2 | 6 |
| simon-i-of-alexandria | 347 | 6.07 | 75.29 | 0 | 8 |
| records.json | | | | 0 | 3 |

## R1 review, era 4 Who batch 6, PART B

**Scope.** alexander-ii-of-alexandria, michael-i-of-alexandria, joseph-i-of-alexandria, severus-ibn-al-muqaffa (brief, card, audio, records.json rows), plus the batch README.md.

**Method.** Read CLAUDE.md, Who_Profile_Pattern.md (14-point checklist), the README, all four profiles' files, and the batch 2 Benjamin I brief and card for calibration. Re-read every quote against its file. Opened every cited line range and read the context around it. Searched for missed witnesses and false absences with grep across the held files. Ran `grade_text` on each brief and checked card sentence lengths by script.

**Files opened (cic/texts/).** PO5 = chronicle-of-seert_...-patrologia-orientalis-5-...scher-dib1910.txt (Evetts's History, PO 5); SEV = severus-al-muqaffa_history-patriarchs-coptic-church-v1_evetts1904.txt; REN = renaudot_historia-patriarcharum-alexandrinorum-jacobitarum-lat_1713.txt; PO11 = synaxaire-arabe-jacobite_po11-toubeh-amshir-fra_basset1915.txt; BAS1 = synaxaire-arabe-jacobite_po1-thout-babeh-...basset-guidi1907.txt; PO16 = patrologia-orientalis-tomus16_synaxaire-...graffin-nau1922.txt; PO17 = john-ephesus_lives-eastern-saints-po17_brooks1923.txt; BUD1, BUD2, BUDM = the three Budge Ethiopic synaxarium files; BH1 = barhebraeus_chronicon-ecclesiasticum-vol1-lat_abbeloos-lamy1872.txt; ABU = abu-salih_churches-and-monasteries-of-egypt_evetts1895.txt; PO15 = patrologia-orientalis-tomus15_...graffin-nau1927.txt; ASS1 = assemani_bibliotheca-orientalis-tomus1-...1719.txt.

**Quotes.** Every quotation in the four briefs and cards matches its file word for word, allowing for OCR: PO5 "liim", "wheu", "Thcy" and "bv thc", "Alexandcr", "thai" (Alexander's close, l.3907-3912); "l am", "tlic" (Michael's scene, l.8458-8471); "cxile", "becomc" (l.10415-10419); SEV "ihe", "nto" (l.2133-2138); BUD1 l.14646-14651 and l.14814-14815 clean. Quote fidelity passes. The failures below are about context and who said what, not wording.

---

### alexander-ii-of-alexandria

**Verdict: revise.** 4 blocking, 5 minor.

**B-B1. Renaudot's "right hand" is an iron ring worn on the hand. It is not a brand.** Brief, paragraph 5: "Eusèbe Renaudot ... puts it on the right" ("it" is the branding). Card, uncertain: "The brand. The History puts Usamah's ring brand on the left hand, and Renaudot on the right." records.json, contested_claims "Which hand bore Usamah's ring brand".
Evidence: REN l.13440-13442: "Omnes Monachos censu habito numeravit, eosque manicam ferream in dextra ferre jussit ut agnoscerentur; inscripto simul nomine Ecclesiae aut Monasterii". Renaudot has the monks counted and made to *wear* an iron ring (manica) on the right hand, inscribed with their church's name. He does not mention branding. PO5 l.3470-3472 has the brand: "branded each one of them on his left hand, with a branding iron in the form of a ring". The two sources differ on what was done as well as on which hand, and the profile tells only half the difference.
Fix, brief: "Under the governor Usamah, monks were branded on the left hand with a ring-shaped iron. Eusèbe Renaudot, a Catholic scholar writing in Latin in 1713, says instead that they had to wear an iron ring on the right hand."
Fix, card: "The brand. The History says Usamah branded the monks on the left hand with a ring-shaped iron. Renaudot says they had to wear an iron ring on the right hand, with their church's name on it."
Fix, records: contested_claims → "What Usamah put on the monks' hands", with the sides "A ring-shaped brand on the left hand: the History (PO5 l.3470-3472)" and "An iron ring worn on the right hand: Renaudot (REN l.13440-13442)". Make the Renaudot claim row match: "Renaudot: 'manicam ferream in dextra ferre jussit'".

**B-B2. "With only Shamul ... beside him" is misleading.** Brief, paragraph 6: "At dawn, at Tarnut, he died, with only Shamul, bishop of Wasim, beside him."
Evidence: PO5 l.3906-3909: the father spoke "to the brethren", "Accordingly they departed; but not one of the bishops was with him, except Abba Shamul, bishop of Wasim." Shamul was the only *bishop* with him. The brothers were there too. The brief's own previous sentence says "They fled down the river".
Fix: "At dawn, at Tarnut, he died. Shamul, bishop of Wasim, was the only bishop with him."

**B-B3. Alexander asked to go and beg. Kurrah did not send him.** Brief, paragraph 3: "Kurrah sent him to beg in Upper Egypt." Card, knownFor: "He was twice sent out to beg his own ransom".
Evidence: PO5 l.3000-3004: "So when he saw that he could not escape from him, he begged him to let him travel to Upper Egypt, and whatever God allowed him to collect by the alms of the people he would send it to him. Then Kurrah released him". The first time, the begging trip was George the deacon's proposal (PO5 l.2851-2855). Alexander himself later says Abd Allah "sent me out into the country like a beggar" (l.2992-2993).
Fix, brief: "Alexander asked leave to beg in Upper Egypt, and Kurrah let him go."
Fix, card knownFor: "Coptic patriarch of Alexandria under a run of hard governors. Twice he had to beg his own ransom, and he died fleeing a branding."

**B-B4. False absence: John the deacon says he wrote Alexander's last years.** Card, uncertain: "No held line names the writer of Alexander's last years." records.json absent_details: "The writer of his last years ... no held line names who wrote the rest." The README repeats it ("No held line names the writer ... of Alexander's last years").
Evidence: PO5 l.4555-4560. John the deacon, right after his account of George's history: "the Lord Christ knows that we have added nothing to the facts, having related what took place down to the death of the blessed Father Theodore, patriarch of Alexandria, and the affairs of state in his days, to the end of the seventeenth chapter of the History, completed above." Chapter XVII is Alexander II's chapter (PO5 l.2536). A second witness reads it the same way: REN l.13766-13772 says George wrote "usque ad Solimanum Abdelmelici filium; quibus ipse autor adjecit quae usque ad Theodori mortem, sub Asama & aliis Aegypti Praefectis ... secuta sunt". So the History's author, John, added what followed down to Theodore's death.
Fix, card: "Who wrote it. John the deacon, who wrote the History's life of Michael I, says the archdeacon George's history ran to the removal of the governor Usamah. John says he told what followed himself, down to the death of the patriarch Theodore. Renaudot reads him the same way."
Fix, records: delete that absent_details row. Add a claim: "John the deacon: 'we have added nothing to the facts, having related what took place down to the death of the blessed Father Theodore ... to the end of the seventeenth chapter'; Renaudot: 'ipse autor adjecit quae usque ad Theodori mortem'", witness PO5 l.4555-4560 and REN l.13766-13772, Documented. Fix, README: change the sentence to "No held line names the writer of the lives of Agathon or Simon. John the deacon says he wrote the rest of Alexander's chapter himself, down to Theodore's death."

**B-M1. Card uncertain item 1 has no context.** "A note in it says the writer called one emperor "still reigning" at the time he wrote." The listener is not told why this matters, or which emperor. PO5 l.2953-2956: "Anastasius was made prince of the Romans, and is still reigning. (N. B. By saying «still» the writer means at the time of composing the history.)" Evetts's footnote (l.2956): "This note is evidently added by the translator."
Fix: "A note in it says that when the writer called the emperor Anastasius "still reigning", he meant at the time he wrote. B. Evetts says a translator added that note." Or drop the item, since item 2 already covers who wrote it.

**B-M2. The same man is named in two forms.** The card has "B. Evetts heads his life" (dates, uncertain) and "B. T. A. Evetts's 1895 English of Abu Salih" (place). A reader will take these for two people. Pick one form for the whole card, for example "B. T. A. Evetts" at first mention and "Evetts" after. The same problem is in Michael's and Severus's cards (see S-M below).

**B-M3. Alexander's first mention in the brief has no identifier (item 8).** "The patriarch Alexander went to Misr" comes first. "Alexander II of Alexandria" does not appear until paragraph 2. Fix: "Alexander II, the Coptic patriarch of Alexandria, went to Misr to greet the new governor, Abd Allah, as patriarchs did."

**B-M4. "His own clergy" drops the people.** Paragraph 4: "At Easter, Alexander's own clergy demanded their dues." PO5 l.3137-3139: "the people and clergy of Alexandria rose against him, and demanded that he should pay them some of the dues and church-rates on the third day of the Feast of Easter". Fix: "At Easter, the people and clergy of Alexandria demanded their dues."

**B-M5. records.json does not cite Renaudot for the card's "one leaden seal with a lion".** The card's uncertain item rests on REN l.13550-13552 ("Christianos sigillum plumbeum, in quo leonis figura erat, ex collo pendens ferre jussit"), but the Ubaid Allah claim row cites only PO5. Add REN l.13550-13552 to that row.

Writing (item 4). The brief passes. Its rhythm leans choppy in paragraph 5 ("Alexander refused." / "On the third day he fell sick."), and FK 5.8 is well under the grade 8 floor CLAUDE.md asks writers to stay above. The fixes in B-B1 and B-B2 join two short sentences, which helps. Paragraph 2 ("So says the History of the Patriarchs of Alexandria, a later Arabic history of the Coptic church") is word for word Benjamin I's paragraph 2 (see S-M1).

---

### michael-i-of-alexandria

**Verdict: revise.** 1 blocking, 4 minor.

**M-B1. John the deacon is Moses of Wasim's spiritual son. The profile makes him Michael's.** Brief, paragraph 2: "Michael's life in it is told by an eyewitness who shared his prisons. He calls himself "his son John, the poor sinner and deacon."" Placed there, "his" reads as Michael. Card, uncertain item 1: "Its writer, John the deacon, was an eyewitness and Michael's spiritual son." The card's statement is unsupported. The brief's quote is verbatim but has come loose from what it refers to.
Evidence: PO5 l.8766-8769: "the first to be fettered with iron was the holy father and patriarch; and after him the bishop, Abba Moses, and I, his son John, the poor sinner and deacon, upon whom he had laid his holy hand". The nearest antecedent is Moses. John says outright, at PO5 l.5169: "my spiritual father, Abba Moses, bishop of Wasim". At l.10509-10512 he says "my father Moses ... and so also did I, John, the sinner." Renaudot (REN l.15350-15356) also notes that the author speaks often of "Mosem Episcopum Wissim". records.json itself has the claim "John the spiritual son of Moses of Wasim".
Fix, brief: "Michael's life in it is told by an eyewitness who shared his prisons. He calls himself "John, the sinner," and calls Moses, bishop of Wasim, his spiritual father."
Fix, card: "His life rests on the History of the Patriarchs, a later Arabic history of the Coptic church. Its writer, John the deacon, was an eyewitness. He calls Moses, bishop of Wasim, his spiritual father."

**M-M1. "A monk of the church of Saint Macarius" is told with the History as its source, but the History calls him a priest.** Brief, paragraph 2, and card place. PO5 l.5500-5502: "the priest Michael at the church of Saint Macarius, a pure virgin, brought up in the desert". The synaxaria call him a monk: PO16 l.12449-12450 "Ce pere etait moine a l'eglise de Saint-Macaire"; BUDM l.20799 "a monk in the church of Saint Abba macarius". Nothing in this is false. The fix only puts each word with its own witness. Brief fix: "Michael I of Alexandria, also called Khail, was a priest at the church of Saint Macarius." Card place: "Alexandria. A priest at the church of Saint Macarius in Wadi Habib, the History says, and a monk there, the synaxaria say. Held in prison at Misr and at Giza".

**M-M2. "Letters about him" claims more than the line says.** Paragraph 3: "Letters about him reached Cyriacus". PO5 l.7070-7072: "letters had been sent to this king from Egypt, and had reached him while the father, Abba Michael, was in prison with us." The line does not say what the letters held. Fix: "Letters from Egypt reached Cyriacus, the Christian king of Nubia, while Michael was in prison, and the governor seized Michael again, John says."

**M-M3. A role stands in for a named witness (item 5).** Card, uncertain, last item: "which its translator calls a copyist's slip". ABU l.13474 is Evetts's own note: "This is an anachronism due to the carelessness of a copyist." Fix: "The book under the name of Abu Salih names Saladin. B. T. A. Evetts, its translator, calls that a copyist's slip."

**M-M4. Name-form drift.** The card has "B. Evetts" (dates, uncertain) and "B. T. A. Evetts" (Abu Salih source). Same fix as B-M2.

Noted, not a finding. Basset's 11 Mesore notice (PO17 l.60599-60605) says Masis of Ousim was chosen "apres notre pere Anba Djamoul". That matches the History's Shamul of Wasim, so Masis is probably the History's Moses of Wasim. The card's "a bishop who shared his sufferings" is safe as written. Do not make the link without a source that states it.

Checked and sound: scene (PO5 l.8458-8471), Cyriacus and his army (l.7041-7137), Kauzara (l.7835-7957), Isaac of Harran and the ban (l.10200-10419), death and the Saint Macarius record (l.10703-10705), the Saint Mennas letter and its opening (l.5977, 6014-6016, 6500-6518), fasting before communion (l.7239-7241), Renaudot's "fabulae quam historiae propior" (REN l.14910-14911), Renaudot's 741 to 742 (l.14163-14167), Mennas as successor (l.15641-15645), the Budge and Basset army sizes.

---

### joseph-i-of-alexandria

**Verdict: pass after minor fixes.** 0 blocking, 5 minor.

**J-M1. Dionysius has no identifier in the brief (item 8).** Paragraph 3: "with Dionysius, patriarch of the Syriac Orthodox church". The card names him "Dionysius of Tel Mahre", and BH1 l.21266 has "Dionysii Telmaharensis patriarchae". Fix: "The caliph al-Ma'mun came to Egypt with Dionysius of Tel Mahre, patriarch of the Syriac Orthodox church, and sent both patriarchs to the rebels."

**J-M2. "The archbishop of Manuf" will mislead a listener.** Brief close and card remembered. BUD1 l.14814-14815: "Salutation to Archbishop JOSEPH of the city of MANUF". Manuf is his home town (BUD1 l.14593-14594: "the son of one of the elders of the city of MANUF"). His see was Alexandria. Fix, brief: "The Ethiopic Synaxarium greets him as Joseph of the city of Manuf, "unto whom was given the knowledge of Letters."" Make the same change in the card.

**J-M3. Two sources are blended under one name, and one witness is missed.** Paragraph 5: "A man came to the church with a sword to kill him. The sword struck a pillar and broke, the Arabic Synaxarium says." "Came to the church" is Renaudot's (REN l.18197-18199: "patrem suum in Ecclesiam misit, ut occideret Patriarcham"). Basset (BAS1 l.20397-20401) has the emir's brother summon Joseph, with no church. The next line also misses a witness: "In the Ethiopic Synaxarium, Joseph begged the ruler to spare the two bishops." Renaudot has the same plea (REN l.18205-18206: "Cumque Afschinus supplicium de illis sumi juberet, intercessit & obtinuit, ut illis parceretur").
Fix: "A man came with a sword to kill him. The sword struck a pillar and broke, the Arabic Synaxarium says. In the Ethiopic Synaxarium and in Renaudot, Joseph begged the ruler to spare the two bishops."

**J-M4. Card uncertain, "The bishop of Ethiopia whom he sent back", misses a held witness.** BUD1 l.14745-14775 names him John six times ("send unto us as bishop Abba JOHN"). So two witnesses say John against Makrizi's Jacob. Fix: "The bishop of Ethiopia whom he sent back. The History, as Renaudot retells it, and the Ethiopic Synaxarium name him John. Renaudot reports that Makrizi calls him Jacob."

**J-M5. A records.json witness is not a held source.** The claim row "Dionysius of Tel Mahre is the Syriac Orthodox patriarch ..." gives an approved profile file as its witness. Add a held line: BH1 l.21266 ("Dionysii Telmaharensis patriarchae") or l.20113.

Checked and sound: scene (BUD1 l.14611-14651; BAS1 l.20286-20313), family and orphanhood (BAS1 l.20276-20281), 831 and 850 (REN l.18081-18082, 18890-18894), the Bashmurite letters and the embassy (REN l.18128-18166; BH1 l.21805-21818), Dionysius's report (BH1 l.21905-21926), the ages, Georgios (REN l.18238-18286; ABU l.13529-13551), the diploma, the bishops sent out (REN l.18600-18603), "heretics" (REN l.18609). The scene and the close are attributed well.

---

### severus-ibn-al-muqaffa

**Verdict: revise.** 1 blocking, 5 minor. Brief rule 23 (keep the History's compilers apart from Severus, tag the dispute contested): **met**. The authorship extent and the century both have contested_claims rows. The brief tells the dispute in place with Evetts and Renaudot named, and never calls a later life Severus's.

**S-B1. False absence in records.json.** The absent_details row "His works other than the History" says "The Refutation of Eutychius and the History of the Councils are named in PO publisher lists only; not held." Both works are named in held lines that are not publisher lists. REN l.23111-23118 lists "Adversus Said filium Batrik, Alexandrinum Melchitarum Patriarcham" and "De quatuor primis Conciliis Synopsis Historica". ASS1 l.118017-118020 lists "historia quatuor priorum Synodorum". SEV l.163-164 (Evetts) names the refutation's purpose. The card's keyWorks already cites Evetts, Renaudot and Assemani, so the record contradicts the card. Fix: "The texts of the Refutation of Eutychius and of the History of the Councils are not held. Renaudot's list (REN l.23100-23122), Assemani's catalogue (ASS1 l.118017-118020) and Evetts (SEV l.163-164) name them."

**S-M1. Missed held witnesses that bear on the contested claim and on "Little else of his life is recorded".**
(a) REN l.32122-32125: the History's author says an earlier patriarch of the same family name was the one "cujus vitam Severus Aschmonin Episcopus scripsit, Ephrem scilicet". So Renaudot's source has Severus *writing* the life of the patriarch Abraham (Ephraem), his contemporary. That is a life inside the History, beyond translation. It belongs on the "His" side of the contested extent.
(b) REN l.23570-23573 and l.23644-23646: Severus was a close friend of Wadih son of Raja ("magnam cum Severo filio Mocfiih, Episcopo Aschmonin, amicitiam coluit") and told him of a miracle of the Eucharist, which Wadih wrote down. This is held life detail.
Fix, card uncertain (add): "Renaudot's source says Severus himself wrote the life of the patriarch Abraham." Card legacy remembered (add): "Renaudot says Severus was a close friend of Wadih, son of Raja, who wrote down a miracle story Severus told him." records: add both as claims, and add REN l.32122-32125 to the "His" side of the contested extent. The brief's "Little else of his life is recorded" can stand, since this is still little.

**S-M2. Writing (item 4), paragraph 4.** "How much of the History is his is not settled." opens the paragraph on a thesis. "Even his century is unsettled." is a build-up line ("Even"). Fix: "B. Evetts, the History's translator, says no one can know how far Severus's work of translation reaches. ..." (begin with the witness), and "Evetts himself changed his date for Severus. He placed him in the ninth century in 1895, and near the end of the tenth in 1904."

**S-M3. Paragraph 5 is a one-line beat.** "Evetts says he wrote to refute Eutychius, a Melkite patriarch of Alexandria who also wrote history." It sits alone between the dispute and the close. Join it to paragraph 2, after the mastery of Arabic: "Evetts says he wrote to refute Eutychius, a Melkite patriarch of Alexandria who also wrote history." Renaudot backs it too (REN l.22001-22003: "quod fecerunt inter alios Severus Episcopus Aschmonin").

**S-M4. "The patriarch Abraham" has no identifier (item 8), in the brief and the card.** REN l.23003 heads him "EPHRAEM SYRUS, FILIUS ZARAA". Fix: "the patriarch Abraham the Syrian" at first mention in each text.

**S-M5. "A Jewish courtier" overstates.** REN l.23065-23069: the courtier was Abu Yacoub ibn Kalas, a convert to Islam. The man who asked to debate was another Jew, Moses, "qui illi familiarissimus erat" (Abu Yacoub's close friend). Budge (BUD2 l.2000-2004) also has the Jew favoured through his friendship with the caliph's captain. Fix: "Under the caliph al-Mu'izz, a Jew named Moses, a friend of the caliph's adviser, asked to debate the patriarch Abraham the Syrian."

Checked and sound: the dog story (REN l.23087-23096, told as "Narrant"); the mastery of Arabic (l.23072-23074); the debate going no further (l.23083-23087); the third preface and its closing prayer (SEV l.1997-2003, 2133-2138, 2373-2376; the prayer does end the preface before chapter 1 opens at l.2377); Evetts's 1904 notice (SEV l.137-166) and his 1895 dating (ABU l.494-497, 3592-3594); Renaudot on Greek (REN l.869-871), continuers (l.1034-1037), Mauhub and 1088 (l.25855-25877), past a hundred (l.20582); "Sawiros" (PO15 l.61414); Assemani; the Ethiopic debate outcome. Evetts's two name forms ("B. Evetts" and "B. T. A. Evetts" for the Abu Salih source) appear here too. Use one form (see B-M2).

---

### README.md

- **R-B1 (same root as B-B4).** "No held line names the writer of the lives of Agathon or Simon, or of Alexander's last years." This is false for Alexander's last years: PO5 l.4555-4560 and REN l.13766-13772. Fix as in B-B4.
- **R-M1.** "Michael I's life is told by John the deacon, an eyewitness who names himself." Add: "He calls Moses, bishop of Wasim, his spiritual father." This heads off the M-B1 error in later drafting.
- Rest of README checked against my four profiles: the witness lists, the Joseph and Severus source notes, the "drachmae/denarii", "twenty-four and a half" and "line 4414" corrections (PO5 l.3997, l.4414), the ids, and the tradition and date range. All sound.

### Checklist summary (my four profiles)

| Item | Alexander | Michael | Joseph | Severus |
|---|---|---|---|---|
| 1 source establishes | fail (B1-B3) | fail (B1) | pass | pass |
| 2 quotes verbatim | pass | pass (context fail at B1) | pass | pass |
| 3 no invention | pass | pass | pass | pass |
| 4 writing aids | pass, choppy | pass | pass | minor (S-M2, S-M3) |
| 5 named witnesses | pass | minor (M3) | pass | pass |
| 6 partisan marked | pass | pass (Renaudot's scorn shown) | pass (heretics) | pass |
| 7 contested shown | fail (B1 contested row wrong) | pass | pass | pass |
| 8 common names | minor (M3) | pass | minor (J-M1) | minor (S-M4) |
| 9 one term | minor (Evetts forms) | minor | pass | minor |
| 10 story, scene, length | pass | pass | pass | pass |
| 11 grade_text | pass | pass | pass | pass |
| 12 card order, caveat | pass | pass | pass | pass |
| 13 audio tags | pass | pass | pass | pass |
| 14 list line / Who basis | n/a in these files | n/a | n/a | recorder ruling, pass |

The card order matches Mark's order in all four. Missing fields are absent. Each card's What is uncertain opens with the brief's caveat. The audio scripts equal the briefs plus `[calmly]` at the start and `[warmly]` at the start of the last paragraph, and no tag appears in a brief, card or records.json. No card sentence runs past 25 words except a source title in Michael's card, which is a citation.

### Scores

| Brief | Words | FK | Flesch | Approx. time |
|---|---|---|---|---|
| alexander-ii-of-alexandria | 340 | 5.76 | 73.4 | 2:08 |
| michael-i-of-alexandria | 352 | 6.55 | 72.2 | 2:12 |
| joseph-i-of-alexandria | 355 | 6.90 | 67.5 | 2:13 |
| severus-ibn-al-muqaffa | 360 | 6.47 | 71.7 | 2:15 |

All four pass `grade_text` (FK ≤ 10, Flesch ≥ 60). All four are below the grade 8 floor CLAUDE.md describes, which is a rhythm signal and not a gate failure. At 160 words a minute, all four run slightly past 2 minutes.

Cross-profile sameness. "So says the History of the Patriarchs of Alexandria, a later Arabic history of the Coptic church" (Alexander) and "B. Evetts ... heads his life X to Y" (Alexander, Michael, and Benjamin I) are the same sentence frame from profile to profile. They are accurate. Across seven patriarchs from one History, though, they will read interchangeably. Vary the frame, or fold the date into the who-line.

### Count

**Blocking: 7** (B-B1, B-B2, B-B3, B-B4, M-B1, S-B1, R-B1, where R-B1 shares B-B4's root; 6 distinct defects).
**Minor: 21** (Alexander 5, Michael 4, Joseph 5, Severus 5, README 1, plus the cross-profile frame note counted once).
