"""Accounts' HTTP edge: sign-in by a typed code, the cookie, step-up,
address change, export and deletion, and the proof that with the flag off none
of the routes exist."""
import dataclasses
import logging
import re

import pytest
from fastapi.testclient import TestClient

from engine.accounts.config import AccountsConfig
from engine.accounts.keys import KeyRing
from engine.accounts.service import AccountsService
from engine.accounts.store import AccountStore
from engine.accounts.tests.conftest import ADDRESS_KEY, SESSION_KEY, Clock, FakeMailer
from engine.api import accounts_routes
from engine.api.accounts_routes import AccountsConfigError, AccountsRuntime, build_runtime
from engine.api.app import create_app

H = {"x-cic-accounts": "1"}
ADDR = "ada@example.org"
NEW = "ada.new@example.org"


@pytest.fixture
def mailer():
    return FakeMailer()


@pytest.fixture
def runtime(tmp_path, mailer):
    store = AccountStore(str(tmp_path / "d.db"), str(tmp_path / "e.db"))
    service = AccountsService(store, KeyRing(ADDRESS_KEY, SESSION_KEY), mailer, clock=Clock())
    yield AccountsRuntime(service=service, miss_delay_seconds=0.0, start_floor_seconds=0.0)
    store.close()


def make_app(store, usage_store, world_loader, registry, *, accounts=None):
    return create_app(
        voice_client=object(), voice_model_id="m", safety_client=object(), safety_model_id="m",
        store=store, usage_store=usage_store, world_loader=world_loader, registry=registry,
        default_world_key="fix", accounts=accounts, rate_limit=False,
    )


@pytest.fixture
def http(store, usage_store, world_loader, registry, runtime):
    return TestClient(make_app(store, usage_store, world_loader, registry, accounts=runtime), base_url="https://testserver")


def sign_in(http, mailer, address=ADDR, birth_year=1990):
    started = http.post("/api/accounts/sign-in/start", json={"address": address}, headers=H)
    assert started.status_code == 200, started.text
    r = http.post(
        "/api/accounts/sign-in/finish",
        json={"challenge": started.json()["challenge"], "address": address, "code": mailer.last_code(address), "birth_year": birth_year},
        headers=H,
    )
    assert r.status_code == 200 and r.json()["status"] == "ok", r.text
    return r


def step_up(http, mailer, address=ADDR):
    started = http.post("/api/accounts/step-up/start", json={"address": address}, headers=H)
    assert started.status_code == 200
    r = http.post("/api/accounts/step-up/finish", json={"challenge": started.json()["challenge"], "code": mailer.last_code(address)}, headers=H)
    assert r.status_code == 200


def test_flag_off_mounts_no_accounts_route(store, usage_store, world_loader, registry):
    app = make_app(store, usage_store, world_loader, registry, accounts=None)
    assert not [p for p in (getattr(r, "path", "") for r in app.routes) if p.startswith("/api/accounts")]
    http = TestClient(app)
    for path in ("/api/accounts/me", "/api/accounts/sign-in/start", "/api/accounts/delete"):
        assert http.post(path, json={}, headers=H).status_code in (404, 405)
    assert http.get("/api/accounts/me").status_code == 404


def test_sign_in_sets_a_host_only_http_only_same_site_cookie(http, mailer):
    r = sign_in(http, mailer)
    header = r.headers["set-cookie"]
    assert header.startswith("__Host-cic_account=")
    assert "HttpOnly" in header and "Secure" in header and "SameSite=lax" in header.replace("Lax", "lax") and "Path=/" in header
    assert "Domain" not in header
    me = http.get("/api/accounts/me").json()
    assert me["signed_in"] and set(me) == {"signed_in", "refill_day", "age_band"}


def test_signed_out_me_says_so_and_a_protected_route_is_401(http):
    assert http.get("/api/accounts/me").json() == {"signed_in": False}
    assert http.post("/api/accounts/export", json={}, headers=H).status_code == 401


def test_every_post_needs_the_header_and_json_and_a_matching_origin(http, mailer):
    assert http.post("/api/accounts/sign-in/start", json={"address": ADDR}).status_code == 400
    assert http.post("/api/accounts/sign-in/start", content=b'{"address": "%s"}' % ADDR.encode(),
                     headers={**H, "content-type": "text/plain"}).status_code in (400, 422)
    ok = http.post("/api/accounts/sign-in/start", json={"address": ADDR}, headers={**H, "origin": "https://testserver"})
    assert ok.status_code == 200
    bad = http.post("/api/accounts/sign-in/start", json={"address": ADDR}, headers={**H, "origin": "https://evil.example"})
    assert bad.status_code == 403


def test_start_says_the_same_thing_for_a_known_and_an_unknown_address(http, mailer):
    sign_in(http, mailer)
    known = http.post("/api/accounts/sign-in/start", json={"address": ADDR}, headers=H)
    unknown = http.post("/api/accounts/sign-in/start", json={"address": "nobody@example.org"}, headers=H)
    assert known.status_code == unknown.status_code == 200
    assert set(known.json()) == set(unknown.json()) and known.json()["message"] == unknown.json()["message"]


def test_a_wrong_code_is_400_and_the_new_account_flow_asks_for_a_year(http, mailer):
    challenge = http.post("/api/accounts/sign-in/start", json={"address": ADDR}, headers=H).json()["challenge"]
    wrong = http.post("/api/accounts/sign-in/finish", json={"challenge": challenge, "address": ADDR, "code": "000000"}, headers=H)
    assert wrong.status_code == 400
    asked = http.post("/api/accounts/sign-in/finish", json={"challenge": challenge, "address": ADDR, "code": mailer.last_code(ADDR)}, headers=H)
    assert asked.status_code == 200 and asked.json()["status"] == "needs_birth_year"
    young = http.post("/api/accounts/sign-in/finish", json={"challenge": challenge, "address": ADDR, "code": mailer.last_code(ADDR), "birth_year": 2020}, headers=H)
    assert young.json()["status"] == "under_age" and "set-cookie" not in young.headers


def test_sign_out_clears_the_session(http, mailer):
    sign_in(http, mailer)
    assert http.post("/api/accounts/sign-out", json={}, headers=H).status_code == 200
    assert http.get("/api/accounts/me").json() == {"signed_in": False}


def test_sensitive_actions_need_step_up_then_work(http, mailer):
    sign_in(http, mailer)
    assert http.post("/api/accounts/export", json={}, headers=H).status_code == 400
    step_up(http, mailer)
    export = http.post("/api/accounts/export", json={}, headers=H)
    assert export.status_code == 200 and set(export.json()["account"]) == {"day_created", "refill_day", "week_last_used", "age_band"}


def test_address_change_over_http_signs_out_other_devices(http, mailer):
    sign_in(http, mailer)
    other = TestClient(http.app, base_url="https://testserver")
    challenge = other.post("/api/accounts/sign-in/start", json={"address": ADDR}, headers=H).json()["challenge"]
    other.post("/api/accounts/sign-in/finish", json={"challenge": challenge, "address": ADDR, "code": mailer.last_code(ADDR)}, headers=H)
    step_up(http, mailer)
    started = http.post("/api/accounts/address/start", json={"new_address": NEW}, headers=H)
    assert started.status_code == 200
    r = http.post("/api/accounts/address/finish", json={"challenge": started.json()["challenge"], "code": mailer.last_code(NEW)}, headers=H)
    assert r.status_code == 200
    assert other.get("/api/accounts/me").json() == {"signed_in": False}
    assert http.get("/api/accounts/me").json()["signed_in"]


def test_delete_ends_the_account_and_the_cookie(http, mailer):
    sign_in(http, mailer)
    step_up(http, mailer)
    assert http.post("/api/accounts/delete", json={}, headers=H).status_code == 200
    assert http.get("/api/accounts/me").json() == {"signed_in": False}


def test_limits_answer_429_and_a_paused_sign_in_503(http, mailer):
    statuses = [http.post("/api/accounts/sign-in/start", json={"address": ADDR}, headers=H).status_code for _ in range(4)]
    assert statuses == [200, 200, 200, 429]


def test_no_log_line_holds_an_address_a_code_or_a_cookie(http, mailer, caplog):
    with caplog.at_level(logging.DEBUG):
        r = sign_in(http, mailer)
        step_up(http, mailer)
        http.post("/api/accounts/sign-in/finish", json={"challenge": "nope", "address": "x@example.org", "code": "000000"}, headers=H)
    text = caplog.text
    assert not re.search(r"[\w.+-]+@[\w-]+\.[\w.]+", text)
    for _, code in mailer.sent:
        assert code not in text
    assert r.cookies.get("__Host-cic_account") not in text


def test_the_access_log_filter_drops_accounts_lines_only():
    f = accounts_routes.AccessLogFilter()
    def line(path):
        return logging.LogRecord("uvicorn.access", logging.INFO, "", 0, '%s - "%s %s HTTP/1.1" %d', ("1.2.3.4", "POST", path, 200), None)
    assert not f.filter(line("/api/accounts/sign-in/start"))
    assert f.filter(line("/api/worlds"))


def test_start_up_refuses_with_no_key_a_short_key_or_no_mail(tmp_path, mailer):
    config = AccountsConfig.from_env(str(tmp_path))
    env = {"CIC_ACCOUNTS_KEY": ADDRESS_KEY, "CIC_ACCOUNTS_SESSION_KEY": SESSION_KEY}
    with pytest.raises(AccountsConfigError):
        build_runtime(config, {}, mailer)
    with pytest.raises(AccountsConfigError):
        build_runtime(config, {**env, "CIC_ACCOUNTS_KEY": "short"}, mailer)
    with pytest.raises(AccountsConfigError):
        build_runtime(config, {**env, "CIC_ACCOUNTS_SESSION_KEY": ADDRESS_KEY}, mailer)
    with pytest.raises(AccountsConfigError, match="mail provider"):
        build_runtime(config, env, None)
    runtime = build_runtime(config, env, mailer)
    runtime.service.store.close()


def test_the_flag_off_default_config_is_off(tmp_path, monkeypatch):
    monkeypatch.delenv("CIC_ACCOUNTS_ENABLED", raising=False)
    assert AccountsConfig.from_env(str(tmp_path)).enabled is False


def test_sign_out_deletes_the_cookie_with_the_attributes_a_browser_needs(http, mailer):
    sign_in(http, mailer)
    header = http.post("/api/accounts/sign-out", json={}, headers=H).headers["set-cookie"]
    assert header.startswith("__Host-cic_account=") and "Secure" in header and "Path=/" in header
    assert "Max-Age=0" in header or "expires=" in header.lower()


def test_an_origin_with_another_scheme_is_refused(http):
    bad = http.post("/api/accounts/sign-in/start", json={"address": ADDR}, headers={**H, "origin": "http://testserver"})
    assert bad.status_code == 403


def test_a_paused_sign_in_is_503(http, runtime, mailer):
    runtime.service.limits = type(runtime.service.limits)(sends_global_hour=1)
    first = http.post("/api/accounts/sign-in/start", json={"address": ADDR}, headers=H)
    second = http.post("/api/accounts/sign-in/start", json={"address": NEW}, headers={**H})
    assert first.status_code == 200 and second.status_code == 503


def test_address_change_replies_and_limits_are_the_same_for_a_taken_and_a_free_address(http, mailer, runtime):
    runtime.service.limits = dataclasses.replace(runtime.service.limits, account_actions_15min=200)
    sign_in(http, mailer, "bob@example.org")
    other = TestClient(http.app, base_url="https://testserver")
    sign_in(other, mailer, ADDR, 1990)
    step_up(other, mailer, ADDR)

    def probe(address, forwarded):
        out = []
        for _ in range(9):
            r = other.post("/api/accounts/address/start", json={"new_address": address}, headers={**H, "x-forwarded-for": forwarded})
            out.append((r.status_code, tuple(sorted(r.json())), r.json().get("message")))
        return out

    taken = probe("bob@example.org", "192.0.2.63")
    free = probe("later@example.org", "192.0.2.64")
    assert taken == free and taken[0][0] == 200 and taken[-1][0] == 429


def test_a_queued_send_never_blocks_the_reply_and_logs_no_address(caplog):
    import threading

    from engine.api.accounts_routes import QueuedMailer

    release = threading.Event()
    done = threading.Event()

    class Slow:
        def send_code(self, address, code):
            release.wait(2)
            done.set()
            raise RuntimeError("provider down")

    queued = QueuedMailer(Slow(), workers=1)
    with caplog.at_level(logging.DEBUG):
        queued.send_code("ada@example.org", "123456")  # returns at once, though the provider is slow
        release.set()
        assert done.wait(3)
        queued._pool.shutdown(wait=True)
    assert not re.search(r"[\w.+-]+@[\w-]+\.[\w.]+", caplog.text) and "123456" not in caplog.text
    assert "could not be sent" in caplog.text
