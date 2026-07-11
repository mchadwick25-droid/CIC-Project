"""LangGraph node functions for The Table conversation."""

import re
from typing import Literal

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

from app.config import settings
from app.graph.state import ConversationState, DriftSignal, RetrievedContext
from app.prompts import (
    FACILITATOR_CLOSING_PROMPT,
    FACILITATOR_MONITORING_PROMPT,
    FACILITATOR_RECEPTION_PROMPT,
    FACILITATOR_REROOT_PROMPT,
    build_representative_prompt,
)
from app.prompts.facilitator_prompts import (
    get_facilitator_handoff_prompt,
    get_multi_world_handoff_prompt,
    get_representative_message_name,
    get_representative_name,
)
from app.prompts.representative_prompts import REPRESENTATIVE_CONTINUATION_PROMPT
from app.rag import LexiconRetriever


def get_llm():
    """Get the configured LLM."""
    if settings.llm_provider == "anthropic":
        from langchain_anthropic import ChatAnthropic

        return ChatAnthropic(
            model=settings.llm_model,
            anthropic_api_key=settings.anthropic_api_key,
        )
    else:
        from langchain_openai import ChatOpenAI

        return ChatOpenAI(
            model=settings.llm_model,
            openai_api_key=settings.openai_api_key,
        )


def get_monitoring_llm():
    """Get a faster LLM for monitoring (invisible operations)."""
    if settings.llm_provider == "anthropic":
        from langchain_anthropic import ChatAnthropic

        return ChatAnthropic(
            model="claude-haiku-4-5-20251001",
            anthropic_api_key=settings.anthropic_api_key,
        )
    else:
        from langchain_openai import ChatOpenAI

        return ChatOpenAI(
            model="gpt-4o-mini",
            openai_api_key=settings.openai_api_key,
        )


# Per-world retrievers cache
_retrievers: dict[str, LexiconRetriever] = {}


def get_retriever(world_id: str = "syriac-edessa-nisibis") -> LexiconRetriever:
    """Get or create the lexicon retriever for a specific world."""
    global _retrievers
    if world_id not in _retrievers:
        _retrievers[world_id] = LexiconRetriever(world_id=world_id)
    return _retrievers[world_id]


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

    return {
        "messages": [AIMessage(content=response.content, name="facilitator")],
        "phase": "handoff",
        "current_speaker": "facilitator",
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

    return {
        "messages": [AIMessage(content=response.content, name="facilitator")],
        "phase": "active_encounter",
        "current_speaker": "representative",
        "current_world_id": world_ids[0],  # First representative starts
    }


def representative_engages(state: ConversationState) -> dict:
    """
    The representative responds to the participant with RAG-augmented context.

    This is the main conversation loop node. In multi-world tables, uses
    current_world_id to determine which representative speaks.
    """
    llm = get_llm()

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

    # Get conversation context for RAG (last few exchanges)
    # In multi-world, include speaker names for context
    context_messages = []
    for msg in state.messages[-6:]:
        if isinstance(msg, HumanMessage):
            context_messages.append(f"Participant: {msg.content}")
        elif hasattr(msg, "name") and msg.name:
            # Use representative name for context
            context_messages.append(f"{msg.name}: {msg.content}")
        else:
            context_messages.append(f"Representative: {msg.content}")
    conversation_context = "\n".join(context_messages)

    # Retrieve relevant lexicon context
    retrieved_context = retriever.get_context_for_response(
        query=last_human_message,
        conversation_context=conversation_context,
    )

    # Check if there's reroot guidance from a previous drift detection
    reroot_guidance = ""
    if state.requires_reroot and state.drift_signals:
        last_signal = state.drift_signals[-1]
        reroot_guidance = f"Adjust for: {last_signal.description}"

    # Build the full system prompt
    system_prompt = build_representative_prompt(
        permanent_prompt=permanent_prompt,
        world_capsule=world_capsule,
        retrieved_context=retrieved_context,
        reroot_guidance=reroot_guidance,
    )

    # For multi-world, add awareness of other voices at table
    if is_multi_world:
        other_reps = []
        for wid in world_ids:
            if wid != current_world_id:
                other_reps.append(get_representative_name(wid))
        if other_reps:
            system_prompt += f"\n\n# Others at The Table\nAlso present at this table: {', '.join(other_reps)}. You may hear their voices in the conversation. You are not obligated to respond to them, but you may acknowledge what they have said if it is natural to do so. Speak from your own formation, not in reaction to theirs.\n"

    # Build message for continuation
    continuation = REPRESENTATIVE_CONTINUATION_PROMPT.format(message=last_human_message)

    # Get response
    response = llm.invoke([
        SystemMessage(content=system_prompt),
        HumanMessage(content=continuation),
    ])

    # Track retrieved terms for state
    retrieved_terms = []
    if retrieved_context:
        terms = re.findall(r"### ([^\n]+)", retrieved_context)
        retrieved_terms = terms

    return {
        "messages": [AIMessage(content=response.content, name=rep_message_name)],
        "turn_count": state.turn_count + 1,
        "requires_reroot": False,  # Clear reroot flag after using it
        "current_world_id": current_world_id,
        "retrieved_context": RetrievedContext(
            chunks=[retrieved_context] if retrieved_context else [],
            terms=retrieved_terms,
            sources=[],
        ) if retrieved_context else None,
    }


def facilitator_monitors(state: ConversationState) -> dict:
    """
    Facilitator invisibly monitors the representative's response for drift.

    This check happens after each representative turn but is invisible
    to the participant. In multi-world tables, monitors the current speaker.
    """
    llm = get_monitoring_llm()

    # Get the current representative's message name
    current_world_id = state.current_world_id or state.world_id
    rep_message_name = get_representative_message_name(current_world_id)

    # Get the last representative message from the current speaker
    last_rep_message = None
    for msg in reversed(state.messages):
        if hasattr(msg, "name") and msg.name == rep_message_name:
            last_rep_message = msg.content
            break

    if not last_rep_message:
        return {"requires_reroot": False}

    # Run drift detection
    prompt = FACILITATOR_MONITORING_PROMPT.format(response=last_rep_message)
    response = llm.invoke([
        SystemMessage(content=prompt),
        HumanMessage(content="Analyze the response above for drift signals."),
    ])

    result = response.content.strip()

    if result.startswith("DRIFT_DETECTED"):
        # Parse drift signal
        lines = result.split("\n")
        signal_type = "smoothing"
        severity = "low"
        description = ""

        for line in lines[1:]:
            if line.startswith("Signal:"):
                signal_type = line.split(":", 1)[1].strip().lower().replace("-", "_")
            elif line.startswith("Severity:"):
                severity = line.split(":", 1)[1].strip().lower()
            elif line.startswith("Description:"):
                description = line.split(":", 1)[1].strip()

        # Validate signal type
        valid_signals = [
            "smoothing", "generating", "agreeing", "first_person",
            "anachronism", "fabrication", "apologetics"
        ]
        if signal_type not in valid_signals:
            signal_type = "smoothing"

        drift_signal = DriftSignal(
            signal_type=signal_type,
            description=description,
            severity=severity,
        )

        return {
            "drift_signals": [drift_signal],
            "requires_reroot": severity in ["medium", "high"],
        }

    return {"requires_reroot": False}


def facilitator_reroots(state: ConversationState) -> dict:
    """
    Facilitator provides invisible correction guidance after drift detection.

    This guidance is injected into the representative's context for their
    next response, but is not visible to the participant.
    """
    if not state.drift_signals:
        return {"requires_reroot": False}

    last_signal = state.drift_signals[-1]
    llm = get_monitoring_llm()

    prompt = FACILITATOR_REROOT_PROMPT.format(
        drift_description=f"{last_signal.signal_type}: {last_signal.description}"
    )
    response = llm.invoke([
        SystemMessage(content=prompt),
        HumanMessage(content="Provide correction guidance."),
    ])

    # The reroot guidance is stored and will be used in the next representative turn
    # Update the last drift signal with the correction
    updated_signal = DriftSignal(
        signal_type=last_signal.signal_type,
        description=f"{last_signal.description}\n\nCorrection: {response.content}",
        severity=last_signal.severity,
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


def determine_next_speaker(state: ConversationState) -> str:
    """
    Determine which representative should speak next in a multi-world table.

    Uses LLM to analyze the participant's message and determine if it's
    directed at a specific representative or should go to the current one.

    Returns the world_id of the representative who should respond.
    """
    from app.prompts.facilitator_prompts import REPRESENTATIVE_INFO

    world_ids = state.world_ids if state.world_ids else [state.world_id]

    # Single world - no routing needed
    if len(world_ids) <= 1:
        return state.world_id

    # Get the last human message
    last_human_message = None
    for msg in reversed(state.messages):
        if isinstance(msg, HumanMessage):
            last_human_message = msg.content
            break

    if not last_human_message:
        return state.current_world_id or world_ids[0]

    # Build representative options
    rep_options = []
    for wid in world_ids:
        info = REPRESENTATIVE_INFO.get(wid)
        if info:
            rep_options.append(f"- {info['name']} (world_id: {wid}): {info['description']}")

    # Use LLM to determine routing
    llm = get_monitoring_llm()
    routing_prompt = f"""You are determining which representative should respond to the participant's message.

Representatives at the table:
{chr(10).join(rep_options)}

Current speaker: {state.current_world_id}

Participant's message:
"{last_human_message}"

Rules:
1. If the message directly addresses a representative by name, they should respond
2. If the message asks about something clearly within one representative's world (their time period, location, practices), they should respond
3. If the message is general or continues the current thread, the current speaker should continue
4. If the message asks for another perspective or comparison, consider switching

Respond with ONLY the world_id of the representative who should speak next. No explanation."""

    response = llm.invoke([
        SystemMessage(content=routing_prompt),
        HumanMessage(content="Which representative should respond?"),
    ])

    # Parse response - should be just the world_id
    suggested_world = response.content.strip().lower()

    # Validate the suggested world
    for wid in world_ids:
        if wid in suggested_world:
            return wid

    # Default to current speaker
    return state.current_world_id or world_ids[0]


def route_to_representative(state: ConversationState) -> dict:
    """
    Route the conversation to the appropriate representative.

    In multi-world tables, determines which representative should respond.
    """
    next_world_id = determine_next_speaker(state)
    return {"current_world_id": next_world_id}
