import json,re,collections,sys
S=sys.argv[1]
P=json.load(open('Build/Ministry/Operations/Audits/2026-11-10_agreed-entries/counts/aliases_all.json'))
def nk(s): return re.sub(r'\W+',' ',s.lower()).strip()
par=list(range(len(P)))
def f(i):
    while par[i]!=i: par[i]=par[par[i]]; i=par[i]
    return i
def u(a,b): par[f(a)]=f(b)
by=collections.defaultdict(list)
for i,p in enumerate(P):
    if p.get('author'): by['A:'+p['author']].append(i)
    by['N:'+nk(p['name'])].append(i)
    for a in p['aliases']:
        if ' ' in a.strip(): by['N:'+nk(a)].append(i)
for k,v in by.items():
    for j in v[1:]: u(v[0],j)
G=collections.defaultdict(list)
for i in range(len(P)): G[f(i)].append(i)
groups=list(G.values())
# possible same-person pairs not merged: share a one-word alias and dates within 40 years
one=collections.defaultdict(set)
for gi,g in enumerate(groups):
    for i in g:
        for a in P[i]['aliases']+[P[i]['name']]:
            a=a.strip()
            if ' ' not in a: one[a].add(gi)
def yr(g):
    ys=[P[i].get('last_year') or P[i].get('year') for i in g]; ys=[y for y in ys if y]; return max(ys) if ys else None
sus=set()
for a,s in one.items():
    s=sorted(s)
    for x in range(len(s)):
        for y in range(x+1,len(s)):
            a1,a2=yr(groups[s[x]]),yr(groups[s[y]])
            if a1 and a2 and abs(a1-a2)<=40: sus.add((s[x],s[y],a))
json.dump({'groups':groups,'suspect_pairs':sorted(sus)},open(S+'/groups.json','w'))
print(len(P),'rows ->',len(groups),'groups; suspect pairs',len(sus))
for x,y,a in sorted(sus)[:400]:
    print(a,'|',[ (P[i]['name'],P[i]['movement'],P[i].get('year')) for i in groups[x]][:2],'||',[(P[i]['name'],P[i]['movement'],P[i].get('year')) for i in groups[y]][:2])
