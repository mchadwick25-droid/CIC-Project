"""The CI-shaped package checks: determinism (compiler runs
twice, diff must be empty) and staleness (recompile every built/admitted/
open world from its stored records_commit, diff against what is stored).
The compiler list is explicit here, never a glob (Build-Blueprint.md SS6
landmine: "a guard pointed at the wrong tree").
"""
import json
from pathlib import Path

from engine.m1.registry import load_registry

from . import demo_net
from .compiler import compile_world

REPO_ROOT = Path(__file__).resolve().parents[2]
STALENESS_CHECKABLE_STATES = {"built", "admitted", "open"}


def determinism_twice(*, world_key: str, package_id: str, records_commit: str, compiler_version: str) -> list[str]:
    """Returns a list of differing paths; empty means byte-identical."""
    first = compile_world(
        world_key=world_key, package_id=package_id, records_commit=records_commit, compiler_version=compiler_version
    )
    second = compile_world(
        world_key=world_key, package_id=package_id, records_commit=records_commit, compiler_version=compiler_version
    )
    diffs = []
    all_paths = set(first) | set(second)
    for path in sorted(all_paths):
        if first.get(path) != second.get(path):
            diffs.append(path)
    return diffs


def _read_stored_package(location: Path) -> dict[str, bytes]:
    manifest_path = location / "manifest.json"
    package = {"manifest.json": manifest_path.read_bytes()}
    manifest = json.loads(package["manifest.json"])
    for path in manifest["files"]:
        package[path] = (location / path).read_bytes()
    return package


def staleness_sweep(registry: dict | None = None, repo_root: Path = REPO_ROOT) -> dict[str, dict]:
    registry = registry if registry is not None else load_registry()
    results = {}
    for world_key, entry in sorted(registry.items()):
        if entry.get("state") not in STALENESS_CHECKABLE_STATES:
            continue
        package_info = entry.get("package") or {}
        location = package_info.get("location")
        if not location:
            results[world_key] = {"stale": True, "reason": f"state={entry.get('state')!r} but no package.location recorded"}
            continue
        package_dir = repo_root / location
        stored = _read_stored_package(package_dir)
        stored_manifest = json.loads(stored["manifest.json"])
        recompiled = compile_world(
            world_key=world_key,
            package_id=stored_manifest["package_id"],
            records_commit=stored_manifest["records_commit"],
            compiler_version=_compiler_version_from(stored_manifest),
        )
        diffs = sorted(p for p in set(stored) | set(recompiled) if stored.get(p) != recompiled.get(p))
        results[world_key] = {"stale": bool(diffs), "diff": diffs}
    return results


def _compiler_version_from(manifest: dict) -> str:
    # built_by = "cic-m2-compiler <version>"
    return manifest["built_by"].removeprefix("cic-m2-compiler ").strip()


def demonstration_net_sweep(registry: dict | None = None, repo_root: Path = REPO_ROOT) -> dict[str, dict]:
    """Every checkable world's STORED package, run through the live
    grounding net (engine/m2/demo_net.py). Reads the shipped bytes rather
    than recompiling, so it reports what is actually serving live traffic
    today, not what a fixed compiler would produce - a world whose package
    predates a compiler fix stays visibly red here until it is recompiled
    and its registry entry committed, which is exactly the signal wanted."""
    registry = registry if registry is not None else load_registry()
    results = {}
    for world_key, entry in sorted(registry.items()):
        if entry.get("state") not in STALENESS_CHECKABLE_STATES:
            continue
        location = (entry.get("package") or {}).get("location")
        if not location:
            results[world_key] = {"pass": False, "reason": f"state={entry.get('state')!r} but no package.location recorded"}
            continue
        package_dir = repo_root / location
        results[world_key] = demo_net.build_demonstration_net_report(
            (package_dir / "compiled" / "prompt.txt").read_bytes(),
            (package_dir / "compiled" / "repository.json").read_bytes(),
        )
    return results
