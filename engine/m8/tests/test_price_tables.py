import pytest

from engine.m8.price_tables import (
    HAIKU_4_5_PRICE_TABLE,
    OPUS_5_5_PRICE_TABLE,
    SONNET_4_5_PRICE_TABLE,
    SONNET_5_5_PRICE_TABLE,
    price_for_call,
    price_for_model,
)


@pytest.mark.parametrize("model_id, table", [
    ("us.anthropic.claude-sonnet-4-5-20250929-v1:0", SONNET_4_5_PRICE_TABLE),
    ("us.anthropic.claude-haiku-4-5-20251001-v1:0", HAIKU_4_5_PRICE_TABLE),
    ("anthropic.claude-sonnet-5-5", SONNET_5_5_PRICE_TABLE),
    ("claude-opus-5-5", OPUS_5_5_PRICE_TABLE),
])
def test_a_model_id_finds_its_family_row(model_id, table):
    assert price_for_model(model_id) is table


@pytest.mark.parametrize("model_id", ["", "m", "us.anthropic.claude-opus-4-1-20250805-v1:0", "claude-sonnet-5"])
def test_a_model_without_a_row_is_unpriced(model_id):
    assert price_for_model(model_id) is None


def test_a_priced_5_family_call_uses_its_own_rates():
    table = price_for_call("voice_generation", "anthropic.claude-sonnet-5-5")
    assert table.input_per_token == pytest.approx(2.00 / 1_000_000)
    assert table.output_per_token == pytest.approx(10.00 / 1_000_000)
    assert table.cache_write_per_token == pytest.approx(2.50 / 1_000_000)
    assert table.cache_read_per_token == pytest.approx(0.20 / 1_000_000)


def test_preflight_stays_unpriced_whatever_its_model():
    assert price_for_call("preflight", "us.anthropic.claude-sonnet-4-5-20250929-v1:0") is None


def test_the_voice_call_is_priced_by_its_model_not_its_kind():
    assert price_for_call("voice_generation", "us.anthropic.claude-haiku-4-5-20251001-v1:0") is HAIKU_4_5_PRICE_TABLE
