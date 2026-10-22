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
    assert start.status == "sent" and start.effective_on is None
    finished = svc.recover_finish(NEW, mailer.last_code(NEW), OTHER_NET)
    assert finished.status == "waiting" and finished.effective_on == week_on
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
    assert result.recovery_code and result.recovery_code != code  # the used code is replaced, shown once
    assert svc.recover_start(code, "late@example.org", OTHER_NET).status == "wrong"


def test_a_recovery_code_is_spent_when_the_new_address_is_proved(svc, mailer, clock):
    code, _ = _recovery_code(svc, mailer, clock)
    assert svc.recover_start(code, NEW, OTHER_NET).status == "sent"
    assert svc.recover_start(code, NEW, OTHER_NET).status == "sent"  # not yet spent; a resend is possible
    assert svc.recover_finish(NEW, mailer.last_code(NEW), OTHER_NET).status == "waiting"
    assert svc.recover_start(code, "x@example.org", OTHER_NET).status == "wrong"


def test_a_failed_send_does_not_spend_the_recovery_code(svc, mailer, clock, store):
    code, _ = _recovery_code(svc, mailer, clock)
    mailer.fail = True
    assert svc.recover_start(code, NEW, OTHER_NET).status == "send_failed"
    mailer.fail = False
    assert store.account_by_recovery_hash(__import__("hashlib").sha256(code.encode()).hexdigest()) is not None
    assert svc.recover_start(code, NEW, OTHER_NET).status == "sent"


def test_a_recovery_never_proved_expires_in_a_day(svc, mailer, clock, store):
    code, cookie = _recovery_code(svc, mailer, clock)
    svc.recover_start(code, NEW, OTHER_NET)
    assert svc.session(cookie).pending_recovery
    clock.advance(2 * 86400)
    svc.purge()
    session = svc.session(cookie)
    assert session is not None and not session.pending_recovery


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


def test_recovery_refuses_a_bad_code_and_bad_input(svc, mailer, clock):
    code, _ = _recovery_code(svc, mailer, clock)
    assert svc.recover_start("AAAAAAAAAAAAAAAAAAAA", NEW, OTHER_NET).status == "wrong"
    assert svc.recover_start(None, NEW, OTHER_NET).status == "wrong"
    assert svc.recover_start(code, "not an address", OTHER_NET).status == "wrong"


def test_the_replies_never_say_whether_an_address_has_an_account(svc, mailer, clock):
    sign_in(svc, mailer, "bob@example.org", "192.0.2.9")
    code, _ = _recovery_code(svc, mailer, clock)
    taken = svc.recover_start(code, "bob@example.org", OTHER_NET)
    free = svc.recover_start(code, NEW, OTHER_NET)
    assert taken.status == free.status == "sent"
    sent_to_bob = [c for a, c in mailer.sent if a == "bob@example.org"]
    assert len(sent_to_bob) == 1  # only his own sign-in code
    clock.advance(901)
    session, _ = stepped_up_session(svc, mailer, clock, ADDR, "198.51.100.40")
    a = svc.change_address_start(session, "bob@example.org", NET)
    b = svc.change_address_start(session, "carol@example.org", NET)
    assert a.status == b.status == "sent"
    assert len([1 for addr, _ in mailer.sent if addr == "bob@example.org"]) == 1
    assert len([1 for addr, _ in mailer.sent if addr == "carol@example.org"]) == 1


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


def test_an_address_change_to_another_account_s_address_sends_nothing_and_changes_nothing(svc, mailer, clock, store):
    sign_in(svc, mailer, "bob@example.org", "192.0.2.9")
    session, cookie = stepped_up_session(svc, mailer, clock)
    before = len(mailer.sent)
    assert svc.change_address_start(session, "bob@example.org", NET).status == "sent"
    assert len(mailer.sent) == before
    assert svc.change_address_finish(svc.session(cookie), "bob@example.org", "123456", NET).status == "wrong"
    assert store.account_by_hashes(svc.keys.candidate_hashes(ADDR)) is not None


def test_a_code_for_one_account_s_change_cannot_finish_another(svc, mailer, clock):
    session, cookie = stepped_up_session(svc, mailer, clock)
    other, other_cookie = stepped_up_session(svc, mailer, clock, "bob@example.org", "192.0.2.9")
    svc.change_address_start(session, NEW, NET)
    code = mailer.last_code(NEW)
    assert svc.change_address_finish(other, NEW, code, NET).status == "wrong"


def test_a_stranger_cannot_block_a_recovery_by_starting_one_to_the_same_address(svc, mailer, clock):
    code, cookie = _recovery_code(svc, mailer, clock)
    sign_in(svc, mailer, "mallory@example.org", "192.0.2.50")
    session, mcookie = stepped_up_session(svc, mailer, clock, "mallory@example.org", "192.0.2.50")
    mallory_code = svc.make_recovery_code(svc.session(mcookie)).recovery_code
    assert svc.recover_start(mallory_code, NEW, "192.0.2.51").status == "sent"  # unproved, proves nothing
    assert svc.recover_start(code, NEW, OTHER_NET).status == "sent"
    assert svc.recover_finish(NEW, mailer.last_code(NEW), OTHER_NET).status == "waiting"
    assert svc.recover_finish(NEW, mailer.last_code(NEW), "192.0.2.52").status == "wrong"  # one proof, one account


def test_an_address_taken_during_the_wait_moves_nothing_and_replaces_no_recovery_code(svc, mailer, clock, store):
    code, cookie = _recovery_code(svc, mailer, clock)
    account_id = svc.session(cookie).account_id
    svc.recover_start(code, NEW, OTHER_NET)
    svc.recover_finish(NEW, mailer.last_code(NEW), OTHER_NET)
    other_account_id = store.create_account(__import__("engine.accounts.store", fromlist=["Account"]).Account(
        "f" * 32, svc.keys.address_hash(NEW), "x", 1, "x", "18+")) and "f" * 32
    owner_code = svc._issue_recovery_code(other_account_id)
    clock.advance(7 * 86400)
    svc.start_sign_in(NEW, OTHER_NET)
    result = svc.finish_sign_in(NEW, mailer.last_code(NEW), OTHER_NET)
    assert result.status == "ok" and result.recovery_code is None
    assert svc.session(result.cookie).account_id == other_account_id
    assert store.account_by_recovery_hash(__import__("hashlib").sha256(owner_code.encode()).hexdigest()) == other_account_id
    assert store.account(account_id) is not None and store.pending_for_account(account_id) is None
