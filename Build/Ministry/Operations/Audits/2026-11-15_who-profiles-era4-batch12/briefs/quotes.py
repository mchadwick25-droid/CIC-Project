import json,re,glob,os,sys
B='/home/user/CIC-Project/Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era4/batch12/'
def norm(s): 
    s=s.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"')
    s=re.sub(r'-\s*\n\s*','',s); return re.sub(r'\s+',' ',s).lower()
bad=0
for cf in sorted(glob.glob(B+'*.card.json')):
    i=os.path.basename(cf)[:-10]; c=json.load(open(cf))
    files=set('/home/user/CIC-Project/'+s['file'] for s in c['sources']['ownWords']+c['sources']['about'])
    texts=[norm(open(f,errors='ignore').read()) for f in files if os.path.exists(f)]
    blob=open(B+i+'.brief.txt').read()+json.dumps(c,ensure_ascii=False).replace('\\"','"')
    for q in re.findall(r'"([^"]{6,})"',open(B+i+'.brief.txt').read())+re.findall(r'\\"(.{4,}?)\\"',json.dumps(c,ensure_ascii=False)):
        qq=norm(q).strip(' .,;')
        if not any(qq in t for t in texts): print('MISSING',i,'|',q); bad+=1
    for f in files:
        if not os.path.exists(f): print('NOFILE',i,f); bad+=1
print('bad',bad)
