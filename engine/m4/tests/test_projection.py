import uuid

from engine.m4.entrance import open_session
from engine.m4.projection import project_fresh
from engine.m4.store import Store


def _seed(store, sid):
    open_session(
        store,
        session_id=sid,
        event_uuid=str(uuid.uuid4()),
        world_key="fix",
        mode="interview",
        frame="general_seeker",
        code_hash="abc123",
        package_manifest_hash="sha256:xyz",
    )
    store.append(session_id=sid, event_uuid=str(uuid.uuid4()), event_type="participant_message", payload={"text": "who was Jesus?", "client_msg_id": "m1"})
    store.append(
        session_id=sid,
        event_uuid=str(uuid.uuid4()),
        event_type="gate_decision",
        payload={"asks": [{"order": 1, "text": "who was Jesus"}], "register": "informational", "out_of_scope": {"class": "none", "pressed": False}, "modern_terms": [], "safety": {"signal": "NO_SIGNAL", "confidence": "high"}, "route": "voice", "directive": {}, "degraded": False},
    )
    store.append(session_id=sid, event_uuid=str(uuid.uuid4()), event_type="voice_turn", payload={"speaker": "Vera", "text": "I did not see him myself...", "citations": ["fix.source.witness-scroll"], "glosses": [], "quote_offers": [], "attempts_meta": {}})
    store.append(session_id=sid, event_uuid=str(uuid.uuid4()), event_type="safety_state", payload={"track": "B", "level": "none", "accumulator": {"CONFIDANT_LANGUAGE": 1}})
    store.append(session_id=sid, event_uuid=str(uuid.uuid4()), event_type="turn_committed", payload={"turn_no": 1})


def test_project_fresh_folds_full_state(tmp_path):
    store = Store(tmp_path / "events.db")
    sid = str(uuid.uuid4())
    _seed(store, sid)

    state = project_fresh(sid, store)
    assert state.exists
    assert state.world_key == "fix"
    assert state.mode == "interview"
    assert state.frame == "general_seeker"
    assert state.turn_count == 1
    assert state.last_turn_no == 1
    assert state.degraded_turn_count == 0
    assert state.safety.track_b_accumulator == {"CONFIDANT_LANGUAGE": 1}
    assert [t["speaker"] for t in state.transcript] == ["participant", "Vera"]


def test_project_fresh_on_unknown_session_is_empty(tmp_path):
    store = Store(tmp_path / "events.db")
    state = project_fresh(str(uuid.uuid4()), store)
    assert state.exists is False
    assert state.world_key is None


def test_pressed_state_folds_from_escalation_pressed(tmp_path):
    store = Store(tmp_path / "events.db")
    sid = str(uuid.uuid4())
    _seed(store, sid)
    store.append(session_id=sid, event_uuid=str(uuid.uuid4()), event_type="escalation_pressed", payload={"class": "later_age"})

    state = project_fresh(sid, store)
    assert state.pressed == {"later_age": True, "other_tradition": False}
