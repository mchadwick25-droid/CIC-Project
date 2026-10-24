"""The meter's coupon source: a gift code with no payment and no last day."""
import sqlite3
from datetime import date

import pytest

from engine.deeper import codes
from engine.deeper.meter import Meter, PaymentVoided


class Clock:
    def __call__(self):
        return date(2026, 10, 24)


@pytest.fixture
def meter(tmp_path):
    m = Meter(str(tmp_path / "meter.db"), clock=Clock())
    yield m
    m.close()


def make(meter, payment="coupon_a1", tokens=3000):
    (code,) = meter.mint("single", tokens, payment, 1, source="coupon")
    return code


def test_a_coupon_code_is_a_live_single_code_with_no_last_day(meter):
    code = make(meter)
    status = meter.status(code)
    assert (status.kind, status.status, status.remaining, status.expires_on) == ("single", "live", 3000, None)


def test_a_coupon_needs_its_own_prefix_and_never_a_last_day(meter):
    with pytest.raises(ValueError):
        meter.mint("single", 100, "tester_x", 1, source="coupon")
    with pytest.raises(ValueError):
        meter.mint("single", 100, "coupon_x", 1, source="coupon", expires_in_days=5)
    with pytest.raises(ValueError):
        meter.mint("single", 100, "coupon_x", 1)  # a purchase cannot borrow a grant's id


def test_a_coupon_counts_in_its_own_column_and_never_as_a_payment_or_money_owed(meter):
    make(meter)
    day = meter.reconciliation(1)[0]
    assert day["coupon_codes_minted"] == 1
    assert (day["payments_seen"], day["codes_minted"], day["admin_codes_minted"], day["tester_codes_minted"]) == (0, 0, 0, 0)
    assert meter.owed() == []
    assert [g["grant_id"] for g in meter.grants()] == ["coupon_a1"]


def test_the_hash_of_a_made_coupon_is_found_without_the_plain_code(meter):
    code = make(meter)
    assert meter.code_hash_of_payment("coupon_a1") == codes.hash_code(code)
    assert meter.code_hash_of_payment("coupon_none") is None


def test_a_cancelled_coupon_has_no_hash_to_attach_and_cannot_be_made_again(meter):
    make(meter)
    meter.void("coupon_a1")
    assert meter.code_hash_of_payment("coupon_a1") is None
    with pytest.raises(PaymentVoided):
        make(meter)


def test_the_gift_amounts_are_the_unspent_tokens_of_live_coupons_only(meter):
    gift, other = make(meter, "coupon_a1", 3000), make(meter, "coupon_a2", 500)
    (paid,) = meter.mint("single", 900, "pi_paid", 1)
    tester = meter.mint("single", 400, "tester_x", 1, source="tester", expires_in_days=3)[0]
    hashes = [codes.hash_code(c) for c in (gift, other, paid, tester)]
    assert meter.coupon_tokens_left(hashes) == [3000, 500]
    meter.settle(meter.reserve(gift, 1000).reservation, True)
    assert meter.coupon_tokens_left(hashes) == [2000, 500]
    meter.void("coupon_a2")
    assert meter.coupon_tokens_left(hashes) == [2000]
    assert meter.coupon_tokens_left([]) == []


def test_a_meter_made_before_coupons_gains_the_column(tmp_path):
    path = str(tmp_path / "old.db")
    conn = sqlite3.connect(path)
    conn.execute(
        "CREATE TABLE reconcile (day TEXT PRIMARY KEY, payments_seen INTEGER NOT NULL DEFAULT 0, payments_minted INTEGER NOT NULL DEFAULT 0,"
        " payments_voided_first INTEGER NOT NULL DEFAULT 0, codes_minted INTEGER NOT NULL DEFAULT 0, refunds_applied INTEGER NOT NULL DEFAULT 0,"
        " partial_refunds_ignored INTEGER NOT NULL DEFAULT 0) WITHOUT ROWID"
    )
    conn.commit()
    conn.close()
    meter = Meter(path, clock=Clock())
    make(meter)
    assert meter.reconciliation(1)[0]["coupon_codes_minted"] == 1
    meter.close()
