"""Who is allowed to act on a session.

This is request authorization, not retrieval, and it deliberately does NOT
share machinery with the evidence pipeline it happens to sit near in main.py.
The only thing the two have in common is the file they were edited in.

The gap this closes
-------------------
/api/session/{id}/message, /message/stream and GET /api/session/{id} used to
check only EVENT_STORE.has(session_id). A session_id is a UUID, and a UUID
leaks: a shared link, a Referer header, a log line, a screenshot. Anyone
holding one could read a participant's entire transcript or post into their
conversation as them.

Why identity cannot close it
----------------------------
app/auth.py's get_current_user/AuthedUser is real Supabase-backed identity,
but sign-in is optional by explicit project design. Every anonymous
participant therefore shares the same user_id (None) and cannot be told apart
from any other. An identity check would either lock out anonymous
participants - which the design forbids - or authorize all of them equally,
which is the gap it was meant to close.

So this is possession-based, not identity-based: a random secret minted once
at session start, returned to whoever started the session, and required on
every later request against it. It works whether or not the participant ever
signs in, which is exactly the property the optional-sign-in design needs.

One deliberate non-application
------------------------------
/audit is not covered UNCONDITIONALLY. That endpoint exists for a signed-in
reviewer reading a session they did not start; get_audit_user already gates
it once Supabase is configured, and this module's check is never applied on
top of that - doing so would lock every reviewer out of every session but
their own, which would not harden the endpoint, it would break its purpose.

/audit's real gap was different: no restriction at all when Supabase is
unconfigured, since get_audit_user has no identity to check against and
admits everyone. That gap now has its own answer (see get_session_audit in
main.py): when supabase_configured() is False, it calls
require_session_access same as every other session-scoped route - the
participant who started the session can still read their own audit trail,
but a session_id alone no longer opens every session's transcript to anyone
holding one. That branch never runs once Supabase is configured; the
signed-in check takes back over as the only gate, exactly as before.

Sessions predating this field are never enforced against (session_token is
None). That is a deliberate, bounded fail-open so a conversation already in
flight at deploy time does not start 403-ing a real participant mid-sentence.
Every session created after this ships mints a token and is enforced.
"""

import secrets

from fastapi import HTTPException

# 32 bytes from secrets.token_urlsafe - ~256 bits of entropy, URL-safe so it
# survives being carried in a header without encoding surprises.
_TOKEN_BYTES = 32


def mint_session_token() -> str:
    """A fresh session secret. Called exactly once, at session start."""
    return secrets.token_urlsafe(_TOKEN_BYTES)


def require_session_access(state, presented_token: str | None) -> None:
    """Raise 403 unless `presented_token` is this session's secret.

    Returns silently for a pre-token session (state.session_token is None) -
    see the module docstring on why that fail-open is bounded and deliberate.

    Comparison is secrets.compare_digest, not ==, so the check does not leak
    the token one byte at a time through response timing.
    """
    expected = getattr(state, "session_token", None)
    if expected is None:
        return
    if not presented_token or not secrets.compare_digest(presented_token, expected):
        raise HTTPException(status_code=403, detail="Not authorized for this session.")
