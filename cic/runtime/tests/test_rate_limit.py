"""One client must not be able to spend the pilot's budget.

Before 2026-08-17 nothing bounded request volume per client. message_cap
bounds one conversation at 40 turns; it does not stop a client opening
unlimited conversations, and session_cap is a documented no-op without
sign-in, which is optional by product decision. At measured per-turn cost
that is a five-figure month inside a day, and it lands the first time the
URL is public rather than at scale.

These tests cover the limiter's own logic. They do not spin up the app -
the endpoints are wired via Depends and FastAPI resolves Request by type,
which is checked by the import test at the bottom rather than by standing
up a server the suite has no business needing.

Pure counting - no LLM, no key, no network.
"""
import pytest
from fastapi import HTTPException

from app import rate_limit


@pytest.fixture(autouse=True)
def clean():
    rate_limit._reset_for_tests()
    yield
    rate_limit._reset_for_tests()


class FakeRequest:
    """Enough of starlette.Request for the limiter: headers and a peer."""

    def __init__(self, ip="1.2.3.4", forwarded=None):
        self.headers = {"x-forwarded-for": forwarded} if forwarded else {}
        self.client = type("C", (), {"host": ip})()


def test_allows_up_to_the_limit_then_refuses():
    req = FakeRequest()
    for _ in range(5):
        rate_limit.enforce(req, 5, 60.0, "messages")
    with pytest.raises(HTTPException) as excinfo:
        rate_limit.enforce(req, 5, 60.0, "messages")
    assert excinfo.value.status_code == 429


def test_refusal_carries_retry_after():
    """A 429 without Retry-After tells a client nothing about when to come
    back, so a polite client and an impolite one behave identically."""
    req = FakeRequest()
    rate_limit.enforce(req, 1, 60.0, "messages")
    with pytest.raises(HTTPException) as excinfo:
        rate_limit.enforce(req, 1, 60.0, "messages")
    assert excinfo.value.headers["Retry-After"] == "60"


def test_the_message_is_addressed_to_a_person():
    """The realistic cause of a real 429 here is a retry loop or an
    impatient double-click, not an attacker reading the response."""
    req = FakeRequest()
    rate_limit.enforce(req, 1, 60.0, "messages")
    with pytest.raises(HTTPException) as excinfo:
        rate_limit.enforce(req, 1, 60.0, "messages")
    detail = excinfo.value.detail.lower()
    assert "try again" in detail
    for jargon in ("rate limit", "quota", "429", "throttl"):
        assert jargon not in detail


def test_clients_are_counted_separately():
    a, b = FakeRequest(ip="10.0.0.1"), FakeRequest(ip="10.0.0.2")
    rate_limit.enforce(a, 1, 60.0, "messages")
    rate_limit.enforce(b, 1, 60.0, "messages")  # must not raise
    with pytest.raises(HTTPException):
        rate_limit.enforce(a, 1, 60.0, "messages")


def test_forwarded_header_wins_over_the_socket_peer():
    """Behind a proxy the socket peer is the proxy for every request, so
    without this the whole pilot shares one participant's budget."""
    one = FakeRequest(ip="10.0.0.9", forwarded="203.0.113.7, 10.0.0.9")
    two = FakeRequest(ip="10.0.0.9", forwarded="203.0.113.8, 10.0.0.9")
    rate_limit.enforce(one, 1, 60.0, "messages")
    rate_limit.enforce(two, 1, 60.0, "messages")  # different client
    with pytest.raises(HTTPException):
        rate_limit.enforce(one, 1, 60.0, "messages")


def test_the_window_rolls_off(monkeypatch):
    clock = {"t": 1000.0}
    monkeypatch.setattr(rate_limit.time, "monotonic", lambda: clock["t"])
    req = FakeRequest()
    rate_limit.enforce(req, 2, 60.0, "messages")
    rate_limit.enforce(req, 2, 60.0, "messages")
    with pytest.raises(HTTPException):
        rate_limit.enforce(req, 2, 60.0, "messages")
    clock["t"] += 61.0
    rate_limit.enforce(req, 2, 60.0, "messages")  # window has passed


def test_it_fails_open(monkeypatch):
    """A limiter that raises takes down the endpoint it protects, which is
    a worse outcome than the spend it was guarding against."""
    def boom(*_a, **_k):
        raise RuntimeError("counter exploded")

    monkeypatch.setattr(rate_limit, "_check", boom)
    rate_limit.enforce(FakeRequest(), 1, 60.0, "messages")  # must not raise


def test_key_table_is_bounded():
    """A spray of spoofed forwarded-for values must not grow memory without
    bound on a box with a recorded OOM history."""
    for i in range(rate_limit._MAX_KEYS + 500):
        rate_limit.enforce(FakeRequest(forwarded=f"198.51.100.{i}"), 5, 60.0, "m")
    assert len(rate_limit._hits) <= rate_limit._MAX_KEYS + 1


def test_endpoints_declare_the_dependency():
    """The limiter is only worth anything if it is actually wired on."""
    import inspect

    import app.main as main

    for fn, dep in (("start_session", "limit_session_start"),
                    ("send_message", "limit_message"),
                    ("send_message_stream", "limit_message")):
        src = inspect.getsource(getattr(main, fn))
        assert dep in src, f"{fn} is not rate limited"
