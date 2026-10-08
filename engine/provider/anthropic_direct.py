"""The Anthropic API client behind the provider seam: a manual second route
for testing (decision 55). It builds only when CIC_MODEL_ROUTE=anthropic and
CIC_ANTHROPIC_API_KEY is set; the key belongs to the live-tests environment
and is never set on Render. Same Messages API shape as the Bedrock client,
so usage normalizes through the same function."""
import os

from anthropic import Anthropic

from engine.provider import guard, route
from engine.provider.bedrock import ModelResolutionError, normalize_usage  # noqa: F401 - the one usage normalizer, shared by both routes

KEY_ENV = "CIC_ANTHROPIC_API_KEY"


class RouteNotEnabledError(Exception):
    """The Anthropic route was asked for without being chosen and keyed, or
    from the Render deployment."""


def make_client() -> Anthropic:
    if os.environ.get("RENDER"):
        raise RouteNotEnabledError("the Anthropic route is never built on Render, whatever the settings hold")
    if route.active_route() != route.ANTHROPIC:
        raise RouteNotEnabledError(f"the Anthropic client builds only when {route.ROUTE_ENV}={route.ANTHROPIC}")
    key = os.environ.get(KEY_ENV)
    if not key:
        raise RouteNotEnabledError(f"{KEY_ENV} is not set")
    live_test = guard.admit()
    return guard.wrap(Anthropic(api_key=key), live_test, provider="anthropic")


def resolve_model_id(pattern: str) -> str:
    """The Anthropic route names models without the Bedrock prefix, so the
    pattern's own `us.anthropic.` prefix is dropped before matching. Lists the
    live catalogue (a metadata call, no model spend) and requires exactly one
    match, as the Bedrock side does."""
    needle = pattern.lower().removeprefix("us.").removeprefix("global.").removeprefix("anthropic.")
    models = [m.id for m in make_client().models.list(limit=1000).data]
    matches = [m for m in models if needle in m.lower()]
    if not matches:
        raise ModelResolutionError(f"no Anthropic model matched pattern {pattern!r}")
    if len(matches) > 1:
        raise ModelResolutionError(f"pattern {pattern!r} matched {len(matches)} models, ambiguous: {', '.join(matches)}")
    guard.note_model(matches[0])
    return matches[0]
