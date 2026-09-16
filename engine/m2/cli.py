"""Thin CLI over the pure compiler. Wall-clock/git-sha resolution happens
only here, never inside compile_world() itself, so the compiler stays a pure
function the determinism check can call twice with identical arguments.
"""
import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

from .checks import determinism_twice, restore_package, staleness_sweep
from .compiler import compile_and_hash

REPO_ROOT = Path(__file__).resolve().parents[2]


def _git_head() -> str:
    return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPO_ROOT, text=True).strip()


def _new_package_id() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H-%M-%SZ")


def _write_package(package: dict[str, bytes], out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    for rel_path, content in package.items():
        target = out_dir / rel_path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(content)


def cmd_build(args: argparse.Namespace) -> int:
    records_commit = args.records_commit or _git_head()
    compiler_version = args.compiler_version or _git_head()
    package_id = args.package_id or _new_package_id()
    package, digest = compile_and_hash(
        world_key=args.world_key,
        package_id=package_id,
        records_commit=records_commit,
        compiler_version=compiler_version,
    )
    out_dir = REPO_ROOT / "packages" / args.world_key / package_id
    _write_package(package, out_dir)
    location = str(out_dir.relative_to(REPO_ROOT))
    print(json.dumps({"package_id": package_id, "manifest_hash": digest, "location": location}, indent=2))
    return 0


def cmd_determinism_check(args: argparse.Namespace) -> int:
    diffs = determinism_twice(
        world_key=args.world_key,
        package_id="determinism-check",
        records_commit=args.records_commit or _git_head(),
        compiler_version=args.compiler_version or _git_head(),
    )
    if diffs:
        print(json.dumps({"pass": False, "differing_paths": diffs}, indent=2))
        return 1
    print(json.dumps({"pass": True, "differing_paths": []}, indent=2))
    return 0


def cmd_staleness_check(args: argparse.Namespace) -> int:
    results = staleness_sweep()
    overall_pass = all(not r["stale"] for r in results.values())
    print(json.dumps({"pass": overall_pass, "worlds": results}, indent=2))
    return 0 if overall_pass else 1


def cmd_upload(args: argparse.Namespace) -> int:
    """WO-1 (2026-09-16): pushes an already-built package to object
    storage, so a deploy running the OLD image can still serve it -
    Artifact-2 SS5's "packages are built by CI, uploaded to object
    storage." Manual for now (a human runs this after `build`, the same
    way a world-build thread already runs `build` by hand); wiring a CI
    job to call it automatically on every records/ change is real
    follow-on work, not done here - see the object-storage runbook."""
    from engine.m4 import object_storage

    if not object_storage.is_configured():
        print("CIC_API_PACKAGE_BUCKET is not set - nothing to upload to (see the object-storage runbook)", file=sys.stderr)
        return 1
    from engine.m1.registry import load_registry

    registry = load_registry()
    entry = registry.get(args.world_key)
    if entry is None:
        print(f"{args.world_key!r} is not in the registry", file=sys.stderr)
        return 1
    location = entry["package"]["location"]
    local_dir = REPO_ROOT / location
    if not (local_dir / "manifest.json").is_file():
        print(f"no manifest.json under {local_dir} - build it first (engine.m2.cli build {args.world_key})", file=sys.stderr)
        return 1
    keys = object_storage.upload_package_dir(local_dir, location)
    print(json.dumps({"world_key": args.world_key, "location": location, "objects_written": len(keys)}, indent=2))
    return 0


def cmd_restore(args: argparse.Namespace) -> int:
    from engine.m1.registry import load_registry, world_keys

    registry = load_registry()
    keys = [args.world_key] if args.world_key else world_keys(registry)
    results = [restore_package(k, registry=registry) for k in keys]
    ok = all(r["restored"] for r in results)
    print(json.dumps({"pass": ok, "worlds": results}, indent=2))
    return 0 if ok else 1


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="python -m engine.m2.cli")
    sub = parser.add_subparsers(dest="command", required=True)

    build = sub.add_parser("build", help="compile a world and write its package under packages/")
    build.add_argument("world_key")
    build.add_argument("--package-id")
    build.add_argument("--records-commit")
    build.add_argument("--compiler-version")
    build.set_defaults(func=cmd_build)

    det = sub.add_parser("determinism-check", help="compile a world twice, assert byte-identical output")
    det.add_argument("world_key")
    det.add_argument("--records-commit")
    det.add_argument("--compiler-version")
    det.set_defaults(func=cmd_determinism_check)

    restore = sub.add_parser("restore", help="rebuild the pinned package(s) from records onto disk - the compiled bytes are not in git")
    restore.add_argument("world_key", nargs="?", help="omit to restore every world in the registry")
    restore.set_defaults(func=cmd_restore)

    stale = sub.add_parser("staleness-check", help="recompile every built/admitted/open world, check against its manifest")
    stale.set_defaults(func=cmd_staleness_check)

    upload = sub.add_parser("upload", help="push an already-built package to object storage (WO-1), so a running deploy can fetch it without a redeploy")
    upload.add_argument("world_key")
    upload.set_defaults(func=cmd_upload)

    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
