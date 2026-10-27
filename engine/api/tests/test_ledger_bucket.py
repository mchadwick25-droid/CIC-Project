"""A deletion is written outside the disk at once, and a file restored from before it loses the account again."""
import sqlite3
import time
from datetime import date, timedelta
from pathlib import Path

import pytest

from engine.accounts.service import AccountsService, ledger_hash
from engine.accounts.store import AccountStore
from engine.accounts.tests.conftest import ADDRESS_KEY, SESSION_KEY, Clock, FakeMailer, delete_now, stepped_up_session
from engine.accounts.keys import KeyRing
from engine.api import db_backup, ledger_bucket
from engine.api.backup_seal import BackupSealer


class FakeBucket:
    def __init__(self):
        self.objects: dict[str, bytes] = {}
        self.refuse = False

    def put_object(self, Bucket, Key, Body):  # noqa: N803
        if self.refuse:
            raise RuntimeError("bucket down for someone@example.org")
        self.objects[Key] = Body

    def get_paginator(self, name):
        client = self

        class _P:
            def paginate(self, Bucket, Prefix):  # noqa: N803
                yield {"Contents": [{"Key": k} for k in client.objects if k.startswith(Prefix)]}

        return _P()

    def delete_object(self, Bucket, Key):  # noqa: N803
        self.objects.pop(Key, None)

    def get_object(self, Bucket, Key):  # noqa: N803
        body = self.objects[Key]

        class _Body:
            def read(self_inner):
                return body

        return {"Body": _Body()}


@pytest.fixture
def bucket(monkeypatch):
    fake = FakeBucket()
    monkeypatch.setenv(db_backup._ENV_BUCKET, "test-bucket")
    monkeypatch.setattr(db_backup, "_client", lambda **kw: fake)
    return fake


SEALER = BackupSealer("s" * 40)


def make_service(tmp_path, name="a", clock=None, publish=True):
    store = AccountStore(str(tmp_path / f"{name}-d.db"), str(tmp_path / f"{name}-e.db"))
    svc = AccountsService(
        store, KeyRing(ADDRESS_KEY, SESSION_KEY), FakeMailer(), clock=clock or Clock(time.time()),
        ledger_publisher=ledger_bucket.publish if publish else None, ledger_source=ledger_bucket.entries if publish else None,
        erasure_publisher=(lambda h, t, e: ledger_bucket.publish_erasure(SEALER, h, t, e)) if publish else None,
        erasure_source=(lambda: ledger_bucket.erasures(SEALER)) if publish else None,
        closure_publisher=ledger_bucket.publish_closure if publish else None,
        closure_remover=ledger_bucket.remove_closure if publish else None,
        closure_source=ledger_bucket.closures if publish else None,
    )
    return svc, store


def entry_names(bucket, kind="ledger"):
    return [k.rsplit("/", 1)[1] for k in bucket.objects if f"/{kind}/" in k]


def test_a_deletion_is_written_outside_the_disk_as_a_hash_and_a_day_only(tmp_path, bucket):
    clock = Clock(time.time())
    svc, store = make_service(tmp_path, clock=clock)
    session, cookie = stepped_up_session(svc, svc.mailer, clock)
    account_id = svc.session(cookie).account_id
    assert delete_now(svc, clock, svc.session(cookie)).status == "ok"
    expires = (svc.today() + timedelta(days=16)).isoformat()
    assert entry_names(bucket) == [f"{expires}_{ledger_hash(account_id)}"]
    assert all(body == b"" for body in bucket.objects.values())
    assert store.unpublished_ledger() == []
    store.close()


def test_a_bucket_that_is_down_does_not_fail_the_deletion_and_the_entry_is_sent_later(tmp_path, bucket, caplog):
    clock = Clock(time.time())
    svc, store = make_service(tmp_path, clock=clock)
    session, cookie = stepped_up_session(svc, svc.mailer, clock)
    bucket.refuse = True
    assert delete_now(svc, clock, svc.session(cookie)).status == "ok"
    assert len(store.unpublished_ledger()) == 1 and bucket.objects == {}
    assert "someone@example.org" not in caplog.text
    bucket.refuse = False
    assert svc.publish_ledger() == 1
    assert len(bucket.objects) == 1 and store.unpublished_ledger() == []
    store.close()


def test_with_no_bucket_the_entry_waits_and_nothing_fails(tmp_path, monkeypatch):
    monkeypatch.delenv(db_backup._ENV_BUCKET, raising=False)
    clock = Clock(time.time())
    svc, store = make_service(tmp_path, clock=clock)
    session, cookie = stepped_up_session(svc, svc.mailer, clock)
    assert delete_now(svc, clock, svc.session(cookie)).status == "ok"
    assert len(store.unpublished_ledger()) == 1
    store.close()


def test_a_file_restored_from_before_a_deletion_loses_that_account_again(tmp_path, bucket):
    clock = Clock(time.time())
    svc, store = make_service(tmp_path, clock=clock)
    session, cookie = stepped_up_session(svc, svc.mailer, clock)
    account = store.account(svc.session(cookie).account_id)
    backup = tmp_path / "backup.db"
    db_backup.backup_one(tmp_path / "a-d.db", backup)  # last night's backup, taken before the deletion
    delete_now(svc, clock, svc.session(cookie))
    store.close()

    db_backup.restore_one(backup, tmp_path / "a-d.db")  # the disk is lost; last night's file is put back
    restored, restored_store = make_service(tmp_path, clock=clock)
    assert restored_store.account(account.account_id) is not None
    assert restored_store.unpublished_ledger() == []
    assert restored.sync_ledger() == 1
    assert restored_store.account(account.account_id) is None
    restored_store.close()


def test_a_restore_with_the_bucket_unreachable_still_applies_the_files_own_ledger(tmp_path, bucket):
    clock = Clock(time.time())
    svc, store = make_service(tmp_path, clock=clock)
    session, cookie = stepped_up_session(svc, svc.mailer, clock)
    account = store.account(svc.session(cookie).account_id)
    delete_now(svc, clock, svc.session(cookie))
    store.create_account(account)  # a restore that kept the ledger
    bucket.get_paginator = lambda name: (_ for _ in ()).throw(RuntimeError("down"))
    assert svc.sync_ledger() == 1
    assert store.account(account.account_id) is None
    store.close()


def test_entries_past_their_day_are_ignored_and_pruned_and_foreign_names_are_left_alone(bucket):
    today = date.today()
    old = (today - timedelta(days=2)).isoformat()
    new = (today + timedelta(days=5)).isoformat()
    h = "a" * 64
    bucket.objects = {
        f"db-backups/cic-engine/ledger/{old}_{h}": b"",
        f"db-backups/cic-engine/ledger/{new}_{h}": b"",
        "db-backups/cic-engine/ledger/readme.txt": b"",
    }
    assert ledger_bucket.entries() == [(h, new)]
    assert ledger_bucket.prune() == [f"db-backups/cic-engine/ledger/{old}_{h}"]
    assert set(bucket.objects) == {f"db-backups/cic-engine/ledger/{new}_{h}", "db-backups/cic-engine/ledger/readme.txt"}


def test_an_older_file_without_the_published_column_is_opened_and_its_entries_are_sent(tmp_path, bucket):
    path = tmp_path / "old-d.db"
    conn = sqlite3.connect(str(path))
    conn.executescript("CREATE TABLE deletion_ledger (ledger_hash TEXT PRIMARY KEY, expires_on TEXT NOT NULL) WITHOUT ROWID;")
    conn.execute("INSERT INTO deletion_ledger VALUES (?, ?)", ("b" * 64, (date.today() + timedelta(days=3)).isoformat()))
    conn.commit()
    conn.close()
    store = AccountStore(str(path), str(tmp_path / "old-e.db"))
    assert store.unpublished_ledger() == [("b" * 64, (date.today() + timedelta(days=3)).isoformat())]
    store.close()


def erased_names(bucket):
    return [k for k in bucket.objects if "/erased/" in k]


def test_an_erasure_is_written_outside_the_disk_sealed_and_named_without_the_conversation(tmp_path, bucket):
    svc, store = make_service(tmp_path)
    svc.note_erased("session-abc", ("tok1", "tok2"))
    (key,) = erased_names(bucket)
    body = bucket.objects[key]
    assert b"session-abc" not in body and b"tok1" not in body and b"session-abc" not in key.encode()
    assert SEALER.open(body, "erased")
    assert store.unpublished_erasures() == []
    store.close()


def test_a_file_restored_from_before_an_erasure_finds_the_erased_conversation_again(tmp_path, bucket):
    clock = Clock(time.time())
    svc, store = make_service(tmp_path, clock=clock)
    backup = tmp_path / "backup.db"
    db_backup.backup_one(tmp_path / "a-d.db", backup)  # last night's file, before the erasure
    svc.note_erased("session-abc", ("tok1",))
    store.close()

    db_backup.restore_one(backup, tmp_path / "a-d.db")
    restored, restored_store = make_service(tmp_path, clock=clock)
    assert restored.erased_matches(["session-abc"]) == []
    assert restored.sync_erasures() == 1
    assert restored.erased_matches(["session-abc", "other"]) == [("session-abc", ("tok1",))]
    restored_store.close()


def test_an_erasure_gaining_review_tokens_is_sent_again_with_all_of_them(tmp_path, bucket):
    svc, store = make_service(tmp_path)
    svc.note_erased("session-abc", ("tok1",))
    svc.note_erased("session-abc", ("tok2",))
    (key,) = erased_names(bucket)
    import json
    assert set(json.loads(SEALER.open(bucket.objects[key], "erased"))["t"].split(",")) == {"tok1", "tok2"}
    store.close()


def test_a_bucket_that_is_down_does_not_fail_an_erasure_and_it_is_sent_later(tmp_path, bucket):
    svc, store = make_service(tmp_path)
    bucket.refuse = True
    svc.note_erased("session-abc", ("tok1",))
    assert len(store.unpublished_erasures()) == 1
    bucket.refuse = False
    assert svc.publish_erasures() == 1 and store.unpublished_erasures() == []
    store.close()


def test_an_unreadable_erasure_entry_does_not_hide_the_others(tmp_path, bucket):
    svc, store = make_service(tmp_path)
    svc.note_erased("session-one", ("t1",))
    day = (date.today() + timedelta(days=3)).isoformat()
    bucket.objects[f"db-backups/cic-engine/erased/{day}_{'c' * 64}"] = b"not sealed"
    found = ledger_bucket.erasures(SEALER)
    assert len(found) == 1 and found[0][1] == "t1"
    store.close()


def test_expired_erasure_entries_are_pruned_with_the_deletion_ones(bucket):
    old = (date.today() - timedelta(days=2)).isoformat()
    new = (date.today() + timedelta(days=5)).isoformat()
    bucket.objects = {
        f"db-backups/cic-engine/erased/{old}_{'d' * 64}": b"x",
        f"db-backups/cic-engine/erased/{new}_{'d' * 64}": b"x",
        f"db-backups/cic-engine/ledger/{old}_{'e' * 64}": b"",
    }
    assert sorted(ledger_bucket.prune()) == sorted([f"db-backups/cic-engine/erased/{old}_{'d' * 64}", f"db-backups/cic-engine/ledger/{old}_{'e' * 64}"])
    assert list(bucket.objects) == [f"db-backups/cic-engine/erased/{new}_{'d' * 64}"]


def test_an_older_file_without_the_published_column_on_its_erasures_is_opened(tmp_path):
    path = tmp_path / "old-d.db"
    conn = sqlite3.connect(str(path))
    conn.executescript("CREATE TABLE erased_sessions (session_hash TEXT PRIMARY KEY, qc_tokens TEXT NOT NULL, expires_on TEXT NOT NULL) WITHOUT ROWID;")
    later = (date.today() + timedelta(days=30)).isoformat()
    conn.execute("INSERT INTO erased_sessions VALUES ('h', 't', ?)", (later,))
    conn.commit()
    conn.close()
    store = AccountStore(str(path), str(tmp_path / "old-e.db"))
    assert store.unpublished_erasures() == [("h", "t", later)]
    store.close()
