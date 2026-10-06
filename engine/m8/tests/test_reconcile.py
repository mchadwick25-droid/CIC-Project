from engine.m8.log_store import UsageLogStore
from engine.m8.reconcile import month_bounds, reconcile
from engine.m8.usage import record_usage
from engine.provider.bedrock import NormalizedUsage

USAGE = NormalizedUsage(input_tokens=1_000_000, output_tokens=0, cache_creation_input_tokens=0, cache_read_input_tokens=0)
MODEL = "us.anthropic.claude-sonnet-4-5-20250929-v1:0"


def _store(tmp_path, when):
    store = UsageLogStore(str(tmp_path / "u.db"))
    store.append(record_usage(usage=USAGE, session_id="s", call_kind="voice_generation", model_id=MODEL, provider="bedrock"))
    with store._connect() as conn:
        conn.execute("UPDATE usage_log SET created_at = ?", (when,))
        conn.commit()
    return store


def test_month_bounds_roll_over_the_year():
    assert month_bounds("2026-12")[1].startswith("2027-01-01")


def test_invoice_matching_the_route_price_is_within_tolerance(tmp_path):
    result = reconcile(_store(tmp_path, "2026-09-10T00:00:00+00:00"), "2026-09", "bedrock", 3.30)
    assert result.calls == 1 and result.within_tolerance
    assert round(result.list_factor, 2) == 1.10


def test_drift_past_tolerance_fails(tmp_path):
    assert not reconcile(_store(tmp_path, "2026-09-10T00:00:00+00:00"), "2026-09", "bedrock", 4.50).within_tolerance


def test_other_months_and_routes_are_left_out(tmp_path):
    store = _store(tmp_path, "2026-08-10T00:00:00+00:00")
    assert reconcile(store, "2026-09", "bedrock", 3.30).calls == 0
