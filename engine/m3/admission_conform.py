"""Admission bound to registry state (slice 11): every admitted or open world
must have a live admission report run on what the runtime reads from the
package the registry pins - its compiled/ files without their generated-by
stamps (engine.m2.manifest.compiled_content_hash) - and under the engine's current shape segment. That report
must pass every sealed probe, or the probes it failed must be covered by a
ruling recorded against that same compiled hash in admission_rulings.yaml.
A change to what the voice reads, or to the shape, therefore needs a fresh
admission run; a change only to the validation report or the frozen record
copy does not. A report written before content hashes were recorded carries
only the manifest hash of the package it ran on; content-bindings.json gives
that package's compiled hash, computed from the package restored and checked
against its own manifest.

Run: python -m engine.m3.admission_conform    (exits 1 on any failure)
     python -m engine.m3.admission_conform bind --at <commit> <package dir>...
"""
import json
import sys
from pathlib import Path

import yaml

from engine.m1.registry import load_registry
from engine.m2.canonical import sha256_prefixed
from engine.m2.manifest import manifest_hash, package_content_hash
from engine.shape import SHAPE_HASH

REPO_ROOT = Path(__file__).resolve().parents[2]
REPORTS_DIR = Path(__file__).resolve().parent / "reports"
RULINGS_PATH = Path(__file__).resolve().parent / "admission_rulings.yaml"
BINDINGS_PATH = REPORTS_DIR / "content-bindings.json"
ADMITTED_STATES = {"admitted", "open"}


def load_bindings(path: Path = BINDINGS_PATH) -> dict[str, str]:
    """Package manifest hash -> compiled content hash, for packages that
    admission reports name only by manifest."""
    if not path.exists():
        return {}
    return {m: b["compiled"] for m, b in json.loads(path.read_text())["bindings"].items()}


def load_reports(reports_dir: Path = REPORTS_DIR, bindings: dict[str, str] | None = None) -> list[dict]:
    """Every live admission report that records the package hash it ran on."""
    bindings = load_bindings() if bindings is None else bindings
    found = []
    for path in sorted(reports_dir.rglob("live-admission-report*.json")):
        doc = json.loads(path.read_text())
        settings = doc.get("run_settings") or {}
        hashes = settings.get("package_manifest_hash") or {}
        compiled = settings.get("package_content_hash") or {}
        for world, result in (doc.get("worlds") or {}).items():
            if world in hashes and result.get("battery_size"):
                failed = sorted(p["probe_id"] for p in result.get("per_probe", []) if not p.get("passed"))
                found.append({
                    "path": str(path.relative_to(REPO_ROOT)), "world": world, "manifest_hash": hashes[world],
                    "compiled_hash": compiled.get(world) or bindings.get(hashes[world]),
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


def bind(package_dirs: list[Path], at: str, path: Path = BINDINGS_PATH) -> dict[str, str]:
    """Record each package's compiled hash under its manifest hash. Every
    compiled file must match the package's own manifest, so the hash is of
    exactly the package the manifest names."""
    doc = json.loads(path.read_text()) if path.exists() else {"bindings": {}}
    added = {}
    for package_dir in package_dirs:
        manifest = json.loads((package_dir / "manifest.json").read_text())
        compiled = {k: v for k, v in manifest["files"].items() if k.startswith("compiled/")}
        for rel, digest in compiled.items():
            if sha256_prefixed((package_dir / rel).read_bytes()) != digest:
                raise ValueError(f"{package_dir / rel} does not match its manifest; restore the package first")
        content = package_content_hash(package_dir)
        doc["bindings"][manifest_hash(manifest)] = {"compiled": content, "world": manifest["world_key"], "restored_at": at}
        added[manifest_hash(manifest)] = content
    doc["bindings"] = dict(sorted(doc["bindings"].items()))
    path.write_text(json.dumps(doc, indent=2) + "\n")
    return added


def main() -> int:
    if sys.argv[1:2] == ["bind"]:
        args = sys.argv[2:]
        at = args[args.index("--at") + 1]
        dirs = [Path(a) for i, a in enumerate(args) if a != "--at" and (i == 0 or args[i - 1] != "--at")]
        for m, c in bind(dirs, at).items():
            print(f"bound {m} -> {c}")
        return 0
    failures = check(load_registry(), load_reports(), load_rulings())
    for line in failures:
        print(line)
    print(f"admission conform: {len(failures)} failure(s)")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
