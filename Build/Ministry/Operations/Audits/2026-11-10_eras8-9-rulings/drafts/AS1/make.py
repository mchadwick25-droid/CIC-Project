import json, sys
from lib import *

FACTS = []   # fact_table rows

def para(entry, field, items):
    """items: list of (sentence, [evidence dicts]) ; returns the paragraph text, logs fact rows."""
    out = []
    for sent, evs in items:
        out.append(sent)
        for ev in evs:
            row = {'entry': entry, 'field': field, 'sentence': sent}
            row.update(ev)
            FACTS.append(row)
    return ' '.join(out)

def text(entry, field, paras):
    return '\n\n'.join(para(entry, field, p) for p in paras)

WHW = "Thomas Whitehouse, Lingerings of Light in a Dark Land (1873)"
APPD = "Appendix D, Abstract of a brief history of the Syrians in Malabar, preserved among themselves (reprinted from the Church Missionary Society Report for 1818-19), in " + WHW
APPE = "Appendix E, the document of the Church people of Malankara assembled at Angamaly, 1 February 1787, in " + WHW
APPB = "Appendix B, list of the bishops of Malabar, in " + WHW

# ===================================================================== AP1
AP1 = 'st-thomas-christians-two-obediences'
e1 = {}
e1['id'] = AP1
e1['atlasId'] = 'TBD'
e1['era'] = 8
e1['name'] = 'The St Thomas Christians — Two Obediences'
e1['shortName'] = 'Two Obediences'
e1['informalName'] = 'The Thomas Christians Between Rome and Antioch'
e1['dates'] = '1665-1815'
e1['start'] = 1665
e1['end'] = 1815
e1['region'] = 'Malabar Coast'
e1['placeLabel'] = 'Malabar Coast'
e1['modernCountries'] = [{'country': 'India', 'countryId': 'Q668', 'place': 'Malabar Coast', 'placeId': 'Q473181'}]
e1['regions'] = ['Greater Asia']
e1['lane'] = '1 Syriac East & Asia'
e1['laneLabel'] = 'Syriac East & Asia'
e1['laneOrder'] = 1
e1['beyondFloor'] = False
e1['status'] = 'Pre-Survey Candidate'
e1['chip'] = 'psc'
e1['glyph'] = 'psc'
e1['statusWord'] = 'Researched — strong candidate'
e1['statusDescription'] = text(AP1, 'statusDescription', [[
    ("Tiered Strong (Tier 1) on two texts the community wrote itself, one for each party.",
     [rec('§5 G89-AP1 Tier and B1 (Strong)', 'tier and source claim restated from the record')]),
    ("Its window opens in 1665, where the entry on the Coonan Cross ends, and closes in 1815.",
     [rec('§5 G89-AP1 Dates; census VI.18 dates 1599-1665')]),
    ("Not yet reviewed.", [])]])
e1['living'] = False
e1['overlayCurrent'] = False
e1['c2'] = None
e1['sourcing'] = text(AP1, 'sourcing', [[
    ("Strong for this window.", [rec('§5 G89-AP1 B1 (Strong)')]),
    ("The Library holds two texts by the community itself, printed in English in 1873.",
     [lib('WH', "PRESERVED AMONG THEMSELVES AS THEIR GENUINE HISTORY."),
      lib('WH', "THE DOCUMENT signed by all the Church people of Malankara")]),
    ("One is a history kept by the Malankara party, whose date is unknown.",
     [lib('WH', "Reprinted from the ‘Church Missionary Society Report for 1818-19,”", note='Printed in 1818-19; the abstract itself is undated (record §5 AP1 Section A)')]),
    ("The other is the Angamaly document of 1787, from the party that kept to Rome.",
     [lib('WH', "a gathering of the Romo-Syrians, of more than ordinary importance, took place", note='Whitehouse names the Angamaly assembly of 1787 as Romo-Syrian and cites Appendix E (lines 14121-14130)')]),
    ("An English chaplain's book of 1873 and an English visitor's account of 1806 add outside views.",
     [rec('§5 G89-AP1 Evidence (Whitehouse 1873; Buchanan 1811 for the visit of 1806)')]),
    ("No Malayalam original has been read.", [rec('§5 G89-AP1 B1 (Varthamanappusthakam wanted; originals not seen)')])]])
e1['floorNote'] = text(AP1, 'floorNote', [[
    ("No question.", [rec('§5 G89-AP1 Section A (both parties clear)')]),
    ("The Malankara party's own history says Mar Evanius taught \"that Christ has one nature and that the Holy Ghost is equal with the Father and the Son\".",
     [lib('WH', "taught that Christ has one nature and that the Holy Ghost is equal with the Father and the Son")]),
    ("The other party stood under Rome.",
     [lib('WH', "This bishop was afterwards called the Bishop of Verapoly. He governed the followers of bishop Alexandrius; and from that time the pope has regularly sent bishops to Verapoly.")])]])
e1['relationsSummary'] = text(AP1, 'relationsSummary', [[
    ("This row carries on the church of the Coonan Cross.", [rec('census VI.18 relationsSummary; link VI.18 continued as this row')]),
    ("After 1665 its people took two roads.", [lib('WH', "At that time two parties were formed; one acknowledged the bishop Alexandrius, and are called Old Christians (Roman Catholics), and the other, who separated from the Portuguese, are called New Christians (Syrians).")]),
    ("One party took bishops from Antioch.", [lib('WH', "by the safe arrival, in 1665, of a bishop, sent by the Jacobite Patriarch of Antioch, to be Metropolitan of Malabar")]),
    ("The other kept to Rome, under Carmelite bishops at Verapoly.", [lib('WH', "This bishop was afterwards called the Bishop of Verapoly. He governed the followers of bishop Alexandrius; and from that time the pope has regularly sent bishops to Verapoly.")]),
    ("A bishop of the Church of the East came once, in 1708.", [lib('WH', "In 1708, by the direction of Mar Alea, Gabriel, a Nestorian bishop, arrived.")]),
    ("The Mar Thoma reform of 1836 grew inside the Antioch party.", [rec('census VIII.27 longDescription; link this row gave rise to VIII.27', 'the Malankara party is the one the reform divided')])]])
e1['why'] = text(AP1, 'why', [[
    ("In 1665 a bishop sent from Antioch reached Malabar.", [lib('WH', "by the safe arrival, in 1665, of a bishop, sent by the Jacobite Patriarch of Antioch, to be Metropolitan of Malabar")]),
    ("By his hands, the community's own history says, its leader Mar Thomas the Great \"was lawfully consecrated\".", [lib('WH', "By the laying on of his hands, Mar Thomas the Great, was lawfully consecrated")]),
    ("Part of the community went with Antioch, and part stayed with Rome.", [lib('WH', "At that time two parties were formed; one acknowledged the bishop Alexandrius, and are called Old Christians (Roman Catholics), and the other, who separated from the Portuguese, are called New Christians (Syrians).")]),
    ("In 1787 delegates of eighty-four churches wrote that in future they would have no bishop but one of their own.", [lib('WH', "We, the representatives of eighty-four churches in the diocese of Malankara"), lib('WH', "in future we will have no Bishop but from among ourselves")])]])
e1['entry'] = None
e1['teaser'] = text(AP1, 'teaser', [[
    ("The Malabar coast, 1665 to 1815 — one ancient church under two sets of bishops, and a paper of 1787 that said: no bishop but our own.",
     [lib('WH', "in future we will have no Bishop but from among ourselves"), lib('WH', "At that time two parties were formed; one acknowledged the bishop Alexandrius, and are called Old Christians (Roman Catholics), and the other, who separated from the Portuguese, are called New Christians (Syrians).")])]])
e1['longDescription'] = text(AP1, 'longDescription', [
 [("In 1653 the Thomas Christians swore at Mattancherry that they would have nothing more to do with the Jesuits.",
   [lib('WH', "Upon this our forefathers assembled at Muttan- cherry, and took an oath that neither they themselves, nor their descendants, should ever have anything to do with the Paulists."),
    lib('WH', "Then the Paulists (Jesuits) stopped the arrival of other Syrians", note="the translator's gloss reads Paulists as Jesuits")]),
  ("They named Archdeacon Thoma as their Metran, but he had been named only, and not consecrated.",
   [lib('WH', "where they duly nom- inated Archdeacon Thoma as their Metran"), lib('WH', "having been only nominated before, and not consecrated")]),
  ("In 1665 a bishop named Mar Gregorius arrived, sent from Antioch.",
   [lib('WH', "by the safe arrival, in 1665, of a bishop, sent by the Jacobite Patriarch of Antioch, to be Metropolitan of Malabar"), lib('WH', "In 1665, by the direction of St. Ignatius of Antioch, Mar Gregorius")]),
  ("By the laying on of his hands, the community's own history says, Mar Thomas the Great \"was lawfully consecrated\".",
   [lib('WH', "By the laying on of his hands, Mar Thomas the Great, was lawfully consecrated")])],
 [("Two parties formed.", [lib('WH', "At that time two parties were formed")]),
  ("In the words of the Malankara party's own history, one was the Old Christians, who are Roman Catholics, and the other the New Christians, who are Syrians.",
   [lib('WH', "At that time two parties were formed; one acknowledged the bishop Alexandrius, and are called Old Christians (Roman Catholics), and the other, who separated from the Portuguese, are called New Christians (Syrians).")]),
  ("The pope sent Carmelite bishops to Verapoly to govern the Old Christians.",
   [lib('WH', "This bishop was afterwards called the Bishop of Verapoly. He governed the followers of bishop Alexandrius; and from that time the pope has regularly sent bishops to Verapoly."),
    lib('WH', "Not long after, the Carmelites, who were then established at Goa", note='App. E names the Carmelites; the App. D text says "another Carmelite bishop, sent by the pope"') if False else lib('WH', "After these things came another Carmelite bishop, sent by the pope")])],
 [("More bishops came from the east.", [lib('WH', "In 1678, Mar Basilius, patriarch, and Mar Evanius, bishop, arrived.")]),
  ("In 1678, says the same history, Mar Basilius and Mar Evanius arrived.", [lib('WH', "In 1678, Mar Basilius, patriarch, and Mar Evanius, bishop, arrived.")]),
  ("Evanius \"re-established our former church services\" and taught the Trinity and one nature in Christ.",
   [lib('WH', "re-established our former church services, and taught that Christ has one nature and that the Holy Ghost is equal with the Father and the Son.")]),
  ("A priest of Kottayam, writing in 1869, dates the coming of Mar Evanius to 1685.",
   [lib('PHI', "in 1685, Mar Evanious the Bishop came from Antioch")])],
 [("In 1708 a bishop called Gabriel came \"by the direction of Mar Alea\".", [lib('WH', "In 1708, by the direction of Mar Alea, Gabriel, a Nestorian bishop, arrived.")]),
  ("The text calls him a Nestorian bishop, a name for the Church of the East.", [lib('WH', "In 1708, by the direction of Mar Alea, Gabriel, a Nestorian bishop, arrived."), rec('census VI.30 name and lane (Church of the East)', 'Nestorian is the text\'s word, an older name for the Church of the East')]),
  ("He taught that the Messiah has two natures, and \"much dispute arose\".", [lib('WH', "He taught the people that the Messiah has two natures and two substances, on which account much dispute arose.")]),
  ("Some Syrians and some Roman Catholics joined him.", [lib('WH', "Some Syrians and also Roman Catholics joined him.")]),
  ("After he died, the history says, those who joined him returned to their former parties.", [lib('WH', "Those who joined him returned to their former parties after his death.")]),
  ("A list of the bishops in the same book says he died at Kottayam in 1731.", [lib('WH', "GaxsRIkL, a Nestorian Bishop arrived 1708. He died at Cottayam, 1731.", note='OCR reads GaxsRIkL for Gabriel')])],
 [("In 1751, the history says, a patriarch and two bishops came from Syria.", [lib('WH', "1751, Mar Basilius, patriarch of the city of Bercea, in the county of Aleppo, Mar Gregorius, Metropolitan of Jerusalem, and Mar Evanius, bishop")]),
  ("For nineteen years they disputed with the Syrians.", [lib('WH', "For the space of nineteen years after their arrival there were disputes about different things between them and the Syrians.")]),
  ("Then letters from Antioch made Mar Thomas a Metropolitan, as Mar Dionysius.", [lib('WH', "Letters patent were sent ‘by Mar Ignatius, of Antioch, for Mar Thomas, who was consecrated Metropolitan by one of the above bishops, and called Mar Dionysius.")]),
  ("The list of bishops dates the three bishops to 1761 and the consecration to 1772.", [lib('WH', "Basitius, GREGORY, and JoHN, three Jacobite Bishops, arrived in 1761."), lib('WH', "he was con- secrated in 1772 by Mar Gregory, who died the same year.")])],
 [("On 1 February 1787 delegates of eighty-four churches met at Angamaly.", [lib('WH', "THE DOCUMENT signed by all the Church people of Malankara"), lib('WH', "We, the representatives of eighty-four churches in the diocese of Malankara")]),
  ("The English chaplain Whitehouse names them Romo-Syrians, Syrians in union with Rome.", [lib('WH', "a gathering of the Romo-Syrians, of more than ordinary importance, took place")]),
  ("Their paper says the Carmelites and the Jesuits \"oppressed our forefathers in various ways\".", [lib('WH', "Thus have these two religious orders oppressed our forefathers in various ways.")]),
  ("In future, it says, \"we will have no Bishop but from among ourselves\".", [lib('WH', "in future we will have no Bishop but from among ourselves")]),
  ("If the Queen of Portugal refused, they would turn to the Chaldean Patriarch.", [lib('WH', "we will transfer our allegiance to the Chaldean Patriarch, Mar Joseph")])],
 [("In 1806 the English chaplain Claudius Buchanan visited the Metropolitan, Mar Dionysius, at Kandanad.", [raw('buchanan', "Cande-nad , a Church of the Syrian Christians , November 23, 1806.") if False else raw('buchanan', "This is the residence of Mar Dionysius, the Metro¬ politan of the Syrian Church.")]),
  ("Buchanan wrote that the old man told him he had come \"to visit a declining Church\".", [raw('buchanan', "to visit a declining Church")]),
  ("The list of bishops says Mar Dionysius died about 1814.", [lib('WH', "He died about 1814.")])],
])
e1['voices'] = [
    "Mar Gregorius — the bishop sent from Antioch who reached Malabar in 1665 and consecrated Mar Thoma",
    "The signers at Angamaly — delegates of eighty-four churches who wrote the document of 1 February 1787",
    "Mar Gabriel — the bishop of the Church of the East who came to Malabar in 1708",
    "Mar Dionysius — the Metropolitan whom Claudius Buchanan met at Kandanad in 1806",
]
e1['legacy'] = text(AP1, 'legacy', [[
    ("In 1836 a reform began inside the Malankara party and divided it again.", [rec('census VIII.27 longDescription (reform of 1836 divided the ancient community)')]),
    ("The next entry tells that story.", [])]])
e1['livingEvidence_note'] = None
del e1['livingEvidence_note']
e1['documentedStories'] = []
e1['people'] = [{
    'name': 'The signers at Angamaly', 'year': 1787, 'voice': 1,
    'source': {'work': APPE, 'file': FILES['WH'], 'lines': find_lines('WH', "in future we will have no Bishop but from among ourselves"),
               'quote': "in future we will have no Bishop but from among ourselves"}}]
e1['reviewStatus'] = 'AI-checked'

# ===================================================================== AP2
AP2 = 'chinese-catholicism-1650-1906'
CE = 'cathen3'
e2 = {}
e2['id'] = AP2
e2['atlasId'] = 'TBD'
e2['era'] = 8
e2['name'] = 'Chinese Catholics Under Edict and Treaty'
e2['shortName'] = 'Chinese Catholics'
e2['informalName'] = 'The Church of the Court and the Provinces'
e2['dates'] = '1650-1906'
e2['start'] = 1650
e2['end'] = 1906
e2['region'] = 'China'
e2['placeLabel'] = 'China'
e2['modernCountries'] = []
e2['regions'] = ['Greater Asia']
e2['lane'] = '5 Latin West & Catholicism'
e2['laneLabel'] = 'Latin West & Catholicism'
e2['laneOrder'] = 5
e2['beyondFloor'] = False
e2['status'] = 'Pre-Survey Candidate'
e2['chip'] = 'psc'
e2['glyph'] = 'psc'
e2['statusWord'] = 'Researched — strong candidate'
e2['statusDescription'] = text(AP2, 'statusDescription', [[
    ("Tiered Strong (Tier 1) on Rome's rulings, the Jesuits' letters and one Catholic encyclopedia of 1908.", [rec('§5 G89-AP2 Tier 1, B1; sources opened in this draft')]),
    ("Its window runs from 1650, where the Ming China entry ends, to 1906, where the twentieth-century entry begins.", [rec('census VI.13c dates 1583-1650; census IX.65 dates 1906-c. 2010')]),
    ("Almost nothing in it comes from Chinese hands.", [rec('§5 G89-AP2 B1 (Chinese-language sources wanted)')]),
    ("Not yet reviewed.", [])]])
e2['living'] = False
e2['overlayCurrent'] = False
e2['c2'] = None
e2['sourcing'] = text(AP2, 'sourcing', [[
    ("Good for the eighteenth century, thinner for the nineteenth.", [rec('§5 G89-AP2 B1 (good for era 8; era 9 thin in the sweep, one source added here)')]),
    ("Almost every text is a missionary's or a Roman office's.", [rec('§5 G89-AP2 B1')]),
    ("They are the rulings of Propaganda and the Holy Office, a Jesuit's letter from Peking and a Catholic encyclopedia of 1908.",
     [lib('COL', "S. C. S. Officii 23 Martii 1656."), raw('lettres3', "A  Pékin,  ce  16  octobre  1724.".replace('  ', ' ')) if False else raw('lettres3', "A Pékin, ce 16 octobre 1724."), rec('the Catholic Encyclopedia vol. 3 (1908), article China, opened raw', 'archive.org catholicencyclop0003char')]),
    ("The Chinese edicts and memorials come only in the missionaries' translations.", [raw('lettres3', "Nous osons donc supplier Votre Majesté de")]),
    ("No text by a Chinese Catholic has been read.", [rec('§5 G89-AP2 B1 (Huang Bolu 1883 and Chinese texts wanted, not found)')])]])
e2['floorNote'] = text(AP2, 'floorNote', [[
    ("No question.", [rec('§5 G89-AP2 Section A (Catholic, Nicene)')]),
    ("This is the Catholic Church, which holds the Nicene Creed.", [rec('§5 G89-AP2 Section A')]),
    ("The Rites dispute was about practice, not the creed.", [rec('§5 G89-AP2 Section A')])]])
e2['relationsSummary'] = text(AP2, 'relationsSummary', [[
    ("This row carries on the church the Jesuit mission began in Ming China.", [rec('census VI.13c relationsSummary; link VI.13c continued as this row')]),
    ("It tells the Jesuits at the court, the Rites quarrel and the church of the provinces.", [rec('§5 G89-AP2 Mark\'s test and G89-23 (a)')]),
    ("Priests of the Paris Foreign Missions Society served in it from the 1660s.", [raw('cathen3', "The first departure from the Paris seminary took place 8 Nov., 1665.")]),
    ("The twentieth-century entry carries its story on from 1906.", [rec('census IX.65 dates 1906-c. 2010; link this row continued as IX.65')])]])
e2['why'] = text(AP2, 'why', [[
    ("For two and a half centuries the Catholic Church in China lived by the favor of the court and the text of edicts.", [raw('cathen3', "The Jesuits, as astronomers or interpreters were in high favour at Court"), raw('cathen3', "issued an edict exiling to Canton all missionaries with the exception of those occupying various offices at Court")]),
    ("Rome argued over whether Chinese Christians could honor Confucius and their dead.", [lib('COL', "christianis praenomatas caeremonias, quia videtur cultus esse mere civilis et politicus", rendering="the Holy Office allowed the ceremonies for Chinese Christians, 'because it seems to be a merely civil and political rite'")]),
    ("In 1724 an edict sent nearly every missionary out of the provinces.", [raw('lettres3', "notre sainte religion est entièrement proscrite à la Chine", rendering="our holy religion is entirely banned in China")]),
    ("Treaties of the 1840s and 1860s then opened the country again.", [raw('cathen3', "Special privileges were awarded to missions by Art. XIII of the French Treaty of T'ien-tsin (1858) and Art. VI of the French Peking Convention (1860)."), raw('cathen3', "In an edict of 20 Feb., 1846, Tao-kwang ordered that the establishments belonging formerly to Chris- tians be restored to their owners")])]])
e2['entry'] = None
e2['teaser'] = text(AP2, 'teaser', [[
    ("China, 1650 to 1906 — a church that served the emperor's court, split Rome over Confucius and outlasted a ban on its missionaries.",
     [raw('cathen3', "The Jesuits, as astronomers or interpreters were in high favour at Court"), lib('COL', "christianis praenomatas caeremonias, quia videtur cultus esse mere civilis et politicus"), raw('lettres3', "notre sainte religion est entièrement proscrite à la Chine")])]])
e2['longDescription'] = text(AP2, 'longDescription', [
 [("The Jesuit mission of the Ming years went on at the Qing court.", [rec('§5 G89-AP2 Mark\'s test (the Jesuits are one carrier: the court, 1650-1773)')]),
  ("The Jesuits served as astronomers and interpreters, and the Catholic Encyclopedia of 1908 says they stood high in favor under the emperor K'ang-hi.", [raw('cathen3', "The Jesuits, as astronomers or interpreters were in high favour at Court")]),
  ("In March 1692, it adds, a note from the president of the Board of Rites said it seemed unfair to ban the Europeans' religion.", [raw('cathen3', "In March, 1692, Ku Pa-tai, President of the Board of Rites and some of his colleagues addressed to the emperor a note to the effect that as Europeans were not guilty of any breach of the laws, it seemed unfair to prohibit their religion")]),
  ("An imperial decree approved the note and sent copies to all the provincial governors.", [raw('cathen3', "An imperial decree approved of this note, and copies were sent to all the provincial governors.")])],
 [("The Rites quarrel asked what a Chinese Christian might do for Confucius and the dead.", [lib('COL', "Num accipiendorum gra- duum caeremoniam, quae fit in aula Confu- cii, christiani litterati licite agere valeant", rendering="whether Christian scholars may lawfully perform the ceremony of taking degrees, which is held in the hall of Confucius")]),
  ("On 23 March 1656 the Holy Office answered questions that missionaries in China had sent to Rome in 1645.", [lib('COL', "Ab aliquibus in regno Sinarum missionariis pro- posita fuerunt, anno 1645, Sacrae Congrega- tioni de Propaganda Fide infrascripta et alia quamplurima quaesita", rendering="questions put by some missionaries in the kingdom of China in the year 1645 to the Sacred Congregation of Propaganda"), lib('COL', "S. C. S. Officii 23 Martii 1656.")]),
  ("It allowed Chinese Christians the ceremony of the Confucius hall, \"because it seems to be a merely civil and political rite\" (our rendering).", [lib('COL', "christianis praenomatas caeremonias, quia videtur cultus esse mere civilis et politicus", rendering="because it seems to be worship merely civil and political")])],
 [("Rome later turned against the rites.", [raw('cathen3', "the whole knotty question was settled (11 July, 1742) by a Bull")]),
  ("Charles Maigrot of the Paris Foreign Missions Society, vicar apostolic of Fujian, condemned them in a mandate of 1693.", [raw('cathen3', "March, 1693, Charles Maigrot, of the Missions Etran-"), raw('cathen3', "Bishop of Conon, issued a mandate condemning the Chirfese Rites.")]),
  ("A bull of Benedict XIV settled the matter on 11 July 1742.", [raw('cathen3', "the whole knotty question was settled (11 July, 1742) by a Bull of Benedict XIV")]),
  ("The Catholic Encyclopedia calls it \"a terrible blow to the missions in China\".", [raw('cathen3', "was a terrible blow to the missions in China")]),
  ("The Jesuits had favored tolerance, and the Rites were decided in Rome, not in China.", [raw('cathen3', "Father Ricci, the first su- perior of the Jesuits in China, had remarkable success in his work of evangelizing because of the great tolerance he showed"), rec('§5 G89-AP2 Mark\'s test (decided by Propaganda, the Holy Office and two popes)', 'also CE lines 123062-123086 on decrees of Alexander VII and Clement IX')])],
 [("In 1659 Propaganda sent an instruction to the vicars apostolic of the Society of Foreign Missions.", [lib('COL', "Instr. S. C. de Propag. Fide r659", note='OCR reads r659'), lib('COL', "SoctETATIS MissION. AD EX- TEROS", note='OCR of the addressee line')]),
  ("It asked: \"For what is more absurd than to carry France, Spain, Italy or any other part of Europe into China?\" (our rendering).", [lib('COL', "Quid enim absurdius quam Galliam, Hispaniam, aut Italiam, aut aliam Europae partem in Sinas invehere", rendering="For what is more absurd than to carry France, Spain, Italy or any other part of Europe into China?")]),
  ("In 1658 Rome had named two priests of that Society, Pallu and Lambert de la Motte, vicars apostolic for the missions of China and the neighboring lands.", [raw('launay1', "Propa- gande proposa de nommer M. Pallu et M. de la Motte") if False else raw('launay1', "M. de la Motte Lambert vicaires apostoliques dans les Missions de Chine et les pays voisins"), raw('cathen3', "This was the beginning of the Société des Missions Etrangéres.")])],
 [("In 1723 the governor-general and the viceroy of Fujian asked the emperor to send the Europeans out of the provinces.", [raw('lettres3', "nous la supplions de les faire sortir des provinces", rendering="we beg him to make them leave the provinces"), raw('lettres3', "le 22 de novembre 1723")]),
  ("Europeans at the court could stay.", [raw('lettres3', "permettre auxEuropéens qui sont à la cour d'y rester comme auparavant", note='OCR runs aux and Europeens together')]),
  ("On 16 October 1724 the Jesuit de Mailla wrote from Peking that \"our holy religion is entirely banned in China\" (our rendering).", [raw('lettres3', "A Pékin, ce 16 octobre 1724."), raw('lettres3', "notre sainte religion est entièrement proscrite à la Chine", rendering="our holy religion is entirely banned in China")]),
  ("Churches were pulled down or turned to common uses.", [raw('lettres3', "les églises sont ou démolies, ou des- linées à des usages profanes", rendering="the churches are either demolished or put to profane uses", note='OCR reads des- linées for des- tinées')]),
  ("An official's order of 1723 had complained that girls were kept from marriage and called \"virgins\" (our rendering).", [raw('lettres3', "il y a des jeunes filles qui la suivent, à qui on interdit le mariage, et qu'on leur donne le nom de vierges", rendering="there are young girls who follow it, to whom marriage is forbidden, and who are given the name of virgins")])],
 [("The church went on in the provinces.", [rec('§5 G89-AP2 B2 and Mark\'s test (provincial communities after 1724)')]),
  ("In 1726 Propaganda ruled that Chinese-born priests must swear the same oath as the Europeans.", [lib('COL', "sacerdoti nativi cinesi"), lib('COL', "cocincinenses, tunquinenses etc. teneri emittere iuramentum"), lib('COL', "S. C. de Prop. Fide 4 Oct. 17236", note='OCR reads 17236; the neighboring items are of 7 June 1726 and 22 January 1727')]),
  ("In 1736 an edict of the Ch'ien-lung emperor forbade the preaching of Christian doctrine on pain of death.", [raw('cathen3', "in 1736, an edict of K'ien Lung, son and successor of, Yung Cheng, prohibited the preaching of Christian doctrine under penalty of death")]),
  ("A persecution in Fujian in 1746 killed Bishop Sanz and four Spanish Dominicans.", [raw('cathen3', "a cruel persecution oe out in Fu- kien during which the vicar Apostolic, Bishop Sanz, and four other Spanish Dominicans", note='OCR reads oe for broke')]),
  ("In 1755 Propaganda warned the missionary at Peking for letting Mass be sung in Chinese on feast days.", [lib('COL', "Moneatur missionarius Pekini eo quod in solemnitatibus lingua sinensi Mis- sam celebrari permiserit"), lib('COL', "S. C. de Prop. Fide 7 Jan. 1755")]),
  ("It forbade the practice for the future.", [lib('COL', "quod fieri in posterum omnino prohibetur")]),
  ("In 1766 the Holy Office was told that Christians in China were few and could not avoid their pagan neighbors' tables.", [lib('COL', "Cum christiani (in Sinis), numero pauci"), lib('COL', "S. Cong. S. Officii r5 Decem. 1766", note='OCR reads r5 for 15')]),
  ("It allowed them to eat food set before them, even if offered to idols, outside any temple and with no sign of worship.", [lib('COL', "decernit licitum esse comedere epulas indifferenter appositas, quamvis. idolis oblatas, dummodo non in templo")])],
 [("The nineteenth century began with more edicts.", [raw('cathen3', "A decree was issued Sept., 1811, prescribing a search for foreign preachers.")]),
  ("After a treaty at Whampoa in 1844, the emperor Tao-kwang ordered on 20 February 1846 that the former Christian buildings be restored.", [raw('cathen3', "Brighter days were looked for after the pene of a treaty at Wham-poa (1844) by the French ambassador, Théodose de Lagrené"), raw('cathen3', "In an edict of 20 Feb., 1846, Tao-kwang ordered that the establishments belonging formerly to Chris- tians be restored to their owners")]),
  ("The Treaty of Tientsin in 1858 and the Peking Convention of 1860 gave missions special privileges.", [raw('cathen3', "Special privileges were awarded to missions by Art. XIII of the French Treaty of T'ien-tsin (1858) and Art. VI of the French Peking Convention (1860).")]),
  ("Anger followed.", [raw('cathen3', "Finally came the massacre of T'ien-tsin, 21 June, 1870.")]),
  ("In the 1860s a Holy Office instruction told a vicar apostolic in Yunnan what to do when pagans, angry at the freedom a treaty gave Christians, drew crosses on the roads so that Christians had to step on them.", [lib('COL', "ob libertatem christianae religioni decretam ex publica con- ventione inter Gallorum ac Sinarum imperato- res inita", rendering="because of the freedom decreed for the Christian religion by a public convention made between the emperors of the French and the Chinese"), lib('COL', "ut venerandae Crucis signum pedibus ultro citroque euntium"), lib('COL', "Instr. S. C. S. Officii 1663", note='OCR reads 1663; the page head reads An. C. 1865'), lib('COL', "An. C. 1865")]),
  ("At Tientsin on 21 June 1870, twenty-one people died, among them a Lazarist and a Chinese priest named Hu.", [raw('cathen3', "the Lazarist Father Chevrier and the Cantonese priest Hu"), raw('cathen3', "in all twenty-one persons, were put to death with great barbarity")]),
  ("The Boxer rising of 1900 brought \"sad days for the missions\".", [raw('cathen3', "The Boxer rebellion brought sad days for the missions.")]),
  ("The encyclopedia names five bishops among the dead, Fantosati, Grassi, Fogolla, Guillon and Hamer.", [raw('cathen3', "Fantosati of Northern Hu-nan, Grassi and Fogolla of Shan-si, Italian Franciscans; Guillon, Missions Etran- géres of Manchuria, Hamer (Dutch) of Kan-su (burnt to death)")])],
])
e2['voices'] = [
    "Jean-Alexis de Mailla — a Jesuit at Peking whose letter of 16 October 1724 says the faith was banned",
    "Charles Maigrot — a priest of the Paris Foreign Missions Society and vicar apostolic of Fujian, who condemned the Chinese rites in 1693",
    "The governor-general and viceroy of Fujian — who asked in 1723 that Europeans leave the provinces",
]
e2['legacy'] = text(AP2, 'legacy', [[
    ("The church outlived the edicts.", [rec('§5 G89-AP2 (the church lives on in the twentieth-century entry)')]),
    ("The encyclopedia of 1908 says the Paris Foreign Missions Society's priests were spread over a great part of the Chinese Empire.", [raw('cathen3', "the Missions Etrangéres continued to flourish, and to-day they are spread over a great portion of the Chinese Empire")])]])
e2['documentedStories'] = []
e2['people'] = []
e2['peopleNote'] = text(AP2, 'peopleNote', [[("The Library holds no words of their own from a Chinese Catholic of these years, so no one is shown.", [rec('§5 G89-AP2 B1 (no Chinese-language source found)')])]])
e2['reviewStatus'] = 'AI-checked'

# ===================================================================== AP3
AP3 = 'japans-hidden-christians'
e3 = {}
e3['id'] = AP3
e3['atlasId'] = 'TBD'
e3['era'] = 8
e3['name'] = "Japan's Hidden Christians"
e3['shortName'] = 'Hidden Christians'
e3['informalName'] = 'The Church Without Priests'
e3['dates'] = '1650-1865'
e3['start'] = 1650
e3['end'] = 1865
e3['region'] = 'Japan'
e3['placeLabel'] = 'Japan'
e3['modernCountries'] = [{'country': 'Japan', 'countryId': 'Q17', 'place': 'Japan', 'placeId': 'Q17'}]
e3['regions'] = ['Greater Asia']
e3['lane'] = '5 Latin West & Catholicism'
e3['laneLabel'] = 'Latin West & Catholicism'
e3['laneOrder'] = 5
e3['beyondFloor'] = False
e3['status'] = 'Pre-Survey Candidate'
e3['chip'] = 'psc'
e3['glyph'] = 'psc'
e3['statusWord'] = 'Researched — viable, secondary'
e3['statusDescription'] = text(AP3, 'statusDescription', [[
    ("Tiered Strong (Tier 1) as a gap in the story, but the evidence is thin.", [rec('§5 G89-AP3 Tier 1 and B1 (Adequate)')]),
    ("Its window runs from 1650, where the Kirishitan entry ends, to 17 March 1865, where the next entry begins.", [rec('census VI.13b dates 1549-1650; census VIII.45 dates 1865-1906')]),
    ("The village communities speak only through a French historian of 1896.", [rec('§5 G89-AP3 B1 (Marnas 1896; their own book not found raw)')]),
    ("Not yet reviewed.", [])]])
e3['living'] = False
e3['overlayCurrent'] = False
e3['c2'] = None
e3['sourcing'] = text(AP3, 'sourcing', [[
    ("Adequate, and almost all from one source.", [rec('§5 G89-AP3 B1 (Adequate)')]),
    ("The French historian Francisque Marnas told the story in 1896, from the missionaries' letters.", [raw('marnas1', "M. Petitjean a raconté (1) comment", note='Marnas draws on two letters of Petitjean (footnote lines 21288-21293)')]),
    ("He is an outsider and a Catholic writer.", [rec('§5 G89-AP3 Evidence (pre-1930 study quoting primary letters, French)')]),
    ("The communities' own book, Tenchi hajimari no koto, the Beginning of Heaven and Earth, has not been found in Japanese.", [rec('§5 G89-AP3 B1 (wanted)')])]])
e3['floorNote'] = text(AP3, 'floorNote', [[
    ("No dated statement of belief by the communities has been read.", [rec('§5 G89-AP3 Section A (not assessable on a dated statement)')]),
    ("They are treated as the Kirishitan church carried on in hiding, and that church clears the floor.", [rec('§5 G89-AP3 Section A (world level, A5); ruling G89-26 sub-question (i)')]),
    ("In 1865 the missionaries found the Creed among the prayers they kept, in old Japanese.", [raw('marnas1', "le Pater, Y Ave, le Credo, le Salve Regina", note='OCR Y Ave for the Ave')]),
    ("Whether the later Kakure still hold the creed is a question for the next entry.", [rec('census VIII.45 (Kakure); §5 G89-AP3 Section A')])]])
e3['relationsSummary'] = text(AP3, 'relationsSummary', [[
    ("This row carries on the Kirishitan church that the ban of 1614 drove underground.", [rec('census VI.13b relationsSummary')]),
    ("It ends on 17 March 1865, when villagers at Urakami told Father Petitjean that their hearts were the same as his.", [raw('marnas1', "Notre cœur à nous tous, qui sommes ici, est le même que le vôtre.", rendering="The heart of all of us here is the same as yours.")]),
    ("The next entry takes up the story from that day.", [rec('census VIII.45 dates 1865-1906')]),
    ("The Paris Foreign Missions Society, Marnas wrote, was the body that found them.", [raw('marnas1', "la Société des Missions Etrangères de Paris, née jadis à l'inspiration d'Alexandre de Rhodes, retrouva au Japon les descendants des anciens chrétiens")])]])
e3['why'] = text(AP3, 'why', [[
    ("In 1666, Marnas says, the government at Edo ordered an inquiry in every town and village into the faith of each family.", [raw('marnas1', "ordonnances rendues en 1666 par le gouvernement de Yedo")]),
    ("Once a year every Japanese had to trample a cross or a holy picture.", [raw('marnas1', "une fois par an, tout japonais devrait fouler aux pieds une croix placée sur le sol, ou quelque image de la Vierge et des Saints")]),
    ("When the missionaries returned in 1865, almost every village they met had a chief of prayer and a baptizer.", [raw('marnas1', "Presque partout les chrétiens avaient une organisa- tion identique."), raw('marnas1', "Dans la plupart des villages, il existait deux principaux chefs.")]),
    ("Later studies hold that the hidden believers kept the faith for about 250 years without a priest.", [rec('census VI.13b why ("Later studies hold ...")')])]])
e3['entry'] = None
e3['teaser'] = text(AP3, 'teaser', [[
    ("Japan, 1650 to 1865 — village churches that kept baptism and prayer for more than two centuries under a ban.",
     [raw('marnas1', "Dans la plupart des villages, il existait deux principaux chefs."), rec('census VI.13b why (about 250 years, later studies)')])]])
e3['longDescription'] = text(AP3, 'longDescription', [
 [("In 1614 Japan banned Christianity, and the entry before this one tells how it began.", [rec('census VI.13b relationsSummary (the ban of 1614)')]),
  ("Marnas wrote the history of the church's return in 1896.", [rec('Marnas 1896 title page and approbations, record §5 AP3 Evidence')]),
  ("He says that in 1666 the government at Edo set up an inquiry in every town and village to learn what each family believed.", [raw('marnas1', "ordonnances rendues en 1666 par le gouvernement de Yedo"), raw('marnas1', "pour rechercher la croyance de cha- que famille")]),
  ("Once a year, he adds, every Japanese had to tread on a cross laid on the ground, or on an image of the Virgin and the saints.", [raw('marnas1', "une fois par an, tout japonais devrait fouler aux pieds une croix placée sur le sol, ou quelque image de la Vierge et des Saints")]),
  ("This was the e-fumi, the treading of the image.", [raw('marnas1', "Cette abominable profanation appelée Ye-Fumi"), raw('marnas1', "Foulement de l'image")]),
  ("Marnas says its inventors meant it to expose the surviving Christians or force them to give up the faith.", [raw('marnas1', "faire découvrir les chrétiens survivants,, ou les obliger à apostasier", note='OCR has a double comma')])],
 [("Almost everywhere the hidden Christians kept the same order, Marnas says.", [raw('marnas1', "Presque partout les chrétiens avaient une organisa- tion identique.")]),
  ("Most villages had two chiefs.", [raw('marnas1', "Dans la plupart des villages, il existait deux principaux chefs.")]),
  ("The chief of prayer led the Sunday prayers and went to the dying.", [raw('marnas1', "C'est lui, qui présidait aux prières du dimanche, et se rendait auprès des mourants")]),
  ("The baptizer gave baptism and trained a pupil to take his place.", [raw('marnas1', "il devait avoir auprès de lui un élève baptiseur, appelé à lui succéder") if False else raw('marnas1', "Le second, le baptiseur administrait le sacre- ment de baptême.")]),
  ("Marnas credits these offices, oral teaching and a few kept books and images for the survival of the faith.", [raw('marnas1', "ainsi qu'à la tradition orale des principales véri- tés de la Foi")])],
 [("In 1865 the missionaries studied the written things the villagers had kept.", [raw('marnas1', "Les missionnaires étudièrent avec soin tous les docu- ments qui leur furent soumis")]),
  ("They included prayer books, written baptism formulas and Christian calendars.", [raw('marnas1', "formules écrites de baptême")]),
  ("One treatise, called Contrition, was dated 1603 and written wholly in Japanese.", [raw('marnas1', "Un traité composé, l'an 1603"), raw('marnas1', "Il était entière- ment écrit en japonais")]),
  ("The baptizer Domingo brought it to the missionaries.", [raw('marnas1', "Ce traité avait été ap- porté aux missionnaires par le baptiseur Domingo.")]),
  ("It had escaped a search at Urakami eight years before, when twenty-eight Christians were jailed and most of their books were burned.", [raw('marnas1', "Il avait échappé aux dernières perquisitions faites huit années auparavant à Urakami, alors que vingt-huit chrétiens de la vallée avaient été jetés en prison, et que la plupart de leurs livres, images ou objets de piété avaient été brûlés et confisqués.")])],
 [("On 17 March 1865, about noon, twelve to fifteen people stood at the door of the church of the Twenty-Six Martyrs in Nagasaki.", [raw('marnas1', "Le vendredi, 17 mars, vers midi et demi, un groupe de douze à quinze personnes"), raw('marnas1', "se tenait à l'entrée de l'église des Vingt-Six Martyrs")]),
  ("Three women knelt beside Father Petitjean.", [raw('marnas1', "trois femmes de cinquante à soixante ans viennent s'agenouiller tout près de lui")]),
  ("One said, with her hand on her heart: \"The heart of all of us here is the same as yours\" (our rendering).", [raw('marnas1', "Notre cœur à nous tous, qui sommes ici, est le même que le vôtre.", rendering="The heart of all of us here is the same as yours."), raw('marnas1', "la main sur la poitrine")]),
  ("Then she asked, \"Sancta Maria no gozowa doko?\", \"Where is the image of Holy Mary?\" (our rendering).", [raw('marnas1', "Sancta Maria no gozowa doko ? — Où est l'image de Sainte Marie ?", note='Japanese words in Latin letters, with Marnas\'s French gloss')])],
 [("Within weeks the missionaries counted about 3,800 Christians.", [raw('marnas1', "Cette découverte de 3800 chrétiens")]),
  ("About 1,300 lived at Urakami and 2,500 in the hills and on the nearby islands.", [raw('marnas1', "C'étaient donc 2,500 chrétiens disséminés dans les montagnes et dans les îles voisines, qu'il fallait ajouter désormais à ceux d'Urakami, au nombre d'environ 1.300.")])],
])
e3['voices'] = [
    "Bernard Petitjean — the French priest at Nagasaki who met the Urakami villagers on 17 March 1865",
    "Domingo — a village baptizer who brought the missionaries the treatise Contrition in 1865",
]
e3['legacy'] = text(AP3, 'legacy', [[
    ("The next entry takes up their story on 17 March 1865.", [rec('census VIII.45 dates 1865-1906')]),
    ("Some of the villagers, the Kakure, chose to stay apart from the visible church.", [rec('census VIII.45 longDescription (Kakure "remain separate to this day")')])]])
e3['documentedStories'] = []
e3['people'] = []
e3['peopleNote'] = text(AP3, 'peopleNote', [[("The Library holds no words of their own from the hidden Christians, so no one is shown.", [rec('§5 G89-AP3 B1 (their own book not found in Japanese)')])]])
e3['reviewStatus'] = 'AI-checked'

ENTRIES = [e1, e2, e3]
