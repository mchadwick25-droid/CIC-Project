"""Coupons: a gift of tokens kept under the keyed hash of an address and attached at that person's next sign-in."""
import dataclasses
from datetime import date, timedelta
from types import SimpleNamespace

import pytest

from engine.accounts.keys import KeyRing, PreviousKey
from engine.accounts.service import AccountsService
from engine.accounts.store import AccountStore
from engine.accounts.tests.conftest import ADDRESS_KEY, SESSION_KEY, START, FakeVerifier, provider_sign_in, sign_in, start_sign_in
from engine.api.coupon_routes import coupon_code_hash
from engine.deeper.meter import Meter

ADDR = "ada@example.org"
MAX, PER_DAY = 20000, 20


class AddressVerifier(FakeVerifier):
    """A provider token is "<subject>|<nonce>"; the address it vouches for is set per subject."""

    def __init__(self, addresses):
        super().__init__()
        self.addresses = addresses

    def verified_address(self, provider, id_token, nonce):
        subject, _, given = id_token.rpartition("|")
        return self.addresses.get(subject) if given == nonce else None


@pytest.fixture
def meter(tmp_path, clock):
    m = Meter(str(tmp_path / "m.db"), clock=lambda: date(2026, 10, 24))
    yield m
    m.close()


@pytest.fixture
def wired(svc, meter):
    svc.coupon_code_hash = coupon_code_hash(SimpleNamespace(meter=meter))
    return svc


def approve(svc, address=ADDR, tokens=3000, **kw):
    return svc.coupon_approve(address, tokens, max_tokens=kw.get("max_tokens", MAX), max_per_day=kw.get("max_per_day", PER_DAY))


def sign_in_result(svc, mailer, address=ADDR):
    challenge, code = start_sign_in(svc, mailer, address)
    result = svc.finish_sign_in(challenge, address, code, "203.0.113.5", True)
    assert result.status == "ok"
    return result


def held(svc, result):
    return svc.store.code_scrambles_of(svc.session(result.cookie).account_id)


def test_approving_keeps_the_hash_the_amount_and_the_day_and_nothing_else(wired, store, tmp_path):
    made = approve(wired)
    assert made.status == "ok" and set(made.data) == {"coupon_id", "tokens", "day_made"}
    assert made.data["coupon_id"].startswith("coupon_") and made.data["tokens"] == 3000
    row = store._d.execute("SELECT * FROM pending_coupons").fetchone()
    assert row[1] == wired.keys.address_hash(ADDR) and row[2] == 3000
    store.close()
    assert ADDR.encode() not in (tmp_path / "d.db").read_bytes()
    assert b"ada" not in (tmp_path / "d.db").read_bytes()


def test_the_reply_is_the_same_whether_or_not_the_address_has_an_account(wired, mailer):
    sign_in(wired, mailer, "known@example.org")
    known = approve(wired, "known@example.org")
    unknown = approve(wired, "stranger@example.org")
    assert known.status == unknown.status == "ok"
    assert set(known.data) == set(unknown.data) and known.data["tokens"] == unknown.data["tokens"]


@pytest.mark.parametrize("address", ["", "no-at-sign", "a@b", None, 5])
def test_a_bad_address_keeps_nothing(wired, address):
    assert approve(wired, address).status == "invalid_address"
    assert wired.coupon_pending() == []


@pytest.mark.parametrize("tokens", [0, -1, MAX + 1, True, 3.5, "3000", None])
def test_a_bad_amount_keeps_nothing(wired, tokens):
    assert approve(wired, tokens=tokens).status == "invalid_tokens"
    assert wired.coupon_pending() == []


def test_the_day_s_limit_counts_a_cancelled_coupon_too(wired):
    first, second = approve(wired, max_per_day=2), approve(wired, "b@example.org", max_per_day=2)
    assert first.status == second.status == "ok"
    assert wired.coupon_cancel(first.data["coupon_id"]) is True
    assert approve(wired, "c@example.org", max_per_day=2).status == "limit"
    assert len(wired.coupon_pending()) == 1


def test_a_coupon_attaches_at_the_next_sign_in_and_only_once(wired, mailer):
    approve(wired)
    first = sign_in_result(wired, mailer)
    assert first.data["coupons"] == [3000] and len(held(wired, first)) == 1
    assert wired.coupon_pending() == []
    again = sign_in_result(wired, mailer)
    assert again.data["coupons"] == [] and len(held(wired, again)) == 1


def test_a_new_account_gets_the_coupon_kept_before_it_existed(wired, mailer):
    approve(wired, "new@example.org", 1100)
    result = sign_in_result(wired, mailer, "new@example.org")
    assert result.new_account is True and result.data["coupons"] == [1100]


def test_the_address_matches_however_it_is_typed(wired, mailer):
    approve(wired, "  Ada@Example.ORG ")
    assert sign_in_result(wired, mailer, ADDR).data["coupons"] == [3000]


def test_another_address_gets_nothing_and_the_coupon_keeps_waiting(wired, mailer):
    approve(wired)
    assert sign_in_result(wired, mailer, "other@example.org").data["coupons"] == []
    assert len(wired.coupon_pending()) == 1


def test_several_coupons_for_one_address_all_attach(wired, mailer):
    approve(wired, tokens=1100)
    approve(wired, tokens=500)
    result = sign_in_result(wired, mailer)
    assert sorted(result.data["coupons"]) == [500, 1100] and len(held(wired, result)) == 2


def test_a_cancelled_coupon_does_not_attach(wired, mailer):
    made = approve(wired)
    assert wired.coupon_cancel(made.data["coupon_id"]) is True
    assert sign_in_result(wired, mailer).data["coupons"] == []
    assert wired.coupon_cancel(made.data["coupon_id"]) is False
    assert wired.coupon_cancel("coupon_nothing") is False and wired.coupon_cancel(None) is False


def test_the_pending_list_shows_ids_amounts_and_days_and_no_address(wired):
    approve(wired)
    (row,) = wired.coupon_pending()
    assert set(row) == {"coupon_id", "tokens", "day_made"}
    assert ADDR not in str(row) and "ada" not in str(row) and "k1:" not in str(row)


def test_a_coupon_nobody_claims_lapses_after_the_set_days_and_not_before(wired, clock):
    wired.coupon_unclaimed_days = 90
    approve(wired)
    clock.advance(90 * 86400)
    wired.purge()
    assert len(wired.coupon_pending()) == 1
    clock.advance(2 * 86400)
    wired.purge()
    assert wired.coupon_pending() == []


def test_with_no_meter_wired_the_coupon_waits_and_sign_in_is_unharmed(svc, mailer):
    approve(svc)
    result = sign_in_result(svc, mailer)
    assert result.data["coupons"] == [] and len(svc.coupon_pending()) == 1


def test_a_fault_while_attaching_never_fails_the_sign_in_and_the_next_one_finishes_it(wired, mailer, meter, monkeypatch):
    approve(wired)
    real = wired.store.claim_coupon

    def broken(*args, **kwargs):
        raise RuntimeError("disk")

    monkeypatch.setattr(wired.store, "claim_coupon", broken)
    failed = sign_in_result(wired, mailer)
    assert failed.data["coupons"] == [] and held(wired, failed) == []
    monkeypatch.setattr(wired.store, "claim_coupon", real)
    done = sign_in_result(wired, mailer)
    assert done.data["coupons"] == [3000] and len(held(wired, done)) == 1
    (coupon_id,) = {r[0] for r in meter._conn.execute("SELECT payment_id FROM meter")}
    assert coupon_id.startswith("coupon_")
    assert meter._conn.execute("SELECT COUNT(*) FROM meter").fetchone()[0] == 1  # made once, found the second time


def test_an_account_at_its_code_limit_leaves_the_coupon_waiting(wired, mailer):
    approve(wired)
    wired.limits = dataclasses.replace(wired.limits, codes_per_account=0)
    result = sign_in_result(wired, mailer)
    assert result.data["coupons"] == [] and len(wired.coupon_pending()) == 1


def test_the_coupon_s_code_is_a_live_gift_with_no_last_day_counted_as_a_coupon(wired, mailer, meter):
    approve(wired, tokens=3000)
    sign_in_result(wired, mailer)
    ((payment, tokens, used, status, expires),) = meter._conn.execute(
        "SELECT payment_id, tokens_total, tokens_used, status, expires_on FROM meter"
    ).fetchall()
    assert payment.startswith("coupon_") and (tokens, used, status, expires) == (3000, 0, "live", None)
    assert meter.reconciliation(1)[0]["coupon_codes_minted"] == 1
    assert meter.owed() == []


def test_a_coupon_is_found_after_the_address_key_is_rotated(tmp_path, mailer, clock, meter, contacts):
    old = KeyRing(ADDRESS_KEY, SESSION_KEY)
    store = AccountStore(str(tmp_path / "r.db"), str(tmp_path / "re.db"))
    first = AccountsService(store, old, mailer, clock=clock, contacts=contacts)
    first.coupon_approve(ADDR, 3000, max_tokens=MAX, max_per_day=PER_DAY)
    retire = date.fromtimestamp(START) + timedelta(days=30)
    rotated = KeyRing("n" * 40, SESSION_KEY, key_id="k2", previous=[PreviousKey("k1", ADDRESS_KEY, retire)], today=lambda: date.fromtimestamp(START))
    second = AccountsService(store, rotated, mailer, clock=clock, contacts=contacts)
    second.coupon_code_hash = coupon_code_hash(SimpleNamespace(meter=meter))
    assert sign_in_result(second, mailer).data["coupons"] == [3000]
    store.close()


def test_a_google_sign_in_with_a_verified_address_gets_the_coupon_and_the_address_opens_nothing(svc, meter, mailer):
    svc.verifier = AddressVerifier({"g-ada": ADDR})
    svc.coupon_code_hash = coupon_code_hash(SimpleNamespace(meter=meter))
    approve(svc)
    nonce = svc.provider_start("203.0.113.5").challenge
    result = svc.provider_sign_in("google", f"g-ada|{nonce}", nonce, "203.0.113.5", True)
    assert result.status == "ok" and result.data["coupons"] == [3000]
    account = svc.store.account(svc.session(result.cookie).account_id)
    assert account.address_hash is None  # the provider's address was used to find a coupon, never to keep or link


def test_a_provider_with_no_verified_address_or_a_relay_one_attaches_nothing(svc, meter):
    svc.verifier = AddressVerifier({"g-ada": None})
    svc.coupon_code_hash = coupon_code_hash(SimpleNamespace(meter=meter))
    approve(svc)
    cookie = provider_sign_in(svc)
    assert svc.store.code_scrambles_of(svc.session(cookie).account_id) == [] and len(svc.coupon_pending()) == 1


def test_a_returning_provider_account_gets_a_coupon_kept_after_it_was_made(svc, meter):
    svc.verifier = AddressVerifier({"g-ada": ADDR})
    svc.coupon_code_hash = coupon_code_hash(SimpleNamespace(meter=meter))
    provider_sign_in(svc)
    approve(svc)
    nonce = svc.provider_start("203.0.113.5").challenge
    again = svc.provider_sign_in("google", f"g-ada|{nonce}", nonce, "203.0.113.5")
    assert again.status == "ok" and again.data["coupons"] == [3000]


def test_a_verifier_without_the_address_call_still_signs_in(svc, meter):
    svc.coupon_code_hash = coupon_code_hash(SimpleNamespace(meter=meter))
    approve(svc)
    cookie = provider_sign_in(svc)  # the plain fake verifier has no verified_address
    assert svc.session(cookie) is not None and len(svc.coupon_pending()) == 1
