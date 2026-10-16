"""live_watch.problems: what the scheduled check calls a failure."""
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import live_watch

NOW = datetime(2026, 10, 15, 12, 0, tzinfo=timezone.utc)
HEAD = "a" * 40
OLD_HEAD_AT = NOW - timedelta(hours=2)
GOOD_BACKUP = {"uploaded": True, "last_run_at": "2026-10-15T04:41:00+00:00"}


def _health(commit=HEAD, backup=GOOD_BACKUP):
    return {"status": "ok", "commit": commit, "backup": backup}


def test_all_clear():
    assert live_watch.problems(_health(), HEAD, OLD_HEAD_AT, NOW) == []


def test_no_answer_is_one_problem():
    assert len(live_watch.problems(None, HEAD, OLD_HEAD_AT, NOW)) == 1


def test_an_old_build_still_serving_is_caught():
    found = live_watch.problems(_health(commit="b" * 40), HEAD, OLD_HEAD_AT, NOW)
    assert len(found) == 1 and "has not gone live" in found[0]


def test_a_deploy_still_in_progress_is_not_an_alarm():
    assert live_watch.problems(_health(commit="b" * 40), HEAD, NOW - timedelta(minutes=10), NOW) == []


def test_an_unreported_commit_is_caught():
    assert "RENDER_GIT_COMMIT" in live_watch.problems(_health(commit="unknown"), HEAD, OLD_HEAD_AT, NOW)[0]


def test_a_backup_that_did_not_upload_is_caught():
    found = live_watch.problems(_health(backup={**GOOD_BACKUP, "uploaded": False}), HEAD, OLD_HEAD_AT, NOW)
    assert len(found) == 1 and "CIC_API_BACKUP_BUCKET" in found[0]


def test_a_stale_backup_is_caught():
    stale = {"uploaded": True, "last_run_at": "2026-10-13T04:41:00+00:00"}
    found = live_watch.problems(_health(backup=stale), HEAD, OLD_HEAD_AT, NOW)
    assert len(found) == 1 and "more than a day ago" in found[0]


def test_no_backup_yet_is_caught():
    found = live_watch.problems(_health(backup={"uploaded": False, "last_run_at": None}), HEAD, OLD_HEAD_AT, NOW)
    assert found == ["No database backup has run yet."]


def test_an_engine_without_a_backup_line_is_caught():
    assert live_watch.problems(_health(backup=None), HEAD, OLD_HEAD_AT, NOW) == ["The engine does not report a backup result."]
