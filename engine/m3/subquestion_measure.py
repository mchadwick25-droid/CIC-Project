"""Measures what routing by sub-question does to the offer, with no model call.

For each wording whose sub-question has records in the world's sidecar, it asks
whether the offer holds a record the sidecar lists for that sub-question. Three
arms: the offer as it is, the offer when the right sub-question is named (the
most routing can reach), and the offer when a reader's named sub-question is
used. A reader's picks come from a JSON file of wording id to sub-question id.

  python -m engine.m3.subquestion_measure --world lpc --truth <truth.json> \
      --text <text.json> [--named <reader picks.json>]
"""
import argparse
import json
from pathlib import Path

from engine.m1.loader import load_fleet_records
from engine.m4 import evidence, subquestion_routing
from engine.m4.world_loader import LazyWorldLoader

REPO_ROOT = Path(__file__).resolve().parents[2]
TOP = 5


def offer(*, message: str, coverage: dict, repository_records: dict, canon_questions: dict, sub_question: str | None) -> list[str]:
    result = evidence.assemble_evidence(
        message=message, asks=None, canon_questions=canon_questions, coverage=coverage,
        repository_records=repository_records, sub_question=sub_question,
    )
    return [c["id"] for c in result["candidates"]]


def hit(offered: list[str], listed: set[str], top: int | None = None) -> bool:
    return bool(set(offered[:top] if top else offered) & listed)


def measure(*, world_key: str, truth: dict[str, str], text: dict[str, str], named: dict[str, str] | None) -> dict:
    from engine.m1.registry import load_registry
    registry = load_registry()[world_key]
    loaded, _ = LazyWorldLoader().load(
        world_key, package_dir=REPO_ROOT / registry["package"]["location"], expected_manifest_hash=registry["package"]["manifest_hash"],
    )
    records = evidence.repository_records_by_id(loaded.repository)
    sidecar = subquestion_routing.load_sidecar(REPO_ROOT / "Build" / "worlds" / world_key / "build" / f"{world_key}_Answers_Sidecar.yaml")
    coverage = {**loaded.coverage, **subquestion_routing.coverage_entries(sidecar, records)}
    canon = load_fleet_records()
    arms = {"offer_today": lambda i: None, "right_sub_question": lambda i: truth[i]}
    if named is not None:
        arms["reader_named"] = lambda i: subquestion_routing.parse_sub_question({"sub_question": named.get(i)}, sidecar)
    out = {name: {"hit_offer": 0, "hit_top5": 0, "offered_records": 0} for name in arms}
    for wording_id, sub_question in truth.items():
        listed = {r for r in sidecar["subquestions"][sub_question]["records"] if r in records}
        for name, pick in arms.items():
            ids = offer(message=text[wording_id], coverage=coverage, repository_records=records, canon_questions=canon, sub_question=pick(wording_id))
            out[name]["hit_offer"] += hit(ids, listed)
            out[name]["hit_top5"] += hit(ids, listed, TOP)
            out[name]["offered_records"] += len(ids)
    n = len(truth)
    result = {"wordings": n}
    for name, counts in out.items():
        result[name] = {"hit_offer": counts["hit_offer"], "hit_top5": counts["hit_top5"], "mean_offered": round(counts["offered_records"] / n, 1)}
    if named is not None:
        result["reader_named_right"] = sum(1 for i in truth if named.get(i) == truth[i])
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--world", required=True)
    parser.add_argument("--truth", type=Path, required=True)
    parser.add_argument("--text", type=Path, required=True)
    parser.add_argument("--named", type=Path)
    args = parser.parse_args(argv)
    named = json.loads(args.named.read_text(encoding="utf-8")) if args.named else None
    print(json.dumps(measure(world_key=args.world, truth=json.loads(args.truth.read_text()), text=json.loads(args.text.read_text()), named=named), indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
