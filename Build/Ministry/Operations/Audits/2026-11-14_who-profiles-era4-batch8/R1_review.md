# R1 review: era 4 batch 8

Round 1, the full checklist review, by three fresh Opus agents that had not seen the drafting, at full effort. Part A covers Eadburga of Thanet, Abbess Bugga and Adam (Jingjing). Part B covers Yahya ibn Said of Antioch, Elias of Nisibis, the README and the final sweep. Part C covers al-Baladhuri, added to the batch by the coordinator while parts A and B ran. Each part is given as its reviewer wrote it.

## Era 4 Who batch 8, round 1 review: PART A

**Scope.** eadburga-of-thanet, abbess-bugga, adam-jingjing. For each I reviewed the brief, the card, the audio script and its records.json entry. I also read the batch README.

**Method.** I read CLAUDE.md, Who_Profile_Pattern.md (the 14-point checklist), the batch README, the approved Leoba profile (era4/batch3) and Alopen profile (era4/batch5), and the batch 6 R1 review for its format. I checked every quotation against its vendored file, allowing for whitespace and OCR noise. I opened each cited line range and read it in context. I diffed each audio script against its brief. I ran `engine.m1.gates.grade_text` on each brief and counted sentence lengths with a script. I searched all of `cic/texts/` for Eadburg*, Bugga/Buggan/Bucga, Heaburg, Eangyth, King-Tsing/King-tsing, Ching-ching, Jingjing, Takakusu, Satparamita, Si-ngan and Adam near the stele. I edited no files.

**Files opened (cic/texts/).**
- BONI = boniface_english-correspondence_kylie1911.txt: contents l.236-300; intro l.786-800, 918-935, 1060-1142, 1170-1195, 1410-1420, 1555-1570, 1740-1756; letters IV l.2425-2485, VII (Egburg) l.2694, VIII l.2855-3050, IX l.3110-3215, XIII l.3436-3470, XIV-XV l.3900-3970, XXII-XXIII l.4455-4560, XXVIII l.5160-5200, XXIX l.5268-5300, XXXVIII l.6020-6075; index l.8025-8060, 8102, 8149.
- AASS3 = acta-sanctorum_martii-tomus-3 l.126330-126385, 167771.
- PL96 = ildefonsus-julian-toledo-pl96 l.69740-69825, 130225-130236.
- PL159 = anselm-canterbury…pl159 l.58220-58232.
- ALC = alcuin_opera-omnia l.60650-60760, 115010-115026, 116655-116664, 118128-118134.
- PLUM = bede_opera-historica-v1 l.1180-1196, 5855-5870.
- LP1 = liber-pontificalis t1 l.38288-38297.
- MAL = malech_history… l.13140-13210, 13560-13650, 13940-14180, 14355-14372.
- YULE = marco-polo…v2 l.2980-3010.
- ASS2 = assemani…tomus3-pars2 l.32985-33030, 36280-36345, 36440-36482, 36560-36800.
- CHAB = yahballaha-sauma…chabot1895 l.1318-1372.
- BUDGE = yahballaha-sauma…budge1928 l.5150-5240.
- Searched beyond these: benedict-aniane_concordia-regularum…pl103 (PL103) l.93280-93292; john-biclaro-leander-pl72 l.47110-47122 (an Eadburga virgin on 15 June, another woman); liber-pontificalis t2 l.130110 (index only); wigram_assyrians…1929; barhebraeus_chronicon…vol3.

**Quotations.** Every quotation in the three briefs and cards matches its file word for word, once OCR noise is allowed for. The OCR differences:
- BONI l.3923 has "my be honoured". The brief paraphrases this line and does not quote it.
- BONI l.2451-2457: a page break and running head fall between "my" and "mind".
- BONI l.3159: "wai[t]". BONI l.3172: "gitts".
- MAL l.13623: "books’" carries a footnote mark.
- The Adam brief, para 1, sets a comma inside the quote after "substance". The file has a full stop there (MAL l.13574-13575). See A-M21.

**Audio.** All three scripts equal their briefs once `[calmly] ` (line 1) and `[warmly] ` (start of the last paragraph) are removed. The tags appear nowhere else. Checklist 13 passes for all three.

---

### eadburga-of-thanet

**Verdict: one blocking finding (A-B1). Otherwise passes with minor fixes.** The profile agrees with Leoba on every point: the verses, Eadburga's teaching, and Kylie's placing of Leoba at Thanet.

**A-B1 (card `dates` and `uncertain[4]`; records: the AASS3 claim and absent_details: a false absence).**
- The card says "No source used here gives her birth or death" and "Neither her birth nor her death is in the sources used here."
- The Bollandists are a source used here, and they give a death day for this Eadburga, under their merged identity. Evidence: AASS3 l.126368-126371: "Creditur Eadburga, cognomento Buggan, Abbatissa fuisse in Cantio, et mortua γι [vi] Kalendas Januarii anno Dccurx, et inscripta variis Martyrologiis ad xvi Julii."
- They mean the same Eadburga. The passage follows their quotation of Boniface's vision letter to her (l.126353-126366).
- The day is legible: vi Kal. Jan. is 27 December. Only the year is garbled. So the records note ("a death day in December whose figures the OCR garbles") and the absent_details note ("the OCR garbles it") are also wrong.
- The Bugga profile already uses the same day, 27 December, from Bregwin.
- Fix, card `dates`: "Eighth century. Edward Kylie dates the letters to her from about 717 to the 740s. The Bollandists, who take her to be Bugga, give her death day as 27 December; the year cannot be read in the held scan. No source used here gives her birth."
- Fix, `uncertain[4]`: "Her years. Kylie dates the letters to her from about 717 to the 740s. The Bollandists give her death day as 27 December, the same day Bregwin of Canterbury gives for an abbess Bugga, and say martyrologies list her on 16 July. That rests on their view that she was Bugga."
- Fix, records: correct the AASS3 claim to "vi Kal. Jan. (27 December); year garbled", and rewrite the absent_details note to match.

**A-M1 (brief, para 7: the stylus reads as a writing tool).** "Lul, Boniface's deacon, wrote to Eadburga too, with a silver stylus, storax and cinnamon, and asked for her prayers." Heard aloud, "wrote … with a silver stylus" sounds like the pen he wrote with. Evidence: BONI l.4482-4483: "Some small presents I have sent … a silver style and some pieces of storax and cinnamon". Fix: "Lul, Boniface's deacon, wrote to Eadburga too. He sent her a silver stylus, storax and cinnamon, and asked for her prayers."

**A-M2 (brief, para 5: Milburga has no place; checklist 8).** "in the convent of Abbess Milburga". Kylie's heading places the vision at Wenlock. Evidence: BONI l.3441-3443: "a vision seen in the monastery at Wenlock". Fix: "A man in the convent of Abbess Milburga at Wenlock had died and come back to life".

**A-M3 (card, `uncertain[3]`: the Alcuin note is overstated as a guess).** The card says the note "says Eadburga built that church, and marks the whole as a guess." In the note, "Forte" ("perhaps") governs only the identification of the poem with the church at Thanet. The building is stated as a fact, in a relative clause. Evidence: ALC l.60695-60697: "Forte ecclesiam Tanetensem in Anglia, quam Eadburga abbatissa eodem pene tempore aedificavit". Fix: "A note in Migne's edition of Alcuin's poems suggests, as a guess, that a poem on an apse of Saint Peter is about the church at Thanet. The note states that Eadburga built that church. It gives no source for this."

**A-M4 (brief, paras 7 and 9: paragraphs open on a thesis; checklist 4).** "She was also a teacher." and "Who she was beyond these letters is less clear." Both are status lines that open a paragraph, and the evidence follows them. The second is vague. Fix, para 7: open on the fact: "Leoba, a young woman of Boniface's circle, learned verse from her." Fix, para 9: "The Bollandists, editors of the Acta Sanctorum, report a belief that she was an abbess in Kent also called Bugga."

**A-M5 (missed witness on the stylus letter).** A note in PL103 credits the silver-stylus gift to Boniface. Kylie gives the letter to Lul. Evidence: PL103 l.93286-93289: "S. Bonifacius praesul Moguntinus epist. ad Eadburgam abbatissam: 'Parva munuscula … id est, unum graphium argenteum.'"; BONI l.4464-4470 (letter XXII, headed as Lul's). Fix: add a records claim, tagged Documented for the note's words, with a contested_claim on the sender: Lul (Kylie, BONI l.4464-4470; Plummer, PLUM l.5862-5868; Duchesne, LP1 l.38292-38295) against Boniface (the PL103 note). Optionally add one card `uncertain` line. The brief can stay as it is, since three named witnesses give Lul.

**Scores.** 357 words, about 2 minutes 10 seconds. FK 6.62, Flesch 71.85. Passes. The longest brief sentences are 25 words, and the last of them is mostly quotation. Card sentences are all 25 words or fewer.

---

### abbess-bugga

**Verdict: three blocking findings (A-B2 to A-B4). Otherwise passes with minor fixes.**

**A-B2 (brief, para 5: Boniface's advice misread).**
- The brief says: "He would neither forbid it nor urge it. Their sister Wiethburga had found quiet at the shrine of Saint Peter, he wrote. But she advised waiting until the dangers 'from the Saracens' in Italy were over."
- In the letter, Boniface will not urge the journey *strongly*. He then says going abroad seems better to him, accepts Wiethburga's advice to wait as the best plan, and tells Bugga to prepare for the journey.
- The brief drops "strongly" and leaves out his advice. That makes him neutral, and it makes the delay Wiethburga's counsel against his own.
- Evidence: BONI l.3133-3135: "I cannot presume either to forbid or to urge strongly upon thee a journey abroad"; l.3140-3150: "It seems to me better that if … thou canst not find in thy native land the freedom of a quiet mind, thou shouldst … seek liberty for contemplation by going abroad, just as did our sister Wiethburga"; l.3157-3166: "she bade me have thee wai[t] … and this I think myself to be the best plan. And so thou shouldst prepare the necessaries for the journey".
- Fix: "She had asked whether to go abroad. He would not urge it strongly, he wrote, but if she found no quiet at home, going seemed better. Their sister Wiethburga had found quiet at the shrine of Saint Peter. Wiethburga advised waiting until the dangers 'from the Saracens' in Italy were over, and Boniface agreed."

**A-B3 (card `sources.ownWords`, records, and the Eadburga records: wrong letter number).**
- The card's title reads "letter VII, Eangyth and Heaburg to Wynfrith". The records say "Letter VII" in both profiles.
- Kylie's letter VII is Egburg's letter. Eangyth and Heaburg's letter is VIII. The OCR dropped one "I" from its heading.
- Evidence: BONI l.2694 "13 VII" heads Egburg's letter. BONI l.2862 reads "14 VII" but stands between VII and IX. The contents (l.250-256) list Egburg, then Eangyth and Heaburg. Kylie's intro, l.1073-1076, cites "Egburga … (VII), while Abbess Eangyth and her daughter, Bugga … (VIII, IX)".
- Fix: "letter VIII" in the card title and in every records claim and contested_claim side (Bugga: the letter VII claim; Eadburga: the claim "Kylie's index … letter VII names").

**A-B4 (brief, para 3: "An earlier letter" is unsupported).**
- "An earlier letter, from her mother Eangyth, an abbess, names her as …"
- Kylie dates letter VIII to 719-722 and Bugga's letter IV to 720-722, and he numbers VIII after IV. No held line says VIII came first.
- Evidence: BONI l.2865-2867 "719-722"; l.2436 "720-722".
- Fix: "Another letter, from her mother Eangyth, an abbess, names her as 'her only daughter Heaburg, called Bugga'."

**A-M6 (brief, para 1: Rathbod has no context; checklist 4).** A listener does not know who Rathbod is. Kylie says. Evidence: BONI l.788-795: the Frisians … "Their King, Rathbod". Fix: "and Rathbod, king of the Frisians, 'that enemy of the Catholic Church', had been laid low."

**A-M7 (brief, para 3: "signed").** "She signed herself 'Bugga, a lowly handmaiden'." The words come from the letter's opening greeting. They are not a signature. Evidence: BONI l.2438-2441. Fix: "She named herself in the greeting as 'Bugga, a lowly handmaiden'."

**A-M8 (brief, para 7: a pronoun that shifts, and a common name).**
- "She had prayed at the holy places of Rome, he told Boniface, and met him there." "Him" can be heard as Ethelbert, the subject "he". Ethelbert met her at home, after her return, and not in Rome. Evidence: BONI l.6048-6056: "when at her invitation I came at once to speech with her … while you were both in Rome".
- "Ethelbert, king of Kent" can also be heard as the Ethelbert of Augustine's day. Kylie's heading (BONI l.6035) gives "Ethelbert the Second".
- Fix: "Years later Ethelbert the Second, king of Kent, wrote of 'the venerable Abbess Bugga', his kinswoman. She had prayed at the holy places of Rome, he told Boniface, and had met Boniface there." Apply the same identifier on the card ("King Ethelbert of Kent" in `place` and `legacy.traces[1]`).

**A-M9 (brief, para 11: "They", and what Bugga asked for).**
- "Bregwin … later wrote to Lul, who followed Boniface at Mainz. They kept the burial day …" "They" can be heard as Lul and Boniface.
- Bugga's request was that Mainz keep her day too. She asked for more than that Lul be told.
- Evidence: PL96 l.69812-69818: "Diem … depositionis … Buggan celebramus … Rogavit me obnixe, dum adhuc viveret, ut hoc vestrae beatitudini transmitterem. Et sicut speravit et credidit, ita facere curate, quoniam illius pater atque patronus fuit in Christo Bonifacius episcopus."
- Fix: "He and his church kept the burial day of an abbess named Bugga, 27 December, he said. While she lived, she had asked him to send word, so that Mainz would keep it too, since Boniface had been her father in Christ."

**A-M10 (brief, paras 7 and 9: the order suggests a sequence the dates do not give).** Letter XXIX (723-745) comes after Ethelbert's letter XXXVIII (748-754). That makes it sound as if her old-age sorrows followed the return from Rome. Evidence: BONI l.5275 "723-745"; l.6039 "748-754". Fix: move para 9 before para 7. Or anchor it: "Some years before Ethelbert wrote, Boniface heard …"

**A-M11 (brief para 11 and card `uncertain[1]`, `uncertain[2]`: the Bollandists' wording, and a missed match).**
- Both texts say the Bollandists made Bugga another name of "Eadburga of Thanet". They say "in Cantio" (in Kent) and never name Thanet. Their Eadburga is the one Boniface wrote to about the vision. Evidence: AASS3 l.126353-126369.
- The Bollandists give their Eadburga-Bugga the same death day, vi Kal. Jan. (27 December), that Bregwin gives for his Bugga. This bears directly on `uncertain[2]` ("He gives no other mark"). Evidence: AASS3 l.126370; PL96 l.69815.
- Fix, brief: "… report a belief that Bugga was another name of Abbess Eadburga, the woman Boniface wrote to about the vision."
- Fix, `uncertain[2]`: add "The Bollandists give the same day, 27 December, for the death of their Eadburga called Bugga."

**A-M12 (card: `dates` and `uncertain[3]` wording).**
- `dates`: "the last letters about her to between 748 and 754". Only letter XXXVIII has that date. Fix: "the last letter about her".
- `uncertain[3]`: "The same volume calls the poem about her spurious." The list rejects the poem as Alcuin's, because it was written in the reign of Ine. It does not call the poem a fake about her. Evidence: ALC l.115017-115023: "In carminibus etiam quaedam notha et spuria sunt: ut carmen seu epigramma 3 de Bugga, quod scriptum est regnante Ina Westsaxonum rege". Fix: "The same volume says that poem is not Alcuin's, since it was written under Ine, king of the West Saxons."

**A-M13 (card `uncertain`: joining Ethelbert's Bugga to the others is Kylie's call).** Ethelbert's abbess Bugga is joined to the Bugga of letters IV, VIII and IX only by Kylie's index and introduction (BONI l.8029, 1074-1076, 1563-1564). The brief's "Bugga did go." rests on that join. Fix: add to `uncertain`: "That Ethelbert's Abbess Bugga is the same woman. Kylie's index and introduction join them; Ethelbert names no mother or earlier letters."

**Scores.** 382 words, about 2 minutes 20 seconds. That is the long end for a non-major Who, though within this batch's range. FK 7.19, Flesch 66.71. Passes. The longest brief sentences are 24 words. Card sentences are all 25 words or fewer.

---

### adam-jingjing

**Verdict: one blocking finding (A-B5). Otherwise passes with minor fixes.** The profile agrees with Alopen on the stele: 781, King-Tsing as author in Wylie's English, Alopen from Syria reaching Chang-an in 635, and the emperors' favor.

**A-B5 (brief, para 7: who set up the stone is told as settled, in an ambiguous clause).**
- "The stone names a second Adam too, a deacon, son of the priest Jazedbuzid, who set the stone up."
- records.json carries a contested_claim, "Who set up the stone": Jazedbuzid, by the Syriac, against Adam, by Cordier (YULE l.3000). The card's `uncertain[3]` gives both. The brief gives one side with no witness named.
- The relative clause can also be heard as the deacon Adam setting it up.
- Evidence: MAL l.14162-14165; ASS2 l.36709-36711; YULE l.3000: "Adam (King-tsing), who erected the monument".
- Fix: "The stone names a second Adam too, a deacon, son of the priest Jazedbuzid. The Syriac, as Kircher and Assemani read it, says Jazedbuzid set the stone up. Cordier writes that Adam erected it."
- Or the coordinator rules that Cordier's "erected" is not a rival reading, and the contested_claim is removed. Either way, the brief and the records must agree.

**A-M14 (brief, para 9: "the same emperor" has no antecedent).** No emperor of 781 is named earlier in the brief. Evidence: YULE l.3000-3001: "under Te-Tsung … under the same Emperor". Fix: "under Te-Tsung, the emperor in whose reign the stone was raised".

**A-M15 (brief, para 5: "It closes with praise of the priest I-sz'").** The praise of I-sz' closes the prose preface. An ode and the dating lines follow it. Evidence: MAL l.13998-14003 (I-sz', end of the preface); l.14006 "ODE."; l.14141-14145 (date and writer). Fix: "Its prose part closes with praise of the priest I-sz' …"

**A-M16 (brief paras 3 and 11; card `uncertain[6]`: "held" is project jargon).** "the held sources", "No held source gives …", "not legible in any held file". A listener does not know what "held" means. The cards use "sources used here". Fix, brief para 3: "everything the sources say of Adam comes from the stone". Fix, para 11: "No source gives his birth, his death or where he came from." (Records note the full-Library search.) Fix, card: "It is not legible in any file used here".

**A-M17 (brief, para 7: undefined terms and an unplaced name; checklist 4).** "chorepiscopus" and "papas" are never explained. "Athanasius Kircher" appears with no context. The Kircher renderings in the next sentence gloss "chorepiscopus" only in passing. Evidence: ASS2 l.36644-36646 (Kircher's "Archiepiscopum … Vicarium Episcopi"); ASS2 l.33003-33008 (Assemani on "Papas" as a title among these churches). Fix: "… naming Adam priest and chorepiscopus, a bishop's assistant over country churches, and papas, or father, of China. Athanasius Kircher, who first published the stone in Latin, had rendered …" If no held line supports the gloss on "chorepiscopus", use Kircher's own pair: "a word Kircher rendered once as archbishop and once as a bishop's vicar".

**A-M18 (card `uncertain[5]`, README: "Two Adams" undercounts).** The stone names more Adams than two. Malech's lists of the names include an Adam in the fifth band and another in the seventh. Assemani's classes of names list an "Adam Presbyter". Evidence: MAL l.13193-13194, 13201-13202; ASS2 l.36340. Fix: "Other Adams. The stone also names Adam the deacon, a son of Jazedbuzid, a different man. Its lists of names, in Malech and Assemani, include at least one more Adam, a priest." The brief's "a second Adam too" is accurate as written.

**A-M19 (records and card `uncertain[2]`: Kircher's readings).**
- Assemani reports that Kircher read the stone as saying the Papa (Adam) set it up. That belongs on the Adam side of the "Who set up the stone" contest. Evidence: ASS2 l.36780-36783: "ipse ubique legit Papa, & hunc tabulam illam lapideam erexisse affirmat: Constituit tabulam hanc Papa". Fix: add to that contested_claim's Adam side: "Kircher, as Assemani reports him (ASS2 l.36780-36783)".
- "Kircher's English in Malech" is loose. Kircher wrote in Latin, and Malech prints an English version of his reading (MAL l.14150: "Kircher translates this as follows"). Fix: "Kircher's reading, in Malech's English, has …"

**A-M20 (card `legacy.traces[0]`: an evaluative claim with no witness).** "His text is the main source for Alopen and the coming of the Church of the East to China." No witness is named. Alopen's approved card shows that all its held sources go back to the stele. Fix: "Every source used for Alopen's profile goes back to his text."

**A-M21 (brief, paras 1 and 3: wording).**
- Para 3: "names him as Adam, with King-tsing beside it" is awkward. Fix: "joins the two names: he writes 'Adam (King-tsing)'." (YULE l.3000)
- Para 1: the quote puts a comma inside the quotation marks after "substance", where the file has a full stop (MAL l.13574-13575). Fix: "It praises 'our eternal true lord God, triune and mysterious in substance'. He 'appointed the cross as the means for determining the four cardinal points'."

**Scores.** 374 words, about 2 minutes 15 seconds. FK 6.78, Flesch 70.42. Passes. The longest brief sentence is 25 words, and most of it is quotation. Card sentences are all 25 words or fewer.

---

### records.json (these three)

- Line numbers and witness labels match the files. I opened every cited range. The two exceptions are the letter VII label (A-B3) and the AASS3 death-day note (A-B1).
- The confidence tags fit the pattern. Kylie's and Cordier's own views are tagged Dominant Modern Reconstruction. The Bollandist identity is Contested. The Alcuin index and note are Inferential-Thin.
- The other absent_details are honest. I found no held letter of Eadburga's, no held name or place for Bugga's monastery, and no held line on Adam beyond the stone and Cordier's note. I searched King-Tsing, King-tsing, Ching-ching, Jingjing, Takakusu and Satparamita across `cic/texts/`.
- The scope fixes are under A-B1, A-B3, A-M5 and A-M19.

### Checklist summary

| # | Eadburga | Bugga | Adam |
|---|---|---|---|
| 1 Sources establish sentences | pass | fail (A-B2, A-B4) | pass |
| 2 Quotes verbatim | pass | pass | pass (punctuation, A-M21) |
| 3 No invention | pass | pass | pass |
| 4 Reading aids | minor (A-M1, A-M4) | minor (A-M6) | minor (A-M16, A-M17) |
| 5 Named witnesses | pass | pass | pass |
| 6 Partisan marked | n/a | n/a | n/a |
| 7 Contested both sides | fail on card absence (A-B1) | pass, minor (A-M11) | fail (A-B5) |
| 8 Common names | minor (A-M2) | minor (A-M8) | pass |
| 9 One term | pass | pass | pass |
| 10 Story, scene, length | pass | pass, long end | pass |
| 11 grade_text | pass | pass | pass |
| 12 Card order and caveat | pass | pass | pass |
| 13 Audio tags | pass | pass | pass |
| 14 Who test | pass (taught and led) | pass (governed) | pass (author) |

American spelling holds in the narrator's prose. "honoured" appears only inside quotation.

### Count

- **Blocking: 5.** A-B1 (Eadburga); A-B2, A-B3 and A-B4 (Bugga; A-B3 also corrects the Eadburga records); A-B5 (Adam).
- **Minor: 21.** A-M1 to A-M21. Eadburga 5, Bugga 8, Adam 8.

| Profile | Words | FK | Flesch | Blocking | Minor |
|---|---|---|---|---|---|
| eadburga-of-thanet | 357 | 6.62 | 71.85 | 1 | 5 |
| abbess-bugga | 382 | 7.19 | 66.71 | 3 | 8 |
| adam-jingjing | 374 | 6.78 | 70.42 | 1 | 8 |

**Files reviewed (absolute paths)**
- /home/user/CIC-Project/Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era4/batch8/eadburga-of-thanet.brief.txt and .card.json
- /home/user/CIC-Project/Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era4/batch8/abbess-bugga.brief.txt and .card.json
- /home/user/CIC-Project/Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era4/batch8/adam-jingjing.brief.txt and .card.json
- /home/user/CIC-Project/Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era4/batch8/audio/ (the three scripts)
- /home/user/CIC-Project/Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era4/batch8/records.json

---

## Era 4 Who batch 8, round 1 review: PART B

**Scope.** yahya-ibn-said-of-antioch and elias-of-nisibis: the brief, the card, the audio script and the records.json entry for each. Also the batch README.md, including its "final sweep" section. I reviewed branch `claude/who-profiles-era4-batch8` at HEAD `c10503d0` ("al-Baladhuri draft, before review"). That commit landed while I was reviewing. It adds an al-Baladhuri profile, and the README has not been updated for it (R-M1).

**Method.** I read CLAUDE.md, Who_Profile_Pattern.md (the 14-point checklist) and the batch README. For calibration I read the batch 6 Severus ibn al-Muqaffa brief and the batch 5 Thomas of Marga brief and card, plus the batch 6 R1 review for its format.

For each brief sentence and card string I opened the cited lines and read them in context. I checked every telling of French or Latin against the original. I worked out every Seleucid and Hijri conversion again, and checked the weekdays the sources give against a Julian calendar.

I grepped all of cic/texts for both men under every spelling. For Yahya: Yahya, Yahia, Iahia, Jahia, Jahja, al-Antaki, "continuateur d'Eutychius". For Elias: Elias/Elie/Elijah of Nisibis, Nisibenus, Bar-Sinaeus/Barsinaeus, bar Sinaya/Shinaya/Shinaji, Sobensis. I ran `grade_text` on each brief, measured sentence lengths by script, and diffed each audio script against its brief.

For the final sweep I took every WHO row from both scan tables by script. I matched them against the ids in batches 1 to 8, with batch 7 read from `origin/claude/who-profiles-era4-batch7`. I also read both scans' rulings sections and searched the Decision-Log.

**Files opened (cic/texts/).**
- PO18 = po18_patrologia-orientalis-t18-yahya-ibn-said-histoire-ara-fra_kratchkovsky-vasiliev1924.txt (l.1-10, 44330-44560, 44585-44860, 45060-45080, 50300-50540, 52600-52700)
- MAC = stepanos-taron_histoire-universelle-deuxieme-partie-fra_macler1917.txt (l.612-622, 13225-13320, 13843-13852)
- PO5 = chronicle-of-seert_..._scher-dib1910.txt (l.1-12, 29380-29420)
- ELI = elias-of-nisibis_opus-chronologicum-lat_brooks-chabot-csco1910.txt (l.1-12, 85-225, 8395-8610, 8830-8870, 60310-60345)
- ASS1 = assemani_bibliotheca-orientalis-tomus3-pars1-..._1725.txt (l.46100-46300)
- BH3 = barhebraeus_chronicon-ecclesiasticum-vol3-..._1877.txt (l.15940-16000, 31215-31235)
- MARI = mari-ibn-sulayman_..._gismondi1899.txt (l.10925-11002)
- PAR = aphrahat_demonstrationes-1-22-syr-lat_parisot1894.txt (l.3100-3130)
- CM = chronica-minora-pars-prior-versio-lat_guidi1903.txt (l.19360-19380, 25270-25290)
- MAL = malech_..._1910.txt (l.1128-1140, 8500-8508, 15598-15608)
- Beyond the main list:
  - MAI = mai_scriptorum-veterum-nova-collectio-tomus10-ebedjesu-synodus-timothei-lat_mai1838.txt (l.390-402, 7340-7510, 8405-8430, 16340-16365)
  - SYN = synodicon-orientale_recueil-de-synodes-nestoriens-syr-fra_chabot1902.txt (l.1722-1745, 45495-45510)
  - PO2 = zacharias-scholasticus_vie-de-severe-po2-syr-fra_kugener1903.txt (l.20040-20060)
  - BRAUN = synodicon-orientale_das-buch-der-synhados-deu_braun1900.txt (l.150-170)
  - thomas-of-marga_book-of-governors-v2-english_budge1893.txt (l.12910-12925)
  - john-ephesus_lives-eastern-saints-po18_brooks1924.txt (a second OCR of PO18, l.39862)

**Quotations.** Neither brief and neither card uses quotation marks. Every source line is French or Latin, and each is told in modern words with its source named, as the README says. I checked each telling against the original. They hold, apart from the points listed below (Y-M3, Y-M7, E-B1, E-M4, E-M6). The records.json quotations match their files apart from OCR noise. Examples: PO18 l.44372 "x1°", "d'Kutychius"; l.44783 "aprés m'étre"; ELI l.8601 "linitus"; ASS1 l.46185-46216, long-s and ligature OCR ("fortiter rettitit", "Hoiaino Abulcafo» mo"); CM l.19372 "RECITA TA".

**Dates.** Every conversion is right.
- AH 326 is 8 November 937 to 28 October 938 (PO18 l.44613).
- AH 405 is 2 July 1014 to 20 June 1015 (l.44802).
- 5 Jumada II 355 is 28 May 966, a Monday. Easter 966 fell on 15 April, so Pentecost was 3 June and the Monday before it was 28 May.
- AH 397 began 27 Ilul 1317 Seleucid, which is Friday 27 September 1006 ("praeparatione").
- Elias's life note:
  - Thursday night, 11 Shebat 1286, is 11 February 975, a Thursday.
  - Saturday, 15 Ilul 1305, is 15 September 994, a Saturday.
  - Sunday, 15 Shebat 1313, is 15 February 1002, a Sunday.
  - Sunday, 26 Kanun I 1320, is 26 December 1008, a Sunday.
- Isho'yahb was ordained in December 1020. Bar Hebraeus has Advent of AH 411, Assemani has December 1332, and Mari has Sunday 11 December 1332, 22 Sha'ban 411.
- Seleucid 1360 is 1049.

**Audio.** Both scripts equal their brief once `[calmly] ` (start) and `[warmly] ` (start of the last paragraph) are removed. The tags appear nowhere else. Item 13 passes.

---

### yahya-ibn-said-of-antioch

**Verdict: passes with minor fixes. No blocking finding.**

The scene, the who-line, the plan, the two revisions, the honest limit and the closing all rest on PO18 and read correctly in context. The Schlumberger lines match MAC l.13264-13293.

**Y-M1 (brief, para 6; card, legacy.remembered[1]: "the emperor Basil", a common name; checklist 8).** Two emperors named Basil appear in these files. Macler's note around this passage discusses Basil I (MAC l.612-622). The quoted passage is about Basil II.
- Evidence: MAC l.13238 "Basile II" (the note on this very war, the "Seconde guerre bulgare"); PO18 l.44377 "l'empereur Basile Bulgaroktonos".
- Fix, brief: "Yet only lately, he writes, has Yahya's chronicle shown that the emperor Basil II's Bulgarian war lasted four whole years."
- Fix, card: the same, "the emperor Basil II's Bulgarian war".

**Y-M2 (brief, para 5; card, keyWorks.about and uncertain[3]-[4]: project jargon in participant text; checklist 4).** The brief has "all the held sources give of his life". The card has "The part held here", "the held text" and "the held scan". "Held" is the Library's working word, and a listener will not know it. The approved Thomas of Marga card uses "the sources used here".
- Fix, brief: "His preface is all that the sources used here give of his life."
- Fix, card: "The part used here runs to about 970", and "His Arabic. The Arabic in this scan cannot be read, so his words are read in his editors' French."

**Y-M3 (brief, para 3: "a patron").** The preface says only that someone asked for and urged the book.
- Evidence: PO18 l.44601-44604 "celui qui m'a prié de faire (ce livre) et de l'écrire, qui m'a poussé à le mettre en ordre"; l.44779 "celui qui m'avait chargé de le composer".
- Fix: "He wrote for someone he does not name, who had asked him for the book."

**Y-M4 (brief, para 6: Schlumberger given no context; pattern, common names, "any name a general listener would not know").** The listener is not told who Schlumberger is.
- Evidence: MAC l.13277 cites "G. Schlumberger, L'Épopée byzantine … II, p. 43". PO18 l.44383-44384 and its footnote 2 name his books on Nicephorus Phocas and on the Byzantine epic of the tenth century.
- Fix: "Frédéric Macler, translating the Armenian historian Stepanos of Taron, quotes Gustave Schlumberger's history of Byzantium in that age, L'Épopée byzantine."

**Y-M5 (brief, para 1: the patriarch's refusal compressed; the attack's leader dropped).** "The governor of Jerusalem had pressed him for more gifts than custom allowed, and John had refused." In the source, John at first paid. He appealed to Kafur, and refused only the extra Pentecost demand. The governor then led his own band to the church.
- Evidence: PO18 l.50321-50323 "le patriarche lui avait donné tout ce qu'il lui avait demandé"; l.50388-50395 (the Pentecost demand; "ne lui donna pas ce qu'il lui avait réclamé"); l.50446-50447 "ag-Canadji partit avec sa troupe".
- Fix: "The governor of Jerusalem had demanded more gifts than custom allowed. John paid at first, but he refused a new demand at Pentecost. The governor gathered his followers and came for him."

**Y-M6 (card, uncertain[0]: "or his family").** His own title names his father.
- Evidence: PO18 l.44595 "Yahya, fils de Sa'id, d'Antioche".
- Fix: "His preface is all the sources used here give of his life. None gives his birth or his death. Of his family, only his father's name, Sa'id, is in his title."

**Y-M7 (card, legacy.traces[0]: the purpose clause is attached to the wrong verb).** "He revised the history twice ... so that readers would know why copies differ." He recorded the revisions so readers would know. He did not revise for that reason.
- Evidence: PO18 l.44790-44793 "Je voulais signaler tout cela, afin que, s'il se trouvait d'autres manuscrits ... la cause de ceci fût connue."
- Fix: "His preface says he revised the history twice, the second time after moving to Antioch. He set this down so that readers would know why copies differ."

**Records.** The witnesses and line numbers are correct, and so are the absent_details: I found no held Yahya line beyond PO18, MAC and PO5. For information, cic/texts also holds a second OCR of the same tome (john-ephesus_lives-eastern-saints-po18_brooks1924.txt, Yahya's avant-propos at l.39862). It adds no witness, but it could help where the first OCR is garbled.

**Scores.** 374 words, about 2 minutes 15 seconds. FK 6.85, Flesch 69.35. Passes. The longest brief sentence is 25 words (the Schlumberger line), and one card sentence is 23 words.

---

### elias-of-nisibis

**Verdict: two blocking findings (the opening scene misdates his writing and places him in the wrong see; a held text of his own words is missed and recorded as not held). The rest are minor.**

**E-B1 (brief, para 1: the scene dates his writing to 1006 and calls him "a churchman of Nisibis" that year).** "In the Arab year 397, which began in 1006, a churchman of Nisibis noted a split among Christians." This says he made the note in 1006 at Nisibis. He wrote the Chronography in 1019. In 1006 he was bishop of Beth Nuhadra, and he became metropolitan of Nisibis only in December 1008. Paragraph 3 of the brief says so itself, so the brief contradicts itself.
- Evidence: ELI l.90-92 "A. S. 1330, i. e. A. C. 1019, conscripta"; l.8466-8473 (the AH 397 entry, in the canon's last part, which names no sources, l.213-214); l.8578-8583 (bishop of Beth Nuhadra 15 Shebat 1313; metropolitan 26 Kanun I 1320).
- Fix: "Under the Arab year 397, which began in 1006, Elias of Nisibis recorded a split among Christians." Para 2 then opens: "Elias was metropolitan of Nisibis in the Church of the East. He set this down in his Chronography ...". See E-M10 for "the fast".

**E-B2 (records absent_details; card sources.ownWords, uncertain[1]-[2]; brief para 5: missed own words, wrongly recorded as not held).** records.json says of "his other works": "Not held; Assemani names them." That is wrong. Angelo Mai's 1838 Latin of Ebedjesu's collection of church law prints Elias of Soba's preface and chapters on dividing inheritances. Soba is Nisibis (ASS1 l.46116 "Metropolita Sobae"; l.46185 "Episcopus Sobae seu Nisibis"). In that preface Elias prays for the soul of the patriarch Elias I. This is the preface Assemani reasons from: ASS1 l.46207-46212 says it comes "ex ipsius Praefatione in libros de Decisione judiciorum ... quam ex Ebedjesu Sobensi mox referimus".

The same volume also describes a Vatican codex that holds Elias's letter on the Isho'yahb case. That makes it a second held witness for the letter, beside Assemani.

- Evidence:
  - MAI l.398 "Elias Nisibis, auctor praefationis et capitum 24. in tractatu III".
  - MAI l.7402-7412 "religiosissimo Eliae Sobensi, viro nempe accuratissimo et acutissimo ... definitiones illas ... quas religiosissimus Elias Sobensis diligenter et accurate collegit ex opere ... Eliae patriarchae".
  - MAI l.7431-7433 "Sobensis (Eliae) verba hic attexenda duximus".
  - MAI l.7456-7458 "Mar Eliae patriarchae, cuius animae requiem precamur".
  - Mai's note, MAI l.7483 "Hunc ergo tractatum composuit Elias Subensis post obitum Eliae patriarchae".
  - MAI l.8412 "ELIAS SOBENSIS DICIT".
  - MAI l.16356-16360 "epistola mar Eliae metropolitae Nisibis ad episcopos provinciae magnae, ad cives bagdadenses in causa Iesuiabi catholici", followed in the codex by a canon of the synod of Beth Lapat "de iis qui pecunia emunt impositionem manus sacerdotalis".
- Fix, records: replace the absent_detail with a claim for MAI l.7402-7483 and 8412 (Documented). Add a claim for MAI l.16356-16360. Narrow the absent_detail to "The text of his letter against Isho'yahb and his Sessions: not held. Mai describes the letter in a Vatican codex, and Assemani names both."
- Fix, card: add to ownWords "Ebedjesu of Soba, Collection of canons, tract III: Elias's preface and chapters on inheritance (Latin tr. Angelo Mai, 1838)", with the MAI file. Change uncertain[2]'s last sentence to: "The letter itself is not among the sources used here. Angelo Mai describes a Vatican manuscript that holds it."
- Fix, brief para 5 (it now rests on his own words): "When Elias died is not settled. In a preface on dividing inheritances, which Ebedjesu of Soba copied into his book of church law, Elias prays for the soul of the catholicos Elias I. Assemani reasons from this that he outlived Elias I, who died in 1049." Then add the witnesses from E-M1.
- Optional for legacy.remembered: Ebedjesu calls him a most exact and sharp-minded man, and has every reader follow his rulings on inheritance (MAI l.7402-7408).

**E-M1 (brief, para 5; card, dates and uncertain[1]; records contested_claim "When he died": witnesses missed, and a Library header used as a side).** The contested_claim sets Assemani against "the Library header ... gives 1046". The header is project metadata, not a witness. Three held witnesses on the death year were missed, and all of them put it after 1049.
- Evidence:
  - SYN l.1733-1735, J.-B. Chabot (1902): "Élias bar Sinaya, métrop. de Nisibe, mort peu de temps après son homonyme, le patriarche Élias Ier (1049), composa « quatre tomes de décisions ecclésiastiques »".
  - MAC l.617-618, Frédéric Macler (1917): "Elie bar-Sinaya ..., né en 975 J.-C, mort vers 1056".
  - MAI l.7483 (Mai's note).
- Fix, records: replace the second side with "About 1056: Frédéric Macler (MAC l.617-618)". Add Chabot (SYN l.1733-1735) to Assemani's side. Log the header's 1046 as a Library correction, not as a side.
- Fix, brief: after the Assemani sentence, add "J.-B. Chabot agrees that he died soon after. Frédéric Macler puts his death at about 1056."
- Fix, card dates: "Joseph Assemani and J.-B. Chabot put his death soon after 1049; Frédéric Macler gives about 1056."

**E-M2 (card, knownFor: "finished in 1019" told as settled).** M.-A. Kugener, in 1903, dates the Chronicle to 1008 and says it survives in a manuscript of the author's own time.
- Evidence: PO2 l.20047-20048 "La Chronique d'Elie de Nisibe date de 1008, et nous est parvenue dans un manuscrit contemporain de l'auteur, l'add. 7.197 du British Museum." Against it, ELI l.91-92 (Brooks, 1019).
- Fix: knownFor "... a year-by-year record that E. W. Brooks dates to 1019." Add to uncertain: "When he wrote it. E. W. Brooks dates the Chronography to 1019. M.-A. Kugener dates it to 1008, and says the British Museum copy was made in Elias's own time."

**E-M3 (brief, para 4: the witness comes loose from the claim).** "Joseph Assemani ... says Elias stood firm against him. Elias wrote to the people of Baghdad that Isho'yahb had bought his office. From the synods and the Fathers, he argued that the ordination was void." The second and third sentences are told as plain fact. They are Assemani's report of a letter that is not held.
- Evidence: ASS1 l.46187-46192.
- Fix: "Joseph Assemani, writing in 1725, says Elias stood firm against him. In a letter to the people of Baghdad, Assemani says, Elias called Isho'yahb a buyer of his office. He argued from the synods and the Fathers that the ordination was void."

**E-M4 (brief, para 4: Bar Hebraeus has no context, and "he" is ambiguous).** "Bar Hebraeus says he paid the governor" can be heard as Bar Hebraeus paying.
- Fix: "Bar Hebraeus, a later Syriac church historian, says Isho'yahb paid the governor five thousand denarii." Context: the BH3 edition by Abbeloos and Lamy.

**E-M5 (brief, para 2: "E. W. Brooks, its Latin translator").** Brooks translated the first part only. Chabot translated the second, which the closing paragraph quotes.
- Evidence: ELI l.1 ("Pars prior, interpretatus est E. W. Brooks; pars posterior, interpretatus est I.-B. Chabot"); l.8830.
- Fix: "which E. W. Brooks, who put its first part into Latin, dates to 1019."

**E-M6 (card, place: "in the region of Senn").** Brooks's Latin is "e regione Sennae". In Latin, "e regione" with a genitive means "opposite, facing".
- Evidence: ELI l.8573-8574.
- Fix: "Nisibis; earlier Beth Nuhadra. He was ordained priest at the monastery of Father Simeon, facing Senn in Brooks's Latin."

**E-M7 (records contested_claim "Where he was a monk"; card uncertain[5], "His own monastery": no real conflict).** The note says he was ordained priest at Father Simeon's. It does not say he was a monk there, so it does not conflict with Assemani's Saint Michael's.
- Evidence: ELI l.8573-8575; ASS1 l.46184-46186 "in coenobio S. Michaelis apud urbem Mosul ... monachum egit, ut de seipso narrat".
- Fix: delete the contested_claim. Card: "Where he was a monk. Assemani, citing Elias's own words, says he was a monk at Saint Michael's near Mosul. The note says only that he was ordained priest at the monastery of Father Simeon."

**E-M8 (card, uncertain[0]: "Neither is his own account").** Assemani's monastery detail rests on Elias's own words ("ut de seipso narrat", ASS1 l.46185-46186).
- Fix: "His life is told in a note that later hands added to his Chronography, and in Assemani, who draws one detail from Elias's own words."

**E-M9 (card, keyWorks: two wording faults).**
- Chronography: "each year naming its sources". Brooks says "paene ubique", and the last years name none (ELI l.120-121, 213-214). Fix: "and year-by-year tables, most years naming their sources".
- Grammar: "Assemani adds a Syriac-Arabic word list" reads as if Assemani wrote the list. ASS1 l.46293 "Grammaticae subjungitur eiusdem Eliae Nomenclator Syro-Arabicus". Fix: "Assemani says a Syriac-Arabic word list by Elias follows it."
- Four books: Chabot corroborates them (SYN l.1734-1735, "quatre tomes de décisions ecclésiastiques"), and MAI tract III holds part of them (E-B2). Add both to "about".

**E-M10 (brief, para 1: "the fast" is not explained).** A general listener will not know which fast is meant. The entry ends "et Pascha hoc anno in gumada II incidit" (ELI l.8473), so this is the great fast before Easter.
- Fix: "... did not agree on how to reckon the fast before Easter and the feasts."

**E-M11 (card: Ebedjesu, a common name; checklist 8).** "Ebedjesu's catalogue" has no place.
- Evidence: ASS1 l.46213 "ex Ebedjesu Sobensi".
- Fix: "named in the catalogue of Ebedjesu of Soba, as Assemani prints it."

**E-M12 (card, sources: a cited work is missing).** legacy.traces[1] cites the Chronica Minora, but it is not in "Sources". Add it (CM file, "Testimonia Iacobi Edesseni apud Eliam Nisibenum recitata"). Add MAI, SYN, MAC and PO2 if E-B2, E-M1 and E-M2 are taken up.

**E-M13 (card, legacy.remembered[1]: Malech's words loosened).** "Names him among the writers of the Syrian church." Malech lists him among "our own honorable Syrian ancestors" whose short writings tell of the generations of Shem (MAL l.1133-1137).
- Fix: "George David Malech lists him, as Elias Bar Shinaji, among the Syrian forebears whose writings trace their nation from Shem."

**Records, the rest.** All other line numbers and witness labels check out: ELI 8465-8473, 8568-8583, 8566/8601, 8409-8410/8447/8481-8482/8505, 8846-8858, 60320-60342; BH3 15968-15994; ASS1 46183-46216; MARI 10936-10941, 10989-10999; PAR 3104-3105, 3125-3126; CM 19369-19372, 25278-25281; MAL 1136, 15604-15605. The README's line "Elias's life rests on ... Bar Hebraeus and ... Mari" overstates them, since neither speaks of Elias's life (see R-M2).

**Scores.** 346 words, about 2 minutes 10 seconds. FK 6.10, Flesch 74.31. Passes. The longest brief sentence is 24 words. No card sentence is over 22 words.

---

### README and the final sweep

**The sweep, checked.** I compared every WHO row of the era 4 scan table (46 rows, `Who_Scan_Era4.md` l.22-184) and of the supplement's "### Era 4" table (14 rows, l.182-207) with the profile ids.

Era 4 scan, 46 of 46 are covered:
- **Batch 1:** Bede, Boniface (`boniface-of-mainz`), Aidan, Hild, Adomnan, Nennius, Alcuin, Dhuoda.
- **Batch 2:** Maximus, Martin I, Photius, Timothy I, Dionysius of Tel Mahre, Jacob of Edessa, Gregory of Narek.
- **Batch 3:** Theodore of Tarsus, Willibrord, Leoba, Muirchu, Tirechan, Cogitosus.
- **Batch 4:** Jonas, Hincmar, Prudentius, Braulio, Ildefonsus, Humbert, Beuno.
- **Batch 5:** Athanasios, Sophronius, Sebeos, Antony of Choziba, Moses bar Kepha, Alopen, Thomas of Marga, John of Nikiu.
- **Batch 6:** Michael I, Simon I, Alexander II, John III, Agatho (`agathon-of-alexandria`), Severus, Isaac, Yusab (`joseph-i-of-alexandria`).
- **Batch 8:** Adam, and al-Baladhuri. Al-Baladhuri now has a draft at HEAD `c10503d0`, outside this review's scope.

Supplement, 14 of 14 are covered:
- **Batch 3:** Wilfrid (`wilfrid-of-ripon`), Cuthbert.
- **Batch 4:** Julian of Toledo.
- **Batch 7, from its branch:** Symeon, Cedd and Chad, Elipandus and Felix, Paulus Emeritanus, Pisentius and John the Elder, Paul the Deacon, Niketas Stethatos.
- **Batch 8:** Eadburga, Yahya, Elias, Bugga.

Benjamin I, moved from era 3, is in batch 2.

The rulings sections dispose of no WHO row:
- Era 4 scan, "Mark's answers and the coordinator's calls" (l.350-366): John of Damascus WANTED, Charlemagne STORY, Vladimir and Olga LISTED, Heraclius STORY; Adam of Bremen and Nestor go to era 5.
- Supplement, "Calls made by the scan" and "The coordinator's answers" (l.35-72): they only confirm verdicts.
- Decision-Log: "Eras 4 to 7 built in full" (2026-11-14) and the era 5 entry moving Symeon, Yahya and John of Rila to an era 4 supplement (l.2125). John of Rila is LISTED there.

The README's claims about pairing and skipping hold.

**R-M1 (README is stale against the branch).** The README says "Five profiles" and that al-Baladhuri "is not written here; the coordinator and Mark decide". Commit `c10503d0` adds `al-baladhuri.brief.txt`, `.card.json`, `audio/al-baladhuri.audio.txt` and a records.json entry, and leaves the README unchanged.
- Fix: list six ids and give al-Baladhuri's row source (era 4 scan, "WHO (OUTSIDE WITNESS)"). Rewrite the sweep's close: "Every WHO row of both tables is written. Era 4's Who list closes once batch 7 merges." If the al-Baladhuri draft was meant to wait for a ruling, take it off the branch or say so.

**R-M2 (README, "Held witnesses beyond those the scans cite", Elias; and the line on what his life rests on).** The README misses the witnesses found in this review:
- Ebedjesu in Mai's Latin (MAI), with Elias's own preface and Mai's note on the Isho'yahb letter.
- Chabot's Synodicon (SYN l.1733-1735).
- Macler (MAC l.617-618).
- Kugener (PO2 l.20047-20048).

"Elias's life rests on ... Bar Hebraeus and on Mari ibn Sulayman" overstates them. They tell of Isho'yahb and of Elias I, and Mari does not name the metropolitan.
- Fix: add the four witnesses. Reword to "Elias's life rests on the later note and on Assemani. Bar Hebraeus and Mari give the setting of the Isho'yahb affair and of his peace with Elias I."

The README's corrections to the scans are accurate: the 1046 header year, pp. 228-229 as the later-hand note, and Thanet.

---

### Count

- **Blocking: 2.** E-B1 and E-B2, both in elias-of-nisibis.
- **Minor: 22.** Y-M1 to Y-M7 (7), E-M1 to E-M13 (13), R-M1 to R-M2 (2).

| Profile | Words | FK | Flesch | Blocking | Minor |
|---|---|---|---|---|---|
| yahya-ibn-said-of-antioch | 374 | 6.85 | 69.35 | 0 | 7 |
| elias-of-nisibis | 346 | 6.10 | 74.31 | 2 | 13 |
| README and final sweep | | | | 0 | 2 |

I edited no files.

---

## Era 4 Who batch 8, round 1 review: PART C

**Scope.** al-baladhuri (Outside witness): `al-baladhuri.brief.txt`, `al-baladhuri.card.json`, `audio/al-baladhuri.audio.txt`, and the `al-baladhuri` entry of `records.json`, all in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era4/batch8/`. I did not review the other profiles or the README.

**Method.** I read CLAUDE.md and `Who_Profile_Pattern.md`, including the 14-point checklist and the "outside witness" section. For calibration I read the approved outside-witness profiles, `era3/batch3/procopius-of-caesarea.*` and `era3/batch4/agathias.*`, and I used the era 4 batch 6 R1 review as the model for the format. I checked every quote against the vendored file with whitespace and hyphen breaks normalized. I opened every cited line range in records.json and read it in context, and I read the passages the brief draws on but does not cite: Khalid's Damascus terms, the half-the-churches dispute, the Ghutah footnote, and the full Nubia section. I searched all of `cic/texts/` for other witnesses under Baladhuri, Beladhori, Beladori, Beladsori, Baladori, Belâdhorî and Futuh. I diffed the audio script against the brief, ran `engine.m1.gates.grade_text`, and counted words and sentence lengths with a script.

**Files opened (cic/texts/).** BAL = `baladhuri_origins-of-the-islamic-state-v1_hitti1916.txt` (l.140-200 Gottheil's foreword; l.600-930 Hitti's introduction; l.4440-4600 Najran; l.7440-7500 Ghutah and its footnote; l.7885-7945 Khalid's Damascus terms; l.8010-8030 and 8062-8090 the church disputes; l.8100-8180 Saint John's; l.8480-8492 Hims; l.15170-15300 Nubia). The other hits are citations only: `liber-pontificalis_..._duchesne1886.txt` l.162957 ("Le chroniqueur Beladori (fin du ixe siècle)"), `thomas-of-marga_..._budge1893.txt` l.23410-23414, `marco-polo_..._yule-cordier1903.txt` l.23790, `persian-martyr-acts_..._hoffmann1880.txt` l.14425, 15037, 15193, `chronicle-of-arbela_..._sachau1915.txt` l.1141, `rhc-historiens-orientaux_t2-pt1` l.8429, 23002, `book-of-the-himyarites_..._moberg1924.txt` l.10023, and `usama-ibn-munqidh_..._hitti1929.txt` l.658. None of them gives a life, a birth year or a judgment that the profile leaves out. The card's "No source used here gives his birth" holds.

**Quotations.** All quotes match BAL word for word after OCR and line-break normalization:
- "tears down a church will lose his wits" (l.8150-8151)
- "a robe of yellow silk" (l.8154-8155)
- "their persons, religion, lands and possessions" (l.4553-4554)
- "No attempt shall be made to turn a bishop from his office as a bishop" (l.4558-4560)
- "free from exaggeration" (l.774)
- "We know of no better work on the history of the Moslem conquests" (l.920-921), which appears in both the brief and the card

The records.json quote strings also match.

**Audio.** The audio script equals the brief once `[calmly] ` (start of line 1) and `[warmly] ` (start of the last paragraph) are removed. The diff is clean, and there are no tags in the brief or the card. Checklist item 13 passes.

---

### al-baladhuri

**Verdict: one blocking finding (the Nubian terms told as an instance of "the church" in the terms, with nothing to say the Nubians were Christian). The rest are minor fixes.**

**C-B1 (brief, para 3; card, knownFor and legacy.traces[0]: the Nubians are filed under "the church" with no witness).**
- **What is wrong.** The brief says: "In his account of how the Muslims won their lands, the church appears in the terms they made." It then gives two examples, Najran and the Nubians: "Under the terms he reports with the Nubians, they gave slaves each year and received food in exchange." The card's traces[0] reads "terms made with Christian peoples, among them Najran, Damascus and the Nubians", and knownFor says "terms made with Christian peoples".
- **Evidence.** The Nubian terms in BAL (l.15226-15268) are about slaves, food, wheat, lentils, a giraffe and the end of fighting. They say nothing about a church, a bishop or the Nubians' faith. A search of l.15100-15300 for church, Christian, bishop and mosque finds nothing. (Page 379, the opening of Part VIII, is missing from the OCR at l.15204-15206.) No claim in records.json gives a witness that the Nubians were Christian. A listener is told this is where "the church appears" and hears only a slave tribute. That is unsupported as placed, and it leaves a statement with no context.
- **Fix.** Use BAL's own Damascus terms instead. They are church-related, sourced, and they set up the Saint John's story. Bishop and Khalid are both in the source (l.7930-7938).

  > When the Muslims took Damascus, he reports, the general Khalid ibn al-Walid wrote terms at the bishop's request. They promised the people "security for their lives, property and churches".

  Then the card's traces[0] becomes "terms made with Christian peoples, among them Najran and Damascus", and the records claim cites BAL l.7930-7942.

  If the Nubians stay, cite a held witness that they were Christian and say so in the brief. Also drop "the church appears" as the frame for them. The Nubian reports also disagree with each other: Yazid ibn abi Habib says "no treaty or covenant exists. Only a truce" (l.15228-15231), and abu-l-Bukhturi gives four hundred slaves a year (l.15243-15252). Any Nubian sentence should name its reporter.

**C-M1 (brief, para 3: the opening line is a thesis and is vague).** "the church appears in the terms they made" is an abstraction that opens the paragraph, and "they" is unclear (checklist 4). The C-B1 fix replaces it. If any lead-in is kept, make it concrete. For example: "His book also keeps the written terms the Muslims made with Christian towns."

**C-M2 (brief, para 1: the caliphs are given no context; checklist 4 and 8).**
- **What is wrong.** "Mu'awiyah wanted it added to the mosque … 'Abd al-Malik offered them money …" A general listener does not know who either man is. Only al-Walid gets "the caliph". Mu'awiyah is also a common name in this book: Mu'awiyah ibn Hudaij appears at l.15224.
- **Evidence.** "Mu'awiyah ibn-abi-Sufyan came to power" (l.8130-8131), Hitti's footnote "caliph 41-60/661-680" (l.674), "'Abd-al-Malik ibn-Marwan was in power" (l.8142-8143), and "al-Walid ibn-'Abd-al-Malik" (l.8146).
- **Fix.** "The caliph Mu'awiyah wanted it added to the mosque, and they refused. Later the caliph 'Abd al-Malik offered them money, and they refused again. Then his son, the caliph al-Walid, threatened to tear it down."

**C-M3 (brief, para 1: "beside" is not in the source).**
- **What is wrong.** "kept the church of Saint John beside the mosque" places the church, but BAL never does.
- **Evidence.** BAL says only "desired to add the church of St. John to the mosque in Damascus" and "the enlargement of the mosque" (l.8131-8144). Adjacency is an inference.
- **Fix.** "The Christians of Damascus still held their church of Saint John. The caliph Mu'awiyah wanted to add it to the city's mosque, and they refused."

**C-M4 (brief, para 4: a signpost, the story is split, and al-Ghutah is unexplained).**
- **What is wrong.** "His Damascus story goes on." is a signpost beat line. It is needed only because the Saint John's story is split across paragraphs 1 and 4 with Najran in between (checklist 4 and 10). A listener also does not know what al-Ghutah is.
- **Evidence.** BAL l.8157-8172 follows straight on from the demolition. Hitti's footnote at l.7491 says al-Ghutah is "A place in Damascus noted for its orchards". BAL l.7895: "Al-Ghutah and its churches the Moslems took by force."
- **Fix.** Move paragraph 4 so it follows paragraph 2, after the who-line. Open it with the event: "Years later the caliph 'Umar ibn 'Abd al-'Aziz ordered the part taken from the church returned …". End it with: "In return they received the churches of al-Ghutah, an orchard district of Damascus, that had been taken by force."

**C-M5 (brief, para 2, and card dates and uncertain[0] and [4]: "older" and "later" Arab lives, with the real witnesses unnamed; checklist 5 and 9).**
- **What is wrong.** The brief and the card's dates field say "older Arab lives". uncertain[0] says "later Arab lives", and uncertain[4] says "the older lives". The two words describe the same sources from opposite ends, and none of these texts names them.
- **Evidence.** Hitti names them at l.729-734: al-Fihrist, then Yakut's Mu'jam al-Udaba' and al-Kutubi's Fawat al-Wafayat.
- **Fix, brief.** "From al-Fihrist and the lives by Yakut and al-Kutubi, Hitti says, he was Ahmad ibn Yahya ibn Jabir …". This sentence is already 25 words. If it runs long, split it after "Jabir".
- **Fix, card.** Use one wording throughout: "the Arab lives Hitti draws on, al-Fihrist, Yakut and al-Kutubi".
- **Fix, records.** The life claim's witness should be l.729-747, not l.731-746, so that it includes al-Fihrist at l.729-730.

**C-M6 (brief, para 5: Hitti's method sentence is cut short, and it bears on the brief's own lead story).**
- **What is wrong.** "He says al-Baladhuri tries, wherever he can, to rest each fact on its own chain of named reporters." This drops the rest of Hitti's sentence.
- **Evidence.** Hitti's sentence goes on: "yet he sometimes resorts to the other method as he himself acknowledges", that is, combining reports "abridged and pieced up together into one whole". He adds that "Where his store of authorities fails him", al-Baladhuri writes "they said" or "it was said" (l.626-640). The Saint John's story, the brief's opening, is one of those cases. It begins "It is reported" with no chain (l.8130). The outside-witness rule asks how far the account can be trusted, so this is the doubt that touches the story the listener just heard.
- **Fix.** Add after the sentence: "Sometimes, as he says himself, he pieces reports together into one account. The Saint John's story is one he opens only with 'It is reported'."
- **Optional.** Al-Baladhuri weighs his own reports. Al-Haitham ibn 'Adi claimed that Damascus gave up half its churches, and al-Wakidi says Khalid's statement has "no mention in it of 'half the homes and churches'" (l.8016-8023). This is a strong, sourced example of how he handles conflicting witnesses, if room allows.

**C-M7 (brief, para 5: "he" is ambiguous).** "Hitti weighs how far he can be trusted." Heard aloud, "he" can attach to Hitti, and the sentence also announces a topic (checklist 4, status register). Fix: "Hitti, his translator, weighs how far al-Baladhuri can be trusted." Hitti is named, so "translator" here is an identifier and does not stand in for a name.

**C-M8 (brief, para 3: "the Prophet" in narrator prose).** "When the Christians of Najran came to the Prophet, he reports …". The narrator takes over the source's title. Agathias's profile keeps a source's word ("the heretics") out of the narrator's voice, and the same rule applies here. Fix: "When the Christians of Najran came to Muhammad, he reports …". BAL l.4529: "the Messenger of Allah, Muhammad".

**C-M9 (brief, paras 1-2: the time gap is not stated).** The who-line says "ninth century" right after an eighth-century scene. Nothing says al-Baladhuri wrote long after the events, and for an outside witness that gap is part of "how far it can be trusted". Fix: add to para 2, "He wrote well over a century after Mu'awiyah's reign." This rests on BAL l.674 (Mu'awiyah's reign 661-680) and l.742 (his death in 892).

**C-M10 (card, uncertain[4]: a doubt with no one raising it).**
- **What is wrong.** "How he died. Hitti reports from the older lives that he lost his mind from drinking anacardia juice. That story also explains his name." The pattern says each doubt names who raises it and why. Calling the account "that story" implies a doubt that no held witness raises.
- **Evidence.** Hitti gives the death and the surname without question (l.742-744).
- **Fix.** Either drop the item, since the brief and dates already carry the death, or reword it: "How he died. Hitti reports it from al-Fihrist, Yakut and al-Kutubi and does not question it: he lost his mind from drinking anacardia juice, in Arabic baladhur, which gave him his surname."

**C-M11 (card, uncertain[3]: a strength filed as a doubt).**
- **What is wrong.** "Hitti says he mostly follows the tradition of Medina …" sits under uncertain without Hitti's reason. Hitti presents it as a strength.
- **Evidence.** "the tradition of al-Madinah, which for obvious reasons is more reliable than that of al-'Irak, forms the basis of his works" (l.649-652). The "lost works" half is "most of whose works are either unknown to us or have entirely disappeared", and it is said of his favorite authorities (l.904-909).
- **Fix.** "His sources. Hitti says his works rest on the tradition of Medina, which Hitti judges the more reliable. Most of the works of his favorite authorities, Hitti adds, are unknown or lost."

**C-M12 (card, keyWorks[0]: the quantifier is too strong).** "with the terms made with each people" is stronger than the book. Many conquests are told without terms, and some are told as "by force". Hitti gives the reason such books were written: whether a land was taken "by peace", "by capitulation" or "by force", "and what the terms in each case were" (l.698-703). Fix: "the conquests, land by land, and whether each was taken by force or by terms, with many of the terms written out."

**C-M13 (card, legacy.remembered[0]: al-Mas'udi has no context in the card).** The card is its own text, and here al-Mas'udi appears bare. The brief gives "the later historian". Fix: "Al-Mas'udi, a historian of the next century, as Hitti quotes him: …". Basis: BAL l.917 "al-Mas'udi (d. 346)", against al-Baladhuri's death in 279. "The later historian al-Mas'udi" is also fine.

**C-M14 (records.json: the Nubia line range stops short).** The Nubia claim cites "l.15235-15249", but abu-l-Bukhturi's quoted words run to l.15252 ("for whom they shall receive food in exchange", l.15251-15252, after the page break at l.15249). Fix: "l.15235-15252". If C-B1 replaces the Nubians, add the Damascus terms claim: "security for their lives, property and churches", BAL l.7930-7942, Documented.

**Checks that pass.**
- Tradition reads "Outside the church", and the label is present beside the role.
- The card is in Mark's order, and no field is filled in for something missing.
- What is uncertain opens with the brief's caveat.
- Hitti and Gottheil are each credited correctly: the "shortened edition" is Gottheil's (l.179) and the "digest" is Hitti's (l.745). There is no witness swap with al-Baladhuri's own informants.
- There is no "what they fought for" beat, and no polemicist question arises.
- American spelling holds, and I found no "not X but Y", colon-reveal, rhetorical question or aphorism.
- The closing quote adds a fact and is not a beat line.
- The death in 892, his Persian descent, the friendship with caliphs, Ansab al-Ashraf with "only two volumes", Yakut reproducing "a great part", and later historians drawing "freely" all match the text.
- I found no false absence. A search of all of `cic/texts/` gives no birth year and no other life.

**Scores.**
- Length: 367 words, about 2 minutes 15 seconds, at the cap.
- Readability: `grade_text` gives FK 7.00 and Flesch 71.54. Passes.
- Sentence length: the longest brief sentence is 25 words ("From older Arab lives …"). All the others are 24 words or fewer, and the card's sentences are within 25 words.
- The fixes above add about 40 words and cut about 15. To stay near 365, trim para 2's translation sentence or the Najran bishop line.

---

**Summary: 1 blocking finding (C-B1) and 14 minor findings (C-M1 to C-M14).**
