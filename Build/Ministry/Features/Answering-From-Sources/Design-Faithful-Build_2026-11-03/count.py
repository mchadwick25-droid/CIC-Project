import yaml,json,glob,os,collections,re,sys
sys.path.insert(0,'/home/user/CIC-Project')
R='/home/user/CIC-Project/'
T=R+'Build/Ministry/Features/Answering-From-Sources/Cross-World-Test_2026-11-02/'
sc={'lpc':R+'Build/worlds/lpc/build/lpc_Answers_Sidecar.yaml'}
for w in('alx','syr','rzg'): sc[w]=f'{T}{w}/{w}_Answers_Sidecar.yaml'
MAP={"doctrinal_witness","term","story","quote","gravity","force","contested_claim","figure","honest_limit"}
out={}
for w in('lpc','alx','syr','rzg'):
    s=yaml.safe_load(open(sc[w]))['subquestions']
    pk=sorted(glob.glob(R+f'packages/{w}/*/compiled/repository.json'))[-1]
    repo={r['id']:r for r in json.load(open(pk))['records']}
    status={}
    for f in glob.glob(R+f'records/{w}/*/*.md'):
        t=open(f).read().split('---')[1]; d=yaml.safe_load(t); status[d['id']]=d.get('status')
    seed=yaml.safe_load(open(R+f'Build/worlds/{w}/build/{w}_Passage_Seeds.yaml'))
    sq=seed['subquestions']
    rec_side=set();rec_held=set();rec_ready=set()
    for sid,e in s.items():
        ids=e.get('records') or []
        if ids: rec_side.add(sid)
        if any(repo.get(i,{}).get('record_type') in MAP for i in ids): rec_held.add(sid)
        if any(repo.get(i,{}).get('record_type') in MAP and status.get(i,'ready')=='ready' for i in ids): rec_ready.add(sid)
    usable=set();fl=set();tot=0;u=0;f_=0;vo=0;et=0;uvo=0;uet=0
    fileonly=collections.defaultdict(lambda:[0,set()])
    bind=collections.Counter()
    for sid,e in sq.items():
        ss=e.get('seeds') or []
        us=[x for x in ss if str(x.get('shelf_binding') or '').startswith('row narrowed')]
        for x in ss:
            tot+=1; b=str(x.get('shelf_binding')); bind[b[:40]]+=1
            isu=x in us
            if isu:u+=1
            else:
                f_+=1; fileonly[x['file']][0]+=1; fileonly[x['file']][1].add(sid)
            if x.get('voice')=='voiceable': vo+=1; uvo+=isu
            else: et+=1; uet+=isu
        if us: usable.add(sid)
        elif ss: fl.add(sid)
    allq=set(s)|set(sq)
    neither=[q for q in allq if q not in rec_held and q not in usable]
    out[w]=dict(n=len(allq),sidecar_n=len(s),seed_n=len(sq),rec_sidecar=len(rec_side),rec_held=len(rec_held),rec_ready=len(rec_ready),usable_sq=len(usable),fileonly_sq=len(fl),neither=len(neither),both=len(rec_held&usable),seeds=tot,usable=u,fileonly=f_,vo=vo,et=et,uvo=uvo,uet=uet,pkg=pk.split('/')[2],bind=dict(bind),draft_in_sidecar=sum(1 for e in s.values() for i in (e.get('records') or []) if status.get(i)=='draft'),unheld=sum(1 for e in s.values() for i in (e.get('records') or []) if i not in repo))
    out[w]['_fileonly']={k:(v[0],sorted(v[1])) for k,v in fileonly.items()}
    out[w]['_seedkeys']=sorted(set(k for e in sq.values() for x in (e.get('seeds') or []) for k in x))
for w,o in out.items():
    print(w,{k:v for k,v in o.items() if not k.startswith('_')})
json.dump(out,open(R and '/tmp/claude-0/-home-user-CIC-Project/f598af84-ac3a-5cc1-8063-e51943cacaa7/scratchpad/step1/counts.json','w'),indent=1,default=list)
for w in('alx','syr'):
    print(w)
    for k,v in sorted(out[w]['_fileonly'].items()): print(' ',v[0],k,v[1])
print(out['syr']['_seedkeys'])
