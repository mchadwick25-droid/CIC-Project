"""The quality-control store (System Hub decisions 7, 19 and 28): one row per
turn, kept apart from the event log and the usage log and holding nothing
that leads back to a person. A turn is found by a random conversation
token that exists only here and in the running server's memory, never in
the event log; the date is the ISO week, never a time. Questions are kept;
answers are deleted after 90 days; scores are kept. A turn the safety call
flagged keeps its routing flags and no text.
"""
import json
import random
import sqlite3
from datetime import date, timedelta
from pathlib import Path

DDL = """
CREATE TABLE IF NOT EXISTS qc_turn (
  conversation_token TEXT    NOT NULL,
  round              INTEGER NOT NULL,
  world              TEXT    NOT NULL,
  package_hash       TEXT,
  model_id           TEXT,
  routing            TEXT    NOT NULL,
  flags              TEXT    NOT NULL,
  question_text      TEXT,
  answer_text        TEXT,
  marks              TEXT    NOT NULL,
  scores             TEXT    NOT NULL,
  week               TEXT    NOT NULL,
  PRIMARY KEY (conversation_token, round)
);
"""

ANSWER_RETENTION_DAYS = 90


def iso_week(day: date) -> str:
    year, week, _ = day.isocalendar()
    return f"{year}-W{week:02d}"


def week_start(week: str) -> date:
    year, number = week.split("-W")
    return date.fromisocalendar(int(year), int(number), 1)


class QCStore:
    def __init__(self, db_path: str | Path):
        self.db_path = str(db_path)
        with self._connect() as conn:
            conn.executescript(DDL)

    def _connect(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path, timeout=5.0)
        conn.execute("PRAGMA journal_mode=WAL")
        return conn

    def write_turn(self, *, conversation_token: str, round_no: int, world: str, package_hash: str | None,
                   model_id: str | None, routing: str, flags: dict, question_text: str | None,
                   answer_text: str | None, marks: dict, scores: dict, day: date) -> None:
        with self._connect() as conn:
            conn.execute(
                "INSERT OR REPLACE INTO qc_turn VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (conversation_token, round_no, world, package_hash, model_id, routing,
                 json.dumps(flags, sort_keys=True), question_text, answer_text,
                 json.dumps(marks, sort_keys=True), json.dumps(scores, sort_keys=True), iso_week(day)),
            )
            conn.commit()

    def expire_answers(self, today: date) -> int:
        """Delete answer text from every week that ended more than 90 days
        ago. Returns the number of rows cleared."""
        cutoff = today - timedelta(days=ANSWER_RETENTION_DAYS)
        with self._connect() as conn:
            weeks = [w for (w,) in conn.execute("SELECT DISTINCT week FROM qc_turn WHERE answer_text IS NOT NULL")]
            old = [w for w in weeks if week_start(w) + timedelta(days=6) < cutoff]
            cleared = 0
            for w in old:
                cleared += conn.execute("UPDATE qc_turn SET answer_text = NULL WHERE week = ? AND answer_text IS NOT NULL", (w,)).rowcount
            conn.commit()
        return cleared

    def rows(self) -> list[dict]:
        with self._connect() as conn:
            conn.row_factory = sqlite3.Row
            return [dict(r) for r in conn.execute("SELECT * FROM qc_turn ORDER BY conversation_token, round")]

    def sample_conversations(self, week: str, n: int, seed: int) -> list[list[dict]]:
        """A seeded random sample of whole conversations from one week, for
        the offline audit."""
        by_token: dict[str, list[dict]] = {}
        for r in self.rows():
            if r["week"] == week:
                by_token.setdefault(r["conversation_token"], []).append(r)
        tokens = sorted(by_token)
        return [by_token[t] for t in random.Random(seed).sample(tokens, min(n, len(tokens)))]
