"""S4.2 - the append-only conversation event log; state as projection.

Pass 1 §6.7: the mutable in-memory conversation state (with its
hand-patched read-modify-write race) is replaced by an append-only event
log; state is a derived projection. Same discipline the Source Registry
chose - never renumber, never delete - applied to the conversation layer.

What this module provides:

- EVENT_STORE: the process-wide append-only store. Appends are atomic
  (single lock) and every event is durably appended to a per-session
  JSONL file (`transcripts/events/<session_id>.jsonl` - the transcripts/
  dir is already the gitignored, per-deployment home for conversation
  data) and, when Supabase is configured, inserted into the
  `session_events` table (fail-open, same never-break-the-conversation
  discipline as transcript_logging - but NOT gated on
  settings.pilot_logging_enabled the way transcript_logging is; see
  `_persist_supabase`'s own docstring for why those are different
  questions, Wave 3 Engineering P1-4). There is NO in-place update path -
  the race disappears structurally, not by a cleverer merge. In-memory
  `_events` is also bounded (LRU by last-touch, same wave) so this store's
  memory footprint doesn't grow without bound across a process's lifetime.

- project(): fold a session's events into a ConversationState. The
  endpoints work on a per-request projected copy; every mutation they
  used to make on the shared dict object is now an appended event, and
  the next request's projection folds it in. The S4.2 state-parity
  instrument (app/graph/replay/state_parity.py) proves projected state
  equals the legacy store's state across the recorded suites.

- The §6.7 public-transcript data shape: `spoken_events_from_messages()`
  renders the ordered log of spoken events - speaker, text, designated
  addressee where one exists - from which each Representative's view is
  a deterministic render (nodes.build_public_transcript). The addressee
  is always None until S4.4's direct-address detection lands, and
  bridge-reframe events are logged (type `bridge_reframe`) but not yet
  rendered into any Representative's view - that behavior change is
  S4.5's, declared there. S4.2 is behavior-preserving: the render keeps
  today's Facilitator-skip and last-10 window exactly.

Event envelope: {seq, type, payload, ts}. `ts` is wall-clock
observability only and is never folded into the projection (replay
determinism). Payloads are JSON-safe primitives only - no live message
objects cross this boundary.

Projected fields deliberately reproduce two documented behaviors of the
legacy store rather than "fixing" them here (replay-parity forbids it):
FLAG-007's streaming-path exclusion-set omission is preserved (events
only record what the legacy paths actually persisted), and turn-local
fields (retrieval_query_override) never enter the log at all, exactly as
they never entered the legacy sessions dict.
"""
from __future__ import annotations

import json
import os
import threading
from collections import OrderedDict
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterator, Optional

from langchain_core.messages import AIMessage, HumanMessage

from app.graph.state import (
    ConversationState,
    DriftSignal,
    RetrievedContext,
    WorldContext,
)

_BACKEND = Path(__file__).resolve().parents[2]


def _events_dir() -> Path:
    return Path(os.environ.get("CIC_EVENTS_DIR",
                               _BACKEND / "transcripts" / "events"))


# World content is static on disk for a process's lifetime; the projection
# reloads it per world rather than storing megabytes of prompt text in
# every session's log (the state-parity instrument asserts sha-equality
# of the loaded content against the legacy store's copies).
_world_content_cache: dict[str, tuple[str, str]] = {}


def _load_world_content(world_id: str) -> tuple[str, str]:
    if world_id not in _world_content_cache:
        # same three lines as app.main.load_world_content - duplicated
        # here (not imported) so projecting never imports the FastAPI app
        from app.config import settings
        wc = settings.get_world_config(world_id)
        _world_content_cache[world_id] = (
            wc.permanent_prompt_path.read_text(encoding="utf-8"),
            wc.world_capsule_path.read_text(encoding="utf-8"),
        )
    return _world_content_cache[world_id]


@dataclass
class Event:
    seq: int
    type: str
    payload: dict
    ts: str = ""

    def to_json(self) -> dict:
        return {"seq": self.seq, "type": self.type,
                "payload": self.payload, "ts": self.ts}


def serialize_message(msg) -> dict:
    """A spoken/participant message as a JSON-safe event payload."""
    content = msg.content
    if isinstance(content, list):
        parts = []
        for block in content:
            if isinstance(block, dict) and block.get("type") == "text":
                parts.append(block.get("text", ""))
            elif isinstance(block, str):
                parts.append(block)
        content = "\n".join(parts)
    kwargs = getattr(msg, "additional_kwargs", {}) or {}
    return {
        "name": getattr(msg, "name", None),
        "text": content,
        "addressee": None,  # §6.7 shape; populated from S4.4 onward
        "citations": kwargs.get("citations") or None,
        "glosses_used": kwargs.get("glosses_used") or None,
        "retrieval_audit": kwargs.get("retrieval_audit") or None,
    }


def spoken_events_from_messages(messages) -> list[dict]:
    """The §6.7 public-transcript data shape: the ordered log of spoken
    events (speaker, text, designated addressee where one exists) from
    which each Representative's view is a deterministic render."""
    out = []
    for msg in messages:
        if isinstance(msg, HumanMessage):
            out.append({"speaker": "participant", "text": msg.content,
                        "addressee": None})
        elif getattr(msg, "name", None):
            out.append({"speaker": msg.name, "text": msg.content,
                        "addressee": None})
    return out


def _message_from_payload(p: dict, role: str):
    if role == "user":
        return HumanMessage(content=p["text"])
    kwargs = {}
    if p.get("citations"):
        kwargs["citations"] = p["citations"]
    if p.get("glosses_used"):
        kwargs["glosses_used"] = p["glosses_used"]
    if p.get("retrieval_audit"):
        kwargs["retrieval_audit"] = p["retrieval_audit"]
    return AIMessage(content=p["text"], name=p.get("name"),
                     additional_kwargs=kwargs)


def project(session_id: str, events: list[Event]) -> ConversationState:
    """Fold a session's events into a ConversationState.

    Observability-only event types (classifier_decision, bridge_reframe)
    fold to nothing by design - they exist for the audit endpoint and the
    A.4 re-diagnosis, not for state.
    """
    state = ConversationState(session_id=session_id)
    for ev in events:
        p = ev.payload
        t = ev.type
        if t == "session_started":
            state.user_id = p.get("user_id")
            state.session_token = p.get("session_token")
            state.world_id = p["world_id"]
            state.world_ids = list(p["world_ids"])
            state.current_world_id = p["world_id"]
            prompt, capsule = _load_world_content(p["world_id"])
            state.permanent_prompt = prompt
            state.world_capsule_core = capsule
            state.worlds_at_table = []
            for wid in p["world_ids"]:
                w_prompt, w_capsule = _load_world_content(wid)
                state.worlds_at_table.append(WorldContext(
                    world_id=wid, permanent_prompt=w_prompt,
                    world_capsule=w_capsule))
        elif t == "participant_message":
            state.messages = list(state.messages) + [
                _message_from_payload(p, "user")]
        elif t == "spoken_message":
            state.messages = list(state.messages) + [
                _message_from_payload(p, "assistant")]
        elif t == "turn_committed":
            if "phase" in p:
                state.phase = p["phase"]
            if "turn_count" in p:
                state.turn_count = p["turn_count"]
            if "current_world_id" in p:
                state.current_world_id = p["current_world_id"]
            if "requires_reroot" in p:
                state.requires_reroot = p["requires_reroot"]
            if "current_speaker" in p:
                state.current_speaker = p["current_speaker"]
        elif t == "phase_changed":
            state.phase = p["phase"]
        elif t == "close_requested":
            state.close_requested = True
        elif t == "closing_stage_changed":
            state.closing_stage = p["stage"]
        elif t == "rs_state_updated":
            for k, v in p["updates"].items():
                setattr(state, k, v)
        elif t == "drift_signals_appended":
            state.drift_signals = list(state.drift_signals) + [
                DriftSignal(**s) for s in p["signals"]]
        elif t == "guidance_queued":
            # S4.3 payload shape: {world_id, entry:{signal_type, severity,
            # text}} folded through THE gate (governance.queue_guidance),
            # so the projection and the live writers share one ordering.
            # No committed event log carries the older S4.2 dict-merge
            # shape (verified at S4.3: no guidance events exist in any
            # committed JSONL), so no legacy fold is kept.
            from app.graph.governance import queue_guidance
            e = p["entry"]
            state.pending_guidance = queue_guidance(
                state.pending_guidance, p["world_id"], e["signal_type"],
                e["severity"], e["text"])
        elif t == "guidance_consumed":
            # pops the highest-priority entry (the head of the sorted
            # queue) for the world; drops the key once the queue is empty
            new = dict(state.pending_guidance)
            entries = list(new.get(p["world_id"]) or [])
            if entries:
                entries.pop(0)
            if entries:
                new[p["world_id"]] = entries
            else:
                new.pop(p["world_id"], None)
            state.pending_guidance = new
        elif t == "chunks_surfaced":
            seen = state.surfaced_chunk_ids.setdefault(p["world_id"], [])
            for stem in p["chunk_ids"]:
                if stem not in seen:
                    seen.append(stem)
        elif t == "retrieved_context_set":
            ctx = p.get("context")
            state.retrieved_context = (RetrievedContext(**ctx)
                                       if ctx is not None else None)
        elif t == "register_observed":
            # S4.7: the latest observation wins - rendered as the one
            # selector-input line select_next_speaker appends
            if p.get("absent"):
                state.register_note = (
                    "One more observation from the last round: the "
                    f"participant's own register leaned toward "
                    f"{p.get('participant_register') or 'their own key'}, and "
                    f"the round's speech left {p['absent']} conspicuously "
                    "absent. Where it genuinely fits, prefer the voice able "
                    "to meet that absent register - never force it."
                )
            else:
                state.register_note = None
        elif t == "bridge_reframe" and p.get("question"):
            # S4.5 (Pass 1 §6.6): the reframed question persists as the
            # question actually asked - folded as a Facilitator-spoken
            # sentinel every Representative's transcript render includes,
            # but which participant-facing responses filter out (the
            # participant heard the Facilitator's own spoken version).
            # S4.2-era bridge_reframe events (match-only payload, no
            # "question") fold to nothing, as before.
            state.messages = list(state.messages) + [AIMessage(
                content=p["question"], name="facilitator",
                additional_kwargs={"bridge_reframe": True})]
        # classifier_decision (and question-less bridge_reframe):
        # observability only
    return state


class EventStore:
    """Process-wide append-only event store with JSONL durability.

    In-memory `_events` is bounded, not unbounded (Wave 3, Engineering
    P1-4) - `render.yaml`'s 512MB starter plan already has an OOM history,
    and now loads two transformer models on top of that. Bounded by
    recency (`_events` is an OrderedDict; every touch moves a session to
    the end), evicting the least-recently-touched session once the cap is
    exceeded. Eviction removes ONLY the in-memory copy - the durable
    JSONL file (and Supabase mirror, when configured) are untouched, and
    `_read_jsonl`'s existing fallback (already used by `has()`) means an
    evicted session's next read transparently rehydrates from disk. This
    bounds worst-case memory without losing any data a live participant
    could still reach.
    """

    def __init__(self, max_sessions: int = 200):
        self._events: OrderedDict[str, list[Event]] = OrderedDict()
        self._lock = threading.Lock()
        self._max_sessions = max_sessions

    def _touch(self, session_id: str) -> None:
        """Move session_id to most-recently-used position. Caller holds _lock."""
        self._events.move_to_end(session_id)

    def _evict_lru_locked(self) -> None:
        """Evict least-recently-touched sessions over the cap. Caller holds _lock."""
        while len(self._events) > self._max_sessions:
            self._events.popitem(last=False)

    # -- append side ----------------------------------------------------
    def append(self, session_id: str, type: str, payload: dict) -> Event:
        return self.append_many(session_id, [(type, payload)])[0]

    def append_many(self, session_id: str,
                    items: list[tuple[str, dict]]) -> list[Event]:
        with self._lock:
            log = self._events.setdefault(session_id, [])
            self._touch(session_id)
            ts = datetime.now(timezone.utc).isoformat()
            new = []
            for type_, payload in items:
                ev = Event(seq=len(log) + 1, type=type_, payload=payload,
                           ts=ts)
                log.append(ev)
                new.append(ev)
            self._evict_lru_locked()
        self._persist_jsonl(session_id, new)
        self._persist_supabase(session_id, new)
        return new

    # -- read side ------------------------------------------------------
    def has(self, session_id: str) -> bool:
        if session_id in self._events:
            return True
        return (_events_dir() / f"{session_id}.jsonl").is_file()

    def session_ids(self) -> list[str]:
        with self._lock:
            return list(self._events.keys())

    def events(self, session_id: str, since_seq: int = 0) -> list[Event]:
        with self._lock:
            log = self._events.get(session_id)
            if log is not None:
                self._touch(session_id)
                return [e for e in log if e.seq > since_seq]
        # Miss (evicted, or never loaded this process) - rehydrate from the
        # durable JSONL log rather than treating this as "no such session".
        rehydrated = self._read_jsonl(session_id)
        if rehydrated:
            with self._lock:
                self._events[session_id] = list(rehydrated)
                self._touch(session_id)
                self._evict_lru_locked()
        return [e for e in rehydrated if e.seq > since_seq]

    def get_state(self, session_id: str) -> ConversationState:
        """Project this session's state. Always a fresh object - two
        concurrent requests never share a mutable state instance (the
        legacy dict handed both the same object; that sharing was the
        race's raw material)."""
        if not self.has(session_id):
            raise KeyError(session_id)
        return project(session_id, self.events(session_id))

    def project_fresh(self, session_id: str) -> ConversationState:
        """Project from the DURABLE log only (the JSONL on disk), proving
        the persisted log alone reconstructs the session - what makes the
        audit endpoint durable across a process restart."""
        events = self._read_jsonl(session_id)
        if not events:
            raise KeyError(session_id)
        return project(session_id, events)

    def clear(self) -> None:
        with self._lock:
            self._events.clear()

    # -- durability -----------------------------------------------------
    def _persist_jsonl(self, session_id: str, new: list[Event]) -> None:
        try:
            d = _events_dir()
            d.mkdir(parents=True, exist_ok=True)
            with open(d / f"{session_id}.jsonl", "a", encoding="utf-8") as f:
                for ev in new:
                    f.write(json.dumps(ev.to_json(), ensure_ascii=False)
                            + "\n")
        except Exception:
            # never let durability plumbing break a live conversation;
            # the in-memory log remains authoritative for this process
            pass

    def _read_jsonl(self, session_id: str) -> list[Event]:
        try:
            path = _events_dir() / f"{session_id}.jsonl"
            if not path.is_file():
                return []
            out = []
            for line in path.read_text(encoding="utf-8").splitlines():
                if not line.strip():
                    continue
                row = json.loads(line)
                out.append(Event(seq=row["seq"], type=row["type"],
                                 payload=row["payload"],
                                 ts=row.get("ts", "")))
            return out
        except Exception:
            return []

    def _persist_supabase(self, session_id: str, new: list[Event]) -> None:
        # Un-gated from settings.pilot_logging_enabled (Wave 3, Engineering
        # P1-4) - that flag governs a separate question (does the
        # human-readable transcript_logging.write_transcript view exist for
        # the project team to review, per the pilot plan's own disclosure
        # scoping) from this table's actual job: durability of the audit
        # log the participant is ALREADY told about unconditionally, in
        # every deployment, by OnboardingScreen.tsx's "we're cataloging
        # this conversation" paragraph. Before this fix, that promise held
        # only for the process's lifetime (JSONL on ephemeral disk) unless
        # pilot_logging_enabled also happened to be on - the durability
        # this table exists for was silently opt-in on a flag that has
        # nothing to do with durability. Still fully off when Supabase
        # isn't configured (local dev/mock mode never touches a live
        # project) - only the pilot_logging_enabled coupling is removed.
        try:
            from app.auth import _get_client, supabase_configured
            if not supabase_configured():
                return
            _get_client().table("session_events").insert([
                {"session_id": session_id, "seq": ev.seq, "type": ev.type,
                 "payload": ev.payload, "ts": ev.ts}
                for ev in new
            ]).execute()
        except Exception:
            # same never-break-the-conversation discipline as
            # transcript_logging.write_transcript
            pass


def _make_event_store() -> EventStore:
    try:
        from app.config import settings
        return EventStore(max_sessions=settings.event_store_max_sessions)
    except Exception:
        # Settings unavailable at import time (e.g. a narrow unit-test
        # context) - the class default keeps this working rather than
        # failing the whole module import over a bound-size preference.
        return EventStore()


EVENT_STORE = _make_event_store()
