"""Writes one quality-control row per finished turn (engine.m7.qc_store).
The conversation token is a keyed hash of the session id under a server
secret and is never written to the event log, so the QC store and the event
log share no key and cannot be joined without the secret. The same session
has the same token across restarts, which is how a deleted conversation's
rows are found and removed. With no secret given (tests, local runs) the
token is random and held in this process's memory only.
"""
import hashlib
import hmac
import logging
import secrets
import sqlite3
import threading
from collections import OrderedDict
from datetime import date, datetime, timezone

from engine.m4 import evidence
from engine.m4.grounding_net import all_text
from engine.m7.qc_scrub import known_names, scrub
from engine.m7.qc_store import QCStore

logger = logging.getLogger("cic.api")

TOKENS_HELD = 10_000

# A turn the safety call flagged, or could not classify, keeps no text.
_TEXT_FREE_SIGNALS = {"ACUTE_DISTRESS", "HARMFUL_DYNAMIC_SIGNAL", "AMBIGUOUS_LOW_CONFIDENCE"}


def text_free(safety: dict | None) -> bool:
    if safety is None:
        return True
    return safety.get("signal") in _TEXT_FREE_SIGNALS or bool(safety.get("dynamic_tags"))


class QCRecorder:
    def __init__(self, store: QCStore, registry: dict, secret: str | None = None):
        self.store = store
        self._secret = secret.encode() if secret else None
        self._registry_names = known_names(
            name for entry in registry.values() for name in (entry.get("card_name"), entry.get("name")) if name
        )
        self._tokens: OrderedDict[str, list] = OrderedDict()
        self._known: dict[str, frozenset] = {}
        self._lock = threading.Lock()

    def token_for(self, session_id: str) -> str | None:
        """The conversation token for a session, or None where tokens are random per process."""
        if self._secret is None:
            return None
        return hmac.new(self._secret, b"cic-qc-token-v1|" + session_id.encode(), hashlib.sha256).hexdigest()[:32]

    def forget(self, session_id: str) -> int:
        """Removes a deleted conversation's rows. Where the token is random, only a session this
        process still remembers can be found."""
        token = self.token_for(session_id)
        with self._lock:
            entry = self._tokens.pop(session_id, None)
        token = token or (entry[0] if entry else None)
        return self.store.delete_conversation(token) if token else 0

    def _next_round(self, session_id: str) -> tuple[str, int]:
        with self._lock:
            entry = self._tokens.pop(session_id, None)
            if entry is None:
                fixed = self.token_for(session_id)
                # A session seen again after a restart carries on from the last round written.
                entry = [fixed, self.store.max_round(fixed)] if fixed else [secrets.token_hex(16), 0]
            entry[1] += 1
            self._tokens[session_id] = entry
            while len(self._tokens) > TOKENS_HELD:
                self._tokens.popitem(last=False)
            return entry[0], entry[1]

    def _names_for(self, world) -> frozenset:
        if world is None:
            return self._registry_names
        key = world.world_key
        if key not in self._known:
            records = evidence.repository_records_by_id(world.repository).values()
            self._known[key] = known_names(all_text(r) for r in records) | self._registry_names
        return self._known[key]

    def record_safely(self, **kwargs) -> None:
        """record(), but a failed QC write is logged and never breaks the
        participant's turn: the QC store is secondary to the conversation."""
        try:
            self.record(**kwargs)
        except sqlite3.Error:
            logger.exception("QC store write failed")

    def record(self, *, session_id: str, world_key: str, world=None, package_hash: str | None, model_id: str | None, question: str,
               routing_action: str, safety: dict | None, voice_event: dict | None, answer_text: str | None,
               today: date | None = None) -> None:
        token, round_no = self._next_round(session_id)
        flags = {
            "safety_signal": "failed" if safety is None else safety.get("signal"),
            "dynamic_tags": [] if safety is None else list(safety.get("dynamic_tags") or []),
            "text_free": text_free(safety),
        }
        citations = (voice_event or {}).get("citations") or []
        marks = {
            "cited_record_ids": sorted({rid for c in citations for rid in c.get("record_ids", [])}),
            "cited_sentences": len(citations),
            "attached_sentences": sum(1 for c in citations if c.get("attached")),
        }
        scores = {
            "degraded_by_net": bool((voice_event or {}).get("degraded_by_net")),
            "horizon_mentions": sum(1 for d in (voice_event or {}).get("output_defects") or [] if d.get("family") == "horizon"),
        }
        names = self._names_for(world)
        keep_text = not flags["text_free"]
        self.store.write_turn(
            conversation_token=token, round_no=round_no, world=world_key, package_hash=package_hash,
            model_id=model_id, routing=routing_action, flags=flags,
            question_text=scrub(question, names) if keep_text else None,
            answer_text=scrub(answer_text, names) if keep_text and answer_text else None,
            marks=marks, scores=scores, day=today or datetime.now(timezone.utc).date(),
        )
