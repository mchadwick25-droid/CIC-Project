# R2 recheck: era 4 Who batch 5

Round 2 of at most three. It is a targeted recheck by a fresh Opus agent that had not seen the drafting, round 1 in progress or the fixes, at full effort. It covers all eight profiles, `records.json` and the README.

## Method

Reviewer: independent Opus, first sight of these files. I edited no profile file. I made no git commit and no web, paid or model call, and used local scripts only. Inputs: `CLAUDE.md` in full, the review brief, `R1_review.md` parts A and B, `R1_changes.md`, era 4 batch 3's `R2_recheck.md` for form, and the two fix commits over `Who-Profiles/era4/batch5/`: `git diff 9d78d832 304514c8` (part B) and `git diff 304514c8 560983e0` (part A, the README and all audio). The working tree matches 560983e0 for this folder.

I opened each cited line again in its vendored file under `cic/texts/` and read 15 to 60 lines around it, folding OCR noise, double spaces, hyphen breaks and Migne's two columns. Short names follow R1: THEOPH (PG 108), MANSI10, PG87.3, NPNF14, EUTYCH and PG111 (the same PG 111 file), CHARON, MEYER, PEETERS, GEORGIRENES, MACLER04, MACLER17, AB7, NIKODEMOS, HOROLOGION, BH1, BH3, ASS1, ASS3-1, ASS3-2, HM (Harris-Mingana 1920), MITCHELL (`ephraim_prose-refutations_mitchell1912-1921.txt`), MALECH, YULE, CHABOT, WIGRAM1929, BG (Book of Governors), MARI, WIGRAM1910, CHARLES, HP5 (the Evetts PO 5 file), HP1 (the Evetts PO 1 file), NAU.

Every changed string was treated as a new claim and checked against its line. Every quotation in the eight briefs was checked again verbatim by script against its file (hyphen breaks and footnote marks folded), and by eye where the script missed a line break.

## Mechanical checks (all eight)

A script confirmed that each `audio/<id>.audio.txt` equals its brief with `[calmly] ` at the start and `[warmly] ` at the start of the last paragraph, one tag of each. No tag is in a brief or card. Every card is in Mark's field order (`name` to `sources`), with no null or empty field; Sebeos's `otherNames` is now absent, as A-M21 asked. Every new `sources` file exists and holds the named work.

| Profile | Words | Time @162 | FK | Flesch | Longest brief sentence |
|---|---|---|---|---|---|
| sophronius-of-jerusalem | 356 | 2:12 | 7.82 | 67.60 | 24 |
| athanasios-the-athonite (major) | 405 | 2:30 | 7.05 | 68.98 | 24 |
| sebeos | 358 | 2:13 | 6.57 | 73.43 | 26 (P1, unchanged since R1) |
| antony-of-choziba | 347 | 2:09 | 6.14 | 75.67 | 21 |
| moses-bar-kepha | 356 | 2:12 | 6.55 | 72.14 | 25 |
| alopen (major) | 362 | 2:14 | 7.23 | 63.82 | 26 (the closing verse, quoted) |
| thomas-of-marga | 355 | 2:11 | 6.08 | 75.62 | 27 (P11, with a quote; unchanged) |
| john-of-nikiu | 356 | 2:12 | 5.95 | 75.54 | 27 (P11, two quotes; unchanged) |

All pass `grade_text` (FK 10 or below, Flesch 60 or above). The figures match `R1_changes.md` and the README. Athanasios sits on the 405-word cap. Alopen's margin is still the thinnest (63.82).

Quotations: all 23 quoted strings in the four briefs that quote (Alopen 10, John 7, Moses 1, Thomas 5) are word for word. "the Greatly-virtuous Olopun, of the kingdom of Syria" spans MALECH l.13701-13702. "wanting in eloquence beyond all authors" has a footnote mark inside it (CHARLES l.1487), which is allowed. "I have been honest" is at CHARLES l.1492. Sophronius, Athanasios, Sebeos and Antony quote nothing in the brief. Card quotations checked: Percival's two (NPNF14 l.25716-25722), "magnus Athanasius" (PEETERS l.2860), the stele verse, "a young man" (BG l.11877-11878), "the divinely pious man and spiritual philosopher" (BG l.30194), "to write a history of the Arab conquest of Egypt" (CHARLES l.190-191), "this holy bishop" (HP5 l.1878), "every one said" (CHARLES l.12008). All hold.

---

## 1. R1 findings

### Part A: Sophronius of Jerusalem, Athanasios the Athonite, Sebeos, Antony of Choziba, README

| Finding | Status | Evidence |
|---|---|---|
| A-B1 (pronoun "it" for the temple) | PARTLY | "it" is gone. But the fix puts in the opposite reading as Theophanes's own: "Sophronius looked at him and wept". It rests on the Latin translator's "Hunc" (THEOPH l.61824). Theophanes wrote in Greek, and his "Τοῦτον" (OCR "Toiroy", l.61789) is masculine and agrees with "τὸν ναὸν" (OCR "vady", l.61787), the temple, as well as with Umar. The Greek does not settle it. See R2-B1. |
| A-M1 (faith at risk) | RESOLVED | "si distuleris & postposueris fidem ejus periclitantem" (MANSI10 l.91457-91458). The fix makes an echo with the next sentence (R2-M1). |
| A-M2 (apostolic see) | RESOLVED | "at Rome" is added; the synod is the Lateran synod of 649. |
| A-M3 (quote marks on "two"; "he") | RESOLVED | No quote marks; "spoke of two in those very words" fits "duas nominatim et ipsis verbis operationes" (PG87.3 l.25686-25687). The new "he says" after "Sophronius could not" can take Sophronius (R2-M2). |
| A-M4 ("them") | RESOLVED | "nos ... domi manere cogimur; ... Saracenico metu absterriti" (PG87.3 l.30709-30714). |
| A-M5 (Eutychius in the brief, optional) | DECLINED-OK | The brief names Sergius as the owner of the Constantinople account; card `uncertain` 4 carries Eutychius (EUTYCH l.83850-83853). The Eutychius death sentence cut from P5 stays on the card's `dates`. Sound. |
| A-M6 (Mansi's editor) | RESOLVED | `dates` and `uncertain` 2 read "A note in J. D. Mansi's collection of the councils" (MANSI10 l.68215-68219). |
| A-M7 (bare names) | RESOLVED | "Theophanes, writing in the early ninth century"; "Johann Albert Fabricius, in Harles's edition of his Bibliotheca Graeca" (PG87.3 l.24198-24202); "Sergius, patriarch of Constantinople"; "Cyrus, patriarch of Alexandria" (EUTYCH l.83846). |
| A-M8 (Renaudot, Charon) | RESOLVED | Both are in `sources.about`; Charon's "paraît bien indiscutable" (CHARON l.21284-21286) is in the records. A search for the Sophist beside Sophronius in the likely files found no held source that splits the two men. |
| A-M9 (service books) | RESOLVED | The service books are gone. The new second sentence keeps only half of what Papebroch says (R2-M3). |
| A-M10 (reproach witness) | RESOLVED | "Athanasios went to Constantinople, his rule says, and blamed him to his face." The P2 cut of "the German scholar" loses nothing the card lacks. |
| A-M11 (charter copied) | RESOLVED | "καθὼς αὐταῖς λέξεσιν οὑτωσὶ περιέχει τὸ χρυσοβούλλιον" (MEYER l.5644-5645, OCR "χαφθὼς"). Brief "quotes in his rule"; card "with passages of Nikephoros's charter quoted in it". |
| A-M12 (manuscript printed) | RESOLVED | "Nach einem Msc., das Hase ans Licht gezogen ... (Leon Diak. notae S. 426)" (MEYER l.1342-1345). |
| A-M13 ("my abbot" in quote marks) | RESOLVED | The quote marks are gone. The added "at Mount Kyminas" is not in the rule (R2-M4). |
| A-M14 (knownFor unowned) | RESOLVED | Meyer is named twice; "Athanasios wrote its rule" follows. |
| A-M15 (Georgirenes) | RESOLVED | "The Monks of the place have a long Story, how this Athanasius, wanting Money to go on with the great Church ... was met with by the Blessed Virgin ... she bid him take no care for necessaries, she would provide" (GEORGIRENES l.3994-4007, OCR). The narrowing of R1's l.3966-4010, 4486-4488 to l.3966, 3993-4007 is sound: those are the lines that carry it. |
| A-M16 (records lines) | RESOLVED | Melana l.6578, John l.6646, Euthymios l.6666, "magnus Athanasius" l.2860: all checked. The drafter's move of the chrysobull line to l.5644 is right (καθὼς sits on l.5644). A different testament line in the records is still wrong (R2-M5). |
| A-B2 (Macler's hedge and anchor) | RESOLVED | The note is marked (3) on "Une frayeur inspirée par le Seigneur s'empara de l'armée des Grecs" (MACLER04 l.6483-6484) and opens "Bien qu'il ne le dise pas explicitement" (l.6509-6510). The new P7 keeps the hedge, and brief and card now agree. P7 leaves "the invasion" without a referent (R2-M7). |
| A-M17 ("who") | RESOLVED | "son ouvrage est donc de trois siècles postérieur à Sebeos" (MACLER04 l.432, 480). |
| A-M18 (beat paragraph) | RESOLVED | The sentence now sits in P5. It leaves "his name" in the next sentence pointing at Macler (R2-M6). |
| A-M19 (28 words; cuts) | RESOLVED | Split; the two cut facts are on the card (`place`, `uncertain` 3, `keyWorks`). |
| A-M20 ("one source") | RESOLVED for the count | "Nous avons appris ces faits de prisonniers [venus] d'Arabie, qui en ont été témoins oculaires" (MACLER04 l.6752-6753). "names his witnesses" is a new fault (R2-M8). |
| A-M21 (otherNames) | RESOLVED | Absent. |
| A-M22 (Vienna copy) | RESOLVED | "Le n° 52 des manuscrits de la bibliothèque des PP. Mkhitharistes de Vienne ... renferme l'histoire de Sebéos" (MACLER17 l.361-364). The wording "a second copy" is a count, and clashes with "The second" book a sentence earlier (R2-M9). |
| A-M23 (records line) | RESOLVED | l.6116-6121 open the Cross chapter; l.6147-6154 carry the weeping and the hymns. |
| A-B3 (George "only") | RESOLVED | Nikodemos's notice "τοῦ ὁσίου πατρὸς ἡμῶν ΓΕΩΡΓΙΟΥ τοῦ Χοζεβίτου ... τὸ μοναστήριον ... τοῦ Χοζεβᾶ" (NIKODEMOS l.48569-48585) is short and names no Antony. Nikodemos is in `sources.about`. |
| A-M24 (friend his own age) | RESOLVED | "comite tantum uno ex consortibus meis" (AB7 l.11936-11937); "socio meo" (l.11949). |
| A-M25 ("In the Greek") | RESOLVED | |
| A-M26 (27 words) | RESOLVED | |
| A-M27 (Miracles as settled) | RESOLVED in the brief | "ANTONIO HOZEBITA AUCTORE"; "eodem auctore Antonio" (AB7 l.38275, 38281). The card's `knownFor` still says it flat (R2-M10). |
| A-M28 (C. Houze) | RESOLVED | The second option was taken; the brief, `keyWorks` 1, `remembered` 1 and `sources` name the Bollandists, and `absent_details` logs the header. Sound. |
| A-M29 (opening lost) | RESOLVED | |
| A-M30 (Moschus trace) | RESOLVED | Removed, with the source. |
| A-M31 (restoration) | RESOLVED | The claim now marks "[post inv]" as a restoration. |
| A-M32 (README) | RESOLVED | The README names both writings. Its "known only" is a flat absence (R2-M11). |

### Part B: Moses bar Kepha, Alopen, Thomas of Marga, John of Nikiu, README

| Finding | Status | Evidence |
|---|---|---|
| B-B1 (Basil and the builders) | RESOLVED | Moses quotes Basil, Gregory of Nyssa and Severus, then "Sunt etiam qui hinc constare existiment" in his own voice (PG111 l.38243-38267). "Others, the bishop added" is right. |
| B-B2 (wrong work) | RESOLVED | The liturgy commentary is item 5 of the editors' list (BH1 l.22907); the baptism tract is its own `keyWorks` entry, as HM l.1174-1175 names it. |
| B-M1 (Beth Kiyonaye) | RESOLVED | "BETH-CENO" (PG111 l.36957); "Beth-Raman, Beth-Ceno, & Mosal" (ASS1 l.109579-109580). The records cite both at wrong lines (R2-M16). |
| B-M2 (ring of light) | RESOLVED | "non aliter atque lunae orbis lunam cingit" (PG111 l.38283-38284). |
| B-M3 (Basil) | RESOLVED | "Basilium quidem et ejus fratrem Gregorium Nyssenum" (PG111 l.38238-38241). |
| B-M4 ("as printed") | RESOLVED | |
| B-M5 (33 words; Aytoun) | RESOLVED in the brief | "as a Mr. Aytoun gives it" is true to HM l.1174-1179. The card's new "Mr. Aytoun (tr.)" claims more than HM says (R2-M15). |
| B-M6 (913/914; Masius's order) | RESOLVED | "nongentesimo decimo quarto (aut decimo tertio)" (ASS1 l.109586-109588); "his non multo posterior mihi videtur" in the preface "LECTORI ANDREAS MASIUS" (PG111 l.36996, 37011); "Valde autem hallucinatus est Masius" (l.36979); "CIRCA MEDIUM SECULUM X" (l.36948). |
| B-M7 (maphrian) | RESOLVED | "(Chr. 898) Mar Dionysium ... patriarcham ordinarunt" (BH1 l.22832-22834); "Anno insequente ... obiit Athanasius Maphrianus" (BH3 l.12596-12598). |
| B-M8 (held matter) | PARTLY | (b) is right: "He was a pupil of Moses Bar Kepha" (MALECH l.15327), the same Abd Ishu elected in 963 (l.15315) as Assemani's Ebedjesu (ASS3-1 l.35635-35644). (c) left out, as R1 allowed. The cut of the Bible sentence is sound; `knownFor` keeps it. But (a) credits the passage to C. W. Mitchell. It stands in "INTRODUCTORY ESSAY BY F. C. BURKITT" (MITCHELL l.2585-2586), in volume 2, which Burkitt completed after Mitchell's death (l.1310). See R2-B2. |
| B-B3 (one stone) | RESOLVED | Brief P3, card `uncertain` 1 and README now speak of what the held sources say; the records name the Tang huiyao as a second witness not held. |
| B-M9 (Olopun) | RESOLVED | "A. Wylie put it into English, and calls him Olopun." |
| B-M10 (Yule's hedge) | RESOLVED | "Olopan (probably a Chinese form of Rabban — Monk)" (YULE l.2939). |
| B-M11 (bare names) | RESOLVED | "Athanasius Kircher", "P. Y. Saeki", "E. C. Bridgman" (MALECH l.14227-14231). |
| B-M12 (colon; "Wylie's stele") | RESOLVED | |
| B-M13 (translation) | RESOLVED | |
| B-M14 (Abbeloos and Lamy) | RESOLVED | In `sources.about`. |
| B-M15 (the stone, Lamy, Wigram, Olopan) | RESOLVED | "accidentally found in 1625 by some workmen who were digging" (YULE l.2930); "the discussion regarding its authenticity has been rather warm between the Jesuits and their opponents, the weight of evidence ... leaves no doubt" (MALECH l.14214-14217); "Dès 635, il comptait dans la capitale une église et vingt et un prêtres" (CHABOT l.1344); "about the year 630" (WIGRAM1929 l.4188-4190). The drafter's move of the 699/713 paragraph to `legacy.traces` 2 is sound: it is about the church, and the card keeps it (MALECH l.13745-13757). The records put Wigram's 630 on the 636 side (R2-M17). |
| B-B4 (Seleucia) | RESOLVED | "when in the days of my youth I was copying letters before the Patriarchal throne" (BG l.4608-4610). |
| B-M16 (from 837) | RESOLVED | "In A. H. 222 == 837 A. D. he acted as secretary" (BG l.187-188). |
| B-M17 (a count; colon) | RESOLVED | |
| B-M18 (29 words) | RESOLVED | |
| B-M19 (Wigram) | RESOLVED | "but his existence need not therefore be questioned" (WIGRAM1910 l.11310-11312). |
| B-M20 (puer; Budge's corrupt words) | RESOLVED | "Quoniam puer quum essem" (ASS3-1 l.78703); "The words ... are corrupt, and should probably be omitted" (BG l.11893-11894). |
| B-M21 (Amr) | RESOLVED | |
| B-B5 (spiritual son) | RESOLVED | "And the writer of this history was with him, for he was his spiritual son" (HP5 l.1229) is gone. The new paragraph opener still presupposes the identity (R2-M19). |
| B-B6 (Evetts's heading) | RESOLVED | "ISAAC, THE FORTY-FIRST PATRIARCH. A. D. 686-689", with Evetts's footnote to Amélineau (HP5 l.1278, 1283). Brief, card `dates`, `uncertain` 3 and both records places now give it to Evetts. |
| B-B7 ("the source") | RESOLVED | "Amr gave orders that Benjamin should be brought before him with honour" (HP1 l.44676-44679); "returned to the city of Alexandria in the thirteenth year after his flight" (CHARLES l.12005-12007). The HP1 volume is not in `sources` (R2-M20). |
| B-M22 (breaks off) | RESOLVED | Two sentences on other towns stand between (CHARLES l.11351-11357). |
| B-M23 (one man as settled) | RESOLVED in part | The Charles sentence is added (CHARLES l.177-185), but after a sentence that already calls the History's John "John's own life" (R2-M19). |
| B-M24 (Ibshadi hedge) | RESOLVED | |
| B-M25 (election of Isaac) | RESOLVED | "they agreed that they should promote the deacon" (HP5 l.1313-1318). |
| B-M26 (Nau) | RESOLVED | "la Chronique de Jean de Nikiou (fin du VIIe siècle)" (NAU l.13604-13605). |
| B-M27 ("your sees") | RESOLVED | "the Lord ... shall make you all, O ye bishops, strangers to your sees" (HP5 l.1846, 1873). The second option and the cut of the Renaudot sentence are sound; card `uncertain` 5 keeps Renaudot. |
| B-M28 (because) | RESOLVED | "at the order of the Abyssinian general Athanasius and of Mariara Sena ..., the wife of Jacob" (CHARLES l.332-337). |

---

## 2. New findings

### Blocking

- **R2-B1 BLOCKING (Sophronius brief P9 and audio; records claim "Theophanes: ..."; items 1 and 7; a reading the source does not settle, told as the source's, made by the A-B1 fix).** The brief reads: "When Umar asked to be shown the temple Solomon built, Theophanes says, Sophronius looked at him and wept. This is truly the abomination of desolation, he said, standing in the holy place." The records add: "\"Hunc\" (masculine) is Umar, so the words are said of the caliph in the holy place".
  - Theophanes wrote in Greek. His Greek is "τὸν ναὸν ἐζήτησε τὸν Ἰουδαίων, ὃν ᾠκοδόμησε Σολομών ... Τοῦτον δὲ ἰδὼν Σωφρόνιος ἔφη· Τοῦτό ἐστιν ἀληθῶς τὸ βδέλυγμα τῆς ἐρημώσεως" (THEOPH l.61787-61790, OCR "Toy vady iFhrnaev tov 'Toubaluy ... Toiroy d wy Lwpdvs ... Tovrd &orw"). "Τοῦτον" is masculine, and so is "ναός", the nearest noun before it. So the Greek can mean that Sophronius saw the temple, or that he saw Umar. The Latin printed beside it chooses Umar with "Hunc" (l.61824), because "templum" is neuter in Latin. That is the translator's choice, not Theophanes's. The earlier draft told the temple as settled, and the fix tells Umar as settled.
  - The Greek and the Latin agree that he spoke the words, and that he wept at the same time ("simul", l.61827; "δάκρυσι", l.61792).
  - Fix, brief P9 and audio: "Sophronius looked at him and wept." -> "Sophronius wept." (The paragraph then reads: "When Umar asked to be shown the temple Solomon built, Theophanes says, Sophronius wept. This is truly the abomination of desolation, he said, standing in the holy place." "He said" can only be Sophronius. Minus 4 words.)
  - Fix, records: replace "; \"Hunc\" (masculine) is Umar, so the words are said of the caliph in the holy place" with "; the Greek \"Τοῦτον\" (l.61789, OCR \"Toiroy\") can take the temple, \"ναόν\" (l.61787), or Umar; the Latin \"Hunc\" (l.61824) takes Umar. The brief leaves it open". Add l.61787-61792 to the witness.
  - Recommended, card `uncertain` 1, after its first sentence: "His Greek can be read as saying it of the temple or of Umar; the Latin printed with it takes Umar." (19 words.)

- **R2-B2 BLOCKING (Moses card `uncertain` 1, `sources.ownWords` 3; records claim "Mitchell: ..." and contested claim "year of death", 903 side; item 1; a claim credited to a man who does not make it, made by the B-M8 (a) fix).** The card says "C. W. Mitchell gives 903" and gives the passage as "Moses bar Kepha; C. W. Mitchell (tr.)". The passage at MITCHELL l.2652-2656 ("I will begin by quoting what Moses bar Kepha says about him"; "Moses bar Kepha died 903 A.D.") stands in the "INTRODUCTORY ESSAY BY F. C. BURKITT" (l.2585-2586), which Burkitt signs (l.2777). Burkitt explains that he wrote the essay "wholly new" because Mitchell left only a rough draft (l.1310). The file header gives Burkitt the volume 2 introduction (l.6-7). Burkitt's footnote 9 sends the reader to F. Nau's text and translation (l.3001), so the English is Burkitt's.
  - Fix, card `uncertain` 1: "C. W. Mitchell gives 903." -> "F. C. Burkitt, introducing the second volume of C. W. Mitchell's edition of Ephrem, gives 903." (16 words.)
  - Fix, card `sources.ownWords` 3: title "S. Ephraim's Prose Refutations of Mani, Marcion and Bardaisan, volume 2: F. C. Burkitt's introductory essay, quoting Moses bar Kepha on Bardaisan"; author "Moses bar Kepha; F. C. Burkitt (English)". Date (1921), language and file stay.
  - Fix, records: the claim "Mitchell: ..." -> "F. C. Burkitt's introductory essay to volume 2: ...", witness "MITCHELL l.2585-2586, 2652-2656". In the contested claim's 903 side, "C. W. Mitchell (MITCHELL l.2656)" -> "F. C. Burkitt (MITCHELL l.2585-2586, 2656)".

### Minor

- **R2-M1 MINOR (Sophronius brief P1 and audio; item 4, an echo that blurs who holds back; made by the A-M1 fix).** "You will answer to God ... if you hold back while his faith is in danger. He would go himself, he said, but the Saracen invasion held him back." Two "hold back"s in a row, with different subjects. The Latin of the second is "incursionem Sarracenorum praepedior", "I am hindered" (MANSI10 l.91459-91460). Fix: "but the Saracen invasion held him back." -> "but the Saracen invasion hindered him."

- **R2-M2 MINOR (Sophronius brief P5 and audio; item 4, pronoun capture; made by the A-M3 fix).** "Sophronius could not, he says, bring texts of the Fathers ..." Set right after "Sophronius", "he says" can be heard as Sophronius speaking of himself. It is Sergius (PG87.3 l.25681-25688). Fix: "Sophronius could not, he says, bring texts of the Fathers that spoke of two in those very words. It was agreed, Sergius says, that Sophronius would speak no more of one or two." -> "Sergius says Sophronius could not bring texts of the Fathers that spoke of two in those very words. In the end, he writes, it was agreed that Sophronius would speak no more of one or two." ("Et ad ultimum stetit ac placuit, quatenus praedictus Sophronius ... nullum sermonem de caetero, de una sive duabus operationibus movere debeat", l.25704-25707. 18 and 18 words.)

- **R2-M3 MINOR (Sophronius card `uncertain` 7; item 7, one side dropped; made by the A-M9 fix).** "Papebroch says nothing in it settles whether it is his." Papebroch goes on: "multum alioqui diversus est stylus ab eo, quo SS. Cyri et Joannis laudationem atque miracula descripta" (PG87.3 l.25420-25424). The half that leans against Sophronius is gone. Fix: "Papebroch says nothing in it settles whether it is his." -> "Papebroch says nothing in it settles whether it is his, though its style is very different from that of the Miracles." (21 words.)

- **R2-M4 MINOR (Athanasios card `uncertain` 6; item 1, a fact moved to the wrong witness; made by the A-M13 fix).** "His own rule calls Michael, uncle of Nikephoros, his abbot at Mount Kyminas." The rule has "ἐν τῇ τοῦ μακαρίου θείου αὐτοῦ λαύρᾳ Μιχαὴλ ... τοῦ ἐμοῦ καθηγουμένου" (MEYER l.5381-5382) and names no mountain. Kyminas appears in the volume only in Meyer's introduction, from the Life ("Hegumen vom Berge Kyminas", l.1259-1260, 1265; "Alles nach dem Bios", l.1277). Fix: "His own rule calls Michael, uncle of Nikephoros, his abbot at Mount Kyminas. The family name Maleinos comes from Meyer, who draws on Michael's own Life." -> "His own rule calls Michael, uncle of Nikephoros, his abbot. Mount Kyminas and the family name Maleinos come from Meyer, who draws on the Life of Athanasios and on Michael's own Life." (Maleinos: l.1279-1281.)

- **R2-M5 MINOR (Athanasios records, claim "Testament: \"Μετὰ λύπης ...\""; item 9, wrong line).** The witness reads "MEYER l.6585-6587". Those lines are about the keeping of the testament by the monk Michael. "Μετὰ λύπης ὑπερβαλλούσης διήνυσα πᾶσας τὰς ημέρας ... εἰς τὸ προΐστασθαι ἑτέρων" is at l.6592-6594. Fix: "MEYER l.6592-6594".

- **R2-M6 MINOR (Sebeos brief P5 and audio; item 4, pronoun capture; made by the A-M18 move).** "Later writers, Macler says, drew on the book as a source. The printed editions place three books under his name." The nearest man is now Macler. Fix: "under his name" -> "under Sebeos's name".

- **R2-M7 MINOR (Sebeos brief P7 and audio; items 4 and 10, a term with no referent; made by the A-B2 fix).** "After the Greeks crossed the Jordan, Sebeos writes, a terror sent by the Lord seized their army. Macler takes him to see the invasion as God's punishment of the Greeks ..." Nothing in the paragraph says whom the Greeks were fighting, so "the invasion" has no referent. They crossed the Jordan into Arabia and went against the Ishmaelites' camp (MACLER04 l.6472-6484). Macler's note is on "l'invasion des Arabes" (l.6510-6515). Fix: "After the Greeks crossed the Jordan, Sebeos writes," -> "After the Greeks crossed the Jordan to fight the Arabs, Sebeos writes,"; and "to see the invasion" -> "to see the Arab invasion". (21 and 21 words.)

- **R2-M8 MINOR (Sebeos brief P9 and audio; item 4; made by the A-M20 fix).** "For the first Arab wars, Sebeos names his witnesses." He names none. He says "prisoners [venus] d'Arabie, qui en ont été témoins oculaires" (MACLER04 l.6752-6753). Fix: "Sebeos names his witnesses." -> "Sebeos says who his witnesses were."

- **R2-M9 MINOR (Sebeos card `uncertain` 1; items 3 and 4, a count, and "second" in two senses; made by the A-M22 fix).** "The second copies Moses of Khoren and Stephen of Taron. In 1917 Macler listed a second copy, in the Mekhitarist library at Vienna, ..." Macler does not call it a second copy. He gives it as "Le n° 52 des manuscrits", and his catalogue reference carries two numbers, "sous les n° 52? et 86" (MACLER17 l.361-367). Fix: "In 1917 Macler listed a second copy, in the Mekhitarist library at Vienna, with extracts of Moses of Khoren and Stephen of Taron." -> "In 1917 Macler listed another copy, manuscript 52 of the Mekhitarist library at Vienna, with extracts of Moses of Khoren and Stephen of Taron." The `keyWorks` sentence on the two editions and one Etchmiadzin manuscript stays true (MACLER04 l.357-359).

- **R2-M10 MINOR (Antony card `knownFor`; items 1 and 12; the A-M27 fault left on the card).** "He also wrote down miracles of the Mother of God at Choziba." The card's own `uncertain` 3 and `keyWorks` 2 rest it on the Bollandist heading (AB7 l.38275, 38281), and the brief now does too. Fix: -> "The Bollandist heading also gives him the Miracles of the Mother of God at Choziba."

- **R2-M11 MINOR (Antony card `uncertain` 1; README, the majors paragraph; item 1, a flat absence of the kind B-B3 fixed for Alopen).** Card: "All that is known of him comes from his own two works." README: "known only from his own writings". These claim more than a search of the Library can show, and "his own two works" contradicts `uncertain` 3. The held-source form is the one the batch uses for Alopen. Fix, card: "All that is known of him comes from his own two works." -> "Everything the held sources say of him comes from the Life and from the Miracles printed under his name." README: "known only from his own writings," -> "known in the held sources only from his own writings,". (The Choziba search in R1 stands: no other held source names him; Nikodemos's notice of George does not, NIKODEMOS l.48569-48610.)

- **R2-M12 MINOR (Antony brief P11 and audio; item 4, a reference with no antecedent; made by the A-M27 fix).** "The same volume prints, under his name, miracles ..." No volume has been named; P3 says only "The Bollandists edited it in 1888". Fix: "The same volume prints," -> "The Bollandists' volume also prints,".

- **R2-M13 MINOR (Moses brief P5 and audio; item 4, pronoun capture; not changed since R1, found on the whole read).** "... from an anonymous Syriac life that Joseph Assemani reports. He lived about ninety years, it says." The nearest man is Assemani. Fix: "He lived about ninety years, it says." -> "Moses lived about ninety years, it says." (BH1 l.22849-22850.)

- **R2-M14 MINOR (Moses brief P13 and audio; item 4, pronoun capture; found on the whole read).** P11 is about Bar Hebraeus's book of church law. P13 then says "a line from his tract on baptism", and the nearest man is Bar Hebraeus. Fix: "from his tract on baptism" -> "from Moses's tract on baptism" (HM l.1174-1175).

- **R2-M15 MINOR (Moses card `sources.ownWords` 2; item 1; made by the B-M5 fix).** "Mr. Aytoun (tr.)". HM says only that "Mr. Aytoun reminds us that Ephrem's language has affected Moses Bar Kepha in his tract on the Mysteries of Baptism", then gives the line (HM l.1174-1179). It does not say the English is his own. The brief's "as a Mr. Aytoun gives it" is right. Fix: author -> "Moses bar Kepha, in English as Mr. Aytoun gives it; J. Rendel Harris and Alphonse Mingana (ed.)".

- **R2-M16 MINOR (Moses records, editors' note claim on the three sees; item 9, wrong lines; from the B-M1 fix).** "Migne's heading and Assemani have \"Beth-Ceno\" (PG111 l.36955; ASSEMANI1 l.109574-109575)". The heading is at PG111 l.36957, and Assemani's "Beth-Raman, Beth-Ceno, & Mosal" at ASS1 l.109579-109580. Fix those two numbers.

- **R2-M17 MINOR (Alopen records, contested claim "The year he came"; items 7 and 9, a witness on the wrong side; made by the B-M15 fix).** The 636 side ends "W. A. Wigram 1929: about 630 (WIGRAM1929 l.4183-4190)". Wigram gives neither 635 nor 636 (l.4188-4190). Fix: take it off the 636 side and add a third side: "About 630: W. A. Wigram, 1929 (WIGRAM1929 l.4184-4190)". The card's `uncertain` 2 already tells it as a third date.

- **R2-M18 MINOR (Thomas brief P9 and audio; item 4, pronoun capture; found on the whole read).** "The caliph al-Mutawakkil held the patriarch in prison for three years and six months. All that time, Mari says, his brother Thomas ..." The caliph is the subject of the sentence before, so "his" can take him. Mari's "ipsius frater Thomas" is the patriarch's brother (MARI l.12742-12744). Fix: "his brother Thomas" -> "the patriarch's brother Thomas".

- **R2-M19 MINOR (John brief P5 and audio; items 7 and 4; the B-M23 hedge sits after a sentence that already settles it, and a pronoun follows Charles).** "John's own life is told in the History of the Patriarchs of Alexandria ... R. H. Charles takes this bishop and the chronicler for one man. The patriarch Simon later gave him charge ..." The opener tells the identity as fact before the hedge. The "him" after the Charles sentence can take Charles. Fix: "John's own life is told in the History of the Patriarchs of Alexandria, a later Arabic history. John of Nikiu was among the bishops at the deathbed of the patriarch John III, and met with them to choose the next. R. H. Charles takes this bishop and the chronicler for one man." -> "A John, bishop of Nikiu, appears in the History of the Patriarchs of Alexandria, a later Arabic history. R. H. Charles takes him for the chronicler. This John was among the bishops at the deathbed of the patriarch John III, and met with them to choose the next." (17, 8 and 22 words; HP5 l.1230-1233, 1313-1318; CHARLES l.177-185. The next sentence's "him" is then this John.)

- **R2-M20 MINOR (John card `sources`; item 8; made by the B-B7 fix).** `legacy.traces` 3 now cites the History of the Patriarchs for Benjamin's return, from HP1 l.44676-44680. That is the earlier Evetts volume, Peter I to Benjamin I, and `sources` holds only the PO 5 volume (Agathon to Michael I). Fix: add to `sources.about`: {"title": "History of the Patriarchs of the Coptic Church of Alexandria, Peter I to Benjamin I, in Patrologia Orientalis 1 (tr. B. Evetts)", "author": "Attributed to Severus ibn al-Muqaffa", "date": "1907", "language": "English translation", "file": "cic/texts/severus-al-muqaffa_history-patriarchs-coptic-church-v1_evetts1904.txt"} (the file's content note puts the Benjamin chapters in the 1907 fascicule).

Brief fixes scored on scratch copies (`/tmp/claude-0/-home-user-CIC-Project/e2402255-0732-5843-bbde-cb8d08b63388/scratchpad/r2/fix/`):

| Profile | Fixes | Words | Time | FK | Flesch | Longest |
|---|---|---|---|---|---|---|
| sophronius-of-jerusalem | R2-B1, R2-M1, R2-M2 | 354 | 2:11 | 7.88 | 66.99 | 24 |
| sebeos | R2-M6, R2-M7, R2-M8 | 365 | 2:15 | 6.66 | 73.34 | 26 |
| antony-of-choziba | R2-M12 | 348 | 2:09 | 6.25 | 74.99 | 21 |
| moses-bar-kepha | R2-M13, R2-M14 | 356 | 2:12 | 6.62 | 71.66 | 25 |
| thomas-of-marga | R2-M18 | 356 | 2:12 | 6.12 | 75.44 | 27 |
| john-of-nikiu | R2-M19 | 352 | 2:10 | 5.98 | 75.06 | 27 |

Sebeos at 365 words is the longest non-major in this batch. If a cut is wanted, "Later writers, Macler says, drew on the book as a source." can go from P5 (11 words; the card's `legacy.traces` 1 keeps it, from MACLER04 l.264-265), and R2-M6 then falls away, since "his name" follows the Stephen sentence again. Every brief fix has to be carried into the audio file, and README word counts updated.

---

## 3. Each brief read whole

I read each brief once more as a listener, start to end.

- **Sophronius.** It still opens on Calvary and keeps the man apart from Maximus. The fixes left an echo (R2-M1), a "he says" that can take the wrong man (R2-M2), and the Umar reading (R2-B1). Apart from these, the sentences are plain and short.
- **Athanasios.** It reads well at the cap. The pronouns hold through P7 ("He asked only", "He was murdered" are the emperor) and P9 ("his rule" is Athanasios). No new fault in the brief.
- **Sebeos.** The new P7 is a good scene, but it lacks its enemy (R2-M7), and the move in P5 left "his" on Macler (R2-M6). "names his witnesses" overstates (R2-M8).
- **Antony.** It reads as his own story. One loose "same volume" (R2-M12).
- **Moses.** The paradise opening is clear and the Basil fix holds. Two pronouns can take the wrong man (R2-M13, R2-M14); neither is new, but both are the listed failure.
- **Alopen.** The new P3 on the stone is a good addition and reads cleanly. No fault in the brief.
- **Thomas.** It reads as a story that opens on a scene. One pronoun (R2-M18).
- **John.** The opening and the deposition story are strong. P5 puts the hedge after the claim (R2-M19).

No brief has hedging filler, colon-reveals outside quotations, a rhetorical question, an aphorism or a beat line. Quotation marks are only on held English.

## 4. Not findings

- Georgirenes's "The Monks of the place" are the Lavra's monks; the card's "the monks of Athos" is true of them. "wrote in 1678" gives the year his English was printed (licensed 1677, GEORGIRENES l.3), which the source entry also gives.
- The six sentences of 26 to 27 words (Sebeos P1, Alopen's closing verse, Thomas P11, John P1 and P11) are unchanged since R1, carry quotations or a close paraphrase, and read in one pass.
- "Workmen dug the stone up in 1625" is fair for "accidentally found ... by some workmen who were digging" (YULE l.2930).
- Lamy's "Dès 635" (CHABOT l.1344) as "puts the church ... in 635" is a fair short form.
- "Some monks carried a virgin off" now rests on the History's "the monk who had committed the sin" (HP5 l.1835) with Renaudot's "quidam Monachi" on the card. It holds.
- "Cyrille Charon calls it hardly open to doubt" fits "paraît bien indiscutable".
- Williams's mention of "the signatures of Olopun" in Syriac (MALECH l.14218-14219) does not touch any card sentence.
- The README's colon before "everything the held sources say" is in a working file, not participant text.
- The Alopen and Thomas cards' `briefLength` and the undotted ends of `dates` fields follow the approved batch 2 and 3 cards.

---

## 5. Verdicts

| Profile | R1 findings | New blocking | New minor | Verdict |
|---|---|---|---|---|
| Sophronius of Jerusalem | 8 of 10 resolved; A-M5 declined-OK; A-B1 partly | 1 (R2-B1) | 3 (R2-M1 to R2-M3) | NOT CLEAR |
| Athanasios the Athonite | 7 of 7 resolved (A-M10 to A-M16) | 0 | 2 (R2-M4, R2-M5; card and records only) | NOT CLEAR |
| Sebeos | 8 of 8 resolved (A-B2, A-M17 to A-M23) | 0 | 4 (R2-M6 to R2-M9) | NOT CLEAR |
| Antony of Choziba | 10 of 10 resolved (A-B3, A-M24 to A-M32; A-M27 in the brief) | 0 | 3 (R2-M10 to R2-M12; R2-M11 also touches the README) | NOT CLEAR |
| Moses bar Kepha | 9 of 10 resolved; B-M8 partly | 1 (R2-B2) | 4 (R2-M13 to R2-M16) | NOT CLEAR |
| Alopen | 8 of 8 resolved (B-B3, B-M9 to B-M15) | 0 | 1 (R2-M17; records only) | NOT CLEAR |
| Thomas of Marga | 7 of 7 resolved (B-B4, B-M16 to B-M21) | 0 | 1 (R2-M18) | NOT CLEAR |
| John of Nikiu | 10 of 10 resolved (B-B5 to B-B7, B-M22 to B-M28; B-M23 in part) | 0 | 2 (R2-M19, R2-M20) | NOT CLEAR |
| README.md | A-M32 and B-B3's README part resolved | 0 | 1 (R2-M11, shared) | CLEAR once R2-M11 is applied |

**Totals.** R1 had 70 findings (10 blocking, 60 minor): 67 resolved (A-M27 in the brief only, B-M23 in part), 1 declined-OK (A-M5) and 2 partly (A-B1, B-M8). The drafter's stated deviations (A-M5, A-M15, A-M16, A-M28, B-M8's cut, B-M15, B-M27, and the length cuts in Sophronius, Sebeos, Moses and John) are sound, except that B-M8 (a) carried R1's own wrong attribution. Round 2 found 2 new blocking findings (R2-B1, R2-B2) and 20 new minor ones (R2-M1 to R2-M20). Both blocking points came from fix wordings that R1 supplied and that were taken as worded. Every quotation in the eight briefs still matches its vendored file. All eight briefs pass `grade_text` before and after the fixes, and every audio file equals its brief plus tags.

Round 2 is the second of the three review rounds the cap allows on each profile. Not approved to proceed until R2-B1 and R2-B2 are fixed and independently rechecked. The fixes are small and named string by string; a targeted round 3 on the changed strings should be enough.
