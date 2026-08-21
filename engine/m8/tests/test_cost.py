from engine.m8.cost import PriceTable, TURNS_PER_HOUR_CONVENTION, dollars_per_hour, estimate_cost
from engine.provider.bedrock import NormalizedUsage

USAGE = NormalizedUsage(input_tokens=1000, output_tokens=330, cache_creation_input_tokens=0, cache_read_input_tokens=0)


def test_no_price_table_is_explicitly_unpriced_never_a_guessed_number():
    """Spec principle 13: no $/token or $/turn figure until measured on
    the billing provider - the default path must say so, not silently
    return 0.0 (which would read as 'free,' a different and wrong claim)."""
    estimate = estimate_cost(USAGE)
    assert estimate.priced is False
    assert estimate.dollars is None
    assert estimate.price_source is None
    assert estimate.token_breakdown["input_tokens"] == 1000


def test_price_table_requires_a_source_never_an_anonymous_number():
    table = PriceTable(input_per_token=0.000003, output_per_token=0.000015, cache_write_per_token=0.000006, cache_read_per_token=0.0000003, source="test fixture rate, not a real quote")
    estimate = estimate_cost(USAGE, table)
    assert estimate.priced is True
    assert estimate.price_source == "test fixture rate, not a real quote"
    expected = 1000 * 0.000003 + 330 * 0.000015
    assert abs(estimate.dollars - expected) < 1e-12


def test_cache_tokens_priced_at_their_own_rate_not_input_rate():
    table = PriceTable(input_per_token=1.0, output_per_token=1.0, cache_write_per_token=2.0, cache_read_per_token=0.1, source="test")
    cached_usage = NormalizedUsage(input_tokens=0, output_tokens=0, cache_creation_input_tokens=100, cache_read_input_tokens=100)
    estimate = estimate_cost(cached_usage, table)
    assert estimate.dollars == 100 * 2.0 + 100 * 0.1


def test_turns_per_hour_convention_is_the_one_declared_in_spec():
    assert TURNS_PER_HOUR_CONVENTION == 12


def test_dollars_per_hour_uses_the_declared_convention():
    assert dollars_per_hour(0.017) == 0.017 * 12
