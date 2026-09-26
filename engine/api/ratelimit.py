"""Per-IP rate limiting for the two spend-bearing surfaces
(Artifact-6-Operations.md §"no unauthenticated expensive endpoints").
POST /api/session is unauthenticated and creates real Bedrock spend;
/message and /continue each hold a worker thread through a full voice
call. Uncapped, either one is both an open wallet and a trivial
denial-of-service (saturate the thread pool and the whole surface —
static pages included — stops answering).

A third bucket covers /api/admin/* - not spend-bearing, but its Bearer
token (engine.api.app._authenticate_admin) has no anti-automation control
otherwise: hmac.compare_digest is constant-time against a KNOWN token,
but nothing stops an attacker from simply trying tokens at unlimited
rate. Same mechanism, different reason (ASVS V2.2.1, not spend).

In-process and dependency-free on purpose: one instance serves all
traffic today (the SQLite session store already pins us there), so a
shared limiter store would be scaffolding for a topology that doesn't
exist. When the Postgres move unlocks multiple instances, this limiter's
per-instance counts become per-instance limits — still a real bound,
revisited in that same move.

Sliding window, two buckets per client IP: session creation (expensive,
rare for a real participant) and conversation traffic (a table round is
1 message + up to 3 continues; the conversation limit is set so no real
participant pace can hit it — the measured floor is one voice turn per
10-30s, so even a fast table sitting stays under half the bound).

Client IP: LAST entry of X-Forwarded-For when present (Render's proxy
sets it; uvicorn runs with --proxy-headers), else the socket peer. Last,
not first: a standard reverse proxy APPENDS the peer it actually observed
onto whatever X-Forwarded-For it received, rather than replacing the
header - so the first entry is exactly the part of the header a client
controls directly, and taking it would let anyone bypass every limiter in
this file with one request header (`X-Forwarded-For: 1.2.3.4`), no
exploit tooling required. With exactly one trusted proxy hop in front of
this service
(Render's edge - the only thing that can reach this container, per the
Dockerfile's own comment on --forwarded-allow-ips='*'), the entry THAT
proxy appended - the last one - is the only one this process didn't just
receive verbatim from the request itself.
"""
import threading
import time
from collections import deque

from fastapi import Request
from fastapi.responses import JSONResponse

# window, max requests. Create: 6/min covers a household retrying; no
# real participant creates sessions faster. Converse: 40/min per IP is
# ~4x the fastest real table pace. Admin: 10/min per IP - generous for
# the one legitimate operator polling pilot-summary, hostile to guessing
# a token by brute force (a real token is a long random string; even an
# attacker with no rate limit at all would need an astronomical number
# of attempts, but zero throttle meant zero cost to trying anyway).
CREATE_LIMIT = (60.0, 6)
CONVERSE_LIMIT = (60.0, 40)
ADMIN_LIMIT = (60.0, 10)

# Participant-facing words (full inventory in the decision log, alongside
# the move-3 error layer): plain, no blame, says what to do.
RETRY_DETAIL = "The room is full for a moment - please wait a little and try again."


class SlidingWindowLimiter:
    def __init__(self, window_seconds: float, max_requests: int):
        self.window = window_seconds
        self.max_requests = max_requests
        self._hits: dict[str, deque] = {}
        self._lock = threading.Lock()

    def allow(self, key: str, now: float | None = None) -> bool:
        now = time.monotonic() if now is None else now
        with self._lock:
            q = self._hits.setdefault(key, deque())
            cutoff = now - self.window
            while q and q[0] <= cutoff:
                q.popleft()
            if len(q) >= self.max_requests:
                return False
            q.append(now)
            # Keep the map from growing one entry per IP forever: drop
            # empty queues opportunistically (any request from a quiet IP
            # re-creates its queue for pennies).
            if len(self._hits) > 10_000:
                for k in [k for k, v in self._hits.items() if not v]:
                    del self._hits[k]
            return True


def client_ip(request: Request) -> str:
    forwarded = request.headers.get("x-forwarded-for")
    if forwarded:
        return forwarded.split(",")[-1].strip()
    return request.client.host if request.client else "unknown"


def install(app):
    """HTTP middleware: session creation, conversation traffic (including
    the two per-session GET reads, not just the two message POSTs - see
    below), and admin requests each get their own per-IP bucket;
    everything else (worlds list, health, static files) passes untouched.
    429 carries Retry-After and a participant-appropriate detail
    string."""
    create_limiter = SlidingWindowLimiter(*CREATE_LIMIT)
    converse_limiter = SlidingWindowLimiter(*CONVERSE_LIMIT)
    admin_limiter = SlidingWindowLimiter(*ADMIN_LIMIT)

    @app.middleware("http")
    async def _rate_limit(request: Request, call_next):
        path = request.url.path
        if request.method == "POST" and path == "/api/session":
            limiter = create_limiter
        elif path.startswith("/api/session/") and (
            (request.method == "POST" and (path.endswith("/message") or path.endswith("/continue")))
            # GET /transcript and /round-close-reasons both guess a
            # session CODE via the same _authenticate() 401 as the two
            # POSTs above (engine/api/app.py) - the same unlimited-rate
            # credential-guessing surface as the admin bucket above, just
            # the participant-facing instance of it rather than the
            # operator-facing one (ASVS V2.2.1).
            or (request.method == "GET" and (path.endswith("/transcript") or path.endswith("/round-close-reasons")))
        ):
            limiter = converse_limiter
        elif path.startswith("/api/admin"):
            limiter = admin_limiter
        else:
            return await call_next(request)
        if not limiter.allow(client_ip(request)):
            return JSONResponse(
                status_code=429,
                content={"detail": RETRY_DETAIL},
                headers={"Retry-After": str(int(limiter.window))},
            )
        return await call_next(request)

    return app
