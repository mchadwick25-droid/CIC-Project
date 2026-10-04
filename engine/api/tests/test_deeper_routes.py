"""Go Deeper's HTTP edge: the signed webhook, claim, balance, pause and
reconciliation routes, and the proof that with the flag off none of them exist."""
import hashlib
import hmac
import json
import logging
import re
import time
from datetime import date, timedelta

import pytest
from fastapi.testclient import TestClient

from engine.api import deeper_routes
from engine.api.app import create_app
from engine.api.deeper_ops import load_ops
from engine.api.deeper_routes import DeeperConfigError, DeeperRuntime, Product, parse_products, verify_signature
from engine.deeper import codes
from engine.deeper.claims import ClaimStore
from engine.deeper.config import DeeperConfig
from engine.deeper.meter import Meter

FREE_KEY = "k" * 40
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
    assert http.get("/api/deeper/door").status_code == 404
    assert http.post("/api/admin/deeper/pause", json={"on": True}, headers=admin()).status_code == 404
    assert http.get("/api/admin/deeper/reconciliation", headers=admin()).status_code == 404
    assert http.get("/api/admin/deeper/funds", headers=admin()).status_code == 404
    assert http.get("/api/admin/deeper/door", headers=admin()).status_code == 404
    assert http.get("/api/admin/deeper/owed", headers=admin()).status_code == 404
    assert http.post("/api/admin/deeper/void", json={"payment_id": "pi_x"}, headers=admin()).status_code == 404
    assert http.get("/api/admin/deeper/measures", headers=admin()).status_code == 404


def test_flag_on_mounts_every_route(store, usage_store, world_loader, registry, runtime):
    app = make_app(store, usage_store, world_loader, registry, deeper=runtime)
    paths = {getattr(r, "path", "") for r in app.routes}
    assert {
        "/api/deeper/webhook", "/api/deeper/claim", "/api/deeper/balance", "/api/deeper/door",
        "/api/admin/deeper/pause", "/api/admin/deeper/reconciliation",
        "/api/admin/deeper/funds", "/api/admin/deeper/funds/{entry_id}/reverse", "/api/admin/deeper/door", "/api/admin/deeper/measures", "/api/admin/deeper/owed", "/api/admin/deeper/void",
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
        config, {"CIC_DEEPER_WEBHOOK_SECRET": SECRET, "CIC_DEEPER_SITE_ORIGIN": "https://site.example", "CIC_API_ANON_CAP_ENABLED": "1", "CIC_DEEPER_FREE_KEY": FREE_KEY}
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
        "door": {"stage": 3, "ratio": 0.912, "ceiling_usd": 150.0, "free_voice": True, "paid_voice": True, "observe": False}
    }


def test_the_door_route_needs_the_admin_credential(http):
    assert http.get("/api/admin/deeper/door").status_code == 404
    assert http.get("/api/admin/deeper/door", headers=admin("wrong")).status_code == 404


def test_the_runtime_gets_a_door_only_when_given_the_usage_log(tmp_path):
    from engine.m8.log_store import UsageLogStore

    config = DeeperConfig(True, str(tmp_path / "m.db"), str(tmp_path / "c.db"))
    env = {"CIC_DEEPER_WEBHOOK_SECRET": SECRET, "CIC_API_ANON_CAP_ENABLED": "1", "CIC_DEEPER_FREE_KEY": FREE_KEY}
    without = deeper_routes.build_runtime(config, env)
    assert without.door is None
    without.meter.close()
    without.claims.close()
    config = DeeperConfig(True, str(tmp_path / "m2.db"), str(tmp_path / "c2.db"))
    with_log = deeper_routes.build_runtime(config, env, usage_store=UsageLogStore(tmp_path / "usage.db"))
    assert with_log.door is not None and with_log.door.state().stage == 0
    with_log.meter.close()
    with_log.claims.close()


def test_a_restart_with_the_usage_log_down_still_finds_the_door_where_it_was_left(tmp_path):
    from engine.api.deeper_door import STATE_KEY, _encode
    from engine.deeper import door as door_module

    meter_path = str(tmp_path / "m.db")
    closed = door_module.DoorState(stage=4, ratio=0.97, ceiling_usd=150.0, table_free_rounds=0, free_voice=False)
    first = Meter(meter_path)
    first.set_state(STATE_KEY, _encode(closed))
    first.close()

    class Broken:
        def read_since(self, _since):
            raise RuntimeError("usage log down")

    config = DeeperConfig(True, meter_path, str(tmp_path / "c.db"))
    runtime = deeper_routes.build_runtime(config, {"CIC_DEEPER_WEBHOOK_SECRET": SECRET, "CIC_API_ANON_CAP_ENABLED": "1", "CIC_DEEPER_FREE_KEY": FREE_KEY}, usage_store=Broken())
    state = runtime.door.state()
    assert (state.stage, state.free_voice, state.table_free_rounds) == (4, False, 0)
    runtime.meter.close()
    runtime.claims.close()


# ---- the standing measure's route ------------------------------------------------------------

def test_the_measures_route_needs_the_admin_credential(http):
    assert http.get("/api/admin/deeper/measures").status_code == 404
    assert http.get("/api/admin/deeper/measures", headers=admin("wrong")).status_code == 404


def test_the_measures_route_shows_daily_totals_and_the_reconciliation_and_no_keys(http, runtime):
    runtime.meter.mint("single", 1100, "pi_m")
    runtime.meter.measure("refused_no_code")
    body = http.get("/api/admin/deeper/measures", headers=admin()).json()
    (today,) = body["measures"]
    assert (today["codes_single"], today["tokens_sold"], today["refused_no_code"]) == (1, 1100, 1)
    assert body["reconciliation"][0]["payments_minted"] == 1
    assert not any(word in json.dumps(body).lower() for word in ("session", "visitor", "hash"))


def test_the_door_monitor_reports_each_stage_it_reaches_to_be_counted(tmp_path):
    from datetime import datetime, timezone

    from engine.api.deeper_door import DoorMonitor
    from engine.api.deeper_ops import load_ops
    from engine.m8.log_store import UsageLogStore

    seen = []
    monitor = DoorMonitor(
        load_ops().door, UsageLogStore(tmp_path / "usage.db"), lambda: {},
        clock=lambda: datetime(2026, 10, 5, tzinfo=timezone.utc), observe=lambda state: seen.append(state.stage),
    )
    monitor.state()
    assert seen == [0]


def test_a_measure_that_fails_never_touches_the_door(tmp_path):
    from datetime import datetime, timezone

    from engine.api.deeper_door import DoorMonitor
    from engine.api.deeper_ops import load_ops
    from engine.m8.log_store import UsageLogStore

    def broken(_state):
        raise RuntimeError("meter down")

    monitor = DoorMonitor(
        load_ops().door, UsageLogStore(tmp_path / "usage.db"), lambda: {},
        clock=lambda: datetime(2026, 10, 5, tzinfo=timezone.utc), observe=broken,
    )
    assert monitor.state().stage == 0


def test_the_dashboard_section_is_hidden_until_the_route_answers_and_names_every_measure():
    from pathlib import Path

    from engine.deeper.meter import REFUSAL_REASONS, SUM_MEASURES

    page = (Path(deeper_routes.__file__).parent / "static" / "admin_dashboard.html").read_text()
    assert '<section id="deeper-section" class="hidden">' in page
    assert "/api/admin/deeper/measures" in page
    for reason in REFUSAL_REASONS:
        assert f"refused_{reason}:" in page, reason
    for name in SUM_MEASURES:
        assert name in page or name.startswith("refused_"), name


# ---- the public door line ----------------------------------------------------------------

def _public_door(http, runtime, **fields):
    from engine.deeper import door as door_module

    from engine.api.deeper_ops import load_ops

    runtime.ops = load_ops()

    stage = fields.pop("stage", 1)

    class Stub:
        def state(self):
            return door_module.DoorState(stage=stage, ratio=0.8, ceiling_usd=150.0, **fields)

    runtime.door = Stub()
    return http.get("/api/deeper/door")


def test_the_public_door_line_is_silent_while_the_door_is_wide_open(http, runtime):
    assert http.get("/api/deeper/door").json() == {"state": "open", "line": None}
    assert _public_door(http, runtime, stage=0).json() == {"state": "open", "line": None}


def test_the_public_door_line_says_limited_then_paused_in_mark_s_words(http, runtime):
    limited = _public_door(http, runtime, solo_free_rounds=2)
    words = runtime.ops.door_words
    assert limited.json() == {"state": "limited", "line": words["limited"]}
    paused = _public_door(http, runtime, stage=4, free_voice=False)
    assert paused.json() == {"state": "paused", "line": words["paused"] + " " + words["code_still_works"]}


def test_the_public_door_line_never_says_a_code_works_once_codes_are_refused(http, runtime):
    body = _public_door(http, runtime, stage=5, free_voice=False, paid_voice=False).json()
    assert body == {"state": "paused", "line": runtime.ops.door_words["paused"]}
    assert "code" not in body["line"].lower()


def test_the_public_door_line_carries_words_only_and_may_be_kept_a_minute(http, runtime):
    response = _public_door(http, runtime, stage=4, free_voice=False)
    assert set(response.json()) == {"state", "line"}
    assert response.headers["cache-control"] == "public, max-age=60"
    assert not any(key in response.text for key in ("ratio", "ceiling", "stage"))


# ---- the balances owed ---------------------------------------------------------------------------

def test_the_owed_route_needs_the_admin_credential(http):
    assert http.get("/api/admin/deeper/owed").status_code == 404
    assert http.get("/api/admin/deeper/owed", headers=admin("wrong")).status_code == 404


def test_the_owed_route_lists_unspent_tokens_by_payment(http, runtime):
    runtime.meter.mint("single", 1100, "pi_owed")
    (row,) = http.get("/api/admin/deeper/owed", headers=admin()).json()["owed"]
    assert (row["payment_id"], row["kind"], row["codes"], row["tokens_bought"], row["tokens_left"]) == ("pi_owed", "single", 1, 1100, 1100)


# ---- the admin void: a refund the webhook cannot see ---------------------------------------------------

def test_the_void_route_needs_the_admin_credential(http):
    assert http.post("/api/admin/deeper/void", json={"payment_id": "pi_x"}).status_code == 404
    assert http.post("/api/admin/deeper/void", json={"payment_id": "pi_x"}, headers=admin("wrong")).status_code == 404


def test_the_void_route_voids_the_codes_the_money_and_the_balance_owed(http, runtime):
    (code,) = runtime.meter.mint("single", 1100, "pi_partial")
    runtime.meter.add_funds("purchase", 700, "pi_partial")
    body = http.post("/api/admin/deeper/void", json={"payment_id": "pi_partial"}, headers=admin()).json()
    assert body == {"payment_id": "pi_partial", "voided": 1}
    assert runtime.meter.status(code).status == "void"
    assert runtime.meter.owed() == []
    assert runtime.meter.net_funds(7).get("purchase", 0) == 0
    assert runtime.meter.reconciliation()[0]["refunds_applied"] == 1


def test_a_payment_with_no_codes_is_not_found_and_nothing_is_recorded(http, runtime):
    body = http.post("/api/admin/deeper/void", json={"payment_id": "pi_mistyped"}, headers=admin())
    assert body.status_code == 404
    assert not runtime.meter.payment_voided("pi_mistyped")


def test_a_repeated_void_changes_nothing_and_a_late_completion_mints_nothing(http, runtime):
    runtime.meter.mint("single", 25, "pi_twice")
    first = http.post("/api/admin/deeper/void", json={"payment_id": "pi_twice"}, headers=admin()).json()
    again = http.post("/api/admin/deeper/void", json={"payment_id": "pi_twice"}, headers=admin()).json()
    assert (first["voided"], again["voided"]) == (1, 0)
    assert runtime.meter.owed() == []
    assert post_event(http, completed(payment="pi_twice")).status_code == 200
    assert runtime.meter.reconciliation()[0]["codes_minted"] == 1
    assert runtime.meter.reconciliation()[0]["payments_voided_first"] == 1


def test_the_webhook_refund_and_the_admin_void_do_the_same_thing(http, runtime):
    from engine.api.deeper_routes import apply_refund

    (code,) = runtime.meter.mint("single", 25, "pi_same")
    assert apply_refund(runtime, "pi_same") == 1
    assert runtime.meter.status(code).status == "void"


def test_in_observe_mode_the_public_door_line_says_nothing_even_at_a_closed_door(http, runtime):
    runtime.door_observe = True
    assert _public_door(http, runtime, stage=4, free_voice=False).json() == {"state": "open", "line": None}


def test_the_admin_door_route_says_whether_the_door_is_only_observing(http, runtime):
    from engine.deeper import door as door_module

    class Stub:
        def state(self):
            return door_module.DoorState(stage=2, ratio=0.8, ceiling_usd=150.0)

    runtime.door = Stub()
    runtime.door_observe = True
    assert http.get("/api/admin/deeper/door", headers=admin()).json()["door"]["observe"] is True


def test_the_door_monitor_keeps_the_days_peak_stage_ratio_and_spend(runtime):
    from engine.api.deeper_routes import _count_door
    from engine.deeper import door as door_module

    _count_door(runtime.meter, door_module.DoorState(stage=2, ratio=0.8, ceiling_usd=150.0))
    _count_door(runtime.meter, door_module.DoorState(stage=1, ratio=0.5, ceiling_usd=150.0))
    (day,) = runtime.meter.measures(1)
    assert (day["door_stage"], day["door_ratio_permille"], day["door_spend_cents"]) == (2, 800, 12000)


def test_a_runtime_built_for_real_keeps_the_doors_peaks_as_the_door_is_read(tmp_path):
    from engine.m8.log_store import UsageLogStore

    config = DeeperConfig(True, str(tmp_path / "m.db"), str(tmp_path / "c.db"))
    env = {"CIC_DEEPER_WEBHOOK_SECRET": SECRET, "CIC_API_ANON_CAP_ENABLED": "1", "CIC_DEEPER_FREE_KEY": FREE_KEY}
    rt = deeper_routes.build_runtime(config, env, usage_store=UsageLogStore(tmp_path / "usage.db"))
    try:
        assert rt.door_observe is True and rt.paid_round_cap == 40
        rt.door.state()
        (day,) = rt.meter.measures(1)
        assert (day["door_stage"], day["door_ratio_permille"], day["door_spend_cents"]) == (0, 0, 0)
    finally:
        rt.meter.close()
        rt.claims.close()


# ---- admin mint (S13) ----------------------------------------------------------

@pytest.fixture
def minting(runtime):
    runtime.ops = load_ops()
    return runtime


def mint(http, pack_usd=7, count=1, mode="separate", headers=None):
    return http.post("/api/admin/deeper/mint", json={"pack_usd": pack_usd, "count": count, "mode": mode}, headers=headers or admin())


def test_mint_needs_the_admin_credential_and_a_json_body(http, minting):
    body = {"pack_usd": 7, "count": 1, "mode": "separate"}
    assert http.post("/api/admin/deeper/mint", json=body).status_code == 404
    assert http.post("/api/admin/deeper/mint", json=body, headers=admin("wrong")).status_code == 404
    refused = http.post("/api/admin/deeper/mint", content=json.dumps(body), headers={**admin(), "content-type": "text/plain"})
    assert refused.status_code == 422
    assert minting.meter.reconciliation(1) == []


def test_mint_separate_makes_that_many_codes_of_one_pack_each(http, minting):
    made = mint(http, count=3).json()
    assert len(made["codes"]) == 3 and made["tokens_each"] == 1100
    assert made["mint_id"].startswith("admin_")
    for code in made["codes"]:
        assert minting.meter.status(code).tokens_total == 1100
        assert minting.meter.status(code).kind == "batch"


def test_mint_one_code_holds_the_whole_amount(http, minting):
    made = mint(http, pack_usd=15, count=2, mode="one_code").json()
    assert len(made["codes"]) == 1 and made["tokens_each"] == 2750 * 2
    assert minting.meter.status(made["codes"][0]).kind == "single"


def test_mint_is_never_a_payment_or_a_sale(http, minting):
    mint(http, count=2)
    day = minting.meter.reconciliation(1)[0]
    assert (day["payments_seen"], day["payments_minted"], day["codes_minted"], day["gap"]) == (0, 0, 0, 0)
    assert (day["admin_codes_minted"], day["pilot_codes_minted"]) == (2, 0)
    row = minting.meter.measures(1)[0]
    assert (row["tokens_granted"], row["tokens_sold"], row["codes_batch"]) == (2200, 0, 0)
    assert minting.meter.owed() == []


def test_mint_counts_toward_the_door_as_a_gift_of_the_packs_price(http, minting):
    mint(http, count=3)
    assert minting.meter.net_funds(7)["gift"] == 2100


def test_mint_refuses_what_is_not_a_pack_a_bad_mode_or_too_much(http, minting):
    assert mint(http, pack_usd=9).status_code == 422
    assert mint(http, mode="all").status_code == 422
    assert mint(http, count=0).status_code == 422
    assert mint(http, pack_usd=30, count=2).status_code == 422
    assert minting.meter.reconciliation(1) == []


def test_mint_stops_at_the_days_token_limit_and_resets_tomorrow(tmp_path, http, minting):
    limit = minting.ops.admin_mint_max_tokens_per_day
    per = minting.ops.admin_mint_max_tokens_per_request
    assert mint(http, pack_usd=30, count=1).status_code == 200
    assert mint(http, pack_usd=30, count=1).status_code == 200
    assert 6600 * 2 == limit and per == 6600
    refused = mint(http, count=1)
    assert refused.status_code == 429
    assert minting.meter.reconciliation(1)[0]["admin_codes_minted"] == 2
    assert minting.meter.net_funds(7)["gift"] == 6000


def test_a_mint_is_voided_by_its_id_and_its_gift_leaves_the_door(http, minting):
    made = mint(http, count=2).json()
    voided = http.post("/api/admin/deeper/void", json={"payment_id": made["mint_id"]}, headers=admin()).json()
    assert voided["voided"] == 2
    assert all(minting.meter.status(c).status == "void" for c in made["codes"])
    assert minting.meter.net_funds(7).get("gift", 0) == 0
    assert minting.meter.reconciliation(1)[0]["refunds_applied"] == 0


def test_mint_never_logs_a_code(http, minting, caplog):
    caplog.set_level(logging.DEBUG)
    made = mint(http).json()
    plain = made["codes"][0].replace(" ", "")
    assert plain not in caplog.text and made["codes"][0] not in caplog.text
    assert mint(http).headers["cache-control"] == "no-store"


def test_a_grant_id_cannot_be_used_by_a_purchase_or_the_wrong_source(minting):
    with pytest.raises(ValueError):
        minting.meter.mint("single", 100, "admin_x")
    with pytest.raises(ValueError):
        minting.meter.mint("single", 100, "pi_x", source="admin")
    with pytest.raises(ValueError):
        minting.meter.mint("single", 100, "admin_x", source="pilot")


def test_status_shows_the_live_day_read_only(http, minting):
    body = http.get("/api/admin/deeper/status", headers=admin()).json()
    assert body["paused"] is False and body["door"] is None
    assert body["free_grant"] == {"baseline_tokens": 550, "window_days": 30, "rounds_per_conversation": 3, "now_tokens": 550}
    assert [p["price_usd"] for p in body["packs"]] == [7, 15, 30]
    assert body["mint_limits"] == {"tokens_per_request": 6600, "tokens_per_day": 13200}
    assert http.get("/api/admin/deeper/status").status_code == 404


def test_an_older_reconcile_table_gains_the_grant_columns(tmp_path):
    import sqlite3
    path = str(tmp_path / "old.db")
    conn = sqlite3.connect(path)
    conn.execute(
        "CREATE TABLE reconcile (day TEXT PRIMARY KEY, payments_seen INTEGER NOT NULL DEFAULT 0, payments_minted INTEGER NOT NULL DEFAULT 0,"
        " payments_voided_first INTEGER NOT NULL DEFAULT 0, codes_minted INTEGER NOT NULL DEFAULT 0, refunds_applied INTEGER NOT NULL DEFAULT 0,"
        " partial_refunds_ignored INTEGER NOT NULL DEFAULT 0) WITHOUT ROWID"
    )
    conn.execute("INSERT INTO reconcile (day) VALUES (?)", (str(date(2026, 10, 4)),))
    conn.commit()
    conn.close()
    meter = Meter(path, clock=lambda: date(2026, 10, 5))
    meter.mint("single", 100, "admin_a", source="admin")
    days = {d["day"]: d for d in meter.reconciliation(5)}
    assert days[str(date(2026, 10, 4))]["admin_codes_minted"] == 0 and days[str(date(2026, 10, 5))]["admin_codes_minted"] == 1
    meter.close()


def test_a_voided_grant_still_counts_toward_the_days_limit(minting):
    from engine.deeper.meter import MintLimit

    meter = minting.meter
    limit = minting.ops.admin_mint_max_tokens_per_day
    meter.mint("single", limit, "admin_one", source="admin", daily_token_limit=limit)
    meter.void("admin_one")
    with pytest.raises(MintLimit):
        meter.mint("single", 1, "admin_two", source="admin", daily_token_limit=limit)


def test_the_grants_list_names_each_grant_without_its_codes(http, minting):
    made = mint(http, count=2).json()
    (row,) = http.get("/api/admin/deeper/grants", headers=admin()).json()["grants"]
    assert row["grant_id"] == made["mint_id"] and row["codes"] == 2 and row["tokens"] == 2200 and row["codes_void"] == 0
    assert not any(c.replace(" ", "") in json.dumps(row) for c in made["codes"])
    http.post("/api/admin/deeper/void", json={"payment_id": made["mint_id"]}, headers=admin())
    assert http.get("/api/admin/deeper/grants", headers=admin()).json()["grants"][0]["codes_void"] == 2
    assert http.get("/api/admin/deeper/grants").status_code == 404


# ---- pilot join (S12) ----------------------------------------------------------

def open_pilot(runtime, audience="general", **changes):
    import dataclasses

    ops = runtime.ops or load_ops()
    audiences = dict(ops.pilot_audiences)
    audiences[audience] = dataclasses.replace(audiences[audience], pilot_open=True, **changes)
    runtime.ops = dataclasses.replace(ops, pilot_audiences=audiences)
    return runtime


def join(http, ip="203.0.113.7", audience="general", **headers):
    return http.post("/api/deeper/pilot-join", json={"audience": audience}, headers={"x-forwarded-for": ip, **headers})


def test_the_shipped_pilot_is_closed_and_the_route_then_does_not_exist_to_a_visitor(http, minting):
    assert not any(a.pilot_open for a in load_ops().pilot_audiences.values())
    assert join(http).status_code == 404
    assert minting.meter.reconciliation(1) == []


def test_a_press_gives_one_ordinary_pack_code_shown_once(http, runtime):
    open_pilot(runtime)
    made = join(http)
    body = made.json()
    assert made.status_code == 200 and body["joined"] is True and body["tokens"] == 1100
    assert body["conversations"] == 10
    assert made.headers["cache-control"] == "no-store"
    assert runtime.meter.status(body["code"]).tokens_total == 1100
    assert runtime.meter.reserve(body["code"]).ok


def test_a_pilot_code_is_a_gift_not_a_payment_or_a_sale(http, runtime):
    open_pilot(runtime)
    join(http)
    day = runtime.meter.reconciliation(1)[0]
    assert (day["pilot_codes_minted"], day["admin_codes_minted"], day["payments_seen"], day["gap"]) == (1, 0, 0, 0)
    assert runtime.meter.measures(1)[0]["tokens_granted"] == 1100 and runtime.meter.measures(1)[0]["tokens_sold"] == 0
    assert runtime.meter.net_funds(7)["gift"] == 700
    assert runtime.meter.owed() == []
    assert [g["grant_id"][:6] for g in runtime.meter.grants(1)] == ["pilot_"]


def test_an_address_gets_its_few_and_then_is_told_so_while_another_still_joins(http, runtime):
    open_pilot(runtime, per_address=2)
    assert [join(http).status_code for _ in range(2)] == [200, 200]
    refused = join(http)
    assert refused.status_code == 409 and refused.json() == {"joined": False, "reason": "address_limit"}
    assert join(http, ip="203.0.113.8").status_code == 200
    assert runtime.meter.pilot_total("general") == 3


def test_the_cap_stops_the_pilot_for_everyone_and_a_refusal_takes_nothing(http, runtime):
    open_pilot(runtime, pilot_cap=2, per_address=5)
    assert join(http).status_code == 200 and join(http, ip="198.51.100.1").status_code == 200
    full = join(http, ip="198.51.100.2")
    assert full.status_code == 409 and full.json()["reason"] == "full"
    assert runtime.meter.pilot_total("general") == 2
    assert runtime.meter.reconciliation(1)[0]["pilot_codes_minted"] == 2


def test_the_pilot_ends_on_its_date(http, runtime):
    open_pilot(runtime, pilot_end_date=date(2026, 10, 5))
    assert join(http).status_code == 200
    open_pilot(runtime, pilot_end_date=date(2026, 10, 4))
    ended = join(http, ip="198.51.100.3")
    assert ended.status_code == 409 and ended.json()["reason"] == "ended"


def test_the_address_is_never_kept_in_plain_form(http, runtime):
    open_pilot(runtime)
    join(http, ip="203.0.113.99")
    rows = runtime.meter._conn.execute("SELECT key_hash FROM pilot_joined").fetchall()
    assert len(rows) == 1 and "203.0.113.99" not in rows[0][0] and len(rows[0][0]) == 32
    dump = "\n".join(runtime.meter._conn.iterdump())
    assert "203.0.113.99" not in dump


def test_a_failed_mint_keeps_the_address_count_and_the_total_unspent(runtime):
    open_pilot(runtime)
    with pytest.raises(ValueError):
        runtime.meter.join_pilot(
            "general", "203.0.113.5", 1100, "pi_wrong", open_=True, end_date=date(2026, 12, 31), cap=5, per_address=2,
        )
    assert runtime.meter.pilot_total("general") == 0
    assert runtime.meter._conn.execute("SELECT COUNT(*) FROM pilot_joined").fetchone()[0] == 0


def test_the_pilot_join_answers_the_site_and_no_other_origin(http, runtime):
    open_pilot(runtime)
    ok = join(http, ip="198.51.100.9", origin="https://site.example")
    assert ok.headers["access-control-allow-origin"] == "https://site.example"
    other = join(http, ip="198.51.100.10", origin="https://elsewhere.example")
    assert "access-control-allow-origin" not in other.headers


def test_the_status_reports_the_pilot_against_its_cap(http, runtime):
    open_pilot(runtime, pilot_cap=10)
    join(http)
    pilot = {row["audience"]: row for row in http.get("/api/admin/deeper/status", headers=admin()).json()["pilot"]}
    assert pilot["general"] == {
        "audience": "general", "open": True, "cap": 10, "given": 1,
        "end_date": runtime.ops.pilot_audiences["general"].pilot_end_date.isoformat(), "per_address": 2,
    }
    assert pilot["pastors"]["open"] is False and pilot["pastors"]["given"] == 0


def test_addresses_in_one_ipv6_block_share_a_count_and_ipv4_stays_exact(http, runtime):
    open_pilot(runtime, per_address=2, pilot_cap=50)
    block = "2001:db8:abcd:12"
    assert [join(http, ip=f"{block}::{n}").status_code for n in (1, 2)] == [200, 200]
    assert join(http, ip=f"{block}:ffff:1:2:3").json()["reason"] == "address_limit"
    assert join(http, ip="2001:db8:abcd:13::1").status_code == 200
    assert join(http, ip="203.0.113.50").status_code == 200 and join(http, ip="203.0.113.51").status_code == 200


def test_the_pilot_route_is_a_404_to_a_preflight_too_while_closed(http, runtime):
    assert http.options("/api/deeper/pilot-join", headers={"origin": "https://site.example"}).status_code == 404
    open_pilot(runtime)
    assert http.options("/api/deeper/pilot-join", headers={"origin": "https://site.example"}).status_code == 204


def test_an_address_row_is_kept_for_ninety_days_and_then_deleted(runtime):
    from engine.deeper.meter import PILOT_RETENTION_DAYS

    meter = runtime.meter
    meter.join_pilot("general", "203.0.113.5", 1100, "pilot_a", open_=True, end_date=date(2027, 1, 1), cap=5, per_address=2)
    assert PILOT_RETENTION_DAYS == 90
    first = date(2026, 10, 5)
    for days, kept in ((PILOT_RETENTION_DAYS - 1, 1), (PILOT_RETENTION_DAYS, 0)):
        meter._clock = lambda d=days: first + timedelta(days=d)
        meter.purge()
        assert meter._conn.execute("SELECT COUNT(*) FROM pilot_joined").fetchone()[0] == kept
    assert meter.pilot_total("general") == 1


def test_the_deeper_rate_limit_counts_one_ipv6_block_as_one_visitor(store, usage_store, world_loader, registry, runtime):
    http = TestClient(make_app(store, usage_store, world_loader, registry, deeper=runtime, rate_limit=True))
    statuses = [
        http.get("/api/deeper/balance", headers={"x-forwarded-for": f"2001:db8:5:6::{n}"}).status_code for n in range(1, 61)
    ]
    assert 429 not in statuses
    assert http.get("/api/deeper/balance", headers={"x-forwarded-for": "2001:db8:5:6:ffff::9"}).status_code == 429
    assert http.get("/api/deeper/balance", headers={"x-forwarded-for": "2001:db8:5:7::1"}).status_code != 429


def test_each_audience_has_its_own_switch_cap_and_count(http, runtime):
    open_pilot(runtime, "pastors", pilot_cap=1, per_address=1)
    assert join(http, audience="general").status_code == 404
    assert join(http, audience="pastors").status_code == 200
    again = join(http, audience="pastors")
    assert again.status_code == 409 and again.json()["reason"] in ("full", "address_limit")
    assert runtime.meter.pilot_total("pastors") == 1 and runtime.meter.pilot_total("general") == 0
    open_pilot(runtime, "pastors", pilot_cap=5, per_address=1)
    open_pilot(runtime, "historians", pilot_cap=5, per_address=1)
    assert join(http, ip="198.51.100.40", audience="historians").status_code == 200
    assert join(http, ip="198.51.100.40", audience="pastors").status_code == 200
    assert join(http, ip="198.51.100.40", audience="pastors").json()["reason"] == "address_limit"


def test_an_unnamed_audience_is_a_404_and_a_missing_one_is_refused(http, runtime):
    open_pilot(runtime)
    assert join(http, audience="clergy").status_code == 404
    assert join(http, audience="General").status_code == 404
    assert http.post("/api/deeper/pilot-join", headers={"x-forwarded-for": "198.51.100.41"}).status_code == 422
    assert runtime.meter.pilot_total("general") == 0


def test_the_same_address_counts_separately_under_each_audience_without_storing_the_audience_name(http, runtime):
    open_pilot(runtime, "pastors")
    open_pilot(runtime, "historians")
    join(http, ip="203.0.113.60", audience="pastors")
    join(http, ip="203.0.113.60", audience="historians")
    keys = [row[0] for row in runtime.meter._conn.execute("SELECT key_hash FROM pilot_joined")]
    assert len(keys) == 2 and len(set(keys)) == 2
    dump = "\n".join(runtime.meter._conn.iterdump())
    assert "pastors:203" not in dump and "historians:203" not in dump
