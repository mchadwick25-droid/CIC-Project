import threading
from datetime import datetime, timedelta, timezone

import pytest

from access_ledger import Ledger, LedgerError, connect, init_schema


def test_free_units_are_spent_before_paid(ledger):
    ledger.grant_free("v1", 1, "free:welcome:v1")
    ledger.grant_paid("v1", 2, "cs_1")
    first = ledger.hold("v1", "s1")
    ledger.capture("s1")
    second = ledger.hold("v1", "s2")
    assert first.bucket == "free"
    assert second.bucket == "paid"


def test_hold_reserves_a_unit_and_release_returns_it(ledger):
    ledger.grant_paid("v1", 1, "cs_1")
    assert ledger.hold("v1", "s1").admitted
    assert ledger.balance("v1") == 0
    ledger.release("s1")
    assert ledger.balance("v1") == 1


def test_capture_keeps_the_unit_spent(ledger):
    ledger.grant_paid("v1", 1, "cs_1")
    ledger.hold("v1", "s1")
    assert ledger.capture("s1") is True
    assert ledger.balance("v1") == 0
    assert ledger.open_holds() == []


def test_hold_is_idempotent_per_session(ledger):
    ledger.grant_paid("v1", 3, "cs_1")
    ledger.hold("v1", "s1")
    again = ledger.hold("v1", "s1")
    assert again.reason == "already_held"
    assert ledger.balance("v1") == 2


def test_no_balance_is_a_value_not_an_exception(ledger):
    admission = ledger.hold("v1", "s1")
    assert admission.admitted is False
    assert admission.reason == "no_balance"
    assert ledger.balance("v1") == 0


def test_an_open_conversation_needs_no_further_ledger_call(ledger):
    ledger.grant_paid("v1", 1, "cs_1")
    ledger.hold("v1", "s1")
    ledger.capture("s1")
    assert ledger.balance("v1") == 0
    assert ledger.hold("v1", "s1").admitted is True
    assert ledger.balance("v1") == 0


def test_capture_and_release_are_repeatable_without_double_effect(ledger):
    ledger.grant_paid("v1", 1, "cs_1")
    ledger.hold("v1", "s1")
    assert ledger.capture("s1") is True
    assert ledger.capture("s1") is False
    ledger.grant_paid("v2", 1, "cs_2")
    ledger.hold("v2", "s2")
    assert ledger.release("s2") is True
    assert ledger.release("s2") is False
    assert ledger.balance("v2") == 1


def test_capture_after_release_and_release_after_capture_are_refused(ledger):
    ledger.grant_paid("v1", 2, "cs_1")
    ledger.hold("v1", "s1")
    ledger.release("s1")
    with pytest.raises(LedgerError):
        ledger.capture("s1")
    ledger.hold("v1", "s2")
    ledger.capture("s2")
    with pytest.raises(LedgerError):
        ledger.release("s2")


def test_settling_an_unknown_session_is_refused(ledger):
    with pytest.raises(LedgerError):
        ledger.capture("missing")
    with pytest.raises(LedgerError):
        ledger.release("missing")


def test_a_grant_with_the_same_reference_is_applied_once(ledger):
    assert ledger.grant_paid("v1", 4, "cs_1") is True
    assert ledger.grant_paid("v1", 4, "cs_1") is False
    assert ledger.balance("v1") == 4
    assert ledger.grant_free("v1", 1, "free:welcome:v1") is True
    assert ledger.grant_free("v1", 1, "free:welcome:v1") is False


def test_non_positive_grants_are_refused(ledger):
    with pytest.raises(LedgerError):
        ledger.grant_paid("v1", 0, "cs_1")
    with pytest.raises(LedgerError):
        ledger.grant_free("v1", -1, "free:x")


def test_idle_holds_are_released_and_captured_ones_are_kept(ledger):
    start = datetime(2026, 10, 1, 12, 0, tzinfo=timezone.utc)
    ledger.grant_paid("v1", 3, "cs_1")
    ledger.hold("v1", "idle", now=start)
    ledger.hold("v1", "fresh", now=start + timedelta(hours=2))
    ledger.hold("v1", "done", now=start)
    ledger.capture("done", now=start)
    released = ledger.release_idle_holds(timedelta(hours=1), now=start + timedelta(hours=2, minutes=1))
    assert released == ["idle"]
    assert [h[0] for h in ledger.open_holds()] == ["fresh"]


def test_two_visitors_cannot_both_take_the_last_unit_of_one_visitor(tmp_path):
    path = tmp_path / "race.db"
    seed = connect(path)
    init_schema(seed)
    Ledger(seed).grant_paid("v1", 1, "cs_1")
    results = []

    def worker(session_id):
        c = connect(path)
        results.append(Ledger(c).hold("v1", session_id).admitted)

    threads = [threading.Thread(target=worker, args=(f"s{i}",)) for i in range(6)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    assert results.count(True) == 1
    assert Ledger(seed).balance("v1") == 0


def test_ledger_rows_are_never_changed_by_settlement(ledger, conn):
    ledger.grant_paid("v1", 1, "cs_1")
    ledger.hold("v1", "s1")
    before = conn.execute("SELECT id, kind, delta FROM access_ledger ORDER BY id").fetchall()
    ledger.release("s1")
    after = conn.execute("SELECT id, kind, delta FROM access_ledger ORDER BY id").fetchall()
    assert after[: len(before)] == before
    assert len(after) == len(before) + 1
