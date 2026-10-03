"""Removing a conversation from the M7 audit files, and pruning old ones.

The daily audit writes operator-only copies of participant text under
<audit root>/<run stamp>/ (engine.m7.report): sessions/<session_id>.json,
plus a rollup, a digest and canon candidates that name the sessions they
were computed from. A deletion request (erase_session) removes that
session's file and every entry and mention of it from the shared files;
prune_older_than removes whole runs past the retention window, so audit
copies never outlive the conversations they were made from.
"""
import json
import shutil
from datetime import date, datetime, timedelta
from pathlib import Path

_STAMP_FORMAT = "%Y-%m-%dT%H-%M-%SZ"
_LINEAGE_PREFIX = "Computed from session_ids:"


def _scrub_digest_line(line: str, session_id: str) -> str:
    """The digest's lineage line keeps its other ids; every other line that
    names the session was already dropped by the caller."""
    if not line.startswith(_LINEAGE_PREFIX):
        return line
    ids = [s.strip() for s in line[len(_LINEAGE_PREFIX):].split(",") if s.strip() and s.strip() != session_id]
    return f"{_LINEAGE_PREFIX} {', '.join(ids) or 'none'}"


def _run_dirs(audit_root: Path) -> list[Path]:
    if not audit_root.is_dir():
        return []
    runs = []
    for d in audit_root.iterdir():
        try:
            datetime.strptime(d.name, _STAMP_FORMAT)
        except ValueError:
            continue
        if d.is_dir():
            runs.append(d)
    return sorted(runs)


def _rewrite_json(path: Path, session_id: str) -> bool:
    doc = json.loads(path.read_text())
    before = json.dumps(doc, sort_keys=True)
    if "lineage_session_ids" in doc:
        doc["lineage_session_ids"] = [s for s in doc["lineage_session_ids"] if s != session_id]
    for key in ("findings", "sessions"):
        if isinstance(doc.get(key), list):
            doc[key] = [x for x in doc[key] if not (isinstance(x, dict) and x.get("session_id") == session_id)]
    if isinstance(doc.get("candidates"), list):
        kept = []
        for c in doc["candidates"]:
            ids = [s for s in c.get("session_ids", []) if s != session_id]
            if ids:
                kept.append({**c, "session_ids": ids})
        doc["candidates"] = kept
    if json.dumps(doc, sort_keys=True) == before:
        return False
    path.write_text(json.dumps(doc, indent=2, sort_keys=False) + "\n")
    return True


def erase_session(audit_root: Path, session_id: str) -> int:
    """Remove every trace of session_id from every audit run. Returns the
    number of files deleted or rewritten."""
    touched = 0
    for run in _run_dirs(audit_root):
        own = run / "sessions" / f"{session_id}.json"
        if own.exists():
            own.unlink()
            touched += 1
        for path in run.glob("*.json"):
            if _rewrite_json(path, session_id):
                touched += 1
        for path in run.glob("*.md"):
            text = path.read_text()
            if session_id in text:
                path.write_text("\n".join(_scrub_digest_line(line, session_id) for line in text.split("\n")
                                          if session_id not in line or line.startswith(_LINEAGE_PREFIX)))
                touched += 1
    return touched


def prune_older_than(audit_root: Path, today: date, days: int) -> int:
    """Delete every audit run whose stamp is more than `days` days old.
    Returns the number of runs deleted."""
    cutoff = today - timedelta(days=days)
    pruned = 0
    for run in _run_dirs(audit_root):
        if datetime.strptime(run.name, _STAMP_FORMAT).date() < cutoff:
            shutil.rmtree(run)
            pruned += 1
    return pruned
