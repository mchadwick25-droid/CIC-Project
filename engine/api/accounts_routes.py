"""The HTTP edge of accounts: sign-in by a typed emailed code, the session
cookie, step-up, the recovery code, address change, export and deletion.

Mounted only when CIC_ACCOUNTS_ENABLED is on (engine.api.app.create_app is
handed an AccountsRuntime, or none). With the flag off no path under
/api/accounts exists, no file is opened and no thread starts. The conversation
engine never sees any of this.

Every POST must be JSON, carry the x-cic-accounts header, and, if it has an
Origin, come from the host it is sent to. The session cookie is HTTP-only and
same-site, and holds a token that points to a server-side session. A wrong or
missing code is answered after a fixed delay. Nothing here logs an address, a
code or a request body.
"""
import asyncio
import logging
import threading
import time
from dataclasses import dataclass
from typing import Callable
from urllib.parse import urlsplit

from fastapi import FastAPI, HTTPException, Request, Response
from pydantic import BaseModel, Field
from starlette.concurrency import run_in_threadpool

from engine.accounts.config import AccountsConfig
from engine.accounts.keys import AccountsKeyError, KeyRing, parse_previous
from engine.accounts.service import AccountsService, Mailer, Result, Session
from engine.accounts.store import AccountStore
from engine.api.ratelimit import client_ip, network_of

logger = logging.getLogger("cic.accounts")

PROTECTED_LOG_PREFIXES = ("/api/accounts",)
CSRF_HEADER = "x-cic-accounts"
COOKIE_NAME = "__Host-cic_account"
COOKIE_NAME_INSECURE = "cic_account"
MISS_DELAY_SECONDS = 0.5
START_FLOOR_SECONDS = 0.3

MESSAGES = {
    "sent": "If that address can receive mail, a code is on its way. It works for ten minutes.",
    "invalid_address": "That does not look like an email address.",
    "throttled": "Too many tries just now. Please wait a little and try again.",
    "paused": "Sign-in is paused for a moment. Please try again later.",
    "send_failed": "We could not send the code. Please try again.",
    "wrong": "That code did not work. Check it, or ask for a new one.",
    "needs_birth_year": "Please tell us your year of birth.",
    "invalid_birth_year": "Please enter a four-digit year of birth.",
    "under_age": "You need to be 16 or over to open an account.",
    "step_up_needed": "Please confirm your address with a fresh code first.",
    "cannot_use": "That address cannot be used.",
}


class AccountsConfigError(Exception):
    """A misconfiguration found at startup, never papered over."""


@dataclass
class AccountsRuntime:
    service: AccountsService
    secure_cookie: bool = True
    miss_delay_seconds: float = MISS_DELAY_SECONDS
    start_floor_seconds: float = START_FLOOR_SECONDS

    @property
    def cookie_name(self) -> str:
        return COOKIE_NAME if self.secure_cookie else COOKIE_NAME_INSECURE


def build_runtime(config: AccountsConfig, env: dict, mailer: Mailer | None = None,
                  clock: Callable[[], float] = time.time) -> AccountsRuntime:
    """The runtime for a deploy with the flag on. A missing or short key, or no
    way to send mail, refuses to start."""
    try:
        keys = KeyRing(
            env.get("CIC_ACCOUNTS_KEY", ""), env.get("CIC_ACCOUNTS_SESSION_KEY", ""),
            key_id=env.get("CIC_ACCOUNTS_KEY_ID", "k1"), previous=parse_previous(env.get("CIC_ACCOUNTS_KEYS_PREVIOUS")),
        )
    except AccountsKeyError as exc:
        raise AccountsConfigError(f"CIC_ACCOUNTS_ENABLED is on but the keys are not usable: {exc}") from exc
    if mailer is None:
        raise AccountsConfigError(
            "CIC_ACCOUNTS_ENABLED is on but no sign-in mail provider is configured; a sign-in code cannot be sent"
        )
    store = AccountStore(config.durable_db_path, config.ephemeral_db_path)
    service = AccountsService(store, keys, mailer, clock=clock)
    service.reapply_ledger()
    return AccountsRuntime(service=service)


class AccessLogFilter(logging.Filter):
    """Drops uvicorn access lines for the accounts routes, so no client address
    is ever logged beside a sign-in."""

    def filter(self, record: logging.LogRecord) -> bool:
        args = record.args
        path = args[2] if isinstance(args, tuple) and len(args) >= 3 and isinstance(args[2], str) else ""
        return not path.startswith(PROTECTED_LOG_PREFIXES)


def install_access_log_filter() -> None:
    target = logging.getLogger("uvicorn.access")
    if not any(isinstance(f, AccessLogFilter) for f in target.filters):
        target.addFilter(AccessLogFilter())


def start_retention_thread(runtime: AccountsRuntime, *, every_seconds: int = 3600) -> None:
    def _loop() -> None:
        while True:
            time.sleep(every_seconds)
            try:
                runtime.service.purge()
                older = runtime.service.store.accounts_on_older_keys(runtime.service.keys.key_id)
                if older:
                    logger.info("accounts still on an older address key: %d", older)
            except Exception:  # noqa: BLE001 - a purge fault must not stop the loop
                logger.exception("accounts purge failed")

    threading.Thread(target=_loop, name="accounts-purge", daemon=True).start()


class AddressBody(BaseModel):
    address: str = Field(max_length=300)


class FinishBody(BaseModel):
    address: str = Field(max_length=300)
    code: str = Field(max_length=40)
    birth_year: int | None = None


class RecoveryStartBody(BaseModel):
    recovery_code: str = Field(max_length=60)
    new_address: str = Field(max_length=300)


class RecoveryFinishBody(BaseModel):
    recovery_code: str = Field(max_length=60)
    new_address: str = Field(max_length=300)
    code: str = Field(max_length=40)


class NewAddressBody(BaseModel):
    new_address: str = Field(max_length=300)


class NewAddressFinishBody(BaseModel):
    new_address: str = Field(max_length=300)
    code: str = Field(max_length=40)


def install(app: FastAPI, runtime: AccountsRuntime) -> None:
    service = runtime.service

    def _guard(request: Request) -> None:
        if request.headers.get(CSRF_HEADER) != "1":
            raise HTTPException(status_code=400, detail="bad request")
        if not (request.headers.get("content-type") or "").startswith("application/json"):
            raise HTTPException(status_code=400, detail="bad request")
        origin = request.headers.get("origin")
        if origin:
            parts = urlsplit(origin)
            if parts.scheme != request.url.scheme or parts.netloc != request.headers.get("host", ""):
                raise HTTPException(status_code=403, detail="bad origin")

    def _network(request: Request) -> str:
        return network_of(client_ip(request))

    async def _session(request: Request) -> Session:
        session = await run_in_threadpool(service.session, request.cookies.get(runtime.cookie_name))
        if session is None:
            raise HTTPException(status_code=401, detail="not signed in")
        return session

    async def _floor(began: float) -> None:
        remaining = runtime.start_floor_seconds - (time.monotonic() - began)
        if remaining > 0:
            await asyncio.sleep(remaining)

    def _clear_cookie(response: Response) -> None:
        response.delete_cookie(
            runtime.cookie_name, path="/", secure=runtime.secure_cookie, httponly=True, samesite="lax"
        )

    def _set_cookie(response: Response, value: str) -> None:
        response.set_cookie(
            runtime.cookie_name, value, max_age=service.limits.session_absolute_seconds, path="/",
            secure=runtime.secure_cookie, httponly=True, samesite="lax",
        )

    async def _refuse(result: Result, *, delay: bool) -> None:
        if delay:
            await asyncio.sleep(runtime.miss_delay_seconds)
        status = {"throttled": 429, "paused": 503, "send_failed": 503}.get(result.status, 400)
        raise HTTPException(status_code=status, detail=MESSAGES.get(result.status, "That did not work."))

    @app.post("/api/accounts/sign-in/start")
    async def sign_in_start(body: AddressBody, request: Request):
        _guard(request)
        began = time.monotonic()
        result = await run_in_threadpool(service.start_sign_in, body.address, _network(request))
        await _floor(began)
        if result.status != "sent":
            await _refuse(result, delay=False)
        return {"status": "sent", "message": MESSAGES["sent"]}

    @app.post("/api/accounts/sign-in/finish")
    async def sign_in_finish(body: FinishBody, request: Request, response: Response):
        _guard(request)
        result = await run_in_threadpool(
            service.finish_sign_in, body.address, body.code, _network(request), body.birth_year
        )
        if result.status == "ok":
            _set_cookie(response, result.cookie)
            reply = {"status": "ok", "new_account": result.new_account}
            if result.recovery_code:
                reply["recovery_code"] = result.recovery_code
            return reply
        if result.status in ("needs_birth_year", "invalid_birth_year", "under_age"):
            return {"status": result.status, "message": MESSAGES[result.status]}
        if result.status == "recovery_waiting":
            return {"status": "recovery_waiting", "effective_on": result.effective_on}
        await _refuse(result, delay=True)

    @app.get("/api/accounts/me")
    async def me(request: Request):
        session = await run_in_threadpool(service.session, request.cookies.get(runtime.cookie_name))
        if session is None:
            return {"signed_in": False}
        return await run_in_threadpool(service.me, session)

    @app.post("/api/accounts/sign-out")
    async def sign_out(request: Request, response: Response):
        _guard(request)
        session = await run_in_threadpool(service.session, request.cookies.get(runtime.cookie_name))
        if session is not None:
            await run_in_threadpool(service.sign_out, session)
        _clear_cookie(response)
        return {"status": "ok"}

    @app.post("/api/accounts/sign-out-everywhere")
    async def sign_out_everywhere(request: Request, response: Response):
        _guard(request)
        session = await _session(request)
        await run_in_threadpool(service.sign_out_everywhere, session)
        _clear_cookie(response)
        return {"status": "ok"}

    @app.post("/api/accounts/step-up/start")
    async def step_up_start(body: AddressBody, request: Request):
        _guard(request)
        began = time.monotonic()
        result = await run_in_threadpool(service.step_up_start, await _session(request), body.address, _network(request))
        await _floor(began)
        if result.status != "sent":
            await _refuse(result, delay=False)
        return {"status": "sent", "message": MESSAGES["sent"]}

    @app.post("/api/accounts/step-up/finish")
    async def step_up_finish(body: FinishBody, request: Request):
        _guard(request)
        result = await run_in_threadpool(
            service.step_up_finish, await _session(request), body.address, body.code, _network(request)
        )
        if result.status != "ok":
            await _refuse(result, delay=True)
        return {"status": "ok"}

    @app.post("/api/accounts/recovery-code")
    async def recovery_code(request: Request):
        _guard(request)
        result = await run_in_threadpool(service.make_recovery_code, await _session(request))
        if result.status != "ok":
            await _refuse(result, delay=False)
        return {"status": "ok", "recovery_code": result.recovery_code}

    @app.post("/api/accounts/recovery/start")
    async def recovery_start(body: RecoveryStartBody, request: Request):
        _guard(request)
        began = time.monotonic()
        result = await run_in_threadpool(service.recover_start, body.recovery_code, body.new_address, _network(request))
        await _floor(began)
        if result.status != "sent":
            await _refuse(result, delay=True)
        return {"status": "sent", "message": MESSAGES["sent"]}

    @app.post("/api/accounts/recovery/finish")
    async def recovery_finish(body: RecoveryFinishBody, request: Request):
        _guard(request)
        result = await run_in_threadpool(
            service.recover_finish, body.recovery_code, body.new_address, body.code, _network(request)
        )
        if result.status != "waiting":
            await _refuse(result, delay=True)
        return {"status": "waiting", "effective_on": result.effective_on}

    @app.post("/api/accounts/recovery/cancel")
    async def recovery_cancel(request: Request):
        _guard(request)
        result = await run_in_threadpool(service.cancel_recovery, await _session(request))
        if result.status != "ok":
            await _refuse(result, delay=False)
        return {"status": "ok"}

    @app.post("/api/accounts/address/start")
    async def address_start(body: NewAddressBody, request: Request):
        _guard(request)
        began = time.monotonic()
        result = await run_in_threadpool(service.change_address_start, await _session(request), body.new_address, _network(request))
        await _floor(began)
        if result.status != "sent":
            await _refuse(result, delay=False)
        return {"status": "sent", "message": MESSAGES["sent"]}

    @app.post("/api/accounts/address/finish")
    async def address_finish(body: NewAddressFinishBody, request: Request):
        _guard(request)
        result = await run_in_threadpool(
            service.change_address_finish, await _session(request), body.new_address, body.code, _network(request)
        )
        if result.status != "ok":
            await _refuse(result, delay=True)
        return {"status": "ok"}

    @app.post("/api/accounts/export")
    async def export(request: Request):
        _guard(request)
        result = await run_in_threadpool(service.export, await _session(request))
        if result.status != "ok":
            await _refuse(result, delay=False)
        return {"status": "ok", "account": result.data}

    @app.post("/api/accounts/delete")
    async def delete(request: Request, response: Response):
        _guard(request)
        result = await run_in_threadpool(service.delete_account, await _session(request))
        if result.status != "ok":
            await _refuse(result, delay=False)
        _clear_cookie(response)
        return {"status": "ok"}
