from datetime import timedelta  # noqa: F401

from engine.accounts.service import AccountsService, Limits
from engine.accounts.tests.conftest import sign_in, stepped_up_session

ADDR = "ada@example.org"
NEW = "ada.new@example.org"
NET = "203.0.113.5"


def test_an_address_change_needs_the_old_address_then_a_code_to_the_new_one(svc, mailer, clock):
    session, cookie = stepped_up_session(svc, mailer, clock)
    other = sign_in(svc, mailer, ADDR, "198.51.100.30")  # a second device
    started = svc.change_address_start(session, NEW, NET)
    assert started.status == "sent"
    assert svc.change_address_finish(session, started.challenge, "000000", NET).status == "wrong"
    assert svc.change_address_finish(svc.session(cookie), started.challenge, mailer.last_code(NEW), NET).status == "ok"
    assert svc.session(other) is None and svc.session(cookie) is not None
    clock.advance(901)
    old = svc.start_sign_in(ADDR, NET).challenge
    assert svc.finish_sign_in(old, ADDR, mailer.last_code(ADDR), NET).status == "needs_birth_date"  # no account at the old address
    new = svc.start_sign_in(NEW, NET).challenge
    assert svc.finish_sign_in(new, NEW, mailer.last_code(NEW), NET).status == "ok"


def test_an_address_change_to_another_account_s_address_sends_nothing_and_changes_nothing(svc, mailer, clock, store):
    sign_in(svc, mailer, "bob@example.org", "192.0.2.9")
    session, cookie = stepped_up_session(svc, mailer, clock)
    before = len(mailer.sent)
    started = svc.change_address_start(session, "bob@example.org", NET)
    assert started.status == "sent" and len(mailer.sent) == before
    for guess in ("000000", "123456", "654321"):
        assert svc.change_address_finish(svc.session(cookie), started.challenge, guess, NET).status == "wrong"
    assert store.account_by_hashes(svc.keys.candidate_hashes(ADDR)) is not None


def test_the_replies_never_say_whether_an_address_has_an_account(svc, mailer, clock):
    sign_in(svc, mailer, "bob@example.org", "192.0.2.9")
    mails_to_bob = len([1 for to, _ in mailer.sent if to == "bob@example.org"])
    clock.advance(901)
    session, _ = stepped_up_session(svc, mailer, clock, ADDR, "198.51.100.40")
    taken = svc.change_address_start(session, "bob@example.org", NET)
    free = svc.change_address_start(session, "carol@example.org", NET)
    assert taken.status == free.status == "sent" and taken.challenge and free.challenge
    assert len([1 for to, _ in mailer.sent if to == "bob@example.org"]) == mails_to_bob  # nothing is sent to bob
    assert len([1 for to, _ in mailer.sent if to == "carol@example.org"]) == 1


def test_a_challenge_for_one_account_s_change_cannot_finish_another(svc, mailer, clock):
    session, cookie = stepped_up_session(svc, mailer, clock)
    other, other_cookie = stepped_up_session(svc, mailer, clock, "bob@example.org", "192.0.2.9")
    started = svc.change_address_start(session, NEW, NET)
    code = mailer.last_code(NEW)
    assert svc.change_address_finish(other, started.challenge, code, NET).status == "wrong"


def test_many_accounts_cannot_send_more_than_a_few_codes_to_one_inbox(svc, mailer, clock):
    victim = "victim@example.org"
    for i in range(10):
        network = f"198.51.100.{i + 1}"
        session, _ = stepped_up_session(svc, mailer, clock, f"attacker{i}@example.org", network)
        svc.change_address_start(session, victim, network)
    assert len([1 for to, _ in mailer.sent if to == victim]) == svc.limits.sends_per_address_open_15min


def test_an_owner_can_always_prove_their_address_however_full_the_shared_budgets_are(store, keys, mailer, clock):
    svc = AccountsService(store, keys, mailer, clock=clock, limits=Limits(sends_global_hour_other=1))
    session, cookie = stepped_up_session(svc, mailer, clock)
    svc.change_address_start(session, "x1@example.org", NET)
    assert svc.change_address_start(svc.session(cookie), "x2@example.org", "198.51.100.8").status == "paused"
    clock.advance(601)  # the first step-up lapses
    started = svc.step_up_start(svc.session(cookie), ADDR, NET)
    assert started.status == "sent"
    assert svc.step_up_finish(svc.session(cookie), started.challenge, mailer.last_code(ADDR), NET).status == "ok"
    assert svc.session(cookie).stepped_up


def test_one_account_cannot_send_more_than_its_daily_share_of_mail(store, keys, mailer, clock):
    svc = AccountsService(store, keys, mailer, clock=clock, limits=Limits(account_actions_15min=100, account_actions_day=4))
    session, cookie = stepped_up_session(svc, mailer, clock)  # the helper's own step-up is the first of the four
    statuses = [svc.step_up_start(svc.session(cookie), ADDR, NET).status for _ in range(5)]
    assert statuses == ["sent", "sent", "sent", "throttled", "throttled"]
    clock.advance(86400)
    assert svc.step_up_start(svc.session(cookie), ADDR, NET).status == "sent"
