"""The literal stage-5 gate item: "resume across two processes incl. the
accumulator." Two independent Store instances pointed at the same backing
file stand in for two runtime processes/instances - neither shares any
Python object with the other, so full-fidelity reconstruction here proves
the "no process-local session state" guarantee for real, not by assertion.
"""
import uuid

from engine.m4.entrance import open_session
from engine.m4.projection import project_fresh
from engine.m4.store import Store


def test_resume_across_two_store_instances_full_fidelity(tmp_path):
    db_path = tmp_path / "events.db"
    sid = str(uuid.uuid4())

    process_one = Store(db_path)
    open_session(
        process_one,
        session_id=sid,
        event_uuid=str(uuid.uuid4()),
        world_key="fix",
        mode="interview",
        frame=None,
        code_hash="abc",
        package_manifest_hash="sha256:xyz",
    )
    process_one.append(session_id=sid, event_uuid=str(uuid.uuid4()), event_type="participant_message", payload={"text": "hello", "client_msg_id": "1"})
    process_one.append(session_id=sid, event_uuid=str(uuid.uuid4()), event_type="safety_state", payload={"track": "B", "level": "none", "accumulator": {"RETURN_COMPULSION": 2}})
    process_one.append(session_id=sid, event_uuid=str(uuid.uuid4()), event_type="turn_committed", payload={"turn_no": 1})
    del process_one  # nothing about this process may be relied on further

    # A brand new instance, sharing nothing but the file path - the resume.
    process_two = Store(db_path)
    process_two.append(session_id=sid, event_uuid=str(uuid.uuid4()), event_type="session_resumed", payload={"device_hint": "new-device"})
    process_two.append(session_id=sid, event_uuid=str(uuid.uuid4()), event_type="safety_state", payload={"track": "B", "level": "none", "accumulator": {"RETURN_COMPULSION": 3}})

    state = project_fresh(sid, process_two)
    assert state.world_key == "fix"
    assert state.turn_count == 1
    assert state.resumed_count == 1
    # the accumulator carried forward and was updated post-resume, never
    # silently reset to zero by the new process (spec SS8).
    assert state.safety.track_b_accumulator == {"RETURN_COMPULSION": 3}


def test_a_third_instance_sees_identical_state(tmp_path):
    """Any instance can serve any session (Artifact-3 SS1) - a third,
    still-different instance must fold to the exact same state as the
    second, not just "close enough.\""""
    db_path = tmp_path / "events.db"
    sid = str(uuid.uuid4())
    store_a = Store(db_path)
    open_session(store_a, session_id=sid, event_uuid=str(uuid.uuid4()), world_key="fix", mode="interview", frame=None, code_hash="c", package_manifest_hash="m")
    store_a.append(session_id=sid, event_uuid=str(uuid.uuid4()), event_type="turn_committed", payload={"turn_no": 1})

    store_b = Store(db_path)
    store_c = Store(db_path)
    assert project_fresh(sid, store_b) == project_fresh(sid, store_c)
