import json, os, sys
S = sys.argv[1]; out = sys.argv[2]
man = json.load(open(S + "/dl/manifest.json"))
rows = []
for d in ("A", "B", "C", "E5a", "E5b", "E6a", "E6b", "E7a", "E7b"):
    p = S + "/" + d + "/picks.json"
    if not os.path.exists(p): continue
    for x in json.load(open(p)):
        i = x.get("ia_id"); m = man.get(i, {})
        x["searcher"] = d
        x.pop("local", None)
        x["library_thread_refetch"] = {"djvu": m.get("djvu"), "bytes": m.get("bytes"), "match": m.get("match"), "host_rights": m.get("rights"), "host_date": m.get("date")} if m else None
        rows.append(x)
for i in ("patrologiaorient10pariuoft", "nestorianmonumen00legg"):
    m = man[i]; rows.append({"searcher": "library thread", "ia_id": i, "library_thread_refetch": {"djvu": m["djvu"], "bytes": m["bytes"], "match": m["match"], "host_rights": m["rights"], "host_date": m["date"]}})
json.dump(rows, open(out, "w"), indent=1, ensure_ascii=False)
print(len(rows), "rows;", sum(1 for r in rows if r["library_thread_refetch"]), "refetched")
