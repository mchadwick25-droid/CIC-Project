"""The meter: what each code holds and how much of it is spent.

The meter keys on a hash of the code. It stores no session id, visitor id,
session-code hash, IP address, name, email or text, and no timestamp finer
than a day: the day a code was made and the week it was last used. It keeps
the Stripe payment id, so a refund or dispute can void a code and a sponsor's
batch can be voided in one step.

Admission reserves an exchange before the voice speaks; settling spends it,
releasing returns it. Reservations live in memory only, so a restart gives
every in-flight reservation back and nobody pays for an exchange that never
finished. One process serves all traffic, so the lock below is the arbiter.
"""
import logging
import sqlite3
import threading
from dataclasses import dataclass
from datetime import date, datetime, timedelta, timezone
from typing import Callable

from engine.deeper import codes
from engine.deeper.config import DEFAULT_GROUP_DAILY_CEILING

logger = logging.getLogger("cic.deeper")

KINDS = ("single", "batch", "group")
LIVE, SPENT, VOID = "live", "spent", "void"

TALLY_FIELDS = ("payments_seen", "payments_minted", "payments_voided_first", "codes_minted", "refunds_applied", "partial_refunds_ignored")
RECONCILE_RETENTION_DAYS = 90

MAX_EXCHANGES_PER_CODE = 10_000
MAX_BATCH_COUNT = 1_000
RETENTION_DAYS = 30

_SCHEMA = """
CREATE TABLE IF NOT EXISTS meter (
    code_hash TEXT PRIMARY KEY,
    kind TEXT NOT NULL CHECK (kind IN ('single', 'batch', 'group')),
    exchanges_total INTEGER NOT NULL CHECK (exchanges_total > 0),
    exchanges_used INTEGER NOT NULL DEFAULT 0 CHECK (exchanges_used >= 0 AND exchanges_used <= exchanges_total),
    payment_id TEXT NOT NULL,
    day_created TEXT NOT NULL,
    week_last_used TEXT,
    status TEXT NOT NULL DEFAULT 'live' CHECK (status IN ('live', 'spent', 'void')),
    daily_ceiling INTEGER CHECK (daily_ceiling IS NULL OR daily_ceiling > 0)
) WITHOUT ROWID;
CREATE INDEX IF NOT EXISTS meter_payment ON meter (payment_id);
CREATE TABLE IF NOT EXISTS voided_payments (
    payment_id TEXT PRIMARY KEY,
    week_voided TEXT NOT NULL
) WITHOUT ROWID;
CREATE TABLE IF NOT EXISTS reconcile (
    day TEXT PRIMARY KEY,
    payments_seen INTEGER NOT NULL DEFAULT 0,
    payments_minted INTEGER NOT NULL DEFAULT 0,
    payments_voided_first INTEGER NOT NULL DEFAULT 0,
    codes_minted INTEGER NOT NULL DEFAULT 0,
    refunds_applied INTEGER NOT NULL DEFAULT 0,
    partial_refunds_ignored INTEGER NOT NULL DEFAULT 0
) WITHOUT ROWID;
CREATE TABLE IF NOT EXISTS state (
    key TEXT PRIMARY KEY,
    value TEXT NOT NULL
) WITHOUT ROWID;
"""


class DeeperError(Exception):
    pass


class AlreadyMinted(DeeperError):
    """The payment already has codes; a replayed webhook mints nothing."""


class PaymentVoided(DeeperError):
    """The payment was refunded or disputed before its codes were made."""


@dataclass(frozen=True)
class CodeStatus:
    kind: str
    status: str
    exchanges_total: int
    exchanges_used: int
    daily_ceiling: int | None

    @property
    def remaining(self) -> int:
        return 0 if self.status == VOID else self.exchanges_total - self.exchanges_used


class Reservation:
    """One exchange held against a code. Carries the code's hash, never the code."""

    __slots__ = ("code_hash", "day", "done")

    def __init__(self, code_hash: str, day: str):
        self.code_hash = code_hash
        self.day = day
        self.done = False


@dataclass(frozen=True)
class Admission:
    ok: bool
    reason: str | None = None
    reservation: Reservation | None = None
    remaining: int | None = None


def week_of(day: date) -> str:
    iso = day.isocalendar()
    return f"{iso.year}-W{iso.week:02d}"


def _end_of_week(week: str) -> date:
    year, number = week.split("-W")
    return date.fromisocalendar(int(year), int(number), 7)


def _utc_today() -> date:
    return datetime.now(timezone.utc).date()


class Meter:
    def __init__(
        self,
        path: str,
        *,
        clock: Callable[[], date] = _utc_today,
        group_daily_ceiling: int = DEFAULT_GROUP_DAILY_CEILING,
    ):
        self._clock = clock
        self._group_daily_ceiling = group_daily_ceiling
        self._lock = threading.RLock()
        self._reserved: dict[str, int] = {}
        self._day_used: dict[str, tuple[str, int]] = {}
        self._conn = sqlite3.connect(path, check_same_thread=False, isolation_level=None)
        self._conn.execute("PRAGMA journal_mode=WAL")
        self._conn.execute("PRAGMA secure_delete=ON")
        self._conn.executescript(_SCHEMA)

    def close(self) -> None:
        with self._lock:
            self._conn.close()

    def mint(
        self,
        kind: str,
        exchanges: int,
        payment_id: str,
        count: int = 1,
        *,
        daily_ceiling: int | None = None,
        prepared: list[str] | None = None,
    ) -> list[str]:
        """Makes the codes for one payment and returns them in plain form, the
        only moment they exist outside a person's hands. Raises AlreadyMinted
        for a payment that has codes, PaymentVoided for one refunded first.

        prepared: codes the caller generated and has already put somewhere
        safe, so a crash between the two steps loses nothing. The payment's
        reconciliation counts commit in the same transaction as its codes."""
        if kind not in KINDS:
            raise ValueError(f"unknown kind {kind!r}")
        if not isinstance(exchanges, int) or not 0 < exchanges <= MAX_EXCHANGES_PER_CODE:
            raise ValueError("exchanges out of range")
        if not payment_id:
            raise ValueError("payment_id is required")
        if kind == "batch":
            if not 1 <= count <= MAX_BATCH_COUNT:
                raise ValueError("batch count out of range")
        elif count != 1:
            raise ValueError(f"a {kind} purchase makes exactly one code")
        if prepared is not None and (
            len(prepared) != count or len(set(prepared)) != count or any(codes.normalize(c) != c for c in prepared)
        ):
            raise ValueError("prepared codes must be distinct, well-formed, and as many as the purchase makes")
        ceiling = None
        if kind == "group":
            ceiling = daily_ceiling if daily_ceiling is not None else self._group_daily_ceiling
            if ceiling <= 0:
                raise ValueError("daily ceiling must be positive")
        with self._lock:
            self._conn.execute("BEGIN IMMEDIATE")
            try:
                if self._conn.execute("SELECT 1 FROM voided_payments WHERE payment_id = ?", (payment_id,)).fetchone():
                    raise PaymentVoided(payment_id)
                if self._conn.execute("SELECT 1 FROM meter WHERE payment_id = ? LIMIT 1", (payment_id,)).fetchone():
                    raise AlreadyMinted(payment_id)
                today = self._clock().isoformat()
                made: list[str] = []
                while len(made) < count:
                    code = prepared[len(made)] if prepared is not None else codes.generate()
                    inserted = self._conn.execute(
                        "INSERT OR IGNORE INTO meter (code_hash, kind, exchanges_total, payment_id, day_created, daily_ceiling)"
                        " VALUES (?, ?, ?, ?, ?, ?)",
                        (codes.hash_code(code), kind, exchanges, payment_id, today, ceiling),
                    ).rowcount
                    if inserted:
                        made.append(code)
                    elif prepared is not None:
                        raise ValueError("a prepared code is already in the meter")
                self._conn.execute("INSERT OR IGNORE INTO reconcile (day) VALUES (?)", (today,))
                self._conn.execute(
                    "UPDATE reconcile SET payments_seen = payments_seen + 1, payments_minted = payments_minted + 1,"
                    " codes_minted = codes_minted + ? WHERE day = ?",
                    (count, today),
                )
                self._conn.execute("COMMIT")
            except BaseException:
                self._conn.execute("ROLLBACK")
                raise
        logger.info("minted kind=%s codes=%d exchanges=%d", kind, len(made), exchanges)
        return made

    def _row(self, code_hash: str):
        return self._conn.execute(
            "SELECT code_hash, kind, exchanges_total, exchanges_used, status, daily_ceiling FROM meter WHERE code_hash = ?",
            (code_hash,),
        ).fetchone()

    def _lookup(self, raw: str | None):
        """The row for a typed code, found by hash and then compared in
        constant time. A malformed code costs the same work as a wrong one."""
        code = codes.normalize(raw)
        candidate = codes.hash_code(code if code is not None else "-" * codes.CODE_LENGTH)
        if code is None:
            return None
        row = self._row(candidate)
        if row is None or not codes.hashes_match(row[0], candidate):
            return None
        return row

    def verify(self, code: str | None) -> bool:
        with self._lock:
            row = self._lookup(code)
        return row is not None and row[4] == LIVE and row[3] < row[2]

    def status(self, code: str | None) -> CodeStatus | None:
        with self._lock:
            row = self._lookup(code)
        if row is None:
            return None
        return CodeStatus(kind=row[1], status=row[4], exchanges_total=row[2], exchanges_used=row[3], daily_ceiling=row[5])

    def reserve(self, code: str | None) -> Admission:
        """Holds one exchange, or says why not. Reasons: paused, unknown, void,
        spent, in_use (every remaining exchange is already held by a sitting in
        flight), daily_ceiling (a group code's day is full)."""
        with self._lock:
            if self.is_paused():
                return Admission(False, "paused")
            row = self._lookup(code)
            if row is None:
                return Admission(False, "unknown")
            code_hash, _kind, total, used, status, ceiling = row
            if status == VOID:
                return Admission(False, "void")
            if used >= total:
                return Admission(False, "spent")
            held = self._reserved.get(code_hash, 0)
            if total - used - held <= 0:
                return Admission(False, "in_use")
            today = self._clock().isoformat()
            if ceiling is not None and self._used_today(code_hash, today) + held >= ceiling:
                return Admission(False, "daily_ceiling")
            self._reserved[code_hash] = held + 1
            return Admission(True, reservation=Reservation(code_hash, today), remaining=total - used)

    def _used_today(self, code_hash: str, today: str) -> int:
        day, count = self._day_used.get(code_hash, (today, 0))
        return count if day == today else 0

    def settle(self, reservation: Reservation, ok: bool) -> int | None:
        """Spends the held exchange when ok, returns it when not. Returns what
        the code has left, or None if the code was voided while held."""
        with self._lock:
            if reservation.done:
                return None
            reservation.done = True
            held = self._reserved.get(reservation.code_hash, 0) - 1
            if held > 0:
                self._reserved[reservation.code_hash] = held
            else:
                self._reserved.pop(reservation.code_hash, None)
            if not ok:
                row = self._row(reservation.code_hash)
                return None if row is None or row[4] == VOID else row[2] - row[3]
            today = self._clock()
            updated = self._conn.execute(
                "UPDATE meter SET exchanges_used = exchanges_used + 1, week_last_used = ?,"
                " status = CASE WHEN exchanges_used + 1 >= exchanges_total THEN 'spent' ELSE status END"
                " WHERE code_hash = ? AND status != 'void' AND exchanges_used < exchanges_total",
                (week_of(today), reservation.code_hash),
            ).rowcount
            if not updated:
                return None
            day, count = self._day_used.get(reservation.code_hash, (today.isoformat(), 0))
            self._day_used[reservation.code_hash] = (day, count + 1) if day == today.isoformat() else (today.isoformat(), 1)
            row = self._row(reservation.code_hash)
            return row[2] - row[3]

    def release(self, reservation: Reservation) -> None:
        self.settle(reservation, False)

    def void(self, payment_id: str) -> int:
        """Voids every code the payment made, and remembers the payment so a
        completion event arriving after its refund makes none."""
        with self._lock:
            week = week_of(self._clock())
            self._conn.execute("INSERT OR IGNORE INTO voided_payments (payment_id, week_voided) VALUES (?, ?)", (payment_id, week))
            changed = self._conn.execute(
                "UPDATE meter SET status = 'void', week_last_used = ? WHERE payment_id = ? AND status != 'void'",
                (week, payment_id),
            ).rowcount
        logger.info("voided codes=%d", changed)
        return changed

    def payment_minted(self, payment_id: str) -> bool:
        with self._lock:
            return self._conn.execute("SELECT 1 FROM meter WHERE payment_id = ? LIMIT 1", (payment_id,)).fetchone() is not None

    def payment_voided(self, payment_id: str) -> bool:
        with self._lock:
            return self._conn.execute("SELECT 1 FROM voided_payments WHERE payment_id = ?", (payment_id,)).fetchone() is not None

    def pause(self, on: bool) -> None:
        with self._lock:
            self._conn.execute(
                "INSERT INTO state (key, value) VALUES ('paused', ?) ON CONFLICT (key) DO UPDATE SET value = excluded.value",
                ("1" if on else "0",),
            )
        logger.warning("codes %s", "paused" if on else "unpaused")

    def is_paused(self) -> bool:
        with self._lock:
            row = self._conn.execute("SELECT value FROM state WHERE key = 'paused'").fetchone()
        return bool(row) and row[0] == "1"

    def tally(self, field: str, amount: int = 1) -> None:
        """Adds to today's reconciliation count. The counts are daily totals
        with no key beyond the day."""
        if field not in TALLY_FIELDS:
            raise ValueError(f"unknown tally {field!r}")
        day = self._clock().isoformat()
        with self._lock:
            self._conn.execute("INSERT OR IGNORE INTO reconcile (day) VALUES (?)", (day,))
            self._conn.execute(f"UPDATE reconcile SET {field} = {field} + ? WHERE day = ?", (amount, day))

    def reconciliation(self, days: int = 7) -> list[dict]:
        """Payments seen against payments that made codes, newest day first.
        gap is what is still owed: seen, minus minted, minus refunded first."""
        with self._lock:
            rows = self._conn.execute(
                f"SELECT day, {', '.join(TALLY_FIELDS)} FROM reconcile ORDER BY day DESC LIMIT ?", (days,)
            ).fetchall()
        report = []
        for day, *counts in rows:
            entry = {"day": day, **dict(zip(TALLY_FIELDS, counts))}
            entry["gap"] = entry["payments_seen"] - entry["payments_minted"] - entry["payments_voided_first"]
            report.append(entry)
        return report

    def purge(self) -> int:
        """Deletes spent and void rows 30 days after the end of the week they
        were last used, and the void memory on the same rule."""
        today = self._clock()
        cutoff = today - timedelta(days=RETENTION_DAYS)
        removed = 0
        with self._lock:
            for table, week_column, where in (
                ("meter", "week_last_used", "status IN ('spent', 'void') AND week_last_used IS NOT NULL"),
                ("voided_payments", "week_voided", "1"),
            ):
                key = "code_hash" if table == "meter" else "payment_id"
                rows = self._conn.execute(f"SELECT {key}, {week_column} FROM {table} WHERE {where}").fetchall()
                for key_value, week in rows:
                    if _end_of_week(week) <= cutoff:
                        self._conn.execute(f"DELETE FROM {table} WHERE {key} = ?", (key_value,))
                        removed += 1
            removed += self._conn.execute(
                "DELETE FROM reconcile WHERE day <= ?", ((today - timedelta(days=RECONCILE_RETENTION_DAYS)).isoformat(),)
            ).rowcount
        return removed
