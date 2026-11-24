# Trust gate: P01 to P06

| Piece | Subject (census card) | Sentences checked | HELD | SUMMARY HOLDS | SOFTENED | ASSUMPTION | MODERN ONLY | NOT FOUND | Gate |
|---|---|---|---|---|---|---|---|---|---|
| P01 | Post-Apostolic Household-Church Christianity (`post-apostolic-house-church`, entry.summary) | 8 | 2 | 3 | 0 | 0 | 3 | 0 | FAIL |
| P02 | Lutheran Wittenberg & Its Congregations (`lutheran-wittenberg-and-its-congregations`; new text, not yet on the card) | 44 | 22 | 15 | 3 | 0 | 3 | 1 | FAIL |
| P03 | Tacitus (`tacitus`, person card) | 23 | 14 | 7 | 0 | 0 | 2 | 0 | FAIL |
| P04 | Basil of Caesarea (`basil-of-caesarea`; matches longDescription) | 39 | 25 | 10 | 0 | 0 | 4 | 0 | FAIL |
| P05 | Rufinus of Aquileia (`rufinus-of-aquileia`; matches longDescription) | 40 | 26 | 7 | 0 | 0 | 7 | 0 | FAIL |
| P06 | Kongo Christianity, Afonso I to 1650 (`kongo-christianity-afonso-to-1650`; matches longDescription) | 27 | 21 | 4 | 2 | 0 | 0 | 0 | FAIL |

How I counted:
- A rhetorical question with no claim (P04, "Who turned him away?") is not counted.
- A date is marked MODERN ONLY when it is an editor's reconstruction for a text that carries no date of its own. Examples: Basil's 370 and 378/379 (Jackson), Fremantle's 397/398 and 410, Jerome Letter 3's "374" from the editors' heading, Tertullian's "about 200" (ANF), and Tacitus "about fifty years after ... 64" (from the file's vendoring header).
- A date is SUMMARY HOLDS, with a note, when it converts the old text's own dating (for example Stilicho's consulship giving about 400), or is the plain year a known book was printed (for example the Book of Concord, 1580).
- Statements about the record itself ("almost everything rests on this chapter", "rests on his word alone") were checked against what the Library holds. Where the Library bears them out, they are marked SUMMARY HOLDS or HELD.

Every sentence not marked HELD is quoted below with its evidence. HELD sentences are listed with their anchor line only.

---

## P01: The Scattered Households (census entry summary)

Card sources: Ignatius, 1 Clement, Didache, Martyrdom of Polycarp, Polycarp to the Philippians, Justin, Martyrdom of Justin, Hermas, Pliny 10.96. Pliny is **not held** in `cic/texts/`. The Library holds only a Pliny Fisk memoir.

1. "From about 70 to 200 CE, Christians in Antioch, the cities of Asia Minor and Rome gathered in households." **SUMMARY HOLDS.**
   - Households are greeted in Ignatius, Smyrnaeans 13: "I salute the house of Tavias" (`anf01_apostolic-fathers-justin-irenaeus.xml` 8507) and "the wife of Epitropus, with all her house and children" (8869).
   - Note: 70–200 is the project's own period, not a dated event. No held text shows a household gathering at Antioch in particular.
2. "No central body ruled them." **MODERN ONLY.**
   - This is a modern argument from silence. No old text says it.
   - 1 Clement writes to Corinth in strong terms: "esteem those who have the rule over us" (anf01 1223). Ignatius greets Rome as the church that "presides".
   - Whether Rome had authority is the point scholars dispute. The sentence presents it as settled.
3. "Letters carried by hand held them together." **SUMMARY HOLDS.**
   - Named couriers: "our messengers to you: Claudius Ephebus and Valerius Bito" (anf01 2396); "I write to you by Burrhus" (anf01 7895).
   - Polycarp: "The Epistles of Ignatius written by him to us ... we have sent to you" (anf01 3613).
   - "Held them together" is a fair compression of what these letters do.
4. "After the apostles died, these churches had not yet settled who should lead." **MODERN ONLY.**
   - The old text claims the opposite: 1 Clement 44: "Our apostles also knew ... there would be strife on account of the office of the episcopate. For this reason ... they appointed those [ministers] already mentioned, and afterwards gave instructions ..." (anf01 1916-1922).
   - "Not yet settled" is a modern reconstruction drawn from the variety of the sources.
5. "Ignatius's letters urged one bishop with elders beside him." **HELD.** Magnesians 6: "your bishop presides in the place of God, and your presbyters in the place of the assembly of the apostles" (anf01 5854-5855).
6. "At Rome, early letters show a council of elders leading." **MODERN ONLY.**
   - Neither 1 Clement nor Ignatius to the Romans describes Rome's own leaders. 1 Clement's presbyters are Corinth's. Reading a Roman council of elders from the absence of a named bishop is a modern inference.
   - An old text does say it, but it is not a letter: Hermas, Vision 2.4, "you will read the words in this city, along with the presbyters who preside over the Church" (`anf02_hermas-tatian-athenagoras-theophilus-clement-alexandria.xml` 1026).
   - Fix: rest the sentence on Hermas.
7. "Being a Christian could bring real danger." **SUMMARY HOLDS.** Ignatius under guard (next sentence) and the Martyrdom of Polycarp (anf01). Pliny's torture report is cited on the card but is not held.
8. "Ignatius's letters say he was marched under guard toward death." **HELD.** Romans 5: "being bound to ten leopards, I mean a band of soldiers" (anf01 7087).

**Heart:** right for a summary tile: dispersed churches, unsettled order, intermittent danger. But two of its three structural claims (2 and 4) state modern consensus as fact, and 4 runs against 1 Clement 44.

---

## P02: Lutheran Wittenberg (new long text)

Library files used: `melanchthon_augsburg-confession_anon-pg275.txt` (AC), `book-of-concord_symbolical-books-evangelical-lutheran-church_jacobs1911.txt` (BoC), `luther_small-catechism_smith1994.txt` (SC), `luther_large-catechism_bente-dau1921.txt` (LC), `luther_letters-of-martin-luther_currie1908.txt` (Currie), `luther_table-talk_bell1886.txt` (TT), `luther_works-v1/v2/v4/v6...` (PE), `luther_first-principles-reformation_wace-buchheim1885.txt` (Wace), `luther_hymns_bacon-allen.txt` (Bacon).

HELD, with anchors:
- 2: Theses heading, "Lecturer in Ordinary on the same at that place [Wittenberg]" (PE v1 1146).
- 6: SC 404, "the old Adam in us should be drowned by daily sorrow and repentance"; SC 421, "absolution ... as if from God Himself".
- 8: Currie 3395-3407, dated October 31, 1517.
- 9: Currie 3421-3428, "the Papal Indulgence for the rebuilding of St. Peter's ... regret the false meaning, which the simple folk attach to it".
- 11, 12, 13: TT 3437-3452, "In the year 1518 ... cited and summoned ... an Italian ... persuaded me ... namely, Revoco ... fell down first upon my knees".
- 14: TT 3549-3551.
- 16: TT 3561-3566, "books of doctrine; the same I neither can nor will revoke. But if ... I have in my books of controversies been too violent ... I am content therein to be better directed".
- 21: PE v2 14677, "I see no signs of love among you"; the sermons are headed Invocavit Sunday and the days after (14636 ff.).
- 25: PE v6 9006-9050, German Mass, "we sing a hymn or a German Psalm ... After the Epistle a German hymn".
- 27, 28: Bacon 772-778 (Walter), "He kept me three weeks long at Wittenberg, to write out the notes over some of the Gospels and Epistles, until the first German Mass was sung".
- 31: LC 241-243.
- 32: LC 322-325.
- 33: SC, "What does this mean?" after each part.
- 35: AC 50-53.
- 37, 38: AC 1559-1567. The signers are John, Elector; George; Ernest; Philip; John Frederick; Francis; Wolfgang; the Senates of Nuremberg and Reutlingen. Luther is not among them.
- 39: AC 323-324, "they reject those that teach otherwise".
- 41: confirmed. PE v4 holds the three 1525 peasant writings. No Library file holds the 1543 treatise.
- 44: BoC contents (Creeds, AC, Apology, Smalcald, both Catechisms, FC).

Non-HELD:

1. "From 1517 to 1580, a reform grew out of Wittenberg." **SUMMARY HOLDS.** 1517 is held (the letter). For 1580, see 43.
3. "At the heart of this tradition sits a frightened conscience." **SUMMARY HOLDS.** AC XX: "This whole doctrine is to be referred to that conflict of the terrified conscience" (AC 552). Apology: "terrified consciences waver ... and they rush into despair unless they hear ... the Gospel" (BoC 4123-4128).
4. "The churches of this reform taught that the commandments lead a person to despair of his own powers, and that God's promise then comforts him." **SUMMARY HOLDS.**
   - Luther, Christian Liberty: "that through them he may learn his own impotence for good, and may despair of his own strength" (Wace 8444-8445).
   - The confessional form is in the Apology at BoC 4127-4128.
5. "a sinner is freely justified for Christ's sake, through faith, and the sacraments carry that promise." **SUMMARY HOLDS.** AC IV, "freely justified for Christ's sake" (AC 235). AC XIII: "signs and testimonies of the will of God toward us ... believe the promises which are offered and set forth through the Sacraments" (AC 367-372).
7. "...in and under the bread and wine, and they gave no explanation of how." **SOFTENED OR CHANGED** (low severity).
   - "In and under" is held at BoC 24826 (LC).
   - But the Formula of Concord, inside this piece's own 1517–1580 frame, does explain. It sets out the "sacramental union" (BoC 26675) and quotes Luther's modes of presence: "Secondly, the incomprehensible, spiritual mode ..." (BoC 32720).
   - What it then says is: "how it occurs we do not know; this [mystery] is above nature and reason" (BoC 32755-32757).
   - The source's force is "they would not claim to know how", not "they gave no explanation". Fix: "and they said they did not know how".
10. "He asked the archbishop to withdraw the instruction ... and he sent ninety-five statements for debate with it, the Ninety-Five Theses." **SUMMARY HOLDS.**
    - The letter: "do away with this little book of instructions ... perhaps you would glance at my enclosed theses" (Currie 3483-3496).
    - Note: that the enclosure was the 95 theses is the editors' identification (Currie headnote 3399; PE v1 797-798). It is supported by Luther to Leo X: "I published my Disputation" (PE v1 1702-1703).
15. "He told the story years afterward to his students at his own table." **SUMMARY HOLDS.** Aurifaber: "in the years 1545 and 1546 ... was much with and about him, and ... writ and noted down" (TT 140-142); Lauterbach "noted and wrote out of the holy mouth of Luther" (TT 135-136). Note: "students" is a loose gloss. The anecdote passages only say "said Luther".
17. "...the next day he said he would accept instruction in everything except what touches Holy Scripture." **SUMMARY HOLDS.** It is Joachim's summary, and Luther assents: "Marquis Joachim said unto me 'Sir Martin ... you are content to be instructed, excepting only what may concern the Holy Writ.' I said, 'Yea'" (TT 3572-3574).
18. "The reform ran ahead of its founder." **SUMMARY HOLDS.** Eight Sermons: "I would not have gone so far as you have done, if I had been here ... you have gone too fast" (PE v2 14726-14728).
19. "In March 1522 Luther left the Wartburg ... against the Elector's instruction to stay." **SUMMARY HOLDS.** Letter of March 5, 1522: "I have done sufficient for your Grace this year in remaining in my forced seclusion ... seeing I decline to follow your Grace" (Currie 7514, 7531, 7590). The Elector's own letter is not held. That it urged him to stay comes from Luther's reply and from Currie's headnote.
20. "Wittenberg was in disorder over how fast to sweep away the old forms of worship." **SUMMARY HOLDS.** The Eight Sermons, as at 18.
22. "On 1 July 1523 two young monks, John and Henry, were burned at Brussels after they refused to give up their teaching." **MODERN ONLY (the date).**
    - The ballad holds the rest: "One of these youths was called John, And Henry was the other ... They bade them God's dear Word abjure ... Their monkish garb from them they take ... Two fires were lit" (Bacon 1758-1819).
    - The day comes only from Bacon's bracket: "in the year MDXXII [July 1, 1523]" (Bacon 1745). Bacon's editorial note repeats it: "Their martyrdom took place July 1, 1523" (Bacon 697).
23. "Within months Luther wrote a ballad about them." **MODERN ONLY.** This is Bacon's inference: "the critics can hardly be mistaken in assigning as early a date to the ballad ... must have been inspired by the story as it was first brought to Wittenberg" (Bacon 695-700).
24. "The reform also taught people in their own language." **SUMMARY HOLDS** (German Mass, catechism).
26. "Wittenberg's first hymn-book was printed in 1524 and held eight hymns, four of them Luther's." **MODERN ONLY.** This is Bacon's modern bibliographic judgment: "The earliest hymn-book of the Reformation ... was published at Wittenberg in 1524, and contained eight hymns, four of them from the pen of Luther himself" (Bacon 687-690). No old text in the Library holds it.
29. "The reform's chief tool for forming people was a household catechism, written in 1529." **SUMMARY HOLDS.**
    - Formula of Concord: "the Small and Large Catechisms of Dr. Luther ... as the Bible of the laity" (BoC 25518-25520).
    - Luther, March 3, 1529: "The Catechism is not ready, but it will soon be" (Currie 12227).
    - Note: 30–32 take their details from the Large Catechism's preface and 33 from the Small. The piece merges the two into one "household catechism".
30. "Its three parts were the Ten Commandments, the Creed and the Lord's Prayer." **SOFTENED OR CHANGED.**
    - The source calls these three the minimum for common folk, then goes on: "for the common people we are satisfied with the three parts ... Now, when these three arts are apprehended, it behooves a person also to know what to say concerning our Sacraments ... Baptism" (LC 251-252, 342-345).
    - Both catechisms continue with Baptism and the Supper, and the Small with Confession (SC 395 ff.). "Its three parts were" drops the sacraments, which the piece itself made central in 5–7.
34. "At his table, Luther told his students that his wife, Katharina von Bora, had asked him why the old church prayed so hard, and their own household so coldly." **SOFTENED OR CHANGED.**
    - Source: "my wife said unto me, Sir! how is it, that in Popedom they pray so often with great vehemence, but we are very cold and careless in praying? I answered her, ... we, indeed, are ice cold therein" (TT 3144-3149).
    - The contrast in the source is Popedom against "we", the evangelical side. The piece narrows "we" to "their own household".
    - It also leaves out Luther's answer, which accepts the charge ("we ... are ice cold").
    - "Students" is not in the passage. "Katharina von Bora" is a fair identification of "my wife" (compare "Kate my wife", TT 3014).
36. "Melanchthon wrote the Augsburg Confession for it." **SUMMARY HOLDS.** Luther, May 15, 1530: "I have read Philip's Apology, with which I am delighted" (Currie 13614-13615). Note: that this "Apology" is the Confession is the editor's identification (Currie headnotes 13010-13014, 14233-14234).
40. "In 1525 Luther wrote against the peasants' rising, and in 1543 he wrote a treatise against the Jews." **NOT FOUND (1543 part).**
    - 1525 is held: Admonition to Peace, Against the Robbing and Murdering Hordes, and the Open Letter (PE v4, contents line 9 and 118 ff.; dated by the editors' headings).
    - I searched all `luther_*` files, Currie, the De Wette Briefe and the Library at large for the 1543 treatise ("Jews and their lies", "Von den Juden", "1543"). Nothing holds it.
    - The piece says so itself in 41. Even so, 40 tells a fact for which no Library text is the ground.
42. "Luther died in the mid-1540s." **SUMMARY HOLDS.** Aurifaber, 1569: "in the years 1545 and 1546, before the death of that most famous Divine, Luther" (TT 140). Note: the vagueness loses a documented date.
43. "In 1580 a fuller book of confessions was gathered, the Book of Concord." **SUMMARY HOLDS (date bibliographic).** The preface's own text (BoC 440-1100) names 1530, 1537 and 1558 but prints no year of its own. 1580 comes from Jacobs's front matter.

**Heart:** right. "Terrified conscience" consoled by the promise is the Confession's own word for what its teaching is for (AC XX). The piece is the most carefully hedged of the six; it even discloses the missing 1543 treatise. Its failures are three modern hymnological facts (22, 23, 26) and three compressions (7, 30, 34).

---

## P03: Tacitus

Library files used: `tacitus_annals-15-44_church-brodribb1876.txt` (Ann.), `anf03_tertullian.xml`, `npnf211_sulpitius-severus-vincent-lerins-cassian.xml`, `suetonius_lives-of-the-caesars-loeb_rolfe1914.txt`.

HELD, with anchors:
- 1, 2: Ann. 15.44, "Covered with the skins of beasts, they were torn by dogs ... nailed to crosses, or ... burnt, to serve as a nightly illumination, when daylight had expired. Nero offered his gardens ... mingled with the people in the dress of a charioteer".
- 5, 10: "Christus, from whom the name had its origin, suffered the extreme penalty during the reign of Tiberius at the hands of one of our procurators, Pontius Pilatus".
- 7: "all human efforts ... and the propitiations of the gods, did not banish the sinister belief that the conflagration was the result of an order".
- 8: "to get rid of the report, Nero fastened the guilt and inflicted the most exquisite tortures on a class hated for their abominations, called Christians by the populace".
- 11: the Latin is "Exitiabilis superstitio" (quoted in `apologists-fragmentary_reliquiae-corpus-apologetarum-vol9-grc-lat_otto1872.txt` 12189). "Deadly" renders exitiabilis faithfully. Church and Brodribb have "most mischievous".
- 12: "broke out not only in Judaea, the first source of the evil, but even in Rome, where all things hideous and shameful ... find their centre". "The Roman province around Jerusalem" is an allowed gloss.
- 13: "an arrest was first made of all who pleaded guilty; then, upon their information, an immense multitude".
- 14: "not so much of the crime of firing the city, as of hatred against mankind".
- 19: Tertullian, Apology 16: "the said Cornelius Tacitus (the very opposite of tacit in telling lies) ... when Cneius Pompeius captured Jerusalem, he entered the temple ... but found no image there" (anf03 2583-2586). Also To the Nations 1.11, "most loquacious in falsehood" (anf03 10094-10095).
- 21: Sulpicius, Sacred History 2.29, "the most cruel tortures were accordingly inflicted upon the innocent" (npnf211 10660-10661).
- 22, 23: Ann. 15.44, closing sentence.

Non-HELD:

3. "The Roman who tells it, the historian Tacitus, thought they were criminals." **SUMMARY HOLDS.** "even for criminals who deserved extreme and exemplary punishment".
4. "Writing about fifty years after the great fire of Rome in 64, Tacitus gives the fullest account outside the church of what Nero did to the Christians." **MODERN ONLY (date and interval).**
   - Neither the year 64 nor a date of writing is in the held text.
   - Both come from the vendoring header: "Written c. 116 CE, describing events of 64 CE" (Ann. file lines 8-9). The file warns that the Library holds only 15.44.
   - "Fullest account outside the church" checks out against the Library. Suetonius has one line: "Punishment was inflicted on the Christians, a class of men given to a new and mischievous superstition" (Suetonius 28523-28525).
6. "He despised them and said so." **SUMMARY HOLDS.** His own words: "a most mischievous superstition ... the first source of the evil ... all things hideous and shameful".
9. "Tacitus stops to explain the name, and gives Christ in its Latin form." **SUMMARY HOLDS** ("Christus, from whom the name had its origin").
15. "Their deaths were made a show, as Nero held games at the chariot-racing ground." **SUMMARY HOLDS.** "Mockery of every sort was added to their deaths ... was exhibiting a show in the circus". "Chariot-racing ground" glosses "circus".
16. "Almost everything known of these deaths rests on this one chapter, and Tacitus never says where he learned of Christus." **SUMMARY HOLDS.** This is a statement about the record, and it checks out against the Library. Suetonius gives one line. Sulpicius retells Tacitus's own sequence (see 20). The chapter names no informant. The card lists the second clause as "uncertain".
17. "About the year 200, Tertullian, defending the Christians, answered him by name over another of his histories." **MODERN ONLY (date).** The Apology bears no date. The ANF dating is editorial: "dates this treatise circa A.D. 197" (anf03 6536; compare anf03 974). The rest is held: "In the fifth book of his histories" (anf03 2571).
18. "Tacitus had written there that the Jews honored an ass's head, a charge Tertullian thought had passed to the Christians." **SUMMARY HOLDS.** "they consecrated a head of this species of animal. And as Christianity is nearly allied to Judaism, from this, I suppose, it was taken for granted that we too are devoted to the worship of the same image" (anf03 2577-2582).
20. "About 400, Sulpicius Severus, a Christian writing a history of the world, told the same deaths in the same order." **SUMMARY HOLDS.**
    - The date comes from his own reckoning: "I have made the entire reckoning down to the time of Stilico" (npnf211 9778) and "up to the consulship of Stilico" (npnf211 10599).
    - Same order: "covered in the skins of wild beasts ... devoured by dogs, while many were crucified or slain by fire ... consumed to serve for light during the night" (npnf211 10662-10666).

**Heart:** right. An outside, hostile Roman witness whose contempt and whose pity both survive. Tertullian and Sulpicius are used to show how Christians answered him. That is the card's own frame ("Outside witness").

---

## P04: Basil of Caesarea

Library files used: `npnf208_basil-letters-select-works.xml` (Basil), `npnf207_cyril-jerusalem-gregory-nazianzen.xml` (Or. 43; a plain-text extract was used for reading), `eusebius_werke-bd2-2-...rufinus...schwartz-mommsen1908.txt` (Rufinus HE), `gregory-nyssa_life-of-macrina_clarke1916.txt`, `basil_ascetic-works-longer-shorter-rules_clarke1925.txt` (LR), `basil_opera-omnia-pg31-grc-lat_migne1857.txt`, `npnf214_seven-ecumenical-councils.xml`, `npnf202_...`, `benedict_rule-of-saint-benedict_gasquet1925.txt`.

HELD, with anchors:
- 1, 2, 3: Letter 223.2, "had wasted nearly all my youth in the vain labour ... Then once upon a time, like a man roused from deep sleep, I turned my eyes to the marvellous light of the truth of the Gospel" (Basil 39133-39135).
- 6, 16, 17, 18: LR 7, "He girded Himself and washed the feet of the disciples ... Whose feet then wilt thou wash? Whom wilt thou care for? In comparison with whom wilt thou be last if thou livest by thyself?" (LR 13457-13464; Greek in PG31 72547-72549, which has "whom" without "feet", as the card notes).
- 7: Or. 43.63, "Go forth a little way from the city, and behold the new city".
- 10, 14: Rufinus HE 11.9, "ambo de auditorio digressi ad profitendam rhetoricam rogabantur. quod opus magnifice quidem implebat Basilius ... ut sedentem Basilium de doctoris cathedra deponeret ac secum ad monasterium ... perduceret" (Rufinus HE 29989-29994).
- 12: Letter 223.2, "Then I read the Gospel ... the selling of one's goods, the sharing them with the poor ... I prayed that I might find some one of the brethren".
- 13: Life of Macrina, "Macrina took him in hand ... he forsook the glories of this world and despised fame gained by speaking" (Macrina 136).
- 15: Or. 43.29, "he set out ... into Pontus, and presided over the abodes of contemplation there. He himself too founded one".
- 23, 25: Or. 43.48-49, "Confiscation, banishment, torture, death ... a man who has nothing, is beyond the reach of confiscation; unless you demand my tattered rags, and the few books ... Death is my benefactor, for it will send me the sooner to God".
- 24: Or. 43 is a funeral oration.
- 26: Or. 43.58, "to seize his mules by the bridle and bar the passage with a robber band".
- 28: Letter 94, "lest ... I might come off worse than my accusers ... to whom do we do any harm by building a place of entertainment for strangers ... physicians, doctors, means of conveyance" (Basil 29985-30018).
- 29, 30: Or. 43.63, "the common treasury of the wealthy ... in consequence of his exhortations ... driven away from their cities and homes ... saluted them as brethren ... taking the lead in approaching to tend them".
- 31, 32: On the Holy Spirit 1.3 (Basil 8794-8799).
- 33: On the Holy Spirit 10.24, "It is not permissible, they assert, for the Holy Spirit to be ranked with the Father and Son" (Basil 10556-10558).
- 36: Creed, "who with the Father and the Son together is worshipped and glorified" (npnf214 13395).
- 40: Or. 43.79, "Around him poured the whole city".

Non-HELD:

4. "That waking set the course of his life in Caesarea, an inland city in Asia Minor." **SUMMARY HOLDS.** In Basil's own sequence the waking leads to the gospel and the search for monks (Letter 223.2). "Inland city" is an allowed gloss.
5. "Basil gave up teaching rhetoric for a life of prayer and shared work." **SUMMARY HOLDS.** Rufinus 11.9 (above). Macrina: "deserted it for this busy life where one toils with one's hands" (Macrina 136).
8. "As bishop from 370, he defended the Holy Spirit's place beside the Father and the Son." **MODERN ONLY (the year).** The card: "Made bishop in 370, by the same chronology [Blomfield Jackson]". No held old text gives 370.
9. "He died in 378 or 379, before a council confessed it." **MODERN ONLY (the years).** The card: "Jackson and W. K. L. Clarke give his death as 1 January 379. Gwynn gives the end of 378. Gregory of Nyssa says only that he died eight years after his election." That he died before 381 is held.
19. "A man alone has no one to serve." **SUMMARY HOLDS** (LR 7, the solitary serves only his own needs).
20. "The bishop of Caesarea made him a priest, though they quarreled." **SUMMARY HOLDS.** Or. 43.27-28: "to praise the Lord in the seat of the Presbyters ... There arose a disagreement between him and his predecessor in the rule over this Church".
21. "When the emperor Valens, who favored the party that ranked the Son below the Father, moved against the churches that held them equal, Basil came back to serve the bishop." **SUMMARY HOLDS.**
    - Or. 43.30-32: "an Emperor ... hostile ... to the more devout and pure party of Christians, who worship the Trinity ... the error of Arius ... dishonouring His offspring with his unequal degrees of Godhead ... He immediately returned with me from Pontus ... devoted himself to the service of his mother, the Church ... He was at once completely reconciled".
    - "To serve the bishop" compresses "the service of his mother, the Church" together with "completely reconciled".
22. "When the old bishop died, Gregory says, Basil was chosen against the bishops of the province." **SUMMARY HOLDS.** Or. 43.37: "not without difficulty or without the envious struggles of the prelates of his native land".
27. "Basil answered by making his brother bishop of Nyssa and his friend bishop of Sasima, a hurt, Gregory said, that time had not healed." **MODERN ONLY (the Nyssa link).**
    - Or. 43.59 says only: "the disaster ... resulted in the multiplication of the Bishops of the country ... I myself was treated as an appendage to this scheme ... a cause of pain which even time has not obliterated". It names neither see and does not mention the brother.
    - Socrates holds the two bishoprics but no reason for them: "Gregory was first made bishop of Sasima" (npnf202 21065-21066); "Gregory Basil's brother, bishop of Nyssa" (npnf202 15175).
    - That the Nyssa consecration was part of Basil's answer to the rival bishop is Jackson's synopsis: "Basil Forces Gregory of Nazianzus to be consecrated bishop of Sasima, and consecrates his brother Gregory to Nyssa" (Basil 722-724).
    - The Sasima half is fairly implied by Gregory's "appendage".
34. "He answered from what the church already did, and in a letter put it this way: 'As we were baptized, so we confess our faith ...'" **SUMMARY HOLDS.**
    - Letter 159.2: "As we were baptized, so we profess our belief. As we profess our belief, so also we offer praise" (Basil 33483-33485).
    - On the Holy Spirit makes the same argument: "either not to baptize as we have received, or not to believe as we were baptized, or not to ascribe glory as we have believed" (Basil 14168-14170).
    - Caution: the card says Letter 159 (Jackson, about 373) comes before the attack and "is not his reply to the attackers". The wording "and in a letter put it this way" invites that reading.
35. "Gregory admits that in writing Basil held back the bare words that the Spirit is God, from caution, though he often preached it." **SUMMARY HOLDS.**
    - Or. 43.68-69: "The enemy were on the watch for the unqualified statement 'the Spirit is God' ... His treatise on this subject ... He postponed for the time the use of the exact term ... his often having publicly preached this truth".
    - Note: Gregory is defending Basil here, not admitting a fault. "Admits" adds a shade the source lacks.
37. "Rufinus put his Rule into Latin in 397 or 398." **MODERN ONLY.** The card: "Fremantle lists ... the Rule of St. Basil, put into Latin at Pinetum for the abbot Urseius in 397 or 398." The translation itself is held through Gennadius, but not its date.
38. "In the sixth century Benedict of Nursia closed his own Rule by pointing his monks to Basil's as an example of good living." **SUMMARY HOLDS.**
    - Rule 73: "the Rule of our Holy Father St. Basil, but examples of the virtues, of the good living and obedience of monks" (Gasquet 4291-4293).
    - "Sixth century" converts Gregory's Dialogues, Totila's visit (`gregory-great_dialogues_gardner1911.txt` 16, 207).
39. "In 787 a council told the houses still standing where men and women lived as monks, side by side but apart, to keep his rule." **SUMMARY HOLDS.** Canon 20: "The double monasteries which are already in existence, shall observe the rule of our holy Father Basil ... monks and nuns shall not dwell together in the same monastery" (npnf214 41060-41062). "Side by side but apart" glosses this fairly.

**Heart:** right. The waking, the common life (LR 7), the Basileias and lepers, and the Spirit argued from worship are what Basil's own letters and Gregory's oration put at the centre. It also matches the card. The failures are the Jackson chronology (8, 9, 37) and one editorial causal link (27).

---

## P05: Rufinus of Aquileia

Library files used: `npnf203_theodoret-jerome-gennadius-rufinus.xml` (N3), `npnf206_jerome-principal-works.xml` (N6), `npnf202_...` (Socrates).

HELD, with anchors:
- 2: Jerome Letter 3, "The friendship which can cease has never been real" (N6 3941-3942).
- 4: Apology to Anastasius, "I have just returned to my family after an absence of nearly 30 years" (N3 45950-45958); "of Aquileia" is from Gennadius 17.
- 5, 7: Preface to the Church History, "translating into Latin the ecclesiastical history ... of Eusebius" (N3 58745-58747). The two added books are in the card's brief.
- 10: Apology to Apronianus II, "stayed six years, and again after an interval for two" (N3 49435).
- 14, 15, 16, 17, 18: Preface to First Principles (N3 45775-45780; the card's lines).
- 20: Jerome, Apology I, "books had been falsely translated by another" (N3 51284).
- 21: Jerome Letter 81 (card).
- 22: Jerome Letter 124.2 (card).
- 23, 24: Jerome, Apology I.7 (N3 51325-51331; Latin, Migne PL23 31112-31115).
- 25: "I am not a defender or a champion of Origen ... cutting out not a few passages; but only those as to which I had come to suspect that the thing had not been so stated by Origen himself" (N3 46061-46070).
- 26: "it will be this very flesh in which we now live" (N3 45989-45991); "the eternal fire" (N3 46010).
- 27, 28: Anastasius to John, "his object was to disintegrate our faith" (N3 46164); "bring his conscience to the bar of the divine majesty" (N3 46151); "know nor wish to know either what he is doing or where he is living" (N3 46224).
- 30, 31, 32: Preface to the Church History, "when the gates of Italy were broken through by Alaric the commander of the Goths ... it might to some extent become oblivious of their actual sufferings" (N3 58737-58750).
- 35: Socrates II.1 (card).
- 37: Preface to Numbers, "the Barbarian was within sight of us; he had set fire to the city of Rhegium" (N3 58986-58988).
- 38, 39: "the short comments upon Deuteronomy alone are wanting; these, if God so will, and if he restores my eye-sight, I hope to add" (N3 59011-59013).

Non-HELD:

1. "Jerome heard, in 374, that his friend Rufinus was traveling among the monks in the far parts of Egypt. He wrote to draw him to Syria ..." **MODERN ONLY (the year).** The letter is held: "remotest parts of Egypt, visiting the monks" (N6 3773). The year 374 comes from the editors' heading. The card says: "written from Antioch in 374 by the editors' heading".
3. "Within thirty years, a book Rufinus translated had ended theirs." **SUMMARY HOLDS.** It follows from 1 and from Jerome's Apology. Note: the interval depends on the modern 374 and 397.
6. "One was First Principles, by Origen, a Greek Bible scholar of the 200s, much admired and by now much attacked." **SUMMARY HOLDS** (a gloss; the attacks are in Epiphanius and Jerome).
8. "First Principles and many of Origen's other works survive chiefly in his reworded Latin, his editors note." **MODERN ONLY.** This is the ANF vol. 4 introductory note (card): "On First Principles comes to us chiefly in Rufinus's Latin". Attributing it to the editors discloses its source but does not make it an old-source claim.
9. "And the preface to First Principles broke his friendship with Jerome." **SUMMARY HOLDS.** Jerome takes the preface as aimed at him (Letter 81). Jerome says the injury came "since friendship had been restored between us" (N3 50495-50499).
11. "When the emperor turned on the monks there for their creed, he says, he was jailed and exiled." **SUMMARY HOLDS.**
    - Rufinus: "My faith ... was sufficiently proved when the heretics persecuted me. I was at that time sojourning in the church of Alexandria, and underwent imprisonment and exile" (N3 45963-45966).
    - The emperor comes from Socrates IV.24, not from Rufinus. Note: "he says" attaches Socrates's framing to Rufinus, who names "the heretics".
12. "At Jerusalem, in the 390s, a bishop from Cyprus charged that Origen taught souls had sinned in heaven before birth, that the devil would be saved, and that this flesh would not rise." **MODERN ONLY (the decade).** The charges are held in Epiphanius, Letter 51, in Jerome's Latin (card). "390s" is an editorial date (low severity).
13. "Jerome took his side, Rufinus the other, but they made peace before Rufinus sailed home." **SUMMARY HOLDS.**
    - Jerome: "since friendship had been restored between us, and that with difficulty and much trouble" (N3 50499-50500); "unfaithful after the restoration of our friendship" (N3 55903).
    - The sides: Jerome translated Epiphanius's letter. Fremantle's introduction states the sides outright.
19. "The rule of faith is the church's summary of its belief." **SUMMARY HOLDS** (an allowed clarifying gloss).
29. "Each wrote a full defense against the other, and the friendship did not recover." **SUMMARY HOLDS.** The Apology to Apronianus and Jerome's Apology are both held. Jerome's later hostility is in his later letters (the "scorpion" line, card).
33. "The few Greek fragments of First Principles show, his editors note, that he altered Origen's wording." **MODERN ONLY.** ANF introduction: "was justly chargeable with altering many of Origen's expressions" (card).
34. "His History became the Latin West's Eusebius through the Middle Ages, an editor judges." **MODERN ONLY.** McGiffert: "became in the Western Church a substitute for the original throughout the Middle Ages" (card).
36. "Rufinus's last work came in Sicily, about 410 by his editor's date." **MODERN ONLY.** Fremantle's note: "410. The date is fixed by the burning of Rhegium by Alaric" (N3 58973). "Last work" is also Fremantle's.
40. "He died soon after, his editors judge." **MODERN ONLY.** Fremantle, and the notes to Jerome identifying the "scorpion" (card).

**Heart:** right. A friendship ended by a translation, with both men's own words. But the piece hands over its legacy and ending to the editors four times (8, 33, 34, 36/40). Attribution does not cure it under this rule. The old sources can carry the ending: the Numbers preface on its own is a strong close, and Gennadius 17 can carry the legacy.

---

## P06: Kongo, Afonso I

Library files used: `paiva-manso_historia-do-congo-documentos-por_1877.txt` (PM), `lopes_report-of-the-kingdom-of-congo_hutchinson1881.txt` (Lopes).

HELD, with anchors:
- 1, 2, 3: Letter of 6 July 1526, "pela grande e estreyta necesydade Em que estauamos de vinho e farynha pêra o santo sacramento ... nosa terra se despouoa toda" (PM 2351-2353, 2418).
- 6: Lopes, "taking the name of Dom Joao ... his son, who soon also became a Christian, taking the name of Affonso" (Lopes 3700-3707). Lopes is Pigafetta, Rome 1591.
- 8: Letter of 1512 to the pope, "mandarão a estas terras pessoas religiosas, com a doctrina dos quais (sendo nós enganados pelo demónio, adorando Ídolos) nos apartamos" (PM 539-541). Paiva Manso's note cites Damião de Góis's Chronicle of D. Manuel as his print source (PM 551), which is allowed as help in finding a text.
- 9, 10: Letter of 27 May 1517, "os meus parentes que eu enviava a eses Reynos haprender ... por alumiar os cegos que sam em meus Reynos pêra que depois de minha morte posam sostentar ha fé" (PM 1927-1934).
- 11, 12: Lopes, "his brother, who was called Pango ... opposed to the Gospel command ... that a man shall have but one wife ... whose wives, seeing themselves separated from their lords ... spoke evil of the new religion" (Lopes 3709-3720).
- 13: "Affonso favoured the Christian religion in order to usurp his place ... deprived the prince of the province ... got the king to retract the sentence" (Lopes 3722-3740).
- 14: "kept the death of the king concealed for three days ... that she would keep it secret till he arrived" (Lopes 3763-3771).
- 15: "a great force ... nearly 200 thousand men"; "routed" (Lopes 3804-3807, 3998).
- 17: "os ditos mercadores leuam cada dia nossos naturaes filhos da terra e filhos de nossos fidallgos e vassallos e nossos parentes" (PM 2412-2414).
- 18: "nam temos necesydade desses Reynos mães que de padres e algumas poucas pessoas pêra emsynarem nas escollas nem menos de nenhumas mercadoryas" (PM 2419-2421).
- 19: "nossa vontade he que nestes Reynos nam aja trato de esprauos nem sayda pêra elles" (PM 2424-2425).
- 20: the letter is a request ("pedymos a vossa alteza").
- 22, 23, 24: Letter of 17 December 1540, "Ja escrevemos a vossa alteza que vertuoso padre frey alvaro ... ordenou hum dia de páscoa com sete ou oyto homens brancos, estamdo nos ouvímdo myssa tirassem todos com suas espimgardas ... polias nossas fraldas pasou o pilouro" (PM 3424-3430).
- 26: no other held document mentions frei Álvaro's plot. Searched PM for "frey/frei alvaro" and "Pessanha"; the only hits are this letter and its heading.
- 27: "Au muylo poderoso e exleiíte príncipe dom João Rey nosso Irmão"; "ElRey + dom affonso" (PM 2431-2434, 3445).

Non-HELD:

4. "Contact with Portugal had brought Kongo both the faith and this trade, and in his letters Afonso set the one against the other." **SOFTENED OR CHANGED.**
   - "In his letters" generalizes from the July 1526 letter. Afonso's other held letters do not set faith against the trade in slaves.
   - 18 October 1526, three months later: he sets up a law under which any white man who has bought "peças" must show them to three named nobles. They check "se ssam catiuos se forras" (whether they are captives or free). Once cleared, "as poderam leuar e Embarquar". He grants this "por ssabermos que tanto seu seruiço [he] e as peças que de nosso Reyno tiram" (PM 2549-2560).
   - 4 December 1540: he boasts that Kongo alone yields more to Portugal's trade than all the other rivers. No king, he says, favors the trade more, "abrimdo feiras, almadias, caminhos, pumbus omde se Resgatem as peças" (PM 3326-3334). He pays in a currency "com a quall se Resgatão peças" (PM 3352-3353).
   - 1514: he himself sends "esprivos" to Portugal as gifts and payment (PM 841-848).
   - The source's force is that he set kidnapping of free subjects, nobles and kin against faith and order, while regulating, and later promoting, the trade in captives. The piece flattens that into faith against trade.
5. "Portuguese ships reached the mouth of the Zaire River in 1491." **SUMMARY HOLDS.** Lopes: "the ships arrived ... in the year 1491 of our era, and anchored at the mouth of the Zaire" (Lopes 3511-3514). Note: this is told in the narrator's voice from a source written a century later. Lopes also reports earlier Portuguese arrivals at the Zaire (Lopes 3468-3477), so it is not a first arrival.
7. "Afonso spoke for himself in letters his scribes wrote down, and they survive, while almost everything else about Kongo's Christians was written by Portuguese and Italian outsiders." **SUMMARY HOLDS.**
   - Scribes: "dom Joham teyxeira o fez" (PM 2430); "Ruy godinho a fez" (PM 1945); "dom joam a ffez" (PM 3444).
   - "Almost everything else" holds against the Library's Kongo holdings: Lopes/Pigafetta, Cavazzi, Carli, Merolla, Zucchelli. PM also holds later Kongo kings' letters, hence "almost".
16. "By 1526, the letters turn to a harm that came with Portugal." **SUMMARY HOLDS.** Note: the 1514 letter already complains at length of Portuguese abuses, such as Fernão de Mello seizing goods and slaves (PM 840-860). The 1526 turn is to depopulation by kidnapping.
21. "It does not tell us what came of it." **SOFTENED OR CHANGED.**
   - The sentence is true of the July letter, but as an honest limit it misleads. The next letter in the same source, 18 October 1526 (PM 2549-2563, quoted at 4), tells what Afonso himself did next. He did not end the trade. He regulated it, protecting the free and letting inspected captives be shipped.
   - Presenting the outcome as unknown withholds the one held document that most changes how the quotation in 19 reads.
25. "It killed one man and wounded two." **SUMMARY HOLDS.** "foy dar no noso merinho moor que jumto com nossa pessoa estava e dahi foy matar hum homem e ferir dous outros" (PM 3430-3431). The ball first struck his chief bailiff.

**Heart:** partly wrong. The faith-against-trade frame (1, 4, 19, 21) is the modern textbook Afonso. The held letters show something harder and more distinctive. He is a Christian king who writes as Portugal's "brother" and asks for priests, teachers, wine and flour. He fights the kidnapping of free people, nobles' sons and his own kin. In the same year he licenses the shipping of inspected captives, and by 1540 he presents himself as the trade's best partner. The October 1526 law and the December 1540 boast belong in the piece, or the heart misstates what the sources show.

---

## Patterns across the six

1. **Editor chronology passed off as narration.** This is the largest category: 9 of 19 MODERN ONLY marks. The pieces are careful with claims and loose with years: Jackson's 370 and 378/379, Fremantle's 397/398 and 410, the editors' 374, ANF's c. 197, the vendoring header's 64 and c. 116, Bacon's 1 July 1523. Where the old text has no date, the narration should either drop the year or tie it to an old anchor (as P03 does well with Sulpicius and Stilicho).
2. **"His editors note / an editor judges" is not a cure.** P05 attributes four modern judgments openly. The rule says such a claim must not be told. Attribution only makes the breach visible.
3. **Compression that drops the counter-evidence.** P06 4 and 21, and P02 30 and 34, keep the quotable line and drop the next sentence in the same source, which changes its force. These are the most serious findings, because they would pass a quote-only check.
4. **Modern structural summaries in summary tiles.** P01 2, 4 and 6 state the modern reconstruction of early church order as fact. In one case (1 Clement 44) it runs against the old text.
