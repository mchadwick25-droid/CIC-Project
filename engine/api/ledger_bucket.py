"""The outside copy of the deletion ledger, the erasure ledger and the closure marks.

Both ledgers sit in the accounts file, so a backup made before a deletion or an
erasure restores without it: a deleted account would return, and so would an
erased conversation. Each entry is therefore also written to the backup bucket
the moment it is made.

A deletion entry is an empty object named by the day it expires and the ledger
hash (a hash of the account's random internal id, never an address or its hash).
A closure mark is also an empty object, named by the day the closed account will be erased and the
same ledger hash. A restored file reads the marks back and closes any account they name that the file
still shows open, so a restore never re-opens an account its owner deleted. Re-opening removes the mark.
An erasure entry is named by its expiry day and a hash of the conversation's keyed
hash, and its body, sealed under the backup key, holds that keyed hash and the
review tokens that find the conversation's review rows. A restored file reads
both back at start-up and each hour, and removes the accounts they name and erases
the conversations they name again. Entries are removed from the bucket once they
expire, a margin after the 14 days backups are kept.
"""
import hashlib
import json
import logging
import os
import re
from datetime import date, datetime, timezone

from engine.api import db_backup

logger = logging.getLogger("cic.accounts")

SERVICE_LABEL = "cic-engine"
_NAME = re.compile(r"^(\d{4}-\d{2}-\d{2})_([0-9a-f]{64})$")


def _prefix() -> str:
    return f"db-backups/{SERVICE_LABEL}/ledger/"


def _erased_prefix() -> str:
    return f"db-backups/{SERVICE_LABEL}/erased/"


def _closed_prefix() -> str:
    return f"db-backups/{SERVICE_LABEL}/closed/"


def _today() -> date:
    return datetime.now(timezone.utc).date()


def publish(ledger_hash: str, expires_on: str) -> bool:
    """True when the entry is in the bucket. False when no bucket is set, so the entry waits."""
    if not db_backup.is_configured():
        return False
    if not _NAME.match(f"{expires_on}_{ledger_hash}"):
        raise ValueError("not a ledger entry")
    client = db_backup._client(quick=True)
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


def publish_closure(ledger_hash: str, erase_on: str) -> bool:
    """True when the mark is in the bucket. False when no bucket is set, so the mark waits."""
    if not db_backup.is_configured():
        return False
    if not _NAME.match(f"{erase_on}_{ledger_hash}"):
        raise ValueError("not a closure mark")
    db_backup._client(quick=True).put_object(Bucket=_bucket(), Key=f"{_closed_prefix()}{erase_on}_{ledger_hash}", Body=b"")
    return True


def remove_closure(ledger_hash: str, erase_on: str) -> bool:
    """True when the mark is gone from the bucket, or there is no bucket. A refusal raises."""
    if not db_backup.is_configured():
        return True
    if not _NAME.match(f"{erase_on}_{ledger_hash}"):
        raise ValueError("not a closure mark")
    db_backup._client(quick=True).delete_object(Bucket=_bucket(), Key=f"{_closed_prefix()}{erase_on}_{ledger_hash}")
    return True


def closures() -> list[tuple[str, str]]:
    """(ledger hash, erase day) for each closure mark in the bucket that has not passed its day."""
    if not db_backup.is_configured():
        return []
    found = []
    for key in db_backup.list_backups(_closed_prefix()):
        match = _NAME.match(key[len(_closed_prefix()):])
        if match and date.fromisoformat(match.group(1)) >= _today():
            found.append((match.group(2), match.group(1)))
    return found


def publish_erasure(sealer, session_hash: str, qc_tokens: str, expires_on: str) -> bool:
    """True when the erasure is in the bucket. The entry is sealed under the backup key: it holds the
    keyed hash of the conversation's id and the review tokens, which find the review rows. Its name
    holds only the expiry day and a hash of the keyed hash."""
    if not db_backup.is_configured():
        return False
    name = f"{expires_on}_{hashlib.sha256(session_hash.encode()).hexdigest()}"
    if not _NAME.match(name):
        raise ValueError("not an erasure entry")
    body = sealer.seal(json.dumps({"h": session_hash, "t": qc_tokens}).encode(), "erased")
    db_backup._client(quick=True).put_object(Bucket=_bucket(), Key=f"{_erased_prefix()}{name}", Body=body)
    return True


def erasures(sealer) -> list[tuple[str, str, str]]:
    """(session hash, review tokens, expiry day) for each unexpired erasure in the bucket. An entry
    that cannot be opened is skipped; the others are still returned."""
    if not db_backup.is_configured():
        return []
    client = db_backup._client(quick=True)
    found = []
    for key in db_backup.list_backups(_erased_prefix()):
        match = _NAME.match(key[len(_erased_prefix()):])
        if not match or date.fromisoformat(match.group(1)) < _today():
            continue
        try:
            body = client.get_object(Bucket=_bucket(), Key=key)["Body"].read()
            data = json.loads(sealer.open(body, "erased"))
            found.append((data["h"], data["t"], match.group(1)))
        except Exception:  # noqa: BLE001 - one unreadable entry must not hide the rest
            logger.warning("an erasure-ledger entry could not be read")
    return found


def prune() -> list[str]:
    """Removes entries past their expiry, from all three. A name this module did not write is left alone."""
    if not db_backup.is_configured():
        return []
    client = db_backup._client(quick=True)
    removed = []
    for prefix in (_prefix(), _erased_prefix(), _closed_prefix()):
        for key in db_backup.list_backups(prefix):
            match = _NAME.match(key[len(prefix):])
            if match and date.fromisoformat(match.group(1)) < _today():
                client.delete_object(Bucket=_bucket(), Key=key)
                removed.append(key)
    return removed


def _bucket() -> str:
    return os.environ[db_backup._ENV_BUCKET]
