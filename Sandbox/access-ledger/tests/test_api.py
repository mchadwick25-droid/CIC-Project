import hashlib
import hmac
import json
import time

import pytest
from fastapi.testclient import TestClient

from access_ledger.api import create_app
from tests.test_checkout import FakeTransport
from tests.test_stripe_events import session_event

TOKEN = "internal-secret"
WEBHOOK_SECRET = "whsec_test"
H = {"X-Access-Token": TOKEN}


@pytest.fixture
def client(tmp_path, catalogue):
    app = create_app(
        tmp_path / "api.db", catalogue, {"pack_small": "5 conversations", "pack_large": "13 conversations"}, TOKEN, "sk_test_x",
        WEBHOOK_SECRET, FakeTransport(), "https://x/ok", "https://x/cancel",
    )
    return TestClient(app)


def signed(payload: dict) -> tuple[bytes, dict]:
    body = json.dumps(payload).encode()
    ts = int(time.time())
    digest = hmac.new(WEBHOOK_SECRET.encode(), f"{ts}.".encode() + body, hashlib.sha256).hexdigest()
    return body, {"Stripe-Signature": f"t={ts},v1={digest}", "Content-Type": "application/json"}


def test_internal_endpoints_refuse_a_missing_or_wrong_token(client):
    assert client.post("/access/start", json={"visitor_id": "v1", "session_id": "s1"}).status_code == 401
    assert client.post("/access/start", json={"visitor_id": "v1", "session_id": "s1"}, headers={"X-Access-Token": "bad"}).status_code == 401
    assert client.get("/access/balance", params={"visitor_id": "v1"}).status_code == 401


def test_packs_are_listed_without_a_token(client):
    packs = client.get("/access/packs").json()
    assert {p["sku"] for p in packs} == {"pack_small", "pack_large"}


def test_start_then_first_reply_spends_a_free_unit(client):
    started = client.post("/access/start", json={"visitor_id": "v1", "session_id": "s1"}, headers=H).json()
    assert started["admitted"] and started["bucket"] == "free" and started["turn_cap"] == 3
    assert client.post("/access/first-reply", json={"session_id": "s1"}, headers=H).json() == {"captured": True}
    assert client.get("/access/balance", params={"visitor_id": "v1"}, headers=H).json()["free"] == 2


def test_failed_conversation_gives_the_unit_back(client):
    client.post("/access/start", json={"visitor_id": "v1", "session_id": "s1"}, headers=H)
    assert client.post("/access/failed", json={"session_id": "s1"}, headers=H).json() == {"released": True}
    assert client.get("/access/balance", params={"visitor_id": "v1"}, headers=H).json()["free"] == 3


def test_settling_an_unknown_session_is_a_conflict(client):
    assert client.post("/access/first-reply", json={"session_id": "ghost"}, headers=H).status_code == 409


def test_checkout_returns_the_hosted_url_and_refuses_unknown_packs(client):
    ok = client.post("/access/checkout", json={"visitor_id": "v1", "sku": "pack_small"}, headers=H)
    assert ok.status_code == 200 and ok.json()["url"].startswith("https://checkout.stripe.com/")
    assert client.post("/access/checkout", json={"visitor_id": "v1", "sku": "nope"}, headers=H).status_code == 400


def test_webhook_rejects_a_bad_signature_and_grants_nothing(client):
    body = json.dumps(session_event()).encode()
    response = client.post("/access/stripe-webhook", content=body, headers={"Stripe-Signature": "t=1,v1=00"})
    assert response.status_code == 400
    assert client.get("/access/balance", params={"visitor_id": "v1"}, headers=H).json()["paid"] == 0


def test_webhook_grants_once_and_replays_are_duplicates(client):
    body, headers = signed(session_event())
    assert client.post("/access/stripe-webhook", content=body, headers=headers).json() == {"outcome": "granted"}
    body2, headers2 = signed(session_event())
    assert client.post("/access/stripe-webhook", content=body2, headers=headers2).json() == {"outcome": "duplicate"}
    assert client.get("/access/balance", params={"visitor_id": "v1"}, headers=H).json()["paid"] == 4


def test_a_purchase_lets_a_visitor_with_no_free_units_start_a_paid_conversation(client):
    for i in range(3):
        client.post("/access/start", json={"visitor_id": "v1", "session_id": f"f{i}"}, headers=H)
        client.post("/access/first-reply", json={"session_id": f"f{i}"}, headers=H)
    refused = client.post("/access/start", json={"visitor_id": "v1", "session_id": "x"}, headers=H).json()
    assert refused["admitted"] is False and refused["reason"] == "no_balance"
    body, headers = signed(session_event())
    client.post("/access/stripe-webhook", content=body, headers=headers)
    paid = client.post("/access/start", json={"visitor_id": "v1", "session_id": "p1"}, headers=H).json()
    assert paid["admitted"] and paid["bucket"] == "paid" and paid["turn_cap"] == 7
