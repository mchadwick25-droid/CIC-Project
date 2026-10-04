"""The meter: what each code holds and how much of it is spent.

The meter keys on a hash of the code. It stores no session id, visitor id,
session-code hash, IP address, name, email or text, and no timestamp finer
than a day: the day a code was made and the week it was last used. It keeps
the Stripe payment id, so a refund or dispute can void a code and a sponsor's
batch can be voided in one step.

One table holds a visitor-derived value by ruling: the free allowance keeps,
for each visitor in a free window, a keyed hash of the visitor key, the day the
window began and the amount drawn. The key for that hash comes from the
server's environment and is never written to this file, so the file alone
cannot be matched to a visitor and an address cannot be recovered from it.

Admission reserves a turn's tokens before the voice speaks; settling spends them,
releasing returns them. Reservations live in memory only, so a restart gives
every in-flight reservation back and nobody pays for a turn that never
finished. One process serves all traffic, so the lock below is the arbiter.
"""
import hashlib
import hmac
import logging
import secrets
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
MEASURE_RETENTION_DAYS = 90
REFUSAL_REASONS = (
    "no_code", "code_not_accepted", "spent", "too_few", "daily_ceiling", "paused", "in_use",
    "free_rounds_done", "free_allowance_spent", "door_free_closed", "door_paid_closed", "paid_round_cap",
)
SUM_MEASURES = (
    "codes_single", "codes_batch", "codes_group", "tokens_sold", "tokens_spent",
    *(f"refused_{reason}" for reason in REFUSAL_REASONS),
    "observed_free_refused", "observed_paid_refused",
)
MAX_MEASURES = ("door_stage", "door_ratio_permille", "door_spend_cents")
FUNDS_KINDS = ("gift", "purchase", "adjustment")
FUNDS_RETENTION_DAYS = 90
MAX_FUNDS_CENTS = 10_000_000
MAX_NOTE_CHARS = 200

MAX_TOKENS_PER_CODE = 1_000_000
MAX_BATCH_COUNT = 1_000
RETENTION_DAYS = 30
DEFAULT_FREE_WINDOW_DAYS = 30

_SCHEMA = """
CREATE TABLE IF NOT EXISTS meter (
    code_hash TEXT PRIMARY KEY,
    kind TEXT NOT NULL CHECK (kind IN ('single', 'batch', 'group')),
    tokens_total INTEGER NOT NULL CHECK (tokens_total > 0),
    tokens_used INTEGER NOT NULL DEFAULT 0 CHECK (tokens_used >= 0 AND tokens_used <= tokens_total),
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
CREATE TABLE IF NOT EXISTS funds (
    entry TEXT PRIMARY KEY,
    day TEXT NOT NULL,
    kind TEXT NOT NULL CHECK (kind IN ('gift', 'purchase', 'adjustment')),
    cents INTEGER NOT NULL CHECK (cents != 0),
    payment_id TEXT UNIQUE,
    note TEXT,
    reversed INTEGER NOT NULL DEFAULT 0
) WITHOUT ROWID;
CREATE TABLE IF NOT EXISTS daily (
    day TEXT NOT NULL,
    measure TEXT NOT NULL,
    total INTEGER NOT NULL,
    PRIMARY KEY (day, measure)
) WITHOUT ROWID;
CREATE TABLE IF NOT EXISTS free_window (
    key_hash TEXT PRIMARY KEY,
    first_day TEXT NOT NULL,
    spent INTEGER NOT NULL CHECK (spent >= 0)
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
    tokens_total: int
    tokens_used: int
    daily_ceiling: int | None

    @property
    def remaining(self) -> int:
        return 0 if self.status == VOID else self.tokens_total - self.tokens_used


class Reservation:
    """Tokens held against a code for one turn. Carries the code's hash, never the code."""

    __slots__ = ("code_hash", "day", "count", "done")

    def __init__(self, code_hash: str, day: str, count: int = 1):
        self.code_hash = code_hash
        self.day = day
        self.count = count
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
        free_window_days: int = DEFAULT_FREE_WINDOW_DAYS,
        free_key: bytes | None = None,
    ):
        self._clock = clock
        self._free_secret = free_key if free_key is not None else secrets.token_bytes(32)
        self._free_window_days = free_window_days
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
        tokens: int,
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
        if not isinstance(tokens, int) or not 0 < tokens <= MAX_TOKENS_PER_CODE:
            raise ValueError("tokens out of range")
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
                        "INSERT OR IGNORE INTO meter (code_hash, kind, tokens_total, payment_id, day_created, daily_ceiling)"
                        " VALUES (?, ?, ?, ?, ?, ?)",
                        (codes.hash_code(code), kind, tokens, payment_id, today, ceiling),
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
                self._count(f"codes_{kind}", count, today)
                self._count("tokens_sold", tokens * count, today)
                self._conn.execute("COMMIT")
            except BaseException:
                self._conn.execute("ROLLBACK")
                raise
        logger.info("minted kind=%s codes=%d tokens=%d", kind, len(made), tokens)
        return made

    def _row(self, code_hash: str):
        return self._conn.execute(
            "SELECT code_hash, kind, tokens_total, tokens_used, status, daily_ceiling FROM meter WHERE code_hash = ?",
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
        return CodeStatus(kind=row[1], status=row[4], tokens_total=row[2], tokens_used=row[3], daily_ceiling=row[5])

    def reserve(self, code: str | None, count: int = 1) -> Admission:
        """Holds count tokens (what the turn would draw),
        or says why not. Reasons: paused, unknown, void, spent, insufficient
        (fewer than count remain), in_use (the rest are held by sittings in
        flight), daily_ceiling (a group code's day is full)."""
        if count < 1:
            raise ValueError("count must be at least 1")
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
            if total - used < count:
                return Admission(False, "insufficient")
            held = self._reserved.get(code_hash, 0)
            if total - used - held < count:
                return Admission(False, "in_use")
            today = self._clock().isoformat()
            if ceiling is not None and self._used_today(code_hash, today) + held + count > ceiling:
                return Admission(False, "daily_ceiling")
            self._reserved[code_hash] = held + count
            return Admission(True, reservation=Reservation(code_hash, today, count), remaining=total - used)

    def _used_today(self, code_hash: str, today: str) -> int:
        day, count = self._day_used.get(code_hash, (today, 0))
        return count if day == today else 0

    def settle(self, reservation: Reservation, ok: bool) -> int | None:
        """Spends the held tokens when ok, returns it when not. Returns what
        the code has left, or None if the code was voided while held."""
        with self._lock:
            if reservation.done:
                return None
            reservation.done = True
            held = self._reserved.get(reservation.code_hash, 0) - reservation.count
            if held > 0:
                self._reserved[reservation.code_hash] = held
            else:
                self._reserved.pop(reservation.code_hash, None)
            if not ok:
                row = self._row(reservation.code_hash)
                return None if row is None or row[4] == VOID else row[2] - row[3]
            today = self._clock()
            updated = self._conn.execute(
                "UPDATE meter SET tokens_used = tokens_used + ?, week_last_used = ?,"
                " status = CASE WHEN tokens_used + ? >= tokens_total THEN 'spent' ELSE status END"
                " WHERE code_hash = ? AND status != 'void' AND tokens_used + ? <= tokens_total",
                (reservation.count, week_of(today), reservation.count, reservation.code_hash, reservation.count),
            ).rowcount
            if not updated:
                return None
            day, count = self._day_used.get(reservation.code_hash, (today.isoformat(), 0))
            self._day_used[reservation.code_hash] = (
                (day, count + reservation.count) if day == today.isoformat() else (today.isoformat(), reservation.count)
            )
            self._count("tokens_spent", reservation.count, today.isoformat())
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

    def set_state(self, key: str, value: str) -> None:
        """Keeps one named value that must survive a restart (the pause, the door's last stage)."""
        with self._lock:
            self._conn.execute(
                "INSERT INTO state (key, value) VALUES (?, ?) ON CONFLICT (key) DO UPDATE SET value = excluded.value", (key, value)
            )

    def get_state(self, key: str) -> str | None:
        with self._lock:
            row = self._conn.execute("SELECT value FROM state WHERE key = ?", (key,)).fetchone()
        return row[0] if row else None

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

    def today(self) -> date:
        return self._clock()

    def free_key(self, visitor: str) -> str:
        """The free allowance's row key for a visitor key: a keyed hash under a
        secret that comes from the server's environment and is never written to
        this file. Without a secret given, one is made for this process only, so
        what was drawn is not remembered across a restart (tests and local use)."""
        return hmac.new(self._free_secret, visitor.encode("utf-8"), hashlib.sha256).hexdigest()[:32]

    def free_window_spent(self, key_hash: str) -> int:
        """What this key has drawn in its current window; 0 once the window has ended."""
        with self._lock:
            row = self._conn.execute("SELECT first_day, spent FROM free_window WHERE key_hash = ?", (key_hash,)).fetchone()
        if row is None or self._window_ended(row[0]):
            return 0
        return row[1]

    def free_window_spend(self, key_hash: str, amount: int) -> None:
        """Adds a settled draw. A key's first draw starts its window, and a
        draw after the window has ended starts a new one."""
        today = self._clock().isoformat()
        with self._lock:
            row = self._conn.execute("SELECT first_day, spent FROM free_window WHERE key_hash = ?", (key_hash,)).fetchone()
            if row is None or self._window_ended(row[0]):
                self._conn.execute(
                    "INSERT INTO free_window (key_hash, first_day, spent) VALUES (?, ?, ?)"
                    " ON CONFLICT (key_hash) DO UPDATE SET first_day = excluded.first_day, spent = excluded.spent",
                    (key_hash, today, amount),
                )
            else:
                self._conn.execute("UPDATE free_window SET spent = spent + ? WHERE key_hash = ?", (amount, key_hash))

    def _window_ended(self, first_day: str) -> bool:
        return self._clock() >= date.fromisoformat(first_day) + timedelta(days=self._free_window_days)

    def owed(self) -> list[dict]:
        """What each payment still holds in unspent tokens, for refunds at a
        switch-off. By Stripe payment id, which the meter already keeps; the
        codes themselves stay hashed and nothing here names a person."""
        with self._lock:
            rows = self._conn.execute(
                "SELECT payment_id, kind, COUNT(*), SUM(tokens_total), SUM(tokens_used), MIN(day_created)"
                " FROM meter WHERE status != 'void' GROUP BY payment_id ORDER BY MIN(day_created), payment_id"
            ).fetchall()
        return [
            {"payment_id": pid, "kind": kind, "codes": codes_n, "tokens_bought": total, "tokens_left": total - used, "day_bought": day}
            for pid, kind, codes_n, total, used, day in rows
            if total - used > 0
        ]

    def _add(self, measure: str, amount: int, day: str) -> None:
        self._conn.execute(
            "INSERT INTO daily (day, measure, total) VALUES (?, ?, ?)"
            " ON CONFLICT (day, measure) DO UPDATE SET total = total + excluded.total",
            (day, measure, amount),
        )

    def _count(self, measure: str, amount: int, day: str) -> None:
        """A measure written beside real work: if it fails, the work stands."""
        try:
            self._add(measure, amount, day)
        except Exception:  # noqa: BLE001 - a count must never undo or block a purchase or a spend
            logger.exception("could not count %s", measure)

    def measure(self, name: str, amount: int = 1) -> None:
        """Adds to today's total for one measure. The totals are one number per
        measure per day: no code, no visitor, no time of day."""
        if name not in SUM_MEASURES:
            raise ValueError(f"unknown measure {name!r}")
        with self._lock:
            self._add(name, amount, self._clock().isoformat())

    def measure_peak(self, name: str, value: int) -> None:
        """Keeps today's highest value for a measure that is a level, not a count."""
        if name not in MAX_MEASURES:
            raise ValueError(f"unknown measure {name!r}")
        with self._lock:
            self._conn.execute(
                "INSERT INTO daily (day, measure, total) VALUES (?, ?, ?)"
                " ON CONFLICT (day, measure) DO UPDATE SET total = MAX(total, excluded.total)",
                (self._clock().isoformat(), name, value),
            )

    def measures(self, days: int = 14) -> list[dict]:
        """Daily totals, newest day first; a measure with nothing that day reads 0."""
        since = (self._clock() - timedelta(days=days - 1)).isoformat()
        with self._lock:
            rows = self._conn.execute("SELECT day, measure, total FROM daily WHERE day >= ?", (since,)).fetchall()
        by_day: dict[str, dict[str, int]] = {}
        for day, name, total in rows:
            by_day.setdefault(day, {})[name] = total
        return [
            {"day": day, **{name: by_day[day].get(name, 0) for name in (*SUM_MEASURES, *MAX_MEASURES)}}
            for day in sorted(by_day, reverse=True)
        ]

    def add_funds(self, kind: str, cents: int, payment_id: str | None = None, note: str | None = None) -> str | None:
        """Records money that raises the door's ceiling: a gift or a go-deeper
        purchase from Stripe (keyed by its payment id, so a replayed event adds
        nothing and a payment refunded first adds nothing), or an adjustment by
        hand. Returns the entry's id (random, so the order entries were made in is
        not kept), or None when nothing was added."""
        if kind not in FUNDS_KINDS:
            raise ValueError(f"unknown kind {kind!r}")
        if isinstance(cents, bool) or not isinstance(cents, int) or cents == 0 or abs(cents) > MAX_FUNDS_CENTS:
            raise ValueError("cents out of range")
        if kind != "adjustment" and cents < 0:
            raise ValueError("only an adjustment can be negative")
        if kind != "adjustment" and not payment_id:
            raise ValueError("a gift or purchase needs its payment id")
        if note is not None and (not isinstance(note, str) or len(note) > MAX_NOTE_CHARS):
            raise ValueError("note too long")
        with self._lock:
            if payment_id is not None:
                if self._conn.execute("SELECT 1 FROM funds WHERE payment_id = ?", (payment_id,)).fetchone():
                    return None
                if self._conn.execute("SELECT 1 FROM voided_payments WHERE payment_id = ?", (payment_id,)).fetchone():
                    return None
            entry = secrets.token_hex(6)
            self._conn.execute(
                "INSERT INTO funds (entry, day, kind, cents, payment_id, note) VALUES (?, ?, ?, ?, ?, ?)",
                (entry, self._clock().isoformat(), kind, cents, payment_id, note),
            )
            return entry

    def reverse_funds(self, entry_id: str) -> bool:
        """Takes one entry back out of the sum. It stays on the page as reversed."""
        with self._lock:
            return self._conn.execute("UPDATE funds SET reversed = 1 WHERE entry = ? AND reversed = 0", (entry_id,)).rowcount == 1

    def void_funds(self, payment_id: str) -> int:
        """A refund or dispute takes a payment's money back out of the sum."""
        with self._lock:
            return self._conn.execute("UPDATE funds SET reversed = 1 WHERE payment_id = ? AND reversed = 0", (payment_id,)).rowcount

    def net_funds(self, days: int = 7) -> dict[str, int]:
        """What came in over the last `days` days (today included), by kind, in cents."""
        since = (self._clock() - timedelta(days=days - 1)).isoformat()
        with self._lock:
            rows = self._conn.execute(
                "SELECT kind, SUM(cents) FROM funds WHERE reversed = 0 AND day >= ? GROUP BY kind", (since,)
            ).fetchall()
        totals = {kind: 0 for kind in FUNDS_KINDS}
        totals.update({kind: total for kind, total in rows})
        return totals

    def list_funds(self, days: int = 14) -> list[dict]:
        """The entries behind the sum, newest day first, for the one person who sets the base number."""
        since = (self._clock() - timedelta(days=days - 1)).isoformat()
        with self._lock:
            rows = self._conn.execute(
                "SELECT entry, day, kind, cents, note, reversed FROM funds WHERE day >= ? ORDER BY day DESC", (since,)
            ).fetchall()
        return [dict(zip(("id", "day", "kind", "cents", "note", "reversed"), row)) for row in rows]

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
            removed += self._conn.execute(
                "DELETE FROM free_window WHERE first_day <= ?", ((today - timedelta(days=self._free_window_days)).isoformat(),)
            ).rowcount
            removed += self._conn.execute(
                "DELETE FROM daily WHERE day <= ?", ((today - timedelta(days=MEASURE_RETENTION_DAYS)).isoformat(),)
            ).rowcount
            removed += self._conn.execute(
                "DELETE FROM funds WHERE day <= ?", ((today - timedelta(days=FUNDS_RETENTION_DAYS)).isoformat(),)
            ).rowcount
        return removed
