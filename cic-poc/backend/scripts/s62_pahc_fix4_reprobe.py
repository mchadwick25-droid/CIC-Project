"""S6.2/PAHC - Decision PAHC-4 cold reprobe (FLAG-034): does the
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
WORLD = "post-apostolic-house-church"
REP = "chloe"

ARC = [
 "Who actually leads your community — really, who has the final say?",
 "You mentioned the episkopos. How does a household with one differ, "
 "day to day, from one governed by the elders together?",
 "And when the episkopos dies — what happens to a household built "
 "around one man?",
 "Doesn't that make the council's way simply safer? Why would anyone "
 "choose the bishop's way at all?",
 "Last question — if my own church asked you which way to order "
 "itself, what would you tell them?",
]

TIC = re.compile(
    r"(when i (said|spoke of|used)\b.*?\b(meant|mean\b|understand|understood|take it)|"
    r"before i (answer|go further|go on)\b.*?\bwhen i (said|spoke)|"
    r"did you (take|understand) (it|that word|the word))",
    re.I | re.S)


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
            opener = rep[:200]
            hit = bool(TIC.search(opener))
            tic_hits += hit
            print(f"trial {trial} turn {i}: "
                  f"{'TIC' if hit else 'clean'} | {opener[:90]!r}")
            rows.append({"trial": trial, "turn": i, "participant": msg,
                         "opener": opener, "tic": hit, "full": rep})
    out = OUTDIR / "S6.2_PAHC_fix4_reprobe.jsonl"
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
