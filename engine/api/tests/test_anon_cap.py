"""engine/api/anon_cap.py - the visitor cookie. Unit tests for the token
primitives, plus the app-level pins that an app built with
anon_cap_enabled=True issues and honours the cookie and sets no daily limit
on conversations or messages."""
import pytest

from engine.api.anon_cap import COOKIE_NAME, issue_token, verify_token


def test_issued_token_verifies_with_the_right_secret():
    token = issue_token("s3cret")
    assert verify_token(token, "s3cret") is not None


def test_token_signed_with_a_different_secret_fails():
    token = issue_token("s3cret")
    assert verify_token(token, "different") is None


def test_missing_or_malformed_token_fails_closed():
    assert verify_token(None, "s3cret") is None
    assert verify_token("", "s3cret") is None
    assert verify_token("not-a-real-token", "s3cret") is None


def test_two_issued_tokens_are_different_visitors():
    a = verify_token(issue_token("s3cret"), "s3cret")
    b = verify_token(issue_token("s3cret"), "s3cret")
    assert a != b


def _app(
    *, anon_cap_enabled, secret, rate_limit=False,
    store, usage_store, world_loader, registry, safety_signal="NO_SIGNAL",
):
    from fastapi.testclient import TestClient

    from engine.api.app import create_app
    from engine.api.tests.conftest import FakeBedrockClient, reader_response, safety_response

    acute = {"acute_level": "a2", "risk_subject": "self"} if safety_signal == "ACUTE_DISTRESS" else {}
    client = FakeBedrockClient(safety_response=safety_response(safety_signal, **acute), reader_response=reader_response())
    app = create_app(
        voice_client=client,
        voice_model_id="m",
        safety_client=client,
        safety_model_id="m",
        store=store,
        usage_store=usage_store,
        world_loader=world_loader,
        registry=registry,
        default_world_key="fix",
        rate_limit=rate_limit,
        anon_cap_enabled=anon_cap_enabled,
        anon_visitor_secret=secret,
        deeper=None,
    )
    # base_url must be https: the visitor cookie is Secure (correctly, per
    # this service always sitting behind Render's TLS termination), and
    # httpx's cookie jar - matching every real browser - never returns a
    # Secure cookie over a plain-http connection. Building this TestClient
    # against the default http://testserver silently never round-trips
    # the cookie at all, which is exactly the gap that let the real
    # minting bug (see the harvest-then-redeem tests below) ship with a
    # suite that was "green" - every request landed in the ip: fallback
    # bucket instead of ever exercising the cookie path.
    return TestClient(app, base_url="https://testserver")


def test_the_burst_limiter_still_bounds_session_creation(store, usage_store, world_loader, registry):
    """The per-minute burst limit is the only rate bound left on creating
    sessions, and it runs ahead of the cookie middleware."""
    from engine.api.ratelimit import CREATE_LIMIT

    _, max_creates = CREATE_LIMIT
    client = _app(
        anon_cap_enabled=True, secret="s3cret", rate_limit=True, store=store, usage_store=usage_store,
        world_loader=world_loader, registry=registry,
    )
    codes = [client.post("/api/session", json={"world_key": "fix"}).status_code for _ in range(max_creates + 3)]
    assert codes.count(429) >= 3
    assert codes[:max_creates] == [201] * max_creates


def test_default_app_is_not_capped(store, usage_store, world_loader, registry):
    client = _app(anon_cap_enabled=False, secret=None, store=store, usage_store=usage_store, world_loader=world_loader, registry=registry)
    codes = [client.post("/api/session", json={"world_key": "fix"}).status_code for _ in range(10)]
    assert 429 not in codes


def test_enabling_without_a_secret_is_refused_loudly(store, usage_store, world_loader, registry):
    from engine.api.app import MissingAnonCapSecret

    with pytest.raises(MissingAnonCapSecret):
        _app(anon_cap_enabled=True, secret=None, store=store, usage_store=usage_store, world_loader=world_loader, registry=registry)


def test_capped_app_issues_a_visitor_cookie_on_first_request(store, usage_store, world_loader, registry):
    client = _app(
        anon_cap_enabled=True, secret="s3cret", store=store, usage_store=usage_store, world_loader=world_loader, registry=registry,
    )
    response = client.post("/api/session", json={"world_key": "fix"})
    assert response.status_code == 201
    assert COOKIE_NAME in response.cookies


def test_a_visitor_can_open_more_conversations_than_the_old_daily_limit_with_one_cookie(store, usage_store, world_loader, registry):
    client = _app(
        anon_cap_enabled=True, secret="s3cret", store=store, usage_store=usage_store, world_loader=world_loader, registry=registry,
    )
    # TestClient persists Set-Cookie across requests: one visitor across all calls (the https
    # base_url in _app() is what lets the Secure cookie round-trip).
    codes = [client.post("/api/session", json={"world_key": "fix"}).status_code for _ in range(8)]
    assert codes == [201] * 8


def test_a_returning_visitor_keeps_the_same_cookie(store, usage_store, world_loader, registry):
    client = _app(
        anon_cap_enabled=True, secret="s3cret", store=store, usage_store=usage_store, world_loader=world_loader, registry=registry,
    )
    first = client.post("/api/session", json={"world_key": "fix"})
    second = client.post("/api/session", json={"world_key": "fix"})
    assert COOKIE_NAME in first.cookies
    assert COOKIE_NAME not in second.cookies


def test_a_forged_or_tampered_cookie_is_treated_as_no_cookie_at_all(store, usage_store, world_loader, registry):
    client = _app(
        anon_cap_enabled=True, secret="s3cret", store=store, usage_store=usage_store, world_loader=world_loader, registry=registry,
    )
    forged = issue_token("wrong-secret")
    response = client.post("/api/session", json={"world_key": "fix"}, cookies={COOKIE_NAME: forged})
    # Refused signature -> treated as absent -> a fresh, correctly-signed token is minted.
    assert response.status_code == 201
    assert verify_token(response.cookies[COOKIE_NAME], "s3cret") is not None


def _send(http, created, text="hello"):
    return http.post(
        f"/api/session/{created['session_id']}/message",
        headers={"Authorization": f"Session {created['session_code']}"},
        json={"text": text},
    )


def test_a_crisis_message_still_gets_the_facilitator_redirect_with_the_cookie_on(store, usage_store, world_loader, registry):
    http = _app(
        anon_cap_enabled=True, secret="s" * 32, safety_signal="ACUTE_DISTRESS",
        store=store, usage_store=usage_store, world_loader=world_loader, registry=registry,
    )
    created = http.post("/api/session", json={"world_key": "fix"}).json()
    resp = _send(http, created, text="I don't want to be here anymore")
    assert resp.status_code == 200
    body = resp.json()
    assert body["routing_action"] == "safety_turn"
    assert body["facilitator"]["resources_appended"]


def test_a_message_request_without_a_cookie_never_mints_a_token(store, usage_store, world_loader, registry):
    client = _app(
        anon_cap_enabled=True, secret="s3cret", store=store, usage_store=usage_store, world_loader=world_loader, registry=registry,
    )
    created = client.post("/api/session", json={"world_key": "fix"}).json()
    for _ in range(3):
        client.cookies.clear()
        response = _send(client, created)
        assert COOKIE_NAME not in response.cookies
