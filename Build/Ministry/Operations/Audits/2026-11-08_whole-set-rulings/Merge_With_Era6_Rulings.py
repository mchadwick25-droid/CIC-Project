import json,copy,sys
S=sys.argv[1]
b=json.load(open(f'{S}/main/base_release17.json')); o=json.load(open(f'{S}/main/main_r18_other.json')); m=json.load(open(f'{S}/main/mine_r18.json'))
B={e['id']:e for e in b['edges']};M={e['id']:e for e in m['edges']}
d=copy.deepcopy(o); O={e['id']:e for e in d['edges']}
key=lambda s:(s['kind'],s['work'],s.get('lines'))
special={'latin-papal-church-gregorian--the-carmelites','byzantine-church-after-1054--kievan-rus-christianity-1054-1240'}
log=[]
for i in B:
    if i not in M or B[i]==M[i] or i in special: continue
    if i not in O: log.append(('gone-in-theirs',i)); continue
    for k in set(B[i])|set(M[i]):
        if B[i].get(k)!=M[i].get(k):
            assert B[i].get(k)==O[i].get(k),(i,k)   # theirs did not touch it
            if k in M[i]: O[i][k]=copy.deepcopy(M[i][k])
            else: O[i].pop(k,None)
            log.append(('mine',i,k))
# Carmelites: theirs + my restored Zimmerman quote
c=O['latin-papal-church-gregorian--the-carmelites']
z=[s for s in M['latin-papal-church-gregorian--the-carmelites']['sources'] if s['kind']=='secondary' and s.get('quote')]
c['sources']=[s for s in c['sources'] if not (s['kind']=='secondary' and 'Zimmerman' in s['work'] and not s.get('quote'))]+z
# Kievan metropolitans: theirs sources + outcome; my grade and note; add my 1802-1805 quote
k=O['byzantine-church-after-1054--kievan-rus-christianity-1054-1240']; mk=M[k['id']]
k['confidence']=mk['confidence']; k['note']=mk['note']
have={s.get('lines') for s in k['sources']}
k['sources']+= [copy.deepcopy(s) for s in mk['sources'] if s.get('lines')=='1802-1805' and '1802-1805' not in have]
# retirement (ruling 5)
mr=[r for r in m['retiredLinks'] if r['id']=='bogomils--cathars-albigensians'][0]
d['edges']=[e for e in d['edges'] if e['id']!=mr['id']]
if mr['id'] not in {r['id'] for r in d['retiredLinks']}: d['retiredLinks'].append(mr)
# ruling 2 across the whole set
for e in d['edges']:
    q=any(s.get('quote') and s.get('file') and s.get('lines') for s in e['sources'])
    old=e['verification_state']
    if q: e['verification_state']='verified-direct'
    elif old in('verified-direct','unverified'): e['verification_state']='named-not-rechecked'
    if e['verification_state']!=old: log.append(('R2',e['id'],old+'->'+e['verification_state']))
d['meta']['release']={'number':19,'date':'2026-11-08'}
open('cic-website/data/world-census.json','w').write(json.dumps(d,ensure_ascii=False,indent=1)+'\n')
import collections; print(collections.Counter(l[0] for l in log)); [print(l) for l in log if l[0]!='mine']
