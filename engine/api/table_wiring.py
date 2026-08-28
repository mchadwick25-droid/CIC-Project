"""Table-session orchestration (Artifact-7): the event-log-owning layer for
mode="table", kept in its own module so engine.api.wiring's interview path
stays visibly untouched. Same division of labor as wiring: engine.m4.round /
engine.m4.turn / engine.m4.turn_selector compute and this module writes.

The turn-at-a-time shape (C2, Artifact-7 SS6): handle_table_message opens
the round (gate once, resolve routing, write the facilitator's part) and -
when voices speak at all - advances it by exactly one voice turn.
continue_table_round advances the open round by one more, or reports the
close. BOTH paths advance through the same _advance_open_round, which
re-projects the session from the store every time: all round state is a
projection of the log (engine.m4.projection's round bookkeeping), so a
continue served by a different process behind the same store continues the
same round, and the two entry points cannot disagree about where the round
stands.

THE ISOLATION PROPERTY lives one level down and is worth restating at the
layer that assembles the pieces: the selected voice's turn runs
engine.m4.turn.run_voice_turn_for_world with exactly one LoadedWorld - its
own. Evidence, grounding net, name bridge, glosses: all scoped to that
world's package. What crosses between worlds is ONLY what this module
builds into history/context_prefix from the transcript - what was SAID at
the Table (Table Design V2.3 SS6), attributed by name, never records or
package internals. engine/api/tests/test_table_isolation.py holds this to
account with a seeded cross-world leak.
"""
import uuid
from dataclasses import dataclass

from engine.api.wiring import (
    DuplicateMessage,
    ProviderCallFailed,
    SessionClosed,
    SessionNotFound,
            _check_admission,
    _load_world,
    _replay_text,
    replay_transcript,
)
from engine.m1.loader import load_fleet_records
from engine.m4 import events, facilitator_turns, session_code
from engine.m4.entrance import open_session
from engine.m4.projection import SessionState, project_fresh
from engine.m4.round import (
    RoundConfig,
    open_table_round,
    voice_message_for_round,
)
from engine.m4.table_governance import detect_direct_address, governance_summary
from engine.m4.store import Store
from engine.m4.turn import UnhandledRoutingAction, _maybe_record_usage, run_gate, run_voice_turn_for_world
from engine.m4.turn_selector import Selection, select_speaker

import threading
from contextlib import contextmanager

# One in-process lock per table session (2026-08-28 audit): two overlapping
# advances both project the same open round and both run a voice turn.
# In-process is the true scope today - the SQLite store already pins the
# service to one instance; the Postgres move revisits this alongside it.
_ADVANCE_LOCKS: dict[str, threading.Lock] = {}
_ADVANCE_LOCKS_GUARD = threading.Lock()


@contextmanager
def _advance_lock(session_id: str):
    with _ADVANCE_LOCKS_GUARD:
        lock = _ADVANCE_LOCKS.setdefault(session_id, threading.Lock())
    if not lock.acquire(blocking=False):
        raise TableAdvanceInFlight(session_id)
    try:
        yield
    finally:
        lock.release()
from engine.m4.world_loader import LazyWorldLoader, LoadedWorld
from engine.m5.anachronism import anachronistic_term_ids as compute_anachronistic_term_ids
from engine.m5.routing import PRESSABLE_CLASSES
from engine.m8.log_store import UsageLogStore

PARTICIPANT_LABEL = "The participant"
FACILITATOR_LABEL = "The Facilitator"
_SELECTOR_TRANSCRIPT_WINDOW = 12  # attributed entries the selector sees; the round itself is always inside this


class TableRoundNotOpen(Exception):
    """continue was called with no round in flight (or on an interview
    session) - a client sequencing error, mapped to 409 by the app layer."""


class TableAdvanceInFlight(Exception):
    """Another advance (message or /continue) for this table session is
    already running in this process - the overlap the 2026-08-28 audit
    found: a mid-round reload's auto-resume racing the original tab's
    loop, each advancing the same round and doubling voice turns and
    spend. Refused as a 409; the client simply keeps continuing."""


class TableRoundStillOpen(Exception):
    """A new participant message arrived while a round is still open - the
    client must continue (or be told the close) before the next message."""


@dataclass(frozen=True)
class TableMessageResult:
    round_no: int
    round_open: bool
    routing_action: str | None
    routing_reason: str
    degraded: bool
    facilitator: list[dict]
    turn_selected: dict | None
    voice: dict | None
    position: int | None
    turn_no: int | None  # set only when this request committed the round
    session_closed: bool = False


def create_table_session(*, store: Store, world_loader: LazyWorldLoader, registry: dict, world_keys: list[str], require_admitted: bool = False) -> tuple[str, str]:
    """Returns (session_id, raw_code), same contract as the interview's
    create_session. Every seated world is loaded (and its manifest hash
    pinned) before anything is written - a table with an unloadable seat is
    refused whole, never opened partially. Under admission enforcement
    (require_admitted, Settings.enforce_admission) every seat must be
    admitted/open - one unadmitted seat refuses the whole table, checked
    before any load and before anything is written."""
    for k in world_keys:
        _check_admission(registry, k, require_admitted=require_admitted)
    worlds = [_load_world(world_loader, registry, k) for k in world_keys]
    session_id = str(uuid.uuid4())
    raw_code = session_code.generate_code()
    open_session(
        store,
        session_id=session_id,
        event_uuid=str(uuid.uuid4()),
        mode="table",
        frame=None,
        code_hash=session_code.hash_code(raw_code),
        world_keys=list(world_keys),
        package_manifest_hashes={w.world_key: w.manifest_hash for w in worlds},
    )
    seated = [
        {
            "representative_name": w.frame["representative"]["name"],
            "role_label": w.frame["representative"]["role_label"],
            "display_name": w.frame["display_name"],
        }
        for w in worlds
    ]
    door_event = facilitator_turns.table_door_turn(seated)
    events.validate("facilitator_turn", door_event)
    store.append(session_id=session_id, event_uuid=str(uuid.uuid4()), event_type="facilitator_turn", payload=door_event)
    return session_id, raw_code


def _seated_worlds(state: SessionState, world_loader: LazyWorldLoader, registry: dict) -> dict[str, LoadedWorld]:
    """Every seated world, loaded against the hash pinned at session
    creation - a mid-session recompile of ANY seat refuses the session's
    load, same discipline as the interview's single pin."""
    return {
        k: _load_world(world_loader, registry, k, expected_manifest_hash=state.package_manifest_hashes[k])
        for k in state.world_keys
    }


def _labels(worlds: dict[str, LoadedWorld]) -> dict[str, str]:
    labels = {k: f"{w.frame['representative']['name']} ({w.frame['display_name']})" for k, w in worlds.items()}
    labels["participant"] = PARTICIPANT_LABEL
    labels["facilitator"] = FACILITATOR_LABEL
    return labels


def _round_anachronistic_term_ids(worlds: dict[str, LoadedWorld]) -> set:
    """A term is round-anachronistic only when it is anachronistic for EVERY
    seated world (Artifact-7 SS2) - a term inside one seated world's horizon
    is not bridged away from a voice that can answer it. Deterministic from
    the fleet records and the seated frames, which is what lets a continue
    re-derive the identical set."""
    fleet = load_fleet_records()
    per_world = [compute_anachronistic_term_ids(fleet, w.frame["time_window"]) for w in worlds.values()]
    return set.intersection(*per_world) if per_world else set()


def _attributed_lines(transcript: list[dict], labels: dict[str, str]) -> list[str]:
    lines = []
    for entry in transcript:
        text = (entry.get("text") or "").strip()
        if not text:
            continue
        speaker = entry.get("speaker")
        lines.append(f"{labels.get(speaker, speaker)}: {text}")
    return lines


def table_history_for(world_key: str, transcript: list[dict], labels: dict[str, str]) -> tuple[list[dict], list[str]]:
    """The public transcript projected for one viewer (Artifact-7 SS4, spec
    O9's "viewer-parameterized transcript projection"): the voice's own
    turns replay as assistant turns with their verified citations re-tagged
    (engine.api.wiring._replay_text - the anti-citation-decay fix, applied
    per voice); everything else said at the Table - participant, other
    voices, the Facilitator - folds into the user side, attributed by name.
    Returns (history_pairs, pending): pending is the attributed speech since
    this voice's last turn, which the caller renders into the current call's
    context_prefix. Roles alternate strictly by construction; a turn of this
    voice the net emptied out produces no pair (the interview's own
    no-dangling-role rule) and its bucket rolls forward."""
    history: list[dict] = []
    pending: list[str] = []
    for entry in transcript:
        speaker = entry.get("speaker")
        if speaker == world_key:
            said = _replay_text(entry)
            if said and pending:
                history.append({"role": "user", "content": "\n\n".join(pending)})
                history.append({"role": "assistant", "content": said})
                pending = []
            continue
        text = (entry.get("text") or "").strip()
        if text:
            pending.append(f"{labels.get(speaker, speaker)}: {text}")
    return history, pending


def _context_prefix(pending: list[str]) -> str | None:
    """Tightened 2026-08-28 after the first live smoke run, on Mark's read
    of the transcript. Two corrections, both his calls:

    NO FOREKNOWLEDGE. A Representative has insight into the conversation
    and its own world ONLY (Table Design V2.3 SS6: it knows the other "only
    as a voice it has encountered at this Table"). The live run showed the
    gap this instruction closes: the grounding net keeps citations inside
    the speaker's own world, but nothing stopped a voice from
    characterizing the OTHER world from the model's general knowledge -
    Papnoute spoke about Alexandria in claims the net could only strip
    badges from, never block. The instruction now states the epistemic
    position outright: the other voices are strangers met here, known only
    by their spoken words.

    COMPACT TURNS. Mark's settled read of the first transcript (2026-08-28,
    second pass - an earlier register note the same day was his own
    misread, withdrawn): the voices are very good, just LONG. Turns ran
    400-670 words, and at 3-6 turns a round that is the wall-of-text the
    UX review flagged. The guidance is table-scoped: a voice at a table
    leaves room for the others and can always be drawn back in - the
    single-voice interview's length is untouched."""
    if not pending:
        return None
    return (
        "What has been said at the Table since your last turn:\n"
        + "\n\n".join(pending)
        + "\n\n(You are being brought in now. Respond as yourself to the participant's message below.\n"
        "You know the other voices at this Table only through what they have said here, in this "
        "conversation. You have no knowledge of their worlds, their traditions, their practices, or their "
        "people beyond their own spoken words above - and no memory of meeting them before this Table. "
        "Engage what they actually said where it genuinely touches your own world's witness; never "
        # The no-foreknowledge line is performed in we-voice - option (a),
        # Mark's ruling 2026-08-28 ("use option a"): one pronoun rule, no
        # second sanctioned "I" exception. The rule itself stays performed
        # plainly; only its person changed (was "you know only what you
        # have heard", rendered by the model as "I know only...", which
        # every battery's output check flagged as unsanctioned singular).
        "describe, summarize, or characterize their world yourself, and if the participant asks you about "
        "another voice's world, say plainly that we know only what we have heard at this Table. "
        "What another voice has said is THEIR witness, never yours: never retell their stories, figures, "
        "or claims in your own world's first person - your 'we' and 'our' reach only what your own world "
        "holds. Everything you say about your OWN world stays grounded in your own records, exactly as "
        "always.\n"
        "Keep this turn compact - this is a table, not a lecture. Say the one or two things most worth "
        "saying right now, at perhaps half the length you would take alone with the participant, and leave "
        "room for the other voices; you can always be drawn back in.)"
    )


def _already_sets_for(world_key: str, transcript: list[dict]) -> tuple[set, set, set]:
    """The interview's three session-memory sets, PER WORLD (Artifact-7
    SS3): a story desert told is not "already told" for alx, and a figure
    alx bridged is not bridged for desert - so each derivation filters by
    this speaker's own turns."""
    own = [t for t in transcript if t.get("speaker") == world_key]
    told = {rid for t in own for c in (t.get("citations") or []) for rid in c.get("record_ids", [])}
    figures = {f["id"] for t in own for f in (t.get("figures_used") or [])}
    glosses = {g["id"] for t in own for g in (t.get("glosses") or [])}
    return told, figures, glosses


def _last_gate_payload(state: SessionState) -> dict:
    for event in reversed(state.raw_events):
        if event.event_type == "gate_decision":
            return event.payload
    raise TableRoundNotOpen(f"session {state.session_id} has an open round but no gate_decision on record")


def _last_participant_text(state: SessionState) -> str:
    for entry in reversed(state.transcript):
        if entry.get("speaker") == "participant":
            return entry.get("text") or ""
    raise TableRoundNotOpen(f"session {state.session_id} has an open round but no participant message on record")


def _close_round(store: Store, state: SessionState, *, reason: str, turns: int) -> int:
    """round_closed + turn_committed, in that order - a round, not a voice
    turn, is the committed unit (Artifact-7 SS2). Returns the turn_no.

    Every close carries the deterministic governance summary (C5,
    engine.m4.table_governance): per-voice word/turn shares and any
    dominance findings over the conversation so far - detected and
    audit-visible on the round_closed event, never blocking. Convergence
    is deliberately absent here: the poc implemented it as a conservative
    model judgment, so it runs in the live battery, not the round loop."""
    closed_payload = {
        "round_no": state.round_no, "reason": reason, "turns": turns,
        "governance": governance_summary(state.transcript, state.world_keys or []),
    }
    events.validate("round_closed", closed_payload)
    store.append(session_id=state.session_id, event_uuid=str(uuid.uuid4()), event_type="round_closed", payload=closed_payload)
    turn_no = state.turn_count + 1
    store.append(session_id=state.session_id, event_uuid=str(uuid.uuid4()), event_type="turn_committed", payload={"turn_no": turn_no})
    return turn_no


def _advance_open_round(
    *,
    store: Store,
    usage_store: UsageLogStore,
    worlds: dict[str, LoadedWorld],
    voice_client,
    voice_model_id: str,
    safety_client,
    safety_model_id: str,
    session_id: str,
    config: RoundConfig,
    routing_action: str,
    routing_reason: str,
    degraded: bool,
    facilitator: list[dict],
) -> TableMessageResult:
    """One voice-turn advance of the open round - selector step, then the
    selected voice's turn, then the close when the cap lands. Re-projects
    from the store first (module docstring: the log is the only round
    state), so message-open and continue share this identically."""
    state = project_fresh(session_id, store)
    if not state.round_open:
        raise TableRoundNotOpen(session_id)

    gate_payload = _last_gate_payload(state)
    participant_text = _last_participant_text(state)
    anachronistic_ids = _round_anachronistic_term_ids(worlds)
    voice_message, directive = voice_message_for_round(gate_payload, participant_text, anachronistic_ids)
    labels = _labels(worlds)
    # Everything a voice or the selector reads back from the session -
    # history, context, the selector's window - replays bridged rounds'
    # participant text as the underlying subject (SS77 applied to session
    # memory; engine.api.wiring.replay_transcript's docstring is the full
    # account). Citations and speakers are untouched, so the per-world
    # memory sets read the same entries.
    transcript = replay_transcript(state, anachronistic_ids)

    common = dict(
        round_no=state.round_no, routing_action=routing_action, routing_reason=routing_reason,
        degraded=degraded, facilitator=facilitator,
    )

    if config.cap_reached(state.round_turns):
        # Defensive only: the cap closes the round in the same request that
        # reaches it (below), so a continue should never find this - but a
        # crash between voice_turn and round_closed would, and the honest
        # answer is to close now rather than run turn cap+1.
        turn_no = _close_round(store, state, reason="cap", turns=state.round_turns)
        return TableMessageResult(**common, round_open=False, turn_selected=None, voice=None, position=None, turn_no=turn_no)

    # DIRECT ADDRESS BY NAME (Facilitator Governance SS8, C5): a participant
    # who names exactly one seated Representative gets that voice at the
    # round's opening position - immediately, with no selector call. The
    # detection runs on the participant's RAW message (names are not modern
    # terms; a bridged round's underlying subject carries no names to find).
    direct_address = None
    if state.round_turns == 0:
        name_to_world = {w.frame["representative"]["name"]: k for k, w in worlds.items()}
        direct_address = detect_direct_address(participant_text, name_to_world)
    if direct_address is not None:
        selection = Selection(
            world_key=direct_address, close=False,
            reason="direct address by name - routed immediately, no selector call (Facilitator Governance SS8)",
            degraded=False,
        )
        selector_outcomes = []
    else:
        selector_transcript = "\n\n".join(_attributed_lines(transcript, labels)[-_SELECTOR_TRANSCRIPT_WINDOW:])
        seated_lines = "\n".join(
            f"- {w.frame['representative']['name']}, {w.frame['representative']['role_label']} of {w.frame['display_name']} (world_key: {k})"
            for k, w in worlds.items()
        )
        transcript_speakers = [t["speaker"] for t in transcript if t.get("speaker") not in ("participant", "facilitator", None)]
        selection, selector_outcomes = select_speaker(
            safety_client,
            safety_model_id,
            message=voice_message,
            transcript_text=selector_transcript or "(nothing yet - this is the opening turn)",
            seated_lines=seated_lines,
            world_keys=list(state.world_keys),
            last_speaker=state.round_speakers[-1] if state.round_speakers else None,
            close_allowed=config.close_allowed(state.round_turns),
            transcript_speakers=transcript_speakers,
            round_speakers=list(state.round_speakers),
        )
    usage_records = []
    for outcome in selector_outcomes:
        if rec := _maybe_record_usage(
            outcome, session_id=session_id, call_kind="turn_selector", model_id=safety_model_id, world_key=selection.world_key
        ):
            usage_records.append(rec)

    if selection.close:
        for rec in usage_records:
            usage_store.append(rec)
        turn_no = _close_round(store, state, reason="selector_closed", turns=state.round_turns)
        return TableMessageResult(**common, round_open=False, turn_selected=None, voice=None, position=None, turn_no=turn_no)

    position = state.round_turns + 1
    selected_payload = {
        "round_no": state.round_no, "position": position, "world_key": selection.world_key,
        "reason": selection.reason, "degraded": selection.degraded,
    }
    events.validate("turn_selected", selected_payload)
    store.append(session_id=session_id, event_uuid=str(uuid.uuid4()), event_type="turn_selected", payload=selected_payload)

    world = worlds[selection.world_key]
    already_told, already_figures, already_glosses = _already_sets_for(selection.world_key, transcript)
    history, pending = table_history_for(selection.world_key, transcript, labels)

    try:
        voice_event, voice_usage = run_voice_turn_for_world(
            voice_client=voice_client,
            voice_model_id=voice_model_id,
            world=world,
            participant_message=voice_message,
            directive=directive,
            session_id=session_id,
            already_told_ids=already_told,
            already_bridged_figure_ids=already_figures,
            already_bridged_gloss_ids=already_glosses,
            history=history,
            context_prefix=_context_prefix(pending),
            usage_world_key=selection.world_key,
        )
    except UnhandledRoutingAction:
        raise
    except Exception as exc:
        # Same seam as the interview's handle_message: the events written so
        # far this request (participant_message, gate, turn_selected) stay
        # in the log as evidence; the round stays open and a continue can
        # retry the voice turn.
        for rec in usage_records:
            usage_store.append(rec)
        raise ProviderCallFailed(str(exc)) from exc

    usage_records.extend(voice_usage)
    events.validate("voice_turn", voice_event)
    store.append(session_id=session_id, event_uuid=str(uuid.uuid4()), event_type="voice_turn", payload=voice_event)
    for rec in usage_records:
        usage_store.append(rec)

    turns_now = position
    if config.cap_reached(turns_now):
        # state still reflects pre-turn bookkeeping; round_no is unchanged
        # and the close carries the real turn count.
        turn_no = _close_round(store, state, reason="cap", turns=turns_now)
        return TableMessageResult(
            **common, round_open=False, turn_selected=selected_payload, voice=voice_event, position=position, turn_no=turn_no
        )
    return TableMessageResult(
        **common, round_open=True, turn_selected=selected_payload, voice=voice_event, position=position, turn_no=None
    )


def _handle_table_message_unlocked(
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
    config: RoundConfig | None = None,
) -> TableMessageResult:
    config = config or RoundConfig()
    state = project_fresh(session_id, store)
    if not state.exists:
        raise SessionNotFound(session_id)
    if state.closed:
        raise SessionClosed(session_id)
    if state.mode != "table":
        raise TableRoundNotOpen(f"session {session_id} is not a table session")
    if state.round_open:
        raise TableRoundStillOpen(session_id)

    worlds = _seated_worlds(state, world_loader, registry)
    representative_names = [worlds[k].frame["representative"]["name"] for k in state.world_keys]
    anachronistic_ids = _round_anachronistic_term_ids(worlds)

    msg_uuid = client_msg_id or str(uuid.uuid4())
    participant_event_uuid = (
        str(uuid.uuid5(uuid.NAMESPACE_URL, f"cic:{session_id}:{msg_uuid}")) if client_msg_id else str(uuid.uuid4())
    )
    if client_msg_id and store.event_exists(participant_event_uuid):
        raise DuplicateMessage(session_id)
    participant_payload = {"text": text, "client_msg_id": msg_uuid}
    events.validate("participant_message", participant_payload)
    store.append(session_id=session_id, event_uuid=participant_event_uuid, event_type="participant_message", payload=participant_payload)
    round_no = state.round_no + 1

    gate_run = run_gate(
        session_id=session_id,
        safety_client=safety_client,
        safety_model_id=safety_model_id,
        participant_message=text,
        pressed=state.pressed,
        anachronistic_term_ids=anachronistic_ids,
        track_b_accumulator=state.safety.track_b_accumulator,
    )
    opening = open_table_round(
        gate_run=gate_run,
        representative_names=representative_names,
        track_a_last=state.safety.track_a_last,
        rounds_completed=state.turn_count,
        anachronistic_term_ids=anachronistic_ids,
    )

    # The gate payload is written AFTER open_table_round - the bridge branch
    # updates its directive in place (engine.m4.round's own
    # record-what-the-voices-were-handed discipline), and a continue reads
    # this event back to re-derive what the voices are answering.
    events.validate("gate_decision", opening.gate)
    store.append(session_id=session_id, event_uuid=str(uuid.uuid4()), event_type="gate_decision", payload=opening.gate)
    for safety_state in opening.safety_state_events:
        events.validate("safety_state", safety_state)
        store.append(session_id=session_id, event_uuid=str(uuid.uuid4()), event_type="safety_state", payload=safety_state)
    for rec in gate_run.usage_records:
        usage_store.append(rec)

    # THE PRESSED FLAG - identical rule and identical reason as the
    # interview's handle_message (its own comment block is authoritative):
    # fires on the in-world answer, recording that this class has HAD its
    # first answer.
    out_of_scope_class = (opening.gate.get("out_of_scope") or {}).get("class")
    if opening.routing_action == "voice_with_directive" and out_of_scope_class in PRESSABLE_CLASSES:
        pressed_payload = {"class": out_of_scope_class}
        events.validate("escalation_pressed", pressed_payload)
        store.append(session_id=session_id, event_uuid=str(uuid.uuid4()), event_type="escalation_pressed", payload=pressed_payload)

    for fe in opening.facilitator_events:
        events.validate("facilitator_turn", fe)
        store.append(session_id=session_id, event_uuid=str(uuid.uuid4()), event_type="facilitator_turn", payload=fe)

    if opening.session_capped:
        capped_state = project_fresh(session_id, store)
        turn_no = _close_round(store, capped_state, reason="cap", turns=0)
        closed_payload = {"reason": "cap"}
        events.validate("session_closed", closed_payload)
        store.append(session_id=session_id, event_uuid=str(uuid.uuid4()), event_type="session_closed", payload=closed_payload)
        return TableMessageResult(
            round_no=round_no, round_open=False, routing_action=opening.routing_action,
            routing_reason=opening.routing_reason, degraded=opening.degraded,
            facilitator=opening.facilitator_events, turn_selected=None, voice=None, position=None,
            turn_no=turn_no, session_closed=True,
        )

    if not opening.voices_speak:
        # A governed round: the Facilitator's events above are the whole
        # round (Artifact-7 SS2) - closed immediately, turns: 0.
        governed_state = project_fresh(session_id, store)
        turn_no = _close_round(store, governed_state, reason="selector_closed", turns=0)
        return TableMessageResult(
            round_no=round_no, round_open=False, routing_action=opening.routing_action,
            routing_reason=opening.routing_reason, degraded=opening.degraded,
            facilitator=opening.facilitator_events, turn_selected=None, voice=None, position=None, turn_no=turn_no,
        )

    return _advance_open_round(
        store=store, usage_store=usage_store, worlds=worlds,
        voice_client=voice_client, voice_model_id=voice_model_id,
        safety_client=safety_client, safety_model_id=safety_model_id,
        session_id=session_id, config=config,
        routing_action=opening.routing_action, routing_reason=opening.routing_reason,
        degraded=opening.degraded, facilitator=opening.facilitator_events,
    )


def _continue_table_round_unlocked(
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
    config: RoundConfig | None = None,
) -> TableMessageResult:
    config = config or RoundConfig()
    state = project_fresh(session_id, store)
    if not state.exists:
        raise SessionNotFound(session_id)
    if state.closed:
        raise SessionClosed(session_id)
    if state.mode != "table" or not state.round_open:
        raise TableRoundNotOpen(session_id)

    worlds = _seated_worlds(state, world_loader, registry)
    gate_payload = _last_gate_payload(state)
    return _advance_open_round(
        store=store, usage_store=usage_store, worlds=worlds,
        voice_client=voice_client, voice_model_id=voice_model_id,
        safety_client=safety_client, safety_model_id=safety_model_id,
        session_id=session_id, config=config,
        routing_action=gate_payload.get("route") or "voice_pass_through",
        routing_reason="continuing the open round",
        degraded=bool(gate_payload.get("degraded")),
        facilitator=[],
    )


def handle_table_message(*, session_id: str, **kwargs) -> TableMessageResult:
    """Public entry - one advance in flight per table session (see
    _advance_lock). All real work is _handle_table_message_unlocked."""
    with _advance_lock(session_id):
        return _handle_table_message_unlocked(session_id=session_id, **kwargs)


def continue_table_round(*, session_id: str, **kwargs) -> TableMessageResult:
    """Public entry - same single-advance guarantee as handle_table_message:
    the mid-round-reload race (two clients continuing one round) is refused
    as TableAdvanceInFlight instead of doubling voice turns and spend."""
    with _advance_lock(session_id):
        return _continue_table_round_unlocked(session_id=session_id, **kwargs)
