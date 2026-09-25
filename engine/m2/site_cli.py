"""CLI + staleness sweep for the Website V2 world_front compiler stage
(engine.m2.site_compiler). Mirrors engine/m2/cli.py's own build/
staleness-check pair and engine/m2/checks.py's own staleness_sweep()
shape - see both for the established pattern this follows.

No world (fixture or real) has a world_front record yet - content
migration is a separate, later stage from this infrastructure. So
`staleness-check` currently finds nothing to check and passes trivially,
the same "0% fire rate is not automatically health" caveat
engine/m2/checks.py's own module comment already names for its sibling
sweep - which is exactly why the comparison logic below is wired for
real, not stubbed to `return True`, so it does real work the moment a
world_front record and a compiled cic-website/data/worlds/<census_id>.json
both exist.
"""
import argparse
import json
import re
import sys
from pathlib import Path

from engine.m1.loader import RECORDS_ROOT, load_fleet_records, load_world_records
from engine.m1.registry import load_registry

from .site_compiler import compile_world_front

REPO_ROOT = Path(__file__).resolve().parents[2]
SITE_DATA_DIR = REPO_ROOT / "cic-website" / "data" / "worlds"

# Parses compile_world_front()'s own `_generated_by` header back into the
# exact (compiler_version, records_commit) pair it was built from - the
# same "read the committed manifest's own provenance, recompile with
# those exact inputs, diff the result" discipline engine/m2/checks.py's
# own staleness_sweep() already uses against manifest.json's `built_by`.
_GENERATED_BY_RE = re.compile(
    r"^cic-m2-site-compiler (?P<compiler_version>\S+) from records_commit (?P<records_commit>\S+), "
)


def _find_world_front(records: dict) -> dict | None:
    for rec in records.values():
        if rec.get("record_type") == "world_front":
            return rec
    return None


def compile_site_json_for_world(
    world_key: str,
    *,
    compiler_version: str,
    records_commit: str,
    records_root: Path = RECORDS_ROOT,
) -> bytes | None:
    """The compiled site JSON for `world_key`, or None if that world has
    no world_front record - not a failure by itself, since a world
    without one simply has nothing for this compiler to produce yet."""
    fleet = load_fleet_records(records_root=records_root)
    records = load_world_records(world_key, records_root=records_root)
    world_front = _find_world_front(records)
    if world_front is None:
        return None
    return compile_world_front(
        world_front, records, fleet, compiler_version=compiler_version, records_commit=records_commit
    )


def _diff_keys(a: dict, b: dict) -> list[str]:
    return sorted({k for k in set(a) | set(b) if a.get(k) != b.get(k)})


def site_staleness_sweep(
    registry: dict | None = None, site_data_dir: Path = SITE_DATA_DIR
) -> dict[str, dict]:
    """Recompiles every migrated world's site JSON from its OWN committed
    file's pinned records_commit/compiler_version (read back out of that
    file's own `_generated_by` header), and reports it stale if that
    differs from what's actually committed. A world not yet admitted/open
    with no committed cic-website/data/worlds/<census_id>.json is simply
    absent from the results - not a pass, not a fail, the same as an
    unbuilt world in engine/m2/checks.py's own staleness_sweep(). An
    ADMITTED/OPEN world with no committed file is different: participants
    can already reach it, so a missing site JSON is reported stale rather
    than silently skipped - the same gap engine.m1.cross_world's own
    check_required_record_types_and_site_json flags from the records
    side (2026-09-25 CI/tooling audit)."""
    registry = registry if registry is not None else load_registry()
    results: dict[str, dict] = {}
    if not site_data_dir.is_dir():
        return results
    for world_key, entry in sorted(registry.items()):
        census_id = entry.get("census_id")
        if not census_id:
            continue
        site_json_path = site_data_dir / f"{census_id}.json"
        if not site_json_path.is_file():
            if entry.get("state") in ("admitted", "open"):
                results[world_key] = {
                    "stale": True,
                    "reason": f"{world_key} is {entry.get('state')} but {site_json_path} does not exist",
                }
            continue
        committed = json.loads(site_json_path.read_text(encoding="utf-8"))
        match = _GENERATED_BY_RE.match(committed.get("_generated_by", ""))
        if not match:
            results[world_key] = {
                "stale": True,
                "reason": f"{site_json_path} has no parseable _generated_by header",
            }
            continue
        recompiled_bytes = compile_site_json_for_world(
            world_key,
            compiler_version=match.group("compiler_version"),
            records_commit=match.group("records_commit"),
        )
        if recompiled_bytes is None:
            results[world_key] = {
                "stale": True,
                "reason": f"{site_json_path} is committed but {world_key} now has no world_front record",
            }
            continue
        recompiled = json.loads(recompiled_bytes)
        stale = recompiled != committed
        results[world_key] = {"stale": stale, "diff": _diff_keys(committed, recompiled) if stale else []}
    return results


def cmd_build(args: argparse.Namespace) -> int:
    registry = load_registry()
    entry = registry.get(args.world_key)
    if entry is None:
        print(f"{args.world_key!r} is not in the registry", file=sys.stderr)
        return 1
    census_id = entry.get("census_id")
    if not census_id:
        print(f"{args.world_key!r} has no census_id - nothing to name the compiled file after", file=sys.stderr)
        return 1
    compiled = compile_site_json_for_world(
        args.world_key, compiler_version=args.compiler_version, records_commit=args.records_commit
    )
    if compiled is None:
        print(f"{args.world_key!r} has no world_front record yet - nothing to compile", file=sys.stderr)
        return 1
    SITE_DATA_DIR.mkdir(parents=True, exist_ok=True)
    out_path = SITE_DATA_DIR / f"{census_id}.json"
    out_path.write_bytes(compiled)
    print(json.dumps({"world_key": args.world_key, "location": str(out_path.relative_to(REPO_ROOT))}, indent=2))
    return 0


def cmd_staleness_check(args: argparse.Namespace) -> int:
    results = site_staleness_sweep()
    overall_pass = all(not r["stale"] for r in results.values())
    print(json.dumps({"pass": overall_pass, "worlds": results}, indent=2))
    return 0 if overall_pass else 1


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="python -m engine.m2.site_cli")
    sub = parser.add_subparsers(dest="command", required=True)

    build = sub.add_parser("build", help="compile a world's world_front record to cic-website/data/worlds/<census_id>.json")
    build.add_argument("world_key")
    build.add_argument("--records-commit", required=True)
    build.add_argument("--compiler-version", required=True)
    build.set_defaults(func=cmd_build)

    stale = sub.add_parser("staleness-check", help="recompile every migrated world's site JSON, check against what's committed")
    stale.set_defaults(func=cmd_staleness_check)

    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
