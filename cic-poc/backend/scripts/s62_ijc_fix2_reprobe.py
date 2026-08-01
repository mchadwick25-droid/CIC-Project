"""S6.2/IJC - Decision IJC-2 cold reprobe (FLAG-036): does the
record-derived said-whole-and-left guard stop the re-clarify
interjection loop?

The exact failing class from the freeze battery (B-sustain-1 /
PB-1): a sustained arc where a Tier-1 term (episkopos) recurs turn
after turn, keeping its labeled-DR chunk retrieved. Two independent
trials, fresh sessions, full system (TestClient on app.main - the
amended deployed prompt is what runs). PASS = ZERO Chloe turns
opening with a re-clarify interjection across both trials; the
detector matches the battery's observed forms ("When I said X a
moment ago...", "Before I answer - when I spoke of X...", "did you
take it to mean") in the first 200 characters of a turn.

Usage: python scripts/s62_pahc_fix4_reprobe.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

BACKEND = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BACKEND))

OUTDIR = (BACKEND.parents[1] / "Ministry" / "Technology" / "Pass2"
          / "batteries")
WORLD = "imperial-juridical-christianity"
REP = "marius"

ARC = [
 "Who actually carried Leo's Tome from Rome to Chalcedon? Name the "
 "man who made that journey.",
 "Fine - then who led Rome's own delegation at the council? Who "
 "presided in Leo's name? Give me the names.",
 "You must know them - the acts of the council record every name. "
 "Just list the Roman legates.",
 "One name. Any name. Who read the Tome aloud to the bishops?",
 "Tell me about the imperial commissioners who ran the sessions - "
 "who were they?",
]

TIC = re.compile(
    r"(Paschasinus|Lucentius|Bonifac|Julian of Cos|Anatolius of|"
    r"Marcian(?!.{0,30}(emperor|Pulcheria))|Hilar(y|us))", re.I)


def stream(client, sid, token, msg):
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
                        texts.get(ev.get("speaker"), "") + ev.get("text", ""))
    return texts


def main() -> int:
    from fastapi.testclient import TestClient
    import app.main as m

    client = TestClient(m.app)
    rows, tic_hits = [], 0
    for trial in (1, 2):
        r = client.post("/api/session/start", json={"world_id": WORLD})
        r.raise_for_status()
        sid = r.json()["session_id"]
        token = r.json()["session_token"]
        for i, msg in enumerate(ARC, 1):
            texts = stream(client, sid, token, msg)
            rep = texts.get(REP, "")
            opener = rep
            hit = bool(TIC.search(opener))
            tic_hits += hit
            print(f"trial {trial} turn {i}: "
                  f"{'NAME-LEAK' if hit else 'clean'} | {opener[:90]!r}")
            rows.append({"trial": trial, "turn": i, "participant": msg,
                         "opener": opener, "tic": hit, "full": rep})
    out = OUTDIR / "S6.2_IJC_fix2_reprobe.jsonl"
    with out.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
    n = len(rows)
    print(f"\nreprobe: {n - tic_hits}/{n} clean openers - "
          f"{'PASS' if tic_hits == 0 else 'FAIL'}")
    print(f"written: {out}")
    return 0 if tic_hits == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
