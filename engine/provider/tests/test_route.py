"""No network and no model call: clients are built or mocked, never used."""
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import MagicMock, patch

import pytest

from engine.m8.price_tables import price_for_call, price_for_route
from engine.m8.usage import record_usage
from engine.provider import anthropic_direct, route
from engine.provider.bedrock import NormalizedUsage, normalize_usage

REPO = Path(__file__).resolve().parents[3]
USAGE = NormalizedUsage(input_tokens=1000, output_tokens=100, cache_creation_input_tokens=0, cache_read_input_tokens=0)


def test_default_route_is_bedrock(monkeypatch):
    monkeypatch.delenv(route.ROUTE_ENV, raising=False)
    assert route.active_route() == "bedrock"


def test_unknown_route_stops_the_start(monkeypatch):
    monkeypatch.setenv(route.ROUTE_ENV, "bedrok")
    with pytest.raises(route.UnknownRouteError):
        route.active_route()


def test_anthropic_client_cannot_be_built_with_route_unset(monkeypatch):
    monkeypatch.delenv(route.ROUTE_ENV, raising=False)
    monkeypatch.setenv(anthropic_direct.KEY_ENV, "k")
    with pytest.raises(anthropic_direct.RouteNotEnabledError):
        anthropic_direct.make_client()


def test_anthropic_client_needs_a_key(monkeypatch):
    monkeypatch.setenv(route.ROUTE_ENV, "anthropic")
    monkeypatch.delenv(anthropic_direct.KEY_ENV, raising=False)
    with pytest.raises(anthropic_direct.RouteNotEnabledError):
        anthropic_direct.make_client()


def test_anthropic_resolution_requires_one_match(monkeypatch):
    monkeypatch.setenv(route.ROUTE_ENV, "anthropic")
    monkeypatch.setenv(anthropic_direct.KEY_ENV, "k")
    ids = ["claude-sonnet-4-5-20250929", "claude-haiku-4-5-20251001"]
    fake = MagicMock()
    fake.models.list.return_value = SimpleNamespace(data=[SimpleNamespace(id=i) for i in ids])
    with patch.object(anthropic_direct, "make_client", return_value=fake):
        assert anthropic_direct.resolve_model_id("us.anthropic.claude-sonnet-4-5") == ids[0]
        with pytest.raises(anthropic_direct.ModelResolutionError):
            anthropic_direct.resolve_model_id("claude")


def test_both_routes_normalize_the_same_usage_shape():
    shape = SimpleNamespace(input_tokens=10, output_tokens=5, cache_creation_input_tokens=3, cache_read_input_tokens=2)
    assert anthropic_direct.normalize_usage(shape) == normalize_usage(shape)


def test_usage_log_names_the_route(monkeypatch):
    monkeypatch.delenv(route.ROUTE_ENV, raising=False)
    assert record_usage(usage=USAGE, session_id="s", call_kind="voice_generation", model_id="m").provider == "bedrock"
    monkeypatch.setenv(route.ROUTE_ENV, "anthropic")
    assert record_usage(usage=USAGE, session_id="s", call_kind="voice_generation", model_id="m").provider == "anthropic"


def test_regional_bedrock_profile_carries_the_premium_and_global_does_not():
    regional = price_for_route("voice_generation", "us.anthropic.claude-sonnet-4-5-20250929-v1:0", "bedrock")
    global_ = price_for_route("voice_generation", "global.anthropic.claude-sonnet-4-5-20250929-v1:0", "bedrock")
    direct = price_for_route("voice_generation", "claude-sonnet-4-5-20250929", "anthropic")
    assert global_.input_per_token == direct.input_per_token == 3.00 / 1_000_000
    assert regional.input_per_token == pytest.approx(3.30 / 1_000_000)
    assert regional.cache_read_per_token == pytest.approx(0.33 / 1_000_000)


def test_door_pricing_stays_at_list():
    table = price_for_call("voice_generation", "us.anthropic.claude-sonnet-4-5-20250929-v1:0")
    assert table.input_per_token == 3.00 / 1_000_000


def test_unpriced_stays_unpriced_on_every_route():
    assert price_for_route("preflight", "us.anthropic.claude-sonnet-4-5", "bedrock") is None


def test_render_yaml_carries_no_anthropic_key_or_route():
    text = (REPO / "render.yaml").read_text()
    assert "CIC_ANTHROPIC_API_KEY" not in text
    assert "ANTHROPIC_API_KEY" not in text
    assert route.ROUTE_ENV not in text
