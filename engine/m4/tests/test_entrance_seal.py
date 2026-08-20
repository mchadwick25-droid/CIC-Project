import uuid

import pytest

from engine.m4.entrance import SecondWriterError, find_second_writer_violations, open_session
from engine.m4.store import Store


def _open(store, sid):
    return open_session(
        store,
        session_id=sid,
        event_uuid=str(uuid.uuid4()),
        world_key="fix",
        mode="interview",
        frame=None,
        code_hash="deadbeef",
        package_manifest_hash="sha256:deadbeef",
    )


def test_open_session_writes_session_started(tmp_path):
    store = Store(tmp_path / "events.db")
    sid = str(uuid.uuid4())
    seq = _open(store, sid)
    assert seq == 1
    events = store.read_events(sid)
    assert events[0].event_type == "session_started"
    assert events[0].payload["world_key"] == "fix"


def test_second_session_started_is_refused(tmp_path):
    store = Store(tmp_path / "events.db")
    sid = str(uuid.uuid4())
    _open(store, sid)
    with pytest.raises(SecondWriterError):
        _open(store, sid)


def test_no_production_code_outside_entrance_constructs_session_started():
    assert find_second_writer_violations() == []
