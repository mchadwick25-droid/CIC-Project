# R1 review: eight Who profiles, era 1 batch 2 (Church Family Tree)

Reviewer: independent, first sight of these drafts. Bar: `Who_Profile_Pattern.md` review checklist 1 to 14, `CLAUDE.md` "Trust and source fidelity" and "Accessible and rigorous", and Mark's batch 1 rulings (Decision-Log, 2026-11-12: majors capped at 2:30, about 405 words; non-majors 1 to 2 minutes, at most about 324 words). I did not edit the drafts. I made no paid calls of any kind.

Method. Every quotation in the briefs and cards was searched in the vendored file with whitespace-tolerant matching (`wsfind.py`), then read in context, with translator and editor notes nearby. Every factual sentence was checked against the passage it rests on. I grepped the whole of `cic/texts/` before passing any "only", "alone", "never" or single-witness line. Readability came from `engine.m1.gates.grade_text`, run locally with no model call. Length assumes 162 words a minute. Line numbers point to the vendored files under `cic/texts/`.

Applies to all eight:
- The audio scripts match the briefs word for word once tags are removed. Each opens with `[calmly]`, and `[warmly]` sits before the closing line only. No tags appear in the briefs or cards. Item 13 passes everywhere.
- `grade_text` passes for all eight (FK at most 10, Flesch at least 60). All eight score below FK 8. None reads as choppy, so this is noted, not raised.
- No sentence in the narrator's own prose runs past 25 words. The two long sentences (Tacitus on Christus, 27 words; Tatian on the "barbaric writings", 26) are quotations.
- Card fields are in Mark's order. No card has a "links on the map" field, which is correct for a missing field. As in batch 1, the outside-witness `label` sits above `knownFor`, not beside `role`. Check on the page.
- Lengths. The four proposed majors run 401 to 405 words (2:28 to 2:30), inside the cap. The four non-majors run 315 to 321 words (1:56 to 1:58), inside 2:00. Dionysius sits exactly at the cap.
- The major proposals (Tatian, Hippolytus, Novatian, Dionysius) are reasonable on the record: two founded or led a lasting church body, and two are main writers of their century. That call is Mark's.
- Item 14, list lines (report only, not fixed). In `cft-website/index.html`: Dionysius of Alexandria (l.34000), Tatian (l.34568), Pontius the Deacon (l.34741) and Novatian (l.35463) have people-list lines. Hippolytus has two, under two display names: "Hippolytus" (l.35987) and "Hippolytus of Rome" (l.40315). Bardaisan has no person line. His tradition "Bardaisan and the Bardaisanites" (l.40364) lists Philip. Tacitus appears only as a source row, "Outside view" (l.32593). Suetonius does not appear. Every subject passes the Who test. Tacitus and Suetonius are historians, not polemicists, and both are named as outside witnesses in the era 2 scan ruling.

| Profile | Words | Est. length | FK | Flesch |
|---|---|---|---|---|
| Tacitus (outside witness) | 321 | 1:58 | 7.8 | 61.6 |
| Suetonius (outside witness) | 315 | 1:56 | 7.3 | 66.9 |
| Tatian (proposed major) | 402 | 2:28 | 7.9 | 63.3 |
| Bardaisan of Edessa | 321 | 1:58 | 7.8 | 62.8 |
| Hippolytus of Rome (proposed major) | 401 | 2:28 | 7.2 | 65.1 |
| Novatian (proposed major) | 402 | 2:28 | 7.7 | 64.2 |
| Pontius the Deacon | 318 | 1:57 | 6.7 | 71.8 |
| Dionysius of Alexandria (proposed major) | 405 | 2:30 | 7.0 | 67.8 |

---

## 1. Tacitus (Outside witness)

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | PASS, with minor overreach (M1, M4) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS, with minor points (M2, M3) |
| 5 | No role for a witness | PASS |
| 6 | Partisan witness marked | PASS. Tacitus's own hostility is stated. Tertullian is placed as a defender of the Christians |
| 7 | Contested both sides | PASS (Gibbon and Schiller against McGiffert) |
| 8 | Common names | PASS (Tertullian of Carthage, Eusebius of Caesarea, Sulpicius Severus with Aquitania) |
| 9 | One term | PASS |
| 10 | Story, scene, length | PASS (1:58) |
| 11 | grade_text | PASS |
| 12 | Card order and caveat | PASS |
| 13 | Audio tags | PASS |
| 14 | List line; objective historian | PASS on the label. No people-list line (source row only, l.32593) |

**Quotes** (all Annals 15.44 quotations are on the file's single text line, `tacitus_annals-15-44_church-brodribb1876.txt` l.68)
- "fastened the guilt" / "a class hated for their abominations, called Christians by the populace.": exact.
- "to serve as a nightly illumination, when daylight had expired.": exact.
- "Christus, from whom the name had its origin, suffered the extreme penalty during the reign of Tiberius at the hands of one of our procurators, Pontius Pilatus.": exact.
- "a most mischievous superstition.": exact.
- "an immense multitude" / "hatred against mankind." / "to glut one man's cruelty.": exact.
- "most loquacious in falsehood": exact (Tertullian, To the Nations I.11, anf03 l.10093–10094).
- "In this way," ... "cruelty first began to be manifested against the Christians.": exact (Sulpicius Severus, Sacred History II.29, npnf211 l.10666 region).
- Card: "where Tacitus and Suetonius end": exact once the page header "VI PREFACE." is stripped (Yonge, ammianus file l.759–764). Other card quotes as above.

**Findings**
- **M1 MINOR.** "Even Romans began to pity them, because they seemed to die 'to glut one man's cruelty.'" Tacitus says "even for criminals who deserved extreme and exemplary punishment, there arose a feeling of compassion" (l.68). He does not say who felt it, and his "even" attaches to criminals who deserved punishment. That clause is itself a mark of his hostility. Fix: "Even for people who deserved the worst, he says, pity arose, because..."
- **M2 MINOR.** "Tacitus was not a Christian, and he did not like them." The paragraph opens on a verdict, and "them" has no plural antecedent. Give the evidence in his words, which the brief already holds ("hated for their abominations").
- **M3 MINOR.** "The Library holds one chapter of his Annals, Book 15, chapter 44." This is status-announcement register (Style Guide 1.11) in a spoken brief. The card's What is uncertain already carries it. Drop it from the brief.
- **M4 MINOR.** "Tacitus does not say where he learned about Christus. Tertullian ... calls him 'most loquacious in falsehood' over a tale he told about the Jews." Tertullian's charge is about the ass's-head story in Histories V (anf03 l.10081–10094). Placing it straight after the Christus limit suggests it bears on the Christus line. Separate the two, or say that Tertullian's complaint concerns the Jews only.
- **M5 MINOR.** Card `place`: "Rome". No vendored source places Tacitus's life or work at Rome. Leave the field absent or name the source.

---

## 2. Suetonius (Outside witness)

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | PASS in the brief. Card date fails (B1) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS, with minor points (M5) |
| 5 | No role for a witness | PASS (Rolfe, Thomson and Forester named) |
| 6 | Partisan witness marked | n/a |
| 7 | Contested both sides | FAIL on the card (B1). Chrestus passes |
| 8 | Common names | PASS in the brief. "Dio" on the card is minor (M1) |
| 9 | One term | PASS |
| 10 | Story, scene, length | PASS (1:56) |
| 11 | grade_text | PASS |
| 12 | Card order and caveat | PASS |
| 13 | Audio tags | PASS |
| 14 | List line; objective historian | PASS on the label. No list line anywhere on the site (M7) |

**Quotes**
- "Since the Jews constantly made disturbances at the instigation of Chrestus," ... "expelled them from Rome.": exact once Rolfe's footnote marker "*" is stripped (Claudius 25.4, Rolfe l.25908).
- "inflicted punishments on the Christians, a sort of people who held a new and impious superstition.": exact once the footnote marker "[577]" is stripped (Nero 16, Thomson-Forester l.11612–11614).
- "Another form of Christus.": exact (Rolfe's note, l.25866–25871 region).
- "one Chrestus.": exact (Thomson-Forester l.10640).
- Card: same as above. records.json "a new and mischievous superstition" matches Rolfe (l.28522–28523).

**Findings**
- **B1 BLOCKING.** Card `dates`: "Born late in the reign of Vespasian". This takes the Thomson-Forester preface (l.49–51) as settled. Rolfe, the card's own main witness, reports that Mommsen dates the birth to 77 and Macé "with somewhat greater probability to 69" (Rolfe l.155–158). 69 is the first year of Vespasian's reign, not late in it. A contested date is told as settled (item 7). Fix: "Born about 69 or 77 (Rolfe reports both); dismissed by Hadrian about 121", or move the birth to What is uncertain with both names.
- **M1 MINOR.** Card uncertain: "The notes to Thomson and Forester's edition add that Dio says Claudius did not expel the Jews, only forbade their meetings." The same note first cites Luke, Acts 18:2, for the expulsion (Thomson-Forester l.20383–20386). Giving only Dio leaves the doubt with the last word. "Dio" is also a common name. McGiffert writes "Dion Cassius" (npnf201 l.13817). Use "Dio Cassius" and give Luke as well.
- **M2 MINOR.** "Their translation says 'one Chrestus.' Rolfe notes that the Latin has no such word". Rolfe's note argues from "the absence of quodam" and does not mention Thomson and Forester's rendering. The order makes it sound like Rolfe answering them. Write "Rolfe notes that the Latin has no word for 'one' here".
- **M3 MINOR.** Card legacy, remembered: "His life of Vespasian also tells of Josephus's prediction that Vespasian would rule." This is a fact about his work, not how he is remembered. Move it or drop it.
- **M4 MINOR.** records.json contested_claim: both sides are given to Rolfe. Name the Thomson-Forester notes for Christ, and say that no vendored witness holds the other reading, only Rolfe's allowance.
- **M5 MINOR.** "Whether 'Chrestus' means Christ is argued." (card) and "Rolfe also traces his reach." (brief) are openers that announce rather than tell. The card line also makes a present-tense claim on 1909–1914 witnesses (the batch 1 Josephus B2 point).
- **M6 MINOR.** "Paulinus" carries a role and not a place, and the vendored source gives only "his secretary Paulinus" (Rolfe l.380–382). Log the gap. "The battle of Betriacum" is given without context for a general listener.
- **M7 MINOR.** Item 14. Suetonius has no list line in `cft-website/index.html`. Confirm where outside witnesses are listed.

---

## 3. Tatian (proposed major)

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | FAIL on the card (B1). Minor points M2, M3, M8 |
| 2 | Quotes verbatim | PASS. "through four" is minor (M6) |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS, with minor points (M5) |
| 5 | No role for a witness | PASS. "Later writers" is minor (M2) |
| 6 | Partisan witness marked | PASS for Irenaeus. Hippolytus is minor (M1) |
| 7 | Contested both sides | FAIL (B1: the life reconstruction is told as settled on the card, and its named witness's verdict is left out) |
| 8 | Common names | MINOR (M7: Marcion, Saturninus, Zahn, Harnack) |
| 9 | One term | PASS |
| 10 | Story, scene, length | PASS (major, 2:28) |
| 11 | grade_text | PASS |
| 12 | Card order and caveat | PASS |
| 13 | Audio tags | PASS |
| 14 | List line, Who | PASS (l.34568) |

**Quotes**
- "retiring by myself, I sought how I might be able to discover the truth.": exact (Address 29, anf02 l.6970).
- "certain barbaric writings, too old to be compared with the opinions of the Greeks, and too divine to be compared with their errors.": exact (anf02 l.6971–6972).
- "born in the land of the Assyrians": exact (Address 42, anf02 l.7460).
- "the most admirable Justin.": exact (Address 18, anf02 l.6526; the editor's bracketed note follows).
- "separated from the Church," / "like the followers of Valentinus," / "corruption and fornication,": exact (Irenaeus I.28.1, anf01 l.33666 region).
- "I know not how.": exact (Eusebius IV.29.6, npnf201 l.26425).
- "very widely if not universally read in the Syriac churches.": exact (Hogg, anf09 l.1928–1929).
- "held in respect in the churches.": exact (anf09 l.1922–1923).
- "These things, O Greeks, I Tatian, a disciple of the barbarian philosophy, have composed for you.": exact once the editor's bracket "[Comp. cap. xxix. p. 77, supra.]" is stripped (anf02 l.7458–7460).
- "through four": not in any vendored file as a gloss (M6).
- Card quotes: as above.

**Findings**
- **B1 BLOCKING.** Card `dates`: "Broke with the church at Rome about 172". Card `place`: "taught at Rome". Card uncertain: "His life is told in two ways. McGiffert reports that Harnack had him at Rome twice ... Zahn had him at Rome once, becoming a heretic in the East." The dates line asserts Harnack's reconstruction as fact, while the card's own uncertain line calls it one of two. The uncertain line also stops before its witness's outcome: McGiffert says Harnack's arguments against Zahn "seem fully to establish his main positions" (npnf201 l.26230–26233). And it leaves out the other named witness in the Library. Hogg says Tatian, "after Justin's death left Rome and returned to Mesopotamia. It was probably here that he issued in Syriac his most important work" (anf09 l.1958–1962). McGiffert also says the "only trustworthy information" in Epiphanius is that Tatian "returned to Mesopotamia and taught for a while there" (l.26211–26214). The brief never says Tatian went East, though his tradition is Syriac Christianity. Fix: dates "Broke with the church about 172 (Eusebius's Chronicle)". In What is uncertain, give Harnack and Zahn with McGiffert's verdict, and Hogg's account of the return to Mesopotamia. Add a contested_claim with both sides named. One clause in the brief on the return East would also tie the Diatessaron paragraph to the Syriac churches.
- **M1 MINOR.** "Hippolytus of Rome gives the same three points in the same order." Refutation VIII.9 (anf05 l.12999–13013) follows Irenaeus almost line for line, and Hippolytus is also an opponent. As written it sounds like independent support. Say that Hippolytus repeats Irenaeus. The records.json "Widely Accepted" tag leans on it.
- **M2 MINOR.** "Later writers made Tatian the founder of the Encratites" names no one. Eusebius does it himself: "their original founder, Tatian" (IV.29.6, l.26425 region), and his Chronicle has "a quo Encratitae" (l.26219–26220). Jerome does it too (npnf203 l.40091–40093). Name them. McGiffert's point also concerns "the particular sect which Irenaeus describes", since he says the word was used "in a wider sense" for several groups (l.26290–26312). The brief's gloss "who refused marriage, meat and wine" is his general description, so keep the two apart.
- **M3 MINOR.** "Eusebius did not know it at first hand" is stated as fact. It is McGiffert's reading. He reports that Lightfoot read "I know not how" as disapproval, not ignorance (l.26426–26432). The card's "knew the Diatessaron only by name" goes further still, since Eusebius knew what it was. Attribute it to McGiffert and drop "only by name".
- **M4 MINOR.** "Hope Hogg ... concludes that at an early stage it was..." Hogg writes "It would seem, therefore" (anf09 l.1928). His hedge is dropped. Hogg also says "considerably more than half" of the translation is his wife's work (l.2005–2007). "Who translated it from Arabic" is not wrong, but note it.
- **M5 MINOR.** "McGiffert also reports a dispute over its first language." This is a dispute-announcing opener. Both sides are named, which passes item 7. But the two named witnesses lean opposite ways: McGiffert says Harnack "has given very strong reasons" for Greek (l.26461), and Hogg reports "the view favoured by an increasing majority of scholars, that it was written in Syriac" (anf09 l.1996). Give both leanings in one sentence.
- **M6 MINOR.** "called the Diatessaron, 'through four.'" The quotation marks present the drafter's gloss of the Greek as a quotation. The vendored gloss is Isho'dad's "the Combined" (anf09 l.1767), and McGiffert gives only the Greek. Drop the quotation marks, or use the vendored gloss with its owner.
- **M7 MINOR.** Item 8. "Saturninus and Marcion" (brief and card) lacks the identifier Mark ruled on 2026-11-12 ("Marcion of Pontus"; the Bardaisan brief uses it). "Saturninus", "Zahn" and "Harnack" are given without context for a general listener.
- **M8 MINOR.** "At Rome he became a hearer of Justin Martyr, as Irenaeus of Lyon reports". Irenaeus says Tatian was "a hearer of Justin's" but not where (anf01 l.33666 region). Rome comes from Tatian himself ("when sojourning in the city of the Romans", Address 35, anf02 l.7250). Place the attribution so each claim has its own owner.
- **M9 MINOR.** Card otherNames "Tatian the Assyrian". The form appears only in the vendoring header of the Otto file (`tatian_oratio-ad-graecos-grc-lat_otto1851.txt` l.2), not in a source's text. Check it against the census `informalName`.

---

## 4. Bardaisan of Edessa

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | FAIL (B1) |
| 2 | Quotes verbatim | FAIL (B2) |
| 3 | No invention | PASS. M2 is a small overreach in wording |
| 4 | Reading aids | PASS, with a dispute opener folded into B1 |
| 5 | No role for a witness | PASS |
| 6 | Partisan witness marked | FAIL (B1: Eusebius is cast as a hostile witness though he praises Bardaisan) |
| 7 | Contested both sides | FAIL (B1: the order-of-life dispute ends on Epiphanius, though the named witness resolves it) |
| 8 | Common names | PASS for Marcion of Pontus and Epiphanius of Salamis. Minor M5 |
| 9 | One term | MINOR (M7) |
| 10 | Story, scene, length | PASS (1:58) |
| 11 | grade_text | PASS |
| 12 | Card order and caveat | PASS. Sources grouping is minor (M4) |
| 13 | Audio tags | PASS |
| 14 | List line, Who | PASS on the Who test. No person list line (see top) |

**Quotes**
- "What were you talking about?" ... "I heard your voice outside as I was coming in.": NOT exact (B2). Book of the Laws of Divers Countries, anf08 l.67912 region.
- "the new race of us Christians, whom Christ at His advent planted in every country and in every region.": exact (anf08 l.68966).
- "a most skillful disputant in the Syriac tongue.": exact (Eusebius IV.30.1, npnf201 l.26633).
- Card: "Philip and Baryama.": exact (anf08 l.68337).

**Findings**
- **B1 BLOCKING.** "Eusebius of Caesarea and Epiphanius of Salamis, both writers against heresy, tell his story in opposite orders. ... Only later, Epiphanius says, did he fall into the error of Valentinus." The dispute ends with Epiphanius, and the paragraph after it turns to Ephrem's attack. McGiffert, the brief's own named witness, resolves the order. He writes "It is not improbable that he may, as Eusebius says, have been a Valentinian for a time" (npnf201 l.26562), and "It is undoubtedly quite true ... that Bardesanes, after leaving Valentianism, still retained views acquired under its influence" (l.26657). He also reports Hort: Bardaisan "is commonly classed among the Gnostics, but, as Hort shows, without sufficient reason", and "There is no reason to think that he taught a system of æons" (l.26525–26545). Separately, "both writers against heresy" casts Eusebius as a hostile witness, but Eusebius calls Bardaisan "a powerful defender of the faith" (l.26637–26638). The brief therefore reaches the listener through two heresiologists and Ephrem, and stops before the defence and the outcome its own witness gives. Fix: drop "both writers against heresy" for Eusebius, give McGiffert's judgment that Eusebius's order is the likelier one, and add Hort's view in one sentence. Give the records.json contested_claim McGiffert and Hort on Eusebius's side.
- **B2 BLOCKING.** Item 2. The brief reads "'What were you talking about?' he asked. 'I heard your voice outside as I was coming in.'" The source reads "What were you talking about? for I heard your voice outside as I was coming in." (anf08 l.67912 region). The word "for" is silently dropped and a new quoted sentence is begun. Restore it: "'What were you talking about?' he asked, 'for I heard your voice outside as I was coming in.'"
- **M1 MINOR.** "Sozomen says that Bardaisan's son Harmonius set Syriac verse to metre and music." Sozomen writes "It is related that this latter ... was the first to subdue his native tongue to meters and musical laws" (npnf202 l.32085). His hedge is dropped.
- **M2 MINOR.** "Some friends were visiting their brother Shemashgram". The dialogue says "we were calling to pay a visit to our brother Shemashgram". The narrators are named "Philip and Baryama" (anf08 l.68337), and "brother" most likely means a fellow Christian. "Their brother" can be heard as a sibling. Write "Two of his pupils, Philip and Baryama, were visiting Shemashgram".
- **M3 MINOR.** records.json tags "Ephrem knew him only through his followers" Inferential-Thin. This is McGiffert's judgment, stated as "Undoubtedly" (l.26574). Dominant Modern Reconstruction (McGiffert) fits the vocabulary.
- **M4 MINOR.** The card lists the Book of the Laws under "Their own words", yet its own uncertain line says a disciple wrote it. Move it to "Written about them", or label it in the group's heading.
- **M5 MINOR.** Names without context: "Sozomen" (the church historian), "Valentinus", and "Abgar". There are several Abgars of Edessa, and the ANF note identifies this one as Abgar bar Manu (anf08 l.68966).
- **M6 MINOR.** The card's dates "by later Syriac chronicles" are right. Holl's apparatus gives Barhebraeus's death year as 221/2 (Holl Panarion l.26427), against McGiffert's 223. One clause on the card would cover it.
- **M7 MINOR.** Item 9. The title appears as "the Book of the Laws of Countries" in the brief and card, and as "The Book of the Laws of Divers Countries" in the card's source list.

---

## 5. Hippolytus of Rome (proposed major)

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | PASS, with minor points (M1, M2) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS. M3 is minor |
| 5 | No role for a witness | PASS (MacMahon, McGiffert named) |
| 6 | Partisan witness marked | PASS ("He tells Callistus's life as an enemy"; McGiffert's "very bitter opponent") |
| 7 | Contested both sides | PASS (Portus: MacMahon, Döllinger, McGiffert; authorship) |
| 8 | Common names | MINOR (M4) |
| 9 | One term | PASS |
| 10 | Story, scene, length | PASS (major, 2:28) |
| 11 | grade_text | PASS |
| 12 | Card order and caveat | PASS |
| 13 | Audio tags | PASS |
| 14 | List line, Who | PASS. Two display names on the site (M6) |

**Quotes**
- "episcopus": exact. "presbiter": exact once the OCR misreading "presbitcr" is corrected. Liberian catalogue, "Eo tempore Pontianus episcopus et Yppolitus presbiter exoles sunt deportati in Sardinia" (`chronica-minora-liber-genealogus_mommsen1892.txt` l.13078–13079, l.13107).
- "over another church.": exact (Eusebius VI.20.2, npnf201 l.35449).
- "saying that all had their sins forgiven by himself.": exact (Refutation IX.7, anf05 l.13875).
- "from the pen of a very bitter opponent.": exact (McGiffert, npnf201 l.35510).
- "greatly overdrawn,": exact (l.35521).
- "quite worthless.": exact ("is quite worthless", l.35662).
- Card: as above.

**Findings**
- **M1 MINOR.** "He notes that Hippolytus never calls Callistus a bishop, yet calls himself a successor of the apostles." McGiffert says Hippolytus "never recognizes Callistus as bishop of Rome" (l.35666) and "calls himself a bishop" (l.35672–35676). "Successor of the apostles" is Hippolytus's own wording in the Refutation's preface ("we, as being their successors", anf05 l.1130). Credit each part to its owner.
- **M2 MINOR.** "Callistus, he says, was a slave who lost his master's money in a bank". Hippolytus charges that Callistus "made away with all" the deposits (anf05 l.13685), and McGiffert summarises "a dishonest banker" (l.35513). "Lost" softens the charge the enemy actually makes. Tell it as charged.
- **M3 MINOR.** "Callistus called Hippolytus and his party worshippers of two gods." No context is given for what the charge meant. McGiffert names the quarrel: Hippolytus held Callistus a Patripassian, and Callistus answered with "two gods" (l.35517–35518). One clause would do.
- **M4 MINOR.** Item 8. The subject's own first mention in the brief is "Hippolytus", without "of Rome". The opening sentence does place him at Rome, so this is minor (the batch 1 Justin M1 point). "Zephyrinus" (brief) and "Prudentius" (card) have no context.
- **M5 MINOR.** records.json tags "Callistus was a slave, banker and convict who rose to be bishop" Widely Accepted. It rests on one hostile witness, which McGiffert calls "greatly overdrawn". Documented with a note (one hostile witness, groundwork accepted by McGiffert) fits better.
- **M6 MINOR.** Item 14. The site lists him as "Hippolytus" (l.35987) and "Hippolytus of Rome" (l.40315). Report only.

No blocking findings.

---

## 6. Novatian (proposed major)

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | PASS in the brief. Card wording is minor (M2, M3) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS, with a minor thesis opener (M4) |
| 5 | No role for a witness | PASS |
| 6 | Partisan witness marked | FAIL (B1: the Acesius story's partisan source is unmarked). Cornelius passes, marked at once |
| 7 | Contested both sides | PASS on the persecution charge and the martyrdom. B1 covers Socrates's standpoint |
| 8 | Common names | PASS in the brief. Card is minor (M5) |
| 9 | One term | PASS |
| 10 | Story, scene, length | PASS (major, 2:28) |
| 11 | grade_text | PASS |
| 12 | Card order and caveat | PASS |
| 13 | Audio tags | PASS |
| 14 | List line, Who | PASS (l.35463) |

**Quotes**
- "Swear to me by the body and blood of our Lord Jesus Christ that you will never forsake me and turn to Cornelius.": exact (Cornelius in Eusebius VI.43.18, npnf201 l.38767).
- "The Rule of truth requires that we should first of all things believe on God the Father and Lord Omnipotent.": exact (On the Trinity 1, anf05 l.60470).
- "both able and orthodox.": exact (McGiffert, npnf201 l.38244).
- "rustic and very simple men": exact (l.38522).
- "another philosophy.": exact (l.38717).
- "If, as thou sayest, thou hast been led on unwillingly, thou wilt prove this if thou retirest willingly. For it were better to suffer everything, rather than divide the Church of God.": exact (Dionysius in Eusebius VI.45, l.38923).
- "he who is not in the Church of Christ is not a Christian.": exact (Cyprian to Antonianus, anf05 l.33976).
- "Place a ladder, Acesius," ... "and climb alone into heaven.": exact (Socrates I.10, npnf202 l.3720–3721).
- Card: as above.

**Findings**
- **B1 BLOCKING.** "Socrates of Constantinople, who wrote fairly of it, tells a story he heard from a very old man." In I.13 Socrates names that old man. He was "Auxanon, a very aged presbyter of the Novatian church; who when quite a youth accompanied Acesius to the Synod at Nicæa, and related to me what I have said concerning him" (npnf202 l.3855–3857). Hartranft's note to Sozomen I.22 also identifies him as Socrates's source for I.10 (l.28061–28062). So the story comes from a Novatian partisan, and the brief presents its source as neutral. "Who wrote fairly of it" also tells as settled a question the translator says has "considerable difference of opinion". Baronius, Labbé and others held Socrates a Novatian, while Valesius, "followed by most of the more recent writers", held him impartial (npnf202 l.935–1040). The card has that dispute, but the brief settles it. Fix: "Socrates of Constantinople tells a story he had from Auxanon, an aged Novatian presbyter who had gone to Nicaea with Acesius." Either drop "who wrote fairly", or write "whom Valesius and most later writers think fair". Add Auxanon to the card's uncertain line.
- **M1 MINOR.** records.json tags the Acesius story "Socrates I.10 (one witness, from an old man)", Inferential-Thin. Sozomen I.22 also tells it (npnf202 l.28053–28089), though from Socrates. A direct report is not an inference either, and the same applies to the oath (Cornelius). Documented with a note, naming the source chain, fits the vocabulary. The card's "says no other writer records it" is correctly given as Socrates's own claim.
- **M2 MINOR.** Card: "McGiffert sees no reason to doubt Novatian's own word." McGiffert writes "Novatian may well have been urged against his will" (npnf201 l.38913). His hedge is turned into certainty. Write "McGiffert thinks Novatian may well have been urged against his will".
- **M3 MINOR.** Card keyWorks: On the Jewish Meats "written while he was in retirement during the persecution of Decius". Coxe says it "seems to have been composed during the Decian persecution" (anf05 l.60321). The hedge is dropped, and "in retirement" has no source at that point.
- **M4 MINOR.** "The quarrel was about discipline." The paragraph opens on a thesis.
- **M5 MINOR.** Card: "Cornelius" has no identifier at its first mention in the card ("his enemies, Cornelius and those on his side"). "Lardner", "Neander", "Valesius" and "Baronius" have no context. Lardner's line reaches us through Coxe (anf05 l.60304–60306), so say so.

---

## 7. Pontius the Deacon

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | PASS |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS. The death scene's trees, blindfold and shaking hand are all in Life 18 |
| 4 | Reading aids | PASS |
| 5 | No role for a witness | FAIL (B1) |
| 6 | Partisan witness marked | PASS ("He writes as an admirer and praises Cyprian at every turn") |
| 7 | Contested both sides | PASS. M1 is minor |
| 8 | Common names | PASS (Cyprian of Carthage, Jerome of Strido) |
| 9 | One term | PASS |
| 10 | Story, scene, length | PASS (1:57) |
| 11 | grade_text | PASS |
| 12 | Card order and caveat | PASS |
| 13 | Audio tags | PASS |
| 14 | List line, Who | PASS (recorder; l.34741) |

**Quotes**
- "with hand expanded and flattened like a blade, he imitated the stroke of the accustomed punishment.": exact (Life 12, anf05 l.28071 region).
- "could also have chosen me to share his passion!": exact as a substring of "would that he could also have chosen me to share his passion!" (l.28058–28060).
- "Much and excessively I exult at his glory; but still more do I grieve that I remained behind.": exact (Life 19, l.28302).
- Card: "a notable volume.": exact (Jerome, Lives 68, npnf203 l.40831–40833). Hartel's "Pontio diacono uulgo adscripta" supports "commonly attributed" (Hartel l.40260).

**Findings**
- **B1 BLOCKING.** Item 5. Card uncertain: "The note to Jerome in the English edition says he died about 260." This is a role standing in for a named witness, which the pattern rules out ("never 'his editor', 'the translator'"). The npnf203 Lives of Illustrious Men is "Translated, with introduction and notes, by Ernest Cushing Richardson" (npnf203 l.688). Write "Ernest Cushing Richardson, in a note to his translation of Jerome, gives his death as about 260."
- **M1 MINOR.** "He tells how Cyprian sold whole estates to help the poor." Benson reports Otto Ritschl's view that the gardens were confiscated later, and that Pontius "mistakes this for charitable sale now" (Benson l.2899–2906). A clause on the card's uncertain list would cover it.
- **M2 MINOR.** records.json tags "Pontius died a martyr" Inferential-Thin with "Coxe note, no source given". This is a reported tradition with no witness behind it, not an inference from evidence. Model it as an honest limit or absent detail (`kind: absence`), per `CLAUDE.md`'s note on "Not Attested".

---

## 8. Dionysius of Alexandria (proposed major)

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | PASS, with minor overreach (M1) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS, with a minor dispute opener (M5) |
| 5 | No role for a witness | PASS (Robertson, McGiffert named) |
| 6 | Partisan witness marked | PASS (his own defence; "a bishop praising his own people") |
| 7 | Contested both sides | PASS in the brief. records.json is minor (M2) |
| 8 | Common names | PASS for Dionysius of Rome, Athanasius of Alexandria and Paul of Samosata. Minor M4 |
| 9 | One term | PASS |
| 10 | Story, scene, length | PASS (major, 2:30, at the cap) |
| 11 | grade_text | PASS |
| 12 | Card order and caveat | PASS |
| 13 | Audio tags | PASS |
| 14 | List line, Who | PASS (l.34000) |

**Quotes**
- "as if on a preconcerted signal, arose with one impulse,": exact (letter to Germanus, Eusebius VI.40.6, npnf201 l.37718).
- "better to suffer everything," ... "rather than divide the Church of God.": exact (VI.45, l.38923; only the comma between the two parts is removed).
- "The most of our brethren were unsparing in their exceeding love": exact (VII.22.7, l.41084).
- "deserted those who began to be sick.": exact (VII.22.10, l.41121).
- "I could not venture to reject the book, as many brethren hold it in high esteem,": exact (VII.25.4, l.41418).
- "uses barbarous idioms.": exact (VII.25.26, l.41636).
- Card: no further quotations. Taposiris, the frumentarius and the wedding feast are in VI.40.2–9 (l.37640–37718).

**Findings**
- **M1 MINOR.** "But he compared its Greek with the Gospel of John, and found that its writer 'uses barbarous idioms.' So he could not accept that this John was the apostle." The card adds "His judgment ... rests on comparing its Greek with the Gospel of John." Dionysius gives several grounds. He judges "from the character of both, and the forms of expression, and the entire execution of the book" (VII.25.8, l.41460). He also argues from the evangelist never naming himself, and from the vocabulary shared by the Gospel and the Epistle but missing from the Revelation (VII.25.8–23). Only then does he turn to the Greek (25.24–26). "So" makes the Greek the sole cause. Write "Among his reasons was its Greek" and drop "rests on" from the card.
- **M2 MINOR.** records.json contested_claim: "Dionysius, from its Greek, against those many brethren who held it in high esteem as John's". The brethren esteemed the book, and Dionysius does not say they held it the apostle's. He also reports that "some before us" rejected the book altogether and gave it to Cerinthus (VII.25.1–2, l.41418 region). Restate the sides as Dionysius reports them.
- **M3 MINOR.** Later reception. The card's "How they're remembered" gives only Athanasius's defence. The Library holds a dissent: Basil, Letter 9, charged Dionysius with sowing the seeds of the Anomoean heresy (Jackson's note, npnf208 l.14431). Robertson also says the Arians "had good prima facie ground for their appeal", and calls one of Athanasius's defences "scarcely tenable" (npnf204 l.29269, l.29291). Robertson still sides with Athanasius ("Athanasius, not the Arians, had the right to claim him"), so the brief is not misleading. The card would be fuller with Basil.
- **M4 MINOR.** Names without context: "Germanus" (McGiffert says his see is unknown, npnf201 l.37606–37608, so log the gap), "Origen" (bare here, though the Hippolytus brief gives "Origen of Alexandria"), "Sabellius", "Gallienus", and "Nepos" on the card.
- **M5 MINOR.** "His letters against Sabellius brought a dispute of his own." This opener announces a dispute before telling it (the batch 1 Ignatius M5 pattern).
- **M6 MINOR.** records.json tags "Christians nursed the sick in the plague" Widely Accepted on one partisan witness. Documented with a note (one witness, a bishop on his own flock) fits better.

No blocking findings.

---

## Summary

| Profile | Blocking | Minor |
|---|---|---|
| Tacitus | 0 | 5 |
| Suetonius | 1 | 7 |
| Tatian | 1 | 9 |
| Bardaisan of Edessa | 2 | 7 |
| Hippolytus of Rome | 0 | 6 |
| Novatian | 1 | 5 |
| Pontius the Deacon | 1 | 2 |
| Dionysius of Alexandria | 0 | 6 |
| **Total** | **6** | **47** |

Blocking findings in one line each:
1. Suetonius B1: the card's "Born late in the reign of Vespasian" is told as settled, though Rolfe reports 77 (Mommsen) and the more probable 69 (Macé).
2. Tatian B1: the card's "Broke with the church at Rome about 172" asserts Harnack's reconstruction. Its uncertain line omits McGiffert's verdict and Hogg's account of the return to Mesopotamia.
3. Bardaisan B1: the order-of-life dispute ends on Epiphanius, and Eusebius is cast as a heresy-writer. McGiffert (with Hort) resolves for Eusebius's order, and Eusebius calls Bardaisan "a powerful defender of the faith".
4. Bardaisan B2: the opening quote drops "for" and splits one sentence into two.
5. Novatian B1: the Acesius story's "very old man" is Auxanon, a Novatian presbyter who went to Nicaea with Acesius (Socrates I.13). The brief marks him as neutral and calls Socrates fair, though that is disputed.
6. Pontius B1: "The note to Jerome in the English edition" is a role standing in for Ernest Cushing Richardson.

Patterns that recur, each already counted above:
- **Dispute outcomes.** Twice a dispute is told to its end on the wrong side, or without the verdict of the witness the profile itself names (Tatian, Bardaisan). This is the batch 1 Ignatius pattern.
- **Sources of sources.** A witness's own informant or dependence goes unmarked: Auxanon behind Socrates, and Hippolytus repeating Irenaeus on Tatian.
- **records.json.** Single direct reports are still tagged Inferential-Thin (Novatian's oath and Acesius, Bardaisan's Ephrem, Pontius's martyrdom), the same pattern batch 1 found.
- **Hedges dropped.** Hogg's "It would seem", Sozomen's "It is related", McGiffert's "may well have been" and Coxe's "seems to have been".
- **"Only" lines.** All were grepped against the whole Library. None fails in a brief. The one single-witness claim that fails is records.json "one witness" for the Acesius story, since Sozomen I.22 retells it.
