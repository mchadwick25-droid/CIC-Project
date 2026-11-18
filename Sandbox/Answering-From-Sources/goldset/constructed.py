"""Constructed gold-set items, for the failure classes the natural sentences
leave short of the per-class minimum. Each is written by hand to carry one
known defect, bound to the record whose own words make the defect certain,
read before use, and then labelled blind among other lines like any item.

They are counted apart from natural items in every figure: the item's kind is
"constructed" in the stream key and in the gold set, and no count mixes the
two.

The readings file lists the candidate files and, for each candidate id, the
reading: accepted (optionally with a repair to grammar or capitals only) or
rejected with a reason. A candidate not read does not enter.

  python -m goldset.constructed --readings <Constructed_Readings.yaml> --out <constructed.jsonl>
"""
import argparse
import json
from collections import Counter
from pathlib import Path

from goldset.common import git_show, records_at, stable_id, write_jsonl, yaml
from goldset.labeller import _fold
from goldset.seeds import EXPECTED_CLASS


def construct_id(candidate: dict) -> str:
    return stable_id("cx", candidate["seed_type"], candidate["world"], candidate["sentence"])


def problems(candidate: dict) -> list[str]:
    """Why a candidate cannot enter, from its bound records at its commit."""
    found = []
    if candidate["seed_type"] not in EXPECTED_CLASS or candidate["seed_type"] == "control":
        found.append(f"unknown defect type {candidate['seed_type']!r}")
    records = records_at(candidate["records_commit"], candidate["world"])
    texts = []
    for binding in candidate["bindings"]:
        record = records.get(binding["id"])
        if record is None:
            found.append(f"{binding['id']} is not a record of {candidate['world']} at {candidate['records_commit'][:8]}")
        else:
            if record.get("status") != "ready":
                found.append(f"{binding['id']} has status {record.get('status')!r}, not ready")
            texts.append(_fold(git_show(candidate["records_commit"], record["_path"]) or ""))
    if texts and not any(_fold(candidate["record_words"]) in t for t in texts):
        found.append("record_words are not in any bound record")
    return found


def build(readings: dict, root: Path) -> tuple[list[dict], dict]:
    candidates = {}
    for name in readings["candidates"]:
        for candidate in yaml.safe_load((root / name).read_text(encoding="utf-8")) or []:
            candidates[construct_id(candidate)] = candidate
    read = readings.get("readings") or {}
    out, tally = [], Counter()
    for cid, candidate in sorted(candidates.items()):
        reading = read.get(cid)
        if not reading:
            tally["not read"] += 1
            continue
        if reading.get("verdict") != "accepted":
            tally[f"rejected {candidate['seed_type']}"] += 1
            continue
        wrong = problems(candidate)
        if wrong:
            raise ValueError(f"{cid} accepted but {'; '.join(wrong)}")
        row = {
            "construct_id": cid, "kind": "constructed", "seed_type": candidate["seed_type"],
            "expected_class": EXPECTED_CLASS[candidate["seed_type"]], "world": candidate["world"],
            "records_commit": candidate["records_commit"], "bindings": candidate["bindings"],
            "sentence": reading.get("repair") or candidate["sentence"], "record_words": candidate["record_words"],
            "construction": candidate["construction"],
        }
        if reading.get("repair"):
            row["repaired_from"] = candidate["sentence"]
        out.append(row)
        tally[f"accepted {candidate['seed_type']}"] += 1
    return out, dict(tally)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--readings", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--list", action="store_true", help="print every candidate with its id and checks, for the reading")
    args = parser.parse_args(argv)
    readings = yaml.safe_load(args.readings.read_text(encoding="utf-8"))
    root = args.readings.parent
    if args.list:
        for name in readings["candidates"]:
            for c in yaml.safe_load((root / name).read_text(encoding="utf-8")) or []:
                print(json.dumps({"id": construct_id(c), "type": c["seed_type"], "world": c["world"], "bindings": [b["id"] for b in c["bindings"]],
                                  "sentence": c["sentence"], "record_words": c["record_words"], "construction": c["construction"],
                                  "problems": problems(c)}, ensure_ascii=False))
        return 0
    rows, tally = build(readings, root)
    write_jsonl(args.out, rows)
    print(json.dumps(tally, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
