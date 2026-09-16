"""M9's own selftest, mirroring engine/m1/selftest.py's contract exactly:
"the clean fixture is clean; every seeded M9 defect fires its named check;
inertness reporting fires." Reads fixtures/seeded_defects.yaml's
`layer: M9` entries.

Unlike M1's defects (which only ever mutate records/fix/**), an M9 defect
may target three different things - `target_kind: record | bucket | pairs`,
this increment's own extension to that catalog's mutation vocabulary
(fixtures/seeded_defects.yaml's own header names it). `record` reuses
engine.m1.mutate.apply() directly (an M9 defect can mutate a record field
exactly like an M1 one can - kind, shelf_row and a quote's text all live
on records). `bucket` and `pairs` mutate a deep copy of the RAW bucket
rows / PAIRS.yaml data engine/m9/loader.py reads, before build_shelf()
ever turns it into a Shelf - always in memory, never touching a file.
"""
import copy
import json
import sys
from pathlib import Path

import yaml

from engine.m1 import mutate
from engine.m1.loader import load_world_records
from engine.m1.registry import load_registry

from . import loader
from .confinement import CHECKS, run_all
from .shelf import build_shelf

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFECTS_PATH = REPO_ROOT / "fixtures" / "seeded_defects.yaml"
REPORT_PATH = Path(__file__).resolve().parent / "reports" / "selftest-report.json"
WORLD_KEY = "fix"


def _load_defects() -> list[dict]:
    with open(DEFECTS_PATH, encoding="utf-8") as f:
        return yaml.safe_load(f)["defects"]


def _apply_bucket_mutation(bucket_rows: list[dict], defect: dict) -> None:
    mutation = defect["mutation"]
    row = next((r for r in bucket_rows if r.get("row_id") == defect["target_row"]), None)
    if row is None:
        raise KeyError(f"no bucket row {defect['target_row']!r} in this copy")
    op = mutation["op"]
    if op in ("set_field", "add_field"):
        row[mutation["path"]] = mutation["value"]
    elif op == "delete_field":
        row.pop(mutation["path"], None)
    else:
        raise ValueError(f"unknown mutation op {op!r} in defect {defect['id']!r}")


def _apply_pairs_mutation(pairs_list: list[dict], defect: dict) -> None:
    mutation = defect["mutation"]
    wanted = {defect["target_pair_a"], defect["target_pair_b"]}
    pair = next((p for p in pairs_list if {p.get("a"), p.get("b")} == wanted), None)
    if pair is None:
        raise KeyError(f"no pair {sorted(wanted)} in this copy")
    op = mutation["op"]
    if op in ("set_field", "add_field"):
        pair[mutation["path"]] = mutation["value"]
    elif op == "delete_field":
        pair.pop(mutation["path"], None)
    else:
        raise ValueError(f"unknown mutation op {op!r} in defect {defect['id']!r}")


def _run_one_defect(defect: dict, clean_records: dict, census_id: str, bucket_rows: list[dict],
                     pairs_list: list[dict], parties: dict, units: dict, vendored_files: frozenset) -> dict[str, list[str]]:
    target_kind = defect.get("target_kind", "record")
    records = clean_records
    rows = bucket_rows
    pairs = pairs_list

    if target_kind == "record":
        records = copy.deepcopy(clean_records)
        mutate.apply(records, defect)
    elif target_kind == "bucket":
        rows = copy.deepcopy(bucket_rows)
        _apply_bucket_mutation(rows, defect)
    elif target_kind == "pairs":
        pairs = copy.deepcopy(pairs_list)
        _apply_pairs_mutation(pairs, defect)
    else:
        raise ValueError(f"unknown target_kind {target_kind!r} in defect {defect['id']!r}")

    shelf = build_shelf(
        world_key=WORLD_KEY,
        census_id=census_id,
        bucket_rows=rows,
        pairs_list=pairs,
        parties=parties,
        units_by_file=units,
        vendored_files=vendored_files,
    )
    return run_all(records, shelf)


def run() -> dict:
    registry = load_registry()
    entry = registry[WORLD_KEY]
    census_id = entry["census_id"]
    clean_records = load_world_records(WORLD_KEY)

    bucket_rows = loader.read_bucket_rows(census_id)
    pairs_list, parties = loader.read_pairs()
    units = loader.read_units(bucket_rows, clean_records)
    vendored_files = loader.read_vendored_files()

    clean_shelf = build_shelf(
        world_key=WORLD_KEY, census_id=census_id, bucket_rows=bucket_rows,
        pairs_list=pairs_list, parties=parties, units_by_file=units, vendored_files=vendored_files,
    )
    baseline = run_all(clean_records, clean_shelf)
    baseline_clean = {name: findings for name, findings in baseline.items() if findings}

    defects = [d for d in _load_defects() if d.get("layer") == "M9" and d["id"] != "m9-inertness-proof"]
    fired_checks: set[str] = set()
    defect_results = []

    for defect in defects:
        run_report = _run_one_defect(defect, clean_records, census_id, bucket_rows, pairs_list, parties, units, vendored_files)
        check_name = defect["gate"]
        findings = run_report.get(check_name, [])
        fired = len(findings) > 0
        if fired:
            fired_checks.add(check_name)
        defect_results.append({
            "id": defect["id"],
            "gate": check_name,
            "status": "caught" if fired else "MISSED",
            "findings": findings,
        })

    inert_checks = sorted(
        name for name in CHECKS if name not in fired_checks or baseline.get(name)
    )
    missed = [r for r in defect_results if r["status"] == "MISSED"]
    overall_pass = not baseline_clean and not missed and not inert_checks

    return {
        "stage": "M9-increment-3",
        "world": WORLD_KEY,
        "baseline_clean_fixture": {
            "pass": not baseline_clean,
            "findings_by_check": baseline_clean,
        },
        "defects": defect_results,
        "inertness": {
            "pass": not inert_checks,
            "checks_never_fired_or_not_silent_on_clean": inert_checks,
        },
        "overall_pass": overall_pass,
    }


def main() -> int:
    report = run()
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0 if report["overall_pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
