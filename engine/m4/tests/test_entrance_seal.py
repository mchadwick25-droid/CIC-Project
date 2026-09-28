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


def test_open_session_carries_visitor_id_when_given(tmp_path):
    store = Store(tmp_path / "events.db")
    sid = str(uuid.uuid4())
    open_session(
        store, session_id=sid, event_uuid=str(uuid.uuid4()), world_key="fix", mode="interview", frame=None,
        code_hash="deadbeef", package_manifest_hash="sha256:deadbeef", visitor_id="visitor-a",
    )
    assert store.read_events(sid)[0].payload["visitor_id"] == "visitor-a"


def test_open_session_omits_visitor_id_when_not_given(tmp_path):
    """Same "Nones are never written" contract package_location already
    has - an absent visitor_id must not appear as a null key, so a
    session_started event written before this field existed folds
    identically to one written with anon_cap disabled today."""
    store = Store(tmp_path / "events.db")
    sid = str(uuid.uuid4())
    _open(store, sid)
    assert "visitor_id" not in store.read_events(sid)[0].payload
