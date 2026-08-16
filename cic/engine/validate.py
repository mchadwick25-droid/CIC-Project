#!/usr/bin/env python3
"""Schema validation for the clean system's record store.

Carried from the old tree's proven validator at the
clean-room setup, scrubbed to the parts that execute for records:
front-matter parsing, per-type jsonschema validation, and the
sentinel-string rejection. The gloss and traceability extras stayed
behind - they validate artifacts this system does not carry.

  python cic/engine/validate.py            # validate cic/records/**
  python cic/engine/validate.py --records DIR
"""
import argparse
import json
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent  # cic/
SCHEMA = json.loads((HERE / "records.schema.json").read_text(encoding="utf-8"))

SENTINELS = {"—", "-", "--", "n/a", "N/A", "none", "None"}


def parse_front_matter(path: Path):
    text = path.read_text(encoding="utf-8")
    if path.suffix == ".yaml":
        return yaml.safe_load(text)
    if not text.startswith("---"):
        raise ValueError(f"{path}: no front-matter fence")
    parts = text.split("\n---", 2)
    return yaml.safe_load(parts[0][3:])


def sentinel_violations(record):
    out = []
    r = record.get("retrieval") or {}
    for cond in r.get("retrieve_when") or []:
        if cond.strip() in SENTINELS:
            out.append(f"retrieve_when carries a sentinel string {cond!r} - use an empty list")
    for cond in r.get("do_not_retrieve_when") or []:
        if isinstance(cond, dict) and cond.get("text", "").strip() in SENTINELS:
            out.append("do_not_retrieve_when carries a sentinel string - use an empty list")
    return out


def validate_record(record, source=""):
    import jsonschema
    errs = []
    rt = record.get("record_type")
    defs = SCHEMA["$defs"]
    if rt not in defs:
        return [f"{source}: unknown or missing record_type: {rt!r}"]
    sub = {"$defs": SCHEMA["$defs"], **defs[rt]}
    v = jsonschema.Draft202012Validator(sub)
    for e in sorted(v.iter_errors(record), key=lambda e: list(e.absolute_path)):
        errs.append(f"{source}: {'/'.join(str(p) for p in e.absolute_path) or '<root>'}: {e.message[:160]}")
    errs += [f"{source}: {m}" for m in sentinel_violations(record)]
    return errs


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--records", default=str(ROOT / "records"))
    args = p.parse_args()
    paths = sorted(Path(args.records).rglob("*.md")) + \
        sorted(Path(args.records).rglob("*.yaml"))
    n_ok, errs = 0, []
    for path in paths:
        try:
            rec = parse_front_matter(path)
        except Exception as exc:  # noqa: BLE001
            errs.append(f"{path}: unparseable front matter: {exc}")
            continue
        e = validate_record(rec, source=str(path.relative_to(ROOT.parent)))
        if e:
            errs.extend(e)
        else:
            n_ok += 1
    for e in errs:
        print(f"  ERROR: {e}")
    print(f"valid: {n_ok} / {len(paths)} files")
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main())
