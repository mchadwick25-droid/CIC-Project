# Reader C: blind source reading of P01 to P12

| Piece | Modern-voice sentences | Modern-only claims | Quotes not found / total | Key claims held / not found / contradicted | Heart; early? | Fit contradictions |
|---|---|---|---|---|---|---|
| P01 house churches | 0 | 1 | 0/0 | 3/0/0 | present; yes | 0 |
| P02 Lutheran Wittenberg | 0 (+1 process sentence) | 3 | 0/0 | 3/0/0 | partial; yes | 0 |
| P03 Tacitus (short) | 0 | 4 | 3/3 | 3/0/0 | present; yes | 0 |
| P04 Basil | 0 | 4 | 3/3 | 3/0/0 | present; yes | 0 |
| P05 Rufinus | 5 | 2 | 3/3 | 3/0/0 | present; yes | 0 |
| P06 Kongo / Afonso | 0 | 0 | 1/1 | 3/0/0 | present; yes | 0 |
| P07 Ulfila | 3 | 2 | 2/4 | 3/0/0 | present; partly (Scripture at word 158, creed at 175) | 0 |
| P08 Epiphanius | 0 | 0 (1 not checked) | 2/2 | 3/0/0 | present; yes | 0 |
| P09 Ancien Régime church | 0 (+1 process note) | 3 (+1 misleading) | 0/0 | 3/0/0 | present; yes | 0 |
| P10 Priscillian | 3 | 3 | 3/3 | 3/0/0 | present; yes | 0 |
| P11 Jerome | 0 | 5 | 4/5 | 3/0/0 | present; partly (the women at word ~175 to 201) | 0 |
| P12 Tacitus (long) | 6 | 4 | 3/3 | 3/0/0 | present; yes | 0 |

How to read the quote column: I searched every quotation across all of `cic/texts/`, ignoring case, punctuation and markup between words (ripgrep, multiline). Almost every quotation in these pieces is a modern English rendering, not a printed text, so it is "not found" word for word. In every case I located the held passage it renders, cited below. So "not found" here means "rendered, not quoted verbatim". It does not mean the quotation is unsupported. If the project's rule is "verbatim from a held source", every rendering fails it as written.

General observation: P04 to P08 and P12 match the census `longDescription` for their entry exactly. P11 is a 0.99 match and P10 a 0.81 match. P03 is P12 with its modern-historian sentences removed. P01 is the census `entry.summary` word for word.

---

## P01: Post-Apostolic Household-Church Christianity (`post-apostolic-house-church`)

**Heart (from census):** House churches in Antioch, Asia Minor and Rome (70 to 200) held together by letters, with no fixed hierarchy and no finished New Testament. Leadership was unsettled: one bishop with elders (Ignatius) or a council of elders (Rome). Danger came and went. This is the root layer most later traditions claim.

**1. True to sources**
- Modern-voice sentences: none.
- Modern-only claims: 1. "From about 70 to 200 CE" is a modern period frame; no held source gives it.
- Quotations: none.
- Key claims:
  - "Ignatius's letters urged one bishop with elders beside him": **held**, anf01_apostolic-fathers-justin-irenaeus.xml line 4783 ("being subject to the bishop and the presbytery").
  - "At Rome, early letters show a council of elders leading": **held**, anf01 line 2336 (1 Clement: "submit yourselves to the presbyters").
  - "marched under guard toward death": **held**, anf01 line 7087 ("bound to ten leopards, I mean a band of soldiers").
- Invented: nothing. The piece is very thin (80 words). The census `sourcing` field says the dating and authorship of Ignatius's letters are contested, and the piece puts no date on them, so it does not overstate.

**2. Heart:** present. The missing pieces are "no finished New Testament" and the Corinth episode. Early: yes.

**3. Fit:** the piece states no links. Census edges: continued as `roman-church-third-century`; argued against Montanism, Marcion and the Valentinians. Nothing contradicts them.

## P02: Lutheran Wittenberg & Its Congregations (`lutheran-wittenberg-and-its-congregations`)

**Heart:** From Luther's 1517 indulgence protest, a reform taught that a person stands before God by a gift received through faith. Princes and city councils carried it, not bishops, and the household catechism formed it at home. The census `why` adds that the visitation records show parishes knew less than the pamphlets imply, and that women such as Argula von Grumbach and Katharina Schütz Zell published for the cause.

**1. True to sources**
- Modern-voice sentences: 0 naming scholars. There is one process or meta sentence: "The sources behind this account hold the 1525 writings, but not the 1543 treatise." That is narration about the library, not story.
- Modern-only claims: 3.
  - "On 1 July 1523 two young monks ... were burned at Brussels." The exact date comes from editors: luther_hymns_bacon-allen.txt line 1745 prints "[July 1, 1523]" in brackets after the source's own "MDXXII", and luther_works-v4-selected_various1931.txt lines 4878 and 8546 are 1931 editorial notes.
  - "Within months Luther wrote a ballad about them." This is Bacon's dating (bacon-allen lines 695-698: "the critics can hardly be mistaken in assigning as early a date").
  - "Wittenberg's first hymn-book was printed in 1524 and held eight hymns, four of them Luther's." This is Bacon's editorial introduction (lines 684-688), not an old source.
- Quotations: none in quotation marks. The word "Revoco" is held: luther_table-talk_bell1886.txt line 3446.
- Key claims:
  - The 31 October 1517 letter to Albrecht of Mainz: **held**, luther_letters-of-martin-luther_currie1908.txt line 787.
  - The Augsburg "Revoco" episode in Table Talk: **held**, Table Talk lines 3438-3447.
  - The catechism rule of "neither food nor drink": **held**, luther_large-catechism_bente-dau1921.txt line 334.
  - Also held: Walter's "three weeks" (bacon-allen line 766); "no signs of love among you" (luther_works-v2 line 14677); the Augsburg Confession's signers including the Senate of Reutlingen (melanchthon_augsburg-confession_anon-pg275.txt line 1567); and Katharina's question about praying in Popedom (Table Talk lines 3146-3147).
- Invented: nothing found. "Luther died in the mid-1540s" is vague; I did not check it.

**2. Heart:** partial. Justification through faith and the conscience come early (word 63). The catechism comes late (word 461). The princes and cities appear only through the Confession's signers (word ~579). The visitation evidence and the women writers in the census `why` are missing. Early: yes for the doctrinal core.

**3. Fit:** The piece names Rome (indulgences, St Peter's) and says the Confession "rejected those who taught otherwise about the Supper". Both agree with the census edges (argued against `latin-papal-church-avignon-to-lateran-v`; argued against `the-reformed-cities-zurich-and-geneva`). None of the influence edges (Theologia Deutsch, Hus) or offspring edges (Scandinavia and others) is stated. No contradiction.

## P03: Tacitus, short version (`tacitus`)

**Heart:** A Roman outside witness. Annals 15.44 tells how Nero blamed the Christians for the fire of Rome, and names Christus as executed under Pontius Pilate. It matters as the main non-Christian record of this.

**1. True to sources**
- Modern-voice sentences: 0.
- Modern-only claims: 4.
  - "about fifty years after the great fire of Rome in 64": the year 64 and "Written c. 116" appear only in the vendoring header of tacitus_annals-15-44_church-brodribb1876.txt (lines 4 and 9), not in the chapter text (line 68).
  - "the fullest account outside the church" is a modern comparative judgment.
  - "Almost everything known of these deaths rests on this one chapter" is a modern judgment, and the piece itself goes on to cite Sulpicius.
  - "About the year 200" for Tertullian and "About 400" for Sulpicius are modern datings.
- Quotations (3), none verbatim:
  - "Christus, from whom the name came..." **not found**. It renders tacitus file line 68 ("Christus, from whom the name had its origin, suffered the extreme penalty...").
  - "that same Cornelius Tacitus, who truly talks more lies than anyone": **not found**. It renders the Latin in tertullian_quae-supersunt-t1-apologetica-lat_oehler1853.txt line 17916 ("sane ille mendaciorum loquacissimus"). The English print, anf03_tertullian.xml line 2583, reads differently.
  - "So even for criminals...": **not found**. It renders tacitus line 68 ("Hence, even for criminals who deserved extreme and exemplary punishment...").
- Key claims:
  - Christus under Pilate, Nero's tortures and the gardens: **held**, tacitus line 68.
  - Tertullian on the ass's head and the empty temple: **held**, anf03 lines 2578-2586.
  - Sulpicius calls them innocent: **held**, npnf211_sulpitius-severus-vincent-lerins-cassian.xml lines 10660-10661 ("tortures were accordingly inflicted upon the innocent").
- Invented: nothing.

**2. Heart:** present. Early: yes (Christus at word 82).

**3. Fit:** Person entry with no edges. The links to Tertullian and Sulpicius agree with the card's `legacy`. No contradiction.

## P04: Basil of Caesarea (`basil-of-caesarea`)

**Heart:** Bishop of Caesarea from 370. He gave up rhetoric for the ascetic life, wrote the Rules for monks living in common, built a lodging for the poor and sick, and in On the Holy Spirit defended the Spirit's place beside the Father and the Son. He matters because his Rule was named by the 787 council and by Benedict.

**1. True to sources**
- Modern-voice sentences: 0. "Gregory's speech in Basil's memory is praise" is a narrator's caution, not a modern authority.
- Modern-only claims: 4.
  - "As bishop from 370" is Jackson's chronology (census `datesNote`).
  - "He died in 378 or 379" comes from Jackson, Clarke and Gwynn.
  - "Rufinus put his Rule into Latin in 397 or 398" is a modern date.
  - "In the sixth century Benedict" is a modern dating.
- Quotations (3), none verbatim:
  - "Then one day, like a man roused from deep sleep..." **not found**. It renders npnf208_basil-letters-select-works.xml lines 39133-39135.
  - "Whom, then, will you wash?..." **not found**. It renders the Greek in basil_opera-omnia-pg31 lines 72547-72549. Clarke's English, basil_ascetic-works-longer-shorter-rules_clarke1925.txt lines 13460-13464, differs.
  - "As we were baptized, so we confess our faith..." **not found**. It renders npnf208 lines 33483-33485 ("As we were baptized, so we profess our belief. As we profess our belief, so also we offer praise").
- Key claims:
  - Rufinus says Basil taught rhetoric: **held**. Rufinus, HE 11, in eusebius_werke-bd2-2-...-rufinus file lines 29989-29991 ("ad profitendam rhetoricam rogabantur. quod opus magnifice quidem implebat Basilius").
  - The 787 council told double monasteries to keep his rule: **held**, npnf214_seven-ecumenical-councils.xml line 41061.
  - Benedict points to Basil's Rule: **held**, benedict_rule-of-st-benedict-lat-eng_hunter-blair1907.txt line 10446.
  - Also seen: Sasima, npnf207 line 22983.
- Invented: nothing.

**2. Heart:** present. Early: yes (Rules at word 88, lodging at 103, Holy Spirit at 123).

**3. Fit:** told within the Cappadocians. The piece names his brother Gregory of Nyssa and his friend Gregory of Nazianzus, which agrees with `relationsSummary`. The 787 rule matches the edge `desert-monasticism` influenced `iconophile-byzantine-monasticism` (concerns Basil). No contradiction.

## P05: Rufinus of Aquileia (`rufinus-of-aquileia`)

**Heart:** A Latin monk and translator who carried Origen and Eusebius's Church History into Latin. His preface to On First Principles ended his old friendship with Jerome. He matters because much of Origen survives through his Latin.

**1. True to sources**
- Modern-voice sentences: 5.
  1. "First Principles and many of Origen's other works survive chiefly in his reworded Latin, his editors note."
  2. "The few Greek fragments of First Principles show, his editors note, that he altered Origen's wording."
  3. "His History became the Latin West's Eusebius through the Middle Ages, an editor judges."
  4. "Rufinus's last work came in Sicily, about 410 by his editor's date."
  5. "He died soon after, his editors judge."
- Modern-only claims: 2. "in 374" (Fremantle's date for Jerome's Letter 3), and "Origen, a Greek Bible scholar of the 200s" (a modern dating).
- Quotations (3), none verbatim:
  - "A friendship that can end was never real." **not found**. It renders npnf206_jerome-principal-works.xml lines 3941-3942 ("The friendship which can cease has never been real").
  - "Where I found anything in his books..." **not found**. It renders npnf203_theodoret-jerome-gennadius-rufinus.xml lines 45775-45780.
  - "In the books On First Principles, I simply set down..." **not found**. It renders npnf203 lines 51325-51330 ("I expressed in Latin just what I found in the Greek text ... not wishing the reader to believe what was in my translation, but wishing him not to believe what was in yours").
- Key claims:
  - Eight years in Egypt: **held** as "six years, and again after an interval for two more", npnf203 line 49435.
  - Chromatius asked for the History when the Goths broke into Italy: **held**, Rufinus's HE preface, eusebius_werke-bd2-2 lines 26043-26045 ("diruptis Italiae claustris Alarico duce Gothorum").
  - The Numbers preface, Rhegium on fire, quiet nights: **held**, npnf203 lines 58989-59000. The year 410 is the editor's note at line 58973.
- Invented: nothing.

**2. Heart:** present. Early: yes (Latin at word 76, the friendship break at 138).

**3. Fit:** told within `aquileian-christianity`. The census edge "aquileian-christianity broke with hieronymian-ascetic-literary" (concerns Jerome) agrees with the broken friendship. No contradiction.

## P06: Kongo Christianity, Afonso I to 1650 (`kongo-christianity-afonso-to-1650`)

**Heart:** King Afonso I took the faith, sent kin to Portugal and asked for priests. His own letters survive and argue with Portugal over the slave trade and his church. Almost everything else about Kongo's Christians was written by missionaries.

**1. True to sources**
- Modern-voice sentences: 0.
- Modern-only claims: 0 found. "which a Portuguese chronicler later printed" (the 1512 letter) is not verified; that search was inconclusive.
- Quotations (1):
  - "It is our will that in these kingdoms there be no trade in slaves, and no outlet for them." **not found** in English. It renders the Portuguese in paiva-manso_historia-do-congo-documentos-por_1877.txt lines 2410-2411 ("nossa vontade he que nestes Reynos nam aja trato de esprauos nem sayda pêra elles"), in the letter of 6 July 1526.
- Key claims:
  - The July 1526 letter (wine and flour, people carried off, the land emptied): **held**, Paiva Manso lines 2337-2420.
  - The Easter Mass attempt, "seven or eight white men", the shot through his robe's skirts: **held**, in the letter of 17 December 1540, about lines 3426-3431 ("hum dia de páscoa com sete ou oyto homens brancos"; "polias nossas fraldas pasou o pilouro").
  - Portuguese ships at the Zaire in 1491: **held**, lopes_report-of-the-kingdom-of-congo_hutchinson1881.txt line 3513. Also held: Pango, Lopes line 3714; the 1512 letter to the pope on idols, Paiva Manso lines 533-545.
- Invented: nothing. The piece flags well what rests on Afonso's word alone.

**2. Heart:** present. Early: yes (the slave trade at word 40, "outsiders" at 134). The piece covers Afonso only, not the period to 1650.

**3. Fit:** Census edges: in contact with `the-society-of-jesus` (1547); gave rise to `the-antonian-movement-in-kongo` (Inferential-Thin); continued as `kongo-christianity-after-1650`. The piece states none of them, only contact with Portugal. No contradiction.

## P07: Ulfila (`ulfila`)

**Heart:** Bishop of the Goths. He led Gothic Christians across the Danube, gave the Goths letters and the Scriptures in their tongue, and taught the Homoian creed (the Son "like the Father"). He matters because the Goths kept that faith.

**1. True to sources**
- Modern-voice sentences: 3.
  1. "A modern historian takes this Eusebius for the bishop of Nicomedia." (Duchesne, per the census card.)
  2. "Fragments of a Gothic Bible survive without a translator's name, but their editor in 1908 had no doubt they were Ulfila's." (Streitberg.)
  3. "In 360, by the usual date, he joined the bishops at Constantinople..." Socrates gives no year (npnf202 lines 9606-9611).
- Modern-only claims: 2. "He died there, about 383" is Kauffmann's dating (auxentius file lines 2068 and 2368, German editorial text). "360" rests on the modern convention.
- Quotations (4):
  - The long Auxentius passage ("Through Moses, God freed his people..."): **not found**. It renders the Latin in auxentius-durostorum_epistula-de-fide-vita-obitu-wulfilae_kauffmann1899.txt lines 15273-15277.
  - "alone unbegotten": the phrase occurs, but only in unrelated files (anf05, anf01, npnf207). The Ulfila source has the Latin "solum ingenitum" (auxentius lines 15071 and 15310), so it is not found in his source as English.
  - "subject and obedient in all things": **not found**. It renders auxentius line 15324 ("filium subditum et oboedientem suo in omnibus deo patri").
  - "substance": **found**, Socrates, npnf202 line 9607.
  - Count: 2 of 4 not found. A strict count, treating "alone unbegotten" as a chance match, would be 3 of 4.
- Key claims:
  - Driven out after seven years as bishop and received under Constantius: **held**, auxentius lines 7203-7205.
  - Philostorgius on letters for the Goths and Scripture without the Books of Kings: **held**, philostorgius_ecclesiastical-history_walford1855.txt line 120.
  - Socrates on the 360 creed after earlier holding Nicaea: **held**, npnf202 lines 9606-9611, without a year.
- Invented: nothing found.

**2. Heart:** present. Early: partly. The crossing comes at word 33, but the Scriptures come at word 158 and the creed at 175.

**3. Fit:** told within `homoian-arian-christianity`; the piece names the faith Homoian, which agrees. No edges for this person. No contradiction.

## P08: Epiphanius of Salamis (`epiphanius-of-salamis`)

**Heart:** Bishop of Salamis in Cyprus who wrote the Panarion, a "medicine chest" against eighty heresies, and led the attack on Origen in the 390s and 400s. Later writers took his list as their own.

**1. True to sources**
- Modern-voice sentences: 0. "The scholar Jerome" and "The historian Sozomen/Socrates" are ancient.
- Modern-only claims: 0 confirmed. "He wrote the Panarion about 375, by his own dating" was not checked (inconclusive). The census `uncertain` says his life dates are Richardson's, which is a different matter.
- Quotations (2), none verbatim:
  - "We are going to show you the names of the heresies..." **not found**. It renders the Greek in epiphanius_ancoratus-panarion-haer-1-33-gcs-bd1-grc_holl1915.txt lines 12387-12391. No printed English is held.
  - "I have also drunk from the great river Euphrates..." **not found**. It renders npnf206 Letter 51 ("I have drunk also from the great river Euphrates, not spiritual but actual water...").
- Key claims:
  - The torn curtain: **held**, npnf206 lines 11102-11114.
  - Died at sea before reaching Cyprus: **held**, npnf202 lines 18227-18228.
  - The 787 council argued from his eighty chapters that the passage was not his: **held**, mendham_seventh-general-council-second-of-nicaea_1850.txt lines 26275-26284. Also held: "stop his mouth", npnf206 line 10691.
- Invented: nothing.

**2. Heart:** present. Early: yes ("eighty heresies" at word 98, Origen at 142).

**3. Fit:** told within `palestinian-ascetic-monasticism-early`; "a monk from Palestine" agrees. No edges for this person. No contradiction.

## P09: The Catholic Church of the Ancien Régime (`catholic-church-ancien-regime`)

**Heart:** Rome and Catholic Europe from 1650 to 1815: the church at its most established and most helpless. It moved from Unigenitus and the Jansenist crisis, through the kings forcing the Jesuits' suppression in 1773, to the Revolution, the Concordat and Napoleon's captive pope. The census `relationsSummary` adds the Gallican Articles, Quietism and Liguori.

**1. True to sources**
- Modern-voice sentences: 0. There is one process artifact inside the story: "(in a plain English rendering)".
- Modern-only claims: 3.
  - "This was the Catholic Church at the height of its establishment and on the edge of its worst crisis: enormously wealthy, woven into the monarchies of Europe, and increasingly unable to control them." This is a modern synthetic judgment.
  - "turned into a fifty-year political crisis in France" is a modern assessment.
  - "thousands killed or driven abroad" is a modern figure. No source was checked; the search was inconclusive.
- Misleading: "The pope outlived him and restored the Jesuits that year." Set after "until 1814", it reads as if Napoleon died by 1814. He died in 1821. The restoration in 1814 is held, but the sentence joins two unrelated facts.
- Quotations: none.
- Key claims:
  - The 1659 instruction ("What is more absurd than to carry France, Spain or Italy into China"): **held**, propaganda-fide_collectanea-decreta-instructiones-rescripta-v1-lat_1907.txt lines 8192-8197 ("Quid enim absurdius quam Galliam, Hispaniam, aut Italiam ... in Sinas invehere").
  - The 1726 oath for native priests under Ex illa die: **held**, the same file lines 18648-18660. It sits under "An. C. 1726", although the OCR of the date line reads "17236".
  - The 1656 ruling that the Confucius cult "seemed merely civil and political": **held**, the same file about line 7488 ("videtur cultus esse mere civilis et politicus"), next to "LiCR 1656".
  - Also held: Clement XIV's brief naming the kings, clement-xiv_bulls-suppression-and-restoration-of-the-jesuits-lat-eng_1814.txt lines 250-344; Napoleon's decree of 17 May 1809 on joined spiritual and temporal authority, anderson-frank-maloy_constitutions-and-documents-history-of-france_1908.txt lines 25925-25938.

**2. Heart:** present. Early: yes (Unigenitus at word 40, Jesuits at 62, Revolution at 98, concordat at 124).

**3. Fit:** The piece mentions Jansenism, the Jesuits and the China rites. These agree with the edges argued against `port-royal-jansenism`, argued against `society-of-jesus-1650-1814` (1773 and 1814), and in contact with `chinese-catholicism-1650-1906` (1656, 1726). The concordat agrees with continued as `catholic-church-long-nineteenth-century`. The piece also names Tonkin and Cochinchina, but the census has no edge from this entry to `vietnamese-catholicism-to-1815`. That is a gap, not a contradiction. No contradiction.

## P10: Priscillian (`priscillian`)

**Heart:** A Spanish lay teacher of a strict ascetic life, made bishop of Abila. He was condemned by bishops and put to death under the usurper Maximus, then honored by his followers as a martyr. Bishops killing through the state split the church.

**1. True to sources**
- Modern-voice sentences: 3.
  1. "In 1885, a scholar opened an old manuscript at Würzburg and found eleven unsigned treatises."
  2. "He judged they could be no one's but Priscillian's."
  3. "Among them was the book Priscillian had carried to Damasus, with his call in his own words again."
  These rest on Schepss's preface, priscillian_quae-supersunt-lat_schepss1889-csel18.txt lines 86 and 188.
- Modern-only claims: 3.
  - "In about 385" is a modern date.
  - "sixty years on" for Leo assumes the modern date of 447.
  - "Nearly all we know of him comes from Sulpicius Severus" and "For centuries Priscillian was known only through his enemies" are modern framings. They also sit in tension with the piece's own use of Priscillian's treatises.
- Quotations (3), none verbatim:
  - "No one should be forbidden..." **not found**. It renders the Latin in the Schepss file lines 4415-4417.
  - "My own view is that the accused displease me as much as the accusers." **not found**. The held English, npnf211 lines 11642-11643, reads "the accusers were as distasteful to me as the accused". The piece reverses the order, following the Latin per the census.
  - "Even the rulers of the world loathed this unholy folly..." **not found**. It renders npnf212_leo-great-gregory-great.xml lines 3276-3278 ("the leaders of the world so abhorred this profane folly that they laid low its originator, with most of his disciples, by the sword of the public laws").
- Key claims:
  - Martin begged the emperor not to shed blood: **held**, npnf211 line 11655.
  - Leo praised the killing: **held**, npnf212 line 3278.
  - Clergy at Toledo still called him a holy martyr: **held**, mansi_sacrorum-conciliorum-collectio-tomus-3-347-409-lat_welter-facsimile1901.txt line 96782 ("sanctumque martyrem clamassent").
- Invented: nothing.

**2. Heart:** present. Early: yes ("strict life" at word 63, put to death at 90, martyr at 103).

**3. Fit:** told within `priscillianist-asceticism`, which agrees with his followers being honored. No edges for this person. No contradiction.

## P11: Jerome (`jerome`)

**Heart:** A Latin scholar who learned Hebrew and at Bethlehem put the Old Testament into Latin from the Hebrew, in the work later called the Vulgate, fought over in his lifetime. His letters are the main record of the Roman women, above all Paula, who shared and funded that life.

**1. True to sources**
- Modern-voice sentences: 0 naming scholars.
- Modern-only claims: 5.
  - "From about 391 he addressed many prefaces" is Fremantle's dating.
  - "In 400 Rufinus wrote against him" is a modern date.
  - "In 403 Augustine told Jerome" is a modern date.
  - "About 411 he wrote" is a modern date.
  - "The decree does not name Jerome, but the version the council chose was his" is an identification the decree does not make. It rests on later or modern identification. The census edge rates the Jerome-to-Trent link "Widely Accepted" and cites the 1848 translator.
- Quotations (5):
  - "I began to learn my letters all over again..." **not found**. It renders npnf206 lines 25515-25516.
  - "Who but you would have laid hands on God's gift..." **not found**. It renders npnf203 lines 50284-50285.
  - "The Greeks above all found fault..." **not found**. It renders npnf101_augustine-confessions-letters.xml about lines 32548-32550. Note that the quotation marks enclose an added sentence, "The town was Oea." The source has only a parenthesis ("it was in the town of Oea"), and the clause order is rearranged.
  - "old and Vulgate edition": **found**, council-of-trent_canons-and-decrees_waterworth1848.txt and schaff_creeds-of-christendom-v2.
  - "But I thank the Lord that from this seed of learning..." **not found**. It renders npnf206 lines 25520-25522 ("I now cull sweet fruits").
- Key claims:
  - Damasus and "almost as many forms of texts as copies": **held**, npnf206 line 46650.
  - The Oea uproar over the gourd and the ivy: **held**, npnf101 lines 32550 and 33954.
  - A bishop in Spain judged his version rightly preferred: **held**, isidore-seville_etymologiae-origines-lat_lindsay1911.txt line 13116 ("Cuius interpretatio merito ceteris antefertur").
  - Also held: "restorer of the ancient faith", npnf101 line 54054.

**2. Heart:** present. Early: partly. The Hebrew comes at word 79 and "standard" at 115, but the women appear only at about word 175 and Paula at 201.

**3. Fit:** The census edges agree with the piece. "aquileian-christianity broke with hieronymian" matches the Rufinus quarrel. "In contact with latin-pastoral-congregational-christianity" matches Augustine and Oea. "Hieronymian influenced the-tridentine-church" matches Trent. No contradiction.

## P12: Tacitus, long version (`tacitus`)

**Heart:** the same as P03.

**1. True to sources**
- Modern-voice sentences: 6.
  1. "Yet his one chapter became what later historians built on."
  2. "Historians a century ago read that to mean the inquiry proved them Christians, not that they set the fire."
  3. "Later historians made the chapter their main outside record of these deaths, and a Roman's witness that Christus was put to death under Pilate."
  4. "In an 1876 debate, a speaker arguing that the Bible was not divine said the passage was open to challenge."
  5. "The historians who weighed it treated it as Tacitus's own."
  6. "In 1890, a translator of Eusebius's history of the early church rejected the view of some historians that the victims were Jews, not Christians." (McGiffert, per the census card.)
- Modern-only claims: 4, the same as P03 (the year 64 and "fifty years", "fullest account", "almost everything known", the approximate dates for Tertullian and Sulpicius). Each modern-voice sentence above also supplies a modern judgment.
- Quotations: the same 3 as P03, all not found verbatim; the renderings are located as in P03.
- Key claims: the same 3 as P03, all held.
- Invented: nothing.

**2. Heart:** present. Early: yes.

**3. Fit:** No edges for this person. Tertullian, Sulpicius and the 1890 translator agree with the card's `legacy` and `uncertain`. No contradiction.
