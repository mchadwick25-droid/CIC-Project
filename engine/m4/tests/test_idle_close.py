"""Daily idle-close sweep (engine/m4/idle_close.py): the timing math and
close_idle_sessions' own selection logic against a constructed event log.
Not covered here: the background thread itself actually firing on a real
clock - that's exercised by construction (a plain threading.Thread
sleeping a computed duration), not something worth a slow or flaky test
(same discipline engine/m7/tests/test_scheduler.py already holds itself
to for its own, structurally identical scheduler).

Store.append always stamps created_at with the real wall clock (Artifact-3
SS1 - no caller-injectable timestamp), so every test below anchors its own
`now` off datetime.now(timezone.utc) at test-run time, offset by however
old a session needs to look, rather than a fixed calendar date that would
drift stale as soon as "today" moves past it.
"""
import uuid
from datetime import datetime, timedelta, timezone

from engine.m4.idle_close import _next_run_at, close_idle_sessions
from engine.m4.projection import project_fresh
from engine.m4.store import Store


def _append(store, sid, etype, payload):
    store.append(session_id=sid, event_uuid=str(uuid.uuid4()), event_type=etype, payload=payload)


def _start_session(store, sid):
    _append(store, sid, "session_started", {
        "mode": "interview", "frame": "general_seeker", "code_hash": "abc",
        "world_key": "fix", "package_manifest_hash": "sha256:x",
    })


def test_next_run_at_today_if_not_yet_passed():
    now = datetime(2026, 9, 6, 1, 0, tzinfo=timezone.utc)
    assert _next_run_at(now, hour=4, minute=5) == datetime(2026, 9, 6, 4, 5, tzinfo=timezone.utc)


def test_next_run_at_tomorrow_if_already_passed():
    now = datetime(2026, 9, 6, 5, 0, tzinfo=timezone.utc)
    assert _next_run_at(now, hour=4, minute=5) == datetime(2026, 9, 7, 4, 5, tzinfo=timezone.utc)


def test_closes_a_session_quiet_past_the_threshold(tmp_path):
    store = Store(tmp_path / "events.db")
    _start_session(store, "old")
    sweep_now = datetime.now(timezone.utc) + timedelta(days=8)

    closed = close_idle_sessions(store, now=sweep_now, idle_after=timedelta(days=7))

    assert closed == ["old"]
    state = project_fresh("old", store)
    assert state.closed is True
    assert state.close_reason == "idle"


def test_leaves_a_recently_active_session_alone(tmp_path):
    store = Store(tmp_path / "events.db")
    _start_session(store, "recent")
    sweep_now = datetime.now(timezone.utc)

    closed = close_idle_sessions(store, now=sweep_now, idle_after=timedelta(days=7))

    assert closed == []
    assert project_fresh("recent", store).closed is False


def test_never_touches_an_already_closed_session(tmp_path):
    store = Store(tmp_path / "events.db")
    _start_session(store, "capped")
    _append(store, "capped", "session_closed", {"reason": "cap"})
    sweep_now = datetime.now(timezone.utc) + timedelta(days=30)

    closed = close_idle_sessions(store, now=sweep_now, idle_after=timedelta(days=7))

    assert closed == []
    events_after = [e.event_type for e in store.read_events("capped")]
    assert events_after.count("session_closed") == 1


def test_sweep_is_a_no_op_on_a_session_it_already_idle_closed(tmp_path):
    store = Store(tmp_path / "events.db")
    _start_session(store, "old")
    base = datetime.now(timezone.utc)

    first = close_idle_sessions(store, now=base + timedelta(days=8), idle_after=timedelta(days=7))
    second = close_idle_sessions(store, now=base + timedelta(days=15), idle_after=timedelta(days=7))

    assert first == ["old"]
    assert second == []
    events_after = [e.event_type for e in store.read_events("old")]
    assert events_after.count("session_closed") == 1
