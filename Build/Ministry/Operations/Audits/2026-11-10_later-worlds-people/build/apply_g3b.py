"""P2-G3b apply: merge the reviewed person-entry drafts into the census as one data release.
Usage (repo root): python3 -I apply_g3b.py <census in> <census out> <release number> <date> <decisions.json> <Draft.json>...
decisions.json: {"field_overrides": [{"id", "set", "reason"}], "concerns_skip": [link ids], "text_fixes": [{"id", "old", "new"}], "rows_drop": [{"movement", "name", "reason"}]}"""
import json, sys, re, collections, os
HERE = os.path.dirname(os.path.abspath(__file__))
cin, cout, REL, DATE, decf, *drafts = sys.argv[1:]
dec = json.load(open(decf))
c = json.load(open(cin))
M = {m['id']: m for m in c['movements']}
E = {e['id']: e for e in c['edges']}
log = collections.defaultdict(list)
PREFIX = {1: 'I', 2: 'I', 3: 'II', 4: 'III', 5: 'IV', 6: 'V', 7: 'VI', 8: 'VII', 9: 'VIII', 10: 'IX'}
nextnum = collections.Counter()
for m in c['movements']:
    p, _, n = m['atlasId'].partition('.')
    k = re.match(r'\d+', n)
    nextnum[p] = max(nextnum[p], int(k.group()) if k else 0)
EDGE_KEYS = {'id','from','to','type','confidence','note','sources','citation_specificity','verification_state','outcome','concerns'}
retired = {r['id'] for r in c['retiredMovements']}
skip = set(dec.get('concerns_skip', []))
for f in drafts:
    x = json.load(open(f))
    for e in x.get('entries', []):
        assert e['id'] not in M and e['id'] not in retired, e['id']
        assert e.get('kind') == 'person' and e.get('toldWithin') in M, e['id']
        p = PREFIX[int(e['era'])]; nextnum[p] += 1
        e['atlasId'] = f'{p}.{nextnum[p]}'
        e.setdefault('reviewStatus', 'AI-checked'); e.pop('people', None)
        c['movements'].append(e); M[e['id']] = e; log['entries'].append((os.path.basename(os.path.dirname(f)), e['id'], e['atlasId']))
    for l in x.get('links', []):
        l = {k: v for k, v in l.items() if k in EDGE_KEYS}
        assert l['id'] not in E, l['id']
        c['edges'].append(l); E[l['id']] = l; log['links'].append(l['id'])
    for ce in x.get('concerns', []) + [ce for ce in dec.get('concerns_add', []) if ce.get('draft') == f]:
        if ce['link_id'] in skip: log['concerns_skipped'].append(ce['link_id']); continue
        e = E[ce['link_id']]
        if e.get('concerns') and e['concerns'] != ce['concerns']:
            log['concerns_conflict'].append((ce['link_id'], e['concerns'], ce['concerns'])); continue
        e['concerns'] = ce['concerns']; log['concerns'].append((ce['link_id'], ce['concerns']))
    for r in x.get('rows', []):
        m = M[r['movement']]; items = m.setdefault('people', [])
        if r.get('replace_name'):
            hit = [i for i in items if i.get('name') == r['replace_name']]
            assert len(hit) == 1, r
            items[items.index(hit[0])] = {'person': r['person']}
        else:
            assert not any(i.get('person') == r['person'] for i in items), r
            items.append({'person': r['person']})
        log['rows'].append((r['movement'], r.get('replace_name'), r['person']))
for rd in dec.get('rows_drop', []):
    m = M[rd['movement']]; before = len(m.get('people', []))
    m['people'] = [i for i in m.get('people', []) if i.get('name') != rd['name']]
    assert len(m['people']) == before - 1, rd
    log['rows_dropped'].append((rd['movement'], rd['name'], rd['reason']))
for fo in dec.get('field_overrides', []):
    tgt = E[fo['id']] if fo.get('kind') == 'edge' else M[fo['id']]
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
year = lambda i: int(M[i['person']]['start']) if 'person' in i else int(i['year'])
for m in c['movements']:
    if m.get('kind') != 'person' and m.get('people'):
        m['people'] = sorted(m['people'], key=year)
        m.pop('peopleNote', None)
c['meta']['totalEntries'] = len(c['movements'])
sc = collections.Counter(m['status'] for m in c['movements'])
c['meta']['statusCounts'] = {k: sc[k] for k in c['meta']['statusCounts'] if sc[k]} | {k: v for k, v in sc.items() if k not in c['meta']['statusCounts']}
c['meta']['release'] = {'number': int(REL), 'date': DATE}
json.dump(c, open(cout, 'w'), ensure_ascii=False, indent=1)
json.dump({k: v for k, v in log.items()}, open(f'{HERE}/apply_log.json', 'w'), indent=1, ensure_ascii=False)
print({k: len(v) for k, v in log.items()})
