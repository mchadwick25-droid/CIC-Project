"""Per-IP rate limiting for the two spend-bearing surfaces (2026-08-28
foundation audit; Artifact-6-Operations.md §"no unauthenticated expensive
endpoints" — specified there from the start, built now). POST /api/session
is unauthenticated and creates real Bedrock spend; /message and /continue
each hold a worker thread through a full voice call. Uncapped, either one
is both an open wallet and a trivial denial-of-service (saturate the
thread pool and the whole surface — static pages included — stops
answering).

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

Client IP: first entry of X-Forwarded-For when present (Render's proxy
sets it; uvicorn runs with --proxy-headers), else the socket peer.
"""
import threading
import time
from collections import deque

from fastapi import Request
from fastapi.responses import JSONResponse

# window, max requests. Create: 6/min covers a household retrying; no
# real participant creates sessions faster. Converse: 40/min per IP is
# ~4x the fastest real table pace.
CREATE_LIMIT = (60.0, 6)
CONVERSE_LIMIT = (60.0, 40)

# Participant-facing words (inventoried for Mark's read in the decision
# log, alongside the move-3 error layer): plain, no blame, says what to do.
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
        return forwarded.split(",")[0].strip()
    return request.client.host if request.client else "unknown"


def install(app):
    """HTTP middleware: session creation and conversation traffic each get
    their own per-IP bucket; everything else (worlds list, transcript,
    health, static files) passes untouched. 429 carries Retry-After and a
    participant-appropriate detail string."""
    create_limiter = SlidingWindowLimiter(*CREATE_LIMIT)
    converse_limiter = SlidingWindowLimiter(*CONVERSE_LIMIT)

    @app.middleware("http")
    async def _rate_limit(request: Request, call_next):
        if request.method == "POST" and request.url.path.startswith("/api/session"):
            limiter = create_limiter if request.url.path == "/api/session" else converse_limiter
            if not limiter.allow(client_ip(request)):
                return JSONResponse(
                    status_code=429,
                    content={"detail": RETRY_DETAIL},
                    headers={"Retry-After": str(int(limiter.window))},
                )
        return await call_next(request)

    return app
