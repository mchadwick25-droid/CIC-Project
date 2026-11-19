import sys,urllib.request,io,time
from PIL import Image,ImageDraw
from concurrent.futures import ThreadPoolExecutor
out=sys.argv[1]; items=[a.split(':') for a in sys.argv[2:]]
def get(a):
    ident,n=a[0],a[1]
    u='https://archive.org/download/%s/page/n%s_w300.jpg'%(ident,n)
    for k in range(3):
        try:
            d=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'library-fetch/1.0'}),timeout=90).read()
            im=Image.open(io.BytesIO(d)).convert('RGB'); im.thumbnail((300,460)); return im
        except Exception as e: time.sleep(3)
    return Image.new('RGB',(300,460),'gray')
with ThreadPoolExecutor(6) as ex: ims=list(ex.map(get,items))
cols=6; rows=(len(ims)+cols-1)//cols
sh=Image.new('RGB',(300*cols,480*rows),'white'); dr=ImageDraw.Draw(sh)
for i,(a,im) in enumerate(zip(items,ims)):
    x,y=(i%cols)*300,(i//cols)*480; sh.paste(im,(x,y+18)); dr.text((x+4,y+2),a[2] if len(a)>2 else a[0][-22:],fill='red')
sh.save(out,quality=80)
