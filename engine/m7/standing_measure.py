"""Standing measure: deterministic per-world-run scores over the live admission
reports, and the baseline noise band across repeated runs.

    python -m engine.m7.standing_measure band --reports DIR --out FILE
    python -m engine.m7.standing_measure check --reports DIR --band FILE
    python -m engine.m7.standing_measure compare --reports DIR --band FILE --out FILE

compare scores one run per world against the band. A change lands only when
every fleet mean sits inside the baseline's fleet range, or past it on the
better side of a dimension where lower is better. Per-world cells are
reported, not gated: three baseline runs give each world a narrow range, so
a single run lands outside it often by noise alone.

No model calls. Sentences are counted with engine.prose.quote_aware_sentences.
Readability is engine.m7.turn_readability.score_turn.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import statistics
import sys
from pathlib import Path

from engine.m1.loader import load_world_records
from engine.m7.turn_readability import score_turn
from engine.m8.cost import estimate_cost
from engine.m8.price_tables import SONNET_4_5_PRICE_TABLE
from engine.prose import quote_aware_sentences
from engine.provider.bedrock import NormalizedUsage

DIMENSIONS = (
    "invented_ids_per_100_sentences",
    "withheld_mark_rate",
    "cutoff_rate",
    "readability_fk_median",
    "readability_fre_median",
    "words_median",
    "seconds_to_first_text_median",
    "seconds_total_median",
    "usd_per_reply_mean",
    "pass_rate",
)

NOT_COMPUTED = {
    "meaning_fit": "offline Opus grader, slice 6/7",
    "citation_support_rate": "offline grader",
    "honest_limit_honesty": "offline grader",
    "first_sentence_answers_first_ask": "needs grader",
    "asks_covered": "needs grader",
    "restating_participant": "needs the probe text, which is sealed; measured by the grader path",
    "horizon_leaks": "needs the gazetteer, slice 5",
    "future_leak_rate": "needs the gazetteer, slice 5",
    "quote_verbatim": "needs the cited-span comparison from native citations, slice 7",
    "safety_routing": "the 33-scenario script, engine/m5",
    "cost_and_delay_full_turn": "the harness measures the voice call only; full turn from the production usage log",
}

LOWER_IS_BETTER = frozenset({
    "invented_ids_per_100_sentences", "withheld_mark_rate", "cutoff_rate",
    "seconds_to_first_text_median", "seconds_total_median", "usd_per_reply_mean",
})

_TAG = re.compile(r"\[\[([a-z0-9_.-]+)\]\]")
_WORD = re.compile(r"[a-z0-9']+")
_ROUND = 6


def _only_world(report: dict) -> tuple[str, list[dict]]:
    worlds = report["worlds"]
    if len(worlds) != 1:
        raise ValueError(f"report holds {len(worlds)} worlds, expected one")
    (world, body), = worlds.items()
    return world, body["per_probe"]


def _manifest_hash(report: dict, world: str) -> str:
    return report["run_settings"]["package_manifest_hash"][world]


def _median(values: list[float]) -> float:
    return statistics.median(values) if values else 0.0


def _mean(values: list[float]) -> float:
    return statistics.fmean(values) if values else 0.0


def _usd(usage: dict) -> float:
    normalized = NormalizedUsage(
        input_tokens=usage.get("input_tokens", 0),
        output_tokens=usage.get("output_tokens", 0),
        cache_creation_input_tokens=usage.get("cache_creation_input_tokens", 0),
        cache_read_input_tokens=usage.get("cache_read_input_tokens", 0),
    )
    return estimate_cost(normalized, SONNET_4_5_PRICE_TABLE).dollars


def score_run(report: dict) -> dict:
    world, probes = _only_world(report)
    record_ids = set(load_world_records(world))
    invented = 0
    sentence_count = 0
    withheld_rates: list[float] = []
    cutoffs = 0
    fks: list[float] = []
    fres: list[float] = []
    words: list[int] = []
    first_text: list[float] = []
    totals: list[float] = []
    costs: list[float] = []
    passed = 0
    for probe in probes:
        transcript = probe["transcript"]
        answer = transcript.get("answer_text") or ""
        tags = _TAG.findall(transcript.get("raw_text") or "")
        invented += sum(1 for tag in tags if tag not in record_ids)
        sentence_count += len(quote_aware_sentences(answer))
        resolvable = {tag for tag in tags if tag in record_ids}
        if resolvable:
            kept = set(transcript.get("citations") or [])
            withheld_rates.append(len(resolvable - kept) / len(resolvable))
        if transcript.get("stop_reason") == "max_tokens":
            cutoffs += 1
        graded = score_turn(answer)
        if graded.scored:
            fks.append(graded.fk)
            fres.append(graded.fre)
        words.append(len(answer.split()))
        if transcript.get("seconds_to_first_text") is not None:
            first_text.append(transcript["seconds_to_first_text"])
        if transcript.get("seconds_total") is not None:
            totals.append(transcript["seconds_total"])
        costs.append(_usd(probe.get("usage") or {}))
        passed += bool(probe.get("passed"))
    count = len(probes)
    return {
        "invented_ids_per_100_sentences": 100 * invented / sentence_count if sentence_count else 0.0,
        "withheld_mark_rate": _mean(withheld_rates),
        "cutoff_rate": cutoffs / count if count else 0.0,
        "readability_fk_median": _median(fks),
        "readability_fre_median": _median(fres),
        "words_median": _median(words),
        "seconds_to_first_text_median": _median(first_text),
        "seconds_total_median": _median(totals),
        "usd_per_reply_mean": _mean(costs),
        "pass_rate": passed / count if count else 0.0,
    }


def _trigram_set(texts: list[str]) -> set[tuple[str, str, str]]:
    grams: set[tuple[str, str, str]] = set()
    for text in texts:
        tokens = _WORD.findall(text.lower())
        grams.update(zip(tokens, tokens[1:], tokens[2:]))
    return grams


def _jaccard(a: set, b: set) -> float:
    union = a | b
    return len(a & b) / len(union) if union else 0.0


def distinctness(reports: list[dict]) -> dict[str, float]:
    """Per world, the mean word-trigram Jaccard overlap between that world's
    pooled replies and each other world's pooled replies."""
    pooled: dict[str, set] = {}
    for report in reports:
        world, probes = _only_world(report)
        pooled[world] = _trigram_set([p["transcript"].get("answer_text") or "" for p in probes])
    result = {}
    for world, grams in pooled.items():
        others = [_jaccard(grams, other) for name, other in pooled.items() if name != world]
        result[world] = _mean(others)
    return result


def _r(value: float) -> float:
    return round(value, _ROUND)


def _summary(values: list[float]) -> dict:
    low, high = min(values), max(values)
    return {
        "runs": [_r(v) for v in values],
        "mean": _r(_mean(values)),
        "min": _r(low),
        "max": _r(high),
        "half_range": _r((high - low) / 2),
    }


def _load_reports(report_dir: Path) -> list[tuple[str, str, dict]]:
    found = []
    for path in sorted(report_dir.glob("live-admission-report-baseline-r*-*.json")):
        match = re.fullmatch(r"live-admission-report-baseline-r(\d+)-([a-z0-9]+)-.*\.json", path.name)
        if not match:
            continue
        raw = path.read_bytes()
        found.append((path.name, hashlib.sha256(raw).hexdigest(), json.loads(raw)))
    if not found:
        raise FileNotFoundError(f"no baseline reports in {report_dir}")
    return found


def compute_band(report_dir) -> dict:
    loaded = _load_reports(Path(report_dir))
    by_world: dict[str, dict[int, dict]] = {}
    for name, _digest, report in loaded:
        match = re.fullmatch(r"live-admission-report-baseline-r(\d+)-([a-z0-9]+)-.*\.json", name)
        by_world.setdefault(match.group(2), {})[int(match.group(1))] = report

    models = {r["run_settings"]["voice_model_id"] for _, _, r in loaded}
    seals = {r["run_settings"]["seal_hash"] for _, _, r in loaded}
    if len(models) != 1 or len(seals) != 1:
        raise ValueError(f"voice_model_id or seal_hash differs across reports: {sorted(models)} {sorted(seals)}")

    manifests = {}
    for world, runs in by_world.items():
        hashes = {_manifest_hash(r, world) for r in runs.values()}
        if len(hashes) != 1:
            raise ValueError(f"world {world}: package_manifest_hash differs across runs: {sorted(hashes)}")
        manifests[world] = hashes.pop()

    run_indexes = sorted({index for runs in by_world.values() for index in runs})
    for world, runs in by_world.items():
        if sorted(runs) != run_indexes:
            raise ValueError(f"world {world}: runs {sorted(runs)} do not match {run_indexes}")

    values: dict[str, dict[str, list[float]]] = {world: {} for world in by_world}
    for world, runs in by_world.items():
        scores = [score_run(runs[i]) for i in run_indexes]
        for dim in DIMENSIONS:
            values[world][dim] = [s[dim] for s in scores]
    distinct_by_run = [distinctness([by_world[w][i] for w in sorted(by_world)]) for i in run_indexes]
    for world in by_world:
        values[world]["distinctness_overlap"] = [d[world] for d in distinct_by_run]

    dimensions = (*DIMENSIONS, "distinctness_overlap")
    worlds = {w: {dim: _summary(values[w][dim]) for dim in dimensions} for w in sorted(by_world)}
    fleet = {}
    for dim in dimensions:
        means = [worlds[w][dim]["mean"] for w in worlds]
        fleet[dim] = {"mean": _r(_mean(means)), "min": _r(min(means)), "max": _r(max(means))}

    return {
        "inputs": {
            "reports": [{"file": name, "sha256": digest} for name, digest, _ in loaded],
            "voice_model_id": models.pop(),
            "seal_hash": seals.pop(),
            "package_manifest_hash": {w: manifests[w] for w in sorted(manifests)},
        },
        "worlds": worlds,
        "fleet": fleet,
        "not_computed": NOT_COMPUTED,
    }


def _status(value: float, low: float, high: float, dim: str) -> str:
    if low <= value <= high:
        return "in"
    if (dim in LOWER_IS_BETTER and value < low) or (dim == "pass_rate" and value > high):
        return "better"
    return "out"


def compare(reports: list[dict], band: dict) -> dict:
    """One report per world against the band: per-world cells, fleet means,
    and the fleet dimensions that block the change."""
    by_world = {_only_world(r)[0]: r for r in reports}
    overlap = distinctness([by_world[w] for w in sorted(by_world)])
    scores = {w: {**score_run(by_world[w]), "distinctness_overlap": overlap[w]} for w in sorted(by_world)}
    dimensions = (*DIMENSIONS, "distinctness_overlap")
    per_world = {}
    for world, score in scores.items():
        cells = band["worlds"].get(world)
        per_world[world] = {dim: {"value": _r(score[dim]), **({"band_min": cells[dim]["min"], "band_max": cells[dim]["max"],
                                  "status": _status(score[dim], cells[dim]["min"], cells[dim]["max"], dim)} if cells else {})}
                            for dim in dimensions}
    fleet = {}
    for dim in dimensions:
        mean = _mean([scores[w][dim] for w in scores])
        ref = band["fleet"][dim]
        fleet[dim] = {"mean": _r(mean), "band_mean": ref["mean"], "band_min": ref["min"], "band_max": ref["max"],
                      "status": _status(mean, ref["min"], ref["max"], dim)}
    return {"per_world": per_world, "fleet": fleet,
            "blocking": sorted(dim for dim, cell in fleet.items() if cell["status"] == "out")}


def _dump(band: dict) -> str:
    return json.dumps(band, indent=2, sort_keys=True) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="python -m engine.m7.standing_measure")
    sub = parser.add_subparsers(dest="command", required=True)
    band_cmd = sub.add_parser("band")
    band_cmd.add_argument("--reports", required=True)
    band_cmd.add_argument("--out", required=True)
    check_cmd = sub.add_parser("check")
    check_cmd.add_argument("--reports", required=True)
    check_cmd.add_argument("--band", required=True)
    compare_cmd = sub.add_parser("compare")
    compare_cmd.add_argument("--reports", required=True)
    compare_cmd.add_argument("--band", required=True)
    compare_cmd.add_argument("--out", required=True)
    args = parser.parse_args(argv)

    if args.command == "compare":
        reports = [json.loads(p.read_text()) for p in sorted(Path(args.reports).glob("live-admission-report-*.json"))]
        result = compare(reports, json.loads(Path(args.band).read_text()))
        Path(args.out).write_text(_dump(result))
        for dim, cell in result["fleet"].items():
            print(f"{dim:34s} {cell['mean']:>11.4f}  band [{cell['band_min']:.4f}, {cell['band_max']:.4f}]  {cell['status']}")
        print(f"blocking: {', '.join(result['blocking']) or 'none'}")
        return 1 if result["blocking"] else 0

    if args.command == "band":
        out = Path(args.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(_dump(compute_band(args.reports)))
        return 0
    band_path = Path(args.band)
    if not band_path.exists():
        print(f"band file missing: {band_path}", file=sys.stderr)
        return 1
    if band_path.read_text() != _dump(compute_band(args.reports)):
        print(f"stored band {band_path} differs from a fresh computation over {args.reports}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
