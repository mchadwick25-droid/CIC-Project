"""
The anachronism bridge (a.k.a. the reverse lexicon) — the third classify-then-
route intercept, mirroring classify_frame_breaker / classify_relational_safety.

This is FACILITATOR behavior and is WORLD-AGNOSTIC: it works the exact same way
for every world, with no per-world authoring. When a participant asks a seated
Representative about a modern theological term that Representative's world never
held, the Facilitator names it as later, gives its modern sense neutrally, and
hands the Representative only the term-free UNDERLYING SUBJECT — never the modern
term. The Representative then answers from its own world's life and terms (or says
honestly that its world held nothing like it). The participant draws the line
between then and now themselves.

What makes it world-agnostic:
- definitions.json is a world-agnostic dictionary (the modern term, its neutral
  sense, its origin_year, and the term-free underlying_subject). No per-world file.
- Whether the bridge fires is DERIVED, not authored: a term bridges only when its
  origin_year postdates the seated world's end year (parsed from the manifest
  `period`). A world that already lived in the term's era just answers normally.
  So "the Trinity" bridges for a pre-Nicaea house-church but not for a post-381
  world - the dates do the work, not a hand-authored disposition.

Design: Ministry/Technology/CiC_Anachronism_Bridge_Spec_V0_1.md
Data:   backend/data/modern_term_bridge/definitions.json  (world-agnostic)
"""

import json
import re
from functools import lru_cache
from pathlib import Path

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

from app.graph.state import ConversationState

_DATA_DIR = Path(__file__).resolve().parents[2] / "data" / "modern_term_bridge"


_CLASSIFIER_PROMPT = """You are classifying a single incoming participant message for the anachronism bridge. This classifier has no Representative-generation role - it only decides routing, and it runs before any Representative is invoked.

Your only job: decide whether the participant is asking about ONE specific MODERN theological term from the list below - a term/concept from a later period of Christianity.

Candidate terms (term_id: the forms a participant might use):
{candidates}

Rules:
- Output the single term_id (exactly as written above) ONLY IF the message is genuinely asking about that term or its concept - "what's your view of X", "do you believe in X", "how does X work", or clearly invoking the concept in other words.
- Output NONE for anything else - above all for a world's OWN native topics (the meal, the letters, who leads, martyrdom, mercy, the desert cell, the covenant, scholarship). Those are not modern terms and must never be bridged.
- A message may mention a word in passing without asking about the modern doctrine - that is NONE. Fire only when the modern term/concept is what the participant actually wants addressed.
- A bare question about a universal Christian concept that merely SHARES A WORD with a modern term's name is NOT the same as asking about that term's specific, distinguishing formula - every era has discussed faith, grace, sin, love, hope; only later eras coined the specific slogans below. Match only when the participant's own words invoke what actually makes the modern term distinct, not just its root word.
  - "What is faith?" -> NONE (a world's own native topic; nothing in the message invokes "alone," "not by works," or any faith-versus-works framing).
  - "Is it faith alone that saves you, and not anything you do?" -> sola-fide (the distinguishing claim - faith excluding works - is actually present).
- When unsure, output NONE. A missed term is caught later by drift monitoring; a wrong interruption is not recoverable.
- Match at most ONE term, the closest. Output nothing but that term_id, or NONE.

Message:
{message}
"""


def _extract_piece(content) -> str:
    if isinstance(content, list):
        return "".join(
            b.get("text", "") for b in content
            if isinstance(b, dict) and b.get("type") == "text"
        )
    return content or ""


@lru_cache(maxsize=1)
def _load_definitions() -> dict:
    """term_id -> definition dict (world-agnostic)."""
    with open(_DATA_DIR / "definitions.json", encoding="utf-8") as f:
        data = json.load(f)
    return {t["term_id"]: t for t in data.get("terms", [])}


@lru_cache(maxsize=None)
def _world_end_year(world_id: str) -> int | None:
    """
    The last year of a world's span, parsed generically from the manifest
    `period` string (e.g. "70–200 CE" -> 200, "c. 382–420 CE" -> 420). Used to
    decide, world-agnostically, whether a term postdates the world. None if the
    world/period can't be read - in which case the bridge treats every dictionary
    term as anachronistic (safe default for the pre-modern worlds shipped so far).
    """
    try:
        from app.world_manifest import get_manifest_entry
        period = get_manifest_entry(world_id).period or ""
        years = [int(y) for y in re.findall(r"\d{1,4}", period)]
        return max(years) if years else None
    except Exception:
        return None


def _is_anachronistic(term: dict, world_id: str) -> bool:
    """A term is anachronistic for a world when it originated AFTER the world's
    span ended. If the world's end year is unknown, default to True (bridge)."""
    end_year = _world_end_year(world_id)
    if end_year is None:
        return True
    return int(term.get("origin_year", 99999)) > end_year


def classify_modern_term(message: str, seated_world_ids: list[str]) -> dict | None:
    """
    Decide whether `message` asks about a modern term anachronistic for the seated
    world. Returns {"term_id", "world_id"} or None (-> normal flow). World-
    agnostic: the candidate list is the whole dictionary; whether it fires is
    derived from the term's origin_year vs. the seated world's end year, not from
    any per-world data. Fails toward None (a false positive has no backstop; a
    false negative is caught by the temporal_bleed drift monitor). Mirrors
    classify_frame_breaker's fail-open discipline.
    """
    try:
        definitions = _load_definitions()
        if not definitions:
            return None
        world_id = seated_world_ids[0] if seated_world_ids else None
        if world_id is None:
            return None

        lines = [
            f"- {tid}: {'; '.join(d.get('display_terms', [tid]))}"
            for tid, d in definitions.items()
        ]
        from app.graph.nodes import CLASSIFIER_MAX_TOKENS, _MONITORING_MODEL, get_monitoring_llm
        from app.usage_logging import log_llm_usage

        llm = get_monitoring_llm(max_tokens=CLASSIFIER_MAX_TOKENS)
        response = llm.invoke([
            SystemMessage(content=_CLASSIFIER_PROMPT.format(
                candidates="\n".join(lines), message=message)),
            HumanMessage(content="Classify the message above."),
        ])
        log_llm_usage("modern_term_bridge", response, _MONITORING_MODEL)
        result = (response.content or "").strip()
        if not result:
            return None

        first = result.split()[0].strip().strip(".:,").lower()
        term_id = None
        if first in definitions:
            term_id = first
        else:
            low = result.lower()
            for tid in definitions:
                if tid in low:
                    term_id = tid
                    break
        if term_id is None:
            return None

        # World-agnostic gate: only bridge if the term postdates the seated world.
        # A world that already lived in the term's era just answers normally.
        if not _is_anachronistic(definitions[term_id], world_id):
            return None
        return {"term_id": term_id, "world_id": world_id}
    except Exception:
        return None


def stream_modern_term_bridge(state: ConversationState, match: dict):
    """
    Beats 1-2 (Facilitator: name-as-later + neutral modern sense), then the
    Representative answers the term-free UNDERLYING SUBJECT in its own world's
    terms - or says honestly its world held nothing like it. World-agnostic: the
    subject and definition come from the shared dictionary; the Representative
    supplies its own world's content. Yields normalized events. The handback
    message injected for the Representative is NEVER persisted to the transcript
    (spec section 5) - only the `complete` messages yielded here are.
    """
    from app.config import settings
    from app.graph.nodes import (
        REACTIVE_TURN_MAX_TOKENS,
        get_llm,
        stream_representative_turn,
    )
    from app.usage_logging import log_llm_usage
    from app.prompts.facilitator_prompts import (
        FACILITATOR_MODERN_TERM_BRIDGE_PROMPT,
        get_representative_message_name,
        get_representative_name,
    )

    definitions = _load_definitions()
    term = definitions[match["term_id"]]
    rep_name = get_representative_name(match["world_id"])
    subject = term.get("underlying_subject", "what your world actually held here")

    handback = (
        f"Then hand back to {rep_name}: say you will ask what {rep_name}'s own world "
        f"actually held about {subject}, in {rep_name}'s own terms - and that if "
        f"{rep_name}'s world had nothing like it, {rep_name} will say so plainly. Do "
        "not answer it yourself."
    )
    display_term = (term.get("display_terms") or [term["term_id"]])[0]
    prompt = FACILITATOR_MODERN_TERM_BRIDGE_PROMPT.format(
        term=display_term,
        modern_sense=term["modern_sense"],
        period=term.get("period_originated", "a later period"),
        representative_name=rep_name,
        handback=handback,
    )

    # --- Beats 1-2: the Facilitator, alone. ---
    yield {"type": "speaker_start", "speaker": "facilitator"}
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
    log_llm_usage("modern_term_bridge_facilitator_turn", usage_chunk,
                  settings.llm_model, session_id=state.session_id)
    yield {"type": "speaker_end", "speaker": "facilitator", "citations": None}
    yield {
        "type": "complete",
        "speaker": "facilitator",
        "message": AIMessage(content=full_text, name="facilitator"),
    }

    # --- Beat 3: the Representative, on the term-free underlying subject. ---
    # The injected message is term-free (never the modern term) and world-agnostic
    # (the Representative supplies its own world's content). It is not persisted.
    rep_message_name = get_representative_message_name(match["world_id"])
    handback_message = (
        f"In your own world, and in your own words: what did your community actually "
        f"hold about {subject}? Answer only from your world's own life and terms. If "
        "your world had nothing like this, say so plainly - that silence is itself "
        "worth naming."
    )
    working_state = ConversationState(
        messages=list(state.messages) + [HumanMessage(content=handback_message)],
        # S3.5 (Pass 1 R9): retrieval searches the extracted SUBJECT, not
        # this handback boilerplate - the bridge already computed the
        # underlying subject deterministically, no extra call needed
        retrieval_query_override=subject,
        phase=state.phase,
        current_speaker="representative",
        current_world_id=match["world_id"],
        turn_count=state.turn_count,
        retrieved_context=state.retrieved_context,
        worlds_at_table=state.worlds_at_table,
        world_capsule_core=state.world_capsule_core,
        permanent_prompt=state.permanent_prompt,
        session_id=state.session_id,
        world_id=state.world_id,
        world_ids=state.world_ids,
    )

    yield {"type": "speaker_start", "speaker": rep_message_name}
    rep_message = None
    for event in stream_representative_turn(working_state, is_reactive=False):
        if event["type"] == "token":
            yield {"type": "token", "speaker": event["speaker"], "text": event["text"]}
        elif event["type"] == "complete":
            rep_message = event["message"]
    yield {
        "type": "speaker_end",
        "speaker": rep_message_name,
        "citations": rep_message.additional_kwargs.get("citations") if rep_message else None,
    }
    if rep_message is not None:
        yield {"type": "complete", "speaker": rep_message_name, "message": rep_message}
