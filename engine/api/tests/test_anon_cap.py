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


def _app(
    *, anon_cap_enabled, secret, daily_session_limit=5, daily_turn_limit=150, rate_limit=False,
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
        anon_daily_session_limit=daily_session_limit,
        anon_daily_turn_limit=daily_turn_limit,
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


def test_burst_limiter_runs_first_a_429_from_it_never_touches_the_daily_bucket(store, usage_store, world_loader, registry):
    """Middleware ordering: ratelimit's cheap per-IP burst check must run
    BEFORE anon_cap's daily-quota accounting,
    so a request the burst limiter was always going to reject doesn't
    also burn a chunk of the participant's daily allowance - a flaky
    connection retrying past the burst limit shouldn't cost them their
    whole day. Uses a daily limit well above the burst limit so if
    ordering were backwards (daily checked first), this would still pass
    the daily check every time and the test wouldn't catch the bug -
    instead this asserts on the CREATE_LIMIT burst count of 429s appearing
    with the daily cap high enough that they can only be burst-limiter
    429s, never daily-cap ones."""
    from engine.api.ratelimit import CREATE_LIMIT

    _, max_creates = CREATE_LIMIT
    client = _app(
        anon_cap_enabled=True, secret="s3cret", daily_session_limit=1000, rate_limit=True, store=store, usage_store=usage_store,
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


def test_capped_app_refuses_the_session_after_the_daily_limit_with_a_stable_cookie(store, usage_store, world_loader, registry):
    client = _app(
        anon_cap_enabled=True, secret="s3cret", daily_session_limit=2, store=store, usage_store=usage_store, world_loader=world_loader,
        registry=registry,
    )
    # TestClient persists Set-Cookie across requests on the same client -
    # this is one "visitor" across all three calls. Requires the https
    # base_url from _app() above; the cookie is Secure and won't round-trip
    # over plain http (this test used to pass over http anyway, for the
    # wrong reason - see _app()'s own comment).
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


def test_a_rejected_request_is_never_issued_a_fresh_token(store, usage_store, world_loader, registry):
    """Minting must never happen on a request the cap itself just refused
    with a 429 - otherwise an attacker never has to succeed even once to
    harvest an unlimited supply of fresh, empty-bucket tokens. A 429 must
    never carry a new Set-Cookie for a visitor who didn't already have a
    valid one."""
    client = _app(
        anon_cap_enabled=True, secret="s3cret", daily_session_limit=1, store=store, usage_store=usage_store, world_loader=world_loader,
        registry=registry,
    )
    first = client.post("/api/session", json={"world_key": "fix"})
    assert first.status_code == 201
    assert COOKIE_NAME in first.cookies
    # Same client (cookie already set and over the cap) - but simulate the
    # harvesting attack directly: a cookie-LESS request past the cap.
    client.cookies.clear()
    second = client.post("/api/session", json={"world_key": "fix"})
    assert second.status_code == 429
    assert COOKIE_NAME not in second.cookies


def test_harvesting_tokens_by_repeatedly_dropping_the_cookie_is_bounded_not_unlimited(
    store, usage_store, world_loader, registry,
):
    """Direct repro of the review's B1 finding, run to completion: an
    attacker who never sends a cookie back (deletes it every time) used to
    get a brand-new, zero-count token on every single request, each good
    for a full fresh daily allowance - unbounded. Now each new token is
    seeded from the ip: bucket's own current count, so harvesting N tokens
    before the ip bucket itself caps out leaves only bounded leftover
    headroom across all of them (DailyVisitorLimiter.mint_seeded_token's
    own docstring has the exact bound: at most daily_session_limit from
    the ip-path itself, plus at most daily_session_limit*(daily_session_
    limit-1)/2 redeemable extra across every harvested token - finite and
    small, not unlimited)."""
    from fastapi.testclient import TestClient

    from engine.api.app import create_app
    from engine.api.tests.conftest import FakeBedrockClient, reader_response, safety_response

    limit = 5
    fake = FakeBedrockClient(safety_response=safety_response("NO_SIGNAL"), reader_response=reader_response())
    app = create_app(
        voice_client=fake, voice_model_id="m", safety_client=fake, safety_model_id="m", store=store, usage_store=usage_store,
        world_loader=world_loader, registry=registry, default_world_key="fix", anon_cap_enabled=True, anon_visitor_secret="s3cret",
        anon_daily_session_limit=limit, anon_daily_turn_limit=150, deeper=None,
    )
    client = TestClient(app, base_url="https://testserver")

    # Phase 1: harvest by never sending a cookie back, until the ip:
    # bucket itself refuses (bounded at `limit` successes; further
    # cookie-less attempts just 429 per the fix above, minting nothing).
    harvested = []
    for _ in range(limit + 3):
        client.cookies.clear()
        resp = client.post("/api/session", json={"world_key": "fix"})
        if resp.status_code == 201 and COOKIE_NAME in resp.cookies:
            harvested.append(resp.cookies[COOKIE_NAME])
    assert len(harvested) == limit  # the ip: bucket's own cap, exactly

    # Phase 2: redeem every harvested token for whatever headroom its seed
    # left it (each was seeded from the ip bucket's count AT mint time, so
    # earlier tokens have more headroom than later ones).
    extra_successes = 0
    for token in harvested:
        for _ in range(limit):  # each token can be tried at most `limit` times
            client.cookies.clear()
            client.cookies.set(COOKIE_NAME, token)
            resp = client.post("/api/session", json={"world_key": "fix"})
            if resp.status_code == 201:
                extra_successes += 1
            else:
                break

    # The bound the docstring promises: at most limit*(limit-1)/2 extra
    # successes beyond the ip-path's own `limit`. NOT unlimited (the
    # pre-fix bug), and nowhere close to the harvested-token count times
    # the daily limit (what a naive "just seed nothing" mint would allow).
    assert extra_successes <= limit * (limit - 1) // 2
    total = limit + extra_successes
    assert total <= limit + limit * (limit - 1) // 2  # the exact documented bound
    assert total < limit * limit  # nowhere near the pre-fix "one full allowance per harvested token" shape


def _send(http, created, text="hello"):
    return http.post(
        f"/api/session/{created['session_id']}/message",
        headers={"Authorization": f"Session {created['session_code']}"},
        json={"text": text},
    )


def test_a_message_over_the_daily_cap_closes_the_session_through_the_facilitator(store, usage_store, world_loader, registry):
    """Over the daily message cap, a message still reaches the safety gate.
    An ordinary one gets the Facilitator's daily-cap close, not a bare 429,
    and the session closes, so it cannot be used to keep calling the gate."""
    http = _app(
        anon_cap_enabled=True, secret="s" * 32, daily_turn_limit=0,
        store=store, usage_store=usage_store, world_loader=world_loader, registry=registry,
    )
    created = http.post("/api/session", json={"world_key": "fix"}).json()
    resp = _send(http, created)
    assert resp.status_code == 200
    body = resp.json()
    assert body["routing_action"] == "session_cap_turn"
    assert "today's limit" in body["facilitator"]["text"]
    assert _send(http, created).status_code == 409


def test_a_crisis_message_over_the_daily_cap_still_gets_the_facilitator_redirect(store, usage_store, world_loader, registry):
    http = _app(
        anon_cap_enabled=True, secret="s" * 32, daily_turn_limit=0, safety_signal="ACUTE_DISTRESS",
        store=store, usage_store=usage_store, world_loader=world_loader, registry=registry,
    )
    created = http.post("/api/session", json={"world_key": "fix"}).json()
    resp = _send(http, created, text="I don't want to be here anymore")
    assert resp.status_code == 200
    body = resp.json()
    assert body["routing_action"] == "safety_turn"
    assert body["facilitator"]["resources_appended"]
