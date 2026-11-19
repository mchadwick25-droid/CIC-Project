import pickle,json,collections,sys,re,os
S=sys.argv[1]; NB=int(sys.argv[2]); PER=int(sys.argv[3]); NT=int(sys.argv[4])
out=pickle.load(open(S+'/t3.pkl','rb'))
rows=json.load(open(S+'/shelf_rows.json'))
cen=json.load(open('cic-website/data/world-census.json'))
mv={m['id']:m for m in cen['movements']}
amb=set(json.load(open('Build/Ministry/Operations/Audits/2026-11-10_agreed-entries/counts/ambiguous_aliases.json'))['aliases'])
rowinfo=collections.defaultdict(list)
for r in rows: rowinfo[(r['T'],r['file'])].append(f"{r['work']} (author id: {r['author']}; locus: {(r.get('locus') or '').strip()[:120]})")
fl={}
def lines(f):
    if f not in fl: fl[f]=open('cic/texts/'+f,encoding='utf-8',errors='replace').read().split('\n')
    return fl[f]
TAG=re.compile(r'<[^>]+>')
def ctx(f,ln,a):
    L=lines(f); seg=' '.join(L[max(0,ln-2):ln+1])
    if f.endswith('.xml'): seg=TAG.sub(' ',seg)
    seg=re.sub(r'\s+',' ',seg); i=seg.find(a)
    if i<0: i=len(seg)//2
    return seg[max(0,i-220):i+len(a)+220]
def sample(L,k):
    byf=collections.defaultdict(list)
    for x in L: byf[x[0]].append(x)
    for f in byf: 
        v=byf[f]; step=max(1,len(v)//k); byf[f]=v[::step]
    res=[]; fs=sorted(byf,key=lambda f:-len(byf[f]))
    while len(res)<k and any(byf[f] for f in fs):
        for f in fs:
            if byf[f] and len(res)<k: res.append(byf[f].pop(0))
    return res
cands=[r for r in out if r['pass_masked']]
cands.sort(key=lambda r:(r['year'] or 0))
os.makedirs(S+'/packets',exist_ok=True)
idx=[]
for ci,r in enumerate(cands):
    pk={'cid':f'C{ci:03d}','name':r['name'],'other_names':r['names'],'homes':r['homes'],'year':r['year'],'last_year':r['last_year'],
        'aliases_searched':r['aliases_all'],'aliases_with_namesake_risk':[a for a in r['aliases_all'] if a in amb or ' ' not in a],'traditions':[]}
    for T,n in list(r['per_masked'].items())[:NT]:
        smp=sample(r['_detail'][T],PER)
        pk['traditions'].append({'tradition':T,'tradition_name':mv[T]['name'],'tradition_start':mv[T]['start'],'masked_count':n,
            'files':{f:rowinfo[(T,f)] for f in sorted({x[0] for x in smp})},
            'contexts':[{'id':f'{T}#{j}','file':x[0],'line':x[1],'alias':x[2],'text':ctx(*x)} for j,x in enumerate(smp)]})
    pk['other_traditions_at_floor']={T:n for T,n in list(r['per_masked'].items())[NT:]}
    idx.append(pk)
for b in range(NB):
    json.dump(idx[b::NB],open(f'{S}/packets/batch{b:02d}.json','w'),indent=1,ensure_ascii=False)
json.dump([{'cid':p['cid'],'name':p['name']} for p in idx],open(S+'/packets/index.json','w'),indent=0)
print(len(idx),'candidates;',[os.path.getsize(f'{S}/packets/batch{b:02d}.json')//1000 for b in range(NB)],'KB')
