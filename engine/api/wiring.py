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
from pathlib import Path

from engine.api.config import REPO_ROOT
from engine.m1.loader import load_fleet_records
from engine.m4 import events, facilitator_turns, session_code
from engine.m4.entrance import open_session
from engine.m4.package_fetch import ensure_package_local
from engine.m4.projection import SessionState, project_fresh
from engine.m4.store import Store
from engine.m4 import evidence as ev
from engine.m4.turn import TurnResult, UnhandledRoutingAction, run_turn
from engine.m4.uncited_claims import (
    build_uncited_claims_event,
    conversation_revealed_excerpts,
    known_tradition_names,
    match_named_tradition,
    tradition_known_in_window,
    world_records_mention_tradition,
)
from engine.m4.world_loader import LazyWorldLoader, LoadedWorld
from engine.m5.anachronism import anachronistic_term_ids as compute_anachronistic_term_ids
from engine.m5.routing import PRESSABLE_CLASSES
from engine.m7.session_reader import read_session
from engine.m8.log_store import UsageLogStore

class UnknownWorldError(Exception):
    """world_key isn't in the registry (records/worlds.yaml)."""


class WorldNotAdmitted(Exception):
    """The world exists but its registry state is not admitted/open, and
    admission enforcement is on (Settings.enforce_admission - see its own
    comment for the stage-10 semantics). Raised before any session event is
    written; the app layer maps it to 403. Carries the world_key."""


# The registry states a participant-facing session may be built on once
# enforcement is on (Artifact-1 SS2's lifecycle: built -> admitted -> open;
# `built` means gates-green + compiled, NOT validated by the live admission
# battery or human review). The fixture world never reaches these states, so
# enforcement also closes the fixture-session hole for free.
ADMITTED_STATES = frozenset({"admitted", "open"})


def _check_admission(registry: dict, world_key: str, *, require_admitted: bool) -> None:
    if not require_admitted:
        return
    entry = registry.get(world_key) or {}
    if entry.get("state") not in ADMITTED_STATES:
        raise WorldNotAdmitted(world_key)


class SessionNotFound(Exception):
    """No session_started event exists for this session_id."""


class DuplicateMessage(Exception):
    """A client_msg_id this session has already processed - the retry is
    refused before any model call (409 at the API), never re-run."""


class SessionClosed(Exception):
    """A session_closed event is already on record (engine.m4.projection's
    SessionState.closed) - the session ended, most often via
    engine.m4.turn.SESSION_TURN_CAP's own graceful redirect, and no further
    message is processed. Raised here, before run_turn is ever called, so a
    closed session costs nothing to refuse."""


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
    facilitator: dict | None
    voice: dict | None


def _load_world(
    world_loader: LazyWorldLoader,
    registry: dict,
    world_key: str,
    *,
    expected_manifest_hash: str | None = None,
    package_location_override: str | None = None,
    package_cache_dir: Path | None = None,
) -> LoadedWorld:
    entry = registry.get(world_key)
    if entry is None:
        raise UnknownWorldError(world_key)
    # package_location_override (2026-09-04): an in-flight session's own
    # pinned directory, when it has one (see entrance.py's open_session
    # docstring) - never the registry's CURRENT pointer for that call, since
    # a repin between this session's open and this turn would otherwise
    # resolve a directory this session never verified against. Old packages
    # are never deleted, so the pinned directory is still there to read.
    # Falls back to today's registry pointer for callers with no pin of
    # their own (list_worlds, a fresh create_session/create_table_session)
    # and for sessions opened before this field existed.
    location = package_location_override or entry["package"]["location"]
    package_dir = REPO_ROOT / location
    # WO-1 (2026-09-16): package_cache_dir is None for every caller that
    # doesn't pass one (every test app, and a real deploy with no bucket
    # configured) - ensure_package_local is a no-op in that case, package_dir
    # is used exactly as it always was. Only a real deploy with object
    # storage configured ever takes the fetch path, and only for a world
    # not already sitting on local disk.
    if package_cache_dir is not None:
        package_dir = ensure_package_local(package_dir=package_dir, cache_dir=package_cache_dir, key_prefix=location)
    world, _timing = world_loader.load(
        world_key, package_dir=package_dir, expected_manifest_hash=expected_manifest_hash or entry["package"]["manifest_hash"]
    )
    return world


def create_session(
    *,
    store: Store,
    world_loader: LazyWorldLoader,
    registry: dict,
    world_key: str,
    require_admitted: bool = False,
    package_cache_dir: Path | None = None,
) -> tuple[str, str]:
    """Returns (session_id, raw_code). The raw code is returned exactly once
    - only its hash is ever stored (engine.m4.session_code).

    require_admitted is the admission gate (Settings.enforce_admission):
    checked BEFORE the world is even loaded, so a refused create costs
    nothing and writes nothing."""
    _check_admission(registry, world_key, require_admitted=require_admitted)
    world = _load_world(world_loader, registry, world_key, package_cache_dir=package_cache_dir)
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
        # The directory this world actually loaded from, pinned alongside
        # its hash - registry[world_key] re-read here rather than reusing
        # any value from _load_world above, since that call's own default
        # (no override) resolved through today's registry, which is
        # exactly the value this session needs to remember (see entrance.py).
        package_location=str(registry[world_key]["package"]["location"]),
    )

    # The conversation's first-ever line, Program-Spec SS71 ("visible at
    # door, thresholds, and close") - open_session above is the only
    # allowed writer of session_started itself (engine.m4.entrance's own
    # seal), not of everything create_session appends after it.
    representative = world.frame["representative"]
    # card_name over display_name: see door_turn's own docstring
    # (Built-World Voice Alignment, Mark's ruling 2026-09-17). Falls back to
    # display_name only for an entry with no card_name (the fix fixture).
    world_name = registry[world_key].get("card_name") or world.frame["display_name"]
    door_event = facilitator_turns.door_turn(
        representative_name=representative["name"],
        role_label=representative["role_label"],
        world_name=world_name,
    )
    events.validate("facilitator_turn", door_event)
    store.append(session_id=session_id, event_uuid=str(uuid.uuid4()), event_type="facilitator_turn", payload=door_event)

    return session_id, raw_code


def list_worlds(*, world_loader: LazyWorldLoader, registry: dict, require_admitted: bool = False, package_cache_dir: Path | None = None) -> list[dict]:
    """The doorway's own content, per formation world - never the fix
    fixture (kind == "fixture": "NOT one of the six formation worlds...
    never listed beside them, never admitted, never reachable by a
    participant", per its own registry comment). Reads each world's real
    compiled frame.json through the same LazyWorldLoader/manifest-hash
    verification path a session load uses, rather than re-deriving a second
    copy of this data by hand - the world-list screen was doing that until
    now (data/worlds.ts, baked at frontend build time, hand-copied from the
    registry with its own comment admitting "no /api/worlds endpoint exists
    yet"). Explicit field selection rather than returning `world.frame`
    whole: frame.json also carries `_generated_by`, a compiler/commit
    fingerprint with no participant-facing purpose.
    """
    worlds = []
    for world_key, entry in registry.items():
        if entry.get("kind") != "formation":
            continue
        if require_admitted and entry.get("state") not in ADMITTED_STATES:
            # Under enforcement the doorway lists only worlds a participant
            # may actually enter - an unadmitted world simply is not
            # offered, rather than offered and then refused at the door.
            continue
        world = _load_world(world_loader, registry, world_key, package_cache_dir=package_cache_dir)
        frame = world.frame
        starters = frame.get("frames", {}).get("general_seeker", {}).get("starters", [])
        worlds.append(
            {
                "world_key": world_key,
                "census_id": entry.get("census_id"),
                "display_name": frame.get("display_name"),
                # BOTH name registers are kept: card_name
                # is the friendly participant-facing name ("the right
                # picture in their mind"), display_name the scholarly one
                # ("to show rigor"). The registry owns both.
                "card_name": entry.get("card_name") or frame.get("display_name"),
                # Registry-owned participant-facing doorway paragraph, plain
                # English, same registry-first
                # pattern as card_name. `horizon` below is the world_core's
                # model-facing self-description and stays served as the
                # fallback for a registry entry that hasn't authored one.
                "doorway_description": entry.get("doorway_description"),
                "representative": frame.get("representative"),
                "time_window": frame.get("time_window"),
                # doorway_place: participant-facing subtitle where the
                # registry authored one; frame's place is MODEL-FACING (it
                # compiles into the voice capsule's "Place:" line), which is
                # why the plain-English rewrite lives beside it instead of
                # replacing it.
                "place": entry.get("doorway_place") or frame.get("place"),
                "thinness_statement": frame.get("thinness_statement"),
                "horizon": frame.get("horizon"),
                "living_tradition_flag": frame.get("living_tradition_flag", False),
                "starters": starters,
            }
        )
    return worlds


def get_transcript(store: Store, session_id: str) -> SessionState:
    state = project_fresh(session_id, store)
    if not state.exists:
        raise SessionNotFound(session_id)
    return state


@dataclass(frozen=True)
class PilotSummary:
    """Aggregate, participant-content-free counts over the whole session
    log (2026-09-05: "how many pilot id/transcripts have been generated"
    had no answer from outside the service itself - no admin surface
    existed at all, only per-session lookups gated by that session's own
    auth code). Never carries transcript text, citation content, or a
    session_id list - just enough to answer "how many" and "is the table
    round cap firing where it should," the two questions that prompted
    this."""

    total_sessions: int
    by_mode: dict[str, int]
    open_sessions: int
    closed_by_reason: dict[str, int]
    # round count -> how many table sessions closed there via the session
    # round cap (session_closed reason "cap", table mode only) - a direct
    # check on TABLE_SESSION_ROUND_CAP actually firing at the configured
    # number in real use, not just in a fake-backed test. Keys are strings
    # (JSON object keys, not a list) since the round count itself carries
    # the finding: unexpected keys mean the cap fired somewhere it
    # shouldn't have.
    table_round_counts_on_cap: dict[str, int]
    earliest_session_at: str | None
    latest_session_at: str | None


def get_pilot_summary(store: Store, *, since: str | None = None) -> PilotSummary:
    """Reuses engine.m7.session_reader (the M7 audit's own reader) rather
    than re-deriving the event fold a second way - this only tallies what
    that reader already exposes per session, never re-reads raw events
    itself. `since` passes straight through to Store.list_session_ids,
    the same M7-sweep filter."""
    session_ids = store.list_session_ids(since=since)
    by_mode: dict[str, int] = {}
    closed_by_reason: dict[str, int] = {}
    table_round_counts_on_cap: dict[str, int] = {}
    open_sessions = 0
    earliest: str | None = None
    latest: str | None = None

    for session_id in session_ids:
        session = read_session(store, session_id)
        if session is None:
            continue
        by_mode[session.mode] = by_mode.get(session.mode, 0) + 1
        if session.first_at and (earliest is None or session.first_at < earliest):
            earliest = session.first_at
        if session.last_at and (latest is None or session.last_at > latest):
            latest = session.last_at
        if not session.closed:
            open_sessions += 1
            continue
        reason = session.close_reason or "unknown"
        closed_by_reason[reason] = closed_by_reason.get(reason, 0) + 1
        if session.mode == "table" and reason == "cap":
            # table_wiring.handle_table_message's session_capped branch
            # always appends its OWN zero-turn round_closed (+
            # turn_committed) as the cap's own close, on top of however
            # many real rounds preceded it (the same event pair every
            # real round gets - table_wiring._close_round's own
            # docstring) - so the round count the cap actually fired AT
            # (what TABLE_SESSION_ROUND_CAP compares rounds_completed
            # against) is one fewer than the raw event count.
            round_no = str(len(session.rounds_closed) - 1)
            table_round_counts_on_cap[round_no] = table_round_counts_on_cap.get(round_no, 0) + 1

    return PilotSummary(
        total_sessions=len(session_ids),
        by_mode=by_mode,
        open_sessions=open_sessions,
        closed_by_reason=closed_by_reason,
        table_round_counts_on_cap=table_round_counts_on_cap,
        earliest_session_at=earliest,
        latest_session_at=latest,
    )



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


def replay_transcript(state: SessionState, anachronistic_term_ids: set) -> list[dict]:
    """The transcript as session memory may replay it: each participant
    entry whose round routed bridge_turn has its text replaced by the
    underlying subject the voice actually received.

    SS77's "the voice never sees the participant's modern word" was honored
    on the bridge turn itself and then leaked one turn later: history was
    built from the transcript's raw participant text, so from the next turn
    on, the voice read the barred word in its own replayed history (found
    2026-08-28 while building the Table; fixed for both modes at once - the
    table's builders consume this same function).

    The route per participant message comes from the logged gate_decision
    (each participant_message's gate is the next gate_decision after it in
    the event order - a message whose request crashed before its gate wrote
    stays un-gated and replays raw, which is honest: no route ever resolved
    for it). The substitute text is derived by engine.m4.round.
    voice_message_for_round - the SAME derivation the live bridge turn
    used, so memory and the turn it remembers cannot disagree.

    This does not touch _replay_text's own discipline ("history must match
    what the person read"): that rule is about the VOICE's words, which the
    participant read on screen. The participant's message was never shown
    back to the participant - substituting what the voice was actually
    handed keeps the voice's memory consistent with its own experience of
    the turn, which is the memory being replayed here.
    """
    from engine.m4.round import voice_message_for_round

    gate_for_message: list[dict | None] = []
    for event in state.raw_events:
        if event.event_type == "participant_message":
            gate_for_message.append(None)
        elif event.event_type == "gate_decision" and gate_for_message and gate_for_message[-1] is None:
            gate_for_message[-1] = event.payload

    result = []
    ordinal = 0
    for entry in state.transcript:
        if entry.get("speaker") == "participant":
            gate = gate_for_message[ordinal] if ordinal < len(gate_for_message) else None
            ordinal += 1
            if gate and gate.get("route") == "bridge_turn":
                substitute, _directive = voice_message_for_round(gate, entry.get("text") or "", anachronistic_term_ids)
                if substitute:
                    entry = {**entry, "text": substitute}
        result.append(entry)
    return result


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
    package_cache_dir: Path | None = None,
    r27_enforce: bool = False,
    self_revision_enabled: bool = True,
) -> MessageResult:
    state = project_fresh(session_id, store)
    if not state.exists:
        raise SessionNotFound(session_id)
    # An idle close (engine.m4.idle_close) is reporting-only - a
    # participant resuming with their session code is never refused for
    # it, unlike a real (cap/participant) close. project_fresh's own fold
    # already reopens state.closed once this message lands, so this is
    # the one place that still needs to look past it before that happens.
    if state.closed and state.close_reason != "idle":
        raise SessionClosed(session_id)

    # The world pinned at session creation, not the registry's current value -
    # a mid-session recompile can't silently swap what serves an in-flight
    # session. Both the hash AND the directory are pinned (package_location,
    # 2026-09-04): a repin changes both in the registry, and resolving only
    # the hash pin against today's (post-repin) directory reliably refuses,
    # since the two no longer describe the same package - see entrance.py's
    # open_session docstring. A hash mismatch (still possible: a session
    # opened before package_location existed has no pin to fall back on)
    # surfaces as PackageRefused (engine.m2.loader_stub), left uncaught here
    # so the caller (app.py) maps it to a 503.
    world = _load_world(
        world_loader,
        registry,
        state.world_key,
        expected_manifest_hash=state.package_manifest_hash,
        package_location_override=state.package_location,
        package_cache_dir=package_cache_dir,
    )

    msg_uuid = client_msg_id or str(uuid.uuid4())
    # Idempotency, ENFORCED (2026-08-28 foundation audit: client_msg_id was
    # recorded in the payload but the dedupe key - event_uuid - was minted
    # fresh every call, so a retried message ran a second full turn and
    # doubled the spend). With a client_msg_id the event_uuid is derived
    # deterministically, so the same logical message can only ever be one
    # event - and a replay is refused BEFORE any model call runs.
    participant_event_uuid = (
        str(uuid.uuid5(uuid.NAMESPACE_URL, f"cic:{session_id}:{msg_uuid}")) if client_msg_id else str(uuid.uuid4())
    )
    if client_msg_id and store.event_exists(participant_event_uuid):
        raise DuplicateMessage(session_id)
    participant_payload = {"text": text, "client_msg_id": msg_uuid}
    events.validate("participant_message", participant_payload)
    store.append(session_id=session_id, event_uuid=participant_event_uuid, event_type="participant_message", payload=participant_payload)

    already_told_ids = {
        record_id
        for turn in state.transcript
        for citation in (turn.get("citations") or [])
        for record_id in citation.get("record_ids", [])
    }
    # Same shape, same reason, for engine.m4.name_bridge.find_figures_used:
    # figure ids a prior turn this session already bridged, read from that
    # turn's own figures_used - see engine.m4.turn.run_turn's docstring on
    # already_bridged_figure_ids for why this lives with the caller.
    already_bridged_figure_ids = {
        figure["id"]
        for turn in state.transcript
        for figure in (turn.get("figures_used") or [])
    }
    # Same shape again, for engine.m4.term_glosses.find_glosses_used: term
    # ids a prior turn this session already glossed, read from that turn's
    # own glosses (a required voice_turn key since the event catalog was
    # written; this is the first thing that ever populates it).
    already_bridged_gloss_ids = {
        gloss["id"]
        for turn in state.transcript
        for gloss in (turn.get("glosses") or [])
    }
    term_ids = compute_anachronistic_term_ids(load_fleet_records(), world.frame["time_window"])
    # History replays bridged rounds' participant text as the underlying
    # subject the voice actually received (SS77 applied to session memory,
    # not only the live turn - see replay_transcript's own docstring).
    replayed = replay_transcript(state, term_ids)
    history = history_from_transcript(replayed)

    turn_no = state.turn_count + 1

    # R39's own reviewer-ordered fix (2026-09-23): unconditional, never
    # gated behind r27_enforce - this corrects an existing false statement
    # (_other_tradition_directive's own fixed honest-limit sentence, said
    # even when this world's own records already name the tradition
    # asked about) rather than adding new enforcement. match_named_
    # tradition works from the raw participant text, independent of
    # whatever the reader ends up classifying - harmless to compute even
    # on a turn the reader does not route other_tradition, since
    # _build_turn_directive only ever reads it when is_other_tradition_
    # first_ask is also true.
    named_tradition_key = match_named_tradition(text, registry, exclude_world_key=state.world_key)
    other_tradition_evidence_ids = (
        world_records_mention_tradition(ev.repository_records_by_id(world.repository), registry[named_tradition_key])
        if named_tradition_key else None
    )
    # R37 (Rulings-Pending.md R37, R37-A, R37-B): the pivot's own licence
    # for the same named tradition - condition (a) from the registry's own
    # time_windows, condition (b) from what this conversation actually
    # said, read from the same replayed transcript the voice's own history
    # is (what the voice was actually told). state was projected before
    # this turn's own participant_message was appended, so the question
    # itself is not counted as a revelation. No other Representative
    # speaks in an interview, so R37-B's third source is empty here by
    # construction.
    other_tradition_known_in_window = (
        tradition_known_in_window(registry[state.world_key], registry[named_tradition_key])
        if named_tradition_key else None
    )
    other_tradition_revealed = (
        conversation_revealed_excerpts(replayed, registry[named_tradition_key], speaking_world_key=state.world_key)
        if named_tradition_key else None
    )

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
            track_b_accumulator=state.safety.track_b_accumulator,
            track_a_last=state.safety.track_a_last,
            already_told_ids=already_told_ids,
            already_bridged_figure_ids=already_bridged_figure_ids,
            already_bridged_gloss_ids=already_bridged_gloss_ids,
            history=history,
            r27_enforce=r27_enforce,
            known_tradition_names=known_tradition_names(registry, exclude_world_key=state.world_key) if r27_enforce else None,
            other_tradition_evidence_ids=other_tradition_evidence_ids,
            other_tradition_known_in_window=other_tradition_known_in_window,
            other_tradition_revealed=other_tradition_revealed,
            self_revision_enabled=self_revision_enabled,
        )
    except UnhandledRoutingAction:
        # Deleted 2026-08-24, not weakened: this used to catch the raise and
        # hand the participant a note about a test build, because four of
        # the seven routing actions genuinely had no content. All seven have
        # content now, so the state that text described cannot occur, and a
        # graceful degradation path for an impossible state is just a
        # permanently-false field in the public response schema.
        #
        # The raise in engine.m4.turn stays as the guard for an EIGHTH
        # routing action someone adds without a branch. Re-raised here so it
        # surfaces as itself - a programming error, a 500 - rather than
        # being swallowed by the provider-failure catch below and reported
        # to the operator as a Bedrock problem it is not.
        raise
    except Exception as exc:
        # engine.m5.live_calls only catches anthropic.APIError/APITimeoutError
        # (confirmed by reading it directly) - a raw botocore/credential
        # failure propagates straight through run_turn uncaught. Nothing
        # commits past this point; the participant_message stays in the log
        # as evidence of what was sent and they may resend.
        raise ProviderCallFailed(str(exc)) from exc

    # What the gate actually said, written whole. This was a hand-built
    # blank until 2026-08-24 - every key but route and degraded hardcoded
    # empty, on every gate_decision this build ever logged, so a successful
    # gate and a failed one were indistinguishable in the record and the
    # M7 audit had nothing to audit. engine.m4.turn assembles it now, where
    # the two gate outcomes are; this writes it verbatim rather than
    # rebuilding a second version that could drift from the first.
    gate_payload = result.gate
    events.validate("gate_decision", gate_payload)
    store.append(session_id=session_id, event_uuid=str(uuid.uuid4()), event_type="gate_decision", payload=gate_payload)

    # THE PRESSED FLAG'S ONLY WRITER. engine.m5.routing rule 5 gives a
    # pressable out_of_scope class its in-world answer on the first ask and
    # the etic turn on the second - but "second" is read from
    # SessionState.pressed, which folds from escalation_pressed, which was
    # declared in engine.m4.events, folded in engine.m4.projection, and
    # appended by nothing anywhere. `pressed` was therefore permanently {},
    # every ask was a first ask, and etic_turn was unreachable by any real
    # session (proven live, pahc, 2026-08-24). This is the missing append.
    #
    # It fires on the in-world answer, not on the etic turn: what the flag
    # records is that this class has now HAD its first answer, so the next
    # ask is a press. Appending it after the etic turn would be recording a
    # state the session had already used. Re-appending on a later first-ask
    # is harmless - the projection folds it to True either way.
    # What the sealed safety call said, kept. Written straight after the
    # gate decision it derives from, and only when something changed - most
    # turns append nothing. This RECORDS ONLY: routing is untouched, the
    # safety call's own input is untouched, and nothing reads the
    # accumulator back except the next turn's own payload. The threshold
    # that would act on it is a separate decision (engine.m5.
    # safety_accumulation).
    for safety_state in result.safety_state_events:
        events.validate("safety_state", safety_state)
        store.append(session_id=session_id, event_uuid=str(uuid.uuid4()), event_type="safety_state", payload=safety_state)

    out_of_scope_class = (gate_payload.get("out_of_scope") or {}).get("class")
    if result.routing_action == "voice_with_directive" and out_of_scope_class in PRESSABLE_CLASSES:
        pressed_payload = {"class": out_of_scope_class}
        events.validate("escalation_pressed", pressed_payload)
        store.append(session_id=session_id, event_uuid=str(uuid.uuid4()), event_type="escalation_pressed", payload=pressed_payload)

    facilitator_payload = None
    for fe in result.facilitator_events:
        events.validate("facilitator_turn", fe)
        store.append(session_id=session_id, event_uuid=str(uuid.uuid4()), event_type="facilitator_turn", payload=fe)
        facilitator_payload = fe  # today there's ever 0 or 1; last one wins for the response shape

    # THE CAP'S OWN CLOSE. session_cap_turn's facilitator_turn (just appended
    # above, kind="close") is the participant-facing side; this is the
    # state-changing side - the same session_closed/reason="cap" shape
    # engine.m4.events and engine.m4.projection already carried, unused,
    # before this turn cap existed to fire it. Appended after the
    # facilitator_turn so a reader replaying the log sees the closing words
    # before the event that makes them final.
    if result.routing_action == "session_cap_turn":
        closed_payload = {"reason": "cap"}
        events.validate("session_closed", closed_payload)
        store.append(session_id=session_id, event_uuid=str(uuid.uuid4()), event_type="session_closed", payload=closed_payload)

    voice_payload = None
    if result.voice_event is not None:
        events.validate("voice_turn", result.voice_event)
        store.append(session_id=session_id, event_uuid=str(uuid.uuid4()), event_type="voice_turn", payload=result.voice_event)
        voice_payload = result.voice_event

        # R27 (Decision-Log.md Entry 51, 2026-09-22), report-only: same
        # out_of_scope_class already read above for the pressed-flag append,
        # not re-derived - a voice_with_directive turn routed via
        # other_tradition is the "own doctrine in another tradition's turn"
        # shape build_uncited_claims_event's own classify_other_tradition_turn
        # is built to catch.
        uncited_event = build_uncited_claims_event(
            result.voice_event,
            registry=registry,
            is_other_tradition_turn=(result.routing_action == "voice_with_directive" and out_of_scope_class == "other_tradition"),
        )
        if uncited_event is not None:
            events.validate("uncited_claims", uncited_event)
            store.append(session_id=session_id, event_uuid=str(uuid.uuid4()), event_type="uncited_claims", payload=uncited_event)

        # R27 build item 5 (Decision-Log.md Entry 56/Rulings-Pending.md
        # R36, 2026-09-23): the interview-mode analog of
        # engine.api.table_wiring's own seat_identity_guard_exhausted
        # handling below - the voice_turn just persisted above already
        # carries empty text (engine.m4.turn sets it that way), so the
        # Facilitator's own turn is what a participant actually reads.
        # "Last one wins" (this function's own established convention
        # for facilitator_payload) is correct here too: an r27-exhausted
        # turn is a real generation failure for this turn, which
        # supersedes any other facilitator_event the same turn produced.
        if result.voice_event.get("r27_enforcement_exhausted"):
            fallback_event = facilitator_turns.voice_rejected_turn(world.frame["representative"]["name"])
            events.validate("facilitator_turn", fallback_event)
            store.append(session_id=session_id, event_uuid=str(uuid.uuid4()), event_type="facilitator_turn", payload=fallback_event)
            facilitator_payload = fallback_event

    store.append(session_id=session_id, event_uuid=str(uuid.uuid4()), event_type="turn_committed", payload={"turn_no": turn_no})

    for rec in result.usage_records:
        usage_store.append(rec)

    return MessageResult(
        turn_no=turn_no,
        routing_action=result.routing_action,
        routing_reason=result.routing_reason,
        degraded=result.degraded,
        facilitator=facilitator_payload,
        voice=voice_payload,
    )
