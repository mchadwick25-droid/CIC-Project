"""Table round semantics (Artifact-7 SS2), compute-only - same discipline
as engine.m4.turn: no store reads or writes of their own; the caller
(engine.api.wiring) owns the event log. One participant message opens one
round; this module resolves what kind of round it is (governed by the
Facilitator, bridged, or ordinary) from the gate pass that already ran, and
carries the round's rules (floor/cap, close eligibility) as configuration.

The gate runs ONCE per round (engine.m4.turn.run_gate) - it is
message-level and world-agnostic. Routing then resolves at the round level:
a crisis is a crisis at any table, and the governed routes (acute safety,
check-in, system-nature, etic) are the Facilitator's whole round - no voice
speaks, and the round closes with turns: 0. Track B's non-acute signal
keeps the interview's own semantics (a dependency check spoken, then an
explicit continue path back to the voices - Program-Spec SS8). The bridge
speaks the modern sense once for the whole table, and every subsequent
voice turn in the round answers the term-free underlying subject.

Continue re-derivation: a turn-at-a-time continue (Artifact-7 SS6) arrives
in a fresh request with no memory of the open round beyond the log, so the
voice-facing message and directive must be re-derivable from the
gate_decision event alone. voice_message_for_round is that derivation,
used identically at round open and on every continue - one code path, so
the two can never disagree about what the voices are answering.
"""
from dataclasses import dataclass

from engine.m1.loader import load_fleet_records
from engine.m4 import crisis_resources, facilitator_turns
from engine.m4.turn import GateRun
from engine.m5.routing import Directive, directive_without_terms


@dataclass(frozen=True)
class RoundConfig:
    """C3 (decided 2026-08-28): floor ships as configuration - floor 3,
    binding the selector's close option (Table Process V1.0 SS2: it never
    forces every voice to speak). Unconditional, every round, every table
    size - this predates and is untouched by the seat-scaled cap below.

    SEAT-SCALED CAP (Mark's ruling, 2026-09-05, superseding this thread's
    own first pass at a broad-only 5/6 minimum): "for 2 voices and a
    participant, the max turns should be 5... for 3 voices the cap is 6" -
    applied to EVERY round regardless of how it opened (his explicit
    scoping, walked through and confirmed), not only a genuinely-open one.
    The "4 / 5 being the ultimate zone" language in that same ruling is
    deliberately NOT a second mechanical floor - his own point 3 ("no hard
    cap or post-conversation monitoring... just a small increased
    pressure") and his direct confirmation both place it as guidance in the
    selector's own prompt (engine.m4.turn_selector.round_facts), never a
    second code-enforced gate; cap_for is the one hard number here. Two
    seats and three are the only seatings a table ever has (Artifact-7
    SS1: world_keys 2-3), so a plain mapping is honest about these being
    two authored numbers, not a formula with a principle behind it.

    EXIT CONDITION (Mark's own check, 2026-09-05, confirmed already true of
    this design rather than newly built): the moment cap_reached fires -
    turn 5 for a 2-seat table, turn 6 for a 3-seat table - the round loop
    (engine.api.table_wiring._advance_open_round) writes round_closed in
    that same request and returns round_open: False. There is no
    subsequent generation of any kind until a new participant_message
    opens the next round (Artifact-7 SS6's turn-at-a-time transport:
    /continue on a closed round is a 409, not a retry point) - the
    generation cycle ends unambiguously there and the system waits.

    CONTEXT PASSING (Mark's own check, same date, also already true): each
    voice turn is one real request against the persisted event log, not a
    batch of turns generated from one snapshot - _advance_open_round
    re-projects the FULL transcript from the store (project_fresh) on
    every single call, so turn 4 is built from turns 1-3 exactly as they
    were actually written, never from a stale copy taken before turn 1 ran.
    This is inherent to the production architecture (Artifact-3's
    event-sourced store), not a property of any one round-length change."""
    floor: int = 3
    # A tuple of pairs, not a dict (independent review, 2026-09-05): a
    # mutable dict field on a frozen dataclass defeats `frozen` twice over -
    # instances become unhashable, AND `cap_by_seats[2] = 99` mutates the
    # config out from under `frozen`'s own guarantee, silently, with no
    # error. A tuple of pairs is a real value, not a mutable container.
    cap_by_seats: tuple = ((2, 5), (3, 6))
    default_cap: int = 4  # unreached in practice - every real table seats 2 or 3

    def __post_init__(self):
        # The §6 ceiling the turn-cap incident verified (Process V1.0 §6)
        # applies to every configured cap, not just the old single `cap`
        # field it used to be - restored here after the seat-scaling
        # refactor dropped it entirely (independent review, 2026-09-05).
        caps = [c for _, c in self.cap_by_seats] + [self.default_cap]
        if not all(1 <= self.floor <= c <= 6 for c in caps):
            raise ValueError(
                f"round config must satisfy 1 <= floor <= cap <= 6 for every seat count, "
                f"got floor={self.floor} cap_by_seats={self.cap_by_seats} default_cap={self.default_cap}"
            )

    def cap_for(self, num_seats: int) -> int:
        return dict(self.cap_by_seats).get(num_seats, self.default_cap)

    def close_allowed(self, round_turns: int) -> bool:
        return round_turns >= self.floor

    def cap_reached(self, round_turns: int, num_seats: int) -> bool:
        return round_turns >= self.cap_for(num_seats)


@dataclass(frozen=True)
class RoundOpening:
    """What the gate decided this round is. voices_speak False is a governed
    round: the facilitator_events are the whole round, and the caller writes
    round_closed (turns: 0) immediately. session_capped is the C4-provisional
    session cap firing - the caller additionally closes the session."""
    routing_action: str
    routing_reason: str
    gate: dict
    safety_state_events: list[dict]
    facilitator_events: list[dict]
    voices_speak: bool
    degraded: bool
    session_capped: bool = False


# C4 RESOLVED (2026-08-28, Mark's delegation of the full C4 range): the
# table session cap is counted in COMPLETED ROUNDS, not voice turns. The
# interview's voice-turn unit was the right cost proxy for a mode where one
# exchange is one voice turn; at a table one participant exchange spends
# several voice turns, and capping the session at 10 voice turns would have
# handed a participant roughly three questions - a cost unit leaking into
# the participant's experience. Rounds are what a participant actually
# spends. The NUMBER was originally set from a measured live run (token
# counts, engine/m4/reports/live-table-report-2.json): a compact-turn round
# ran ~1.8k output tokens across 3 voice turns, sizing 5 rounds against the
# interview's measured 10-turn cap.
#
# THAT BASIS NO LONGER HOLDS (independent review, 2026-09-05, flagged
# rather than silently left stale): RoundConfig.cap_for now runs rounds to
# 5 turns at a 2-seat table and 6 at a 3-seat table (soft target 4/5),
# not the 3 turns this number was measured against - roughly 1.3-2x the
# per-round output tokens the 5-round session figure was sized on,
# depending on how often a round actually reaches its target versus its
# cap. TABLE_SESSION_ROUND_CAP itself was NOT re-measured or re-sized as
# part of the round-length change that invalidated its own basis - a real
# gap, not a decision. Needs its own live long-session measurement before
# either number is treated as load-bearing again (same discipline the
# interview cap's own memory-growth measurement already holds itself to;
# no $ figure until a reconciled invoice, principle 13). Config, not
# constant law - swappable without touching round semantics.
TABLE_SESSION_ROUND_CAP = 5


def open_table_round(
    *,
    gate_run: GateRun,
    representative_names: list[str],
    track_a_last: dict | None,
    rounds_completed: int,
    anachronistic_term_ids: set,
) -> RoundOpening:
    """Resolve one gated participant message into the round it opens.
    Mirrors engine.m4.turn.run_turn's branches with the table's own
    round-level semantics (Artifact-7 SS2); the branch ORDER matters the
    same way it does there - the cap yields only to a real crisis."""
    gate_result = gate_run.gate_result
    action = gate_result.routing.action
    safety_outcome = gate_run.safety_outcome
    common = dict(
        routing_reason=gate_result.routing.reason,
        gate=gate_run.gate,
        safety_state_events=gate_run.safety_state_events,
        degraded=gate_result.degraded,
    )

    is_acute_crisis = (
        action == "safety_turn" and not safety_outcome.failed and safety_outcome.value.get("signal") == "ACUTE_DISTRESS"
    )
    # THE CAP OVERRIDES EVERYTHING EXCEPT A REAL CRISIS - same rule, same
    # placement as the interview (checked after routing, before any voice
    # call is spent). C4: the table unit is completed ROUNDS - see
    # TABLE_SESSION_ROUND_CAP's own comment for the resolution and its
    # measured basis.
    if not is_acute_crisis and rounds_completed >= TABLE_SESSION_ROUND_CAP:
        return RoundOpening(
            routing_action="session_cap_turn",
            **{**common, "routing_reason": f"session round cap reached ({TABLE_SESSION_ROUND_CAP} rounds)"},
            facilitator_events=[facilitator_turns.table_session_cap_turn(representative_names)],
            voices_speak=False,
            session_capped=True,
        )

    if is_acute_crisis:
        # Governed: at a table no voice speaks in a crisis round (Artifact-7
        # SS2) - the interview's optional empathy stream has no single voice
        # to belong to here, and the crisis append never depended on it
        # anyway (crisis_resources' own stage-5 proof point). The
        # Mark-approved resources text is reused verbatim; only its
        # {representative_name} slot is filled with the or-joined names.
        facilitator_event = crisis_resources.append_crisis_resources_turn(
            signal=safety_outcome.value["signal"],
            stream_text=None,
            stream_failed=True,
            representative_name=facilitator_turns.names_or_phrase(representative_names),
            acute_level=safety_outcome.value["acute_level"],
            already_fired=track_a_last is not None,
        )
        return RoundOpening(routing_action=action, **common, facilitator_events=[facilitator_event], voices_speak=False)

    if action == "safety_turn":
        # Track B non-acute: a dependency dynamic, not a crisis - the check
        # is spoken and the round proceeds ordinarily (the explicit continue
        # path back to the voices, Program-Spec SS8).
        return RoundOpening(
            routing_action=action,
            **common,
            facilitator_events=[facilitator_turns.table_dependency_check_turn(representative_names)],
            voices_speak=True,
        )

    if action == "check_in_turn":
        return RoundOpening(routing_action=action, **common, facilitator_events=[facilitator_turns.check_in_turn()], voices_speak=False)

    if action == "system_nature_turn":
        return RoundOpening(routing_action=action, **common, facilitator_events=[facilitator_turns.system_nature_turn()], voices_speak=False)

    if action == "etic_turn":
        facilitator_event = facilitator_turns.etic_turn(gate_run.reader_outcome.value["out_of_scope"]["class"])
        return RoundOpening(routing_action=action, **common, facilitator_events=[facilitator_event], voices_speak=False)

    if action == "bridge_turn":
        fired = _fired_terms(gate_run.gate, anachronistic_term_ids)
        facilitator_event, _underlying_subject = facilitator_turns.bridge_turn(fired)
        # Same record-what-the-voices-were-handed discipline as the
        # interview's bridge branch: the gate payload's directive is updated
        # to the barred-terms directive BEFORE the caller writes it, so the
        # logged gate_decision agrees with what every voice turn in this
        # round receives - and so voice_message_for_round can re-derive the
        # directive from the log alone on a continue.
        barred = [term for record in fired for term in (record.get("display_terms") or [])]
        bridge_directive = directive_without_terms(gate_run.reader_outcome.value, barred)
        gate_run.gate["directive"] = _directive_payload(bridge_directive)
        return RoundOpening(routing_action=action, **common, facilitator_events=[facilitator_event], voices_speak=True)

    if action in ("voice_with_directive", "voice_pass_through"):
        return RoundOpening(routing_action=action, **common, facilitator_events=[], voices_speak=True)

    from engine.m4.turn import UnhandledRoutingAction

    raise UnhandledRoutingAction(f"routing action {action!r} has no table round content wired up - see engine.m4.turn's own guard")


def _fired_terms(gate_payload: dict, anachronistic_term_ids: set) -> list[dict]:
    """The bridge's fired modern_term records - the identical derivation to
    the interview's bridge branch (engine.m4.turn), from the gate_decision
    payload's already-resolved modern_terms: term flagged AND round-
    anachronistic AND carried by the fleet. For a table,
    anachronistic_term_ids is the ROUND's set - a term is round-
    anachronistic only when it is anachronistic for every seated world
    (Artifact-7 SS2: a term inside one seated world's horizon is not bridged
    away from a voice that can answer it); the caller computes that
    intersection deterministically, which is what lets a continue re-derive
    the same fired list from the log alone."""
    fleet = load_fleet_records()
    return [
        fleet[t["term_id"]]
        for t in (gate_payload.get("modern_terms") or [])
        if t.get("term_id") in anachronistic_term_ids and t.get("term_id") in fleet
    ]


def _directive_payload(directive: Directive | None) -> dict | None:
    # Same shape as engine.m4.turn._directive_payload - reproduced rather
    # than imported to keep this module's import surface off turn.py's
    # private helpers; test_round pins the two against each other.
    return None if directive is None else {
        "asks": list(directive.asks),
        "register_note": directive.register_note,
        "suspend_register_statement_1": directive.suspend_register_statement_1,
        "ambiguity_options": list(directive.ambiguity_options),
    }


def directive_from_payload(payload: dict | None) -> Directive | None:
    """The inverse of the gate payload's directive dict, for continue
    re-derivation (module docstring): a fresh request rebuilds the Directive
    the voices are answering under from the logged gate_decision alone."""
    if payload is None:
        return None
    return Directive(
        asks=list(payload.get("asks") or []),
        register_note=payload.get("register_note"),
        suspend_register_statement_1=bool(payload.get("suspend_register_statement_1")),
        ambiguity_options=list(payload.get("ambiguity_options") or []),
    )


def voice_message_for_round(gate_payload: dict, participant_message: str, anachronistic_term_ids: set) -> tuple[str, Directive | None]:
    """What every voice turn in this round answers, derived from the logged
    gate_decision + the participant's message - used identically at round
    open and on every continue so the two cannot disagree. For the bridge
    route the voices receive the term-free underlying subject and never see
    the participant's modern word (Program-Spec SS77); for every other
    voice-speaking route, the message itself."""
    directive = directive_from_payload(gate_payload.get("directive"))
    if gate_payload.get("route") == "bridge_turn":
        fired = _fired_terms(gate_payload, anachronistic_term_ids)
        subjects = " ".join(t["underlying_subject"].strip() for t in fired if t.get("underlying_subject"))
        return subjects, directive
    return participant_message, directive
