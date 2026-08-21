"""$/turn engineering unit (CiC-Program-Spec.md M8, SS7 Cost model). Spec
principle 13: "no $/token or $/turn figure quoted onward until measured on
the billing provider" - this module computes the unit's STRUCTURE (token
counts by category, ready to multiply by a price table) but returns an
explicitly unpriced result when no price table is supplied. It never ships
a default/invented price table - that would be exactly the guessed figure
principle 13 exists to prevent (see engine/provider/preflight.py's own
docstring: "never quotes a $/turn or $/token figure"). A real price table
is a Mark-approved input, sourced from the reconciled AWS invoice
(preflight's still-pending third leg) or an explicit published-rate
decision, never hardcoded here.
"""
from dataclasses import dataclass

from engine.provider.bedrock import NormalizedUsage

TURNS_PER_HOUR_CONVENTION = 12  # CiC-Program-Spec.md SS7: "reported in $/participant-hour at the declared 12 turns/hour convention" - the one place this constant is defined; every reporting surface should import it, not restate "12"


@dataclass(frozen=True)
class PriceTable:
    """$ per token, by category - supplied by the caller, never a module
    default. `source` names where these numbers came from (e.g. "AWS
    invoice 2026-09 reconciliation" or "published Bedrock rate card,
    approved by Mark 2026-09-01") - a price table with no source is as
    untrustworthy as no price table at all, so source is required, not
    optional."""

    input_per_token: float
    output_per_token: float
    cache_write_per_token: float
    cache_read_per_token: float
    source: str


@dataclass(frozen=True)
class CostEstimate:
    priced: bool
    dollars: float | None
    token_breakdown: dict[str, int]
    price_source: str | None


def estimate_cost(usage: NormalizedUsage, price_table: PriceTable | None = None) -> CostEstimate:
    breakdown = {
        "input_tokens": usage.input_tokens,
        "output_tokens": usage.output_tokens,
        "cache_creation_input_tokens": usage.cache_creation_input_tokens,
        "cache_read_input_tokens": usage.cache_read_input_tokens,
    }
    if price_table is None:
        return CostEstimate(priced=False, dollars=None, token_breakdown=breakdown, price_source=None)
    dollars = (
        usage.input_tokens * price_table.input_per_token
        + usage.output_tokens * price_table.output_per_token
        + usage.cache_creation_input_tokens * price_table.cache_write_per_token
        + usage.cache_read_input_tokens * price_table.cache_read_per_token
    )
    return CostEstimate(priced=True, dollars=dollars, token_breakdown=breakdown, price_source=price_table.source)


def dollars_per_hour(dollars_per_turn: float) -> float:
    return dollars_per_turn * TURNS_PER_HOUR_CONVENTION
