"""FastAPI application for the CiC POC backend."""

import asyncio
import json
import re
import uuid
from contextlib import asynccontextmanager
from pathlib import Path
from typing import Optional

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from pydantic import BaseModel

from app.auth import AuthedUser, get_current_user
from app.config import settings
from app.graph.builder import get_compiled_graph
from app.graph.nodes import representative_engages
from app.graph.state import ConversationState
from app.session_cap import check_and_reserve_session_slot
from app.transcript_logging import write_transcript
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
    # No eager RAG preload here on purpose. This used to loop through every
    # world in AVAILABLE_WORLDS at startup, backgrounded in a thread so
    # uvicorn could still report "startup complete" and open the port
    # immediately (a real, previously-fixed bug: awaiting it directly on
    # the event loop blocked the port from opening in time on a
    # resource-constrained host). But get_retriever/get_story_retriever
    # (app/graph/nodes.py) already do correct per-world lazy loading of
    # their own - a module-level dict cache that only builds/loads a given
    # world's FAISS index the first time that world is actually asked for,
    # never twice. Looping through all 6 at startup warmed worlds nobody
    # may ever seat at this session, for no reason but "just in case" -
    # every real session only ever touches the 1-3 worlds it actually
    # seats. Removed; the lazy path is the only loading path now, and
    # FAISS indices are pre-built and baked into the Docker image (see
    # build_indices.py), so a world's first real touch is a cheap
    # FAISS.load_local() deserialize, not a from-scratch embedding build.
    yield

    # Cleanup
    sessions.clear()


app = FastAPI(
    title="Church in Conversation POC",
    description="The Table - Engaging conversations with representative voices from Christian history",
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


class PilotRequest(BaseModel):
    """A pilot "express interest" submission from cic-website/pilot.html."""

    name: str
    email: str
    seat: str | None = None
    why_interested: str | None = None
    referred_by: str | None = None


class GenerateReferralRequest(BaseModel):
    """Identifies the referring tester by self-reported email, not a bearer
    token - see submit_referral_redemption's docstring for why."""

    referrer_email: str


class RedeemReferralRequest(BaseModel):
    """A friend redeeming a code from cic-website/refer-a-friend.html."""

    code: str
    name: str
    email: str


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
async def start_session(request: StartSessionRequest, user: AuthedUser = Depends(get_current_user)):
    """
    Start a new conversation session.

    This initializes the conversation with the facilitator's welcome
    and introduction of the representative(s) for the selected world(s).

    Supports both single-world (world_id) and multi-world (world_ids) modes.
    Multi-world tables allow 1-3 representatives to engage together.

    `user` comes from the signed-in participant's Supabase session (see
    app/auth.py) - a dev placeholder with no real identity when Supabase
    isn't configured, so local dev/mock-mode work unchanged.
    """
    from app.graph.state import WorldContext

    allowed, reason = check_and_reserve_session_slot(user)
    if not allowed:
        raise HTTPException(status_code=403, detail=reason)

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
        user_id=user.user_id,
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
            user_id=user.user_id,
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


@app.post("/api/pilot/request")
async def submit_pilot_request(request: PilotRequest):
    """
    Record a pilot "express interest" submission (cic-website/pilot.html's
    form). Mark reviews these directly in Supabase's table editor and, on
    approval, invites the person via Supabase Auth and assigns their
    profiles.pilot_cohort - no separate admin UI needed for this pass.

    A no-op (but still returns success, so the form doesn't show an error)
    if Supabase isn't configured - matches every other Supabase-dependent
    module's "off until configured" discipline.
    """
    from app.auth import _get_client, supabase_configured

    if not supabase_configured():
        return {"status": "received"}

    try:
        _get_client().table("pilot_requests").insert(
            {
                "name": request.name,
                "email": request.email,
                "seat": request.seat,
                "why_interested": request.why_interested,
                "referred_by": request.referred_by,
            }
        ).execute()
    except Exception:
        raise HTTPException(status_code=500, detail="Something went wrong submitting your interest. Please try again or email hello@churchinconversation.org directly.")

    return {"status": "received"}


def _generate_referral_code() -> str:
    import secrets
    import string

    alphabet = string.ascii_uppercase + string.digits
    return "CIC-" + "".join(secrets.choice(alphabet) for _ in range(6))


@app.post("/api/referral/generate")
async def generate_referral(request: GenerateReferralRequest):
    """
    Called from cic-website/refer-a-friend.html after a tester who just
    completed their post-conversation survey says yes to inviting a friend.

    Identifies the referring tester by self-reported email rather than a
    bearer token. The alternative - requiring an active Supabase session -
    doesn't reliably survive the trip through an external Google Form and
    back to a different origin (cic-website is a separate static site from
    wherever the app itself ends up hosted; browser-persisted auth doesn't
    cross that origin boundary without extra plumbing this pilot's scale
    doesn't warrant). At ~20-30 known, invited participants, a self-reported
    email checked against Supabase's own user list is a reasonable trust
    level - not the right call at public scale, fine here.

    One-hop enforcement: refuses if the referring user's own profile shows
    they arrived via a referral themselves (profiles.referred_by_invite_id
    is set) - a referred friend cannot refer further.
    """
    from app.auth import _get_client, supabase_configured

    if not supabase_configured():
        raise HTTPException(status_code=503, detail="Referrals aren't live yet - check back soon.")

    client = _get_client()

    users_response = client.auth.admin.list_users()
    matching_user = next(
        (u for u in users_response if u.email and u.email.lower() == request.referrer_email.lower()),
        None,
    )
    if matching_user is None:
        raise HTTPException(status_code=404, detail="We couldn't find an account for that email.")

    profile_rows = (
        client.table("profiles")
        .select("referred_by_invite_id")
        .eq("user_id", matching_user.id)
        .limit(1)
        .execute()
        .data
    )
    if profile_rows and profile_rows[0].get("referred_by_invite_id"):
        raise HTTPException(
            status_code=403,
            detail="Referrals go one friend deep - since you joined through a referral yourself, this isn't available for your account.",
        )

    code = _generate_referral_code()
    client.table("referral_invites").insert(
        {"code": code, "referring_user_id": matching_user.id}
    ).execute()

    return {"code": code}


@app.post("/api/referral/redeem")
async def redeem_referral(request: RedeemReferralRequest):
    """
    Called from cic-website/refer-a-friend.html when a referred friend enters
    the code they were given. Sends them a real Supabase invite (same
    mechanism Mark already uses manually for pilot_requests approvals) and
    marks the code spent so it can't be reused.
    """
    from app.auth import _get_client, supabase_configured

    if not supabase_configured():
        raise HTTPException(status_code=503, detail="Referrals aren't live yet - check back soon.")

    client = _get_client()

    invite_rows = (
        client.table("referral_invites")
        .select("id, status")
        .eq("code", request.code.strip().upper())
        .limit(1)
        .execute()
        .data
    )
    if not invite_rows:
        raise HTTPException(status_code=404, detail="That invite code wasn't found - check it and try again.")
    if invite_rows[0]["status"] != "active":
        raise HTTPException(status_code=410, detail="That invite has already been used.")

    invite_id = invite_rows[0]["id"]

    try:
        invited = client.auth.admin.invite_user_by_email(request.email)
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Something went wrong sending your invite. Please email hello@churchinconversation.org directly.",
        )

    client.table("referral_invites").update(
        {
            "status": "redeemed",
            "redeemed_by_user_id": invited.user.id,
            "redeemed_email": request.email,
            "redeemed_at": "now()",
        }
    ).eq("id", invite_id).execute()

    # New profile row already exists via the on_auth_user_created trigger;
    # stamp it with the referral link and this pilot's standard session cap.
    client.table("profiles").update(
        {"referred_by_invite_id": invite_id, "max_sessions": 2}
    ).eq("user_id", invited.user.id).execute()

    return {"status": "invited"}


@app.post("/api/session/{session_id}/message", response_model=SendMessageResponse)
async def send_message(session_id: str, request: SendMessageRequest):
    """
    Send a message in an existing conversation.

    The message is processed by the representative (with RAG augmentation)
    and then monitored for drift by the facilitator.
    """
    from app.graph.nodes import new_request_id
    request_id = new_request_id()

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
        write_transcript(session_id, state)

        return SendMessageResponse(
            messages=state_to_messages(state),
            phase=state.phase,
            turn_count=state.turn_count,
        )

    # Soft, identity-free conversation-length cap (see app/message_cap.py) -
    # checked before anything else in the main flow, since this pilot runs
    # with no sign-in and session_cap.py's own per-identity protection is a
    # permanent no-op without one. A capped session still gets a graceful
    # message, not a hard error.
    from app.message_cap import check_message_cap
    cap_allowed, cap_reason = check_message_cap(state.turn_count)
    if not cap_allowed:
        state.messages = list(state.messages) + [
            AIMessage(content=cap_reason, name="facilitator")
        ]
        sessions[session_id] = state
        write_transcript(session_id, state)
        return SendMessageResponse(
            messages=state_to_messages(state),
            phase=state.phase,
            turn_count=state.turn_count,
        )

    # Add the participant's message
    state.messages = list(state.messages) + [HumanMessage(content=request.message)]

    # Frame-breaker and relational-safety checks (see send_message_stream for
    # the full rationale - this endpoint mirrors it, minus the epistemology-
    # bridge intercept, which this endpoint has never had). The two
    # classifiers below take only the raw message (and, for relational-
    # safety, session state) as input - neither depends on the other's
    # output - so they're fired concurrently via asyncio.gather rather than
    # sequentially. classify_relational_safety always runs even though its
    # result is only USED when frame-breaker didn't fire, trading one
    # possibly-wasted API call for lower latency on every turn - the same
    # tradeoff applied in send_message_stream. This preserves the exact
    # behavior the old sequential code had: a firing frame-breaker still
    # short-circuits before any relational-safety state mutation happens.
    from app.graph.nodes import (
        classify_frame_breaker,
        classify_relational_safety,
        get_llm,
        relational_safety_should_fire,
        stream_relational_safety_response,
        update_relational_safety_state,
    )
    from app.prompts import FACILITATOR_FRAME_BREAKER_RESPONSE_PROMPT

    frame_breaker_task = asyncio.to_thread(classify_frame_breaker, request.message)
    relational_safety_task = asyncio.to_thread(classify_relational_safety, state, request.message)
    is_frame_breaker, rs_classification = await asyncio.gather(
        frame_breaker_task, relational_safety_task
    )

    if is_frame_breaker:
        llm = get_llm()
        response = llm.invoke([
            SystemMessage(content=FACILITATOR_FRAME_BREAKER_RESPONSE_PROMPT.format(message=request.message)),
            HumanMessage(content="Respond as the Facilitator, per your instructions above."),
        ])
        state.messages = list(state.messages) + [AIMessage(content=response.content, name="facilitator")]
        sessions[session_id] = state
        write_transcript(session_id, state)
        return SendMessageResponse(
            messages=state_to_messages(state),
            phase=state.phase,
            turn_count=state.turn_count,
        )

    # Not a frame-breaker - use the relational-safety classification that
    # was already computed concurrently above, exactly as the sequential
    # code would have computed it here (frame-breaker had already returned,
    # so this is the first and only place it's used).
    pre_track_a_active = state.track_a_active
    pre_track_a_severity = state.track_a_severity
    pre_track_b_active = state.track_b_active

    rs_updates = update_relational_safety_state(state, rs_classification)
    for field_name, value in rs_updates.items():
        setattr(state, field_name, value)

    if relational_safety_should_fire(state, rs_classification, rs_updates):
        new_message = None
        for event in stream_relational_safety_response(
            state, rs_classification, rs_updates,
            pre_track_a_active=pre_track_a_active,
            pre_track_a_severity=pre_track_a_severity,
            pre_track_b_active=pre_track_b_active,
        ):
            if event["type"] == "complete":
                new_message = event["message"]
        state.messages = list(state.messages) + [new_message]
        sessions[session_id] = state
        write_transcript(session_id, state)
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
            result = multi_representative_engages(state, request_id=request_id)
        else:
            # Single representative responds
            state.current_world_id = responding_worlds[0]
            result = representative_engages(state, request_id=request_id)
    else:
        # Single-world table
        result = representative_engages(state, request_id=request_id)

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
    - done           {phase, turn_count}              — all speakers have finished; the participant may respond now. Invisible governance (dominance/convergence/drift monitoring, wind-down sensing) continues briefly in the background after this and is never streamed - see the end of event_stream() for why.
    - error          {message}                        — something went wrong; stream ends

    Closing the conversation (`close_requested`) is not streamed - use the
    plain /message endpoint for that, since it's a single short message.
    """
    from app.graph.nodes import new_request_id
    request_id = new_request_id()

    if session_id not in sessions:
        raise HTTPException(status_code=404, detail="Session not found")

    if request.close_requested:
        raise HTTPException(
            status_code=400,
            detail="close_requested is not supported on the streaming endpoint - use /message",
        )

    state = sessions[session_id]

    # Soft, identity-free conversation-length cap (see app/message_cap.py) -
    # checked before anything else, same rationale and placement as the
    # non-streaming /message endpoint above. Short-circuits with a single
    # facilitator message and skips the classify-then-route chain below
    # entirely rather than threading a cap check through it.
    from app.message_cap import check_message_cap
    cap_allowed, cap_reason = check_message_cap(state.turn_count)
    if not cap_allowed:
        def sse(event: dict) -> str:
            return f"data: {json.dumps(event)}\n\n"

        def capped_stream():
            yield sse({"type": "speaker_start", "speaker": "facilitator"})
            yield sse({"type": "token", "speaker": "facilitator", "text": cap_reason})
            state.messages = list(state.messages) + [
                AIMessage(content=cap_reason, name="facilitator")
            ]
            sessions[session_id] = state
            write_transcript(session_id, state)
            yield sse({"type": "speaker_end", "speaker": "facilitator", "citations": None})
            yield sse({"type": "done", "phase": state.phase, "turn_count": state.turn_count})

        return StreamingResponse(capped_stream(), media_type="text/event-stream")

    state.messages = list(state.messages) + [HumanMessage(content=request.message)]

    from app.graph.nodes import (
        check_convergence,
        check_cross_world_vocabulary_drift,
        check_dominance,
        check_drift_for_message,
        check_length_ceiling,
        check_question_stacking,
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

    # Epistemology-bridge, frame-breaker, and relational-safety are three
    # classify-then-route intercepts whose priority order matters (a firing
    # epistemology-bridge or frame-breaker preempts relational-safety, and
    # epistemology-bridge preempts frame-breaker - see each classifier's own
    # docstring for why), but whose INPUTS don't depend on each other: each
    # takes only the raw message (relational-safety also takes session
    # state, read-only until its own result is applied below), never
    # another classifier's output. The old code ran them sequentially and
    # short-circuited later ones once an earlier one fired, purely as a
    # cost optimization (skip an API call once routing is already decided),
    # not because of a genuine data dependency - the code comments' "double-
    # classification race" concern was about which classifier's result gets
    # ACTED on first, not about needing one's output to compute another.
    # Firing all three concurrently (asyncio.gather, each wrapped in
    # asyncio.to_thread since these are synchronous .invoke() calls - the
    # standard way to run a blocking call off the event loop without
    # making it non-blocking itself) trades the skipped-call saving for
    # materially lower latency before the Representative's response ever
    # starts streaming - the explicit, current priority. classify_relational_safety
    # always runs now, even on a turn where epistemology-bridge or
    # frame-breaker will end up firing and its result won't be used - one
    # possibly-wasted API call per turn, spent on lower latency.
    from app.graph.epistemology_bridge import classify_epistemology_bridge

    epistemology_bridge_task = asyncio.to_thread(classify_epistemology_bridge, request.message)
    frame_breaker_task = asyncio.to_thread(classify_frame_breaker, request.message)
    relational_safety_task = asyncio.to_thread(classify_relational_safety, state, request.message)

    is_epistemology_bridge, frame_breaker_result, relational_safety_result = await asyncio.gather(
        epistemology_bridge_task, frame_breaker_task, relational_safety_task
    )

    # Apply the EXACT SAME priority the sequential code used - epistemology-
    # bridge wins if it fired; else frame-breaker; else relational-safety -
    # just resolved after all three classifications are back instead of
    # skipping the later calls entirely once an earlier one fires.
    is_frame_breaker = False if is_epistemology_bridge else frame_breaker_result

    rs_classification = {"category": "NO_SIGNAL"}
    rs_updates: dict = {}
    is_relational_safety_firing = False
    pre_track_a_active = state.track_a_active
    pre_track_a_severity = state.track_a_severity
    pre_track_b_active = state.track_b_active
    if not is_frame_breaker and not is_epistemology_bridge:
        rs_classification = relational_safety_result
        rs_updates = update_relational_safety_state(state, rs_classification)
        for field_name, value in rs_updates.items():
            setattr(state, field_name, value)
        is_relational_safety_firing = relational_safety_should_fire(state, rs_classification, rs_updates)

    higher_intercept = is_frame_breaker or is_relational_safety_firing or is_epistemology_bridge

    # Sensed closing sequence (CiC_Sensed_Closing_Sequence_Spec_V0_1.md). Runs
    # after the two existing intercepts (which always preempt it - a crisis during
    # a wind-down is a crisis, not a closing) and gates the bridge/round below.
    #   (a) a sequence already in progress -> route the participant's reply; a
    #       genuine new question resets to none and falls through (escape hatch).
    #   (b) idle -> sense wind-down (further below).
    # closing_turns, once set, is the list of Facilitator-only turns to stream.
    closing_turns = None
    if not higher_intercept and state.closing_stage != "none":
        from app.graph.closing_sequence import route_closing_stage
        decision = route_closing_stage(state, request.message)
        if decision["action"] == "resume":
            state.closing_stage = "none"  # a new question: the sequence evaporates
        else:
            state.closing_stage = decision["to"]
            closing_turns = decision["turns"]

    # Anachronism-bridge check: a modern theological term the seated world never
    # held. Third classify-then-route intercept - whitelist-gated by the per-world
    # glossary overlay, failing toward None (see classify_modern_term). Runs only
    # when nothing above is already handling this turn.
    #
    # Deliberately left synchronous/sequential here, unlike the 3-way gather
    # above - unlike frame-breaker/epistemology-bridge/relational-safety,
    # this one has a real ordering dependency on the Representative's own
    # response: when it fires, the Facilitator's "named as later" note is
    # PREPENDED before the Representative's answer, and the Representative
    # is given a different, reframed, term-free input message (never the
    # participant's original one - see stream_modern_term_bridge). Starting
    # the Representative's generation concurrently with this classification
    # would mean starting it against the WRONG input on every turn, only
    # discovering after the fact (once this classifier returns) whether that
    # generation has to be thrown away and restarted against the reframed
    # message instead - a real correctness/race-condition risk on a
    # customer-facing streaming path that isn't safely buildable and
    # API-verified in the time available here. It already got the cheaper,
    # lower-risk half of the same fix as the other classifiers: it's on
    # claude-haiku-4-5 with a tight max_tokens cap (CLASSIFIER_MAX_TOKENS),
    # not the full settings.llm_model - see classify_modern_term's own
    # get_monitoring_llm call.
    modern_term_match = None
    if not higher_intercept and closing_turns is None and state.closing_stage == "none":
        from app.graph.modern_term_bridge import classify_modern_term
        seated_world_ids = state.world_ids if len(state.world_ids) > 0 else [state.world_id]
        modern_term_match = classify_modern_term(request.message, seated_world_ids)
    is_modern_term_bridge = modern_term_match is not None

    # Wind-down sensing used to run here, synchronously, before the
    # Representative's turn - unlike modern-term above, it has no ordering
    # dependency on the Representative's response at all: it never changes
    # what the Representative says, it only ever sets state.closing_stage
    # for the NEXT turn's routing (see route_closing_stage). That makes it
    # safe to defer past "done" entirely, the same "invisible governance"
    # pattern already used below for dominance/convergence/drift - this
    # turn's Representative response no longer waits on it at all. See the
    # end of event_stream() for where it actually runs now.
    should_check_wind_down = (
        not higher_intercept and closing_turns is None and not is_modern_term_bridge
        and not is_epistemology_bridge and state.closing_stage == "none"
    )

    world_ids = state.world_ids if len(state.world_ids) > 0 else [state.world_id]
    is_multi_world = len(world_ids) > 1

    # A multi-representative round should never be "everyone states their
    # position once, done" - real conversation is opening, response,
    # response-to-the-response, sometimes a third voice joining partway
    # through. MIN enforces at least one direct answer to the question (the
    # opening turn) plus two further rounds of exchange before the selector
    # is even allowed to end the round. MAX is just a cost/latency backstop,
    # not a target - most rounds should end well before it from genuine
    # exhaustion of what's worth saying, not from hitting a ceiling.
    #
    # Originally capped at 4 (not 6) after live testing showed a 6-turn
    # round chaining 15+ sequential API calls produced truncated or empty
    # late turns - since root-caused to an interleaved extended-thinking
    # block silently consuming a capped call's token budget, not cumulative
    # latency itself (see get_llm's own docstring, and CiC_L3D_Table_Process_
    # ThreeRepresentative_V1.0.md Section 6). That fix (thinking explicitly
    # disabled on every token-capped call) was already in place project-
    # wide; only the turn cap itself had never been re-tested against it.
    # Re-tested 2026-07-13 with a three-world table: one round ended
    # naturally at 4 turns, a second was pushed to the full 6-turn ceiling
    # and completed cleanly - all six turns substantial (1,800-2,400 chars
    # each), no truncation, no empty responses, no error events. Restored
    # to 6. Full round latency at 6 turns ran ~150s end to end in this
    # test, up from the 4-turn cap's ~60-90s - a real cost worth knowing,
    # not a reliability problem.
    # Lowered from 3 per the Fable conversational-engagement analysis: a
    # round with multiple worlds seated can legitimately be complete at 2
    # turns - one real answer and one short real response. Forcing a third
    # manufactures speech the moment didn't call for, and the historical
    # forms this table hosts include the one-sentence desert word - the
    # floor must be low enough for that form to exist. 2 still guarantees
    # the multi-world contract (more than one voice heard) without
    # scripting the round's shape.
    MIN_MULTI_WORLD_TURNS = 2
    MAX_MULTI_WORLD_TURNS = 6

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
            write_transcript(session_id, state)

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
                for event in stream_relational_safety_response(
                    state, rs_classification, rs_updates,
                    pre_track_a_active=pre_track_a_active,
                    pre_track_a_severity=pre_track_a_severity,
                    pre_track_b_active=pre_track_b_active,
                ):
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
            write_transcript(session_id, state)

            yield sse({
                "type": "speaker_end",
                "speaker": "facilitator",
                "citations": None,
            })
            yield sse({"type": "done", "phase": state.phase, "turn_count": state.turn_count})
            return

        if closing_turns is not None:
            # Sensed closing sequence: one or more Facilitator-only turns
            # (anything-else / resources-offer / resources-show / sensed-close),
            # per the routed plan. The Representative is never invoked. Multiple
            # turns (e.g. show-resources then the close) stream back to back in a
            # single response so the participant needn't send another message.
            from app.graph.closing_sequence import stream_closing_turn
            new_messages = []
            try:
                for kind, _ctx in closing_turns:
                    yield sse({"type": "speaker_start", "speaker": "facilitator"})
                    new_msg = None
                    for event in stream_closing_turn(state, kind):
                        if event["type"] == "token":
                            yield sse({
                                "type": "token",
                                "speaker": event["speaker"],
                                "text": event["text"],
                            })
                        elif event["type"] == "complete":
                            new_msg = event["message"]
                    yield sse({
                        "type": "speaker_end",
                        "speaker": "facilitator",
                        "citations": None,
                    })
                    if new_msg is not None:
                        new_messages.append(new_msg)
            except Exception as exc:
                yield sse({"type": "error", "message": str(exc)})
                return

            state.messages = list(state.messages) + new_messages
            sessions[session_id] = state
            write_transcript(session_id, state)

            yield sse({"type": "done", "phase": state.phase, "turn_count": state.turn_count})
            return

        if is_modern_term_bridge:
            # Facilitator beats 1-2 (name-as-later + neutral modern sense), then
            # - for an `anachronistic` cell - the Representative answers a WORLD-
            # NATIVE reframe, never the modern term (spec sections 3.2/3.4).
            # Unlike the two intercepts above, this is Facilitator-THEN-
            # Representative and so can append two messages. The reframe handed to
            # the Representative is never persisted (spec section 5): only the
            # `complete` messages yielded here are appended to the transcript, so
            # it reads [participant's original message, Facilitator, Rep].
            from app.graph.modern_term_bridge import stream_modern_term_bridge
            new_messages = []
            try:
                for event in stream_modern_term_bridge(state, modern_term_match):
                    if event["type"] == "speaker_start":
                        yield sse({"type": "speaker_start", "speaker": event["speaker"]})
                    elif event["type"] == "token":
                        yield sse({
                            "type": "token",
                            "speaker": event["speaker"],
                            "text": event["text"],
                        })
                    elif event["type"] == "speaker_end":
                        yield sse({
                            "type": "speaker_end",
                            "speaker": event["speaker"],
                            "citations": event.get("citations"),
                        })
                    elif event["type"] == "complete":
                        new_messages.append(event["message"])
            except Exception as exc:
                yield sse({"type": "error", "message": str(exc)})
                return

            state.messages = list(state.messages) + new_messages
            sessions[session_id] = state
            write_transcript(session_id, state)

            yield sse({"type": "done", "phase": state.phase, "turn_count": state.turn_count})
            return

        if is_epistemology_bridge:
            # Facilitator beat 1 (the honest, general, system-level
            # acknowledgment), then beat 2 (the Representative, answering
            # the same question reframed toward their own world's specific
            # epistemology). Same two-message shape as the modern-term
            # bridge above.
            from app.graph.epistemology_bridge import stream_epistemology_bridge
            new_messages = []
            try:
                for event in stream_epistemology_bridge(state):
                    if event["type"] == "speaker_start":
                        yield sse({"type": "speaker_start", "speaker": event["speaker"]})
                    elif event["type"] == "token":
                        yield sse({
                            "type": "token",
                            "speaker": event["speaker"],
                            "text": event["text"],
                        })
                    elif event["type"] == "speaker_end":
                        yield sse({
                            "type": "speaker_end",
                            "speaker": event["speaker"],
                            "citations": event.get("citations"),
                        })
                    elif event["type"] == "complete":
                        new_messages.append(event["message"])
            except Exception as exc:
                yield sse({"type": "error", "message": str(exc)})
                return

            state.messages = list(state.messages) + new_messages
            sessions[session_id] = state
            write_transcript(session_id, state)

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
                for event in stream_representative_turn(working_state, is_reactive=is_reactive, request_id=request_id):
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
        write_transcript(session_id, state)

        yield sse({"type": "done", "phase": state.phase, "turn_count": state.turn_count})

        # Everything below is invisible background governance the participant
        # never waits on - guarded by its own try/except (rather than relying
        # on the round loop's try/except above, which no longer wraps this
        # code now that it runs after "done") so a monitoring failure can
        # never surface as a broken response mid-stream; at worst this
        # round's drift checks are silently skipped. Drift-checking and
        # wind-down sensing get SEPARATE try/except blocks, not one shared
        # one - they're independent concerns (dominance/convergence/drift
        # is about correcting a LATER Representative turn; wind-down is
        # about offering a graceful close) with no reason for a failure in
        # one to silently take out the other too.
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
                for signal in (
                    check_dominance(check_state)
                    + check_convergence(check_state, spoken_this_round)
                    + check_cross_world_vocabulary_drift(check_state, spoken_this_round)
                    + check_length_ceiling(check_state, spoken_this_round)
                    + check_question_stacking(check_state, spoken_this_round)
                ):
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

        # Wind-down sensing (see should_check_wind_down above) - moved here,
        # after "done", instead of blocking the round that just streamed on
        # it. Never changes what the participant just read; it only sets
        # state.closing_stage for the NEXT participant message to route
        # against (see route_closing_stage) - a next-turn-only effect, same
        # as the guidance queued above, just a different field. Its own
        # try/except, separate from the drift-check block above (see the
        # comment introducing this section) - re-reads session state fresh
        # immediately before writing rather than reusing latest_state above,
        # since classify_wind_down's own network call is real elapsed time
        # during which yet another message could have arrived.
        try:
            if should_check_wind_down:
                from app.graph.closing_sequence import classify_wind_down
                if classify_wind_down(state, request.message):
                    wind_down_state = sessions.get(session_id)
                    if wind_down_state is not None:
                        wind_down_state.closing_stage = "anything_else_asked"
                        sessions[session_id] = wind_down_state
        except Exception:
            # Same fail-open discipline as classify_wind_down's own
            # docstring - a missed wind-down here costs nothing.
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
    # Smaller-print academic/scholarly label shown under the main name on
    # the selection tile - None for worlds whose name is already the plain,
    # easy-to-remember form.
    subtitle: Optional[str] = None
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
        subtitle=entry.world_subtitle,
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


# Serve the built frontend from the same origin as the API, if present.
#
# The frontend hardcodes `API_BASE = '/api'` as a same-origin relative path
# (no VITE_API_BASE env var exists) - the Vite dev server's proxy
# (vite.config.ts) makes that work locally, but a production static build
# has no such proxy. Rather than adding a separate reverse-proxy layer or
# a cross-origin API base (which would also need CORS_ORIGINS to include
# wherever the frontend ends up, and a second thing to deploy and keep in
# sync), the simplest correct fix is for this one service to serve both:
# `/api/*` and `/health` above are matched first (FastAPI resolves routes
# in registration order), everything else falls through to here. Guarded
# on the dist/ directory actually existing so local backend-only dev
# (no built frontend) is completely unaffected.
_FRONTEND_DIST = Path(__file__).resolve().parents[2] / "frontend" / "dist"
if _FRONTEND_DIST.is_dir():
    app.mount("/assets", StaticFiles(directory=_FRONTEND_DIST / "assets"), name="frontend-assets")

    @app.get("/{full_path:path}")
    async def serve_frontend(full_path: str):
        """SPA catch-all: any path not already matched above serves index.html
        (client-side routing, if the app ever adds any, resolves from there) or
        a same-named static file at the dist root (favicon.ico, icons, etc.)."""
        candidate = _FRONTEND_DIST / full_path
        if full_path and candidate.is_file():
            return FileResponse(candidate)
        return FileResponse(_FRONTEND_DIST / "index.html")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host=settings.host, port=settings.port)
