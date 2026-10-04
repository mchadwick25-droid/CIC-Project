"""FastAPI shape only (see /root/.claude/plans/linear-popping-dawn.md) - HTTP
parsing, headers, status codes. All business logic lives in engine.api.wiring;
this module never touches the M4/M5 pipeline directly.

`app` (module level) is what `uvicorn engine.api.app:app` serves. It is only
built when CIC_API_REGION is actually set in the environment - importing this
module under pytest (CIC_API_REGION unset in CI) leaves `app = None` rather
than trying to resolve model IDs or make a real, credentialed Bedrock client.
Tests import `create_app` directly and build their own app from fakes.
"""
import hmac
import json
import logging
import os
import queue
import threading
import time
from dataclasses import asdict, dataclass
from pathlib import Path

from fastapi import FastAPI, Header, HTTPException, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import FileResponse, JSONResponse, Response, StreamingResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from engine.api import admin_auth, anon_cap, db_backup, deeper_admission, deeper_routes, ratelimit, table_wiring, wiring
from engine.api.config import REPO_ROOT, Settings
from engine.deeper.config import DeeperConfig
from engine.m1.registry import load_registry
from engine.m4 import idle_close, session_code
from engine.m4 import round as round_module
from engine.m4 import turn as turn_module
from engine.m4.projection import project_fresh
from engine.m4.store import Store
from engine.m4.world_loader import LazyWorldLoader, PackageRefused
from engine.m7 import erase
from engine.m7 import retention
from engine.m7 import scheduler as m7_scheduler
from engine.m7.qc_store import QCStore
from engine.api.qc_recorder import QCRecorder
from engine.m8.log_store import UsageLogStore

def _message_failure(exc: Exception, session_id: str) -> HTTPException | None:
    """The HTTP answer for each refusal a participant message can meet, or
    None for anything else (a programming error stays a 500 and surfaces as
    itself rather than being reported as a provider problem)."""
    refusal = _refusal(exc, session_id)
    return HTTPException(status_code=refusal[0], detail=refusal[1]) if refusal else None


def _refusal(exc: Exception, session_id: str) -> tuple[int, str, str] | None:
    """(status, detail, code) for a refusal. The detail strings are the ones
    the plain endpoint has always returned; the code is the stable name a
    stream's error event carries beside it."""
    if isinstance(exc, wiring.SessionNotFound):
        return 401, _INVALID_SESSION_DETAIL, "invalid_session"
    if isinstance(exc, wiring.SessionClosed):
        return 409, "session already closed", "session_closed"
    if isinstance(exc, wiring.MessageTooLong):
        return 422, f"message too long (at most {wiring.MAX_MESSAGE_LENGTH} characters)", "message_too_long"
    if isinstance(exc, table_wiring.TableRoundStillOpen):
        return 409, "round still open - continue it before the next message", "round_open"
    if isinstance(exc, table_wiring.TableAdvanceInFlight):
        return 409, "advance already in flight - the table is already speaking", "advance_in_flight"
    if isinstance(exc, table_wiring.TableRoundNotOpen):
        return 409, "no open round to continue", "no_open_round"
    if isinstance(exc, wiring.DuplicateMessage):
        return 409, "duplicate message - already received", "duplicate_message"
    if isinstance(exc, PackageRefused):
        logger.warning("message refused: package unavailable session=%s", session_id)
        return 503, _WORLD_UNAVAILABLE_DETAIL, "world_unavailable"
    if isinstance(exc, wiring.ProviderCallFailed):
        # The bound exception carries the real Bedrock error - the one
        # signal that tells throttling apart from credentials apart
        # from a bug.
        logger.error("provider call failed session=%s: %s", session_id, exc)
        return 502, "provider call failed", "provider_failed"
    return None


def _sse(event: str, data: dict) -> str:
    return f"event: {event}\ndata: {json.dumps(jsonable_encoder(data), ensure_ascii=False)}\n\n"


def _spoke(voice) -> bool:
    """Whether a voice turn carries words. A reply with none leaves no pair in
    the memory the next turn counts from, so it is not charged either: the round
    number and the opening amount stay in step with what the person was given."""
    text = voice.get("text") if isinstance(voice, dict) else getattr(voice, "text", None)
    return voice is not None and bool((text or "").strip())


def _stream_turn(handle, done_body, voiced, session_id: str, started: float, admission=None) -> StreamingResponse:
    """One turn answered as an event stream: a "sentence" event for each
    sentence as the voice finishes writing it, with the marks the finished
    plan gives it (engine.m4.sentence_stream), and a final "done" event
    carrying the same body the plain endpoint returns, whose plan is
    authoritative. `handle(on_sentence)` runs the turn, `done_body(result)`
    builds the done body and `voiced(result)` says whether a voice spoke. A
    refusal before the first event is the same HTTP status and detail as the
    plain endpoint; a failure after the stream began is an "error" event
    carrying {code, status, detail}. The turn runs to completion and is
    recorded even if the reader disconnects."""
    events: queue.Queue = queue.Queue()

    def run() -> None:
        try:
            result = handle(lambda event: events.put(("sentence", event)))
        except Exception as exc:
            if admission is not None:
                admission.finish(False)
            events.put(("error", exc))
        else:
            if admission is not None:
                admission.finish(voiced(result))
            events.put(("done", result))

    threading.Thread(target=run, daemon=True).start()
    first = events.get()
    if first[0] == "error":
        failure = _message_failure(first[1], session_id)
        raise failure if failure is not None else first[1]

    def body():
        kind, payload = first
        while True:
            if kind == "sentence":
                yield _sse("sentence", payload)
            elif kind == "done":
                logger.info("turn handled ms=%d streamed=true", (time.monotonic() - started) * 1000)
                yield _sse("done", done_body(payload))
                return
            else:
                status, detail, code = _refusal(payload, session_id) or (500, "internal error", "internal")
                yield _sse("error", {"code": code, "status": status, "detail": detail})
                return
            kind, payload = events.get()

    return StreamingResponse(body(), media_type="text/event-stream", headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"})


class MissingAnonCapSecret(Exception):
    """Raised at app construction when anon_cap_enabled=True but no secret
    was given - same "never guess, fail loudly" posture as MissingConfigError
    in engine.api.config for region."""


_INVALID_SESSION_DETAIL = "invalid session"
_WORLD_UNAVAILABLE_DETAIL = "world temporarily unavailable"
_AUTH_PREFIX = "Session "

# The service's one logger. Bedrock errors are captured and logged bound
# to it, so a throttling storm is distinguishable from a credential
# failure. Session ids are logged; participant text and voice text never
# are.
logger = logging.getLogger("cic.api")


@dataclass
class Deps:
    voice_client: object
    voice_model_id: str
    safety_client: object
    safety_model_id: str
    store: Store
    usage_store: UsageLogStore
    world_loader: LazyWorldLoader
    registry: dict
    default_world_key: str
    enforce_admission: bool
    admin_token: str | None = None
    package_cache_dir: Path | None = None
    r27_enforce: bool = False
    self_revision_enabled: bool = True
    citation_attach_enabled: bool = False
    qc_recorder: object | None = None
    # Whether a client that asks for an event stream gets the reply sentence
    # by sentence while it is written (the Accept header decides per request).
    streaming_enabled: bool = False
    # Same directory m7_scheduler.start_background_scheduler already
    # writes to below - the usage-summary endpoint reads its
    # canon-candidates.json (last_run.json's own out_dir) rather than
    # recomputing it, so this is a read-only second consumer of an
    # existing daily job, not a new one. None in every test app (no
    # scheduler running, nothing to read) - the endpoint degrades to
    # omitting that section rather than erroring.
    m7_audit_root: Path | None = None
    # The dashboard's password login (engine.api.admin_auth) - None when
    # admin_token itself is unset, since a
    # password login with no admin_token to bootstrap it or sign its
    # sessions makes no sense (same "the whole feature is off" posture
    # admin_token's own absence already gives pilot-summary).
    admin_auth_store: admin_auth.AdminAuthStore | None = None


class SessionCreateRequest(BaseModel):
    world_key: str | None = None
    # 2-3 world keys creates a table session (Artifact-7 SS1/SS6); mutually
    # exclusive with world_key. Omit both for the default interview world.
    world_keys: list[str] | None = None


class SessionCreateResponse(BaseModel):
    session_id: str
    session_code: str
    # Stage 0c (Build-Plan.md): None for an interview session (no round cap
    # applies); the table session round cap for a table session - so the
    # frontend can render the real configured number instead of guessing.
    round_cap: int | None = None


# The hard bound on what the API accepts at all, against a payload attack.
# Anything over wiring.MAX_MESSAGE_LENGTH (4,000) is read by the safety call
# and then refused unless it routes to safety (System Hub decision 35).
_HARD_MAX_MESSAGE_LENGTH = 20000


class MessageRequest(BaseModel):
    # Bounds participant input length. Every message is forwarded to
    # Bedrock TWICE per turn (the safety gate, then voice generation) and
    # stored verbatim, at up to 40 messages/min per IP. Output is bounded
    # by max_tokens on the generation call; this bounds input the same
    # way.
    text: str = Field(max_length=_HARD_MAX_MESSAGE_LENGTH)
    client_msg_id: str | None = None


class MessageResponse(BaseModel):
    turn_no: int
    routing_action: str | None
    routing_reason: str
    degraded: bool
    facilitator: dict | None
    voice: dict | None
    limit_note: dict | None = None


class TableMessageResponse(BaseModel):
    """One table-round advance (Artifact-7 SS6): at most one voice turn per
    response, round_open says whether to POST /continue for the next.
    turn_no is set only on the response that committed the round."""
    round_no: int
    round_open: bool
    routing_action: str | None
    routing_reason: str
    degraded: bool
    facilitator: list[dict]
    turn_selected: dict | None
    voice: dict | None
    position: int | None
    turn_no: int | None
    session_closed: bool
    limit_note: dict | None = None


class TranscriptResponse(BaseModel):
    session_id: str
    world_key: str | None
    turn_count: int
    closed: bool
    transcript: list[dict]
    # Table sessions (Artifact-7): mode "table" with the seated world_keys;
    # interview sessions carry mode "interview" and world_keys None.
    mode: str | None = None
    world_keys: list[str] | None = None
    round_open: bool = False
    # Stage 0c (Build-Plan.md): same rule as SessionCreateResponse above.
    round_cap: int | None = None


class RoundCloseReasonsResponse(BaseModel):
    """Diagnostic-only, table sessions: every round_closed event's own
    payload for this session, in round order. Empty for an interview
    session or a table session with no round closed yet."""
    session_id: str
    rounds: list[dict]


class AdminSetPasswordRequest(BaseModel):
    password: str


class AdminLoginRequest(BaseModel):
    password: str


class AdminAuthStatusResponse(BaseModel):
    password_set: bool


class PilotSummaryResponse(BaseModel):
    """Admin-only, see wiring.PilotSummary's own docstring for what this
    deliberately does and doesn't carry."""
    total_sessions: int
    by_mode: dict[str, int]
    open_sessions: int
    closed_by_reason: dict[str, int]
    table_round_counts_on_cap: dict[str, int]
    earliest_session_at: str | None
    latest_session_at: str | None


class VisitorUsageResponse(BaseModel):
    """See wiring.VisitorUsage's own docstring."""
    unique_visitors: int
    sessions_with_visitor_id: int
    median_session_seconds: float | None
    average_session_seconds: float | None
    median_visitor_total_seconds: float | None
    average_visitor_total_seconds: float | None


class WorldUsageResponse(BaseModel):
    world_key: str
    calls: int
    input_tokens: int
    output_tokens: int
    cache_creation_input_tokens: int
    cache_read_input_tokens: int
    priced_dollars: float
    unpriced_calls: int


class AskCandidateResponse(BaseModel):
    ask: str
    count: int
    session_ids: list[str]


class UsageSummaryResponse(BaseModel):
    """Admin-only, see wiring.get_usage_summary's own docstring - the same
    operator-only tier /api/admin/pilot-summary already lives at, extended
    with the identity/duration/cost/per-world/questions-asked scope."""
    visitors: VisitorUsageResponse
    by_world: list[WorldUsageResponse]
    price_table_source: str | None
    top_asks: list[AskCandidateResponse]
    asks_generated_at: str | None
    asks_as_of_run: str | None


class WorldSummary(BaseModel):
    world_key: str
    census_id: str | None
    display_name: str | None
    # The friendly participant-facing name; display_name is the scholarly
    # one. Both registers are kept.
    card_name: str | None = None
    representative: dict | None
    time_window: dict | None
    place: str | None
    thinness_statement: str | None
    # The participant-facing doorway paragraph (registry-owned, plain
    # English); horizon is the model-facing world_core self-description the
    # doorway used to reuse verbatim, kept as the client-side fallback.
    doorway_description: str | None = None
    horizon: str | None
    living_tradition_flag: bool
    starters: list[dict]


class WorldListResponse(BaseModel):
    worlds: list[WorldSummary]


def _extract_code(authorization: str | None) -> str | None:
    if not authorization or not authorization.startswith(_AUTH_PREFIX):
        return None
    candidate = authorization[len(_AUTH_PREFIX) :].strip()
    return candidate or None


def _authenticate(store: Store, session_id: str, authorization: str | None):
    """Missing session and wrong code return the identical 401 body -
    engine.m4.session_code.codes_match is constant-time, so this reuses an
    already-built guarantee rather than adding new hardening."""
    state = project_fresh(session_id, store)
    candidate = _extract_code(authorization)
    if not state.exists or not candidate or not session_code.codes_match(candidate, state.code_hash):
        raise HTTPException(status_code=401, detail=_INVALID_SESSION_DETAIL)
    return state


_ADMIN_AUTH_PREFIX = "Bearer "


def _authenticate_admin(configured_token: str | None, authorization: str | None, *, session_token: str | None = None) -> None:
    """A separate credential from _authenticate above: that one proves
    'this caller holds THIS session's own code' (a participant, legitimately);
    this one proves 'this caller is an operator,' answering across every
    session at once. Unconfigured, missing, and wrong all return the
    identical 404 - unlike a session id (which a real participant already
    knows exists), this route shouldn't confirm its own existence to
    anyone who lacks the token, config-not-set included.

    session_token: the dashboard's password-login
    cookie (engine.api.admin_auth) is a second, equally valid way in -
    checked first since it's the common case for the browser dashboard,
    falling through to the original Bearer-token check unchanged so a
    direct API caller (a script hitting pilot-summary) is unaffected.
    configured_token doubles as the session-signing secret
    (admin_auth.verify_session_token) - unconfigured admin_token means no
    valid session can exist either, the same single off-switch as
    before."""
    if not configured_token:
        raise HTTPException(status_code=404)
    if session_token and admin_auth.verify_session_token(session_token, configured_token):
        return
    if not authorization or not authorization.startswith(_ADMIN_AUTH_PREFIX):
        raise HTTPException(status_code=404)
    candidate = authorization[len(_ADMIN_AUTH_PREFIX) :].strip()
    if not candidate or not hmac.compare_digest(candidate, configured_token):
        raise HTTPException(status_code=404)


def create_app(
    *,
    voice_client,
    voice_model_id: str,
    safety_client,
    safety_model_id: str,
    store: Store,
    usage_store: UsageLogStore,
    world_loader: LazyWorldLoader,
    registry: dict,
    default_world_key: str,
    enforce_admission: bool = False,
    rate_limit: bool = False,
    admin_token: str | None = None,
    package_cache_dir: Path | None = None,
    anon_cap_enabled: bool = False,
    anon_visitor_secret: str | None = None,
    anon_daily_session_limit: int = anon_cap.DEFAULT_DAILY_SESSION_LIMIT,
    anon_daily_turn_limit: int = anon_cap.DEFAULT_DAILY_TURN_LIMIT,
    r27_enforce: bool = False,
    self_revision_enabled: bool = True,
    citation_attach_enabled: bool = False,
    qc_recorder=None,
    streaming_enabled: bool = False,
    m7_audit_root: Path | None = None,
    admin_auth_store: admin_auth.AdminAuthStore | None = None,
    deeper: deeper_routes.DeeperRuntime | None = None,
) -> FastAPI:
    """All dependencies pre-built and injected - never touches env vars or
    makes a real Bedrock call itself. This is what tests call with fakes.

    rate_limit defaults False so the fake-backed test apps (which fire
    many requests from one TestClient 'IP' in seconds) aren't throttled;
    _build_real_app - the ONLY production constructor - passes True, and
    engine/api/tests/test_ratelimit.py pins that a rate-limited app
    actually limits.

    admin_token defaults None, same disabled-by-default posture: unset in
    a test app (or a real deploy that hasn't configured one yet) means
    /api/admin/pilot-summary 404s outright rather than existing in a
    permanently-unauthorizable state.

    anon_cap_enabled defaults False as a code default (see
    engine.api.anon_cap's own module docstring - both real deploys turn it
    on via render.yaml). Enabling it with
    no secret is refused loudly, not silently skipped - a caller opting in
    without providing the one thing that makes the token unforgeable is a
    misconfiguration, not a valid "off" state."""
    if anon_cap_enabled and not anon_visitor_secret:
        raise MissingAnonCapSecret("CIC_API_ANON_CAP_ENABLED is on but CIC_API_ANON_VISITOR_SECRET is unset")
    app = FastAPI(title="CiC engine/api (minimal test backend)")
    # Registration order matters: Starlette's middleware stack is LIFO
    # (the last one registered ends up outermost and runs first), so
    # anon_cap is installed BEFORE ratelimit here on purpose - the cheap,
    # no-cookie-read burst check stays the actual first line a request
    # meets (see anon_cap.install's own docstring for why that matters -
    # a burst-rejected request should never reach anon_cap's daily-quota
    # accounting at all).
    app.state.deeper = deeper
    if anon_cap_enabled:
        anon_cap.install(
            app, secret=anon_visitor_secret, daily_session_limit=anon_daily_session_limit, daily_turn_limit=anon_daily_turn_limit,
            exempt=(
                (lambda request, is_create: deeper_admission.code_is_usable(deeper, request, strict=is_create))
                if deeper is not None else None
            ),
            session_cap_facilitator_only=deeper is not None,
        )
    if rate_limit:
        ratelimit.install(
            app, bucket_for=(lambda request: deeper_admission.burst_key(deeper, request)) if deeper is not None else None
        )
    app.state.deps = Deps(
        voice_client=voice_client,
        voice_model_id=voice_model_id,
        safety_client=safety_client,
        safety_model_id=safety_model_id,
        store=store,
        usage_store=usage_store,
        world_loader=world_loader,
        registry=registry,
        admin_token=admin_token,
        default_world_key=default_world_key,
        enforce_admission=enforce_admission,
        package_cache_dir=package_cache_dir,
        r27_enforce=r27_enforce,
        self_revision_enabled=self_revision_enabled,
        citation_attach_enabled=citation_attach_enabled,
        qc_recorder=qc_recorder,
        streaming_enabled=streaming_enabled,
        m7_audit_root=m7_audit_root,
        admin_auth_store=admin_auth_store,
    )

    @app.get("/health")
    def health():
        return {"status": "ok"}

    def _note_facilitator_only(request: Request, session_id: str) -> None:
        if deeper is None:
            return
        if getattr(request.state, "facilitator_only_session", False):
            deeper.facilitator_only_sessions.add(session_id)
        if getattr(request.state, "paid_session", False):
            deeper.paid_sessions.add(session_id)

    if deeper is not None:
        def _admin_check(request: Request, authorization: str | None) -> None:
            _authenticate_admin(
                request.app.state.deps.admin_token, authorization,
                session_token=request.cookies.get(admin_auth.SESSION_COOKIE_NAME),
            )

        deeper_routes.install(app, deeper, authenticate_admin=_admin_check)

    @app.get("/api/worlds", response_model=WorldListResponse)
    def list_worlds_endpoint(request: Request):
        deps: Deps = request.app.state.deps
        try:
            worlds = wiring.list_worlds(
                world_loader=deps.world_loader, registry=deps.registry, require_admitted=deps.enforce_admission,
                package_cache_dir=deps.package_cache_dir,
            )
        except PackageRefused:
            raise HTTPException(status_code=503, detail=_WORLD_UNAVAILABLE_DETAIL)
        return WorldListResponse(worlds=worlds)

    @app.post("/api/session", status_code=201, response_model=SessionCreateResponse)
    def create_session_endpoint(req: SessionCreateRequest, request: Request):
        deps: Deps = request.app.state.deps
        # Set only when anon_cap.install's middleware ran (CIC_API_ANON_CAP_ENABLED) -
        # absent otherwise, same as a pre-visitor-cookie session_started event.
        visitor_id = getattr(request.state, "visitor_id", None)
        if req.world_keys is not None:
            if req.world_key is not None:
                raise HTTPException(status_code=400, detail="pass world_key OR world_keys, not both")
            if not (2 <= len(req.world_keys) <= 3) or len(set(req.world_keys)) != len(req.world_keys):
                # Same bound the event schema enforces (Artifact-7 SS1) -
                # refused here too so the client gets a 400, not a 500 from
                # the validation layer.
                raise HTTPException(status_code=400, detail="world_keys must be 2-3 distinct keys")
            try:
                session_id, code = table_wiring.create_table_session(
                    store=deps.store, world_loader=deps.world_loader, registry=deps.registry, world_keys=req.world_keys,
                    require_admitted=deps.enforce_admission, package_cache_dir=deps.package_cache_dir,
                    visitor_id=visitor_id,
                )
            except wiring.UnknownWorldError as exc:
                raise HTTPException(status_code=400, detail=f"unknown world_key {exc.args[0]!r}")
            except wiring.WorldNotAdmitted as exc:
                raise HTTPException(status_code=403, detail=f"world {exc.args[0]!r} has not passed admission")
            except PackageRefused:
                logger.warning("table session refused: package unavailable worlds=%s", req.world_keys)
                raise HTTPException(status_code=503, detail=_WORLD_UNAVAILABLE_DETAIL)
            _note_facilitator_only(request, session_id)
            logger.info("session created session=%s mode=table worlds=%s", session_id, ",".join(req.world_keys))
            return SessionCreateResponse(session_id=session_id, session_code=code, round_cap=table_wiring.round_cap_for("table"))
        if req.world_key is None:
            # POST {} must not fall through to default_world_key -
            # configured in production as the synthetic fixture world,
            # which records/worlds.yaml says must never be
            # participant-reachable ("never listed beside them, never
            # admitted"). A session names its world or doesn't open; the
            # frontend always names one, so no real caller changes.
            raise HTTPException(status_code=400, detail="world_key is required - one world for an interview, or world_keys for a table")
        world_key = req.world_key
        try:
            session_id, code = wiring.create_session(
                store=deps.store, world_loader=deps.world_loader, registry=deps.registry, world_key=world_key,
                require_admitted=deps.enforce_admission, package_cache_dir=deps.package_cache_dir,
                visitor_id=visitor_id,
            )
        except wiring.UnknownWorldError:
            raise HTTPException(status_code=400, detail=f"unknown world_key {world_key!r}")
        except wiring.WorldNotAdmitted as exc:
            raise HTTPException(status_code=403, detail=f"world {exc.args[0]!r} has not passed admission")
        except PackageRefused:
            logger.warning("session refused: package unavailable world=%s", world_key)
            raise HTTPException(status_code=503, detail=_WORLD_UNAVAILABLE_DETAIL)
        _note_facilitator_only(request, session_id)
        logger.info("session created session=%s mode=interview world=%s", session_id, world_key)
        return SessionCreateResponse(session_id=session_id, session_code=code)

    @app.post("/api/session/{session_id}/message", response_model=MessageResponse | TableMessageResponse)
    def send_message(
        session_id: str, req: MessageRequest, request: Request, response: Response, authorization: str | None = Header(default=None)
    ):
        deps: Deps = request.app.state.deps
        state = _authenticate(deps.store, session_id, authorization)
        is_table = state.mode == "table"
        admission = deeper_admission.new_admission(
            deeper, request, session_id=session_id,
            free_cap=round_module.TABLE_SESSION_ROUND_CAP if is_table else turn_module.SESSION_TURN_CAP,
            seats=len(state.world_keys) if is_table else 1,
        )
        call_kwargs = dict(
            store=deps.store,
            usage_store=deps.usage_store,
            world_loader=deps.world_loader,
            registry=deps.registry,
            voice_client=deps.voice_client,
            voice_model_id=deps.voice_model_id,
            safety_client=deps.safety_client,
            safety_model_id=deps.safety_model_id,
            session_id=session_id,
            text=req.text,
            client_msg_id=req.client_msg_id,
            package_cache_dir=deps.package_cache_dir,
            r27_enforce=deps.r27_enforce,
            self_revision_enabled=deps.self_revision_enabled,
            citation_attach_enabled=deps.citation_attach_enabled,
            qc_recorder=deps.qc_recorder,
            daily_turn_cap_reached=getattr(request.state, "daily_turn_cap_reached", False),
            grant_for=admission.provider if admission is not None else None,
        )
        started = time.monotonic()
        if deps.streaming_enabled and "text/event-stream" in request.headers.get("accept", ""):
            def with_balance(done: dict, result) -> dict:
                if admission is not None and admission.remaining is not None:
                    done["remaining"] = admission.remaining
                    if admission.low:
                        done["low"] = True
                if admission is not None:
                    done["limit_note"] = admission.limit_note(result.routing_action)
                return done

            if is_table:
                return _stream_turn(
                    lambda on_sentence: table_wiring.handle_table_message(**call_kwargs, on_sentence=on_sentence),
                    lambda result: with_balance(TableMessageResponse(**asdict(result)).model_dump(), result),
                    lambda result: result.round_open or result.voice is not None,
                    session_id, started, admission,
                )

            return _stream_turn(
                lambda on_sentence: wiring.handle_message(**call_kwargs, on_sentence=on_sentence),
                lambda result: with_balance(MessageResponse(**asdict(result)).model_dump(), result), lambda result: _spoke(result.voice), session_id, started, admission,
            )
        voiced = False
        try:
            if is_table:
                result = table_wiring.handle_table_message(**call_kwargs)
                voiced = result.round_open or result.voice is not None
                logger.info("table message handled ms=%d", (time.monotonic() - started) * 1000)
                return TableMessageResponse(**asdict(result), limit_note=admission.limit_note(result.routing_action) if admission else None)
            result = wiring.handle_message(**call_kwargs)
            voiced = _spoke(result.voice)
        except Exception as exc:
            failure = _message_failure(exc, session_id)
            if failure is None:
                raise
            raise failure
        finally:
            if admission is not None:
                remaining = admission.finish(voiced)
                if remaining is not None:
                    response.headers[deeper_admission.REMAINING_HEADER] = str(remaining)
                    if admission.low:
                        response.headers[deeper_admission.LOW_HEADER] = "1"
        logger.info("message handled ms=%d", (time.monotonic() - started) * 1000)
        return MessageResponse(**asdict(result), limit_note=admission.limit_note(result.routing_action) if admission else None)

    @app.post("/api/session/{session_id}/continue", response_model=TableMessageResponse)
    def continue_round(session_id: str, request: Request, authorization: str | None = Header(default=None)):
        """Advance the open table round by one voice turn, or report its
        close (Artifact-7 SS6). 409 when no round is open - including on an
        interview session, which never has one."""
        deps: Deps = request.app.state.deps
        _authenticate(deps.store, session_id, authorization)
        continue_kwargs = dict(
            store=deps.store, usage_store=deps.usage_store, world_loader=deps.world_loader, registry=deps.registry,
            voice_client=deps.voice_client, voice_model_id=deps.voice_model_id,
            safety_client=deps.safety_client, safety_model_id=deps.safety_model_id,
            session_id=session_id, package_cache_dir=deps.package_cache_dir, r27_enforce=deps.r27_enforce,
            self_revision_enabled=deps.self_revision_enabled, citation_attach_enabled=deps.citation_attach_enabled,
            qc_recorder=deps.qc_recorder,
        )
        if deps.streaming_enabled and "text/event-stream" in request.headers.get("accept", ""):
            return _stream_turn(
                lambda on_sentence: table_wiring.continue_table_round(**continue_kwargs, on_sentence=on_sentence),
                lambda result: TableMessageResponse(**asdict(result)).model_dump(),
                lambda result: result.voice is not None, session_id, time.monotonic(),
            )
        try:
            result = table_wiring.continue_table_round(**continue_kwargs)
        except Exception as exc:
            failure = _message_failure(exc, session_id)
            if failure is None:
                raise
            raise failure from exc
        return TableMessageResponse(**asdict(result))

    @app.get("/api/session/{session_id}/transcript", response_model=TranscriptResponse)
    def get_transcript_endpoint(session_id: str, request: Request, authorization: str | None = Header(default=None)):
        deps: Deps = request.app.state.deps
        _authenticate(deps.store, session_id, authorization)
        state = wiring.get_transcript(deps.store, session_id)
        return TranscriptResponse(
            session_id=session_id, world_key=state.world_key, turn_count=state.turn_count, closed=state.closed, transcript=state.transcript,
            mode=state.mode, world_keys=state.world_keys, round_open=state.round_open,
            round_cap=table_wiring.round_cap_for(state.mode),
        )

    @app.delete("/api/session/{session_id}", status_code=204)
    def delete_session_endpoint(session_id: str, request: Request, authorization: str | None = Header(default=None)):
        """A participant's deletion request, authorised by the session's own
        code: the conversation leaves the event log and the M7 audit files
        now, and the daily backups within their 14-day rotation. The
        anonymous quality-control store holds nothing that links to it."""
        deps: Deps = request.app.state.deps
        _authenticate(deps.store, session_id, authorization)
        events_deleted = deps.store.delete_session(session_id)
        audit_files = erase.erase_session(deps.m7_audit_root, session_id) if deps.m7_audit_root else 0
        logger.info("session deleted session=%s events=%d audit_files=%d", session_id, events_deleted, audit_files)
        return Response(status_code=204)

    @app.get("/api/session/{session_id}/round-close-reasons", response_model=RoundCloseReasonsResponse)
    def get_round_close_reasons_endpoint(session_id: str, request: Request, authorization: str | None = Header(default=None)):
        """Diagnostic-only: gated by the same per-session code as the
        transcript endpoint above, never a new auth surface. A real
        production round's close reason - including the turn selector's
        own free-text justification on a genuine close - is answerable
        without a direct read against the store."""
        deps: Deps = request.app.state.deps
        _authenticate(deps.store, session_id, authorization)
        rounds = table_wiring.get_round_close_reasons(deps.store, session_id)
        return RoundCloseReasonsResponse(session_id=session_id, rounds=rounds)

    @app.get("/api/admin/pilot-summary", response_model=PilotSummaryResponse)
    def get_pilot_summary_endpoint(
        request: Request, authorization: str | None = Header(default=None), since: str | None = None
    ):
        """Operator-only: answers 'how many real pilot sessions exist' and
        'is the table round cap firing where it should' from outside the
        service. `since` is the same ISO-8601 prefix filter
        Store.list_session_ids already defines - unset means every
        session ever logged."""
        deps: Deps = request.app.state.deps
        _authenticate_admin(deps.admin_token, authorization, session_token=request.cookies.get(admin_auth.SESSION_COOKIE_NAME))
        summary = wiring.get_pilot_summary(deps.store, since=since)
        return PilotSummaryResponse(**asdict(summary))

    @app.get("/api/admin/usage-summary", response_model=UsageSummaryResponse)
    def get_usage_summary_endpoint(
        request: Request, authorization: str | None = Header(default=None), since: str | None = None
    ):
        """Operator-only, same gate as pilot-summary above: unique
        visitors, duration, cost/tokens, per-world breakdown, and the
        latest questions-asked rollup - see wiring.get_usage_summary's own
        docstring for exactly what each covers and the one disclosed scope
        gap (cost/per-world doesn't respect `since` yet)."""
        deps: Deps = request.app.state.deps
        _authenticate_admin(deps.admin_token, authorization, session_token=request.cookies.get(admin_auth.SESSION_COOKIE_NAME))
        summary = wiring.get_usage_summary(deps.store, deps.usage_store, since=since, m7_audit_root=deps.m7_audit_root)
        return UsageSummaryResponse(**asdict(summary))

    @app.get("/api/admin/auth-status", response_model=AdminAuthStatusResponse)
    def get_admin_auth_status(request: Request):
        """Unauthenticated on purpose - the dashboard calls this BEFORE it
        has any credential at all, to decide which form to show: 'set up
        your password' (password_set: false) or 'log in' (true). Reveals
        only a boolean, never whether admin_token itself is configured -
        that stays 404-everywhere like every other /api/admin/* route
        when it's unset, via the same admin_auth_store being None."""
        deps: Deps = request.app.state.deps
        if deps.admin_auth_store is None:
            raise HTTPException(status_code=404)
        return AdminAuthStatusResponse(password_set=deps.admin_auth_store.read_password_hash() is not None)

    @app.post("/api/admin/set-password", status_code=204)
    def set_admin_password(req: AdminSetPasswordRequest, request: Request, authorization: str | None = Header(default=None)):
        """Bootstraps or changes the dashboard's password - gated on the
        ORIGINAL admin_token (Bearer), never a session, since this is the
        one action that creates the credential a session would otherwise
        prove. The raw token from Render is needed here exactly once (or
        again, to change the password later), never afterward for ordinary
        dashboard use."""
        deps: Deps = request.app.state.deps
        _authenticate_admin(deps.admin_token, authorization)
        if deps.admin_auth_store is None:
            raise HTTPException(status_code=404)
        try:
            admin_auth.validate_password_policy(req.password)
        except admin_auth.PasswordPolicyError as exc:
            raise HTTPException(status_code=400, detail=str(exc))
        deps.admin_auth_store.write_password_hash(admin_auth.hash_password(req.password))

    @app.post("/api/admin/login")
    def admin_login(req: AdminLoginRequest, request: Request):
        """Rate-limited to 5 attempts/15min per IP (engine.api.ratelimit.
        ADMIN_LOGIN_LIMIT) - that lockout, not the password's own length,
        is what makes a 12-20 character password (engine.api.admin_auth.
        PASSWORD_MIN_LENGTH/MAX_LENGTH) safe here. Wrong password and
        no-password-set-yet return the identical 401 - the dashboard asks
        auth-status separately to tell those apart, this route never
        leaks it on a failed attempt."""
        deps: Deps = request.app.state.deps
        if deps.admin_auth_store is None:
            raise HTTPException(status_code=404)
        stored_hash = deps.admin_auth_store.read_password_hash()
        if not stored_hash or not admin_auth.verify_password(req.password, stored_hash):
            raise HTTPException(status_code=401, detail="incorrect password")
        token = admin_auth.issue_session_token(deps.admin_token)
        response = JSONResponse({"status": "ok"})
        response.set_cookie(
            admin_auth.SESSION_COOKIE_NAME, token, max_age=admin_auth.DEFAULT_SESSION_TTL_SECONDS,
            httponly=True, samesite="lax", secure=True, path="/api/admin",
        )
        return response

    @app.post("/api/admin/logout")
    def admin_logout():
        response = JSONResponse({"status": "ok"})
        response.delete_cookie(admin_auth.SESSION_COOKIE_NAME, path="/api/admin")
        return response

    _ADMIN_DASHBOARD_PATH = Path(__file__).resolve().parent / "static" / "admin_dashboard.html"

    @app.get("/admin/dashboard", include_in_schema=False)
    def get_admin_dashboard():
        """The visual half of the usage dashboard - a static page,
        unauthenticated to SERVE (same posture as cic-poc/frontend below:
        no page here carries data of its own), that logs in with a
        password (engine.api.admin_auth) and calls
        /api/admin/usage-summary + /api/admin/pilot-summary with the
        resulting session cookie. Registered BEFORE the SPA catch-all below so it isn't swallowed by
        that route's index.html fallback."""
        return FileResponse(_ADMIN_DASHBOARD_PATH)

    # Stage 5 (PHASE-1-LAUNCH.md): one Render service, not two - same
    # pattern cic-poc/backend/app/main.py already used, so no CORS_ORIGINS
    # config and no second thing to deploy and keep in sync. `/api/*` and
    # `/health` above are matched first (FastAPI resolves routes in
    # registration order); everything else falls through to here. Guarded
    # on the dist/ directory existing so local backend-only dev (no built
    # frontend) is unaffected - this is why engine/api's own test suite
    # never sees this route.
    _frontend_dist = REPO_ROOT / "cic-poc" / "frontend" / "dist"
    if _frontend_dist.is_dir():
        app.mount("/assets", StaticFiles(directory=_frontend_dist / "assets"), name="frontend-assets")

        @app.get("/{full_path:path}")
        async def serve_frontend(full_path: str):
            """SPA catch-all: serves a same-named static file at the dist
            root (favicon, manifest icons, ...) or falls back to
            index.html. full_path is attacker-controlled (the literal rest
            of the URL via Starlette's `path` converter, which does not
            strip `..`) - resolving the candidate and requiring it stay
            under _frontend_dist closes the path-traversal this exact join
            pattern opened in cic-poc's own backend before that fix."""
            candidate = (_frontend_dist / full_path).resolve()
            if full_path and candidate.is_relative_to(_frontend_dist) and candidate.is_file():
                return FileResponse(candidate)
            return FileResponse(_frontend_dist / "index.html")

    return app


def _build_real_app() -> FastAPI:
    from engine.provider.bedrock import make_client, resolve_model_id

    # Make the module logger actually emit under uvicorn: uvicorn
    # configures its own loggers only, so without a root handler the
    # "cic.api" records vanish. basicConfig is a no-op if a root handler
    # already exists (e.g. a future log-shipping setup), so this never
    # double-configures.
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s %(message)s")

    settings = Settings.from_env()
    voice_model_id = resolve_model_id(settings.voice_model_pattern, settings.region)
    safety_model_id = resolve_model_id(settings.safety_model_pattern, settings.region)
    client = make_client(settings.region)  # ONE client, reused for both roles - matches live_turn_run.py
    store = Store(settings.events_db_path)
    usage_store = UsageLogStore(settings.usage_db_path)
    full_registry = load_registry(settings.worlds_yaml_path)

    # M7's conversation-quality audit existed but depended on someone
    # remembering to run it by hand. Started here, not as a separate
    # Render service: a Cron Job service can't share this service's
    # already-attached Persistent Disk. Read-only over the event log, so a
    # bad run can never affect a live conversation.
    m7_scheduler.start_background_scheduler(
        settings.events_db_path, Path(settings.events_db_path).parent / "m7-audits"
    )

    # Idle-close sweep: a separate daily background thread, deliberately
    # not folded into M7's own scheduler above - M7 is read-only over the
    # event log by design, and this sweep's whole job is to write
    # session_closed/reason="idle" (engine.m4.idle_close's own docstring).
    # Reporting-only: never blocks a participant resuming.
    idle_close.start_background_scheduler(settings.events_db_path)

    # DB backup sweep: a third daily background thread, same reason as the
    # two above - a Cron Job service cannot reach this service's own
    # Persistent Disk (module docstring, engine/api/db_backup.py).
    # Online-backs-up both SQLite stores and uploads to
    # CIC_API_BACKUP_BUCKET when configured; a no-op upload (logged, not
    # fatal) until that bucket is configured (setup steps in
    # Build/Ministry/Operations/Standing/CiC_Backup_Restore_Runbook.md),
    # same deferred-until-configured pattern as CIC_API_PACKAGE_BUCKET.
    data_dir = Path(settings.events_db_path).parent
    deeper_config = DeeperConfig.from_env(str(data_dir))
    deeper_runtime = None
    if deeper_config.enabled:
        deeper_runtime = deeper_routes.build_runtime(deeper_config, dict(os.environ))
        deeper_routes.install_access_log_filter()
        deeper_routes.start_retention_thread(deeper_runtime)
    db_backup.start_background_scheduler(
        settings.events_db_path, settings.usage_db_path, data_dir / "backups-staging",
        qc_db_path=settings.qc_db_path,
        extra_dbs={"meter": deeper_config.meter_db_path} if deeper_runtime is not None else None,
    )

    # The anonymous quality-control store and the daily retention job
    # (System Hub decision 34): conversations inactive for 90 days leave
    # the event log; QC answer text older than 90 days is deleted.
    qc_recorder = QCRecorder(QCStore(settings.qc_db_path), full_registry)
    retention.start_background_scheduler(
        settings.events_db_path, settings.qc_db_path, Path(settings.events_db_path).parent / "retention",
        audit_root=Path(settings.events_db_path).parent / "m7-audits",
    )

    return create_app(
        voice_client=client,
        voice_model_id=voice_model_id,
        safety_client=client,
        safety_model_id=safety_model_id,
        store=store,
        usage_store=usage_store,
        world_loader=LazyWorldLoader(max_idle_seconds=settings.world_idle_unload_seconds),
        registry=full_registry,
        default_world_key=settings.default_world_key,
        enforce_admission=settings.enforce_admission,
        rate_limit=True,
        admin_token=settings.admin_token,
        package_cache_dir=settings.package_cache_dir,
        anon_cap_enabled=settings.anon_cap_enabled,
        anon_visitor_secret=settings.anon_visitor_secret,
        anon_daily_session_limit=settings.anon_daily_session_limit,
        anon_daily_turn_limit=settings.anon_daily_turn_limit,
        r27_enforce=settings.r27_enforce,
        self_revision_enabled=settings.self_revision_enabled,
        citation_attach_enabled=settings.citation_attach_enabled,
        qc_recorder=qc_recorder,
        streaming_enabled=settings.streaming_enabled,
        deeper=deeper_runtime,
        # Same path m7_scheduler.start_background_scheduler was already
        # given above - one directory, two readers (the daily job writes
        # it, the usage-summary endpoint reads it).
        m7_audit_root=Path(settings.events_db_path).parent / "m7-audits",
        # Same persistent disk as events.db/usage.db/m7-audits above - one
        # small file, only ever constructed when admin_token itself is
        # set (None otherwise disables the whole password-login feature,
        # same posture admin_token's own absence already gives every
        # other /api/admin/* route).
        admin_auth_store=(
            admin_auth.AdminAuthStore(Path(settings.events_db_path).parent / "admin_auth.json")
            if settings.admin_token else None
        ),
    )


# Only built when CIC_API_REGION is actually set - importing this module
# under pytest (CIC_API_REGION unset in CI) leaves `app = None` rather than
# resolving model IDs or making a real, credentialed Bedrock call at import
# time. `uvicorn engine.api.app:app` sets the env var first, so the real
# server still gets a real app.
app = _build_real_app() if os.environ.get("CIC_API_REGION") else None
