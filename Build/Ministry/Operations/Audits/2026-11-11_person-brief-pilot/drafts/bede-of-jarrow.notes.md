# bede-of-jarrow notes

File: B = /home/user/CIC-Project/cic/texts/bede_ecclesiastical-history-english-people_giles1903.txt (Giles edition, 1903). Line numbers are file lines.

## Claim table
| Claim | File : line | Support |
|---|---|---|
| Born on the monastery's land at Wearmouth and Jarrow | B:15420-15423 | "who being born in the territory of that same monastery, was given, at seven years of age, to be educated by the most reverend Abbat Benedict" |
| Given at seven to Abbot Benedict | B:15422-15423 | same passage |
| Spent the rest of his life there, Scripture, discipline, daily singing | B:15424-15428 | "spending all the remaining time of my life in that monastery, I wholly applied myself to the study of Scripture, and amidst the observance of regular discipline, and the daily care of singing in the church" |
| Commentaries compiled from the Fathers | B:15433-15436 | "to compile out of the works of the venerable Fathers, and to interpret and explain according to their meaning these following pieces" |
| History written for King Ceolwulph; opens by naming helpers | B:113-128, 144-152 | Preface "To the most glorious king Ceolwulph"; "I will take care briefly to intimate from what authors I chiefly learned the same" |
| Abbot Albinus trained at Canterbury, chief encouragement | B:154-158, 190-191 | "learned and reverend Abbot Albinus; who, educated in the Church of Canterbury"; "chiefly encouraged to undertake this work by the persuasions of the same Albinus" |
| News of Kent through Nothelm, a priest of London | B:157-161 | "transmitted to me by Nothelm, the pious priest of the Church of London" |
| Nothelm searched Roman archives for Gregory's letters | B:163-171 | "searched into the archives of the holy Roman Church, found there some epistles of the blessed Pope Gregory, and other popes" |
| Northumbria: no single author, "innumerable witnesses", plus own knowledge | B:216-224 | "I received not from any particular author, but by the faithful testimony of innumerable witnesses... besides what I had of my own knowledge" |
| Whitby: Oswy heard Colman, who kept the Easter received from his elders | B:7975-7990 | "The Easter which I keep, I received from my elders" |
| Wilfrid spoke for Rome | B:7992-8010 | Agilbert: "I desire that my disciple, the priest Wilfrid, may speak in my stead" |
| Oswy would not oppose Peter, the door-keeper; Colman went home | B:8195-8215, 8230-8233 | "he is the door-keeper, whom I will not contradict"; "Colman... went back into Scotland" |
| Of Aidan, Bede writes with love yet detests his Easter | B:6985-6990, 7009-7010 | "very much detesting the same"; "These things I much love and admire in the aforesaid bishop" |
| Cuthbert, a pupil, described his death; Ascension Day 735; just finished the Gospel of John | B:15613-15617 | "the scene at his deathbed is depicted for us by Cuthbert, his pupil... It was on Ascension Day, 735, at the age of sixty-two, that Bede died, having just completed his translation of the Gospel according to St. John" |

## The quote
B:15428-15429, printed across two lines: "I always took delight in learning, teaching, and writing." Verified character for character after joining the line break. No trimming.

## Contested or uncertain
- The death claim does not come from Cuthbert's letter. The edition does not print that letter. It comes from the editor's Biographical Notice at the end of the volume (B:15595-15620), which is not Bede's own and is unsigned. The brief says only that Cuthbert described the death; it gives no detail of the scene because none is in the file.
- Bede's bias: the brief calls the History "no neutral guide" and shows it through his own words about Aidan's Easter (B:6985-6990) and a line on the Britons (B:15174-15178, "through innate hatred, are adverse to the English nation"; not used in the final text for length).
- The Easter dispute itself: told only from Bede's pages (Whitby is Bede's account, with Wilfrid's and Colman's speeches as Bede gives them).

## Dropped
- Deacon at nineteen, priest at thirty: sourced (B:15429-15432) but cut for length.
- Ceolfrid as second abbot: sourced (B:15423) but cut.
- Ceolfrid's Easter letter to the Picts (Book V), Bede's De Temporibus: De Temporibus is named at B:6989; not used.
- "Venerable": the editor's notice says it was a tribute, not sourced to a witness; left out.
- Any claim about his scholarship in Greek: the notice says his Greek shows (B:15605), an editor's inference; left out.
- Theological stances beyond Easter: only the Easter dispute and his reliance on the Fathers are in my passes of the file. The Pelagian passage at B:5392-5433 is the Pope's letter quoted by Bede, not Bede's own statement of doctrine; not used. So the brief is light on "what he taught"; there is no file passage stating Bede's doctrine in his own voice beyond what is cited.

## score.py
bede-of-jarrow.txt {'words': 228, 'secs': 91, 'fk': 9.0, 'fre': 63.9, 'fails': [], 'below': False}

## Round-1 changes (the claim table above describes the first draft; this section governs the revision)
- Ceolwulph: now "When King Ceolwulph asked to read his History... Bede sent it" (B:117-121, "at your request... transmitted to you... I now send it again").
- Neutrality: narrator verdict removed; now "He calls himself an impartial historian" with Aidan loved and his Easter detested (B:6985-6991, 7009-7010).
- Easter explained: opens on Whitby. Oswy gathered the synod at Hilda's monastery (B:7955-7970, "the kings, both father and son, came thither"); Colman: Easter from his elders and the one John kept (B:7984-7993); Wilfrid for Rome and Peter (B:7996-8010); Hilda "for the Scots" (B:7966-7967); Oswy's keys question, both answered "We do" (B:8195-8203); quote "lest, when I come to the gates of the kingdom of heaven, there should be none to open them" (B:8204-8206, verified); Colman "went back into Scotland" (B:8232).
- Ending: death as two plain facts (date, age, Gospel of John, and Cuthbert's account all rest on the unsigned notice, B:15610-15617; Cuthbert's account itself is not in the file; the card says so). Years of work (deacon, priest, fifty-ninth year) kept on the card side/cut from audio for length.
- Legacy beat added: Roman Breviary calendar line (roman-breviary_bute1908.txt:1935, "Bede the Venerable, Confessor, and Doctor of the Church", 27 May) and Missal collect (roman-missal_england1843.txt:34724-34729, "enlightened thy church by the learning of blessed Bede"). The brief paraphrases the collect; no quotation marks.
- "born some years later": 673 is the edition notice's date (B:15600) against 664 for Whitby (B:8238).
- Dropped: the "Wycliffite tract citing Saint Bede" from the entry's legacy field: not found in the Wyclif files by grep, so not used. Audio no longer names Albinus's work or Northumbria witnesses (cut for length; Albinus/Northumbria claims remain valid in the table).
- Both quotes verified by whitespace-normalized exact-substring test.
- Score: bede-of-jarrow.txt words 279, FK 8.6, FRE 68.6, no failures. (Over 270 by a little; sources allow.)
- Card: card.json written; sources: B:8258-8268 (Eata, Tuda), B:15485-15545 (list of works), B:6989, B:15174-15178, notice.

## Round-2 changes
- Missal misreport (blocking): closing now says an English Roman Missal of 1843 prays to God, "who enlightened his church 'by the learning of blessed Bede,'" that his servants may always be enlightened by his wisdom. Quote "by the learning of blessed Bede," verified whole on roman-missal_england1843.txt:34728 (normalized test). "enlightened thy church" is not quoted (hyphenated across a line). The 27 May Breviary sentence was cut from the audio for the 300-word ceiling (it stays on the card, roman-breviary_bute1908.txt:1935); the Missal is no longer tied to that feast.
- Alcuin added to the audio: alcuin_opera-omnia-letters_migne-pl100-101_1863.txt:9436-9442 (letter to Charlemagne, "Anno 800", sending the books against Felix); Bede cited as "beatus Beda presbyter" on Acts at :12017-12018 (Acts 10) and :13850-13852 (Acts 20), and on the Song of Songs at :10320. Two citations on Acts, so "turned twice ... for his reading of the Acts" holds.
- Card: On the Times "about" now uses Bede's own claim (BH:6985-6989, "as I have most manifestly proved in the book De Temporibus"); legacy_traces replaced by Alcuin and the Lollard tract (apology-for-lollard-doctrines_todd1842.txt:6031-6034, "þus seiþ Bede, and rehersiþ Gregor... as we watteren plantis til þey han ben rotid"). My round-1 note that the Lollard tract was not found was wrong; it is vendored and now cited. Both added to written_about.
- Card legacy_remembered: Missal wording corrected; the Britons item moved out (it was Bede's bias, not a remembrance). uncertain rewritten in new words (BH:6985-7029, 15174-15178, 15432-15434, 15612-15614); no mention of the edition.
- To meet the 300-word ceiling: dropped "at the start", "Colman went home", the Breviary sentence, and the Nothelm detail (now "one of them searched the archives in Rome for letters of Pope Gregory", Nothelm per BH:163-171).
- Score: words 298, FK 9.3, FRE 65.8, no failures.
