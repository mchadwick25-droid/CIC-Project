"""P2-G89b apply: merge the reviewed slice drafts into the census as one data release.
Usage (repo root): python3 -I apply_g89b.py <census in> <census out> <release number> <date> [decisions.json]
Reads drafts/<slice>/Draft.json for each slice in SLICES. decisions.json (optional):
{"variants": {"<entry id>": "<variant name>"}, "field_overrides": [{"id", "kind"?, "set", "reason"}],
 "drop_links": [{"id", "reason"}], "drop_entries": [{"id", "reason"}]}
Drafting keys (ruling, reason, raw_file, variants, flags) never reach the census."""
import json, sys, re, collections, os
HERE = os.path.dirname(os.path.abspath(__file__))
SLICES = ['AF', 'LA', 'AS1', 'AS2', 'ME1', 'ME2', 'RVA', 'RVB']
cin, cout, REL, DATE = sys.argv[1:5]
dec = json.load(open(sys.argv[5])) if len(sys.argv) > 5 else {}
c = json.load(open(cin))
M = {m['id']: m for m in c['movements']}
E = {e['id']: e for e in c['edges']}
log = collections.defaultdict(list)
DRAFT_KEYS = {'ruling', 'reason', 'variants', 'flags', 'drafter_flags', 'raw_file', 'g89'}

def clean(o):
    if isinstance(o, dict): return {k: clean(v) for k, v in o.items() if k not in DRAFT_KEYS}
    if isinstance(o, list): return [clean(x) for x in o]
    return o

PREFIX = {8: 'VII', 9: 'VIII'}
nextnum = collections.Counter()
for m in c['movements']:
    p, _, n = m['atlasId'].partition('.')
    k = re.match(r'\d+', n)
    nextnum[p] = max(nextnum[p], int(k.group()) if k else 0)

EDGE_KEYS = {'id', 'from', 'to', 'type', 'confidence', 'note', 'sources', 'citation_specificity', 'verification_state', 'outcome', 'concerns'}
drop_e = {d['id'] for d in dec.get('drop_entries', [])}
drop_l = {d['id'] for d in dec.get('drop_links', [])}
drafts = {s: json.load(open(f'{HERE}/drafts/{s}/Draft.json')) for s in SLICES}
# entries first, in era then start order, so atlasIds follow the timeline
ents = sorted([(s, e) for s, x in drafts.items() for e in x.get('entries', []) if e['id'] not in drop_e],
              key=lambda t: (t[1]['era'], t[1]['start'], t[1]['id']))
for s, e in ents:
    assert e['id'] not in M, e['id']
    assert e['id'] not in {r['id'] for r in c['retiredMovements']}, e['id']
    v = dec.get('variants', {}).get(e['id'])
    if v: e.update(e['variants'][v]); log['variant'].append((e['id'], v))
    e = clean(e)
    p = PREFIX[e['era']]; nextnum[p] += 1
    e['atlasId'] = f'{p}.{nextnum[p]}'
    e.setdefault('reviewStatus', 'AI-checked'); e.setdefault('people', [])
    c['movements'].append(e); M[e['id']] = e; log['entries'].append((s, e['id'], e['atlasId']))
for s, x in drafts.items():
    for n in x.get('neighbor_changes', []):
        tgt = E[n['id']] if n.get('kind') == 'edge' else M[n['id']]
        for k, v in clean(n['set']).items(): tgt[k] = v
        log['neighbor'].append((s, n['id'], sorted(n['set'])))
    for r in x.get('retire_links', []):
        assert r['id'] in E, r['id']
        c['edges'] = [e for e in c['edges'] if e['id'] != r['id']]; del E[r['id']]
        rec = {'id': r['id'], 'date': DATE, 'reason': r['reason']}
        if r.get('replacedBy'): rec['replacedBy'] = r['replacedBy']
        c['retiredLinks'].append(rec); log['retired'].append(r['id'])
    for l in x.get('links', []):
        if l['id'] in drop_l: log['link_dropped'].append(l['id']); continue
        l = clean({k: v for k, v in l.items() if k in EDGE_KEYS})
        assert l['from'] in M and l['to'] in M, (l['id'], l['from'], l['to'])
        if l['id'] in E:
            E[l['id']].clear(); E[l['id']].update(l); log['rewritten'].append(l['id'])
        else:
            c['edges'].append(l); E[l['id']] = l; log['links'].append(l['id'])
for fo in dec.get('field_overrides', []):
    tgt = E[fo['id']] if fo.get('kind') == 'edge' else M[fo['id']]
    for k, v in fo['set'].items(): tgt[k] = v
    log['overrides'].append((fo['id'], sorted(fo['set']), fo['reason']))

c['meta']['totalEntries'] = len(c['movements'])
sc = collections.Counter(m['status'] for m in c['movements'])
c['meta']['statusCounts'] = {k: sc[k] for k in c['meta']['statusCounts'] if sc[k]} | {k: v for k, v in sc.items() if k not in c['meta']['statusCounts']}
c['meta']['release'] = {'number': int(REL), 'date': DATE}
open(cout, 'w').write(json.dumps(c, ensure_ascii=False, indent=1) + '\n')
json.dump({k: v for k, v in log.items()}, open(f'{HERE}/apply_log.json', 'w'), indent=1, ensure_ascii=False)
print({k: len(v) for k, v in log.items()})
