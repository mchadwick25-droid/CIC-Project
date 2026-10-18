"""Feedback endpoints: a like or flag on one reply (the session's own code), a
comment from the app or the site (CORS against the site origin), and the
operator's queue (admin credential)."""
from datetime import datetime, timedelta, timezone

import pytest
from fastapi.testclient import TestClient

from engine.api import db_backup
from engine.api.app import backup_extra_dbs, create_app
from engine.api.config import Settings
from engine.api.feedback_routes import sentence_basis
from engine.api.tests.conftest import FakeBedrockClient, reader_response, safety_response
from engine.feedback.store import FeedbackStore
from engine.m7 import retention
from engine.m7.qc_store import QCStore

SITE = "https://site.example"
ADMIN = {"Authorization": "Bearer " + "t" * 40}
REPLY = "We did not claim to have seen him ourselves [[fix.witness.who-is-jesus]]."


def _http(store, usage_store, world_loader, registry, feedback_store, **extra):
    client = FakeBedrockClient(safety_response=safety_response("NO_SIGNAL"), reader_response=reader_response(), stream_chunks=[REPLY])
    return TestClient(create_app(
        voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
        store=store, usage_store=usage_store, world_loader=world_loader, registry=registry,
        default_world_key="fix", feedback_store=feedback_store, site_origin=SITE, admin_token="t" * 40, **extra,
    ))


@pytest.fixture
def feedback(tmp_path):
    return FeedbackStore(tmp_path / "feedback.db")


@pytest.fixture
def http(store, usage_store, world_loader, registry, feedback):
    return _http(store, usage_store, world_loader, registry, feedback)


def _conversation(http):
    created = http.post("/api/session", json={"world_key": "fix"}).json()
    sid, auth = created["session_id"], {"Authorization": f"Session {created['session_code']}"}
    assert http.post(f"/api/session/{sid}/message", headers=auth, json={"text": "who was Jesus"}).status_code == 200
    transcript = http.get(f"/api/session/{sid}/transcript", headers=auth).json()["transcript"]
    voice = next(i for i, t in enumerate(transcript) if "citations" in t)
    return sid, auth, voice


def test_flag_needs_the_sessions_own_code(http, feedback):
    sid, auth, turn = _conversation(http)
    body = {"kind": "flag", "turn_index": turn, "sentence_index": 0, "reason": "fact_wrong"}
    assert http.post(f"/api/session/{sid}/feedback", json=body).status_code == 401
    assert http.post(f"/api/session/{sid}/feedback", json=body, headers={"Authorization": "Session wrong"}).status_code == 401
    assert http.post(f"/api/session/{sid}/feedback", json={"kind": "like", "turn_index": turn}).status_code == 401
    assert feedback.list_open() == []


def test_flag_derives_record_ids_and_keeps_no_reply_text(http, feedback):
    sid, auth, turn = _conversation(http)
    resp = http.post(f"/api/session/{sid}/feedback", headers=auth, json={
        "kind": "flag", "turn_index": turn, "sentence_index": 0, "reason": "source_mismatch", "text": "  it does not say that ", "email": "a@b.org",
    })
    assert resp.status_code == 201
    [item] = feedback.list_open()
    assert item["id"] == resp.json()["id"] and item["kind"] == "flag" and item["page"] == "fix"
    assert "fix.witness.who-is-jesus" in item["record_ids"]
    assert item["session_id"] == sid and item["turn_index"] == turn and item["sentence_index"] == 0
    assert item["reason"] == "source_mismatch" and item["text"] == "it does not say that" and item["email"] == "a@b.org"
    assert "did not claim" not in repr(item)


def test_flag_refuses_a_non_voice_turn_a_missing_reason_and_a_bad_sentence(http, feedback):
    sid, auth, turn = _conversation(http)
    url = f"/api/session/{sid}/feedback"
    participant = 0
    assert http.post(url, headers=auth, json={"kind": "flag", "turn_index": participant, "reason": "unclear"}).status_code == 400
    assert http.post(url, headers=auth, json={"kind": "flag", "turn_index": 99, "reason": "unclear"}).status_code == 400
    assert http.post(url, headers=auth, json={"kind": "flag", "turn_index": turn, "sentence_index": 0}).status_code == 400
    assert http.post(url, headers=auth, json={"kind": "flag", "turn_index": turn, "sentence_index": 99, "reason": "unclear"}).status_code == 400
    assert http.post(url, headers=auth, json={"kind": "flag", "turn_index": turn, "reason": "sounds_off"}).status_code == 422
    assert http.post(url, headers=auth, json={"kind": "flag", "turn_index": turn, "reason": "unclear", "text": "x" * 601}).status_code == 422
    assert feedback.list_open() == []


def test_flag_without_a_sentence_uses_every_record_the_turn_cites(http, feedback):
    sid, auth, turn = _conversation(http)
    assert http.post(f"/api/session/{sid}/feedback", headers=auth, json={"kind": "flag", "turn_index": turn, "reason": "unclear"}).status_code == 201
    [item] = feedback.list_open()
    assert item["sentence_index"] is None and "fix.witness.who-is-jesus" in item["record_ids"]


def test_a_repeated_like_does_not_duplicate(http, feedback, tmp_path):
    sid, auth, turn = _conversation(http)
    first = http.post(f"/api/session/{sid}/feedback", headers=auth, json={"kind": "like", "turn_index": turn})
    second = http.post(f"/api/session/{sid}/feedback", headers=auth, json={"kind": "like", "turn_index": turn})
    assert first.status_code == 201 and second.status_code == 200 and first.json() == second.json()
    assert feedback.like_exists(sid, turn) and not feedback.like_exists(sid, turn + 1)
    import sqlite3
    with sqlite3.connect(feedback.db_path) as conn:
        assert conn.execute("SELECT COUNT(*) FROM feedback WHERE kind = 'like'").fetchone()[0] == 1
        row = conn.execute("SELECT page, record_ids, text, email FROM feedback WHERE kind = 'like'").fetchone()
    assert row[0] == "fix" and "fix.witness.who-is-jesus" in row[1] and row[2] is None and row[3] is None
    assert feedback.list_open() == []


def test_sentence_basis_uses_plan_elements_then_citations_in_the_span():
    turn = {
        "text": "First sentence. Second sentence here.",
        "citations": [
            {"sentence": "First sentence.", "record_ids": ["a.quote.one"], "sources": []},
            {"sentence": "Second sentence here.", "record_ids": ["a.witness.two"], "sources": []},
        ],
        "transparency": {
            "sentences": [{"index": 0, "text_start": 0, "text_end": 15}, {"index": 1, "text_start": 16, "text_end": 37}],
            "elements": [{"record_id": "a.quote.one", "sentence_index": 0, "confidence": {"level": "Documented"}}],
            "references": [{"record_id": "a.witness.two", "confidence": {"level": "Contested"}}],
        },
    }
    assert sentence_basis(turn, 0) == (["a.quote.one"], {"a.quote.one": {"level": "Documented"}})
    assert sentence_basis(turn, 1) == (["a.witness.two"], {"a.witness.two": {"level": "Contested"}})
    ids, confidence = sentence_basis(turn, None)
    assert ids == ["a.quote.one", "a.witness.two"] and set(confidence) == set(ids)


def test_comment_from_the_site_origin_gets_the_cors_header(http, feedback):
    body = {"page": "index.html", "text": "Thank you", "quote_consent": "first_name", "first_name": " Ana ", "email": "x@y.org"}
    ok = http.post("/api/feedback", json=body, headers={"Origin": SITE})
    assert ok.status_code == 201 and ok.headers["access-control-allow-origin"] == SITE
    other = http.post("/api/feedback", json=body, headers={"Origin": "https://elsewhere.example"})
    assert other.status_code == 201 and "access-control-allow-origin" not in other.headers
    pre = http.options("/api/feedback", headers={"Origin": SITE})
    assert pre.status_code == 204 and pre.headers["access-control-allow-origin"] == SITE and pre.headers["access-control-allow-methods"] == "POST"
    assert "access-control-allow-origin" not in http.options("/api/feedback", headers={"Origin": "https://elsewhere.example"}).headers
    [first, _] = feedback.list_open()
    assert first["kind"] == "comment" and first["page"] == "index.html" and first["first_name"] == "Ana" and first["session_id"] is None


def test_comment_keeps_a_first_name_only_with_that_consent_and_defaults_to_no(http, feedback):
    http.post("/api/feedback", json={"page": "p", "text": "t", "first_name": "Ana"})
    [item] = feedback.list_open()
    assert item["quote_consent"] == "no" and item["first_name"] is None


@pytest.mark.parametrize("body", [
    {"page": "p"}, {"text": "t"}, {"page": "p", "text": ""}, {"page": "p", "text": "x" * 2001}, {"page": "x" * 81, "text": "t"},
    {"page": "p", "text": "t", "quote_consent": "yes"}, {"page": "p", "text": "t", "first_name": "x" * 61},
    {"page": "p", "text": "t", "email": "x" * 201}, {"page": "p", "text": "   "}, {"page": "  ", "text": "t"},
])
def test_comment_validation(http, feedback, body):
    assert http.post("/api/feedback", json=body).status_code == 422
    assert feedback.list_open() == []


def test_comment_at_the_limits_is_accepted(http):
    assert http.post("/api/feedback", json={"page": "x" * 80, "text": "y" * 2000, "first_name": "n" * 60, "email": "e" * 200}).status_code == 201


def test_admin_queue_needs_the_admin_credential(http, feedback):
    item = http.post("/api/feedback", json={"page": "p", "text": "t"}).json()["id"]
    for path, call in (("/api/admin/feedback", http.get), (f"/api/admin/feedback/{item}/close", http.post)):
        kwargs = {"json": {"outcome": "no_action"}} if call == http.post else {}
        assert call(path, **kwargs).status_code == 404
        assert call(path, headers={"Authorization": "Bearer wrong"}, **kwargs).status_code == 404
    assert feedback.list_open()[0]["closed_at"] is None


def test_admin_close_clears_the_email_and_moves_the_item_to_closed(http, feedback):
    item = http.post("/api/feedback", json={"page": "p", "text": "t", "email": "x@y.org", "quote_consent": "first_name", "first_name": "Ana"}).json()["id"]
    listed = http.get("/api/admin/feedback", headers=ADMIN).json()["items"]
    assert [i["id"] for i in listed] == [item] and listed[0]["email"] == "x@y.org"
    assert http.get("/api/admin/feedback?status=closed", headers=ADMIN).json() == {"items": []}
    assert http.get("/api/admin/feedback?status=other", headers=ADMIN).status_code == 422

    closed = http.post(f"/api/admin/feedback/{item}/close", headers=ADMIN, json={"outcome": "corrected", "note": "fixed"})
    assert closed.status_code == 200
    body = closed.json()
    assert body["email"] is None and body["first_name"] == "Ana" and body["closed_at"] and body["outcome"] == "corrected" and body["outcome_note"] == "fixed"
    assert http.get("/api/admin/feedback", headers=ADMIN).json() == {"items": []}
    assert [i["id"] for i in http.get("/api/admin/feedback?status=closed", headers=ADMIN).json()["items"]] == [item]


def test_admin_close_rejects_a_bad_outcome_and_an_unknown_id(http):
    item = http.post("/api/feedback", json={"page": "p", "text": "t"}).json()["id"]
    assert http.post(f"/api/admin/feedback/{item}/close", headers=ADMIN, json={"outcome": "deleted"}).status_code == 400
    assert http.post("/api/admin/feedback/nope/close", headers=ADMIN, json={"outcome": "no_action"}).status_code == 404
    assert http.post(f"/api/admin/feedback/{item}/close", headers=ADMIN, json={"outcome": "no_action"}).status_code == 200
    assert http.post(f"/api/admin/feedback/{item}/close", headers=ADMIN, json={"outcome": "no_action"}).status_code == 404


def test_admin_cookie_also_opens_the_queue(http):
    from engine.api import admin_auth
    token = admin_auth.issue_session_token("t" * 40)
    http.cookies.set(admin_auth.SESSION_COOKIE_NAME, token)
    resp = http.get("/api/admin/feedback")
    assert resp.status_code == 200


def test_without_a_feedback_store_every_route_is_404(store, usage_store, world_loader, registry):
    http = _http(store, usage_store, world_loader, registry, None)
    sid, auth, turn = _conversation(http)
    assert http.post(f"/api/session/{sid}/feedback", headers=auth, json={"kind": "like", "turn_index": turn}).status_code == 404
    assert http.post("/api/feedback", json={"page": "p", "text": "t"}).status_code == 404
    assert http.options("/api/feedback", headers={"Origin": SITE}).status_code == 404
    assert http.get("/api/admin/feedback", headers=ADMIN).status_code == 404
    assert http.post("/api/admin/feedback/x/close", headers=ADMIN, json={"outcome": "no_action"}).status_code == 404


def test_feedback_posts_are_rate_limited(store, usage_store, world_loader, registry, feedback):
    http = _http(store, usage_store, world_loader, registry, feedback, rate_limit=True)
    codes = [http.post("/api/feedback", json={"page": "p", "text": "t"}).status_code for _ in range(25)]
    assert codes[:20] == [201] * 20 and 429 in codes[20:]


def test_retention_pass_purges_closed_feedback_older_than_ninety_days(tmp_path, feedback, store):
    now = datetime(2026, 10, 16, tzinfo=timezone.utc)
    old = feedback.add({"kind": "comment", "page": "p", "text": "old"})
    fresh = feedback.add({"kind": "comment", "page": "p", "text": "fresh"})
    open_one = feedback.add({"kind": "comment", "page": "p", "text": "open"})
    feedback.close(old, "no_action", None)
    feedback.close(fresh, "no_action", None)
    import sqlite3
    with sqlite3.connect(feedback.db_path) as conn:
        conn.execute("UPDATE feedback SET closed_at = ? WHERE id = ?", ((now - timedelta(days=91)).isoformat(), old))
        conn.execute("UPDATE feedback SET created_at = ?", ((now - timedelta(days=200)).isoformat(),))
    qc = QCStore(tmp_path / "qc.db")
    status = retention.run_once(store.db_path, qc.db_path, tmp_path / "status", now=now, feedback_store=feedback)
    assert status["outcome"] == "ok" and status["feedback_purged"] == 1
    assert feedback.get(old) is None and feedback.get(fresh) is not None and feedback.get(open_one) is not None


def test_backup_includes_the_feedback_database(tmp_path, feedback, monkeypatch):
    settings = Settings(
        region="r", voice_model_pattern="v", safety_model_pattern="s", events_db_path="e", usage_db_path="u",
        worlds_yaml_path=tmp_path, default_world_key="fix", enforce_admission=False, admin_token=None,
        world_idle_unload_seconds=None, package_cache_dir=tmp_path, anon_cap_enabled=False, anon_visitor_secret=None,
        anon_daily_session_limit=5, anon_daily_turn_limit=150, r27_enforce=False, self_revision_enabled=True,
        citation_attach_enabled=False, qc_db_path="q", streaming_enabled=False, feedback_db_path=feedback.db_path, site_origin=None,
    )
    assert backup_extra_dbs(settings, None) == {"feedback": feedback.db_path}
    assert backup_extra_dbs(settings, "m.db") == {"feedback": feedback.db_path, "meter": "m.db"}
    feedback.add({"kind": "comment", "page": "p", "text": "t"})
    monkeypatch.setattr(db_backup, "is_configured", lambda: False)
    from engine.m4.store import Store
    from engine.m8.log_store import UsageLogStore
    Store(tmp_path / "e.db"), UsageLogStore(tmp_path / "u.db")
    status = db_backup.run_backup_once(str(tmp_path / "e.db"), str(tmp_path / "u.db"), tmp_path / "stage", extra_dbs=backup_extra_dbs(settings, None))
    assert status["results"]["feedback"]["outcome"] != "skipped"


def test_settings_read_the_feedback_paths(monkeypatch):
    monkeypatch.setenv("CIC_API_REGION", "r")
    for name in ("CIC_API_FEEDBACK_DB", "CIC_API_SITE_ORIGIN", "CIC_DEEPER_SITE_ORIGIN"):
        monkeypatch.delenv(name, raising=False)
    settings = Settings.from_env()
    assert settings.feedback_db_path == "./cic_api_feedback.db" and settings.site_origin is None
    monkeypatch.setenv("CIC_DEEPER_SITE_ORIGIN", "https://a.example")
    assert Settings.from_env().site_origin == "https://a.example"
    monkeypatch.setenv("CIC_API_SITE_ORIGIN", "https://b.example")
    assert Settings.from_env().site_origin == "https://b.example"
