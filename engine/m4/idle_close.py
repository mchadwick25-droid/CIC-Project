"""Marks a session session_closed/reason="idle" after a period of no new
activity - built 2026-09-06, after the admin pilot-summary endpoint
(engine.api.wiring.get_pilot_summary) surfaced that every real pilot
session showed "open" forever: engine.m4.events' own schema had always
declared "idle" as a legal session_closed reason, but no code anywhere
ever wrote one.

Reporting-only by Mark's own call, not a hard stop like the turn/round
cap: a participant resuming a "closed" idle session with their session
code is never refused (engine.api.wiring.handle_message and
engine.api.table_wiring's own gates look past close_reason=="idle"
specifically), and engine.m4.projection's fold treats an idle close as
reversible - any real activity after one un-marks it, so a resumed
session reads as open again rather than sticking "idle" forever. Only a
cap or participant close is permanent; idle is the one reason that
isn't.

Run in-process inside the cic-engine web service (engine/api/app.py's
production app only), same placement reasoning as engine.m7.scheduler:
one Render Persistent Disk, one service attached to it, so a daily sweep
runs as a background thread here rather than a separate Cron Job service
that would need its own attachment of the same disk. Kept fully separate
from engine.m7.scheduler rather than folded into it - M7's own audit is
read-only over the event log by design ("a scheduled run can never
corrupt or affect a live conversation"); this module's whole job is to
write, so it never shares M7's guarantee or its code path.
"""
import logging
import threading
import time
import uuid
from datetime import datetime, timedelta, timezone

from . import events
from .projection import project_fresh
from .store import Store

logger = logging.getLogger("cic.api")

# Mark's call, 2026-09-06 (Ministry/Operations/Standing/
# CiC_Cross_System_Analysis_Tracking.md, "Pilot-summary endpoint confirmed
# live" entry): generous enough that a participant picking a conversation
# back up a few days later never finds their own session idle-closed.
IDLE_AFTER = timedelta(days=7)

# Arbitrary, low-traffic UTC hour, same reasoning as engine.m7.scheduler's
# own pick - offset from it (3:17) so the two daily sweeps don't land on
# the same instant.
_DEFAULT_HOUR = 4
_DEFAULT_MINUTE = 5


def _next_run_at(now: datetime, hour: int = _DEFAULT_HOUR, minute: int = _DEFAULT_MINUTE) -> datetime:
    """Next occurrence of hour:minute UTC - today if it hasn't passed yet,
    otherwise tomorrow. Pure function of `now` so this is testable without
    waiting on a real clock (identical shape to engine.m7.scheduler's own
    function of the same name - not imported from there, so this module's
    schedule can change independently of M7's)."""
    candidate = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
    if candidate <= now:
        candidate += timedelta(days=1)
    return candidate


def close_idle_sessions(store: Store, *, now: datetime | None = None, idle_after: timedelta = IDLE_AFTER) -> list[str]:
    """Appends session_closed/reason="idle" to every session whose last
    event predates `now - idle_after` and isn't already closed. Returns
    the session_ids closed, oldest-first (Store.list_session_ids' own
    order).

    Never touches a session that's already closed for any reason -
    re-closing an already-idle one would be a duplicate event carrying no
    new information, and a cap/participant close's permanence must never
    be second-guessed here."""
    now = now or datetime.now(timezone.utc)
    cutoff = now - idle_after
    closed_ids = []
    for session_id in store.list_session_ids():
        state = project_fresh(session_id, store)
        if not state.exists or state.closed or not state.raw_events:
            continue
        last_at = datetime.fromisoformat(state.raw_events[-1].created_at)
        if last_at >= cutoff:
            continue
        payload = {"reason": "idle"}
        events.validate("session_closed", payload)
        store.append(session_id=session_id, event_uuid=str(uuid.uuid4()), event_type="session_closed", payload=payload)
        closed_ids.append(session_id)
    return closed_ids


def start_background_scheduler(events_db_path: str) -> None:
    """Starts a daemon thread that runs the idle-close sweep once daily.
    Fire-and-forget, same as engine.m7.scheduler's own: the caller
    (engine/api/app.py's production app builder) does not wait on or
    manage this thread's lifecycle - it exits with the process, same as
    everything else in this single-instance service."""
    store = Store(events_db_path)

    def _loop() -> None:
        while True:
            now = datetime.now(timezone.utc)
            next_run = _next_run_at(now)
            time.sleep(max(0.0, (next_run - now).total_seconds()))
            try:
                closed = close_idle_sessions(store)
                if closed:
                    logger.info("idle-close sweep closed %d session(s)", len(closed))
            except Exception:  # noqa: BLE001 - the loop must survive its own job failing and try again tomorrow
                logger.exception("idle-close sweep failed")

    threading.Thread(target=_loop, name="m4-idle-close", daemon=True).start()
