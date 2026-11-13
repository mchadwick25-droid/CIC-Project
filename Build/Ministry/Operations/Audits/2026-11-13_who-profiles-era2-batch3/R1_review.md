# R1 review: nine Who profiles, era 2 batch 3 (Church Family Tree)

Reviewer: independent, first sight of these drafts. Bar: `Who_Profile_Pattern.md` review checklist 1 to 14, its outside-witness section, and the Style Guide sections it cites; `CLAUDE.md` "Trust and source fidelity" and "Accessible and rigorous"; Mark's rulings in the Decision-Log (2026-11-12: majors capped at 2:30, about 405 words; non-majors 1 to 2 minutes, at most about 324 words; major is a cap, not a target). Majors by the coordinator's call: Martin of Tours, Evagrius Ponticus, Epiphanius of Salamis. Not major: Ammianus Marcellinus (outside witness), Didymus the Blind, Fabiola of Rome, Olympias of Constantinople, Melania the Elder, Marcella of Rome. The findings of the four earlier Who review folders (era 1 batches 1 to 3, era 2 batch 1, R1 to R3) were read first and checked for again, above all the era 2 batch 1 witness swap. I did not edit the drafts. I made no model calls and no paid calls of any kind.

Method. Every quotation in the briefs and cards was searched in its vendored file with whitespace-tolerant matching (tags stripped in .xml, whitespace collapsed, quote marks straightened), then read in context with the translator's and editor's notes nearby. For every "X says", the words were found in X's own text, not in the headings, notes or prolegomena around it. Every factual sentence was checked against the passage it rests on. "Only", "first", "never" and single-witness lines were grepped across `cic/texts/`. Readability came from `engine.m1.gates.grade_text`, run locally with no model call. Length assumes 162 words a minute. Line numbers point to the vendored files under `cic/texts/`.

Applies to all nine:
- The audio scripts match the briefs word for word once tags are removed. Each opens with `[calmly]`, and in all nine `[warmly]` sits immediately before the last sentence (89 to 153 characters from the end). No tags appear in the briefs, cards or records.json.
- `grade_text` passes for all nine (FK 5.9 to 8.2, Flesch 60.9 to 75.7). Didymus (60.9), Evagrius (61.0) and Ammianus (61.5) sit near the Flesch floor; re-score any clause added by the fixes below. None reads as choppy.
- No narrator sentence runs past 25 words. The three long sentences are quotation-led: Didymus's close (28 words), Fabiola's close (28) and Olympias's answer to the prefect (27).
- Lengths. The three majors run 403 to 405 words (2:29 to 2:30), at the cap. The six non-majors run 322 to 323 (1:59 to 2:00), at the limit. None reads as stretched. The major calls are reasonable on the record: the founder of Gallic monasticism, the first systematic writer on the eight thoughts, and the author of the Panarion who opened the Origenist quarrels in the East. That call is Mark's.
- Card fields are in Mark's order in all nine. No card carries an empty array or string. `sources` entries carry `"date": null`, as the approved era 1 batch 2 and era 2 batch 1 cards do; not counted.
- Outside witness (Ammianus). The card has `label: "Outside witness"` and Tradition "Outside the church", as Tacitus and Pliny the Younger do. The brief says who he was, exactly what he says, and how far he can be trusted, with each doubt owned (Gibbon, Ramsay and Abbott, each through the writer who quotes him). It has no "what he fought for" beat. He is a historian and not a polemicist. Item 14 passes.
- Witness swaps, the era 2 batch 1 pattern, were checked line by line and were not found in this batch. Each modern note is given to the edition or to its named writer: "The notes to W. H. Fremantle's edition" (the Melania pun, the Marcella translator), "W. H. Fremantle's English edition of Jerome dates her death to 399" (the edition's heading to Letter 77), Clarke's note on the suppression of Evagrius's works, Abbott inside Jackson's note, Gibbon and Ramsay inside Yonge's preface, Zenos's note on the anthropomorphite charge. Quotes that a writer gives inside another's text are given to the right person (Didymus's praise of Origen through Socrates; Evagrius's "Let then what is inexplicable be adored in silence" inside Socrates's quotation marks). The one line that adds words to a witness's report is Evagrius B1.
- One term (item 9), report only. Two card `tradition` values are not site tradition names in `cft-website/index.html`: Epiphanius "Palestinian / Cyprus" and Olympias "Constantinople". Both are the region column of the era 2 scan. Ammianus's card cites "Theodoret of Cyrus"; the era 2 batch 1 R2 fixes settled the batch on "Theodoret of Cyrrhus" (counted under Ammianus and Didymus). Didymus's brief has "Antony the hermit", where the era 2 batch 1 profile is "Antony the Great"; report only. Settle these when the profiles are placed.
- Item 14, list lines (report only, not fixed). Didymus the Blind (l.34040) and "Evagrius" (l.36572) appear as voice entries in their traditions' source lists. None of the nine has a people-list line found on the site. Every subject passes the Who test.
- "Only", "first", "never", all grepped. They pass: Fabiola "the first person to found a hospital" is Jerome's, in his words, and the card names Gregory of Nazianzus's "new city" against it (Fabiola M2 asks for one clause in the brief); Marcella "no highborn lady at Rome ... had yet dared" is Jerome's; Gennadius's "first, or among the first" is his own hedge (Evagrius M1 on the wording); Marcella card "known from Jerome alone" holds (every other Library mention of her cites Jerome, for example Fremantle's prolegomena to Rufinus, npnf203 l.45908); Melania "her only son" is Jerome's and the card gives Clarke's "two other sons"; Ammianus "never 'knowingly perverted'" is his own (Ammianus M3 on a dropped hedge).

| Profile | Words | Est. length | FK | Flesch |
|---|---|---|---|---|
| Ammianus Marcellinus (outside witness) | 323 | 2:00 | 7.9 | 61.5 |
| Martin of Tours (major) | 405 | 2:30 | 6.6 | 70.7 |
| Didymus the Blind | 323 | 2:00 | 7.9 | 60.9 |
| Evagrius Ponticus (major) | 405 | 2:30 | 8.2 | 61.0 |
| Fabiola of Rome | 322 | 1:59 | 5.9 | 75.7 |
| Epiphanius of Salamis (major) | 403 | 2:29 | 7.4 | 64.3 |
| Olympias of Constantinople | 323 | 2:00 | 7.5 | 62.4 |
| Melania the Elder | 322 | 1:59 | 6.5 | 70.5 |
| Marcella of Rome | 323 | 2:00 | 6.8 | 66.7 |

---

## 1. Ammianus Marcellinus (outside witness)

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | PASS, with minor points M1, M2 |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS, with minor points M3, M4 (dropped hedges) |
| 5 | No role for a witness | PASS (Yonge, Gibbon, Ramsay, Abbott, Jackson, Rolfe, Hefele named) |
| 6 | Partisan witness marked | PASS (not applicable; his own religion is told as uncertain) |
| 7 | Contested both sides | PASS (the Temple fire: Ammianus against Abbott, with a contested_claim) |
| 8 | Common names | MINOR (M6) |
| 9 | One term | MINOR (M7) |
| 10 | Story, scene, length | PASS (2:00) |
| 11 | grade_text | PASS |
| 12 | Card order and caveat | PASS. knownFor is minor (M5) |
| 13 | Audio tags | PASS |
| 14 | List line, outside witness | PASS as an objective historian. No list line (report only) |

**Quotes** (`ammianus-marcellinus_roman-history_yonge1862.txt` unless named)
- "It is certain that on one day one hundred and thirty-seven dead bodies were found in the Basilica of Sicininus, which is a Christian church.": exact (XXVII.3.13, l.23185; a note marker "1" follows "church").
- "a Greek by birth, and formerly a soldier": exact (XXXI.16.9, l.32329).
- "enriched by offerings from matrons, riding in carriages, dressing splendidly": exact (XXVII.3.14, l.23196).
- "no wild beasts are so hostile to men as Christian sects in general are to one another.": exact (XXII.5.4, l.15127).
- "a cruel action, and one deserving to be buried in everlasting silence.": exact (XXII.10.7, l.15973). See M2 on what the action was.
- "knowingly perverted": exact (l.32333), inside "as I believe, I have never knowingly perverted" (M3).
- "an accurate and faithful guide.": exact (Gibbon, in Yonge's preface, l.770).
- "fearful balls of fire burst forth": exact (XXIII.1.3, l.16876).
- "generally believed": Abbott's words, "was generally believed to have been stopped by some supernatural fiery manifestation" (Jackson's note to Theodoret III.15, `npnf203_...` l.12370–12382).
- "if both parties had not been equally exasperated by hatred of George.": exact (XXII.11.10, l.16070).
- Card: "an accurate and faithful guide, who has composed the history of his own times." exact (l.770; "without^" OCR mark follows). "did not find a follower until the time of Ammianus Marcellinus." exact (Rolfe, `suetonius_..._rolfe1914.txt` l.375). "the heathen historian Ammianus Marcellinus" exact (Hefele v2 l.5495). "the general belief is, that he adhered to the religion of the ancient Romans." exact (l.751). "did not entirely escape the contagion" exact (l.809). "was generally believed", "was probably stopped by a violent thunderstorm or thunderstorms." exact (npnf203 l.12380–12382). "it was said" exact (XV.7.8, l.4189). Antioch and the staff of Ursicinus: Yonge's preface, l.735–745. The 367 running head: l.23163.

**Findings**
- **M1 MINOR.** "He says Julian let the Christian sects argue freely." Ammianus says Julian called the sect leaders to the palace and "expressed his wish that their dissensions being appeased, each without any hindrance might fearlessly follow the religion he preferred". He did it "the more resolutely because, as long licence increased their dissensions, he thought he should never have to fear the unanimity of the common people" (l.15117–15127). Fix: "He says Julian gave the Christian sects freedom, expecting it to deepen their quarrels." records.json `claims[5]` has the same wording.
- **M2 MINOR.** "Julian's ban on Christian teachers of rhetoric". The held English says "his forbidding masters of rhetoric and grammar to instruct Christians" (l.15972). The brief's reading is the usual one, but no held text gives it, and the Library has no Latin. Fix: "Still, he calls Julian's law on teachers of rhetoric and grammar 'a cruel action...'". records.json `claims[6]` likewise.
- **M3 MINOR.** "Ammianus says he never 'knowingly perverted' the truth." His sentence is hedged: "which, as I believe, I have never knowingly perverted" (l.32333). Fix: "Ammianus says he believes he never 'knowingly perverted' the truth."
- **M4 MINOR.** "Professor Ramsay ... says he shared his age's belief in omens." Ramsay says he "did not entirely escape the contagion" and that the belief "evidently exercised no small influence over his mind" (l.809–812). Fix: "says the age's belief in omens had some hold on him."
- **M5 MINOR.** Card `knownFor`: "A soldier and historian, not of the church". Yonge, the brief's own witness, says "it is even uncertain whether he was a Christian or a Pagan" (l.751), and the card's first uncertain line says so. records.json `claims[2]` tags "Not a Christian" Widely Accepted on that same sentence. Fix: "A soldier and historian, outside the church by the general belief that Yonge reports", and tag the claim Dominant Modern Reconstruction (Yonge's "general belief"; Hefele's "heathen").
- **M6 MINOR.** First mentions without context in the brief: "Professor Ramsay" (Yonge: "in Smith's Dictionary of Greek and Roman Biography", l.773–774), "E. A. Abbott" and "Blomfield Jackson" (a listener is not told who either is). Fix: "Blomfield Jackson, in his notes to Theodoret's history, quotes the scholar E. A. Abbott..."
- **M7 MINOR.** Card: "Theodoret of Cyrus". The approved era 2 batch 1 texts use "Theodoret of Cyrrhus" throughout. Use the same form.

No blocking findings.

---

## 2. Martin of Tours (major)

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | PASS, with minor point M1 |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS, with minor point M2 |
| 5 | No role for a witness | PASS (Roberts, Brehaut, Gibson, Halm named) |
| 6 | Partisan witness marked | PASS. The Life is marked as a saint's life by a disciple; Sulpicius placed on Martin's side at Trier on the card |
| 7 | Contested both sides | PASS (the worth of the Life: Sulpicius, Smith's Dictionary, Roberts, with a contested_claim) |
| 8 | Common names | PASS (Sulpicius Severus, Hilary of Poitiers, Auxentius of Milan, Gregory of Tours) |
| 9 | One term | PASS |
| 10 | Story, scene, length | PASS (major, 2:30) |
| 11 | grade_text | PASS |
| 12 | Card order and caveat | PASS |
| 13 | Audio tags | PASS |
| 14 | List line, Who | No people-list line (report only) |

**Quotes** (`npnf211_sulpitius-severus-vincent-lerins-cassian.xml` unless named)
- "Martin, who is still but a catechumen, clothed me with this robe.": exact (Life 3, l.793). A scripture note, "St. Matt. xxv. 40.", sits between "clothed" and "me"; read and passed.
- "extremely difficult to decide as to the real value of his narrative.": exact (Roberts's note to Life 1, l.623).
- "I am the soldier of Christ: it is not lawful for me to fight.": exact (Life 4, l.841).
- "that his clothing was mean, and his hair disgusting.": exact (Life 9, l.1080).
- "a foul and unheard-of indignity, that a secular ruler should be judge in an ecclesiastical cause.": exact (Chronicle II.50, l.11658).
- "O Lord, if I am still necessary to thy people, I do not shrink from toil: thy will be done.": exact (Letter III, l.2429; "is said to have burst into tears" just before).
- Card: "never again did he attend a synod" exact (Dialogue III.13, l.5217). "nothing of which I had not certain knowledge and evidence." exact (l.616). "filled with the most puerile fables" exact (l.625). "must be left to the judgment of the reader." exact (l.629). "a bold, loquacious, impudent, and extravagant man" exact (l.11644). "the accusers were as distasteful to me as the accused." exact (l.11642). "as long as Martin survived" exact (l.11659); Halm's Latin "quoad usque Martinus Treueris fuit, dilata cognitio est" (`sulpicius-severus_..._halm1866-csel1.txt` l.5905–5906) bears out the card's note and the brief. "is supposed to be the modern Amiens." exact (l.772). "became a model for saints' lives.", "merely a continuation of it." exact (Brehaut, `gregory-tours_..._brehaut1916.txt` l.11935–11936). Gregory: the eleventh year of Constantine and Sabaria (l.1414–1417), Candes, the eighty-first year and the quarrel over the body (l.1470–1500). Brehaut's 397 (l.595, l.11933). Gibson on Ligugé and Marmoutier (l.15446). Condate "probably" Cosne (l.2382). The cloak and the sword (l.775–790), the exorcist (l.887), Illyria and Milan (l.946–950), eighty disciples and goods in common (l.1133–1140), Sulpicius's visit and questions (l.1840).

**Findings**
- **M1 MINOR.** "Sulpicius says Martin begged them to drop the charge". Sulpicius names one accuser: Martin "did not cease to importune Ithacius, that he should give up his accusations" (l.11655; Halm "increpare Ithacium", l.5902). Fix: "Martin pressed Ithacius to drop the charge".
- **M2 MINOR.** "In Illyria he spoke against the Arians and was publicly beaten. Auxentius of Milan drove him from that city." "That city" has no antecedent in the brief, and the Life has him driven from his own monastery at Milan after he had left Illyria (l.946–950). Fix: "Back in Italy he set up as a monk at Milan, and Auxentius, the Arian bishop there, drove him out."

No blocking findings.

---

## 3. Didymus the Blind

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | PASS, with minor point M1 |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS |
| 5 | No role for a witness | PASS (Richardson, Jackson named) |
| 6 | Partisan witness marked | PASS |
| 7 | Contested both sides | PASS (four tellings of the Antony saying, each named, with their hedges, on the card) |
| 8 | Common names | MINOR (M4 card, M5 brief) |
| 9 | One term | PASS |
| 10 | Story, scene, length | PASS (2:00) |
| 11 | grade_text | PASS (60.9, near the floor) |
| 12 | Card order and caveat | PASS in order. Card dates (M2) and holdings (M3) |
| 13 | Audio tags | PASS |
| 14 | List line, Who | Voice entry, l.34040 (report only) |

**Quotes**
- "a faculty which he shares with ants and flies and gnats.": exact (Jerome, Letter 68.2, `npnf206_...` l.15814).
- "the great bulwark of the true faith": exact (Socrates IV.25, `npnf202_...` l.13847).
- "the profound wisdom of that extraordinary man.": exact, inside Socrates's quotation of Didymus (l.13847).
- "for what I did not know I learned from him, and what I knew already I did not forget.": exact (Letter 84.3, npnf206 l.19004). The "master" defence is at the end of the same section ("for me a disciple to give to one both old and learned the name of master").
- Card: "gnats and flies" (Socrates, l.13847), "rats, mice, and the lowest animals" and "is related" (Sozomen III.15, l.31968), "is said" (both), "for the express purpose of hearing, or, at least, of seeing him." exact (l.31968). "has already passed his eighty-third year." exact (Lives 109, npnf203 l.41463). Rufinus's mice, flies and lizards ("mures et muscae et lacertae"), the readers asleep, the clean animal chewing the cud, the school and Athanasius's approval, and "vivae vocis eius ... auditores" (`eusebius_werke-bd2-2-..._schwartz-mommsen1908.txt` l.29849–29919). Palladius's four visits, age 85, blind at four, never learned to read (`palladius_lausiac-history_clarke1918.txt` l.211). Justinian "after he had anathematized Origen, Didymus, and Evagrius" (`evagrius-scholasticus_..._walford1846.txt` l.9724; the dispute at l.9529).

**Findings**
- **M1 MINOR.** "Socrates of Constantinople, Sozomen and Rufinus of Aquileia tell the same saying, each with other animals." Socrates's "gnats and flies" (l.13847) are two of Jerome's three. Fix: "each with a different list of animals."
- **M2 MINOR.** Card uncertain: "Blomfield Jackson's note to Theodoret gives about 309 to 399." The note reads "Flourished c. 309–399" (npnf203 l.15033), years of activity, not of life. Fix: "Blomfield Jackson's note to Theodoret has him flourishing from about 309 to 399."
- **M3 MINOR.** Card keyWorks and `sources.ownWords`: "the Library holds the Greek text Mingarelli printed in 1769", language "Greek and Latin". The vendored file's own header says a full census "found ZERO Greek characters anywhere" and the Greek column "is wholly unrecoverable as Greek text" (l.50–54). Fix: "the Library holds Mingarelli's 1769 edition; its Greek column did not survive the scan, and his Latin translation is usable", language "Latin (Greek unreadable in the scan)".
- **M4 MINOR.** Card first mentions without place: "Palladius" in `dates` (the card never gives "Palladius of Helenopolis") and "Socrates" in keyWorks, before "Socrates of Constantinople" in legacy. Socrates is the pattern's own example of a common name. Also "Theodoret of Cyrus" in sources; use "Cyrrhus" as Ammianus M7.
- **M5 MINOR.** The brief's first mention is "A blind scholar named Didymus"; "Didymus of Alexandria" waits for paragraph 2. Fix: "A blind scholar of Alexandria named Didymus came to see him."

No blocking findings.

---

## 4. Evagrius Ponticus (major)

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | FAIL (B1). Minor point M1 |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | FAIL in part (B1: words added inside a witness's report) |
| 4 | Reading aids | PASS |
| 5 | No role for a witness | PASS (Dysinger, Clarke named) |
| 6 | Partisan witness marked | PASS for Jerome (hostile, on the card). Palladius's praise is minor (M4) |
| 7 | Contested both sides | FAIL (B1, an identification the record tags Inferential-Thin told as stated). The route is minor (M2) |
| 8 | Common names | PASS in the brief. Card is minor (M3) |
| 9 | One term | PASS |
| 10 | Story, scene, length | PASS (major, 2:30, at the cap) |
| 11 | grade_text | PASS (61.0, near the floor) |
| 12 | Card order and caveat | PASS in order. Caveat is minor (M4) |
| 13 | Audio tags | PASS |
| 14 | List line, Who | Voice entry "Evagrius", l.36572 (report only) |

**Quotes**
- "Even if the oath was in a trance, nevertheless I did take it.": exact (Lausiac History 38.7, `palladius_lausiac-history_clarke1918.txt` l.457).
- "The demon of acedia, which is also called the noonday demon, is the most burdensome of all the demons,": exact (Praktikos 12, `evagrius_praktikos_dysinger.txt` l.216). "so that the day appears to be fifty hours long.": exact (l.217). The eight thoughts, gluttony first and pride eighth: l.188–196. The CC BY attribution travels ("in Luke Dysinger's English").
- "or among the first at least": exact (Gennadius 11, `npnf203_...` l.42329). See M1.
- "Let then what is inexplicable be adored in silence.": exact, inside Socrates's quotation of the Monachicus (III.7, `npnf202_...` l.10614).
- "becomes either a stone or a God.": exact, in Jerome's own text (Letter 133.3, `npnf206_...` l.27826; the Melanium note sits a few words earlier).
- "Origenistic tendency.": exact (Clarke's note 255, l.1149).
- "Whoever shall read these productions," / "will be convinced of their excellence.": exact (Socrates IV.23, l.13545).
- Card: "or among the first at least" as above. Socrates on Palladius as "a disciple of Evagrius" (l.13707) and the route "with him into Egypt" (l.13545). Sozomen: the husband "plotted his death", Jerusalem, then Scetis (VI.30, l.39664). Palladius: "imagined that her husband had intervened" (l.457). Clarke: Palladius "present at his death, at Cellia in 399 or 400" (note 269); Richardson "Born 345, died 399" (l.42329). "Evagrius the Monk" in the Philokalia: ΕΥΑΓΡΙΟΥ ΜΟΝΑΧΟΥ (`philokalia_..._v1-grc_tzelatis1893.txt` l.4205). Justinian and "Evagrius": Walford l.9529, l.9724.

**Findings**
- **B1 BLOCKING.** "The historian Evagrius Scholasticus reports that the emperor Justinian condemned the Alexandrian teacher Origen, Didymus the Blind and Evagrius." Evagrius Scholasticus writes "Origen, Didymus, and Evagrius" (l.9724; "Origen, Evagrius, and Didymus", l.9529). "The Blind" is not in his report. More important, this profile's own card says: "He does not say which Evagrius. That it is this one is a reading of the passage, not his statement." records.json `absent_details` tags the identification Inferential-Thin "as a statement of Evagrius Scholasticus". The brief tells as his statement what its own record says he does not state, and the pattern says an Inferential-Thin point is "said as an inference with what it rests on, or kept to the card". Fix: "Evagrius Scholasticus, a sixth-century historian, reports that the emperor Justinian condemned Origen, Didymus and an Evagrius. Clarke's note on the suppression of his works points to this Evagrius." Or keep the card's caveat only, and drop the sentence from the brief. records.json `claims[10]` (see M5) should match.
- **M1 MINOR.** "Gennadius ... says he was the first, 'or among the first at least', to teach the eight." Gennadius: "He was first to mention or among the first at least to teach these" (l.42329). Fix: "says he was the first to mention the eight, 'or among the first at least to teach these'." The card's traces line has the same compression.
- **M2 MINOR.** The brief takes him to Jerusalem and Melania without a word on the dispute that records.json sets out as a `contested_claim` (Socrates IV.23: "went with him into Egypt", l.13545). Palladius and Sozomen, two witnesses, agree on Jerusalem, so the line is not unsupported. One clause would place it: "Palladius and Sozomen take him to Jerusalem; Socrates has him go with Gregory into Egypt."
- **M3 MINOR.** Card first mentions without place: "Palladius says he died at fifty-four" in `dates` (the full form comes later in traces) and "as Socrates describes it" in keyWorks (before "Socrates of Constantinople" in traces).
- **M4 MINOR.** The card's uncertain line opens on "his disciple Palladius, who writes in praise of him and tells it as he heard it from Evagrius himself". The brief names Palladius as the man Evagrius told, but never says he writes in praise. The caveat should be in the brief first (item 12). Fix, paragraph 1: "He later told the story to his disciple, Palladius of Helenopolis, who wrote it down in praise of him."
- **M5 MINOR.** records.json `claims[10]`, "His works were later suppressed for their Origenist tendency", Widely Accepted, cites Clarke's note together with Evagrius Scholasticus on Justinian. The second is the Inferential-Thin identification of B1. Split it: Clarke's note alone for the suppression, and the condemnation as its own claim, tagged Inferential-Thin as the `absent_details` note already says.

---

## 5. Fabiola of Rome

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | PASS |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS, with minor point M2 |
| 5 | No role for a witness | PASS ("W. H. Fremantle's English edition"; Thierry named as the edition reports him) |
| 6 | Partisan witness marked | PASS (Jerome's "letter of praise"; the card: "her friend and host") |
| 7 | Contested both sides | PASS (Letter 55 and Thierry, with a contested_claim; the first-hospital claim against Gregory of Nazianzus on the card) |
| 8 | Common names | PASS (Jerome of Strido; Pammachius as Jerome's friend; Gregory of Nazianzus and Basil of Caesarea on the card) |
| 9 | One term | MINOR (M1) |
| 10 | Story, scene, length | PASS (1:59) |
| 11 | grade_text | PASS |
| 12 | Card order and caveat | PASS. The card catches the edition's heading against the letter on Portus |
| 13 | Audio tags | PASS |
| 14 | List line, Who | No people-list line (report only) |

**Quotes** (Jerome, Letter 77, `npnf206_jerome-principal-works.xml` l.17329–17777)
- "dishevelled hair, pale features, soiled hands and unwashed neck.": exact (77.4).
- "She was the first person to found a hospital," / "into which she might gather sufferers out of the streets.": exact (77.6).
- "she may rejoice that she has passed through the wilderness of this world and has come at last to the land of promise.": exact (77.7). An editor's note, "Letter LXXVIII. on the Mansions or Halting-places of Israel in the Desert.", sits between "the present" and "she may rejoice"; read and passed.
- Card: "Britain has learned in the summer what Egypt and Parthia knew in the spring." exact (77.10). "the praise of the Christians, the marvel of the gentiles, the sorrow of the poor, and the consolation of the monks." exact (77.2). "the hospital established by her at Portus" exact (the edition's heading). "supposed by Thierry to have been Fabiola" exact (heading to Letter 55, l.12890). "must be carefully distinguished from the lady so often mentioned by Jerome." exact (note to Letter 126, l.25908). The 395 entry, "Oceanus and Fabiola at Bethlehem" (l.3100). Gregory of Nazianzus, Oration on Basil 63: "the new city" with the note "New city—a hospital for the sick." (`npnf207_...` l.42729).

**Findings**
- **M1 MINOR.** "She had once asked him what the camps of Israel in the desert meant". Jerome calls them "the halting-places" (77.7), the edition calls the work "the Mansions or Halting-places of Israel in the Desert", and the card says "halting-places". "Camps" is a third term for one thing. Use "halting-places" in the brief.
- **M2 MINOR.** "'She was the first person to found a hospital,' Jerome writes". The words are Jerome's, but the brief gives the "first" with nothing beside it, while the card says it is praise and sets Basil's "new city" at Caesarea against it. A listener hears a fact. Fix: "'She was the first person to found a hospital,' Jerome writes in his praise".

No blocking findings.

---

## 6. Epiphanius of Salamis (major)

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | PASS, with minor points M1, M2 |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS, with minor point M2 |
| 5 | No role for a witness | PASS (Richardson, Zenos, Moore named) |
| 6 | Partisan witness marked | PASS. Epiphanius as heresy's enemy; Socrates's "simple mind"; the Dialogue as Moore's Palladius |
| 7 | Contested both sides | PASS (the last exchange, told as hearsay with Socrates's disclaimer; the anthropomorphite charge against Zenos on Jerome; both with contested_claims) |
| 8 | Common names | PASS in the brief (Jerome of Strido, Socrates of Constantinople, Theophilus bishop of Alexandria, John bishop of Jerusalem, John Chrysostom). Card is minor (M3) |
| 9 | One term | PASS |
| 10 | Story, scene, length | PASS (major, 2:29) |
| 11 | grade_text | PASS |
| 12 | Card order and caveat | PASS |
| 13 | Audio tags | PASS |
| 14 | List line, Who | No people-list line (report only) |

**Quotes**
- "and to stop his mouth": exact, Epiphanius's letter to John (Jerome, Letter 51.1, `npnf206_...` l.10691).
- "that the devil will once more be what he at one time was": exact (51.5, l.10877).
- "Against all heresies.": Jerome, Lives 114, "wrote books Against all heresies" (`npnf203_...` l.41529).
- "and also by the plain people, on account of their language.": exact (l.41529).
- "the most revered man under the whole heaven.": exact (Sozomen VI.32, `npnf202_...` l.39797).
- "on account of his extraordinary piety", "a man of simple mind and manners,": exact (Socrates VI.10, l.17884).
- "measurably convinced,": exact (Sozomen VIII.15, l.43616).
- "I hope that you will not die a bishop.": exact (Socrates VI.14, l.18221). Sozomen has "I hope you will not die a bishop" (l.43616); the brief follows Socrates's form, as it follows his "Expect not to arrive at your own country" for John's reply.
- "it was said that demons were expelled, and diseases healed": exact (Sozomen VII.27, l.42331; "at his tomb" follows).
- Card: "a heretic, or a paltry schismatic", "a most holy saint" exact (the Dialogue, `palladius_dialogue-life-of-chrysostom_moore1921.txt` l.8921–8925). Zenos's note "Epiphanius himself repudiates their views according to the testimony of Jerome" (l.17884). The refusal to stay or pray with John: Socrates VI.14 (l.18193), Sozomen VIII.14 (l.43553). Richardson's "Born about 310, bishop about 368–9, died 403" (l.41529).

**Findings**
- **M1 MINOR.** "In a village church". Epiphanius's letter: "the church of the villa which adjoins our monastery" (l.10691). A villa is an estate, and the church stood by Epiphanius's own monastery. Fix: "In the church of an estate beside his monastery".
- **M2 MINOR.** "His sharpest charges were against Origen." The superlative has no witness. The letter's charges are given; Socrates says he "had long opposed" Origen's writings (VI.10). Fix: "In the same letter he turned his charges on Origen."
- **M3 MINOR.** Card first mentions: "Jerome's Lives of Illustrious Men" in `dates` and "which Jerome calls" in keyWorks come before "Jerome of Strido" in legacy; "Palladius" in the uncertain line never gets "of Helenopolis" on the card.

No blocking findings.

---

## 7. Olympias of Constantinople

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | PASS |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS |
| 5 | No role for a witness | PASS (Moore, Stephens, Schaff named) |
| 6 | Partisan witness marked | PASS (the Dialogue as "a defence of John" on the card) |
| 7 | Contested both sides | PASS (the fire: Socrates against Sozomen, in place in the opening; the length of the marriage on the card; both with contested_claims) |
| 8 | Common names | PASS in the brief. Card is minor (M1) |
| 9 | One term | PASS |
| 10 | Story, scene, length | PASS (2:00) |
| 11 | grade_text | PASS |
| 12 | Card order and caveat | PASS |
| 13 | Audio tags | PASS |
| 14 | List line, Who | No people-list line (report only) |

**Quotes**
- "My past life ought to avert all suspicion from me," / "for I have devoted my large property to the restoration of the temples of God.": exact (Sozomen VIII.24, `npnf202_...` l.44185).
- "I will not hold communion with those from whom I ought to secede.": exact (l.44202).
- "dispersed among the poor, and the Churches.": exact (the Dialogue, Moore l.9528).
- "with economy.": exact (Sozomen VIII.9, l.43216).
- "instructed many women.": exact (Lausiac History 56.2, `palladius_lausiac-history_clarke1918.txt` l.549).
- "there is only one thing, Olympias, which is really terrible, only one real trial, and that is sin.": exact (the first letter, "To My Lady", `npnf109_...` l.20387).
- "reckon her life among the confessors.": exact (l.549).
- Card: "bride for a few days" exact (l.549). "even for twenty months" exact (Moore l.9475). "she is a man in everything but body." exact (l.8891). Stephens: "seventeen of Chrysostom's extant letters", "born about 368", the husband's death "about two years after", and "nor have we any definite information concerning the remainder of her life" (npnf109 l.20276–20330); the brief's "nothing definite is known" is a fair paraphrase and is not in quotation marks. Schaff "died between 408 and 420" (l.1585). Socrates VI.18, "some of the Johannites set fire to the church" (l.18496). Sozomen VIII.22, "The two parties mutually accused each other" (l.44059). Elpidius, the trust until her thirtieth year (Moore l.9504–9516). The bishops she gave to (l.9586).

**Findings**
- **M1 MINOR.** Card traces: "names Nectarius, Amphilochius, Optimus and Epiphanius of Salamis". Amphilochius and Optimus have no identifier and a general reader will not know them. The Dialogue gives none either (l.9586), so either drop them ("names bishops she provided for, Nectarius and Epiphanius of Salamis among them") or log the gap.

No blocking findings.

---

## 8. Melania the Elder

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | PASS, with minor point M3 |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | MINOR (M2) |
| 5 | No role for a witness | PASS ("The notes to W. H. Fremantle's edition"; Clarke, Fotheringham named) |
| 6 | Partisan witness marked | MINOR in the brief (M1). PASS on the card |
| 7 | Contested both sides | PASS (her father, with a contested_claim; her sons; the erasure, with Fotheringham) |
| 8 | Common names | PASS in the brief (Jerome of Strido, Paula of Rome, Palladius of Helenopolis, Rufinus of Aquileia). Card is minor (M4) |
| 9 | One term | PASS |
| 10 | Story, scene, length | PASS (1:59) |
| 11 | grade_text | PASS |
| 12 | Card order and caveat | PASS in order. One uncertain line is minor (M5) |
| 13 | Audio tags | PASS |
| 14 | List line, Who | No people-list line (report only) |

**Quotes**
- "Henceforth, Lord," / "I will serve Thee more readily, for Thou hast freed me from a great burden.": exact (Jerome, Letter 39.5, `npnf206_...` l.8093).
- "but I am Christ's slave.": exact (Lausiac History 46.4, `palladius_lausiac-history_clarke1918.txt` l.499).
- "her whose name bears witness to the blackness of her perfidy.": exact (Letter 133.3, npnf206 l.27826). The note "Viz., Melanium ... The name means 'black.'" follows.
- "Little children, it was written 400 years ago, It is the last hour.": exact (54.5, l.537; note marker "320" follows "hour").
- "both a monastery in Jerusalem and an endowment for it.": exact (54.6, l.537).
- Card: "Paula and Melanium" exact (Letter 45.4, l.8658). "the thrice-blessed Melania" exact (l.499). "her only son." exact (Letter 39.5). The Chronicle: "Melanius nobilissima mulierum Romanarum et Marcellini quondam consulis filia ... tanto uirtutum praecipueque humilitatis miraculo fuit ut Theclae nomen acceperit" (`jerome_eusebii-chronici-canones-lat_fotheringham1923.txt` l.46246–46252), with the apparatus "ab Hieronymo ipso de exemplaribus suis erasum: vide Rufinum, Apol. II. 26" (l.46286–46287). Rufinus, "he erased her name from all the copies of his work" and "the granddaughter of the Consul Marcellinus" (Apology II.26, npnf203 l.49971). Fremantle, "early in the spring of 397" (npnf203 l.44202). Clarke's notes 287, 317, 318, 323, 324, 327 (l.1213–1293).

**Findings**
- **M1 MINOR.** "Rufinus, her companion, says Jerome later cut her name from every copy of the Chronicle". Rufinus says it in his Apology against Jerome, a book written against him. The brief marks Rufinus only as her companion; the card's first uncertain line marks him as one who "wrote against Jerome". A partisan witness is marked where he is used (item 6). Fix: "Rufinus, her companion and by then Jerome's opponent, says..." Fotheringham's apparatus, which accepts the erasure citing Rufinus, could follow.
- **M2 MINOR.** "Jerome's Chronicle says her humility earned her the name of Thecla." A general listener does not know Thecla (a statement with no context, item 4). Fix: "the name of Thecla, the companion of Paul in the old legend" needs a held witness; if none is quick to hand, "the name of the early woman saint Thecla" is enough.
- **M3 MINOR.** Paragraph 1 ends "and sailed for Jerusalem" (Jerome), and paragraph 2 puts her in Egypt with the monks of Nitria (Palladius: "she sailed with all speed to Alexandria", 46.1). The listener is not told that the two accounts differ on the route. Fix, paragraph 2: "Palladius has her sail first to Alexandria. In Egypt she spent half a year..."
- **M4 MINOR.** Card first mentions: the card never gives "Jerome of Strido" (it opens on "Melanium (in Jerome's letters)"), and "Palladius's account" in `dates` comes before "Palladius of Helenopolis" in legacy.
- **M5 MINOR.** Card uncertain, Silvania: "W. K. Lowther Clarke's notes report that Turner and Butler read it as a continuation of the chapter on Melania, and take Palladius's 'we' as Palladius and Melania." Note 323 reports Turner and Butler on the continuation. Note 324, "I. e. Palladius and Melania.", is Clarke's own and names no one (l.1285–1287). Fix: "...read it as a continuation of the chapter on Melania. Clarke takes Palladius's 'we' as Palladius and Melania."

No blocking findings.

---

## 9. Marcella of Rome

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | PASS, with minor point M1 |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | MINOR (M1, M4) |
| 5 | No role for a witness | PASS ("The notes in W. H. Fremantle's English edition" name Rufinus) |
| 6 | Partisan witness marked | PASS for the Origenist quarrel (Jerome's own "rancour"). The friend's memorial is minor (M2) |
| 7 | Contested both sides | PASS. The sack is told as hearsay with Jerome's "is said" kept |
| 8 | Common names | PASS in the brief (Jerome of Strido, Rufinus of Aquileia). Card is minor (M3) |
| 9 | One term | PASS |
| 10 | Story, scene, length | PASS (2:00) |
| 11 | grade_text | PASS |
| 12 | Card order and caveat | PASS in order. Caveat is minor (M2) |
| 13 | Audio tags | PASS |
| 14 | List line, Who | No people-list line (report only) |

**Quotes** (Jerome, Letter 127, `npnf206_jerome-principal-works.xml`, unless named)
- "scourged her and beat her with cudgels.": exact (127.13).
- "what holy men have seen.": exact (127.13; Jerome's own frame, after a line of Virgil).
- "a young man may indeed die early, but an old man cannot live long.": exact (127.2).
- "publicly to call herself a nun.": exact (127.5).
- "recourse was had to her to settle": exact (127.7).
- "I suffer not a woman to teach.": exact (127.7, quoting 1 Tim. ii. 12).
- "She it was who originated the condemnation of the heretics,": exact (127.10).
- "giving vent to my own rancour.": exact (127.10).
- "Marcella the glory of her native Rome.": exact (127.1, where Jerome also says he let "two years ... go over").
- Card: "has her abode upon the Aventine" exact (Letter 47.3, l.9223). The seventeen letters to Marcella the card lists (23 to 29, 32, 34, 37, 38, 40 to 44, 59) count to seventeen. The notes "By Alaric, 410 a.d." and "i.e. That published by Rufinus" are the edition's, within Letter 127.

**Findings**
- **M1 MINOR.** "She died a few days later, in Principia's arms." The sentence follows the paragraph on the Origenist quarrel of about 399, so "a few days later" reads as a few days after the condemnation. Jerome means a few days after the soldiers' beating in 410 (127.14). Fix: "A few days after the soldiers came, she died in Principia's arms."
- **M2 MINOR.** The card's uncertain line opens on "a friend's praise". The brief never says that Letter 127 is a memorial written by her friend, only that it went "to her friend Principia". The caveat should be in the brief first (item 12). Fix, paragraph 1: "Jerome of Strido tells this in a memorial letter, written in her praise to her friend Principia."
- **M3 MINOR.** Card first mention: "by Jerome's account" in knownFor comes before "Jerome of Strido" in legacy.
- **M4 MINOR.** Card uncertain: "The notes in W. H. Fremantle's English edition, not Jerome's letter, name the translator". This is the "X, not Y" shape (item 4). Fix: "The notes in W. H. Fremantle's English edition name the translator of Origen's book as Rufinus of Aquileia. Jerome's letter does not name him."

No blocking findings.

---

## Summary

| Profile | Blocking | Minor |
|---|---|---|
| Ammianus Marcellinus (outside witness) | 0 | 7 |
| Martin of Tours (major) | 0 | 2 |
| Didymus the Blind | 0 | 5 |
| Evagrius Ponticus (major) | 1 | 5 |
| Fabiola of Rome | 0 | 2 |
| Epiphanius of Salamis (major) | 0 | 3 |
| Olympias of Constantinople | 0 | 1 |
| Melania the Elder | 0 | 5 |
| Marcella of Rome | 0 | 4 |
| **Total** | **1** | **34** |

Blocking finding in one line:
1. Evagrius B1: "Evagrius Scholasticus reports that ... Justinian condemned ... Didymus the Blind and Evagrius" adds "the Blind" to his report and tells as his statement the identification that the profile's own card calls "a reading of the passage, not his statement" and its records tag Inferential-Thin.

Patterns that recur, each already counted above:
- **Witness swaps.** Checked line by line against each witness's own text, notes and headings set apart. None found in this batch. The drafts give each modern note to its edition or named writer, and each quoted-inside-a-quote line to the right voice. The one addition of words inside a report is Evagrius B1.
- **Roles for witnesses.** None. "The notes to W. H. Fremantle's edition" and "Fremantle's English edition" name the edition as the witness, which is the approved form.
- **Told as settled.** One, from the drafts' own records (Evagrius B1). The route after Constantinople is minor because two witnesses agree (Evagrius M2).
- **Hedges dropped.** Ammianus's "as I believe" (M3), Ramsay's "not entirely" (M4), Yonge's "uncertain" behind "not of the church" (M5), Jackson's "flourished" (Didymus M2), Gennadius's "first to mention" (Evagrius M1). Every hedge inside a quoted story is kept: Sozomen's "is related" and "is said", Socrates's "Some say" and "I cannot be sure", Sulpicius's "is said to have", Jerome's "is said" at the sack.
- **Sources of sources.** Marked throughout (Gibbon and Ramsay through Yonge, Abbott through Jackson, Smith's Dictionary through Roberts, Didymus through Socrates, Evagrius's Monachicus through Socrates). One misplaced: Clarke's own note given to Turner and Butler (Melania M5).
- **Partisan or praise caveat not in the brief.** The card's first uncertain line marks a witness that the brief does not (Evagrius M4 Palladius's praise, Marcella M2 a friend's memorial, Melania M1 Rufinus against Jerome).
- **Common names on the card.** The brief is clean in all nine. Five cards first name Jerome, Palladius or Socrates without the place, which comes later in the card or not at all (Didymus M4, Evagrius M3, Epiphanius M3, Melania M4, Marcella M3).
- **"Only", "first", "never".** All grepped against the whole Library. None fails as a single-witness claim. One "first" is left bare in the brief though the card answers it (Fabiola M2).
- **records.json.** Tags are sound on the whole: single direct reports are Documented with a one-witness note, modern dates are Dominant Modern Reconstruction with the reckoner named, and each Contested tag has a `contested_claim`. Two claims need work: Ammianus "Not a Christian" tagged Widely Accepted on Yonge's "uncertain" (M5), and Evagrius's suppression claim carrying the Inferential-Thin condemnation (M5).
