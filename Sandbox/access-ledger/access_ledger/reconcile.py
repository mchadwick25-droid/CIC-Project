"""Compares Stripe charges with the ledger and checks ledger invariants.

Stripe charges are passed in as plain dicts, so the check runs without a
network call. Each charge carries: payment_intent, amount, amount_refunded,
status, and dispute_status (None, 'open', 'lost' or 'won').
"""
import sqlite3
from dataclasses import dataclass


@dataclass(frozen=True)
class Finding:
    code: str
    ref: str
    detail: str


def _purchase_rows(conn: sqlite3.Connection) -> dict[str, tuple]:
    rows = conn.execute("SELECT payment_intent, purchase_id, units, amount_cents, status FROM purchases").fetchall()
    return {r[0]: r for r in rows if r[0]}


def _net_reversed(conn: sqlite3.Connection, purchase_id: str) -> int:
    return -int(
        conn.execute(
            "SELECT COALESCE(SUM(delta), 0) FROM access_ledger WHERE purchase_id = ? AND kind IN ('reverse','adjust')", (purchase_id,),
        ).fetchone()[0]
    )


def _stripe_findings(conn: sqlite3.Connection, charges: list[dict], charges_complete: bool) -> list[Finding]:
    findings: list[Finding] = []
    purchases = _purchase_rows(conn)
    seen: set[str] = set()
    for charge in charges:
        intent = charge["payment_intent"]
        seen.add(intent)
        if charge.get("status") != "succeeded":
            continue
        purchase = purchases.get(intent)
        if purchase is None or purchase[4] != "granted":
            findings.append(Finding("ORPHAN_PAYMENT", intent, "succeeded charge with no granted purchase"))
            continue
        _intent, purchase_id, units, amount_cents, _status = purchase
        if charge["amount"] != amount_cents:
            findings.append(Finding("AMOUNT_MISMATCH", intent, f"charge {charge['amount']} vs purchase {amount_cents}"))
        refund_units = min(units, units * (charge.get("amount_refunded") or 0) // charge["amount"]) if charge["amount"] else 0
        expected = units if charge.get("dispute_status") in ("open", "lost") else refund_units
        actual = _net_reversed(conn, purchase_id)
        if actual != expected:
            findings.append(Finding("REFUND_MISMATCH", intent, f"expected {expected} units reversed, ledger shows {actual}"))
    if charges_complete:
        for intent, (_i, purchase_id, _u, _a, status) in purchases.items():
            if status == "granted" and intent not in seen:
                findings.append(Finding("UNBACKED_GRANT", intent, f"purchase {purchase_id} has no charge in the Stripe data"))
    return findings


def _ledger_findings(conn: sqlite3.Connection) -> list[Finding]:
    findings: list[Finding] = []
    for purchase_id, count in conn.execute(
        "SELECT purchase_id, COUNT(*) FROM access_ledger WHERE kind = 'grant_paid' GROUP BY purchase_id HAVING COUNT(*) > 1",
    ):
        findings.append(Finding("DUPLICATE_GRANT", purchase_id, f"{count} paid grants"))
    for (session_id,) in conn.execute(
        "SELECT s.session_id FROM access_ledger s WHERE s.kind IN ('capture','release')"
        " AND NOT EXISTS (SELECT 1 FROM access_ledger h WHERE h.session_id = s.session_id AND h.kind = 'hold')",
    ):
        findings.append(Finding("SETTLEMENT_WITHOUT_HOLD", session_id, "capture or release with no hold"))
    for (session_id,) in conn.execute(
        "SELECT session_id FROM access_ledger WHERE kind IN ('capture','release') GROUP BY session_id"
        " HAVING COUNT(DISTINCT kind) > 1",
    ):
        findings.append(Finding("CAPTURED_AND_RELEASED", session_id, "hold both captured and released"))
    for (purchase_id,) in conn.execute(
        "SELECT p.purchase_id FROM purchases p WHERE p.status = 'granted'"
        " AND NOT EXISTS (SELECT 1 FROM access_ledger g WHERE g.purchase_id = p.purchase_id AND g.kind = 'grant_paid')",
    ):
        findings.append(Finding("GRANT_MISSING", purchase_id, "granted purchase has no ledger grant"))
    return findings


def reconcile(conn: sqlite3.Connection, charges: list[dict], charges_complete: bool = True) -> list[Finding]:
    """Returns every discrepancy found; an empty list means the ledger agrees
    with the Stripe data and its own invariants."""
    return _stripe_findings(conn, charges, charges_complete) + _ledger_findings(conn)
