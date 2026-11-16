import sys,json,urllib.request,urllib.parse,os,time
out=sys.argv[1]; ids=[l.strip() for l in open(sys.argv[2]) if l.strip()]
man={}
mp=os.path.join(out,'manifest.json')
if os.path.exists(mp): man=json.load(open(mp))
def get(u):
    for k in range(4):
        try:
            return urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'library-fetch/1.0'}),timeout=120).read()
        except Exception as e:
            err=e; time.sleep(3*(k+1))
    raise err
for i in ids:
    if i in man and man[i].get('match'): continue
    try:
        md=json.loads(get('https://archive.org/metadata/'+i))
        files=[f for f in md.get('files',[]) if f['name'].endswith('_djvu.txt')]
        m=md.get('metadata',{})
        rec=dict(title=m.get('title'),creator=m.get('creator'),date=m.get('date'),publisher=m.get('publisher'),language=m.get('language'),
                 rights=m.get('rights'),licenseurl=m.get('licenseurl'),pcs=m.get('possible-copyright-status'),collection=m.get('collection'),
                 access=m.get('access-restricted-item'),djvu=[(f['name'],f.get('size')) for f in files])
        if len(files)!=1: rec['match']=False; man[i]=rec; print(i,'DJVU FILES',len(files)); continue
        f=files[0]; raw=get('https://archive.org/download/%s/%s'%(i,urllib.parse.quote(f['name'])))
        open(os.path.join(out,i+'__'+f['name']),'wb').write(raw)
        rec['bytes']=len(raw); rec['match']=(str(len(raw))==str(f.get('size')))
        man[i]=rec; print(i,len(raw),f.get('size'),rec['match'],m.get('date'),m.get('licenseurl') or m.get('rights') or m.get('pcs') or '-')
    except Exception as e:
        man[i]=dict(error=str(e)); print(i,'ERROR',e)
    json.dump(man,open(mp,'w'),indent=1)
