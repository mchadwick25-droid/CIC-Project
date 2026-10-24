"""The visitor cookie (Tech-Readiness P1-Security item 3).
Feature-flagged via CIC_API_ANON_CAP_ENABLED - the code default
stays off (a fresh/local/test app opts in explicitly), but both real
deployments turn it on (render.yaml), and the engine refuses to start with
the free allowance on and this flag off, because the free allowance
(engine.deeper.free) is keyed on the id issued here.

There is no daily count. A visitor's free allowance is a monthly window of
tokens (engine.deeper.free); nothing here limits conversations or messages
by day. Burst rate stays with engine/api/ratelimit.py's per-IP sliding
window, and spend with the group codes (engine.deeper).

Mechanism: a random, server-issued, HMAC-signed opaque token in an
HttpOnly cookie. No accounts, no email, no name, no device fingerprint -
the token is a bare random id, unlinkable to a real identity, and the
signature verifies it wasn't handed back tampered with. Cookie only (no
frontend change needed): cic-poc/frontend is same-origin with engine/api
(render.yaml's own "ONE service" design), so the browser sends it
automatically.

install() hands the verified-or-freshly-minted id to the request as
`request.state.visitor_id`, BEFORE the route handler runs, so
engine.api.wiring.create_session can write it onto that session's own
session_started event (engine/m4/entrance.py) - the one place a session's
identity is actually persisted - and admission can key the free allowance
on it. That event write is what makes the id durable across restarts and
usable for the usage dashboard's unique-visitor count; this module itself
keeps no record of who visited.
"""
import hmac
import secrets

from fastapi import Request

COOKIE_NAME = "cic_visitor"
_TOKEN_BYTES = 18  # 144 bits, base64url-encoded by secrets.token_urlsafe
_SEPARATOR = "."

# The cookie's own lifetime. 400 days is the practical ceiling, not a round-number guess:
# Chrome (and Chromium-based browsers) caps any Set-Cookie Max-Age at 400
# days and silently clamps a longer one, so asking for more would just be
# asking for the same 400 with extra steps. Needs to be long because the
# usage dashboard's unique-visitor count depends on this cookie surviving
# from one visit to the next across a pilot that may run for months.
VISITOR_COOKIE_MAX_AGE_SECONDS = 60 * 60 * 24 * 400


def _sign(visitor_id: str, secret: str) -> str:
    return hmac.new(secret.encode(), visitor_id.encode(), "sha256").hexdigest()[:32]


def issue_token(secret: str) -> str:
    visitor_id = secrets.token_urlsafe(_TOKEN_BYTES)
    return f"{visitor_id}{_SEPARATOR}{_sign(visitor_id, secret)}"


def verify_token(token: str, secret: str) -> str | None:
    """Returns the visitor_id if the token's signature is valid, else None
    (missing cookie, corrupted value, or signed with a since-rotated
    secret all fall through to None - the caller mints a fresh one, never
    trusts an unverified id as someone's existing visitor)."""
    if not token or _SEPARATOR not in token:
        return None
    visitor_id, _, signature = token.partition(_SEPARATOR)
    if not visitor_id or not signature:
        return None
    if not hmac.compare_digest(_sign(visitor_id, secret), signature):
        return None
    return visitor_id


def install(app, *, secret: str):
    """HTTP middleware, only ever installed when CIC_API_ANON_CAP_ENABLED
    is on (see engine.api.app._build_real_app). A valid cookie names the
    visitor on a session create or a message. A create with no valid cookie
    mints a fresh token and sets it on the response. A message with no valid
    cookie mints nothing, so tokens cannot be collected by sending messages
    that never open anything; admission keys that request on the address.

    The mint happens BEFORE call_next so request.state.visitor_id is set
    before the route handler runs and create_session_endpoint can read it."""

    @app.middleware("http")
    async def _visitor_cookie(request: Request, call_next):
        is_create = request.method == "POST" and request.url.path == "/api/session"
        is_turn = request.method == "POST" and request.url.path.startswith("/api/session/") and (
            request.url.path.endswith("/message") or request.url.path.endswith("/continue")
        )
        # A sign-in that finishes reads the visitor id, and mints nothing, so a new account can
        # begin with what is left of its browser's free window.
        reads_only = request.method == "POST" and request.url.path.startswith("/api/accounts/") and request.url.path.endswith("/finish")
        # The page asks what is left of the free window before any reply; that reads the cookie and mints nothing.
        reads_free = request.method == "GET" and request.url.path == "/api/deeper/free"
        if not (is_create or is_turn or reads_only or reads_free):
            return await call_next(request)

        raw_cookie = request.cookies.get(COOKIE_NAME)
        visitor_id = verify_token(raw_cookie, secret) if raw_cookie else None
        new_token: str | None = None
        if visitor_id is None and is_create:
            new_token = issue_token(secret)
            visitor_id = new_token.split(_SEPARATOR, 1)[0]
        request.state.visitor_id = visitor_id

        response = await call_next(request)
        if new_token is not None:
            response.set_cookie(
                COOKIE_NAME, new_token, max_age=VISITOR_COOKIE_MAX_AGE_SECONDS, httponly=True, samesite="lax", secure=True, path="/api",
            )
        return response

    return app
