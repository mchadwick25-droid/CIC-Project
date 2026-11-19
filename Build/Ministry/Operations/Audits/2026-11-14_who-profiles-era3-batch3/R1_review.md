# R1 review: ten Who profiles, era 3 batch 3

Three independent Opus reviewers, each at first sight of its drafts, reviewed the batch in three parts: part A (Theodora, wife of Justinian, Marcellinus Comes, Procopius of Caesarea), part B (Vigilius of Rome, Romanos the Melodist, Samson of Dol) and part C (Mar Aba I, Cosmas Indicopleustes, Barsanuphius and John of Gaza, Cyril of Scythopolis, and the README). Totals: 11 blocking and 57 minor (part A 0 and 23, part B 5 and 14, part C 6 and 20).

## Part A

Reviewer: independent, first sight of these drafts. Bar: `Who_Profile_Pattern.md` review checklist 1 to 14 and the standards it points to; `CLAUDE.md` "Trust and source fidelity" and "Accessible and rigorous"; the Who profile rulings in `Decision-Log.md`, 2026-11-12 to 2026-11-14 (majors capped at 2:30, about 405 words, a cap and not a target; non-majors 1 to 2 minutes, at most about 325 words at 162 wpm; the outside witness card's Tradition line "Outside the church", as on era 1 batch 2's Tacitus card). Known for this batch: Theodora is a Who on Mark's named ruling "Theodora: Who" (era 3 scan, `Who_Scan_Era3.md` l.22) and is major; Procopius carries the Outside witness label; Marcellinus is a recorder with no label. I hunted hardest for the recurring faults of earlier batches: witness swaps, an editor's year told as the ancient writer's, a contested point told as settled, absence claims a held file contradicts, pronouns that can point the wrong way in a sentence marking a source partisan, common names without a place, and AI tells. I did not edit any repo file. I made no paid or model-API calls and used no web. Quote search and readability ran on local scripts only.

Profiles: `theodora-wife-of-justinian` (major), `marcellinus-comes` and `procopius-of-caesarea`, with their cards, audio scripts and entries in `records.json`. Files are in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era3/batch3/`. Brief line numbers refer to the `.brief.txt` files, where each paragraph is one line and blank lines count (paragraphs sit on l.1, 3, 5, 7, 9, 11, 13). Card line numbers refer to the `.card.json` files as they stand. Other line numbers point to files under `cic/texts/`.

Method. I searched every quotation in the three briefs and cards in the vendored file the card or records cite, with a script that collapses whitespace, normalises quote marks and dashes, folds accents and lets letters be split by OCR spacing. For the OCR files (Brooks's Lives of the Eastern Saints, Chabot's Michael the Syrian, Mommsen's Chronica minora II, Migne's Cassiodorus, Walford's and Bidez-Parmentier's Evagrius, Migne's Nicephorus Callistus) I read each passage by line number. I read each hit in context to see who is speaking: the ancient author, a document he quotes, a translator's preface, a footnote, or an editor's margin or bracket. I checked every factual sentence of each brief against its passage. Before accepting each absence claim (Theodora's birth year; words of her own; the Cyprus tradition; Marcellinus's birth and death; Procopius's firm years) I searched the Library. I compared each `records.json` entry with its brief and card. Readability came from `engine.m1.gates.grade_text`, run from the repo root. Every suggested brief fix below was applied to a scratch copy and re-scored; the post-fix word count and scores are given with each profile.

### Applies to all three

- **Audio = brief.** Each audio script matches its brief exactly once `[calmly] ` and `[warmly] ` are removed (checked by script). Each starts with `[calmly]` and has one `[warmly]`, before the closing paragraph. No tag appears in any brief or card. When a brief fix below changes a line, the audio script follows it.
- **Readability.** All three pass (FK at most 10, Flesch at least 60). Marcellinus sits nearest the floor (Flesch 61.8). Narrator sentences past 25 words: Procopius l.1 (27) and l.5 (28); A-M13.
- **Length.** Theodora runs 404 words (2:30), at the cap. Marcellinus runs 317 (1:57) and Procopius 323 (2:00). Every `briefLength` matches.
- **Card order.** All three follow Mark's order. Missing fields are left out (Theodora has no keyWorks; Procopius has no otherNames). keyWorks never goes past three. Procopius's `label` sits where Tacitus's does. Each `uncertain` list carries the brief's caveats. The `"date": null` in source entries is the schema the earlier batches used.
- **Who test (item 14).** Theodora stands on Mark's named ruling; the README, card and records all say no words of her own are held and that the Nika speech is Procopius's. Marcellinus is a recorder whose chronicle is a main source for the church riots of the capital. Procopius is a historian reporting on the church, and none of the three works is a polemic against the church; the Secret History's attack is on the court. The drafts carry no list lines; those belong to the map build and were not checked here.
- **No findings.** I found no blocking point in part A. Every quotation matches its vendored file. No absence claim is contradicted by a held file (but see A-M7 on the Cyprus tradition, which the Library holds directly).

| Profile | Words | Est. length @162 | FK | Flesch |
|---|---|---|---|---|
| Theodora, wife of Justinian (major) | 404 | 2:30 | 6.5 | 68.6 |
| Marcellinus Comes | 317 | 1:57 | 7.6 | 61.8 |
| Procopius of Caesarea | 323 | 2:00 | 7.4 | 65.6 |

---

### 1. Theodora, wife of Justinian (major)

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | minor (A-M1, A-M4, A-M8) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | minor (A-M9 pronoun) |
| 5 | No role for a witness | PASS (John of Ephesus, Payne Smith, Procopius, Dewing, Michael, Evagrius, Brooks, Chabot named) |
| 6 | Partisan witness named and marked | minor (A-M1, A-M2) |
| 7 | Contested both sides | minor (A-M4, A-M7) |
| 8 | Common names placed | FAIL, minor (A-M6) |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | PASS (404 words, 2:30, at the cap) |
| 11 | grade_text | PASS |
| 12 | Card order, caveat repeated | PASS ("Her witnesses take sides" opens `uncertain`) |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS (Mark's named ruling; no own words, said so) |

**Quotes and close tellings**
- Mare and Stephen (l.1): `john-of-ephesus_lives-of-the-eastern-saints_brooks1923.txt` l.10418-10424 (Mare exiled at Petra, sends "Stephen his deacon and notary to the royal city"), l.10456-10466: "directed the virtuous Stephen to Theodora who came froin the brothel (mosvetov), Who was at that time a patrician, but eventually beeame queen also with King Justimian… made entreaty to Justinian her hushand… the King's nephew… that he would inform his uncle… even with tears… an order went out to them to come to Alexandria". The quote matches through OCR "froin". Same passage in the PO 17 file. Settlement in Alexandria follows (l.10480-10483). Faithful.
- Payne Smith (l.3): `john-of-ephesus_ecclesiastical-history-part3_paynesmith1860.txt` l.287-290, "he was a Monophysite: and though his party… yet they refused to receive the council of Chalcedon". Faithful.
- Secret History (l.3): `procopius_secret-history_athenian-society1896.txt` l.1826-1828, "There was one Acacius at Byzantium, of the Green faction, who was keeper of the wild beasts… called the Bear-keeper"; l.1842-1843, "their mother straightway sent them on the stage". Faithful.
- Dewing (l.3): `procopius_wars-1-2-persian_dewing1914.txt` l.155-158, "an account of her early years which is both shocking and disgusting, but which, happily, we are not forced to regard as true". Faithful paraphrase.
- Michael (l.3): `michael-the-syrian_chronique-tome2-livres-viii-xi-fra_chabot1901.txt` l.32343 and l.32392-32395, "de Dâmân, ville située au-dessus de Callinice. Son père était prêtre… grandi dans la chasteté et la foi orthodoxe". Faithful.
- Nika speech (l.5): Wars I.xxiv, Dewing l.3102-3122: "the emperor and his court were deliberating as to whether… they took to flight in the ships… the Empress Theodora also spoke to the following effect… I approve a certain ancient saying that royalty is a good burial-shroud." Quote exact; see A-M3. "Spoke to the following effect" is Procopius's own mark that the words are his telling. Dewing on speeches, l.196-199: "especially in the speeches he is fond of introducing sounding phrases". The year 532 is Dewing's (l.131-132). Faithful.
- Evagrius (l.7): `evagrius-scholasticus_ecclesiastical-history_walford1846.txt` l.8149-8167 (IV.10), "either because such were their real sentiments… or by mutual understanding… She also persuades Justinian to send for Severus." "Native of Epiphania" is Walford, l.327. Faithful. The Greek (Bidez-Parmentier l.14987) agrees.
- Secret History X (l.7): l.2069-2076, "this disagreement was seen to have been purposely arranged between them… they split up the Christians into two parties". Faithful.
- Anthimus (l.9): Lives, l.25960-26003, "she took him and hid him in a chamber in hee palace… a space often years in hiding… until the time of the queen's death"; Brooks's note l.26024-26025, "Theodora lived 12 years after his deprivation. In the Eccl. Hist. (Land, p. 388) J. says that he was 7 years in hiding." See A-M4.
- Hormisdas (l.9): Lives ch. 47, l.25497-25503, "who did not fall short of the number of five hundred"; l.25612-25613, "once in every two or three days come down to them to be blessed by them"; l.25653-25654, "even after her death she laid an injunction upon the king about it, and it was preserved". Faithful.
- Bishops (l.9): Lives ch. 50, l.26697-26703 ("in the sixteenth year of the reign of Justinian… Hereth Bar Gabala, the great king of the Saracens… asked the Christ-loving queen Theodora"), l.26745-26750 ("James and Theodore… one for Hirtha of the Saracens, that is Theodore, and James for the city of Edessa"). Faithful; see A-M6.
- Death (l.11): Michael tome 2 l.18175-18177, "en l'an 20 de Justinianus, qui est l'an 859 (des Grecs)"; Brooks, Lives introduction l.248-249, "after her death (548)". Faithful.
- Close (l.13): Lives l.17536-17538, "the Christ-Ioving Fheodora, who was perhaps appointed queen by God to be à support for the persecuted". Exact through OCR.
- Card: the Zachariah chronicle quote ("incited thereto by Theodora the queen, who was devoted to Severus", `zachariah-rhetor_chronicle_hamiltonbrooks1899.txt` l.13165-13167) is exact, and the introduction that gives Zachariah's own work an end at 491 (l.300-314) is signed "E. W. BROOKS" (l.724), so the card's credit is right. Evagrius's "those who maintained the single nature" and "Our people she treated with the warmest kindness" are exact. Chabot's "inventé par les Monophysites" is note 5, l.13546, on the Mabboug story (l.13518-13522). The Anthimus durations match Brooks's note. Birth year: no held line gives one (searched the Library).

**Findings**
- **A-M1 MINOR (items 1, 6).** Brief l.3: "John wrote as her friend." Card `uncertain` 1 (l.27) "John of Ephesus wrote as her friend" and `uncertain` 2 (l.28) "John of Ephesus, her friend". No held source makes John her friend. What the held files show is that he wrote for the party she protected (Payne Smith l.287-290) and lived, Brooks thinks "perhaps", in the palace of Hormisdas "where many of the refugees were settled under the protection of Theodora" (Lives introduction l.286-287). "Friend" claims a personal tie. Fix, brief l.3: "John wrote from the side she sheltered." Card `uncertain` 1: "John of Ephesus wrote from the party she sheltered and belonged, R. Payne Smith notes, to the party that refused Chalcedon." Card `uncertain` 2: "John of Ephesus, of the party she sheltered, also calls her…".
- **A-M2 MINOR (item 6).** Brief l.3: "The twelfth-century patriarch Michael the Syrian made her a priest's daughter…, raised in chastity." John, Procopius and Evagrius are each placed. Michael, whose account is the friendliest of all, is not: he is the Jacobite patriarch of Antioch (Chabot's title, tome 2 l.1 and l.39), of John's own church, and Chabot judges his Mabboug version of the marriage "inventé par les Monophysites" (l.13546). Fix: "The twelfth-century Michael the Syrian, a patriarch of John's church, made her a priest's daughter from Daman, near Callinicus, raised in chastity."
- **A-M3 MINOR (item 1).** Brief l.5: "She ends, 'royalty is a good burial-shroud.'" In Procopius she cites the line as a proverb: "I approve a certain ancient saying that royalty is a good burial-shroud" (Dewing l.3121-3122). The cut makes an old saying sound like her own coinage. Fix: "She ends by approving an ancient saying, 'royalty is a good burial-shroud.'"
- **A-M4 MINOR (items 1, 7).** Brief l.9: "she hid him in her palace until her death." This follows the Lives (l.26000-26002). But John's own Church History gives seven years in hiding, and Theodora lived twelve years after Anthimus was deposed (Brooks's note, l.26024-26025). The card tells the dispute (`uncertain` 5); the brief states one side as settled. At the cap the shortest fix is to drop the disputed end point and leave it to the card: "she hid him in her palace for years."
- **A-M5 MINOR (records).** `records.json`: the claim "Length of Anthimus's hiding" is tagged Contested, but `contested_claims` has no entry for it. The pattern's Confidence section requires one. Add: `{"claim": "How long Anthimus stayed hidden", "sides": "John of Ephesus, Lives (combined l.26000-26002): ten years, until her death. John's Church History, as Brooks reports it (l.26024-26025): seven years. Brooks: she lived twelve years after his deprivation."}`
- **A-M6 MINOR (item 8).** Brief l.9: "James and Theodore were made bishops, James for Edessa." Theodore is a common name and is given no place, though John gives it (Hirtha of the Saracens, l.26747-26748). Card `knownFor` (l.7), its first mention, "the bishops James and Theodore", has neither. Card `legacy.traces` 2 (l.16) repeats the brief's form. Fix, brief: "She gave the order, and James was made bishop for Edessa and Theodore for Hirtha of the Saracens." Card `knownFor`: "…and gave the order for James, bishop for Edessa, and Theodore, bishop for Hirtha of the Saracens." Card `legacy.traces` 2: "…she gave the order by which James was made bishop for Edessa and Theodore for Hirtha of the Saracens, John says."
- **A-M7 MINOR (items 1, 7).** Card `uncertain` 2 (l.28) gives the Cyprus tradition only through Chabot's note and ends "The held English Evagrius has no such line." The records say the same ("not found in the held Walford Evagrius"). That is true (the Greek Evagrius has none either; Bidez-Parmentier, no Cyprus line near any Theodora hit). But the Library holds Nicephorus Callistus, the other writer Chabot names, and he says it directly: Justinian honoured Cyprus "ἐπὶ δόξῃ τῆς γαμετῆς Θεοδώρας Κύπρον λαχούσης πατρίδα" (`nicephorus-callistus_historia-ecclesiastica-with-hesychast-tracts-pg147-grc-lat_migne1865.txt` l.9790-9791), and again "εἰς τιμὴν τῆς γαμετῆς Θεοδώρας τῆς Βασιλίδος· ἐκεῖθεν γὰρ ὥρμητο" (l.14762-14765; Latin l.14727, "conjugis suae Theodorae Augustae inde ortae"). As written, the card leaves a held third account resting on an editor's note with a hint of doubt. Fix, card `uncertain` 2, replace the last two sentences: "J.-B. Chabot, Michael's French translator, judges the Mabboug story 'inventé par les Monophysites'. Nicephorus Callistus, a later Greek church historian, says Cyprus was her homeland. Chabot gives the same to Evagrius, but the held Evagrius has no such line." Add Nicephorus (PG 147) to `sources.about`, add a records claim tagged Contested with that witness, and add his side to the "Theodora's origins" contested claim. The held file does not date him in its header, so "later" is the safe word.
- **A-M8 MINOR (item 1; records).** Card `dates` (l.8): "empress from his accession in 527." The year is unattributed and has no records claim. Dewing gives it (`procopius_wars-1-2-persian_dewing1914.txt` l.68-69, "the eventful reign of Justinian (527-565 A.D.)", and l.78-80). Fix: "empress from his accession, in 527 by H. B. Dewing's year." Add a records claim: "Justinian's reign began in 527", witness Dewing's introduction (wars-1-2 l.68-69, 78-80), Widely Accepted.
- **A-M9 MINOR (item 4).** Brief l.7: "…says Justinian upheld the council and Theodora backed the single nature of Christ. He offers two reasons…" The nearest "he" is Justinian; the reasons are Evagrius's. Fix: "Evagrius offers two reasons: true conviction, or an agreement between them."

Not findings. "She was then a patrician, married to Justinian" follows John. Brooks dates the marriage after a law of 520-524 and Mare's expulsion probably to 521 (PO 17 l.11012-11016), but he does not say John is wrong. "The rest he tells as scandal" marks the polemic and names its owner. The Nika speech is marked as Procopius's composition in brief, card and records, and the records tag it Inferential-Thin. Hostile and friendly witnesses are each named and placed once (John l.3, Procopius l.3, Evagrius l.7); later mentions refer back.

Length with A-M1 to A-M9: the fixes add words. Suggested cut: "Every two or three days she came down to be blessed by them." (l.9). Scored: 405 words (2:30), FK 6.8, Flesch 67.3.

---

### 2. Marcellinus Comes

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | minor (A-M10, A-M11, A-M12) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS |
| 5 | No role for a witness | PASS (Mommsen, Cassiodorus named) |
| 6 | Partisan witness named and marked | PASS ("those he calls orthodox", "what Marcellinus calls his usual false oaths"; Mommsen on his hatred of heretics) |
| 7 | Contested both sides | PASS (no dispute told; Mommsen's readings are tagged as his) |
| 8 | Common names placed | FAIL, minor (A-M13 card) |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | PASS (317 words, 1:57) |
| 11 | grade_text | PASS (Flesch 61.8) |
| 12 | Card order, caveat repeated | PASS |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS (recorder) |

**Quotes and close tellings** (`chronica-minora-2_marcellinus-victor-tunnunensis-biclaro-isidore-mgh-aa-11-lat_mommsen1894.txt`)
- The hymn riot (l.1, 3): l.8299-8308, "512 V. PAVLI ET MVSCIANI… Die dominico, dum iubente Anastasio Caesare per Marinum perque Platonem in ecclesiae pulpito consistentes in hymnum trinitatis deipassianorum quaternitas additur, multi orthodoxorum pristina voce psallentes perfidosque praecones clamoribus obiurgantes in eiusdem ecclesiae gremio caesi sunt ductique in carceres perierunt. altera nihilominus die in atrio sancti Theodori maiore caede…"; l.8308-8359, the forum of Constantine, "Areobindam sibi imperatorem fieri clamitant", "imaginibus deinde statuisque Anastasii in terram deiectis", "solitis periuriis simulatisque vocibus, sese facturum cuncta promittens, tertio die… sine ullo rerum effectu ad sua fecit habitacula repedare". The year 512 is Mommsen's margin, and the brief gives it to him. Faithful, except A-M10.
- Mommsen (l.5): l.3100-3104, "Latina lingua ut patria utitur"; l.3162-3163, "Vixisse eum Constantinopoli". Faithful.
- Cassiodorus (l.5, 11): Institutions I.17, quoted by Mommsen l.3056-3058 and in Migne PL 70 l.83217-83222: "hunc subsecutus est supra scriptus Marcellinus Illyricianus, qui adhuc patricii Iustiniani fertur egisse cancellos". Faithful. "Of the same age" is Mommsen's "aequalis Cassiodorus" (l.3172).
- Preface (l.7): l.4711-4720, "ego vero vir clarissimus Marcellinus comes… Orientale tantum secutus imperium… a consulatu Ausonii et Olybrii… usque in consulatu Magni… eorundem auctorum operi subrogavi. Itemque alios sedecim annos a consulatu Iustini Augusti primo usque in consulatum Iustiniani Augusti quartum suffeci… et meum rusticum opus subposui." "meum rusticum opus" is exact. The years are Mommsen's headings (l.4722); see A-M11.
- Mommsen's judgments (l.9): l.3173-3175, "orthodoxum odium quaevis pagina apud Marcellinum spirat cum adversus haereticos omnes tum maxime adversus Nestorianos"; l.3184-3185, "studium auctoris in Iustinianum"; l.3188-3191, "Auctarium, quod ex duobus a quibus pendemus Marcellini archetypis alterum solum exhibet, ab anno illo 534 incipiens et desinens mutilum in a. 548, Marcellino abiudicandum est, non solum quod Cassiodorus id non novit, sed multo magis quod in praefatione non commemoratur". See A-M12.
- Card: "Marcellinus Illyricianus", "fertur", "meliore condicione devotus" (l.3059), the four books on Constantinople and Jerusalem (l.3049-3051, 3094-3096), "probabile est" for the East (l.3193-3194), and Mommsen's dating of the first edition "regnante Iustino, id est ante a. 527" (l.3179) are exact. The absence of birth, death and family holds (no other held file gives them).

**Findings**
- **A-M10 MINOR (item 1).** Brief l.1: "They were cut down in the church, he writes, and others died in prison." Marcellinus says the same men were struck down in the church and, led off to prison, died there: "in eiusdem ecclesiae gremio caesi sunt ductique in carceres perierunt" (l.8308). "Others" adds a second group the Latin does not have. Fix: "They were struck down in the church, he writes, and taken to prison, where they died."
- **A-M11 MINOR (item 1).** Brief l.7: "In his preface Marcellinus calls himself… His book carries on the chronicle… It runs from 379 to 518. Later he added sixteen more years, up to 534." The preface counts by consuls and indictions, from the consulship of Ausonius and Olybrius to that of Magnus, then to Justinian's fourth consulship (l.4711-4720). The years are Mommsen's (l.4722, the heading "379 VII INDICTIONE"), and the card says so (`uncertain` 2), but the brief sets them inside the preface paragraph as Marcellinus's own. Fix: "Mommsen dates it from 379 to 518. Later Marcellinus added sixteen more years, up to 534." ("Marcellinus" in the second sentence keeps "he" from pointing at Mommsen.)
- **A-M12 MINOR (item 1).** Brief l.9: "One manuscript goes on to 548." Card `legacy.traces` 1 (l.21): "Two early copies carry the chronicle: one ends at 534… and the other runs on to 548." Mommsen speaks of the two archetypes from which the manuscripts descend, one of which alone carries the continuation, which breaks off in 548 ("ex duobus a quibus pendemus Marcellini archetypis alterum solum exhibet… desinens mutilum in a. 548", l.3188-3189). It is a family of manuscripts, not one manuscript, and it ends broken off. Fix, brief: "One of the two families of manuscripts runs on to 548." Card: "All the manuscripts come down from two lost early copies, Mommsen says. One ends at 534, where the preface says it ends; the other runs on to 548, where it breaks off."
- **A-M13 MINOR (item 8).** Card `dates` (l.8): "Theodor Mommsen judges that he first issued it under Justin, before 527." The card's first mention of Justin (a name shared with Justin Martyr and Justin II) has no identifier. The brief does not name him. Fix: "…under the emperor Justin, before 527."

Length with A-M10 to A-M12: 325 words (2:00), FK 7.8, Flesch 60.8. This sits at the non-major ceiling and near the Flesch floor; no cut is needed, but the drafter should re-score after any other change.

---

### 3. Procopius of Caesarea (Outside witness)

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | minor (A-M16, A-M17, A-M18, A-M19, A-M22) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | minor (A-M14, A-M15, A-M20) |
| 5 | No role for a witness | PASS (Dewing named; the 1896 preface is unsigned and the drafts call its writer the unnamed translator, consistent with the preface's own "the translator", l.220) |
| 6 | Partisan witness named and marked | PASS (Secret History marked as an attack; its owner named; the Buildings as court praise) |
| 7 | Contested both sides | PASS in the brief (authorship and trust give Dewing and the 1896 translator); card minor (A-M21) |
| 8 | Common names placed | PASS |
| 9 | One term | PASS ("chief priest of Rome", defined as Procopius's word for the pope) |
| 10 | Story, scene, disputes in place, length | PASS (323 words, 2:00) |
| 11 | grade_text | PASS |
| 12 | Card order, caveat repeated | PASS |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS (historian reporting on the church; no polemic against it; the card's Tradition line reads "Outside the church") |

**Quotes and close tellings**
- The envoys (l.1): `procopius_wars-5-6-gothic_dewing1919.txt` l.403-416, "there came from Byzantium to the chief priest of Rome two envoys… a tenet of faith, which is a subject of disagreement and controversy among the Christians… although I know them well, I shall by no means make mention of them; for I consider it a sort of insane folly to investigate the nature of God… I, for my part, will say nothing whatever about God save that He is altogether good and has all things in His power." Both quotes exact.
- Life (l.3): Dewing's introduction, `procopius_wars-1-2-persian_dewing1914.txt` l.69-75 and 84-89 ("born late in the fifth century in the city of Caesarea in Palestine… studied to fit himself for the legal profession… came as a young man to Constantinople… in 533 he accompanied Belisarius to Africa; and in 536 he journeyed with him to Italy… an eye-witness"). Wars I.xiii, l.1510-1512, "It was at that time that Procopius, who wrote this history, was chosen as his adviser. [527 A.D.]"; the year is Dewing's bracket and the card says so. Faithful.
- Silverius (l.5): Wars V.xxv, `procopius_wars-5-6-gothic_dewing1919.txt` l.3473-3476, "a suspicion arose against Silverius, the chief priest of the city, that he was engaged in treasonable negotiations with the Goths, and Belisarius sent him immediately to Greece, and a little later appointed another man, Vigilius". Faithful (A-M15 re-words it more closely).
- Hagia Sophia (l.5): `procopius_buildings_stewart1888.txt` l.493-496, "as though it were suspended from heaven by the fabled golden chain". Exact.
- Dewing on the three works (l.5, 7): l.141-160, 161-170, 172-191 ("the very extravagance of the calumny makes it impossible to be believed", "very few contradictions in statements of fact", "it is now believed to be highly probable at least, that the Anecdota is the work of Procopius", "the calm tone of the History", "written in the empty style of the fawning flatterer… a storehouse of information concerning the internal administration of the empire"). Close tellings checked in A-M16 to A-M18.
- The 1896 preface (l.7, 9): `procopius_secret-history_athenian-society1896.txt` l.94-100 ("His own writings do not decide the question… being of a sceptical turn of mind, he was indifferent; but that, living under an orthodox Emperor, he affected the forms and language of Christianity"), l.155-158 ("Direct proofs of authenticity are wanting, since the most ancient authors who attribute it to him—Suidas and Nicephorus Callistus—lived centuries later"), l.183-186 ("although details may be exaggerated, the work on the whole gives a faithful picture of the Byzantine Court of the period"). Faithful.
- Card: "Procopius is known to posterity as the historian of the eventful reign of Justinian" (Dewing l.68-69), "the first and most talented of Byzantine historians" (1896 l.111-112), "highly probable at least", "affected the forms and language of Christianity", "is supposed to have died in 565" (Buildings preface l.111) are exact. The Buildings' opening on the burned church (Stewart l.395-403) supports `legacy.traces` 2.

**Findings**
- **A-M14 MINOR (item 4).** Two narrator sentences run past 25 words. Brief l.1 (27): "Two envoys came… about a point of faith that Christians quarrelled over." Brief l.5 (28): "It tells how Belisarius sent Silverius… and put Vigilius in his place." Fix, l.1: "Two envoys came from Constantinople to the chief priest of Rome, as Procopius of Caesarea calls the pope. They came about a point of faith that Christians quarrelled over." Fix, l.5: see A-M15.
- **A-M15 MINOR (item 1).** Brief l.5: "sent Silverius… away to Greece on a charge of plotting with the Goths". Procopius says "a suspicion arose against Silverius" and Belisarius acted on it at once (l.3473-3475); no charge is brought in this passage. Fix (with A-M14): "It tells how Belisarius suspected Silverius, the chief priest of Rome, of plotting with the Goths. He sent him away to Greece and put Vigilius in his place."
- **A-M16 MINOR (items 1, 4).** Brief l.5 opens on a thesis in the narrator's voice: "His three works judge the same reign in three ways." The judgment is Dewing's ("three different points of view which vary so widely that posterity has sometimes found it difficult to reconcile them", l.108-110), but no witness is named, and the paragraph that follows gives Dewing's view of each work anyway. Fix: delete the sentence, so l.5 opens "Dewing notes the calm tone of the History of the Wars." (Or, if kept: "Dewing says his three works show the same reign from three points of view.")
- **A-M17 MINOR (item 1).** Brief l.5: "Dewing calls the Buildings the work of a fawning flatterer". Dewing speaks of the style, "written in the empty style of the fawning flatterer" (l.182-183), and says earlier that Procopius "could not obliterate himself enough to play the abject flatterer always" (l.102). The brief turns a judgment on the style into a judgment on the man. Fix: "Dewing says the Buildings is written in the style of a fawning flatterer, but is still a storehouse of facts."
- **A-M18 MINOR (item 1).** Brief l.7: "Dewing thinks it highly probable that he did." Dewing reports a general view: "it is now believed to be highly probable at least" (l.168). The card has it right. Fix: "Dewing says it is now believed highly probable that he did."
- **A-M19 MINOR (item 1).** Brief l.9: "at times like a follower of the old Greek gods." Dewing: "at times as one imbued with the ideas of the ancient religion of Greece. Doubtless his study of the classical writers led him into this, perhaps unconsciously" (l.205-207). "Follower" makes him at times a worshipper, which Dewing does not say. Fix: "at times like a man steeped in the old religion of Greece."
- **A-M20 MINOR (item 4).** Two pronouns point the wrong way. Brief l.3: "…says H. B. Dewing, his English translator. He trained in law" (the nearest "he" is Dewing). Brief l.5: "The Buildings praises Justinian's churches. He writes that the dome…" (the nearest "he" is Justinian). Fix: "Procopius trained in law and went to Constantinople." and "Procopius writes that the dome of Hagia Sophia seemed…".
- **A-M21 MINOR (items 1, 7; card).** Card `dates` (l.5): "Born late in the fifth century, by H. B. Dewing's account". The other two held prefaces differ: the 1896 translator, "towards the beginning of the sixth century" (l.46); the Palestine Pilgrims' Text Society, "early in the sixth or at the end of the fifth century" (Buildings l.98-99). The records note it (`absent_details`, "His birth year and death year"), but the card gives one side only. Add to `uncertain`: "His birth. Dewing says late in the fifth century; the 1896 translator, towards the beginning of the sixth; the Palestine Pilgrims' Text Society's preface, early in the sixth or at the end of the fifth."
- **A-M22 MINOR (item 1; card).** Two card sentences claim more than the source. `uncertain` 5 (l.39): "Dewing says only that he seems to have outlived Belisarius." Dewing also says "His own activity continued till well nigh the end of Justinian's life" (l.82). Fix: "Dewing says his work went on till near the end of Justinian's life, and that he seems to have outlived Belisarius." `legacy.traces` 2 (l.27): "a storehouse of facts about how the empire was run, in Dewing's words" presents a paraphrase as Dewing's words. Fix: "…and is, in Dewing's words, 'a storehouse of information concerning the internal administration of the empire'."
- **A-M23 MINOR (item 4; card).** Card `uncertain` 1 (l.35) ends: "The label Outside witness and the line Outside the church follow the standing rule for a historian who reports on the church; they make no claim about his faith." "Follow the standing rule" is process narration on a participant-facing card (Style Guide 1.11; `CLAUDE.md`, live surfaces carry no process commentary). The point itself is worth keeping, since Dewing has him write "at times as a Christian". Fix: "Outside the church marks him as a historian who reports on the church and kept out of its disputes; it makes no claim about his faith." (Basis: Wars V.iii, l.409-414.)

Length with A-M14 to A-M20: 324 words (2:00), FK 7.6, Flesch 63.3. The A-M16 deletion pays for the other fixes.

---

### Part A totals

| Profile | Blocking | Minor |
|---|---|---|
| Theodora, wife of Justinian | 0 | 9 (A-M1 to A-M9) |
| Marcellinus Comes | 0 | 4 (A-M10 to A-M13) |
| Procopius of Caesarea | 0 | 10 (A-M14 to A-M23) |
| Part A | 0 | 23 |

## Part B

Reviewer: independent, first sight of these drafts. Bar: `Who_Profile_Pattern.md` review checklist 1 to 14 and the standards it points to; `CLAUDE.md` "Trust and source fidelity" and "Accessible and rigorous"; the Who profile rulings in `Decision-Log.md` (2026-11-12 to 2026-11-14), with Mark's length rulings as the earlier batch reviews apply them (majors capped at 2:30, about 405 words, a cap and not a target; non-majors 1 to 2 minutes, at most about 325 words at 162 a minute). I hunted hardest for the recurring faults of earlier batches: witness swaps, an editor's year told as an ancient writer's, an attribution or identification told as settled where a held file disputes it, absence claims a held file contradicts, pronouns that can mislead in sentences that mark a witness partisan, common names without a place, and AI tells. I did not edit the drafts. I made no paid or model-API calls and used no web. Readability and quote search ran on local scripts only.

Profiles: `vigilius-of-rome` (major), `romanos-the-melodist` and `samson-of-dol`, with their cards, audio scripts and entries in `records.json`. Files are in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era3/batch3/`. Brief line numbers refer to the `.brief.txt` files, where each paragraph is one line and blank lines count (paragraphs sit on l.1, 3, 5, 7 and so on). Other line numbers point to files under `cic/texts/`.

Method. I searched every quotation in the three briefs and cards in the vendored file the card or records cite, with a script that folds accents and case and drops whitespace and punctuation, so OCR letter-spacing and quote marks cannot hide a hit. For the OCR files (Loomis's Book of the Popes, Mommsen's Chronica minora II, Guenther's Collectio Avellana, Pitra's Romanos, Maassen's Merovingian councils, Taylor's Samson) I read each passage by line number. I read each hit in context to see who is speaking: the ancient author, a document he quotes, a translator's note, an editor's heading, or a bracket the editor supplied. I checked every factual sentence of each brief against its passage. Before accepting each absence claim or settled attribution I searched the whole Library (`cic/texts`) for the name, the manuscript, or the work: that search found three held files the drafts do not use (Liberatus's own Latin in PL 68; Nikodemos's Synaxaristes on Romanos; Migne's PG 99 and the Bollandists on the Vatican Menologion), and one held scholar's dating of the Life of Samson (Hugh Williams's Gildas). I compared each `records.json` entry with its brief and card. Readability came from `engine.m1.gates.grade_text`, run from the repo root. Every suggested brief fix below was applied to a scratch copy and re-scored; the post-fix word count and scores are given with each profile.

### Applies to all three

- **Audio = brief.** Each audio script matches its brief exactly once `[calmly] ` and `[warmly] ` are removed (checked by script). Each starts with `[calmly]` and has one `[warmly]`, before the closing paragraph. No tag appears in any brief or card. When a brief fix below changes the text, the audio script follows it.
- **Readability.** All three pass (FK at most 10, Flesch at least 60). Vigilius sits on the floor (Flesch 60.5), so every Vigilius fix below was tuned to keep it above 60.
- **Length.** Vigilius runs 405 words (2:30), at the cap. Romanos runs 322 (1:59) and Samson 325 (2:00). Every `briefLength` matches.
- **Card order.** All three follow Mark's order. Missing fields are left out; Samson has no keyWorks, since nothing of his own is held beyond a signature. Each `uncertain` list opens with the brief's main caveat.
- **Who test (item 14).** Vigilius has his Constitutum and letters in his own words. Romanos has his kontakia, held in Pitra's Latin. Samson is a founder known through his Life, which the brief marks as a book of miracles (the era 2 ruling on founders known through a biographer). The drafts carry no list lines; those belong to the map build and were not checked here.

| Profile | Words | Est. length @162 | FK | Flesch |
|---|---|---|---|---|
| Vigilius of Rome (major) | 405 | 2:30 | 8.2 | 60.5 |
| Romanos the Melodist | 322 | 1:59 | 7.2 | 73.6 |
| Samson of Dol | 325 | 2:00 | 6.4 | 73.3 |

---

### 1. Vigilius of Rome (major)

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | FAIL, blocking (B-B1, B-B2); minor (B-M3, B-M5) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | minor (B-M1, B-M2, B-M4, B-M6) |
| 5 | No role for a witness | PASS (Loomis, Duchesne, Mommsen, Hefele, Percival, Procopius named) |
| 6 | Partisan witness named and marked | FAIL, blocking (B-B1); minor (B-M2) |
| 7 | Contested both sides | FAIL, blocking (B-B2, records); minor (B-M3) |
| 8 | Common names placed | FAIL, minor (B-M5, card) |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | PASS (2:30, at the cap) |
| 11 | grade_text | PASS (Flesch 60.5, on the floor) |
| 12 | Card order, caveat repeated | PASS |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |

**Quotes and close tellings**
- The departure (l.1): Book of the Popes, tr. Loomis, "Augusta… sent Anthemius, the scribe… found Vigilius in the church of Saint Cecilia, November 22; for it was her birthday… brought him down to the Tiber and set him on a ship… the people commenced to throw stones after him and sticks and dirty vessels and to cry out: 'Your hunger go with you!'" (`liber-pontificalis_book-of-the-popes-v1_loomis1916.txt` l.11699–11721). The quote is exact. The LP names "Theodora Augusta" at l.11639. See B-M1.
- "We declare him to be a murderer" (l.3, card): l.11659–11660, exact, the Romans' accusation as the LP reports it.
- Loomis's notes (l.3, card): the life "is found to be full of inaccuracies and mistakes", Duchesne dating its author no earlier than Pelagius II (l.11536–11546); "The circumstances of Vigilius' departure from Rome are described nowhere else" (l.11734). Faithful.
- Procopius (l.5): "a suspicion arose against Silverius… that he was engaged in treasonable negotiations with the Goths, and Belisarius sent him immediately to Greece, and a little later appointed another man, Vigilius by name, to the office of chief priest" (`procopius_wars-5-6-gothic_dewing1919.txt` l.3473–3477). Exact.
- 537 (l.5): the continuation of Marcellinus, under "XV. ITERVM POST CONSVLATVM BELISARII", "Silverium Belisarius ab episcopatu summovit et loco eius Vigilium diaconum ordinavit" (`chronica-minora-2_…_mommsen1894.txt` l.8957–8959). The year is the chronicle's own post-consular year. Faithful.
- Liberatus (l.7): "asked him secretly to promise her that if he were made pope he would annul the synod of Chalcedon… seven hundred thousand sesterces. So Vigilius gladly gave his promise, desiring the bishopric and the gold" (Loomis l.11389–11400). Faithful; see B-M2 for the pronoun.
- The letter (l.7): Victor of Tunnuna copies it, to "Theodosio, Anthimo et Severo… iam pridem ab apostolica Sede damnatis… eam fidem, quam tenetis… et tenuisse me et tenere significo" (Mommsen l.18897–18910). Faithful.
- Mommsen (l.7, card): "Liberatus et Victor… acerrimi orthodoxae fidei defensores… iusto odio exacerbati in Vigilium inter malos pontifices Romanos fortasse pessimum ambo afferunt epistulam… sive vere ea a Vigilio scripta est sive, ut alii censent, ei supposita… sine dubio eo tempore publici iuris facta… cupide accepta" (l.17574–17582). The "perhaps the worst" is Mommsen's own clause. Faithful.
- Loomis on the letter (l.7, card): "Unless Vigilius be regarded as an absolutely unscrupulous doubledealer, the letter to Anthemius must be classed as a forgery… Duchesne, op. cit., p. 300, n. 9" (l.11683–11688). Faithful.
- Judicatum (l.9): "in 548, he issued a document, commonly called the Judicatum, anathematizing the three Nestorians but stoutly maintaining his adherence to the Council of Chalcedon" (Loomis l.11787–11791). Faithful.
- Hefele (l.11): "In accordance with the imperial command, but without the assent of the Pope, the synod was opened on the 5th of May A.D. 553" (`npnf214_seven-ecumenical-councils.xml` l.22877–22878). Percival calls him "Bishop Hefele" (l.1291, 15908). Faithful.
- Constitutum (l.11): "Dat. prid. Iduum Maiarum… anno XXVII… in Constantinopolitana ciuitate" (`collectio-avellana_…_guenther1895.txt` l.24223–24225); "eum nostra non audemus condemnare sententia sed nec ab alio quoquam condemnari concedimus", of "Theodori Mopsuesteni" (l.22360–22363). Faithful.
- Decretal (l.13, l.17): Percival's head note, "Some doubts have been expressed about its genuineness and Harduin is of opinion that the learned Jesuit, Garnerius… has proved its supposititious character. But the learned have not generally been of this mind but have accepted the letter as genuine" (l.24339–24343). "there ought to be no shame when what was at first omitted is made public after it is discovered by a further study of the truth… the blessed Augustine… retracted some of his own writings" (l.24385–24393), exact. The date "VI. Id. Dec.… the xijth year after the consulate of the illustrious Basil" (l.24490–24492) is the letter's own post-consular year, so "That December" holds.
- Death (l.15): "They came with Vigilius to Sicily, to the city of Syracuse, And he suffered from the malady of the stone and died" (Loomis l.11916–11918). Loomis's note: "A contemporary record says… 'the seventh day before the Ides of June in the third indiction (June 7, 555)' Duchesne" (l.11934–11937). See B-M3.
- Card: Percival on the West (l.24512–24526), exact in substance; Bossuet on the Constitutum (l.22962–22974); Loomis "which lasted seventy years" (l.11797–11798), exact; the maltreatment "partly legendary" (l.11834).

**Findings**
- **B-B1 BLOCKING (items 1, 6; a witness's character told wrongly).** Brief l.3: "Its life of Vigilius is hostile and reports Romans calling him a murderer." Card `remembered` 1: "The Book of the Popes gives a hostile life of him: Romans call him a murderer, the crowd throws stones after his ship, and he is dragged from an altar at Constantinople." Card `uncertain` 1 and the records claim ("the Book of the Popes' report, hostile to him") say the same. No held scholar calls the life of Vigilius hostile, and its text is mixed. It reports the Romans' charges and the crowd's curses (l.11655–11664, 11718–11721), but it also has Vigilius refuse Theodora to her face, "Far be this from me, Lady Augusta… I do assuredly refuse to restore a man who is a heretic… I am the vicar of blessed Peter" (l.11646–11651), and says that at Constantinople "Vigilius would not yield to them but preferred to die virtuously than to live" (l.11761–11762). The dragging from the altar is told as his suffering at the empire's hands, not as a charge against him. The partisan account Loomis does mark is the Silverius life: a later writer "more sympathetic" to Silverius (l.11328–11338, citing Duchesne), whose story has Vigilius take Silverius "as if in his own charge" into exile (l.11443–11470). Loomis's general verdict is that this portion of the book "is often fraudulent, often partisan" (l.575–576). Telling the listener the Vigilius life is hostile misplaces the bias and hides that the same book shows him defying the empress.
  - Fix, brief l.3: "The scene comes from the Book of the Popes, a record of the popes' lives. Its life of Vigilius tells of Romans who called him a murderer. It also shows him stand up to the empress. Louise Loomis, its translator, finds the life full of mistakes and the scene told nowhere else." (Dropping "Roman" before "record" saves a word.)
  - Card `remembered` 1: "The Book of the Popes gives a mixed life of him. Romans call him a murderer and the crowd throws stones after his ship, but he refuses the empress and, at Constantinople, is dragged from an altar rather than yield. Loomis judges that last account partly legendary." Card `uncertain` 1: "The scene of his leaving Rome comes from the Book of the Popes, which Loomis finds full of mistakes and calls often partisan in this part; she says the scene is told nowhere else. Louis Duchesne, whom Loomis follows, argues…" (rest as is).
  - Records: change the witness note on "The Romans accuse Vigilius of murder" to "the Book of the Popes' report; Loomis calls this part of the book often partisan (l.575–576)".
- **B-B2 BLOCKING (items 1, 7; a false "only").** Card `uncertain` 4: "the Book of the Popes says only that he was exiled and died a confessor." The LP says more, and against Vigilius: "Vigilius, the archdeacon, took Silverius as if in his own charge, and sent him into exile to Pontiae and fed him with the bread of tribulation and the water of bitterness. And he fell ill and died a confessor" (Loomis l.11443–11471). The card makes the LP look silent on Vigilius's part where it names him. The records tag the claim Contested but give it no `contested_claim`, which the pattern's Confidence section requires.
  - Fix, card `uncertain` 4: "The death of Silverius. Liberatus, as Loomis gives him, says Silverius was handed to Vigilius's guards and starved on the island of Palmaria. The Book of the Popes says Vigilius took him into his own charge, sent him into exile and fed him 'the bread of tribulation', and that he died a confessor. Loomis judges the guilt to rest partly on Antonina, the wife of Belisarius, and partly on Vigilius."
  - Records: add a `contested_claim`, "Vigilius's part in the death of Silverius": Liberatus (Breviarium 22, PL 68 l.81613–81617, via Loomis l.11484–11488) and the LP's Silverius life (l.11443–11470) put him in charge of Silverius; Loomis (l.11492–11493) divides the guilt between Antonina and Vigilius; Procopius's Secret History, as Loomis reports it (l.11488–11491), names Antonina.
- **B-B3 BLOCKING (records; a false absence).** `absent_details` 3: "the Latin Breviarium is in liberatus-victor-tunnunensis-primasius-junillus-pl68-lat_migne1866.txt but chapter 22 was not located in its OCR." It is there: "CAPUT XXII. De Silverio et Vigilio" (l.81553–81554), with "Augusta vero vocans Vigilium Agapeti diaconum, profiteri sibi secreto ab eo flagitavit, ut si papa fieret, tolleret synodum, et scriberet Theodosio, Anthimo et Severo" (l.81585–81590), Silverius "traditus est duobus Vigilii defensoribus… in Palmariam insulam adductus, sub eorum custodia defecit inedia" (l.81613–81617), and the letter (l.81621–81640). The editor's note beside it says Liberatus tells the story in its own chapter "ut Vigilio trium capitulorum damnatori tanto majorem faciat invidiam, quanto iniquiorem ejus primam ordinationem ostendit" (l.81654–81657): a held editor marking Liberatus's account as aimed against Vigilius.
  - Fix, records: delete the absent detail. Cite Liberatus from PL 68 l.81553–81640 beside Loomis's English, and add the PL 68 note (l.81654–81657) as a second witness to Liberatus's bias beside Mommsen. Card `sources.about`: add "Breviarium, ch. 22 (Latin, PL 68, ed. Migne)" with that file. The brief needs no change; its quotation of Liberatus is through Loomis and matches the Latin.
- **B-M1 MINOR (item 4; pronoun).** Brief l.1: "an officer sent by the empress Theodora found Pope Vigilius in her church in Rome." The nearest "her" is Theodora. Fix: "On 22 November, Saint Cecilia's feast, an officer sent by the empress Theodora found Pope Vigilius in Cecilia's church in Rome."
- **B-M2 MINOR (items 4, 6; pronoun in the sentence that tells a partisan witness).** Brief l.7: "Liberatus of Carthage says Theodora had him promise in secret to set aside the Council of Chalcedon, and offered him gold." The shared subject of "offered" reads as Liberatus. Fix: "…to set aside the Council of Chalcedon, and that she offered him gold."
- **B-M3 MINOR (items 1, 7; an editor's year as the record's, and one side of a recorded dispute).** Brief l.15: "Loomis reports a record of the time giving 7 June 555." The record gives "the seventh day before the Ides of June in the third indiction"; "(June 7, 555)" is the bracket in Loomis's note from Duchesne (l.11934–11937). Percival gives "the end of 554 or the beginning of 555" (l.24512–24513), and the records hold the date as a `contested_claim`. A chronicle note Mommsen prints with Marcellinus also puts the death in "Indictione II. XIII p. c. Basilii" (l.3260–3263). The brief gives one side. The records tag the Loomis side Widely Accepted and the Percival side Contested, two tags for one dispute. The card's `dates` and `uncertain` 6 already hold both sides.
  - Fix, brief: delete "Loomis reports a record of the time giving 7 June 555." (the card keeps the dates). Records: tag both death-date claims Contested, note that 555 is the reckoning of the third indiction in Loomis's note from Duchesne, and add the Marcellinus note (l.3260) to the `contested_claim`.
- **B-M4 MINOR (item 4, card; pronoun).** Card `knownFor`: "Bishop of Rome from 537 to 555, made pope in place of Silverius, who was held at Constantinople through the quarrel…" reads as Silverius held at Constantinople. Fix: "Bishop of Rome from 537 to 555. Made pope in place of Silverius, he was held at Constantinople through the quarrel over the Three Chapters and the council of 553, first resisting their condemnation, then condemning them, then defending them, and at last condemning them."
- **B-M5 MINOR (items 1, 8, card).** Card `dates`: "Made pope in 537… (the continuation of Marcellinus's chronicle and the Book of the Popes; Procopius gives no year)". The LP's life of Vigilius gives no year; 537 and "March 20, 537" are Duchesne's, in Loomis's notes (l.11352–11353), and the heading "(537-555)" is Loomis's. This is also the card's first mention of Marcellinus and of Procopius, both common names (Procopius of Gaza wrote in the same years). Fix: "Made pope in 537, when Belisarius removed Silverius (the continuation of the chronicle of Marcellinus Comes; Louis Duchesne, as Loomis reports, gives 20 March 537; Procopius of Caesarea gives no year)."
- **B-M6 MINOR (item 4; a referent two paragraphs back).** Brief l.17: "In that letter Vigilius pointed to Augustine of Hippo". The letter was last named at l.13, before the paragraph on his death, and l.7 tells another letter. Fix: "In that letter to Eutychius, Vigilius pointed to Augustine of Hippo, who had corrected his own writings."
- Length with B-B1 and B-M1, M2, M3, M6: 403 words (2:29), FK 8.1, Flesch 61.1.

---

### 2. Romanos the Melodist

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | FAIL, blocking (B-B4) |
| 2 | Quotes verbatim | PASS ("Aperi nobis", "Humilis Romani", Pitra's title, checked) |
| 3 | No invention | PASS |
| 4 | Reading aids | minor (B-M8) |
| 5 | No role for a witness | PASS (Pitra, Cross named) |
| 6 | Partisan witness named and marked | PASS (none used; the notice is marked a saint's story) |
| 7 | Contested both sides | FAIL, blocking (B-B4, B-B5) |
| 8 | Common names placed | FAIL, minor (B-M7) |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | PASS (1:59) |
| 11 | grade_text | PASS |
| 12 | Card order, caveat repeated | PASS |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |

**Quotes and close tellings** (`romanos-melodist_cantica-grc_pitra1888.txt`)
- The dream (l.1): the notice in Pitra's Latin, "dormienti ei apparuit in somnis sanctissima Deipara, chartaeque rotulum tradidit, inquiens: « Accipe chartam et comede eam »… Erat vero festum sanctorum Christi natalium… admiratione plenus… Tum conscenso ambone, psallere caepit: Virgo parit hodie supersubstantialem Filium" (l.6811–6831). Faithful.
- The source (l.3): "Ex Menologio imperatoris Constantini Porphyrogeniti… sub num. 1613… etiam nimis breve continet S. Romani elogium, de quo alibi nihil fere amplius commemoratur" (l.6791–6797). Faithful to Pitra; see B-B4. Cross: "Constantine Porphyrogenitus (reg. 944-959)" (`russian-primary-chronicle_cross1930.txt` l.6708). "Cardinalis Pitra" (l.673).
- The life (l.5): "ex Syria ortus, sanctae ecclesiae Beryti diaconus… temporibus Anastasii imperatoris, commoratus est in templo sanctissimae Dei genitricis, in aedibus Cyri… agere pervigilium Blachernarum solitus… aliorum etiam festorum contacia ad mille scripsisset, migravit ad Dominum" (l.6811–6833). Note 5: the roll "quae contacio nomen suum dedit" (l.6845–6849). Faithful.
- Which Anastasius (l.7): "Utrum primus an secundus Anastasius imperator intelligendus sit… ex ipso tertio contacio" (l.6808, 6836–6838); "Sed pleraque vix concurrunt cum brevissimo Anastasii II. imperio, a. 713-716, neque omnino liquet an Romanus tunc floruerit" (l.8241–8246). Faithful.
- The poems (l.9, l.11, card): "Ex insula Patmo… missa… plurima poemata, nomine sancti Romani ornata… Ex his tria selegimus" (l.6965–6970); headings "De sancto Stephano protomartyre. Acrostichis: Humilis Romani" (l.6923–6929), "De casto Josef… acrostichis: Alphabetum Romani" (l.7399–7400), "De decem virginibus. Acrostichis: Humilis Romani" (l.8079–8082); refrain "Ne foris maneamus, clamantes: Aperi nobis!" (l.8085–8086), recurring (l.8091, 8222). "Sicut Romani duo sunt de Iosepho cantica" (l.8099–8100) supports the card's two poems on Joseph; "solus enim magnus est Dominus salvator noster" (l.7411) its refrain. Title "SANCTUS ROMANUS veterum melodorum Princeps" (l.309). All exact.

**Findings**
- **B-B4 BLOCKING (items 1, 7; an attribution told as settled that held files contradict).** Brief l.3: "It was made for the emperor Constantine Porphyrogenitus, who reigned from 944 to 959, as Samuel Cross dates him." Pitra's attribution (l.6791) is told as fact. Held files give the same manuscript, Vatican 1613, to the emperor Basil. Migne's edition of Theodore the Studite heads an extract "Ex Menologio Basilii imperatoris. Cod. Vatic. n. 1613" (`theodore-studite_opera-omnia-pg99-grc-lat_migne1860.txt` l.7839). The Bollandists cite "Menologio Graecorum, jussu Basilii Porphyrogeniti Imperatoris seculo Christi decimo conscripto" (`acta-sanctorum_martii-tomus-3-lat-grc_palme1865.txt` l.180301–180302), and Assemani the same (`assemani_…tomus3-pars2…1728.txt` l.39715–39716). The illustrated Vatican menologion is called "the menologion of Basilius II (976-1025) in the Vatican Library" in `studia-biblica-et-ecclesiastica-v5-life-of-st-nino_wardrop1903.txt` l.16382–16386. Pitra's own note 3 corrects "editio Urbini 1727" (l.6840), the printed edition of this Menologion. The card repeats Pitra's attribution (`uncertain` 1, with Cross's dates), and the records tag it Widely Accepted.
  - Fix, brief l.3: "The story comes from one short notice in a Menologion, a book of saints for the church year. Cardinal Jean-Baptiste Pitra, who printed it in 1888, calls it the Menologion of the emperor Constantine Porphyrogenitus. Migne's edition of Theodore the Studite gives the same Vatican manuscript to the emperor Basil. Pitra says almost nothing more is recorded of Romanos anywhere."
  - Card `uncertain` 1: "His life rests mainly on one short notice in a Menologion, a book of saints for the church year. Pitra calls it the Menologion of the emperor Constantine Porphyrogenitus, who reigned from 944 to 959 in Samuel Cross's dates; Migne's Theodore the Studite and the Bollandists give the same Vatican manuscript, number 1613, to the emperor Basil. It is a saint's story, and Pitra says almost nothing more is recorded of Romanos anywhere." Add PG 99 and Acta Sanctorum Martii III to `sources.about`.
  - Records: the claim becomes Pitra's, tagged Contested, with a `contested_claim` ("Whose Menologion holds the notice": Pitra l.6791 against PG 99 l.7839, AASS Mart. III l.180301, Assemani l.39715, the Studia Biblica essay l.16386).
- **B-B5 BLOCKING (items 1, 7; a false absence, and a held side missing from a dispute).** Records `absent_details` 3: "no other held file was found that tells his life". `nikodemos-hagiorite_synaxaristes-vol1-sep-feb-grc_1900.txt` holds a Greek notice of Romanos, "poet of the Kontakia" (OCR "ΡΩΜΑΝΟΥ τοϋ χουμοϋ των Κοντακίων"), under 1 October (l.13987–14063). It gives his home city as Emesa (OCR "'Εαεσαν, ή ότοία τώρα λέγεται τουρκιστί Έμσ", that is Emesa, now called Homs in Turkish; l.13994–13995), the Berytus diaconate, and his coming to Constantinople "κατά τους χρόνους Αναστασίου τοΰ βασιλέως έν έτε:" with a year the OCR shows as "υν-' 196" (l.13998–13999). That reads as 496 in Greek numerals (υϟϛ'), under the first Anastasius; check the page before quoting it. It retells the dream, the ambo and the thousand kontakia (l.14029–14062), and its footnote reports Nikephoros Xanthopoulos's story that Romanos was at first unmusical and mocked (l.14004–14036). This notice is later and draws on the same tradition. Even so, the brief's "Which Anastasius is meant is unclear" (l.7), the card's `dates`, `place` ("From Syria") and `uncertain` 2, and the records' `contested_claim` all leave out a held witness that names the emperor and the year. Pitra's own lean (most signs "vix concurrunt" with Anastasius II, l.8241) also points the same way.
  - Fix, brief l.7: "Pitra asks which Anastasius is meant, the first or the second, and looks for clues in one of the poems. He says it is not at all clear that Romanos lived under the second, who reigned from 713 to 716. A later Greek book of saints, revised by Nikodemos the Hagiorite, gives the year 496, under the first."
  - Card `place`: "From Syria; from Emesa, by the later Greek book of saints that Nikodemos revised; a deacon of the church at Berytus…". Card `dates`: add "The later Greek book of saints revised by Nikodemos the Hagiorite gives 496, under the first." Card `uncertain` 2: add that sentence and that this book is much later than the Menologion. Add the Synaxaristes to `sources.about` (Greek; ed. Nikodemos the Hagiorite, reissued 1868).
  - Records: delete `absent_details` 3, or reword it to "No witness older than the Menologion notice is held; Nikodemos's Synaxaristes (l.13987–14063) is later and follows the same tradition." Add the Synaxaristes side (496, Anastasius I; Emesa) to the `contested_claim` on which Anastasius.
- **B-M7 MINOR (item 8).** Brief l.1, first mention: "came to Romanos in his sleep". Romanos is a common name (the Synaxaristes alone has several emperors Romanos, l.15470, 38872), and the record's epithet identifies him. Fix: "the Mother of God came to Romanos the Melodist in his sleep."
- **B-M8 MINOR (item 4; the Library's process in participant text, Style Guide 1.11).** Brief l.9: "Only his Latin prose can be read in the scanned copy, since the Greek did not survive the scan." Card `uncertain` 3: "known here only in Pitra's Latin prose… could not be read in the scanned copy." A listener has no "scanned copy"; the sentence reports the project's OCR. The honest limit stands, said in the world's terms. Fix, brief: "He set a Latin prose version beside the Greek, and the words here are from it." Card `uncertain` 3: "The poems are quoted here only in Pitra's Latin prose version, not in Romanos's Greek."
- Length with B-B4, B-B5, B-M7 and B-M8 (and dropping l.5's last sentence, "Pitra notes that the roll in the dream gave the kontakion its name.", which the card's `remembered` 2 keeps): 326 words (2:01), FK 7.8, Flesch 69.4.

---

### 3. Samson of Dol

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | minor (B-M10, B-M11) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | minor (B-M12) |
| 5 | No role for a witness | PASS (Taylor, Duine, Fawtier, Loth, Maassen named) |
| 6 | Partisan witness named and marked | PASS (the Life marked as a book of miracles) |
| 7 | Contested both sides | minor (B-M13, card and records) |
| 8 | Common names placed | FAIL, minor (B-M9) |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | PASS (2:00) |
| 11 | grade_text | PASS |
| 12 | Card order, caveat repeated | minor (B-M14) |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |

**Quotes and close tellings** (`samson-of-dol_life-of-st-samson_taylor1925.txt`)
- The scene (l.1): Life I.48, "a certain district which they call Tricurius… men worshipping a certain idol after the custom of the Bacchantes, by means of a play in honour of an image… on the summit of a certain hill, an abominable image. On this hill I myself have been and have adored and with my hand have traced the sign of the cross which St. Samson with his own hand carved by means of an iron instrument on a standing stone… selecting two only of the brothers… gently admonished them" (l.3874–3894); Taylor's note, "the Hundred of Trigg in Cornwall" (l.3900). Faithful.
- Eltut (l.3): "the school of the famous master of the Britons, Eltut by name… Eltut was of all the Britons the most accomplished in all the Scriptures" (l.2337–2341). The career follows Taylor's sketch (l.455–495) and the Life (l.4040–4048, dove l.2595–2611, burial at Dol l.4286–4289). Faithful. Taylor says "His birthplace is not given" (l.445); the card's "Of Demetia… by the Life" rests on "Saint SAMSON, then, was of the country of Demetia" (l.2091), which is a country, not a birthplace, so both hold.
- Sources of the Life (l.5): "O most blessed Tigernomalus, bishop of an apostolic see, hast asked me" (l.1916–1918); the old man "being himself a cousin of St. Samson and a deacon… the said holy deacon, Henoc by name, had brought from beyond the sea" (l.1985–1996). See B-M10. "Its writer gives no name": Taylor, "our anonymous writer" (l.538), "The anonymous author" (l.1615), "the work of the anonymous writer as that of Henoc's nephew" (l.1716–1719). No held file names him.
- The date (l.7): Duine, "no trace of any literary composition subsequent to the end of the sixth century… the first is a convincing argument in favour of the date 610-615" (l.728–743); Fawtier "charge[d] our author with untruthfulness and… declare[d] his work spurious… M. Fawtier has been answered by the Abbé Duine and Professor Loth" (l.567–575); Fawtier "does not accept the anonymous writer's statements respecting its authorship and provenance" (l.1652–1654). See B-M11.
- The council (l.9): "CONCILIUM PARISIENSE A. 556—573" (`concilia-aevi-merovingici-mgh-concilia-1-lat_maassen1893.txt` l.11525, 11838); "Samson subscripsi et consensi in nomine Christi" (l.11857), exact; note "ep. Dolensis (?)" (l.11869–11870); index "Samson ep. Dolensis" (l.20493). Faithful.
- The close (l.11): "the Life of St. Samson actually furnished the mould into which many of them were cast. Not only did the successors of our anonymous writer seek to rival him in the number and extent of the miracles they related" (l.535–540). Exact.
- Card: Hiltbert and Judual (l.4063–4074), the Fowey and Southill churches (l.1729–1732), pilgrimages "from Britain no less than from Brittany… to his sarcophagus at Dol" (l.1517–1520), the Vita Iltuti, "Samson videlicet, Paulinus, Gildas et Dewi" (`rees_…1853.txt` l.7949–7950); Rees puts these Lives "probably about the twelfth century" (l.322–323), which supports "later". Taylor's 521 and 486 (l.448–455). All faithful.

**Findings**
- **B-M9 MINOR (item 8).** Brief l.1, first mention: "Samson heard people worshipping". Samson is a name the Library holds for other people, among them the biblical judge and Samson, son of King Chilperic, in Gregory of Tours (`gregory-tours_history-of-the-franks-v2_dalton1927.txt` l.9407). The pattern gives the subject's own name its place too. Fix: "In Cornwall, in a district called Tricurius, Samson of Dol heard people worshipping an idol with a play."
- **B-M10 MINOR (item 1).** Brief l.5: "and from writings of the deacon Henoc." Card `uncertain` 1: "on writings of the deacon Henoc." The Life says the accounts were ones "the said holy deacon, Henoc by name, had brought from beyond the sea" (l.1994–1996), read aloud to the writer. It does not say Henoc wrote them; the records have it right ("accounts the deacon Henoc had brought"). Fix, brief: "and from accounts the deacon Henoc brought." Card: "and on accounts the deacon Henoc brought from overseas."
- **B-M11 MINOR (item 1).** Brief l.7: Fawtier "rejected what its writer says of his sources." Taylor reports that he rejected "the anonymous writer's statements respecting its authorship and provenance" (l.1652–1654), which is wider than his sources. The card has it right ("authorship and origin"). Fix: "and rejected what its writer says of its authorship and origin."
- **B-M12 MINOR (item 4).** Brief l.9: one sentence of 37 words ("Among the bishops who signed… in the name of Christ."). Fix: "Friedrich Maassen dates a council at Paris between 556 and 573. One of its bishops signed, "Samson subscripsi et consensi in nomine Christi": I, Samson, have signed and agreed, in the name of Christ."
- **B-M13 MINOR (item 7, card and records).** The dispute over the Life's date gives one dated side (Taylor and Duine, 610 to 615) and Fawtier with no date; the records say Fawtier's date is not held, which is true. A held scholar does give a range. Hugh Williams, editing Gildas, writes: "The Vita Samsonis cannot be anterior to the seventh century, because the writer is familiar with the Homilies of Gregory I… neither can it be later than Nominoe, that is, than 824" (`gildas_de-excidio-britanniae-lorica-penitential-lat-eng_williams1899.txt` l.18737–18740). He also says "older biographies supplied the basis for the Life of Samson" (l.18811). The brief can stay as it is. Fix, card `uncertain` 2: add "Hugh Williams, editing Gildas in 1899, puts it no earlier than the seventh century and no later than 824." Records: add Williams to the `contested_claim` sides and to `sources.about`.
- **B-M14 MINOR (item 12, card).** The council signature is the only line in Samson's own words. The records say so ("No writing of his own is held beyond the council signature"), yet the card lists Maassen only under "Written about them" and has no `ownWords`. Fix: add `sources.ownWords` with one entry, "Signature at the council of Paris, 556 to 573, if the signer is he (in Concilia aevi Merovingici, ed. Friedrich Maassen)", Latin, the Maassen file. Keep Maassen's note and index under `about`.
- Length with B-M9 to B-M12 (and "He died and was buried at Dol." for "He died at Dol and was buried there."): 325 words (2:00), FK 6.2, Flesch 73.4.

---

### Totals, part B

| Profile | Blocking | Minor |
|---|---|---|
| Vigilius of Rome | 3 (B-B1, B-B2, B-B3) | 6 (B-M1 to B-M6) |
| Romanos the Melodist | 2 (B-B4, B-B5) | 2 (B-M7, B-M8) |
| Samson of Dol | 0 | 6 (B-M9 to B-M14) |
| **Part B** | **5** | **14** |

## Part C

Reviewer: independent, first sight of these drafts. Profiles: `mar-aba-i` (major), `cosmas-indicopleustes`, `barsanuphius-and-john-of-gaza` and `cyril-of-scythopolis`, with their cards, audio scripts and entries in `records.json`, and the batch `README.md`. Files are in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era3/batch3/`. Bar: `Who_Profile_Pattern.md` review checklist 1 to 14 and the standards it points to; `CLAUDE.md` "Trust and source fidelity" and "Accessible and rigorous"; Mark's length rulings as the earlier era 3 reviews apply them (majors capped at 2:30, about 405 words, a cap and not a target; non-majors 1 to 2 minutes, at most about 325 words). Brief line numbers refer to the `.brief.txt` files, where each paragraph is one line and blank lines count (paragraphs sit on l.1, 3, 5, 7 and so on). Other line numbers point to files under `cic/texts/`.

Method. I searched every quotation in the four briefs and cards in the vendored file the card or records cite, with a search that collapses whitespace, folds quote marks and accents and lets OCR split letters. For the OCR files (Chabot's Synodicon, Gismondi's Mari, Abbeloos and Lamy's Bar Hebraeus, Migne's PG 88, Cotelier's Monumenta II, Kugener's PO 2, Nau's PO 8) I read each passage by line number. I read each hit in context to see who speaks: the ancient author, a document he quotes, a later compiler, an editor's notice reprinted from another editor, a translator's note, or a bracket. I checked every factual sentence of each brief against its passage. Before accepting any absence claim I searched the whole Library (`cic/texts`) for the person; that search turned up three held witnesses the drafts do not use and that their absence claims deny: Oskar Braun's German translation of the Life of Mar Aba, J. Labourt's history of the Persian church, and Evagrius Scholasticus on Barsanuphius. I compared each `records.json` entry with its brief and card, and the README with the era 3 scan, the census (`cic-website/data/world-census.json`) and the batch 1 and batch 2 READMEs. Readability came from `engine.m1.gates.grade_text`, run from the repo root. Length assumes 162 words a minute. Every suggested brief fix was applied to a scratch copy and re-scored. I did not edit the drafts, made no paid or model-API calls and used no web.

### Applies to all four

- **Audio = brief.** Each audio script matches its brief exactly once `[calmly] ` and `[warmly] ` are removed (checked by script). Each starts with `[calmly]` and has one `[warmly]`, before the closing paragraph. No tag appears in a brief or card. When a fix below changes the closing paragraph (Mar Aba), the audio script follows it.
- **Readability.** All four pass. Narrator sentences past 25 words: Mar Aba l.9 (27) and l.13 (26), M7. The other long ones in Cosmas are quotation.
- **Length.** Mar Aba runs 404 words (2:30), at the cap. The others run 320 to 324 (about 2:00). Every `briefLength` matches.
- **Card order.** All four follow Mark's order; missing fields are left out; keyWorks never passes three; each `uncertain` list opens with the brief's main caveat.
- **Who test (item 14).** Mar Aba has the synod's documents and letters issued in his name. Cosmas and Cyril are recorders whose books are main sources (scan rows 57, 63). Barsanuphius and John have the held answers and a following (Dorotheus).

| Profile | Words | Est. length @162 | FK | Flesch | After fixes |
|---|---|---|---|---|---|
| Mar Aba I (major) | 404 | 2:30 | 6.8 | 72.1 | 402 words, 2:29, FK 6.6, Flesch 72.3 |
| Cosmas Indicopleustes | 320 | 1:59 | 7.3 | 68.7 | brief unchanged |
| Barsanuphius and John of Gaza | 324 | 2:00 | 6.2 | 72.4 | 321 words, 1:59, FK 6.3, Flesch 71.8 |
| Cyril of Scythopolis | 324 | 2:00 | 6.8 | 70.3 | 322 words, 1:59, FK 6.7, Flesch 70.7 |

---

### 1. Mar Aba I

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | FAIL, blocking (C-B1); minor (C-M1, C-M2, C-M3, C-M5) |
| 2 | Quotes verbatim | PASS (the brief quotes nothing directly; close tellings checked below) |
| 3 | No invention | PASS |
| 4 | Reading aids | minor (C-M7) |
| 5 | No role for a witness | PASS |
| 6 | Partisan witness named and marked | PASS (Bar Hebraeus "of the rival Syriac Orthodox church") |
| 7 | Contested both sides | FAIL, blocking (C-B2) |
| 8 | Common names placed | PASS (Joseph, Samuel, Narses, Elisha, Ezekiel, Thomas all carry a role or place) |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | PASS (2:30, at the cap) |
| 11 | grade_text | PASS |
| 12 | Card order, caveat repeated | PASS (but see C-B1, C-B2, C-M4, C-M6 on card fields) |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |

**Close tellings** (`synodicon-orientale_..._chabot1902.txt` unless named)
- Kashkar (l.1): "il descendit au pays de Kaškar ... se réunirent près de lui, à la ville de Zizwarda ... tous les gens de Kaskar se mirent d'accord ... Mar Samuel ... qui se disputaient mutuellement l'épiscopat dans le temps de la discorde ... destitués de tout titre ... et ils se soumirent avec grande joie à Mar Samuel ... accomplissant ... les fonctions presbytérales" (l.21158-21173). Faithful.
- Election (l.3): Chabot's note, Kosrau's 13th year "décembre 543-janvier 544 ... un document du mois de février 540 (p. 320) ... nous devons conclure qu'il fut élu au mois de janvier" (l.20941-20948); the p.320 document is the synod's first, dated in Kosrau's 10th year, which Chabot reads as October 540 (l.21062-21065, 21106). "From the synod's own dates" holds.
- Mari (l.5, l.11, l.15): "Mar Abba Magnus magus fuerat suae religionis tenacissimus ... a Josepho quodam scholastico ... quum id abnuisset ... exortis flatibus traiectio impeditur" (Gismondi l.14092-14099); "Mar Abbam invidia prosecuti sunt magi propterea quod de eorum genere erat eorumque instituta mutaverat ... in carcere itaque septem annis detentus est Adorbigani sui gregis sollicitudinem gerere non cessans ... 'si meam vis nocem [necem] occido [occide] me'" (l.14016-14024); "eumque Hirtam detulit Qyura discipulus eius ... coenobium super eius sepulcrum exstruxit" (l.13997-13999); two altars (l.14069-14070). See C-M1, C-M2, C-B2.
- Chabot's outline (l.7): "Nous possédons une assez longue histoire de Mar Aba, éditée par P. Bedjan ... qui aurait besoin d'un examen critique minutieux ... Né dans la religion de Zoroastre, il reçut le baptême à Hira, étudia à l'École de Nisibe, puis se rendit à Édesse, où il apprit le grec de son disciple Thomas ... il retourna à Nisibe où il se fit connaître comme un professeur distingué" (l.20963-20979). See C-B1, C-B2.
- Synod and letter (l.9): "la dualité du patriarcat introduite par Mar Élisée et Mar Narsé eut totalement cessé" (l.20923-20925); "comme un lien d'amour de l'union chaste et légitime de l'homme et de la femme" (l.22276, OCR "Funion", "Fhomme"); "de s'approcher de la femme de leur père ... comme les mages" (l.22289-22297). See C-M3.
- Death (l.13): Chabot, "Selon l'auteur de sa Vie, il retrouva ensuite les faveurs du roi et mourut en paix sur son siège. Mais, d'après Bar Hébréus, étant revenu à Séleucie malgré la défense du roi, il fut jeté en prison et y mourut ... en l'an 552 (d'après les Actes du synode de Mar Joseph)" (l.20993-20997, 20930-20932); Bar Hebraeus, "rediit Seleuciam: quod ubi audivit rex eum catenis ligatum inclusit, atque ille in carcere e vita discessit" (Abbeloos-Lamy l.5518-5523); "Sedit Abas ab anno 538 ad annum 552" (l.5254). Faithful. "Les Nestoriens l'honorent comme un saint" (l.20935). Faithful.
- Card `remembered` 3 and `uncertain` 5 on Patricius: McCrindle, "from the Catalogue of the Nestorian Patriarchs it has been clearly proved that Patricius, who was a Magian and was called by the Syrians Abas or Mar-Abas, became Bishop Catholic" and Montfaucon's other reading (`cosmas_..._mccrindle1897.txt` l.2557-2563). Faithful. (Labourt and Braun make the same identification, Labourt l.9667-9669 "ce point n'est pas sûr" on the name only; Braun l.10898-10903.)
- Namesakes: Mari's "post obitum Mar Abae" at l.13942 is the notice of his successor Joseph; Bar Hebraeus's Abas succeeds Paul (l.5224-5225); no namesake (Mar Aba II, the archdeacon, Aba of Kashkar) is merged.

**Findings**

- **C-B1 BLOCKING (items 1, 12; false absence: the Life of Mar Aba is held).** Card `uncertain` 1: "Chabot summarises a longer Life, edited by Paul Bedjan and not held in the Library". Records `absent_details` 1: "Paul Bedjan's edition (1895) is not held; everything from it comes through Chabot's summary. The census entry also cites Oskar Braun's German and Richard Payne's English excerpts; neither was checked here." The Life itself is held, whole, in Braun's German: `persian-martyr-acts_ausgewahlte-akten-persischer-martyrer-bkv22-deu_braun1915.txt`, "XX. Geschichte der wunderbaren und göttlichen Kämpfe des heiligen Zeugen Mär Abä" (l.10660-12360), introduced as "Das unblutige Martyrium des Patriarchen Mär Abä, 540-552 ... Bedjan, Histoire, S. 206 ff." (l.833-839). J. Labourt's held history also retells the Life chapter by chapter with Bedjan's page numbers, "Les sources de la Vie de Maraba sont: Bedjan ... Vie de Maraba, p. 206-274" (`labourt_le-christianisme-dans-l-empire-perse-sassanide-fra_1904.txt` l.9502-9506, the reign at l.9479-11010), and judges its author "réellement, comme il le prétend, un disciple du catholicos" (l.9559-9562). Neither is used. The Life changes what the brief can say: it makes him a pagan official, "machten sie ihn zum Arzabed" (Braun l.10678; Labourt l.9488-9492, "naquit dans une famille mazdéiste ... entra dans la carrière administrative"), baptized "im Dorfe 'KD" (Braun l.10826; Labourt l.9556, "Au bourg d''Akda, d'après sa Vie ... à Hira, d'après Mare"), dying of illness near the church of Bet Narkos "am Freitag der zweiten Fastenwoche" (Braun l.12290, 12318-12322) and buried "bis zum Kloster von Seleucia" (l.12350-12355). The records' second absence, "His birth year and family: No held source gives them", is also partly false: Labourt gives his home district and his Mazdean family (l.9483-9488).
  Fix, card `uncertain` 1: "His life outside the synod's record rests on later accounts. His Life, by a disciple in J. Labourt's judgment, is held in Oskar Braun's German translation from Paul Bedjan's Syriac; Chabot says it needs careful critical study and lacks dates. Mari ibn Sulayman wrote in the 1100s and tells the conversion as a wonder." Card `sources.about`: add {"title": "History of the struggles of the holy witness Mar Aba (German tr. Oskar Braun)", "author": "Anonymous disciple", "date": "1915", "language": "German translation", "file": "cic/texts/persian-martyr-acts_ausgewahlte-akten-persischer-martyrer-bkv22-deu_braun1915.txt"} and {"title": "Le christianisme dans l'empire perse", "author": "J. Labourt", "date": "1904", "language": "French", "file": "cic/texts/labourt_le-christianisme-dans-l-empire-perse-sassanide-fra_1904.txt"}. Records: replace `absent_details` 1 with "The Syriac of Bedjan's edition is not held; the Life is held in Braun's German (l.10660-12360) and retold by Labourt (l.9479-11010). Payne's English was not checked." Change `absent_details` 2 to "His birth year: no held source gives it. Labourt gives his home on the Tigris opposite Hale, in the district of Radan, and his Mazdean family (l.9483-9488)." Add claims, Documented as the Life's own account and Dominant Modern Reconstruction for Labourt: the Life's pagan official made Arzabed (Braun l.10670-10678), baptism at the village of 'KD / Akda (l.10826; Labourt l.9556), death of illness on the Friday of the second week of Lent near Bet Narkos (l.12290, 12318-12322), burial at the monastery of Seleucia (l.12350-12355), nine years' captivity (l.12238); Labourt's date of death, 29 February 552 at Seleucia (l.10930-10931, 11008). The brief fix is in C-B2.

- **C-B2 BLOCKING (items 1, 7; two contested places told one way).** (a) Baptism. Brief l.7 tells Chabot's outline, "Aba baptized at Hira", as the Life's story, and card `place` gives "Hira ... in his early years" flat. The Life puts the baptism at the village of 'KD (Braun l.10826); Labourt sets the two side by side, "Au bourg d''Akda, d'après sa Vie, p. 211; à Hira, d'après Mare" (l.9556). (b) Burial. The closing paragraph (l.15) gives only Mari's burial at Hira. The Life buries him at the monastery of Seleucia (Braun l.12350-12355), and Braun's note sets Mari against it, "Nach Mare, S. 45, wurde er von seinem Jünger Kajora in Hira beigesetzt" (l.12361-12362); Labourt: "c'est pour cette raison, peut-être, que les chroniqueurs postérieurs le font mourir à Hira" and "les restes du catholicos furent portés en grande pompe au monastère de Séleucie" (l.10976-10987). (c) Card `legacy.traces` 2 gives the school at Seleucia from Chabot and Mari; Labourt doubts it, "L'existence de l'École de Séleucie à cette époque me semble problématique" (l.9843-9844).
  Fix, brief l.7: "A Life of Mar Aba survives, which Chabot says needs careful critical study. It has him baptized in the village of Akda, a student at Nisibis, a learner of Greek at Edessa, and later a teacher." (Labourt quotes the Life, "il passa un certain temps dans l'enseignement", l.9816-9818.) Brief l.15: "The Life has him buried in the monastery of Seleucia. Mari says his disciple Qyura carried his body to Hira and built a monastery over the grave. Chabot notes that his church honours him as a saint." Brief l.13 then reads: "How he died is told two ways. The Life has him regain the king's favour and die of illness, as head of his church. Bar Hebraeus, of the rival Syriac Orthodox church, says the king chained him when he returned to Seleucia, and he died in prison. Chabot gives the year as 552." Card `place`: "Seleucia-Ctesiphon, the seat of his church; Nisibis and Edessa in his early years; Adorbigan, in exile". Add card `uncertain`: "Where he was baptized and buried. The Life puts his baptism in the village of Akda and his burial in the monastery of Seleucia. Mari ibn Sulayman puts both at Hira, and Chabot's outline follows him on the baptism." Card `legacy.traces` 2 add: "J. Labourt doubts that the school at Seleucia existed so early." Records: add the contested claims "Where he was baptized" and "Where he was buried" with these sides. Audio: the `[warmly]` tag stays before the new closing paragraph.

- **C-M1 MINOR (item 1; a gloss the Life contradicts).** Brief l.5: "a magus, a priest of the old Persian religion". Mari's "magus" says only that he held that religion; the Life makes him a pagan official, not a priest (Braun l.10670-10678; Labourt l.9488-9492). Fix: "a magus, a follower of the old Persian religion".
- **C-M2 MINOR (item 1).** Brief l.11: "The magi hated him, Mari says". Mari: "invidia prosecuti sunt magi" (Gismondi l.14016), they pursued him with envy. Fix: "The magi turned against him, Mari says, because he had been one of them and changed their customs."
- **C-M3 MINOR (item 1).** Brief l.9: "forbids marriage to a father's widow". The letter says "la femme de leur père" (l.22289-22290), a father's wife; nothing says the father is dead. Fix: "a father's wife". The same fix splits the 27-word sentence (C-M7): "A letter in Mar Aba's name calls marriage a bond of love in the chaste and lawful union of a man and a woman."
- **C-M4 MINOR (card; anachronism, item 4).** Card `place`: "Adorbigan, now Azerbaijan". The province is Persian Adharbaijan, now north-west Iran (Labourt places his exile "dans la région de Ganzak", l.10647); "now Azerbaijan" reads as the modern country. Fix: drop "now Azerbaijan" (as in the C-B2 place text).
- **C-M5 MINOR (card, item 1).** Card `remembered` 2: Mari "tells his conversion, his trial before the king and his death with wonders". Mari's death is an illness, with no wonder (Gismondi l.13990-13999); the wonders come in his life, "miracula quoque ac prodigia operatus est" (l.14021-14022). Fix: "tells his conversion, his wonders, his trial before the king and his death".
- **C-M6 MINOR (card; an editor's year told as the record's).** Card `knownFor` "whose synod of 544" and `keyWorks` title "The Synod of Mar Aba (544)". The 544 is Chabot's bracket, "[A.D. 544]" (l.20902), reckoned from "la 13e année ... de Kosrau" (l.20909); the document recording the end of the split is dated in Kosrau's 10th year, October 540 by Chabot (l.21062-21065, 21106). Fix, `knownFor`: "... whose synod, dated by J.-B. Chabot to 544, records the end of a split between rival patriarchs." `keyWorks` title: "The Synod of Mar Aba (dated by Chabot to 544)".
- **C-M7 MINOR (item 4).** Narrator sentences past about 25 words: l.9 (27, the letter) and l.13 (26, Bar Hebraeus). The fixes in C-M3 and C-B2 bring both to 25 and 22.

**After the fixes.** 402 words, 2:29, FK 6.6, Flesch 72.3; no narrator sentence past 25 words.

---

### 2. Cosmas Indicopleustes

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | PASS in the brief; card minor (C-M8, C-M10) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS |
| 5 | No role for a witness | PASS |
| 6 | Partisan witness named and marked | PASS |
| 7 | Contested both sides | FAIL, blocking (C-B3); minor (C-M10) |
| 8 | Common names placed | FAIL, minor (C-M9) |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | PASS (1:59) |
| 11 | grade_text | PASS |
| 12 | Card order, caveat repeated | FAIL, blocking (C-B3, the Tradition line) |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |

**Quotes and close tellings** (`cosmas-indicopleustes_christian-topography_mccrindle1897.txt`)
- The voyage (l.1): "bound for Further India ... mouth of the ocean, I saw there to the right of our course a great flight of the birds which they call Souspha ... we were all in alarm; for all the men of experience on board, whether passengers or sailors ... called out to the pilot: 'Steer the ship to port and make for the gulf, or we shall be swept along by the currents and be carried into the ocean and be lost.'" (l.3289-3329). Quote exact.
- l.3: "voyages for commercial purposes in three of these gulfs — the Roman, the Arabian and the Persian" (l.3283-3285); McCrindle, "the Mediterranean Sea, the Red Sea, and Persian Gulf" (l.609-611), "most probably a native of Alexandria" (l.578-579), "Indicopleustes, or the Indian Navigator" (l.443-445). Faithful.
- Adulis (l.5): "some five and twenty years ago, more or less, at the beginning of the reign of the Roman Emperor Justinus, Elesbaan ... preparing to start on an expedition against the Homerites on the opposite side of the Gulf ... the Governor ... applied to myself and another merchant called Menas" (l.4069-4103); McCrindle, "Cosmas found himself here in the year 525" (l.695-696), "about the year 547" (l.848-849). Faithful.
- l.7: Photius, "neither the sky nor the earth is spherical, but that the former is a kind of vault, and the latter a rectangular plane" (`photius_library-v1_freese1920.txt` l.2627-2630); "that most divine man and great teacher Patricius" (l.2529-2531), exact; "elevated to the lofty episcopal throne of all Persia, having been appointed to the office of Bishop Catholic" (l.2536-2539); McCrindle's identification (l.2557-2563); De La Croze (l.781-810); "the Mother of God, an expression abhorrent to the Nestorians" (l.811-813). Faithful, and attributed.
- l.9 and l.11: "there is a Church of Christians, with clergy and a body of believers" (l.7191-7202), "a bishop, who is appointed from Persia" (l.7210-7211), "This I avouch to be the veritable fact, from what I have seen and heard in the many places which I have visited" (l.7187-7189). All exact.
- Card: Photius "may fairly be regarded as a fabulist rather than a trustworthy authority" (Freese l.2625-2627); "The condemnatory verdict of Photius upon the work of Cosmas has not been endorsed by modern opinion" (l.886-888), exact; Voss and Fabricius (l.563-574); Salt's 522 and 530 (l.4117-4119). Faithful.

**Findings**

- **C-B3 BLOCKING (items 7, 12; README and card; a placing misread and a contested affiliation placed as settled).** README l.11: "Card traditions are the scan's placings, except Cosmas, whose card follows the census's 'The Church of the East under Persia'; McCrindle leaves his church an open question, and the card says so." Card `tradition`: "The Church of the East under Persia". The census does not place Cosmas there. In `cic-website/data/world-census.json` he is a person of Aksumite Christianity (movement `aksumite-christianity`, `people`: "Cosmas Indicopleustes", year 522); The Church of the East under Persia lists only Narsai, Barsauma and Mar Aba I as people, and the corpus map files his book there as "context", "Provisional on his affiliation" (`cic/corpus-map/the-church-of-the-east-under-persia.yaml` l.113-123). The scan has "Alexandrian / Church of the East leaning" (row 57). And McCrindle does not leave the question open: "That to which Cosmas most probably belonged was the Nestorian" (l.781-782), with one passage "to throw some doubt" (l.809-811); the card says that, so "and the card says so" contradicts the card. The Tradition line thus puts a disputed affiliation on the card as his church, on a placing no file makes.
  Fix, card `tradition`: "Aksumite Christianity" (the census person entry). README l.11: "Card traditions are the scan's placings, in the census's names. Cosmas's card follows the census, which lists him among the people of Aksumite Christianity, where his account of Adulis belongs; the scan has 'Alexandrian / Church of the East leaning'. McCrindle thinks he most probably belonged to the Church of the East, and the card's What is uncertain says so. They are to be settled with the placing."
- **C-M8 MINOR (card, item 1; unsupported superlative).** `legacy.traces` 1: his notes "are among the earliest reports of Christians in those places". No held line says so (searched McCrindle, Labourt, Howard, Mackenzie, Hough). Labourt calls the account "des renseignements précieux sur l'extension de l'Église de Perse à cette époque" (l.9620-9622). Fix: "His notes of churches with clergy in Ceylon, on the pepper coast of Male, at Calliana under a bishop appointed from Persia, and on the island of Dioscorides are, in J. Labourt's words, precious evidence for the spread of the church of Persia in his day."
- **C-M9 MINOR (card, item 8).** `dates`: "at the start of the emperor Justin's reign". Two emperors bore the name, and Freese notes the doubt for Photius (l.2614-2618). McCrindle identifies Cosmas's Justinus as "Justinus I, or the Elder" (l.4083-4084). Fix: "At Adulis at the start of the reign of the emperor Justin I, as McCrindle identifies him, some twenty-five years before he wrote, by his own account; ..." and `uncertain` 5: "Cosmas gives only the start of Justin's reign".
- **C-M10 MINOR (card; contested told as settled within the card).** `keyWorks` "about": "with an eyewitness account of Adulis, Ethiopia, Ceylon and the trade of India". `uncertain` 2 rightly says it is disputed whether he reached India, and Book XI tells Ceylon partly through the merchant Sopatrus (l.18885-18891). Fix: "with an eyewitness account of Adulis and Ethiopia and reports of Ceylon and the trade of India".

---

### 3. Barsanuphius and John of Gaza

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | FAIL, blocking (C-B5); minor (C-M11, C-M13, C-M14) |
| 2 | Quotes verbatim | PASS (close tellings checked below) |
| 3 | No invention | PASS |
| 4 | Reading aids | minor (C-M12) |
| 5 | No role for a witness | PASS |
| 6 | Partisan witness named and marked | PASS |
| 7 | Contested both sides | PASS (the two Barsanuphii: the preface and Theodore; Theodore's own index in PG 99 separates "Barsanuphius (S.) monachus" and "Barsanuphius haereticus Acephalus", l.159161-159163) |
| 8 | Common names placed | FAIL, minor (C-M15) |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | PASS (2:00) |
| 11 | grade_text | PASS |
| 12 | Card order, caveat repeated | FAIL, blocking (C-B4, `uncertain` 4 and `place`) |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |

**Close tellings** (`dorotheus-gaza_doctrinae-barsanuphius-climacus-agathias-grc-lat_migne-pg88.txt`)
- l.1: "Ad magnum senem sanctum Barsanuphium, et ad ejus discipulum abbatem Joannem, cognomento Prophetam, ob perspicaciae donum quod habuit a Deo. Interrogatio I. Abbatis Dorothei ad abbatem Joannem ... Quomodo possum nimiam libertatem restringere et linguam meam moderari? ... Responsio. Per luctum ... Quo pacto possum quotidianam habens consuetudinem cum hominibus seculi ... planctum servare? ... Non fletus per lacrymas, sed per fletum lacrymae" (l.139571-139714). Faithful.
- l.9: no later heading in l.139581-142030 names Barsanuphius or John (searched). Holds.
- l.7: "reponebam semper omnia apud abbatem Joannem ... « Quid nunc turbare senem pergas? hoc tibi dicturus est quod ego » ... « Anathema tibi ... » ... saepiusque accidit ut id ipsum mihi senex responderet, quod ante cogitatio mea praemeditata erat" (l.127966-127980); "abbatem Joannem beati Barsanuphii discipulum interrogasse ... per litteras sciscitabar" (l.124093-124102); "quicunque sese in Patrum obedientiam dedidere" (l.124112-124113; and l.128015-128016). Faithful but for C-M13.
- l.11 and l.13: "ANONYMI PRAEFATIO. Cum duo Dorothei, totidemque Barsanuphii fuerint, quorum alteri Severi errores defenderunt, alteri sanam doctrinam ... retinuerunt ... Theodorus pater noster ... testis est locupletissimus" (l.122096-122111); Theodore: Pamphilus "sanctos illos viros ... illos Acephalorum propugnatores ... a sancto Sophronio tabella anathematis confixos, intelligo. Ab his enim longe diversissimi sunt superiores illi ... Barsanuphii imago in Magna ecclesia juxta sanctos Patres Antonium, Ephraim aliosque rite dicata et collocata visitur" (l.122127-122131, 122182-122201). Migne prints it as "Anonymi Praefatio", footnote "(h) Anonymi Praefatio ad Doroth. Doctrinas" (l.122025); "without an author's name" stands.
- Nau (card): "le monastère dont les hégoumènes successifs ont été, au VIe siècle, Barsanuphios, Séridos et enfin Dorothée ... C'est vers Choubâna qu'il nous faut placer le monastère de Séridos" (`po08_..._1912.txt` l.11422-11424, 11495-11501). Jerome: "the village Thabatha, situate about five miles to the south of Gaza" (`npnf206_jerome-principal-works.xml` l.30129-30130). Faithful.

**Findings**

- **C-B4 BLOCKING (items 1, 12; false absence: a held church historian on Barsanuphius).** Records `absent_details`: "The census line that Barsanuphius was an Egyptian walled into a cell around 520 was not found in any held file", and "No held line calls them 'of Gaza'. The place rests on Nau's placing ... and on Jerome's"; card `uncertain` 4: "The held text gives no birth, origin or death for either man"; card `dates`: "No held source gives their years". Evagrius Scholasticus, held in English, gives a chapter to him: "BARSANUPHIUS THE ASCETIC. There lived at that season men divinely inspired ... First, Barsanuphius, an Egyptian. He maintained in the flesh the exercise of the fleshless life, in a certain seat of contemplation near the town of Gaza ... He is also believed to be still alive, enclosed in a chamber, although for fifty years and more from this time he has not been seen by any one ... When Eustochius, the president of the church of Jerusalem, in disbelief of this account, had determined to dig into the chamber ... fire burst forth" (`evagrius-scholasticus_ecclesiastical-history_walford1846.txt` l.9256-9277, Book IV ch. 33). That gives his origin, his enclosure and Gaza directly, and a time ("at that season", in Justinian's reign, under Eustochius). Nau also gives the century, "au VIe siècle" (po08 l.11423), and a birth year for Dorotheus, "Dorothée est né vers 540" (l.11524).
  Fix, brief l.5 (with C-B5): "The church historian Evagrius Scholasticus calls Barsanuphius an Egyptian, shut in a cell near Gaza. No one had seen him for over fifty years, Evagrius says. Dorotheus came to know the two old men when he entered the monastery of the abbot Seridus. So says a Life of Dositheus, as Gallandi's notice reports it." (Nau's and Jerome's placing of the monastery stays on the card.) Card `place`: "Near the town of Gaza, in Evagrius Scholasticus's account of Barsanuphius; the monastery of the abbot Seridus, which François Nau places near the village of Thabatha, about five miles south of Gaza in Jerome's account". Card `dates`: "No held source gives their years. Evagrius Scholasticus sets Barsanuphius in Justinian's reign and says no one had seen him for over fifty years; François Nau puts the monastery's heads in the sixth century and Dorotheus's birth about 540. Migne heads the notice on their disciple Dorotheus with the year 596, and the notice reports the Bollandists' view that Dorotheus flourished at the end of the sixth century". Card `uncertain` 4: "Their life. Evagrius Scholasticus calls Barsanuphius an Egyptian, enclosed in a cell near Gaza and unseen for over fifty years; the held texts give no birth or death for either man, and nothing of John's origin." Card `sources.about`: add {"title": "Ecclesiastical History, Book IV, ch. 33 (tr. E. Walford)", "author": "Evagrius Scholasticus", "date": "1846", "language": "English translation", "file": "cic/texts/evagrius-scholasticus_ecclesiastical-history_walford1846.txt"}. Records: add the claim "Barsanuphius, an Egyptian, lived enclosed in a cell near Gaza, unseen for fifty years and more; Eustochius of Jerusalem tried to dig into it and fire burst out", witness Evagrius IV.33 (l.9256-9277), Documented for Evagrius's report, the fire told as a wonder; replace the first and third `absent_details` notes to match.
- **C-B5 BLOCKING (items 1, 5; witness swap: an editor's notice credited to its reprinter).** Brief l.5 "So says Migne's notice on Dorotheus"; card `dates` ("Migne ... reports the Bollandists' view"), `legacy.traces` 2 ("Migne's notice reports"), `uncertain` 3 and 5, `sources.about` 2 (author "J.-P. Migne"); records (witness "Migne's Notitia"), README l.5 (C-M16). The Notitia is Andrea Gallandi's prolegomenon, which Migne reprints with its source line: "S. DOROTHEUS ARCHIMANDRITA NOTITIA (Galland., Veterum Patrum Biblioth., tom. XII, Proleg., p. xxvii, et p. 571.)" (l.121947-121951). Its reports (the Life of Dositheus, the Bollandists, Theodore the Studite, the Latin of Hilarion revised by Fronto Ducaeus) are Gallandi's. Migne's own is the year heading "ANNO DOMINI DXCVI" (l.121945).
  Fix: brief l.5 as in C-B4. Card: "Gallandi's notice, which Migne reprints" wherever "Migne's notice" stands (`dates` as in C-B4; `legacy.traces` 2 "..., Gallandi's notice reports"; `uncertain` 3 "the Life of Dositheus, as Gallandi's notice reports it"; `uncertain` 5 "which Gallandi's notice gives to Hilarion of Verona"). `sources.about` 2: {"title": "Notice on Dorotheus (reprinted in Patrologia Graeca 88), and an anonymous preface", "author": "Andrea Gallandi", ...}; Migne stays as editor in `ownWords`. Records: witness "Gallandi's Notitia, reprinted in PG 88 (l.121947-121992)".
- **C-M11 MINOR (item 1; misleading).** Brief l.3: "The questions and answers survive among Dorotheus's writings, in Latin, printed by J.-P. Migne." Migne prints the Greek and the Latin (Greek heading "TOY AYTOY ABBA ΔΩΡΟΘΕΟΥ", l.139592-139597, garbled in the scan); "survive ... in Latin" reads as if only a Latin survives. Fix: "J.-P. Migne prints the questions and answers among Dorotheus's writings, in Greek and Latin."
- **C-M12 MINOR (item 4; pronoun).** Brief l.3: "Its heading sends them ..." has no singular antecedent. Fix: "Their heading sends them ..."
- **C-M13 MINOR (item 1).** Brief l.7: "Once a thought told him ... and often John gave the very answer". Dorotheus tells a habit, "Quod si mihi aliquando cogitatio ... respondisset ... saepiusque accidit" (l.127969-127979), not one occasion. Fix: "When a thought told him not to trouble the old man, since he knew the answer already, Dorotheus cursed the thought and went anyway. Often John gave the very answer the thought had foreseen." (To hold the length, l.7 opens "Dorotheus later told monks how he took everything to John.")
- **C-M14 MINOR (card, item 1).** `knownFor`: "whose written answers guided Dorotheus of Gaza and others". The held answers are Dorotheus's set only (card `keyWorks`; records `absent_details` 2); "and others" rests on the census's unheld correspondence. Fix: "Two monks, a master and his disciple, whose written answers guided Dorotheus of Gaza; the questions he put to them survive with their answers."
- **C-M15 MINOR (item 8).** Brief l.13 and card `remembered` 1: "the holy fathers Antony and Ephrem", common names with no place. Theodore names them only "Antonium, Ephraim" (l.122200), so adding "of Egypt" or "the Syrian" would be an identification no held line makes. Fix: keep the source's form and log the gap in Open-Gaps, as batch 2 did for Sigebert.

**After the fixes.** 321 words, 1:59, FK 6.3, Flesch 71.8.

---

### 4. Cyril of Scythopolis

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | FAIL, blocking (C-B6); minor (C-M17) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS |
| 5 | No role for a witness | PASS |
| 6 | Partisan witness named and marked | PASS ("Cyril writes for the side that accepted Chalcedon"; card `uncertain` 1, "le chef des Acéphales") |
| 7 | Contested both sides | PASS |
| 8 | Common names placed | FAIL, minor (C-M19) |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | PASS (2:00) |
| 11 | grade_text | PASS |
| 12 | Card order, caveat repeated | PASS (card minors C-M18, C-M20) |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |

**Close tellings**
- The scene (l.1): Kugener's French of the Life of Sabas, "Anastase, fils de Pamphile, qui était à la tête du duché de Palestine ... avec mission d'amener Jean à communiquer avec Sévère et à anathématiser le concile de Chalcédoine ... l'archevêque fit venir pendant la nuit tous les moines dans la ville sainte ... au dire de ceux qui ont compté cette multitude, comprenait dix mille moines ... le dimanche dans le temple du saint protomartyr Étienne ... l'archevêque monta à l'ambon, ayant à ses côtés Théodose et Sabas ... le peuple tout entier se mit à crier pendant de longues heures: « Anathématise les hérétiques et confirme le concile. » ... anathématisèrent ... Sévère ... et quiconque ne recevait pas le concile de Chalcédoine ... le duc, craignant la multitude des moines, s'enfuit à Césarée" (`zacharias-scholasticus_vie-de-severe-po2-syr-fra_kugener1903.txt` l.25076-25204). Faithful.
- Kugener (l.3): "Cyrille né à Scythopolis en Galilée vers 523, et mourut après 557. Sa Vie de saint Sabas ... constitue une source du plus grand prix pour l'histoire de l'Église de Jérusalem et du monachisme palestinien" (l.24692-24694). Faithful.
- The Life of Euthymius (l.5 to l.9; `cyril-scythopolis_vita-euthymii-cotelier-monumenta-v2-grc-lat_1681.txt`): "viderem ejus thecam assidue multis scatere miraculis, mirabar semper apud me, et cogitabam quo modo ad Deum tantam assecutus sit fiduciam ... cum incidissem in multos ex hujus eremi Patribus, qui partim recte audierant res Euthymii, partim [a] beato Saba ... quaecumque unusquisque mihi ... narravit, omnia quidem accurate conscripsi" (l.45444-45472); "Haec mihi Anachoreta Cyriacus narravit" (l.31776-31777); the vision, "magnus Euthymius divinusque Sabas mihi apparent ... nondum potuit orationi ne principium quidem imponere ... argenteum quemdam mellis alabastrum ... specillum intinxisset, ter meum in os immisit ... ejus adhuc in ore remanserunt reliquiae ... praesens opus inchoavi" (l.45600-45698). Faithful, the scan rough, except C-M17.

**Findings**

- **C-B6 BLOCKING (item 1; a completeness claim the held editor contradicts).** Brief l.5: "His Life of Euthymius survives whole". Cotelier, in the notes the card cites, says his copy lacks the opening letter that others give as its beginning: "Principium Epistola ... At Vita nostra nec Epistolam habet, nec eo modo incipit" (l.72960-72971), and that the Life was "composita primitus a Cyrillo ... postea vero, uti videtur, in ..." (l.72945-72950), first written by Cyril and afterwards, it seems, altered (the scan breaks off). The card's own `uncertain` 3 reports the missing letter, so brief and card disagree. Fix, brief l.5: "Jean-Baptiste Cotelier printed his Life of Euthymius the Great with a Latin translation in 1681." (With C-M19.)
- **C-M17 MINOR (item 1).** Brief l.5: "He sought out old monks of the desert". Cyril: "cum incidissem in multos", when he had met many (l.45463). Fix: "He met many old monks of the desert who had heard the story of Euthymius, some of it from Sabas."
- **C-M18 MINOR (card, item 1).** `keyWorks` 1 "about": "the life of the founder of the desert lauras". That phrase rests only on the Library's file header (l.25-26); no held line makes Euthymius the founder of the desert lauras as a class. Fix: "the life of the monk Euthymius the Great, from what old monks told Cyril, with his own account of the vision that let him begin".
- **C-M19 MINOR (item 8).** First mention of Euthymius in the brief (l.5) and card `knownFor` gives no epithet, and the batch 1 profile is `euthymius-the-great`; Cyril calls him "magnus Euthymius" (l.45601). Fix: "Euthymius the Great" at first mention in brief (as in C-B6) and card ("above all Euthymius the Great and Sabas").
- **C-M20 MINOR (card, item 1).** `uncertain` 2: "by leave of the solitary John, once a bishop". The Latin reads "admirabilis solitarii Johannis, Episcopi inquam" (l.45536-45538), the solitary John, the bishop I mean; "once" is added. Fix: "by leave of the solitary John, whom he calls a bishop".

**After the fixes.** 322 words, 1:59, FK 6.7, Flesch 70.7.

---

### 5. README

The README matches the scan on the ten ids, the order and years (Cosmas "fl. to about 550", scan "fl. c.520-c.550"; Barsanuphius and John "first half of the sixth century"; Mar Aba 552; Cyril about 559), the live-entry skip (Justinian I), the major marks, the recorder Whos, the Outside witness label on Procopius and the pairing ruling, and it follows the form of the batch 1 and batch 2 READMEs. Two points:

- The Cosmas tradition sentence (l.11) is wrong on the census and on McCrindle; see C-B3, counted there.
- **C-M16 MINOR (witness swap, as C-B5).** README l.5: "Migne heads his notice 'ANNO DOMINI DXCVI' and reports the Bollandists placing him at the end of the sixth century". The heading is Migne's; the report is Gallandi's notice, reprinted (PG 88 l.121945-121961). Nau also puts Dorotheus's birth about 540 (po08 l.11524), which supports leaving him out of this run. Fix: "Migne heads the notice on him 'ANNO DOMINI DXCVI'; the notice, Gallandi's, reprinted by Migne, reports the Bollandists placing him at the end of the sixth century, with his death year unknown, and François Nau puts his birth about 540."

---

### Part C totals

| Profile | Blocking | Minor |
|---|---|---|
| Mar Aba I | 2 (C-B1, C-B2) | 7 (C-M1 to C-M7) |
| Cosmas Indicopleustes (with the README tradition sentence) | 1 (C-B3) | 3 (C-M8 to C-M10) |
| Barsanuphius and John of Gaza | 2 (C-B4, C-B5) | 5 (C-M11 to C-M15) |
| Cyril of Scythopolis | 1 (C-B6) | 4 (C-M17 to C-M20) |
| README | 0 | 1 (C-M16) |
| **Part C** | **6** | **20** |

Three of the six blocking points are false absences or a missed witness found by searching the Library before accepting the drafts' claims: Braun's German Life of Mar Aba and Labourt's retelling of it (C-B1, with C-B2 following from it), and Evagrius Scholasticus on Barsanuphius (C-B4). Every quotation in the four briefs and cards was re-checked against its vendored file and matches.
