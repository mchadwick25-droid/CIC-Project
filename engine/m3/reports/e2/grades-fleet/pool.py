import json, glob, sys
sys.path.insert(0, "/home/user/CIC-Project")
from engine.m7.standing_measure import quote_aware_sentences
R = "/home/user/CIC-Project/engine/m3/reports/e2"
def pooled():
    rows = {}
    for f in sorted(glob.glob(f"{R}/fleet/e2-pair-*.json")):
        for w, rs in json.load(open(f))["worlds"].items():
            for r in rs:
                if r["arms"]: rows.setdefault(w, {})[r["probe_id"]] = {"off": r["arms"]["off"], "records_only": r["arms"]["records_only"]}
    A = json.load(open(f"{R}/e2-sample-hal-rzg-2026-10-03.json")); B = json.load(open(f"{R}/e2-records-only-hal-rzg-2026-10-03.json"))
    for w in ("hal", "rzg"):
        b = {r["probe_id"]: r for r in B["worlds"][w]}
        for r in A["worlds"][w]:
            if r["arms"]: rows.setdefault(w, {})[r["probe_id"]] = {"off": r["arms"]["off"], "records_only": b[r["probe_id"]]["arms"]["records_only"]}
    return rows
if __name__ == "__main__":
    rows = pooled(); tot = {"off": [0, 0, 0], "records_only": [0, 0, 0]}
    for w in sorted(rows):
        line = f"{w:12s} n={len(rows[w]):2d} "
        for a in ("off", "records_only"):
            u = sum(len(p[a]["uncited_claim_sentences"]) for p in rows[w].values())
            s = sum(len(quote_aware_sentences(p[a]["answer_text"])) for p in rows[w].values())
            wd = sum(len(p[a]["answer_text"].split()) for p in rows[w].values())
            t = tot[a]; t[0] += u; t[1] += s; t[2] += wd
            line += f"| {a} uncited {u/s:5.1%} words {wd/len(rows[w]):4.0f} "
        print(line)
    n = sum(len(v) for v in rows.values())
    print("FLEET", n, "probes", " ".join(f"| {a} uncited {t[0]/t[1]:5.1%} words {t[2]/n:4.0f}" for a, t in tot.items()))
