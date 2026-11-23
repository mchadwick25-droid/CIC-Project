import json,re
p='pelagius.card.json'
s=open(p,encoding='utf-8').read()
d=json.loads(s)
q=d['quotationOriginals']
# FIX 1
assert q[0]['printed'].startswith('your spiritual riches')
q[0]={
 "modern": q[0]['modern'],
 "printed": "Spirituales vero divitias nullus tibi, praeter te, conferre poterit. In his ergo jure laudanda es : in his merito caeteris praeferenda es : quae nisi ex te, et in te esse non possunt.",
 "work": "Pelagius, Letter to Demetrias, ch. 11, ed. Migne (PL 30)",
 "file": "cic/texts/pelagius_epistula-ad-demetriadem-lat_migne.txt",
 "lines": "814-817",
 "englishPrinted": "your spiritual riches no one can have conferred on you but yourself; for these, then, you are justly praised, for these you are deservedly to be preferred to others,—for they can exist only from yourself and in yourself",
 "englishFile": "cic/texts/npnf105_augustine-anti-pelagian-writings.xml",
 "englishLines": "1281-1282",
 "uncertain": "The print is damaged; the wording given here is the reading it shares with Migne PL 33 lines 62416-62419 and Goldbacher lines 4493-4496, both also damaged, which quote the passage inside Augustine's Letter 188 without \"es\" after \"laudanda\". The English is B. B. Warfield's."
}
# FIX 2
assert q[1]['printed'].startswith("Non possunt esse ista bona nisi in te',")
q[1]['printed']="'"+q[1]['printed']
# step 2 additions
d['legacy']['traces'] += [
 "Bede, writing in 731, calls him \"a Briton\" who spread \"far and near\" the infection of his doctrine against the assistance of God's grace.",
 "Vincent of Lérins, in 434, asks who before \"that profane Pelagius\" gave free will so much strength \"as to deny the necessity of God's grace to aid it towards good in every single act\".",
 "Faustus of Riez, about 474, begins the list of chapters of his book On Grace with the view of Pelagius, who denied grace, which he says must first be destroyed.",
 "Constantius of Lyon, about 480, in his Life of Germanus, sets two sides of a public dispute against each other: on one side divine authority, on the other human presumption; on one side Pelagius as author, on the other Christ. Bede copies the passage."
]
d['sources']['about'] += [
 {"title":"On Grace (De gratia), list of chapters of Book 1","author":"Faustus of Riez","date":None,"language":"Latin","file":"cic/texts/faustus-riez_de-gratia-and-collected-works_engelbrecht1891.txt"},
 {"title":"Life of Germanus (Vita Germani)","author":"Constantius of Lyon","date":None,"language":"Latin","file":"cic/texts/constantius-lyon_vita-germani_levison1920.txt"},
 {"title":"Commonitorium, chapter 24 (Vincent of Lérins)","author":"Vincent of Lérins","date":None,"language":"English translation","file":"cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml"},
]
json.dump(d,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
open(p,'a').write('\n')
