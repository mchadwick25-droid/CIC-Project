"""
Per-participant ceiling on sessions started, now backed by Supabase Postgres
instead of the pilot's original flat JSON files (git history has the old
version, which counted anonymous "tester codes" typed into a URL rather than
real signed-in users).

The reasoning that shaped the original mechanism still holds and is
preserved here: a single shared budget lets whoever dives in first burn the
whole pilot's spend before anyone else gets a turn, so each participant gets
their own ceiling (profiles.max_sessions, default 5) instead of one shared
pool. What's different now: identity comes from a real signed-in Supabase
user (see app/auth.py) rather than a code typed into a URL, and the count
itself is a `select count(*)` against the durable `sessions` table rather
than a hand-maintained counts file - both fixes for the old mechanism's
documented non-atomic, no-real-accounts limitations.

Off by default: if Supabase isn't configured (see app/auth.py's
supabase_configured()), every request is allowed uncapped - normal local
dev/mock-mode behavior, unchanged from before.

Also allowed uncapped for an anonymous request even once Supabase IS
configured: sign-in is an ask for this pilot, not a requirement (Mark's
call, 2026-07-25 - see app/auth.py's get_current_user), so a request with
no signed-in identity has nothing to count sessions against and is let
through rather than blocked. This cap only actually bites for a
participant who chose to sign in.
"""

from app.auth import AuthedUser, supabase_configured


def check_and_reserve_session_slot(user: AuthedUser) -> tuple[bool, str]:
    """
    Returns (allowed, reason). Unlike the old file-based version, this does
    NOT reserve/increment anything itself - the reservation is implicit: the
    caller (main.py's start_session) inserts a new row into `sessions`
    later in the same request, once the session's initial state is known,
    and that insert *is* the usage record the next check counts against.
    There is nothing to "give back" if session creation fails partway,
    since no separate counter exists to roll back.

    2026-08-05: this insert previously didn't exist anywhere in the
    codebase despite this docstring's claim - the cap could never actually
    fire (full-system review, Engineering P0-2). Fixed in start_session,
    decoupled from settings.pilot_logging_enabled (session *counting* and
    transcript *capture* are different questions; conflating them under one
    flag was the root cause).
    """
    if not supabase_configured() or user.user_id is None:
        return True, ""

    from app.auth import _get_client  # local import: avoids a hard dependency at module load

    client = _get_client()
    count_response = (
        client.table("sessions")
        .select("id", count="exact")
        .eq("user_id", user.user_id)
        .execute()
    )
    used = count_response.count or 0

    if used >= user.max_sessions:
        return False, (
            "You've reached this pilot's session limit for your account. "
            "Please reach out to the project team directly if you'd like to continue."
        )

    return True, ""
