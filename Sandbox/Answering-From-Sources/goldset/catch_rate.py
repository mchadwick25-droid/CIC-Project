"""The seeded-defect catch rate of one labeller run, with the false-alarm rate
on the known-supported controls beside it.

A seed is caught when the labeller's verdict on it is "unsupported"; the
report also says how many were caught under the expected class. A seed left
unlabelled (both replies rejected) counts as missed. A control is a false
alarm when its verdict is "unsupported". The pass rule is Mark's: at least
the threshold of seeds caught (default 19 of 20). No rule is set on false
alarms; the count is published beside the catch rate so a labeller that
flags everything is seen to.

  python -m goldset.catch_rate --key <key.jsonl> --labels <labels.jsonl> --test-set qualify
"""
import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path

from goldset.common import read_jsonl
from goldset.labeller import gold_class

DEFAULT_THRESHOLD = (19, 20)


def report(key: list[dict], labels: list[dict], test_set: str, threshold: tuple[int, int] = DEFAULT_THRESHOLD) -> dict:
    by_line = {r["line_id"]: r for r in labels}
    seeds = [k for k in key if k["kind"] == "seed" and k["test_set"] == test_set]
    controls = [k for k in key if k["kind"] == "control" and k["test_set"] == test_set]
    per_type: dict[str, Counter] = defaultdict(Counter)
    missed = []
    for k in seeds:
        label = (by_line.get(k["line_id"]) or {}).get("label")
        counts = per_type[k["seed_type"]]
        counts["planted"] += 1
        if label is None:
            counts["unlabelled"] += 1
            missed.append({"line_id": k["line_id"], "ref": k["ref"], "seed_type": k["seed_type"], "verdict": None})
        elif label["verdict"] == "unsupported":
            counts["caught"] += 1
            if gold_class(label) == k["expected_class"] or k["expected_class"] in label["other_classes"]:
                counts["caught_as_expected_class"] += 1
        else:
            missed.append({"line_id": k["line_id"], "ref": k["ref"], "seed_type": k["seed_type"], "verdict": label["verdict"], "reason": label["reason"]})
    false_alarms = []
    unlabelled_controls = 0
    for k in controls:
        label = (by_line.get(k["line_id"]) or {}).get("label")
        if label is None:
            unlabelled_controls += 1
        elif label["verdict"] == "unsupported":
            false_alarms.append({"line_id": k["line_id"], "ref": k["ref"], "class": gold_class(label), "reason": label["reason"]})
    caught = sum(c["caught"] for c in per_type.values())
    need, out_of = threshold
    scaled_need = -(-need * len(seeds) // out_of) if seeds else need
    models = sorted({r["model_id"] for r in labels if r["line_id"] in {k["line_id"] for k in seeds + controls}})
    return {
        "test_set": test_set, "model_ids": models,
        "seeds_planted": len(seeds), "seeds_caught": caught,
        "seeds_caught_as_expected_class": sum(c["caught_as_expected_class"] for c in per_type.values()),
        "threshold": f"{need} of {out_of}", "needed_for_this_set": scaled_need,
        "passes_catch_threshold": len(seeds) > 0 and caught >= scaled_need,
        "per_type": {t: dict(c) for t, c in sorted(per_type.items())},
        "controls": len(controls), "false_alarms": len(false_alarms), "unlabelled_controls": unlabelled_controls,
        "missed": missed, "false_alarm_detail": false_alarms,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--key", type=Path, required=True)
    parser.add_argument("--labels", type=Path, required=True)
    parser.add_argument("--test-set", required=True)
    parser.add_argument("--need", type=int, default=DEFAULT_THRESHOLD[0])
    parser.add_argument("--out-of", type=int, default=DEFAULT_THRESHOLD[1])
    parser.add_argument("--out", type=Path)
    args = parser.parse_args(argv)
    result = report(read_jsonl(args.key), read_jsonl(args.labels), args.test_set, (args.need, args.out_of))
    text = json.dumps(result, indent=2, ensure_ascii=False)
    if args.out:
        args.out.write_text(text + "\n", encoding="utf-8")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
