"""Stage-1 gate: "selftest passes the clean fixture and fails every
seeded-defect fixture; inertness reporting fires" (Build-Blueprint.md SS5).

Reads fixtures/seeded_defects.yaml, runs the M1 gate battery against the
clean fixture world (must be all-green) and then against one mutated copy
per M1-layer defect (the named gate must fire, and only that run - the
mutation, not the copy machinery, is what's under test). M3-layer defects
are catalogued here but deferred to stage 4's admission harness, which does
not exist yet. Writes evidence to engine/m1/reports/selftest-report.json -
a stage's gate is evidence in the repo, never an assertion (blueprint SS5
progress discipline).
"""
import copy
import json
import sys
from pathlib import Path

import yaml

from . import gates, mutate
from .loader import load_fleet_records, load_world_records
from .registry import load_registry

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFECTS_PATH = REPO_ROOT / "fixtures" / "seeded_defects.yaml"
REPORT_PATH = Path(__file__).resolve().parent / "reports" / "selftest-report.json"
WORLD_KEY = "fix"


def _load_defects() -> list[dict]:
    with open(DEFECTS_PATH, encoding="utf-8") as f:
        return yaml.safe_load(f)["defects"]


def run() -> dict:
    registry = load_registry()
    fleet = load_fleet_records()
    clean_records = load_world_records(WORLD_KEY)

    baseline = gates.run_all(clean_records, fleet, registry)
    baseline_clean = {name: findings for name, findings in baseline.items() if findings}

    defects = _load_defects()
    fired_gates: set[str] = set()
    defect_results = []

    for defect in defects:
        if defect["id"] == "inertness-proof":
            continue
        if defect.get("layer") == "M3":
            defect_results.append(
                {"id": defect["id"], "gate": defect["gate"], "status": "deferred-to-stage-4"}
            )
            continue

        mutated = copy.deepcopy(clean_records)
        mutate.apply(mutated, defect)
        run_report = gates.run_all(mutated, fleet, registry)
        gate_name = defect["gate"]
        findings = run_report.get(gate_name, [])
        fired = len(findings) > 0
        if fired:
            fired_gates.add(gate_name)
        defect_results.append(
            {
                "id": defect["id"],
                "gate": gate_name,
                "status": "caught" if fired else "MISSED",
                "findings": findings,
            }
        )

    inert_gates = sorted(
        name for name in gates.GATES if name not in fired_gates or baseline.get(name)
    )

    missed = [r for r in defect_results if r.get("status") == "MISSED"]
    overall_pass = not baseline_clean and not missed and not inert_gates

    report = {
        "stage": "1",
        "world": WORLD_KEY,
        "baseline_clean_fixture": {
            "pass": not baseline_clean,
            "findings_by_gate": baseline_clean,
        },
        "defects": defect_results,
        "inertness": {
            "pass": not inert_gates,
            "gates_never_fired_or_not_silent_on_clean": inert_gates,
        },
        "overall_pass": overall_pass,
    }
    return report


def main() -> int:
    report = run()
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0 if report["overall_pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
