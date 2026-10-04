"""The door's spend: what the usage log says the last seven days cost, at the
approved prices, and a monitor that keeps its last state when it cannot tell."""
import sqlite3
from datetime import datetime, timedelta, timezone

import pytest

from engine.api import deeper_door
from engine.api.deeper_door import DEAREST, DoorMonitor, week_spend_usd
from engine.api.deeper_ops import load_ops
from engine.deeper import door as door_module
from engine.m8 import price_tables
from engine.m8.cost import estimate_cost
from engine.m8.log_store import UsageLogStore
from engine.m8.usage import SYSTEM_SESSION_ID, UsageRecord
from engine.provider.bedrock import NormalizedUsage

NOW = datetime(2026, 10, 12, 12, 0, tzinfo=timezone.utc)
USAGE = NormalizedUsage(input_tokens=10_000, output_tokens=1_000, cache_creation_input_tokens=5_000, cache_read_input_tokens=20_000)
SONNET = "us.anthropic.claude-sonnet-4-5-20250929-v1:0"


def record(trace, *, kind="voice_generation", model=SONNET, session="s1", usage=USAGE):
    return UsageRecord(trace_id=trace, session_id=session, call_kind=kind, model_id=model, provider="bedrock", usage=usage)


@pytest.fixture
def usage_store(tmp_path):
    return UsageLogStore(tmp_path / "usage.db")


def age(store, trace, when):
    with sqlite3.connect(store.db_path) as conn:
        conn.execute("UPDATE usage_log SET created_at = ? WHERE trace_id = ?", (when.isoformat(), trace))


def test_the_week_is_priced_at_the_approved_table_for_the_model_and_call(usage_store):
    usage_store.append(record("a"))
    age(usage_store, "a", NOW - timedelta(days=1))
    expected = estimate_cost(USAGE, price_tables.SONNET_4_5_PRICE_TABLE).dollars
    assert week_spend_usd(usage_store, NOW) == pytest.approx(expected)


def test_calls_older_than_seven_days_and_system_calls_are_left_out(usage_store):
    usage_store.append(record("old"))
    usage_store.append(record("system", session=SYSTEM_SESSION_ID))
    usage_store.append(record("new"))
    age(usage_store, "old", NOW - timedelta(days=8))
    age(usage_store, "system", NOW - timedelta(days=1))
    age(usage_store, "new", NOW - timedelta(days=6))
    expected = estimate_cost(USAGE, price_tables.SONNET_4_5_PRICE_TABLE).dollars
    assert week_spend_usd(usage_store, NOW) == pytest.approx(expected)


def test_a_call_on_a_model_with_no_approved_price_counts_at_the_dearest_price_never_zero(usage_store):
    usage_store.append(record("mystery", model="some.unknown.model-9"))
    age(usage_store, "mystery", NOW - timedelta(days=1))
    spend = week_spend_usd(usage_store, NOW)
    assert spend == pytest.approx(estimate_cost(USAGE, DEAREST).dollars)
    assert spend >= estimate_cost(USAGE, price_tables.SONNET_4_5_PRICE_TABLE).dollars


def test_a_call_kind_the_tables_do_not_know_is_still_counted(usage_store):
    usage_store.append(record("new-kind", kind="a_future_call"))
    age(usage_store, "new-kind", NOW - timedelta(days=1))
    assert week_spend_usd(usage_store, NOW) > 0


def test_the_dearest_price_is_at_least_every_approved_price_in_every_category():
    for table in (
        price_tables.SONNET_4_5_PRICE_TABLE, price_tables.SONNET_5_5_PRICE_TABLE,
        price_tables.OPUS_5_5_PRICE_TABLE, price_tables.HAIKU_4_5_PRICE_TABLE,
    ):
        assert DEAREST.input_per_token >= table.input_per_token
        assert DEAREST.output_per_token >= table.output_per_token
        assert DEAREST.cache_write_per_token >= table.cache_write_per_token
        assert DEAREST.cache_read_per_token >= table.cache_read_per_token


def test_read_since_returns_only_records_at_or_after_the_time(usage_store):
    usage_store.append(record("a"))
    usage_store.append(record("b"))
    age(usage_store, "a", NOW - timedelta(days=3))
    age(usage_store, "b", NOW - timedelta(days=1))
    got = usage_store.read_since((NOW - timedelta(days=2)).isoformat())
    assert [r.trace_id for r in got] == ["b"]


class Clock:
    def __init__(self):
        self.now = 1000.0

    def __call__(self):
        return self.now


def make_monitor(usage_store, funds=None, clock=None, refresh=60.0):
    return DoorMonitor(
        load_ops().door, usage_store, funds or (lambda: {"gift": 0, "purchase": 0, "adjustment": 0}),
        clock=lambda: NOW, monotonic=clock or Clock(), refresh_seconds=refresh,
    )


def heavy(usage_store, n, days=1):
    big = NormalizedUsage(input_tokens=1_000_000, output_tokens=200_000, cache_creation_input_tokens=0, cache_read_input_tokens=0)
    for i in range(n):
        usage_store.append(record(f"h{i}", usage=big))
        age(usage_store, f"h{i}", NOW - timedelta(days=days))


def test_the_door_starts_open_and_narrows_as_the_weeks_spend_climbs(usage_store):
    monitor = make_monitor(usage_store)
    assert monitor.state().stage == 0
    heavy(usage_store, 20)
    clock = Clock()
    monitor = make_monitor(usage_store, clock=clock)
    state = monitor.state()
    assert state.stage > 0 and state.ratio > 0.5


def test_a_gift_raises_the_ceiling_and_the_door_follows_on_the_next_refresh(usage_store):
    heavy(usage_store, 30)
    funds = {"gift": 0, "purchase": 0, "adjustment": 0}
    clock = Clock()
    monitor = make_monitor(usage_store, funds=lambda: dict(funds), clock=clock)
    narrowed = monitor.state()
    assert narrowed.stage > 0
    funds["gift"] = 5_000_000
    assert monitor.state().stage == narrowed.stage
    clock.now += 61
    assert monitor.state().stage < narrowed.stage


def test_the_state_is_recomputed_at_most_once_a_minute(usage_store):
    calls = []
    clock = Clock()
    monitor = make_monitor(usage_store, funds=lambda: calls.append(1) or {"gift": 0, "purchase": 0, "adjustment": 0}, clock=clock)
    monitor.state()
    monitor.state()
    clock.now += 59
    monitor.state()
    assert len(calls) == 1
    clock.now += 2
    monitor.state()
    assert len(calls) == 2


def test_a_fault_keeps_the_last_state_and_never_opens_what_had_closed(usage_store):
    heavy(usage_store, 60)
    clock = Clock()
    broken = {"on": False}

    def funds():
        if broken["on"]:
            raise RuntimeError("meter down")
        return {"gift": 0, "purchase": 0, "adjustment": 0}

    monitor = make_monitor(usage_store, funds=funds, clock=clock)
    closed = monitor.state()
    assert not closed.free_voice
    broken["on"] = True
    clock.now += 61
    assert monitor.state() == closed


def test_a_fault_before_the_first_state_leaves_the_door_open(usage_store):
    def funds():
        raise RuntimeError("meter down")

    assert make_monitor(usage_store, funds=funds).state() == door_module.OPEN
