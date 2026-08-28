"""The entrance contract (Artifact-3 SS2 catalog note: session_started is
"the ONLY writer of world/mode - a test fails on a second writer"; Artifact-5
SS4: "exactly one writer of session_started"). open_session() is the one
production call site in this codebase allowed to construct a
session_started event - enforced two ways: (1) at runtime, by refusing to
append a second one for the same session_id; (2) statically, by
engine/m4/tests/test_entrance_seal.py grepping the whole engine/ tree for
the "session_started" string literal and failing if it appears as a
constructed event_type anywhere outside this file - the same grep-guard
pattern engine/canon/check_seal_isolation.py already uses for a different
invariant.
"""
import re
from pathlib import Path

from . import events
from .store import Store

SESSION_STARTED_EVENT_TYPE = "session_started"

REPO_ROOT = Path(__file__).resolve().parents[2]
_AUTHORIZED_WRITER_FILE = "entrance.py"
# Matches a WRITE site - event_type="session_started" (single '=', keyword-
# argument shape) - never a read (event.event_type == "session_started",
# excluded because '==' fails the negative lookbehind) or a schema
# declaration (a dict key/tuple element, which has no '=' immediately
# before it at all). Precision matters here: a plain substring grep for
# "session_started" false-positived on events.py's schema table and
# projection.py's fold logic on the first real run - both legitimate
# readers, and a guard that flags legitimate code is exactly the
# "permanently-red guard everyone scrolls past" landmine (Build-Blueprint.md
# SS6).
_WRITE_PATTERN = re.compile(r'(?<![=!<>])=\s*["\']session_started["\']')


def find_second_writer_violations(engine_root: Path = REPO_ROOT / "engine") -> list[str]:
    """Static half of the entrance seal: grep the whole engine/ tree
    (production code only, not tests) for a session_started WRITE site
    outside this file. This is defense-in-depth on top of open_session()'s
    runtime refusal (the real guarantee) - a regex can't see a write
    through an imported constant, but the runtime check catches that
    regardless of which code path triggered it. Mirrors engine/canon/
    check_seal_isolation.py's guard pattern for a different invariant."""
    violations = []
    for path in sorted(engine_root.rglob("*.py")):
        if path.name == _AUTHORIZED_WRITER_FILE or "/tests/" in str(path):
            continue
        if _WRITE_PATTERN.search(path.read_text(encoding="utf-8")):
            violations.append(str(path.relative_to(REPO_ROOT)))
    return violations


class SecondWriterError(Exception):
    pass


def open_session(
    store: Store,
    *,
    session_id: str,
    event_uuid: str,
    mode: str,
    frame: str | None,
    code_hash: str,
    world_key: str | None = None,
    package_manifest_hash: str | None = None,
    world_keys: list[str] | None = None,
    package_manifest_hashes: dict[str, str] | None = None,
) -> int:
    """One sealed writer, two mode shapes (Artifact-7 SS1): an interview
    passes world_key/package_manifest_hash, a table passes world_keys/
    package_manifest_hashes. The payload carries only the caller's shape -
    Nones are never written - and events.validate() is what enforces that
    the shape matches the mode, so this function stays a writer, not a
    second validator."""
    existing = store.read_events(session_id)
    if any(e.event_type == SESSION_STARTED_EVENT_TYPE for e in existing):
        raise SecondWriterError(
            f"session {session_id} already has a {SESSION_STARTED_EVENT_TYPE} event - "
            "this is the only allowed writer of world/mode (Artifact-3 SS2)"
        )
    payload: dict = {"mode": mode, "frame": frame, "code_hash": code_hash}
    if world_key is not None:
        payload["world_key"] = world_key
    if package_manifest_hash is not None:
        payload["package_manifest_hash"] = package_manifest_hash
    if world_keys is not None:
        payload["world_keys"] = world_keys
    if package_manifest_hashes is not None:
        payload["package_manifest_hashes"] = package_manifest_hashes
    events.validate(SESSION_STARTED_EVENT_TYPE, payload)
    return store.append(
        session_id=session_id, event_uuid=event_uuid, event_type=SESSION_STARTED_EVENT_TYPE, payload=payload
    )
