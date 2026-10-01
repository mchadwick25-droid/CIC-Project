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
        trace_id=str(uuid.uuid4()), session_id="s1", call_kind="voice_generation", model_id="m",
        provider="bedrock", usage=NormalizedUsage(100, 50, 0, 0), world_key="fix",
    ))
    usage_store.append(UsageRecord(
        trace_id=str(uuid.uuid4()), session_id="s1", call_kind="turn_selector", model_id="m",
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
        trace_id=str(uuid.uuid4()), session_id="s1", call_kind="voice_generation", model_id="m",
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
    assert fix.priced_dollars == pytest.approx(3.00)  # 1M input tokens @ $3/M, Sonnet-class
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
