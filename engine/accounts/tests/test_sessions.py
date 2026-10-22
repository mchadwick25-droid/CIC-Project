import pytest

from engine.accounts.tests.conftest import sign_in, stepped_up_session

ADDR = "ada@example.org"
NET = "203.0.113.5"


def test_the_cookie_points_to_a_session_and_holds_no_account_value(svc, mailer, store):
    cookie = sign_in(svc, mailer)
    session = svc.session(cookie)
    token, _, tag = cookie.rpartition(".")
    account = store.account(session.account_id)
    for held in (account.account_id, account.address_hash, ADDR, "example.org"):
        assert held not in cookie
    assert len(token) >= 40 and len(tag) == 22


def test_a_forged_or_missing_cookie_is_no_session(svc, mailer):
    cookie = sign_in(svc, mailer)
    assert svc.session(None) is None and svc.session("") is None and svc.session("a.b") is None
    assert svc.session(cookie[:-1] + ("a" if cookie[-1] != "a" else "b")) is None


def test_a_session_slides_while_used_and_ends_when_idle(svc, mailer, clock):
    cookie = sign_in(svc, mailer)
    for _ in range(5):
        clock.advance(10 * 86400)
        assert svc.session(cookie) is not None
    clock.advance(15 * 86400)
    assert svc.session(cookie) is None


def test_a_session_ends_at_the_absolute_limit_however_active(svc, mailer, clock):
    cookie = sign_in(svc, mailer)
    for _ in range(5):
        clock.advance(10 * 86400)
        assert svc.session(cookie) is not None
    clock.advance(10 * 86400)
    assert svc.session(cookie) is None


def test_sign_out_ends_one_session_and_everywhere_ends_all(svc, mailer, store):
    first = sign_in(svc, mailer)
    challenge = svc.start_sign_in(ADDR, "203.0.113.6").challenge
    second = svc.finish_sign_in(challenge, ADDR, mailer.last_code(ADDR), "203.0.113.6").cookie
    svc.sign_out(svc.session(first))
    assert svc.session(first) is None and svc.session(second) is not None
    svc.sign_out_everywhere(svc.session(second))
    assert svc.session(second) is None


def test_expired_sessions_and_codes_are_purged(svc, mailer, store, clock):
    sign_in(svc, mailer)
    svc.start_sign_in("other@example.org", NET)
    clock.advance(70 * 86400)
    assert svc.purge() > 0
    assert store._e.execute("SELECT COUNT(*) FROM sessions").fetchone()[0] == 0
    assert store._e.execute("SELECT COUNT(*) FROM challenges").fetchone()[0] == 0
    assert store._e.execute("SELECT COUNT(*) FROM counters").fetchone()[0] == 0


def test_step_up_needs_the_account_s_own_address_and_replies_alike_for_any_address(svc, mailer, clock):
    cookie = sign_in(svc, mailer)
    session = svc.session(cookie)
    sent_before = len(mailer.sent)
    stranger = svc.step_up_start(session, "someone.else@example.org", NET)
    assert stranger.status == "sent" and stranger.challenge
    assert len(mailer.sent) == sent_before  # the same reply, and nothing is sent
    assert svc.step_up_finish(session, stranger.challenge, "000000", NET).status == "wrong"
    own = svc.step_up_start(session, ADDR, NET)
    assert own.status == "sent" and len(mailer.sent) == sent_before + 1
    assert svc.step_up_finish(svc.session(cookie), own.challenge, "000000", NET).status == "wrong"
    assert not svc.session(cookie).stepped_up
    assert svc.step_up_finish(svc.session(cookie), own.challenge, mailer.last_code(ADDR), NET).status == "ok"
    assert svc.session(cookie).stepped_up


def test_a_step_up_challenge_cannot_be_used_by_another_account(svc, mailer, clock):
    cookie = sign_in(svc, mailer)
    other = sign_in(svc, mailer, "bob@example.org", "192.0.2.9")
    started = svc.step_up_start(svc.session(cookie), ADDR, NET)
    code = mailer.last_code(ADDR)
    assert svc.step_up_finish(svc.session(other), started.challenge, code, NET).status == "wrong"


def test_step_up_lapses_after_ten_minutes(svc, mailer, clock):
    session, cookie = stepped_up_session(svc, mailer, clock)
    clock.advance(601)
    assert not svc.session(cookie).stepped_up


@pytest.mark.parametrize("action", ["recovery", "cancel", "export", "delete", "change"])
def test_sensitive_actions_need_a_fresh_step_up(svc, mailer, action):
    session = svc.session(sign_in(svc, mailer))
    result = {
        "recovery": lambda: svc.make_recovery_code(session),
        "cancel": lambda: svc.cancel_recovery(session),
        "export": lambda: svc.export(session),
        "delete": lambda: svc.delete_account(session),
        "change": lambda: svc.change_address_start(session, "new@example.org", NET),
    }[action]()
    assert result.status == "step_up_needed"
