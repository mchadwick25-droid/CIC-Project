"""The outside copy of the deletion ledger.

The ledger sits in the accounts file, so a backup made before a deletion restores
without it and the deleted account would return. Each ledger entry is therefore
also written to the backup bucket the moment the account is deleted: an empty
object whose name is the day it expires and the ledger hash (a hash of the
account's random internal id, never an address or its hash). A restored file reads
these back at start-up and removes the accounts they name. Entries are removed
from the bucket once they expire, a margin after the 14 days backups are kept.
"""
import os
import re
from datetime import date, datetime, timezone

from engine.api import db_backup

SERVICE_LABEL = "cic-engine"
_NAME = re.compile(r"^(\d{4}-\d{2}-\d{2})_([0-9a-f]{64})$")


def _prefix() -> str:
    return f"db-backups/{SERVICE_LABEL}/ledger/"


def _today() -> date:
    return datetime.now(timezone.utc).date()


def publish(ledger_hash: str, expires_on: str) -> bool:
    """True when the entry is in the bucket. False when no bucket is set, so the entry waits."""
    if not db_backup.is_configured():
        return False
    if not _NAME.match(f"{expires_on}_{ledger_hash}"):
        raise ValueError("not a ledger entry")
    client = db_backup._client()
    client.put_object(Bucket=_bucket(), Key=f"{_prefix()}{expires_on}_{ledger_hash}", Body=b"")
    return True


def entries() -> list[tuple[str, str]]:
    """(ledger hash, expiry day) for each entry in the bucket that has not expired."""
    if not db_backup.is_configured():
        return []
    found = []
    for key in db_backup.list_backups(_prefix()):
        match = _NAME.match(key[len(_prefix()):])
        if match and date.fromisoformat(match.group(1)) >= _today():
            found.append((match.group(2), match.group(1)))
    return found


def prune() -> list[str]:
    """Removes entries past their expiry. A name this module did not write is left alone."""
    if not db_backup.is_configured():
        return []
    client = db_backup._client()
    removed = []
    for key in db_backup.list_backups(_prefix()):
        match = _NAME.match(key[len(_prefix()):])
        if match and date.fromisoformat(match.group(1)) < _today():
            client.delete_object(Bucket=_bucket(), Key=key)
            removed.append(key)
    return removed


def _bucket() -> str:
    return os.environ[db_backup._ENV_BUCKET]
