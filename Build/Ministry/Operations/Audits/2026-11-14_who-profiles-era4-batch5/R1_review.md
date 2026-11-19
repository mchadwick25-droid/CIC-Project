# R1 review: era 4 Who batch 5

Round 1 of at most three, by two fresh Opus agents that had not seen the drafting, at full effort, in two parts. Part A covers Sophronius of Jerusalem, Athanasios the Athonite, Sebeos and Antony of Choziba, with the checks that apply to all eight. Part B covers Moses bar Kepha, Alopen, Thomas of Marga and John of Nikiu, with the README. Totals: 10 blocking and 60 minor (part A 3 and 32, part B 7 and 28). The changes made are in `R1_changes.md`.

## R1 review, part A: Sophronius of Jerusalem, Athanasios the Athonite, Sebeos, Antony of Choziba (era 4 Who batch 5)

Reviewer: independent Opus, first sight of these drafts. I edited no profile file. I made no git, web, paid or model calls, and used local scripts only.

### Method

Bar: `CLAUDE.md` in full; `Who_Profile_Pattern.md` checklist 1 to 14; the Decision-Log Who profile entries of 2026-11-12 to 2026-11-14 and their cap rulings; the rulings block of `Who_Scan_Era4.md`; the coordinator calls in the brief (Athanasios major; Sophronius, Antony not major; Sebeos a recorder; Sebeos's authorship question tagged contested; Sophronius his own man beside the approved Maximus card). Form follows era 4 batch 3's `R1_review.md`. A false absence is blocking wherever it sits; a missing identifier is minor.

For each id I read the `.brief.txt`, `.card.json`, `audio/<id>.audio.txt` and the `records.json` entry, and opened every cited line in its vendored file with 15 to 60 lines around it. Files: PG 87.3 (`john-moschus_pratum-spirituale-sophronius-opera-grc-lat_migne-pg87-3.txt`, "PG87.3"), Mansi 10 ("MANSI10"), NPNF 2.14 ("NPNF14"), Theophanes PG 108 ("THEOPH"), Eutychius PG 111 ("EUTYCH"), Renaudot 1713, Charon 1911, Meyer 1894 ("MEYER"), Peeters 1917-1919 ("PEETERS"), Brosset 1849, Macler 1917 ("MACLER17"), Palamas PG 150, Macler 1904 ("MACLER04"), Gelzer-Burckhardt 1907, Hoffmann 1880, Braun 1900, Analecta Bollandiana 7 ("AB7"), Georgirenes 1678, the Horologion of 1851 and Nikodemos's Synaxaristes vol. 1 (1900).

The Greek of MEYER and AB7 is badly garbled, as their headers say. No Greek is quoted in any reader-facing text of these four. I checked each Greek-based claim against the Greek as far as it reads, and against Meyer's German and the AB7 Latin: Athanasios's rule on the letters, the lavra in his cell, his reluctance, the reproach, the oath and the "martyr's end" (MEYER l.5381-5408, 5457-5476); his testament (l.6578-6587, 6646, 6666); George's "Τέκνον Ἀντώνιε" and "ὁ τρόπος" (AB7 l.11925-11926, 35345). All hold, except the points in A-M24 and A-M25.

Absence searches across all of `cic/texts/`: Sophronius with "abominatio desolationis" and "abomination of desolation" (hits read: only Theophanes, Papebroch quoting him, and Nicephorus Callistus); Mary of Egypt with Menaea/Triodion forms in PG87.3; Athanasios with Athonit-, Lavra/Laura/Lawra (60+ files listed, the likely ones read: Acta SS June 5, Bessarion, PO 16, Georgirenes 1678); Sebeos with whitespace-tolerant S-e-b-e-o-s and accented forms (11 files, every relevant hit read); Choziba with ch-o-z-i-b, Koziba, Cuziba, Chuziba, Chozeb-, Χοζεβ/Χοζιβ (12 files, every hit read). "Houze" and spaced forms in AB7.

Readability is from `engine.m1.gates.grade_text`, run from the repo root. I applied the brief fixes below to scratch copies and scored them again: `/tmp/claude-0/-home-user-CIC-Project/e2402255-0732-5843-bbde-cb8d08b63388/scratchpad/fixA/`.

**Applies to all (all eight ids checked here, not only part A's four).** A script confirmed that each audio file equals its brief with `[calmly] ` at the start and `[warmly] ` at the start of the last paragraph, with matching trailing newlines. No tag appears in any brief or card. Every brief passes `grade_text`: Sophronius FK 8.10 / Flesch 66.64; Athanasios 7.11 / 68.56; Sebeos 6.65 / 74.20; Antony 5.88 / 77.72; Moses bar Kepha 6.76 / 71.59; Alopen 7.50 / 63.10 (the thinnest margin); Thomas of Marga 6.46 / 74.90; John of Nikiu 6.46 / 73.82. Lengths: Athanasios 405 words (the cap, major); Alopen 359 (major); the six non-majors 346 to 356, about 2:08 to 2:12, which is a little over the 327-346 of earlier batches but inside 1 to 2 minutes plus a few seconds. All eight cards are in the batch's field order (name, otherNames, knownFor, dates, place, tradition, role, briefLength, keyWorks, legacy, uncertain, sources), matching the approved batch 2 and 3 cards. No field is null or empty; Antony's card rightly has no otherNames, Alopen's no keyWorks. Every `sources` file exists and holds the named work. Every brief fix below must be carried into the audio. Sentences over 25 words in my four briefs: Sebeos 26 and 28, Antony 27 (A-M19, A-M26); the long sentences in the other four belong to part B.

---

### Sophronius of Jerusalem (353 words, about 2:10; FK 8.10, Flesch 66.64)

| # | Item | Result |
|---|---|---|
| 1 | Each sentence sourced | FAIL (A-B1, A-M9) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | FAIL (A-M1, A-M2, A-M3, A-M4) |
| 5 | Witness named, not a role | FAIL (A-M6) |
| 6 | Partisan witness marked | PASS (Theophanes placed as early ninth century) |
| 7 | Contested both sides | PASS, with A-M5 |
| 8 | Common names | FAIL (A-M7) |
| 9 | One term | PASS |
| 10 | Story, scene, length | PASS |
| 11 | Readability | PASS |
| 12 | Card order, caveat repeated | FAIL (A-M8: sources incomplete) |
| 13 | Audio tags | PASS |
| 14 | List line, Who test | PASS (own works and a following) |

**Sentences checked and found faithful.** Stephen of Dor at Calvary, the oath, the Saracen hindrance and "from end to end of the earth" to the apostolic see (MANSI10 l.91434-91464; heading "Libellus Stephani Dorensis episcopi" l.967). The poem: Phoenicia and Damascus, parents dead and named Myro and Plinthas, no marriage or children, a monk in the precinct of Theodosius in the hills of Jerusalem, and the cure of his eyes (PG87.3 l.47785-47800; Mai's note l.47805-47809). Moschus's "Sophronio Sophistae" (l.3757), Papebroch's "magistro suo Joanne Moscho" (l.24647), and the identity of the Sophist with the patriarch, which Papebroch, Fabricius (l.3562-3570) and Charon ("paraît bien indiscutable", Charon 1911 l.21284-21286) all hold. Sergius to Honorius on Sophronius at Alexandria, the two operations, the Fathers he could not bring, and the agreement of silence (PG87.3 l.25645-25707). The synodal letter on quiet and on clergy, monks and laity who forced him "more tyrannico" (l.26236-26248, 26458-26462). The Christmas sermon (l.30713-30723). Theophanes on the pledge for Palestine (THEOPH l.61809-61812). Eutychius on four years in office (EUTYCH l.84234-84252) and on the second year of Umar (l.83882). Constantinople III, Session XIII: the card's two quotations are word for word (NPNF14 l.25716-25724). Card items checked: Papebroch's 634 and March 638 (l.25527-25529, 26127-26134); the note in Mansi on May 633 (MANSI10 l.68215-68218); Mai's "circa annum Christi 640" (PG87.3 l.44131); Fabricius-Harles "ab a. C. 629 ad 638" and "monachus S. Sabae" (l.24200-24201); the Bibliotheca Patrum note on 14 March 636 (l.30436); Symeon of Thessalonica via Papebroch (l.25483-25512); Leontius via Papebroch (l.25184-25191); Maximus on "Divinus ergo magnusque Sophronius" and on Africa (MANSI10 l.72546-72549, 72701-72702); Renaudot (l.17086-17088); John of Damascus and Nicaea II citing the Miracles (PG87.3 l.24289-24291, 44147-44148); the Meadow under his name (l.3562-3570, 24448-24453); Papebroch on the Life of Mary of Egypt (l.25414-25425). The profile stands apart from the approved Maximus and John Moschus cards and agrees with the Moschus card on the Meadow and the burial at Saint Theodosius.

**Findings.**

- **A-B1 BLOCKING (brief P5; items 1 and 4; a pronoun that changes what the source says).** "When Umar asked to see the temple Solomon built, Theophanes says, Sophronius wept, and called it the abomination of desolation in the holy place." THEOPH l.61821-61828: "lemplum a Salomone constructum ... sibi ostendi postulavit. Hunc cum Sophronius vidisset : Hæc est vere, inquit, abominatio desolationis a propheta Daniele praenuntiata, quae modo stat in loco sancto; multaque simul lacrymarum copia ... Christianam gentem deflebat." "Hunc" is masculine and means Umar; the temple (neuter) would be "hoc". The brief's "it" makes Sophronius call Solomon's temple the abomination, where Theophanes has him say it of the caliph standing in the holy place. Fix: "When Umar asked to be shown the temple Solomon built, Theophanes says, Sophronius looked at him and wept. This is truly the abomination of desolation, he said, standing in the holy place." ("simul" = at the same time; "him" can only be Umar.) The card's `uncertain` 1 needs no change.
- **A-M1 MINOR (brief P1; item 4).** "if you let his faith be put at risk". MANSI10 l.91455-91456: "si distuleris & postposueris fidem ejus periclitantem": the faith is already in danger, and the charge is delay and neglect. Fix: "if you hold back while his faith is in danger."
- **A-M2 MINOR (brief P1; item 4, an undefined term).** "until he reached the apostolic see." A general listener cannot place it. The synod Stephen addresses is at Rome (MANSI10, the Lateran acts). Fix: "until he reached the apostolic see at Rome."
- **A-M3 MINOR (brief P3; item 4, quotation marks and a pronoun).** 'texts of the Fathers that said "two" in those very words' puts quotation marks on a word of Latin ("duas nominatim et ipsis verbis operationes", PG87.3 l.25688-25690), which the house rule keeps for held English. In "Sergius says it was agreed that he would speak no more", "he" can be heard as Sergius. The first sentence is also 25 words. Fix: "Sergius, patriarch of Constantinople, wrote that Sophronius held two operations. Sophronius could not, he says, bring texts of the Fathers that spoke of two in those very words. It was agreed, Sergius says, that Sophronius would speak no more of one or two."
- **A-M4 MINOR (brief P4; item 4, a pronoun with no antecedent).** "kept them from it" has no "them" before it. PG87.3 l.30709-30715: "Nos ... prohibemur, sed vel inviti ... domi manere cogimur; ... Saracenico metu absterriti". Fix: "but fear of the Saracen sword kept him and his people at home."
- **A-M5 MINOR (brief P3; item 7).** The brief gives Constantinople in Sergius's words only; `records.json` carries a contested_claim with Eutychius on the other side (EUTYCH l.83850-83853: after gifts from Cyrus, "mutata sententia sua, adversus Sophronio factus"). The brief names its owner, so nothing is told as settled, and the card carries Eutychius. Optional fix, if length allows: after the P3 silence sentence add "Eutychius, a later patriarch of Alexandria, says Sergius turned against him after gifts came from Cyrus." and in P5 shorten "Eutychius, a later patriarch of Alexandria, says" to "Eutychius says". This adds about 16 words.
- **A-M6 MINOR (card `dates` and `uncertain` 2; item 5).** "Mansi's editor says he was still a monk in May 633." The note at MANSI10 l.68215-68218 is unsigned in the print and written in the first person of the collection's editor; "Mansi's editor" is a role, and could be Mansi himself. Fix, both places: "A note in J. D. Mansi's collection of the councils says he was still a monk in May 633."
- **A-M7 MINOR (card, first mentions; item 8).** `dates`: "Theophanes" is bare. `uncertain` 2: "Fabricius and Harles" are bare surnames. `uncertain` 4: "Sergius" is bare, and "gifts came from Cyrus" follows a key work on the martyrs Cyrus and John, so it can be heard as the martyr. Fixes: `dates` "Theophanes puts" -> "Theophanes, writing in the early ninth century, puts"; `uncertain` 2 "Fabricius and Harles give 629." -> "Johann Albert Fabricius, in Harles's edition of his Bibliotheca Graeca, gives 629." (PG87.3 l.24196 "Biblioth. Graec. ed. Harles"; the approved John Moschus card uses "Johann Albert Fabricius"); `uncertain` 6 "Fabricius and Harles say" -> "Fabricius says"; `uncertain` 4 "Sergius says" -> "Sergius, patriarch of Constantinople, says" and "after gifts came from Cyrus" -> "after gifts came from Cyrus, patriarch of Alexandria" (EUTYCH l.83838 "Cyrum patriarcham Alexandrinum").
- **A-M8 MINOR (card `sources`; item 12).** `remembered` 4 cites Eusèbe Renaudot and `uncertain` 5 cites Cyrille Charon; neither is in `sources`. Add to `about`: {"title": "Historia patriarcharum Alexandrinorum Jacobitarum", "author": "Eusèbe Renaudot", "date": "1713", "language": "Latin", "file": "cic/texts/renaudot_historia-patriarcharum-alexandrinorum-jacobitarum-lat_1713.txt"} and {"title": "Histoire des patriarcats melkites, volumes 2 and 3", "author": "Cyrille Charon", "date": "1911", "language": "French", "file": "cic/texts/charon_histoire-des-patriarcats-melkites-t2-t3-fra_1911.txt"}. In `uncertain` 5, Charon calls the identity "bien indiscutable" (l.21284-21286), and no held source denies it. Fix: "Whether the Sophist of John Moschus is the patriarch. Papebroch and Angelo Mai hold that they are one man, and Cyrille Charon calls it hardly open to doubt. No held source says otherwise. The poem and the Miracles give the author as a monk of Theodosius from Damascus."
- **A-M9 MINOR (card `uncertain` 7; item 1).** "given to him by Nicephorus Callistus and the Greek service books". Papebroch names Nicephorus Callistus only (PG87.3 l.25414-25417), and records.json holds no line for the service books; I found none in PG87.3's Menaea and Triodion mentions. Fix: "The Life of Mary of Egypt is given to him by Nicephorus Callistus. Papebroch says nothing in it settles whether it is his." Restore the service books only with a held line.

**Post-fix.** With A-B1 and A-M1 to A-M4: 370 words, about 2:17; FK 7.87, Flesch 67.08; longest sentence 24 words. If the coordinator wants it nearer 355, the Eutychius sentence in P5 can go (the card's `dates` carries it).

---

### Athanasios the Athonite (405 words, about 2:30, major; FK 7.11, Flesch 68.56)

| # | Item | Result |
|---|---|---|
| 1 | Each sentence sourced | FAIL (A-M10, A-M11, A-M12, A-M14) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | FAIL (A-M13) |
| 5 | Witness named, not a role | PASS |
| 6 | Partisan witness marked | PASS (the Life marked as the Life, through Meyer, throughout) |
| 7 | Contested both sides | PASS, with A-M10 |
| 8 | Common names | PASS |
| 9 | One term | PASS |
| 10 | Story, scene, length | PASS (405 = the cap) |
| 11 | Readability | PASS |
| 12 | Card order, caveat repeated | PASS |
| 13 | Audio tags | PASS |
| 14 | List line, Who test | PASS (founder, rule, testament, following) |

**Sentences checked and found faithful.** P1 against the rule's Greek (MEYER l.5385-5408): Nikephoros sent against the Cretans; letters "πλειστάκις", then "γράμμασι πυκνοτέροις" when he would not yield; on the island, the lavra "ἐν τῷ κελλίῳ", so that Nikephoros might become a monk on Athos; "ἐλευθερίως καὶ μεμονωμένως βιοῦν"; "ἀγαπητὸν γὰρ ἐλογιζόμην εἰ ἐμαυτὸν σώσαιμι". "Arabs of Crete" is Meyer's ("gegen die Araber in Creta", l.1322). P2 against Meyer l.1225-1308: the Life by a Lavriot under Eustratios, known to Meyer only in Agapios's Modern Greek of Venice 1657; Abramios of Trebizond, orphaned, raised in Constantinople and "zum Lehrer bestimmt"; Michael Maleinos of Kyminas, uncle of Nikephoros; the flight when Michael wanted him as successor. P3: Meyer's July 960 to March 961 and his "Sage" (l.1330, 1340-1350). P4: the coronation and the half-built church (Typikon l.5455-5457, Meyer's reckoning l.1350-1368); "ὡς ἄνωθεν ἄλλα διαλογιζομένου σου ... ἄλλα διωρίζου ἡμῖν" (l.5460-5461); the oaths, "μόνον λέγων ... ἡμιτέλεστον καταλείψῃς" and "μαρτυρικῷ τέλει" (l.5464-5476); 16 December 969 (l.15485-15486). P5: "αὐτοδέσποτον" and "nur unter dem Hegumenos stehend" (l.1432-1437, 5675-5677); the Life's charge before Emperor John (l.1404-1405); the Tzimiskes ruling's complaint against "Ἀθανασίου ... τῆς βασιλικῆς λαύρας τῆς οὕτω λεγομένης τὰ Μελανά" (l.7577-7583), the two signatures (l.8152-8153), and Meyer's 972 "nach der Unterschrift" (l.1726-1728); "für die andern Athosklöster im Allgemeinen maassgebend" (l.1005-1009). P6: the dome and the keystone, six companions, "Als Leichen", 997 to 1011 (l.1410-1416, 1447-1450). P7: "Μετὰ λύπης ὑπερβαλλούσης διήνυσα πάσας τὰς ἡμέρας τῆς ζωῆς μου ... ἀνίκανον τῆς ἀσθενοῦς μου ψυχῆς εἰς τὸ προΐστασθαι ἑτέρων" (l.6585-6587). Card items checked: Peeters's "circa annum millesimum" (PEETERS l.1805-1806); George the Hagiorite on the kitchen, the church a mile off, "magno Athanasio" and John's charge (l.1003-1007, 1054-1071, 1764-1767), and the Life dated about 1045 (l.655-657); Meyer on Theodore of Stoudios (l.1043-1047, 1615-1616) and on the first great house being Greek (l.4752-4753); Iviron in Athanasios's lifetime (l.4783-4787); the testament's John and Euthymios (l.6646, 6666) and its date under Basil II (l.15489-15493); the Hypotyposis doubt (l.15497-15500); Brosset (l.15412-15413) and Macler 1917 (l.14096-14098) on his origin; the Palamas codices (PG 150 l.52597-52599).

**Findings.**

- **A-M10 MINOR (brief P4; items 1 and 7; witness detached).** "Athanasios went to Constantinople and blamed him to his face." The paragraph opens "By Meyer's reckoning", so the reproach can be heard as Meyer's; it is the rule's, and the Life tells it differently (records contested_claim; MEYER l.1394-1395). Fix: "Athanasios went to Constantinople, his rule says, and blamed him to his face." To hold the 405 cap, P2 "Philipp Meyer, the German scholar who edited his writings in 1894," -> "Philipp Meyer, who edited his writings in 1894,".
- **A-M11 MINOR (brief P5 and card `keyWorks` 1; item 1).** "Nikephoros's charter, which Athanasios copied into his rule" and "with Nikephoros's charter copied into it". The rule quotes the charter's key passages, "καθὼς αὐταῖς λέξεσιν οὑτωσὶ περιέχει τὸ χρυσοβούλλιον" (MEYER l.5642-5643; again l.5782-5783); it does not copy the whole. Fix: brief "which Athanasios quotes in his rule"; card "with passages of Nikephoros's charter quoted in it".
- **A-M12 MINOR (brief P3; item 1).** "A manuscript printed in the notes to Leo the Deacon's history". Meyer says only that a manuscript Hase brought to light is cited there: "Nach einem Msc., das Hase ans Licht gezogen ... (Leon Diak. notae S. 426)" (l.1340-1344). Fix: "A manuscript cited in the notes to Leo the Deacon's history", as the card's `uncertain` 2 already says.
- **A-M13 MINOR (card `uncertain` 6; item 4).** 'His own rule calls Michael, uncle of Nikephoros, "my abbot"' puts quotation marks on the profile's English of "τοῦ ἐμοῦ καθηγουμένου" (l.5381), with no "in modern words" beside it. Fix: "His own rule calls Michael, uncle of Nikephoros, his abbot at Mount Kyminas."
- **A-M14 MINOR (card `knownFor`; item 1, and item 4 on Dominant Modern Reconstruction).** "the first great monastery of the Holy Mountain" is Meyer's (l.4752-4753, records DMR) and is told unowned. Fix: "Founder of the Lavra on Mount Athos, with the help of his friend the emperor Nikephoros Phokas. Philipp Meyer calls it the first great monastery of the Holy Mountain. Athanasios wrote its rule and his own testament for it. Meyer says that rule became the general standard for the other houses of Athos." ("Athanasios", not "He", after a sentence whose subject is Meyer.)
- **A-M15 MINOR (held material not used; card `legacy`).** Joseph Georgirenes, archbishop of Samos, in the English of 1678, says the Laura was "built by Athanasius", the first who "founded a College" on Athos, and that the monks tell "a long Story, how this Athanasius, wanting Money to go on with the great Church of the Monastry, which he had begun, was met with by the Blessed Virgin", who told him "take no care for necessaries, she would provide" (georgirenes_present-state-samos-nicaria-patmos-athos_denton1678.txt l.3966-4010, 4486-4488). It is not a false absence, since no line denies it, but it is the one held witness of how the Mountain itself remembered him. Fix: add to `remembered`: "Joseph Georgirenes, archbishop of Samos, wrote in 1678 that the monks of Athos told a long story of how the Virgin met Athanasios when he lacked money to finish the great church, and promised to provide." Add to `sources.about`: {"title": "A Description of the Present State of Samos, Nicaria, Patmos, and Mount Athos", "author": "Joseph Georgirenes (English tr., translator not named)", "date": "1678", "language": "English translation", "file": "cic/texts/georgirenes_present-state-samos-nicaria-patmos-athos_denton1678.txt"}.
- **A-M16 MINOR (records.json).** Testament witness "l.6573-6574, 6624, 6645-6646": Melana is at l.6578, John at l.6646, Euthymios at l.6666 (l.6624 is Nikephoros's chrysobull). The George the Hagiorite witness for the nominative "magnus Athanasius" that the card quotes is l.2860; l.1057 reads "magno Athanasio". Fix the line numbers.

Not findings: the brief tells Trebizond with its owner ("By that Life") and the card carries Brosset's and Macler's Georgian reading. Peeters says Brosset misread the Moscow Greek Life on another point (PEETERS l.920-923), which does not touch the card.

**Post-fix.** With A-M10 to A-M12: 405 words, about 2:30; FK 7.05, Flesch 68.98.

---

### Sebeos (346 words, about 2:08, recorder; FK 6.65, Flesch 74.20)

| # | Item | Result |
|---|---|---|
| 1 | Each sentence sourced | FAIL (A-B2, A-M20) |
| 2 | Quotes verbatim | PASS (no quotation marks in brief or card) |
| 3 | No invention | PASS |
| 4 | Reading aids | FAIL (A-B2, A-M17, A-M18, A-M19) |
| 5 | Witness named, not a role | PASS |
| 6 | Partisan witness marked | PASS (Macler's "avant tout celle d'un prêtre" on the card) |
| 7 | Contested both sides | PASS (the three books: Stephen and the title against Macler) |
| 8 | Common names | PASS |
| 9 | One term | PASS |
| 10 | Story, scene, length | PASS |
| 11 | Readability | PASS |
| 12 | Card order, caveat repeated | FAIL (A-B2: the brief drops the caveat the card keeps; A-M21) |
| 13 | Audio tags | PASS |
| 14 | List line, Who test | PASS (recorder) |

**Sentences checked and found faithful.** The Cross at Jerusalem: weeping and sighing, a great flame in the hearts, the king, princes and people, no one able to sing the hymns, the Cross set back in its place (MACLER04 l.6144-6153). The title "Histoire d'Héraclius par l'évêque Sebeos" (l.166-167). Macler's "seul écrivain arménien du VIIe siècle qui raconte les premières invasions des Arabes en Arménie" and the eyewitness (l.252-256); the third quarter of the century, after Baumgartner (l.326); the end at Muawiya, 661 (l.300). Stephen of Taron's list, "die Geschichte des Herakl, die durch Bischof Sebeos geschrieben worden ist" (Gelzer l.200-201), and "Étienne de Taron est du Xe siècle" (MACLER04 l.376). The editions on one Etchmiadzin manuscript, and the citations by Giragos and Tchamtchean (l.354-359); the three books, book I "manifestement pas de Sebeos", book II a compilation of Moses and Stephen, book III alone Sebeos's (l.427-433, 479-484). The prisoners from Arabia (l.6752-6753); the evils of our time and the burning wind, "Et nous l'avions mérité, car nous avons péché contre le Seigneur" (l.8141-8145); later writers drawing on the book (l.264-265); the closing words (l.9009-9011). Card items: "au petit bonheur" (l.270-271); "valeur historique incontestable" and no dates (MACLER17 l.1019-1021); the chronology "très obscure" (l.6127); Hoffmann and Braun on the assembly at Khosrau's court (Hoffmann l.6503-6510; Braun l.14985-14988); the unnamed bishop at Dvin (l.8519-8580). The authorship question is tagged Contested with a contested_claim, as the coordinator required.

**Findings.**

- **A-B2 BLOCKING (brief P4; items 1, 4 and 12; a hedge dropped and a note moved to the wrong passage).** "Macler notes that Sebeos sees the invasion as God's punishment of the Greeks, for not keeping one faith with the Armenians." Macler's note opens "Bien qu'il ne le dise pas explicitement" (MACLER04 l.6510-6516); the brief drops that hedge and "notes" hardens his reading into an observation. The card's `uncertain` 6 keeps it ("He says Sebeos never states it outright"), so brief and card disagree. The note is also anchored to the Greek rout after the crossing of the Jordan, "Une frayeur inspirée par le Seigneur s'empara de l'armée des Grecs" (l.6472-6484, mark (3)). The brief sets it right after Sebeos's own "we had deserved it, for we sinned against the Lord" (l.8144-8145), from another chapter, where "we" are not the Greeks, so the listener hears Macler glossing a line he does not gloss. Fix: delete the sentence from P4 and open a new paragraph before "Sebeos names one source": "After the Greeks crossed the Jordan, Sebeos writes, a terror sent by the Lord seized their army. Macler takes him to see the invasion as God's punishment of the Greeks, for not keeping one faith with the Armenians. Sebeos never says so outright, Macler adds." ("Arrivés au Jourdain, [les Grecs] le franchirent", l.6472.)
- **A-M17 MINOR (brief P3; item 4, a relative clause that can take the wrong man).** "The second copies Moses of Khoren and Stephen, who wrote three centuries after Sebeos." "who" can be heard as both men; Macler says it of Stephen's work only ("ce dernier écrivit jusqu'en 1004; son ouvrage est donc de trois siècles postérieur à Sebeos", l.432-480). Fix: "The second copies Moses of Khoren and also Stephen, whose work, Macler notes, came three centuries after Sebeos."
- **A-M18 MINOR (brief P5; item 4, a one-line beat paragraph).** "Later writers, Macler says, drew on his book as a source." stands alone as a paragraph before the close. Fix: delete P5 and put the sentence in P3 after the Stephen sentence: "Later writers, Macler says, drew on the book as a source."
- **A-M19 MINOR (brief P2; item 4, length and a pronoun).** "Frédéric Macler, who put it into French in 1904, calls him the only Armenian writer ..." runs 28 words. Fix: "Frédéric Macler put it into French in 1904. He calls Sebeos the only Armenian writer of the seventh century who tells of the first Arab invasions of Armenia." To pay for A-B2 without losing a fact the card lacks, also cut "Macler names no see for him, and gives no years for his birth or death." (the card's `dates`, `place` and `uncertain` 3 carry it) and "made from one manuscript at Etchmiadzin," (the card's `keyWorks` carries it).
- **A-M20 MINOR (brief P4; item 4, a count).** "Sebeos names one source." is a count no one has made over the whole book; Macler says only that he names no written source (l.262-264). Fix: "For the first Arab wars, Sebeos names his witnesses." (The prisoners' line closes Macler's chapter XXX, on the Arab rise, l.6752.)
- **A-M21 MINOR (card `otherNames`; item 12).** "Bishop Sebeos" is his name with a title, not another form of it. Fix: drop `otherNames`; the field is then absent.
- **A-M22 MINOR (held material not used; card `keyWorks` or `uncertain`).** Macler in 1917 lists a second copy: "Le n° 52 des manuscrits de la bibliothèque des PP. Mkhitharistes de Vienne (Autriche) renferme l'histoire de Sebéos et des extraits de Moïse de Khorèn et d'Étienne de Tarôn" (MACLER17 l.361-364). The card's "The two printed editions rest on one manuscript at Etchmiadzin" stays true. Fix: add to `uncertain` 1, after the Stephen of Taron sentence: "In 1917 Macler listed a second copy, in the Mekhitarist library at Vienna, with extracts of Moses of Khoren and Stephen of Taron."
- **A-M23 MINOR (records.json).** The Cross witness "l.6116-6143" is l.6144-6153 (l.6116-6143 are the chapter heading and footnotes).

**Post-fix.** With A-B2 and A-M17 to A-M20 (six paragraphs): 358 words, about 2:12; FK 6.57, Flesch 73.43; one 26-word sentence remains (the P1 crowd sentence, a close paraphrase; it may stand).

---

### Antony of Choziba (349 words, about 2:09, recorder; FK 5.88, Flesch 77.72)

| # | Item | Result |
|---|---|---|
| 1 | Each sentence sourced | FAIL (A-B3, A-M24, A-M27, A-M29) |
| 2 | Quotes verbatim | PASS (no quotation marks in brief or card) |
| 3 | No invention | FAIL (A-M24) |
| 4 | Reading aids | FAIL (A-M25, A-M26) |
| 5 | Witness named, not a role | FAIL (A-M28, A-M29) |
| 6 | Partisan witness marked | PASS (he tells the invasion through George) |
| 7 | Contested both sides | PASS (none) |
| 8 | Common names | PASS |
| 9 | One term | PASS, with A-M24 (friend/companion) |
| 10 | Story, scene, length | PASS |
| 11 | Readability | PASS |
| 12 | Card order, caveat repeated | PASS |
| 13 | Audio tags | PASS |
| 14 | List line, Who test | PASS (recorder, two works) |

**Sentences checked and found faithful.** Against the AB7 Latin and what reads of the Greek: Raithou, the Saracen raids on the public roads, the holy fathers' advice, Choziba, reception by the abbot and tonsure soon after, and the companion leaving for Raithou unknown to him (l.11934-11949); George, come to the coenobium on a Sunday, taking him aside: "locum ... sed mores" / "ὁ τρόπος", "non pater mater aut cognati aut amici, sed voluntas", "Nullus nobis assistet in die illa magna et tremenda, sed solum actiones cujusque" (l.11925-11965); "Τέκνον Ἀντώνιε" (l.35345); "rogat Ubi est Antonius ... in eo enim sum ut moriar" (l.37866-37868); the Persian siege, flight to Arabia, Stephen the Syrian "centum annorum vel amplius" killed in another ravine, George let go as "pauperem et debilem atque modestum" (l.11775-11850, Greek "ἀπέλυσαν" l.11880); the Jericho xenodochium, cellarer, "commercio versabar cum mundanis et feminis, impugnatus violenter", the secret journey to the holy city and George's "verboque et opere me curavit ac retinuit" (l.12388-12425); the close of the Miracles, "cum non sim sapiens neque sermonis facultate valeam ... Deus autem dives et liberalis non dedignatus est et super me inutilem ac insipientem ... exiguam hanc guttulam effundere benedictionis" (l.39489-39500). Card: the preface on "sinceritatis characteres", the Latin version and the "graeco-barbara" words (l.7941-7957); the closing prayer (l.38201); Moschus's cells of Choziba (PG87.3 l.5217-5219). No other held source names Antony (Choziba search above: Cyril of Scythopolis, Evagrius, Nicephorus Callistus, Moschus, the Horologion and Nikodemos name the place, John or George, never Antony). The Persian sack by Antiochus Strategos (Conybeare 1910) is a different author.

**Findings.**

- **A-B3 BLOCKING (card `legacy.traces` 1; item 1, a false absence).** "His Life is the only held account of George of Choziba". Nikodemos the Hagiorite's Synaxaristes gives George a notice of his own, from his leaving home for Jerusalem to his monastic life and death at the monastery "τοῦ Χοζεβᾶ" (nikodemos-hagiorite_synaxaristes-vol1-sep-feb-grc_1900.txt l.48570-48610), and the Horologion keeps his feast, "τοῦ ὁσίου Πατρὸς ἡμῶν Γεωργίου τοῦ Χοζεβίτου" (horologion-to-mega_venice-edition-grc_koutloumousianos1851.txt l.16458-16465). records.json's own absent_details note names both. Fix: "His Life is the one full held account of George of Choziba; Nikodemos the Hagiorite's Synaxaristes gives George a short notice. It is also one of the held accounts of the Persian invasion as the desert monks lived it." Add to `sources.about`: {"title": "Synaxaristes, volume 1 (September to February)", "author": "Nikodemos the Hagiorite", "date": "1900", "language": "Greek", "file": "cic/texts/nikodemos-hagiorite_synaxaristes-vol1-sep-feb-grc_1900.txt"}. (The Horologion's line dates George to "τὰς ἀρχὰς τοῦ Θ'", which reads as the ninth century but may be an OCR numeral; it should not go on the card, and Antony's own Persian-invasion anchor stands.)
- **A-M24 MINOR (brief P1, P3; items 1, 3 and 9).** "with one friend his own age": the Latin has "comite tantum uno ex consortibus meis" (l.11935-11936), a companion, with no age; the Greek at that point does not read. The later "socio meo" (l.11946) is a companion too. Fix: P1 "with one friend his own age and none of his family knowing" -> "with a single companion and none of his family knowing"; "Later his friend slipped away" -> "Later his companion slipped away"; P3 "When Antony wanted to follow his friend" -> "When Antony wanted to follow his companion".
- **A-M25 MINOR (brief P2; items 1 and 4, process narration and a witness on the wrong side).** "In the Greek, George calls him his child Antony, and when dying he asks where Antony is." The first half reads in the Greek (l.35345); the second reads only in the Latin translation (l.37866-37868). "In the Greek" is also the kind of how-the-text-survives narration item 4 lists. Fix: "In the Life, George calls him his child Antony, and when dying he asks where Antony is."
- **A-M26 MINOR (brief P2; item 4, length).** "He is Antony of Choziba, a monk who lived through the Persian attack on Jerusalem and wrote the Life of his teacher, George of Choziba, in Greek." runs 27 words. Fix: "He is Antony of Choziba, a monk who lived through the Persian attack on Jerusalem. He wrote the Life of his teacher, George of Choziba, in Greek."
- **A-M27 MINOR (brief P6; item 1, an attribution told as settled).** "He also wrote down miracles of the Mother of God at Choziba." The authorship rests on the Bollandist heading ("ANTONIO HOZEBITA AUCTORE", "eodem auctore Antonio", l.38275-38278), as the card's `keyWorks` 2 says. Fix: "The same volume prints, under his name, miracles of the Mother of God at Choziba." The next sentence's "he" is still Antony.
- **A-M28 MINOR (brief P2; card `keyWorks` 1, `remembered` 1, `sources`; item 5).** "C. Houze" stands only in the Library file header (l.2). The volume's OCR has no "Houze" in any spacing, and the preface speaks as the Bollandists, "Analectis nostris inserimus, addita versione latina" (l.7954). The name is the editor's in fact, but no held line of the volume carries it. Fix: either log in Open-Gaps that the editor's name rests on the file header and keep it, or write "The Bollandists edited it in 1888, with a Latin translation" in the brief, "edited by the Bollandists" in `keyWorks` 1, "The Bollandist editors find that the Life plainly bears the marks of sincerity" in `remembered` 1, and "Société des Bollandistes" as the preface's author.
- **A-M29 MINOR (card `uncertain` 2; items 1 and 5).** "The opening of the Life is lost in the held copy" has no records witness, and chapter 1 on George's homeland and parents is present ("patria et parentes; initium vitae ejus mona[sticae]", l.8052, with the chapter heading at l.8095). "the editor's headings" is a role. Fix: "His name appears in the Life where George speaks to him, and in the Bollandist headings." Restore the second sentence only with a line that shows what is lost.
- **A-M30 MINOR (card `legacy.traces` 2; item 1).** "John Moschus, in his Spiritual Meadow, tells stories of monks who lived in the cells of Choziba." It is true (PG87.3 l.5217-5219), but nothing in it traces to Antony; it is context for the place. Fix: delete it from `traces`, and drop the Spiritual Meadow from `sources.about` unless another field cites it.
- **A-M31 MINOR (records.json).** The Jericho claim quotes "[post inv]asionem Persarum"; the file reads "Acriter 886. asionem Persarum" (l.12407). The bracketed letters are a restoration and should be marked as one in the claim. "After the invasion" in the brief rests on that restoration; the sense is likely, given the caves and the Saracen and Hebrew dangers just before (l.12404-12406).
- **A-M32 MINOR (README line 7).** "Antony of Choziba is a recorder too, known only from his own Life of George of Choziba." The card has two works. Fix: "known only from his own writings, the Life of George of Choziba and the Miracles printed after it under his name."

**Post-fix.** With A-M24 to A-M27: 350 words, about 2:09; FK 5.94, Flesch 76.37; no sentence over 25 words.

---

### README (lines about part A's four)

Checked against `cic-website/data/world-census.json`: "The Byzantine Imperial Church (Heraclian & Iconoclast Eras)" runs 622-843 and does not name Sophronius in voices, people or text; "Chalcedonian Monasticism - Judean Desert & Gaza" runs c. 450-614, holds John Moschus in voices and people, and its long description ends "In 614 the Persian army sacked Jerusalem and tore through the desert houses. Those who lived wrote down what was lost."; "The Byzantine Imperial Church (Macedonian Era)" (843-1054) and "Athonite & Comnenian Byzantine Monasticism" (era 5, c. 963-1300) both list Athanasios the Athonite as a voice; "Armenian Christianity before the Bagratids" runs c. 554-884 and "Bagratid Armenian Christianity" begins c. 884; no other era 4 Armenian movement exists. The scan's "Armenian Apostolic" for Sebeos (Who_Scan_Era4.md l.52) is no census name. The word counts (405; 359; the six at 346 to 356) are right. The Renaudot line behind "a ninth-century Sophronius of Alexandria" ("poft annos prope du« centos", l.17088-17089) holds. One finding, A-M32 above.

### Verdict

Part A: **3 blocking** (A-B1 Sophronius, A-B2 Sebeos, A-B3 Antony) and **32 minor** (A-M1 to A-M32: Sophronius A-M1 to A-M9, Athanasios A-M10 to A-M16, Sebeos A-M17 to A-M23, Antony and the README A-M24 to A-M32). Athanasios has no blocking point. Not approved to proceed until the three blocking points are fixed and independently rechecked. Every quotation in the four briefs and cards was checked against its vendored file; the two Percival quotations on the Sophronius card and the Latin "magnus Athanasius" are word for word.

---

## R1 review, part B: Moses bar Kepha, Alopen, Thomas of Marga, John of Nikiu (era 4 Who batch 5)

Reviewer: independent Opus, first sight of these drafts. I edited no profile file. I made no git, web, paid or model calls, and used local scripts only.

### Method

Bar: `CLAUDE.md` in full; `Who_Profile_Pattern.md` checklist 1 to 14; the Decision-Log Who profile entries of 2026-11-12 to 2026-11-14; the rulings block of `Who_Scan_Era4.md`; the coordinator calls in the brief. Alopen is a major (cap about 405 words). The other three are not majors. Thomas of Marga and John of Nikiu are recorders at standard length. Form follows the era 4 batch 3 `R1_review.md`. As in earlier rounds, a false absence and a claim credited to the wrong man or the wrong work are blocking. A missing common-name identifier is minor.

For each id I read the `.brief.txt`, `.card.json`, `audio/<id>.audio.txt` and the `records.json` entry. I opened every cited line in its vendored file and read 15 to 30 lines around it. Files, with the short names used below: Masius's Latin in PG 111 ("PG111"); Bar Hebraeus, Abbeloos-Lamy vol. 1 and 3 ("BH1", "BH3"); Mai vol. 10, Bar Hebraeus's Nomocanon ("MAI10"); Assemani BO 1, 3.1, 3.2 ("ASS1", "ASS3-1", "ASS3-2"); Harris-Mingana 1920 ("HM"); Harris 1911; Budge's Philoxenus 1894; Malech 1910, with Wylie's stele and S. Wells Williams ("MALECH"); Yule-Cordier 1903 ("YULE"); Budge, Monks of Kublai Khan ("BUDGE28"); Chabot 1895; Budge, Book of Governors vol. 2 ("BG"); Mari, Gismondi 1899 ("MARI"); Labourt 1904; Mingana 1926; Wigram 1910; Charles 1916 ("CHARLES"); Evetts's History of the Patriarchs in PO 5 ("HP5") and in the v1 file ("HP1"); Renaudot 1713; Evetts 1895 ("EVETTS"); the census, `cic-website/data/world-census.json` ("CENSUS").

Absence searches across all of `cic/texts/`, whitespace-tolerant and in Latin and other forms:
- Moses: `bar[ -]*k[eé]pha|bar[- ]*c[eé]pha|barc[eé]pha|bar[ -]*kipha|bar[ -]*kaipha` (22 files, every one opened at its hit); `Kiyon`, `Beth[- ]*Ceno`, `Beth[- ]*Kion`.
- Alopen: `A[ -]*lo[ -]*p[eéu]n|O[ -]*lo[ -]*p(u|e|a|ue)n|Alopen|Olopuen|Olopen|Olopan|O-lo-pen` (14 files; the non-Alopen hits are "colophon", "Holophernes" and "Olops"); `hui[ -]*yao|huiyao|T'ang[ -]*hui` (no hit).
- Thomas: Seleucia, Ctesiphon, Mahoze and Bagdad across BG, read wherever Thomas, Abraham, "secretary" or "copying" stand within four lines; `puer` in ASS3-1.
- John: `Nikiou|Nikiu|Niciu|Nakius|Nakyus` in the Coptic, French and Latin files; Benjamin's return in HP1 and Renaudot.

Readability is from `engine.m1.gates.grade_text`, run from the repo root. I applied the brief fixes below to scratch copies and scored them again: `/tmp/claude-0/-home-user-CIC-Project/e2402255-0732-5843-bbde-cb8d08b63388/scratchpad/fixB/`.

**Applies to all four.** A script confirmed that each audio file equals its brief with `[calmly] ` at the start and `[warmly] ` at the start of the last paragraph. No tag appears in a brief or card. Every brief fix below has to be carried into the audio. All four cards are in Mark's order (`name` to `sources`), with no null or empty field. Alopen has no `keyWorks`, and the field is left out. Every `sources` file exists and holds the named work. "No source used here" on the cards is the approved house form and is not flagged. The drafts carry no list lines, so the list-line half of item 14 was not checked.

---

### Moses bar Kepha (356 words, about 2:12; FK 6.8, Flesch 71.6)

| # | Item | Result |
|---|---|---|
| 1 | Each sentence sourced | FAIL (B-B1, B-M1, B-M2) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | FAIL (B-M2) |
| 4 | Reading aids | FAIL (B-M4, B-M5) |
| 5 | Named witnesses | FAIL (B-M5) |
| 6 | Partisan witness marked | PASS |
| 7 | Contested claims both sides | PASS (year of death: 903 and 913 both told, with the editors' reading named) |
| 8 | Common names | FAIL (B-M3, B-M7) |
| 9 | One term for one thing | PASS |
| 10 | Story, scene, disputes in place, length | PASS |
| 11 | Readability | PASS |
| 12 | Card order, fields, caveat repeated | PASS (`uncertain` 1 repeats the 903/913 caveat) |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |
| — | Card and records | FAIL (B-B2, B-M6, B-M8) |

**Sentences checked and found faithful.**
- P1: the question of where paradise lies is at PG111 l.38224-38227. Basil's sermon, "ad Orientem versi inter orandum stetimus, ut oculos nostros ad contemplandum paradisum assuefaceremus", is at l.38236-38240. The church builders and the sun rising in Nisan are at l.38259-38264. Ephrem's paradise that rings the earth beyond the Ocean is at l.38269-38274. The speaker is Moses's own book throughout, and Latin is told without quote marks.
- P2: "Severus episcopus Beth-Raman, qui et Moses Bar-Cepha ... appellatur, sanctarum Scripturarum commentator" is at BH1 l.22836-22837 and l.23005. "qui interpretatus est totum volumen bibliorum ... necnon libros dialecticae" is at BH3 l.12459-12465.
- P3: the anonymous life through Assemani BO II, with about ninety years, forty years, the three sees "Ninivitiae ditionis", and ten years as visitor of Tagrit's church "proprio tunc episcopo viduatae", is at BH1 l.22841-22856. Assemani BO II is not held (checked: only BO 1, 3.1 and 3.2 are in `cic/texts/`).
- P4: the twelfth of Shebat, February, is at BH1 l.23006 and BH3 l.12591. Mar Sergius, "quod Moallak appellant", is at BH3 l.12592-12594. The editors' 903 and their "mendum ... in notatione numerali" are at BH1 l.22864-22876.
- P5: "COMMENTARIA DE PARADISO AD IGNATIUM FRATREM" and "sancte frater Ignati" are at PG111 l.37059-37074. His aim, "accurata et clara ... singula capita ... divisa ... neque per oblivionem aliquid ... amittant", is at l.37121-37126. Masius's 1569 printing is at BH1 l.22887-22889.
- P6: the Nomocanon heading, Bar Hebraeus's (MAI10 l.38229-38250), and "Commentaria mar Ephraemi, et mar Iohannis, et Moysis Barcephae, et Barsalibaei" among the books of the teachers read in the church (l.44295-44296, 44342-44344).
- P7: the quotation is verbatim at HM l.1173-1176.

**Card.** I checked these against their lines: `dates` (BH1, BH3 as above); `place` (BH1 l.22846-22856, l.22876-22880 for the Tigris opposite Balad and the mother from Balad); `legacy.traces` 1 to 4 (MAI10 l.44342-44344; Budge 1894 l.915-923; Harris 1911 l.1203-1205; PG111 l.36967-36968; ASS3-1 l.35640-35644, where Nasicha teaches Ebedjesu "in Dialectica"); `legacy.remembered` 1 to 3 (BH3 l.12459-12461 "religiosissimus"; BH1 l.22841-22842 "inter celebriores ... scriptores jure censeatur"; PG111 l.36999-37001); `uncertain` 2 (ASS1 l.109577-109580), 3, 4, 5 (BH1 l.22902-22906, 22983-22993), 6 and 8 (PG111 l.36981-36983; ASS1 l.109573-109577). The contested claims hold.

**Findings.**

- **B-B1 BLOCKING (brief P1; item 1; a claim credited to the wrong man by a pronoun).** "Basil said we face east to pray, to train our eyes on paradise. Some, he added, think church builders prove it, since they lay out churches to face the sun rising in the month of Nisan." The nearest "he" is Basil, so the listener hears Basil adding the church builders. In the Latin, Moses quotes Basil, then Gregory of Nyssa, then Severus, and only then says in his own voice "Sunt etiam qui hinc constare existiment, paradisum in Oriente esse, quia qui templa ... construere volunt ad Orientem spectantia ..." (PG111 l.38259-38264). Fix: "Others, the bishop added, think church builders prove it, since they lay out churches to face the sun rising in the month of Nisan." (With B-M3, the sentence before reads "Basil, the brother of Gregory of Nyssa, said we face east to pray, to train our eyes on paradise.")

- **B-B2 BLOCKING (card `keyWorks` 3 `about`; item 1; the wrong work).** "Commentary on the liturgy ... J. Rendel Harris and Alphonse Mingana quote a line from it in English." HM says the line is from "his tract on the Mysteries of Baptism" (HM l.1173-1174). The brief and the card's own `sources` entry rightly say "his tract on baptism". The Abbeloos-Lamy list names the liturgy commentary as item 5 and an exposition of the mysteries of the monks' tonsure as item 8 (BH1 l.22907, 22915-22916). It names no tract on baptism. Fix: in `keyWorks` 3, "named in the list of his works given by Abbeloos and Lamy. It is not among the sources used here." Add a fourth entry: `{"title": "On the Mysteries of Baptism", "about": "a tract named by J. Rendel Harris and Alphonse Mingana, who quote one line of it in English, as a Mr. Aytoun gives it"}`.

- **B-M1 MINOR (brief P3 and card `place`; item 1; a name form not held).** "Beth Kiyonaye". No held file has this form. The forms held are "Beth-Chinne seu Beth-Chiuc" (BH1 l.22849, OCR) and "Beth-Ceno", in Migne's heading (PG111 l.36955) and in Assemani (ASS1 l.109574-109575). Fix, in both places: "Beth Raman, Beth Ceno and Mosul".

- **B-M2 MINOR (brief P1; items 1 and 3).** "as a ring of light circles the moon". The Latin is "non aliter atque lunae orbis lunam cingit" (PG111 l.38273-38274). It says a ring, and "of light" is added. Fix: "as a ring circles the moon".

- **B-M3 MINOR (brief P1; item 8).** "Basil" is bare in the brief, and several Basils lived. Moses names him with "ejus fratrem Gregorium Nyssenum" (PG111 l.38231-38232). Fix: "Basil, the brother of Gregory of Nyssa, said we face east to pray".

- **B-M4 MINOR (brief P4; item 4, print register).** "One part of his chronicle, as printed, gives the year 913". "As printed" is process narration, and the sentence is true without it, since the editors' next sentence explains the slip. Fix: "One part of his chronicle gives the year 913, and another gives 903." The card's "as printed" in `dates` and `uncertain` 1 may stay.

- **B-M5 MINOR (brief P7; items 4 and 5).** The closing sentence runs 33 words with its quote. It also leaves out whose English it is: HM says "Mr. Aytoun reminds us that ... Moses Bar Kepha in his tract on the Mysteries of Baptism" and then gives the line (HM l.1172-1176). The records name Aytoun, but the brief and card do not. Fix: "J. Rendel Harris and Alphonse Mingana quote a line from his tract on baptism, as a Mr. Aytoun gives it. It tells the one baptized that "thou goest down to baptism one person, and comest up another instead, the new instead of the old"." In the card's `sources.ownWords` 2, make the author "Moses bar Kepha; Mr. Aytoun (tr.), as quoted by J. Rendel Harris and Alphonse Mingana (ed.)".

- **B-M6 MINOR (card `uncertain` 1 and 7; item 1).** (a) "Andreas Masius gave 913, as Joseph Assemani reports him." Assemani has "anno Graecorum 1224 ... hoc est, anno a Christo nongentesimo decimo quarto (aut decimo tertio)" (ASS1 l.109577-109584). He reports 914, or 913. Fix: "Andreas Masius gave 914 or 913, as Joseph Assemani reports him, and Assemani later wrote 903." (b) "Andreas Masius at first placed him not long after John Chrysostom". No line gives an order. The preface Migne prints is Masius's own, and it says "his non multo posterior mihi videtur" (PG111 l.37011). Renaudot calls this a bad mistake, "Valde autem hallucinatus est Masius" (l.36979). Fix: "Andreas Masius, in the preface Migne prints, thought him not much later than John Chrysostom. Eusèbe Renaudot calls this a great mistake, and Migne's heading puts him about the middle of the tenth century."

- **B-M7 MINOR (card `uncertain` 7; items 4 and 8).** "Bar Hebraeus names him in the time of the patriarch Dionysius and the maphrian Athanasius." "Maphrian" is undefined, and both names are common. BH1 has Dionysius ordained in 898 from the monastery of Beth Botin (BH1 l.22830-22834). BH3 has Athanasius the maphrian die the year after Moses (BH3 l.12596-12598). Fix: "Bar Hebraeus names him in the time of the patriarch Dionysius, ordained in 898, and of Athanasius, the maphrian, the church's head in the east."

- **B-M8 MINOR (card `sources`, `legacy.traces` 4 and records; held matter left out).** Three held lines bear on him and are not used. (a) Mitchell's English quotes Moses at length on Bardaisan's five entities and says "Moses bar Kepha died 903 A.D." (`ephraim_prose-refutations_mitchell1912-1921.txt` l.2652-2656). That is a fourth held passage in his own words, and a further witness for 903. (b) Malech says of the catholicos Abd Ishu, elected about 963, "He was a pupil of Moses Bar Kepha" (MALECH l.15325-15328). Assemani's Bar Hebraeus, which `legacy.traces` 4 cites, makes him a pupil of Nasicha, who was Moses's disciple (ASS3-1 l.35640-35644). (c) Howard gives Renaudot's report that "Moses Barcepha finds fault" with priests striking their foreheads at the invocation (`howard_christians-of-st-thomas-and-their-liturgies_1864.txt` l.13385-13393). Fix: add (a) to `sources.ownWords` and to the 903 side of the contested claim. Add to `uncertain`: "Malech makes 'Abdisho' Moses's own pupil. Bar Hebraeus, as Assemani quotes him, makes him a pupil of Moses's disciple Nasicha." (c) may stay out.

After the fixes (B-B1, B-M1 to B-M5 in the brief): 369 words, about 2:16, FK 6.7, Flesch 71.4 (scratch copy scored). That is about thirteen words over the longest non-major in earlier batches. No fact needs to go. If a cut is wanted, the editors' names in P3 can go, since P2 and P4 name them.

**Verdict: NOT CLEAR** (two blocking).

---

### Alopen (major; 359 words, about 2:13; FK 7.5, Flesch 63.1)

| # | Item | Result |
|---|---|---|
| 1 | Each sentence sourced | FAIL (B-B3, B-M9, B-M13) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | FAIL (B-M12) |
| 5 | Named witnesses | PASS |
| 6 | Partisan witness marked | PASS (the stele is told as his own church's monument) |
| 7 | Contested claims both sides | FAIL (B-M10, a hedge dropped) |
| 8 | Common names | FAIL (B-M11) |
| 9 | One term for one thing | PASS |
| 10 | Story, scene, disputes in place, length | PASS (under the cap; see B-M15 on what is left out) |
| 11 | Readability | PASS (thin margin; 63.95 after the fixes) |
| 12 | Card order, fields, caveat repeated | PASS (`uncertain` 1 and 2 repeat the one-witness and 635/636 caveats) |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS (founder of a mission, known through his church's record) |
| — | Card and records | FAIL (B-M14, B-M15) |

**Sentences checked and found faithful.**
- P1: "Observing the azure clouds, he bore the true sacred books; beholding the direction of the winds, he braved difficulties and dangers." is verbatim (MALECH l.13681-13684). 635, Chang-an, Duke Fang Hiuen-ling, the official staff, the west border, the guest brought in, translation in the imperial library, study "in his private apartments" and "special orders for its dissemination" are at l.13684-13693. The 781 date is at l.14141-14142.
- P2: "Composed by King-Tsing, A Priest of the Syrian Church" is at l.13562-13564. Wylie as translator is at l.770-771. 781 less 635 is 146 years, which is "nearly a century and a half".
- P3: the decree of the seventh month of 638 is at l.13692-13711. "Right principles have no invariable name, holy men have no invariable station", "The Greatly-virtuous Olopun, of the kingdom of Syria", "his sacred books and images", "purely excellent and natural" and "which shall be governed by twenty-one priests." are all verbatim.
- P4: Kautsung, churches in every province and "making him the great conservator of doctrine for the preservation of the State." are verbatim (l.13737-13741). "honorans Olopuen titulo Episcopi magnae legis, quae gubernat regnum Sinae" is at ASS3-2 l.35966-35967.
- P5: 699, the Buddhists, the eastern capital, 713, slanders in the western capital, and the emperor who restored the timbers and stones are at MALECH l.13743-13757.
- P6: 635 is at YULE l.2939 and 2964; 636 at ASS3-2 l.55232-55233. Hirth's "O-lo-pen = Ruben, Rupen?" is in Cordier's bracketed note at YULE l.2944. Assemani's "Olopuen Sinicum nomen est, si bene conjicio, ex Syriaco Jab-allaha formatum" is at ASS3-2 l.35913-35914, and "suggests" keeps his "si bene conjicio".
- P7: the closing verse is verbatim (MALECH l.14028-14031).

**Card.** I checked these against their lines: `knownFor` (apart from B-M13); `dates`; `place` (YULE l.2933-2935, 2967-2968, with "apparently" kept); `legacy.traces` 1 to 3 (MALECH l.13738-13757, 14249-14252); `legacy.remembered` 2 (BUDGE28 l.12436-12437) and 3 (Chabot l.1320-1344, inside Chabot's quotation of Lamy); `uncertain` 2 (BUDGE28 l.1844, 1882, 5174; BH3 l.9523), 4 (BUDGE28 l.5211-5214), 5 (ASS3-2 l.35910-35912, where "cujus etiam effigiem" can take Olopuen as antecedent), 6 (MALECH l.14277-14279) and 8 (MALECH l.14212-14232).

**Findings.**

- **B-B3 BLOCKING (brief P2; card `uncertain` 1; README, the majors paragraph; item 1; a false absence).** Brief: "All that is known of him comes from that one stone, the Xi'an stele." Card: "Everything about him comes from one witness, the Xi'an stele of 781". README: "everything known of him comes from the one stele". The drafter's own records say otherwise: "The Tang huiyao, which the census cites for the decree, is not held." The census entry says "a missionary the Chinese records call Alopen" and cites "Tang huiyao (Institutional History of the Tang), ch. 49, edict of 638" (CENSUS l.41481, 41537). So a second witness exists, outside the Library. What is true is that every held mention goes back to the stele. My search found the stele in Wylie, Yule, Assemani, Budge, Chabot's Lamy, Williams and Wigram 1929 (l.4183-4190), and no other source. Fixes:
  - Brief P2: "His story is told on that stone, the Xi'an stele." (With B-M9, P2 then reads: "The man was Alopen, of the Church of the East. His story is told on that stone, the Xi'an stele. His own church raised it nearly a century and a half after he came. Its Chinese text names its author as King-Tsing, a priest. A. Wylie put it into English, and calls him Olopun.")
  - Card `uncertain` 1: "Everything the sources used here say of him goes back to one witness, the Xi'an stele of 781, set up by his own church nearly a century and a half after he came. Its Chinese text names King-Tsing, a priest, as its author. The Tang court's own record of the 638 decree is not among the sources used here. No words of his own are held, and nothing of his death."
  - README: "everything the held sources say of him goes back to the one stele, and the brief runs to what it carries."

- **B-M9 MINOR (brief P2; item 1).** "whom the stone calls Olopun". The stone is in Chinese. Olopun is Wylie's English spelling of the name, and the card says so in `otherNames`. The fix is folded into B-B3 above.

- **B-M10 MINOR (brief P6; card `uncertain` 3 and 7; item 7, a hedge dropped).** "Yule takes the name Alopen for a Chinese form of Rabban, meaning monk." Yule has "Olopan (probably a Chinese form of Rabban — Monk)" (YULE l.2939). Card `uncertain` 7, "Monk is Yule's and Budge's word", is half right: Budge calls him "the monk A-lo-pen" (BUDGE28 l.1881), but Yule calls him "the missionary" and reads "monk" only from the name. Fixes: brief, "Yule thinks the name is probably a Chinese form of Rabban, meaning monk." Card `uncertain` 3, "Yule thinks Olopan probably a Chinese form of Rabban, meaning monk." Card `uncertain` 7, "Monk is Budge's word, and Yule reads it in his name. Bishop is Assemani's word, and priest Lamy's."

- **B-M11 MINOR (brief P4; card `uncertain` 4 and 8; item 8, bare scholar names).** The brief has "Kircher" and the card has "Kircher", "Saeki" and "Dr. Bridgman", all bare. Held: "Kircher, Athanasius. China ... Illustrata" (YULE l.46324); "Professor P. Y. Saeki" (BUDGE28 l.1062); "Dr. E. C. Bridgman" (MALECH l.14227-14228). Fix: "Athanasius Kircher", "P. Y. Saeki", "E. C. Bridgman", at first mention in each text.

- **B-M12 MINOR (brief P4 and P6; item 4).** P4 has a colon-reveal: "has another title: bishop of the great law that governs China." P6's "Wylie's stele" reads as if Wylie owned the stone. Fixes: P4, "The Latin that Athanasius Kircher published, as Joseph Assemani gives it, names a different title. It calls him bishop of the great law that governs China." P6, "Wylie's English of the stele gives 635 for Alopen's arrival, and so does Yule." (Henry Yule is named in full earlier once B-M15 is applied.)

- **B-M13 MINOR (card `knownFor`; item 1).** "The emperor had them translated and ordered the religion spread." The stele says only "the sacred books were translated in the imperial library" (MALECH l.13689-13690), and the card's own `uncertain` 6 says so. Fix: "The books were translated in the imperial library, and the emperor ordered the religion spread."

- **B-M14 MINOR (card `sources`; item 12).** `uncertain` 2 cites "the editors of Bar Hebraeus, J. B. Abbeloos and T. J. Lamy" for 636 (BH3 l.9519-9523). No `sources` entry carries them. Fix: add `{"title": "Chronicon ecclesiasticum, volume 3, editors' notes (Latin tr. J. B. Abbeloos and T. J. Lamy)", "author": "J. B. Abbeloos and T. J. Lamy", "date": "1877", "language": "Latin", "file": "cic/texts/barhebraeus_chronicon-ecclesiasticum-vol3-lat_abbeloos-lamy1877.txt"}`.

- **B-M15 MINOR (brief length and card; the coordinator's question on what the held lines carry).** The brief carries what the stele says of Alopen himself: the books, the welcome, the decree and the title. Nothing the stele says of him is left out, except the emperor's portrait on the church wall, which is told in `uncertain` 5. P5, on 699, 713 and the restoration, is about the church and not him. Held lines that matter more for a man known through one stone are on the card only, or nowhere:
  - (a) The stone's own story: "accidentally found in 1625 by some workmen" (YULE l.2930). Williams on the authenticity quarrel: "the discussion regarding its authenticity has been rather warm between the Jesuits and their opponents, the weight of evidence, both internal and external, leaves no doubt regarding its verity" (MALECH l.14212-14217).
  - (b) Lamy, as Chabot quotes him, dates the church and its twenty-one priests "Dès 635" (Chabot l.1342-1344). Lamy's own line thus gives 635, and his editors' note gives 636.
  - (c) Wigram 1929 puts the greeting "about the year 630" (`wigram_assyrians-and-their-neighbours_1929.txt` l.4183-4190). The scan logs this as a held date conflict (scan, "Dates that conflict inside held texts").
  - (d) `otherNames` leaves out Yule's "Olopan" (YULE l.2939), and the README says the card keeps "the other spellings the sources use".
  Fixes: add to the brief, as a paragraph after P2: "Workmen dug the stone up in 1625, Henry Yule writes. Jesuits and their opponents argued warmly over whether it was genuine, S. Wells Williams says. To him the weight of evidence leaves no doubt." With B-B3 and B-M9 to B-M12, the brief is 395 words, under the 405 cap. Add (c) to `uncertain` 2: "W. A. Wigram, in 1929, says about 630." Add "Olopan (Henry Yule)" to `otherNames`. Add the Wigram 1929 file to `sources` if (c) goes in.

After the fixes (B-B3, B-M9 to B-M12, and B-M15's added paragraph): 395 words, about 2:26, FK 7.2, Flesch 64.0 (scratch copy scored). Without B-M15's paragraph the brief is about 362 words.

**Verdict: NOT CLEAR** (one blocking, shared with the README).

---

### Thomas of Marga (recorder; 354 words, about 2:11; FK 6.5, Flesch 74.9)

| # | Item | Result |
|---|---|---|
| 1 | Each sentence sourced | FAIL (B-M16, B-M17) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | FAIL (B-M17, B-M18) |
| 5 | Named witnesses | PASS |
| 6 | Partisan witness marked | PASS |
| 7 | Contested claims both sides | PASS (840 against 832-850 in the brief; the metropolitan question on the card) |
| 8 | Common names | FAIL (B-M21, card only) |
| 9 | One term for one thing | PASS |
| 10 | Story, scene, disputes in place, length | PASS |
| 11 | Readability | PASS |
| 12 | Card order, fields, caveat repeated | PASS (`uncertain` 1) |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS (recorder) |
| — | Card and records | FAIL (B-B4, B-M19, B-M20) |

**Sentences checked and found faithful.**
- P1: "Now I came to this holy monastery when I was a young man, in the two hundred and seventeenth year of the era of the dominion of the Arabs" and "by reason of the fervour which burned in me I used to make enquiries concerning them ... from the old men who were to be found here" are at BG l.11877-11884. "did not know that I should become the historian" is verbatim, with a footnote mark after "historian" (l.20218-20221). There it is the bishops of the holy man's house that he did not ask about.
- P2: Budge's note, "in 217 A. H. = 832 A. D. ... he entered the Monastery", the secretary to Abraham, "promoted to be Bishop of Marga, and afterwards Metropolitan of Beth Garmai", is at l.180-190. "before the Patriarchal throne" is verbatim (l.4609-4611).
- P3: 'Abhd-Isho', the many years of urging, the "two reasons", "severe labour" and "cessation from daily work" are at l.11739-11750. The book's title is at l.154-163. The deacon of Shalmath is at l.11842-11844, Timothy's letters at l.20158-20160, and "related to me fully" is verbatim (l.21529-21531). "not vain imaginations of my own" is verbatim, with a hyphen break (l.1065-1067).
- P4: Budge's title, "A.D. 840", is at l.1. "Thomas de Marga, qui écrit entre 832 et 850" is at Labourt l.17234-17235.
- P5: "carcerem toleravit ad triennium et sex menses; quo tempore ei adstitit ipsius frater Thomas Bagarmae metropolita omnia ei humanitatis officia praestans" is at MARI l.12742-12744. The patriarch is Theodosius, consecrated in A.H. 238 (l.12767, 12790-12791), and the passage falls in his life.
- P6: "the choice and well-filled ears of corn" is verbatim (l.980-990, with a footnote break).

**Card.** I checked these against their lines: `otherNames` (l.161-163); `knownFor`; `dates`; `keyWorks` 1 and 2 (l.141, 147, 15383-15386); `legacy.traces` 1 (Mingana l.3344-3346) and 2 (BG l.20155-20160, with Budge's note glossing Beth Sinaye as China); `legacy.remembered` 1 (l.30193-30195), 2 (ASS3-1 l.78727-78730) and 3 (ASS3-1 l.84556-84557); `uncertain` 1 (ASS3-1 l.78625-78626, "nono saeculo ineunte claruit"), 4 (ASS3-1 l.84827-84829), 5 and 6.

**Findings.**

- **B-B4 BLOCKING (card `place`; item 1; a claim credited to someone who does not make it).** "the patriarch's court, which Budge takes to be Seleucia". The records give no witness for it. Budge's note on the line where Thomas copies letters "before the Patriarchal throne" says only that Abraham sat from 837 to 850, and gives his earlier sees (BG l.4626-4630). I read every Seleucia, Ctesiphon, Mahoze and Bagdad line in BG that stands near Thomas, Abraham or the secretary. None places Abraham's court. Mari has the patriarchs of Thomas's day at Baghdad and Surra-man-ra'a (MARI l.12700-12706). Fix: "the patriarch's court, where he copied letters as a young man".

- **B-M16 MINOR (brief P2; card `dates`; item 1).** "From 837, Budge says, he was secretary". Budge: "In A. H. 222 = 837 A. D. he acted as secretary to the Patriarch Abraham" (BG l.187-188). Fixes: brief, "In 837, Budge says, he was secretary to the catholicos Abraham, the head of his church." Card, "Budge has him secretary to Abraham in 837."

- **B-M17 MINOR (brief P3; items 1 and 4; a count that is not complete, and a colon list).** "He names those who told him: an old deacon of Shalmath, the letters of the patriarch Timothy I, and Abraham himself". These are three of many. He also names Isho'-zekha with the deacon (l.11844), Narsai the Elder and an elder of Beth Hazkiel (l.4605-4609), and others. A letter is also not someone who "told him". Fix: "He names his sources. Among them are an old deacon of Shalmath, the letters of the patriarch Timothy I, and Abraham himself, who "related to me fully" one story."

- **B-M18 MINOR (brief P1; item 4, sentence length).** The opening sentence runs 29 words. Fix: "In the Arab year 217, a young man came to the monastery of Beth 'Abhe. He began asking the old monks about the holy men who had lived there."

- **B-M19 MINOR (card `legacy.traces` 3; item 1).** "W. A. Wigram notes the same silence." Wigram draws the opposite conclusion from Labourt: "Neither Theodoret nor Thomas of Marga, however, have any knowledge of Mar Augin; but his existence need not therefore be questioned" (Wigram 1910 l.11310-11312). Fix: "W. A. Wigram notes the same silence, but holds that Awgin's existence need not be questioned for it."

- **B-M20 MINOR (card `uncertain` 2 and 3; records).** (a) The "boy" in Assemani's Latin has no witness in the records. It is "Quoniam puer quum essem, ad hoc sacrum monasterium (Beth-Abense) anno regni Arabum ducentesimo decimo septimo accessi" (ASS3-1 l.78703-78706, OCR). Add it as a claim. (b) `uncertain` 3, "Budge thinks the Syriac of that line is corrupt, and reads the Arab year 217 as 832." Budge calls certain words in the line corrupt, words that "should probably be omitted" and may have given the time in Christian years. He does not call the year corrupt (BG l.11893-11899). Fix: "Budge thinks some words in that line are corrupt and should probably be omitted. He reads the Arab year 217 as 832."

- **B-M21 MINOR (card `legacy.remembered` 3; item 8).** "the chronicler Amr" is bare. The Library file is `amr-ibn-matta_...`, and Assemani's marginal source is "Amrus" (ASS3-1 l.84556). Fix: "the chronicler Amr ibn Matta".

After the fixes (B-M16 to B-M18 in the brief): 355 words, about 2:11, FK 6.1, Flesch 75.6 (scratch copy scored).

**Verdict: NOT CLEAR** (one blocking, card only).

---

### John of Nikiu (recorder; 356 words, about 2:12; FK 6.5, Flesch 73.8)

| # | Item | Result |
|---|---|---|
| 1 | Each sentence sourced | FAIL (B-B5, B-B6, B-M22) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | FAIL (B-M27) |
| 5 | Named witnesses | PASS |
| 6 | Partisan witness marked | PASS (the History's and Renaudot's tellings are set side by side) |
| 7 | Contested claims both sides | FAIL (B-B6, B-M23) |
| 8 | Common names | PASS |
| 9 | One term for one thing | PASS |
| 10 | Story, scene, disputes in place, length | PASS |
| 11 | Readability | PASS |
| 12 | Card order, fields, caveat repeated | FAIL (B-M23: the card's one-man caveat is not in the brief) |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS (recorder) |
| — | Card and records | FAIL (B-B7, B-M24, B-M25, B-M26, B-M28) |

**Sentences checked and found faithful.**
- P1: the entry into Nakius, "finding no soldiers", the sword in streets and churches, "men, women, and infants", and "and they showed mercy to none." are at CHARLES l.11346-11350. "Let us now cease, for it is impossible to recount the iniquities" is verbatim (l.11356-11357). The brief's "women and infants" drops a comma inside narrator prose, outside the quote, which is fine.
- P2: the Ethiopic of 1602 from a lost Arabic is at l.280-282. Amélineau's claim to an Arabic manuscript came to nothing (l.282-286), so "survives only" holds. Charles's Greek is at l.253-254, and "probably born about the time" is at l.177-178, with "He thinks" keeping the hedge.
- P3: "Abba John, bishop of Niciu" at John III's deathbed is at HP5 l.1229-1231. The bishops' meeting is at l.1313-1315. "Abba Simon committed to Abba John, bishop of Niciu, the management ... because he was conversant with the life of the monks, and knew their rules" is at l.1800-1806.
- P4: the virgin, the beating, the death ten days later, "transgressed the limit of what humanity required in him", "he was silent while they did so" and "strangers to your sees" are at l.1807-1849. Renaudot's "quidam Monachi ... feminam abducerent", "verberari jussit" and "quod ille impatienter tulit" are at Renaudot l.12551-12561. Renaudot supports both "some monks" and "had ... beaten".
- P5: 690 is at CHARLES l.181.
- P6: "every one said" with Heraclius and Cyrus is at l.12007-12010. "had no mercy on the Egyptians" (l.11758) and "he took none of the property of the Churches" (l.12016) are both said of 'Amr.
- P7: "wanting in eloquence beyond all authors" is verbatim, with a footnote mark (l.1486). "I have been honest" is at l.1490.

**Card.** I checked these against their lines: `otherNames` (HP5 l.1230; CHARLES l.12090-12091); `knownFor`; `keyWorks` 1 (l.253-258, 280-282, 670, 707); `legacy.traces` 1 and 2 (l.186-189); `legacy.remembered` 1 (HP5 l.1851); `uncertain` 1, 2 (l.688-690), 4 to 8 (l.12007; HP5 l.1314; CHARLES l.197-201).

**Findings.**

- **B-B5 BLOCKING (brief P3; item 1; pronoun capture).** "John's own life is told in the History of the Patriarchs of Alexandria, a later Arabic history. Its writer says he was the spiritual son of the patriarch John III." In a paragraph on John's life, the listener hears that John of Nikiu was John III's spiritual son. The History says the writer was: "And the writer of this history was with him, for he was his spiritual son" (HP5 l.1229). Here "he" is the writer, and "him" is the patriarch on his last journey to Alexandria. John of Nikiu is named only in the next sentence, among the bishops (l.1229-1231). Fix: delete that sentence, and make the next "John of Nikiu was among the bishops at the deathbed of the patriarch John III, and met with them to choose the next." (With B-M23 a sentence is added after it.)

- **B-B6 BLOCKING (brief P5; card `dates`; card `uncertain` 3; records contested claim 1; item 7; an editor's heading told as the source's).** "The History heads the life of the patriarch then chosen, Isaac, 686 to 689." The heading "ISAAC, THE FORTY-FIRST PATRIARCH. A. D. 686-689", and the running head "PT. I. CH. XVI. ISAAC, A. D. 686-689", are B. Evetts's editorial headings in his English edition (HP5 l.1278, 1239). A medieval Arabic history does not reckon in A.D. years, and the heading carries Evetts's footnote to Amélineau (l.1283). One side of the contested date is therefore an editor's, not the History's. Fixes:
  - Brief: "B. Evetts, who put the History into English, heads the life of the patriarch then chosen, Isaac, 686 to 689."
  - Card `dates`: "... and among the bishops who met to choose his successor. B. Evetts, its English translator, heads the life of the next patriarch, Isaac, 686 to 689." (B-M25 changes the first half.)
  - Card `uncertain` 3: "B. Evetts's English of the History heads Isaac's life 686 to 689".
  - Records: "B. Evetts's heading to Isaac's life in his English of the History: 686-689 (HP-PO5 l.1278)".

- **B-B7 BLOCKING (card `legacy.traces` 3; item 1; a false "only").** "Its account of the conquest is the source for Benjamin I of Alexandria's return to the city, in the thirteenth year after his flight." "The source" claims a monopoly. The History of the Patriarchs, held, tells Benjamin's return to 'Amr's safe-conduct and his welcome (HP1, `severus-al-muqaffa_history-patriarchs-coptic-church-v1_evetts1904.txt` l.44676-44680). The thirteenth year is the Chronicle's own (CHARLES l.12004-12006). Fix: "Its account of the conquest tells of Benjamin I of Alexandria's return to the city, in the thirteenth year after his flight. The History of the Patriarchs tells of his return too."

- **B-M22 MINOR (brief P1; item 1).** "Then the chronicler breaks off:" Two sentences on the next towns come between, and John goes straight on after "Let us now cease" to list "the horrors committed" (CHARLES l.11351-11360). Fix: "Soon after, the chronicler writes:".

- **B-M23 MINOR (brief P2-P3; items 7 and 12).** The brief tells the chronicler and the bishop the History deposes as one man, as settled. The card's `uncertain` 2 rightly says the History never says its John wrote a chronicle, and that Charles takes them as one. Fix: after the B-B5 sentence, add "R. H. Charles takes this bishop and the chronicler for one man." (Charles's own sketch joins them: CHARLES l.177-185.)

- **B-M24 MINOR (card `place`; item 7, a hedge dropped).** "B. Evetts places it at the modern village of Ibshadi". Evetts: Ibshadi "is probably on the site of the ancient Nakyus" (EVETTS l.5901-5902). Fix: "B. Evetts thinks the modern village of Ibshadi, east of the Rosetta branch of the Nile, is probably on its site."

- **B-M25 MINOR (card `dates`; item 1).** "places him ... at the election of Isaac". The meeting he sat in chose the deacon George. The amir then cancelled that and ordered Isaac appointed (HP5 l.1313-1350). Fix, with B-B6: "The History of the Patriarchs places him at the death of the patriarch John III and among the bishops who met to choose his successor."

- **B-M26 MINOR (records `absent_details`, "When he wrote the Chronicle").** "No held source dates it. F. Nau says the end of the seventh century." The second sentence contradicts the first, and it has no line. Nau's line is "la Chronique de Jean de Nikiou (fin du VIIe siècle)" (`theopistus_histoire-de-dioscore-journal-asiatique-1903-fra_nau1903.txt` l.13604-13605). Fix: "No held source gives a year. F. Nau puts it at the end of the seventh century (nau1903 l.13604-13605)."

- **B-M27 MINOR (brief P4; item 4).** "Then he cried out that the Lord would make them "strangers to your sees"." The pronoun switches from "them" to "your" inside one clause. Fix: "Then he cried out to them that the Lord would make them all "strangers to your sees"." Or keep the quote in direct speech: "Then he cried out that the Lord would make them, in his words, "strangers to your sees"."

- **B-M28 MINOR (card `legacy.remembered` 2; item 1).** "It survives because, as R. H. Charles reports from the manuscript, the Abyssinian general Athanasius and the wife of King Jacob had it put into Ethiopic in 1602." The manuscript records who ordered the version (CHARLES l.332-336). "Because" is the drafter's inference, and the line is a trace, not a memory. Fix: move it to `legacy.traces` as "R. H. Charles reports from the manuscript that the Abyssinian general Athanasius and the wife of King Jacob had it put into Ethiopic in 1602."

After the fixes (B-B5, B-B6, B-M22, B-M23 in the brief): 365 words, about 2:15, FK 6.1, Flesch 74.5 (scratch copy scored).

**Verdict: NOT CLEAR** (three blocking).

---

### README (the lines on these four, and its general claims)

Checked and true:
- The eight ids, and their rows in the scan. Antony of Choziba is a recorder (scan "Own work (recorder)").
- Mark's ruling of 2026-11-14 that eras 4 to 7 are built in full (Decision-Log, "Eras 4 to 7 built in full").
- Adam (Jingjing) is a separate scan row, and the briefs name him only as King-Tsing.
- The word counts: Athanasios 405, Alopen 359, the other six 346 to 356.
- The name lines for Moses (Bar-Cepha, Barcepha, Severus) and for Alopen (Olopun).
- Thomas of Kashkar (BG l.17350) and Thomas of Hedhodh (l.20126) are other men in the same book, and John III of Samannud is not John of Nikiu.
- The four tradition lines are census names, and the dates fit each man. Syriac Orthodox under Islam runs c.650-1054 and lists Moses as a voice. The Church of the East on the Silk Road runs c.635-845 and lists Alopen as a voice. The Church of the East under the Abbasids runs c.845-1220; Theodosius's imprisonment, after his consecration in A.H. 238, falls in it. Coptic Christianity under Early Islam runs 642-1013.
- "None is a live census person entry": Moses and Alopen are census voice lines, not person entries, so this holds.
- The table of files and fields matches the files.

Findings: the README's "everything known of him comes from the one stele" is part of B-B3, with its fix there. "The card keeps the other spellings the sources use" becomes true once B-M15(d) adds Olopan.

---

### Summary

- Blocking, 7:
  - B-B1, Moses brief: Basil credited with Moses's church-builders point.
  - B-B2, Moses card: the baptism line credited to the liturgy commentary.
  - B-B3, Alopen brief, card and README: "all that is known" comes from the stele, a false absence; the census cites the Tang huiyao decree.
  - B-B4, Thomas card: Budge does not place the patriarch's court at Seleucia.
  - B-B5, John brief: the History's writer, not John of Nikiu, was John III's spiritual son.
  - B-B6, John brief, card and records: Evetts's A.D. heading told as the History's.
  - B-B7, John card: the Chronicle is not "the source" for Benjamin's return.
- Minor, 28: B-M1 to B-M8 (Moses, 8), B-M9 to B-M15 (Alopen, 7), B-M16 to B-M21 (Thomas, 6), B-M22 to B-M28 (John, 7).
- Verdict for part B: **NOT CLEAR**. All four profiles have at least one blocking point. Every brief passes readability before and after the fixes. Alopen's margin is the thinnest: Flesch 63.1 before and 64.0 after.
