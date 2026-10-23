"""The feedback store: what participants say from inside the conversation and
from the site. A separate SQLite file, sharing no key with the event log.

A row is a pointer, never conversation text: the session, the turn and
sentence indexes, the record ids and confidence tags behind that sentence, a
reason from a fixed set, and the optional line the person typed. A like is
one row per session and turn. A comment names the page it was left on. A page
like and a page report carry the page and no session, turn or record id.

A waiting item is a flag, a comment or a report waiting for a person. Closing it records
one of five outcomes and clears the email, so a contact address never outlives
the reply it was left for. A like needs no answer: it is never in the queue and
is deleted with the conversations it points to. Closed items older than the
retention window are deleted.
"""
import json
import sqlite3
import uuid
from datetime import datetime, timedelta, timezone
from pathlib import Path

from engine import sqlite_scrub as scrub

KINDS = ("like", "flag", "comment", "report")
REASONS = ("fact_wrong", "source_mismatch", "overcertain", "unclear", "accuracy", "craft")
QUOTE_CONSENTS = ("no", "anonymous", "first_name")
OUTCOMES = ("corrected", "checked_stands", "open_lead", "conviction", "no_action")
CLOSED_RETENTION_DAYS = 90

_TABLE = f"""
CREATE TABLE {{name}} (
  id            TEXT PRIMARY KEY,
  kind          TEXT NOT NULL CHECK (kind IN {KINDS!r}),
  created_at    TEXT NOT NULL,
  page          TEXT,
  session_id    TEXT,
  turn_index    INTEGER,
  sentence_index INTEGER,
  record_ids    TEXT NOT NULL DEFAULT '[]',
  confidence    TEXT,
  reason        TEXT CHECK (reason IS NULL OR reason IN {REASONS!r}),
  text          TEXT,
  quote_consent TEXT CHECK (quote_consent IS NULL OR quote_consent IN {QUOTE_CONSENTS!r}),
  first_name    TEXT,
  email         TEXT,
  outcome       TEXT CHECK (outcome IS NULL OR outcome IN {OUTCOMES!r}),
  outcome_note  TEXT,
  closed_at     TEXT
)"""
_LIKE_INDEX = "CREATE INDEX IF NOT EXISTS feedback_like_idx ON feedback (session_id, turn_index) WHERE kind = 'like'"

_COLUMNS = (
    "id", "kind", "created_at", "page", "session_id", "turn_index", "sentence_index", "record_ids", "confidence",
    "reason", "text", "quote_consent", "first_name", "email", "outcome", "outcome_note", "closed_at",
)


def _item(row) -> dict:
    item = dict(zip(_COLUMNS, row))
    item["record_ids"] = json.loads(item["record_ids"] or "[]")
    item["confidence"] = json.loads(item["confidence"]) if item["confidence"] else None
    return item


class FeedbackStore:
    def __init__(self, db_path: str | Path):
        self.db_path = str(db_path)
        conn = self._connect()
        try:
            self._ensure_schema(conn)
        finally:
            conn.close()

    @staticmethod
    def _ensure_schema(conn: sqlite3.Connection) -> None:
        """Creates the table, or rebuilds one made before the page-level kind
        and reasons existed: rows are copied across unchanged, then the
        indexes are made again. Safe to run on every start."""
        conn.isolation_level = None
        conn.execute("BEGIN IMMEDIATE")
        try:
            row = conn.execute("SELECT sql FROM sqlite_master WHERE type = 'table' AND name = 'feedback'").fetchone()
            if row is None:
                conn.execute(_TABLE.format(name="feedback"))
            elif "'report'" not in row[0] or "'craft'" not in row[0]:
                conn.execute("DROP TABLE IF EXISTS feedback_rebuilt")
                conn.execute(_TABLE.format(name="feedback_rebuilt"))
                columns = ", ".join(_COLUMNS)
                conn.execute(f"INSERT INTO feedback_rebuilt ({columns}) SELECT {columns} FROM feedback")
                conn.execute("DROP TABLE feedback")
                conn.execute("ALTER TABLE feedback_rebuilt RENAME TO feedback")
            conn.execute(_LIKE_INDEX)
            conn.execute("COMMIT")
        except BaseException:
            conn.execute("ROLLBACK")
            raise

    def _connect(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path, timeout=5.0)
        conn.execute("PRAGMA journal_mode=WAL")
        conn.execute("PRAGMA secure_delete=ON")
        return conn

    def add(self, record: dict) -> str:
        """Stores one item and returns its id. `record` carries the fields of
        the table; anything missing is stored empty."""
        item_id = str(uuid.uuid4())
        confidence = record.get("confidence")
        with self._connect() as conn:
            conn.execute(
                f"INSERT INTO feedback ({', '.join(_COLUMNS[:14])}) VALUES ({', '.join('?' * 14)})",
                (
                    item_id, record["kind"], datetime.now(timezone.utc).isoformat(), record.get("page"),
                    record.get("session_id"), record.get("turn_index"), record.get("sentence_index"),
                    json.dumps(list(record.get("record_ids") or [])),
                    json.dumps(confidence) if confidence is not None else None,
                    record.get("reason"), record.get("text"), record.get("quote_consent"), record.get("first_name"),
                    record.get("email"),
                ),
            )
        return item_id

    def like_id(self, session_id: str, turn_index: int) -> str | None:
        with self._connect() as conn:
            row = conn.execute(
                "SELECT id FROM feedback WHERE kind = 'like' AND session_id = ? AND turn_index = ?", (session_id, turn_index)
            ).fetchone()
        return row[0] if row else None

    def like_exists(self, session_id: str, turn_index: int) -> bool:
        return self.like_id(session_id, turn_index) is not None

    def get(self, item_id: str) -> dict | None:
        with self._connect() as conn:
            row = conn.execute(f"SELECT {', '.join(_COLUMNS)} FROM feedback WHERE id = ?", (item_id,)).fetchone()
        return _item(row) if row else None

    def list_open(self) -> list[dict]:
        with self._connect() as conn:
            rows = conn.execute(
                f"SELECT {', '.join(_COLUMNS)} FROM feedback WHERE closed_at IS NULL AND kind != 'like' ORDER BY created_at"
            ).fetchall()
        return [_item(r) for r in rows]

    def list_closed(self, limit: int = 200) -> list[dict]:
        with self._connect() as conn:
            rows = conn.execute(
                f"SELECT {', '.join(_COLUMNS)} FROM feedback WHERE closed_at IS NOT NULL ORDER BY closed_at DESC LIMIT ?",
                (limit,),
            ).fetchall()
        return [_item(r) for r in rows]

    def close(self, item_id: str, outcome: str, note: str | None) -> bool:
        """Records the outcome and the time, and clears the email. The first
        name stays, since it is only ever quoted with the person's consent.
        False when no waiting item has this id."""
        if outcome not in OUTCOMES:
            raise ValueError(f"unknown outcome {outcome!r}")
        with self._connect() as conn:
            cursor = conn.execute(
                "UPDATE feedback SET outcome = ?, outcome_note = ?, closed_at = ?, email = NULL "
                "WHERE id = ? AND closed_at IS NULL",
                (outcome, note, datetime.now(timezone.utc).isoformat(), item_id),
            )
        return cursor.rowcount == 1

    def delete_session(self, session_id: str) -> int:
        """Deletes every like, flag and comment that names a deleted conversation."""
        with self._connect() as conn:
            deleted = conn.execute("DELETE FROM feedback WHERE session_id = ?", (session_id,)).rowcount
            conn.commit()
            scrub.truncate_wal(conn)
            return deleted

    def purge_closed_older_than(self, days: int = CLOSED_RETENTION_DAYS, now: datetime | None = None) -> int:
        """Deletes closed items whose closing is older than `days`, and likes
        older than `days`. Open flags and comments stay until someone closes
        them."""
        cutoff = ((now or datetime.now(timezone.utc)) - timedelta(days=days)).isoformat()
        with self._connect() as conn:
            cursor = conn.execute(
                "DELETE FROM feedback WHERE (closed_at IS NOT NULL AND closed_at < ?) OR (kind = 'like' AND created_at < ?)",
                (cutoff, cutoff),
            )
        return cursor.rowcount
