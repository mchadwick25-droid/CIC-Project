"""FastAPI application for the CiC POC backend."""

import asyncio
import json
import logging
import re
import uuid
from contextlib import asynccontextmanager
from pathlib import Path
from typing import Optional
from urllib.parse import urlparse

from fastapi import Depends, FastAPI, Header, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from pydantic import BaseModel

from app.auth import AuthedUser, get_audit_user, get_current_user, supabase_configured
from app.config import settings
from app.session_auth import mint_session_token, require_session_access
from app.graph.builder import get_compiled_graph
from app.graph.events import EVENT_STORE, serialize_message
from app.graph.nodes import representative_engages
from app.graph.state import ConversationState, RetrievedContext
from app.session_cap import check_and_reserve_session_slot
from app.transcript_logging import write_transcript
from app.world_manifest import WORLD_MANIFEST

# Same "no root logging.basicConfig anywhere" situation as usage_logging.py -
# a dedicated logger with its own handler, not reliant on root config.
logger = logging.getLogger("cic.main")
logger.setLevel(logging.INFO)
if not logger.handlers:
    _handler = logging.StreamHandler()
    _handler.setFormatter(logging.Formatter("%(asctime)s [%(name)s] %(message)s"))
    logger.addHandler(_handler)


# S4.2 (Pass 1 §6.7): the mutable in-memory sessions dict is gone. All
# conversation state lives in the append-only event log (app/graph/events
# .py); every read below is a projection, every write an appended event.


def _serialize_drift_signal(s) -> dict:
    return {"signal_type": s.signal_type, "description": s.description,
            "severity": s.severity, "world_id": s.world_id}


def _serialize_retrieved_context(rc: Optional[RetrievedContext]) -> Optional[dict]:
    if rc is None:
        return None
    return {"chunks": list(rc.chunks), "terms": list(rc.terms),
            "sources": list(rc.sources), "citations": list(rc.citations)}


def _multi_world_turn_floor() -> int:
    """S4.4a, per F9: the named FIRST runtime consumer of
    wrs/parameters.yaml. The per-round floor (MIN_MULTI_WORLD_TURNS) is
    read from the canonical parameters file instead of a hardcoded local
    constant - `turn_floor_multi_world.value`, whose entry documents its
    own provenance and whose retirement to a per-conversation contract is
    M3 (S4.4b, only after Mark decides). Fail-open to the historical
    value 2: a deployment must never fail to serve because a parameters
    file is missing or malformed (the session-contract deployability
    rule), and the fallback is byte-identical to the pre-F9 behavior.
    """
    try:
        import yaml
        params_path = Path(__file__).resolve().parents[1] / "wrs" / "parameters.yaml"
        params = yaml.safe_load(params_path.read_text(encoding="utf-8"))
        return int(params["parameters"]["turn_floor_multi_world"]["value"])
    except Exception:
        # This used to fail silently and identically whether the file was
        # missing (a real deployment gap - see the Dockerfile's wrs/
        # COPY lines) or just malformed. Both still fail open to the
        # historical value, per the deployability rule above, but now at
        # least the difference between "working as designed" and "the
        # canonical parameters file didn't make it into this image" is
        # visible in the logs instead of indistinguishable
        # (2026-08-05 full-system review, Engineering P1-2).
        logger.warning(
            "wrs/parameters.yaml unreadable or malformed at %s - "
            "falling back to the hardcoded turn_floor_multi_world=2",
            Path(__file__).resolve().parents[1] / "wrs" / "parameters.yaml",
            exc_info=True,
        )
        return 2


_TURN_FLOOR_MULTI_WORLD = _multi_world_turn_floor()


def _message_events(msgs) -> list[tuple[str, dict]]:
    """spoken_message events for a batch of new messages - EXCEPT
    bridge-reframe sentinels, which are already persisted as their own
    bridge_reframe event (S4.5, §6.6) and must not double-log."""
    return [("spoken_message", serialize_message(m)) for m in msgs
            if not (getattr(m, "additional_kwargs", None) or {}).get("bridge_reframe")]


def _classifier_events(pre_turn) -> list[tuple[str, dict]]:
    """Per-turn classifier categories as logged events (Pass 1 §7's crisis
    row: observability is what makes A.4 diagnosable). Raw results are
    logged alongside whether the chain's priority applied them."""
    events: list[tuple[str, dict]] = [
        ("classifier_decision", {
            "classifier": "frame_breaker",
            "raw": bool(pre_turn.frame_breaker_raw),
            "applied": bool(pre_turn.is_frame_breaker),
        }),
        ("classifier_decision", {
            "classifier": "relational_safety",
            "raw": pre_turn.rs_raw,
            "applied": bool(pre_turn.rs_updates) or pre_turn.is_relational_safety_firing,
            "firing": bool(pre_turn.is_relational_safety_firing),
        }),
    ]
    if pre_turn.is_epistemology_bridge:
        events.insert(0, ("classifier_decision", {
            "classifier": "epistemology_bridge", "raw": True,
            "applied": True}))
    if pre_turn.modern_term_match is not None:
        events.append(("classifier_decision", {
            "classifier": "modern_term",
            "raw": pre_turn.modern_term_match, "applied": True}))
    if pre_turn.repair is not None:
        events.append(("classifier_decision", {
            "classifier": "repair", "raw": {
                "kind": pre_turn.repair["kind"],
                "claim": pre_turn.repair["claim"],
                "verdict": pre_turn.repair["verdict"],
                "matched_contested": pre_turn.repair["matched_contested"],
            }, "applied": True}))
        # the datum §10's held/concession rates are computed from
        events.append(("challenge_adjudicated", {
            "world_id": pre_turn.repair["challenged_world_id"],
            "kind": pre_turn.repair["kind"],
            "verdict": pre_turn.repair["verdict"],
            "matched_contested": pre_turn.repair["matched_contested"],
        }))
    if getattr(pre_turn, "grounding_offer", None) is not None:
        events.append(("classifier_decision", {
            "classifier": "grounding_offer",
            "raw": {"term": pre_turn.grounding_offer["term"]},
            "applied": True}))
    if pre_turn.rs_updates:
        events.append(("rs_state_updated", {"updates": pre_turn.rs_updates}))
    return events


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

    # Cleanup (in-memory event log only; the durable JSONL/Supabase log
    # survives the process by design - §6.7's audit durability)
    EVENT_STORE.clear()


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
    # Wave 3 (Readiness P0-3b): the optional "what brings you here?" answer,
    # stored for feedback correlation only - see sessions.persona in
    # supabase_schema.sql. Never read by the graph; not participant_role.
    persona: str | None = None


class StartSessionResponse(BaseModel):
    """Response for starting a new session."""

    session_id: str
    session_token: str  # possession secret - see app/session_auth.py
    messages: list[dict]
    world_id: str  # Primary world (first in list)
    world_ids: list[str] = []  # All worlds at table


class CurriculumRef(BaseModel):
    """Identifies an exact, unmodified tap on a Guided-Questions curriculum
    starter (see app/answer_bank.py) - never sent for a free-typed message,
    and never inferred from one. role/set_id/question_order match
    Ministry/Features/Guided-Questions/Design/CiC_Guided_Questions_Curriculum_V1_0.json
    exactly (roles[].id, roles[].sets[].id, roles[].sets[].questions[].order)."""

    role: str
    set_id: str
    question_order: int


class SendMessageRequest(BaseModel):
    """Request to send a message."""

    message: str
    close_requested: bool = False
    # SH-11: present only when `message` is a verbatim curriculum-starter
    # tap - see CurriculumRef and app/answer_bank.py. None for every
    # ordinary free-typed message, which is the overwhelming majority of
    # traffic and always goes straight to live generation.
    curriculum_ref: CurriculumRef | None = None


class PilotRequest(BaseModel):
    """A pilot "express interest" submission from cic-website/pilot.html."""

    name: str
    email: str
    seat: str | None = None
    why_interested: str | None = None
    referred_by: str | None = None


class PilotFeedbackRequest(BaseModel):
    """Post-conversation feedback from cic-website/pilot-feedback.html - a
    different thing from PilotRequest above (that's "I'd like to join",
    this is "here's what a conversation I already had was actually like").
    Every field but the form's own required-by-browser select is optional,
    matching the form's own "answer whatever feels comfortable" framing."""

    perspective: str | None = None
    tradition: str | None = None
    confusing: str | None = None
    invented_or_overstated: str | None = None
    what_it_opened: str | None = None
    fundable_potential: str | None = None
    anything_else: str | None = None
    name: str | None = None
    email: str | None = None


class GenerateReferralRequest(BaseModel):
    """Identifies the referring tester by self-reported email, not a bearer
    token - see submit_referral_redemption's docstring for why."""

    referrer_email: str


class RedeemReferralRequest(BaseModel):
    """A friend redeeming a code from cic-website/refer-a-friend.html."""

    code: str
    name: str
    email: str


class CheckoutRequest(BaseModel):
    """A contribution started from cic-website/support.html (SH-9)."""

    mode: str  # "once" or "monthly" - see app/giving.py
    amount_cents: int
    success_url: str
    cancel_url: str


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
    # Added Wave 3 (Engineering P1-11): without these, a rehydrated session
    # has no way to know which world(s)/representative(s) it was talking to -
    # the reconnect endpoint existed but nothing in the frontend called it,
    # so a page refresh always lost the conversation. See useConversation.ts.
    world_id: str | None = None
    world_ids: list[str] = []


def state_to_messages(state: ConversationState) -> list[dict]:
    """Convert state messages to serializable dicts.

    S4.5: bridge-reframe sentinels (the persisted "question actually
    asked", §6.6) are internal to the Representatives' transcript view -
    the participant already heard the Facilitator's spoken version, so
    they are filtered from every participant-facing response."""
    result = []
    for msg in state.messages:
        if (getattr(msg, "additional_kwargs", None) or {}).get("bridge_reframe"):
            continue
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
        glosses_used = None
        if hasattr(msg, "additional_kwargs"):
            citations = msg.additional_kwargs.get("citations") or None
            glosses_used = msg.additional_kwargs.get("glosses_used") or None

        result.append({
            "role": role,
            "content": content,
            "name": name,
            "citations": citations,
            "glosses_used": glosses_used,
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
        world_ids = request.world_ids[:3]  # Cap at 3 worlds max - permanent (Mark's decision 2026-08-01, cost-driven; not a Phase-1 placeholder for a later raise to 5)
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

    # Insert the sessions row check_and_reserve_session_slot's own docstring
    # already claimed happens here - it didn't (2026-08-05 full-system
    # review, Engineering P0-2). transcript_logging.write_transcript later
    # upserts this same row by id, so this insert and that upsert can't
    # race into a duplicate-key error; this just makes sure the row exists
    # from turn zero, independent of pilot_logging_enabled, since session
    # *counting* and transcript *capture* are different questions that
    # sharing one flag was quietly conflating. Never blocks session start:
    # a failed insert here is logged and swallowed, same fail-open
    # discipline as write_transcript itself.
    if supabase_configured() and user.user_id is not None:
        from app.auth import _get_client  # local import: same pattern as this file's other Supabase call sites

        try:
            _get_client().table("sessions").insert({
                "id": session_id,
                "user_id": user.user_id,
                "world_ids": world_ids,
                "phase": state.phase,
                "turn_count": state.turn_count,
                "persona": request.persona,
            }).execute()
        except Exception:
            logger.exception("sessions row insert failed for session %s", session_id)

    # Commit the session's opening to the event log: who was seated, the
    # facilitator's spoken reception/handoff, and the flow scalars the
    # graph run produced. The projection (EVENT_STORE.get_state) is now
    # the only way any later request sees this session.
    # The session's possession secret, minted exactly once, here. It reaches
    # a later request only by being folded into ConversationState through the
    # session_started event (events.py's project), exactly like user_id -
    # not stored beside the event log in a parallel dict.
    session_token = mint_session_token()
    EVENT_STORE.append_many(session_id, [
        ("session_started", {
            "user_id": user.user_id,
            "session_token": session_token,
            "world_id": world_id,
            "world_ids": world_ids,
        }),
        *[("spoken_message", serialize_message(m)) for m in state.messages],
        ("turn_committed", {
            "phase": state.phase,
            "current_speaker": state.current_speaker,
            "current_world_id": state.current_world_id,
            "turn_count": state.turn_count,
        }),
    ])

    return StartSessionResponse(
        session_id=session_id,
        session_token=session_token,
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


@app.post("/api/pilot/feedback")
async def submit_pilot_feedback(request: PilotFeedbackRequest):
    """
    Record a post-conversation feedback submission
    (cic-website/pilot-feedback.html's form). Added 2026-08-05 - the form
    previously posted to a mailto: action, which is unreliable in modern
    browsers and, per the full-system review (Readiness P1-9), was reaching
    almost nobody.

    A no-op (but still returns success, so the form doesn't show an error)
    if Supabase isn't configured - same "off until configured" discipline
    as submit_pilot_request above.
    """
    from app.auth import _get_client, supabase_configured

    if not supabase_configured():
        return {"status": "received"}

    try:
        _get_client().table("pilot_feedback").insert(
            {
                "perspective": request.perspective,
                "tradition": request.tradition,
                "confusing": request.confusing,
                "invented_or_overstated": request.invented_or_overstated,
                "what_it_opened": request.what_it_opened,
                "fundable_potential": request.fundable_potential,
                "anything_else": request.anything_else,
                "name": request.name,
                "email": request.email,
            }
        ).execute()
    except Exception:
        raise HTTPException(status_code=500, detail="Something went wrong submitting your feedback. Please try again or email info@churchinconversation.com directly.")

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
        {"referred_by_invite_id": invite_id, "max_sessions": 5}
    ).eq("user_id", invited.user.id).execute()

    return {"status": "invited"}


# Where a checkout's success_url/cancel_url are allowed to point. Both are
# caller-supplied (cic-website builds them from its own current page), so
# without a check here this endpoint would create a real, working Stripe
# Checkout Session that redirects a paying participant's browser wherever
# an attacker's request asked - not a way to steal the gift itself (Stripe's
# own hosted page collects the card), but a real open-redirect surface
# riding on a legitimate payment flow. localhost stays allowed for local
# dev against a real Stripe test-mode key.
# _ALLOWED_REDIRECT_PREFIXES used to be matched with str.startswith(), which
# a host like "churchinconversation.com.attacker.example" or
# "localhost.attacker.example" also starts with - the exact open-redirect
# this check exists to close. Compare the parsed hostname exactly instead
# (2026-08-05, full-system review, Engineering P1-1).
_ALLOWED_REDIRECT_HOSTS = {
    "churchinconversation.com",
    "www.churchinconversation.com",
    "churchinconversation.org",
    "www.churchinconversation.org",
    "localhost",
    "127.0.0.1",
}


def _validate_redirect_url(url: str) -> None:
    parsed = urlparse(url)
    if parsed.scheme not in ("https", "http") or parsed.hostname not in _ALLOWED_REDIRECT_HOSTS:
        raise HTTPException(status_code=400, detail="Invalid redirect URL.")


@app.post("/api/support/checkout")
async def create_support_checkout(request: CheckoutRequest):
    """
    Start a Stripe Checkout Session for a voluntary contribution
    (cic-website/support.html - SH-9). No sign-in, no session, no gating -
    see app/giving.py's module docstring for why a gift is deliberately
    independent of everything else in this app.

    503s cleanly if STRIPE_SECRET_KEY isn't set yet, matching every other
    Supabase/Stripe-dependent endpoint's "off until configured" discipline -
    the frontend already knows to fall back to the direct email ask when it
    sees this, so the Support page can ship before Mark has real Stripe keys.
    """
    from app.giving import GivingNotConfigured, InvalidAmount, create_checkout_session

    _validate_redirect_url(request.success_url)
    _validate_redirect_url(request.cancel_url)

    try:
        url = create_checkout_session(
            request.mode, request.amount_cents, request.success_url, request.cancel_url
        )
    except GivingNotConfigured:
        raise HTTPException(status_code=503, detail="Giving isn't live yet - check back soon.")
    except InvalidAmount:
        raise HTTPException(status_code=400, detail="That amount is outside what this form accepts.")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    return {"url": url}


@app.post("/api/support/webhook")
async def support_webhook(request: Request):
    """
    Stripe's own server calls this, not a participant's browser - see the
    Stripe dashboard webhook config in the SH-9 logistics doc. The only
    durable record a contribution leaves in this app (see app/giving.py);
    everything else about the gift lives in Stripe's own dashboard.
    """
    from app.giving import GivingNotConfigured, verify_and_log_webhook

    payload = await request.body()
    sig_header = request.headers.get("stripe-signature")

    try:
        verify_and_log_webhook(payload, sig_header)
    except GivingNotConfigured:
        raise HTTPException(status_code=503, detail="Giving isn't live yet - check back soon.")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception:
        # Covers stripe.error.SignatureVerificationError without importing
        # the stripe package at module load time when it isn't configured -
        # same lazy-import discipline as the rest of this module.
        raise HTTPException(status_code=400, detail="Invalid webhook signature.")

    return {"status": "ok"}


@app.post("/api/session/{session_id}/message", response_model=SendMessageResponse)
async def send_message(session_id: str, request: SendMessageRequest,
                        x_session_token: str | None = Header(default=None)):
    """
    Send a message in an existing conversation.

    The message is processed by the representative (with RAG augmentation)
    and then monitored for drift by the facilitator.
    """
    from app.graph.nodes import new_request_id
    request_id = new_request_id()

    if not EVENT_STORE.has(session_id):
        raise HTTPException(status_code=404, detail="Session not found")

    # A fresh per-request projection of the event log - the working state
    # this handler mutates locally; every mutation that used to persist on
    # the shared dict object is appended to the log at the same point.
    state = EVENT_STORE.get_state(session_id)
    require_session_access(state, x_session_token)

    # Handle close request
    if request.close_requested:
        state.close_requested = True
        EVENT_STORE.append(session_id, "close_requested", {})

        # Run closing node
        from app.graph.nodes import facilitator_closes
        result = facilitator_closes(state)

        # Update state
        new_msgs = result.get("messages", [])
        state.messages = list(state.messages) + new_msgs
        state.phase = result.get("phase", "closing")

        EVENT_STORE.append_many(session_id, [
            *[("spoken_message", serialize_message(m)) for m in new_msgs],
            ("phase_changed", {"phase": state.phase}),
        ])
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
    cap_allowed, cap_reason = check_message_cap(state.turn_count, is_table=len(state.world_ids) > 1)
    if not cap_allowed:
        cap_message = AIMessage(content=cap_reason, name="facilitator")
        state.messages = list(state.messages) + [cap_message]
        EVENT_STORE.append(session_id, "spoken_message",
                           serialize_message(cap_message))
        write_transcript(session_id, state)
        return SendMessageResponse(
            messages=state_to_messages(state),
            phase=state.phase,
            turn_count=state.turn_count,
        )

    # Add the participant's message
    state.messages = list(state.messages) + [HumanMessage(content=request.message)]
    EVENT_STORE.append(session_id, "participant_message",
                       {"text": request.message, "name": None,
                        "addressee": None})

    # S4.1: the same governance layer the streaming endpoint traverses
    # (app/graph/governance.py), with this endpoint's historical intercept
    # set: frame-breaker + relational-safety (it has never had the
    # epistemology or modern-term bridges - unchanged here; the ONE
    # intended S4.1 delta is the table checks added below).
    from app.graph import governance
    from app.graph.nodes import get_llm, stream_relational_safety_response
    from app.prompts import FACILITATOR_FRAME_BREAKER_RESPONSE_PROMPT

    pre_turn = await governance.classify_pre_turn(
        state, request.message,
        include_epistemology=False,
        include_closing=False,
        include_modern_term=False,
        include_repair=True,
    )
    is_frame_breaker = pre_turn.is_frame_breaker
    rs_classification = pre_turn.rs_classification
    rs_updates = pre_turn.rs_updates
    pre_track_a_active = pre_turn.pre_track_a_active
    pre_track_a_severity = pre_turn.pre_track_a_severity
    pre_track_b_active = pre_turn.pre_track_b_active

    # per-turn classifier categories become logged events (§6.7 - what
    # makes A.4 diagnosable), plus the relational-safety state mutation
    # classify_pre_turn just applied to the working state
    EVENT_STORE.append_many(session_id, _classifier_events(pre_turn))

    if is_frame_breaker:
        from app.usage_logging import log_llm_usage
        from app.graph.nodes import build_table_composition
        llm = get_llm()
        response = llm.invoke([
            SystemMessage(content=FACILITATOR_FRAME_BREAKER_RESPONSE_PROMPT.format(
                message=request.message,
                table_composition=build_table_composition(state))),
            HumanMessage(content="Respond as the Facilitator, per your instructions above."),
        ])
        log_llm_usage("frame_breaker_response_plain", response, settings.llm_model,
                      session_id=session_id)
        fb_message = AIMessage(content=response.content, name="facilitator")
        state.messages = list(state.messages) + [fb_message]
        EVENT_STORE.append(session_id, "spoken_message",
                           serialize_message(fb_message))
        write_transcript(session_id, state)
        return SendMessageResponse(
            messages=state_to_messages(state),
            phase=state.phase,
            turn_count=state.turn_count,
        )

    # Not a frame-breaker - the relational-safety classification, state
    # mutation, and firing decision were all made inside
    # governance.classify_pre_turn with the exact old semantics (mutation
    # only when no higher intercept fired)
    if pre_turn.is_relational_safety_firing:
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
        EVENT_STORE.append(session_id, "spoken_message",
                           serialize_message(new_message))
        write_transcript(session_id, state)
        return SendMessageResponse(
            messages=state_to_messages(state),
            phase=state.phase,
            turn_count=state.turn_count,
        )

    # S4.6: a repair hit conditions the challenged Representative's own
    # turn - the selected hold/concede strategy rides in as the private
    # directive (turn-local, never persisted). Single-responder paths
    # only; the plain multi-world "all" path keeps current behavior (its
    # working states don't carry the directive - declared in the
    # checkpoint artifact).
    if pre_turn.repair is not None:
        state.private_directive = pre_turn.repair["directive"]
        state.current_world_id = pre_turn.repair["challenged_world_id"]
    elif pre_turn.grounding_offer is not None:
        # S4.7 (Pass 1 §6.4): the restricted offer opens the answering
        # turn - one directive slot, repair takes precedence
        state.private_directive = pre_turn.grounding_offer["directive"]

    # For multi-world tables, determine turn type (single or all representatives)
    from app.graph.nodes import determine_turn_type, multi_representative_engages

    # The exclusion-set diff: representative_engages mutates
    # state.surfaced_chunk_ids in place on the plain single-world path
    # (and, per FLAG-007, only there) - captured as events by diffing
    # around the call rather than changing the mechanism this step.
    pre_surfaced = {k: list(v) for k, v in state.surfaced_chunk_ids.items()}

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
        # Single-world table (interview mode) - check the answer bank first
        # (SH-11: app/answer_bank.py). Returns None on any kind of miss
        # (no curriculum_ref at all - the overwhelming majority of
        # messages - no bank entry yet, or a text mismatch), in which case
        # this is byte-for-byte the same call the live path always made.
        from app.answer_bank import try_answer_bank
        result = try_answer_bank(state, request.curriculum_ref.model_dump()
                                 if request.curriculum_ref else None,
                                 request.message, request_id=request_id)
        if result is None:
            result = representative_engages(state, request_id=request_id)

    # Update state with representative's response(s)
    new_msgs = result.get("messages", [])
    state.messages = list(state.messages) + new_msgs
    state.turn_count = result.get("turn_count", state.turn_count)
    state.requires_reroot = result.get("requires_reroot", False)
    state.retrieved_context = result.get("retrieved_context")
    state.current_world_id = result.get("current_world_id", state.current_world_id)

    turn_events: list[tuple[str, dict]] = []
    for wid, ids in state.surfaced_chunk_ids.items():
        prev = set(pre_surfaced.get(wid, []))
        newly = [i for i in ids if i not in prev]
        if newly:
            turn_events.append(("chunks_surfaced",
                                {"world_id": wid, "chunk_ids": newly}))
    turn_events.extend(
        ("spoken_message", serialize_message(m)) for m in new_msgs)
    turn_events.append(("turn_committed", {
        "turn_count": state.turn_count,
        "current_world_id": state.current_world_id,
        "requires_reroot": state.requires_reroot,
    }))
    turn_events.append(("retrieved_context_set", {
        "context": _serialize_retrieved_context(state.retrieved_context)}))
    EVENT_STORE.append_many(session_id, turn_events)

    # Run monitoring
    from app.graph.nodes import facilitator_monitors, facilitator_reroots

    monitor_result = facilitator_monitors(state)
    state.requires_reroot = monitor_result.get("requires_reroot", False)

    monitor_events: list[tuple[str, dict]] = []
    if monitor_result.get("drift_signals"):
        state.drift_signals = list(state.drift_signals) + monitor_result["drift_signals"]
        monitor_events.append(("drift_signals_appended", {
            "signals": [_serialize_drift_signal(s)
                        for s in monitor_result["drift_signals"]]}))

    # If reroot needed, run reroot (invisible to participant)
    if state.requires_reroot:
        reroot_result = facilitator_reroots(state)
        if reroot_result.get("drift_signals"):
            state.drift_signals = list(state.drift_signals) + reroot_result["drift_signals"]
            monitor_events.append(("drift_signals_appended", {
                "signals": [_serialize_drift_signal(s)
                            for s in reroot_result["drift_signals"]]}))
        state.requires_reroot = reroot_result.get("requires_reroot", False)
    monitor_events.append(("turn_committed",
                           {"requires_reroot": state.requires_reroot}))
    EVENT_STORE.append_many(session_id, monitor_events)

    # S4.1's ONE intended behavior delta: this endpoint gains the same
    # per-round table checks the streaming path always ran - multi-world
    # turns only, fail-open like all invisible governance
    if state.world_ids and len(state.world_ids) > 1:
        try:
            signals, guidance_items = governance.run_table_checks(
                state, list(state.messages), responding_worlds,
                state.world_id, state.world_ids)
            state.drift_signals = list(state.drift_signals) + signals
            table_events: list[tuple[str, dict]] = []
            if signals:
                table_events.append(("drift_signals_appended", {
                    "signals": [_serialize_drift_signal(s) for s in signals]}))
            # S4.3: every finding goes through the one guidance gate -
            # priority-ordered per world, nothing lost to statement order
            for wid, stype, sev, text in guidance_items:
                state.pending_guidance = governance.queue_guidance(
                    state.pending_guidance, wid, stype, sev, text)
                table_events.append(("guidance_queued", {
                    "world_id": wid,
                    "entry": {"signal_type": stype, "severity": sev,
                              "text": text}}))
            if table_events:
                EVENT_STORE.append_many(session_id, table_events)
        except Exception:
            pass

    return SendMessageResponse(
        messages=state_to_messages(state),
        phase=state.phase,
        turn_count=state.turn_count,
    )


@app.post("/api/session/{session_id}/message/stream")
async def send_message_stream(session_id: str, request: SendMessageRequest,
                               x_session_token: str | None = Header(default=None)):
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

    if not EVENT_STORE.has(session_id):
        raise HTTPException(status_code=404, detail="Session not found")

    if request.close_requested:
        raise HTTPException(
            status_code=400,
            detail="close_requested is not supported on the streaming endpoint - use /message",
        )

    # fresh per-request projection of the event log (see /message above)
    state = EVENT_STORE.get_state(session_id)
    require_session_access(state, x_session_token)

    # Soft, identity-free conversation-length cap (see app/message_cap.py) -
    # checked before anything else, same rationale and placement as the
    # non-streaming /message endpoint above. Short-circuits with a single
    # facilitator message and skips the classify-then-route chain below
    # entirely rather than threading a cap check through it.
    from app.message_cap import check_message_cap
    cap_allowed, cap_reason = check_message_cap(state.turn_count, is_table=len(state.world_ids) > 1)
    if not cap_allowed:
        def sse(event: dict) -> str:
            return f"data: {json.dumps(event)}\n\n"

        def capped_stream():
            yield sse({"type": "speaker_start", "speaker": "facilitator"})
            yield sse({"type": "token", "speaker": "facilitator", "text": cap_reason})
            cap_message = AIMessage(content=cap_reason, name="facilitator")
            state.messages = list(state.messages) + [cap_message]
            EVENT_STORE.append(session_id, "spoken_message",
                               serialize_message(cap_message))
            write_transcript(session_id, state)
            yield sse({"type": "speaker_end", "speaker": "facilitator", "citations": None})
            yield sse({"type": "done", "phase": state.phase, "turn_count": state.turn_count})

        return StreamingResponse(capped_stream(), media_type="text/event-stream")

    state.messages = list(state.messages) + [HumanMessage(content=request.message)]
    EVENT_STORE.append(session_id, "participant_message",
                       {"text": request.message, "name": None,
                        "addressee": None})

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

    # S4.1: the pre-turn intercept phase lives in the governance layer
    # (app/graph/governance.py) - one layer both endpoints traverse, with
    # the chain order preserved exactly (see its docstring; the original
    # inline rationale is preserved in git history at this spot). The
    # streaming path enables the full chain.
    from app.graph import governance

    pre_closing_stage = state.closing_stage
    pre_turn = await governance.classify_pre_turn(
        state, request.message,
        include_epistemology=True,
        include_closing=True,
        include_modern_term=True,
        include_repair=True,
    )
    # classifier categories + applied relational-safety/closing state
    # mutations, as events (§6.7 observability; A.4's diagnosis data)
    _pre_events = _classifier_events(pre_turn)
    if state.closing_stage != pre_closing_stage:
        _pre_events.append(("closing_stage_changed",
                            {"stage": state.closing_stage}))
    EVENT_STORE.append_many(session_id, _pre_events)

    is_epistemology_bridge = pre_turn.is_epistemology_bridge
    is_frame_breaker = pre_turn.is_frame_breaker
    rs_classification = pre_turn.rs_classification
    rs_updates = pre_turn.rs_updates
    is_relational_safety_firing = pre_turn.is_relational_safety_firing
    pre_track_a_active = pre_turn.pre_track_a_active
    pre_track_a_severity = pre_turn.pre_track_a_severity
    pre_track_b_active = pre_turn.pre_track_b_active
    higher_intercept = pre_turn.higher_intercept
    closing_turns = pre_turn.closing_turns
    modern_term_match = pre_turn.modern_term_match
    is_modern_term_bridge = pre_turn.is_modern_term_bridge
    should_check_wind_down = pre_turn.should_check_wind_down

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
    # S4.4a (F9): the floor now reads wrs/parameters.yaml's
    # turn_floor_multi_world - the first runtime consumer of the
    # canonical parameters file (see _multi_world_turn_floor above).
    # Its retirement to a per-conversation contract is S4.4b, after M3.
    MIN_MULTI_WORLD_TURNS = _TURN_FLOOR_MULTI_WORLD
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
            EVENT_STORE.append(session_id, "spoken_message",
                               serialize_message(new_message))
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
            # defined, and the matching rs_state_updated event was already
            # appended to the log - so they're durable even before this
            # branch's own message is appended below.
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
            EVENT_STORE.append(session_id, "spoken_message",
                               serialize_message(new_message))
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
            EVENT_STORE.append_many(session_id, [
                ("spoken_message", serialize_message(m))
                for m in new_messages])
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
                    elif event["type"] == "reframe":
                        # S4.5 (§6.6): the reframed question persists as a
                        # first-class event AND as a Facilitator-spoken
                        # sentinel in the transcript every Representative
                        # reads - never streamed to the participant (they
                        # heard the Facilitator's own spoken version)
                        EVENT_STORE.append(session_id, "bridge_reframe", {
                            "bridge": "modern_term",
                            "question": event["question"],
                            "term_id": event["term_id"],
                            "subject": event["subject"],
                            "split": event["split"],
                            "anachronistic_for": event["anachronistic_for"],
                            "native_for": event["native_for"],
                            "native_subject_map": event["native_subject_map"],
                        })
                        new_messages.append(AIMessage(
                            content=event["question"], name="facilitator",
                            additional_kwargs={"bridge_reframe": True}))
                    elif event["type"] == "complete":
                        new_messages.append(event["message"])
            except Exception as exc:
                yield sse({"type": "error", "message": str(exc)})
                return

            if not is_multi_world:
                state.messages = list(state.messages) + new_messages
                EVENT_STORE.append_many(session_id, _message_events(new_messages))
                write_transcript(session_id, state)

                yield sse({"type": "done", "phase": state.phase, "turn_count": state.turn_count})
                return

            # Multi-world: the bridge itself only ever answers through ONE
            # seated world (see stream_modern_term_bridge/classify_modern_term -
            # it hands the reframed question to seated_world_ids[0] alone).
            # Returning unconditionally here regardless of how many worlds are
            # seated was the actual root cause of a reported live failure -
            # "only Chloe talked" in a three-world round - not a flaky
            # exception; every anachronism-bridge turn in a multi-world round
            # silently ended the round after one speaker. Seed the shared
            # continuation loop below with what already happened so the other
            # seated worlds still get their contractual chance to react,
            # instead of hard-ending the round here.
            bridge_seed_messages = new_messages
            bridge_seed_world_id = modern_term_match["world_id"]

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
            EVENT_STORE.append_many(session_id, [
                ("spoken_message", serialize_message(m))
                for m in new_messages])
            write_transcript(session_id, state)

            yield sse({"type": "done", "phase": state.phase, "turn_count": state.turn_count})
            return

        # everything already in state.messages is already in the event log;
        # the round commit below events exactly what this round adds
        round_base_len = len(state.messages)
        if is_modern_term_bridge:
            # Falls through from the multi-world bridge branch above (the
            # single-world case already returned there) - the bridge's own
            # representative turn seeds the loop as turn 1 so the MIN/MAX
            # counters and must_continue logic below see it as part of this
            # round, not a fresh empty round.
            working_messages = list(state.messages) + bridge_seed_messages
            last_current_world_id = bridge_seed_world_id
            turns_completed = 1
            spoken_this_round: list[str] = [bridge_seed_world_id]
        else:
            working_messages = list(state.messages)
            last_current_world_id = state.current_world_id
            turns_completed = 0
            spoken_this_round: list[str] = []

        # A round the participant opened by naming one representative
        # directly ("Marius, what did Leo actually claim?") should be able
        # to end after that one answer. select_next_speaker already routes
        # the opening turn to the addressed representative regardless of
        # must_continue (nodes.py's direct-address detection runs before
        # the must_continue check) - but until now, must_continue's own
        # MIN_MULTI_WORLD_TURNS floor still forced a second, unaddressed
        # voice into every round regardless, since it had no way to know
        # the opening turn was already a complete, addressed answer rather
        # than an opening volley expecting more voices. Detected once, on
        # the participant's own message, since that's what select_next_speaker
        # itself checks for the round's opening turn (2026-08-05 full-system
        # review, Readiness P1-8).
        round_was_direct_addressed = False
        if is_multi_world and not is_modern_term_bridge:
            from app.graph.nodes import detect_direct_address
            round_was_direct_addressed = (
                detect_direct_address(request.message, world_ids) is not None)

        try:
            while True:
                # S4.6: a repair hit determines the round's FIRST speaker -
                # the challenged Representative answers, carrying the
                # selected hold/concede strategy; no selector call (the
                # repair initiation is addressed to them as surely as a
                # direct address is)
                if (pre_turn.repair is not None and turns_completed == 0
                        and pre_turn.repair["challenged_world_id"] in world_ids):
                    world_id = pre_turn.repair["challenged_world_id"]
                    private_directive = pre_turn.repair["directive"]
                elif (getattr(pre_turn, "grounding_offer", None) is not None
                        and turns_completed == 0 and not is_multi_world):
                    # S4.7 (§6.4): the restricted offer opens the answering
                    # turn - single migrated-world sessions, one offer only
                    world_id = state.world_id
                    private_directive = pre_turn.grounding_offer["directive"]
                elif is_multi_world:
                    # Ask, before each turn, who is most directly positioned to
                    # speak next given what has actually been said so far -
                    # instead of working through a fixed list of every world at
                    # the table in the same order every round.
                    snapshot = ConversationState(
                        messages=working_messages,
                        world_id=state.world_id,
                        world_ids=state.world_ids,
                        worlds_at_table=state.worlds_at_table,
                        # S4.7: the mode-register observation rides into
                        # the selector as input (Pass 1 §6.5)
                        register_note=state.register_note,
                    )
                    must_continue = (turns_completed < MIN_MULTI_WORLD_TURNS
                                      and not round_was_direct_addressed)
                    # S4.4a: the selector's REASON (or the deterministic
                    # direct-address note) comes back through the sink and
                    # is delivered to the selected speaker as a private
                    # directive - see select_next_speaker's docstring
                    reason_sink: list[str] = []
                    world_id = select_next_speaker(snapshot, spoken_this_round, must_continue=must_continue, reason_sink=reason_sink)
                    if world_id is None:
                        break
                    private_directive = reason_sink[0] if reason_sink else None
                else:
                    if spoken_this_round:
                        break
                    world_id = state.world_id
                    private_directive = None

                # Pop (consume) the highest-priority guidance entry waiting
                # for this specific representative from an earlier round -
                # once delivered, it shouldn't repeat on every future turn.
                # S4.3: the slot is a priority queue; one entry is delivered
                # per turn and the rest stay queued (nothing is silently
                # dropped by contention anymore - see governance.queue_guidance).
                guidance_entry = None
                _queue = list(state.pending_guidance.get(world_id) or [])
                if _queue:
                    guidance_entry = _queue.pop(0)
                    if _queue:
                        state.pending_guidance = {**state.pending_guidance,
                                                  world_id: _queue}
                    else:
                        state.pending_guidance = {
                            k: v for k, v in state.pending_guidance.items()
                            if k != world_id}
                    EVENT_STORE.append(session_id, "guidance_consumed",
                                       {"world_id": world_id,
                                        "signal_type": guidance_entry["signal_type"]})
                guidance_for_speaker = (guidance_entry["text"]
                                        if guidance_entry else None)

                working_state = ConversationState(
                    messages=working_messages,
                    phase=state.phase,
                    current_speaker=state.current_speaker,
                    current_world_id=world_id,
                    turn_count=state.turn_count,
                    drift_signals=list(state.drift_signals),
                    requires_reroot=state.requires_reroot,
                    pending_guidance={world_id: [guidance_entry]} if guidance_entry else {},
                    private_directive=private_directive,
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
                # SH-11 (app/answer_bank.py): only the direct, non-reactive
                # answer to what the participant just sent is ever eligible
                # - a continuation turn within the same round is a live
                # reaction to another representative, never a curriculum
                # match. bank_turn_gen is None on any miss (including
                # simply not having a curriculum_ref at all, the ordinary
                # case), which falls straight through to the unchanged live
                # generator - same yield contract either way.
                bank_turn_gen = None
                if not is_reactive:
                    from app.answer_bank import stream_answer_bank
                    bank_turn_gen = stream_answer_bank(
                        working_state,
                        request.curriculum_ref.model_dump() if request.curriculum_ref else None,
                        request.message, request_id=request_id)
                turn_gen = bank_turn_gen if bank_turn_gen is not None else stream_representative_turn(
                    working_state, is_reactive=is_reactive, request_id=request_id)
                for event in turn_gen:
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
                    "glosses_used": new_message.additional_kwargs.get("glosses_used"),
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
            if turns_completed == 0:
                # Nothing was produced at all this round - a genuine failure
                # the participant needs to know about, not something to
                # paper over.
                yield sse({"type": "error", "message": str(exc)})
                return
            # At least one representative already answered in full before
            # this happened (e.g. a transient failure picking or generating
            # a SECOND speaker in a multi-world round - the exact failure
            # mode a real multi-world session hit live, "only Chloe talked"
            # when Marius/Albina were also seated). That answer is real and
            # complete; the participant already has something worth reading.
            # Commit what succeeded and close the round normally instead of
            # surfacing a dead-end error after a perfectly good response -
            # only the logs need to know a later speaker was skipped.
            logger.exception(
                "Multi-world round degraded early after %d turn(s) in session %s: %s",
                turns_completed, session_id, exc,
            )

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
        EVENT_STORE.append_many(session_id, [
            *_message_events(working_messages[round_base_len:]),
            ("turn_committed", {
                "turn_count": state.turn_count,
                "current_world_id": state.current_world_id,
                "requires_reroot": False,
            }),
        ])
        write_transcript(session_id, state)

        # Wind-down sensing streams here, before "done" - deliberately NOT
        # in the post-round invisible tail below. Unlike table checks
        # (which only ever queue guidance for a LATER turn via
        # pending_guidance, never anything the current participant sees),
        # this one has to actually put a question in front of the
        # participant to mean anything. Checking it after "done" used to
        # just flip state.closing_stage to "anything_else_asked" with
        # nobody having asked anything - the participant's own next,
        # unrelated message then got silently classified as a reply to a
        # question that was never sent, the visible failure being an
        # unprompted resources offer arriving out of nowhere (2026-08-05
        # full-system review, Readiness P1-4). Costs one extra classifier
        # call's latency before "done", only on rounds where
        # should_check_wind_down is already True (closing_stage=="none"
        # and no higher-priority intercept fired) - a real tradeoff, but
        # the alternative is a feature that has never once actually worked.
        if should_check_wind_down:
            try:
                from app.graph.closing_sequence import classify_wind_down, stream_closing_turn
                fired = classify_wind_down(state, request.message)
                EVENT_STORE.append(session_id, "classifier_decision", {
                    "classifier": "wind_down", "raw": bool(fired),
                    "applied": bool(fired)})
                if fired:
                    yield sse({"type": "speaker_start", "speaker": "facilitator"})
                    anything_else_msg = None
                    for event in stream_closing_turn(state, "anything_else"):
                        if event["type"] == "token":
                            yield sse({
                                "type": "token",
                                "speaker": event["speaker"],
                                "text": event["text"],
                            })
                        elif event["type"] == "complete":
                            anything_else_msg = event["message"]
                    yield sse({
                        "type": "speaker_end",
                        "speaker": "facilitator",
                        "citations": None,
                    })
                    if anything_else_msg is not None:
                        state.messages = list(state.messages) + [anything_else_msg]
                        state.closing_stage = "anything_else_asked"
                        EVENT_STORE.append_many(session_id, [
                            ("spoken_message", serialize_message(anything_else_msg)),
                            ("closing_stage_changed", {"stage": "anything_else_asked"}),
                        ])
                        write_transcript(session_id, state)
            except Exception:
                # Same fail-open discipline as the rest of this endpoint's
                # invisible governance: a failed wind-down check must never
                # break or delay the response the participant already has.
                logger.exception(
                    "wind-down anything-else turn failed for session %s", session_id)

        yield sse({"type": "done", "phase": state.phase, "turn_count": state.turn_count})

        # Everything below is invisible background governance the participant
        # never waits on - guarded by its own try/except (rather than relying
        # on the round loop's try/except above, which no longer wraps this
        # code now that it runs after "done") so a monitoring failure can
        # never surface as a broken response mid-stream; at worst this
        # round's drift checks are silently skipped.
        # S4.1: the invisible-governance tail lives in the governance
        # layer - table checks + per-message drift, each half fail-open.
        # S4.2: its findings are APPENDED to the event log - the
        # read-latest-merge (and the race it hand-patched) is gone
        # structurally; an append can never clobber a message that arrived
        # after "done" went out.
        # Wind-down sensing used to live here too - moved above, before
        # "done", 2026-08-05 (see the comment at that call site for why:
        # this tail can only ever affect a LATER turn, and wind-down needs
        # to affect this one).
        governance.run_post_round_governance(
            state, request.message,
            working_messages=working_messages,
            spoken_this_round=spoken_this_round,
            turns_completed=turns_completed,
            world_ids=world_ids,
            is_multi_world=is_multi_world,
            session_id=session_id,
        )

    return StreamingResponse(
        event_stream(),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )


@app.get("/api/session/{session_id}", response_model=SessionResponse)
async def get_session(session_id: str,
                       x_session_token: str | None = Header(default=None)):
    """
    Get the current state of a conversation session.

    Useful for reconnection or state inspection.
    """
    if not EVENT_STORE.has(session_id):
        raise HTTPException(status_code=404, detail="Session not found")

    state = EVENT_STORE.get_state(session_id)
    require_session_access(state, x_session_token)

    return SessionResponse(
        session_id=session_id,
        messages=state_to_messages(state),
        phase=state.phase,
        turn_count=state.turn_count,
        world_id=state.world_id,
        world_ids=state.world_ids or [],
    )


@app.get("/api/session/{session_id}/audit")
async def get_session_audit(session_id: str, since_seq: int = 0,
                            x_session_token: str | None = Header(default=None),
                            user: AuthedUser = Depends(get_audit_user)):
    """
    Get the full retrieval audit trail for a session, for review purposes.

    Unlike the normal message endpoints (which only surface citations meant
    for participants), this includes every lexicon file the retriever
    considered for each representative turn - retrieved or skipped, and why -
    so a reviewer can see exactly what source material each answer drew on.

    S4.2 (Pass 1 §6.7): durable and authenticated - it is Level 3's
    backbone for live conversations. Durable: the session is projected
    from the append-only event log, which persists to disk (and Supabase
    when configured), so this endpoint survives a process restart instead
    of dying with the in-memory dict. Authenticated: requires a signed-in
    account once Supabase is configured (see auth.get_audit_user).

    Unconfigured deployments (no Supabase project yet) fall back to the same
    possession check every other session-scoped endpoint requires
    (app/session_auth.py) instead of staying open to anyone holding a
    session_id - see the supabase_configured() branch below. This only
    applies while unconfigured: once a real project exists, get_audit_user's
    signed-in check is the real gate, and a reviewer reading a session they
    did not start must NOT be made to hold that session's token too - that
    would lock out every reviewer but the participant themselves, breaking
    the endpoint's whole purpose.

    Temporal query: the response now also carries the raw event log
    (`events`), and `?since_seq=N` returns only events after sequence N -
    all existing response fields are unchanged (compatibility rule:
    participant-facing shapes only gain fields, never change them).
    """
    if not EVENT_STORE.has(session_id):
        raise HTTPException(status_code=404, detail="Session not found")

    state = EVENT_STORE.get_state(session_id)
    if not supabase_configured():
        require_session_access(state, x_session_token)

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
        # additive (§6.7): the append-only event log itself - per-turn
        # classifier categories, state transitions, spoken events - the
        # temporal record the projection above is derived from
        "events": [ev.to_json()
                   for ev in EVENT_STORE.events(session_id,
                                                since_seq=since_seq)],
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
    # S5.4 (additive - compatibility rule): for migrated worlds, the
    # repository record behind this term, so the frontend can fetch its
    # Level 2/Level 3 faces from /api/repository/record/{record_id}.
    # None for unmigrated worlds (no records yet).
    record_id: Optional[str] = None
    world_id: Optional[str] = None


class LexiconResponse(BaseModel):
    """Response containing all lexicon terms."""

    terms: list[LexiconTerm]


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

    # S5.4: for migrated worlds the chunk filename's stem prefix IS the
    # record id (generated views name files <record_id>_<slug>.md) - map
    # it only when the repository view confirms the id, so unmigrated
    # worlds' arbitrary filenames never produce a false link.
    repo_record_ids: set[str] = set()
    repo_path = world_config.data_path / "repository.json"
    if repo_path.exists():
        try:
            repo_view = _load_repository_view(world_id, "repository.json")
            repo_record_ids = {e["id"] for e in repo_view["records"]}
        except HTTPException:
            repo_record_ids = set()

    terms = []
    for file_path in sorted(lexicon_path.glob("*.md")):
        entry = indexer.parse_lexicon_file(file_path)

        # S3.1: the indexer now parses Quick Meaning itself (single
        # parser - the parallel one here silently dropped the section
        # for the fenced-front-matter worlds; see Pass 1 SS3.2)
        quick_meaning = entry.quick_meaning

        candidate_id = file_path.stem.split("_")[0]
        record_id = candidate_id if candidate_id in repo_record_ids else None

        terms.append(LexiconTerm(
            term=entry.term,
            aliases=entry.aliases,
            quick_meaning=quick_meaning,
            full_content=entry.content,
            related_terms=entry.related_terms,
            record_id=record_id,
            world_id=world_id if record_id else None,
        ))

    return LexiconResponse(terms=terms)


class ResourcePack(BaseModel):
    """One world's (or general's) further-reading list."""

    world_id: str
    world_offer_label: str
    resources: list[dict]


class ResourcesResponse(BaseModel):
    """Response for the ending-screen further-reading list (Readiness P1-3/Wave 3)."""

    packs: list[ResourcePack]


@app.get("/api/resources", response_model=ResourcesResponse)
async def get_resources(world_ids: str = ""):
    """
    Further-reading packs for the ending screen's takeaway artifact. Reuses the
    same per-world JSON files and loader the Facilitator's own sensed-closing
    resources offer already reads (app/graph/closing_sequence.py) - one source
    of truth, no duplicated resource lists. `general` is always appended last,
    matching that module's own append order.
    """
    from app.graph.closing_sequence import _load_resources

    valid_world_ids = [w.id for w in AVAILABLE_WORLDS]
    requested = [w for w in world_ids.split(",") if w]
    for w in requested:
        if w not in valid_world_ids:
            raise HTTPException(status_code=400, detail=f"Invalid world_id: {w}")

    packs = []
    seen: set[str] = set()
    for wid in [*requested, "general"]:
        if wid in seen:
            continue
        seen.add(wid)
        pack = _load_resources(wid)
        if not pack:
            continue
        packs.append(ResourcePack(
            world_id=pack.get("world_id", wid),
            world_offer_label=pack.get("world_offer_label", wid),
            resources=pack.get("resources", []),
        ))

    return ResourcesResponse(packs=packs)


# ---------------------------------------------------------------------------
# S5.4 - repository endpoints (Pass 1 §5.6): the browsable repository.
# The same records the Representative speaks from, browsable with no
# conversation running - by domain, by source, by figure, by contested
# claim; every record carries its Level 2 (terms) and Level 3 faces.
# Rights enforcement (display_permitted, FLAG-013 fail-closed) is applied
# at view GENERATION time (wrs/views/repository.py) - these endpoints
# serve the generated view and never touch raw records, so a rights leak
# would require regenerating the view, not just calling an endpoint.
# Additive beside the existing lexicon and audit endpoints; worlds without
# a generated repository (unmigrated) 404 honestly.
# ---------------------------------------------------------------------------

_REPOSITORY_CACHE: dict[str, tuple[float, dict]] = {}


def _load_repository_view(world_id: str, filename: str) -> dict:
    valid_world_ids = [w.id for w in AVAILABLE_WORLDS]
    if world_id not in valid_world_ids:
        raise HTTPException(status_code=400,
                            detail=f"Invalid world_id. Must be one of: {valid_world_ids}")
    path = settings.get_world_config(world_id).data_path / filename
    if not path.exists():
        raise HTTPException(
            status_code=404,
            detail=(f"No {filename} for {world_id} yet - repository views "
                    "exist for migrated worlds only (generated by "
                    "wrs/views/repository.py)"))
    key = str(path)
    mtime = path.stat().st_mtime
    cached = _REPOSITORY_CACHE.get(key)
    if cached and cached[0] == mtime:
        return cached[1]
    data = json.loads(path.read_text(encoding="utf-8"))
    _REPOSITORY_CACHE[key] = (mtime, data)
    return data


def _record_summary(entry: dict) -> dict:
    return {
        "id": entry["id"],
        "record_type": entry["record_type"],
        "title": entry["title"],
        "rights": entry["rights"],
    }


@app.get("/api/repository")
async def get_repository(world_id: str = "desert-monasticism"):
    """Browse index: record summaries + the four §5.6 browse dimensions."""
    repo = _load_repository_view(world_id, "repository.json")
    return {
        "world_id": repo["world_id"],
        "record_count": repo["record_count"],
        "rights_rule": repo["rights_rule"],
        "records": [_record_summary(e) for e in repo["records"]],
        "browse": repo["browse"],
    }


@app.get("/api/repository/search")
async def search_repository(q: str, world_id: str = "desert-monasticism"):
    """Substring search over the public search text (built after rights
    redaction - withheld text is unfindable by construction)."""
    repo = _load_repository_view(world_id, "repository.json")
    needle = q.strip().lower()
    if not needle:
        return {"world_id": world_id, "query": q, "matches": []}
    matches = [_record_summary(e) for e in repo["records"]
               if needle in e["search_text"]]
    return {"world_id": world_id, "query": q, "matches": matches}


@app.get("/api/repository/sources")
async def get_repository_sources(world_id: str = "desert-monasticism"):
    """The FAIR export (sources.json): stable ids, external identifiers,
    stated rights - machine-readable, per §5.6."""
    return _load_repository_view(world_id, "sources.json")


@app.get("/api/repository/record/{record_id}")
async def get_repository_record(record_id: str,
                                world_id: str = "desert-monasticism"):
    """One record's full faces: Level 2 (terms) + the Level 3
    Observe-Reflect-Question scaffold with the full record beneath."""
    repo = _load_repository_view(world_id, "repository.json")
    for entry in repo["records"]:
        if entry["id"] == record_id:
            return entry
    raise HTTPException(status_code=404,
                        detail=f"No record {record_id} in {world_id}")


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
        a same-named static file at the dist root (favicon.ico, icons, etc.).

        full_path is attacker-controlled (it's the literal rest of the URL,
        via Starlette's `path` converter, which does not strip `..`). Joining
        it onto _FRONTEND_DIST unresolved and trusting .is_file() is a path
        traversal: `Path("/a/b") / "../../../etc/passwd"` stats straight
        through to `/etc/passwd`, confirmed with a real file read in this
        exact join pattern before this fix went in. Since the container runs
        as root (no USER in the Dockerfile) with ANTHROPIC_API_KEY and other
        secrets as env vars, an unresolved join here can reach
        /proc/self/environ. Resolving the candidate and requiring it stay
        under _FRONTEND_DIST closes that; anything that resolves outside
        falls through to index.html, same as any other not-found path."""
        candidate = (_FRONTEND_DIST / full_path).resolve()
        if full_path and candidate.is_relative_to(_FRONTEND_DIST) and candidate.is_file():
            return FileResponse(candidate)
        return FileResponse(_FRONTEND_DIST / "index.html")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host=settings.host, port=settings.port)
