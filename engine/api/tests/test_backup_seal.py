"""The accounts files are sealed before they leave the disk, and a sealed backup restores."""
import sqlite3
from pathlib import Path

import pytest

from engine.api import backup_seal, db_backup
from engine.api.backup_seal import BackupKeyError, BackupOpenError, BackupSealer

KEY = "k" * 40
OTHER = "o" * 40
MARK = b"SENTINEL-AN-ADDRESS-BLOB"


class FakeBucket:
    """Keeps the bytes at upload time, because the staging copy is removed straight after."""

    def __init__(self):
        self.objects: dict[str, bytes] = {}
        self.deleted: list[str] = []

    def upload_file(self, local_path, bucket, key):
        self.objects[key] = Path(local_path).read_bytes()

    def get_paginator(self, name):
        client = self

        class _P:
            def paginate(self, Bucket, Prefix):  # noqa: N803
                yield {"Contents": [{"Key": k} for k in client.objects if k.startswith(Prefix)]}

        return _P()

    def delete_object(self, Bucket, Key):  # noqa: N803
        self.deleted.append(Key)
        self.objects.pop(Key, None)

    def download_file(self, bucket, key, dest_path):
        Path(dest_path).write_bytes(self.objects[key])


def make_db(path: Path, value: bytes = MARK) -> None:
    conn = sqlite3.connect(str(path))
    conn.execute("CREATE TABLE t (id INTEGER PRIMARY KEY, val BLOB NOT NULL)")
    conn.execute("INSERT INTO t VALUES (1, ?)", (value,))
    conn.commit()
    conn.close()


def read_val(path: Path) -> bytes:
    conn = sqlite3.connect(str(path))
    try:
        return conn.execute("SELECT val FROM t WHERE id = 1").fetchone()[0]
    finally:
        conn.close()


@pytest.fixture
def bucket(monkeypatch):
    fake = FakeBucket()
    monkeypatch.setenv(db_backup._ENV_BUCKET, "test-bucket")
    monkeypatch.setattr(db_backup, "_client", lambda: fake)
    return fake


def run(tmp_path, sealer, labels=("accounts", "contact")):
    sources = {}
    for label in labels:
        src = tmp_path / f"{label}.db"
        make_db(src)
        sources[label] = str(src)
    events, usage = tmp_path / "events.db", tmp_path / "usage.db"
    make_db(events, b"e")
    make_db(usage, b"u")
    return db_backup.run_backup_once(str(events), str(usage), tmp_path / "staging", service_label="svc",
                                     sealed_dbs=sources, sealer=sealer)


def test_a_sealed_blob_opens_only_under_its_key_and_label():
    sealer = BackupSealer(KEY)
    blob = sealer.seal(b"hello", "accounts")
    assert sealer.open(blob, "accounts") == b"hello"
    with pytest.raises(BackupOpenError):
        sealer.open(blob, "contact")
    with pytest.raises(BackupOpenError):
        BackupSealer("z" * 40).open(blob, "accounts")
    with pytest.raises(BackupOpenError):
        sealer.open(blob[:-1] + bytes([blob[-1] ^ 1]), "accounts")
    with pytest.raises(BackupOpenError):
        sealer.open(b"plain sqlite bytes", "accounts")


def test_a_previous_key_still_opens_an_older_backup():
    old = BackupSealer(KEY, key_id="b1")
    blob = old.seal(b"older", "accounts")
    new = BackupSealer("n" * 40, key_id="b2", previous=[backup_seal.PreviousBackupKey("b1", KEY)])
    assert new.open(blob, "accounts") == b"older"
    assert new.seal(b"x", "accounts")[:8] != blob[:8]


@pytest.mark.parametrize("secret,kwargs", [
    ("short", {}), ("", {}), (KEY, {"other_secrets": (KEY,)}), (KEY, {"key_id": "B1"}), (KEY, {"key_id": "waytoolongid"}),
    (KEY, {"previous": [backup_seal.PreviousBackupKey("b1", KEY)], "key_id": "b2"}),
])
def test_an_unusable_key_is_refused(secret, kwargs):
    with pytest.raises(BackupKeyError):
        BackupSealer(secret, **kwargs)


def test_the_environment_builds_the_key_ring():
    sealer = backup_seal.from_env({"CIC_ACCOUNTS_BACKUP_KEY": KEY, "CIC_ACCOUNTS_BACKUP_KEY_ID": "b3",
                                   "CIC_ACCOUNTS_BACKUP_KEYS_PREVIOUS": f"b1:{OTHER}"})
    assert sealer.key_id == "b3"
    with pytest.raises(BackupKeyError):
        backup_seal.from_env({})


def test_only_sealed_copies_reach_the_bucket_and_they_hold_no_plain_bytes(tmp_path, bucket):
    status = run(tmp_path, BackupSealer(KEY))
    assert status["results"]["accounts"]["outcome"] == "ok" and status["results"]["contact"]["outcome"] == "ok"
    sealed = {k: v for k, v in bucket.objects.items() if "/accounts/" in k or "/contact/" in k}
    assert len(sealed) == 2 and all(k.endswith(".db.enc") for k in sealed)
    assert all(MARK not in v and not v.startswith(b"SQLite format 3") for v in sealed.values())
    assert list((tmp_path / "staging").glob("*.db*")) == []


def test_a_sealed_file_is_never_uploaded_without_a_key(tmp_path, bucket):
    status = run(tmp_path, None)
    assert status["results"]["accounts"]["outcome"] == "error"
    assert not any("/accounts/" in k or "/contact/" in k for k in bucket.objects)
    assert list((tmp_path / "staging").glob("*.db*")) == []


def test_without_a_bucket_nothing_is_sealed_or_left_behind(tmp_path, monkeypatch):
    monkeypatch.delenv(db_backup._ENV_BUCKET, raising=False)
    status = run(tmp_path, BackupSealer(KEY))
    assert status["results"]["accounts"]["outcome"] == "backed_up_not_uploaded"
    assert list((tmp_path / "staging").glob("*.db*")) == []


def test_an_absent_file_is_skipped(tmp_path, bucket):
    status = db_backup.run_backup_once(str(tmp_path / "e.db"), str(tmp_path / "u.db"), tmp_path / "staging",
                                       sealed_dbs={"accounts": str(tmp_path / "nope.db")}, sealer=BackupSealer(KEY))
    assert status["results"]["accounts"]["outcome"] == "skipped"


def test_the_old_sealed_backups_age_out_with_the_plain_ones(bucket):
    bucket.objects = {
        "db-backups/svc/accounts/2020-01-01T00-00-00Z.db.enc": b"x",
        "db-backups/svc/accounts/2099-01-01T00-00-00Z.db.enc": b"x",
        "db-backups/svc/accounts/not-a-stamp.db.enc": b"x",
    }
    assert db_backup.prune_remote("db-backups/svc/accounts/", keep_days=14) == ["db-backups/svc/accounts/2020-01-01T00-00-00Z.db.enc"]


def test_a_sealed_backup_restores_to_the_same_rows(tmp_path, bucket):
    sealer = BackupSealer(KEY)
    run(tmp_path, sealer)
    key = next(k for k in bucket.objects if "/accounts/" in k)
    downloaded = db_backup.download_sealed(key, tmp_path / "got.enc")
    target = tmp_path / "restored.db"
    make_db(target, b"damaged")
    db_backup.restore_sealed(downloaded, "accounts", sealer, target)
    assert read_val(target) == MARK
    assert not list(tmp_path.glob("*.opened"))


def test_a_restore_under_the_wrong_label_or_key_leaves_the_target_alone(tmp_path, bucket):
    sealer = BackupSealer(KEY)
    run(tmp_path, sealer)
    key = next(k for k in bucket.objects if "/accounts/" in k)
    downloaded = db_backup.download_sealed(key, tmp_path / "got.enc")
    target = tmp_path / "restored.db"
    make_db(target, b"keep me")
    with pytest.raises(BackupOpenError):
        db_backup.restore_sealed(downloaded, "contact", sealer, target)
    with pytest.raises(BackupOpenError):
        db_backup.restore_sealed(downloaded, "accounts", BackupSealer("w" * 40), target)
    assert read_val(target) == b"keep me"
    assert not list(tmp_path.glob("*.opened"))


def test_the_app_seals_the_durable_and_contact_files_and_never_the_ephemeral_one(tmp_path):
    from engine.accounts.config import AccountsConfig
    from engine.api.app import sealed_account_dbs

    config = AccountsConfig.from_env(str(tmp_path))
    assert sealed_account_dbs(config) == {"accounts": config.durable_db_path, "contact": config.contact_db_path}
    assert config.ephemeral_db_path not in sealed_account_dbs(config).values()
