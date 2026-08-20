"""validation/ folder assembly (Artifact-2 SS1): gates-report.json is real
(runs the actual M1 battery via engine.m1.gates - the same code stage 1's
selftest already proved catches every seeded defect). admission/
results.json stays a placeholder here on purpose, even after stage 4:
engine/m2 (the compiler) is one of the code paths canon/sealed_probes/
README.md and engine/canon/check_seal_isolation.py bar from the sealed
probe plaintext, and engine.m3.harness reads that plaintext - so M2 must
never import M3, even transitively through "just building the package."
Real admission evidence lives at engine/m3/reports/selftest-report.json
instead, produced by M3 directly, never routed through the compiler.
signoffs.json stays a placeholder too: Mark's real touchpoints don't apply
to a synthetic, never-admitted fixture world.
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
                f"{world_key} has no admission run bundled into its package by design: M2 (this "
                "module) is barred from importing M3, even to embed a real result, because M3 is "
                "the sealed probes' one authorized reader and M2 is explicitly not (canon/"
                "sealed_probes/README.md). See engine/m3/reports/selftest-report.json for the real "
                "(mock-harness) stage-4 evidence, kept separate from any package on purpose."
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
