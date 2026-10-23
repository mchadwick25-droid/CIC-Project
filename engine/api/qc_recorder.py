"""Writes one quality-control row per finished turn (engine.m7.qc_store).
The conversation token is a keyed hash of the conversation's own code under a
dedicated review key. The server keeps only a hash of that code, so the token
cannot be worked out from the event log, the account file or the review copy
with every secret in hand: it can be made only by someone holding the code,
which is the participant, or the shelf for its owner. A conversation's rows
can therefore be found and removed wherever its code is at hand, and are
otherwise unlinkable. With no review key given (tests, local runs) the token
is random and held in this process's memory only.
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
    def __init__(self, store: QCStore, registry: dict, secret: str | None = None, previous: tuple[str, ...] = ()):
        self.store = store
        self._secret = secret.encode() if secret else None
        self._previous = tuple(p.encode() for p in previous if p)
        self._registry_names = known_names(
            name for entry in registry.values() for name in (entry.get("card_name"), entry.get("name")) if name
        )
        self._tokens: OrderedDict[str, list] = OrderedDict()
        self._known: dict[str, frozenset] = {}
        self._lock = threading.Lock()

    @staticmethod
    def _normal(code: str) -> bytes:
        return code.replace("-", "").upper().encode()

    def token_for_code(self, code: str | None, *, key: bytes | None = None) -> str | None:
        """The conversation token for a code, or None where there is no code or no review key."""
        key = key if key is not None else self._secret
        if key is None or not code:
            return None
        return hmac.new(key, b"cic-qc-token-v2|" + self._normal(code), hashlib.sha256).hexdigest()[:32]

    def bound_to(self, code: str | None) -> "_BoundRecorder":
        """This recorder, for one conversation's turn, with its code in hand."""
        return _BoundRecorder(self, code)

    def forget(self, session_id: str, code: str | None = None) -> tuple[str, ...]:
        """Removes a deleted conversation's rows and returns the tokens it removed them under. With
        the code, every live review key is tried; without it only a session this process still
        remembers can be found."""
        tokens = []
        if code:
            for key in (self._secret, *self._previous):
                token = self.token_for_code(code, key=key) if key is not None else None
                if token:
                    tokens.append(token)
        with self._lock:
            entry = self._tokens.pop(session_id, None)
        if entry:
            tokens.append(entry[0])
        tokens = list(dict.fromkeys(tokens))
        for token in tokens:
            self.store.delete_conversation(token)
        return tuple(tokens)

    def forget_token(self, token: str) -> int:
        return self.store.delete_conversation(token)

    def _next_round(self, session_id: str, session_code: str | None = None) -> tuple[str, int]:
        with self._lock:
            entry = self._tokens.pop(session_id, None)
            if entry is None:
                fixed = self.token_for_code(session_code)
                # A conversation seen again after a restart carries on from the last round written.
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

    def record_safely(self, session_code: str | None = None, **kwargs) -> None:
        """record(), but a failed QC write is logged and never breaks the
        participant's turn: the QC store is secondary to the conversation."""
        try:
            self.record(session_code=session_code, **kwargs)
        except sqlite3.Error:
            logger.exception("QC store write failed")

    def record(self, *, session_id: str, world_key: str, world=None, package_hash: str | None, model_id: str | None, question: str,
               routing_action: str, safety: dict | None, voice_event: dict | None, answer_text: str | None,
               today: date | None = None, session_code: str | None = None) -> None:
        token, round_no = self._next_round(session_id, session_code)
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


class _BoundRecorder:
    """A recorder for one turn that knows the conversation's code, so the turn's review row gets
    the conversation's own token. Everything else is the recorder itself."""

    def __init__(self, recorder: QCRecorder, code: str | None):
        self._recorder = recorder
        self._code = code

    def record_safely(self, **kwargs) -> None:
        self._recorder.record_safely(session_code=self._code, **kwargs)

    def __getattr__(self, name):
        return getattr(self._recorder, name)
