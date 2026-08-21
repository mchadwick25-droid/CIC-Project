"""M8's usage-log store. SQLite dev/test stand-in - same DECIDABLE pattern
as engine.m4.store.Store (real deployment target is the same conversation
as M4's managed Postgres, Artifact-6 SS3). Append-only, one row per
UsageRecord - this is the thing per-session/per-participant attribution and
"zero unattributed calls" get checked AGAINST, not merely asserted about.

Deliberately a SEPARATE store from M4's session_events table, not a new
event type on it - M8 "owns: the truthful number" (CiC-Program-Spec.md
boundary rules), a distinct concern from M4's conversation state, and
mixing them would mean a cost query has to filter conversation events (or
vice versa) instead of just reading its own table.
"""
import json
import sqlite3
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path

from engine.provider.bedrock import NormalizedUsage

from .usage import UsageRecord

DDL = """
CREATE TABLE IF NOT EXISTS usage_log (
  trace_id    TEXT NOT NULL UNIQUE,
  session_id  TEXT NOT NULL,
  call_kind   TEXT NOT NULL,
  model_id    TEXT NOT NULL,
  provider    TEXT NOT NULL,
  usage_json  TEXT NOT NULL,
  created_at  TEXT NOT NULL
);
"""


def _row_to_record(row) -> UsageRecord:
    trace_id, session_id, call_kind, model_id, provider, usage_json, _created_at = row
    usage_dict = json.loads(usage_json)
    return UsageRecord(
        trace_id=trace_id, session_id=session_id, call_kind=call_kind, model_id=model_id, provider=provider, usage=NormalizedUsage(**usage_dict)
    )


class UsageLogStore:
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

    def append(self, record: UsageRecord) -> None:
        """Idempotent on trace_id, same discipline as engine.m4.store.Store
        on event_uuid - a retried append is a silent success, never a
        duplicate row."""
        with self._connect() as conn:
            conn.execute(
                "INSERT OR IGNORE INTO usage_log (trace_id, session_id, call_kind, model_id, provider, usage_json, created_at) "
                "VALUES (?, ?, ?, ?, ?, ?, ?)",
                (
                    record.trace_id,
                    record.session_id,
                    record.call_kind,
                    record.model_id,
                    record.provider,
                    json.dumps(asdict(record.usage)),
                    datetime.now(timezone.utc).isoformat(),
                ),
            )
            conn.commit()

    def read_all(self) -> list[UsageRecord]:
        with self._connect() as conn:
            rows = conn.execute(
                "SELECT trace_id, session_id, call_kind, model_id, provider, usage_json, created_at FROM usage_log ORDER BY created_at ASC"
            ).fetchall()
        return [_row_to_record(r) for r in rows]

    def read_for_session(self, session_id: str) -> list[UsageRecord]:
        with self._connect() as conn:
            rows = conn.execute(
                "SELECT trace_id, session_id, call_kind, model_id, provider, usage_json, created_at FROM usage_log "
                "WHERE session_id = ? ORDER BY created_at ASC",
                (session_id,),
            ).fetchall()
        return [_row_to_record(r) for r in rows]
