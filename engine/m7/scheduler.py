"""Daily M7 audit scheduler, run in-process inside the cic-engine web
service (engine/api/app.py's production app only) rather than as a
separate Render service: Render mounts a Persistent Disk to exactly one
running service, and cic-engine already has /data mounted there - a
separate Cron Job service would need its own attachment of that same
disk, which Render does not support once it's already attached. See
Build/Ministry/Operations/Standing/CiC_System_Health_Tracking.md, 2026-09-04,
for the fuller reasoning and the standing duty this closes.

Read-only over the event log (engine.m7.cli.audit's own guarantee, see
its docstring) - a scheduled run can never corrupt or affect a live
conversation. Worst case of anything going wrong here is a missed or
delayed audit, never a broken session.
"""
import json
import logging
import threading
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

from engine.m7.cli import audit

logger = logging.getLogger("cic.api")

# Arbitrary, not a real constraint - picked as a plausible low-traffic UTC
# hour, off the round number so this wouldn't pile up against anything
# else in the fleet that might wake at a clean :00. Change freely.
_DEFAULT_HOUR = 3
_DEFAULT_MINUTE = 17

STATUS_FILENAME = "last_run.json"


def _next_run_at(now: datetime, hour: int = _DEFAULT_HOUR, minute: int = _DEFAULT_MINUTE) -> datetime:
    """Next occurrence of hour:minute UTC - today if it hasn't passed yet,
    otherwise tomorrow. Pure function of `now` so this is testable without
    waiting on a real clock."""
    candidate = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
    if candidate <= now:
        candidate += timedelta(days=1)
    return candidate


def run_once(events_db_path: str, out_root: Path, *, since: str | None = None) -> dict:
    """Run one audit pass and record its outcome in out_root/last_run.json.
    Never raises: a failed audit becomes a status entry, not a crashed
    service - the scheduler loop calling this must survive a bad run and
    try again tomorrow.

    `since` defaults to yesterday's UTC date, matching the CLI's own
    documented daily-cadence convention (engine/m7/cli.py's module
    docstring: "Daily cadence = yesterday's --since")."""
    out_root.mkdir(parents=True, exist_ok=True)
    run_at = datetime.now(timezone.utc)
    if since is None:
        since = (run_at - timedelta(days=1)).date().isoformat()
    out_dir = out_root / run_at.strftime("%Y-%m-%dT%H-%M-%SZ")
    status = {"run_at": run_at.isoformat(), "since": since, "out_dir": str(out_dir)}
    try:
        rollup = audit(events_db_path, out_dir, since=since)
        sev = rollup.get("findings_by_severity", {})
        status.update({
            "outcome": "ok",
            "sessions_audited": rollup.get("sessions_audited", 0),
            "defect": sev.get("defect", 0),
            "review": sev.get("review", 0),
            "info": sev.get("info", 0),
        })
    except Exception as exc:  # noqa: BLE001 - the loop must survive its own job failing
        logger.exception("M7 scheduled audit run failed")
        status.update({"outcome": "error", "error": repr(exc)})
    (out_root / STATUS_FILENAME).write_text(json.dumps(status, indent=2))
    return status


def start_background_scheduler(events_db_path: str, out_root: Path) -> None:
    """Starts a daemon thread that runs the M7 audit once daily. Fire-and-
    forget: the caller (engine/api/app.py's production app builder) does
    not wait on or manage this thread's lifecycle - it exits with the
    process, same as everything else in this single-instance service
    (render.yaml: no --workers flag, one uvicorn process, the SQLite
    store already requires this)."""

    def _loop() -> None:
        while True:
            now = datetime.now(timezone.utc)
            next_run = _next_run_at(now)
            time.sleep(max(0.0, (next_run - now).total_seconds()))
            run_once(events_db_path, out_root)

    threading.Thread(target=_loop, name="m7-daily-audit", daemon=True).start()
