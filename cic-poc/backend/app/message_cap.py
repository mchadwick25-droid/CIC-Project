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

# Raised 20 -> 40 at the S6.2 freeze fix session (2026-07-28), per this
# module's own instruction ("Adjust CONVERSATION_TURN_CAP directly if it
# turns out to bind on real, wanted use"): a two-representative table
# sitting runs 2-5 representative sub-turns per round (continuation
# exchanges), so an 8-round Table Readiness Round hit 20 at round 4-5 -
# wanted use, not runaway. 40 still bounds a genuinely runaway session.
#
# Split into two caps 2026-07-31 (Task Board SH item, Table-mode product
# shape): this single number was itself still cutting Table sittings short
# relative to solo ones - a 40-rep-turn conversation is 40 real participant
# rounds solo, but the B-COST baseline measured a 3-world table burning
# 2-3 representative turns per participant round (cost_baseline_2026-07_
# run_notes.md), so the same 40 landed at only ~13-20 real rounds for a
# table. Mark's call: split it rather than raise the shared number further
# (which would just let a runaway solo session run longer too, for no
# reason). CONVERSATION_TURN_CAP_TABLE = 100 targets the same ~40 real
# participant rounds a solo sitting already gets, at the measured mid-range
# burn rate (40 x 2.5 = 100) - deliberately the average case, not the
# worst-case 5x from the comment above, so it still bounds something
# genuinely runaway.
CONVERSATION_TURN_CAP_SOLO = 40
CONVERSATION_TURN_CAP_TABLE = 100

# Backwards-compatible alias - anything still importing the old flat name
# gets the solo figure, which is what it always meant before the split.
CONVERSATION_TURN_CAP = CONVERSATION_TURN_CAP_SOLO


def check_message_cap(turn_count: int, is_table: bool = False) -> tuple[bool, str]:
    """
    Returns (allowed, reason). Call before generating a new Representative
    turn; a False return means the caller should end the round gracefully
    instead of generating one, same shape as session_cap.check_and_reserve_
    session_slot so both can be checked the same way at a call site.

    is_table: True when more than one world is seated (state.world_ids has
    more than one entry) - picks the higher table-mode cap so a multi-
    representative sitting isn't cut short relative to a solo one just
    because it burns more representative turns per real exchange.
    """
    cap = CONVERSATION_TURN_CAP_TABLE if is_table else CONVERSATION_TURN_CAP_SOLO
    if turn_count >= cap:
        return False, (
            "This conversation has reached its length for one sitting. "
            "Thank you for the time you gave it - if you'd like to continue, "
            "please reach out to the project team directly."
        )
    return True, ""
