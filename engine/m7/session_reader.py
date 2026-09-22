"""The reader half of M7 (Artifact-8 §2): one session's event stream,
collected into the shape the instruments consume. Read-only over the M4
store; never writes, never calls a provider. This module is deliberately
dumb - it collects what the log says and attaches nothing the log doesn't
carry. Judgment lives in instruments.py; prose lives in report.py.

This is where the four formerly-unread outputs acquire their reader
(Artifact-8 §1): voice_turn.grounding, voice_turn.do_not_voice_violation,
voice_turn.output_defects, round_closed.governance - each is lifted off
its event verbatim and handed to the instruments.
"""
from dataclasses import dataclass, field

from engine.m4.store import Store


@dataclass
class VoiceTurnRecord:
    seq: int
    speaker: str
    text: str
    citations: list
    grounding: dict | None
    output_defects: list
    do_not_voice_violation: object
    degraded_by_net: bool
    round_no: int | None  # table mode only
    # Stage 6d / R17 (Rulings-Pending.md): lifted verbatim off the
    # voice_turn event's own payload (engine/m4/turn.py's voice_event),
    # same as citations above - the source data behind the
    # level1_element_density instrument's count.
    figures_used: list = field(default_factory=list)
    glosses: list = field(default_factory=list)
    transparency: dict | None = None


@dataclass
class AuditSession:
    session_id: str
    mode: str
    world_keys: list[str]           # one entry for an interview
    closed: bool
    close_reason: str | None
    participant_messages: list[dict] = field(default_factory=list)  # {"seq", "text"} - operator-only (Artifact-8 §4)
    gate_decisions: list[dict] = field(default_factory=list)        # payloads verbatim, with "seq"
    voice_turns: list[VoiceTurnRecord] = field(default_factory=list)
    facilitator_turns: list[dict] = field(default_factory=list)     # {"seq", "kind", "text"}
    safety_states: list[dict] = field(default_factory=list)
    turn_selected: list[dict] = field(default_factory=list)
    rounds_closed: list[dict] = field(default_factory=list)         # governance rides here when present
    event_count: int = 0
    first_at: str | None = None
    last_at: str | None = None


def read_session(store: Store, session_id: str) -> AuditSession | None:
    events = store.read_events(session_id)
    if not events:
        return None
    mode, world_keys, closed, close_reason = "interview", [], False, None
    session = None
    current_round: int | None = None
    for ev in events:
        p = ev.payload
        if ev.event_type == "session_started":
            mode = p.get("mode", "interview")
            world_keys = list(p.get("world_keys") or ([p["world_key"]] if p.get("world_key") else []))
            session = AuditSession(session_id=session_id, mode=mode, world_keys=world_keys, closed=False, close_reason=None)
            session.first_at = ev.created_at
        if session is None:
            # A log that doesn't start with session_started is itself a
            # finding; collect it as a bare session so nothing is dropped.
            session = AuditSession(session_id=session_id, mode="unknown", world_keys=[], closed=False, close_reason=None)
            session.first_at = ev.created_at
        session.event_count += 1
        session.last_at = ev.created_at
        if session.closed and session.close_reason == "idle" and ev.event_type != "session_closed":
            # Mirrors engine.m4.projection._fold's identical reopen rule
            # (2026-09-06): an idle close is reporting-only, and real
            # activity after one un-marks it - this reader must agree with
            # that fold, or a resumed session would read "closed (idle)"
            # here (engine.api.wiring.get_pilot_summary's own source) while
            # reading open everywhere a participant or the API actually
            # looks. A cap/participant close is never reopened this way.
            session.closed = False
            session.close_reason = None
        if ev.event_type == "participant_message":
            session.participant_messages.append({"seq": ev.seq, "text": p.get("text", "")})
        elif ev.event_type == "gate_decision":
            session.gate_decisions.append({"seq": ev.seq, **p})
        elif ev.event_type == "turn_selected":
            current_round = p.get("round_no")
            session.turn_selected.append({"seq": ev.seq, **p})
        elif ev.event_type == "voice_turn":
            session.voice_turns.append(
                VoiceTurnRecord(
                    seq=ev.seq,
                    speaker=p.get("speaker", ""),
                    text=p.get("text", ""),
                    citations=p.get("citations") or [],
                    grounding=p.get("grounding"),
                    output_defects=p.get("output_defects") or [],
                    do_not_voice_violation=p.get("do_not_voice_violation"),
                    degraded_by_net=bool(p.get("degraded_by_net")),
                    round_no=current_round if mode == "table" else None,
                    figures_used=p.get("figures_used") or [],
                    glosses=p.get("glosses") or [],
                    transparency=p.get("transparency"),
                )
            )
        elif ev.event_type == "facilitator_turn":
            session.facilitator_turns.append({"seq": ev.seq, "kind": p.get("kind"), "text": p.get("text", "")})
        elif ev.event_type == "safety_state":
            session.safety_states.append({"seq": ev.seq, **p})
        elif ev.event_type == "round_closed":
            current_round = None
            session.rounds_closed.append({"seq": ev.seq, **p})
        elif ev.event_type == "session_closed":
            session.closed = True
            session.close_reason = p.get("reason")
    return session
