"""engine/api/anon_cap.py - the per-visitor daily cap (Tech-Readiness
P1-Security item 3). Unit tests for the token/limiter primitives, plus the
app-level pin that an app built with anon_cap_enabled=True actually caps,
and a default app doesn't - same shape as test_ratelimit.py."""
import pytest

from engine.api.anon_cap import COOKIE_NAME, DailyVisitorLimiter, issue_token, verify_token


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


def test_limiter_allows_up_to_the_daily_session_limit_then_refuses():
    limiter = DailyVisitorLimiter(daily_session_limit=3, daily_turn_limit=100)
    assert all(limiter.allow_session("v1") for _ in range(3))
    assert not limiter.allow_session("v1")


def test_limiter_allows_up_to_the_daily_turn_limit_then_refuses():
    limiter = DailyVisitorLimiter(daily_session_limit=100, daily_turn_limit=2)
    assert limiter.allow_turn("v1")
    assert limiter.allow_turn("v1")
    assert not limiter.allow_turn("v1")


def test_limiter_visitors_are_independent():
    limiter = DailyVisitorLimiter(daily_session_limit=1, daily_turn_limit=100)
    assert limiter.allow_session("v1")
    assert limiter.allow_session("v2")
    assert not limiter.allow_session("v1")


def _app(*, anon_cap_enabled, secret, daily_session_limit=5, daily_turn_limit=150, store, usage_store, world_loader, registry):
    from fastapi.testclient import TestClient

    from engine.api.app import create_app
    from engine.api.tests.conftest import FakeBedrockClient, reader_response, safety_response

    client = FakeBedrockClient(safety_response=safety_response("NO_SIGNAL"), reader_response=reader_response())
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
        anon_cap_enabled=anon_cap_enabled,
        anon_visitor_secret=secret,
        anon_daily_session_limit=daily_session_limit,
        anon_daily_turn_limit=daily_turn_limit,
    )
    return TestClient(app)


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


def test_capped_app_refuses_the_session_after_the_daily_limit_with_a_stable_cookie(store, usage_store, world_loader, registry):
    client = _app(
        anon_cap_enabled=True, secret="s3cret", daily_session_limit=2, store=store, usage_store=usage_store, world_loader=world_loader,
        registry=registry,
    )
    # TestClient persists Set-Cookie across requests on the same client -
    # this is one "visitor" across all three calls.
    codes = [client.post("/api/session", json={"world_key": "fix"}).status_code for _ in range(3)]
    assert codes == [201, 201, 429]


def test_two_visitors_with_distinct_tokens_are_independent(store, usage_store, world_loader, registry):
    # Two already-issued, valid tokens (as if two different browsers each
    # already hold their own cookie) must not share a bucket - each gets
    # its own daily allowance regardless of hitting the same test host/IP.
    client = _app(
        anon_cap_enabled=True, secret="s3cret", daily_session_limit=1, store=store, usage_store=usage_store, world_loader=world_loader,
        registry=registry,
    )
    token_a, token_b = issue_token("s3cret"), issue_token("s3cret")
    assert client.post("/api/session", json={"world_key": "fix"}, cookies={COOKIE_NAME: token_a}).status_code == 201
    assert client.post("/api/session", json={"world_key": "fix"}, cookies={COOKIE_NAME: token_a}).status_code == 429
    assert client.post("/api/session", json={"world_key": "fix"}, cookies={COOKIE_NAME: token_b}).status_code == 201


def test_a_forged_or_tampered_cookie_is_treated_as_no_cookie_at_all(store, usage_store, world_loader, registry):
    client = _app(
        anon_cap_enabled=True, secret="s3cret", store=store, usage_store=usage_store, world_loader=world_loader, registry=registry,
    )
    forged = issue_token("wrong-secret")
    response = client.post("/api/session", json={"world_key": "fix"}, cookies={COOKIE_NAME: forged})
    # Refused signature -> treated as absent -> falls back to the IP
    # bucket and gets a fresh, correctly-signed token minted for it.
    assert response.status_code == 201
    assert verify_token(response.cookies[COOKIE_NAME], "s3cret") is not None
