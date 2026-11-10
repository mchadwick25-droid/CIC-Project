import json,glob,collections
R1={};PK1={}
for b in range(10):
    for x in json.load(open(f'agents/v{b:02d}/result.json')): R1[x['cid']]=x
    for p in json.load(open(f'packets/batch{b:02d}.json')): PK1[p['cid']]=p
R2={};PK2={}
for b in range(10):
    for x in json.load(open(f'agents2/w{b:02d}/result.json')): R2[x['cid']]=x
    for p in json.load(open(f'packets2/batch{b:02d}.json')): PK2[p['cid']]=p
v04={p['cid'] for p in json.load(open('packets/batch04.json'))}
ctx1={c['id']:c for p in PK1.values() for t in p['traditions'] for c in t['contexts']}
ctx2={c['id']:c for p in PK2.values() for t in p['traditions'] for c in t['contexts']}
out=[]
for cid,p in sorted(PK1.items()):
    trads={}
    x1=R1[cid]
    for T,v in x1['traditions'].items():
        if v.get('clean_passages',0)>=5 and not (cid in v04):
            refs=[f"{ctx1[k]['file']}:{ctx1[k]['line']}" for k,L in v['labels'].items() if L=='S' and k in ctx1]
            trads[T]={'clean':v['clean_passages'],'refs':refs,'best_quote':v.get('best_quote'),'round':1,'strict_rechecked':False}
    if cid in R2:
        for T,v in R2[cid]['traditions'].items():
            if v.get('clean_passages',0)>=5:
                refs=v.get('clean_refs') or [f"{ctx2[k]['file']}:{ctx2[k]['line']}" for k,L in v.get('labels',{}).items() if L=='S' and k in ctx2]
                trads[T]={'clean':v['clean_passages'],'refs':refs,'best_quote':v.get('best_quote'),'round':2,'strict_rechecked':True}
    rec={'cid':cid,'name':p['name'],'homes':p['homes'],'year':p['year'],'last_year':p['last_year'],'traditions_at_5':trads,'passes':len(trads)>=2,
         'notes':[x1.get('namesake_notes'),x1.get('comment')]+([R2[cid].get('namesake_notes'),R2[cid].get('comment')] if cid in R2 else [])}
    out.append(rec)
json.dump(out,open('consolidated.json','w'),indent=1,ensure_ascii=False)
ps=[r for r in out if r['passes']]
print(len(ps),'pass')
for r in ps: print(r['cid'],r['name'],r['homes'][:1],r['last_year'],{T:(v['clean'],v['round']) for T,v in r['traditions_at_5'].items()})
print('one tradition only:',[r['name'] for r in out if len(r['traditions_at_5'])==1])
