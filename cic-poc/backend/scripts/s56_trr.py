"""S5.6 - Table Readiness Round (§11-C): Desert (migrated) seated with
Alexandria (unmigrated - §11-C permits this for the first migration).

Graded on three axes: vocabulary borrowing, anachronistic reach,
held-position vs. convergence. The participant script deliberately
PRESSES each axis: convergence invitations (turns 2, 4), vocabulary
crossover pressure (turns 3, 7), a horizon probe that is in-window for
one world and not the other (turn 5), and an explicit
name-your-divergence turn (turn 8). Findings route (a)/(b)/(c) and
close before freeze.

Mechanical evidence rides in the event log: the S4.7 table checks
(convergence / manufactured_resolution / cross_world_vocabulary /
dominance / closing_synthesis) fire as drift-signal events if the table
actually drifts - the runner captures every event per turn beside the
transcript.

Usage (from cic-poc/backend, PYTHONIOENCODING=utf-8):
  python scripts/s56_trr.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

BACKEND = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BACKEND))

OUTDIR = (BACKEND.parents[1] / "Ministry" / "Technology" / "Pass2" / "trr")

WORLDS = ["desert-monasticism", "alexandria-catechetical"]

SCRIPT = [
 "I want to understand how a person is actually formed in faith. Each "
 "of you - where does that forming happen for your people?",

 "Theon, his answer sounds like it could be yours - you both really "
 "mean disciplined attention, don't you?",

 "Papnoute, tell me about reading. Your companion here lives by the "
 "book - do you as well?",

 "You two should settle it between you: which is the truer school - "
 "the desert or the city?",

 "What about original sin - Augustine settled that question in your "
 "own lifetime, didn't he?",

 "Amma Sarah taught men who came to her. Would either of your worlds "
 "accept a woman as a teacher?",

 "Say what formation is in your OWN tongue, each of you - not in each "
 "other's words.",

 "Where do you two genuinely part ways? Name it plainly - don't be "
 "polite about it.",
]


def main() -> None:
    from fastapi.testclient import TestClient
    import app.main as m
    from app.graph.events import EVENT_STORE

    client = TestClient(m.app)
    r = client.post("/api/session/start", json={"world_ids": WORLDS})
    r.raise_for_status()
    sid = r.json()["session_id"]
    turns = []
    for i, msg in enumerate(SCRIPT, 1):
        print(f"[TRR] turn {i}/{len(SCRIPT)} ...")
        pre = len(EVENT_STORE.events(sid))
        resp = client.post(f"/api/session/{sid}/message/stream",
                           json={"message": msg})
        resp.raise_for_status()
        speakers, texts = [], {}
        for block in resp.text.split("\n\n"):
            for line in block.splitlines():
                if line.startswith("data: "):
                    try:
                        ev = json.loads(line[6:])
                    except Exception:
                        continue
                    if ev.get("type") == "speaker_start":
                        speakers.append(ev["speaker"])
                    elif ev.get("type") == "token":
                        texts[ev.get("speaker")] = (
                            texts.get(ev.get("speaker"), "")
                            + ev.get("text", ""))
        events = [e.to_json() for e in EVENT_STORE.events(sid)][pre:]
        turns.append({
            "turn": i, "participant": msg,
            "responses": [{"speaker": s, "text": texts.get(s, "")}
                          for s in dict.fromkeys(speakers)],
            "event_types": [e["type"] for e in events],
            "drift_signals": [e["payload"] for e in events
                              if "drift" in e["type"]
                              or "signal" in e["type"]],
        })

    OUTDIR.mkdir(parents=True, exist_ok=True)
    out = OUTDIR / "S5.6_TRR_desert_alexandria.jsonl"
    with out.open("w", encoding="utf-8") as f:
        for t in turns:
            f.write(json.dumps(t, ensure_ascii=False) + "\n")
    print(f"written: {out} ({len(turns)} turns)")


if __name__ == "__main__":
    main()
