import json

from access_ledger import apply_event, run_reconciliation
from tests.test_stripe_events import charge_event, session_event


class Pages:
    def __init__(self, pages):
        self.pages = pages
        self.calls = []

    def __call__(self, method, url, headers, body):
        self.calls.append(url)
        index = len(self.calls) - 1
        return 200, self.pages[index]


def charge(intent="pi_1", amount=1000, refunded=0, status="succeeded", dispute=None, cid="ch_1"):
    return {"id": cid, "payment_intent": intent, "amount": amount, "amount_refunded": refunded, "status": status, "dispute": dispute}


def test_a_clean_ledger_reconciles_with_no_findings(conn, catalogue):
    apply_event(conn, session_event(), catalogue)
    transport = Pages([{"data": [charge()], "has_more": False}])
    assert run_reconciliation(conn, "sk_test_x", transport) == []


def test_charges_are_read_across_pages(conn, catalogue):
    apply_event(conn, session_event(), catalogue)
    apply_event(conn, session_event(event_id="evt_2", session_id="cs_2", intent="pi_2"), catalogue)
    transport = Pages([
        {"data": [charge(cid="ch_1")], "has_more": True},
        {"data": [charge(intent="pi_2", cid="ch_2")], "has_more": False},
    ])
    assert run_reconciliation(conn, "sk_test_x", transport) == []
    assert "starting_after=ch_1" in transport.calls[1]


def test_a_charge_with_no_purchase_is_reported_as_an_orphan(conn):
    transport = Pages([{"data": [charge()], "has_more": False}])
    assert [f.code for f in run_reconciliation(conn, "sk_test_x", transport)] == ["ORPHAN_PAYMENT"]


def test_a_recent_purchase_with_no_charge_is_reported_as_unbacked(conn, catalogue):
    apply_event(conn, session_event(), catalogue)
    transport = Pages([{"data": [], "has_more": False}])
    assert [f.code for f in run_reconciliation(conn, "sk_test_x", transport)] == ["UNBACKED_GRANT"]


def test_an_unprocessed_refund_in_stripe_is_reported(conn, catalogue):
    apply_event(conn, session_event(), catalogue)
    transport = Pages([{"data": [charge(refunded=1000)], "has_more": False}])
    assert [f.code for f in run_reconciliation(conn, "sk_test_x", transport)] == ["REFUND_MISMATCH"]


def test_a_processed_refund_and_dispute_reconcile(conn, catalogue):
    apply_event(conn, session_event(), catalogue)
    apply_event(conn, charge_event("charge.dispute.created", "evt_2"), catalogue)
    transport = Pages([{"data": [charge(dispute={"status": "needs_response"})], "has_more": False}])
    assert run_reconciliation(conn, "sk_test_x", transport) == []
