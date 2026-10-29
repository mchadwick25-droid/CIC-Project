"""Six-question replay for the eleven other worlds, for the named, capped live test "fleet graded run 1".

Asks each world the same six questions, in one conversation, that the 13 October
eleven-world test asked (the messages are read from those reports), through the
live turn path with the safety and reader calls. The whole-run cap is $15.00:
before each world the spent total plus that world's 13 October cost, padded by
15%, must fit, and each call's own cap is the dollars left. Resumable from the
checkpoint.

  python Build/Ministry/Operations/Audits/fleet-graded-run-1/run_replay.py
"""
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
OUT = ROOT / "engine" / "m3" / "reports" / "fleet-graded-run-1"
REPLAY = OUT / "replay"
CHECKPOINT = OUT / "checkpoint.json"
OLD = ROOT / "engine" / "m4" / "reports"
CAP = 15.0
PAD = 1.15
NAME = "fleet graded run 1"
REGION = "us-east-1"
BRANCH = "claude/fleet-graded-run-1"
ORDER = ["gallic", "desert", "ijc", "alx", "witt", "rzg", "pahc", "hal", "syr", "cappadocian", "don"]


def ledger_spent(path):
    spent = 0.0
    if path.exists():
        for line in path.read_text().splitlines():
            try:
                spent = max(spent, float(json.loads(line).get("spent_usd", 0.0)))
            except ValueError:
                pass
    return spent


def push(message):
    subprocess.run(["git", "add", str(OUT.relative_to(ROOT))], cwd=ROOT, check=True)
    subprocess.run(["git", "commit", "-q", "-m",
                    f"{message}\n\nCo-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>\n"
                    "Claude-Session: https://claude.ai/code/session_01JMNsSB4Hzhx5LFPu4ZKcZW"], cwd=ROOT)
    for wait in (0, 2, 4, 8, 16):
        time.sleep(wait)
        if subprocess.run(["git", "push", "-q", "-u", "origin", BRANCH], cwd=ROOT).returncode == 0:
            return subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    return "PUSH FAILED"


def main():
    REPLAY.mkdir(parents=True, exist_ok=True)
    cp = json.loads(CHECKPOINT.read_text())
    rep = cp.setdefault("replay", {})
    for world in ORDER:
        st = rep.get(world, {})
        if st.get("status") == "done":
            continue
        if st.get("status") == "running":
            lost = round(ledger_spent(ROOT / st["ledger"]), 6)
            cp["spent_usd"] = round(cp["spent_usd"] + lost, 6)
            st.update(status="failed", spent_usd_world=lost)
            rep[world] = st
            CHECKPOINT.write_text(json.dumps(cp, indent=2) + "\n")
            print(f"{world}: earlier run stopped mid-conversation; ${lost} added. Report before retrying.")
            return 3
        old = json.loads((OLD / f"live-turn-report-{world}-2026-10-13-eleven-world-test.json").read_text())
        messages = [r["message"] for r in old["results"]]
        estimate = round(float(old["live_test"]["priced_total_usd"]) * PAD, 4)
        if cp["spent_usd"] + estimate > CAP:
            rep[world] = {"status": "not_run", "reason": f"spent ${cp['spent_usd']:.4f} + estimate ${estimate:.4f} would pass ${CAP}"}
            CHECKPOINT.write_text(json.dumps(cp, indent=2) + "\n")
            print(f"STOP before {world}: {rep[world]['reason']}")
            continue
        remaining = round(CAP - cp["spent_usd"], 4)
        ledger = REPLAY / f"ledger-{world}.jsonl"
        rep[world] = {"status": "running", "ledger": str(ledger.relative_to(ROOT)), "estimate": estimate}
        CHECKPOINT.write_text(json.dumps(cp, indent=2) + "\n")
        live_report = OLD / f"live-turn-report-{world}.json"
        if live_report.exists():
            live_report.unlink()
        cmd = [sys.executable, "-m", "engine.m4.live_turn_run", "--live-test", NAME, "--cap-usd", str(remaining),
               "--region", REGION, "--world", world]
        for m in messages:
            cmd += ["--message", m]
        env = dict(os.environ, CIC_LIVE_TEST_LEDGER=str(ledger))
        with open(REPLAY / f"{world}.stdout.txt", "w") as fo, open(REPLAY / f"{world}.stderr.txt", "w") as fe:
            rc = subprocess.run(cmd, cwd=ROOT, env=env, stdout=fo, stderr=fe).returncode
        spent = round(ledger_spent(ledger), 6)
        cp["spent_usd"] = round(cp["spent_usd"] + spent, 6)
        ok = live_report.exists()
        if ok:
            shutil.move(str(live_report), str(REPLAY / f"{world}.json"))
            ok = not json.loads((REPLAY / f"{world}.json").read_text()).get("stopped_by_cap_at")
        rep[world].update(status="done" if ok else "failed", spent_usd_world=spent, exit_code=rc)
        CHECKPOINT.write_text(json.dumps(cp, indent=2) + "\n")
        sha = push(f"fleet graded run 1: replay {world} ({rep[world]['status']}; ${spent:.4f}; running ${cp['spent_usd']:.4f} of ${CAP})")
        print(json.dumps({"replay": world, "status": rep[world]["status"], "spent": spent,
                          "running_total": cp["spent_usd"], "pushed": sha}), flush=True)
        if not ok:
            return 2
    print("replay finished")
    return 0


if __name__ == "__main__":
    sys.exit(main())
