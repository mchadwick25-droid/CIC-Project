import tempfile
from pathlib import Path

from engine.m8.log_store import UsageLogStore
from engine.m8.usage import record_usage
from engine.provider.bedrock import NormalizedUsage

USAGE = NormalizedUsage(input_tokens=10, output_tokens=5, cache_creation_input_tokens=1600, cache_read_input_tokens=0)


def _store():
    tmp = tempfile.NamedTemporaryFile(suffix=".sqlite3", delete=False)
    return UsageLogStore(Path(tmp.name))


def test_append_and_read_all_round_trips_the_record():
    store = _store()
    record = record_usage(usage=USAGE, session_id="s1", call_kind="safety_call", model_id="m")
    store.append(record)
    all_records = store.read_all()
    assert len(all_records) == 1
    assert all_records[0].trace_id == record.trace_id
    assert all_records[0].usage == USAGE


def test_read_for_session_filters_correctly():
    store = _store()
    store.append(record_usage(usage=USAGE, session_id="s1", call_kind="safety_call", model_id="m"))
    store.append(record_usage(usage=USAGE, session_id="s2", call_kind="safety_call", model_id="m"))
    store.append(record_usage(usage=USAGE, session_id="s1", call_kind="reader_call", model_id="m"))

    s1_records = store.read_for_session("s1")
    assert len(s1_records) == 2
    assert all(r.session_id == "s1" for r in s1_records)


def test_append_is_idempotent_on_trace_id():
    store = _store()
    record = record_usage(usage=USAGE, session_id="s1", call_kind="safety_call", model_id="m", trace_id="fixed-trace-id")
    store.append(record)
    store.append(record)  # retried append, same trace_id
    assert len(store.read_all()) == 1


def test_two_independent_store_instances_see_the_same_data():
    """Same 'any instance can serve any session' discipline as engine.m4.
    store.Store - a second Store instance against the same file sees what
    the first wrote."""
    tmp = tempfile.NamedTemporaryFile(suffix=".sqlite3", delete=False)
    store1 = UsageLogStore(Path(tmp.name))
    store1.append(record_usage(usage=USAGE, session_id="s1", call_kind="safety_call", model_id="m"))

    store2 = UsageLogStore(Path(tmp.name))
    assert len(store2.read_all()) == 1
