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
import logging
import os
import time
from dataclasses import asdict, dataclass
from pathlib import Path

from fastapi import FastAPI, Header, HTTPException, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from engine.api import anon_cap, db_backup, ratelimit, table_wiring, wiring
from engine.api.config import REPO_ROOT, Settings
from engine.m1.registry import load_registry
from engine.m4 import idle_close, session_code
from engine.m4.projection import project_fresh
from engine.m4.store import Store
from engine.m4.world_loader import LazyWorldLoader, PackageRefused
from engine.m7 import scheduler as m7_scheduler
from engine.m8.log_store import UsageLogStore

class MissingAnonCapSecret(Exception):
    """Raised at app construction when anon_cap_enabled=True but no secret
    was given - same "never guess, fail loudly" posture as MissingConfigError
    in engine.api.config for region."""


_INVALID_SESSION_DETAIL = "invalid session"
_WORLD_UNAVAILABLE_DETAIL = "world temporarily unavailable"
_AUTH_PREFIX = "Session "

# The service's one logger (2026-08-28 foundation audit: the service had
# ZERO logging, and the one place the real Bedrock error was captured it
# was discarded unbound - a throttling storm was indistinguishable from a
# credential failure). Session ids are logged; participant text and voice
# text never are.
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


_MAX_MESSAGE_LENGTH = 4000  # ~800-1000 words - generous for a real participant turn, bounded against a payload attack


class MessageRequest(BaseModel):
    # 2026-09-21, closing adversarial review of Tech-Readiness P1-Security:
    # unbounded before this. Nothing anywhere in the request path - not
    # this model, not engine/m4/turn.py, not the Dockerfile - capped
    # participant input length; every message is forwarded to Bedrock
    # TWICE per turn (the safety gate, then voice generation) and stored
    # verbatim, at up to 40 messages/min per IP. Output was already
    # bounded (max_tokens on the generation call); input wasn't - textbook
    # OWASP LLM Top 10 "unbounded consumption," and cheaper for an
    # attacker to hit than the session-creation path this package's own
    # anonymous-cap work (item 3) addresses.
    text: str = Field(max_length=_MAX_MESSAGE_LENGTH)
    client_msg_id: str | None = None


class MessageResponse(BaseModel):
    turn_no: int
    routing_action: str | None
    routing_reason: str
    degraded: bool
    facilitator: dict | None
    voice: dict | None


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
    """Diagnostic-only, table sessions (2026-09-05): every round_closed
    event's own payload for this session, in round order. Empty for an
    interview session or a table session with no round closed yet."""
    session_id: str
    rounds: list[dict]


class PilotSummaryResponse(BaseModel):
    """Admin-only (2026-09-05), see wiring.PilotSummary's own docstring for
    what this deliberately does and doesn't carry."""
    total_sessions: int
    by_mode: dict[str, int]
    open_sessions: int
    closed_by_reason: dict[str, int]
    table_round_counts_on_cap: dict[str, int]
    earliest_session_at: str | None
    latest_session_at: str | None


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


def _authenticate_admin(configured_token: str | None, authorization: str | None) -> None:
    """A separate credential from _authenticate above: that one proves
    'this caller holds THIS session's own code' (a participant, legitimately);
    this one proves 'this caller is an operator,' answering across every
    session at once. Unconfigured, missing, and wrong all return the
    identical 404 - unlike a session id (which a real participant already
    knows exists), this route shouldn't confirm its own existence to
    anyone who lacks the token, config-not-set included."""
    if not configured_token or not authorization or not authorization.startswith(_ADMIN_AUTH_PREFIX):
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

    anon_cap_enabled defaults False, same posture again (see
    engine.api.anon_cap's own module docstring for what this is and why
    it's proposed, not decided, even once code-complete). Enabling it with
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
    if anon_cap_enabled:
        anon_cap.install(
            app, secret=anon_visitor_secret, daily_session_limit=anon_daily_session_limit, daily_turn_limit=anon_daily_turn_limit,
        )
    if rate_limit:
        ratelimit.install(app)
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
    )

    @app.get("/health")
    def health():
        return {"status": "ok"}

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
                )
            except wiring.UnknownWorldError as exc:
                raise HTTPException(status_code=400, detail=f"unknown world_key {exc.args[0]!r}")
            except wiring.WorldNotAdmitted as exc:
                raise HTTPException(status_code=403, detail=f"world {exc.args[0]!r} has not passed admission")
            except PackageRefused:
                logger.warning("table session refused: package unavailable worlds=%s", req.world_keys)
                raise HTTPException(status_code=503, detail=_WORLD_UNAVAILABLE_DETAIL)
            logger.info("session created session=%s mode=table worlds=%s", session_id, ",".join(req.world_keys))
            return SessionCreateResponse(session_id=session_id, session_code=code, round_cap=table_wiring.round_cap_for("table"))
        if req.world_key is None:
            # Foundation audit (2026-08-28): POST {} used to fall through to
            # default_world_key - configured in production as the synthetic
            # fixture world, which records/worlds.yaml says must never be
            # participant-reachable ("never listed beside them, never
            # admitted"). A session names its world or doesn't open; the
            # frontend always names one, so no real caller changes.
            raise HTTPException(status_code=400, detail="world_key is required - one world for an interview, or world_keys for a table")
        world_key = req.world_key
        try:
            session_id, code = wiring.create_session(
                store=deps.store, world_loader=deps.world_loader, registry=deps.registry, world_key=world_key,
                require_admitted=deps.enforce_admission, package_cache_dir=deps.package_cache_dir,
            )
        except wiring.UnknownWorldError:
            raise HTTPException(status_code=400, detail=f"unknown world_key {world_key!r}")
        except wiring.WorldNotAdmitted as exc:
            raise HTTPException(status_code=403, detail=f"world {exc.args[0]!r} has not passed admission")
        except PackageRefused:
            logger.warning("session refused: package unavailable world=%s", world_key)
            raise HTTPException(status_code=503, detail=_WORLD_UNAVAILABLE_DETAIL)
        logger.info("session created session=%s mode=interview world=%s", session_id, world_key)
        return SessionCreateResponse(session_id=session_id, session_code=code)

    @app.post("/api/session/{session_id}/message", response_model=MessageResponse | TableMessageResponse)
    def send_message(session_id: str, req: MessageRequest, request: Request, authorization: str | None = Header(default=None)):
        deps: Deps = request.app.state.deps
        state = _authenticate(deps.store, session_id, authorization)
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
        )
        started = time.monotonic()
        try:
            if state.mode == "table":
                result = table_wiring.handle_table_message(**call_kwargs)
                logger.info("table message handled session=%s round=%s ms=%d", session_id, result.round_no, (time.monotonic() - started) * 1000)
                return TableMessageResponse(**asdict(result))
            result = wiring.handle_message(**call_kwargs)
        except wiring.SessionNotFound:
            raise HTTPException(status_code=401, detail=_INVALID_SESSION_DETAIL)
        except wiring.SessionClosed:
            raise HTTPException(status_code=409, detail="session already closed")
        except table_wiring.TableRoundStillOpen:
            raise HTTPException(status_code=409, detail="round still open - continue it before the next message")
        except table_wiring.TableAdvanceInFlight:
            raise HTTPException(status_code=409, detail="advance already in flight - the table is already speaking")
        except wiring.DuplicateMessage:
            raise HTTPException(status_code=409, detail="duplicate message - already received")
        except PackageRefused:
            logger.warning("message refused: package unavailable session=%s", session_id)
            raise HTTPException(status_code=503, detail=_WORLD_UNAVAILABLE_DETAIL)
        except wiring.ProviderCallFailed as exc:
            # The bound exception carries the real Bedrock error - the one
            # signal that tells throttling apart from credentials apart
            # from a bug. The audit found it constructed and discarded.
            logger.error("provider call failed session=%s: %s", session_id, exc)
            raise HTTPException(status_code=502, detail="provider call failed")
        logger.info("message handled session=%s turn=%s ms=%d", session_id, result.turn_no, (time.monotonic() - started) * 1000)
        return MessageResponse(**asdict(result))

    @app.post("/api/session/{session_id}/continue", response_model=TableMessageResponse)
    def continue_round(session_id: str, request: Request, authorization: str | None = Header(default=None)):
        """Advance the open table round by one voice turn, or report its
        close (Artifact-7 SS6). 409 when no round is open - including on an
        interview session, which never has one."""
        deps: Deps = request.app.state.deps
        _authenticate(deps.store, session_id, authorization)
        try:
            result = table_wiring.continue_table_round(
                store=deps.store,
                usage_store=deps.usage_store,
                world_loader=deps.world_loader,
                registry=deps.registry,
                voice_client=deps.voice_client,
                voice_model_id=deps.voice_model_id,
                safety_client=deps.safety_client,
                safety_model_id=deps.safety_model_id,
                session_id=session_id,
                package_cache_dir=deps.package_cache_dir,
            )
        except wiring.SessionNotFound:
            raise HTTPException(status_code=401, detail=_INVALID_SESSION_DETAIL)
        except wiring.SessionClosed:
            raise HTTPException(status_code=409, detail="session already closed")
        except table_wiring.TableRoundNotOpen:
            raise HTTPException(status_code=409, detail="no open round to continue")
        except table_wiring.TableAdvanceInFlight:
            raise HTTPException(status_code=409, detail="advance already in flight - the table is already speaking")
        except PackageRefused:
            logger.warning("continue refused: package unavailable session=%s", session_id)
            raise HTTPException(status_code=503, detail=_WORLD_UNAVAILABLE_DETAIL)
        except wiring.ProviderCallFailed as exc:
            logger.error("provider call failed session=%s (continue): %s", session_id, exc)
            raise HTTPException(status_code=502, detail="provider call failed")
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

    @app.get("/api/session/{session_id}/round-close-reasons", response_model=RoundCloseReasonsResponse)
    def get_round_close_reasons_endpoint(session_id: str, request: Request, authorization: str | None = Header(default=None)):
        """Diagnostic-only: gated by the same per-session code as the
        transcript endpoint above, never a new auth surface. Built
        2026-09-05 so a real production round's close reason - including
        the turn selector's own free-text justification on a genuine
        close - is answerable without a direct read against the store."""
        deps: Deps = request.app.state.deps
        _authenticate(deps.store, session_id, authorization)
        rounds = table_wiring.get_round_close_reasons(deps.store, session_id)
        return RoundCloseReasonsResponse(session_id=session_id, rounds=rounds)

    @app.get("/api/admin/pilot-summary", response_model=PilotSummaryResponse)
    def get_pilot_summary_endpoint(
        request: Request, authorization: str | None = Header(default=None), since: str | None = None
    ):
        """Operator-only (2026-09-05: no way to answer 'how many real
        pilot sessions exist' or 'is the table round cap firing where it
        should' from outside the service). `since` is the same ISO-8601
        prefix filter Store.list_session_ids already defines - unset means
        every session ever logged."""
        deps: Deps = request.app.state.deps
        _authenticate_admin(deps.admin_token, authorization)
        summary = wiring.get_pilot_summary(deps.store, since=since)
        return PilotSummaryResponse(**asdict(summary))

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
    # remembering to run it by hand - the one real gap in an otherwise-live
    # pilot data pipeline (System Health thread, 2026-09-04). Started here,
    # not as a separate Render service: a Cron Job service can't share this
    # service's already-attached Persistent Disk. Read-only over the event
    # log, so a bad run can never affect a live conversation.
    m7_scheduler.start_background_scheduler(
        settings.events_db_path, Path(settings.events_db_path).parent / "m7-audits"
    )

    # Idle-close sweep (2026-09-06): a separate daily background thread,
    # deliberately not folded into M7's own scheduler above - M7 is
    # read-only over the event log by design, and this sweep's whole job
    # is to write session_closed/reason="idle" (engine.m4.idle_close's own
    # docstring). Reporting-only: never blocks a participant resuming.
    idle_close.start_background_scheduler(settings.events_db_path)

    # DB backup sweep (Tech-Readiness Package 2, 2026-09-21): a third
    # daily background thread, same reason as the two above - a Cron Job
    # service cannot reach this service's own Persistent Disk (module
    # docstring, engine/api/db_backup.py). Online-backs-up both SQLite
    # stores and uploads to CIC_API_BACKUP_BUCKET when configured; a no-op
    # upload (logged, not fatal) until Mark completes that bucket's own
    # one-time setup (Ministry/Operations/Standing/
    # CiC_Backup_Restore_Runbook.md), same deferred-until-configured
    # pattern as CIC_API_PACKAGE_BUCKET.
    db_backup.start_background_scheduler(
        settings.events_db_path, settings.usage_db_path, Path(settings.events_db_path).parent / "backups-staging"
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
    )


# Only built when CIC_API_REGION is actually set - importing this module
# under pytest (CIC_API_REGION unset in CI) leaves `app = None` rather than
# resolving model IDs or making a real, credentialed Bedrock call at import
# time. `uvicorn engine.api.app:app` sets the env var first, so the real
# server still gets a real app.
app = _build_real_app() if os.environ.get("CIC_API_REGION") else None
