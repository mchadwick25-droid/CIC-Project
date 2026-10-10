"""M8: usage attribution (CiC-Program-Spec.md M8: "per-session and
per-participant attribution with zero unattributed calls"). Builds
directly on engine.provider.bedrock.NormalizedUsage - this module never
re-derives cache/token math, only attaches WHO/WHAT/WHEN to an already-
normalized usage object.

"Zero unattributed calls" is enforced structurally, not just checked after
the fact: record_usage requires a real session_id - there is no default,
no empty-string fallback. Administrative/non-session calls (preflight,
ad-hoc evidence scripts) use the explicit SYSTEM_SESSION_ID sentinel
rather than silently passing nothing - "unattributed" means "nobody can
say which session/participant this call belonged to," and a tagged system
call is not that.
"""
import uuid
from dataclasses import dataclass

from engine.provider.bedrock import NormalizedUsage
from engine.provider.guard import active_live_test_name
from engine.provider.route import active_route

# Explicit tag for admin/evidence calls that are genuinely not part of a
# participant session (preflight, this module's own re-measurement
# scripts) - never a blank/None fallback, so "attributed" always means
# something real, even for non-session calls.
SYSTEM_SESSION_ID = "_system"


@dataclass(frozen=True)
class UsageRecord:
    trace_id: str
    session_id: str  # required - SYSTEM_SESSION_ID for non-session calls, never blank
    call_kind: str  # e.g. "safety_call" | "reader_call" | "voice_generation" | "turn_selector" | "preflight" (citations_call retired: M4 step 5, LIVE-GENERATION-DESIGN.md Fork 1 - one call now carries its own grounding inline)
    model_id: str
    provider: str
    usage: NormalizedUsage
    # Which world this call belongs to (Artifact-7 SS7): at a table,
    # session_id alone no longer answers "which world cost what" - several
    # voices share one session. Every one-to-one call carries its session's
    # world: the gate calls (safety, reader), the voice calls and the
    # citation calls. None only where no single world owns the call: the
    # Table's gate call, which serves several worlds at once, preflight,
    # and rows written before world_key existed. It is
    # nullable rather than defaulted to a sentinel so an old row is never
    # rewritten to claim a world it never carried.
    world_key: str | None = None
    # The approved live test this call ran under (decision 56); None for a
    # conversation, which is not a test.
    live_test: str | None = None

    @property
    def is_attributed(self) -> bool:
        return bool(self.session_id)


def new_trace_id() -> str:
    return str(uuid.uuid4())


def record_usage(
    *, usage: NormalizedUsage, session_id: str, call_kind: str, model_id: str, provider: str | None = None, trace_id: str | None = None,
    world_key: str | None = None,
) -> UsageRecord:
    if not session_id:
        raise ValueError("session_id is required - use usage.SYSTEM_SESSION_ID for non-session calls, never blank")
    provider = provider or active_route()
    return UsageRecord(
        trace_id=trace_id or new_trace_id(), session_id=session_id, call_kind=call_kind, model_id=model_id, provider=provider, usage=usage,
        world_key=world_key, live_test=active_live_test_name(),
    )


def zero_unattributed(records: list[UsageRecord]) -> bool:
    """The literal stage-6 gate item, as a checkable predicate over a real
    batch of records - not just "the type made it hard to forget," but "here
    is a batch of records and none of them are unattributed.\""""
    return all(r.is_attributed for r in records)
