"""Round 2: drop aliases round 1 showed to be namesakes (N>=2, S=0), recount, and give each candidate
still in reach fresh contexts (not labelled in round 1) for every tradition not yet at 5, plus a
strict-locus recheck for traditions batch v04 confirmed."""
import json,pickle,collections,sys,os
S=sys.argv[1]
out=pickle.load(open(S+'/t3.pkl','rb'))
cands=sorted([r for r in out if r['pass_masked']],key=lambda r:(r['year'] or 0))
R={};pk={}
for b in range(10):
    for x in json.load(open(f'{S}/agents/v{b:02d}/result.json')): R[x['cid']]=x
    for p in json.load(open(f'{S}/packets/batch{b:02d}.json')): pk[p['cid']]=p
sys.argv=[None,S,'1','1','1']
exec(open(S+'/packets.py').read().split('cands=[r for r')[0])  # reuse ctx/sample/rowinfo
dropped={};plan=[]
for ci,r in enumerate(cands):
    cid=f'C{ci:03d}'; x=R[cid]; p=pk[cid]
    lab=collections.defaultdict(collections.Counter); seen=set()
    for t in p['traditions']:
        for c in t['contexts']:
            L=x['traditions'].get(t['tradition'],{}).get('labels',{}).get(c['id'])
            lab[c['alias']][L]+=1; seen.add((c['file'],c['line'],c['alias']))
    bad={a for a,cn in lab.items() if cn['N']+cn['E']>=2 and cn['S']==0 and cn['N']>=1}
    dropped[cid]=sorted(bad)
    clean={T:v.get('clean_passages',0) for T,v in x['traditions'].items()}
    strict_recheck = (cid in [q['cid'] for q in json.load(open(f'{S}/packets/batch04.json'))])
    per={}
    for T,L in r['_detail'].items():
        L2=[y for y in L if y[2] not in bad]
        if len(L2)>=5: per[T]=L2
    confirmed=[T for T,v in clean.items() if v>=5 and not strict_recheck]
    need=2-len(confirmed)
    if need<=0: continue
    todo=[T for T in sorted(per,key=lambda T:-len(per[T])) if T not in confirmed]
    if len(todo)<need: continue
    trads=[]
    for T in todo[:4]:
        fresh=[y for y in per[T] if (y[0],y[1],y[2]) not in seen]
        prior=[(c['id'],x['traditions'][T]['labels'].get(c['id'])) for t in p['traditions'] if t['tradition']==T for c in t['contexts']] if T in x['traditions'] else []
        k=25 if (strict_recheck and T in clean) else 15
        smp=sample(fresh,k)
        if strict_recheck and T in clean:  # re-show round-1 S contexts for strict recheck
            smp=[(c['file'],c['line'],c['alias']) for t in p['traditions'] if t['tradition']==T for c in t['contexts'] if x['traditions'][T]['labels'].get(c['id'])=='S']+smp[:15]
        if not smp: continue
        trads.append({'tradition':T,'tradition_name':mv[T]['name'],'tradition_start':mv[T]['start'],'count_after_dropping':len(per[T]),
            'round1_clean':clean.get(T),'files':{f:rowinfo[(T,f)] for f in sorted({y[0] for y in smp})},
            'contexts':[{'id':f'{T}#r2-{j}','file':y[0],'line':y[1],'alias':y[2],'text':ctx(*y)} for j,y in enumerate(smp)]})
    plan.append({'cid':cid,'name':r['name'],'homes':r['homes'],'year':r['year'],'last_year':r['last_year'],'aliases_dropped_as_namesakes':sorted(bad),
                 'confirmed_round1':{T:clean[T] for T in confirmed},'needs':need,'traditions':trads,'round1_notes':{k:x.get(k) for k in ('namesake_notes','comment')}})
json.dump(dropped,open(S+'/round2_dropped_aliases.json','w'),indent=0)
plan=[p for p in plan if len(p['traditions'])>=p['needs']]
NB=10
os.makedirs(S+'/packets2',exist_ok=True)
for b in range(NB): json.dump(plan[b::NB],open(f'{S}/packets2/batch{b:02d}.json','w'),indent=1,ensure_ascii=False)
print(len(plan),'candidates in round 2; contexts',sum(len(t['contexts']) for p in plan for t in p['traditions']))
print([os.path.getsize(f'{S}/packets2/batch{b:02d}.json')//1000 for b in range(NB)])
