# R1 review: era 4 batch 4

Round 1 ran in four parts, each by a fresh Opus agent that had not seen the drafting, at full effort. The parts follow, unchanged.

## R1 review, part A: Humbert of Silva Candida, Hincmar of Reims (era 4 Who batch 4)

Reviewer: independent Opus, first sight of these drafts. I edited no profile, records, README or repo file. I made no git, web, paid or model calls, and used local scripts only.

### Method

Bar: `Who_Profile_Pattern.md` checklist 1 to 14; `CLAUDE.md` "Trust and source fidelity" and "Accessible and rigorous"; the Decision-Log Who rulings of 2026-11-12 to 2026-11-14 (major cap 2:30, about 405 words; standard about 325; quotation marks only for held English; dates name their owner; named witnesses; partisan witnesses marked); `lessons.md` sections 1 to 4. For each id I read the `.brief.txt`, `.card.json`, `audio/<id>.audio.txt`, its `records.json` entry and the README lines. I opened every cited line in its vendored file and read it in context, folding two-column interleave, long s, double spaces and hyphen breaks.

Files opened: `will_acta-et-scripta-…_1861.txt` ("WILL"; prolegomena l.4040-4160, Sigebert/Wibert l.4280-4292, 8338-8351, the reply to Nicetas l.13125-13200, the Commemoratio l.14765-14945, the sentence l.14954-15050, the Edict l.15088-15420, 15600-15760, 16150-16300, Michael's letter I to Peter of Antioch l.17195-17225, letter II l.18170-18246); `mirbt_quellen-…_1911.txt` ("MIRBT" l.9860-9885, 9995-10000, 10130-10142, index l.40100-40112); `prudentius-troyes_annales-bertiniani_waitz1883.txt` ("BERT" preface l.60-372, l.2490-2510, 3520-3545, 6930-6980, 8488-8548, 9055-9105); `mansi_…-tomus-15-…` ("MANSI15" l.5418-5430, 50880-50902, 81818-81830); `mansi_…-tomus-16-…` ("MANSI16" l.53095-53140, 53940-54010, 74300-75060, 75385-75460); `mansi_…-tomus-17-18-…` ("MANSI17" l.9765-9800, 36040-36090, 36780-36990); `passiones-vitaeque-…-krusch1896.txt` ("SRM3" l.19200-19262, 19595-19608); `eulogius-cordoba_…-pl115-…` ("PL115" l.79250-79262, 79372-79470, 79580-79634); `chronica-minora-2_…-mgh-aa-11-…_mommsen1894.txt` ("AA11" l.3734-3742); `paulus-alvarus_…-pl121-…` l.27745-27756; `flodoard_annales-lat_lauer1905.txt` (header and Hincmar hits).

Absence searches across `cic/texts/`: "Silva(e) Candida(e)", "Sylva(e) Candida(e)", "Silva-candida", "Humbert" with dates or death words (Humbert's birth, death and other works: none held beyond Will's note l.9657; Le Quien in PG94 l.27414, 28884 and the Acta Sanctorum index l.165465 name him only as Leo IX's legate who answered the Greeks); "Hincmar/Hinemar/Hingmar/Ingmar" within 250 characters of obiit, defunctus, mortuus, decessit, ordinatus, died, with an 84x-88x year (found AA11 l.3739 and MANSI15 l.5427, see A-B7); "Laudun" within 400 characters of caecat/excaec/cacat (found MANSI16 l.75046, see A-M18); "proclamatio" in Mansi 15 to 18 (found MANSI17 l.36782 on, see A-B8); "Épernay/Epernay" (BERT index l.11412 "Sparnacus … Eper-nay"). Readability is from `engine.m1.gates.grade_text`, run from the repo root. I applied every suggested brief fix to scratch copies and scored them again: `/tmp/claude-0/-home-user-CIC-Project/05eab76a-1ca8-5978-bc8b-13971bb600f8/scratchpad/review/partA/humbert.fixed.txt` and `/tmp/claude-0/-home-user-CIC-Project/05eab76a-1ca8-5978-bc8b-13971bb600f8/scratchpad/review/partA/hincmar.fixed.txt`.

**Applies to both.** Audio equals the brief with `[calmly] ` at the start and `[warmly] ` at the start of the last paragraph, checked by script (both PASS). Card field order is the batch-1 order; no empty field; at most 3 keyWorks. Census traditions exist with these exact names and fit the dates: "The Latin Papal Church (Gregorian Reform to Innocent III)" 1049-1300 and "The Byzantine Imperial Church (Macedonian Era)" 843-1054 both list Humbert as a voice; "Carolingian Reform Christianity" 751-888 lists Hincmar. Every cited file exists.

---

### Humbert of Silva Candida (major; 403 words, about 2:29; FK 6.88, Flesch 71.94)

| # | Item | Result |
|---|---|---|
| 1 | Each sentence sourced | FAIL (A-B1, A-B4, A-M2, A-M4) |
| 2 | Quotes verbatim | PASS (no quotation marks in the brief; card A-M8) |
| 3 | No invention | PASS |
| 4 | Reading aids | FAIL (A-M5, A-M6) |
| 5 | Named witnesses | PASS |
| 6 | Partisan witness marked | PASS (the envoys' account, the Edict and Will are each placed) |
| 7 | Contested claims both sides | FAIL (A-B2, A-B3, A-B5, A-M1, A-M3) |
| 8 | Common names | FAIL (A-M6) |
| 9 | One term for one thing | PASS |
| 10 | Story, scene, disputes in place, length | PASS (403 words, under the cap) |
| 11 | Readability | PASS |
| 12 | Card order, fields, caveat repeated | FAIL (A-B1 `dates`; A-M7, A-M8, A-M9, A-M12) |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |
| — | Records | FAIL (A-M11) |

**Does the brief tell 1054 fairly from the held lines on both sides?** Not yet. The Latin side is given its doctrinal charges (simony, the creed) and its own account of who refused whom. The Greek side is given only its insults (darkness, wild boar) and its forgery charge. Three held Greek lines are missing: Michael's own account of why no meeting took place (A-B3), the Edict's doctrinal answer on the creed (A-B5), and the conditions in the Latin curse that the Greek version itself carries (A-B4). The contested readings are partly tagged. Authorship of the account, the reply to Nicetas, and who forged what are each told with named sides. The day of the sentence (A-B2) and where the Dialogue was written (A-M3) are told as settled. The pope's death before the sentence is left vague (A-M1).

**Sentences checked and found faithful.**
- P1: "clero ex more ad missas praeparato jam hora tertia diei sabbati chartam excommunicationis super principale altare posuerunt … pulverem pedum suorum excussere … proclamantes: Videat Deus et judicet" (WILL l.14872-14880). The scene follows the Latin; Saturday is the account's "diei sabbati". The date is A-B2.
- P2: the three envoys "a domino papa Leone nono … Humberto scilicet cardinali episcopo Silvae Candidae et Petro Amalphitanorum archiepiscopo, Friderico quoque diacono et cancellario" (WILL l.14779-14783, 14803-14804; MIRBT l.9876-9880). Will: "dubitari vix potest, quin hoc quoque scriptum … ab eodem profectum sit" (l.14794-14796). "Believes" is fair for "hardly to be doubted".
- P3: Leo of Ohrid's letter "Quo tempore (1053) instigante Michaéle Caerulario" (l.4052-4054). The year is given as Will's.
- P4: Nicetas "monachus coenobii Studiensis" (Will, l.4086-4087); the book "De azymo, de sabbato et de nuptiis sacerdotum" (l.14810-14813); the emperor "jussit … incendi scriptum" (l.14820-14821); the next day "Sic ab eis in communionem receptus et effectus est eorum familiaris amicus" (l.14806-14812); "stultior asino" (l.13191). Wibert gives the reply to Frederick and Will to Humbert (l.13143-13158).
- P5: the sentence "sicut Simoniaci donum Dei vendunt … sicut Pneumatomachi vel Theumachi absciderunt a symbolo Spiritus sancti processionem a Filio" (l.14974-14985).
- P6: the Edict "homines e tenebris erumpentes, nam ex Hesperia originem ducunt" and "veluti silvester porcus irruerunt" (l.15279-15289); "ipsi ex se advenerant nullo modo a papa missi" on "consilis Argyri" (l.15645-15646); 20 July is Will's emendation of the Edict's κδ' to κ' (note 80, l.16290-16296), so "by Will's reckoning" is right.
- P7: "ut ostensa charta illorum, quam omnino corruperat transferendo, obruerentur ibidem a populo" (l.14905-14909); Will: "mendacia mendaciis cumulantur" (l.15102).
- P8: "Humbertus sanctae ecclesiae Silvae Candidae episcopus subscripsi" under no. 229, "Papstwahlgesetz (1059)" (MIRBT l.9998, 10139).
- P9: Will's note 1 on the sentence: "inde separatio et perfecta et consummata est atque permanet" (l.15005). It is told as Will's.

**Card.** I checked these against their lines: `place` (Pigi, l.14805, 14893); `knownFor`; `keyWorks` 2 and 3 (Wibert, l.8345-8348); `legacy.traces` 2 (l.4154-4157); `remembered` 1 (l.4287-4289) and 2 (l.14786-14789); `uncertain` 1, 3, 4, 5, 6 (l.14783, 14832-14834, 4116-4118; MIRBT l.9865) and 7 (note 76, l.16172-16175; the emperor's letter blames "interpretibus et sociis Argyri", l.16225-16226). `otherNames` "Humbertus" is spelled in WILL and MIRBT; "Cardinal Humbert of Silva Candida" is the census form. The sentence lengths were checked by script: `remembered` 4 runs 26 words and `sources.ownWords[0].title` 36 words (A-M8, A-M9).

#### Findings

- **A-B1 BLOCKING (brief P3, "The envoys reached the city on 24 June"; card `dates` 1, "In Constantinople from 24 June 1054, by the envoys' own account"; records claim 2; item 1; a date attached to the wrong event).** The Commemoratio's date goes with Nicetas's recantation. Its main verb is Nicetas's "anathematizavit", and "advenientibus … apocrisiariis" is background ("the envoys having come"): "ipso die nativitatis beati Ioannis Baptistae, advenientibus a domino papa Leone nono apocrisiariis … ad monasterium Studii … Niceta monachus … anathematizavit quoddam scriptum" (WILL l.14779-14810; MIRBT l.9876-9883). No held line gives the day they arrived. Will says only that the emperor "benigne excepit et nonnullos dies in palatio suo retinuit" (l.4079-4080), and he dates their sending: "quos Leo ad pacem restituendam Constantinopolim mittere non neglexit (m. Januario 1054)" (l.4075-4077). Fix, brief P3 second sentence: "Will dates the embassy to January 1054." (7 words.) Move 24 June to Nicetas in P4: "On 24 June, the account says, Nicetas cursed his own book before the emperor, and it was burned." (18 words.) Fix, card `dates` 1: "Sent to Constantinople in January 1054, Cornelius Will says." (9 words.) Add to card `uncertain` 6, after its last sentence: "No held source gives the day the envoys arrived." (9 words.)

- **A-B2 BLOCKING (brief P1, "On Saturday, 16 July 1054"; item 7; a contested date told as settled, with no owner).** The account gives only "XVII Kal Augusti … diei sabbati" (l.14825-14874). Will reads 16 July (note 80, l.16294-16295). Mirbt's heading gives "13. Juli 1054" (MIRBT l.9865). The year rests on Will's choice of the twelfth year of Monomachos over codex C's eleventh (l.14783, 14832-14834). The card (`uncertain` 5, 6) and records (`contested_claims` 3) treat the day as contested, and the brief's own P6 names Will's reckoning for 20 July. Fix, P1 first sentence: "On a Saturday in July, the clergy of Hagia Sophia in Constantinople were ready for Mass." (16 words.) Add to P2, last: "Will reads its date as 16 July 1054, and Carl Mirbt gives 13 July." (14 words.)

- **A-B3 BLOCKING (brief P5, "The patriarch would not meet them."; item 7; one side's account told as fact).** This is the envoys' account: "Michaële praesentiam eorum et colloquium devitante" (l.14823-14824), with the sentence's "praesentiam suam et colloquium denegavit" (l.15031). Michael's own account is held. In his first letter to Peter of Antioch he says that when they came to him they were "nulla penitus nos salutatione impertiti nec sustinentes vel minimum capita sua inclinare … neque etiam omnino admittentes post metropolitanos … sedere" (l.17206-17225). In his second he says they refused to come before him (l.18183-18195), and Will's note 9 says this "prorsus adversatur Humberti narrationi" (l.18241). Will himself grants that Michael's description makes clear "quomodo factum sit, ut colloquium non institueretur" (note 6, l.14855-14866, 14939-14943). He also says the patriarch avoided them only "postquam primum cum iis congressus est" (l.4081). Fix, P5 opening: "The envoys' account says the patriarch avoided them. Michael wrote that they came to him but would not greet him, bow, or sit below his bishops." (9 and 18 words.) Fix, card: add to `uncertain`, after item 2: "Why they never met. The envoys' account says the patriarch avoided them. Michael wrote to Peter of Antioch that they would not greet him, bow, or sit below his metropolitans." (5, 9 and 21 words.)

- **A-B4 BLOCKING (brief P5, "It curses Michael, Leo of Ohrid and all who follow them."; item 1; a condition dropped).** The curse falls on "omnes sequaces eorum in praefatis erroribus et praesumptionibus" and ends "nisi forte resipuerint" (l.15036-15044). Will notes that the Greek version kept the condition as ἐὰν μὴ πεισθῶσιν (l.16036). Fix: "It curses Michael, Leo of Ohrid and their followers, unless they repent." (12 words.)

- **A-B5 BLOCKING (brief P6; item 7; the held Greek answer on the creed is missing).** The brief gives the sentence's charge that the Greeks "cut from the creed" the procession from the Son. The Edict's answer is held: the Latins condemn the Greeks "quod sacrosanctum symbolum … adulterare nolumus nec, ut illi, ex Patre et Filio Spiritum sanctum … sed ex Patre dicimus procedere" (l.15380-15388; Greek l.15326-15333). Will's note 18 flags that this is the first time the question is raised in the eleventh-century quarrel (l.15417-15419). As written, a listener hears the Roman charge on the creed and only insults from the Greek side. Fix, P6, after the first sentence: "The Greeks will not corrupt the creed, it says, for they hold that the Spirit proceeds from the Father." (19 words.)

- **A-M1 MINOR (brief P7, the Leo of Ostia sentence; item 7; a held date left out, so a listener places the pope's death in July).** Leo of Ostia's "quum jam intra hos dies defuncto papa redire disponerent" (l.4138) is told faithfully. Will, though, dates the death "XIII Cal. Maj. 1054" (l.4111; again l.16747), three months before the sentence. That date bears on the Edict's charge that the pope never sent them. Fix, replacing the Leo of Ostia sentence (this also removes the third Leo, see A-M6; the card keeps Leo of Ostia in `sources`): "Will dates Pope Leo's death to 19 April, before the sentence." (11 words.)

- **A-M2 MINOR (brief P4, "a book on the bread of the Mass"; item 1; the source softened).** "De azymo" names unleavened bread, and the leavened/unleavened question runs through all these texts ("azymitas", l.15033; "prozymita", l.15701). The book was also "contra sedem apostolicam et omnem Latinam ecclesiam" (l.14809-14810). Fix: "A monk of the Studios monastery, Nicetas, had written a book against the Latins, on unleavened bread at Mass, the Sabbath and married priests." (24 words.)

- **A-M3 MINOR (brief P3, "There Humbert wrote a Dialogue …"; item 7; a held side left out).** The place rests on Wibert: "ab ipso Latine scriptam apocrisariatus sui tempore Constantinopoli" (l.8345-8348). Will reports that Gfrörer held the Dialogue was brought from Rome, "id quod Gfrörer … opinatur" (l.8350-8351), and argues against him. Fix, brief: "Wibert, Pope Leo's biographer, says Humbert wrote a Dialogue in the city, against the Greek charges." (16 words.) Fix, card `keyWorks` 3, add: "Will reports that Gfrörer thought it was brought from Rome." (10 words.)

- **A-M4 MINOR (brief P6, "forged the seals on their letters"; item 1).** The Edict says they forged the letters themselves ("literas, quas ab eo, ut ipsi dicebant, deferebant, commenti sunt"), and that this was shown above all because "litterarum sigilla adulterata esse deprehensa sunt" (l.15608-15612, 15657-15660). Fix: "They came on the advice of Argyrus, the Greek governor in Italy, and forged the pope's letters." (17 words.)

- **A-M5 MINOR (brief P8 and P9; item 4; a floating one-line paragraph and a dangling "this curse").** P8 is a fact set loose from the story, and the card already holds it twice (`dates`, `traces` 3). P9's "this curse" then reaches back across it, and a listener cannot tell whether it means the Latin sentence or the synod's anathema. Will's note is on the Latin sentence (l.15000-15005). Fix: remove P8 (the card keeps it), and P9: "Will wrote that the sentence of 1054 made the split between the churches complete, and that it has lasted." (19 words.) The same fix applies to card `remembered` 3: "Will wrote that through the sentence of 1054 the separation of the churches was made complete, and that it has lasted." (21 words.)

- **A-M6 MINOR (brief P3 to P7; item 8; three Leos).** Pope Leo IX, Leo of Ohrid and Leo of Ostia all speak in a 400-word brief heard once, and Leo of Ohrid appears as "Leo, archbishop of Ohrid" and then "Leo of Ohrid". A-M1 removes Leo of Ostia. Keep "Pope Leo" for the pope and "Leo, archbishop of Ohrid" at first mention.

- **A-M7 MINOR (card `keyWorks` 1, "headed with Humbert's name"; item 1).** The heading "VIII. HUMBERTI BREVIS ET SUCCINCTA COMMEMORATIO" is Will's series heading (contents, l.1538). Will argues the authorship "ut ex multis indiciis apparet" (l.14794), and he would not need to if the copies named Humbert. Fix: "a record of the 1054 embassy, told in the third person. Cornelius Will and Carl Mirbt print it under Humbert's name, and Will believes he wrote it." (Then keep the Sigebert and Ekkehard clause as it stands.)

- **A-M8 MINOR (card `remembered` 4; quotation marks round German; 26 words).** Marks are for held English. Fix: "Carl Mirbt's collection of papal sources prints the account and the sentence under a heading that calls it the break between Rome and Byzantium." (24 words.)

- **A-M9 MINOR (card `sources`; item 12; named sources not listed, and a 36-word title).** Michael's letters to Peter of Antioch are named in `traces` 2, and A-B3 adds them to the brief, but they are not in `sources.about`. Fix: add `{"title": "Letters of Michael Keroularios to Peter, patriarch of Antioch, in Acta et scripta", "author": "Michael Keroularios", "date": "1861", "language": "Greek, with Latin translation", "file": "cic/texts/will_acta-et-scripta-de-controversiis-ecclesiae-graecae-et-latinae-saec-xi-grc-lat_1861.txt"}`. Shorten `ownWords[0].title` to "The envoys' account, the sentence, the Dialogue and the reply to Nicetas, in Will's Acta et scripta" (17 words).

- **A-M10 MINOR (records `absent_details` 1; wording).** "The scan's c.1000-1061 rests on no held text" is true, and my searches agree: no held line gives his birth or death. No change to the claim. Note only that Le Quien (PG94 l.27414, 28884) and the Acta Sanctorum index (l.165465) name Humbert as Leo IX's legate. Neither adds a life detail.

- **A-M11 MINOR (records).** `contested_claims` 3 cites Will's reading at "note l.15736-15740", which is the Greek text of the sentence. The notes are at l.15213-15216 (note 4) and l.16290-16296 (note 80). Claim 2 joins "ipso die nativitatis … (24 June)" to the envoys' arrival (see A-B1). Add these claims: Will on the January 1054 sending (l.4075-4077); Michael's letter I ch. VI (l.17206-17225) and letter II with Will's note 9 (l.18183-18195, 18241) as a side in a new contested claim, "why no meeting took place"; the Edict on the creed (l.15380-15388); the curse's conditions (l.15036-15044, 16036); Leo IX's death per Will (l.4111); Gfrörer's view of the Dialogue (l.8350-8351).

- **A-M12 MINOR (card `legacy.traces` 1, "to the lasting shame of those who wrote it"; item 1; sharpened).** The Edict: "ad perpetuum eorum dedecus et stabiliorem condemnationem, qui similia adversus Deum nostrum blasphemarunt" (l.4133-4136; 16287 on). The shame is that "of those who uttered such blasphemies against our God". Fix, second sentence: "It was kept in the archive of the patriarch's record keeper, to the lasting shame of all who blaspheme God so." (21 words.)

After the fixes (A-B1 to A-B5, A-M1 to A-M6 in the brief; for length I also dropped the second and third Nicetas sentences, whose contested reply the card keeps in `uncertain` 4): 396 words, about 2:27, FK 7.05, Flesch 71.06, longest sentence 24 words (scratch copy scored). Audio to be rebuilt from the fixed brief.

---

### Hincmar of Reims (standard; 336 words, about 2:04; FK 7.20, Flesch 71.36)

| # | Item | Result |
|---|---|---|
| 1 | Each sentence sourced | FAIL (A-B6, A-B9, A-B10, A-B11, A-M13, A-M14) |
| 2 | Quotes verbatim | PASS (no quotation marks) |
| 3 | No invention | PASS |
| 4 | Reading aids | FAIL (A-B7, the "held lines" register; A-M17) |
| 5 | Named witnesses | FAIL (A-B6, A-B12: the wrong man named) |
| 6 | Partisan witness marked | FAIL (A-M18) |
| 7 | Contested claims both sides | FAIL (A-B8, A-M15, A-M16) |
| 8 | Common names | FAIL (A-M16, A-M20) |
| 9 | One term for one thing | PASS |
| 10 | Story, scene, disputes in place, length | PASS |
| 11 | Readability | PASS |
| 12 | Card order, fields, caveat repeated | FAIL (A-B7, A-B8, A-B10, A-B11, A-B12, A-M19, A-M20) |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |
| — | Records | FAIL (A-M22) |

**Sentences checked and found faithful.**
- P1: the Northmen "usque circa Laudunum castellum venerunt … disponentes Remi venire"; Hincmar "vix noctu cum corpore sancti Remigii et ornamentis Remensis ecclesiae, sicut infirmitas corporis eius poscebat, sella gestatoria deportatus … ultra Matronam in quadam villa quae Sparnacus nominatur vix fuga lapsus pervenit" (BERT l.9061-9077). The Épernay gloss is in Waitz's index (l.11412). The last two sentences are A-B9.
- P2: "His annals end that year" (the 882 entry is the last, l.9094-9100). "From 861 he carried on the royal annals": the heading "AUCTORE HINCMARO ARCHIEPISCOPO REMENSI" (l.3530), and Hincmar's own "in annali gestorum nostrorum regum" (l.132-133).
- P3: Hincmar's notice: "Gotescalco praedestinatiano restiterat, post, felle commotus … ipsius heresis defensor acerrimus" (l.3532-3536), with his letter to Egilo against Prudentius's 859 entry on "geminae praedestinationis" (l.131-146).
- P4: Cellotius: "pro nepote adversus vim externam pugnat avunculus", in a fight "pro vindicandis ecclesiae rebus & juribus" (MANSI16 l.75398-75412). The annals of 871: "nomine tantum episcopus, homo insolentiae singularis … contra regem rebellans … metropolitano suo … oboedire contempnens" (BERT l.6939-6944) and "depositionis iudicium regulare suscepit" (l.6971-6977). The Mansi note: "in exilium missus, ferro vinctus, ac denique oculis caecatus … in libello proclamationis quem Joanni papae postea oblatum" (MANSI16 l.53125-53133). Troyes: "Hincmarum, vestimentis sacerdotalibus indutum, in praesentiam ipsius papae adduxerunt; indeque sublatum cantantes in ecclesiam illum duxerunt" (BERT l.8504-8510).
- P5: Krusch: "Homo vanus fallaxque … periodos formavit, quae spiritum intercludunt neque sine angore legi possunt" (SRM3 l.19603-19605). The Waitz sentence is A-B6.

**Card.** I checked these against their lines: `otherNames` ("Hincmarus" throughout; "Ingmarus" in Prudentius's part, BERT l.2437, 2504); `place`; `keyWorks` 2 (MANSI15 l.50885-50900, "Capitula presbyteris data anno DCCCLII") and 3 (SRM3 l.19219); `traces` 1 (BERT l.6944-6977; "petentibus" is the king's petition, l.6972); `traces` 2; `remembered` 2; `dates` 849 (PL115 l.79427-79432, from Hincmar's own letter to Pope Nicholas, as Antonio says). No card sentence runs past 25 words.

#### Findings

- **A-B6 BLOCKING (brief P2, "Georg Waitz, their editor, says the author is beyond doubt …"; brief P5, "Waitz calls him deeply versed …"; card `keyWorks` 1 and `remembered` 1; records claim 3; items 1 and 5; the wrong man).** The preface lines quoted are G. H. Pertz's, reprinted at the head of Waitz's edition and signed "G. H PERTZ." (BERT l.249). They include "auctorem ipsum Hincmarum fuisse, extra dubium venit", "in iure canonico … versatissimi" and "vix cuiquam praeter Hincmarum nota" (l.203-214). The margin "SS. I, p. 419" (l.84) places them in Pertz's own edition, and Waitz says he drew on "Bouqueti et Pertzii editionibus" (l.368). Pertz's same passage also gives the caution the brief leaves to a bare narrator line ("They tell his quarrels from his own side."): "Hincmarum vero, in rebus praecipue suis, maiore circumspectione consulendum esse" (l.247-248). Fix, brief P2, replacing the two Waitz sentences and "They tell his quarrels from his own side.": "G. H. Pertz, an earlier editor, held that Hincmar wrote them, and warned that they need care where his own affairs are concerned." (23 words.) Fix, brief P5 first sentence: "Pertz calls the archbishop deeply versed in church law and in the affairs of his own time." (17 words; this also fixes A-M17.) Fix, card `keyWorks` 1 `about`: "the royal annals he carried on after Prudentius of Troyes. G. H. Pertz, an earlier editor, says hardly anyone but Hincmar could have told some of what they hold, such as his flight to Épernay." (10 and 25 words.) Fix, card `remembered` 1: "G. H. Pertz calls him deeply versed in church law and in the affairs of his own time. He warns that Hincmar needs more care where his own affairs are concerned." (17 and 13 words.) Add to `sources.about`: `{"title": "Preface to the Annales Bertiniani, reprinted in Georg Waitz's edition (MGH)", "author": "G. H. Pertz", "date": "1883", "language": "Latin", "file": "cic/texts/prudentius-troyes_annales-bertiniani_waitz1883.txt"}`.

- **A-B7 BLOCKING (brief P2, "the held lines show him at work from 849 to 882"; card `dates`, "At work from 849 to 882 … No held source gives his birth or death"; card `uncertain` 4; records `absent_details` 1; a false absence, with process register in the brief).** His ordination and death are both held. Mansi's chronological table, under "Annus 845": "Concilium Belvacense Aprili mense celebratum … in quo inter cetera ordinatus est Hincmarus" (MANSI15 l.5421-5428). Theodor Mommsen, describing the codex that alone preserves the annals: "scriptos maximam partem a Prudentio episcopo Trecensi et Hincmaro archiepiscopo Remensi, finientes anno quo hic obiit 882" (AA11 l.3737-3739). Waitz's own preface agrees that Hincmar continued them "fere usque ad vitae terminum" (BERT l.261). "The held lines" is also the Library's process language, heard by a listener. Fix, brief P2 opening: "His annals end that year, the year he died, Theodor Mommsen says. Hincmar was archbishop of Reims, in Frankish Gaul. A table of dates in Mansi's council volumes puts his ordination in 845." (12, 8 and 13 words.) Fix, card `dates`: "Ordained archbishop of Reims in 845, by a table of dates in J. D. Mansi's council collection. In 849 the bishops at Quierzy sent him the condemned monk Gottschalk to hold, Nicolás Antonio says. His annals end in 882, the year Theodor Mommsen gives for his death. No held source gives his birth." (17, 19, 14 and 6 words; this also fixes the missing full stop, A-M19.) Fix, card `uncertain` 4: "His birth. No held source gives it. Theodor Mommsen gives 882, the year the annals end, as the year he died." (2, 6 and 13 words.) Add to `sources.about`: `{"title": "Chronica minora, vol. II, preface on the codex of the Annales Bertiniani (MGH AA 11)", "author": "Theodor Mommsen (ed.)", "date": "1894", "language": "Latin", "file": "cic/texts/chronica-minora-2_marcellinus-victor-tunnunensis-biclaro-isidore-mgh-aa-11-lat_mommsen1894.txt"}`. Records: replace `absent_details` 1 with Documented claims for 845 (MANSI15 l.5421-5428; OCR "inquointer", "Belvacenfe") and 882 (AA11 l.3739; OCR "Mc obiit"). Keep "birth and family" absent.

- **A-B8 BLOCKING (card `uncertain` 1, "His opponents' words come through his annals and through notes in Mansi's collection"; brief P4, the nephew's complaint known only "A note in Mansi's council volumes says …"; records `contested_claims` side 2; a false absence).** The nephew's own complaint to Pope John VIII is held in full: "Reclamatio & proclamatio Hincmari, qui quondam praeerat ecclesiae Laudunensi" (MANSI17 l.36782-36950; listed at l.36076-36077; summarized "Exponit quae a suo archiepiscopo injuste passus sit", l.9773-9779). An excerpt is printed again in MANSI16 l.53955-53964. In it he says: "violentia hostili in medio itinere segregatus sum ab ovibus meis, privatus sum & spoliatus omnibus rebus meis"; he held the archbishop "manifestissime … infestum"; "transmissus sum in exilium, in quo … aliquanto tempore ferro vinctus custoditus sum. Duobus annis ferme peractis, insuper caecatus sum". Fix, brief, a new paragraph after P4, replacing the Mansi-note sentence: "In his own complaint to Pope John, the nephew says he was seized on the road and exiled. He was kept for a time in chains, he says, and after nearly two years he was blinded." (18 and 18 words.) Fix, card `uncertain` 1, which must also repeat the brief's caveat (A-B6): "Much of his story comes from his own annals. G. H. Pertz warns that they need care where his own affairs are concerned. His nephew's own complaint to Pope John survives in Mansi's collection." (9, 14 and 12 words.) Fix, card `uncertain` 2: "What happened to his nephew after Douzy. In his own complaint to Pope John, the nephew says he was exiled, chained, and blinded after nearly two years. He does not say who blinded him. Ludovicus Cellotius, a Jesuit who took the uncle's side, says the nephew brought blindness and prison on himself by plotting against the king." (7, 21, 7 and 24 words; Cellotius's notes, MANSI16 l.75040-75046: "nova aliqua machinatione in regem … excaecationem sibi carceremque confecisset".) Add to `sources.about`: `{"title": "Complaint of Hincmar, once bishop of Laon, to Pope John VIII, in Sacrorum conciliorum collectio 17", "author": "Hincmar of Laon", "date": "1902", "language": "Latin", "file": "cic/texts/mansi_sacrorum-conciliorum-collectio-tomus-17-18-lat_welter-facsimile1902.txt"}`. Records: the nephew's side cites MANSI17 l.36782-36950.

- **A-B9 BLOCKING (brief P1, "The city had no wall and no defenders, he wrote. God's power and the merits of the saints kept the raiders out."; item 1; a miracle told in the narrator's voice, and a sharpened source).** The split leaves the second sentence with no witness, so the narrator asserts the saints' protection as fact. The Latin is a single clause: "civitatem, quam nec murus nec humana manus defendit, Dei potentia et sanctorum merita, ne illam ingrederentur, defenderunt" (BERT l.9080-9082). It also says no wall defended the city, which is not "had no wall". Fix: "No wall or human hand defended the city, he wrote, but God's power and the merits of the saints kept the raiders out." (23 words.)

- **A-B10 BLOCKING (card `remembered` 3, "Nicolás Antonio calls his annal on Prudentius a slander."; item 1; a witness made to say more).** Antonio does not give the annal to Hincmar. He blames "laudatus auctor Annalium Bertinianorum" (PL115 l.79379-79380) and calls him "Bertinianus Anonymus, Hincmari metropolitae … velificatus partibus", an unnamed annalist who took Hincmar's side (l.79623-79630, "calumniosi Annales"). Antonio is also a partisan for Prudentius ("vere catholicae sunt Prudentii sententiae", l.79373). Fix: "Nicolás Antonio, who defends Prudentius, calls the annal on him a slander. He gives it to an unnamed annalist on Hincmar's side." (13 and 10 words.)

- **A-B11 BLOCKING (card `legacy.traces` 3, "the fullest held account of Prudentius's life"; item 1; an untrue comparison, in process register).** Antonio's "Notitia historica in S. Prudentium" in PL115 runs from l.79250 to past l.79634 and is far fuller than the annal's one sentence (BERT l.3532-3538). Fix: "His notice of Prudentius's death, in the annals for 861, gives Prudentius's Spanish birth and his turn in the predestination quarrel." (21 words; "natione Hispanus", l.3533.)

- **A-B12 BLOCKING (card `uncertain` 3, "Georg Waitz reports the abbé Lebeuf's view that Hincmar reworked it"; records last claim; the wrong man, and a hedge lost).** The Lebeuf note is Martin Bouquet's. Waitz reprints it, signed "BOUQ.", and it says "ab Hincmaro interpolatum suspicatur" (BERT l.2495-2505). Pertz's preface goes further: Hincmar's correcting the book "re ipsa patet", and Lebeuf "restituendi periculum fecit" (l.220-225, 240-242). Fix: "His part in the 849 entry on Gottschalk, in Prudentius's part of the annals. G. H. Pertz holds it plain that Hincmar reworked it. A note from Bouquet's edition says the abbé Lebeuf suspected so." (14, 10 and 12 words.) The file prints "Bouqueti" and "BOUQ." but no first name, so it stays "Bouquet's edition".

- **A-M13 MINOR (brief P2, "with many of his letters"; item 4, loose quantifier).** Mansi heads them "HINCMARI RHEMENSIS EPISTOLAE ALIQUOT", some letters (MANSI15 l.81824). The A-B7 fix drops the sentence for length, and the card's `keyWorks` 2 keeps the chapters. If the sentence is kept, read "with some of his letters".

- **A-M14 MINOR (brief P2 and card `keyWorks` 1, "only Hincmar could have known"; item 1; a hedge lost).** "vix cuiquam praeter Hincmarum" means hardly anyone but Hincmar (l.210-211). The A-B6 card text restores "hardly".

- **A-M15 MINOR (brief P4, "At Douzy in 871 a synod deposed him."; card `traces` 1; item 7; held papal sides left out).** The Mansi note the brief already cites goes on: "extat tamen Hadriani rescriptum ad synodum, in quo Hincmari depositionem improbat, eumque in urbem iterandi judicii gratia mitti jubet" (MANSI16 l.53133-53137; the heading names "Hadriani II. papae", l.53119). John VIII later wrote to the uncle: "agnovimus justum fuisse omnino judicium" (MANSI16 l.53945-53951). Fix, brief, after the Douzy sentence: "Pope Hadrian II rejected the sentence, a note in Mansi says, but Pope John VIII later wrote that it was just." (21 words.) Fix, card `traces` 1, add: "Pope Hadrian II rejected the deposition, a note in Mansi says, and Pope John VIII later called the judgment just." (20 words.)

- **A-M16 MINOR (brief P4, Troyes, "At Troyes in 878, Hincmar wrote, the nephew's supporters …"; items 1 and 8).** After the nephew "also named Hincmar", "Hincmar wrote" could mean either man. The annal also says the supporters acted "sine praeceptione papae" (l.8506), and the brief drops that. Fix: "At Troyes in 878, the uncle's annals say, the nephew's supporters dressed the blind man in his vestments. Without the pope's order, they led him before the pope and into the church, singing." (18 and 15 words.) Also P4 first sentence ("his own nephew, also named Hincmar", where "also" appears twice): "He also quarreled with his nephew and namesake, Hincmar, bishop of Laon." (12 words.)

- **A-M17 MINOR (brief P5, "Waitz calls him"; item 4, pronoun).** The last man named before it is the nephew, "the blind man", or the pope. Fixed in A-B6 ("Pertz calls the archbishop").

- **A-M18 MINOR (brief P4, the Cellotius sentence; card `traces` 2; item 6; a partisan witness not marked).** Cellotius prints the writings to add "illustrius aliquid ad Hincmari Rhemensis gloriam" (MANSI16 l.75450-75451). His notes call the nephew's complaint a calumny and say the nephew brought blindness and prison on himself (l.75040-75050; margin "Hincmar. Laudun. calumnia"). For length the A-B8 rewrite drops the sentence from the brief. Fix, card `traces` 2, second sentence: "Cellotius, a Jesuit who wrote to the uncle's credit, says the uncle then fought for his nephew against outside force." (20 words.) Add to `sources.about`: `{"title": "Preface and notes to the council of Douzy and the writings of both Hincmars, in Sacrorum conciliorum collectio 16", "author": "Ludovicus Cellotius", "date": "1902", "language": "Latin", "file": "cic/texts/mansi_sacrorum-conciliorum-collectio-tomus-16-lat_welter-facsimile1902.txt"}`.

- **A-M19 MINOR (card `dates`; a missing full stop, "in 882 No held source"; "Gottschalk" with no gloss).** Fixed in A-B7.

- **A-M20 MINOR (card; items 8 and 12).** "Mansi" at its first card mention (`keyWorks` 2) needs "J. D. Mansi" (MANSI17 header: "Edited by J. D. Mansi"). "King Charles" (`traces` 1) needs "Charles the Bald" (MANSI16 l.53119, "Caroli Calvi regis"). Bruno Krusch's introduction is named in `remembered` 2 but sits inside an `ownWords` title. Move it to `sources.about` as "Introduction to the Life of Saint Remigius, MGH Scriptores rerum Merovingicarum 3", author "Bruno Krusch (ed.)", 1896, with its file.

- **A-M21 MINOR (README, the Hincmar line; a held witness not listed).** Add: "Mansi 17 holds his nephew's own complaint to Pope John VIII, and Mommsen's MGH volume gives his death year."

- **A-M22 MINOR (records).** Claim 3 gives Pertz's words to Waitz ("Waitz: …"). Re-witness it: "PERTZ preface in BERT l.203-214, signed l.249". The last claim (Lebeuf) cites l.2495-2505 as Waitz's. It is Bouquet's note (DMR, "suspicatur"), with Pertz l.220-225. Add claims for 845 and 882 (A-B7), the nephew's complaint (A-B8), Hadrian II and John VIII (A-M15), "sine praeceptione papae" (A-M16), Antonio's anonymous annalist (A-B10) and Cellotius's partisanship (A-M18). `absent_details` 2 (letter to Hadrian II, "not read through") stays as an honest limit.

After the fixes (A-B6 to A-B9 and A-M13 to A-M17 in the brief; the Cellotius sentence dropped from the brief): 341 words, about 2:06, FK 6.86, Flesch 71.91, longest sentence 24 words (scratch copy scored). That is at the top of the README's "about 300 to 340 words" for standard briefs. Audio to be rebuilt from the fixed brief.

---

### Verdicts

- **Humbert of Silva Candida:** NOT CLEAR. 5 blocking (A-B1 the 24 June date given to the envoys' arrival; A-B2 the day told as settled with no owner; A-B3 the envoys' side of the failed meeting told as fact, with Michael's held account left out; A-B4 the curse's "unless they repent" dropped; A-B5 the Edict's held answer on the creed missing) and 12 minor (A-M1 to A-M12). On 1054: as written, the brief is not fair to both sides. With A-B3, A-B4, A-B5 and A-M1, each side is heard on doctrine and on conduct, and every contested reading is owned.
- **Hincmar of Reims:** NOT CLEAR. 7 blocking (A-B6 Pertz's preface given to Waitz; A-B7 the false absence of his 845 ordination and 882 death; A-B8 the false absence of the nephew's own complaint; A-B9 the saints' protection told in the narrator's voice; A-B10 Antonio made to blame Hincmar; A-B11 "the fullest held account" untrue; A-B12 the Lebeuf note given to Waitz) and 10 minor (A-M13 to A-M22).

---

## R1 review, part B: Prudentius of Troyes, Jonas of Bobbio (era 4 Who batch 4)

Reviewer: independent Opus, first sight of these drafts. I edited no profile, records, README or repo file. I made no git, web, paid or model calls, and used local scripts only.

### Method

Bar: `Who_Profile_Pattern.md` checklist 1 to 14; `CLAUDE.md` "Trust and source fidelity" and "Accessible and rigorous"; the Decision-Log Who rulings of 2026-11-12 to 2026-11-14 as summarized in the brief (recorders stay standard length, later-retelling rule, quotation marks for held English only, named witnesses, dates with owners); the lessons file, sections 1 to 3. For each id I read the `.brief.txt`, `.card.json`, `audio/<id>.audio.txt`, its `records.json` entry and the README lines 3, 7, 12, 13, 16, 26 and 28. I opened every cited line in its vendored file and read it in context, folding OCR noise, long s, two-column interleaving and hyphen breaks.

Files: `prudentius-troyes_annales-bertiniani_waitz1883.txt` ("BERT"; title page l.66, G. H. Pertz's introduction l.84-249 signed "G. H PERTZ." at l.249, Waitz's own preface l.250-383 signed "G. WAITZ." at l.383, the 849 entry and Bouquet's note l.2421-2505, 859 l.3410-3418, 861 l.3527-3535); `eulogius-cordoba_opera-with-alvarus-vita-eulogii-pl115-lat_migne1852.txt` ("PL115"; Antonio's notice l.79250-79810, the letter to Hincmar and Pardulus from l.79864, the treatise and the Hautvillers note l.82815-82895, Prudentius's verses from Camusat l.114856-114872); `mansi_sacrorum-conciliorum-collectio-tomus-14-lat_welter-facsimile1902.txt` (Prudentius's subscriptions and Leo IV's letter, l.89874, 93639, 103777, 104336); `jonas-bobbio_life-of-st-columban_munro1895.txt` ("MUNRO"; l.60-97, 690-713, 862-866, 1528-1532); `barralis_chronologia-sanctorum-insulae-lerinensis-lat_1613.txt` ("BARRALIS"; l.36410-36462); `passiones-vitaeque-sanctorum-merovingici-mgh-srm-3-lat_krusch1896.txt` ("SRM3"; Bibianus l.7755-7780, Vedast l.31878-31940, Réomé l.39836-39935, Addenda l.58420-58525); `mansi_sacrorum-conciliorum-collectio-tomus-10-lat_welter-facsimile1901.txt` ("MANSI10"; l.61315-61385); `acta-sanctorum_martii-tomus-3-lat-grc_palme1865.txt` ("AASS-Mar3"; l.197370-197512, 197570-197595); the Columbanus profile at `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era3/batch6/columbanus.*`; `cic-website/data/world-census.json`.

Absence searches across `cic/texts/` (grep -l, several spellings and OCR forms):
- Prudentius: "Prudenti* Tre[cs]", "Prudenti* Tricass", "Prudentius of Troyes", "Galindo" (hits in PL115, BERT, Mansi 14 and 17-18, AASS Maii 6, Annales regni Francorum; the AASS and Mansi 17-18 "Galindo" hits are other men); "Celt", "Hesperi" in PL115 (found his own verses, l.114868); "Camusat"; "Pertz" and "Georg Heinrich Pertz" (the full name is printed in other held files); "Nicol[aá]s Antonio" and Latin forms (printed in ten held files).
- Jonas: "Jonas of Bobbio", "Jonas Bobiensis", "Ionas abbas", "Jonas monachus", "monk Jonas" (hits in AASS-Mar3, PL72, PL80, PL103, Foulke's Paul the Deacon); "Segusi", "Susa"; the preface's own words ("Sicambror", "Scaldeus", "Elnonis", "almi patris Columbani", "adulatorem putent", "onas peccator"), to test the card's claim that the preface Latin is held only in Barralis; "Bobolen", "Waldebert"; birth and death phrasings near "Jona".

Readability comes from `engine.m1.gates.grade_text`, run from the repo root. I applied every suggested brief fix to scratch copies and scored them again: `/tmp/claude-0/-home-user-CIC-Project/05eab76a-1ca8-5978-bc8b-13971bb600f8/scratchpad/review/partB_prudentius-of-troyes.fixed.brief.txt` and `/tmp/claude-0/-home-user-CIC-Project/05eab76a-1ca8-5978-bc8b-13971bb600f8/scratchpad/review/partB_jonas-of-bobbio.fixed.brief.txt`.

**Applies to both.** Audio equals the brief with `[calmly] ` at the start and `[warmly] ` at the start of the last paragraph, and nothing else (diff checked). Card keys are in the batch order (`name, otherNames, knownFor, dates, place, tradition, role, briefLength, keyWorks, legacy{traces, remembered}, uncertain, sources{ownWords, about}`); no null or empty field; three keyWorks each; every card sentence is 25 words or fewer (script); every cited file exists. Traditions match census names exactly and fit the dates: Carolingian Reform Christianity runs 751-888 (Prudentius, 830s-861); Insular / Irish Monastic Christianity runs 450-664 (Jonas, about 640 and 659). Neither is a census person entry; both come from the era 4 Who scan, as the README says.

---

### Prudentius of Troyes (standard, recorder; 303 words, about 1:52; FK 7.62, Flesch 64.78)

| # | Item | Result |
|---|---|---|
| 1 | Each sentence sourced | FAIL (B-B1, B-B2, B-M3, B-M5) |
| 2 | Quotes verbatim | PASS (the brief has no quotation marks; all Latin is told in modern words) |
| 3 | No invention | PASS |
| 4 | Reading aids | FAIL (B-M1, B-M4, B-M9, B-M10, B-M11) |
| 5 | Named witnesses, no roles | FAIL (B-B1: "Georg Waitz, their editor" names the wrong man) |
| 6 | Partisan witness marked | FAIL (B-B4: Antonio, the defender, is given no time or standing) |
| 7 | Contested claims both sides | FAIL (B-B3) |
| 8 | Common names | FAIL (B-M2) |
| 9 | One term for one thing | PASS |
| 10 | Story, scene, disputes in place, length | PASS (scene from his own treatise; the Gottschalk dispute is told where it arises) |
| 11 | Readability | PASS |
| 12 | Card order, fields, caveat repeated | FAIL (B-M7) |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS (recorder: the annals 835-861, his treatises) |
| — | Records | FAIL (B-B1, B-M12) |

**Sentences checked and found faithful.**
- P1: "misisti mihi quamdam schedulam decem et novem capitula continentem ex libro cujusdam Scoti selecta ... rogans et monens ut quaecunque in eis a vero exorbitantia comperissem ... responsa"; "reperi in eis Pelagianae venena perfidiae"; "Intremui, fateor, et expavi tot olim errores cum suis auctoribus jam sopitos nostris denuo temporibus pullulare" (PL115 l.82835-82891; OCR "GuenLont", "lutremni", "expavyi", "denno Llempori- bus"). The identification with Eriugena is the treatise's own title (l.82819). Faithful except B-M1 and B-M3.
- P2: Hincmar's 861 entry, "Galindo cognomento Prudentius Trecassinae civitatis episcopus, natione Hispanus" (BERT l.3530-3531). Death in 861: the same entry, "moritur". Antonio on the poem, "Hispania genitum se, ac Celtas deductum, ibique alitum ait" (PL115 l.79304-79306). Faithful to Antonio; see B-M5 for the poem itself.
- P3: Epiphany as "apparitionis Domini festum", the Roman city names, eclipses, comets, floods, wolves, "omnia, bona malave ... divinae omnipotentiae libenter adscribere" (BERT l.154-194). The details are right; their owner and purpose are not (B-B1, B-B2).
- P4: "magnis undique animis agitata ... de Praedestinatione Dei disquisitio" supports "the great quarrel" (PL115 l.79482-79485). Gottschalk "publice flagellatus librosque suarum adsertionum igni cremare compulsus est" (BERT l.2457-2458; Lebeuf's suspected rewording stops before this line, his form ends "Karolus etc.", l.2505). The sides: "Hinc ... Hincmarus Remensis ... Hinc Prudentius noster" (PL115 l.79488-79492). 859: "de veritate geminae praedestinationis ... fideliter confirmat" (BERT l.3415-3418; OCR "Komanus", "praedistinationis"). Hincmar to Egilo, "quod per alium non audivimus, nec alibi legimus" (BERT l.139-140). Faithful.
- P5: Pertz, "annalium inde ab a. 861. auctorem ipsum Hincmarum fuisse, extra dubium venit" (BERT l.203-205). The 861 entry, "qui ante aliquot annos Gotescalco praedestinatiano restiterat, post, felle commotus ... ipsius heresis defensor acerrimus" (BERT l.3532-3535). Antonio, "calumniose et inique" (PL115 l.79379, 79391) and "Nec verum est Prudentium Gotescalcho obstitisse unquam" (l.79627-79629). Faithful.
- P6: "Trecensemque ipsam ejus quondam ecclesiam, quae in catalogis suorum praesulum sanctum vocat" (PL115 l.79788-79789 area, OCR "calalogis svorum"; records give l.79612-79616). Faithful.

**Card.** Checked against their lines: the councils (PL115 l.79317-79325; Antonio also gives Tours or Paris 849; OCR "$35" for 853); the letter to Hincmar and Pardulus "scriptum anno 849" (l.79640) and its text (from l.79864); the Tractoria and its four propositions (l.79666-79672); Hincmar's plea to Egilo "ne scandalum inde in ecclesia veniat" (BERT l.143-144); the Hautvillers note and Camusat's answer (PL115 l.82845-82866); Galindo and the count of Aragon (PL115 l.79272-79278). Faults are in the findings.

#### Findings

- **B-B1 BLOCKING (brief P3 sentence 2; card `dates`, `legacy.traces` 1, `uncertain` 3, `sources.about` 1; records claims 4, 5 and 6; items 1, 5; the wrong man given the introduction and the note).** The introduction the profile gives to Georg Waitz is G. H. Pertz's. It runs from l.84 under the heading "Annalium Bertinianorum auctores ... SS. I, p. 419" (his MGH Scriptores I) and is signed "G. H PERTZ." at l.249. Waitz's own preface follows (l.250-383, signed "G. WAITZ."); his additions inside Pertz's text are marked "G. W." (l.126) or bracketed (l.217-218). So these are Pertz's: the first writer stopping "medio anno 835" (l.98), Hincmar's letter to Egilo (l.131-147), Lebeuf's signs (l.154-194), Hincmar's authorship from 861 (l.203-205), and the judgment on the 849 passage, "a Prudentio scribi non potuisse viri docti existimant, eam in speciem mutatus sit. Hincmarum enim ... correcturum fuisse, re ipsa patet" (l.222-226). The note giving Lebeuf's shorter form is signed "BOUQ." (l.2495-2505): it is Bouquet's note, which Waitz reprints, and Pertz says Lebeuf made the attempt "in editione Bouquetiana" (l.242). Waitz himself says only that Hincmar carried the annals on "fere usque ad vitae terminum" (l.260-261). He does not give 882; the held annals end there (l.9060), and Antonio gives "ad annum usque 882" (PL115 l.79270-79271). Fixes:
  - Brief P3 sentence 2: "G. H. Pertz, in Waitz's edition, gives the abbé Lebeuf's signs of his hand." (14 words; it also carries B-B2.)
  - `dates` sentence 1: "Kept the annals from 835, after a first writer who stopped in the middle of that year, G. H. Pertz says." (21 words.)
  - `traces` 1: "Hincmar took over the annals after his death, G. H. Pertz says. Hincmar carried them on almost to the end of his own life, Georg Waitz says." (12 and 15 words.)
  - `uncertain` 3: "The entry on Gottschalk under 849. G. H. Pertz says learned men judge that Prudentius could not have written it as it stands, and that Hincmar changed it. A note from Bouquet's edition, which Waitz prints, gives the abbé Lebeuf's guess at the first wording." (6, 20 and 17 words.)
  - `sources.about` 1: title "Annales Bertiniani, the entry for 861; G. H. Pertz's introduction, with Hincmar's letter to Egilo; and Georg Waitz's preface", author "Hincmar of Reims; G. H. Pertz; Georg Waitz (ed.)".
  - Records: claim 4 and 5 witness "Pertz's introduction (signed l.249)"; claim 6 "Bouquet's note, reprinted by Waitz (l.2495-2505, signed 'BOUQ.'); Pertz l.219-226 endorses it"; contested claim 2, side 2 "Lebeuf, in Bouquet's note (l.2495-2505), and Pertz (l.219-226): reworked by Hincmar".

- **B-B2 BLOCKING (brief P3 sentence 2; item 1; the argument misreported).** The brief says Lebeuf gave "reasons for seeing a Spaniard's hand". Lebeuf's dissertation, as Pertz reports it, proved that the part from 861 on is "a prioribus plane diversa" (BERT l.153-154), so his signs separate Prudentius's part from Hincmar's. Only the Epiphany usage is tied to Spain ("patrio more", l.155-156). The Roman city names he learned "ex Iulii Caesaris commentariis et Itinerario Antoniniano" (l.160), and the weather, wolves and credit to God are no Spanish marks at all. Fix: the B-B1 sentence. Then: "Prudentius calls Epiphany the Apparition of the Lord, by the custom of his homeland." (14 words.) The Roman-names clause can stay ("and gives Gaulish cities their old Roman names") or be cut for length. The scratch copy cuts it.

- **B-B3 BLOCKING (brief P3 sentence 1; card `knownFor`, `keyWorks` 1; item 7; a contested point told as settled).** "the royal annals" says they were the court's official record. Waitz reports that this very point is disputed: "Hos annales sub imperatoris Ludovici et regis Karoli Calvi auspiciis scriptos esse, ut seriem annalium publica auctoritate susceptorum continuarent, alii contenderunt, alii in dubium vocaverunt" (BERT l.250-253). He leans with Wattenbach against it, and thinks Hincmar kept the book, not the court (l.254-263). Hincmar's own words are "annali gestorum nostrorum regum" and "rex habet" (l.133-134, 146). Fixes:
  - Brief P3 sentence 1: "He kept the annals of the Frankish kings' deeds, now called the Annals of Saint-Bertin, from the 830s until his death." (21 words.)
  - `knownFor` sentence 1: "Spanish-born bishop of Troyes who kept the annals now called the Annals of Saint-Bertin until his death in 861." (19 words.)
  - `keyWorks` 1 `about`: "the annals of the deeds of the Frankish kings, which Hincmar says Prudentius composed and the king held. Georg Waitz says some have held them to be official annals and others have doubted it" (18 and 16 words).

- **B-B4 BLOCKING (brief P2 sentence 3 and P5; card `dates`; items 6 and 4; a defender with no time or standing, which a listener will mishear).** Nicolás Antonio is introduced bare, "Nicolás Antonio reports". Heard once, "Antonio calls this a slander. He says Prudentius never opposed Gottschalk" sounds like a ninth-century answer to Hincmar. It is a later bibliographer's defense, written after the 1650 collection it cites (PL115 l.79553-79557), in the "Biblioth. vet. Hisp." (l.79258), of "Prudentius noster" (l.79492). The card's first mention (`dates`) has the same gap. Fixes:
  - Brief P2, after the poem sentence (see B-M5): "Nicolás Antonio, a Spanish scholar writing after 1650, takes Hesperia to be Spain." (13 words.)
  - Card `dates` sentence 3: "At councils at Paris in 846 and at Soissons in 853, says Nicolás Antonio, a Spanish scholar writing after 1650." (20 words.)

- **B-M1 MINOR (brief P1 sentence 1; item 4; a word a listener will mishear).** "the book of a Scot, John Scotus Eriugena" leads a modern listener to hear a man from Scotland. The Latin "cujusdam Scoti" (PL115 l.82858) means an Irishman here, but the brief does not say so. Fix, also folding in the next sentence for length: "Wenilo, archbishop of Sens, sent Prudentius of Troyes nineteen chapters from a book by John Scotus Eriugena, and asked him to answer each error." (24 words.)

- **B-M2 MINOR (brief P1, P4; card `legacy.traces` 2; item 8).** The first mention of the subject is a bare "Prudentius", and a listener may know the earlier Spanish poet of that name. The fix in B-M1 gives "Prudentius of Troyes". "Pope Nicholas" should be "Pope Nicholas the First", as Antonio has "Nicolao I" (PL115 l.79625), in the brief P4 and in card `traces` 2. Fix for `traces` 2, sentence 1: "His entry under 859, that Pope Nicholas the First had confirmed a double predestination, made Hincmar write to Egilo of Sens." (21 words.)

- **B-M3 MINOR (brief P1 sentence 3; item 1; a quantifier lost).** "et aliquoties Origenis amentiam" (PL115 l.82882) is the madness of Origen "at times". The brief makes it as general as the Pelagian poison. Fix: "Prudentius found the poison of Pelagius in them, he wrote, and at times the madness of Origen." (17 words.)

- **B-M4 MINOR (brief P4; item 4, undefined term; pattern, "the positions they fought for").** "double predestination" is never explained, and the brief gives no line of what Prudentius taught. Antonio sets out his propositions: "Quosdam a Deo fuisse gratuito praedestinatos ad vitam, quosdam imperscrutabili justitia praedestinatos ad poenam" (PL115 l.79394-79396). Fix, after "Prudentius took the side Hincmar opposed.": "He taught, Antonio says, that God freely chose some for life, and by a justice past searching out destined others for punishment." (22 words.) In the 859 sentence, "the truth of" can go for length.

- **B-M5 MINOR (brief P2 sentence 3; card `place`, `sources.ownWords`; records claim 3; item 1; his own words held but told through Antonio).** The poem itself is in PL115: "VERSUS SANCTI PRUDENTII. (Apud Camuzat., Promptuarium ...)", with "Hinc ego devoto famulans Prudentius actu / Hoc Evangelii solvo libenter opus / Hesperia genitus, Celtas deductus et altus" (l.114856-114868). It says Hesperia, and "Spain" is Antonio's reading. Fixes:
  - Brief: "In verses for a Gospel book, he calls himself born in Hesperia and brought to the Celts." (17 words), then the B-B4 sentence.
  - `place`: "Born in Hesperia and brought to the Celts, by his own verses for a Gospel book; Nicolás Antonio takes Hesperia to be Spain. Bishop of Troyes" (the first sentence is 23 words).
  - `sources.ownWords` 2 title: add "Verses for a Gospel book, from Camusat's Promptuarium".
  - Records claim 3: cite PL115 l.114864-114869 as well.

- **B-M6 MINOR (card `legacy.remembered` 3; `sources.about`; items 1 and 8; a hedge dropped, a name form, a source unlisted).** Camusat says the note came "ex alicujus fortasse capite" (PL115 l.82867), "perhaps" from someone not up to the work. The card drops "fortasse". "Nicolas" is not a form any held file prints: PL115 has "Nic. Camusat." (l.82873, OCR "Canusat.") and "Nicolaus Camusatius" (l.79794). Camusat's Promptuarium is named but not listed in `sources`. Fix: "A note in a manuscript of his treatise, printed in Patrologia Latina 115, warns that he did not think rightly on some teachings. Nicolaus Camusat of Troyes answers that it came perhaps from someone who could not follow him." (23 and 16 words.) Add to `sources.about` "Note on the Hautvillers manuscript, from the Promptuarium of Troyes, in Patrologia Latina 115", author "Nicolaus Camusat", date "1852".

- **B-M7 MINOR (card `uncertain` 1 and order; items 12 and 4; the caveat not first, and a loose quantifier).** The brief's caveat is the Gottschalk dispute (P5), but it stands second in `uncertain`. The first item, "Little of his life is held beyond his writings", is loose. PL115 and Mansi 14 hold his council subscriptions, a letter of Leo IV to him and Lupus's letters to him (Mansi 14 l.89874, 93639, 104336; PL115 l.79327-79340). Fix: move the Gottschalk item first, and rewrite item 1 as "Most of what is told of his life comes through Hincmar, his opponent, and through defenders who answered Hincmar, such as Nicolás Antonio." (23 words.)

- **B-M8 MINOR (card `uncertain` 4; item 1; the guess placed wrong).** Antonio says the count of Aragon proves the name Spanish, "dubitare nos haud sinit" (PL115 l.79272-79275). His guess is the kinship: "Quid vero impedit ex eadem progenie cum Galindo nostro Prudentium fuisse?" (l.79275-79276). The card's "only as a guess to a count of Aragon of that name" blurs the two. Fix: "His name. Hincmar calls him Galindo, surnamed Prudentius. Antonio says a count Galindo of Aragon shows the name is Spanish. He asks what stops Prudentius being of the same family." (2, 6, 12 and 10 words.)

- **B-M9 MINOR (card `legacy.remembered` 1 sentence 2; item 4; label register).** "Hincmar is the hostile witness of the predestination quarrel." is a review label put into the card. Fix: "Hincmar was his opponent in the predestination quarrel." (8 words.)

- **B-M10 MINOR (card `legacy.traces` 3; item 4; undefined term).** "Tractoria" is not explained. Antonio gives it as the letter he sent through his vicar Arnald to the synod of Sens (PL115 l.79666-79668). Fix: "Antonio says he sent a letter, his Tractoria, to the synod of Sens. In it he held that Aeneas, chosen bishop of Paris, must sign four statements first." (13 and 16 words.)

- **B-M11 MINOR (brief P3; item 4; choppy run and a loose word).** "Prudentius calls ... He gives ... He notes ..." is a run of short "He" sentences. "notes ... wolves" undersells "luporum devastationibus" (BERT l.191). Fix: "He notes eclipses, comets, floods and the ravages of wolves, and he credits good and bad alike to God." (19 words.) The B-B2 fix joins the Epiphany sentence to what comes before.

- **B-M12 MINOR (records).**
  - Claim 11 (councils): flag OCR "$35" for 853 (PL115 l.79325). The locator starts at l.79317.
  - Claim 15 (Galindo): the locator is l.79272-79278, not 79275-79290.
  - `absent_details` "his family": Antonio's kinship guess is held (B-M8). Say so: "no held line gives it; Antonio guesses kinship with Count Galindo of Aragon (Inferential-Thin)".
  - Add the verses (B-M5) and Camusat's "fortasse" (B-M6).

After the fixes (B-B1 to B-B4 and B-M1 to B-M5 and B-M11 in the brief; the cut of the Roman-names clause and "the truth of" for length): 327 words, about 2:01, FK 7.67, Flesch 64.14, longest sentence 24 words (scratch copy scored). The audio file takes the same changes.

---

### Jonas of Bobbio (standard, recorder with a thin own life; 326 words, about 2:01; FK 7.88, Flesch 67.48)

| # | Item | Result |
|---|---|---|
| 1 | Each sentence sourced | FAIL (B-M14, B-M16, B-M17) |
| 2 | Quotes verbatim | PASS ("Theudegisil himself told us of this", MUNRO l.708-709, line-break hyphen "Theudegi- sil"; the source runs on with "and showed his finger", so the comma correctly sits outside the marks) |
| 3 | No invention | PASS |
| 4 | Reading aids | FAIL (B-M14, B-M15) |
| 5 | Named witnesses, no roles | PASS (Munro and Krusch are named with roles) |
| 6 | Partisan witness marked | PASS ("It is a saint's Life ... as Munro notes") |
| 7 | Contested claims both sides | PASS (Vedast: "Krusch believes"; the card gives the Life's silence) |
| 8 | Common names | FAIL (B-M13) |
| 9 | One term for one thing | PASS |
| 10 | Story, scene, disputes in place, length | PASS |
| 11 | Readability | PASS |
| 12 | Card order, fields, caveat repeated | FAIL (B-B5, B-M20, B-M22) |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS (recorder: the Life of Columbanus and the Life of John) |
| — | Records | FAIL (B-B5, B-M21) |

**Sentences checked and found faithful.**
- P1: "quamquam me et per triennium Oceani per ora vehit ... Scaldeus molles sulcando vias, madere facit saepe et lenta palus Elnonis plantas, ob venerabilis Amandi Pontificis ferendum suffragium: qui his constitutus in locis veteres Sicambrorum errores Evangelico mucrone coercet" (BARRALIS l.36442-36445; OCR "perora", "Scalteus", "Elnomis piant as", "amandi Pottfiat"). Krusch reads it the same way: "Scaldim fluvium, sed etiam Scarbeam rivum navigasse" (SRM3 l.31896-31898). Faithful except B-M14 and B-M15.
- P2: "Memini me ante hoc ferme triennium ... Beati Bertulfi Abbatis imperio jubente ... fuisse pollicitum"; "quamplurimi penes nos superstites sint"; "per venerabiles viros Attalam et Eustasium didicimus, quorum primus Bobiensis, secundus Luxoviensis coenobii ... successores fuerunt" (BARRALIS l.36424-36432). Munro, "became a monk at Bobbio ... three years after Columban's death" (MUNRO l.76-77). Faithful.
- P3: Munro, "As is usual in such biographies, the miracles are numerous" (l.81-82); Krusch, "Ionas c. a. 640." (SRM3 l.7772). Named informants: Theudegisil (MUNRO l.709), Chamnoald (l.863), Eustasius (l.1530), Somarius "who is still alive" (l.550), so "often" holds. Munro on "great value" (l.73-74). Faithful.
- P4: "ex iusso ipsius principes vel genetrices suae praecelse domne Baltilde regine ... Ionas abbas per Riomao ... paucis diebus inibi pro labore itineris quievit, cumque victus precibus fratrum" (SRM3 l.39929-39935). The forgers: "a duobus falsariis retractatus ... se ipsum saeculo VI, ideoque ante Ionam, vixisse affirmans" (l.39838-39844). Faithful except B-M16 and B-M17.
- P5: "cumque Ionae peculiare elocutionis genus ita subsecutus sit, ut apud utrumque idem miraculum legatur iisdem fere verbis enarratum ... mihi quidem persuasum est ... ab uno eodemque auctore condita est" (SRM3 l.31892-31901). Faithful and hedged.
- P6: "Et si me quempiam laudare repererint qui adhuc superis iunctus sit, non me adulatorem putent ... nec favere cuiquam panegyrico carmine sed digna memoriae commendare" (BARRALIS l.36455-36457). Faithful.

**Card.** Checked against their lines: Munro's judgments and the omitted preface (MUNRO l.78-81, 96-97); Krusch on Bibianus (SRM3 l.7771-7774); C's claim "qui illum saepe vidissent" (l.39855; OCR "illuni"); the Réomé journey toward Chalon, "ad urbem Cabalonnensem" (l.39929-39930); the Mâcon account, "Quae fusius a Jona monacho narrantur in vita Eustasii" (MANSI10 l.61340-61342); the Surius heading, "ab eius aequali Iona Abbate" (BARRALIS l.36419). The claim that the preface's Latin is held only in Barralis survives the search: AASS-Mar3's Eustasius preface (l.197575-197595) echoes it but is not it. "Ionas" is spelled in SRM3 (l.39931). Faults are in the findings.

**Agreement with the era 3 Columbanus profile.** The overlaps agree. Both say Jonas was a monk of Bobbio who came three years after Columbanus's death (Munro), drew on companions and on Attala and Eustasius, and wrote a saint's Life. Both date the Life about 640 (Columbanus via Foulke and Hodgkin, Jonas via Krusch; the same date). Both cite the Mâcon account from "Jonas's Life of Eustasius, which Giovanni Domenico Mansi quotes", and both list Barralis's printing of the Latin. Two notes for the lead. If B-B5's Susa birth goes onto Jonas's card, the Columbanus card has nothing that contradicts it. The Columbanus card's Mansi entry also lacks a date (B-M20 applies there too, outside this batch).

#### Findings

- **B-B5 BLOCKING (records `absent_details` 1 and 2; card `place`, `dates` last sentence, `uncertain` 1, `sources.about`; a false absence, and an honest limit that hides held lines).** The records say his "birth, origin and death" have "No held line", and that the house he ruled as abbot is not named. AASS-Mar3 holds both, in the Bollandists' commentary on Eustasius. "Acta SS. Columbani, Eustasii, Attalae, Bertulphi Abbatum, et S. Burgundoforae ... scripsit Jonas, qui Bobii sub Attala, Bertulpho et Boboleno vix monachus, et forsan huic, quia Abbas appellatur, successit, natione non Hibernus, sed Italus Segusii, vulgo Susae, ad radices Alpium et montis Cinisi natus" (l.197480-197486). Earlier, the abbots of Bobbio run "S. Attala ... S. Bertulphus ... postea Bobolenus et forsan Jonas" (l.197378-197382). They say they prove this at 10 March, in the Life of Attala (l.197486-197487), which is not held. So the held lines give his birthplace (Susa, Italian, not Irish) and a hedged ("forsan") succession as abbot of Bobbio. His birth year and death stay unheld. Fixes:
  - Card `place`: "Born at Susa in Italy, at the foot of the Alps, say the Acta Sanctorum editors G. Henschenius and D. Papebrochius. A monk of Bobbio; with Bishop Amand on the Scheldt and the marsh of the Elnone; at Réomé, on his way to Chalon" (17 and 23 words; the editors' names as the file header gives them).
  - Card `dates`, last sentence: "No held source gives his birth year or his death" (10 words).
  - Card `uncertain`, a new item: "His origin. The Acta Sanctorum editors say he was Italian, not Irish, and born at Susa. They rest this on their Life of Attala, which is not held." (2, 14 and 12 words.)
  - Card `uncertain`, another new item: "Whether he was abbot of Bobbio. The Acta Sanctorum editors list him after Bobolenus among its abbots, with a perhaps. The Réomé opening calls him abbot but names no house." (6, 14 and 10 words.)
  - Card `uncertain` 1: "His own life is known mostly from his prefaces and the opening of his Life of John. Dana Munro, Bruno Krusch and the Acta Sanctorum editors add a little." (17 and 12 words.)
  - `sources.about`, add: title "Commentary on St Eustasius, abbot of Luxeuil, in Acta Sanctorum, March, volume 3", author "G. Henschenius and D. Papebrochius", date "1865", language "Latin", file `cic/texts/acta-sanctorum_martii-tomus-3-lat-grc_palme1865.txt`.
  - Records: replace `absent_details` 1 with a claim, "Born at Segusium (Susa), Italian not Irish; a monk under Attala, Bertulf and Bobolenus", witness "AASS-Mar3 l.197480-197486; OCR 'Susz', '.4ttala'", tagged Documented as the Bollandists' statement. Replace `absent_details` 2 with "Perhaps abbot of Bobbio after Bobolenus", witness "AASS-Mar3 l.197381, 197482-197483 ('forsan')", tagged Inferential-Thin. Keep "birth year and death: no held line".
  - Optional, brief P2 (not needed to clear): "The Acta Sanctorum editors say he was born at Susa, in Italy." (12 words; this would take the brief to about 339 words.)

- **B-M13 MINOR (brief P1 sentence 1; item 8; the subject's own name).** The first mention is a bare "Jonas". The Library holds other men of the name: Jonas of Orléans (AASS-Mar3 l.85544) and Jonas, a monk of Fontenelle (l.241268). Fix: "For three years, Jonas of Bobbio wrote, he was carried along the shores of the Ocean." (16 words; it also carries B-M14.)

- **B-M14 MINOR (brief P1 sentence 1; items 1 and 4; a misparsed line).** "the shores of the Ocean carried him" makes "ora" the subject. In "me ... Oceani per ora vehit" (BARRALIS l.36442) the shores sit inside the phrase "per ora", so the shores cannot be the subject. He was carried along them. Fix: the B-M13 sentence.

- **B-M15 MINOR (brief P1 sentence 3; item 4; an undefined name).** "the Sicambri" means nothing to a general listener, and no held line glosses it for this passage. Fix: "He had gone to help Bishop Amand, who was curbing the old errors of the people there with the blade of the Gospel." (23 words.) The card can keep the source's name if a gloss is wanted later.

- **B-M16 MINOR (brief P4 sentence 1; item 1; a date without its owner).** The text dates the journey "anno tercio regni domni Clotharii regis" (SRM3 l.39928). The 659 is Krusch's margin (l.39931, "659"). The brief gives the bare year as fact, though the card names Krusch. Fix: "In the third year of King Clothar, which Krusch reckons as 659, Jonas was an abbot himself." (17 words.) Then: "On a journey ordered by the king and his mother, Queen Balthild, he rested a few days at the monastery of Réomé." (22 words.)

- **B-M17 MINOR (brief P4 sentence 3; item 1; a part of the witness chain dropped).** The monks asked for what had been learned "per discipulos memorati confessoris Christi vel posteris eorum" (SRM3 l.39933-39934). The brief keeps the disciples and drops their successors. Fix: "Its monks begged him to write down what the disciples of their founder, John, and those after them had passed on, and he did so." (25 words.)

- **B-M18 MINOR (card `legacy.traces` 2; item 1; a word that hides the editor's point).** "an old Life of Bibianus" hides Krusch's point. He argues against Stiltingus that the Life is late, because its prologue echoes Jonas's and "Sermo ... ad Carolingicum referendus est" (SRM3 l.7771-7775). Fix: "Krusch finds a prologue like Jonas's, and a phrase Jonas often used, in a Life of Bibianus of Saintes. He places its language in the Carolingian age." (17 and 9 words.)

- **B-M19 MINOR (card `uncertain` 2; records contested claim 1; addenda not read).** Krusch's Addenda give one more supporter for the Vedast attribution: "P. 399, l. 32. Etiam G. Kurth l. l. p. 610, opinioni meae nuper accessit" (SRM3 l.58518). Page 399, line 32 is the Duchesne sentence. Fix, `uncertain` 2: "Whether he wrote the older Life of Vedast, bishop of Arras. Krusch believes so, from its style and a wonder told in nearly the same words. He says Louis Duchesne agreed, and later G. Kurth. The Life itself names no author." (11, 15, 8 and 6 words.) Records: add l.58518 to Krusch's side.

- **B-M20 MINOR (card `sources.about` 2; item 12).** The Mansi entry has no `date`, while every other source has one and the file header gives the 1901 facsimile. Fix: add `"date": "1901"` after `author`.

- **B-M21 MINOR (records, claim "Card: Surius's heading").** The records quote the heading as "quem quidam vocant discipulum eius". The OCR "quem quidam vocat difiif alorum eim difci falam" (BARRALIS l.36419-36420) reads "quem quidam vocant discipulorum eius discipulum", a disciple of his disciples. The card does not use the phrase, so only the records change. Fix the quoted string and flag the OCR forms.

- **B-M22 MINOR (card `uncertain` order and item 1; items 12 and 4).** The brief's caveat is the Vedast attribution (P5), but it stands second. Item 1 opens on a label, "His own life is thin." (the lessons' "label opener"). Fix: move the Vedast item first, and use the B-B5 rewrite of item 1.

After the fixes (B-M13 to B-M17 in the brief, with Munro's "great value" sentence cut for length, since the card's `remembered` 1 keeps it): 327 words, about 2:01, FK 8.04, Flesch 67.97, longest sentence 25 words (scratch copy scored). The audio file takes the same changes.

---

### Verdicts

- **Prudentius of Troyes:** NOT CLEAR. 4 blocking (B-B1 Pertz's introduction and Bouquet's note given to Waitz; B-B2 Lebeuf's signs told as signs of a Spaniard rather than of Prudentius's part; B-B3 "royal annals" told as settled where Waitz reports the dispute; B-B4 Nicolás Antonio given no time, so his defense sounds contemporary) and 12 minor (B-M1 to B-M12).
- **Jonas of Bobbio:** NOT CLEAR. 1 blocking (B-B5, a false absence: the Acta Sanctorum editors give his birth at Susa and a hedged abbacy of Bobbio) and 10 minor (B-M13 to B-M22). It agrees with the era 3 Columbanus profile wherever they overlap.

---

## R1 review, part C: Braulio of Zaragoza, Ildefonsus of Toledo (era 4 Who batch 4)

Reviewer: independent Opus, first sight of these drafts. I edited no profile, records, README or repo file. I made no git, web, paid or model calls, and used local scripts only.

### Method

Bar: `CLAUDE.md` "Trust and source fidelity" and "Accessible and rigorous"; `Who_Profile_Pattern.md`, checklist 1 to 14; the lessons file (sections 1 to 4); the Decision-Log Who entries of 2026-11-12 to 2026-11-14 as summarized in the brief. For each id I read the `.brief.txt`, `.card.json`, `audio/<id>.audio.txt`, its `records.json` entry and the README lines on it. I opened every cited line in its vendored file and read it in context, folding OCR noise, long s, interleaved columns and hyphen breaks.

Files: `paulus-emeritanus-braulio-sisebut-pl80-lat_migne1863.txt` ("PL80"); `ildefonsus-julian-toledo-pl96-lat_migne1862.txt` ("PL96"); `collectio-canonum-ecclesiae-hispanae-toledo-iii-lat_1808.txt` ("HISP"); `isidore-seville_encyclopedist-of-the-dark-ages-extracts_brehaut1912.txt` ("BREHAUT"); also `chronica-minora-2_marcellinus-victor-tunnunensis-biclaro-isidore-mgh-aa-11-lat_mommsen1894.txt` ("MGH11"), `mozarabic-liturgy_missale-mixtum-pl85-lat_migne1862.txt` ("PL85"), `acta-sanctorum_martii-tomus-3-lat-grc_palme1865.txt` ("AASS-Mar3"), and the era 3 Isidore profile (`Who-Profiles/era3/batch6/isidore-of-seville.*`).

Absence searches across `cic/texts/` (grep -l, several spellings: braulio/braulion/draulio/craulio; ildefons/hildefons/ildephons/hildephons; agali/agaliens; caesaraugust/cesaraugust/ciesaraugust; archidiacon; praenotatio/pranotatio; pacens; kalend.*febr): Braulio's death year (MGH11 holds Mommsen's range, see C-M8); an Acta of Braulio (AASS-Mar3 has only a two-line notice at l.155180); a held line joining Braulio's archdeacon to Eugenius II (none: PL80 Letter XXXVI to "Eugenius primate of Toledo", l.54771ff, does not make it; Antonio, PL96 l.706-710, says Eugenius was a Toledo cleric before he took the habit at Zaragoza, which is Ildefonsus's account again); Ildefonsus's birth and family (held, see C-B3); where Agali stood (held, see C-B4); his death day elsewhere (PL85 l.93258).

Readability comes from `engine.m1.gates.grade_text`, run from the repo root. I applied every proposed brief fix to scratch copies and scored them again: `/tmp/claude-0/-home-user-CIC-Project/05eab76a-1ca8-5978-bc8b-13971bb600f8/scratchpad/review/partC/braulio-of-zaragoza.brief.R1fix.txt` and `/tmp/claude-0/-home-user-CIC-Project/05eab76a-1ca8-5978-bc8b-13971bb600f8/scratchpad/review/partC/ildefonsus-of-toledo.brief.R1fix.txt`.

**Applies to both.** Audio equals the brief with `[calmly] ` at the start and `[warmly] ` at the start of the last paragraph, nothing else (diffed). Card keys are in batch order; `legacy` is `traces` then `remembered`; `sources` is `ownWords` then `about`; no empty field; at most 3 keyWorks; no card sentence over 25 words (script, splitting on . ! ? ;). Tradition "Nicene Visigothic Iberia" is a census movement name (560 to 711) and fits both men's dates. Both keep their census line (census l.41106-41107, l.41198-41209). The README's lines on them are true.

**On the laws against Jews.** I read Toledo VI canon III whole (HISP l.41727-41775) and Braulio's letter to Honorius whole (PL80 l.53689-53910). The Braulio brief's two sentences on the canon are fair to it and do not soften it: Chintila "nec sinit degere in regno suo eum qui non sit catholicus" is told as said. One word adds to it ("that law", C-M5). The card softens the letter once, where "superstitionem suae religionis" becomes "their old religion" (C-M11). The Braulio brief agrees with the era 3 Isidore profile, which tells Toledo IV's canon on forced baptism (Isidore brief P5, card `traces` 2). The Ildefonsus files have no line on Jewish law. The card's naming of the third "unbeliever" as a Jew follows Antonio (PL96 l.898-904) and is fair.

---

### Braulio of Zaragoza (standard; 326 words, about 2:01; FK 6.80, Flesch 71.45)

| # | Item | Result |
|---|---|---|
| 1 | Each sentence sourced | FAIL (C-B1, C-M1, C-M5, C-M6) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | FAIL (C-M4) |
| 5 | Named witnesses | PASS |
| 6 | Partisan witness marked | PASS |
| 7 | Contested claims both sides | FAIL (C-B2, C-M2) |
| 8 | Common names | PASS |
| 9 | One term for one thing | PASS |
| 10 | Story, scene, disputes in place, length | FAIL (C-M3) |
| 11 | Readability | PASS |
| 12 | Card order, fields, caveat repeated | FAIL (C-M7 to C-M11) |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |
| — | Records | FAIL (C-B2, C-M8) |

**Sentences checked and found faithful.**
- P1: "Lumine corporis caecutio"; "jussione gloriae vestrae aufertur pars animae meae"; "preces dirigo ut non separes eum a me"; "Eugenii mei archidiaconi" (PL80 l.54479-54524). The king's reply, "quod ipse hinc exstiterit oriundus ubi nunc consecrandum speculatorem optamus" (l.54566-54572). "Etsi disrupto potius quam scisso societatis vinculo ... misimus" (l.54591-54594). "Braulio sent him" leaves out his plea that the king send Eugenius back to Saint Vincent's (l.54595-54597). That is a cut, not a fault.
- P2: Ildefonsus XIV, "Hic cum Ecclesiae regiae clericus esset ... sagaci fuga urbem Caesaraugustanam petens ... unde principali violentia reductus, atque in pontificatum ascitus" (PL96 l.17048-17051, 17056, 17066-17067; columns interleaved).
- P3: Ildefonsus XII, "frater Joannis ... adeptus est locum ... Habuit sacerdotium ferme viginti annis ... temporibus Sisenandi, Chintilae, Tulganis et Chindasvinthi" (PL96 l.17059, 17096-17101). Signatures at HISP l.41071 (IV), l.41419 (V), l.42439 (VI). IV is era 671 (l.38628) and VI era 676 (l.41560). V reads "DCLXIV" in OCR, and the apparatus gives "DCLXXIV" (l.41144, 41159). "In the 630s" holds.
- P4: Brehaut's English, verbatim: "the _Etymologiae_, a vast work which he left unfinished, and which I have divided into twenty books, since he wrote it at my request." (BREHAUT l.822-825). The period sits inside the marks, and the source ends there. Brehaut calls Braulio "his friend and correspondent" (l.731-732). The census calls him "editor" (census l.41106).
- P5: the heading "BRAULIONIS NOMINE CONCILII VI SCRIPTA AD HONORIUM I." and "universi episcopi per Hispaniam constituti" (PL80 l.53690-53696). The decree, "quo et robustiores pro fide et alacriores in perfidorum essemus rescindenda pernicie" (l.53733-53737). Toledo VI canon III (HISP l.41728-41768). "artificioso temperamento ... Christianis blanditiis flecteremus" (PL80 l.53774-53777).
- P6: Letter XI. Taio turned "ad convicia et ad contumelias" (PL80 l.52861-52862). "me posse remordere si velim" (l.52896-52897). "Dorsum meum posui ad flagella ... non remaledicebat" (l.52906-52909).

**Card.** I checked these against their lines: `dates` (Ildefonsus XII; HISP eras); `place`; keyWorks 1 (PL80 l.51880-51896 letter list; l.55020); keyWorks 2 (PL80 l.51634-51637; PL96 l.17096-17098); `traces` 1 ("Codicem Etymologiarum ... transmisi", PL80 l.52658-52659); `traces` 2 and 3; `remembered` 1 and 2 (PL80 l.51545-51556); `uncertain` 1 to 4 (PL80 l.51536-51538, l.53836-53838). `uncertain` 1 repeats the brief's ground. Every source named in the brief is in `sources`.

**Agreement with the Isidore profile (era 3 batch 6).** They agree on "friend", on the Etymologies written at Braulio's request and divided by him into twenty books, and on Isidore sending the book on from the road. The Isidore card's open question on the covering letter's addressee does not touch Braulio's `traces` 1, which rests on Isidore's own letter. Neither profile records the held dispute over who wrote the notice of Isidore's works (C-B2). The Isidore profile is not mine to fix. I flag it to the lead for Open-Gaps.

#### Findings

- **C-B1 BLOCKING (brief P5, last sentence, and audio; item 1; source content misreported by omission).** The brief: "He added that the pope's line about dumb dogs that cannot bark came from Isaiah, not Ezekiel." The letter's claim is that the text, which the pope had used to rebuke them undeservedly, does not apply to them at all. The Isaiah point is an aside inside that claim, softened by "though all the prophets speak by one Spirit": "Et licet nos horum quae in objurgationem nostri vestra sanctitas indebite protulit ... nihil omnino respectet, praecipue tamen illud non Ezechielis sed Isaiae testimonium, quanquam prophetae omnes uno proloquantur Spiritu: Canes muti non valentes latrare, ad nos ... nullo modo pertinet" (PL80 l.53781-53787). Heard once, the brief makes Braulio's answer a correction of the pope's citation. Fix: "The pope's rebuke had called them dumb dogs that cannot bark. That did not fit them at all, Braulio answered." (11 and 9 words.)

- **C-B2 BLOCKING (card `uncertain`; records `contested_claims`; item 7; a held dispute missing).** The brief's quote comes from Braulio's notice of Isidore's works, the Praenotatio, which Antonio calls his "praefatio ad sancti pontificis Opera" (PL80 l.51958-51962). A note printed with Antonio's notice records a dispute. It says Gregorius Mayansius held it "falso ... Braulioni tributam" (l.52007-52008, 52036-52040). The note's writer then keeps it as Braulio's, on "veterum quotquot viderim Codicum, ac bibliographorum fere omnium ... consensionem" (l.52054-52061). He is not Antonio: he cites Mayansius's own Life of Nicolás Antonio (l.52039-52040). The brief may keep "Braulio says", since the old manuscripts and nearly all bibliographers agree. The card and records must give both sides.
  - Fix, card, a new last `uncertain` item: "Whether Braulio wrote the notice of Isidore's works. A note printed with Nicolás Antonio's notice says Gregorius Mayansius denied it. The note keeps it as his, as the old manuscripts and nearly all bibliographers agree." (10, 13 and 15 words.)
  - Fix, records `contested_claims`: {"claim": "Braulio's authorship of the Praenotatio librorum Isidori", "sides": ["Mayansius, as reported in a note to Antonio's notice: 'falso eam Praenotationem Braulioni tributam asserit' (PL80 l.52007-52008, 52036-52040)", "The same note: the consensus of the old codices and nearly all bibliographers keeps it as Braulio's (PL80 l.52054-52061); Brehaut treats it as his (BREHAUT l.731-735)"]}. The Brehaut claim's tag becomes "Widely Accepted".

- **C-M1 MINOR (brief P1, sentence 3; item 1; a hedge dropped).** "The king answered that this was God's will." The king writes "si ista in Dei voluntate, ut confidimus, persistunt" (PL80 l.54565-54566). Fix: "The king answered that he trusted this was God's will, and that Eugenius had been born in the city that now needed a bishop." (24 words.)

- **C-M2 MINOR (brief P2; item 7; an inference heard as fact).** Put side by side, P1 and P2 make the archdeacon and Ildefonsus's Eugenius one man. The card (`uncertain` 2) and records (`absent_details` 2) rightly call that a join no held line makes. Ildefonsus XIV does not name Braulio (PL96 l.17048-17067). Fix: add at the end of P2, "Ildefonsus does not name Braulio." (5 words.)

- **C-M3 MINOR (brief P1 and P3; item 10; no time in the who-line until sentence 9).** "Braulio lived in Visigothic Spain in the seventh century" opens P3, after the Ildefonsus paragraph. Fix: P1 sentence 1 becomes "In seventh-century Visigothic Spain, Braulio, bishop of Zaragoza, was losing his sight when King Chindaswinth sent for his archdeacon, Eugenius." (20 words.) Delete the P3 opener. P3 sentence 1 becomes "Ildefonsus says Braulio followed his brother John as bishop of Zaragoza and served about twenty years, under four kings." (19 words.) That also clears "see" (C-M4).

- **C-M4 MINOR (brief P3; item 4; undefined term).** "held the see" will be heard as "sea". Fixed by C-M3's "served".

- **C-M5 MINOR (brief P5, "uphold that law"; item 1; a word past the source).** Canon III names no law. It praises the king's policy and makes each later king promise, before he takes the throne, "hanc se catholicam non permissurum eos violare fidem", and that "quod magnopere nostro est tempore conquisitum, debeat illibatum perseverare" (HISP l.41749-41760). Fix: "Its canon on the Jews made every later king swear to keep it so." (13 words.)

- **C-M6 MINOR (brief P6, sentence 1; item 1; framing sharpened).** "A priest named Taio once wrote to insult him." Braulio says Taio's insults answered his own joke about an ass: "me causa joci ... de illo asino in litteris meis conscripsisse" (PL80 l.52863-52866). Fix: "Braulio once teased a priest named Taio, who answered with insults." (11 words.) To keep the witness, sentence 2 becomes "Braulio could bite back if he wished, he wrote." (9 words.)

- **C-M7 MINOR (card `remembered` 1 and 2; `sources.about`; items 5 and 1).** (a) The chronicle is held in its own edition. Theodor Mommsen prints it as the "Continuatio Hispana a. DCCLIV" (MGH11 l.31309; the passages at l.32613-32626). He says it is known "sub nomine ficticio Isidori Pacensis" (l.16363). The card's "under the name of" is Mommsen's judgment, given no owner. Antonio himself calls the writer "Isidorus Pacensis episcopus" (PL80 l.51540-51541). (b) "sound teaching" renders "piam doctrinam" (PL80 l.51552; MGH11 l.32625), which means devout. (c) Antonio has no role at his first card mention. Fix, `remembered` 1: "Nicolás Antonio, in his Bibliotheca Hispana vetus, quotes a chronicle he gives to Isidore, bishop of Pax. Theodor Mommsen, who edits it, dates it to 754 and calls the name false." (19 and 13 words.) Then: "It says Braulio shone at the fourth council of Toledo, and that Rome later marveled at his eloquence through a letter." (21 words.) `remembered` 2: "The same chronicle says that at the sixth council he poured devout teaching into Christian minds, and that the church still read his short works." (25 words.) Add to `sources.about`: {"title": "Chronicle of 754 (Continuatio Hispana), in Chronica minora II, MGH Auctores antiquissimi XI", "author": "Theodor Mommsen (ed.)", "date": "1894", "language": "Latin", "file": "cic/texts/chronica-minora-2_marcellinus-victor-tunnunensis-biclaro-isidore-mgh-aa-11-lat_mommsen1894.txt"}.

- **C-M8 MINOR (card `dates` and `uncertain` 4; records `absent_details` 1; an honest limit that hides a held range).** Mommsen writes "obiit sub Chindasuintho rege a. 641-652 teste Ildefonso" (MGH11 l.21948-21949). That is an editor's range, not a year, so "No held source gives the year" stays true. The range should still be given. Fix, `uncertain` 4, after "No held source gives the year of his death.": "Theodor Mommsen, from Ildefonsus's list of kings, puts it under Chindaswinth, between 641 and 652." (16 words.) Records note 1 gains: "Mommsen's range 641-652, from Ildefonsus XII (MGH11 l.21948-21949)."

- **C-M9 MINOR (card keyWorks 2 `about`; item 4; a pronoun pointing to the wrong noun).** "commends the memory of the one and the virtue of the other" follows "Aemilian, sent to his brother Fronimian", so "the one" reads as Aemilian and "the other" as Fronimian. Ildefonsus's "memoriam hujus et virtutem illius sancti viri" means Braulio's memory and the holy man's virtue (PL96 l.17096-17098). Fix: "Ildefonsus of Toledo says it keeps Braulio's own memory and makes the holy man's virtue known." (16 words.)

- **C-M10 MINOR (card `uncertain` 4; item 1; a witness given more than he says).** "His name is missing from the acts of the seventh council of Toledo, Antonio notes." True (PL80 l.51535-51537; HISP l.42508-43155 has no Zaragoza signature). But Antonio is first named here without his full name. With C-M7 his first mention moves to `remembered` 1, and `uncertain` comes after `legacy`, so "Antonio" can stand. No text change if C-M7 is taken. Otherwise write "Nicolás Antonio".

- **C-M11 MINOR (card `uncertain` 3; item 1; a source softened).** "a rumor that baptized Jews had been allowed back to their old religion". The letter says the rumor was that this was allowed "oraculis venerabilis Romani principis", back "ad superstitionem suae religionis", and calls it false (PL80 l.53835-53839). Fix: "Braulio's reply speaks of the faithless. It also denies a rumor that a ruling of the Roman prince let baptized Jews return to what it calls their superstition." (6 and 22 words.)

After the fixes (C-B1, C-M1 to C-M6 in the brief): 327 words, about 2:01, FK 6.83, Flesch 70.37, longest sentence 24 words (scratch copy scored). The card fixes add no sentence over 25 words.

---

### Ildefonsus of Toledo (standard; 327 words, about 2:01; FK 7.42, Flesch 68.27)

| # | Item | Result |
|---|---|---|
| 1 | Each sentence sourced | FAIL (C-M13, C-M15) |
| 2 | Quotes verbatim | PASS (none) |
| 3 | No invention | FAIL (C-M13) |
| 4 | Reading aids | FAIL (C-M12, C-M14) |
| 5 | Named witnesses | PASS |
| 6 | Partisan witness marked | PASS |
| 7 | Contested claims both sides | FAIL (C-M16) |
| 8 | Common names | PASS |
| 9 | One term for one thing | FAIL (C-M12) |
| 10 | Story, scene, disputes in place, length | PASS |
| 11 | Readability | PASS |
| 12 | Card order, fields, caveat repeated | FAIL (C-B3, C-B4, C-M16 to C-M20) |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |
| — | Records | FAIL (C-B3, C-B4, C-M16) |

**Sentences checked and found faithful.**
- P1: Julian's Elogium, "sub rudimentis adhuc infantiae ... Agaliense monasterium petiit, cujus fugam rabido furore insequens pater, uno tantum maceriae impeditus est obice ... dum percitus in interiora praetenderet, latibulum ... reliquit ... dum quaesitum non invenit, rediens in propriam, ut perditum deploravit" (PL96 l.3692-3716, left column).
- P2: Antonio, Julian "post Quiricum Hildefonsi successorem Toletanus antistes ... qui eum descripsit coaevus" (PL96 l.649-652). "Percognita ... abstinentia parentali ... monachumque se in eo multis fere annis ... Coenobium quoque virginum ... propriis opibus decoravit. Rector deinde effectus Agaliensis coenobii" (l.3718-3727). "Ildephonsus abbas" at HISP l.44645 (VIII, era 691, l.43163) and l.45659 (IX, era 693, l.45090).
- P3: "Principali post haec violentia Toletum reducitur ... praesul post secundum Eugenium ... nono gloriosi Reccesvinthi principis anno, novem annis et duobus fere mensibus ... decimo Kalendas Februarii ... in ecclesia beatae Leocadiae tumulatur, ad pedes sui conditus decessoris" (PL96 l.3663-3665, 3712-3724).
- P4: "libellum de Virginitate sanctae Mariae contra tres infideles" (l.3678-3680). The preface to On Famous Men, Jerome, "Hunc secutus Gennadius", Isidore, and "ne incurrerem ex silentio damnum ... tenebrosa nube silentii contexissem" (l.16523-16566).
- P5: Cixila's heading, "A Cixilano ejusdem urbis episcopo edita" (l.3733); Antonio, "sub Maurorum tyrannide" (l.652-653). Leocadia before all present, with the king there (l.3812-3843). The Life is said to be late ("written later"), under the later-retelling rule.

**Card.** I checked these against their lines: `dates` (l.3712-3722; Antonio l.655-661; HISP eras); keyWorks 1 to 3 (l.3674-3698; Antonio §9, l.896-904); `remembered` 1 and 2 (l.3812-3847); `remembered` 3 (l.658-659); `uncertain` 1. Every source named in the brief is in `sources`.

#### Findings

- **C-B3 BLOCKING (records `absent_details` 1, "His birth year and family ... No held line gives them"; a false absence).** Antonio: "Natum Toleti ex nobilissimis parentibus Stephano et Lucia Hildefonsum fama fert, sub rege nimirum Witterico, anno hujus saeculi septimo. Lucia soror germana dicitur fuisse Eugenii III, Toletani praesulis" (PL96 l.704-708). He later calls that Eugenius "ejus avunculo" (l.725). The Life by Rodericus Cerratensis, of the thirteenth century by the volume's Monitum (l.3651-3653), says "ex Hispania, civitate Toletana nobilibus parentibus oriundus" (l.4123-4127). These are report ("fama fert", "dicitur") and should be told as such. They exist, so the absence is false.
  - Fix, records: replace `absent_details` 1 with a claim. {"claim": "Report has it (fama fert), Antonio says, that he was born at Toledo to noble parents Stephen and Lucia, in 607 under Witteric; Lucia is said (dicitur) to be the sister of Eugenius, his predecessor, whom Antonio numbers III", "witness": "PL96 l.704-708, 725; Cerratensis l.4126-4127 (Toledo, noble parents)", "formation_confidence": "Inferential-Thin"}.
  - Fix, card, a new `uncertain` item after item 1: "His birth and family. Report has it, Nicolás Antonio says, that he was born at Toledo in 607, to noble parents named Stephen and Lucia. Lucia is said to have been the sister of Eugenius, the bishop before him." (3, 24 and 16 words.) Antonio gets his role at first card mention in `dates`: "Nicolás Antonio, in his Bibliotheca Hispana vetus, reckons these as 659 and 669." (13 words.)

- **C-B4 BLOCKING (records `absent_details` 2, "Where Agali stood ... Julian names the monastery but not its place"; card `place`; a false absence).** Antonio: "in sanctorum Cosmae et Damiani monasterio, quod et Agaliense audiit, ejusdem urbis" (PL96 l.715-718; "Agaliense" at l.717). Cerratensis: "in ecclesia sanctorum Cosmae et Damiani, quae in suburbio sita est Toletano, quae antiquitus Agaliense monasterium dicebatur" (l.4200-4203). Cixila makes him abbot "in ecclesia sanctorum Cosmae et Damiani, quae sita est in suburbio Toletano" (l.3747-3750), without the name Agali. The note is true of Julian alone, but a reader takes it as the limit of what is held.
  - Fix, records: replace `absent_details` 2 with a claim. {"claim": "Agali was the monastery of Saints Cosmas and Damian in the suburb of Toledo, Antonio and Cerratensis say; Julian gives no place", "witness": "PL96 l.715-718; l.4200-4203; Cixila l.3747-3750 (Cosmas and Damian, no name Agali)", "formation_confidence": "Widely Accepted"}.
  - Fix, card `place`: "The monastery of Agali, which Nicolás Antonio and a thirteenth-century Life call the monastery of Saints Cosmas and Damian, near Toledo; Toledo, where he was bishop and was buried in the church of Saint Leocadia" (19 and 16 words by semicolon.) If C-B3 is taken, Antonio's role goes in `dates`, which comes first.

- **C-M12 MINOR (brief P2, sentence 3, and audio; items 9 and 4; two terms for one work, and a doublet).** "Julian's short Life is a tribute, written in his praise." The card calls the work a tribute (`sources.about` 1; `uncertain` 1), and the brief also uses "Life" for Cixila's. "A tribute, written in his praise" says one thing twice. Fix: "Julian's account is a short tribute to him." (8 words.)

- **C-M13 MINOR (brief P1, last sentence, and audio; items 1 and 3; a detail added).** "struck at the monastery with drawn sword". Julian has "Armata deinde manu Agaliensem cellam impetens gladio" (PL96 l.3713-3714). "Drawn" is added. Fix: "Then he attacked the monastery, sword in hand, found nothing, and went home to mourn a lost son." (18 words.)

- **C-M14 MINOR (brief P3 and P4, and audio; item 4; undefined term).** "held the see" and "the great men of his see" will be heard as "sea". Fix: "held the office for nine years and about two months" and "the great men of his church".

- **C-M15 MINOR (brief P5, last sentence, and audio; item 1; a hedge lost).** Cixila hedges the saint's words: "talia fertur depromere vota ... Deo gratias, vivit domina mea per vitam Hildefonsi" (PL96 l.3844-3848). Fix: "She is said to have thanked God that her Lady lived through the life of Ildefonsus." (16 words.) Records claim 11 should quote "fertur".

- **C-M16 MINOR (card `uncertain` 2; records `contested_claims`; item 7; a dispute that may rest on OCR, and a misdescribed witness).** The card says Antonio, "reckoning Julian's years, gives 25 January 669". In the same sentence Antonio quotes Julian's "X Kalendarum Februariarum", then prints "die Januarii 25" (PL96 l.654-659). He reckons the year, not the day. "25" against his own quotation may be an OCR "3" read as "5" or a slip. The Mozarabic calendar in the Missale mixtum puts "X. Obitum domni Ildefonsi epi. Toleto." at the tenth before the Kalends of February (PL85 l.93258). Fix, `uncertain` 2: "His death day. Julian gives the tenth day before the Kalends of February, 23 January, as does the Mozarabic calendar in the Missale mixtum. Nicolás Antonio quotes Julian's day, but the held copy of his notice prints 25 January." (3, 23 and 16 words.) Records: add the PL85 side to the Julian side, and note "OCR '25' in a sentence quoting X Kal. Feb." Flag to the lead as a possible Library OCR point. The brief's "23 January" can stand.

- **C-M17 MINOR (card `uncertain` 3; item 1; a witness told short).** "Whether the abbot Ildefonsus who signed ... is he. Antonio says Ildefonsus was still an abbot at the council of 656." Antonio takes the signatures as his: "inde Toletano concilio viii, anno quinquagesimo tertio, necnon et ix, circa annum 657, ut e subscriptionibus constat" (PL96 l.731-734). His 657 for the ninth is not the acts' era 693, which is 655 (HISP l.45090). The line on 656 is about Quiricus of Barcelona at the tenth council (l.1332-1333). Fix: "Whether he is the abbot Ildefonsus who signed the councils of 653 and 655. The acts give only the name and the title abbot. Nicolás Antonio takes the signatures as his, and puts the ninth council about 657." (13, 10 and 15 words.)

- **C-M18 MINOR (card keyWorks 1 `about` and `uncertain` 4; item 5; Antonio's text and a later note mixed).** keyWorks 1, "Nicolás Antonio's note names them": the naming is in the notice's own text, §9 (l.896-904). `uncertain` 4, "Antonio's notes count some as lost or doubtful": Antonio's text counts works lost (§21-22, about l.1264-1290; §22 opens l.1287). The "inter deperdita, imo et inter dubia" line is a footnote that cites the newest Madrid edition of the Toledo Fathers (l.1324-1327). The witness should be named as what he is. Fix, keyWorks 1: "written, Julian of Toledo says, against three unbelievers. Nicolás Antonio names them as Jovinian, Helvidius and a Jew" (8 and 10 words). `uncertain` 4: "Which of his books survive. Julian lists more than the volume prints. Nicolás Antonio counts several as lost, and a note to his notice counts one as lost or doubtful." (5, 8 and 17 words.)

- **C-M19 MINOR (card `traces` 1; item 4; "his book" points to the wrong man).** "added a chapter on him to his book On Famous Men" reads as Julian's own book. Julian's tribute is "in appendice ad librum de Viris illustribus ab ipso Hildefonso conscriptum" (PL96 l.3663-3664). Fix: "Julian of Toledo, a later bishop of the city, added a chapter on him to Ildefonsus's own On Famous Men." (19 words.)

- **C-M20 MINOR (card `traces` 2; item 4; meaning unclear).** "among them a seventh for the feast of Mary" leaves "seventh" with no noun. Cixila has "missam superscriptam, quae in ejus laude decantaretur, perfecit, quae est septima" (PL96 l.3870-3873). Fix: "Cixila says he composed Masses, among them one to be sung in Mary's praise on her feast, which Cixila counts as the seventh." (23 words.)

After the fixes (C-M12 to C-M15 in the brief): 328 words, about 2:01, FK 7.53, Flesch 67.56, longest sentence 23 words (scratch copy scored). The card fixes add no sentence over 25 words.

---

### Verdicts

- **Braulio of Zaragoza:** NOT CLEAR. 2 blocking (C-B1, the "dumb dogs" answer misreported; C-B2, the held dispute over the Praenotatio missing from the card and records) and 11 minor (C-M1 to C-M11; C-M1 to C-M6 touch the brief and audio).
- **Ildefonsus of Toledo:** NOT CLEAR. 2 blocking (C-B3 and C-B4, false absences for his birth and family and for where Agali stood) and 9 minor (C-M12 to C-M20; C-M12 to C-M15 touch the brief and audio).
- **For the lead (Open-Gaps, not mine to fix):** the era 3 Isidore profile tells the Praenotatio as Braulio's without the held dispute (C-B2). The "25" in Antonio's Ildefonsus notice may be OCR (C-M16). The notes printed in Antonio's notices in PL80 and PL96 come from a later annotator, and that annotator is not named in the held file.

---

## R1 review, part D: Julian of Toledo, Beuno (era 4 Who batch 4)

Reviewer: independent Opus, first sight of these drafts. I edited no profile, records, README or repo file. I made no git, web, paid or model calls, and used local scripts only.

### Method

Bar: `Who_Profile_Pattern.md` checklist 1 to 14; `CLAUDE.md` "Trust and source fidelity" and "Accessible and rigorous"; the Decision-Log Who rulings of 2026-11-12 to 2026-11-14 as summarized in the brief (standard length about 325 words; later-retelling rule; quotation marks only for held English; dates name their owner); the lessons file, sections 1 to 3. For each id I read the `.brief.txt`, `.card.json`, `audio/<id>.audio.txt`, its `records.json` entry and the README lines. I opened every cited line in its vendored file and read it in context, folding two-column interleaves, long s, OCR noise and hyphen breaks.

Files: `ildefonsus-julian-toledo-pl96-lat_migne1862.txt` ("PL96": Antonio's notice l.36858-36912; Felix's Life with the Toledo edition's notes l.37480-37830, and its close l.37340-37450; the monitum l.38129-38145; the Prognosticon preface l.38150-38200; Julian's letter to Idalius l.38200-38380; the dedication to Ervig l.45550-45670; contents l.405-430; "Antonio Lorenza" l.3640, 16518); `collectio-canonum-ecclesiae-hispanae-toledo-iii-lat_1808.txt` ("HISP": Toledo XII to XV, l.47965-53241); `rees_lives-of-the-cambro-british-saints-lat-eng_1853.txt` ("REES": preface l.305-345; contents l.600-645, 840-868; the Welsh Life in English l.13380-13815; Latin Life of Winefred l.9230-9375); `gildas_..._williams1899.txt` l.15500-15572; `mirk_festial-enm_erbe1905.txt` header and l.9385-9440, and a year search of the whole file.

Absence searches across `cic/texts/`: Beuno under "Beuno", "Beino", "Bewnow", "Beunon", "Beunou", "Beunw", "Clynog", "Clynnog", "Celynnog" (only REES, Gildas/Williams, Mirk and a passing note in Stokes's Lismore, l.27913, are relevant; no early witness); Julian's death in PL96 under "pridie Nonas", "Martii", "Egicanis", "obiit" (found: see D-B3); Julian's birth year (none); "Lorenzana", "Rice Rees" (not printed in these files; see D-M4, D-M9); Mirk's date, every 13xx/14xx year in the Mirk file (none for Mirk himself; see D-B5).

Readability comes from `engine.m1.gates.grade_text`, run from the repo root. I applied the suggested brief fixes to scratch copies and scored them again: `/tmp/claude-0/-home-user-CIC-Project/05eab76a-1ca8-5978-bc8b-13971bb600f8/scratchpad/review/D_julian_fixed.txt` and `/tmp/claude-0/-home-user-CIC-Project/05eab76a-1ca8-5978-bc8b-13971bb600f8/scratchpad/review/D_beuno_fixed.txt`.

**Applies to both.** Audio equals the brief with `[calmly] ` at the start and `[warmly] ` at the start of the last paragraph, and nothing else (checked by diff). Card keys are in order; Beuno has no `keyWorks` and no `ownWords`, which is right for him (absent, not empty). No empty or null fields. No card sentence over 25 words (script; Julian `uncertain` 1 is exactly 25). Traditions match the census: Nicene Visigothic Iberia runs 560 to 711, covering Julian's 680s; British and Welsh Christianity runs 451 to 768, covering the note's sixth and seventh centuries.

---

### Julian of Toledo (standard; 323 words, about 2:00; FK 6.61, Flesch 72.42)

| # | Item | Result |
|---|---|---|
| 1 | Each sentence sourced | FAIL (D-B1, D-B2, D-M1) |
| 2 | Quotes verbatim | PASS (no quotation marks; Latin told in reported speech) |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS |
| 5 | Named witnesses | PASS |
| 6 | Partisan witness marked | PASS (Felix's Life named as a Life; card calls it a tribute) |
| 7 | Contested claims both sides | FAIL (D-B3, D-M3) |
| 8 | Common names | FAIL (D-M4, card) |
| 9 | One term for one thing | PASS |
| 10 | Story, scene, disputes in place, length | FAIL (D-M2, no time in the who-line) |
| 11 | Readability | PASS |
| 12 | Card order, fields, caveat repeated | FAIL (D-B1, D-B3, D-M3, D-M4) |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |
| — | Records | FAIL (D-B3, D-M5) |

**Sentences checked and found faithful.**
- P1: the feast of the Passion, "passionis Dominicae festum"; the remote room sought for silence, "remotiorem secreti locum intraremus"; separate beds, "discretis ambo stratibus lectulorum excipimur"; the Gospel read; the passage he cannot now recall, "quem nunc recordari non valeo"; "concutimur, gemimus, suspiramus ... Obortae lacrymae"; Idalius "podagrici doloris contortionibus tabidus, sed multo amplius spe divinae contemplationis erectus" (PL96 l.38216-38269). The telling says what the Latin says.
- P2: "coepimus inter nos quaerere quomodo se habeant animae defunctorum ante illam ultimam corporum resurrectionem" (l.38281-38284); the secretary, "accito notario ... eodem die" (l.38303-38305); the king's departure taking the crowds, "bellica profectio gloriosi principis ab urbe regia turbulentos cuneos populorum secum abegit" (l.38320-38322). See D-M1 for two dropped words.
- P3: the letter at the head of the work (l.38160-38163, 38200-38205); Felix a contemporary and successor after Sisbert (monitum, l.38143-38145); citizen of Toledo, baptized in its principal church, pupil of Eugenius, successor "quarto in loco" of his teacher (l.37506-37515); Gudila "levitae", the wish for monastic life, "aliter in superni numinis fuit judicio" (l.37517-37554).
- P4: after Quiricus (Felix l.37580-37582); first signature at Toledo XII (HISP l.49064, era 719), XIII (l.50783), XIV (l.51683) and XV (l.52960), so the acts themselves bear this out, beyond Antonio (PL96 l.36889-36899); the History of Wamba (l.423-424).
- P6, last sentence: "si post haec et ab ipsis dogmatibus patrum ... in quocumque dissentiunt, non jam cum illis est amplius contendendum" (HISP l.52571-52581); the section heading "De tribus substantiis in Christo manentibus domini Juliani assertio manifesta" (l.51991-51994).
- P7: "Fuit enim vir timore Domini plenus" (PL96 l.37666).

**Card.** I checked these against their lines: `knownFor`; `place` (l.37509-37515); `keyWorks` 1 (Felix l.37703-37710; letter l.38326-38330); `keyWorks` 3 (l.423-424); `traces` 1 to 3 (HISP l.51989-51994; monitum l.38139-38141; Felix's list l.37703-37724; editions l.38177-38182, "religionem ab haereticis impudenter impetitam defenderent"); `remembered` 1 (l.37666-37672) and 2 (Antonio l.36902-36905); `uncertain` 4 (Felix l.37548-37554; note l.37630-37637). `otherNames` "Julianus" is held.

#### Findings

- **D-B1 BLOCKING (brief P5; card `keyWorks` 2 `about`; items 1 and 12; the dedication to Ervig told loosely, so a listener cannot tell what the "rot" is or why the book was written).** The letter does not liken the king to a surgeon who cuts away rotting flesh. Julian writes that he believes the king's clemency wished to copy the surgeon's skill: "Hujus admirabilis medelae peritiam credo vestram ... voluisse imitari clementiam" (PL96 l.45597-45599). The aim is to keep the rot from reaching healthy limbs, "ne locus vulneris sana membra contingat" (l.45592), and the king charges Julian to care for the limbs still healthy, "sanis adhuc membris me praecipis impendere curam" (l.45605). The rot, not the limbs, is what Julian would name the tongues of the Jews: "Horum igitur membrorum evitandam putredinem linguas dixerim Judaeorum" (l.45610-45611). The same sentence says which Jews and why: those "qui promissum ex lege Christum Dei Filium necdum adhuc natum fuisse putant", who argue that the count of years from the world's beginning by the Hebrew books shows the fifth age still running, while they expect Christ in the sixth (l.45612-45617). The brief drops the "credo", the "dixerim", the healthy limbs, the Jews' argument and the book's title. What remains reads as the king cutting away Jews as rotting limbs. That is harsher in one way and vaguer in another than the letter, which is harsh in its own words ("pestilentiosis objectibus garrientes", "detestabilem impietatis errorem"). The card has the same shift ("calls their tongues the rotting limbs a surgeon must cut away").
  - Fix, brief P5 (whole paragraph): "At King Ervig's command he wrote On the Proof of the Sixth Age, against Jews of his day. They counted the years from Creation and said the world was still in its fifth age, so Christ had not yet come. In the opening letter, Julian says he believes the king follows the surgeon, who cuts away rot before it reaches healthy limbs. That rot, he writes, he would call the tongues of the Jews." (69 words; longest sentence 23.)
  - Fix, card `keyWorks` 2 `about`: "three books written at King Ervig's command, against Jews of his day. They reckoned the world was still in its fifth age, so Christ had not yet come. The opening letter calls their tongues the rot a surgeon cuts away before it reaches healthy limbs" (11, 18 and 18 words.)

- **D-B2 BLOCKING (brief P6; README "Julian" line; item 1; a dead pope told as the one answered).** The acts call Benedict "beatae memoriae Romanus papa Benedictus", already dead. He raised his points two years before, "ante hoc biennium", by word to their messenger, not in writing, and they had answered him that same year, "illi jam eodem anno sufficienter congrueque responsum est" (HISP l.51985-51993). "In 688 the bishops at Toledo answered Pope Benedict, who had faulted a statement of their faith" leads a listener to think the pope was alive and received this answer. The card's `traces` 1 ("against Pope Benedict's objections") is fine.
  - Fix, brief P6, first three sentences: "In 688 the bishops met again at Toledo. Pope Benedict, now dead, had raised points against a statement of their faith two years before. One section of their answer bears Julian's name." (8, 17 and 8 words.) The last sentence stays.
  - Fix, README: "Toledo XV's answer to the points Pope Benedict had raised, with a section under Julian's name, is held in the Collectio canonum Ecclesiae Hispanae."

- **D-B3 BLOCKING (card `dates`; records `absent_details` 2; items 1 and 7; a false absence and a one-sided start).** The records say Felix's death notice "is not in the held lines read". It is held. Felix: "pontificatus dignitatem annis decem obtinuit, mense uno, diebus septem. Quique etiam inevitabilis mortis praeventus occasu, anno tertio Egicanis principis, pridie Nonas Martii, aera septingentesima vigesima octava, diem vitae clausit extremum, ac sic in basilica gloriosissimae sanctae Leocadiae virginis sorte sepulcrali est tumulatus" (PL96 l.37355-37360, two columns interleaved; OCR "Noiias", "Mariii", "inbasilioagloriosissimse", "tnmn- latus"). The Toledo edition's note reads it as "die vi" of March, "aera 728 (hoc est anno Dom. 690)", and from the ten years, one month and seven days dates his consecration to 29 January 680, holding he was already bishop when Wamba gave up the throne in 680 (l.37362-37389). Antonio has Quiricus dying in 681 (l.36887-36889). The card gives only Antonio's side.
  - Fix, card `dates`: "Bishop after Quiricus. Felix says he held the see ten years, one month and seven days, and died in the third year of King Egica, in era 728. The Toledo edition's notes read this as 6 March 690, with his consecration on 29 January 680. Nicolás Antonio has Quiricus dying in 681. He signed the councils of Toledo of 681, 683, 684 and 688. No held source gives his birth year" (5, 24, 18, 8, 11 and 7 words.)
  - Fix, records: replace absent detail 2 with a Documented claim, "Felix: death 'anno tertio Egicanis principis, pridie Nonas Martii, aera septingentesima vigesima octava'; burial in the basilica of Saint Leocadia", witness "PL96 l.37355-37360 [OCR 'Noiias', 'Mariii']"; add a contested claim, "When he became bishop", sides "Nicolás Antonio: Quiricus died in 681 (l.36887-36889)" and "The Toledo edition's note: consecrated 29 January 680, from Felix's count (l.37362-37389)".
  - Optional, card `remembered` 2: the same note says the 6 March of Usuard and the old catalogue is his death day, and the Toledo Breviary's 8 March an error (l.37399-37445).

- **D-M1 MINOR (brief P2; item 1; a hedge and a condition dropped, and one verb past the source).** "Tunc ego, ni fallor, urgentibus vobis, accito notario" (PL96 l.38302-38303): "if I am not mistaken" and "at your urging" are lost. "He finished the book" goes past "recordari me contigit. Egi ergo ... quae promisi" (l.38323-38326): when the city quieted, he remembered his promise and did it. Fix: "That same day, if he remembered rightly, Julian called a secretary and set down the questions. He wrote the book, the Prognosticon, when the king rode out to war and the crowds left the city." (+4 words.)

- **D-M2 MINOR (brief P3; item 10; no time in the who-line).** The listener first hears a year in P4. The Prognosticon preface says he "saeculo septimo vixerat" (PL96 l.38181-38182). Fix: "Julian, a seventh-century bishop of Toledo in Visigothic Spain, tells this in his letter to Idalius at the head of the work." (22 words.)

- **D-M3 MINOR (card `uncertain` 3; items 7 and 1; a hedge lost).** The preface reaches 688 or 689 by conjecture, "Quod si conjectura aliquid assequi possumus ... referenda videtur", and says only that Idalius is not known to have come to Toledo except for Toledo XV, "non constat Toletum venisse, praeterquam ad concilium Toletanum xv" (l.38168-38172). Fix: "The year of the Prognosticon. The preface in Patrologia Latina 96 guesses 688 or 689. Idalius is not known to have come to Toledo except for the council of 688, it says." (5, 11 and 16 words.)

- **D-M4 MINOR (card `uncertain` 2; items 8 and 1; a common name unplaced, a softened warning, and a name form no held file prints).** "Isidore Pacensis" can be heard as Isidore of Seville; the edition's note places him "medio saeculo post Felicem auctor" (l.45586-45587, the note on the title). Antonio also says some doubt the story, "subdubitari a quibusdam video", and calls it a rumour among later writers, "Increbuit apud posteros fama" (l.36870-36873). Lorenzana's note warns against believing Isidore Pacensis readily, "ut facile ... credat" (l.37574-37575), not against trusting him at all. PL96 prints the editor as "Antonio Lorenza" (l.3640) and "Antonii Lorenza" (l.16518); PL83 prints "Franciscus Lorenzana cardinalis" (l.106911). None prints "Francisco Antonio Lorenzana". Fix: "Whether he came from a Jewish family. Nicolás Antonio reports this as a story among later writers, from Rodericus of Toledo and Isidore Pacensis, a chronicler of half a century after Felix. Felix does not say it. Some doubt it, Antonio says, but many believe it with reason. The notes of Cardinal Lorenzana's Toledo edition, which Migne follows, warn the reader not to believe it readily, since its source is unknown." (6, 25, 5, 11 and 21 words.) Use the same "Lorenzana" form in `sources.about` 2 and `uncertain` 4.

- **D-M5 MINOR (records claim 7; under-cited and under-tagged).** The four first signatures are in the acts: HISP l.49064 (Toledo XII, era 719, l.49058-49060), l.50783 (XIII), l.51683 (XIV), l.52960 (XV). Fix: cite all four with Antonio, and tag "Documented".

- **D-M6 MINOR (brief length, after D-B1, D-B2, D-M1 and D-M2).** The fixes run to about 375 words. To keep near 2:00 I cut the Gudila sentences from P3 in the scratch copy ("As a boy he was bound ... Felix says."); the monk question stays on the card (`uncertain` 4). This is an editorial choice the drafter may make otherwise.

After the fixes (D-B1, D-B2, D-M1, D-M2, D-M6 in the brief; D-B1, D-B3, D-M3, D-M4 on the card; D-B3, D-M5 in the records; D-B2 in the README): 345 words, about 2:08, FK 6.70, Flesch 73.55, longest sentence 23 words (scratch copy scored).

---

### Beuno (standard; 334 words, about 2:04; FK 4.92, Flesch 81.72)

| # | Item | Result |
|---|---|---|
| 1 | Each sentence sourced | FAIL (D-M7, D-M8) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | FAIL (D-M8, "held" status register) |
| 5 | Named witnesses | PASS |
| 6 | Partisan witness marked | PASS (the Life is named as a saint's Life, and as late) |
| 7 | Contested claims both sides | PASS |
| 8 | Common names | FAIL (D-M9, D-M10) |
| 9 | One term for one thing | PASS |
| 10 | Story, scene, disputes in place, length | FAIL (D-B4) |
| 11 | Readability | PASS |
| 12 | Card order, fields, caveat repeated | FAIL (D-B5, D-M7, D-M11) |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |
| — | Records | FAIL (D-B5) |

**The later-retelling rule.** P2 says plainly, in its third sentence and the brief's sixth, "It is a late telling", and gives Rees's "probably about the twelfth century" with its owner and hedge (REES l.322-323). The card repeats it first in `uncertain`. This passes. D-B4 is about the time of his own life, which a listener does not hear until the end.

**Sentences checked and found faithful.**
- P1: the ford on the Severn, the Englishman, "Cergia", "he immediately returned" (REES l.13527-13533); both quotes match l.13537-13541 word for word. Punctuation sits outside the marks where the source runs on ("abominable", and "theirs".).
- P2: the two manuscripts (l.13414-13415); "The time when these "Lives" were compiled, is not known, but it was probably about the twelfth century" (l.322-323).
- P3: aged parents (l.13399-13401; summary l.622); "a Saint, who was at Caerwent. The name of that saint was Tangusius" (l.13434-13436); gifts from Ynyr Gwent, Maun, Cynan and Temic, with churches built (l.13447-13449, 13519-13524, 13548-13554, 13584-13589).
- P4: Cadwallon and Gwaredauc (l.13636-13641); the woman, the crying child, "the land which you possess ... is a township of the father of the child" (l.13644-13663); the quote "who is in that woman's arms owns that land, and is heir thereof" matches l.13675-13676; the "arrogant answer" and the curse (l.13680-13686); Guideuit's gift of Kelynauc (l.13686-13692).
- P5: the beheading, the raising, the fountain "called, after the name of the maiden, WINEFRED'S WELL" (l.13613-13632); the footnote "A celebrated and copious flowing fountain in Flintshire" (l.13658).
- P6: the note, "He lived in the sixth century ... at Clynog Fawr ... in the year 616", the eleven churches, "Professor Rees's Welsh Saints, page 268" (l.13452-13462).

**Card.** I checked `otherNames` ("Beino" throughout REES; "Beunonus" l.9240), `place` (l.13434, 13522-13524, 13545, 13552, 13585, 13639, 13691), `traces` 1 (l.13458-13462), `traces` 2 (Williams l.15568-15570), `remembered` 1 (Latin Life l.9355-9372; summary l.849, 863-864), `remembered` 3 (l.13775-13781), `uncertain` 2 and 3 (l.13452-13456; l.13616-13619).

#### Findings

- **D-B4 BLOCKING (brief P2 to P6; item 10; no time for his own life until the last paragraph, and the only date heard before it is the twelfth century).** The who-line in P3 has no time. A listener who hears "probably compiled about the twelfth century" in P2 and nothing else until the closing paragraph can take Beuno for a twelfth-century man. The note's centuries belong in the who-line. Moving them also clears the "Rees ... Professor Rees" confusion (D-M9).
  - Fix, brief P3, first sentences: "The Life makes him a Welsh clergyman and a founder of churches. A note in W. J. Rees's edition, quoting a Professor Rees, places his life in the sixth century and into the seventh." (12 and 23 words; "clergyman" is D-M7.)
  - Fix, brief P6: "The same note says Beuno founded the religious house at Clynog Fawr in 616, and it counts eleven churches dedicated to him." (22 words.)

- **D-B5 BLOCKING (card `remembered` 2; records claim 4; item 1; a date from the Library header, which no held text gives).** "John Mirk's English sermon book of about 1403" rests on the header line "Creator: John Mirk (active about 1403)" (Mirk l.2). No other line of the file gives a year for Mirk; I searched every 13xx and 14xx year (only l.25936-26162, the series list, which dates other books). The same batch's Julian record rightly refuses the header's "c.642" because it "rests on no held text"; the Mirk date must meet the same bar. Side note for the lead: the header says Erbe edited from "British Museum MS. Cotton Claudius A. II", but the title page reads "EDITED FROM BODL. MS. GOUGH ECCL. TOP. 4" (l.110). That is a Library header defect for Open-Gaps.
  - Fix, card `remembered` 2: "John Mirk's English sermon book, the Festial, tells the same story of a holy hermit called Bewnow." (17 words.)
  - Fix, records claim 4: drop "Mirk active about 1403", and add "Mirk's date is the Library header's; no held line gives it" to the note.

- **D-M7 MINOR (brief P3; card `knownFor`, `role`; item 1; a word the Life does not use of him).** The Life says he "took orders, and became a clergyman" (REES l.13440). It calls Ynyr Gwent "a disciple and monk to Saint Beino" (l.13445-13446), so he had monks under him, and Williams gives "clas Beuno ... the monastery of Beuno" (l.15569), but "The Life makes him a Welsh monk" goes past the Life's words for him. Fix: brief as in D-B4; card `knownFor`: "Welsh clergyman and founder of churches, as the late Welsh Life tells him. A note in W. J. Rees's edition says he founded the religious house at Clynog Fawr in 616." (12 and 19 words); card `role`: "Clergyman; founder of churches".

- **D-M8 MINOR (brief P2, last sentence; item 4; status register).** "The other held accounts of him are late as well" uses the project's word "held", which a listener does not know. Fix: "The few other accounts of him are late as well." (10 words.)

- **D-M9 MINOR (brief P6, card `dates`; item 8; two Reeses heard once).** "A note in Rees, from Professor Rees's Welsh Saints" puts W. J. Rees and a second Rees in one breath. No held file gives the professor's first name ("Rice Rees" is not printed). The D-B4 fix names them apart. Fix, card `dates`, first sentence: "A note in W. J. Rees's edition, quoting a Professor Rees's Welsh Saints, puts his life in the sixth century and into the seventh." (24 words.)

- **D-M10 MINOR (brief P4; item 8; a common name unplaced).** "A king named Cadwallon" can be heard as another Cadwallon. The Life says he was Cadvan's son and "king after him", and Cadvan "king of North Wales" (l.13637-13641). Fix: "Cadwallon, king after his father Cadvan, gave him land in Arvon, and Beuno began to build." (16 words.)

- **D-M11 MINOR (card `dates`, last sentence; item 1; a death day read past the Life).** The Life says that "as the life-time of Beino was ending, and his last day approaching, on the seventh day after Easter, he saw heaven opening" (l.13783-13785). It gives the day of his vision, with his end near. Fix: "The Life sets his last vision on the seventh day after Easter, as his end drew near, and gives no year" (21 words.) Optional: the note gives his festival as April 21 (l.13457-13458).

After the fixes (D-B4, D-M7, D-M8, D-M10 in the brief; D-B5, D-M7, D-M9, D-M11 on the card; D-B5 in the records): 342 words, about 2:07, FK 4.88, Flesch 80.97, longest sentence 23 words (scratch copy scored). The draft already ran 334.

---

### Verdicts

- **Julian of Toledo:** NOT CLEAR. 3 blocking (D-B1 the dedication to Ervig told loosely, losing what the "rot" is and why the book was written; D-B2 a dead pope told as the one answered; D-B3 a false absence of Felix's death notice, and a one-sided start of his episcopate) and 6 minor (D-M1 to D-M6).
- **Beuno:** NOT CLEAR. 2 blocking (D-B4 no time for his own life until the end, after a twelfth-century date; D-B5 Mirk's "about 1403" taken from the Library header) and 5 minor (D-M7 to D-M11). The later-retelling rule is met: the brief says early and plainly that his record is late.

---

