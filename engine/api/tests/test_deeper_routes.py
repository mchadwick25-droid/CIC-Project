"""Go Deeper's HTTP edge: the signed webhook, claim, balance, pause and
reconciliation routes, and the proof that with the flag off none of them exist."""
import hashlib
import hmac
import json
import logging
import re
import time
from datetime import date

import pytest
from fastapi.testclient import TestClient

from engine.api import deeper_routes
from engine.api.app import create_app
from engine.api.deeper_routes import DeeperConfigError, DeeperRuntime, Product, parse_products, verify_signature
from engine.deeper import codes
from engine.deeper.claims import ClaimStore
from engine.deeper.config import DeeperConfig
from engine.deeper.meter import Meter

SECRET = "whsec_test_secret"
REF = "browser-made-reference-0001"
LINK_SINGLE = "plink_single"
LINK_SPONSOR = "plink_sponsor"
LINK_GIFT = "plink_gift"
ADMIN = "a" * 40


def sign(body: bytes, *, secret: str = SECRET, stamp: int | None = None) -> str:
    stamp = int(time.time()) if stamp is None else stamp
    digest = hmac.new(secret.encode(), f"{stamp}.".encode() + body, hashlib.sha256).hexdigest()
    return f"t={stamp},v1={digest}"


def completed(*, payment="pi_100", link=LINK_SINGLE, reference=REF, paid="paid", kind="checkout.session.completed", amount=700, currency="usd"):
    return {
        "id": "evt_1",
        "type": kind,
        "data": {"object": {"id": "cs_1", "payment_link": link, "payment_status": paid, "payment_intent": payment, "client_reference_id": reference, "amount_total": amount, "currency": currency}},
    }


def refunded(payment="pi_100", full=True):
    return {"type": "charge.refunded", "data": {"object": {"payment_intent": payment, "refunded": full}}}


def disputed(payment="pi_100"):
    return {"type": "charge.dispute.created", "data": {"object": {"payment_intent": payment}}}


@pytest.fixture
def runtime(tmp_path):
    rt = DeeperRuntime(
        meter=Meter(str(tmp_path / "meter.db"), clock=lambda: date(2026, 10, 5)),
        claims=ClaimStore(str(tmp_path / "claims.db")),
        webhook_secret=SECRET,
        products={
            LINK_SINGLE: Product("single", 25),
            LINK_SPONSOR: Product("batch", 10, count=3),
        },
        site_origin="https://site.example",
        miss_delay_seconds=0.0,
    )
    yield rt
    rt.meter.close()
    rt.claims.close()


def make_app(store, usage_store, world_loader, registry, *, deeper=None, rate_limit=False, admin_token=ADMIN):
    return create_app(
        voice_client=object(), voice_model_id="m", safety_client=object(), safety_model_id="m",
        store=store, usage_store=usage_store, world_loader=world_loader, registry=registry,
        default_world_key="fix", admin_token=admin_token, deeper=deeper, rate_limit=rate_limit,
    )


@pytest.fixture
def http(store, usage_store, world_loader, registry, runtime):
    return TestClient(make_app(store, usage_store, world_loader, registry, deeper=runtime))


def post_event(http, event, *, stamp=None, secret=SECRET):
    body = json.dumps(event).encode()
    return http.post("/api/deeper/webhook", content=body, headers={"Stripe-Signature": sign(body, secret=secret, stamp=stamp), "content-type": "application/json"})


def claim(http, reference=REF, **kw):
    return http.post("/api/deeper/claim", json={"reference": reference}, **kw)


def admin(token=ADMIN):
    return {"Authorization": f"Bearer {token}"}


# ---- flag off ----------------------------------------------------------------

def test_flag_off_mounts_no_deeper_route(store, usage_store, world_loader, registry):
    app = make_app(store, usage_store, world_loader, registry, deeper=None)
    paths = [getattr(r, "path", "") for r in app.routes]
    assert not [p for p in paths if p.startswith(("/api/deeper", "/api/admin/deeper"))]
    http = TestClient(app)
    assert http.post("/api/deeper/webhook", content=b"{}").status_code == 404
    assert http.post("/api/deeper/claim", json={"reference": REF}).status_code == 404
    assert http.get("/api/deeper/balance").status_code == 404
    assert http.post("/api/admin/deeper/pause", json={"on": True}, headers=admin()).status_code == 404
    assert http.get("/api/admin/deeper/reconciliation", headers=admin()).status_code == 404
    assert http.get("/api/admin/deeper/funds", headers=admin()).status_code == 404
    assert http.get("/api/admin/deeper/door", headers=admin()).status_code == 404


def test_flag_on_mounts_every_route(store, usage_store, world_loader, registry, runtime):
    app = make_app(store, usage_store, world_loader, registry, deeper=runtime)
    paths = {getattr(r, "path", "") for r in app.routes}
    assert {
        "/api/deeper/webhook", "/api/deeper/claim", "/api/deeper/balance",
        "/api/admin/deeper/pause", "/api/admin/deeper/reconciliation",
        "/api/admin/deeper/funds", "/api/admin/deeper/funds/{entry_id}/reverse", "/api/admin/deeper/door",
    } <= paths


# ---- signature ---------------------------------------------------------------

def test_a_bad_signature_is_400_and_mints_nothing(http, runtime):
    assert post_event(http, completed(), secret="whsec_wrong").status_code == 400
    assert runtime.meter.reconciliation() == []
    assert claim(http).status_code == 404


def test_a_missing_or_malformed_signature_is_400(http):
    body = json.dumps(completed()).encode()
    assert http.post("/api/deeper/webhook", content=body).status_code == 400
    assert http.post("/api/deeper/webhook", content=body, headers={"Stripe-Signature": "nonsense"}).status_code == 400
    assert http.post("/api/deeper/webhook", content=body, headers={"Stripe-Signature": "t=abc,v1=00"}).status_code == 400


def test_a_stale_signature_is_400(http):
    assert post_event(http, completed(), stamp=int(time.time()) - 301).status_code == 400


def test_a_tampered_body_is_400(http):
    body = json.dumps(completed()).encode()
    header = sign(body)
    assert http.post("/api/deeper/webhook", content=body + b" ", headers={"Stripe-Signature": header}).status_code == 400


def test_verify_signature_accepts_any_matching_v1():
    body = b"{}"
    good = sign(body).split("v1=")[1]
    stamp = sign(body).split(",")[0]
    assert verify_signature(body, f"{stamp},v1={'0' * 64},v1={good}", SECRET)
    assert not verify_signature(body, f"{stamp},v1={'0' * 64}", SECRET)
    assert not verify_signature(body, f"{stamp},{stamp},v1={good}", SECRET)
    assert not verify_signature(body, None, SECRET)
    assert not verify_signature(body, sign(body), "")


def test_a_non_object_payload_is_400(http):
    body = b"[1]"
    assert http.post("/api/deeper/webhook", content=body, headers={"Stripe-Signature": sign(body)}).status_code == 400
    body = b"not json"
    assert http.post("/api/deeper/webhook", content=body, headers={"Stripe-Signature": sign(body)}).status_code == 400


# ---- minting and claiming ----------------------------------------------------

def test_a_paid_checkout_mints_one_code_the_page_can_claim(http, runtime):
    assert post_event(http, completed()).status_code == 200
    got = claim(http)
    assert got.status_code == 200
    body = got.json()
    assert body["tokens"] == 25 and len(body["codes"]) == 1
    assert runtime.meter.verify(body["codes"][0])
    assert runtime.meter.status(body["codes"][0]).remaining == 25


def test_a_claim_can_be_read_again(http):
    post_event(http, completed())
    assert claim(http).json() == claim(http).json()


def test_a_replayed_webhook_is_idempotent(http, runtime):
    post_event(http, completed())
    first = claim(http).json()
    assert post_event(http, completed()).status_code == 200
    assert claim(http).json() == first
    (day,) = runtime.meter.reconciliation()
    assert day["payments_seen"] == 1 and day["payments_minted"] == 1 and day["codes_minted"] == 1 and day["gap"] == 0


def test_a_replay_after_the_claim_expired_leaves_no_dead_claim(http, runtime):
    post_event(http, completed())
    runtime.claims.delete(REF)
    post_event(http, completed())
    assert claim(http).status_code == 404


def test_a_sponsor_batch_gives_every_code_the_full_balance(http, runtime):
    post_event(http, completed(payment="pi_200", link=LINK_SPONSOR, reference="sponsor-reference-0001"))
    body = claim(http, "sponsor-reference-0001").json()
    assert len(set(body["codes"])) == 3 and body["tokens"] == 10
    assert all(runtime.meter.status(c).remaining == 10 for c in body["codes"])
    (day,) = runtime.meter.reconciliation()
    assert day["codes_minted"] == 3 and day["payments_minted"] == 1


def test_a_gift_link_makes_no_codes_and_is_not_counted(http, runtime):
    assert post_event(http, completed(link=LINK_GIFT)).status_code == 200
    assert claim(http).status_code == 404
    assert runtime.meter.reconciliation() == []


def test_an_unpaid_checkout_makes_no_codes_until_it_is_paid(http, runtime):
    post_event(http, completed(paid="unpaid"))
    assert claim(http).status_code == 404
    post_event(http, completed(kind="checkout.session.async_payment_succeeded"))
    assert claim(http).status_code == 200


def test_unrelated_event_types_are_acknowledged_and_ignored(http, runtime):
    assert post_event(http, {"type": "customer.created", "data": {"object": {}}}).status_code == 200
    assert runtime.meter.reconciliation() == []


def test_a_paid_checkout_with_no_usable_reference_is_a_counted_gap_and_mints_nothing(http, runtime):
    post_event(http, completed(reference=None))
    post_event(http, completed(payment="pi_101", reference="short"))
    (day,) = runtime.meter.reconciliation()
    assert day["payments_seen"] == 2 and day["payments_minted"] == 0 and day["gap"] == 2
    assert runtime.meter._conn.execute("SELECT COUNT(*) FROM meter").fetchone() == (0,)


def test_a_paid_checkout_with_no_payment_intent_is_a_counted_gap(http, runtime):
    event = completed()
    del event["data"]["object"]["payment_intent"]
    post_event(http, event)
    (day,) = runtime.meter.reconciliation()
    assert day["gap"] == 1


def test_a_reference_reused_for_a_different_purchase_mints_nothing_new(http, runtime):
    post_event(http, completed(payment="pi_300"))
    first = claim(http).json()
    post_event(http, completed(payment="pi_301", link=LINK_SPONSOR))
    assert claim(http).json() == first
    (day,) = runtime.meter.reconciliation()
    assert day["gap"] == 1


def test_a_crash_between_claim_and_mint_is_finished_by_the_replay(http, runtime):
    stored = [codes.generate()]
    runtime.claims.put(REF, stored)
    assert runtime.meter.status(stored[0]) is None
    post_event(http, completed())
    assert claim(http).json()["codes"] == [codes.display(stored[0])]
    assert runtime.meter.verify(stored[0])


def test_an_expired_claim_is_gone(http, runtime):
    now = [1_800_000_000.0]
    runtime.claims._clock = lambda: now[0]
    post_event(http, completed())
    assert claim(http).status_code == 200
    now[0] += 3600
    assert claim(http).status_code == 404


def test_a_malformed_or_unknown_reference_is_404(http):
    assert claim(http, "x" * 20).status_code == 404
    assert claim(http, "short").status_code == 404
    assert http.post("/api/deeper/claim", json={}).status_code == 422


# ---- refunds and disputes ----------------------------------------------------

def test_a_full_refund_voids_the_code(http, runtime):
    post_event(http, completed())
    (code,) = claim(http).json()["codes"]
    post_event(http, refunded())
    assert runtime.meter.reserve(code).reason == "void"
    assert http.get("/api/deeper/balance", headers={"x-cic-code": code}).status_code == 404
    assert runtime.meter.reconciliation()[0]["refunds_applied"] == 1


def test_a_partial_refund_voids_nothing(http, runtime):
    post_event(http, completed())
    (code,) = claim(http).json()["codes"]
    post_event(http, refunded(full=False))
    assert runtime.meter.reserve(code).ok


def test_a_dispute_voids_the_whole_sponsor_batch(http, runtime):
    post_event(http, completed(payment="pi_400", link=LINK_SPONSOR, reference="sponsor-reference-0002"))
    batch = claim(http, "sponsor-reference-0002").json()["codes"]
    post_event(http, disputed("pi_400"))
    assert all(runtime.meter.reserve(c).reason == "void" for c in batch)
    assert runtime.meter.reconciliation()[0]["refunds_applied"] == 3


def test_a_refund_arriving_before_its_completion_blocks_the_mint(http, runtime):
    post_event(http, refunded("pi_500"))
    post_event(http, completed(payment="pi_500"))
    assert claim(http).status_code == 404
    (day,) = runtime.meter.reconciliation()
    assert day["payments_voided_first"] == 1 and day["gap"] == 0


# ---- balance -----------------------------------------------------------------

def test_balance_reports_what_is_left(http, runtime):
    post_event(http, completed())
    (code,) = claim(http).json()["codes"]
    runtime.meter.settle(runtime.meter.reserve(code).reservation, True)
    got = http.get("/api/deeper/balance", headers={"x-cic-code": codes.display(code).lower()})
    assert got.status_code == 200
    assert got.json() == {"kind": "single", "remaining": 24, "paused": False}


def test_balance_of_a_spent_code_is_zero_not_missing(http, runtime):
    post_event(http, completed())
    (code,) = claim(http).json()["codes"]
    for _ in range(25):
        runtime.meter.settle(runtime.meter.reserve(code).reservation, True)
    assert http.get("/api/deeper/balance", headers={"x-cic-code": code}).json()["remaining"] == 0


def test_a_wrong_code_is_a_plain_404_after_the_delay(http, runtime):
    runtime.miss_delay_seconds = 0.2
    started = time.monotonic()
    got = http.get("/api/deeper/balance", headers={"x-cic-code": codes.generate()})
    assert got.status_code == 404
    assert time.monotonic() - started >= 0.2
    assert http.get("/api/deeper/balance").status_code == 404
    assert http.get("/api/deeper/balance", headers={"x-cic-code": "garbage"}).status_code == 404


# ---- pause -------------------------------------------------------------------

def test_pause_needs_the_admin_credential(http, runtime):
    assert http.post("/api/admin/deeper/pause", json={"on": True}).status_code == 404
    assert http.post("/api/admin/deeper/pause", json={"on": True}, headers=admin("wrong")).status_code == 404
    assert not runtime.meter.is_paused()


def test_pause_stops_the_next_admission_and_unpause_restores_it(http, runtime):
    post_event(http, completed())
    (code,) = claim(http).json()["codes"]
    assert http.post("/api/admin/deeper/pause", json={"on": True}, headers=admin()).json() == {"paused": True}
    assert runtime.meter.reserve(code).reason == "paused"
    assert http.get("/api/deeper/balance", headers={"x-cic-code": code}).json()["paused"] is True
    assert http.post("/api/admin/deeper/pause", json={"on": False}, headers=admin()).json() == {"paused": False}
    assert runtime.meter.reserve(code).ok


def test_pause_works_with_no_admin_token_configured_only_as_a_404(store, usage_store, world_loader, registry, runtime):
    http = TestClient(make_app(store, usage_store, world_loader, registry, deeper=runtime, admin_token=None))
    assert http.post("/api/admin/deeper/pause", json={"on": True}, headers=admin()).status_code == 404


# ---- reconciliation ----------------------------------------------------------

def test_reconciliation_is_admin_only_and_shows_the_gap(http, runtime):
    post_event(http, completed(reference=None))
    assert http.get("/api/admin/deeper/reconciliation").status_code == 404
    days = http.get("/api/admin/deeper/reconciliation", headers=admin()).json()["days"]
    assert days[0]["gap"] == 1


def test_the_retention_pass_reports_and_warns_on_a_gap(http, runtime, caplog):
    post_event(http, completed(reference=None))
    caplog.set_level(logging.WARNING, logger="cic.deeper")
    result = deeper_routes.run_retention_once(runtime)
    assert result["gap_days"] == 1
    assert "reconciliation gap" in caplog.text


# ---- cross-origin claim ------------------------------------------------------

def test_the_claim_route_answers_the_site_origin_and_no_other(http):
    post_event(http, completed())
    ok = claim(http, headers={"Origin": "https://site.example"})
    assert ok.headers["access-control-allow-origin"] == "https://site.example"
    assert "access-control-allow-origin" not in claim(http, headers={"Origin": "https://evil.example"}).headers
    pre = http.options("/api/deeper/claim", headers={"Origin": "https://site.example"})
    assert pre.status_code == 204 and pre.headers["access-control-allow-origin"] == "https://site.example"
    assert "access-control-allow-origin" not in http.options("/api/deeper/claim", headers={"Origin": "https://evil.example"}).headers


def test_no_origin_is_allowed_when_none_is_configured(store, usage_store, world_loader, registry, runtime):
    runtime.site_origin = None
    http = TestClient(make_app(store, usage_store, world_loader, registry, deeper=runtime))
    post_event(http, completed())
    assert "access-control-allow-origin" not in claim(http, headers={"Origin": "https://site.example"}).headers


# ---- rate limit --------------------------------------------------------------

def test_the_webhook_is_exempt_from_the_per_ip_limit_and_the_deeper_bucket_is_its_own(store, usage_store, world_loader, registry, runtime):
    http = TestClient(make_app(store, usage_store, world_loader, registry, deeper=runtime, rate_limit=True))
    for _ in range(120):
        assert http.post("/api/deeper/webhook", content=b"{}").status_code == 400
    statuses = [http.get("/api/deeper/balance").status_code for _ in range(61)]
    assert statuses[:60] == [404] * 60 and statuses[60] == 429
    assert http.post("/api/deeper/webhook", content=b"{}").status_code == 400


def test_deeper_traffic_does_not_use_up_the_conversation_bucket(store, usage_store, world_loader, registry, runtime):
    http = TestClient(make_app(store, usage_store, world_loader, registry, deeper=runtime, rate_limit=True))
    for _ in range(61):
        http.get("/api/deeper/balance")
    assert http.get("/api/session/abc/transcript").status_code != 429


# ---- logs --------------------------------------------------------------------

def test_the_access_log_filter_drops_session_and_deeper_paths_only():
    flt = deeper_routes.AccessLogFilter()

    def record(path):
        return logging.LogRecord("uvicorn.access", logging.INFO, "", 0, '%s - "%s %s HTTP/%s" %d', ("1.2.3.4:5", "POST", path, "1.1", 200), None)

    assert not flt.filter(record("/api/session"))
    assert not flt.filter(record("/api/session/abc/message"))
    assert not flt.filter(record("/api/deeper/claim?x=1"))
    assert flt.filter(record("/health"))
    assert flt.filter(record("/api/worlds"))
    assert flt.filter(logging.LogRecord("uvicorn.access", logging.INFO, "", 0, "plain", None, None))


def test_install_access_log_filter_is_idempotent():
    deeper_routes.install_access_log_filter()
    deeper_routes.install_access_log_filter()
    target = logging.getLogger("uvicorn.access")
    assert sum(isinstance(f, deeper_routes.AccessLogFilter) for f in target.filters) == 1
    for f in [f for f in target.filters if isinstance(f, deeper_routes.AccessLogFilter)]:
        target.removeFilter(f)


def test_no_code_reference_or_hash_reaches_the_logs(http, runtime, caplog):
    caplog.set_level(logging.DEBUG)
    post_event(http, completed())
    (code,) = claim(http).json()["codes"]
    plain = codes.normalize(code)
    http.get("/api/deeper/balance", headers={"x-cic-code": code})
    post_event(http, refunded())
    http.post("/api/admin/deeper/pause", json={"on": True}, headers=admin())
    text = caplog.text
    assert plain not in text and code not in text
    assert codes.hash_code(plain) not in text
    assert REF not in text
    assert not re.search(r"[2-9A-HJ-NP-Z]{20}", text)


# ---- startup -----------------------------------------------------------------

def test_parse_products_reads_the_deploy_setting():
    parsed = parse_products(json.dumps({"p1": {"kind": "batch", "tokens": 5, "count": 4}, "p2": {"kind": "group", "tokens": 80, "daily_ceiling": 40}}))
    assert parsed["p1"] == Product("batch", 5, 4)
    assert parsed["p2"] == Product("group", 80, 1, 40)
    assert parse_products(None) == {} and parse_products("") == {}


@pytest.mark.parametrize(
    "raw",
    ["not json", "[1]", json.dumps({"p": {"kind": "pack", "tokens": 5}}), json.dumps({"p": {"kind": "single"}}),
     json.dumps({"p": {"kind": "single", "tokens": 0}}), json.dumps({"p": {"kind": "single", "tokens": 5, "count": 2}})],
)
def test_parse_products_refuses_a_bad_setting(raw):
    with pytest.raises(DeeperConfigError):
        parse_products(raw)


def test_the_flag_on_refuses_to_start_without_a_webhook_secret(tmp_path):
    config = DeeperConfig(True, str(tmp_path / "m.db"), str(tmp_path / "c.db"))
    with pytest.raises(DeeperConfigError):
        deeper_routes.build_runtime(config, {})
    runtime = deeper_routes.build_runtime(
        config, {"CIC_DEEPER_WEBHOOK_SECRET": SECRET, "CIC_DEEPER_SITE_ORIGIN": "https://site.example", "CIC_API_ANON_CAP_ENABLED": "1"}
    )
    assert runtime.site_origin == "https://site.example" and runtime.products == {}
    runtime.meter.close()
    runtime.claims.close()


@pytest.mark.parametrize("flag", [None, "", "0", "no"])
def test_the_flag_on_refuses_to_start_without_the_visitor_cap(tmp_path, flag):
    config = DeeperConfig(True, str(tmp_path / "m.db"), str(tmp_path / "c.db"))
    env = {"CIC_DEEPER_WEBHOOK_SECRET": SECRET}
    if flag is not None:
        env["CIC_API_ANON_CAP_ENABLED"] = flag
    with pytest.raises(DeeperConfigError):
        deeper_routes.build_runtime(config, env)


def test_the_config_defaults_to_the_data_directory(monkeypatch, tmp_path):
    for name in ("CIC_DEEPER_ENABLED", "CIC_DEEPER_METER_DB", "CIC_DEEPER_CLAIMS_DB"):
        monkeypatch.delenv(name, raising=False)
    config = DeeperConfig.from_env(str(tmp_path))
    assert not config.enabled
    assert config.meter_db_path == str(tmp_path / "cic_deeper_meter.db")
    assert config.claims_db_path == str(tmp_path / "cic_deeper_claims.db")
    monkeypatch.setenv("CIC_DEEPER_ENABLED", "1")
    assert DeeperConfig.from_env(str(tmp_path)).enabled


# ---- round two: reused references, stale claims, bounded bodies --------------

def test_a_second_purchase_on_the_same_reference_leaves_the_first_claim_intact(http, runtime):
    post_event(http, completed(payment="pi_a"))
    first = claim(http).json()
    post_event(http, completed(payment="pi_b"))
    assert claim(http).json() == first
    assert all(runtime.meter.verify(c) for c in first["codes"])
    (day,) = runtime.meter.reconciliation()
    assert day["payments_minted"] == 1 and day["gap"] == 1


def test_a_retry_after_the_claim_hour_makes_codes_the_buyer_can_reach(http, runtime):
    now = [1_800_000_000.0]
    runtime.claims._clock = lambda: now[0]
    runtime.claims.put(REF, [codes.generate()])
    now[0] += 3600
    post_event(http, completed(payment="pi_late"))
    got = claim(http)
    assert got.status_code == 200
    assert all(runtime.meter.verify(c) for c in got.json()["codes"])
    (day,) = runtime.meter.reconciliation()
    assert day["payments_minted"] == 1 and day["gap"] == 0


def test_a_claim_that_cannot_be_stored_mints_nothing_and_shows_as_a_gap(http, runtime, monkeypatch):
    monkeypatch.setattr(runtime.claims, "put", lambda *a, **k: False)
    post_event(http, completed())
    assert runtime.meter._conn.execute("SELECT COUNT(*) FROM meter").fetchone() == (0,)
    assert runtime.meter.reconciliation()[0]["gap"] == 1


def test_a_replay_never_touches_a_claim_it_did_not_make(http, runtime):
    post_event(http, completed())
    first = claim(http).json()
    post_event(http, completed())
    post_event(http, completed())
    assert claim(http).json() == first


def test_the_claim_page_waits_until_the_codes_exist_in_the_meter(http, runtime):
    runtime.claims.put(REF, [codes.generate()])
    assert claim(http).status_code == 404
    post_event(http, completed())
    assert claim(http).status_code == 200


def test_an_oversized_webhook_body_is_refused_before_the_signature_is_read(http):
    big = b"x" * (deeper_routes.MAX_WEBHOOK_BODY_BYTES + 1)
    assert http.post("/api/deeper/webhook", content=big, headers={"Stripe-Signature": sign(big)}).status_code == 413


def test_a_partial_refund_leaves_a_trace_on_the_reconciliation(http, runtime):
    post_event(http, completed())
    post_event(http, refunded(full=False))
    assert runtime.meter.reconciliation()[0]["partial_refunds_ignored"] == 1


def test_a_refunded_code_is_not_served_by_the_claim_route(http, runtime):
    post_event(http, completed())
    assert claim(http).status_code == 200
    post_event(http, refunded())
    assert claim(http).status_code == 404


# ---- the door's funds: gifts, purchases and adjustments ------------------------------

@pytest.fixture
def gift_runtime(runtime):
    runtime.gift_links = frozenset({LINK_GIFT})
    return runtime


def test_a_paid_gift_is_counted_and_makes_no_code(http, gift_runtime):
    assert post_event(http, completed(link=LINK_GIFT, payment="pi_g1", amount=2500)).status_code == 200
    assert gift_runtime.meter.net_funds() == {"gift": 2500, "purchase": 0, "adjustment": 0}
    assert claim(http).status_code == 404


def test_a_go_deeper_purchase_counts_as_a_purchase_and_never_as_a_gift(http, gift_runtime):
    post_event(http, completed(payment="pi_p1", amount=700))
    assert gift_runtime.meter.net_funds() == {"gift": 0, "purchase": 700, "adjustment": 0}


def test_a_replayed_event_adds_the_money_once(http, gift_runtime):
    for _ in range(3):
        post_event(http, completed(link=LINK_GIFT, payment="pi_g1", amount=2500))
    assert gift_runtime.meter.net_funds()["gift"] == 2500


def test_an_unpaid_checkout_counts_nothing(http, gift_runtime):
    post_event(http, completed(link=LINK_GIFT, payment="pi_g2", amount=2500, paid="unpaid"))
    assert gift_runtime.meter.net_funds() == {"gift": 0, "purchase": 0, "adjustment": 0}


def test_a_refund_or_dispute_takes_a_gift_and_a_purchase_back_out(http, gift_runtime):
    post_event(http, completed(link=LINK_GIFT, payment="pi_g1", amount=2500))
    post_event(http, completed(payment="pi_p1", amount=700))
    post_event(http, refunded("pi_g1"))
    post_event(http, disputed("pi_p1"))
    assert gift_runtime.meter.net_funds() == {"gift": 0, "purchase": 0, "adjustment": 0}


def test_a_payment_refunded_before_its_completion_arrives_counts_nothing(http, gift_runtime):
    post_event(http, refunded("pi_late"))
    post_event(http, completed(link=LINK_GIFT, payment="pi_late", amount=2500))
    assert gift_runtime.meter.net_funds()["gift"] == 0


@pytest.mark.parametrize("amount", [None, 0, -5, "700", True, 10_000_001])
def test_a_checkout_with_no_usable_amount_counts_nothing(http, gift_runtime, amount):
    event = completed(link=LINK_GIFT, payment="pi_g3")
    event["data"]["object"]["amount_total"] = amount
    assert post_event(http, event).status_code == 200
    assert gift_runtime.meter.net_funds()["gift"] == 0


def test_the_admin_adds_lists_and_reverses_an_adjustment(http, runtime):
    added = http.post("/api/admin/deeper/funds", json={"cents": 5000, "note": "church gift, cash"}, headers=admin())
    assert added.status_code == 200
    entry = added.json()["id"]
    listing = http.get("/api/admin/deeper/funds", headers=admin()).json()
    assert listing["net"]["adjustment"] == 5000
    assert listing["entries"][0]["note"] == "church gift, cash" and "payment_id" not in listing["entries"][0]
    assert http.post(f"/api/admin/deeper/funds/{entry}/reverse", headers=admin()).status_code == 200
    assert http.get("/api/admin/deeper/funds", headers=admin()).json()["net"]["adjustment"] == 0
    assert http.post(f"/api/admin/deeper/funds/{entry}/reverse", headers=admin()).status_code == 404


@pytest.mark.parametrize("body", [{"cents": 0, "note": "x"}, {"cents": 5000, "note": ""}, {"cents": 5000}, {"note": "x"}, {"cents": 10_000_001, "note": "x"}])
def test_a_bad_adjustment_is_refused(http, body):
    assert http.post("/api/admin/deeper/funds", json=body, headers=admin()).status_code == 422


def test_the_funds_routes_need_the_admin_credential(http, runtime):
    entry = runtime.meter.add_funds("adjustment", 500, note="kept")
    assert http.get("/api/admin/deeper/funds").status_code == 404
    assert http.post("/api/admin/deeper/funds", json={"cents": 1, "note": "x"}, headers=admin("wrong")).status_code == 404
    assert http.post(f"/api/admin/deeper/funds/{entry}/reverse").status_code == 404
    assert http.post(f"/api/admin/deeper/funds/{entry}/reverse", headers=admin("wrong")).status_code == 404
    assert runtime.meter.net_funds()["adjustment"] == 500
    assert http.post(f"/api/admin/deeper/funds/{entry}/reverse", headers=admin()).status_code == 200
    assert runtime.meter.net_funds()["adjustment"] == 0


@pytest.mark.parametrize("currency", ["inr", "eur", "USD", None, ""])
def test_a_checkout_not_in_us_dollars_counts_nothing(http, gift_runtime, currency):
    event = completed(link=LINK_GIFT, payment="pi_fx", amount=60000)
    if currency is None:
        del event["data"]["object"]["currency"]
    else:
        event["data"]["object"]["currency"] = currency
    assert post_event(http, event).status_code == 200
    assert gift_runtime.meter.net_funds()["gift"] == 0


def test_a_checkout_in_us_dollars_counts(http, gift_runtime):
    post_event(http, completed(link=LINK_GIFT, payment="pi_usd", amount=2500, currency="usd"))
    assert gift_runtime.meter.net_funds()["gift"] == 2500


def test_a_link_cannot_be_both_a_gift_and_a_product():
    products = {LINK_SINGLE: Product("single", 25)}
    assert deeper_routes.parse_gift_links(json.dumps([LINK_GIFT]), products) == frozenset({LINK_GIFT})
    assert deeper_routes.parse_gift_links(None, products) == frozenset()
    for bad in ("not json", "{}", json.dumps([1]), json.dumps([""]), json.dumps([LINK_SINGLE])):
        with pytest.raises(DeeperConfigError):
            deeper_routes.parse_gift_links(bad, products)


# ---- the door's route and its wiring --------------------------------------------------

def test_the_door_route_reports_nothing_without_a_door_and_the_state_with_one(http, runtime, tmp_path):
    assert http.get("/api/admin/deeper/door", headers=admin()).json() == {"door": None}
    from engine.deeper import door as door_module

    class Stub:
        def state(self):
            return door_module.DoorState(stage=3, ratio=0.91234, ceiling_usd=150.0, table_free_rounds=0, free_voice=True, paid_voice=True)

    runtime.door = Stub()
    assert http.get("/api/admin/deeper/door", headers=admin()).json() == {
        "door": {"stage": 3, "ratio": 0.912, "ceiling_usd": 150.0, "free_voice": True, "paid_voice": True}
    }


def test_the_door_route_needs_the_admin_credential(http):
    assert http.get("/api/admin/deeper/door").status_code == 404
    assert http.get("/api/admin/deeper/door", headers=admin("wrong")).status_code == 404


def test_the_runtime_gets_a_door_only_when_given_the_usage_log(tmp_path):
    from engine.m8.log_store import UsageLogStore

    config = DeeperConfig(True, str(tmp_path / "m.db"), str(tmp_path / "c.db"))
    env = {"CIC_DEEPER_WEBHOOK_SECRET": SECRET, "CIC_API_ANON_CAP_ENABLED": "1"}
    without = deeper_routes.build_runtime(config, env)
    assert without.door is None
    without.meter.close()
    without.claims.close()
    config = DeeperConfig(True, str(tmp_path / "m2.db"), str(tmp_path / "c2.db"))
    with_log = deeper_routes.build_runtime(config, env, usage_store=UsageLogStore(tmp_path / "usage.db"))
    assert with_log.door is not None and with_log.door.state().stage == 0
    with_log.meter.close()
    with_log.claims.close()
