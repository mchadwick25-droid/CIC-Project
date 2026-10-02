"""Conversation access units: free and paid grants, holds, captures, releases.

A unit is held when a conversation starts, captured when its first
Representative reply is stored, and released if no reply lands. Free units are
spent before paid ones. Holds are per conversation, never per message, so an
open conversation needs no ledger call to continue.
"""
import sqlite3
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone

FREE = "free"
PAID = "paid"


class LedgerError(Exception):
    pass


@dataclass(frozen=True)
class Admission:
    admitted: bool
    bucket: str | None
    reason: str


def _now(now: datetime | None) -> str:
    return (now or datetime.now(timezone.utc)).isoformat()


class Ledger:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn

    def _insert(
        self, visitor_id: str, kind: str, bucket: str, delta: int, *, session_id: str | None = None,
        purchase_id: str | None = None, source_ref: str | None = None, now: datetime | None = None,
    ) -> bool:
        try:
            self.conn.execute(
                "INSERT INTO access_ledger (visitor_id, kind, bucket, delta, session_id, purchase_id, source_ref, created_at)"
                " VALUES (?,?,?,?,?,?,?,?)",
                (visitor_id, kind, bucket, delta, session_id, purchase_id, source_ref, _now(now)),
            )
        except sqlite3.IntegrityError as exc:
            if "source_ref" in str(exc):
                return False
            raise
        return True

    def balance(self, visitor_id: str, bucket: str | None = None) -> int:
        sql = "SELECT COALESCE(SUM(delta), 0) FROM access_ledger WHERE visitor_id = ?"
        args: list = [visitor_id]
        if bucket is not None:
            sql += " AND bucket = ?"
            args.append(bucket)
        return int(self.conn.execute(sql, args).fetchone()[0])

    def grant_free(self, visitor_id: str, units: int, source_ref: str, now: datetime | None = None) -> bool:
        if units <= 0:
            raise LedgerError("units must be positive")
        return self._insert(visitor_id, "grant_free", FREE, units, source_ref=source_ref, now=now)

    def grant_paid(self, visitor_id: str, units: int, purchase_id: str, now: datetime | None = None) -> bool:
        if units <= 0:
            raise LedgerError("units must be positive")
        return self._insert(
            visitor_id, "grant_paid", PAID, units, purchase_id=purchase_id, source_ref=f"grant:{purchase_id}", now=now,
        )

    def reverse_paid(self, visitor_id: str, units: int, purchase_id: str, source_ref: str, now: datetime | None = None) -> bool:
        if units <= 0:
            raise LedgerError("units must be positive")
        return self._insert(visitor_id, "reverse", PAID, -units, purchase_id=purchase_id, source_ref=source_ref, now=now)

    def adjust_paid(self, visitor_id: str, units: int, purchase_id: str, source_ref: str, now: datetime | None = None) -> bool:
        if units == 0:
            raise LedgerError("units must not be zero")
        return self._insert(visitor_id, "adjust", PAID, units, purchase_id=purchase_id, source_ref=source_ref, now=now)

    def _hold_row(self, session_id: str):
        return self.conn.execute(
            "SELECT visitor_id, bucket FROM access_ledger WHERE kind = 'hold' AND session_id = ?", (session_id,),
        ).fetchone()

    def _settled(self, session_id: str) -> str | None:
        row = self.conn.execute(
            "SELECT kind FROM access_ledger WHERE session_id = ? AND kind IN ('capture','release')", (session_id,),
        ).fetchone()
        return row[0] if row else None

    def hold(self, visitor_id: str, session_id: str, now: datetime | None = None) -> Admission:
        """Reserves one unit for a new conversation. A visitor with no unit gets
        an Admission with admitted=False; no exception is raised, so the caller
        can route that visitor to a Facilitator-governed path."""
        self.conn.execute("BEGIN IMMEDIATE")
        try:
            existing = self._hold_row(session_id)
            if existing is not None:
                self.conn.execute("COMMIT")
                return Admission(True, existing[1], "already_held")
            bucket = FREE if self.balance(visitor_id, FREE) > 0 else PAID if self.balance(visitor_id, PAID) > 0 else None
            if bucket is None:
                self.conn.execute("COMMIT")
                return Admission(False, None, "no_balance")
            self._insert(visitor_id, "hold", bucket, -1, session_id=session_id, source_ref=f"hold:{session_id}", now=now)
            self.conn.execute("COMMIT")
            return Admission(True, bucket, "held")
        except Exception:
            self.conn.execute("ROLLBACK")
            raise

    def capture(self, session_id: str, now: datetime | None = None) -> bool:
        """Finalises the held unit once the first Representative reply is stored.
        Returns False when the session was already captured."""
        held = self._hold_row(session_id)
        if held is None:
            raise LedgerError(f"no hold for session {session_id}")
        settled = self._settled(session_id)
        if settled == "release":
            raise LedgerError(f"hold for session {session_id} was already released")
        return self._insert(held[0], "capture", held[1], 0, session_id=session_id, source_ref=f"capture:{session_id}", now=now)

    def release(self, session_id: str, now: datetime | None = None) -> bool:
        """Returns a held unit when no reply landed. Returns False when the
        session was already released."""
        held = self._hold_row(session_id)
        if held is None:
            raise LedgerError(f"no hold for session {session_id}")
        settled = self._settled(session_id)
        if settled == "capture":
            raise LedgerError(f"hold for session {session_id} was already captured")
        return self._insert(held[0], "release", held[1], 1, session_id=session_id, source_ref=f"release:{session_id}", now=now)

    def open_holds(self) -> list[tuple[str, str, str]]:
        rows = self.conn.execute(
            "SELECT h.session_id, h.visitor_id, h.created_at FROM access_ledger h WHERE h.kind = 'hold'"
            " AND NOT EXISTS (SELECT 1 FROM access_ledger s WHERE s.session_id = h.session_id AND s.kind IN ('capture','release'))"
            " ORDER BY h.id",
        ).fetchall()
        return [(r[0], r[1], r[2]) for r in rows]

    def release_idle_holds(self, older_than: timedelta, now: datetime | None = None) -> list[str]:
        current = now or datetime.now(timezone.utc)
        cutoff = current - older_than
        released = []
        for session_id, _visitor, created_at in self.open_holds():
            if datetime.fromisoformat(created_at) <= cutoff:
                self.release(session_id, now=current)
                released.append(session_id)
        return released
