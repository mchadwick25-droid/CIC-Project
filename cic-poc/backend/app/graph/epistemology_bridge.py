"""
The epistemology bridge - a fourth classify-then-route intercept, mirroring
classify_frame_breaker / classify_modern_term.

This is FACILITATOR behavior and is WORLD-AGNOSTIC: it works the exact same
way for every world, with no per-world authoring. Some questions are
genuinely double-valenced between two readings that the frame-breaker
classifier is deliberately conservative about separating (Facilitator
Governance Section 12's "when genuinely unsure, prefer SUBSTANTIVE"):
"Where does documentation end and inference begin for you?" reads at once as
a real historiographical question about a tradition's OWN account of itself,
and as a question about this system's own construction. Passed through
unbridged, a Representative resolving that ambiguity toward the second
reading breaks character narrating its own construction (Governance Section
10, SELF_NARRATION) - confirmed live 2026-07-20, re-testing the exact
reproduction steps in
`Ministry/Operations/Audits/CiC_System_Hub_Handoff_RepresentativeSelfReference_2026-07-19.md`
against the frame-breaker classifier alone, which is not enough on its own
for this specific ambiguity by design.

Mirrors the anachronism bridge's shape: the Facilitator answers the
system-level half honestly and briefly (beat 1), then hands the
Representative a reframed, world-specific version of the same question -
never the version that invites self-narration (beat 2).
"""

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

from app.graph.state import ConversationState


def _extract_piece(content) -> str:
    if isinstance(content, list):
        return "".join(
            b.get("text", "") for b in content
            if isinstance(b, dict) and b.get("type") == "text"
        )
    return content or ""


def classify_epistemology_bridge(message: str) -> bool:
    """
    Decide whether an incoming participant message asks - in a way that is
    genuinely ambiguous between the tradition's own historical epistemology
    and this system's own construction - about the line between documented
    record and reasoned inference. Callers should only run this after
    classify_frame_breaker has already said this message is not a clear,
    unambiguous frame-breaker; a true "are you an AI" belongs to that
    classifier alone, not this one.

    Fails open to False (treat as ordinary substantive) on any parse
    ambiguity or error - the same discipline as classify_frame_breaker and
    classify_modern_term. A missed bridge falls through to normal
    Representative generation, where SELF_NARRATION monitoring is the
    existing second-layer backstop.
    """
    from app.graph.nodes import get_monitoring_llm
    from app.prompts.facilitator_prompts import FACILITATOR_EPISTEMOLOGY_BRIDGE_CLASSIFIER_PROMPT

    llm = get_monitoring_llm()
    try:
        response = llm.invoke([
            SystemMessage(content=FACILITATOR_EPISTEMOLOGY_BRIDGE_CLASSIFIER_PROMPT.format(message=message)),
            HumanMessage(content="Classify the message above."),
        ])
        result = response.content.strip().upper()
        return result.startswith("EPISTEMOLOGY_BRIDGE")
    except Exception:
        return False


def stream_epistemology_bridge(state: ConversationState):
    """
    Beat 1 (Facilitator: the honest, general, system-level acknowledgment -
    never world-specific, never claiming to speak for any tradition), then
    beat 2 (the Representative, answering the SAME question reframed toward
    their own world's specific epistemology). Mirrors
    stream_modern_term_bridge's shape exactly. Yields normalized events. The
    reframed handback message injected for the Representative is NEVER
    persisted to the transcript - only the `complete` messages yielded here
    are.
    """
    from app.graph.nodes import (
        REACTIVE_TURN_MAX_TOKENS,
        get_llm,
        stream_representative_turn,
    )
    from app.prompts.facilitator_prompts import (
        FACILITATOR_EPISTEMOLOGY_BRIDGE_PROMPT,
        get_representative_message_name,
        get_representative_name,
    )

    world_id = state.current_world_id or (state.world_ids[0] if state.world_ids else state.world_id)
    rep_name = get_representative_name(world_id)

    last_human_message = ""
    for msg in reversed(state.messages):
        if isinstance(msg, HumanMessage):
            last_human_message = _extract_piece(msg.content) if isinstance(msg.content, list) else msg.content
            break

    prompt = FACILITATOR_EPISTEMOLOGY_BRIDGE_PROMPT.format(
        representative_name=rep_name,
        message=last_human_message,
    )

    # --- Beat 1: the Facilitator, alone. ---
    yield {"type": "speaker_start", "speaker": "facilitator"}
    llm = get_llm(max_tokens=REACTIVE_TURN_MAX_TOKENS)
    full_text = ""
    for chunk in llm.stream([
        SystemMessage(content=prompt),
        HumanMessage(content="Respond as the Facilitator, per your instructions above."),
    ]):
        piece = _extract_piece(chunk.content)
        if piece:
            full_text += piece
            yield {"type": "token", "speaker": "facilitator", "text": piece}
    yield {"type": "speaker_end", "speaker": "facilitator", "citations": None}
    yield {
        "type": "complete",
        "speaker": "facilitator",
        "message": AIMessage(content=full_text, name="facilitator"),
    }

    # --- Beat 2: the Representative, on the reframed, world-specific question. ---
    rep_message_name = get_representative_message_name(world_id)
    handback_message = (
        "The participant just asked a question about the line between what's "
        "documented and what's inferred. Answer it about your OWN world only: "
        "in your own community's own account of itself, what was actually "
        "witnessed and written down directly, and what do you have to reason "
        "forward from silence, later custom, or a single voice's telling? "
        "Never describe how you personally are built or generated - answer as "
        "your world's own historiography, in your own terms."
    )
    working_state = ConversationState(
        messages=list(state.messages) + [HumanMessage(content=handback_message)],
        phase=state.phase,
        current_speaker="representative",
        current_world_id=world_id,
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
