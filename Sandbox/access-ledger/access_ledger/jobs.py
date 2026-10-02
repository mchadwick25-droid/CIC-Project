"""Scheduled jobs: daily reconciliation of Stripe charges against the ledger."""
import argparse
import json
import os
import sqlite3
import sys
import time
import urllib.error
import urllib.request
from dataclasses import asdict

from .checkout import Transport
from .reconcile import Finding, reconcile
from .store import connect, init_schema
from .stripe_data import list_charges, to_reconcile_charge

DAY_SECONDS = 86400


def run_reconciliation(conn: sqlite3.Connection, secret_key: str, transport: Transport, lookback_days: int = 35, now: float | None = None) -> list[Finding]:
    """Reconciles charges created in the lookback window. Purchases older than
    the window are not checked for a missing charge, so UNBACKED_GRANT is
    reported only for charges the window can see."""
    since = int((now if now is not None else time.time()) - lookback_days * DAY_SECONDS)
    charges = [to_reconcile_charge(c) for c in list_charges(secret_key, transport, since)]
    window_intents = {c["payment_intent"] for c in charges}
    findings = reconcile(conn, charges, charges_complete=False)
    unbacked = [
        Finding("UNBACKED_GRANT", intent, f"purchase {purchase_id} created in the window has no charge in the Stripe data")
        for intent, purchase_id in conn.execute(
            "SELECT payment_intent, purchase_id FROM purchases WHERE status = 'granted' AND created_at >= ?",
            (time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime(since)),),
        )
        if intent and intent not in window_intents
    ]
    return findings + unbacked


def urllib_transport(method: str, url: str, headers: dict[str, str], body: str) -> tuple[int, dict]:
    request = urllib.request.Request(url, data=body.encode() if body else None, headers=headers, method=method)
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return response.status, json.loads(response.read() or b"{}")
    except urllib.error.HTTPError as exc:
        return exc.code, json.loads(exc.read() or b"{}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Reconcile Stripe charges against the access ledger")
    parser.add_argument("--db", required=True)
    parser.add_argument("--lookback-days", type=int, default=35)
    args = parser.parse_args(argv)
    conn = connect(args.db)
    init_schema(conn)
    findings = run_reconciliation(conn, os.environ["STRIPE_SECRET_KEY"], urllib_transport, args.lookback_days)
    print(json.dumps([asdict(f) for f in findings], indent=2))
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
