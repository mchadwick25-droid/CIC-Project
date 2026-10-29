"""The gold set: every labelled natural item and every constructed item, each
with its gold label and where that label came from.

  mark          Mark ruled on it (his ruling always wins)
  construction  a constructed item nobody ruled on: unsupported, in the class
                it was written and read to carry
  specialist    a natural item nobody ruled on: the AI specialist's label

Each item keeps its origin (natural or constructed), its bound records with
each source and locus, and the evidence spans the labels quote, so a reader
can always go from the sentence to the source span. No count mixes the two
origins. Seeds and controls are test sets, never gold items.

Rulings are the rows of the rulings page's store ({item_id, verdict, class,
note, at}), saved as JSON lines.

  python -m goldset.build --pool <pool.jsonl> --constructed <constructed.jsonl> \\
      --specialist <key> <labels> [--specialist <key> <labels> ...] \\
      --second <key> <labels> [...] --rulings <rulings.jsonl> --out <gold.jsonl>
"""
import argparse
import json
from collections import Counter
from pathlib import Path

from goldset import agreement
from goldset.common import read_jsonl, records_at, write_jsonl
from goldset.labeller import gold_class

ITEM_FIELDS = ("world", "records_commit", "bindings", "sentence")


def _sources(item: dict) -> list[dict]:
    records = records_at(item["records_commit"], item["world"])
    out = []
    for binding in item["bindings"]:
        record = records.get(binding["id"]) or {}
        for source in record.get("sources") or [{}]:
            out.append({"record_id": binding["id"], "source_id": source.get("source_id"),
                        "locus": " ".join(str(source.get("locus") or "").split()) or None})
    return out


def _label(row: dict | None) -> dict | None:
    if not row:
        return None
    return {**row["label"], "model_id": row["model_id"]}


def ruled_label(ruling: dict, specialist: dict | None) -> dict:
    """Mark's ruling as a label. The specialist's evidence is kept only when
    the ruling has the same verdict and class, since it was quoted for that
    reading."""
    unsupported = ruling["verdict"] == "unsupported"
    label = {"verdict": ruling["verdict"], "failure_class": ruling["class"] if unsupported else None,
             "other_classes": [], "reason": ruling.get("note") or "", "evidence": []}
    if specialist and gold_class(specialist) == gold_class(label):
        label["evidence"] = specialist.get("evidence", [])
        label["other_classes"] = specialist.get("other_classes", [])
    return label


def build(pool: dict, constructed: dict, specialist: dict, second: dict, rulings: dict) -> list[dict]:
    items = []
    for item_id in sorted(specialist.keys() | constructed.keys()):
        made = constructed.get(item_id)
        base = made or pool[item_id]
        spec, sec, ruling = _label(specialist.get(item_id)), _label(second.get(item_id)), rulings.get(item_id)
        if ruling:
            label, source = ruled_label(ruling, spec), "mark"
        elif made:
            label = {"verdict": "unsupported", "failure_class": made["expected_class"], "other_classes": [],
                     "reason": made["construction"], "evidence": [{"block": "R1", "words": made["record_words"]}]}
            source = "construction"
        else:
            label, source = {k: v for k, v in spec.items() if k != "model_id"}, "specialist"
        row = {"item_id": item_id, "origin": "constructed" if made else "natural", **{k: base[k] for k in ITEM_FIELDS},
               "label": label, "label_source": source, "sources": _sources(base),
               "specialist": spec, "second": sec, "ruling": ruling}
        if made:
            row["construction"] = {"class": made["expected_class"], "note": made["construction"], "record_words": made["record_words"]}
        else:
            row.update(probe_id=base["probe_id"], gate=base["gate"])
        items.append(row)
    return items


def counts(items: list[dict]) -> dict:
    return {origin: {"items": sum(i["origin"] == origin for i in items),
                     "by_class": dict(Counter(gold_class(i["label"]) for i in items if i["origin"] == origin)),
                     "by_label_source": dict(Counter(i["label_source"] for i in items if i["origin"] == origin))}
            for origin in ("natural", "constructed")}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--pool", type=Path, required=True)
    parser.add_argument("--constructed", type=Path, required=True)
    parser.add_argument("--specialist", nargs=2, type=Path, action="append", required=True, metavar=("KEY", "LABELS"))
    parser.add_argument("--second", nargs=2, type=Path, action="append", default=[], metavar=("KEY", "LABELS"))
    parser.add_argument("--rulings", type=Path)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args(argv)
    kinds = ("pool", "constructed")
    specialist, second = {}, {}
    for key, labels in args.specialist:
        for item_id, row in agreement.by_item(read_jsonl(key), read_jsonl(labels), kinds).items():
            if item_id in specialist:
                raise SystemExit(f"{item_id} has a specialist label in two runs")
            specialist[item_id] = row
    for key, labels in args.second:
        second.update(agreement.by_item(read_jsonl(key), read_jsonl(labels), kinds))
    constructed = {c["construct_id"]: c for c in read_jsonl(args.constructed)}
    missing = sorted(set(constructed) - set(specialist))
    if missing:
        raise SystemExit(f"constructed items without a blind label: {', '.join(missing)}")
    rulings = {r["item_id"]: r for r in read_jsonl(args.rulings)} if args.rulings and args.rulings.exists() else {}
    pool = {i["item_id"]: i for i in read_jsonl(args.pool)}
    unknown = sorted(set(rulings) - set(specialist))
    if unknown:
        raise SystemExit(f"rulings for items with no label: {', '.join(unknown)}")
    items = build(pool, constructed, specialist, second, rulings)
    write_jsonl(args.out, items)
    print(json.dumps(counts(items), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
