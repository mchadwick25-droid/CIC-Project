"""Pure orchestration layer for the minimal test backend (see
/root/.claude/plans/linear-popping-dawn.md) - no FastAPI import here, so this
is testable directly against a real Store/LazyWorldLoader with a fake Bedrock
client, no HTTP involved. engine.m4.turn.run_turn() has zero side effects by
design (see its own module docstring) - everything below is this module
owning the event-log/usage-log writes run_turn() deliberately leaves to its
caller.
"""
import uuid
from dataclasses import dataclass

from engine.api.config import REPO_ROOT
from engine.m1.loader import load_fleet_records
from engine.m4 import events, session_code
from engine.m4.entrance import open_session
from engine.m4.projection import SessionState, project_fresh
from engine.m4.store import Store
from engine.m4.turn import TurnResult, UnhandledRoutingAction, run_turn
from engine.m4.world_loader import LazyWorldLoader, LoadedWorld
from engine.m5.anachronism import anachronistic_term_ids as compute_anachronistic_term_ids
from engine.m8.log_store import UsageLogStore

UNHANDLED_ROUTING_FACILITATOR_TEXT = (
    "This kind of turn isn't wired up to generate a response yet in this test build "
    "(the routing gate itself worked correctly - the Facilitator just has no scripted "
    "content for this branch). Your message was recorded; try rephrasing, or see "
    "engine/api/README.md for the known gap."
)


class UnknownWorldError(Exception):
    """world_key isn't in the registry (records/worlds.yaml)."""


class SessionNotFound(Exception):
    """No session_started event exists for this session_id."""


class ProviderCallFailed(Exception):
    """run_turn() raised something other than UnhandledRoutingAction - most
    likely a real Bedrock/credential failure. The participant_message event
    (if this happened mid-message) is already committed; nothing else is."""


@dataclass(frozen=True)
class MessageResult:
    turn_no: int
    routing_action: str | None
    routing_reason: str
    degraded: bool
    unhandled_routing_gap: bool
    facilitator: dict | None
    voice: dict | None


def _load_world(world_loader: LazyWorldLoader, registry: dict, world_key: str, *, expected_manifest_hash: str | None = None) -> LoadedWorld:
    entry = registry.get(world_key)
    if entry is None:
        raise UnknownWorldError(world_key)
    package_dir = REPO_ROOT / entry["package"]["location"]
    world, _timing = world_loader.load(
        world_key, package_dir=package_dir, expected_manifest_hash=expected_manifest_hash or entry["package"]["manifest_hash"]
    )
    return world


def create_session(*, store: Store, world_loader: LazyWorldLoader, registry: dict, world_key: str) -> tuple[str, str]:
    """Returns (session_id, raw_code). The raw code is returned exactly once
    - only its hash is ever stored (engine.m4.session_code)."""
    world = _load_world(world_loader, registry, world_key)
    session_id = str(uuid.uuid4())
    raw_code = session_code.generate_code()
    open_session(
        store,
        session_id=session_id,
        event_uuid=str(uuid.uuid4()),
        world_key=world_key,
        mode="interview",
        frame=None,
        code_hash=session_code.hash_code(raw_code),
        package_manifest_hash=world.manifest_hash,
    )
    return session_id, raw_code


def get_transcript(store: Store, session_id: str) -> SessionState:
    state = project_fresh(session_id, store)
    if not state.exists:
        raise SessionNotFound(session_id)
    return state



def _replay_text(entry: dict) -> str:
    """One past voice turn as the model should hear itself say it: every
    sentence it wrote, with the citations that VERIFIED re-attached.

    The tags have to go back on. Measured over a six-turn live conversation
    on desert: the voice cited 9 sentences on turn 1 and 6 on turn 2, then
    0, 0, 0, 0. From turn 3 every withheld sentence's reason was "with no
    citation tag" - not a bad tag, no tag at all. The model was reading its
    own prior turns in the history, seeing text with the tags stripped off,
    and copying that. Session memory was teaching the Representative to
    stop citing.

    Only the tags that survived the net are replayed, which is why this
    rebuilds from `citations` rather than keeping the raw output around.
    Turn 1 of that same run tagged three sentences to two record ids that
    do not exist (desert.dw.f6-e-struggle-interior,
    desert.dw.f1-i-discernment-contemplation - the net caught both). A
    fabricated id must not come back as an example of how to cite.

    Withheld sentences keep their text and lose their tags. They were shown
    to the participant - the net gates decoration, not text (Program-Spec
    M4) - so the model heard itself say them, and dropping them here would
    make its own memory disagree with what the person read.
    """
    said = (entry.get("text") or "").strip()
    for citation in entry.get("citations") or []:
        sentence = (citation.get("sentence") or "").strip()
        record_ids = citation.get("record_ids") or []
        if not sentence or not record_ids or sentence not in said:
            continue
        tags = " ".join(f"[[{rid}]]" for rid in record_ids)
        # BEFORE the terminal punctuation, the same rule the compiler uses
        # for demonstration tags (engine.m2.builders) and the same one the
        # net's own splitter assumes - a tag after the stop is carried onto
        # the next sentence.
        cut = max(sentence.rfind(mark) for mark in ".!?")
        tagged = f"{sentence} {tags}" if cut < 0 else f"{sentence[:cut]} {tags}{sentence[cut:]}"
        said = said.replace(sentence, tagged, 1)
    return said


def history_from_transcript(transcript: list[dict]) -> list[dict]:
    """Program-Spec M4's "full-session memory", as Messages-API turns.
    Until now the generation call sent a single user message and the voice
    had never heard the last thing it said.

    Three deliberate choices, each with a test. The voice is replayed the
    text a participant actually read, with its verified citations back on
    it - see _replay_text for why the tags have to be there, and what an
    earlier version of this docstring got wrong. Facilitator turns are left
    out: they belong to a different voice, and folding them in would put
    the Facilitator's words in the Representative's mouth. And pairs are
    emitted strictly alternating, so a participant message that produced no
    voice reply - a routing gap, a crisis turn, a turn the net emptied -
    leaves no dangling role behind.
    """
    history: list[dict] = []
    pending: str | None = None
    for entry in transcript:
        if entry.get("speaker") == "participant":
            pending = entry.get("text") or ""
        elif entry.get("speaker") not in (None, "facilitator") and pending is not None:
            said = _replay_text(entry)
            if said:
                history.append({"role": "user", "content": pending})
                history.append({"role": "assistant", "content": said})
            pending = None
    return history


def handle_message(
    *,
    store: Store,
    usage_store: UsageLogStore,
    world_loader: LazyWorldLoader,
    registry: dict,
    voice_client,
    voice_model_id: str,
    safety_client,
    safety_model_id: str,
    session_id: str,
    text: str,
    client_msg_id: str | None = None,
) -> MessageResult:
    state = project_fresh(session_id, store)
    if not state.exists:
        raise SessionNotFound(session_id)

    # The world pinned at session creation, not the registry's current value -
    # a mid-session recompile can't silently swap what serves an in-flight
    # session. A hash mismatch surfaces as PackageRefused (engine.m2.loader_stub),
    # left uncaught here so the caller (app.py) maps it to a 503.
    world = _load_world(world_loader, registry, state.world_key, expected_manifest_hash=state.package_manifest_hash)

    msg_uuid = client_msg_id or str(uuid.uuid4())
    participant_payload = {"text": text, "client_msg_id": msg_uuid}
    events.validate("participant_message", participant_payload)
    store.append(session_id=session_id, event_uuid=str(uuid.uuid4()), event_type="participant_message", payload=participant_payload)

    already_told_ids = {
        record_id
        for turn in state.transcript
        for citation in (turn.get("citations") or [])
        for record_id in citation.get("record_ids", [])
    }
    history = history_from_transcript(state.transcript)

    term_ids = compute_anachronistic_term_ids(load_fleet_records(), world.frame["time_window"])
    turn_no = state.turn_count + 1

    try:
        result: TurnResult = run_turn(
            session_id=session_id,
            voice_client=voice_client,
            voice_model_id=voice_model_id,
            safety_client=safety_client,
            safety_model_id=safety_model_id,
            world=world,
            participant_message=text,
            pressed=state.pressed,
            anachronistic_term_ids=term_ids,
            already_told_ids=already_told_ids,
            history=history,
        )
    except UnhandledRoutingAction as exc:
        # A real, tested routing outcome with no generation content wired up
        # yet (engine.m4.turn's own module docstring names which ones) -
        # graceful, never a 500. The participant's message is already
        # committed above; this still commits a turn so the conversation
        # stays usable afterward.
        facilitator_event = {"kind": "threshold", "text": UNHANDLED_ROUTING_FACILITATOR_TEXT, "unhandled_routing_gap": True}
        events.validate("facilitator_turn", facilitator_event)
        store.append(session_id=session_id, event_uuid=str(uuid.uuid4()), event_type="facilitator_turn", payload=facilitator_event)
        store.append(session_id=session_id, event_uuid=str(uuid.uuid4()), event_type="turn_committed", payload={"turn_no": turn_no})
        return MessageResult(
            turn_no=turn_no,
            routing_action=None,
            routing_reason=str(exc),
            degraded=True,
            unhandled_routing_gap=True,
            facilitator=facilitator_event,
            voice=None,
        )
    except Exception as exc:
        # engine.m5.live_calls only catches anthropic.APIError/APITimeoutError
        # (confirmed by reading it directly) - a raw botocore/credential
        # failure propagates straight through run_turn uncaught. Nothing
        # commits past this point; the participant_message stays in the log
        # as evidence of what was sent and they may resend.
        raise ProviderCallFailed(str(exc)) from exc

    gate_payload = {
        "asks": [],
        "register": None,
        "out_of_scope": None,
        "modern_terms": [],
        "safety": None,
        "route": result.routing_action,
        "directive": None,
        "degraded": result.degraded,
    }
    events.validate("gate_decision", gate_payload)
    store.append(session_id=session_id, event_uuid=str(uuid.uuid4()), event_type="gate_decision", payload=gate_payload)

    facilitator_payload = None
    for fe in result.facilitator_events:
        events.validate("facilitator_turn", fe)
        store.append(session_id=session_id, event_uuid=str(uuid.uuid4()), event_type="facilitator_turn", payload=fe)
        facilitator_payload = fe  # today there's ever 0 or 1; last one wins for the response shape

    voice_payload = None
    if result.voice_event is not None:
        events.validate("voice_turn", result.voice_event)
        store.append(session_id=session_id, event_uuid=str(uuid.uuid4()), event_type="voice_turn", payload=result.voice_event)
        voice_payload = result.voice_event

    store.append(session_id=session_id, event_uuid=str(uuid.uuid4()), event_type="turn_committed", payload={"turn_no": turn_no})

    for rec in result.usage_records:
        usage_store.append(rec)

    return MessageResult(
        turn_no=turn_no,
        routing_action=result.routing_action,
        routing_reason=result.routing_reason,
        degraded=result.degraded,
        unhandled_routing_gap=False,
        facilitator=facilitator_payload,
        voice=voice_payload,
    )
