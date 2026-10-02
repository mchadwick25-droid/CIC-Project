import json, os, sys, time
from pathlib import Path
S = Path("/tmp/claude-0/-home-user-CIC-Project/a40ae112-c813-5159-a0ca-b337b35041ea/scratchpad")
os.environ.update({
    "CIC_API_REGION": "us-east-1", "CIC_ENFORCE_ADMISSION": "1", "CIC_SELF_REVISION": "0",
    "CIC_API_EVENTS_DB": str(S / "live_events.db"), "CIC_API_USAGE_DB": str(S / "live_usage.db"),
})
sys.path.insert(0, "/home/user/CIC-Project")
from fastapi.testclient import TestClient
from engine.api.app import app

MESSAGES = [
    "I grew up in a church where nobody asked hard questions. Who was Jesus to your people, and how did they come to say it the way they did?",
    "When your community gathers for the Eucharist, what do you believe is actually happening? I would like to hear it the way you would explain it to someone who has never been there.",
    "You spoke about Jesus earlier. How does that connect to what you just said about the Eucharist, and where would someone like me begin if I wanted to understand it better?",
    "What would you say to someone who thinks all of this is just a story people tell to feel safe?",
    "How does a person actually join your community, and what is asked of them in the first year?",
    "What does your community believe happens to the soul after death, and how does that shape the way you live now?",
    "Who has the authority to teach in your community, and what happens when two teachers disagree?",
]
print("SETTINGS", json.dumps({"path": "real FastAPI app via POST /api/session and /message", "world": "alx", "turns": len(MESSAGES),
    "region": "us-east-1", "admission": "enforced (as deployed)", "self_revision": "0 (as deployed)", "streaming": "off (as deployed)"}), flush=True)
out = []
with TestClient(app) as c:
    r = c.post("/api/session", json={"world_key": "alx"})
    print("SESSION", r.status_code, flush=True)
    r.raise_for_status()
    sid, code = r.json()["session_id"], r.json()["session_code"]
    h = {"Authorization": f"Session {code}"}
    for i, m in enumerate(MESSAGES):
        t0 = time.time()
        resp = c.post(f"/api/session/{sid}/message", json={"text": m}, headers=h)
        dt = round(time.time() - t0, 1)
        body = resp.json() if resp.headers.get("content-type", "").startswith("application/json") else {"raw": resp.text[:300]}
        out.append({"turn": i + 1, "status": resp.status_code, "seconds": dt, "message": m, "response": body})
        v = (body.get("voice") or {}) if isinstance(body, dict) else {}
        print("TURN", i + 1, resp.status_code, dt, body.get("routing_action"), "citations", len(v.get("citations") or []), "words", len((v.get("text") or "").split()), flush=True)
    tr = c.get(f"/api/session/{sid}/transcript", headers=h)
    out.append({"transcript_status": tr.status_code})
(S / "live_api_run.json").write_text(json.dumps(out, indent=1, default=str))
print("DONE", flush=True)
