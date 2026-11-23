import json
c=json.load(open('john-cassian.card.json'))
log=[]
def rep(old,new,where):
    assert old in where, old
    return where.replace(old,new,1)
br=c['briefReferences']
def edit(i,old,new):
    br[i]=rep(old,new,br[i])
edit(0,"addressed to Honoratus and Eucherius; one wished","one wished")
edit(0,"this Part was dedicated to Honoratus and Eucherius.","this Part of seven Conferences was dedicated to the two.")
edit(4,"their bishop expelled with the help of the military.","their bishop expelled with the help of the military and sent into exile through a plot formed by four named bishops.")
edit(5," Egypt's rules tempered with the customs of Palestine and Mesopotamia where harsh climate or different ways made them hard in Gaul.","")
edit(6,"Chaeremon, as Cassian writes him, says","an old hermit, as Cassian writes him, says")
edit(7,"runs against the Fathers.","runs against the Fathers; the monks held that a choice of the chosen and the rejected made before the world began leaves effort useless.")
edit(8,"the Pelagians said that men could also be without sin if they liked.","Nestorius, as Gibson's note names him, declares that our Lord was born a mere man, and Cassian says the Pelagians said the same before him; the Pelagians said that men could also be without sin if they liked.")
edit(9,"grants only the first, and never names","grants only the first, that the beginning of every good thought is from God, and rejects the others, among them that the first beginnings of a good will sometimes arise in us; he never names")
br.insert(9,"Socrates, Ecclesiastical History, book 7, chapter 32, in the held English translation: Nestorius's priest Anastasius preached against calling Mary the Mother of God, and Nestorius rejected the word. Council of Ephesus, decree against Nestorius, in Seven Ecumenical Councils: Nestorius excluded from the episcopal dignity. Gibson dates On the Incarnation to the year before the council.")
c['uncertain'].append("Socrates, a historian of the same century, says the people charged Nestorius with teaching that the Lord is a mere man. Having read his writings, Socrates says he cannot grant that Nestorius denied the divinity of Christ; he seemed scared at the word for Mother of God. Cassian's charge in the seven books is that Nestorius declared our Lord born a mere man.")
kw=c['keyWorks'][0]
assert kw['title']=="The Institutes"
kw['about']+="; in its preface Cassian says he will leave out the wonders and tell only the rules of the monasteries and the remedies for the eight faults, and that he will temper Egypt's rules by the customs of Palestine and Mesopotamia where harsh climate or different ways made them hard"
c['sources']['about'].insert(4,{"title":"Ecclesiastical History, book 7, chapter 32","author":"Socrates Scholasticus","date":None,"language":"English translation","file":"cic/texts/npnf202_socrates-sozomen-ecclesiastical-histories.xml"})
c['sources']['about'].insert(5,{"title":"Decree of the Council of Ephesus against Nestorius, in The Seven Ecumenical Councils","author":None,"date":None,"language":"English translation","file":"cic/texts/npnf214_seven-ecumenical-councils.xml"})
json.dump(c,open('Card.pass2.json','w'),indent=2,ensure_ascii=False); open('Card.pass2.json','a').write("\n")
