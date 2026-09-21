"""The per-IP rate limiter (engine/api/ratelimit.py) - unit tests for the
sliding window, plus the app-level pin that a rate_limit=True app actually
limits and a rate_limit-default app doesn't (the fake-backed test suites
depend on that default staying off)."""
from engine.api.ratelimit import ADMIN_LIMIT, CREATE_LIMIT, RETRY_DETAIL, SlidingWindowLimiter


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
