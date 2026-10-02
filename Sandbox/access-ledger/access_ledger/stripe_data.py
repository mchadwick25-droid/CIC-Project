"""Reads succeeded charges from Stripe for reconciliation."""
import urllib.parse
from typing import Iterator

from .checkout import API_BASE, Transport


def list_charges(secret_key: str, transport: Transport, created_gte: int, page_size: int = 100) -> Iterator[dict]:
    headers = {"Authorization": f"Bearer {secret_key}"}
    starting_after = None
    while True:
        params = {"limit": str(page_size), "created[gte]": str(created_gte)}
        if starting_after:
            params["starting_after"] = starting_after
        status, payload = transport("GET", f"{API_BASE}/charges?{urllib.parse.urlencode(params)}", headers, "")
        if status >= 400:
            raise RuntimeError(f"Stripe returned {status} listing charges")
        for charge in payload.get("data", []):
            yield charge
        if not payload.get("has_more") or not payload.get("data"):
            return
        starting_after = payload["data"][-1]["id"]


def to_reconcile_charge(charge: dict) -> dict:
    dispute = charge.get("dispute")
    status = None
    if isinstance(dispute, dict):
        raw = dispute.get("status")
        status = "won" if raw == "won" else "lost" if raw == "lost" else "open"
    elif dispute:
        status = "open"
    return {
        "payment_intent": charge.get("payment_intent"),
        "amount": charge.get("amount", 0),
        "amount_refunded": charge.get("amount_refunded", 0),
        "status": charge.get("status"),
        "dispute_status": status,
    }
