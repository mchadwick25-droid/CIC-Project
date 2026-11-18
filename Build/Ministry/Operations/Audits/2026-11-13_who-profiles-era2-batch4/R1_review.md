# R1 review: nine Who profiles, era 2 batch 4

Two independent Opus reviewers, each at first sight of its drafts, reviewed the batch in two parts: part A (Rufinus of Aquileia, Pelagius, Paulinus of Milan, Sulpicius Severus, Honoratus of Arles, and the README) and part B (John Cassian, Palladius of Helenopolis, Possidius of Calama, Philostorgius). Totals: 2 blocking, 23 minor. Each part follows as written.

## R1 review: era 2 batch 4, part A (Church Family Tree Who profiles)

Reviewer: independent, first sight of these drafts. Bar: `Who_Profile_Pattern.md` review checklist 1 to 14 and the standards it points to; `CLAUDE.md` "Trust and source fidelity" and "Accessible and rigorous"; and the failure types of the era 2 batch 1 and batch 2 R1 reviews, above all the witness swap. I did not edit the drafts. I made no paid or model-API calls and used no web. Readability and quote search ran on local scripts only.

Profiles: `rufinus-of-aquileia` (MAJOR), `pelagius` (MAJOR), `paulinus-of-milan`, `sulpicius-severus`, `honoratus-of-arles`, and the batch `README.md`. Files are in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era2/batch4/`. Brief line numbers refer to the `.brief.txt` files, where each paragraph is one line. Other line numbers point to files under `cic/texts/` unless marked.

Method. I searched every quotation in the five briefs and cards in the vendored file the card names. The match ignored XML tags, whitespace and quote style. For the Kaniecka and Migne OCR I also used a letters-only match. I read each hit in context to see who is speaking: the ancient author, a document he quotes, the translator's introduction, or a note. I checked every factual sentence of each brief against its passage. I read the Latin where the Library holds only Latin and compared the narrator's telling with it. Those are Pelagius to Demetrias (Migne PL 30), Hilary's sermon on Honoratus (PL 50), Paulinus's petition (Collectio Avellana 47), Mercator (PL 48) and Eucherius (PL 50). I compared each `records.json` entry with its brief and card. Readability came from `engine.m1.gates.grade_text`, run from the repo root. Length assumes 162 words a minute.

## Applies to all five

- **Audio = brief.** Each audio script matches its brief exactly once `[calmly] ` and `[warmly] ` are removed (checked by script). Each starts with `[calmly]` and has one `[warmly]`, placed before the final sentence. No tag appears in any brief or card.
- **Readability.** All five pass (FK at most 10, Flesch at least 60). Rufinus sits nearest the floor (Flesch 61.5). No brief sentence runs past 25 words in the narrator's own prose. Pelagius l.1 runs to 26 words, but most of them are Pelagius's own words at Diospolis, so this is not a finding.
- **Card order.** All five follow Mark's order. Missing fields are left out: Pelagius has no otherNames, and Honoratus has no keyWorks and no "Their own words". keyWorks never goes past three. Each `uncertain` list opens with the brief's own caveat. The `"date": null` in source entries is the same schema batch 2 used, so it is not a finding here.
- **Length.** Rufinus (405 words, 2:30) and Pelagius (404, 2:30) are at the major cap. Paulinus is 323 words, Honoratus 324 and Sulpicius 326. Sulpicius is one word over "about 325", which is within "about", so this is not a finding. Every `briefLength` matches.
- **Who test (item 14).** Rufinus and Pelagius each have a body of work and a following. Paulinus and Sulpicius are recorder Whos, as the README says. Honoratus is a founder with a following (Lérins). The drafts carry no list lines. Those belong to the map build and were not checked here.

| Profile | Words | Est. length @162 | FK | Flesch |
|---|---|---|---|---|
| Rufinus of Aquileia (MAJOR) | 405 | 2:30 | 7.6 | 61.5 |
| Pelagius (MAJOR) | 404 | 2:30 | 7.4 | 64.3 |
| Paulinus of Milan | 323 | 2:00 | 7.1 | 65.1 |
| Sulpicius Severus | 326 | 2:01 | 6.6 | 70.6 |
| Honoratus of Arles | 324 | 2:00 | 6.6 | 69.6 |

---

## 1. Rufinus of Aquileia (MAJOR)

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | FAIL, minor (M1, M3) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS |
| 5 | No role for a witness | PASS (Fremantle, Palladius, Gennadius, Socrates, Richardson, Lightfoot named) |
| 6 | Partisan witness named and marked | PASS (Jerome and Rufinus each partisan on the other; Palladius and Gennadius "took his side") |
| 7 | Contested both sides | PASS (translation of Origen; author of the Defence; Anastasius; the scorpion) |
| 8 | Common names placed | PASS in the brief; card minor (M2) |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | PASS (2:30) |
| 11 | grade_text | PASS |
| 12 | Card order, caveat repeated | PASS |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |

**Quotes** (all exact, speaker confirmed)
- "the Barbarian was within sight of us; he had set fire to the city of Rhegium" and "as a solace from our troubles": Rufinus's own preface to Origen on Numbers, `npnf203_theodoret-jerome-gennadius-rufinus.xml` l.58989, 58997. The date 410 and Alaric come from the head note to that preface (l.58976–58978), which the brief rightly gives as Fremantle's date.
- "is inseparably bound to me in brotherly love": Jerome, Letter 4, `npnf206_jerome-principal-works.xml` l.3978. Jerome is the speaker.
- "underwent imprisonment and exile": Rufinus, Apology to Anastasius 2 (npnf203 l.45968).
- "after an absence of nearly 30 years": Apology to Anastasius 1 (l.45955). The note on "parentes" in that same line is Fremantle's, and the brief does not use it.
- "A more learned man or a kinder than he was not to be found among men": Palladius, Lausiac History 46.5, `palladius_lausiac-history_clarke1918.txt` l.501, in Palladius's own text. "Receiving at their own charges" is 46.6. Clarke's note 292.4 (l.1223), "Palladius takes Rufinus' part unhesitatingly", backs "who took his side", and Palladius's own remarks on Jerome (l.435, 475) back it too.
- "under the name of a friend I detected the snares of an enemy": Jerome, Apology I (npnf203 l.51054). It is part of a rhetorical question, quoted verbatim.
- "I am not a defender or a champion of Origen": Rufinus, Apology to Anastasius 7 (l.46070).
- "like the two fishes to the loaves": Rufinus's preface to his two added books (l.58786).
- "each contributing his several sentence to one common summary": Rufinus, Commentary on the Creed 2 (l.56670). The commentary itself frames this as tradition ("Our forefathers have handed down to us the tradition", l.56658).
- "the scorpion lies beneath the ground": Jerome, Preface to Ezekiel (npnf206 l.47996). The name Rufinus sits only in endnote 5438 (l.47992–47994). That note is the editor's, as the brief says.
- "opened to the Latin speaking church the greater part of the Greek literature" and "was not the least among the doctors of the church…": Gennadius 17 (npnf203 l.42467–42469). "Born 345, at Jerusalem about 390, died 410" in that line is Richardson's inline note, and the card attributes it to him correctly.
- Card: "lost in their native Greek" is Fremantle's prolegomena (l.44042). "has erred in respect to chronology" is Socrates II.1 (`npnf202_socrates-sozomen-ecclesiastical-histories.xml` l.5651, the text after Hartranft's note). "He descended into Hell" is Commentary 18 (l.57401). "where is the friend…" is Augustine, Letter 73 (`npnf101_augustine-confessions-letters.xml` l.32950; div3 LXXIII at l.32764). "especially the presbyter Rufinus, from the heresy of Origen" is Epiphanius, Letter 51 (npnf206 l.10977), and Jerome's Latin version is noted at l.13162. "would take in these heretical views without warning" is Jerome, Apology I.7 (npnf203 l.51302). "must bring his conscience to the bar of the divine majesty" is Anastasius (l.46151).

**Narrative checks**
- Six years plus two more "where Didymus lived": Apology to Apronianus II (l.49435). Melania "a Spaniard by origin, but afterwards belonged to Rome", a widow with a convent: Clarke l.497–501. That is fair for "a widow from Rome".
- The preface to On First Principles (l.45686–45760) shows the unnamed predecessor who purged "all the causes of stumbling", and the omitting of passages thought falsified by heretics. "cut only passages he believed heretics had put in" (card, records) is Rufinus's own word in the Apology to Anastasius 7 (l.46050–46064: "but only those as to which I had come to suspect…"). Correct.
- Chromatius's request "when the gates of Italy were broken through by Alaric": Rufinus's own preface (l.58719–58735).
- Concordia in Letter 81 is endnote 2489 (npnf206 l.18428), and the card correctly names it as Fremantle's edition. Lightfoot is quoted in the note at l.51373. Fremantle's "no reason to suppose… that the Pope passed sentence upon him, still less that he summoned him to Rome" is at l.44414. The letter dated 400 is at l.45937.

**Findings**
- **M1 MINOR (items 1, 6).** Card `uncertain` item 7 says "His imprisonment and exile in Egypt rest on his own word. Socrates repeats it as Rufinus's claim." The records witness has the same line ("Socrates IV.24 … repeats it as Rufinus's own claim"). Socrates says only that "Rufinus declares that he was not only a witness of these cruelties, but also one of the sufferers", about the soldiers driving the Egyptian monks from their oratories (npnf202 l.13741–13742). He says nothing of prison or exile. Fix: "His imprisonment and exile in Egypt rest on his own word. Socrates of Constantinople says only that Rufinus called himself a witness, and one of the sufferers, when the monks of Egypt were attacked." Make the same change in the records witness.
- **M2 MINOR (item 8).** Card `legacy.traces` item 2 reads "the Recognitions of Clement". Clement is a common name, and Gennadius's own line names him "Clement of Rome" (npnf203 l.42470). Fix: "the Recognitions of Clement of Rome".
- **M3 MINOR (items 1, 9).** Card `dates` ends "in Sicily in 410, when he wrote his preface to Origen on Numbers; dead by then or soon after, by Fremantle's note to Jerome". The clause cannot be read straight: he cannot be dead "by" the year in which he is writing. The note it cites says plainly "Rufinus who died a.d. 410, in Sicily" (npnf206 l.47992–47994), and the card's own `uncertain` item 8 says "dates his death to 410, in Sicily". Fix: "…in Sicily in 410, when he wrote his preface to Origen on Numbers; died there in 410, by Fremantle's note to Jerome".

---

## 2. Pelagius (MAJOR)

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | FAIL, minor (M3) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS |
| 5 | No role for a witness | PASS (Augustine, Warfield, Holmes, Fremantle, Gennadius named) |
| 6 | Partisan witness named and marked | PASS (Augustine and Jerome placed once as one side; Warfield "who takes Augustine's side") |
| 7 | Contested both sides | FAIL, minor (M1 date told plainly; M2 Zosimus's first verdict left out) |
| 8 | Common names placed | PASS |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | PASS (2:30) |
| 11 | grade_text | PASS |
| 12 | Card order, caveat repeated | PASS |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |

**Quotes** (all exact, speaker confirmed)
- "A man is able, if he likes, to be without sin": the charge read at the synod, in Augustine, On the Proceedings of Pelagius 16 (`npnf105_augustine-anti-pelagian-writings.xml` l.9736). "has been given to him by God" is Pelagius's own answer (l.9738). "I anathematize them as fools, not as heretics, for there is no dogma" is Pelagius (l.9740). "In communion with the Catholic Church" is the synod's verdict (l.10270, 10473). Heros and Lazarus were absent through "the severe indisposition of one of them" (l.9487).
- "a holy man, as I am told": Augustine, On the Merits III.1 (l.4627). The bracketed note after it is Warfield's ("—W.") and the brief does not use it.
- "Give what Thou commandest": Augustine, On the Gift of Perseverance 53 (l.22532), in Augustine's own words: "Which words of mine, Pelagius at Rome, when they were mentioned in his presence by a certain brother and fellow bishop of mine, could not bear… nearly came to a quarrel". It is correctly given to Augustine ("he says"). Warfield's retelling at l.799 is not used.
- "we are men", "Oh, blind madness!", "the force of nature": Warfield's English (l.792, 834), and the brief names it so. The Latin agrees: "Durum est, arduum est, non possumus, homines sumus… O c[a]ec[am] insaniam!" (`pelagius_epistula-ad-demetriadem-lat_migne.txt` l.1024–1026) and "ut vim quodammodo videatur habere naturae" (l.611). The plain-words telling "he always begins by showing what human nature can do… what they think impossible" matches ch. 2 (l.169–174: "Quoties… soleo prius humanae naturae vim qualitatemque monstrare… ne nihil prosit ad ea vocari, quae forte sibi impossibilia esse praesumpserit").
- "they will find that we so commend the nature of man as always to add the help of God's grace": Pelagius's letter to Innocent, in On the Grace of Christ 40 (l.11255). "almost persuaded me" is Augustine's own, as are the reading of grace as teaching (ch. 40), forgiveness (ch. 41) and the example of Christ (ch. 42) (l.11255–11300).
- "works of practical value for students" and "the heresiarch": Gennadius 43 (npnf203 l.42971). "does not scruple to brand Pelagius as a heretic" is Fremantle (npnf206 l.1728). "only by a course of most ingenious disingenuousness" is Warfield (l.910). "quite uncertain" is Holmes (l.2001). "and easily to keep the commandments of God, if he wishes" is the letter ascribed to Pelagius in Proceedings 54 (l.10381), and Augustine doubts it is his (l.10385), as the card says.

**Narrative checks**
- Africa in 411 fleeing Alaric with Caelestius, the African synods of 416, Innocent's agreement, the decree from Ravenna, the council of about 200 bishops on 1 May with nine canons, and Zosimus's condemnation: Warfield, l.880–941. Holmes says Augustine, Prosper and Gennadius call him Brito and Jerome ties him to the Scots (l.2001). Fremantle's "come to Rome in 409" (npnf206 l.869–870) and Diospolis "in 416" (l.42453) are correctly given.

**Findings**
- **M1 MINOR (item 7).** Brief l.1 says "Late in 415, fourteen bishops met at Diospolis". The date is told plainly, yet `records.json` carries it as a `contested_claim`: Fremantle's introduction to the Dialogue gives 416 (npnf206 l.42453). The card is careful ("B. B. Warfield's dates"). This is the batch 2 Damasus M2 pattern. Fix: "Late in 415, by B. B. Warfield's date, fourteen bishops…".
- **M2 MINOR (items 1, 7).** Brief l.9 and the card tell Rome as against him from the start: "Innocent… agreed… Innocent's successor Zosimus condemned him". The same witness the brief relies on says Zosimus first took his side. In September 417, "Zosimus, with the approbation of the clergy, declared both Pelagius and Cœlestius to be orthodox, and severely rebuked the Africans", then wavered and condemned them in 418 (Warfield, l.924–927, 941). Pelagius's letter to Innocent reached Zosimus, and it is the very letter the brief quotes in l.11. Leaving out his one Roman acquittal hides his side of the story. Fix for l.9: "…and Innocent, bishop of Rome, agreed. His successor Zosimus at first declared Pelagius orthodox in 417, Warfield says. In 418 the emperor banished the Pelagians from Rome, and Zosimus condemned him." Add the 417 verdict to the card's `keyWorks` "about" for the letter to Innocent, or to `uncertain`.
- **M3 MINOR (item 1; records).** Brief l.3 says "Augustine and Jerome of Strido worked together against Pelagius." The records claim behind it cites as witness "W. H. Fremantle's prolegomena… ; Who scan era 2 and Opus check notes". The last two are build notes, not sources. Fremantle supports less than "worked together": Jerome "engaged rather at the instance of others", "Augustin from Africa and Ctesiphon from Rome appealed to him" (npnf206 l.1712–1720), and he was "induced to interest himself in it by his increasing regard for Augustin" (l.42449). Fix for the brief: "Augustine of Hippo wrote book after book against him. Jerome of Strido, whom Augustine asked for help, wrote against him too." In the record, cite npnf206 l.1712–1720 and l.42449 and drop the build notes.

---

## 3. Paulinus of Milan

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | FAIL, minor (M1) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS |
| 5 | No role for a witness | PASS (Kaniecka, Mercator, Augustine, Günther named) |
| 6 | Partisan witness named and marked | PASS (the Life marked as hagiography, in Kaniecka's words) |
| 7 | Contested both sides | FAIL, minor (M2) |
| 8 | Common names placed | FAIL, minor (M3) |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | PASS (2:00) |
| 11 | grade_text | PASS |
| 12 | Card order, caveat repeated | PASS |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS (recorder Who) |

**Quotes** (all exact in Kaniecka's English, `paulinus-milan_vita-ambrosii_kaniecka1928.txt`; found by letters-only match because of OCR line breaks)
- "a fire in the shape of a small shield covered his head": Life 42 (l.4703). The rest of the scene follows the passage: dictating the 43rd Psalm, the face "like snow", "I became stiff and was unable to write…".
- "in which we now live and write": Life 51 (l.5219). "since indeed it is better to say nothing at all than to set forth something false": Life 2 (l.2250). "the most humble man and sinner Paulinus": Life 56 (l.5392).
- Card: "contains many interesting details…", "the Vita is something of a disappointment", "The integrity of the writer cannot be questioned" (l.1289–1296); "does not give evidence of any great theological depth or learning" (l.1029); "of five years before" (l.1017); "Of the life of Paulinus we know very little" (l.787). All are Kaniecka's own words.
- "Tell us their names" / "Is not one priest enough for you?": the Carthage record in Augustine, On Original Sin 3 (npnf105 l.11555–11559). Paulinus and Caelestius are the speakers. "all the objectionable points which had been alleged against him by the deacon Paulinus" is Augustine, ch. 8 (l.11605).

**Narrative checks**
- The petition (`collectio-avellana_…_guenther1895-csel35.txt` l.11489–11620): "cuius ego non damnationem sed correctionem semper optaui et opto" supports "What he had always wanted… was his correction". The thanks are given to God that the see ordered the charges condemned, and then "quo gratiam referam tantae sedi et sententiis iustissimis" (l.11608). So "thanks Zosimus for ordering…" is a fair telling. The summons through Basiliscus is at l.11610, and Günther's date of 8 November 417 at l.11515.
- Mercator: "Diacono [sanctae] memoriae Ambrosii Mediolanensis episcopi est accusatus" (`marius-mercator_opera-omnia-lat_migne-pl48.txt` l.3688). The card is right that Mercator's Latin does not name him as the biographer. (A note in the same Migne volume, l.3660–3667, cites Baronius for the identification.)
- The Life drawing on those who served Ambrose and on Marcellina (Kaniecka l.2885–2895), hagiography "to edify" and "pays no heed whatever to chronological details" (l.~1270–1277), and minor orders, deacon, and Isidore's "presbyter" (l.~840–870): all verified.

**Findings**
- **M1 MINOR (items 1, 5).** Brief l.7 and card `uncertain` item 2 call Marius Mercator "a Latin layman who wrote against the Pelagians". No witness held here states that he was a layman. In the Migne volume it is Jean Garnier's guess: "Non fuit umquam, opinor, episcopus, immo neque presbyter, neque etiam forte diaconus" (l.488) and "si laicus perpetuum vixerit" (l.561). The plain phrase "a Latin layman" is the wording of the vendored file's own build header (l.10, "Content note"). An identifier must "add no claim". Fix: "Marius Mercator, a Latin writer against the Pelagians," in both places.
- **M2 MINOR (item 7).** Brief l.7 says "At Carthage in 412". The year is told plainly, yet `records.json` holds it as a `contested_claim`: Kaniecka's note gives 416 (Kaniecka l.1041). This is the same pattern as Pelagius M1. Fix: "At Carthage in 412, by B. B. Warfield's date," (Warfield: "Early in 412, or, less probably… 411", npnf105 l.885).
- **M3 MINOR (item 8).** The subject's first mention is plain "Paulinus" (brief l.1, "Paulinus was taking it down"), and "Paulinus of Milan" comes only in l.3. Paulinus is a common name, and Kaniecka warns that he "must not be confused with Paulinus, the bishop of Nola" (l.814). The pattern applies the rule to the subject's own name. Fix: l.1 "Paulinus of Milan was taking it down." and l.3 "Paulinus tells this in his Life of Ambrose…".
- **M4 MINOR (records tag).** The records claim "The accuser of Caelestius is the author of the Life of Ambrose" is tagged Widely Accepted. Its own witness field says "Inference", and the card calls it "an inference" that Kaniecka draws. Fix: tag it Dominant Modern Reconstruction, naming Kaniecka (and Baronius as cited in the Mercator volume's note, l.3660–3667), or make the card's wording match the tag.

---

## 4. Sulpicius Severus

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | PASS |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS |
| 5 | No role for a witness | PASS (Gennadius, Roberts, Richardson, Paulinus of Nola named) |
| 6 | Partisan witness named and marked | PASS |
| 7 | Contested both sides | PASS (Pelagian charge: Gennadius v. Roberts; dates: Roberts v. Richardson) |
| 8 | Common names placed | PASS |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | PASS (2:01) |
| 11 | grade_text | PASS |
| 12 | Card order, caveat repeated | PASS |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS (recorder Who) |
| — | Confidence handling (pattern, "Confidence") | FAIL, minor (M1) |

**Quotes** (all exact, speaker confirmed; `npnf211_sulpitius-severus-vincent-lerins-cassian.xml` unless marked)
- The scene is Life of Martin 25 (l.1826–1850): water for his hands, his feet washed at evening, "nor had I sufficient courage to resist" (told in plain words, not quoted), and Paulinus held up as one who sold everything for the poor.
- "the small treatise which I had written concerning his life" (l.2171) and "they have brought word that Martin is dead" (l.2191): Sulpicius, Letter II. The dream is "in the morning hours" (l.2155).
- "the accusers were as distasteful to me as the accused": Sacred History II.50 (l.11642). Martin's plea to Maximus "not [to] shed the blood" is at l.11655.
- "distinguished by his birth", "wrote small books which are far from despicable", "In his old age, he was led astray by the Pelagians": Gennadius 19 (npnf203 l.42537–42555). The brief correctly uses the Richardson English and not the different wording in Roberts's introduction (l.478).
- "no ground for any such conclusion" (l.380), "over-credulous in his acceptance of the miraculous" (l.389), "has been called" "the Christian Sallust" (l.397), "Sulpitius is not always a trustworthy" (l.448) and "as is generally supposed" (l.352) are all Roberts. "He is the purest of all the ecclesiastical writers" is Scaliger as Roberts quotes him (l.478). "his name was known from Armenia to Egypt…" is Farrar as Roberts quotes him (l.491). "a historian worthy of his faith and of his life" is Paulinus of Nola, Letter 5, as Roberts quotes him (l.463). Each is given to the right voice.

**Findings**
- **M1 MINOR (confidence handling; item 1).** Brief l.3 says "Alexander Roberts, who translated him, says he gave up a name at the bar after his wife died young." `records.json` tags this Inferential-Thin, and the card says Roberts "names no source for these, and the sources used here do not give them" (Roberts l.352–372 confirms he names none). The pattern says Inferential-Thin is "said as an inference with what it rests on, or kept to the card". The brief tells it as a plain report. Fix: "Alexander Roberts, who translated him, says without naming a source that he gave up a name at the bar after his wife died young." Or drop the sentence and keep it on the card.

---

## 5. Honoratus of Arles

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | FAIL, blocking on the card (B1) |
| 2 | Quotes verbatim | PASS (brief quotes none; card quotes checked) |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS |
| 5 | No role for a witness | PASS (Hilary, Eucherius, Gibson, Cassian, Heurtley, Gennadius named) |
| 6 | Partisan witness named and marked | PASS (one witness, a sermon of praise by his disciple, said early) |
| 7 | Contested both sides | PASS |
| 8 | Common names placed | FAIL, minor (M1) |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | PASS (2:00) |
| 11 | grade_text | PASS |
| 12 | Card order, caveat repeated | PASS |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |

**Narrative checks** (Hilary's Latin, `hilary-arles_sermo-de-vita-sancti-honorati_migne-pl50.txt`)
- Empty island: "Vacantem… insulam ob nimietatem squaloris, et inaccessam venenatorum animalium metu" (l.677–678). Ps. 90 "Super aspidem et basiliscum ambulabis" (l.689). "Ingreditur itaque impavidus… cedit turba serpentium" (l.693–695). Presbyter against his will (l.706–712). Church and cells (l.718–720). Many lands and tongues, "tam moribus quam linguis dissona" (l.875).
- Consular family (l.221). Father kept him from baptism, "timens ne totus… religionis amore raperetur" (l.203–204). Short hair and fasting (l.369–373). The elder brother followed, "Senior juniorem secutus" (l.423). Property sold for the poor (l.544–549). Caprasius (l.579). The Achaean shore, and Venantius dead at Methone (l.556–563).
- Hilary won with tears (l.1145, 1212–1236). The church at Arles divided "de assumendo episcopo" and its discord ended (l.1381–1390). Last sermon on Epiphany (l.1416–1417). Eucherius's "Mel, inquit, suum ceris reddidisti" (l.1097–1099). Gold coin to a poor man (l.1028–1031). Two days or three (l.1155, 1182).
- Eucherius, De laude eremi: "Honorato auctore fundata… Haec nunc successorem ejus tenet, Maximum" (`eucherius-lyon_de-laude-eremi_migne-pl50.txt` l.718–730). Cassian's prefaces: "holy brothers Honoratus and Eucherius" (npnf211 l.36721) and "Honoratus, a Bishop blessed in name as well as merits" (l.42293). Heurtley's "Now St. Honorat" (l.11777). Gennadius 70, "of so great practical value to many" (npnf203 l.43399). All verified. Gibson's "Honoratus died in January, 429" is at npnf211 l.15566.

**Findings**
- **B1 BLOCKING (items 1, 5; witness reasoning reversed).** Card `uncertain` item 3 says "Gibson's dates rest on his reading of Cassian's prefaces, where Honoratus is styled brother in one and bishop in the next." The records witness has the same idea: "Edgar Gibson, Prolegomena to Cassian, from the prefaces to the Conferences". Gibson reasons the other way round. He treats 426 and January 429 as known and uses them to date Cassian's prefaces: "as Honoratus was raised to the see of Arles in 426, the volume must have been published not later than that year, or he would have been termed 'Episcopus'…", and Part III "cannot be later than 428, as Honoratus died in January, 429" (npnf211 l.15545–15566). The card gives Gibson an argument he does not make and makes his dates look like inferences from Cassian. Fix for the card: "Gibson gives 426 and January 429 without naming a source. He uses them to date Cassian's prefaces, where Honoratus is styled brother in one and bishop in the next. His date of 410 for the founding of Lérins is also his own." Make the same change in the records witness. (Migne's note to Hilary's sermon gives a second accession date, the end of 426 or the start of 427, at l.1500. It may be added as a second side, but leaving it out is not a fault.)
- **M1 MINOR (item 8).** In the brief the subject is only ever "Honoratus" (first at l.1, "Honoratus went in unafraid"). He never carries "of Arles", although the name is common and the pattern applies the rule to the subject's own name. Also, "Edgar Gibson, Cassian's translator" (l.9) is the brief's only mention of Cassian, with no first name or context, while the card has "John Cassian". Fix: l.1 "Honoratus, later bishop of Arles, went in unafraid…". l.9: "Edgar Gibson, who translated John Cassian, dates his death to January 429."

---

## 6. Batch README.md

- **README-M1 MINOR.** The README orders the batch "by death or last attested year: Rufinus (411), Pelagius (about 420)… Sulpicius Severus (about 425)…". These years match neither the cards nor the witnesses they hold. For Rufinus, Fremantle and Richardson give 410 (card `uncertain` item 8; npnf203 l.42466). For Sulpicius, Roberts gives 420 and Richardson about 410 (card `dates`). For Pelagius, the records say no held source gives his death and the census figure "rests on no held witness". The README is internal, but it is where a later reviewer looks first. Fix: say the years are the Who scan's (census) years, or give Rufinus 410, Pelagius "condemned 418, death not given" and Sulpicius "about 420 or 410"; the order does not change.
- The rest of the README is correct. It names the nine ids, the major marks, the recorder Whos, and the card and records schema. The card schema matches the five cards.

---

## Totals (part A)

- **Blocking: 1.** Honoratus B1 (Gibson's reasoning reversed on the card and in records).
- **Minor: 13.** Rufinus M1–M3, Pelagius M1–M3, Paulinus M1–M4, Sulpicius M1, Honoratus M1, README-M1.

Patterns across part A:
1. **Witness reasoning or witness wording swapped.** Honoratus B1 gives Gibson an argument he runs backwards. Paulinus M1 takes "layman" from Garnier's guess and the build header. Rufinus M1 makes Socrates say more than he does.
2. **Contested dates told plainly in the brief** while `records.json` carries the contested claim (Pelagius M1, Paulinus M2). Rufinus's "by W. H. Fremantle's date" is the model.
3. **One side of a reversal left out.** Pelagius M2: Zosimus's first verdict in his favour.
4. **Records hygiene.** A build note is cited as a witness (Pelagius M3), and a tag does not match the text (Paulinus M4, Sulpicius M1).

## R1 review: era 2 batch 4, part B (Church Family Tree Who profiles)

Reviewer: independent, first sight of these drafts. Bar: `Who_Profile_Pattern.md` review checklist 1 to 14 and the standards it points to; `CLAUDE.md` "Trust and source fidelity" and "Accessible and rigorous"; and the failure types of the era 2 batch 1 and batch 2 R1 reviews, above all the witness swap. I did not edit the drafts. I made no paid or model-API calls and used no web. Readability and quote search ran on local scripts only.

Profiles: `john-cassian` (MAJOR), `palladius-of-helenopolis`, `possidius-of-calama`, `philostorgius` (all three not major; recorder Whos per the batch README). Files are in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era2/batch4/`. Brief line numbers refer to the `.brief.txt` files, where each paragraph is one line (paragraphs fall on lines 1, 3, 5, 7, 9, 11).

Method. Every quotation in the four briefs and cards was searched in its vendored file with whitespace-tolerant, tag-stripping matching, and read in context. For each attributed sentence I checked who is speaking at that place: the ancient author, a document or speaker he reports, the translator's introduction, or a footnote. Every factual sentence of each brief and each card item was checked against the passage it rests on. records.json claims, tags, contested_claims and absent_details were compared with brief and card. Readability came from `engine.m1.gates.grade_text`, run from the repo root. Length assumes 162 words a minute. Line numbers point to files under `cic/texts/` unless marked otherwise.

## Applies to all four

- **Audio = brief.** Each audio script is identical to its brief once `[calmly] ` and `[warmly] ` are removed (checked by script). Each opens with `[calmly]` and carries one `[warmly]`, before the final sentence. No other tag; no tag in any brief or card.
- **Readability.** All four pass (FK at most 10, Flesch at least 60). Philostorgius (60.5) sits at the Flesch floor. No sentence in any brief runs past 25 words.
- **Card order.** All four follow Mark's order. Missing fields are left out (Philostorgius has no otherNames). keyWorks never exceeds three. Each `uncertain` opens with the brief's own caveat.
- **Length.** John Cassian 404 words, 2:30, is just under the major cap of about 405. Palladius 325 and Possidius 325 are at the non-major ceiling; Philostorgius 324. Every `briefLength` matches.
- **Who test (item 14).** John Cassian has a body of work and a following. Palladius, Possidius and Philostorgius are recorder Whos, the Auxentius form, as the README says. The drafts carry no list lines; those belong to the map build and were not checked here.

| Profile | Words | Est. length @162 | FK | Flesch |
|---|---|---|---|---|
| John Cassian (MAJOR) | 404 | 2:30 | 7.6 | 65.6 |
| Palladius of Helenopolis | 325 | 2:00 | 7.3 | 63.0 |
| Possidius of Calama | 325 | 2:00 | 6.8 | 72.0 |
| Philostorgius | 324 | 2:00 | 7.9 | 60.5 |

---

## 1. John Cassian (MAJOR)

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | PASS, with M1 and M2 |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS, with a floating time anchor (M1) |
| 5 | No role for a witness | PASS (Gennadius, Gibson, Richardson, Bright, Benedict named) |
| 6 | Partisan witness named and marked | PASS (Gennadius "who takes Cassian's side"; Prosper "an ardent Augustinian") |
| 7 | Contested both sides | PASS (birthplace: Gennadius v. Gibson; Conference XIII: Prosper, Gennadius, Gibson) |
| 8 | Common names placed | FAIL, minor (M3 brief, M5 card) |
| 9 | One term | PASS, with M4 |
| 10 | Story, scene, disputes in place, length | PASS (2:30) |
| 11 | grade_text | PASS |
| 12 | Card order, caveat repeated | PASS |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |

**Quotes** (all exact, speaker confirmed)
- "they have taken away my God from me" (brief l.1): Sarapion's cry in Conference X.3, Cassian's first-person narrative (`npnf211_sulpitius-severus-vincent-lerins-cassian.xml` l.36052). Theophilus's festal letter against the Anthropomorphites, Photinus the learned deacon from Cappadocia, Sarapion's tears and fall to the ground, and "all of us" present (l.35950–36052) support the whole scene.
- "Scythian by race" (brief l.3, card): Gennadius, Lives 62, in Richardson's translation (`npnf203_theodoret-jerome-gennadius-rufinus.xml` l.43243 region).
- "I was admitted into the sacred ministry by the Bishop John, of blessed memory" (brief l.5): Cassian, On the Incarnation VII.31 (npnf211 l.55143). Gennadius's "ordained deacon by bishop John the Great, at Constantinople" and Gibson's "ordained deacon by S. Chrysostom" (npnf211 Prolegomena, l.15330 region) support the setting and the identification.
- "about the way to improve our character" (brief l.5): Cassian, Institutes, Preface (npnf211 l.16513). The skipping of "God's miracles and signs" is in the same sentence.
- "seem opposed to each other, but really are in harmony" and "inclined to will what is good" (brief l.7): Chaeremon's speech in Conference XIII.11 (npnf211 l.38029–38033). Gibson also quotes the first phrase as Prosper's sixth proposition (l.15840), but the brief cites the Conference, and the words are there. Correct speaker.
- "an ardent Augustinian" and "the teaching of Augustine was one-sided and required to be balanced" (brief l.7, card): Gibson's Prolegomena (npnf211 l.15700 region; l.15925 region). Gibson's own words, not Bright's.
- "which the church of God finds salutary" (brief l.7, card): Gennadius, Lives 85 (npnf203 l.43670).
- "made an end, both of writing and living, at Marseilles" (brief l.9): Gennadius, Lives 62.
- Card: "He wrote from experience, and in forcible language" (Gennadius 62); "revising and condensing certain works of Saint Cassianus, he compressed them into one volume" (Gennadius 64, npnf203 l.43295); "the first organizer and systematizer, of Western monachism" (Gibson, l.15490 region); "Never formally canonized", "the blessed Cassian", "a verdict of guilty must be returned on the charge of Semi-Pelagianism", "it is impossible to speak with certainty", "how far they really represent the discourses actually spoken by the Egyptian", "never once names him directly", "Of his family we know nothing" (all Gibson, l.14940–15930). All exact.

**Narrative checks**
- Gibson doubts "Scytha", suggests Scete, and thinks a Western, perhaps Provençal, birth most probable (l.14948–15028). Bethlehem with Germanus "while still young", and the two Egyptian visits "between 380 and 400" (l.15100–15330). Faithful.
- Two monasteries at Marseilles, one for men and one for women (Gennadius 62; Gibson l.15470). Institutes in twelve books for Castor, Bishop of Apta Julia (Gibson l.15520). Leo "then Archdeacon of Rome" (Gibson l.15420). Prosper a layman (Gibson l.15700). Benedict "enjoins that the Conferences should be read daily" (Gibson l.15495 region). Rule 42 and 73 (`benedict_rule-of-st-benedict-lat-eng_hunter-blair1907.txt` l.6839–6892, l.10410–10450). Faithful.
- Card dates: Gibson, born about 360 (l.15060 region); last known event Prosper's book "not earlier than 432", death "shortly afterwards" (l.15903–15912). Richardson's heading note "Johannes Cassianus died 450" is his, and he is the named translator (npnf203 l.38386–38400). Faithful.
- records.json tags match the brief and card. Both disputes have `contested_claim` records.

**Findings**
- **M1 MINOR.** Brief l.3: "Gennadius of Marseilles, writing later that century, calls Cassian 'Scythian by race.'" No century has been named. The only time the listener has is the Scete scene, which Gibson's note dates to 399 (npnf211 l.35967). Read against that, "later that century" puts Gennadius in the 300s, which is wrong. Gibson dates him to a.d. 495 (l.14969) and Richardson puts the bulk of the work about 480 (npnf203 l.38473–38486). Fix: "Gennadius of Marseilles, writing late in the next century, calls Cassian..." or "Gennadius of Marseilles, writing about fifty years after Cassian's death, ..." (both rest on Gibson's 495 and his "soon after 432"). The plainest is "Gennadius of Marseilles, who wrote late in the fifth century, calls Cassian..." (Gibson, Richardson).
- **M2 MINOR.** Brief l.7: "Gennadius, who takes Cassian's side, says Prosper's book attacked works 'which the church of God finds salutary.'" Gennadius does not say the book is Prosper's. He says "I regard as his also an anonymous book against certain works of Cassianus" (npnf203 l.43670). The card says this correctly ("believed an anonymous book ... was Prosper's"); the brief drops the hedge and gives Gennadius a certainty he does not claim. The authorship itself is not in doubt, since Gibson names the book as Prosper's Contra Collatorem (npnf211 l.15790 region). Fix: "Gennadius, who takes Cassian's side, took an unsigned attack on works 'which the church of God finds salutary' to be Prosper's."
- **M3 MINOR.** Item 8. Brief l.7: "the old man Chaeremon" has no identifier, and the name could mean more than one person. Fix: "the old man Chaeremon, a hermit near Panephysis in the Nile delta," (Gibson, Prolegomena, l.15120–15140, drawn from Conference XI.i–iii).
- **M4 MINOR.** Card uncertain #4: "The name Semi-Pelagian is Gibson's, and William Bright's, whom he quotes; Cassian does not use it." This reads as if Gibson coined the name. He does not claim to; he uses an existing name for the "School of Marseilles" (l.15620 region). Fix: "Gibson, and William Bright whom he quotes, call this teaching Semi-Pelagian. Cassian does not use the word." Then keep the two Gibson quotations.
- **M5 MINOR.** Item 8, card. Card uncertain #1: "Gibson adds that Photius calls him a Roman." Photius has no identifier at his first mention in the card. Fix: "Photius of Constantinople" (Walford's title page, `philostorgius_ecclesiastical-history_walford1855.txt` l.21–23, "Photius, Patriarch of Constantinople").

---

## 2. Palladius of Helenopolis

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | PASS |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS |
| 5 | No role for a witness | PASS (Clarke, Moore, Butler, Bigot, Sozomen named) |
| 6 | Partisan witness named and marked | FAIL (B1: Epiphanius and Jerome not placed in the brief) |
| 7 | Contested both sides | FAIL (B1); PASS on the Dialogue's authorship (Moore and Butler v. Bigot) |
| 8 | Common names placed | FAIL, minor (M1 brief, M2 card) |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | PASS (2:00) |
| 11 | grade_text | PASS |
| 12 | Card order, caveat repeated | PASS |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS (recorder Who) |

**Quotes** (all exact, speaker confirmed)
- "This is my bishopric, for gluttony ordained me." and "You have to be ordained bishop, and toil much and be afflicted." (brief l.3): Lausiac History XXXV.10–11, Palladius's own words and John of Lycopolis's reply (`palladius_lausiac-history_clarke1918.txt` l.423–425).
- "having become embroiled in the disturbance connected with the blessed John" (brief l.5): XXXV.12 (l.427). Clarke's note 238 reads "Chrysostom" (l.1113). Correctly given to Clarke.
- "a disciple of Evagrius" (brief l.5, card): Sozomen VI.29 (`npnf202_socrates-sozomen-ecclesiastical-histories.xml` l.13711).
- "Palladius of Galatia", "the heresy of Origen" (brief l.9, card): Epiphanius's letter, Jerome Letter 51 (`npnf206_jerome-principal-works.xml` l.11123). Correct speaker: Epiphanius, not Jerome.
- "no better than a villainous slave" (brief l.9, card): Jerome, Against the Pelagians, Prologue (npnf206 l.42618). Jerome's own words.
- "into the shade his splendid achievements" (brief l.9): Lausiac History XXXVI.6, Palladius's narration (Clarke l.433).
- "I welcomed all the hardship of the way so long as I might meet some man that loved God" (brief l.11): Prologue 5 (Clarke l.199 region). This is the Prologue, not the Preface Butler thinks spurious (note 1, l.633).
- Card: Sozomen's "composed by the monk Palladius, who was a disciple of Evagrius"; Budge's Syriac heading "Palladius, the Bishop of the city of Helenopolis" (`palladius_paradise-v1-syriac_budge1907.txt` l.721); Innocent's letter in Sozomen VIII.26 (npnf202 l.44399); Socrates VII.36, "was transferred from Helenopolis to Aspuna" (npnf202 l.21072); Fremantle's edition on Tillemont (npnf206 l.42616); Clarke's note 360, "A transparent device by which Palladius speaks about himself" (l.1359). All exact.

**Narrative checks**
- The journey to John of Lycopolis follows XXXV.3–4: Evagrius's wish, the closed cell, eighteen days "partly on foot, and partly by boat on the river", John at the window (l.423). Galatia (XXXV.5), Alexandria and Nitria (I, VII), illness to Alexandria, Palestine and Bithynia (XXXV.12). Faithful.
- Moore: the treatise anonymous, generally given to Palladius; Butler's 1908 monograph; "Emeritus Bigot" first editor, who "goes so far as to suggest that another Palladius succeeded the Lausiac author at Helenopolis, and wrote the Dialogue" (`palladius_dialogue-life-of-chrysostom_moore1921.txt` l.729–935). The Rome arrival with the edict (l.2627–2634) and Syene (l.10754–10776) are third-person reports in the Dialogue, so they hold whoever wrote it. Faithful.
- Lausus as chamberlain (heading, l.181; note 6, l.643); journeys of thirty days on foot (Prologue 5). Faithful.

**Findings**
- **B1 BLOCKING.** Items 6 and 7. Brief l.9: "Jerome called him 'no better than a villainous slave.'" The brief tells as settled that Jerome's Palladius is this Palladius. The source the card cites says it is disputed: the note on that very passage in Fremantle's edition reads "According to Epiphanius, as well as Jerome, he was tainted with Origenism. Tillemont, however, thinks that another Palladius may be referred to in these passages" (npnf206 l.42614–42617). "These passages" covers both Epiphanius's letter and Jerome's prologue. The card's own What is uncertain (#4) and the records.json witness line both report Tillemont's doubt. The brief does not, and records.json tags the claim Widely Accepted with no `contested_claim`. This is the Damasus and Priscillian B1 type of batch 2: the brief tells plainly what the card and records present as disputed. The same paragraph also gives Epiphanius's and Jerome's charges without saying they were his opponents in the quarrel over Origen, which the card places (uncertain #1). The charge reads as a neutral report. Fix (all wording checked against the files cited): "Epiphanius of Salamis, in a letter Jerome of Strido put into Latin, warned that 'Palladius of Galatia' taught 'the heresy of Origen.' Jerome wrote that a Palladius, 'no better than a villainous slave,' tried to revive the same heresy. The notes to Fremantle's edition of Jerome take both for this man, and report that Tillemont thought another Palladius may be meant. Palladius wrote that Jerome's temper threw 'into the shade his splendid achievements.'" The Jerome sentence rests on "Palladius, no better than a villainous slave, tried to impart energy to the same heresy" (l.42618). Use "the notes to Fremantle's edition", not "Fremantle": his preface says Lewis and Martley "added most of the notes" (npnf206 l.486–490). The same correction applies to records.json ("identification in Fremantle's note"). The fix adds about 28 words to a brief already at 325. Trim elsewhere: the Sozomen line (l.5) and "It tells of monks and holy women he met or heard of" (l.11) are both already on the card. In records.json, retag "Jerome called him ..." Contested. Add a `contested_claim`: "Whether the Palladius of Epiphanius's letter and of Jerome's prologue is Palladius of Helenopolis". Sides: the notes to Fremantle's edition, and Clarke's note 241 that the dislike was mutual (l.1119), yes; Tillemont, as those notes report, perhaps another.
- **M1 MINOR.** Item 8 and "no statements with no context". Brief l.7: "follows Cuthbert Butler in giving it to Palladius." Moore and Bigot are each given a role, but Butler is not, and a listener does not know him. Fix: "follows Cuthbert Butler, who edited the Lausiac History, in giving it to Palladius" (Moore l.903–906, "to whom we owe an edition of the Lausiac History (Cambridge, 1904)").
- **M2 MINOR.** Card uncertain #4: "Tillemont" has no context at first mention. Fix: "Tillemont, author of the Mémoires of 1707," (Fremantle's Prolegomena, npnf206 l.1958, "Tillemont in his painstaking Mémoires (Paris, 1707)").

---

## 3. Possidius of Calama

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | PASS |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS |
| 5 | No role for a witness | PASS (Weiskotten, Cunningham, Augustine, Prosper named) |
| 6 | Partisan witness named and marked | PASS (the Life marked as a friend's memorial written to build up the church) |
| 7 | Contested both sides | PASS (the 408 bishop and the 437 Posidius told as inferences, with their basis) |
| 8 | Common names placed | FAIL, minor (M1 card) |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | PASS (2:00) |
| 11 | grade_text | PASS |
| 12 | Card order, caveat repeated | PASS |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS (recorder Who) |

**Quotes** (all exact, speaker confirmed)
- "that He may take me from this world unto Himself" (brief l.1): Augustine's words at table, reported by Possidius, Life 29 (`possidius_vita-augustini_weiskotten1919.txt` l.4142 region; Latin "aut certe ut sese de hoc seculo ad se accipiat", l.4110 region).
- "for almost forty years" and "continue to emulate and imitate him in this world" (brief l.3, l.11): Life, closing prayer (l.5059–5060).
- "the things that I have seen in him and heard from him" (brief l.3): Life, Preface (l.1527).
- "in which he lay folded double" (brief l.5): Augustine, Letter 91.8 (`npnf101_augustine-confessions-letters.xml` l.37414).
- "you will find one who is very much the same as myself" (brief l.5, card): Letter 101.1, to Memor, "My Brother and Colleague" (npnf101 l.40480–40510).
- "while we stood by and watched and prayed" (brief l.9): Life 31 (l.4979).
- Card: "in a way more likely to promote their welfare than you do yourself" (Letter 104.1, l.41871); "with the Lord's bread" (Letter 101.1); "from the library of the church of Hippo" (Life 18, l.3094); "He may have gone to Italy, but there is no evidence to that effect" (Weiskotten, l.479–480); "Possidius Calamensis" (Gesta of 411, `pl11-zeno-optatus-collatio-carthaginiensis_migne.txt` l.113084). All exact.

**Narrative checks**
- Siege of Hippo, the sea-coast cut off, the bishops taking refuge, the third month and the fever (Life 28–29, l.4080–4142). Faithful.
- The 408 riot: stoned three times, then fire, the bishop in the crevice (Letter 91.8, dated a.d. 408 at l.37196). Unnamed there; Letter 104 (a.d. 409) speaks of "my brother Possidius" and Nectarius's fears for the citizens; Cunningham's note on Letter 245 names Possidius as the bishop of 91.8 (l.57062–57064). The brief tells it as an inference. Faithful.
- The seven Catholic speakers of 411 (PL 11 l.113064–113084). Prosper's 437 entry, "quorum Posidius et Novatus ac Severianus clariores erant ... etiam civitatibus pelleret" (`prosper_chronica-minora-1-lat_mommsen1892.txt` l.54395–54399). Weiskotten's identification (l.475–479). Faithful.
- Card: Weiskotten's "two main sources" (l.124), "practically unknown" (l.289–290), birth 360–370 and see from 397 (l.324–327), Calama about forty miles from Hippo (l.512). The Life 12 ambush of an unnamed bishop of Calama (l.2420–2467), and Cunningham's note to Letter 88 naming Possidius (l.36712–36714). Faithful.
- records.json matches; the inferences are tagged and noted.

**Findings**
- **M1 MINOR.** Item 8, card uncertain #3: "names Possidius as the bishop Crispinus was charged with trying to kill." Crispinus has no identifier, and a listener does not know him. Fix: "Crispinus, the Donatist bishop of Calama," (Cunningham's heading to Letter 66, npnf101 l.32099).

---

## 4. Philostorgius

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | PASS, with one card item that names a person the source leaves open (M2) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS |
| 5 | No role for a witness | PASS (Photius, Walford, Quasten, Pearse named) |
| 6 | Partisan witness named and marked | PASS (Photius "hostile throughout", l.3; Philostorgius placed as of Eunomius's party, l.1) |
| 7 | Contested both sides | PASS (birth year kept to the card with both sides; the brief gives no year) |
| 8 | Common names placed | FAIL, minor (M1) |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | PASS (2:00) |
| 11 | grade_text | PASS (Flesch 60.5, at the floor) |
| 12 | Card order, caveat repeated | PASS |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS (recorder Who) |

**Quotes** (all exact, speaker confirmed)
- "is not ashamed to exalt this lisp into a mark of great grace and elegance" (brief l.1): Photius, Epitome X.6 (`philostorgius_ecclesiastical-history_walford1855.txt` l.382). The brief gives it to Photius, correctly.
- "impious contriver of lies" (brief l.3, card): Photius, II.11 (l.132).
- "the consubstantial faith", "her brothers, then her father" (brief l.5): Photius, IX.9, reporting Philostorgius (l.348). The brief frames the paragraph "Through Photius".
- "a style well suited to learners" (brief l.7): Photius, VIII.18 (l.328). "not even by His own only-begotten Son" (brief l.7): Photius, II.3 (l.116). "on behalf of the Christians" (brief l.7): Photius, X.10 (l.390). The paragraph opens on "Photius names", and l.3 has said the book survives only in his summary. These are Photius's English words reporting Philostorgius, and the brief does not offer them as Philostorgius's own.
- "Athanasius must be judged a mere child in comparison with them" (brief l.11): the Suidas fragment headed "IN THE WORDS OF PHILOSTORGIUS" (l.472). It is the one passage the brief gives as his own words, and it says the dictionary keeps it.
- Card: "an encomium on the heretical party, and an attack and assault upon the orthodox, rather than a history" (Epitome opening, l.82); "does not blush to avow" (III.21, l.190); "inventions of the author" (IX.1, l.332); "rather inclined to credulity" (Walford's Biographical Notice, l.40); "that heresy" (fragment, l.472). All exact.

**Narrative checks**
- Twenty years old at Constantinople (X.6). Anysius a presbyter at Borissus, "a village of the further part of Cappadocia"; Eulampia; Carterius a Eunomian (IX.9). Aetius and Eunomius leaders of the "unlikeness" party (IV.12, l.230). Twelve books, from Arius and Alexander to Valentinian the Younger, the initials spelling his name (l.82). Walford's 425, his hostile-throughout and his remote countries (l.36–40). Faithful.
- Card: Walford's 364 and Quasten's 368 and "layman" (l.36, l.48); Quasten on "excellent sources no longer extant, especially documents of Arian origin" (l.54); Walford's appointment date 853 for Photius (l.38); Pearse named as transcriber (l.6, l.68). Faithful.
- records.json matches. The birth-year `contested_claim` is in place.

**Findings**
- **M1 MINOR.** Item 8 and "no statements with no context". Brief l.7: "another against Porphyry 'on behalf of the Christians.'" A general listener does not know Porphyry, and the bare name gives no context. Fix: "another against Porphyry of Tyre, a pagan critic of the Gospels, 'on behalf of the Christians.'" The source is Socrates III.23, who quotes Libanius on Julian attacking the Christian books as "wiser and more skillful than the Tyrian old man", with the note "Porphyry. See above, I. 9" (npnf202 l.11730–11735). Constantine's letter in Socrates I.9 calls him "that enemy of piety" (l.3366–3370). If a shorter fix is wanted: "against Porphyry of Tyre" (npnf202 l.11733–11735).
- **M2 MINOR.** Item 1, card uncertain #4: "Photius reports that he told how Basil of Caesarea died of remorse after reading Eunomius's first book against him." Walford's English does not name the man who died: "not only Basil the Great, but also Apollinaris, wrote against the Apology of Eunomius; but that Eunomius replied to him in five books, and that when he had read only the first of these, he was struck with such profound remorse that he died" (VIII.12, l.316). "Him" follows two names, and the nearest is Apollinaris. The card settles a referent the cited text leaves open. Fix: "Photius reports his story that Eunomius answered a critic in five books, and that the critic died of remorse after reading the first. Walford's English leaves open whether Basil of Caesarea or Apollinaris is meant. Photius calls it falsehood."

---

## Totals, part B

| Profile | Blocking | Minor |
|---|---|---|
| John Cassian | 0 | 5 (M1–M5) |
| Palladius of Helenopolis | 1 (B1) | 2 (M1–M2) |
| Possidius of Calama | 0 | 1 (M1) |
| Philostorgius | 0 | 2 (M1–M2) |
| **Part B** | **1** | **10** |

No witness swap was found in part B. Every quotation was confirmed at its place in the vendored file, with its speaker: Cassian's narrative against Chaeremon's speech, Gennadius against Richardson's notes, Gibson against Bright, and Photius against the Suidas fragment.
