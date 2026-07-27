"""
Server-side transcript capture for pilot participants, now durable in
Supabase Postgres instead of an overwrite-every-round local JSON file (git
history has the old version).

Scoped narrowly per the pilot plan (Ministry/Operations/
CiC_Prototype_Testing_Pilot_Plan_DRAFT_V0_1.md, Section 4/6): every pilot
conversation saved automatically, project-team visibility only. Off by
default (settings.pilot_logging_enabled), so a non-pilot deployment doesn't
silently start logging conversations nobody disclosed logging to. Also a
no-op if Supabase isn't configured (see app/auth.py's supabase_configured())
- local dev/mock mode never needs a live project.

Testers are told about this plainly, in advance, in the onboarding text -
this module does not add any disclosure of its own; the disclosure lives in
the participant-facing onboarding screen, not here.

Storage model: `sessions` is upserted (one row per session_id, updated in
place - phase/turn_count/status change over a conversation's life).
`messages` is append-only, so each call only inserts the messages not yet
persisted rather than re-writing the whole history every round.

S4.2 note: the `state` passed in is now a projection of the append-only
event log (app/graph/events.py) rather than the old shared mutable
object - this module's interface and behavior are unchanged. The event
log ALSO persists itself (JSONL + the session_events table) - that is the
complete governance/audit record; these `sessions`/`messages` tables stay
as the human-readable transcript view Mark actually reviews.
"""

from langchain_core.messages import BaseMessage

from app.auth import _get_client, supabase_configured
from app.config import settings
from app.graph.state import ConversationState


def _serialize_message(msg: BaseMessage) -> dict:
    role = "user" if msg.type == "human" else "assistant"
    entry = {
        "role": role,
        "name": getattr(msg, "name", None),
        "content": msg.content if isinstance(msg.content, str) else str(msg.content),
    }
    citations = msg.additional_kwargs.get("citations") if hasattr(msg, "additional_kwargs") else None
    if citations:
        entry["citations"] = citations
    return entry


def write_transcript(session_id: str, state: ConversationState) -> None:
    """
    Upsert this session's row and append any messages not yet persisted.
    Called after each completed round (same call sites/trigger points as
    before). Never raises - transcript capture must never be able to break
    or slow down a participant's actual conversation (same discipline as
    the other invisible-background-governance code in main.py's streaming
    endpoint, which this is called alongside).
    """
    if not settings.pilot_logging_enabled or not supabase_configured():
        return

    try:
        client = _get_client()

        client.table("sessions").upsert(
            {
                "id": session_id,
                "user_id": state.user_id,
                "world_ids": state.world_ids or [state.world_id],
                "phase": state.phase,
                "turn_count": state.turn_count,
                "status": "closed" if state.closing_stage == "closed" else "active",
            }
        ).execute()

        already_persisted = (
            client.table("messages")
            .select("id", count="exact")
            .eq("session_id", session_id)
            .execute()
            .count
            or 0
        )

        new_messages = [_serialize_message(m) for m in state.messages[already_persisted:]]
        if new_messages:
            client.table("messages").insert(
                [{"session_id": session_id, **m} for m in new_messages]
            ).execute()
    except Exception:
        # Never let transcript capture surface as a broken response -
        # worst case, this round's persistence is silently skipped and the
        # next round's call catches up (upsert + already_persisted count
        # make this self-healing rather than duplicating rows).
        pass
