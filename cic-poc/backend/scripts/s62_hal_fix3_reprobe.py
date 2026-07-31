"""S6.2/HAL Decision HAL-3 verification - the vindication-frame
anachronism class re-probed COLD through the LIVE system (the ALX
fix2_reprobe precedent): the Trent probe verbatim + a praise-frame
variant + a defeat-frame variant, two trials each, fresh session per
trial. Output for manual grading against the anachronism standard
(the later thing met unrecognizing; no weighing of post-window
verdicts about the household).

Usage: python scripts/s62_hal_fix3_reprobe.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

BACKEND = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BACKEND))

OUTDIR = (BACKEND.parents[1] / "Ministry" / "Technology" / "Pass2"
          / "batteries")
WORLD = "hieronymian-ascetic-literary"

PROBES = [
    ("trent", "Centuries later your translation became the official "
              "Bible of the whole Catholic Church — the Council of "
              "Trent made it so. Doesn't that prove your household won "
              "the argument with Augustine?"),
    ("praise", "Looking back, history vindicated your household "
               "completely — your corrected text became THE Bible of "
               "the West for over a thousand years. How does that feel?"),
    ("defeat", "Modern translators have now abandoned your Vulgate and "
               "gone back to the original languages themselves — "
               "doesn't that undo your scholar's whole life's work?"),
]


def _stream_turn(client, sid, message):
    resp = client.post(f"/api/session/{sid}/message/stream",
                       json={"message": message})
    resp.raise_for_status()
    texts = {}
    for block in resp.text.split("\n\n"):
        for line in block.splitlines():
            if line.startswith("data: "):
                try:
                    ev = json.loads(line[6:])
                except Exception:
                    continue
                if ev.get("type") == "token":
                    texts[ev.get("speaker")] = (
                        texts.get(ev.get("speaker"), "") + ev.get("text", ""))
    return texts


def main() -> None:
    from fastapi.testclient import TestClient
    import app.main as m

    client = TestClient(m.app)
    rows = []
    for pid, probe in PROBES:
        for trial in (1, 2):
            print(f"[{pid}] trial {trial} ...", flush=True)
            r = client.post("/api/session/start", json={"world_id": WORLD})
            r.raise_for_status()
            sid = r.json()["session_id"]
            texts = _stream_turn(client, sid, probe)
            rows.append({"probe": pid, "trial": trial,
                         "responses": texts})
    out = OUTDIR / "S6.2_HAL_fix3_reprobe.jsonl"
    with out.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(f"written: {out} ({len(rows)} rows)")


if __name__ == "__main__":
    main()
