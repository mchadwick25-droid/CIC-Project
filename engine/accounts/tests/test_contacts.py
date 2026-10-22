from engine.accounts.contacts import ContactStore
from engine.accounts.tests.conftest import FakeCipher, sign_in, stepped_up_session

ADDR = "ada@example.org"
NEW = "ada.new@example.org"
NET = "203.0.113.5"


def test_a_first_sign_in_keeps_the_address_for_sending_only(svc, mailer, contacts):
    session = svc.session(sign_in(svc, mailer, ADDR))
    assert contacts.get(session.account_id) == ADDR


def test_the_account_file_still_holds_no_address(svc, mailer, contacts, tmp_path):
    sign_in(svc, mailer, ADDR)
    for name in ("d.db", "e.db"):
        assert b"ada@example.org" not in (tmp_path / name).read_bytes()


def test_an_address_change_replaces_the_kept_address(svc, mailer, clock, contacts):
    session, cookie = stepped_up_session(svc, mailer, clock)
    started = svc.change_address_start(session, NEW, NET)
    assert svc.change_address_finish(session, started.challenge, mailer.last_code(NEW), NET, NEW).status == "ok"
    assert contacts.get(session.account_id) == NEW


def test_an_address_change_must_finish_with_the_address_the_code_went_to(svc, mailer, clock, contacts):
    session, cookie = stepped_up_session(svc, mailer, clock)
    started = svc.change_address_start(session, NEW, NET)
    assert svc.change_address_finish(session, started.challenge, mailer.last_code(NEW), NET, "other@example.org").status == "wrong"
    assert contacts.get(session.account_id) == ADDR


def test_deleting_an_account_deletes_its_contact(svc, mailer, clock, contacts):
    session, cookie = stepped_up_session(svc, mailer, clock)
    contacts.put_pending(session.account_id, NEW)
    assert svc.delete_account(session).status == "ok"
    assert contacts.get(session.account_id) is None
    assert contacts.take_pending(session.account_id) is None
    rows = contacts._c.execute("SELECT (SELECT COUNT(*) FROM contacts), (SELECT COUNT(*) FROM pending_contacts)").fetchone()
    assert rows == (0, 0)


def test_a_restored_backup_does_not_bring_a_deleted_contact_back(svc, mailer, clock, contacts, store):
    session, cookie = stepped_up_session(svc, mailer, clock)
    snapshot = store._d.execute("SELECT * FROM accounts").fetchall()
    svc.delete_account(session)
    store._d.executemany("INSERT INTO accounts VALUES (?, ?, ?, ?, ?, ?)", snapshot)  # a restore
    contacts.put(session.account_id, ADDR)
    assert svc.reapply_ledger() == 1
    assert contacts.get(session.account_id) is None


def test_a_row_moved_to_another_account_does_not_open(svc, mailer, contacts):
    a = svc.session(sign_in(svc, mailer, ADDR))
    b = svc.session(sign_in(svc, mailer, "bob@example.org", "198.51.100.9"))
    blob = contacts._c.execute("SELECT blob FROM contacts WHERE account_id = ?", (a.account_id,)).fetchone()[0]
    contacts._c.execute("UPDATE contacts SET blob = ? WHERE account_id = ?", (blob, b.account_id))
    assert contacts.get(b.account_id) is None


def test_a_wrong_key_reads_nothing(tmp_path, svc, mailer, contacts):
    session = svc.session(sign_in(svc, mailer, ADDR))
    other = ContactStore(str(tmp_path / "c.db"), FakeCipher("c2"))
    assert other.get(session.account_id) is None
    other.close()


def test_a_contact_sealed_under_an_older_key_is_resealed_at_the_next_code_sign_in(tmp_path, svc, mailer, contacts, store, keys, clock):
    from engine.accounts.service import AccountsService
    session = svc.session(sign_in(svc, mailer, ADDR))
    assert contacts.on_older_keys() == 0
    rotated = ContactStore(str(tmp_path / "c.db"), FakeCipher("c2", known=("c2", "c1")))
    assert rotated.on_older_keys() == 1
    second = AccountsService(store, keys, mailer, clock=clock, contacts=rotated)
    sign_in(second, mailer, ADDR, "198.51.100.9")
    assert rotated.on_older_keys() == 0 and rotated.is_current(session.account_id)
    rotated.close()


def test_a_provider_only_account_has_no_contact(svc, contacts):
    from engine.accounts.tests.conftest import provider_sign_in
    session = svc.session(provider_sign_in(svc))
    assert contacts.get(session.account_id) is None


def test_no_log_line_holds_the_kept_address(svc, mailer, caplog):
    import logging
    caplog.set_level(logging.DEBUG)
    mailer.fail = True
    sign_in_ok = svc.start_sign_in(ADDR, NET)
    assert sign_in_ok.status == "send_failed"
    assert "ada@example.org" not in caplog.text
