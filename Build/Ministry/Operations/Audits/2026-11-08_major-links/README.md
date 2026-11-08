# Major links: the outcome pass over eras 1 to 5 (P2-ML), 2026-11-08

Ruling, change order and cap ruling: `Build/Ministry/Features/Church-Family-Tree/Decision-Log.md`, "Major links: a switch, and what makes a link major" (2026-11-08).

## What "major" means

- "Gave rise to", "continued as" and "broke with" are major by type.
- An "influenced", "argued against" or "in contact with" link is major only when its own sources show an institutional act. That means a council, canon, synod or law condemning, deposing or excluding a group or its teaching; a split into a separate church or body; or a rule, practice or settlement changed by an authority. Such a link carries `outcome`, one plain sentence naming the act.

## Rounds

1. **Inventory** (a script, no model): `Inventory_Era1.json` to `Inventory_Era5.json`, `Inventory_Summary.json`. 228 links of the three judged types; 74 more major by type.
2. **Draft** (Opus, one agent per era): `Draft_Era1.json` to `Draft_Era5.json`, merged in `Drafting_Record.json`. 95 major, 133 minor. A script confirmed every evidence text verbatim at its stated lines.
3. **Review round 1** (separate Opus, full): `Opus_Review_Round1.json`. Revise: 1 blocking, 20 substantial, 9 minor. It cut the count to 77 and ruled once on each borderline category.
4. **Change order** (Mark): 151 major lines in eras 1 to 5 was far more than "the top few". The test was narrowed to institutional acts, so a teaching or text merely taken up no longer counts.
5. **Revision** (Opus): `Revision_Round1.json`. It applied the review and the narrowed test. 27 links were demoted as "taken up". 50 major, 178 minor.
6. **Review round 2** (separate Opus, targeted): `Opus_Review_Round2_TargetedRecheck.json`. Pass: 0 blocking, 0 substantial, 5 minor, all applied (`Final.json`).
7. **Readability**: `Outcome_Prose.json`. 43 of the 50 outcome sentences were rewritten, keeping every fact. Each now scores Reading Ease 60 or more and FK grade 10 or less with `engine.m7.turn_readability.score_turn`.
8. **Review round 3** (separate Opus, targeted, of the rewrites): `Opus_Review_Round3_TargetedRecheck.json`. One substantial finding (the Carmelite 1247 sentence), at the cap. **Cap ruling (Mark): the reviewer's fix applied as written.**

All three rounds of the cap were used.

## Counts (eras 1 to 5, data release 10)

- Links in scope: 302. Major: 124 (22 gave rise to, 8 broke with, 44 continued as; 50 by outcome).
- By outcome kind: split 2, rule-changed 17, council-law 31.
- Per era (major / all links whose earlier movement is in that era): era 1: 18 / 78; era 2: 26 / 71; era 3: 29 / 58; era 4: 25 / 40; era 5: 26 / 55.

## Major by outcome

| Link | Kind | Outcome |
|---|---|---|
| `syriac-edessa-nisibis--the-church-of-the-east-under-persia` | split | Narsai founded a new school at Nisibis in Persian lands, and most of the students from the school of Edessa came to him. |
| `anatolian-church-third-century--byzantine-imperial-church-heraclian-iconoclast` | rule-changed | At Constantinople, the Council in Trullo set its seal on the canons of Gregory the Wonderworker. It put them with those of the great councils. |
| `post-apostolic-house-church--montanism-the-new-prophecy` | council-law | Meetings of the faithful across Asia judged the New Prophecy to be heresy. Its followers were thrown out of the church and barred from communion. |
| `imperial-juridical-christianity--montanism-the-new-prophecy` | council-law | Constantine's law said the Montanists could not meet, not even in a private house. It urged them to join the catholic Church instead. |
| `byzantine-imperial-church-justinianic--montanism-the-new-prophecy` | council-law | Justinian ordered the Montanists to give up their faith, Procopius says. He threatened those who held out with losing the right to leave property to their families. |
| `imperial-juridical-christianity--novatianism` | rule-changed | The Council of Nicaea let Novatianist clergy keep their rank. First they had to promise in writing to follow the teaching of the Catholic Church. |
| `post-apostolic-house-church--marcion-marcionism` | council-law | The church later threw Marcion out, Tertullian says, and turned away the money he had given it along with him. |
| `post-apostolic-house-church--valentinian-and-other-gnostic-christianities` | council-law | Tertullian says the church at Rome threw out Valentinus more than once for spreading his ideas among its members. |
| `anatolian-church-third-century--antiochene-church-third-century` | council-law | Gregory and Athenodorus took part in the meetings at Antioch on Paul of Samosata. These came to an end when a last synod cut him off from communion. |
| `imperial-juridical-christianity--anomoean-eunomian-christianity` | council-law | An imperial law of July 381 forbade Eunomians to build churches in town or country. It seized any land where they did. |
| `imperial-juridical-christianity--pneumatomachian-current` | council-law | Theodosius had the bishops meet at Constantinople. In their first canon they put a curse on the Semi-Arians, who were also known as the Pneumatomachi. |
| `imperial-juridical-christianity--apollinarian-christianity` | council-law | A law of March 388 drove the Apollinarians from the cities and stripped their bishops of the title of bishop. |
| `gallic-nicene-episcopate--homoian-arian-christianity` | council-law | The bishops of Gaul refused communion to Saturninus. They condemned the creed sent to them from Sirmium as soon as it came. |
| `imperial-juridical-christianity--homoian-arian-christianity` | council-law | In July 383 an imperial law said the Arians could not meet or gather any crowd. Eunomians and other groups were banned as well. |
| `imperial-juridical-christianity--donatism` | council-law | Constantine gave leave for a council of nineteen bishops to meet at Rome. It found Donatus guilty and cleared his rival, Caecilian. |
| `imperial-juridical-christianity--persian-church-of-the-east-early` | rule-changed | In a canon, the Persian bishops made a pledge. They would serve the liturgy in the western way that Bishops Isaac and Marutha had taught them. |
| `cappadocian-nicene-pastoral-monastic-tradition--imperial-juridical-christianity` | rule-changed | A law of July 381 named Helladius of Caesarea, Gregory of Nyssa and others. It said all churches must go to bishops in communion with them. |
| `ambrosian-milan-standalone--imperial-juridical-christianity` | rule-changed | Ambrose got Theodosius to promise two things. He would change his edict on the burned synagogue, and he would end the whole inquiry. |
| `antiochene-exegetical-christianity-chrysostom-ce--imperial-juridical-christianity` | rule-changed | A law of July 381 named Diodore of Tarsus and others. It said that every church must go to bishops in communion with them. |
| `imperial-juridical-christianity--antiochene-exegetical-christianity-chrysostom-ce` | split | After synods condemned John Chrysostom, his followers left the church. They met on their own and were known as the Johannites. |
| `byzantine-imperial-church-justinianic--antiochene-exegetical-christianity-chrysostom-ce` | council-law | The Second Council of Constantinople cursed Theodore of Mopsuestia. It also cursed all who stood up for him or said the way he read Scripture was orthodox. |
| `aquileian-christianity--homoian-arian-christianity` | council-law | At Aquileia the bishops condemned Palladius. They found him unworthy to be a priest, and said a Catholic must be made bishop in his place. |
| `hieronymian-ascetic-literary--the-tridentine-church` | rule-changed | The Council of Trent made the old Latin Vulgate the authentic text for public lectures, debates, sermons and teaching. No one could reject it. |
| `byzantine-imperial-church-justinianic--donatism` | council-law | Justinian banned Donatists, Arians, Jews and pagans from having places to meet. Nor could they hold rites as the church does. |
| `imperial-juridical-christianity--priscillianist-asceticism` | council-law | Once the case was reported to the palace, the emperor decreed that Priscillian and his friends be put to death. |
| `syriac-orthodox-west-syriac-christianity--cyrilline-miaphysite-egyptian-christianity` | rule-changed | Dioscorus of Alexandria took Severus's advice. He won back men who had long kept out of communion, and they joined the Egyptian church. |
| `latin-africa-under-byzantium--byzantine-imperial-church-justinianic` | council-law | Reparatus of Carthage would not condemn the Three Chapters. For this he lost his office and was exiled, and his own envoy was made bishop in his place. |
| `byzantine-imperial-church-justinianic--syriac-orthodox-west-syriac-christianity--2` | council-law | Justinian's law said every copy of Severus's writings must be burned. It also kept him out of the capital and the land around it. |
| `armenian-christianity-after-avarayr--byzantine-imperial-church-justinianic` | council-law | In 554 Catholicos Nerses II held a synod at Dvin. It confirmed that the Armenian church would not accept Chalcedon, and set out the faith of Ephesus against it. |
| `armenian-christianity-before-the-bagratids--church-of-caucasian-albania` | council-law | Nerses Bakur, head of the Albanian church, leaned toward communion with the Greek church. For this he was removed, and Simeon took his place. |
| `early-benedictine-italian-monasticism--carolingian-reform-christianity` | rule-changed | In 802 Charlemagne gave an order about monasteries. Anything done in them against the Rule of Saint Benedict was to be put right by that rule. |
| `byzantine-imperial-church-justinianic--gothic-and-vandal-homoian-christianity` | council-law | Justinian let no Christian outside the orthodox faith have baptism or any other rite of the church. Arian soldiers in the Roman army took part in a mutiny over it. |
| `nicene-visigothic-iberia--gothic-and-vandal-homoian-christianity` | council-law | In 589 the third council of Toledo cursed anyone who still held to the faith and communion that came from Arius. |
| `anglo-saxon-christianity--insular-irish-monastic-christianity` | rule-changed | In 664 the king and all at the debate decided to follow the Catholic Easter. Bishop Colman went back to Scotland with those who would not. |
| `anglo-saxon-christianity--carolingian-reform-christianity` | rule-changed | In 742 Carloman, on the advice of Boniface and his fellow bishops, ordered a church synod each year. Its aim was to restore church law and correct Christian practice. |
| `byzantine-imperial-church-heraclian-iconoclast--iconophile-byzantine-monasticism` | council-law | In 754 a council against icons said John of Damascus was deposed and cursed. It said the same of George and of Germanus of Constantinople. |
| `iconophile-byzantine-monasticism--byzantine-imperial-church-heraclian-iconoclast` | rule-changed | At the Second Council of Nicaea, bishops who had been against images read out confessions that venerated them. The synod then took them back. |
| `church-of-the-east-under-the-abbasids--st-thomas-christians-of-india` | rule-changed | The patriarch Theodosius made a church law. It bound the metropolitans of India, China and other far lands to send letters of communion every six years. |
| `latin-papal-church-gregorian--the-carmelites` | rule-changed | In 1247 the Carmelites asked Pope Innocent IV to correct and soften their rule. He had this done, and then he confirmed it. |
| `latin-church-of-outremer--the-carmelites` | rule-changed | Albert, patriarch of Jerusalem, gave the Carmelite friars their rule. Later the friars asked the pope to explain, correct and soften it. |
| `latin-papal-church-gregorian--the-franciscan-movement` | rule-changed | Pope Innocent III granted and confirmed Francis's way of life for him and for all his brothers, present and future. |
| `latin-papal-church-avignon-to-lateran-v--the-beguines` | council-law | The Council of Vienne formally condemned eight errors. It said they were held by the beguines and beghards of Germany. |
| `latin-papal-church-avignon-to-lateran-v--free-spirit-heresy` | council-law | The Council of Vienne in 1311-12 ruled as error the claim that those who live in the spirit of liberty owe no human obedience. |
| `the-tridentine-church--the-humiliati` | council-law | Pope Pius V put an end to the order of Humiliati brothers. He also did away with its general, its heads in each province and all its statutes. |
| `latin-papal-church-gregorian--the-humiliati--2` | rule-changed | In 1200 Pope Innocent III approved the Humiliati. They soon had 220 houses in just the province of Milan. |
| `latin-papal-church-gregorian--the-waldensians` | council-law | A church council at Rome met before the Lateran one. It judged Valdes's followers guilty of schism, and then it condemned them as heretics. |
| `latin-papal-church-gregorian--cathars-albigensians` | council-law | In 1179 the Third Lateran Council cut off the Cathars and all who defended or sheltered them. It barred anyone from housing them. |
| `byzantine-church-after-1054--balkan-bogomil-continuation` | council-law | Emperor Alexios I had Basil, who led the Bogomils, burned in the Hippodrome. He kept the many who followed Basil in jail till they died. |
| `latin-papal-church-gregorian--joachimite-current` | council-law | In 1215 the Fourth Lateran Council condemned and rejected a book by Joachim. In it he wrote against Peter Lombard on the Trinity. |
| `latin-papal-church-avignon-to-lateran-v--military-religious-orders-templars-hospitallers` | council-law | In 1312 Pope Clement V did away with the Templars' order, habit and name for ever. The Council of Vienne approved. |

Every judged link's decision, with its reason (and its evidence lines where major): `Final.json`.

## Open

- Eras 6 and 7 were launched before this pass and were sent the narrowed rule; eras 8 to 10 carry it in the launch prompt (step 4b).
- The map in eras 1 and 2 is still busy with the switch on, because most major links there are condemnations. Shown to Mark in screenshots before merge.

## Wanted texts

- A Syriac or Greek source naming the Philocalia's compilers, rather than the NPNF editors' prolegomena.
- A dated text of the Armenian custom of consecration at Caesarea, independent of Moses of Khoren.
- A law against the Manichaeans (Diocletian's rescript, or Theodosian Code XVI.5) for the Ephraim and Augustine lines against Mani.
- A primary Georgian witness (e.g. Life of John and Euthymius) for the Iviron translators.
- A primary for Kievan Rus' adopting Slavonic letters and books (the Russian Primary Chronicle)
- A source for what Paul and Macarius's mission to Africa (347) imposed on the Donatists.
- A source showing Caesarius of Arles's Rule drawing on Lérins practice.
- A text of the African councils of 416 and 418, or Zosimus's letter, condemning Pelagius (would test the Augustine-Pelagius lines).
- A text recording the result of Pope Gregory's ordered council on the Donatists in Numidia.
- A text showing the Merovingian church adopting Hilary's teaching or practice, not just praising him.
- A vendored Movses Dasxuranci (Dowsett) for the removal of Nerses Bakur
- A vendored text of Sweet's edition of Alfred's preface to the Pastoral Care
- Acts of the Lateran synod of 649 canons condemning Paul of Constantinople, for the African link
- An edition of the acts of the Council of Aquileia (381) with its sentence on Palladius close to Ambrose's questioning, or a clean text of the sentence, for the Ambrose link.
- Anna Komnene, Alexiad 15, on the trial and burning of Basil the Bogomil.
- Bernard Gui, Liber sententiarum (sentences against Cathars), for the Dominican-Cathar link.
- Cite canon 2 of the 585 synod (lines 26710-26718 of its vendored file) on antiochene-exegetical-christianity-chrysostom-ce--the-church-of-the-east-under-persia, then re-judge the link as major (round-2 finding R2-04).
- Cluny's foundation charter (910), to show whether Cluny took the Rule of Benedict through the Carolingian reform
- Cluny's own customaries (e.g. Ulrich's or Bernard's Consuetudines) showing Cluny living by the Rule of Benedict
- Confessions IX.6 or Paulinus's Life of Ambrose naming Ambrose as the bishop who baptized Augustine.
- Cosmas the Priest, Sermon against the Bogomils, and the Interrogatio Iohannis, to test what (if anything) passed from Paulicians to Bogomils to Cathars
- Early Cistercian foundation texts (Exordium Parvum, Carta Caritatis) on keeping the Rule of Benedict
- Eusebius, Church History VII.30.19 on Aurelian's ruling for the church house at Antioch: in the same file (near line 42325) but far outside the cited passage of the Antioch-Rome letter.
- Gratian's Decretum or another later canon collection showing the False Decretals taken into church law
- Innocent III's bull Quia divinae sapientiae (1216) to the Maronites, and William of Tyre, Historia 22.8, on the Maronite union.
- Justinian's edict against Origen (543) or the anathemas of 553 (would test the Jerome, Methodius and Coptic lines against Origen).
- Lucius III, Ad abolendam (1184), naming the Humiliati and the Poor of Lyon (would test the Humiliati condemnation link).
- Paterik of the Kyiv Caves (Kievo-Pechersky Paterik) on Anthony and Athos.
- Peter of Sicily's History of the Paulicians and Anna Comnena's Alexiad on the Paulician settlers at Philippopolis
- The 1255 Anagni protocol or Alexander IV's condemnation of the Introductorius in Evangelium aeternum.
- The Synodikon of Orthodoxy (843), to show the iconophile feast and condemnations adopted by the Macedonian-era church
- The Typikon of Athanasius for the Great Lavra or Athonite foundation acts, for imperial founding of Athonite houses
- The verdict of Marcellinus after the 411 Carthage conference, or the Theodosian Code laws against the Donatists.
- Theophanes' Chronicle on the Paulicians under Michael I, a primary for the persecution of 811-813
