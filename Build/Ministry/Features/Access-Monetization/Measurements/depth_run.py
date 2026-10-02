import argparse, json, sys, time
from pathlib import Path
REPO = Path("/home/user/CIC-Project")
sys.path.insert(0, str(REPO))
from engine.m1.registry import load_registry
import engine.m4.turn as turn_mod
from engine.m4.turn import run_turn
from engine.m4.world_loader import LazyWorldLoader
from engine.m8.cost import estimate_cost
from engine.m8.live_cost_run import PRICE_TABLE_SOURCE, _price_for_call_kind
from engine.provider.bedrock import make_client, resolve_model_id

MESSAGES = [
    "I grew up in a church where nobody asked hard questions. Who was Jesus to your people, and how did they come to say it the way they did?",
    "When your community gathers for the Eucharist, what do you believe is actually happening? I would like to hear it the way you would explain it to someone who has never been there.",
    "You spoke about Jesus earlier. How does that connect to what you just said about the Eucharist, and where would someone like me begin if I wanted to understand it better?",
    "What would you say to someone who thinks all of this is just a story people tell to feel safe?",
    "How does a person actually join your community, and what is asked of them in the first year?",
    "What does your community believe happens to the soul after death, and how does that shape the way you live now?",
    "Who has the authority to teach in your community, and what happens when two teachers disagree?",
    "What is the hardest thing about holding to your faith in this time and place?",
    "How do you read scripture? Is there more than one way to understand a passage?",
    "Looking back on everything we have talked about, what is the one thing you most want me to understand?",
    "I want to push back on something. How do you know any of this is true and not just inherited habit?",
    "Tell me about a moment when your community was tested and held together.",
    "What do you wish people today understood about your world that they get wrong?",
    "If I came back in a year, what would you hope had changed in me?",
    "Is there anything you would want to ask me?",
]

ap = argparse.ArgumentParser()
ap.add_argument("--turns", type=int, required=True)
ap.add_argument("--region", required=True)
ap.add_argument("--world", default="alx")
ap.add_argument("--pause-after", type=int, default=0, help="turn index after which to pause")
ap.add_argument("--pause-seconds", type=int, default=0)
ap.add_argument("--out", required=True)
a = ap.parse_args()

turn_mod.SESSION_TURN_CAP = max(turn_mod.SESSION_TURN_CAP, a.turns)

registry = load_registry()
entry = registry[a.world]
world, _ = LazyWorldLoader().load(a.world, package_dir=REPO / entry["package"]["location"], expected_manifest_hash=entry["package"]["manifest_hash"])
voice_id = resolve_model_id("us.anthropic.claude-sonnet-4-5", a.region)
safety_id = resolve_model_id("us.anthropic.claude-haiku-4-5", a.region)
client = make_client(a.region)

msgs = MESSAGES[: a.turns]
print("SETTINGS", json.dumps({"voice_model": voice_id, "safety_model": safety_id, "region": a.region, "world": a.world,
    "turns": a.turns, "message_chars_total": sum(len(m) for m in msgs), "pause_after_turn": a.pause_after if a.pause_seconds else None,
    "pause_seconds": a.pause_seconds, "cap_override": turn_mod.SESSION_TURN_CAP, "price_source": PRICE_TABLE_SOURCE[:90]}, indent=1), flush=True)

history, rows = [], []
for i, m in enumerate(msgs):
    t0 = time.time()
    r = run_turn(session_id=f"depth-{a.world}", voice_client=client, voice_model_id=voice_id, safety_client=client, safety_model_id=safety_id,
        world=world, participant_message=m, pressed={}, anachronistic_term_ids=set(), history=history)
    dollars = sum(estimate_cost(rec.usage, _price_for_call_kind(rec.call_kind)).dollars for rec in r.usage_records)
    vr = [x for x in r.usage_records if x.call_kind == "voice_generation"]
    u = vr[0].usage if vr else None
    text = (r.voice_event or {}).get("text") or ""
    rows.append({"turn": i + 1, "message": m, "reply": text, "routing": r.routing_action, "dollars": dollars,
        "history_messages_sent": len(history),
        "in_tokens": u.input_tokens if u else None, "cache_read": u.cache_read_input_tokens if u else None,
        "cache_write": u.cache_creation_input_tokens if u else None, "out_tokens": u.output_tokens if u else None,
        "seconds": round(time.time() - t0, 1),
        "facilitator": [e.get("text") for e in r.facilitator_events if e.get("text")]})
    print("TURN", i + 1, r.routing_action, round(dollars, 4), rows[-1]["in_tokens"], rows[-1]["cache_read"], rows[-1]["cache_write"], flush=True)
    history = [*history, {"role": "user", "content": m}, {"role": "assistant", "content": text}]
    if a.pause_seconds and i == a.pause_after:
        time.sleep(a.pause_seconds)
Path(a.out).write_text(json.dumps({"world": a.world, "voice_model": voice_id, "rows": rows, "total_dollars": sum(x["dollars"] for x in rows)}, indent=1))
print("TOTAL", round(sum(x["dollars"] for x in rows), 4))
