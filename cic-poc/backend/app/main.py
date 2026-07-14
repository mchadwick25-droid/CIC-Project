"""FastAPI application for the CiC POC backend."""

import json
import re
import uuid
from contextlib import asynccontextmanager
from typing import Optional

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from pydantic import BaseModel

from app.config import settings
from app.graph.builder import get_compiled_graph
from app.graph.nodes import get_retriever, get_story_retriever, representative_engages
from app.graph.state import ConversationState
from app.world_manifest import WORLD_MANIFEST


# In-memory session storage (POC only)
sessions: dict[str, ConversationState] = {}


def load_world_content(world_id: str = "syriac-edessa-nisibis") -> tuple[str, str]:
    """Load the permanent prompt and world capsule content for a specific world."""
    world_config = settings.get_world_config(world_id)
    permanent_prompt = world_config.permanent_prompt_path.read_text(encoding="utf-8")
    world_capsule = world_config.world_capsule_path.read_text(encoding="utf-8")
    return permanent_prompt, world_capsule


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan handler."""
    # Pre-load the RAG indexes for all worlds on startup
    print("Loading RAG indexes for all worlds...")
    for world in AVAILABLE_WORLDS:
        try:
            get_retriever(world.id)
            print(f"  {world.name}: lexicon loaded successfully")
        except Exception as e:
            print(f"  {world.name}: Warning - Could not load lexicon index: {e}")
            print(f"    RAG retrieval will be attempted on first request")

        try:
            get_story_retriever(world.id)
            print(f"  {world.name}: stories loaded successfully")
        except Exception as e:
            print(f"  {world.name}: Warning - Could not load story index: {e}")
            print(f"    Story retrieval will be attempted on first request")

    yield

    # Cleanup
    sessions.clear()


app = FastAPI(
    title="Church in Conversation POC",
    description="The Table - Engaging conversations with voices from Christian history",
    version="0.1.0",
    lifespan=lifespan,
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Request/Response models
class StartSessionRequest(BaseModel):
    """Request to start a new session."""

    world_id: str = "syriac-edessa-nisibis"  # For single-world (backwards compat)
    world_ids: list[str] = []  # For multi-world table (1-3 worlds)


class StartSessionResponse(BaseModel):
    """Response for starting a new session."""

    session_id: str
    messages: list[dict]
    world_id: str  # Primary world (first in list)
    world_ids: list[str] = []  # All worlds at table


class SendMessageRequest(BaseModel):
    """Request to send a message."""

    message: str
    close_requested: bool = False


class SendMessageResponse(BaseModel):
    """Response after sending a message."""

    messages: list[dict]
    phase: str
    turn_count: int


class SessionResponse(BaseModel):
    """Response for getting session state."""

    session_id: str
    messages: list[dict]
    phase: str
    turn_count: int


def state_to_messages(state: ConversationState) -> list[dict]:
    """Convert state messages to serializable dicts."""
    result = []
    for msg in state.messages:
        role = "assistant"
        name = None

        if isinstance(msg, HumanMessage):
            role = "user"
        elif hasattr(msg, "name"):
            name = msg.name

        # Handle extended thinking responses where content is a list of blocks
        content = msg.content
        if isinstance(content, list):
            # Extract text content from content blocks
            text_parts = []
            for block in content:
                if isinstance(block, dict) and block.get("type") == "text":
                    text_parts.append(block.get("text", ""))
                elif isinstance(block, str):
                    text_parts.append(block)
            content = "\n".join(text_parts)

        citations = None
        if hasattr(msg, "additional_kwargs"):
            citations = msg.additional_kwargs.get("citations") or None

        result.append({
            "role": role,
            "content": content,
            "name": name,
            "citations": citations,
        })

    return result


@app.post("/api/session/start", response_model=StartSessionResponse)
async def start_session(request: StartSessionRequest):
    """
    Start a new conversation session.

    This initializes the conversation with the facilitator's welcome
    and introduction of the representative(s) for the selected world(s).

    Supports both single-world (world_id) and multi-world (world_ids) modes.
    Multi-world tables allow 1-3 representatives to engage together.
    """
    from app.graph.state import WorldContext

    session_id = str(uuid.uuid4())
    valid_world_ids = [w.id for w in AVAILABLE_WORLDS]

    # Determine which worlds are at the table
    if request.world_ids:
        # Multi-world mode
        world_ids = request.world_ids[:3]  # Cap at 3 worlds max (Prototype/Phase 1 scope - cost and complexity)
        for wid in world_ids:
            if wid not in valid_world_ids:
                raise HTTPException(
                    status_code=400,
                    detail=f"Invalid world_id '{wid}'. Must be one of: {valid_world_ids}"
                )
        world_id = world_ids[0]  # Primary world is first in list
    else:
        # Single-world mode (backwards compatible)
        world_id = request.world_id
        if world_id not in valid_world_ids:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid world_id. Must be one of: {valid_world_ids}"
            )
        world_ids = [world_id]

    # Load world content for primary world (legacy fields)
    permanent_prompt, world_capsule = load_world_content(world_id)

    # Build WorldContext for all worlds at the table
    worlds_at_table = []
    for wid in world_ids:
        w_prompt, w_capsule = load_world_content(wid)
        worlds_at_table.append(WorldContext(
            world_id=wid,
            permanent_prompt=w_prompt,
            world_capsule=w_capsule,
        ))

    # Create initial state
    initial_state = ConversationState(
        session_id=session_id,
        world_id=world_id,
        world_ids=world_ids,
        worlds_at_table=worlds_at_table,
        permanent_prompt=permanent_prompt,
        world_capsule_core=world_capsule,
        current_world_id=world_id,  # First representative speaks first
    )

    # Run the graph through reception and handoff
    graph = get_compiled_graph()
    result = graph.invoke(initial_state)

    # Convert result to ConversationState if needed
    if isinstance(result, dict):
        # Update state with results
        state = ConversationState(
            messages=result.get("messages", []),
            phase=result.get("phase", "active_encounter"),
            current_speaker=result.get("current_speaker", "representative"),
            turn_count=result.get("turn_count", 0),
            session_id=session_id,
            world_id=world_id,
            world_ids=world_ids,
            worlds_at_table=worlds_at_table,
            current_world_id=result.get("current_world_id", world_id),
            permanent_prompt=permanent_prompt,
            world_capsule_core=world_capsule,
        )
    else:
        state = result

    # Store session
    sessions[session_id] = state

    return StartSessionResponse(
        session_id=session_id,
        messages=state_to_messages(state),
        world_id=world_id,
        world_ids=world_ids,
    )


@app.post("/api/session/{session_id}/message", response_model=SendMessageResponse)
async def send_message(session_id: str, request: SendMessageRequest):
    """
    Send a message in an existing conversation.

    The message is processed by the representative (with RAG augmentation)
    and then monitored for drift by the facilitator.
    """
    if session_id not in sessions:
        raise HTTPException(status_code=404, detail="Session not found")

    state = sessions[session_id]

    # Handle close request
    if request.close_requested:
        state.close_requested = True

        # Run closing node
        from app.graph.nodes import facilitator_closes
        result = facilitator_closes(state)

        # Update state
        state.messages = list(state.messages) + result.get("messages", [])
        state.phase = result.get("phase", "closing")

        sessions[session_id] = state

        return SendMessageResponse(
            messages=state_to_messages(state),
            phase=state.phase,
            turn_count=state.turn_count,
        )

    # Add the participant's message
    state.messages = list(state.messages) + [HumanMessage(content=request.message)]

    # Frame-breaker check (see send_message_stream for the full rationale) -
    # applied here too since this endpoint is still live API surface, even
    # though the frontend's real conversation flow uses the streaming
    # endpoint above.
    from app.graph.nodes import classify_frame_breaker, get_llm
    from app.prompts import FACILITATOR_FRAME_BREAKER_RESPONSE_PROMPT

    if classify_frame_breaker(request.message):
        llm = get_llm()
        response = llm.invoke([
            SystemMessage(content=FACILITATOR_FRAME_BREAKER_RESPONSE_PROMPT.format(message=request.message)),
            HumanMessage(content="Respond as the Facilitator, per your instructions above."),
        ])
        state.messages = list(state.messages) + [AIMessage(content=response.content, name="facilitator")]
        sessions[session_id] = state
        return SendMessageResponse(
            messages=state_to_messages(state),
            phase=state.phase,
            turn_count=state.turn_count,
        )

    # Relational-safety check (see send_message_stream for the full
    # rationale) - runs only when the message wasn't already a frame-breaker,
    # since the two are effectively mutually exclusive categories and
    # frame-breaker's own classifier is already tested and should take
    # priority on any overlap.
    from app.graph.nodes import (
        classify_relational_safety,
        relational_safety_should_fire,
        stream_relational_safety_response,
        update_relational_safety_state,
    )

    rs_classification = classify_relational_safety(state, request.message)
    rs_updates = update_relational_safety_state(state, rs_classification)
    for field_name, value in rs_updates.items():
        setattr(state, field_name, value)

    if relational_safety_should_fire(state, rs_classification, rs_updates):
        new_message = None
        for event in stream_relational_safety_response(state, rs_classification, rs_updates):
            if event["type"] == "complete":
                new_message = event["message"]
        state.messages = list(state.messages) + [new_message]
        sessions[session_id] = state
        return SendMessageResponse(
            messages=state_to_messages(state),
            phase=state.phase,
            turn_count=state.turn_count,
        )

    # For multi-world tables, determine turn type (single or all representatives)
    from app.graph.nodes import determine_turn_type, multi_representative_engages

    if state.world_ids and len(state.world_ids) > 1:
        turn_type, responding_worlds = determine_turn_type(state)

        if turn_type == "all" and len(responding_worlds) > 1:
            # Multiple representatives should respond - each sees what others said
            state.current_world_id = responding_worlds[0]
            result = multi_representative_engages(state)
        else:
            # Single representative responds
            state.current_world_id = responding_worlds[0]
            result = representative_engages(state)
    else:
        # Single-world table
        result = representative_engages(state)

    # Update state with representative's response(s)
    state.messages = list(state.messages) + result.get("messages", [])
    state.turn_count = result.get("turn_count", state.turn_count)
    state.requires_reroot = result.get("requires_reroot", False)
    state.retrieved_context = result.get("retrieved_context")
    state.current_world_id = result.get("current_world_id", state.current_world_id)

    # Run monitoring
    from app.graph.nodes import facilitator_monitors, facilitator_reroots

    monitor_result = facilitator_monitors(state)
    state.requires_reroot = monitor_result.get("requires_reroot", False)

    if monitor_result.get("drift_signals"):
        state.drift_signals = list(state.drift_signals) + monitor_result["drift_signals"]

    # If reroot needed, run reroot (invisible to participant)
    if state.requires_reroot:
        reroot_result = facilitator_reroots(state)
        if reroot_result.get("drift_signals"):
            state.drift_signals = list(state.drift_signals) + reroot_result["drift_signals"]
        state.requires_reroot = reroot_result.get("requires_reroot", False)

    # Store updated session
    sessions[session_id] = state

    return SendMessageResponse(
        messages=state_to_messages(state),
        phase=state.phase,
        turn_count=state.turn_count,
    )


@app.post("/api/session/{session_id}/message/stream")
async def send_message_stream(session_id: str, request: SendMessageRequest):
    """
    Send a message and stream the representative(s)' response as Server-Sent Events.

    Emits one event per line as `data: {json}\\n\\n`:
    - speaker_start  {speaker}                      — a representative begins their turn
    - token          {speaker, text}                 — one chunk of generated text
    - speaker_end    {speaker, citations}             — that representative's turn is complete
    - done           {phase, turn_count}              — all speakers have finished; the participant may respond now. Invisible governance (dominance/convergence/drift monitoring) continues briefly in the background after this and is never streamed - see the end of event_stream() for why.
    - error          {message}                        — something went wrong; stream ends

    Closing the conversation (`close_requested`) is not streamed - use the
    plain /message endpoint for that, since it's a single short message.
    """
    if session_id not in sessions:
        raise HTTPException(status_code=404, detail="Session not found")

    if request.close_requested:
        raise HTTPException(
            status_code=400,
            detail="close_requested is not supported on the streaming endpoint - use /message",
        )

    state = sessions[session_id]
    state.messages = list(state.messages) + [HumanMessage(content=request.message)]

    from app.graph.nodes import (
        check_convergence,
        check_dominance,
        check_drift_for_message,
        classify_frame_breaker,
        classify_relational_safety,
        generate_reroot_guidance,
        relational_safety_should_fire,
        select_next_speaker,
        stream_frame_breaker_response,
        stream_relational_safety_response,
        stream_representative_turn,
        update_relational_safety_state,
    )
    from app.prompts.facilitator_prompts import get_representative_message_name

    # Frame-breaker check: a direct/adversarial question about a
    # Representative's own construction, nature, or grammar is intercepted
    # here, before any Representative generation is ever invoked, per
    # Governance V3.6 Section 10 (Self-Narration, CO-019) and Section 12
    # (frame-breaker trigger) - the recommended decoupled classify-then-route
    # design. See classify_frame_breaker's docstring for why this is a
    # separate call rather than something asked of representative generation
    # itself.
    is_frame_breaker = classify_frame_breaker(request.message)

    # Relational-safety check: Acute Distress / Harmful Dynamic, per
    # Governance V3.6 Section 12 as operationalized in CiC_L3D_
    # AcuteDistress_HarmfulDynamic_Mechanism_Proposal_DRAFT.md. Runs only
    # when the current message isn't already a frame-breaker - the two
    # categories are effectively mutually exclusive, and the frame-breaker
    # classifier already has a tested track record, so it takes priority on
    # any overlap rather than risking a double-classification race. State
    # updates (accumulator, track flags) are applied to `state` immediately
    # so they persist in `sessions[session_id]` even if this turn doesn't
    # itself fire - the accumulator has to see every turn to work at all.
    rs_classification = {"category": "NO_SIGNAL"}
    rs_updates: dict = {}
    is_relational_safety_firing = False
    if not is_frame_breaker:
        rs_classification = classify_relational_safety(state, request.message)
        rs_updates = update_relational_safety_state(state, rs_classification)
        for field_name, value in rs_updates.items():
            setattr(state, field_name, value)
        is_relational_safety_firing = relational_safety_should_fire(state, rs_classification, rs_updates)

    world_ids = state.world_ids if len(state.world_ids) > 0 else [state.world_id]
    is_multi_world = len(world_ids) > 1

    # A multi-representative round should never be "everyone states their
    # position once, done" - real conversation is opening, response,
    # response-to-the-response, sometimes a third voice joining partway
    # through. MIN enforces at least one direct answer to the question (the
    # opening turn) plus two further rounds of exchange before the selector
    # is even allowed to end the round. MAX is just a cost/latency backstop,
    # not a target - most rounds should end well before it from genuine
    # exhaustion of what's worth saying, not from hitting a ceiling. Capped
    # at 4 (not 6) after live testing showed a 6-turn round chains 15+
    # sequential API calls (selector + generation per turn, plus dominance/
    # convergence/monitor checks) and runs 90+ seconds end to end - late
    # turns in that long a chain came back truncated or empty even with a
    # retry safety net, most likely from cumulative request latency rather
    # than anything wrong with an individual call.
    MIN_MULTI_WORLD_TURNS = 3
    MAX_MULTI_WORLD_TURNS = 4

    def sse(event: dict) -> str:
        return f"data: {json.dumps(event)}\n\n"

    def event_stream():
        if is_frame_breaker:
            # Facilitator-only turn, per Section 12's "surface, answer,
            # recede" posture - no Representative is invoked, no turn
            # selection runs, and this does not count toward
            # MIN/MAX_MULTI_WORLD_TURNS since it isn't a representative turn.
            yield sse({"type": "speaker_start", "speaker": "facilitator"})
            new_message = None
            try:
                for event in stream_frame_breaker_response(state):
                    if event["type"] == "token":
                        yield sse({
                            "type": "token",
                            "speaker": event["speaker"],
                            "text": event["text"],
                        })
                    elif event["type"] == "complete":
                        new_message = event["message"]
            except Exception as exc:
                yield sse({"type": "error", "message": str(exc)})
                return

            state.messages = list(state.messages) + [new_message]
            sessions[session_id] = state

            yield sse({
                "type": "speaker_end",
                "speaker": "facilitator",
                "citations": None,
            })
            yield sse({"type": "done", "phase": state.phase, "turn_count": state.turn_count})
            return

        if is_relational_safety_firing:
            # Facilitator-only turn, per the corrected design's strict
            # decoupling (no dual-voice response) - the Representative is
            # not invoked and does not see this message, exactly as the
            # frame-breaker branch above withholds Representative
            # invocation. Does not count toward MIN/MAX_MULTI_WORLD_TURNS.
            # state.track_a_active/track_b_active/relational_safety_tags
            # were already updated on `state` before event_stream() was
            # defined, so they're already reflected in `sessions[session_id]`
            # even before this branch's own message is appended below.
            yield sse({"type": "speaker_start", "speaker": "facilitator"})
            new_message = None
            try:
                for event in stream_relational_safety_response(state, rs_classification, rs_updates):
                    if event["type"] == "token":
                        yield sse({
                            "type": "token",
                            "speaker": event["speaker"],
                            "text": event["text"],
                        })
                    elif event["type"] == "complete":
                        new_message = event["message"]
            except Exception as exc:
                yield sse({"type": "error", "message": str(exc)})
                return

            state.messages = list(state.messages) + [new_message]
            sessions[session_id] = state

            yield sse({
                "type": "speaker_end",
                "speaker": "facilitator",
                "citations": None,
            })
            yield sse({"type": "done", "phase": state.phase, "turn_count": state.turn_count})
            return

        working_messages = list(state.messages)
        last_current_world_id = state.current_world_id
        turns_completed = 0
        spoken_this_round: list[str] = []

        try:
            while True:
                if is_multi_world:
                    # Ask, before each turn, who is most directly positioned to
                    # speak next given what has actually been said so far -
                    # instead of working through a fixed list of every world at
                    # the table in the same order every round.
                    snapshot = ConversationState(
                        messages=working_messages,
                        world_id=state.world_id,
                        world_ids=state.world_ids,
                        worlds_at_table=state.worlds_at_table,
                    )
                    must_continue = turns_completed < MIN_MULTI_WORLD_TURNS
                    world_id = select_next_speaker(snapshot, spoken_this_round, must_continue=must_continue)
                    if world_id is None:
                        break
                else:
                    if spoken_this_round:
                        break
                    world_id = state.world_id

                # Pop (consume) any dominance/convergence guidance waiting for
                # this specific representative from an earlier round - once
                # delivered, it shouldn't repeat on every future turn.
                guidance_for_speaker = state.pending_guidance.pop(world_id, None)

                working_state = ConversationState(
                    messages=working_messages,
                    phase=state.phase,
                    current_speaker=state.current_speaker,
                    current_world_id=world_id,
                    turn_count=state.turn_count,
                    drift_signals=list(state.drift_signals),
                    requires_reroot=state.requires_reroot,
                    pending_guidance={world_id: guidance_for_speaker} if guidance_for_speaker else {},
                    retrieved_context=state.retrieved_context,
                    worlds_at_table=state.worlds_at_table,
                    world_capsule_core=state.world_capsule_core,
                    permanent_prompt=state.permanent_prompt,
                    session_id=state.session_id,
                    world_id=state.world_id,
                    world_ids=state.world_ids,
                    close_requested=state.close_requested,
                )

                speaker_name = get_representative_message_name(world_id)
                yield sse({"type": "speaker_start", "speaker": speaker_name})

                new_message = None
                is_reactive = bool(spoken_this_round)
                for event in stream_representative_turn(working_state, is_reactive=is_reactive):
                    if event["type"] == "token":
                        yield sse({
                            "type": "token",
                            "speaker": event["speaker"],
                            "text": event["text"],
                        })
                    elif event["type"] == "complete":
                        new_message = event["message"]
                        last_current_world_id = event["current_world_id"]

                working_messages = working_messages + [new_message]
                turns_completed += 1
                spoken_this_round.append(world_id)

                yield sse({
                    "type": "speaker_end",
                    "speaker": new_message.name,
                    "citations": new_message.additional_kwargs.get("citations"),
                })

                # Cost/latency backstop only - not a target. Most rounds
                # should end earlier via must_continue going False and the
                # selector genuinely returning NONE.
                if turns_completed >= MAX_MULTI_WORLD_TURNS:
                    break

            # No mechanical "now it's your turn" prompt back to the participant
            # here - Facilitator Governance V3.6 Section 12 is explicit that
            # the room should almost never need to acquire a voice ("most
            # encounters should never require the room to acquire a voice";
            # "if the Facilitator is present in the middle of a rich encounter,
            # the governance is too loud"). The participant can always speak
            # next themselves - manufacturing a scripted question every round
            # is exactly the "presentation with a question" pattern, not
            # genuine conversation.
        except Exception as exc:
            yield sse({"type": "error", "message": str(exc)})
            return

        # Commit the completed round to session state and tell the
        # participant they can speak again right away. Everything below this
        # point - dominance/convergence, monitoring, reroot - is post-hoc by
        # design: none of it can change the turn the participant just read,
        # it only ever queues guidance for a LATER turn (pending_guidance).
        # There is therefore no reason to make the participant wait for it;
        # it used to run before "done" was sent, costing several seconds of
        # invisible latency for zero visible benefit. It keeps running after
        # this yield - the SSE connection just stays open a little longer
        # while it finishes in the background.
        state.messages = working_messages
        state.turn_count = state.turn_count + turns_completed
        state.current_world_id = last_current_world_id
        state.requires_reroot = False
        sessions[session_id] = state

        yield sse({"type": "done", "phase": state.phase, "turn_count": state.turn_count})

        # Everything below is invisible background governance the participant
        # never waits on - guarded by its own try/except (rather than relying
        # on the round loop's try/except above, which no longer wraps this
        # code now that it runs after "done") so a monitoring failure can
        # never surface as a broken response mid-stream; at worst this
        # round's drift checks are silently skipped.
        try:
            # Per-representative drift checks - dominance looks at cumulative
            # airtime across the whole conversation, convergence looks at
            # just this round's speakers. Both are invisible to the
            # participant; medium/high findings become guidance queued for
            # that representative's next turn (see pending_guidance above).
            new_drift_signals: list = []
            new_pending_guidance: dict[str, str] = {}
            if is_multi_world and turns_completed >= 1:
                check_state = ConversationState(
                    messages=working_messages,
                    world_id=state.world_id,
                    world_ids=state.world_ids,
                )
                for signal in check_dominance(check_state) + check_convergence(check_state, spoken_this_round):
                    new_drift_signals.append(signal)
                    if signal.world_id and signal.severity in ("medium", "high"):
                        new_pending_guidance[signal.world_id] = signal.description

            # Monitor every turn completed this round, not just the last
            # speaker's - facilitator_monitors only ever sees
            # state.current_world_id's most recent message, which silently
            # skipped drift checking on every turn but the final one in a
            # multi-turn round. Each turn is checked and, if flagged,
            # corrected against its OWN speaker's world_id via
            # pending_guidance - not the global requires_reroot flag every
            # representative used to read from regardless of who the
            # finding was actually about.
            round_turns = working_messages[-turns_completed:] if turns_completed else []
            for msg in round_turns:
                msg_world_id = next(
                    (wid for wid in world_ids if get_representative_message_name(wid) == msg.name),
                    None,
                )
                if msg_world_id is None:
                    continue
                signal = check_drift_for_message(msg_world_id, msg.content)
                if signal is None:
                    continue
                new_drift_signals.append(signal)
                if signal.severity in ("medium", "high"):
                    # A representative who drifted more than once this round
                    # gets the latest correction, not a stacked list -
                    # pending_guidance holds one string per world_id.
                    new_pending_guidance[msg_world_id] = generate_reroot_guidance(signal)

            # Re-read and merge rather than overwrite wholesale - since "done"
            # already went out above, the participant's next message may have
            # already been appended to this session by the time this
            # background work finishes, and a blind overwrite here would
            # clobber it.
            latest_state = sessions.get(session_id)
            if latest_state is not None:
                latest_state.drift_signals = list(latest_state.drift_signals) + new_drift_signals
                latest_state.pending_guidance = {**latest_state.pending_guidance, **new_pending_guidance}
                sessions[session_id] = latest_state
        except Exception:
            # Invisible governance failing silently is the correct behavior
            # here - the participant already has their response, and this
            # round's drift signals simply don't get recorded.
            pass

    return StreamingResponse(
        event_stream(),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )


@app.get("/api/session/{session_id}", response_model=SessionResponse)
async def get_session(session_id: str):
    """
    Get the current state of a conversation session.

    Useful for reconnection or state inspection.
    """
    if session_id not in sessions:
        raise HTTPException(status_code=404, detail="Session not found")

    state = sessions[session_id]

    return SessionResponse(
        session_id=session_id,
        messages=state_to_messages(state),
        phase=state.phase,
        turn_count=state.turn_count,
    )


@app.get("/api/session/{session_id}/audit")
async def get_session_audit(session_id: str):
    """
    Get the full retrieval audit trail for a session, for review purposes.

    Unlike the normal message endpoints (which only surface citations meant
    for participants), this includes every lexicon file the retriever
    considered for each representative turn - retrieved or skipped, and why -
    so a reviewer can see exactly what source material each answer drew on.
    """
    if session_id not in sessions:
        raise HTTPException(status_code=404, detail="Session not found")

    state = sessions[session_id]

    turns = []
    for msg in state.messages:
        role = "assistant"
        name = None
        if isinstance(msg, HumanMessage):
            role = "user"
        elif hasattr(msg, "name"):
            name = msg.name

        content = msg.content
        if isinstance(content, list):
            text_parts = []
            for block in content:
                if isinstance(block, dict) and block.get("type") == "text":
                    text_parts.append(block.get("text", ""))
                elif isinstance(block, str):
                    text_parts.append(block)
            content = "\n".join(text_parts)

        entry = {"role": role, "name": name, "content": content}

        if hasattr(msg, "additional_kwargs"):
            if msg.additional_kwargs.get("citations"):
                entry["citations"] = msg.additional_kwargs["citations"]
            if msg.additional_kwargs.get("retrieval_audit"):
                entry["retrieval_audit"] = msg.additional_kwargs["retrieval_audit"]

        turns.append(entry)

    return {
        "session_id": session_id,
        "world_id": state.world_id,
        "world_ids": state.world_ids,
        "phase": state.phase,
        "turn_count": state.turn_count,
        "drift_signals": [
            {
                "signal_type": s.signal_type,
                "description": s.description,
                "severity": s.severity,
                "world_id": s.world_id,
            }
            for s in state.drift_signals
        ],
        "turns": turns,
    }


class Representative(BaseModel):
    """A representative from a world."""

    id: str
    name: str
    title: str
    description: str


class World(BaseModel):
    """A world/tradition available for conversation."""

    id: str
    name: str
    period: str
    region: str
    description: str
    representative: Representative
    color: str  # For UI theming


class WorldsResponse(BaseModel):
    """Response containing available worlds."""

    worlds: list[World]


# Available worlds - built from the single-source-of-truth manifest
# (app/world_manifest.py) rather than hardcoded here.
AVAILABLE_WORLDS = [
    World(
        id=entry.world_id,
        name=entry.world_name,
        period=entry.period,
        region=entry.region,
        description=entry.world_description,
        representative=Representative(
            id=entry.representative_id,
            name=entry.representative_name,
            title=entry.representative_title,
            description=entry.representative_description,
        ),
        color=entry.color,
    )
    for entry in WORLD_MANIFEST
]


class LexiconTerm(BaseModel):
    """A lexicon term with its definitions."""

    term: str
    aliases: list[str]
    quick_meaning: str
    full_content: str
    related_terms: list[str]


class LexiconResponse(BaseModel):
    """Response containing all lexicon terms."""

    terms: list[LexiconTerm]


def _extract_quick_meaning(full_content: str, fallback_content: str) -> str:
    """Extract a short tooltip-ready summary for a lexicon term.

    Handles both the "## Quick Meaning" heading convention (Syriac/PAHC,
    content follows on later lines) and the inline "**Quick Meaning:**"
    bold-label convention (Desert Monasticism, content follows on the same
    line). Falls back to a truncated snippet of the entry's own content
    (its first real section) for files that have neither - a tooltip should
    never show nothing just because a source file omitted this section.
    """
    for marker in ("## Quick Meaning", "**Quick Meaning:**", "**Quick Meaning**"):
        if marker not in full_content:
            continue

        remaining = full_content.split(marker, 1)[1]
        end_markers = ["\n---", "\n## ", "\n\n**"]
        end_pos = len(remaining)
        for end_marker in end_markers:
            pos = remaining.find(end_marker)
            if pos > 0 and pos < end_pos:
                end_pos = pos

        quick_meaning = remaining[:end_pos].strip().lstrip(":").strip()
        if quick_meaning:
            return quick_meaning

    # No Quick Meaning section at all - fall back to a truncated snippet of
    # the first real content section, so the tooltip isn't simply empty.
    snippet = re.split(r"\n---|\n## |\n\*\*", fallback_content.strip(), maxsplit=1)[0]
    snippet = snippet.strip()
    if len(snippet) > 240:
        truncated = snippet[:240].rsplit(" ", 1)[0]
        snippet = truncated + "…"
    return snippet


@app.get("/api/lexicon", response_model=LexiconResponse)
async def get_lexicon(world_id: str = "syriac-edessa-nisibis"):
    """
    Get all lexicon terms for a specific world.

    Returns terms with their quick meanings (for tooltips)
    and full content (for detail views).
    """
    from app.rag.indexer import LexiconIndexer

    # Validate world_id
    valid_world_ids = [w.id for w in AVAILABLE_WORLDS]
    if world_id not in valid_world_ids:
        raise HTTPException(status_code=400, detail=f"Invalid world_id. Must be one of: {valid_world_ids}")

    world_config = settings.get_world_config(world_id)
    indexer = LexiconIndexer()
    lexicon_path = world_config.lexicon_chunks_path

    terms = []
    for file_path in sorted(lexicon_path.glob("*.md")):
        # Read full file content to extract Quick Meaning
        full_content = file_path.read_text(encoding="utf-8")
        entry = indexer.parse_lexicon_file(file_path)

        quick_meaning = _extract_quick_meaning(full_content, entry.content)

        terms.append(LexiconTerm(
            term=entry.term,
            aliases=entry.aliases,
            quick_meaning=quick_meaning,
            full_content=entry.content,
            related_terms=entry.related_terms,
        ))

    return LexiconResponse(terms=terms)


@app.get("/api/worlds", response_model=WorldsResponse)
async def get_worlds():
    """
    Get all available worlds for conversation.

    Returns worlds with their representatives and metadata.
    """
    return WorldsResponse(worlds=AVAILABLE_WORLDS)


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "version": "0.1.0"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host=settings.host, port=settings.port)
