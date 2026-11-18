# R2 recheck: era 3 batch 3

Scope: only what changed, checked against `R1_review.md` and `R1_changes.md`. Text that did not change was not reviewed again. I read the changes as a word diff from `8a5c8b09` (the version R1 reviewed, "all ten drafts, records and README for review") to `61dd8f97` (HEAD), limited to `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era3/batch3/`. I opened every new or changed sentence, quotation, identifier and `records.json` entry at its line in the vendored file. I checked who is speaking at each line: the ancient writer, a document he quotes, the translator, or an editor's note, bracket or apparatus. The OCR files (Braun's Persian martyr acts, Labourt, Nikodemos's Synaxaristes, Migne PG 88, 99 and 147, the Acta Sanctorum, Assemani, Mommsen's Chronica minora II, Nau PO 8) were read by line and searched tolerantly. Before accepting each new absence or limit I searched the Library. I did not edit the drafts, and I made no paid calls, model-API calls or web requests. Line numbers point to files under `cic/texts/` unless another path is given. Brief line numbers count blank lines, so paragraphs sit on l.1, 3, 5, 7 and so on.

Mechanical checks, all ten:
- Each audio script equals its brief once `[calmly] ` and `[warmly] ` are removed (checked by script; three briefs carry one extra trailing newline, which is not text). Each starts with `[calmly]` and has one `[warmly]`, before the closing paragraph. No tag appears in a brief or card.
- `grade_text` passes for all ten (FK at most 10, Flesch at least 60). Marcellinus (60.8) and Vigilius (61.1) sit nearest the floor.
- Sentences: no new or changed narrator sentence runs past about 25 words. The longest new ones are Mar Aba l.9, "A letter in Mar Aba's name calls marriage a bond of love in the chaste and lawful union of a man and a woman." (24), and Procopius l.5, "It tells how Belisarius suspected Silverius, the chief priest of Rome, of plotting with the Goths." (16).
- `briefLength` matches on all ten. All ten cards and `records.json` parse as JSON, and `records.json` has exactly the ten ids. Every `file` named in a card's sources exists under `cic/texts/`, including the new ones (Nicephorus PG 147; Liberatus PL 68; PG 99, the Acta Sanctorum and the Synaxaristes on Romanos; Williams's Gildas and the Maassen `ownWords` on Samson; Braun and Labourt on Mar Aba; Labourt on Cosmas; Evagrius on Barsanuphius).

| Profile | Words | Est. length @162 | FK | Flesch | Cap |
|---|---|---|---|---|---|
| Theodora, wife of Justinian (MAJOR) | 405 | 2:30 | 6.8 | 67.3 | 405, at the cap |
| Marcellinus Comes | 325 | 2:00 | 7.8 | 60.8 | 325, at the cap |
| Procopius of Caesarea | 324 | 2:00 | 7.6 | 63.3 | within |
| Vigilius of Rome (MAJOR) | 405 | 2:30 | 8.2 | 61.1 | 405, at the cap |
| Romanos the Melodist | 325 | 2:00 | 7.9 | 68.8 | 325, at the cap |
| Samson of Dol | 325 | 2:00 | 6.2 | 73.4 | 325, at the cap |
| Mar Aba I (MAJOR) | 402 | 2:29 | 6.6 | 72.3 | within |
| Cosmas Indicopleustes | 320 | 1:59 | 7.3 | 68.7 | within |
| Barsanuphius and John of Gaza | 322 | 1:59 | 6.4 | 71.6 | within |
| Cyril of Scythopolis | 322 | 1:59 | 6.7 | 70.7 | within |

## 1. The 11 R1 blocking findings

| Finding | Status | Evidence |
|---|---|---|
| B-B1 (Vigilius: the Book of the Popes' life called hostile) | RESOLVED | Brief l.3: "Its life of Vigilius tells of Romans who called him a murderer. It also shows him stand up to the empress." Loomis: "Far be this from me, Lady Augusta… I do assuredly refuse to restore a man who is a heretic" (l.11646–11648); "We declare him to be a murderer" (l.11659–11660). Card `remembered` 1 ("a mixed life… dragged from an altar rather than yield"; l.11761–11762, 11815, "partly legendary" l.11834) and `uncertain` 1 ("calls often partisan in this part": "This portion of the Liber Pontificalis is often fraudulent, often partisan", l.575–576, where the portion is the book up to the seventh century, l.546–548). Records witness matches. |
| B-B2 (Vigilius: a false "only" on Silverius's death) | RESOLVED | Card `uncertain` 4 as R1 worded it. Loomis: "took Silverius as if in his own charge… fed him with the bread of tribulation" (l.11443–11471, the quoted words exact at l.11470); Liberatus via Loomis, "turned over to the guards of Vigilius, who transported him to the island of 'Palmaria,' where he died of starvation" (l.11487–11488); "The guilt seems to rest partly upon her and partly upon Vigilius" (l.11491–11492). The new `contested_claim` holds all four sides. |
| B-B3 (Vigilius: Liberatus ch. 22 "not located") | RESOLVED | The absent detail is gone. "CAPUT XXII. De Silverio et Vigilio" (PL 68 l.81553–81554) and the editor's note "ut Vigilio… tanto majorem faciat invidiam" (l.81654–81657) are cited in the records; the Breviarium (PL 68) is in `sources.about`. |
| B-B4 (Romanos: Pitra's attribution told as settled) | RESOLVED | Brief l.3: "Cardinal Jean-Baptiste Pitra, who printed it in 1888, calls it the Menologion of the emperor Constantine Porphyrogenitus. Migne's edition of Theodore the Studite gives the same Vatican manuscript to the emperor Basil." Pitra: "Ex Menologio imperatoris Constantini Porphyrogeniti… sub num. 1613" (l.6791–6793); PG 99: "Ex Menologio Basilii imperatoris. Cod. Vatic. n. 1613." (l.7839), a heading the edition prints. Records: Pitra's claim Contested, a `contested_claim` added. The card overstates two of the Basil witnesses (N2). |
| B-B5 (Romanos: false absence; the Synaxaristes) | RESOLVED | The absent detail is reworded ("A witness older than the Menologion notice"). Brief l.5: "A later Greek book of saints, revised by Nikodemos the Hagiorite, names his home city as Emesa." Synaxaristes: "κατήγετο άπό την Συρίαν, πατρίοα έχων τήν πόλιν "Εαεσαν, ή ότοία τώρα λέγεται τουρκιστί Έμσ" (l.13993–13995); the file header says the work was first written by Maurikios and "corrected and annotated by Nikodemos", so "revised" holds. Card `place`, `dates`, `uncertain` 2 (whose "much later than the Menologion" holds: Nikodemos, 1748/9–1809, file header) and the records carry it. The year 496 was declined; see section 3. |
| C-B1 (Mar Aba: the Life is held) | RESOLVED | Card `uncertain` 1: "His Life, by a disciple in J. Labourt's judgment, is held in Oskar Braun's German translation from Paul Bedjan's Syriac". Braun: "Bedjan, Histoire, S. 206 ff." (l.838), "Geschichte der wunderbaren und göttlichen Kämpfe des heiligen Zeugen Mär Abä" (l.842–844); Labourt: "l'auteur de l'Histoire de Maraba était réellement, comme il le prétend, un disciple du catholicos" (l.9559–9561). The author "Anonymous disciple" in `sources.about` holds: Labourt, "dit le rédacteur anonyme de sa Vie" (l.9491), and no held file names him. The nine new records claims match Braun l.10670–10678 ("machten sie ihn zum Arzabed"), l.10826 ("im Dorfe 'KD"), l.10833–10885 (Nisibis; Edessa, "in der griechischen Sprache unterwiesen"), l.12238 ("nach neun Jahren"), l.12285–12322 ("neben der Kirche von Bet Narkös… am Freitag der zweiten Fastenwoche"), l.12350–12355 ("bis zum Kloster von Seleucia") and Labourt l.9483–9492, 10930–10931 ("le 29 février 552, à Séleucie"), 9843–9844. One typo in a changed records claim (N5). |
| C-B2 (Mar Aba: baptism and burial told one way) | RESOLVED | Brief l.7: "A Life of Mar Aba survives, which Chabot says needs careful critical study. It has him baptized in the village of Akda, a student at Nisibis, a learner of Greek at Edessa, and later a teacher." Braun l.10826; Labourt "Au bourg d''Akda, d'après sa Vie, p. 211; à Hira, d'après MARE" (l.9556); "il passa un certain temps dans l'enseignement" (l.9817–9818). Brief l.13: "The Life has him regain the king's favour and die of illness": the king lets him live where he will and sends doctors who cannot heal him (Braun l.12287, 12319–12320). Brief l.15: "The Life has him buried in the monastery of Seleucia." (l.12350–12355). Card `place` drops Hira; the new `uncertain` items and both `contested_claims` match Braun's note "Nach Mare, S. 45… in Hira beigesetzt" (l.12361–12362). |
| C-B3 (Cosmas: the census placing misread) | RESOLVED | Card `tradition` "Aksumite Christianity": the census movement `aksumite-christianity`, name "Aksumite Christianity", `people` "Cosmas Indicopleustes", year 522 (`cic-website/data/world-census.json`). README l.11 as R1 worded it; McCrindle "That to which Cosmas most probably belonged was the Nestorian" (l.781–782). |
| C-B4 (Barsanuphius: Evagrius held) | RESOLVED | Brief l.5: "The church historian Evagrius Scholasticus calls Barsanuphius an Egyptian, shut in a cell near Gaza. No one had seen him for over fifty years, Evagrius says." Evagrius IV.33: "First, Barsanuphius, an Egyptian… in a certain seat of contemplation near the town of Gaza… enclosed in a chamber, although for fifty years and more from this time he has not been seen by any one" (l.9262–9271); the chapter follows the account of Justinian and the factions (l.9245–9253), "at that season" (l.9260), which supports the card's "in Justinian's reign". Nau: "au vi siecle" (po08 l.11423), "Dorothée est né vers 540" (l.11524). The rewritten `absent_details` notes now match. |
| C-B5 (Barsanuphius: Gallandi's notice credited to Migne) | RESOLVED | Brief l.5 "as Andrea Gallandi's notice reports it"; card, records and README now give the report to Gallandi and the heading "ANNO DOMINI DXCVI" (PG 88 l.121945) to Migne. Source line "(Galland., Veterum Patrum Biblioth., tom. XII, Proleg.…)" (l.121951); the first name is held, "ANDREAS GALLANDI" (`tatian_oratio-ad-graecos-grc-lat_otto1851.txt` l.20101). The notice says the Life of Dositheus was written by Dorotheus's disciple ("perhibet ejus discipulus qui vitam sancti Dosithei conscripsit", l.121955–121956), which the brief's "a Life of Dositheus" does not contradict. |
| C-B6 (Cyril: "survives whole") | RESOLVED | Brief l.5: "Jean-Baptiste Cotelier printed his Life of Euthymius the Great with a Latin translation in 1681." The completeness claim is gone; brief and card `uncertain` 3 now agree. "his" follows a paragraph whose subject is Cyril. |

## 2. R1 minor findings

**Theodora, wife of Justinian**
- A-M1: RESOLVED. Brief l.3 "John wrote from the side she sheltered."; card `uncertain` 1 and 2 and records as worded. Payne Smith l.287–290.
- A-M2: RESOLVED. "The twelfth-century Michael the Syrian, a patriarch of John's church, made her…"; card `uncertain` 1 adds Michael "from the same side". Chabot's title, "patriarche jacobite d'Antioche" (tome 2 l.37–40).
- A-M3: RESOLVED. "She ends by approving an ancient saying, 'royalty is a good burial-shroud.'" Dewing l.3121–3122.
- A-M4: RESOLVED. "she hid him in her palace for years." Card `legacy.traces` 3 the same; `uncertain` 5 keeps both sides.
- A-M5: RESOLVED. `contested_claim` "How long Anthimus stayed hidden" added as worded.
- A-M6: RESOLVED. Brief l.9, card `knownFor` and `legacy.traces` 2 now place Theodore at Hirtha of the Saracens (Lives l.26745–26748).
- A-M7: RESOLVED. Card `uncertain` 2: "Nicephorus Callistus, a later Greek church historian, says Cyprus was her homeland." PG 147: "ἐπὶ δόξῃ τῆς γαμετῆς Θεοδώρας Κύ-/rp0) δλαχούσης πατρίδα" (l.9789–9790), "εἰς τιμὴν τῆς γαμετῆς Θεοδώρας τῆς Βασιλίδος· ἐχεῖδεν γὰρ ὥρμητο" (l.14764–14765), Latin "conjugis su: Theodore Auguste inde orta" (l.14727). Source entry, records claim (Contested) and contested side added. The records quote normalises the OCR, as R1's did.
- A-M8: RESOLVED. "empress from his accession, in 527 by H. B. Dewing's year." Records claim added.
- A-M9: RESOLVED. "Evagrius offers two reasons…".
- Length: RESOLVED. The Hormisdas visits sentence left the brief; 405 words.

**Marcellinus Comes**
- A-M10: RESOLVED. "They were struck down in the church, he writes, and taken to prison, where they died." Mommsen l.8305–8306. Records claim added.
- A-M11: RESOLVED. "Mommsen dates it from 379 to 518. Later Marcellinus added sixteen more years, up to 534." Card `dates` also fixed ("in Theodor Mommsen's years for the consulships his preface names").
- A-M12: RESOLVED in the brief ("One of the two families of manuscripts runs on to 548.") and `uncertain` 4. The card wording R1 supplied for `legacy.traces` 1 calls the two copies lost, which Mommsen does not say (N1).
- A-M13: RESOLVED. "under the emperor Justin, before 527."

**Procopius of Caesarea**
- A-M14: RESOLVED. Brief l.1 is two sentences; l.5 split with A-M15.
- A-M15: RESOLVED. "It tells how Belisarius suspected Silverius… He sent him away to Greece and put Vigilius in his place." Wars V.xxv l.3473–3476.
- A-M16: RESOLVED. The thesis sentence is deleted.
- A-M17: RESOLVED. "Dewing says the Buildings is written in the style of a fawning flatterer, but is still a storehouse of facts." Dewing l.181–182, 190–191.
- A-M18: RESOLVED. "Dewing says it is now believed highly probable that he did." Dewing l.168.
- A-M19: RESOLVED. "at times like a man steeped in the old religion of Greece."
- A-M20: RESOLVED. Both pronouns are now "Procopius".
- A-M21: RESOLVED. New card `uncertain` "His birth" gives all three: 1896 translator "towards the beginning of the sixth century" (l.45–46); Buildings preface "early in the sixth or at the end of the fifth century" (l.97–98).
- A-M22: RESOLVED. "Dewing says his work went on till near the end of Justinian's life" ("His own activity continued till well nigh the end of Justinian's life", l.81–82); `legacy.traces` 2 now quotes Dewing exactly (l.190–191).
- A-M23: RESOLVED (reworded). The process narration is gone. The drafter's reason for not taking "kept out of its disputes" holds. The new words go slightly past the passage they cite (N4).

**Vigilius of Rome**
- B-M1: RESOLVED. "in Cecilia's church in Rome".
- B-M2: RESOLVED. "and that she offered him gold"; card `uncertain` 2 the same, and "Liberatus and Victor are both hostile to him".
- B-M3: RESOLVED in the brief (the sentence is gone) and the records (both claims Contested; the 555 claim marked as Duchesne's bracket for "the third indiction", Loomis l.11934–11936; the Marcellinus note, Mommsen l.3260–3263, added). The card's `dates` and `uncertain` 6 still give 555 as the record's own year and lack the new side (N3).
- B-M4: RESOLVED (reworded). The pronoun now points to Vigilius. The drafter's reason for dropping "first resisting their condemnation", that no held line shows a resistance before 548, does not hold: Loomis's note says "Vigilius was commanded in Constantinople to give the edict his approval. He resisted stubbornly for a while… But at length, in 548, he issued… the Judicatum" (l.11787–11789). The new text ("condemning them in 548, defending them in his Constitutum of May 553, and condemning them again that December") is true as it stands and needs no change; it simply begins in 548.
- B-M5: RESOLVED. "(the continuation of the chronicle of Marcellinus Comes; Louis Duchesne, as Loomis reports, gives 20 March 537; Procopius of Caesarea gives no year)". Loomis "Vigilius was ordained March 20, 537. Duchesne" (l.11352–11353).
- B-M6: RESOLVED. "In that letter to Eutychius, Vigilius pointed to Augustine of Hippo…".

**Romanos the Melodist**
- B-M7: RESOLVED. "came to Romanos the Melodist in his sleep".
- B-M8: RESOLVED. Brief l.9 "He set a Latin prose version beside the Greek, and the words here are from it."; card `uncertain` 3 "quoted here only in Pitra's Latin prose version, not in Romanos's Greek."
- Length: RESOLVED. 325 words.

**Samson of Dol**
- B-M9: RESOLVED. "Samson of Dol heard people worshipping".
- B-M10: RESOLVED. "from accounts the deacon Henoc brought"; card "brought from overseas". Taylor l.1992–1997.
- B-M11: RESOLVED. "rejected what its writer says of its authorship and origin." Taylor l.1652–1654.
- B-M12: RESOLVED. Two sentences, 13 and 22 words.
- B-M13: RESOLVED. Card `uncertain` 2 adds Williams: "cannot be anterior to the seventh century… neither can it be later than Nominoe, hat is, than 824" (l.18737–18740). Records claim, contested side and source entry match.
- B-M14: RESOLVED. `sources.ownWords` holds the Paris signature, "if the signer is he".

**Mar Aba I**
- C-M1: RESOLVED. "a follower of the old Persian religion"; Braun l.10670–10678 ("ursprünglich Heide").
- C-M2: RESOLVED. "The magi turned against him". Gismondi l.14016.
- C-M3: RESOLVED. "a father's wife"; the letter sentence is 24 words.
- C-M4: RESOLVED. "now Azerbaijan" is gone.
- C-M5: RESOLVED. "tells his conversion, his wonders, his trial before the king and his death."
- C-M6: RESOLVED. "whose synod, dated by J.-B. Chabot to 544"; `keyWorks` "(dated by Chabot to 544)".
- C-M7: RESOLVED. No narrator sentence past 25 words.

**Cosmas Indicopleustes**
- C-M8: RESOLVED. "…are, in J. Labourt's words, precious evidence for the spread of the church of Persia in his day." Labourt "des renseignements précieux sur l'extension de l'Église de Perse à cette époque" (l.9619–9621). The records claim's 547 and 520–525 match l.9618–9619.
- C-M9: RESOLVED. "the emperor Justin I, as McCrindle identifies him"; McCrindle "Justinus I, or the Elder" (l.4083).
- C-M10: RESOLVED. "an eyewitness account of Adulis and Ethiopia and reports of Ceylon and the trade of India".

**Barsanuphius and John of Gaza**
- C-M11: RESOLVED. "J.-P. Migne prints the questions and answers among Dorotheus's writings, in Greek and Latin."
- C-M12: RESOLVED. "Their heading".
- C-M13: RESOLVED. "When a thought told him… Dorotheus cursed the thought and went anyway. Often John gave the very answer…" Migne l.127969–127979.
- C-M14: RESOLVED. "whose written answers guided Dorotheus of Gaza; the questions he put to them survive".
- C-M15: PARTLY. The source's form ("Antonium, Ephraim", l.122200) is kept in brief and card, as asked. The Open-Gaps line the finding calls for is not yet written; `R1_changes.md` leaves it "for the Open-Gaps entry", which is the batch's closing entry, as for batch 2's Sigebert. It must go in that entry.

**Cyril of Scythopolis**
- C-M17: RESOLVED. "He met many old monks of the desert". Cotelier "cum incidissem in multos" (l.45463–45464).
- C-M18: RESOLVED. `keyWorks` "the life of the monk Euthymius the Great…".
- C-M19: RESOLVED. "Euthymius the Great" in brief l.5 and card `knownFor`; "magnus Euthymius" (l.45601).
- C-M20: RESOLVED. "by leave of the solitary John, whom he calls a bishop"; records the same.

**README**
- C-M16: RESOLVED. "Migne heads the notice on him 'ANNO DOMINI DXCVI'; the notice, Andrea Gallandi's, reprinted by Migne, reports…, and François Nau puts his birth about 540." Nau po08 l.11524.

## 3. The declined and reworded points

- **Romanos, the year 496 (B-B5).** The reason holds. The OCR reads "έν έτε: υν-' 196" (Synaxaristes l.13999). Neither the Greek numeral nor the figure can be read with confidence (the letter after υ is printed as ν, which would give 450, and "196" may or may not be 496), no page image is held, and R1 itself asked for the page to be read before quoting. Leaving the year out of brief, card and claim, and saying why in the records, is the faithful choice. The emperor and Emesa, which are legible, are used.
- **Vigilius, B-M4.** The reword fixes the pronoun and is true. The stated reason (no held line for resistance before 548) is wrong (Loomis l.11788), but nothing in the new text needs to change; see section 2.
- **Procopius, A-M23.** The reason holds: Wars V.iii does not say he kept out of the church's disputes, only that he would not record the points of faith. The replacement goes a little past the passage the other way (N4).

## 4. New findings

- **N1 MINOR (`marcellinus-comes.card.json` `legacy.traces` 1; item 1; carried by R1's own fix wording).** "All the manuscripts come down from two lost early copies, Mommsen says." Mommsen does not call them lost. He says the chronicle comes down in two books, the Saint-Omer manuscript and the Tilianus, which stand for two archetypes close to the author's own time, and that the Tilianus, which runs on to 548 and breaks off, "ipse scriptus est saeculo eo quo auctor vixit": "Marcellini comitis chronica tradita habemus libris duobus Omerensi et Tiliano, quibus repraesentari archetypa duo auctori fere aequaeva… Tilianus… narrationem continuans ad a. 548, ubi desinit mutilus, ipse scriptus est saeculo eo quo auctor vixit" (`chronica-minora-2_…_mommsen1894.txt` l.3717–3721). Fix: "All the manuscripts come down from two early copies of nearly the author's own time, Mommsen says. One ends at 534, where the preface says it ends; the other runs on to 548, where it breaks off." The brief and records need no change.

- **N2 MINOR (`romanos-the-melodist.card.json` `uncertain` 1; `records.json`, `romanos-the-melodist`, the claim "Vatican codex 1613 is the Menologion of the emperor Basil"; item 1; carried by R1's own fix wording).** The card says "Migne's edition of Theodore the Studite and the Bollandists give the same Vatican manuscript, number 1613, to the emperor Basil." Only PG 99 names the manuscript: "Ex Menologio Basilii imperatoris. Cod. Vatic. n. 1613." (`theodore-studite_…migne1860.txt` l.7839). The Bollandists cite "Menologio Graecorum, jussu. Basilii Porphyrogeniti Imperatoris seculo Christi decimo conscripto" (`acta-sanctorum_martii-tomus-3…` l.180301–180302), with no manuscript or number; the file has no "1613" for it. Assemani likewise cites "Menologio Graecorum, quod Basilii Porphyrogeniti Imperatoris jussu prodiit" (l.39715–39716), and the Studia Biblica essay "the menologion of Basilius II (976-1025) in the Vatican Library" (l.16385–16386); neither gives the number. The records claim lists all four as witnesses that codex 1613 is Basil's. The brief is right ("Migne's edition of Theodore the Studite gives the same Vatican manuscript to the emperor Basil"). Fix, card `uncertain` 1, second sentence: "Pitra calls it the Menologion of the emperor Constantine Porphyrogenitus, who reigned from 944 to 959 in Samuel Cross's dates. Migne's edition of Theodore the Studite gives the same Vatican manuscript, number 1613, to the emperor Basil, and the Bollandists cite a Menologion made by order of the emperor Basil Porphyrogenitus." Records: make the claim "PG 99 heads an extract 'Ex Menologio Basilii imperatoris. Cod. Vatic. n. 1613'", witness PG 99 l.7839, Contested; add a second claim "The Bollandists and Assemani cite a Menologion of the Greeks made by order of the emperor Basil Porphyrogenitus; the Studia Biblica essay names a menologion of Basil II in the Vatican Library", with those three witnesses, Contested. In the `contested_claim` "Whose Menologion holds the notice", end the second side: "the Menologion of the emperor Basil (PG 99 names Vatican 1613; the others give no number)."

- **N3 MINOR (`vigilius-of-rome.card.json` `dates` and `uncertain` 6; items 1, 7, 12; card left behind the B-M3 records fix).** `dates`: "a record of the time that Loomis reports gives 7 June 555"; `uncertain` 6: "7 June 555 in the record of the time Loomis reports, the end of 554 or the start of 555 in Percival." The record gives "the seventh day before the Ides of June in the third indiction"; "(June 7, 555)" is Duchesne's bracket (Loomis l.11934–11936). The B-M3 fix now says so in the records, and adds the chronicle note printed with Marcellinus, "Indictione II. XIII p. c. Basilii" (Mommsen l.3260–3263), to the `contested_claim`. The card still gives the editor's year as the record's and omits the third side, so card and records disagree. Fix, `dates`, last sentence: "Died in Sicily on his way home. A record of the time that Loomis reports gives 7 June in the third indiction, 555 by Louis Duchesne's reckoning; Henry Percival gives the end of 554 or the start of 555". `uncertain` 6: "The year of his death. A record of the time that Loomis reports gives 7 June in the third indiction, 555 by Duchesne's reckoning. A chronicle note printed with Marcellinus Comes gives the second indiction, the thirteenth year after Basil's consulship. Percival gives the end of 554 or the start of 555." The brief needs no change.

- **N4 MINOR (`procopius-of-caesarea.card.json` `uncertain` 1; item 1; the A-M23 reword).** "Outside the church marks him as a historian who reports on the church and, by his own word, would not set down its disputes". Procopius does set down the church's disputes: the envoys who came "about a tenet of faith, which is a subject of disagreement and controversy among the Christians", and Silverius's removal. What he declines is the doctrine: "As for the points in dispute, although I know them well, I shall by no means make mention of them" (`procopius_wars-5-6-gothic_dewing1919.txt` l.407–408). The brief has it right ("He knew the points well, he writes, but would not record them."). Fix: "…and, by his own word, would not set down the points of faith in dispute; it makes no claim about his faith."

- **N5 MINOR (`records.json`, `mar-aba-i`, l.440; a typo in a changed claim).** "edited by Bedjan (1895) and held in Braun's German,, 'aurait besoin…'". Fix: one comma, "held in Braun's German, 'aurait besoin…'".

No new or changed quotation is misquoted. I found no new absence claim that a held file contradicts, no work called anonymous where an editor prints a name (the Life of Mar Aba's "rédacteur anonyme", Labourt l.9491; the Life of Samson, Taylor; the PG 88 preface), no witness swap, and no contested point told as settled in a brief. Every common name in the new text carries a place or role at first mention: Evagrius Scholasticus, Andrea Gallandi, Nikodemos the Hagiorite, Justin I, Euthymius the Great, Theodore of Hirtha, Marcellinus Comes and Procopius of Caesarea on the Vigilius card. No new sentence has an ambiguous pronoun, and none reads as an AI tell.

## Totals

R1 findings: of 11 blocking, 11 RESOLVED. Of 57 minor, 56 RESOLVED and 1 PARTLY (C-M15: the source's form is kept; the Open-Gaps line is owed in the batch's closing entry). None is NOT RESOLVED. The declined year 496 on Romanos is sound. The reasons for the Vigilius B-M4 and Procopius A-M23 rewordings are judged in section 3; neither leaves a fault in the brief.

New: 0 blocking, 5 minor (N1 `marcellinus-comes` card; N2 `romanos-the-melodist` card and records; N3 `vigilius-of-rome` card; N4 `procopius-of-caesarea` card; N5 `records.json` for `mar-aba-i`). N1 and N2 come from R1's own fix wording, and N3 from a records fix that left the card behind. None touches a brief or an audio script. Every fix above was checked against the line it cites.

Verdict: clear. No blocking point remains. The five new minors and the C-M15 Open-Gaps line are card, records and logging fixes that need no further review round.
