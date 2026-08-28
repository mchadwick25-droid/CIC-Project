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
    """C3 (decided 2026-08-28): floor and cap ship as configuration -
    floor 3 / cap 4 default, 6 allowed. The floor binds the selector's
    close option (Table Process V1.0 SS2: it never forces every voice to
    speak); the cap binds absolutely. 6 is the ceiling the turn-cap
    incident's re-test verified (Process V1.0 SS6), not an arbitrary max."""
    floor: int = 3
    cap: int = 4

    def __post_init__(self):
        if not (1 <= self.floor <= self.cap <= 6):
            raise ValueError(f"round config must satisfy 1 <= floor <= cap <= 6, got floor={self.floor} cap={self.cap}")

    def close_allowed(self, round_turns: int) -> bool:
        return round_turns >= self.floor

    def cap_reached(self, round_turns: int) -> bool:
        return round_turns >= self.cap


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
# 1-4 voice turns, and capping the session at 10 voice turns would have
# handed a participant roughly three questions - a cost unit leaking into
# the participant's experience. Rounds are what a participant actually
# spends. The NUMBER is set from the measured live runs (token counts,
# engine/m4/reports/live-table-report-2.json): a compact-turn round ran
# ~1.8k output tokens across 3 voice turns, so 5 rounds sits in the same
# output-token envelope as the interview's measured 10-turn cap, with
# input growth to be re-measured by a live long-session run before this
# number is treated as load-bearing (same discipline as the interview
# cap's own memory-growth measurement; no $ figure until a reconciled
# invoice, principle 13). Config, not constant law - swappable without
# touching round semantics.
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
