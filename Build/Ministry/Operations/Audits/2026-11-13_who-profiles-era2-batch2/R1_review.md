# R1 review: nine Who profiles, era 2 batch 2

Two independent Opus reviewers, each at first sight of its drafts, reviewed the batch in two parts: part A (Ulfila, Auxentius of Durostorum, Eunomius of Cyzicus, Macrina the Younger) and part B (Damasus of Rome, Priscillian, Tyconius, Cyril of Jerusalem, Apollinaris of Laodicea). Totals: 7 blocking, 40 minor. Each part follows as written.

## R1 review: era 2 batch 2, part A (Church Family Tree Who profiles)

Reviewer: independent, first sight of these drafts. Bar: `Who_Profile_Pattern.md` review checklist 1 to 14 and the standards it points to; `CLAUDE.md` "Trust and source fidelity" and "Accessible and rigorous"; and the era 1 R1 reviews (batch 1, 2 and 3), whose failure types were checked here again. I did not edit the drafts. I made no paid or model-API calls and used no web; readability and quote search ran on local scripts only.

Profiles: `ulfila` (MAJOR), `auxentius-of-durostorum` (not major; recorder Who), `eunomius-of-cyzicus` (MAJOR), `macrina-the-younger` (not major; Who on Mark's women rule). Files are in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era2/batch2/`. Brief line numbers below refer to the `.brief.txt` files, where each paragraph is one line.

Method. Every quotation in the four briefs and cards was searched in the vendored file named in the card's sources, with whitespace- and hyphen-tolerant matching (needed on the Kauffmann and Streitberg OCR), and read in context with the editor's and translator's notes. Every factual sentence of each brief was checked against the passage it rests on. Latin (Auxentius, Maximinus) and German (Kauffmann, Streitberg) material was read in the original and the paraphrase compared with it. Before passing any count, "only", "first" or single-witness line I searched the cited files for the other cases. For each contested point I located both named sides and the witness's own verdict where there is one. Readability came from `engine.m1.gates.grade_text`, run from the repo root. Length assumes 162 words a minute. Line numbers point to files under `cic/texts/` unless marked otherwise.

## Applies to all four

- **Audio = brief.** Each audio script is identical to its brief once `[calmly]` and `[warmly]` are removed (checked by script). Each opens with `[calmly]` and carries one `[warmly]`. No tag appears in any brief or card. In Ulfila, Auxentius and Eunomius, `[warmly]` sits before the final sentence. In Macrina it sits before a two-sentence closing paragraph (Macrina M3).
- **Readability.** All four pass (FK at most 10, Flesch at least 60). Eunomius (60.7) and Ulfila (61.0) sit near the Flesch floor. Macrina is the plainest at FK 6.6; it reads as story and not flattened, so no finding.
- **Card order.** All four follow Mark's order (name, otherNames, knownFor, dates, place, tradition, role, briefLength, keyWorks, legacy, uncertain, sources). Missing fields are left out: Eunomius has no otherNames, Macrina no keyWorks and no "Their own words". keyWorks never exceeds three. Each `uncertain` opens with the brief's own caveat.
- **Length.** Ulfila 402 words, 2:29, and Eunomius 402, 2:29, are under the major ceiling of about 405. Auxentius 324, 2:00, is exactly at the non-major ceiling. Macrina 322, 1:59. Every `briefLength` matches.
- **Who test (item 14).** Ulfila and Eunomius each have a body of work and a following. Auxentius is a recorder Who, the Pontius the Deacon form. Macrina is a Who on Mark's women rule. The drafts carry no list lines; those belong to the map build and were not checked here. Auxentius's card tradition ("Gothic, Vandal & Lombard Homoian Christianity") and Ulfila's ("Homoian ('Arian') Christianity") are two different live traditions, both of which list Ulfila (`cft-website/tree/`); the batch README explains Auxentius's choice. No finding.

| Profile | Words | Est. length @162 | FK | Flesch |
|---|---|---|---|---|
| Ulfila (MAJOR) | 402 | 2:29 | 8.3 | 61.0 |
| Auxentius of Durostorum | 324 | 2:00 | 7.9 | 61.6 |
| Eunomius of Cyzicus (MAJOR) | 402 | 2:29 | 7.7 | 60.7 |
| Macrina the Younger | 322 | 1:59 | 6.6 | 76.1 |

---

## 1. Ulfila (MAJOR)

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | PASS, with one reading the cited editor rejects (M1) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS, with a dispute-announcing opener (M4) and an overstated label (M3) |
| 5 | No role for a witness | PASS (Auxentius, Philostorgius, Photius, Socrates, Sozomen, Kauffmann, Streitberg named) |
| 6 | Partisan witness named and marked | PASS (Auxentius "who wrote in his praise"; Philostorgius a follower of Eunomius; Photius hostile) |
| 7 | Contested both sides | PASS (first bishop: Philostorgius v. Socrates; when he turned: Socrates v. Sozomen, with Auxentius's faith set out first) |
| 8 | Common names placed | PASS in the brief; card minor (M5) |
| 9 | One term | PASS, with M3 |
| 10 | Story, scene, disputes in place, length | PASS (2:29) |
| 11 | grade_text | PASS |
| 12 | Card order, caveat repeated | PASS |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |

**Quotes** (all exact against the rendered text)
- "the Moses of his day" (brief and card): exact, Philostorgius II.5 in Photius's epitome (`philostorgius_ecclesiastical-history_walford1855.txt` l.120). The source says the emperor "would often speak of him in conversation as the Moses of his day"; "named him" is a fair telling.
- "is loud in his praises of this Urphilas" (card): exact (Walford l.120).
- "thinking that it was better to hold such views concerning the Divine nature" (brief): exact, Sozomen VI.37 (`npnf202_socrates-sozomen-ecclesiastical-histories.xml` l.40168–40169).
- "had exposed himself to innumerable perils in defense of the faith" (card): exact (npnf202 l.40176–40177).

**Narrative checks**
- The opening scene follows Auxentius 58–59 (`auxentius-durostorum_epistula-de-fide-vita-obitu-wulfilae_kauffmann1899.txt` l.15263–15276): "ab inreligioso et sacrilogo iudice Gothorum ... persecutio est excitata"; "post multorum seruorum et ancillarum Cristi gloriosum martyrium"; "conpletis septem annis tantummodo in episkopatu"; "cum grandi populo confessorum de uarbarico pulsus in solo Romanie, athuc beate memorie Constantio principe, honorifice est susceptus"; "per Danubium transire fecit". Faithful. Kauffmann reads it the same way (l.3743–3745, "kaiser Constantius ... habe ihm ehrenvolle aufnahme im römischen reich gewährt").
- Bishop at thirty from reader (Auxentius 56, l.15240–15241); birth in 311 and death in June 383 are Kauffmann's working (l.3740–3755, l.3732), and the brief names him for both.
- The faith paragraph matches Auxentius 42–53 (l.15111–15215): the Father "solum uerum deum ... solum esse ingenitum"; the Son "totius creationis auctorem" with "maiorem habentem deum et patrem suum"; the homoousian profession spurned "ut diabolicam adinuentionem"; the homoiousian "errorem ... deuitauit"; forty years preaching "grecam et latinam et goticam linguam". The deathbed creed closing ("in hac fide sola et uera transitum facio ad dominum meum", l.15304) is faithful.
- Letters and Scriptures without Kings, "because ... the Gothic tribes were especially fond of war" (Walford l.120). Streitberg's "kann es doch nicht zweifelhaft sein" that the fragments are the remains of the translation tradition ascribes to Wulfila (`wulfila_gothic-bible-v1-got_streitberg1908.txt` l.600–605) is faithfully told.
- Socrates II.41 (npnf202 l.9608–9612): assent to the Constantinople creed "although he had previously adhered to that of Nicæa", disciple of Theophilus who signed at Nicaea. The year 360 comes from the same book's dating (II.43 and n. 444, l.9739). Sozomen VI.37 (l.40158–40171): Nicene at the council, joined the Arians later over the embassy, "compelled ... or, possibly, thinking". Faithful.
- Card: Codex Argenteus at Uppsala in silver and gold on purple parchment, and the Ambrosian palimpsests from Bobbio at Milan (Streitberg l.1347–1353, l.1402–1418); Selinus as secretary and successor (npnf202 l.41606–41611); Kauffmann's emendation of Constantine to Constantius, Antioch 341 and chorbishop (Kauffmann l.3801–3815); Kauffmann's remark that that age treated numbers otherwise (l.3756–3764 and n. 1, l.3779–3782); Waitz's doubt about the Latin creed (l.3733–3734). All verified.

**Findings**
- **M1 MINOR.** Brief l.13: "Called to Constantinople by the emperor for a debate, Ulfila fell ill there and died, in 383 by Kauffmann's date." The same editor, in the note to that page, says this was Bessell's reading and that Sievers set it right: "Bessell meinte, Wulfila sei auf befehl des kaisers zu dieser disputation abgereist ... Erst Sievers hat den Sachverhalt klargestellt" (Kauffmann l.3718–3719). Kauffmann's own account is that Ulfila answered the emperor's summons to the bishops for an expected council, and meant to debate the Pneumatomachi before it opened (l.3702–3706). The Latin "precepto inperiali ... ad disputationem ... perrexit" (l.15283–15284) can carry either reading. records.json repeats the brief's reading as Documented. Fix: "The emperor summoned the bishops to Constantinople, and Ulfila went, meaning to debate the Pneumatomachi" (or name the two readings), and match records.json.
- **M2 MINOR.** Card uncertain #5: "forty years in all, like Moses". Auxentius names Moses for the crossing of the Danube (59, l.15273–15276). For the forty years he says only "quorum sanctorum imitator erat" (60, l.15278–15280), the saints whose imitator he was; David, also named in 56, reigned forty years too. Kauffmann does not name Moses here (l.3740–3764). The Moses link for the forty is the drafter's. Fix: "forty years in all, the span of the saints he followed", or say whose reading it is. The same words are in the Auxentius brief (Auxentius M4).
- **M3 MINOR.** Brief l.3: Philostorgius's history survives in "a summary by Photius, a later patriarch of Constantinople and his enemy." Photius wrote some four hundred years later; the sources make him hostile to the book and its author (Walford l.52, "The author is a liar"), not a personal enemy. "His" can also be heard as Ulfila. The card says "who was hostile to him" and the Eunomius brief "a hostile one". Fix: "and hostile to him", to match.
- **M4 MINOR.** Brief l.11 opens "The Nicene historians tell his faith another way." This announces the dispute before telling it (the batch 1 Ignatius M5 and batch 3 Peter M1 pattern). It is milder, because the paragraph then gives Socrates and Sozomen in place. The card's uncertain #1 opens the same way ("is told three ways"). Fix: start with "Socrates says ...", and mark the two as Nicene in that sentence.
- **M5 MINOR.** Card uncertain #3: "made bishop by a bishop named Eusebius". This is a common name. The vendored sources give no place: Philostorgius says "Eusebius and the other prelates" (Walford l.120), and Kauffmann speaks only of "Eusebius und die Eusebianer" and an "Eusebianersynode" (l.3767–3769, l.3809–3811). The pattern allows the bare name only with the gap logged. It is not in records.json `absent_details`. Fix: log the gap (or use an identifier only if a vendored source gives one).

No blocking findings.

---

## 2. Auxentius of Durostorum (not major; recorder)

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | PASS, with M3 and M4 |
| 2 | Quotes verbatim | PASS (no direct quotations; Latin paraphrases checked) |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS, with an undefined term (M2) and a dispute opener (M6) |
| 5 | No role for a witness | PASS (Kauffmann, Maximinus, Luft, Traube, Bessell, Jülicher, Waitz named) |
| 6 | Partisan witness named and marked | PASS (card: "writes as a pupil and an admirer"; brief shows the pupil-teacher tie from line 1) |
| 7 | Contested both sides | PASS for authorship (Luft v. Kauffmann); readers one-sided in the brief (M6) |
| 8 | Common names placed | FAIL, minor (M1) |
| 9 | One term | Minor (M2) |
| 10 | Story, scene, disputes in place, length | PASS (2:00, at the ceiling) |
| 11 | grade_text | PASS |
| 12 | Card order, caveat repeated | PASS (card uncertain #1 repeats the brief's authorship caveat) |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS (recorder) |

**Latin and German checked**
- Pupil from earliest years, given by his parents, taught Scripture, raised "ut filium suum in fide": Auxentius 55 (l.15234–15238). "Quem condigne laudare non sufficio et penitus tacere non audeo" (l.15234) is told faithfully as "could not praise his teacher enough ... did not dare stay silent".
- Durostorum (Silistria) in Moesia inferior (Kauffmann l.3397); Ulfila before him in that see as Kauffmann's view, "Ich zweifle nicht daran, dass Wulfila dem schüler auf dem bischofstuhl von Dorostorum vorangegangen war" (l.3431–3433).
- Maximinus 140 (l.16230–16235): "Aucxenti ita meministi, ut non indicares de quo dixeris utrum de superstite, id est Dorostorensi, an de Mediolanensi, qui sine successore decessit"; and both Palladius of Ratiaria and Auxentius "ubicumque examen haberi placuerit ... certamini non defuturos". The brief's two sentences are faithful.
- Luft against Kauffmann on authorship, and Kauffmann's "gleichmässige einheitlichkeit des biblischen stils" (l.3477–3494); Bessell and Jülicher for Theodosius, Waitz against, Kauffmann looking to the Arians of Moesia (l.3474–3478); the margin dating by Waitz and Pertz, Bessell, Traube and Hauler (l.741–753); the lost address, opening and end (l.3455–3456); the "hagiographie der Arianer" remark (l.3449–3451). All verified.
- Streitberg puts Auxentius first under "A. Arianische Quellen" (Streitberg l.612–613). Verified.

**Findings**
- **M1 MINOR.** Brief l.1: the first mention is a bare "Auxentius" ("From his earliest years, Auxentius was Ulfila's pupil"). The identifier waits until l.3. This brief itself turns on there being two men of the name (Maximinus's Durostorum and Milan, l.3). The pattern asks for the subject's own name with its place at first mention. Fix: "From his earliest years, Auxentius of Durostorum was Ulfila's pupil", then "Auxentius" in l.3.
- **M2 MINOR.** Brief l.3: "a Homoian bishop" is the only use of the term, and it is never explained. The same party is then "Arian" twice in the brief: Maximinus "an Arian bishop" (l.3) and "the Arians of Moesia" (l.9). A listener cannot tell these are one party. Fix: one plain gloss at first use (the Ulfila tree page has one: "holding that the Son is like the Father"), or use the sources' "Arian" throughout with a word on the name.
- **M3 MINOR.** Brief l.5: the letter "comes down in the margins of a fifth-century manuscript of Hilary of Poitiers, now in Paris." The codex holds Hilary's works and then Ambrose's On the Faith (Kauffmann l.495–500). The margin text begins at fol. 298, after Hilary ends at fol. 297' (l.683–690), on the leaves of Ambrose's first book: "am rande einiger blätter des ersten buches von Ambrosius" (l.509–512). The sentence names the wrong host text for the margins. Fix: "in the margins of Ambrose's On the Faith, in a fifth-century Paris manuscript that also holds Hilary of Poitiers", or simply "a fifth-century manuscript, now in Paris".
- **M4 MINOR.** Brief l.7: "Seven years among the Goths and thirty-three in Roman lands make forty, like Moses." Auxentius 60 (l.15277–15280) gives the sum and says "quorum sanctorum imitator erat", without naming Moses for it (see Ulfila M2). Fix as there.
- **M5 MINOR.** Card uncertain #2: "Kauffmann thought, with Bessell, that Auxentius sent it from Constantinople to the Arians of Moesia." The item's own previous sentence has Bessell holding that it was written for Theodosius. Kauffmann's "mit Bessell" covers only the place and time of sending (l.3475–3477); the Moesian readers are his own guess ("Ich suche den oder die adressaten unter den Arianern Moesiens"). records.json states this correctly. Fix: "Kauffmann looked for its readers among the Arians of Moesia. With Bessell, he thought Auxentius sent it from Constantinople soon after Ulfila's death."
- **M6 MINOR.** Brief l.9. (a) It opens "How much is Auxentius's own was argued in Kauffmann's day", a dispute-announcing opener (Ulfila M4). (b) Its last sentence gives only Kauffmann's view of the letter's readers. records.json tags this Contested, and the card names Bessell and Jülicher on the other side. The brief does not tell it as settled ("He thought"), but it shows one side. Fix: open on "W. Luft held ...", and add one clause for Bessell and Jülicher's view, or cut the readers sentence and leave it to the card.

No blocking findings.

---

## 3. Eunomius of Cyzicus (MAJOR)

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | PASS |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS, with one choppy paragraph (M4, borderline) |
| 5 | No role for a witness | PASS (Whiston, Cave, Zenos named on the card) |
| 6 | Partisan witness named and marked | PASS for Philostorgius, Photius and Gregory of Nyssa; Socrates unmarked in the brief (M1) |
| 7 | Contested both sides | PASS for the bishopric date and the leaving of Cyzicus; burial one-sided in the brief (M2) |
| 8 | Common names placed | PASS in the brief; card minor (M3) |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | PASS (2:29) |
| 11 | grade_text | PASS |
| 12 | Card order, caveat repeated | PASS |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |

**Quotes** (all exact against the rendered text)
- "Eunomius himself undertook the cause of the Eunomians" (brief): exact, Socrates V.10 (npnf202 l.15350–15351).
- "the Unbegotten Substance" (brief): exact, Apology VII and VIII (`eunomius_first-apology_whiston1711.txt` l.38, l.42).
- "the Son, when he was not before, was begotten" (brief): exact, Apology XV (Whiston l.58).
- "The Father, who sent me, is Greater than I" (brief): exact, Apology XI (Whiston l.48).
- "before an imaginary court" (brief): exact, Gregory of Nyssa, Against Eunomius I (`npnf205_gregory-nyssa-dogmatic-treatises.txt` l.3555).
- "We have learnt to honour in silence what transcends speech and thought" (brief): exact apart from the capital W (npnf205 l.13089–13090).
- "compares also to pearls the speeches which flowed from his lips" (brief): exact, Philostorgius X.6 (Walford l.382).
- Card: "a style well suited to learners" (Walford l.328), "a great scarcity of sense, amidst a profusion of verbiage" (npnf202 l.12483), "God knows no more of his own substance than we do" (l.12515–12516), "had it not found opponents in Basil and Gregory, the Cappadocians" (l.39176–39177), "that we were condemned by default" (npnf205 l.3524), and "the Sly Arch-Heretick reasons shrewdly" (Whiston l.156, Whiston's English for Cave's Latin, as the card says). All exact. Searching the Apology for "knows no more" and "no more of his own" finds nothing, so the card's limit holds.

**Narrative checks**
- The 383 scene: Socrates V.10 (l.15276–15360; the June 383 date at n. 716, l.15280) for the gathering, the written creeds, and the emperor alone at prayer choosing the homoousion; Sozomen VII.12 (l.41115–41126) for "destroyed the others". Faithful.
- Philostorgius III.20 (Walford l.188): from Cappadocia, and taught by Aetius. Gregory's poor farmer father who in winter "used to carve out neatly the letters of the alphabet for boys" (npnf205 l.3364–3372), marked "a foe".
- Bishopric: Philostorgius V.3 under Constantius (Walford l.238); Socrates IV.7 under Valens, with Zenos's note that Sozomen VI.8 agrees and Philostorgius and Theodoret differ (npnf202 l.12484–12490). Leaving Cyzicus: Philostorgius VI.1 and VI.3 (Walford l.246, l.250); Socrates IV.7 (l.12492–12495); Sozomen VI.26 (l.39133–39139). All three are told in place. Faithful.
- Apology paraphrase: no parts (VIII, l.42); no sharing of substance without "Division and Separation, or ... Coalition" (IX, l.44); begotten by the Father's will (XV, l.58; XXIV, l.94); image in operation, not substance (XXIV, l.94). Faithful.
- Banishment and burial at Dacora, his birthplace (Sozomen VII.17, l.41523–41533). Philostorgius at twenty (Walford l.382), and the lisp, "even against his will". Faithful.

**Findings**
- **M1 MINOR.** Brief l.5: "Socrates says the people of Cyzicus grew tired of his showy talk and drove him out." Socrates is a hostile witness here: in the same chapter he calls Eunomius's books "a great scarcity of sense" and his teaching "blasphemous heresies" (npnf202 l.12466–12483). The brief marks Philostorgius, Photius and Gregory, but not Socrates, whose judgment it carries as the reason the people drove Eunomius out. The card marks him ("Socrates, an opponent"). Fix: place Socrates once in the brief ("Socrates, a Nicene opponent, says ...").
- **M2 MINOR.** Brief l.11: "Sozomen says he died soon after and was buried at Dacora in Cappadocia, where he was born." It is attributed, but the other side is only on the card. Philostorgius XI.5 (Walford l.410) has Eutropius move him from there to Tyana and keep his body from his master's tomb, and records.json lists "Where his body lay" as contested. records.json is also inconsistent with itself. It tags "Banished by Theodosius, died soon after, buried at Dacora" Documented while listing the burial as contested. It tags "Taught that God knows no more of his own substance" Contested, but has no `contested_claim` behind it, and the pattern ties Contested to one. Fix: one clause in the brief ("Philostorgius says his body was moved to Tyana"), or drop the burial place from the brief. In records.json, split the burial out of the Documented claim. Then either add a contested_claim for the Socrates quotation (Socrates against the Apology's silence) or tag it Documented as a one-witness hostile report.
- **M3 MINOR.** Card first mentions. The first time Socrates appears on the card is in `dates`, "(Socrates, Sozomen)", with no place; "Socrates of Constantinople" first appears later, in legacy. "Theodoret" (uncertain #2) has no identifier, and a general listener would not know the name. Fix: "Socrates of Constantinople" in `dates`; "Theodoret of Cyrrhus" if a vendored source gives the place, otherwise log the gap.
- **M4 MINOR (borderline).** Brief l.5 runs as seven short sentences, five of them in the form "X says" (average about 10 words). The brief's mean of 11.8 words is the lowest of the four, just under the roughly 12 to 20 the standard asks for. This paragraph reads as a list of witnesses, not as a story. Fix: join the bishopric date into one sentence and the three accounts of the leaving into two.

No blocking findings.

---

## 4. Macrina the Younger (not major; women rule)

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | FAIL on the card (B1); brief PASS, with a loose count (M1) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS, with a long sentence (M5, borderline) |
| 5 | No role for a witness | PASS (Clarke, Moore and Wilson, Jackson, Lampadia, Vestiana named) |
| 6 | Partisan witness named and marked | PASS ("a loving record, written in her honour"; dreams and healing marked as Gregory's signs) |
| 7 | Contested both sides | FAIL (B1); family size framed as a conflict its cited editor resolves (M2) |
| 8 | Common names placed | Minor (M4) |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | PASS (1:59) |
| 11 | grade_text | PASS |
| 12 | Card order, caveat repeated | PASS |
| 13 | Audio tags | Minor (M3) |
| 14 | Who test | PASS |

**Quotes** (all exact against the rendered text)
- "puffed up beyond measure with the pride of oratory" (brief): exact, Life (`gregory-nyssa_life-of-macrina_clarke1916.txt` l.136).
- "the Teacher" (brief, card): exact, On the Soul and the Resurrection (npnf205 l.38089, l.38093).
- "Away, she cried, with that pagan nonsense!" (brief): exact (npnf205 l.38171).
- "Thou, O Lord, hast freed us from the fear of death" (brief): exact (Life l.230).
- Card: "the great Macrina" (Life l.154, l.274); "you have in front of you all her treasure" (l.284, spoken by Lampadia, l.278); "the Church should possess her Phædo, or Death-bed Dialogue" (npnf205 l.247–248; "her" is the Church's, and the card keeps "the Church" in the quote). All exact.

**Narrative checks**
- The opening scene: "the ninth month or a little longer after this disaster" (Basil's death, l.180) and the synod at Antioch (l.184); "no less than eight years, or very nearly" (l.184); the sack spread on a board, and raised "on her elbow but could not come to meet me, her strength being already drained by fever" (l.192). The year 379 is Clarke's (l.52), and the card says so.
- Eldest child, and named for the grandmother who confessed Christ (l.108, l.112); the twelfth year, the betrothal, the young man's death, and the refusals (l.124–128); the mother brought to share the maids' life (l.138, l.158); children "exposed by the roadside in the time of famine" (l.264). Faithful.
- Double monastery under Peter and Macrina: Clarke's introduction (l.80), with his doubt whether Basil's house across the Iris still stood (l.80). Clarke's plain-style argument (l.64). Faithful.
- The Vestiana healing (l.292–310) and the Thecla dream (l.116). Faithful.

**Findings**
- **B1 BLOCKING.** Card legacy traces #1: "Gregory of Nyssa says she drew their brother Basil from the pride of oratory to a life of prayer and work. Blomfield Jackson, who translated Basil's letters, follows Gregory on this." Jackson does not simply follow him. He sets two witnesses side by side (`npnf208_basil-letters-select-works.xml` l.1252–1264). First: "According to his friend Gregory [of Nazianzus, Or. xliii], Basil had already determined to renounce the world." Then: "His brother Gregory, however, represents him as at this period still under more mundane influences ... indebted to the persuasion and example of his sister Macrina for the resolution, with which he now carried out the determination." Jackson reconciles the two: Basil had already decided, and Macrina gave him the resolve to carry it out. The card turns a two-witness point into one witness backed by a modern who agrees, and it cites Jackson for the opposite of his framing. "Gregory" is also ambiguous in Jackson's passage, which names both Gregories. records.json repeats the error ("followed by Blomfield Jackson", Documented, no contested_claim). Fix: "Gregory of Nyssa says she drew Basil ... Gregory of Nazianzus says Basil had already resolved on it; Blomfield Jackson, who translated Basil's letters, gives both and reads Macrina as giving him the resolve to carry it out." Add a contested_claim. The brief's l.5 sentence is attributed ("Gregory says") and may stand, but the card must carry both sides.
- **M1 MINOR.** Brief l.3 and card uncertain #1: the Life "tells dreams and a healing as signs from God". The Life tells two healings. One is Macrina's own tumour, told by Vestiana (l.306–310). The other is the soldier's daughter's eye, told by her father (l.356–378). Gregory then says he leaves out more: the corn that did not run out in the famine, "Healings of diseases, and castings out of demons, and true predictions of the future" (l.384). Card uncertain #4 names only the tumour. Fix: "dreams and healings" in the brief and the card, with the soldier's story beside Vestiana's in uncertain #4 and a note that Gregory says he left more out.
- **M2 MINOR.** Card uncertain #5: "The size of the family is given two ways. The Life speaks of four sons and five daughters ... Moore and Wilson give ten children, five sons and five daughters." The card's own cited editor resolves this. Clarke: "His parents, Basil and Emmelia, had ten children, of whom four sons and five daughters survived infancy" (Clarke l.44). Moore and Wilson's "five of whom were boys and five girls" is at npnf205 l.492. Leaving Clarke out makes a plain count look like an open conflict. records.json carries no entry for it. Fix: give Clarke's account with the other two, or drop the item.
- **M3 MINOR.** Audio: `[warmly]` comes before the two-sentence closing paragraph ("Near the end, Gregory says ... 'Thou, O Lord ...' she began."). Every approved era 1 audio script places it before the final sentence only, as do the other three here. Fix: move `[warmly]` to before "'Thou, O Lord, hast freed us from the fear of death,' she began."
- **M4 MINOR.** Brief l.5 and card legacy #2: "her brother Peter" carries no identifier. Peter is a common name, and Clarke gives the place: Gregory and Peter "became bishops eventually of Nyssa and Sebaste" (l.44). A relation is a role, which the pattern allows only where no place is available. Fix: "her brother Peter of Sebaste" at first mention in each text.
- **M5 MINOR (borderline).** Brief l.5: "W. K. Lowther Clarke, who translated the Life in 1916, reads their home as a double monastery, the women under Macrina and the men under her brother Peter" is 28 words, past the about-25 limit, and grows with M4's fix. Fix: split after "double monastery".

---

## Summary

| Profile | Blocking | Minor |
|---|---|---|
| Ulfila (MAJOR) | 0 | 5 |
| Auxentius of Durostorum | 0 | 6 |
| Eunomius of Cyzicus (MAJOR) | 0 | 4 |
| Macrina the Younger | 1 | 5 |
| **Total** | **1** | **20** |

Every quotation in the four briefs and cards matched its vendored file word for word. The one blocking finding is a card line that cites a modern editor for the opposite of what he says, and so hides a second ancient witness (Macrina B1). The recurring minor failures are the same types the era 1 reviews found: dispute-announcing openers, first mentions without a place, one side of a contested point left to the card, and records.json tags that do not match its own contested_claims.

## R1 review: five Who profiles, era 2 batch 2, part B (Church Family Tree)

Reviewer: independent, first sight of these drafts. Bar: `Who_Profile_Pattern.md`, review checklist 1 to 14, its common-name, witness, card-order and confidence sections; `CLAUDE.md` "Trust and source fidelity" and "Accessible and rigorous"; and the era 1 R1 reviews (batch 1 and 2, 2026-11-12; batch 3, 2026-11-13), whose failure types were checked here: dropped hedges, unnamed modern judgments, false "only"/"no" claims, partisan witnesses left unmarked, card dates taking a contested point as settled, dispute-announcing openers, sentences past about 25 words, records tags that do not fit the five levels. I did not edit the drafts. No paid calls, no model-API calls and no web access were used. Readability and quote search ran as local scripts only.

Profiles: `damasus-of-rome` (MAJOR), `priscillian` (MAJOR), `tyconius` (not major), `cyril-of-jerusalem` (MAJOR), `apollinaris-of-laodicea` (MAJOR). The README records the coordinator's confirmation of the major marks (2026-11-13).

Method. I searched every quotation in the briefs and cards in the vendored file named in the card's sources. I used a whitespace-tolerant matcher that strips XML tags, joins words hyphenated across lines and keeps editor notes in place. I read each quote in context, notes included. Where a brief paraphrases Latin, Greek or German (the Collectio Avellana Gesta, Halm's Sulpicius, Schepss's Priscillian and Orosius, Bruns's Braga canons, Burkitt's Tyconius, Lietzmann's Apollinaris), I opened the passage and checked that the paraphrase is faithful. Every factual sentence in each brief was checked against the passage it rests on. Each contested point was checked for both named sides and the witness's own verdict. Counts, dates, "only" and "no" claims were checked against the files: 137 and 160 dead; the Gesta's consuls Gratian and Dagalaifus (366); the Braga council's Spanish era DXCIX (561); 270 bishops; Schepss 1885; Lietzmann 1904; Cyril's 348, 351, 381, 382, 386 and three exiles. Readability came from `engine.m1.gates.grade_text`, run locally from the repo root. Length is at 162 words a minute. Line numbers point to the vendored files under `cic/texts/` unless another path is given.

## Applies to all five

- **Audio = brief.** Each audio script equals its brief once `[calmly] ` and `[warmly] ` are removed (checked by script). Each opens with `[calmly]` and carries one `[warmly]`, immediately before the closing sentence. No tags appear in any brief or card. Item 13 passes everywhere.
- **Readability.** All five pass (FK at most 10, Flesch at least 60). Damasus sits on the floor (Flesch 60.3).
- **Card order.** All five cards run name, otherNames, knownFor, dates, place, tradition, role, briefLength, keyWorks (three), legacy (traces, remembered), uncertain, sources. No `label`, which is right: none is an outside witness. `"date": null` in sources follows the era 1 cards.
- **Length.** All within the caps. Apollinaris (404 words, 2:30) and Tyconius (324, 2:00) are at the ceilings. `briefLength` on each card matches.
- **List lines (item 14).** Report only, as in era 1: list lines belong to the map Who build. Note that `cic-website/data/world-census.json` holds people rows for Tyconius (Donatism), Cyril (Jerusalem Liturgical-Pilgrimage Christianity) and Apollinaris (Apollinarian Christianity). It holds none for Damasus (card tradition "Imperial and Juridical Christianity") or for Priscillian (the Priscillianist Asceticism people list holds only Sulpicius Severus). The coordinator should confirm where those two keep their list line. All five pass the Who test.

| Profile | Words | Est. length @162 | FK | Flesch |
|---|---|---|---|---|
| Damasus of Rome (MAJOR) | 400 | 2:28 | 8.2 | 60.3 |
| Priscillian (MAJOR) | 399 | 2:28 | 8.0 | 61.2 |
| Tyconius | 324 | 2:00 | 7.5 | 65.4 |
| Cyril of Jerusalem (MAJOR) | 398 | 2:27 | 7.4 | 65.6 |
| Apollinaris of Laodicea (MAJOR) | 404 | 2:30 | 8.2 | 60.9 |

**G-M1 MINOR (cards of Damasus, Cyril, Apollinaris).** "Sozomen" appears at first mention in each card with no context ("Socrates of Constantinople and Sozomen blame Ursinus"; "Socrates of Constantinople and Sozomen say the party of Acacius"; "says Sozomen" in the Apollinaris legacy). The briefs give him context ("a church historian of the next century"), but the card is a separate text. The era 1 batch 2 Bardaisan review (M5) flagged the same. Fix: "Sozomen, a church historian of the fifth century" at first mention in each card.

---

## 1. Damasus of Rome (MAJOR)

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | PASS, with M1, M5 |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS |
| 5 | No role for a witness | PASS (Zenos, Hartranft, Fremantle, Richardson, Jackson named) |
| 6 | Partisan witness named and marked | PASS (the Gesta "from the clergy who backed Ursinus", but see M1) |
| 7 | Contested shown both sides, not settled | FAIL (B1) |
| 8 | Common names placed | PASS in the brief; G-M1 in the card |
| 9 | One term | PASS |
| 10 | Story, scene, in-place disputes, length | PASS (scene at the basilica; the election told three ways in place) |
| 11 | grade_text | PASS |
| 12 | Card order and caveat repeated | PASS |
| 13 | Audio tags | PASS |
| 14 | List line; Who test | Who PASS; list line report only (see above) |

**Quotes** (all exact)
- "both immoderately eager to obtain the bishopric" (Ammianus XXVII.3.12, `ammianus-marcellinus_roman-history_yonge1862.txt` l.14867). The 137 bodies in the Basilica of Sicininus and the prefect's withdrawal to the suburbs are at l.14867 to 14878.
- "of little distinction" (Socrates IV.29, `npnf202` l.14197 region).
- "deprived of the name of bishop" (synodal letter to Illyria, Theodoret II.17, `npnf203` l.10312 region; Auxentius of Milan condemned at l.10272).
- "by the judgment of the apostolic see" (Damasus on Timothy, Theodoret V.10, `npnf203` l.16117).
- "You urge me to revise the old Latin version"; "the command is given by you who are the supreme bishop" (Preface to the Four Gospels, `npnf206` l.46626 to 46641).
- "They were not even admitted to his presence." (Sulpicius II.48, `npnf211` l.11557 region).
- "had a fine talent for making verses and published many brief works in heroic metre" (Lives 103, `npnf203` l.41382 region).
- Card: "that is with the chair of Peter" (Letter 15, `npnf206` l.5045; the date "376 or 377" is at l.5004). "councils of the East and West" paraphrase (Letter 123.10, l.24186). "enriched by offerings from matrons, riding in carriages, dressing splendidly" (Ammianus l.14887). "to rediscover the tombs which had been blocked up for concealment under Diocletian" (Jackson's note, `npnf203` l.10224). "a Spaniard by race" (Zenos's note, `npnf202` l.14197 region). Anathemas against Arius, Eunomius, Sabellius, Photinus and the Macedonians (Theodoret V.11, `npnf203` l.16150 to 16165).
- Gesta (Collectio Avellana 1, `collectio-avellana_...csel35.txt` l.5100 to 5168): Damasus "omnes quadrigarios et imperitam multitudinem pretio concitat"; "inuitat arenarios quadrigarios et fossores"; besieged the basilica; "centum sexaginta de plebe tam uiros quam mulieres occiderunt ... de parte uero Damasi nullus est mortuus". The brief's paraphrase is faithful. Liberius's death is dated "Gratiano et Dagalaifo consulibus" (l.5098), which is 366.

**Findings**
- **B1 BLOCKING.** Item 7. The brief says "Damasus of Rome followed Liberius as bishop in 366", and the card's `dates` field says "Bishop from 366", both plainly. The draft's own records.json lists "The year of his accession and of his death" as a `contested_claim`: 366 (the Gesta's consuls; Hartranft's note on Sozomen VI.23, `npnf202` l.38756 region) against 367 (Jerome's Chronicle, per Zenos's note, `npnf202` l.14197 region; Yonge's margin also reads "A.D. 367" at the riot, Ammianus l.14867). records.json then tags "Succeeded Liberius ... in 366" **Documented**, which contradicts its own contested record. The card's What is uncertain does give both sides. This is the era 1 Suetonius B1 / Tatian B1 pattern: a card date taking a contested point as settled. Fix: card dates "Bishop from 366 (the Gesta's date; Jerome's Chronicle has 367)". In the brief, "followed Liberius as bishop in 366, by the date of the Ursinian account" or round it ("in the 360s"). Retag claim 1 to match the contested record.
- **M1 MINOR.** The brief's "An account from the clergy who backed Ursinus", the card's source author "The clergy who backed Ursinus" and records.json "written by the clergy who backed Ursinus" name an author that no source names. The Gesta is anonymous. The "clergy" attribution comes from the project's own vendoring header ("from the side of the Roman clergy who stayed loyal to Liberius", l.9), which is not a source. The text's partisanship is plain from the text itself ("Ursinus uir uenerabilis", l.5150; "sanctum Ursinum", l.5247; Damasus's party "periuri", l.5103). Fix: "An account from Ursinus's side"; card author "Anonymous, from Ursinus's party".
- **M2 MINOR.** Card uncertain: "Zenos notes that he was 'a Spaniard by race'. No early witness in the sources used here gives his birthplace." The same note continues "native of Mantua" (`npnf202` l.14197 region). The card quotes half the note and then says no birthplace is given. Saying "no early witness" is true, but the cut hides the birthplace the cited note does give. Fix: "Zenos's note calls him 'a Spaniard by race, native of Mantua'; no early witness in the sources used here gives his birthplace." The same applies to the absent_details note.
- **M3 MINOR.** "Ammianus Marcellinus, a pagan soldier and historian" (brief) and "a pagan historian" / "a pagan" (card). Yonge's preface, the edition cited, says "it is even uncertain whether he was a Christian or a Pagan; though the general belief is, that he adhered to the religion of the ancient Romans" (l.750 to 752). Only the vendoring header (l.5 to 6) says "pagan" outright. The hedge is dropped (the era 1 Clement M2 / Bardaisan M1 type). Fix: "Ammianus Marcellinus, a soldier and historian, most likely a pagan".
- **M4 MINOR.** Card uncertain: "Socrates of Constantinople and Sozomen blame Ursinus" reads as two independent witnesses. Hartranft's note at Sozomen VI.23 points to "Soc. iv. 29; Ruf. H. E. ii. 10" (`npnf202` l.38756 region), and Zenos notes that "Socrates follows Rufinus here" (l.14197 region). records.json already says "(from Socrates and Rufinus)". The era 1 Tatian M1 type. Fix: "Socrates of Constantinople, and Sozomen after him, blame Ursinus".
- **M5 MINOR.** "His comfort was that 'the command is given by you who are the supreme bishop.'" Jerome names "two consoling reflections" (`npnf206` l.46641). The second is that readings at variance with the early copies cannot be right. Fix: "One comfort was that ...".

---

## 2. Priscillian (MAJOR)

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | PASS, with M1, M2, M3 |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS |
| 5 | No role for a witness | PASS (Schepss, Richardson, Roberts, Halm named) |
| 6 | Partisan witness named and marked | FAIL (B2) |
| 7 | Contested shown both sides, not settled | FAIL (B1) |
| 8 | Common names placed | PASS |
| 9 | One term | PASS |
| 10 | Story, scene, in-place disputes, length | PASS |
| 11 | grade_text | PASS |
| 12 | Card order and caveat repeated | FAIL (the card opens on a caveat the brief does not carry; part of B2) |
| 13 | Audio tags | PASS |
| 14 | List line; Who test | Who PASS; list line report only (see above) |

**Quotes** (all exact)
- Sulpicius, Chronicle II.46 to 51 (`npnf211` l.11445 to 11730): "a man of noble birth, of great riches"; "the accusers were as distasteful to me as the accused"; "with great pomp"; "it came to be thought the highest exercise of religion to swear by Priscillian"; "not even admitted to his presence"; card "bold, restless, eloquent, learned through much reading"; "could not by any means be set at rest"; "in the town of Arles"; "it was believed that he had practised magical arts from his boyhood". Ithacius "the only one of all of them who was thrust out of the episcopate" supports "Ithacius alone".
- Halm's Latin: "suas episcopum in Abilensi oppido constituunt" (`sulpicius-severus_...halm1866-csel1.txt` l.5740).
- Jerome, Lives 121: "He is still accused by some, of being tainted with Gnosticism"; card "published many short writings, some of which have reached us"; "belonged to the party of Hydatius and Ithacius"; Richardson's "Flourished 379, condemned 380, died 385" (`npnf203` l.41626 region).
- Schepss's preface (`priscillian_quae-supersunt-lat_schepss1889-csel18.txt` l.84 to 94): found autumn 1885 in the Würzburg codex, no name of Priscillian anywhere in it, judged his from the names in Tractates I and II.
- Tractate II (l.4381 to 4392): "in conuentu episcopali qui Caesaraugustae fuit nemo e nostris reus factus tenetur, nemo accusatus, nemo conuictus, nemo damnatus est"; Damasus's letter "ne quid in absentes et inauditos decerneretur". Faithful.
- Tractate I (l.3747 region): "Anathema sit qui Manetem et opera eius doctrinas adque instituta non damnat". Faithful.
- Orosius, Commonitorium 2 (l.10260 to 10266): the soul "descendentem per quosdam circulos a principatibus malignis capi ... in corpora diuersa contrudi". Faithful. Orosius as a Spanish priest rests on Augustine's Retractations, cited in the apparatus (l.10187 region).
- Braga I (`bruns_...1839.txt` l.2367 "ERA DXCIX", which is 561; canon VI l.2512 to 2515, souls that sinned in heaven cast down into bodies, "sicut Priscillianus dixit"; canon IX l.2529 to 2531, souls and bodies bound to fatal stars).

**Findings**
- **B1 BLOCKING.** Item 7. Card `dates`: "Condemned at Saragossa and put to death at Trèves under Maximus". This tells the Saragossa condemnation plainly, while the card's own What is uncertain, records.json (claim tagged Contested) and the brief all present it as disputed. Sulpicius says sentence was passed in absence (`npnf211` l.11504 to 11508). Priscillian says no one of his group was accused, convicted or condemned there (Tractate II l.4381 to 4384). Richardson's "condemned 380" restates the same side. This is the era 1 Suetonius B1 / Tatian B1 pattern. Fix: "Sulpicius Severus says he was condemned at Saragossa (he denied it); put to death at Trèves under Maximus; Ernest Cushing Richardson dates him flourished 379, died 385".
- **B2 BLOCKING.** Items 6 and 12. The brief marks Sulpicius as hostile, but it gives Priscillian's teaching through Orosius and the Braga council without saying either was an enemy. "Orosius, a Spanish priest writing to Augustine of Hippo, says Priscillian taught that souls came down ..." is told as a neutral report. Orosius calls him worse than the Manichaeans ("Manichaeis miserior", l.10260). The Braga canons come 176 years after his death and curse "sicut Manicheus et Priscillianus dixerunt". The brief never says what the card's What is uncertain opens with: "What he taught comes to us mostly through opponents." The pattern asks the card to open with the brief's own caveat, not one the brief lacks. The era 1 Epiphanius B1 is the same type. Fix: one clause in the brief, e.g. "What he taught comes to us mostly through his enemies. Orosius, a Spanish priest who wrote against him to Augustine of Hippo, says ...", and "a council at Braga, long after, in 561".
- **M1 MINOR.** "He says Priscillian did not deny that he had taught lewd doctrines". Sulpicius: "Priscillian did not deny that he had given himself up to lewd doctrines" (`npnf211` l.11648 region). "Taught" adds a charge the source does not make. Fix: "had given himself up to lewd teachings".
- **M2 MINOR.** "He calls Ithacius of Sossuba ... bold, loud and greedy for pleasure." Sulpicius: "a bold, loquacious, impudent, and extravagant man; excessively devoted to the pleasures of sensuality". "Loquacious" means talkative, not loud. Fix: "bold, talkative and given to pleasure".
- **M3 MINOR.** "A council at Braga in 561 cursed souls cast down into bodies and bound to the stars, naming Priscillian." As written the council cursed souls. The canons curse anyone who teaches it ("Si quis animas humanas dicit ... anathema sit"). Fix: "cursed the teaching that souls were cast down into bodies and bound to the stars, as Priscillian said".
- **M4 MINOR.** records.json tags "Did not deny lewd doctrines, night meetings with women and praying naked" **Contested**. No contested_claim stands behind it, and no witness takes the other side (the note itself says "no account from Priscillian's side"). Under the pattern, Contested needs both sides by name and a contested_claim record. This is one hostile witness's report of a court's findings: Documented, with the note "Sulpicius II.50 only; hostile; reports the court".
- **M5 MINOR.** Card legacy, remembered: "Martin of Tours, Sulpicius says, begged the emperor not to shed the blood of the accused ..." This is an event in the case, told during it, not how Priscillian is remembered (the era 1 Suetonius M3 type). Move it to What is uncertain, or drop it, since the brief already tells it.

---

## 3. Tyconius

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | PASS |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS, with M1, M2 |
| 5 | No role for a witness | PASS (Burkitt named throughout) |
| 6 | Partisan witness named and marked | FAIL (B1) |
| 7 | Contested shown both sides, not settled | PASS (Augustine's verdict is attributed; see M3 on the record) |
| 8 | Common names placed | PASS (Augustine of Hippo, Gennadius of Marseilles, Parmenian of Carthage) |
| 9 | One term | PASS |
| 10 | Story, scene, in-place disputes, length | PASS (opens on the book's own first line; 2:00) |
| 11 | grade_text | PASS |
| 12 | Card order and caveat repeated | PASS |
| 13 | Audio tags | PASS |
| 14 | List line; Who test | PASS (census Donatism row holds him) |

**Quotes** (all exact)
- Preface: "Of all the things that occur to me, I consider none so necessary as to write a little book of rules"; "the secret places of the law"; "the vast forest of prophecy" (Augustine, On Christian Doctrine III.30, `npnf102` l.53050 region).
- "a most inconsistent disposition"; card "who, although a Donatist himself, has written most triumphantly against the Donatists" (III.30, l.53015 region).
- "the mixed Church" (III.32, l.53123 to 53124; source "Concerning *the mixed Church*"). The Song of Songs example is in Tyconius's own Rule II too, "Fusca sum et decora" (`tyconius_liber-regularum_burkitt1894.txt` l.7279), so "Tyconius found it" holds.
- "must be read with caution"; "for it is of very great assistance in understanding Scripture" (III.30, l.53076 region). Faith "did not come to us from God"; card "having no enemy to guard against" (III.33, l.53170 to 53180).
- "in defence of the Church" (Letter 93.43, `npnf101` l.39046 to 39047). The council of 270 bishops, Parmenian's reply and warning, and the many still living who could prove it are at l.39050 to 39087.
- "regarding nothing in it in a carnal sense"; card "it is said, sufficiently learned in sacred literature, not wholly unacquainted with secular literature and zealous in ecclesiastical affairs"; flourished "during the reign of Theodosius and his sons" (Gennadius 18, `npnf203` l.42511 region).
- Burkitt: "the little that is known about his life comes chiefly from references scattered up and down in the works of S. Augustine"; the Apocalypse commentary "is believed to be lost"; Primasius, Bede and "above all Beatus, a Spanish priest contemporary with Charlemagne"; Bellum Intestinum "has unfortunately perished" (l.376 to 402). "it would seem that Tyconius wrote before 383 AD" (l.668). "treats Tyconius as an authority to be explained rather than as a theorist to be criticised" (l.685).
- Parmenian as "the successor of Donatus the Great in the see of Carthage" (`npnf104` l.10260).

**Findings**
- **B1 BLOCKING.** Item 6. Augustine of Hippo is the brief's main witness for the life. He was the leading Catholic opponent of the Donatists, and Letter 93 is a polemic written to a Donatist bishop, in which he uses Tyconius against his correspondent. The brief never places him. "Augustine says Tyconius wrote 'in defence of the Church' against his own party" then reads as neutral fact, though "the Church" there is Augustine's Catholic church. "Who both criticised his book and drew on it" places him as a reader of the book, not as an opponent of Tyconius's party. records.json itself notes "(an opponent of his party, one witness for the council report)". The era 1 Epiphanius B1 is the same type. Fix: "Augustine of Hippo, a Catholic bishop who wrote against the Donatists, ..." at first mention, with the card's What is uncertain saying the same.
- **M1 MINOR.** One narrator sentence runs 29 words: "F. C. Burkitt, who edited the Book of Rules, says the little known of his life comes chiefly from Augustine of Hippo, who both criticised his book and drew on it." Past "about 25" (the era 1 batch 3 Anatolius M1 type). Splitting it also gives room for the B1 clause.
- **M2 MINOR.** Card uncertain: "A Donatist council's condemnation of him around 380 is not found in the sources used here." The card raises a claim the reader has never met in order to say it is unsourced. Its only basis is the census and the project's own vendoring header (Burkitt file l.6 to 7), which records.json already logs as an absent detail. This is status-announcement register (Style Guide 1.11; the era 1 Tacitus M3 type). Drop it from the card and keep it in absent_details.
- **M3 MINOR.** records.json contested_claim "Whether Tyconius was right or inconsistent ..." gives no second side. Augustine and Parmenian, as Augustine reports him, are both against Tyconius, and the entry says no writing of Tyconius on his own choice survives. A contested record needs two named sides. Either reframe it as an absent detail (Tyconius's own case is lost with Bellum Intestinum) or tag the claim Documented as Augustine's verdict.

---

## 4. Cyril of Jerusalem (MAJOR)

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | PASS in the brief, with M1; FAIL in the card (B2) |
| 2 | Quotes verbatim | FAIL (B1) |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS in the brief; card M2 |
| 5 | No role for a witness | PASS (Gifford, Touttée, Reischl named) |
| 6 | Partisan witness named and marked | PASS ("Jerome of Strido is hostile"; "Gifford, who defends Cyril") |
| 7 | Contested shown both sides, not settled | PASS (ordination, deposition, 381, prophecy, Mystagogic authorship) |
| 8 | Common names placed | PASS (Maximus and Acacius placed by see); G-M1 in the card |
| 9 | One term | PASS |
| 10 | Story, scene, in-place disputes, length | PASS (opens on the cross of light; 2:27) |
| 11 | grade_text | PASS |
| 12 | Card order and caveat repeated | PASS |
| 13 | Audio tags | PASS |
| 14 | List line; Who test | PASS (census row held) |

**Quotes**
- Sozomen IV.5, the cross "from Calvary to the Mount of Olives"; "Men, women, and children ... ran to the church, where they sang hymns to Christ" (`npnf202` l.32775 region). Exact in substance.
- Gifford: the letter "written on the 7th of May, 351" (`npnf207` l.764 to 767). Jerome's Chronicle as Gifford quotes it, and "strongly marked by personal prejudice" (l.640 to 657). "irreconcileable, and both improbable" (l.782 region). "no satisfactory evidence that he ventured to foretell any miraculous interposition" (l.1140). Lent 348 (chapter IX, l.4125 onward; l.12333). Three exiles: "a third time deposed and driven from Jerusalem, probably in the year 367" (chapter I). Touttée rejects the 381 change: "though the term ὁμοούσιος is not used" (chapter I, l.1326 to 1336 region). Jerome's eight years and the Roman Martyrology's 18 March (l.1360 to 1370 region). All exact.
- "We comprise the whole doctrine of the Faith in a few lines" (Cat. V.12, l.8818). "here is Golgotha to confute me, near which we are now assembled" (Cat. XIII.4, l.14405). Exact.
- "was some time ago canonically ordained by the bishops of the province"; card "has in several places fought a good fight against the Arians" (synodical letter of 382, Theodoret V.9, `npnf203` l.16043). Exact.
- "owing to fear" and the appeal against ecclesiastical usage (Socrates II.40, `npnf202` l.9430 to 9445). "having retracted his former opinion" (Socrates V.8, l.12258). The famine sale, the actress and "under this pretext" (Sozomen IV.25, l.34716). Exact.
- Card: "bishop of Jerusalem often expelled by the church, and at last received" (Lives 112, `npnf203` l.35307 region). "seized some small occasion" (Theodoret II.22, l.8988). The robe "bought ... by a certain stage dancer" (II.23, l.10746). Exact.
- Card: "Testimony of Cyril, Bishop of Jerusalem." **Not exact** (B1).

**Findings**
- **B1 BLOCKING.** Item 2. Card legacy, traces: Theodoret "quotes his fourth lecture as the 'Testimony of Cyril, Bishop of Jerusalem.'" The vendored heading reads "Testimony of Cyril, bishop / Jerusalem." (`npnf203` l.24428 to 24429), with lower-case "bishop" and no "of". The quote silently corrects and recapitalises the source. The heading is also in Theodoret's Dialogues (Eranistes), "From his fourth catechetical oration concerning the ten dogmas" (l.24431). That work is not in the card's Sources, which list only Theodoret's Church History. Fix: drop the quotation marks ("Theodoret of Cyrus, in his Dialogues, cites the fourth lecture as a testimony of Cyril, bishop of Jerusalem") and add the Dialogues to the Theodoret source entry.
- **B2 BLOCKING.** Item 1, loose "no". Card uncertain: "No source gives his birth, family or schooling." Gifford, the card's own main source, says "One member only of Cyril's family is mentioned by name, his sister's son Gelasius" (`npnf207` l.586 to 588). Theodoret names Gelasius of Caesarea too (`npnf203` l.15861). records.json's absent_details note itself mentions the nephew. The claim is false against the Library (the era 1 Josephus B1 type), and it is unqualified ("No source", not "no source used here"). Fix: "No source used here gives his birth, parents or schooling. Gifford names one relative, his sister's son Gelasius, whom Cyril made bishop of Caesarea."
- **M1 MINOR.** "He died in 386." is told with no witness. The year is Gifford's reckoning from Jerome's "eight consecutive years, in the reign of Theodosius" (`npnf203` l.35307 region; `npnf207` l.1360 to 1370 region). The pattern tells Widely Accepted points "plainly with the witness named". Fix: "Jerome says he held his see eight more years under Theodosius, and Gifford reckons he died in 386."
- **M2 MINOR.** Card uncertain items open on verbless labels and dispute announcements: "How he became bishop is disputed." and "Why Acacius deposed him." (the era 1 batch 3 Peter M1 type; Style Guide 1.2 and 1.3). Fix: lead with the witnesses ("Socrates of Constantinople and Sozomen say ...") and drop the label sentences.

---

## 5. Apollinaris of Laodicea (MAJOR)

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | PASS, with M1 |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS in the brief; card M4 |
| 5 | No role for a witness | PASS (Lietzmann, Browne and Swallow, Ullman, Schaff, Percival, Richardson named) |
| 6 | Partisan witness named and marked | PASS ("His teaching on Christ reaches us mostly through opponents"; Gregory "who wrote against him"; Theodoret "an opponent" in the card) |
| 7 | Contested shown both sides, not settled | PASS in the brief (George's reason, the Julian paraphrases with Lietzmann's verdict); card M2 |
| 8 | Common names placed | PASS (Epiphanius placed at Laodicea; Athanasius of Alexandria; Julius of Rome; the two Gregorys) |
| 9 | One term | PASS |
| 10 | Story, scene, in-place disputes, length | PASS (opens on the Dionysus hymn; 2:30, at the ceiling) |
| 11 | grade_text | PASS |
| 12 | Card order and caveat repeated | PASS |
| 13 | Audio tags | PASS |
| 14 | List line; Who test | PASS (census row held) |

**Quotes** (all exact)
- The scene: Epiphanius the sophist's hymn to Dionysus, the uninitiated told to go out, father and son staying, Theodotus ejecting and then restoring them "by tears and fasting" (Sozomen VI.25, `npnf202` l.39040 to 39070 region). George's expulsion over Athanasius (same chapter). Songs "at their daily labor, and women ... at the loom". Damasus and Peter at the Roman council, with the note "Held a.d. 377 (Rade), 374 (Hefele)".
- Born at Laodicea to a father from Alexandria; George over the friendship with Epiphanius, or George's wavering creed; "God the Word himself being in the place of a mind"; the Trinity point (Socrates II.46, l.9921 to 9965). Moses in heroic verse and the Gospels as Platonic dialogues (III.16, l.9160 region). Sozomen V.18, the epic of Hebrew antiquities and other works (l.36696 region); card "the writings of Apolinarius would be held in as much estimation as those of the ancients" (same place).
- "For that which He has not assumed He has not healed" (Gregory, Ep. 101, `npnf207` l.44691). Card "the boldness of the Apollinarians" (Ep. 202, l.44513). The pamphlet (l.44521 to 44545). Ullman's view (translators' note, l.44443 to 44448).
- Fragment 81: "εἰ ἀνθρώπῳ (φησὶ) συνήφθη ὁ θεός, τέλειος τελείῳ, δύο ἂν ἦσαν, εἷς μὲν φύσει υἱὸς θεοῦ εἷς δὲ θετός" (Lietzmann l.11479 to 11480). The modern telling is faithful and is not presented as a quote.
- "Although he instructed me in the holy scriptures, I never embraced his disputable doctrine as to their meaning" (Jerome, Letter 84.3, `npnf206` l.18994 region).
- Lietzmann: the destruction of the dogmatic works, and the works saved under the names of Gregory Thaumaturgus, Julius and Felix of Rome and Athanasius (l.4094 to 4160). Sozomen the more credible on the paraphrases (l.2566 to 2577). October 346 (l.479, 806). 377 (l.560). Perhaps a rival bishop from 360 (l.488 to 490). Death year unknown, with Gregory of Nyssa's book written after 385 presuming him alive (l.3484 to 3488). The Theodotus expulsion aimed at the family's Nicene stand (l.754 to 768).
- Card: "the first to apply the results of the Nicene controversy to Christology proper" (Schaff in `npnf214` l.14084 to 14085). "the doctrine of the one nature of the Flesh and of the Godhead" (Theodoret V.3, `npnf203` l.15481 to 15482). "assumed a mask of piety" (l.15448). Constantinople 381, canon 1, names "that of the Apollinarians" (`npnf214` l.13960 to 13976).

**Findings**
- **M1 MINOR.** "Sozomen gives all of it to the son, with an epic of Hebrew history." Sozomen V.18 does not mention the Moses verse or the Gospel dialogues. He credits Apolinarius with a different set of works (an epic on Hebrew antiquities in twenty-four parts, comedies, tragedies, odes) and never mentions the father. "All of it" says Sozomen gave the son the works Socrates gives the father. The card's "Sozomen gives all the work to the son" has the same slip. Fix: "Sozomen names only the son, and gives him an epic of Hebrew history, plays and odes."
- **M2 MINOR.** Card `dates`: "condemned at Rome in 377" is told plainly. Hartranft's note at Sozomen VI.25 gives "377 (Rade), 374 (Hefele)" (`npnf202`, the council note in VI.25). The brief rightly says "in 377 by Lietzmann's date". Fix: "condemned at Rome in 377, by Lietzmann's date (Hefele, 374)", or give the second date in What is uncertain.
- **M3 MINOR.** Card keyWorks, Against Porphyry: "which Jerome of Strido calls among the best of his works". Jerome says the thirty books "are generally considered as among the best of his works" (Lives 104, `npnf203` l.41382 region). He reports a general judgment and does not give his own. Fix: "which Jerome says were generally counted among his best works".
- **M4 MINOR.** Card uncertain items open on verbless labels: "Who rewrote Scripture in Greek forms under Julian.", "Why George of Laodicea put him out.", "What he taught about Christ's flesh." These are the same type as Cyril M2 (Style Guide 1.2 and 1.3). Fix: lead each with its witnesses ("Socrates gives the verse of the books of Moses to the father ...").

---

## Summary

| Profile | Blocking | Minor |
|---|---|---|
| All (G-M1, Sozomen in cards) | 0 | 1 |
| Damasus of Rome (MAJOR) | 1 (B1) | 5 (M1 to M5) |
| Priscillian (MAJOR) | 2 (B1, B2) | 5 (M1 to M5) |
| Tyconius | 1 (B1) | 3 (M1 to M3) |
| Cyril of Jerusalem (MAJOR) | 2 (B1, B2) | 2 (M1, M2) |
| Apollinaris of Laodicea (MAJOR) | 0 | 4 (M1 to M4) |
| **Total** | **6** | **20** |

Apollinaris of Laodicea clears R1 on its blocking items; its minors are small card fixes. The other four need a targeted round-2 recheck of the blocking items listed, against these findings only.
