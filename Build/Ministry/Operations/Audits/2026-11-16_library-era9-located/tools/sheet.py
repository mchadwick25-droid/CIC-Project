import sys,urllib.request,io,time
from PIL import Image
ident,a,b,out=sys.argv[1],int(sys.argv[2]),int(sys.argv[3]),sys.argv[4]
ims=[]
for n in range(a,b+1):
    u='https://archive.org/download/%s/page/n%d_w260.jpg'%(ident,n)
    for k in range(3):
        try:
            d=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'library-fetch/1.0'}),timeout=90).read(); break
        except Exception as e: d=None; time.sleep(3)
    if d is None: continue
    im=Image.open(io.BytesIO(d)).convert('RGB'); im.thumbnail((260,420)); ims.append((n,im))
from PIL import ImageDraw
W=260*len(ims); sh=Image.new('RGB',(W,440),'white'); dr=ImageDraw.Draw(sh)
for i,(n,im) in enumerate(ims):
    sh.paste(im,(i*260,20)); dr.text((i*260+5,2),'n%d'%n,fill='red')
sh.save(out,quality=80)
