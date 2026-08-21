"""Stage-6 gate item: "usage logging with correct cache accounting tested
against raw API shapes" / "parity against raw usage shapes." Never trust
engine.provider.bedrock.normalize_usage's output alone - reconcile every
field it derived back against the raw Bedrock/Anthropic usage object it
came from, so a provider SDK or response-shape change would be CAUGHT here
rather than silently miscounting cost forever (spec SS10's silent-absence
risk, generalized from "does streaming carry cache fields at all" to "does
our own transform stay faithful to whatever the SDK actually returned").
"""
from dataclasses import dataclass

from engine.provider.bedrock import NormalizedUsage


class UsageParityError(Exception):
    """Names exactly which field(s) diverged - never a silent pass, and
    never a vague 'usage mismatch' either."""


@dataclass(frozen=True)
class ParityResult:
    ok: bool
    mismatches: dict[str, tuple[int, int]]  # field -> (raw, normalized)


_FIELDS = ("input_tokens", "output_tokens", "cache_creation_input_tokens", "cache_read_input_tokens")


def check_parity(raw_usage, normalized: NormalizedUsage) -> ParityResult:
    """raw_usage: the SDK's own usage object (duck-typed - the same
    accessor shape whether it came from a non-streaming Message or a
    streaming response's final usage, per the Messages API). A field the
    raw object simply doesn't carry is treated as 0, matching normalize_
    usage's own tolerant getattr - the parity check's job is to confirm
    the two AGREE on that, not to demand a field neither ever required."""
    mismatches = {}
    for field in _FIELDS:
        raw_value = getattr(raw_usage, field, None) or 0
        normalized_value = getattr(normalized, field)
        if raw_value != normalized_value:
            mismatches[field] = (raw_value, normalized_value)
    return ParityResult(ok=not mismatches, mismatches=mismatches)


def assert_parity(raw_usage, normalized: NormalizedUsage) -> None:
    result = check_parity(raw_usage, normalized)
    if not result.ok:
        raise UsageParityError(f"normalize_usage diverged from the raw usage shape on: {result.mismatches}")
