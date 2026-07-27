"""S4.1 - the governance layer both endpoints traverse (blueprint S4.1).

Behavior-preserving extraction from main.py's two endpoint bodies:

- classify_pre_turn(): the classify-then-route intercept phase, with the
  chain order preserved EXACTLY as the streaming path resolved it -
  epistemology-bridge preempts frame-breaker preempts relational-safety
  (all three classified concurrently, priority applied after; the
  relational-safety classification always runs and its state mutation
  happens only when no higher intercept fired); then closing-sequence
  routing; then the modern-term bridge (whose ordering dependency on the
  Representative's input is real and documented at its old call site).
  The plain endpoint traverses the same function with the intercepts it
  has always had (frame-breaker + relational-safety); the streaming
  endpoint enables the full chain. Same layer, declared capabilities -
  not two diverging copies.

- run_table_checks(): the five per-round table checks (dominance,
  convergence, cross-world vocabulary drift, length ceiling, question
  stacking) with medium/high findings queued as per-world guidance. The
  streaming path always ran these; the plain endpoint now runs them too
  on multi-world turns - THE one intended behavior delta of S4.1,
  declared in the parity report.

- run_post_round_governance(): the streaming path's full invisible-
  governance tail (table checks + per-message drift checks + the
  read-latest-merge session write + wind-down sensing), verbatim in
  logic, with its two independent fail-open try/except blocks intact.

Every LLM-dependent function is imported function-locally so the S4.1
replay harness's module-attribute patching reaches each call - the same
property main.py's endpoint bodies had.
"""
from __future__ import annotations

import asyncio
from dataclasses import dataclass, field


@dataclass
class PreTurnOutcome:
    is_epistemology_bridge: bool = False
    is_frame_breaker: bool = False
    is_relational_safety_firing: bool = False
    rs_classification: dict = field(default_factory=lambda: {"category": "NO_SIGNAL"})
    rs_updates: dict = field(default_factory=dict)
    # S4.2 observability additions (behavior-neutral): the RAW classifier
    # results before the chain's priority is applied - what the event log
    # records so a discarded classification is still diagnosable (A.4)
    frame_breaker_raw: bool = False
    rs_raw: dict = field(default_factory=dict)
    pre_track_a_active: bool = False
    pre_track_a_severity: str | None = None
    pre_track_b_active: bool = False
    closing_turns: list | None = None
    modern_term_match: dict | None = None
    should_check_wind_down: bool = False
    # S4.6: the repair intercept's outcome - None, or the selected
    # hold/concede strategy for the challenged Representative's turn
    repair: dict | None = None
    # S4.7: the restricted-offer grounding plan (Pass 1 §6.4) - None, or
    # {"term", "directive"} for the answering turn; repair takes the one
    # directive slot when both exist
    grounding_offer: dict | None = None

    @property
    def higher_intercept(self) -> bool:
        return (self.is_frame_breaker or self.is_relational_safety_firing
                or self.is_epistemology_bridge)

    @property
    def is_modern_term_bridge(self) -> bool:
        return self.modern_term_match is not None


async def classify_pre_turn(
    state,
    message: str,
    *,
    include_epistemology: bool,
    include_closing: bool,
    include_modern_term: bool,
    include_repair: bool = False,
) -> PreTurnOutcome:
    """The pre-turn intercept phase. Priority and concurrency semantics
    are byte-for-byte the streaming endpoint's (see its original inline
    comments, preserved in git history at main.py pre-S4.1): the three
    classifiers have no data dependency, so they run concurrently and
    the sequential code's exact priority is applied to the results."""
    from app.graph.nodes import (
        classify_frame_breaker,
        classify_relational_safety,
        relational_safety_should_fire,
        update_relational_safety_state,
    )

    out = PreTurnOutcome()

    frame_breaker_task = asyncio.to_thread(classify_frame_breaker, message)
    relational_safety_task = asyncio.to_thread(
        classify_relational_safety, state, message)

    if include_epistemology:
        from app.graph.epistemology_bridge import classify_epistemology_bridge
        epistemology_task = asyncio.to_thread(
            classify_epistemology_bridge, message)
        (out.is_epistemology_bridge, frame_breaker_result,
         relational_safety_result) = await asyncio.gather(
            epistemology_task, frame_breaker_task, relational_safety_task)
    else:
        frame_breaker_result, relational_safety_result = await asyncio.gather(
            frame_breaker_task, relational_safety_task)

    # epistemology-bridge wins if it fired; else frame-breaker; else
    # relational-safety - the sequential code's exact priority
    out.frame_breaker_raw = frame_breaker_result
    out.rs_raw = relational_safety_result
    out.is_frame_breaker = (False if out.is_epistemology_bridge
                             else frame_breaker_result)

    out.pre_track_a_active = state.track_a_active
    out.pre_track_a_severity = state.track_a_severity
    out.pre_track_b_active = state.track_b_active
    if not out.is_frame_breaker and not out.is_epistemology_bridge:
        out.rs_classification = relational_safety_result
        out.rs_updates = update_relational_safety_state(
            state, out.rs_classification)
        for field_name, value in out.rs_updates.items():
            setattr(state, field_name, value)
        out.is_relational_safety_firing = relational_safety_should_fire(
            state, out.rs_classification, out.rs_updates)

    # Sensed closing sequence: runs after the intercepts (a crisis during
    # a wind-down is a crisis, not a closing) and gates the bridge below
    if include_closing and not out.higher_intercept and state.closing_stage != "none":
        from app.graph.closing_sequence import route_closing_stage
        decision = route_closing_stage(state, message)
        if decision["action"] == "resume":
            state.closing_stage = "none"
        else:
            state.closing_stage = decision["to"]
            out.closing_turns = decision["turns"]

    # Modern-term bridge: deliberately sequential - its firing changes the
    # Representative's input message, so it cannot overlap generation
    if (include_modern_term and not out.higher_intercept
            and out.closing_turns is None and state.closing_stage == "none"):
        from app.graph.modern_term_bridge import classify_modern_term
        seated_world_ids = (state.world_ids if len(state.world_ids) > 0
                             else [state.world_id])
        out.modern_term_match = classify_modern_term(message, seated_world_ids)

    # S4.6: the repair classifier - the SIXTH intercept, deliberately
    # LAST in chain order: it runs only when every safety intercept, the
    # epistemology bridge, the closing sequence, and the modern-term
    # bridge have all declined (a pushback phrasing that is actually
    # distress has already routed to relational safety above - the
    # battery's crisis-overlap case). Its hit never replaces the turn;
    # it conditions the challenged Representative's own answer.
    if (include_repair and not out.higher_intercept
            and out.closing_turns is None and state.closing_stage == "none"
            and not out.is_modern_term_bridge):
        from app.graph.repair_classifier import run_repair_intercept
        from app.prompts.facilitator_prompts import get_representative_message_name
        world_ids = (state.world_ids if len(state.world_ids) > 0
                     else [state.world_id])
        name_to_wid = {get_representative_message_name(w): w
                       for w in world_ids}
        last_rep_world_id, last_rep_text = None, None
        for msg in reversed(state.messages):
            wid = name_to_wid.get(getattr(msg, "name", None))
            if wid is not None:
                last_rep_world_id = wid
                last_rep_text = str(msg.content)
                break
        out.repair = run_repair_intercept(message, last_rep_world_id,
                                          last_rep_text)

    # S4.7 (Pass 1 §6.4): the restricted-offer grounding plan -
    # deterministic, zero LLM calls; computed only when the turn is
    # otherwise ordinary and repair has not claimed the directive slot
    if (not out.higher_intercept and out.closing_turns is None
            and state.closing_stage == "none"
            and not out.is_modern_term_bridge and out.repair is None):
        from app.graph.nodes import plan_restricted_offer
        out.grounding_offer = plan_restricted_offer(state, message)

    out.should_check_wind_down = (
        include_closing
        and not out.higher_intercept and out.closing_turns is None
        and not out.is_modern_term_bridge and not out.is_epistemology_bridge
        and state.closing_stage == "none"
    )
    return out


def queue_guidance(pending: dict, world_id: str, signal_type: str,
                   severity: str, text: str) -> dict:
    """S4.3 (Pass 1 §6.5): THE one gate every guidance writer goes
    through. Each world's slot is a priority queue kept sorted by the one
    signal ordering (nodes.signal_rank - the same ordering the monitor's
    one-finding-per-turn slot uses, extended to the table signals), so
    contention is decided by governance priority instead of by statement
    order in a background block - the old last-writer-wins string slot
    could cost a fabrication its slot to a stylistic complaint.

    A newer entry of the same signal_type supersedes the older one (the
    correction for a defect class goes stale the moment a fresher finding
    of that class exists); different types coexist in priority order and
    are delivered one per turn, so nothing is silently dropped anymore.
    Pure function: returns a new dict, mutates nothing (the caller
    appends the matching guidance_queued event)."""
    from app.graph.nodes import signal_rank

    entries = [e for e in (pending.get(world_id) or [])
               if e["signal_type"] != signal_type]
    entries.append({"signal_type": signal_type, "severity": severity,
                    "text": text})
    entries.sort(key=lambda e: signal_rank(e["signal_type"], e["severity"]))
    return {**pending, world_id: entries}


def run_table_checks(state, working_messages, spoken_this_round,
                     world_id, world_ids) -> tuple[list, list]:
    """The five per-round table checks. Returns (signals, guidance_items)
    where guidance_items is a list of (world_id, signal_type, severity,
    text) for every medium/high finding with a world - S4.3: ALL of them
    are handed to the queue_guidance gate by the caller, replacing the
    old one-string-per-world latest-wins dict that silently dropped every
    finding but the last."""
    from app.graph.state import ConversationState
    from app.graph.nodes import (
        check_closing_synthesis,
        check_convergence,
        check_cross_world_vocabulary_drift,
        check_dominance,
        check_length_ceiling,
        check_manufactured_resolution,
        check_misattribution,
        check_question_stacking,
    )

    check_state = ConversationState(
        messages=working_messages,
        world_id=world_id,
        world_ids=world_ids,
    )
    signals, guidance_items = [], []
    # S4.7: the table-check suite grows from five to eight - the
    # convergence split's second half (manufactured_resolution), the
    # misattribution check, and the closing-speaker rule's detection half
    # (closing_synthesis) join per Pass 1 §6.5
    for signal in (
        check_dominance(check_state)
        + check_convergence(check_state, spoken_this_round)
        + check_manufactured_resolution(check_state, spoken_this_round)
        + check_closing_synthesis(check_state, spoken_this_round)
        + check_misattribution(check_state, spoken_this_round)
        + check_cross_world_vocabulary_drift(check_state, spoken_this_round)
        + check_length_ceiling(check_state, spoken_this_round)
        + check_question_stacking(check_state, spoken_this_round)
    ):
        signals.append(signal)
        if signal.world_id and signal.severity in ("medium", "high"):
            guidance_items.append((signal.world_id, signal.signal_type,
                                   signal.severity, signal.description))
    return signals, guidance_items


def run_post_round_governance(
    state,
    message: str,
    *,
    working_messages,
    spoken_this_round,
    turns_completed: int,
    world_ids,
    is_multi_world: bool,
    should_check_wind_down: bool,
    session_id: str,
) -> None:
    """The streaming path's invisible-governance tail, verbatim in logic:
    table checks + per-message drift checks (queued per-world), then
    wind-down sensing - each half in its own fail-open try/except,
    independent concerns.

    S4.2: findings are APPENDED to the event log instead of merged into a
    mutable store. The hand-patched read-latest-merge this replaces
    existed because a blind overwrite could clobber a message that
    arrived after 'done' went out - and the merge itself still carried a
    lost-update window (read latest -> concurrent write -> write back).
    An append has no read-modify-write cycle at all: whatever arrived in
    the meantime is simply earlier in the log, and the projection folds
    both. The race is gone structurally, which is exactly what the S4.2
    race-regression fixture proves."""
    from app.prompts.facilitator_prompts import get_representative_message_name

    try:
        from app.graph.events import EVENT_STORE
        from app.graph.nodes import (
            check_drift_for_message,
            generate_reroot_guidance,
        )

        new_drift_signals: list = []
        # S4.3: every guidance writer goes through the queue_guidance
        # gate - (world_id, signal_type, severity, text) items, ordered
        # by the one signal ranking, nothing dropped by statement order
        guidance_items: list[tuple[str, str, str, str]] = []
        if is_multi_world and turns_completed >= 1:
            signals, table_items = run_table_checks(
                state, working_messages, spoken_this_round,
                state.world_id, state.world_ids)
            new_drift_signals.extend(signals)
            guidance_items.extend(table_items)

        round_turns = (working_messages[-turns_completed:]
                       if turns_completed else [])
        for msg in round_turns:
            msg_world_id = next(
                (wid for wid in world_ids
                 if get_representative_message_name(wid) == msg.name),
                None,
            )
            if msg_world_id is None:
                continue
            signal = check_drift_for_message(msg_world_id, msg.content)
            if signal is None:
                continue
            new_drift_signals.append(signal)
            if signal.severity in ("medium", "high"):
                guidance_items.append((msg_world_id, signal.signal_type,
                                       signal.severity,
                                       generate_reroot_guidance(signal)))

        tail_events: list[tuple[str, dict]] = []
        if new_drift_signals:
            tail_events.append(("drift_signals_appended", {"signals": [
                {"signal_type": s.signal_type, "description": s.description,
                 "severity": s.severity, "world_id": s.world_id}
                for s in new_drift_signals]}))
        for wid, stype, sev, text in guidance_items:
            tail_events.append(("guidance_queued", {
                "world_id": wid,
                "entry": {"signal_type": stype, "severity": sev,
                          "text": text}}))

        # S4.7 (Pass 1 §6.5): the mode-register observation - selector
        # input for the NEXT round, computed once per multi-world round
        if is_multi_world and turns_completed >= 2:
            from app.graph.nodes import classify_round_register
            reg = classify_round_register(state, spoken_this_round, message)
            if reg is not None:
                tail_events.append(("register_observed", reg))

        if tail_events and EVENT_STORE.has(session_id):
            EVENT_STORE.append_many(session_id, tail_events)
    except Exception:
        # invisible governance fails silently by design - the participant
        # already has their response
        pass

    try:
        if should_check_wind_down:
            from app.graph.closing_sequence import classify_wind_down
            from app.graph.events import EVENT_STORE
            fired = classify_wind_down(state, message)
            if EVENT_STORE.has(session_id):
                EVENT_STORE.append(session_id, "classifier_decision", {
                    "classifier": "wind_down", "raw": bool(fired),
                    "applied": bool(fired)})
            if fired and EVENT_STORE.has(session_id):
                EVENT_STORE.append(session_id, "closing_stage_changed",
                                   {"stage": "anything_else_asked"})
    except Exception:
        pass
