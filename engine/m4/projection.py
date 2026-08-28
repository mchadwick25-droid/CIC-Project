"""project_fresh(): folds the append-only log into a state object - "a
fresh state object per request, never a shared mutable instance" (Artifact-3
SS2). This is the ONLY way session state is ever read; nothing in this
build keeps a session in memory across calls. Tested (stage 5) by
reconstructing full fidelity, including the safety accumulator, from a
brand-new Store instance pointed at the same backing file - the literal
"resume across two processes" gate item.
"""
from dataclasses import dataclass, field

from .store import Store, StoredEvent


@dataclass
class SafetyState:
    # each safety_state event already carries the FULL current accumulator
    # value (the writer computed it once, appended the fact) - folding is
    # "take the latest per track," never a manual re-summation here. Track A
    # (acute) acts on the single message and doesn't accumulate; Track B
    # (harmful-dynamic/dependency) does, and reload-from-log is what makes
    # "never silently zeroed" (spec SS8) true across a resume.
    track_a_last: dict | None = None
    track_b_accumulator: dict | None = None


@dataclass
class SessionState:
    session_id: str
    exists: bool = False
    world_key: str | None = None
    mode: str | None = None
    frame: str | None = None
    code_hash: str | None = None
    package_manifest_hash: str | None = None
    # Table mode (Artifact-7 SS1-2). world_keys/package_manifest_hashes are
    # the table's counterparts to the two singular fields above - exactly
    # one pair is ever set, per the event schema's mode-shape rule. The
    # round_* fields are the open round's own state, folded from
    # participant_message / turn_selected / voice_turn / round_closed so a
    # turn-at-a-time continue served by a different process resumes the same
    # round (Artifact-7 SS6) - never held in memory between requests.
    world_keys: list[str] | None = None
    package_manifest_hashes: dict[str, str] | None = None
    round_no: int = 0
    round_open: bool = False
    round_turns: int = 0
    round_speakers: list[str] = field(default_factory=list)
    transcript: list[dict] = field(default_factory=list)
    turn_count: int = 0
    last_turn_no: int | None = None
    safety: SafetyState = field(default_factory=SafetyState)
    pressed: dict[str, bool] = field(default_factory=lambda: {"later_age": False, "other_tradition": False})
    degraded_turn_count: int = 0
    resumed_count: int = 0
    closed: bool = False
    close_reason: str | None = None
    deletion_requested: bool = False
    raw_events: list[StoredEvent] = field(default_factory=list)


def _fold(session_id: str, events: list[StoredEvent]) -> SessionState:
    state = SessionState(session_id=session_id, raw_events=events)
    if not events:
        return state
    state.exists = True
    for event in events:
        payload = event.payload
        if event.event_type == "session_started":
            state.mode = payload["mode"]
            state.frame = payload["frame"]
            state.code_hash = payload["code_hash"]
            if payload["mode"] == "table":
                state.world_keys = list(payload["world_keys"])
                state.package_manifest_hashes = dict(payload["package_manifest_hashes"])
            else:
                state.world_key = payload["world_key"]
                state.package_manifest_hash = payload["package_manifest_hash"]
        elif event.event_type == "participant_message":
            state.transcript.append({"speaker": "participant", "text": payload["text"]})
            if state.mode == "table":
                # A participant message opens the next round (Artifact-7
                # SS2). A message arriving with a round somehow still open
                # closes nothing here - the fold records what the log says,
                # and the round loop is what refuses that sequence.
                state.round_no += 1
                state.round_open = True
                state.round_turns = 0
                state.round_speakers = []
        elif event.event_type == "facilitator_turn":
            state.transcript.append({"speaker": "facilitator", "kind": payload["kind"], "text": payload["text"]})
        elif event.event_type == "voice_turn":
            state.transcript.append(
                {
                    "speaker": payload["speaker"],
                    "text": payload["text"],
                    "citations": payload["citations"],
                    "glosses": payload["glosses"],
                    "figures_used": payload["figures_used"],
                }
            )
            if state.mode == "table" and state.round_open:
                state.round_turns += 1
                state.round_speakers.append(payload["speaker"])
        elif event.event_type == "round_closed":
            state.round_open = False
        elif event.event_type == "gate_decision":
            if payload.get("degraded"):
                state.degraded_turn_count += 1
        elif event.event_type == "safety_state":
            if payload["track"] == "A":
                state.safety.track_a_last = payload
            else:
                state.safety.track_b_accumulator = payload["accumulator"]
        elif event.event_type == "escalation_pressed":
            state.pressed[payload["class"]] = True
        elif event.event_type == "turn_committed":
            state.turn_count += 1
            state.last_turn_no = payload["turn_no"]
        elif event.event_type == "session_resumed":
            state.resumed_count += 1
        elif event.event_type == "deletion_requested":
            state.deletion_requested = True
        elif event.event_type == "session_closed":
            state.closed = True
            state.close_reason = payload["reason"]
    return state


def project_fresh(session_id: str, store: Store) -> SessionState:
    """Every call re-reads the store and re-folds from scratch - the
    'no process-local session state' guarantee, not an optimization to
    relax later."""
    events = store.read_events(session_id)
    return _fold(session_id, events)
