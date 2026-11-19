"""A labelling stream: natural pool items with a seed test set and any
constructed items planted among them, in a fixed shuffled order, each under a
blind line id.

Two files are written. The stream holds what a labeller run needs to build a
prompt (sentence, bindings, world, commit) under the line id. The key holds
what each line really is (pool item, seeded defect, control or constructed
item; its type and
expected class), and is read only by the scoring.

  python -m goldset.stream --pool <pool.jsonl> --world lpc --seed-tests <seed-tests.jsonl> \\
      --test-set qualify --out <stream.jsonl> --key <key.jsonl> [--limit N]
"""
import argparse
import json
from pathlib import Path

from goldset.common import read_jsonl, stable_id, write_jsonl

PROMPT_FIELDS = ("world", "records_commit", "bindings", "sentence")


def build_stream(pool_items: list[dict], seeds: list[dict], salt: str, drawn_by: dict[str, str] | None = None,
                 constructed: list[dict] | None = None) -> tuple[list[dict], list[dict]]:
    drawn_by = drawn_by or {}
    entries = [("pool", i["item_id"], i, None) for i in pool_items]
    entries += [("control" if s["seed_type"] == "control" else "seed", s["seed_id"], s, s) for s in seeds]
    entries += [("constructed", c["construct_id"], c, c) for c in constructed or []]
    lines, key = [], []
    for kind, ref, source, seed in entries:
        line_id = stable_id("ln", salt, ref)
        lines.append({"line_id": line_id, "item_id": ref, **{k: source[k] for k in PROMPT_FIELDS}})
        key.append({
            "line_id": line_id, "kind": kind, "ref": ref,
            "seed_type": seed["seed_type"] if seed else None,
            "expected_class": seed["expected_class"] if seed else None,
            "test_set": seed.get("test_set") if seed else None,
            "drawn_by": None if seed else drawn_by.get(ref, "world"),
        })
    order = {line["line_id"]: stable_id("o", salt, line["line_id"], length=16) for line in lines}
    lines.sort(key=lambda line: order[line["line_id"]])
    key.sort(key=lambda row: order[row["line_id"]])
    return lines, key


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--pool", type=Path, required=True)
    parser.add_argument("--world", action="append", default=[], help="pool items of these worlds (repeatable); none takes no pool items")
    parser.add_argument("--exclude-labelled", type=Path, action="append", default=[], help="a key whose pool items are already in another stream")
    parser.add_argument("--limit", type=int, default=None, help="at most N pool items, in pool order")
    parser.add_argument("--one-in", type=int, default=None, help="keep at least one in N of the pool items, the lowest by hash under --salt (a second labeller's fifth: 5)")
    parser.add_argument("--items", type=Path, help="a draw (goldset.cues --select): keep only these pool items, any world")
    parser.add_argument("--constructed", type=Path, help="constructed items (goldset.constructed) to label among the rest")
    parser.add_argument("--seed-tests", type=Path)
    parser.add_argument("--test-set", help="which seed test set to plant")
    parser.add_argument("--salt", required=True, help="names the stream; the same salt gives the same ids and order")
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--key", type=Path, required=True)
    args = parser.parse_args(argv)
    taken = {row["ref"] for path in args.exclude_labelled for row in read_jsonl(path) if row["kind"] == "pool"}
    drawn_by = {d["item_id"]: d["drawn_by"] for d in read_jsonl(args.items)} if args.items else {}
    items = [i for i in read_jsonl(args.pool)
             if (i["item_id"] in drawn_by if args.items else i["world"] in args.world)
             and i["item_id"] not in taken and i["gate"]["verdict"] != "unmatched"]
    if args.one_in:
        keep = -(-len(items) // args.one_in)
        items = sorted(items, key=lambda i: stable_id("f", args.salt, i["item_id"], length=16))[:keep]
    items = items[: args.limit]
    seeds = [s for s in read_jsonl(args.seed_tests) if s["test_set"] == args.test_set] if args.seed_tests else []
    constructed = read_jsonl(args.constructed) if args.constructed else []
    lines, key = build_stream(items, seeds, args.salt, drawn_by, constructed)
    write_jsonl(args.out, lines)
    write_jsonl(args.key, key)
    print(json.dumps({"lines": len(lines), "pool": len(items), "seeds": sum(r["kind"] == "seed" for r in key), "controls": sum(r["kind"] == "control" for r in key), "constructed": len(constructed)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
