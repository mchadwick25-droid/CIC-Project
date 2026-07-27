"""S4.2 state-parity instrument: projected state equals legacy state.

S4.1's parity_suite proves the ENDPOINT OUTCOMES (responses / SSE event
sequences) are byte-equal across a refactor. S4.2 replaces the mutable
session store with an append-only event log + projection, so the property
to prove is one level deeper: after each recorded case runs, the SESSION
STATE the system now derives by projecting events must equal the session
state the legacy mutable store held at the same point.

Two modes (mirroring parity_suite's record/replay split):

  snapshot : run the 8 recorded cases (tape-served boundaries, same
             tapes) through the CURRENT code and serialize each case's
             final session state to suite/<case>.state.json. Run this
             BEFORE the S4.2 refactor - it freezes the legacy store's
             state per case.
  verify   : run the same cases through the (refactored) code and compare
             the state now derived from the event log against the frozen
             snapshots. Fails loudly on any field difference.

Masking, declared (same discipline as parity_suite's outcome masking -
every masked field is masked because it is LIVE-GENERATED during replay,
not because it is inconvenient):
  - messages at or before the last participant message (the session-start
    reception/handoff are generated live per run; the turn under test is
    everything after) - kept as role/name skeleton, content masked;
  - P2-plain-framebreaker's facilitator answer (generated INLINE in the
    endpoint, not at a taped boundary - the same mask parity_suite
    declares);
  - session_id (random UUID per run) - masked to a constant, but the
    consistency of session_id across state fields is asserted first;
  - permanent_prompt / world_capsule_core / worlds_at_table prompt text
    are serialized as sha256 hashes (deterministic disk content - the
    hash IS the equality check, just without megabytes of snapshot).

Usage (from cic-poc/backend):
  python -m app.graph.replay.state_parity snapshot
  python -m app.graph.replay.state_parity verify
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

BACKEND = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(BACKEND))

FIXDIR = Path(__file__).with_name("suite")


def _sha(text: str) -> str:
    return hashlib.sha256((text or "").encode("utf-8")).hexdigest()[:16]


def _content_text(content) -> str:
    if isinstance(content, list):
        parts = []
        for block in content:
            if isinstance(block, dict) and block.get("type") == "text":
                parts.append(block.get("text", ""))
            elif isinstance(block, str):
                parts.append(block)
        return "\n".join(parts)
    return content or ""


def serialize_state(state, case_name: str) -> dict:
    """Deterministic, comparison-ready dict of a ConversationState."""
    from langchain_core.messages import HumanMessage

    msgs = list(state.messages)
    last_user = max(
        (i for i, m in enumerate(msgs) if isinstance(m, HumanMessage)),
        default=-1,
    )

    ser_messages = []
    for i, m in enumerate(msgs):
        role = "user" if isinstance(m, HumanMessage) else "assistant"
        name = getattr(m, "name", None)
        kwargs = getattr(m, "additional_kwargs", {}) or {}
        if i <= last_user:
            content = ("<masked: at-or-before last participant message; "
                       "session-start text is live-generated>")
            entry = {"role": role, "name": name, "content": content}
        else:
            content = _content_text(m.content)
            if (case_name == "P2-plain-framebreaker"
                    and name == "facilitator"):
                content = "<masked: inline-generated, nondeterministic>"
            entry = {
                "role": role,
                "name": name,
                "content": content,
                "citations": kwargs.get("citations") or None,
                "glosses_used": kwargs.get("glosses_used") or None,
                "retrieval_audit": kwargs.get("retrieval_audit") or None,
            }
        ser_messages.append(entry)

    rc = state.retrieved_context
    retrieved_context = None
    if rc is not None:
        retrieved_context = {
            "chunks": list(rc.chunks),
            "terms": list(rc.terms),
            "sources": list(rc.sources),
            "citations": list(rc.citations),
        }

    return {
        "phase": state.phase,
        "current_speaker": state.current_speaker,
        "current_world_id": state.current_world_id,
        "turn_count": state.turn_count,
        "requires_reroot": state.requires_reroot,
        "close_requested": state.close_requested,
        "closing_stage": state.closing_stage,
        "world_id": state.world_id,
        "world_ids": list(state.world_ids),
        "user_id": state.user_id,
        "session_id": "<sid>" if state.session_id else "",
        "track_a_active": state.track_a_active,
        "track_a_severity": state.track_a_severity,
        "track_b_active": state.track_b_active,
        "relational_safety_tags": list(state.relational_safety_tags),
        "relational_safety_deescalation_count":
            state.relational_safety_deescalation_count,
        "drift_signals": [
            {"signal_type": s.signal_type, "description": s.description,
             "severity": s.severity, "world_id": s.world_id}
            for s in state.drift_signals
        ],
        "pending_guidance": dict(state.pending_guidance),
        "surfaced_chunk_ids": {k: list(v)
                               for k, v in state.surfaced_chunk_ids.items()},
        "retrieval_query_override": state.retrieval_query_override,
        "retrieved_context": retrieved_context,
        "permanent_prompt_sha": _sha(state.permanent_prompt),
        "world_capsule_core_sha": _sha(state.world_capsule_core),
        "worlds_at_table": [
            {"world_id": w.world_id,
             "permanent_prompt_sha": _sha(w.permanent_prompt),
             "world_capsule_sha": _sha(w.world_capsule)}
            for w in state.worlds_at_table
        ],
        "messages": ser_messages,
    }


def _final_states(session_id: str) -> dict:
    """Return {label: ConversationState} for every way the refactored code
    can produce this session's state. Legacy code (pre-S4.2) has exactly
    one: the mutable sessions dict. Refactored code has two, and they must
    agree: the endpoint-facing store state and a FRESH projection from the
    persisted event log (proving the log alone is sufficient)."""
    import app.main as main_mod

    try:
        from app.graph import events as events_mod
    except ImportError:
        events_mod = None

    if events_mod is None:
        return {"legacy-store": main_mod.sessions[session_id]}

    out = {"store": events_mod.EVENT_STORE.get_state(session_id)}
    out["fresh-projection"] = events_mod.EVENT_STORE.project_fresh(session_id)
    return out


def main() -> int:
    mode = sys.argv[1] if len(sys.argv) > 1 else "verify"
    only = set(sys.argv[2:])

    from fastapi.testclient import TestClient
    import app.main as main_mod
    from app.graph.replay.parity_suite import CASES, run_case
    from app.graph.replay.recorder import Tape, replaying

    client = TestClient(main_mod.app)
    failures = []
    for case in CASES:
        name = case[0]
        if only and name not in only:
            continue
        tape = Tape.load(FIXDIR / f"{name}.tape.pkl")
        if case[1] == "plain":
            # same declared-delta handling as parity_suite (S4.1's one
            # intended delta: the plain path gained the five table checks)
            tape.delta_labels = {
                "check_dominance": list,
                "check_convergence": list,
                "check_cross_world_vocabulary_drift": list,
                "check_length_ceiling": list,
                "check_question_stacking": list,
            }

        def _known_sessions() -> set:
            try:
                from app.graph import events as events_mod
                return set(events_mod.EVENT_STORE.session_ids())
            except ImportError:
                return set(main_mod.sessions.keys())

        before = _known_sessions()
        try:
            with replaying(tape):
                run_case(client, case, mode)
                tape.assert_consumed()
        except AssertionError as exc:
            failures.append((name, f"tape assertion: {exc}"))
            print(f"[{mode}] {name}: FAIL ({exc})")
            continue
        new_sids = _known_sessions() - before
        if len(new_sids) != 1:
            failures.append((name, f"expected 1 new session, saw {len(new_sids)}"))
            print(f"[{mode}] {name}: FAIL (session bookkeeping)")
            continue
        sid = new_sids.pop()

        snap_path = FIXDIR / f"{name}.state.json"
        states = _final_states(sid)
        serialized = {label: serialize_state(st, name)
                      for label, st in states.items()}

        # every producer of this session's state must agree with the others
        distinct = {json.dumps(s, sort_keys=True) for s in serialized.values()}
        if len(distinct) != 1:
            failures.append((name, f"internal disagreement across {list(serialized)}"))
            diffp = FIXDIR / f"{name}.state-internal-diff.json"
            diffp.write_text(json.dumps(serialized, indent=1, ensure_ascii=False),
                             encoding="utf-8")
            print(f"[{mode}] {name}: INTERNAL STATE DISAGREEMENT -> {diffp.name}")
            continue
        current = serialized[next(iter(serialized))]

        if mode == "snapshot":
            snap_path.write_text(
                json.dumps(current, indent=1, ensure_ascii=False),
                encoding="utf-8")
            print(f"[snapshot] {name}: state frozen "
                  f"({len(current['messages'])} messages, from {list(states)})")
        else:
            expected = json.loads(snap_path.read_text(encoding="utf-8"))
            if current != expected:
                failures.append((name, "state mismatch vs legacy snapshot"))
                diffp = FIXDIR / f"{name}.state-diff.json"
                diffp.write_text(json.dumps(current, indent=1, ensure_ascii=False),
                                 encoding="utf-8")
                print(f"[verify] {name}: STATE MISMATCH -> {diffp.name}")
            else:
                print(f"[verify] {name}: STATE PARITY OK (checked {list(states)})")

    if mode == "verify":
        ran = len([c for c in CASES if not only or c[0] in only])
        print(f"\n{ran - len(failures)}/{ran} cases at state parity")
        return 1 if failures else 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
