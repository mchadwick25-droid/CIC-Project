import hashlib
import hmac
import time

from access_ledger import Ledger, apply_event, verify_signature


def sign(payload: bytes, secret: str, timestamp: int) -> str:
    digest = hmac.new(secret.encode(), f"{timestamp}.".encode() + payload, hashlib.sha256).hexdigest()
    return f"t={timestamp},v1={digest}"


def session_event(event_id="evt_1", session_id="cs_1", visitor="v1", sku="pack_small", amount=1000, status="paid", intent="pi_1"):
    return {
        "id": event_id,
        "type": "checkout.session.completed",
        "data": {"object": {
            "id": session_id, "client_reference_id": visitor, "metadata": {"sku": sku}, "amount_total": amount,
            "currency": "usd", "payment_status": status, "payment_intent": intent,
        }},
    }


def charge_event(event_type, event_id, intent="pi_1", amount=1000, refunded=0, charge_id="ch_1", status=None):
    obj = {"id": charge_id if "dispute" not in event_type else "dp_1", "payment_intent": intent, "amount": amount, "amount_refunded": refunded}
    if status:
        obj["status"] = status
    return {"id": event_id, "type": event_type, "data": {"object": obj}}


def test_signature_accepts_a_correct_header():
    payload = b'{"id":"evt_1"}'
    now = int(time.time())
    assert verify_signature(payload, sign(payload, "whsec_x", now), "whsec_x", now=now)


def test_signature_rejects_wrong_secret_altered_payload_and_old_timestamp():
    payload = b'{"id":"evt_1"}'
    now = int(time.time())
    header = sign(payload, "whsec_x", now)
    assert not verify_signature(payload, header, "whsec_other", now=now)
    assert not verify_signature(payload + b" ", header, "whsec_x", now=now)
    assert not verify_signature(payload, sign(payload, "whsec_x", now - 3600), "whsec_x", now=now)
    assert not verify_signature(payload, "garbage", "whsec_x", now=now)
    assert not verify_signature(payload, "t=abc,v1=00", "whsec_x", now=now)


def test_signature_accepts_any_of_several_v1_values():
    payload = b"{}"
    now = int(time.time())
    good = sign(payload, "whsec_x", now).split("v1=")[1]
    assert verify_signature(payload, f"t={now},v1=deadbeef,v1={good}", "whsec_x", now=now)


def test_paid_checkout_grants_units(conn, catalogue):
    result = apply_event(conn, session_event(), catalogue)
    assert result.outcome == "granted"
    assert Ledger(conn).balance("v1", "paid") == 4


def test_a_repeated_event_id_changes_nothing(conn, catalogue):
    apply_event(conn, session_event(), catalogue)
    assert apply_event(conn, session_event(), catalogue).outcome == "duplicate"
    assert Ledger(conn).balance("v1") == 4


def test_a_new_event_for_the_same_session_does_not_grant_twice(conn, catalogue):
    apply_event(conn, session_event(event_id="evt_1"), catalogue)
    assert apply_event(conn, session_event(event_id="evt_2"), catalogue).outcome == "already_recorded"
    assert Ledger(conn).balance("v1") == 4


def test_amount_that_differs_from_the_catalogue_grants_nothing(conn, catalogue):
    result = apply_event(conn, session_event(amount=100), catalogue)
    assert result.outcome == "amount_mismatch"
    assert Ledger(conn).balance("v1") == 0
    assert conn.execute("SELECT status FROM purchases WHERE purchase_id = 'cs_1'").fetchone()[0] == "amount_mismatch"


def test_unknown_sku_and_missing_fields_grant_nothing(conn, catalogue):
    assert apply_event(conn, session_event(sku="nope"), catalogue).outcome == "unknown_sku"
    bad = session_event(event_id="evt_9")
    bad["data"]["object"]["client_reference_id"] = None
    assert apply_event(conn, bad, catalogue).outcome == "invalid"
    assert Ledger(conn).balance("v1") == 0


def test_unpaid_checkout_waits_for_async_success(conn, catalogue):
    assert apply_event(conn, session_event(status="unpaid"), catalogue).outcome == "pending"
    assert Ledger(conn).balance("v1") == 0
    done = {"id": "evt_2", "type": "checkout.session.async_payment_succeeded", "data": {"object": {"id": "cs_1"}}}
    assert apply_event(conn, done, catalogue).outcome == "granted"
    assert Ledger(conn).balance("v1") == 4


def test_async_failure_marks_the_purchase_failed(conn, catalogue):
    apply_event(conn, session_event(status="unpaid"), catalogue)
    failed = {"id": "evt_2", "type": "checkout.session.async_payment_failed", "data": {"object": {"id": "cs_1"}}}
    assert apply_event(conn, failed, catalogue).outcome == "failed"
    assert Ledger(conn).balance("v1") == 0


def test_full_refund_reverses_all_units(conn, catalogue):
    apply_event(conn, session_event(), catalogue)
    assert apply_event(conn, charge_event("charge.refunded", "evt_2", refunded=1000), catalogue).outcome == "reversed"
    assert Ledger(conn).balance("v1") == 0


def test_partial_refund_reverses_proportionally_and_later_refund_tops_up(conn, catalogue):
    apply_event(conn, session_event(), catalogue)
    apply_event(conn, charge_event("charge.refunded", "evt_2", refunded=500), catalogue)
    assert Ledger(conn).balance("v1") == 2
    apply_event(conn, charge_event("charge.refunded", "evt_3", refunded=1000), catalogue)
    assert Ledger(conn).balance("v1") == 0


def test_a_repeated_refund_amount_reverses_nothing_more(conn, catalogue):
    apply_event(conn, session_event(), catalogue)
    apply_event(conn, charge_event("charge.refunded", "evt_2", refunded=500), catalogue)
    assert apply_event(conn, charge_event("charge.refunded", "evt_3", refunded=500), catalogue).outcome == "already_recorded"
    assert Ledger(conn).balance("v1") == 2


def test_spent_units_can_leave_a_negative_balance_after_a_refund(conn, catalogue):
    apply_event(conn, session_event(), catalogue)
    ledger = Ledger(conn)
    for i in range(3):
        ledger.hold("v1", f"s{i}")
        ledger.capture(f"s{i}")
    apply_event(conn, charge_event("charge.refunded", "evt_2", refunded=1000), catalogue)
    assert ledger.balance("v1") == -3
    assert ledger.hold("v1", "s9").admitted is False


def test_dispute_reverses_the_unrefunded_units_and_a_win_restores_them(conn, catalogue):
    apply_event(conn, session_event(), catalogue)
    apply_event(conn, charge_event("charge.refunded", "evt_2", refunded=500), catalogue)
    apply_event(conn, charge_event("charge.dispute.created", "evt_3"), catalogue)
    assert Ledger(conn).balance("v1") == 0
    won = charge_event("charge.dispute.closed", "evt_4", status="won")
    assert apply_event(conn, won, catalogue).outcome == "restored"
    assert Ledger(conn).balance("v1") == 2


def test_a_lost_dispute_keeps_units_reversed(conn, catalogue):
    apply_event(conn, session_event(), catalogue)
    apply_event(conn, charge_event("charge.dispute.created", "evt_2"), catalogue)
    lost = charge_event("charge.dispute.closed", "evt_3", status="lost")
    assert apply_event(conn, lost, catalogue).outcome == "no_change"
    assert Ledger(conn).balance("v1") == 0


def test_refund_for_an_unknown_charge_is_recorded_and_ignored(conn, catalogue):
    assert apply_event(conn, charge_event("charge.refunded", "evt_1", intent="pi_missing", refunded=1000), catalogue).outcome == "unknown_purchase"


def test_unhandled_event_types_are_recorded_once(conn, catalogue):
    event = {"id": "evt_1", "type": "customer.created", "data": {"object": {}}}
    assert apply_event(conn, event, catalogue).outcome == "ignored"
    assert apply_event(conn, event, catalogue).outcome == "duplicate"


def test_a_failure_inside_an_event_leaves_no_partial_state(conn, catalogue, monkeypatch):
    def boom(*args, **kwargs):
        raise RuntimeError("disk full")

    monkeypatch.setattr(Ledger, "grant_paid", boom)
    try:
        apply_event(conn, session_event(), catalogue)
    except RuntimeError:
        pass
    assert conn.execute("SELECT COUNT(*) FROM purchases").fetchone()[0] == 0
    assert conn.execute("SELECT COUNT(*) FROM stripe_events").fetchone()[0] == 0
