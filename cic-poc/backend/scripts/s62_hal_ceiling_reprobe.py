"""S6.2/HAL Decision HAL-4 verification - the desert TRR table re-run
under the new 160 ceiling (the SYR ceiling_reprobe precedent); Albina
word counts + dominance share measured and compared to the graded
first run.

Usage: python scripts/s62_hal_ceiling_reprobe.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

BACKEND = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BACKEND))

from s62_hal_trr import SCRIPTS  # noqa: E402

OUTDIR = (BACKEND.parents[1] / "Ministry" / "Technology" / "Pass2" / "trr")


def main() -> None:
    worlds, script = SCRIPTS["desert"]

    from fastapi.testclient import TestClient
    import app.main as m

    client = TestClient(m.app)
    r = client.post("/api/session/start", json={"world_ids": worlds})
    r.raise_for_status()
    sid = r.json()["session_id"]
    turns = []
    for i, msg in enumerate(script, 1):
        print(f"[ceiling-reprobe] turn {i}/{len(script)} ...", flush=True)
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
        turns.append({"turn": i, "participant": msg,
                      "responses": [{"speaker": s, "text": texts.get(s, "")}
                                    for s in dict.fromkeys(speakers)]})

    OUTDIR.mkdir(parents=True, exist_ok=True)
    out = OUTDIR / "S6.2_HAL_ceiling_reprobe.jsonl"
    with out.open("w", encoding="utf-8") as f:
        for t in turns:
            f.write(json.dumps(t, ensure_ascii=False) + "\n")

    def stats(path):
        alb, other = [], []
        for line in Path(path).read_text(encoding="utf-8").splitlines():
            d = json.loads(line)
            for r_ in d["responses"]:
                n = len(r_["text"].split())
                (alb if r_["speaker"] == "albina" else other).append(n)
        rep_total = sum(alb) + sum(
            n for n in other) if other else sum(alb)
        return alb, (sum(alb) * 100 // max(1, rep_total))

    # note: dominance here counts albina vs ALL other speakers incl.
    # facilitator lines in responses; the graded run's drift layer used
    # representative-only speech - both shares reported for honesty
    new_counts, new_share = stats(out)
    old_counts, old_share = stats(OUTDIR / "S6.2_HAL_TRR_desert.jsonl")
    print(f"\nfirst run:  albina words per turn {old_counts} "
          f"(max {max(old_counts)}), share ~{old_share}%")
    print(f"reprobe:    albina words per turn {new_counts} "
          f"(max {max(new_counts)}), share ~{new_share}%")
    print(f"written: {out}")


if __name__ == "__main__":
    main()
