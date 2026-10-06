"""engine.api.db_backup - online backup/restore via sqlite3's own backup
API, and the object-storage half mocked (no live AWS/R2 call), matching
this repo's own convention for anything touching a real cloud credential
(engine/m8's usage tests, engine/m4/tests for object_storage)."""
import sqlite3
from pathlib import Path

import pytest

from engine.api import db_backup


def _make_db(path: Path, rows: list[tuple[int, str]]) -> None:
    conn = sqlite3.connect(str(path))
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("CREATE TABLE t (id INTEGER PRIMARY KEY, val TEXT NOT NULL)")
    conn.executemany("INSERT INTO t (id, val) VALUES (?, ?)", rows)
    conn.commit()
    conn.close()


def _read_rows(path: Path) -> list[tuple[int, str]]:
    conn = sqlite3.connect(str(path))
    rows = conn.execute("SELECT id, val FROM t ORDER BY id").fetchall()
    conn.close()
    return rows


def test_backup_one_is_row_for_row_identical(tmp_path):
    src = tmp_path / "source.db"
    _make_db(src, [(1, "a"), (2, "b"), (3, "c")])

    dest = db_backup.backup_one(src, tmp_path / "backup.db")

    assert _read_rows(dest) == [(1, "a"), (2, "b"), (3, "c")]


def test_backup_one_survives_a_live_wal_writer(tmp_path):
    """The whole reason this uses sqlite3's backup API instead of a file
    copy: a writer with uncommitted WAL pages must not produce a torn
    backup. Simulated here by holding a second connection open with an
    uncommitted write while the backup runs."""
    src = tmp_path / "source.db"
    _make_db(src, [(1, "a")])

    writer = sqlite3.connect(str(src))
    writer.execute("INSERT INTO t (id, val) VALUES (2, 'uncommitted')")
    # Deliberately not committed - a file-copy backup taken right now could
    # see a torn WAL; the backup API must not.

    dest = db_backup.backup_one(src, tmp_path / "backup.db")
    writer.rollback()
    writer.close()

    assert _read_rows(dest) == [(1, "a")]  # the committed state only


def test_verify_integrity_raises_on_a_corrupted_file(tmp_path):
    bad = tmp_path / "bad.db"
    bad.write_bytes(b"not a sqlite file at all, just garbage bytes" * 10)

    with pytest.raises(db_backup.BackupIntegrityError):
        db_backup.verify_integrity(bad)


def test_restore_one_replaces_target_and_cleans_stale_wal_files(tmp_path):
    src = tmp_path / "source.db"
    _make_db(src, [(1, "a"), (2, "b")])
    backup = db_backup.backup_one(src, tmp_path / "backup.db")

    target = tmp_path / "target.db"
    _make_db(target, [(99, "stale-data-to-be-overwritten")])
    stale_wal = Path(str(target) + "-wal")
    stale_wal.write_bytes(b"stale wal bytes")

    db_backup.restore_one(backup, target)

    assert _read_rows(target) == [(1, "a"), (2, "b")]
    assert not stale_wal.exists()


def test_restore_one_refuses_a_corrupted_backup(tmp_path):
    bad_backup = tmp_path / "bad-backup.db"
    bad_backup.write_bytes(b"garbage")
    target = tmp_path / "target.db"
    _make_db(target, [(1, "a")])

    with pytest.raises(db_backup.BackupIntegrityError):
        db_backup.restore_one(bad_backup, target)

    assert _read_rows(target) == [(1, "a")]  # untouched on refusal


def test_run_backup_once_without_bucket_configured_still_verifies_and_reports(tmp_path, monkeypatch):
    monkeypatch.delenv(db_backup._ENV_BUCKET, raising=False)
    events_db = tmp_path / "events.db"
    usage_db = tmp_path / "usage.db"
    _make_db(events_db, [(1, "e")])
    _make_db(usage_db, [(1, "u")])
    staging = tmp_path / "staging"

    status = db_backup.run_backup_once(str(events_db), str(usage_db), staging)

    assert status["results"]["events"]["outcome"] == "backed_up_not_uploaded"
    assert status["results"]["usage"]["outcome"] == "backed_up_not_uploaded"
    # Never left sitting on the same disk as the source DBs (module docstring).
    assert list(staging.glob("*.db")) == []
    assert (staging / db_backup.STATUS_FILENAME).exists()


def test_run_backup_once_reports_skipped_for_a_missing_source(tmp_path):
    staging = tmp_path / "staging"
    status = db_backup.run_backup_once(str(tmp_path / "nope-events.db"), str(tmp_path / "nope-usage.db"), staging)
    assert status["results"]["events"]["outcome"] == "skipped"
    assert status["results"]["usage"]["outcome"] == "skipped"


class _FakeS3Client:
    """Records calls in place of a real R2/boto3 client - no network call,
    matching this repo's own mocked-cloud-call test convention."""

    def __init__(self):
        self.uploaded: dict[str, str] = {}
        self.deleted: list[str] = []

    def upload_file(self, local_path, bucket, key):
        self.uploaded[key] = local_path

    def get_paginator(self, name):
        assert name == "list_objects_v2"
        client = self

        class _Paginator:
            def paginate(self, Bucket, Prefix):  # noqa: N803 - matches boto3's own kwarg casing
                keys = [k for k in client.uploaded if k.startswith(Prefix)]
                yield {"Contents": [{"Key": k} for k in keys]}

        return _Paginator()

    def delete_object(self, Bucket, Key):  # noqa: N803
        self.deleted.append(Key)
        self.uploaded.pop(Key, None)

    def download_file(self, bucket, key, dest_path):
        Path(dest_path).write_bytes(Path(self.uploaded[key]).read_bytes())


def test_run_backup_once_uploads_and_prunes_when_configured(tmp_path, monkeypatch):
    fake = _FakeS3Client()
    monkeypatch.setenv(db_backup._ENV_BUCKET, "test-bucket")
    monkeypatch.setenv(db_backup._ENV_ENDPOINT, "https://example.invalid")
    monkeypatch.setenv(db_backup._ENV_ACCESS_KEY, "key")
    monkeypatch.setenv(db_backup._ENV_SECRET_KEY, "secret")
    monkeypatch.setattr(db_backup, "_client", lambda: fake)

    events_db = tmp_path / "events.db"
    usage_db = tmp_path / "usage.db"
    _make_db(events_db, [(1, "e")])
    _make_db(usage_db, [(1, "u")])

    status = db_backup.run_backup_once(str(events_db), str(usage_db), tmp_path / "staging", service_label="test-svc")

    assert status["results"]["events"]["outcome"] == "ok"
    assert len(fake.uploaded) == 2
    assert all(k.startswith("db-backups/test-svc/") for k in fake.uploaded)


def test_prune_remote_keeps_recent_and_deletes_old(monkeypatch):
    fake = _FakeS3Client()
    fake.uploaded = {
        "db-backups/svc/events/2020-01-01T00-00-00Z.db": "/x",  # ancient
        "db-backups/svc/events/2099-01-01T00-00-00Z.db": "/x",  # far future, kept
        "db-backups/svc/events/not-a-timestamp.db": "/x",  # unrecognized, left alone
    }
    monkeypatch.setenv(db_backup._ENV_BUCKET, "test-bucket")
    monkeypatch.setattr(db_backup, "_client", lambda: fake)

    deleted = db_backup.prune_remote("db-backups/svc/events/", keep_days=1)

    assert deleted == ["db-backups/svc/events/2020-01-01T00-00-00Z.db"]
    assert "db-backups/svc/events/2099-01-01T00-00-00Z.db" in fake.uploaded
    assert "db-backups/svc/events/not-a-timestamp.db" in fake.uploaded


def test_next_run_at_picks_today_or_tomorrow():
    from datetime import datetime, timezone

    before = datetime(2026, 9, 21, 1, 0, tzinfo=timezone.utc)
    assert db_backup._next_run_at(before).date().isoformat() == "2026-09-21"

    after = datetime(2026, 9, 21, 23, 0, tzinfo=timezone.utc)
    assert db_backup._next_run_at(after).date().isoformat() == "2026-09-22"
