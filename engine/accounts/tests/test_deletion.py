import re
from datetime import timedelta

from engine.accounts.service import ledger_hash
from engine.accounts.tests.conftest import sign_in, stepped_up_session

ADDR = "ada@example.org"
NET = "203.0.113.5"


def test_deleting_an_account_removes_it_its_sessions_and_its_codes(svc, mailer, clock, store):
    session, cookie = stepped_up_session(svc, mailer, clock)
    svc.make_recovery_code(svc.session(cookie))
    assert svc.delete_account(svc.session(cookie)).status == "ok"
    assert svc.session(cookie) is None
    for table in ("accounts", "recovery_codes", "pending_changes"):
        assert store._d.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0] == 0
    for table in ("sessions", "sign_in_codes"):
        assert store._e.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0] == 0


def test_the_ledger_holds_a_hash_of_the_random_id_never_the_address(svc, mailer, clock, store):
    session, cookie = stepped_up_session(svc, mailer, clock)
    account_id = svc.session(cookie).account_id
    address_hash = svc.keys.address_hash(ADDR)
    svc.delete_account(svc.session(cookie))
    rows = store._d.execute("SELECT ledger_hash, expires_on FROM deletion_ledger").fetchall()
    assert rows == [(ledger_hash(account_id), (svc.today() + timedelta(days=16)).isoformat())]
    assert address_hash.split(":")[1] not in rows[0][0]
    clock.advance(17 * 86400)
    svc.purge()
    assert store._d.execute("SELECT COUNT(*) FROM deletion_ledger").fetchone()[0] == 0


def test_a_restored_backup_does_not_bring_a_deleted_account_back(svc, mailer, clock, store):
    session, cookie = stepped_up_session(svc, mailer, clock)
    account = store.account(svc.session(cookie).account_id)
    svc.delete_account(svc.session(cookie))
    store.create_account(account)  # what a restore does
    assert store.account(account.account_id) is not None
    assert svc.reapply_ledger() == 1
    assert store.account(account.account_id) is None


def test_export_holds_the_account_s_fields_and_no_code(svc, mailer, clock):
    session, cookie = stepped_up_session(svc, mailer, clock)
    svc.make_recovery_code(svc.session(cookie))
    data = svc.export(svc.session(cookie)).data
    assert set(data) == {"day_created", "refill_day", "week_last_used", "age_band"}


def test_me_reports_the_account_without_identifying_it(svc, mailer, clock):
    session, cookie = stepped_up_session(svc, mailer, clock)
    info = svc.me(svc.session(cookie))
    assert set(info) == {"signed_in", "refill_day", "age_band", "pending_recovery", "has_recovery_code"}


def test_neither_file_holds_an_address_after_a_hundred_sign_ins(svc, mailer, clock, store, tmp_path):
    addresses = [f"person{i}.name@mail{i}.example.org" for i in range(100)]
    for i, address in enumerate(addresses):
        sign_in(svc, mailer, address, f"198.51.100.{i % 250}", 1985)
        clock.advance(2)
    # also exercise a recovery change and an address change, which hold hashes of new addresses
    session, cookie = stepped_up_session(svc, mailer, clock, addresses[0], "198.51.100.200")
    svc.change_address_start(session, "moved.person@elsewhere.example.net", "198.51.100.201")
    svc.change_address_finish(svc.session(cookie), "moved.person@elsewhere.example.net",
                              mailer.last_code("moved.person@elsewhere.example.net"), "198.51.100.201")
    store._d.execute("VACUUM")
    store._e.execute("VACUUM")
    for name in ("d.db", "e.db"):
        data = (tmp_path / name).read_bytes()
        for address in addresses + ["moved.person@elsewhere.example.net"]:
            local, domain = address.split("@")
            for held in (address, local, domain):
                assert held.encode() not in data, f"{name} holds {held}"
        assert not re.search(rb"[\w.+-]+@[\w-]+\.[\w.]+", data)
    assert not list(tmp_path.glob("*-journal")) and not list(tmp_path.glob("*-wal"))


def test_a_deleted_account_s_bytes_are_overwritten(svc, mailer, clock, store, tmp_path):
    session, cookie = stepped_up_session(svc, mailer, clock)
    account_id = svc.session(cookie).account_id
    address_hash = svc.keys.address_hash(ADDR)
    assert account_id.encode() in (tmp_path / "d.db").read_bytes()
    svc.delete_account(svc.session(cookie))
    data = (tmp_path / "d.db").read_bytes()
    assert account_id.encode() not in data and address_hash.encode() not in data


def test_no_log_line_holds_an_address_or_a_code(svc, mailer, clock, caplog):
    with caplog.at_level("DEBUG"):
        session, cookie = stepped_up_session(svc, mailer, clock)
        svc.start_sign_in("nobody@example.org", NET)
        svc.finish_sign_in("nobody@example.org", "000000", NET)
        svc.make_recovery_code(svc.session(cookie))
        svc.delete_account(svc.session(cookie))
    text = caplog.text
    assert not re.search(r"[\w.+-]+@[\w-]+\.[\w.]+", text)
    for _, code in mailer.sent:
        assert code not in text
