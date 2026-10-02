"""Builds the access service from environment variables.

STRIPE_SECRET_KEY, STRIPE_WEBHOOK_SECRET, ACCESS_DB, ACCESS_INTERNAL_TOKEN,
ACCESS_SUCCESS_URL and ACCESS_CANCEL_URL are required. A STRIPE_SECRET_KEY that
does not start with sk_test_ is refused unless ACCESS_ALLOW_LIVE is set.
"""
import os

from fastapi import FastAPI

from .api import create_app
from .jobs import urllib_transport
from .packs import PACKS, PRODUCT_NAMES


class ConfigError(Exception):
    pass


def build_app(env: dict[str, str] | None = None) -> FastAPI:
    env = env if env is not None else dict(os.environ)
    missing = [k for k in ("STRIPE_SECRET_KEY", "STRIPE_WEBHOOK_SECRET", "ACCESS_DB", "ACCESS_INTERNAL_TOKEN", "ACCESS_SUCCESS_URL", "ACCESS_CANCEL_URL") if not env.get(k)]
    if missing:
        raise ConfigError(f"missing settings: {', '.join(missing)}")
    key = env["STRIPE_SECRET_KEY"]
    if not key.startswith("sk_test_") and env.get("ACCESS_ALLOW_LIVE") not in ("1", "true", "yes"):
        raise ConfigError("a live Stripe key needs ACCESS_ALLOW_LIVE")
    return create_app(
        env["ACCESS_DB"], PACKS, PRODUCT_NAMES, env["ACCESS_INTERNAL_TOKEN"], key, env["STRIPE_WEBHOOK_SECRET"],
        urllib_transport, env["ACCESS_SUCCESS_URL"], env["ACCESS_CANCEL_URL"],
    )
