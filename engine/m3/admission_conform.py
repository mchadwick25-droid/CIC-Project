"""Admission bound to registry state (slice 11): every admitted or open world
must have a live admission report run on what the runtime reads from the
package the registry pins - its compiled/ files without their generated-by
stamps (engine.m2.manifest.compiled_content_hash) - and under the engine's current shape segment. That report
must pass every sealed probe, or the probes it failed must be covered by a
ruling recorded against that same compiled hash in admission_rulings.yaml.
A change to what the voice reads, or to the shape, therefore needs a fresh
admission run; a change only to the validation report or the frozen record
copy does not. A report written before content hashes were recorded counts
when it ran on the pinned package itself.

Run: python -m engine.m3.admission_conform    (exits 1 on any failure)
"""
import json
import sys
from pathlib import Path

import yaml

from engine.m1.registry import load_registry
from engine.m2.manifest import package_content_hash
from engine.shape import SHAPE_HASH

REPO_ROOT = Path(__file__).resolve().parents[2]
REPORTS_DIR = Path(__file__).resolve().parent / "reports"
RULINGS_PATH = Path(__file__).resolve().parent / "admission_rulings.yaml"
ADMITTED_STATES = {"admitted", "open"}


def load_reports(reports_dir: Path = REPORTS_DIR) -> list[dict]:
    """Every live admission report that records the package hash it ran on."""
    found = []
    for path in sorted(reports_dir.rglob("live-admission-report*.json")):
        doc = json.loads(path.read_text())
        settings = doc.get("run_settings") or {}
        if settings.get("probe_limit"):
            continue
        hashes = settings.get("package_manifest_hash") or {}
        compiled = settings.get("package_content_hash") or {}
        for world, result in (doc.get("worlds") or {}).items():
            if world in hashes and result.get("battery_size"):
                failed = sorted(p["probe_id"] for p in result.get("per_probe", []) if not p.get("passed"))
                found.append({
                    "path": str(path.relative_to(REPO_ROOT)), "world": world, "manifest_hash": hashes[world],
                    "compiled_hash": compiled.get(world),
                    "shape_hash": settings.get("shape_hash"),
                    "pass_count": result.get("pass_count"), "battery_size": result["battery_size"], "failed": failed,
                })
    return found


def load_rulings(path: Path = RULINGS_PATH) -> list[dict]:
    if not path.exists():
        return []
    return yaml.safe_load(path.read_text()) or []


def pinned_compiled_hash(entry: dict, repo_root: Path = REPO_ROOT) -> str | None:
    location = (entry.get("package") or {}).get("location")
    return package_content_hash(repo_root / location) if location else None


def check(registry: dict, reports: list[dict], rulings: list[dict], shape: str = SHAPE_HASH,
          compiled_of=pinned_compiled_hash) -> list[str]:
    """The failures, one line each; empty when every admitted world conforms."""
    failures = []
    for world, entry in sorted(registry.items()):
        if entry.get("state") not in ADMITTED_STATES:
            continue
        pinned = (entry.get("package") or {}).get("manifest_hash")
        pinned_compiled = compiled_of(entry)

        def same_package(item: dict) -> bool:
            if item.get("compiled_hash") and pinned_compiled:
                return item["compiled_hash"] == pinned_compiled
            return item.get("manifest_hash") == pinned

        runs = [r for r in reports if r["world"] == world and same_package(r) and r["shape_hash"] == shape]
        if not runs:
            failures.append(f"{world}: no live admission report on what the pinned package {pinned} compiles "
                            f"(compiled {pinned_compiled}) under shape {shape}; "
                            "run engine.m3.live_admission_run for it and commit the report")
            continue
        covered = {tuple(sorted(r.get("failing_probes", []))) for r in rulings
                   if r.get("world") == world and same_package(r)}
        if any(not r["failed"] or tuple(r["failed"]) in covered for r in runs):
            continue
        best = max(runs, key=lambda r: r["pass_count"] or 0)
        failures.append(f"{world}: best run on {pinned} passed {best['pass_count']}/{best['battery_size']} "
                        f"(failed {', '.join(best['failed'])}) and no ruling in admission_rulings.yaml covers it")
    return failures


def main() -> int:
    failures = check(load_registry(), load_reports(), load_rulings())
    for line in failures:
        print(line)
    print(f"admission conform: {len(failures)} failure(s)")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
