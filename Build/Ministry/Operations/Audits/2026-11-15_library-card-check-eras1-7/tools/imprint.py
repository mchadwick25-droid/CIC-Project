"""imprint.py <id> <leaf> [<leaf>...] : fetch leaves, crop bottom 30%, stack into img/<id>_imp.jpg"""
import sys, urllib.request, io, os
from PIL import Image
S = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
i = sys.argv[1]; crops = []
for l in sys.argv[2:]:
    b = urllib.request.urlopen(urllib.request.Request(f"https://archive.org/download/{i}/page/n{l}.jpg", headers={"User-Agent": "Mozilla/5.0"}), timeout=90).read()
    im = Image.open(io.BytesIO(b)).convert("L"); w, h = im.size
    c = im.crop((0, int(h*0.68), w, h)); c = c.resize((640, int(640*c.size[1]/w))); crops.append(c)
H = sum(c.size[1] for c in crops); out = Image.new("L", (640, H)); y = 0
for c in crops: out.paste(c, (0, y)); y += c.size[1]
p = f"{S}/img/{i}_imp.jpg"; out.save(p, quality=55); print(p)
