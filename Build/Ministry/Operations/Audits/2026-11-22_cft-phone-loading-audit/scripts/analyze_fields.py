import json, collections, statistics
h = open('/home/user/CIC-Project/cft-website/index.html', encoding='utf8').read()
j = h.index('=', h.index('const DATA')) + 1
D, _ = json.JSONDecoder().raw_decode(h[j:].lstrip())
sz = lambda v: len(json.dumps(v, separators=(',', ':'), ensure_ascii=False).encode())
U = {}
def walk(o, path):
    if o is None or not isinstance(o, (dict, list)): return
    if isinstance(o, list):
        for x in o: walk(x, path + '[]')
        return
    for k, v in o.items():
        pp = path + '.' + k
        e = U.setdefault(pp, {'bytes': 0, 'n': 0}); e['bytes'] += sz(v); e['n'] += 1
        walk(v, pp)
walk(D, 'DATA')
a = json.load(open('audit_reads2.json'))
R = a['main']['reads']; DL = a['deeplink']['startup']; phases = list(R.keys())
first = {}
for ph in phases:
    for p in R[ph]:
        if not p.endswith(' (in)'): first.setdefault(p, ph)
for p in DL: first.setdefault(p, 'deeplink-only')
paths = set(U)
leaves = [p for p in paths if not any(q != p and (q.startswith(p + '.') or q.startswith(p + '[]')) for q in paths)]
GROUP = {'startup': 'start-up', 'hover-link': 'link tooltip', 'open-link-card': 'link card', 'open-story': 'story card', 'open-card-tradition': 'card', 'open-card-built-world': 'card', 'open-card-person': 'card', 'open-card-council': 'card', 'deeplink-only': 'card'}
def grp(p):
    ph = first.get(p)
    if ph is None: return 'not read in any scenario'
    return GROUP.get(ph, 'other')
agg = collections.defaultdict(lambda: collections.defaultdict(int)); tot = 0
for L in leaves:
    top = L.split('.')[1].split('[]')[0]
    agg[top][grp(L)] += U[L]['bytes']; tot += U[L]['bytes']
print('leaf bytes %.2f MB vs data literal (compact) %.2f MB' % (tot / 1e6, sz(D) / 1e6))
for top in ('movements', 'edges', 'stories', 'eras', 'meta', 'statusMeta'):
    for g, b in sorted(agg[top].items(), key=lambda x: -x[1]):
        if b > 5000: print('  %-10s %-26s %6.2f MB' % (top, g, b / 1e6))
# per-entry card payload: bytes of movement fields NOT read at start-up (what a card would fetch)
start_leaf = {L for L in leaves if first.get(L) == 'startup'}
def entry_bytes(m, path='DATA.movements[]'):
    need = 0; lazy = 0
    def rec(o, p):
        nonlocal need, lazy
        if isinstance(o, list):
            for x in o: rec(x, p + '[]')
        elif isinstance(o, dict):
            for k, v in o.items(): rec(v, p + '.' + k)
        else:
            b = len(json.dumps(o, ensure_ascii=False).encode())
            if p in start_leaf: need += b
            else: lazy += b
    rec(m, path); return need, lazy
lazy_sizes = []; need_sizes = []
for m in D['movements']:
    n, l = entry_bytes(m); need_sizes.append(n); lazy_sizes.append(l)
lazy_sizes.sort()
print('\nper-entry start-up data: median %.0f B, total %.2f MB' % (statistics.median(need_sizes), sum(need_sizes) / 1e6))
print('per-entry card payload: median %.1f KB, p90 %.1f KB, p99 %.1f KB, max %.1f KB (%d entries)' % (statistics.median(lazy_sizes) / 1e3, lazy_sizes[int(len(lazy_sizes) * .9)] / 1e3, lazy_sizes[int(len(lazy_sizes) * .99)] / 1e3, lazy_sizes[-1] / 1e3, len(lazy_sizes)))
big = sorted(zip(lazy_sizes, ), reverse=True)[:1]
ids = sorted(((entry_bytes(m)[1], m['id']) for m in D['movements']), reverse=True)[:5]
print('largest card payloads:', [(i, round(b / 1e3)) for b, i in ids])
json.dump({'startup_leaves': sorted(start_leaf)}, open('startup_leaves.json', 'w'), indent=1)
