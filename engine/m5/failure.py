"""Timeout/failure semantics (Artifact-4 SS4). Both gate calls are modeled
as a CallOutcome the caller already resolved (ok / timeout / error /
parse_failure - "structured-output parse failure = failure, no salvage
parsing") - this module never makes or awaits a call itself; it only
decides what a completed-or-failed pair of outcomes means for routing,
which is exactly the part that's pure code and testable without a live
model.
"""
from dataclasses import dataclass

from .routing import RoutingDecision, route

FAILURE_STATUSES = {"timeout", "error", "parse_failure"}


@dataclass(frozen=True)
class CallOutcome:
    status: str  # ok | timeout | error | parse_failure
    value: dict | None = None
    raw_usage: object | None = None  # the SDK's own Usage object, when status="ok" - engine.m8's attribution reads this; never re-derived, only carried

    @property
    def failed(self) -> bool:
        return self.status in FAILURE_STATUSES


@dataclass(frozen=True)
class GateResult:
    routing: RoutingDecision
    degraded: bool
    needs_async_safety_reclassification: bool


def resolve_gate(
    *, safety_outcome: CallOutcome, reader_outcome: CallOutcome, pressed: dict[str, bool], anachronistic_term_ids: set[str]
) -> GateResult:
    if reader_outcome.failed:
        # Reader fails/times out -> pass-through: the voice answers the raw
        # message with no directive (the pre-guard state). Safety's own
        # outcome doesn't change this - "both fail" collapses to the same
        # pass-through, per spec.
        return GateResult(
            routing=RoutingDecision(action="voice_pass_through", reason="reader failed/timed out - pass-through"),
            degraded=True,
            needs_async_safety_reclassification=safety_outcome.failed,
        )

    reader = reader_outcome.value
    if safety_outcome.failed:
        # Safety fails/times out -> the turn proceeds (fail open toward the
        # pre-guard state); routing still applies the reader's own rules
        # (2-5), just without the safety-triggered rule 1. The caller is
        # responsible for actually scheduling the async re-classification
        # and, if it retroactively fires acute, interjecting on the next
        # event with the safety turn.
        routing = route(safety=None, reader=reader, pressed=pressed, anachronistic_term_ids=anachronistic_term_ids)
        return GateResult(routing=routing, degraded=True, needs_async_safety_reclassification=True)

    routing = route(safety=safety_outcome.value, reader=reader, pressed=pressed, anachronistic_term_ids=anachronistic_term_ids)
    return GateResult(routing=routing, degraded=False, needs_async_safety_reclassification=False)


def should_page_operator(recent_degraded_flags: list[bool]) -> bool:
    """"Two consecutive degraded gate turns" pages the operator (Artifact-6
    SS3). Takes the tail of a session's degraded flags in turn order -
    pure, so it's testable without any real paging integration existing
    yet."""
    return len(recent_degraded_flags) >= 2 and recent_degraded_flags[-1] and recent_degraded_flags[-2]
