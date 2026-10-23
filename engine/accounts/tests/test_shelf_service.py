import pytest

from engine.accounts.service import AccountsService
from engine.accounts.tests.conftest import FakeCipher, sign_in

ADDR = "ada@example.org"
SESSION_ID = "11111111-2222-3333-4444-555555555555"
CODE = "ABCD-EFGH-JKMN-PQRS-TVWX-YZ12-34"


@pytest.fixture
def shelved(store, keys, mailer, clock, contacts):
    return AccountsService(store, keys, mailer, clock=clock, contacts=contacts, shelf_cipher=FakeCipher("s1"))


def test_a_shelved_conversation_is_listed_and_its_code_comes_back_only_to_its_owner(shelved, mailer):
    owner = shelved.session(sign_in(shelved, mailer, ADDR))
    other = shelved.session(sign_in(shelved, mailer, "bob@example.org", "198.51.100.9"))
    assert shelved.shelf_add(owner, SESSION_ID, CODE).status == "ok"
    assert [s for s, _ in shelved.shelf_list(owner)] == [SESSION_ID]
    assert shelved.shelf_open(owner, SESSION_ID) == CODE
    assert shelved.shelf_open(other, SESSION_ID) is None and shelved.shelf_list(other) == []
    assert shelved.shelf_add(other, SESSION_ID, CODE).status == "shelf_taken"


def test_the_sealed_code_is_bound_to_its_account_and_conversation(shelved, mailer, store):
    owner = shelved.session(sign_in(shelved, mailer, ADDR))
    shelved.shelf_add(owner, SESSION_ID, CODE)
    sealed = store.shelf_sealed(owner.account_id, SESSION_ID)
    other_context = shelved.shelf_cipher.decrypt(sealed, "shelf|someone-else|" + SESSION_ID)
    assert other_context is None


def test_the_shelf_is_not_available_without_a_cipher(store, keys, mailer, clock):
    plain = AccountsService(store, keys, mailer, clock=clock)
    owner = plain.session(sign_in(plain, mailer, ADDR))
    assert plain.shelf_add(owner, SESSION_ID, CODE).status == "not_available"
    assert plain.shelf_open(owner, SESSION_ID) is None


@pytest.mark.parametrize("session_id, code", [("", CODE), (SESSION_ID, ""), (None, CODE), (SESSION_ID, None), ("x" * 65, CODE), (SESSION_ID, "c" * 81)])
def test_a_bad_id_or_code_is_refused(shelved, mailer, session_id, code):
    owner = shelved.session(sign_in(shelved, mailer, ADDR))
    assert shelved.shelf_add(owner, session_id, code).status == "wrong"


def test_removing_a_conversation_takes_it_off_the_shelf(shelved, mailer):
    owner = shelved.session(sign_in(shelved, mailer, ADDR))
    shelved.shelf_add(owner, SESSION_ID, CODE)
    assert shelved.is_shelved(SESSION_ID) and shelved.shelf_remove(owner, SESSION_ID)
    assert not shelved.is_shelved(SESSION_ID) and not shelved.shelf_remove(owner, SESSION_ID)


def test_use_of_an_account_counts_as_activity(shelved, mailer, clock, store):
    cookie = sign_in(shelved, mailer, ADDR)
    owner = shelved.session(cookie)
    for _ in range(4):
        clock.advance(8 * 86400)
        assert shelved.session(cookie) is not None  # a live session in use
    assert store.account(owner.account_id).week_last_used == f"{shelved.today().isocalendar()[0]}-W{shelved.today().isocalendar()[1]:02d}"
    assert shelved.stale_account_ids() == []
