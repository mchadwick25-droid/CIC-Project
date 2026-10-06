import json, glob, collections
import pathlib; D = str(pathlib.Path(__file__).parent)
idx = json.load(open(f"{D}/index.json"))
want = {e["reply"]: e["sentences"] for e in idx["replies"]}
prim = {}
for f in glob.glob(f"{D}/primary/*.json"):
    for r in json.load(open(f))["replies"]:
        prim[r["reply"]] = {s["s"]: s for s in r["sentences"]}
problems = [r for r, n in want.items() if r not in prim or sorted(prim[r]) != list(range(1, n + 1))]
print("coverage problems:", problems)
LABELS = ["no_claim", "supported", "stretched", "unsupported", "uncited"]
byw = collections.defaultdict(collections.Counter)
for r, ss in prim.items():
    for s in ss.values(): byw[r.split(":")[0]][s["label"]] += 1
tot = sum(byw.values(), collections.Counter())
def row(name, c):
    claims = sum(c[l] for l in LABELS[1:])
    u = c["unsupported"] / claims if claims else 0
    us = (c["unsupported"] + c["uncited"]) / claims if claims else 0
    st = c["stretched"] / claims if claims else 0
    print(f"{name:12s} " + " ".join(f"{c[l]:4d}" for l in LABELS) + f"   claims {claims:4d}  unsupported {u:6.1%}  +uncited {us:6.1%}  stretched {st:6.1%}")
print(" " * 13 + " ".join(f"{l[:4]:>4s}" for l in LABELS))
for w in sorted(byw): row(w, byw[w])
row("FLEET", tot)
sec = {r["reply"]: {s["s"]: s for s in r["sentences"]} for r in json.load(open(f"{D}/second.json"))["replies"]}
agree = n = 0; conf = collections.Counter(); claimagree = claimn = 0
for r, ss in sec.items():
    for k, s in ss.items():
        a, b = prim[r][k]["label"], s["label"]; n += 1; agree += a == b; conf[(a, b)] += 1
        if a != "no_claim" or b != "no_claim":
            claimn += 1; claimagree += a == b
print(f"\nagreement all sentences {agree}/{n} = {agree/n:.1%}; on sentences either grader saw a claim {claimagree}/{claimn} = {claimagree/claimn:.1%}")
coarse = lambda l: "ok" if l in ("no_claim", "supported") else "flag"
ca = sum(coarse(prim[r][k]["label"]) == coarse(s["label"]) for r, ss in sec.items() for k, s in ss.items())
print(f"agreement on ok-vs-flag: {ca}/{n} = {ca/n:.1%}")
for (a, b), c in sorted(conf.items(), key=lambda x: -x[1]):
    if a != b: print(f"  primary {a:11s} second {b:11s} {c}")
