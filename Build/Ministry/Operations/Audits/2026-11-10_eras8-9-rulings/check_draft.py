"""Usage (repo root): python3 check_draft.py <Draft.json> [<raw dir>]
Scores every prose paragraph (Reading Ease 60+, FK 10 or less, engine.m7.turn_readability) and checks
every quote: Library quotes against cic/texts at their lines, online quotes against the saved raw text
named by raw_file (resolved against the raw dir's parent). Whitespace is squashed; nothing else."""
import json, sys, re, os
sys.path.insert(0, os.getcwd())
from engine.m7.turn_readability import score_turn
PROSE = ['relationsSummary', 'why', 'teaser', 'longDescription', 'legacy', 'sourcing', 'floorNote', 'statusDescription', 'peopleNote']
sq = lambda s: re.sub(r'\s+', ' ', s).strip()
d = json.load(open(sys.argv[1]))
base = os.path.dirname(os.path.abspath(sys.argv[2])) if len(sys.argv) > 2 else os.path.dirname(os.path.abspath(sys.argv[1]))
n = {'quotes': 0, 'paras': 0}

def qcheck(tag, s):
    q = s.get('quote')
    if not q: return
    n['quotes'] += 1
    if s.get('file'):
        f = s['file']
        if not f.startswith('cic/texts/') or not os.path.exists(f): print('QUOTE-FILE', tag, f); return
        L = open(f, encoding='utf8').read().split('\n'); m = re.match(r'^(\d+)(?:-(\d+))?$', str(s.get('lines', '')))
        if not m: print('QUOTE-LINES', tag, s.get('lines')); return
        a, b = int(m[1]), int(m[2] or m[1])
        if sq(q) not in sq(' '.join(L[a - 1:b])): print('QUOTE-MISS', tag, f, s.get('lines'), q[:80])
    elif s.get('raw_file'):
        p = os.path.join(base, s['raw_file'])
        if not os.path.exists(p): print('RAW-MISSING', tag, s['raw_file']); return
        if sq(q) not in sq(open(p, encoding='utf8', errors='replace').read()): print('QUOTE-MISS-RAW', tag, s['raw_file'], q[:80])
        if not s.get('url') or not s.get('accessed'): print('RAW-NO-URL', tag)
    elif s.get('url'):
        print('QUOTE-UNCHECKED (no raw_file)', tag, q[:60])

def score(tag, text):
    for i, p in enumerate([p for p in re.split(r'\n\s*\n', text) if p.strip()]):
        r = score_turn(p); n['paras'] += 1
        if r.scored and (r.fre < 60 or r.fk > 10): print(f'READ-FAIL {tag}[{i}] FRE={r.fre:.0f} FK={r.fk:.1f}: {p[:70]}')

for m in d.get('entries', []):
    for k in PROSE:
        if isinstance(m.get(k), str): score(f"{m.get('id')}.{k}", m[k])
    for j, s in enumerate(m.get('documentedStories') or []):
        for k in ('teaser', 'text', 'caveat'):
            if isinstance(s.get(k), str): score(f"{m.get('id')}.story{j}.{k}", s[k])
        for t, src in enumerate(s.get('sources') or []): qcheck(f"{m.get('id')}.story{j}.src{t}", src)
    for j, p in enumerate(m.get('people') or []):
        if p.get('source'): qcheck(f"{m.get('id')}.people{j}", p['source'])
for i, r in enumerate(d.get('fact_table') or []): qcheck(f'fact{i}', r)
for e in d.get('links') or []:
    for k in ('note', 'outcome'):
        if e.get(k): score(f"link {e.get('id')}.{k}", e[k])
    for j, s in enumerate(e.get('sources') or []): qcheck(f"link {e.get('id')}.src{j}", s)
for c in d.get('neighbor_changes') or []:
    for k, v in (c.get('set') or {}).items():
        if k in PROSE and isinstance(v, str): score(f"{c.get('id')}.{k}", v)
print('checked', n)
