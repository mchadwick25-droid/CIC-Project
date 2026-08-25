"""FastAPI shape only (see /root/.claude/plans/linear-popping-dawn.md) - HTTP
parsing, headers, status codes. All business logic lives in engine.api.wiring;
this module never touches the M4/M5 pipeline directly.

`app` (module level) is what `uvicorn engine.api.app:app` serves. It is only
built when CIC_API_REGION is actually set in the environment - importing this
module under pytest (CIC_API_REGION unset in CI) leaves `app = None` rather
than trying to resolve model IDs or make a real, credentialed Bedrock client.
Tests import `create_app` directly and build their own app from fakes.
"""
import os
from dataclasses import asdict, dataclass

import yaml
from fastapi import FastAPI, Header, HTTPException, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from engine.api import wiring
from engine.api.config import REPO_ROOT, Settings
from engine.m4 import session_code
from engine.m4.projection import project_fresh
from engine.m4.store import Store
from engine.m4.world_loader import LazyWorldLoader, PackageRefused
from engine.m8.log_store import UsageLogStore

_INVALID_SESSION_DETAIL = "invalid session"
_WORLD_UNAVAILABLE_DETAIL = "world temporarily unavailable"
_AUTH_PREFIX = "Session "


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


class SessionCreateRequest(BaseModel):
    world_key: str | None = None


class SessionCreateResponse(BaseModel):
    session_id: str
    session_code: str


class MessageRequest(BaseModel):
    text: str
    client_msg_id: str | None = None


class MessageResponse(BaseModel):
    turn_no: int
    routing_action: str | None
    routing_reason: str
    degraded: bool
    facilitator: dict | None
    voice: dict | None


class TranscriptResponse(BaseModel):
    session_id: str
    world_key: str | None
    turn_count: int
    closed: bool
    transcript: list[dict]


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
) -> FastAPI:
    """All dependencies pre-built and injected - never touches env vars or
    makes a real Bedrock call itself. This is what tests call with fakes."""
    app = FastAPI(title="CiC engine/api (minimal test backend)")
    app.state.deps = Deps(
        voice_client=voice_client,
        voice_model_id=voice_model_id,
        safety_client=safety_client,
        safety_model_id=safety_model_id,
        store=store,
        usage_store=usage_store,
        world_loader=world_loader,
        registry=registry,
        default_world_key=default_world_key,
    )

    @app.get("/health")
    def health():
        return {"status": "ok"}

    @app.post("/api/session", status_code=201, response_model=SessionCreateResponse)
    def create_session_endpoint(req: SessionCreateRequest, request: Request):
        deps: Deps = request.app.state.deps
        world_key = req.world_key or deps.default_world_key
        try:
            session_id, code = wiring.create_session(
                store=deps.store, world_loader=deps.world_loader, registry=deps.registry, world_key=world_key
            )
        except wiring.UnknownWorldError:
            raise HTTPException(status_code=400, detail=f"unknown world_key {world_key!r}")
        except PackageRefused:
            raise HTTPException(status_code=503, detail=_WORLD_UNAVAILABLE_DETAIL)
        return SessionCreateResponse(session_id=session_id, session_code=code)

    @app.post("/api/session/{session_id}/message", response_model=MessageResponse)
    def send_message(session_id: str, req: MessageRequest, request: Request, authorization: str | None = Header(default=None)):
        deps: Deps = request.app.state.deps
        _authenticate(deps.store, session_id, authorization)
        try:
            result = wiring.handle_message(
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
            )
        except wiring.SessionNotFound:
            raise HTTPException(status_code=401, detail=_INVALID_SESSION_DETAIL)
        except wiring.SessionClosed:
            raise HTTPException(status_code=409, detail="session already closed")
        except PackageRefused:
            raise HTTPException(status_code=503, detail=_WORLD_UNAVAILABLE_DETAIL)
        except wiring.ProviderCallFailed:
            raise HTTPException(status_code=502, detail="provider call failed")
        return MessageResponse(**asdict(result))

    @app.get("/api/session/{session_id}/transcript", response_model=TranscriptResponse)
    def get_transcript_endpoint(session_id: str, request: Request, authorization: str | None = Header(default=None)):
        deps: Deps = request.app.state.deps
        _authenticate(deps.store, session_id, authorization)
        state = wiring.get_transcript(deps.store, session_id)
        return TranscriptResponse(
            session_id=session_id, world_key=state.world_key, turn_count=state.turn_count, closed=state.closed, transcript=state.transcript
        )

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

    settings = Settings.from_env()
    voice_model_id = resolve_model_id(settings.voice_model_pattern, settings.region)
    safety_model_id = resolve_model_id(settings.safety_model_pattern, settings.region)
    client = make_client(settings.region)  # ONE client, reused for both roles - matches live_turn_run.py
    store = Store(settings.events_db_path)
    usage_store = UsageLogStore(settings.usage_db_path)
    full_registry = yaml.safe_load(settings.worlds_yaml_path.read_text(encoding="utf-8"))
    return create_app(
        voice_client=client,
        voice_model_id=voice_model_id,
        safety_client=client,
        safety_model_id=safety_model_id,
        store=store,
        usage_store=usage_store,
        world_loader=LazyWorldLoader(),
        registry=full_registry["worlds"],
        default_world_key=settings.default_world_key,
    )


# Only built when CIC_API_REGION is actually set - importing this module
# under pytest (CIC_API_REGION unset in CI) leaves `app = None` rather than
# resolving model IDs or making a real, credentialed Bedrock call at import
# time. `uvicorn engine.api.app:app` sets the env var first, so the real
# server still gets a real app.
app = _build_real_app() if os.environ.get("CIC_API_REGION") else None
