"""The operator's coupon button, and a coupon reaching a person at sign-in."""
import dataclasses
import logging
from datetime import date

import pytest
from fastapi.testclient import TestClient

from engine.accounts.keys import KeyRing
from engine.accounts.service import AccountsService
from engine.accounts.store import AccountStore
from engine.accounts.tests.conftest import ADDRESS_KEY, SESSION_KEY, Clock, FakeMailer
from engine.api.accounts_routes import AccountsRuntime
from engine.api.app import create_app
from engine.api.deeper_ops import load_ops
from engine.api.deeper_routes import DeeperRuntime
from engine.deeper.claims import ClaimStore
from engine.deeper.meter import Meter

H = {"x-cic-accounts": "1"}
ADMIN = "a" * 40
ADDR = "ada@example.org"
AUTH = {"Authorization": f"Bearer {ADMIN}"}


@pytest.fixture
def runtime(tmp_path):
    rt = DeeperRuntime(
        meter=Meter(str(tmp_path / "m.db"), clock=lambda: date(2026, 10, 24)),
        claims=ClaimStore(str(tmp_path / "c.db")),
        webhook_secret="whsec_x", products={}, miss_delay_seconds=0.0, ops=load_ops(),
    )
    yield rt
    rt.meter.close()
    rt.claims.close()


@pytest.fixture
def mailer():
    return FakeMailer()


@pytest.fixture
def accounts(tmp_path, mailer):
    store = AccountStore(str(tmp_path / "d.db"), str(tmp_path / "e.db"))
    service = AccountsService(store, KeyRing(ADDRESS_KEY, SESSION_KEY), mailer, clock=Clock())
    yield AccountsRuntime(service=service, miss_delay_seconds=0.0, start_floor_seconds=0.0)
    store.close()


def build(store, usage_store, world_loader, registry, *, deeper, accounts):
    return TestClient(
        create_app(
            voice_client=object(), voice_model_id="m", safety_client=object(), safety_model_id="m",
            store=store, usage_store=usage_store, world_loader=world_loader, registry=registry,
            default_world_key="fix", admin_token=ADMIN, deeper=deeper, accounts=accounts, rate_limit=False,
            anon_cap_enabled=True, anon_visitor_secret="s" * 32,
        ),
        base_url="https://testserver",
    )


@pytest.fixture
def http(store, usage_store, world_loader, registry, runtime, accounts):
    return build(store, usage_store, world_loader, registry, deeper=runtime, accounts=accounts)


def sign_in(http, mailer, address=ADDR):
    started = http.post("/api/accounts/sign-in/start", json={"address": address}, headers=H)
    done = http.post(
        "/api/accounts/sign-in/finish",
        json={"challenge": started.json()["challenge"], "address": address, "code": mailer.last_code(address), "over_18": True},
        headers=H,
    )
    assert done.status_code == 200 and done.json()["status"] == "ok", done.text
    return done.json()


def approve(http, address=ADDR, tokens=3000):
    return http.post("/api/admin/deeper/coupon", json={"address": address, "tokens": tokens}, headers=AUTH)


def test_the_routes_need_both_modules_and_the_operator(store, usage_store, world_loader, registry, runtime, accounts, http):
    for only in (build(store, usage_store, world_loader, registry, deeper=runtime, accounts=None),):
        assert only.post("/api/admin/deeper/coupon", json={"address": ADDR, "tokens": 5}, headers=AUTH).status_code == 404
        assert only.get("/api/admin/deeper/coupons", headers=AUTH).status_code == 404
    # Without the operator's credential the answer is the same 404 as for a route that does not exist.
    wrong = {"Authorization": "Bearer " + "b" * 40}
    assert http.post("/api/admin/deeper/coupon", json={"address": ADDR, "tokens": 5}).status_code == 404
    assert http.post("/api/admin/deeper/coupon", json={"address": ADDR, "tokens": 5}, headers=wrong).status_code == 404
    assert http.get("/api/admin/deeper/coupons").status_code == 404
    assert http.post("/api/admin/deeper/coupon/cancel", json={"coupon_id": "coupon_x"}).status_code == 404
    assert http.get("/api/admin/deeper/coupons", headers=wrong).status_code == 404
    assert http.get("/api/admin/deeper/coupons").json() != http.get("/api/admin/deeper/coupons", headers=AUTH).json()
    assert approve(http).status_code == 200


def test_approving_answers_with_an_id_an_amount_and_a_day_and_never_the_address(http):
    r = approve(http, "  Ada@Example.org ", 3000)
    assert r.status_code == 200 and set(r.json()) == {"coupon_id", "tokens", "day_made"}
    assert r.json()["tokens"] == 3000 and r.headers["cache-control"] == "no-store"
    assert "ada@" not in r.text.lower() and "example" not in r.text.lower()
    listed = http.get("/api/admin/deeper/coupons", headers=AUTH)
    assert listed.status_code == 200 and listed.json()["coupons"] == [r.json()]
    assert "ada@" not in listed.text.lower() and "example" not in listed.text.lower()


def test_the_list_carries_the_limits_from_the_operations_file(http, runtime):
    body = http.get("/api/admin/deeper/coupons", headers=AUTH).json()
    assert (body["max_tokens"], body["per_day"], body["unclaimed_days"]) == (
        runtime.ops.coupon_max_tokens, runtime.ops.coupon_max_per_day, runtime.ops.coupon_unclaimed_days,
    )


@pytest.mark.parametrize("payload", [
    {"address": "not-an-address", "tokens": 100}, {"address": ADDR, "tokens": 0}, {"address": ADDR, "tokens": 20001},
    {"address": ADDR, "tokens": "100"}, {"address": ADDR, "tokens": True}, {"address": ADDR},
])
def test_a_bad_request_keeps_nothing(http, payload):
    assert http.post("/api/admin/deeper/coupon", json=payload, headers=AUTH).status_code == 422
    assert http.get("/api/admin/deeper/coupons", headers=AUTH).json()["coupons"] == []


def test_the_day_s_limit_stops_the_next_coupon(http, runtime):
    runtime.ops = dataclasses.replace(runtime.ops, coupon_max_per_day=2)
    assert approve(http, "a@example.org").status_code == 200
    assert approve(http, "b@example.org").status_code == 200
    stopped = approve(http, "c@example.org")
    assert stopped.status_code == 429 and "limit" in stopped.json()["detail"]
    assert len(http.get("/api/admin/deeper/coupons", headers=AUTH).json()["coupons"]) == 2


def test_cancelling_a_waiting_coupon_stops_it_attaching(http, mailer):
    made = approve(http).json()
    assert http.post("/api/admin/deeper/coupon/cancel", json={"coupon_id": made["coupon_id"]}, headers=AUTH).json() == {
        "coupon_id": made["coupon_id"], "cancelled": True,
    }
    assert http.post("/api/admin/deeper/coupon/cancel", json={"coupon_id": made["coupon_id"]}, headers=AUTH).status_code == 404
    assert sign_in(http, mailer)["coupons"] == []


def test_a_coupon_attaches_at_sign_in_and_shows_on_the_account(http, mailer, runtime):
    approve(http, tokens=3000)
    done = sign_in(http, mailer)
    assert done["coupons"] == [3000]
    balance = http.get("/api/accounts/balance").json()
    assert balance["codes_held"] == 1 and balance["code_tokens"] == 3000 and balance["gifts"] == [3000]
    assert runtime.meter.reconciliation(1)[0]["coupon_codes_minted"] == 1
    assert http.get("/api/admin/deeper/coupons", headers=AUTH).json()["coupons"] == []
    http.post("/api/accounts/sign-out", headers=H)
    assert sign_in(http, mailer)["coupons"] == []
    assert http.get("/api/accounts/balance").json()["gifts"] == [3000]


def attached_grant_id(http, made):
    ids = [g["grant_id"] for g in http.get("/api/admin/deeper/grants", headers=AUTH).json()["grants"] if g["grant_id"].startswith("coupon_")]
    assert len(ids) == 1 and ids[0] != made["coupon_id"]
    return ids[0]


def test_an_attached_coupon_is_cancelled_with_its_codes_and_leaves_the_account(http, mailer, runtime):
    made = approve(http).json()
    sign_in(http, mailer)
    voided = http.post("/api/admin/deeper/void", json={"payment_id": attached_grant_id(http, made)}, headers=AUTH)
    assert voided.status_code == 200 and voided.json()["voided"] == 1
    balance = http.get("/api/accounts/balance").json()
    assert balance["code_tokens"] == 0 and balance["gifts"] == []


def test_the_grants_list_shows_an_attached_coupon_by_its_id(http, mailer):
    made = approve(http).json()
    sign_in(http, mailer)
    assert attached_grant_id(http, made).startswith("coupon_")


def test_the_address_reaches_no_log_while_it_is_approved_and_used(http, mailer, caplog):
    caplog.set_level(logging.DEBUG)
    approve(http, "private.person@example.org")
    sign_in(http, mailer, "private.person@example.org")
    assert "private.person" not in caplog.text


def _dashboard_cookie(http):
    from engine.api import admin_auth

    http.cookies.set(admin_auth.SESSION_COOKIE_NAME, admin_auth.issue_session_token(ADMIN))


def test_a_change_made_with_the_dashboard_cookie_must_come_from_our_own_page(http, accounts, mailer):
    _dashboard_cookie(http)
    body = {"address": ADDR, "tokens": 5}
    assert http.post("/api/admin/deeper/coupon", json=body).status_code == 400
    assert http.post("/api/admin/deeper/coupon", json=body, headers={"x-cic-accounts": "1", "Origin": "https://elsewhere.example"}).status_code == 403
    assert http.get("/api/admin/deeper/coupons").json()["coupons"] == []
    ours = {"x-cic-accounts": "1", "Origin": "https://testserver"}
    made = http.post("/api/admin/deeper/coupon", json=body, headers=ours)
    assert made.status_code == 200
    cancel = {"coupon_id": made.json()["coupon_id"]}
    assert http.post("/api/admin/deeper/coupon/cancel", json=cancel).status_code == 400
    assert http.post("/api/admin/deeper/coupon/cancel", json=cancel, headers=ours).status_code == 200


DASHBOARD_CHANGES = [
    ("/api/admin/deeper/pause", {"on": True}),
    ("/api/admin/deeper/mint", {"pack_usd": 5, "count": 1, "mode": "one_code"}),
    ("/api/admin/deeper/tester", {}),
    ("/api/admin/deeper/void", {"payment_id": "p1"}),
    ("/api/admin/deeper/funds", {"cents": 100, "note": "correction"}),
    ("/api/admin/deeper/funds/e1/reverse", None),
    ("/api/admin/deeper/unmatched/dismiss", {"payment_id": "p1"}),
]


@pytest.mark.parametrize("path,body", DASHBOARD_CHANGES)
def test_every_dashboard_change_made_with_the_cookie_must_come_from_our_own_page(http, path, body):
    _dashboard_cookie(http)
    assert http.post(path, json=body).status_code == 400
    assert http.post(path, json=body, headers={"x-cic-accounts": "1", "Origin": "https://elsewhere.example"}).status_code == 403
    guarded = http.post(path, json=body, headers={"x-cic-accounts": "1", "Origin": "https://testserver"})
    assert guarded.status_code not in (400, 403)
