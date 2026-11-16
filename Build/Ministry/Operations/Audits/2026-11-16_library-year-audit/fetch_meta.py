import json,urllib.request,concurrent.futures,time,os
rows=json.load(open("rows.json")); ids=sorted({r["ident"] for r in rows if r["ident"]})
out=json.load(open("meta.json")) if os.path.exists("meta.json") else {}
def get(i):
    for t in range(4):
        try:
            d=json.load(urllib.request.urlopen(urllib.request.Request("https://archive.org/metadata/%s/metadata"%i,headers={"User-Agent":"library-fetch/1.0"}),timeout=60))
            r=d.get("result") or {}
            return i,{k:r.get(k) for k in ("date","year","publicdate","title","publisher","volume","issue","possible-copyright-status","licenseurl","rights")} if r else {"missing":True}
        except Exception as e:
            err=str(e); time.sleep(3*(t+1))
    return i,{"error":err}
todo=[i for i in ids if i not in out or "error" in out[i]]
print(len(ids),len(todo),flush=True)
with concurrent.futures.ThreadPoolExecutor(4) as ex:
    for n,(i,m) in enumerate(ex.map(get,todo)):
        out[i]=m
        if n%200==0: json.dump(out,open("meta.json","w")); print(n,flush=True)
json.dump(out,open("meta.json","w")); print("done",sum(1 for v in out.values() if "error" in v),sum(1 for v in out.values() if v.get("missing")))
