"""Hosted Stripe Checkout for one-time packs.

Sessions are created server-side. The visitor id travels as client_reference_id
and the pack code in metadata, so the webhook can grant units without trusting
the browser. No card data touches this service.
"""
import urllib.parse
from dataclasses import dataclass
from typing import Callable, Protocol

from .stripe_events import Catalogue

API_BASE = "https://api.stripe.com/v1"


class Transport(Protocol):
    def __call__(self, method: str, url: str, headers: dict[str, str], body: str) -> tuple[int, dict]: ...


class CheckoutError(Exception):
    pass


@dataclass(frozen=True)
class CheckoutSession:
    session_id: str
    url: str


def session_params(visitor_id: str, sku_code: str, catalogue: Catalogue, product_names: dict[str, str], success_url: str, cancel_url: str) -> dict[str, str]:
    sku = catalogue.get(sku_code)
    if sku is None:
        raise CheckoutError(f"unknown pack {sku_code!r}")
    return {
        "mode": "payment",
        "client_reference_id": visitor_id,
        "success_url": success_url,
        "cancel_url": cancel_url,
        "metadata[sku]": sku_code,
        "payment_intent_data[metadata][sku]": sku_code,
        "payment_intent_data[metadata][visitor_id]": visitor_id,
        "line_items[0][quantity]": "1",
        "line_items[0][price_data][currency]": sku.currency,
        "line_items[0][price_data][unit_amount]": str(sku.amount_cents),
        "line_items[0][price_data][product_data][name]": product_names.get(sku_code, sku_code),
    }


def create_checkout_session(
    secret_key: str, visitor_id: str, sku_code: str, catalogue: Catalogue, product_names: dict[str, str],
    success_url: str, cancel_url: str, transport: Transport, idempotency_key: str | None = None,
) -> CheckoutSession:
    params = session_params(visitor_id, sku_code, catalogue, product_names, success_url, cancel_url)
    headers = {"Authorization": f"Bearer {secret_key}", "Content-Type": "application/x-www-form-urlencoded"}
    if idempotency_key:
        headers["Idempotency-Key"] = idempotency_key
    status, payload = transport("POST", f"{API_BASE}/checkout/sessions", headers, urllib.parse.urlencode(params))
    if status >= 400 or "url" not in payload or "id" not in payload:
        raise CheckoutError(f"Stripe returned {status}: {payload.get('error', {}).get('message', 'no session url')}")
    return CheckoutSession(session_id=payload["id"], url=payload["url"])
