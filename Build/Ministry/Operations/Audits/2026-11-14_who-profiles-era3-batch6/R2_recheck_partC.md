# R2 recheck, part C: era 3 batch 6

## Method

Scope: `constantius-of-lyon`, `faustus-of-riez`, `gennadius-of-marseilles` and `ruricius-of-limoges`, with their briefs, cards, audio scripts and `records.json` entries, in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era3/batch6/`. I am a fresh Opus reviewer and did not draft or fix these files. This is a targeted recheck: round 2 of at most 3. I read part C of `R1_review.md` and `R1_changes.md`. I then read the changes as a word diff from `65412883` (the drafts R1 reviewed) to HEAD (`deb3cc1d`), with the four `records.json` entries diffed one by one. For each R1 finding I opened the cited lines in the vendored file myself. I then checked every new or changed sentence against its source. For each one I asked who speaks at that line: the ancient writer, an editor, a note or an apparatus. Quotations were checked with whitespace collapsed, and the OCR was read line by line. Untouched text was not re-reviewed. I edited no profile file, and made no git, model or web calls. Line numbers point to files under `cic/texts/` unless another path is given. Brief line numbers count blank lines.

Mechanical checks, all four:
- Each audio script equals its brief once `[calmly] ` and `[warmly] ` are removed (checked by script). Each has one `[calmly]` at the start and one `[warmly]`, at the start of the closing paragraph. Ruricius's brief now has six paragraphs, and the tag sits on the sixth.
- `grade_text` passes for all four. `briefLength` is "about 2 minutes" on all four. All four cards and `records.json` parse, and `records.json` holds the ten batch ids. Every `file` named in the four cards' sources exists.
- Narrator sentences past 25 words are lead-ins to quotations or modern renderings only. Constantius's new rendering runs 26 words by my count (R1 gave 25). That is within "about 25", so I do not raise it.

| Profile | Words | Est. @162 | FK | Flesch | Cap |
|---|---|---|---|---|---|
| Constantius of Lyon (recorder) | 323 | 2:00 | 8.0 | 66.1 | within 325 |
| Faustus of Riez | 324 | 2:00 | 8.1 | 63.1 | within 325 |
| Gennadius of Marseilles (recorder) | 325 | 2:00 | 8.2 | 64.0 | 325, at the cap |
| Ruricius of Limoges | 324 | 2:00 | 7.2 | 67.3 | within 325 |

## 1. R1 findings

| Finding | Status | Evidence |
|---|---|---|
| C-B1 (Constantius: Krusch's superseded view told as his view) | RESOLVED | Card `uncertain` 6 now gives both of Krusch's positions. In the introduction he says "E Constantii Vita S. Germani Autisiodorensis (I, 1) totum caput 29. M. S. Iuliani ad verbum exscripsit" (gregory-tours arndt-krusch1885 l.35826-35827). In the addenda (p.883, head at l.66231) he writes "De Vita S. Germani Autisiodorensis, quae Constantio vulgo attribuitur … Iam nullus dubito, quin Vitae scriptor e Gregorio ipso hauserit" (l.66256-66258). The p.460 l.23 that the addendum corrects is this line of the introduction. Levison: "Opus Constantii primigenium adhuc a solo Mombritio publici iuris factum est … Vita altera admodum interpolata" (l.659-661), and "Textum vulgatum interpolationibus refertum esse, monuerunt etiam B. Krusch, SS. R. Merov. I, 883" (l.703-704). The contested claim now has both sides. Two citation slips in the records (R2-C-M2). One phrase, and the shape of the fixed sentence, need a small fix (R2-C-M1). |
| C-M1 (Constantius: the rendering) | RESOLVED | "I call God, who knows what is hidden, to witness that I have left out many deeds of my lord Germanus that were known and proved." Levison l.4577-4579, "Deum testor conscium secretorum, me plura de domni mei Germani factis agnita et probata tacuisse." "All" is gone, and the passive is kept. The records epilogue claim carries the new rendering. |
| C-M2 (Constantius: "Bede, in England") | RESOLVED | "Bede copied large parts of it almost word for word into his History of the English." Levison l.587-589, "Beda Vitam Germani c. 12-16. et 25-27. magna ex parte ad verbum fere in Historia ecclesiastica gentis Anglorum I, 17-21. descripsit". |
| C-M3 (Constantius: length) | RESOLVED | 323 words. |
| C-M4 (Constantius: "later bishop of Clermont") | RESOLVED | "Sidonius Apollinaris, bishop of Clermont." Records claim on the see stands. Its new parenthesis is review history (R2-C-M7). |
| C-M5 (Constantius: orders said absent, then given) | RESOLVED in substance | `uncertain` 1: "No source used here gives his family, his birth or his death, and the sources disagree on his orders." `uncertain` 2 adds Rees and PL 48. Rees: "the life of Saint Germanus, written by Constantius, a priest of Lyons" (rees 1853 l.17717-17718). PL 48: "quod Constantius presbyter scriptum reliquit" (marius-mercator pl48 l.20173-20174). The PL 48 passage is from a dissertation, not a note (R2-C-M3). Neither book is in the card's sources (R2-C-M4). |
| C-M6 (Constantius `knownFor`) | RESOLVED | "…journeys to Britain, parts of which Bede later copied." Levison l.587-589. |
| C-M7 (log the truncated Levison file in Open-Gaps) | PENDING, not a finding | This falls to the lead's Open-Gaps entry for batch 6, written before merge. Neither `Build/Ministry/Features/Church-Family-Tree/Open-Gaps.md` nor the Library file carries it yet. The file still ends "Et ideo in scribendo succinctum^" and a newline (checked with `od`). |
| F-B1 (Faustus: Riochatus hid the books) | RESOLVED | Brief l.1: "Unrest among the peoples held him at Clermont, where he kept the books hidden. When he left, the bishop there, Sidonius Apollinaris, rode after him and read them." Barralis, first print: "apud oppidum nostrum cum moraretur, donec gentium concitatarum procella defremeret … reliqua vestra dona detexit, ut perurbane quae praestantiora portabat, operuerit … sed post duos, aut iis amplius menses … pernicibus equis insequutus abeuntem … quaesitum volumen invenio, produco, lectito, excerpo" (l.4755-4772). The second print agrees on every word used (l.5532-5548). "A bishop and monk" is "Antistes ac monachus" (l.4751; l.5528-5529). Williams: "This Riocatus is styled bishop and monk — antistes ac monachus" (gildas williams1899 l.9662). Records claim 1 carries all three witnesses (also meets F-M5). |
| F-M1 (Faustus: length) | RESOLVED | 324 words. The cuts read cleanly: "and its abbot from 433, by Engelbrecht's reckoning. Then he became bishop of Riez." "Lucidus later retracted the view…" "praised them". "he wrote to Ruricius of Limoges". |
| F-M2 (Faustus: Warfield introduced) | RESOLVED | "The Princeton scholar Benjamin Warfield calls Faustus the chief champion of what he names semi-Pelagianism. He says the Council of Orange put it down in 529." npnf105 l.519, "PROFESSOR IN THE THEOLOGICAL SEMINARY AT PRINCETON, N.J."; l.954, "its chief champion at a somewhat later day was Faustus of Rhegium (Riez)"; l.957-958, "the 3d of July, 529 … so far as a formal condemnation could reach, semi-Pelagianism was suppressed". |
| F-M3 (Faustus: "At last") | RESOLVED | "Then he became bishop of Riez." |
| F-M4 (Faustus card `place`) | RESOLVED | "Britain, by August Engelbrecht's reading of Avitus of Vienne, who calls him a Briton by birth". |
| F-M5 (Faustus records: second print, Williams) | RESOLVED | See F-B1. |
| F-M6 (Faustus: doubled hedge) | RESOLVED | "In old age Faustus was exiled by the Gothic king Euric, Engelbrecht thinks." |
| G-M1 (Gennadius: the Prosper sentence) | RESOLVED | "Gennadius thinks Prosper of Aquitaine wrote an unsigned book against works of John Cassian. He says Prosper "brands as injurious" works "which the church of God finds salutary"." npnf203 l.43666-43669, "I regard as his also an anonymous book against certain works of Cassianus, which the church of God finds salutary, but which he brands as injurious". Both fragments are verbatim. The reordering keeps the sense, and "He" can only be Gennadius. |
| G-M2 (Gennadius: Jackson introduced) | RESOLVED | "He and Blomfield Jackson, Theodoret's translator in the same volume, give 496 for his death." npnf203 l.682-684; Jackson l.3611-3612, "Gennadius, presbyter of Marseilles, who died in 496". Merge at l.5: "The line drew much comment on his bias, Richardson says, though it almost certainly does not go back to Gennadius." The "though" clause stays inside Richardson's attribution, and his note says "almost certainly does not represent the original form of the text" (l.42864-42865). |
| G-M3 (Gennadius card: note or prolegomena) | RESOLVED | "…given in a note by Richardson and in Blomfield Jackson's prolegomena to Theodoret…". Richardson's endnote "Died 496." is at l.43968. |
| G-M4 (Gennadius card: Acta Sanctorum in sources) | RESOLVED | Entry added. The file exists, and l.180635-180636 read "Gennadius Presbyter Massiliensis, qui sub finem dicti seculi quinti floruit". |
| G-M5 (Gennadius records: Scholarios) | RESOLVED | Namesake claim added. PG 160 header l.1, "Gennadii, Constantinopolitani patriarchae, qui et Georgius Scholarius, Opera omnia". |
| R-B1 (Ruricius: the food metaphor) | RESOLVED | "He asks that Faustus's letters be harsher food, fit for a sinner's sickness, in place of the sweet dishes sent so far." Engelbrecht l.20070-20074, "quoties dignati fueritis ariditatem terrae meae eloquentiae vestrae imbre perfundere, non mihi, sicut nunc fecistis … delicatos et dulces cibos, sed austeriores et aegritudini meae congruos suggeratis"; l.20078-20079, "ne vulneribus meis gratior sit foventis dextera quam secantis". |
| R-M1 (Ruricius: 506 is in the acts) | RESOLVED in brief and card | Brief: "…at Agde under Caesarius of Arles, in 506". Card: "Caesarius's letter names Agde, whose acts date it to 506." Bruns, note 3: "Conc. Agath. viginti quinque episcoporum habitum era 644 [643 JE.], Anno vicesimo secundo Alarici regis sub die tertio Idus Septembris … Messala v. c. consulem habet Corbej." (bruns 1839 l.10498-10501). Caesarius's letter: "Agate" (l.24686). The PL 67 prolegomenon and Basnage are both reported fairly (PL 67 l.96512-96553). In the records, the era figure the claim quotes does not fit 506 (R2-C-M6). |
| R-M2 (Ruricius: Caesarius's pardon) | RESOLVED in substance | "Yet he held nothing against him." Engelbrecht l.24713-24716, "nihil pietati vestrae vel potuimus vel debuimus inputare"; PL 67 l.96517-96518, "partim objurgat, partim excusat Ruricium". "Ruricius answered" now opens a new paragraph. The pronoun is unclear when heard aloud (R2-C-M5). |
| R-M3 (Ruricius: Krusch unintroduced) | RESOLVED | "Engelbrecht thinks he died not long after 507…". Krusch stays on the card (`dates`, `uncertain` 3). |
| R-M4 (Ruricius: length, choppy pair) | RESOLVED | "Caesarius himself, he wrote, had seen him worn out at Bordeaux, and in winter, when he was usually stronger." Engelbrecht l.23186-23188, "ipsi etenim recolere potestis, quam fessum me Burdigala videritis et hoc hieme, quando esse soleo fortior solito". "Each Ruricius founded" reads cleanly. 324 words. |
| R-M5 (Ruricius: the later signer) | RESOLVED | Card `uncertain` 5. Leo's index: "alter nepos illius interfuit concilio Arverno I. a. 535, Aurelianensi IV. a. 541, V. a. 549 per Bantaredum archidiaconum subscripsit" (venantius-fortunatus leo-krusch1881 l.53125-53130, "alter nepos" at l.53128). Maassen l.6019 (under "CONCILIUM ARVERNENSE A. 535", l.6007), l.8139 (under "AURELIANENSE A. 541", l.8109), l.9442 (under "AURELIANENSE A. 549", l.9332). `absent_details` is corrected. Its new aside on the first search is review history (R2-C-M7). |
| R-M6 (Ruricius: 485) | RESOLVED | Card `uncertain` 1. Engelbrecht l.348-350, "Quodsi Euricus in causa fuit, ut Faustus a. 477 in exsilium pelleretur, illo demum mortuo i. e. anno 485 in patriam hunc rediisse veri simile est"; l.954-959, "Epistulae quarta et quinta post Fausti exsilium scriptae sunt, unde Faustus a. 485 rediit, quo eodem anno Ruricius episcopus factus est". |
| R-M7 (Ruricius: "Ruricius the elder") | RESOLVED | `otherNames` now holds only "Ruricius Lemovicensis". |

Totals: all 3 R1 blocking findings resolved. Of the 25 R1 minors, 24 are resolved or resolved in substance, and C-M7 is pending the lead's Open-Gaps entry.

## 2. New findings

No new blocking findings. Seven minor.

**R2-C-M1 MINOR (Constantius card `uncertain` 6; one phrase not true to Levison, a colon-reveal, a run-on sentence).**
Evidence: the fixed item says "In the additions at the end of the same volume he holds the reverse: the writer of that Life…" and closes "Wilhelm Levison holds that Gregory did not know Constantius's Life, since Gregory has Germanus die at Rome, where the Life has Ravenna, and he says the text then in print was a much-interpolated second Life."
- "The text then in print" is not what Levison says. He says the genuine text *was* in print, in Mombritius's edition, though neglected: "Opus Constantii primigenium adhuc a solo Mombritio publici iuris factum est, cuius textus imperfectus omnino neglegebatur postquam Vita altera admodum interpolata … apud Surium Bollandianosque lucem aspexit" (levison1920 l.659-661). His word for the interpolated text is "vulgatum", the common text (l.703).
- The Duru edition Krusch cites is that interpolated text. Duru "editionem Boschianam iteravit" (l.1620-1621), and Levison cites the second Life in Duru (l.599, "Vitae Germani secundae … Duru l. l. I, 57-66"). Saying so makes the link a reader needs.
- "He holds the reverse:" is a colon-reveal (Who_Profile_Pattern checklist item 4). The last sentence runs 41 words.
Fix, replace the item with: "Whether Gregory of Tours knew the Life. In his introduction to Gregory's Miracles, Bruno Krusch says Gregory copied a whole chapter of his Miracles of Julian almost word for word from a Life of Germanus, which he cites in Duru's edition. In the additions at the end of the same volume he reverses this, and holds that the writer of that Life, which he calls the Life commonly given to Constantius, drew on Gregory. Wilhelm Levison holds that Gregory did not know Constantius's Life, since Gregory has Germanus die at Rome, where the Life has Ravenna. Levison also says the text in common use was a much-interpolated second Life, and Duru's edition reprints that second Life." Records, contested claim side 2: add "Duru reprinted the Bollandist text of the second Life (levison1920 l.599, 1620-1621)".

**R2-C-M2 MINOR (Constantius records, contested claim "Whether Gregory of Tours knew the Life of Germanus", side 1; citation lines).**
Evidence: side 1 cites "note l.44305-44306, citing Duru's text" and "(l.66256-66257, p.883…)". At l.44305-44306 the file has "e) s. in te 2." and a blank line. Krusch's note 2 is at l.44307-44310: "Hoc caput Gregorius fere ad verbum cum Vita S. Germani Autisiod. a Constantio composita convenit; lib. I, c. 7, Duru…". "Iam nullus dubito…" is at l.66258, not l.66257, and the page head "ADDENDA ET EMENDANDA. 883" is at l.66231. R1 and R1_changes gave the same numbers, so the slip was copied forward.
Fix: "note l.44307-44310, citing Duru's text" and "(l.66256-66258, p.883, page head l.66231; OCR 'jiuUus', 'nttribuitur')".

**R2-C-M3 MINOR (Constantius card `uncertain` 2 and the new records claim; witness form).**
Evidence: "an unsigned note in Migne's Marius Mercator". The passage "quod Constantius presbyter scriptum reliquit (In Vita S. Germani Altissiodorensis)" (pl48 l.20173-20174) is not a note. It is the running text of Dissertation I, "De primis auctoribus et praecipuis defensoribus haeresis Pelagianae", one of the "Dissertationes septem" in the volume's second appendix (l.18388-18399, 18470-18472). No signature is in the held lines, so "unsigned" stands.
Fix, card: "W. J. Rees and an unsigned dissertation in Migne's Marius Mercator also call him a priest." Records claim: "…an unsigned dissertation (Dissertation I) in Migne's Marius Mercator: 'Constantius presbyter'", with witness "PL 48, appendix 2, Dissertation I (marius-mercator_opera-omnia-lat_migne-pl48 l.20173-20174; heading l.18470-18472)".

**R2-C-M4 MINOR (Constantius card `sources.about`; checklist item 12, the same fault as R1 G-M4).**
Evidence: `uncertain` 2 now cites Rees and PL 48, but `sources.about` lists only Levison's prolegomena, Isidore and Krusch's introduction. Both files exist.
Fix, add to `sources.about`:
`{"title": "Lives of the Cambro-British Saints, notes", "author": "W. J. Rees", "date": "1853", "language": "English", "file": "cic/texts/rees_lives-of-the-cambro-british-saints-lat-eng_1853.txt"}` and
`{"title": "Works of Marius Mercator, appendix 2, Dissertation I (Patrologia Latina 48)", "author": "Unsigned", "date": null, "language": "Latin", "file": "cic/texts/marius-mercator_opera-omnia-lat_migne-pl48.txt"}`.

**R2-C-M5 MINOR (Ruricius brief l.1 and audio; clarity aloud, checklist item 4).**
Evidence: "Ruricius should, he wrote, have sent someone to sign in his place. Yet he held nothing against him." Heard aloud, the paragraph's last named man is Ruricius. So "he held nothing against him" can be taken as Ruricius holding nothing against Caesarius, which reverses the pardon R-M2 put in.
Fix: "Yet Caesarius held nothing against him." Audio script to match. Scored: 324 words, FK 7.3, Flesch 66.8.

**R2-C-M6 MINOR (Ruricius records, claim "Agde 506"; a quoted date that does not fit the claim's year).**
Evidence: the claim, now tagged Documented, quotes "habitum era 644" as the acts' dating of the 506 council (bruns 1839 l.10499). Spanish era 644 is AD 606, and Bruns's variant 643 is 605. What gives 506 is Alaric's twenty-second year and the consul Messala (l.10499-10500). Engelbrecht turns that into 506: "anno enim 506 (sub d. III Idus Septembris Messala u. c. consule …)" (engelbrecht1891 l.2933-2934). The brief and card are sound, but a checker who reads the records will meet a year that contradicts the claim. Bruns's second print of the heading gives the variant as "[543. JE.]" (l.13760), so "644" is probably a slip for 544, but the held text does not settle this.
Fix, add to the claim: "(the era figure as printed, 644, does not fit 506, and Bruns gives the variants 643 and 543; the year rests on the twenty-second year of Alaric and the consul Messala, which Engelbrecht reckons as 506, l.2933-2934)".

**R2-C-M7 MINOR (records, part C ids; review history inside claim text).**
Evidence: five claims and one note now carry the history of round 1 rather than what the source says:
- Constantius: "(the brief now says 'bishop of Clermont' without 'later', R1 C-M4)", and "(R1 C-M1: 'all' dropped, passive 'agnita et probata' kept)".
- Faustus: "(R1 F-B1)".
- Ruricius: "(brief: 'Yet he held nothing against him', R1 R-M2)", "(R1 R-B1; brief now 'He asks that Faustus's letters be harsher food, fit for a sinner's sickness')", and in `absent_details` 1, "(the first search missed the OCR form 'Huricii' there)".

None of the batch 5 records carries such tags. Where each change came from is already in `R1_changes.md`.
Fix: delete the six parentheses or asides. Keep the brief's wording only where a claim needs it to show what the brief renders, as the epilogue claim does: "the brief gives this in Opus's modern English: '…'".

## 3. Verdicts

- Constantius of Lyon: CLEAR on blocking points. Four minor findings to apply (R2-C-M1 to M4), plus the Constantius parts of R2-C-M7. C-M7 is pending the lead's Open-Gaps entry.
- Faustus of Riez: CLEAR. Only the Faustus part of R2-C-M7, a records tidy-up.
- Gennadius of Marseilles: CLEAR.
- Ruricius of Limoges: CLEAR on blocking points. R2-C-M5 (one word in the brief and audio), R2-C-M6 and the Ruricius parts of R2-C-M7 to apply.

None of the new findings is blocking. Each is worded so it can be applied without another review round. A round 3 check, if one is held, needs to look only at the changed strings.
