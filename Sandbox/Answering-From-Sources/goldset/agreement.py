"""Agreement between two labellers on the same pool items, and the queue for
Mark: every disagreement (on the verdict, or on the class of an unsupported
sentence), every item either labeller puts in a key class, and a random
sample of the rest.

The two runs label different streams (different line ids), so items are
joined through each stream's key by pool item id.

  python -m goldset.agreement --key <key A> --labels <labels A> --key <key B> --labels <labels B> \\
      --sample 10 --out <queue.json>
"""
import argparse
import json
import random
from collections import Counter
from pathlib import Path

from goldset.common import read_jsonl
from goldset.labeller import KEY_CLASSES, gold_class


def by_item(key: list[dict], labels: list[dict], kinds: tuple[str, ...] = ("pool",)) -> dict[str, dict]:
    ref = {k["line_id"]: k["ref"] for k in key if k["kind"] in kinds}
    out = {}
    for row in labels:
        if row["line_id"] in ref and row.get("label") is not None:
            out.setdefault(ref[row["line_id"]], row)
    return out


def _binary(label: dict) -> str | None:
    return {"supported": "supported", "unsupported": "unsupported"}.get(label["verdict"])


def kappa(pairs: list[tuple[str, str]]) -> float | None:
    if not pairs:
        return None
    n = len(pairs)
    observed = sum(a == b for a, b in pairs) / n
    cats = {x for p in pairs for x in p}
    left, right = Counter(a for a, _ in pairs), Counter(b for _, b in pairs)
    expected = sum(left[c] * right[c] for c in cats) / (n * n)
    return (observed - expected) / (1 - expected) if expected < 1 else None


def compare(first: dict[str, dict], second: dict[str, dict], sample: int, seed: int = 20261029) -> dict:
    shared = sorted(set(first) & set(second))
    rows, binary_pairs, class_pairs = [], [], []
    for item in shared:
        a, b = first[item]["label"], second[item]["label"]
        ca, cb = gold_class(a), gold_class(b)
        ba, bb = _binary(a), _binary(b)
        if ba and bb:
            binary_pairs.append((ba, bb))
        class_pairs.append((ca, cb))
        key_class = bool({a.get("failure_class"), *a.get("other_classes", []), b.get("failure_class"), *b.get("other_classes", [])} & set(KEY_CLASSES))
        rows.append({"item_id": item, "first": ca, "second": cb, "disagree": ca != cb, "key_class": key_class,
                     "first_model": first[item]["model_id"], "second_model": second[item]["model_id"]})
    must = [r for r in rows if r["disagree"] or r["key_class"]]
    rest = [r for r in rows if not (r["disagree"] or r["key_class"])]
    drawn = random.Random(seed).sample(rest, min(sample, len(rest)))
    return {
        "items_both_labelled": len(shared),
        "verdict_agreement": sum(a == b for a, b in binary_pairs) / len(binary_pairs) if binary_pairs else None,
        "verdict_kappa": kappa(binary_pairs),
        "class_agreement": sum(a == b for a, b in class_pairs) / len(class_pairs) if class_pairs else None,
        "class_kappa": kappa(class_pairs),
        "disagreements": sum(r["disagree"] for r in rows),
        "queue": [{**r, "why": "disagreement" if r["disagree"] else "key class"} for r in must]
        + [{**r, "why": "random sample of agreements"} for r in drawn],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--key", type=Path, action="append", required=True)
    parser.add_argument("--labels", type=Path, action="append", required=True)
    parser.add_argument("--sample", type=int, default=10)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args(argv)
    if len(args.key) != 2 or len(args.labels) != 2:
        parser.error("give exactly two --key and two --labels, first labeller first")
    first = by_item(read_jsonl(args.key[0]), read_jsonl(args.labels[0]))
    second = by_item(read_jsonl(args.key[1]), read_jsonl(args.labels[1]))
    result = compare(first, second, args.sample)
    text = json.dumps(result, indent=2)
    if args.out:
        args.out.write_text(text + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in result.items() if k != "queue"}, indent=2), f"\nqueue: {len(result['queue'])} items")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
