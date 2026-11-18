# R1 review: ten Who profiles, era 3 batch 4

Three independent Opus reviewers, each seeing the drafts for the first time, reviewed the batch in three parts. Part A covered Theodosius I of Alexandria, Jacob Baradaeus and Longinus, bishop of the Nobadae. Part B covered John of Ephesus, Victor of Tunnuna, Cassiodorus and Agathias of Myrina. Part C covered Gildas, David of Wales, Radegund and the README. Totals: 6 blocking and 63 minor (part A 3 and 21, part B 1 and 25, part C 2 and 17).

## Part A

Reviewer: independent, first sight of these drafts. Bar: `Who_Profile_Pattern.md` review checklist 1 to 14 and the standards it points to; `CLAUDE.md` "Trust and source fidelity" and "Accessible and rigorous"; the batch rulings in the brief (majors capped at 2:30, about 405 words at 162 wpm, a cap and not a target; non-majors 1 to 2 minutes, at most about 325 words). Theodosius I of Alexandria and Jacob Baradaeus are majors by the coordinator's call; Longinus is a non-major. I hunted hardest for false absences, editor's years told as the ancient writer's, notices credited to the wrong source, witness swaps, non-verbatim quotes, contested points told one way, unmarked partisan witnesses, common names without a place, AI tells and long sentences. I edited no repo file, made no paid or model-API call and used no web.

Profiles: `theodosius-i-of-alexandria` (major), `jacob-baradaeus` (major), `longinus-bishop-of-the-nobadae`, with their cards, audio scripts and `records.json` entries, in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era3/batch4/`. Brief line numbers refer to the `.brief.txt` files (paragraphs on l.1, 3, 5, 7, 9, 11). Card line numbers refer to the `.card.json` files as they stand. Other line numbers point to files under `cic/texts/`.

Method. I read every quotation in the briefs and cards against its file by line number, and each hit in context to see who speaks (the ancient writer, a document he quotes, a translator's bracket or note). I checked each factual sentence against its passage. Before accepting an absence claim I searched every held file that names the person (Liberatus/Victor PL 68, Mommsen's Chronica minora II, the three Brooks Lives files, both Payne Smith files, Evetts's History of the Patriarchs, Renaudot, both Chabot Michael volumes, Bar Hebraeus, the Ethiopic and Arabic synaxaries, Mansi 10 and 11, Moschus/Sophronius PG 87.3, Assemani, Hefele, Elias of Nisibis, Crum's Epiphanius ostraca). Readability is `engine.m1.gates.grade_text`, run from the repo root. Every suggested brief fix below was applied to a scratch copy and re-scored; the post-fix counts and scores are given per profile.

### Applies to all three

- **Audio = brief.** Each audio script equals its brief once `[calmly] ` and `[warmly] ` are removed (checked by script). Each starts with `[calmly]` and has one `[warmly]`, before the last paragraph. No tag is in any brief or card. When a fix changes a brief line, the audio script follows it.
- **Readability.** All three pass. Narrator sentences past 25 words: Theodosius l.1 (29), l.3 (28), l.5 (39) (A-M2). Jacob and Longinus have none outside quotes.
- **Length.** Theodosius 400 words (2:28), Jacob 404 (2:30), Longinus 321 (1:59). All inside their caps; every `briefLength` matches.
- **Card order.** All three follow Mark's order; missing fields are left out (Jacob has no keyWorks). Each `uncertain` list opens with or carries the brief's caveat.
- **Who test (item 14).** Theodosius: patriarch with a following named after him (the Theodosians). Jacob: the ordaining bishop of the anti-Chalcedonian church, with the Jacobites named after him. Longinus: missionary bishop with a following among the Nobadae and the Alodaei and a letter of his own. List lines are not in these drafts and were not checked.

| Profile | Words | Est. @162 | FK | Flesch | After fixes |
|---|---|---|---|---|---|
| Theodosius I of Alexandria (major) | 400 | 2:28 | 8.1 | 64.5 | 401 words, FK 7.2, Flesch 66.1 |
| Jacob Baradaeus (major) | 404 | 2:30 | 5.9 | 75.9 | 402 words, FK 6.0, Flesch 75.6 |
| Longinus, bishop of the Nobadae | 321 | 1:59 | 7.1 | 70.3 | 320 words, FK 7.1, Flesch 70.2 |

---

### 1. Theodosius I of Alexandria (major)

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | minor (A-M1, A-M4) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | minor (A-M2, A-M8) |
| 5 | No role for a witness | PASS |
| 6 | Partisan witness named and marked | BLOCKING (A-B1) |
| 7 | Contested both sides | BLOCKING (A-B1, A-B2) |
| 8 | Common names placed | minor (A-M3) |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | PASS (400 words) |
| 11 | grade_text | PASS (FK 8.1, Flesch 64.5) |
| 12 | Card order, caveat repeated | PASS |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |

**Quotes and close tellings checked**
- Opening (l.1): Liberatus, Breviarium 20, `liberatus-victor-tunnunensis-primasius-junillus-pl68-lat_migne1866.txt` l.81263-81280: "Consuetudo quidem est Alexandriae illum qui defuncto succedit excubias super defuncti corpus agere, manumque dexteram ejus capiti suo imponere, et sepulto manibus suis, accipere collo suo beati Marci pallium… dum hoc Theodosius nocte pertentat, cognoverunt populi et monasteria quid esset factum vespere in episcopio… mox Theodosium persecuti sunt et expulerunt, ne colligeret funus Timothei" (OCR "Consueludo", "Alexandiia", "luc Theodositis"). "Vivitque usque nunc" (l.81332). Faithful, except A-M1. Liberatus is a deacon of Carthage (l.74548, l.74953).
- Zachariah chronicle (l.3): `zachariah-rhetor_chronicle_hamiltonbrooks1899.txt` l.13194-13199, "after Gaian had been driven out, who was a Julianist, and was there for three months after the death of Timothy, Theodosius became bishop, a man of conspicuous faith and learned and kind and gentle; and he was an acquaintance and a friend of the holy Severus". Faithful.
- Narses (l.3): Liberatus l.81291-81310, "Narses cubicularius missus ab Augusta Theodora, Theodosium quidem inthronizavit… igne vicit, quod ferro non potuit. Divisa est usque nunc illa civitas… ut Gaianitae et Theodosiani in ea vocentur". Faithful.
- Speech (l.5): Evetts, `severus-al-muqaffa_history-patriarchs-coptic-church-v1_evetts1904.txt` l.38592-38594, "The prince has no power except over my body; but the Lord Jesus Christ, the true and great prince, has power over my soul and body together." Exact. Renaudot l.9935-9936, "ab Historici sincerissimi testimonio longe discrepat". Faithful. See A-M4 on the offer.
- Dercus (l.7): `john-ephesus_lives-eastern-saints-po18_brooks1924.txt` l.32346-32354, "the bishops with the most eminent clergy, about three hundred of them, in the interior of Thrace… a certain fortress called Dercus, to which also we often used to go to visit the same saints". Faithful.
- Twelve bishops and Jacob (l.7): `john-of-ephesus_lives-of-the-eastern-saints_brooks1923.txt` l.26920-26924, "by the mandate of the blessed Theodosius the patriarch, they ordained twelve bishops… Inasmuch as the patriarch Theodosius would not consent to ordain priests after he had left his see"; l.26805-26817, "having received the advice and permission of the blessed Theodosius… made these two blessed men bishops". Faithful.
- Letter to Anthimus (l.9): chronicle IX.26 (heading l.14452), l.14484-14485, "For I, who am feeble, judge that it is on account of my shortcomings that I endure all the troubles which befall me". Exact. l.14556-14558, "the formula of Zeno uniting the Churches, which aimed at the annulling of the Synod of Chalcedon and of the Tome of Leo". Faithful.
- Death (l.11): Brooks PO 18 l.39353-39363, "nine months after the death of the same Justinian the king"; note 6, "This would place his death in A[ug.] 566" (OCR damaged). Evetts heading l.37025, "A. D. 535-567" (OCR "o3.)-.)G7"). Evetts l.39594-39595, "counted worthy to be called Theodosians after his name". Exact.
- Card: the Severus letter quote, "a man of conspicuous faith…" and the Michael, Victor and Payne Smith items match their files (Michael tome 2 l.13868 "un général avec 6.000 hommes", l.14043-14046 "10 ans dans le palais"; Victor, Mommsen l.18802-18803 "ordinantur uno die episcopi, Theodosius scilicet et Gaianus", l.18872 "haereticus"; Payne Smith `john-of-ephesus_…` l.2519-2520 "to his death in A. D. 567"; Garnier PL 68 l.75135-75136 "anno I Justini junioris, qui Christi 566"). "Pope Theodosius" is in John, Payne Smith `john-ephesus_…` l.11052. The Lateran and Sophronius condemnations are true (A-M5).
- Absences checked: birthplace, family, age (none in Evetts l.37027-37040, Liberatus, John, Michael, Ethiopic synaxary); the treatise against the Tritheites (Michael reports it, l.19229-19238, l.19345-19348, without its text). No absence claim is contradicted. A held fragment the card leaves out is A-M9.

**Findings**

- **A-B1 BLOCKING (items 6, 7).** No witness in the brief is marked as partisan, and the opening rests on the hostile one. Brief l.1 "So says Liberatus of Carthage, a deacon who wrote while Theodosius still lived." Liberatus writes from the side of Chalcedon and calls the Theodosians "Corrupticolae" (PL 68 l.81316-81318, "Gaianitae et Theodosiani… id est, Phantasiastae et Corrupticolae"); the card says so (`uncertain` 3, l.36, "Liberatus from the side of Chalcedon") but the brief does not. The chronicle under Zachariah's name (l.3), the History of the Patriarchs (l.5) and John of Ephesus (l.7) are all of his own party, and none is marked. Then l.3 tells the order of ordination as settled in the narrator's voice, "A rival, Gaianus, was set up in his place", though the chronicle the same paragraph cites has Gaianus there first (l.13194-13197, "after Gaian had been driven out… and was there for three months after the death of Timothy, Theodosius became bishop") and Victor has both on one day (Mommsen l.18802-18803). The card and records carry this dispute (`uncertain` 1; contested claim "Who was ordained first"); the brief does not. Fix:
  - l.1: "So says Liberatus of Carthage, a deacon on the side of Chalcedon who wrote while Theodosius still lived."
  - l.3: "The Syriac chronicle under the name of Zachariah Rhetor, from his own side, calls him learned, kind and gentle, and a friend of Severus of Antioch." and "A rival, Gaianus, was set up in his place, though that chronicle puts Gaianus first."
  - l.5, first sentence: "The History of the Patriarchs of Alexandria is a later history written in his own church. It tells how Justinian offered him the governorship of Egypt if he would accept the Tome of Leo." (Renaudot's judgment stays in the card, `uncertain` 3.)
  - l.7: "John of Ephesus, of his own party, says he and about three hundred bishops and clergy were held at Dercus, a fortress in Thrace. John often visited them there."
  - Word room: "Summoned to Constantinople, he still refused Chalcedon." and "With his permission, Jacob Baradaeus made bishops at Alexandria." (l.7).

- **A-B2 BLOCKING (items 1, 7; witness misreported).** Card `uncertain` 5 (l.38): "The Coptic and Ethiopic notices give twenty-eight years in Upper Egypt." The Coptic notice, the History of the Patriarchs, says otherwise: "Theodosius remained twenty-eight years in banishment and otherwise, and in Upper Egypt four years" (Evetts l.39586-39587, OCR "twcnl v-eiidit \ears in hanislnncnt… in Upper Kgypt four yiaaivs"). Only the Ethiopic synaxary gives twenty-eight years in Upper Egypt (`ethiopian-synaxarium_book-of-saints-ethiopian-church-v2-v4-microform_budge1928.txt` l.37624-37626, "THEODOSIUS remained in exile in Upper Egypt for eight and twenty years"), and it is not in the card's sources. The records' contested claim "Where his long exile was" also names "the Ethiopic and Arabic synaxaries" but cites only the Ethiopic file; no held Arabic synaxary covers Baounah. Victor of Tunnuna's own placing is missing too: "Theodosius Constantinopolim Sycas relegatus" (Mommsen l.18841). Fix, card `uncertain` 5: "Where his exile was. John of Ephesus says the fortress of Dercus in Thrace; Liberatus, six miles from Constantinople; Victor of Tunnuna, Sycae at Constantinople; Michael the Syrian, ten years in Theodora's palace. The Ethiopic Synaxarium gives twenty-eight years of exile in Upper Egypt. The History of the Patriarchs gives twenty-eight years 'in banishment and otherwise', and four in Upper Egypt." Add the Ethiopic Synaxarium (tr. E. A. W. Budge) to `sources.about`. In records, change the contested claim's last side to "The Ethiopic Synaxarium: twenty-eight years in Upper Egypt (l.37624-37626). The History of the Patriarchs: twenty-eight years in banishment and otherwise, four in Upper Egypt (l.39586-39587). Victor of Tunnuna: Sycae (Mommsen l.18841)."

- **A-M1 MINOR (item 1).** Brief l.1 "On the night the patriarch Timothy died, the new bishop kept watch over the body." Liberatus places the vigil at night after an evening ordination ("dum hoc Theodosius nocte pertentat… quid esset factum vespere in episcopio", l.81273-81275). He does not say it was the night of the death. Fix: "When the patriarch Timothy died, the new bishop kept watch over the body by night."

- **A-M2 MINOR (item 4).** Narrator sentences past 25 words: l.1 "At Alexandria, the custom was… pallium of Saint Mark." (29), l.3 "Theodosius I of Alexandria was patriarch… in exile." (28), l.5 "The History of the Patriarchs… Tome of Leo and Chalcedon." (39; fixed by A-B1). Fix, l.1: "By custom at Alexandria, the successor laid the dead man's right hand on his own head. Then he buried him and put on the pallium of Saint Mark." ("the successor" is Liberatus's "illum qui defuncto succedit".) l.3: "Theodosius I of Alexandria was patriarch of the church in Egypt that refused the council of Chalcedon. He spent most of his time as patriarch in exile."

- **A-M3 MINOR (items 4, 8).** Names with no context for a listener. l.3 "her man Narses": Narses is a common name, and Liberatus gives his role ("Narses cubicularius", l.81291). l.11 "E. W. Brooks" and "Evetts" appear with nothing to say who they are. l.9 "the formula of Zeno" does not say Zeno was an emperor. Fix: l.3 "her chamberlain Narses"; l.9 "the emperor Zeno's formula uniting the churches"; l.11 "E. W. Brooks, John's translator, puts that in 566. B. Evetts, who translated the History, gives 567." Word room: drop "It counts his patriarchate as thirty-two years." (l.11); the figure stays in the records.

- **A-M4 MINOR (item 1).** Brief l.5 "if he would accept the Tome of Leo and Chalcedon." In the History, Justinian's condition is the Tome alone: "praying him to receive the Tome of Leo, and yield to him on that point" (Evetts l.38469-38470); Renaudot likewise, "ut Theodosius Tomum Leonis susciperet" (l.10046). Theodosius then anathematizes both (l.38589-38590). Fix: given in A-B1 ("if he would accept the Tome of Leo").

- **A-M5 MINOR (records; item 1).** Card `legacy.remembered` 2 (l.30): "Sophronius of Jerusalem and the Lateran council of 649 condemned him." Both are true, but no records claim or card source carries them. Evidence: Sophronius's synodical letter, `john-moschus_pratum-spirituale-sophronius-opera-grc-lat_migne-pg87-3.txt` l.29642-29643, "Theodosius quoque Alexandrinus, Anthimus Trapezuntius, Jacobus Syrus…" in its list of the anathematized; Lateran 649, `mansi_sacrorum-conciliorum-collectio-tomus-10-lat_welter-facsimile1901.txt` l.114428-114430, "Severum, Theodosium, Colluthum, Themistium" among the condemned. Fix: add two records claims with those witnesses, tagged Documented, and add both files to `sources.about`.

- **A-M6 MINOR (item 12; card sources).** `uncertain` cites Michael the Syrian (items 2, 5), Victor of Tunnuna (items 1, 6), R. Payne Smith (item 6) and Jean Garnier (item 6), but `sources.about` lists only Liberatus, John's Lives, the History and Renaudot. Fix: add Michael, Chronique tome 2 (`michael-the-syrian_chronique-tome2-livres-viii-xi-fra_chabot1901.txt`); Victor of Tunnuna, Chronicle (`chronica-minora-2_marcellinus-victor-tunnunensis-biclaro-isidore-mgh-aa-11-lat_mommsen1894.txt`); and John of Ephesus, Ecclesiastical History part 3, tr. R. Payne Smith (`john-of-ephesus_ecclesiastical-history-part3_paynesmith1860.txt`). Garnier is in the Liberatus file already listed.

- **A-M7 MINOR (records).** The claim "Justinian offered him the civil governorship… he refused: 'The prince has no power…'" is tagged Contested, but `contested_claims` has no entry for it, and no held source disputes it. What is weak is that one later partisan history alone tells it; the card says the speech is "the History of the Patriarchs' telling". Fix: retag it Inferential-Thin, with the witness line "History of the Patriarchs only, a later history of his own church (Evetts l.38467-38594)".

- **A-M8 MINOR (item 4).** Card `uncertain` 4 (l.37): "His speeches before the emperor's envoys are the History of the Patriarchs' telling, not a document of his." An "X, not Y" contrast. Fix: "His speeches before the emperor's envoys come only from the History of the Patriarchs."

- **A-M9 MINOR (card ownWords; records).** A fragment of his own words is held and not listed. Jean Garnier's note to Liberatus quotes, from the Lateran council, a tome Theodosius wrote to Theodora: "lomi a Theodosio ad Theodoram Augustam scripti, unde haec decerpta sunt: 'Reliquum est ut una sit operatio ex utrisque deifica…'" (PL 68 l.81419-81428, OCR "lomi", "deilica"). Mansi 10 also cites "tomo Theodosii" (l.111238). The brief's "Two of his letters survive in that chronicle" stays true. Fix: add to `sources.ownWords` "Fragment of his tome to the empress Theodora, cited at the Lateran council of 649, in Jean Garnier's notes to Liberatus (Latin)", file `cic/texts/liberatus-victor-tunnunensis-primasius-junillus-pl68-lat_migne1866.txt`; add a records claim with that witness, Documented.

Not findings. "Severus of Antioch", "Anthimus of Constantinople", "Liberatus of Carthage" and "Jacob Baradaeus" are placed at first mention. "The governorship of Egypt" follows Renaudot's "in Aegypti praefectura" (l.10049). "Pope Theodosius" is John's own form. The two death years are each given with their owner. Liberatus wrote "while Theodosius still lived" is Liberatus's own "vivitque usque nunc".

Length with A-B1 and A-M1 to A-M4 applied (scratch copy): 401 words (2:29), FK 7.2, Flesch 66.1. Remaining sentences past 25 words are quotations.

---

### 2. Jacob Baradaeus (major)

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | minor (A-M10, A-M11, A-M12, A-M13) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | minor (A-M17) |
| 5 | No role for a witness | PASS |
| 6 | Partisan witness named and marked | PASS (John, made bishop by him; Michael, of the same church; Brooks's "hero" on the card) |
| 7 | Contested both sides | minor (A-M14, A-M16) |
| 8 | Common names placed | minor (A-M15) |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | PASS (404 words) |
| 11 | grade_text | PASS (FK 5.9, Flesch 75.9) |
| 12 | Card order, caveat repeated | PASS |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |
| — | Records absence | BLOCKING (A-B3) |

**Quotes and close tellings checked**
- Opening (l.1): Brooks PO 18 l.39657-39666, "those who were pursuing him often met the blessed James himself, and asked him about himself, saying, « Have you heard any secret news ofthat deceiver James anywhere there? », and he on his side would name to them a place no small distance behind him… and, if you set out, perhaps you will catch him." Exact through OCR "ofthat", "110 small". See A-M10, A-M16.
- Tella, Fsiltha, house, cloak (l.3): PO 18 l.39447-39449 ("by his birth from Thella, was trained in the celebrated convent of the monastery called that of Fsiltha"), l.39470-39476 ("she had given them also a house… he would cut one thick and ugly cloak of withes (?) into two, and out of its halves make what was required for his clothing and his scanty covering"); Brooks's note l.39494-39496, "From this attire he got the nickname 'Burd'aya' or 'Burd'ana' (the man of the patchwork garment)". Fifteen years: brooks1923 l.26270-26271, "a period of about fifteen years in these labours in the same royal city in his cell". See A-M11.
- Made bishop (l.5): PO 19 l.10497-10504 and l.10541-10546, "in the sixteenth year of the reign of Justinian… Hereth Bar Gabala, the great king of the Saracens… asked the Christ-loving queen Theodora to give orders that two or three bishops might immediately be instituted… one for Hirtha of the Saracens, that is Theodore, and James for the city of Edessa"; note l.10511, "542". "Harith" is Payne Smith's form (`john-ephesus_ecclesiastical-history-part3_paynesmith1860.txt` l.1120). Faithful.
- Travels (l.7): brooks1923 l.26751-26760 (Syria, Armenia, Cappadocia… Asia, the islands), l.26332-26334 ("in one night perhaps and one day, and would pass the next night thirty or forty miles or more farther on"), l.26397-26398 ("he used to accomplish his travelling on foot"). Count: PO 19 l.10757-10760, "twenty-seven, besides two patriarchs whom the blessed James ordained". Hundred thousand: PO 18 l.39719-39727, "if a man take upon himself to say that a hundred thousand were ordained by him, I do not think he will depart from the truth" (OCR "bim", "tlie"). Faithful; see A-M12 on the gold.
- Paul (l.9): Payne Smith `john-ephesus_…` l.11964-11968, "being, as we have said above, a simple man, he was influenced by the violent persons who surrounded him". Exact. Michael l.25345-25347, "Plusieurs étaient d'accord avec le vieillard Jacques… De là, ils furent appelés Jacobites". Brooks PO 19 l.15652-15653, "This name probably arose out of the schism about the deprivation of Paul of Antioch". Faithful.
- Death (l.11): Payne Smith l.12444-12460 (Cassianus, four dead within twelve days), l.13985-14001 (the ship report, "which of these stories is true, God knows"); Michael l.26331, "Le vieillard Jacques mourut le 30 de tamouz (juillet) de l'an 889"; Brooks PO 19 l.16188, "James d. 30 July, 578". Quote exact. See A-M14.
- Card: Brooks's "hero" (brooks1923 l.275-276), the spurious Life and Kleyn (l.680-684), the colophon (l.724-726), "eighty-seven" (PO 19 l.14954), the pack-saddle variant (PO 19 l.14547), Michael and Bar Hebraeus on Gamoua (Michael l.18407-18410; Bar Hebraeus l.13273-13275), Elias's year 879 (l.5465-5467), "Zanzalus" (Assemani I l.10058), John made bishop of Ephesus (PO 19 l.10708, Brooks's note "The author") all match.

**Findings**

- **A-B3 BLOCKING (false absence; card ownWords).** `records.json`, `absent_details`: "Writings of his own — No letter or treatise by him is held as text." Michael the Syrian gives his reply to the Alexandrians in direct speech: "Jacques répondit aux Alexandrins : « Nous nous disposons à nous rendre près de vous ; et nous ferons ce qui paraîtra bon à toute l'assemblée. »" (Michael tome 2 l.24984-24987). He also reports "des lettres de Jacques et des Orientaux" carried to the emperor by Hereth, with their formula, "La Trinité est une divinité, une nature, une essence" (l.19424-19428). The card has no "Their own words" group as a result. Fix: records `absent_details` note: "No letter or treatise of his survives whole. Michael the Syrian gives one sentence of his reply to the Alexandrians (l.24984-24987) and reports letters of his and the Easterners carried by Hereth (l.19424-19428)." Add a records claim for the reply (witness Michael l.24984-24987, Documented as Michael's report). Add to the card `sources.ownWords`: `{"title": "His reply to the Alexandrians, in Michael the Syrian, Chronique, book X (tr. J.-B. Chabot)", "language": "French translation", "file": "cic/texts/michael-the-syrian_chronique-tome2-livres-viii-xi-fra_chabot1901.txt"}`. No brief change is needed: the brief's own-words line is his reply to the pursuers, as John gives it.

- **A-M10 MINOR (item 1; quantifier).** Brief l.1 "Sometimes they met him on the way" and "John of Ephesus, whom James later made a bishop". John says the pursuers "often met the blessed James" (l.39657). "Later" is not established: the chase went on "for many years, indeed even till after king Justinian's death" (l.39715-39716), and John's ordination at Ephesus came on the second journey to Asia (PO 19 l.10706-10708), with no order given between them. Fix: "Often they met him on the way, and did not know him." and "John of Ephesus, whom James made a bishop, tells the story." (Dropping "in his Lives of the Eastern Saints" gives word room; the card names the work.)

- **A-M11 MINOR (item 1).** Brief l.3 "He cut one thick, ugly cloak in two and wore the halves." John: "out of its halves make what was required for his clothing and his scanty covering" (l.39474-39476); Brooks's note: "he used half for clothing and half for a night-covering" (l.39493-39494). Fix: "He cut one thick, ugly cloak in two and made his clothing from the halves."

- **A-M12 MINOR (item 1).** Brief l.7 "The emperor offered gold to anyone who could catch him." John says the king paid in advance those who promised, and many cheated him: "who gave no small amount of gold to those who promised to capture the blessed man… used consequently to deceive him, and promise and receive gold" (brooks1923 l.26478-26486). Fix: "The emperor paid gold to anyone who promised to catch him."

- **A-M13 MINOR (records; card).** Card `uncertain` 4 (l.29): "Assemani and Hefele 541". Both are held but neither has a records claim or a card source: Assemani, `assemani_bibliotheca-orientalis-tomus1-de-scriptoribus-syris-orthodoxis-lat_1719.txt` l.10058-10063, "Jacobo Baradaeo, seu Zanzalo… quem Episcopatum Edessae anno Christi 541 adeptum fuisse, refert idem Dionysius" (so Assemani gives the year from Dionysius); Hefele, `hefele_history-of-the-councils-v3-431-451_clark1883.txt` l.24187-24190, "consecrated Bishop of Edessa… in the year 541". Fix: add two records claims with those witnesses, Dominant Modern Reconstruction; add both files to `sources.about`; card text: "Brooks makes it 542; Joseph Assemani, after the chronicle he calls Dionysius's, and Hefele make it 541."

- **A-M14 MINOR (item 7).** Brief l.11 "He died on the road to Alexandria, at the monastery of Cassianus on the border of Egypt. John tells two versions of his death…" The place is told as settled before the doubt. One of John's reports has the ship sink with no trace: "their ship sunk, and all perished in the sea, and their corpses were never found" (Payne Smith l.13987-13990). Fix: "He died on the road to Alexandria, at the monastery of Cassianus on the border of Egypt, by John's first account. John also reports a rumour that their ship sank, and says, "which of these stories is true, God knows.""

- **A-M15 MINOR (item 8).** Brief l.9 "a bitter quarrel over Paul, a patriarch he had made." Paul is a common name with no place; Brooks names him "Paul of Antioch" (PO 19 l.15652). Fix: "a bitter quarrel over Paul of Antioch, a patriarch he had made."

- **A-M16 MINOR (item 7; card).** The opening story is a stock one, and the card does not say so. Brooks, note to the passage: "The same story is told of Simeon of Beth Arsham" (PO 18 l.39674, OCR "Sinn' m"). The name of the Jacobites also has more sides held than the card shows: Bar Hebraeus derives it from the priests he multiplied ("eamque ob causam ex ejusdem nomine 'Jacobitae' nuncupati fuere", l.13365-13367; in the records), and Hefele says they took it "out of gratitude to him" (l.24202-24203). Fix: add to card `uncertain`: "The escape from his pursuers. Brooks notes that the same story is told of Simeon of Beth Arsham." and "The name Jacobites. Michael ties it to the quarrel over Paul, and Brooks thinks so too. The spurious Life gives the cry 'We are of the faith of James'. Bar Hebraeus says it came from the priests he multiplied." Move the spurious Life's naming story out of `uncertain` 2 into this item.

- **A-M17 MINOR (item 4; process word).** Card `uncertain` 4 (l.29): "No held source gives a year of birth." "Held" is a process word in participant text. Fix: "The sources give no year of birth."

Not findings. Michael is placed once, as of the same church. John's closeness to Jacob is shown at first mention, and Brooks's "hero" and John's opposite side in 575 are on the card. "Theodore for Hirtha of the Saracens" carries John's place. "Brooks thinks the name arose from that quarrel" keeps Brooks's "probably". Bar Hebraeus's year reads "880" in the OCR (l.14829), but the editors' margin gives "(Chr. 578)" (l.14906), which supports Seleucid 889.

Length with A-M10 to A-M15 applied, and "Brooks gives the year as 542." (l.5) dropped for room (the year stays on the card): 402 words (2:29), FK 6.0, Flesch 75.6.

---

### 3. Longinus, bishop of the Nobadae

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | minor (A-M20) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | minor (A-M21) |
| 5 | No role for a witness | PASS |
| 6 | Partisan witness named and marked | PASS ("Almost all of this comes from John, of his own party.") |
| 7 | Contested both sides | minor (A-M18) |
| 8 | Common names placed | PASS (Theodosius of Alexandria, John of Ephesus, the presbyter Julian, R. Payne Smith with his role) |
| 9 | One term | minor (A-M19) |
| 10 | Story, scene, disputes in place, length | PASS (321 words) |
| 11 | grade_text | PASS (FK 7.1, Flesch 70.3) |
| 12 | Card order, caveat repeated | PASS |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |

**Quotes and close tellings checked** (all in `john-of-ephesus_ecclesiastical-history-part3_paynesmith1860.txt` unless named)
- Escape (l.1): l.13004-13012, "three years passed by… as he was aware that he was watched… he disguised himself, and put a wig on his head,—for he was very bald ;—and taking with him two servants, he fled". Exact, including the file's " ;".
- Who-line (l.3): l.12755-12757 ("the wandering people who dwell on the eastern borders of the Thebais beyond Egypt"); l.12976-12982 ("her late majesty, the queen Theodora, had given orders that the excellent Longinus should be made bishop there… Immediately therefore after the pope's decease, Longinus was consecrated"). Faithful; see A-M18.
- Work and envoy (l.5): l.13018-13021 ("built them a church, and ordained clergy, and taught them the order of divine service"); l.13030-13036 ("honourably received in the presence of myself and the rest of the court, and spake highly of Longinus, saying, 'Though we were Christians in name, yet we did not really know what Christianity was until Longinus came to us"). Exact.
- Alexandria and the Alodaei (l.7): l.13049-13059 ("five years, more or less… to consecrate for them a pope"); l.15393-15397 ("another powerful tribe many score leagues beyond them, whom the Greeks call Alodaei"); l.15498-15502 (the act of deposition); l.15592-15594 ("we will receive him who baptized the Nobadæ, and by him will we be baptized"). Exact.
- Letter (l.9): l.15764-15765 ("so that we lost no less than seventeen camels"), l.15780-15782 ("the king hearing of our coming rejoiced, and came out in person to meet us, and received us with great joy"), l.15783-15784 (baptism of "him and his nobles"), l.15826-15827 ("For I desire neither silver, nor gold, nor dresses, as God is my witness"); John, l.15832-15833, "This then was written by the holy Longinus himself". Exact; see A-M20.
- Date (l.11): l.15943-15944, "in the year 891 (A. D. 580)"; the bracket is Payne Smith's, as the brief says.
- Card: the Alodaei king's "my father, the holy father Longinus" (l.15707-15709), the six years (l.15481), Michael's Theodosius order (Michael l.20413-20415), the chapter heading (`john-ephesus_…` l.1050-1054), Hirah (l.14216, "Longinus went to Hirah"; Michael l.25362-25363), and Payne Smith's bridge (l.12735-12746, his own paragraph after "The loss of most of the first five chapters", l.12722) all match.
- Absences checked: his origin, age and death, and any event after 891. I searched both Payne Smith files, both Michael volumes (Longinus at l.20413-20418, 23561-23563, 25349-25377, 26888-26899, all before or at 891), the Arabic and Ethiopic synaxaries (their Longinus entries are other men) and Crum's ostraca (Longinus of the Enaton, another man). The brief's "No source tells of Longinus after that, or of his death" holds.

**Findings**

- **A-M18 MINOR (item 7).** Brief l.3 "The empress Theodora had ordered that he be made their bishop, John says." John's own chapter heading says Theodosius "commanded that Longinus should be immediately made" bishop (`john-ephesus_…` l.1050-1052), and Michael agrees ("il ordonna que Longinus fût leur évêque", l.20414). The card and records carry both sides; the brief gives one. Fix, replacing the two sentences: "He was consecrated as soon as the patriarch Theodosius of Alexandria died. John says the empress Theodora had ordered it; his chapter heading says Theodosius did."

- **A-M19 MINOR (item 9).** The brief names the party "the party that refused the council of Chalcedon" (l.3), then "the anti-Chalcedonians" (l.7). It names the people "the Nobadae" (l.3, 5) and then the land "Nubia" (l.7), never introduced. Fix, l.7: "to help make a patriarch for his party at Alexandria" and "Back among the Nobadae, he went on to the Alodaei".

- **A-M20 MINOR (item 1; witness swap).** Brief l.9 "On the road through the desert, Longinus says, they all fell ill". Longinus's letter speaks of "the heat, and the thirst in the mountains" (l.15762-15763). "The desert" is John's own narrative ("he lost in the desert no less than seventeen camels", l.15619-15620). Fix: "On the road, Longinus says, they all fell ill".

- **A-M21 MINOR (item 4; process word).** Card `uncertain` 5 (l.33): "No held source gives his origin, his age or his death." Fix: "The sources give nothing of his origin, his age or his death."

Not findings. "In the presence of myself" is John's own claim to have heard the envoy, and the brief gives it as his. John's partisanship is stated in the brief and opens the card's `uncertain`. "Theodosius of Alexandria" is placed at first mention. The closing honest limit names what is missing and does not end on a bare how or why.

Length with A-M18 to A-M20 applied: 320 words (1:59), FK 7.1, Flesch 70.2.

---

Totals, part A: 3 blocking (A-B1, A-B2, A-B3) and 21 minor (A-M1 to A-M21). Theodosius 2 and 9, Jacob 1 and 8, Longinus 0 and 4.

## Part B

Reviewer: independent, first sight of these drafts. Bar: `Who_Profile_Pattern.md` review checklist 1 to 14 and the standards it points to; `CLAUDE.md` "Trust and source fidelity" and "Accessible and rigorous"; the batch rulings in the brief (majors capped at 2:30, about 405 words; non-majors 1 to 2 minutes, at most about 325 words; outside witness Tradition line "Outside the church"; Cassiodorus major; John of Ephesus a recorder at standard length; Agathias carries the Outside witness label). I did not edit any repo file, made no paid or model-API calls and used no web.

Profiles: `john-of-ephesus`, `victor-of-tunnuna`, `cassiodorus` (major), `agathias` (Outside witness), with their cards, audio scripts and `records.json` entries, in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era3/batch4/`. Brief line numbers refer to the `.brief.txt` files (one paragraph per line, blank lines counted: l.1, 3, 5 ...). Card line numbers refer to the `.card.json` files as they stand. Other line numbers point to files under `cic/texts/`.

Method. I read every cited passage by line number in the vendored file, for the OCR files (Brooks's Lives in PO 17 and PO 19 and the combined file, Payne Smith's Church History, Chabot's Michael the Syrian tome 2, Mommsen's Chronica minora II, Migne PL 68, PL 70, PL 83, PG 88) reading each in context to see who speaks: the ancient author, a translator's preface, a footnote or an editor's margin. I followed editors' footnotes back to their sources where the Library holds them (this is how J-B1 was found: Brooks's note for the Chalcedon prison cites "Mich., p. 364", and the held Michael carries it under the page marker [364]). Before accepting each absence claim I searched the held files that name the person (`grep -il` with OCR-tolerant forms: Tunnun/Tonnen/Tunun/Tunnens; Jean d'Asie/d'Amid; Cassiodor; Agathi). Readability came from `engine.m1.gates.grade_text`, run from the repo root. Every suggested brief fix below was applied to a scratch copy and re-scored; the post-fix word count and scores are given with each profile.

### Applies to all four

- **Audio = brief.** Each audio script matches its brief exactly once `[calmly] ` and `[warmly] ` are removed (checked by script). Each starts with `[calmly]` and has one `[warmly]`, at the start of the closing paragraph. No tag appears in any brief or card. When a brief fix below changes a line, the audio script follows it.
- **Readability.** All four pass. Victor of Tunnuna sits on the Flesch floor (60.6); any change to it must be re-scored (see V-M2).
- **Length.** John of Ephesus 326 words, Victor 326 and Agathias 328, each a hair over the "about 325" non-major ceiling; the fixes below bring all three under it. Cassiodorus 403 (2:29), under the 405 cap. Every `briefLength` matches.
- **Card order.** All four follow Mark's order; missing fields are left out; keyWorks never past three; Agathias's `label` sits before `knownFor` as on earlier outside-witness cards, and his Tradition line reads "Outside the church".
- **Who test (item 14).** John of Ephesus and Victor are recorders whose works are main sources for their churches' side of the sixth-century quarrels. Cassiodorus has a body of work and a foundation. Agathias is a historian, never a polemicist; Niebuhr holds that he professed Christianity, and the card's `uncertain` 1 says plainly that the label makes no claim about his faith, which handles the tension honestly (not a finding; the label is the coordinator's ruling). List lines belong to the map build and were not checked here.
- **Process words in cards.** Three cards use "held" in the Library sense in participant text (J-B1, C-M6, G-M5). The prison sense of "held" in Victor's card is ordinary English and is not a finding.

| Profile | Words | Est. @162 | FK | Flesch |
|---|---|---|---|---|
| John of Ephesus | 326 | 2:01 | 6.2 | 73.6 |
| Victor of Tunnuna | 326 | 2:01 | 8.0 | 60.6 |
| Cassiodorus (major) | 403 | 2:29 | 6.8 | 73.7 |
| Agathias of Myrina (Outside witness) | 328 | 2:01 | 6.3 | 72.9 |

---

### 1. John of Ephesus

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | minor (B-M1, B-M6) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS |
| 5 | No role for a witness | PASS (Brooks, Payne Smith, Michael, Chabot named) |
| 6 | Partisan witness named and marked | PASS (his party named in brief l.3 and card `uncertain` 1) |
| 7 | Contested both sides | BLOCKING (B-B1); minor (B-M2, B-M3, B-M4) |
| 8 | Common names placed | minor (B-M1 subject's own name; B-M5 card) |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | PASS (326 words; see B-M2 fix) |
| 11 | grade_text | PASS |
| 12 | Card order, caveat repeated | PASS |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS (recorder) |

**Quotes and close tellings**
- Maro (l.1): `john-ephesus_lives-eastern-saints-po17_brooks1923.txt` l.4146-4157: "every son who was born to them used to die at the end of a year and a half or two years… as my parents used to tell me, they immediately repaired to the holy Maro, carrying me and weeping… « Be quiet, be quiet. John shall not die before Maro »". Quote exact. "Lived on a pillar": Brooks l.247, "the monastery of the stylite Maro". See B-M1 on the age.
- Birth (l.3): Brooks l.243-249, "born about 507 in the territory of Ingila… united with the province of Mesopotamia of which the capital was Amida… placed in the neighbouring monastery of the stylite Maro… after Maro's death, he moved to the monastery founded by John Urtaya at Amida". Faithful.
- Mission (l.5): `john-ephesus_ecclesiastical-history-part3_paynesmith1860.txt` l.10119-10160 (margin III.36, John's own words): "appointed teacher of the heathen in Justinian's time in the four provinces of Asia, Caria, Phrygia, and Lydia… in the territory of which city alone he converted many thousands… built… twenty-four churches, and four monasteries… at a village called Derira… having levelled it to its very foundations, he built this chief monastery". Faithful. Brooks's condition, PO 17 l.308-310, "on condition that he should convert them to the Chalcedonian faith". Faithful, and credited to Brooks.
- Bishop (l.7): PO 19 l.10706-10708, "they ordained four bishops in Asia, one in Ephesus a man whose name was John the Syrian, the converter of the pagans", Brooks's note "The author" (l.10714). Brooks l.323-325, "There is nothing to show that he ever resided at Ephesus; and after the death of the patriarch Theodosius in 566 he became the acknowledged head of the Monophysites in Constantinople". Faithful.
- Prison quote (l.7): Payne Smith l.4913-4987 (margin II.4), "the hospital of Eubulus, in which, after his two former imprisonments in the patriarch's palace… 'Even though you eat me roasted, if I be but quit of the sight of you, I am ready on these terms to be delivered to a painful death'". Exact through OCR line breaks. "Jailed more than once" holds.
- Eyewitness (l.9): Brooks l.1044-1050 (OCR), "except those of whom I have been an eye-witness… I will in no case commit any… to the memorial of my handwriting". Faithful.
- Payne Smith's joins (l.9): l.253-257, "I have endeavoured to connect the various facts by inserting a few lines here and there… I have marked where the author's own words begin". Faithful.
- Brooks's judgments (l.9): l.732 "John is not a literary writer"; l.771 "His chronological statements are aften [often] loose or even wild"; l.761 "he shows little interest in theology" (card). Exact through OCR "aften".
- Close (l.11): Brooks l.359-360, "His history ends in 585, and he probably died in 586 after a year spent in prison at Chalcedon"; Payne Smith l.105-108, "as the author was resident at Constantinople, and a busy actor in the scenes which he describes". Quote exact.
- Card: "Born… R. Payne Smith gives about 516" (Payne Smith l.148-151, "born at Amid… probably about A. D. 516", from Assemani's extracts). Michael's "quarante ans auparavant, Jean d'Amid, lui-même, avait été créé évêque à Éphèse, par le vénérable Jacques" (`michael-the-syrian_chronique-tome2-livres-viii-xi-fra_chabot1901.txt` l.25319-25321). The 70,000 (l.20711) and Chabot's note "Ainsi d'après le Ps.-D. ; ms. : 7 mille" (l.20722-20723). Brooks's "his hero James" (l.356-357). Brooks's chronology on Dyakonov (l.238-239). All faithful, but see B-M3 and B-M4.

**Findings**
- **B-B1 BLOCKING (items 1, 7; false absence).** Card `uncertain` 6 (l.40): "Brooks says he probably died in 586 after a year in prison at Chalcedon. No ancient source for that prison is held." `records.json` `absent_details` 2: "Brooks alone gives the year in prison at Chalcedon; no ancient source for it is held." Brooks's own footnote for that sentence cites "Mich., p. 364" (PO 17 l.400, note 3, for the sentence at l.359-360), and the held Michael carries it under the page marker [364] (OCR "[3641", l.26271): "Ils s'emparèrent de l'évèque Jean, qui était gardé en prison à Chalcédoine depuis un an… « …tel jour, malgré vous je serai délivré. » Et il mourut au jour qu'il avait indiqué. Il fut enseveli en grande pompe" (l.26282-26303). Chabot's note 4 says the passage is probably a summary of John's own lost chapters (l.26296-26297). The card is one of the sources Michael is already listed in. Michael says "the bishop John" without "of Ephesus", so the identification is Brooks's. Fix, card `uncertain` 6: "His death. Brooks says he probably died in 586 after a year in prison at Chalcedon. His source is Michael the Syrian, who tells of 'the bishop John', held a year in prison at Chalcedon, who died on the day he had foretold." In `records.json`, delete that `absent_details` entry and add a claim: `{"claim": "The bishop John, held in prison at Chalcedon for a year, refused communion and died on the day he had foretold", "witness": "Michael the Syrian, tr. Chabot (l.26282-26303), probably summarising John's lost chapters (Chabot's note, l.26296-26297); Brooks's source for 586 (PO17 l.359-360, note l.400)", "formation_confidence": "Inferential-Thin"}`. No brief change is needed.
- **B-M1 MINOR (items 1, 8).** Brief l.1: "Every son born to his parents had died before the age of two. When John fell ill too…". John says they died "at the end of a year and a half or two years" (PO 17 l.4146-4147), so "before the age of two" is a little off. The subject is also first named as "John" and gets his identifier only in the fourth sentence. Fix: "Every son born to the parents of John of Ephesus had died by the age of two. When John fell ill too…", and in the last sentence of l.1, "John tells this himself, as his parents used to tell it to him, in his Lives of the Eastern Saints."
- **B-M2 MINOR (item 7).** Brief l.3 gives Brooks's birth (about 507, near Amida) and leaves out the other side. Payne Smith, from the extracts in Assemani, gives Amid, "probably about A. D. 516" (Payne Smith l.148-151). The card and `contested_claims` 1 give both sides; the brief gives one, though it names its witness. Fix, add after "…and grew up in monasteries there.": "R. Payne Smith, who put his Church History into English, gives about 516." and shorten l.9 to "Payne Smith joined the History's broken pieces with lines of his own, he says." To stay under the ceiling, cut l.5 "He levelled a great pagan temple at Derira and built a monastery in its place." (The card keeps it in `legacy.traces` 1.)
- **B-M3 MINOR (item 7).** Card `uncertain` 1 (l.35): "In the quarrel of 575 he stood apart from the side of Jacob Baradaeus, whom Brooks calls his hero." This is Brooks's reading ("the division… eventually led to a schism (575) in which John is found on the opposite side to his hero James", PO 17 l.355-357), told as fact. The held Michael gives the other side: "Quand il vit que des motifs futiles et les passions humaines excitaient les partisans de Jacques contre Paulus, il ne se sépara point d'eux; mais il avertit et blâma les deux partis" (l.25322-25325), after quoting John: "Nous nous abstiendrons d'innocenter un parti et de couvrir l'autre de blâme" (l.25318-25319). Fix, second sentence: "In the quarrel of 575, Brooks places him on the side opposed to Jacob Baradaeus, whom Brooks calls his hero. Michael the Syrian says he did not break with Jacob's party but rebuked both sides." Add a `contested_claims` entry: `{"claim": "Where John stood in the schism of 575", "sides": "Brooks: on the side opposed to James (PO17 l.355-357). Michael: he did not separate from James's partisans but rebuked both parties (Michael l.25318-25325)."}`.
- **B-M4 MINOR (item 7).** Card `uncertain` 4 (l.38) and `contested_claims` 2 give the converts as "many thousands" (John), 70,000 (Michael, Chabot's reading) and 70,000 in four years (Payne Smith). The same Michael passage gives a third figure: "Jean d'Amid, qui fut appelé « d'Asie », parce qu'il avait baptisé plus tard en Asie, vingt-trois mille (païens)" (l.20769-20772). Fix, append to `uncertain` 4: "In the same chapter Michael also says he later baptised twenty-three thousand in Asia." Add the figure to `contested_claims` 2. Chabot's 70,000 is a reading taken from the so-called Dionysius ("d'après le Ps.-D.", l.20722); "correction" may stay.
- **B-M5 MINOR (item 8).** Card `legacy.traces` 2 (l.27): "Theodora's refugees". Theodora is a common name, and this is the card's first and only mention. Fix: "the empress Theodora's refugees".
- **B-M6 MINOR (item 1).** Brief l.11: "His history ends in 585. Brooks thinks he probably died the next year." The 585 is Brooks's figure in the same sentence as the death (PO 17 l.359). The card says so (`keyWorks` 2, "by Brooks's account"); the brief does not. Fix: "His history ends in 585, Brooks says, and he probably died the next year."

Not findings. "Brooks says the emperor set one condition" is credited to Brooks; his note cites Michael and the Revue de l'Orient chrétien, which I could not match to a held line, and the brief claims no more than Brooks says. "Country around Amida" is a fair short form of Brooks's "territory of Ingila… united… with… Mesopotamia of which the capital was Amida". The 37-word sentence at l.7 is mostly John's quoted words; the narrator's part is short.

Length with B-M1, B-M2 (with its cut) and B-M6: 320 words (1:59), FK 6.2, Flesch 74.2.

---

### 2. Victor of Tunnuna

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | minor (B-M9, B-M10, B-M11, B-M12) |
| 2 | Quotes verbatim | PASS (Latin told in modern words; no English is held, and the records say so) |
| 3 | No invention | PASS |
| 4 | Reading aids | minor (B-M7) |
| 5 | No role for a witness | PASS (Mommsen, Isidore, Gallandi, Mesnage named) |
| 6 | Partisan witness named and marked | PASS ("Victor writes as a partisan", l.11); see B-M9 |
| 7 | Contested both sides | minor (B-M11) |
| 8 | Common names placed | minor (B-M8) |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | minor (B-M7 opening) |
| 11 | grade_text | PASS (Flesch 60.6, at the floor) |
| 12 | Card order, caveat repeated | PASS ("He writes as a partisan" opens `uncertain`) |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS (recorder) |

**Quotes and close tellings** (`chronica-minora-2_marcellinus-victor-tunnunensis-biclaro-isidore-mgh-aa-11-lat_mommsen1894.txt`)
- Exile (l.1): l.19187-19198, "555 POST CONSVLATVM BASILI V. C. ANNO XV… Victor Tunnennensis ecclesiae episcopus huius auctor operis post custodias simulque et plagas, quas in insulis est Balearicis perpessus nec non etiam in monasterio de Mandracio primo, ac secundo exilio Aegimuritanae insulae, tertio Alexandriam una cum Theodoro Cebarsusitanae ecclesiae episcopo… et carceri castelli Diocletiani post praetorianum carcerem truditur"; apparatus l.19236, "in insulis est balearicis] scripsi, in sala est ualericis VP(ES)". The brief leaves out the disputed first place and the card tells it (`uncertain` 4). Faithful. Migne PL 68 l.74762-74770 agrees ("quas Sala et Valericis perpessus").
- Town (l.3): l.17264-17265, "Oppidum, cuius sedem tenuit, quomodo vere appellandum sit, parum constat"; l.17299-17300, "fuisse in provincia proconsulari fortasse non longe a Carthagine magna". Faithful.
- Vigilius (l.5): l.19047-19049, "Africani antistites Vigilium Romanum episcopum damnatorem trium capitulorum synodaliter a catholica communione reservato ei paenitentiae loco secludunt". Justinian's condemnation: Mommsen l.17306-17308. Faithful.
- Canopus and Constantinople (l.7): l.19202-19204 ("post disputationes in praetorio continuas dierum XV… monasterii Tabennesiotarum, quod est apud Canopum XII milibus procul ab urbe Alexandrina"); l.19304-19310 ("Victor ac Theodorus… ad urbem regiam imperiali praecepto evocantur… Iustiniano principi praesentes et postea Eutychio regiae urbis episcopo altercanti novae superstitioni resistunt, ab invicem segregati per monasteria eiusdem urbis custodiae mittuntur"); l.19349-19354, Theodore "eo mense et die quo Iustinianus moritur". Migne's punctuation (PL 68 l.74905-74908, "quo Justinianus, moritur ;") makes "moritur" Theodore's verb. Faithful.
- Isidore (l.9, 13, 15): `isidore-seville_sententiae-eccl-officiis-historia-gothorum-pl83-lat_migne1860.txt` l.122566-122582, "a principio mundi usque ad primum Justini Junioris imperii annum… memoria dignissimam… in monasterio ejusdem civitatis custodiendus mittitur, atque in eadem damnatione (ut dicunt) permanens, moritur". Faithful.
- Theodora and Mommsen (l.11): l.19041-19042, "Theodora Augusta Calchedonensis synodi inimica canceris plaga corpore toto perfusa"; l.17574-17576, "acerrimi orthodoxae fidei defensores et impugnatores omnium eorum, qui a Calchedonensi synodo plus minus recederent". "Fierce defenders of Chalcedon" is a fair short form. See B-M9.
- Mesnage (l.15): `mesnage_afrique-chretienne-eveches-ruines-fra_1912.txt` l.14675-14677, "très précieuse pour l'histoire religieuse de l'Afrique au vie siècle". Faithful.
- Absence of a death year (l.13): searched the Library; Isidore alone gives the death and no year. The modern years are on the card (see B-M11).

**Findings**
- **B-M7 MINOR (items 4, 10).** Brief l.1 opens: "In his own chronicle, Victor of Tunnuna names himself as the author of this work." "This work" has nothing to point to in the brief (it renders Victor's "huius auctor operis"), and the sentence delays the scene. Fix: "Victor of Tunnuna wrote a chronicle. In it he tells how he was kept under guard and beaten, first in a monastery at Mandracium, then on the island of Aegimurus."
- **B-M8 MINOR (item 8).** Brief l.1: "with Theodore, another African bishop". Theodore is a common name, and Victor gives his see: "Theodoro Cebarsusitanae ecclesiae episcopo" (l.19194-19195). Fix: "with Theodore, bishop of Cebarsussi in Africa".
- **B-M9 MINOR (items 1, 6).** Card `uncertain` 1 (l.31): "Theodor Mommsen calls him and his fellow African Liberatus fierce defenders of Chalcedon, embittered against Vigilius." It is offered as a mark of partisanship, but Mommsen calls the bitterness just: "iusto odio exacerbati in Vigilium inter malos pontifices Romanos fortasse pessimum" (l.17577-17578). Cut that way, Mommsen seems to say something he does not. Fix: "Theodor Mommsen calls him and his fellow African Liberatus fierce defenders of Chalcedon, embittered against Vigilius by a hatred Mommsen thinks just."
- **B-M10 MINOR (item 1).** Card `uncertain` 5 (l.35): "Cardinal Noris, as Andrea Gallandi quotes him, trusts his facts but finds his years full of errors." The held notice names him only "Noris"; "Cardinal" is not in the file. Noris also lays the errors on a corrupter, not on Victor: "ejus Chronicon plenum mendis est, non Victoris, ut arbitror, sed corruptoris cujuspiam ignorantia" (PL 68 l.73053-73057). Fix: "Noris, as Andrea Gallandi quotes him, trusts his facts but finds the years in the chronicle full of errors, which he blames on a later copyist."
- **B-M11 MINOR (item 7).** Card `dates` (l.9) and `uncertain` 6 (l.36) give one modern year for the death, Gallandi's "shortly after 566". `contested_claims` 2 also holds Hodgkin, "Victor Tunnunensis, chronicler (died in 569)" (`cassiodorus_variae-letters-hodgkin1886.txt` l.25466), and Kugener, "Victor mourut vers l'an 569 dans un couvent de Constantinople" (`zacharias-scholasticus_vie-de-severe-po2-syr-fra_kugener1903.txt` l.26975). Fix, `uncertain` 6, last sentence: "No early source gives a year. Gallandi thinks shortly after 566; Thomas Hodgkin and M.-A. Kugener give about 569."
- **B-M12 MINOR (item 1).** Card `knownFor` (l.8): "wrote a Latin chronicle from his exile". Mommsen says only that he seems to have: "exul videtur chronica dictavisse" (l.17312-17313). Card `dates`: "Justinian, who died in 565", while `uncertain` 5 says every year is Mommsen's and Mommsen's margin numbers Justinian's death "567?" (l.19347). His introduction has the narrative reach 565 (l.17313). Fix, `knownFor`: "…and wrote a Latin chronicle, in exile as Mommsen thinks." `dates`: "…in the last years of Justinian, who died in 565 by Mommsen's introduction."

Length with B-M7 and B-M8: 321 words (1:59), FK 8.0, Flesch 60.6. Opening variants that ran the first two sentences together fell below Flesch 60; the wording above holds the floor.

---

### 3. Cassiodorus (major)

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | minor (B-M13, B-M14) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | minor (B-M15, B-M20) |
| 5 | No role for a witness | PASS (Hodgkin, Mommsen, Jordanes, Trithemius, Williams, Paul the Deacon named) |
| 6 | Partisan witness named and marked | PASS (card `uncertain` 5, letters in the king's name praising himself) |
| 7 | Contested both sides | minor (B-M17, B-M19) |
| 8 | Common names placed | minor (B-M16) |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | PASS (403 words, 2:29) |
| 11 | grade_text | PASS |
| 12 | Card order, caveat repeated | PASS |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |

**Quotes and close tellings**
- Spelling (l.1): `cassiodorus_variae-letters-hodgkin1886.txt` l.3489-3498, "in the ninety-third year of his age… He tells us that the monks suddenly exclaimed, 'What doth it profit us to study either those works which the ancients have composed or those which your Wisdom has caused to be added to the list, if we are altogether ignorant how we ought to write these things'". Latin, `cassiodorus_opera-institutiones-pl70-lat_migne1847.txt` l.91802-91804 (OCR, "no ;elaii$ me.e noiiap-es ino lerlio"). Faithful.
- Name (l.3): Hodgkin l.1247-1249, "Senator, it is clear, was part of the original name of Cassiodorus, and not a title"; Mommsen, Chronica minora II l.9267-9269, "Cassiodori vocabulum pro signo eum habuisse et proprio nomine Senatorem… appellari". Faithful; see B-M15.
- Anecdoton (l.3): Hodgkin l.3747-3752, "Juvenis adeo… laudes Theodorichi regis Gothorum facundissime recitasset, ab eo Quaestor est factus. Patricius et Consul Ordinarius, postmodum dehinc Magister Officiorum". Faithful; see B-M13 on its date.
- Consulship (l.3): Chronica minora II l.16040-16044, "Senator v. c. cons. Me etiam consule… adunato clero vel populo Romanae ecclesiae rediit optata concordia". Faithful.
- Variae (l.5): Hodgkin l.6231-6232, "The author is told to keep his writings by him for nine years for reflection; but I have not as many hours, hardly as many moments." Quote exact. Twelve books, l.6385-6388.
- Jordanes (l.5): `jordanes_origin-and-deeds-of-the-goths_mierow1908.txt` l.121-135, "condense… the twelve volumes of the Senator… I have in times past read the books a second time by his steward's loan for a three days' reading". Faithful.
- School (l.7): Institutions preface, Hodgkin note l.3151-3157 and PL 70 l.81295-81310, "Nisus sum ergo cum beatissimo Agapeto papa… collatis expensis… professos doctores… per bella ferventia et turbulenta nimis in Italico regno certamina". Faithful. Scyllacium and Vivarium: Hodgkin l.3076-3086, "his ancestral Scyllacium… one for the austere hermit… Mons Castellius… the Vivaria (fish-ponds)". Faithful.
- Copyist (l.9): Hodgkin l.3196-3199, "With his fingers he gives life to men and arms them against the wiles of the devil." Exact. Benedict and the abbacy: Hodgkin l.3097-3101 and l.3125-3128. Faithful; see B-M14 on the lamps.
- Years (l.11): Hodgkin l.1388-1393, "a very late and somewhat unsatisfactory source. John Trittheim (or Trithemius)… who died in 1516"; l.1474-1476 (480); l.3542-3546 ("as I believe… 575"). Absence holds: no held ancient line gives either year (searched).
- Close (l.13): Hodgkin l.1077-1080. Exact; it ends where Hodgkin's sentence goes on with "however unworthy", which the card keeps.
- Card: Alcuin, "Cassiodorus item, Chrysostomus atque Joannes" (`alcuin_opera-omnia-letters_migne-pl100-101_1863.txt` l.67435); Paul the Deacon, "He was in the first place a consul, then a senator, and at last a monk" (`paul-the-deacon_history-of-the-langobards_foulke1907.txt` l.3234-3235); Williams, "Cassiodorus, who died a.d. 570" (`gildas_de-excidio-britanniae-lorica-penitential-lat-eng_williams1899.txt` l.286); the Psalms "conversionis meae tempore" (PL 70 l.91761-91762). All faithful.

**Findings**
- **B-M13 MINOR (item 1; an editor's date told as settled).** Brief l.3: "A fragment from his own century says that as a young man he spoke the praises of King Theoderic…". Hodgkin does not date the fragment to the sixth century. He says it is an excerpt from "a short tract by Cassiodorus on the literary history of his family", that "the 'Excerpta' have been made by some later hand–perhaps that of a monk in the Vivarian convent", and that "the fragment cannot consist of the very words of Cassiodorus" (l.3757-3770). It survives on the last page of a tenth-century copy (l.3700-3707), and Hodgkin calls it valuable "if genuine" (l.3681). Fix (with B-M16): "A fragment drawn from a lost tract of his own, Hodgkin says, tells how he praised Theoderic, king of the Goths. He spoke so well that the king made him quaestor."
- **B-M14 MINOR (item 1).** Brief l.9: "He gave them lamps that seem to have trimmed themselves, with sundials and water-clocks." The "seem" is Hodgkin's guess at the mechanism ("which appears to have made them self-trimming", l.3233-3235), told here without its owner. Cassiodorus says the lamps feed their own flame ("mechanicas lucernas, conservatrices illuminantium flammarum, ipsas sibi nutrientes incendium", PL 70 l.84039-84045). He names one sundial and one water-clock ("horologium vobis unum quod solis claritas indicet… alterum vero aquatile", l.84056-84060). Card `legacy.traces` 1 (l.30) gives Hodgkin's "self-trimming" as Cassiodorus's description. Fix, brief: "He made them lamps that fed their own flame, with a sundial and a water-clock." Card: "…and made them lamps that fed their own flame, a sundial and a water-clock for the work, as he describes in the Institutions."
- **B-M15 MINOR (item 4, "X, not Y").** Brief l.3: "Senator was part of his own name, Hodgkin and Theodor Mommsen say, not a title." This is narrator prose. The dispute with Paul the Deacon is the card's (`uncertain` 2). Fix: "Hodgkin and Theodor Mommsen say Senator was part of his own name."
- **B-M16 MINOR (item 8).** Brief l.3, "King Theoderic", and brief l.9, "no mention of Benedict". Both names are shared by others, and the held Hodgkin gives "the Ostrogothic King Theodoric" (l.1091) and "Benedict was born in Nursia" (l.15797). Card `uncertain` 3 (l.42) has the card's first and only "Benedict". Fix: brief l.3 as in B-M13 ("Theoderic, king of the Goths"); brief l.9, "Hodgkin finds no mention of Benedict of Nursia in all his writings…"; card `uncertain` 3, "Benedict of Nursia".
- **B-M17 MINOR (item 7).** Card `uncertain` 3 (l.42): "Hodgkin thinks he never formally held the office, against Trithemius." Hodgkin is more open than that: Trithemius's "abbas electus est" "_may_ preserve a genuine and accurate tradition". The two named abbots show only that "at any rate in the infancy of his monasteries he was not Abbot of either of them" (l.3141-3147). Fix: "Hodgkin thinks he probably never formally held the office, though he allows that Trithemius, who says he was elected abbot, may preserve a true tradition."
- **B-M18 MINOR (item 4, process word).** Card `uncertain` 3 (l.42): "Garet's argument on his monastic life is not held." This is a Library status line in participant text. Fix: delete the sentence. The `absent_details` entry keeps it.
- **B-M19 MINOR (items 7, 12).** Card `uncertain` 1 (l.40) gives Hodgkin's 575 and Williams's 570 for the death. It leaves out the third side in `contested_claims` 1, Strauch's "Cassiodori Senatoris († 563)" (`langmann_offenbarungen-gmh_strauch1878.txt` l.22202). Fix: "Hugh Williams gives his death as 570, and Philipp Strauch as 563." The first name is in the file's header (l.1-2).
- **B-M20 MINOR (item 4).** Brief l.1, 28 words ("What good was it, they asked… if they did not know how to spell what they read?"), and brief l.3, 27 words (the Anecdoton sentence), are narrator sentences past about 25 words. Fix, l.1: "What good was it, they asked, to study the old books and the ones he had added? They did not know how to spell what they read." l.3 is fixed by B-M13. To stay at the cap, also change l.1 "tells the scene" to "tells it". (The l.5 Variae sentence is 26 words only because it carries the quote.)

Length with B-M13 to B-M16 and B-M20: 405 words (2:30), FK 6.1, Flesch 76.3. That is at the cap.

---

### 4. Agathias of Myrina (Outside witness)

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | minor (B-M21, B-M22, B-M23, B-M24) |
| 2 | Quotes verbatim | PASS (brief tells the Latin in modern words and says so); card minor (B-M23) |
| 3 | No invention | PASS |
| 4 | Reading aids | minor (B-M25) |
| 5 | No role for a witness | PASS (Niebuhr, Vossius, Evagrius, John of Nikiu named) |
| 6 | Partisan witness named and marked | PASS (no partisan witness; Niebuhr's judgments are his own) |
| 7 | Contested both sides | PASS (his faith: Vossius and Niebuhr, l.7) |
| 8 | Common names placed | PASS (Procopius of Caesarea, Evagrius Scholasticus; "the martyr Stephen") |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | PASS (328 words; under 325 with B-M22) |
| 11 | grade_text | PASS |
| 12 | Card order, caveat repeated | PASS (label placed; "Outside the church") |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS (an objective historian; the label is the coordinator's ruling) |

**Quotes and close tellings** (`dorotheus-gaza_doctrinae-barsanuphius-climacus-agathias-grc-lat_migne-pg88.txt`, Latin version)
- Earthquake (l.1): l.116351-116365, "[Byzan]tii ingens terrae motus fuit… Cum enim illius anni autumnus iam esset exactus… frigus erat… sole ad brumales conversiones"; l.116925-116959, "Nonnulli vero… solitariam quamdam et montanam vitam sunt amplexi… noctu lautiores opulentioresque cives plateas obeuntes, largo cibo et vestibus donabant egenos… Simul ac vero malum remitti ac cessare coepit, confestim plerique ad pristinos mores redierunt… Bona itaque opera, ita demum necessitate cogente, degustamus, quandiu metus premit." Faithful except B-M21.
- Name (l.3): l.94967-94969, "Nomen itaque mihi Agathias, Myrina patria; Memnonius pater; ars vero Romanorum instituta ac leges et fori certamina… quae est in Asia". Niebuhr's Life (its author is the editor who wrote the preface: "De Rehdigerano et Lugdunensi, quibus usus sum, dixi", l.94221; "supra in Praefatione indicavi", l.94362), l.94020-94032, "Alexandriae studuit… ut causas ante tribunalia oraret: idque Constantinopoli… ac necessitate coactus, ut victum sibi quaereret". Turn to history, l.94850-94886, "ne omnis vita mihi in fabularum studia… consumeretur, sed aliquid etiam utilitatis publico afferret". Faithful.
- Evagrius (l.5): `evagrius-scholasticus_ecclesiastical-history_walford1846.txt` l.11142-11146, "continued by Agathias the rhetorician, and John, my fellow-citizen and kinsman". Faithful; see B-M22.
- Dome (l.5): l.117349-117373, "Per hanc enim hiemem… mediam vero ipsius tecti partem collapsam… imperator firmiorem reddidit, et in majorem altitudinem sustulit". Faithful.
- Franks and Alamanni (l.5): l.95635-95638, "Christiani enim omnes sunt… Habent et magistratus in urbibus et sacerdotes; festa etiam perinde atque nos celebrant"; l.96409-96424, on the Alamanni, "Arbores enim quasdam colunt, et fluminum lapsus… commiseratione et venia, potius quam odio, digni sunt quotquot a vero aberrant". Faithful.
- Faith (l.7): Vossius in the testimonia, l.94359-94363, "Gentilem fuisse praeter alia ostendit illud φασίν… cum sermo fit de martyrio B. Stephani"; the passage, l.106104-106121 ("quem quidem primum olim aiunt"); Niebuhr l.94204-94215, "edito epigrammate quo tabulam archangelo dedicat, illum religionem professum esse extra dubium est… probabile est gentili patre procreatum… ne legum poenis… obnoxius esset, neu opinionis vi adductum, Christianis se adjunxisse". Faithful except B-M23.
- Close (l.9): l.94139-94141, "Tiberio adhuc regnante, ante annum 582… e vita decessisse arbitror"; l.94164-94179, "immunis ab insectatione pariter atque ab adulatione… virum autem multo meliorem esse Procopio". Faithful.
- Card: Niebuhr "quam abjicere maluissem" (l.92892-92893); history begun "mortuo Justiniano imperatore" (l.94120-94121); birth reckoned from 554 (l.94022-94024, OCR "556"); John of Nikiu, "one of the renowned scholars of the city of Constantinople" (`john-nikiu_chronicle_charles1916.txt` l.8946-8947). All faithful.

**Findings**
- **B-M21 MINOR (item 1).** Brief l.1: "In the winter after a great earthquake at Constantinople…". Card `uncertain` 4 (l.38): "the damage of the winter after the earthquake". The earthquake itself struck in that winter: autumn was over and the sun was turning to the winter solstice (l.116357-116365). The dome passage begins "Per hanc enim hiemem" (l.117349). Fix, brief: "After a great winter earthquake at Constantinople, Agathias writes, the people turned good for a while." Card: "He tells it among the damage of the winter of the earthquake."
- **B-M22 MINOR (item 1).** Brief l.5: "as Evagrius Scholasticus, writing a generation later, records." No held source puts a generation between them. Niebuhr dates Evagrius's finished history to 593 (l.94137) and Agathias's death before 582, so the gap is about a decade on the held dates. Fix: "as Evagrius Scholasticus records." (This also brings the brief under the ceiling.)
- **B-M23 MINOR (items 1, 2).** Brief l.7: "G. J. Vossius thought him a pagan, because he tells of the martyr Stephen only as something they say." Vossius gives the "they say" as one sign among others ("praeter alia ostendit", l.94361). Card `uncertain` 1 (l.35) also puts "they say" in quotation marks, but those English words are not in the file (the Greek is φασίν, the Latin "aiunt"). Fix, brief: "G. J. Vossius thought him a pagan, partly because he tells of the martyr Stephen as something they say." Card: "…because, among other signs, he tells the martyrdom of Stephen only as something people say."
- **B-M24 MINOR (item 1).** Card `keyWorks` 2 (l.20-21): title "Daphniaca and the Cycle", about "…and a collection of new epigrams, which he names in his preface". The preface names the Daphniaca ("quae Daphniaca vocavi", l.94852) and describes gathering new epigrams. It does not name a "Cycle", and no held file does (searched the Agathias section, Latin and Greek). Niebuhr says only that he collected them into seven books (l.94037). Fix: title "Daphniaca, and a collection of epigrams"; about: "love poems he wrote when young, which he names in his preface, and new epigrams by others that he gathered into seven books, Niebuhr says; neither is given here." (See B-M25 on "held".)
- **B-M25 MINOR (item 4, process words).** Card `keyWorks` 2 (l.21), "neither is held", and `uncertain` 2 (l.36), "No English translation is held. The Greek of the held edition is badly scanned…". These are Library status lines in participant text. Fix, `uncertain` 2: "His words. They are told here from the Latin version printed beside the Greek in the Bonn edition, a version Niebuhr says he would rather have thrown out." `keyWorks` 2 as in B-M24.

Not findings. Niebuhr's 1828 is the Bonn title page (OCR "MDCCCIXVIII", l.93810). "Hagia Sophia" names what the Latin calls "augustissimum illud Dei templum" and adds no claim. The closing sentence of l.1 ("His Greek is told here from an old Latin version") is the honest-limit line the records call for.

Length with B-M21 to B-M23: 322 words (1:59), FK 6.1, Flesch 73.8.

---

Part B totals: 1 blocking and 25 minor (John of Ephesus 1 and 6, Victor of Tunnuna 0 and 6, Cassiodorus 0 and 8, Agathias 0 and 5).

## Part C

Reviewer: independent, first sight of these drafts. Bar: `Who_Profile_Pattern.md` review checklist 1 to 14 and the standards it points to; `CLAUDE.md` "Trust and source fidelity" and "Accessible and rigorous"; the batch rulings in the brief (majors capped at about 405 words; non-majors at most about 325; Gildas is major; Radegund judged by what is held in her own words). I did not edit any repo file, made no paid or model-API calls and used no web.

Profiles: `gildas` (major), `david-of-wales`, `radegund`, and the batch `README.md`, in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era3/batch4/`. Brief line numbers refer to the `.brief.txt` files, where each paragraph is one line and blank lines count (paragraphs on l.1, 3, 5, 7, 9, 11, 13). Card line numbers refer to the `.card.json` files as they stand. Other line numbers point to files under `cic/texts/`.

Method. I read every quotation in the three briefs and cards against its cited file and lines, by line number, reading each hit in context to see who speaks (the ancient author, the translator, a footnote, a quoted third party). I checked every factual sentence of each brief against its passage. Before accepting each absence claim I ran `grep -il` across `cic/texts/` for every file naming the person (Gildas, Giltas/Gillas; David, Dewi, Devius, Menevia; Radegund/Radegundis/Radegunde) and read the hits that bear on the claim, including the Acta Sanctorum for 1 March and Krusch's 1896 note. Readability came from `engine.m1.gates.grade_text`, run from the repo root. Every suggested brief fix below was applied to a scratch copy and re-scored.

### Applies to all three

- **Audio = brief.** Each audio script matches its brief exactly once `[calmly] ` and `[warmly] ` are removed (checked by script). Each starts with `[calmly]` and has one `[warmly]`, before the closing paragraph. No tag appears in any brief or card.
- **Readability.** All three pass (FK at most 10, Flesch at least 60).
- **Length.** Gildas 401 words (2:28), under the major cap. David 324 (2:00) and Radegund 326 (2:01), at the non-major ceiling. Every `briefLength` matches.
- **Card order.** All three follow Mark's order; missing fields are left out (David has no keyWorks and no ownWords). keyWorks never passes three.

| Profile | Words | Est. @162 | FK | Flesch | After fixes |
|---|---|---|---|---|---|
| Gildas (major) | 401 | 2:28 | 6.1 | 75.5 | 403 words, FK 6.2, Flesch 75.8 |
| David of Wales | 324 | 2:00 | 6.1 | 74.9 | 325 words, FK 6.3, Flesch 74.7 |
| Radegund | 326 | 2:01 | 5.8 | 75.8 | 326 words, FK 5.7, Flesch 76.6 |

---

### 1. Gildas (major)

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | BLOCKING (C-B1); minor (C-M2, C-M4) |
| 2 | Quotes verbatim | PASS (OCR "clragon" for "dragon", Williams l.4760, named in records) |
| 3 | No invention | PASS |
| 4 | Reading aids | minor (C-M1, C-M3) |
| 5 | No role for a witness | PASS (Williams, Ussher, Bede, Columbanus, Alcuin, Caradoc named) |
| 6 | Partisan witness named and marked | PASS (the two Lives marked late; Caradoc's Glastonbury chapters marked fiction by Williams) |
| 7 | Contested both sides | BLOCKING (C-B1) |
| 8 | Common names placed | PASS (Alcuin of York, Caradoc of Llancarfan, Pope Gregory the Great, the Irish saint Columbanus) |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place | PASS |
| 11 | Readability | PASS |
| 12 | Card order, caveat repeated | PASS (Lives-late caveat opens What is uncertain) |
| 13 | Audio tags | PASS |
| 14 | Who test, list line | PASS (own work, the De Excidio) |

**C-B1 (BLOCKING). brief l.5: Ussher's reading of the forty-four years is told as Gildas's own words, and contradicts the brief's next sentence.**
The brief says: "That year, he writes, began forty-four years before, 'with one month now elapsed'." Gildas does not write that Badon's year "began forty-four years before". His sentence, in Williams's English, is ambiguous: `gildas_de-excidio-britanniae-lorica-penitential-lat-eng_williams1899.txt` l.3951-3952, "And this commences, a fact I know, as the forty-fourth year, with one month now elapsed ; it is also the year of my birth." What the forty-four years count from is the controversy the brief then names (Williams l.3927-3928, "There has been much controversy as to the meaning of these words. Beda took them to mean, forty-four years after the coming of the Saxons"). Counting them from Badon to the time of writing is Ussher's reading (l.3969-3976), which Williams adopts, and on that reading Gildas wrote "forty-three years and one month from his time of writing" (l.3643-3644), not forty-four. So the sentence does three wrong things: it gives one side of a contested reading under "he writes", it changes Gildas's number, and two sentences later it is contradicted by "Gildas wrote some forty-three years after his birth".
Fix (whole paragraph l.5; also clears C-M1, C-M2 and C-M3): "Gildas was born in the year of the siege of Badon Hill, almost the last great British victory over the Saxons. He writes of "the forty-fourth year, with one month now elapsed". Bede took the years from the coming of the Saxons. Williams follows the scholar Ussher, who counts them from Badon, so Gildas wrote some forty-three years after his birth. Williams puts that birth about 500, a date no early source gives. He dates the book a few years after 540, and before 547, while a king it attacks, Maglocunus, was alive. The Welsh annals put that king's death in a great plague, in Williams's year 547." (Brief then 403 words, FK 6.2, Flesch 75.8. The quotation is verbatim from l.3951-3952.)

**C-M1. brief l.5: "Gildas gives one fact about himself."** A loose quantifier. The brief's own opening gives another fact from his hand, his ten years of silence (l.393-395), and his book calls the clergy "of my own order" (l.9481). Fix: covered by the C-B1 paragraph, which drops the sentence.

**C-M2. brief l.5: "before 547 ... the great plague of 547": an editor's year told as the annals' own, and a mixed cause.** The Annales Cambriae count by annus; 547 is the reckoning Williams prints, and he says so: l.4743-4745, "An. [547] mortalitas magna in qua pausat Mailcun rex Guenedotiae. The date, 547, can only be an approximate one." The draft's "after 540 and before 547, because a king it attacks, Maglocunus, was still alive" also hangs "after 540" on Maglocunus, which is not Williams's ground for it (l.19789-19790, "the writing of the De Excidio a few years after 540", on "grounds discussed elsewhere"). Fix: covered by the C-B1 paragraph ("a few years after 540, and before 547, while a king it attacks, Maglocunus, was alive. The Welsh annals put that king's death in a great plague, in Williams's year 547.").

**C-M3. brief l.5: colon-reveal.** "Williams follows the scholar Ussher: Gildas wrote some forty-three years after his birth." Fix: covered by the C-B1 paragraph ("Williams follows the scholar Ussher, who counts them from Badon, so Gildas wrote...").

**C-M4. card l.8 (knownFor): "and is almost the only voice of the British church that survives from his time".** No source the card cites says this. Thomas Taylor's nearest line is about the history of Britain, not the British church's voice (`samson-of-dol_life-of-st-samson_taylor1925.txt` l.397-399, "it is to him that we owe practically all that we know of Britain during the fifth and sixth centuries"), and Williams argues against reading Gildas as that kind of source (Williams l.141-142). Fix: end knownFor at "...condemns the kings and clergy of his country."

---

### 2. David of Wales

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | BLOCKING (C-B2); minor (C-M5, C-M6, C-M8, C-M10) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | minor (C-M11, C-M12) |
| 5 | No role for a witness | PASS |
| 6 | Partisan witness named and marked | PASS (the Lives marked late, Ricemarch named) |
| 7 | Contested both sides | PASS in the brief (death year 601 and 588); card see C-B2 |
| 8 | Common names placed | minor (C-M9) |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place | PASS |
| 11 | Readability | PASS |
| 12 | Card order, caveat repeated | PASS |
| 13 | Audio tags | PASS |
| 14 | Who test, list line | PASS (following and Lives, marked late) |

**C-B2 (BLOCKING). card l.30: false absence. "No other held source gives a year" for his birth.**
The Acta Sanctorum for 1 March holds the Bollandists' commentary on David, and it reckons his years. It dates Patrick's stay in the Rosina valley "xxx. annis antequam S. David nasceretur" and then counts the thirty years forward to a year (`acta-sanctorum_martii-tomus-1-lat_1735.txt` l.15502-15529: "Primo S. Patricium, xxx. annis antequam S. David nasceretur, fuisse in Britannia ... Ab anno igitur ccccx1v. annos xxx. numerando ad annum CCCCXIV. pervenitur"; the numerals are OCR-damaged). The same commentary argues for his death "anno intermedio DXLIV" or "anno DL", the years when 1 March fell on a Tuesday (l.15658, l.15675), and dismisses Baronius's 650 as an error. The records already cite this file (l.15297-15298) for the Bollandists' judgement on his Acts, so the file was open; its chronology was missed. The death-year bullet (card l.28) and the `contested_claims` entry on the year of his death also leave the Bollandists out.
Fix: card l.30, replace "No other held source gives a year." with "The Bollandists, in the Acta Sanctorum for the first of March, reckon his birth from the same story of Patrick." Card l.28, add after "Wasserschleben gives 544.": "The Bollandists argue for 544 or 550." Add both to `records.json` (claims and the death-year `contested_claims` sides), with the birth year written out only after the passage at l.15502-15530 has been read and its damaged numerals settled.

**C-M5. brief l.3 and card l.27: "two Lives".** The Acta Sanctorum prints a third Life, from a Utrecht manuscript, and the Bollandists judge it the oldest of the Acts they know (l.15299-15302, OCR-damaged: "ex his antiquissima ea opinamur, quae olim in Belgium ex Britannia delatae, reperimus in codice MS. Ultrajectino"; the Life itself is headed at l.15701-15702, "VITA ex MS. Ultrajectino"). They also say none of his Acts was written by contemporaries (l.15297-15298), which supports the brief's point. Fix: brief l.3, "Almost all that is told of him comes from Lives written centuries later." Card l.27, "Almost all that is told of him comes from Lives written centuries after him, two of them printed by W. J. Rees and one by the Bollandists."

**C-M6. brief l.3 and card l.27: "quotes a Welsh chronicle on his death in 1096".** Williams quotes the chronicle's name for him and a year, nothing about a death: Williams l.22762, "" Rychmarch doeth mab Sulyen escob" (a.D. 1096). — Bruts, p. 273." No other held file gives Ricemarch's death (searched Rychmarch, Ricemarch, Ricemarcus, Rhygyfarch across `cic/texts/`). Fix: brief l.3, "...and quotes a Welsh chronicle that names him under 1096." Card l.27, "...and quotes a Welsh chronicle naming him, son of Bishop Sulien, under 1096."

**C-M7. brief l.7 and card l.27: W. J. Rees's "general truth" sentence carries a source of its own.** The sentence sits in parentheses with a footnote: `rees_lives-of-the-cambro-british-saints-lat-eng_1853.txt` l.398-406, "(And it may be concluded ... that their foundation was in general truth ... to be sought for in vain elsewhere.)5", and note 5 (l.420) is "Monumenta Historica Britannica, fol. London, 1848. Page 39." Rees is citing the view, so "Rees says" makes it wholly his. Fix: brief l.7, "W. J. Rees, who printed both Lives, cites the view that such Lives were rooted in general truth but written to stir devotion, perhaps by exaggerating." Card l.27, "...and cites the view that such Lives were rooted in general truth but written to stir devotion."

**C-M8. brief l.7 and card l.23: "David as we know him" widens Williams.** Williams limits it to the David of the miracles: Williams l.23071-23074, "Perhaps David appears to us in the wonders by which he is known, because clothed in them by this biographer of the eleventh century ; he is the creation, probably, of Ricemarcus". Fix: brief l.7, "Williams thinks the David of the wonders is "the creation, probably, of Ricemarcus", meant to magnify the see of Saint David's." Card l.23, "Williams: the David of the wonders is \"the creation, probably, of Ricemarcus\", written to magnify the see of Saint David's."

**C-M9. brief l.1 and l.9, card l.31: first mentions without identifier.** "Paulinus, his old teacher" is a common name (Paulinus of Nola, Paulinus of York) and has a place in the held file: Rees l.18001, "afterwards in the school of Paulinus, in White House on Tave". "Gildas" in brief l.9 comes with no context for a listener. Fix: brief l.1, "Paulinus, his old teacher from the White House on the Tave, told them to send for David." Brief l.9, "...says their second order received the mass from Bishop David and the writer Gildas." (also clears C-M11). Card l.31, "His Lives name Paulinus, of the White House on the Tave."

**C-M10. brief l.11: "The Welsh Life gives his last sermon."** The quoted words come after the sermon: Rees l.18589-18592, "And when the sermon and mass were concluded David pronounced his blessing ... he spoke as follows, " Lords, brethren, and sisters, be joyful..."". Fix: "The Welsh Life gives his words after his last sermon."

**C-M11. brief l.9: a 26-word narrator sentence.** "A list of Irish saints, which Williams dates to the 700s, says the second order of Irish saints received the mass from Bishop David and Gildas." Fix: "A list of Irish saints, which Williams dates to the 700s, says their second order received the mass from Bishop David and the writer Gildas." (24 words).
Word budget: the fixes for C-M5, C-M6, C-M7, C-M9, C-M10 and C-M11 add 10 words. Offset by cutting brief l.1 "It was done, the Life adds, "at Llanddewibrefi"." The card already gives the place (card l.11). With all of them the brief is 325 words, FK 6.3, Flesch 74.7.

**C-M12. card l.30 and l.32: process word "held" in participant text.** "No other held source gives a year" (replaced under C-B2) and "No held source gives a year for it." Fix: card l.32, "The synod of Brefi. None of these sources gives a year for it."

---

### 3. Radegund

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | minor (C-M14, C-M16) |
| 2 | Quotes verbatim | PASS (letter, Dalton l.19841-19843; card Latin checked against Krusch 1888 and Arndt-Krusch 1885) |
| 3 | No invention | PASS (Fortunatus's scene told in modern words and named; no English of the Lives is held) |
| 4 | Reading aids | PASS |
| 5 | No role for a witness | minor (C-M13) |
| 6 | Partisan witness named and marked | PASS (Fortunatus "her friend"; Baudonivia "a nun of her house") |
| 7 | Contested both sides | PASS (Arles: Gregory and Krusch named) |
| 8 | Common names placed | PASS (Medard at Noyon, Maroveus the bishop of Poitiers, Caesarius of Arles, Gregory of Tours) |
| 9 | One term | minor (C-M15) |
| 10 | Story, scene, disputes in place | PASS |
| 11 | Readability | PASS |
| 12 | Card order, caveat repeated | PASS (her-own-words caveat opens What is uncertain) |
| 13 | Audio tags | PASS |
| 14 | Who test, list line | PASS (her letter in Gregory IX.42 as her own words, the poems marked as Fortunatus's; the tree page's list line is unchanged) |

Absence checks passed. I searched every file in `cic/texts/` that names her for a birth year, a capture year, an English Life and a poem given to her. None contradicts the records. Leo puts the three poems in his appendix of poems kept outside the eleven books, as "carmina ... ut quae olim corporis partem fuisse certum sit" (`venantius-fortunatus_opera-mgh-aa-4-lat_leo-krusch1881.txt` l.1021-1022). That is distinct from the wrongly ascribed poems he exiles (l.1014-1015), so the Fortunatus attribution stands.

**C-M13. brief l.11: "Their editors treat them as his" puts a role in place of the named witnesses.** The card names them (Leo, Krusch, Luchi, Dalton). Krusch: `fredegar-liber-historiae-francorum-vitae-mgh-srm-2-lat_krusch1888.txt` l.28607-28608, "Radegundis nomine Fortunatus ... his versibus planxit". Fix (with the offset below): "Three poems in her voice are printed with Fortunatus's works. Friedrich Leo, who edited them, and Krusch treat them as his, written in her name."

**C-M14. brief l.5: the judgement on Arles is Arnold's, which Krusch adopts, and the brief gives it to Krusch alone.** `passiones-vitaeque-sanctorum-merovingici-mgh-srm-3-lat_krusch1896.txt` l.35704-35705, "Gregorius, H. Fr. IX, 40, rettulit, sed eum falli Arnold l. l. p. 418, recte monuisse mihi videtur". The card (l.33) has it right. Fix: "Bruno Krusch, who edited her two Lives, later agreed with the scholar Arnold that Gregory was wrong."

**C-M15. brief l.5: "rule" in two senses in one sentence.** "She made Agnes its abbess, lived under her rule, and took for the house the Rule of Caesarius of Arles." Her letter says "I submitted myself in regular obedience to her authority" (`gregory-tours_history-of-the-franks-v2_dalton1927.txt` l.19859-19860). Fix: "She made Agnes its abbess, obeyed her, and took for the house the Rule of Caesarius of Arles."

**C-M16. brief l.7 and card l.22: the name Holy Cross.** Brief l.7, "Her house came to be called Holy Cross", names no witness, and the sentence before it is Gregory's. In the cited History passage (IX.40) Gregory does not give the name; Krusch does (Krusch 1888 l.28153, "Monasterium autem quod construxit Pictavicum nomen S. Crucis accepit"). Card l.22 adds "after the relic of the Cross", which Krusch's sentence does not say. Fix: brief l.7, "Her house came to be called Holy Cross, Krusch says." Card l.22, "Her monastery at Poitiers took the name of Holy Cross, Bruno Krusch says. Gregory of Tours tells how she brought it a relic of the Cross from the East."
Word budget: C-M13, C-M14 and C-M16 add 11 words and C-M15 saves 3. Offset by brief l.3, "Then, Fortunatus writes, she came from the king to Medard." (for "It was then, Fortunatus writes, that she came from the king to Medard."), and by dropping "among them a lament for Thuringia," from l.11 (the card keeps it, l.32). With all of them the brief is 326 words, as drafted: FK 5.7, Flesch 76.6.

**C-M17. card l.32 and l.35: the process word "held", and a claim wider than its evidence.** Card l.32 has "no held editor doubts it", and card l.35 "No held source gives a year of birth or of her capture." Also, Krusch 1896 reports Malnory as "hanc falsam esse suspicatus" (l.35706). Read in context, "hanc" most likely means Caesaria's letter, but a universal "no editor doubts" should not rest on that reading. Fix: card l.32, "Her letter in Gregory's History is given as hers, and Dalton and Krusch take it so." Card l.35, "Her years. None of these sources gives a year of birth or of her capture."

---

### 4. README.md

PASS. Its account of the major marks, John of Ephesus as a recorder, Agathias's label, Radegund's own words (the letter given as hers, the three poems Fortunatus's) and David's Lives marked late matches the drafts and the rulings in the review brief. The file table matches the files on disk.

---

**Totals for part C: 2 blocking (C-B1 Gildas, C-B2 David of Wales) and 17 minor (Gildas 4, David of Wales 8, Radegund 5, README 0).**
