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


def deleted_everywhere(session_id, store, usage_store, feedback, qc, tmp_path):
    assert store.read_events(session_id) == []
    assert all(r.session_id != session_id for r in usage_store.read_all())
    assert feedback.like_exists(session_id, 1) is False
    assert qc.store.rows() == [] or all(r["conversation_token"] != qc.token_for(session_id) for r in qc.store.rows())


def test_deleting_one_conversation_removes_it_from_every_store_and_the_shelf(http, accounts, mailer, store, usage_store, feedback, qc, tmp_path):
    sign_in(http, mailer)
    session_id, auth = open_session(http)
    say(http, session_id, auth, "hello")
    feedback.add({"kind": "like", "page": "p", "session_id": session_id, "turn_index": 1})
    assert qc.store.max_round(qc.token_for(session_id)) >= 1
    other_id, other_auth = open_session(http)
    say(http, other_id, other_auth, "keep this one")
    assert post(http, "shelf/delete", session_id=session_id).status_code == 200
    deleted_everywhere(session_id, store, usage_store, feedback, qc, tmp_path)
    assert qc.store.max_round(qc.token_for(session_id)) == 0 and qc.store.max_round(qc.token_for(other_id)) >= 1
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
    ids = []
    for text in ("first question", "second question"):
        session_id, auth = open_session(http)
        say(http, session_id, auth, text)
        feedback.add({"kind": "like", "page": "p", "session_id": session_id, "turn_index": 1})
        ids.append(session_id)
    tokens = [qc.token_for(i) for i in ids]
    stepped_up(http, accounts)
    assert http.post("/api/accounts/delete", json={}, headers=H).status_code == 200
    for session_id in ids:
        deleted_everywhere(session_id, store, usage_store, feedback, qc, tmp_path)
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
    first = QCRecorder(QCStore(tmp_path / "q.db"), registry, secret=QC_SECRET)
    token, round_one = first._next_round("sess-1")
    first.store.write_turn(conversation_token=token, round_no=round_one, world="fix", package_hash=None, model_id=None,
                           routing="x", flags={}, question_text=None, answer_text=None, marks={}, scores={}, day=date(2026, 10, 5))
    restarted = QCRecorder(QCStore(tmp_path / "q.db"), registry, secret=QC_SECRET)
    again, round_two = restarted._next_round("sess-1")
    assert again == token and round_two == round_one + 1
    assert restarted.forget("sess-1") == 1
    assert restarted.store.max_round(token) == 0


def test_without_a_secret_the_review_token_is_random_and_forget_is_best_effort(tmp_path, registry):
    recorder = QCRecorder(QCStore(tmp_path / "q.db"), registry)
    assert recorder.token_for("sess-1") is None
    token, round_no = recorder._next_round("sess-1")
    recorder.store.write_turn(conversation_token=token, round_no=round_no, world="fix", package_hash=None, model_id=None,
                              routing="x", flags={}, question_text=None, answer_text=None, marks={}, scores={}, day=date(2026, 10, 5))
    assert recorder.forget("sess-1") == 1 and recorder.forget("never-seen") == 0


def test_the_review_copy_holds_no_session_id_or_account_value(http, accounts, mailer, qc, tmp_path):
    sign_in(http, mailer)
    session_id, auth = open_session(http)
    say(http, session_id, auth, "hello")
    context = accounts.service.admission_context(http.cookies.get(accounts.cookie_name))
    for row in qc.store.rows():
        assert session_id not in str(row) and context["account_id"] not in str(row)
    assert qc.token_for(session_id) in {r["conversation_token"] for r in qc.store.rows()}


def test_a_conversation_deleted_by_its_own_code_leaves_the_shelf_and_every_store(http, accounts, mailer, store, usage_store, feedback, qc, tmp_path):
    sign_in(http, mailer)
    session_id, auth = open_session(http)
    say(http, session_id, auth, "hello")
    assert http.delete(f"/api/session/{session_id}", headers=auth).status_code == 204
    deleted_everywhere(session_id, store, usage_store, feedback, qc, tmp_path)
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
