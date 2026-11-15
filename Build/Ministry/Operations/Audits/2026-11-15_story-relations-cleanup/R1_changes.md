# Round 1 changes: story cards, "How it connects" (2026-11-15)

Answers to R1_review.md. Every BLOCKING finding in both sets is addressed; most MINOR findings are taken. The line as shipped is given for each story whose line changed in round 1 (51 of 62). Proposed lines were taken as worded or shortened; where a proposal added detail the connection did not need, the detail was left out.

## Decisions on points not taken as worded

- Cross-cutting (set B): home traditions the census now holds (Hungary Protestants, Catholics of Ceylon, Arab Evangelicals, Dutch Reformed Cape, Caribbean churches, Chinese Catholics, Mennonites & Amish). The lines now name them where the census itself tells the story's subject or episode, and the false "no tradition of its own" sentences are gone. Adding these ids to the cards' `relatedIds` (so "Nearby on the map" lists them) would add links, which this job may not do. Listed for the coordinator and Mark as a follow-up.
- plinys-two-ministrae: the set A proposal is taken, without the place list for Third-Century Anatolia ("the same wider region" is enough, and the place list read as filler).
- juliana-and-corpus-christi: Marie d'Oignies is dropped. The census Beguines text does not name her, and the connection holds without her.
- cassiodorus-vivarium: the Church of the East sentence in the set A proposal is left out; the line keeps only the Syriac Edessa link the card makes, now true to the census (Nisibis was Edessa's world a century before the school).
- severinus-of-noricum: "one earlier Christian voice" is gone; the line says only that Victorinus wrote in the same provinces around 300.
- ludmila-javorova: the married-priests sentence in the set B proposal is left out, to keep the line short.
- ramon-llull: the Franciscan sentence (placement reasoning) is cut; the Vienne link is kept.
- bruder-klaus-at-stans: the old "Zurich and Geneva" was loose, since Geneva was not in the Confederation; the line now names Zurich only.
- Eight lines had a sentence past 25 words after revision; each was split.

## Same-kind fix found in review

- scillitan-martyrs, story `text`: "he does not recognize the empire of this Christian tradition" was a bad replace of the Acts' words. The vendored ANF text (`cic/texts/anf09_gospel-of-peter-diatessaron-origen-commentaries.xml`, l.19787) reads "The empire of this world I know not", as the design prototype still does. Restored to "the empire of this world". The story's audio file has no manifest hash and was not checked (that would need a paid call).

## Lines after round 1

### silesian-childrens-prayer-revival
Before: The revival links to Herrnhut through Teschen. Many of the evangelical refugees Zinzendorf received from 1722 had been awakened by Pastor Johann Adam Steinmetz at Teschen's Jesus Church, the congregation this revival helped bring into being. No one has shown that a child of 1707-08 reached Herrnhut. The line runs through Teschen's evangelical life in the years after, not through a handoff between two named groups.
After: The revival links to Herrnhut through Teschen. Many of the refugees Zinzendorf took in from 1722 had been awakened by the Pietist pastor Johann Adam Steinmetz at Teschen's Jesus Church. This revival helped bring that congregation into being. Whether any of the praying children later reached Herrnhut is not known.

### plinys-two-ministrae
Before: The Scattered Households tell this story in their own account. Pliny questioned two enslaved women who held office among the believers. Third-Century Anatolia is the church of the same wider region about 130 years later, at Neocaesarea in Pontus and Olympus in Lycia.
After: The two women belonged to the Scattered Households, the house churches of Antioch, Asia Minor and Rome. Pliny's letter is the earliest outside account of those churches. Third-Century Anatolia is the church of the same wider region about 130 years later.

### perpetua-and-felicity
Before: Tertullian cites Perpetua's vision in On the Soul (55) within a few years of her death, a direct textual link. The Passio opens by defending new visions and prophecies, so some scholars read it beside Montanism. The Latin Pastoral tradition begins in the 240s, a generation later, in the same city.
After: Tertullian cites Perpetua's vision in On the Soul (55) within a few years of her death, a direct textual link. The account of their deaths opens by defending new visions and prophecies, so some scholars read it beside Montanism. The Latin Pastoral tradition begins in the 240s, a generation later, in the same city.

### abercius-epitaph
Before: Phrygia was the home of the New Prophecy. The epitaph's insistence on 'the same faith everywhere' has often been read as a mainstream Phrygian bishop's answer to it, though that link is plausible and unproven. Nisibis, the far end of his journey, belongs to Syriac Edessa, a tradition that begins around the same date.
After: Phrygia was the home of the New Prophecy. The epitaph insists on 'the same faith everywhere', and it has often been read as a mainstream Phrygian bishop's answer to the Prophecy. That link is plausible but unproven. Nisibis, the far end of his journey, belongs to Syriac Edessa, a tradition that begins around the same date.

### abitinian-martyrs
Before: This is the documented seed of Donatism. The Abitinians refused communion with a bishop who had handed over the scriptures under persecution, and that is the issue the Donatist dispute turned on. Latin Pastoral is the same North African congregational world, under Cyprian and Augustine.
After: This is the documented seed of Donatism. The Abitinians refused communion with a bishop who had handed over the Scriptures under persecution, and that is the issue the Donatist split turned on. Latin Pastoral is the same North African world of congregations, under Cyprian and Augustine.

### julians-galileans
Before: This is the Christian church as seen by its last imperial opponent, and it falls inside the years of Church & Empire (c. 312-451). The Cappadocians mention Julian as the emperor under whom their martyr Eupsychius was put to death.
After: This is the church as seen by its last imperial opponent, inside the years of Church & Empire (c. 312-451). Julian's reign struck the Cappadocians directly: their martyr Eupsychius was put to death under him in 362.

### moses-the-ethiopian
Before: Moses belongs to the world of the Desert: Scetis, Macarius and the Sayings. A formerly enslaved African who became an abba widens the picture of who lived in that world.
After: Moses belongs to the world of the Desert. He lived at Scetis, the home of Macarius, and the Sayings of the Desert Fathers keep his words. A formerly enslaved African who became an abba widens the picture of who lived there.

### fabiolas-hospital
Before: Fabiola belonged to Jerome's circle, with Paula, Marcella, Eustochium and Pammachius. Like them, she gave away a senatorial fortune. Basil's hospital outside Caesarea, built after the famine of 368, came first in the East. Jerome's claim that hers was the 'first' has to be measured against it.
After: Fabiola belonged to Jerome's circle, with Paula, Marcella, Eustochium and Pammachius, wealthy Romans who gave their fortunes away. Basil's hospital outside Caesarea, built after the famine of 368, was older than hers. So Jerome's claim that hers was the 'first' holds only for the Latin West.

### olympias-the-deaconess
Before: Olympias was the closest lay collaborator of John Chrysostom, the central figure of Antioch (c. 350-430), and his Constantinople years and exile frame her story. Her monastery beside the Great Church makes her a precursor of the urban women's communities of the Iconophiles, four centuries later. That is a lineage of place, not of documented influence.
After: Olympias was the closest lay collaborator of John Chrysostom, the central figure of the Antioch tradition, and his Constantinople years and exile frame her story. Her monastery beside the Great Church makes her a forerunner of the city's women's communities among the Iconophiles, four centuries later. The link is one of place, not of proven influence.

### simeon-on-the-pillar
Before: His biographer Theodoret was a man of Antioch, so the nearest tradition is Antioch under Chrysostom's heirs (c. 350-430). After 451 both the Syriac Orthodox and the Chalcedonian church of Antioch claimed Simeon. His language, origin and disciples were Syriac, yet his own church was Antioch's and he backed Chalcedon.
After: His biographer Theodoret was a man of Antioch, the world of Chrysostom and his heirs. After 451 both the Syriac Orthodox and the Chalcedonian church of Antioch claimed Simeon. His language, origin and disciples were Syriac, yet his own church was Antioch's, and he backed Chalcedon.

### genevieve-of-paris
Before: Geneviève stands at the opening of Merovingian Gaul (c. 480-620), whose cast is Clovis, Clotilde and the Gallo-Roman bishops. The Germanus who blessed her is Germanus of Auxerre, whose mission to Britain belongs to the British Church.
After: Geneviève stands at the opening of Merovingian Gaul (c. 480-620), whose leading figures are Clovis, Clotilde and the Gallo-Roman bishops. The Germanus who blessed her is Germanus of Auxerre, whose mission to Britain belongs to the British Church.

### severinus-of-noricum
Before: Severinus lived in the Danube provinces, whose one earlier Christian voice is Victorinus of Poetovio. He shows what became of the church there afterwards. The Rugian kings he dealt with were Homoian Christians, the world of the Gothic Homoians.
After: Severinus worked on the Danube frontier, in the provinces where Victorinus of Poetovio had written around 300. His story shows what became of the church there as Roman rule fell apart. The Rugian kings he dealt with were Homoian Christians, the world of the Gothic Homoians.

### cassiodorus-vivarium
Before: Cassiodorus was a contemporary of Benedict of Nursia and lived in the Italy of the Benedictines (c. 500-604). The two projects, Benedict's rule for living and Cassiodorus's rule for reading, are usually told together. The Nisibis school he had wanted to imitate belongs to Syriac Edessa.
After: Cassiodorus was a contemporary of Benedict of Nursia and lived in the Italy of the Benedictines (c. 500-604). Benedict's rule for living and Cassiodorus's rule for reading are usually told together. A century before the school at Nisibis he hoped to copy, Nisibis had been a home of Syriac Edessa, the world of Ephrem.

### masona-of-merida
Before: Masona's story is the immediate prehistory of Visigothic Iberia (c. 560-711). That tradition opens with King Reccared's conversion at Toledo III in 589, the event that ended Masona's exile. The Arian king who exiled him belongs to the world of the Gothic Homoians.
After: Masona's story is the immediate prehistory of Visigothic Iberia (c. 560-711). That tradition opens when King Reccared brought his kingdom into the Nicene church at the third council of Toledo in 589, ending Masona's exile. The Arian king who had exiled him belongs to the world of the Gothic Homoians.

### john-the-almsgiver
Before: John was the Chalcedonian ('Melkite') patriarch of a city whose church this map otherwise follows through its Coptic majority: the Church of Alexandria to 642, then Coptic Egypt. He stands for the minority church there just before the Arab conquest. The Jerusalem he relieved belongs to the Jerusalem pilgrimage tradition. The emperor who appointed him was Heraclius, of the Byzantine imperial church of 622-843.
After: John was the Chalcedonian ('Melkite') patriarch of Alexandria. This map follows that city's church through its Coptic majority: the Church of Alexandria to 642, then Coptic Egypt. John stands for the minority church there just before the Arab conquest. The Jerusalem he relieved belongs to the Jerusalem pilgrimage tradition. He was appointed by the emperor Heraclius, of the Byzantine imperial church of 622-843.

### caedmons-hymn
Before: Cædmon belongs inside Anglo-Saxon England (597-793). Hild and Whitby are among that tradition's voices, and Bede is its named source. The Whitby double house had Irish roots, since Hild was formed under Aidan, which ties it to Ireland & Iona.
After: Cædmon belongs inside Anglo-Saxon England (597-793). He was a herdsman at Hild's Whitby, and Bede, the great historian of that church, tells his story. Hild had been formed under Aidan, the monk from Iona, so Whitby also had roots in Ireland & Iona.

### kassia-the-hymnographer
Before: Kassia corresponded with Theodore the Studite, the central figure of the Iconophiles, and her flogging was part of their resistance. Her convent, founded after 843, opens the period of Macedonian Byzantium.
After: Kassia corresponded with Theodore the Studite, the central figure of the Iconophiles, and her flogging was part of their resistance. Her convent, founded after the icons returned in 843, belongs to the first years of Macedonian Byzantium.

### hrotsvitha-of-gandersheim
Before: The map has no Ottonian German tradition, so the links here are neighbors only. The Benedictine Reform of Late Anglo-Saxon England (c. 793-1066) was a contemporary of the learning at Gandersheim, and so was Cluny (909-1109). Gandersheim itself was a house of secular canonesses, not a reformed Benedictine convent.
After: The map has no Ottonian German tradition, so these are neighbors in time, not in place. The Benedictine Reform of Late Anglo-Saxon England was a contemporary of the learning at Gandersheim, and so was Cluny. Gandersheim itself was a house of secular canonesses, not a reformed Benedictine convent.

### peace-of-god
Before: Odilo, abbot of Cluny, 'lent his weight to efforts to limit private warfare.' That effort is the Truce of God. The knightly ethic the Peace of God tried to create fed into the Military Orders a century later.
After: Abbot Odilo of Cluny backed the Truce of God, the later form of the Peace. It tried to forbid fighting on set days of the week. The knightly ethic the Peace of God tried to create fed into the Military Orders a century later.

### christina-of-markyate
Before: Christina is the earliest well-documented English anchoress. She is a direct ancestor of the English Mystics (c. 1330-1440): Julian of Norwich's cell is the same institution two centuries later. The bishop who persecuted her and the abbey that protected her are the ordinary machinery of the Papal Church (c. 1049-1300).
After: Christina is the earliest well-documented English anchoress. She is a forerunner of the English Mystics (c. 1330-1440): Julian of Norwich's cell, more than two centuries later, was the same kind of life. The bishop who persecuted her and the abbey that protected her are the ordinary workings of the Papal Church (c. 1049-1300).

### hildegard-preaches
Before: Bernard of Clairvaux's support at Trier in 1147 is a documented link to the Cistercians. Her Cologne sermons against the Cathars put her beside them as a contemporary opponent. She founded houses but no order. The Rhineland Mystics begin about a century and a half after her.
After: Bernard of Clairvaux spoke for her at Trier in 1147, a documented link to the Cistercians. Her sermons at Cologne against the Cathars make her one of their opponents in their own time. She founded houses but no order. The Rhineland Mystics begin more than a century after her.

### great-alleluia-1233
Before: The preachers were friars of the first generation after their founders, a direct link to the Franciscans (1209-1300) and the Dominicans (1216-1300). The revival's successor was the flagellant outbreak of 1260. Both belong to northern Italy's lay confraternity culture, the world of the Humiliati.
After: The preachers were friars of the first generation after their founders, a direct link to the Franciscans (1209-1300) and the Dominicans (1216-1300). The revival was a forerunner of the flagellants of 1260. Both moved through the towns of Lombardy. There the Humiliati, lay men and women living a life of penance, had been at home since the twelfth century.

### juliana-and-corpus-christi
Before: Liège in the 1240s was the heartland of the Beguines. Marie d'Oignies came from the same diocese, and Juliana and her companion Eve belonged to the same semi-religious women's world. The friars who carried her cause were Dominicans.
After: Liège in the 1240s was the heartland of the Beguines, women who lived a religious life without taking vows. Juliana and her friend Eve belonged to that world of devout women. The friars who carried her cause were Dominicans.

### flagellants-of-1260
Before: The Joachimites had fixed on 1260 as the year the new age would open. The flagellants were the popular response of that year. Their immediate precursor was the Great Alleluia of 1233, and the lay confraternities they created are the Disciplinati world of late-medieval Italian piety.
After: The Joachimites had fixed on 1260 as the year the new age would open. The flagellants were that year's popular response. Their forerunner was the Great Alleluia of 1233, and they left behind lay brotherhoods of disciplinati, 'the disciplined', who shaped late-medieval Italian piety.

### ramon-llull
Before: Miramar was a Franciscan house, and Llull's mission theory shaped the order's later approach. So the Franciscans, in both their eras, are his nearest neighbors. The Vienne decree of 1311 belongs to the Papal Church of 1300-1517. He was a lay missionary with no institution of his own.
After: Miramar was a Franciscan house, and Llull's mission theory shaped the order's later approach. The Council of Vienne, which in 1311 took up his call for teaching Arabic, belongs to the Papal Church of 1300-1517. He was a lay missionary with no order behind him.

### bianchi-of-1399
Before: The Bianchi belong to the lay world of Parish Piety (c. 1400-1517), though that tradition is English and built from churchwardens' accounts. They came a generation before the friars' great sermon cycles of the Observants (c. 1368-1517). The split papacy behind them is the Papal Church of 1300-1517.
After: The Bianchi marched during the great schism, when rival popes divided the Papal Church (1300-1517). They came a generation before the Observant friars' great sermon cycles. Parish Piety follows the same kind of lay devotion in England in the century after.

### drummer-of-niklashausen
Before: He was a lay preacher with no learning and no license, a shadow of the Observant friars and their great sermon cycles. His program looked ahead to the Bundschuh risings and the Peasants' War. The Anabaptists and Wittenberg took up that legacy fifty years later.
After: He was a lay preacher with no learning and no license, a shadow of the Observant friars and their great sermon cycles. His program looked ahead to the Bundschuh peasant risings and the Peasants' War. The Anabaptists and Wittenberg had to reckon with that upheaval fifty years later.

### bruder-klaus-at-stans
Before: Bruder Klaus was a layman of the same time and region as the Observant preachers and the world of Parish Piety. Fifty years later the Confederation he held together gave rise to Reformed Zurich. Both Zwingli and the Catholic cantons later claimed him.
After: Bruder Klaus was a layman of the same years as the Observant preachers and the lay world of Parish Piety. A generation after him, Zurich, a member of the Confederation he held together, turned Reformed under Zwingli. Both Zwingli and the Catholic cantons later claimed him.

### montesinos-advent-sermon
Before: This sermon began the documented argument over conquest and mission in Spanish America, where the two came together. The argument runs under Mission-Born Christianities and the Catholicism of New Spain and Peru. Montesinos preached as a Dominican, true to the order's founding aim: a community that preached.
After: This sermon opened the first recorded argument over how Spain treated the peoples it conquered. In Spanish America conquest and mission arrived together, and the argument runs on through Mission-Born Christianities and the Catholicism of New Spain and Peru. Montesinos spoke as a Dominican, true to an order founded to preach.

### anne-askew
Before: Anne Askew died in 1546, the last year of Henry VIII, before England's turn toward Protestantism. Her circle around Catherine Parr and her sacramentarian views make her a forerunner of the Marian martyrs and of the world the Puritans later drew on.
After: Anne Askew died in 1546, the last year of Henry VIII, before England swung toward Protestantism under Edward VI. She moved in Catherine Parr's circle and denied that Christ was bodily present in the bread and wine. That makes her a forerunner of the Marian martyrs and of the world the Puritans later drew on.

### walatta-petros
Before: Walatta Petros was a leader of the revolt against Emperor Susenyos's Catholic policy, so fierce that he gave up the throne in 1632. That revolt is part of Ethiopia's Ordeal. The Jesuit side of the story belongs to the Jesuits.
After: Walatta Petros helped lead the resistance to Emperor Susenyos's Catholic policy, a revolt so fierce that he gave up the throne in 1632. That struggle is part of Ethiopia's Ordeal. The Jesuits who won the emperor over belong to the Society of Jesus.

### little-gidding
Before: Little Gidding lived the Laudian, Prayer Book world of the English Reformation at household scale. The Puritans attacked it as the 'Arminian Nunnery'. George Herbert's link ties it to the same Anglican devotional stream. Despite its quasi-monastic shape, it saw itself as Church of England and Protestant.
After: Little Gidding lived the Laudian, Prayer Book world of the English Reformation at the scale of one household. Puritan writers attacked it as 'the Arminian Nunnery'. George Herbert ties it to the same Anglican devotional stream. For all its near-monastic shape, it saw itself as Church of England and Protestant.

### jakob-boehme-the-shoemaker
Before: Böhme is the outstanding lay figure of the spiritualist current of the generation before him: the Family of Love and the Schwenckfelders. Franck and Schwenckfeld were among his indirect sources. Pietists and the Ephrata circle took up his work, which puts the Radical Pietists downstream of him.
After: Böhme is the outstanding lay voice of the spiritualist current that ran through the Family of Love and the Schwenckfelders a generation before him. Franck and Schwenckfeld were among his indirect sources. Later Pietists and the Ephrata circle took up his books, so the Radical Pietists stand downstream of him.

### hungarian-galley-pastors
Before: Hungarian Protestants have no tradition of their own on this map. Hungary appears on the map only through Transylvania, inside the Anti-Trinitarians. The closest parallel is the French Protestant galley convicts of the same generation, in the Church of the Desert and the Huguenots. The Dutch who bought the survivors free belong to the Dutch Reformation.
After: This episode belongs to Hungary's Protestants, whose churches lost pastors to the galleys in these years. The closest parallel is the French Protestant galley convicts of the same generation, in the Church of the Desert. The Dutch who won the survivors' release belong to the Dutch Reformation.

### candida-xu
Before: Her grandfather Xu Guangqi was one of the Chinese converts who argued out a Confucian Christian idiom, part of the Mission-Born Christianities. Candida carried that household's faith into the generation after that tradition ends on the map. The Jesuits she supported are the Society of Jesus.
After: Her grandfather Xu Guangqi was one of the Chinese converts who worked out a Confucian way of speaking about Christian faith. That work is part of the Mission-Born Christianities. Candida carried her household's faith into the next generation, among the Chinese Catholics of the Qing. The Jesuits she supported are the Society of Jesus.

### joseph-vaz-in-ceylon
Before: Sri Lankan Christianity has no tradition of its own on this map. Vaz came out of the Goan world of Portuguese church patronage, which the St. Thomas Christians met from the Malabar side. Here that same Portuguese church is at its most sympathetic: an Indian priest going where the Portuguese no longer could. His network of lay catechists shows the same instinct as the Korean Catholics later did.
After: Vaz's mission belongs to the Catholics of Ceylon, the church the Dutch had outlawed. He came out of the Goan world of Portuguese church patronage, which the St. Thomas Christians met from the Malabar side. Here that Portuguese church is at its most sympathetic: an Indian priest going where the Portuguese no longer could. His network of lay leaders shows the same instinct the Korean Catholics showed later.

### salzburg-emigrants
Before: Halle's Francke Foundations organized relief and publicity, and the Georgia settlement was a Halle project through Urlsperger, a direct link to Pietism (1675-1750). The Lutheran church that received them is the world of Wittenberg two centuries on. Zinzendorf's Herrnhut watched the emigration closely. The Silesian Children's Prayer Revival is the nearest story in kind: a hidden Protestant population under a Catholic prince, twenty-five years earlier and one border east.
After: Halle's Francke Foundations organized relief and publicity for the emigrants, and the Georgia settlement was a Halle project through Urlsperger, a direct link to Pietism. The Lutheran church that took them in was the world of Wittenberg, two centuries on. Zinzendorf's Herrnhut watched the emigration closely. The nearest story in kind is the Silesian Children's Prayer Revival. It too tells of a hidden Protestant people under a Catholic prince, twenty-five years earlier and one border east.

### genadendal-pear-tree
Before: George Schmidt was sent by the Moravian community of Herrnhut (1722-1815). Magdalena is the earliest named indigenous Christian leader in southern Africa, well before the African-Initiated churches of the 1880s on. The clergy who stopped Schmidt were the Cape's Dutch Reformed church, the colonial arm of the Dutch Reformation.
After: Georg Schmidt was sent from the Moravian community at Herrnhut. Magdalena is the earliest named indigenous Christian leader in southern Africa, long before Africans began founding churches of their own in the 1880s. The clergy who stopped Schmidt belonged to the Dutch Reformed Church at the Cape.

### ntsikanas-great-hymn
Before: Ntsikana was a Christian prophet outside the mission, about sixty years before the African-Initiated Churches begin. The missionary movement's native churches (1793-1906) are the missions he never joined. His followers' descendants, the Sogas and the Bokwes, staffed the first Presbyterian missions of the Eastern Cape.
After: Ntsikana was a Christian prophet who stood outside the mission, about sixty years before Africans began founding churches of their own. Before he died, he sent his followers to the missionaries. Their descendants, the Sogas and the Bokwes, staffed the first Presbyterian missions of the Eastern Cape.

### asad-shidyaq
Before: As'ad's life was an ancient Syriac-family church meeting nineteenth-century Anglo-American Protestantism. The Maronite church that confined him appears on this map only up to 1517, and he died at its patriarchate in the Qadisha valley. The mission he joined was the American Board's, one wing of the missionary movement's native churches. Arab Protestants have no tradition of their own on this map.
After: In As'ad's life an ancient Syriac-family church met nineteenth-century Anglo-American Protestantism head on. The American missionaries in Beirut called him their first convert and first martyr, at the start of the Arab Evangelical churches. The Maronite church held him at its patriarchal monastery in the Qadisha valley, and he died there.

### sam-sharpe-baptist-war
Before: The Native Baptist network Sharpe led descended directly from George Liele's mission in Jamaica. The mission church he also belonged to was the Baptist Missionary Society, which the Baptists trace to William Carey. In the United States, the Black Church is the parallel world of Black congregations under slavery.
After: The Native Baptist network Sharpe led grew directly from George Liele's mission in Jamaica. He also belonged to a church of the Baptist Missionary Society, which the Baptists trace to William Carey. His own story belongs to the Caribbean churches of slavery and emancipation. In the United States, the Black Church is the parallel world of Black congregations under slavery.

### damien-of-molokai
Before: Damien belonged to the new Catholic congregations of sisters and brothers who staffed hospitals across the world in the nineteenth century. The Hawaiian field he worked in is the Pacific wing of the missionary movement's native churches. That movement's Protestant side, Hyde's own church, is where the attack on him began. There is no Pacific Catholic tradition on this map.
After: Damien belonged to the new Catholic congregations of sisters and brothers who staffed schools and hospitals across the world in the nineteenth century. Hawai'i was also a Protestant mission field, part of the missionary movement's native churches. Charles Hyde, whose letter began the attack on Damien, was a minister of that Protestant world. The map has no tradition of Pacific Catholicism.

### onesimos-and-aster-ganno
Before: They were kept out of the Ethiopian empire of the nineteenth century, and the Orthodox clergy who tried Onesimos in 1906 belonged to it. The church their work founded became the Mekane Yesus church of modern Ethiopia. They worked inside a Swedish Lutheran mission, though their later church became Ethiopian.
After: They were kept out of the Ethiopian empire of the late nineteenth century, and the Orthodox clergy who tried Onesimos in 1906 belonged to it. They worked inside a Swedish Lutheran mission. The church their work founded grew into the Mekane Yesus church of modern Ethiopia.

### le-chambon-sur-lignon
Before: The plateau's Protestants are the direct heirs of the Church of the Desert and the Huguenots. The villagers themselves point to the memory of the Desert as the reason for their reflex to hide people. This is the twentieth-century sequel to traditions that stop in 1787. The Confessing Church is the German Protestant parallel of the same years; there was no organizational link.
After: The plateau's Protestants are the direct heirs of the Huguenots and the Church of the Desert. The villagers themselves name the memory of the Desert as the reason they hid people. Their story is the twentieth-century sequel to a church that won toleration only in 1787. The Confessing Church is the German Protestant parallel of the same years; there was no organizational link.

### franz-jagerstatter
Before: He was a layman of the Catholic Church of 1906-1962. His case, a conscience set against his own bishops' counsel, bears on that church's wartime record, Pius XII's included, which was argued about for decades. Dietrich Bonhoeffer of the Confessing Church is the Protestant parallel.
After: He was a Catholic layman in the decades between Pius X and the Second Vatican Council. His case, one man's conscience set against his bishop's counsel, bears on that church's wartime record, Pius XII's included, which was argued about for decades. Dietrich Bonhoeffer of the Confessing Church is the Protestant parallel.

### ludmila-javorova
Before: The Czechoslovak underground church was separate from the Lviv Underground. But the two worlds looked alike, with secret ordinations, night liturgies and bishops made in secret. The Persecuted Church covers the Protestant and Orthodox undergrounds of the same years.
After: The Czechoslovak underground church was separate from the Lviv Underground. But the two looked alike: priests ordained in secret, and liturgies held in apartments and forests. The Protestant and Orthodox undergrounds of the same years are the Persecuted Church.

### elcho-island-revival
Before: This is an indigenous-led revival of the kind the map groups with Ratana and the Balokole, though it produced no separate church. Charismatic Renewal in white Australian churches in the same decade was a parallel, not a cause. The map has no tradition of Aboriginal Australian Christianity.
After: This was a revival led by indigenous Christians, like Rātana in New Zealand and the Balokole in East Africa. Like the Balokole, it founded no separate church. Charismatic Renewal in white Australian churches in the same decade was a parallel, not a cause. The map has no tradition of Aboriginal Australian Christianity.

### montecorvino-at-khanbaliq
Before: He worked at the same Mongol court as the Church of the East under the Mongols, from the opposite side of the Christian world. Yahballaha III and Rabban Bar Sauma were his contemporaries, and the two traditions at times competed for the same converts. His mission grew out of the Franciscans' missionary reach a century after Francis.
After: He worked at the same Mongol court as the Church of the East, but came from the Latin, western side of the Christian world. Yahballaha III and Rabban Bar Sauma were his contemporaries, and the two churches at times competed for the same converts. His mission grew out of the Franciscans' missionary reach a century after Francis.

### benjamin-lay-burlington
Before: Lay was a far more radical forerunner of the reform the Quakers credit to John Woolman a full generation later. Woolman is known to have owned and read a copy of Lay's book.
After: Lay was a far more radical forerunner of John Woolman, who a full generation later turned the Quakers against slaveholding. Woolman is known to have owned and read a copy of Lay's book.

### ditt-chuhra-movement
Before: Ditt fits the same pattern as Liang Fa in China, in the missionary movement's native churches. An early convert became the real evangelist.
After: Ditt fits a pattern seen across the missionary movement's native churches, from India to Liang Fa's China. An early convert, not the mission, became the real evangelist.

### nickel-mines-forgiveness
Before: The Amish split off from the Anabaptist family in the 1690s, long after the first Anabaptist movements of 1525-1650.
After: The Amish began in the 1690s, in a split within the Anabaptist family, long after the first Anabaptist movements of 1525-1650. Their later history belongs with the Mennonites & Amish.
