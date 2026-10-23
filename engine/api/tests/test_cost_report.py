"""engine/api/cost_report.py and /api/admin/cost-report: what a voiced round and a
safety check cost, read from the usage log as aggregate numbers."""
import json
import uuid
from datetime import datetime, timedelta, timezone

import pytest
from fastapi.testclient import TestClient

from engine.api import cost_report
from engine.api.app import create_app
from engine.api.tests.test_table_api import _table_client
from engine.m4.entrance import open_session
from engine.m8.usage import SYSTEM_SESSION_ID, NormalizedUsage, UsageRecord

SONNET = "us.anthropic.claude-sonnet-4-5-20250929-v1:0"
HAIKU = "us.anthropic.claude-haiku-4-5-20251001-v1:0"
BASE = datetime(2026, 10, 20, 12, 0, tzinfo=timezone.utc)
NOW = BASE + timedelta(days=2)


def _usage(inp=1000, out=100, write=0, read=0):
    return NormalizedUsage(input_tokens=inp, output_tokens=out, cache_creation_input_tokens=write, cache_read_input_tokens=read)


def _call(session, kind, when, usage, model=None, world="fix", live_test=None):
    model = model or (SONNET if kind == "voice_generation" else HAIKU)
    record = UsageRecord(
        trace_id=str(uuid.uuid4()), session_id=session, call_kind=kind, model_id=model, provider="bedrock", usage=usage,
        world_key=world, live_test=live_test,
    )
    return when.isoformat(), record


def _message(session, start, *, voiced, warm=False, voice_after=10):
    calls = [
        _call(session, "safety_call", start, _usage()),
        _call(session, "reader_call", start + timedelta(seconds=1), _usage()),
    ]
    if voiced:
        usage = _usage(inp=500, out=400, read=12000) if warm else _usage(inp=500, out=400, write=12000)
        calls.append(_call(session, "voice_generation", start + timedelta(seconds=voice_after), usage))
    return calls


def _price(record):
    return cost_report._price(record)[0]


def _solo_session(session="s1"):
    """Four voiced messages and one with no voice reply. The second follows after 60 s with a warm cache; the third after 400 s and the fourth after 4000 s, both cold."""
    calls = []
    calls += _message(session, BASE, voiced=True)
    calls += _message(session, BASE + timedelta(seconds=60), voiced=True, warm=True)
    calls += _message(session, BASE + timedelta(seconds=60 + 10 + 400), voiced=True)
    calls += _message(session, BASE + timedelta(seconds=60 + 10 + 400 + 10 + 4000), voiced=True)
    calls += _message(session, BASE + timedelta(seconds=9000), voiced=False)
    return calls


def _by_round(report):
    return {row["round"]: row for row in report["voiced_rounds_by_round_number"]}


def test_rounds_are_rebuilt_from_the_log_and_priced_with_the_approved_tables():
    timed = _solo_session()
    report = cost_report.build(timed, {"s1": "interview"}, NOW)
    rounds = _by_round(report)
    voice_calls = [r for _w, r in timed if r.call_kind == "voice_generation"]
    assert [rounds[str(n)]["rounds"] for n in (1, 2, 3, 4)] == [1, 1, 1, 1]
    assert rounds["5"]["rounds"] == 0 and rounds["5"]["voice_usd_mean"] is None
    for n, record in enumerate(voice_calls, start=1):
        assert rounds[str(n)]["voice_usd_mean"] == pytest.approx(_price(record), abs=1e-5)
    assert rounds["2"]["voice_usd_mean"] < rounds["1"]["voice_usd_mean"], "a warm round is cheaper than a cold one"
    assert rounds["2"]["cache_warm_share"] == 1.0 and rounds["1"]["cache_warm_share"] == 0.0


def test_a_rounds_total_includes_its_safety_and_reader_calls():
    timed = _solo_session()
    report = cost_report.build(timed, {"s1": "interview"}, NOW)
    first = _by_round(report)["1"]
    gate = sum(_price(r) for _w, r in timed[:2])
    assert first["voice_and_safety_usd_mean"] == pytest.approx(first["voice_usd_mean"] + gate, abs=1e-5)


def test_cache_warm_and_cold_are_split_by_the_pause_before_the_round():
    report = cost_report.build(_solo_session(), {"s1": "interview"}, NOW)
    pauses = {row["pause"]: row for row in report["cache"]["by_pause_before_the_round"]}
    assert (pauses["under_5_min"]["rounds"], pauses["under_5_min"]["warm"]["rounds"], pauses["under_5_min"]["cold"]["rounds"]) == (1, 1, 0)
    assert (pauses["5_to_60_min"]["rounds"], pauses["5_to_60_min"]["cold"]["rounds"]) == (1, 1)
    assert (pauses["over_60_min"]["rounds"], pauses["over_60_min"]["cold"]["rounds"]) == (1, 1)
    overall = report["cache"]["all_rounds_from_the_second"]
    assert (overall["rounds"], overall["warm"]["rounds"], overall["cold"]["rounds"]) == (3, 1, 2)
    assert overall["warm"]["voice_usd_mean"] < overall["cold"]["voice_usd_mean"]


def test_safety_checks_and_messages_with_no_voice_reply_are_counted_and_priced():
    timed = _solo_session()
    report = cost_report.build(timed, {"s1": "interview"}, NOW)
    safety = report["safety_checks"]
    assert safety["messages"] == 5 and safety["messages_with_no_voice_reply"] == 1
    one_gate = _price(timed[0][1]) + _price(timed[1][1])
    assert safety["no_voice_message_usd_mean"] == pytest.approx(one_gate, abs=1e-5)
    assert safety["safety_call_usd_mean"] == pytest.approx(_price(timed[0][1]), abs=1e-5)
    assert safety["no_voice_messages_usd_total"] == pytest.approx(one_gate, abs=1e-4)


def test_totals_cover_the_last_seven_and_thirty_days():
    old = BASE - timedelta(days=20)
    timed = _message("old", old, voiced=True) + _solo_session()
    timed.sort(key=lambda row: row[0])
    report = cost_report.build(timed, {"old": "interview", "s1": "interview"}, NOW)
    seven, thirty = report["totals"]["last_7_days"], report["totals"]["last_30_days"]
    assert (seven["messages"], thirty["messages"]) == (5, 6)
    assert (seven["voiced_rounds"], thirty["voiced_rounds"]) == (4, 5)
    assert thirty["total_usd"] > seven["total_usd"]
    assert seven["total_usd"] == pytest.approx(seven["voice_usd"] + seven["safety_and_other_usd"], abs=1e-4)
    assert seven["unvoiced_messages"] == 1 and seven["unvoiced_messages_usd"] > 0


def test_our_own_sessions_tests_and_system_calls_are_left_out():
    timed = _solo_session("s1") + _solo_session("ours")
    timed += [_call(SYSTEM_SESSION_ID, "preflight", BASE, _usage())]
    timed += [_call("t", "voice_generation", BASE, _usage(write=12000), live_test="a named test")]
    report = cost_report.build(timed, {"s1": "interview", "ours": "internal", "t": "interview"}, NOW)
    assert report["sessions"]["counted"] == 1
    assert report["sessions"]["left_out_as_our_own"] == 1
    assert report["totals"]["last_30_days"]["messages"] == 5


def test_a_table_or_unknown_session_is_in_the_totals_but_not_the_per_round_tables():
    timed = _solo_session("s1") + _message("tbl", BASE, voiced=True) + _message("who", BASE, voiced=True)
    report = cost_report.build(timed, {"s1": "interview", "tbl": "table"}, NOW)
    assert report["sessions"]["counted_in_totals_only_not_per_round"] == 2
    assert _by_round(report)["1"]["rounds"] == 1
    assert report["totals"]["last_30_days"]["voiced_rounds"] == 6


def test_a_model_with_no_approved_price_is_priced_at_the_dearest_and_counted():
    timed = [_call("s1", "voice_generation", BASE, _usage(write=12000), model="some.unlisted.model")]
    report = cost_report.build(timed, {"s1": "interview"}, NOW)
    assert report["calls_priced_at_the_dearest_price"] == 1
    assert report["totals"]["last_30_days"]["total_usd"] > 0


def test_rounds_past_ten_are_gathered_in_one_row():
    timed = []
    for n in range(12):
        timed += _message("long", BASE + timedelta(seconds=60 * n), voiced=True, warm=n > 0)
    report = cost_report.build(timed, {"long": "interview"}, NOW)
    rounds = report["voiced_rounds_by_round_number"]
    assert [row["rounds"] for row in rounds[:10]] == [1] * 10
    assert rounds[10]["round"] == "11 and later" and rounds[10]["rounds"] == 2


def test_an_empty_log_gives_zeros_and_no_averages():
    report = cost_report.build([], {}, NOW)
    assert report["sessions"]["counted"] == 0
    assert report["totals"]["last_30_days"]["total_usd"] == 0
    assert all(row["voice_usd_mean"] is None for row in report["voiced_rounds_by_round_number"])
    assert report["cache"]["all_rounds_from_the_second"]["voice_usd_mean"] is None


def test_the_report_names_no_session_world_or_address():
    report = cost_report.build(_solo_session("a-secret-session-id"), {"a-secret-session-id": "interview"}, NOW)
    text = json.dumps(report)
    assert "a-secret-session-id" not in text and "fix" not in report["sessions"]


# ---- the route ---------------------------------------------------------------------

def _open(store, *, internal=False, mode="interview"):
    session_id = str(uuid.uuid4())
    open_session(
        store, session_id=session_id, event_uuid=str(uuid.uuid4()), mode=mode, frame=None,
        code_hash="h", world_key="fix", package_manifest_hash="m", internal=internal,
    )
    return session_id


def _app(store, usage_store, world_loader, registry, token="the-real-token-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"):
    client = _table_client(selector_script=[], stream_scripts=[])
    return TestClient(create_app(
        voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
        store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, default_world_key="fix",
        admin_token=token,
    ))


def test_the_route_is_closed_without_the_admin_login(store, usage_store, world_loader, registry):
    http = _app(store, usage_store, world_loader, registry)
    assert http.get("/api/admin/cost-report").status_code == 404
    assert http.get("/api/admin/cost-report", headers={"Authorization": "Bearer wrong"}).status_code == 404


def test_the_route_is_a_404_when_no_admin_token_is_set(store, usage_store, world_loader, registry):
    client = _table_client(selector_script=[], stream_scripts=[])
    http = TestClient(create_app(
        voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
        store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, default_world_key="fix",
    ))
    assert http.get("/api/admin/cost-report", headers={"Authorization": "Bearer anything"}).status_code == 404


def test_the_route_reads_the_usage_log_and_the_conversation_store(store, usage_store, world_loader, registry):
    mine, ours = _open(store), _open(store, internal=True)
    for session in (mine, ours):
        for _when, record in _message(session, datetime.now(timezone.utc), voiced=True):
            usage_store.append(record)
    token = "the-real-token-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    http = _app(store, usage_store, world_loader, registry, token)
    body = http.get("/api/admin/cost-report", headers={"Authorization": f"Bearer {token}"}).json()
    assert body["sessions"]["counted"] == 1 and body["sessions"]["left_out_as_our_own"] == 1
    assert body["voiced_rounds_by_round_number"][0]["rounds"] == 1
    assert body["totals"]["last_7_days"]["voiced_rounds"] == 1
    assert mine not in json.dumps(body)


def test_the_store_reads_each_records_time(usage_store):
    _when, record = _message("s", datetime.now(timezone.utc), voiced=False)[0]
    usage_store.append(record)
    rows = usage_store.read_timed_since("2000-01-01T00:00:00+00:00")
    assert len(rows) == 1 and rows[0][1].trace_id == record.trace_id
    assert datetime.fromisoformat(rows[0][0]).tzinfo is not None
    assert usage_store.read_timed_since("2999-01-01T00:00:00+00:00") == []


def test_the_dashboard_shows_the_report_with_text_only():
    from pathlib import Path

    page = (Path(cost_report.__file__).parent / "static" / "admin_dashboard.html").read_text()
    assert "/api/admin/cost-report" in page and "renderCostReport" in page
    body = page[page.index("function renderCostReport"):page.index("function banner")]
    assert "innerHTML = \"\"" in body and body.count("innerHTML") == 1, "the report is written with textContent only"
