"""lpc validation conversations for the named, capped live test "fleet graded run 1".

Replays the same 30 conversations as the lpc run 3 validation (the messages are
read from that run's reports), one live_turn_run per conversation, deep interview
first. The whole-run cap stays $12.00: before each conversation the spent total
plus that conversation's run 3 cost must fit, and each call's own cap is the
dollars left. Resumable from the checkpoint.

  python Build/Ministry/Operations/Audits/fleet-graded-run-1/run_validation.py
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
VAL = OUT / "lpc-validation"
CHECKPOINT = OUT / "checkpoint.json"
RUN3 = ROOT / "engine" / "m4" / "reports" / "lpc-validation-2026-10-28-run3"
LIVE_REPORT = ROOT / "engine" / "m4" / "reports" / "live-turn-report-lpc.json"
CAP = 12.0
NAME = "fleet graded run 1"
REGION = "us-east-1"
BRANCH = "claude/fleet-graded-run-1"


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


def conversations():
    names = sorted(p.stem for p in RUN3.glob("*.json"))
    names.sort(key=lambda n: (n != "deep-interview", n))
    out = []
    for n in names:
        d = json.loads((RUN3 / f"{n}.json").read_text())
        out.append({"name": n, "messages": [r["message"] for r in d["results"]],
                    "estimate": float(d["live_test"]["priced_total_usd"])})
    return out


def main():
    VAL.mkdir(parents=True, exist_ok=True)
    cp = json.loads(CHECKPOINT.read_text())
    val = cp.setdefault("validation", {})
    for conv in conversations():
        name = conv["name"]
        st = val.get(name, {})
        if st.get("status") == "done":
            continue
        if st.get("status") == "running":
            lost = round(ledger_spent(ROOT / st["ledger"]), 6)
            cp["spent_usd"] = round(cp["spent_usd"] + lost, 6)
            st.update(status="failed", spent_usd_world=lost)
            val[name] = st
            CHECKPOINT.write_text(json.dumps(cp, indent=2) + "\n")
            print(f"{name}: earlier run stopped mid-conversation; ${lost} added. Report before retrying.")
            return 3
        if cp["spent_usd"] + conv["estimate"] > CAP:
            print(f"STOP: spent ${cp['spent_usd']:.4f} + {name} estimate ${conv['estimate']:.4f} would pass ${CAP}")
            return 0
        remaining = round(CAP - cp["spent_usd"], 4)
        ledger = VAL / f"ledger-{name}.jsonl"
        val[name] = {"status": "running", "ledger": str(ledger.relative_to(ROOT)), "estimate": conv["estimate"]}
        CHECKPOINT.write_text(json.dumps(cp, indent=2) + "\n")
        if LIVE_REPORT.exists():
            LIVE_REPORT.unlink()
        cmd = [sys.executable, "-m", "engine.m4.live_turn_run", "--live-test", NAME, "--cap-usd", str(remaining),
               "--region", REGION, "--world", "lpc"]
        for m in conv["messages"]:
            cmd += ["--message", m]
        env = dict(os.environ, CIC_LIVE_TEST_LEDGER=str(ledger))
        with open(VAL / f"{name}.stdout.txt", "w") as fo, open(VAL / f"{name}.stderr.txt", "w") as fe:
            rc = subprocess.run(cmd, cwd=ROOT, env=env, stdout=fo, stderr=fe).returncode
        spent = round(ledger_spent(ledger), 6)
        cp["spent_usd"] = round(cp["spent_usd"] + spent, 6)
        ok = LIVE_REPORT.exists()
        if ok:
            shutil.move(str(LIVE_REPORT), str(VAL / f"{name}.json"))
            ok = not json.loads((VAL / f"{name}.json").read_text()).get("stopped_by_cap_at")
        val[name].update(status="done" if ok else "failed", spent_usd_world=spent, exit_code=rc)
        CHECKPOINT.write_text(json.dumps(cp, indent=2) + "\n")
        sha = push(f"fleet graded run 1: lpc validation {name} ({val[name]['status']}; ${spent:.4f}; running ${cp['spent_usd']:.4f} of ${CAP})")
        print(json.dumps({"validation": name, "status": val[name]["status"], "spent": spent,
                          "running_total": cp["spent_usd"], "pushed": sha}), flush=True)
        if not ok:
            return 2
    print("all validation conversations finished")
    return 0


if __name__ == "__main__":
    sys.exit(main())
