# usage: python3 -I leaves.py <ident>   -> prints leaf count and leaves typed Title/Cover, as n-indexes for crop.py
import sys,re,urllib.request,json
i=sys.argv[1]
def get(u):
    return urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'library-fetch/1.0'}),timeout=90).read()
m=json.loads(get('https://archive.org/metadata/%s'%i))
names=[f['name'] for f in m.get('files',[])]
sd=[n for n in names if n.endswith('_scandata.xml') or n=='scandata.xml']
print('title:',str(m.get('metadata',{}).get('title'))[:100],'| host date:',m.get('metadata',{}).get('date'),'| volume:',m.get('metadata',{}).get('volume'))
if not sd: print('no scandata; try leaves n1..n12 by hand'); sys.exit()
x=get('https://archive.org/download/%s/%s'%(i,sd[0])).decode('utf8','replace')
pages=re.findall(r'<page leafNum="(\d+)">(.*?)</page>',x,flags=re.S)
acc=[(int(l),b) for l,b in pages if 'addToAccessFormats>true' in b or 'addToAccessFormats' not in b]
print('leaves:',len(pages),'shown:',len(acc))
for n,(l,b) in enumerate(acc):
    t=re.search(r'<pageType>(.*?)</pageType>',b); t=t.group(1) if t else ''
    if t in('Title','Title Page','Cover') or n<1: print('  n=%d leaf=%d type=%s'%(n,l,t))
