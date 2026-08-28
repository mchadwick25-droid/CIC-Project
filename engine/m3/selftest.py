"""Stage-4 gate (Build-Blueprint.md SS5): "catches a seeded register defect
and a seeded fabrication on the fixture world." Mirrors engine/m1/selftest.py's
shape: run the battery clean (must be all-pass), then once per M3-layer
entry in fixtures/seeded_defects.yaml, mutated (must fail, and specifically
must fail via the probe(s) the defect actually touches - not just fail
somewhere).
"""
import copy
import json
import sys
from pathlib import Path

import yaml

from engine.m1.loader import load_world_records
from engine.m1.mutate import apply as apply_mutation

from . import harness, results

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFECTS_PATH = REPO_ROOT / "fixtures" / "seeded_defects.yaml"
REPORT_PATH = Path(__file__).resolve().parent / "reports" / "selftest-report.json"
WORLD_KEY = "fix"


def _load_m3_defects() -> list[dict]:
    defects = yaml.safe_load(DEFECTS_PATH.read_text())["defects"]
    return [d for d in defects if d.get("layer") == "M3"]


def _advisory_register_findings(battery) -> list[str]:
    """Findings the register heuristic recorded without failing the probe -
    Mark's 2026-08-28 ruling made that check advisory (direction, not a
    gate; engine.m3.grading.register_check's own docstring carries the
    ruling). The seeded-defect proof and the anti-inertness proof both
    survive with "flag" meaning DETECTED: a seeded register defect must
    surface as an advisory finding, and the clean fixture must surface
    none."""
    return [
        f
        for r in battery
        for c in r.checks
        if c["check"] == "register_coined_aphorism_heuristic"
        for f in c.get("findings", [])
    ]


def run() -> dict:
    clean_records = load_world_records(WORLD_KEY)
    baseline = harness.run_battery(WORLD_KEY, clean_records)
    baseline_advisories = _advisory_register_findings(baseline)
    # Anti-inertness now includes the advisory channel: a clean fixture
    # must neither fail probes nor trip advisory register findings.
    baseline_pass = all(r.passed for r in baseline) and not baseline_advisories
    baseline_failures = [r.probe_id for r in baseline if not r.passed]

    defect_results = []
    for defect in _load_m3_defects():
        mutated = copy.deepcopy(clean_records)
        apply_mutation(mutated, defect)
        battery = harness.run_battery(WORLD_KEY, mutated)
        failing = [r for r in battery if not r.passed]
        caught = len(failing) > 0 or bool(_advisory_register_findings(battery))
        defect_results.append(
            {
                "id": defect["id"],
                "gate": defect["gate"],
                "status": "caught" if caught else "MISSED",
                "failing_probes": [r.probe_id for r in failing],
                "findings": [c for r in failing for c in r.checks if not c["passed"]],
                "advisory_register_findings": _advisory_register_findings(battery),
            }
        )

    missed = [d for d in defect_results if d["status"] == "MISSED"]
    overall_pass = baseline_pass and not missed

    baseline_results_doc = results.build_results(WORLD_KEY, baseline, mock_harness=True)

    return {
        "stage": "4",
        "world": WORLD_KEY,
        "baseline_clean_fixture": {"pass": baseline_pass, "failing_probes": baseline_failures, "advisory_register_findings": baseline_advisories},
        "defects": defect_results,
        "overall_pass": overall_pass,
        "admission_results_preview": baseline_results_doc,
    }


def main() -> int:
    report = run()
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in report.items() if k != "admission_results_preview"}, indent=2))
    return 0 if report["overall_pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
