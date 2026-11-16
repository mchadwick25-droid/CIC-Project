# Era 1 into the census (data release N). Re-runnable: run from repo root after any rebase.
import json, glob, os, re, sys, unicodedata
REL = int(sys.argv[1]); DATE = sys.argv[2]
B = 'Build/Ministry/Features/Church-Family-Tree/'
CEN = 'cic-website/data/world-census.json'
REC = 'Build/Ministry/Operations/Audits/2026-11-16_era1-standard-v1/renderings/comparison.md'
d = json.load(open(CEN)); m = {x['id']: x for x in d['movements']}
def fold(s): s=unicodedata.normalize('NFKD',s); s=''.join(c for c in s if not unicodedata.combining(c)).lower().replace('æ','ae').replace('œ','oe'); return ' '.join(re.sub(r'[^a-z0-9]+',' ',s).split())
MAP = [('otherNames','otherNames'),('label','label'),('knownFor','knownFor'),('dates','datesNote'),('place','placeNote'),('role','role'),('keyWorks','keyWorks'),('legacy','legacy'),('uncertain','uncertain'),('sources','sources'),('briefReferences','briefReferences'),('quotationOriginals','quotationOriginals')]
rend = json.load(open('tools/quote_renderings.json'))
ids = []
for bf in sorted(glob.glob(B+'Who-Profiles/era1/batch*/*.brief.txt')):
    i = os.path.basename(bf)[:-10]; ids.append(i)
    c = json.load(open(bf[:-10]+'.card.json')); x = m[i]
    x['longDescription'] = open(bf).read().strip()
    card = {}
    for a, b in MAP:
        if c.get(a) not in (None, [], {}, ''): card[b] = c[a]
    x['card'] = card
cid = 'councils-of-rome-and-carthage-251'; ids.append(cid)
e = json.load(open(B+'Council-Profiles/era1/'+cid+'.entry.json')); x = m[cid]
x['longDescription'] = open(B+'Council-Profiles/era1/'+cid+'.brief.txt').read().strip()
for k in list(x['council'].keys()) + [k for k in e if k in ('rivers','knownFor','datesNote','issue','calledBy','attended','decided','outcome','record','traditions','uncertain','sources') and k not in x['council']]:
    if k in e: x['council'][k] = e[k]
if 'people' in e: x['people'] = [({'person': q['id'], 'part': q['part']} if q.get('id') else {k: q[k] for k in ('name','verdict','part')}) for q in e['people']]
# renderings: every brief quotation whose words are ours (differ from the printed wording)
rend['renderings'] = [r for r in rend['renderings'] if r['id'] not in ids]
for i in ids:
    x = m[i]; qo = (x.get('card') or {}).get('quotationOriginals') or []
    if i == cid:
        qo = json.load(open('Build/Ministry/Operations/Audits/2026-11-16_era1-standard-v1/build-scripts/council_qo.json'))
    for q in qo:
        if fold(q['modern']) != fold(q['printed']):
            rend['renderings'].append({'id': i, 'quote': q['modern'], 'original': {'file': q['file'], 'lines': q['lines'], 'language': 'English'}, 'second_reading': {'record': REC, 'verdict': q['secondReading']}})
d['meta']['release'] = {'number': REL, 'date': DATE}
json.dump(d, open(CEN, 'w'), indent=1); open(CEN, 'a').write('\n')
json.dump(rend, open('tools/quote_renderings.json', 'w'), indent=1, ensure_ascii=False); open('tools/quote_renderings.json', 'a').write('\n')
print('updated', len(ids), 'entries')
# Bardaisan tradition card: the baptism told through its one late witness (coordinator, under Mark's presentation rulings)
d = json.load(open(CEN)); m = {x['id']: x for x in d['movements']}; t = m['bardaisanite-current']
R = {'floorNote': [("But he was a baptized member of the Edessene church who wrote against Marcion, and how far", "But he wrote against Marcion, and Michael the Syrian, writing in the 12th century, says he was baptized in the Edessene church. How far")],
     'why': [("was a courtier, philosopher, and baptized member of the Edessene church who wrote against Marcion and argued that human freedom is real against the fatalism of the astrologers.", "was a courtier and philosopher who wrote against Marcion and argued that human freedom is real against the fatalism of the astrologers. Michael the Syrian, writing in the 12th century, says he was baptized in the Edessene church.")],
     'longDescription': [("He wrote against Marcion, and he was baptized in the Edessene church.", "He wrote against Marcion. Michael the Syrian, writing in the 12th century, says he was baptized in the Edessene church.")]}
for k, rs in R.items():
    for a, b in rs:
        if a in t[k]: t[k] = t[k].replace(a, b)
        elif b not in t[k]: raise SystemExit('bardaisan text changed: ' + k)
json.dump(d, open(CEN, 'w'), indent=1); open(CEN, 'a').write('\n')
print('bardaisan tradition card attributed')
