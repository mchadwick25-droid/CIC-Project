"""
Supabase-backed participant identity.

Replaces the pilot's old ?code=... URL-param scheme (see the superseded
app/session_cap.py, which this module's companion rework now backs with
these same tables) with a real signed-in user, verified from the
Authorization: Bearer <token> header the frontend attaches after a
Supabase magic-link sign-in.

Off by default: if settings.supabase_url/supabase_service_key aren't set
(local dev, mock mode, or before Mark's Supabase project exists), every
request is treated as an unauthenticated dev user rather than rejected -
this file only starts enforcing real sign-in once a real project is
configured, mirroring session_cap.py's existing "off until configured"
discipline.

Sign-in itself stays optional even once a project is configured (Mark's
call, 2026-07-25): this pilot asks participants to keep to a session
limit rather than enforcing one, so a request with no Authorization
header at all is treated as anonymous, not rejected - the same
unauthenticated-dev-user identity used when Supabase isn't configured at
all. Only a token that's actually present but invalid/expired is treated
as an error, since that means someone believes they're signed in and
isn't - worth telling them, unlike simply never having signed in.
"""

from dataclasses import dataclass
from functools import lru_cache

from fastapi import Header, HTTPException

from app.config import settings


@dataclass
class AuthedUser:
    user_id: str | None
    pilot_cohort: str | None
    max_sessions: int


@lru_cache
def _get_client():
    from supabase import create_client

    return create_client(settings.supabase_url, settings.supabase_service_key)


def supabase_configured() -> bool:
    return bool(settings.supabase_url and settings.supabase_service_key)


async def get_current_user(authorization: str | None = Header(default=None)) -> AuthedUser:
    """
    FastAPI dependency. Verifies the bearer token against Supabase Auth and
    loads the matching profiles row (created automatically on signup by the
    on_auth_user_created trigger in supabase_schema.sql).

    Returns a dev placeholder (no real identity, unlimited sessions) when
    Supabase isn't configured, so local development and mock-mode testing
    keep working without a project. Returns that same anonymous placeholder
    when Supabase IS configured but no token was offered at all - sign-in
    is an ask for this pilot, not a requirement (see module docstring).
    """
    if not supabase_configured():
        return AuthedUser(user_id=None, pilot_cohort=None, max_sessions=999)

    if not authorization or not authorization.lower().startswith("bearer "):
        return AuthedUser(user_id=None, pilot_cohort=None, max_sessions=999)

    token = authorization.split(" ", 1)[1].strip()
    client = _get_client()

    try:
        auth_response = client.auth.get_user(token)
    except Exception:
        raise HTTPException(status_code=401, detail="That sign-in has expired. Please sign in again.")

    user = getattr(auth_response, "user", None)
    if user is None:
        raise HTTPException(status_code=401, detail="That sign-in has expired. Please sign in again.")

    profile_rows = (
        client.table("profiles")
        .select("pilot_cohort, max_sessions")
        .eq("user_id", user.id)
        .limit(1)
        .execute()
        .data
    )
    profile = profile_rows[0] if profile_rows else {}

    return AuthedUser(
        user_id=user.id,
        pilot_cohort=profile.get("pilot_cohort"),
        max_sessions=profile.get("max_sessions", 5),
    )


async def get_audit_user(authorization: str | None = Header(default=None)) -> AuthedUser:
    """
    FastAPI dependency for the session audit endpoint (S4.2, Pass 1 §6.7:
    the audit endpoint becomes authenticated and durable).

    Stricter than get_current_user in exactly one way: once Supabase is
    configured, an anonymous request is REJECTED rather than admitted as
    the anonymous placeholder. Participants may keep conversation itself
    sign-in-optional (Mark's 2026-07-25 call, unchanged); the audit trail
    is a reviewer surface and Level 3's backbone, not part of that ask.
    Unconfigured (local dev / mock mode) deployments stay open - the same
    "off until configured" discipline as everything else in this module.
    """
    user = await get_current_user(authorization)
    if supabase_configured() and user.user_id is None:
        raise HTTPException(
            status_code=401,
            detail="The audit view requires a signed-in account.",
        )
    return user
