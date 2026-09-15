"""Thin CLI over the pure census_sync. Same shape as engine/m2/cli.py's
build/staleness-check pair: `sync` writes, `check` only diffs (the CI gate).
"""
import argparse
import json
import sys
from pathlib import Path

from engine.m1.registry import load_registry

from .census_sync import sync_census

REPO_ROOT = Path(__file__).resolve().parents[2]
CENSUS_PATH = REPO_ROOT / "cic-website" / "data" / "world-census.json"


def _serialize(census: dict) -> bytes:
    # Matches the committed file's own formatting exactly (verified by
    # round-tripping it byte-for-byte before this module was written) -
    # indent=1, non-ASCII characters written literally, one trailing newline.
    return (json.dumps(census, indent=1, ensure_ascii=False) + "\n").encode("utf-8")


def _load_census(path: Path = CENSUS_PATH) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def cmd_sync(args: argparse.Namespace) -> int:
    registry = load_registry()
    census = _load_census()
    new_census, changes = sync_census(registry, census)
    if changes:
        CENSUS_PATH.write_bytes(_serialize(new_census))
    print(json.dumps({"changed": bool(changes), "changes": changes}, indent=2))
    return 0


def cmd_check(args: argparse.Namespace) -> int:
    registry = load_registry()
    census = _load_census()
    new_census, changes = sync_census(registry, census)
    passed = not changes
    print(json.dumps({"pass": passed, "changes": changes}, indent=2))
    return 0 if passed else 1


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="python -m engine.m6.cli")
    sub = parser.add_subparsers(dest="command", required=True)

    sync = sub.add_parser("sync", help="sync world-census.json's registry-derivable fields from records/worlds.yaml, writing the file if it changed")
    sync.set_defaults(func=cmd_sync)

    check = sub.add_parser("check", help="report drift between world-census.json and what sync would produce, without writing - the CI gate")
    check.set_defaults(func=cmd_check)

    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
