"""Daily M7 audit scheduler (engine/m7/scheduler.py): the timing math and
one real end-to-end run against a constructed event log, status file
included. Not covered here: the background thread itself actually firing
on a real clock - that's exercised by construction (a plain
threading.Thread sleeping a computed duration), not something worth a
slow or flaky test.
"""
import json
import uuid
from datetime import datetime, timezone

from engine.m4.store import Store
from engine.m7.scheduler import STATUS_FILENAME, _next_run_at, run_once


def _append(store, sid, etype, payload):
    store.append(session_id=sid, event_uuid=str(uuid.uuid4()), event_type=etype, payload=payload)


def test_next_run_at_today_if_not_yet_passed():
    now = datetime(2026, 9, 4, 1, 0, tzinfo=timezone.utc)
    assert _next_run_at(now, hour=3, minute=17) == datetime(2026, 9, 4, 3, 17, tzinfo=timezone.utc)


def test_next_run_at_tomorrow_if_already_passed():
    now = datetime(2026, 9, 4, 5, 0, tzinfo=timezone.utc)
    assert _next_run_at(now, hour=3, minute=17) == datetime(2026, 9, 5, 3, 17, tzinfo=timezone.utc)


def test_next_run_at_tomorrow_at_the_exact_instant():
    now = datetime(2026, 9, 4, 3, 17, tzinfo=timezone.utc)
    assert _next_run_at(now, hour=3, minute=17) == datetime(2026, 9, 5, 3, 17, tzinfo=timezone.utc)


def test_run_once_writes_a_status_file_and_reports_a_real_count(tmp_path):
    db_path = tmp_path / "events.db"
    store = Store(str(db_path))
    _append(store, "s1", "session_started", {
        "mode": "interview", "frame": "general_seeker", "code_hash": "abc",
        "world_key": "fix", "package_manifest_hash": "sha256:x",
    })

    out_root = tmp_path / "m7-audits"
    status = run_once(str(db_path), out_root)

    assert status["outcome"] == "ok"
    assert status["sessions_audited"] == 1

    on_disk = json.loads((out_root / STATUS_FILENAME).read_text())
    assert on_disk == status


def test_run_once_records_an_error_status_instead_of_raising(tmp_path):
    out_root = tmp_path / "m7-audits"
    # A nonexistent events DB: Store() would create it empty, so point
    # instead at something that can never be a valid sqlite file to force
    # a real failure inside audit() and prove the scheduler survives it.
    bad_db_path = str(tmp_path)  # a directory, not a file

    status = run_once(bad_db_path, out_root)

    assert status["outcome"] == "error"
    assert "error" in status
    on_disk = json.loads((out_root / STATUS_FILENAME).read_text())
    assert on_disk["outcome"] == "error"
