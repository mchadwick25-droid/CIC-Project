"""Usage: python3 check_draft.py <draft.json>
Scores every prose field (paragraph by paragraph) and checks every quote in fact_table,
links[].sources[] and people[].source against cic/texts at the stated lines (whitespace squashed).
Run from the repo root."""
import json,sys,re,os
sys.path.insert(0,os.getcwd())
from engine.m7.turn_readability import score_turn
PROSE=['relationsSummary','why','teaser','longDescription','legacy','sourcing','floorNote']
sq=lambda s:re.sub(r'\s+',' ',s).strip()
def qcheck(tag,f,lines,q):
    if not f or not lines or not q: return
    if not f.startswith('cic/texts/') or not os.path.exists(f): print('QUOTE-FILE',tag,f); return
    L=open(f,encoding='utf8').read().split('\n'); m=re.match(r'^(\d+)(?:-(\d+))?$',str(lines))
    if not m: print('QUOTE-LINES',tag,lines); return
    a,b=int(m[1]),int(m[2] or m[1])
    if sq(q) not in sq(' '.join(L[a-1:b])): print('QUOTE-MISS',tag,f,lines,q[:80])
def score(tag,text):
    for i,p in enumerate([p for p in re.split(r'\n\s*\n',text) if p.strip()]):
        r=score_turn(p)
        if r.scored and (r.fre<60 or r.fk>10): print(f'READ-FAIL {tag}[{i}] FRE={r.fre:.0f} FK={r.fk:.1f}: {p[:70]}')
d=json.load(open(sys.argv[1]))
ents=d.get('entries') or ([d['movement']] if 'movement' in d else [])
for m in ents:
    for k in PROSE:
        if isinstance(m.get(k),str): score(f"{m.get('id')}.{k}",m[k])
    for j,s in enumerate(m.get('documentedStories') or []):
        for k in ('teaser','text','caveat'):
            if isinstance(s.get(k),str): score(f"{m.get('id')}.story{j}.{k}",s[k])
        for t,src in enumerate(s.get('sources') or []): qcheck(f"{m.get('id')}.story{j}.src{t}",src.get('file'),src.get('lines'),src.get('quote'))
    for j,p in enumerate(m.get('people') or []):
        s=p.get('source')
        if s: qcheck(f"{m.get('id')}.people{j}",s.get('file'),s.get('lines'),s.get('quote'))
for i,r in enumerate(d.get('fact_table') or []): qcheck(f'fact{i}',r.get('file'),r.get('lines'),r.get('quote'))
for e in d.get('links') or []:
    if e.get('note'): score(f"link {e.get('id')}.note",e['note'])
    if e.get('outcome'): score(f"link {e.get('id')}.outcome",e['outcome'])
    for j,s in enumerate(e.get('sources') or []): qcheck(f"link {e.get('id')}.src{j}",s.get('file'),s.get('lines'),s.get('quote'))
for n in d.get('neighbor_changes') or []:
    for k,v in (n.get('set') or {}).items():
        if k in PROSE and isinstance(v,str): score(f"{n.get('id')}.{k}",v)
print('check done')
