"""Live (real Bedrock spend) M3 admission run against alx and desert -
requires explicit per-run authorization, named on the command line.
Every prior run of this battery in this repo
(selftest.py, the CI admission-harness check, M2's own compile-time
validation.build_admission_results) has used FixtureRecordAnswerer, the
deterministic no-model stand-in - this is the first time the identical
battery/masking/grading pipeline runs against a real streaming voice-
generation call instead, per generation.py's own LiveModelAnswerer
docstring: "admission finally measures the real generation path, which is
the whole point of admission."

Records real token counts and prices them against the same sourced rate
card engine/m8/live_cost_run.py already documents (spec principle 13: a
price table must name where its numbers came from - an estimate against
a published rate card, not yet a reconciled AWS invoice). This script
never touches generation.py/harness.py/results.py to get those counts -
a thin usage-recording proxy wraps the real client instead, so
admission's own answer path (assemble_evidence -> stream_voice_turn ->
check_turn) runs completely unmodified, exactly as it will for a real
participant.

Before any billed call, the estimated total cost for every requested
world (each world's own latest real cost, or the highest real cost
observed anywhere, for a world with no report of its own yet) must be at
or under --max-usd. Running, before each next world's own calls, the
same check applies again against the actual spend recorded so far -
real per-world costs vary enough (by system-prompt size and answer
length) that the preflight total alone does not bound a many-world run.

With --save-transcripts, every probe's entry also keeps its transcript:
the reply as graded, the raw tagged reply the model returned, its
citations, the request settings, the stop reason and the timings. The
battery, masking and grading are unchanged by the flag; it only records
what the run already produced, for the standing-measure suite to read.
--settings-only prints the run settings and the preflight estimate and
exits before any billed call.

Writes engine/m3/reports/live-admission-report.json - a by-hand report,
same pattern as the three scripts above, not
validation/admission/results.json (that path is M2's own compile-time
artifact, built from the fixture-harness run baked into each world's
package; this script's job is to report a live result, not to replace
that baked-in mock one).
"""
import argparse
import hashlib
import inspect
import json
import re
import subprocess
import sys
import time
from dataclasses import asdict
from pathlib import Path

from engine.m1.loader import load_fleet_records, load_world_records
from engine.m1.registry import formation_world_keys, load_registry
from engine.m3 import harness, protocol, results
from engine.m2.manifest import package_content_hash
from engine.m3.generation import LiveModelAnswerer
from engine.m4.generation import stream_voice_turn
from engine.m4.world_loader import LazyWorldLoader
from engine.m8.cost import estimate_cost
from engine.m8.live_cost_run import SONNET_4_5_PRICE_TABLE
from engine.provider import guard
from engine.provider.bedrock import NormalizedUsage, make_client, normalize_usage, resolve_model_id
from engine.shape import shape_hash, shape_text

REPO_ROOT = Path(__file__).resolve().parents[2]
REPORTS_DIR = Path(__file__).resolve().parent / "reports"
REPORT_PATH = REPORTS_DIR / "live-admission-report.json"

# Per-run authorization is required every time, named on the command line.
# The original hardcoded ["alx", "desert"] scope became a --worlds argument
# once the remaining four worlds needed single admission too - the
# authorization discipline is unchanged: the
# person running this passes exactly the worlds authorized for the run, and the
# report records which they were.
DEFAULT_WORLD_KEYS = ["alx", "desert"]

DEFAULT_VOICE_MODEL_PATTERN = "us.anthropic.claude-sonnet-4-5"

# --max-usd defaults to this ceiling; going above it takes an explicit,
# higher --max-usd on the command line - the default itself is the
# ceiling, so nothing above it is ever silent. No weekly or aggregate cap:
# this bounds one run.
DEFAULT_MAX_USD = 3.00

# A real observed run's own usage (engine/m3/reports/live-admission-report-
# alx-2026-09-08-postfix.json: alx, 28 probes - protocol.battery()'s own
# fixed size, one per sealed cell), priced against the same real, sourced
# rate card engine.m8.live_cost_run.SONNET_4_5_PRICE_TABLE already
# documents (Anthropic's published API rate card) -
# this module invents no price of its own, per spec principle 13. Used
# only as estimate_world_cost_usd's own last-resort fallback, for the
# case where no world anywhere has a real report yet.
_OBSERVED_RUN_USAGE = NormalizedUsage(
    input_tokens=24_048, output_tokens=14_189,
    cache_creation_input_tokens=14_792, cache_read_input_tokens=399_384,
)
_OBSERVED_RUN_PROBE_COUNT = 28

_REPORT_DATE_RE = re.compile(r"(\d{4}-\d{2}-\d{2})")


def _usage_cost(info: dict) -> float:
    usage = NormalizedUsage(
        input_tokens=info.get("total_input_tokens", 0),
        output_tokens=info.get("total_output_tokens", 0),
        cache_creation_input_tokens=info.get("total_cache_creation_input_tokens", 0),
        cache_read_input_tokens=info.get("total_cache_read_input_tokens", 0),
    )
    return estimate_cost(usage, SONNET_4_5_PRICE_TABLE).dollars


def real_world_costs(reports_dir: Path = REPORTS_DIR) -> dict[str, float]:
    """Every world's own cost from its LATEST live-admission report on
    disk (by the ISO date in the report's own filename), priced against
    the same rate card as everywhere else here. Real per-world costs vary
    a lot by system-prompt size and answer length - don $0.715, gallic
    $0.71, cappadocian $0.57, witt $0.55, several others near $0.45 - so a
    single flat per-world figure is not a safe preflight basis."""
    best_date: dict[str, str] = {}
    best_cost: dict[str, float] = {}
    for path in sorted(reports_dir.glob("live-admission-report*.json")):
        date_m = _REPORT_DATE_RE.search(path.name)
        if not date_m:
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            continue
        worlds = data.get("worlds")
        if not isinstance(worlds, dict):
            continue
        for world_key, info in worlds.items():
            if not isinstance(info, dict) or "total_input_tokens" not in info:
                continue
            date = date_m.group(1)
            if world_key in best_date and date <= best_date[world_key]:
                continue
            best_date[world_key] = date
            best_cost[world_key] = _usage_cost(info)
    return best_cost


def estimate_world_cost_usd(world_key: str, real_costs: dict[str, float] | None = None) -> float:
    """This world's own latest observed cost, or the highest cost observed
    for any world with a real report, as a conservative fallback for a
    world with no live-admission report of its own yet."""
    real_costs = real_costs if real_costs is not None else real_world_costs()
    if world_key in real_costs:
        return real_costs[world_key]
    if real_costs:
        return max(real_costs.values())
    per_probe = estimate_cost(_OBSERVED_RUN_USAGE, SONNET_4_5_PRICE_TABLE).dollars / _OBSERVED_RUN_PROBE_COUNT
    return per_probe * len(protocol.battery())


def estimate_run_cost_usd(world_keys: list[str], real_costs: dict[str, float] | None = None) -> float:
    """The preflight total for a whole run: each requested world's own
    estimate (real_world_costs()'s per-world figure, or the conservative
    fallback), summed."""
    real_costs = real_costs if real_costs is not None else real_world_costs()
    return sum(estimate_world_cost_usd(w, real_costs) for w in world_keys)


class _UsageRecordingStream:
    """Wraps the real stream object just enough to intercept
    get_final_message()'s usage, raw text and stop reason, and the time of
    the first text chunk - text_stream yields exactly the inner chunks, so
    stream_voice_turn (engine/m4/generation.py) sees nothing different
    about the client it was handed."""

    def __init__(self, inner, log, call):
        self._inner = inner
        self._log = log
        self._call = call
        self.text_stream = self._timed(inner.text_stream)

    def _timed(self, chunks):
        for chunk in chunks:
            if "seconds_to_first_text" not in self._call:
                self._call["seconds_to_first_text"] = round(time.monotonic() - self._call["_started"], 3)
            yield chunk

    def get_final_message(self):
        message = self._inner.get_final_message()
        self._log.append(message.usage)
        self._call["raw_text"] = "".join(
            getattr(block, "text", "") for block in (message.content or []) if getattr(block, "type", None) == "text"
        )
        self._call["stop_reason"] = getattr(message, "stop_reason", None)
        return message


class _UsageRecordingStreamCtx:
    def __init__(self, inner_ctx, log, call):
        self._inner_ctx = inner_ctx
        self._log = log
        self._call = call

    def __enter__(self):
        return _UsageRecordingStream(self._inner_ctx.__enter__(), self._log, self._call)

    def __exit__(self, *exc):
        self._call["seconds_total"] = round(time.monotonic() - self._call.pop("_started"), 3)
        return self._inner_ctx.__exit__(*exc)


class _UsageRecordingMessages:
    def __init__(self, inner):
        self._inner = inner
        self.log: list = []
        self.calls: list[dict] = []

    def stream(self, **kwargs):
        call = {
            "request": {"model": kwargs.get("model"), "max_tokens": kwargs.get("max_tokens")},
            "_started": time.monotonic(),
        }
        self.calls.append(call)
        return _UsageRecordingStreamCtx(self._inner.stream(**kwargs), self.log, call)


class _UsageRecordingClient:
    """One log per LiveModelAnswerer/world, in call order - LiveModelAnswerer
    never raises NoCoverageError (only FixtureRecordAnswerer does, per
    generation.py), so every probe in the battery makes exactly one
    streaming call and this log lines up 1:1 with run_battery's own
    results list, in the same order."""

    def __init__(self, inner):
        self.messages = _UsageRecordingMessages(inner.messages)


class _RecordingAnswerer:
    """Passes every answer() call to the real answerer and keeps the
    AnswerResult it returned, in call order, without changing it."""

    def __init__(self, inner):
        self._inner = inner
        self.answers: list = []

    def answer(self, cell: str, probe_text: str):
        result = self._inner.answer(cell, probe_text)
        self.answers.append(result)
        return result


def _transcript(answer, call: dict) -> dict:
    return {
        "answer_text": answer.text,
        "raw_text": call.get("raw_text"),
        "citations": list(answer.citations),
        "citation_entries": answer.citation_entries,
        "request": call["request"],
        "stop_reason": call.get("stop_reason"),
        "seconds_to_first_text": call.get("seconds_to_first_text"),
        "seconds_total": call.get("seconds_total"),
    }


def seal_hash(seals_path: Path = protocol.SEALS_PATH) -> str:
    """sha256 over the sealed battery's own seals file - the file that
    names every probe and the hash of its plaintext."""
    return "sha256:" + hashlib.sha256(seals_path.read_bytes()).hexdigest()


def _repo_commit() -> str | None:
    try:
        return subprocess.run(
            ["git", "rev-parse", "HEAD"], cwd=REPO_ROOT, capture_output=True, text=True, check=True
        ).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return None


def run_settings(*, registry: dict, world_keys: list[str], region: str, voice_model_id: str, max_usd: float,
                 save_transcripts: bool, probe_limit: int | None = None) -> dict:
    """Every setting that decides what this paid run produces, printed
    before the first billed call and kept in the report."""
    return {
        "voice_model_id": voice_model_id,
        "voice_max_tokens": inspect.signature(stream_voice_turn).parameters["max_tokens"].default,
        "voice_temperature": "API default (not set by stream_voice_turn)",
        "safety_model_id": None,
        "safety_call": "not made - LiveModelAnswerer answers each sealed probe with the voice call only",
        "reader_call": "not made - not in the admission harness path",
        "self_revision": "off - not in the admission harness path",
        "region": region,
        "package_manifest_hash": {w: registry[w]["package"]["manifest_hash"] for w in world_keys},
        "package_content_hash": {w: package_content_hash(REPO_ROOT / registry[w]["package"]["location"]) for w in world_keys},
        "shape_hash": shape_hash(shape_text()),
        "seal_hash": seal_hash(),
        "battery_size": len(protocol.battery()[:probe_limit]),
        "probe_limit": probe_limit,
        "max_usd": max_usd,
        "save_transcripts": save_transcripts,
        "repo_commit": _repo_commit(),
    }


def _run_world(world_key: str, *, registry: dict, loader: LazyWorldLoader, voice_model_id: str, region: str, canon_questions: dict,
               save_transcripts: bool = False, probe_limit: int | None = None) -> dict:
    """One world's own full battery, against a real, billed streaming
    call per probe - battery size, pass count, per-probe detail, real
    token totals, and the real USD cost priced from them."""
    entry = registry[world_key]
    world, _timing = loader.load(
        world_key, package_dir=REPO_ROOT / entry["package"]["location"], expected_manifest_hash=entry["package"]["manifest_hash"]
    )
    clean_records = load_world_records(world_key)

    recording_client = _UsageRecordingClient(make_client(region))
    answerer = _RecordingAnswerer(
        LiveModelAnswerer(world=world, canon_questions=canon_questions, client=recording_client, model_id=voice_model_id)
    )

    battery = harness.run_battery(world_key, clean_records, answerer=answerer, limit=probe_limit)
    results_doc = results.build_results(world_key, battery, mock_harness=False)

    usage_log = recording_client.messages.log
    if len(usage_log) != len(battery):
        raise RuntimeError(
            f"{world_key}: {len(usage_log)} usage records for {len(battery)} probes - "
            "expected exactly one streaming call per probe"
        )
    normalized = [normalize_usage(u) for u in usage_log]
    calls = recording_client.messages.calls
    if save_transcripts and not (len(calls) == len(answerer.answers) == len(battery)):
        raise RuntimeError(
            f"{world_key}: {len(calls)} calls and {len(answerer.answers)} answers for {len(battery)} probes - "
            "expected exactly one of each per probe"
        )

    per_probe = [
        {
            "probe_id": r.probe_id,
            "cell": r.cell,
            "passed": r.passed,
            "checks": r.checks,
            "usage": asdict(u),
            # Failing probes keep their answer text so a register flag
            # can actually be READ (a human read is the instrument; the
            # heuristic is its stand-in). Failing only, and never the
            # probe text: an answer can paraphrase its sealed probe,
            # so the bound stays as tight as the read requires.
            **({"answer_text": r.answer_text} if not r.passed else {}),
            **({"transcript": _transcript(answerer.answers[i], calls[i])} if save_transcripts else {}),
        }
        for i, (r, u) in enumerate(zip(battery, normalized))
    ]

    world_usage = {
        "total_input_tokens": sum(u.input_tokens for u in normalized),
        "total_output_tokens": sum(u.output_tokens for u in normalized),
        "total_cache_creation_input_tokens": sum(u.cache_creation_input_tokens for u in normalized),
        "total_cache_read_input_tokens": sum(u.cache_read_input_tokens for u in normalized),
    }
    return {
        "battery_size": len(battery),
        "pass_count": sum(1 for r in battery if r.passed),
        "overall_pass": results_doc["overall_pass"],
        "per_probe": per_probe,
        "actual_usd": _usage_cost(world_usage),
        **world_usage,
    }


def run(region: str, world_keys: list[str] | None = None, *, max_usd: float = DEFAULT_MAX_USD, authorized_by: str,
        voice_model_pattern: str = DEFAULT_VOICE_MODEL_PATTERN, save_transcripts: bool = False,
        settings_only: bool = False, probe_limit: int | None = None) -> dict:
    registry = load_registry()
    formation_keys = set(formation_world_keys(registry))
    requested = world_keys or DEFAULT_WORLD_KEYS
    unknown = [w for w in requested if w not in formation_keys]
    if unknown:
        raise SystemExit(
            f"--worlds names {unknown} - not a real formation world in the registry "
            f"(records/worlds/<code>.yaml). Live-billed, so a typo widening or narrowing "
            f"the authorized scope fails loudly here rather than deep inside a paid run. "
            f"Formation worlds: {sorted(formation_keys)}"
        )
    if not authorized_by.strip():
        raise SystemExit("--authorized-by is required and cannot be blank - every live-billed run names who authorized it")
    real_costs = real_world_costs()
    share = len(protocol.battery()[:probe_limit]) / len(protocol.battery())
    per_world_estimates = {w: estimate_world_cost_usd(w, real_costs) * share for w in requested}
    preflight_total = sum(per_world_estimates.values())
    if preflight_total > max_usd:
        breakdown = ", ".join(f"{w}=${c:.2f}" for w, c in per_world_estimates.items())
        raise SystemExit(
            f"preflight estimate ${preflight_total:.2f} for {requested} ({breakdown}) exceeds "
            f"--max-usd ${max_usd:.2f} - aborting before any billed call is made. Raise --max-usd "
            f"if this spend is actually authorized, or narrow --worlds."
        )
    loader = LazyWorldLoader()
    voice_model_id = resolve_model_id(voice_model_pattern, region)
    settings = run_settings(
        registry=registry, world_keys=requested, region=region, voice_model_id=voice_model_id, max_usd=max_usd,
        save_transcripts=save_transcripts, probe_limit=probe_limit,
    )
    print(json.dumps({"run_settings": settings, "per_world_estimated_usd": per_world_estimates,
                      "estimated_usd_preflight": preflight_total}, indent=2), file=sys.stderr, flush=True)
    if settings_only:
        return {"run_settings": settings, "per_world_estimated_usd": per_world_estimates,
                "estimated_usd_preflight": preflight_total, "settings_only": True}

    canon_questions = load_fleet_records()
    per_world = {}
    spent_so_far = 0.0
    aborted_reason = None

    for world_key in requested:
        next_estimate = per_world_estimates[world_key]
        if spent_so_far + next_estimate > max_usd:
            aborted_reason = (
                f"${spent_so_far:.2f} already spent plus {world_key}'s own estimate ${next_estimate:.2f} "
                f"would exceed --max-usd ${max_usd:.2f} - stopped before {world_key}'s own billed calls. "
                f"{len(per_world)} world(s) already ran and were billed; their real usage is recorded "
                f"in this report's own worlds/actual_usd_spent fields."
            )
            break
        world_result = _run_world(world_key, registry=registry, loader=loader, voice_model_id=voice_model_id, region=region,
                                  canon_questions=canon_questions, save_transcripts=save_transcripts, probe_limit=probe_limit)
        spent_so_far += world_result["actual_usd"]
        per_world[world_key] = world_result

    report = {
        "voice_model_id": voice_model_id,
        "region": region,
        "run_settings": settings,
        "protocol": "blind",
        "worlds": per_world,
        "overall_pass": aborted_reason is None and all(w["overall_pass"] for w in per_world.values()),
        "authorized_by": authorized_by,
        "max_usd": max_usd,
        "per_world_estimated_usd": per_world_estimates,
        "estimated_usd_preflight": preflight_total,
        "actual_usd_spent": spent_so_far,
        "aborted_reason": aborted_reason,
        "note": (
            "Real, billed admission run - LiveModelAnswerer against a live Bedrock voice-generation "
            "call, once per probe, for every probe in the sealed battery, per world. Token counts are "
            "measured directly from each call's own usage and priced against the same real, sourced "
            "rate card engine.m8.live_cost_run.SONNET_4_5_PRICE_TABLE documents - a $/token figure is "
            "fair game here (spec principle 13), though it is an estimate against a published rate "
            "card, not a reconciled AWS invoice. Preflight-estimated per world against max_usd before "
            "any billed call was made, then checked again, running, before each next world's own calls, "
            "against the actual spend recorded so far."
        ),
    }
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    guard.add_arguments(parser)
    parser.add_argument("--region", required=True)
    parser.add_argument("--worlds", default=",".join(DEFAULT_WORLD_KEYS),
                        help="comma-separated world keys, exactly as authorized for this run")
    parser.add_argument("--max-usd", type=float, default=DEFAULT_MAX_USD,
                        help=f"cost ceiling in USD (default ${DEFAULT_MAX_USD:.2f}, no weekly/aggregate cap) - "
                             f"the run aborts before any billed call if the preflight total exceeds this, and "
                             f"again, running, before each next world's own calls if spend so far plus that "
                             f"world's own estimate would; pass a higher value explicitly to authorize more")
    parser.add_argument("--authorized-by", required=True,
                        help="who authorized this specific live-billed run - recorded in the report, never blank")
    parser.add_argument("--voice-model", default=DEFAULT_VOICE_MODEL_PATTERN,
                        help="inference-profile pattern for the voice model; must match exactly one profile")
    parser.add_argument("--save-transcripts", action="store_true",
                        help="keep every probe's transcript (graded reply, raw reply, citations, request, stop reason, "
                             "timings) in the report; grading is unchanged")
    parser.add_argument("--settings-only", action="store_true",
                        help="print the run settings and preflight estimate, then exit before any billed call")
    parser.add_argument("--probe-limit", type=int, default=None,
                        help="run only the battery's first N probes, as a sample before the paid run; a sample is "
                             "never admission evidence and must be written outside engine/m3/reports")
    parser.add_argument("--out", default=str(REPORT_PATH),
                        help="report path - use a distinct file so prior runs' records survive")
    args = parser.parse_args()

    world_keys = [k.strip() for k in args.worlds.split(",") if k.strip()]
    if args.probe_limit is not None and Path(args.out).resolve().is_relative_to(REPORTS_DIR.resolve()):
        raise SystemExit("--probe-limit writes a sample, which is not admission evidence; pass --out outside engine/m3/reports")
    report = run(args.region, world_keys=world_keys, max_usd=args.max_usd, authorized_by=args.authorized_by,
                 voice_model_pattern=args.voice_model, save_transcripts=args.save_transcripts,
                 settings_only=args.settings_only, probe_limit=args.probe_limit)
    if report.get("settings_only"):
        return 0
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

    summary = {
        "voice_model_id": report["voice_model_id"],
        "region": report["region"],
        "overall_pass": report["overall_pass"],
        "max_usd": report["max_usd"],
        "estimated_usd_preflight": report["estimated_usd_preflight"],
        "actual_usd_spent": report["actual_usd_spent"],
        "aborted_reason": report["aborted_reason"],
        "worlds": {
            k: {
                "battery_size": v["battery_size"],
                "pass_count": v["pass_count"],
                "overall_pass": v["overall_pass"],
                "actual_usd": v["actual_usd"],
                "total_input_tokens": v["total_input_tokens"],
                "total_output_tokens": v["total_output_tokens"],
                "total_cache_creation_input_tokens": v["total_cache_creation_input_tokens"],
                "total_cache_read_input_tokens": v["total_cache_read_input_tokens"],
                "failing_probes": [p["probe_id"] for p in v["per_probe"] if not p["passed"]],
            }
            for k, v in report["worlds"].items()
        },
    }
    print(json.dumps(summary, indent=2))
    return 0 if report["overall_pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
