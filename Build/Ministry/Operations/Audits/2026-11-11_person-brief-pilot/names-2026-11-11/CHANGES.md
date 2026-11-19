# Name clarification changes, 2026-11-11

Source paths below are under /home/user/CIC-Project/cic/texts/. Short names:
- S2 = npnf202_socrates-sozomen-ecclesiastical-histories.xml
- S1 = npnf201_eusebius-church-history-life-of-constantine.xml
- S3 = npnf203_theodoret-jerome-gennadius-rufinus.xml
- S4 = npnf204_athanasius-select-works-letters.xml
- S6 = npnf206_jerome-principal-works.xml
- S14 = npnf214_seven-ecumenical-councils.xml

Common support for "church historian": S2 line 58 (title "Socrates and Sozomenus Ecclesiastical Histories"), S2 line 21633 ("The Ecclesiastical History of Sozomen"), S1 lines 47 and 848 (Eusebius, "Church History").

Note: the scoring script named in the task (scratchpad/score.py) does not exist. I scored with the repo's own engine.m7.turn_readability.score_turn (read-only import, no bytecode written) through /tmp/claude-0/-home-user-CIC-Project/1ff025fb-e133-53cc-8b59-cca268383c4f/scratchpad/score_names.py.

## origen
Brief (`origen.txt`)
- "and Eusebius says he was seized" -> "and the church historian Eusebius says he was seized". Support: S1:47, 848.
- "which he and Basil are thought to have gathered" -> "which he and Basil of Caesarea are thought to have gathered". Support: S3:42470 ("Basil of Cæsarea in Cappadocia").
- "Socrates, who defended Origen, says Athanasius" -> "The church historian Socrates, who defended Origen, says Athanasius". Support: S2:58.

Card (`origen.card.json`)
- keyWorks, The Hexapla, about: "; Eusebius says Origen left us copies of it, and Jerome says" -> "; the church historian Eusebius says Origen left us copies of it. Jerome says" (split to stay near 28 words). Support: S1:47, 848.
- legacy.traces[0]: "two brothers, Gregory and Athenodorus" -> "two brothers, Gregory the Wonderworker and Athenodorus". Support: S6:16659 (Theodore "afterwards called Gregory", "Surnamed Thaumaturgus or Wonderworker. One of Origen's pupils"); anf09_gospel-of-peter-diatessaron-origen-commentaries.xml:20185 ("Gregory ... called Thaumaturgus"); S1:36590-36596 (brothers Gregory and Athenodorus with Origen at Caesarea).
- legacy.remembered[0]: "Socrates, who defended Origen, names four men who attacked him: Methodius, Eustathius, Apollinaris and Theophilus." -> "The church historian Socrates, who defended Origen, names four men who attacked him: Methodius of Olympus, Eustathius of Antioch, Apollinaris and Theophilus of Alexandria." Support: S2:18141-18144 (Methodius "bishop of a city in Lycia named Olympus", Eustathius "presided over the church at Antioch"), S2:17563 (chapter title: Theophilus Bishop of Alexandria, condemnation of Origen's books), S2:58.
- legacy.remembered[2]: "Epiphanius charged" -> "Epiphanius of Cyprus charged". Support: S2:16792 ("Epiphanius, bishop of Cyprus").
- legacy.remembered[3]: "The historian Evagrius says" -> "The historian Evagrius Scholasticus says". Support: evagrius-scholasticus_ecclesiastical-history_walford1846.txt:5 ("Evagrius Scholasticus ... Antiochene lawyer and historian"); there is also Evagrius Ponticus, hence the surname.
- uncertain[1]: "which so enraged Demetrius that" -> "which so enraged his bishop Demetrius that". Support: S1:36335 and 51763 ("Demetrius, bishop of Alexandria"); the brief itself says "his own bishop, Demetrius".

## athanasius-of-alexandria
Brief
- "Socrates, who tells it with plain sympathy, says Arsenius was found alive ... under his cloak, and Athanasius showed both. Sozomen adds a rumor" -> "The church historian Socrates, who tells it with plain sympathy, says Arsenius was found alive ... under his cloak. Athanasius showed both. Another church historian, Sozomen, adds a rumor". Split at "and" to keep the sentence under 28 words. Support: S2:58, 21633.

Card
- traces[0]: "Socrates declines to tell" -> "The church historian Socrates declines to tell". Support: S2:58.
- traces[2]: "In 433 Cyril wrote to John of Antioch that some had garbled Athanasius's letter to Epictetus, and sent transcripts" -> "In 433 Cyril of Alexandria wrote to John of Antioch that some had garbled Athanasius's letter to Epictetus of Corinth. He sent transcripts". Support: S14:1076 ("Cyril of Alexandria"); S4:70618 ("Epictetus, bishop of Corinth"). Epictetus needed a place because of the Stoic philosopher of the same name.
- uncertain[0]: "Sozomen gives two reasons, ... a plan of Athanasius, and says Arsenius" -> "The church historian Sozomen gives two reasons, ... a plan of Athanasius. He says Arsenius" (split). Support: S2:21633. The quoted words are untouched.
- uncertain[1]: "Rufinus tells that Bishop Alexander once" -> "The historian Rufinus tells that Bishop Alexander of Alexandria once". Support: S2:5655, 5667 (Socrates wrote "following Rufinus" for his history); S2:4009 ("Alexander bishop of Alexandria happening to pass by" the boys at play). "Historian" not "church historian" only to keep the sentence at 28 words.

## john-chrysostom
Brief
- "Socrates says some thought John added" -> "The church historian Socrates says some thought John added". Support: S2:58.
- "his own favorite, Isidore," -> "his own favorite, the Alexandrian priest Isidore,". Support: S2:42753 ("a presbyter of his church named Isidore, who took charge of strangers and of the poor at Alexandria"); S2:46284 index ("Isidore, a presbyter of Alexandria").
- "against Athanasius, and so" -> "against Athanasius of Alexandria, and so". Support: S2:4009; S4 is the Athanasius of Alexandria volume; the Athanasius brief calls him bishop of Alexandria.
- "In 438 Bishop Proclus carried John's body back to Constantinople in procession" -> "In 438 Bishop Proclus of Constantinople carried John's body back to the city in procession". Support: S2:21269, 21292 (Proclus succeeds Maximian as bishop of Constantinople); S2:48076 index ("Proclus, bishop of Constantinople"); another Proclus was bishop of Cyzicus (S2:20470).

Card
- keyWorks, On the Priesthood, about: "written, Socrates says, while" -> "written, the church historian Socrates says, while". Support: S2:58.
- legacy.traces[2]: "only when Proclus brought John's body home on the twenty-seventh of January, 438, and laid it in" -> "only when Proclus of Constantinople brought John's body home on the twenty-seventh of January, 438. He laid it in". Support: S2:21269, 21292, 48076.
- legacy.remembered[1]: "Severian preached that ... depose him, and Sisinnius" -> "Severian of Gabala preached that ... depose him. Sisinnius". Support: S2:17922 ("Severian presided over the church at Gabala, a city of Syria"). Split because the sentence was already 33 words; the single-quoted words are untouched.
- legacy.remembered[2]: "Socrates notes that Theophilus's condemnation of Origen came about two hundred years after Origen's death, while John was restored" -> "... Theophilus of Alexandria's condemnation ... after Origen's death. John was restored". Support: S2:17563. Split at "while" to stay near 28 words; the word "while" is dropped.

## gregory-of-nyssa
Brief
- "until Valens died in 378" -> "until the emperor Valens died in 378". Support: S2:12222 ("the Emperor Valens").
Card
- legacy.remembered[0]: "counted him and Basil among" -> "counted him and Basil of Caesarea among". Support: S3:42470 ("Basil of Cæsarea in Cappadocia"); the brief says Gregory's brother Basil made him bishop.

## gregory-of-nazianzus
Brief
- "When its president Meletius died," -> "When its president, Meletius of Antioch, died,". Support: S2:13930, 13997, 34932 ("Meletius, bishop of Antioch").
- "His closest friend was Basil, whom" -> "His closest friend was Basil of Caesarea, whom". Support: S3:42470.
Card
- legacy.traces[0]: "Gennadius, calling Gregory that most eloquent man, reports that Rufinus put his works into Latin along with Basil's." -> "Gennadius of Marseilles, calling Gregory that most eloquent man, reports that Rufinus put his works into Latin along with those of Basil of Caesarea." Support: S3:3611 ("Gennadius, presbyter of Marseilles"); S3:42466-42471 (Gennadius's chapter on Rufinus: "Basil of Cæsarea ... Gregory Nazianzan, that most eloquent man").

## constantine-the-great
Brief
- "prayed, Eusebius says, that" -> "prayed, the church historian Eusebius says, that". Support: S1:47, 848. The later "Eusebius, the bishop of Caesarea" stays; it adds the second role.
- "Sozomen says later Christian emperors" -> "The church historian Sozomen says later Christian emperors". Support: S2:21633.
Card
- legacy.remembered[1]: "Sozomen calls him a powerful" -> "The church historian Sozomen calls him a powerful". Support: S2:21633.
- uncertain[1]: "his conversion by Silvester is kept" -> "his conversion by Silvester of Rome is kept". Support: zachariah-rhetor_chronicle_hamiltonbrooks1899.txt:752 ("Silvester, Patriarch of Rome"), 974-975. This sentence was already about 43 words before; the addition makes it 45. I did not split it because the "since" clause carries the argument.

## ephrem-the-syrian
Brief
- "Palladius tells what came next" -> "Palladius of Galatia tells what came next". Support: palladius_lausiac-history_clarke1918.txt:5 ("Palladius of Galatia"), 471 (the Ephraim chapter).
- "Sozomen says Bardaisan's son" -> "The church historian Sozomen says Bardaisan's son". Support: S2:21633.
Card
- legacy.traces[0]: "Sozomen names his best-known" -> "The church historian Sozomen names his best-known". Support: S2:21633.
- uncertain[1]: "Palladius says he died" -> "Palladius of Galatia says he died". Support: as above.

## methodius-of-olympus
Brief
- "Epiphanius called him a learned man" -> "Epiphanius of Cyprus called him a learned man". Support: S2:16792.
Card
- legacy.traces[0]: "Epiphanius made great use" -> "Epiphanius of Cyprus made great use". Support: S2:16792.
- legacy.remembered[0]: "Socrates names him first" -> "The church historian Socrates names him first". Support: S2:58.

## Names considered and left alone
- Socrates in methodius brief: already "The historian Socrates" (role given at first mention).
- Palladius in the chrysostom brief and card: already introduced by role ("who stood by John to the end", "a bishop who stood by him").
- Jacob in the ephrem brief: "its bishop, Jacob" already gives role and place (Nisibis).
- Peter in the athanasius brief: "named Peter as his successor" already says who he is; S4:7264 confirms.
- Flavian in the chrysostom brief: "old Bishop Flavian" follows "a tax riot in Antioch" in the same paragraph. Adding "of Antioch" would push a 27-word sentence to 29. Supported if wanted by S2:17819.
- Rufinus in origen brief and card, and in the nazianzus card: "Rufinus's Latin" and "Rufinus put his works into Latin" show him as the translator in context. S3:42465 says "presbyter of the church at Aquileia" if Mark wants it added.
- Jerome everywhere: the one famous Jerome, and always a named source.
- Eusebius in the athanasius/other texts: no bare mentions beyond those fixed. In the constantine card the first mention already reads "Eusebius of Nicomedia" and "Eusebius of Caesarea".
- Theophilus in the chrysostom brief: first mention already "Theophilus of Alexandria". Second mention in the origen card ("Socrates also says Theophilus of Alexandria wrote") already full.
- Gregory of Nazianzus, Cyril of Alexandria, John of Antioch, Evagrius "later bishop at Antioch": already full at first mention.
- Gregory in the nyssa brief ("his friend Gregory of Nazianzus"): full. The person's own bare "Gregory" is the subject.
- Basil in the nyssa brief: "his brother Basil"; in the ephrem card: "Basil, later bishop of Caesarea".
- Constantine in the athanasius brief ("Constantine sent him to Trier"): left, because the text says "the emperor" in the same sentence, but note that Constantine II also ruled from Trier. If Mark wants it, "the emperor Constantine" does not separate them; "Constantine the Great" would.
- Athanasius in the origen brief ("Athanasius often cited him"): left, the name is not shared by a rival figure of note.
- Eutropius (chrysostom card uncertain[0]): rare name, and the brief gives role.
- Apollinaris (origen card): I could not confirm "of Laodicea" for the one Socrates names at the Origen passage (S2:45530 index is the Laodicean father and son), so I left it bare.
- Theodoret, Photius, Lactantius, Zachariah, Nicephorus Callistus, Justinian, Valens (card), Eunomius, Arius, Demetrius in the origen brief (role given): not shared names or already carry a role.
- Abraham, Simeon, Zenobius (ephrem card "best-known pupils"): role given by "pupils"; no identification in the source beyond that.

## Scores (engine.m7.turn_readability, FK ceiling 10, FRE floor 60)
| brief | FK before | FK after | FRE before | FRE after | fails |
|---|---|---|---|---|---|
| origen | 8.58 | 8.77 | 62.5 | 61.7 | none |
| athanasius-of-alexandria | 8.43 | 8.35 | 63.3 | 63.0 | none |
| john-chrysostom | 8.51 | 8.80 | 61.5 | 60.3 | none |
| gregory-of-nyssa | 8.88 | 8.96 | 63.3 | 63.0 | none |
| gregory-of-nazianzus | 8.93 | 9.05 | 61.2 | 60.7 | none |
| constantine-the-great | 8.40 | 8.60 | 67.6 | 66.9 | none |
| ephrem-the-syrian | 8.37 | 8.58 | 66.9 | 66.0 | none |
| methodius-of-olympus | 8.06 | 8.10 | 61.9 | 61.8 | none |

All eight stay in FK 8 to 10 with FRE at least 60. john-chrysostom (60.3) and gregory-of-nazianzus (60.7) sit close to the FRE floor. No brief has parentheses. Card JSON files all parse, keep the same keys, and their `sources` blocks are byte-identical in content to the pre copies.
