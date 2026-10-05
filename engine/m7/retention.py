"""Daily retention (System Hub decision 34), run in-process inside the
cic-engine web service like the other daily jobs (engine/m7/scheduler.py's
module docstring says why it cannot be a separate Render service):
conversations inactive for 90 days are deleted from the event log, answer
text older than 90 days is deleted from the quality-control store, and M7
audit runs (operator copies of participant text) older than 90 days are
deleted.
Questions and scores in the QC store are kept. The 14-day backup rotation
(engine/api/db_backup.py) carries each deletion into the backups.

A conversation a signed-in person saved to their account is exempt from the
90 days (accounts change order, 2026-10-05). The engine never learns which
sessions those are or why: the edge passes `is_exempt`, a callable from
session id to bool, the way it passes a grant. The default exempts none.
"""
import json
import logging
import threading
import time
from collections.abc import Callable
from datetime import datetime, timedelta, timezone
from pathlib import Path

from engine.m4.store import Store
from engine.m7 import erase
from engine.m7.qc_store import QCStore
from engine.m7.scheduler import _next_run_at

logger = logging.getLogger("cic.api")

CONVERSATION_RETENTION_DAYS = 90
STATUS_FILENAME = "retention_last_run.json"
_HOUR, _MINUTE = 3, 41


def _none_exempt(_session_id: str) -> bool:
    return False


def run_once(events_db_path: str, qc_db_path: str, status_dir: Path, *, audit_root: Path | None = None,
             now: datetime | None = None, is_exempt: Callable[[str], bool] = _none_exempt) -> dict:
    """One retention pass; records its counts in status_dir. Never raises:
    a failed pass is logged and retried the next day."""
    now = now or datetime.now(timezone.utc)
    cutoff = (now - timedelta(days=CONVERSATION_RETENTION_DAYS)).isoformat()
    status = {"run_at": now.isoformat(), "conversation_cutoff": cutoff}
    try:
        status["conversations_deleted"] = Store(events_db_path).purge_inactive(cutoff, is_exempt)
        status["qc_answers_cleared"] = QCStore(qc_db_path).expire_answers(now.date())
        if audit_root is not None:
            status["audit_runs_pruned"] = erase.prune_older_than(audit_root, now.date(), CONVERSATION_RETENTION_DAYS)
        status["outcome"] = "ok"
    except Exception as exc:  # noqa: BLE001 - the loop must survive its own job failing
        logger.exception("retention run failed")
        status.update({"outcome": "error", "error": repr(exc)})
    status_dir.mkdir(parents=True, exist_ok=True)
    (status_dir / STATUS_FILENAME).write_text(json.dumps(status, indent=2))
    logger.info("retention run %s", json.dumps(status))
    return status


def start_background_scheduler(events_db_path: str, qc_db_path: str, status_dir: Path, audit_root: Path | None = None,
                               is_exempt: Callable[[str], bool] = _none_exempt) -> None:
    def _loop() -> None:
        while True:
            now = datetime.now(timezone.utc)
            next_run = _next_run_at(now, _HOUR, _MINUTE)
            time.sleep(max(0.0, (next_run - now).total_seconds()))
            run_once(events_db_path, qc_db_path, status_dir, audit_root=audit_root, is_exempt=is_exempt)

    threading.Thread(target=_loop, name="retention-daily", daemon=True).start()
