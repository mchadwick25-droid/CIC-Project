# R1 review: nine Who profiles, era 2 batch 6

Two independent Opus reviewers, each at first sight of its drafts, reviewed the batch in two parts: part A (Liberius of Rome, Marcellus of Ancyra, Moses the Black, Germanus of Auxerre, Hilary of Arles, and the README) and part B (Marius Mercator, Eutyches, Prosper of Aquitaine, Eznik of Kolb). Totals: 2 blocking, 40 minor (part A 0 and 30, part B 2 and 10). Each part follows as written.

## R1 review: era 2 batch 6, part A (Church Family Tree Who profiles)

Reviewer: independent, first sight of these drafts. Bar: `Who_Profile_Pattern.md` review checklist 1 to 14 and the standards it points to; `CLAUDE.md` "Trust and source fidelity" and "Accessible and rigorous"; Mark's rulings in the Decision-Log (2026-11-12: majors capped at 2:30, about 405 words; non-majors 1 to 2 minutes, at most about 324 words). I also hunted for the failure types of the earlier R1 reviews, above all the witness swap. I did not edit the drafts. I made no paid or model-API calls and used no web. Readability and quote search ran on local scripts only.

Profiles: `liberius-of-rome`, `marcellus-of-ancyra`, `moses-the-black`, `germanus-of-auxerre`, `hilary-of-arles`, all not major, and the batch `README.md`. Files are in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era2/batch6/`. Brief line numbers refer to the `.brief.txt` files, where each paragraph is one line and blank lines count (paragraphs sit on l.1, 3, 5, 7, 9, 11, 13). Other line numbers point to files under `cic/texts/`.

Method. I searched every quotation in the five briefs and cards in the vendored file the card names. The match stripped XML tags, collapsed whitespace and normalised quote marks. For the OCR files (Feder's Hilary dossier, Migne's PG 42 and PL 50, Levison's Constantius, Mansi VI, Mommsen, Fotheringham's Jerome) I read the passage by line number and searched tolerantly. I read each hit in context to see who is speaking: the ancient author, a document he quotes, a translator's introduction, a footnote (`<note>` in the npnf XML), or a bracket the translator supplied. I checked every factual sentence of each brief against its passage, and compared each `records.json` entry with its brief and card. Readability came from `engine.m1.gates.grade_text`, run from the repo root. Length assumes 162 words a minute.

## Applies to all five

- **Audio = brief.** Each audio script matches its brief exactly once `[calmly] ` and `[warmly] ` are removed (checked by script). Each starts with `[calmly]` and has one `[warmly]`, placed before the final sentence or quoted line. No tag appears in any brief or card.
- **Readability.** All five pass (FK at most 10, Flesch at least 60). Marcellus sits nearest the floor (Flesch 62.3). One narrator sentence runs past 25 words (Liberius l.9, 30 words; see Liberius M6).
- **Card order.** All five follow Mark's order. Missing fields are left out: Moses and Germanus have no keyWorks and no "Their own words". keyWorks never goes past three. Each `uncertain` list opens with the brief's main caveat. The `"date": null` in source entries is the schema the earlier batches used.
- **Who test (item 14).** Liberius has his own letters and a following in the Roman see. Marcellus has his own letter and a following (the Marcellians, Photinus). Moses is known through Palladius's Life, his sayings and seventy disciples. Germanus is known through Constantius's Life and Bede. Hilary has a held body of work (the sermon on Honoratus). The drafts carry no list lines; those belong to the map build and were not checked here.
- **Sources lists.** The batch 5 cards list every held work their sentences rest on. Each card here leaves out works its own brief or `uncertain` list rests on. This is a finding on each profile (Liberius M7, Marcellus M6, Moses M5, Germanus M3, Hilary M6).

| Profile | Words | Est. length @162 | FK | Flesch |
|---|---|---|---|---|
| Liberius of Rome | 344 | 2:07 | 7.5 | 63.8 |
| Marcellus of Ancyra | 338 | 2:05 | 7.6 | 62.3 |
| Moses the Black | 335 | 2:04 | 5.3 | 78.0 |
| Germanus of Auxerre | 335 | 2:04 | 7.6 | 65.4 |
| Hilary of Arles | 339 | 2:06 | 7.5 | 67.3 |

**Batch finding**
- **G1 MINOR (item 10; length).** All five are non-major, and Mark's ruling caps non-majors at 1 to 2 minutes, about 324 words. Earlier non-majors ran 317 to 329 words. These run 335 to 344 (2:04 to 2:07), and every `briefLength` says "about 2 minutes". Fix: trim each to about 324 words. Each profile below suggests cuts that also carry its other fixes. The cuts remove facts the card already holds, which the pattern says the brief does not repeat.

---

## 1. Liberius of Rome

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | FAIL, minor (M1, M2, M3, M4) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | FAIL, minor (M6) |
| 5 | No role for a witness | PASS (Theodoret, Ammianus, Athanasius, Jerome, Sozomen, Feder, Hartranft, Ambrose, Loomis, Jackson named) |
| 6 | Partisan witness named and marked | PASS (Athanasius "his ally"; Hilary's "angry notes" on the card; Ammianus outside the church) |
| 7 | Contested both sides | PASS (the lapse: Athanasius, Jerome, Sozomen, Theodoret, Feder; Felix's installer and the recall on the card) |
| 8 | Common names placed | brief minor (M5); card minor (M5) |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | FAIL, minor (G1; 2:07) |
| 11 | grade_text | PASS |
| 12 | Card order, caveat repeated | PASS on order and caveat; sources minor (M7) |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |

**Quotes** (all exact; speaker confirmed)
- "My standing alone does not make the truth a whit the weaker." (l.1): the record in Theodoret II.13, Liberius speaking (npnf203 l.9749). Theodoret says the talk is "recorded by some of the pious men of that period" (l.9655–9659), and the brief says so.
- "Neither three days nor three months can change my sentiments. Send me wherever you please." (l.1): l.9829–9830.
- "to pay his troops" (l.1): "he has need of them to pay his troops" (l.9838), said of the emperor's gold.
- "among whom he was exceedingly popular" (l.3, card): Ammianus XV.7 (`ammianus-marcellinus_roman-history_yonge1862.txt` l.4215–4216). "Removed by night… through the fear which his enemies had of the people" is the same passage.
- "gave way, and from fear of threatened death subscribed" (l.5) and the card's "the hatred of Liberius against the heresy": Athanasius, History of the Arians 41 (npnf204 l.39176–39177).
- "One God, one Christ, one bishop." (l.7): Theodoret II.14 (npnf203 l.9905–9908).
- "You," … "my daughter, have desired a good espousal." (l.11): Ambrose, On Virgins III.1 (npnf210 l.38143).
- Card: "This victorious champion of the truth" (Theodoret II.14, npnf203 l.9860). Exact.

**Narrative checks**
- Jerome's Chronicle: "Liberius taedio uictus exilii et in haeretica prauitate subscribens Romam quasi uictor intrauerat" (`jerome_eusebii-chronici-canones-lat_fotheringham1923.txt` l.45536–45540). Faithful. Jerome's Lives 97 on Fortunatianus and 98 on Acacius (npnf203 l.41295–41312). Faithful.
- Sozomen IV.15: Liberius and others "were induced to assent to this document", and a confession "drawn up by Liberius" was partially approved (npnf202 l.33560–33584). See M3.
- Feder lists "epistulae dubiae Pro deifico, Quia scio, Non doceo" (Feder l.15187; "ex parte genuinae, ex parte dubiae", l.2796). "Pro deifico" has "ego Athanasium non defendi" and Hilary's brackets "anathema tibi a me dictum, Liberi" (l.14072–14110). The card's "did not defend" and "angry notes" are exact.
- Death: "octauo Kalendas Octobr. Gratiano et Dagalaifo consulibus Liberius humanis rebus eximitur" (`collectio-avellana_…-v1-lat_guenther1895.txt` l.5098–5099). Hartranft's "a.d. 366, Sept. 24" is his note to Sozomen VI.23 (npnf202 l.38766). The same Avellana account says Liberius "manus perfidiae dederat" (l.5087), a further lapse witness the brief does not use; nothing told is wrong.
- Loomis: "a strange medley of facts and legend", and Liberius "ordained in his stead Felix" in the Book of the Popes (`liber-pontificalis_book-of-the-popes-v1_loomis1916.txt` l.5915–5931). Socrates's "the adherents of Ursacius appointing Felix" (npnf202 l.8934). Jackson's Milan note (npnf203 l.9666–9667). All faithful.
- records.json matches brief and card apart from M2, and carries both `contested_claim` records.

**Findings**
- **M1 MINOR (items 1, 5; a fact placed under the wrong witness).** Brief l.3: "Ammianus Marcellinus… He says Liberius was taken from Rome by night… A deacon, Felix, was put in his place." Ammianus does not mention Felix (Yonge l.4175–4216). The deacon Felix is Theodoret's: "one of his deacons, named Felix, had been appointed bishop" (npnf203 l.9878–9880). As written, a listener gives the line to Ammianus. Fix: "Theodoret says a deacon, Felix, was put in his place."
- **M2 MINOR (items 1, 5; a translator's note given to Ambrose).** Brief l.11 says Liberius was "giving the veil to Ambrose's sister", and the card's `legacy.traces` 2 says she "took the veil". Ambrose says she "signified your profession of virginity by your change of attire". The veil is the translator's footnote at that point: "evidently a public profession with receiving the veil, etc." (npnf210 l.38143). Ambrose was also not present. He passes on "those precepts of Liberius… which you used to talk over with me", so "Ambrose recalls him saying" overstates it. Fix, brief l.11: "Ambrose of Milan passed on the words Liberius spoke at Christmas in Saint Peter's, when Ambrose's sister made her profession as a virgin. "You," he said, "my daughter, have desired a good espousal."" Card `legacy.traces` 2: "Ambrose of Milan passes on, from his sister, the sermon he gave when she made her profession as a virgin." Records: change "Gave the veil to Ambrose's sister" to "Received the profession of Ambrose's sister", with "the veil is the translator's note".
- **M3 MINOR (item 1).** Brief l.5 and card `uncertain` 1: "Sozomen says he signed a creed made at Sirmium". In Sozomen, the document was put together by Basil, Eustathius and Eusebius from the decrees against Paul of Samosata and Photinus, "to which they subjoined a formulary of faith drawn up at Antioch" (npnf202 l.33566–33572). The creed in it was made at Antioch. Fix (brief, card, records): "Sozomen says he signed a document drawn up by Eastern bishops at Sirmium, with his own statement added."
- **M4 MINOR (items 1, 5, card).** Card `legacy.traces` 1: "Theodoret of Cyrrhus copies a record of his talk… to stir others to the same zeal." In Theodoret, that purpose belongs to the recorders: "They are recorded by some of the pious men of that period in order to stimulate others to the exercise of similar zeal" (npnf203 l.9655–9658). Fix: "Theodoret of Cyrrhus copies into his Church History a record of his talk with Constantius, which pious men of the time kept to stir others to the same zeal."
- **M5 MINOR (item 8; "no statements with no context").** Brief l.5: "Sozomen says" is his only mention, with no context, and batch 5 (Eusebius of Nicomedia M1) asked for one. Card: in `uncertain` 1, "blames Fortunatianus" is bare. In `uncertain` 3, "Who put Felix in his place" is the card's first Felix, and "Jerome says Acacius" names a common name bare. Jerome gives both sees: "Fortunatianus… bishop of Aquilia" and "Acacius… bishop of the church of Cæsarea in Palestine" (npnf203 l.41296, 41305–41312). Fixes: brief "Sozomen, a church historian of the next century, says…"; card "blames Fortunatianus, bishop of Aquileia"; "Who put the deacon Felix in his place…; Jerome says Acacius of Caesarea…".
- **M6 MINOR (item 4; length of sentence; G1).** Brief l.9 is one 30-word narrator sentence, and its two facts (24 September; Hartranft's 366) are already on the card's `dates`. Hartranft also revised the translation of Sozomen and did not make it (npnf202 l.21640–21650, "Revised by Chester D. Hartranft"). Fix: delete l.9. That removes 39 words, and with M1, M2 and M5 the brief comes to about 315 words.
- **M7 MINOR (item 12; sources).** The card's `sources.about` leaves out works the brief rests on: Ammianus Marcellinus (Yonge, `ammianus-marcellinus_roman-history_yonge1862.txt`), Jerome's Chronicle (`jerome_eusebii-chronici-canones-lat_fotheringham1923.txt`), Jerome's Lives 97–98 (npnf203; the entry lists only Theodoret), Ambrose On Virgins III (`npnf210_ambrose-select-works-letters.xml`), the account of Liberius and Felix in the Collectio Avellana (`collectio-avellana_epistulae-imperatorum-pontificum-v1-lat_guenther1895.txt`) and Loomis's Book of the Popes (`liber-pontificalis_book-of-the-popes-v1_loomis1916.txt`). Fix: add the six entries, and retitle the npnf203 entry "Church History II.13–14 (tr. Blomfield Jackson); Lives of Illustrious Men 97–98 (Jerome)".

---

## 2. Marcellus of Ancyra

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | FAIL, minor (M1, M5) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | card minor (M4) |
| 5 | No role for a witness | PASS (Epiphanius, Socrates, Sozomen, Zenos, Watson, Hefele, Percival, Robertson named) |
| 6 | Partisan witness named and marked | PASS (charges given as "opponents' charges"; Epiphanius's heresy frame on the card) |
| 7 | Contested both sides | FAIL, minor (M2) |
| 8 | Common names placed | FAIL, minor (M3) |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | FAIL, minor (G1; 2:05) |
| 11 | grade_text | PASS |
| 12 | Card order, caveat repeated | PASS on order and caveat; sources minor (M6) |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |

**Quotes and close tellings**
- The letter to Julius (l.1), Epiphanius, Panarion 72 (`epiphanius_panarion-haer-65-80-pg42-grc-lat_migne1863.txt`): "ἐνιαυτὸν καὶ τρεῖς ὅλους μῆνας" in Rome (l.28794–28800); "τῇ ἐμαυτοῦ χειρὶ γράψας" (l.28825); "ὁ ἀεὶ συνυπάρχων τῷ Πατρί" (l.28869–28870); "οὗ τῆς βασιλείας… οὐκ ἔσται τέλος" (l.28890–28897). Faithful, apart from M1.
- "the most execrable of all heretics" (l.5, card): the Oriental bishops' synodical letter from Sardica, quoted in Zenos's note to Socrates II.19 (npnf202 l.6707–6713). The brief names both.
- "notorious that he never did so" (l.7, card): Watson's introduction to the English Hilary (npnf209 l.4343–4344).
- Card: the Sardican letter's "he had written that His kingdom was both without beginning and without end" (npnf204 l.24192–24193). Exact.

**Narrative checks**
- Asterius, who "commended the dogmas of Arius", and Marcellus "fell into the diametrically opposite error… as the Samosatene had done, that Christ was a mere man" (Socrates I.36, npnf202 l.5379–5422). Sozomen II.33: the Son's existence "commenced when He was born of Mary", "His kingdom would have an end", Basil installed, and "Some persons, however, maintained that Marcellus had merely propounded a few questions" (l.30604–30626). Faithful.
- Sardica: "what Marcellus had advanced by way of enquiry they falsely represented as his professed opinion" (npnf204 l.24186–24188). Faithful.
- Epiphanius on Athanasius: "οὔτε ὑπεραπελογήσατο… μόνον δὲ διὰ τοῦ προσώπου μειδιάσας ὑπέφηνε, μοχθηρίας μὴ μακρὰν αὐτὸν εἶναι, καὶ ὡς ἀπολογησάμενον εἶχε" (l.29100–29108). Faithful.
- Hilary's dossier: "negata sibi ab Athanasio communione" (Feder l.12871). Watson's note in full says Fragments ii and iii "are not by Hilary" and the excommunication is "a mistake… which Hilary could not possibly have made" (npnf209 l.4331–4345). The brief's "the dossier of Hilary of Poitiers" is a fair name for the collection. Robertson: "a personal estrangement… did not amount to a formal breach of communion" (npnf204 l.4292–4294).
- Death: "ὡς ἀπὸ δύο ἐτῶν ἐτελεύτα, ἢ πλείω ἢ ἐλάσσω" (PG42 l.28607–28608). "τὰ μὲν κρύφια τῆς ἐννοίας Θεῷ ἔγνωσται" (l.28684). Canon 1 of 381 (npnf214 l.13975); Hefele "and indeed he himself, once more acknowledged the truth" (l.14004–14007), under the heading "Hefele." Faithful.
- Photinus "a disciple of that Marcellus who had been deposed" (Socrates II.18, npnf202 l.6569–6571). Faithful.

**Findings**
- **M1 MINOR (items 1, 5; an editor's words given to the subject).** Brief l.1: "At the Council of Nicaea, he reminds Julius, he had refuted the Arians." The letter does not say "Arians". It says that some "of those condemned before for not believing rightly, whom I refuted at the synod in Nicaea, dared to write against me" (PG42 l.28776–28779). "Played the man at Nicæa, and was accused by the Arians" is Blomfield Jackson's note to Theodoret (npnf203 l.8631–8632). The card's `knownFor` "opposed the Arians at Nicaea" and the records claim carry the same reading. Fix, brief: "At the Council of Nicaea, he reminds Julius, he had refuted the men now writing against him." Card `knownFor`: "Bishop of Ancyra in Galatia who, by his own letter, refuted at Nicaea the men who later accused him, was deposed…". Records: "said he had refuted at Nicaea those now writing against him".
- **M2 MINOR (item 7; one side of two disputes missing).** (a) Brief l.9 gives only Hefele's view that Marcellus "came back to the truth". The other side, the Benedictine note to Basil, "Videtur ergo Marcellus sub finem vitæ aliquid peccasse" (npnf208 l.43542), is on the card and in the record but not in the brief. (b) That same note says the Benedictines think Athanasius "extremis vitæ suæ annis Marcellum a communione sua removerit" (l.43533–43534). That is a held editor's side on whether Athanasius broke with him. The card's `uncertain` 3 and the records' `contested_claim` leave it out. Fixes: brief l.9, "Hefele, quoted in Henry Percival's edition, says Marcellus himself came back to the truth. A Benedictine note to Basil's letters thinks he erred at the end of his life." Card `uncertain` 3, add: "The Benedictine note in the edition of Basil's letters holds that Athanasius removed him from communion in his last years." Records, add that side (npnf208 l.43532–43542).
- **M3 MINOR (item 8).** Brief l.3: "put Basil in his place". Basil is a common name, and the card's `uncertain` 2 names Basil of Caesarea, who later condemned Marcellus, so the listener may take this Basil for that one. Theodoret gives the see: "Basilius had succeeded Marcellus, and held the helm of the church of Ancyra" (npnf203 l.10601–10602). Fix: "…deposed him and put Basil in his place at Ancyra."
- **M4 MINOR (items 4, 12; status-announcement register on a participant card).** Card `uncertain` 6: "The card's tradition is the scan's, from the Library shelf where Epiphanius is held; it is not his party." This is build-process narration ("the scan", "the Library shelf") on a participant-facing card. The README already records that the tradition is to be settled with the placing. Fix: delete the item. Until the placing, leave the note in the README and Open-Gaps.
- **M5 MINOR (item 1, card).** Card `dates`: "372 or 374 by E. C. Richardson's". Richardson's note reads "Died 372, or 374 (Ffoulkes.)" (npnf203 l.41145–41146), so he gives the dates on Ffoulkes's authority. Fix: "…or 372 or 374 by E. C. Richardson's note, after Ffoulkes…".
- **M6 MINOR (item 12; sources).** `sources.about` leaves out works the card and brief rest on: Theodoret, with Jackson's and Richardson's notes (npnf203); Watson's introduction (`npnf209_hilary-poitiers-john-damascus.xml`); Hilary's dossier (Feder, CSEL 65); Percival's council records with Hefele (`npnf214_seven-ecumenical-councils.xml`); Basil's letters with the Benedictine note (npnf208). Fix: add the five entries.
- Length (G1): with M2(a) and M3 the brief grows by about 12 words. Suggested cuts: delete l.9's "Epiphanius writes that Marcellus had died about two years before, more or less." (the card's `dates` holds it); shorten "in his introduction to the English Hilary" to "Hilary's English editor"; shorten "in Henry Percival's edition of the council records" to "in Henry Percival's edition". The result is about 325 words.

---

## 3. Moses the Black

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | FAIL, minor (M1, M3, M4) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS |
| 5 | No role for a witness | PASS (Palladius, Sozomen, Isidore, Budge, Clarke, Butler, Gibson named) |
| 6 | Partisan witness named and marked | FAIL, minor (M2: hagiography not marked in the brief) |
| 7 | Contested both sides | PASS (Ethiopian or Egyptian; the death; which Moses) |
| 8 | Common names placed | PASS (Palladius of Helenopolis; Isidore, the priest of Scete) |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | FAIL, minor (G1; 2:04) |
| 11 | grade_text | PASS |
| 12 | Card order, caveat repeated | PASS on order and caveat; sources minor (M5) |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |

**Quotes** (all exact; speaker confirmed)
- "Since I am not allowed to hurt anyone… what do you bid me do with these?" (l.1): Palladius, Lausiac History 19 (`palladius_lausiac-history_clarke1918.txt` l.335), Moses speaking.
- "an Ethiopian by race and black" (l.3, card): l.333.
- "I will never cease until the appearance of the demons ceases" (l.5): l.337, Moses to Isidore.
- "an Egyptian" (l.5, card): Sozomen VI.29, "Moses, an Egyptian" (npnf202 l.39461).
- "Get outside, O Ethiopian" and "They have treated thee rightly, O thou whose skin is dark and black" (l.9): Budge's Paradise II, saying 477 (`anan-isho_paradise-v2-sayings_budge1907.txt` l.1028), the clergy and then Moses to himself.
- Card: "This was the manner of life of Moses the Ethiopian" (Palladius l.337); Sozomen's "he died at the age of seventy-five, leaving behind him numerous eminent disciples." (npnf202 l.39525); "they used to say" (Palladius l.333). Exact.

**Narrative checks**
- House-servant to an official, driven out for "immorality and brigandage"; "said to go even the length of murder"; "they used to say that he was leader of a robber-band"; "conscience-stricken as a result of one of his adventures, gave himself up to a monastery"; six years standing all night; "the great Isidore, the priest of Scete"; died at Scete at seventy-five, a priest, with seventy disciples (Palladius l.333–337). Faithful.
- Clarke's note 143: "Butler, II. 197, distinguishes between the various monks of this name. Moses the Robber is the Moses whose sayings are recorded in the Apophthegmata," (l.919). The held note stops there, mid-sentence. The brief's "Clarke takes the robber for the Moses of the sayings" is the natural reading.
- Cassian's Abbot Moses recalls "while I was still a boy, in the region of Thebaid, where the blessed Antony lived" (npnf211 l.27196–27199); Gibson: "probably the one to whom the first two Conferences are attributed… and possibly the second of this name (Moses the Libyan)" (l.24272–24276). The card is faithful; the record is not (M4).
- Clarke dates Palladius's book "419-420" (note 13, l.657). The card is faithful.

**Findings**
- **M1 MINOR (item 1).** Brief l.7: "where Moses stayed and was killed with seven brothers". The card's `uncertain` 4 and the records claim say the same. The saying reads: "Now the brethren were seven in number… the barbarians entered and slew them. Now one of them had been afraid, and he fled behind the palm leaves, and he saw seven crowns come down and place themselves on the heads of those who had been slain" (Budge l.1464). One of the seven fled, and seven crowns fell, so the saying does not have seven brothers killed beside Moses. Fix (brief): "One tells of barbarians coming to Scete, where Moses stayed and was killed with the brothers who stayed with him." Card and records: "…killed Abba Moses and the brothers who stayed with him."
- **M2 MINOR (items 6, 12; hagiography not marked in the brief).** The README says Moses and Germanus "are known through Lives and sayings, which the briefs mark as such". Germanus's brief does this ("It is a saint's Life, full of wonders"). Moses's brief tells demon attacks as narrated fact (l.5) and never says the Lausiac History is a book of holy lives. Only the card says so (`uncertain` 1). Fix, l.1: "Palladius of Helenopolis, in his book of holy lives, tells what followed."
- **M3 MINOR (item 1; a loose quantifier and a misstatement).** Brief l.9: "One saying does name the Ethiopian. When Moses was a priest, …". Several held sayings mark him out, which bears on the identification told in l.7: "Abbâ Moses, the Black" (saying 18, Budge l.88), "Abbâ Moses who was a thief" (l.96) and "Why doth this Ethiopian come and go in our midst?" (saying 55, l.164). Saying 477 also says "when Abbâ Moses was one of the clergy", not a priest (l.1028). Fix: "Some sayings do mark him out. One calls him Abba Moses the Black. In another, when Moses was one of the clergy, his bishop had the clergy drive him out, to test him." Then go on as now.
- **M4 MINOR (items 1, 3; card and records).** (a) Card `uncertain` 2: "Sozomen tells much the same story in much the same order, so he is not a separate witness." No held source says Sozomen drew on Palladius. The drafter infers it, and the card tells it as fact. Fix: "Sozomen tells much the same story in much the same order, so he likely depends on Palladius and is no separate witness." (b) Card `uncertain` 1: "His robbery and the murders he was said to have done come to Palladius… as report". Palladius states the brigandage as fact ("drove him out because of his immorality and brigandage"). The murder and the leading of a band are what "was said" and what "they used to say" (l.333). Fix: "The murders he was said to have done, and his leading a robber band, come to Palladius as report ('they used to say')." (c) The records `contested_claim` "Whether Cassian's Abbot Moses is the same man" gives Gibson "probably another, possibly Moses the Libyan". Gibson's "probably" is about the Conferences: "probably the one to whom the first two Conferences are attributed… and possibly… Moses the Libyan" (npnf211 l.24272–24275). Fix: "Gibson: probably the Moses of the first two Conferences, and possibly Moses the Libyan."
- **M5 MINOR (item 12; sources).** `uncertain` 3 rests on Cassian and Gibson (`npnf211_sulpitius-severus-vincent-cassian.xml`), which `sources.about` does not list. Fix: add "Institutes and Conferences (tr. Edgar Gibson)", author John Cassian, with that file.
- Length (G1): M2 and M3 add about 9 words. Suggested cuts: l.7's "Palladius says only that he died at Scete." (the card holds it), and l.5's "Sozomen, a church historian, tells much the same story but calls him" can become "Sozomen, a church historian, calls him" (the card holds "much the same story"). The result is about 323 words.

---

## 4. Germanus of Auxerre

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | PASS |
| 2 | Quotes verbatim | PASS (no direct quotations; close tellings checked) |
| 3 | No invention | PASS |
| 4 | Reading aids | FAIL, minor (M2) |
| 5 | No role for a witness | PASS (Constantius, Levison, Prosper, Mommsen, Bede, Giles named) |
| 6 | Partisan witness named and marked | PASS (the Life marked "a saint's Life, full of wonders", l.3) |
| 7 | Contested both sides | PASS (who sent him: Prosper v. Constantius, with Levison) |
| 8 | Common names placed | FAIL, minor (M1) |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | FAIL, minor (G1; 2:04) |
| 11 | grade_text | PASS |
| 12 | Card order, caveat repeated | PASS on order and caveat; sources minor (M3) |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |

**Close tellings** (`constantius-lyon_vita-germani_levison1920.txt` unless marked)
- The Alleluia battle (l.1): "Saxones Pictique bellum adversus Brittanos iunctis viribus susceperunt"; Lent and baptisms, Easter; "Germanus ducem se proelii profitetur… vallem circumdatam editis montibus"; "Alleluia tertio repetitum sacerdotes exclamant. Sequitur una vox omnium… Hostile agmen terrore prosternitur" (l.2992–3073). Faithful.
- Levison: "Vitam c. 480. aut paulo post compositam esse" (l.431). His note: "De incursione Saxonum Pictorumque a. 429. facta aliunde nihil traditum est", apart from the "fabulosa" Historia Brittonum count, which he says lacks authority (l.3026–3031). The brief's "Levison knows no other record of that raid" is fair.
- Birth, Rome, the prefect's courts, the rule of provinces (l.2040–2051); "Germanum episcopum omnium una vox postulat… Suscepit sacerdotium invitus" (l.2120–2124). Faithful.
- Prosper: "Agricola Pelagianus… sed ad insinuationem Palladii diaconi papa Caelestinus Germanum Autisidorensem episcopum vice sua mittit", under Mommsen's "a. 429" (`prosper_chronica-minora-1-lat_mommsen1892.txt` l.54147–54155). Constantius's embassy and "synodus numerosa" choosing Germanus and Lupus (l.2664–2669). Levison: "Constantius, qui Caelestini mentionem non fecit… Prospero tacente, hae merae coniecturae sunt" (l.189–194). Faithful.
- Second journey "Adiuncto itaque Severo episcopo" (l.3474–3480). Bede copied c. 12–18 and 25–27 "magna ex parte ad verbum fere" (l.587–589). Bede: Severus "afterwards, as bishop of Treves" (`bede_…giles1903.txt` l.1693–1695); the bracketed headings "[a.d. 429.]" and "[a.d. 447.]" (l.1375, 1684). Faithful.
- Ravenna, Placidia "cum filio Valentiniano", "quod illa invita concessit, ut gleba corporis sui patriae redderetur", "Septimo incommodi die" (l.4018–4022, 4407–4413). Faithful.
- Chronica Gallica of 452: "Germanus episcopus Altisiodori virtutibus et vitae districtione clarescit" (Mommsen l.71158–71159). Faithful.
- Card `dates`: Levison's "post a. 444… die 31. Iulii" and "anni 418–448… etsi non ita certa sunt" (l.74–83). The wife's name: "Eustachiam nomine addunt Gesta pontif. Autissiod." (l.2097–2098). Faithful.

**Findings**
- **M1 MINOR (item 8).** Brief l.7: "a large synod chose Germanus and Lupus". Lupus is a common name, and the brief gives him no see. Levison gives it: "cum Lupo episcopo (Trecensi)" (l.190). Fix: "…chose Germanus and Lupus of Troyes."
- **M2 MINOR (item 4; an unclear reference).** Brief l.7: "Pope Celestine, urged by the deacon Palladius, sent Germanus in his place." The sentence before is about Agricola, so "his place" can be heard as Agricola's or Palladius's. Prosper's "vice sua" means as Celestine's own deputy. Fix: "…sent Germanus to act for him."
- **M3 MINOR (item 12; sources).** `remembered` 1 and the brief's close rest on the Chronica Gallica of 452. It is held in the same Mommsen file, but it is a different work, and `sources.about` lists only Prosper's Epitoma. Fix: add "Chronica Gallica of 452 (ed. Theodor Mommsen)", no author, Latin, with the same file.
- Length (G1): M1 and M2 add about 3 words. Suggested cuts: l.11's "He died on the seventh day of his illness." and "with her son Valentinian". The result is about 325 words.

---

## 5. Hilary of Arles

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | FAIL, minor (M1, M2, M3) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | FAIL, minor (M5) |
| 5 | No role for a witness | PASS (the Life, Mansi's editors, Leo, Feltoe, Gennadius, Constantius, Richardson, Jackson named) |
| 6 | Partisan witness named and marked | PASS (the Life "takes Hilary's side"; "Leo was a party to the quarrel") |
| 7 | Contested both sides | PASS (the quarrel; Celidonius's deposition; birth year on the card) |
| 8 | Common names placed | FAIL, minor (M4) |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | FAIL, minor (G1; 2:06) |
| 11 | grade_text | PASS |
| 12 | Card order, caveat repeated | PASS on order and caveat; sources minor (M6) |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |

**Quotes and close tellings**
- The Life of Hilary in Mansi VI (`mansi_sacrorum-conciliorum-collectio-tomus-6-441-451-lat_welter-facsimile1901.txt`): "Ille urbem credidit expetendam, ibique se injusto rigore adstruit condemnatum. Quod ubi comperit vir beatus, pedibus iter aggrediens, Romam sine equo, sine sagmario festinus intravit… se ad officia non ad causam venisse" (l.44880–44898). "accusatio testimoniis confirmatur" (l.44884). Faithful.
- "such as no layman could make and no priest listen to" (l.5): Leo, Letter 10 (npnf212 l.2161). Celidonius "had proved himself wrongfully deposed" (l.2163–2166). The courier: "the swiftness of a courier rather than… the sobriety of a priest" (l.2262–2263). "A band of soldiers, as we have learnt, follows the priest" (l.2297–2298). Loss of "his power over the province of Vienne" (l.2349–2351). Faithful.
- "not very creditable encounter with Hilary" (l.5, card): Feltoe's introduction (npnf212 l.496).
- "Hilary of holy memory" (l.9, card): Letter 40 (npnf212 l.6513–6516; a translator's note stands between "Hilary" and "of holy memory" and was stripped). "Dated 22 August in the consulship of Asturius and Protogenes (449)" (l.6528). The card rightly gives the year to Feltoe from the consuls.
- Gennadius 70: "this man of noble race and very differently brought up, engaged in farming, though it was beyond his strength"; "that work which is of so great practical value to many, his Life of Saint Honoratus"; "He died during the reign of Valentinianus and Martianus" (npnf203 l.43386–43402). Richardson's note "Born about 401, bishop 429, died 449" (l.43387). Jackson's "before his death at the age of 41 in 449" (l.3089–3090). Faithful.
- The sermon (`hilary-arles_sermo-de-vita-sancti-honorati_migne-pl50.txt`): "patriam quam fastidierat non dedignatur accedere" for his sake (l.1046–1047); "obluctanti mihi" (l.1084); "Gratias tibi, Jesu bone… qui dirupisti vincula mea, famuli tui Honorati pia supplicatione permotus" (l.1202–1204); "quaerens in me fidei, sicut sanguinis sui venam" (l.1811–1812), with the editors' chapter head "Hilarius successor Honorati, ejus consanguineus" (l.1778). Faithful.

**Findings**
- **M1 MINOR (items 1, 7; a held editor's note contradicts the card).** Card `keyWorks` 1: "his funeral sermon for Honoratus of Arles". The note in the held Migne edition cites the Vatican manuscripts: "editus a S. Hilario Arelatensi episcopo depositionis ejus in die", and adds that "sermonem habuit Hilarius elapso anno ab Honorati morte" (D. Joannes Salinas, l.115–128). On that note, he gave it on Honoratus's feast day, a year after his death, and it was not a funeral sermon. (The word "funeral" comes from the file's vendoring header, which is not a source.) Fix: "his sermon on the life of Honoratus of Arles, founder of the community on Lérins; held in Latin".
- **M2 MINOR (item 1; a doubt overstated).** Brief l.3: "The editors of that collection doubt that Honoratus of Marseilles, its usual author, wrote it." The card's `uncertain` 1 and the record say the same. Mansi's editors write "innuit Honoratus Massiliensis, seu quis alius vitae Hilarii ejusdem est auctor" (l.44820–44822). That is "Honoratus of Marseilles, or whoever else is the author", which leaves the question open and does not doubt him. Fix (brief): "The editors of that collection give it to Honoratus of Marseilles, or to whoever else wrote it." Card: "…whose editors leave its author open: Honoratus of Marseilles, or another."
- **M3 MINOR (item 1; a translation merged).** Brief l.9 and card `remembered` 1: "a fiery torrent of faith and heavenly speech". Constantius has "erat enim fide igneus, torrens caelestis eloquii" (Levison l.3377): fiery in faith, a torrent of heavenly eloquence. Fix (card): "calls him fiery in faith and a torrent of heavenly speech". For the brief, see the length note.
- **M4 MINOR (item 8).** Brief l.7: "Hilary preached a sermon on Honoratus". The brief has just named Honoratus of Marseilles (l.3), so a listener may take this bare Honoratus for him. Fix: "Hilary preached a sermon on Honoratus of Arles, who had led him…".
- **M5 MINOR (item 4; statements with no context; a bare limit line).** Brief l.7 opens "Gennadius of Marseilles says Hilary was of noble birth and brought up very differently." Differently from what is not said until l.9, where the farming comes. Brief l.9 ends "No ancient source gives his birth." This is unqualified: the card says "No ancient source used here". It is also a date fact the card's `dates` already holds. Fix: delete the l.7 sentence and write l.9 "As bishop, Gennadius says, he chose poverty and farmed beyond his strength, though he was of noble birth and had been brought up very differently." Delete "No ancient source gives his birth."
- **M6 MINOR (item 12; sources).** `remembered` 1 and the brief rest on Constantius of Lyon's Life of Germanus (`constantius-lyon_vita-germani_levison1920.txt`), and the records cite Heurtley (npnf211). Neither is in `sources.about`. Fix: add "Life of Germanus 23 (ed. Wilhelm Levison)", author Constantius of Lyon, Latin, and "Introduction to Vincent of Lérins (tr. C. A. Heurtley)", npnf211.
- Length (G1): M4 and M5 come to about −7 words. Also delete l.9's "Constantius of Lyon calls him a fiery torrent of faith and heavenly speech." The card's `remembered` 1 holds it, and in the brief Constantius has no context. The result is about 321 words.

---

## README

- **README-M1 MINOR.** "after the three in era 2 batch 5, in the scan's order: Liberius of Rome, Marcellus of Ancyra, Moses the Black, Germanus of Auxerre, Hilary of Arles, Marius Mercator, Eutyches, Prosper of Aquitaine and Eznik of Kolb". The supplement scan's table runs Eutyches, Moses the Black, Eusebius of Nicomedia, Liberius, Marcellus, Marius Mercator, Eznik, Prosper, Hilary of Arles, Germanus (`Build/Ministry/Operations/Audits/2026-11-12_who-scan-supplement/Who_Scan_Supplement.md` l.106–115). Open-Gaps 236 lists the same order. The batch's order is not the scan's. Fix: "in the batch's own order", or reorder the list to the scan's.
- **README-M2 MINOR.** "Moses the Black and Germanus of Auxerre are known through Lives and sayings, which the briefs mark as such." This holds for Germanus and not yet for Moses (Moses M2). Fix: make Moses M2's change. The README then stands.
- The README's note that four card traditions are the scan's agrees with the cards. Marcellus's card should not repeat it (Marcellus M4).

## Totals

Blocking: 0. Minor: 30, made up of 1 batch finding (G1, length, touching all five), 27 profile findings (Liberius 7, Marcellus 6, Moses 5, Germanus 3, Hilary 6; Moses M4 has three parts), and 2 README findings. No quote is misquoted. The recurring faults found are three witness swaps (Liberius M1, M2, M4), an editor's phrase put in the subject's letter (Marcellus M1), one note's dating given without its source (Marcellus M5), a held editor's side left out (Marcellus M2), loose quantifiers (Moses M3; Hilary M5), common names without a place (Liberius M5, Marcellus M3, Germanus M1, Hilary M4), and sources lists that drop works the text rests on (all five).

---

## R1 review: era 2 batch 6, part B (Church Family Tree Who profiles)

Reviewer: independent, first sight of these drafts. Bar: `Who_Profile_Pattern.md` review checklist 1 to 14 and the standards it points to; `CLAUDE.md` "Trust and source fidelity" and "Accessible and rigorous"; and the recurring faults of the earlier era 2 R1 reviews (witness swaps, fixes that bring in new wrong attributions, editors' dates told as ancient, identifications told as settled, "no source gives X" when a held editor does). I did not edit the drafts. I made no paid or model-API calls and used no web. Readability, length, the audio check and the quote search ran on local scripts only.

Profiles: `marius-mercator`, `eutyches` (MAJOR), `prosper-of-aquitaine`, `eznik-of-kolb`. Files are in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era2/batch6/`. Brief line numbers refer to the `.brief.txt` files, where each paragraph is one line and blank lines count. Other line numbers point to files under `cic/texts/`. The other five profiles and the batch README are outside part B, except where the README bears on a card here.

Method. I searched every quotation in the four briefs and cards in the vendored file the card names. The match stripped XML tags and `<note>` blocks, collapsed whitespace and normalised quote marks. For the Migne OCR (PL48, PL33, PL68), Mommsen's Prosper and the Langlois OCR I searched by hand and read each passage in the Latin or French. I read each hit in context to see who is speaking: the ancient author, a document he quotes, the translator, a footnote, or an unsigned introduction. I checked every factual sentence of each brief against its passage, and compared each `records.json` entry with its brief and card. Readability came from `engine.m1.gates.grade_text`, run from the repo root. Length assumes 162 words a minute.

## Applies to all four

- **Audio = brief.** Each audio script matches its brief exactly once `[calmly] ` and `[warmly] ` are removed (checked by script). Each starts with `[calmly]` and has one `[warmly]`, placed before the final sentence. No tag appears in any brief or card.
- **Readability.** All four pass (FK at most 10, Flesch at least 60). Marius Mercator sits right on the floor (Flesch 60.9). The sentences past 25 words are each carried by quoted source (Eutyches l.1, l.3, l.5, l.7, l.9, l.11; Prosper l.3), so none is a finding.
- **Length.** Eutyches is 391 words (2:25), under the major cap of about 405. The three non-major profiles run 2:04 to 2:06, which is "about 2 minutes". Every `briefLength` matches.
- **Card order.** All four follow Mark's order, missing fields are left out, keyWorks never passes three, and each `uncertain` list opens with the brief's own caveat. The `"date": null` in source entries is the schema the earlier batches used.
- **Who test (item 14).** Mercator is a Who as a recorder and translator (README). Eutyches, Prosper and Eznik each have a body of work or a following. The drafts carry no list lines; those belong to the map build and were not checked here.
- **Card traditions.** The README says Mercator's "Pelagianism", Prosper's "Gallic Monastic-Ascetic Christianity" and Eutyches's "The Church of Alexandria and Miaphysite Egypt" are the scans' and are to be settled with the placing. A participant reading "Pelagianism" on the card of a man who wrote against the Pelagians will be misled, so that placing should not ship as it stands. It is already logged as open, so it is not counted as a finding here.

| Profile | Words | Est. length @162 | FK | Flesch |
|---|---|---|---|---|
| Marius Mercator | 334 | 2:04 | 7.7 | 60.9 |
| Eutyches (MAJOR) | 391 | 2:25 | 7.9 | 61.0 |
| Prosper of Aquitaine | 334 | 2:04 | 8.3 | 62.3 |
| Eznik of Kolb | 341 | 2:06 | 7.0 | 69.3 |

---

## 1. Marius Mercator

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | PASS |
| 2 | Quotes verbatim | PASS (see note on "my son") |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS |
| 5 | No role for a witness | PASS (Garnier, Baluze, Schoenemann, Hefele, Warfield named) |
| 6 | Partisan witness named and marked | PASS (l.9; card `uncertain` 5) |
| 7 | Contested both sides | PASS (origin; lay status; Chalcedon) |
| 8 | Common names placed | PASS in the brief; card minor (M2) |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | PASS (2:04) |
| 11 | grade_text | PASS (on the floor) |
| 12 | Card order, caveat repeated | PASS |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS (recorder and translator) |

**Quotes and close tellings** (`marius-mercator_opera-omnia-lat_migne-pl48.txt` unless marked)
- The Commonitorium's title (l.1): "Exemplum Commonitorii quod super nomine Caelestii Graeco sermone a Mercatore datum est, non solum Ecclesiae Constantinopolitanae… oblatum quoque piissimo principi Theodosio… consulatu Florentii et Dionysii… imperiali praecepto… Julianus defensor et sequax ejus, cum caeteris sociis… quam ipse Caelestius de Constantinopolitana urbe detrusi, in synodo quoque Ephesiensi… postmodum… damnati sunt" (Garnier's preface, l.396–403). Garnier adds "Habuit autem, ut fasti docent, annus 429 consules Florentium et Dionysium" (l.404). The telling is faithful; for the year see M1.
- Gennadius (l.3): "ne appellatus quidem sit de nomine, vel a Gennadio… ecclesiasticorum scriptorum censore" (l.304–306). "Prodeunt nunc primum in lucem opera Marii Mercatoris" (l.303) supports "his first editor". The section is headed "GARNERII PRAEFATIO GENERALIS".
- "my son" (l.3; card `legacy.remembered` 1): Letter 193 is addressed "filio Mercatori" and says "fili dilectissime" (PL33 l.63823, 63882). Augustine's own "filium meum… Mercatorem" is in his book to Dulcitius, quoted by Garnier (PL48 l.320–321). This is a fair English rendering of Latin the brief says is "held here in Latin", so it is noted and not counted.
- Letters received at Carthage (l.3): "Litterae… quas prius abs te missas apud Carthaginem accepi" (PL33 l.63838–63839). "He had not known… how far Mercator had grown": "tantum te profecisse nesciebam" (l.63884–63885). Faithful.
- Origin (l.5): Garnier's "vel Campanus fuit, vel Apulus, vel ex ea parte Italiae quae vergit ad Siciliam", because he knew the private affairs of Caelestius and Julian (l.459–462); Baluze's "quoniam mihi quoque fas est divinare, arbitror hunc nostrum Mercatorem fuisse Afrum" (Baluze's preface, l.2220–2224); Schoenemann's "conjecturis innituntur, haud quidem improbabilibus" (l.2290–2296). Faithful. Schoenemann gives the African view first to Gerberon, with Baluze agreeing (l.2304–2311). The brief does not need that detail.
- Lay status (l.5): Garnier argues from "filium" against "fratres… coepiscopos" (l.486–495) and from his absence among the bishops at Ephesus (l.497–501). Hefele: "The Western layman, Marius Mercator… who at that time resided in Constantinople" (`hefele_…clark1883.txt` l.1242–1243). Faithful.
- Translations (l.7): the preface's "nonnulla ad plebem blasphemiarum dicta… ex Graeco in Latinum sermonem… curavi transferre, a fidelibus linguae meae fratribus cognoscenda atque vitanda" (l.58505–58515), with "Nestorii quondam episcopi". The note "Scripta est prooemialis haec epistola post concilium Ephesinum, quod ostendunt haec verba: Nestorii quondam episcopi" (l.58524–58526) belongs to Garnier's notes, which reorder the codex by date. Faithful.
- Hefele on the anathemas (l.7; card `legacy.traces` 1): "These have been preserved for us only by the Western layman Marius Mercator" (Hefele l.2428–2431). Faithful.
- Theodore of Mopsuestia (l.9): "Quaestio contra catholicam fidem… a Theodoro quondam episcopo oppidi Mopsuesteni jamdudum mota" (Liber Subnotationum preface, l.6828–6835). Faithful.
- The rumours (l.9): the private matters Garnier lists from Mercator, Caelestius "vitio naturae eunuchum" and Julian "creditum… suppositam fuisse" (l.470–479). "Rumours" is the narrator's word for an opponent's report, and the card marks it as such.
- Chalcedon (l.11): Garnier's "vel non pervenisse ad annum 450… vel ex eo tempore nihil scripto mandasse" (l.442–444); Baluze's "superstitem fuisse concilio Chalcedonensi, quod… mentionem facit Eutychianorum" (l.2262–2273). Faithful.
- The close (l.13): "verbum de verbo, in quantum fieri potuit, conatus sum translator exprimere, ne prius falsarius magis quam verus postea probarer interpres" (l.58547–58549). Faithful.
- Card: Garnier's 418 for Augustine's letter ("accepit ab Augustino epistolam ann. 418", l.332–333; argued at l.340–384); Warfield's "an African layman" (`npnf105` l.1468, Warfield's own prose). Exact, and the speakers are right.

**Narrative checks**
- records.json matches the brief and card, and carries `contested_claim` records for origin and for Chalcedon.

**Findings**
- **M1 MINOR (item 1; recurring fault 3).** Brief l.1 opens "In 429 a Latin writer named Marius Mercator gave…", and the next sentence is "Its title says…". The title gives only the consuls Florentius and Dionysius. Garnier converts them to 429 "ut fasti docent" (l.404). Placed next to "Its title says", the year sounds as though the title gives it. The card gets this right ("in 429, by the consuls its title names"), and the Prosper brief in this same batch says "which Mommsen's edition sets in 429". Fix: l.1 "In 429, by the consuls its title names, a Latin writer named Marius Mercator gave the church of Constantinople a short warning, written in Greek."
- **M2 MINOR (item 8, card; item 1).** (a) Card `keyWorks` 1: "offered to the emperor Theodosius". Theodosius is a common name and this is the card's first mention of him. Hefele gives "the Emperor Theodosius the younger" (Hefele l.2426). Fix: "offered to the emperor Theodosius the Younger". (b) Card `uncertain` 3: "One manuscript of Possidius reads \"bishop\", which Garnier takes as a copyist's slip." Garnier gives no manuscript. He corrects "Possidii indiculo, ad Mercatorem episcopum", put there "notariorum culpa", in Possidius's list of Augustine's works (l.523–526), and the words he cites are found only in Hommerius's Louvain printing (l.325–330). The card also gives Possidius no context. Fix: "Possidius's list of Augustine's works, as printed at Louvain, reads \"bishop\"; Garnier takes it as a copyists' slip for \"letter\"."

---

## 2. Eutyches (MAJOR)

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | FAIL, minor (M3, M4) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | FAIL, minor (M4: a thesis opener with a loose generalisation) |
| 5 | No role for a witness | PASS in the brief; card minor (M5: "modern notes") |
| 6 | Partisan witness named and marked | PASS (opponents told through events; card `uncertain` 3) |
| 7 | Contested both sides | PASS (minutes; appeal) |
| 8 | Common names placed | PASS |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | PASS (2:25, under the cap) |
| 11 | grade_text | PASS |
| 12 | Card order, caveat repeated | PASS |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |

**Quotes** (all exact; speaker given)
- "I confess that our LORD was of Two Natures before the Union, but after the Union I confess Him to be of One Nature." (l.1): the minutes of Flavian's synod as read at Ephesus in 449, Eutyches answering Florentius (Perry, `council-of-ephesus-449_…perry1881.txt` l.23835–23845). Leo's Tome quotes the same answer (`npnf212` l.5597).
- November 448 (l.1): Perry's footnote "the one held in Nov. 448, A.D. at Constantinople, at which Eutyches was condemned" (Perry l.19121); Feltoe's introduction "in November, 448" (`npnf212` l.580). Both are named as editors. Correct.
- "dedicated to God from his birth" (l.3, told): the petition to the council, "in It, too, was I born and forthwith dedicated to God" (Perry l.23388–23390), under "THE LIBEL OF EUTYCHES… TO THE HOLY SYNOD" (l.23325–23336).
- "seventy years of life in continence and all chastity", "the defender of religion", the anathemas on Apollinaris and Nestorius, and "I stand in jeopardy of my life as a heretic" (l.3, l.13): Eutyches to Leo, Letter 21 (`npnf212` l.4596–4610). Exact.
- "what he said to me was not put on paper, and what I did not say, they put into the Documents" (l.5): petition to Theodosius and Valentinian (Perry l.23295–23311). Exact.
- "this he certainly never did" (l.5): Flavian to Leo, Letter 26 (`npnf212` l.5023–5028). Flavian is denying what Leo had told him Eutyches wrote. Faithful.
- "This sentence, therefore, was altered." (l.7): Juvenal (Perry l.23871–23873). "to his Monastery and to his Grade" (l.7): see M3.
- "very unwary and exceedingly ignorant" (l.9): the Tome, Letter 28, chap. 1 (`npnf212` l.5127). Exact.
- "for the removal of the false doctrines of Eutyches" (l.9): Definition of Chalcedon (`npnf214` l.20262–20267). Exact.
- Feltoe's summary (l.9): Letter 134 to Marcian, "(Suggesting that Eutyches should be banished to a still remoter place…)" (`npnf212` l.11331–11333), with no translated text. The brief names Feltoe and calls it his summary. Correct.
- "introduced and increased the heresy of Nestorius" (l.11): the chronicle, book III, Zachariah's preface to Eupraxius (`zachariah-rhetor_…1899.txt` l.2174–2178). "affirmed an inaccurate dogma… not having been well instructed" (l.11, the last words told): book II (l.1167–1172). Both are the chronicle's.
- Card: "the ignorant old man" is Leo to Theodosius, Letter 29 (`npnf212` l.5706), not one of the letters the card lists (M5). The godson is in Liberatus, "quem Eutyches susceperat de sacro baptismate" (PL68 l.78115–78118), and in Feltoe's "the eunuch Chrysaphius, Eutyches' godson" (`npnf212` l.588–589).

**Narrative checks**
- "Later councils name Eutyches beside Nestorius" (card `legacy.traces` 2): Constantinople II, anathema XI, and the canon on returning heretics (`npnf214`). Supported.
- records.json matches the brief and card, with `contested_claim` records for the minutes and the appeal.

**Findings**
- **M3 MINOR (items 1, 5; a vote given to the council; a hedge left out).** Brief l.7: "The council restored Eutyches \"to his Monastery and to his Grade.\"" The quoted words are Juvenal of Jerusalem's own vote: "I, also, decree and vote that he be restored to his Monastery and to his Grade". The Synod answers only "That is a correct judgment." (Perry l.24015–24024). The same paragraph has Basil of Seleucia deny the sentence. In the acts he then says, "I do not remember and I do not know if I did say so." (Perry l.23876–23877). Card `uncertain` 1 uses his denial as evidence that the record was false. Fix: l.7 "At Ephesus in 449, under Dioscorus of Alexandria, the minutes were read again. Basil of Seleucia denied a sentence written as his, though he then said he did not remember. Juvenal of Jerusalem declared, \"This sentence, therefore, was altered.\" Juvenal voted that Eutyches be restored \"to his Monastery and to his Grade,\" and the council agreed." Card `uncertain` 1: "…Basil of Seleucia denied a sentence written as his, then said he did not remember." This adds about 13 words. With M4 the brief is about 401 words, still under the cap.
- **M4 MINOR (items 1, 4; loose generalisation, thesis opener).** Brief l.11 opens "Those who rejected Chalcedon did not take his side either." The sentence speaks for a whole party on the strength of one chronicle, and that chronicle partly does take his side. It says the 448 accusers taught "the two Natures after the union… in conformity with the doctrine of Nestorius" (l.1226–1229), and that at Ephesus "Eutyches the archimandrite was received, because he presented a libel of recantation… and confessed the true faith" (l.1308–1310). The brief's own l.7 has Dioscorus's council restoring him. Card `uncertain` 7 calls the chronicle "that church's own Syriac chronicle", meaning the card's Alexandrian and Egyptian tradition. Hamilton and Brooks place the compiler at Amida, or at any rate in Mesopotamia (l.453–455). Fix: delete l.11's first sentence and open "The Syriac chronicle known as that of Zachariah of Mitylene, from the side that rejected Chalcedon, says the council \"introduced and increased the heresy of Nestorius.\" Yet it also says Eutyches \"affirmed an inaccurate dogma,\" not having been well taught." Card `uncertain` 7: "The card's tradition is the scan's. The Syriac chronicle cited here comes from the side that rejected Chalcedon; Hamilton and Brooks place its compiler in Mesopotamia, probably at Amida. It faults his teaching, though it says he was received at Ephesus after he confessed the true faith."
- **M5 MINOR (card: items 1, 5, 12).** (a) `keyWorks` 1 says "held in Latin, in Feltoe's English (Leo, Letter 21)". The Library holds no Latin of Leo's letters, and Feltoe's note says "the Gk. original is not found", the text coming from a Monte Cassino collection printed by Lupus and Baluze (`npnf212` l.4500–4504). Fix: "his appeal against Flavian's sentence; the Greek is lost, and the Library holds Feltoe's English of the Latin (Leo, Letter 21)". (b) `legacy.remembered` 1 quotes "the ignorant old man" from Letter 29, which the Sources list leaves out. Fix: source title "Letters 22, 26, 28 (the Tome) and 29". (c) `uncertain` 4 says the godson rests "on modern notes". The one held modern witness is Feltoe's introduction (`npnf212` l.588–589). Fix: "…held only in a rough scan, and on Charles Lett Feltoe's introduction to Leo's letters."

---

## 3. Prosper of Aquitaine

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | FAIL, blocking (B1); minor (M6) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | FAIL, minor (M7) |
| 5 | No role for a witness | FAIL, minor (B1: "his editors" for a translator) |
| 6 | Partisan witness named and marked | PASS (Gennadius "who sided with Cassian"; Gibson "not scrupulously fair"; Prosper's "those he saw as enemies of grace") |
| 7 | Contested both sides | FAIL, minor (M6) |
| 8 | Common names placed | PASS in the brief; card minor (M8) |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | PASS (2:04) |
| 11 | grade_text | PASS |
| 12 | Card order, caveat repeated | PASS |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |

**Quotes and close tellings**
- Letter to Augustine (l.1): "Ignotus quidem tibi facie… per… fratrem meum Leontium diaconum misi epistolas et recepi" and "Multi ergo servorum Christi qui in Massiliensi urbe consistunt… contrarium putant patrum opinioni… quidquid in eis de vocatione electorum secundum Dei propositum disputasti" (PL33 l.73495–73514). Faithful.
- "scholastic in style and vigorous in statement" (l.3), "brands as injurious" (l.7), and the letters of Leo "are also thought… to have been dictated by him" (l.9; card): Gennadius 85 (`npnf203` l.43663–43675). Exact. The years 403 and 463 in the same place are Richardson's endnote, not Gennadius's (see B1).
- Gibson (`npnf211` l.15692–15772): "Hilary (a layman, not to be confounded with his namesake, the Bishop of Arles)"; "Prosper of Aquitaine, also a layman"; "This fixes the date of the correspondence as 429"; "almost his latest works"; "De Ingratis" after Augustine's treatises; the appeal to Pope Celestine after Augustine's death and "a letter addressed to the Gallican Bishops"; "Cassian, the leading presbyter, of the diocese of Marseilles"; "a treatise of considerable power and force, although not scrupulously fair". All Gibson's own words, and the brief names him.
- Mommsen (`prosper_chronica-minora-1-lat_mommsen1892.txt`): "cuiusnam civitatis fuerit, ignoratur" (l.42726–42727); "clericum quidem eum fuisse vel eo tempore, quo epistulam illam ad Augustinum dedit, quod in ea… diaconum Leontium fratrem suum dicit" (l.42768–42770); "episcopi locum eum tenuisse recte negavit Sirmondus" (l.42777); "inde medio aevo collegerunt Prosperum notarium factum esse ecclesiae Romanae: vere ne hoc quidem ex ea narratione efficitur sedem eum in Gallia cum domicilio urbano permutavisse" (l.42789–42792); "postremum a. 455, ad hunc advixit" (l.42792–42793). The brief and card are faithful.
- Chronicle 1301 under "Florentio et Dionysio", with Mommsen's margin "a. 429" (l.54144–54155): Celestine, "ad insinuationem Palladii diaconi", sends Germanus "Autisidorensem episcopum… et deturbatis hereticis Britannos ad catholicam fidem dirigit". Faithful, and the brief calls the year Mommsen's.
- Chronicle 1304 (l.11): "Aurelius Augustinus… moritur V. kl. Sept., libris Iuliani inter impetus obsidentium Wandalorum in ipso dierum suorum fine respondens et gloriose in defensione Christianae gratiae perseverans" (l.54206–54209). Faithful. Julian is "Aeclanensis" in Prosper's own later entry, as the record says.
- Card: Palladius "ad Scottos in Christum credentes ordinatus… primus episcopus" (l.54222); Freese's note "Prosper of Aquitaine (403-463)" and Photius's "truly a man of God" (`photius_library-v1_freese1920.txt` l.3530, 3543); Garnier's "Restitere primi Massiliensibus presbyteris laici duo, Hilarius et Prosper" (PL48 l.570–571). Exact.

**Findings**
- **B1 BLOCKING (items 1, 5; recurring fault 5).** Brief l.3: "No held source gives his city, birth or death, and his editors disagree on whether he was a layman." Two held editors give his birth and death. Richardson's endnote to Gennadius 85 reads "Born 403, wrote chronicle 445? died 463." (`npnf203` l.43663), and Freese's note to Photius reads "Prosper of Aquitaine (403-463)" (`photius_library-v1_freese1920.txt` l.3543). The card and the record already say so ("No ancient source used here gives his birth or death. The years 403 to 463 are an editor's note…"), so the brief contradicts its own card on a core fact. "His editors" is also wrong for Gibson, who translated Cassian and did not edit Prosper. Fix: l.3 "No ancient source used here gives his city, birth or death, and those who wrote on him later disagree on whether he was a layman."
- **M6 MINOR (items 1, 7; recurring fault 4).** Brief l.5 tells the appeal "Gibson says" with "a layman named Hilary who was not the bishop of Arles", and card `uncertain` 4 calls the appeal "Gibson's account". Mommsen, the card's own editor of the chronicle, names the other letter's writer "Hilario episcopo Arelatensi" (l.42731). His note argues that this Hilary "cum se laicum dicat, scripsit antequam episcopus Arelatensis factus est" (l.42748–42750). The Maurist note in Augustine's letters keeps them apart: "alius profecto ab Hilario Arelatensi" (PL33 l.73873). So a held editor disputes the identification, and the profile does not say so. Fix: l.5 "…Prosper and a friend, a layman named Hilary, appealed to Pope Celestine. Gibson keeps this Hilary apart from Hilary of Arles; Mommsen takes them as one man, writing before he became bishop." Card `uncertain` 4: add "Mommsen takes the Hilary who wrote with him for Hilary of Arles before he became bishop; Gibson and the Maurist note in Augustine's letters keep them apart." Records: add a `contested_claim` for it.
- **M7 MINOR (item 4).** Brief l.7: "…says the church finds Cassian's works helpful, while Prosper \"brands as injurious\" them." The quote fragment pushes the object to the end of the sentence, and the line is hard to follow aloud. Fix: "Gennadius, who sided with Cassian, says Prosper \"brands as injurious\" works that the church finds helpful."
- **M8 MINOR (card: items 1, 8, 12).** (a) `knownFor`: "against the monks of Marseilles". No held line calls them monks. Prosper's letter has "servorum Christi qui in Massiliensi urbe consistunt", Garnier "Massiliensibus presbyteris", Gibson "the School of Marseilles". Fix: "against many at Marseilles". (b) `legacy.remembered` 2 quotes Photius, and `uncertain` 5 cites Freese's note, but the Sources list does not include the Photius file. Photius is also a common name and has no place at this, his only mention in the card. Fix: "Photius of Constantinople, in his Library, calls him…", and add to `sources.about` {"title": "Library (tr. J. H. Freese)", "author": "Photius of Constantinople", "language": "English translation", "file": "cic/texts/photius_library-v1_freese1920.txt"}.

---

## 4. Eznik of Kolb

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | FAIL, blocking (B2) |
| 2 | Quotes verbatim | PASS (no quote marks; tellings checked) |
| 3 | No invention | PASS |
| 4 | Reading aids | FAIL, minor (M9) |
| 5 | No role for a witness | PASS ("the introduction to his book in Victor Langlois's collection" is used because it is unsigned) |
| 6 | Partisan witness named and marked | PASS (l.3; card `uncertain` 1) |
| 7 | Contested both sides | PASS (Koriun v. Moses of Khoren on the journey) |
| 8 | Common names placed | FAIL, minor (M10) |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | PASS (2:06) |
| 11 | grade_text | PASS |
| 12 | Card order, caveat repeated | PASS |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |

**Close tellings** (`langlois_collection-historiens-armenie-tome2-fra_1869.txt`)
- Zurvan (l.1): "Avant que rien n'existât, disent-ils (les mages)… il y avait un certain Zérouan… Pendant mille ans, il fit des sacrifices pour qu'il lui naquît un fils qui serait appelé Ormizt, qui créerait les cieux et la terre… Ormizt à cause des sacrifices… et Arhmèn, parce qu'[il avait] douté" (l.49638–49652). Faithful. "(les mages)" is the translator's gloss in parentheses, the only place the extract uses the word. The chapter title, "Réfutation de la religion des Perses", carries the same sense, so it is noted and not counted.
- The refutation (l.3): "il est prouvé que Zérouan était impuissant, imparfait et ignorant. La cause des maux, c'est lui-même" and "jamais deux sources ne sortent d'un seul orifice… jamais d'un même arbre ne proviennent deux fruits" (l.49830–49842). Faithful; for the attribution see M9.
- Four parts, the Nilus Maxims, only §§ I–11 of chapter II translated (unsigned introduction, l.49448–49548). "Un des plus illustres écrivains qu'ait produits l'Arménie au Ve siècle est sans contredit Eznig" and "on ignore même l'époque de sa naissance et la date de sa mort" (l.49331–49405). Faithful. "No one recorded his birth or death" closely tells "Les biographes et les annalistes ne nous ont transmis aucun détail".
- Koriun (l.5): "ils envoyèrent deux de leurs disciples, Eznig et Joseph, dans la ville d'Édesse, pour qu'ils traduisissent de nouveau en arménien les Saintes-Écritures sur le texte syriaque… Puis ils passèrent… à Byzance… devinrent traducteurs de la langue grecque… Léon… Gorioun… se joignirent à Eznig, comme à un frère de la même famille, avec qui ils avaient été élevés… copies authentiques… canons des saints conciles de Nicée et d'Éphèse" (l.3807–3861). The note "(2) L'auteur de la Biographie de Mesrob" (l.3896) confirms that this Gorioun is Koriun. Faithful.
- Moses of Khoren (l.7): "d'après des lettres mensongères de quelques fourbes… s'y rendent sans retard et sans en avoir reçu l'ordre de leurs docteurs" (l.24618–24622); "leur travail fut trouvé défectueux en beaucoup de points" (l.24730–24734). Faithful.
- Burkitt (card): "Eznik's well-known chapters against them" and "very likely… a translation from some early Syriac writer" (`ephraim_prose-refutations_mitchell1912-1921.txt` l.2628, in the "INTRODUCTORY ESSAY BY F. C. BURKITT", l.2586). Exact.

**Findings**
- **B2 BLOCKING (item 1; recurring fault 1, witness swap).** Brief l.9: "Elishe and Lazar of Pharp both list him among the bishops who met at Artashat to answer an edict. It came from Mihr-Nerseh, the Persian governor…" Only Elishe gives the place and the sender. Elishe's bishops are "réunis ensemble à Ardaschad" and answer "Mihr-Nersèh, gouverneur suprême de l'Iran et de l'Aniran" (l.27118–27129, 27344–27354). Lazar's list ("le seigneur Emig, évêque de Pakrévant", l.38341) names no place. In Lazar the assembly answers "l'édit du roi Iezdedjerd" (l.38371–38372), which "le roi… rédigea" (l.38241–38242). Only an editor's note in Lazar links it to Mihr-Nerseh's letter (l.38325–38327). Card `uncertain` 3 repeats the error where it weighs witnesses on the place: "…though Elishe and Lazar of Pharp place it at Artashat". That counts two ancient witnesses for one. The record's witness line for the claim does the same. Fix: l.9 "Elishe and Lazar of Pharp both list him among the bishops who answered a Persian edict calling Armenia to the Persian faith. Elishe places the meeting at Artashat and says the edict came from Mihr-Nerseh, the Persian governor. Lazar names King Yazdegerd as its author. Neither writer gives a year." Card `uncertain` 3: "…The introduction to his book calls the gathering a council of Ashtishat, though Elishe places it at Artashat; Lazar of Pharp names no place." Card `dates`: change "signed as bishop of Bagrevand at the assembly of Artashat, which neither Elishe nor Lazar of Pharp dates" to "is listed as bishop of Bagrevand among those who answered the Persian edict, at Artashat by Elishe's account; neither Elishe nor Lazar of Pharp gives a year". Neither list is a signature. Records: in the claim, make the witness line Elishe for the place and Mihr-Nerseh, and Lazar for the list and Yazdegerd's edict.
- **M9 MINOR (items 1, 4).** Brief l.3: "Two springs never flow from one opening, one sweet and one bitter. One tree never bears a sweet fruit and a bitter one." These are Eznik's arguments, but they stand in the narrator's voice with no attribution, so they sound like the narrator's own sayings. Fix: "Two springs never flow from one opening, he argued, one sweet and one bitter, and one tree never bears a sweet fruit and a bitter one."
- **M10 MINOR (item 8, brief and card).** "Sahak" (brief l.5; card `knownFor`) has no identifier, though the same held lists have a second Sahak, bishop of the Reshtunik (l.27344, 38340). Moses gives "Sahag le Grand" (l.24610). "Joseph" (brief l.5; card `uncertain` 2) has none either, though card `uncertain` 3 names a second Joseph, the catholicos. The introduction gives "son condisciple Joseph de Baghin" (l.49364). "Leon" (brief l.5) has none; Langlois's note gives "Léon ou Ghévont, prêtre de Vanant" (l.3887). Fix: brief l.5 "a pupil of Sahak the Great and of Mesrop Mashtots", "a companion, Joseph of Baghin", "Koriun and Leon, a priest of Vanand,"; card `knownFor` "a pupil of Sahak the Great and Mesrop Mashtots"; card `uncertain` 2 "drew him and Joseph of Baghin to Byzantium".

---

## Totals

2 blocking (B1 `prosper-of-aquitaine`; B2 `eznik-of-kolb`) and 10 minor (M1–M2 `marius-mercator`; M3–M5 `eutyches`; M6–M8 `prosper-of-aquitaine`; M9–M10 `eznik-of-kolb`). Every fix above was checked against the line it cites. Eutyches stays under the major cap with M3 and M4 applied (about 401 words).
