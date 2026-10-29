"""The calibration and held-out halves of the gold set, and the seal on the
held-out half.

An item's half is fixed by a hash of its id alone, before any judge has seen
it, and never by its label, so a corrected label never moves an item. The
seal records, for every held-out item, the sha256 of its content (sentence,
bindings, commit) at the time it was sealed; a later edit to a sealed item is
detectable. Tuning reads the calibration half only; the held-out file is read
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
SEALED_FIELDS = ("item_id", "world", "records_commit", "bindings", "sentence")


def half(item_id: str) -> str:
    digest = hashlib.sha256(f"{SPLIT_SALT}:{item_id}".encode("utf-8")).hexdigest()
    return HELDOUT if int(digest[0], 16) < 8 else CALIBRATION


def sealed_content(item: dict) -> str:
    return json.dumps({k: item[k] for k in SEALED_FIELDS}, ensure_ascii=False, sort_keys=True)


def seal(items: list[dict], sealed_at: str) -> dict:
    return {
        "schema": 1, "salt": SPLIT_SALT,
        "seals": [{"item_id": i["item_id"], "sha256": sha256_text(sealed_content(i)), "sealed_at": sealed_at} for i in sorted(items, key=lambda i: i["item_id"])],
    }


def broken_seals(items: list[dict], seals: dict) -> list[str]:
    """Held-out items whose content no longer matches their seal, or that
    the seal does not hold."""
    want = {s["item_id"]: s["sha256"] for s in seals["seals"]}
    return sorted(i["item_id"] for i in items if want.get(i["item_id"]) != sha256_text(sealed_content(i)))


def write_halves(gold: list[dict], out_dir: Path, sealed_at: str) -> dict:
    halves = {CALIBRATION: [], HELDOUT: []}
    for item in gold:
        halves[half(item["item_id"])].append(item)
    out_dir.mkdir(parents=True, exist_ok=True)
    seals_path = out_dir / "seals.yaml"
    existing = yaml.safe_load(seals_path.read_text(encoding="utf-8")) if seals_path.exists() else {"seals": []}
    if broken := [s for s in broken_seals(halves[HELDOUT], existing) if s in {x["item_id"] for x in existing["seals"]}]:
        raise SystemExit(f"sealed held-out items changed: {', '.join(broken)}")
    known = {s["item_id"] for s in existing["seals"]}
    new = seal([i for i in halves[HELDOUT] if i["item_id"] not in known], sealed_at)["seals"]
    seals = {"schema": 1, "salt": SPLIT_SALT, "seals": sorted(existing["seals"] + new, key=lambda s: s["item_id"])}
    for name, items in halves.items():
        write_jsonl(out_dir / f"{name}.jsonl", sorted(items, key=lambda i: i["item_id"]))
    seals_path.write_text(yaml.safe_dump(seals, sort_keys=False, allow_unicode=True), encoding="utf-8")
    return {name: dict(Counter(gold_class(i["label"]) for i in items)) for name, items in halves.items()}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--gold", type=Path, required=True)
    parser.add_argument("--out-dir", type=Path, default=GOLD_DIR)
    parser.add_argument("--sealed-at", default=date.today().isoformat())
    args = parser.parse_args(argv)
    print(json.dumps(write_halves(read_jsonl(args.gold), args.out_dir, args.sealed_at), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
