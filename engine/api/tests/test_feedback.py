"""Feedback endpoints: a like or flag on one reply (the session's own code), a
comment, a page like or a page report from the app or the site (CORS against
the site origin), and the operator's queue (admin credential)."""
import sqlite3
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
        r27_enforce=False, self_revision_enabled=True,
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


OLD_TABLE = """
CREATE TABLE feedback (
  id TEXT PRIMARY KEY,
  kind TEXT NOT NULL CHECK (kind IN ('like', 'flag', 'comment')),
  created_at TEXT NOT NULL,
  page TEXT,
  session_id TEXT,
  turn_index INTEGER,
  sentence_index INTEGER,
  record_ids TEXT NOT NULL DEFAULT '[]',
  confidence TEXT,
  reason TEXT CHECK (reason IS NULL OR reason IN ('fact_wrong', 'source_mismatch', 'overcertain', 'unclear')),
  text TEXT,
  quote_consent TEXT CHECK (quote_consent IS NULL OR quote_consent IN ('no', 'anonymous', 'first_name')),
  first_name TEXT,
  email TEXT,
  outcome TEXT CHECK (outcome IS NULL OR outcome IN ('corrected', 'checked_stands', 'open_lead', 'conviction', 'no_action')),
  outcome_note TEXT,
  closed_at TEXT
);
CREATE INDEX feedback_like_idx ON feedback (session_id, turn_index) WHERE kind = 'like';
"""


def _report(page="tree/donatism", reason="accuracy", text="The date looks wrong.", **extra):
    return {"kind": "report", "page": page, "reason": reason, "text": text, **extra}


def test_page_like_is_stored_with_no_text_reason_email_or_session(http, feedback):
    resp = http.post("/api/feedback", json={"kind": "like", "page": "tree/donatism"}, headers={"Origin": SITE})
    assert resp.status_code == 201 and resp.headers["access-control-allow-origin"] == SITE
    item = feedback.get(resp.json()["id"])
    assert item["kind"] == "like" and item["page"] == "tree/donatism"
    for field in ("text", "reason", "email", "session_id", "turn_index", "sentence_index", "first_name", "quote_consent"):
        assert item[field] is None
    assert item["record_ids"] == []


def test_page_like_ignores_extra_fields_and_can_repeat(http, feedback):
    body = {"kind": "like", "page": "atlas", "text": "hello", "email": "a@b.org", "reason": "craft"}
    assert http.post("/api/feedback", json=body).status_code == 201
    assert http.post("/api/feedback", json=body).status_code == 201
    with sqlite3.connect(feedback.db_path) as conn:
        rows = conn.execute("SELECT text, reason, email FROM feedback WHERE kind = 'like'").fetchall()
    assert rows == [(None, None, None)] * 2


def test_page_report_is_stored_with_reason_text_and_email(http, feedback):
    resp = http.post("/api/feedback", json=_report(text="  Wrong century.  ", reason="craft", email=" a@b.org "), headers={"Origin": SITE})
    assert resp.status_code == 201 and resp.headers["access-control-allow-origin"] == SITE
    item = feedback.get(resp.json()["id"])
    assert (item["kind"], item["page"], item["reason"], item["text"], item["email"]) == ("report", "tree/donatism", "craft", "Wrong century.", "a@b.org")
    assert item["session_id"] is None and item["turn_index"] is None and item["record_ids"] == []


def test_page_report_email_is_optional_and_blank_is_dropped(http, feedback):
    assert http.post("/api/feedback", json=_report()).status_code == 201
    assert http.post("/api/feedback", json=_report(email="   ")).status_code == 201
    assert [i["email"] for i in feedback.list_open()] == [None, None]


@pytest.mark.parametrize("body", [
    {"kind": "report", "page": "p", "text": "t"},
    {"kind": "report", "page": "p", "reason": "unclear", "text": "t"},
    {"kind": "report", "page": "p", "reason": "fact_wrong", "text": "t"},
    {"kind": "report", "page": "p", "reason": None, "text": "t"},
    {"kind": "report", "page": "p", "reason": "accuracy"},
    {"kind": "report", "page": "p", "reason": "accuracy", "text": ""},
    {"kind": "report", "page": "p", "reason": "accuracy", "text": "   "},
    {"kind": "report", "page": "p", "reason": "accuracy", "text": "x" * 601},
    {"kind": "report", "page": "p", "reason": "accuracy", "text": "t", "email": "x" * 201},
    {"kind": "report", "reason": "accuracy", "text": "t"},
])
def test_page_report_validation(http, feedback, body):
    assert http.post("/api/feedback", json=body).status_code == 422
    assert feedback.list_open() == []


@pytest.mark.parametrize("page", ["", "x" * 121, "tree/don atism", "tree/donatism?x=1", "a#b", "tree\\x", "tr\u00e9e", "<b>", "a,b", "a+b", "tree/x\n"])
@pytest.mark.parametrize("make", [lambda page: {"kind": "like", "page": page}, lambda page: _report(page=page)])
def test_page_id_charset_and_length_are_enforced(http, feedback, page, make):
    assert http.post("/api/feedback", json=make(page)).status_code == 422
    with sqlite3.connect(feedback.db_path) as conn:
        assert conn.execute("SELECT COUNT(*) FROM feedback").fetchone()[0] == 0


@pytest.mark.parametrize("page", ["tree/donatism", "atlas-v3", "conversation:donatism", "table:alx-syr", "table", "a.b_c-d/e:f", "x" * 120])
def test_page_ids_in_the_allowed_set_are_accepted(http, page):
    assert http.post("/api/feedback", json={"kind": "like", "page": page}).status_code == 201
    assert http.post("/api/feedback", json=_report(page=page)).status_code == 201


def test_other_kinds_are_refused_and_a_missing_kind_is_a_comment(http, feedback):
    assert http.post("/api/feedback", json={"kind": "flag", "page": "p", "text": "t"}).status_code == 422
    assert http.post("/api/feedback", json={"kind": "bogus", "page": "p"}).status_code == 422
    assert http.post("/api/feedback", json=["like"]).status_code == 422
    assert feedback.list_open() == []
    assert http.post("/api/feedback", json={"page": "p", "text": "t"}).status_code == 201
    assert feedback.list_open()[0]["kind"] == "comment"


def test_comment_with_old_page_text_is_unchanged_by_the_page_id_rules(http, feedback):
    assert http.post("/api/feedback", json={"page": "my page (1).html", "text": "t"}).status_code == 201
    assert feedback.list_open()[0]["page"] == "my page (1).html"


def test_preflight_still_answers_for_the_new_kinds(http):
    pre = http.options("/api/feedback", headers={"Origin": SITE, "Access-Control-Request-Method": "POST"})
    assert pre.status_code == 204 and pre.headers["access-control-allow-origin"] == SITE
    assert pre.headers["access-control-allow-headers"] == "content-type"


def test_page_likes_and_reports_share_the_feedback_rate_limit(store, usage_store, world_loader, registry, feedback):
    http = _http(store, usage_store, world_loader, registry, feedback, rate_limit=True)
    codes = [http.post("/api/feedback", json={"kind": "like", "page": "atlas"}).status_code for _ in range(15)]
    codes += [http.post("/api/feedback", json=_report()).status_code for _ in range(10)]
    assert codes[:20] == [201] * 20 and set(codes[20:]) == {429}


def test_admin_list_shows_a_report_and_never_a_page_like(http, feedback):
    like = http.post("/api/feedback", json={"kind": "like", "page": "tree/donatism"}).json()["id"]
    report = http.post("/api/feedback", json=_report(reason="craft", email="a@b.org")).json()["id"]
    listed = http.get("/api/admin/feedback", headers=ADMIN).json()["items"]
    assert [i["id"] for i in listed] == [report] and like not in [i["id"] for i in listed]
    assert listed[0]["page"] == "tree/donatism" and listed[0]["reason"] == "craft" and listed[0]["turn_index"] is None
    assert http.get("/api/admin/feedback?status=closed", headers=ADMIN).json() == {"items": []}


def test_closing_a_report_clears_the_email_and_files_it_as_closed(http, feedback):
    report = http.post("/api/feedback", json=_report(email="a@b.org")).json()["id"]
    closed = http.post(f"/api/admin/feedback/{report}/close", headers=ADMIN, json={"outcome": "corrected", "note": "fixed"})
    assert closed.status_code == 200 and closed.json()["email"] is None and closed.json()["reason"] == "accuracy"
    assert [i["id"] for i in http.get("/api/admin/feedback?status=closed", headers=ADMIN).json()["items"]] == [report]
    assert http.get("/api/admin/feedback", headers=ADMIN).json() == {"items": []}


def test_retention_pass_purges_old_page_likes_and_closed_reports(tmp_path, feedback, store):
    now = datetime(2026, 10, 16, tzinfo=timezone.utc)
    old_like = feedback.add({"kind": "like", "page": "atlas"})
    closed_report = feedback.add({"kind": "report", "page": "atlas", "reason": "craft", "text": "t"})
    open_report = feedback.add({"kind": "report", "page": "atlas", "reason": "accuracy", "text": "t"})
    fresh_like = feedback.add({"kind": "like", "page": "atlas"})
    feedback.close(closed_report, "no_action", None)
    old, recent = (now - timedelta(days=91)).isoformat(), (now - timedelta(days=5)).isoformat()
    with sqlite3.connect(feedback.db_path) as conn:
        conn.execute("UPDATE feedback SET created_at = ?, closed_at = ?", (old, None))
        conn.execute("UPDATE feedback SET closed_at = ? WHERE id = ?", (old, closed_report))
        conn.execute("UPDATE feedback SET created_at = ? WHERE id = ?", (recent, fresh_like))
    qc = QCStore(tmp_path / "qc.db")
    status = retention.run_once(store.db_path, qc.db_path, tmp_path / "status", now=now, feedback_store=feedback)
    assert status["feedback_purged"] == 2
    assert feedback.get(old_like) is None and feedback.get(closed_report) is None
    assert feedback.get(open_report) is not None and feedback.get(fresh_like) is not None


def _old_database(path):
    with sqlite3.connect(path) as conn:
        conn.executescript(OLD_TABLE)
        conn.execute(
            "INSERT INTO feedback (id, kind, created_at, page, session_id, turn_index, record_ids, reason, text, email) VALUES "
            "('a', 'flag', 'day-1', 'fix', 's1', 2, '[\"r.one\"]', 'unclear', 'old flag', 'x@y.org')"
        )
        conn.execute("INSERT INTO feedback (id, kind, created_at, session_id, turn_index) VALUES ('b', 'like', 'day-1', 's1', 2)")
        conn.execute("INSERT INTO feedback (id, kind, created_at, page, text, quote_consent) VALUES ('c', 'comment', 'day-2', 'p', 'old comment', 'anonymous')")
        conn.execute("UPDATE feedback SET outcome = 'corrected', closed_at = 'day-3', email = NULL WHERE id = 'c'")


def test_an_older_database_is_rebuilt_with_every_row_and_index_kept(tmp_path):
    path = tmp_path / "old.db"
    _old_database(path)
    store = FeedbackStore(path)
    flag = store.get("a")
    assert flag["kind"] == "flag" and flag["record_ids"] == ["r.one"] and flag["email"] == "x@y.org" and flag["turn_index"] == 2
    assert store.like_exists("s1", 2) and store.get("c")["outcome"] == "corrected" and store.get("c")["quote_consent"] == "anonymous"
    assert [i["id"] for i in store.list_open()] == ["a"] and [i["id"] for i in store.list_closed()] == ["c"]
    report = store.add({"kind": "report", "page": "atlas", "reason": "craft", "text": "t"})
    assert store.get(report)["reason"] == "craft"
    with sqlite3.connect(path) as conn:
        assert conn.execute("SELECT name FROM sqlite_master WHERE type = 'index' AND name = 'feedback_like_idx'").fetchone()
        assert conn.execute("SELECT name FROM sqlite_master WHERE name = 'feedback_rebuilt'").fetchone() is None
        with pytest.raises(sqlite3.IntegrityError):
            conn.execute("INSERT INTO feedback (id, kind, created_at, reason) VALUES ('z', 'comment', 'now', 'bogus')")


def test_the_rebuild_is_idempotent_and_leaves_a_current_database_alone(tmp_path):
    path = tmp_path / "old.db"
    _old_database(path)
    FeedbackStore(path)
    with sqlite3.connect(path) as conn:
        before = conn.execute("SELECT sql FROM sqlite_master WHERE name = 'feedback'").fetchone()
    again = FeedbackStore(path)
    with sqlite3.connect(path) as conn:
        assert conn.execute("SELECT sql FROM sqlite_master WHERE name = 'feedback'").fetchone() == before
        assert conn.execute("SELECT COUNT(*) FROM feedback").fetchone()[0] == 3
    assert again.get("a") is not None


def test_a_failed_rebuild_leaves_the_old_table_untouched(tmp_path, monkeypatch):
    from engine.feedback import store as store_module
    path = tmp_path / "old.db"
    _old_database(path)
    monkeypatch.setattr(store_module, "_COLUMNS", store_module._COLUMNS + ("missing_column",))
    with pytest.raises(sqlite3.OperationalError):
        FeedbackStore(path)
    monkeypatch.undo()
    with sqlite3.connect(path) as conn:
        assert conn.execute("SELECT COUNT(*) FROM feedback").fetchone()[0] == 3
        assert "'report'" not in conn.execute("SELECT sql FROM sqlite_master WHERE name = 'feedback'").fetchone()[0]
        assert conn.execute("SELECT name FROM sqlite_master WHERE name = 'feedback_rebuilt'").fetchone() is None
    assert FeedbackStore(path).get("a") is not None
