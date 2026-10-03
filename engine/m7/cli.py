"""The M7 batch audit entry point (Artifact-8 §6):

    python -m engine.m7.cli audit --events-db PATH --out DIR [--since ISO]

Daily cadence = yesterday's --since; on-demand = no --since. Read-only over
the event log; deterministic; zero model calls, zero spend (phase 1,
Artifact-8 §3). Exit code 1 when any defect-severity finding surfaced, so
a scheduled run can page without parsing JSON - that is reporting posture,
not a bar (principle 10: the finding routes to the world build, nothing
here blocks anything live).
"""
import argparse
import sys
from pathlib import Path

from engine.m1.registry import load_registry
from engine.m4.store import Store
from engine.m7.instruments import run_all
from engine.m7.report import (
    build_rollup,
    write_canon_candidates,
    write_digest,
    write_rollup,
    write_session_audit,
)
from engine.m7.session_reader import read_session


_CITABLE_TYPES = ("doctrinal_witness", "term", "story", "quote", "honest_limit",
                  "gravity", "force", "contested_claim", "figure", "world_core")


def _world_shelves(registry: dict) -> dict[str, dict]:
    """world_key -> citable shelf, read from each formation world's pinned
    package repository (read-only, same posture as everything in M7). A
    world whose package isn't on disk is simply omitted - the utilization
    block degrades to the worlds it can see rather than failing the audit."""
    import json as _json
    from engine.api.config import REPO_ROOT
    shelves: dict[str, dict] = {}
    for key, entry in registry.items():
        if not isinstance(entry, dict) or entry.get("kind") != "formation" or not entry.get("package"):
            continue
        repo_path = REPO_ROOT / entry["package"]["location"] / "compiled" / "repository.json"
        if not repo_path.exists():
            continue
        records = _json.loads(repo_path.read_text())["records"]
        by_type: dict[str, list[str]] = {}
        for r in records:
            if r.get("record_type") in _CITABLE_TYPES:
                by_type.setdefault(r["record_type"], []).append(r["id"])
        shelves[key] = {
            "citable_ids": [rid for ids in by_type.values() for rid in ids],
            "by_type": by_type,
        }
    return shelves


def _world_names(registry: dict) -> dict[str, list[str]]:
    """world_key -> that world's own names, for the register_frame
    self-reference detector. Read-only over the registry, same as
    everything else here."""
    names: dict[str, list[str]] = {}
    for key, entry in registry.items():
        if not isinstance(entry, dict):
            continue
        rep = entry.get("representative") or {}
        names[key] = [n for n in (rep.get("name"), entry.get("display_name"), entry.get("card_name")) if n]
    return names


def audit(events_db: str, out_dir: Path, since: str | None = None) -> dict:
    store = Store(events_db)
    registry = load_registry()
    names = _world_names(registry)
    shelves = _world_shelves(registry)
    session_ids = store.list_session_ids(since=since)
    audits = []
    for sid in session_ids:
        session = read_session(store, sid)
        if session is None:
            continue
        a = run_all(session, names)
        write_session_audit(out_dir, a)
        audits.append(a)
    rollup = build_rollup(audits, shelves)
    write_rollup(out_dir, rollup)
    write_digest(out_dir, rollup)
    write_canon_candidates(out_dir, audits)
    return rollup


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="python -m engine.m7.cli", description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    p = sub.add_parser("audit", help="run the phase-1 instrument suite over the event log")
    p.add_argument("--events-db", required=True, help="path to the M4 session-events SQLite file")
    p.add_argument("--out", required=True, help="output directory for the three report layers")
    p.add_argument("--since", default=None, help="ISO-8601 floor on event created_at (daily cadence)")
    args = parser.parse_args(argv)

    rollup = audit(args.events_db, Path(args.out), since=args.since)
    sev = rollup["findings_by_severity"]
    print(
        f"audited {rollup['sessions_audited']} session(s): "
        f"{sev.get('defect', 0)} defect / {sev.get('review', 0)} review / {sev.get('info', 0)} info"
    )
    print(f"reports in {args.out} (per-session + canon files are operator-only)")
    return 1 if sev.get("defect", 0) else 0


if __name__ == "__main__":
    sys.exit(main())
