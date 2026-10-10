"""Offline-selected, model-graded sample of out-of-dossier citations.

A per-cell dossier holds only the records whose `canon_cells` include the
probe's cell. This script takes the citations in the saved run-1 baseline
replies that such a dossier would not hold, draws a stratified sample, and
asks a grader model (one billed Bedrock call per item) whether each cited
record is load-bearing, supporting or incidental in the sentence that
carries it.

Item selection reads only saved reports and the world records. The sealed
probe text is read (engine.m3.sealed_probes.read_probe) solely to build the
grader prompt; it is never written to the report or to stdout - probes are
referenced by probe_id only.

Every setting is passed on the command line and printed to stderr before the
first billed call; --settings-only stops there. --max-usd is checked against
a preflight estimate and again, running, before each call.
"""
import argparse
import json
import random
import re
import sys
from collections import Counter
from pathlib import Path

from engine.m1.loader import load_world_records
from engine.m3.sealed_probes import read_probe
from engine.m8 import price_tables
from engine.m8.cost import PriceTable, estimate_cost
from engine.provider.bedrock import make_client, normalize_usage, resolve_model_id

REPORTS_DIR = Path(__file__).resolve().parent / "reports"
REPORT_GLOB = "baseline-*/live-admission-report-baseline-r1-*.json"
DEFAULT_REPORT_PATH = Path(__file__).resolve().parent / "reports" / "dossier-citation-grade.json"

MAX_TOKENS = 2000
ESTIMATED_OUTPUT_TOKENS = 400
RECORD_TEXT_LIMIT = 1500
ROLES = ("load_bearing", "supporting", "incidental")

LABEL_FIELDS = ("title", "name", "world_word", "claim", "statement", "work", "query")
VOICED_FIELDS = (
    "text", "modern_rendering", "plain_meaning", "quick_meaning", "summary", "description", "claim",
    "statement", "held_against", "concedes", "positions", "tensions", "narratable", "bridge_line",
    "exchange", "result", "note", "why_sources_cannot_answer",
)

SYSTEM_PROMPT = (
    "You are a scholar of the tradition reviewing one citation in an answer that a historical "
    "Representative of that tradition gave to a participant. You are shown the participant's "
    "question, the sentence or sentences of the answer that carry the citation, and the cited "
    "record (its type, its label and its voiced text).\n\n"
    "Classify the record's role in that sentence:\n"
    '- "load_bearing": the sentence makes a specific claim that rests on this record, and an '
    "answer to this question would be weaker or wrong without it.\n"
    '- "supporting": it adds colour or a secondary point; the answer stands without it.\n'
    '- "incidental": it could be dropped with no loss.\n\n'
    "Reply with a single line of JSON and nothing else, in this form: "
    '{"role": "load_bearing" | "supporting" | "incidental", "reason": "<one sentence>"}'
)


def _cells(record: dict) -> list[str]:
    cells = record.get("canon_cells")
    if not cells:
        return []
    if isinstance(cells, str):
        return [cells]
    return [str(c) for c in cells]


def load_population(reports_dir: Path | None = None) -> tuple[dict[str, list[dict]], dict[str, int]]:
    """Every (probe, record) pair cited in a run-1 reply whose record does
    not list the probe's cell, per world, plus a per-world count of pairs
    dropped because no reply sentence carries the record."""
    population: dict[str, list[dict]] = {}
    no_sentence: dict[str, int] = {}
    for path in sorted((reports_dir or REPORTS_DIR).glob(REPORT_GLOB)):
        report = json.loads(path.read_text(encoding="utf-8"))
        for world, info in sorted(report["worlds"].items()):
            records = load_world_records(world)
            items = population.setdefault(world, [])
            no_sentence.setdefault(world, 0)
            for probe in info["per_probe"]:
                transcript = probe.get("transcript")
                if not transcript:
                    continue
                entries = transcript.get("citation_entries") or []
                for record_id in transcript.get("citations") or []:
                    record = records.get(record_id)
                    if record is None:
                        continue
                    cells = _cells(record)
                    if probe["cell"] in cells:
                        continue
                    sentences = [e["sentence"] for e in entries if record_id in e.get("record_ids", [])]
                    if not sentences:
                        no_sentence[world] += 1
                        continue
                    items.append({
                        "world": world,
                        "probe_id": probe["probe_id"],
                        "cell": probe["cell"],
                        "record_id": record_id,
                        "record_type": record.get("record_type"),
                        "record_cells": cells,
                        "sentences": sentences,
                    })
    for items in population.values():
        items.sort(key=lambda i: (i["probe_id"], i["record_id"]))
    return population, no_sentence


def draw_sample(population: dict[str, list[dict]], per_world: int, seed: int) -> list[dict]:
    rng = random.Random(seed)
    sample: list[dict] = []
    for world in sorted(population):
        items = population[world]
        sample.extend(rng.sample(items, min(per_world, len(items))))
    return sample


def _as_text(value) -> str:
    return value if isinstance(value, str) else json.dumps(value, ensure_ascii=False, default=str)


def record_excerpt(record: dict, limit: int = RECORD_TEXT_LIMIT) -> str:
    label = next((_as_text(record[f]) for f in LABEL_FIELDS if record.get(f)), record.get("id", ""))
    parts = [f"{f}: {_as_text(record[f])}" for f in VOICED_FIELDS if record.get(f)]
    body = "\n".join(parts)
    if len(body) > limit:
        body = body[:limit]
    return f"record_type: {record.get('record_type')}\nlabel: {label}\n{body}"


def build_user_prompt(question: str, sentences: list[str], record: dict) -> str:
    quoted = "\n".join(f"- {s}" for s in sentences)
    return (
        f"Participant's question:\n{question}\n\n"
        f"Answer sentence(s) carrying the citation:\n{quoted}\n\n"
        f"Cited record:\n{record_excerpt(record)}"
    )


def parse_grade(text: str) -> dict:
    """{"role", "reason"} from the reply, or {"role": "unparsed", "raw_text"}.
    A reply that does not carry a valid role is never guessed at."""
    candidates = [text.strip()]
    candidates.extend(re.findall(r"\{.*?\}", text, re.DOTALL))
    for candidate in candidates:
        try:
            data = json.loads(candidate)
        except (json.JSONDecodeError, TypeError):
            continue
        if isinstance(data, dict) and data.get("role") in ROLES:
            return {"role": data["role"], "reason": str(data.get("reason", ""))}
    return {"role": "unparsed", "raw_text": text}


def resolve_price(model_id: str, override: tuple[float | None, float | None, float | None]) -> tuple[PriceTable, str]:
    if any(p is not None for p in override):
        if any(p is None for p in override):
            raise SystemExit("--price-input, --price-output and --price-cache-read must be given together")
        inp, out, cache = override
        table = PriceTable(
            input_per_token=inp / 1e6, output_per_token=out / 1e6,
            cache_write_per_token=inp / 1e6, cache_read_per_token=cache / 1e6,
            source="explicit command-line override (USD per million tokens)",
        )
        return table, "override"
    lookup = getattr(price_tables, "price_for_model", None)
    table = lookup(model_id) if lookup else None
    if table is None:
        raise SystemExit(
            f"no price for {model_id} in engine.m8.price_tables - refusing to call an unpriced model; "
            "pass --price-input/--price-output/--price-cache-read (USD per million tokens)"
        )
    return table, "price_tables.price_for_model"


def _estimate_item_usd(prompt_chars: int, table: PriceTable) -> float:
    return (prompt_chars / 4) * table.input_per_token + ESTIMATED_OUTPUT_TOKENS * table.output_per_token


def _summarise(items: list[dict]) -> dict:
    def block(group: list[dict]) -> dict:
        counts = Counter(i["role"] for i in group)
        parsed = sum(counts[r] for r in ROLES)
        return {
            "n": len(group),
            "roles": dict(counts),
            "load_bearing_share": (counts["load_bearing"] / parsed) if parsed else None,
        }

    def by(key: str) -> dict:
        keys = sorted({str(i[key]) for i in items})
        return {k: block([i for i in items if str(i[key]) == k]) for k in keys}

    return {"overall": block(items), "by_world": by("world"), "by_record_type": by("record_type")}


def run(*, region: str, grader_model: str, per_world: int, seed: int, max_usd: float, authorized_by: str,
        price_override: tuple[float | None, float | None, float | None] = (None, None, None),
        settings_only: bool = False, reports_dir: Path | None = None) -> dict:
    if not authorized_by.strip():
        raise SystemExit("--authorized-by is required and cannot be blank")
    population, no_sentence = load_population(reports_dir)
    sample = draw_sample(population, per_world, seed)
    model_id = resolve_model_id(grader_model, region)
    table, price_source = resolve_price(model_id, price_override)

    prompts = []
    for item in sample:
        record = load_world_records(item["world"])[item["record_id"]]
        question = read_probe(item["probe_id"])["text"]
        prompts.append(build_user_prompt(question, item["sentences"], record))
    estimates = [_estimate_item_usd(len(SYSTEM_PROMPT) + len(p), table) for p in prompts]
    preflight = sum(estimates)

    settings = {
        "grader_model_id": model_id,
        "max_tokens": MAX_TOKENS,
        "temperature": "not set",
        "thinking": "not sent",
        "region": region,
        "seed": seed,
        "per_world": per_world,
        "population_per_world": {w: len(i) for w, i in population.items()},
        "dropped_no_carrying_sentence_per_world": no_sentence,
        "sample_size": len(sample),
        "price_source": price_source,
        "price_per_million": {
            "input": table.input_per_token * 1e6, "output": table.output_per_token * 1e6,
            "cache_read": table.cache_read_per_token * 1e6,
        },
        "max_usd": max_usd,
        "estimated_usd_preflight": preflight,
        "authorized_by": authorized_by,
        "settings_only": settings_only,
    }
    print(json.dumps({"run_settings": settings}, indent=2), file=sys.stderr, flush=True)
    if preflight > max_usd:
        raise SystemExit(
            f"preflight estimate ${preflight:.4f} exceeds --max-usd ${max_usd:.2f} - aborting before any billed call"
        )
    if settings_only:
        return {"run_settings": settings, "settings_only": True}

    client = make_client(region)
    graded: list[dict] = []
    spent = 0.0
    aborted_reason = None
    for item, prompt, estimate in zip(sample, prompts, estimates):
        if spent + estimate > max_usd:
            aborted_reason = (
                f"${spent:.4f} spent plus the next item's estimate ${estimate:.4f} would exceed "
                f"--max-usd ${max_usd:.2f}; {len(graded)} of {len(sample)} items graded"
            )
            break
        response = client.messages.create(
            model=model_id, max_tokens=MAX_TOKENS, system=SYSTEM_PROMPT,
            messages=[{"role": "user", "content": prompt}],
        )
        usage = normalize_usage(response.usage)
        spent += estimate_cost(usage, table).dollars
        text = "".join(b.text for b in response.content if getattr(b, "type", None) == "text")
        graded.append({
            "world": item["world"], "probe_id": item["probe_id"], "cell": item["cell"],
            "record_id": item["record_id"], "record_type": item["record_type"],
            "record_cells": item["record_cells"], **parse_grade(text),
            "usage": {
                "input_tokens": usage.input_tokens, "output_tokens": usage.output_tokens,
                "cache_creation_input_tokens": usage.cache_creation_input_tokens,
                "cache_read_input_tokens": usage.cache_read_input_tokens,
            },
        })
    return {
        "run_settings": settings,
        "items": graded,
        "summary": _summarise(graded),
        "actual_usd_spent": spent,
        "aborted_reason": aborted_reason,
    }


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--region", required=True)
    p.add_argument("--grader-model", required=True, help="inference-profile pattern; must match exactly one profile")
    p.add_argument("--per-world", type=int, required=True)
    p.add_argument("--seed", type=int, required=True)
    p.add_argument("--max-usd", type=float, required=True)
    p.add_argument("--authorized-by", required=True)
    p.add_argument("--price-input", type=float, help="USD per million input tokens")
    p.add_argument("--price-output", type=float, help="USD per million output tokens")
    p.add_argument("--price-cache-read", type=float, help="USD per million cache-read tokens")
    p.add_argument("--settings-only", action="store_true",
                   help="print settings, population and preflight estimate, then exit before any billed call")
    p.add_argument("--out", default=str(DEFAULT_REPORT_PATH))
    args = p.parse_args(argv)

    report = run(
        region=args.region, grader_model=args.grader_model, per_world=args.per_world, seed=args.seed,
        max_usd=args.max_usd, authorized_by=args.authorized_by,
        price_override=(args.price_input, args.price_output, args.price_cache_read),
        settings_only=args.settings_only,
    )
    if report.get("settings_only"):
        return 0
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"summary": report["summary"]["overall"], "actual_usd_spent": report["actual_usd_spent"],
                      "aborted_reason": report["aborted_reason"], "report": str(out)}, indent=2))
    return 1 if report["aborted_reason"] else 0


if __name__ == "__main__":
    sys.exit(main())
