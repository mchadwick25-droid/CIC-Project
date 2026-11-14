# R1 review: era 3 batch 6

Round 1 ran in three parts, each by a fresh Opus agent that had not seen the drafting (review) or by the part's drafter (changes). The parts follow, unchanged.

## R1 review, part A: Columbanus, Isidore of Seville, John of Biclaro (era 3 Who batch 6)

Reviewer: independent Opus, first sight of these drafts. I did not edit any profile file, made no git, web or paid calls, and used local scripts only.

### Method

Bar: `Who_Profile_Pattern.md`, review checklist 1 to 14 and the standards it points to; `CLAUDE.md`, "Trust and source fidelity" and "Accessible and rigorous"; `Decision-Log.md`, the era 3 Who scan entry (2026-11-11) and every "Who profiles" entry from 2026-11-12 to 2026-11-14 (majors capped at 2:30, about 405 words, a cap and not a target; recorders at standard length, at most about 325 words). Columbanus and Isidore of Seville are major; John of Biclaro is a recorder at standard length. I read batch 5's R1 to R4 and batch 4's R1 for the bar and the recurring faults. Files read: for each id the `.brief.txt`, `.card.json`, `audio/<id>.audio.txt` and its `records.json` entry, and the batch `README.md` sentences that name these three (l.3, 5, 7). Brief line numbers below are paragraph lines, with blank lines counted (paragraphs sit on l.1, 3, 5 and so on). Other line numbers point to files under `cic/texts/`.

I opened every quotation in its vendored file at the cited line, folding whitespace, hyphen breaks and OCR noise, and read each hit in context to see who speaks there: the ancient writer, a document he copies, a translator, an editor's note, a margin or a running head. I checked each factual sentence of each brief against its passage. The OCR Latin files (Migne's PL 72, 80, 83, 96 and 103, Mommsen's Chronica minora II, the Madrid 1808 Collectio canonum, Mansi 10, Krusch's Fredegar, Barralis 1613, Wasserschleben 1851) were read by line. Before accepting any absence or "only" I searched all of `cic/texts/` for each person and each disputed point under the spellings the sources use (Columbanus, Columban, Columba, Kolumban; Isidorus, Isidor; Iohannes or Joannes Biclarensis, Gerundensis; Redemptus, Redemtus; Hispalense II; Maccurritae, Makoritae, Makuria). That search found three held witnesses the drafts do not use: Antoine Pagi's note on the year of the Second Council of Seville, printed in Mansi 10; Bernhard Poschmann's retelling of Redemptus's account of Isidore's death, with its Latin (1928); and a statement in the preface to Migne's Breviarium Gothicum that Isidore presided at Toledo IV. Readability came from `engine.m1.gates.grade_text`, run from the repo root. All suggested brief fixes for a profile were applied together to a scratch copy and re-scored; the post-fix word count and scores are given with each profile. The scratch copies are in `/tmp/claude-0/-home-user-CIC-Project/5632ba95-e0b1-504b-a130-94b73aea15af/scratchpad/fixA/`.

#### Applies to all three

- **Audio = brief.** Each audio script equals its brief once `[calmly] ` and `[warmly] ` are removed (checked by script). Each opens with `[calmly]` and has one `[warmly]`, at the start of the closing paragraph. No tag appears in a brief or card. Every brief fix below must be carried into the audio script.
- **Readability.** Columbanus 400 words, FK 7.4, Flesch 67.7. Isidore 393 words, FK 8.0, Flesch 62.7. John of Biclaro 321 words, FK 7.6, Flesch 65.4. All pass. No narrator sentence runs past 24 words.
- **Length.** Columbanus 400 (2:28) and Isidore 393 (2:26), under the major cap. John 321 (1:59), within the recorder length. The `briefLength` fields match.
- **Card order.** All three follow Mark's order. Missing fields are absent, `keyWorks` never passes three, and each `uncertain` list opens with the brief's caveat.
- **Who test (item 14).** Columbanus is a founder with his own rule, penitential and letters; Isidore has a large body of work; John is a recorder. The drafts carry no list lines; those belong to the map build and were not checked.
- **README.** The sentences on these three (l.3, 5, 7) are accurate. Their years are given as the scan's, and the recorder ruling for John matches the Decision-Log.
- **Narrator renderings in quotation marks (items 2, 4; a recurring point).** Several quoted lines are the narrator's English from Latin, with no translator held, set in quotation marks beside lines that are a named translator's English. A listener cannot tell which is which. Batch 4 and 5 passed such lines only where the brief said so ("Their Latin is told here in modern words"; "in plain words"). The Pattern allows an Opus-authored rendering as the quote, but the rendering must keep every clause (`CLAUDE.md`, the rendering exception). Per-profile findings: A-B1 (Columbanus), A-M7 (Isidore), A-M14 (John).

#### Points the coordinator asked me to look at

- **Columbanus's age at leaving Ireland.** No finding. The brief gives no age and no year for his leaving ("After many years he longed to live among strangers", l.5), so it tells nothing as settled. The Pattern puts a dispute where it arises, and it does not arise here. The card (`uncertain` 2) gives both sides by name, and the records carry a `contested_claim`. A note for the records: the Latin Life in Barralis also reads the twentieth year, "vigesimum aetatis annum agens" (barralis l.36689), so Jonas's twentieth stands in two held texts.
- **The Barralis 1613 Latin Life.** No finding on substance. Only the card's `uncertain` 1 rests on it, for Jonas's preface, which Munro omits (munro1895 l.96-98). The words it relies on are legible in the OCR: "quamplurimi penes nos superstites sint, qui nobis non audita sed visa narrent" and "per venerabiles viros Attalam [et] Eustasium didicimus, quorum primus Bobiensis, secundus Luxoviensis coenobii … successores fuerunt" (l.36426-36429; OCR "fuperftites fim.qui nebis", "Attalam (^Eutiachium", "Luxouienfis"). "Eustasium" is a reading of the garbled "Eutiachium", but "secundus Luxoviensis" fixes it. The card paraphrases and quotes nothing from this file, which keeps to the file header's "quote only after checking the passage against the scanned page". The source entry on the card has a process word and a witness swap: A-M6.
- **"His Penitential", told outright (brief l.7).** PASS. The line paraphrases the opening of the penitential proper, "Diversitas culparum diversitatem facit poenitentiarum: nam et corporum medici …" (wasserschleben1851 l.22218-22221; PL 80 l.17714-17717). Wasserschleben gives that text to Columbanus himself: "Die eigentliche Bussordnung beginnt mit 'Diversitas culparum' … In der Einleitung sagt Kolumban u. A. …" (l.3617-3622). His doubt reaches only the twelve-chapter fragment that comes before it in Fleming's codex: "Jener hat vielleicht ebenfalls Kolumban zum Verfasser" (l.3611-3612). Gallandi also gives the book to "ejusdem sancti abbatis" (PL 80 l.16265-16267). No held source doubts that the passage is his.
- **Seville II "in 619".** BLOCKING: A-B3. The acts give only the Spanish era 657 and Sisebut's ninth year. The 619 is Ernest Brehaut's year (after Gams), and Pagi's note in Mansi argues for 618.
- **The two sides on the addressee of the Etymologies covering letter.** The card's two sides are correctly reported (lindsay1911 l.894-919; PL 80 l.52675-52682). One held witness on the Braulio side is missing: A-M9.
- **Isidore's leading role at Toledo IV.** PASS. The brief claims only what the acts show, the first signature (Hispana l.40882-40884), and the card gives Brehaut's "probably" presided. Not a finding, only a note: the preface to Migne's Breviarium Gothicum states it flat, "concil. iv Tolet., praeside sancto Isidoro" (`mozarabic-liturgy_breviarium-gothicum-pl86-lat_migne1862.txt` l.474), and could be added to the presiding side if wanted.
- **Consistency with batch 5's `leander-of-seville` and `reccared`.** Isidore agrees on every shared point: Leander's death year is disputed, Isidore was the younger brother left a child when their parents died (the same Latin, PL 72 l.66698-66702), and Leander was bishop before him. John agrees on Toledo III (Leander and Eutropius ran its business), on his exile, and on John as a Catholic-side witness. One name form differs: A-M12 (Goiswinth against batch 5's Gosuintha). Batch 5's Leander card gives 633 "by Theodor Mommsen's year" and Isidore's brief gives it bare. That is consistent enough, since for Toledo IV the era 671 and Sisenand's third year agree, and Mommsen, Brehaut and the PL 96 note all give 633 (mommsen1894 l.21966-21967; brehaut1912 l.702-703).

---

### Columbanus (major)

| # | Item | Result |
|---|---|---|
| 1 | Each sentence sourced, source establishes it | FAIL (A-M1) |
| 2 | Quotes verbatim | FAIL (A-B1) |
| 3 | No invention | PASS |
| 4 | Reading aids, no AI tells | FAIL (A-M3, A-M4) |
| 5 | Named witnesses, no role in place of one | PASS |
| 6 | Partisan witness named and marked | PASS (Jonas's Life marked as a saint's Life that takes his side) |
| 7 | Contested claims both sides | PASS |
| 8 | Common names, first mention | FAIL (A-M5) |
| 9 | One term for one thing | PASS |
| 10 | Story, scene opening, disputes in place, length | PASS |
| 11 | Readability | PASS (FK 7.4, Flesch 67.7) |
| 12 | Card order, missing fields absent, caveat repeated | FAIL (A-M2, A-M6) |
| 13 | Audio tags | PASS |
| 14 | List line, Who test | PASS |

**Sentences checked and found faithful.** Brief l.1: Letter IV, "narrans mihi navem parari qua invitus vehar in meam regionem … Si in mare projiciar more Jonae … orate ut vice ceti sit quidam felici revocans remigio tutus celator, qui Jonam vestrum terrae reddat optatae" (PL 80 l.21305-21326; but see A-M1). L.3: Jonas's informants Theudegisil, Chamnoald and Eustasius (munro1895 l.708-709, 864-866, 1530-1531); Munro, "the miracles are numerous" (l.82). L.5: Lagener-land, glossed Leinster (l.220-221, 235); Bangor under "the holy Congall" (l.244-246); "go into strange lands" and twelve companions (l.255-256, 291). L.7: Anegray, Luxeuil and Fontaines and "the rule which they were to follow" (l.362-380, 520-541); Rule ch. III, "quotidie jejunandum est, sicut quotidie orandum est, quotidie laborandum, quotidieque est legendum" (PL 80 l.16615-16617). L.9: concubines, Brunhild "a second Jezebel", the sons not blessed (munro1895 l.894-912); Barmby's note (npnf213 l.4186-4190); "error is manifestly ancient; but truth which reproves it is ever more ancient still" (l.4592-4594, exact but for a comma). L.11: "twenty years after he had come to this place" (munro1895 l.1123); Nantes, the ship stuck, "God did not wish Columban to return home" (l.1330-1346); the Swabians at Brigantia, glossed Bregenz (l.1452, 1479-1481, 1495); Agilulf (l.1640-1642); Paul the Deacon, "kindly received by the king of the Langobards" (foulke1907 l.8968-8970); "After a single year in his monastery of Bobbio" and Munro's "probably 615" (munro1895 l.1705-1707, 1713). L.13: Letter II (PL 80 l.20758-20765; but see A-B1).

**Card.** All `keyWorks`, `legacy` and `uncertain` statements were checked against the lines the records cite. Faithful except as noted below: Gallandi on the age at leaving (PL 80 l.16145-16146), on Guntram and 590 (l.16146-16151), on the Olympiads (l.16160-16186); Goldast, "anno aetatis xc" (l.24174); Krusch on Fredegar (fredegar krusch1888 l.10043-10049, 10074); Barmby on Gregory's silence and Satan's hindering (npnf213 l.4206-4211; PL 80 l.20972); Wasserschleben on Fleming and the Continent (l.1559-1569); the Mâcon council (mansi10 l.61318-61385; PL 80 l.15978-15983); Bede II.4 (giles1903 l.3855-3857).

#### Findings

- **A-B1 BLOCKING (items 2, 4; a rendering in quotation marks drops the source's condition).** Brief l.13 and audio: "Let Gaul, I pray, hold us together," he wrote, "whom the kingdom of heaven will hold." The Latin sentence goes on: "Capiat nos simul, oro, Gallia, quos capiet regnum coelorum, si boni simus meriti" (PL 80 l.20763-20765). The rendering stops at the comma and drops "if our merits are good", with no mark of the cut. That turns his hope into a certainty. No English of this letter is held, so the words in quotation marks are the narrator's, but nothing tells a listener so, while the Gregory line two paragraphs earlier is marked "in Barmby's English". A second, smaller point: "those woods" comes right after Bobbio, so it can be heard as the Apennines. The letter means the Vosges ("in his silvis", l.20759; twelve years "inter vos", l.20761-20762).
  - Fix, brief l.13 and audio: "Writing to a council of Gallic bishops, he had asked to live in silence in the Vosges woods, by the bones of seventeen dead brothers. "Let Gaul, I pray, hold us together," he wrote, in modern words, "whom the kingdom of heaven will hold, if our merits are good.""
- **A-M1 MINOR (items 1, 7; an editor's placing told as the scene).** Brief l.1 opens "At Nantes, Columbanus was writing to his monks". The letter names no place. It says only that his brothers are "hic in vicinia Brittonum", here near the Bretons (PL 80 l.21345). The placing at Nantes is Mabillon's, as Gallandi quotes him: "ex ejus Epistola IV ad suos Luxovienses Namnetis scripta" (l.16362-16370). Gallandi repeats it at l.16380-16382. It fits Jonas, who has him held at Nantes for shipping (munro1895 l.1330-1332), but the narrator tells the editor's join as plain fact. The card does the same in `keyWorks` 3 ("to his monks from Nantes") and `uncertain` 6 ("the letter from Nantes").
  - Fix, brief l.1 and audio: "Columbanus was writing to his monks from near the Bretons when a messenger came in. A ship was being made ready, the messenger said, to carry him back to his own country against his will. If he were thrown into the sea like Jonah, he wrote, they should pray that someone would row their Jonah back to land." (The removed "He put the news into his letter" keeps the brief under the cap; l.11 still takes him to Nantes.)
  - Card `keyWorks` 3: "… twice to Pope Boniface IV, to his monks as he waited to be shipped home, and to a disciple …". Card `uncertain` 6: "Gallandi dates the letter to his monks to 610, and Mabillon, as Gallandi quotes him, places it at Nantes."
  - Records claim 1: add to the witness "placed at Nantes by Mabillon, as Gallandi quotes him (PL 80 l.16362-16370); the letter says 'hic in vicinia Brittonum' (l.21345)".
- **A-M2 MINOR (items 1, 12; the card contradicts itself).** Card `dates`: "No source used here gives his birth year. Gallandi reports … about the middle of the sixth century. William Dudley Foulke … gives about 543". Foulke's note gives a year. The records say what is meant: "No ancient line held gives it." Fix: "No early source used here gives his birth year."
- **A-M3 MINOR (items 1, 4; a loose word and a 30-word sentence).** Card `legacy.traces` 1: "names houses founded under his rule by people he had blessed. They include Donatus, bishop of Besançon, and his brother Ramelen, and the brothers Ado, at a house Dana Munro identifies as Jouarre, and Dado, on the little river Rebais." Columbanus raised Donatus from the font. Ramelen was born later, of the same promise, and Jonas tells of no blessing for him (munro1895 l.664-676). Only Ado and Dado are blessed as children (l.1415-1427). The second sentence runs 30 words with a stacked "and … and". Fix: "Jonas of Bobbio names houses founded under his rule. Donatus, bishop of Besançon, whom Columbanus raised from the font, founded one, and his brother Ramelen another. The brothers Ado and Dado, whom he blessed as children, founded two more. Dana Munro identifies Ado's as Jouarre; Dado's stood on the little river Rebais."
- **A-M4 MINOR (items 4, 9; an ambiguous phrase).** Card `uncertain` 1: "he learned more from Attala and Eustasius, abbots after Columbanus of Bobbio and Luxeuil." "Columbanus of Bobbio" reads as a name, and the sentence runs 30 words. Fix: "In his preface he says many who saw the deeds were still alive to tell them. He learned more, he says, from Attala and Eustasius, who followed Columbanus as abbots of Bobbio and Luxeuil."
- **A-M5 MINOR (item 8; first mentions on the card).** Card `dates` names "Charles Le Cointe and Mabillon", and later fields name "Ussher", "Goldast" and "Hodgkin" bare. A general listener knows none of them, and the card gives Le Cointe a forename. Fix at first mention: "Jean Mabillon" (`dates`), "James Ussher" (`uncertain` 4), "Melchior Goldast" (`uncertain` 4), and "citing Thomas Hodgkin" (`dates`, and "citing Hodgkin" in `uncertain` 1).
- **A-M6 MINOR (items 5, 12; a process word on a card, a reprinter as author).** Card `sources.about` 2: title "… in Chronologia sanctorum insulae Lerinensis (poor OCR)", author "Jonas of Bobbio; Vincentius Barralis". "Poor OCR" is the Library's register, which batch 1 ruled off cards. Barralis did not write the Life. He reprinted it from Laurentius Surius (barralis l.36412-36419, "EX TOMO SEXTO F. LAVRENTII SVRII"). Fix: title "Life of Columbanus in Latin, with Jonas's preface, from Laurentius Surius, as printed by Vincentius Barralis in Chronologia sanctorum insulae Lerinensis"; author "Jonas of Bobbio".

**Post-fix brief** (A-B1 and A-M1 applied together): 404 words, FK 7.6, Flesch 67.2. Under the cap.

**Verdict: NOT CLEAR** (1 blocking, 6 minor).

---

### Isidore of Seville (major)

| # | Item | Result |
|---|---|---|
| 1 | Each sentence sourced, source establishes it | FAIL (A-B2) |
| 2 | Quotes verbatim | PASS (the Brehaut lines are exact; the renderings keep every clause) |
| 3 | No invention | PASS |
| 4 | Reading aids, no AI tells | FAIL (A-M7) |
| 5 | Named witnesses, no role in place of one | FAIL (A-M8) |
| 6 | Partisan witness named and marked | PASS (Braulio as friend, Leander as brother) |
| 7 | Contested claims both sides | FAIL (A-B3, A-M9) |
| 8 | Common names, first mention | FAIL (A-M10) |
| 9 | One term for one thing | PASS |
| 10 | Story, scene opening, disputes in place, length | PASS |
| 11 | Readability | PASS (FK 8.0, Flesch 62.7) |
| 12 | Card order, missing fields absent, caveat repeated | FAIL (A-B4) |
| 13 | Audio tags | PASS |
| 14 | List line, Who test | PASS |

**Sentences checked and found faithful.** Brief l.1: Braulio, Letter V, "Septimum, ni fallor, annum … libros a te conditos Originum postulasse", "vertam preces in querelam", "Redde, redde, quos debes" (PL 80 l.52464-52467, 52484-52490, 52558; Lindsay "quod debes", l.740-741). Isidore to Braulio: "Tuae sanctitatis epistolae me in urbe Toletana invenerunt. Nam permotus fueram causa concilii", "quamvis debilis atque fessus", "Codicem Etymologiarum … de itinere transmisi, et, licet inemendatum prae valitudine" (lindsay1911 l.854-855, 880, 883-884). L.3: Ildefonsus ch. 9, "post Leandrum fratrem" (pl96 l.16899); Leander, "junioris fratris Isidori … parentes reliquerunt … de ejus nihil formidantes infantia" (PL 72 l.66698-66702). L.5: Ildefonsus, "annis fere quadraginta", the reigns from Reccared to Sisenand, and "in stuporem verteret audientes" (pl96 l.16951-16952, 16996-16999); Mommsen, "obiit a. 636" (mommsen1894 l.21945-21967). L.7: Seville II opens "Isidorus, Bisinnus, Rufinus …" (Hispana l.59351-59352); ch. XII, "ex haerese Acephalorum natione Syrus, ut asserit ipse, episcopus … deitatem passibilem asserens … per multos diuturnosque conflictus … duasque naturas et unam personam … confessus est" (l.59818-59836). L.9: Toledo IV heading and first signature (l.38613-38625, 40882-40884); Isidore's History, "aemulationem quidem habuit, sed non secundum scientiam: potestate enim conpulit, quos provocare fidei ratione oportuit" (mommsen1894 l.28443-28446). L.11: Braulio's list in Brehaut's English (brehaut1912 l.822-829), exact; Ildefonsus, "in ejus opere diem extremum visus est conclusisse" (pl96 l.16992-16995). L.13: Etymologies I.29, "For every consideration of a thing is clearer when its etymology is known" (brehaut1912 l.3591-3592), exact.

**Card.** Checked and faithful except as below: Mommsen on the start of his bishopric, the epitaph and Redemptus (mommsen1894 l.21945-21965); Brehaut on 600, 619, Toledo IV and Redemptus (brehaut1912 l.695-705); Brehaut on the thirteenth-century Lives (l.642-647); Lindsay on the faulty proarchetype (lindsay1911 l.337-347); the Maximus chronicle and Nicolás Antonio's notice (PL 80 l.50302-50304, 48904-48923, 49007-49011); Severianus (PL 83 l.122769-122770); Braulio's "lucerna ardens, et non marcescens" signed "manu sua" (PL 80 l.52416-52418); "detruncatos corrososque" (l.52593-52596).

#### Findings

- **A-B2 BLOCKING (items 1, 7; the canon is about Jews, and it orders coercion).** Brief l.9 and audio: "The council ruled that no one should be forced to believe. Those already forced into baptism under King Sisebut, it added, must keep the faith they had received." Card `legacy.traces` 2 says the same. The canon is headed "De discretione judaeorum" and reads "De judaeis autem hoc praecepit sancta synodus nemini deinceps ad credendum vim inferre". Of those forced under Sisebut it says "oportet ut fidem etiam quam vi vel necessitate susceperunt tenere cogantur", that they must be compelled to keep the faith they took under force (Hispana l.40196-40228). The brief makes a ruling about Jews into a general ruling on belief. It also softens "be compelled to keep" into "must keep". A listener hears a freedom-of-conscience decree the council did not make. Isidore's line on Sisebut, which follows, is also about forcing Jews (mommsen1894 l.28441-28446, OCR "Inilaros" for Iudaeos). The records claim quotes the canon correctly.
  - Fix, brief l.9 and audio: "The council ruled that from then on no Jew should be forced to believe. Jews already forced into baptism under King Sisebut, it added, must be made to keep the faith they had received."
  - Card `legacy.traces` 2: "The Fourth Council of Toledo, where Isidore signed first, ruled that from then on no Jew should be forced to believe. Jews already baptized by force under King Sisebut, it said, must be made to keep the faith."
- **A-B3 BLOCKING (items 1, 7; a disputed year told as settled, the other side left out).** Brief l.7 and audio: "In 619 Isidore is named first among the bishops who met in council at Seville." The acts give no year AD. They are dated "die iduum novembrium anno nono regni … Sisebuti, era DCLVII" (Hispana l.59339-59345). Era 657 gives 619, the arithmetic of the Spanish era, and the held witness for 619 is Ernest Brehaut, after Gams (brehaut1912 l.701-702, note 20 at l.718). Mansi heads the council 619 (mansi10 l.57663-57665). But the Annotatio Pagii that Mansi prints, "Ad An. Ch. 619 n. 2" (l.59503-59536; OCR "ApvpnoTraTio Pacey"), says the date is "magnis tenebris circumsepta". Era 657 falls in 619, it says, but Sisebut's ninth year began only in the next year, after mid-February. Isidore of Beja, Rodrigo of Toledo and Vasaeus give Sisebut's seventh year, Vasaeus adding December. Pagi prefers them and sets the council in 618, "si tamen mense Novembri aut Decembri celebrata sit" (l.59519-59536; OCR "628" and "648" for 618). Vasaeus's and Mariana's seventh year is also quoted in Migne's Alcuin (`alcuin_opera-omnia-letters_migne-pl100-101_1863.txt` l.27624-27627, 27645-27646), and Bruns's list of councils gives "618 Hispalense II" (`codex-canonum-ecclesiae-africanae_bruns-pars1-1839.txt` l.27403). A bare year is wanted only where the year is the event, and here the year is disputed. The card's `uncertain` 4 also gives "the Second Council of Seville in 619" as Brehaut's, with no other side.
  - Fix, brief l.7 and audio: "Under King Sisebut, Isidore is named first among the bishops who met in council at Seville."
  - Card, a new `uncertain` item after item 4: "The year of the Second Council of Seville. Its acts give the Spanish era 657, which is 619, and King Sisebut's ninth year. Antoine Pagi, in a note Mansi prints, says the two do not agree. He follows Isidore of Beja and later Spanish writers, who give Sisebut's seventh year, and sets it in 618. Ernest Brehaut gives 619." (Mansi's heading names him only "Pagius". The note's form, "Ad An. Ch. 619 n. 2", is that of Antoine Pagi's Critica. If the drafter prefers not to supply the forename, write "Pagi".)
  - Records: tag the Seville II claim's year Contested. Add a `contested_claim` "The year of the Second Council of Seville", with sides "The acts: era 657 and Sisebut's ninth year (Hispana l.59339-59345)"; "Brehaut, after Gams: 619 (brehaut1912 l.701-702); Mansi's heading 619 (mansi10 l.57663-57665)"; and "Pagi, in Mansi: the era and the regnal year disagree; Sisebut's seventh year, after Isidore of Beja, Rodrigo of Toledo and Vasaeus, so 618 if held in November or December (mansi10 l.59506-59536; OCR '628', '648'); Vasaeus and Mariana as quoted in PL 100-101 l.27624-27646; Bruns's list, 618 (l.27403)".
- **A-B4 BLOCKING (items 1, 12; a false absence in the records, and the card hides a held account).** Records `absent_details` 2: "Redemptus's account of his death. Not held; known here only through Mommsen (…) and Brehaut (…)." Card `uncertain` 3 ends: "Redemptus's account is not among the sources used here." Bernhard Poschmann, held in the Library, retells the account and quotes its Latin. Isidore had himself carried into the church of the martyr Vincent, put on sackcloth and ashes, and confessed before the people, the clergy and two bishops. He said "peccavi super numerum arene maris". Then he received communion from the bishops and asked the people's pardon, "Et omnes voce magna pro eo indulgentiam cum lacrimis postulaverunt" (`poschmann_abendlaendische-kirchenbusse-deu_1928.txt` l.15200-15240). The records' "not held … only through Mommsen and Brehaut" is false. The card's sentence is literally true, but it points the reader away from a held source on the very point it raises.
  - Fix, card `uncertain` 3, last sentence: "Bernhard Poschmann retells Redemptus's account and quotes its Latin. Isidore, he reports, had himself carried into the church of Saint Vincent and did public penance before the people and two bishops."
  - Card `sources.about`: add "Die abendländische Kirchenbusse im Ausgang des christlichen Altertums, on Redemptus's account of Isidore's death", author "Bernhard Poschmann", date "1928", language "German", file `cic/texts/poschmann_abendlaendische-kirchenbusse-deu_1928.txt`.
  - Records `absent_details` 2: "Redemptus's text itself is not held. Poschmann retells it and quotes its Latin (poschmann1928 l.15200-15240); Mommsen (mommsen1894 l.21960-21965) and Brehaut (brehaut1912 l.703-704, 726-727) report it." Add a records claim with Poschmann as witness, Dominant Modern Reconstruction.
- **A-M7 MINOR (items 2, 4; narrator renderings not marked).** Brief l.1, "Give back, give back what you owe," and l.9, Sisebut "had zeal, but not according to knowledge," are the narrator's English from Latin. No English of either is held: Brehaut's book has neither (searched). L.11 marks Brehaut's English, but l.13 quotes Brehaut's English unmarked, so a listener cannot tell the translator's words from the narrator's. The renderings themselves keep every clause.
  - Fix, brief l.1: after "he pleaded." add "Their Latin is told here in modern words." Brief l.9: "In his History of the Goths, Isidore wrote that Sisebut had zeal, but not according to knowledge." (quotation marks removed). Brief l.13: "For every consideration of a thing is clearer," Isidore wrote, in Brehaut's English, "when its etymology is known."
  - To keep the brief under the cap, brief l.5 becomes "Theodor Mommsen sets his death in 636." The card `dates` keeps his grounds.
- **A-M8 MINOR (items 1, 5; the translator's identification given as Braulio's).** Card `legacy.remembered` 2: "Braulio applies to him Cicero's words to Varro". Braulio says only "the famous words of the philosopher" (brehaut1912 l.752-753). Cicero to Varro is Brehaut's note 24 (l.772-773). Fix: "Braulio applies to him words of "the philosopher", which Ernest Brehaut traces to Cicero writing to Varro: "your books brought us home, as it were, so that we could at last recognize who and where we were.""
- **A-M9 MINOR (item 7; a held witness missing from one side).** Card `uncertain` 5, on the addressee of the Etymologies. Brehaut, held, says "the brief preface, addressed to Braulio" (brehaut1912 l.1158-1159). Lindsay too speaks in his own preface of "ipse ille liber quem Isidorus Braulioni transmisit" (lindsay1911 l.337-338), though his text heads the covering letter to Sisebut. Fix, add to the item: "Ernest Brehaut calls the preface addressed to Braulio." Records: add Brehaut l.1158-1159 to the Braulio side of the `contested_claim`.
- **A-M10 MINOR (item 8; first mention).** Card `uncertain` 3 names "Redemptus" bare. Mommsen calls him "archidiaconus" (l.21960) and Brehaut "a cleric named Redemptus" (l.702-703). Fix: "the cleric Redemptus". Card `uncertain` 5 names "Flórez" bare; fix, "Enrique Flórez".

**Post-fix brief** (A-B2, A-B3 and A-M7 applied together): 405 words, FK 7.8, Flesch 64.0. At the cap and not over it.

**Verdict: NOT CLEAR** (3 blocking, 4 minor).

---

### John of Biclaro (recorder, standard length)

| # | Item | Result |
|---|---|---|
| 1 | Each sentence sourced, source establishes it | FAIL (A-B5, A-M11, A-M13) |
| 2 | Quotes verbatim | PASS (renderings faithful; see A-M14) |
| 3 | No invention | PASS |
| 4 | Reading aids, no AI tells | FAIL (A-M14) |
| 5 | Named witnesses, no role in place of one | PASS |
| 6 | Partisan witness named and marked | PASS |
| 7 | Contested claims both sides | PASS |
| 8 | Common names, first mention | FAIL (A-M15) |
| 9 | One term for one thing | FAIL (A-M12) |
| 10 | Story, scene opening, disputes in place, length | PASS |
| 11 | Readability | PASS (FK 7.6, Flesch 65.4) |
| 12 | Card order, missing fields absent, caveat repeated | FAIL (A-B5) |
| 13 | Audio tags | PASS |
| 14 | List line, Who test | PASS |

**Sentences checked and found faithful.** Brief l.1: "In regia urbe mortalitas inguinalis plagae exardescit, in qua multa milia hominum vidimus defecisse"; "Legati gentis Maccurritarum Constantinopolim veniunt dentes elephantinos et camelopardam Iustino principi munera offerentes", both under "ANNO VII IVSTINI" (mommsen1894 l.19920, 19930-19937). L.3: Isidore, On Famous Men 44, born at Scallabis, a Goth, "post decem et septem annos" in PL 83 (l.122958-122963) and "septimo decimo anno" in Mommsen (l.19387-19389), with the seventh year in some copies (apparatus l.19400-19410); Mommsen's argument from the Constantinople news (l.19397-19399, 19426-19429). L.5: the exile at Barcelona, ten years of "insidias et persecutiones ab Arianis", the monastery and rule (l.19390-19394); Mommsen on the Gerona signatures (l.19440-19446; Hispana l.60740, 49418-49419). L.7: John's own note, "Hucusque Victor Tunnunensis … nos quae consecuta sunt adicere curavimus" (l.19766-19767); Isidore on the span (PL 83 l.123049-123053); Hermenegild "factione Gosuinthae reginae tyrannidem assumens" (l.20114-20115); Reccared "renovans temporibus nostris antiquum principem Constantinum Magnum sanctam synodum Nicaenam sua illustrasse praesentia" (l.20400-20402); Mommsen, "summa admiratione prosequitur" (l.19432-19433). L.9: the preface (l.19772-19778).

**Card.** Checked and faithful except as below: Gallandi on Antonio's 592, Mariana's "post annum 621" and the Pyrenees (PL 72 l.64478-64500); Mommsen on Biclaro's site (mommsen1894 l.19436-19440), the margin years and 590 (l.19733-19745), and "Expilavit eum pariter atque Victorem Isidorus" (l.19763); Alicius at Toledo III (Hispana l.38268-38269); Nonnitus (pl96 l.17020-17021; Hispana l.40915-40916); the PL 103 note and Calmet (l.34126-34137); the Maccurritae (mommsen1894 l.19833, 19879-19880).

#### Findings

- **A-B5 BLOCKING (items 1, 12; wrong on the card).** Card `keyWorks` 1: "… on the empire, the Lombards, the Franks and the Visigoths; it ends with the Third Council of Toledo". Card `knownFor`: "ends with King Reccared's fourth year and the Third Council of Toledo". The Chronicle does not end with the council. After it, under the same year, John tells of the Persian king's conversion and then the plot of Argimund, a duke of the king's household. Argimund was flogged, shaved, had his right hand cut off and was paraded on an ass through Toledo. A reckoning of the years from Adam follows (mommsen1894 l.20423-20437, 20460-20467).
  - Fix, `keyWorks` 1: "year-by-year notes from the first year of the emperor Justin the Younger to King Reccared's fourth, on the empire, the Lombards, the Franks and the Visigoths; its last year tells of the Third Council of Toledo and a plot against Reccared". `knownFor`: "His Chronicle carries on from Victor of Tunnuna's and runs to King Reccared's fourth year, the year of the Third Council of Toledo."
- **A-M11 MINOR (item 1; "short" against the editor's word).** Brief l.3, "His life is known mainly from Isidore's short notice", and card `uncertain` 1, "Isidore of Seville's short notice". Mommsen says Isidore tells John's life "solito diligentius et plenius", with more care and fullness than usual (mommsen1894 l.19387). Fix, brief: "His life is known mainly from Isidore's notice of him." Card: "His life is known mainly from Isidore of Seville's notice of him in On Famous Men, which Theodor Mommsen calls fuller than Isidore's usual."
- **A-M12 MINOR (item 9 and batch consistency; name form).** Brief l.7: "Leovigild's queen, Goiswinth". The Latin here is "Gosuinthae" (mommsen1894 l.20115; "Gosuintha" at l.19837, 20339, 20342), and batch 5's `reccared` card calls her "Queen Gosuintha, his father's widow". The same queen should carry the same name across the tree. Fix: "Leovigild's queen, Gosuintha."
- **A-M13 MINOR (item 1; "learned Greek and Latin").** Brief l.3: "went to Constantinople and learned Greek and Latin there." Isidore says "Graeca et Latina eruditione nutritus", nourished in Greek and Latin learning (mommsen1894 l.19388). A Goth of Lusitania did not go east to learn Latin. Fix: "As a young man John went to Constantinople and was schooled there in Greek and Latin learning."
- **A-M14 MINOR (items 2, 4; narrator renderings not marked).** Brief l.1, "We saw many thousands of people die of it", and l.9, "partly what we saw with our own eyes, and partly what we learned from the reports of faithful men", are the narrator's English from John's Latin (l.19930-19931, 19776-19777), in quotation marks with no sign that they are. Both renderings are faithful. Adding a marker sentence would take the brief past the recorder length, so the fix tells both in reported speech. Fix, brief l.1: "He saw many thousands of people die of it, he says." Brief l.9: "He set down partly what he saw with his own eyes, and partly what he learned from the reports of faithful men."
- **A-M15 MINOR (item 8; first mentions on the card).** Card `uncertain` 4 names "Mariana" and `uncertain` 6 names "Calmet" bare. Fix: "Juan de Mariana" and "Augustin Calmet".

**Post-fix brief** (A-M11, A-M12, A-M13 and A-M14 applied together): 325 words, FK 7.9, Flesch 64.6.

**Verdict: NOT CLEAR** (1 blocking, 5 minor).

---

### Verdicts

- `columbanus`: NOT CLEAR (1 blocking, 6 minor)
- `isidore-of-seville`: NOT CLEAR (3 blocking, 4 minor)
- `john-of-biclaro`: NOT CLEAR (1 blocking, 5 minor)

Part A totals: 5 blocking, 15 minor.

## R1 review, part B: John Moschus, Babai the Great, Severinus of Noricum (era 3 batch 6)

Reviewer: independent Opus, first sight of these drafts. Bar: `Who_Profile_Pattern.md` review checklist 1 to 14 and the standards it points to (Style Guide 1.1 to 1.12); `CLAUDE.md` "Trust and source fidelity" and "Accessible and rigorous"; the Who profile rulings in `Decision-Log.md`, 2026-11-12 to 2026-11-14. Babai the Great is major (cap 2:30, about 405 words, a cap and not a target). John Moschus is a recorder at standard length, and Severinus is standard: both 1 to 2 minutes, at most about 325 words at 162 wpm. Severinus's card tradition, "Early Benedictine / Italian Monasticism", is the coordinator's call (2026-11-14) and was checked only for being stated as the README says. I edited no profile file, made no paid or model-API calls and used no web.

Profiles: `john-moschus`, `babai-the-great`, `severinus-of-noricum`, with their cards, audio scripts and `records.json` entries, and the batch `README.md` sentences on them. Files are in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era3/batch6/`. Brief line numbers refer to the `.brief.txt` files, where each paragraph is one line and blank lines count (paragraphs sit on l.1, 3, 5, 7, 9, 11, 13). Card fields are named by key and list position. Other line numbers point to files under `cic/texts/`. An extra section checks the batch 5 `henana-of-adiabene` records correction made on this branch.

Method. I opened every quoted passage at its cited line in the vendored file. For each one I read the context to see who is speaking: the ancient author, a document he copies, a translator's or editor's note, or a running head. That meant the PG 87.3 Moschus volume, where Papebroch's Life of Sophronius quotes the old notice, Fabricius's notice as Harles printed it ("HAL." marks, "Hactenus Fabricius" at l.24445), and Lipomanus's letter. For Babai it meant Scher's Chronicle of Seert, Budge's Thomas of Marga, Labourt, Chabot's and Braun's Synodicon, Duval's Ishoyahb, Badger's Abdisho and Wigram. For Severinus it meant Robinson's Eugippius, Foulke's Paul the Deacon and Mansi 10. I checked each factual sentence of each brief against its passage. Before accepting any "not held", "only" or "none" claim, I searched all of `cic/texts/` with whitespace-tolerant patterns under every spelling and OCR form I could find. For Moschus: Moschus, Moschi, Moscho, Eucrat-, Evirat-, Limonar-, Leimon, "Spiritual Meadow", "Pratum spirituale", "Pré spirituel". For Babai: Babai, Babaï, Bäbai, Babhai, Bàbhay, Babaeus, Babaeo, Babaoo, "Mar iJabae". For Henana: Hnana, Henana, Hannänä, Hananus, Rannana. For Severinus: Severin- beside Noric-, Eugipp-, Favian-, Lucull- and Odoac-. That search found held files the drafts do not use. Mari's and 'Amr's histories name Babai the Great (Gismondi's Latin; the records say they do not). Oskar Braun's 1915 German gives Babai's whole Life of George, and Georg Hoffmann's 1880 German gives extracts. The anonymous Syriac chronicle Guidi edited (Chronica minora) has a notice of Babai and his quarrel with "Babai the Little". Cotelier's Monumenta II and John of Damascus in PG 94 hold Meadow chapters and the Damascene's citations. The Anonymus Valesianus in Mommsen's Chronica minora quotes the Life of Severinus. Readability is `engine.m1.gates.grade_text`, run from the repo root. Every brief fix below was applied together to a scratch copy (`/tmp/claude-0/-home-user-CIC-Project/5632ba95-e0b1-504b-a130-94b73aea15af/scratchpad/partB/`) and re-scored.

#### Applies to all three

- **Audio = brief.** Each audio script matches its brief exactly once `[calmly] ` and `[warmly] ` are removed (checked by script). Each starts with `[calmly]` and has one `[warmly]`, at the start of the closing paragraph. No tag appears in any brief or card. When a brief fix below changes a line, the audio script follows it.
- **Readability.** All three pass before and after the fixes. No narrator sentence runs past 25 words. Babai l.13 has 30, but 24 of them are Thomas's quoted words.
- **Card order.** All three follow Mark's order. Missing fields are left out: Severinus has no `keyWorks` or `ownWords`. Each `uncertain` list opens with the brief's caveat.
- **Who test (item 14).** Moschus is a recorder. Babai heads a following and a body of 84 works. Severinus is a founder known through his disciple's record, which the brief marks as a saint's Life. The drafts carry no list lines; those belong to the map build and were not checked here.
- **Modern renderings in quotation marks.** Moschus l.1 and l.11 put English renderings of the Latin column in quotation marks. Babai l.9 renders Labourt's French. The records mark each one as a rendering. I checked each against its Latin or French and found them faithful (Moschus l.10086-10095, 3784-3786; Labourt l.15845-15866). The pattern allows an Opus-authored rendering presented as the quote, and the card's `uncertain` (Moschus) and `ownWords` (Babai) say which language stands behind them. So I raise no finding.

| Profile | Words | Est. length @162 | FK | Flesch | After fixes: words, FK, Flesch |
|---|---|---|---|---|---|
| John Moschus (recorder) | 327 | 2:01 | 6.7 | 70.0 | 324, 7.0, 68.4 |
| Babai the Great (major) | 403 | 2:29 | 6.8 | 73.0 | 404, 6.8, 73.0 |
| Severinus of Noricum | 322 | 1:59 | 6.9 | 69.4 | 324, 7.0, 69.0 |

Totals for part B: 6 blocking (B-B1 to B-B5, B-H1) and 14 minor (B-M1 to B-M14).

---

#### 1. John Moschus (recorder)

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | minor (B-M1) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | minor (B-M3) |
| 5 | No role for a named witness | PASS |
| 6 | Partisan witness marked | PASS (n/a) |
| 7 | Contested claims show both sides | minor (B-M4) |
| 8 | Common names have place | minor (B-M2) |
| 9 | One term for one thing | PASS |
| 10 | Story, scene, disputes in place, length | minor (B-M3, 327 words) |
| 11 | Readability | PASS (6.7 / 70.0) |
| 12 | Card order, caveat repeated | PASS |
| 13 | Audio tags | PASS |
| 14 | List line, Who test | PASS (recorder) |

Checked and sound: the chapter 77 scene (l.9983-10095: noon, Stephen asleep, the Tetrapylon, the three blind men, the corpse that sat up, Sophronius's nod and words); the old notice as Papebroch prints it. That covers Saint Theodosius, the Jordan desert, the New Laura, Antioch, Alexandria, Rome, the wish for burial on Sinai and the Agarene raids (l.24917-24965, 25365-25398, 25455-25462). It also covers Papebroch's 620 from the eighth indiction (l.25403-25405) and Fabricius's first paragraph, before any "HAL." mark (l.3368-3400: "Passim invehitur in heresin Severi Acephali", "fabulosis non destitutum narrationibus", 620 from Bolland). I also checked Lipomanus on John of Damascus and Nicaea II (l.3664-3672), chapter 45 (l.7564-7590) and the dedication (l.3756, 3781-3786). The points the coordinator asked about hold. Photius's notice (Bibliotheca cod. 199) is not held: Freese's volume 1 is the only Photius, and searches for Moschus, Eucrat-, Leimon and 199 find nothing. No English Meadow is held. The brief keeps who is speaking straight, giving the notice its own voice ("the notice says") and Papebroch and Fabricius theirs.

**B-M1 MINOR (item 1). "Monks he met" overstates the Meadow's reach.** Brief l.3, "his book of stories about monks he met"; card `knownFor`, "the sayings and deeds of the monks they met". The dedication speaks of holy men "qui temporibus nostris claruere" (l.3776-3777). The notice says he wrote down what he "audisset vel vidisset" (l.24973), and Papebroch says the same: "ex omnibus quae viderat, audierat" (l.25364-25365). Many chapters are stories told to him about others ("Enarravit nobis abbas Joannes Persa", l.3662). Fix, brief l.3 (merged with B-M3): "Moschus, a monk of Palestine, tells this in the Spiritual Meadow, his book of stories about monks of his time, written for Sophronius." Fix, `knownFor`: "Monk of Palestine who travelled with his disciple Sophronius, later patriarch of Jerusalem, and gathered the sayings and deeds of monks of his time, seen on their travels or told to them, into the Spiritual Meadow, which he dedicated to him."

**B-M2 MINOR (item 8). Three names without their identifier at first mention.**
- Brief l.1, "his friend Sophronius". The identifier "later patriarch of Jerusalem" comes only in l.3. Fix: "One noon in Alexandria, John Moschus and his friend Sophronius, later patriarch of Jerusalem, went to study with the philosopher Stephen." (l.3 loses the phrase, see B-M1.)
- Brief l.5, "says Photius copied much of it". This is a bare name a general listener cannot place. Lipomanus gives "Photius patriarcha Constantinopolitanus" (l.3630). Fix: "says Photius of Constantinople copied much of it." On the card, `keyWorks` 1 `about` becomes "Photius of Constantinople, as Papebroch quotes him, found up to 342 in some copies".
- Card `dates`, "the reigns of the emperors Tiberius and Maurice". A listener will think of Tiberius Caesar. The notes to the same volume write "temporibus Tiberii II imp." (l.24460). Fix: "the reigns of the emperors Tiberius II and Maurice".

**B-M3 MINOR (items 4, 10). Length and two loose phrasings.** The brief runs 327 words, past the non-major ceiling of about 325. In l.5, "He lived long in the desert by the Jordan and at the New Laura" spreads "long" to the New Laura. The notice gives "non exiguo tempore" only for the Jordan desert (l.24938-24939). Fixes, applied with B-M1 and B-M2 to reach 324 words (FK 7.0, Flesch 68.4):
- l.1: "where three blind men were telling how each had lost his sight" becomes "where three blind men told how each had lost his sight".
- l.5: "He lived long in the desert by the Jordan, then at the New Laura of Saint Sabas."
- l.5: "When he heard the holy places had been taken," becomes "Hearing that the holy places had been taken,".
- l.7: "Raiders had closed the road to Sinai, so Sophronius buried him there."

**B-M4 MINOR (item 7). The notice's last words, which Papebroch has to explain away, are not on the card.** The brief tells the burial by Sophronius on the notice's word (l.7). The notice ends by saying the disciple who buried him "reliquumque vitae suae tempus in eodem coenobio transegit" (l.25464-25465). Papebroch says that unless Moschus's companion was someone other than Sophronius of Jerusalem, against "totius pene Graecae antiquitatis consensum", the words must be read loosely, as "de longe maxima vitae reliquae parte" (l.25465-25473). The brief may stand. The card should carry the point. Add to `uncertain`, after "His years": "The disciple. The notice says the disciple who buried him spent the rest of his life at Saint Theodosius. Daniel Papebroch, who holds with almost all Greek tradition that the disciple was Sophronius, later patriarch of Jerusalem, reads that as most of the rest of his life."

**B-M5 MINOR (records). The "English translation" note misdescribes what the search finds.** `absent_details` "An English translation of the Meadow" says the whole-Library search "finds only citations". It also finds two held texts. Cotelier's Monumenta II holds Meadow chapters in Greek and Latin (`cyril-scythopolis_vita-euthymii-cotelier-monumenta-v2-grc-lat_1681.txt` l.46158-59653, "EX JOHANNIS MOSCHI" running heads). John of Damascus's own citations under Sophronius's name are held in PG 94 (`john-damascus_opera-omnia-t1-with-vita-pg94-grc-lat_migne1860.txt` l.91844, 94857, 96433). The absence itself stands. Fix the note: "None held. Whole-Library search for Moschus/Moschi/Moscho, Eucrat-, Evirat-, Limonar-, Leimon, 'Spiritual Meadow' and 'Pratum spirituale' finds no English. It finds Cotelier's Greek-Latin chapters (cotelier monumenta-v2 l.46158-59653), which duplicate part of PG 87.3, John of Damascus's citations in PG 94 (l.91844, 94857, 96433), and citations elsewhere (e.g. Wardrop's Life of Nino l.16933-17002, PO 8, PO 16, Acta Sanctorum March III). The file header says no public-domain English exists."

**Verdict: John Moschus CLEAR** (no blocking finding; B-M1 to B-M5 to apply).

---

#### 2. Babai the Great (major)

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | FAIL (B-B1) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS |
| 5 | No role for a named witness | FAIL (B-B2, Chabot for Mari and 'Amr) |
| 6 | Partisan witness marked | PASS (Braun on Babai; Thomas writing at Beth Abe) |
| 7 | Contested claims show both sides | FAIL (B-B1, B-B4, B-B5) |
| 8 | Common names have place | minor (B-M6); FAIL on namesakes (B-B4) |
| 9 | One term for one thing | PASS |
| 10 | Story, scene, disputes in place, length | PASS (403 words, under the cap) |
| 11 | Readability | PASS (6.8 / 73.0) |
| 12 | Card order, caveat repeated | PASS |
| 13 | Audio tags | PASS |
| 14 | List line, Who test | PASS |

Checked and sound: the Seert scene (l.29640-29644) and Babai's career there (l.29652-29680). Thomas I.7 ("somewhat hasty of speech and harsh in command", l.2100-2107), I.12-14 (Jacob's expulsion and the fathers' rebuke, l.2681-2683, 2769-2770; the dispersion, l.2938-3022), I.27 (the three metropolitans, l.4085-4140) and I.35 (the refusal and the angel, l.5164-5188; the closing quotation is verbatim). Braun's "der leidenschaftliche Babai" (braun1900 l.13690-13696). Labourt's De Unione passage (l.15845-15866). Scher's reading of the death (l.29693-29695). On the Thomas of Marga lead, the card rightly cites Book I. Book III, chapters I to III, is Rabban Babai of Gebilta under Selibha-zekha (l.12861-12895), a different man. The brief tells the Seert-against-Thomas dispute over his end in place, naming Scher as the reader. But see B-B4 on the namesakes, and B-B1 and B-B5 on dates.

**B-B1 BLOCKING (items 1, 7). Brief l.3 makes him abbot in the late 500s.** "Babai was an abbot of the Church of the East, in the Persian empire, in the late 500s and early 600s." No source has him abbot before the 600s. Scher reckons his succession to Dadisho "en 603/4" (seert l.29695). Labourt puts Dadisho's death "entre 615 et 620" (labourt1904 l.17771-17772). The card's own `uncertain` 4 carries that dispute. In the 580s and 590s he was a monk under Abraham and Dadisho (seert l.29644-29653; Thomas l.2104-2107). Fix: "Babai was a monk of the Church of the East, in the Persian empire, in the late 500s and early 600s."

**B-B2 BLOCKING (false absence, witness swap: records `absent_details` 3; card `uncertain` 5).** The records say Mari and 'Amr "name other Babais ... but no line naming Babai the Great was found". Both name him, in OCR the search missed. Mari: "Proprio itaque patriarcha ecclesia caruit ad annos decem et septem, eius interea gubernationem gerentibus Mar Aba archidiacono atque Mar Babaoo Magno e coenobio Mar Abraham" (`mari-ibn-sulayman_...gismondi1899.txt` l.13514-13517; "Babaoo" = Babaeo). 'Amr: "Sedem itaque administravit [citra ordinationem ut vicarius] Mar A!ia archidiaconus una cum Mar iJabae-) ^lngno" (`amr-ibn-matta_...gismondi1896-1897.txt` l.13424-13426; = Mar Aba ... Mar Babaeo Magno). The card's `uncertain` 5 gives the point to "J.-B. Chabot says the archdeacon Mar Aba and Babai directed the church". That passage names its sources: "Comp. 'Amr et Mâri dans la Vie du patriarche Grégoire" (chabot1902 l.37359-37361). So the card credits the modern editor with what the held medieval histories say.
- Fix, card `uncertain` 5: "His part in the vacancy. Thomas says three metropolitans asked him to visit the monasteries; the angel in Thomas's story calls him the vicar of the catholicos. The Arabic histories of Mari and 'Amr, in Enrico Gismondi's Latin, say the archdeacon Mar Aba and Mar Babai the Great governed the church while it had no head, and Mari counts seventeen years. J.-B. Chabot follows them."
- Fix, records: replace `absent_details` "Mari and Amr on Babai the Great" with a claim. Claim: "Mari: 'eius interea gubernationem gerentibus Mar Aba archidiacono atque Mar Babaoo Magno e coenobio Mar Abraham' for 'annos decem et septem' (OCR 'Babaoo' = Babaeo); 'Amr: 'Sedem itaque administravit [citra ordinationem ut vicarius] Mar A!ia archidiaconus una cum Mar iJabae-) ^lngno' (OCR for Mar Aba ... Mar Babaeo Magno; the bracket is Gismondi's)". Witness: "Mari, tr. Gismondi (mari gismondi1899 l.13514-13517); 'Amr, tr. Gismondi (amr gismondi1896-1897 l.13424-13426); Chabot cites both (chabot1902 l.37359-37361)". `formation_confidence`: Documented.

**B-B3 BLOCKING (false absence: records `absent_details` 1; card `keyWorks` 2 and `sources.ownWords`).** The records say "the Life of George only as two passages in Chabot's French ... Searched all of cic/texts for Babai/Babaï/Babhai/Babaeus". The whole Life is held in German, under the spelling "Bäbai". Oskar Braun's translation runs from "Geschichte unseres herrlichen und allheiligen Vaters Mär Giwargis ... verfaßt vom heiligen Rabban Mär Bäbai, dem Abte auf dem Berge Izalä" (`persian-martyr-acts_ausgewahlte-akten-persischer-martyrer-bkv22-deu_braun1915.txt` l.12419-12423). It runs to the end of the volume's acts, and Braun abridges only the long introduction (l.12442-12443). Braun's own heading dates George's death to 14 January 615 and calls Babai "Klostervisitator" during the vacancy "608—628" (l.852-858). The Henana charges are at l.13355-13400. Georg Hoffmann's German extracts of the same Life are also held (`persian-martyr-acts_auszuge-aus-syrischen-akten-persischer-martyrer-deu_hoffmann1880.txt` l.5596-5612). The held Life also carries Babai's own first-person preface, listing his earlier Lives of Abraham of Kashkar, written "vor ungefähr dreiunddreißig Jahren", and of Dadisho of Beth Daraye (braun1915 l.12435-12446).
- Fix, records `absent_details` 1: "The Book of the Union is held only as passages quoted in Labourt's French (l.15845-16120). The Life of George is held whole in Oskar Braun's German (braun1915 l.12419 ff., the introduction abridged, l.12442-12443), in Georg Hoffmann's German extracts (hoffmann1880 l.5596-5612) and as two passages in Chabot's French (chabot1902 l.42080-42240). No Syriac or English text of his books is held. Searched all of cic/texts for Babai/Babaï/Bäbai/Babhai/Bàbhay/Babaeus/Babaeo."
- Fix, card `keyWorks` 2 `about`: "a monk of Izla, once a Magian named Mihramgushnasp, put to death under Khosrau. Oskar Braun translates the whole Life into German, and J.-B. Chabot gives two passages in French, among them the charges against Henana of Adiabene; Scher says Paul Bedjan published the Syriac".
- Fix, card `sources.ownWords`: add `{"title": "Life of the martyr George (Mar Giwargis), in Ausgewählte Akten persischer Märtyrer (German tr. Oskar Braun)", "language": "German translation", "file": "cic/texts/persian-martyr-acts_ausgewahlte-akten-persischer-martyrer-bkv22-deu_braun1915.txt"}`.

**B-B4 BLOCKING (items 7, 8; namesakes kept apart wrongly; a held near-contemporary source unused: card `uncertain` 6 and 1; records).** Card `uncertain` 6 lists "Rabban Babai of Gebilta, the singer ... nor Babai bar Nisibnaye, Babai of Nisibis or Babai the Scribe" as separate men. The held East Syrian chronicle that Guidi edited (`chronica-minora-pars-prior-versio-lat_guidi1903.txt`) treats bar Nisibnaye and "Babai of Nisibis" as one man, and as Babai the Great's own contemporary. It names "Màr Babhay filius Nisibenorum" among the monks who came out of the Izla monastery (l.2032-2037). It says Satan stirred quarrels between "duo Babhay", and that "Asseclae, monachi, Mar Babhay magni (maioris) nemini permittebant ut in suum monasterium intraret, quin anathema diceret in eximium Mar Babhay nisibenum quem Babhay parvum (minorem) cognominaverunt" (l.2051-2058). It also says "Scripsit autem Mar Babhay magnus (maior) libros multos, disputationes atque interpretationes" (l.2069-2070). Labourt, a source the card already uses, reports the same quarrel from "l'anonyme de Guidi" (labourt1904 l.13093-13096). Budge instead places "Babhai bar-Nesibhnaye" under the catholicos Selibha-zekha (713-729), "famous for his beautiful voice" (budge1893 l.2071-2073). That is the time and the gift Thomas gives Rabban Babai of Gebilta (l.12863-12895). So the card splits what may be one man into two, and leaves out a dated quarrel between the two Babais that a near-contemporary chronicle records.
- Fix, card `uncertain` 6: "Namesakes. He is not Babai the catholicos of 497 to 502 in J.-B. Chabot's dates, nor Babai the Scribe, whom Abdisho of Nisibis lists. Nor is he his contemporary Babai of Nisibis, also called bar Nisibnaye, a monk who came out of Izla. An anonymous Syriac chronicle that Ignazio Guidi edited calls that monk Babai the Little, and says Babai the Great's followers let no one into their monastery who would not anathematize him. E. A. Wallis Budge instead puts a Babai bar Nesibhnaye, famous for his voice, under the catholicos Selibha-zekha, the time Thomas gives for Rabban Babai of Gebilta, the singer and founder of schools."
- Fix, card `uncertain` 1, add after its first sentence: "An anonymous Syriac chronicle that Ignazio Guidi edited also praises him and tells of his followers' quarrel with Babai the Little."
- Fix, records: add a claim. Claim: the three Guidi quotations above. Witness: "Anonymous East Syrian chronicle, tr. Guidi (chronica-minora guidi1903 l.2032-2037, 2051-2058, 2069-2070); Labourt (labourt1904 l.13093-13096)". `formation_confidence`: Documented. Add a `contested_claim`: "Who Babai bar Nisibnaye was". Sides: "Guidi's chronicle: Babai of Nisibis, son of the Nisibenes, a monk from Izla and Babai the Great's rival, called Babai the Little (l.2036-2058). Budge: Babhai bar-Nesibhnaye flourished under Selibha-zekha, 713-729 (budge1893 l.2071-2073)." Replace `absent_details` 4's companion note as needed so it names the chronicle.

**B-B5 BLOCKING (an editor's year told as the source's: card `legacy.traces` 4).** "In 612, the Chronicle of Seert says, he was too weak and old to join the bishops' debate before Khosrau, but helped them with his pen." The chronicle gives no year. "En 612" is Scher's footnote (seert l.29565), as the records' own witness line says ("612 is Scher's note"). Fix: "The Chronicle of Seert says he was too weak and old to join the bishops' debate before Khosrau, which Addai Scher dates to 612, but helped them with his pen."

**B-M6 MINOR (item 8). Brief l.7, "His Life of the martyr George".** George is a common name. Fix: "His Life of the Izla martyr George charges Henana with teaching fate and denying the resurrection of the body." (Post-fix with B-B1: 404 words, FK 6.8, Flesch 73.0.)

**B-M7 MINOR (item 1). Card `keyWorks` 1, "an unpublished copy that J.-B. Chabot lent him".** Labourt says only "Grâce à l'obligeance de M. Chabot, nous sommes en mesure d'adjoindre à ces textes un traité inédit de Babaï" (labourt1904 l.15764-15766). "Lent" adds a detail. Fix: "from an unpublished copy that J.-B. Chabot made available to him".

**B-M8 MINOR (item 7). Card `uncertain` 4, "J. Labourt puts Dadisho's death between 615 and 620".** The OCR line reads "Il mourut âgé de soixante-quinze ans, phone / 'entre 615 et 620" (labourt1904 l.17771-17772). A garbled word stands before "entre" and may be a hedge such as "probablement". Check the page image. If it is a hedge, write "J. Labourt puts Dadisho's death probably between 615 and 620", and adjust the records claim and contested side to match.

**Verdict: Babai the Great NOT CLEAR** (B-B1 to B-B5).

---

#### 3. Severinus of Noricum

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | PASS |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS |
| 5 | No role for a named witness | PASS ("his translator George W. Robinson" names him) |
| 6 | Partisan witness marked | PASS (n/a; hagiography marked) |
| 7 | Contested claims show both sides | minor (B-M11) |
| 8 | Common names have place | minor (B-M9) |
| 9 | One term for one thing | minor (B-M10) |
| 10 | Story, scene, disputes in place, length | PASS (322 words) |
| 11 | Readability | PASS (6.9 / 69.4) |
| 12 | Card order, caveat repeated | PASS |
| 13 | Audio tags | PASS |
| 14 | List line, Who test | PASS |

Checked and sound. The death scene and both quotations are verbatim (robinson1914 l.3709-3712, 3828-3837). The memoir from "the daily narrations of the elder brethren" is at l.294-296, and Primenius and "purest Latin stock" at l.395-452. The rest checked at: the coming after Attila's death (l.788-793); fasting, prayer and alms (l.864-865); the refused bishopric (l.1689-1691); Odoacer and "Go forth to Italy!" (l.1489-1523); Giso, the rebaptism and Feva's reverence (l.1531-1538); Joseph's bones (l.3583-3585); Onoulfus's order (l.3927-3928); Gelasius, Victor, Barbaria and the Lucullan castle (l.4037-4049); Paschasius's reply (l.4253-4260); Gregory's letter to Anthemius (mansi-10 l.23210-23229); Foulke's note after Waitz (l.2672-2677). On the dates the coordinator asked about, the brief and card are right. The year is Robinson's ("c. 482", table l.4863) and Waitz's, through Foulke ("He died A.D. 482", foulke1907 l.2674). Eugippius gives only the day. No held line gives Mommsen's own year for the death. Mommsen's held Chronica minora dates only the Life, "editam a. 511" (chronica-minora-liber-genealogus l.33502). The card tradition reads as the README says. The README's reason holds: Eugippius has him "in the confession of the Catholic faith" (l.796), and the Rugian rulers' Arianism is Robinson's conclusion (l.1305-1308). The placing in Early Benedictine / Italian Monasticism rests on his community's move to the Lucullan castle, which Gregory's letter attests. It is a census placing and makes no claim on the card.

**B-M9 MINOR (item 8). Brief l.1, "Severinus felt a pain in his side".** The subject's own common name has no place at first mention, and "Riverside Noricum" first comes in l.5. Pope Severinus and Severinus Boethius share the name. Fix: "On the fifth of January, Severinus of Noricum felt a pain in his side." (Post-fix: 324 words, FK 7.0, Flesch 69.0.)

**B-M10 MINOR (item 9). The card names the Rugian queen two ways.** `legacy.traces` 3 has "King Feletheus and Queen Gisa" (Paul's spellings, foulke1907 l.2656-2657). `uncertain` 4 has "Queen Giso" (Eugippius's, robinson1914 l.1532), and the brief says "King Feva". Fix, `legacy.traces` 3: "Paul the Deacon, writing the History of the Langobards, names his monastery in Noricum and his warnings to the Rugian king Feletheus and his wife, whom Paul calls Gisa, and says Naples keeps his remains."

**B-M11 MINOR (items 1, 7). Card `uncertain` 3 loosens Eugippius's clue and pins it to the wrong year.** It says "more than five years had passed when the grave was opened, after Odoacer's war on the Rugians, which Robinson dates to 487". Eugippius says "the sixth year of his burial had already passed" (l.3965-3966). The opening came when Onoulfus ordered the Romans out, after Fredericus's return, which Robinson dates "488 ?" (table l.4869-4876). The war of 487 came before that. Fix: "The year of his death. Eugippius gives the day only. The year 482 is Robinson's and Waitz's. Eugippius's own clue is relative. He says the sixth year since the burial had passed when the grave was opened, as the Romans left for Italy after Odoacer's war on the Rugians. Robinson dates the war to 487 and the removal, with a query, to 488."

**B-M12 MINOR (records). A held early reader of the Life is left out of the "second witness" note.** `absent_details` "A second independent witness" lists what the search finds. It leaves out the Anonymus Valesianus in Mommsen's Chronica minora, which quotes the Life on Odoacer's visit: "de quo ita invenitur in libris vitae beati Severini monachi intra Pannoniam" (`chronica-minora-liber-genealogus_mommsen1892.txt` l.40428-40445; also `prosper_chronica-minora-1-lat_mommsen1892.txt` l.40340-40357). It is not independent, and Mommsen says it cites the Life (l.33502). The absence stands. Fix: add to the note, "and the Anonymus Valesianus, which quotes the Life on Odoacer (chronica-minora mommsen1892 l.40428-40445)".

**B-M13 MINOR (README l.9). "The correction is logged in Open-Gaps."** `Build/Ministry/Features/Church-Family-Tree/Open-Gaps.md` has no entry on Severinus's placing, and this branch does not touch the file (`git log origin/main..HEAD -- .../Open-Gaps.md` is empty). Fix: append the numbered Open-Gaps entry the README promises (the batch 6 entry, with the scan correction "Severinus of Noricum: Early Benedictine / Italian Monasticism only; the Homoian placing came from the Rugians he lived among"), or until then reword to "The correction is to be logged in Open-Gaps with the batch 6 entry."

**Verdict: Severinus of Noricum CLEAR** (no blocking finding; B-M9 to B-M13 to apply).

---

#### 4. Batch 5 records correction: `henana-of-adiabene`, "A second witness to Babai's doctrinal charges"

The corrected note in `era3/batch5/records.json` reads in part: "Both held texts that state the charges are Babai's own: his De Unione, held in part as J. Labourt quotes it in French from an unpublished copy Chabot lent him (labourt1904 l.15763-15866; on Henana and the resurrection body, l.15816-15818), and his Life of George of Izla, held as the two passages Chabot gives in French (synodicon-orientale chabot1902 l.42081-42240)."

Cited lines:
- labourt1904 l.15763-15866. The De Unione introduction is at l.15764-15768 ("Grâce à l'obligeance de M. Chabot ... un traité inédit de Babaï sur l'Incarnation (De unione)"). l.15763 is the end of the preceding sentence, on the Passion of George and the 612 exposition. The first quoted passage ends at l.15866 ("en sorte qu'il n'y a pas deux Fils ou deux Fils du Très-Haut"). The range is right to within one line.
- labourt1904 l.15816-15818. Labourt's footnote: "D'après le traité De Unione, Henana admettait que le corps du Christ ressuscité et ceux des fidèles ... étaient [sphériques] (ms., p. 126)". The sentence runs on to l.15820 ("comme on le voit d'après l'anathème qui conclut le ch. xix"). It is a report by Labourt of De Unione, not a quotation. The note's "as J. Labourt quotes it" covers the passages; for this point "reports" is the exact word.
- chabot1902 l.42081-42240. Chabot's two passages, from "composée par saint Rabban Mar Babai" (l.42080-42081) through the monk's list of charges (l.42093-42104) and "Le sort et la fatalité sont cause de tout" (l.42113-42118), to the anathema on "Henana le chaldéen et l'hérétique" (l.42242). Right.

Is the note now true? The core claim holds. Every held text that states the fate and resurrection charges is Babai's own. I found no other held author who states them: Seert's "doctrines hérétiques" names none, and Timothy I, through Assemani, condemns Henana's exegesis, not these doctrines (assemani 3.1 l.14926-14935). But one clause is false.

**B-H1 BLOCKING (false absence, batch 5 records).** "His Life of George of Izla, held as the two passages Chabot gives in French". The Life is held whole in Oskar Braun's German (braun1915 l.12419 ff.). The charges stand there: "Er leugnet die Auferstehung der Leiber und (lehrt), daß es eine Erlösung nur für die Seelen gebe" (l.13355-13400). Georg Hoffmann's German extracts hold the same passage: "der dort sehr verbreiteten Haerese des Hannänä Hdhaijabhäja, welcher das Schicksal lehrt ... leugnet die Auferstehung der Leiber" (hoffmann1880 l.5596-5612). The batch 5 R1 review already named the Hoffmann extracts as "a second translation of Babai, not a second witness" (R1_review.md l.183). Exact replacement note: "None held. Both held texts that state the charges are Babai's own: his De Unione, held in part as J. Labourt quotes and reports it in French from an unpublished copy Chabot made available to him (labourt1904 l.15764-15866; on Henana and the resurrection body, l.15816-15820), and his Life of George of Izla, held whole in Oskar Braun's German (persian-martyr-acts bkv22 braun1915 l.12419 ff.; the charges at l.13355-13400), in Georg Hoffmann's German extracts (persian-martyr-acts hoffmann1880 l.5596-5612) and as the two passages Chabot gives in French (synodicon-orientale chabot1902 l.42080-42240). Babai's Evagrius commentary is cited by Braun and Labourt but not held; the Chronicle of Seert speaks of 'doctrines heretiques' without naming them."

**B-M14 MINOR (same note).** The same false "lent him" as B-M7 ("an unpublished copy Chabot lent him"). The replacement above already uses "made available to him".

---

### Verdicts

- John Moschus: **CLEAR** (0 blocking, 5 minor).
- Babai the Great: **NOT CLEAR** (5 blocking: B-B1 to B-B5; 3 minor).
- Severinus of Noricum: **CLEAR** (0 blocking, 5 minor).
- Batch 5 Henana records correction: **NOT YET TRUE** in one clause (B-H1 blocking, B-M14 minor).

## R1 review, part C: Constantius of Lyon, Faustus of Riez, Gennadius of Marseilles, Ruricius of Limoges (era 3 Who batch 6)

Reviewer: independent Opus, first sight of these drafts, full effort. Profiles: `constantius-of-lyon` (recorder), `faustus-of-riez`, `gennadius-of-marseilles` (recorder) and `ruricius-of-limoges`, all non-major, at most about 325 words. For each I read the brief, card, audio script and `records.json` entry, and the batch `README.md` sentences on these ids. Files are in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era3/batch6/`. Bar: `Who_Profile_Pattern.md` review checklist 1 to 14 and the standards it points to; `CLAUDE.md` "Trust and source fidelity" and "Accessible and rigorous"; the era 3 Who scan entry and the Who profile entries of 2026-11-12 to 2026-11-14 in `Decision-Log.md`. Brief line numbers refer to the `.brief.txt` files, where each paragraph is one line and blank lines count (paragraphs sit on l.1, 3, 5, 7, 9). Card line numbers refer to the `.card.json` files. Other line numbers point to files under `cic/texts/`.

Method. I re-checked every quotation and close telling in the four briefs, cards and records against the vendored file and lines cited, collapsing whitespace and reading the OCR by line (Engelbrecht's CSEL 21, Levison's MGH SRM 7 extract, Richardson's and Jackson's NPNF 2.3, Barralis 1613, Peiper's Avitus, Migne's PL 42, 65, 67, 83 and 100-101, Leo and Krusch's MGH AA 4, Arndt and Krusch's MGH SRM 1, Maassen's MGH Concilia 1, Bruns's Canones II, Wasserschleben's Regino, Warfield's NPNF 1.5, Mommsen's Chronica minora 1). I read each hit in context to see who speaks: the ancient author, a document he quotes, an editor's prolegomena, a note, an apparatus, an index or a corrigenda page. I checked every factual sentence of each brief against its passage. Before accepting any absence or "only" I searched the whole Library under OCR variants with whitespace-tolerant patterns: Riochatus (`[a-z]iochat|r.ochat|riocat`), Sidonius's letters (`Sidonius\s+(domino|Constantio|Ruricio|Fausto|Patienti)`, the opening of I.1, the Patiens verses of II.10), `Ruric|Roric|Kuric|Huric`, Agde (`Agath`), Gennadius with Massil- and Scholari-, and Constantius with Germanus. That search found three held lines the drafts do not use and that change what they say: Krusch's own reversal in the addenda of MGH SRM 1 (C-B1), Leo's index naming the grandson as the later council signer (R-M5), and the acts of Agde with their own year (R-M1). Truncation of the Levison file was checked by two independent methods (below). Readability came from `engine.m1.gates.grade_text`, run from the repo root, and every suggested brief fix was applied to a scratch copy in the session scratchpad and re-scored. I did not edit any profile file, made no paid or model-API calls and used no web.

#### Applies to all four

- **Audio = brief.** Each audio script equals its brief once `[calmly] ` and `[warmly] ` are removed (checked by script). Each opens with `[calmly]` and has one `[warmly]`, at the start of the closing paragraph. No tag appears in a brief or card. When a fix below changes a brief, the audio script follows it.
- **Readability.** All four pass now and after the fixes. Narrator sentences over 25 words are only the lead-ins to quotations and modern renderings, noted where the rendering itself runs long (C-M1).
- **Length.** The drafts run 324 to 331 words. Three are over the ~325 ceiling (Constantius 327, Faustus 331, Ruricius 328). The fixes below bring all four to 323 to 325; each re-scored figure is in the table.
- **Card order.** All four follow Mark's order; missing fields are absent; keyWorks never pass three; each `uncertain` list opens with the brief's own caveat.
- **Who test (item 14).** Constantius and Gennadius are recorders, per the README and the Palladius ruling. Faustus has his works held and a following (Ruricius, Sidonius's praise, the feast at Riez). Ruricius has two books of letters held. List lines belong to the map build and were not checked.
- **README.** Its sentences on these ids (order by best held date, Ruricius in Benjamin's place, Constantius and Gennadius as recorders at standard length, card traditions as the scan's placings) match the drafts and the supplement scan.

| Profile | Words | Est. @162 | FK | Flesch | After fixes |
|---|---|---|---|---|---|
| Constantius of Lyon | 327 | 2:01 | 8.2 | 65.4 | 323 words, 2:00, FK 8.0, Flesch 66.1 |
| Faustus of Riez | 331 | 2:03 | 8.5 | 62.4 | 324 words, 2:00, FK 8.1, Flesch 63.1 |
| Gennadius of Marseilles | 324 | 2:00 | 8.0 | 65.0 | 325 words, 2:00, FK 8.2, Flesch 64.0 |
| Ruricius of Limoges | 328 | 2:01 | 7.3 | 66.6 | 324 words, 2:00, FK 7.2, Flesch 67.3 |

---

#### 1. Constantius of Lyon (recorder)

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | FAIL, blocking (C-B1, card); minor (C-M4, C-M5, C-M6) |
| 2 | Quotes verbatim | PASS (no verbatim quote; the close is a modern rendering, see C-M1) |
| 3 | No invention | PASS |
| 4 | Reading aids | minor (C-M1 rendering length; C-M2 anachronism) |
| 5 | No role for a witness | PASS (Levison, Sidonius, Isidore, Krusch, Prosper named) |
| 6 | Partisan witness named and marked | PASS (none in play; Levison's judgment of the Life is his) |
| 7 | Contested both sides | FAIL, blocking (C-B1: Krusch's side is his superseded view) |
| 8 | Common names placed | PASS (Patiens of Lyon, Germanus bishop of Auxerre, Martin of Tours, Ennodius of Pavia, Adomnán of Iona) |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | minor (327 words; fixed by C-M1 and C-M2) |
| 11 | grade_text | PASS |
| 12 | Card order, caveat repeated | PASS ("His own life is thin" opens `uncertain`) |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS (recorder) |

**Quotes and close tellings** (`constantius-lyon_vita-germani_levison1920.txt` unless named)
- The verses (l.1): Levison l.371-373, "cum Patiens episcopus Lugduni ecclesiam aedificasset, versus hexametros composuit una cum carmine Secundini parietibus basilicae altari vicinis inscribendos", from Sidonius ep. II.10 (note 16, l.389). Faithful.
- Life (l.3): l.364-370, "virum Lugdunensem sive clericum sive absque ordinibus sacris vitae religiosae deditum amicum Sidonii, qui ei et singulas epistulas inscripsit et octo libros earum collectos dedicavit, quas ut ederet Constantius ei suaserat"; "c. a. 473 Arvernis in 'civica simultate' concordiae restituendae operam dedisset"; "persona aetate gravis … religione venerabilis"; l.391 "De ordinibus eius ecclesiasticis non constat". Faithful.
- The writing of the Life (l.5): letter to Patiens, l.1789-1791, "imperasti saepissime, ut vitam sancti Germani episcopi obumbratam silentio … traderem"; preface l.1965-1966, "tanta enim iam temporum fluxere curricula, ut obscurata per silentium vix colligatur agnitio"; letter to Censurius l.1880-1885, "ut pagina, quae adhuc intra secreti vicinia tenebatur, longius me auctore procederet essemque ipse reatus mei quodammodo et accusator et proditor"; Levison l.432, "Vitam c. 480. aut paulo post compositam". Faithful.
- Judgment (l.7): l.455-458 ("non tam biographi quam hagiographi munere fungens … miracula exigui momenti magnam partem operis efficiant aeque atque in Vita Martini a Sulpicio Severo composita, quam Constantio notam fuisse … demonstrant"); l.529-531 ("in tanta penuria testium minime omnino spernendum est; sed quamvis caute adhibendae sint"); l.587-589 (Bede, HE I.17-21, "magna ex parte ad verbum fere … descripsit"). Faithful.
- Close (l.9): l.4574-4579, "Ego duplicem veniam a te, lector, exposco, primum quod soloecismis et abiectione verborum aures tuas vulnero, deinde quod prolixior pagina videtur parare fastidium … Et tamen Deum testor conscium secretorum, me plura de domni mei Germani factis agnita et probata tacuisse". See C-M1.
- Card: Isidore, De vir. ill. 17, "Siquidem et Constantius episcopus Germani vitam contexuit" (`isidore-seville_…pl83…` l.121539-121540); Levison on Isidore's error and the Spanish codex (l.391-402, 583-584); Ennodius, Fortunatus, Adomnán (l.536-538, 585-587); Patiens 449 to before 494 (l.375-376, 1768-1770); Prosper and the synod (l.471-476, 505); the Alleluia victory (l.466-468); fifteen years packed (l.521). All faithful except uncertain 6 (C-B1).

**Truncation of `constantius-lyon_vita-germani_levison1920.txt`.** Confirmed by two independent methods. (1) Text end: the file's last bytes are "Et ideo in scribendo succinctum^" followed by a newline (l.4579-4580, checked with `od`); the sentence and the epilogue stop mid-clause, and p.283 carries no apparatus block, while every other page does (compare p.282, l.4513-4553). (2) Stated boundary: the header says the extract runs "through 'EXPLICIT VITA SANCTI GERMANI EPISCOPI' (p. 283)" (l.9); no such body line exists after the p.283 running head (l.4571), and the only "Explicit vita sancti Germani" in the file is a variant reading inside p.282's apparatus (l.4550). So the rest of the epilogue and its apparatus are missing. No claim leans on the missing text: the brief's close, the card and every records claim cite lines up to l.4579, and the rendered clause ("Deum testor … tacuisse") is complete in the file. The records already note the gap (`absent_details`, "The end of the Life"). See C-M7 for logging it.

**Tradition placing ("British and Welsh Christianity").** Checked, not raised as a finding. It is the supplement scan's placing (`Who_Scan_Supplement.md` l.150, "British and Welsh Christianity (Germanus's missions)") and matches Germanus of Auxerre's card (`era2/batch6/germanus-of-auxerre.card.json`). It is defensible for a recorder whose one work is the main source for the British missions and for Bede's account. A listener will see a man of Lyon placed in a British tradition; the card's `place` ("Lyon, in Gaul") and `knownFor` make the reason clear. If the coordinator wants him on the Gallic side too, Faustus's card shows the two-placing form ("Gallic Monastic-Ascetic Christianity; British and Welsh Christianity"). That is a coordinator's call, not a fault.

**Findings**

- **C-B1 BLOCKING (card `uncertain` 6, l.31; records `contested_claims` 1; items 1, 5, 7; a witness's superseded view told as his view).** The card says: "Bruno Krusch says Gregory copied a whole chapter of his Miracles of Julian word for word from it without naming it. Levison holds that Gregory did not know it." Krusch said that in his introduction (`gregory-tours_opera-mgh-srm-1-lat_arndt-krusch1885.txt` l.35826-35829), but in the Addenda et emendanda of the same volume, p.883, he reverses it: "De Vita S. Germani Autisiodorensis, quae Constantio vulgo attribuitur, vide quae p. 772 n. 6 scripsi. Iam nullus dubito, quin Vitae scriptor e Gregorio ipso hauserit" (l.66231, 66256-66257): I now have no doubt that the Life's writer drew on Gregory himself. The text Krusch compared was Duru's edition (his notes cite it by book, "lib. I, c. 7, Duru", l.44305-44306), which he calls "Pseudo-Constantius" (l.60038) and the Life "quae Constantio tribuitur" (l.58580-58581); Levison says the genuine text had been printed only by Mombritius, that the vulgate is a much-interpolated second Life, and that Krusch himself said so at that same p.883 ("Textum vulgatum interpolationibus refertum esse, monuerunt etiam B. Krusch, SS. R. Merov. I, 883", Levison l.659-660, 703-704). So the card sets up a dispute between Krusch and Levison that Krusch's own final word, in a held volume, does not support.
  Fix, card `uncertain` 6: "Whether Gregory of Tours knew the Life. In his introduction to Gregory's Miracles, Bruno Krusch says Gregory copied a whole chapter of his Miracles of Julian almost word for word from a Life of Germanus, which he cites in Duru's edition. In the additions at the end of the same volume he holds the reverse: the writer of that Life, which he calls the Life commonly given to Constantius, drew on Gregory. Wilhelm Levison holds that Gregory did not know Constantius's Life, since Gregory has Germanus die at Rome, where the Life has Ravenna, and he says the text then in print was a much-interpolated second Life." Records: side 1 of "Whether Gregory of Tours knew the Life of Germanus" becomes "Bruno Krusch, first: Gregory copied Virt. Iul. 29 almost word for word from the Life (gregory-tours arndt-krusch1885 l.35826-35829; note l.44305-44306, citing Duru's text); Krusch, later in the same volume: 'Iam nullus dubito, quin Vitae scriptor e Gregorio ipso hauserit', of the Life 'quae Constantio vulgo attribuitur' (l.66256-66257, p.883)"; and add to side 2 Levison l.659-660 and 703-704 on the interpolated vulgate text and Krusch's note at p.883.

- **C-M1 MINOR (brief l.9; items 2, 4; the rendering bar in `CLAUDE.md`).** "I call God, who knows all secrets, to witness that I have kept silent about many deeds of my lord Germanus that I knew and had proved." Three points. "All" is added: the Latin is "conscium secretorum", who knows secrets. "That I knew and had proved" makes Constantius the knower and prover, where "agnita et probata" is passive, deeds known and proved. And the rendering runs 27 words, past the ~25-word bar for a modern rendering. Fix: "Then he writes, in modern words, "I call God, who knows what is hidden, to witness that I have left out many deeds of my lord Germanus that were known and proved."" (rendering 25 words; Opus-authored per `CLAUDE.md`). Records: the epilogue claim notes the new rendering.

- **C-M2 MINOR (brief l.7; item 4, Style Guide 1.7 anachronism).** "Bede, in England, copied large parts of it". There was no England in Bede's day; his title names a people, the English. Fix: "Bede copied large parts of it almost word for word into his History of the English." (also holds the length).

- **C-M3 MINOR (item 10; length).** 327 words, over the ~325 ceiling. C-M1 and C-M2 bring it to 323. No other cut needed.

- **C-M4 MINOR (brief l.1; item 1).** "Sidonius Apollinaris, later bishop of Clermont." "Later" asserts that he became bishop after the church and verses, which no held line dates (Levison gives the letters "paulo post a. 470", l.1768-1769, about when Sidonius became bishop). Fix: "Sidonius Apollinaris, bishop of Clermont." Witness for the see: Gregory of Tours, HF II.23, tr. Dalton (`gregory-tours_history-of-the-franks-v2_dalton1927.txt` l.2963-2967), already in the records.

- **C-M5 MINOR (card `uncertain` 1, l.26, and 2, l.27; item 1).** Item 1 says "No source used here gives his family, his birth, his death or his orders", but item 2 then gives sources that do name his orders (manuscript headings, priest; Isidore, bishop), and the records' own search found two more that call him a priest: Rees, "Constantius, a priest of Lyons" (`rees_lives-of-the-cambro-british-saints-lat-eng_1853.txt` l.17717-17718), and an unsigned note in Migne's Marius Mercator, "Constantius presbyter" (`marius-mercator_opera-omnia-lat_migne-pl48.txt` l.20173). Fix, item 1: "No source used here gives his family, his birth or his death, and the sources disagree on his orders." Item 2, add after the manuscript headings: "W. J. Rees and an unsigned note in Migne's Marius Mercator also call him a priest."

- **C-M6 MINOR (card `knownFor`, l.3; item 1).** "the account of Germanus's life and journeys to Britain that Bede later copied". Bede copied chapters 12-16 and 25-27 (Levison l.587-589), not the account. Fix: "…the account of Germanus's life and journeys to Britain, parts of which Bede later copied."

- **C-M7 MINOR (records and tracking; `CLAUDE.md`, "Track gaps").** The truncation of the Levison file is recorded only in this profile's `absent_details` ("For the lead"). It is a Library defect that every future user of the file inherits. Fix: log it in Open-Gaps under this batch's entry ("Era 3 Who batch 6"), naming the file, the two checks above, the missing end of the epilogue and its apparatus on p.283, and the lead to re-extract p.283 from archive.org item `passionesvitaequesanctorum5`.

After the fixes: 323 words, 2:00, FK 8.0, Flesch 66.1.

---

#### 2. Faustus of Riez

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | FAIL, blocking (F-B1); minor (F-M4) |
| 2 | Quotes verbatim | PASS (Gennadius's English exact; Latin renderings marked "in modern words") |
| 3 | No invention | PASS |
| 4 | Reading aids | minor (F-M2, F-M3, F-M6) |
| 5 | No role for a witness | PASS (Engelbrecht, Avitus, Gennadius, Warfield, Sidonius named) |
| 6 | Partisan witness named and marked | PASS ("A Life of Fulgentius of Ruspe, hostile to Faustus") |
| 7 | Contested both sides | PASS (see below) |
| 8 | Common names placed | PASS (Faustus of Riez, Avitus of Vienne, Gennadius of Marseilles, Fulgentius of Ruspe, Caesarius of Arles, Ruricius of Limoges) |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | FAIL, minor (331 words; F-M1) |
| 11 | grade_text | PASS (Flesch 62.4, close to the floor; 63.1 after fixes) |
| 12 | Card order, caveat repeated | PASS ("The judgment on his teaching" opens `uncertain`) |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |

**The grace dispute.** Told in place with both sides named, and no label told as settled. The brief gives the hostile Life of Fulgentius (marked hostile; `fulgentius-ruspe_opera-contra-arianos-pl65-lat_migne1847.txt` l.9687-9693, "favens occulte Pelagianis, sed catholicus tamen volens videri"); Warfield's "chief champion" with the label as his ("what he names semi-Pelagianism"; `npnf105_augustine-anti-pelagian-writings.xml` l.954-956) and Orange 529 as his ("he says"; l.956-957, "so far as a formal condemnation could reach, semi-Pelagianism was suppressed"); Engelbrecht's denial (`faustus-riez_de-gratia-and-collected-works_engelbrecht1891.txt` l.652-667, "Faustum neque Semipelagianum fuisse neque a Caesario … habitum esse … hominis bona fide errantis verba"); the 534 treatise with its attribution to Caesarius as Engelbrecht's (l.659-662; fragment l.13805-13821); and Gennadius's praise. The card adds Isidore (`isidore-seville_…pl83…` l.122089-122092, "Pelagianae pravitati consentienti"), the Scythian monks and Hormisdas (l.590-606), Fulgentius's lost seven books (l.622-628), Ado on Avitus and Engelbrecht's answer (l.630-647). Orange 529 is not named in the brief as Caesarius's condemnation of Faustus, which the canons do not do (records `absent_details`, checked). Engelbrecht also reports Krusch's argument that Caesarius wrote nothing against Faustus (l.648-652); the brief does not need it.

**The Riochatus opening and Barralis.** The letter is Sidonius IX.9, held only in Barralis's 1613 print, but held twice there: once whole (`barralis_chronologia-sanctorum-insulae-lerinensis-lat_1613.txt` l.4712-4800) and once again with Barralis's hostile gloss (l.5510-5545). The two OCR passes of the same pages agree on every word the brief uses, and Engelbrecht's summary (l.566-572) and Hugh Williams's note in the Gildas volume ("Faustus sent two of his writings to Britain by the hands of a fellow-countryman, Riocatus … antistes ac monachus (Mon. Hist. Germ., viii, 157)", `gildas_de-excidio-britanniae-lorica-penitential-lat-eng_williams1899.txt` l.9659-9663) are two further witnesses. The opening can rest on it, told in modern words as the drafter does, once F-B1 is fixed. Barralis's gloss (Faustus hid the books from a bad conscience) is his, and is rightly not used.

**Is any Sidonius text truly not held?** No Sidonius edition is held, and no letter to Faustus other than IX.9 (Barralis). Some Sidonius letters are held in other books, none touching these four people: to Domnulus, Agroecius, Perpetuus and Euphronius in Mansi 7 (`mansi_sacrorum-conciliorum-collectio-tomus-7-451-492-lat_welter-facsimile1901.txt` l.99896-100197) and to Euphronius in the Acta Sanctorum (`acta-sanctorum_augusti-tomus-1-lat_1750.txt` l.40220). The records' "No Sidonius edition is held" stands. The card and records never claim more.

**Quotes and close tellings** (Engelbrecht unless named)
- Birth (l.3): Avitus, "ortu Britannum habitaculo Regiensem" (`avitus-vienne_opera-mgh-aa-6-2-lat_peiper1883.txt` l.7378-7379, OCR "Britauuum"). Lérins and 433: l.159, 229-240 ("itaque a. 433 Faustum abbatem Lerinensem factum esse constat"). Riez: Gennadius ch. LXXXVI (`npnf203…` l.43684-43686).
- Lucidus (l.5): retraction l.11205-11206, "qui dicit alios deputatos ad mortem, alios ad vitam praedestinatos"; Faustus l.11046-11048, "nos ergo per medium Christo duce gradientes post gratiam, sine qua nihil sumus, laborem officiosae servitutis adserimus" (rendered faithfully, marked "in modern words"); prologue l.3550-3567 (Leontius's council and mandate); l.3602-3604, "humanam … infirmitatem sine gratia sibi posse sufficere stulte credidit"; 474, l.555-562; Gennadius l.43693-43697, "that the grace of God always invites, precedes and helps our will" (exact).
- Close (l.9): exile l.322-350 ("neque improbabilis est coniectura virorum doctorum ab Eurico"); ep. 9 l.13401-13404, "sine sede propria possessores, sine possessione divites sumus" (faithful).
- Card: Regino/Gelasian list l.29717-29718 and Wasserschleben's note l.29638-29639 (exact); Engelbrecht on the interpolation l.582-589; De spiritu sancto l.427-434; Barralis's feast l.4535-4536; Maassen's Faustus of 549 (records). All faithful except `place` (F-M4).

**Findings**

- **F-B1 BLOCKING (brief l.1; records claim 1; item 1; the scene misreported).** "Unrest among the peoples kept him at Clermont, and there its bishop, Sidonius Apollinaris, read the books." The letter says the reverse of "there". While Riochatus stayed in the town he showed Sidonius Faustus's other gifts but hid the books: "sic reliqua dona vestra detexit, ut perurbane quae praestantiora portabat operuerit" (Barralis l.5539-5540, second print; first print l.4759-4760). Only after two months or more, when he had left, did Sidonius ride after him, catch him and read them: "post duos aut his amplius menses … pernicibus equis insecutus abeuntem … sarcinas solvo, quaesitum volumen invenio, produco, lectito, excerpo" (l.5540-5548; l.4762-4772). That pursuit is the scene of the letter, and the complaint that the books "brushed past his walls without a greeting" (l.4731-4732) is about the books being kept from him.
  Fix, brief l.1 (scored with F-M1 to F-M3 and F-M6): "Riochatus, a bishop and monk, was carrying books by Faustus of Riez to the Britons. Unrest among the peoples held him at Clermont, where he kept the books hidden. When he left, the bishop there, Sidonius Apollinaris, rode after him and read them. August Engelbrecht, who edited Faustus, takes them to be his work On Grace." Records claim 1: add "he hid the books during his stay ('quae praestantiora portabat operuerit'); after 'duos aut his amplius menses' Sidonius rode after him 'pernicibus equis', found the book and read it ('quaesitum volumen invenio, produco, lectito, excerpo')", with witness Barralis l.4759-4772 and l.5539-5548, and add Williams, Gildas volume, l.9659-9663, as a further witness to Riochatus and the books.

- **F-M1 MINOR (item 10; length).** 331 words, over the ~325 ceiling, and F-B1 adds words. Cuts, all scored: drop the "brushed past his walls" sentence (the pursuit carries the scene); l.3 "and then its abbot, from 433 by Engelbrecht's reckoning" becomes "and its abbot from 433, by Engelbrecht's reckoning", and "At last he became bishop of Riez in Gaul" becomes "Then he became bishop of Riez" (the card keeps "in Gaul"); l.5 "Lucidus's later retraction condemns the view" becomes "Lucidus later retracted the view"; "praised the books for teaching" becomes "praised them for teaching"; l.9 "he wrote to his friend Ruricius" becomes "he wrote to Ruricius".

- **F-M2 MINOR (brief l.7; items 4, 8; context).** "Benjamin Warfield calls Faustus…". Engelbrecht is introduced and Warfield is not, so a listener does not know who he is (Mark: "no statements that have no context"; the batch 5 C-M2 ruling on Dalton). The sentence also runs 23 words with a nested "which, he says". Fix: "The Princeton scholar Benjamin Warfield calls Faustus the chief champion of what he names semi-Pelagianism. He says the Council of Orange put it down in 529." Witness for Princeton: `npnf105…` l.516-519, "BENJAMIN B. WARFIELD, D.D., PROFESSOR IN THE THEOLOGICAL SEMINARY AT PRINCETON, N.J."

- **F-M3 MINOR (brief l.3; item 4, unearned word).** "At last he became bishop of Riez" carries a sense of long waiting that no source gives. Fixed in F-M1 ("Then").

- **F-M4 MINOR (card `place`, l.9; items 1, 7).** "Britain, where Avitus of Vienne says he was born" settles a point the card itself lists as uncertain (item 4) and the records as contested: Avitus says "a Briton by birth"; that this means the island is Engelbrecht's reading ("pro certo habemus", l.152-154), against others who place him in Brittany (l.146-150). Fix: "Britain, by August Engelbrecht's reading of Avitus of Vienne, who calls him a Briton by birth; the island monastery of Lérins; Riez, in Gaul, as its bishop".

- **F-M5 MINOR (records).** Claim 1 cites only Barralis's first print and Engelbrecht. Add the second print (l.5528-5548) and Williams (l.9659-9663), as in F-B1; this matters because the Barralis header asks for a second check before quoting.

- **F-M6 MINOR (brief l.9; item 4, doubled hedge).** "probably by the Gothic king Euric, Engelbrecht thinks". Fix: "by the Gothic king Euric, Engelbrecht thinks." Engelbrecht calls the guess "neque improbabilis" (l.324-325), and "thinks" carries that.

After the fixes: 324 words, 2:00, FK 8.1, Flesch 63.1.

---

#### 3. Gennadius of Marseilles (recorder)

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | PASS; card minor (G-M3) |
| 2 | Quotes verbatim | PASS (all Richardson's English, exact) |
| 3 | No invention | PASS |
| 4 | Reading aids | minor (G-M1, G-M2) |
| 5 | No role for a witness | PASS (Richardson, Jackson, Mommsen, Walafrid, Alcuin named) |
| 6 | Partisan witness named and marked | PASS (the Louvain theologians are given as an unsigned note's report, placing him in a party) |
| 7 | Contested both sides | PASS (the Augustine line, the "I Gennadius" notice, the Book of Church Dogmas, priest or bishop) |
| 8 | Common names placed | PASS (Proterius as bishop of Alexandria, Timothy Aelurus, Prosper of Aquitaine, John Cassian, Augustine of Hippo, Macarius the Egyptian, Gelasius bishop of Rome, Faustus of Riez) |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | PASS (324 words) |
| 11 | grade_text | PASS |
| 12 | Card order, caveat repeated | PASS ("His own life is thin" opens `uncertain`) |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS (recorder) |

**Quotes and close tellings** (`npnf203_theodoret-jerome-gennadius-rufinus.xml`)
- Timothy (l.1): ch. LXXIII, l.43441-43458, "when Proterius had been put to death by the Alexandrians, in response to popular clamour, willingly or unwillingly allowed himself to be made bishop by a single bishop … wrote a very persuasive book to the Emperor Leo … that Leo of Rome, pontiff of the city, and the synod of Chalcedon, and all the Western bishops were fundamentally Nestorians … This book of his for learning’s sake, I translated by request of the brethren into Latin and prefixed a caveat." Both quoted phrases exact. Richardson's apparatus (l.43458-43459) says Migne and Herding omit the sentence; the manuscripts he collated carry it, so telling it as Gennadius's is sound, and the card notes the omission.
- Life and dating (l.3): Richardson's introduction l.38471-38487 ("The bulk of the work at least was composed about 480"); the title page l.688 (Richardson translated Jerome and Gennadius); Evagrius ch. XI l.42324-42343 ("the intimate disciple of the above mentioned Macarius … This work I have, under instructions, translated into Latin"). Faithful.
- Semi-Pelagian view (l.5): l.38488-38491, "glimpses of his own—the semi-Pelagian—point of view"; Prosper ch. LXXXV l.43661-43669 (exact); the Augustine line and Richardson's note l.42851-42865, "This expression in the editions has been the ground of much comment on Gennadius’ Semi-pelagian bias, but it almost certainly does not represent the original form of the text" (faithful).
- The notice and 496 (l.7): ch. XCIX l.43968-43975 (exact; Richardson's endnote "Died 496."); Richardson's rejection of the notice "as by a later hand" l.38477-38479; Jackson's prolegomena l.3611-3612, "Gennadius, presbyter of Marseilles, who died in 496". Neither gives a reason for 496 in the held lines, and Gelasius's own note reads "Bishop 492, died 496" (l.43862); the brief and card rightly give the year as theirs and draw no inference from it.
- Close (l.9): ch. LXXXVI l.43711-43712 (exact).
- Card: PL 42 admonition l.97003-97058 (Walafrid, Ratramnus, the Padolirone codex, Platina, the Louvain censure); Alcuin l.5646-5650; Mommsen l.42784-42785; the Acta Sanctorum l.180635-180636. The Book of Church Dogmas is under "Their own words" as "ascribed to Gennadius", with the attribution dispute in keyWorks and `uncertain` 6; that labels it honestly.

**Findings**

- **G-M1 MINOR (brief l.5; item 4, clarity).** "Gennadius credits Prosper of Aquitaine with an unsigned book against works of John Cassian, "which the church of God finds salutary, but which he brands as injurious"." Heard aloud, "he" can be taken for Gennadius, and what "which" refers to is unclear, so the point (Gennadius sides with Cassian's works against Prosper) is lost. Fix, same word count, verbatim fragments: "Gennadius thinks Prosper of Aquitaine wrote an unsigned book against works of John Cassian. He says Prosper "brands as injurious" works "which the church of God finds salutary"." ("I regard as his also", l.43666, is "thinks … wrote".)

- **G-M2 MINOR (brief l.7; item 4, context).** "He and Blomfield Jackson, in the same volume, give 496 for his death." Jackson is not introduced, and "in the same volume" means nothing to a listener. Fix: "He and Blomfield Jackson, Theodoret's translator in the same volume, give 496 for his death." Witness: title page l.682-684. To hold length, l.5's last two sentences merge: "The line drew much comment on his bias, Richardson says, though it almost certainly does not go back to Gennadius."; and l.3 "Little more is known of his own life" becomes "Little more is known of his life".

- **G-M3 MINOR (card `uncertain` 2, l.35; item 1, witness form).** "The year 496 for his death is given in notes by Richardson and by Blomfield Jackson". Richardson's is an endnote; Jackson's is a sentence of his prolegomena to Theodoret (l.3611-3612), not a note. Fix: "The year 496 for his death is given in a note by Richardson and in Blomfield Jackson's prolegomena to Theodoret, in the same English volume, with no reason given in the lines used here."

- **G-M4 MINOR (card `sources`; item 12).** `uncertain` 2 cites the Acta Sanctorum, but no Acta Sanctorum entry is in `sources.about`. Add: `{"title": "Acta Sanctorum, March, volume 3", "author": "Bollandists", "date": "1865", "language": "Latin", "file": "cic/texts/acta-sanctorum_martii-tomus-3-lat-grc_palme1865.txt"}`.

- **G-M5 MINOR (records).** Card `uncertain` 8 names "the much later Gennadios Scholarios", but the records' namesake claim covers only the patriarch of ch. XC. Scholarios is held: add a namesake claim citing `gennadius-scholarius_opera-omnia-pg160-grc-lat_migne1866.txt` (its header and title), Documented.

After the fixes: 325 words, 2:00, FK 8.2, Flesch 64.0.

---

#### 4. Ruricius of Limoges

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | FAIL, blocking (R-B1); minor (R-M1, R-M6) |
| 2 | Quotes verbatim | PASS (all modern renderings, marked "in modern words", faithful) |
| 3 | No invention | PASS |
| 4 | Reading aids | minor (R-M3, R-M4) |
| 5 | No role for a witness | PASS (Engelbrecht, Caesarius, Fortunatus, Sidonius, Faustus named) |
| 6 | Partisan witness named and marked | PASS (none in play) |
| 7 | Contested both sides | minor (R-M2, one side of Caesarius's letter) |
| 8 | Common names placed | PASS (Caesarius of Arles, Verus bishop of Tours, Faustus of Riez, Venantius Fortunatus, Sidonius Apollinaris) |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | minor (328 words; R-M4) |
| 11 | grade_text | PASS |
| 12 | Card order, caveat repeated | PASS ("His life comes almost wholly from his letters" opens `uncertain`) |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |

**Quotes and close tellings** (Engelbrecht unless named)
- Agde (l.1): Caesarius to Ruricius l.24680-24694, "Dum nimium tribularetur animus meus, quare ad synodum vestram praesentiam non meruimus obtinere, sanctus et domnus meus Verus episcopus mihi dignatus est dicere, quod per suum diaconum mihi Agate vestras litteras destinasset, quas ego nescio quo casu aut qua neglegentia me non retineo suscepisse … dignissimum fuerat, ut personam dirigeretis, quae ad vicem vestram subscriberet"; Verus of Tours, l.2959-2960. Ruricius, ep. II.33, l.23184-23188, "fecit hoc infirmitas, non voluntas. ipsi etenim recolere potestis, quam fessum me Burdigala videritis et hoc hieme, quando esse soleo fortior solito". Faithful. A second witness ties II.33 to Agde: the Maurist prolegomenon in PL 67 (`facundus-ferrandus-caesarius-dionysius-pl67-lat_migne1865.txt` l.96512-96546).
- 485, the epitaph, the wedding (l.3): l.2901-2903 and 953-958; Fortunatus carm. IV.5 (`venantius-fortunatus_opera-mgh-aa-4-lat_leo-krusch1881.txt` l.8290-8311, "Ruricii gemini flores, quibus Aniciorum iuncta parentali culmine Roma fuit … hinc avus, inde nepos"); l.2850-2851, "Ruricio et Iberiae epithalamium confecit Sidonius". Faithful, but see R-M6.
- Faustus (l.5): l.2890-2893, "Fausto imprimis auctore"; ep. I.1 l.20027-20044, "Olim te … fama celeberrima praedicante cognovi … adhaesit, doctor eximie, anima mea post te" (Ps. 62:9, l.20046); l.20070-20074 (see R-B1); Faustus ep. 9 l.13409-13412, "hanc primam munificentiam domino largiente percepi, quod piissimus meus Ruricius post vitae huius iactationes ad portum religionis proram salutis … convertit". Faithful.
- Death and churches (l.7): l.2926-2974 ("non multo post eum diem supremum obiisse veri simile esse cum Kruschio statuimus"); Fortunatus l.8302-8303, "tempore quisque suo fundans pia templa patroni iste Augustini, condidit ille Petri". Faithful.
- Close (l.9): ep. II.33 l.23197-23200, "si aliis nomen urbium praestat auctoritas, nobis auctoritatem demere non debet urbis humilitas, siquidem multo melius multoque eminentius est civitatem de sacerdote, quam sacerdotem de civitate notescere"; Engelbrecht l.2904-2906, "civitas … exigua atque infirma". Faithful.
- The councils of 535 and 541: Maassen l.6019, 6050, 8139 ("Ruricius Deo propitio Lemouice civitatis episcopus"), 9442 (549, through the archdeacon Bantardus). See R-M5.

**Findings**

- **R-B1 BLOCKING (brief l.5; item 1; a metaphor told as fact).** "He asks Faustus to send him harsher food, fit for his sickness, in place of the sweet dishes sent so far." In the letter the food is Faustus's words. Ruricius asks that whenever Faustus waters "the dryness of my earth with the rain of your eloquence", he send "non … delicatos et dulces cibos, sed austeriores et aegritudini meae congruos" (l.20070-20074); the sickness is the wounds of his sins, which he wants cut, not soothed: "ne vulneribus meis gratior sit foventis dextera quam secantis" (l.20078-20079), with "peccatorum meorum vincula" and "spinas criminum" just before (l.20034, 20043). As drafted, a listener hears that a sick man asked for real food. Fix: "He asks that Faustus's letters be harsher food, fit for a sinner's sickness, in place of the sweet dishes sent so far." Records claim on ep. I.1: add "quoties dignati fueritis ariditatem terrae meae eloquentiae vestrae imbre perfundere" and "ne vulneribus meis gratior sit foventis dextera quam secantis" (l.20070-20072, 20078-20079).

- **R-M1 MINOR (brief l.1; card `uncertain` 2, l.31; records claim 3; items 1, 5; a documented date told as an editor's).** "in 506 by August Engelbrecht's date" and "the year 506 is Engelbrecht's". The year is in the council's own acts, which are held: Bruns gives the heading "habitum era 644 … Anno vicesimo secundo Alarici regis sub die tertio Idus Septembris", with "Messala v. c. consule" in other codices (`bruns_canones-apostolorum-et-conciliorum-pars-altera-lat_1839.txt` l.10481-10501), and Engelbrecht cites the same dating (l.2933-2934). Fix, brief: "Bishops of Gaul met at Agde under Caesarius of Arles, in 506, and Ruricius of Limoges did not come." (Engelbrecht's first name moves to l.3: "August Engelbrecht, who edited his letters…".) Card `uncertain` 2: "The council he missed. Caesarius's letter names Agde, whose acts date it to 506. August Engelbrecht and an unsigned prolegomenon in Migne's Caesarius tie Ruricius's answer, that infirmity kept him away, to that council; Jacques Basnage, as that prolegomenon reports, held that he stayed away on purpose, which it calls invented. Ruricius also missed the council of Toulouse planned for the next year, as Sedatus of Nîmes's letter shows." (PL 67 l.96546-96553, "Hinc commentita sunt, quae de causa huius absentiae scripsit Iacobus Basnage … ac si venire noluisset Ruricius, quia primatum … usurpabat Caesarius".) Records: retag the 506 claim Documented, with Bruns as witness; add the PL 67 claim and the Basnage side as a contested claim.

- **R-M2 MINOR (brief l.1; item 7; one side of a letter).** The brief tells Caesarius's reproach and not his pardon, so Ruricius's answer reads as a defence against blame Caesarius in fact withdrew: "Sed quia novi, quam sancto et frequenti ac pio desiderio interesse volueritis, omnibus fratribus vestris votum vestrum et sanctam voluntatem exposui, pro qua re nihil pietati vestrae vel potuimus vel debuimus inputare" (l.24713-24716). The PL 67 prolegomenon reads the letter the same way: "partim obiurgat, partim excusat Ruricium" (l.96517-96518). Fix: after "Ruricius should, he wrote, have sent someone to sign in his place." add "Yet he held nothing against him." and start a new paragraph at "Ruricius answered" (which also brings l.1 back to one idea per paragraph).

- **R-M3 MINOR (brief l.7; items 4, 5).** "Engelbrecht, with Bruno Krusch, thinks he died…". Krusch is not introduced anywhere in the brief. The judgment is stated by Engelbrecht ("cum Kruschio statuimus"), and the card keeps Krusch. Fix: "Engelbrecht thinks he died not long after 507, when he was too frail to reach a council at Toulouse."

- **R-M4 MINOR (brief l.1 and l.7; items 4, 10).** Length 328, over the ~325 ceiling; and l.1 ends on a choppy pair, "Ruricius reminded Caesarius that he had seen him worn out at Bordeaux. That was in winter, when Ruricius was usually stronger." Fixes: "Caesarius himself, he wrote, had seen him worn out at Bordeaux, and in winter, when he was usually stronger." ("ipsi etenim recolere potestis", l.23186-23187); l.7 "Fortunatus says each of the two Ruricii founded" becomes "Fortunatus says each Ruricius founded". With R-B1, R-M1, R-M2 and R-M3 the brief is 324 words.

- **R-M5 MINOR (card `uncertain` 5, l.34; records `absent_details` 1; a held identification missed).** "A Ruricius signs at councils of 535 and 541 in Friedrich Maassen's edition; he cannot be this man if Engelbrecht's reckoning of his death is right." This leaves an open puzzle that a held line settles: Leo's index to Fortunatus names the signer as the grandson, "alter nepos illius interfuit concilio Arverno I. a. 535, Aurelianensi IV. a. 541, V. a. 549 per Bantaredum archidiaconum subscripsit" (`venantius-fortunatus_opera-mgh-aa-4-lat_leo-krusch1881.txt` l.53125-53130, "alter nepos" at l.53128), and gives the elder's death as "c. a. 507" (l.53126, OCR "51)7"). The records' search for "Huric-" missed this index line. Fix: "Which Ruricius. His grandson, also named Ruricius, was later bishop of Limoges too, by Venantius Fortunatus's epitaph. The index to Fortunatus's works in the Monumenta edition names the grandson as the Ruricius who signs at the councils of Clermont in 535 and Orléans in 541, and through his archdeacon at Orléans in 549, which Friedrich Maassen's edition prints." Records: add the claim with witness Leo l.53125-53130 and Maassen l.6019, 8139, 9442, and correct `absent_details` 1.

- **R-M6 MINOR (card `dates`, l.8, and `uncertain` 1, l.30; item 1).** The 485 rests on more than "a letter Faustus wrote soon after returning from exile". That letter shows only that Ruricius was newly bishop when Faustus had newly come home (l.957-959). The year is Engelbrecht's year for Faustus's return, which is itself conditional: "Quodsi Euricus in causa fuit, ut Faustus a. 477 in exsilium pelleretur, illo demum mortuo i. e. anno 485 in patriam hunc rediisse veri simile est" (l.348-350). Fix, `uncertain` 1: "…The year 485 for his election rests on Engelbrecht's reading of a letter Faustus wrote soon after returning from exile, to Ruricius newly made bishop, and on his guess that Faustus came home in 485, when King Euric died, if Euric had exiled him." The brief's "dates his election to 485 from one of Faustus's letters" may stand, since it gives the year as Engelbrecht's.

- **R-M7 MINOR (card `otherNames`, l.5; Naming rule).** "Ruricius the elder" is not a form any vendored source spells; the sources say "avus" (Fortunatus), "Ruricius noster" against "Ruricio iuniori" (Engelbrecht l.2975) and "alterum" (Leo). Fix: drop it, or replace it with a spelled form, "Ruricius Lemovicensis episcopus" being already covered by the first entry.

After the fixes: 324 words, 2:00, FK 7.2, Flesch 67.3.

---

#### Verdicts

- Constantius of Lyon: NOT CLEAR (1 blocking, 7 minor).
- Faustus of Riez: NOT CLEAR (1 blocking, 6 minor).
- Gennadius of Marseilles: CLEAR on blocking points, with 5 minor findings to apply (NOT CLEAR until they are applied and rechecked).
- Ruricius of Limoges: NOT CLEAR (1 blocking, 7 minor).
