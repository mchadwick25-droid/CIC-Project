from access_ledger import Ledger, apply_event, reconcile
from tests.test_stripe_events import charge_event, session_event


def charge(intent="pi_1", amount=1000, refunded=0, status="succeeded", dispute=None):
    return {"payment_intent": intent, "amount": amount, "amount_refunded": refunded, "status": status, "dispute_status": dispute}


def codes(findings):
    return sorted(f.code for f in findings)


def test_a_matching_ledger_and_charge_list_has_no_findings(conn, catalogue):
    apply_event(conn, session_event(), catalogue)
    assert reconcile(conn, [charge()]) == []


def test_a_succeeded_charge_with_no_purchase_is_an_orphan(conn):
    assert codes(reconcile(conn, [charge()])) == ["ORPHAN_PAYMENT"]


def test_a_failed_charge_is_not_an_orphan(conn):
    assert reconcile(conn, [charge(status="failed")]) == []


def test_a_granted_purchase_with_no_charge_is_unbacked_only_when_the_list_is_complete(conn, catalogue):
    apply_event(conn, session_event(), catalogue)
    assert codes(reconcile(conn, [])) == ["UNBACKED_GRANT"]
    assert reconcile(conn, [], charges_complete=False) == []


def test_charge_amount_that_differs_from_the_purchase_is_flagged(conn, catalogue):
    apply_event(conn, session_event(), catalogue)
    assert "AMOUNT_MISMATCH" in codes(reconcile(conn, [charge(amount=1200)]))


def test_a_refund_in_stripe_that_the_ledger_missed_is_flagged(conn, catalogue):
    apply_event(conn, session_event(), catalogue)
    assert codes(reconcile(conn, [charge(refunded=1000)])) == ["REFUND_MISMATCH"]


def test_a_processed_refund_reconciles(conn, catalogue):
    apply_event(conn, session_event(), catalogue)
    apply_event(conn, charge_event("charge.refunded", "evt_2", refunded=500), catalogue)
    assert reconcile(conn, [charge(refunded=500)]) == []


def test_open_dispute_expects_full_reversal_and_a_won_dispute_expects_none(conn, catalogue):
    apply_event(conn, session_event(), catalogue)
    apply_event(conn, charge_event("charge.dispute.created", "evt_2"), catalogue)
    assert reconcile(conn, [charge(dispute="open")]) == []
    assert codes(reconcile(conn, [charge(dispute="won")])) == ["REFUND_MISMATCH"]
    apply_event(conn, charge_event("charge.dispute.closed", "evt_3", status="won"), catalogue)
    assert reconcile(conn, [charge(dispute="won")]) == []


def test_ledger_invariants_catch_settlement_without_a_hold(conn):
    conn.execute(
        "INSERT INTO access_ledger (visitor_id, kind, bucket, delta, session_id, source_ref, created_at)"
        " VALUES ('v1','capture','paid',0,'ghost','capture:ghost','2026-10-01T00:00:00+00:00')",
    )
    assert codes(reconcile(conn, [])) == ["SETTLEMENT_WITHOUT_HOLD"]


def test_ledger_invariants_catch_a_hold_both_captured_and_released(conn):
    ledger = Ledger(conn)
    ledger.grant_paid("v1", 1, "cs_1")
    ledger.hold("v1", "s1")
    conn.execute(
        "INSERT INTO access_ledger (visitor_id, kind, bucket, delta, session_id, source_ref, created_at)"
        " VALUES ('v1','capture','paid',0,'s1','capture:s1','2026-10-01T00:00:00+00:00')",
    )
    conn.execute(
        "INSERT INTO access_ledger (visitor_id, kind, bucket, delta, session_id, source_ref, created_at)"
        " VALUES ('v1','release','paid',1,'s1','release:s1','2026-10-01T00:00:00+00:00')",
    )
    assert "CAPTURED_AND_RELEASED" in codes(reconcile(conn, [], charges_complete=False))


def test_a_granted_purchase_without_a_grant_row_is_flagged(conn):
    conn.execute(
        "INSERT INTO purchases (purchase_id, payment_intent, visitor_id, sku, units, amount_cents, currency, status, created_at)"
        " VALUES ('cs_1','pi_1','v1','pack_small',4,1000,'usd','granted','2026-10-01T00:00:00+00:00')",
    )
    assert codes(reconcile(conn, [charge()])) == ["GRANT_MISSING"]
