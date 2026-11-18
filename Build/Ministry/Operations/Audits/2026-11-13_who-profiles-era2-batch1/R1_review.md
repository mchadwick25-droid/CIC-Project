# R1 review: nine Who profiles, era 2 batch 1 (Church Family Tree)

Reviewer: independent, first sight of these drafts. Bar: `Who_Profile_Pattern.md` review checklist 1 to 14 and the Style Guide sections it cites; `CLAUDE.md` "Trust and source fidelity" and "Accessible and rigorous"; Mark's rulings in the Decision-Log (2026-11-12: majors capped at 2:30, about 405 words; non-majors 1 to 2 minutes, at most about 324 words; major is a cap, not a target). Majors by the coordinator's call: Arius, Pachomius, Antony the Great, Frumentius, Hilary of Poitiers. Not major: Melitius of Lycopolis, Aetius of Antioch, Lucifer of Cagliari, Hilarion of Gaza. The findings of the two era 1 R1 reviews were read first and checked for again. I did not edit the drafts. I made no model calls and no paid calls of any kind.

Method. Every quotation in the briefs and cards was searched in its vendored file with whitespace-tolerant matching (a small helper that strips XML tags, collapses whitespace and straightens quote marks), then read in context with the translator's and editor's notes nearby. Every factual sentence was checked against the passage it rests on. I grepped the whole of `cic/texts/` before passing any "only", "first", "never", "one" or single-witness line. Readability came from `engine.m1.gates.grade_text`, run locally with no model call. Length assumes 162 words a minute. Line numbers point to the vendored files under `cic/texts/`.

Applies to all nine:
- The audio scripts match the briefs word for word once tags are removed. Each opens with `[calmly]`. No tags appear in the briefs or cards. In seven scripts `[warmly]` sits before the closing line. In Antony and Hilarion it sits before the whole last paragraph (374 and 259 characters from the end; the approved era 1 scripts run 88 to 136). Counted as a minor under each.
- `grade_text` passes for all nine (FK 6.9 to 8.5, Flesch 60.6 to 70.8). Melitius, Arius, Frumentius and Lucifer sit just above the Flesch floor (60.6 to 60.9). Any clause added by the fixes below should be re-scored. None reads as choppy.
- No narrator sentence runs past 25 words. The two long sentences are quotation-led: Arius's opening (33 words, mostly Socrates's quote) and the Pachomius angel line (28 words, 16 of them narrator).
- Lengths. The five majors run 380 to 404 words (2:21 to 2:30), inside the cap. The four non-majors run 285 to 324 words (1:46 to 2:00). Hilarion sits exactly at 324. None reads as stretched, though the last Frumentius paragraph is thin (Frumentius M4). The major calls are reasonable on the record: two founders of monastic movements, the presbyter whose name the controversy carries, the first bishop of a new church, and the chief Latin writer of the Nicene side. That call is Mark's.
- Card fields are in Mark's order except Aetius, whose `keyWorks` comes before `briefLength`. No card has a "links on the map" field, which is correct for a missing field. Antony (`ownWords: []`) and Hilarion (`otherNames: []`, `ownWords: []`) carry empty fields where the field should be absent. Counted under each.
- One term (item 9), report only. Five card `tradition` values differ from the site's tradition names in `cft-website/index.html`: Hilary "Gallic Nicene" (site: "The Gallic Nicene Episcopate", l.39196), Lucifer "Luciferian" ("The Luciferians", l.79588), Pachomius "Desert Monasticism (Pachomian)" ("Desert Monasticism", l.36188), Frumentius "Aksumite" ("Aksumite Christianity (conversion era)", l.38491), Arius "Arianism" (the nearest is "Homoian ('Arian') Christianity", l.39751). Settle which name the card uses when the profiles are placed.
- Item 14, list lines (report only, not fixed). People-list lines exist for Pachomius (l.36565), Hilary of Poitiers (l.39251), Aetius of Antioch (l.39942), Melitius of Lycopolis (l.79549) and Lucifer of Cagliari (l.79644). Arius, Antony, Frumentius and Hilarion have none. Their traditions' people lists hold others: Desert Monasticism lists Pachomius, Evagrius and John Cassian; Early Palestinian Ascetic Monasticism lists Jerome; Aksumite Christianity (conversion era) lists Athanasius. Every subject passes the Who test.
- Founder rules. The three founders known through a biographer mark the record as praise or as a saint's life: Antony ("a work of praise", with Robertson's "idealisation, panegyric"), Pachomius ("tells it as the story of a holy man"), Hilarion ("tells it as the life of a saint"). Melitius, known through opponents: his teaching here is a matter of church order, and the brief rests it on two independent contemporary letters, which meets "teaching two". His own side of the lapsed question is never stated (Melitius M2).
- "Only", "first", "never" and single-witness lines, all grepped. They pass: Arius "Only his enemies kept any of it" (no Thalia text survives outside Athanasius; Philostorgius reports the songs and quotes none); the Melitius card's "the one surviving piece of his own"; Frumentius "first bishop" (Rufinus: "sacerdotium coepit"; Sozomen: "the first to manifest the name of Christian"); Frumentius "rests on that one chain" (Socrates, Sozomen, Theodoret and Gelasius all derive from Rufinus); Hilarion "the first monk in Palestine" (told as Jerome's; Hartranft agrees, npnf202 l.21744); the Arius card's Thalia "known only from ... Athanasius". Four overreach: Melitius "never about doctrine", Aetius "fooled only himself", Pachomius "founded communal monasticism" and Antony "the first monks". All four are minors.

| Profile | Words | Est. length | FK | Flesch |
|---|---|---|---|---|
| Melitius of Lycopolis | 320 | 1:59 | 7.5 | 60.6 |
| Arius (major) | 380 | 2:21 | 8.0 | 60.7 |
| Pachomius (major) | 404 | 2:30 | 8.5 | 61.4 |
| Antony the Great (major) | 401 | 2:29 | 7.0 | 70.0 |
| Frumentius (major) | 397 | 2:27 | 7.9 | 60.9 |
| Aetius of Antioch | 285 | 1:46 | 8.1 | 62.5 |
| Hilary of Poitiers (major) | 401 | 2:29 | 7.6 | 62.6 |
| Lucifer of Cagliari | 314 | 1:56 | 7.4 | 60.9 |
| Hilarion of Gaza | 324 | 2:00 | 6.9 | 70.8 |

---

## 1. Melitius of Lycopolis

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | PASS, with minor overreach (M3, M5, M7) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS, with minor points (M3, M5) |
| 5 | No role for a witness | PASS |
| 6 | Partisan witness marked | PASS. Athanasius is marked as his enemy. Epiphanius is minor (M1). Teaching on two witnesses: PASS, with M2 |
| 7 | Contested both sides | PASS (Athanasius against Bell). Socrates is minor (M4) |
| 8 | Common names | MINOR (M6) |
| 9 | One term | PASS |
| 10 | Story, scene, length | PASS (1:59) |
| 11 | grade_text | PASS |
| 12 | Card order and caveat | PASS. Card date and legacy are minor (M7, M8) |
| 13 | Audio tags | PASS |
| 14 | List line, Who | PASS (l.79549) |

**Quotes**
- "The Meletian account of the matter.": exact (Robertson's prolegomena, `npnf204_athanasius-select-works-letters.xml` l.1645).
- "ordained in the prison several unto himself.": exact (Peter's letter, `anf06_...` l.27801).
- "offering sacrifice to idols.": exact (Defence against the Arians 59, npnf204 l.24779).
- "a nominal dignity.": exact (the synod's letter in Socrates I.9, `npnf202_socrates-sozomen-ecclesiastical-histories.xml` l.3211).
- No card quotations. The prison scene matches Epiphanius, Panarion 68.3, in Oehler's Latin (`epiphanius_panarion-haer-48-69-...` l.43922–43932: "pallium ... veli instar oppandens", "maior numerus sese ad Meletium adiunxit"). The four bishops' letter is anf06 l.16711 onward. The schedule of clergy is Defence 71 (npnf204 l.25344). John as successor is Sozomen II.21 (npnf202 l.29611–29613).

**Findings**
- **M1 MINOR.** "Epiphanius wrote about seventy years later, as a foe of every heresy." The listener is left to discount the prison story. Robertson calls it the Meletian side's own account, and Bell, the brief's main modern witness, says Epiphanius "had excellent authority, probably in part that of Egyptian Bishops banished to Palestine" (`bell_jews-christians-egypt-meletian-papyri_1924.txt` l.3157–3159). The brief gives Bell's verdict on Athanasius but not on Epiphanius. Fix: "Epiphanius, a foe of every heresy, wrote about seventy years later. Here he tells the Melitians' side, and Bell thinks his informants were good, probably Egyptian bishops exiled to Palestine."
- **M2 MINOR.** Melitius's own position on the lapsed is never stated. Epiphanius has Peter arguing for mercy and Melitius for the stricter line (Oehler l.43916–43920), and Bell confirms the issue from Peter's own canons, following Schwartz (l.3176–3178 and note 2). Add one sentence, such as "Melitius wanted a longer wait before those who gave way were taken back." That gives the teaching its two witnesses.
- **M3 MINOR.** "It was never about doctrine." Bell says the schism "had no doctrinal origin" (l.3167) and Robertson that "No doctrinal question, however, was involved" (npnf204 l.1645 region). Sozomen II.21 says the Melitians later "received the Arian doctrines" (npnf202 l.29632–29633). Fix: "It did not begin over doctrine."
- **M4 MINOR.** The sacrifice charge has a second ancient witness. Socrates I.6 says Peter deposed Melitius "because during the persecution he had denied the faith and sacrificed" (npnf202 l.2406–2408). Name Socrates beside Athanasius in the card's What is uncertain and in records.json.
- **M5 MINOR.** "Melitius's fiercest enemy." The superlative is unsourced. Bell calls Athanasius "an uncompromising opponent of the Meletians" (l.3150). Use Bell's words.
- **M6 MINOR.** The brief's first mention is "Melitius" alone, in the prison scene. The place comes two paragraphs later. Era 2 also has Meletius of Antioch. Fix: "Peter, bishop of Alexandria, was held there with Melitius of Lycopolis and other clergy."
- **M7 MINOR.** Card `dates`: "deposed about 306". No held source gives that year for a deposition. Robertson puts the accusation in 301 and gives no year for Peter's synod (npnf204 l.1645 region). Bell has Peter's excommunication letter after the four bishops were martyred, "probably in 306" (l.3205). Fix: "excommunicated by Peter about 306, by Bell's dating", or drop the year.
- **M8 MINOR.** Card legacy, remembered: "The Council of Nicaea in 325 left him the title of bishop..." This is a fact about him, not how he is remembered (the era 1 Suetonius M3 point). Move it to the brief's facts or drop it.
- **M9 MINOR.** records.json tags "lasted into the eighth century" Documented. Bell writes "We may probably conclude that the sect died out finally during the eighth century" (l.3452). Keep the hedge in the note, or tag it Widely Accepted.

No blocking findings.

---

## 2. Arius (major)

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | FAIL (B1, B2). Minor points M1, M2, M5 |
| 2 | Quotes verbatim | FAIL (B1: a quote is given to the wrong writer) |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS, with minor point M7 |
| 5 | No role for a witness | PASS |
| 6 | Partisan witness marked | PASS for Athanasius and Photius. Philostorgius is minor (M3, M4) |
| 7 | Contested both sides | FAIL (B3: the start of the controversy is told as settled) |
| 8 | Common names | MINOR (M6) |
| 9 | One term | PASS |
| 10 | Story, scene, length | PASS (major, 2:21) |
| 11 | grade_text | PASS |
| 12 | Card order and caveat | PASS in order. Card uncertain carries B2 |
| 13 | Audio tags | PASS |
| 14 | List line, Who | No people-list line (report only) |

**Quotes**
- "If the Father begat the Son," / "he that was begotten had a beginning of existence: and from this it is evident, that there was a time when the Son was not.": exact (Socrates I.5, npnf202 l.2094; Zenos's long note on "Libyan" sits just before it).
- "unjustly persecuted by Alexander the Pope": exact (Theodoret I.4, `npnf203_theodoret-jerome-gennadius-rufinus.xml` l.6006).
- "We are persecuted, because we say that the Son has a beginning, but that God is without beginning.": exact (l.6045). It is not the letter's end (M1).
- "According to faith of God's elect, God's prudent ones,": exact (Orations I.5, npnf204 l.41460).
- "consubstantial with the Father,": exact (the creed in Socrates I.8, npnf202 l.3075).
- "either Arius or himself might be taken away": found only in Robertson's prolegomena (npnf204 l.4870–4871), not in Athanasius (B1).
- Card: "there was a time when the Son was not." exact, as above.

**Findings**
- **B1 BLOCKING.** "The aged bishop Alexander of Constantinople prayed, Athanasius says, that 'either Arius or himself might be taken away' first." The quoted words are Archibald Robertson's summary in his prolegomena (npnf204 l.4870–4871), not Athanasius's. Athanasius's own account, the letter to Serapion on the death of Arius, gives the prayer as: "If Arius is brought to communion to-morrow, let me Thy servant depart, and destroy not the pious with the impious; but if Thou wilt spare Thy Church ... take off Arius" (l.70093–70099). Athanasius also says he was not there: "I was not at Constantinople when he died, but Macarius the Presbyter was, and I heard the account of it from him" (l.70064–70065). The next two sentences, "His friends blamed magic. Alexander's side saw the hand of God.", are Robertson citing Sozomen II.29, and Sozomen gives a third view, "the public generally to the effect of excitement on a diseased heart" (l.4874–4876). Fix: "Athanasius was not in the city, but the presbyter Macarius told him what happened. Alexander, the aged bishop of Constantinople, prayed that if Arius came to communion, God would 'let me Thy servant depart', and if not, 'take off Arius'." Then: "Sozomen gives three views of the death. His friends blamed magic, Alexander's side saw God's judgment, and most people blamed a weak heart."
- **B2 BLOCKING.** Two facts are given to Athanasius that are Robertson's. Brief: "Athanasius of Alexandria, his great foe, grants that he was given charge of teaching Scripture." Robertson writes that "we find him not only in charge of the urban parish of Baucalis, but entrusted with the duties of a professor of scriptural exegesis" (npnf204 l.1688–1690). No passage of Athanasius says it. The word "grants" turns a modern editor's statement into a hostile witness's concession, which a listener will weigh more heavily. Card uncertain: "Athanasius calls him a native of Libya and places his death in 336." This is Robertson again, and hedged: "We are told that Arius, a native of Libya" (l.1676). The year 336 is Robertson's chronology (l.4854, l.10090). records.json `absent_details` repeats both. Fix, brief: "Archibald Robertson, who edited Athanasius in English, says he also taught Scripture." Card: "Robertson reports that he was said to be a native of Libya, and dates his death to 336."
- **B3 BLOCKING.** "That argument began the Arian controversy." This tells one account as settled. Robertson says "The origin of the controversy is obscure" (l.1673) and gives two others: Constantine's own letter, which has Alexander asking his presbyters about a passage of Scripture (l.1703–1706), and the view that Arius was the aggressor (l.1699–1702). Philostorgius, through Photius, says a presbyter called Baucalis started the quarrel (`philostorgius_ecclesiastical-history_walford1855.txt` l.92). Socrates wrote about a century later. The date "about the year 318" is also Robertson's ("as early as 318 or 319", l.1674). Fix: "Socrates dates the start of the quarrel to this moment. Archibald Robertson says the true origin is obscure, and Constantine's own letter tells it differently." Add a `contested_claim` naming Socrates, Constantine (via Robertson) and Philostorgius.
- **M1 MINOR.** "He ends, 'We are persecuted...'" The letter goes on: "This is the cause of our persecution ... For this are we persecuted; the rest you know. I bid thee farewell" (npnf203 l.6045–6050). Write "Near the end he writes".
- **M2 MINOR.** "Athanasius quotes its start ... then mocks the verses that follow." What follows the opening is more of the Thalia, which Athanasius calls Arius's own "mockeries" (npnf204 l.41462). His scorn falls on the metre: "flippancy, effeminate in tune and nature" (l.41460). Fix: "then calls the lines that follow mockeries."
- **M3 MINOR.** The songs for "sailors and travellers" have no witness. They are Philostorgius's, through Photius: "songs to be sung by sailors, and by millers, and by travellers" (Walford l.114; also Newman's note, npnf204 l.57007). Name him. As placed, the report from an admirer sits just before "Only his enemies kept any of it".
- **M4 MINOR.** "The kind account of Arius comes from Philostorgius, who praised him." Photius says Philostorgius "extols Arius to the skies ... yet he asserts that the latter is involved in the most absurd errors" (l.116). Add "though he also faulted him".
- **M5 MINOR.** "God made him out of nothing, before all time, as the first and highest of creatures." No witness uses "first and highest". Arius's letter says the Son "has subsisted before time, and before ages, as perfect God" (npnf203 l.6045 region), and the Arians' answer to Alexander says "He is a creature, but not as one of the creatures" (npnf204 l.46732). Use their words.
- **M6 MINOR.** First mentions without context: "Theodoret" (Theodoret of Cyrrhus, as the Lucifer brief has him) and "Photius" (patriarch of Constantinople in the 800s, Walford's notice, l.25 region).
- **M7 MINOR.** The closing line, "The creed the council wrote against him became the measure of the faith for the churches that condemned him.", names no witness and adds a beat (item 4, tails). Give it a source or end on the line before.
- **M8 MINOR.** records.json: the Baucalis claim cites Philostorgius, but his "Baucalis" is a presbyter's nickname, which Gothofred thinks is the church's name (Walford l.92, l.524). The songs claim cites only Athanasius. Add Philostorgius there instead.

---

## 3. Pachomius (major)

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | FAIL (B1). Minor points M2, M5, M7 |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS |
| 5 | No role for a witness | MINOR on the card (M1) |
| 6 | Partisan witness marked | PASS. Palladius's record is marked as a holy man's story |
| 7 | Contested both sides | PASS (Ladeuze against Butler). Gennadius is minor (M3) |
| 8 | Common names | MINOR (M6) |
| 9 | One term | PASS |
| 10 | Story, scene, length | PASS (major, 2:30, at the cap) |
| 11 | grade_text | PASS |
| 12 | Card order and caveat | PASS in order. Card own-words entry is minor (M4) |
| 13 | Audio tags | PASS |
| 14 | List line, Who | PASS (l.36565) |

**Quotes** (`palladius_lausiac-history_clarke1918.txt` unless named)
- "Either drive him out, or know that we are all going.": exact (XVIII.15, l.309).
- "I thank you for letting my children feel your fist," / "lest they should be proud of their ascetic achievements.": exact (XVIII.16, l.309).
- "that even the little ones keep the rule and are not afflicted.": exact (XXXII.7, l.403; Clarke's note marker "211" follows).
- "probably the most authentic epitome.": exact (Clarke's note 207, l.1049).
- "almost to the days of Pachomius himself.": exact (Schodde, `pachomius_rules-ethiopic_schodde1885.txt` l.162).
- "the father of monastic institutions.": exact (Schodde l.136, the opening of his introduction).
- Card: "a man endowed with apostolic grace both in teaching and in performing miracles.": exact (Gennadius 7, npnf203 l.42255).

**Findings**
- **B1 BLOCKING.** Card uncertain: "Palladius, who wrote about 420, some forty years after Pachomius died". The card's own dates put the death in 348, so 420 is about seventy years after. The brief's "Palladius visited the Pachomian houses some forty years after Pachomius died" has no source either. Palladius says only that he lived nine years at Cellia (l.295) and does not date his visit to Panopolis (l.405). Fix: drop the interval in both texts, or give it with a named source. In the card, give 420 a source or drop it.
- **M1 MINOR.** Card `dates`: "(the dates in the editor's note to Gennadius's chapter)". This is a role standing in for a witness (item 5; the era 1 Pontius B1 pattern). The note is Richardson's, and Schodde gives the same years, 292 and 348 (l.136). Fix: "(Schodde; Richardson's note to Gennadius)". records.json has the same wording.
- **M2 MINOR.** "came to the monastery of Tabennisi". Palladius says "the monastery of the Tabennesiots" (l.309), and Clarke notes that the head house "was now Pabau, not Tabennisi" (note 132, l.897; again note 213, l.1063). Write "the Tabennesiot monastery".
- **M3 MINOR.** The angel. The card says "Palladius and Sozomen both say". Gennadius says it too: the rule was "received by angelic dictation" (npnf203 l.42255). Clarke sets him against Ladeuze: "But cf. Gennadius, de vir. illus., 7" (note 200, l.1033). Butler's disagreement concerns Palladius's version of the rules in general (note 207, l.1049), not the angel. Add Gennadius on the card. In the brief, "Butler did not accept Ladeuze's low view of Palladius's rule" is closer than "Butler disagreed".
- **M4 MINOR.** The card lists the Rules under "Their own words", and its first uncertain line says "Pachomius left no writing of his own that is held here." Schodde says the first part, "if not verbatim from his pen, are yet authentic enough" (l.162). Fix the uncertain line: "No writing held here is certainly his own. Schodde thinks the first part of the Ethiopic rules comes close to him."
- **M5 MINOR.** Card `knownFor`: "founded communal monasticism". This is a "first" claim. The Library is not of one voice: the editor's note in the Confessions says "To Antony is the world indebted for establishing communities of monks" (`npnf101_augustine-confessions-letters.xml` l.12519–12521). Tell it with its witness: "whom Gennadius calls founder of the Egyptian monasteries".
- **M6 MINOR.** "Butler" has no context at first mention. "Ladeuze" gets "the scholar". Give Butler the same.
- **M7 MINOR.** "An Ethiopic version of the rules also survives." Schodde says its first part "is ... the same as the Greek form" (l.162), so it is not independent of the rule Palladius knew. Add "which Schodde says follows the Greek".

---

## 4. Antony the Great (major)

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | FAIL (B1). Minor points M2, M3, M4, M6 |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS |
| 5 | No role for a witness | PASS |
| 6 | Partisan witness marked | PASS. The Life is marked as praise; Robertson's "idealisation, panegyric" is given |
| 7 | Contested both sides | PASS on authorship (Robertson; Gwatkin on the card) |
| 8 | Common names | PASS (Athanasius of Alexandria, Jerome of Strido) |
| 9 | One term | PASS |
| 10 | Story, scene, length | PASS (major, 2:29) |
| 11 | grade_text | PASS |
| 12 | Card order and caveat | PASS in order. Empty field (M8), sources (M5) |
| 13 | Audio tags | MINOR (M7) |
| 14 | List line, Who | No people-list line (report only) |

**Quotes** (npnf204 unless named)
- "If thou wouldest be perfect, go and sell that thou hast and give to the poor.": exact up to "poor", where the Life goes on "; and come follow Me" (Life 2, l.31244). The full stop marks the cut.
- "poured water on his hands.": exact (prologue, l.31199). The editor's note on it is the subject of B1.
- "the external evidence for the Vita is too strong to allow us to set it aside as spurious": exact (Robertson's introduction, l.30447).
- "idealisation, panegyric": exact (l.30919).
- "the desert was colonised by monks": exact (Life 14, l.31625).
- "saying that their heresy was the last of all": exact (Life 69, l.32930; the Life goes on "and a forerunner of Antichrist").
- "Do not be astonished if an emperor writes to us," / "for he is a man.": exact (Life 81, l.33193).
- "maketh His own known everywhere.": exact (Life 93, l.33574).
- Card: "kindled the flame of monastic aspirations": exact (l.30944). "never existed,": exact (l.30616). Coma "in Upper Egypt" is the editor's note to Life 1 (l.31216); Sozomen I.13 has "Coma, which was situated near the Heraclea" (npnf202 l.27323). Jerome 88 is npnf203 l.41177.

**Findings**
- **B1 BLOCKING.** "Its writer says he was Antony's attendant and 'poured water on his hands.'" The note on that very phrase says: "The text is uncertain, as some mss., both Greek and Latin read, 'was able to learn from him who was his attendant,' &c. The question of textual evidence requires further sifting" (l.31199–31205). On the other reading, the attendant is someone else and the writer is not. The brief uses the line as the writer's own claim to have known Antony, just before it turns to who wrote the Life. A hedge that decides the point is dropped. Fix: "Its writer says, in most copies, that he was Antony's attendant and 'poured water on his hands.' Some copies make the attendant someone else."
- **M1 MINOR.** Card `knownFor`: "drew the first monks after him". Jerome, Life of Paul 1, reports that two of Antony's own disciples, Amathas and Macarius, say "a certain Paul of Thebes was the leader in the movement" (`npnf206_jerome-principal-works.xml` l.29747–29753). The Life itself has Antony learn from an older hermit (Life 3). Write "drew monks after him".
- **M2 MINOR.** "About six months after his parents died". The Life says "not six months after the death of his parents" (l.31237). Write "Less than six months after".
- **M3 MINOR.** "Antony lived, by its account, from about 251 to 356". The Life gives his age, "near a hundred and five" (l.33446), not years. The years are Richardson's note to Jerome 88 (npnf203 l.41177) and the note in anf06 (l.27749). Card `dates` repeats "by the Life of Antony". Fix: "By the usual reckoning, which Richardson gives, Antony lived from about 251 to 356."
- **M4 MINOR.** Card legacy: "how reading of Antony turned two court officials, and himself". The officials read the Life (Confessions VIII.6, npnf101 l.12613). Augustine himself says "For I had heard of Antony" (VIII.12, l.13116). Write "how two court officials read the Life, and how hearing of Antony moved him".
- **M5 MINOR.** Card sources: the npnf203 entry is titled "On Illustrious Men, chapter 88, and the Confessions, Book 8" with Augustine as an author. The Confessions are in npnf101, already listed below it. Drop them from the npnf203 entry.
- **M6 MINOR.** Card uncertain and key works: "The seven Coptic letters survive". No held source says they survive. Jerome says they "have been translated into Greek" (npnf203 l.41178). Write "Jerome says they were translated into Greek. None is held in this Library."
- **M7 MINOR.** `[warmly]` sits before the five-sentence last paragraph. Move it before "The Life closes on what it says his fame proved".
- **M8 MINOR.** Card `sources.ownWords: []`. A missing field is absent, never filled (item 12). Remove it.
- **M9 MINOR.** records.json tags several claims that rest on the Life alone Widely Accepted (the inheritance, the stages of withdrawal, the death at about 105). One hagiographic witness's direct report fits Documented with a one-witness note. "Jerome's Chronicle gives 356": the Chronicle is not held. The year is Richardson's note to Jerome 88.

---

## 5. Frumentius (major)

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | FAIL (B1 in the brief, B2 on the card) |
| 2 | Quotes verbatim | FAIL (B1: the words are real, the speaker is wrong) |
| 3 | No invention | FAIL on the card (B2) |
| 4 | Reading aids | PASS |
| 5 | No role for a witness | PASS (Zenos, Valesius, Robertson, Hartranft, Jackson named) |
| 6 | Partisan witness marked | PASS. The emperor's hostility shows in his own words |
| 7 | Contested both sides | PASS (Rufinus against Valesius and Robertson, with a contested_claim) |
| 8 | Common names | PASS (Rufinus of Aquileia, Socrates of Constantinople, Athanasius of Alexandria) |
| 9 | One term | PASS (Auxumis glossed as Axum) |
| 10 | Story, scene, length | PASS (major, 2:27). M4 on the close |
| 11 | grade_text | PASS |
| 12 | Card order and caveat | PASS |
| 13 | Audio tags | PASS |
| 14 | List line, Who | No people-list line (report only) |

**Quotes**
- "Bishop of Auxumis.": the words are in Athanasius's own narrative, Apology to Constantius 29 (npnf204 l.36003), not in the emperor's letter (B1).
- "was advanced to his present rank by Athanasius, a man who is guilty of ten thousand crimes.": exact (the letter, Apology 31, l.36150).
- "the Father of Peace.": exact (Jackson's note quoting the Dictionary of Christian Biography, npnf203 l.7768).
- Rufinus's story checked in the Latin (`eusebius_werke-bd2-2-...-rufinus-..._schwartz-mommsen1908.txt` l.27304–27383): the boys "sub arbore meditantes et lectiones suas parantes", "propinquos", the cup-bearer and the accounts, the queen, the "conventicula", Athanasius "nuper sacerdotium susceperat", and "ipso Edesio Tyri presbytero postmodum facto ... referente". Valesius and Zenos: npnf202 l.4283–4296. Hartranft: l.29919.

**Findings**
- **B1 BLOCKING.** "Athanasius later copied into his defence a letter from the emperor Constantius to the princes of Auxumis ... It calls Frumentius 'Bishop of Auxumis.'" The letter does not. It names him "the Bishop Frumentius" (l.36145). "Frumentius, Bishop of Auxumis" is Athanasius's own phrase in §29 (l.36003), and the heading over the letter, "respecting Frumentius, Bishop of that place", is his too (l.36109). The point matters because the brief offers the letter as the independent witness. Its real witness is the line that follows, "advanced to his present rank by Athanasius". Fix: "Athanasius calls him 'Bishop of Auxumis.' The emperor's letter speaks of 'the Bishop Frumentius,' and says he 'was advanced to his present rank by Athanasius, a man who is guilty of ten thousand crimes.'"
- **B2 BLOCKING.** Card `knownFor`: "A shipwrecked Roman captive". There was no shipwreck. In Rufinus the ship put in at a port for water, and the local people killed everyone on board (l.27307–27311). Socrates, Sozomen and Theodoret tell it the same way. Fix: "A Roman captive, taken as a boy when his ship's company was killed".
- **M1 MINOR.** Card legacy: "The emperor Constantius tried to have him replaced by an Arian bishop, Theophilus, which Blomfield Jackson notes from Athanasius's Apology to Constantius 31; the attempt did not succeed." Apology 31 names no Theophilus. It asks that Frumentius be sent to George of Alexandria for examination (l.36145–36170). Theophilus and the failure come from the Dictionary of Christian Biography, which Jackson quotes (npnf203 l.7768). Fix: "Blomfield Jackson's note, quoting the Dictionary of Christian Biography, says..."
- **M2 MINOR.** "Valesius thought it came later, under Constantius. Archibald Robertson ... agrees." Robertson does not cite Valesius. He cites Gwatkin for the chronology and says the Dictionary of Christian Biography's argument "is faulty" (npnf204 l.5676–5682). Write "Archibald Robertson, following Gwatkin, also puts it later."
- **M3 MINOR.** The brief names Socrates and Sozomen as the retellers. Theodoret I.23 retells it too and is on the card. Jackson: "copied or varied by Sozomen, Socrates, and our author, from the version found also in Rufinus" (npnf203 l.7768 region). Add him or write "the Greek historians who followed him".
- **M4 MINOR.** The last paragraph passes one name through two translators' notes. A major brief does not need to reach 2:30. One sentence would carry it: "The Ethiopian tradition, Hartranft notes, calls him Abba Salama, which the Dictionary of Christian Biography gives as 'the Father of Peace.'"

---

## 6. Aetius of Antioch

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | FAIL (B1). Minor points M1, M7 |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | FAIL (B1: who gave the nickname is supplied) |
| 4 | Reading aids | PASS, with minor point M1 |
| 5 | No role for a witness | PASS |
| 6 | Partisan witness marked | PASS for Philostorgius and Socrates. Photius's layer is minor (M3) |
| 7 | Contested both sides | PASS |
| 8 | Common names | MINOR (M5) |
| 9 | One term | PASS |
| 10 | Story, scene, length | PASS (1:46) |
| 11 | grade_text | PASS |
| 12 | Card order and caveat | MINOR (M4 order; M2 date) |
| 13 | Audio tags | PASS |
| 14 | List line, Who | PASS (l.39942) |

**Quotes**
- "a sacrifice to the Emperor's scruples.": exact (Robertson, npnf204 l.6558).
- "unlike": Robertson's gloss on ἀνόμοιος (l.6247).
- No card quotations. The Syntagmation is in Panarion 76 (`epiphanius_panarion-haer-65-80-pg42-grc-lat_migne1863.txt` l.40318, l.41223). Philostorgius on the trade, Leontius, Julian, Lesbos and the death: Walford l.178, l.182, l.258, l.338, l.342. Julian's "letters full of benignity": Sozomen V.5 (npnf202 l.35604–35611).

**Findings**
- **B1 BLOCKING.** The nickname is given to the wrong people, in four places. Brief: "Aetius argued about God with a boldness that troubled even his fellow Arians. They gave him a nickname: Atheus, the godless one. Socrates of Constantinople records it." Card `otherNames`: "the nickname given him by the Arians". Card remembered: "the nickname his own side gave him". records.json: "Nicknamed Atheus (the godless) by his own Arian side", Documented, Socrates II.35. Socrates says only "He has therefore been surnamed Atheus", after his "tedious disputes" in letters to Constantius. It is a separate sentence that "his associates in Arianism pronounced him a heretic" (npnf202 l.8388–8393). Sozomen III.15: "He reasoned so boldly concerning the nature of God, that many persons gave him the name of 'Atheist'" (l.32004–32006). Athanasius himself calls him "Aetius, who was surnamed godless" (de Synodis 6, npnf204 l.56564; Newman's note at l.26588). The uproar at his ordination was not from his fellow Arians either. Robertson: "Flavian and Diodorus ... raised such a storm that the cautious bishop felt obliged to suspend him" (l.6237–6239). Flavian and Diodorus led the Nicene side at Antioch. Fix, brief: "Two Nicene leaders, Flavian and Diodorus, raised such an uproar that Leontius soon had to suspend him. Aetius reasoned so boldly about God, Sozomen says, that many people called him Atheus, the godless one." Fix the card's two lines and the records.json claim to match.
- **M1 MINOR.** "built clever arguments that fooled only himself". Socrates: "he was little aware that he was framing fallacious arguments to perplex and deceive himself" (l.8376–8377). "Only" is not his. Write "arguments that, Socrates says, deceived himself".
- **M2 MINOR.** Card `dates`: "died at Constantinople, about 367". The card's own uncertain line says the year is not given, and none of the held sources gives it. Philostorgius places the death at Constantinople after Procopius's revolt (IX.6, l.342). Drop the year or write "after 366".
- **M3 MINOR.** The brief names Philostorgius as an admirer but not that his work survives only in Photius's hostile summary, which the Arius brief and the Aetius card both say. Add the clause at his first mention.
- **M4 MINOR.** Card field order: `keyWorks` comes before `briefLength`. Mark's order puts the brief and its length first (item 12).
- **M5 MINOR.** First mentions without context in the brief: "Eudoxius" (bishop of Antioch, later of Constantinople; Robertson l.6245–6246) and "Eunomius" (the card's "Eunomius of Cyzicus").
- **M6 MINOR.** records.json cites "Socrates II.35 and III.x". The second chapter is a placeholder. Give the chapter or drop it.
- **M7 MINOR.** "Aetius came from Coele-Syria" stands before Philostorgius is named. Socrates says Antioch "was his native place" (l.8352). Write "Philostorgius says Aetius came from Coele-Syria and was poor."

---

## 7. Hilary of Poitiers (major)

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | PASS |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS, with minor point M1 |
| 5 | No role for a witness | PASS (Watson named) |
| 6 | Partisan witness marked | PASS (Sulpicius "firmly on Hilary's side"; Hilary's own account of the hearing named as his) |
| 7 | Contested both sides | PASS (the hearing: Hilary's account, Auxentius's, Watson's verdict) |
| 8 | Common names | PASS (Eusebius of Vercelli, Auxentius of Milan, Saturninus of Arles, Cyprian of Carthage, Jerome of Strido) |
| 9 | One term | PASS |
| 10 | Story, scene, length | PASS (major, 2:29) |
| 11 | grade_text | PASS |
| 12 | Card order and caveat | PASS. Other names is minor (M2) |
| 13 | Audio tags | PASS |
| 14 | List line, Who | PASS (l.39251) |

**Quotes**
- "I chanced upon the books which, according to the tradition of the Hebrew faith, were written by Moses and the prophets.": exact (On the Trinity I.5, `npnf209_hilary-poitiers-john-damascus.xml` l.10620).
- "I Am that I Am.": exact (l.10623).
- "a troubler of the East,": exact (Sulpicius, Chronicle II.45, `npnf211_sulpitius-severus-vincent-lerins-cassian.xml` l.11411; the full phrase is "a sower of discord, and a troubler of the East").
- "were set free from the guilt of heresy through the kind efforts of Hilarius alone.": exact (l.11433).
- Card: "sixth year after his return": exact (l.11441).
- Watson checked: the search for God not "literal history" (l.768–772); Béziers and "his conduct, not his faith" (l.1423–1431); born "probably about the year 300" (l.573); "never once named" by Athanasius (l.556–557); Abra (l.812–815); Orosius (l.3005); the hearing and Auxentius's report "not inconsistent with Hilary's" (l.4030–4040); death in 367 (l.4526). Jerome, Lives 100: npnf203 l.41333. Augustine, On Christian Doctrine II.40: `npnf102_...` l.51719–51722.

**Findings**
- **M1 MINOR.** "Watson says the charges concerned his conduct, not his faith." This is the "X, not Y" shape in narrator prose (item 4), though the words are Watson's (l.1430–1431). Fix: "The charges, Watson says, were about his conduct. His faith was not in question."
- **M2 MINOR.** Card `otherNames`: "Hilary of Pictavium in Jerome". The form is Rufinus's, in his book on the adulteration of Origen's works (npnf203 l.45533). Jerome's Lives 100 has "a bishop of Poitiers in Aquitania" (l.41334). Fix: "Hilary of Pictavium in Rufinus".
- **M3 MINOR.** Augustine names "Victorinus, and Optatus, and Hilary" in one breath, after Cyprian and Lactantius (npnf102 l.51721–51722). "All of them" reads as three. Optional: "named Hilary with Cyprian of Carthage, Lactantius and others".

No blocking findings.

---

## 8. Lucifer of Cagliari

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | PASS |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS, with minor point M4 |
| 5 | No role for a witness | PASS (Fremantle, Richardson named) |
| 6 | Partisan witness marked | PASS (Jerome placed as ordained by Paulinus) |
| 7 | Contested both sides | PASS (Socrates against Ambrose and Augustine; Jerome between). M5 |
| 8 | Common names | MINOR (M1, M2) |
| 9 | One term | PASS |
| 10 | Story, scene, length | PASS (1:56). Opener is minor (M4) |
| 11 | grade_text | PASS |
| 12 | Card order and caveat | PASS |
| 13 | Audio tags | PASS |
| 14 | List line, Who | PASS (l.79644) |

**Quotes**
- "with wonderful constancy and willingness to meet martyrdom.": exact (Jerome, Lives 95, npnf203 l.41268).
- "a distinct sect arose under the name of 'Luciferians.'": exact (Socrates III.9, npnf202 l.10924).
- "that saintly man,": exact (Dialogue against the Luciferians 20, npnf206 l.32533).
- "He himself was a good shepherd," / "but he was leaving a vast spoil to the beasts of prey.": exact (l.32537).
- Fremantle's introduction: npnf206 l.31408–31452. Theodoret III.2 with Jackson's notes: npnf203 l.11534–11600.

**Findings**
- **M1 MINOR.** "Liberius of Rome had sent him to the emperor with the clergy Pancratius and Hilary." This Hilary is a namesake of Hilary of Poitiers, whose profile is in this batch. Fremantle: "the priest Pancratius and the deacon Hilarius" (l.31417); Jerome: "clergy of the Roman church" (npnf203 l.41268). Fix: "with the Roman priest Pancratius and the deacon Hilary".
- **M2 MINOR.** "There he made Paulinus bishop of one party." Paulinus is a common name. Theodoret gives the context: "The Eustathians, led by Paulinus, a presbyter" (npnf203 l.11568–11569). Write "Paulinus, a presbyter who led one party".
- **M3 MINOR.** "Jerome's Chronicle says he died in 371." The Chronicle is not held. Fremantle (npnf206 l.31449) and Jackson (npnf203 l.11595) report it. Write "Jerome's Chronicle, Fremantle notes, gives 371." Fremantle's "no one who had yielded to any compromise..." is also in quotation marks in his introduction (l.31438–31443), quoting an unnamed source. The brief's paraphrase is fine; records.json should not give it as Fremantle's own.
- **M4 MINOR.** The opener, "Lucifer of Cagliari would not condemn the Nicene faith. Instead he wrote a book...", opens on a stance in the "not X, instead Y" shape. Open on the act, which Jackson places: "relegated in 355 to Eleutheropolis, whence he wrote the controversial pamphlets ... He vigorously abused Constantius, to whom he paid the compliment of sending a copy" (npnf203 l.11535–11538). For example: "In exile in Palestine, Lucifer of Cagliari wrote a book against the emperor Constantius and sent it to him to read."
- **M5 MINOR.** Card uncertain: "How far Lucifer himself was a schismatic is not settled." This is J. Ll. Davies's judgment in the Dictionary of Christian Biography, quoted by Jackson: "To what extent he was an actual schismatic remains obscure" (npnf203 l.11596). Name him.

No blocking findings.

---

## 9. Hilarion of Gaza

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | PASS, with minor points M2, M3, M7 |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | MINOR (M4) |
| 5 | No role for a witness | FAIL (B1) |
| 6 | Partisan witness marked | PASS. Jerome's Life is marked as a saint's life |
| 7 | Contested both sides | PASS |
| 8 | Common names | PASS (Jerome of Strido, Epiphanius of Salamis on the card) |
| 9 | One term | PASS |
| 10 | Story, scene, length | PASS (2:00, at the non-major limit) |
| 11 | grade_text | PASS |
| 12 | Card order and caveat | PASS in order. Empty fields (M6) |
| 13 | Audio tags | MINOR (M5) |
| 14 | List line, Who | No people-list line (report only) |

**Quotes** (npnf206 unless named)
- "contains, amidst much that is legendary, some statements which attach it to genuine history.": exact (the introduction to the Life, l.30090).
- "It was he who originated this mode of life and devotion,": exact (Life 14, l.30348).
- "The Lord Jesus had in Egypt the aged Antony: in Palestine He had the youthful Hilarion.": exact (l.30350).
- "I have returned again to the world," / "and have received my reward in my lifetime.": exact (Life 29, l.30689).
- "by simply calling on the name of Christ.": exact (Sozomen V.15, npnf202 l.36376).
- Card: "set forth his praises in a short but widely circulated letter,": exact (Life 1, l.30111). "nearly seventy years.": exact (Life 45, l.31071).
- The Aristaenete scene matches Life 14 (l.30312–30346): the three sons, the visit to Antony, "never left his cell", "after sunset", "the sign of the cross", "in that very hour".

**Findings**
- **B1 BLOCKING.** "The editor of Jerome's works warns that the Life 'contains, amidst much that is legendary...'" The card's uncertain line says the same. This is a role standing in for a named witness (item 5), the pattern era 1 batch 2 blocked as Pontius B1. The introduction is unsigned. The volume's preface says G. Lewis and W. G. Martley drafted most of the notes, and W. H. Fremantle went through every part and wrote the Prolegomena (l.486–527). The same introduction also says that the theory of the Life as "a sort of religious romance, seems destitute of foundation" (l.30091–30092). Fix: "W. H. Fremantle's English edition of Jerome warns that the Life 'contains, amidst much that is legendary, some statements which attach it to genuine history.'" Make the same change on the card.
- **M1 MINOR.** "Through that cure, Sozomen writes, Alaphion's household and his own grandfather became Christians." Sozomen hedges: "It is said that the above-mentioned families were converted through the instrumentality of the monk Hilarion" (npnf202 l.36372–36373). Keep his hedge: "Sozomen writes that, as it was told, the cure made Christians of Alaphion's household and his own grandfather's."
- **M2 MINOR.** The cure is in Sozomen V.15 (chapter heading at npnf202 l.36259). The card's sources give "Book 3, chapter 14, and Book 6, chapter 32", and records.json cites VI.32. Add V.15.
- **M3 MINOR.** Card uncertain: "Sozomen ... gives an independent notice ... He drew in part on Jerome's Life and diverges from it on some points." No witness is named, and Hartranft's list of Sozomen's sources for III.14 does not include Jerome's Life (npnf202 l.31654–31661). "Independent" and "drew in part" also pull against each other. Name a witness or drop the second sentence. records.json `absent_details` repeats it.
- **M4 MINOR.** "The church historian Sozomen adds a debt of his own." The meaning is unclear until two sentences later (item 4, a statement with no context). Write "Sozomen, the church historian, had a family reason to remember Hilarion."
- **M5 MINOR.** `[warmly]` sits before the three-sentence last paragraph. Move it before the last sentence.
- **M6 MINOR.** Card `otherNames: []` and `sources.ownWords: []`. Remove both (item 12).
- **M7 MINOR.** Card `dates`: "About 291 to about 371", and uncertain: "His dates rest on the Life and on Sozomen." The year 371 is Hartranft's reckoning, "Hilarion passed away about 371" (npnf202 l.21793), not Sozomen's. records.json calls it "editor's reckoning", a role. Name Hartranft.

---

## Summary

| Profile | Blocking | Minor |
|---|---|---|
| Melitius of Lycopolis | 0 | 9 |
| Arius | 3 | 8 |
| Pachomius | 1 | 7 |
| Antony the Great | 1 | 9 |
| Frumentius | 2 | 4 |
| Aetius of Antioch | 1 | 7 |
| Hilary of Poitiers | 0 | 3 |
| Lucifer of Cagliari | 0 | 5 |
| Hilarion of Gaza | 1 | 7 |
| **Total** | **9** | **59** |

Blocking findings in one line each:
1. Arius B1: "either Arius or himself might be taken away" is Robertson's summary given as Athanasius's quote. Athanasius's own words differ, and he had the story from Macarius.
2. Arius B2: "Athanasius ... grants that he was given charge of teaching Scripture" (brief) and "Athanasius calls him a native of Libya and places his death in 336" (card) are Robertson's statements, the Libya one hedged.
3. Arius B3: "That argument began the Arian controversy" tells Socrates's account as settled. Robertson calls the origin obscure and gives Constantine's different account.
4. Pachomius B1: the card's "wrote about 420, some forty years after Pachomius died" is wrong by its own dates (about seventy). The brief's "forty years" has no source.
5. Antony B1: "poured water on his hands" is given as the writer's claim, and the editor's note on that phrase, that some manuscripts make the attendant someone else, is dropped.
6. Frumentius B1: "It calls Frumentius 'Bishop of Auxumis'": the emperor's letter does not. The phrase is Athanasius's own.
7. Frumentius B2: card "A shipwrecked Roman captive": there was no shipwreck in any held account.
8. Aetius B1: the nickname Atheus is said to come from his fellow Arians (brief, card twice, records). Socrates gives no namer, Sozomen says "many persons", and Athanasius uses it himself. The uproar came from the Nicene leaders Flavian and Diodorus.
9. Hilarion B1: "The editor of Jerome's works" (brief and card) is a role standing in for a named witness.

Patterns that recur, each already counted above:
- **Witness swaps.** This is new in this batch and the most serious. Four times, words or facts are given to the wrong writer: a modern editor's sentence is given to an ancient author (Arius B1, B2), or an author's own phrase is given to the document he quotes (Frumentius B1, Aetius B1). Each one changes how much weight a listener gives the line. Before a line says "X says", find the words in X's own text, not in the editor's prolegomena or notes around it.
- **Roles for witnesses.** "The editor" stands in for a name again (Hilarion B1, Pachomius M1, two records.json notes). This is the era 1 Pontius pattern.
- **Told as settled.** The start of the Arian controversy (Arius B3). Melitius M1 is the era 1 dispute-outcome pattern in a milder form: Bell's verdict on Epiphanius is left out.
- **Sources of sources.** Athanasius's informant Macarius (Arius B1), Philostorgius through Photius (Aetius M3), Jerome's Chronicle through Fremantle (Lucifer M3), and the Dictionary of Christian Biography through Jackson (Frumentius M1, Lucifer M5).
- **Hedges dropped.** The manuscript note on "poured water" (Antony B1), Robertson's "We are told" (Arius B2), Sozomen's "It is said" (Hilarion M1) and Bell's "probably" (Melitius M9).
- **"Only", "first", "never".** All were grepped against the whole Library. None fails as a single-witness claim. Four quantifiers overreach their witness (Melitius M3, Aetius M1, Pachomius M5, Antony M1).
- **records.json.** The era 1 pattern of single direct reports tagged Inferential-Thin does not recur. The opposite appears: reports from the Life alone are tagged Widely Accepted (Antony M9).
