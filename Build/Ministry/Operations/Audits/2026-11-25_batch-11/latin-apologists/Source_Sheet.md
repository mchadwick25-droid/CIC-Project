# Source sheet: The Latin Apologists (`latin-apologists`)

Every line number is a file line in `cic/texts/<file>`. Witness kinds: **own** (the subject's own words), **contemporary**, **later** (with rough gap), **late legend**. Confidence uses the project's five levels. Abbreviations for files:

- **ANF3** `anf03_tertullian.xml` (Edinburgh/Coxe English, printed 1885)
- **ANF4** `anf04_tertullian4-minucius-felix-commodian-origen1-2.xml` (English, 1885)
- **ANF6** `anf06_gregory-thaumaturgus-dionysius-julius-africanus-methodius-arnobius.xml` (English, 1886)
- **ANF7** `anf07_lactantius-apostolic-constitutions-didache-liturgies.xml` (Fletcher's English, 1886)
- **NPNF2-3** `npnf203_theodoret-jerome-gennadius-rufinus.xml` (Jerome, Lives of Illustrious Men, English, 1892)
- **NPNF2-6** `npnf206_jerome-principal-works.xml` (Jerome's letters, English, 1893)
- **NPNF1-3** `npnf103_augustine-holy-trinity-doctrinal-moral-treatises.xml` (English, 1887)
- **MinLat** `minucius-felix_octavius-lat_halm1867-csel2-tei.txt` (Halm, CSEL 2, 1867; clean TEI)
- **ArnLat** `arnobius_adversus-nationes-lat_reifferscheid1875-csel-tei.txt` (Reifferscheid, CSEL 4, 1875; clean TEI); scan twin `arnobius_adversus-nationes-lat_reifferscheid-csel4.txt`
- **JerChron** `jerome_eusebii-chronici-canones-lat_fotheringham1923.txt` (Fotheringham 1923; OCR damaged in places)
- **Monc3** `monceaux_histoire-litteraire-afrique-chretienne-tome3_1905.txt` (Monceaux 1905; prints Jerome's Chronicle Latin)
- **LactLat** `lactantius_divinae-institutiones-lat_brandt1890-csel-tei.txt` (Brandt, CSEL 19, 1890; clean TEI)
- **TertLat1** `tertullian_quae-supersunt-t1-apologetica-lat_oehler1853.txt` (Oehler 1853; OCR noisy)
- **AugLat** `augustine_arian-sermon-collatio-maximinum-pl42-lat_migne1886.txt` (PL 42, holds De Trinitate)

---

## 1. Setting

| Claim | File and lines | Witness | Confidence | Verbatim |
|---|---|---|---|---|
| Minucius Felix was a pleader (advocate) at Rome | NPNF2-3 40646-40649 | later, Jerome c. 392 (gap uncertain, Minucius undated) | Documented | "Felix, a distinguished advocate of Rome, wrote a dialogue representing a discussion between a Christian and a Gentile, which is entitled Octavius" |
| Lactantius: Minucius "of no ignoble rank among pleaders" | ANF7 4470; LactLat 22701-22705 | contemporary-to-later (Lactantius, c. 305-310, gap to Minucius unknown) | Documented | "Of those who are known to me, Minucius Felix was of no ignoble rank among pleaders." / "ex iis qui mihi noti sunt Minucius Felix non ignobilis inter causidicos loci fuit." |
| The Octavius is a memory of a dead friend; Minucius and Octavius were both converts | ANF4 17195-17221 | own (Minucius) | Documented | "that remarkable and holy man, when he departed this life, left to me an unbounded regret for him" … "when, after the gloom had been dispersed, I emerged from the abyss of darkness into the light of wisdom and truth, he did not cast off his associate" |
| Octavius came to Rome on business, leaving wife and small children | ANF4 17235-17240 | own | Documented | "Octavius had hastened to Rome, having left his home, his wife, his children" |
| Court holiday at vintage; autumn; walk to the sea at Ostia, early morning | ANF4 17247-17255; MinLat 210-222 | own | Documented | "we agreed to go to that very pleasant city Ostia … especially as the holidays of the courts at the vintage-time had released me from my cares … when in the early morning we were going towards the sea along the shore" / "ad uindemiam feriae iudiciariam curam relaxauerant … cum diluculo ad mare inambulando litore pergeremus" |
| Date of the Octavius: not fixed; Jerome's editor puts "196?"; ANF editor's note "probably written in Cirta, circa A.D. 210" | NPNF2-3 40646; ANF4 18998-19001 | modern (editors' notes) | Contested | ANF note: "this suggests that the Octavius was probably written in Cirta, circa a.d. 210." (editor's claim, not a witness) |
| Tertullian: from Carthage; flourished under Severus and Caracalla; presbyter | NPNF2-3 40493-40499 | later, Jerome c. 392 (c. 180 years) | Widely Accepted | "was from the city of Carthage in the province of Africa … he flourished chiefly in the reign of the emperor Severus and Antoninus Caracalla" |
| Jerome ranks Tertullian "chief of the Latin writers after Victor and Apollonius" (so not the first Latin Christian writer) | NPNF2-3 40494-40495 | later | Documented | "now regarded as chief of the Latin writers after Victor and Apollonius" |
| Apology addressed to the rulers who sat in judgment | ANF3 1448-1453 | own | Documented | "Rulers of the Roman Empire, if, seated for the administration of justice on your lofty tribunal …" (the opening sentences are barred as quotes; facts only) |
| Apology date disputed among critics | ANF3 1443-1446 | modern (editor) | Contested | "Great diversity exists among the critics as to the date of this Apology … Mosheim says, a.d. 198, Kaye a.d. 204." |
| Arnobius taught rhetoric at Sicca in Africa under Diocletian | NPNF2-3 41022-41025 | later, Jerome c. 392 (c. 90 years) | Documented | "was a most successful teacher of rhetoric at Sicca in Africa during the reign of Diocletian, and wrote volumes Against the nations which may be found everywhere." |
| Jerome's Chronicle sets Arnobius among Constantine's years (c. 326/327) | JerChron 45066 (entry XXI, after Crispus's death 45054-45056 and the vicennalia 45059); ANF6 39071-39079 | later; ANF intro notes the clash with DVI | Contested (date) | JerChron: "XXI • Arnobius rhetor in Africa clarus habetur" / ANF6: "It must at once be seen that there is here a mistake" (editor's opinion: not used) |
| Lactantius, Arnobius's pupil, called to Nicomedia under Diocletian to teach rhetoric; few pupils in a Greek city; turned to writing | NPNF2-3 41033-41038 | later, Jerome (c. 70 years) | Documented (pupil link rests on Jerome alone) | "Firmianus, known also as Lactantius, a disciple of Arnobius, during the reign of Diocletian summoned to Nicomedia … taught rhetoric there and on account of his lack of pupils (since it was a Greek city) he betook himself to writing." |
| Lactantius's own word: teaching rhetoric in Bithynia when "the temple of God was overthrown" | ANF7 4487; LactLat 22774-22775 | own | Documented | "When I was teaching rhetorical learning in Bithynia, having been called thither, and it had happened that at the same time the temple of God was overthrown" / "ego cum in Bithynia oratorias litteras accitus docerem contigissetque ut eodem tempore dei templum euerteretur" |
| Arnobius wrote while scriptures were burned and meeting-places torn down | ANF6 48676-48684; ArnLat 7436-7440 | own | Documented (that he says so); ANF note "generally thought to refer" to Diocletian's persecution = modern | "why, indeed, have our writings deserved to be given to the flames? our meetings to be cruelly broken up" / "nam nostra quidem scripta cur ignibus meruerunt dari? cur immaniter conuenticula dirui" |

## 2. Events (in time order where the record allows)

### 2a. The beach at Ostia (Minucius Felix, Octavius; date Contested)

| Claim | File and lines | Witness | Confidence | Verbatim |
|---|---|---|---|---|
| Caecilius sees an image of Serapis, raises his hand to his mouth and kisses it (he kisses his own hand toward the image) | ANF4 17256-17258; MinLat 222-224 | own (Minucius) | Documented (as Minucius tells it) | "Cæcilius, observing an image of Serapis, raised his hand to his mouth, as is the custom of the superstitious common people, and pressed a kiss on it with his lips." / "Caecilius simulacro Serapidis denotato, ut uulgus superstitiosus solet, manum ori admouens osculum labiis inpressit." |
| Octavius rebukes Minucius for letting his friend bow to anointed, garlanded stones | ANF4 17267-17273; MinLat 235-238 | own | Documented | "to give himself up to stones, however they may be carved into images, anointed and crowned" / "in lapides eum patiaris inpingere, effigiatos sane et unctos et coronatos" |
| Boys skimming shells by the beached boats; Caecilius stands apart, silent | ANF4 17291-17313 | own | Documented | "we saw some boys eagerly gesticulating as they played at throwing shells into the sea" … "Cæcilius was paying no attention … silent, uneasy, standing apart" |
| Caecilius asks to argue; they sit on the stone breakwater, Minucius in the middle as judge | ANF4 17321-17331 | own | Documented | "Let us be seated on those rocky barriers that are cast there for the protection of the baths, and that run far out into the deep" |
| Caecilius's charge: gathered from the dregs, the unlearned and credulous women; night meetings, fasts, "inhuman meats"; lurking, light-shunning | ANF4 17582-17592; MinLat 822-828 | own (Minucius voicing a pagan's case) | Documented (that the charge was made) | "a people skulking and shunning the light, silent in public, but garrulous in corners" / "latebrosa et lucifuga natio, in publicum muta, in angulis garrula" (Halm note 862-863: the manuscript reads "lucifugax"; same sense) |
| Caecilius's charge: secret signs, "brothers and sisters" made incest; ass's head; a crucified criminal; infant covered in meal killed by the novice; incest feasts where a dog tied to the lamp puts out the light; cites "our Cirtensian" (Fronto)'s speech | ANF4 17613-17670; MinLat 894, 914, 927, 947 | own (pagan voice as Minucius writes it) | Documented (charge) | "An infant covered over with meal … is placed before him who is to be stained with their rites" / "infans farre contectus, ut decipiat" ; "a dog that has been tied to the chandelier is provoked … the conscious light being overturned and extinguished" |
| Caecilius's charge: no altars, temples or images; one unseen God who pries into everything; they threaten the world with fire and promise rising again | ANF4 17680-17742 | own (pagan voice) | Documented (charge) | "Why have they no altars, no temples, no acknowledged images?" |
| Octavius: we were once the same; as advocates we defended the worst but would not hear Christians, and tortured them to make them deny | ANF4 18824-18848; MinLat 3138-3148 | own | Documented | "Believe us ourselves when penitent, for we also were the same as you, and formerly, while yet blind and obtuse, thought the same things as you" … "we were more cruelly violent against them, so as to torture them when they confessed, that they might deny" |
| Octavius: our banquets are modest and sober; one marriage or none; we are not "garrulous in corners"; we love one another because we do not know how to hate; we call one another brothers | ANF4 19018-19044; MinLat 3543, 3559-3563 | own | Documented | "we love one another, to your regret, with a mutual love, because we do not know how to hate" / "sic nos mutuo, quod doletis, amore diligimus, quoniam odisse non nouimus" |
| Octavius: no temple can hold God; the offering is a good mind; the just man is the most religious | ANF4 19058-19076 | own | Documented | "the victim fit for sacrifice is a good disposition, and a pure mind, and a sincere judgment" |
| Octavius: God sees all, "we live not only in His eyes but in His bosom" | ANF4 19115-19121; MinLat 3704-3708 | own | Documented | "non enim solum in oculis eius, sed in sinu uiuimus" |
| Minucius: Octavius beat them "with the very weapons of the philosophers" | ANF4 19475-19483; MinLat 4392-4398 | own | Documented | "he had repelled the malevolent objectors with the very weapons of the philosophers with which they are armed" / "maleuolos isdem illis quibus armantur, philosophorum telis retudisset" |
| Caecilius yields: "he is my conqueror, I triumph over error"; the rest postponed till morning as the sun sets | ANF4 19492-19508; MinLat 4410-4425 | own | Documented | "nam ut ille mei uictor est, ita ego triumphator erroris" … "de quibus crastino, quod iam sol occasui decliuis est" |
| All three leave glad | ANF4 19523-19526; MinLat 4464-4466 | own | Documented | "Post haec laeti hilaresque discessimus, Caecilius quod crediderit, Octauius gaudere quod uicerit, ego et quod hic crediderit et hic uicerit." |

### 2b. Tertullian at Carthage (short turn; his own page tells his life)

| Claim | File and lines | Witness | Confidence | Verbatim |
|---|---|---|---|---|
| The same charges answered: child killed and eaten in a rite, incest after the feast, dogs overturning the lights | ANF3 1946-1950 | own | Documented | "we are accused of observing a holy rite in which we kill a little child and then eat it; in which, after the feast, we practise incest, the dogs—our pimps, forsooth, overturning the lights" |
| The executioner made to force denial, not confession | ANF3 1956-1958 | own | Documented | "he is not to make them confess what they do, but to make them deny what they are" |
| The ass's-head charge traced to Tacitus | ANF3 10078-10093 (Ad Nationes I.11, citing Apology 16) | own | Documented | "some among you have dreamed that our god is an ass's head,—an absurdity which Cornelius Tacitus first suggested" |
| Christian gathering: prayer together, for emperors and peace; reading Scripture; elders by character; monthly voluntary gift; spent on burying the poor, orphans, old people kept at home, shipwrecked, those in mines, islands, prisons | ANF3 3868-3907 | own | Documented | "On the monthly day, if he likes, each puts in a small donation … but to support and bury poor people, to supply the wants of boys and girls destitute of means and parents, and of old persons confined now to the house; such, too, as have suffered shipwreck" |
| Pagans brand them for it: "See, they say, how they love one another" | ANF3 3907-3913; TertLat1 26759-26763 (OCR noisy; ANF confirms) | own | Documented | "it is mainly the deeds of a love so noble that lead many to put a brand upon us. See, they say, how they love one another" / "notam nobis inurit penes quosdam. Vide, inquiunt, ut invicem se diligant" |
| The love feast: prayer first, eat to hunger, hymns sung by each, prayer at the close | ANF3 3953-3975 | own | Documented | "each is asked to stand forth and sing, as he can, a hymn to God, either one from the holy Scriptures or one of his own composing" |
| Latin believers mouth the Greek word "monarchia" (borrowed word) | ANF3 51176-51186 | own (Against Praxeas 3) | Documented | "We, say they, maintain the Monarchy … And so, as far as the sound goes, do even Latins (and ignorant ones too) pronounce the word" |
| Later joined the New Prophecy, after "the envy and abuse of the clergy of the Roman church" (Jerome); wrote On fasts, On monogamy | NPNF2-3 40506-40513 | later, Jerome | Contested (motive is Jerome's; the Montanism story owns this) | "afterwards driven by the envy and abuse of the clergy of the Roman church, he lapsed to the doctrine of Montanus, and mentions the new prophecy in many of his books." |
| Wrote against Marcion, who brought in two Gods | ANF3 22609-22612 | own | Documented | "The heretic of Pontus introduces two Gods … One whom it was impossible to deny, i.e. our Creator; and one whom he will never be able to prove, i.e. his own god." |
| Tertullian names Justin among earlier writers (Greek forerunners) | ANF3 43160-43163 | own | Documented | "for instance Justin, philosopher and martyr" |

### 2c. The convert at Sicca (Arnobius; Jerome alone for the conversion)

| Claim | File and lines | Witness | Confidence | Verbatim |
|---|---|---|---|---|
| Teaching young men declamation at Sicca, still a pagan, driven to belief by dreams; the bishop would not grant him the faith he had always attacked; he wrote brilliant books against his old religion; "as if by hostages of devotion" won the covenant | JerChron 45066-45082 (OCR: "dedamandum", "ncque", "ptetatts"); Monc3 21709-21714 prints the same Latin cleanly from "neque" on; ANF6 39072-39077 (English, partial) | later, Jerome's Chronicle c. 380 (c. 80 years) | Documented that Jerome says it; the story rests on him alone | "qui cum Siccae ad declamandum iuuenes erudiret et adhuc ethnicus ad credulitatem somniis compelleretur, neque ab episcopo impetraret fidem quam semper inpugnauerat, elucubrauit aduersum pristinam religionem luculentissimos libros et tandem ueluti quibusdam obsidibus pietatis foedus impetrauit." (normalized from JerChron; Monc3: "neque ab episcopo impetraret fidem quam semper impugnaverat, elucubravit adversum pristinam religionem luculentissimos libros, et tandem veluti quibusdam obsidibus pietatis fœdus impetravit") |
| Arnobius's pupil was Lactantius; seven books | NPNF2-6 16713-16716; NPNF2-3 41033-41035 | later, Jerome | Documented (Jerome alone) | "Arnobius has published seven books against the Gentiles, and his pupil Lactantius as many" |
| The charge he answers: since Christians came, the world has gone to ruin and the gods have left | ANF6 39480-39515; ArnLat 110-116 | own | Documented | "that from the time when the Christian people began to exist in the world the universe has gone to ruin … the very gods … have been driven from the regions of earth" / "postquam esse in mundo Christiana gens coepit, terrarum orbem perisse" |
| His own past: worshipped furnace-made images, fawned on an oiled stone | ANF6 40657-40670; ArnLat 1130-1135; scan twin 2148-2153 | own | Documented | "But lately, O blindness, I worshipped images produced from the furnace … whenever I espied an anointed stone and one bedaubed with olive oil, as if some power resided in it I worshipped it, I addressed myself to it and begged blessings from a senseless stock." / "si quando conspexeram lubricatum lapidem et ex oliui unguine sordidatum, tamquam inesset uis praesens, adulabar, adfabar et beneficia poscebam nihil sentiente de trunco" |
| He asks: shall Christ not be held God, from whom we have received such gifts? | ANF6 40681-40686; ArnLat 1142-1145 | own | Documented | "Is Christ, then, not to be regarded by us as God?" |
| The meetings torn down were places of prayer for magistrates, armies, kings, friends, enemies, living and dead; nothing heard there but what makes people humane | ANF6 48676-48705; ArnLat 7436-7443 | own | Documented | "our meetings to be cruelly broken up, in which prayer is made to the Supreme God, peace and pardon are asked for all in authority, for soldiers, kings, friends, enemies, for those still in life, and those freed from the bondage of the flesh" |

### 2d. Lactantius at Nicomedia (short turn; his own page tells his life)

| Claim | File and lines | Witness | Confidence | Verbatim |
|---|---|---|---|---|
| The learned scorn Scripture for its plain speech; they will believe only what is polished | ANF7 4456; LactLat 22641-22654 | own | Documented | "with the wise and the learned, and the princes of this world, the sacred Scriptures are without credit, because the prophets spoke in common and simple language" |
| "Wisdom and truth need suitable heralds"; the learned who came over were not enough to defend it | ANF7 4456; LactLat 22697-22699 | own | Documented | "Hence it comes to pass that wisdom and truth need suitable heralds." / "eo fit ut sapientia et ueritas idoneis praeconibus indigeat." |
| His judgment of Minucius, Tertullian, Cyprian | ANF7 4470; LactLat 22701-22715 | own (judgment) | Documented (as his judgment) | "His book, which bears the title of Octavius, declares how suitable a maintainer of the truth he might have been, if he had given himself altogether to that pursuit." / "huius liber, cui Octauio titulus est, declarat quam idoneus ueritatis adsertor esse potuisset, si se totum ad id studium contulisset." |
| Lack of skilled teachers spurred enemies to write | ANF7 4487 | own | Documented | "because there have been wanting among us suitable and skilful teachers … this very want incited some to venture to write against the truth" |
| Tertullian's Apology had pleaded the same cause in full | ANF7 4565-4569; LactLat 23225 | own | Documented | "Although Tertullian fully pleaded the same cause in that treatise which is entitled the Apology" |
| Lactantius cites the Octavius by name | ANF7 890; LactLat 2615 | own | Documented | "Minucius Felix, in his treatise which has the title of Octavius, alleged these proofs" |

## 3. Explain it (each thing or act the story could name)

| Thing / act | Own side | Other side (enemy included) | Lines |
|---|---|---|---|
| **Apology / apologist** | A defense speech for the accused, addressed to judges; Tertullian's Apology is written to "rulers … seated for the administration of justice" | – | ANF3 1448-1453 |
| **Serapis** | Octavius: the image is a carved stone, anointed and garlanded | Caecilius greets it "as is the custom of the superstitious common people" (Minucius's words); a god whose image stood by the road to the sea | ANF4 17256-17271 |
| **The charges** (child-killing, incest feasts, ass's head) | Octavius: rumours never proved, sown by demons; "no one can believe this, except one who can dare to do it"; Tertullian: you never inquire into them | Caecilius: "the story about the initiation of young novices is as much to be detested as it is well known"; cites Fronto's speech | ANF4 17640-17670, 18950-18982; ANF3 1946-1956 |
| **Why Christians were hated / punished** | Arnobius: they say the world went to ruin since Christians came; Tertullian: hatred of the name; torture to force denial | Caecilius: a "profane conspiracy" that rejects the gods; "this confederacy ought to be rooted out" | ANF6 39480-39515; ANF4 17582-17617; ANF3 1956-1958 |
| **No temples, altars, images** | Octavius: no temple can hold God; man is God's image; the offering is a good mind | Caecilius: honourable things rejoice in publicity; why hide? | ANF4 17683-17690, 19058-19076 |
| **The meetings / love feast** | Tertullian: prayer, Scripture, monthly gift for the poor; agape, sober, hymns; Arnobius: prayer for all, even enemies | Pagans brand them: "See how they love one another" | ANF3 3868-3975; ANF6 48676-48705 |
| **Arnobius's conversion and books** | Jerome: dreams drove him; bishop refused; books as hostages | Arnobius himself: he once fawned on oiled stones (no bishop, no dreams in his own text that I found) | JerChron 45066-45082; ANF6 40657-40670 |
| **Rhetoric** | the art of public speaking taught to young men ("ad declamandum iuuenes erudiret") | – | JerChron 45066-45068 |
| **Destruction of churches (Diocletian)** | Lactantius: "the temple of God was overthrown"; Arnobius: meetings torn down, writings burned | – | ANF7 4487; ANF6 48676-48678 |
| **New Prophecy** | Jerome: Tertullian "lapsed to the doctrine of Montanus", wrote On fasts, On monogamy | Jerome's motive: envy of Roman clergy | NPNF2-3 40506-40513 |
| **Marcion** | Tertullian: brought in two Gods, the Creator and another | – | ANF3 22609-22612 |

## 4. Impact, ranked heaviest first (what later witnesses carried on and used)

1. **Lactantius takes the earlier Latin defenders as his forerunners and builds on them.** He names Minucius and Tertullian and Cyprian, judges them, says Tertullian's Apology pleaded the cause in full, and cites the Octavius by title. ANF7 4470, 4565-4569, 890. Documented. *Defended: the faith argued to the learned in their own terms.*
2. **Jerome carries them as a set of Latin writers who used pagan learning.** Letter 70 (397) to Magnus: Tertullian's Apology "contains all the wisdom of the world"; Minucius "ransacked all heathen literature"; Arnobius seven books; his pupil Lactantius as many. NPNF2-6 16477-16480, 16704-16720. Later (c. 100-200 years). Documented. *Defended: a Christian's right to use pagan books.* Also DVI 53, 58, 79, 80 (NPNF2-3 40491-40516, 40644-40653, 41019-41054).
3. **Jerome's verdicts on their style** (Letter 58): Tertullian "rugged", Lactantius's eloquence "worthy of Tully", Arnobius "lengthy and unequal". NPNF2-6 14107-14116. Later. Documented. (Lactantius part is used by the lactantius story; card only.)
4. **Augustine on Latin words for God**: many Latin writers of authority said "three persons" for want of a fitter way. NPNF1-3 8211-8227; AugLat 70651-70666. Later, c. 200 years after Tertullian. Documented for what Augustine says; he names no writer, so linking it to these apologists is Inferential-Thin. Card at most.
5. **Gennadius on Commodian**: a pagan scholar who read Christian books, became a Christian and wrote "in barely tolerable semi-versified language" against the pagans. NPNF2-3 42424-42432. Later (date of Commodian Contested). Card.

## 5. Links to other people and stories

- **Tertullian** (tertullian-s-voice, told within this entry): the Apology; New Prophecy; Against Marcion. Lactantius on him: ANF7 4470, 4565-4569.
- **Lactantius** (lactantius, told within): Arnobius's pupil (Jerome); Nicomedia; looks back on the others.
- **Greek Apologists**: Tertullian names "Justin, philosopher and martyr" (ANF3 43160-43163; census edge). The Greek Apologists' live text: Justin and others answered the same charges of atheism, cannibalism and disloyalty.
- **Montanism**: Tertullian's turn (NPNF2-3 40506-40513). That story's job.
- **Marcionism**: Against Marcion (ANF3 22609-22612). That story's job.
- **Jerome** (jerome): writes the lives (DVI) and the Chronicle entry; Letter 70.
- **Cyprian of Carthage**: named by Lactantius as the most renowned (ANF7 4470). His own story; not needed here.
- **Imperial church**: Inferential-Thin (Crispus); stays out per slate.

## 6. Where sources disagree or come late

- **Arnobius's date**: Jerome DVI 79 "during the reign of Diocletian" vs Jerome's Chronicle placing him among Constantine's years (JerChron 45066; ANF6 39071-39079). Tell "in Diocletian's reign, Jerome says"; card the clash.
- **Arnobius's conversion story** rests on Jerome's Chronicle alone, written c. 80 years later. Arnobius's own text says nothing of a bishop. The ANF translators doubt it (ANF6 39094-39108): a modern opinion, not used.
- **Minucius's date**: no old source fixes it; Lactantius lists him before Tertullian, Jerome after (ANF7 4470; NPNF2-3 40491, 40644). Contested. The story must not put the Octavius before or after Tertullian.
- **Tertullian's Apology date**: critics differ (ANF3 1443-1446). Tell by reign (Jerome).
- **Lactantius as Arnobius's pupil**: Jerome alone (DVI 80, Letter 70); Lactantius does not name Arnobius in the review of his forerunners (ANF7 4470).
- **Caecilius's case** is a pagan's case as a Christian author wrote it. Caecilius himself cites the orator Fronto's speech (ANF4 17653-17659); Octavius says Fronto "scattered reproaches as a rhetorician" (ANF4 18998-19004).
- **The kiss**: Latin "manum ori admouens osculum labiis inpressit" (MinLat 223-224): he put his hand to his mouth and kissed it; he did not kiss the statue.

## Library sweep

- **Card `sources`**: the card here has no general `sources` list; its documented story cites Lactantius DMP 12-13, DI V, Eusebius HE VIII.5, Barnes. Those are the lactantius story's ground (the Nicomedia morning) and were not used. Card `people` held ids pointed to the ANF4 Octavius, ANF4 Commodian and ANF6 Arnobius, all read.
- **Corpus map**: `cic/corpus-map/latin-apologists.yaml` (117 rows: Arnobius ×3, Commodian ×5, Cyprian ×6, Minucius ×4, Gennadius, Jerome ×6, Lactantius ×9, Passion of Perpetua ×4, Tertullian ×~70, plus Monceaux, Harnack, Audollent, Brewer, Schanz-Hosius-Krüger as modern works). Tertullian and Lactantius have no buckets of their own; their census `toldWithin` is this entry. `WORKS.yaml` and `AUTHOR-IDS.yaml` checked for felix, arnobius, commodian, lactantius, tertullian; `RETRIEVAL-HINTS.md` holds no entry for these names.
- **Text search of `cic/texts/`**: files naming Minucius 176 (most are the Roman name Minucius in other contexts), Arnobius 173, Lactantius 312, Tertullian 613, Commodian 58, Octavius 136. Later witnesses who carry the subject on: Lactantius (DI I.11, V.1-4), Jerome (DVI 53, 58, 79, 80; Chronicle; Letters 58, 70), Gennadius XV, Augustine De Trin. V.9. Searches for a Decretum Gelasianum text listing Arnobius or Lactantius found none held.
- **Used**: ANF3, ANF4, ANF6, ANF7, NPNF2-3, NPNF2-6, NPNF1-3; Latin: MinLat, ArnLat (+scan twin), JerChron (+Monc3 confirming), LactLat, TertLat1, AugLat.
- **Set aside**: Commodian's Instructiones and Carmen (date uncertain by centuries; Gennadius alone, a century and more later; a story of its own if ever); Cyprian's Ad Demetrianum and Quod idola (Cyprian's own entry and the Latin pastoral story); Passion of Perpetua (a martyr text, not a defense; its own story); Tertullian's other treatises (his own page); Lactantius's On the Deaths of the Persecutors (the lactantius story and the census documented story); Waltzing and Boenig Octavius (checked as second prints only); Harnack, Schanz-Hosius-Krüger, Monceaux, Audollent, Brewer (modern: only Monceaux used, and only as a second print of Jerome's Latin).

## Modern works (for the card's Modern works list; never witnesses)

- Halm, *Minucii Felicis Octavius* (CSEL 2, 1867): edition; clarifies the text (e.g. lucifuga/lucifugax).
- Reifferscheid, *Arnobii adversus nationes* (CSEL 4, 1875): edition.
- Brandt, *Lactantii Divinae institutiones* (CSEL 19, 1890): edition.
- Fotheringham, *Eusebii Pamphili Chronici canones* (1923): edition of Jerome's Chronicle.
- Monceaux, *Histoire littéraire de l'Afrique chrétienne*, vols 1-3 (1901-1905): literary history of Christian Africa; prints Jerome's Chronicle note on Arnobius.
- Bryce and Campbell, introduction to Arnobius, ANF 6 (1871/1886): makes its own claim (doubts the Chronicle story); not used.
- Harnack, *Chronologie*, vol. 2 (1904): makes its own claims on dates; not used.
