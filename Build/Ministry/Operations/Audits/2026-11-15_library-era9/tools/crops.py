#!/usr/bin/env python3
"""crops.py <out.jpg> id:leaf ... : bottom 45% of each leaf, side by side in a grid of 3 columns, labeled by order."""
import sys, io, os
sys.path.insert(0, os.path.dirname(__file__)); import ia
from PIL import Image, ImageDraw
out = sys.argv[1]; ims = []
for a in sys.argv[2:]:
    i, k = a.rsplit(":", 1)
    try:
        im = Image.open(io.BytesIO(ia.get(f"https://archive.org/download/{i}/page/n{k}_w700.jpg", tries=2))).convert("L")
        w, h = im.size; im = im.crop((0, int(h * 0.55), w, h)).resize((640, int(640 * (h * 0.45) / w)))
        ImageDraw.Draw(im).text((5, 5), f"{len(ims)+1}: {i[:30]} n{k}", fill=0); ims.append(im)
    except Exception as e: print("fail", a, e)
H = max(x.size[1] for x in ims); cols = 3; rows = (len(ims) + 2) // 3
s = Image.new("L", (cols * 640, rows * H), 255)
for n, im in enumerate(ims): s.paste(im, ((n % 3) * 640, (n // 3) * H))
s.save(out, quality=75); print(out, len(ims))
