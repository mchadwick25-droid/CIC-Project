# R1 review: eight Who profiles (Church Family Tree)

Reviewer: independent, first sight of these drafts. Bar: `Who_Profile_Pattern.md` review checklist 1 to 14, and `CLAUDE.md` "Trust and source fidelity" and "Accessible and rigorous". I did not edit the drafts. I made no paid calls.

Method. Every quotation in the briefs and cards was grepped in the vendored file and read in context, notes included. Readability came from `engine.m1.gates.grade_text`, run locally (no model call). Length assumes 160 words a minute. Line numbers point to the vendored files under `cic/texts/`.

Applies to all eight:
- The audio scripts match the briefs word for word once tags are removed. Each opens with `[calmly]`, and `[warmly]` sits before the closing line. No tags appear in the briefs or cards. Item 13 passes everywhere.
- `grade_text` passes for all eight (FK at most 10, Flesch at least 60). Five briefs score below FK 8 (Ignatius 6.7, Josephus 7.0, Marcion 7.0, Justin 7.3, Hermas 7.4). The pattern makes 8 a floor and not a target, and none of them reads as choppy, so this is noted and not raised as a finding.
- No card has a "links on the map" field. A missing field is left absent, which is correct.
- Item 14 (the list line). The drafts do not carry list lines. I checked `cft-website/index.html`: seven of the eight names appear in tradition or people lists. Josephus does not appear there (see Josephus M9). Every subject passes the Who test.

| Profile | Words | Est. length | FK | Flesch |
|---|---|---|---|---|
| Josephus | 412 | 2:34 | 7.0 | 70.0 |
| Ignatius of Antioch | 408 | 2:33 | 6.7 | 72.4 |
| Marcion of Sinope | 411 | 2:34 | 7.0 | 69.1 |
| Justin Martyr | 432 | 2:42 | 7.3 | 66.0 |
| Clement of Alexandria | 407 | 2:33 | 8.0 | 63.6 |
| Eusebius of Caesarea | 444 | 2:46 | 9.4 | 60.8 |
| Hermas (not major) | 342 | **2:08** | 7.4 | 70.7 |
| Valentinus (not major) | 323 | 2:01 | 8.6 | 62.1 |

---

## 1. Josephus (Outside witness)

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | FAIL (B1, B3, B4) |
| 2 | Quotes verbatim | PASS in the brief. The card's quote is in the wrong scope (B4) |
| 3 | No invention | PASS |
| 4 | Reading aids | FAIL (B2: tail and status close) |
| 5 | No role standing in for a witness | PASS |
| 6 | Partisan witness marked | n/a. He is an outside witness. Origen and Eusebius are named for what they report |
| 7 | Contested shown both sides | PASS. The Testimonium is given with several named views |
| 8 | Common names | PASS (Origen, Eusebius of Caesarea, Titus, Ananus all placed) |
| 9 | One term | MINOR drift (M6) |
| 10 | Story, scene, in-place disputes, length | PASS (major figure) |
| 11 | grade_text | PASS |
| 12 | Card order and caveat repeated | PASS. The label's position is noted at M8 |
| 13 | Audio tags | PASS |
| 14 | List line; outside witness is an objective historian | PASS on the label. List line unverified (M9) |

**Quotes**
- "the brother of Jesus, who was called Christ, whose name was James": exact (Whiston OCR l.91003–91009, across a line-end hyphen).
- "so-called Christ": exact (McGiffert, npnf201 l.13608, italic *so-called*).
- "if indeed it be proper to call him a man": exact (Eusebius HE I.11, npnf201 l.9229–9230).
- "He was the Christ": exact (npnf201 l.9232).
- "did not accept Jesus as Christ": exact (Origen, Comm. Matt. X.17, anf09 l.30628).
- Card: "He was the Christ": exact. "who was called Christ" (attributed to McGiffert's note): see B4.

**Findings**
- **B1 BLOCKING.** Card, What is uncertain: "His meeting with Vespasian, and the prediction that he would rule, are known only from Josephus himself." This is false against the Library. Suetonius, *Vespasian* 5 (`suetonius_lives-of-the-twelve-caesars_thomson-forester1909.txt` l.14840–14842) reports it: "when Josephus, one of the noble prisoners, was put in chains, he confidently affirmed that he should be released ... by the same Vespasian, but he would be emperor first." The records.json tag (Inferential-Thin, "his own account only") rests on the same error. Rewrite the line and re-tag: Josephus and Suetonius both report it.
- **B2 BLOCKING.** The closing paragraph reads "How much of it Josephus wrote is still argued. [warmly] McGiffert, who thought it was added, still trusted the short line about James." The second sentence repeats what the third paragraph already said, so it is a tail with a beat and no new fact (item 4). "Still argued" makes a present-day claim, but the newest witness in the profile is McGiffert in 1890. Either name the witness and time ("in McGiffert's day, in 1890, it was argued four ways") or end on a sourced fact. The card's first uncertain line has the same "is still argued".
- **B3 BLOCKING.** "McGiffert names scholars for each view." He does not. For view (1), "entirely genuine", he names no one and calls it "absolutely untenable" (npnf201 l.9186–9188). The brief also gives three views and leaves out Ewald's fourth. It then puts William Whiston in the "genuine" slot as if McGiffert had cited him. Write "McGiffert sets out four views" and attribute Whiston on his own.
- **B4 BLOCKING.** Card: "McGiffert notes that some critics doubted the words 'who was called Christ' in the James passage." McGiffert's bracket (npnf201 l.13594–13604) takes in the whole identification, [τὸν ἀδελφὸν Ἰησοῦ τοῦ χριστοῦ λεγομένου, Ἰάκωβος ὄνομα αὐτῷ, καί], so the doubted words are "the brother of Jesus, the so-called Christ, James by name". He also does not use the wording "who was called Christ", which is Whiston's. The doubt's scope is stated wrongly, and a quotation is credited to the wrong translator.
- **M1 MINOR.** "Eusebius is the first writer known to quote the passage" (brief), and the card's "He is the first writer known to do so", state McGiffert's judgment (npnf201 l.9208) without naming him.
- **M2 MINOR.** "the high priest Ananus had a man stoned": Josephus says James "and some others" were delivered to be stoned (Whiston l.91009–91012; npnf201 l.13594).
- **M3 MINOR.** "He asked for the freedom of his family, and for the holy books." Josephus asked for his family. He "had also the holy books by Titus's concession" (Whiston l.5359–5365), and the Life does not say he asked for them. The same passage gives his brother and fifty friends, who could stand in place of the books.
- **M4 MINOR.** Card dates, "died about 100". McGiffert says he "lived in prosperity there until early in the second century", and the Life was "written after the year 100" (npnf201 l.15882, 15900–15901). Prefer "died early in the second century".
- **M5 MINOR.** Card legacy, remembered: "Origen, more than a century later ..." This is accurate. Note that the line Origen quotes from Josephus, that the city fell because of James, is not in our Antiquities text. Whiston discusses this. Worth a clause in What is uncertain if the card keeps the Origen line.
- **M6 MINOR.** Item 9. The third paragraph quotes Whiston's "who was called Christ" and then McGiffert's "so-called Christ" for the same Greek, without saying these are two translations.
- **M7 MINOR.** The opening sentence runs to 29 words and the James sentence to 27.
- **M8 MINOR.** The pattern puts the label "beside the role". The card JSON places `label` above `knownFor`, far from `role`. This depends on rendering, so check the page.
- **M9 MINOR.** No Josephus list line appears in `cft-website/index.html`. Confirm the outside-witness list line exists wherever outside witnesses are listed (item 14).

---

## 2. Ignatius of Antioch

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | FAIL (B1) |
| 2 | Quotes verbatim | FAIL (B2) |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS, with minor signposts (M5) |
| 5 | No role for a witness | PASS |
| 6 | Partisan witness marked | n/a. No hostile witness is used |
| 7 | Contested shown both sides | FAIL (B1: the letters dispute stops at one side's last word) |
| 8 | Common names | PASS (Polycarp of Smyrna, Eusebius of Caesarea, Irenaeus of Lyon) |
| 9 | One term | PASS |
| 10 | Story, scene, length | PASS (major) |
| 11 | grade_text | PASS |
| 12 | Card order and caveat | PASS |
| 13 | Audio tags | PASS |
| 14 | List line, Who | PASS |

**Quotes**
- "From Syria even unto Rome I fight with beasts," ... "being bound to ten leopards, I mean a band of soldiers": NOT exact as joined. See B2 (anf01 l.7082–7087).
- "I am the wheat of God," ... "and let me be ground by the teeth of the wild beasts, that I may be found the pure bread of Christ": exact (anf01 l.7040–7042, shorter Greek Romans 4).
- "the blessed Ignatius": exact (Polycarp, Phil. 9, anf01 l.3487).
- "But if these things were done by our Lord only in appearance," ... "then am I also only in appearance bound": exact (Smyrn. 4, anf01 l.8102–8103).
- "Let no man do anything connected with the Church without the bishop": exact (Smyrn. 8, anf01 l.8277–8278).
- "wherever Jesus Christ is, there is the Catholic Church": exact (anf01 l.8285–8286).
- "one of our people": exact in Eusebius HE III.36.12 (npnf201 l.20068). See M1.
- Card: "is still celebrated by a great many": exact (npnf201 l.19742). Card quotes as above: exact.

**Findings**
- **B1 BLOCKING.** The letters dispute ends with "Then in 1845 William Cureton published a Syriac version of just three letters, and argued that these alone were what Ignatius wrote." Cureton is left with the last word. McGiffert, the profile's own named witness (npnf201 l.19836–19849), says that "the defense of the genuineness of the latter [shorter Greek] by Zahn and Lightfoot may be regarded as finally settling the matter" against the Syriac, and that "candid scholars almost unanimously admit that the question is settled". The ANF editors (anf01 intro, l.4353 ff.) wrote earlier that "the Ignatian controversy is not yet settled". The brief and card should give this outcome with its names. The card's dispute line ends on Bunsen and Hefele. The records.json contested_claim lists Pearson, Daillé and Cureton but not Zahn and Lightfoot.
- **B2 BLOCKING.** The Romans quote is split by "he wrote", which hides an unmarked omission. The source reads "From Syria even unto Rome I fight with beasts, both by land and sea, both by night and day, being bound to ten leopards" (anf01 l.7082–7087). Either restore the words or end the first quote at "beasts" and paraphrase the rest.
- **M1 MINOR.** "one of our people" is McGiffert's rendering of Irenaeus inside Eusebius HE III.36.12. The vendored Irenaeus (anf01 l.53556–53560, Adv. Haer. V.28.4) reads "a certain man of ours" and "wheat of Christ ... bread of God". The attribution to Irenaeus stands. The card should list Eusebius III.36 as the source of the wording.
- **M2 MINOR.** "Almost everything known of him comes from those letters" (brief), and the card's "Eusebius ... adds only that ...", are McGiffert's analysis (npnf201 l.19780–19790, 19812–19815) presented without his name.
- **M3 MINOR.** Card knownFor, "among the earliest Christian writings after the New Testament", is unattributed modern judgment. keyWorks, "first use of the phrase 'Catholic Church'", is Coxe's claim with no name at that point (it is attributed in Legacy).
- **M4 MINOR.** "At Smyrna, where Polycarp of Smyrna was bishop": the place is said twice. "where Polycarp was bishop" is enough.
- **M5 MINOR.** "The letters became a long dispute." and "The year of his death is disputed too." are paragraph openers that announce a dispute before telling it. The same formula recurs in Hermas and Josephus.

---

## 3. Marcion of Sinope (hostile-witness founder)

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | FAIL (B1) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | FAIL (B2: context-free close, "Even" beat). M4 is minor |
| 5 | No role for a witness | PASS |
| 6 | Hostile witness named; two for the teaching | PASS on the teaching (Justin, Irenaeus, Tertullian). FAIL on separating single-witness life material (B1) |
| 7 | Contested both sides | FAIL (B1). M1 is minor |
| 8 | Common names | PASS |
| 9 | One term | PASS |
| 10 | Story, scene, length | PASS (major) |
| 11 | grade_text | PASS |
| 12 | Card order and caveat | PASS |
| 13 | Audio tags | PASS |
| 14 | List line, Who | PASS (listed in `cft-website/index.html` l.34931) |

**Quotes**
- "instructed by apostles": exact (Irenaeus III.3.4, anf01 l.39858).
- "Dost thou know me?" / "I do know thee, the first-born of Satan.": exact (anf01 l.39883–39884).
- "to believe in some other god greater than the Creator": exact (Justin, 1 Apol. 26, anf01 l.14945–14946).
- "that shipmaster of Pontus": exact (Tertullian, Praescr. 30, anf03 l.21331–21332).
- "the author of evils": exact (Irenaeus I.27.2, anf01 l.33575).
- "Marcion's special and principal work is the separation of the law and the gospel.": exact (Adv. Marc. I.19, anf03 l.23735–23736).
- "as if he alone knew the truth": exact (1 Apol. 58, anf01 l.16135).
- "Even wasps make combs; so also these Marcionites make churches.": exact once the translator's note is stripped (Adv. Marc. IV.5, anf03 l.29328–29330).
- "in the first warmth of faith": exact (Adv. Marc. IV.4, anf03 l.29239–29240).
- Card: "of every nation": exact (anf01 l.14946). "the first-born of Satan": exact.

**Findings**
- **B1 BLOCKING.** "One more story rests on a single late witness." The card goes further: "Only Epiphanius of Salamis ... says he came from Sinope, was a bishop's son, and was put out by his father for seducing a young woman." Only the Sinope detail is single-witness. Pseudo-Tertullian, *Against All Heresies* 6 (anf03 l.55757–55765), has Marcion as "son of a bishop, excommunicated because of a rape committed on a certain virgin". Holl's own apparatus, on the page the brief cites (Holl Panarion l.7498–7500), names Ps.-Tertullian and quotes "episcopi filius propter stuprum cuiusdam virginis". The Coxe note in anf03 argues the detail is early. So "teaching two, life one" is misapplied here, and the life detail has two witnesses. Rewrite the brief's frame and the card line, and give the records.json contested_claim both named sides. Holl also says the silence of Tertullian argues against the story (see B2).
- **B2 BLOCKING.** The closing line "[warmly] Even Tertullian granted that Marcion gave his money to the church 'in the first warmth of faith.'" is a statement with no context (item 4). It hints at an argument against Epiphanius's story without saying so. "Even" adds a rhetorical beat. The argument belongs to Karl Holl, who says the silence of Tertullian, and his calling Marcion "sanctissimus" in Praescr. 30, speak against the story's credibility (Holl l.7503–7504; anf03 l.21361 renders it "most abstemious"). Name Holl and say what he argues, or close on something else.
- **M1 MINOR.** "he was teaching at Rome in the middle of the second century" is told plainly. Tertullian puts him "under the episcopate of the blessed Eleutherus" (anf03 l.21336–21337), and the card and records.json mark this as Contested. Justin and Irenaeus do support mid-century, so a short clause in place would do.
- **M2 MINOR.** "Justin, Irenaeus and Tertullian all say he taught two gods. ... The other was a higher, good God, unknown until Jesus came." Justin says "some other god greater than the Creator" (anf01 l.14945). "Good" and "unknown" come from Irenaeus and Tertullian. Give the details to their owners.
- **M3 MINOR.** The display name "Marcion of Sinope" (card name, and the identifier used in the Valentinus brief) rests on the one detail the profile calls single-witness. Justin and Irenaeus give "Marcion of Pontus". This is a census naming call to flag, not to change here.
- **M4 MINOR.** "Tertullian puts it in one line:" is a colon build-up before the quote.
- **M5 MINOR.** records.json tags direct single-witness reports Inferential-Thin: shipmaster and money (Tertullian), Polycarp's words (Irenaeus). These are attested reports from one partisan witness, not inferences. Documented with a note, or Widely Accepted, fits the five-level vocabulary better.

---

## 4. Justin Martyr

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | PASS |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS |
| 5 | No role for a witness | PASS ("Dods, who translated it" and McGiffert are named) |
| 6 | Partisan witness marked | PASS (Crescens known only from his enemies, McGiffert named) |
| 7 | Contested both sides | PASS (Crescens; date) |
| 8 | Common names | PASS with minor points (M1, M2) |
| 9 | One term | PASS |
| 10 | Story, scene, length | PASS (major) |
| 11 | grade_text | PASS |
| 12 | Card order and caveat | PASS. Caveat order is minor (M4) |
| 13 | Audio tags | PASS |
| 14 | List line, Who | PASS |

**Quotes**
- "above one Martinus, at the Timiotinian Bath": exact (anf01 l.29309).
- "Are you not, then, a Christian?" / "Yes, I am a Christian.": exact (l.29313–29314).
- "wings": exact ("furnished my mind with wings", Dial. 2, l.17453).
- "But straightway a flame was kindled in my soul": exact (l.17852–17853).
- "Thus, and for this reason, I am a philosopher.": exact (l.17856–17857).
- "those who lived reasonably are Christians, even though they have been thought atheists": exact once the translator's note at l.15686 is stripped (1 Apol. 46).
- "plotted against and fixed to the stake": exact (2 Apol. 3, l.16850).
- "his bitterest enemies": exact (McGiffert, npnf201 l.23786–23787).
- "I do not suppose it," ... "but I know and am fully persuaded of it.": exact (l.29373–29374).
- Card: "a genuine lover of the true philosophy": exact (Eusebius HE IV.8, npnf201 l.21865).

**Findings**
- **M1 MINOR.** The brief's first mention is "a teacher named Justin", and the record's epithet "Justin Martyr" never appears in the brief. "In Rome" in the same sentence does identify him, but using the epithet once would meet the naming rule fully.
- **M2 MINOR.** "the Greek thinkers Socrates and Heraclitus" uses a role where the pattern asks for name-of-place ("Socrates of Athens") at first mention.
- **M3 MINOR.** Card legacy: "The account of his trial ... was kept and read as the Martyrdom of Justin." Nothing vendored establishes "read".
- **M4 MINOR.** The card's What is uncertain opens with the trial account's unknown date and author, which the brief never raises. The pattern asks it to open with the brief's own caveat (Crescens, then the date).
- **M5 MINOR.** "They were, in McGiffert's words, 'his bitterest enemies.'" In McGiffert "his" means Crescens. In the brief "his" follows "Justin and Justin's pupil Tatian", so it may be heard as Justin's. Write "Crescens's bitterest enemies".

No blocking findings.

---

## 5. Clement of Alexandria

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | FAIL (B1, B2) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS (M1 is an overreach in wording) |
| 4 | Reading aids | FAIL ("Why Clement had left Alexandria is not recorded" ends a limit on a bare why, and it is misleading: B1) |
| 5 | No role for a witness | PASS |
| 6 | Partisan witness marked | n/a |
| 7 | Contested both sides | FAIL (B1: the evidence is turned against itself) |
| 8 | Common names | PASS (Clement of Rome, Alexander of Jerusalem). "Jerome" is minor (M5) |
| 9 | One term | PASS |
| 10 | Story, scene, length | PASS (major) |
| 11 | grade_text | PASS (FK 8.0) |
| 12 | Card order and caveat | PASS |
| 13 | Audio tags | PASS |
| 14 | List line, Who | PASS |

**Quotes**
- "Having tracked him out concealed in Egypt," ... "I found rest.": exact (Strom. I.1, anf02 l.27492).
- "the Sicilian bee": exact (l.27493).
- "the blessed presbyter, a man virtuous and approved": exact (Eusebius HE VI.11.6, npnf201 l.33614).
- "Gnostic Notes on the True Philosophy": exact in Eusebius HE VI.13.1 (npnf201 l.33870–33871), where Eusebius reports the title. Clement's own wording is "gnostic notes, according to the true philosophy" (anf02 l.31484).
- "Philosophy, therefore, was a preparation," ... "paving the way for him who is perfected in Christ.": exact (Strom. I.5, anf02 l.27893–27895).
- "gnostic": present.
- "the simple": exact (Strom. II.3, anf02 l.32107).
- "and the second, that from faith to knowledge": exact (Strom. VII.10, anf02 l.51356).
- "against old age, as a remedy against forgetfulness": exact (anf02 l.27478–27479).
- Card quotes: exact as above.

**Findings**
- **B1 BLOCKING.** "Why Clement had left Alexandria is not recorded. ... Eusebius, telling of that persecution, does not name Clement among those driven away." The card adds "so this is an inference". Eusebius VI.3.1 says "there was no one at Alexandria to give instruction in the faith, as all were driven away by the threat of persecution" (npnf201 l.32671–32673). McGiffert cites exactly this line as the cause of Clement's leaving (VI.6 note, l.33030–33034), and adds that Alexander's letters clear him of cowardice. Eusebius's statement is general, so it covers the head of the school. The brief presents it as silence that tells against McGiffert. That misleads. Say that Eusebius writes all the teachers were driven out and that McGiffert, reading this, dates Clement's leaving to 202.
- **B2 BLOCKING.** Card, What is uncertain: "Little of his life is known beyond his own books, two notices in Eusebius of Caesarea and one in Jerome." Eusebius treats Clement in V.11, VI.6, VI.11, VI.13 and VI.14. The card's own Sources list five chapters. The count is wrong.
- **M1 MINOR.** "Clement of Alexandria travelled far to find his teachers." Clement names teachers in Greece, Magna Graecia, the East and Egypt, and says he "tracked out" the last. That he travelled is a reasonable reading but not his words. Something like "Clement learned from teachers across the Greek world" stays within the source.
- **M2 MINOR.** "There he says philosophy was given to the Greeks as the law was given to the Hebrews". Clement writes "Perchance, too, philosophy was given to the Greeks directly and primarily" (anf02 l.27890). His own hedge is dropped.
- **M3 MINOR.** "Clement used the word 'gnostic' ... That put him at odds with the followers of Valentinus" claims a cause the source does not give. Strom. II.3 shows the quarrel was over faith against knowledge and who is saved by nature, not over the word itself.
- **M4 MINOR.** records.json tags the 202 departure Inferential-Thin. It is McGiffert's reconstruction from Eusebius VI.3, so Dominant Modern Reconstruction (McGiffert) fits better.
- **M5 MINOR.** "Jerome" appears without an identifier in the brief and card (also in Hermas). npnf203 gives a place once ("Strido"). Use it, or log the gap as the pattern asks.

---

## 6. Eusebius of Caesarea

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | PASS |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS ("rose in anger" is McGiffert's, l.1525) |
| 4 | Reading aids | PASS, with minor points (M2, M3) |
| 5 | No role for a witness | PASS |
| 6 | Partisan witness marked | FAIL (B1) |
| 7 | Contested both sides | PASS (Potamo; acceptance of the Nicene wording) |
| 8 | Common names | PASS (Socrates of Constantinople, Eustathius of Antioch, Athanasius of Alexandria, Epiphanius of Salamis). Heraclea is minor (M1) |
| 9 | One term | PASS |
| 10 | Story, scene, length | PASS (major) |
| 11 | grade_text | PASS (Flesch 60.8, close to the line) |
| 12 | Card order and caveat | PASS |
| 13 | Audio tags | PASS |
| 14 | List line, Who | PASS (recorder) |

**Quotes**
- "We, also being on the spot ourselves," ... "have observed large crowds in one day.": exact (HE VIII.9.4, npnf201 l.44268–44269).
- "the murderous sword was blunted": exact (l.44270–44271).
- "Since I am the first to enter upon the subject," ... "I am attempting to traverse as it were a lonely and untrodden path.": exact (HE I.1.3, l.6936–6937).
- "Conquer by this.": exact (VC I.28, l.61206).
- "One-in-essence": exact (npnf204 l.19660).
- "we did not let it pass without inquiry": exact (npnf204 l.19699–19700; npnf201 l.2122).
- "accused of sacrificing": exact (McGiffert, npnf201 l.1544–1545).
- "treating what he has said as an authority": exact (Socrates I.8, npnf202 l.2869).
- Card: "accused of sacrificing": exact.

**Findings**
- **B1 BLOCKING.** Item 6. Epiphanius of Salamis is the only source for the Potamo scene, and he is not marked as partisan. In the same passage he describes the judges at Tyre, Eusebius among them, as men "qui omnes in Arianorum inanissimum dogma propensiores erant" (Oehler l.44540–44541). He writes some forty years later and takes Athanasius's side. The charge itself is rightly marked as Potamo's guess and answered with McGiffert, but the witness also needs placing once, for example "Epiphanius, who wrote decades later on Athanasius's side".
- **M1 MINOR.** Card legacy: "Sabinus, a bishop of Heraclea who scorned the Council of Nicaea". The same card names "Potamo of Heraclea". These are different towns. Socrates and his translator say Sabinus was "bishop of the Macedonians at Heraclea in Thrace" (npnf202 l.2878–2884), and McGiffert puts Potamo's Heraclea "in Egypt" (npnf201 l.1515). Under the namesake rule, give each town its region.
- **M2 MINOR.** "Constantine then asked that one word be added: the Son is 'One-in-essence' with the Father" is a colon reveal.
- **M3 MINOR.** Two sentences run past 25 words (the cross of light sentence at 27, the Sabellius sentence at 29).
- **M4 MINOR.** The card's Legacy "How they're remembered" line on Eustathius repeats What is uncertain #2, and an accusation is not how he is remembered. Drop one of the two.

---

## 7. Hermas (not major)

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | PASS |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS, with minor points (M2, M5, M6) |
| 5 | No role for a witness | PASS |
| 6 | Partisan witness marked | PASS (Tertullian's On Modesty reads as polemic in context). Minor, not raised |
| 7 | Contested both sides | PASS on the date. The once-only clause is minor (M3) |
| 8 | Common names | PASS. "Jerome" as Clement M5 |
| 9 | One term | PASS |
| 10 | Story, scene, length | FAIL (B1) |
| 11 | grade_text | PASS |
| 12 | Card order and caveat | PASS |
| 13 | Audio tags | PASS |
| 14 | List line, Who | PASS |

**Quotes**
- "He who had brought me up, sold me to one Rhode in Rome,": exact (Vis. I.1, anf02 l.648–649).
- "very recently in our times in the city of Rome": exact (Muratorian Canon, anf05 l.60178–60179; also in McGiffert's note, npnf201 l.14766).
- "she was created first of all.": exact (anf02 l.1003–1004).
- "that great and holy calling": exact (Mand. IV.3, anf02 l.2013–2014).
- "opportunity to repent but once": exact (l.2020).
- "the only one which favours adulterers.": exact (Tertullian, On Modesty 10, anf04 l.8141).
- Card: "a mere guess": exact as a substring of "no more than a mere guess" (npnf201 l.14795). Others as above.

**Findings**
- **B1 BLOCKING.** Item 10. The brief has 342 words, about 2 minutes 8 seconds at 160 words a minute. Hermas is not a major figure, so the limit is 1 to 2 minutes. The card's "about 2 minutes" understates it. About 20 words need to come out. The brief should not be cut to fit (the pattern says it is rewritten), but the sentences flagged at M5 and M6 are natural places to trim.
- **M1 MINOR.** Card: "Zahn dated it between 97 and 100, because Hermas is told to send a copy to a Clemens he took to be Clement of Rome." McGiffert gives that inference as "concluded by many" and reports only that Zahn assigns it "to an unknown Hermas, a contemporary of the Roman Clement" (npnf201 l.14799–14808). The "because" is the drafter's.
- **M2 MINOR.** "The book's hardest point comes in the commands." "Hardest" is an unearned judgment.
- **M3 MINOR.** On the once-only repentance, the ANF editor asks in a note "Can the following words be genuine? They reflect the very Montanism here so strictly opposed", and records that part of the clause occurs only in one manuscript (anf02 l.2014–2017). The brief and card state the teaching flatly. Tertullian's attack supports the book's lenient reading, so this is minor, but the doubt could go on the card.
- **M4 MINOR.** records.json: the Zahn contested_claim names only one side. Name the other (the Muratorian Canon and the majority McGiffert reports).
- **M5 MINOR.** Three sentences run past 25 words (Muratorian 29, Tertullian 26, Jerome 31).
- **M6 MINOR.** "When he wrote is argued." and "That one chance became a dispute." are dispute-announcing openers (the same formula as Ignatius M5).

---

## 8. Valentinus (not major; hostile-witness founder)

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | FAIL (B1, B3, B4) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | FAIL (B1: the scene's place and time are added) |
| 4 | Reading aids | PASS, with minor points (M2, M7) |
| 5 | No role for a witness | PASS |
| 6 | Hostile witness; two for the teaching; separate agreed from single | FAIL (B2) |
| 7 | Contested both sides | PASS on the card. The brief is minor (M4) |
| 8 | Common names | PASS. "Marcus" is minor (M3) |
| 9 | One term | PASS |
| 10 | Story, scene, length | PASS (2:01) |
| 11 | grade_text | PASS |
| 12 | Card order and caveat | PASS |
| 13 | Audio tags | PASS |
| 14 | List line, Who | PASS |

**Quotes**
- "an able man both in genius and eloquence.": exact (Adv. Val. 4, anf03 l.43110–43111).
- "broke with the church of the true faith.": exact (l.43113).
- "came to Rome in the time of Hyginus, flourished under Pius, and remained until Anicetus,": exact (Irenaeus III.4.3, anf01 l.39969–39970).
- "the disciple of Platonism,": exact (Praescr. 30, anf03 l.21333).
- "the simple,": exact (anf02 l.32107).
- "But when the only good Father visits it, it is sanctified, and gleams with light.": exact (Strom. II.20, anf02 l.34301–34302).
- Card: "the disciple of Platonism.": exact.

**Findings**
- **B1 BLOCKING.** The opening, "At Rome, in the middle of the second century, a teacher named Valentinus hoped to be made bishop", sets the scene with a place and time its sole witness does not give. Tertullian, *Against the Valentinians* 4 (anf03 l.43110–43115), names neither Rome nor a date for the bishopric. The time comes from Irenaeus and the place is inferred. The brief says Tertullian "alone tells this story", so the scene should hold only what he says.
- **B2 BLOCKING.** The two-witness rule. The brief says "His teaching reaches us through two opponents, Irenaeus and Clement, who wrote separately". It then gives each witness a different point: the paired beings to Irenaeus, and faith against knowledge to Clement, who is speaking of the followers. No single point of teaching is shown agreed by two witnesses. The pattern also asks the brief to separate what the witnesses agree on from what rests on one, and it does not. records.json tags the paired-beings claim Documented with "Clement (independent on teaching)", but Clement does not attest the pairs. The Library holds a second witness to the system: Hippolytus, *Refutation* VI (anf05 l.8701 ff.), sets out the Valentinian emanation of Aeons, though he may depend on Irenaeus in part. On the saved-by-nature point, Irenaeus I.6 and Clement Strom. II.3 do agree. Rebuild the paragraph on points that two witnesses share, and mark the rest as resting on one.
- **B3 BLOCKING.** Card legacy: "Irenaeus of Lyon calls him the first who adapted the Gnostic teaching to a school of his own." The translator's note at Adv. Haer. I.11.1 (anf01 l.31516–31519) warns against exactly this reading: "The first of the two or three here referred to, not the first of the Gnostic teachers, as some have imagined." Irenaeus says Valentinus "adapted the principles of the heresy called 'Gnostic' to the peculiar character of his own school". Drop "the first".
- **B4 BLOCKING.** Card, What is uncertain: "His own words survive only in Clement's quotations." The Hippolytus translator's note in the Library says the Refutation's account of Valentinus is "mostly given in extracts from Valentinus' work Sophia" (anf05 l.8735–8741). Hippolytus also reports Valentinus's own vision of a newborn child who said he was the Logos (anf05 l.10054–10058). Against the vendored sources, "only" is wrong. Name Hippolytus with a hedge, for example "in quotations, chiefly Clement's".
- **M1 MINOR.** The caravanserai paraphrase says the heart is a place "where many evil spirits lodge and care nothing for the place". In Clement it is the men lodging in the inn who take "no care for the place as belonging to others", and the heart is "the abode of many demons" (anf02 l.34297–34301). The tight paraphrase merges the two halves of the image.
- **M2 MINOR.** The letter quote is split. The paraphrase ends one paragraph, the school paragraph follows, and the closing line then returns to the heart. The close lands as a beat cut off from its passage. Keep the quote with its paraphrase and close on the school, or move the school paragraph before the letter.
- **M3 MINOR.** "Ptolemaeus, Heracleon and Marcus": the vendored translator spells "Heraclean" (anf03 l.43120). "Marcus" is a common name, and Tertullian's own identifier is "the magician Marcus". Use it at first mention in both the brief and the card.
- **M4 MINOR.** "in the middle of the second century" (and Hyginus to Anicetus) is told plainly, while Tertullian's "under the episcopate of the blessed Eleutherus" (anf03 l.21336–21337) appears only on the card and in records.json, where it is Contested.
- **M5 MINOR.** "Marcion of Sinope" is used as the identifier. See Marcion M3.
- **M6 MINOR.** records.json tags single direct witnesses Inferential-Thin (Irenaeus on the dates, Tertullian on the bishopric). See Marcion M5.
- **M7 MINOR.** Two sentences run past 25 words (the confessor sentence at 26, the caravanserai sentence at 28).

---

## Summary

| Profile | Blocking | Minor |
|---|---|---|
| Josephus | 4 | 9 |
| Ignatius of Antioch | 2 | 5 |
| Marcion of Sinope | 2 | 5 |
| Justin Martyr | 0 | 5 |
| Clement of Alexandria | 2 | 5 |
| Eusebius of Caesarea | 1 | 4 |
| Hermas | 1 | 6 |
| Valentinus | 4 | 7 |
| **Total** | **16** | **46** |

Patterns that recur across profiles, each already counted above:
- **Single-witness claims.** "Only" and "single witness" claims fail against the Library more than once: Josephus on Vespasian (Suetonius), Marcion's bishop-father (Ps.-Tertullian), and Valentinus's own words (Hippolytus). Before any "only" or "alone" line passes, grep the whole Library.
- **records.json tags.** Direct reports from one partisan witness are tagged Inferential-Thin. One witness's direct report is not an inference.
- **Dispute openers.** Paragraphs open with a line announcing a dispute ("X became a dispute", "X is argued").
