from make import *
import json

# ------------------------------------------------------------------ links
LINKS = []
def link(frm, to, typ, conf, note, sources, spec, ver, ruling, outcome=None, wants=None, flags=None):
    d = {'id': f'{frm}--{to}', 'from': frm, 'to': to, 'type': typ, 'confidence': conf, 'note': note}
    if outcome: d['outcome'] = outcome
    d['sources'] = sources
    d['citation_specificity'] = spec
    d['verification_state'] = ver
    d['ruling'] = ruling
    if wants: d['wants'] = wants
    if flags: d['drafter_flags'] = flags
    LINKS.append(d)

VI18 = 'st-thomas-christians-under-portuguese-pressure-d'
VIII27 = 'northeast-india-revivals-and-the-mar-thoma-refor'
ME1 = 'church-of-the-east-three-patriarchates'
VI13B = 'kirishitan-japan'
VIII45 = 'japanese-christianity-hidden-emergence-meiji'
VI13C = 'china-mission-born-christianity'
IX65 = 'chinese-catholicism-twentieth-century'

# L1 VI.18 -> AP1 continued as
link(VI18, AP1, 'continued as', 'Documented',
     "The Angamaly document of 1787 calls the men who swore the oath at Mattancherry \"our forefathers\". The community's own history says Mar Thomas the Great was consecrated in 1665. An English chaplain adds that he was the archdeacon who had headed the revolt from Rome.",
     [lsrc_lib('primary', APPE, 'WH', "Upon this our forefathers assembled at Muttan- cherry, and took an oath that neither they themselves, nor their descendants, should ever have anything to do with the Paulists.", 'Appendix E'),
      lsrc_lib('primary', APPD, 'WH', "By the laying on of his hands, Mar Thomas the Great, was lawfully consecrated", 'Appendix D, entry for 1665'),
      lsrc_lib('secondary', WHW + ', chapter on the Dutch conquest and the Carmelite mission', 'WH', "the Archdeacon who had headed the revolt from Rome", 'narrative, the arrival of Mar Gregorius')],
     'A', 'verified-direct', 'G89-24 (a)')

# L2 AP1 -> VIII.27 gave rise to
link(AP1, VIII27, 'gave rise to', 'Widely Accepted',
     "The Mar Thoma reform of 1836 grew inside the Malankara party. In 1847 the Patriarch of Antioch wrote that his predecessor had sent a bishop to keep \"all the flock of Mar Thomas\" from the reforming bishop Matthew. The hill churches of the northeast are not part of this line.",
     [lsrc_lib('primary', "Ignatius Jacob II, Patriarch of Antioch, letter of 29 May 1847, on the earlier Patriarch Elias sending Mar Koorillos, in Edavalikel Philipos, The Syrian Christians of Malabar, ed. G. B. Howard (1869)", 'PHI',
               "And he sent him to India hour before hour, that he might expel the reprobate Matthew, and keep from him all the flock of Mar Thomas,", 'The Patriarch\'s Letter (May, 1847)'),
      {'kind': 'secondary', 'work': 'Robert Eric Frykenberg, Christianity in India: From Beginnings to the Present (Oxford University Press, 2008)'}],
     'B', 'verified-direct', 'G89-24 (a)',
     wants=['A source in which the reformers or their opponents place the reform inside the Malankara party by name, for a Documented grade'],
     flags=['The reform-party reading rests on the 1847 letter plus the repo-cited Frykenberg (2008), named and not rechecked in this run. The existing link from VI.18 to VIII.27 (gave rise to, Widely Accepted) is left in place; it now skips this row.'])

# L3 ME-1 <-> AP1 in contact with (Mar Gabriel, 1708)
link(ME1, AP1, 'in contact with', 'Documented',
     "In 1708, the community's own history says, a bishop called Gabriel arrived \"by the direction of Mar Alea\". The text names him a Nestorian bishop. Some Syrians and some Roman Catholics joined him.",
     [lsrc_lib('primary', APPD, 'WH', "In 1708, by the direction of Mar Alea, Gabriel, a Nestorian bishop, arrived.", 'Appendix D, entry for 1708'),
      lsrc_lib('primary', APPD, 'WH', "Some Syrians and also Roman Catholics joined him.", 'Appendix D, entry for 1708'),
      lsrc_lib('secondary', APPB, 'WH', "GaxsRIkL, a Nestorian Bishop arrived 1708. He died at Cottayam, 1731.", 'Appendix B')],
     'A', 'verified-direct', 'G89-24 (a); G89-43 (a)',
     outcome="A bishop sent from the Church of the East reached Malabar in 1708. Those who joined him went back to their former parties after his death.",
     flags=['The pair is a link to a new row of another slice (ME1). The note reads the text\'s "Nestorian" as the Church of the East; the ME-1 note should name the same 1708 event. The outcome rests on App. D lines 19251-19253 ("After he died, no such bishop came into Malabar. Those who joined him returned to their former parties after his death.").'])
LINKS[-1]['sources'].insert(2, lsrc_lib('primary', APPD, 'WH', "Those who joined him returned to their former parties after his death.", 'Appendix D, entry for 1708'))

# L4 VI.13b -> AP3 continued as
link(VI13B, AP3, 'continued as', 'Widely Accepted',
     "A Franciscan report of the 1620s says that most missionaries stayed in hiding after the ban of 1614 and kept the faith alive. Marnas wrote in 1896 that in 1865 the Paris Foreign Missions Society found the descendants of the old Christians. No text from the years between was read.",
     [lsrc_lib('primary', "Luis Sotelo, O.F.M., memorial (Latin, after 1622), in Léon Pagès, Histoire de la religion chrétienne au Japon, seconde partie: Annexes (1870)", 'PAG', "diversis in locis occultati", "annex, running head 'Mémorial Sotelo'"),
      lsrc_lib('primary', "Luis Sotelo, O.F.M., memorial (Latin, after 1622), in Léon Pagès, Histoire de la religion chrétienne au Japon, seconde partie: Annexes (1870)", 'PAG', "quorum labore, doctrina et exemplo fides in multis fidelibus egerrima conservatur", "annex, running head 'Mémorial Sotelo'"),
      lsrc_raw('secondary', "Francisque Marnas, La \"Religion de Jésus\" (Iaso ja-kyō) ressuscitée au Japon, vol. 1 (Paris and Lyon, 1896)", 'marnas1',
               "la Société des Missions Etrangères de Paris, née jadis à l'inspiration d'Alexandre de Rhodes, retrouva au Japon les descendants des anciens chrétiens", 'Livre préliminaire, before the Sidotti chapter'),
      {'kind': 'secondary', 'work': 'Stephen Turnbull, The Kakure Kirishitan of Japan: A Study of Their Development, Beliefs and Rituals to the Present Day (Richmond, 1998)'},
      {'kind': 'secondary', 'work': "Christal Whelan, trans., The Beginning of Heaven and Earth: The Sacred Book of Japan's Hidden Christians (Honolulu, 1996), introduction"}],
     'A', 'verified-online', 'G89-26 (a), sub-question (i)',
     flags=['The primary source covers 1614 to the 1620s only; nothing dated between 1650 and 1865 was read. The grade follows the same reading as the existing link from VI.13b to VIII.45 (Inferential-Thin), raised because Marnas (1896) names the 1865 communities descendants of the old Christians and because the 1603 treatise survived in their villages. Turnbull and Whelan are repo-cited and named, not rechecked.'])

# L5 AP3 -> VIII.45 continued as
link(AP3, VIII45, 'continued as', 'Widely Accepted',
     "On 17 March 1865 three women at Nagasaki told Father Petitjean, \"The heart of all of us here is the same as yours\" (our rendering). Marnas says the missionaries then found chiefs of prayer and baptizers in the villages. He credits those offices, and oral teaching, for the survival of the faith.",
     [lsrc_raw('primary', "Bernard Petitjean, letters of 18 and 22 March 1865, as told in Marnas, La \"Religion de Jésus\" ressuscitée au Japon, vol. 1 (1896)", 'marnas1',
               "Notre cœur à nous tous, qui sommes ici, est le même que le vôtre.", 'Marnas I, chap. on the discovery of the Christians, 17 March 1865'),
      lsrc_raw('secondary', "Francisque Marnas, La \"Religion de Jésus\" (Iaso ja-kyō) ressuscitée au Japon, vol. 1 (Paris and Lyon, 1896)", 'marnas1',
               "ainsi qu'à la tradition orale des principales véri- tés de la Foi", 'Marnas I, the village offices'),
      {'kind': 'secondary', 'work': 'Stephen Turnbull, The Kakure Kirishitan of Japan: A Study of Their Development, Beliefs and Rituals to the Present Day (Richmond, 1998)'}],
     'A', 'verified-online', 'G89-26 (a), sub-question (i)',
     flags=['The existing link from VI.13b to VIII.45 (gave rise to, Inferential-Thin) is left in place; it now skips this row. The brief retires only "continued as" links, so no retirement is drafted.'])

# L6 VI.13c -> AP2 continued as
link(VI13C, AP2, 'continued as', 'Widely Accepted',
     "In 1656 the Holy Office answered questions that missionaries in China had sent to Rome in 1645. The Catholic Encyclopedia of 1908 tells the Ming mission, the Rites quarrel and the later church as one story. No text says in so many words that one church became the other.",
     [lsrc_lib('primary', "Collectanea S. Congregationis de Propaganda Fide, vol. I (Rome, 1907), decree of the Holy Office, 23 March 1656", 'COL',
               "Ab aliquibus in regno Sinarum missionariis pro- posita fuerunt, anno 1645, Sacrae Congrega- tioni de Propaganda Fide infrascripta et alia quamplurima quaesita", 'Holy Office, 23 March 1656'),
      lsrc_raw('secondary', "The Catholic Encyclopedia, vol. 3 (New York, 1908), article 'China'", 'cathen3',
               "Father Ricci, the first su- perior of the Jesuits in China, had remarkable success in his work of evangelizing because of the great tolerance he showed", "article 'China', The Question of Rites")],
     'A', 'verified-online', 'G89-23 (a)',
     flags=['This link is not on the record\'s named list. It is drafted because the row\'s own text says it carries on the Ming-era church. VI.13c\'s continuesAs is not set here (VI.13c is not on this slice\'s list of rows to edit); the coordinator can add it.'])

# L7 AP2 -> IX.65 continued as
link(AP2, IX65, 'continued as', 'Inferential-Thin',
     "The Catholic Encyclopedia of 1908 describes Catholic missions of many societies spread over the Chinese Empire. The twentieth-century entry takes up the same church from 1906. This rests on one early account.",
     [lsrc_raw('secondary', "The Catholic Encyclopedia, vol. 3 (New York, 1908), article 'China'", 'cathen3',
               "the Missions Etrangéres continued to flourish, and to-day they are spread over a great portion of the Chinese Empire", "article 'China', the Paris Foreign Missions Society")],
     'A', 'verified-online', 'G89-23 (a)',
     flags=['No continuesAs is set on the new row: it is an era 8 row and IX.65 is era 10, so the validator\'s adjacent-era rule would fail. The link stands without the field. Evidence for the 1906 hand-over itself was not found; the grade is the honest one.'])

# ------------------------------------------------------------------ neighbor changes
WH45 = "On 17 March 1865, weeks after a French church opened in Nagasaki's foreign settlement"
NC = []
# VI.18 and VI.13b: continuesAs
NC.append({'id': VI18, 'set': {'continuesAs': AP1}, 'ruling': 'G89-24 (a)',
           'reason': "The new row for 1665 to 1815 sits between VI.18 (to 1665) and VIII.27 (from 1836); VI.18 continues as it, as the new link says."})
NC.append({'id': VI13B, 'set': {'continuesAs': AP3}, 'ruling': 'G89-26 (a), sub-question (i)',
           'reason': "The hidden centuries are VI.13b's church carried on (the A5 reading, Mark's ruling), so VI.13b continues as the new row, which continues as VIII.45."})

# VIII.45 and VIII.21: MEP lines (whole new longDescription)
import copy
census = json.load(open(ROOT + '/cic-website/data/world-census.json'))
M = {m['id']: m for m in census['movements']}
old45 = M[VIII45]['longDescription']
old21 = M['korean-catholic-origins']['longDescription']
add45 = text(VIII45, 'longDescription', [[
    ("The priests who met them belonged to the Paris Foreign Missions Society.", [raw('marnas1', "Messieurs les- directeurs du Séminaire de Paris") if False else raw('marnas1', "la Société des Missions Etrangères de Paris, née jadis à l'inspiration d'Alexandre de Rhodes, retrouva au Japon les descendants des anciens chrétiens")]),
    ("The historian Marnas wrote in 1896 that this Society, \"born long ago of the inspiration of Alexandre de Rhodes\", found the descendants of the old Christians in 1865 (our rendering).", [raw('marnas1', "la Société des Missions Etrangères de Paris, née jadis à l'inspiration d'Alexandre de Rhodes, retrouva au Japon les descendants des anciens chrétiens", rendering="the Society of Foreign Missions of Paris, born long ago of the inspiration of Alexandre de Rhodes, found again in Japan the descendants of the old Christians")])]])
NC.append({'id': VIII45, 'set': {'longDescription': old45 + '\n\n' + add45}, 'ruling': 'G89-2 (a)',
           'reason': 'MEP is named as a carrier in the row that tells the 1865 meeting; Petitjean wrote to the superior of the Paris Seminary (Marnas, lines 22193-22194), and Marnas names the Society as the finder. No MEP row is made.'})
add21 = text('korean-catholic-origins', 'longDescription', [[
    ("The Paris Foreign Missions Society had an establishment in Korea.", [raw('cathen3', "Of the flourishing establishment of the Missions Etran- géres de Paris, there were left only Fathers Ridel, later on vicar Apostolic, Féron, and Calais.")]),
    ("In the persecution of 1866, the Catholic Encyclopedia says, two bishops and seven priests were beheaded.", [raw('cathen3', "Bishop Ber- neux, with Fathers de Breteniéres, Beaulieu, and Dorie (8 March), Pourthié and Petitnicolas (11 March), the coadjutor Bishop Daveluy, and Fathers Aumaitre and Huin (30 March) were all decapitated.")]),
    ("Of the Society's flourishing establishment, only Fathers Ridel, Féron and Calais were left.", [raw('cathen3', "Of the flourishing establishment of the Missions Etran- géres de Paris, there were left only Fathers Ridel, later on vicar Apostolic, Féron, and Calais.")])]])
NC.append({'id': 'korean-catholic-origins', 'set': {'longDescription': old21 + '\n\n' + add21}, 'ruling': 'G89-2 (a)',
           'reason': 'MEP is named as a carrier in the row that tells the Korean church under persecution, on the Catholic Encyclopedia of 1908 (opened raw). Only the 1866 facts the article states are used.'})

# ------------------------------------------------------------------ holds
HOLDS = [
 {'item': 'AP7: the Catholic St Thomas Christians and the Chaldean Syrian body at Thrissur, 1815-1906; then extend the AP1 row to 1906; a link to VIII.40 for the Chaldean bishops sent to Thrissur in 1861 and 1874', 'g89': 'G89-29 (c), then (a)',
  'reason': 'The record holds it: it rests on two pre-1930 Protestant studies opened raw (Richards 1908; Rae 1892, passage not located), and no Catholic or Malayalam source was opened. The Chaldean bishops of 1861 and 1874, the vicariates of 1887 and Chavara are [S].',
  'waits_for': 'One Catholic or Malayalam source for the Catholic half of the community in era 9 (for example Chavara\'s own writings, or Syro-Malabar sources). Then AP1 is extended to 1906 and the AP7 link to VIII.40 is drafted.'},
 {'item': 'AP11: the Russian Ecclesiastical Mission in Peking and the Albazinians, 1685/1715-1906; then a line in VIII.31', 'g89': 'G89-36 (b)',
  'reason': 'The record opened no source for it this run; Widmer 1976 was searched on archive.org and not found, and is [S].',
  'waits_for': 'A source on the Peking mission and the Albazinians (Widmer, The Russian Ecclesiastical Mission in Peking during the Eighteenth Century, Harvard 1976, or a pre-1930 work). Then a line in VIII.31 (ME-18 also routes Peking to Asia; the rivers pass finds this consistent).'},
 {'item': 'AP15: Korea 1884/1886-1906, the Protestant beginnings and the Catholic years after toleration; then named lines (Catholic: the end of VIII.21; Protestant: VIII.7)', 'g89': 'G89-34 (b)',
  'reason': 'No source was opened this run. VIII.21 ends at 1886 and says Protestant missionaries came in 1884; IX.64 opens at 1907 and IX.2 at 1904.',
  'waits_for': 'Dated primary sources for the Protestant congregations (the Ross translation, the Nevius plan) and for the Catholic church after 1886.'},
 {'item': 'AP1 in era 9 (1815-1906) beyond the Malankara party', 'g89': 'G89-29 (c)', 'reason': 'Same as AP7 above: the Catholic party after 1815 has no source read.',
  'waits_for': 'See AP7.'},
]
# drop the redundant fourth hold (kept in AP7)
HOLDS = HOLDS[:3]

WANTS = [
 "Paremmakkal Thoma Kathanar, Varthamanappusthakam (Malayalam, c. 1790): the Catholic party's own voice for AP1; no pre-1930 printing found.",
 "Malayalam originals of the abstract of the Malankara party's history (Whitehouse App. D) and of the Angamaly document of 1787 (App. E): the Library holds English only, from 1873.",
 "Raulin 1745 and Sebastiani 1666 and 1672 (in the Library) were not read for AP1's window; the fuller Library check is open.",
 "Huang Bolu (黃伯祿), 正教奉褒 Zhengjiao fengbao (Shanghai, 1883); the Chinese text of the 1692 edict and of the 1723 memorial: for AP2, a Chinese voice. None found raw.",
 "Tenchi hajimari no koto (天地始之事), the hidden Christians' own text, in Japanese: for AP3 and its Section A.",
 "Urakawa Wasaburō, Kirishitan no fukkatsu (1927-28), and a Japanese source for the village communities: for AP3.",
 "Eric Widmer, The Russian Ecclesiastical Mission in Peking during the Eighteenth Century (Harvard, 1976): for AP11.",
]
