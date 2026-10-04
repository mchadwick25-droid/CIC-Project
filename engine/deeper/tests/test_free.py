from datetime import date, timedelta

import pytest

from engine.deeper.free import DailyFreeAllowance


class Day:
    def __init__(self):
        self.today = date(2026, 10, 5)

    def __call__(self):
        return self.today


@pytest.fixture
def day():
    return Day()


@pytest.fixture
def free(day):
    return DailyFreeAllowance(330, clock=day)


def test_a_turn_that_fits_is_held_and_spent_when_it_is_voiced(free):
    held = free.reserve("v", 110)
    assert held is not None and free.remaining("v") == 220
    free.settle(held, True)
    assert free.remaining("v") == 220


def test_a_turn_that_does_not_fit_is_refused_and_nothing_is_held(free):
    assert free.reserve("v", 331) is None
    assert free.remaining("v") == 330


def test_a_turn_that_was_not_voiced_gives_its_amount_back(free):
    held = free.reserve("v", 110)
    free.settle(held, False)
    assert free.remaining("v") == 330


def test_a_hold_counts_against_the_day_until_it_is_settled(free):
    first = free.reserve("v", 200)
    assert free.reserve("v", 200) is None
    free.settle(first, False)
    assert free.reserve("v", 200) is not None


def test_settling_twice_changes_nothing(free):
    held = free.reserve("v", 100)
    free.settle(held, True)
    free.settle(held, True)
    free.settle(held, False)
    assert free.remaining("v") == 230


def test_visitors_have_their_own_days(free):
    free.settle(free.reserve("a", 330), True)
    assert free.remaining("a") == 0
    assert free.remaining("b") == 330


def test_a_new_day_starts_full(free, day):
    free.settle(free.reserve("v", 330), True)
    assert free.reserve("v", 1) is None
    day.today += timedelta(days=1)
    assert free.remaining("v") == 330


@pytest.mark.parametrize("bad", [0, -5])
def test_an_amount_below_one_is_refused(free, bad):
    with pytest.raises(ValueError):
        free.reserve("v", bad)


def test_a_free_day_below_one_is_refused():
    with pytest.raises(ValueError):
        DailyFreeAllowance(0)


def test_the_allowance_never_logs_or_stores_a_visitor_key():
    import ast
    from pathlib import Path

    import engine.deeper.free as module

    tree = ast.parse(Path(module.__file__).read_text())
    imported = {a.name.split(".")[0] for n in ast.walk(tree) if isinstance(n, ast.Import) for a in n.names}
    imported |= {n.module.split(".")[0] for n in ast.walk(tree) if isinstance(n, ast.ImportFrom) and n.module}
    assert imported <= {"threading", "datetime", "typing"}
    called = {n.func.id for n in ast.walk(tree) if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)}
    assert not called & {"print", "open"}


def test_a_share_narrows_the_day(free):
    assert free.reserve("v", 200, share=0.5) is None
    held = free.reserve("v", 165, share=0.5)
    assert held is not None
    free.settle(held, True)
    assert free.reserve("v", 1, share=0.5) is None
    assert free.reserve("v", 1) is not None


@pytest.mark.parametrize("share", [0, -0.5, 1.5])
def test_a_share_outside_zero_to_one_is_refused(free, share):
    with pytest.raises(ValueError):
        free.reserve("v", 10, share=share)
