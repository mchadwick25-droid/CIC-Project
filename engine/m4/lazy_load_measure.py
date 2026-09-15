"""Stage-5 gate item: "lazy world load/unload measured." Runs the real
LazyWorldLoader against the REAL committed fixture package (whichever
package_dir/manifest_hash records/worlds/fix.yaml currently registers)
and records real wall-clock timings for: a cold load (disk read + hash
verification), a warm load (cache hit, no disk read), an unload, and a
second cold load (proving unload actually evicted rather than being a
no-op). No model call - pure I/O, free to run any time, unlike the safety
script or a real generation call.
"""
import json
import sys
from pathlib import Path

from engine.m1.registry import load_registry
from engine.m4.world_loader import LazyWorldLoader

REPO_ROOT = Path(__file__).resolve().parents[2]
REPORT_PATH = Path(__file__).resolve().parent / "reports" / "lazy-load-report.json"


def run() -> dict:
    registry = load_registry()
    entry = registry["fix"]
    package_dir = REPO_ROOT / entry["package"]["location"]
    manifest_hash = entry["package"]["manifest_hash"]

    loader = LazyWorldLoader()

    _world, cold_load = loader.load("fix", package_dir=package_dir, expected_manifest_hash=manifest_hash)
    _world, warm_load = loader.load("fix", package_dir=package_dir, expected_manifest_hash=manifest_hash)
    unload_timing = loader.unload("fix")
    _world, cold_reload = loader.load("fix", package_dir=package_dir, expected_manifest_hash=manifest_hash)

    report = {
        "world_key": "fix",
        "package_dir": str(package_dir.relative_to(REPO_ROOT)),
        "manifest_hash": manifest_hash,
        "measurements": {
            "cold_load_seconds": cold_load.seconds,
            "warm_load_seconds (cache hit)": warm_load.seconds,
            "unload_seconds": unload_timing.seconds,
            "cold_reload_seconds (proves unload actually evicted)": cold_reload.seconds,
        },
        "cache_hit_flags": {"cold_load": cold_load.cache_hit, "warm_load": warm_load.cache_hit, "cold_reload": cold_reload.cache_hit},
        "note": (
            "This fixture package is small (312K total across manifest+compiled+records+validation) - "
            "the timings here prove the MECHANISM (lazy on first use, cache hit avoids a second read, "
            "unload actually evicts) rather than production latency at real-world scale, which will carry "
            "larger compiled artifacts (FAISS indexes, a longer prompt/capsule) once a real world is built."
        ),
    }
    report["mechanism_proven"] = (
        cold_load.cache_hit is False
        and warm_load.cache_hit is True
        and cold_reload.cache_hit is False
        and warm_load.seconds <= cold_load.seconds
    )
    return report


def main() -> int:
    report = run()
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0 if report["mechanism_proven"] else 1


if __name__ == "__main__":
    sys.exit(main())
