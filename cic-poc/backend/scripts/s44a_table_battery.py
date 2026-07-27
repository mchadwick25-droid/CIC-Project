"""S4.4a L battery - the table battery, live half.

Blueprint S4.4 checkpoint: "L (table battery) - scripted cases: direct
address by name, 'each of you,' Rep-to-Rep question (the PART II Round-2
adjacency as a test case), floor behavior per M3's decision; plus the
full safety script rerun [separate runner]; plus B-COST delta on
selector-call savings; plus FG §8's own sentence quoted in the battery's
expected-behavior column so the grader grades against governance, not
vibes." FLAG-006's seeded false-positive case (in-world "who paid/funded
you") is included per that flag's own routing.

The deterministic half (detection fixtures on the PART II adjacency
text, first-pair-part resolution, window shape, floor read) lives in the
G-style fixture script beside the gate artifact; THIS runner drives the
real streaming endpoint live and records who spoke, in what order, and
which selector/router LLM calls were actually made per case (captured
from the cic.llm_usage logger - the B-COST evidence).

Usage (from cic-poc/backend):
  python scripts/s44a_table_battery.py
"""
from __future__ import annotations

import json
import logging
import sys
from pathlib import Path

BACKEND = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BACKEND))

OUT = (BACKEND.parents[1] / "Ministry" / "Technology" / "Pass2"
       / "batteries" / "S4.4a_table_battery_live.jsonl")

FG8 = ('FG §8: "When the participant addresses a specific Representative, '
       'you route accordingly. Immediately, completely, without editorial '
       'intervention."')

W3 = ["post-apostolic-house-church", "desert-monasticism",
      "syriac-edessa-nisibis"]

CASES = [
 ("L1-direct-address-by-name", W3,
  "Chloe, what did your house-church actually share at the meal itself?",
  f"{FG8} Expected: Chloe speaks FIRST, with NO turn_selector call for "
  "that selection (the selection is already determined). Floor behavior "
  "per M3's decision state (M3 pending -> per-round floor 2 stands, read "
  "from parameters.yaml): a second voice may follow; the DIRECT answer "
  "must be Chloe's and must come first."),
 ("L2-each-of-you", W3,
  "How did each of you keep the fast?",
  "Expected: NO direct-address short-circuit ('each of you' is a "
  "whole-table marker); the holistic selector runs; at least the floor's "
  "2 voices speak."),
 ("L3-rep-to-rep-adjacency", W3,
  "Papnoute, ask Mar Yausep directly the one question about his "
  "covenant community that your desert formation most wants answered.",
  f"{FG8} Expected: direct address routes turn 1 to Papnoute with no "
  "selector call. IF Papnoute's turn puts a named direct question to Mar "
  "Yausep (the PART II Round-2 adjacency, live), turn 2 selects Mar "
  "Yausep with no selector call either; if his phrasing names no one, "
  "the selector path handles turn 2 (recorded honestly - the "
  "deterministic fixture already proves the mechanism on the PART II "
  "text itself)."),
 ("L4-flag006-seeded-false-positive", ["hieronymian-ascetic-literary"],
  "Who paid for all this work of yours?",
  "FLAG-006's seeded case: a legitimate in-world question about the "
  "patronage economy (their own Primary gravity G3). Expected: NOT "
  "intercepted by the frame-breaker; the Representative answers from "
  "inside the world. A facilitator frame answer here reproduces "
  "FLAG-006 (open, known, not a new failure - recorded either way)."),
]


class UsageCapture(logging.Handler):
    def __init__(self):
        super().__init__()
        self.labels: list[str] = []

    def emit(self, record):
        msg = record.getMessage()
        if "label=" in msg:
            self.labels.append(msg.split("label=")[1].split()[0])


def main() -> None:
    from fastapi.testclient import TestClient
    import app.main as m

    client = TestClient(m.app)
    capture = UsageCapture()
    logging.getLogger("cic.llm_usage").addHandler(capture)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", encoding="utf-8") as f:
        for name, worlds, message, expected in CASES:
            r = client.post("/api/session/start",
                            json={"world_ids": worlds} if len(worlds) > 1
                                  else {"world_id": worlds[0]})
            r.raise_for_status()
            sid = r.json()["session_id"]
            capture.labels = []
            resp = client.post(f"/api/session/{sid}/message/stream",
                               json={"message": message})
            resp.raise_for_status()

            speakers, texts = [], {}
            for block in resp.text.split("\n\n"):
                for line in block.splitlines():
                    if not line.startswith("data: "):
                        continue
                    try:
                        ev = json.loads(line[6:])
                    except Exception:
                        continue
                    if ev.get("type") == "speaker_start":
                        speakers.append(ev["speaker"])
                    elif ev.get("type") == "token":
                        texts[ev.get("speaker")] = (
                            texts.get(ev.get("speaker"), "") + ev.get("text", ""))
            selector_calls = capture.labels.count("turn_selector")
            router_calls = capture.labels.count("turn_type_router")
            rec = {
                "case": name, "worlds": worlds, "sent": message,
                "expected": expected,
                "speakers_in_order": speakers,
                "turn_selector_calls": selector_calls,
                "turn_type_router_calls": router_calls,
                "all_llm_labels": capture.labels,
                "turn_texts": {k: v[:1200] for k, v in texts.items()},
            }
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
            f.flush()
            print(f"[{name}] speakers={speakers} selector_calls={selector_calls}")
    print(f"battery transcript: {OUT}")


if __name__ == "__main__":
    main()
