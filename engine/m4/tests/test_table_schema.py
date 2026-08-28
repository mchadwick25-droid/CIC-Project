"""Table mode's schema layer (Artifact-7 SS1-2): the mode-shaped
session_started payload, the two round event types, the sealed entrance's
table shape, and the projection's round bookkeeping. The interview mode's
own behavior is covered by the existing suites, which must keep passing
unmodified - the one interview assertion here (test_interview_log_projects_
unchanged) exists to say so in the same file that adds the new mode."""
import uuid

import pytest

from engine.m4.entrance import SecondWriterError, open_session
from engine.m4.events import EventValidationError, validate
from engine.m4.projection import project_fresh
from engine.m4.store import Store


def _table_started(world_keys=("alx", "desert"), **overrides):
    payload = {
        "mode": "table",
        "frame": None,
        "code_hash": "abc123",
        "world_keys": list(world_keys),
        "package_manifest_hashes": {k: f"sha256:{k}" for k in world_keys},
    }
    payload.update(overrides)
    return payload


# --- session_started, table shape ---


def test_table_session_started_two_worlds_passes():
    validate("session_started", _table_started(("alx", "desert")))


def test_table_session_started_three_worlds_passes():
    validate("session_started", _table_started(("alx", "desert", "pahc")))


def test_one_world_table_rejected():
    # One world is an interview, not a table (Artifact-7 SS1).
    with pytest.raises(EventValidationError):
        validate("session_started", _table_started(("alx",)))


def test_four_world_table_rejected():
    # The ceiling is schema-enforced - the mechanism the design doc's
    # construction note said did not exist.
    with pytest.raises(EventValidationError):
        validate("session_started", _table_started(("alx", "desert", "pahc", "syr")))


def test_duplicate_world_rejected():
    payload = _table_started(("alx", "desert"))
    payload["world_keys"] = ["alx", "alx"]
    payload["package_manifest_hashes"] = {"alx": "sha256:alx"}
    with pytest.raises(EventValidationError):
        validate("session_started", payload)


def test_hash_keys_must_match_world_keys():
    with pytest.raises(EventValidationError):
        validate("session_started", _table_started(("alx", "desert"), package_manifest_hashes={"alx": "sha256:alx"}))
    with pytest.raises(EventValidationError):
        validate(
            "session_started",
            _table_started(("alx", "desert"), package_manifest_hashes={"alx": "x", "desert": "y", "pahc": "z"}),
        )


def test_table_mode_with_interview_keys_rejected():
    # The old test_events bad-enum payload, now failing for its real reason:
    # mode "table" with the interview's singular keys is a shape mismatch.
    with pytest.raises(EventValidationError):
        validate(
            "session_started",
            {"world_key": "fix", "mode": "table", "frame": None, "code_hash": "x", "package_manifest_hash": "y"},
        )


def test_mixed_shape_rejected():
    payload = _table_started(("alx", "desert"))
    payload["world_key"] = "alx"
    with pytest.raises(EventValidationError):
        validate("session_started", payload)


def test_interview_with_table_keys_rejected():
    with pytest.raises(EventValidationError):
        validate(
            "session_started",
            {
                "mode": "interview",
                "frame": None,
                "code_hash": "x",
                "world_key": "fix",
                "package_manifest_hash": "y",
                "world_keys": ["alx", "desert"],
            },
        )


# --- the round event types ---


def test_turn_selected_shape():
    validate("turn_selected", {"round_no": 1, "position": 1, "world_key": "alx", "reason": "direct address", "degraded": False})
    with pytest.raises(EventValidationError):
        validate("turn_selected", {"round_no": 1, "world_key": "alx", "reason": "x", "degraded": False})  # missing position


def test_round_closed_shape_and_reasons():
    for reason in ("selector_closed", "cap", "floor_unmet_exhausted"):
        validate("round_closed", {"round_no": 1, "reason": reason, "turns": 3})
    with pytest.raises(EventValidationError):
        validate("round_closed", {"round_no": 1, "reason": "tired", "turns": 3})


# --- the sealed entrance, table shape ---


def _open_table(store, sid, world_keys=("alx", "desert")):
    return open_session(
        store,
        session_id=sid,
        event_uuid=str(uuid.uuid4()),
        mode="table",
        frame=None,
        code_hash="abc123",
        world_keys=list(world_keys),
        package_manifest_hashes={k: f"sha256:{k}" for k in world_keys},
    )


def test_open_session_table_shape(tmp_path):
    store = Store(tmp_path / "events.db")
    sid = str(uuid.uuid4())
    _open_table(store, sid)
    state = project_fresh(sid, store)
    assert state.exists
    assert state.mode == "table"
    assert state.world_keys == ["alx", "desert"]
    assert state.package_manifest_hashes == {"alx": "sha256:alx", "desert": "sha256:desert"}
    # The singular fields stay None - exactly one shape is ever set.
    assert state.world_key is None
    assert state.package_manifest_hash is None


def test_open_session_table_seal_holds(tmp_path):
    store = Store(tmp_path / "events.db")
    sid = str(uuid.uuid4())
    _open_table(store, sid)
    with pytest.raises(SecondWriterError):
        _open_table(store, sid)


def test_open_session_refuses_wrong_shape(tmp_path):
    store = Store(tmp_path / "events.db")
    with pytest.raises(EventValidationError):
        open_session(
            store,
            session_id=str(uuid.uuid4()),
            event_uuid=str(uuid.uuid4()),
            mode="table",
            frame=None,
            code_hash="abc123",
            world_key="fix",
            package_manifest_hash="sha256:fix",
        )


# --- projection: round bookkeeping ---


def _voice(speaker, text="something true"):
    return {
        "speaker": speaker,
        "text": text,
        "citations": [],
        "glosses": [],
        "figures_used": [],
        "quote_offers": [],
        "attempts_meta": {},
        "output_defects": [],
    }


def test_round_lifecycle_folds(tmp_path):
    store = Store(tmp_path / "events.db")
    sid = str(uuid.uuid4())
    _open_table(store, sid)

    def append(event_type, payload):
        store.append(session_id=sid, event_uuid=str(uuid.uuid4()), event_type=event_type, payload=payload)

    append("participant_message", {"text": "what is prayer?", "client_msg_id": "m1"})
    state = project_fresh(sid, store)
    assert (state.round_no, state.round_open, state.round_turns) == (1, True, 0)

    append("turn_selected", {"round_no": 1, "position": 1, "world_key": "alx", "reason": "most directly positioned", "degraded": False})
    append("voice_turn", _voice("alx"))
    append("turn_selected", {"round_no": 1, "position": 2, "world_key": "desert", "reason": "breadth of voice", "degraded": False})
    append("voice_turn", _voice("desert"))
    state = project_fresh(sid, store)
    assert state.round_turns == 2
    assert state.round_speakers == ["alx", "desert"]
    assert state.round_open

    append("round_closed", {"round_no": 1, "reason": "selector_closed", "turns": 2})
    append("turn_committed", {"turn_no": 1})
    state = project_fresh(sid, store)
    assert not state.round_open
    assert state.turn_count == 1

    # The next participant message opens round 2 with fresh bookkeeping.
    append("participant_message", {"text": "and fasting?", "client_msg_id": "m2"})
    state = project_fresh(sid, store)
    assert (state.round_no, state.round_open, state.round_turns) == (2, True, 0)
    assert state.round_speakers == []
    # The transcript keeps every speaker across rounds - round state resets,
    # the record never does.
    assert [t["speaker"] for t in state.transcript] == ["participant", "alx", "desert", "participant"]


def test_interview_log_projects_unchanged(tmp_path):
    # An interview session written through the same entrance keeps its
    # singular fields and never grows round state (round bookkeeping is
    # table-only).
    store = Store(tmp_path / "events.db")
    sid = str(uuid.uuid4())
    open_session(
        store,
        session_id=sid,
        event_uuid=str(uuid.uuid4()),
        mode="interview",
        frame=None,
        code_hash="abc123",
        world_key="fix",
        package_manifest_hash="sha256:fix",
    )
    store.append(session_id=sid, event_uuid=str(uuid.uuid4()), event_type="participant_message", payload={"text": "hi", "client_msg_id": "m1"})
    store.append(session_id=sid, event_uuid=str(uuid.uuid4()), event_type="voice_turn", payload=_voice("fix"))
    state = project_fresh(sid, store)
    assert state.world_key == "fix"
    assert state.world_keys is None
    assert (state.round_no, state.round_open, state.round_turns) == (0, False, 0)
