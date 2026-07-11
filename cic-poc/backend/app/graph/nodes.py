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


def build_public_transcript(state: ConversationState, exclude_world_id: str = None) -> str:
    """
    Build the public transcript - the record of what has been spoken at The Table.

    The public transcript is what Representatives share with each other.
    Each Representative sees what others have said, but not their inner formation.
    This is how Representatives encounter each other: through words spoken at the Table.
    """
    transcript_lines = []
    for msg in state.messages:
        if isinstance(msg, HumanMessage):
            transcript_lines.append(f"Participant: {msg.content}")
        elif hasattr(msg, "name") and msg.name:
            # Skip facilitator messages in transcript for representatives
            if msg.name == "facilitator":
                continue
            # Include other representatives' messages
            speaker_name = msg.name.replace("_", " ").title()
            transcript_lines.append(f"{speaker_name}: {msg.content}")

    return "\n\n".join(transcript_lines[-10:])  # Last 10 exchanges


def representative_engages(state: ConversationState) -> dict:
    """
    The representative responds to the participant with RAG-augmented context.

    This is the main conversation loop node. In multi-world tables, uses
    current_world_id to determine which representative speaks.

    Representatives see the "public transcript" - what has been said at The Table -
    allowing them to respond to what other representatives have said.
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

    # Build the public transcript - what has been said at The Table
    public_transcript = build_public_transcript(state)

    # Retrieve relevant lexicon context
    retrieved_context = retriever.get_context_for_response(
        query=last_human_message,
        conversation_context=public_transcript,
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

    # For multi-world, add the public transcript and guidance on encountering other voices
    if is_multi_world and public_transcript:
        other_reps = []
        for wid in world_ids:
            if wid != current_world_id:
                other_reps.append(get_representative_name(wid))

        system_prompt += f"""

# The Public Transcript — What Has Been Said at This Table

Also present at this table: {', '.join(other_reps)}.

Below is the record of what has been spoken at this Table. You encounter the other voices here through their words — not through access to their inner formation, but through what they have said aloud. You may find resonance with what another has said. You may find difference. You may find things you cannot fully reach from your own formation. Respond as yourself — bringing your own vocabulary, your own reasoning, your own formation to bear on what you have heard.

You are not obligated to respond to everything the others have said. But when their words touch something you recognize or something that differs from how your formation has shaped you, you may name it. The participant is witnessing this encounter between worlds.

PUBLIC TRANSCRIPT:
{public_transcript}
"""

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


def multi_representative_engages(state: ConversationState) -> dict:
    """
    Multiple representatives respond to a question at The Table.

    When a question is directed to all representatives, or when the facilitator
    determines multiple voices should respond, each representative speaks in turn.
    Each subsequent representative sees what the previous ones said in the public
    transcript, allowing genuine encounter between worlds.
    """
    from dataclasses import replace

    world_ids = state.world_ids if len(state.world_ids) > 0 else [state.world_id]

    if len(world_ids) <= 1:
        # Single world - delegate to regular function
        return representative_engages(state)

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

        # Get this representative's response
        result = representative_engages(working_state)

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
