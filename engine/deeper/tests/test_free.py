"""The free allowance: a rolling window from a visitor's first use, kept in the meter's file."""
from datetime import date

import pytest

from engine.deeper.free import FreeAllowance
from engine.deeper.meter import Meter

WINDOW = 550


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
    m = Meter(str(tmp_path / "meter.db"), clock=clock, free_window_days=30)
    yield m
    m.close()


@pytest.fixture
def free(meter):
    return FreeAllowance(meter, WINDOW)


def draw(free, key, amount):
    held = free.reserve(key, amount)
    assert held is not None
    free.settle(held, True)


def test_a_visitor_draws_up_to_the_window_and_no_more(free):
    for _ in range(5):
        draw(free, "v", 110)
    assert free.remaining("v") == 0
    assert free.reserve("v", 1) is None


def test_five_three_round_solo_conversations_fit_and_a_sixth_does_not(free):
    for _ in range(5):
        draw(free, "v", 110)
    assert free.reserve("v", 110) is None


def test_a_turn_that_was_not_voiced_gives_its_amount_back(free):
    held = free.reserve("v", 100)
    free.settle(held, False)
    assert free.remaining("v") == WINDOW


def test_a_hold_counts_against_the_window_until_it_is_settled(free):
    held = free.reserve("v", 500)
    assert free.reserve("v", 100) is None
    free.settle(held, False)
    assert free.reserve("v", 100) is not None


def test_settling_twice_changes_nothing(free):
    held = free.reserve("v", 100)
    free.settle(held, True)
    free.settle(held, True)
    free.settle(held, False)
    assert free.remaining("v") == WINDOW - 100


def test_visitors_have_their_own_windows(free):
    draw(free, "a", WINDOW)
    assert free.reserve("a", 1) is None
    assert free.reserve("b", 1) is not None


def test_the_window_starts_at_the_first_draw_and_refills_thirty_days_after_it(free, clock):
    draw(free, "v", WINDOW)
    clock.day = date(2026, 11, 3)
    assert free.reserve("v", 1) is None, "day 29 of the window: still spent"
    clock.day = date(2026, 11, 4)
    assert free.remaining("v") == WINDOW, "day 30: refilled"


def test_the_refill_rolls_from_the_visitors_own_first_use_not_the_calendar(free, clock):
    clock.day = date(2026, 10, 20)
    draw(free, "late", 100)
    clock.day = date(2026, 11, 4)
    assert free.remaining("late") == WINDOW - 100, "a calendar month would have refilled by now"
    clock.day = date(2026, 11, 19)
    assert free.remaining("late") == WINDOW


def test_a_draw_after_the_window_ends_starts_a_new_window(free, clock):
    draw(free, "v", WINDOW)
    clock.day = date(2026, 11, 4)
    draw(free, "v", 200)
    clock.day = date(2026, 11, 20)
    assert free.remaining("v") == WINDOW - 200, "the new window began on the day of the first new draw"
    clock.day = date(2026, 12, 4)
    assert free.remaining("v") == WINDOW


def test_a_reservation_alone_does_not_start_a_window(free, clock):
    held = free.reserve("v", 100)
    free.settle(held, False)
    clock.day = date(2026, 10, 25)
    draw(free, "v", 100)
    clock.day = date(2026, 11, 5)
    assert free.remaining("v") == WINDOW - 100, "the window began at the first settled draw, on the 25th"


def test_what_a_visitor_has_drawn_survives_a_restart(tmp_path, clock):
    path = str(tmp_path / "m.db")
    first = Meter(path, clock=clock)
    draw(FreeAllowance(first, WINDOW), "v", 400)
    first.close()
    second = Meter(path, clock=clock)
    try:
        assert FreeAllowance(second, WINDOW).remaining("v") == WINDOW - 400
    finally:
        second.close()


def test_the_visitor_key_is_never_written_to_the_file(tmp_path, clock):
    path = tmp_path / "m.db"
    m = Meter(str(path), clock=clock)
    draw(FreeAllowance(m, WINDOW), "ip:203.0.113.77", 100)
    draw(FreeAllowance(m, WINDOW), "visitor-cookie-abcdef", 100)
    m.close()
    raw = path.read_bytes()
    assert b"203.0.113.77" not in raw and b"visitor-cookie-abcdef" not in raw


def test_the_same_visitor_gets_the_same_row_after_a_restart_and_two_files_do_not_agree(tmp_path, clock):
    a, b = Meter(str(tmp_path / "a.db"), clock=clock), Meter(str(tmp_path / "b.db"), clock=clock)
    try:
        assert a.free_key("v") == a.free_key("v")
        assert a.free_key("v") != b.free_key("v"), "each file has its own salt, so a key means nothing outside it"
    finally:
        a.close()
        b.close()


def test_a_window_that_has_ended_is_deleted_by_the_purge(free, meter, clock):
    draw(free, "v", 100)
    clock.day = date(2026, 11, 4)
    meter.purge()
    import sqlite3

    rows = sqlite3.connect(meter._conn.execute("PRAGMA database_list").fetchone()[2]).execute("SELECT COUNT(*) FROM free_window").fetchone()
    assert rows[0] == 0


def test_a_window_still_running_is_kept_by_the_purge(free, meter, clock):
    draw(free, "v", 100)
    clock.day = date(2026, 11, 3)
    meter.purge()
    assert free.remaining("v") == WINDOW - 100


def test_a_window_below_one_is_refused(meter):
    with pytest.raises(ValueError):
        FreeAllowance(meter, 0)


@pytest.mark.parametrize("amount", [0, -5])
def test_an_amount_below_one_is_refused(free, amount):
    with pytest.raises(ValueError):
        free.reserve("v", amount)


def test_a_share_narrows_the_window(free):
    assert free.reserve("v", 300, share=0.5) is None
    assert free.reserve("v", 275, share=0.5) is not None


@pytest.mark.parametrize("share", [0, -0.5, 1.5])
def test_a_share_outside_zero_to_one_is_refused(free, share):
    with pytest.raises(ValueError):
        free.reserve("v", 10, share=share)
