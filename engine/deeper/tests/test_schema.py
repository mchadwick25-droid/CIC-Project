"""No join exists between the three stores: nothing in the meter or claim
files can name a session, a visitor, an address, a person, or a moment finer
than a day."""
import re
import sqlite3
from datetime import date

import pytest

from engine.deeper.claims import ClaimStore
from engine.deeper.meter import Meter

BANNED_NAME = re.compile(r"session|visitor|(^|_)ip($|_)|address|email|name|phone|user|stamp|(^|_)at$|(^|_)time|epoch|clock")
BANNED_TYPE = re.compile(r"TIMESTAMP|DATETIME|TIME", re.I)
TIME_OF_DAY = re.compile(r"\d{2}:\d{2}|\dT\d{2}")
EPOCH_LIKE = re.compile(r"^\d{9,}$")


def _tables(path):
    conn = sqlite3.connect(path)
    try:
        names = [r[0] for r in conn.execute("SELECT name FROM sqlite_master WHERE type = 'table' AND name NOT LIKE 'sqlite_%'")]
        return {n: conn.execute(f"PRAGMA table_info({n})").fetchall() for n in names}, conn.execute("SELECT name, sql FROM sqlite_master WHERE type='table'").fetchall()
    finally:
        conn.close()


@pytest.fixture
def used_meter(tmp_path):
    path = str(tmp_path / "meter.db")
    m = Meter(path, clock=lambda: date(2026, 10, 5))
    (code,) = m.mint("single", 4, "pi_a")
    m.settle(m.reserve(code).reservation, True)
    m.mint("batch", 2, "pi_b", count=2)
    m.mint("group", 9, "pi_c")
    m.void("pi_b")
    m.tally("payments_seen")
    m.add_funds("gift", 2500, "pi_g")
    m.add_funds("adjustment", 1000, note="a church gift")
    m.free_window_spend(m.free_key("a-visitor"), 110)
    m.join_pilot("a-visitor", 5, "pilot_a", open_=True, end_date=date(2026, 12, 31), cap=9, per_address=2)
    m.pause(True)
    m.close()
    return path


def test_meter_columns_name_nothing_personal_and_no_fine_time(used_meter):
    tables, _ = _tables(used_meter)
    assert set(tables) == {"meter", "voided_payments", "state", "reconcile", "funds", "daily", "free_window", "pilot_joined"}
    for table, columns in tables.items():
        for _cid, name, ctype, *_ in columns:
            assert not BANNED_NAME.search(name), f"{table}.{name}"
            assert not BANNED_TYPE.search(ctype or ""), f"{table}.{name} is typed {ctype}"


def test_meter_tables_have_no_rowid(used_meter):
    _, sql = _tables(used_meter)
    for name, statement in sql:
        assert "WITHOUT ROWID" in statement, name
    conn = sqlite3.connect(used_meter)
    with pytest.raises(sqlite3.OperationalError):
        conn.execute("SELECT rowid FROM meter")
    conn.close()


def test_meter_holds_no_time_finer_than_a_day(used_meter):
    conn = sqlite3.connect(used_meter)
    for table in ("meter", "voided_payments", "state", "reconcile", "daily", "free_window", "pilot_joined"):
        for row in conn.execute(f"SELECT * FROM {table}"):
            for value in row:
                text = str(value)
                assert not TIME_OF_DAY.search(text), (table, value)
                assert not EPOCH_LIKE.match(text), (table, value)
    conn.close()


def test_meter_stores_no_plain_code(used_meter):
    assert re.search(rb"[2-9A-HJ-NP-Z]{20}", open(used_meter, "rb").read()) is None


def test_claim_file_names_nothing_personal(tmp_path):
    path = str(tmp_path / "claims.db")
    ClaimStore(path).close()
    tables, _ = _tables(path)
    assert set(tables) == {"claims"}
    for _cid, name, *_ in tables["claims"]:
        assert not re.search(r"session|visitor|(^|_)ip($|_)|address|email|name|phone|user|payment|hash", name), name


def test_the_meter_and_claim_files_share_no_column(used_meter, tmp_path):
    claims = str(tmp_path / "claims.db")
    ClaimStore(claims).close()
    meter_cols = {c[1] for cols in _tables(used_meter)[0].values() for c in cols}
    claim_cols = {c[1] for cols in _tables(claims)[0].values() for c in cols}
    assert meter_cols.isdisjoint(claim_cols)


def test_the_free_window_table_holds_a_salted_hash_a_day_and_a_number_and_nothing_else(used_meter):
    tables, _ = _tables(used_meter)
    assert [c[1] for c in tables["free_window"]] == ["key_hash", "first_day", "spent"]
    conn = sqlite3.connect(used_meter)
    (key_hash, first_day, spent) = conn.execute("SELECT key_hash, first_day, spent FROM free_window").fetchone()
    conn.close()
    assert re.fullmatch(r"[0-9a-f]{32}", key_hash) and re.fullmatch(r"\d{4}-\d{2}-\d{2}", first_day) and spent == 110


def test_the_pilot_table_holds_a_keyed_hash_a_count_and_a_day_and_nothing_else(used_meter):
    tables, _ = _tables(used_meter)
    assert [c[1] for c in tables["pilot_joined"]] == ["key_hash", "joins", "first_day"]
    conn = sqlite3.connect(used_meter)
    (key_hash, joins, first_day) = conn.execute("SELECT key_hash, joins, first_day FROM pilot_joined").fetchone()
    conn.close()
    assert re.fullmatch(r"[0-9a-f]{32}", key_hash) and joins == 1 and re.fullmatch(r"\d{4}-\d{2}-\d{2}", first_day)
