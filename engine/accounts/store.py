"""The two SQLite files.

Durable: accounts, linked sign-ins and the deletion ledger. An account row holds
a random account id, a keyed address hash (none for an account that signs in
only with Google or Apple), days and weeks (never a time of day), an age band.
A linked sign-in holds the keyed hash of a provider's account id and the
provider's name. Nothing else.

Ephemeral: challenges, sessions and counters. A challenge is one proof of
control of an address: it has its own random id, belongs to one action, and is
found only by that id. They carry times so they can expire, are deleted when
they do, and are left out of backups.

Both files use secure_delete, so a deleted row's bytes are overwritten.
"""
import sqlite3
import threading
from dataclasses import dataclass
from typing import Callable

ACCOUNTS_TABLE = """(
  account_id    TEXT PRIMARY KEY,
  address_hash  TEXT UNIQUE,
  day_created   TEXT NOT NULL,
  refill_day    INTEGER NOT NULL,
  week_last_used TEXT NOT NULL,
  age_band      TEXT NOT NULL
) WITHOUT ROWID"""

DURABLE_DDL = f"""
DROP TABLE IF EXISTS recovery_codes;
DROP TABLE IF EXISTS pending_changes;
CREATE TABLE IF NOT EXISTS accounts {ACCOUNTS_TABLE};
CREATE TABLE IF NOT EXISTS linked_sign_ins (
  subject_hash TEXT PRIMARY KEY,
  account_id   TEXT NOT NULL,
  provider     TEXT NOT NULL,
  UNIQUE (account_id, provider)
) WITHOUT ROWID;
CREATE TABLE IF NOT EXISTS deletion_ledger (
  ledger_hash TEXT PRIMARY KEY,
  expires_on  TEXT NOT NULL
) WITHOUT ROWID;
"""

EPHEMERAL_DDL = """
CREATE TABLE IF NOT EXISTS challenges (
  challenge_id TEXT PRIMARY KEY,
  kind         TEXT NOT NULL,
  address_hash TEXT NOT NULL,
  account_id   TEXT,
  mac          TEXT NOT NULL,
  expires_at   INTEGER NOT NULL,
  tries        INTEGER NOT NULL DEFAULT 0
) WITHOUT ROWID;
CREATE INDEX IF NOT EXISTS challenges_by_address ON challenges (address_hash, kind);
CREATE INDEX IF NOT EXISTS challenges_by_account ON challenges (account_id);
CREATE TABLE IF NOT EXISTS sessions (
  token_hash       TEXT PRIMARY KEY,
  account_id       TEXT NOT NULL,
  idle_expires_at  INTEGER NOT NULL,
  abs_expires_at   INTEGER NOT NULL,
  stepped_up_until INTEGER NOT NULL DEFAULT 0
) WITHOUT ROWID;
CREATE INDEX IF NOT EXISTS sessions_by_account ON sessions (account_id);
CREATE TABLE IF NOT EXISTS spent_nonces (
  nonce      TEXT PRIMARY KEY,
  expires_at INTEGER NOT NULL
) WITHOUT ROWID;
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
    address_hash: str | None
    day_created: str
    refill_day: int
    week_last_used: str
    age_band: str


@dataclass(frozen=True)
class Challenge:
    challenge_id: str
    kind: str
    address_hash: str
    account_id: str | None
    mac: str
    expires_at: int
    tries: int


@dataclass(frozen=True)
class SessionRow:
    token_hash: str
    account_id: str
    idle_expires_at: int
    abs_expires_at: int
    stepped_up_until: int


def _open(path: str, ddl: str) -> sqlite3.Connection:
    conn = sqlite3.connect(path, check_same_thread=False, isolation_level=None)
    conn.execute("PRAGMA secure_delete = ON")
    conn.execute("PRAGMA journal_mode = DELETE")
    conn.executescript(ddl)
    return conn


def _allow_accounts_without_address(conn: sqlite3.Connection) -> None:
    """A durable file made when every account had an address has the column marked required;
    the table is rebuilt once with it optional, in one transaction."""
    column = next((r for r in conn.execute("PRAGMA table_info(accounts)") if r[1] == "address_hash"), None)
    if column is None or not column[3]:
        return
    try:
        conn.executescript(f"""
            BEGIN IMMEDIATE;
            ALTER TABLE accounts RENAME TO accounts_before;
            CREATE TABLE accounts {ACCOUNTS_TABLE};
            INSERT INTO accounts SELECT * FROM accounts_before;
            DROP TABLE accounts_before;
            COMMIT;
        """)
    except BaseException:
        if conn.in_transaction:
            conn.execute("ROLLBACK")
        raise


class AccountStore:
    def __init__(self, durable_path: str, ephemeral_path: str):
        self._lock = threading.RLock()
        self._d = _open(durable_path, DURABLE_DDL)
        _allow_accounts_without_address(self._d)
        self._e = _open(ephemeral_path, EPHEMERAL_DDL)

    def close(self) -> None:
        with self._lock:
            self._d.close()
            self._e.close()

    # accounts -------------------------------------------------------------

    def create_account(self, account: Account, link: tuple[str, str] | None = None) -> bool:
        """The account, and with it the provider link it signs in by, in one transaction. False
        when the address or the provider id already belongs to an account; nothing is written."""
        with self._lock:
            self._d.execute("BEGIN IMMEDIATE")
            try:
                made = self._d.execute(
                    "INSERT OR IGNORE INTO accounts VALUES (?, ?, ?, ?, ?, ?)",
                    (account.account_id, account.address_hash, account.day_created, account.refill_day,
                     account.week_last_used, account.age_band),
                ).rowcount == 1
                if made and link is not None:
                    made = self._d.execute(
                        "INSERT OR IGNORE INTO linked_sign_ins VALUES (?, ?, ?)", (link[0], account.account_id, link[1])
                    ).rowcount == 1
                self._d.execute("COMMIT" if made else "ROLLBACK")
            except BaseException:
                self._d.execute("ROLLBACK")
                raise
            return made

    # linked sign-ins -------------------------------------------------------

    def account_by_subjects(self, hashes: list[str]) -> tuple[Account, str, str] | None:
        """(account, the matching stored hash, provider) for a provider id, under any live key."""
        if not hashes:
            return None
        marks = ",".join("?" * len(hashes))
        with self._lock:
            link = self._d.execute(
                f"SELECT subject_hash, account_id, provider FROM linked_sign_ins WHERE subject_hash IN ({marks})", hashes
            ).fetchone()
            row = self._d.execute("SELECT * FROM accounts WHERE account_id = ?", (link[1],)).fetchone() if link else None
        return (Account(*row), link[0], link[2]) if row else None

    def links_of(self, account_id: str) -> dict[str, str]:
        """{provider: stored subject hash} for the account."""
        with self._lock:
            rows = self._d.execute("SELECT provider, subject_hash FROM linked_sign_ins WHERE account_id = ?", (account_id,))
            return {provider: subject_hash for provider, subject_hash in rows}

    def add_link(self, account_id: str, subject_hash: str, provider: str) -> bool:
        """False when the account is gone, the provider id is already linked anywhere, or the
        account has one for that provider."""
        with self._lock:
            return self._d.execute(
                "INSERT OR IGNORE INTO linked_sign_ins SELECT ?, account_id, ? FROM accounts WHERE account_id = ?",
                (subject_hash, provider, account_id),
            ).rowcount == 1

    def remove_link(self, account_id: str, provider: str) -> str:
        """'ok', 'missing' when the account has no such link, or 'last_method' when removing it
        would leave the account with no address and no other link. One statement, so two
        removals at once cannot both pass the check."""
        with self._lock:
            removed = self._d.execute(
                "DELETE FROM linked_sign_ins WHERE account_id = ?1 AND provider = ?2 AND ("
                " EXISTS (SELECT 1 FROM accounts WHERE account_id = ?1 AND address_hash IS NOT NULL)"
                " OR (SELECT COUNT(*) FROM linked_sign_ins WHERE account_id = ?1) > 1)",
                (account_id, provider),
            ).rowcount
            if removed:
                return "ok"
            held = self._d.execute(
                "SELECT 1 FROM linked_sign_ins WHERE account_id = ? AND provider = ?", (account_id, provider)
            ).fetchone()
        return "last_method" if held else "missing"

    def rekey_link(self, old_hash: str, new_hash: str) -> None:
        with self._lock:
            try:
                self._d.execute("UPDATE linked_sign_ins SET subject_hash = ? WHERE subject_hash = ?", (new_hash, old_hash))
            except sqlite3.IntegrityError:
                pass

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

    def accounts_on_older_keys(self, current_key_id: str) -> int:
        """Accounts holding an address or a provider id under an older key."""
        pattern = current_key_id + ":%"
        with self._lock:
            return self._d.execute(
                "SELECT COUNT(*) FROM (SELECT account_id FROM accounts WHERE address_hash NOT LIKE ? "
                "UNION SELECT account_id FROM linked_sign_ins WHERE subject_hash NOT LIKE ?)",
                (pattern, pattern),
            ).fetchone()[0]

    def delete_account(self, account_id: str, ledger_hash: str, ledger_expires_on: str) -> bool:
        """The account and one ledger entry, in one transaction."""
        with self._lock:
            self._d.execute("BEGIN IMMEDIATE")
            try:
                gone = self._d.execute("DELETE FROM accounts WHERE account_id = ?", (account_id,)).rowcount
                self._d.execute("DELETE FROM linked_sign_ins WHERE account_id = ?", (account_id,))
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
        with self._lock:
            return self._d.execute("DELETE FROM deletion_ledger WHERE expires_on < ?", (today,)).rowcount

    # challenges ---------------------------------------------------------------

    def put_challenge(self, challenge: Challenge, *, replace_same_address: bool = False) -> None:
        """Stores a challenge. For a sign-in the earlier ones for the same address are
        dropped, so only the newest code is live."""
        with self._lock:
            if replace_same_address:
                self._e.execute(
                    "DELETE FROM challenges WHERE address_hash = ? AND kind = ?", (challenge.address_hash, challenge.kind)
                )
            self._e.execute(
                "INSERT INTO challenges VALUES (?, ?, ?, ?, ?, ?, 0)",
                (challenge.challenge_id, challenge.kind, challenge.address_hash, challenge.account_id,
                 challenge.mac, challenge.expires_at),
            )

    def take_try(self, challenge_id: str, now: int, max_tries: int) -> Challenge | None:
        """Counts one try against a live challenge and returns it, in one transaction, so
        concurrent guesses cannot each read an unspent count. One that is expired, or
        already at its limit, is deleted and nothing is returned."""
        with self._lock:
            self._e.execute("BEGIN IMMEDIATE")
            try:
                row = self._e.execute("SELECT * FROM challenges WHERE challenge_id = ?", (challenge_id,)).fetchone()
                result = None
                if row is not None:
                    if row[5] <= now or row[6] >= max_tries:
                        self._e.execute("DELETE FROM challenges WHERE challenge_id = ?", (challenge_id,))
                    else:
                        self._e.execute("UPDATE challenges SET tries = tries + 1 WHERE challenge_id = ?", (challenge_id,))
                        result = Challenge(*row[:6], row[6] + 1)
                self._e.execute("COMMIT")
            except BaseException:
                self._e.execute("ROLLBACK")
                raise
        return result

    def burn_challenge_if(self, challenge_id: str, mac: str) -> bool:
        """Deletes the challenge if it is still the one given. Of several requests that
        present the same right code, exactly one gets True."""
        with self._lock:
            return self._e.execute(
                "DELETE FROM challenges WHERE challenge_id = ? AND mac = ?", (challenge_id, mac)
            ).rowcount == 1

    def burn_challenge(self, challenge_id: str) -> None:
        with self._lock:
            self._e.execute("DELETE FROM challenges WHERE challenge_id = ?", (challenge_id,))

    def delete_challenges_of(self, account_id: str, kind: str | None = None) -> None:
        with self._lock:
            if kind is None:
                self._e.execute("DELETE FROM challenges WHERE account_id = ?", (account_id,))
            else:
                self._e.execute("DELETE FROM challenges WHERE account_id = ? AND kind = ?", (account_id, kind))

    def forget_address(self, address_hash: str) -> None:
        """Removes the challenges and counters that carry an address hash."""
        with self._lock:
            self._e.execute("DELETE FROM challenges WHERE address_hash = ?", (address_hash,))
            self._e.execute("DELETE FROM counters WHERE key LIKE ?", ("%|" + address_hash,))

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

    # nonces ------------------------------------------------------------------

    def spend_nonce(self, nonce: str, expires_at: int) -> bool:
        """Records a provider nonce as used. Of several requests with the same nonce, one gets True."""
        with self._lock:
            return self._e.execute("INSERT OR IGNORE INTO spent_nonces VALUES (?, ?)", (nonce, expires_at)).rowcount == 1

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
        """Drops expired challenges and sessions and counters whose window has ended."""
        with self._lock:
            removed = self._e.execute("DELETE FROM challenges WHERE expires_at <= ?", (now,)).rowcount
            removed += self._e.execute(
                "DELETE FROM sessions WHERE idle_expires_at <= ? OR abs_expires_at <= ?", (now, now)
            ).rowcount
            removed += self._e.execute("DELETE FROM counters WHERE expires_at <= ?", (now,)).rowcount
            removed += self._e.execute("DELETE FROM spent_nonces WHERE expires_at <= ?", (now,)).rowcount
        return removed
