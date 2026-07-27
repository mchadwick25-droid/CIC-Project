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
    pre_track_a_active: bool = False
    pre_track_a_severity: str | None = None
    pre_track_b_active: bool = False
    closing_turns: list | None = None
    modern_term_match: dict | None = None
    should_check_wind_down: bool = False

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

    out.should_check_wind_down = (
        include_closing
        and not out.higher_intercept and out.closing_turns is None
        and not out.is_modern_term_bridge and not out.is_epistemology_bridge
        and state.closing_stage == "none"
    )
    return out


def run_table_checks(state, working_messages, spoken_this_round,
                     world_id, world_ids) -> tuple[list, dict]:
    """The five per-round table checks. Returns (signals, guidance) where
    guidance maps world_id -> correction text for medium/high findings -
    one string per world (latest wins), exactly the streaming path's
    queueing rule."""
    from app.graph.state import ConversationState
    from app.graph.nodes import (
        check_convergence,
        check_cross_world_vocabulary_drift,
        check_dominance,
        check_length_ceiling,
        check_question_stacking,
    )

    check_state = ConversationState(
        messages=working_messages,
        world_id=world_id,
        world_ids=world_ids,
    )
    signals, guidance = [], {}
    for signal in (
        check_dominance(check_state)
        + check_convergence(check_state, spoken_this_round)
        + check_cross_world_vocabulary_drift(check_state, spoken_this_round)
        + check_length_ceiling(check_state, spoken_this_round)
        + check_question_stacking(check_state, spoken_this_round)
    ):
        signals.append(signal)
        if signal.world_id and signal.severity in ("medium", "high"):
            guidance[signal.world_id] = signal.description
    return signals, guidance


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
    sessions,
    session_id: str,
) -> None:
    """The streaming path's invisible-governance tail, verbatim in logic:
    table checks + per-message drift checks (queued per-world), the
    read-latest-merge session write (a blind overwrite could clobber a
    message that arrived after 'done' went out), then wind-down sensing -
    each half in its own fail-open try/except, independent concerns."""
    from app.prompts.facilitator_prompts import get_representative_message_name

    try:
        from app.graph.nodes import (
            check_drift_for_message,
            generate_reroot_guidance,
        )

        new_drift_signals: list = []
        new_pending_guidance: dict[str, str] = {}
        if is_multi_world and turns_completed >= 1:
            signals, guidance = run_table_checks(
                state, working_messages, spoken_this_round,
                state.world_id, state.world_ids)
            new_drift_signals.extend(signals)
            new_pending_guidance.update(guidance)

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
                new_pending_guidance[msg_world_id] = generate_reroot_guidance(signal)

        latest_state = sessions.get(session_id)
        if latest_state is not None:
            latest_state.drift_signals = (
                list(latest_state.drift_signals) + new_drift_signals)
            latest_state.pending_guidance = {
                **latest_state.pending_guidance, **new_pending_guidance}
            sessions[session_id] = latest_state
    except Exception:
        # invisible governance fails silently by design - the participant
        # already has their response
        pass

    try:
        if should_check_wind_down:
            from app.graph.closing_sequence import classify_wind_down
            if classify_wind_down(state, message):
                wind_down_state = sessions.get(session_id)
                if wind_down_state is not None:
                    wind_down_state.closing_stage = "anything_else_asked"
                    sessions[session_id] = wind_down_state
    except Exception:
        pass
