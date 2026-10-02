"""SQLite storage for access units, purchases and processed Stripe events.

The ledger table is append-only: rows are inserted, never updated or deleted.
A visitor's balance is the sum of their rows.
"""
import sqlite3
from pathlib import Path

DDL = """
CREATE TABLE IF NOT EXISTS access_ledger (
  id          INTEGER PRIMARY KEY AUTOINCREMENT,
  visitor_id  TEXT NOT NULL,
  kind        TEXT NOT NULL CHECK (kind IN
              ('grant_free','grant_paid','hold','capture','release','reverse','expire','adjust')),
  bucket      TEXT NOT NULL CHECK (bucket IN ('free','paid')),
  delta       INTEGER NOT NULL,
  session_id  TEXT,
  purchase_id TEXT,
  source_ref  TEXT UNIQUE,
  created_at  TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS access_ledger_visitor ON access_ledger (visitor_id);
CREATE INDEX IF NOT EXISTS access_ledger_session ON access_ledger (session_id);

CREATE TABLE IF NOT EXISTS purchases (
  purchase_id    TEXT PRIMARY KEY,
  payment_intent TEXT,
  visitor_id     TEXT NOT NULL,
  sku            TEXT NOT NULL,
  units          INTEGER NOT NULL,
  amount_cents   INTEGER NOT NULL,
  currency       TEXT NOT NULL,
  status         TEXT NOT NULL CHECK (status IN ('pending','granted','failed','amount_mismatch')),
  created_at     TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS purchases_payment_intent ON purchases (payment_intent);

CREATE TABLE IF NOT EXISTS stripe_events (
  event_id     TEXT PRIMARY KEY,
  event_type   TEXT NOT NULL,
  outcome      TEXT NOT NULL,
  processed_at TEXT NOT NULL
);
"""


def connect(db_path: str | Path) -> sqlite3.Connection:
    conn = sqlite3.connect(str(db_path), timeout=5.0, isolation_level=None)
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    return conn


def init_schema(conn: sqlite3.Connection) -> None:
    conn.executescript(DDL)
