"""Live (billed) M3 admission run: the sealed battery answered through the
conversation path, one fresh interview session per probe.

Each probe goes through engine.m3.generation.LiveModelAnswerer, which calls
engine.m4.turn.run_turn: the gate (safety and reader), routing, the per-turn
directive, evidence assembly, the voice call, the recital retry,
self-revision where the deployment runs it, the net and the settled reply. The
model ids and the four flags that change a turn are read from the
production service in render.yaml. The battery, masking and grading are
unchanged.

Every run names who authorized it and carries an approved live test (--live-test
and --cap-usd, engine.provider.guard). Before any billed call it prints the run
settings and a preflight estimate, and it stops when the estimate for the next
world would pass --max-usd. Each probe's answer is appended to
<out>.answers.jsonl the moment it returns, so a run that stops partway keeps
every answer it paid for.

With --save-transcripts each probe's entry also keeps its transcript: the
reply as graded, the raw tagged draft of every voice call, the route and the
reader's reading, what the net removed and why, the calls' usage, and the
timings. --settings-only prints the run settings and the preflight estimate
and exits before any billed call.

Costs are priced against the rate card in engine.m8.price_tables, an estimate
against a published rate card and not a reconciled invoice.
"""
import argparse
import hashlib
import inspect
import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

from engine.m1.loader import load_world_records
from engine.m1.registry import formation_world_keys, load_registry
from engine.m3 import harness, protocol, results
from engine.m2.manifest import package_content_hash
from engine.m3.generation import AnswerUnavailable, LivePathSettings, LiveModelAnswerer, RENDER_YAML, RESENDS, production_settings
from engine.m4.generation import stream_voice_turn
from engine.m4.world_loader import LazyWorldLoader
from engine.m8.cost import estimate_cost
from engine.m8.live_cost_run import SONNET_4_5_PRICE_TABLE
from engine.m8.price_tables import price_for_model
from engine.provider import guard
from engine.provider.bedrock import NormalizedUsage, make_client, resolve_model_id
from engine.shape import shape_hash, shape_text

REPO_ROOT = Path(__file__).resolve().parents[2]
REPORTS_DIR = Path(__file__).resolve().parent / "reports"
REPORT_PATH = REPORTS_DIR / "live-admission-report.json"

# The worlds a run covers are named on the command line, exactly as authorized.
DEFAULT_WORLD_KEYS = ["alx", "desert"]

LIVE_COST_REPORT = REPO_ROOT / "engine" / "m8" / "reports" / "live-cost-report.json"

# --max-usd defaults to this ceiling; going above it takes an explicit,
# higher --max-usd on the command line. It bounds one run.
DEFAULT_MAX_USD = 3.00


def live_path_turn_ceiling_usd(report_path: Path = LIVE_COST_REPORT) -> float:
    """The highest cost of one whole live-path turn (gate calls and voice call)
    in the measured conversation run, priced at the Sonnet 4.5 and Haiku 4.5 rates."""
    report = json.loads(report_path.read_text(encoding="utf-8"))
    return max(turn["turn_dollars"] for world in report["worlds"].values() for turn in world["turns"])


def estimate_world_cost_usd(probes: int, voice_model_id: str, ceiling_usd: float | None = None) -> float:
    """A preflight ceiling for one world: the measured per-turn ceiling for every
    probe, scaled by the voice model's output price against Sonnet 4.5's when the
    run overrides the voice model. A send that fails and is sent again is not counted;
    the live-test cap bounds it."""
    ceiling = live_path_turn_ceiling_usd() if ceiling_usd is None else ceiling_usd
    table = price_for_model(voice_model_id)
    if table is None:
        raise RuntimeError(f"no approved price for voice model {voice_model_id!r}")
    return ceiling * probes * table.output_per_token / SONNET_4_5_PRICE_TABLE.output_per_token


class _RecordingAnswerer:
    """Passes every answer() call to the real answerer and keeps the
    AnswerResult it returned, in call order, without changing it. A probe
    the live path could not answer is kept as None."""

    def __init__(self, inner, spill_path: Path | None = None):
        self._inner = inner
        self.answers: list = []
        self._spill_path = spill_path

    def answer(self, cell: str, probe_text: str):
        try:
            result = self._inner.answer(cell, probe_text)
        except AnswerUnavailable:
            self.answers.append(None)
            raise
        self.answers.append(result)
        if self._spill_path is not None:
            line = {"index": len(self.answers) - 1, "cell": cell, **_transcript(result)}
            with open(self._spill_path, "a", encoding="utf-8") as f:
                f.write(json.dumps(line) + "\n")
                f.flush()
                os.fsync(f.fileno())
        return result


def _transcript(answer) -> dict:
    turn = answer.live_turn
    event = turn.voice_event or {}
    return {
        "answer_text": answer.text,
        "citations": list(answer.citations),
        "citation_entries": answer.citation_entries,
        "routing_action": turn.routing_action,
        "routing_reason": turn.routing_reason,
        "reader": turn.gate,
        "drafts": [
            {k: call.get(k) for k in ("raw_text", "stop_reason", "request", "seconds_to_first_text", "seconds_total")}
            for call in turn.voice_calls
        ],
        "kind": event.get("kind"),
        "offered_ids": event.get("offered_ids"),
        "reply_shape": event.get("reply_shape"),
        "answer_record_fallback": event.get("answer_record_fallback"),
        "degraded_by_net": event.get("degraded_by_net"),
        "attempts_meta": event.get("attempts_meta"),
        "facilitator_events": turn.facilitator_events,
        "usage": turn.usage,
        "sends": turn.sends,
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


def live_path_settings(region: str, *, voice_model_pattern: str | None = None, safety_model_pattern: str | None = None,
                       self_revision: bool | None = None) -> LivePathSettings:
    """The production service's own settings, with the two model patterns
    and the self-revision switch open to override for a named variant."""
    production = production_settings()
    return LivePathSettings(
        voice_model_id=resolve_model_id(voice_model_pattern or production["voice_model_pattern"], region),
        safety_model_id=resolve_model_id(safety_model_pattern or production["safety_model_pattern"], region),
        r27_enforce=production["r27_enforce"],
        streaming_enabled=production["streaming_enabled"],
        self_revision_enabled=production["self_revision_enabled"] if self_revision is None else self_revision,
        citation_attach_enabled=production["citation_attach_enabled"],
    )


def run_settings(*, registry: dict, world_keys: list[str], region: str, settings: LivePathSettings, max_usd: float,
                 save_transcripts: bool, probe_limit: int | None = None) -> dict:
    """Every setting that decides what this paid run produces, printed
    before the first billed call and kept in the report."""
    return {
        "path": "engine.m4.turn.run_turn, one fresh interview session per sealed probe",
        **settings.printable(),
        "voice_max_tokens": inspect.signature(stream_voice_turn).parameters["max_tokens"].default,
        "voice_temperature": "API default (not set by stream_voice_turn)",
        "resends_per_probe": RESENDS,
        "render_yaml_sha256": hashlib.sha256(RENDER_YAML.read_bytes()).hexdigest(),
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


def _priced_usage(turns: list) -> float:
    """What a world's answered sends cost, from their own usage records, each
    priced at its model's approved rate."""
    total = 0.0
    for turn in turns:
        for record in turn.usage:
            table = price_for_model(record["model_id"])
            if table is None:
                raise RuntimeError(f"no approved price for model {record['model_id']!r}")
            total += estimate_cost(NormalizedUsage(
                input_tokens=record["input_tokens"], output_tokens=record["output_tokens"],
                cache_creation_input_tokens=record["cache_creation_input_tokens"],
                cache_read_input_tokens=record["cache_read_input_tokens"],
            ), table).dollars
    return total


def _run_world(world_key: str, *, registry: dict, loader: LazyWorldLoader, settings: LivePathSettings, region: str,
               save_transcripts: bool = False, probe_limit: int | None = None, answers_path: Path | None = None) -> dict:
    """One world's own full battery through the live path: pass count,
    per-probe detail, and what the calls cost."""
    entry = registry[world_key]
    world, _timing = loader.load(
        world_key, package_dir=REPO_ROOT / entry["package"]["location"], expected_manifest_hash=entry["package"]["manifest_hash"]
    )
    clean_records = load_world_records(world_key)

    live = LiveModelAnswerer(world=world, registry=registry, client=make_client(region), settings=settings)
    answerer = _RecordingAnswerer(live, spill_path=answers_path)
    spent_before = guard.priced_total()

    battery = harness.run_battery(world_key, clean_records, answerer=answerer, limit=probe_limit)
    results_doc = results.build_results(world_key, battery, mock_harness=False)

    per_probe = []
    for r, answer in zip(battery, answerer.answers):
        turn = answer.live_turn if answer is not None else None
        per_probe.append({
            "probe_id": r.probe_id,
            "cell": r.cell,
            "passed": r.passed,
            "checks": r.checks,
            **({"error": r.error} if r.error else {}),
            "routing_action": turn.routing_action if turn else None,
            "sends": turn.sends if turn else None,
            "usage": turn.usage if turn else None,
            # Failing probes keep their answer text so a register flag can be
            # read by a person; never the probe text, which an answer can paraphrase.
            **({"answer_text": r.answer_text} if not r.passed and r.answer_text is not None else {}),
            **({"transcript": _transcript(answer)} if save_transcripts and answer is not None else {}),
        })
    return {
        "battery_size": len(battery),
        "pass_count": sum(1 for r in battery if r.passed),
        "unanswered": sum(1 for r in battery if r.error),
        "overall_pass": results_doc["overall_pass"],
        "per_probe": per_probe,
        "actual_usd": guard.priced_total() - spent_before,
        "priced_from_usage_usd": _priced_usage(live.turns),
    }


def run(region: str, world_keys: list[str] | None = None, *, max_usd: float = DEFAULT_MAX_USD, authorized_by: str,
        voice_model_pattern: str | None = None, safety_model_pattern: str | None = None, self_revision: bool | None = None,
        save_transcripts: bool = False,
        settings_only: bool = False, probe_limit: int | None = None, answers_path: Path | None = None,
        report_path: Path | None = None) -> dict:
    """report_path, when given, receives the report after every world and
    again at the end, so a stop or a crash part way through loses only the
    world it stopped in, never the worlds already paid for."""
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
    probes = len(protocol.battery()[:probe_limit])
    priced_pattern = voice_model_pattern or production_settings()["voice_model_pattern"]
    per_world_estimates = {w: estimate_world_cost_usd(probes, priced_pattern) for w in requested}
    preflight_total = sum(per_world_estimates.values())
    if preflight_total > max_usd:
        breakdown = ", ".join(f"{w}=${c:.2f}" for w, c in per_world_estimates.items())
        raise SystemExit(
            f"preflight estimate ${preflight_total:.2f} for {requested} ({breakdown}) exceeds "
            f"--max-usd ${max_usd:.2f} - aborting before any billed call is made. Raise --max-usd "
            f"if this spend is actually authorized, or narrow --worlds."
        )
    loader = LazyWorldLoader()
    path_settings = live_path_settings(
        region, voice_model_pattern=voice_model_pattern, safety_model_pattern=safety_model_pattern, self_revision=self_revision,
    )
    settings = run_settings(
        registry=registry, world_keys=requested, region=region, settings=path_settings, max_usd=max_usd,
        save_transcripts=save_transcripts, probe_limit=probe_limit,
    )
    print(json.dumps({"run_settings": settings, "per_world_estimated_usd": per_world_estimates,
                      "estimated_usd_preflight": preflight_total}, indent=2), file=sys.stderr, flush=True)
    if settings_only:
        return {"run_settings": settings, "per_world_estimated_usd": per_world_estimates,
                "estimated_usd_preflight": preflight_total, "settings_only": True}

    started_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    per_world = {}
    spent_so_far = 0.0
    aborted_reason = None

    def build_report(stopped: str | None) -> dict:
        return _assemble_report(started_at=started_at, region=region, settings=settings, per_world=per_world,
                                authorized_by=authorized_by, max_usd=max_usd, per_world_estimates=per_world_estimates,
                                preflight_total=preflight_total, spent_so_far=spent_so_far, aborted_reason=stopped)

    def write_so_far(stopped: str | None) -> None:
        if report_path is None:
            return
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(json.dumps(build_report(stopped), indent=2) + "\n", encoding="utf-8")

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
        try:
            world_result = _run_world(world_key, registry=registry, loader=loader, settings=path_settings, region=region,
                                      save_transcripts=save_transcripts, probe_limit=probe_limit, answers_path=answers_path)
        except guard.LiveTestCapReached as stop:
            # The live-test cap refused a call part way through this world.
            # The worlds already run keep their evidence; this world has none,
            # and the ledger, not this report, holds what its calls cost.
            aborted_reason = (
                f"{stop} - stopped during {world_key}'s own billed calls, which are not admission evidence. "
                f"{len(per_world)} world(s) completed before it and are reported here; the live-test ledger "
                f"holds the full spend including {world_key}'s calls."
            )
            break
        spent_so_far += world_result["actual_usd"]
        per_world[world_key] = world_result
        write_so_far(f"in progress: {len(per_world)} of {len(requested)} world(s) run" if len(per_world) < len(requested) else None)

    report = build_report(aborted_reason)
    write_so_far(aborted_reason)
    return report


def _assemble_report(*, started_at: str, region: str, settings: dict, per_world: dict, authorized_by: str, max_usd: float,
                     per_world_estimates: dict, preflight_total: float, spent_so_far: float, aborted_reason: str | None) -> dict:
    report = {
        "voice_model_id": settings["voice_model_id"],
        "safety_model_id": settings["safety_model_id"],
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
        "live_test": guard.run_summary(),
        "started_at": started_at,
        "finished_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "note": (
            "Billed admission run through the conversation path (engine.m4.turn.run_turn), one fresh interview "
            "session per sealed probe. actual_usd is the live-test guard's priced total for the world, every "
            "call included; priced_from_usage_usd is the answered sends' own usage at the approved rates; they "
            "differ by every call of a failed send (its gate calls at their price, its voice call at the guard's "
            "full hold) and of any unanswered probe. Preflight is estimated against "
            "max_usd before any billed call, then checked again, running, before each next world."
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
    parser.add_argument("--voice-model", default=None,
                        help="inference-profile pattern for the voice model; defaults to the production service's pin")
    parser.add_argument("--safety-model", default=None,
                        help="inference-profile pattern for the gate model; defaults to the production service's pin")
    parser.add_argument("--self-revision", choices=("on", "off"), default=None,
                        help="defaults to the production service's setting")
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
    out_path = Path(args.out)
    report = run(args.region, world_keys=world_keys, max_usd=args.max_usd, authorized_by=args.authorized_by,
                 voice_model_pattern=args.voice_model, safety_model_pattern=args.safety_model,
                 self_revision=None if args.self_revision is None else args.self_revision == "on", save_transcripts=args.save_transcripts,
                 settings_only=args.settings_only, probe_limit=args.probe_limit,
                 answers_path=Path(args.out + ".answers.jsonl") if args.save_transcripts else None,
                 report_path=None if args.settings_only else out_path)
    if report.get("settings_only"):
        return 0
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

    summary = {
        "voice_model_id": report["voice_model_id"],
        "safety_model_id": report["safety_model_id"],
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
                "unanswered": v["unanswered"],
                "priced_from_usage_usd": v["priced_from_usage_usd"],
                "failing_probes": [p["probe_id"] for p in v["per_probe"] if not p["passed"]],
            }
            for k, v in report["worlds"].items()
        },
    }
    print(json.dumps(summary, indent=2))
    return 0 if report["overall_pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
