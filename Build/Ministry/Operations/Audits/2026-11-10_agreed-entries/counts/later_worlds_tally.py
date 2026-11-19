"""Later-worlds count, tally step (rule: Decision-Log 2026-11-09, People on the map).
Input: aliases_all.json (people with aliases, year, last_year, movement, author) and matches.txt
(ripgrep: every whole-word, case-sensitive alias hit in the cic/texts files that some Library shelf
holds in role "tradition"). A tradition's own-voice texts are the files of its shelf's tradition rows,
less rows by the person. Later = the tradition starts after the person's last year (or year).
Pass = FLOOR or more mentions in each of TRADS or more later traditions."""
import json,yaml,glob,os,sys,collections
FLOOR,TRADS=5,2
S=sys.argv[1]
cen=json.load(open('cic-website/data/world-census.json'))
start={m['id']:m['start'] for m in cen['movements'] if m.get('kind')!='person'}
people=json.load(open(f'{S}/aliases_all.json'))
alias_to=collections.defaultdict(set)
for i,p in enumerate(people):
    for a in p['aliases_counted']: alias_to[a.strip()].add(i)
hits=collections.defaultdict(collections.Counter)  # file -> alias -> n
for line in open(f'{S}/matches.txt',encoding='utf8',errors='ignore'):
    f,_,a=line.rstrip('\n').partition(':')
    if a in alias_to: hits[f][a]+=1
shelf=collections.defaultdict(set)
for fn in glob.glob('cic/corpus-map/*.yaml'):
    T=os.path.basename(fn)[:-5]
    if T not in start: continue
    for r in yaml.safe_load(open(fn)).get('works') or []:
        if r.get('role')=='tradition' and r.get('source_file'): shelf[T].add(('cic/texts/'+r['source_file'],r.get('author')))
import re as _re
def nk(s): return _re.sub(r'\W+',' ',s.lower()).strip()
group={}; homes=collections.defaultdict(set); reps={}
for i,p in enumerate(people):
    k=nk(p['name']); 
    for a in p['aliases_counted']:
        if ' ' in a and nk(a) in group: k=group[nk(a)]; break
    group.setdefault(nk(p['name']),k)
    for a in p['aliases_counted']:
        if ' ' in a: group.setdefault(nk(a),k)
    homes[k].add(p.get('movement')); reps.setdefault(k,[]).append(i)
res=[]
for k,idx in reps.items():
    i=idx[0]; p=people[i]
    lasts=[people[j].get('last_year') for j in idx if people[j].get('last_year')]
    years=[people[j].get('year') for j in idx if people[j].get('year')]
    last=max(lasts) if lasts else (max(years) if years else None)
    if last is None: res.append({'name':p['name'],'homes':sorted(h for h in homes[k] if h),'last_year':None,'later_traditions_at_floor':0,'passes':False,'note':'no year: not counted'}); continue
    per={}
    for T,rows in shelf.items():
        if T in homes[k] or start[T]<=last: continue
        files={f for f,a in rows if not any(people[j].get('author') and a==people[j]['author'] for j in idx)}
        al={a.strip() for j in idx for a in people[j]['aliases_counted']}
        n=sum(sum(hits[f][a] for a in al) for f in files)
        if n>=FLOOR: per[T]=n
    res.append({'name':p['name'],'homes':sorted(h for h in homes[k] if h),'last_year':last,'aliases_counted':p['aliases_counted'],'later_traditions_at_floor':len(per),'passes':len(per)>=TRADS,'top':dict(sorted(per.items(),key=lambda x:-x[1])[:6])})
if False:
  for i,p in enumerate(people):
    last=p.get('last_year') or p.get('year') or 0
    per={}
    for T,rows in shelf.items():
        if T==p.get('movement') or start[T]<=last: continue
        files={f for f,a in rows if not (p.get('author') and a==p['author'])}
        n=sum(hits[f][i] for f in files)
        if n>=FLOOR: per[T]=n
    res.append({'name':p['name'],'movement':p.get('movement'),'year':p.get('year'),'last_year':p.get('last_year'),
                'aliases':p['aliases'],'later_traditions_at_floor':len(per),'passes':len(per)>=TRADS,
                'top':dict(sorted(per.items(),key=lambda x:-x[1])[:6])})
res.sort(key=lambda r:-r['later_traditions_at_floor'])
json.dump({'floor':FLOOR,'traditions':TRADS,'people':res},open(f'{S}/later_worlds_result.json','w'),indent=1,ensure_ascii=False)
ps=[r for r in res if r['passes']]
print(len(ps),'pass of',len(res))
for r in ps: print(r['later_traditions_at_floor'],r['name'],'|',r['homes'][:2],r['last_year'],'|',list(r['top'].items())[:2])
