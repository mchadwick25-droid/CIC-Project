from datetime import date

import pytest

from engine.accounts.keys import KeyRing, PreviousKey
from engine.accounts.service import AccountsService, Limits
from engine.accounts.tests.conftest import ADDRESS_KEY, SESSION_KEY, sign_in, start_sign_in

ADDR = "ada@example.org"
NET = "203.0.113.5"


def test_a_code_works_once(svc, mailer):
    challenge, code = start_sign_in(svc, mailer)
    first = svc.finish_sign_in(challenge, ADDR, code, NET, 1990)
    assert first.status == "ok" and first.new_account and first.cookie
    assert svc.finish_sign_in(challenge, ADDR, code, NET, 1990).status == "wrong"


def test_a_code_dies_at_ten_minutes(svc, mailer, clock):
    challenge, code = start_sign_in(svc, mailer)
    clock.advance(599)
    assert svc.finish_sign_in(challenge, ADDR, code, NET, 1990).status == "ok"
    clock.advance(1000)
    challenge, code = start_sign_in(svc, mailer)
    clock.advance(600)
    assert svc.finish_sign_in(challenge, ADDR, code, NET, 1990).status == "wrong"


def test_five_wrong_tries_burn_the_code_even_for_the_right_one(svc, mailer):
    challenge, right = start_sign_in(svc, mailer)
    wrong = "000000" if right != "000000" else "111111"
    for _ in range(5):
        assert svc.finish_sign_in(challenge, ADDR, wrong, NET, 1990).status == "wrong"
    assert svc.finish_sign_in(challenge, ADDR, right, NET, 1990).status == "wrong"


def test_a_new_start_replaces_the_old_challenge_for_that_address(svc, mailer):
    old_challenge, old = start_sign_in(svc, mailer)
    new_challenge, new = start_sign_in(svc, mailer)
    assert svc.finish_sign_in(old_challenge, ADDR, old, NET, 1990).status == "wrong"
    assert svc.finish_sign_in(new_challenge, ADDR, new, NET, 1990).status == "ok"


def test_a_malformed_or_missing_challenge_or_code_is_just_wrong(svc, mailer):
    challenge, code = start_sign_in(svc, mailer)
    for bad in (None, "", [], {}, 5, "x" * 200):
        assert svc.finish_sign_in(bad, ADDR, code, NET, 1990).status == "wrong"
    for bad in (None, "", "abcdef", [], {}, "12"):
        assert svc.finish_sign_in(challenge, ADDR, bad, NET, 1990).status == "wrong"


def test_a_challenge_proves_only_the_address_and_kind_it_was_made_for(svc, mailer):
    challenge, code = start_sign_in(svc, mailer, ADDR)
    other, other_code = start_sign_in(svc, mailer, "bob@example.org", "192.0.2.9")
    assert svc.finish_sign_in(challenge, "bob@example.org", code, NET, 1990).status == "wrong"
    assert svc.finish_sign_in(other, ADDR, other_code, NET, 1990).status == "wrong"
    cookie = sign_in(svc, mailer, "carol@example.org", "198.51.100.3")
    stepped = svc.step_up_start(svc.session(cookie), "carol@example.org", "198.51.100.3")
    assert svc.finish_sign_in(stepped.challenge, "carol@example.org", mailer.last_code("carol@example.org"), NET, 1990).status == "wrong"


def test_start_reply_is_the_same_whether_or_not_an_account_exists(svc, mailer):
    sign_in(svc, mailer, ADDR)
    known = svc.start_sign_in(ADDR, NET)
    unknown = svc.start_sign_in("nobody@example.org", NET)
    assert known.status == unknown.status == "sent"
    assert len(known.challenge) == len(unknown.challenge) and known.cookie is None and unknown.cookie is None


def test_an_invalid_address_is_refused_before_anything_is_sent(svc, mailer):
    assert svc.start_sign_in("not an address", NET).status == "invalid_address"
    assert mailer.sent == []


def test_the_age_question_comes_after_the_code_proves_the_address(svc, mailer):
    challenge, code = start_sign_in(svc, mailer)
    assert svc.finish_sign_in(challenge, ADDR, code, NET).status == "needs_birth_year"
    assert svc.store.account_by_hashes([svc.keys.address_hash(ADDR)]) is None
    assert svc.finish_sign_in(challenge, ADDR, code, NET, 1990).status == "ok"


def test_under_sixteen_gets_no_account_and_nothing_is_stored(svc, mailer, store):
    challenge, code = start_sign_in(svc, mailer)
    year = svc.today().year
    assert svc.finish_sign_in(challenge, ADDR, code, NET, year - 15).status == "under_age"
    assert store.account_by_hashes(svc.keys.candidate_hashes(ADDR)) is None
    assert svc.finish_sign_in(challenge, ADDR, code, NET, 1990).status == "wrong"  # the code was burned
    assert store._d.execute("SELECT COUNT(*) FROM accounts").fetchone()[0] == 0


@pytest.mark.parametrize("age,band", [(16, "16-17"), (17, "16-17"), (18, "18+"), (70, "18+")])
def test_sixteen_and_over_may_open_an_account_with_a_coarse_band(svc, mailer, store, age, band):
    challenge, code = start_sign_in(svc, mailer)
    assert svc.finish_sign_in(challenge, ADDR, code, NET, svc.today().year - age).status == "ok"
    assert store.account_by_hashes(svc.keys.candidate_hashes(ADDR)).age_band == band


@pytest.mark.parametrize("bad", ["1990", 1899, 3000, True, 1990.5, None])
def test_a_nonsense_birth_year_never_opens_an_account_and_keeps_the_code(svc, mailer, bad):
    challenge, code = start_sign_in(svc, mailer)
    expected = "needs_birth_year" if bad is None else "invalid_birth_year"
    assert svc.finish_sign_in(challenge, ADDR, code, NET, bad).status == expected
    assert svc.finish_sign_in(challenge, ADDR, code, NET, 1990).status == "ok"


def test_the_account_holds_days_and_weeks_never_a_time(svc, mailer, store):
    sign_in(svc, mailer)
    account = store.account_by_hashes(svc.keys.candidate_hashes(ADDR))
    today = svc.today()
    assert account.day_created == today.isoformat()
    assert account.week_last_used == f"{today.isocalendar()[0]}-W{today.isocalendar()[1]:02d}"
    assert 1 <= account.refill_day <= 28


def test_sends_are_limited_per_address_per_network_and_globally(store, keys, mailer, clock):
    svc = AccountsService(store, keys, mailer, clock=clock, limits=Limits(sends_global_hour=6))
    assert [svc.start_sign_in(ADDR, NET).status for _ in range(4)] == ["sent", "sent", "sent", "throttled"]
    clock.advance(900)
    assert svc.start_sign_in(ADDR, NET).status == "sent"
    for i in range(3):
        svc.start_sign_in(f"p{i}@example.org", f"198.51.100.{i}")
    assert svc.start_sign_in("late@example.org", "198.51.100.99").status == "paused"
    clock.advance(3600)
    assert svc.start_sign_in("late@example.org", "198.51.100.99").status == "sent"


def test_the_ten_a_day_cap_per_address_holds(store, keys, mailer, clock):
    svc = AccountsService(store, keys, mailer, clock=clock)
    statuses = []
    for _ in range(12):
        statuses.append(svc.start_sign_in(ADDR, NET).status)
        clock.advance(901)
    assert statuses.count("sent") == 10


def test_a_network_may_open_only_so_many_new_accounts_a_day(store, keys, mailer, clock):
    svc = AccountsService(store, keys, mailer, clock=clock, limits=Limits(new_accounts_per_network_day=2))
    results = []
    for i in range(3):
        address = f"p{i}@example.org"
        challenge = svc.start_sign_in(address, NET).challenge
        results.append(svc.finish_sign_in(challenge, address, mailer.last_code(address), NET, 1990).status)
    assert results == ["ok", "ok", "throttled"]


def test_a_send_failure_keeps_no_challenge_and_logs_no_address(svc, mailer, caplog, store):
    mailer.fail = True
    with caplog.at_level("DEBUG", logger="cic.accounts"):
        assert svc.start_sign_in(ADDR, NET).status == "send_failed"
    assert "ada" not in caplog.text and "example.org" not in caplog.text
    assert store._e.execute("SELECT COUNT(*) FROM challenges").fetchone()[0] == 0


def test_a_signed_in_address_is_rekeyed_under_the_current_key(store, mailer, clock):
    old = KeyRing("o" * 40, SESSION_KEY, key_id="k0")
    sign_in(AccountsService(store, old, mailer, clock=clock), mailer)
    previous = [PreviousKey("k0", "o" * 40, date(2030, 1, 1))]
    rotated = KeyRing(ADDRESS_KEY, SESSION_KEY, key_id="k1", previous=previous, today=lambda: date(2026, 9, 21))
    second = AccountsService(store, rotated, mailer, clock=clock)
    clock.advance(1000)
    challenge = second.start_sign_in(ADDR, "203.0.113.9").challenge
    result = second.finish_sign_in(challenge, ADDR, mailer.last_code(ADDR), "203.0.113.9")
    assert result.status == "ok" and not result.new_account
    assert store._d.execute("SELECT address_hash FROM accounts").fetchone()[0].startswith("k1:")


def test_step_up_and_recovery_have_their_own_hourly_budget(store, keys, mailer, clock):
    svc = AccountsService(store, keys, mailer, clock=clock, limits=Limits(sends_global_hour=2, sends_global_hour_other=10))
    challenges = [svc.start_sign_in(f"p{i}@example.org", f"198.51.100.{i}").challenge for i in range(2)]
    assert svc.start_sign_in("late@example.org", "198.51.100.77").status == "paused"
    result = svc.finish_sign_in(challenges[1], "p1@example.org", mailer.last_code("p1@example.org"), "198.51.100.1", 1990)
    started = svc.step_up_start(svc.session(result.cookie), "p1@example.org", "198.51.100.1")
    assert started.status == "sent" and mailer.last_code("p1@example.org")


def test_a_wider_block_of_addresses_is_limited_as_well_as_each_network(store, keys, mailer, clock):
    svc = AccountsService(store, keys, mailer, clock=clock, limits=Limits(sends_per_coarse_network_15min=3))
    results = [svc.start_sign_in(f"p{i}@example.org", f"203.0.113.{i + 1}").status for i in range(5)]
    assert results == ["sent", "sent", "sent", "throttled", "throttled"]
    assert svc.start_sign_in("far@example.org", "198.51.100.9").status == "sent"
