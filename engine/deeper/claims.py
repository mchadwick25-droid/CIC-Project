"""The claim table: a purchase reference and the plain code it earned.

This is the one place a plain code and a reference sit together, so it is
kept as small as it can be. It lives in its own file, is never backed up,
deletes with secure_delete on, and a row lasts one hour: long enough for a
dropped response, a link preview or a double page load not to lose the code.
"""
import re
import sqlite3
import threading
import time
from typing import Callable

CLAIM_TTL_SECONDS = 3600
_REFERENCE = re.compile(r"^[A-Za-z0-9_-]{16,64}$")

_SCHEMA = """
CREATE TABLE IF NOT EXISTS claims (
    reference TEXT PRIMARY KEY,
    codes TEXT NOT NULL,
    created_epoch INTEGER NOT NULL
) WITHOUT ROWID;
"""


def valid_reference(reference: str | None) -> bool:
    return isinstance(reference, str) and _REFERENCE.match(reference) is not None


class ClaimStore:
    def __init__(self, path: str, *, clock: Callable[[], float] = time.time):
        self._clock = clock
        self._lock = threading.RLock()
        self._conn = sqlite3.connect(path, check_same_thread=False, isolation_level=None)
        self._conn.execute("PRAGMA journal_mode=DELETE")
        self._conn.execute("PRAGMA secure_delete=ON")
        self._conn.executescript(_SCHEMA)

    def close(self) -> None:
        with self._lock:
            self._conn.close()

    def put(self, reference: str, plain_codes: list[str]) -> bool:
        """False if the reference holds live codes: a replay never overwrites.
        An expired row is removed first, so it cannot shadow the new one."""
        if not valid_reference(reference) or not plain_codes:
            raise ValueError("a claim needs a well-formed reference and at least one code")
        with self._lock:
            self._conn.execute(
                "DELETE FROM claims WHERE reference = ? AND created_epoch <= ?",
                (reference, int(self._clock()) - CLAIM_TTL_SECONDS),
            )
            return bool(
                self._conn.execute(
                    "INSERT OR IGNORE INTO claims (reference, codes, created_epoch) VALUES (?, ?, ?)",
                    (reference, "\n".join(plain_codes), int(self._clock())),
                ).rowcount
            )

    def get(self, reference: str | None) -> list[str] | None:
        if not valid_reference(reference):
            return None
        with self._lock:
            row = self._conn.execute("SELECT codes, created_epoch FROM claims WHERE reference = ?", (reference,)).fetchone()
        if row is None or self._clock() - row[1] >= CLAIM_TTL_SECONDS:
            return None
        return row[0].split("\n")

    def delete(self, reference: str) -> None:
        with self._lock:
            self._conn.execute("DELETE FROM claims WHERE reference = ?", (reference,))

    def purge(self) -> int:
        with self._lock:
            return self._conn.execute(
                "DELETE FROM claims WHERE created_epoch <= ?", (int(self._clock()) - CLAIM_TTL_SECONDS,)
            ).rowcount
