"""Confirm pass after #709: 11 worlds x 1 pass, cap $7.
Original baseline header: A pass runs its 11 worlds in parallel, one
invocation each. Hard cap $35 total: the $0.464 sample and $0.15 for an
unrecorded interrupted invocation count against it, and a pass starts only if
spend so far plus 1.5x the pass's preflight estimate stays at or under $35."""
import json, subprocess, sys, datetime
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
REPO = Path("/home/user/CIC-Project")
sys.path.insert(0, str(REPO))
from engine.m3.live_admission_run import real_world_costs, estimate_world_cost_usd
WORLDS = "alx cappadocian desert don gallic hal ijc pahc rzg syr witt".split()
CAP = 7.00
spent = 0.0
log = []
def sh(*a): return subprocess.run(a, cwd=REPO, capture_output=True, text=True)
def one(rep, w, est):
    out = f"engine/m3/reports/live-admission-report-confirm709-r{rep}-{w}-2026-10-03.json"
    per_cap = round(est * SCALE, 4)
    cmd = [sys.executable, "-m", "engine.m3.live_admission_run", "--region", "us-east-1", "--worlds", w,
           "--voice-model", "us.anthropic.claude-sonnet-4-5", "--max-usd", f"{per_cap:.4f}",
           "--authorized-by", "Mark Chadwick (confirm pass after #709 approved 2026-10-03, total cap $7)",
           "--save-transcripts", "--out", out]
    t0 = datetime.datetime.utcnow().isoformat(timespec="seconds")
    p = subprocess.run(cmd, cwd=REPO, capture_output=True, text=True)
    e = {"pass": rep, "world": w, "started": t0, "exit": p.returncode, "max_usd_given": per_cap}
    if (REPO / out).exists():
        d = json.loads((REPO / out).read_text())
        e.update(actual_usd=d["actual_usd_spent"], aborted=d["aborted_reason"],
                 pass_count=d["worlds"].get(w, {}).get("pass_count"),
                 voice_model_id=d["voice_model_id"], manifest=d["run_settings"]["package_manifest_hash"][w])
    else:
        e["error_tail"] = (p.stderr or p.stdout)[-1500:]
    return e
for rep in (1,):
    costs = real_world_costs()
    ests = {w: estimate_world_cost_usd(w, costs) for w in WORLDS}
    SCALE = CAP / sum(ests.values()); need = SCALE * sum(ests.values())
    if spent + need > CAP + 1e-9:
        print(f"STOP before pass {rep}: spent {spent:.4f} + scaled estimate {need:.4f} > {CAP}", flush=True); break
    print(f"SCALE {SCALE:.4f} preflight {sum(ests.values()):.4f}", flush=True)
    with ThreadPoolExecutor(max_workers=11) as ex:
        entries = list(ex.map(lambda w: one(rep, w, ests[w]), WORLDS))
    for e in entries:
        spent += e.get("actual_usd", 0.0)
        e["spent_total_after_pass"] = None
        log.append(e); print(json.dumps(e), flush=True)
    for e in entries: e["spent_total_after_pass"] = round(spent, 4)
    (REPO / "engine/m3/reports/confirm709-2026-10-03-runlog.json").write_text(
        json.dumps({"cap_usd": CAP, "counted_before_runs": {},
                    "entries": log}, indent=2) + "\n")
    sh("git", "add", "engine/m3/reports")
    sh("git", "commit", "-q", "-m", f"Confirm pass after #709: 11 worlds, transcripts saved\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>\nClaude-Session: https://claude.ai/code/session_0127FzGZ8nfcxCkbyvQvVmCZ")
    r = sh("git", "push", "-q", "origin", "data/confirm-709-2026-10-03")
    print(f"PASS {rep} done, pushed rc={r.returncode}, spent_total={spent:.4f}", flush=True)
print("DONE spent_total", round(spent, 4), flush=True)
