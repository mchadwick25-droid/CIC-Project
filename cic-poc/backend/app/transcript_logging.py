"""
Server-side transcript capture for the tester pilot.

Scoped narrowly per the pilot plan (Ministry/Operations/
CiC_Prototype_Testing_Pilot_Plan_DRAFT_V0_1.md, Section 4/6): every pilot
conversation saved automatically, project-team visibility only, retained
only for the pilot's own review window - not a general-purpose analytics
or training store. Off by default (settings.pilot_logging_enabled), so a
non-pilot deployment doesn't silently start logging conversations nobody
disclosed logging to.

Testers are told about this plainly, in advance, in the onboarding text
(Article 36) - this module does not add any disclosure of its own; the
disclosure lives in the participant-facing onboarding screen, not here.
"""

import json
from datetime import datetime, timezone
from pathlib import Path

from langchain_core.messages import BaseMessage

from app.config import settings
from app.graph.state import ConversationState

TRANSCRIPTS_DIR = Path("./transcripts")


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
    Overwrite this session's transcript file with the full conversation so
    far. Called after each completed round - idempotent full-overwrite
    rather than incremental append, so a mid-write crash can never leave a
    corrupted partial file; the previous round's complete write is only
    ever replaced by another complete write.

    Silently does nothing if pilot_logging_enabled is false, or if writing
    fails for any reason - transcript capture must never be able to break
    or slow down a participant's actual conversation (same discipline as
    the other invisible-background-governance code in main.py's streaming
    endpoint, which this is called alongside).
    """
    if not settings.pilot_logging_enabled:
        return

    try:
        TRANSCRIPTS_DIR.mkdir(parents=True, exist_ok=True)
        payload = {
            "session_id": session_id,
            "world_id": state.world_id,
            "world_ids": state.world_ids,
            "phase": state.phase,
            "turn_count": state.turn_count,
            "last_updated_utc": datetime.now(timezone.utc).isoformat(),
            "messages": [_serialize_message(m) for m in state.messages],
        }
        out_path = TRANSCRIPTS_DIR / f"{session_id}.json"
        out_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    except Exception:
        # Never let transcript capture surface as a broken response -
        # worst case, this round's transcript write is silently skipped.
        pass
