"""The access service: the operations the conversation engine calls.

A visitor is identified by the signed visitor id the engine already issues. The
ledger is consulted when a conversation starts and when its first reply is
stored, never on each message, so an open conversation continues without a
ledger call.
"""
import sqlite3
from dataclasses import dataclass
from datetime import datetime

from .ledger import Admission, Ledger

FREE_CONVERSATIONS = 3
FREE_TURNS = 3
PAID_TURNS = 7


@dataclass(frozen=True)
class BalanceView:
    free: int
    paid: int

    @property
    def total(self) -> int:
        return self.free + self.paid


@dataclass(frozen=True)
class Started:
    admitted: bool
    bucket: str | None
    turn_cap: int | None
    reason: str


class AccessService:
    def __init__(self, conn: sqlite3.Connection, free_conversations: int = FREE_CONVERSATIONS):
        self.ledger = Ledger(conn)
        self.free_conversations = free_conversations

    def ensure_free_allowance(self, visitor_id: str, now: datetime | None = None) -> bool:
        """Grants the free allowance once per visitor. Returns True on the first call."""
        return self.ledger.grant_free(visitor_id, self.free_conversations, f"free:welcome:{visitor_id}", now=now)

    def balance(self, visitor_id: str) -> BalanceView:
        return BalanceView(free=self.ledger.balance(visitor_id, "free"), paid=self.ledger.balance(visitor_id, "paid"))

    def start_conversation(self, visitor_id: str, session_id: str, now: datetime | None = None) -> Started:
        self.ensure_free_allowance(visitor_id, now=now)
        admission: Admission = self.ledger.hold(visitor_id, session_id, now=now)
        if not admission.admitted:
            return Started(False, None, None, admission.reason)
        cap = FREE_TURNS if admission.bucket == "free" else PAID_TURNS
        return Started(True, admission.bucket, cap, admission.reason)

    def first_reply_stored(self, session_id: str, now: datetime | None = None) -> bool:
        return self.ledger.capture(session_id, now=now)

    def conversation_failed(self, session_id: str, now: datetime | None = None) -> bool:
        return self.ledger.release(session_id, now=now)
