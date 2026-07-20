"""
A soft, identity-free ceiling on how long a single conversation can run.

Added 2026-07-20 when Mark simplified the pilot design: no sign-in, no
pre/post-survey gate, no invite-code scheme - the live app goes up on the
website close to how it will look at public launch, access controlled
informally (a personal ask not to forward the link, plus watching traffic)
rather than through app-level identity. That removes session_cap.py's own
protection entirely for this pilot, since it depends on knowing who a
participant is (see app/auth.py) - with no sign-in, every visitor is the
same anonymous dev user and session_cap.py's per-identity check is a
permanent no-op.

This is the replacement backstop for that gap: not who is talking, but how
long any single conversation is allowed to run, checked against
state.turn_count (incremented once per Representative turn, so it's a
direct proxy for API spend on this session) rather than any signed-in
identity. Unlike session_cap.py, this has no "off until Supabase is
configured" switch - it is the actual safety net for exactly the
no-Supabase case, so it stays on unconditionally.

Deliberately generous, not tight: the point is to protect against a
genuinely runaway session (the link spreading further than intended, a
script, or a session left open in a loop), not to cut short an engaged
pilot tester's real conversation. Adjust CONVERSATION_TURN_CAP directly if
it turns out to bind on real, wanted use.
"""

CONVERSATION_TURN_CAP = 60


def check_message_cap(turn_count: int) -> tuple[bool, str]:
    """
    Returns (allowed, reason). Call before generating a new Representative
    turn; a False return means the caller should end the round gracefully
    instead of generating one, same shape as session_cap.check_and_reserve_
    session_slot so both can be checked the same way at a call site.
    """
    if turn_count >= CONVERSATION_TURN_CAP:
        return False, (
            "This conversation has reached its length for one sitting. "
            "Thank you for the time you gave it - if you'd like to continue, "
            "please reach out to the project team directly."
        )
    return True, ""
