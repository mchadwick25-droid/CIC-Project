import json, statistics
h = open('/home/user/CIC-Project/cft-website/index.html', encoding='utf8').read()
j = h.index('=', h.index('const DATA')) + 1
D, _ = json.JSONDecoder().raw_decode(h[j:].lstrip())
SL = set(json.load(open('startup_leaves.json'))['startup_leaves'])
SL.discard('DATA.movements[].longDescription')
SL.add('DATA.movements[].card.role')
def split(m):
    need = lazy = 0
    def rec(o, p):
        nonlocal need, lazy
        if isinstance(o, list):
            for x in o: rec(x, p + '[]')
        elif isinstance(o, dict):
            for k, v in o.items(): rec(v, p + '.' + k)
        else:
            b = len(json.dumps(o, ensure_ascii=False).encode())
            if p in SL: need += b
            else: lazy += b
    rec(m, 'DATA.movements[]'); return need, lazy
r = [split(m) for m in D['movements']]
lazy = sorted(l for _, l in r)
print('start-up per entry: median %d B; all entries %.2f MB (leaf values, before the 629 hashes)' % (statistics.median(n for n, _ in r), sum(n for n, _ in r) / 1e6))
print('card file per entry: median %.1f KB, p90 %.1f KB, p99 %.1f KB, max %.1f KB' % (statistics.median(lazy) / 1e3, lazy[int(.9 * len(lazy))] / 1e3, lazy[int(.99 * len(lazy))] / 1e3, lazy[-1] / 1e3))
print('compressed (gzip) estimate for the median card: ~%.1f KB' % (statistics.median(lazy) / 1e3 * 0.28))
