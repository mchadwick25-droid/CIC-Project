"""Deleting an account closes it for 90 days. Everything stays, the owner can re-open it by signing in,
and on the last day it is erased for good. A restored file never re-opens a closed account."""
from datetime import timedelta

import pytest

from engine.accounts.service import AccountsService, ledger_hash
from engine.accounts.tests.conftest import (
    FakeVerifier, provider_sign_in, provider_token, sign_in, start_sign_in, stepped_up_session,
)

ADDR = "ada@example.org"
NET = "203.0.113.5"
DAY = 86400


class Outside:
    """Stands in for the bucket's closure marks."""

    def __init__(self):
        self.marks: dict[str, str] = {}
        self.refuse = False

    def publish(self, hash_, erase_on):
        if self.refuse:
            raise RuntimeError("down")
        self.marks[hash_] = erase_on
        return True

    def remove(self, hash_, erase_on):
        if self.refuse:
            raise RuntimeError("down")
        self.marks.pop(hash_, None)
        return True

    def source(self):
        return list(self.marks.items())


@pytest.fixture
def outside():
    return Outside()


@pytest.fixture
def marked(store, keys, mailer, clock, contacts, outside):
    return AccountsService(
        store, keys, mailer, clock=clock, verifier=FakeVerifier(), contacts=contacts,
        closure_publisher=outside.publish, closure_remover=outside.remove, closure_source=outside.source,
    )


def _close(svc, mailer, clock):
    session, cookie = stepped_up_session(svc, mailer, clock)
    result = svc.close_account(session)
    assert result.status == "ok"
    return session.account_id, cookie, result


def _sign_in_to_closed(svc, mailer, reopen=None, address=ADDR):
    challenge, code = start_sign_in(svc, mailer, address)
    return svc.finish_sign_in(challenge, address, code, NET, True, reopen), challenge, code


def test_closing_needs_a_fresh_step_up(svc, mailer):
    session = svc.session(sign_in(svc, mailer))
    assert svc.close_account(session).status == "step_up_needed"
    assert svc.store.closure(session.account_id) is None


def test_closing_keeps_the_account_and_signs_it_out_for_ninety_days(svc, mailer, clock, store):
    account_id, cookie, result = _close(svc, mailer, clock)
    assert result.data["erase_on"] == (svc.today() + timedelta(days=90)).isoformat()
    assert store.account(account_id) is not None
    assert store.closure(account_id) == (svc.today().isoformat(), result.data["erase_on"])
    assert svc.session(cookie) is None
    assert store._e.execute("SELECT COUNT(*) FROM sessions").fetchone()[0] == 0


def test_a_session_that_somehow_survives_a_closing_is_refused(svc, mailer, clock, store):
    session, cookie = stepped_up_session(svc, mailer, clock)
    assert store.close_account(session.account_id, svc.today().isoformat(), (svc.today() + timedelta(days=500)).isoformat())
    assert svc.session(cookie) is None


def test_signing_in_to_a_closed_account_offers_to_re_open_it_and_does_not_spend_the_code(svc, mailer, clock):
    account_id, _, closed = _close(svc, mailer, clock)
    result, challenge, code = _sign_in_to_closed(svc, mailer)
    assert result.status == "account_closed" and result.data == {"erase_on": closed.data["erase_on"]}
    assert result.cookie is None
    again = svc.finish_sign_in(challenge, ADDR, code, NET, True, True)
    assert again.status == "ok" and svc.session(again.cookie).account_id == account_id
    assert svc.store.closure(account_id) is None


def test_a_closed_address_cannot_open_a_second_account(svc, mailer, clock, store):
    _close(svc, mailer, clock)
    challenge, code = start_sign_in(svc, mailer)
    assert svc.finish_sign_in(challenge, ADDR, code, NET).status == "account_closed"
    assert store._d.execute("SELECT COUNT(*) FROM accounts").fetchone()[0] == 1


def test_a_wrong_code_learns_nothing_about_a_closed_account(svc, mailer, clock):
    _close(svc, mailer, clock)
    challenge, _ = start_sign_in(svc, mailer)
    closed = svc.finish_sign_in(challenge, ADDR, "00000000", NET, True, True)
    other, _ = start_sign_in(svc, mailer, "nobody@example.org", "198.51.100.7")
    stranger = svc.finish_sign_in(other, "nobody@example.org", "00000000", "198.51.100.7", True, True)
    assert (closed.status, closed.data, closed.cookie) == (stranger.status, stranger.data, stranger.cookie) == ("wrong", {}, None)


def test_on_the_last_day_a_person_can_still_re_open_and_the_day_after_cannot(svc, mailer, clock, store):
    account_id, _, closed = _close(svc, mailer, clock)
    clock.advance(90 * DAY)
    _, challenge, code = _sign_in_to_closed(svc, mailer)
    assert svc.finish_sign_in(challenge, ADDR, code, NET, True, True).status == "ok"
    svc.close_account(svc.session(sign_in(svc, mailer, ADDR, "198.51.100.8")) and stepped_up_session(svc, mailer, clock, ADDR, "198.51.100.8")[0])
    clock.advance(91 * DAY)
    result, _, _ = _sign_in_to_closed(svc, mailer)
    assert result.status == "wrong" and result.cookie is None
    assert svc.erase_closed() == 1 and store.account(account_id) is None


def test_an_erasure_that_meets_a_re_opened_account_leaves_it_whole(svc, mailer, clock, store, contacts):
    account_id, _, _ = _close(svc, mailer, clock)
    clock.advance(40 * DAY)
    _, challenge, code = _sign_in_to_closed(svc, mailer)
    assert svc.finish_sign_in(challenge, ADDR, code, NET, True, True).status == "ok"
    clock.advance(60 * DAY)
    assert svc.purge_account(account_id, closed_due=True).status == "wrong"
    assert store.account(account_id) is not None and contacts.get(account_id) == ADDR


def test_a_mark_written_while_the_account_is_re_opened_is_taken_back_out(marked, mailer, clock, store, outside):
    session, _ = stepped_up_session(marked, mailer, clock)
    marked.close_account(session)
    outside.marks.clear()
    store._d.execute("UPDATE closures SET published = 0")
    real = outside.publish

    def reopened_during_the_write(hash_, erase_on):
        real(hash_, erase_on)
        store.reopen_account(session.account_id, marked.today().isoformat())
        return True

    marked.closure_publisher = reopened_during_the_write
    marked.publish_closures()
    assert outside.marks == {} and store.closure(session.account_id) is None
    assert marked.sync_closures() == 0


def test_a_person_who_signs_in_during_the_two_year_sweep_is_not_closed(svc, mailer, clock, store, monkeypatch):
    sign_in(svc, mailer)
    account_id = store.account_ids()[0]
    clock.advance(365 * 2 * DAY + 20 * DAY)
    listed = svc.stale_account_ids()
    assert listed == [account_id]
    monkeypatch.setattr(svc, "stale_account_ids", lambda: listed)
    sign_in(svc, mailer, ADDR, "198.51.100.9")  # signs in after the list was made
    assert svc.close_stale_accounts() == 0 and store.closure(account_id) is None


def test_deleting_ends_a_recovery_that_is_waiting(svc, mailer, clock, store, contacts):
    from engine.accounts.tests.test_recovery import NEW, _owner_with_code, _prove

    session, cookie, code = _owner_with_code(svc, mailer, clock)
    assert _prove(svc, mailer, code, NEW).status == "ok"
    assert store.pending_of(session.account_id, include_unnotified=True) is not None
    stepped = svc.session(cookie)
    svc.store.step_up_session(stepped.token_hash, svc.now() + 600)
    assert svc.close_account(svc.session(cookie)).status == "ok"
    assert store.pending_of(session.account_id, include_unnotified=True) is None


def test_a_second_delete_at_once_answers_ok_with_the_same_last_day(svc, mailer, clock):
    session, _ = stepped_up_session(svc, mailer, clock)
    first = svc.close_account(session)
    second = svc.close_account(session)
    assert first.status == second.status == "ok" and first.data == second.data


def test_re_opening_keeps_everything_the_account_held(svc, mailer, clock, store):
    session, cookie = stepped_up_session(svc, mailer, clock)
    store.shelf_add(session.account_id, "conv-1", "sealed", svc.today().isoformat(), 500)
    svc.close_account(session)
    clock.advance(60 * DAY)
    result, challenge, code = _sign_in_to_closed(svc, mailer)
    opened = svc.finish_sign_in(challenge, ADDR, code, NET, True, True)
    assert opened.status == "ok"
    assert svc.shelf_ids(session.account_id) == ["conv-1"]
    clock.advance(40 * DAY)
    assert svc.erase_closed() == 0
    assert svc.store.account(session.account_id) is not None


def test_the_account_is_erased_on_its_day_and_not_before(svc, mailer, clock, store):
    account_id, _, _ = _close(svc, mailer, clock)
    clock.advance(89 * DAY)
    assert svc.erase_closed() == 0 and store.account(account_id) is not None
    clock.advance(DAY)
    assert svc.erase_closed() == 0, "the last day still belongs to the person"
    clock.advance(DAY)
    assert svc.erase_closed() == 1
    assert store.account(account_id) is None and store.closure(account_id) is None
    assert store._d.execute("SELECT COUNT(*) FROM deletion_ledger").fetchone()[0] == 1


def test_an_erased_address_starts_fresh(svc, mailer, clock):
    _close(svc, mailer, clock)
    clock.advance(91 * DAY)
    svc.erase_closed()
    challenge, code = start_sign_in(svc, mailer)
    assert svc.finish_sign_in(challenge, ADDR, code, NET).status == "needs_age_answer"


def test_erasing_clears_the_shelf_first_and_a_failure_leaves_the_account_closed(svc, mailer, clock, store):
    session, _ = stepped_up_session(svc, mailer, clock)
    store.shelf_add(session.account_id, "conv-1", "sealed", svc.today().isoformat(), 500)
    svc.close_account(session)
    clock.advance(91 * DAY)
    seen = []

    def broken(items):
        raise RuntimeError("store unavailable")

    assert svc.erase_closed(broken) == 0
    assert store.account(session.account_id) is not None and store.closure(session.account_id) is not None
    assert svc.erase_closed(lambda items: seen.extend(i for i, _ in items)) == 1
    assert seen == ["conv-1"] and store.account(session.account_id) is None


def test_an_account_unused_for_two_years_is_closed_not_erased(svc, mailer, clock, store):
    sign_in(svc, mailer)
    account_id = store.account_ids()[0]
    clock.advance(365 * 2 * DAY + 20 * DAY)
    assert svc.close_stale_accounts() == 1
    assert store.account(account_id) is not None
    assert store.closure(account_id)[1] == (svc.today() + timedelta(days=90)).isoformat()
    assert svc.close_stale_accounts() == 0, "closing again does not move the day"
    assert svc.stale_account_ids() == []


def test_a_stale_account_that_signs_in_during_its_ninety_days_stays(svc, mailer, clock, store):
    sign_in(svc, mailer)
    account_id = store.account_ids()[0]
    clock.advance(365 * 2 * DAY + 20 * DAY)
    svc.close_stale_accounts()
    clock.advance(30 * DAY)
    _, challenge, code = _sign_in_to_closed(svc, mailer)
    assert svc.finish_sign_in(challenge, ADDR, code, NET, True, True).status == "ok"
    clock.advance(70 * DAY)
    assert svc.erase_closed() == 0 and store.account(account_id) is not None
    assert svc.stale_account_ids() == []


def test_a_closed_account_is_not_closed_again_with_a_new_day(svc, mailer, clock, store):
    account_id, _, first = _close(svc, mailer, clock)
    clock.advance(10 * DAY)
    assert store.close_account(account_id, svc.today().isoformat(), (svc.today() + timedelta(days=500)).isoformat()) is False
    assert store.closure(account_id)[1] == first.data["erase_on"]


def test_a_provider_sign_in_to_a_closed_account_offers_to_re_open_and_keeps_the_nonce(svc, mailer, clock, store):
    provider_sign_in(svc)
    account_id = store.account_ids()[0]
    store.close_account(account_id, svc.today().isoformat(), (svc.today() + timedelta(days=90)).isoformat())
    token, nonce = provider_token(svc, "g-ada", "198.51.100.9")
    closed = svc.provider_sign_in("google", token, nonce, "198.51.100.9")
    assert closed.status == "account_closed" and closed.cookie is None
    opened = svc.provider_sign_in("google", token, nonce, "198.51.100.9", None, True)
    assert opened.status == "ok" and svc.session(opened.cookie).account_id == account_id
    assert store.closure(account_id) is None


def test_a_closure_is_written_outside_the_disk_and_a_down_bucket_is_retried(marked, mailer, clock, store, outside):
    outside.refuse = True
    session, _ = stepped_up_session(marked, mailer, clock)
    assert marked.close_account(session).status == "ok"
    assert outside.marks == {} and len(store.unpublished_closures()) == 1
    outside.refuse = False
    assert marked.publish_closures() == 1
    assert outside.marks == {ledger_hash(session.account_id): store.closure(session.account_id)[1]}
    assert store.unpublished_closures() == []


def test_the_outside_mark_holds_only_a_hash_and_a_day(marked, mailer, clock, outside):
    session, _ = stepped_up_session(marked, mailer, clock)
    marked.close_account(session)
    (hash_, day), = outside.marks.items()
    assert hash_ == ledger_hash(session.account_id) and day.count("-") == 2
    assert ADDR.split("@")[0] not in hash_ + day


def test_a_file_restored_from_before_the_closing_is_closed_again_by_the_outside_mark(marked, mailer, clock, store, outside):
    session, _ = stepped_up_session(marked, mailer, clock)
    marked.close_account(session)
    erase_on = store.closure(session.account_id)[1]
    store._d.execute("DELETE FROM closures")  # what a restore of last night's file does
    assert marked.sync_closures() == 1
    assert store.closure(session.account_id) == ((marked.today()).isoformat(), erase_on)
    assert store.unpublished_closures() == []
    assert marked.sync_closures() == 0


def test_re_opening_takes_the_outside_mark_away_so_a_restore_leaves_it_open(marked, mailer, clock, store, outside):
    session, _ = stepped_up_session(marked, mailer, clock)
    marked.close_account(session)
    _, challenge, code = _sign_in_to_closed(marked, mailer)
    assert marked.finish_sign_in(challenge, ADDR, code, NET, True, True).status == "ok"
    assert outside.marks == {}
    assert marked.sync_closures() == 0 and store.closure(session.account_id) is None


def test_a_re_open_the_bucket_refuses_leaves_the_account_closed_and_asks_for_a_new_code(marked, mailer, clock, store, outside):
    session, _ = stepped_up_session(marked, mailer, clock)
    marked.close_account(session)
    outside.refuse = True
    _, challenge, code = _sign_in_to_closed(marked, mailer)
    assert marked.finish_sign_in(challenge, ADDR, code, NET, True, True).status == "reopen_failed"
    assert store.closure(session.account_id) is not None
    outside.refuse = False
    _, challenge, code = _sign_in_to_closed(marked, mailer)
    assert marked.finish_sign_in(challenge, ADDR, code, NET, True, True).status == "ok"
    assert store.closure(session.account_id) is None


def test_an_unreachable_bucket_still_applies_the_files_own_closures(marked, mailer, clock, store):
    session, _ = stepped_up_session(marked, mailer, clock)
    marked.close_account(session)
    marked.closure_source = lambda: (_ for _ in ()).throw(RuntimeError("down"))
    assert marked.sync_closures() == 0
    assert store.closure(session.account_id) is not None
    clock.advance(91 * DAY)
    assert marked.erase_closed() == 1


def test_a_restore_of_an_erased_account_is_removed_by_the_deletion_ledger_and_not_re_closed(marked, mailer, clock, store, outside):
    session, _ = stepped_up_session(marked, mailer, clock)
    account = store.account(session.account_id)
    marked.close_account(session)
    clock.advance(91 * DAY)
    marked.erase_closed()
    store.create_account(account)  # a restore
    assert marked.reapply_ledger() == 1
    assert store.account(account.account_id) is None and store.closure(account.account_id) is None


def test_deleting_the_account_removes_its_closure_row_with_it(svc, mailer, clock, store):
    account_id, _, _ = _close(svc, mailer, clock)
    clock.advance(91 * DAY)
    svc.erase_closed()
    assert store._d.execute("SELECT COUNT(*) FROM closures").fetchone()[0] == 0
