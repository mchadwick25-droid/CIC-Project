import threading
from datetime import date

import pytest

from engine.deeper import codes
from engine.deeper.meter import AlreadyMinted, Meter, PaymentVoided, week_of


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
    m = Meter(str(tmp_path / "meter.db"), clock=clock, group_daily_ceiling=3)
    yield m
    m.close()


def test_mint_single_returns_one_plain_code_and_stores_only_a_hash(meter, tmp_path):
    (code,) = meter.mint("single", 25, "pi_1")
    assert codes.normalize(code) == code
    raw = (tmp_path / "meter.db").read_bytes()
    assert code.encode() not in raw
    assert meter.status(code).remaining == 25


def test_mint_batch_makes_distinct_codes_each_with_the_full_balance(meter):
    batch = meter.mint("batch", 10, "pi_2", count=5)
    assert len(set(batch)) == 5
    assert all(meter.status(c).remaining == 10 for c in batch)


@pytest.mark.parametrize("kind,count", [("single", 2), ("group", 2), ("batch", 0), ("batch", 1001)])
def test_mint_refuses_wrong_counts(meter, kind, count):
    with pytest.raises(ValueError):
        meter.mint(kind, 10, "pi_x", count=count)


@pytest.mark.parametrize("tokens", [0, -1, 1_000_001, 1.5])
def test_mint_refuses_wrong_tokens(meter, tokens):
    with pytest.raises(ValueError):
        meter.mint("single", tokens, "pi_x")


def test_mint_refuses_unknown_kind_and_empty_payment(meter):
    with pytest.raises(ValueError):
        meter.mint("pack", 10, "pi_x")
    with pytest.raises(ValueError):
        meter.mint("single", 10, "")


def test_replayed_payment_mints_nothing_more(meter):
    meter.mint("single", 10, "pi_3")
    with pytest.raises(AlreadyMinted):
        meter.mint("single", 10, "pi_3")


def test_verify(meter):
    (code,) = meter.mint("single", 1, "pi_4")
    assert meter.verify(code)
    assert meter.verify(codes.display(code).lower())
    assert not meter.verify(codes.generate())
    assert not meter.verify("garbage")
    assert not meter.verify(None)
    reservation = meter.reserve(code).reservation
    meter.settle(reservation, True)
    assert not meter.verify(code)


def test_reserve_then_settle_spends_one_exchange(meter):
    (code,) = meter.mint("single", 3, "pi_5")
    admission = meter.reserve(code)
    assert admission.ok and admission.remaining == 3
    assert meter.status(code).remaining == 3
    assert meter.settle(admission.reservation, True) == 2
    assert meter.status(code).remaining == 2


def test_release_returns_the_exchange(meter):
    (code,) = meter.mint("single", 1, "pi_6")
    admission = meter.reserve(code)
    meter.release(admission.reservation)
    assert meter.status(code).remaining == 1
    assert meter.reserve(code).ok


def test_settle_twice_spends_once(meter):
    (code,) = meter.mint("single", 5, "pi_7")
    reservation = meter.reserve(code).reservation
    meter.settle(reservation, True)
    assert meter.settle(reservation, True) is None
    assert meter.status(code).remaining == 4


def test_last_exchange_marks_the_code_spent(meter):
    (code,) = meter.mint("single", 1, "pi_8")
    meter.settle(meter.reserve(code).reservation, True)
    assert meter.status(code).status == "spent"
    assert meter.reserve(code).reason == "spent"


def test_pooled_code_cannot_be_overdrawn(meter):
    (code,) = meter.mint("group", 1, "pi_9")
    first = meter.reserve(code)
    second = meter.reserve(code)
    assert first.ok
    assert not second.ok and second.reason == "in_use"
    meter.release(first.reservation)
    assert meter.reserve(code).ok


def test_two_concurrent_reserves_on_one_exchange_admit_exactly_one(meter):
    (code,) = meter.mint("group", 1, "pi_10")
    barrier = threading.Barrier(8)
    results = []

    def attempt():
        barrier.wait()
        results.append(meter.reserve(code))

    threads = [threading.Thread(target=attempt) for _ in range(8)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    assert sum(r.ok for r in results) == 1
    assert {r.reason for r in results if not r.ok} == {"in_use"}


def test_concurrent_settles_never_overspend(meter):
    (code,) = meter.mint("group", 20, "pi_11", daily_ceiling=100)
    admissions = [meter.reserve(code) for _ in range(20)]
    assert all(a.ok for a in admissions)
    assert meter.reserve(code).reason == "in_use"
    threads = [threading.Thread(target=meter.settle, args=(a.reservation, True)) for a in admissions]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    status = meter.status(code)
    assert status.tokens_used == 20 and status.status == "spent"


def test_wrong_code_reasons(meter):
    assert meter.reserve("garbage").reason == "unknown"
    assert meter.reserve(codes.generate()).reason == "unknown"
    assert meter.reserve(None).reason == "unknown"


def test_pause_refuses_every_code_and_unpause_restores(meter):
    (code,) = meter.mint("single", 2, "pi_12")
    meter.pause(True)
    assert meter.is_paused()
    assert meter.reserve(code).reason == "paused"
    assert meter.status(code).remaining == 2
    meter.pause(False)
    assert not meter.is_paused()
    assert meter.reserve(code).ok


def test_pause_survives_a_restart(tmp_path, clock):
    path = str(tmp_path / "m.db")
    first = Meter(path, clock=clock)
    first.pause(True)
    first.close()
    second = Meter(path, clock=clock)
    assert second.is_paused()
    second.close()


def test_pause_takes_effect_on_the_next_reserve(meter):
    (code,) = meter.mint("single", 5, "pi_13")
    assert meter.reserve(code).ok
    meter.pause(True)
    assert meter.reserve(code).reason == "paused"


def test_void_by_payment_voids_the_whole_batch(meter):
    batch = meter.mint("batch", 5, "pi_14", count=3)
    assert meter.void("pi_14") == 3
    for code in batch:
        assert meter.reserve(code).reason == "void"
        assert meter.status(code).remaining == 0
    assert meter.void("pi_14") == 0


def test_a_refund_arriving_first_blocks_the_mint(meter):
    meter.void("pi_15")
    with pytest.raises(PaymentVoided):
        meter.mint("single", 5, "pi_15")


def test_void_while_held_makes_settle_spend_nothing(meter):
    (code,) = meter.mint("single", 5, "pi_16")
    reservation = meter.reserve(code).reservation
    meter.void("pi_16")
    assert meter.settle(reservation, True) is None
    assert meter.status(code).tokens_used == 0


def test_group_ceiling_limits_a_day_and_resets_the_next(meter, clock):
    (code,) = meter.mint("group", 100, "pi_17")
    for _ in range(3):
        assert meter.settle(meter.reserve(code).reservation, True) is not None
    assert meter.reserve(code).reason == "daily_ceiling"
    clock.day = date(2026, 10, 6)
    assert meter.reserve(code).ok


def test_group_ceiling_counts_tokens_in_flight(meter):
    (code,) = meter.mint("group", 100, "pi_18")
    held = [meter.reserve(code) for _ in range(3)]
    assert all(h.ok for h in held)
    assert meter.reserve(code).reason == "daily_ceiling"


def test_group_ceiling_can_be_set_per_purchase(meter):
    (code,) = meter.mint("group", 100, "pi_19", daily_ceiling=1)
    meter.settle(meter.reserve(code).reservation, True)
    assert meter.reserve(code).reason == "daily_ceiling"


def test_non_group_codes_have_no_daily_ceiling(meter):
    (code,) = meter.mint("single", 50, "pi_20")
    for _ in range(10):
        assert meter.settle(meter.reserve(code).reservation, True) is not None


def test_last_used_is_a_week_not_a_day(meter, clock):
    (code,) = meter.mint("single", 2, "pi_21")
    meter.settle(meter.reserve(code).reservation, True)
    rows = meter._conn.execute("SELECT day_created, week_last_used FROM meter").fetchall()
    assert rows == [(clock.day.isoformat(), week_of(clock.day))]
    assert len(rows[0][1]) == len("0000-W00")
    assert week_of(date(2026, 10, 5)) == "2026-W41"


def test_purge_removes_spent_and_void_rows_thirty_days_after_their_last_week(meter, clock):
    (spent,) = meter.mint("single", 1, "pi_22")
    meter.settle(meter.reserve(spent).reservation, True)
    (voided,) = meter.mint("single", 1, "pi_23")
    meter.void("pi_23")
    (live,) = meter.mint("single", 5, "pi_24")
    (used,) = meter.mint("single", 5, "pi_25")
    meter.settle(meter.reserve(used).reservation, True)
    clock.day = date(2026, 11, 9)
    assert meter.purge() == 0
    clock.day = date(2026, 11, 10)
    assert meter.purge() == 3
    assert meter.status(spent) is None and meter.status(voided) is None
    assert meter.status(live) is not None and meter.status(used) is not None
    assert meter._conn.execute("SELECT COUNT(*) FROM voided_payments").fetchone() == (0,)


def test_balances_survive_a_restart_but_reservations_do_not(tmp_path, clock):
    path = str(tmp_path / "m.db")
    first = Meter(path, clock=clock)
    (code,) = first.mint("single", 3, "pi_26")
    first.settle(first.reserve(code).reservation, True)
    first.reserve(code)
    first.close()
    second = Meter(path, clock=clock)
    assert second.status(code).remaining == 2
    assert second.reserve(code).ok
    second.close()


def test_reconciliation_counts_by_day_and_reports_the_gap(meter, clock):
    meter.tally("payments_seen", 3)
    meter.tally("payments_minted", 2)
    meter.tally("codes_minted", 5)
    meter.tally("payments_voided_first")
    clock.day = date(2026, 10, 6)
    meter.tally("payments_seen")
    report = meter.reconciliation()
    assert [r["day"] for r in report] == [clock.day.isoformat(), date(2026, 10, 5).isoformat()]
    assert report[0]["gap"] == 1
    assert report[1]["gap"] == 0
    assert report[1]["codes_minted"] == 5


def test_tally_refuses_an_unknown_field(meter):
    with pytest.raises(ValueError):
        meter.tally("revenue")


def test_purge_drops_reconciliation_days_after_ninety(meter, clock):
    meter.tally("payments_seen")
    clock.day = date(2027, 1, 2)
    assert meter.purge() == 0
    clock.day = date(2027, 1, 3)
    assert meter.purge() == 1
    assert meter.reconciliation() == []


def test_a_table_round_reserves_and_spends_several_tokens_at_once(meter):
    (code,) = meter.mint("single", 7, "pi_t1")
    first = meter.reserve(code, 3)
    assert first.ok
    assert meter.settle(first.reservation, True) == 4
    second = meter.reserve(code, 3)
    assert meter.settle(second.reservation, True) == 1
    assert meter.reserve(code, 3).reason == "insufficient"
    assert meter.reserve(code, 1).ok


def test_a_released_round_returns_all_its_tokens(meter):
    (code,) = meter.mint("single", 3, "pi_t2")
    held = meter.reserve(code, 3)
    assert meter.reserve(code, 1).reason == "in_use"
    meter.release(held.reservation)
    assert meter.reserve(code, 3).ok
    assert meter.status(code).remaining == 3


def test_a_round_counts_in_full_against_a_group_ceiling(meter):
    (code,) = meter.mint("group", 100, "pi_t3")
    assert meter.reserve(code, 3).ok
    assert meter.reserve(code, 1).reason == "daily_ceiling"


def test_reserve_refuses_a_count_below_one(meter):
    (code,) = meter.mint("single", 3, "pi_t4")
    with pytest.raises(ValueError):
        meter.reserve(code, 0)


# ---- funds: what raises the door's ceiling ------------------------------------------

def test_funds_add_by_kind_and_sum_over_the_last_seven_days(meter):
    meter.add_funds("gift", 2500, "pi_a")
    meter.add_funds("purchase", 700, "pi_b")
    meter.add_funds("adjustment", 1000, note="friends and family")
    meter.add_funds("adjustment", -200, note="correction")
    assert meter.net_funds() == {"gift": 2500, "purchase": 700, "adjustment": 800}


def test_a_payment_adds_once_and_a_voided_one_adds_nothing(meter):
    assert meter.add_funds("gift", 2500, "pi_a") is not None
    assert meter.add_funds("gift", 2500, "pi_a") is None
    meter.void("pi_v")
    assert meter.add_funds("gift", 2500, "pi_v") is None
    assert meter.net_funds()["gift"] == 2500


def test_voiding_a_payment_or_reversing_an_entry_takes_it_out_of_the_sum(meter):
    meter.add_funds("gift", 2500, "pi_a")
    entry = meter.add_funds("adjustment", 1000, note="x")
    assert meter.void_funds("pi_a") == 1 and meter.void_funds("pi_a") == 0
    assert meter.reverse_funds(entry) and not meter.reverse_funds(entry)
    assert meter.net_funds() == {"gift": 0, "purchase": 0, "adjustment": 0}
    assert all(row["reversed"] for row in meter.list_funds())


@pytest.mark.parametrize(
    "args",
    [("grant", 5, "pi"), ("gift", 0, "pi"), ("gift", -5, "pi"), ("gift", 5, None), ("gift", 10_000_001, "pi"), ("gift", True, "pi"), ("gift", 5.5, "pi"), ("adjustment", 5, None, "x" * 201)],
)
def test_a_bad_entry_is_refused(meter, args):
    with pytest.raises(ValueError):
        meter.add_funds(*args)


def test_funds_older_than_the_window_leave_the_sum_and_are_purged_later(tmp_path):
    today = [date(2026, 10, 5)]
    meter = Meter(str(tmp_path / "m.db"), clock=lambda: today[0])
    meter.add_funds("gift", 2500, "pi_a")
    today[0] = date(2026, 10, 11)
    assert meter.net_funds()["gift"] == 2500
    today[0] = date(2026, 10, 12)
    assert meter.net_funds()["gift"] == 0
    assert len(meter.list_funds(days=30)) == 1
    today[0] = date(2027, 1, 5)
    meter.purge()
    assert meter.list_funds(days=365) == []
    meter.close()


def test_the_funds_table_holds_no_code_hash_and_no_note_of_a_buyer(meter):
    columns = {row[1] for row in meter._conn.execute("PRAGMA table_info(funds)")}
    assert columns == {"entry", "day", "kind", "cents", "payment_id", "note", "reversed"}


# ---- the standing measure: daily totals, no keys ------------------------------------------

def test_a_mint_counts_its_codes_by_kind_and_the_tokens_sold(meter):
    meter.mint("single", 1100, "pi_a")
    meter.mint("batch", 500, "pi_b", count=3)
    meter.mint("group", 2000, "pi_c")
    (today,) = meter.measures(1)
    assert (today["codes_single"], today["codes_batch"], today["codes_group"]) == (1, 3, 1)
    assert today["tokens_sold"] == 1100 + 500 * 3 + 2000


def test_only_a_settled_spend_counts_as_tokens_spent(meter):
    (code,) = meter.mint("single", 100, "pi_a")
    meter.settle(meter.reserve(code, 30).reservation, True)
    meter.settle(meter.reserve(code, 20).reservation, False)
    assert meter.measures(1)[0]["tokens_spent"] == 30


def test_a_refused_mint_counts_nothing(meter):
    meter.mint("single", 100, "pi_a")
    with pytest.raises(AlreadyMinted):
        meter.mint("single", 100, "pi_a")
    assert meter.measures(1)[0]["codes_single"] == 1


def test_refusals_and_the_door_peak_are_kept_by_day(meter, clock):
    meter.measure("refused_no_code")
    meter.measure("refused_no_code", 2)
    meter.measure_peak("door_stage", 2)
    meter.measure_peak("door_stage", 1)
    clock.day = date(2026, 10, 6)
    meter.measure("refused_spent")
    today, yesterday = meter.measures(2)
    assert (today["day"], today["refused_spent"], today["refused_no_code"]) == (clock.day.isoformat(), 1, 0)
    assert (yesterday["refused_no_code"], yesterday["door_stage"]) == (3, 2)


def test_an_unknown_measure_is_refused(meter):
    with pytest.raises(ValueError):
        meter.measure("visitors")
    with pytest.raises(ValueError):
        meter.measure_peak("refused_no_code", 1)


def test_measures_with_nothing_to_show_are_an_empty_list(meter):
    assert meter.measures(14) == []


def test_purge_drops_measures_after_ninety_days(meter, clock):
    meter.measure("refused_no_code")
    clock.day = date(2027, 1, 20)
    meter.measure("refused_spent")
    meter.purge()
    assert [row["day"] for row in meter.measures(400)] == [clock.day.isoformat()]


def test_a_failing_measure_never_loosens_the_group_ceiling(meter, monkeypatch):
    def down(*_a, **_k):
        raise RuntimeError("daily table down")

    monkeypatch.setattr(meter, "_add", down)
    (code,) = meter.mint("group", 100, "pi_ceiling", daily_ceiling=3)
    granted = 0
    for _ in range(8):
        admission = meter.reserve(code)
        if admission.ok:
            meter.settle(admission.reservation, True)
            granted += 1
    assert granted == 3
    assert meter.status(code).remaining == 97


def test_a_failing_measure_does_not_undo_a_purchase(meter, monkeypatch):
    def down(*_a, **_k):
        raise RuntimeError("daily table down")

    monkeypatch.setattr(meter, "_add", down)
    (code,) = meter.mint("single", 25, "pi_bought")
    assert meter.status(code).remaining == 25
    assert meter.payment_minted("pi_bought")
    assert meter.reconciliation()[0]["codes_minted"] == 1
