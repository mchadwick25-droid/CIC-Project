import json
p='theodoret-of-cyrrhus.card.json'
raw=open(p,encoding='utf-8').read()
c=json.loads(raw)
rt=json.dumps(c,indent=2,ensure_ascii=False)+"\n"
print("roundtrip", rt==raw, raw.endswith("\n"))
def rep(s,old,new):
    assert s.count(old)==1,(old,s.count(old)); return s.replace(old,new)
# checker fixes
q=c['quotationOriginals'][3]
q['uncertain']=rep(q['uncertain'],"a stray mark where kai tes should stand; the first numeral is printed with a breathing mark that reads as the preposition ex.","a stray mark where tes should stand; the six of thirty-six is printed with a breathing mark that reads as the preposition ex.")
c['briefReferences'][1]=rep(c['briefReferences'][1],"the porticoes, two bridges and the conduit;","two bridges and the conduit;")
c['briefReferences'][3]=rep(c['briefReferences'][3],"his birth at Antioch from the Religious History; Ephesus in 431","Ephesus in 431")
# additions
c['keyWorks'].append({"title":"Compendium of Heretical Fables","about":"a controversial work that Blomfield Jackson lists beside the Eranistes; Photius counts five books of it"})
c['legacy']['traces'] += [
 "At the first session of Chalcedon, as the acts quoted by Blomfield Jackson record, the bishops of Egypt, Illyricum and Palestine called out as he entered, \"Cast out the teacher of Nestorius.\" Later the Egyptians and the bishops with them cried, \"Do not call him a bishop! He is not a bishop! Cast out the fighter against God! Cast out the Jew!\" The bishops of the East and of Pontus, Asia and Thrace shouted, \"We had to sign a blank paper; we were scourged, and so we signed.\" The officials answered, \"The vulgar cries are not worthy of bishops\".",
 "Blomfield Jackson tells that the emperor Theodosius, hunting near his capital in July 450, was thrown from the saddle into a stream, hurt his spine and died a few days afterwards. He says a council was then conceded to reconsider the Council of 449, that his note names Marcian as the emperor who summoned the bishops to Chalcedon, and that the decree keeping Theodoret in Cyrrhus appears to have been rescinded, so that he was free to present himself.",
 "Evagrius, writing about 593 from the acts, says that at the council of 449 the deposition of Eutyches was revoked by Dioscorus and his associates, sentence was passed on Flavian and on Eusebius of Dorylaeum, and they deposed Theodoret of Cyrus.",
 "A. C. Zenos adds that the Tripartite History, the Latin of the three histories made under Cassiodorus, consists of twelve books."
]
c['legacy']['remembered'] += [
 "Juvenal of Jerusalem, in the Syriac acts of 449, gives his decision that Theodoret be removed from the priesthood and from communion, calls all men to witness that \"not even a single communication between him and them ought to take place, nor ought they to offer salt, or (address even) a mere word, to him.\"",
 "The Syriac chronicle under the name of Zachariah, from the side that refused Chalcedon, says \"the story goes\" that Dioscorus, seeing Theodoret sitting upon the throne in the Council and speaking from it, rose, came down from the throne and sat upon the pavement, saying \"I will not sit with the wicked, nor with vain persons will I enter in.\" The chronicle does not name the council in that sentence."
]
c['uncertain'] += [
 "His parents' promise comes from his own letter to the consul Nomus, written to answer his accusers: \"Even before my conception my parents promised to devote me to God\".",
 "In his letter to Leo, bishop of Rome, he says \"I have been condemned without a trial\", and he asks Leo whether he ought to put up with the deposition: \"If you bid me abide by the sentence of condemnation, I abide\". These are his own claims, made to win Leo's help.",
 "In his Letter 119 he asked to be allowed to go to the West and plead his cause, or at least to be commanded to live in his monastery, which Jackson's note names as Nicerte. That the second request was granted is Jackson's statement, not Theodoret's.",
 "In his Prologue he gives his reason for writing the Church History: he thinks it not right to look on without an effort \"while oblivion robs noble deeds and useful stories of their due fame\".",
 "In Letter 150 to John of Antioch he says that Cyril's teaching renews \"that vain and impious teaching of Apollinarius which was long ago stamped out\". This is his charge against Cyril, written while he answered the anathemas.",
 "Blomfield Jackson says that at Ephesus in 431 Theodoret arrived with his metropolitan, Alexander of Hierapolis, and was one of the deputies of the Easterners who hurried to Constantinople but \"were allowed to proceed no further than Chalcedon\".",
 "In the second dialogue of the Eranistes a testimony of Methodius, bishop and martyr, from his discourse on the martyrs, is quoted; the translator's note says this is the only fragment of Methodius that Theodoret preserved.",
 "Hope W. Hogg, in the Ante-Nicene Fathers edition of Tatian's Diatessaron, cites Theodoret's book on Heresies, which he dates to 453, for the statement that Tatian cut out the genealogies and whatever other passages show that the Lord was born of the seed of David according to the flesh. Hogg adds that Theodoret found more than two hundred copies of the Diatessaron \"held in respect in the churches\". The book itself is not printed in the held volume, so the wording is the editor's.",
 "In the Religious History he says the crowds who came to Simeon were past counting and all tried to touch him and take a blessing from his leather clothes, and that Simeon devised standing on a pillar. This is his own account, read from the Greek of one damaged print.",
 "In the Religious History he says that Ishmaelites came to Simeon in bands of two hundred, three hundred and sometimes a thousand, broke their idols before him and took part in the divine mysteries, and that he was an eyewitness of these things and heard of them. This is his own account, read from the Greek of one damaged print."
]
c['sources']['about'] += [
 {"title":"Notes to the Ecclesiastical History of Socrates","author":"A. C. Zenos","date":None,"language":"English","file":"cic/texts/npnf202_socrates-sozomen-ecclesiastical-histories.xml"},
 {"title":"The Diatessaron of Tatian, introduction","author":"Hope W. Hogg","date":None,"language":"English","file":"cic/texts/anf09_gospel-of-peter-diatessaron-origen-commentaries.xml"}
]
open(p,'w',encoding='utf-8').write(json.dumps(c,indent=2,ensure_ascii=False)+"\n")
