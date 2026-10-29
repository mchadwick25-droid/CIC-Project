"""Driver for the named, capped live test "fleet graded run 1" (cap $12.00).

Runs the admission harness one world per call, in the approved order, with
the whole-run cap enforced here and by the harness. Resumable: reads the
checkpoint, skips finished worlds, adds the dollars already spent.

  python Build/Ministry/Operations/Audits/fleet-graded-run-1/run_fleet.py --next
"""
import argparse
import json
import os
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
OUT = ROOT / "engine" / "m3" / "reports" / "fleet-graded-run-1"
CHECKPOINT = OUT / "checkpoint.json"
ORDER = ["lpc", "gallic", "desert", "ijc", "alx", "witt", "rzg", "pahc", "hal", "syr", "cappadocian", "don"]
CAP = 12.0
NAME = "fleet graded run 1"
MODEL = "us.anthropic.claude-sonnet-4-5-20250929-v1:0"
REGION = "us-east-1"
BRANCH = "claude/fleet-graded-run-1"
AUTH = "project lead (Mark), fleet graded run 1, approved 2026-10-28"


def load():
    if CHECKPOINT.exists():
        return json.loads(CHECKPOINT.read_text())
    return {"cap_usd": CAP, "spent_usd": 0.0, "worlds": {}, "current": None}


def save(cp):
    OUT.mkdir(parents=True, exist_ok=True)
    CHECKPOINT.write_text(json.dumps(cp, indent=2) + "\n")


def ledger_spent(path):
    spent = 0.0
    if path.exists():
        for line in path.read_text().splitlines():
            try:
                spent = max(spent, float(json.loads(line).get("spent_usd", 0.0)))
            except ValueError:
                pass
    return spent


def estimate(world):
    out = subprocess.run(
        [sys.executable, "-m", "engine.m3.live_admission_run", "--worlds", world, "--region", REGION,
         "--max-usd", str(CAP), "--authorized-by", AUTH, "--voice-model", MODEL, "--settings-only"],
        cwd=ROOT, capture_output=True, text=True)
    text = out.stderr
    return json.loads(text[text.index("{"):text.rindex("}") + 1])["estimated_usd_preflight"]


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


def run_world(cp, world):
    remaining = round(CAP - cp["spent_usd"], 4)
    est = estimate(world)
    if cp["spent_usd"] + est > CAP:
        print(f"STOP: spent ${cp['spent_usd']:.4f} + {world} estimate ${est:.4f} would pass ${CAP}")
        return "stop"
    state = cp["worlds"].setdefault(world, {"attempts": 0})
    tag = world if state["attempts"] == 0 else f"{world}-attempt{state['attempts'] + 1}"
    report = OUT / f"{tag}.json"
    ledger = OUT / f"ledger-{tag}.jsonl"
    answers = Path(str(report) + ".answers.jsonl")
    state.update(status="running", attempts=state["attempts"] + 1, preflight_usd=est, ledger=str(ledger.relative_to(ROOT)))
    cp["current"] = world
    save(cp)
    env = dict(os.environ, CIC_LIVE_TEST_LEDGER=str(ledger))
    cmd = [sys.executable, "-m", "engine.m3.live_admission_run", "--live-test", NAME, "--cap-usd", str(remaining),
           "--region", REGION, "--worlds", world, "--max-usd", str(remaining), "--authorized-by", AUTH,
           "--voice-model", MODEL, "--save-transcripts", "--out", str(report)]
    log_out, log_err = OUT / f"{tag}.stdout.txt", OUT / f"{tag}.stderr.txt"
    with open(log_out, "w") as fo, open(log_err, "w") as fe:
        proc = subprocess.Popen(cmd, cwd=ROOT, env=env, stdout=fo, stderr=fe)
        while proc.poll() is None:
            time.sleep(5)
            state["probes_answered"] = sum(1 for _ in open(answers)) if answers.exists() else 0
            state["spent_usd_world"] = round(ledger_spent(ledger), 6)
            cp["checkpoint_at"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
            save(cp)
    world_spent = round(ledger_spent(ledger), 6)
    cp["spent_usd"] = round(cp["spent_usd"] + world_spent, 6)
    state["spent_usd_world"] = world_spent
    ok = False
    if report.exists():
        data = json.loads(report.read_text())
        w = data["worlds"].get(world)
        ok = w is not None and data.get("aborted_reason") is None
        if w:
            state.update(pass_count=w["pass_count"], battery_size=w["battery_size"], overall_pass=w["overall_pass"])
        state["aborted_reason"] = data.get("aborted_reason")
    state["status"] = "done" if ok else "failed"
    state["exit_code"] = proc.returncode
    cp["current"] = None
    save(cp)
    sha = push(f"fleet graded run 1: {world} admission ({state['status']}; ${world_spent:.4f}; running ${cp['spent_usd']:.4f} of ${CAP})")
    print(json.dumps({"world": world, "status": state["status"], "spent_world": world_spent,
                      "running_total": cp["spent_usd"], "pushed": sha, **{k: state.get(k) for k in ("pass_count", "battery_size", "aborted_reason")}}))
    return "ok" if ok else "failed"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--next", action="store_true", help="run the next unfinished world, then stop")
    args = parser.parse_args()
    cp = load()
    for world in ORDER:
        st = cp["worlds"].get(world, {})
        if st.get("status") in ("done", "answers_only"):
            continue
        if st.get("status") == "failed" and st.get("attempts", 0) >= 2:
            continue
        if st.get("status") == "running":
            lost = round(ledger_spent(ROOT / st["ledger"]), 6)
            cp["spent_usd"] = round(cp["spent_usd"] + lost, 6)
            st.update(status="failed", spent_usd_world=lost, note="process stopped mid-world; ledger spend added")
            save(cp)
        if st.get("status") == "failed" and not st.get("retry_ok"):
            print(f"{world} is {st['status']} (attempts {st.get('attempts')}). Report it; set retry_ok in the checkpoint to retry once.")
            return 3
        result = run_world(cp, world)
        return 0 if result == "ok" else 2
    print("all worlds finished or skipped")
    return 0


if __name__ == "__main__":
    sys.exit(main())
