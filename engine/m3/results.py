"""validation/admission/results.json (Artifact-2 SS1: "battery results -
blind protocol, sealed-key refs"). Results reference probes by probe_id
only - never the sealed plaintext wording - so this file is safe to commit
and read by anyone, unlike canon/sealed_probes/plaintext/.
"""
from dataclasses import asdict

from .harness import ProbeResult


def build_results(world_key: str, probe_results: list[ProbeResult], *, mock_harness: bool) -> dict:
    return {
        "world_key": world_key,
        "protocol": "blind",
        "center_tested_first": True,
        "battery_size": len(probe_results),
        "results": [asdict(r) for r in probe_results],
        "overall_pass": all(r.passed for r in probe_results),
        "mock_harness": mock_harness,
        "note": (
            "mock_harness=true means this run used FixtureRecordAnswerer (a deterministic, "
            "no-model stand-in) and the narrow register heuristic in grading.py, not a live "
            "model-graded admission run. See engine/m3/generation.py's LiveModelAnswerer "
            "docstring for why: no model provider is configured yet (spec SS10)."
            if mock_harness
            else "live model-graded run."
        ),
    }
