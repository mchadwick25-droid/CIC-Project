import json, sys
from pathlib import Path
REPO = Path("/home/user/CIC-Project"); sys.path.insert(0, str(REPO))
from engine.m1.registry import load_registry
from engine.m4.turn import run_turn
from engine.m4.world_loader import LazyWorldLoader
from engine.m8.cost import estimate_cost
from engine.m8.live_cost_run import _price_for_call_kind
from engine.provider.bedrock import make_client, resolve_model_id
region, world_key = "us-east-1", "alx"
A = "I grew up in a church where nobody asked hard questions. Who was Jesus to your people, and how did they come to say it the way they did?"
B = "Who was Jesus to your people, and how did they come to say it the way they did?"
C = "I grew up in a church where nobody asked hard questions. I would like to understand who Jesus was to your people."
cases = [("A1 original", A), ("A2 original", A), ("B1 no opener", B), ("B2 no opener", B), ("C1 opener, no question mark", C), ("C2 opener, no question mark", C)]
reg = load_registry(); e = reg[world_key]
world, _ = LazyWorldLoader().load(world_key, package_dir=REPO / e["package"]["location"], expected_manifest_hash=e["package"]["manifest_hash"])
v, s = resolve_model_id("us.anthropic.claude-sonnet-4-5", region), resolve_model_id("us.anthropic.claude-haiku-4-5", region)
c = make_client(region)
print("SETTINGS", json.dumps({"voice": v, "safety": s, "region": region, "world": world_key, "calls": len(cases), "turn_1_only": True, "chars": sum(len(x[1]) for x in cases)}), flush=True)
out = []
for label, msg in cases:
    r = run_turn(session_id="probe-"+label.split()[0], voice_client=c, voice_model_id=v, safety_client=c, safety_model_id=s, world=world,
                 participant_message=msg, pressed={}, anachronistic_term_ids=set(), history=[])
    d = sum(estimate_cost(x.usage, _price_for_call_kind(x.call_kind)).dollars for x in r.usage_records)
    t = (r.voice_event or {}).get("text") or ""
    out.append({"case": label, "message": msg, "routing": r.routing_action, "dollars": d, "reply_start": t[:400]})
    print("CASE", label, r.routing_action, round(d, 4), "|", t[:160].replace("\n", " "), flush=True)
Path("probe_restate.json").write_text(json.dumps(out, indent=1))
print("TOTAL", round(sum(x["dollars"] for x in out), 4))
