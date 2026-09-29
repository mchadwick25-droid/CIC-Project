"""The one approved, sourced price table this codebase ships (spec
principle 13: no $/token figure quoted onward until it's either measured
on the billing provider or an explicit published-rate decision - see
engine.m8.cost's own docstring). Extracted out of engine.m8.live_cost_run
(2026-09-28) so a second caller - engine.api.wiring.get_usage_summary,
the usage dashboard's cost figure - reuses the same approved numbers
instead of a second hardcoded copy that could drift from this one.

Covers exactly the two models this deployment actually calls
(engine.api.config's _DEFAULT_VOICE_MODEL_PATTERN /
_DEFAULT_SAFETY_MODEL_PATTERN). A call whose kind isn't in
_PRICE_BY_CALL_KIND has no approved price and must come back unpriced
(engine.m8.cost.estimate_cost's own contract with price_table=None) -
never a guessed table for an unrecognized kind.
"""
from engine.m8.cost import PriceTable

PRICE_TABLE_SOURCE = (
    "Anthropic published API rate card (platform.claude.com/docs/en/about-claude/pricing, "
    "fetched 2026-08-25); Bedrock's own pricing page was not independently fetchable in this "
    "environment (egress to aws.amazon.com blocked) - Bedrock has historically mirrored "
    "Anthropic's direct per-token rates for the same models, not independently re-verified here"
)

SONNET_4_5_PRICE_TABLE = PriceTable(
    input_per_token=3.00 / 1_000_000,
    output_per_token=15.00 / 1_000_000,
    cache_write_per_token=3.75 / 1_000_000,  # 5-minute cache write (Bedrock's own default TTL)
    cache_read_per_token=0.30 / 1_000_000,
    source=PRICE_TABLE_SOURCE,
)
HAIKU_4_5_PRICE_TABLE = PriceTable(
    input_per_token=1.00 / 1_000_000,
    output_per_token=5.00 / 1_000_000,
    cache_write_per_token=1.25 / 1_000_000,
    cache_read_per_token=0.10 / 1_000_000,
    source=PRICE_TABLE_SOURCE,
)

# Which model_id each call_kind is actually called with (grepped from the
# real call sites, not assumed): engine/m4/turn.py passes safety_model_id
# for safety_call/reader_call and voice_model_id for voice_generation,
# voice_generation_retry, and self_revision; engine/api/table_wiring.py
# passes safety_model_id for turn_selector. preflight (usage.py's
# SYSTEM_SESSION_ID sentinel, admin/evidence calls) is deliberately absent
# below - it's never a participant cost this dashboard should count.
_PRICE_BY_CALL_KIND: dict[str, PriceTable] = {
    "safety_call": HAIKU_4_5_PRICE_TABLE,
    "reader_call": HAIKU_4_5_PRICE_TABLE,
    "turn_selector": HAIKU_4_5_PRICE_TABLE,
    "voice_generation": SONNET_4_5_PRICE_TABLE,
    "voice_generation_retry": SONNET_4_5_PRICE_TABLE,
    "self_revision": SONNET_4_5_PRICE_TABLE,
}


def price_for_call_kind(call_kind: str) -> PriceTable | None:
    """None for a call_kind outside the priced classes above (preflight,
    or a future kind this table hasn't been updated for) - the caller
    prices what it can and leaves the rest explicitly unpriced, never
    guesses a table."""
    return _PRICE_BY_CALL_KIND.get(call_kind)
