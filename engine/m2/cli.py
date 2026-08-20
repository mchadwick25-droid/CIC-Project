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

from .checks import determinism_twice, staleness_sweep
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

    stale = sub.add_parser("staleness-check", help="recompile every built/admitted/open world, diff against stored")
    stale.set_defaults(func=cmd_staleness_check)

    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
