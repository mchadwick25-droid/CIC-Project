import sqlite3

from engine.accounts.keys import KeyRing, PreviousKey
from engine.accounts.service import AccountsService
from engine.accounts.store import Account, AccountStore
from engine.accounts.tests.conftest import (
    ADDRESS_KEY, SESSION_KEY, FakeVerifier, provider_sign_in, provider_token, sign_in,
)
from datetime import date

NET = "203.0.113.5"
ADDR = "ada@example.org"


def _count(store, table):
    return store._d.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]


def test_a_provider_sign_in_opens_an_account_with_no_address_on_file(svc, store):
    cookie = provider_sign_in(svc)
    session = svc.session(cookie)
    account = store.account(session.account_id)
    assert account.address_hash is None and account.age_band == "18+"
    assert svc.me(session)["sign_in_methods"] == ["google"]


def test_the_same_provider_id_signs_in_to_the_same_account(svc, store):
    first = svc.session(provider_sign_in(svc))
    second = svc.session(provider_sign_in(svc, network="198.51.100.9"))
    assert first.account_id == second.account_id and _count(store, "accounts") == 1


def test_two_providers_with_the_same_subject_are_two_accounts(svc, store):
    a = svc.session(provider_sign_in(svc, "google", "same"))
    b = svc.session(provider_sign_in(svc, "apple", "same", network="198.51.100.9"))
    assert a.account_id != b.account_id


def test_a_new_provider_id_is_asked_the_age_click_first_and_a_no_stores_nothing(svc, store):
    token, nonce = provider_token(svc, "g-new")
    assert svc.provider_sign_in("google", token, nonce, NET).status == "needs_age_answer"
    assert svc.provider_sign_in("google", token, nonce, NET, False).status == "not_adult"
    assert svc.provider_sign_in("google", token, nonce, NET, "yes").status == "not_adult"
    assert _count(store, "accounts") == 0 and _count(store, "linked_sign_ins") == 0
    assert svc.provider_sign_in("google", token, nonce, NET, True).status == "ok"  # the no spent nothing


def test_a_nonce_works_once(svc):
    token, nonce = provider_token(svc, "g-ada")
    assert svc.provider_sign_in("google", token, nonce, NET, True).status == "ok"
    assert svc.provider_sign_in("google", token, nonce, NET, True).status == "wrong"


def test_a_token_for_another_nonce_or_a_made_up_nonce_is_refused(svc, store):
    _, nonce = provider_token(svc, "g-ada")
    other_token, _ = provider_token(svc, "g-ada")
    assert svc.provider_sign_in("google", other_token, nonce, NET, True).status == "wrong"
    assert svc.provider_sign_in("google", "g-ada|made-up", "made-up", NET, True).status == "wrong"
    assert _count(store, "accounts") == 0


def test_a_nonce_dies_at_ten_minutes(svc, clock):
    token, nonce = provider_token(svc, "g-ada")
    clock.advance(601)
    assert svc.provider_sign_in("google", token, nonce, NET, True).status == "wrong"


def test_a_nonce_is_not_a_sign_in_code(svc, mailer):
    nonce = svc.provider_start(NET).challenge
    start = svc.start_sign_in(ADDR, NET)
    assert svc.finish_sign_in(nonce, ADDR, "000000", NET, True).status == "wrong"
    assert start.status == "sent"


def test_an_unknown_provider_or_one_not_set_up_is_not_available(store, keys, mailer, clock):
    only_google = AccountsService(store, keys, mailer, clock=clock, verifier=FakeVerifier(("google",)))
    token, nonce = provider_token(only_google, "x")
    assert only_google.provider_sign_in("apple", token, nonce, NET, True).status == "not_available"
    assert only_google.provider_sign_in("github", token, nonce, NET, True).status == "not_available"
    none = AccountsService(store, keys, mailer, clock=clock)
    assert none.provider_sign_in("google", token, nonce, NET, True).status == "not_available"


def test_a_provider_id_is_stored_only_as_a_keyed_hash(svc, tmp_path):
    provider_sign_in(svc, subject="g-1234567890-distinct")
    for name in ("d.db", "e.db"):
        data = (tmp_path / name).read_bytes()
        assert b"g-1234567890-distinct" not in data and b"google.example" not in data


def test_the_email_a_provider_reports_is_never_read_or_kept(svc, tmp_path):
    token, nonce = provider_token(svc, "g-ada")
    svc.provider_sign_in("google", token, nonce, NET, True)
    assert b"example.org" not in (tmp_path / "d.db").read_bytes()


def test_a_matching_email_never_joins_an_address_account_to_a_provider_account(svc, mailer, store):
    typed = svc.session(sign_in(svc, mailer, ADDR))
    other = svc.session(provider_sign_in(svc, "google", ADDR, network="198.51.100.9"))
    assert typed.account_id != other.account_id and _count(store, "accounts") == 2


def test_the_new_account_limit_per_network_applies_to_provider_sign_ups(svc):
    for i in range(5):
        provider_sign_in(svc, subject=f"g-{i}")
    token, nonce = provider_token(svc, "g-6")
    assert svc.provider_sign_in("google", token, nonce, NET, True).status == "throttled"


def test_nonce_starts_are_limited_per_network(svc):
    results = [svc.provider_start(NET).status for _ in range(31)]
    assert results[:30] == ["sent"] * 30 and results[30] == "throttled"


def _stepped_up_by_provider(svc, subject="g-ada"):
    cookie = provider_sign_in(svc, subject=subject)
    session = svc.session(cookie)
    token, nonce = provider_token(svc, subject)
    assert svc.provider_step_up(session, "google", token, nonce, NET).status == "ok"
    return svc.session(cookie), cookie


def test_a_provider_only_account_steps_up_only_by_its_own_provider_id(svc):
    cookie = provider_sign_in(svc, subject="g-ada")
    session = svc.session(cookie)
    token, nonce = provider_token(svc, "g-someone-else")
    assert svc.provider_step_up(session, "google", token, nonce, NET).status == "wrong"
    assert not svc.session(cookie).stepped_up
    assert _stepped_up_by_provider(svc, "g-bob")[0].stepped_up


def test_adding_an_address_to_a_provider_only_account_needs_the_provider_step_up(svc, mailer, store):
    cookie = provider_sign_in(svc, subject="g-ada")
    assert svc.change_address_start(svc.session(cookie), ADDR, NET).status == "step_up_needed"
    session, cookie = _stepped_up_by_provider(svc, "g-ada2")
    started = svc.change_address_start(session, ADDR, NET)
    assert svc.change_address_finish(session, started.challenge, mailer.last_code(ADDR), NET, ADDR).status == "ok"
    assert store.account(session.account_id).address_hash == svc.keys.address_hash(ADDR)
    assert svc.me(svc.session(cookie))["sign_in_methods"] == ["address", "google"]


def test_linking_needs_a_step_up_and_clears_every_other_session(svc, mailer, clock):
    from engine.accounts.tests.conftest import stepped_up_session
    session, cookie = stepped_up_session(svc, mailer, clock)
    other = sign_in(svc, mailer, ADDR, "198.51.100.30")
    token, nonce = provider_token(svc, "g-ada")
    assert svc.provider_link(session, "google", token, nonce, NET).status == "ok"
    assert svc.session(other) is None and svc.session(cookie) is not None
    assert svc.me(svc.session(cookie))["sign_in_methods"] == ["address", "google"]
    signed = svc.session(provider_sign_in(svc, subject="g-ada", network="198.51.100.9"))
    assert signed.account_id == svc.session(cookie).account_id


def test_linking_without_a_fresh_step_up_is_refused(svc, mailer):
    session = svc.session(sign_in(svc, mailer, ADDR))
    token, nonce = provider_token(svc, "g-ada")
    assert svc.provider_link(session, "google", token, nonce, NET).status == "step_up_needed"
    assert svc.provider_unlink(session, "google").status == "step_up_needed"


def test_a_provider_id_already_on_another_account_cannot_be_linked(svc, mailer, clock):
    from engine.accounts.tests.conftest import stepped_up_session
    provider_sign_in(svc, subject="g-taken")
    session, _ = stepped_up_session(svc, mailer, clock)
    token, nonce = provider_token(svc, "g-taken")
    assert svc.provider_link(session, "google", token, nonce, NET).status == "provider_cannot_use"
    assert svc.store.links_of(session.account_id) == {}


def test_an_account_holds_one_link_per_provider(svc, mailer, clock):
    from engine.accounts.tests.conftest import stepped_up_session
    session, _ = stepped_up_session(svc, mailer, clock)
    token, nonce = provider_token(svc, "g-1")
    assert svc.provider_link(session, "google", token, nonce, NET).status == "ok"
    token, nonce = provider_token(svc, "g-2")
    assert svc.provider_link(session, "google", token, nonce, NET).status == "provider_cannot_use"


def test_the_last_way_in_cannot_be_unlinked(svc):
    session, _ = _stepped_up_by_provider(svc)
    assert svc.provider_unlink(session, "google").status == "last_method"
    assert svc.store.links_of(session.account_id)


def test_unlinking_a_provider_clears_other_sessions_and_leaves_the_address(svc, mailer, clock):
    from engine.accounts.tests.conftest import stepped_up_session
    session, cookie = stepped_up_session(svc, mailer, clock)
    token, nonce = provider_token(svc, "g-ada")
    svc.provider_link(session, "google", token, nonce, NET)
    other = provider_sign_in(svc, subject="g-ada", network="198.51.100.9")
    assert svc.provider_unlink(svc.session(cookie), "google").status == "ok"
    assert svc.session(other) is None and svc.session(cookie) is not None
    assert svc.me(svc.session(cookie))["sign_in_methods"] == ["address"]
    token, nonce = provider_token(svc, "g-ada")
    assert svc.provider_sign_in("google", token, nonce, NET).status == "needs_age_answer"


def test_deleting_an_account_removes_its_provider_links(svc, store):
    session, _ = _stepped_up_by_provider(svc)
    assert svc.delete_account(session).status == "ok"
    assert _count(store, "accounts") == 0 and _count(store, "linked_sign_ins") == 0
    token, nonce = provider_token(svc, "g-ada")
    assert svc.provider_sign_in("google", token, nonce, NET).status == "needs_age_answer"


def test_a_provider_id_is_found_under_a_previous_key_and_rewritten_under_the_current_one(tmp_path, mailer, clock):
    old = KeyRing(ADDRESS_KEY, SESSION_KEY)
    store = AccountStore(str(tmp_path / "d.db"), str(tmp_path / "e.db"))
    first = AccountsService(store, old, mailer, clock=clock, verifier=FakeVerifier())
    provider_sign_in(first, subject="g-ada")
    rotated = KeyRing("b" * 40, SESSION_KEY, key_id="k2", previous=[PreviousKey("k1", ADDRESS_KEY, date(2099, 1, 1))])
    second = AccountsService(store, rotated, mailer, clock=clock, verifier=FakeVerifier())
    assert store.accounts_on_older_keys("k2") == 1
    provider_sign_in(second, subject="g-ada", network="198.51.100.9")
    assert store.accounts_on_older_keys("k2") == 0 and _count(store, "accounts") == 1
    store.close()


def test_a_file_made_when_every_account_had_an_address_is_rebuilt_with_the_address_optional(tmp_path):
    path = tmp_path / "d.db"
    conn = sqlite3.connect(path)
    conn.executescript(
        "CREATE TABLE accounts (account_id TEXT PRIMARY KEY, address_hash TEXT NOT NULL UNIQUE, day_created TEXT NOT NULL,"
        " refill_day INTEGER NOT NULL, week_last_used TEXT NOT NULL, age_band TEXT NOT NULL) WITHOUT ROWID;"
        "INSERT INTO accounts VALUES ('a1', 'k1:abc', 'day1', 1, 'week1', '18+');"
    )
    conn.close()
    store = AccountStore(str(path), str(tmp_path / "e.db"))
    assert store.account("a1").address_hash == "k1:abc"
    assert store.create_account(Account("a2", None, "day2", 2, "week1", "18+"))
    store.close()


def test_a_provider_cannot_stand_in_for_the_address_code_on_an_account_that_has_an_address(svc, mailer, clock):
    from engine.accounts.tests.conftest import stepped_up_session
    session, cookie = stepped_up_session(svc, mailer, clock)
    token, nonce = provider_token(svc, "g-ada")
    assert svc.provider_link(session, "google", token, nonce, NET).status == "ok"
    clock.advance(601)  # the address step-up has run out
    session = svc.session(cookie)
    assert not session.stepped_up
    via_google = svc.session(provider_sign_in(svc, subject="g-ada", network="198.51.100.9"))
    token, nonce = provider_token(svc, "g-ada")
    assert svc.provider_step_up(via_google, "google", token, nonce, NET).status == "wrong"
    assert svc.change_address_start(svc.session(provider_sign_in(svc, subject="g-ada", network="198.51.100.10")), "evil@example.org", NET).status == "step_up_needed"


def test_two_unlinks_at_once_cannot_leave_a_provider_only_account_with_no_way_in(svc, store):
    import threading
    session, cookie = _stepped_up_by_provider(svc, "g-ada")
    token, nonce = provider_token(svc, "a-ada")
    assert svc.provider_link(session, "apple", token, nonce, NET).status == "ok"
    session = svc.session(cookie)
    svc.store.step_up_session(session.token_hash, svc.now() + 600)
    results = []

    def unlink(provider):
        results.append(svc.provider_unlink(svc.session(cookie), provider).status)

    threads = [threading.Thread(target=unlink, args=(p,)) for p in ("google", "apple")]
    [t.start() for t in threads]
    [t.join() for t in threads]
    assert sorted(results) == ["last_method", "ok"]
    assert len(store.links_of(session.account_id)) == 1


def test_a_link_that_lands_after_the_account_is_deleted_leaves_nothing(svc, store):
    session, _ = _stepped_up_by_provider(svc)
    svc.delete_account(session)
    assert store.add_link(session.account_id, "k1:orphan", "apple") is False
    assert _count(store, "linked_sign_ins") == 0


def test_issuing_a_nonce_writes_nothing_and_many_networks_cannot_lock_sign_in_out(svc, store):
    for i in range(300):
        assert svc.provider_start(f"10.{i // 250}.{i % 250}.1").status == "sent"
    assert [store._e.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0] for t in ("challenges", "spent_nonces")] == [0, 0]
    assert provider_sign_in(svc)


def test_a_forged_or_changed_nonce_is_refused(svc):
    token, nonce = provider_token(svc, "g-ada")
    body, _, tag = nonce.rpartition(".")
    random_part, _, expiry = body.rpartition(".")
    for forged in (f"{random_part}.{int(expiry) + 99999}.{tag}", f"{body}.{'0' * len(tag)}", "x.1.y", ".", ""):
        assert svc.provider_sign_in("google", f"g-ada|{forged}", forged, NET, True).status == "wrong"


def test_a_spent_nonce_row_is_removed_at_its_expiry(svc, store, clock):
    provider_sign_in(svc)
    assert store._e.execute("SELECT COUNT(*) FROM spent_nonces").fetchone()[0] == 1
    clock.advance(601)
    svc.purge()
    assert store._e.execute("SELECT COUNT(*) FROM spent_nonces").fetchone()[0] == 0
