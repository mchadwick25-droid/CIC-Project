"""validation/ folder assembly (Artifact-2 SS1): gates-report.json is real
(runs the actual M1 battery via engine.m1.gates - the same code stage 1's
selftest already proved catches every seeded defect). admission/results.json
and signoffs.json are honest placeholders: M3 (stage 4) and Mark's real
touchpoints don't exist yet for this synthetic, never-admitted fixture
world, and a fabricated pass here would be exactly the invented-depth this
project rules against (spec principle 8, applied to tooling output as much
as to voice content).
"""
from engine.m1 import gates

from .canonical import canonical_json


def build_gates_report(records: dict, fleet: dict, registry: dict) -> bytes:
    report = gates.run_all(records, fleet, registry)
    payload = {
        "gates": {name: {"pass": not findings, "findings": findings} for name, findings in report.items()},
        "overall_pass": all(not findings for findings in report.values()),
    }
    return canonical_json(payload)


def build_admission_results(world_key: str) -> bytes:
    return canonical_json(
        {
            "status": "not_yet_run",
            "reason": (
                "M3 (the admission harness) is stage 4's deliverable and does not exist yet. "
                f"{world_key} is a synthetic fixture world that is never admitted or opened for "
                "real (records/worlds.yaml pins its state at building/built only)."
            ),
        }
    )


def build_signoffs(world_key: str) -> bytes:
    return canonical_json(
        {
            "identity_touchpoint": None,
            "living_tradition_determination": None,
            "freeze": None,
            "admission_read": None,
            "note": (
                f"{world_key} is a synthetic fixture world - none of Mark's four per-world "
                "touchpoints (spec SS4.3) apply to it; it is never admitted or opened for real."
            ),
            "scholarly_review_status": (
                "aspirational, not blocking (spec principle 15); the contribution fund is not "
                "yet established; the methods page states this plainly once M6 exists"
            ),
        }
    )
