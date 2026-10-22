import hashlib
from datetime import timedelta

from engine.accounts.tests.conftest import sign_in, stepped_up_session

ADDR = "ada@example.org"
NEW = "ada.new@example.org"
NET = "203.0.113.5"
OTHER_NET = "198.51.100.7"


def _recovery_code(svc, mailer, clock):
    session, cookie = stepped_up_session(svc, mailer, clock)
    return svc.make_recovery_code(session).recovery_code, cookie


def _start(svc, code, address=NEW, network=OTHER_NET):
    result = svc.recover_start(code, address, network)
    assert result.status == "sent", result.status
    return result.challenge


def test_a_recovery_code_is_long_shown_once_and_stored_only_as_a_hash(svc, mailer, clock, store):
    code, _ = _recovery_code(svc, mailer, clock)
    assert len(code) == 20
    assert store._d.execute("SELECT code_hash FROM recovery_codes").fetchone()[0] != code


def test_a_new_recovery_code_replaces_the_old_one_and_ends_a_recovery_begun_with_it(svc, mailer, clock):
    code, cookie = _recovery_code(svc, mailer, clock)
    challenge = _start(svc, code)
    mail = mailer.last_code(NEW)
    again = svc.make_recovery_code(svc.session(cookie)).recovery_code
    assert again != code
    assert svc.recover_start(code, NEW, OTHER_NET).status == "wrong"
    assert svc.recover_finish(challenge, mail, OTHER_NET).status == "wrong"
    assert svc.recover_start(again, NEW, OTHER_NET).status == "sent"


def test_recovery_waits_a_week_and_then_the_new_address_owns_the_account(svc, mailer, clock, store):
    code, cookie = _recovery_code(svc, mailer, clock)
    account_id = svc.session(cookie).account_id
    challenge = _start(svc, code)
    assert store._d.execute("SELECT COUNT(*) FROM pending_changes").fetchone()[0] == 0  # nothing waits until it is proved
    finished = svc.recover_finish(challenge, mailer.last_code(NEW), OTHER_NET)
    week_on = (svc.today() + timedelta(days=7)).isoformat()
    assert finished.status == "waiting" and finished.effective_on == week_on
    assert svc.session(cookie).pending_recovery  # the old owner sees the banner
    waiting_challenge = svc.start_sign_in(NEW, OTHER_NET).challenge
    waiting = svc.finish_sign_in(waiting_challenge, NEW, mailer.last_code(NEW), OTHER_NET, 1990)
    assert waiting.status == "recovery_waiting" and waiting.effective_on == week_on
    clock.advance(7 * 86400)
    fresh = svc.start_sign_in(NEW, OTHER_NET).challenge
    result = svc.finish_sign_in(fresh, NEW, mailer.last_code(NEW), OTHER_NET)
    assert result.status == "ok" and not result.new_account
    assert svc.session(result.cookie).account_id == account_id
    assert svc.session(cookie) is None  # every old session ended
    assert result.recovery_code and result.recovery_code != code  # the used code is replaced, shown once
    assert svc.recover_start(code, "late@example.org", OTHER_NET).status == "wrong"


def test_a_recovery_code_is_spent_when_the_new_address_is_proved(svc, mailer, clock):
    code, _ = _recovery_code(svc, mailer, clock)
    first = _start(svc, code)
    second = _start(svc, code)  # not yet spent; a second start is allowed
    assert svc.recover_finish(first, mailer.sent[-2][1], OTHER_NET).status == "waiting"
    assert svc.recover_start(code, "x@example.org", OTHER_NET).status == "wrong"
    assert svc.recover_finish(second, mailer.last_code(NEW), OTHER_NET).status == "wrong"


def test_a_failed_send_does_not_spend_the_recovery_code(svc, mailer, clock, store):
    code, _ = _recovery_code(svc, mailer, clock)
    mailer.fail = True
    assert svc.recover_start(code, NEW, OTHER_NET).status == "send_failed"
    mailer.fail = False
    assert store.account_by_recovery_hash(hashlib.sha256(code.encode()).hexdigest()) is not None
    assert svc.recover_start(code, NEW, OTHER_NET).status == "sent"


def test_a_recovery_never_proved_leaves_nothing_behind(svc, mailer, clock, store):
    code, cookie = _recovery_code(svc, mailer, clock)
    _start(svc, code)
    assert not svc.session(cookie).pending_recovery
    clock.advance(2 * 86400)
    svc.purge()
    assert store._e.execute("SELECT COUNT(*) FROM challenges").fetchone()[0] == 0


def test_the_old_owner_can_cancel_a_recovery_a_thief_started(svc, mailer, clock):
    code, cookie = _recovery_code(svc, mailer, clock)
    challenge = _start(svc, code, "thief@example.org")
    svc.recover_finish(challenge, mailer.last_code("thief@example.org"), OTHER_NET)
    assert svc.session(cookie).pending_recovery
    started = svc.step_up_start(svc.session(cookie), ADDR, NET)
    svc.step_up_finish(svc.session(cookie), started.challenge, mailer.last_code(ADDR), NET)
    assert svc.cancel_recovery(svc.session(cookie)).status == "ok"
    assert not svc.session(cookie).pending_recovery
    clock.advance(8 * 86400)
    fresh = svc.start_sign_in("thief@example.org", OTHER_NET).challenge
    result = svc.finish_sign_in(fresh, "thief@example.org", mailer.last_code("thief@example.org"), OTHER_NET, 1990)
    assert result.new_account  # the thief meets an ordinary new account, not the old owner's
    assert svc.session(result.cookie).account_id != svc.session(cookie).account_id


def test_recovery_refuses_a_bad_code_and_bad_input(svc, mailer, clock):
    code, _ = _recovery_code(svc, mailer, clock)
    assert svc.recover_start("AAAAAAAAAAAAAAAAAAAA", NEW, OTHER_NET).status == "wrong"
    assert svc.recover_start(None, NEW, OTHER_NET).status == "wrong"
    assert svc.recover_start(code, "not an address", OTHER_NET).status == "wrong"


def test_the_replies_never_say_whether_an_address_has_an_account(svc, mailer, clock):
    sign_in(svc, mailer, "bob@example.org", "192.0.2.9")
    code, _ = _recovery_code(svc, mailer, clock)
    mails_to_bob = len([1 for to, _ in mailer.sent if to == "bob@example.org"])
    taken = svc.recover_start(code, "bob@example.org", OTHER_NET)
    free = svc.recover_start(code, NEW, OTHER_NET)
    assert taken.status == free.status == "sent" and taken.challenge and free.challenge
    assert len([1 for to, _ in mailer.sent if to == "bob@example.org"]) == mails_to_bob  # nothing is sent to bob
    assert len([1 for to, _ in mailer.sent if to == NEW]) == 1
    assert svc.recover_finish(taken.challenge, "123456", OTHER_NET).status == "wrong"  # and it can never be proved
    clock.advance(901)
    session, _ = stepped_up_session(svc, mailer, clock, ADDR, "198.51.100.40")
    a = svc.change_address_start(session, "bob@example.org", NET)
    b = svc.change_address_start(session, "carol@example.org", NET)
    assert a.status == b.status == "sent" and a.challenge and b.challenge
    assert len([1 for to, _ in mailer.sent if to == "bob@example.org"]) == mails_to_bob
    assert len([1 for to, _ in mailer.sent if to == "carol@example.org"]) == 1


def test_a_stranger_cannot_block_replace_or_borrow_a_recovery_to_the_same_address(svc, mailer, clock):
    code, cookie = _recovery_code(svc, mailer, clock)
    victim_id = svc.session(cookie).account_id
    sign_in(svc, mailer, "mallory@example.org", "192.0.2.50")
    _, mcookie = stepped_up_session(svc, mailer, clock, "mallory@example.org", "192.0.2.50")
    mallory_code = svc.make_recovery_code(svc.session(mcookie)).recovery_code
    victims = _start(svc, code)
    victims_mail = mailer.last_code(NEW)
    strangers = _start(svc, mallory_code, NEW, "192.0.2.51")  # started after the victim, to the same address
    strangers_mail = mailer.sent[-1][1]
    assert strangers_mail != victims_mail and strangers != victims
    assert svc.recover_finish(victims, strangers_mail, OTHER_NET).status == "wrong"  # the other mail proves nothing for the victim
    assert svc.recover_finish(victims, victims_mail, OTHER_NET).status == "waiting"
    clock.advance(7 * 86400)
    fresh = svc.start_sign_in(NEW, OTHER_NET).challenge
    result = svc.finish_sign_in(fresh, NEW, mailer.last_code(NEW), OTHER_NET)
    assert result.status == "ok" and svc.session(result.cookie).account_id == victim_id
    assert svc.recover_finish(strangers, victims_mail, "192.0.2.52").status == "wrong"


def test_many_accounts_cannot_send_more_than_a_few_codes_to_one_inbox(svc, mailer, clock):
    victim = "victim@example.org"
    for i in range(10):
        network = f"198.51.100.{i + 1}"
        session, _ = stepped_up_session(svc, mailer, clock, f"attacker{i}@example.org", network)
        svc.change_address_start(session, victim, network)
    assert len([1 for to, _ in mailer.sent if to == victim]) == svc.limits.sends_per_address_open_15min


def test_an_address_taken_during_the_wait_moves_nothing_and_replaces_no_recovery_code(svc, mailer, clock, store):
    from engine.accounts.store import Account

    code, cookie = _recovery_code(svc, mailer, clock)
    account_id = svc.session(cookie).account_id
    svc.recover_finish(_start(svc, code), mailer.last_code(NEW), OTHER_NET)
    other_account_id = "f" * 32
    store.create_account(Account(other_account_id, svc.keys.address_hash(NEW), "x", 1, "x", "18+"))
    owner_code = svc._issue_recovery_code(other_account_id)
    clock.advance(7 * 86400)
    fresh = svc.start_sign_in(NEW, OTHER_NET).challenge
    result = svc.finish_sign_in(fresh, NEW, mailer.last_code(NEW), OTHER_NET)
    assert result.status == "ok" and result.recovery_code is None
    assert svc.session(result.cookie).account_id == other_account_id
    assert store.account_by_recovery_hash(hashlib.sha256(owner_code.encode()).hexdigest()) == other_account_id
    assert store.account(account_id) is not None and store.pending_for_account(account_id) is None


def test_recovery_attempts_are_limited_per_network(svc, mailer, clock):
    results = [svc.recover_start("AAAAAAAAAAAAAAAAAAAA", NEW, OTHER_NET).status for _ in range(7)]
    assert results[:5] == ["wrong"] * 5 and results[5:] == ["throttled"] * 2


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
    assert svc.finish_sign_in(old, ADDR, mailer.last_code(ADDR), NET).status == "needs_birth_year"  # no account at the old address
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


def test_a_code_for_one_account_s_change_cannot_finish_another(svc, mailer, clock):
    session, cookie = stepped_up_session(svc, mailer, clock)
    other, other_cookie = stepped_up_session(svc, mailer, clock, "bob@example.org", "192.0.2.9")
    started = svc.change_address_start(session, NEW, NET)
    code = mailer.last_code(NEW)
    assert svc.change_address_finish(other, started.challenge, code, NET).status == "wrong"
