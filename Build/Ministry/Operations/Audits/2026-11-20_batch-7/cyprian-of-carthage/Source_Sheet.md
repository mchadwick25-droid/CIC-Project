# Source sheet: Cyprian of Carthage

Researcher's sheet for batch 7 (2026-11-20). The job: the rhetorician made bishop two years after baptism; his hiding under Decius and the charge it brought; the plague sermon at Carthage; the Unity of the Church and its "mother" line; the quarrel with Stephen of Rome over baptism; his trial and death in 258. Shape: Leader. New card. The writer uses the outline, the shapes and the standard only; this sheet is the evidence behind the outline.

**Files and short names used below** (all in `cic/texts/` unless marked):
- **EP** = `cyprian_epistulae-lat_hartel1871-csel3-tei.txt`: Cyprian's letters in Latin, Hartel's CSEL 3.2 (1871), TEI transcription (corrected OCR). Letter numbers are Hartel's. Apparatus footnotes are the editor's.
- **UNIT** = `cyprian_de-unitate-ecclesiae-catholicae-lat_hartel1868-csel3-tei.txt`: *On the Unity of the Catholic Church*, Latin, Hartel, TEI.
- **MORT** = `cyprian_de-mortalitate-lat_hartel1868-csel3-tei.txt`: *On the Mortality* (the plague address), Latin, Hartel, TEI.
- **LAPS** = `cyprian_de-lapsis-lat_hartel1868-csel3-tei.txt`: *On the Lapsed*, Latin, TEI.
- **DON** = `cyprian_ad-donatum-lat_hartel1868-csel3-tei.txt`: *To Donatus*, Latin, TEI.
- **SENT** = `cyprian_sententiae-episcoporum-lat_hartel1868-csel3-tei.txt`: the *Opinions of the Bishops* at the Carthage council on baptism, Latin, TEI.
- **H3** = `cyprian_opera-spuria-vita-pontius-lat_hartel-csel3-pars3.txt`: Hartel CSEL 3.3 (1871), raw OCR of a scan. Holds the Latin *Life of Cyprian* "commonly attributed to Pontius the deacon" (from 40258) and the *Acta Proconsularia*, the record of his two hearings and death (41413–41628). **Damaged scan**: the running text is legible but noisy ("Deo logratias", "lulianus").
- **KNOPF** = `knopf_ausgewaehlte-maertyrerakten-lat-grc-deu_krueger1929.txt`: Knopf and Krüger, *Ausgewählte Märtyrerakten* (1929), no. 13, the *Acta* of Cyprian in Latin (4818–4962), a clean second print of Hartel's text (its own note, 4961–4962).
- **GEB** = `gebhardt_acta-martyrum-selecta-lat-grc-deu_1902.txt`: Gebhardt, *Acta martyrum selecta* (1902), a third print of the *Acta* (from about 6474).
- **ANF** = `anf05_hippolytus-cyprian-caius-novatian.xml`: Ante-Nicene Fathers vol. 5 (Wallis's English, Coxe's American edition). Holds the Edinburgh editor's introduction (ANF-ed 27511–27526), Pontius's *Life* in English (27656–28303), Cyprian's letters and treatises in English. Coxe's bracketed notes and the introductions are **ANF-ed**. ANF does not hold the *Acta* in English.
- **EUS** = `npnf201_eusebius-church-history-life-of-constantine.xml`: Eusebius, *Church History*, McGiffert's English; McGiffert's notes = **EUS-ed**.
- **NPNF3** = `npnf203_theodoret-jerome-gennadius-rufinus.xml`: Jerome, *Lives of Illustrious Men* 53, 67, 68; Theodoret. Richardson's and Jackson's notes = **NPNF3-ed**.
- **AUG** = `npnf104_augustine-anti-manichaean-anti-donatist.xml`: Augustine, *On Baptism, against the Donatists* (King's English).
- **CONF** = `npnf101_augustine-confessions-letters.xml`: Augustine, *Confessions*.
- **MORIN** = `augustine_sermones-post-maurinos-reperti-lat_morin1930.txt`: Augustine's sermons found after the Maurists, Latin, ed. Morin (1930).
- **PROC** = `procopius_wars-3-4-vandalic_dewing1916.txt`: Procopius, *Vandalic War*, Dewing's English.
- **L7** = `anf07_lactantius-apostolic-constitutions-didache-liturgies.xml`: Lactantius, *Divine Institutes*, English.
- **BEN** = `benson_cyprian-his-life-his-times-his-work_1897.txt`: E. W. Benson, *Cyprian: his Life, his Times, his Work* (1897). A modern biography, OCR in two columns; an editor's voice throughout.
- **KOCH** = `koch_cyprian-und-der-roemische-primat-deu_1910.txt`: Hugo Koch, *Cyprian und der römische Primat* (1910). Modern study.
- **CEN** = `cic-website/data/world-census.json` (not in `cic/texts/`): the entry `cyprian-of-carthage` (not its `longDescription`), and the sibling and tradition entries.

**Conventions.** Line numbers are each file's own. XML and TEI quotes are given with tags, line-break marks and footnotes removed. Latin is quoted as printed (u for v). Square brackets are the translator's or editor's own.

**Language.** Cyprian wrote in Latin. Every quote in the outline is rendered from the Latin of Hartel's TEI texts (EP, UNIT, MORT, SENT), which are clean, and checked against the ANF English. The *Acta* and the Latin of Pontius's *Life* are held in H3 only as a damaged scan; the *Acta* is confirmed by two other prints (KNOPF, GEB), and the *Life* by the ANF English. No quote rests on H3 alone.

**Witness kinds and gaps.**
- OWN = Cyprian's letters and treatises (EP, UNIT, MORT, LAPS, DON, SENT). Rich: some eighty letters, including letters to him.
- CONTEMP, hostile or critical = the Roman clergy's letter (EP Ep. 8); **Firmilian**, bishop of Caesarea in Cappadocia, writing to Cyprian (EP Ep. 75); **Stephen** of Rome, known only as Cyprian quotes him (EP Ep. 74). No letter of Stephen survives on its own.
- CONTEMP, friendly = the *Acta Proconsularia* (KNOPF, GEB, H3): a court-style record of the hearings of 257 and 258 and the death, with a church narrative between them. **The *Life* by Pontius** (ANF 27656–28303; Latin H3 40258–41412): written soon after his death by a deacon who shared his exile, as open praise. Jerome is the witness that Pontius wrote it (NPNF3 40833–40835); the *Life* itself is unsigned, and Hartel's title page says "commonly attributed" (H3 header, line 2).
- LATER = Eusebius, about 70 years later (EUS 39310–39314); Lactantius, about 50 years later (L7 4472–4478); Augustine, about 140 years later (AUG, CONF, MORIN); Jerome, about 135 years later (NPNF3); Theodoret, 5th century (NPNF3 36796–36798); Procopius, 533 (PROC).
- MODERN = ANF-ed, EUS-ed, BEN, KOCH: dates, readings, and the argument over chapter 4 of the *Unity*.

---

## 1. Setting

S1. **Place: Carthage, Roman Africa.** He signs the council of 256 "Cyprianus a Cartagine" (SENT 1514). The council met "from the province of Africa, Numidia, Mauretania" (SENT 105–107). Census `placeLabel` "Carthage", modern Tunisia (CEN). OWN. Documented. Plain words: "Carthage, the great city of Roman Africa, in today's Tunisia".

S2. **Time: 248 to 258.** Census `dates` "248-258" (CEN). Bishop from 248 or 249: Benson reckons from Cyprian's own "quadriennio", four years a bishop, in a letter of 252 (EP Ep. 59.6, 9663; BEN 4266–4290: "the earliest date possible for his accession to be June A.D. 248, the latest possible April A.D. 249"). Death 14 September 258 (I-D below). Plain words: "the middle of the third century".

S3. **Tradition.** Census `toldWithin`: `latin-pastoral-congregational-christianity`. Its spoken name is the entry's `name` (CEN): "the Latin Pastoral Congregations" (the census `sourcing` line uses that form). Plain words: "the Latin-speaking churches of North Africa".

S4. **Emperors.** Decius followed Philip (EUS 37382–37384); McGiffert: Philip died June 249 and Decius reigned "a little" over two years (EUS-ed 37384–37387). Valerian and Gallienus are named in the *Acta* (KNOPF 4821–4824) and in Ep. 80 (EP 17288–17305). Documented.

---

## 2. Events

**E1. Before: a teacher of rhetoric.** Jerome: "Cyprian of Africa, at first was famous as a teacher of rhetoric, and afterwards on the persuasion of the presbyter Caecilius, from whom he received his surname, he became a Christian, and gave all his substance to the poor" (NPNF3 40815–40818). LATER, about 130 years. Lactantius: "he had sought great glory to himself from the profession of the art of oratory" (L7 4475). LATER, about 50 years. Pontius passes over his life before conversion: "He may have had pursuits previously, and liberal arts may have imbued his mind while engaged therein; but these things I pass over" (ANF 27705–27708). Widely Accepted (two later witnesses agree). The ANF editor: "highly educated for the profession of a rhetorician, is all that can be said with any degree of certainty" (ANF-ed 27515–27516).

**E2. Conversion.** Pontius: a presbyter "by name Cæcilius ... who had converted him from his worldly errors" (ANF 27802–27805). He sold estates for the poor while still new to the faith: "by dispensing the purchase-money of entire estates" (ANF 27730–27732). CONTEMP, praise. Documented as Pontius's claim. His own account, *To Donatus*: "While I was still lying in darkness and gloomy night ... I used to regard it as a difficult matter ... that a man should be capable of being born again" (ANF 28370–28376; Latin DON 194: "Ego cum in tenebris atque in nocte caeca iacerem"). OWN. Documented. Year of baptism: "We may perhaps assume that Cyprian received baptism a.d. 246" (BEN 2628); the ANF editor gives "conversion a.d. 246" flatly (ANF-ed 27513–27514). Dominant Modern Reconstruction.

**E3. Made bishop, still a new Christian.** Pontius: "he was chosen to the office of the priesthood and the degree of the episcopate while still a neophyte, and, as it was considered, a novice" (ANF 27818–27821; Latin H3 40554: "adhuc neophytus et ut putabatur nouellus"). He "humbly withdrew, giving place to men of older standing" while the people crowded his doors (ANF 27826–27837). "Some resisted him" (ANF 27844). CONTEMP, praise. Documented as Pontius's account. ANF editor: "not without great objections on the part of older presbyters, who saw themselves superseded by his promotion" (ANF-ed 27521–27523): an editor's gloss on "some resisted". **"Two years after baptism"** rests on editors' dates (246 and 248): Dominant Modern Reconstruction. Pontius gives no year. Plain words for neophyte: "a newly baptized Christian".

**E4. Under Decius: he withdraws, and is hunted.** His own account to the Roman clergy: "at the first outbreak of the trouble, when the people had often demanded me with violent clamour, I withdrew for a while, thinking less of my own safety than of the public peace of the brothers, so that my bold presence should not stir up further the riot that had begun" (EP Ep. 20.1, 2967–2976, my rendering of "cum me clamore uiolento frequenter populus flagitasset, non tam meam salutem quam quietem fratrum publicam cogitans interim secessi"). "Absent in body, I was not absent in spirit, deed or counsel" (EP 2975–2978: "absens tamen corpore nec spiritu nec actu nec monitis meis defui"). He says he sent thirteen letters in that time (EP 2983–2984). OWN. Documented. Later, of the same years: "proscribed in the storm, with the name of my episcopate added, so often demanded for the lion in the circus" (EP Ep. 59.6, 9664–9667: "in tempestate proscriptus, adplicito et adiuncto episcopatus sui nomine, totiens ad leonem petitus, in circo"). OWN. Documented. Pontius: "with repeated calls he was frequently demanded for the lions" (ANF 27879–27880). Decius: the persecution is his by Eusebius (EUS 37378–37384) and the census entry. Plain words: "he went into hiding".

**E5. The charge it brought.** The Roman clergy, whose bishop Fabian had just died, wrote to the clergy of Carthage, not to Cyprian: they had heard he "has for a certain reason withdrawn" (ANF 28796–28799; Latin EP 1055–1056: "Didicimus secessisse benedictum Papatem Cyprianum ... certa ex causa"). They went on to the good shepherd who lays down his life and "the hireling ... seeth the wolf coming, and leaveth the sheep, and fleeth" (ANF 28815–28820; EP 1086–1095), and urged Carthage's clergy not to be "hirelings" (ANF 28838–28839; EP 1099). CONTEMP. Documented that they wrote it. **Whether it was a reproach is the editors' reading**: Coxe, "It seems, in a slight degree, to reflect on Cyprian's withdrawal" (ANF-ed 28832–28833); the translator calls the passage "very obscure" (ANF-ed 28827); Benson calls it "a sarcasm" and Cyprian "the fugitive" in their view (BEN 6697–6705). Contested in its force. Cyprian's answer: "Since I have learned, dear brothers, that what we have done and are doing here has been reported to you less than plainly and faithfully, I thought it necessary to write" (EP Ep. 20.1, 2967–2969: "Quoniam conperi ... minus simpliciter et minus fideliter uobis renuntiari quae hic a nobis et gesta sunt et geruntur"). OWN. Documented. Pontius defends him at length, which shows the charge was alive: "Do you wish to be assured that the cause of his withdrawal was not fear? ... he did suffer subsequently" (ANF 27905–27908). CONTEMP, defence. Documented.

**E6. The lapsed (a clause).** Many gave way: some "ran to the forum of their own accord" to sacrifice (LAPS 8, 345–349: "ultro ad forum currere"). Others got certificates (EP Ep. 15.4, 2465–2473, "libellos"). He would not settle their return alone; the councils of 251 did (sibling story). Documented. Plain words: "those who had given way", "the lapsed".

**E7. Novatian (a clause).** "There came to us, dear brother, sent by Novatian, Maximus a presbyter, Augendus a deacon ... and when we learned ... that Novatian had been made bishop ... we judged at once that they should be kept from our communion" (EP Ep. 44.1, 6186–6194). OWN. Documented. The question of baptism began with Novatian's followers: a layman asked whether those coming "from Novatian" after "his profane washing" must be baptized in the church (EP Ep. 69.1, 13132–13136). OWN. Documented.

**E8. On the Unity of the Church.** Written in 251 at the time of Novatian's split, by the ANF editor's dating and argument (ANF-ed 42105, 42116–42119). Dominant Modern Reconstruction. The images: the church is one as the sun's rays are one light, a tree's branches one trunk, streams one spring; "break a branch from the tree, it cannot bud; cut a stream from its spring, it dries up" (UNIT 5, 341–347). Then: "unum tamen caput est et origo una et una mater fecunditatis successibus copiosa: illius fetu nascimur, illius lacte nutrimur, spiritu eius animamur" (UNIT 352–355; ANF 42310–42312: "she is one mother, plentiful in the results of fruitfulness: from her womb we are born, by her milk we are nourished, by her spirit we are animated"). Chapter 6: "alienus est, profanus est, hostis est. habere non potest Deum patrem qui ecclesiam non habet matrem. si potuit euadere quisque extra arcam Noe fuit, et qui extra ecclesiam foris fuerit euadit" (UNIT 6, 363–366; ANF 42320–42323: "He is a stranger; he is profane; he is an enemy. He can no longer have God for his Father, who has not the Church for his mother"). OWN. Documented. **Quote 1.**

**E9. The plague.** Pontius: "Afterwards there broke out a dreadful plague ... All were shuddering, fleeing, shunning the contagion, impiously exposing their own friends" (ANF 27939–27944; Latin H3 40783 "lues dira"). He gathered the people and urged mercy: "there was nothing wonderful in our cherishing our own people only ... but that he might become perfect who would do something more than the publican or the heathen ... loved even his enemies" (ANF 27957–27966). Then "good was done ... to all men, not to those only who are of the household of faith" (ANF 27990–27992). CONTEMP, praise. Documented as Pontius's account. Date: the ANF heading, from Eusebius's *Chronicle*, "a.d. 252" (ANF-ed 46658–46663). Widely Accepted. *On the Mortality*, his own address on it: the symptoms, "the bowels ... loosened into a flow", fever in the throat, vomiting, eyes burning with blood, feet or limbs lost (MORT 14, 498–505). OWN. Documented. Then chapter 16: "pestis ista et lues quae horribilis et feralis uidetur explorat iustitiam singulorum et mentes humani generis examinat, an infirmis seruiant sani, an propinqui cognatos pie diligant, an misereantur seruorum languentium domini, an deprecantes aegros non deserant medici" (MORT 584–588; ANF 47051–47057). OWN. Documented. **Quote 2.** And: "exercitia sunt nobis ista, non funera" (MORT 595–596; ANF 47066: "These are trainings for us, not deaths"). And: our dead are "not lost, but sent before" (MORT 20, 696–700; ANF 47143–47145). Note: the urging to care for pagan sick is in Pontius, not in *On the Mortality* (D6).

**E10. The quarrel with Stephen of Rome over baptism.**
- *What was at issue.* Cyprian and the African councils held that those baptized in a group outside the church, by heretics or schismatics, must be baptized when they came in: "heretics coming to the church ought to be baptized and sanctified with the church's baptism" (SENT 116–118). OWN. Documented. He cites an older African council under Agrippinus for it (EP Ep. 71.4, 14273–14278; Ep. 73.3, 14546–14550). Rome received them by the laying on of hands alone.
- *Stephen's words, as Cyprian quotes them.* "If any come to you from any heresy whatever, let nothing new be done beyond what has been handed down: that hands be laid on them for repentance, since the heretics themselves do not baptize those who come to them from one another, but only receive them to communion" (EP Ep. 74.1, 15424–15433: "si qui ergo a quacumque haeresi uenient ad uos, nihil innouetur nisi quod traditum est, ut manus illis inponatur in paenitentiam"). Stephen's own letter is lost; only Cyprian's extract is held. Cyprian, writing to a colleague, calls Stephen's letter "proud, or beside the point, or self-contradictory" (EP 15427–15428) and his "error" (15426). OWN, hostile. Documented as quoted.
- *The council of 1 September.* 87 bishops "from the province of Africa, Numidia, Mauretania, with presbyters and deacons, and a great part of the people present" (SENT 105–108; title 105: "NVMERO LXXXVII"). Cyprian's opening: "neque enim quisquam nostrum episcopum se episcoporum constituit aut tyrannico terrore ad obsequendi necessitatem collegas suos adigit" (SENT 140–142; AUG 11292). OWN. Documented. **Quote 3.** Year: 256 in most sources; the ANF heading gives 258 (corpus-map note at `latin-pastoral-congregational-christianity.yaml` 15706–15707). Dominant Modern Reconstruction for 256.
- *Stephen's response, by a hostile witness.* Firmilian, bishop of Caesarea in Cappadocia, wrote to Cyprian that Stephen received the African envoy-bishops so "patiently and gently" (irony) that he would not admit them even to talk, and told all the brothers to refuse them "not only peace and communion but even a roof and lodging" (EP Ep. 75.25, 16664–16673). That Stephen "boasts of the place of his episcopate and contends that he holds the succession from Peter" (EP 16447–16449). That Stephen called Cyprian "a false Christ and a false apostle and a deceitful worker" (EP 16707–16710: "Cyprianum pseudochristum et pseudoapostolum et dolosum operarium dicere"). And to Stephen: "you have cut yourself off ... while you think all can be cut off by you, you have cut yourself off from all" (EP 16633–16637). CONTEMP, hostile to Stephen. Documented as Firmilian's claims. Eusebius: "Stephen considering it unnecessary to add any innovation contrary to the tradition which had been held from the beginning, was very indignant at this" (EUS 39311–39314). LATER.
- *How it ended.* Stephen died in 257; his successor Xystus, by McGiffert, "seems to have adopted a more conciliatory tone" (EUS-ed 39431–39434). Pontius calls Xistus "the good and peace-making priest" (ANF 28138). The record holds no reconciliation between Cyprian and Stephen. Documented that no settlement is held.

**E11. Exile, 257.** First hearing, 30 August 257, before the proconsul Paternus: "Cyprianus episcopus dixit: Christianus sum et episcopus. nullos alios deos noui, nisi unum et uerum deum" (KNOPF 4828–4830; GEB 6489; H3 41421). Asked for his presbyters' names, he would not inform: "your laws have rightly forbidden informers" (KNOPF 4839–4841). Sent into exile at Curubis (KNOPF 4836, 4850–4851). CONTEMP record. Documented. The dream at Curubis is Pontius's story (Do not tell here).

**E12. The new edict, and the second hiding, 258.** Ep. 80: Valerian ruled that bishops, presbyters and deacons be put to death at once; Xistus of Rome was beheaded in a cemetery "on the eighth day before the Ides of August" with four deacons (EP 17288–17320). OWN. Documented. Ep. 81, his last letter: officers were sent to take him to Utica; on friends' advice he left his gardens for a while, "because it is fitting that a bishop confess the Lord in the city where he leads the Lord's church, and bring glory to all his people by confessing in their presence" (EP Ep. 81, 17369–17373: "eo quod congruat episcopum in ea ciuitate in qua ecclesiae dominicae praeest illic Dominum confiteri et plebem uniuersam praepositi praesentis confessione clarificare"). He would wait in hiding for the proconsul's return to Carthage (EP 17375–17377). OWN. Documented.

**E13. Trial and death, 13 and 14 September 258.** Arrested at his gardens on the Ides of September, consuls Tuscus and Bassus (KNOPF 4856–4857). The people kept watch all night at the officer's door; he had the young women guarded (KNOPF 4877–4880; Pontius ANF 28184–28186). Next day, the eighteenth before the Kalends of October, the proconsul Galerius Maximus: "Tu es Thascius Cyprianus? ... Ego sum. ... Tu papam te sacrilegae mentis hominibus praebuisti? ... Ego. ... Iusserunt te sacratissimi imperatores caeremoniari. ... Non facio. ... Consule tibi! ... Fac, quod tibi praeceptum est. in re tam iusta nulla est consultatio" (KNOPF 4882–4896). The sentence: he had lived long "with a sacrilegious mind", was an "enemy of the Roman gods", a "standard-bearer" of crimes; "sanguine tuo sancietur disciplina"; "Thascium Cyprianum gladio animaduerti placet. Cyprianus episcopus dixit: Deo gratias" (KNOPF 4900–4911; GEB 6625–6626; H3 41577–41579). The crowd: "Et nos cum ipso decollemur" (KNOPF 4914–4915). At the field of Sextus he took off his cloak, knelt and prayed, gave his tunic to the deacons, stood in his linen, ordered **twenty-five gold pieces** given to the executioner; the brothers spread cloths before him; "beatus Cyprianus manu sua oculos sibi texit. qui cum lacinias manuales ligare sibi non potuisset, Iulianus presbyter et Iulianus subdiaconus ei ligauerunt" (KNOPF 4917–4927). His body was carried by night with tapers to a burial ground on the Mappalian road (KNOPF 4950–4952). CONTEMP record. Documented. Pontius, the same day: people "had climbed up into the branches of the trees"; "having with his own hands bound his eyes, he tried to hasten the slowness of the executioner ... who with difficulty clasped the blade in his failing right hand with trembling fingers" (ANF 28254–28264; Latin H3 41351–41357: "ligatis per manus suas oculis ... uix trementibus digitis"). CONTEMP, praise. Documented as Pontius's account. Pontius: the first bishop of Carthage to die a martyr (ANF 28277–28285). Date: the *Acta* close, "Passus est ... die octaua decima kalendarum Octobrium" (KNOPF 4955–4956), that is 14 September. Year 258 from the consuls; Documented in the ANF editor's dating (ANF-ed 27525–27526) and EUS-ed 39310 note. Widely Accepted.

---

## 3. Impact (heaviest first)

I1. **Augustine and the Donatists: both sides claimed him.** The Donatists quoted his letters and council for rebaptism; Augustine answered: "Cease, then, to bring forward against us the authority of Cyprian in favor of repeating baptism, but cling with us to the example of Cyprian for the preservation of unity" (AUG 11416, *On Baptism* 2.7.12). He quotes the "bishop of bishops" line again and again (AUG 11292, 11626, 12207, 13405), and comments: "What could be more kind? what more humble?" (AUG 11626). He held Cyprian wrong on baptism but faithful to unity: "though he held a different view concerning baptism, he yet did not forsake the unity of the Church, and was in the Lord's vine a branch firmly rooted, bearing fruit, which the heavenly Husbandman purged with the knife of suffering" (AUG 11949). LATER, about 140 years. Documented. Census `relationsSummary` and `legacy` agree (CEN).

I2. **His feast at Carthage.** Augustine preached on "the birthday of blessed Cyprian", the day of his death (MORIN 17206–17212; 61608; 68575). His mother spent a night at "an oratory in memory of the blessed Cyprian" by the harbour (CONF 8103–8104). In 533 Procopius: "Cyprian, a holy man, is reverenced above all others by the Carthaginians", with a temple by the sea and a festival, the "Cypriana", which the Vandals had seized for the Arians (PROC 2206–2216). LATER. Documented.

I3. **His writings read and copied.** Lactantius: "Cyprianus ... was above all others distinguished and renowned" for eloquence (L7 4472–4475). Jerome: his works "are more conspicuous than the sun" (NPNF3 40820–40821). Pontius: "he will probably never cease to speak even to the end of the world" (ANF 27671–27672). Documented.

I4. **The "mother" line and the Unity in later argument.** The ANF editor calls the treatise "a key to the entire writings of Cyprian" (ANF-ed 42107–42109). Chapter 4 became a battleground between those who read it for and against the authority of Rome (D1). Editor's view; Widely Accepted that it was argued over.

I5. **Tertullian read daily (link, a clause).** Jerome had it from an old man who had been Cyprian's secretary that he never passed a day without reading Tertullian (NPNF3 40500–40505). LATER, hearsay at two removes. That story belongs to `tertullian-s-voice`.

Defended: the one church, outside which there is no salvation (E8), and a bishop's freedom in his own church against compulsion (E10, SENT 140–145).

---

## 4. Links to other people

- **Pontius the Deacon** (`pontius-the-deacon`): shared his exile, wrote his *Life* (NPNF3 40833–40835). Credited here as the witness of the death.
- **Novatian** (`novatian`): Cyprian refused his envoys (E7).
- **Councils of 251** (`councils-of-rome-and-carthage-251`): Cyprian called the Carthage council on the lapsed (council entry `people`).
- **Tertullian** (`tertullian-s-voice`): read him daily, by Jerome's report (I5).
- **Dionysius of Alexandria** (`dionysius-of-alexandria`): agreed with Cyprian on rebaptism, by Jerome (NPNF3 40844–40846); his letters to Stephen and Xystus are his own story.
- **Lactantius** (`lactantius`): praised his eloquence and criticised his *To Demetrianus* (L7 4472–4478, 4571). His story's link.
- **Augustine of Hippo** (`augustine-of-hippo`): argued over him against the Donatists (I1); preached on his feast (I2).
- **Jerome** (`jerome`): his short Life (NPNF3 40815–40826).
- **Eusebius of Caesarea** (`eusebius-of-caesarea`): the baptism quarrel (EUS 39310–39314).
- **Procopius of Caesarea** (`procopius-of-caesarea`): the Cypriana at Carthage (I2).
- **Donatism** (`donatism`): quoted him for their break (CEN `relationsSummary`).
- Not on the tree: Stephen of Rome, Firmilian, Cornelius, Xistus, Caecilius, Galerius Maximus, Paternus.

---

## 5. Where sources disagree or come late

D1. **Chapter 4 of the Unity: two texts.** Hartel prints a text without the words "primatus Petro datur" and "cathedra Petri", and puts them in the apparatus as additions found in some manuscripts (UNIT 270–290). Benson calls them "the famous interpolation" (BEN 729, 11938). The ANF editor: "falsifying interpolations, long since exposed and detected" (ANF-ed 42113–42115). Chapman, as Koch reports him, argued that Cyprian himself wrote both forms (KOCH 8083–8098, citing Chapman 1903); Koch doubts it (KOCH 8070–8087). Contested. Card only; the quote is from chapter 6, which is not in dispute.

D2. **How he bound his eyes.** The *Acta*: he covered his eyes with his own hand, but could not tie the cloths, and the presbyter Julian and the subdeacon Julian tied them (KNOPF 4925–4927). Pontius: "having with his own hands bound his eyes" (ANF 28260–28261; H3 41355). Credit each.

D3. **The executioner.** The *Acta*: Cyprian ordered twenty-five gold pieces given to him (KNOPF 4923–4924). Pontius: the executioner's hand shook until it was strengthened "from above" (ANF 28261–28266). Different details, not a contradiction; the strengthening is Pontius's reading, in his voice.

D4. **Withdrawal at the end.** Pontius: friends urged him to withdraw before the arrest and offered places, but he "did not consent" (ANF 28142–28149). Cyprian's own last letter: on friends' advice he did leave his gardens for a while, to avoid being taken to Utica and to die in Carthage (EP 17369–17377). Credit each.

D5. **The manner of death in a later writer.** Theodoret says Cyprian "found a death in the fire" (NPNF3 36797–36798); the editor corrects him from the *Acta* but gives the date as "Aug. 13, 258" (NPNF3-ed 36798–36800), against the *Acta*'s 14 September. Leave out.

D6. **Who told whom to nurse the pagan sick.** Pontius says Cyprian urged care for all, "not to those only who are of the household of faith" (ANF 27990–27992). *On the Mortality* tests whether "the healthy serve the sick" but does not mention pagans (MORT 584–588). The tradition entry's summary merges them (CEN). Credit the pagan sick to Pontius.

D7. **Who first held rebaptism.** Eusebius: "First of all, Cyprian ... maintained that they should not be received except they had been purified ... by baptism" (EUS 39310–39312). Cyprian himself: an African council under Agrippinus "long ago" had decided it (EP 14546–14550). Augustine also names Agrippinus before him (AUG 11606). Credit each.

D8. **The "bishop of bishops" line: aimed at Stephen or not.** Benson: it "states the position of tolerance which he takes as against one who wants to make himself a bishop of bishops" (BEN 21457–21461), against those who read the speech as a peace offer (BEN 21452). Augustine reads it as kindness and humility (AUG 11626). Contested. The story says he spoke it at the council, in the months of the quarrel, and lets the listener hear it; it does not say it named Stephen.

D9. **"Two years after baptism."** No ancient source gives it. Pontius: still a neophyte (E3). Editors: 246 and 248 (E2, E3). Say "about two years after his baptism, by modern reckoning", or "while still a new Christian".

D10. **The Roman letter's tone** (E5): Coxe "in a slight degree"; Benson "a sarcasm". Contested.

---

## 6. Wanted but not held

- No English of the *Acta Proconsularia* is held; renderings from it are made from KNOPF's Latin.
- No letter of Stephen survives apart from Cyprian's extract.
- Augustine's sermons on Cyprian (Sermons 309–313) are held only in part (MORIN), in Latin; no English.
- Prudentius's hymn on Cyprian (*Peristephanon* 13) is not held.

---

## Library sweep

**What I searched.** The census entry (fields other than `longDescription`), the tradition entry `latin-pastoral-congregational-christianity` (text and `documentedStories`), and the sibling entries `pontius-the-deacon`, `novatian` and `councils-of-rome-and-carthage-251` (live text; the council entry's fields). No card exists for this entry. `cic/corpus-map/latin-pastoral-congregational-christianity.yaml` (380 lines naming Cyprian, 45 source files); `donatism.yaml`, `novatianism.yaml`, `roman-church-third-century.yaml`, `latin-apologists.yaml`, `latin-africa-under-byzantium.yaml`, `montanism-the-new-prophecy.yaml`; `WORKS.yaml` (`cyprian-epistulae`, 140–161), `AUTHOR-IDS.yaml` and `RETRIEVAL-HINTS.md` (no further name forms). A search of `cic/texts/` for "Cyprian", "Cypriani", "Cypriano", "Cyprianus", "Cyprianum", "Cyprien", "Kyprian", "Κυπριαν", "Thascius", "Caecilius Cyprianus", and for the quote lines in Latin and English ("habere non potest Deum patrem", "episcopum se episcoporum", "explorat iustitiam", "Deo gratias", "non amitti sed praemitti").

**How many files.** About 820 files carry one of those name forms; many are other Cyprians (Cyprian of Toulon, Cyprian of Antioch) or passing mentions. About 45 are mapped to his tradition; about 30 more carry him on (Augustine, Optatus, Procopius, Jerome, Lactantius, Eusebius, Theodoret).

**Used.** EP, UNIT, MORT, LAPS, DON, SENT (his own words); KNOPF, GEB and H3 (the *Acta*); ANF (Pontius in English, his works in English, editors' notes); H3 (Pontius in Latin, for checking); EUS; NPNF3; AUG; CONF; MORIN; PROC; L7; BEN and KOCH (dates and the chapter 4 dispute, as editors).

**Set aside, and why.**
- `cyprian_opera-omnia-critical_hartel-csel3-pars1-2.txt`: the scan behind the TEI files; the TEI is cleaner and the same edition.
- `harnack_vita-cypriani-commentary-lat-deu_1913.txt`: Harnack's commentary on the *Life*; useful for Pontius's own story, not needed here.
- `cyprian_oeuvres-completes-*-fra_guillon1837.txt`, `cyprian_ausgewaehlte-schriften-band1-deu_uhl-bkv1869.txt`: French and German translations; the Latin and the ANF English are held.
- `vonsoden_*`, `koch_cyprianische-untersuchungen-deu_1926.txt`, `koch_cathedra-petri-deu_1930.txt`, `dales_*`, `monceaux_*`, `bardenhewer_*`, `hefele-leclercq_*`, `duchesne_*`: modern studies on the letter collection, the baptism quarrel, the African bishops; nothing the primary texts do not hold for this story's claims.
- `augustine_scripta-contra-donatistas-*` (Latin), `augustine_oeuvres-completes-*-donatistes-*`: the Latin and French of the Augustine used in English (AUG).
- `optatus_*`: Optatus on the Donatists; carries Cyprian only in passing.
- `anf05` *Treatise against Novatian* and *On Rebaptism*: anonymous, by others; the second argues against Cyprian's side and is for the card at most.
- `npnf214_seven-ecumenical-councils.xml` (the 256 council in English): the Latin SENT is held clean.
- `acta-sanctorum_*` and later lives: medieval, built on the *Acta* and Pontius.
