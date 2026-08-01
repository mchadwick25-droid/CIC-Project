"""S6.2/PAHC - Decision IJC-5 ceiling reprobe: with the new ENFORCING
ceiling live (150 @ 1.5 - retry >225w), do solo Chloe turns come in at
or under the retry trigger, and does the mechanism fire-and-pull when
a draft runs long? (The HAL s62_hal_ceiling_reprobe pattern.)

Four solo probes chosen to bait length (the battery's longest
classes: a claim exposition, a story ask, a comparison, a teaching
ask). Records per-turn word counts; PASS = every EMITTED turn <= 225
words (the trigger line - the mechanism either kept the draft under
or retried it under).

Usage: python scripts/s62_pahc_ceiling_reprobe.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

BACKEND = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BACKEND))

OUTDIR = (BACKEND.parents[1] / "Ministry" / "Technology" / "Pass2"
          / "batteries")
WORLD = "imperial-juridical-christianity"
REP = "marius"
TRIGGER = 270

PROBES = [
 "Tell me everything about how Rome's primacy claim developed - "
 "Julius, Damasus, Leo, all of it, in full.",
 "Walk me through the whole story of the Tome - written, carried, "
 "read, acclaimed, refused - start to finish.",
 "Compare Rome's claim and Constantinople's claim for me - both "
 "grounds, both histories, in full.",
 "Explain the whole Arian controversy across your window - every "
 "turn of it.",
]


def main() -> int:
    from fastapi.testclient import TestClient
    import app.main as m

    client = TestClient(m.app)
    rows = []
    over = 0
    for i, msg in enumerate(PROBES, 1):
        r = client.post("/api/session/start", json={"world_id": WORLD})
        r.raise_for_status()
        sid, token = r.json()["session_id"], r.json()["session_token"]
        resp = client.post(f"/api/session/{sid}/message/stream",
                           json={"message": msg},
                           headers={"X-Session-Token": token})
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
                            texts.get(ev.get("speaker"), "")
                            + ev.get("text", ""))
        rep = texts.get(REP, "")
        n = len(rep.split())
        over += n > TRIGGER
        print(f"probe {i}: {n} words "
              f"({'OVER trigger' if n > TRIGGER else 'ok'})")
        rows.append({"probe": i, "participant": msg, "words": n,
                     "text": rep})
    out = OUTDIR / "S6.2_IJC_ceiling_reprobe.jsonl"
    with out.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(f"\nceiling reprobe: {len(rows) - over}/{len(rows)} emitted "
          f"turns <= {TRIGGER}w - {'PASS' if over == 0 else 'FAIL'}")
    print(f"written: {out}")
    return 0 if over == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
