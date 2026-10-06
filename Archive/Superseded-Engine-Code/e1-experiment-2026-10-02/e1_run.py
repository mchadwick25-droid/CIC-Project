"""Live (real Bedrock spend) E1 run: the sealed battery answered under one
alternative prompt layout, against the whole-world baseline that
engine.m3.live_admission_run measures.

  --arm c        cell dossier layout, the compiler's own record text, one
                 streaming call per probe (engine.m3.e1_answerers.DossierAnswerer)
  --arm native   the same layout with the dossier records as API documents
                 and the API's native citations, one non-streaming call per
                 probe (engine.m3.e1_answerers.NativeCitationAnswerer)

The battery, masking and grading are the admission pipeline unchanged. The
usage-recording proxy, settings print, --settings-only, --max-usd preflight
and running check, --authorized-by and --save-transcripts follow
engine.m3.live_admission_run. Token counts are priced against the table
engine.m8.price_tables.price_for_model names for the voice model.

The preflight estimate is an upper bound computed from the assembled
requests: every input character at the cache-write rate, three characters
per token, and max_tokens of output per probe. Before each next world's own
calls the same check runs against the spend recorded so far.

--save-transcripts keeps each probe's transcript with its manifest (arm,
cells chosen, dossier ids, prompt characters). --settings-only prints the
run settings and the preflight estimate and exits before any billed call.

Writes engine/m3/reports/e1/e1-report-<arm>.json unless --out names a file.
"""
import argparse
import inspect
import json
import sys
import time
from dataclasses import asdict
from pathlib import Path

from engine.m1.loader import load_fleet_records, load_world_records
from engine.m1.registry import formation_world_keys, load_registry
from engine.m3 import e1_layout, harness, protocol, results, sealed_probes
from engine.m3.e1_answerers import WholeWorldNativeAnswerer, DossierAnswerer, NativeCitationAnswerer, read_response
from engine.m3.live_admission_run import (
    DEFAULT_MAX_USD,
    DEFAULT_VOICE_MODEL_PATTERN,
    REPO_ROOT,
    _RecordingAnswerer,
    _UsageRecordingMessages,
    _transcript,
    run_settings,
)
from engine.m4.generation import stream_voice_turn
from engine.m4.world_loader import LazyWorldLoader
from engine.m8.cost import PriceTable, estimate_cost
from engine.m8.price_tables import price_for_model
from engine.provider.bedrock import NormalizedUsage, make_client, normalize_usage, resolve_model_id

REPORTS_DIR = Path(__file__).resolve().parent / "reports" / "e1"
ARMS = {"c": DossierAnswerer, "native": NativeCitationAnswerer, "native-whole": WholeWorldNativeAnswerer}
DEFAULT_WORLD_KEYS = ["alx", "desert"]
CHARS_PER_TOKEN = 3


class _E1Messages(_UsageRecordingMessages):
    """Adds the non-streaming call to the usage-recording proxy."""

    def create(self, **kwargs):
        call = {
            "request": {"model": kwargs.get("model"), "max_tokens": kwargs.get("max_tokens")},
            "_started": time.monotonic(),
        }
        self.calls.append(call)
        response = self._inner.create(**kwargs)
        self.log.append(response.usage)
        titles = [
            b["title"] for m in kwargs.get("messages") or [] if isinstance(m["content"], list)
            for b in m["content"] if b.get("type") == "document"
        ]
        call["raw_text"] = read_response(response, titles)[2]
        call["stop_reason"] = getattr(response, "stop_reason", None)
        call["seconds_total"] = round(time.monotonic() - call.pop("_started"), 3)
        return response


class _E1Client:
    def __init__(self, inner):
        self.messages = _E1Messages(inner.messages)


def _cost(usage: dict, table: PriceTable) -> float:
    return estimate_cost(
        NormalizedUsage(
            input_tokens=usage["total_input_tokens"],
            output_tokens=usage["total_output_tokens"],
            cache_creation_input_tokens=usage["total_cache_creation_input_tokens"],
            cache_read_input_tokens=usage["total_cache_read_input_tokens"],
        ),
        table,
    ).dollars


def _load_world(world_key: str, registry: dict, loader: LazyWorldLoader):
    entry = registry[world_key]
    world, _timing = loader.load(
        world_key, package_dir=REPO_ROOT / entry["package"]["location"], expected_manifest_hash=entry["package"]["manifest_hash"]
    )
    return world


def estimate_world_cost_usd(world_key: str, arm: str, table: PriceTable, *, registry: dict, loader: LazyWorldLoader,
                            canon_questions: dict, max_tokens: int) -> float:
    """Upper bound for one world's battery under `arm`, from the requests
    the answerer would send. Makes no call."""
    world = _load_world(world_key, registry, loader)
    answerer = ARMS[arm](world=world, canon_questions=canon_questions, client=None, model_id="")
    total = 0.0
    for seal in protocol.battery():
        probe_text = sealed_probes.read_probe(seal["probe_id"])["text"]
        if arm == "native-whole":
            system, documents = e1_layout.assemble_native_whole(world.prompt_text)
            prefix = (len(system) + sum(len(d["source"]["data"]) for d in documents)) / CHARS_PER_TOKEN
            first = total == 0.0
            total += (
                prefix * (table.cache_write_per_token if first else table.cache_read_per_token)
                + len(answerer.user_message(probe_text)) / CHARS_PER_TOKEN * table.input_per_token
                + max_tokens * table.output_per_token
            )
            continue
        cells = answerer.choose_cells(probe_text)
        if arm == "c":
            system = e1_layout.assemble_c(world.prompt_text, answerer.repository_records, cells)
            attached = 0
        else:
            system, documents = e1_layout.assemble_native(world.prompt_text, answerer.repository_records, cells)
            attached = sum(len(d["source"]["data"]) for d in documents)
        fresh = (attached + len(answerer.user_message(probe_text))) / CHARS_PER_TOKEN
        total += (
            len(system) / CHARS_PER_TOKEN * table.cache_write_per_token
            + fresh * table.cache_write_per_token
            + max_tokens * table.output_per_token
        )
    return total


def _run_world(world_key: str, *, arm: str, registry: dict, loader: LazyWorldLoader, voice_model_id: str, region: str,
               canon_questions: dict, table: PriceTable, save_transcripts: bool) -> dict:
    world = _load_world(world_key, registry, loader)
    clean_records = load_world_records(world_key)

    recording_client = _E1Client(make_client(region))
    inner = ARMS[arm](world=world, canon_questions=canon_questions, client=recording_client, model_id=voice_model_id)
    answerer = _RecordingAnswerer(inner)

    battery = harness.run_battery(world_key, clean_records, answerer=answerer)
    results_doc = results.build_results(world_key, battery, mock_harness=False)

    usage_log = recording_client.messages.log
    if len(usage_log) != len(battery):
        raise RuntimeError(f"{world_key}: {len(usage_log)} usage records for {len(battery)} probes - expected exactly one call per probe")
    calls = recording_client.messages.calls
    if not (len(calls) == len(answerer.answers) == len(inner.manifests) == len(battery)):
        raise RuntimeError(
            f"{world_key}: {len(calls)} calls, {len(answerer.answers)} answers and {len(inner.manifests)} manifests "
            f"for {len(battery)} probes - expected exactly one of each per probe"
        )
    normalized = [normalize_usage(u) for u in usage_log]

    per_probe = [
        {
            "probe_id": r.probe_id,
            "cell": r.cell,
            "passed": r.passed,
            "checks": r.checks,
            "usage": asdict(u),
            "manifest": inner.manifests[i],
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
        "actual_usd": _cost(world_usage, table),
        **world_usage,
    }


def run(region: str, arm: str, world_keys: list[str] | None = None, *, max_usd: float = DEFAULT_MAX_USD, authorized_by: str,
        voice_model_pattern: str = DEFAULT_VOICE_MODEL_PATTERN, save_transcripts: bool = False,
        settings_only: bool = False) -> dict:
    if arm not in ARMS:
        raise SystemExit(f"--arm must be one of {sorted(ARMS)}")
    registry = load_registry()
    formation_keys = set(formation_world_keys(registry))
    requested = world_keys or DEFAULT_WORLD_KEYS
    unknown = [w for w in requested if w not in formation_keys]
    if unknown:
        raise SystemExit(
            f"--worlds names {unknown} - not a real formation world in the registry "
            f"(records/worlds/<code>.yaml). Formation worlds: {sorted(formation_keys)}"
        )
    if not authorized_by.strip():
        raise SystemExit("--authorized-by is required and cannot be blank - every live-billed run names who authorized it")
    table = price_for_model(voice_model_pattern)
    if table is None:
        raise SystemExit(f"no approved price table for voice model {voice_model_pattern!r} - aborting before any billed call")

    max_tokens = inspect.signature(stream_voice_turn).parameters["max_tokens"].default
    loader = LazyWorldLoader()
    canon_questions = load_fleet_records()
    per_world_estimates = {
        w: estimate_world_cost_usd(w, arm, table, registry=registry, loader=loader, canon_questions=canon_questions,
                                   max_tokens=max_tokens)
        for w in requested
    }
    preflight_total = sum(per_world_estimates.values())
    if preflight_total > max_usd:
        breakdown = ", ".join(f"{w}=${c:.2f}" for w, c in per_world_estimates.items())
        raise SystemExit(
            f"preflight estimate ${preflight_total:.2f} for {requested} ({breakdown}) exceeds "
            f"--max-usd ${max_usd:.2f} - aborting before any billed call is made. Raise --max-usd "
            f"if this spend is actually authorized, or narrow --worlds."
        )
    voice_model_id = resolve_model_id(voice_model_pattern, region)
    if price_for_model(voice_model_id) is not table:
        raise SystemExit(f"resolved voice model {voice_model_id!r} prices differently from pattern {voice_model_pattern!r} - aborting")

    settings = run_settings(
        registry=registry, world_keys=requested, region=region, voice_model_id=voice_model_id, max_usd=max_usd,
        save_transcripts=save_transcripts,
    )
    settings.update({
        "arm": arm,
        "answerer": ARMS[arm].__name__,
        "voice_call": "messages.stream" if arm == "c" else "messages.create (non-streaming, documents with citations enabled)",
        "safety_call": f"not made - {ARMS[arm].__name__} answers each sealed probe with the voice call only",
        "cell_choice": "none - every record attached" if arm == "native-whole" else "match_asks_to_cells, top 2, from the probe text",
        "price_table_source": table.source,
    })
    print(json.dumps({"run_settings": settings, "per_world_estimated_usd": per_world_estimates,
                      "estimated_usd_preflight": preflight_total}, indent=2), file=sys.stderr, flush=True)
    if settings_only:
        return {"run_settings": settings, "per_world_estimated_usd": per_world_estimates,
                "estimated_usd_preflight": preflight_total, "settings_only": True}

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
        world_result = _run_world(world_key, arm=arm, registry=registry, loader=loader, voice_model_id=voice_model_id,
                                  region=region, canon_questions=canon_questions, table=table,
                                  save_transcripts=save_transcripts)
        spent_so_far += world_result["actual_usd"]
        per_world[world_key] = world_result

    return {
        "arm": arm,
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
            f"Real, billed E1 run, arm {arm}: the sealed battery under the {ARMS[arm].__name__} layout, once per "
            f"probe, per world. Token counts are measured from each call's own usage and priced against the "
            f"table price_for_model names for the voice model, an estimate against a published rate card."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--region", required=True)
    parser.add_argument("--arm", required=True, choices=sorted(ARMS))
    parser.add_argument("--worlds", default=",".join(DEFAULT_WORLD_KEYS),
                        help="comma-separated world keys, exactly as authorized for this run")
    parser.add_argument("--max-usd", type=float, default=DEFAULT_MAX_USD,
                        help=f"cost ceiling in USD (default ${DEFAULT_MAX_USD:.2f}) - the run aborts before any billed "
                             f"call if the preflight total exceeds it, and again, running, before each next world")
    parser.add_argument("--authorized-by", required=True,
                        help="who authorized this specific live-billed run - recorded in the report, never blank")
    parser.add_argument("--voice-model", default=DEFAULT_VOICE_MODEL_PATTERN,
                        help="inference-profile pattern for the voice model; must match exactly one profile")
    parser.add_argument("--save-transcripts", action="store_true",
                        help="keep every probe's transcript and manifest in the report; grading is unchanged")
    parser.add_argument("--settings-only", action="store_true",
                        help="print the run settings and preflight estimate, then exit before any billed call")
    parser.add_argument("--out", default=None, help="report path (default engine/m3/reports/e1/e1-report-<arm>.json)")
    args = parser.parse_args()

    world_keys = [k.strip() for k in args.worlds.split(",") if k.strip()]
    report = run(args.region, args.arm, world_keys=world_keys, max_usd=args.max_usd, authorized_by=args.authorized_by,
                 voice_model_pattern=args.voice_model, save_transcripts=args.save_transcripts,
                 settings_only=args.settings_only)
    if report.get("settings_only"):
        return 0
    out_path = Path(args.out) if args.out else REPORTS_DIR / f"e1-report-{args.arm}.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

    summary = {
        "arm": report["arm"],
        "voice_model_id": report["voice_model_id"],
        "overall_pass": report["overall_pass"],
        "max_usd": report["max_usd"],
        "estimated_usd_preflight": report["estimated_usd_preflight"],
        "actual_usd_spent": report["actual_usd_spent"],
        "aborted_reason": report["aborted_reason"],
        "worlds": {
            k: {
                "battery_size": v["battery_size"],
                "pass_count": v["pass_count"],
                "actual_usd": v["actual_usd"],
                "failing_probes": [p["probe_id"] for p in v["per_probe"] if not p["passed"]],
            }
            for k, v in report["worlds"].items()
        },
    }
    print(json.dumps(summary, indent=2))
    return 0 if report["overall_pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
