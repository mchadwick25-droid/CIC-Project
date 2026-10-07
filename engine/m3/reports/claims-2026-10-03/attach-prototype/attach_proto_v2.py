"""Prototype: a Haiku 4.5 technical call that attaches a record id to each
uncited claim sentence, or none. Scored against the Opus diagnostic labels."""
import json, re, sys, glob
sys.path.insert(0, "/home/user/CIC-Project")
from engine.m1.registry import load_registry
from engine.provider.bedrock import make_client, resolve_model_id, normalize_usage
from engine.m8.cost import estimate_cost
from engine.m8.price_tables import price_for_model
S = "/tmp/claude-0/-home-user/c9d17cae-5e89-56a0-b8a6-23b7f4835de1/scratchpad"
INSTRUCTION = """You check citations for the Representative whose world is described above. Below are sentences it said without a citation. For each one, find the single record in the world above whose own text carries the sentence's specific claim, and give that record's id copied exactly from the list of valid ids at the end of these instructions (the same ids the world above shows inside [[...]]). Never build an id from a heading, a cell code or a title. Choose a record only when its text actually states or directly entails the claim; a record on the same topic that does not carry the claim is not enough. If no record carries the claim, answer null. Answer with JSON only: [{"id": "U01", "record_id": "world.type.slug" or null}, ...], one entry per sentence, nothing else."""
def main(max_usd):
    reg = load_registry(); region = "us-east-1"
    model = resolve_model_id("us.anthropic.claude-haiku-4-5", region)
    table = price_for_model(model)
    print(json.dumps({"model": model, "max_tokens": 2000, "temperature": "API default", "max_usd": max_usd, "worlds": 11, "instruction": INSTRUCTION}), flush=True)
    client = make_client(region); spent = 0.0; out = {}
    for f in sorted(glob.glob(f"{S}/uc/items/*.md")):
        w = f.split("/")[-1][:-3]
        if spent >= max_usd: print("STOP cap"); break
        text = open(f).read()
        items = re.findall(r"## (U\d+) .*?\n- preceding sentence: (.*)\n- \*\*sentence:\*\* (.*)", text)
        prompt = open(f"/home/user/CIC-Project/{reg[w]['package']['location']}/compiled/prompt.txt").read()
        valid = sorted(set(re.findall(r"\[\[([a-z0-9_.-]+)\]\]", prompt)))
        user = "\n".join(f'{i}: "{s}" (just before it: "{p}")' for i, p, s in items)
        resp = client.messages.create(model=model, max_tokens=2000,
            system=[{"type": "text", "text": prompt, "cache_control": {"type": "ephemeral"}}, {"type": "text", "text": INSTRUCTION + "\n\nValid ids:\n" + "\n".join(valid)}],
            messages=[{"role": "user", "content": user}])
        cost = estimate_cost(normalize_usage(resp.usage), table).dollars; spent += cost
        raw = resp.content[0].text; m = re.search(r"\[.*\]", raw, re.S)
        got = json.loads(m.group(0)) if m else []
        for g in got:
            if g.get("record_id") not in valid: g["rejected"] = g.get("record_id"); g["record_id"] = None
        out[w] = got
        print(w, len(items), f"usd {cost:.4f} spent {spent:.4f}", flush=True)
    json.dump(out, open(f"{S}/attach_out_v2.json", "w"), indent=1)
if __name__ == "__main__":
    main(float(sys.argv[1]))
