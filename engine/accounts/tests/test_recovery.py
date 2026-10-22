from datetime import timedelta

from engine.accounts.tests.conftest import sign_in, stepped_up_session

ADDR = "ada@example.org"
NEW = "ada.new@example.org"
NET = "203.0.113.5"
OTHER_NET = "198.51.100.7"


def _recovery_code(svc, mailer, clock):
    session, cookie = stepped_up_session(svc, mailer, clock)
    code = svc.make_recovery_code(session).recovery_code
    return code, cookie


def test_a_recovery_code_is_long_shown_once_and_stored_only_as_a_hash(svc, mailer, clock, store):
    code, _ = _recovery_code(svc, mailer, clock)
    assert len(code) == 20
    assert store._d.execute("SELECT code_hash FROM recovery_codes").fetchone()[0] != code


def test_a_new_recovery_code_replaces_the_old_one(svc, mailer, clock):
    code, cookie = _recovery_code(svc, mailer, clock)
    again = svc.make_recovery_code(svc.session(cookie)).recovery_code
    assert again != code
    assert svc.recover_start(code, NEW, OTHER_NET).status == "wrong"
    assert svc.recover_start(again, NEW, OTHER_NET).status == "sent"


def test_recovery_waits_a_week_and_then_the_new_address_owns_the_account(svc, mailer, clock, store):
    code, cookie = _recovery_code(svc, mailer, clock)
    account_id = svc.session(cookie).account_id
    start = svc.recover_start(code, NEW, OTHER_NET)
    week_on = (svc.today() + timedelta(days=7)).isoformat()
    assert start.status == "sent" and start.effective_on == week_on
    assert svc.recover_finish(NEW, mailer.last_code(NEW), OTHER_NET).status == "waiting"
    assert svc.session(cookie).pending_recovery  # the old owner sees the banner
    svc.start_sign_in(NEW, OTHER_NET)
    waiting = svc.finish_sign_in(NEW, mailer.last_code(NEW), OTHER_NET, 1990)
    assert waiting.status == "recovery_waiting" and waiting.effective_on == week_on
    clock.advance(7 * 86400)
    svc.start_sign_in(NEW, OTHER_NET)
    result = svc.finish_sign_in(NEW, mailer.last_code(NEW), OTHER_NET)
    assert result.status == "ok" and not result.new_account
    assert svc.session(result.cookie).account_id == account_id
    assert svc.session(cookie) is None  # every old session ended
    assert not store.has_recovery_code(account_id)  # the used code is gone


def test_a_recovery_code_is_burned_by_its_first_use(svc, mailer, clock):
    code, _ = _recovery_code(svc, mailer, clock)
    assert svc.recover_start(code, NEW, OTHER_NET).status == "sent"
    assert svc.recover_start(code, "x@example.org", OTHER_NET).status == "wrong"


def test_the_old_owner_can_cancel_a_recovery_a_thief_started(svc, mailer, clock):
    code, cookie = _recovery_code(svc, mailer, clock)
    svc.recover_start(code, "thief@example.org", OTHER_NET)
    svc.recover_finish("thief@example.org", mailer.last_code("thief@example.org"), OTHER_NET)
    assert svc.session(cookie).pending_recovery
    session = svc.session(cookie)
    svc.step_up_start(session, ADDR, NET)
    svc.step_up_finish(svc.session(cookie), ADDR, mailer.last_code(ADDR), NET)
    assert svc.cancel_recovery(svc.session(cookie)).status == "ok"
    assert not svc.session(cookie).pending_recovery
    clock.advance(8 * 86400)
    svc.start_sign_in("thief@example.org", OTHER_NET)
    # the thief now meets an ordinary new-account sign-in, not the old owner's account
    result = svc.finish_sign_in("thief@example.org", mailer.last_code("thief@example.org"), OTHER_NET, 1990)
    assert result.new_account
    assert svc.session(result.cookie).account_id != svc.session(cookie).account_id


def test_recovery_refuses_a_bad_code_a_taken_address_and_bad_input(svc, mailer, clock):
    code, _ = _recovery_code(svc, mailer, clock)
    sign_in(svc, mailer, "bob@example.org", "192.0.2.9")
    assert svc.recover_start("AAAAAAAAAAAAAAAAAAAA", NEW, OTHER_NET).status == "wrong"
    assert svc.recover_start(None, NEW, OTHER_NET).status == "wrong"
    assert svc.recover_start(code, "bob@example.org", OTHER_NET).status == "wrong"
    assert svc.recover_start(code, "not an address", OTHER_NET).status == "wrong"


def test_recovery_attempts_are_limited_per_network(svc, mailer, clock):
    results = [svc.recover_start("AAAAAAAAAAAAAAAAAAAA", NEW, OTHER_NET).status for _ in range(7)]
    assert results[:5] == ["wrong"] * 5 and results[5:] == ["throttled"] * 2


def test_an_address_change_needs_the_old_address_then_a_code_to_the_new_one(svc, mailer, clock):
    session, cookie = stepped_up_session(svc, mailer, clock)
    other = sign_in(svc, mailer, ADDR, "198.51.100.30")  # a second device
    assert svc.change_address_start(session, NEW, NET).status == "sent"
    assert svc.change_address_finish(session, NEW, "000000", NET).status == "wrong"
    assert svc.change_address_finish(svc.session(cookie), NEW, mailer.last_code(NEW), NET).status == "ok"
    assert svc.session(other) is None and svc.session(cookie) is not None
    clock.advance(901)
    svc.start_sign_in(ADDR, NET)
    reply = svc.finish_sign_in(ADDR, mailer.last_code(ADDR), NET)
    assert reply.status == "needs_birth_year"  # the old address no longer reaches the account
    svc.start_sign_in(NEW, NET)
    assert svc.finish_sign_in(NEW, mailer.last_code(NEW), NET).status == "ok"


def test_an_address_change_to_another_account_s_address_is_refused(svc, mailer, clock):
    sign_in(svc, mailer, "bob@example.org", "192.0.2.9")
    session, _ = stepped_up_session(svc, mailer, clock)
    assert svc.change_address_start(session, "bob@example.org", NET).status == "cannot_use"


def test_a_code_for_one_account_s_change_cannot_finish_another(svc, mailer, clock):
    session, cookie = stepped_up_session(svc, mailer, clock)
    other, other_cookie = stepped_up_session(svc, mailer, clock, "bob@example.org", "192.0.2.9")
    svc.change_address_start(session, NEW, NET)
    code = mailer.last_code(NEW)
    assert svc.change_address_finish(other, NEW, code, NET).status == "wrong"
