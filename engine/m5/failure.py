"""Timeout/failure semantics (Artifact-4 SS4). Both gate calls are modeled
as a CallOutcome the caller already resolved (ok / timeout / error /
parse_failure - "structured-output parse failure = failure, no salvage
parsing") - this module never makes or awaits a call itself; it only
decides what a completed-or-failed pair of outcomes means for routing,
which is exactly the part that's pure code and testable without a live
model.
"""
from dataclasses import dataclass

from .routing import ACUTE_SIGNALS, RoutingDecision, check_in_due, route

FAILURE_STATUSES = {"timeout", "error", "parse_failure"}

# route() never touches its `reader` argument until after the safety checks -
# an acute or harmful-dynamic signal, or a check-in that is due, resolves to
# safety_turn/check_in_turn without ever dereferencing reader. So when the
# reader call fails but safety succeeded and one of those holds, routing can
# and must proceed on safety alone.


@dataclass(frozen=True)
class CallOutcome:
    status: str  # ok | timeout | error | parse_failure
    value: dict | None = None
    raw_usage: object | None = None  # the SDK's own Usage object, when status="ok" - engine.m8's attribution reads this; never re-derived, only carried

    @property
    def failed(self) -> bool:
        return self.status in FAILURE_STATUSES

    @property
    def rate_limited(self) -> bool:
        """The call failed because the provider throttled it (HTTP 429)."""
        return self.status == "error" and bool(self.value and self.value.get("rate_limited"))


@dataclass(frozen=True)
class GateResult:
    routing: RoutingDecision
    degraded: bool


SAFETY_FAILED = RoutingDecision(action="safety_unread_turn", reason="safety call failed - fixed Facilitator line with the redirect, never the voice")


def resolve_gate(
    *,
    safety_outcome: CallOutcome,
    reader_outcome: CallOutcome,
    pressed: dict[str, bool],
    anachronistic_term_ids: set[str],
    message: str,
    check_ins_shown: frozenset[str] | set[str] = frozenset(),
) -> GateResult:
    # Safety fails or times out
    # -> the Facilitator's fixed line with the redirect, whatever the reader
    # said. A message no one has read for risk never reaches the voice; the
    # participant is told it was not read and is given the redirect, never a
    # question to answer first.
    if safety_outcome.failed:
        return GateResult(routing=SAFETY_FAILED, degraded=True)

    if reader_outcome.failed:
        # Reader fails/times out. A successful safety classification is never
        # discarded because the reader failed on the same turn: safety_turn
        # and check_in_turn do not need a reader, so routing on safety alone
        # is safe for those signals.
        if safety_outcome.value["signal"] in ACUTE_SIGNALS or check_in_due(safety_outcome.value, check_ins_shown):
            routing = route(
                safety=safety_outcome.value,
                reader=None,
                pressed=pressed,
                anachronistic_term_ids=anachronistic_term_ids,
                message=message,
                check_ins_shown=check_ins_shown,
            )
            return GateResult(routing=routing, degraded=True)
        # Reader failed and safety found nothing -> pass-through: the voice
        # answers the raw message with no directive.
        return GateResult(
            routing=RoutingDecision(action="voice_pass_through", reason="reader failed/timed out - pass-through"),
            degraded=True,
        )

    routing = route(
        safety=safety_outcome.value, reader=reader_outcome.value, pressed=pressed,
        anachronistic_term_ids=anachronistic_term_ids, message=message, check_ins_shown=check_ins_shown,
    )
    return GateResult(routing=routing, degraded=False)


def should_page_operator(recent_degraded_flags: list[bool]) -> bool:
    """"Two consecutive degraded gate turns" pages the operator (Artifact-6
    SS3). Takes the tail of a session's degraded flags in turn order -
    pure, so it's testable without any real paging integration existing
    yet."""
    return len(recent_degraded_flags) >= 2 and recent_degraded_flags[-1] and recent_degraded_flags[-2]
