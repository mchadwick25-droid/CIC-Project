"""P2-E10a: apply the era 10 gate ruling to the census in place (release 20 -> 21).
Reuses fix-3/apply3.py's edit and structural-op logic (G-8 option a: no redirectTo)."""
import json, re, sys
REPO = '/home/user/CIC-Project'
C = f'{REPO}/cic-website/data/world-census.json'
E = f'{REPO}/Build/Ministry/Features/Atlas-World-Map/Design/StepZero-Eras/CiC_Step0_Era10_V2_0_Proposed_Edits.json'
DATE = '2026-11-08'
c = json.load(open(C)); e = json.load(open(E))
orig = {m['atlasId']: m for m in json.load(open(C))['movements']}
assert c['meta']['release']['number'] == 20
mv = {m['atlasId']: m for m in c['movements'] if m.get('era') == 10}

def get(m, field):
    parts = re.findall(r'[^.\[\]]+|\[\d+\]', field); obj = m
    for p in parts[:-1]: obj = obj[int(p[1:-1])] if p.startswith('[') else obj[p]
    last = parts[-1]; key = int(last[1:-1]) if last.startswith('[') else last
    return obj, key

problems = []; n = ok = nops = opok = 0
# 1. registerEdits, in order, entry by entry
for ent in e['entries']:
    m = mv[ent['atlasId']]
    for ed in ent.get('registerEdits', []):
        n += 1
        obj, key = get(m, ed['field']); s = obj[key]
        cnt = s.count(ed['old'])
        if cnt != 1 or not ed['old']: problems.append(('count', ent['atlasId'], ed['field'], cnt)); continue
        obj[key] = s.replace(ed['old'], ed['new'], 1); ok += 1
touched = {(ent['atlasId'], re.match(r'(\w+\[\d+\])', ed['field']).group(1)) for ent in e['entries']
           for ed in ent.get('registerEdits', []) if re.match(r'\w+\[\d+\]', ed['field'])}
# 2. structuralOps, after every registerEdit
retire = []
for ent in e['entries']:
    a = ent['atlasId']
    for op in ent.get('structuralOps', []):
        nops += 1
        if op['op'] == 'retireEntry':
            rec = dict(op['record'])
            assert rec['id'] == mv[a]['id']
            rec['date'] = DATE
            rt = op.get('redirectTo', {}).get('G-8 (a)')
            assert rt is None
            rec.pop('redirectTo', None)
            retire.append((a, rec)); opok += 1; continue
        assert op['op'] == 'removeItem', op
        f = op['field']; arr = mv[a][f]
        key = {'documentedStories': ('title', 'matchTitle'), 'sources': ('work', 'matchWork')}.get(f)
        if key:
            idx = [i for i, x in enumerate(arr) if x[key[0]] == op[key[1]]]
            oidx = [i for i, x in enumerate(orig[a][f]) if x[key[0]] == op[key[1]]]
        else:
            assert f == 'voices'
            idx = [i for i, x in enumerate(arr) if x == op['matchValue']]
            oidx = [i for i, x in enumerate(orig[a][f]) if x == op['matchValue']]
        if len(idx) != 1: problems.append(('opmatch', a, f, len(idx))); continue
        if (a, f'{f}[{oidx[0]}]') in touched: problems.append(('op-on-edited-item', a, f))
        arr.pop(idx[0]); opok += 1
for a, rec in retire:
    m = mv.pop(a); c['movements'].remove(m); c['retiredMovements'].append(rec)

# 3. dates, start, end, living; 4. livingEvidence (G-51 a)
RX = re.compile(r'^(?:Alive today|Not alive today)\. (.*?) ?(?:Dated evidence|Evidence): (.*) Grade: (.*?)\. '
                r'(?:Uncertain, group (L-\d) \(§2d; G-5\)|(Settled) \(§2d\))\.(?: .*)?$')
# Process wording (record versions, gate and section numbers, conditionals on decisions now made) is
# removed from the evidence text before it enters the live file. Removal only: no word is added.
STRIP = {
    'IX.4': [('evidence', ' in the V1.0 survey')],
    'IX.5': [('basis', ' (R4 safety; the excluded-by-safety class stands)')],
    'IX.10': [('evidence', ' under the §2d rule')],
    'IX.16': [('basis', ' If INC splits out, the three remaining bodies carry this row.'), ('basis', ' (R4)'),
              ('evidence', ' in the V1.0 survey'), ('evidence', '; INC: see the Iglesia ni Cristo draft')],
    'IX.18': [('evidence', ' (instrument gap named in V1.0)')],
    'IX.28': [('basis', " The census routes its continuation to IX.18 and IX.31, and IX.31 is proposed for retirement (G-8). Changing the flag reverses V1.0's 'living:true stands' and needs a change order.")],
    'IX.44': [('evidence', '; removed in V2.0')],
    'IX.49': [('basis', ' (V1.0)'), ('evidence', ' (status as recorded in the V2.0 IX.49 note)')],
    'IX.51': [('basis', ' New row. In the census today INC sits inside IX.16, marked living.')],
}
def evidence(lr, a):
    m = RX.match(lr); assert m, lr
    basis, ev, grade, grp, settled = m.groups()
    out = {'basis': basis, 'evidence': ev, 'grade': grade, 'group': grp or 'settled'}
    for f, cut in STRIP.get(a, []):
        assert out[f].count(cut) == 1, (a, f, cut)
        out[f] = out[f].replace(cut, '', 1)
    return out
nfields = 0
for ent in e['entries']:
    a = ent['atlasId']
    if a not in mv: continue
    m = mv[a]
    for k in ('dates', 'start', 'end', 'living'):
        if m[k] != ent[k]: nfields += 1
        m[k] = ent[k]
    m['livingEvidence'] = evidence(ent['livingReason'], a)

# 5. G-14: Iglesia ni Cristo, split from IX.16, atlasId IX.51
d = e['newEntries'][0]; assert d['id'] == 'iglesia-ni-cristo'
x16 = mv['IX.16']
assert all(m['atlasId'] != 'IX.51' for m in c['movements'])
inc = {}
ORDER = list(x16.keys())  # same key order as the other era 10 rows
src = {k: v for k, v in d.items() if not k.startswith('_')}
src['atlasId'] = 'IX.51'
borrowed = {
    'placeLabel': 'Philippines',
    'modernCountries': [x for x in x16['modernCountries'] if x['place'] == 'Philippines'],
    'regions': ['Greater Asia'],
    'sources': [x16['sources'][0], x16['sources'][5]],
    'longDescription': d['why'],
    'teaser': 'The Philippines, from 1914 — Iglesia ni Cristo, assessed on its own published texts.',
    'voices': x16['voices'][0:2],
    'legacy': ('Iglesia ni Cristo was still active in 2010. It had passed through two successions, in 1963 and 2009. '
               "Its own counts ran to millions, and it was the largest church founded in the Philippines. "
               'No independent count is cited here.'),
    'documentedStories': [],
}
assert x16['sources'][0]['work'].startswith('Iglesia ni Cristo:') and x16['sources'][5]['work'] == 'CHC vol. 9'
assert all(v.startswith(('Felix Y. Manalo', 'Pasugo')) for v in borrowed['voices'])
for k in ORDER:
    if k in src: inc[k] = src[k]
    elif k in borrowed: inc[k] = borrowed[k]
    elif k == 'livingEvidence': inc[k] = evidence(d['_draft']['livingReason'], 'IX.51')
    else: problems.append(('inc-missing', k))
extra = set(src) - set(inc); assert not extra, extra
c['movements'].append(inc)

# 6. G-1: eras[9]
era = c['eras'][9]; assert era['num'] == 10
era['dates'] = '1906-c. 2010'
era['tag'] = 'A century of global Christianity'
era['stepStatus'] = 'Step 0 run complete — era frozen'
era['keyEvents'] = ['Azusa Street Revival (1906) and Edinburgh Missionary Conference (1910)', 'Second Vatican Council (1962–65)']

# 7. meta
c['meta']['totalEntries'] = len(c['movements'])
sc = {}
for m in c['movements']: sc[m['status']] = sc.get(m['status'], 0) + 1
c['meta']['statusCounts'] = {k: sc[k] for k in c['meta']['statusCounts'] if k in sc} | {k: v for k, v in sc.items() if k not in c['meta']['statusCounts']}
c['meta']['liveCount'] = sum(1 for m in c['movements'] if m['status'] == 'Built & Live')
c['meta']['release'] = {'number': 21, 'date': DATE}

print('registerEdits', n, 'applied', ok, '| structuralOps', nops, 'matched', opok, '| date/living field changes', nfields)
print('problems', problems)
open(C, 'w', encoding='utf-8').write(json.dumps(c, indent=1, ensure_ascii=False) + '\n')
