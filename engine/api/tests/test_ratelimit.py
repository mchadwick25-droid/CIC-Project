"""The per-IP rate limiter (engine/api/ratelimit.py) - unit tests for the
sliding window, plus the app-level pin that a rate_limit=True app actually
limits and a rate_limit-default app doesn't (the fake-backed test suites
depend on that default staying off)."""
from starlette.requests import Request

from engine.api.ratelimit import ADMIN_LIMIT, CONVERSE_LIMIT, CREATE_LIMIT, RETRY_DETAIL, SlidingWindowLimiter, client_ip


def test_allows_up_to_the_limit_then_refuses():
    limiter = SlidingWindowLimiter(60.0, 3)
    assert all(limiter.allow("ip", now=1.0 + i) for i in range(3))
    assert not limiter.allow("ip", now=5.0)


def test_the_window_slides_old_hits_expire():
    limiter = SlidingWindowLimiter(10.0, 2)
    assert limiter.allow("ip", now=0.0)
    assert limiter.allow("ip", now=1.0)
    assert not limiter.allow("ip", now=5.0)
    # first hit (t=0) has left the 10s window by t=10.5
    assert limiter.allow("ip", now=10.5)


def test_ips_are_independent():
    limiter = SlidingWindowLimiter(60.0, 1)
    assert limiter.allow("a", now=0.0)
    assert limiter.allow("b", now=0.0)
    assert not limiter.allow("a", now=1.0)


def _request_with_xff(header_value: str | None) -> Request:
    headers = [(b"x-forwarded-for", header_value.encode())] if header_value else []
    scope = {"type": "http", "headers": headers, "client": ("203.0.113.9", 12345)}
    return Request(scope)


def test_client_ip_trusts_the_last_xff_entry_not_the_first():
    """2026-09-21, closing adversarial review: a standard reverse proxy
    (Render's edge, the only thing that can reach this container) APPENDS
    the peer it actually observed onto X-Forwarded-For rather than
    replacing it - so the FIRST entry is attacker-supplied and trusting it
    let anyone bypass every limiter in this module with one request
    header. The last entry is the one Render's own proxy appended."""
    assert client_ip(_request_with_xff("1.2.3.4, 10.0.0.5")) == "10.0.0.5"
    assert client_ip(_request_with_xff("attacker-spoofed, 9.9.9.9, 10.0.0.5")) == "10.0.0.5"
    assert client_ip(_request_with_xff("203.0.113.50")) == "203.0.113.50"
    assert client_ip(_request_with_xff(None)) == "203.0.113.9"  # falls back to the socket peer


def _app(*, rate_limit, store, usage_store, world_loader, registry):
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
        rate_limit=rate_limit,
    )
    return TestClient(app)


def test_rate_limited_app_returns_429_with_participant_words_past_the_create_limit(store, usage_store, world_loader, registry):
    client = _app(rate_limit=True, store=store, usage_store=usage_store, world_loader=world_loader, registry=registry)
    _, max_creates = CREATE_LIMIT
    codes = [client.post("/api/session", json={"world_key": "fix"}).status_code for _ in range(max_creates + 1)]
    assert codes[-1] == 429
    response = client.post("/api/session", json={"world_key": "fix"})
    assert response.json()["detail"] == RETRY_DETAIL
    assert "Retry-After" in response.headers


def test_default_app_is_not_rate_limited(store, usage_store, world_loader, registry):
    client = _app(rate_limit=False, store=store, usage_store=usage_store, world_loader=world_loader, registry=registry)
    _, max_creates = CREATE_LIMIT
    codes = [client.post("/api/session", json={"world_key": "fix"}).status_code for _ in range(max_creates + 2)]
    assert 429 not in codes


def test_transcript_and_round_close_reasons_gets_are_rate_limited(store, usage_store, world_loader, registry):
    """2026-09-21, closing adversarial review: these two GETs guess a
    session CODE via the exact same _authenticate() 401 as the message/
    continue POSTs, but were never in this limiter's own path match -
    an unlimited-rate credential-guessing surface. No real session is
    needed for this test: the limiter is HTTP middleware and runs before
    routing/auth either way, so a nonexistent session id still exercises
    it (and still gets the normal 401 up to the point the limiter itself
    starts returning 429 instead)."""
    client = _app(rate_limit=True, store=store, usage_store=usage_store, world_loader=world_loader, registry=registry)
    _, max_converse = CONVERSE_LIMIT
    codes = [client.get("/api/session/nonexistent-id/transcript").status_code for _ in range(max_converse + 1)]
    assert codes[:-1] == [401] * max_converse
    assert codes[-1] == 429


def test_admin_route_is_rate_limited_independent_of_a_configured_token(store, usage_store, world_loader, registry):
    """No admin_token configured (so every attempt 404s) still exercises
    the limiter - brute-force throttling shouldn't depend on there being a
    real token to guess against yet."""
    from fastapi.testclient import TestClient

    from engine.api.app import create_app
    from engine.api.tests.conftest import FakeBedrockClient, reader_response, safety_response

    client = FakeBedrockClient(safety_response=safety_response("NO_SIGNAL"), reader_response=reader_response())
    app = create_app(
        voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m", store=store,
        usage_store=usage_store, world_loader=world_loader, registry=registry, default_world_key="fix", rate_limit=True,
    )
    http = TestClient(app)
    _, max_attempts = ADMIN_LIMIT
    codes = [http.get("/api/admin/pilot-summary", headers={"Authorization": "Bearer guess"}).status_code for _ in range(max_attempts + 1)]
    assert codes[:-1] == [404] * max_attempts
    assert codes[-1] == 429
