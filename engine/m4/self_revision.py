"""R38 (Rulings-Pending.md, RULED 2026-09-23): self-revision at
generation, Mark's own chosen fix for the fabrication-riding-a-real-tag
leak class the Theon/Donatists worked example showed (Decision-Log.md
Entries 57/59/60). Candidates A and B (lexical-remainder net rules) are
closed - 0/6 precision on honest paraphrase. Candidate C (the live
support-check reader) stays the documented fallback only; self-revision
measured 0 of 20 real leaks, at Mark's own "0 or 1 of 20" bar for
proposing the build (Decision-Log.md Entry 61).

After the voice drafts its turn, a SECOND voice call - same model, same
system prompt - is given its own draft plus the exact, full text of
every record it tagged, and told: for each tagged sentence, keep only
what that record says or exactly paraphrases; trim any detail the
record does not give, even if believed true; do not add, do not re-tag,
do not change any untagged sentence; return the revised turn. The
revised text is the only text `apply_net`, the guards, and the
participant ever see - generation, not correction: no withhold, no
Facilitator, no regeneration loop.

Scoped by the caller to `other_tradition`-routed turns only (where the
leak class lives) via `is_other_tradition_first_ask` - this module has
no routing knowledge of its own, the same "pure, no registry/routing
context" discipline `engine.m4.uncited_claims.find_uncited_claims`
already follows.

7b/R30 compatibility: the draft-then-revise pair is one atomic pre-
stream step. R30's own ruling already holds the opening paragraph until
the guard has checked it, then streams from a point already known
clean - self-revision fits that same shape without a new mechanism,
since the guard check (and any streaming) never starts on the DRAFT
text, only on what this module returns. Nothing here streams; the
caller's own streaming logic, whenever built, must call this (or skip
it, per the kill-switch below) before it ever begins emitting anything.
"""
from __future__ import annotations

import time

from engine.m4 import evidence as ev
from engine.m4 import grounding_net as gn
from engine.m4.generation import stream_voice_turn
from engine.m5.failure import CallOutcome

REVISION_INSTRUCTION = (
    "REVISION PASS - not a new question, and not addressed to the participant. You wrote the draft answer "
    "below to the participant's question about the Donatists. Review it against the real, full text of "
    "every record you tagged in it, given in full below. For each TAGGED sentence: keep only what that "
    "record actually says, or a fair paraphrase of it - trim any specific detail the record does not give, "
    "even if you believe it to be true. Do not add anything. Do not add, remove, or change any [[tag]]. Do "
    "not touch any UNTAGGED sentence at all, even to reword it. Return the complete revised answer, in the "
    "exact same format as the draft (the same tag grammar, the same structure), and nothing else - no "
    "preamble, no explanation of what you changed.\n\n"
    "YOUR DRAFT:\n{draft}\n\n"
    "THE RECORDS YOU TAGGED, IN FULL:\n{records_block}"
)


def _full_text_for_record(record: dict) -> str:
    return ev._head_text(record)


def _tagged_record_ids(raw_text: str) -> list[str]:
    tagged_text, _truncated = gn._drop_truncated_tail(raw_text)
    parsed = gn.parse_tagged(tagged_text)
    return sorted({rid for s in parsed for rid in (s.get("tags") or [])})


def build_revision_message(*, draft_text: str, tagged_record_ids: list[str], repository_records: dict[str, dict]) -> str:
    lines = []
    for rid in tagged_record_ids:
        record = repository_records.get(rid)
        if record is None:
            continue
        lines.append(f"[[{rid}]]: {_full_text_for_record(record)}")
    records_block = "\n\n".join(lines)
    return REVISION_INSTRUCTION.format(draft=draft_text, records_block=records_block)


def self_revise(
    *, client, model_id: str, system_prompt: str, draft_raw_text: str, repository_records: dict[str, dict],
) -> dict:
    """Returns a dict, always usable text on the `revised_text` key even
    on failure - the caller never needs to special-case a blank turn:
      ran: bool - False only when the draft had no tags at all (nothing
        to revise against; the draft is returned unchanged, no call made,
        no cost spent).
      changed: bool - True when the revised text differs from the draft.
      revised_text: str - what the caller should use in place of the draft.
      draft_length / revised_length: int, character counts.
      fallback_reason: str | None - set whenever revised_text IS the
        draft because the revision call failed or returned nothing
        usable ("no_tagged_records", "call_failed:<status>", "empty_response").
      latency_seconds: float - wall-clock time of the revision call itself
        (0.0 when `ran` is False).
      call_outcome: CallOutcome | None - the raw outcome, for the caller
        to record usage/cost against, same shape every other call in
        this module's own turn pipeline already produces; None when no
        call was made.
    """
    draft_length = len(draft_raw_text)
    tagged_record_ids = _tagged_record_ids(draft_raw_text)
    if not tagged_record_ids:
        return {
            "ran": False, "changed": False, "revised_text": draft_raw_text,
            "draft_length": draft_length, "revised_length": draft_length,
            "fallback_reason": "no_tagged_records", "latency_seconds": 0.0, "call_outcome": None,
        }

    revision_message = build_revision_message(
        draft_text=draft_raw_text, tagged_record_ids=tagged_record_ids, repository_records=repository_records,
    )
    start = time.perf_counter()
    outcome: CallOutcome = stream_voice_turn(
        client, model_id, system_prompt=system_prompt, turn_directive=None,
        message=revision_message, history=None, timeout=90.0,
    )
    latency_seconds = time.perf_counter() - start

    if outcome.status != "ok":
        return {
            "ran": True, "changed": False, "revised_text": draft_raw_text,
            "draft_length": draft_length, "revised_length": draft_length,
            "fallback_reason": f"call_failed:{outcome.status}", "latency_seconds": latency_seconds, "call_outcome": outcome,
        }

    revised_text = (outcome.value.text or "").strip()
    if not revised_text:
        return {
            "ran": True, "changed": False, "revised_text": draft_raw_text,
            "draft_length": draft_length, "revised_length": draft_length,
            "fallback_reason": "empty_response", "latency_seconds": latency_seconds, "call_outcome": outcome,
        }

    return {
        "ran": True, "changed": revised_text != draft_raw_text.strip(), "revised_text": revised_text,
        "draft_length": draft_length, "revised_length": len(revised_text),
        "fallback_reason": None, "latency_seconds": latency_seconds, "call_outcome": outcome,
    }
