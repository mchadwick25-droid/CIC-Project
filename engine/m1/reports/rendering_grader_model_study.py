"""Which model should grade rendering fidelity? Re-grades the R43 labeled
set (Build/Ministry/Operations/Audits/Tech-Readiness-2026-09/Model-Assignment/
R43-Labeled-Set.csv) with each candidate grader model, several runs per
record, through engine.m1.rendering_fidelity's own grade_rendering - same
system prompt, same forced-tool schema, same provider seam - so the only
thing that varies is the model.

What is graded for each row is the rendering a person actually ruled on:
- defect_fixed_on_grader_finding / grader_disagreement_kept: the version
  at `pre_fix_ref`, the main-side text before that record's R43 PR.
- defect_missed_by_grader_caught_by_human: the version at `round1_ref`,
  the round-one re-authoring the human read rejected (fragments, archaic
  register, small adds and drops). The pre-PR text never held those
  defects, so it could not test whether a grader catches them.

Expected verdict per row: any of the three defect labels means the
human found the graded text defective, so a non-"translation" verdict is
a catch and "translation" a miss; grader_disagreement_kept means the
human kept the text, so "translation" is correct and any other verdict a
false positive. The 57 pre-PR rows were selected BY a Haiku flag, so
Haiku's catch rate on them is biased upward by construction; the round-one
rows were never selected by any grader and are the unbiased recall test.

Real, billed Bedrock calls - a by-hand, credentialed run, not a CI job.

Run: python3 -m engine.m1.reports.rendering_grader_model_study --region us-east-1 [--limit N] [--models haiku,sonnet46]
"""
import argparse
import csv
import json
import pathlib
import statistics
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]))

from engine.m1.loader import parse_record_text
from engine.m1.rendering_fidelity import grade_rendering
from engine.m8.cost import PriceTable, estimate_cost
from engine.m8.live_cost_run import HAIKU_4_5_PRICE_TABLE
from engine.provider import guard
from engine.provider.bedrock import make_client, normalize_usage, resolve_model_id

REPO_ROOT = Path(__file__).resolve().parents[3]
LABELED_SET = REPO_ROOT / "Build/Ministry/Operations/Audits/Tech-Readiness-2026-09/Model-Assignment/R43-Labeled-Set.csv"
REPORT_PATH = Path(__file__).resolve().parent / "rendering-grader-model-study-2026-09-24.json"

MISSED = "defect_missed_by_grader_caught_by_human"
KEPT = "grader_disagreement_kept"

RATE_CARD_SOURCE = (
    "Anthropic published API rate card as cached in the claude-api reference (2026-06-24): "
    "Sonnet 4.6 $3/$15 per MTok in/out. Cache rates set at the standard 1.25x write / 0.1x read "
    "multipliers, unused by this study (the grader sends no cache_control). Bedrock pricing "
    "not independently fetchable here - same caveat as engine.m8.live_cost_run.PRICE_TABLE_SOURCE."
)
SONNET_4_6_PRICE_TABLE = PriceTable(
    input_per_token=3.00 / 1_000_000,
    output_per_token=15.00 / 1_000_000,
    cache_write_per_token=3.75 / 1_000_000,
    cache_read_per_token=0.30 / 1_000_000,
    source=RATE_CARD_SOURCE,
)

MODELS = {
    "haiku": ("us.anthropic.claude-haiku-4-5", HAIKU_4_5_PRICE_TABLE),
    "sonnet46": ("us.anthropic.claude-sonnet-4-6", SONNET_4_6_PRICE_TABLE),
}
# Sonnet 5 (the model the study was scoped for) is listed as an inference
# profile but refuses invocation on this account (403, 2026-09-24; see
# engine/provider/reports/model-availability-2026-09-24.json). Sonnet 4.6
# is the newest Sonnet this account can invoke.

# Wider than grade_rendering's 8s default so a slower model's latency is
# measured rather than cut off; timeouts are still recorded per call.
TIMEOUT_SECONDS = 60.0


def graded_version(row: dict) -> tuple[str, str]:
    ref = row["round1_ref"] if row["label"] == MISSED else row["pre_fix_ref"].split()[0].strip(" ;,")
    return ref, f"records/{row['world']}/quote/{row['record_id']}.md"


def load_rendering(ref: str, path: str) -> dict:
    blob = subprocess.run(
        ["git", "-C", str(REPO_ROOT), "show", f"{ref}:{path}"], capture_output=True, text=True, check=True
    ).stdout
    rec = parse_record_text(blob, f"{ref}:{path}")
    return {"text": rec["text"], "modern_rendering": rec["modern_rendering"]}


def run(region: str, model_keys: list[str], runs: int, limit: int | None) -> dict:
    rows = list(csv.DictReader(LABELED_SET.open(encoding="utf-8")))
    if limit:
        rows = rows[:limit]
    client = make_client(region)
    resolved = {k: resolve_model_id(MODELS[k][0], region) for k in model_keys}

    results = []
    for row in rows:
        ref, path = graded_version(row)
        rendering = load_rendering(ref, path)
        entry = {
            "record_id": row["record_id"],
            "world": row["world"],
            "label": row["label"],
            "graded_ref": ref,
            "human_says_defective": row["label"] != KEPT,
            "text": rendering["text"],
            "modern_rendering": rendering["modern_rendering"],
            "runs": {},
        }
        for key in model_keys:
            calls = []
            for _ in range(runs):
                start = time.perf_counter()
                outcome = grade_rendering(
                    client, resolved[key], original=rendering["text"],
                    modern_rendering=rendering["modern_rendering"], timeout=TIMEOUT_SECONDS,
                )
                latency = time.perf_counter() - start
                call = {"status": outcome.status, "latency_seconds": round(latency, 3)}
                if outcome.status == "ok":
                    usage = normalize_usage(outcome.raw_usage)
                    call.update(
                        verdict=outcome.value["verdict"],
                        reasoning=outcome.value["reasoning"],
                        input_tokens=usage.input_tokens,
                        output_tokens=usage.output_tokens,
                        dollars=estimate_cost(usage, MODELS[key][1]).dollars,
                    )
                else:
                    call["detail"] = outcome.value
                calls.append(call)
            entry["runs"][key] = calls
            print(f"{row['record_id']:60} {key:8} {[c.get('verdict', c['status']) for c in calls]}", flush=True)
        results.append(entry)

    return {
        "generated": datetime.now(timezone.utc).isoformat(),
        "region": region,
        "model_ids": resolved,
        "runs_per_record": runs,
        "timeout_seconds": TIMEOUT_SECONDS,
        "price_sources": {k: MODELS[k][1].source for k in model_keys},
        "summary": {k: summarize(results, k) for k in model_keys},
        "records": results,
    }


def _flag(call: dict) -> bool:
    return call["verdict"] != "translation"


def _rates(entries: list[dict], key: str) -> dict:
    """Per-call and majority-of-runs confusion counts over `entries`."""
    per_call = {"catch": 0, "miss": 0, "false_positive": 0, "true_negative": 0}
    majority = dict(per_call)
    for e in entries:
        ok = [c for c in e["runs"][key] if c["status"] == "ok"]
        if not ok:
            continue
        for c in ok:
            per_call[_bucket(e["human_says_defective"], _flag(c))] += 1
        flagged = sum(_flag(c) for c in ok) * 2 > len(ok)
        majority[_bucket(e["human_says_defective"], flagged)] += 1
    return {"per_call": per_call, "majority": majority}


def _bucket(defective: bool, flagged: bool) -> str:
    if defective:
        return "catch" if flagged else "miss"
    return "false_positive" if flagged else "true_negative"


def summarize(results: list[dict], key: str) -> dict:
    calls = [c for e in results for c in e["runs"][key]]
    ok = [c for c in calls if c["status"] == "ok"]
    latencies = sorted(c["latency_seconds"] for c in ok)
    stable_verdict = stable_flag = 0
    for e in results:
        verdicts = [c.get("verdict") for c in e["runs"][key]]
        stable_verdict += len(set(verdicts)) == 1 and None not in verdicts
        flags = {v != "translation" for v in verdicts if v}
        stable_flag += len(flags) == 1 and None not in verdicts
    by_label = {}
    for label in sorted({e["label"] for e in results}):
        by_label[label] = _rates([e for e in results if e["label"] == label], key)
    total_dollars = sum(c["dollars"] for c in ok)
    return {
        "calls": len(calls),
        "ok_calls": len(ok),
        "failed_calls": {s: sum(c["status"] == s for c in calls) for s in {c["status"] for c in calls} if s != "ok"},
        "all": _rates(results, key),
        "by_label": by_label,
        "records_same_verdict_all_runs": stable_verdict,
        "records_same_flag_all_runs": stable_flag,
        "records": len(results),
        "latency_seconds": {
            "p50": round(statistics.median(latencies), 3) if latencies else None,
            "p95": round(latencies[int(0.95 * (len(latencies) - 1))], 3) if latencies else None,
            "max": latencies[-1] if latencies else None,
        },
        "dollars_total": round(total_dollars, 4),
        "dollars_per_call": round(total_dollars / len(ok), 6) if ok else None,
        "mean_output_tokens": round(statistics.mean(c["output_tokens"] for c in ok), 1) if ok else None,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    guard.add_arguments(parser)
    parser.add_argument("--region", required=True)
    parser.add_argument("--models", default="haiku,sonnet46")
    parser.add_argument("--runs", type=int, default=3)
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--out", type=Path, default=REPORT_PATH)
    args = parser.parse_args(argv)

    report = run(args.region, args.models.split(","), args.runs, args.limit)
    args.out.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(report["summary"], indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
