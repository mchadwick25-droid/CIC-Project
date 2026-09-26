"""engine.m7.session_reader's own event fold - specifically the idle-close
reopen rule, which must agree with engine.m4.projection's
identical rule (engine/m4/tests/test_projection.py) or the admin
pilot-summary endpoint (which reads through this module) and the
participant-facing transcript (which reads through projection) would
disagree about whether a resumed session is still "closed"."""
import uuid

from engine.m4.store import Store
from engine.m7.session_reader import read_session


def _append(store, sid, etype, payload):
    store.append(session_id=sid, event_uuid=str(uuid.uuid4()), event_type=etype, payload=payload)


def _start_session(store, sid):
    _append(store, sid, "session_started", {
        "mode": "interview", "frame": "general_seeker", "code_hash": "abc",
        "world_key": "fix", "package_manifest_hash": "sha256:x",
    })


def test_idle_close_reads_closed_until_real_activity_reopens_it(tmp_path):
    store = Store(tmp_path / "events.db")
    _start_session(store, "s1")
    _append(store, "s1", "session_closed", {"reason": "idle"})

    idle = read_session(store, "s1")
    assert idle.closed is True
    assert idle.close_reason == "idle"

    _append(store, "s1", "participant_message", {"text": "still there?", "client_msg_id": "m2"})

    resumed = read_session(store, "s1")
    assert resumed.closed is False
    assert resumed.close_reason is None


def test_cap_close_never_reopens(tmp_path):
    store = Store(tmp_path / "events.db")
    _start_session(store, "s1")
    _append(store, "s1", "session_closed", {"reason": "cap"})
    _append(store, "s1", "participant_message", {"text": "still there?", "client_msg_id": "m2"})

    session = read_session(store, "s1")
    assert session.closed is True
    assert session.close_reason == "cap"
