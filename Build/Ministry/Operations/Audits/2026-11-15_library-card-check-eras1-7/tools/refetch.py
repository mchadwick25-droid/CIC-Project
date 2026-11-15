"""refetch.py <id> [<id>...] : own download of each djvu.txt into S/dl/<id>__<name>, byte check, show imprint lines."""
import sys, json, os, re, urllib.request, urllib.parse, time
S = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA = {"User-Agent": "Mozilla/5.0 (library research client)"}
def get(url, tries=4):
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=180) as r: return r.read()
        except Exception as e: err = e; time.sleep(3*(i+1))
    raise err
os.makedirs(S + "/dl", exist_ok=True)
man_p = S + "/dl/manifest.json"
man = json.load(open(man_p)) if os.path.exists(man_p) else {}
pat = re.compile(r"\b(1[5-9]\d\d)\b|M\.? ?D\.? ?C+|MDCC|M ?DCCC|MCM")
for i in sys.argv[1:]:
    d = json.loads(get("https://archive.org/metadata/" + i)); m = d.get("metadata", {})
    fs = [f for f in d.get("files", []) if f["name"].endswith("_djvu.txt")]
    if not fs: print("##", i, "NO DJVU"); continue
    f = fs[0]; p = S + "/dl/" + i + "__" + f["name"].replace("/", "_")
    if not (os.path.exists(p) and os.path.getsize(p) == int(f["size"])):
        open(p, "wb").write(get("https://archive.org/download/" + i + "/" + urllib.parse.quote(f["name"])))
    n = os.path.getsize(p); ok = n == int(f["size"])
    R = {k: m.get(k, "absent") for k in ("possible-copyright-status", "licenseurl", "rights", "access-restricted-item")}
    man[i] = dict(path=p, djvu=f["name"], bytes=n, match=ok, rights=R, date=m.get("date"), title=str(m.get("title"))[:200], collection=m.get("collection"))
    L = open(p, encoding="utf8", errors="replace").read().split("\n")
    print("##", i, n, "match=%s" % ok, "| host date", m.get("date"), "|", json.dumps(R)[:230], "| lines", len(L))
    shown = 0
    for k, l in enumerate(L[:500]):
        if pat.search(l) and len(l.strip()) < 90:
            print("   %d: %s" % (k+1, " / ".join(x.strip() for x in L[max(0,k-2):k+1] if x.strip())[:200])); shown += 1
            if shown >= 6: break
    tail = [x.strip() for x in L[-400:] if x.strip()][-3:]
    print("   END:", " / ".join(tail)[:200])
json.dump(man, open(man_p, "w"), indent=1)
