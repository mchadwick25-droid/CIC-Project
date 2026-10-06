import json, glob, re, sys, collections
sys.path.insert(0, "/home/user/CIC-Project")
import engine.m7.standing_measure as sm
from engine.m4.grounding_net import _groundable_text
from engine.provider.bedrock import make_client, resolve_model_id, normalize_usage
from engine.m8.cost import estimate_cost
from engine.m8.price_tables import price_for_model
from concurrent.futures import ThreadPoolExecutor
S = "/tmp/claude-0/-home-user/c9d17cae-5e89-56a0-b8a6-23b7f4835de1/scratchpad"
SYSTEM = """You check one citation. You get a sentence and the text of the record it cites. Answer "carries" only if the record's text itself states or directly entails every specific claim in the sentence (people, places, dates, numbers, events, practices, teachings). Paraphrase and modern wording are fine. Answer "partly" if the record carries the core but the sentence adds any specific detail the record does not state. Answer "no" if the record does not carry the main claim. Use only the record text, never outside knowledge. Reply with one word: carries, partly or no."""
att = json.load(open(f"{S}/attach_out_v2.json"))
pairs = []
for f in glob.glob(f"{S}/uc/out/*.json"):
    w = json.load(open(f))["world"]; items = open(f"{S}/uc/items/{w}.md").read()
    sent = dict(re.findall(r"## (U\d+) .*?\n.*?\n- \*\*sentence:\*\* (.*)", items))
    recs = sm.load_world_records(w)
    for x in att[w]:
        if x.get("record_id"): pairs.append((w, x["id"], x["record_id"], sent[x["id"]], _groundable_text(recs[x["record_id"]])))
model = resolve_model_id("us.anthropic.claude-haiku-4-5", "us-east-1"); table = price_for_model(model); client = make_client("us-east-1")
print(json.dumps({"model": model, "max_tokens": 5, "pairs": len(pairs), "max_usd": float(sys.argv[1]), "system": SYSTEM}), flush=True)
def one(p):
    w, uid, rid, s, text = p
    import time, anthropic
    for attempt in range(6):
        try:
            r = client.messages.create(model=model, max_tokens=5, system=SYSTEM,
                                       messages=[{"role": "user", "content": f"Sentence: {s}\n\nRecord {rid}:\n{text}"}])
            break
        except anthropic.RateLimitError:
            time.sleep(2 ** attempt)
    else:
        raise RuntimeError("rate limited six times")
    return (w, uid, rid, r.content[0].text.strip().lower().strip(".")), estimate_cost(normalize_usage(r.usage), table).dollars
with ThreadPoolExecutor(2) as ex: res = list(ex.map(one, pairs))
print("spent", round(sum(c for _, c in res), 4))
json.dump([r for r, _ in res], open(f"{S}/verify_out.json", "w"), indent=1)
