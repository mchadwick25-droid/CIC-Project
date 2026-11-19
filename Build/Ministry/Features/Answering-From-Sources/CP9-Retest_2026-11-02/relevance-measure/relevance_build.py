import sys,json,yaml,re
sys.path[:0]=['/home/user/CIC-Project/Sandbox/answering-library','/home/user/CIC-Project']
from index import retrieve
from engine.m1.loader import load_world_records
S='/tmp/claude-0/-home-user-CIC-Project/f598af84-ac3a-5cc1-8063-e51943cacaa7/scratchpad'
DB={'lpc':f'{S}/lpcbuild/lpc.sqlite','rzg':f'{S}/build_rzg/rzg.sqlite'}
for w in ('lpc','rzg'):
    recs=load_world_records(w)
    sc=yaml.safe_load(open(f'/home/user/CIC-Project/Build/worlds/{w}/build/{w}_Answers_Sidecar.yaml' if w=='lpc' else f'{S}/cp9/sidecars/{w}_Answers_Sidecar.yaml'))['subquestions']
    seed=yaml.safe_load(open(f'{S}/seed_{w}.yaml'))['subquestions']
    items=json.load(open(f'{S}/cp9/rate_{w}_items.json'))
    ques={i['id'].split('-')[0]:i['question'] for i in items}
    out=[]
    for i in range(1,29):
        q=f'q{i:03d}'; a=json.load(open(f'{S}/cp9/{w}/C/answers/{q}.json')); s=a.get('sub_question')
        if not s or s not in sc: continue
        words=[sc[s]['label']]
        for rid in sc[s].get('records',[]):
            rw=(recs.get(rid,{}).get('retrieval') or {}).get('retrieve_when') or []
            words+= [x for x in rw if isinstance(x,str)]
        query=' '.join(words)
        seeded={x['passage_id'] for x in (seed.get(s,{}).get('seeds') or [])}
        hits=retrieve.search(DB[w],query,world=w,roles=['tradition'],min_ocr=0.7,limit=60)
        chosen=[]
        for h in hits:
            src=h.source
            if h.passage_id in seeded or src['language']!='eng' or src['apparatus']: continue
            explicit=[r for r in src['rows'] if r.get('world')==w]
            # lens: the passage has its own (narrowed) row, not just a file-level shelf entry
            import sqlite3
            c=sqlite3.connect(DB[w]); n=c.execute("select count(*) from passage_rows where passage_id=? and world=?",(h.passage_id,w)).fetchone()[0]; c.close()
            if n==0: continue
            chosen.append(h)
            if len(chosen)==3: break
        for n,h in enumerate(chosen):
            out.append({'id':f'{q}-p{n+1}','question':ques[q],'sub_question':s,'sub_question_label':sc[s]['label'],'passage_id':h.passage_id,'passage':' '.join(h.text.split()[:170])})
    json.dump(out,open(f'{S}/cp9/relevance_{w}_items.json','w'),ensure_ascii=False,indent=1)
    print(w,len(out),'items over',len({o['id'].split('-')[0] for o in out}),'questions')
