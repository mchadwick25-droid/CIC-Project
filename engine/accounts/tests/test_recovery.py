import logging
from datetime import timedelta

from engine.accounts.tests.conftest import provider_sign_in, provider_token, sign_in, stepped_up_session

ADDR = "ada@example.org"
NEW = "ada.new@example.org"
NET = "203.0.113.5"
THIEF = "198.51.100.77"


def _owner_with_code(svc, mailer, clock):
    session, cookie = stepped_up_session(svc, mailer, clock)
    code = svc.recovery_code_make(session).data["recovery_code"]
    return session, cookie, code


def _prove(svc, mailer, code, address=NEW, network=THIEF):
    started = svc.recovery_start(code, address, network)
    assert started.status == "sent"
    return svc.recovery_prove(started.challenge, mailer.last_code(address), address, network)


def test_making_a_recovery_code_needs_a_step_up_and_is_kept_only_as_a_hash(svc, mailer, clock, tmp_path):
    session = svc.session(sign_in(svc, mailer, ADDR))
    assert svc.recovery_code_make(session).status == "step_up_needed"
    session, cookie, code = _owner_with_code(svc, mailer, clock)
    assert len(code) >= 22  # 128 bits
    for name in ("d.db", "e.db"):
        assert code.encode() not in (tmp_path / name).read_bytes()
    assert svc.me(svc.session(cookie))["has_recovery_code"] is True


def test_a_new_recovery_code_replaces_the_old(svc, mailer, clock):
    session, cookie, first = _owner_with_code(svc, mailer, clock)
    second = svc.recovery_code_make(svc.session(cookie)).data["recovery_code"]
    assert svc.recovery_start(first, NEW, THIEF).status == "sent" and not [a for a, _ in mailer.sent if a == NEW]
    assert svc.recovery_start(second, NEW, THIEF).status == "sent" and [a for a, _ in mailer.sent if a == NEW]


def test_a_recovery_waits_seven_days_tells_the_old_address_and_shows_a_banner(svc, mailer, clock, contacts):
    session, cookie, code = _owner_with_code(svc, mailer, clock)
    done = _prove(svc, mailer, code)
    assert done.status == "ok" and done.data["effective_on"] == (svc.today() + timedelta(days=8)).isoformat()
    address, kind, fields = mailer.notices[-1]
    assert (address, kind) == (ADDR, "recovery_started") and fields["effective_on"] == done.data["effective_on"] and fields["cancel_code"]
    me = svc.me(svc.session(cookie))
    assert me["recovery_pending"] == {"effective_on": done.data["effective_on"]}
    assert contacts.get(session.account_id) == ADDR  # nothing has moved yet
    assert svc.start_sign_in(ADDR, NET).status == "sent"


def test_after_seven_days_the_new_address_signs_in_to_the_same_account_and_old_sessions_end(svc, mailer, clock, contacts, store):
    session, cookie, code = _owner_with_code(svc, mailer, clock)
    _prove(svc, mailer, code)
    clock.advance(8 * 86400 - 1)
    assert svc.session(cookie) is not None
    clock.advance(86400 + 1)
    challenge = svc.start_sign_in(NEW, NET).challenge
    result = svc.finish_sign_in(challenge, NEW, mailer.last_code(NEW), NET)
    assert result.status == "ok" and not result.new_account
    assert svc.session(result.cookie).account_id == session.account_id
    assert svc.session(cookie) is None
    assert contacts.get(session.account_id) == NEW
    assert store._d.execute("SELECT COUNT(*) FROM accounts").fetchone()[0] == 1


def test_the_purge_carries_out_a_recovery_whose_days_are_up(svc, mailer, clock, contacts, store):
    session, cookie, code = _owner_with_code(svc, mailer, clock)
    _prove(svc, mailer, code)
    clock.advance(8 * 86400)
    svc.purge()
    assert store.account(session.account_id).address_hash == svc.keys.address_hash(NEW)
    assert contacts.get(session.account_id) == NEW and store.pending_of(session.account_id) is None


def test_the_start_reply_is_the_same_for_a_right_and_a_wrong_recovery_code(svc, mailer, clock):
    session, cookie, code = _owner_with_code(svc, mailer, clock)
    sent = len(mailer.sent)
    wrong = svc.recovery_start("not-a-code", "x@example.org", THIEF)
    right = svc.recovery_start(code, NEW, THIEF)
    assert wrong.status == right.status == "sent" and len(wrong.challenge) == len(right.challenge)
    assert len(mailer.sent) == sent + 1 and mailer.sent[-1][0] == NEW


def test_a_recovery_to_an_address_that_has_an_account_sends_nothing(svc, mailer, clock):
    session, cookie, code = _owner_with_code(svc, mailer, clock)
    sign_in(svc, mailer, "bob@example.org", "192.0.2.9")
    sent = len(mailer.sent)
    assert svc.recovery_start(code, "bob@example.org", THIEF).status == "sent" and len(mailer.sent) == sent


def test_the_recovery_code_works_once(svc, mailer, clock):
    session, cookie, code = _owner_with_code(svc, mailer, clock)
    assert _prove(svc, mailer, code).status == "ok"
    sent = len(mailer.sent)
    assert svc.recovery_start(code, "third@example.org", THIEF).status == "sent" and len(mailer.sent) == sent


def test_a_second_recovery_cannot_start_while_one_waits(svc, mailer, clock):
    session, cookie, code = _owner_with_code(svc, mailer, clock)
    new_code = _prove(svc, mailer, code).data["recovery_code"]
    sent = len(mailer.sent)
    assert svc.recovery_start(new_code, "third@example.org", THIEF).status == "sent" and len(mailer.sent) == sent


def test_the_owner_cancels_with_the_code_in_the_notice_and_the_thief_s_new_recovery_code_dies(svc, mailer, clock, contacts, store):
    session, cookie, code = _owner_with_code(svc, mailer, clock)
    thief_code = _prove(svc, mailer, code).data["recovery_code"]
    cancel = mailer.notices[-1][2]["cancel_code"]
    assert svc.recovery_cancel(ADDR, "wrong-code", NET).status == "wrong"
    assert svc.recovery_cancel("nobody@example.org", cancel, NET).status == "wrong"
    assert svc.recovery_cancel(ADDR, cancel, NET).status == "ok"
    assert store.pending_of(session.account_id) is None and contacts.take_pending(session.account_id) is None
    assert svc.me(svc.session(cookie))["recovery_pending"] is None and svc.me(svc.session(cookie))["has_recovery_code"] is False
    sent = len(mailer.sent)
    assert svc.recovery_start(thief_code, "third@example.org", THIEF).status == "sent" and len(mailer.sent) == sent
    clock.advance(8 * 86400)
    svc.purge()
    assert store.account(session.account_id).address_hash == svc.keys.address_hash(ADDR)


def test_cancelling_sends_no_mail_and_works_with_every_sending_limit_used_up(svc, mailer, clock):
    session, cookie, code = _owner_with_code(svc, mailer, clock)
    _prove(svc, mailer, code)
    cancel = mailer.notices[-1][2]["cancel_code"]
    for _ in range(40):
        svc.start_sign_in(ADDR, THIEF)
        svc.start_sign_in("filler@example.org", f"203.0.{_}.9")
    sent = len(mailer.sent)
    assert svc.recovery_cancel(ADDR, cancel, NET).status == "ok" and len(mailer.sent) == sent


def test_a_signed_in_owner_cancels_a_waiting_recovery(svc, mailer, clock, store):
    session, cookie, code = _owner_with_code(svc, mailer, clock)
    _prove(svc, mailer, code)
    assert svc.recovery_cancel_signed_in(svc.session(cookie)).status == "ok"
    assert store.pending_of(session.account_id) is None
    assert svc.recovery_cancel_signed_in(svc.session(cookie)).status == "wrong"


def test_changing_the_address_while_a_recovery_waits_ends_it(svc, mailer, clock, store):
    session, cookie, code = _owner_with_code(svc, mailer, clock)
    _prove(svc, mailer, code)
    mine = svc.session(cookie)
    svc.store.step_up_session(mine.token_hash, svc.now() + 600)
    started = svc.change_address_start(svc.session(cookie), "mine.new@example.org", NET)
    assert svc.change_address_finish(svc.session(cookie), started.challenge, mailer.last_code("mine.new@example.org"), NET, "mine.new@example.org").status == "ok"
    assert store.pending_of(session.account_id) is None


def test_a_recovery_challenge_is_not_a_sign_in_or_step_up_code(svc, mailer, clock):
    session, cookie, code = _owner_with_code(svc, mailer, clock)
    started = svc.recovery_start(code, NEW, THIEF)
    proved_code = mailer.last_code(NEW)
    assert svc.finish_sign_in(started.challenge, NEW, proved_code, THIEF, True).status == "wrong"
    assert svc.step_up_finish(svc.session(cookie), started.challenge, proved_code, THIEF).status == "wrong"
    assert svc.recovery_prove(started.challenge, proved_code, "other@example.org", THIEF).status == "wrong"
    assert svc.recovery_prove(started.challenge, proved_code, NEW, THIEF).status == "ok"


def test_an_account_with_no_address_on_file_cannot_be_recovered(svc, mailer, clock, store):
    cookie = provider_sign_in(svc, subject="g-ada")
    session = svc.session(cookie)
    token, nonce = provider_token(svc, "g-ada")
    assert svc.provider_step_up(session, "google", token, nonce, NET).status == "ok"
    code = svc.recovery_code_make(svc.session(cookie)).data["recovery_code"]
    sent = len(mailer.sent)
    assert svc.recovery_start(code, NEW, THIEF).status == "sent" and len(mailer.sent) == sent


def test_a_recovery_does_not_start_when_the_notice_to_the_old_address_is_not_accepted(svc, mailer, clock, store, caplog):
    session, cookie, code = _owner_with_code(svc, mailer, clock)
    started = svc.recovery_start(code, NEW, THIEF)
    proved = mailer.last_code(NEW)
    mailer.fail = True
    caplog.set_level(logging.DEBUG)
    assert svc.recovery_prove(started.challenge, proved, NEW, THIEF).status == "send_failed"
    assert ADDR not in caplog.text and NEW not in caplog.text and code not in caplog.text
    assert store.pending_of(session.account_id) is None and svc.me(svc.session(cookie))["recovery_pending"] is None
    mailer.fail = False
    assert store.has_recovery_key(session.account_id)  # the code it spent is back
    assert svc.recovery_prove(started.challenge, proved, NEW, THIEF).status == "ok"  # and the challenge was not used up


def test_deleting_an_account_removes_its_recovery_rows(svc, mailer, clock, store, contacts):
    session, cookie, code = _owner_with_code(svc, mailer, clock)
    _prove(svc, mailer, code)
    stepped = svc.session(cookie)
    svc.store.step_up_session(stepped.token_hash, svc.now() + 600)
    assert svc.delete_account(svc.session(cookie)).status == "ok"
    assert store._d.execute("SELECT (SELECT COUNT(*) FROM recovery_keys), (SELECT COUNT(*) FROM pending_recoveries)").fetchone() == (0, 0)
    assert contacts.get(session.account_id) is None and contacts.take_pending(session.account_id) is None


def test_a_challenge_opened_with_one_recovery_code_cannot_be_proved_after_that_code_is_gone(svc, mailer, clock, store):
    session, cookie, code = _owner_with_code(svc, mailer, clock)
    first = svc.recovery_start(code, NEW, THIEF)
    first_code = mailer.last_code(NEW)
    second = svc.recovery_start(code, "other.new@example.org", THIEF)
    second_code = mailer.last_code("other.new@example.org")
    assert svc.recovery_prove(first.challenge, first_code, NEW, THIEF).status == "ok"
    cancel = mailer.notices[-1][2]["cancel_code"]
    assert svc.recovery_cancel(ADDR, cancel, NET).status == "ok"
    mine = svc.session(cookie)
    svc.store.step_up_session(mine.token_hash, svc.now() + 600)
    fresh = svc.recovery_code_make(svc.session(cookie)).data["recovery_code"]
    assert svc.recovery_prove(second.challenge, second_code, "other.new@example.org", THIEF).status == "wrong"
    assert store.pending_of(session.account_id) is None
    assert store.account_by_recovery_key(svc.keys.secret_candidates("recovery", fresh)) is not None


def test_a_waiting_move_that_was_cancelled_is_not_carried_out(svc, mailer, clock, store):
    session, cookie, code = _owner_with_code(svc, mailer, clock)
    _prove(svc, mailer, code)
    new_hash = store.pending_of(session.account_id)[0]
    due_day = (svc.today() + timedelta(days=9)).isoformat()
    svc.recovery_cancel_signed_in(svc.session(cookie))
    assert store.apply_pending(session.account_id, new_hash, due_day) is False
    assert store.account(session.account_id).address_hash == svc.keys.address_hash(ADDR)


def test_signing_in_at_the_new_address_during_the_wait_opens_no_account_and_says_when(svc, mailer, clock, store):
    session, cookie, code = _owner_with_code(svc, mailer, clock)
    done = _prove(svc, mailer, code)
    challenge = svc.start_sign_in(NEW, NET).challenge
    result = svc.finish_sign_in(challenge, NEW, mailer.last_code(NEW), NET, True)
    assert result.status == "recovery_waiting" and result.data["effective_on"] == done.data["effective_on"]
    assert store._d.execute("SELECT COUNT(*) FROM accounts").fetchone()[0] == 1
    clock.advance(8 * 86400)
    challenge = svc.start_sign_in(NEW, NET).challenge
    again = svc.finish_sign_in(challenge, NEW, mailer.last_code(NEW), NET)
    assert again.status == "ok" and svc.session(again.cookie).account_id == session.account_id


def test_a_recovery_cannot_be_proved_for_an_address_that_gained_an_account_after_it_started(svc, mailer, clock, store):
    session, cookie, code = _owner_with_code(svc, mailer, clock)
    started = svc.recovery_start(code, NEW, THIEF)
    proved = mailer.last_code(NEW)
    sign_in(svc, mailer, NEW, "192.0.2.50")
    assert svc.recovery_prove(started.challenge, proved, NEW, THIEF).status == "wrong"
    assert store.pending_of(session.account_id) is None and store.has_recovery_key(session.account_id)


def test_recovery_and_cancel_codes_survive_a_rotation_of_the_address_key(tmp_path, mailer, clock):
    from datetime import date
    from engine.accounts.keys import KeyRing, PreviousKey
    from engine.accounts.service import AccountsService
    from engine.accounts.store import AccountStore
    from engine.accounts.contacts import ContactStore
    from engine.accounts.tests.conftest import ADDRESS_KEY, SESSION_KEY, FakeCipher
    store = AccountStore(str(tmp_path / "d.db"), str(tmp_path / "e.db"))
    contacts = ContactStore(str(tmp_path / "c.db"), FakeCipher())
    first = AccountsService(store, KeyRing(ADDRESS_KEY, SESSION_KEY), mailer, clock=clock, contacts=contacts)
    session, cookie, code = _owner_with_code(first, mailer, clock)
    _prove(first, mailer, code)
    cancel = mailer.notices[-1][2]["cancel_code"]
    rotated = KeyRing("b" * 40, SESSION_KEY, key_id="k2", previous=[PreviousKey("k1", ADDRESS_KEY, date(2099, 1, 1))])
    second = AccountsService(store, rotated, mailer, clock=clock, contacts=contacts)
    assert second.recovery_cancel(ADDR, cancel, NET).status == "ok"
    store.close()
    contacts.close()


def test_a_wrong_or_unreadable_kept_address_is_put_right_at_the_next_code_sign_in(svc, mailer, contacts):
    session = svc.session(sign_in(svc, mailer, ADDR))
    contacts.put(session.account_id, "stale@example.org")
    sign_in(svc, mailer, ADDR, "198.51.100.9")
    assert contacts.get(session.account_id) == ADDR
    contacts._c.execute("UPDATE contacts SET blob = 'garbage' WHERE account_id = ?", (session.account_id,))
    sign_in(svc, mailer, ADDR, "198.51.100.10")
    assert contacts.get(session.account_id) == ADDR


def test_a_kept_address_whose_account_is_gone_is_swept(svc, mailer, contacts, store):
    session = svc.session(sign_in(svc, mailer, ADDR))
    store._d.execute("DELETE FROM accounts WHERE account_id = ?", (session.account_id,))
    assert contacts.get(session.account_id) == ADDR
    svc.purge()
    assert contacts.get(session.account_id) is None and contacts.account_ids() == []


def test_the_wait_is_at_least_seven_full_days(svc, mailer, clock, store):
    session, cookie, code = _owner_with_code(svc, mailer, clock)
    _prove(svc, mailer, code)
    clock.advance(7 * 86400)
    svc.purge()
    assert store.pending_of(session.account_id) is not None
    clock.advance(86400)
    svc.purge()
    assert store.pending_of(session.account_id) is None


def test_the_old_address_finds_the_moved_account_gone_once_the_day_has_come(svc, mailer, clock, store):
    session, cookie, code = _owner_with_code(svc, mailer, clock)
    _prove(svc, mailer, code)
    clock.advance(8 * 86400)
    challenge = svc.start_sign_in(ADDR, NET).challenge
    result = svc.finish_sign_in(challenge, ADDR, mailer.last_code(ADDR), NET, True)
    assert result.status == "ok" and result.new_account and svc.session(result.cookie).account_id != session.account_id


def test_making_a_new_recovery_code_ends_a_recovery_waiting(svc, mailer, clock, store):
    session, cookie, code = _owner_with_code(svc, mailer, clock)
    _prove(svc, mailer, code)
    mine = svc.session(cookie)
    svc.store.step_up_session(mine.token_hash, svc.now() + 600)
    svc.recovery_code_make(svc.session(cookie))
    assert store.pending_of(session.account_id) is None and store.has_recovery_key(session.account_id)


def test_a_second_challenge_with_the_same_recovery_code_sends_no_decoy_notice_and_leaves_the_real_one_working(svc, mailer, clock, store, contacts):
    session, cookie, code = _owner_with_code(svc, mailer, clock)
    first = svc.recovery_start(code, NEW, THIEF)
    first_code = mailer.last_code(NEW)
    second = svc.recovery_start(code, "other.new@example.org", THIEF)
    second_code = mailer.last_code("other.new@example.org")
    assert svc.recovery_prove(first.challenge, first_code, NEW, THIEF).status == "ok"
    notices = len(mailer.notices)
    assert svc.recovery_prove(second.challenge, second_code, "other.new@example.org", THIEF).status == "wrong"
    assert len(mailer.notices) == notices
    assert contacts.pending(session.account_id) == NEW
    assert svc.recovery_cancel(ADDR, mailer.notices[-1][2]["cancel_code"], NET).status == "ok"


def _reserve_without_notice(svc, store, contacts, session):
    key = store._d.execute("SELECT key_hash FROM recovery_keys WHERE account_id = ?", (session.account_id,)).fetchone()[0]
    assert store.begin_recovery(session.account_id, key, "k1:new", svc.today().isoformat(), [svc.keys.address_hash(NEW)],
                                svc.keys.address_hash(NEW), "k1:cancel", (svc.today() + timedelta(days=8)).isoformat())
    contacts.put_pending(session.account_id, NEW)  # a crash here, before the notice is accepted
    return key


def test_a_waiting_move_whose_notice_was_never_accepted_is_never_carried_out_and_is_cleared_the_next_day(svc, mailer, clock, store, contacts):
    session, cookie, code = _owner_with_code(svc, mailer, clock)
    key = _reserve_without_notice(svc, store, contacts, session)
    assert svc.me(svc.session(cookie))["recovery_pending"] is None
    challenge = svc.start_sign_in(NEW, NET).challenge
    assert svc.finish_sign_in(challenge, NEW, mailer.last_code(NEW), NET).status == "needs_age_answer"  # no false wait for the address
    clock.advance(9 * 86400)
    svc.purge()
    assert store.account(session.account_id).address_hash == svc.keys.address_hash(ADDR)
    assert store.pending_of(session.account_id, include_unnotified=True) is None and contacts.pending(session.account_id) is None
    assert store.account_by_recovery_key([key]) is not None  # the code it spent is back
    assert svc.recovery_start(code, NEW, THIEF).status == "sent" and mailer.sent[-1][0] == NEW  # and a new recovery can start


def test_an_undone_reservation_restores_nothing_the_owner_has_since_replaced(svc, mailer, clock, store, contacts):
    session, cookie, code = _owner_with_code(svc, mailer, clock)
    key = _reserve_without_notice(svc, store, contacts, session)
    mine = svc.session(cookie)
    svc.store.step_up_session(mine.token_hash, svc.now() + 600)
    fresh = svc.recovery_code_make(svc.session(cookie)).data["recovery_code"]
    assert store.undo_recovery(session.account_id, "k1:cancel", "k1:new", key, "day") is False
    assert store.account_by_recovery_key([key]) is None
    assert store.account_by_recovery_key(svc.keys.secret_candidates("recovery", fresh)) is not None


def test_an_undo_restores_nothing_when_the_replacement_code_is_already_gone(svc, mailer, clock, store, contacts):
    session, cookie, code = _owner_with_code(svc, mailer, clock)
    key = _reserve_without_notice(svc, store, contacts, session)
    store._d.execute("DELETE FROM recovery_keys WHERE account_id = ?", (session.account_id,))
    store.undo_recovery(session.account_id, "k1:cancel", "k1:new", key, "day")
    assert store.account_by_recovery_key([key]) is None


def test_a_recovery_cancelled_while_its_notice_goes_out_is_not_reported_as_waiting(svc, mailer, clock, store, contacts):
    session, cookie, code = _owner_with_code(svc, mailer, clock)
    started = svc.recovery_start(code, NEW, THIEF)
    proved = mailer.last_code(NEW)
    real = mailer.send_notice

    def cancelling(address, kind, fields):
        real(address, kind, fields)
        assert svc.recovery_cancel_signed_in(svc.session(cookie)).status == "ok"

    mailer.send_notice = cancelling
    result = svc.recovery_prove(started.challenge, proved, NEW, THIEF)
    assert result.status == "wrong" and "recovery_code" not in result.data
    assert store.pending_of(session.account_id, include_unnotified=True) is None and contacts.pending(session.account_id) is None
