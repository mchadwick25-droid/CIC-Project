"""The monthly bound on messages that got a safety check and no Representative reply."""
from datetime import date

import pytest

from engine.deeper.bound import MessageBound
from engine.deeper.meter import Meter


class Clock:
    def __init__(self, day):
        self.day = day

    def __call__(self):
        return self.day


@pytest.fixture
def clock():
    return Clock(date(2026, 10, 5))


@pytest.fixture
def meter(tmp_path, clock):
    m = Meter(str(tmp_path / "meter.db"), clock=clock, free_window_days=30, free_key=b"k" * 32)
    yield m
    m.close()


def test_a_visitor_reaches_its_count_and_not_before(meter):
    bound = MessageBound(meter, 3, 100)
    for _ in range(3):
        assert not bound.reached("v", "n")
        bound.count("v", "n")
    assert bound.reached("v", "n")
    assert not bound.reached("other", "n2")


def test_a_network_reaches_its_count_across_visitors(meter):
    bound = MessageBound(meter, 100, 4)
    for visitor in ("a", "b", "c", "d"):
        bound.count(visitor, "n")
    assert bound.reached("fresh-cookie", "n")
    assert not bound.reached("fresh-cookie", "elsewhere")


def test_the_count_clears_thirty_days_after_the_first_message_counted(meter, clock):
    bound = MessageBound(meter, 1, 100)
    bound.count("v", "n")
    assert bound.reached("v", "n")
    clock.day = date(2026, 11, 4)
    assert not bound.reached("v", "n")
    bound.count("v", "n")
    assert bound.reached("v", "n")


def test_the_rows_hold_a_day_and_a_number_under_scrambled_keys(meter):
    MessageBound(meter, 5, 5).count("visitor-id-abc", "203.0.113.9")
    rows = meter._conn.execute("SELECT key_hash, first_day, spent FROM free_window").fetchall()
    assert len(rows) == 2 and all(row[2] == 1 for row in rows)
    assert not any("visitor-id-abc" in str(row) or "203.0.113.9" in str(row) for row in rows)


def test_a_limit_below_one_is_refused(meter):
    with pytest.raises(ValueError):
        MessageBound(meter, 0, 5)
    with pytest.raises(ValueError):
        MessageBound(meter, 5, 0)


def test_the_bound_and_the_free_allowance_do_not_share_rows(meter):
    from engine.deeper.free import FreeAllowance

    free = FreeAllowance(meter, 550)
    MessageBound(meter, 5, 5).count("v", "v")
    assert free.remaining("v") == 550


def test_the_daily_purge_deletes_the_counts_when_their_window_ends(meter, clock):
    MessageBound(meter, 5, 5).count("v", "n")
    meter.purge()
    assert meter._conn.execute("SELECT COUNT(*) FROM free_window").fetchone()[0] == 2
    clock.day = date(2026, 11, 4)
    meter.purge()
    assert meter._conn.execute("SELECT COUNT(*) FROM free_window").fetchone()[0] == 0
