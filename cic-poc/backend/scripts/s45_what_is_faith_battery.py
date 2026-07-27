"""S4.5 L battery - Pass 1 §9.4 turned into a script.

Cases: bare universal questions (faith, prayer, love - expected
classification NONE, structurally: no distinguishing formula present),
true bridge cases (sola fide, transubstantiation at a PAHC table),
the split-table case (Trinity at PAHC + Imperial-Juridical - the honest
split), and a native-window no-fire case (original sin at Desert, whose
world_core window reaches 430 - the dates do the work). Each case
carries its expected classification and expected per-world speech.

Per case the runner records: the SSE speaker order, whether the
modern-term classifier fired (from the session's own event log:
classifier_decision[modern_term] raw result), the persisted
bridge_reframe event (question/split/native_for/anachronistic_for), and
whether the reframe sentinel stayed OUT of the participant-facing
response while entering the Representatives' transcript.

Usage (from cic-poc/backend):
  python scripts/s45_what_is_faith_battery.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

BACKEND = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BACKEND))

OUT = (BACKEND.parents[1] / "Ministry" / "Technology" / "Pass2"
       / "batteries" / "S4.5_what_is_faith_live.jsonl")

PAHC = "post-apostolic-house-church"
IJC = "imperial-juridical-christianity"
DESERT = "desert-monasticism"
SYRIAC = "syriac-edessa-nisibis"

CASES = [
 ("W1-bare-faith", [DESERT], "What is faith?",
  "NONE structurally (no distinguishing formula present); Papnoute answers natively from his own world."),
 ("W2-bare-prayer", [PAHC], "What is prayer?",
  "NONE structurally; Chloe answers natively."),
 ("W3-bare-love", [SYRIAC], "What is love?",
  "NONE structurally; Mar Yausep answers natively."),
 ("W4-sola-fide", [PAHC], "Is it faith alone that saves you, and not anything you do?",
  "sola-fide bridge (1517 > 200): Facilitator names-as-later + neutral sense, "
  "reframe persisted as bridge_reframe event (sentinel in transcript, NOT in "
  "participant response), Chloe answers the term-free subject."),
 ("W5-transubstantiation", [PAHC], "What did your community believe about transubstantiation?",
  "transubstantiation bridge (1215 > 200): same shape as W4."),
 ("W6-trinity-split", [PAHC, IJC], "What do you hold about the doctrine of the Trinity?",
  "SPLIT (325: later for PAHC/200, native for IJC/451): Facilitator names the "
  "split honestly; Marius answers the term from inside his own era (the "
  "answering world = the native world); Chloe joins on the underlying subject "
  "in the continuation; reframe persisted."),
 ("W7-original-sin-desert", [DESERT], "What is original sin - are people born already guilty?",
  "NO FIRE by the dates (410 <= Desert world_core end 430 - native window): "
  "classifier may match the term but the per-world gate returns None; "
  "Papnoute answers natively."),
]


def main() -> None:
    from fastapi.testclient import TestClient
    import app.main as m
    from app.graph.events import EVENT_STORE

    client = TestClient(m.app)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", encoding="utf-8") as f:
        for name, worlds, message, expected in CASES:
            r = client.post("/api/session/start",
                            json={"world_ids": worlds} if len(worlds) > 1
                                  else {"world_id": worlds[0]})
            r.raise_for_status()
            sid = r.json()["session_id"]
            resp = client.post(f"/api/session/{sid}/message/stream",
                               json={"message": message})
            resp.raise_for_status()

            speakers = []
            for block in resp.text.split("\n\n"):
                for line in block.splitlines():
                    if line.startswith("data: "):
                        try:
                            ev = json.loads(line[6:])
                        except Exception:
                            continue
                        if ev.get("type") == "speaker_start":
                            speakers.append(ev["speaker"])

            events = [e.to_json() for e in EVENT_STORE.events(sid)]
            mt_decision = next((e["payload"] for e in events
                                if e["type"] == "classifier_decision"
                                and e["payload"].get("classifier") == "modern_term"),
                               None)
            reframe = next((e["payload"] for e in events
                            if e["type"] == "bridge_reframe"), None)

            session_view = client.get(f"/api/session/{sid}").json()
            sentinel_in_response = any(
                "If your world had nothing like this" in (msg.get("content") or "")
                for msg in session_view["messages"])

            state = EVENT_STORE.get_state(sid)
            from app.graph.nodes import build_public_transcript
            transcript = build_public_transcript(state)

            rec = {
                "case": name, "worlds": worlds, "sent": message,
                "expected": expected,
                "speakers_in_order": speakers,
                "modern_term_raw": (mt_decision or {}).get("raw"),
                "bridge_reframe_event": reframe,
                "reframe_sentinel_in_participant_response": sentinel_in_response,
                "facilitator_in_rep_transcript": "Facilitator:" in transcript,
                "transcript_tail": transcript[-600:],
            }
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
            f.flush()
            fired = "None" if reframe is None else (
                f"split={reframe.get('split')} term={reframe.get('term_id')}")
            print(f"[{name}] speakers={speakers} bridge={fired}")
    print(f"battery transcript: {OUT}")


if __name__ == "__main__":
    main()
