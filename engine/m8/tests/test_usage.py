import pytest

from engine.m8.usage import SYSTEM_SESSION_ID, record_usage, zero_unattributed
from engine.provider.bedrock import NormalizedUsage

USAGE = NormalizedUsage(input_tokens=10, output_tokens=5, cache_creation_input_tokens=0, cache_read_input_tokens=0)


def test_record_usage_requires_a_real_session_id():
    with pytest.raises(ValueError, match="session_id is required"):
        record_usage(usage=USAGE, session_id="", call_kind="safety_call", model_id="m")


def test_record_usage_rejects_none_session_id():
    with pytest.raises(ValueError, match="session_id is required"):
        record_usage(usage=USAGE, session_id=None, call_kind="safety_call", model_id="m")  # type: ignore[arg-type]


def test_system_session_id_is_a_real_explicit_tag_not_a_blank():
    record = record_usage(usage=USAGE, session_id=SYSTEM_SESSION_ID, call_kind="preflight", model_id="m")
    assert record.is_attributed is True
    assert record.session_id == "_system"


def test_ordinary_session_id_is_attributed():
    record = record_usage(usage=USAGE, session_id="real-session-1", call_kind="voice_generation", model_id="m")
    assert record.is_attributed is True


def test_each_record_gets_a_distinct_trace_id_by_default():
    r1 = record_usage(usage=USAGE, session_id="s1", call_kind="safety_call", model_id="m")
    r2 = record_usage(usage=USAGE, session_id="s1", call_kind="safety_call", model_id="m")
    assert r1.trace_id != r2.trace_id


def test_zero_unattributed_true_for_a_clean_batch():
    records = [record_usage(usage=USAGE, session_id="s1", call_kind="safety_call", model_id="m") for _ in range(3)]
    assert zero_unattributed(records) is True


def test_zero_unattributed_true_for_empty_batch():
    assert zero_unattributed([]) is True
