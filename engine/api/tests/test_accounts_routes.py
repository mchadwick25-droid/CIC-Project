"""Accounts' HTTP edge: sign-in by a typed code, the cookie, step-up,
address change, export and deletion, and the proof that with the flag off none
of the routes exist."""
import dataclasses
import json
import logging
import re

import pytest
from fastapi.testclient import TestClient

from engine.accounts.config import AccountsConfig
from engine.accounts.contacts import ContactStore
from engine.accounts.keys import KeyRing
from engine.accounts.service import AccountsService
from engine.accounts.store import AccountStore
from engine.accounts.tests.conftest import ADDRESS_KEY, SESSION_KEY, Clock, FakeMailer, FakeVerifier
from engine.api import accounts_routes
from engine.api.contact_cipher import ContactCipher
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
    contacts = ContactStore(str(tmp_path / "c.db"), ContactCipher("c" * 40))
    service = AccountsService(store, KeyRing(ADDRESS_KEY, SESSION_KEY), mailer, clock=Clock(), contacts=contacts)
    yield AccountsRuntime(service=service, miss_delay_seconds=0.0, start_floor_seconds=0.0)
    store.close()
    contacts.close()


def make_app(store, usage_store, world_loader, registry, *, accounts=None):
    return create_app(
        voice_client=object(), voice_model_id="m", safety_client=object(), safety_model_id="m",
        store=store, usage_store=usage_store, world_loader=world_loader, registry=registry,
        default_world_key="fix", accounts=accounts, rate_limit=False,
    )


@pytest.fixture
def http(store, usage_store, world_loader, registry, runtime):
    return TestClient(make_app(store, usage_store, world_loader, registry, accounts=runtime), base_url="https://testserver")


def sign_in(http, mailer, address=ADDR):
    started = http.post("/api/accounts/sign-in/start", json={"address": address}, headers=H)
    assert started.status_code == 200, started.text
    r = http.post(
        "/api/accounts/sign-in/finish",
        json={"challenge": started.json()["challenge"], "address": address, "code": mailer.last_code(address), "over_18": True},
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
    assert me["signed_in"] and set(me) == {"signed_in", "refill_day", "age_band", "sign_in_methods", "has_recovery_code", "recovery_pending", "address"}


def test_me_shows_the_signed_in_person_their_own_address_and_is_never_cached(http, mailer):
    assert "address" not in http.get("/api/accounts/me").json()
    sign_in(http, mailer)
    reply = http.get("/api/accounts/me")
    assert reply.json()["address"] == ADDR
    assert reply.headers["cache-control"] == "no-store"
    other = TestClient(http.app, base_url="https://testserver")
    sign_in(other, mailer, "grace@example.org")
    assert other.get("/api/accounts/me").json()["address"] == "grace@example.org"
    assert http.get("/api/accounts/me").json()["address"] == ADDR


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


def test_a_wrong_code_is_400_and_the_new_account_flow_asks_for_the_age_click(http, mailer, tmp_path):
    challenge = http.post("/api/accounts/sign-in/start", json={"address": ADDR}, headers=H).json()["challenge"]
    wrong = http.post("/api/accounts/sign-in/finish", json={"challenge": challenge, "address": ADDR, "code": "000000"}, headers=H)
    assert wrong.status_code == 400
    body = {"challenge": challenge, "address": ADDR, "code": mailer.last_code(ADDR)}
    asked = http.post("/api/accounts/sign-in/finish", json=body, headers=H)
    assert asked.status_code == 200 and asked.json()["status"] == "needs_age_answer" and "set-cookie" not in asked.headers
    declined = http.post("/api/accounts/sign-in/finish", json={**body, "over_18": False}, headers=H)
    assert declined.status_code == 200 and declined.json()["status"] == "not_adult" and "set-cookie" not in declined.headers
    assert "not available yet" in declined.json()["message"]
    assert http.get("/api/accounts/me").json() == {"signed_in": False}
    typed = http.post("/api/accounts/sign-in/finish", json={**body, "over_18": "yes"}, headers=H)
    assert typed.status_code == 422
    sent_date = http.post("/api/accounts/sign-in/finish", json={**body, "over_18": True, "birth_date": "1990-05-15"}, headers=H)
    assert sent_date.status_code == 200 and sent_date.json()["status"] == "ok"
    for name in ("d.db", "e.db"):
        assert b"1990" not in (tmp_path / name).read_bytes()


def test_sign_out_clears_the_session(http, mailer):
    sign_in(http, mailer)
    assert http.post("/api/accounts/sign-out", json={}, headers=H).status_code == 200
    assert http.get("/api/accounts/me").json() == {"signed_in": False}


def test_sensitive_actions_need_step_up_then_work(http, mailer):
    sign_in(http, mailer)
    assert http.post("/api/accounts/export", json={}, headers=H).status_code == 400
    step_up(http, mailer)
    export = http.post("/api/accounts/export", json={}, headers=H)
    assert export.status_code == 200 and set(export.json()["account"]) == {"day_created", "refill_day", "week_last_used", "age_band", "sign_in_methods"}


def test_address_change_over_http_signs_out_other_devices(http, mailer):
    sign_in(http, mailer)
    other = TestClient(http.app, base_url="https://testserver")
    challenge = other.post("/api/accounts/sign-in/start", json={"address": ADDR}, headers=H).json()["challenge"]
    other.post("/api/accounts/sign-in/finish", json={"challenge": challenge, "address": ADDR, "code": mailer.last_code(ADDR)}, headers=H)
    step_up(http, mailer)
    started = http.post("/api/accounts/address/start", json={"new_address": NEW}, headers=H)
    assert started.status_code == 200
    r = http.post("/api/accounts/address/finish", json={"challenge": started.json()["challenge"], "code": mailer.last_code(NEW), "new_address": NEW}, headers=H)
    assert r.status_code == 200
    assert other.get("/api/accounts/me").json() == {"signed_in": False}
    assert http.get("/api/accounts/me").json()["signed_in"]


def test_delete_ends_the_account_and_the_cookie(http, mailer):
    sign_in(http, mailer)
    step_up(http, mailer)
    assert http.post("/api/accounts/delete", json={}, headers=H).status_code == 200
    assert http.get("/api/accounts/me").json() == {"signed_in": False}


def test_delete_closes_the_account_for_ninety_days_and_a_sign_in_can_re_open_it(http, mailer, runtime):
    sign_in(http, mailer)
    step_up(http, mailer)
    deleted = http.post("/api/accounts/delete", json={}, headers=H)
    assert deleted.status_code == 200
    erase_on = deleted.json()["erase_on"]
    assert erase_on == (runtime.service.today() + __import__("datetime").timedelta(days=90)).isoformat()
    started = http.post("/api/accounts/sign-in/start", json={"address": ADDR}, headers=H).json()
    body = {"challenge": started["challenge"], "address": ADDR, "code": mailer.last_code(ADDR)}
    closed = http.post("/api/accounts/sign-in/finish", json=body, headers=H)
    assert closed.status_code == 200 and closed.json()["status"] == "account_closed"
    assert closed.json()["erase_on"] == erase_on and erase_on in closed.json()["message"]
    assert "set-cookie" not in closed.headers
    assert http.get("/api/accounts/me").json() == {"signed_in": False}
    opened = http.post("/api/accounts/sign-in/finish", json={**body, "reopen": True}, headers=H)
    assert opened.status_code == 200 and opened.json()["status"] == "ok" and opened.json()["new_account"] is False
    assert http.get("/api/accounts/me").json()["signed_in"] is True


def test_reopen_must_be_a_true_boolean(http, mailer):
    sign_in(http, mailer)
    step_up(http, mailer)
    http.post("/api/accounts/delete", json={}, headers=H)
    started = http.post("/api/accounts/sign-in/start", json={"address": ADDR}, headers=H).json()
    body = {"challenge": started["challenge"], "address": ADDR, "code": mailer.last_code(ADDR), "reopen": "yes"}
    assert http.post("/api/accounts/sign-in/finish", json=body, headers=H).status_code == 422


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
    contact_key, shelf_key, backup_key = "c" * 40, "h" * 40, "b" * 40
    env = {"CIC_ACCOUNTS_KEY": ADDRESS_KEY, "CIC_ACCOUNTS_SESSION_KEY": SESSION_KEY, "CIC_ACCOUNTS_CONTACT_KEY": contact_key,
           "CIC_ACCOUNTS_SHELF_KEY": shelf_key, "CIC_ACCOUNTS_BACKUP_KEY": backup_key}
    with pytest.raises(AccountsConfigError):
        build_runtime(config, {}, mailer)
    for bad in ("", "short", ADDRESS_KEY, SESSION_KEY, contact_key, shelf_key):
        with pytest.raises(AccountsConfigError, match="backup key"):
            build_runtime(config, {**env, "CIC_ACCOUNTS_BACKUP_KEY": bad}, mailer)
    for bad in ("", "short", ADDRESS_KEY, SESSION_KEY):
        with pytest.raises(AccountsConfigError, match="contact key"):
            build_runtime(config, {**env, "CIC_ACCOUNTS_CONTACT_KEY": bad}, mailer)
    for bad in ("", "short", ADDRESS_KEY, SESSION_KEY, contact_key):
        with pytest.raises(AccountsConfigError, match="shelf key"):
            build_runtime(config, {**env, "CIC_ACCOUNTS_SHELF_KEY": bad}, mailer)
    with pytest.raises(AccountsConfigError):
        build_runtime(config, {**env, "CIC_ACCOUNTS_KEY": "short"}, mailer)
    with pytest.raises(AccountsConfigError):
        build_runtime(config, {**env, "CIC_ACCOUNTS_SESSION_KEY": ADDRESS_KEY}, mailer)
    with pytest.raises(AccountsConfigError, match="mail provider"):
        build_runtime(config, env, None)
    runtime = build_runtime(config, env, mailer)
    assert runtime.backup_sealer is not None and runtime.backup_sealer.key_id == "b1"
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
    sign_in(other, mailer, ADDR)
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


def provider_finish(http, subject="g-ada", provider="google", **extra):
    nonce = http.post("/api/accounts/provider/start", json={}, headers=H).json()["nonce"]
    body = {"provider": provider, "id_token": f"{subject}|{nonce}", "nonce": nonce, **extra}
    return http.post("/api/accounts/provider/finish", json=body, headers=H), nonce, body


def test_a_provider_sign_in_asks_the_age_click_then_sets_the_cookie(http, runtime):
    runtime.service.verifier = FakeVerifier()
    asked, nonce, body = provider_finish(http)
    assert asked.status_code == 200 and asked.json()["status"] == "needs_age_answer" and "set-cookie" not in asked.headers
    declined = http.post("/api/accounts/provider/finish", json={**body, "over_18": False}, headers=H)
    assert declined.json()["status"] == "not_adult" and "set-cookie" not in declined.headers
    typed = http.post("/api/accounts/provider/finish", json={**body, "over_18": "yes"}, headers=H)
    assert typed.status_code == 422
    done = http.post("/api/accounts/provider/finish", json={**body, "over_18": True}, headers=H)
    assert done.status_code == 200 and done.json() == {"status": "ok", "new_account": True, "coupons": []}
    assert "__Host-cic_account" in done.headers["set-cookie"] and "HttpOnly" in done.headers["set-cookie"]
    me = http.get("/api/accounts/me").json()
    assert me["signed_in"] and me["sign_in_methods"] == ["google"]


def test_a_provider_that_is_not_set_up_is_404_and_a_bad_token_is_400(http, runtime):
    nonce = http.post("/api/accounts/provider/start", json={}, headers=H).json()["nonce"]
    body = {"provider": "google", "id_token": f"g|{nonce}", "nonce": nonce, "over_18": True}
    assert http.post("/api/accounts/provider/finish", json=body, headers=H).status_code == 404
    runtime.service.verifier = FakeVerifier()
    bad = http.post("/api/accounts/provider/finish", json={**body, "id_token": "g|other"}, headers=H)
    assert bad.status_code == 400 and "set-cookie" not in bad.headers


def test_the_provider_routes_need_the_header_and_json(http, runtime):
    runtime.service.verifier = FakeVerifier()
    full = {"provider": "google", "id_token": "g|n", "nonce": "n"}
    bodies = {"start": {}, "finish": full, "link": full, "unlink": {"provider": "google"}}
    for path, body in bodies.items():
        url = f"/api/accounts/provider/{path}"
        assert http.post(url, json=body).status_code == 400
        assert http.post(url, content=json.dumps(body).encode(), headers={"x-cic-accounts": "1"}).status_code in (400, 422)
    assert http.post("/api/accounts/step-up/provider", json=full).status_code == 400


def test_step_up_link_and_unlink_by_provider_over_http(http, mailer, runtime):
    runtime.service.verifier = FakeVerifier()
    sign_in(http, mailer)
    step_up(http, mailer)
    nonce = http.post("/api/accounts/provider/start", json={}, headers=H).json()["nonce"]
    link = http.post("/api/accounts/provider/link", json={"provider": "apple", "id_token": f"a-ada|{nonce}", "nonce": nonce}, headers=H)
    assert link.status_code == 200
    assert http.get("/api/accounts/me").json()["sign_in_methods"] == ["address", "apple"]
    unlink = http.post("/api/accounts/provider/unlink", json={"provider": "apple"}, headers=H)
    assert unlink.status_code == 200
    assert http.get("/api/accounts/me").json()["sign_in_methods"] == ["address"]
    last = http.post("/api/accounts/provider/unlink", json={"provider": "apple"}, headers=H)
    assert last.status_code == 400


def test_a_provider_token_is_in_no_log_line(http, runtime, caplog):
    runtime.service.verifier = FakeVerifier()
    caplog.set_level(logging.DEBUG)
    _, nonce, body = provider_finish(http, subject="g-secret-subject", over_18=True)
    assert "g-secret-subject" not in caplog.text and nonce not in caplog.text


def test_recovery_over_http_from_code_to_cancel(http, mailer, runtime):
    sign_in(http, mailer)
    step_up(http, mailer)
    code = http.post("/api/accounts/recovery/code", json={}, headers=H).json()["recovery_code"]
    thief = TestClient(http.app, base_url="https://testserver")
    started = thief.post("/api/accounts/recovery/start", json={"recovery_code": code, "new_address": NEW}, headers=H)
    assert started.status_code == 200 and started.json()["status"] == "sent"
    wrong = thief.post("/api/accounts/recovery/start", json={"recovery_code": "nope", "new_address": "x@example.org"}, headers=H)
    assert wrong.status_code == 200 and set(wrong.json()) == set(started.json())
    body = {"challenge": started.json()["challenge"], "code": mailer.last_code(NEW), "new_address": NEW}
    assert thief.post("/api/accounts/recovery/finish", json={**body, "code": "000000"}, headers=H).status_code == 400
    done = thief.post("/api/accounts/recovery/finish", json=body, headers=H)
    assert done.status_code == 200 and done.json()["recovery_code"] and done.json()["effective_on"]
    assert "set-cookie" not in done.headers
    me = http.get("/api/accounts/me").json()
    assert me["recovery_pending"] == {"effective_on": done.json()["effective_on"]}
    cancel = mailer.notices[-1][2]["cancel_code"]
    assert thief.post("/api/accounts/recovery/cancel", json={"address": ADDR, "cancel_code": "nope"}, headers=H).status_code == 400
    assert thief.post("/api/accounts/recovery/cancel", json={"address": ADDR, "cancel_code": cancel}, headers=H).status_code == 200
    assert http.get("/api/accounts/me").json()["recovery_pending"] is None


def test_the_recovery_routes_need_the_header(http):
    for path, body in (("code", {}), ("start", {"recovery_code": "a", "new_address": NEW}),
                       ("finish", {"challenge": "a", "code": "1", "new_address": NEW}),
                       ("cancel", {"address": ADDR, "cancel_code": "a"}), ("cancel-signed-in", {})):
        assert http.post(f"/api/accounts/recovery/{path}", json=body).status_code == 400


def test_a_signed_in_owner_cancels_over_http(http, mailer):
    sign_in(http, mailer)
    step_up(http, mailer)
    code = http.post("/api/accounts/recovery/code", json={}, headers=H).json()["recovery_code"]
    thief = TestClient(http.app, base_url="https://testserver")
    started = thief.post("/api/accounts/recovery/start", json={"recovery_code": code, "new_address": NEW}, headers=H).json()
    thief.post("/api/accounts/recovery/finish", json={"challenge": started["challenge"], "code": mailer.last_code(NEW), "new_address": NEW}, headers=H)
    assert http.post("/api/accounts/recovery/cancel-signed-in", json={}, headers=H).status_code == 200
    assert http.post("/api/accounts/recovery/cancel-signed-in", json={}, headers=H).status_code == 400


def test_the_providers_route_lists_only_the_providers_that_are_turned_on(http, runtime):
    from engine.api.provider_tokens import ProviderVerifier
    runtime.service.verifier = None
    assert http.get("/api/accounts/providers").json() == {"providers": {}}
    runtime.service.verifier = ProviderVerifier({"google": "g-client", "apple": ""})
    assert http.get("/api/accounts/providers").json() == {"providers": {"google": "g-client"}}


def test_a_refused_provider_token_does_not_talk_about_a_code(http, runtime):
    runtime.service.verifier = FakeVerifier()
    nonce = http.post("/api/accounts/provider/start", json={}, headers=H).json()["nonce"]
    refused = http.post("/api/accounts/provider/finish", json={"provider": "google", "id_token": "bad", "nonce": nonce, "over_18": True}, headers=H)
    assert refused.status_code == 400 and "code" not in refused.json()["detail"].lower()
