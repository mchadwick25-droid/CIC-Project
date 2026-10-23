import sqlite3

from engine import sqlite_scrub


def _db(tmp_path):
    conn = sqlite3.connect(tmp_path / "w.db")
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA secure_delete=ON")
    conn.execute("CREATE TABLE t (v TEXT)")
    conn.execute("INSERT INTO t VALUES ('a-very-particular-deleted-value')")
    conn.commit()
    return conn


def test_the_journal_is_emptied_after_a_deletion(tmp_path):
    conn = _db(tmp_path)
    conn.execute("DELETE FROM t")
    conn.commit()
    assert sqlite_scrub.truncate_wal(conn) is True
    assert b"a-very-particular-deleted-value" not in (tmp_path / "w.db-wal").read_bytes()


def test_a_busy_journal_is_reported_not_assumed_clean(tmp_path, monkeypatch):
    conn = _db(tmp_path)
    reader = sqlite3.connect(tmp_path / "w.db")
    reader.execute("BEGIN")
    reader.execute("SELECT * FROM t").fetchall()
    conn.execute("DELETE FROM t")
    conn.commit()
    monkeypatch.setattr(sqlite_scrub, "PAUSE_SECONDS", 0)
    assert sqlite_scrub.truncate_wal(conn) is False
    reader.close()
