"""A3: the shelf. A signed-in person's conversations, kept apart from the account file and gone
from every store when deleted."""
import dataclasses
from datetime import date, datetime, timedelta, timezone

import pytest
from fastapi.testclient import TestClient

from engine.accounts.contacts import ContactStore
from engine.accounts.keys import KeyRing
from engine.accounts.service import AccountsService
from engine.accounts.store import AccountStore
from engine.accounts.tests.conftest import ADDRESS_KEY, SESSION_KEY, Clock, FakeMailer
from engine.api import shelf
from engine.api.accounts_routes import AccountsRuntime
from engine.api.app import create_app
from engine.api.contact_cipher import ContactCipher
from engine.api.qc_recorder import QCRecorder
from engine.api.tests.test_deeper_seam import ACUTE, RecordingClient, open_session, say
from engine.feedback.store import FeedbackStore
from engine.m7 import retention
from engine.m7.qc_store import QCStore

H = {"x-cic-accounts": "1"}
ADDR = "ada@example.org"
QC_SECRET = "q" * 40


@pytest.fixture
def mailer():
    return FakeMailer()


@pytest.fixture
def accounts(tmp_path, mailer):
    store = AccountStore(str(tmp_path / "d.db"), str(tmp_path / "e.db"))
    contacts = ContactStore(str(tmp_path / "c.db"), ContactCipher("c" * 40))
    service = AccountsService(
        store, KeyRing(ADDRESS_KEY, SESSION_KEY), mailer, clock=Clock(), contacts=contacts,
        shelf_cipher=ContactCipher("h" * 40, key_id="s1", purpose="shelf"),
    )
    yield AccountsRuntime(service=service, miss_delay_seconds=0.0, start_floor_seconds=0.0)
    store.close()
    contacts.close()


@pytest.fixture
def qc(tmp_path, registry):
    return QCRecorder(QCStore(tmp_path / "qc.db"), registry, secret=QC_SECRET)


@pytest.fixture
def feedback(tmp_path):
    return FeedbackStore(tmp_path / "fb.db")


def build(store, usage_store, world_loader, registry, accounts, qc, feedback, tmp_path, client=None):
    app = create_app(
        voice_client=client or RecordingClient(), voice_model_id="m", safety_client=client or RecordingClient(), safety_model_id="m",
        store=store, usage_store=usage_store, world_loader=world_loader, registry=registry,
        default_world_key="fix", accounts=accounts, qc_recorder=qc, feedback_store=feedback,
        m7_audit_root=tmp_path / "audits", rate_limit=False,
    )
    return TestClient(app, base_url="https://testserver")


@pytest.fixture
def http(store, usage_store, world_loader, registry, accounts, qc, feedback, tmp_path):
    return build(store, usage_store, world_loader, registry, accounts, qc, feedback, tmp_path)


def sign_in(client, mailer, address=ADDR):
    started = client.post("/api/accounts/sign-in/start", json={"address": address}, headers=H)
    done = client.post(
        "/api/accounts/sign-in/finish",
        json={"challenge": started.json()["challenge"], "address": address, "code": mailer.last_code(address), "over_18": True},
        headers=H,
    )
    assert done.json()["status"] == "ok", done.text


def post(client, path, **body):
    return client.post(f"/api/accounts/{path}", json=body, headers=H)


def stepped_up(client, accounts):
    session = accounts.service.session(client.cookies.get(accounts.cookie_name))
    accounts.service.store.step_up_session(session.token_hash, accounts.service.now() + 600)


def new_account_client(http, mailer, address):
    other = TestClient(http.app, base_url="https://testserver")
    sign_in(other, mailer, address)
    return other


def test_a_conversation_opened_while_signed_in_is_on_the_shelf_from_the_start(http, accounts, mailer):
    sign_in(http, mailer)
    session_id, auth = open_session(http)
    listed = http.get("/api/accounts/shelf").json()["conversations"]
    assert [c["session_id"] for c in listed] == [session_id]
    assert listed[0]["worlds"] and listed[0]["started"] and listed[0]["turns"] == 0


def test_an_anonymous_conversation_is_never_shelved_and_a_signed_in_one_is_shelved_once_when_carried_over(http, accounts, mailer):
    session_id, auth = open_session(http)
    say(http, session_id, auth, "a question before signing in")
    sign_in(http, mailer)
    assert http.get("/api/accounts/shelf").json()["conversations"] == []
    code = auth["Authorization"].removeprefix("Session ")
    assert post(http, "shelf/add", session_id=session_id, session_code=code).status_code == 200
    assert post(http, "shelf/add", session_id=session_id, session_code=code).status_code == 200
    listed = http.get("/api/accounts/shelf").json()["conversations"]
    assert [c["session_id"] for c in listed] == [session_id] and listed[0]["title"] == "a question before signing in"


def test_a_conversation_cannot_be_shelved_without_its_own_code_or_onto_two_shelves(http, accounts, mailer):
    session_id, auth = open_session(http)
    code = auth["Authorization"].removeprefix("Session ")
    sign_in(http, mailer)
    assert post(http, "shelf/add", session_id=session_id, session_code="WRONGCODE").status_code == 400
    assert post(http, "shelf/add", session_id="no-such", session_code=code).status_code == 400
    assert post(http, "shelf/add", session_id=session_id, session_code=code).status_code == 200
    other = new_account_client(http, mailer, "bob@example.org")
    refused = post(other, "shelf/add", session_id=session_id, session_code=code)
    assert refused.status_code == 400 and "another account" in refused.json()["detail"]


def test_the_account_files_hold_no_conversation_text_title_world_or_plain_code(http, accounts, mailer, tmp_path):
    sign_in(http, mailer)
    session_id, auth = open_session(http)
    say(http, session_id, auth, "a very particular question about the Council of Nicaea")
    code = auth["Authorization"].removeprefix("Session ")
    for name in ("d.db", "e.db", "c.db"):
        data = (tmp_path / name).read_bytes()
        assert b"Nicaea" not in data and code.encode() not in data and code.replace("-", "").encode() not in data
    data = (tmp_path / "d.db").read_bytes()
    assert session_id.encode() in data  # the id is what the shelf holds


def test_only_the_owner_can_reopen_a_shelved_conversation_and_the_code_works(http, accounts, mailer):
    sign_in(http, mailer)
    session_id, auth = open_session(http)
    say(http, session_id, auth, "hello")
    reopened = post(http, "shelf/reopen", session_id=session_id).json()
    assert reopened["session_id"] == session_id and reopened["holds_crisis_turn"] is False
    again = http.get(f"/api/session/{session_id}/transcript", headers={"Authorization": f"Session {reopened['session_code']}"})
    assert again.status_code == 200 and again.json()["turn_count"] >= 1
    other = new_account_client(http, mailer, "bob@example.org")
    assert post(other, "shelf/reopen", session_id=session_id).status_code == 400
    assert TestClient(http.app, base_url="https://testserver").post("/api/accounts/shelf/reopen", json={"session_id": session_id}, headers=H).status_code == 401


def test_reopening_a_conversation_that_holds_a_safety_turn_flags_it_every_time(store, usage_store, world_loader, registry, accounts, qc, feedback, tmp_path, mailer):
    http = build(store, usage_store, world_loader, registry, accounts, qc, feedback, tmp_path, client=RecordingClient(safety=ACUTE))
    sign_in(http, mailer)
    session_id, auth = open_session(http)
    say(http, session_id, auth, "I do not know how to say this")
    assert [post(http, "shelf/reopen", session_id=session_id).json()["holds_crisis_turn"] for _ in range(2)] == [True, True]
    assert http.get("/api/accounts/shelf").json()["conversations"][0]["holds_crisis_turn"] is True


def code_of(auth):
    return auth["Authorization"].removeprefix("Session ")


def deleted_everywhere(session_id, store, usage_store, feedback, qc, tmp_path, code):
    assert store.read_events(session_id) == []
    assert all(r.session_id != session_id for r in usage_store.read_all())
    assert feedback.like_exists(session_id, 1) is False
    assert qc.store.max_round(qc.token_for_code(code)) == 0


def test_deleting_one_conversation_removes_it_from_every_store_and_the_shelf(http, accounts, mailer, store, usage_store, feedback, qc, tmp_path):
    sign_in(http, mailer)
    session_id, auth = open_session(http)
    say(http, session_id, auth, "hello")
    feedback.add({"kind": "like", "page": "p", "session_id": session_id, "turn_index": 1})
    assert qc.store.max_round(qc.token_for_code(code_of(auth))) >= 1
    other_id, other_auth = open_session(http)
    say(http, other_id, other_auth, "keep this one")
    assert post(http, "shelf/delete", session_id=session_id).status_code == 200
    deleted_everywhere(session_id, store, usage_store, feedback, qc, tmp_path, code_of(auth))
    assert qc.store.max_round(qc.token_for_code(code_of(other_auth))) >= 1
    assert [c["session_id"] for c in http.get("/api/accounts/shelf").json()["conversations"]] == [other_id]
    assert http.get(f"/api/session/{session_id}/transcript", headers=auth).status_code == 401
    assert post(http, "shelf/delete", session_id=session_id).status_code == 400


def test_nobody_can_delete_a_conversation_from_another_shelf(http, accounts, mailer, store):
    sign_in(http, mailer)
    session_id, auth = open_session(http)
    other = new_account_client(http, mailer, "bob@example.org")
    assert post(other, "shelf/delete", session_id=session_id).status_code == 400
    assert store.read_events(session_id)


def test_deleting_the_account_leaves_no_trace_of_its_conversations_in_any_file(http, accounts, mailer, store, usage_store, feedback, qc, tmp_path):
    sign_in(http, mailer)
    ids, codes_ = [], []
    for text in ("first question", "second question"):
        session_id, auth = open_session(http)
        say(http, session_id, auth, text)
        feedback.add({"kind": "like", "page": "p", "session_id": session_id, "turn_index": 1})
        ids.append(session_id)
        codes_.append(code_of(auth))
    tokens = [qc.token_for_code(c) for c in codes_]
    assert all(qc.store.max_round(t) >= 1 for t in tokens)
    stepped_up(http, accounts)
    assert http.post("/api/accounts/delete", json={}, headers=H).status_code == 200
    for session_id, code in zip(ids, codes_):
        deleted_everywhere(session_id, store, usage_store, feedback, qc, tmp_path, code)
    assert all(qc.store.max_round(t) == 0 for t in tokens)
    for name in ("d.db", "e.db", "c.db", "events.db", "usage.db", "fb.db", "qc.db"):
        path = tmp_path / name
        if path.exists():
            data = path.read_bytes() + (tmp_path / (name + "-wal")).read_bytes() if (tmp_path / (name + "-wal")).exists() else path.read_bytes()
            assert not any(i.encode() in data for i in ids), name


def test_an_account_whose_conversations_cannot_be_removed_is_kept_whole(http, accounts, mailer, store, monkeypatch):
    sign_in(http, mailer)
    session_id, auth = open_session(http)
    stepped_up(http, accounts)

    def broken(self, session_id):
        raise RuntimeError("store unavailable")

    monkeypatch.setattr(shelf.ConversationEraser, "erase", broken)
    assert http.post("/api/accounts/delete", json={}, headers=H).status_code == 500
    assert accounts.service.store._d.execute("SELECT COUNT(*) FROM accounts").fetchone()[0] == 1
    assert store.read_events(session_id)
    assert http.get("/api/accounts/me").json()["signed_in"] is True


def test_the_ninety_day_clearing_leaves_a_shelved_conversation_and_removes_an_unshelved_one(http, accounts, mailer, store, tmp_path):
    sign_in(http, mailer)
    shelved, shelved_auth = open_session(http)
    other_client = TestClient(http.app, base_url="https://testserver")
    unshelved, _ = open_session(other_client)
    cutoff = (datetime.now(timezone.utc) + timedelta(days=1)).isoformat()
    removed = store.purge_inactive(cutoff, accounts.service.is_shelved)
    assert removed == 1 and store.read_events(shelved) and store.read_events(unshelved) == []


def test_the_retention_job_is_handed_the_shelf_as_its_exemption(http, accounts, mailer, store, tmp_path):
    sign_in(http, mailer)
    shelved, _ = open_session(http)
    future = datetime.now(timezone.utc) + timedelta(days=200)
    retention.run_once(store.db_path, str(tmp_path / "qc.db"), tmp_path / "status", now=future, is_exempt=accounts.service.is_shelved)
    assert store.read_events(shelved)


def test_an_account_unused_for_two_years_is_removed_with_its_shelf_and_a_used_one_stays(http, accounts, mailer, store, usage_store, feedback, qc, tmp_path):
    from engine.api.accounts_routes import sweep_unused_accounts
    clock = accounts.service._clock
    sign_in(http, mailer)
    idle_id, _ = open_session(http)
    active = new_account_client(http, mailer, "bob@example.org")
    active_id, _ = open_session(active)
    clock.advance(365 * 86400 * 2 + 20 * 86400)
    sign_in(active, mailer, "bob@example.org")  # bob is back
    assert sweep_unused_accounts(accounts) == 1
    assert store.read_events(idle_id) == [] and store.read_events(active_id)
    assert accounts.service.store._d.execute("SELECT COUNT(*) FROM accounts").fetchone()[0] == 1
    assert accounts.service.store._d.execute("SELECT COUNT(*) FROM shelf WHERE session_id = ?", (idle_id,)).fetchone()[0] == 0


def test_the_review_token_is_the_same_across_a_restart_and_rounds_carry_on(tmp_path, registry):
    code = "ABCD-EFGH-JKMN-PQRS-TVWX-YZ12-34"
    first = QCRecorder(QCStore(tmp_path / "q.db"), registry, secret=QC_SECRET)
    token, round_one = first._next_round("sess-1", code)
    first.store.write_turn(conversation_token=token, round_no=round_one, world="fix", package_hash=None, model_id=None,
                           routing="x", flags={}, question_text=None, answer_text=None, marks={}, scores={}, day=date(2026, 10, 5))
    restarted = QCRecorder(QCStore(tmp_path / "q.db"), registry, secret=QC_SECRET)
    again, round_two = restarted._next_round("sess-1", code)
    assert again == token and round_two == round_one + 1
    assert restarted.forget("sess-1", code) == (token,)
    assert restarted.store.max_round(token) == 0


def test_the_review_token_cannot_be_made_without_the_conversation_s_code_and_the_review_key(tmp_path, registry):
    code = "ABCD-EFGH-JKMN-PQRS-TVWX-YZ12-34"
    recorder = QCRecorder(QCStore(tmp_path / "q.db"), registry, secret=QC_SECRET)
    other_key = QCRecorder(QCStore(tmp_path / "q2.db"), registry, secret="z" * 40)
    assert recorder.token_for_code(code) != other_key.token_for_code(code)
    assert recorder.token_for_code(code) == recorder.token_for_code(code.replace("-", "").lower().upper())
    assert recorder.token_for_code(None) is None and QCRecorder(QCStore(tmp_path / "q3.db"), registry).token_for_code(code) is None


def test_a_review_key_that_was_rotated_still_finds_the_old_rows_to_delete(tmp_path, registry):
    code = "ABCD-EFGH-JKMN-PQRS-TVWX-YZ12-34"
    old = QCRecorder(QCStore(tmp_path / "q.db"), registry, secret=QC_SECRET)
    token, n = old._next_round("s", code)
    old.store.write_turn(conversation_token=token, round_no=n, world="fix", package_hash=None, model_id=None,
                         routing="x", flags={}, question_text=None, answer_text=None, marks={}, scores={}, day=date(2026, 10, 5))
    rotated = QCRecorder(QCStore(tmp_path / "q.db"), registry, secret="z" * 40, previous=(QC_SECRET,))
    assert token in rotated.forget("s", code) and rotated.store.max_round(token) == 0


def test_without_a_key_the_review_token_is_random_and_forget_is_best_effort(tmp_path, registry):
    recorder = QCRecorder(QCStore(tmp_path / "q.db"), registry)
    assert recorder.token_for_code("ABCD") is None
    token, round_no = recorder._next_round("sess-1")
    recorder.store.write_turn(conversation_token=token, round_no=round_no, world="fix", package_hash=None, model_id=None,
                              routing="x", flags={}, question_text=None, answer_text=None, marks={}, scores={}, day=date(2026, 10, 5))
    assert recorder.forget("sess-1") == (token,) and recorder.forget("never-seen") == ()


def test_the_review_copy_holds_no_session_id_or_account_value(http, accounts, mailer, qc, tmp_path):
    sign_in(http, mailer)
    session_id, auth = open_session(http)
    say(http, session_id, auth, "hello")
    context = accounts.service.admission_context(http.cookies.get(accounts.cookie_name))
    for row in qc.store.rows():
        assert session_id not in str(row) and context["account_id"] not in str(row)
    assert qc.token_for_code(code_of(auth)) in {r["conversation_token"] for r in qc.store.rows()}


def test_a_conversation_deleted_by_its_own_code_leaves_the_shelf_and_every_store(http, accounts, mailer, store, usage_store, feedback, qc, tmp_path):
    sign_in(http, mailer)
    session_id, auth = open_session(http)
    say(http, session_id, auth, "hello")
    assert http.delete(f"/api/session/{session_id}", headers=auth).status_code == 204
    deleted_everywhere(session_id, store, usage_store, feedback, qc, tmp_path, code_of(auth))
    assert http.get("/api/accounts/shelf").json()["conversations"] == []


def test_the_export_carries_the_shelf_and_not_the_review_copy(http, accounts, mailer):
    sign_in(http, mailer)
    session_id, auth = open_session(http)
    say(http, session_id, auth, "an exported question")
    stepped_up(http, accounts)
    body = http.post("/api/accounts/export", json={}, headers=H).json()
    assert [c["session_id"] for c in body["conversations"]] == [session_id]
    assert any("an exported question" in str(t) for t in body["conversations"][0]["transcript"])
    assert "conversation_token" not in str(body)


def test_the_shelf_has_a_limit(http, accounts, mailer):
    sign_in(http, mailer)
    accounts.service.limits = dataclasses.replace(accounts.service.limits, shelf_per_account=2)
    open_session(http)
    open_session(http)
    session_id, auth = open_session(http)
    assert len(http.get("/api/accounts/shelf").json()["conversations"]) == 2


def test_a_shelf_entry_whose_conversation_is_gone_drops_off_the_list(http, accounts, mailer, store):
    sign_in(http, mailer)
    session_id, auth = open_session(http)
    store.delete_session(session_id)
    assert http.get("/api/accounts/shelf").json()["conversations"] == []
    assert accounts.service.store._d.execute("SELECT COUNT(*) FROM shelf").fetchone()[0] == 0


def test_an_erased_conversation_that_comes_back_from_a_backup_is_erased_again(http, accounts, mailer, store, usage_store, feedback, qc, tmp_path):
    import shutil
    from engine.api.accounts_routes import reapply_erasures
    sign_in(http, mailer)
    session_id, auth = open_session(http)
    say(http, session_id, auth, "a question that will be deleted")
    shutil.copy(store.db_path, tmp_path / "events-backup.db")
    assert post(http, "shelf/delete", session_id=session_id).status_code == 200
    shutil.copy(tmp_path / "events-backup.db", store.db_path)  # a restore
    assert store.read_events(session_id)
    assert reapply_erasures(accounts) == 1
    assert store.read_events(session_id) == [] and reapply_erasures(accounts) == 0


def test_a_turn_that_was_in_flight_when_the_conversation_was_deleted_is_cleared_by_the_next_pass(http, accounts, mailer, store, qc):
    from engine.api.accounts_routes import reapply_erasures
    sign_in(http, mailer)
    session_id, auth = open_session(http)
    say(http, session_id, auth, "hello")
    post(http, "shelf/delete", session_id=session_id)
    store.append(session_id=session_id, event_uuid="late-event", event_type="participant_message", payload={"text": "late"})
    assert store.read_events(session_id)
    reapply_erasures(accounts)
    assert store.read_events(session_id) == []


def test_the_erasure_ledger_holds_a_keyed_hash_and_expires(http, accounts, mailer, tmp_path, clock=None):
    sign_in(http, mailer)
    session_id, auth = open_session(http)
    post(http, "shelf/delete", session_id=session_id)
    rows = accounts.service.store.erased_rows()
    assert len(rows) == 1 and session_id not in next(iter(rows))
    accounts.service._clock.advance(20 * 86400)
    accounts.service.purge()
    assert accounts.service.store.erased_rows() == {}


def test_turning_accounts_off_does_not_let_the_clearing_delete_what_people_saved(http, accounts, mailer, store, tmp_path):
    from engine.api.accounts_routes import shelf_exemption_from_file
    sign_in(http, mailer)
    shelved, _ = open_session(http)
    unshelved, _ = open_session(TestClient(http.app, base_url="https://testserver"))
    exempt = shelf_exemption_from_file(str(tmp_path / "d.db"))
    assert exempt(shelved) is True and exempt(unshelved) is False
    assert shelf_exemption_from_file(str(tmp_path / "none.db"))(shelved) is False
    removed = store.purge_inactive((datetime.now(timezone.utc) + timedelta(days=1)).isoformat(), exempt)
    assert removed == 1 and store.read_events(shelved)


def test_a_signed_in_person_is_told_whether_the_new_conversation_went_on_the_shelf(http, accounts, mailer):
    anonymous = http.post("/api/session", json={"world_key": "fix"}).json()
    assert anonymous["shelved"] is None
    sign_in(http, mailer)
    assert http.post("/api/session", json={"world_key": "fix"}).json()["shelved"] is True
    accounts.service.limits = dataclasses.replace(accounts.service.limits, shelf_per_account=1)
    assert http.post("/api/session", json={"world_key": "fix"}).json()["shelved"] is False


def test_a_code_sealed_under_an_older_shelf_key_is_sealed_again_when_it_is_reopened(store, usage_store, world_loader, registry, qc, feedback, tmp_path, mailer):
    store_a = AccountStore(str(tmp_path / "d.db"), str(tmp_path / "e.db"))
    old = AccountsService(store_a, KeyRing(ADDRESS_KEY, SESSION_KEY), mailer, clock=Clock(),
                          shelf_cipher=ContactCipher("h" * 40, key_id="s1", purpose="shelf"))
    from engine.accounts.tests.conftest import sign_in as svc_sign_in
    session = old.session(svc_sign_in(old, mailer, ADDR))
    old.shelf_add(session, "sess-1", "CODE-ONE")
    from engine.api.contact_cipher import PreviousContactKey
    rotated = AccountsService(store_a, KeyRing(ADDRESS_KEY, SESSION_KEY), mailer, clock=Clock(),
                              shelf_cipher=ContactCipher("g" * 40, key_id="s2", purpose="shelf",
                                                         previous=[PreviousContactKey("s1", "h" * 40)]))
    assert store_a.shelf_on_older_keys("s2") == 1
    assert rotated.shelf_open(session, "sess-1") == "CODE-ONE"
    assert store_a.shelf_on_older_keys("s2") == 0 and rotated.shelf_open(session, "sess-1") == "CODE-ONE"
    store_a.close()


def test_a_deletion_that_stops_part_way_leaves_the_account_and_a_retry_finishes_it(http, accounts, mailer, store, monkeypatch):
    sign_in(http, mailer)
    first, _ = open_session(http)
    second, _ = open_session(http)
    stepped_up(http, accounts)
    real = shelf.ConversationEraser.erase
    calls = {"n": 0}

    def flaky(self, session_id, code=None):
        calls["n"] += 1
        if calls["n"] == 2:
            raise RuntimeError("store unavailable")
        return real(self, session_id, code)

    monkeypatch.setattr(shelf.ConversationEraser, "erase", flaky)
    assert http.post("/api/accounts/delete", json={}, headers=H).status_code == 500
    assert accounts.service.store._d.execute("SELECT COUNT(*) FROM accounts").fetchone()[0] == 1
    assert http.post("/api/accounts/delete", json={}, headers=H).status_code == 200
    assert store.read_events(first) == [] and store.read_events(second) == []
    assert accounts.service.store._d.execute("SELECT COUNT(*) FROM accounts").fetchone()[0] == 0


def test_the_sweep_leaves_an_account_that_signed_in_while_it_ran(http, accounts, mailer, store, monkeypatch):
    from engine.api.accounts_routes import sweep_unused_accounts
    sign_in(http, mailer)
    open_session(http)
    accounts.service._clock.advance(365 * 86400 * 2 + 20 * 86400)
    real = accounts.service.stale_account_ids
    seen = {"n": 0}

    def once_then_none():
        seen["n"] += 1
        return real() if seen["n"] == 1 else []

    monkeypatch.setattr(accounts.service, "stale_account_ids", once_then_none)
    assert sweep_unused_accounts(accounts) == 0
    assert accounts.service.store._d.execute("SELECT COUNT(*) FROM accounts").fetchone()[0] == 1


def test_a_second_pass_keeps_the_review_tokens_so_a_later_restore_is_still_cleared(http, accounts, mailer, store, qc, tmp_path):
    from engine.api.accounts_routes import reapply_erasures
    sign_in(http, mailer)
    session_id, auth = open_session(http)
    say(http, session_id, auth, "a question")
    token = qc.token_for_code(code_of(auth))
    import sqlite3

    def snapshot(source, target):
        with sqlite3.connect(source) as src, sqlite3.connect(target) as dst:
            src.backup(dst)

    snapshot(store.db_path, tmp_path / "ev.bak")
    snapshot(qc.store.db_path, tmp_path / "qc.bak")
    post(http, "shelf/delete", session_id=session_id)
    for _ in range(2):  # restored twice, as a backup restored then restored again
        snapshot(tmp_path / "ev.bak", store.db_path)
        snapshot(tmp_path / "qc.bak", qc.store.db_path)
        assert qc.store.max_round(token) >= 1
        assert reapply_erasures(accounts) == 1
        assert store.read_events(session_id) == [] and qc.store.max_round(token) == 0


def test_an_unreadable_account_file_never_lets_the_clearing_delete_a_conversation(tmp_path):
    from engine.api.accounts_routes import shelf_exemption_from_file
    broken = tmp_path / "broken.db"
    broken.write_bytes(b"this is not a database file")
    assert shelf_exemption_from_file(str(broken))("any-session") is True


def test_an_account_is_kept_if_a_conversation_is_shelved_while_it_is_being_cleared(http, accounts, mailer, store, monkeypatch):
    sign_in(http, mailer)
    first, _ = open_session(http)
    stepped_up(http, accounts)
    real = shelf.ConversationEraser.erase

    def shelve_one_more(self, session_id, code=None, known_tokens=()):
        late = TestClient(http.app, base_url="https://testserver")
        late.cookies.set(accounts.cookie_name, http.cookies.get(accounts.cookie_name))
        for _ in range(3):
            open_session(late)
        return real(self, session_id, code, known_tokens)

    monkeypatch.setattr(shelf.ConversationEraser, "erase", shelve_one_more)
    assert http.post("/api/accounts/delete", json={}, headers=H).status_code == 500
    assert accounts.service.store._d.execute("SELECT COUNT(*) FROM accounts").fetchone()[0] == 1
