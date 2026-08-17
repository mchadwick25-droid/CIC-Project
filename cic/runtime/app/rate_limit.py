"""Per-client request limiting on the two endpoints that spend money.

WHY THIS EXISTS. Until 2026-08-17 nothing in the runtime bounded request
volume from any single client. The only backstop was message_cap.py, which
caps ONE conversation at 40 solo turns - it does not stop a client opening
unlimited conversations. session_cap.py is documented as "a permanent
no-op" without sign-in, and sign-in is optional by product decision. So
the ceiling on spend from one script was, in practice, the API key's own
rate limit.

At the measured per-turn cost that is a five-figure month inside a day.
This is not a scale concern; it is the first day the URL is public.

WHAT IT IS, AND WHAT IT IS NOT. A fixed-window counter held in this
process, keyed by client IP. Chosen over a token bucket because the window
boundary is the honest unit here - the question is "how many turns has
this client asked for in the last minute", not "how bursty were they".
Chosen over slowapi/redis because the service runs one worker
(Dockerfile's --workers 1, for a per-process transformer-model reason that
is not going away soon), so a per-process limiter is exactly as effective
as a shared one and adds no dependency and no network hop.

THE LIMIT THAT COMES WITH THAT: this does not survive horizontal scaling.
The moment a second instance exists, each gets its own counters and the
effective limit doubles per instance. That is the same boundary the event
store already has (state is process-local, the Supabase mirror is
write-only), so the fix is the same fix, and this should move to shared
state at the same time rather than being independently rebuilt.

Fails OPEN. A limiter that 500s is worse than one that lets a request
through - and an exception here would take down the endpoint it protects.
"""
from __future__ import annotations

import threading
import time
from collections import deque

from fastapi import HTTPException, Request

from app.config import settings

_lock = threading.Lock()
# key -> deque of request timestamps inside the current window
_hits: dict[str, deque] = {}
# Hard cap on tracked keys, so a spray of spoofed IPs cannot grow this
# without bound. Evicting the coldest key is safe: the evicted client
# starts a fresh window, which is the same thing a window rollover does.
_MAX_KEYS = 20_000


def _client_key(request: Request) -> str:
    """Best available client identity.

    X-Forwarded-For first, because the service sits behind a proxy and the
    socket peer is that proxy for every request. Trusting the header is
    spoofable, but the alternative - limiting everyone as one client -
    would rate-limit the whole pilot to one participant's budget. The
    _MAX_KEYS eviction above is what bounds the cost of that spoofability.
    """
    forwarded = request.headers.get("x-forwarded-for", "")
    if forwarded:
        return forwarded.split(",")[0].strip()
    client = request.client
    return client.host if client else "unknown"


def _check(key: str, limit: int, window_seconds: float) -> bool:
    """True if this request is inside the limit. Records it when it is."""
    now = time.monotonic()
    cutoff = now - window_seconds
    with _lock:
        if len(_hits) > _MAX_KEYS:
            coldest = min(_hits, key=lambda k: _hits[k][-1] if _hits[k] else 0.0)
            _hits.pop(coldest, None)
        bucket = _hits.setdefault(key, deque())
        while bucket and bucket[0] < cutoff:
            bucket.popleft()
        if len(bucket) >= limit:
            return False
        bucket.append(now)
        return True


def enforce(request: Request, limit: int, window_seconds: float, what: str) -> None:
    """Raise 429 when the caller is over the limit. Never raises anything else."""
    try:
        allowed = _check(_client_key(request), limit, window_seconds)
    except Exception:  # noqa: BLE001 - fail open, see module docstring
        return
    if not allowed:
        retry_after = max(1, int(window_seconds))
        raise HTTPException(
            status_code=429,
            # Addressed to a participant who hit this by accident, not to a
            # script - the honest reading of a real 429 here is a browser
            # retry loop or an impatient double-click, and the message
            # should make sense to the person on the other end of that.
            detail=f"That's more {what} than we can take just now. "
                   f"Give it a moment and try again.",
            headers={"Retry-After": str(retry_after)},
        )


def limit_message(request: Request) -> None:
    enforce(request, settings.rate_limit_messages_per_minute, 60.0, "messages")


def limit_session_start(request: Request) -> None:
    enforce(request, settings.rate_limit_sessions_per_hour, 3600.0, "new conversations")


def _reset_for_tests() -> None:
    with _lock:
        _hits.clear()
