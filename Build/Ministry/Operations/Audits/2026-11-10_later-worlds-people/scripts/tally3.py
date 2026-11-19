import json,pickle,collections,sys,re
S=sys.argv[1]
raw=json.load(open(S+'/raw2.json'))
hits=pickle.load(open(S+'/hits.pkl','rb')); span=pickle.load(open(S+'/span.pkl','rb')); bad=pickle.load(open(S+'/bad.pkl','rb'))
rows=json.load(open(S+'/shelf_rows.json'))
cen=json.load(open('cic-website/data/world-census.json'))
start={m['id']:m['start'] for m in cen['movements'] if m.get('kind')!='person'}
pe={m['id']:m['name'] for m in cen['movements'] if m.get('kind')=='person'}
def nk(s): return re.sub(r'\W+',' ',s.lower()).strip()
pen={nk(v):k for k,v in pe.items()}; pen.update({nk('Tertullian of Carthage'):'tertullian',nk('Irenaeus of Lyons'):'irenaeus-of-lyon',nk('Thomas a Kempis'):'thomas-a-kempis'})
shelf=collections.defaultdict(list)
for r in rows: shelf[r['T']].append(r)
out=[]
for r in raw:
    ent=None
    for n in r['names']+[a for a in r['aliases_all'] if ' ' in a]:
        if nk(n) in pen: ent=pen[nk(n)]
    r['person_entry']=ent
    per={}; detail={}
    if r['last_year'] is not None and not ent:
        for T,rs in shelf.items():
            if T in r['homes'] or start[T]<=r['last_year']: continue
            files={x['file'] for x in rs if not (x['author'] and x['author'] in r['authors'])}
            L=[]
            for f in files:
                sp=span[T].get(f); bd=bad[f]
                for a in r['aliases_all']:
                    for ln in hits.get(a,{}).get(f,[]):
                        if ln in bd: continue
                        if sp is not None and ln not in sp: continue
                        L.append((f,ln,a))
            if len(L)>=5: per[T]=len(L); detail[T]=sorted(set(L))
    r['per_masked']=dict(sorted(per.items(),key=lambda x:-x[1])); r['pass_masked']=len(per)>=2
    r['_detail']=detail
    out.append(r)
pickle.dump(out,open(S+'/t3.pkl','wb'))
c=[r for r in out if r['pass_masked']]
print('person entries matched',sum(1 for r in out if r['person_entry']),'| pass masked (all aliases)',len(c),'| of which pass on counted-alias raw',sum(r['pass_cnt'] for r in c))
print('ctx needed if 15/trad top4:',sum(min(15,n) for r in c for n in list(r['per_masked'].values())[:4]))
