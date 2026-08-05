"""S5.6 / FLAG-018 resolution - sustained-category re-run, both trials.

Re-runs ONLY the two 8-turn sustained scripts, fresh sessions, after the
over_settling delivery-instruction fix (nodes.generate_reroot_guidance).
Imports the probe definitions and mechanics from the battery instrument
itself (scripts/freeze_battery.py --world desert, formerly
scripts/s56_freeze_battery.py) rather than editing it - the
gate-integrity rule: the instrument that must pass is not touched.

Output: masked + key files with the same shapes as the battery's, suffix
`_rerun`, blind-graded the same way.

Usage (from cic-poc/backend, PYTHONIOENCODING=utf-8):
  python scripts/s56_sustained_rerun.py
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
from freeze_battery_probes import desert as _probes  # noqa: E402

TRIAL_A_SUSTAINED = _probes.TRIAL_A_SUSTAINED
TRIAL_B_SUSTAINED = _probes.TRIAL_B_SUSTAINED
STANDARDS = fb.build_standards("desert")
OUTDIR = fb.OUTDIR
DESERT = fb.WORLDS["desert"].world_id


def main() -> None:
    from fastapi.testclient import TestClient
    import app.main as m
    from app.graph.events import EVENT_STORE

    client = TestClient(m.app)
    items = []
    for pid, cat, turns in (TRIAL_A_SUSTAINED, TRIAL_B_SUSTAINED):
        pid = pid + "-rerun"
        print(f"[rerun] {pid} ...")
        r = client.post("/api/session/start", json={"world_id": DESERT})
        r.raise_for_status()
        sid = r.json()["session_id"]
        token = r.json()["session_token"]
        exchange, evidence = [], []
        for msg in turns:
            pre = len(EVENT_STORE.events(sid))
            speakers, texts = _stream_turn(client, sid, msg, token)
            exchange.append({"participant": msg,
                             "responses": [
                                 {"speaker": s, "text": texts.get(s, "")}
                                 for s in dict.fromkeys(speakers)]})
            ev = [e.to_json() for e in EVENT_STORE.events(sid)][pre:]
            evidence.append({
                "speakers": speakers,
                "event_types": [e["type"] for e in ev],
                "guidance": [e["payload"] for e in ev
                             if e["type"] in ("guidance_queued",
                                              "guidance_consumed")],
            })
        items.append({"id": pid, "category": cat,
                      "exchange": exchange, "evidence": evidence})

    with (OUTDIR / "S5.6_sustained_rerun_masked.jsonl").open(
            "w", encoding="utf-8") as f:
        for i, it in enumerate(items):
            f.write(json.dumps({"item": i, "category": it["category"],
                                "standard": STANDARDS[it["category"]],
                                "exchange": it["exchange"]},
                               ensure_ascii=False) + "\n")
    with (OUTDIR / "S5.6_sustained_rerun_key.jsonl").open(
            "w", encoding="utf-8") as f:
        for i, it in enumerate(items):
            f.write(json.dumps({"item": i, "id": it["id"],
                                "evidence": it["evidence"]},
                               ensure_ascii=False) + "\n")
    print("written: S5.6_sustained_rerun_{masked,key}.jsonl")


if __name__ == "__main__":
    main()
