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
    store.append(session_id=sid, event_uuid=str(uuid.uuid4()), event_type="voice_turn", payload={"speaker": "Vera", "text": "I did not see him myself...", "citations": ["fix.source.witness-scroll"], "glosses": [], "figures_used": [], "quote_offers": [], "attempts_meta": {}})
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


def test_idle_close_reads_closed_until_real_activity_reopens_it(tmp_path):
    """engine.m4.idle_close's own reporting-only contract, at the fold
    level: an idle close reads exactly like any other close until a real
    event follows it, at which point it reopens - unlike a cap/participant
    close, which a resumed session should never be able to shake."""
    store = Store(tmp_path / "events.db")
    sid = str(uuid.uuid4())
    _seed(store, sid)
    store.append(session_id=sid, event_uuid=str(uuid.uuid4()), event_type="session_closed", payload={"reason": "idle"})

    idle_state = project_fresh(sid, store)
    assert idle_state.closed is True
    assert idle_state.close_reason == "idle"

    # A participant resumes: one more real event lands after the idle
    # close.
    store.append(session_id=sid, event_uuid=str(uuid.uuid4()), event_type="participant_message", payload={"text": "still there?", "client_msg_id": "m2"})

    resumed_state = project_fresh(sid, store)
    assert resumed_state.closed is False
    assert resumed_state.close_reason is None


def test_cap_close_never_reopens(tmp_path):
    store = Store(tmp_path / "events.db")
    sid = str(uuid.uuid4())
    _seed(store, sid)
    store.append(session_id=sid, event_uuid=str(uuid.uuid4()), event_type="session_closed", payload={"reason": "cap"})
    store.append(session_id=sid, event_uuid=str(uuid.uuid4()), event_type="participant_message", payload={"text": "still there?", "client_msg_id": "m2"})

    state = project_fresh(sid, store)
    assert state.closed is True
    assert state.close_reason == "cap"


def test_voice_turn_transparency_plan_folds_into_transcript(tmp_path):
    """Build-Plan.md Stage 3b: the transparency plan attached to a
    voice_turn event (engine.m4.transparency_plan, Stage 3a) has to
    reach state.transcript for a replayed session to carry it, same as
    citations/glosses/figures_used already do - this is the one place
    Stage 3a's addition wasn't wired through yet."""
    store = Store(tmp_path / "events.db")
    sid = str(uuid.uuid4())
    _seed(store, sid)
    plan = {"world_key": "fix", "anchors": [{"record_id": "fix.source.witness-scroll"}], "references": [], "unverified_claims": {"count": 0, "sentence_indexes": []}}
    store.append(
        session_id=sid,
        event_uuid=str(uuid.uuid4()),
        event_type="voice_turn",
        payload={"speaker": "Vera", "text": "Again.", "citations": [], "glosses": [], "figures_used": [], "quote_offers": [], "attempts_meta": {}, "transparency": plan},
    )

    state = project_fresh(sid, store)
    voice_entries = [t for t in state.transcript if t["speaker"] == "Vera"]
    assert voice_entries[0]["transparency"] is None  # the seeded turn, logged before this field existed
    assert voice_entries[1]["transparency"] == plan


def test_bridge_facilitator_turn_carries_modern_terms_through_a_fold(tmp_path):
    """OG-13 (worlds/pahc/Open_Gaps_Tracking.md): a bridge turn's own
    modern_terms cards used to vanish on reload/resume - projection.py
    rebuilt the facilitator entry from only {speaker, kind, text},
    dropping any other payload key. A participant who saw the card live,
    then reloaded the page, would lose it."""
    store = Store(tmp_path / "events.db")
    sid = str(uuid.uuid4())
    _seed(store, sid)
    card = {"record_id": "_fleet.modern.trinity", "record_type": "modern_term", "label": "Trinity", "sources": [], "modern_sense": "One God, three persons.", "distinguishing_claim": "The word is modern; the claim is not."}
    store.append(
        session_id=sid,
        event_uuid=str(uuid.uuid4()),
        event_type="facilitator_turn",
        payload={"kind": "bridge", "text": "Let me put that in plain terms.", "modern_terms": [card]},
    )

    state = project_fresh(sid, store)
    bridge_entries = [t for t in state.transcript if t["speaker"] == "facilitator" and t["kind"] == "bridge"]
    assert bridge_entries[0]["modern_terms"] == [card]


def test_non_bridge_facilitator_turn_folds_with_modern_terms_none(tmp_path):
    """A facilitator_turn logged before this key existed (or of any kind
    other than "bridge") has no 'modern_terms' key at all - the fold
    must not KeyError on it, the same pre-change-transcript guarantee
    test_voice_turn_without_transparency_key_still_folds_cleanly already
    pins for voice_turn."""
    store = Store(tmp_path / "events.db")
    sid = str(uuid.uuid4())
    _seed(store, sid)  # _seed's own facilitator-turn-free; add one with no modern_terms key
    store.append(
        session_id=sid,
        event_uuid=str(uuid.uuid4()),
        event_type="facilitator_turn",
        payload={"kind": "close", "text": "This conversation is closed."},
    )

    state = project_fresh(sid, store)
    facilitator_entries = [t for t in state.transcript if t["speaker"] == "facilitator"]
    assert len(facilitator_entries) == 1
    assert facilitator_entries[0]["modern_terms"] is None


def test_voice_turn_without_transparency_key_still_folds_cleanly(tmp_path):
    """A voice_turn logged before Stage 3a existed has no 'transparency'
    key at all (it was never added to events.REQUIRED_KEYS) - the fold
    must not KeyError on it. This is Build-Plan.md's own Stage 3b
    acceptance criterion: 'pre-change transcripts still load.'"""
    store = Store(tmp_path / "events.db")
    sid = str(uuid.uuid4())
    _seed(store, sid)  # _seed's own voice_turn payload carries no "transparency" key

    state = project_fresh(sid, store)
    voice_entries = [t for t in state.transcript if t["speaker"] == "Vera"]
    assert len(voice_entries) == 1
    assert voice_entries[0]["transparency"] is None
