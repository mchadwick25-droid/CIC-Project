"""The two CI-shaped checks Artifact-2 SS3 names: determinism (compiler runs
twice, diff must be empty) and staleness (recompile every built/admitted/
open world from its stored records_commit, and check it still produces the
package the registry is pinned to).

Staleness compares against the package's own manifest.json - which lists
every file with its sha256 - not against the stored bytes. Same guarantee,
because a manifest that matches a recompile file-for-file IS the package;
and it means the derived bytes need not be in the repository for the guard
to fire. At 100+ worlds (spec M1) a git tree of compiled packages is not a
place to keep them (principle 16: "packages live in S3-compatible object
storage"); a manifest per world is 24 KB and stays.
The compiler list is explicit here, never a glob (Build-Blueprint.md SS6
landmine: "a guard pointed at the wrong tree").
"""
import hashlib
import json
from pathlib import Path

from engine.m1.registry import load_registry

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


def _sha256(payload: bytes) -> str:
    return "sha256:" + hashlib.sha256(payload).hexdigest()


def _read_stored_manifest(location: Path) -> dict:
    """Only the manifest. The package's own file list, each with its hash -
    the whole contract, in one committed file."""
    return json.loads((location / "manifest.json").read_bytes())


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
        manifest_path = package_dir / "manifest.json"
        if not manifest_path.exists():
            results[world_key] = {"stale": True, "reason": f"no manifest.json at {location} - the pinned package's contract is missing"}
            continue
        stored_manifest = _read_stored_manifest(package_dir)
        recompiled = compile_world(
            world_key=world_key,
            package_id=stored_manifest["package_id"],
            records_commit=stored_manifest["records_commit"],
            compiler_version=_compiler_version_from(stored_manifest),
        )
        expected = dict(stored_manifest["files"])
        rebuilt = {path: _sha256(payload) for path, payload in recompiled.items() if path != "manifest.json"}
        diffs = sorted(p for p in set(expected) | set(rebuilt) if expected.get(p) != rebuilt.get(p))
        # the manifest itself must round-trip too, or the file list drifted
        if recompiled.get("manifest.json") and json.loads(recompiled["manifest.json"])["files"] != expected:
            diffs.append("manifest.json")
        results[world_key] = {"stale": bool(diffs), "diff": sorted(set(diffs))}
    return results


def _compiler_version_from(manifest: dict) -> str:
    # built_by = "cic-m2-compiler <version>"
    return manifest["built_by"].removeprefix("cic-m2-compiler ").strip()


def restore_package(world_key: str, *, registry: dict | None = None, repo_root: Path = REPO_ROOT) -> dict:
    """Rebuild the package the registry is pinned to, from records, onto disk.

    The compiled bytes are derived and are not in the repository (see the
    .gitignore note): a clean checkout has records/, worlds.yaml and each
    package's manifest.json, and nothing else. `build` is the wrong command
    for this - it mints a NEW package_id, so it produces a different package
    with a different hash, which is correct for a real rebuild and useless
    for restoring the one a session is pinned to. This recompiles using the
    manifest's own package_id, records_commit and compiler_version, writes
    the files where worlds.yaml expects them, and verifies every hash
    against the manifest before returning.
    """
    registry = registry if registry is not None else load_registry()
    entry = registry[world_key]
    location = repo_root / entry["package"]["location"]
    manifest = _read_stored_manifest(location)
    rebuilt = compile_world(
        world_key=world_key,
        package_id=manifest["package_id"],
        records_commit=manifest["records_commit"],
        compiler_version=_compiler_version_from(manifest),
    )
    mismatched = sorted(
        p for p, payload in rebuilt.items()
        if p != "manifest.json" and manifest["files"].get(p) != _sha256(payload)
    )
    if mismatched:
        return {"world_key": world_key, "restored": False, "mismatched": mismatched}
    written = 0
    for rel, payload in rebuilt.items():
        target = location / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(payload)
        written += 1
    return {"world_key": world_key, "restored": True, "files": written, "location": str(entry["package"]["location"])}
