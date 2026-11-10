import json,collections,sys,pickle
S=sys.argv[1]
P=json.load(open('Build/Ministry/Operations/Audits/2026-11-10_agreed-entries/counts/aliases_all.json'))
G=json.load(open(S+'/groups.json'))['groups']
amb=set(json.load(open('Build/Ministry/Operations/Audits/2026-11-10_agreed-entries/counts/ambiguous_aliases.json'))['aliases'])
cen=json.load(open('cic-website/data/world-census.json'))
start={m['id']:m['start'] for m in cen['movements'] if m.get('kind')!='person'}
persons={m['id']:m for m in cen['movements'] if m.get('kind')=='person'}
rows=json.load(open(S+'/shelf_rows.json'))
shelf=collections.defaultdict(list)
for r in rows: shelf[r['T']].append(r)
hits=collections.defaultdict(lambda: collections.defaultdict(list)) # alias -> file -> [line]
for line in open(S+'/matches.txt',encoding='utf8',errors='ignore'):
    f,_,rest=line.rstrip('\n').partition(':'); ln,_,a=rest.partition(':')
    hits[a][f[len('cic/texts/'):]].append(int(ln))
pickle.dump({k:dict(v) for k,v in hits.items()},open(S+'/hits.pkl','wb'))
out=[]
for g in G:
    ps=[P[i] for i in g]
    homes=sorted({p['movement'] for p in ps if p.get('movement')})
    ys=[p.get('last_year') or p.get('year') for p in ps]; ys=[y for y in ys if y]
    last=max(ys) if ys else None
    authors={p['author'] for p in ps if p.get('author')}
    al_all=sorted({a.strip() for p in ps for a in p['aliases']+[p['name']] if a.strip()})
    al_cnt=sorted({a.strip() for p in ps for a in p['aliases_counted'] if a.strip()})
    rec={'name':ps[0]['name'],'names':sorted({p['name'] for p in ps}),'homes':homes,'last_year':last,'year':min([p['year'] for p in ps if p.get('year')] or [None]) if any(p.get('year') for p in ps) else None,
         'authors':sorted(authors),'aliases_all':al_all,'aliases_counted':al_cnt,'keys':[p['key'] for p in ps]}
    if last is None: rec.update(per_all={},per_cnt={}); out.append(rec); continue
    for lab,al in (('per_all',al_all),('per_cnt',al_cnt)):
        per={}
        for T,rs in shelf.items():
            if T in homes or start[T]<=last: continue
            files={r['file'] for r in rs if not (r['author'] and r['author'] in authors)}
            n=sum(len(hits.get(a,{}).get(f,[])) for f in files for a in al)
            if n>=5: per[T]=n
        rec[lab]=dict(sorted(per.items(),key=lambda x:-x[1]))
    out.append(rec)
for r in out:
    r['pass_cnt']=len(r['per_cnt'])>=2; r['pass_all']=len(r['per_all'])>=2
    r['person_entry']=None
json.dump(out,open(S+'/raw2.json','w'),indent=0,ensure_ascii=False)
print(sum(r['pass_cnt'] for r in out),'pass counted;',sum(r['pass_all'] for r in out),'pass all aliases')
