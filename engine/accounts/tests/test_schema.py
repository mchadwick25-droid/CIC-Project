"""What the account files may name. Accounts hold a keyed hash, days and weeks,
and nothing personal; the durable file holds no time finer than a day."""
import re
import sqlite3

import pytest

FORBIDDEN_NAMES = re.compile(r"address|email|mail|name|text|title|world|conversation|session_id|ip|payment|stripe", re.I)


def _columns(conn, only=None):
    out = {}
    for (table,) in conn.execute("SELECT name FROM sqlite_master WHERE type = 'table'"):
        if only and table not in only:
            continue
        out[table] = [r[1] for r in conn.execute(f"PRAGMA table_info({table})")]
    return out


def test_no_column_in_either_file_names_anything_personal(store):
    for conn in (store._d, store._e):
        for table, columns in _columns(conn).items():
            for column in columns:
                stem = column.replace("address_hash", "").replace("session_", "").replace("_hash", "")
                assert not FORBIDDEN_NAMES.search(stem), f"{table}.{column}"


def test_every_table_is_without_rowid(store):
    for conn in (store._d, store._e):
        for (sql,) in conn.execute("SELECT sql FROM sqlite_master WHERE type = 'table' AND sql IS NOT NULL"):
            assert "WITHOUT ROWID" in sql


def test_the_durable_file_holds_no_time_finer_than_a_day(store):
    for table, columns in _columns(store._d).items():
        for column in columns:
            assert not re.search(r"time|_at$|expires_at|stamp", column), f"{table}.{column}"


def test_the_account_files_hold_no_meter_code_hash_and_no_payment_id(svc, mailer, tmp_path):
    from datetime import date

    from engine.deeper import codes
    from engine.deeper.meter import Meter
    from engine.accounts.tests.conftest import sign_in

    meter = Meter(str(tmp_path / "meter.db"), clock=lambda: date(2026, 10, 5))
    minted = meter.mint("single", 100, "pi_account_proof")
    sign_in(svc, mailer)
    for name in ("d.db", "e.db"):
        data = (tmp_path / name).read_bytes()
        assert codes.hash_code(minted[0]).encode() not in data
        assert b"pi_account_proof" not in data
    meter.close()


def test_a_file_made_before_recovery_was_removed_loses_its_recovery_tables(tmp_path):
    import sqlite3

    from engine.accounts.store import AccountStore

    durable = str(tmp_path / "old.db")
    conn = sqlite3.connect(durable)
    conn.execute("CREATE TABLE recovery_codes (account_id TEXT PRIMARY KEY, code_hash TEXT, day_made TEXT)")
    conn.execute("CREATE TABLE pending_changes (account_id TEXT PRIMARY KEY, new_address_hash TEXT, effective_on TEXT)")
    conn.execute("INSERT INTO recovery_codes VALUES ('a', 'h', 'd')")
    conn.commit()
    conn.close()
    store = AccountStore(durable, str(tmp_path / "e.db"))
    names = {r[0] for r in store._d.execute("SELECT name FROM sqlite_master WHERE type = 'table'")}
    assert names == {"accounts", "linked_sign_ins", "erased_sessions", "shelf", "account_codes", "recovery_keys", "pending_recoveries", "deletion_ledger", "pending_coupons"}
    store.close()


def test_an_older_ephemeral_file_without_the_challenge_order_column_is_opened_and_works(tmp_path):
    import sqlite3
    from engine.accounts.store import AccountStore, Challenge

    path = tmp_path / "old-e.db"
    conn = sqlite3.connect(str(path))
    conn.executescript(
        "CREATE TABLE challenges (challenge_id TEXT PRIMARY KEY, kind TEXT NOT NULL, address_hash TEXT NOT NULL,"
        " account_id TEXT, mac TEXT NOT NULL, expires_at INTEGER NOT NULL, tries INTEGER NOT NULL DEFAULT 0, bound TEXT) WITHOUT ROWID;"
    )
    conn.commit()
    conn.close()
    store = AccountStore(str(tmp_path / "d.db"), str(path))
    for i in range(4):
        store.put_challenge(Challenge(f"c{i}", "sign_in", "h", None, "m", 9999999999, 0, None), keep_live=3)
    live = {r[0] for r in store._e.execute("SELECT challenge_id FROM challenges")}
    assert live == {"c1", "c2", "c3"}
    store.close()
