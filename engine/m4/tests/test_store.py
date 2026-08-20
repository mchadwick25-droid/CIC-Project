import uuid

from engine.m4.store import Store


def _store(tmp_path):
    return Store(tmp_path / "events.db")


def test_append_assigns_sequential_seq(tmp_path):
    store = _store(tmp_path)
    sid = str(uuid.uuid4())
    seq1 = store.append(session_id=sid, event_uuid=str(uuid.uuid4()), event_type="participant_message", payload={"text": "hi", "client_msg_id": "1"})
    seq2 = store.append(session_id=sid, event_uuid=str(uuid.uuid4()), event_type="participant_message", payload={"text": "again", "client_msg_id": "2"})
    assert (seq1, seq2) == (1, 2)


def test_append_is_idempotent_on_event_uuid(tmp_path):
    store = _store(tmp_path)
    sid = str(uuid.uuid4())
    eid = str(uuid.uuid4())
    seq1 = store.append(session_id=sid, event_uuid=eid, event_type="participant_message", payload={"text": "hi", "client_msg_id": "1"})
    seq2 = store.append(session_id=sid, event_uuid=eid, event_type="participant_message", payload={"text": "hi", "client_msg_id": "1"})
    assert seq1 == seq2 == 1
    assert len(store.read_events(sid)) == 1


def test_read_events_ordered(tmp_path):
    store = _store(tmp_path)
    sid = str(uuid.uuid4())
    for i in range(5):
        store.append(session_id=sid, event_uuid=str(uuid.uuid4()), event_type="participant_message", payload={"text": str(i), "client_msg_id": str(i)})
    events = store.read_events(sid)
    assert [e.seq for e in events] == [1, 2, 3, 4, 5]
    assert [e.payload["text"] for e in events] == ["0", "1", "2", "3", "4"]


def test_sessions_are_independent(tmp_path):
    store = _store(tmp_path)
    a, b = str(uuid.uuid4()), str(uuid.uuid4())
    store.append(session_id=a, event_uuid=str(uuid.uuid4()), event_type="participant_message", payload={"text": "a", "client_msg_id": "1"})
    assert store.read_events(b) == []
