import pickle,json,glob,os,yaml,collections,sys,re
S=sys.argv[1]
out=pickle.load(open(S+'/t3.pkl','rb'))
cands=sorted([r for r in out if r['pass_masked']],key=lambda r:(r['year'] or 0))
cen=json.load(open('cic-website/data/world-census.json')); mv={m['id']:m for m in cen['movements']}
allrows=collections.defaultdict(list)
for fn in glob.glob('cic/corpus-map/*.yaml'):
    T=os.path.basename(fn)[:-5]
    for r in yaml.safe_load(open(fn)).get('works') or []:
        if r.get('author'): allrows[r['author']].append({'shelf':T,'work':r.get('work'),'role':r.get('role'),'file':r.get('source_file')})
P=json.load(open('Build/Ministry/Operations/Audits/2026-11-10_agreed-entries/counts/aliases_all.json'))
facts=[]
for ci,r in enumerate(cands):
    ow=[x for a in r['authors'] for x in allrows.get(a,[])]
    homes=[{'id':h,'name':mv[h]['name'] if h in mv else None,'dates':mv[h]['dates'] if h in mv else None} for h in r['homes']]
    # does a home text name them as founder?
    fnd=[]
    for h in r['homes']:
        m=mv.get(h,{}); txt=' '.join(str(m.get(k,'')) for k in ('longDescription','why','voices','legacy','entry','relationsSummary'))
        for n in r['names']:
            last=n.split()[-1] if n.split() else n
            for s in re.split(r'(?<=[.!?])\s+',txt):
                if (n in s or (len(last)>4 and last in s)) and re.search(r'found|began|started|gathered|its leader|named for|named after|took its name',s,re.I): fnd.append(s[:300])
    facts.append({'cid':f'C{ci:03d}','name':r['name'],'names':r['names'],'year':r['year'],'last_year':r['last_year'],'homes':homes,
                  'own_works_rows':ow[:40],'own_works_count':len({(x['work'],x['file']) for x in ow}),'founder_sentences':fnd[:6],'keys':r['keys']})
json.dump(facts,open(S+'/facts.json','w'),indent=1,ensure_ascii=False)
print(len(facts), sum(1 for f in facts if f['own_works_count']), sum(1 for f in facts if f['founder_sentences']))
