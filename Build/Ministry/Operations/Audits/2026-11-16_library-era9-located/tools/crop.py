import sys,urllib.request,io
from PIL import Image
ident,n,top,bot,out=sys.argv[1],int(sys.argv[2]),float(sys.argv[3]),float(sys.argv[4]),sys.argv[5]
w=sys.argv[6] if len(sys.argv)>6 else '1400'
u='https://archive.org/download/%s/page/n%d_w%s.jpg'%(ident,n,w)
d=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'library-fetch/1.0'}),timeout=120).read()
im=Image.open(io.BytesIO(d)).convert('RGB'); W,H=im.size
im=im.crop((0,int(H*top),W,int(H*bot))); im.thumbnail((1100,1100)); im.save(out,quality=85)
