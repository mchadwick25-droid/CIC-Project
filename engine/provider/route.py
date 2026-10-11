"""Which model route this process uses. Bedrock is the primary route and the
default; the Anthropic API is a manual second, chosen only by setting
CIC_MODEL_ROUTE=anthropic, and its key lives only in the live-tests
environment, never on Render (decision 55). Nothing here reads a key."""
import os

BEDROCK = "bedrock"
ANTHROPIC = "anthropic"
ROUTES = (BEDROCK, ANTHROPIC)
ROUTE_ENV = "CIC_MODEL_ROUTE"


class UnknownRouteError(Exception):
    """CIC_MODEL_ROUTE named a route this build does not have. A typo must
    stop the start, never fall back to a route nobody chose."""


def active_route() -> str:
    raw = os.environ.get(ROUTE_ENV, "").strip().lower()
    if not raw:
        return BEDROCK
    if raw not in ROUTES:
        raise UnknownRouteError(f"{ROUTE_ENV}={raw!r} is not one of {', '.join(ROUTES)}")
    return raw


def build_route(region: str, voice_pattern: str, safety_pattern: str):
    """(client, voice_model_id, safety_model_id) for the active route. One
    client serves both roles."""
    route = active_route()
    if route == ANTHROPIC:
        from engine.provider import anthropic_direct as provider
        return (
            provider.make_client(),
            provider.resolve_model_id(voice_pattern),
            provider.resolve_model_id(safety_pattern),
        )
    from engine.provider import bedrock as provider
    return (
        provider.make_client(region),
        provider.resolve_model_id(voice_pattern, region),
        provider.resolve_model_id(safety_pattern, region),
    )
