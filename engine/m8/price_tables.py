"""The one approved, sourced price table this codebase ships (spec
principle 13: no $/token figure quoted onward until it's either measured
on the billing provider or an explicit published-rate decision - see
engine.m8.cost's own docstring). Shared by engine.m8.live_cost_run and
engine.api.wiring.get_usage_summary (the usage dashboard's cost figure),
so both use the same approved numbers instead of a second hardcoded copy
that could drift from this one.

Prices are keyed by model family, matched inside the provider's model id
(a Bedrock inference-profile id such as
us.anthropic.claude-sonnet-4-5-20250929-v1:0 carries claude-sonnet-4-5).
A model with no row here has no approved price and comes back unpriced
(engine.m8.cost.estimate_cost's own contract with price_table=None) -
never a guessed table for an unrecognized model.
"""
import dataclasses

from engine.m8.cost import PriceTable

PRICE_TABLE_SOURCE = (
    "Anthropic published API rate card (platform.claude.com/docs/en/about-claude/pricing, "
    "fetched August 2026); Bedrock's own pricing page was not independently fetchable in this "
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
FAMILY_5_PRICE_SOURCE = (
    "Anthropic published API rate card as carried in the Claude API reference bundled with "
    "Claude Code (model table cached September 2026); 5-minute cache writes at 1.25x input; "
    "Bedrock's own rates for these models not independently verified"
)
SONNET_5_5_PRICE_TABLE = PriceTable(
    input_per_token=2.00 / 1_000_000,
    output_per_token=10.00 / 1_000_000,
    cache_write_per_token=2.50 / 1_000_000,
    cache_read_per_token=0.20 / 1_000_000,
    source=FAMILY_5_PRICE_SOURCE,
)
OPUS_5_5_PRICE_TABLE = PriceTable(
    input_per_token=4.00 / 1_000_000,
    output_per_token=20.00 / 1_000_000,
    cache_write_per_token=5.00 / 1_000_000,
    cache_read_per_token=0.20 / 1_000_000,
    source=FAMILY_5_PRICE_SOURCE,
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
    "citation_propose": HAIKU_4_5_PRICE_TABLE,
    "citation_verify": HAIKU_4_5_PRICE_TABLE,
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


_PRICE_BY_MODEL_FAMILY: dict[str, PriceTable] = {
    "claude-sonnet-4-5": SONNET_4_5_PRICE_TABLE,
    "claude-haiku-4-5": HAIKU_4_5_PRICE_TABLE,
    "claude-sonnet-5-5": SONNET_5_5_PRICE_TABLE,
    "claude-opus-5-5": OPUS_5_5_PRICE_TABLE,
}


def price_for_model(model_id: str) -> PriceTable | None:
    """The table whose model family appears in model_id, or None when no
    family or more than one family matches."""
    matches = [table for family, table in _PRICE_BY_MODEL_FAMILY.items() if family in (model_id or "")]
    return matches[0] if len(matches) == 1 else None


def price_for_call(call_kind: str, model_id: str) -> PriceTable | None:
    """A participant call's price, keyed by the model it actually ran on.
    None for a call_kind outside the participant classes (preflight) and
    for a model with no approved row."""
    if call_kind not in _PRICE_BY_CALL_KIND:
        return None
    return price_for_model(model_id)



# Bedrock's regional inference profiles (an id starting us., eu., ...) bill
# about 10% above list; global. profiles and the Anthropic API bill at list.
# The factor is the figure the Billing Audit measured, not a published rate.
BEDROCK_REGIONAL_PREMIUM = 1.10
_REGIONAL_PREFIXES = ("us.", "eu.", "apac.", "jp.", "au.", "ca.")


def route_factor(provider: str, model_id: str) -> float:
    if provider == "bedrock" and (model_id or "").lower().startswith(_REGIONAL_PREFIXES):
        return BEDROCK_REGIONAL_PREMIUM
    return 1.0


def price_for_route(call_kind: str, model_id: str, provider: str) -> PriceTable | None:
    """price_for_call scaled to what the route bills. The door keeps calling
    price_for_call (list price) and applies its own invoice factor."""
    table = price_for_call(call_kind, model_id)
    factor = route_factor(provider, model_id)
    if table is None or factor == 1.0:
        return table
    return dataclasses.replace(
        table,
        input_per_token=table.input_per_token * factor,
        output_per_token=table.output_per_token * factor,
        cache_write_per_token=table.cache_write_per_token * factor,
        cache_read_per_token=table.cache_read_per_token * factor,
        source=f"{table.source}; x{factor} Bedrock regional-profile premium (Billing Audit measurement)",
    )
