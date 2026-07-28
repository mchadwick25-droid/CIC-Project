"""LangGraph node functions for The Table conversation."""

import functools
import re
import time
import uuid
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Literal

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

from app.config import settings
from app.graph.state import ConversationState, DriftSignal, RetrievedContext
from app.usage_logging import log_llm_usage
from app.prompts import (
    FACILITATOR_ACUTE_DISTRESS_A1_PROMPT,
    FACILITATOR_ACUTE_DISTRESS_A2_PROMPT,
    FACILITATOR_ACUTE_DISTRESS_CONTINUATION_PROMPT,
    FACILITATOR_BRIDGE_PROMPT,
    FACILITATOR_CLOSING_PROMPT,
    FACILITATOR_FRAME_BREAKER_CLASSIFIER_PROMPT,
    FABRICATION_ADJUDICATION_PROMPT,
    OVER_SETTLING_ADJUDICATION_PROMPT,
    OVER_SETTLING_SCREEN_PROMPT,
    FACILITATOR_FRAME_BREAKER_RESPONSE_PROMPT,
    FACILITATOR_HARMFUL_DYNAMIC_CONTINUATION_PROMPT,
    FACILITATOR_HARMFUL_DYNAMIC_PROMPT,
    FACILITATOR_MONITORING_PROMPT,
    FACILITATOR_RECEPTION_PROMPT,
    FACILITATOR_RELATIONAL_SAFETY_CLASSIFIER_PROMPT,
    FACILITATOR_REROOT_PROMPT,
    build_representative_prompt,
)
from app.prompts.facilitator_prompts import (
    get_facilitator_handoff_prompt,
    get_multi_world_handoff_prompt,
    get_representative_message_name,
    get_representative_name,
)
from app.prompts.confirmed_glosses import find_glosses_used
from app.prompts.representative_prompts import (
    REACTIVE_CONTINUATION_PROMPT,
    REPRESENTATIVE_CONTINUATION_PROMPT,
)
from app.prompts.table_discourse import (
    CROSS_WORLD_VOCABULARY_GUIDANCE,
    OPENING_TURN_LARGE_TABLE_GUIDANCE,
    REACTIVE_TURN_GUIDANCE,
)

# Table size at which even a round's OPENING turn (no one has spoken yet)
# gets held to the same brevity discipline reactive turns already have -
# below this, the reader sees at most one other turn after the opener, but
# at 3+ worlds a full-length opening turn is still followed by two or three
# more turns before the participant reaches the last voice. Mark's own
# framing: "the user can't read 5 pages to get to the last representative."
LARGE_TABLE_THRESHOLD = 3


def _is_large_table_opening(state: ConversationState, is_reactive: bool) -> bool:
    """
    True only for the turn that OPENS a round (is_reactive=False - nothing
    to react to yet) at a table seating LARGE_TABLE_THRESHOLD or more
    worlds. Mutually exclusive with is_reactive by construction - a turn is
    never both continuing an exchange and opening one.
    """
    if is_reactive:
        return False
    world_ids = state.world_ids if len(state.world_ids) > 0 else [state.world_id]
    return len(world_ids) > 1 and len(world_ids) >= LARGE_TABLE_THRESHOLD


from app.rag import LexiconRetriever, StoryRetriever

# Hard cap on a reactive turn's length - keeps a multi-representative round
# feeling like conversational exchange rather than a sequence of speeches,
# backing up the "keep this short" prompt guidance with an actual limit the
# model can't reason its way past. Deliberately loose (not "a few sentences"
# tight) - Anthropic's max_tokens is a hard cutoff, not a target the model
# paces itself against, so a tight cap risks truncating mid-sentence, which
# reads far worse than a turn that's merely longer than ideal. Raised twice:
# 500 -> 700 after a reactive turn combining a story with a direct answer
# hit the ceiling mid-sentence; 700 -> 900 after the "respond, then add your
# own developed view" reactive guidance (naming what was said, working
# through real agreement/disagreement) produced turns that legitimately run
# longer than a short rebuttal while still landing well short of a full
# independent turn (~1000+ tokens).
REACTIVE_TURN_MAX_TOKENS = 900

# A large table's OPENING turn (see _is_large_table_opening above) is the
# round's one direct answer to the actual question - Mark's own refinement:
# it can run 20-30% longer than a reactive beat, since it's carrying the
# substantive answer everyone else at the table is about to react to, but
# it is not the old uncapped "full independent turn" either. 25% over
# REACTIVE_TURN_MAX_TOKENS, not freeform.
OPENING_TURN_MAX_TOKENS = int(REACTIVE_TURN_MAX_TOKENS * 1.25)

# The PRIMARY Representative turn - a direct, substantive answer to the
# participant's actual question, not a reactive beat and not a large-table
# opening (see the turn_max_tokens branches in representative_engages/
# stream_representative_turn) - had NO token cap at all until this was
# added: real live testing (a tester's own "the first answers were too
# long" report, independently confirmed live) found this path relies
# entirely on prompt-level guidance (representative_prompts.py's "A Turn
# Has a Measure" section: "most turns are one to two short paragraphs, and
# a turn should almost never exceed three") with no structural enforcement
# behind it - the same class of gap REACTIVE_TURN_MAX_TOKENS was added to
# close for reactive turns, just never carried over to the primary-turn
# path. Applies to every primary (non-reactive, non-large-table-opening)
# turn on every round, not just a conversation's first turn -
# is_reactive/large_table_opening are both recomputed fresh per call, so
# single-world "Deep Interview" mode (where is_reactive is always False)
# and every "Compare Worlds" round's opening speaker are covered uniformly
# by this same branch.
#
# Value chosen from real-API tuning (2026-07, Chloe/post-apostolic-house-
# church, both fresh questions and turns deep into a real conversation),
# not a guess: fully uncapped, real responses landed consistently at
# ~240-300 words (already past the prompt's own "one to two paragraphs"
# target, sitting right at its "almost never exceed three" ceiling on
# every sample - the "prompt guidance alone doesn't reliably hold" failure
# mode get_llm's own docstring already documents, here manifesting as no
# budget at all to enforce it). Caps tight enough to actually force
# shorter output (400 tokens and below) truncated real responses mid-
# sentence on most samples - explicitly the worse failure mode per this
# fix's own priority (a complete, slightly-longer answer beats a chopped-
# off shorter one). 460 still truncated one sample in five. 500 and 550
# both ran clean (0 truncations) across the full real test set; 550 is
# kept for extra margin against production traffic's real variance beyond
# this test's small sample. At this value the cap functions mainly as a
# genuine CEILING against a runaway/outlier turn (whatever produced the
# live "four-to-six paragraph" case), not as something that reliably
# compresses the ALREADY-uncapped typical ~250-290-word response down to
# "one to two focused paragraphs" - going tight enough to force that
# reliably was the same range that started truncating. Raised from 550 to
# 1200 (Mark's own call, 2026-07-24/25): a response running long is far
# less noticeable to a participant than one cut off mid-sentence, so the
# ceiling is set to protect against runaway generation, not to hold the
# typical case to a specific length - that shaping work now lives in
# _HOW_YOU_ENGAGE's own guidance (representative_prompts.py), folded in
# from what was previously a separate PRIMARY_TURN_GUIDANCE block.
PRIMARY_TURN_MAX_TOKENS = 1200

# Hard cap for the blocking pre-response classifiers (frame-breaker,
# epistemology-bridge, relational-safety, modern-term, wind-down) - every
# one of them is specified to answer in a single word or a short
# CATEGORY[:TAG] line (see each classifier's own prompt), so this only
# needs headroom for the longest real response shape: a relational-safety
# multi-tag line like "HARMFUL_DYNAMIC_SIGNAL:CONFIDANT_LANGUAGE+
# AFFIRMATION_DEPENDENCE+RETURN_COMPULSION" (roughly 25-35 tokens through a
# BPE tokenizer). Set generously above that estimate - a truncated
# classification is not a crash (each classifier's own fail-open parsing
# just yields fewer parsed tags), but relational-safety is safety-critical
# enough that the extra headroom costs nothing worth trading away. Passed
# through to get_monitoring_llm the same way REACTIVE_TURN_MAX_TOKENS is
# passed to get_llm - see that function's docstring for why max_tokens also
# disables extended thinking.
CLASSIFIER_MAX_TOKENS = 60

# The model get_monitoring_llm actually constructs for the anthropic
# provider (see that function, below) - kept as its own constant purely so
# every log_llm_usage() call for a classifier/monitoring call can log the
# real model string without duplicating the literal at each call site, not
# because get_monitoring_llm itself reads this constant (it does not - the
# two are independent and must be kept in sync by hand if the model ever
# changes).
_MONITORING_MODEL = "claude-haiku-4-5-20251001"


def get_llm(max_tokens: int | None = None):
    """Get the configured LLM.

    max_tokens: hard cap on response length. Used to actually enforce short
    reactive turns in a multi-representative round - prompt instructions
    alone ("keep this short") are a nudge the model doesn't reliably follow
    once a topic is substantive, so a token cap backs it up structurally.

    When max_tokens is set, extended thinking is explicitly disabled. Live
    testing found this model emits an interleaved thinking block by default
    on every call (present even with no explicit thinking config), and its
    length varies unpredictably per generation - when it runs long, it can
    consume most of a tight max_tokens budget before any visible text is
    written, causing the response to hit the cap and cut off mid-sentence
    with only a fraction of the intended length actually said. Disabling
    thinking for capped (reactive-turn) calls makes the visible-text budget
    the whole budget, which is what a short conversational reactive beat
    actually needs - full-length uncapped calls are left alone since they
    have no tight ceiling for thinking to crowd out.
    """
    if settings.mock_llm:
        from app.mock_llm import MockChatModel
        return MockChatModel()

    if settings.llm_provider == "anthropic":
        from langchain_anthropic import ChatAnthropic

        kwargs = {"model": settings.llm_model, "anthropic_api_key": settings.anthropic_api_key}
        if max_tokens:
            kwargs["max_tokens"] = max_tokens
            kwargs["thinking"] = {"type": "disabled"}
        return ChatAnthropic(**kwargs)
    else:
        from langchain_openai import ChatOpenAI

        kwargs = {"model": settings.llm_model, "openai_api_key": settings.openai_api_key}
        if max_tokens:
            kwargs["max_tokens"] = max_tokens
        return ChatOpenAI(**kwargs)


def new_request_id() -> str:
    """
    Short, human-scannable ID minted once per incoming HTTP request (at the
    top of each endpoint in main.py) and threaded down through every
    Representative-turn call it triggers, so every LLM call this request
    causes can be tied back to it in the log.
    """
    return uuid.uuid4().hex[:8]


def _log_llm_call(request_id: str | None, session_id: str | None, world_id: str | None,
                   speaker: str | None, text: str) -> None:
    """
    Trace-log a completed Representative-turn LLM call: request/session/
    world/speaker identity, timing, and a length + head/tail fingerprint of
    the response text (not the full text, to keep this cheap to scan).

    Added 2026-07-20 after a live-tested response (Theon, in a real
    multi-world table) came back from the API containing a fully unrelated
    block with no connection to this project - confirmed real via the raw
    response content, independently caught by a blind Opus-graded review,
    but NOT reproduced under two rounds of deliberate concurrent-load
    testing, and the application code on this path read clean on direct
    audit. Root cause was not established (see the System Hub Decision
    Log, 2026-07-20, "content-isolation investigation"). This is the
    recommended next step from that investigation: if it recurs, the
    logged request boundaries let it be traced directly instead of
    reconstructed after the fact from a saved transcript. Deliberately
    cheap (one print line, no new storage/service) - upgrade only if a
    recurrence actually needs deeper tracing than this provides.
    """
    head = text[:80].replace("\n", " ")
    tail = text[-80:].replace("\n", " ") if len(text) > 80 else ""
    print(
        f"[llm_trace] req={request_id} session={session_id} world={world_id} "
        f"speaker={speaker} t={time.time():.3f} len={len(text)} "
        f"head={head!r} tail={tail!r}"
    )


def get_monitoring_llm(max_tokens: int | None = None):
    """Get a faster LLM for monitoring (invisible operations) and for the
    blocking pre-response classifiers (frame-breaker, epistemology-bridge,
    relational-safety, modern-term, wind-down) - claude-haiku-4-5 instead of
    the full settings.llm_model those classifiers used to share with actual
    Representative/Facilitator generation.

    max_tokens: same contract as get_llm's own max_tokens parameter - a hard
    cap on response length, with extended thinking explicitly disabled
    whenever it's set. See get_llm's docstring for why: a live-tested model
    in this codebase was found to emit an interleaved thinking block by
    default even with no explicit thinking config, and a tight max_tokens
    budget lets that block consume most of it before any visible text is
    written. The classifiers this is built for all answer in a single word
    or a short CATEGORY[:TAG] line (see CLASSIFIER_MAX_TOKENS), so the same
    risk applies to them and gets the same fix. Calls with no max_tokens
    (the existing invisible-monitoring callers) are left exactly as before.
    """
    if settings.mock_llm:
        from app.mock_llm import MockChatModel
        return MockChatModel()

    if settings.llm_provider == "anthropic":
        from langchain_anthropic import ChatAnthropic

        kwargs = {
            "model": "claude-haiku-4-5-20251001",
            "anthropic_api_key": settings.anthropic_api_key,
        }
        if max_tokens:
            kwargs["max_tokens"] = max_tokens
            kwargs["thinking"] = {"type": "disabled"}
        return ChatAnthropic(**kwargs)
    else:
        from langchain_openai import ChatOpenAI

        kwargs = {
            "model": "gpt-4o-mini",
            "openai_api_key": settings.openai_api_key,
        }
        if max_tokens:
            kwargs["max_tokens"] = max_tokens
        return ChatOpenAI(**kwargs)


# Per-world retrievers cache
_retrievers: dict[str, LexiconRetriever] = {}
_story_retrievers: dict[str, StoryRetriever] = {}


def get_retriever(world_id: str = "syriac-edessa-nisibis") -> LexiconRetriever:
    """Get or create the lexicon retriever for a specific world."""
    global _retrievers
    if world_id not in _retrievers:
        _retrievers[world_id] = LexiconRetriever(world_id=world_id)
    return _retrievers[world_id]


def get_story_retriever(world_id: str = "syriac-edessa-nisibis") -> StoryRetriever:
    """Get or create the story retriever for a specific world."""
    global _story_retrievers
    if world_id not in _story_retrievers:
        _story_retrievers[world_id] = StoryRetriever(world_id=world_id)
    return _story_retrievers[world_id]


def facilitator_receives(state: ConversationState) -> dict:
    """
    Facilitator welcomes the participant with a warm, brief greeting.

    This is the first visible interaction - the participant has just arrived.
    """
    llm = get_llm()

    response = llm.invoke([
        SystemMessage(content=FACILITATOR_RECEPTION_PROMPT),
        HumanMessage(content="A new participant has arrived at The Table."),
    ])
    log_llm_usage("facilitator_reception", response, settings.llm_model,
                  session_id=state.session_id)

    return {
        "messages": [AIMessage(content=response.content, name="facilitator")],
        "phase": "handoff",
        "current_speaker": "facilitator",
    }


def stream_facilitator_bridge(state: ConversationState):
    """
    Stream a brief Facilitator turn back toward the participant after a
    multi-representative round.

    When two or more representatives have just spoken - genuinely to each
    other as well as to the participant - the conversation can start to feel
    like something the participant is watching rather than something they
    are in. This is a short, deliberate handoff back: not a summary of what
    was said, just making it plain the table is listening for the
    participant now. Yields the same token/complete event shape as
    `stream_representative_turn` so callers can treat it identically.
    """
    llm = get_llm(max_tokens=REACTIVE_TURN_MAX_TOKENS)

    public_transcript = build_public_transcript(state)

    full_text = ""
    usage_chunk = None
    for chunk in llm.stream([
        SystemMessage(content=FACILITATOR_BRIDGE_PROMPT),
        HumanMessage(content=f"Here is what was just said at the table:\n\n{public_transcript}"),
    ]):
        usage_chunk = chunk if usage_chunk is None else usage_chunk + chunk
        content = chunk.content
        if isinstance(content, list):
            piece = "".join(
                block.get("text", "")
                for block in content
                if isinstance(block, dict) and block.get("type") == "text"
            )
        else:
            piece = content

        if piece:
            full_text += piece
            yield {"type": "token", "speaker": "facilitator", "text": piece}

    log_llm_usage("facilitator_bridge", usage_chunk, settings.llm_model,
                  session_id=state.session_id)
    yield {
        "type": "complete",
        "speaker": "facilitator",
        "message": AIMessage(content=full_text, name="facilitator"),
        "current_world_id": state.current_world_id,
        "retrieved_context": None,
    }


def classify_frame_breaker(message: str) -> bool:
    """
    Decide whether an incoming participant message is a frame-breaker -
    a direct or adversarial question about a Representative's own
    construction, nature, or grammar - before any Representative ever sees
    it.

    Per Facilitator Governance V3.6 Section 10 (Self-Narration, CO-019) and
    Section 12 (frame-breaker trigger): a Representative's own prompt text
    cannot reliably hold this line alone under sustained pressure, so the
    routing decision is decoupled into its own narrow classifier call rather
    than asked of the same pass that would generate Representative content.
    This is that classifier - it has no Representative-generation role and
    sees only the raw message, never the conversation's substance.

    Fails open to False (treat as substantive) on any parse ambiguity or
    error - a missed frame-breaker falls back to the in-line SELF_NARRATION
    monitoring signal as a second layer; a false positive would incorrectly
    deny the participant a real answer, which is the worse failure mode of
    the two.

    That fallback was fiction until 2026-07-16: this docstring named a
    second layer that did not exist - FACILITATOR_MONITORING_PROMPT had no
    self-narration signal and valid_signals had no entry for it, so the
    deliberate fail-open here rested on a backstop that was never built, and
    a Representative volunteering self-narration unprompted went unwatched.
    Governance V3.6 Section 10 requires both halves: the frame-breaker
    classifier for pressed self-narration (this function), and monitoring for
    the milder unprompted case, "corrected the same way as any other signal
    in this section." The monitoring half now exists.
    """
    llm = get_monitoring_llm(max_tokens=CLASSIFIER_MAX_TOKENS)
    try:
        response = llm.invoke([
            SystemMessage(content=FACILITATOR_FRAME_BREAKER_CLASSIFIER_PROMPT.format(message=message)),
            HumanMessage(content="Classify the message above."),
        ])
        log_llm_usage("frame_breaker", response, _MONITORING_MODEL)
        result = response.content.strip().upper()
        return result.startswith("FRAME_BREAKER")
    except Exception:
        return False


def stream_frame_breaker_response(state: ConversationState):
    """
    Stream the Facilitator's threshold-voice answer to a frame-breaker
    question - "surface, answer, recede" per Governance V3.6 Section 12.

    This is a Facilitator-only call: no Representative's Permanent Prompt is
    ever invoked for this turn, so a Representative is structurally never
    shown a message classified as a frame-breaker and cannot attempt to
    answer one in character. Yields the same token/complete event shape as
    `stream_representative_turn`/`stream_facilitator_bridge` so callers can
    treat it identically.
    """
    llm = get_llm(max_tokens=REACTIVE_TURN_MAX_TOKENS)

    last_human_message = ""
    for msg in reversed(state.messages):
        if isinstance(msg, HumanMessage):
            last_human_message = msg.content
            break

    # FLAG-019 fix (2026-07-28): the frame answer is conditioned on the
    # ACTUAL table composition - seated voices by name and world - so its
    # examples can never confabulate worlds this project does not carry.
    from app.prompts.facilitator_prompts import REPRESENTATIVE_INFO
    seated_ids = state.world_ids if state.world_ids else [state.world_id]
    seated_lines = []
    for wid in seated_ids:
        info = REPRESENTATIVE_INFO.get(wid) or {}
        seated_lines.append(f"- {info.get('name', wid)} - the voice of {wid}")
    table_composition = (
        "Seated at THIS table:\n" + "\n".join(seated_lines) +
        "\nThe project's worlds are early-Christian formation traditions "
        "only; no other traditions, eras, or named figures exist as voices "
        "here.")

    full_text = ""
    usage_chunk = None
    for chunk in llm.stream([
        SystemMessage(content=FACILITATOR_FRAME_BREAKER_RESPONSE_PROMPT.format(
            message=last_human_message, table_composition=table_composition)),
        HumanMessage(content="Respond as the Facilitator, per your instructions above."),
    ]):
        usage_chunk = chunk if usage_chunk is None else usage_chunk + chunk
        content = chunk.content
        if isinstance(content, list):
            piece = "".join(
                block.get("text", "")
                for block in content
                if isinstance(block, dict) and block.get("type") == "text"
            )
        else:
            piece = content

        if piece:
            full_text += piece
            yield {"type": "token", "speaker": "facilitator", "text": piece}

    log_llm_usage("frame_breaker_response", usage_chunk, settings.llm_model,
                  session_id=state.session_id)
    yield {
        "type": "complete",
        "speaker": "facilitator",
        "message": AIMessage(content=full_text, name="facilitator"),
        "current_world_id": state.current_world_id,
        "retrieved_context": None,
    }


# Relational-safety accumulator: Harmful Dynamic (Track B) fires once these
# many CONFIDANT_LANGUAGE/AFFIRMATION_DEPENDENCE tags have pooled, or after
# one RETURN_COMPULSION tag. Starting values per the design doc's own
# calibration disclosure - not a validated threshold.
_HARMFUL_DYNAMIC_POOLED_THRESHOLD = 2
_HARMFUL_DYNAMIC_POOLED_TAGS = {"CONFIDANT_LANGUAGE", "AFFIRMATION_DEPENDENCE"}
_HARMFUL_DYNAMIC_IMMEDIATE_TAGS = {"RETURN_COMPULSION"}

# Consecutive non-signal turns required to clear an active track. This
# implementation's own calibration choice (see state.py's field comment) -
# not specified numerically by the design doc.
_DEESCALATION_TURNS_REQUIRED = 2


def classify_relational_safety(state: ConversationState, message: str) -> dict:
    """
    Decide whether an incoming participant message carries an Acute Distress
    or Harmful Dynamic signal, per Facilitator Governance V3.6 Section 12 as
    operationalized in CiC_L3D_AcuteDistress_HarmfulDynamic_Mechanism_
    Proposal_DRAFT.md Section 4.2.

    Same architectural discipline as classify_frame_breaker: a narrow
    classifier call with no Representative-generation role, run before any
    Representative is invoked. Returns a dict with "category" (one of
    NO_SIGNAL, HISTORICAL_OTHERNESS_DISORIENTATION, ACUTE_DISTRESS,
    HARMFUL_DYNAMIC_SIGNAL, AMBIGUOUS_LOW_CONFIDENCE) and, where applicable,
    "severity" (A1/A2 for ACUTE_DISTRESS) or "tag" (for HARMFUL_DYNAMIC_
    SIGNAL/AMBIGUOUS_LOW_CONFIDENCE).

    Fails open to NO_SIGNAL on any parse ambiguity or error, for the same
    reason classify_frame_breaker fails open to False: a missed signal on a
    single turn is caught by the sustained-attention re-evaluation on
    subsequent turns if the pattern is real, whereas a classifier that
    throws and blocks the whole turn is a worse failure for every other
    conversation that has nothing to do with relational safety.
    """
    llm = get_monitoring_llm(max_tokens=CLASSIFIER_MAX_TOKENS)
    transcript_window = build_public_transcript(state)
    try:
        response = llm.invoke([
            SystemMessage(content=FACILITATOR_RELATIONAL_SAFETY_CLASSIFIER_PROMPT.format(
                transcript_window=transcript_window or "(no prior turns)",
                track_a_active=state.track_a_active,
                track_b_active=state.track_b_active,
                accumulated_tags=state.relational_safety_tags or "(none)",
                message=message,
            )),
            HumanMessage(content="Classify the message above."),
        ])
        log_llm_usage("relational_safety", response, _MONITORING_MODEL)
        result = response.content.strip().upper()
        if ":" in result:
            category, detail = result.split(":", 1)
            category = category.strip()
            detail = detail.strip()
        else:
            category, detail = result.strip(), None

        valid_categories = {
            "NO_SIGNAL",
            "HISTORICAL_OTHERNESS_DISORIENTATION",
            "ACUTE_DISTRESS",
            "HARMFUL_DYNAMIC_SIGNAL",
            "AMBIGUOUS_LOW_CONFIDENCE",
        }
        if category not in valid_categories:
            return {"category": "NO_SIGNAL"}

        out = {"category": category}
        if category == "ACUTE_DISTRESS":
            out["severity"] = detail if detail in ("A1", "A2") else "A1"
        elif category in ("HARMFUL_DYNAMIC_SIGNAL", "AMBIGUOUS_LOW_CONFIDENCE"):
            # The classifier prompt's own worked examples show a single
            # message legitimately carrying more than one tag (e.g.
            # CONFIDANT_LANGUAGE + AFFIRMATION_DEPENDENCE + RETURN_COMPULSION
            # in one line), even though the response-format spec only shows
            # a single-tag example. Parse every known tag token out of
            # `detail` rather than treating it as one opaque string - the
            # same compound-label failure mode already found once this
            # session in the drift-signal whitelist.
            known_tags = {
                "CONFIDANT_LANGUAGE",
                "AFFIRMATION_DEPENDENCE",
                "RETURN_COMPULSION",
                "DISTRESS_ADJACENT",
            }
            raw_tokens = re.split(r"[+,/]|\bAND\b", detail or "")
            parsed_tags = [t.strip() for t in raw_tokens if t.strip() in known_tags]
            if not parsed_tags and detail:
                parsed_tags = [t for t in known_tags if t in detail]
            out["tags"] = parsed_tags
            out["tag"] = parsed_tags[0] if parsed_tags else detail
        return out
    except Exception:
        return {"category": "NO_SIGNAL"}


def update_relational_safety_state(state: ConversationState, classification: dict) -> dict:
    """
    Apply a relational-safety classification to session state - pure logic,
    no LLM call. Returns the state field updates to apply (mirrors the
    dict-return convention every other node function in this module uses).

    Implements: Track A firing/escalation/sustained-attention (design doc
    Section 4.4), Track B's signal accumulator and threshold (Section 4.3),
    and de-escalation clearing for both tracks (this implementation's own
    calibration - see state.py).
    """
    category = classification["category"]
    updates: dict = {}

    is_signal_bearing = category in (
        "HISTORICAL_OTHERNESS_DISORIENTATION",
        "ACUTE_DISTRESS",
        "HARMFUL_DYNAMIC_SIGNAL",
    )

    # --- Track A (Acute Distress) ---
    if category == "ACUTE_DISTRESS":
        severity = classification.get("severity", "A1")
        updates["track_a_active"] = True
        # Escalation: only overwrite severity upward (A1 -> A2), never down -
        # a later A1-consistent turn during an active A2 session is still a
        # continuation of the more severe state, not a downgrade.
        current_severity = state.track_a_severity
        if current_severity == "A2" or severity == "A2":
            updates["track_a_severity"] = "A2"
        else:
            updates["track_a_severity"] = "A1"
        updates["relational_safety_deescalation_count"] = 0

    # --- Track B (Harmful Dynamic) ---
    # A single message can legitimately carry more than one tag (see
    # classify_relational_safety's parsing) - treat every parsed tag from
    # this turn as its own accumulator entry, not one compound entry.
    tags_this_turn = classification.get("tags") or (
        [classification["tag"]] if classification.get("tag") else []
    )
    if category == "HARMFUL_DYNAMIC_SIGNAL" and tags_this_turn:
        new_tags = list(state.relational_safety_tags) + tags_this_turn
        updates["relational_safety_tags"] = new_tags
        updates["relational_safety_deescalation_count"] = 0

        if any(t in _HARMFUL_DYNAMIC_IMMEDIATE_TAGS for t in tags_this_turn):
            updates["track_b_active"] = True
        else:
            pooled_count = sum(1 for t in new_tags if t in _HARMFUL_DYNAMIC_POOLED_TAGS)
            if pooled_count >= _HARMFUL_DYNAMIC_POOLED_THRESHOLD:
                updates["track_b_active"] = True
    elif category == "AMBIGUOUS_LOW_CONFIDENCE" and tags_this_turn:
        # Logged as a weak signal per the design doc, but does not by itself
        # cross the Track B threshold and does not reset the de-escalation
        # counter - an ambiguous turn is not itself evidence against
        # de-escalation the way a clear signal is.
        updates["relational_safety_tags"] = list(state.relational_safety_tags) + tags_this_turn

    # --- De-escalation (applies while a track is active and this turn
    # carries no signal at all - NO_SIGNAL only; HISTORICAL_OTHERNESS_
    # DISORIENTATION and AMBIGUOUS_LOW_CONFIDENCE are deliberately treated as
    # non-clearing, since both can co-occur with genuine ongoing distress) ---
    if (state.track_a_active or state.track_b_active) and category == "NO_SIGNAL":
        count = state.relational_safety_deescalation_count + 1
        updates["relational_safety_deescalation_count"] = count
        if count >= _DEESCALATION_TURNS_REQUIRED:
            updates["track_a_active"] = False
            updates["track_a_severity"] = None
            updates["track_b_active"] = False
            updates["relational_safety_tags"] = []
            updates["relational_safety_deescalation_count"] = 0
    elif not is_signal_bearing and category != "NO_SIGNAL":
        # AMBIGUOUS_LOW_CONFIDENCE with no active track and no threshold
        # crossed - nothing further to update beyond the tag logging above.
        pass

    return updates


def relational_safety_should_fire(state: ConversationState, classification: dict, updates: dict) -> bool:
    """
    Decide whether this turn routes to a Facilitator-only relational-safety
    response instead of the Representative.

    Fires when: (a) this turn's own classification is ACUTE_DISTRESS or
    crosses the Track B threshold, or (b) sustained attention is active from
    a prior turn (track_a_active or track_b_active, after update_relational_
    safety_state's de-escalation check has already run) - per Section 4.4,
    the Representative is withheld for the remainder of a heightened-
    attention state, not only on the exact turn that first fired it.
    """
    if classification["category"] == "ACUTE_DISTRESS":
        return True
    if updates.get("track_b_active") and not state.track_b_active:
        return True
    # Sustained attention: check the state AFTER de-escalation updates are
    # applied, not the raw pre-update flags.
    resolved_track_a = updates.get("track_a_active", state.track_a_active)
    resolved_track_b = updates.get("track_b_active", state.track_b_active)
    return bool(resolved_track_a or resolved_track_b)


def _describe_accumulated_pattern(tags: list[str]) -> str:
    """
    Turn the Track B accumulator's tags into the light, non-diagnostic
    pattern description the Harmful Dynamic template's slot expects -
    naming what the accumulator actually indicates, not inventing detail
    beyond it (design doc Section 5.2's own "[what the accumulator's tags
    suggest]" instruction).
    """
    descriptions = []
    if "CONFIDANT_LANGUAGE" in tags:
        descriptions.append("the place you come to be listened to")
    if "AFFIRMATION_DEPENDENCE" in tags:
        descriptions.append("something you look forward to more than other things in your day")
    if "RETURN_COMPULSION" in tags:
        descriptions.append("something you feel you need to come back to")
    if not descriptions:
        return "a place you're leaning on the way you might lean on a friend or a counselor"
    return " and ".join(descriptions)


def stream_relational_safety_response(
    state: ConversationState,
    classification: dict,
    updates: dict,
    pre_track_a_active: bool = None,
    pre_track_a_severity: str = None,
    pre_track_b_active: bool = None,
):
    """
    Stream the Facilitator's threshold-voice response to a firing relational-
    safety turn, per the corrected design (no dual-voice, no named resource,
    non-directive check-in only - CiC_L3D_AcuteDistress_HarmfulDynamic_
    Mechanism_Proposal_DRAFT.md Section 5, as revised and live-tested
    2026-07-13 in CiC_W1_Phase5_RelationalSafety_LiveAdversarialTest_
    CorrectedDesign_Round1/2.md).

    This is a Facilitator-only call: no Representative's Permanent Prompt is
    ever invoked for this turn, so a Representative is structurally never
    shown a message once a track fires - same withholding discipline as
    stream_frame_breaker_response. Yields the same token/complete event
    shape so callers can treat it identically.

    pre_track_a_active/pre_track_a_severity/pre_track_b_active must be the
    session's track state from BEFORE this turn's `updates` were applied -
    they are what distinguishes a fresh fire (full check-in script) from a
    continuation (light-touch acknowledgment). Callers that have already
    applied `updates` onto `state` before calling this function MUST pass
    these explicitly rather than relying on `state.track_a_active` etc.,
    which would otherwise already reflect the post-update value and make
    every fresh fire misread as a continuation.
    """
    llm = get_llm(max_tokens=REACTIVE_TURN_MAX_TOKENS)
    representative_name = get_representative_name(state.current_world_id or state.world_id)

    last_human_message = ""
    for msg in reversed(state.messages):
        if isinstance(msg, HumanMessage):
            last_human_message = msg.content
            break

    was_track_a_active = state.track_a_active if pre_track_a_active is None else pre_track_a_active
    was_track_a_severity = state.track_a_severity if pre_track_a_severity is None else pre_track_a_severity
    was_track_b_active = state.track_b_active if pre_track_b_active is None else pre_track_b_active

    resolved_track_a = updates.get("track_a_active", was_track_a_active)
    resolved_track_b = updates.get("track_b_active", was_track_b_active)
    category = classification["category"]

    if category == "ACUTE_DISTRESS":
        severity = updates.get("track_a_severity", was_track_a_severity) or classification.get("severity", "A1")
        is_fresh_fire = not was_track_a_active or (
            severity == "A2" and was_track_a_severity != "A2"
        )
        if is_fresh_fire and severity == "A2":
            prompt = FACILITATOR_ACUTE_DISTRESS_A2_PROMPT.format(
                message=last_human_message, representative_name=representative_name,
            )
        elif is_fresh_fire:
            prompt = FACILITATOR_ACUTE_DISTRESS_A1_PROMPT.format(
                message=last_human_message, representative_name=representative_name,
            )
        else:
            prompt = FACILITATOR_ACUTE_DISTRESS_CONTINUATION_PROMPT.format(message=last_human_message)
    elif resolved_track_b and not was_track_b_active:
        prompt = FACILITATOR_HARMFUL_DYNAMIC_PROMPT.format(
            representative_name=representative_name,
            accumulated_pattern_description=_describe_accumulated_pattern(
                updates.get("relational_safety_tags", state.relational_safety_tags)
            ),
        )
    elif resolved_track_b:
        prompt = FACILITATOR_HARMFUL_DYNAMIC_CONTINUATION_PROMPT.format(message=last_human_message)
    else:
        # Sustained attention with no fresh escalation on either track -
        # default to the lighter continuation form.
        prompt = FACILITATOR_ACUTE_DISTRESS_CONTINUATION_PROMPT.format(message=last_human_message)

    full_text = ""
    usage_chunk = None
    for chunk in llm.stream([
        SystemMessage(content=prompt),
        HumanMessage(content="Respond as the Facilitator, per your instructions above."),
    ]):
        usage_chunk = chunk if usage_chunk is None else usage_chunk + chunk
        content = chunk.content
        if isinstance(content, list):
            piece = "".join(
                block.get("text", "")
                for block in content
                if isinstance(block, dict) and block.get("type") == "text"
            )
        else:
            piece = content

        if piece:
            full_text += piece
            yield {"type": "token", "speaker": "facilitator", "text": piece}

    log_llm_usage("relational_safety_response", usage_chunk, settings.llm_model,
                  session_id=state.session_id)
    yield {
        "type": "complete",
        "speaker": "facilitator",
        "message": AIMessage(content=full_text, name="facilitator"),
        "current_world_id": state.current_world_id,
        "retrieved_context": None,
    }


def facilitator_handoff(state: ConversationState) -> dict:
    """
    Facilitator introduces the representative(s) and steps back.

    This transitions the conversation to the representative(s).
    Supports both single-world and multi-world tables.
    """
    llm = get_llm()

    # Check if multi-world table
    world_ids = state.world_ids if len(state.world_ids) > 0 else [state.world_id]
    is_multi_world = len(world_ids) > 1

    if is_multi_world:
        handoff_prompt = get_multi_world_handoff_prompt(world_ids)
        instruction = "Please introduce the representatives gathered at The Table."
    else:
        handoff_prompt = get_facilitator_handoff_prompt(state.world_id)
        instruction = "Please introduce the representative."

    response = llm.invoke([
        SystemMessage(content=handoff_prompt),
        HumanMessage(content=instruction),
    ])
    log_llm_usage("facilitator_handoff", response, settings.llm_model,
                  session_id=state.session_id)

    return {
        "messages": [AIMessage(content=response.content, name="facilitator")],
        "phase": "active_encounter",
        "current_speaker": "representative",
        "current_world_id": world_ids[0],  # First representative starts
    }


# S4.4a: the public-transcript window's shape (see build_public_transcript's
# docstring). The recent window keeps the historical depth of 10; the
# stable prefix pins the participant's opening frame and the first answer.
TRANSCRIPT_STABLE_PREFIX = 2
TRANSCRIPT_RECENT_WINDOW = 10


def build_public_transcript(state: ConversationState, exclude_world_id: str = None) -> str:
    """
    Build the public transcript - the record of what has been spoken at The Table.

    The public transcript is what Representatives share with each other.
    Each Representative sees what others have said, but not their inner formation.
    This is how Representatives encounter each other: through words spoken at the Table.

    S4.2 (Pass 1 §6.7): the transcript is a deterministic render of the
    specified data shape - the ordered log of spoken events (speaker,
    text, designated addressee where one exists; see
    app.graph.events.spoken_events_from_messages).

    S4.5 (Pass 1 §6.6): FACILITATOR TURNS ENTER THE RENDER. The
    constitutional line is "only spoken words cross" - the Facilitator's
    words are spoken; excluding them was never what the boundary
    required, and it silently broke the bridge's own repair mechanism (a
    Representative saw answers to questions that no longer existed in
    the record) and made a held crisis read as an unanswered one (the
    FLAG-008 window). Bridge-reframe entries (the persisted "question
    actually asked") render as Facilitator lines too - every
    Representative reads the same reframed question, ending the
    two-treatments asymmetry.

    S4.4a (Pass 1 §6.2 item 3): the window moves from a naive
    last-10-lines slice to BLOCK TRUNCATION WITH A STABLE PREFIX - the
    conversation's opening turns (the participant's framing and the
    first answer) stay pinned, the middle is elided in whole blocks with
    an explicit marker, and the recent window keeps the old depth. The
    old sliding slice silently dropped the conversation's framing the
    moment a table got talkative, and shifted on every turn; the stable
    prefix is both the long-context resource the selector's measured
    strength depends on and the cached-prefix rule applied to this
    window's shape. Conversations short enough to fit are rendered
    whole, exactly as before.
    """
    from app.graph.events import spoken_events_from_messages

    transcript_lines = []
    for event in spoken_events_from_messages(state.messages):
        if event["speaker"] == "participant":
            transcript_lines.append(f"Participant: {event['text']}")
        elif event["speaker"] == "facilitator":
            transcript_lines.append(f"Facilitator: {event['text']}")
        else:
            speaker_name = event["speaker"].replace("_", " ").title()
            transcript_lines.append(f"{speaker_name}: {event['text']}")

    if len(transcript_lines) <= TRANSCRIPT_STABLE_PREFIX + TRANSCRIPT_RECENT_WINDOW:
        return "\n\n".join(transcript_lines)
    elided = len(transcript_lines) - TRANSCRIPT_STABLE_PREFIX - TRANSCRIPT_RECENT_WINDOW
    return "\n\n".join(
        transcript_lines[:TRANSCRIPT_STABLE_PREFIX]
        + [f"[... {elided} earlier turn(s) not shown ...]"]
        + transcript_lines[-TRANSCRIPT_RECENT_WINDOW:]
    )


def _prepare_representative_turn(state: ConversationState, is_reactive: bool = False) -> dict:
    """
    Do everything a representative's turn needs before generation: figure out
    who is speaking, retrieve lexicon/story context, and assemble the system
    prompt and continuation message.

    Shared by both the non-streaming (`representative_engages`) and streaming
    (`stream_representative_turn`) paths so retrieval/prompt-assembly logic
    only lives in one place.

    is_reactive: True when another representative has already spoken earlier
    in this same multi-representative round. Shapes the turn toward a short,
    responsive beat (agreement, difference, or genuine addition) rather than
    a full independent turn - this is what keeps a multi-voice round feeling
    like conversation instead of a sequence of speeches.
    """
    # Determine which world's representative is speaking
    world_ids = state.world_ids if len(state.world_ids) > 0 else [state.world_id]
    current_world_id = state.current_world_id or state.world_id
    is_multi_world = len(world_ids) > 1

    # Get world context for current representative
    current_world_context = None
    if state.worlds_at_table:
        for wc in state.worlds_at_table:
            if wc.world_id == current_world_id:
                current_world_context = wc
                break

    # Use world context if available, otherwise fall back to legacy fields
    if current_world_context:
        permanent_prompt = current_world_context.permanent_prompt
        world_capsule = current_world_context.world_capsule
    else:
        permanent_prompt = state.permanent_prompt
        world_capsule = state.world_capsule_core

    retriever = get_retriever(current_world_id)
    story_retriever = get_story_retriever(current_world_id)
    rep_message_name = get_representative_message_name(current_world_id)

    # Get the last human message
    last_human_message = None
    for msg in reversed(state.messages):
        if isinstance(msg, HumanMessage):
            last_human_message = msg.content
            break

    if not last_human_message:
        # No question yet, provide an opening
        last_human_message = "(The participant has just been introduced to you.)"

    # For a reactive turn, find the most recent thing another representative
    # actually said - the immediate thing this turn needs to respond to, not
    # just the participant's original question. Without this, retrieval and
    # generation both stay anchored to the opening question no matter how
    # deep into an exchange this turn is, which is what makes multi-
    # representative rounds read as parallel independent statements ("three
    # presentations") instead of a real back-and-forth: the model's most
    # concrete instruction was always "answer the question," never "respond
    # to what was just said."
    last_other_rep_message = None
    last_other_rep_display_name = None
    if is_reactive:
        for msg in reversed(state.messages):
            name = getattr(msg, "name", None)
            if name and name != "facilitator" and name != rep_message_name:
                last_other_rep_message = msg.content
                last_other_rep_display_name = get_representative_name(
                    next((wid for wid in world_ids if get_representative_message_name(wid) == name), None)
                ) or name.replace("_", " ").title()
                break

    # Build the public transcript - what has been said at The Table
    public_transcript = build_public_transcript(state)

    # Retrieve relevant lexicon context. S3.5 (Pass 1 R9): the query must
    # be standalone and world-appropriate -
    # 1. an intercept (bridge) may have supplied the real subject as an
    #    override (consumed once) - previously its handback boilerplate
    #    drove the search;
    # 2. a reactive turn gets ONE Haiku rewrite folding the topic (not
    #    the wording) of what was just said into a standalone query -
    #    previously another world's full turn text drove this world's
    #    vector search (the measured cross-encoder noise-band failure);
    # 3. a plain participant message is already standalone.
    # rewrite_query is fail-open: any failure returns the legacy
    # concatenation, degrading to exactly the old behavior.
    if state.retrieval_query_override:
        retrieval_query = state.retrieval_query_override
        state.retrieval_query_override = None
    elif last_other_rep_message:
        from app.rag.query_rewrite import rewrite_query
        try:
            _wname = settings.get_world_config(current_world_id).name
        except Exception:
            _wname = "a historical Christian community"
        retrieval_query = rewrite_query(
            get_monitoring_llm(), last_human_message,
            last_other_rep_display_name, last_other_rep_message,
            world_name=_wname)
    else:
        retrieval_query = last_human_message

    # Lexicon and story retrieval are independent (different vector stores,
    # different filter-LLM calls) and were previously run sequentially,
    # doubling their combined latency for no reason - run them concurrently
    # instead. Both are synchronous/blocking (network-bound LLM + vector
    # search calls), so a plain thread pool is enough; no need for this
    # whole call chain to become async just for this.
    # S3.3 (Pass 1 R4): the ID-keyed session exclusion set for this world -
    # chunks already surfaced this session are excluded deterministically
    # at candidate stage (replacing both substring de-dup proxies)
    exclude_ids = set(state.surfaced_chunk_ids.get(current_world_id, []))

    with ThreadPoolExecutor(max_workers=2) as executor:
        lexicon_future = executor.submit(
            retriever.get_context_for_response,
            query=retrieval_query,
            conversation_context=public_transcript,
            exclude_ids=exclude_ids,
        )
        story_future = executor.submit(
            story_retriever.get_context_for_response,
            query=retrieval_query,
            conversation_context=public_transcript,
            exclude_ids=exclude_ids,
        )
        retrieved_context, lexicon_citations, lexicon_evaluations = lexicon_future.result()
        story_context, story_citations, story_evaluations = story_future.result()

    citations = lexicon_citations + story_citations
    evaluations = lexicon_evaluations + story_evaluations

    # Record what actually surfaced this turn into the session exclusion
    # set, so the next turn's retrieval can exclude it by ID
    newly_surfaced = [
        Path(ev.source_file).stem
        for ev in evaluations
        if ev.retrieved and ev.source_file
    ]
    if newly_surfaced:
        seen = state.surfaced_chunk_ids.setdefault(current_world_id, [])
        for stem in newly_surfaced:
            if stem not in seen:
                seen.append(stem)

    # Guidance for THIS specific representative, queued from an earlier
    # drift/dominance/convergence finding (see check_dominance,
    # check_convergence, and the streaming endpoint's per-round drift
    # monitoring). Routed through pending_guidance, keyed by world_id, so
    # correction reaches only the representative who actually drifted - not
    # whoever happens to speak next in the round, regardless of who the
    # finding was about. S4.3: the slot is a priority queue; this turn
    # delivers the highest-priority entry (the queue is kept sorted by
    # the one signal ordering - see governance.queue_guidance).
    _queued = state.pending_guidance.get(current_world_id) or []
    reroot_guidance = _queued[0]["text"] if _queued else ""

    # Falls back to the older global requires_reroot/drift_signals[-1]
    # mechanism only when nothing is queued in pending_guidance for this
    # world - this keeps the non-streaming, single-world /message endpoint
    # (facilitator_reroots) working without its own migration. A single-
    # representative session has no "wrong representative" to misroute a
    # correction to in the first place, so the global mechanism was never
    # actually buggy there.
    if not reroot_guidance and state.requires_reroot and state.drift_signals:
        last_signal = state.drift_signals[-1]
        reroot_guidance = f"Adjust for: {last_signal.description}"

    # If another representative already spoke this round, this turn is
    # continuing a live exchange, not opening one. Text lives in
    # table_discourse.REACTIVE_TURN_GUIDANCE (promoted out of this file so
    # it's a versioned, reviewed document rather than an inline literal) -
    # byte-identical across every representative and every reactive turn,
    # which is what makes it cacheable as its own breakpoint in
    # _cached_system_message below.
    #
    # A genuine opening turn (is_reactive=False - nothing to react to yet)
    # at a large table gets a DIFFERENT block, not REACTIVE_TURN_GUIDANCE -
    # that text opens with "someone else has already spoken," which would be
    # false for the turn that opens the round. large_table_opening is mutually
    # exclusive with is_reactive by construction.
    large_table_opening = _is_large_table_opening(state, is_reactive)
    if is_multi_world and is_reactive:
        reactive_turn_guidance = REACTIVE_TURN_GUIDANCE
    elif large_table_opening:
        reactive_turn_guidance = OPENING_TURN_LARGE_TABLE_GUIDANCE
    else:
        # The primary-turn path: single-world "Deep Interview" mode (always,
        # since is_reactive is always False there) and every small-table
        # "Compare Worlds" round's opening speaker. Previously received its
        # own PRIMARY_TURN_GUIDANCE block here; folded into
        # representative_prompts.py's always-present _HOW_YOU_ENGAGE instead
        # (Mark's own call, 2026-07-24/25) - this path now gets today's
        # conversational-shape guidance via the static prompt rather than a
        # conditionally-injected one, matching its original byte-identical
        # behavior with no reactive-guidance block at all.
        reactive_turn_guidance = ""

    # Build the system prompt, split into three segments: a stable cacheable
    # prefix (static_prompt), a conditionally-present but equally cacheable
    # reactive-guidance block (reactive_guidance_block), and everything that
    # changes turn-to-turn (dynamic_prompt) - see build_representative_prompt's
    # docstring.
    # S5.2 (Pass 1 §5.1): migrated worlds carry the post-history guard -
    # the assembly's own export, appended closest to generation. Lazy,
    # fail-open import: an unimportable view must never break a turn.
    post_history_guard = ""
    try:
        from app.graph.repair_classifier import _migrated_world_ids
        if current_world_id in _migrated_world_ids():
            from wrs.views.segments.guards import POST_HISTORY_GUARD
            # FLAG-018 layer 3 (S5.6 sustained re-runs): the
            # no-unprompted-sense-clarification constraint survived only
            # partially when placed before the retrieved context (one
            # false "I meant X earlier" opener remained in 16 turns).
            # Doc 09's own post_history finding - the instruction that
            # must survive attention decay rides closest to generation -
            # is why it now ALSO rides here, composed at the wiring site
            # (the assembly's exported guard text itself is unchanged).
            post_history_guard = POST_HISTORY_GUARD + (
                " And open on the question actually asked: no term "
                "clarifications the participant did not ask for, and never "
                "\"when I said X\" for a word this conversation has not "
                "actually spoken.")
    except Exception:
        post_history_guard = ""

    static_prompt, reactive_guidance_block, dynamic_prompt = build_representative_prompt(
        permanent_prompt=permanent_prompt,
        world_capsule=world_capsule,
        world_id=current_world_id,
        retrieved_context=retrieved_context,
        story_context=story_context,
        reroot_guidance=reroot_guidance,
        reactive_turn_guidance=reactive_turn_guidance,
        post_history_guard=post_history_guard,
    )

    # For multi-world, add the public transcript and guidance on encountering
    # other voices. This changes every turn (new transcript each time), so it
    # belongs in dynamic_prompt, not the cached static block.
    if is_multi_world and public_transcript:
        other_reps = []
        for wid in world_ids:
            if wid != current_world_id:
                other_reps.append(get_representative_name(wid))

        dynamic_prompt += f"""

# The Public Transcript — What Has Been Said at This Table

Also present at this table: {', '.join(other_reps)}.

Below is the record of what has been spoken at this Table. You encounter the other voices here through their words — not through access to their inner formation, but through what they have said aloud.

{CROSS_WORLD_VOCABULARY_GUIDANCE}

PUBLIC TRANSCRIPT:
{public_transcript}
"""

    # S4.4a: the selector's private directive to this specific speaker -
    # the REASON line become a consumer (or the deterministic direct-
    # address note). Injected like reroot guidance: invisible to the
    # participant, concrete to the representative. Last in the dynamic
    # prompt so the most situational instruction sits closest to the turn.
    if getattr(state, "private_directive", None):
        dynamic_prompt += f"""

# A Private Word from the Facilitator (never visible to the participant)

{state.private_directive}
"""

    # Build message for continuation. Reactive turns get a distinct framing
    # that puts what was just said front and center as the thing to respond
    # to - this is the single most concrete instruction the model receives
    # each turn, and it needs to point at the live exchange, not repeat the
    # original question as if this were an independent answer to it.
    if last_other_rep_message:
        continuation = REACTIVE_CONTINUATION_PROMPT.format(
            speaker_name=last_other_rep_display_name,
            statement=last_other_rep_message,
            original_message=last_human_message,
        )
    else:
        continuation = REPRESENTATIVE_CONTINUATION_PROMPT.format(message=last_human_message)

    # Track retrieved terms for state
    retrieved_terms = []
    if retrieved_context:
        terms = re.findall(r"### ([^\n]+)", retrieved_context)
        retrieved_terms = terms

    def _citation_payload(citation, kind: str) -> dict:
        payload = {
            "type": kind,
            "term": citation.term,
            "key_sources": citation.key_sources,
            "source_file": citation.source_file,
        }
        if citation.registry:
            payload["registry"] = citation.registry
        return payload

    citations_payload = [
        _citation_payload(c, "lexicon") for c in lexicon_citations
    ] + [
        _citation_payload(c, "story") for c in story_citations
    ]

    def _audit_payload(evaluation, kind: str) -> dict:
        return {
            "type": kind,
            "term": evaluation.term,
            "source_file": evaluation.source_file,
            "retrieved": evaluation.retrieved,
            "reason": evaluation.reason,
        }

    retrieval_audit_payload = [
        _audit_payload(e, "lexicon") for e in lexicon_evaluations
    ] + [
        _audit_payload(e, "story") for e in story_evaluations
    ]

    return {
        "static_prompt": static_prompt,
        "reactive_guidance_block": reactive_guidance_block,
        "dynamic_prompt": dynamic_prompt,
        "continuation": continuation,
        "rep_message_name": rep_message_name,
        "current_world_id": current_world_id,
        "retrieved_context": retrieved_context,
        "story_context": story_context,
        "retrieved_terms": retrieved_terms,
        "citations_payload": citations_payload,
        "retrieval_audit_payload": retrieval_audit_payload,
    }


def _cached_system_message(
    static_prompt: str, reactive_guidance_block: str, dynamic_prompt: str
) -> SystemMessage:
    """
    Build a SystemMessage with Anthropic prompt-caching breakpoints after
    each cacheable (identical-across-calls) portion of the prompt.

    Anthropic caches everything up through a block marked with cache_control
    as a prefix, and supports multiple such breakpoints per request. Two
    portions of this prompt are cacheable, for different reasons:

    - static_prompt (permanent prompt + world capsule + core engagement
      principles) is byte-identical on every turn for this representative.
    - reactive_guidance_block (table_discourse.REACTIVE_TURN_GUIDANCE, when
      this is a reactive turn) is byte-identical across every representative
      and every reactive turn, but only present some of the time - it gets
      its own breakpoint rather than being folded into static_prompt's,
      because mixing a sometimes-present block into an always-present one
      would make the always-present block's own cache key unstable (a cache
      hit requires the cached prefix to match exactly, so a block that
      changes presence/absence turn to turn can't safely share a breakpoint
      with one that never changes).

    dynamic_prompt (retrieved context, reroot correction - differs on every
    call) stays out of both cached blocks entirely; including it in either
    would make that block a guaranteed cache miss every time, defeating the
    purpose.
    """
    blocks = [{"type": "text", "text": static_prompt, "cache_control": {"type": "ephemeral"}}]
    if reactive_guidance_block:
        blocks.append({
            "type": "text",
            "text": reactive_guidance_block,
            "cache_control": {"type": "ephemeral"},
        })
    if dynamic_prompt:
        blocks.append({"type": "text", "text": dynamic_prompt})
    return SystemMessage(content=blocks)


def representative_engages(state: ConversationState, is_reactive: bool = False,
                            request_id: str | None = None) -> dict:
    """
    The representative responds to the participant with RAG-augmented context.

    This is the main conversation loop node. In multi-world tables, uses
    current_world_id to determine which representative speaks.

    Representatives see the "public transcript" - what has been said at The Table -
    allowing them to respond to what other representatives have said.

    request_id: the calling endpoint's per-HTTP-request trace ID (see
    new_request_id), logged alongside this call's response fingerprint via
    _log_llm_call. Optional and purely observational - never affects
    generation itself.
    """
    large_table_opening = _is_large_table_opening(state, is_reactive)
    if is_reactive:
        turn_max_tokens = REACTIVE_TURN_MAX_TOKENS
    elif large_table_opening:
        turn_max_tokens = OPENING_TURN_MAX_TOKENS
    else:
        turn_max_tokens = PRIMARY_TURN_MAX_TOKENS
    llm = get_llm(max_tokens=turn_max_tokens)
    ctx = _prepare_representative_turn(state, is_reactive=is_reactive)

    response = llm.invoke([
        _cached_system_message(ctx["static_prompt"], ctx["reactive_guidance_block"], ctx["dynamic_prompt"]),
        HumanMessage(content=ctx["continuation"]),
    ])
    log_llm_usage("main_response", response, settings.llm_model,
                   request_id=request_id, session_id=state.session_id)
    _log_llm_call(request_id, state.session_id, ctx["current_world_id"],
                   ctx["rep_message_name"], response.content if isinstance(response.content, str) else str(response.content))

    message_kwargs = {}
    if ctx["citations_payload"]:
        message_kwargs["citations"] = ctx["citations_payload"]
    if ctx["retrieval_audit_payload"]:
        message_kwargs["retrieval_audit"] = ctx["retrieval_audit_payload"]
    glosses_used = find_glosses_used(
        ctx["current_world_id"],
        response.content if isinstance(response.content, str) else str(response.content),
    )
    if glosses_used:
        message_kwargs["glosses_used"] = glosses_used

    return {
        "messages": [
            AIMessage(
                content=response.content,
                name=ctx["rep_message_name"],
                additional_kwargs=message_kwargs,
            )
        ],
        "turn_count": state.turn_count + 1,
        "requires_reroot": False,  # Clear reroot flag after using it
        "current_world_id": ctx["current_world_id"],
        "retrieved_context": RetrievedContext(
            chunks=[c for c in [ctx["retrieved_context"], ctx["story_context"]] if c],
            terms=ctx["retrieved_terms"],
            sources=[],
            citations=ctx["citations_payload"],
        ) if (ctx["retrieved_context"] or ctx["story_context"]) else None,
    }


def stream_representative_turn(state: ConversationState, is_reactive: bool = False,
                                request_id: str | None = None):
    """
    Stream a single representative's turn token-by-token.

    Reuses the same retrieval/prompt-assembly logic as `representative_engages`
    (via `_prepare_representative_turn`) so the streamed and non-streamed paths
    can never drift apart. Yields dicts as generation progresses:

    - {"type": "token", "speaker": name, "text": chunk} for each token chunk
    - {"type": "complete", "speaker": name, "message": AIMessage, ...} once,
      at the end, carrying the full assembled message and state updates

    request_id: see representative_engages - logged alongside this call's
    response fingerprint via _log_llm_call once the full text is known.
    """
    large_table_opening = _is_large_table_opening(state, is_reactive)
    if is_reactive:
        turn_max_tokens = REACTIVE_TURN_MAX_TOKENS
    elif large_table_opening:
        turn_max_tokens = OPENING_TURN_MAX_TOKENS
    else:
        turn_max_tokens = PRIMARY_TURN_MAX_TOKENS
    llm = get_llm(max_tokens=turn_max_tokens)
    ctx = _prepare_representative_turn(state, is_reactive=is_reactive)

    messages = [
        _cached_system_message(ctx["static_prompt"], ctx["reactive_guidance_block"], ctx["dynamic_prompt"]),
        HumanMessage(content=ctx["continuation"]),
    ]

    def _extract_piece(content) -> str:
        # Extended-thinking-capable models can emit content as a list of
        # blocks (text/thinking/etc.) instead of a plain string - only
        # surface the text blocks to the participant, same as the
        # non-streaming path does when parsing the final response.
        if isinstance(content, list):
            return "".join(
                block.get("text", "")
                for block in content
                if isinstance(block, dict) and block.get("type") == "text"
            )
        return content or ""

    def _generate_once(msgs) -> tuple[str, list[str]]:
        text = ""
        pieces: list[str] = []
        # Accumulate the raw chunks via LangChain's own AIMessageChunk.__add__
        # (not just the extracted text) so usage_metadata/response_metadata
        # from across the whole stream are correctly merged into one object -
        # summing chunks is the standard way to get an accurate final usage
        # count out of a streamed call without a second, non-streamed API
        # call just to ask for it again.
        usage_chunk = None
        for chunk in llm.stream(msgs):
            usage_chunk = chunk if usage_chunk is None else usage_chunk + chunk
            piece = _extract_piece(chunk.content)
            if piece:
                text += piece
                pieces.append(piece)
        log_llm_usage("main_response", usage_chunk, settings.llm_model,
                       request_id=request_id, session_id=state.session_id)
        return text, pieces

    # Worlds whose own Permanent Prompt states a hard, all-conditions
    # numeric turn-length ceiling that soft guidance has already been
    # tested against twice (the static prompt text itself, then a
    # check_length_ceiling-queued correction for the next turn) and still
    # missed badly under real multi-world topical pressure - see the
    # 2026-07 Fable/Opus review. For these worlds only, buffer the first
    # attempt instead of streaming it live, token by token, and silently
    # regenerate once if it exceeds the trigger multiple of the stated
    # ceiling, before the participant ever sees a token. This costs
    # latency on that one world's turns but resolves a structural conflict
    # (the ceiling vs. the other things a reactive turn is required to do)
    # that prompt wording alone could not.
    #
    # Both worlds are included, not just Papnoute - an independent Opus
    # review of the first version of this mechanism (Papnoute-only, 2x
    # trigger) correctly flagged that Albina's exclusion rested on a
    # thinner data point than the one that had already proven advisory-only
    # insufficient for Papnoute, and that a 2x trigger (120 words for a
    # 60-word ceiling) leaves a dead zone - a 110-word Papnoute turn in
    # that same retest sailed through with zero enforcement.
    #
    # The trigger multiple is per-world, not a single global constant,
    # because the two worlds' actual distributions differ once real
    # observability data existed to look at (see the dead-zone log line
    # below): Papnoute's uncorrected drafts landed around 175-180 words
    # against a 60-word ceiling (a wide margin, so 1.5x/90 catches him
    # reliably), but Albina's landed consistently at 220-245 against a
    # 180-word ceiling - a narrow enough margin that 1.5x/270 never once
    # fired in that same test batch, leaving her permanently in the dead
    # zone rather than only occasionally. Her multiple is tightened to 1.2x
    # to actually reach the range she is shown to land in.
    # alexandria-catechetical added at the S6.2 freeze fix session (Mark's
    # mandate, 2026-07-28): the S6.2 TRR measured Theon at 77-82% of all
    # representative speech (dominance HIGH every turn), truncating the
    # sitting at 5/8 turns. Ceiling 160 = the cleared solo register's own
    # measured max (alexvoice001.native_measure: responses 123-166, mean
    # ~141) so solo answers never trigger; multiple 1.2 (the Albina
    # narrow-margin precedent) so the 300+-word table turns do.
    HARD_CEILING_WORLDS = {"desert-monasticism": 60, "hieronymian-ascetic-literary": 180,
                           "alexandria-catechetical": 160,
                           # S6.2/SYR freeze (2026-07-28): 165 = the voice
                           # profile's measured max (syrvoice001 native_measure,
                           # range 41-165) so the solo register never triggers;
                           # grounded in the TRR dominance finding (63-79%,
                           # table turns to 1053w vs the 98w native measure)
                           "syriac-edessa-nisibis": 165}
    RETRY_TRIGGER_MULTIPLES = {"desert-monasticism": 1.5, "hieronymian-ascetic-literary": 1.2,
                               "alexandria-catechetical": 1.2,
                               "syriac-edessa-nisibis": 1.2}
    ceiling = HARD_CEILING_WORLDS.get(ctx["current_world_id"])
    retry_trigger_multiple = RETRY_TRIGGER_MULTIPLES.get(ctx["current_world_id"], 1.5)

    if ceiling:
        full_text, pieces = _generate_once(messages)
        word_count = len(full_text.split()) if full_text else 0
        if full_text and word_count > ceiling * retry_trigger_multiple:
            print(
                f"[length_ceiling] {ctx['current_world_id']} turn ran {word_count} words "
                f"(ceiling {ceiling}, trigger {ceiling * retry_trigger_multiple:.0f}) - "
                "regenerating once."
            )
            corrective = HumanMessage(content=(
                f"Your answer just now ran to {word_count} words; your own "
                f"measure holds at most {ceiling}. Say the same thing again, holding to "
                "it - fewer sentences, not less said."
            ))
            retry_text, retry_pieces = _generate_once(
                messages + [AIMessage(content=full_text), corrective]
            )
            if retry_text:
                print(
                    f"[length_ceiling] {ctx['current_world_id']} retry produced "
                    f"{len(retry_text.split())} words."
                )
                full_text, pieces = retry_text, retry_pieces
        elif full_text and word_count > ceiling:
            # Over ceiling but under the retry trigger - the dead zone Opus's
            # review named. Not corrected here (that would defeat the point
            # of bounding the trigger), but logged so this zone's actual
            # frequency is visible rather than invisible, per that review's
            # specific request for observability before trusting the fix.
            print(
                f"[length_ceiling] {ctx['current_world_id']} turn ran {word_count} words "
                f"(ceiling {ceiling}) - over ceiling but under the {retry_trigger_multiple}x "
                "retry trigger, left uncorrected."
            )
        for piece in pieces:
            yield {"type": "token", "speaker": ctx["rep_message_name"], "text": piece}
    else:
        full_text, pieces = "", []
        usage_chunk = None
        for chunk in llm.stream(messages):
            usage_chunk = chunk if usage_chunk is None else usage_chunk + chunk
            piece = _extract_piece(chunk.content)
            if piece:
                full_text += piece
                yield {"type": "token", "speaker": ctx["rep_message_name"], "text": piece}
        log_llm_usage("main_response", usage_chunk, settings.llm_model,
                       request_id=request_id, session_id=state.session_id)

    # A stream that completes with zero text is rare but real (observed in
    # live testing) - shipping a blank message doesn't just look broken to
    # the participant, it corrupts every later turn that reads this one out
    # of the public transcript (an empty "X said:" line reliably confuses
    # subsequent generations). One retry via a fresh non-streaming call
    # catches the transient case; if that also comes back empty, the turn is
    # skipped rather than injected as blank content.
    if not full_text:
        retry_response = llm.invoke(messages)
        log_llm_usage("main_response", retry_response, settings.llm_model,
                       request_id=request_id, session_id=state.session_id)
        full_text = _extract_piece(retry_response.content)
        if full_text:
            yield {"type": "token", "speaker": ctx["rep_message_name"], "text": full_text}

    _log_llm_call(request_id, state.session_id, ctx["current_world_id"], ctx["rep_message_name"], full_text)

    message_kwargs = {}
    if ctx["citations_payload"]:
        message_kwargs["citations"] = ctx["citations_payload"]
    if ctx["retrieval_audit_payload"]:
        message_kwargs["retrieval_audit"] = ctx["retrieval_audit_payload"]
    glosses_used = find_glosses_used(ctx["current_world_id"], full_text)
    if glosses_used:
        message_kwargs["glosses_used"] = glosses_used

    ai_message = AIMessage(
        content=full_text,
        name=ctx["rep_message_name"],
        additional_kwargs=message_kwargs,
    )

    yield {
        "type": "complete",
        "speaker": ctx["rep_message_name"],
        "message": ai_message,
        "current_world_id": ctx["current_world_id"],
        "retrieved_context": RetrievedContext(
            chunks=[c for c in [ctx["retrieved_context"], ctx["story_context"]] if c],
            terms=ctx["retrieved_terms"],
            sources=[],
            citations=ctx["citations_payload"],
        ) if (ctx["retrieved_context"] or ctx["story_context"]) else None,
    }


def multi_representative_engages(state: ConversationState, request_id: str | None = None) -> dict:
    """
    Multiple representatives respond to a question at The Table.

    When a question is directed to all representatives, or when the facilitator
    determines multiple voices should respond, each representative speaks in turn.
    Each subsequent representative sees what the previous ones said in the public
    transcript, allowing genuine encounter between worlds.

    request_id: see representative_engages - passed through to every
    per-world call below so all of this round's LLM calls trace back to the
    same HTTP request in the log.
    """
    from dataclasses import replace

    world_ids = state.world_ids if len(state.world_ids) > 0 else [state.world_id]

    if len(world_ids) <= 1:
        # Single world - delegate to regular function
        return representative_engages(state, request_id=request_id)

    all_messages = []
    # Create a working copy of messages that we'll build up
    working_messages = list(state.messages)

    # Each representative responds in turn
    for world_id in world_ids:
        # Create a state copy with updated messages and current speaker
        # This ensures each representative sees what came before
        working_state = ConversationState(
            messages=working_messages,
            phase=state.phase,
            current_speaker=state.current_speaker,
            current_world_id=world_id,
            turn_count=state.turn_count,
            drift_signals=list(state.drift_signals),
            requires_reroot=state.requires_reroot,
            retrieved_context=state.retrieved_context,
            worlds_at_table=state.worlds_at_table,
            world_capsule_core=state.world_capsule_core,
            permanent_prompt=state.permanent_prompt,
            session_id=state.session_id,
            world_id=state.world_id,
            world_ids=state.world_ids,
            close_requested=state.close_requested,
        )

        # Get this representative's response - every speaker after the first
        # in a round is responding to what's already been said, not opening it
        result = representative_engages(
            working_state, is_reactive=(world_id != world_ids[0]), request_id=request_id
        )

        # Add the message to our collection
        new_messages = result.get("messages", [])
        all_messages.extend(new_messages)

        # Update working messages so next representative sees them
        working_messages = working_messages + new_messages

    return {
        "messages": all_messages,
        "turn_count": state.turn_count + len(world_ids),
        "requires_reroot": False,
        "current_world_id": world_ids[-1],  # Last speaker
    }


# Which finding wins when several compete for one slot. Severity decides
# first; this breaks ties. S4.3 (Pass 1 §6.5): ONE ordering now governs
# BOTH single-slot bottlenecks - the monitor's one-finding-per-turn slot
# (_select_monitor_finding, below) and the per-world guidance queue
# (governance.queue_guidance) - extended to the five table signals, which
# the old per-world guidance slot deprioritized purely by statement order
# in a background block. Ordered by what the governance treats as most
# serious rather than by how any prompt happens to list them:
# FABRICATION is the cardinal failure (Facilitator Governance Section 11) -
# its intrinsic/extrinsic verdicts rank via severity, high vs medium;
# SELF_NARRATION is governed more strictly than the rest (Article 28);
# then the signals that put something untrue or out-of-world in front of
# a participant; then the cross-world identity/agreement signals
# (vocabulary drift, manufactured convergence - the multi-party class the
# old slot structurally lost); then stance; then shape.
_SIGNAL_PRIORITY: list[str] = [
    "fabrication", "misattribution", "self_narration", "first_person",
    "temporal_bleed", "anachronism", "over_settling",
    "cross_world_vocabulary", "manufactured_resolution", "convergence",
    "closing_synthesis", "apologetics", "smoothing", "flattening",
    "agreeing", "dominance", "generating", "over_producing",
    "length_ceiling", "question_stacking",
]
# kept as an alias: the monitor bottleneck's historical name for the list
_MONITOR_SIGNAL_PRIORITY = _SIGNAL_PRIORITY
_SEVERITY_RANK = {"high": 0, "medium": 1, "low": 2}


def signal_rank(signal_type: str, severity: str) -> tuple[int, int]:
    """The one ordering, as a sortable key - shared by both bottlenecks
    (Pass 1 §6.5's 'one ordering governs both')."""
    priority = next(
        (i for i, s in enumerate(_SIGNAL_PRIORITY) if s in signal_type),
        len(_SIGNAL_PRIORITY),
    )
    return _SEVERITY_RANK.get(severity, 2), priority


def _select_monitor_finding(
    findings: list[tuple[str, str, str]]
) -> tuple[str, str, str]:
    """
    The one finding a multi-finding monitor result reports.

    Only one DriftSignal is returned per turn - every caller and the reroot
    path are built around that - so when the monitor names several, which one
    survives matters. Highest severity wins; equal severity falls back to
    _MONITOR_SIGNAL_PRIORITY. Measured motivation: across 45 live turns the
    monitor never once reported OVER_PRODUCING, on an arm averaging 306 words
    and 2.3 threads a turn, because the format admitted a single finding and
    ten signals were competing for it. The reverse case is the dangerous one -
    a fabrication losing that slot to a stylistic complaint.
    """
    def rank(f: tuple[str, str, str]) -> tuple[int, int]:
        signal_type, severity, _ = f
        return signal_rank(signal_type, severity)

    return min(findings, key=rank)


def _detect_drift_signal(response_text: str, world_id: str | None = None) -> DriftSignal | None:
    """
    Run drift detection on a single representative response and return the
    detected DriftSignal (tagged with world_id, if given), or None if clean.

    Shared by facilitator_monitors (the single-turn, backward-compatible
    entry point used by the non-streaming /message endpoint) and
    check_drift_for_message (used by the streaming endpoint's per-round
    monitoring pass, which checks every turn of a round tagged with its own
    speaker - see that function's docstring for why).
    """
    llm = get_monitoring_llm()
    prompt = FACILITATOR_MONITORING_PROMPT.format(response=response_text)
    response = llm.invoke([
        SystemMessage(content=prompt),
        HumanMessage(content="Analyze the response above for drift signals."),
    ])
    log_llm_usage("drift_detection", response, _MONITORING_MODEL)

    result = response.content.strip()
    if not result.startswith("DRIFT_DETECTED"):
        # The general monitor above weighs ten signals at once under a
        # standing instruction to be conservative, which is right for the
        # signals it carries and wrong for OVER_SETTLING: a missing limit
        # leaves no trace in the text, so a turn that reads well overall
        # reads as clean. Measured, not assumed - carried as an eleventh
        # signal in that prompt, it caught 0 of 3 defects that blind grading
        # had already confirmed, and affirmatively cleared one of them as
        # "the exact opposite of OVER_SETTLING." It gets its own screen
        # instead, tuned to flag rather than to be sure, with a source-fed
        # second pass to clear the false positives that tuning invites.
        #
        # Only reached when the general monitor is clean. A turn it already
        # flagged is already getting a correction, and leaving that path
        # byte-identical keeps a tested component untouched - the known cost
        # is that over-settling goes unchecked on a turn that also drifted
        # some other way.
        return _over_settling_signal(response_text, world_id)

    # The prompt asks for one four-line block per finding, since a turn can
    # carry several at once. Parse every block, then choose which one this
    # call reports - the previous loop overwrote as it went and kept whichever
    # block happened to come LAST, which is the opposite of what matters when
    # one of them is FABRICATION.
    findings: list[tuple[str, str, str]] = []
    cur_type = cur_sev = cur_desc = ""
    for line in result.split("\n")[1:]:
        if line.startswith("Signal:"):
            if cur_type:
                findings.append((cur_type, cur_sev or "low", cur_desc))
            cur_type = line.split(":", 1)[1].strip().lower().replace("-", "_")
            cur_sev = cur_desc = ""
        elif line.startswith("Severity:"):
            cur_sev = line.split(":", 1)[1].strip().lower()
        elif line.startswith("Description:"):
            cur_desc = line.split(":", 1)[1].strip()
    if cur_type:
        findings.append((cur_type, cur_sev or "low", cur_desc))

    if not findings:
        return None

    signal_type, severity, description = _select_monitor_finding(findings)

    # Validate signal type - must match the 9 signals defined in
    # FACILITATOR_MONITORING_PROMPT (facilitator_prompts.py). This list had
    # drifted out of sync with the prompt once already: it was missing
    # over_producing, temporal_bleed, and flattening after the prompt was
    # extended, so any of those detections was silently relabeled
    # "smoothing" instead of surfacing under its real signal type. Kept
    # "anachronism" as an accepted alias since temporal_bleed is its
    # current name in the prompt but older sessions/tests may still emit it.
    valid_signals = [
        "smoothing", "generating", "agreeing", "over_producing",
        "temporal_bleed", "flattening", "fabrication", "apologetics",
        "first_person", "anachronism", "self_narration", "over_settling",
    ]
    if signal_type not in valid_signals:
        # The compound-case rule in FACILITATOR_MONITORING_PROMPT's
        # FABRICATION signal explicitly tells the model to flag a combined
        # FABRICATION+FIRST_PERSON finding - and it reliably does, returning
        # a compound label like "FABRICATION + FIRST_PERSON" that doesn't
        # exact-match any single entry above. A naive exact-match check
        # silently discarded these into "smoothing", hiding exactly the
        # compound violation the prompt was written to catch. Search for any
        # known signal name within the raw string instead of requiring an
        # exact match, preferring fabrication when present since the prompt
        # itself says the compound case should surface as FABRICATION.
        found = [s for s in valid_signals if s in signal_type]
        if "fabrication" in found:
            signal_type = "fabrication"
        elif found:
            signal_type = found[0]
        else:
            signal_type = "smoothing"

    # Stage 2: FABRICATION is the only signal of the nine that asks whether
    # content is grounded in sources, and it was the only one denied them -
    # everything else (smoothing, generating, agreeing, over_producing,
    # temporal_bleed, flattening, apologetics, first_person) is a property of
    # the text and judgeable from the response alone. Stage 1 above, given no
    # sources, can only use attribution language as a proxy for groundedness:
    # observed live, Papnoute naming Antony and citing Athanasius passed
    # clean, while the same attested material narrated as "he" was flagged
    # high-severity fabrication on the next turn. That is both a false
    # positive (attested narration flagged) and, worse, a false negative
    # (a misattributed name carrying an attribution phrase reads as clean) -
    # and misattribution is the one fabrication this project has actually
    # recorded. Only fabrication candidates reach this second call, so most
    # turns never pay for it.
    if signal_type == "fabrication" and world_id:
        verdict = _adjudicate_fabrication(response_text, world_id, description)
        if verdict is None:
            # could not adjudicate - stage 1's finding stands unlabeled,
            # at stage 1's own severity (fail-open toward keeping it)
            pass
        elif verdict[0] == "grounded":
            return None
        else:
            # S4.3 (Pass 1 §6.3): the FABRICATED verdict is split.
            # INTRINSIC - the material contradicts the claim (the record
            # attributes it differently, or the permanent prompt/capsule
            # settle it the other way): settled, severe -> high.
            # EXTRINSIC - nothing in the material supports the claim:
            # provisional (fresh retrieval may simply have missed the
            # chunk, the prompt's own evidentiary caution) -> medium.
            # The adjudicator's own prompt already drew this distinction
            # in prose and discarded it in its output format; now the
            # output format carries it, the two verdicts take different
            # severities in the one priority ordering, and different
            # SELECTED corrective strategies (generate_reroot_guidance).
            kind, reason = verdict
            severity = "high" if kind == "intrinsic" else "medium"
            description = (f"{description}\n\nAdjudication: {kind} - "
                           f"{reason}")

    return DriftSignal(
        signal_type=signal_type,
        description=description,
        severity=severity,
        world_id=world_id,
    )


def _adjudicate_fabrication(
    response_text: str, world_id: str, stage1_description: str
) -> tuple[str, str] | None:
    """
    Second-stage FABRICATION check, WITH the sources stage 1 is denied.

    Returns a (verdict, reason) tuple - verdict one of "grounded" (drop
    the signal), "intrinsic" (the material CONTRADICTS the claim: settled,
    severe), "extrinsic" (the material cannot SUPPORT the claim:
    provisional) - or None (could not adjudicate; caller keeps stage 1's
    finding rather than silently clearing a real one). The
    intrinsic/extrinsic split is S4.3 (Pass 1 §6.3): the adjudicator's
    prose already drew the distinction and its old output format
    ("FABRICATED", bare) discarded it.

    Fails open toward keeping the signal: if the capsule can't be read, the
    retrievers error, or the model's verdict is unparseable, the stage 1
    finding stands. A guard that silently disappears on error is worse than a
    noisy one - the noise is at least visible.
    """
    evidence = _gather_world_evidence(world_id, response_text)
    if evidence is None:
        return None
    permanent_prompt, capsule, retrieved = evidence

    try:
        llm = get_monitoring_llm()
        prompt = FABRICATION_ADJUDICATION_PROMPT.format(
            permanent_prompt=permanent_prompt,
            capsule=capsule,
            retrieved=retrieved,
            response=response_text,
            stage1_description=stage1_description,
        )
        response = llm.invoke([
            _cached_adjudication_message(prompt),
            HumanMessage(content="Adjudicate the flagged content against the material above."),
        ])
        log_llm_usage("fabrication_adjudication", response, _MONITORING_MODEL)
        result = response.content.strip()
    except Exception:
        return None

    def _reason(text: str) -> str:
        for line in text.split("\n"):
            if line.strip().startswith("Reason:"):
                return line.split(":", 1)[1].strip()
        return ""

    if result.startswith("GROUNDED"):
        return ("grounded", _reason(result))
    if result.startswith("FABRICATED_INTRINSIC"):
        return ("intrinsic", _reason(result))
    if result.startswith("FABRICATED_EXTRINSIC"):
        return ("extrinsic", _reason(result))
    if result.startswith("FABRICATED"):
        # bare legacy token, no sub-verdict claimed: treat as extrinsic -
        # intrinsic must POINT at the contradicting material (the same
        # affirmative test the over-settling adjudicator applies), and a
        # verdict that didn't is by definition only "unsupported"
        return ("extrinsic", _reason(result))
    return None


_ADJUDICATION_CACHE_BOUNDARY = "## Retrieved source material for this world relevant to this response"


def _cached_adjudication_message(rendered: str) -> SystemMessage:
    """
    A source-fed adjudication prompt, split into a cached prefix and an
    uncached remainder at the point where per-world-stable material ends.

    Both adjudicators (fabrication and over-settling) are built the same way:
    instructions, then the representative's permanent prompt, then the world
    capsule, then retrieved material, then the turn being judged. Everything
    up to the retrieval heading is byte-identical on every call for a given
    world - roughly 9,250 tokens of it, previously paid in full every time a
    finding reached adjudication. Everything after it changes per call and is
    deliberately left out of the cached block; including it would guarantee a
    miss and defeat the purpose. Same reasoning as _cached_system_message,
    applied to the monitoring path, which was simply never given it.

    Falls back to a single uncached block if the boundary is absent, so a
    reworded prompt degrades to today's cost rather than breaking.
    """
    head, sep, tail = rendered.partition(_ADJUDICATION_CACHE_BOUNDARY)
    if not sep:
        return SystemMessage(content=rendered)
    return SystemMessage(content=[
        {"type": "text", "text": head, "cache_control": {"type": "ephemeral"}},
        {"type": "text", "text": sep + tail},
    ])


def _screen_over_settling(response_text: str) -> str | None:
    """
    First-pass OVER_SETTLING screen: its own call, weighing nothing else.

    Returns the flagged claim and concern as a description string, or None if
    the turn reads clean. Deliberately tuned to over-flag - the prompt tells
    it to flag when unsure - because every flag is handed to a source-fed
    second pass that can clear it, and only a miss is unrecoverable.
    """
    try:
        llm = get_monitoring_llm()
        response = llm.invoke([
            SystemMessage(content=OVER_SETTLING_SCREEN_PROMPT.format(response=response_text)),
            HumanMessage(content="Screen the turn above."),
        ])
        log_llm_usage("over_settling_screen", response, _MONITORING_MODEL)
        result = response.content.strip()
    except Exception:
        return None

    if not result.startswith("SCREEN_FLAG"):
        return None

    # Everything after the SCREEN_FLAG line is the numbered candidate list,
    # passed to the adjudicator verbatim: it rules per number, and keeping
    # the numbering intact is what lets its verdicts be matched back.
    candidates = result.split("\n", 1)[1].strip() if "\n" in result else ""
    return candidates or None


def _over_settling_signal(
    response_text: str, world_id: str | None
) -> DriftSignal | None:
    """
    The full OVER_SETTLING path: screen, then source-fed adjudication.

    Returns None unless the adjudicator, reading this world's actual sources,
    confirms that the record limits the flagged claim in a way the turn left
    out. Without a world_id there are no sources to judge against, and this
    check clears rather than guesses (see _adjudicate_over_settling on why
    the asymmetry runs this direction).
    """
    if not world_id:
        return None

    screened = _screen_over_settling(response_text)
    if screened is None:
        return None

    missing_limit = _adjudicate_over_settling(response_text, world_id, screened)
    if missing_limit is False or missing_limit is None:
        return None

    return DriftSignal(
        signal_type="over_settling",
        # The named limit is the whole payload: the correction is only
        # actionable if the representative is told WHICH limit went missing,
        # since it has to speak that limit from inside its own world.
        description=f"{screened}\n\nMissing limit: {missing_limit}",
        # Medium is the floor that sets requires_reroot (see
        # facilitator_monitors), and a claim delivered firmer than the record
        # holds it is never a cosmetic finding.
        severity="medium",
        world_id=world_id,
    )


def _adjudicate_over_settling(
    response_text: str, world_id: str, stage1_description: str
) -> bool | str | None:
    """
    Second-stage OVER_SETTLING check, WITH the sources stage 1 is denied.

    Returns False (cleared - drop the signal), a non-empty string (confirmed;
    the string is the specific limit the record puts on the claim that the
    response omitted), or None (could not adjudicate; caller keeps stage 1's
    finding rather than silently clearing a real one).

    Fails open toward keeping the signal on infrastructure errors, exactly as
    _adjudicate_fabrication does - but note the MODEL-level asymmetry runs the
    other way here and is set in the prompt itself: told to answer under
    genuine uncertainty, this adjudicator clears rather than confirms. A false
    confirmation would push a world to hedge a conviction it actually held,
    which flattens it just as badly as dropping a doubt it actually had.
    """
    evidence = _gather_world_evidence(world_id, response_text)
    if evidence is None:
        return None
    permanent_prompt, capsule, retrieved = evidence

    try:
        llm = get_monitoring_llm()
        prompt = OVER_SETTLING_ADJUDICATION_PROMPT.format(
            permanent_prompt=permanent_prompt,
            capsule=capsule,
            retrieved=retrieved,
            response=response_text,
            stage1_description=stage1_description,
        )
        response = llm.invoke([
            _cached_adjudication_message(prompt),
            HumanMessage(content="Adjudicate the flagged claim against the material above."),
        ])
        log_llm_usage("over_settling_adjudication", response, _MONITORING_MODEL)
        result = response.content.strip()
    except Exception:
        return None

    # One verdict line per candidate. Any single confirmed candidate makes
    # the turn a finding - the first one carries it, since the correction
    # only needs one limit restored to be actionable.
    confirmed = [
        line.split("Missing limit:", 1)[1].strip()
        for line in result.split("\n")
        if "OVER_SETTLED" in line and "Missing limit:" in line
    ]
    for limit in confirmed:
        if limit:
            return limit

    if "OVER_SETTLED" in result:
        # Confirmed but no limit parsed out. Clearing here rather than
        # keeping a nameless finding is deliberate: the correction is only
        # actionable if it names WHICH limit went missing, and telling a
        # representative it over-settled without saying what it left out
        # invites exactly the vague hedging this check's asymmetry exists to
        # prevent.
        return False
    return False


def _gather_world_evidence(
    world_id: str, response_text: str
) -> tuple[str, str, str] | None:
    """
    The three sources a source-fed adjudication is defined against, for one
    world: (permanent_prompt, capsule, retrieved). None if the capsule cannot
    be read at all, which is the one failure that leaves nothing to judge
    against.

    Shared by both second-stage checks (_adjudicate_fabrication and
    _adjudicate_over_settling), which ask opposite questions of identical
    evidence: whether the record supports a claim, and whether the record
    limits it.
    """
    try:
        world_config = settings.get_world_config(world_id)
        capsule = world_config.world_capsule_path.read_text(encoding="utf-8")
    except Exception:
        return None

    # The permanent prompt is the third source FABRICATION's own definition
    # names ("grounded in the permanent prompt, world capsule, or retrieved
    # context"), and it is where each Representative's core formation and
    # world facts live. Adjudicating against only the capsule and retrieval
    # left content grounded ONLY in the permanent prompt still reading as
    # fabricated - the same false-positive class this stage exists to close,
    # surviving in a narrower band. Non-fatal if unreadable: the capsule and
    # retrieval can still settle most cases, and returning None here would
    # keep a stage 1 finding this stage might have cleared.
    try:
        permanent_prompt = world_config.permanent_prompt_path.read_text(encoding="utf-8")
    except Exception:
        permanent_prompt = "(permanent prompt unavailable)"

    retrieved_parts: list[str] = []
    for getter in (get_retriever, get_story_retriever):
        try:
            context, _citations, _evals = getter(world_id).get_context_for_response(
                query=response_text
            )
            if context:
                retrieved_parts.append(context)
        except Exception:
            # One retriever failing shouldn't sink the adjudication - the
            # other's material plus the capsule may still settle it.
            continue

    retrieved = "\n\n".join(retrieved_parts) or "(no additional material retrieved)"

    return permanent_prompt, capsule, retrieved


def check_drift_for_message(world_id: str, message_content: str) -> DriftSignal | None:
    """
    Single-turn drift check for one specific representative's message,
    tagged with that representative's world_id.

    Used by the streaming endpoint to monitor EVERY turn completed in a
    round, not only the last speaker's - facilitator_monitors (below) only
    ever sees state.current_world_id's most recent message, which in a
    multi-turn round silently skips drift checking on every turn but the
    last one.
    """
    return _detect_drift_signal(message_content, world_id=world_id)


def generate_reroot_guidance(signal: DriftSignal) -> str:
    """
    Generate brief correction guidance text for a single drift signal.

    Callers route the result through pending_guidance[world_id] themselves
    (see main.py's streaming endpoint) rather than a global requires_reroot
    flag, so correction reaches only the representative who actually
    drifted - not whoever happens to speak next in the round, regardless of
    who the finding was about.
    """
    # OVER_SETTLING never goes through the generative path below. Its
    # adjudicator has already named the missing limit, from the sources, in
    # terms the representative can speak - so there is nothing left to
    # compose, and composing anyway is actively unsafe. Observed: handed this
    # signal, the reroot model invented supporting sources and told a
    # ~95-155 AD householder to contrast "Tertullian's rigorism" with the
    # Shepherd of Hermas - an author outside her span, reached for to
    # illustrate a limit that had already been stated correctly without him.
    # A guard against overstating certainty would have introduced temporal
    # bleed and a fabricated citation to do it. Pass the adjudicator's own
    # words through instead: safer, and one model call cheaper.
    if signal.signal_type == "over_settling":
        limit = ""
        for line in signal.description.split("\n"):
            if line.startswith("Missing limit:"):
                limit = line.split(":", 1)[1].strip()
                break
        if limit:
            # FLAG-018 (S5.6 freeze battery, both sustained trials): the
            # earlier closing instruction here - "Say that plainly ...
            # before you go further" - made the voice OPEN its next turn
            # with a correction preamble even when the conversation had
            # moved on, narrating clarifications of terms the participant
            # never used (the adjudicator's own lexicon citations). The
            # correction is now carried as a silent constraint: never
            # announced, spoken only if the subject itself returns.
            # FABRICATION below keeps its proactive set-it-right shape on
            # purpose (§6.3's closed strategies; a false attribution
            # stands until corrected - a too-firm phrasing does not).
            return (
                "Your last turn spoke that more firmly than your own record holds it. "
                f"What it left out: {limit} Carry that limit silently from here on. "
                "Do not open your next turn by announcing a correction, and do not "
                "clarify terms the participant has not asked about - simply stop "
                "repeating the over-firm form, and if the participant returns to that "
                "subject, speak the limit plainly then, in your own words and from "
                "inside your own life, reaching for nothing beyond what your own "
                "record already gives you to say."
            )

    # S4.3 (Pass 1 §6.3): FABRICATION corrections are SELECTED from a
    # closed strategy set, never composed - the same rule over_settling
    # above already follows, and for the same recorded reason: handed a
    # certainty-related signal, the generative reroot path once invented
    # supporting sources (Tertullian/Hermas, outside the world's span) to
    # illustrate a limit already stated correctly without them. The
    # adjudicator has already named the specific claim; the strategy per
    # verdict is fixed, its words slotted in, zero further model calls.
    if signal.signal_type == "fabrication":
        kind, reason = "", ""
        for line in signal.description.split("\n"):
            if line.startswith("Adjudication:"):
                verdict_part = line.split(":", 1)[1].strip()
                kind, _, reason = verdict_part.partition(" - ")
                kind = kind.strip()
                reason = reason.strip()
                break
        if kind == "intrinsic":
            return (
                "Your last turn attributed something your own record holds "
                f"differently: {reason} Set it right plainly in your next turn, "
                "from inside your own world's account, and reach for nothing "
                "beyond what your own record actually gives you."
            )
        # extrinsic verdict, or an unadjudicated stage-1 finding: the
        # provisional strategy - do not repeat, own the thinness
        claim = reason or signal.description.split("\n")[0]
        return (
            "Your last turn asserted something nothing in your own record "
            f"supports: {claim} Do not repeat it. If it comes up again, say "
            "plainly that your record does not carry it - honest thinness is "
            "always preferable to invented depth."
        )

    llm = get_monitoring_llm()
    prompt = FACILITATOR_REROOT_PROMPT.format(
        drift_description=f"{signal.signal_type}: {signal.description}"
    )
    response = llm.invoke([
        SystemMessage(content=prompt),
        HumanMessage(content="Provide correction guidance."),
    ])
    log_llm_usage("reroot_guidance", response, _MONITORING_MODEL)
    return response.content.strip()


def facilitator_monitors(state: ConversationState) -> dict:
    """
    Facilitator invisibly monitors the CURRENT speaker's most recent turn
    for drift.

    Kept as the single-turn entry point for the non-streaming /message
    endpoint, where there is only ever one turn to check. The streaming
    endpoint instead calls check_drift_for_message once per turn completed
    in a round, since this function only ever sees the last speaker.
    """
    current_world_id = state.current_world_id or state.world_id
    rep_message_name = get_representative_message_name(current_world_id)

    last_rep_message = None
    for msg in reversed(state.messages):
        if hasattr(msg, "name") and msg.name == rep_message_name:
            last_rep_message = msg.content
            break

    if not last_rep_message:
        return {"requires_reroot": False}

    signal = _detect_drift_signal(last_rep_message, world_id=current_world_id)
    if signal is None:
        return {"requires_reroot": False}

    return {
        "drift_signals": [signal],
        "requires_reroot": signal.severity in ("medium", "high"),
    }


def facilitator_reroots(state: ConversationState) -> dict:
    """
    Facilitator provides invisible correction guidance after drift detection.

    This guidance is injected into the representative's context for their
    next response, but is not visible to the participant. Kept for the
    non-streaming /message endpoint's global requires_reroot flow; the
    streaming endpoint instead calls generate_reroot_guidance directly and
    routes the result through pending_guidance[world_id].
    """
    if not state.drift_signals:
        return {"requires_reroot": False}

    last_signal = state.drift_signals[-1]
    correction = generate_reroot_guidance(last_signal)

    updated_signal = DriftSignal(
        signal_type=last_signal.signal_type,
        description=f"{last_signal.description}\n\nCorrection: {correction}",
        severity=last_signal.severity,
        world_id=last_signal.world_id,
    )

    return {
        "drift_signals": [updated_signal],
        "requires_reroot": True,  # Keep flag set so representative uses it
    }


def facilitator_closes(state: ConversationState) -> dict:
    """
    Facilitator offers a warm, brief goodbye without summarizing.

    This marks the end of the conversation.
    """
    llm = get_llm()

    response = llm.invoke([
        SystemMessage(content=FACILITATOR_CLOSING_PROMPT),
        HumanMessage(content="The participant is leaving. Please offer a closing."),
    ])
    log_llm_usage("facilitator_close", response, settings.llm_model,
                  session_id=state.session_id)

    return {
        "messages": [AIMessage(content=response.content, name="facilitator")],
        "phase": "closing",
        "current_speaker": "facilitator",
    }


# Routing functions
def route_after_monitoring(state: ConversationState) -> Literal["reroot", "wait", "close"]:
    """Route after monitoring based on drift detection and close request."""
    if state.close_requested:
        return "close"
    if state.requires_reroot:
        return "reroot"
    return "wait"


def route_after_input(state: ConversationState) -> Literal["engage", "close"]:
    """Route after receiving participant input."""
    if state.close_requested:
        return "close"
    return "engage"


# S4.4a (Pass 1 §6.2 item 1): direct-address detection - the cheap,
# deterministic check that runs BEFORE any selector/router LLM call.
# Enforces Facilitator Governance §8's own requirement: "When the
# participant addresses a specific Representative, you route accordingly.
# Immediately, completely, without editorial intervention." Conservative
# by design: it fires only when exactly ONE seated representative is
# named and no to-the-whole-table marker is present; every ambiguous case
# falls through to the holistic selector, which §6.2 item 3 keeps for
# exactly that regime. Address by role/title alone ("presbyter", "elder")
# is deliberately NOT detected here - that judgment belongs to the
# selector, not a string check.

_ALL_TABLE_MARKERS = (
    "each of you", "all of you", "you all", "both of you", "you both",
    "everyone", "every one of you", "each of your", "all of your",
    "you three", "you two", "any of you",
)


def _sentences(text: str) -> list[str]:
    """Cheap sentence split, terminators kept."""
    return [s.strip() for s in re.findall(r"[^.!?]*[.!?]", text)] or (
        [text.strip()] if text.strip() else [])


def _rep_display_names(world_ids: list[str]) -> dict[str, str]:
    from app.prompts.facilitator_prompts import REPRESENTATIVE_INFO
    return {wid: REPRESENTATIVE_INFO[wid]["name"]
            for wid in world_ids if wid in REPRESENTATIVE_INFO}


def _named_reps_in(text: str, world_ids: list[str]) -> list[str]:
    """world_ids whose representative's display name appears in text
    (word-boundary, case-insensitive), in seating order."""
    found = []
    for wid, name in _rep_display_names(world_ids).items():
        if re.search(r"\b" + re.escape(name) + r"\b", text, re.IGNORECASE):
            found.append(wid)
    return found


def detect_direct_address(message: str, world_ids: list[str]) -> str | None:
    """Participant → Representative direct address: exactly one seated
    representative named, no whole-table marker. Returns the world_id or
    None (fall through to the holistic path)."""
    if len(world_ids) <= 1 or not message:
        return None
    lowered = message.lower()
    if any(marker in lowered for marker in _ALL_TABLE_MARKERS):
        return None
    named = _named_reps_in(message, world_ids)
    return named[0] if len(named) == 1 else None


def detect_rep_to_rep_address(turn_text: str, speaker_world_id: str | None,
                              world_ids: list[str]) -> str | None:
    """Representative → Representative direct question: a question
    sentence in the previous representative's turn naming exactly one
    OTHER seated representative. The LAST such question wins (it is the
    outstanding first pair part). Returns the addressed world_id or None."""
    if len(world_ids) <= 1 or not turn_text:
        return None
    others = [w for w in world_ids if w != speaker_world_id]
    addressed = None
    for sent in _sentences(turn_text):
        if not sent.endswith("?"):
            continue
        named = _named_reps_in(sent, others)
        if len(named) == 1:
            addressed = named[0]
    return addressed


def outstanding_first_pair_parts(messages, world_ids: list[str]) -> list[dict]:
    """S4.4a (Pass 1 §6.2 item 4): the genuinely unanswered direct
    questions, derived deterministically from the transcript itself - no
    stored counter to drift out of sync with the messages it summarizes.

    A question OPENS when a turn contains a question sentence: asked by
    the participant (addressee = the named representative, else the open
    table) or by a representative (addressee = the named other
    representative, else the participant). A question RESOLVES when its
    addressee next speaks: the named representative for a directed one,
    any representative for an open-table one, the participant for a
    participant-directed one. What remains is outstanding - which is what
    the stacking check should count, not turns that happen to end in
    '?' (a clarification question that was answered in-round is exactly
    the act REACTIVE_TURN_GUIDANCE's 'Ask, Don't Just Answer' licenses,
    and the old shape of this check penalized it)."""
    name_by_wid = {wid: get_representative_message_name(wid)
                   for wid in world_ids}
    wid_by_name = {v: k for k, v in name_by_wid.items()}

    outstanding: list[dict] = []
    for msg in messages:
        if isinstance(msg, HumanMessage):
            speaker = "participant"
        else:
            speaker = getattr(msg, "name", None)
        if speaker is None or speaker == "facilitator":
            # facilitator turns are governance, not table content: they
            # neither open first pair parts nor answer another's
            continue
        speaker_wid = wid_by_name.get(speaker)

        def _resolved(q) -> bool:
            if q["addressee"] == "participant":
                return speaker == "participant"
            if q["addressee"] == "table":
                return speaker_wid is not None
            return q["addressee"] == speaker_wid

        outstanding = [q for q in outstanding if not _resolved(q)]

        text = str(msg.content)
        for sent in _sentences(text):
            if not sent.endswith("?"):
                continue
            if speaker == "participant":
                named = _named_reps_in(sent, world_ids)
                addressee = named[0] if len(named) == 1 else "table"
            else:
                named = _named_reps_in(
                    sent, [w for w in world_ids if w != speaker_wid])
                addressee = named[0] if len(named) == 1 else "participant"
            outstanding.append(
                {"asker": speaker, "addressee": addressee, "text": sent})
    return outstanding


def determine_turn_type(state: ConversationState) -> tuple[str, list[str]]:
    """
    Determine the type of turn needed for a multi-world table.

    Returns a tuple of (turn_type, world_ids) where:
    - turn_type is "single" (one representative) or "all" (all representatives)
    - world_ids is the list of representatives who should respond

    The facilitator's curatorial judgment determines this based on:
    - Direct address to a specific representative → single
    - Question to all ("What do each of you think?") → all
    - Comparative questions → all
    - Continuing a thread with one representative → single (that representative)
    - General questions where multiple perspectives would illuminate → all
    """
    from app.prompts.facilitator_prompts import REPRESENTATIVE_INFO

    world_ids = state.world_ids if len(state.world_ids) > 0 else [state.world_id]

    # Single world - no routing complexity
    if len(world_ids) <= 1:
        return ("single", [state.world_id])

    # Get the last human message
    last_human_message = None
    for msg in reversed(state.messages):
        if isinstance(msg, HumanMessage):
            last_human_message = msg.content
            break

    if not last_human_message:
        return ("single", [state.current_world_id or world_ids[0]])

    # S4.4a: direct address decides the routing BEFORE the router LLM is
    # consulted - FG §8: "route accordingly. Immediately, completely,
    # without editorial intervention." The router call disappears on
    # exactly the turns where routing is already determined.
    addressed = detect_direct_address(last_human_message, world_ids)
    if addressed is not None:
        return ("single", [addressed])

    # Build representative info
    rep_names = []
    for wid in world_ids:
        info = REPRESENTATIVE_INFO.get(wid)
        if info:
            rep_names.append(f"- {info['name']} (world_id: {wid}): {info['description']}")

    # Use LLM to determine routing
    llm = get_monitoring_llm()
    routing_prompt = f"""You are the Facilitator determining how to route a question at The Table.

Representatives present:
{chr(10).join(rep_names)}

Participant's message:
"{last_human_message}"

Determine whether this question should go to:
1. ONE representative (if addressed to a specific person, or about their specific world/time)
2. ALL representatives (if asking for multiple perspectives, comparisons, or "what do you each think")

Consider:
- Direct address by name → that ONE representative
- "What do you all think?" or "How would each of you..." → ALL
- Comparative questions ("How do your traditions differ on...") → ALL
- Questions about a specific time period or practice → the ONE representative from that world
- General theological/spiritual questions where multiple views illuminate → ALL
- Follow-up on what one representative said → that ONE representative
- When genuinely in doubt between single and all, prefer single - a table where every question fans out to every world flattens into a panel, and another world can always be drawn in on a later turn if the exchange calls for it

Respond in this exact format:
TURN_TYPE: single OR all
WORLD_IDS: comma-separated list of world_ids who should respond

Example responses:
TURN_TYPE: single
WORLD_IDS: syriac-edessa-nisibis

TURN_TYPE: all
WORLD_IDS: syriac-edessa-nisibis, post-apostolic-house-church"""

    response = llm.invoke([
        SystemMessage(content=routing_prompt),
        HumanMessage(content="Determine the turn type."),
    ])
    log_llm_usage("turn_type_router", response, _MONITORING_MODEL,
                  session_id=state.session_id)

    # Parse response
    result = response.content.strip()
    turn_type = "single"
    responding_worlds = [state.current_world_id or world_ids[0]]

    for line in result.split("\n"):
        line = line.strip()
        if line.startswith("TURN_TYPE:"):
            turn_type = line.split(":", 1)[1].strip().lower()
        elif line.startswith("WORLD_IDS:"):
            ids_str = line.split(":", 1)[1].strip()
            parsed_ids = [wid.strip() for wid in ids_str.split(",")]
            # Validate the world IDs
            valid_ids = [wid for wid in parsed_ids if wid in world_ids]
            if valid_ids:
                responding_worlds = valid_ids

    return (turn_type, responding_worlds)


def determine_next_speaker(state: ConversationState) -> str:
    """
    Determine which single representative should speak next.

    For backwards compatibility - returns just the first responding world.
    """
    turn_type, responding_worlds = determine_turn_type(state)
    return responding_worlds[0] if responding_worlds else state.world_id


def route_to_representative(state: ConversationState) -> dict:
    """
    Route the conversation to the appropriate representative(s).

    In multi-world tables, determines which representative(s) should respond.
    """
    turn_type, responding_worlds = determine_turn_type(state)
    return {
        "current_world_id": responding_worlds[0],
        # Store all responding worlds for multi_representative_engages
    }


def select_next_speaker(
    state: ConversationState,
    already_spoken: list[str],
    must_continue: bool = False,
    reason_sink: list | None = None,
) -> str | None:
    """
    Decide which representative should speak next in this round, or that the
    round is already complete.

    Called before the first representative speaks (already_spoken=[]) and
    again after each turn, so the order, length, and shape of a multi-
    representative round emerges from the actual conversation instead of a
    fixed rotation through every world at the table. This is the "most
    directly positioned" turn-taking principle from Facilitator Governance
    V3.6 Section 8: not rotation, not equal time, but which voice is most
    directly positioned to meet this specific moment.

    Representatives may be selected more than once in a round - real
    conversation is not "everyone speaks once then done," it's opening,
    response, response-to-the-response, sometimes a third voice joining
    partway through. The only hard rule is no immediate self-repeat (the
    representative who just spoke doesn't speak again next with nothing new
    to react to) and no repeat of the exact position the transcript already
    shows.

    must_continue: when True, NONE is not offered as an option - used to
    enforce a minimum amount of back-and-forth before a round is allowed to
    end (see MIN_MULTI_WORLD_TURNS in the streaming endpoint).

    reason_sink (S4.4a): a caller-supplied list; when the selection
    carries a reason - the LLM path's previously-discarded REASON line,
    or the deterministic direct-address note - it is appended here and
    delivered to the selected speaker as a private directive (Pass 1
    §6.2 item 3, the Confronting act). Old recorded stubs of this
    function ignore the parameter, degrading replay to no-directive
    rather than breaking.

    Returns a world_id, or None if nothing further calls for a voice right
    now (never returned while must_continue is True).
    """
    from app.prompts.facilitator_prompts import REPRESENTATIVE_INFO

    world_ids = state.world_ids if len(state.world_ids) > 0 else [state.world_id]
    just_spoke = already_spoken[-1] if already_spoken else None
    candidates = [wid for wid in world_ids if wid != just_spoke]

    if not candidates:
        return None

    # S4.4a: direct-address detection runs BEFORE the holistic selector
    # (Pass 1 §6.2 item 1; FG §8: "route accordingly. Immediately,
    # completely, without editorial intervention"). The selector LLM call
    # disappears on exactly the turns where selection is already
    # determined. Participant → Rep on the round's opening turn; Rep →
    # Rep direct question on reactive turns.
    last_msg = state.messages[-1] if state.messages else None
    if last_msg is not None:
        addressed = None
        directive = None
        display = _rep_display_names(world_ids)
        if isinstance(last_msg, HumanMessage):
            addressed = detect_direct_address(str(last_msg.content), world_ids)
            if addressed is not None:
                directive = ("The participant addressed you by name - "
                             "answer them directly.")
        else:
            speaker_name = getattr(last_msg, "name", None)
            if speaker_name and speaker_name != "facilitator":
                speaker_wid = next(
                    (w for w in world_ids
                     if get_representative_message_name(w) == speaker_name),
                    None)
                if speaker_wid is not None:
                    addressed = detect_rep_to_rep_address(
                        str(last_msg.content), speaker_wid, world_ids)
                    if addressed is not None:
                        directive = (
                            f"{display.get(speaker_wid, 'The previous speaker')} "
                            "just put a question to you directly - engage "
                            "that question specifically, from your own world.")
        if addressed is not None and addressed in candidates:
            if reason_sink is not None and directive:
                reason_sink.append(directive)
            return addressed

    # When continuation is mandatory and only one representative could
    # possibly speak next (a two-world table, the other one just spoke),
    # there is no real decision to make - the LLM call would only ever
    # confirm the sole candidate the fallback logic would pick anyway. Skip
    # it. This optimization does NOT apply when must_continue is False,
    # since then the real question isn't "who" but "this candidate, or is
    # the round actually done" - a genuine decision worth the call.
    if must_continue and len(candidates) == 1:
        return candidates[0]

    last_human_message = None
    for msg in reversed(state.messages):
        if isinstance(msg, HumanMessage):
            last_human_message = msg.content
            break

    if not last_human_message:
        # No question yet (e.g. opening turn) - the first world at the table opens.
        return candidates[0]

    public_transcript = build_public_transcript(state)

    rep_lines = []
    for wid in world_ids:
        info = REPRESENTATIVE_INFO.get(wid)
        if not info:
            continue
        times_spoken = already_spoken.count(wid)
        # Cross-round memory: how much this world has spoken across the
        # WHOLE conversation, not just this round. A world silent for
        # several consecutive rounds is invisible to a per-round count, so
        # per-round selection alone can let one pairing of worlds carry
        # every round while a third quietly disappears from the table.
        rep_msg_name = get_representative_message_name(wid)
        total_turns = sum(
            1 for m in state.messages if getattr(m, "name", None) == rep_msg_name
        )
        if times_spoken == 0 and total_turns == 0:
            status = "has not spoken yet this round, and has not spoken at all in this conversation"
        elif times_spoken == 0:
            status = f"has not spoken yet this round (spoke {total_turns} turn(s) earlier in the conversation)"
        elif wid == just_spoke:
            status = f"just spoke (spoken {times_spoken}x this round) - do not pick again immediately"
        else:
            status = f"has spoken {times_spoken}x this round, could return with something new"
        rep_lines.append(f"- {info['name']} (world_id: {wid}), {info['description']} — {status}")

    # S4.7 (Pass 1 §6.5): mode-dominance's correction is a SELECTION
    # input - when the last round's registers left the participant's own
    # register unmet, the selector is told, and may prefer the voice that
    # can meet it. Never a spoken intervention.
    register_line = ""
    if getattr(state, "register_note", None):
        register_line = f"\n\n{state.register_note}"

    none_option = (
        ""
        if must_continue
        else "\n\nIf every representative who has something real to add right now has already spoken, or the exchange between them has genuinely run its course, say NONE - a round does not have to keep going until someone forces a point."
    )
    none_instruction = "" if must_continue else " or NONE"

    prompt = f"""You are the Facilitator at The Table, silently deciding who speaks next. This decision is never announced to the participant.

Representatives at the table:
{chr(10).join(rep_lines)}

Participant's message:
"{last_human_message}"

What has been said at the table so far (most recent last):
{public_transcript}

The governing principle is not rotation and not equal time. Real conversation is not "everyone gives one statement in order" - it has shape: someone opens, another responds and then adds their own view, the first may come back once there's something new to answer, a third may jump in partway through instead of waiting their turn. Decide which representative is most directly positioned to speak into this specific moment - because the question addresses their world specifically, because what was just said calls for their agreement or their difference, because their formation would genuinely illuminate something not yet said, or because they have something new to add now that more has been said since they last spoke. A representative who already spoke is a completely valid choice if they now have something new to say in response to what came after their turn - but do not pick whoever just spoke; they need something new to have been said before they'd speak again. Weigh, too, who has gone quiet across the conversation as a whole - a world silent for several rounds is not owed a turn by rotation, but when the current moment genuinely touches their formation, prefer them over a voice that has already carried much of the conversation.{register_line}{none_option}

Respond in this exact format:
NEXT_SPEAKER: <world_id{none_instruction}>
REASON: <one sentence>"""

    llm = get_monitoring_llm()
    response = llm.invoke([
        SystemMessage(content=prompt),
        HumanMessage(content="Decide who speaks next."),
    ])
    log_llm_usage("turn_selector", response, _MONITORING_MODEL)

    next_speaker = None
    reason_line = None
    for line in response.content.strip().split("\n"):
        line = line.strip()
        if line.startswith("NEXT_SPEAKER:") and next_speaker is None:
            candidate = line.split(":", 1)[1].strip()
            if candidate in candidates:
                next_speaker = candidate
        elif line.startswith("REASON:"):
            # S4.4a: the REASON line was always generated and always
            # discarded - it becomes the selected speaker's private
            # directive. A new consumer, not a new model call.
            reason_line = line.split(":", 1)[1].strip()

    # When the round is required to continue, an unparseable or invalid
    # response must never fall through to None - that would silently end
    # the round early despite must_continue, defeating the whole guarantee.
    # Fall back to the first eligible candidate instead.
    if next_speaker is None and must_continue:
        next_speaker = candidates[0]

    if (next_speaker is not None and reason_sink is not None and reason_line
            and next_speaker != "NONE"):
        reason_sink.append(
            f"You are being called on because: {reason_line} "
            "Engage that specifically.")

    return next_speaker


def check_dominance(state: ConversationState) -> list[DriftSignal]:
    """
    Heuristic (no LLM call) check for one representative dominating the
    table's cumulative airtime.

    Counts words spoken by each representative across the whole conversation
    so far, not just the current round - dominance is a pattern across a
    conversation, not a single turn. Only fires once enough total
    representative speech exists for a share comparison to be meaningful,
    and only when more than one representative has actually had a chance
    to speak.
    """
    world_ids = state.world_ids if len(state.world_ids) > 0 else [state.world_id]
    if len(world_ids) <= 1:
        return []

    from app.prompts.facilitator_prompts import REPRESENTATIVE_INFO

    name_to_world = {get_representative_message_name(wid): wid for wid in world_ids}
    word_counts: dict[str, int] = {wid: 0 for wid in world_ids}

    for msg in state.messages:
        name = getattr(msg, "name", None)
        if name in name_to_world:
            word_counts[name_to_world[name]] += len(str(msg.content).split())

    total_words = sum(word_counts.values())
    spoken_worlds = [wid for wid, count in word_counts.items() if count > 0]

    if len(spoken_worlds) < 2 or total_words < 150:
        return []

    # S4.7 (Pass 1 §6.5): the floor-allocation view - a world SELECTED
    # every round can dominate the table at 40% of the words, invisible
    # to the word-share backstop. Turn-count share is the cheap proxy for
    # floor allocation; fires only at 3+ seated worlds with enough turns
    # for a share to mean anything.
    signals = []
    turn_counts: dict[str, int] = {wid: 0 for wid in world_ids}
    for msg in state.messages:
        name = getattr(msg, "name", None)
        if name in name_to_world:
            turn_counts[name_to_world[name]] += 1
    total_turns = sum(turn_counts.values())
    if len(world_ids) >= 3 and total_turns >= 6:
        for wid, tc in turn_counts.items():
            if tc / total_turns >= 0.5:
                info = REPRESENTATIVE_INFO.get(wid)
                name = info["name"] if info else wid
                signals.append(DriftSignal(
                    signal_type="dominance",
                    description=(
                        f"{name} has held the floor in {tc} of the {total_turns} "
                        "representative turns so far - not by talking long, but by "
                        "being the voice selected. Let others carry the coming "
                        "rounds; hold back unless directly called."
                    ),
                    severity="medium",
                    world_id=wid,
                ))

    for wid, count in word_counts.items():
        if count == 0:
            continue
        share = count / total_words
        # Threshold sits at 0.70, not lower: legitimate cross-world length
        # asymmetry is by design (a desert word is a sentence; a Syriac
        # demonstration is staged paragraphs - see each world's own
        # Permanent Prompt), so a longer-formed world holding a majority
        # word-share opposite a deliberately terse one is expected, not
        # dominance. Dominance here means crowding out, not merely
        # out-speaking a form that is short on purpose.
        if share >= 0.70:
            info = REPRESENTATIVE_INFO.get(wid)
            name = info["name"] if info else wid
            signals.append(DriftSignal(
                signal_type="dominance",
                description=(
                    f"{name} has taken roughly {round(share * 100)}% of all representative "
                    "speech in this conversation so far. Let your next turn be economical - "
                    "make one point well rather than covering everything you might say - so "
                    "the other voice(s) at this table have more room."
                ),
                severity="medium" if share < 0.8 else "high",
                world_id=wid,
            ))

    return signals


def check_convergence(state: ConversationState, spoken_this_round: list[str]) -> list[DriftSignal]:
    """
    LLM check (Haiku) for whether the representatives who spoke in this round
    are starting to sound like each other - borrowing vocabulary, agreeing
    without genuine engagement, or losing the distinctiveness that makes
    their formations actually different worlds. Only meaningful when 2+
    representatives spoke in the same round.
    """
    if len(spoken_this_round) < 2:
        return []

    name_to_world = {get_representative_message_name(wid): wid for wid in spoken_this_round}

    round_turns = []
    for msg in reversed(state.messages):
        name = getattr(msg, "name", None)
        if name in name_to_world:
            round_turns.append((name, msg.content))
        if len(round_turns) >= len(spoken_this_round):
            break
    round_turns.reverse()

    if len(round_turns) < 2:
        return []

    transcript_block = "\n\n".join(f"{name}: {content}" for name, content in round_turns)

    # S4.7 (Pass 1 §6.5): this check's target NARROWS to its real half -
    # a conceptual pact that OVERWRITES a world's own sense. Vocabulary
    # blending per se is lexical entrainment, the most robust documented
    # behavior of humans in real conversation - echoing a word is not
    # drift; adopting the other world's MEANING in place of your own is.
    # "Manufactured resolution" is a different phenomenon and is now its
    # own check (check_manufactured_resolution), scored against the
    # seated worlds' own documented divergences.
    prompt = f"""You are the Facilitator at The Table, checking for convergence drift - specifically, a conceptual pact that overwrites a world's own sense.

The bar, stated carefully: representatives in real conversation naturally echo one another's words - that alone is lexical entrainment, documented ordinary human behavior, and is NOT drift. The failure you are checking for is narrower: a representative adopting another world's MEANING in place of their own world's own sense - reasoning from the other formation's concept as if it were their own, so the two voices' senses collapse into one, or losing the distinctiveness that makes their reasoning genuinely different.

Representatives who spoke this round:
{transcript_block}

Did sense-overwriting convergence occur? Be conservative - echoed words with each world's own sense intact are NOT drift; serious engagement with what the other said is NOT drift; real agreement independently held by each formation is NOT drift. Flag only when a voice's own conceptual ground has been displaced by the other's.

Respond in this exact format:
CONVERGENCE_DETECTED: yes or no
SEVERITY: low, medium, or high (omit if not detected)
DESCRIPTION: one sentence (omit if not detected)"""

    llm = get_monitoring_llm()
    response = llm.invoke([
        SystemMessage(content=prompt),
        HumanMessage(content="Check for convergence drift."),
    ])
    log_llm_usage("convergence_check", response, _MONITORING_MODEL,
                  session_id=state.session_id)

    detected = False
    severity = "low"
    description = ""
    for line in response.content.strip().split("\n"):
        line = line.strip()
        if line.upper().startswith("CONVERGENCE_DETECTED:"):
            detected = "yes" in line.lower()
        elif line.upper().startswith("SEVERITY:"):
            value = line.split(":", 1)[1].strip().lower()
            if value in ("low", "medium", "high"):
                severity = value
        elif line.upper().startswith("DESCRIPTION:"):
            description = line.split(":", 1)[1].strip()

    if not detected:
        return []

    # Attribute to every representative who spoke this round - convergence is
    # a relationship between voices, not one representative's individual fault.
    return [
        DriftSignal(
            signal_type="convergence",
            description=(
                description or "Your voice converged with another representative's this round."
            )
            + " Return to your own formation's vocabulary and reasoning, even where it means genuine difference.",
            severity=severity,
            world_id=wid,
        )
        for wid in spoken_this_round
    ]


# Per-world hard word-count ceilings for representatives whose own Permanent
# Prompt states an explicit, all-conditions numeric measure. Both ceilings
# were tested at their most emphatic wording (Papnoute's PP names table
# pressure explicitly; Albina's now does too, added after live testing
# showed the qualitative version alone was not holding) and still failed
# under real multi-world topical load - this is a mechanical backstop for
# that specific, already-proven-resistant failure, not a substitute for the
# prompt text. Do not add worlds here whose PP only gives a qualitative
# measure ("a few sentences") without a stated number - a ceiling with no
# textual anchor in that world's own formation would be arbitrary.
_WORLD_LENGTH_CEILINGS: dict[str, int] = {
    "desert-monasticism": 60,
    "hieronymian-ascetic-literary": 180,
}


# Per-lane word ceilings. These exist because a written target does not bind.
# Measured over 45 live turns: lanes told to hold 90-140 words came in at 169
# and 197, while the two lanes with no number ran 306 and 288 against a no-lane
# baseline of 262 - both LONGER than having no lane at all. Lane guidance
# inflates length whatever it says, because it adds things to attend to.
# Instruction moved it partway; only measurement closes the rest.
#
# general and academic sit at the same 140: both designs state that band, and
# both lanes add their rigor through what fills a turn rather than its size.
#
# pastor-teacher is higher on purpose. Its design asks for depth on one thread,
# which legitimately costs more room than a visitor's answer, so it binds at the
# outer edge of the Representative's own fullest measure (Chloe's formation
# names two short paragraphs; the design spec's own demonstration answers run
# about 230) rather than at a tighter measure borrowed from another lane. Its
# real failure was threads, not words - 2.3 distinct threads per turn, single-
# thread on only 3 of 9 - and the semantically correct detector for that,
# OVER_PRODUCING, fired 0 times across all 45 turns despite being written for
# exactly this ("has become encyclopedic resource rather than voice with its own
# perspective"). A word count is a proxy for the real fault, chosen because it
# is the only mechanism here with a measured track record of firing at all.
#
# reevaluation is absent deliberately, not by oversight. Both directions are
# dangerous in that lane - short reads as managed, long reads as advocacy - so
# its design governs ordering and concreteness instead, and a ceiling would
# invent a constraint its guidance does not make.
_LANE_LENGTH_CEILINGS: dict[str, int] = {
    "general": 140,
    "academic": 140,
    "pastor-teacher": 220,
}


def _effective_length_ceiling(world_id: str, role: str | None) -> tuple[int | None, str]:
    """
    The binding word ceiling for one world under one lane, and which bound set
    it ("world" or "lane"). (None, "") when neither applies.

    A lane may only ever tighten a world's own measure, never loosen it - the
    design spec's rule that role guidance operates inside the Representative's
    own measure rather than over it. So this is a min(), and a world with a
    tighter formation than the lane keeps its own.
    """
    world_ceiling = _WORLD_LENGTH_CEILINGS.get(world_id)
    lane_ceiling = _LANE_LENGTH_CEILINGS.get(role) if role else None

    if world_ceiling is not None and lane_ceiling is not None:
        return (world_ceiling, "world") if world_ceiling <= lane_ceiling else (lane_ceiling, "lane")
    if world_ceiling is not None:
        return world_ceiling, "world"
    if lane_ceiling is not None:
        return lane_ceiling, "lane"
    return None, ""


def check_length_ceiling(state: ConversationState, spoken_this_round: list[str]) -> list[DriftSignal]:
    """
    Heuristic (no LLM call) check for a representative whose own Permanent
    Prompt states a hard per-turn word measure exceeding it on their most
    recent turn this round. Only checks worlds actually at this table and
    present in _WORLD_LENGTH_CEILINGS.
    """
    if not spoken_this_round:
        return []

    name_to_world = {get_representative_message_name(wid): wid for wid in spoken_this_round}
    last_turn_by_world: dict[str, str] = {}
    for msg in reversed(state.messages):
        name = getattr(msg, "name", None)
        wid = name_to_world.get(name)
        if wid and wid not in last_turn_by_world:
            last_turn_by_world[wid] = str(msg.content)
        if len(last_turn_by_world) >= len(name_to_world):
            break

    # Read defensively: participant_role exists only where the role-mode work
    # is present, and this check must behave identically (world ceilings only)
    # where it is not.
    role = getattr(state, "participant_role", None)

    signals = []
    for wid, content in last_turn_by_world.items():
        ceiling, bound_by = _effective_length_ceiling(wid, role)
        if ceiling is None:
            continue
        word_count = len(content.split())
        if word_count > ceiling:
            from app.prompts.facilitator_prompts import REPRESENTATIVE_INFO
            info = REPRESENTATIVE_INFO.get(wid)
            name = info["name"] if info else wid
            overage = word_count - ceiling
            if bound_by == "world":
                reason = (
                    "over the hard measure your own formation states. The pull to say more "
                    "because the table's exchange feels substantial is the exact pull your "
                    "own formation trains you to resist - let your next turn return to your "
                    "true measure, even mid-exchange."
                )
            else:
                # Never attributed to the Representative's own formation, which
                # would be false: this bound comes from who is listening, not
                # from the world. Kept in the same listener-descriptive register
                # the lane blocks themselves use.
                reason = (
                    "over the measure that serves the one at your table today. Say the one "
                    "thing this turn is for and let the rest wait to be asked for - what you "
                    "leave unsaid is what the next turn is for, and holding it back is what "
                    "leaves them room to ask."
                )
            signals.append(DriftSignal(
                signal_type="length_ceiling",
                description=f"{name}'s last turn ran {word_count} words, {overage} {reason}",
                severity="medium" if overage < ceiling else "high",
                world_id=wid,
            ))

    return signals


def check_question_stacking(state: ConversationState, spoken_this_round: list[str]) -> list[DriftSignal]:
    """
    Heuristic (no LLM call) check for too many unanswered questions stacked
    in one round. table_discourse.py's REACTIVE_TURN_GUIDANCE already asks
    representatives to notice this themselves ("One Open Question at the
    Table Is Enough") - this is the structural backstop for that prompt-only
    rule, mirroring the dominance/convergence pattern where a rule proved
    real but not fully self-enforcing under live conditions.

    S4.4a (Pass 1 §6.2 item 4): rebuilt on OUTSTANDING FIRST PAIR PARTS.
    The old shape counted round turns that happened to end in "?" - which
    penalized exactly the clarification act REACTIVE_TURN_GUIDANCE's
    "Ask, Don't Just Answer" licenses, even when the question was answered
    within the same round. Now the check counts the representative-asked
    questions still genuinely unanswered at round end (derived
    deterministically from the transcript - see
    outstanding_first_pair_parts); a question a later speaker actually
    answered no longer stacks.
    """
    if len(spoken_this_round) < 2:
        return []

    world_ids = state.world_ids if len(state.world_ids) > 0 else [state.world_id]
    outstanding = outstanding_first_pair_parts(state.messages, world_ids)
    round_rep_names = {get_representative_message_name(wid)
                       for wid in spoken_this_round}
    stacked = [q for q in outstanding if q["asker"] in round_rep_names]
    if len(stacked) <= 2:
        return []

    return [
        DriftSignal(
            signal_type="question_stacking",
            description=(
                f"This round left {len(stacked)} representative-asked questions "
                "genuinely unanswered - more open threads than the table can hold "
                "at once. Let your next turn end on your substance rather than "
                "adding another question, even if a real one occurs to you."
            ),
            severity="medium",
            world_id=wid,
        )
        for wid in spoken_this_round
    ]


_CROSS_WORLD_TERM_PATTERN_CACHE: dict[str, re.Pattern] = {}


def _term_boundary_pattern(term: str) -> re.Pattern:
    """Word-boundary, case-insensitive regex for a single lexicon term, cached by term string."""
    if term not in _CROSS_WORLD_TERM_PATTERN_CACHE:
        _CROSS_WORLD_TERM_PATTERN_CACHE[term] = re.compile(
            r"\b" + re.escape(term) + r"\b", re.IGNORECASE
        )
    return _CROSS_WORLD_TERM_PATTERN_CACHE[term]


def _extract_term_candidates(term_field: str) -> list[str]:
    """
    A lexicon chunk's raw "Term" field routinely packs multiple forms into
    one string - e.g. "qyama (ܩܝܡܐ) / bnay qyama / bnat qyama" or "madrasha
    (ܡܕܪܫܐ) / madrashe (plural)". Matching that whole string verbatim
    against a Representative's own ordinary speech never matches anything -
    this pulls out the actual candidate word-forms a Representative might
    plausibly say: parenthetical native-script glosses dropped, the
    remainder split on "/", each piece trimmed. Short fragments (under 3
    characters) are dropped as too generic to safely flag.
    """
    without_parens = re.sub(r"\([^)]*\)", "", term_field)
    candidates = [piece.strip() for piece in without_parens.split("/")]
    return [c for c in candidates if len(c) >= 3]


def _get_world_lexicon_terms(world_id: str) -> list[tuple[str, str]]:
    """(term, full_chunk_text) pairs for a world's own lexicon, for cross-world drift detection.

    One raw lexicon entry can yield more than one (term, chunk_text) pair,
    since its own Term field may pack multiple candidate forms together
    (see _extract_term_candidates) - each candidate carries the same chunk
    text back for the disambiguation prompt.
    """
    retriever = get_retriever(world_id)
    docs = list(retriever.vector_store.docstore._dict.values())
    pairs = []
    for doc in docs:
        raw_term = doc.metadata.get("term", "")
        if not raw_term:
            continue
        for candidate in _extract_term_candidates(raw_term):
            # S3.1: the disambiguation prompt needs the chunk body, which
            # now rides in metadata["content"] (page_content is the
            # retrieval surface)
            pairs.append((candidate, doc.metadata.get("content", doc.page_content)))
    return pairs


def check_cross_world_vocabulary_drift(
    state: ConversationState, spoken_this_round: list[str]
) -> list[DriftSignal]:
    """
    Deterministic-first check for a Representative literally using another
    seated world's own lexicon vocabulary - the specific "cross-world drift"
    signal named in Facilitator Governance V3.6 and self-disclosed there as
    unvalidated. Distinct from check_convergence, which only looks for
    voices blending or a manufactured shared conclusion within one round's
    transcript - this checks whether one specific Representative used a
    term that belongs, by this project's own lexicon record, to a
    DIFFERENT seated world's own formation.

    Cheap in the common case: a word-boundary string pre-filter against
    every other seated world's own lexicon terms runs first, with no LLM
    call, and almost always finds nothing. Only when a term-string actually
    appears in another Representative's turn does a small, targeted LLM
    call fire, checking that specific usage against the term's own Tier
    entry (its real Quick Meaning / Ecological Function, already sitting in
    the lexicon chunk) to confirm the term is being invoked in its real,
    world-specific conceptual sense - not a coincidental overlap. Syriac's
    own lexicon term "Mar" is also the ordinary English verb "to mar";
    plenty of other terms have subtler versions of the same problem. A bare
    string match cannot tell a real cross-world vocabulary borrowing from
    an ordinary word doing unrelated work in the sentence - only checking
    the usage against the term's own defined ecological meaning can.
    """
    if len(spoken_this_round) < 2:
        return []

    name_to_world = {get_representative_message_name(wid): wid for wid in spoken_this_round}

    round_turns: dict[str, str] = {}
    for msg in reversed(state.messages):
        name = getattr(msg, "name", None)
        if name in name_to_world and name_to_world[name] not in round_turns:
            round_turns[name_to_world[name]] = str(msg.content)
        if len(round_turns) >= len(spoken_this_round):
            break

    if len(round_turns) < 2:
        return []

    from app.prompts.facilitator_prompts import REPRESENTATIVE_INFO

    # S4.7: for MIGRATED worlds the disambiguation is judged against the
    # term record's own period_sense (the crisp defined sense) instead of
    # a raw chunk-text slice - substring matching stays only as the cheap
    # pre-filter it always was. Unmigrated worlds keep the chunk path.
    def _terms_for(wid: str):
        records = _term_records_for_world(wid)
        if records:
            return [(t[0], f"Period sense: {t[3]}\nQuick meaning: {t[2]}")
                    for t in records if t[0]]
        return _get_world_lexicon_terms(wid)

    terms_by_world = {wid: _terms_for(wid) for wid in round_turns}
    llm = get_monitoring_llm()
    signals: list[DriftSignal] = []

    for speaker_world_id, turn_text in round_turns.items():
        for other_world_id, other_terms in terms_by_world.items():
            if other_world_id == speaker_world_id:
                continue

            for term, chunk_text in other_terms:
                match = _term_boundary_pattern(term).search(turn_text)
                if not match:
                    continue

                context_window = turn_text[max(0, match.start() - 150): match.end() + 150]
                prompt = f"""A Representative formed within one world's own tradition just spoke. Their turn contains the string "{term}", a specific, defined technical term belonging to a DIFFERENT world's own vocabulary - not this Representative's own formation.

That other world's own definition of this term:
{chunk_text[:800]}

The Representative's actual sentence where the string appeared:
"{context_window}"

Is "{term}" here being used to invoke that OTHER world's own specific, technical, ecological meaning of the term - a real cross-world vocabulary borrowing - or is it incidental: an ordinary word, a coincidental homograph, a proper name, or some other sense entirely unrelated to that world's own concept?

Respond with exactly one word: INVOKING or INCIDENTAL."""

                try:
                    response = llm.invoke([HumanMessage(content=prompt)])
                    log_llm_usage("vocab_drift_verdict", response, _MONITORING_MODEL,
                                  session_id=state.session_id)
                    verdict = response.content.strip().upper()
                except Exception:
                    continue

                if "INVOKING" not in verdict:
                    continue

                other_info = REPRESENTATIVE_INFO.get(other_world_id)
                other_name = other_info["name"] if other_info else other_world_id
                signals.append(DriftSignal(
                    signal_type="cross_world_vocabulary",
                    description=(
                        f"You used \"{term}\", which belongs specifically to {other_name}'s own "
                        f"formation, not yours. Speak of this concept in your own world's own "
                        f"vocabulary instead."
                    ),
                    severity="medium",
                    world_id=speaker_world_id,
                ))
                # One confirmed borrowing is enough to queue a correction for
                # this speaker this round - move on to the next speaker
                # rather than piling up redundant signals for the same turn.
                break
            else:
                continue
            break

    return signals


# ---------------------------------------------------------------------------
# S4.7 (Pass 1 §6.4/§6.5) - term-record loaders, the three new table
# checks, restricted-offer planning, and the mode-register observation
# ---------------------------------------------------------------------------

_WRS_RECORDS_ROOT = Path(__file__).resolve().parents[2] / "wrs" / "records"


@functools.lru_cache(maxsize=8)
def _term_records_for_world(world_id: str) -> tuple:
    """(term, aliases, quick_meaning, period_sense, grounding_criterion)
    tuples from a MIGRATED world's term records - empty for unmigrated
    worlds (the compatibility classification). grounding_criterion is the
    §6.4 DERIVED criterion, computed at migration (e.g. desertlex001's
    'Sharp then-vs-now gap: high grounding criterion by rule')."""
    import yaml
    out = []
    try:
        for p in sorted(_WRS_RECORDS_ROOT.glob("*/term/*.md")):
            try:
                front = yaml.safe_load(
                    p.read_text(encoding="utf-8").split("---", 2)[1])
                if front.get("world_id") != world_id:
                    continue
                out.append((
                    str(front.get("term", "")),
                    tuple(front.get("aliases") or []),
                    str(front.get("quick_meaning", "")),
                    str(front.get("period_sense", "")),
                    str(front.get("grounding_criterion", "")),
                ))
            except Exception:
                continue
    except Exception:
        pass
    return tuple(out)


def check_misattribution(state: ConversationState,
                         spoken_this_round: list[str]) -> list[DriftSignal]:
    """S4.7 (Pass 1 §6.5): 'Name What They Actually Said' is instructed
    but was never verified - when a Representative characterizes another's
    position, a cheap targeted check against the named world's actual
    prior turns. The grounding gap's Representative-to-Representative
    face, and the recorded fabrication class (a real voice cited for
    something it did not say) - no other signal covers it."""
    if len(spoken_this_round) < 2:
        return []

    world_ids = state.world_ids if len(state.world_ids) > 0 else [state.world_id]
    display = _rep_display_names(world_ids)
    name_to_world = {get_representative_message_name(wid): wid
                     for wid in world_ids}

    # this round's turns, in order
    round_turns: list[tuple[str, str]] = []
    for msg in reversed(state.messages):
        wid = name_to_world.get(getattr(msg, "name", None))
        if wid is not None:
            round_turns.append((wid, str(msg.content)))
        if len(round_turns) >= len(spoken_this_round):
            break
    round_turns.reverse()

    llm = get_monitoring_llm()
    signals: list[DriftSignal] = []
    for speaker_wid, turn_text in round_turns:
        named = [w for w in _named_reps_in(turn_text, world_ids)
                 if w != speaker_wid]
        for other_wid in named:
            other_name = get_representative_message_name(other_wid)
            prior = [str(m.content) for m in state.messages
                     if getattr(m, "name", None) == other_name]
            if not prior:
                continue
            prior_text = "\n\n".join(prior[-2:])[:2500]
            prompt = (
                f"A representative just referred to {display.get(other_wid, other_wid)} "
                "by name. Check ONLY whether they characterized "
                f"{display.get(other_wid, other_wid)}'s position, and if so whether the "
                "characterization matches what was ACTUALLY said.\n\n"
                f"What {display.get(other_wid, other_wid)} actually said (their own prior "
                f"turns):\n\"\"\"{prior_text}\"\"\"\n\n"
                f"The turn referring to them:\n\"\"\"{turn_text[:2000]}\"\"\"\n\n"
                "Respond with exactly one word:\n"
                "- MISATTRIBUTED - the turn puts a position, claim, or words on "
                "them that their actual turns do not carry (including subtle "
                "restatements that shift what they said)\n"
                "- FAITHFUL - the characterization matches, OR the turn only "
                "addresses/asks them without characterizing their position.\n"
                "When unsure, answer FAITHFUL - only a clear mismatch is a finding."
            )
            try:
                response = llm.invoke([HumanMessage(content=prompt)])
                log_llm_usage("misattribution_check", response,
                              _MONITORING_MODEL, session_id=state.session_id)
                if "MISATTRIBUTED" not in response.content.strip().upper():
                    continue
            except Exception:
                continue
            signals.append(DriftSignal(
                signal_type="misattribution",
                description=(
                    f"Your last turn characterized {display.get(other_wid, other_wid)}'s "
                    "position in words their own turns do not carry. Name what "
                    "they actually said - quote or restate it faithfully - or "
                    "ask them, rather than attributing."
                ),
                severity="high",
                world_id=speaker_wid,
            ))
            break
    return signals


def check_manufactured_resolution(state: ConversationState,
                                  spoken_this_round: list[str]) -> list[DriftSignal]:
    """S4.7 (Pass 1 §6.5): convergence's content half, split out - group-
    level sycophancy arriving at a tidy synthesis. Scored against the
    seated worlds' own documented divergences where records exist: a
    migrated world's contested_claim.divergence_partners naming another
    seated world means the worlds GENUINELY diverge on that ground, and a
    round converging on a tidy resolution there is manufactured."""
    if len(spoken_this_round) < 2:
        return []

    world_ids = state.world_ids if len(state.world_ids) > 0 else [state.world_id]
    name_to_world = {get_representative_message_name(wid): wid
                     for wid in world_ids}
    round_turns = []
    for msg in reversed(state.messages):
        name = getattr(msg, "name", None)
        if name in name_to_world:
            round_turns.append((name, str(msg.content)))
        if len(round_turns) >= len(spoken_this_round):
            break
    round_turns.reverse()
    if len(round_turns) < 2:
        return []
    transcript_block = "\n\n".join(f"{n}: {c}" for n, c in round_turns)

    # documented divergences between seated worlds (migrated records only)
    import yaml
    divergences = []
    try:
        for p in sorted(_WRS_RECORDS_ROOT.glob("*/contested_claim/*.md")):
            try:
                front = yaml.safe_load(
                    p.read_text(encoding="utf-8").split("---", 2)[1])
                if front.get("world_id") not in world_ids:
                    continue
                for partner in front.get("divergence_partners") or []:
                    if partner.get("world_id") in world_ids:
                        divergences.append(
                            f"- {front.get('id')}: {str(front.get('claim'))[:200]} "
                            f"(diverges from {partner['world_id']}: "
                            f"{str(partner.get('note', ''))[:200]})")
            except Exception:
                continue
    except Exception:
        pass
    divergence_block = "\n".join(divergences) or (
        "(no records available for the seated pairing - judge from the "
        "round alone)")

    prompt = f"""You are the Facilitator, checking one round for MANUFACTURED RESOLUTION - a synthesis, resolving insight, or graceful shared conclusion tying the positions together neatly, when that conclusion is not something each formation would independently stand behind. Real impasse, stated plainly and left standing, is the correct outcome when a real impasse exists.

Documented divergences between the worlds at this table (their own records):
{divergence_block}

This round:
{transcript_block}

Be conservative: serious mutual engagement, honest agreement independently held, or one voice noting a resonance while KEEPING the difference standing - none of these is manufactured resolution. Flag only a tidy shared conclusion that dissolves a genuine divergence for the sake of a smooth ending.

Respond in this exact format:
MANUFACTURED: yes or no
SEVERITY: low, medium, or high (omit if no)
DESCRIPTION: one sentence (omit if no)"""

    llm = get_monitoring_llm()
    try:
        response = llm.invoke([
            SystemMessage(content=prompt),
            HumanMessage(content="Check the round above."),
        ])
        log_llm_usage("manufactured_resolution_check", response,
                      _MONITORING_MODEL, session_id=state.session_id)
    except Exception:
        return []

    detected, severity, description = False, "medium", ""
    for line in response.content.strip().split("\n"):
        line = line.strip()
        if line.upper().startswith("MANUFACTURED:"):
            detected = "yes" in line.lower()
        elif line.upper().startswith("SEVERITY:"):
            v = line.split(":", 1)[1].strip().lower()
            if v in ("low", "medium", "high"):
                severity = v
        elif line.upper().startswith("DESCRIPTION:"):
            description = line.split(":", 1)[1].strip()
    if not detected:
        return []
    return [
        DriftSignal(
            signal_type="manufactured_resolution",
            description=(description or "This round manufactured a shared "
                         "resolution.") + " Let the genuine difference stand "
            "- your worlds' own records diverge here, and an honest impasse "
            "serves the participant better than a tidy synthesis.",
            severity=severity,
            world_id=wid,
        )
        for wid in spoken_this_round
    ]


def check_closing_synthesis(state: ConversationState,
                            spoken_this_round: list[str]) -> list[DriftSignal]:
    """S4.7 (Pass 1 §6.5, the PART II reviewer finding): whoever speaks
    last gains unearned authority to characterize consensus. Checks ONLY
    the round's final turn for a totalizing closing frame."""
    if len(spoken_this_round) < 2:
        return []
    world_ids = state.world_ids if len(state.world_ids) > 0 else [state.world_id]
    name_to_world = {get_representative_message_name(wid): wid
                     for wid in world_ids}
    last_wid, last_text = None, None
    for msg in reversed(state.messages):
        wid = name_to_world.get(getattr(msg, "name", None))
        if wid is not None:
            last_wid, last_text = wid, str(msg.content)
            break
    if last_wid is None:
        return []

    prompt = (
        "You are the Facilitator, checking ONE thing about the FINAL turn "
        "of a multi-representative round: does it close the round by "
        "characterizing the whole table's shared direction, consensus, or "
        "underlying unity - a totalizing frame placed last ('we are all "
        "pointing the same direction', 'under all three answers lies one "
        "gravity'), where the speaker's own position stated as their own "
        "would have been the honest close?\n\n"
        f"The final turn:\n\"\"\"{last_text[:2000]}\"\"\"\n\n"
        "Respond with exactly one word: SYNTHESIS (it claims the table's "
        "collective direction as its closing frame) or OWN_GROUND (it "
        "closes on its own position, or addresses others without claiming "
        "what the table collectively holds). When unsure, OWN_GROUND."
    )
    llm = get_monitoring_llm()
    try:
        response = llm.invoke([HumanMessage(content=prompt)])
        log_llm_usage("closing_synthesis_check", response,
                      _MONITORING_MODEL, session_id=state.session_id)
        if "SYNTHESIS" not in response.content.strip().upper():
            return []
    except Exception:
        return []
    return [DriftSignal(
        signal_type="closing_synthesis",
        description=(
            "Your turn closed the round by characterizing what the whole "
            "table holds. The last word carries unearned authority to "
            "define consensus - close on your own world's ground instead, "
            "and let the Facilitator or the participant hold the whole."
        ),
        severity="medium",
        world_id=last_wid,
    )]


def plan_restricted_offer(state: ConversationState, message: str) -> dict | None:
    """S4.7 (Pass 1 §6.4): the one positive-evidence grounding mechanism.
    Deterministic, no LLM call: when the LAST representative turn cited a
    HIGH-grounding-criterion record (the criterion is derived data on the
    record, computed at migration) and the participant's next message
    shows no positive evidence of understanding (no mention of the term
    or its aliases), the answering turn OPENS with a restricted offer -
    a candidate understanding put forward for confirmation. Exactly ONE
    offer (the most recently cited high-criterion term) - over-offering
    is a graded failure. Migrated single-world sessions only (the offer
    puts forward the answering world's own sense; cross-world offers wait
    for migrated tables, S6.2)."""
    world_ids = state.world_ids if len(state.world_ids) > 0 else [state.world_id]
    if len(world_ids) != 1:
        return None
    world_id = world_ids[0]
    terms = _term_records_for_world(world_id)
    if not terms:
        return None
    rep_name = get_representative_message_name(world_id)
    last_rep_msg = next((m for m in reversed(state.messages)
                         if getattr(m, "name", None) == rep_name), None)
    if last_rep_msg is None:
        return None
    citations = (getattr(last_rep_msg, "additional_kwargs", None) or {}).get(
        "citations") or []
    cited_terms = [c.get("term", "") for c in citations]
    if not cited_terms:
        return None

    by_term = {t[0]: t for t in terms}
    lowered = message.lower()
    # S5.6 sustained re-runs (FLAG-018 investigation, layer 4 - the real
    # source of the "when I said X" false-referent openers): a citation
    # proves a chunk was RETRIEVED for the turn, not that the voice SPOKE
    # the term - offers were firing on retrieved-but-unspoken terms, so
    # the directive's own premise ("your last turn leaned on X") was
    # false, and the voice rendered that premise faithfully as "when I
    # said X." §6.4's intent is a term USED without acknowledgment: the
    # offer now requires the term (or an alias) in the representative's
    # actual spoken text, with citations kept only as the candidate list.
    last_rep_text = str(last_rep_msg.content).lower()
    for cited in reversed(cited_terms):  # most recent citation first
        rec = by_term.get(cited)
        if rec is None or rec[4] != "high":
            continue
        term, aliases, quick_meaning, _period_sense, _crit = rec
        probes = [re.sub(r"\([^)]*\)", "", term).strip()] + list(aliases)
        # the voice must actually have spoken the term for an offer to
        # have a true premise
        if not any(p and p.lower() in last_rep_text for p in probes):
            continue
        # positive evidence of understanding = the participant's next
        # message touches the term or any alias; strip parentheticals so
        # "Anachōrēsis (Withdrawal)" also matches on "withdrawal"
        if any(p and p.lower() in lowered for p in probes):
            continue
        display = re.sub(r"\s*\(.*", "", term).strip() or term
        return {
            "term": term,
            "directive": (
                "Grounding note: your last turn spoke of "
                f'"{term}" - a term whose sense then and now diverge sharply - '
                "and the participant has moved on without touching it. Your "
                "FIRST sentence this turn must be ONE restricted offer: a "
                "single short question putting forward your candidate "
                "understanding for confirmation - its real sense in your "
                f"world being: {quick_meaning} Then answer their message. "
                "This holds even inside your world's own word measure: the "
                "offer is one short sentence of it, never dropped for "
                "compression. One offer only; do not stack a second, and do "
                f"not turn the offer into a lecture on {display}."
            ),
        }
    return None


def classify_round_register(state: ConversationState,
                            spoken_this_round: list[str],
                            participant_message: str) -> dict | None:
    """S4.7 (Pass 1 §6.5): mode-dominance's first mechanism. One Haiku
    call per round classifying each speaking world's register this round
    (the six modes Facilitator Governance already enumerates: precision,
    argument, certainty, abstraction, image, silence) against the
    participant's own discerned register. The output is SELECTOR INPUT
    only (state.register_note via the register_observed event) - the
    correction is the selector calling the absent register, never a
    spoken intervention."""
    if len(spoken_this_round) < 2:
        return None
    world_ids = state.world_ids if len(state.world_ids) > 0 else [state.world_id]
    name_to_world = {get_representative_message_name(wid): wid
                     for wid in world_ids}
    round_turns = []
    for msg in reversed(state.messages):
        name = getattr(msg, "name", None)
        if name in name_to_world:
            round_turns.append((name, str(msg.content)[:800]))
        if len(round_turns) >= len(spoken_this_round):
            break
    round_turns.reverse()
    if not round_turns:
        return None
    block = "\n\n".join(f"{n}: {c}" for n, c in round_turns)

    prompt = (
        "Classify registers at a table of historical voices. The six modes: "
        "precision, argument, certainty, abstraction, image, silence.\n\n"
        f"The participant's message this round:\n\"{participant_message[:600]}\"\n\n"
        f"The representatives' turns:\n{block}\n\n"
        "Respond in exactly this format (one MODE line per speaker named "
        "above, using the speaker names as given):\n"
        "PARTICIPANT_REGISTER: <the mode the participant's own message most "
        "asks to be met in>\n"
        "MODE <speaker-name>: <that speaker's dominant mode this round>\n"
        "ABSENT: <the one mode from the six most conspicuously missing from "
        "the round given the participant's register, or NONE>"
    )
    llm = get_monitoring_llm()
    try:
        response = llm.invoke([HumanMessage(content=prompt)])
        log_llm_usage("register_classification", response,
                      _MONITORING_MODEL, session_id=state.session_id)
        result = (response.content or "").strip()
    except Exception:
        return None
    participant_register, modes, absent = None, {}, None
    for line in result.splitlines():
        line = line.strip()
        if line.upper().startswith("PARTICIPANT_REGISTER:"):
            participant_register = line.split(":", 1)[1].strip().lower()
        elif line.upper().startswith("MODE "):
            rest = line[5:]
            if ":" in rest:
                who, mode = rest.split(":", 1)
                wid = name_to_world.get(who.strip())
                if wid:
                    modes[wid] = mode.strip().lower()
        elif line.upper().startswith("ABSENT:"):
            v = line.split(":", 1)[1].strip().lower()
            absent = None if v == "none" else v
    if not modes:
        return None
    return {"participant_register": participant_register,
            "modes": modes, "absent": absent}
