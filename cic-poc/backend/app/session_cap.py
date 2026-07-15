"""
Per-tester ceiling on sessions started during the tester pilot - the real
budget backstop, scoped to each invited tester individually rather than one
shared pool. The pilot lead's own reasoning: a single shared pool lets
whichever tester happens to dive in first (or forwards the link widest)
burn the whole pilot's budget before anyone else gets a turn; a per-tester
cap (roughly 2 sessions each, deliberately more than 1 so a tester can
forward to exactly one other person if they want - itself a useful data
point on organic sharing) bounds each individual's worst case without
needing real user accounts, which this phase of the project doesn't need.

Each invited tester gets a short code (assigned by the pilot lead, embedded
in their personal invite link as a URL query param, e.g.
?code=tester1) - not their email itself, so no real PII needs to live in
this file. A tester_code registry (pilot_tester_codes.json) lists who's
authorized and their own cap; a separate counts file tracks usage per code.

Off by default: if the registry file doesn't exist, every session request
is allowed uncapped and code-free (normal dev/testing behavior) - this only
activates for a real pilot deployment that creates the registry file.
"""

import json
from pathlib import Path

REGISTRY_FILE = Path("./pilot_tester_codes.json")
COUNTS_FILE = Path("./pilot_session_counts.json")

DEFAULT_MAX_SESSIONS_PER_TESTER = 2


def pilot_mode_active() -> bool:
    """True once a real pilot deployment has created the tester-code registry."""
    return REGISTRY_FILE.exists()


def _load_registry() -> dict:
    try:
        return json.loads(REGISTRY_FILE.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def _load_counts() -> dict:
    try:
        return json.loads(COUNTS_FILE.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def check_and_reserve_session_slot(tester_code: str | None) -> tuple[bool, str]:
    """
    Returns (allowed, reason). If allowed, the slot has already been
    reserved (the per-code counter incremented) - callers should not call
    this twice for the same session.

    When pilot mode isn't active (no registry file), always allows,
    code-free - normal dev/testing is never gated by this.

    Simple read-modify-write on a plain JSON file, not database-backed or
    file-locked - accepted risk at this project's actual scale (a handful
    of testers, not real concurrent traffic).
    """
    if not pilot_mode_active():
        return True, ""

    if not tester_code:
        return False, "A tester code is required to start a session during this pilot."

    registry = _load_registry()
    if tester_code not in registry:
        return False, "That tester code isn't recognized for this pilot."

    max_sessions = registry[tester_code].get("max_sessions", DEFAULT_MAX_SESSIONS_PER_TESTER)
    counts = _load_counts()
    used = counts.get(tester_code, 0)

    if used >= max_sessions:
        return False, (
            "This tester code has reached its session limit for this pilot. "
            "Please reach out to the project team directly if you'd like to continue."
        )

    counts[tester_code] = used + 1
    COUNTS_FILE.write_text(json.dumps(counts, indent=2), encoding="utf-8")
    return True, ""
