#!/usr/bin/env python3
"""archive.org helper. Usage:
  ia.py search '<lucene query>' [rows]      -> id | year | title | creator | lang
  ia.py meta <id>                           -> key metadata + djvu.txt file name/size
  ia.py fetch <id> <outdir>                 -> downloads <id>'s djvu.txt, checks byte count
  ia.py page <id> <leaf> <outfile.jpg>      -> downloads one page image
"""
import sys, json, os, urllib.request, urllib.parse, time
UA = {"User-Agent": "Mozilla/5.0 (library research client)"}
def get(url, tries=4):
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120) as r:
                return r.read()
        except Exception as e:
            err = e; time.sleep(3*(i+1))
    raise err
def search(q, rows=25):
    p = urllib.parse.urlencode([("q", q + " AND mediatype:texts"), ("fl[]", "identifier"), ("fl[]", "year"), ("fl[]", "title"), ("fl[]", "creator"), ("fl[]", "language"), ("rows", rows), ("output", "json")])
    d = json.loads(get("https://archive.org/advancedsearch.php?" + p))
    for x in d["response"]["docs"]:
        t = x.get("title", ""); t = t if isinstance(t, str) else "; ".join(t)
        c = x.get("creator", ""); c = c if isinstance(c, str) else "; ".join(c)
        print(f'{x["identifier"]} | {x.get("year","")} | {t[:110]} | {c[:60]} | {x.get("language","")}')
    print(f'-- {d["response"]["numFound"]} found')
def meta(i):
    d = json.loads(get("https://archive.org/metadata/" + i))
    m = d.get("metadata", {})
    for k in ("title", "creator", "publisher", "date", "year", "language", "possible-copyright-status", "licenseurl", "rights", "access-restricted-item", "collection", "volume", "contributor", "description"):
        if k in m: print(f"{k}: {str(m[k])[:400]}")
    for f in d.get("files", []):
        if f["name"].endswith("_djvu.txt"): print(f'DJVU: {f["name"]} size={f.get("size")}')
    return d
def fetch(i, out):
    d = json.loads(get("https://archive.org/metadata/" + i))
    fs = [f for f in d.get("files", []) if f["name"].endswith("_djvu.txt")]
    if not fs: print("NO djvu.txt"); sys.exit(1)
    f = fs[0]; os.makedirs(out, exist_ok=True)
    b = get("https://archive.org/download/" + i + "/" + urllib.parse.quote(f["name"]))
    p = os.path.join(out, i + "_djvu.txt"); open(p, "wb").write(b)
    print(f'{p} bytes={len(b)} listed={f.get("size")} match={str(len(b))==str(f.get("size"))}')
def page(i, leaf, out):
    open(out, "wb").write(get(f"https://archive.org/download/{i}/page/n{leaf}.jpg")); print(out)
if __name__ == "__main__":
    a = sys.argv
    if a[1] == "search": search(a[2], int(a[3]) if len(a) > 3 else 25)
    elif a[1] == "meta": meta(a[2])
    elif a[1] == "fetch": fetch(a[2], a[3])
    elif a[1] == "page": page(a[2], a[3], a[4])
