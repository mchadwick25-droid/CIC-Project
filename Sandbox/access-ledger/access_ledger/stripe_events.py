"""Stripe webhook handling: signature check and ledger updates.

Access is granted only from a verified event, never from a browser redirect.
Each event id is processed once, and each grant, refund and dispute entry has a
unique source reference, so a replayed event changes nothing.
"""
import hashlib
import hmac
import sqlite3
import time
from dataclasses import dataclass
from datetime import datetime, timezone

from .ledger import Ledger


@dataclass(frozen=True)
class Sku:
    units: int
    amount_cents: int
    currency: str


Catalogue = dict[str, Sku]


@dataclass(frozen=True)
class EventResult:
    outcome: str
    purchase_id: str | None = None


def verify_signature(payload: bytes, header: str, secret: str, tolerance_seconds: int = 300, now: float | None = None) -> bool:
    parts: dict[str, list[str]] = {}
    for item in header.split(","):
        key, _, value = item.strip().partition("=")
        parts.setdefault(key, []).append(value)
    try:
        timestamp = int(parts["t"][0])
    except (KeyError, ValueError):
        return False
    if abs((now if now is not None else time.time()) - timestamp) > tolerance_seconds:
        return False
    expected = hmac.new(secret.encode(), f"{timestamp}.".encode() + payload, hashlib.sha256).hexdigest()
    return any(hmac.compare_digest(expected, candidate) for candidate in parts.get("v1", []))


def _now(now: datetime | None) -> str:
    return (now or datetime.now(timezone.utc)).isoformat()


def _purchase_by_intent(conn: sqlite3.Connection, payment_intent: str | None):
    if not payment_intent:
        return None
    return conn.execute(
        "SELECT purchase_id, visitor_id, units, amount_cents, status FROM purchases WHERE payment_intent = ?", (payment_intent,),
    ).fetchone()


def _reversed_units(conn: sqlite3.Connection, purchase_id: str) -> int:
    return -int(
        conn.execute(
            "SELECT COALESCE(SUM(delta), 0) FROM access_ledger WHERE purchase_id = ? AND kind IN ('reverse','adjust')", (purchase_id,),
        ).fetchone()[0]
    )


def _checkout_completed(conn: sqlite3.Connection, ledger: Ledger, obj: dict, catalogue: Catalogue, now: datetime | None) -> EventResult:
    purchase_id = obj.get("id")
    visitor_id = obj.get("client_reference_id")
    sku_code = (obj.get("metadata") or {}).get("sku")
    if not (purchase_id and visitor_id and sku_code):
        return EventResult("invalid")
    sku = catalogue.get(sku_code)
    if sku is None:
        return EventResult("unknown_sku", purchase_id)
    existing = conn.execute("SELECT status FROM purchases WHERE purchase_id = ?", (purchase_id,)).fetchone()
    if existing is not None and existing[0] in ("granted", "amount_mismatch"):
        return EventResult("already_recorded", purchase_id)
    amount, currency = obj.get("amount_total"), (obj.get("currency") or "").lower()
    if amount != sku.amount_cents or currency != sku.currency.lower():
        status = "amount_mismatch"
    elif obj.get("payment_status") == "paid":
        status = "granted"
    else:
        status = "pending"
    if existing is None:
        conn.execute(
            "INSERT INTO purchases (purchase_id, payment_intent, visitor_id, sku, units, amount_cents, currency, status, created_at)"
            " VALUES (?,?,?,?,?,?,?,?,?)",
            (purchase_id, obj.get("payment_intent"), visitor_id, sku_code, sku.units, amount or 0, currency, status, _now(now)),
        )
    elif status != "pending":
        conn.execute("UPDATE purchases SET status = ? WHERE purchase_id = ?", (status, purchase_id))
    if status == "granted":
        ledger.grant_paid(visitor_id, sku.units, purchase_id, now=now)
    return EventResult(status, purchase_id)


def _async_succeeded(conn: sqlite3.Connection, ledger: Ledger, obj: dict, now: datetime | None) -> EventResult:
    row = conn.execute(
        "SELECT visitor_id, units, status FROM purchases WHERE purchase_id = ?", (obj.get("id"),),
    ).fetchone()
    if row is None:
        return EventResult("unknown_purchase", obj.get("id"))
    if row[2] != "pending":
        return EventResult("already_recorded", obj.get("id"))
    conn.execute("UPDATE purchases SET status = 'granted' WHERE purchase_id = ?", (obj["id"],))
    ledger.grant_paid(row[0], row[1], obj["id"], now=now)
    return EventResult("granted", obj["id"])


def _async_failed(conn: sqlite3.Connection, obj: dict) -> EventResult:
    cur = conn.execute("UPDATE purchases SET status = 'failed' WHERE purchase_id = ? AND status = 'pending'", (obj.get("id"),))
    return EventResult("failed" if cur.rowcount else "already_recorded", obj.get("id"))


def _refunded(conn: sqlite3.Connection, ledger: Ledger, obj: dict, now: datetime | None) -> EventResult:
    purchase = _purchase_by_intent(conn, obj.get("payment_intent"))
    if purchase is None or purchase[4] != "granted":
        return EventResult("unknown_purchase")
    purchase_id, visitor_id, units, _amount, _status = purchase
    charged, refunded = obj.get("amount") or 0, obj.get("amount_refunded") or 0
    if charged <= 0:
        return EventResult("invalid", purchase_id)
    target = min(units, units * refunded // charged)
    delta = target - _reversed_units(conn, purchase_id)
    if delta <= 0:
        return EventResult("already_recorded", purchase_id)
    ledger.reverse_paid(visitor_id, delta, purchase_id, f"refund:{obj.get('id')}:{refunded}", now=now)
    return EventResult("reversed", purchase_id)


def _dispute_created(conn: sqlite3.Connection, ledger: Ledger, obj: dict, now: datetime | None) -> EventResult:
    purchase = _purchase_by_intent(conn, obj.get("payment_intent"))
    if purchase is None or purchase[4] != "granted":
        return EventResult("unknown_purchase")
    purchase_id, visitor_id, units, _amount, _status = purchase
    delta = units - _reversed_units(conn, purchase_id)
    if delta <= 0:
        return EventResult("already_recorded", purchase_id)
    ledger.reverse_paid(visitor_id, delta, purchase_id, f"dispute:{obj.get('id')}", now=now)
    return EventResult("reversed", purchase_id)


def _dispute_closed(conn: sqlite3.Connection, ledger: Ledger, obj: dict, now: datetime | None) -> EventResult:
    if obj.get("status") != "won":
        return EventResult("no_change")
    purchase = _purchase_by_intent(conn, obj.get("payment_intent"))
    if purchase is None:
        return EventResult("unknown_purchase")
    purchase_id, visitor_id, _units, _amount, _status = purchase
    held_back = conn.execute(
        "SELECT COALESCE(SUM(-delta), 0) FROM access_ledger WHERE source_ref = ?", (f"dispute:{obj.get('id')}",),
    ).fetchone()[0]
    if held_back <= 0:
        return EventResult("no_change", purchase_id)
    ledger.adjust_paid(visitor_id, int(held_back), purchase_id, f"dispute_won:{obj.get('id')}", now=now)
    return EventResult("restored", purchase_id)


def apply_event(conn: sqlite3.Connection, event: dict, catalogue: Catalogue, now: datetime | None = None) -> EventResult:
    """Applies one verified Stripe event in a single transaction. A repeated
    event id returns outcome 'duplicate' and changes nothing."""
    event_id, event_type = event.get("id"), event.get("type")
    if not (event_id and event_type):
        return EventResult("invalid")
    obj = (event.get("data") or {}).get("object") or {}
    ledger = Ledger(conn)
    conn.execute("BEGIN IMMEDIATE")
    try:
        if conn.execute("SELECT 1 FROM stripe_events WHERE event_id = ?", (event_id,)).fetchone():
            conn.execute("COMMIT")
            return EventResult("duplicate")
        if event_type == "checkout.session.completed":
            result = _checkout_completed(conn, ledger, obj, catalogue, now)
        elif event_type == "checkout.session.async_payment_succeeded":
            result = _async_succeeded(conn, ledger, obj, now)
        elif event_type == "checkout.session.async_payment_failed":
            result = _async_failed(conn, obj)
        elif event_type == "charge.refunded":
            result = _refunded(conn, ledger, obj, now)
        elif event_type == "charge.dispute.created":
            result = _dispute_created(conn, ledger, obj, now)
        elif event_type == "charge.dispute.closed":
            result = _dispute_closed(conn, ledger, obj, now)
        else:
            result = EventResult("ignored")
        conn.execute(
            "INSERT INTO stripe_events (event_id, event_type, outcome, processed_at) VALUES (?,?,?,?)",
            (event_id, event_type, result.outcome, _now(now)),
        )
        conn.execute("COMMIT")
        return result
    except Exception:
        conn.execute("ROLLBACK")
        raise
