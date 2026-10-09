"""Thin CLI over the pure census_sync. Same shape as engine/m2/cli.py's
build/staleness-check pair: `sync` writes, `check` only diffs (the CI gate).
"""
import argparse
import json
import sys
from pathlib import Path

from engine.m1.registry import load_registry

from . import atlas_html
from .census_atlas_sync import compare_edges, sync_atlas
from .census_sync import sync_census

REPO_ROOT = Path(__file__).resolve().parents[2]
CENSUS_PATH = REPO_ROOT / "cic-website" / "data" / "world-census.json"
ATLAS_PATH = REPO_ROOT / "cic-website" / "atlas-v3.html"


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


def _summarize_changes(changes: list[dict]) -> list[dict]:
    # Full old/new values can be entire documentedStories arrays - too long
    # to usefully print to a terminal. The CLI output is a human-readable
    # summary; sync_atlas's own return value (used by callers and tests)
    # still carries the full old/new.
    def brief(v):
        if isinstance(v, (list, dict)):
            return f"<{type(v).__name__}, {len(v)} item(s)>"
        if isinstance(v, str) and len(v) > 80:
            return v[:77] + "..."
        return v

    return [{"id": c["id"], "field": c["field"], "old": brief(c["old"]), "new": brief(c["new"])} for c in changes]


def cmd_atlas_sync(args: argparse.Namespace) -> int:
    census = _load_census()
    atlas_movements = atlas_html.read_movements(ATLAS_PATH)
    new_movements, changes = sync_atlas(census, atlas_movements)
    updates: dict[str, dict] = {}
    for c in changes:
        updates.setdefault(c["id"], {})[c["field"]] = c["new"]
    if updates:
        atlas_html.apply_movement_updates(ATLAS_PATH, updates)
    # Edges are compared, never written: a difference is fixed in census.json
    # and in the Atlas's embedded copy by hand, so it must not pass silently.
    edge_drift = compare_edges(census, atlas_html.read_edges(ATLAS_PATH))
    print(json.dumps({"changed": bool(changes), "changes": _summarize_changes(changes), "edgeDrift": _summarize_changes(edge_drift)}, indent=2))
    return 1 if edge_drift else 0


def cmd_atlas_check(args: argparse.Namespace) -> int:
    census = _load_census()
    atlas_movements = atlas_html.read_movements(ATLAS_PATH)
    _, changes = sync_atlas(census, atlas_movements)
    changes = changes + compare_edges(census, atlas_html.read_edges(ATLAS_PATH))
    passed = not changes
    print(json.dumps({"pass": passed, "changes": _summarize_changes(changes)}, indent=2))
    return 0 if passed else 1


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="python -m engine.m6.cli")
    sub = parser.add_subparsers(dest="command", required=True)

    sync = sub.add_parser("sync", help="sync world-census.json's registry-derivable fields from records/worlds.yaml, writing the file if it changed")
    sync.set_defaults(func=cmd_sync)

    check = sub.add_parser("check", help="report drift between world-census.json and what sync would produce, without writing - the CI gate")
    check.set_defaults(func=cmd_check)

    atlas_sync = sub.add_parser("atlas-sync", help="sync atlas-v3.html's embedded movement records from world-census.json (census.json is authoritative), writing the file if it changed")
    atlas_sync.set_defaults(func=cmd_atlas_sync)

    atlas_check = sub.add_parser("atlas-check", help="report drift between atlas-v3.html and world-census.json without writing - the CI gate")
    atlas_check.set_defaults(func=cmd_atlas_check)

    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
