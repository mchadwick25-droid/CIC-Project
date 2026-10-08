"""wiring.get_usage_summary and /api/admin/usage-summary: the usage
dashboard's one aggregate. Sessions are
opened via engine.m4.entrance.open_session directly, not
wiring.create_session/table_wiring.create_table_session - this suite
never needs a compiled world package, only the event log those two
functions write to (same reasoning test_admin.py's idle-session test
already follows)."""
import json
import uuid

import pytest
from fastapi.testclient import TestClient

from engine.api.app import create_app
from engine.api.tests.test_table_api import _table_client
from engine.api.wiring import get_usage_summary
from engine.m4.entrance import open_session
from engine.m8.usage import NormalizedUsage, UsageRecord


def _open(store, *, world_key="fix", visitor_id=None):
    session_id = str(uuid.uuid4())
    open_session(
        store, session_id=session_id, event_uuid=str(uuid.uuid4()), mode="interview", frame=None,
        code_hash="h", world_key=world_key, package_manifest_hash="m", visitor_id=visitor_id,
    )
    return session_id


def _touch(store, session_id, text="hi"):
    """A second event, so first_at != last_at and duration is > 0."""
    store.append(
        session_id=session_id, event_uuid=str(uuid.uuid4()), event_type="participant_message",
        payload={"text": text, "client_msg_id": str(uuid.uuid4())},
    )


def test_no_sessions_returns_zeros_not_errors(store, usage_store):
    summary = get_usage_summary(store, usage_store)
    assert summary.visitors.unique_visitors == 0
    assert summary.visitors.median_session_seconds is None
    assert summary.by_world == []
    assert summary.price_table_source is None
    assert summary.top_asks == []


def test_sessions_without_a_visitor_id_count_toward_sessions_but_not_visitors(store, usage_store):
    """anon_cap disabled (or a pre-anon_cap session_started event) - the
    honest case, not an error: it should never look like zero sessions."""
    sid = _open(store, visitor_id=None)
    _touch(store, sid)
    summary = get_usage_summary(store, usage_store)
    assert summary.visitors.unique_visitors == 0
    assert summary.visitors.sessions_with_visitor_id == 0
    assert summary.visitors.median_session_seconds is not None  # duration still measured


def test_one_visitor_two_sessions_counts_as_one_unique_visitor(store, usage_store):
    a = _open(store, visitor_id="visitor-a")
    _touch(store, a)
    b = _open(store, visitor_id="visitor-a")
    _touch(store, b)
    c = _open(store, visitor_id="visitor-b")
    _touch(store, c)

    summary = get_usage_summary(store, usage_store)
    assert summary.visitors.unique_visitors == 2
    assert summary.visitors.sessions_with_visitor_id == 3
    # visitor-a's total is the SUM of its two sessions, not a third data point
    assert summary.visitors.median_visitor_total_seconds is not None


def test_usage_log_buckets_by_world_and_unattributed_separately(store, usage_store):
    usage_store.append(UsageRecord(
        trace_id=str(uuid.uuid4()), session_id="s1", call_kind="voice_generation", model_id="us.anthropic.claude-sonnet-4-5-20250929-v1:0",
        provider="bedrock", usage=NormalizedUsage(100, 50, 0, 0), world_key="fix",
    ))
    usage_store.append(UsageRecord(
        trace_id=str(uuid.uuid4()), session_id="s1", call_kind="turn_selector", model_id="us.anthropic.claude-haiku-4-5-20251001-v1:0",
        provider="bedrock", usage=NormalizedUsage(10, 2, 0, 0), world_key=None,
    ))
    summary = get_usage_summary(store, usage_store)
    by_key = {w.world_key: w for w in summary.by_world}
    assert set(by_key) == {"fix", "_unattributed"}
    assert by_key["fix"].calls == 1
    assert by_key["fix"].input_tokens == 100
    assert by_key["_unattributed"].calls == 1
    # every priced call reconciles: nothing silently dropped from the count
    assert sum(w.calls for w in summary.by_world) == 2


def test_priced_call_kinds_get_a_dollar_figure_unpriced_ones_dont(store, usage_store):
    usage_store.append(UsageRecord(
        trace_id=str(uuid.uuid4()), session_id="s1", call_kind="voice_generation", model_id="us.anthropic.claude-sonnet-4-5-20250929-v1:0",
        provider="bedrock", usage=NormalizedUsage(1_000_000, 0, 0, 0), world_key="fix",
    ))
    usage_store.append(UsageRecord(
        # preflight is a real call_kind (usage.py) with no approved price table
        trace_id=str(uuid.uuid4()), session_id="s1", call_kind="preflight", model_id="m",
        provider="bedrock", usage=NormalizedUsage(1_000_000, 0, 0, 0), world_key="fix",
    ))
    summary = get_usage_summary(store, usage_store)
    fix = summary.by_world[0]
    assert fix.calls == 2
    assert fix.unpriced_calls == 1
    assert fix.priced_dollars == pytest.approx(3.30)  # 1M input tokens @ $3/M, Sonnet-class, x1.10 Bedrock regional profile
    bedrock = {r.route: r for r in summary.by_route}["bedrock"]
    assert (bedrock.calls, bedrock.unpriced_calls) == (2, 1)
    assert bedrock.priced_dollars == pytest.approx(3.30)
    assert summary.price_table_source is not None


def test_since_filters_the_visitor_half(store, usage_store):
    _open(store, visitor_id="visitor-old")
    summary_all = get_usage_summary(store, usage_store)
    summary_future = get_usage_summary(store, usage_store, since="2099-01-01")
    assert summary_all.visitors.unique_visitors == 1
    assert summary_future.visitors.unique_visitors == 0


def test_missing_m7_audit_root_degrades_to_no_asks_never_errors(store, usage_store, tmp_path):
    summary = get_usage_summary(store, usage_store, m7_audit_root=tmp_path / "does-not-exist")
    assert summary.top_asks == []
    assert summary.asks_as_of_run is None


def test_endpoint_404s_without_admin_token(store, usage_store, world_loader, registry):
    client = _table_client(selector_script=[], stream_scripts=[])
    app = create_app(
        voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
        store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, default_world_key="fix",
    )
    http = TestClient(app)
    resp = http.get("/api/admin/usage-summary", headers={"Authorization": "Bearer anything"})
    assert resp.status_code == 404


def test_endpoint_returns_the_summary_shape(store, usage_store, world_loader, registry):
    sid = _open(store, visitor_id="visitor-a")
    _touch(store, sid)
    client = _table_client(selector_script=[], stream_scripts=[])
    token = "the-real-token-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    app = create_app(
        voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
        store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, default_world_key="fix",
        admin_token=token,
    )
    http = TestClient(app)
    resp = http.get("/api/admin/usage-summary", headers={"Authorization": f"Bearer {token}"})
    assert resp.status_code == 200
    body = resp.json()
    assert body["visitors"]["unique_visitors"] == 1
    assert body["by_world"] == []
    assert body["top_asks"] == []


def test_dashboard_page_is_served(store, usage_store, world_loader, registry):
    client = _table_client(selector_script=[], stream_scripts=[])
    app = create_app(
        voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
        store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, default_world_key="fix",
    )
    http = TestClient(app)
    resp = http.get("/admin/dashboard")
    assert resp.status_code == 200
    assert "text/html" in resp.headers["content-type"]


def _event(store, session_id, event_type, payload):
    store.append(session_id=session_id, event_uuid=str(uuid.uuid4()), event_type=event_type, payload=payload)


def test_an_idle_close_written_later_does_not_lengthen_the_session(store, usage_store, monkeypatch):
    from engine.m7 import session_reader
    sid = _open(store, visitor_id="visitor-a")
    _touch(store, sid)
    _event(store, sid, "session_closed", {"reason": "idle"})
    events = store.read_events(sid)
    stamps = ["2026-10-01T10:00:00+00:00", "2026-10-01T10:05:00+00:00", "2026-10-08T11:00:00+00:00"]
    patched = [type(e)(**{**e.__dict__, "created_at": t}) for e, t in zip(events, stamps)]
    monkeypatch.setattr(store, "read_events", lambda s: patched if s == sid else [])
    summary = get_usage_summary(store, usage_store)
    assert summary.visitors.median_session_seconds == 300
    assert summary.visitors.median_visitor_total_seconds == 300


def test_a_session_opened_without_a_message_is_counted_apart(store, usage_store):
    _open(store, visitor_id="visitor-a")
    b = _open(store, visitor_id="visitor-b")
    _touch(store, b)
    summary = get_usage_summary(store, usage_store)
    assert summary.visitors.sessions_without_a_message == 1
    assert summary.visitors.unique_visitors == 2
    assert summary.visitors.sessions_with_visitor_id == 2


def _record(**kw):
    base = dict(
        trace_id=str(uuid.uuid4()), session_id="s1", call_kind="voice_generation", model_id="us.anthropic.claude-sonnet-4-5-20250929-v1:0",
        provider="bedrock", usage=NormalizedUsage(1_000_000, 0, 0, 0), world_key="fix",
    )
    base.update(kw)
    return UsageRecord(**base)


def _write_report(directory, name, doc):
    directory.mkdir(exist_ok=True)
    (directory / name).write_text(json.dumps(doc), encoding="utf-8")


def test_a_named_test_report_is_listed_as_internal_with_its_spend(store, usage_store, tmp_path):
    reports = tmp_path / "reports"
    _write_report(reports, "live-turn-report-fix-2026-10-08.json", {
        "world_key": "fix",
        "live_test": {"name": "staging reading", "cap_usd": 5.0, "route": "Bedrock, regional inference profile, us-east-1", "priced_total_usd": 1.25},
        "usage": [{"call_kind": "safety_call", "world_key": "fix"}, {"call_kind": "voice_generation", "world_key": "fix"}],
    })
    summary = get_usage_summary(store, usage_store, live_test_reports_dir=reports)
    assert summary.named_tests.label == "internal"
    (test,) = summary.named_tests.tests
    assert (test.name, test.cap_usd, test.priced_total_usd, test.calls) == ("staging reading", 5.0, 1.25, 2)
    assert test.route == "Bedrock, regional inference profile, us-east-1" and test.world_keys == ["fix"] and test.missing == []
    assert summary.named_tests.recorded_priced_dollars == pytest.approx(1.25)
    assert summary.named_tests.tests_with_gaps == 0


def test_a_report_from_before_the_fields_existed_shows_not_recorded(store, usage_store, tmp_path):
    reports = tmp_path / "reports"
    _write_report(reports, "live-turn-report-alx.json", {"world_key": "alx", "results": [], "crisis_append_proven": None})
    _write_report(reports, "live-turn-report-broken.json", {"live_test": "not an object", "usage": {"not": "a list"}})
    (reports / "live-turn-report-unreadable.json").write_text("{not json", encoding="utf-8")
    summary = get_usage_summary(store, usage_store, live_test_reports_dir=reports)
    by_source = {t.source: t for t in summary.named_tests.tests}
    old = by_source["live-turn-report-alx.json"]
    assert (old.name, old.route) == ("not recorded", "not recorded")
    assert (old.cap_usd, old.priced_total_usd, old.calls) == (None, None, None)
    assert old.world_keys == ["alx"]
    assert set(old.missing) == {"name", "cap_usd", "route", "priced_total_usd", "usage"}
    assert by_source["live-turn-report-broken.json"].name == "not recorded"
    assert by_source["live-turn-report-unreadable.json"].missing[-1] == "unreadable report"
    assert summary.named_tests.recorded_priced_dollars == 0.0  # nothing guessed
    assert summary.named_tests.tests_with_gaps == 3


def test_live_use_is_one_unsplit_line_and_excludes_named_tests(store, usage_store, tmp_path):
    usage_store.append(_record())
    usage_store.append(_record(world_key="alx"))
    usage_store.append(_record(live_test="logged test"))
    summary = get_usage_summary(store, usage_store, live_test_reports_dir=tmp_path / "none")
    assert summary.live_use.label == "live use, not yet split"
    assert summary.live_use.calls == 2
    assert summary.live_use.priced_dollars == pytest.approx(6.60)
    (logged,) = summary.named_tests.tests
    assert (logged.source, logged.name, logged.calls) == ("usage log", "logged test", 1)
    assert logged.priced_total_usd == pytest.approx(3.30) and logged.cap_usd is None and "cap_usd" in logged.missing
    assert sum(w.calls for w in summary.by_world) == 3  # the per-world table still counts every call


def test_the_endpoint_carries_the_split(store, usage_store, world_loader, registry, monkeypatch, tmp_path):
    from engine.api import wiring
    _write_report(tmp_path / "reports", "live-turn-report-fix.json", {"world_key": "fix"})
    monkeypatch.setattr(wiring, "LIVE_TEST_REPORTS_DIR", tmp_path / "reports")
    usage_store.append(_record())
    client = _table_client(selector_script=[], stream_scripts=[])
    app = create_app(
        voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
        store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, default_world_key="fix",
        admin_token="t",
    )
    body = TestClient(app).get("/api/admin/usage-summary", headers={"Authorization": "Bearer t"}).json()
    assert body["live_use"] == {"label": "live use, not yet split", "calls": 1, "priced_dollars": pytest.approx(3.30), "unpriced_calls": 0}
    assert body["named_tests"]["label"] == "internal"
    assert body["named_tests"]["tests"][0]["name"] == "not recorded"
