"""Online backup, restore, and a daily in-process schedule for the two
SQLite stores on cic-engine's Render Disk (engine.m4.store.Store's
events DB, engine.m8.log_store.UsageLogStore's usage DB).

Ministry/Operations/Standing/CiC_Backup_Restore_Runbook.md is the
procedure this module implements; read that first for RPO/RTO and the
one-time R2 bucket setup.

Why in-process, not a Render Cron Job (verified, not assumed): Render
mounts a Persistent Disk to exactly one running service, and a Cron Job
or one-off Job runs on separate compute that cannot reach that disk
(https://render.com/docs/disks - "You can't access a service's disk from
a one-off job you run for the service"). engine/m7/scheduler.py and
engine/m4/idle_close.py already hit this exact constraint and both
resolved it the same way: a daemon thread inside cic-engine's own
process. This module is a third sibling of that same pattern, not a new
one - see start_background_scheduler below.

Why online backup, not a file copy: engine.m4.store.Store and
engine.m8.log_store.UsageLogStore both open their SQLite connection with
`PRAGMA journal_mode=WAL`. Copying the .db file with the service running
can copy it mid-write, or without its -wal/-shm siblings, and produce a
file that looks complete but is silently torn. sqlite3.Connection.backup()
(the "online backup API") is safe against a live writer by design - it is
the mechanism this module uses, exclusively.

Why a separate object-storage bucket from CIC_API_PACKAGE_BUCKET
(engine/m4/object_storage.py): that bucket holds compiled world packages,
which are public-ish derived build output. These backups hold real
participant session transcripts (events.db) and cost/usage records
(usage.db) - a different data-sensitivity class that should not share a
credential with anything engine/m4/package_fetch.py reads at runtime.
Deliberately not added to engine.api.config.Settings, for the same reason
object_storage.py's own credentials aren't: one place to drift, not two
(config.py's own comment on package_cache_dir vs. package bucket vars).
"""
from __future__ import annotations

import json
import logging
import os
import shutil
import sqlite3
import sys
import threading
import time
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path

logger = logging.getLogger("cic.api")

STATUS_FILENAME = "last_run.json"

# Off M7's 03:17 and idle_close's own hour so the three daily threads don't
# pile up against each other on a single-instance service. Arbitrary,
# same as M7's own comment on this - change freely.
_DEFAULT_HOUR = 4
_DEFAULT_MINUTE = 41

# Independent of CIC_API_PACKAGE_BUCKET* on purpose - see module docstring.
_ENV_BUCKET = "CIC_API_BACKUP_BUCKET"
_ENV_ENDPOINT = "CIC_API_BACKUP_BUCKET_ENDPOINT"
_ENV_ACCESS_KEY = "CIC_API_BACKUP_BUCKET_ACCESS_KEY_ID"
_ENV_SECRET_KEY = "CIC_API_BACKUP_BUCKET_SECRET_ACCESS_KEY"

# Daily backups kept online per DB - RPO/RTO reasoning in the Backup &
# Restore Runbook. Prunes both the local staging copy (never kept - see
# run_backup_once) and the remote bucket's own history.
_DEFAULT_RETENTION_DAYS = 14


class BackupStorageError(Exception):
    """A configured backup bucket refused a request, or credentials are
    incomplete - never silently swallowed, same discipline as
    engine.m4.object_storage.ObjectStorageError."""


class BackupIntegrityError(Exception):
    """A backup or a restore candidate failed PRAGMA integrity_check -
    never trusted, never uploaded, never restored over a live DB."""


@dataclass(frozen=True)
class BackupResult:
    db_label: str
    source_path: str
    object_key: str | None
    bytes_written: int
    verified: bool


def is_configured() -> bool:
    return bool(os.environ.get(_ENV_BUCKET))


def _client():
    endpoint = os.environ.get(_ENV_ENDPOINT)
    if not endpoint:
        raise BackupStorageError(
            f"{_ENV_BUCKET} is set but {_ENV_ENDPOINT} is not - R2's account "
            "endpoint has no default to guess."
        )
    access_key = os.environ.get(_ENV_ACCESS_KEY)
    secret_key = os.environ.get(_ENV_SECRET_KEY)
    if not access_key or not secret_key:
        raise BackupStorageError(
            f"{_ENV_BUCKET} is set but its own access key/secret are not - "
            "backup credentials are never read from AWS's own chain or from "
            "CIC_API_PACKAGE_BUCKET*'s credentials (module docstring)."
        )
    import boto3  # local import: keeps this module importable in a boto3-less unit test env

    return boto3.client(
        "s3",
        endpoint_url=endpoint,
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name="auto",
    )


def verify_integrity(db_path: str | Path) -> None:
    """Raises BackupIntegrityError unless PRAGMA integrity_check returns
    exactly ["ok"]. Run against every backup before it is trusted enough to
    upload, and against every restore candidate before it is trusted enough
    to replace a live DB."""
    conn = sqlite3.connect(str(db_path))
    try:
        try:
            rows = conn.execute("PRAGMA integrity_check").fetchall()
        except sqlite3.DatabaseError as exc:
            # Not a SQLite file at all (e.g. truncated download, wrong
            # object entirely) - PRAGMA integrity_check itself raises here
            # rather than returning a row, so this is folded into the same
            # BackupIntegrityError a failing check would raise.
            raise BackupIntegrityError(f"{db_path}: {exc}") from exc
    finally:
        conn.close()
    values = [r[0] for r in rows]
    if values != ["ok"]:
        raise BackupIntegrityError(f"{db_path}: integrity_check returned {values!r}, not ['ok']")


def backup_one(db_path: str | Path, dest_path: str | Path) -> Path:
    """Online backup of db_path to dest_path via sqlite3's own backup API
    (never a file copy - module docstring). Verifies the result before
    returning it; a corrupt backup is never handed back as if it were
    good."""
    db_path = Path(db_path)
    dest_path = Path(dest_path)
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    if dest_path.exists():
        dest_path.unlink()

    # mode=ro: the backup reads a live, possibly-mid-write database without
    # taking a write lock or ever being the thing that blocks a participant
    # turn from committing.
    source = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    dest = sqlite3.connect(str(dest_path))
    try:
        source.backup(dest)
    finally:
        dest.close()
        source.close()

    verify_integrity(dest_path)
    return dest_path


def upload_backup(local_path: str | Path, object_key: str) -> str:
    client = _client()
    bucket = os.environ[_ENV_BUCKET]
    try:
        client.upload_file(str(local_path), bucket, object_key)
    except Exception as e:  # noqa: BLE001 - re-raised as this module's own error, never swallowed
        raise BackupStorageError(f"upload of {local_path} to {bucket}/{object_key} failed: {e}") from e
    return object_key


def list_backups(prefix: str) -> list[str]:
    client = _client()
    bucket = os.environ[_ENV_BUCKET]
    keys: list[str] = []
    paginator = client.get_paginator("list_objects_v2")
    for page in paginator.paginate(Bucket=bucket, Prefix=prefix):
        for obj in page.get("Contents", []):
            keys.append(obj["Key"])
    return sorted(keys)


def prune_remote(prefix: str, *, keep_days: int = _DEFAULT_RETENTION_DAYS) -> list[str]:
    """Deletes objects under prefix whose own embedded UTC timestamp (the
    filename this module writes, YYYY-MM-DDTHH-MM-SSZ.db) is older than
    keep_days. Never deletes an object whose name this module doesn't
    recognize - an unrecognized key is left alone, not swept."""
    client = _client()
    bucket = os.environ[_ENV_BUCKET]
    cutoff = datetime.now(timezone.utc) - timedelta(days=keep_days)
    deleted = []
    for key in list_backups(prefix):
        stem = Path(key).stem  # "2026-09-21T04-41-00Z"
        try:
            ts = datetime.strptime(stem, "%Y-%m-%dT%H-%M-%SZ").replace(tzinfo=timezone.utc)
        except ValueError:
            continue  # not one of ours - leave it
        if ts < cutoff:
            client.delete_object(Bucket=bucket, Key=key)
            deleted.append(key)
    return deleted


def download_backup(object_key: str, dest_path: str | Path) -> Path:
    client = _client()
    bucket = os.environ[_ENV_BUCKET]
    dest_path = Path(dest_path)
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        client.download_file(bucket, object_key, str(dest_path))
    except Exception as e:  # noqa: BLE001
        raise BackupStorageError(f"download of {bucket}/{object_key} failed: {e}") from e
    verify_integrity(dest_path)
    return dest_path


def restore_one(backup_path: str | Path, target_db_path: str | Path) -> None:
    """Replaces target_db_path with backup_path, atomically, only after
    verifying backup_path's own integrity. This is a maintenance action:
    the runbook requires the writer (cic-engine) stopped or the disk
    detached first - this function does not itself stop anything, and
    swapping a WAL-mode DB's main file while a writer holds it open would
    not be atomic from that writer's point of view. Deletes any stale
    -wal/-shm siblings of the target so a restored file doesn't get
    replayed against an old, unrelated WAL."""
    backup_path = Path(backup_path)
    target_db_path = Path(target_db_path)
    verify_integrity(backup_path)  # never restore an unverified file, even a locally-built one

    tmp_path = target_db_path.with_suffix(target_db_path.suffix + ".restoring")
    shutil.copyfile(backup_path, tmp_path)
    verify_integrity(tmp_path)  # catches a truncated copy, not just a truncated source

    for suffix in ("-wal", "-shm"):
        stale = Path(str(target_db_path) + suffix)
        if stale.exists():
            stale.unlink()

    os.replace(tmp_path, target_db_path)  # atomic on the same filesystem


def run_backup_once(
    events_db_path: str,
    usage_db_path: str,
    staging_dir: Path,
    *,
    service_label: str = "cic-engine",
    qc_db_path: str | None = None,
) -> dict:
    """One backup pass over both DBs. Never raises: a failed pass becomes a
    status entry (same convention as engine.m7.scheduler.run_once), so the
    daily thread survives a bad run and tries again tomorrow rather than
    dying silently. The local staging copy is always removed after the
    pass, uploaded or not - the 1GB disk this runs on holds the live DBs
    themselves and cannot also accumulate their backups (module docstring:
    a backup on the same disk as the primary protects against nothing)."""
    run_at = datetime.now(timezone.utc)
    stamp = run_at.strftime("%Y-%m-%dT%H-%M-%SZ")
    staging_dir.mkdir(parents=True, exist_ok=True)
    status: dict = {"run_at": run_at.isoformat(), "results": {}}

    sources = [("events", events_db_path), ("usage", usage_db_path)] + ([("qc", qc_db_path)] if qc_db_path else [])
    for label, db_path in sources:
        local_backup = staging_dir / f"{label}-{stamp}.db"
        try:
            if not Path(db_path).exists():
                status["results"][label] = {"outcome": "skipped", "reason": "source DB does not exist"}
                continue
            backup_one(db_path, local_backup)
            size = local_backup.stat().st_size
            object_key = None
            if is_configured():
                object_key = f"db-backups/{service_label}/{label}/{stamp}.db"
                upload_backup(local_backup, object_key)
                prune_remote(f"db-backups/{service_label}/{label}/")
                status["results"][label] = {"outcome": "ok", "bytes": size, "object_key": object_key}
            else:
                status["results"][label] = {
                    "outcome": "backed_up_not_uploaded",
                    "bytes": size,
                    "reason": f"{_ENV_BUCKET} is not set",
                }
        except Exception as exc:  # noqa: BLE001 - the loop must survive its own job failing
            logger.exception("db_backup: %s backup failed", label)
            status["results"][label] = {"outcome": "error", "error": repr(exc)}
        finally:
            if local_backup.exists():
                local_backup.unlink()

    (staging_dir / STATUS_FILENAME).write_text(json.dumps(status, indent=2))
    return status


def _next_run_at(now: datetime, hour: int = _DEFAULT_HOUR, minute: int = _DEFAULT_MINUTE) -> datetime:
    candidate = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
    if candidate <= now:
        candidate += timedelta(days=1)
    return candidate


def start_background_scheduler(events_db_path: str, usage_db_path: str, staging_dir: Path, qc_db_path: str | None = None) -> None:
    """Starts a daemon thread that runs run_backup_once daily. Fire-and-
    forget, same lifecycle contract as engine.m7.scheduler and
    engine.m4.idle_close's own schedulers: exits with the process, no
    separate management."""

    def _loop() -> None:
        while True:
            now = datetime.now(timezone.utc)
            next_run = _next_run_at(now)
            time.sleep(max(0.0, (next_run - now).total_seconds()))
            run_backup_once(events_db_path, usage_db_path, staging_dir, qc_db_path=qc_db_path)

    threading.Thread(target=_loop, name="db-daily-backup", daemon=True).start()


def _cli(argv: list[str]) -> int:
    """Manual entry point for a human running this inside the live
    container (Render's Shell/SSH - render.com/docs/ssh; Cron/one-off Jobs
    cannot reach the disk, module docstring). Not wired to any HTTP route -
    disaster recovery is a deliberate, human-run action, never an
    automatic response to an API call."""
    import argparse

    parser = argparse.ArgumentParser(prog="python -m engine.api.db_backup")
    sub = parser.add_subparsers(dest="command", required=True)

    p_backup = sub.add_parser("backup", help="run one backup pass now")
    p_backup.add_argument("--events-db", default=os.environ.get("CIC_API_EVENTS_DB", "./cic_api_events.db"))
    p_backup.add_argument("--usage-db", default=os.environ.get("CIC_API_USAGE_DB", "./cic_api_usage.db"))
    p_backup.add_argument("--staging-dir", default="./backups-staging")

    p_list = sub.add_parser("list", help="list backups for one DB label (events|usage)")
    p_list.add_argument("label", choices=["events", "usage"])
    p_list.add_argument("--service-label", default="cic-engine")

    p_restore = sub.add_parser("restore", help="restore one DB from a backup")
    p_restore.add_argument("--from-key", required=True, help="object key, or a local file path with --local")
    p_restore.add_argument("--target", required=True, help="path to overwrite, e.g. /data/cic_api_events.db")
    p_restore.add_argument("--local", action="store_true", help="--from-key is a local file, not an object key")

    args = parser.parse_args(argv)

    if args.command == "backup":
        result = run_backup_once(args.events_db, args.usage_db, Path(args.staging_dir))
        print(json.dumps(result, indent=2))
        return 0 if all(r.get("outcome") in ("ok", "backed_up_not_uploaded", "skipped") for r in result["results"].values()) else 1

    if args.command == "list":
        for key in list_backups(f"db-backups/{args.service_label}/{args.label}/"):
            print(key)
        return 0

    if args.command == "restore":
        if args.local:
            verify_integrity(args.from_key)
            restore_one(args.from_key, args.target)
        else:
            tmp = Path(args.target).with_suffix(".downloaded")
            download_backup(args.from_key, tmp)
            restore_one(tmp, args.target)
            tmp.unlink()
        print(f"restored {args.target} from {args.from_key}")
        return 0

    return 1


if __name__ == "__main__":
    sys.exit(_cli(sys.argv[1:]))
