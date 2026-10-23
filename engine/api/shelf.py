"""The shelf, at the edge.

The account module keeps a list of session ids and each conversation's own code,
sealed. It never reads a conversation. This module is where a shelved
conversation is looked at and removed: it proves a code opens a conversation,
describes one for the owner's list, says whether it holds a Facilitator safety
turn, and erases a conversation from every store that holds it. It imports
nothing from the accounts module.
"""
import logging
from pathlib import Path

from engine.m4 import session_code
from engine.m4.projection import project_fresh
from engine.m7 import erase
from engine.m7.session_reader import read_session

logger = logging.getLogger("cic.api")

TITLE_CHARS = 80


def code_opens(store, session_id, code) -> bool:
    """Whether this code is the one that opens this conversation."""
    if not isinstance(session_id, str) or not isinstance(code, str) or not code:
        return False
    state = project_fresh(session_id, store)
    return bool(state.exists and session_code.codes_match(code, state.code_hash))


def holds_safety_turn(audit) -> bool:
    """A conversation that holds any Facilitator safety turn (a crisis turn, a check-in or a
    dependency check): the owner is shown the resources line first on reopening it."""
    return any(turn.get("kind") == "safety" for turn in audit.facilitator_turns)


def _day(stamp: str | None) -> str | None:
    return stamp[:10] if stamp else None


def describe(store, registry: dict, session_id: str) -> dict | None:
    """What the owner's list shows of one conversation: read now from the conversation store,
    never kept in the account file. None when the conversation is gone."""
    audit = read_session(store, session_id)
    if audit is None:
        return None
    worlds = []
    for key in audit.world_keys:
        entry = registry.get(key) or {}
        worlds.append(entry.get("card_name") or entry.get("name") or key)
    first = audit.participant_messages[0]["text"].strip() if audit.participant_messages else ""
    title = first if len(first) <= TITLE_CHARS else first[: TITLE_CHARS - 1].rstrip() + "…"
    return {
        "session_id": session_id, "mode": audit.mode, "worlds": worlds,
        "world_keys": list(audit.world_keys), "title": title,
        "started": _day(audit.first_at), "last_active": _day(audit.last_activity_at or audit.last_at),
        "turns": len(audit.participant_messages), "closed": audit.closed,
        "holds_crisis_turn": holds_safety_turn(audit),
    }


class ConversationEraser:
    """Removes one conversation from every store that holds it: the event log, the audit files, the
    feedback rows that name it, the quality-control rows (found by their keyed token) and its id on
    the usage rows (the token counts stay, for the cost record). Each step is safe to repeat."""

    def __init__(self, store, usage_store, feedback_store, qc_recorder, audit_root, on_erased=None):
        self.on_erased = on_erased
        self.store = store
        self.usage_store = usage_store
        self.feedback_store = feedback_store
        self.qc_recorder = qc_recorder
        self.audit_root = Path(audit_root) if audit_root else None

    def erase(self, session_id: str, code: str | None = None, known_tokens: tuple[str, ...] = ()) -> dict:
        """Erases one conversation. With its code the review rows are found by their keyed token;
        without it only a conversation the process still remembers can be, and the tokens a first
        erasure recorded are given as known_tokens."""
        counts = {}
        tokens: tuple[str, ...] = tuple(known_tokens)
        if self.qc_recorder is not None:
            for token in known_tokens:
                self.qc_recorder.forget_token(token)
            tokens = tuple(dict.fromkeys((*known_tokens, *self.qc_recorder.forget(session_id, code))))
            counts["qc_tokens"] = len(tokens)
        if self.feedback_store is not None:
            counts["feedback_rows"] = self.feedback_store.delete_session(session_id)
        if self.usage_store is not None:
            counts["usage_rows"] = self.usage_store.forget_session(session_id)
        if self.audit_root is not None:
            counts["audit_files"] = erase.erase_session(self.audit_root, session_id)
        counts["events"] = self.store.delete_session(session_id)
        if self.on_erased is not None:
            self.on_erased(session_id, tokens)
        return counts

    def erase_again(self, session_id: str, qc_tokens: tuple[str, ...] = ()) -> dict:
        """Erases a conversation that came back (from a restored backup) or was written to while
        its deletion ran, by the tokens the first deletion recorded."""
        return self.erase(session_id, None, qc_tokens)
