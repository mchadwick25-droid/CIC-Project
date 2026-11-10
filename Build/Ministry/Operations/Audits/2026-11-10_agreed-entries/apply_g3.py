"""P2-G3 apply: merge the reviewed drafts into the census as one data release.
Usage (repo root): python3 -I apply_g3.py <census in> <census out> <release number> <date> <decisions.json>
decisions.json: {"exclude_source_classes": [...], "carthusian_option": "a"|"b", "rows_fixes": {...}}
"""
import json, sys, re, collections, os
G3 = os.path.dirname(os.path.abspath(__file__))
cin, cout, REL, DATE, decf = sys.argv[1:6]
dec = json.load(open(decf))
c = json.load(open(cin))
M = {m['id']: m for m in c['movements']}
E = {e['id']: e for e in c['edges']}
log = collections.defaultdict(list)

def draft(d):
    if d == 'D2' and dec.get('carthusian_option') == 'a':
        return json.load(open(f'{G3}/D2/Draft_optionA.json'))
    return json.load(open(f'{G3}/{d}/Draft.json'))

PREFIX = {1: 'I', 2: 'I', 3: 'II', 4: 'III', 5: 'IV', 6: 'V', 7: 'VI', 8: 'VII', 9: 'VIII', 10: 'IX'}
nextnum = collections.Counter()
for m in c['movements']:
    p, _, n = m['atlasId'].partition('.')
    k = int(re.match(r'\d+', n).group()) if re.match(r'\d+', n) else 0
    nextnum[p] = max(nextnum[p], k)

EDGE_KEYS = {'id','from','to','type','confidence','note','sources','citation_specificity','verification_state','outcome','concerns'}
new_ids = []
for d in ['D1', 'D2', 'D3', 'D4', 'P1', 'P2', 'P3']:
    x = draft(d)
    for e in x.get('entries', []):
        assert e['id'] not in M, e['id']
        assert e['id'] not in {r['id'] for r in c['retiredMovements']}, e['id']
        p = PREFIX[e['era']]; nextnum[p] += 1
        e['atlasId'] = f'{p}.{nextnum[p]}'
        e.setdefault('reviewStatus', 'AI-checked')
        if e.get('kind') != 'person': e.setdefault('people', [])
        c['movements'].append(e); M[e['id']] = e; new_ids.append(e['id']); log['entries'].append((d, e['id'], e['atlasId']))
    for n in x.get('neighbor_changes', []):
        if n.get('kind') == 'edge':
            for k, v in n['set'].items(): E[n['id']][k] = v
            log['edge_edits'].append((d, n['id'])); continue
        m = M[n['id']]
        for k, v in n['set'].items(): m[k] = v
        log['neighbor'].append((d, n['id'], sorted(n['set'])))
    for r in x.get('retire_links', []):
        assert r['id'] in E, r['id']
        c['edges'] = [e for e in c['edges'] if e['id'] != r['id']]; del E[r['id']]
        rec = {'id': r['id'], 'date': DATE, 'reason': r['reason']}
        if r.get('replacedBy'): rec['replacedBy'] = r['replacedBy']
        c['retiredLinks'].append(rec); log['retired'].append(r['id'])
    for l in x.get('links', []):
        l = {k: v for k, v in l.items() if k in EDGE_KEYS}
        if l['id'] in E:  # a rewrite of an existing link, same ID
            E[l['id']].clear(); E[l['id']].update(l); log['rewritten'].append(l['id'])
        else:
            c['edges'].append(l); E[l['id']] = l; log['links'].append(l['id'])
    for u in x.get('retired_link_updates', []):
        r = next(r for r in c['retiredLinks'] if r['id'] == u['id']); r['replacedBy'] = u['replacedBy']
    for ce in x.get('concerns', []):
        e = E[ce['link_id']]
        if e.get('concerns') and e['concerns'] != ce['concerns']:
            log['concerns_conflict'].append((ce['link_id'], e['concerns'], ce['concerns'])); continue
        e['concerns'] = ce['concerns']
        if ce.get('note_edit'): e['note'] = ce['note_edit']
        log['concerns'].append(ce['link_id'])
for ce in dec.get('concerns_override', []):
    E[ce['link_id']]['concerns'] = ce['concerns']

for fo in dec.get('field_overrides', []):
    tgt = E[fo['id']] if fo.get('kind') == 'edge' else M.get(fo['id'])
    if tgt is None: log['override_missing'].append(fo['id']); continue
    for k, v in fo['set'].items(): tgt[k] = v
    log['overrides'].append((fo['id'], sorted(fo['set']), fo['reason']))

def _sub(o, old, new):
    if isinstance(o, str): return o.replace(old, new)
    if isinstance(o, list): return [_sub(x, old, new) for x in o]
    if isinstance(o, dict): return {k: (v if k == 'quote' else _sub(v, old, new)) for k, v in o.items()}
    return o
for tf in dec.get('text_fixes', []):
    m = M[tf['id']]; before = json.dumps(m, ensure_ascii=False)
    for k in list(m): m[k] = _sub(m[k], tf['old'], tf['new'])
    assert json.dumps(m, ensure_ascii=False) != before, tf
    log['text_fixes'].append((tf['id'], tf['old'], tf['new']))

# people rows
excl = set(dec.get('exclude_source_classes', []))
cls = {}
for x in json.load(open(f'{G3}/REV-R/Review_Round1.json')).get('classification', []):
    if isinstance(x, dict): cls[(x['movement'], x['name'])] = x['kind_of_source']
drop = {(d['movement'], d['name']) for d in dec.get('rows_drop', [])}
for k, v in dec.get('class_extra', {}).items(): cls[tuple(k.split('|', 1))] = v
rows, notes = {}, {}
for b in ['R12', 'R36', 'R78', 'R910', 'RNEW']:
    f = f'{G3}/{b}/rows.json'
    if not os.path.exists(f): continue
    r = json.load(open(f))
    for mid, items in r['rows'].items():
        keep = []
        for i in items:
            if 'person' in i: keep.append({'person': i['person']}); continue
            k = (mid, i['name'])
            if k in drop or cls.get(k) in excl or (('held' in i) and dec.get('held_class', {}).get(f'{mid}|{i["name"]}') in excl): log['row_dropped'].append(k); continue
            keep.append(i)
        rows[mid] = keep
    notes.update(r.get('empty_reasons', {}))
for rp in dec.get('rows_patch', []):
    for i in rows.get(rp['movement'], []):
        if i.get('name') == rp['name']:
            for k in rp.get('unset', []): i.pop(k, None)
            i.update(rp['set']); log['row_patched'].append((rp['movement'], rp['name']))
for a in dec.get('rows_add', []):
    rows.setdefault(a['movement'], []).append(a['item'])
for mid, why in dec.get('notes_override', {}).items(): notes[mid] = why
year = lambda i: M[i['person']]['start'] if 'person' in i else i['year']
for mid, items in rows.items():
    if mid not in M: log['rows_unknown'].append(mid); continue
    M[mid]['people'] = sorted(items, key=year)
for m in c['movements']:
    if m.get('kind') == 'person': continue
    if not m.get('people'):
        why = notes.get(m['id'])
        if why: m['peopleNote'] = why
        else: log['no_note'].append(m['id'])
    else: m.pop('peopleNote', None)

# meta
c['meta']['totalEntries'] = len(c['movements'])
sc = collections.Counter(m['status'] for m in c['movements'])
c['meta']['statusCounts'] = {k: sc[k] for k in c['meta']['statusCounts'] if sc[k]} | {k: v for k, v in sc.items() if k not in c['meta']['statusCounts']}
c['meta']['release'] = {'number': int(REL), 'date': DATE}
json.dump(c, open(cout, 'w'), ensure_ascii=False, indent=1)
json.dump({k: v for k, v in log.items()}, open(f'{G3}/apply_log.json', 'w'), indent=1, ensure_ascii=False)
print({k: len(v) for k, v in log.items()})
