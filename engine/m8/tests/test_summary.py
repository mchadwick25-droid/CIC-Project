import pytest

from engine.m8.summary import summarize_session
from engine.m8.usage import record_usage
from engine.provider.bedrock import NormalizedUsage

USAGE_A = NormalizedUsage(input_tokens=100, output_tokens=50, cache_creation_input_tokens=1600, cache_read_input_tokens=0)
USAGE_B = NormalizedUsage(input_tokens=10, output_tokens=200, cache_creation_input_tokens=0, cache_read_input_tokens=1600)


def test_summarize_session_totals_correctly():
    records = [
        record_usage(usage=USAGE_A, session_id="s1", call_kind="safety_call", model_id="m"),
        record_usage(usage=USAGE_B, session_id="s1", call_kind="voice_generation", model_id="m"),
        record_usage(usage=USAGE_A, session_id="s1", call_kind="reader_call", model_id="m"),
    ]
    summary = summarize_session(records)
    assert summary.session_id == "s1"
    assert summary.call_count == 3
    assert summary.input_tokens == 210
    assert summary.output_tokens == 300
    assert summary.cache_creation_input_tokens == 3200
    assert summary.cache_read_input_tokens == 1600
    assert summary.by_call_kind == {"safety_call": 1, "voice_generation": 1, "reader_call": 1}


def test_summarize_session_rejects_mixed_sessions():
    records = [
        record_usage(usage=USAGE_A, session_id="s1", call_kind="safety_call", model_id="m"),
        record_usage(usage=USAGE_A, session_id="s2", call_kind="safety_call", model_id="m"),
    ]
    with pytest.raises(ValueError, match="multiple sessions"):
        summarize_session(records)


def test_summarize_session_rejects_empty_list():
    with pytest.raises(ValueError, match="no records"):
        summarize_session([])
