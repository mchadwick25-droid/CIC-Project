"""
The sensed closing sequence — wind-down sensing, an optional resources offer, and
a genuine thank-you/invitation close. Facilitator-only throughout (the
Representative is never invoked), mirroring the frame-breaker intercept shape.

S4.7 (Pass 1 §6.5, the closing-speaker rule): whoever speaks last gains
unearned authority to characterize consensus — so any CONVERSATION-level
closing summary is the Facilitator's to deliver, never a Representative's,
which this module already enforces by construction (every closing turn here
is Facilitator-only). The ROUND-level face of the same rule is the
closing_synthesis table check (nodes.check_closing_synthesis): a
Representative's final-turn synthesis of the table draws a queued
correction rather than standing as the round's last word.

Design: old-tree Ministry Technology/CiC_Sensed_Closing_Sequence_Spec_V0_1.md
Data:   cic/deploy/further_encounter_resources/{<world_id>.json, general.json}

The state machine (state.closing_stage):
    none --wind-down sensed--> anything_else_asked
      anything_else_asked: new question -> none (resume) ; "done" -> resources_offered
      resources_offered:    "yes" -> show resources + close (closed) ; "no" -> close (closed)
Every transition past "anything else?" is gated on the participant's own reply; a
genuine new question at anything_else_asked evaporates the sequence (the
false-positive escape hatch). The explicit-close path (close_requested) is untouched.
"""

import json
from functools import lru_cache
from pathlib import Path

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

from app.graph.state import ConversationState

_RES_DIR = Path(__file__).resolve().parents[3] / "deploy" / "further_encounter_resources"


_WIND_DOWN_PROMPT = """You are classifying a single participant message for whether the conversation is genuinely WINDING DOWN — the participant signalling they are about done — versus still going. This classifier only decides routing; it runs before any turn is generated.

Recent conversation (for context):
{transcript_window}

Latest participant message:
{message}

Output WIND_DOWN only on a clear closure signal:
- Explicit closure language: "thank you, that's helpful", "I think I'm good", "this gave me a lot to think about", "I should go", "that's all I wanted to ask".
- Warm gratitude with NO new question attached, reading as a natural ending.

Output CONTINUE for everything else, including:
- Any actual question, or engagement that opens a new thread.
- A short message that still asks or explores something.
- Thanks that is mid-conversation and clearly leads into more.

Rules:
- Turn count, session length, or depth must NEVER by themselves mean WIND_DOWN. A long, rich, still-curious conversation is not winding down.
- When in doubt, output CONTINUE. Missing a wind-down costs nothing; a wrong WIND_DOWN interrupts a live conversation.

Output exactly one word: WIND_DOWN or CONTINUE."""


_ANYTHING_ELSE_REPLY_PROMPT = """You are interpreting a participant's reply right after the Facilitator asked, at a natural pause, whether there was anything else or if it was a good place to stop.

Participant's reply:
{message}

Output DONE if they indicate nothing else / they're finished / a simple thanks-and-goodbye.
Output CONTINUE if they raise anything new — a question, a topic, any real further engagement (even "actually, yes, one more thing…").

When in doubt, output CONTINUE (never push someone toward the door who might have more to say).

Output exactly one word: DONE or CONTINUE."""


_OFFER_REPLY_PROMPT = """You are interpreting a participant's reply right after the Facilitator OFFERED to point them to some further reading/resources about this world.

Participant's reply:
{message}

Output YES if they accept / want the resources.
Output NO if they decline, or their reply isn't a clear acceptance.

When in doubt, output NO (only show resources on a clear yes).

Output exactly one word: YES or NO."""


def _extract_piece(content) -> str:
    if isinstance(content, list):
        return "".join(
            b.get("text", "") for b in content
            if isinstance(b, dict) and b.get("type") == "text"
        )
    return content or ""


def _one_word(llm_response, default: str) -> str:
    try:
        txt = (llm_response.content or "").strip().upper()
        return txt.split()[0].strip(".:,") if txt else default
    except Exception:
        return default


def classify_wind_down(state: ConversationState, message: str) -> bool:
    """
    True only on a clear wind-down signal. Conservative-high threshold, failing
    toward False (not winding down) — a missed wind-down costs nothing because
    the explicit-close path is untouched, while a false positive interrupts a
    live conversation. Never fires on length/turn-count alone (that rule is in
    the prompt). Mirrors classify_frame_breaker's fail-open discipline.
    """
    try:
        from app.graph.nodes import CLASSIFIER_MAX_TOKENS, _MONITORING_MODEL, get_monitoring_llm
        from app.usage_logging import log_llm_usage

        # a short transcript window for context, same helper the rep path uses
        try:
            from app.graph.nodes import build_public_transcript
            window = build_public_transcript(state) or "(no prior turns)"
        except Exception:
            window = "(unavailable)"

        llm = get_monitoring_llm(max_tokens=CLASSIFIER_MAX_TOKENS)
        resp = llm.invoke([
            SystemMessage(content=_WIND_DOWN_PROMPT.format(
                transcript_window=window, message=message)),
            HumanMessage(content="Classify the message above."),
        ])
        log_llm_usage("wind_down", resp, _MONITORING_MODEL)
        return _one_word(resp, "CONTINUE") == "WIND_DOWN"
    except Exception:
        return False


def _classify_reply(prompt: str, message: str, default: str, positive: str) -> bool:
    try:
        from app.graph.nodes import _MONITORING_MODEL, get_monitoring_llm
        from app.usage_logging import log_llm_usage
        llm = get_monitoring_llm()
        resp = llm.invoke([
            SystemMessage(content=prompt.format(message=message)),
            HumanMessage(content="Classify the reply above."),
        ])
        log_llm_usage("closing_reply_classifier", resp, _MONITORING_MODEL)
        return _one_word(resp, default) == positive
    except Exception:
        return default == positive


def route_closing_stage(state: ConversationState, message: str) -> dict:
    """
    Interpret the participant's reply at the current closing stage and return a
    plan: either {"action": "resume"} (a genuine new question — evaporate the
    sequence, resume normal flow) or {"action": "advance", "to": <stage>,
    "turns": [(kind, ctx), ...]} naming the Facilitator turn(s) to stream.
    """
    stage = state.closing_stage

    if stage == "anything_else_asked":
        done = _classify_reply(_ANYTHING_ELSE_REPLY_PROMPT, message, "CONTINUE", "DONE")
        if not done:
            return {"action": "resume"}
        return {"action": "advance", "to": "resources_offered",
                "turns": [("resources_offer", {})]}

    if stage == "resources_offered":
        yes = _classify_reply(_OFFER_REPLY_PROMPT, message, "NO", "YES")
        if yes:
            return {"action": "advance", "to": "closed",
                    "turns": [("resources_show", {}), ("sensed_close", {})]}
        return {"action": "advance", "to": "closed", "turns": [("sensed_close", {})]}

    # resources_shown / closed / anything unexpected: don't trap the participant.
    return {"action": "resume"}


@lru_cache(maxsize=None)
def _load_resources(world_id: str) -> dict | None:
    path = _RES_DIR / f"{world_id}.json"
    if not path.exists():
        return None
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def _world_label(state: ConversationState) -> str:
    wid = state.world_id or (state.world_ids[0] if state.world_ids else "")
    pack = _load_resources(wid)
    if pack and pack.get("world_offer_label"):
        return pack["world_offer_label"]
    return "this world"


def _resource_list_block(state: ConversationState) -> str:
    wid = state.world_id or (state.world_ids[0] if state.world_ids else "")
    lines = []
    for pack_id in (wid, "general"):
        pack = _load_resources(pack_id)
        if not pack:
            continue
        for r in pack.get("resources", []):
            bits = [r["title"]]
            if r.get("author"):
                bits.append(f"by {r['author']}")
            if r.get("publisher") or r.get("year"):
                bits.append(f"({', '.join(x for x in [r.get('publisher',''), r.get('year','')] if x)})")
            loc = f" [{r['locator']}]" if r.get("locator") else ""
            note = f" — {r['note']}" if r.get("note") else ""
            lines.append(f"- {' '.join(bits)}{loc}{note}")
    return "\n".join(lines) if lines else "(no resources available for this world)"


def stream_closing_turn(state: ConversationState, kind: str):
    """
    Stream one Facilitator-only turn for a closing stage. Yields token/complete
    events (speaker 'facilitator'), same shape the streaming endpoint handles.
    """
    from app.config import settings
    from app.graph.nodes import REACTIVE_TURN_MAX_TOKENS, get_llm
    from app.usage_logging import log_llm_usage
    from app.prompts.facilitator_prompts import (
        FACILITATOR_ANYTHING_ELSE_PROMPT,
        FACILITATOR_RESOURCES_OFFER_PROMPT,
        FACILITATOR_RESOURCES_SHOW_PROMPT,
        # Reused, not reauthored: a sensed close is the same "gracious close,
        # threshold outward" moment as an explicit close_requested close
        # (facilitator_closes in nodes.py) - just reached by a different
        # detection path. Aliased so the kind-dispatch below stays unchanged.
        FACILITATOR_CLOSING_PROMPT as FACILITATOR_SENSED_CLOSE_PROMPT,
    )

    if kind == "anything_else":
        prompt = FACILITATOR_ANYTHING_ELSE_PROMPT
    elif kind == "resources_offer":
        prompt = FACILITATOR_RESOURCES_OFFER_PROMPT.format(world_label=_world_label(state))
    elif kind == "resources_show":
        try:
            from app.graph.nodes import build_public_transcript
            window = build_public_transcript(state) or "(the conversation so far)"
        except Exception:
            window = "(the conversation so far)"
        prompt = FACILITATOR_RESOURCES_SHOW_PROMPT.format(
            world_label=_world_label(state),
            resource_list=_resource_list_block(state),
            transcript_window=window,
        )
    elif kind == "sensed_close":
        prompt = FACILITATOR_SENSED_CLOSE_PROMPT
    else:
        prompt = FACILITATOR_SENSED_CLOSE_PROMPT

    llm = get_llm(max_tokens=REACTIVE_TURN_MAX_TOKENS)
    full_text = ""
    usage_chunk = None
    for chunk in llm.stream([
        SystemMessage(content=prompt),
        HumanMessage(content="Respond as the Facilitator, per your instructions above."),
    ]):
        usage_chunk = chunk if usage_chunk is None else usage_chunk + chunk
        piece = _extract_piece(chunk.content)
        if piece:
            full_text += piece
            yield {"type": "token", "speaker": "facilitator", "text": piece}
    log_llm_usage(f"closing_turn_{kind}", usage_chunk, settings.llm_model,
                  session_id=state.session_id)
    yield {
        "type": "complete",
        "speaker": "facilitator",
        "message": AIMessage(content=full_text, name="facilitator"),
    }
