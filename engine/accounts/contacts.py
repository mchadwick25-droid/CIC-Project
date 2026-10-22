"""The contact file: the sign-in address, encrypted, for sending only.

A third SQLite file, apart from the account file and the ephemeral file. A row
holds the random account id and the address encrypted by a cipher the API edge
hands in, so this module needs no library beyond the standard one. The
ciphertext is bound to its account id, so a row cannot be moved to another
account. The address is read only to send mail to its owner: a code, a notice
that a recovery was started, a warning, a breach notice. It is deleted with the
account. Neither this file nor the account file alone names anyone next to an
account; both files and the contact key together do.
"""
import sqlite3
import threading
from typing import Protocol

DDL = """
CREATE TABLE IF NOT EXISTS contacts (
  account_id TEXT PRIMARY KEY,
  key_id     TEXT NOT NULL,
  blob       TEXT NOT NULL
) WITHOUT ROWID;
CREATE TABLE IF NOT EXISTS pending_contacts (
  account_id TEXT PRIMARY KEY,
  key_id     TEXT NOT NULL,
  blob       TEXT NOT NULL
) WITHOUT ROWID;
"""


class Cipher(Protocol):
    key_id: str

    def encrypt(self, plaintext: str, context: str) -> str:
        """The text, sealed under the current key and bound to the context."""

    def decrypt(self, blob: str, context: str) -> str | None:
        """The text, or None when the key, the context or the bytes are wrong."""


class ContactStore:
    def __init__(self, path: str, cipher: Cipher):
        self._cipher = cipher
        self._lock = threading.RLock()
        self._c = sqlite3.connect(path, check_same_thread=False, isolation_level=None)
        self._c.execute("PRAGMA secure_delete = ON")
        self._c.execute("PRAGMA journal_mode = DELETE")
        self._c.executescript(DDL)

    def close(self) -> None:
        with self._lock:
            self._c.close()

    @property
    def key_id(self) -> str:
        return self._cipher.key_id

    def _put(self, table: str, account_id: str, address: str) -> None:
        blob = self._cipher.encrypt(address, f"{table}|{account_id}")
        with self._lock:
            self._c.execute(
                f"INSERT INTO {table} VALUES (?, ?, ?) ON CONFLICT (account_id) DO UPDATE SET key_id = excluded.key_id, blob = excluded.blob",
                (account_id, self._cipher.key_id, blob),
            )

    def _get(self, table: str, account_id: str) -> str | None:
        with self._lock:
            row = self._c.execute(f"SELECT blob FROM {table} WHERE account_id = ?", (account_id,)).fetchone()
        return self._cipher.decrypt(row[0], f"{table}|{account_id}") if row else None

    def put(self, account_id: str, address: str) -> None:
        self._put("contacts", account_id, address)

    def get(self, account_id: str) -> str | None:
        """The address, only to send to it. None when there is none or the key cannot open it."""
        return self._get("contacts", account_id)

    def is_current(self, account_id: str) -> bool:
        """Whether the account has a contact sealed under the current key."""
        with self._lock:
            row = self._c.execute("SELECT key_id FROM contacts WHERE account_id = ?", (account_id,)).fetchone()
        return row is not None and row[0] == self._cipher.key_id

    def put_pending(self, account_id: str, address: str) -> None:
        """The new address of a recovery that has been proved and is waiting out its days."""
        self._put("pending_contacts", account_id, address)

    def take_pending(self, account_id: str) -> str | None:
        address = self._get("pending_contacts", account_id)
        self.forget_pending(account_id)
        return address

    def forget_pending(self, account_id: str) -> None:
        with self._lock:
            self._c.execute("DELETE FROM pending_contacts WHERE account_id = ?", (account_id,))

    def forget(self, account_id: str) -> None:
        with self._lock:
            self._c.execute("DELETE FROM contacts WHERE account_id = ?", (account_id,))
            self._c.execute("DELETE FROM pending_contacts WHERE account_id = ?", (account_id,))

    def on_older_keys(self) -> int:
        with self._lock:
            return self._c.execute("SELECT COUNT(*) FROM contacts WHERE key_id != ?", (self._cipher.key_id,)).fetchone()[0]
