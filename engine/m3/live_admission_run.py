"""Live (real Bedrock spend) M3 admission run against alx and desert -
Mark's explicit authorization, 2026-08-28: "authorize the live M3 run
against alx and desert." Every prior run of this battery in this repo
(selftest.py, the CI admission-harness check, M2's own compile-time
validation.build_admission_results) has used FixtureRecordAnswerer, the
deterministic no-model stand-in - this is the first time the identical
battery/masking/grading pipeline runs against a real streaming voice-
generation call instead, per generation.py's own LiveModelAnswerer
docstring: "admission finally measures the real generation path, which is
the whole point of admission."

Same discipline as every other live-billed script in this repo
(engine/provider/preflight.py, engine/m8/live_memory_growth_run.py,
engine/m8/live_cost_run.py): records real token counts (spec principle 13
- token counts are fair game, a $/token or $/turn figure is not, until
reconciled against a real AWS invoice) and never quotes one here. This
script never touches generation.py/harness.py/results.py to get those
counts - a thin usage-recording proxy wraps the real client instead, so
admission's own answer path (assemble_evidence -> stream_voice_turn ->
check_turn) runs completely unmodified, exactly as it will for a real
participant.

Writes engine/m3/reports/live-admission-report.json - a by-hand report,
same pattern as the three scripts above, not
validation/admission/results.json (that path is M2's own compile-time
artifact, built from the fixture-harness run baked into each world's
package; this script's job is to report a live result, not to replace
that baked-in mock one).
"""
import argparse
import json
import sys
from dataclasses import asdict
from pathlib import Path

from engine.m1.loader import load_fleet_records, load_world_records
from engine.m1.registry import load_registry
from engine.m3 import harness, results
from engine.m3.generation import LiveModelAnswerer
from engine.m4.world_loader import LazyWorldLoader
from engine.provider.bedrock import make_client, normalize_usage, resolve_model_id

REPO_ROOT = Path(__file__).resolve().parents[2]
REPORT_PATH = Path(__file__).resolve().parent / "reports" / "live-admission-report.json"

# Per-run authorization is Mark's, every time, named on the command line.
# The original hardcoded ["alx", "desert"] scope (his 2026-08-28
# authorization for the first run) became a --worlds argument when he
# authorized the remaining four ("lets do the other four worlds single
# admission", same date) - the authorization discipline is unchanged: the
# person running this passes exactly the worlds Mark authorized, and the
# report records which they were.
DEFAULT_WORLD_KEYS = ["alx", "desert"]


class _UsageRecordingStream:
    """Wraps the real stream object just enough to intercept
    get_final_message()'s usage - text_stream passes through untouched,
    so stream_voice_turn (engine/m4/generation.py) sees nothing different
    about the client it was handed."""

    def __init__(self, inner, log):
        self._inner = inner
        self._log = log
        self.text_stream = inner.text_stream

    def get_final_message(self):
        message = self._inner.get_final_message()
        self._log.append(message.usage)
        return message


class _UsageRecordingStreamCtx:
    def __init__(self, inner_ctx, log):
        self._inner_ctx = inner_ctx
        self._log = log

    def __enter__(self):
        return _UsageRecordingStream(self._inner_ctx.__enter__(), self._log)

    def __exit__(self, *exc):
        return self._inner_ctx.__exit__(*exc)


class _UsageRecordingMessages:
    def __init__(self, inner):
        self._inner = inner
        self.log: list = []

    def stream(self, **kwargs):
        return _UsageRecordingStreamCtx(self._inner.stream(**kwargs), self.log)


class _UsageRecordingClient:
    """One log per LiveModelAnswerer/world, in call order - LiveModelAnswerer
    never raises NoCoverageError (only FixtureRecordAnswerer does, per
    generation.py), so every probe in the battery makes exactly one
    streaming call and this log lines up 1:1 with run_battery's own
    results list, in the same order."""

    def __init__(self, inner):
        self.messages = _UsageRecordingMessages(inner.messages)


def run(region: str, world_keys: list[str] | None = None) -> dict:
    registry = load_registry()
    loader = LazyWorldLoader()
    voice_model_id = resolve_model_id("us.anthropic.claude-sonnet-4-5", region)

    canon_questions = load_fleet_records()
    per_world = {}

    for world_key in (world_keys or DEFAULT_WORLD_KEYS):
        entry = registry[world_key]
        world, _timing = loader.load(
            world_key, package_dir=REPO_ROOT / entry["package"]["location"], expected_manifest_hash=entry["package"]["manifest_hash"]
        )
        clean_records = load_world_records(world_key)

        recording_client = _UsageRecordingClient(make_client(region))
        answerer = LiveModelAnswerer(world=world, canon_questions=canon_questions, client=recording_client, model_id=voice_model_id)

        battery = harness.run_battery(world_key, clean_records, answerer=answerer)
        results_doc = results.build_results(world_key, battery, mock_harness=False)

        usage_log = recording_client.messages.log
        if len(usage_log) != len(battery):
            raise RuntimeError(
                f"{world_key}: {len(usage_log)} usage records for {len(battery)} probes - "
                "expected exactly one streaming call per probe"
            )
        normalized = [normalize_usage(u) for u in usage_log]

        per_probe = [
            {
                "probe_id": r.probe_id,
                "cell": r.cell,
                "passed": r.passed,
                "checks": r.checks,
                "usage": asdict(u),
                # Failing probes keep their answer text so a register flag
                # can actually be READ (Mark's read is the instrument; the
                # heuristic is its stand-in). Failing only, and never the
                # probe text: an answer can paraphrase its sealed probe,
                # so the bound stays as tight as the read requires.
                **({"answer_text": r.answer_text} if not r.passed else {}),
            }
            for r, u in zip(battery, normalized)
        ]

        per_world[world_key] = {
            "battery_size": len(battery),
            "pass_count": sum(1 for r in battery if r.passed),
            "overall_pass": results_doc["overall_pass"],
            "per_probe": per_probe,
            "total_input_tokens": sum(u.input_tokens for u in normalized),
            "total_output_tokens": sum(u.output_tokens for u in normalized),
            "total_cache_creation_input_tokens": sum(u.cache_creation_input_tokens for u in normalized),
            "total_cache_read_input_tokens": sum(u.cache_read_input_tokens for u in normalized),
        }

    report = {
        "voice_model_id": voice_model_id,
        "region": region,
        "protocol": "blind",
        "worlds": per_world,
        "overall_pass": all(w["overall_pass"] for w in per_world.values()),
        "note": (
            "Real, billed admission run - LiveModelAnswerer against a live Bedrock voice-generation "
            "call, once per probe, for every probe in the sealed battery, per world. Token counts "
            "are measured directly from each call's own usage; no $/token or $/turn figure is quoted "
            "here (spec principle 13 - that waits on a reconciled AWS invoice, not an estimate). "
            "Run under Mark's explicit per-run authorization for exactly the worlds listed above."
        ),
    }
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--region", required=True)
    parser.add_argument("--worlds", default=",".join(DEFAULT_WORLD_KEYS),
                        help="comma-separated world keys, exactly as Mark authorized for this run")
    parser.add_argument("--out", default=str(REPORT_PATH),
                        help="report path - use a distinct file so prior runs' records survive")
    args = parser.parse_args()

    world_keys = [k.strip() for k in args.worlds.split(",") if k.strip()]
    report = run(args.region, world_keys=world_keys)
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

    summary = {
        "voice_model_id": report["voice_model_id"],
        "region": report["region"],
        "overall_pass": report["overall_pass"],
        "worlds": {
            k: {
                "battery_size": v["battery_size"],
                "pass_count": v["pass_count"],
                "overall_pass": v["overall_pass"],
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
