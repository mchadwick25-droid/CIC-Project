"""Per-visitor daily cap on session creation and conversation turns
(Tech-Readiness P1-Security item 3 — OWASP LLM Top 10 "unbounded
consumption"). Feature-flagged OFF by default (CIC_API_ANON_CAP_ENABLED) —
this module is inert dead code in every deployment until Mark turns it on,
and the cap mechanism/numbers below are the PROPOSED default, not a decided
one; see Ministry/Operations/Audits/Tech-Readiness-2026-09/P1-Security/
Report.md for the 2-3 options this was chosen from and why.

Why a second, per-visitor mechanism on top of engine/api/ratelimit.py's
per-IP sliding window: that limiter already bounds *burst* rate (6
creates/min, 40 converse/min per IP) but has no DAILY ceiling — a single
IP can create 6 sessions every minute, all day, and the limiter never
stops it. This module adds the missing daily bound, scoped to a visitor
rather than an IP so it doesn't collapse every participant behind a
shared/NAT'd address into one bucket the way a pure-IP daily limit would.

Mechanism: a random, server-issued, HMAC-signed opaque token in an
HttpOnly cookie. No accounts, no email, no name, no device fingerprint —
the token is a bare random id, unlinkable to a real identity, and this
module never persists it anywhere but the signature verifies it wasn't
handed back tampered with. Cookie only (no frontend change needed):
cic-poc/frontend is same-origin with engine/api (render.yaml's own
"ONE service" design), so the browser sends it automatically.

In-memory, per-instance, day-bucketed — the same architectural precedent
ratelimit.py already established and justified (one instance serves all
traffic today; the SQLite session store already pins this service there).
A restart resets every visitor's count to zero; that's an acceptable
false-negative for a soft abuse deterrent, not a hard security boundary,
and matches the existing limiter's own accepted tradeoff.
"""
import hmac
import secrets
import threading
import time
from dataclasses import dataclass
from datetime import datetime, timezone

from fastapi import Request
from fastapi.responses import JSONResponse

from engine.api.ratelimit import client_ip

COOKIE_NAME = "cic_visitor"
_TOKEN_BYTES = 18  # 144 bits, base64url-encoded by secrets.token_urlsafe
_SEPARATOR = "."

# PROPOSED defaults (Option A in the report) — deliberately conservative:
# a real participant's own honest use (per Artifact-6-Operations.md's
# measured floor) fits comfortably inside these; see the report for the
# 2-3 option comparison these numbers came from.
DEFAULT_DAILY_SESSION_LIMIT = 5
DEFAULT_DAILY_TURN_LIMIT = 150

CAP_DETAIL = "You've reached today's limit for new conversations - please come back tomorrow, or reach out if this doesn't seem right."
TURN_CAP_DETAIL = "You've reached today's limit for messages - please come back tomorrow, or reach out if this doesn't seem right."


def _today() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def _sign(visitor_id: str, secret: str) -> str:
    return hmac.new(secret.encode(), visitor_id.encode(), "sha256").hexdigest()[:32]


def issue_token(secret: str) -> str:
    visitor_id = secrets.token_urlsafe(_TOKEN_BYTES)
    return f"{visitor_id}{_SEPARATOR}{_sign(visitor_id, secret)}"


def verify_token(token: str, secret: str) -> str | None:
    """Returns the visitor_id if the token's signature is valid, else None
    (missing cookie, corrupted value, or signed with a since-rotated
    secret all fall through to None - the caller mints a fresh one, never
    trusts an unverified id as someone's existing daily bucket)."""
    if not token or _SEPARATOR not in token:
        return None
    visitor_id, _, signature = token.partition(_SEPARATOR)
    if not visitor_id or not signature:
        return None
    if not hmac.compare_digest(_sign(visitor_id, secret), signature):
        return None
    return visitor_id


@dataclass
class _DailyCounts:
    day: str
    sessions: int = 0
    turns: int = 0


class DailyVisitorLimiter:
    """One counter pair per visitor id, reset whenever the wall-clock day
    (UTC) rolls over - checked lazily on access rather than swept, the
    same "cheap enough, no background sweep needed" choice ratelimit.py
    makes for its own map growth."""

    def __init__(self, daily_session_limit: int, daily_turn_limit: int):
        self.daily_session_limit = daily_session_limit
        self.daily_turn_limit = daily_turn_limit
        self._counts: dict[str, _DailyCounts] = {}
        self._lock = threading.Lock()

    def _bucket(self, visitor_id: str) -> _DailyCounts:
        today = _today()
        bucket = self._counts.get(visitor_id)
        if bucket is None or bucket.day != today:
            bucket = _DailyCounts(day=today)
            self._counts[visitor_id] = bucket
            # Same opportunistic trim ratelimit.py uses - only matters
            # under sustained real traffic, cheap when it doesn't.
            if len(self._counts) > 50_000:
                stale = [k for k, v in self._counts.items() if v.day != today]
                for k in stale:
                    del self._counts[k]
        return bucket

    def allow_session(self, visitor_id: str) -> bool:
        with self._lock:
            bucket = self._bucket(visitor_id)
            if bucket.sessions >= self.daily_session_limit:
                return False
            bucket.sessions += 1
            return True

    def allow_turn(self, visitor_id: str) -> bool:
        with self._lock:
            bucket = self._bucket(visitor_id)
            if bucket.turns >= self.daily_turn_limit:
                return False
            bucket.turns += 1
            return True


def install(app, *, secret: str, daily_session_limit: int = DEFAULT_DAILY_SESSION_LIMIT, daily_turn_limit: int = DEFAULT_DAILY_TURN_LIMIT):
    """HTTP middleware, only ever installed when CIC_API_ANON_CAP_ENABLED
    is on (see engine.api.app._build_real_app). Runs after ratelimit's own
    middleware in the stack (installed after it in app.py) - the cheaper,
    IP-only, no-cookie-read check stays the first line.

    Falls back to client_ip(request) as the bucket key on a request with no
    valid cookie: the first request from a genuinely new visitor (or one
    who cleared cookies) is still counted against SOMETHING before its own
    token is minted and returned, rather than getting one free unbounded
    request. The Set-Cookie response still issues a fresh per-visitor token
    for every subsequent request either way."""
    limiter = DailyVisitorLimiter(daily_session_limit, daily_turn_limit)

    @app.middleware("http")
    async def _anon_cap(request: Request, call_next):
        is_create = request.method == "POST" and request.url.path == "/api/session"
        is_turn = request.method == "POST" and request.url.path.startswith("/api/session/") and (
            request.url.path.endswith("/message") or request.url.path.endswith("/continue")
        )
        if not (is_create or is_turn):
            return await call_next(request)

        raw_cookie = request.cookies.get(COOKIE_NAME)
        visitor_id = verify_token(raw_cookie, secret) if raw_cookie else None
        needs_new_token = visitor_id is None
        bucket_key = visitor_id or f"ip:{client_ip(request)}"

        allowed = limiter.allow_session(bucket_key) if is_create else limiter.allow_turn(bucket_key)
        if not allowed:
            response = JSONResponse(status_code=429, content={"detail": CAP_DETAIL if is_create else TURN_CAP_DETAIL})
        else:
            response = await call_next(request)

        if needs_new_token:
            token = issue_token(secret)
            response.set_cookie(
                COOKIE_NAME, token, max_age=60 * 60 * 24 * 2, httponly=True, samesite="lax", secure=True, path="/api",
            )
        return response

    return app
