#!/usr/bin/env python3
import json, sys, re, os
sys.path.insert(0, os.path.dirname(__file__)); import ia
ROM = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
def roman(n):
    out = ""
    for v, s in [(1000,"M"),(900,"CM"),(500,"D"),(400,"CD"),(100,"C"),(90,"XC"),(50,"L"),(40,"XL"),(10,"X"),(9,"IX"),(5,"V"),(4,"IV"),(1,"I")]:
        while n >= v: out += s; n -= v
    return out
SIGNS = re.compile(r"reprint|kessinger|forgotten books|nabu press|bibliolife|microfilms|facsimile|\b19[3-9]\d\b|\b20[0-2]\d\b", re.I)
for g in sys.argv[1:]:
  for p in json.load(open(f"{g}/picks.json")):
    i = p["ia_id"]; loc = f"{g}/dl/{i}_djvu.txt"
    d = json.loads(ia.get("https://archive.org/metadata/" + i)); m = d.get("metadata", {})
    fs = [f for f in d.get("files", []) if f["name"].endswith("_djvu.txt")]
    sz = os.path.getsize(loc); L = open(loc, encoding="utf-8", errors="replace").read().split("\n")
    y = str(p["imprint_year"]); head = "\n".join(L[:400])
    yfound = [k + 1 for k in range(min(400, len(L))) if re.search(r"\b" + y + r"\b", L[k]) or roman(int(y)) in L[k].replace(" ", "").replace(".", "")] if y.isdigit() else []
    flags = []
    if not fs or str(sz) != str(fs[0].get("size")): flags.append("SIZE")
    if not yfound: flags.append("YEAR-NOT-IN-OCR-HEAD")
    if y not in str(m.get("date", "")) : flags.append(f"HOSTDATE={m.get('date')}")
    for k in ("licenseurl", "rights", "access-restricted-item"):
        if k in m: flags.append(f"{k}={str(m[k])[:150]}")
    col = str(m.get("collection"))
    if re.search("inlibrary|printdisabled|internetarchivebooks", col): flags.append("LENDING-COLL")
    hits = [(k + 1, L[k].strip()[:70]) for k in list(range(0, min(300, len(L)))) + list(range(max(300, len(L) - 80), len(L))) if SIGNS.search(L[k]) and "funding" not in L[k] and "Digitized" not in L[k] and not re.search(y, L[k])]
    if hits: flags.append("SIGNS:" + str(hits[:5]))
    words = sum(len(x.split()) for x in L)
    print(f'{g} {p["row"]} | {i} | {y} at {yfound[:3]} | pcs={m.get("possible-copyright-status")} | {words}w | {p.get("imprint_read_at")[:60]} || ' + ("; ".join(flags) or "clean"))
