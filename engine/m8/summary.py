"""Per-session usage summaries (CiC-Program-Spec.md M8: "per-session and
per-participant attribution"). Pure aggregation over already-logged
UsageRecords - reads engine.m8.log_store's output, never makes a call
itself. Per-participant attribution is the same shape at a coarser grain
once accounts exist (spec: "an account is a list of session ids, nothing
more" - not built in Phase 1); per-session is the real unit today.
"""
from dataclasses import dataclass, field

from .usage import UsageRecord


@dataclass(frozen=True)
class SessionUsageSummary:
    session_id: str
    call_count: int
    input_tokens: int
    output_tokens: int
    cache_creation_input_tokens: int
    cache_read_input_tokens: int
    by_call_kind: dict[str, int] = field(default_factory=dict)


def summarize_session(records: list[UsageRecord]) -> SessionUsageSummary:
    if not records:
        raise ValueError("no records to summarize")
    session_ids = {r.session_id for r in records}
    if len(session_ids) > 1:
        raise ValueError(f"records span multiple sessions: {sorted(session_ids)} - summarize one session at a time")

    by_call_kind: dict[str, int] = {}
    for r in records:
        by_call_kind[r.call_kind] = by_call_kind.get(r.call_kind, 0) + 1

    return SessionUsageSummary(
        session_id=records[0].session_id,
        call_count=len(records),
        input_tokens=sum(r.usage.input_tokens for r in records),
        output_tokens=sum(r.usage.output_tokens for r in records),
        cache_creation_input_tokens=sum(r.usage.cache_creation_input_tokens for r in records),
        cache_read_input_tokens=sum(r.usage.cache_read_input_tokens for r in records),
        by_call_kind=by_call_kind,
    )
