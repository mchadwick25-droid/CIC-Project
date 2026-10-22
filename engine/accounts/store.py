"""The two SQLite files.

Durable: accounts, one recovery code each, pending recovery changes, and the
deletion ledger. A row holds a random account id, a keyed address hash, days
and weeks (never a time of day), an age band. Nothing else.

Ephemeral: sign-in codes, sessions and counters. They carry times so they can
expire, are deleted when they do, and are left out of backups.

Both files use secure_delete, so a deleted row's bytes are overwritten.
"""
import sqlite3
import threading
from dataclasses import dataclass
from typing import Callable

DURABLE_DDL = """
CREATE TABLE IF NOT EXISTS accounts (
  account_id    TEXT PRIMARY KEY,
  address_hash  TEXT NOT NULL UNIQUE,
  day_created   TEXT NOT NULL,
  refill_day    INTEGER NOT NULL,
  week_last_used TEXT NOT NULL,
  age_band      TEXT NOT NULL
) WITHOUT ROWID;
CREATE TABLE IF NOT EXISTS recovery_codes (
  account_id TEXT PRIMARY KEY,
  code_hash  TEXT NOT NULL UNIQUE,
  day_made   TEXT NOT NULL
) WITHOUT ROWID;
CREATE TABLE IF NOT EXISTS pending_changes (
  account_id       TEXT PRIMARY KEY,
  new_address_hash TEXT NOT NULL UNIQUE,
  effective_on     TEXT NOT NULL,
  verified         INTEGER NOT NULL DEFAULT 0,
  made_on          TEXT NOT NULL
) WITHOUT ROWID;
CREATE TABLE IF NOT EXISTS deletion_ledger (
  ledger_hash TEXT PRIMARY KEY,
  expires_on  TEXT NOT NULL
) WITHOUT ROWID;
"""

EPHEMERAL_DDL = """
CREATE TABLE IF NOT EXISTS sign_in_codes (
  address_hash TEXT NOT NULL,
  purpose      TEXT NOT NULL,
  mac          TEXT NOT NULL,
  expires_at   INTEGER NOT NULL,
  tries        INTEGER NOT NULL DEFAULT 0,
  account_id   TEXT,
  PRIMARY KEY (address_hash, purpose)
) WITHOUT ROWID;
CREATE TABLE IF NOT EXISTS sessions (
  token_hash       TEXT PRIMARY KEY,
  account_id       TEXT NOT NULL,
  idle_expires_at  INTEGER NOT NULL,
  abs_expires_at   INTEGER NOT NULL,
  stepped_up_until INTEGER NOT NULL DEFAULT 0
) WITHOUT ROWID;
CREATE INDEX IF NOT EXISTS sessions_by_account ON sessions (account_id);
CREATE TABLE IF NOT EXISTS counters (
  scope   TEXT NOT NULL,
  key     TEXT NOT NULL,
  window  INTEGER NOT NULL,
  count   INTEGER NOT NULL,
  expires_at INTEGER NOT NULL,
  PRIMARY KEY (scope, key, window)
) WITHOUT ROWID;
"""


@dataclass(frozen=True)
class Account:
    account_id: str
    address_hash: str
    day_created: str
    refill_day: int
    week_last_used: str
    age_band: str


@dataclass(frozen=True)
class CodeRow:
    mac: str
    expires_at: int
    tries: int
    account_id: str | None


@dataclass(frozen=True)
class SessionRow:
    token_hash: str
    account_id: str
    idle_expires_at: int
    abs_expires_at: int
    stepped_up_until: int


@dataclass(frozen=True)
class Pending:
    account_id: str
    new_address_hash: str
    effective_on: str
    verified: bool
    made_on: str = ""


def _open(path: str, ddl: str) -> sqlite3.Connection:
    conn = sqlite3.connect(path, check_same_thread=False, isolation_level=None)
    conn.execute("PRAGMA secure_delete = ON")
    conn.execute("PRAGMA journal_mode = DELETE")
    conn.executescript(ddl)
    return conn


class AccountStore:
    def __init__(self, durable_path: str, ephemeral_path: str):
        self._lock = threading.RLock()
        self._d = _open(durable_path, DURABLE_DDL)
        self._e = _open(ephemeral_path, EPHEMERAL_DDL)

    def close(self) -> None:
        with self._lock:
            self._d.close()
            self._e.close()

    # accounts -------------------------------------------------------------

    def create_account(self, account: Account) -> bool:
        with self._lock:
            cur = self._d.execute(
                "INSERT OR IGNORE INTO accounts VALUES (?, ?, ?, ?, ?, ?)",
                (account.account_id, account.address_hash, account.day_created, account.refill_day,
                 account.week_last_used, account.age_band),
            )
            return cur.rowcount == 1

    def account_by_hashes(self, hashes: list[str]) -> Account | None:
        if not hashes:
            return None
        marks = ",".join("?" * len(hashes))
        with self._lock:
            row = self._d.execute(f"SELECT * FROM accounts WHERE address_hash IN ({marks})", hashes).fetchone()
        return Account(*row) if row else None

    def account(self, account_id: str) -> Account | None:
        with self._lock:
            row = self._d.execute("SELECT * FROM accounts WHERE account_id = ?", (account_id,)).fetchone()
        return Account(*row) if row else None

    def set_address_hash(self, account_id: str, address_hash: str) -> bool:
        with self._lock:
            try:
                cur = self._d.execute("UPDATE accounts SET address_hash = ? WHERE account_id = ?", (address_hash, account_id))
            except sqlite3.IntegrityError:
                return False
            return cur.rowcount == 1

    def touch(self, account_id: str, week: str) -> None:
        with self._lock:
            self._d.execute("UPDATE accounts SET week_last_used = ? WHERE account_id = ?", (week, account_id))

    def delete_account(self, account_id: str, ledger_hash: str, ledger_expires_on: str) -> bool:
        """The account, its recovery code and its pending change, and one
        ledger entry, in one transaction."""
        with self._lock:
            self._d.execute("BEGIN IMMEDIATE")
            try:
                gone = self._d.execute("DELETE FROM accounts WHERE account_id = ?", (account_id,)).rowcount
                self._d.execute("DELETE FROM recovery_codes WHERE account_id = ?", (account_id,))
                self._d.execute("DELETE FROM pending_changes WHERE account_id = ?", (account_id,))
                if gone:
                    self._d.execute("INSERT OR IGNORE INTO deletion_ledger VALUES (?, ?)", (ledger_hash, ledger_expires_on))
                self._d.execute("COMMIT")
            except BaseException:
                self._d.execute("ROLLBACK")
                raise
            return gone == 1

    def accounts_in_ledger(self, hash_of: Callable[[str], str]) -> list[str]:
        """Ids of live accounts whose ledger hash is on the ledger."""
        with self._lock:
            ledger = {r[0] for r in self._d.execute("SELECT ledger_hash FROM deletion_ledger")}
            ids = [r[0] for r in self._d.execute("SELECT account_id FROM accounts")]
        return [i for i in ids if hash_of(i) in ledger]

    def purge_durable(self, today: str) -> int:
        """Drops expired ledger entries and recovery changes never verified within a day."""
        with self._lock:
            removed = self._d.execute("DELETE FROM deletion_ledger WHERE expires_on < ?", (today,)).rowcount
            removed += self._d.execute(
                "DELETE FROM pending_changes WHERE verified = 0 AND made_on < ?", (today,)
            ).rowcount
        return removed

    def accounts_on_older_keys(self, current_key_id: str) -> int:
        with self._lock:
            return self._d.execute(
                "SELECT COUNT(*) FROM accounts WHERE address_hash NOT LIKE ?", (current_key_id + ":%",)
            ).fetchone()[0]

    # recovery codes -------------------------------------------------------

    def put_recovery_code(self, account_id: str, code_hash: str, day: str) -> None:
        with self._lock:
            self._d.execute("INSERT OR REPLACE INTO recovery_codes VALUES (?, ?, ?)", (account_id, code_hash, day))

    def account_by_recovery_hash(self, code_hash: str) -> str | None:
        with self._lock:
            row = self._d.execute("SELECT account_id FROM recovery_codes WHERE code_hash = ?", (code_hash,)).fetchone()
        return row[0] if row else None

    def has_recovery_code(self, account_id: str) -> bool:
        with self._lock:
            return self._d.execute("SELECT 1 FROM recovery_codes WHERE account_id = ?", (account_id,)).fetchone() is not None

    def delete_recovery_code(self, account_id: str) -> None:
        with self._lock:
            self._d.execute("DELETE FROM recovery_codes WHERE account_id = ?", (account_id,))

    # pending recovery changes --------------------------------------------

    def put_pending(self, pending: Pending) -> bool:
        with self._lock:
            try:
                self._d.execute(
                    "INSERT OR REPLACE INTO pending_changes VALUES (?, ?, ?, ?, ?)",
                    (pending.account_id, pending.new_address_hash, pending.effective_on, int(pending.verified),
                     pending.made_on),
                )
            except sqlite3.IntegrityError:
                return False
            return True

    def pending_for_account(self, account_id: str) -> Pending | None:
        with self._lock:
            row = self._d.execute("SELECT * FROM pending_changes WHERE account_id = ?", (account_id,)).fetchone()
        return Pending(row[0], row[1], row[2], bool(row[3]), row[4]) if row else None

    def pending_for_hash(self, new_address_hash: str) -> Pending | None:
        with self._lock:
            row = self._d.execute("SELECT * FROM pending_changes WHERE new_address_hash = ?", (new_address_hash,)).fetchone()
        return Pending(row[0], row[1], row[2], bool(row[3]), row[4]) if row else None

    def verify_pending(self, new_address_hash: str) -> bool:
        with self._lock:
            return self._d.execute(
                "UPDATE pending_changes SET verified = 1 WHERE new_address_hash = ?", (new_address_hash,)
            ).rowcount == 1

    def delete_pending(self, account_id: str) -> None:
        with self._lock:
            self._d.execute("DELETE FROM pending_changes WHERE account_id = ?", (account_id,))

    # sign-in codes ---------------------------------------------------------

    def put_code(self, address_hash: str, purpose: str, mac: str, expires_at: int, account_id: str | None) -> None:
        with self._lock:
            self._e.execute(
                "INSERT OR REPLACE INTO sign_in_codes VALUES (?, ?, ?, ?, 0, ?)",
                (address_hash, purpose, mac, expires_at, account_id),
            )

    def get_code(self, address_hash: str, purpose: str) -> CodeRow | None:
        with self._lock:
            row = self._e.execute(
                "SELECT mac, expires_at, tries, account_id FROM sign_in_codes WHERE address_hash = ? AND purpose = ?",
                (address_hash, purpose),
            ).fetchone()
        return CodeRow(*row) if row else None

    def take_try(self, address_hash: str, purpose: str, now: int, max_tries: int) -> CodeRow | None:
        """Counts one try against a live code and returns the row, in one
        transaction, so concurrent guesses cannot each read an unspent count. A
        code that is expired, or already at its limit, is deleted and nothing is
        returned."""
        with self._lock:
            self._e.execute("BEGIN IMMEDIATE")
            try:
                row = self._e.execute(
                    "SELECT mac, expires_at, tries, account_id FROM sign_in_codes WHERE address_hash = ? AND purpose = ?",
                    (address_hash, purpose),
                ).fetchone()
                result = None
                if row is not None:
                    if row[1] <= now or row[2] >= max_tries:
                        self._e.execute(
                            "DELETE FROM sign_in_codes WHERE address_hash = ? AND purpose = ?", (address_hash, purpose)
                        )
                    else:
                        self._e.execute(
                            "UPDATE sign_in_codes SET tries = tries + 1 WHERE address_hash = ? AND purpose = ?",
                            (address_hash, purpose),
                        )
                        result = CodeRow(row[0], row[1], row[2] + 1, row[3])
                self._e.execute("COMMIT")
            except BaseException:
                self._e.execute("ROLLBACK")
                raise
        return result

    def burn_code_if(self, address_hash: str, purpose: str, mac: str) -> bool:
        """Deletes the code if it is still the one given. Of several requests
        that present the same right code, exactly one gets True."""
        with self._lock:
            return self._e.execute(
                "DELETE FROM sign_in_codes WHERE address_hash = ? AND purpose = ? AND mac = ?",
                (address_hash, purpose, mac),
            ).rowcount == 1

    def burn_code(self, address_hash: str, purpose: str) -> None:
        with self._lock:
            self._e.execute("DELETE FROM sign_in_codes WHERE address_hash = ? AND purpose = ?", (address_hash, purpose))

    # sessions --------------------------------------------------------------

    def put_session(self, row: SessionRow) -> None:
        with self._lock:
            self._e.execute(
                "INSERT INTO sessions VALUES (?, ?, ?, ?, ?)",
                (row.token_hash, row.account_id, row.idle_expires_at, row.abs_expires_at, row.stepped_up_until),
            )

    def get_session(self, token_hash: str) -> SessionRow | None:
        with self._lock:
            row = self._e.execute("SELECT * FROM sessions WHERE token_hash = ?", (token_hash,)).fetchone()
        return SessionRow(*row) if row else None

    def slide_session(self, token_hash: str, idle_expires_at: int) -> None:
        with self._lock:
            self._e.execute("UPDATE sessions SET idle_expires_at = ? WHERE token_hash = ?", (idle_expires_at, token_hash))

    def step_up_session(self, token_hash: str, until: int) -> None:
        with self._lock:
            self._e.execute("UPDATE sessions SET stepped_up_until = ? WHERE token_hash = ?", (until, token_hash))

    def delete_session(self, token_hash: str) -> None:
        with self._lock:
            self._e.execute("DELETE FROM sessions WHERE token_hash = ?", (token_hash,))

    def delete_sessions_of(self, account_id: str, except_token_hash: str | None = None) -> int:
        with self._lock:
            return self._e.execute(
                "DELETE FROM sessions WHERE account_id = ? AND token_hash IS NOT ?", (account_id, except_token_hash)
            ).rowcount

    def delete_codes_of(self, account_id: str) -> None:
        with self._lock:
            self._e.execute("DELETE FROM sign_in_codes WHERE account_id = ?", (account_id,))

    def forget_address(self, address_hash: str) -> None:
        """Removes the codes and counters that carry an address hash."""
        with self._lock:
            self._e.execute("DELETE FROM sign_in_codes WHERE address_hash = ?", (address_hash,))
            self._e.execute("DELETE FROM counters WHERE key = ?", (address_hash,))

    # counters ---------------------------------------------------------------

    def hit(self, scope: str, key: str, window_seconds: int, limit: int, now: int) -> bool:
        """Counts one event in the current window and says whether it is still
        within the limit. The count survives a restart."""
        window = now // window_seconds
        with self._lock:
            self._e.execute("BEGIN IMMEDIATE")
            try:
                self._e.execute(
                    "INSERT INTO counters VALUES (?, ?, ?, 1, ?) ON CONFLICT (scope, key, window) DO UPDATE SET count = count + 1",
                    (scope, key, window, (window + 1) * window_seconds),
                )
                count = self._e.execute(
                    "SELECT count FROM counters WHERE scope = ? AND key = ? AND window = ?", (scope, key, window)
                ).fetchone()[0]
                self._e.execute("COMMIT")
            except BaseException:
                self._e.execute("ROLLBACK")
                raise
        return count <= limit

    def purge_ephemeral(self, now: int) -> int:
        """Drops expired codes and sessions and counters whose window has ended."""
        with self._lock:
            removed = self._e.execute("DELETE FROM sign_in_codes WHERE expires_at <= ?", (now,)).rowcount
            removed += self._e.execute(
                "DELETE FROM sessions WHERE idle_expires_at <= ? OR abs_expires_at <= ?", (now, now)
            ).rowcount
            removed += self._e.execute("DELETE FROM counters WHERE expires_at <= ?", (now,)).rowcount
        return removed
