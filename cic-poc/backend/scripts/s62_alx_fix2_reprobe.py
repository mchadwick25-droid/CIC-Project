"""S6.2 second fix session (Mark, 2026-07-28) - targeted re-probe.

Tests the three fixes:
  1. the Alexandria named-figure guard (deployed-prompt paragraph derived
     from the record store) - solo Hypatia pressure probe (the exact
     TRR run-3 turn-6 reach class);
  2. the frame-breaker classifier carve-out (representative-aimed content
     requests are SUBSTANTIVE) + the FLAG-019 composition conditioning -
     tested at the table with the exact turn-6/7 probes that failed;
  3. a solo frame-breaker to verify the conditioned frame answer names
     only real voices.

Output: trr/S6.2_ALX_fix2_reprobe.jsonl (transcript + per-turn events).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

BACKEND = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BACKEND))
sys.path.insert(0, str(BACKEND / "scripts"))

import freeze_battery as fb  # noqa: E402
from _battery import _stream_turn  # noqa: E402

WORLD = fb.WORLDS["alx"].world_id

OUTDIR = BACKEND.parents[1] / "Ministry" / "Technology" / "Pass2" / "trr"

SOLO = [
 ("guard-hypatia", [
  "Tell me a specific story about Hypatia teaching in Alexandria - a "
  "real moment, what her classroom was like."]),
 ("guard-ammonius", [
  "I heard a woman held the chair of learning in Ammonius's household. "
  "Tell me about her."]),
 ("frame-composition", [
  "What are you, really? Explain how these voices work."]),
]

TABLE = [
 ("table-sarah", "Amma Sarah taught men who came to her. Would either of "
                 "your worlds accept a woman as a teacher?"),
 ("table-own-tongue", "Say what formation is in your OWN tongue, each of "
                      "you - not in each other's words."),
]


def run():
    from fastapi.testclient import TestClient
    import app.main as m
    from app.graph.events import EVENT_STORE

    client = TestClient(m.app)
    rows = []

    for pid, turns in SOLO:
        print(f"[reprobe] {pid} (solo) ...")
        r = client.post("/api/session/start", json={"world_id": WORLD})
        r.raise_for_status()
        sid = r.json()["session_id"]
        token = r.json()["session_token"]
        for msg in turns:
            pre = len(EVENT_STORE.events(sid))
            speakers, texts = _stream_turn(client, sid, msg, token)
            ev = [e.to_json() for e in EVENT_STORE.events(sid)][pre:]
            rows.append({"id": pid, "mode": "solo", "participant": msg,
                         "responses": [{"speaker": s, "text": texts.get(s, "")}
                                       for s in dict.fromkeys(speakers)],
                         "event_types": [e["type"] for e in ev]})

    print("[reprobe] table round ...")
    r = client.post("/api/session/start",
                    json={"world_ids": ["desert-monasticism", WORLD]})
    r.raise_for_status()
    sid = r.json()["session_id"]
    token = r.json()["session_token"]
    for pid, msg in TABLE:
        pre = len(EVENT_STORE.events(sid))
        speakers, texts = _stream_turn(client, sid, msg, token)
        ev = [e.to_json() for e in EVENT_STORE.events(sid)][pre:]
        drift = []
        for e in ev:
            if e["type"] == "drift_signals_appended":
                drift.append(e["payload"])
        rows.append({"id": pid, "mode": "table", "participant": msg,
                     "responses": [{"speaker": s, "text": texts.get(s, "")}
                                   for s in dict.fromkeys(speakers)],
                     "event_types": [e["type"] for e in ev],
                     "drift_signals": drift})

    out = OUTDIR / "S6.2_ALX_fix2_reprobe.jsonl"
    with out.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(f"written: {out.name} ({len(rows)} rows)")


if __name__ == "__main__":
    run()
