"""The adjudication packet for Mark: the items whose gold label needs a
person. In order: every disagreement between the two labellers, every other
item the specialist put in a key class (whether or not the second labeller
saw it), every item only the second labeller put in one, then the random sample of agreements from the agreement queue.

Each item carries the sentence, its bound records as they stood at the
item's commit (text, use note, and each source with its locus, so the ruling
can be checked against the source span), how the gates treated it, and both
labels with their evidence.

  python -m goldset.packet --pool <pool.jsonl> --key <specialist key> --labels <specialist labels> \\
      --key <second key> --labels <second labels> --queue <agreement-and-queue.json> --out <packet.json>
"""
import argparse
import json
from collections import Counter
from pathlib import Path

from goldset import agreement
from goldset.common import read_jsonl, records_at
from goldset.labeller import KEY_CLASSES, gold_class

TEXT_LIMIT = 1500


def _label(row: dict | None) -> dict | None:
    if not row:
        return None
    label = row["label"]
    return {"model": row["model_id"], "verdict": label["verdict"], "class": gold_class(label), "reason": label["reason"],
            "evidence": label["evidence"], "record_concern": label.get("record_concern")}


def _gate(gate: dict) -> str:
    if gate["verdict"] == "ok":
        return "kept, cited"
    return "removed" if gate.get("removed") else "kept, citation dropped"


def _record(record: dict, record_id: str) -> dict:
    text = " ".join(str(record.get("text") or record.get("modern_rendering") or "").split())
    return {"id": record_id, "means": (record.get("use_note") or {}).get("means"), "text": text[:TEXT_LIMIT],
            "sources": [{"source_id": s.get("source_id"), "locus": " ".join(str(s.get("locus") or "").split())}
                        for s in record.get("sources") or []]}


def order(specialist: dict, queue: list[dict]) -> list[tuple[str, str]]:
    out = [(q["item_id"], "disagreement") for q in queue if q["why"] == "disagreement"]
    taken = {i for i, _ in out}
    for item_id, row in sorted(specialist.items()):
        label = row["label"]
        if item_id not in taken and {label.get("failure_class"), *label.get("other_classes", [])} & set(KEY_CLASSES):
            out.append((item_id, "key class (specialist)"))
            taken.add(item_id)
    for q in queue:
        if q["why"] == "key class" and q["item_id"] not in taken:
            out.append((q["item_id"], "key class (second labeller)"))
            taken.add(q["item_id"])
    out += [(q["item_id"], q["why"]) for q in queue if q["why"] == "random sample of agreements" and q["item_id"] not in taken]
    return out


def build(specialist: dict, second: dict, queue: list[dict], pool: dict) -> list[dict]:
    items = []
    for item_id, why in order(specialist, queue):
        item = pool[item_id]
        records = records_at(item["records_commit"], item["world"])
        items.append({
            "item_id": item_id, "why": why, "world": item["world"], "probe_id": item["probe_id"], "sentence": item["sentence"],
            "records": [_record(records.get(b["id"], {}), b["id"]) for b in item["bindings"]],
            "gate": _gate(item["gate"]), "specialist": _label(specialist.get(item_id)), "second": _label(second.get(item_id)),
        })
    return items


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--pool", type=Path, required=True)
    parser.add_argument("--key", type=Path, action="append", required=True)
    parser.add_argument("--labels", type=Path, action="append", required=True)
    parser.add_argument("--queue", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args(argv)
    if len(args.key) != 2 or len(args.labels) != 2:
        parser.error("give exactly two --key and two --labels, specialist first")
    specialist = agreement.by_item(read_jsonl(args.key[0]), read_jsonl(args.labels[0]))
    second = agreement.by_item(read_jsonl(args.key[1]), read_jsonl(args.labels[1]))
    pool = {i["item_id"]: i for i in read_jsonl(args.pool)}
    items = build(specialist, second, json.loads(args.queue.read_text(encoding="utf-8"))["queue"], pool)
    args.out.write_text(json.dumps(items, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({"items": len(items), "by_reason": Counter(i["why"] for i in items)}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
