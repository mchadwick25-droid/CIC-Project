"""The session event log store (Artifact-3 SS1). DECIDED default is managed
Postgres (single primary, PITR enabled) - that's an infra/deployment
decision (Artifact-6 SS3 topology: RDS Postgres) this build thread doesn't
need to make today to build and prove the log's actual guarantees
(ordering, idempotency, "any instance can serve any session"). SQLite here
is a DECIDABLE dev/test stand-in, same pattern as M2's placeholder FAISS
vectors: the schema below is deliberately close to Artifact-3's Postgres DDL
so the guarantees it proves carry over, not a reason to skip the real
Postgres wiring at deployment (stage 6-ish).

No process-local session state beyond this store (Artifact-3 SS1: "any
instance can serve any session") - Store is stateless except for its
connection; nothing here caches a session in memory between calls.
"""
import json
import sqlite3
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

DDL = """
CREATE TABLE IF NOT EXISTS session_events (
  session_id  TEXT    NOT NULL,
  seq         INTEGER NOT NULL,
  event_uuid  TEXT    NOT NULL UNIQUE,
  event_type  TEXT    NOT NULL,
  payload     TEXT    NOT NULL,
  created_at  TEXT    NOT NULL,
  PRIMARY KEY (session_id, seq)
);
"""

MAX_APPEND_RETRIES = 3  # Artifact-3 SS1: "re-read and retry (bounded, 3x)"


@dataclass(frozen=True)
class StoredEvent:
    session_id: str
    seq: int
    event_uuid: str
    event_type: str
    payload: dict
    created_at: str


class ConcurrentWriteExhausted(Exception):
    """Raised when MAX_APPEND_RETRIES concurrent-writer collisions occur in
    a row - a real condition under real concurrency, never silently retried
    forever (Build-Blueprint.md's fail-open-never-silently ethic applies to
    infrastructure code as much as to the safety gate)."""


class Store:
    """One instance per call, cheap to construct, holds no session state -
    this is what makes 'any instance can serve any session' true rather
    than aspirational. Two independent Store instances against the same
    database file behave exactly like two separate runtime processes."""

    def __init__(self, db_path: str | Path):
        self.db_path = str(db_path)
        self._init_schema()

    def _connect(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path, timeout=5.0)
        conn.execute("PRAGMA journal_mode=WAL")
        return conn

    def _init_schema(self) -> None:
        with self._connect() as conn:
            conn.executescript(DDL)

    def append(self, *, session_id: str, event_uuid: str, event_type: str, payload: dict) -> int:
        """Returns the event's seq. Idempotent on event_uuid: a retried
        append with the same event_uuid is a silent success returning the
        original seq, never a duplicate row (Artifact-3 SS1)."""
        with self._connect() as conn:
            existing = conn.execute(
                "SELECT session_id, seq FROM session_events WHERE event_uuid = ?", (event_uuid,)
            ).fetchone()
            if existing:
                existing_session_id, existing_seq = existing
                if existing_session_id != session_id:
                    raise ValueError(f"event_uuid {event_uuid} already used by a different session")
                return existing_seq

            for _ in range(MAX_APPEND_RETRIES):
                row = conn.execute(
                    "SELECT COALESCE(MAX(seq), 0) FROM session_events WHERE session_id = ?", (session_id,)
                ).fetchone()
                next_seq = row[0] + 1
                try:
                    conn.execute(
                        "INSERT INTO session_events (session_id, seq, event_uuid, event_type, payload, created_at) "
                        "VALUES (?, ?, ?, ?, ?, ?)",
                        (
                            session_id,
                            next_seq,
                            event_uuid,
                            event_type,
                            json.dumps(payload, sort_keys=True),
                            datetime.now(timezone.utc).isoformat(),
                        ),
                    )
                    conn.commit()
                    return next_seq
                except sqlite3.IntegrityError:
                    continue  # concurrent writer took this seq - re-read and retry
            raise ConcurrentWriteExhausted(f"session {session_id}: {MAX_APPEND_RETRIES} seq collisions in a row")

    def read_events(self, session_id: str) -> list[StoredEvent]:
        with self._connect() as conn:
            rows = conn.execute(
                "SELECT session_id, seq, event_uuid, event_type, payload, created_at "
                "FROM session_events WHERE session_id = ? ORDER BY seq ASC",
                (session_id,),
            ).fetchall()
        return [
            StoredEvent(
                session_id=r[0], seq=r[1], event_uuid=r[2], event_type=r[3], payload=json.loads(r[4]), created_at=r[5]
            )
            for r in rows
        ]
