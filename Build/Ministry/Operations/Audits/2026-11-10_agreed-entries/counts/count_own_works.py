import yaml,glob,json,re,os,collections
cen=json.load(open('cic-website/data/world-census.json'))
ids={m['id'] for m in cen['movements']}
out=[]
for f in sorted(glob.glob('cic/corpus-map/*.yaml')):
    mid=os.path.basename(f)[:-5]
    if mid not in ids: continue
    d=yaml.safe_load(open(f))
    works=collections.defaultdict(set)
    for r in d.get('works') or []:
        if r.get('role')!='tradition': continue
        a=r.get('author') or ''
        w=re.sub(r'\W+',' ',(r.get('work') or '').lower()).strip()
        works[a].add(w)
    for a,ws in works.items():
        if len(ws)>=10: out.append((len(ws),a,mid))
for n,a,m in sorted(out,reverse=True): print(n,a,m)
print(len(out))
