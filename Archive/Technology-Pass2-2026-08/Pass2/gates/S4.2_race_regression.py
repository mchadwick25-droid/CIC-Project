"""S4.2 G checkpoint - the read-modify-write race, reproduced as a fixture.

The blueprint's requirement: "the read-modify-write race's regression
test - the hand-patched merge case reproduced as a fixture."

Three parts, all deterministic:

PART A (non-vacuous proof, legacy semantics reproduced):
  A1. The PRE-patch blind overwrite - the historical bug the hand-patched
      merge was written to fix: the background tail writes its stale
      state snapshot back to the store, clobbering a participant message
      that arrived after 'done' went out. The fixture reproduces the loss.
  A2. The residual lost-update the hand-patched merge still carried -
      the merge's own read-latest -> mutate -> write-back cycle (quoted
      verbatim from the pre-S4.2 code, git df04f30
      cic-poc/backend/app/graph/governance.py) loses one writer's drift
      signals when two governance writers interleave read/read/write/
      write. The fixture reproduces the loss.
  Both A cases MUST show the defect - a gate that can't reproduce the
  disease can't certify the cure (same discipline as S1.1a's
  gate-failure proof and S1.3's seeded defects).

PART B (the cure, against the REAL refactored code):
  B1. The A1 schedule against the real EventStore + the real
      run_post_round_governance: a participant message appended while
      the tail is mid-flight (thread synchronization via events, not
      sleeps - deterministic). Nothing is lost.
  B2. The A2 schedule: two real governance tails running concurrently,
      both held mid-flight together, then released. Both writers' drift
      signals land.
  The LLM-dependent leaf calls (check_drift_for_message,
  generate_reroot_guidance) are stubbed with fixed deterministic values -
  the property under test is the STORE WRITE DISCIPLINE, not the
  classifiers, and the race lives entirely in the write path.

PART C (structural): the refactored governance tail has no session-store
  read-modify-write left to race - asserted against its source text and
  signature (no `sessions` parameter; no `sessions[`/`sessions.get`).

Determinism: the whole gate runs twice; the two result summaries must be
byte-identical.

Usage (from cic-poc/backend):
  python <repo>/Ministry/Technology/Pass2/gates/S4.2_race_regression.py
"""
from __future__ import annotations

import inspect
import json
import sys
import threading
from pathlib import Path

BACKEND = Path(__file__).resolve().parents[4] / "cic-poc" / "backend"
sys.path.insert(0, str(BACKEND))


# --------------------------------------------------------------------------
# PART A - legacy semantics, reproduced
# --------------------------------------------------------------------------

def part_a1_blind_overwrite() -> dict:
    """Pre-patch tail: writes its stale snapshot back. The message that
    arrived after 'done' must be lost for this fixture to pass."""
    sessions = {}
    sessions["s"] = {"messages": ["m1"], "drift_signals": []}

    # endpoint: round commits, 'done' goes out; tail holds a STALE snapshot
    stale = {"messages": list(sessions["s"]["messages"]),
             "drift_signals": list(sessions["s"]["drift_signals"])}

    # a new participant message arrives AFTER 'done', BEFORE the tail writes
    sessions["s"] = {"messages": sessions["s"]["messages"] + ["m2-late"],
                     "drift_signals": list(sessions["s"]["drift_signals"])}

    # pre-patch tail: blind overwrite with the stale snapshot + its finding
    stale["drift_signals"] = stale["drift_signals"] + ["tail-signal"]
    sessions["s"] = stale

    lost = "m2-late" not in sessions["s"]["messages"]
    return {"case": "A1-blind-overwrite",
            "late_message_lost": lost,
            "defect_reproduced": lost}


def part_a2_merge_lost_update() -> dict:
    """The hand-patched merge itself (verbatim shape from git df04f30,
    app/graph/governance.py lines 233-239):

        latest_state = sessions.get(session_id)
        if latest_state is not None:
            latest_state.drift_signals = (
                list(latest_state.drift_signals) + new_drift_signals)
            latest_state.pending_guidance = {
                **latest_state.pending_guidance, **new_pending_guidance}
            sessions[session_id] = latest_state

    Two writers interleaved read/read/write/write: writer 1's signals
    must be lost for this fixture to pass. (dict-value semantics stand in
    for the dataclass - the read-copy-write cycle is identical.)"""
    sessions = {"s": {"drift_signals": ["existing"], "pending_guidance": {}}}

    def merge(read_snapshot, new_signals, new_guidance):
        latest_state = read_snapshot          # the READ half, already taken
        if latest_state is not None:
            latest_state = dict(latest_state)
            latest_state["drift_signals"] = (
                list(latest_state["drift_signals"]) + new_signals)
            latest_state["pending_guidance"] = {
                **latest_state["pending_guidance"], **new_guidance}
            sessions["s"] = latest_state      # the WRITE half

    # schedule: both writers read latest, THEN both write (read/read/write/write)
    read_1 = sessions["s"]
    read_2 = sessions["s"]
    merge(read_1, ["writer1-signal"], {"desert-monasticism": "g1"})
    merge(read_2, ["writer2-signal"], {})

    final = sessions["s"]["drift_signals"]
    lost = "writer1-signal" not in final and "writer2-signal" in final
    return {"case": "A2-merge-lost-update",
            "final_signals": final,
            "writer1_lost": lost,
            "defect_reproduced": lost}


# --------------------------------------------------------------------------
# PART B - the refactored path, real code, same schedules
# --------------------------------------------------------------------------

def _fresh_session(events_mod, sid: str):
    events_mod.EVENT_STORE.append_many(sid, [
        ("session_started", {"user_id": None,
                             "world_id": "desert-monasticism",
                             "world_ids": ["desert-monasticism"]}),
        ("participant_message", {"text": "opening question",
                                 "name": None, "addressee": None}),
        ("spoken_message", {"name": "papnoute", "text": "an answer",
                            "addressee": None, "citations": None,
                            "glosses_used": None, "retrieval_audit": None}),
        ("turn_committed", {"phase": "active_encounter", "turn_count": 1,
                            "current_world_id": "desert-monasticism"}),
    ])


def _run_real_tail(sid: str, signal_desc: str, hold: threading.Event,
                   release: threading.Event):
    """Run the REAL run_post_round_governance with deterministic stubs for
    its two LLM-dependent leaf calls. `hold` is set once the tail is
    mid-flight (inside the stubbed classifier); it then waits on
    `release` - the fixture's deterministic interleave point."""
    from app.graph import governance, nodes
    from app.graph.events import EVENT_STORE
    from app.graph.state import DriftSignal
    from langchain_core.messages import AIMessage

    real_check = nodes.check_drift_for_message
    real_guidance = nodes.generate_reroot_guidance

    def stub_check(world_id, content):
        hold.set()
        release.wait(timeout=30)
        return DriftSignal(signal_type="smoothing", description=signal_desc,
                           severity="medium", world_id=world_id)

    def stub_guidance(signal):
        return f"guidance for: {signal.description}"

    nodes.check_drift_for_message = stub_check
    nodes.generate_reroot_guidance = stub_guidance
    try:
        governance.run_post_round_governance(
            EVENT_STORE.get_state(sid), "the participant's message",
            working_messages=[AIMessage(content="an answer", name="papnoute")],
            spoken_this_round=["desert-monasticism"],
            turns_completed=1,
            world_ids=["desert-monasticism"],
            is_multi_world=False,
            should_check_wind_down=False,
            session_id=sid,
        )
    finally:
        nodes.check_drift_for_message = real_check
        nodes.generate_reroot_guidance = real_guidance


def part_b1_message_during_tail() -> dict:
    """A1's schedule on the new path: participant message appended while
    the real tail is mid-flight. Both must survive."""
    from app.graph import events as events_mod
    sid = "gate-s42-race-b1"
    events_mod.EVENT_STORE._events.pop(sid, None)
    jl = events_mod._events_dir() / f"{sid}.jsonl"
    if jl.exists():
        jl.unlink()
    _fresh_session(events_mod, sid)

    hold, release = threading.Event(), threading.Event()
    t = threading.Thread(target=_run_real_tail,
                         args=(sid, "b1-tail-signal", hold, release))
    t.start()
    assert hold.wait(timeout=30), "tail never reached the interleave point"
    # the late message lands while the tail is mid-flight
    events_mod.EVENT_STORE.append(sid, "participant_message",
                                  {"text": "late message after done",
                                   "name": None, "addressee": None})
    release.set()
    t.join(timeout=30)

    state = events_mod.EVENT_STORE.get_state(sid)
    texts = [getattr(m, "content", "") for m in state.messages]
    descs = [s.description for s in state.drift_signals]
    ok = ("late message after done" in texts) and ("b1-tail-signal" in descs)
    return {"case": "B1-message-during-tail",
            "late_message_survives": "late message after done" in texts,
            "tail_signal_survives": "b1-tail-signal" in descs,
            "guidance_queued": dict(state.pending_guidance),
            "pass": ok}


def part_b2_concurrent_tails() -> dict:
    """A2's schedule on the new path: two real tails held mid-flight
    together, then released. Both writers' signals must land."""
    from app.graph import events as events_mod
    sid = "gate-s42-race-b2"
    events_mod.EVENT_STORE._events.pop(sid, None)
    jl = events_mod._events_dir() / f"{sid}.jsonl"
    if jl.exists():
        jl.unlink()
    _fresh_session(events_mod, sid)

    # Two tails, each with its own hold/release pair, both mid-flight
    # before either is released - the read/read/write/write schedule.
    # (Stubs patch the same module attribute, so the second patch must
    # happen only after the first tail is already past it: tail 1 is
    # held INSIDE its stub before tail 2's patch replaces it.)
    h1, r1 = threading.Event(), threading.Event()
    h2, r2 = threading.Event(), threading.Event()
    t1 = threading.Thread(target=_run_real_tail,
                          args=(sid, "b2-writer1", h1, r1))
    t1.start()
    assert h1.wait(timeout=30)
    t2 = threading.Thread(target=_run_real_tail,
                          args=(sid, "b2-writer2", h2, r2))
    t2.start()
    assert h2.wait(timeout=30)
    r1.set()
    t1.join(timeout=30)
    r2.set()
    t2.join(timeout=30)

    state = events_mod.EVENT_STORE.get_state(sid)
    descs = [s.description for s in state.drift_signals]
    ok = "b2-writer1" in descs and "b2-writer2" in descs
    return {"case": "B2-concurrent-tails",
            "final_signals": descs,
            "both_writers_survive": ok,
            "pass": ok}


# --------------------------------------------------------------------------
# PART C - structural: nothing left to race
# --------------------------------------------------------------------------

def part_c_structural() -> dict:
    from app.graph import governance
    sig = inspect.signature(governance.run_post_round_governance)
    src = inspect.getsource(governance.run_post_round_governance)
    no_sessions_param = "sessions" not in sig.parameters
    no_rmw = ("sessions[" not in src and "sessions.get" not in src)
    return {"case": "C-structural",
            "no_sessions_parameter": no_sessions_param,
            "no_store_read_modify_write": no_rmw,
            "pass": no_sessions_param and no_rmw}


def run_once() -> dict:
    a1 = part_a1_blind_overwrite()
    a2 = part_a2_merge_lost_update()
    b1 = part_b1_message_during_tail()
    b2 = part_b2_concurrent_tails()
    c = part_c_structural()
    all_pass = (a1["defect_reproduced"] and a2["defect_reproduced"]
                and b1["pass"] and b2["pass"] and c["pass"])
    return {"A1": a1, "A2": a2, "B1": b1, "B2": b2, "C": c,
            "gate": "PASS" if all_pass else "FAIL"}


def main() -> int:
    r1 = run_once()
    r2 = run_once()
    s1 = json.dumps(r1, sort_keys=True)
    s2 = json.dumps(r2, sort_keys=True)
    print(json.dumps(r1, indent=1))
    print(f"\ndouble-run byte-identical: {s1 == s2}")
    print(f"GATE: {r1['gate']}")
    return 0 if (r1["gate"] == "PASS" and s1 == s2) else 1


if __name__ == "__main__":
    sys.exit(main())
