"""The calibration and held-out halves of the gold set, and the seal on the
held-out half.

An item's half is fixed by a hash of its id alone, before any judge has seen
it, and never by its label, so a corrected label never moves an item. The
seal records, for every held-out item, the sha256 of its content and label at
the time it was sealed. A later change to a sealed item, or a sealed item
that disappears, stops the next write unless it is named with its reason.
An item id is a hash of its sentence, so an edited sentence is a new item and
its old seal shows as gone. Tuning reads the calibration half only; the held-out file is read
by the trial's final scoring alone (tests/test_isolation.py enforces this).

  python -m goldset.split --gold <labelled items.jsonl> --out-dir canon/gold_set
"""
import argparse
import hashlib
import json
from collections import Counter
from datetime import date
from pathlib import Path

from goldset.common import GOLD_DIR, read_jsonl, sha256_text, write_jsonl, yaml
from goldset.labeller import gold_class

SPLIT_SALT = "gold-split-2026-10-29"
CALIBRATION, HELDOUT = "calibration", "heldout"
SEALED_FIELDS = ("item_id", "world", "records_commit", "bindings", "sentence", "label")


def half(item_id: str) -> str:
    digest = hashlib.sha256(f"{SPLIT_SALT}:{item_id}".encode("utf-8")).hexdigest()
    return HELDOUT if int(digest[0], 16) < 8 else CALIBRATION


def sealed_content(item: dict) -> str:
    return json.dumps({k: item.get(k) for k in SEALED_FIELDS}, ensure_ascii=False, sort_keys=True)


def seal_problems(heldout: list[dict], seals: dict) -> dict:
    """What no longer matches the seal: held-out items whose content or label
    changed, sealed items that are gone, and a salt that is not this one."""
    want = {s["item_id"]: s["sha256"] for s in seals.get("seals") or [] if not s.get("withdrawn")}
    have = {i["item_id"]: sha256_text(sealed_content(i)) for i in heldout}
    return {
        "salt": None if seals.get("salt") in (None, SPLIT_SALT) else seals["salt"],
        "changed": sorted(i for i, h in have.items() if i in want and want[i] != h),
        "gone": sorted(i for i in want if i not in have),
    }


def write_halves(gold: list[dict], out_dir: Path, sealed_at: str, reseal: dict[str, str] | None = None) -> dict:
    """Writes both halves and seals the held-out items not yet sealed. A
    sealed item whose content or label changed, or that is gone, stops the
    write, unless it is named in `reseal` with the reason (an adjudicated
    label, for example); the reason is kept in the seal's history."""
    reseal = reseal or {}
    halves = {CALIBRATION: [], HELDOUT: []}
    for item in gold:
        halves[half(item["item_id"])].append(item)
    out_dir.mkdir(parents=True, exist_ok=True)
    seals_path = out_dir / "seals.yaml"
    existing = yaml.safe_load(seals_path.read_text(encoding="utf-8")) if seals_path.exists() else {"schema": 1, "salt": SPLIT_SALT, "seals": []}
    problems = seal_problems(halves[HELDOUT], existing)
    if problems["salt"]:
        raise SystemExit(f"seals.yaml was made with salt {problems['salt']!r}, not {SPLIT_SALT!r}")
    unexplained = [i for i in problems["changed"] + problems["gone"] if i not in reseal]
    if unexplained:
        raise SystemExit(f"sealed held-out items changed or gone without a stated reason: {', '.join(unexplained)}")
    by_id = {i["item_id"]: i for i in halves[HELDOUT]}
    seals = []
    for entry in existing.get("seals") or []:
        if entry["item_id"] in reseal and not entry.get("withdrawn"):
            history = entry.get("history", []) + [{"sha256": entry["sha256"], "sealed_at": entry["sealed_at"], "replaced_because": reseal[entry["item_id"]]}]
            if entry["item_id"] not in by_id:
                seals.append({**entry, "withdrawn": True, "history": history})
                continue
            entry = {"item_id": entry["item_id"], "sha256": sha256_text(sealed_content(by_id[entry["item_id"]])), "sealed_at": sealed_at, "history": history}
        seals.append(entry)
    known = {e["item_id"] for e in seals}
    seals += [{"item_id": i["item_id"], "sha256": sha256_text(sealed_content(i)), "sealed_at": sealed_at} for i in halves[HELDOUT] if i["item_id"] not in known]
    for name, items in halves.items():
        write_jsonl(out_dir / f"{name}.jsonl", sorted(items, key=lambda i: i["item_id"]))
    seals_path.write_text(yaml.safe_dump({"schema": 1, "salt": SPLIT_SALT, "seals": sorted(seals, key=lambda e: e["item_id"])}, sort_keys=False, allow_unicode=True), encoding="utf-8")
    return {name: {origin: dict(Counter(gold_class(i["label"]) for i in items if i.get("origin", "natural") == origin))
                   for origin in ("natural", "constructed")} for name, items in halves.items()}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--gold", type=Path, required=True)
    parser.add_argument("--out-dir", type=Path, default=GOLD_DIR)
    parser.add_argument("--sealed-at", default=date.today().isoformat())
    parser.add_argument("--reseal", nargs=2, action="append", default=[], metavar=("ITEM_ID", "REASON"),
                        help="a sealed item whose change is meant, with the reason kept in its history")
    args = parser.parse_args(argv)
    result = write_halves(read_jsonl(args.gold), args.out_dir, args.sealed_at, dict(args.reseal))
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
