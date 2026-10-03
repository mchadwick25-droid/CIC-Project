import json, glob, sys, random
sys.path.insert(0, "/home/user/CIC-Project")
import engine.m7.standing_measure as sm
from engine.m7.standing_measure import quote_aware_sentences
import pathlib; OUT = str(pathlib.Path(__file__).parent)
WORLDS = "alx cappadocian desert don gallic hal ijc pahc rzg syr witt".split()
rng = random.Random(20261003)
index = []
for w in WORLDS:
    d = json.load(open(glob.glob(f"engine/m3/reports/confirm709-2026-10-03/*-{w}-*.json")[0]))
    _, probes = sm._only_world(d)
    recs = sm.load_world_records(w)
    picks = rng.sample(sorted(probes, key=lambda p: p["probe_id"]), 3)
    md = [f"# Claim-support packet: world {w}\n"]
    for p in picks:
        t = p["transcript"]
        cites = {}
        for e in t.get("citation_entries") or []:
            cites.setdefault(e["sentence"].strip(), []).extend(e["record_ids"])
        sents = quote_aware_sentences(t["answer_text"])
        rid = f"{w}:{p['probe_id']}"
        index.append({"reply": rid, "world": w, "probe_id": p["probe_id"], "sentences": len(sents)})
        md.append(f"\n## Reply {rid}\n\nThe question is not shown (sealed). Full reply as the participant saw it:\n\n> " + t["answer_text"].replace("\n", "\n> ") + "\n\n### Sentences and the records each one cites\n")
        used = []
        for i, s in enumerate(sents, 1):
            ids = cites.get(s.strip(), [])
            used += [x for x in ids if x not in used]
            md.append(f"- **S{i}** {s}\n  - cites: {', '.join(ids) if ids else '(none)'}")
        md.append("\n### Full text of every cited record\n")
        for x in used:
            r = recs.get(x)
            md.append(f"#### {x}\n```json\n{json.dumps(r, indent=1, ensure_ascii=False) if r else 'NOT A RECORD IN THIS WORLD'}\n```")
    open(f"{OUT}/packets/{w}.md", "w").write("\n".join(md) + "\n")
second = rng.sample([e["reply"] for e in index], 7)
json.dump({"replies": index, "second_grader_replies": sorted(second), "seed": 20261003}, open(f"{OUT}/index.json", "w"), indent=1)
print(sum(e["sentences"] for e in index), "sentences;", sorted(second))
