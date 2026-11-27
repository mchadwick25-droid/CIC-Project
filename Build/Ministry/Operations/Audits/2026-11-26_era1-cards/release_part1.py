"""Era 1 cards, release part 1: write the checked card fields into the census."""
import json, re
P = 'cic-website/data/world-census.json'
F = 'Build/Ministry/Operations/Audits/2026-11-26_era1-cards/'
raw = open(P).read()
d = json.loads(raw)
M = {m['id']: m for m in d['movements']}
TRAD = ['montanism-the-new-prophecy', 'alexandria-catechetical', 'post-apostolic-house-church', 'syriac-edessa-nisibis',
        'latin-pastoral-congregational-christianity', 'greek-apologists-second-century', 'latin-apologists',
        'apocryphal-and-pseudepigraphal-literature', 'marcion-marcionism', 'valentinian-and-other-gnostic-christianities',
        'manichaeism', 'ebionite-nazoraean-current', 'novatianism', 'anatolian-church-third-century']
LAY = ['shortDescription', 'briefSources', 'timeline', 'uncertain', 'quotationOriginals']
ev = json.load(open(F + 'Evidence.json'))
for t in TRAD:
    L = json.load(open(F + t + '.layout.json'))
    m = M[t]
    for k in LAY:
        if k in L: m[k] = L[k]
    if 'dates' in L: m['dates'] = L['dates']
M['alexandria-catechetical']['dates'] = ev['alexandria-catechetical']['dates']['shown']
for cid, home in (('polycarp-of-smyrna', 'card'), ('councils-of-rome-and-carthage-251', 'council')):
    L = json.load(open(F + cid + '.layout.json'))
    for k in LAY:
        if k in L: M[cid][home][k] = L[k]
M['polycarp-of-smyrna']['dates'] = ev['polycarp-of-smyrna']['dates']['shown']
M['polycarp-of-smyrna']['card']['datesNote'] = ev['polycarp-of-smyrna']['dates']['datesNote']
E = json.load(open(F + 'era-1.layout.json'))
era = [e for e in d['eras'] if e.get('num') == 1][0]
for k in ('shortDescription', 'timeline', 'uncertain'): era[k] = E[k]
a = M['alexandria-catechetical']['livingEvidence']
a['basis'] = a['basis'].replace('The world built from this entry names', 'The Church in Conversation Tradition built from this entry names')
M['desert-monasticism']['sourcing'] = M['desert-monasticism']['sourcing'].replace("the next richest built world's 37", "the next richest Church in Conversation Tradition's 37")
ind = 1 if raw.startswith('{\n ') and not raw.startswith('{\n  ') else 2
open(P, 'w').write(json.dumps(d, ensure_ascii=False, indent=ind) + '\n')
print('written', len(TRAD), 'traditions, 1 person, 1 council, era 1')
