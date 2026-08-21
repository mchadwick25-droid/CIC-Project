from types import SimpleNamespace

import pytest

from engine.m8.parity import UsageParityError, assert_parity, check_parity
from engine.provider.bedrock import NormalizedUsage, normalize_usage


def test_faithful_normalization_is_parity_ok():
    raw = SimpleNamespace(input_tokens=100, output_tokens=50, cache_creation_input_tokens=1600, cache_read_input_tokens=0)
    normalized = normalize_usage(raw)
    result = check_parity(raw, normalized)
    assert result.ok is True
    assert result.mismatches == {}


def test_raw_missing_cache_fields_still_parity_ok():
    """The exact silent-absence risk (spec SS10): a raw usage shape lacking
    cache_* attributes normalizes to 0 - parity holds because both sides
    agree it's 0, not because the field was ignored."""
    raw = SimpleNamespace(input_tokens=100, output_tokens=50)
    normalized = normalize_usage(raw)
    result = check_parity(raw, normalized)
    assert result.ok is True


def test_a_divergent_normalization_is_caught_by_name():
    raw = SimpleNamespace(input_tokens=100, output_tokens=50, cache_creation_input_tokens=1600, cache_read_input_tokens=0)
    tampered = NormalizedUsage(input_tokens=999, output_tokens=50, cache_creation_input_tokens=1600, cache_read_input_tokens=0)
    result = check_parity(raw, tampered)
    assert result.ok is False
    assert result.mismatches == {"input_tokens": (100, 999)}


def test_assert_parity_raises_with_the_field_name_on_mismatch():
    raw = SimpleNamespace(input_tokens=100, output_tokens=50, cache_creation_input_tokens=0, cache_read_input_tokens=0)
    tampered = NormalizedUsage(input_tokens=100, output_tokens=999, cache_creation_input_tokens=0, cache_read_input_tokens=0)
    with pytest.raises(UsageParityError, match="output_tokens"):
        assert_parity(raw, tampered)


def test_assert_parity_passes_silently_when_faithful():
    raw = SimpleNamespace(input_tokens=10, output_tokens=5, cache_creation_input_tokens=0, cache_read_input_tokens=0)
    assert_parity(raw, normalize_usage(raw))  # no raise
