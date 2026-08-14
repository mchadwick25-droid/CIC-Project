"""SH-11: prepared answers pulled seamlessly into interview mode.

Grounded in old-tree Ministry Technology/Pass3/cost_floor_model.py STEP 5 (a real
analysis, orphaned off `main` by the branch-chaining cleanup rather than
superseded - preserved at commit d7c1e86, never merged). Its headline: a
prior estimate that this could cover 30-50% of cost was wrong. The real
served fraction is ~5.2% central (range 4-16% across optimistic/
conservative assumptions), because a precomputed answer can only be served
when THREE things hold at once - see `old-tree Ministry Features/Guided-Questions/`:

  1. The participant took the question-first door, not "I know who I want
     to talk to" (~1/3 of entries - three co-equal doors, no default).
  2. They tapped a starter question rather than typing their own freely -
     the other branch of that same door.
  3. They stayed on the curriculum's own walk without deviating - "the
     participant can jump anywhere," per the curriculum doc itself, and
     any deviation ends the chain.

So this is real - worth building for the quality/consistency win on
curriculum-path traffic, per the Task Board's own framing of SH-11 - but
it is a narrow, specific lever, not a general FAQ/RAG answer-matcher. It
serves ONE thing: an exact, unmodified tap on a known curriculum starter
question, for a single-world (interview-mode) session. It never serves a
paraphrase, a free-typed question that merely resembles a starter, or
anything in Table mode (the cost model's own table bank is the expensive
one and ages fastest - not this build's scope, and Table is becoming a
paid-tier feature per the 2026-07-31 Table-mode product-shape decision
anyway, which needs its own subscription-gating infrastructure this
doesn't touch).

Why an explicit client signal, not text matching
--------------------------------------------------
Zero UI for the curriculum currently exists (Guided-Questions Design docs,
2026-07-16: "no question here has faced a live model"). Whenever that UI
is built, this module's contract is: a curriculum_ref accompanies a
request ONLY when the participant tapped a starter button whose exact
text this app itself rendered - never inferred from parsing free-typed
text. That is what makes "never serves a paraphrase" true by construction
rather than by hoping a fuzzy matcher never misfires. As a second,
independent safeguard (defense in depth against a future UI bug or a
tampered request), lookup() STILL cross-checks the participant's message
text against the bank entry's own stored question text and refuses to
serve on any mismatch - see _normalize()/lookup() below.

Storage
-------
One JSON file per world (data/answer_bank/<world_id>.json), matching this
app's existing per-world data layout. Each entry is keyed by
(role, set_id, question_order) - see
old-tree Ministry Features/Guided-Questions/Design/CiC_Guided_Questions_Curriculum_V1_0.json
for the real role/set/question IDs this must be built against; nothing
here invents its own numbering. An entry's answer_text, citations,
retrieval_audit, and glosses_used are exactly what a live representative
turn would have produced - captured once, at build time, by
scripts/build_answer_bank.py (not run by this module; needs a live API
key and Mark's go-ahead to spend it, same as B-COST).

A whole CHAIN is precomputable, not just a set's first question - since a
walk is deterministic while undeviated, question 2's precompute call
carries questions/answers 1 in its own transcript, exactly mirroring what
a live undeviated walk would look like at that point. See the build
script for how a chain is actually generated.

Self-invalidating cache, mtime/size keyed - same pattern as
app/graph/world_sources.py, so an edited or newly-built bank file is
never served stale within a running process.
"""

import json
import unicodedata
from pathlib import Path

from langchain_core.messages import AIMessage

from app.answer_bank_logging import log_answer_bank_decision
from app.config import settings
from app.graph.state import RetrievedContext

_CACHE: dict[str, dict] = {}
_CACHE_STAT: dict[str, tuple] = {}


def _bank_path(world_id: str) -> Path:
    return settings.data_base_path / "answer_bank" / f"{world_id}.json"


def _load_bank(world_id: str) -> dict:
    path = _bank_path(world_id)
    if not path.exists():
        return {}
    stat = path.stat()
    cache_key = (stat.st_mtime_ns, stat.st_size)
    if _CACHE_STAT.get(world_id) == cache_key:
        return _CACHE[world_id]

    data = json.loads(path.read_text(encoding="utf-8"))
    entries = {}
    for entry in data.get("entries", []):
        key = (entry["role"], entry["set_id"], entry["question_order"])
        entries[key] = entry

    _CACHE[world_id] = entries
    _CACHE_STAT[world_id] = cache_key
    return entries


def _normalize(text: str) -> str:
    """NFKC + casefold + collapsed whitespace - matches the same message
    modulo the trivial variation a browser/OS could introduce (curly vs
    straight quotes, trailing whitespace), never anything looser than that.
    """
    return " ".join(unicodedata.normalize("NFKC", text).casefold().split())


def lookup(world_id: str, curriculum_ref: dict, participant_message: str) -> dict | None:
    """The bank entry for this (world, role, set, question), or None.

    Refuses to return an entry whose own stored question text doesn't
    normalize-match participant_message, even though curriculum_ref named
    it explicitly - see the module docstring's "defense in depth" note.
    Every outcome is logged (see app/answer_bank_logging.py) since this is
    the only place that can measure the real served fraction against the
    cost model's 5.2% estimate.
    """
    role = curriculum_ref.get("role")
    set_id = curriculum_ref.get("set_id")
    question_order = curriculum_ref.get("question_order")
    key = (role, set_id, question_order)

    entries = _load_bank(world_id)
    entry = entries.get(key)
    if entry is None:
        log_answer_bank_decision(world_id, role, set_id, question_order,
                                  hit=False, reason="no_bank_entry")
        return None

    if _normalize(entry["question_text"]) != _normalize(participant_message):
        log_answer_bank_decision(world_id, role, set_id, question_order,
                                  hit=False, reason="text_mismatch")
        return None

    log_answer_bank_decision(world_id, role, set_id, question_order,
                              hit=True, reason=None)
    return entry


def try_answer_bank(state, curriculum_ref: dict | None, participant_message: str,
                     request_id: str | None = None) -> dict | None:
    """Returns exactly the same shape app.graph.nodes.representative_engages
    returns on a hit - {"messages": [...], "turn_count": ..., ...} - so a
    caller can drop this in ahead of the live call with no other change.
    Returns None on any kind of miss, meaning "fall through to the live
    path"; request_id is accepted only so both branches of that fallthrough
    share one call signature, and isn't used here (nothing is generated).
    """
    if curriculum_ref is None:
        return None
    if state.world_ids and len(state.world_ids) > 1:
        log_answer_bank_decision(state.world_id, curriculum_ref.get("role"),
                                  curriculum_ref.get("set_id"),
                                  curriculum_ref.get("question_order"),
                                  hit=False, reason="table_mode_excluded")
        return None

    world_id = state.current_world_id or state.world_id
    entry = lookup(world_id, curriculum_ref, participant_message)
    if entry is None:
        return None

    message_kwargs = {}
    if entry.get("citations"):
        message_kwargs["citations"] = entry["citations"]
    if entry.get("retrieval_audit"):
        message_kwargs["retrieval_audit"] = entry["retrieval_audit"]
    if entry.get("glosses_used"):
        message_kwargs["glosses_used"] = entry["glosses_used"]

    return {
        "messages": [
            AIMessage(
                content=entry["answer_text"],
                name=entry["representative_name"],
                additional_kwargs=message_kwargs,
            )
        ],
        "turn_count": state.turn_count + 1,
        "requires_reroot": False,
        "current_world_id": world_id,
        "retrieved_context": RetrievedContext(
            chunks=[], terms=[], sources=[],
            citations=entry.get("citations", []),
        ) if entry.get("citations") else None,
    }


def stream_answer_bank(state, curriculum_ref: dict | None, participant_message: str,
                        request_id: str | None = None):
    """Same yield-contract as app.graph.nodes.stream_representative_turn's
    generator ({"type": "token", ...} chunks then one {"type": "complete",
    ...}), for the streaming endpoint. Returns None (not a generator) on a
    miss - the caller's job to fall through to the live generator in that
    case, same contract as try_answer_bank.

    Known simplification, not hidden: chunks are yielded with no pacing
    delay between them (a live call's pacing comes from real network I/O;
    a synchronous sleep() here would block the whole process's event loop
    for every other concurrent request, which is a worse trade). A banked
    answer therefore arrives faster than a live one, not artificially
    slowed to disguise that - flagged for whoever picks this up if that
    ever needs to change, rather than solved speculatively here.
    """
    result = try_answer_bank(state, curriculum_ref, participant_message, request_id=request_id)
    if result is None:
        return None

    message = result["messages"][0]

    def _gen():
        text = message.content
        words = text.split(" ")
        for i, word in enumerate(words):
            piece = word + (" " if i < len(words) - 1 else "")
            yield {"type": "token", "speaker": message.name, "text": piece}
        yield {
            "type": "complete",
            "speaker": message.name,
            "message": message,
            "current_world_id": result["current_world_id"],
        }

    return _gen()
