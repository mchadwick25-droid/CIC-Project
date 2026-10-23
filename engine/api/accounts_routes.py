"""The HTTP edge of accounts: sign-in by a typed emailed code, the session
cookie, step-up, address change, export and deletion.

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
from datetime import timedelta
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from typing import Callable
from urllib.parse import urlsplit

from fastapi import FastAPI, HTTPException, Request, Response
from pydantic import BaseModel, Field, StrictBool
from starlette.concurrency import run_in_threadpool

from engine.accounts.config import AccountsConfig
from engine.accounts.contacts import ContactStore
from engine.accounts.keys import AccountsKeyError, KeyRing, parse_previous
from engine.accounts.service import AccountsService, Mailer, Result, Session
from engine.accounts.store import AccountStore
from engine.api.account_admission import account_context, code_index, real_code_hash
from engine.api import shelf, wiring
from engine.api.contact_cipher import ContactCipher, ContactKeyError, parse_previous as parse_previous_contact
from engine.api.provider_tokens import ProviderVerifier
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
    "needs_age_answer": "Please tell us if you are 18 or over.",
    "not_adult": "Accounts are open to people who are 18 or over. The way in for younger people, with a parent or teacher, is not available yet.",
    "recovery_waiting": "A recovery to this address is waiting until {day}. You can sign in here after that day.",
    "not_available": "That way of signing in is not available right now.",
    "codes_unavailable": "Codes cannot be added right now.",
    "shelf_taken": "That conversation is already on another account's shelf.",
    "shelf_full": "Your shelf is full. Delete a conversation to make room.",
    "delete_failed": "We could not finish deleting. Please try again.",
    "code_taken": "That code belongs to another account.",
    "codes_full": "This account holds as many codes as it can.",
    "provider_cannot_use": "That sign-in cannot be added to this account.",
    "last_method": "This is your only way to sign in. Add another way first.",
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
    # Set when the app is built: removes one conversation (given its id and, when known, its code)
    # from every store that holds it, again by recorded review tokens, and lists the conversations.
    erase_conversation: Callable[..., object] | None = None
    erase_again: Callable[..., object] | None = None
    list_conversations: Callable[[], list[str]] | None = None

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
    try:
        cipher = ContactCipher(
            env.get("CIC_ACCOUNTS_CONTACT_KEY", ""), key_id=env.get("CIC_ACCOUNTS_CONTACT_KEY_ID", "c1"),
            previous=parse_previous_contact(env.get("CIC_ACCOUNTS_CONTACT_KEYS_PREVIOUS")),
            other_secrets=(env.get("CIC_ACCOUNTS_KEY", ""), env.get("CIC_ACCOUNTS_SESSION_KEY", "")),
        )
    except ContactKeyError as exc:
        raise AccountsConfigError(f"CIC_ACCOUNTS_ENABLED is on but the contact key is not usable: {exc}") from exc
    try:
        shelf_cipher = ContactCipher(
            env.get("CIC_ACCOUNTS_SHELF_KEY", ""), key_id=env.get("CIC_ACCOUNTS_SHELF_KEY_ID", "s1"),
            previous=parse_previous_contact(env.get("CIC_ACCOUNTS_SHELF_KEYS_PREVIOUS")), purpose="shelf",
            other_secrets=(env.get("CIC_ACCOUNTS_KEY", ""), env.get("CIC_ACCOUNTS_SESSION_KEY", ""),
                           env.get("CIC_ACCOUNTS_CONTACT_KEY", "")),
        )
    except ContactKeyError as exc:
        raise AccountsConfigError(f"CIC_ACCOUNTS_ENABLED is on but the shelf key is not usable: {exc}") from exc
    store = AccountStore(config.durable_db_path, config.ephemeral_db_path)
    contacts = ContactStore(config.contact_db_path, cipher)
    clients = {"google": env.get("CIC_ACCOUNTS_GOOGLE_CLIENT_ID", ""), "apple": env.get("CIC_ACCOUNTS_APPLE_CLIENT_ID", "")}
    verifier = ProviderVerifier(clients) if any(clients.values()) else None
    service = AccountsService(store, keys, QueuedMailer(mailer), clock=clock, verifier=verifier,
                              contacts=contacts, shelf_cipher=shelf_cipher)
    service.reapply_ledger()
    return AccountsRuntime(service=service)


class QueuedMailer:
    """Hands each send to a small worker pool and returns at once, so a reply never waits on
    the mail provider and never learns from it. A send that fails is logged without the address
    or the code; the person asks for a new code."""

    def __init__(self, mailer: Mailer, workers: int = 4):
        self._mailer = mailer
        self._pool = ThreadPoolExecutor(max_workers=workers, thread_name_prefix="accounts-mail")

    def send_code(self, address: str, code: str) -> None:
        self._pool.submit(self._send, address, code)

    def send_notice(self, address: str, kind: str, fields: dict) -> None:
        """A notice the owner's protection rests on is sent at once and the provider's refusal is
        raised to the caller, so the thing it warns of does not start unwarned."""
        self._mailer.send_notice(address, kind, fields)

    def _send(self, address: str, code: str) -> None:
        try:
            self._mailer.send_code(address, code)
        except Exception:  # noqa: BLE001 - the address and code must not reach a log
            logger.warning("a queued sign-in code could not be sent")


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


def sweep_unused_accounts(runtime: AccountsRuntime) -> int:
    """Removes each account unused for two years, with every conversation on its shelf. With no
    way to erase a conversation, nothing is removed."""
    erase_one = runtime.erase_conversation
    if erase_one is None:
        return 0
    removed = 0
    for account_id in runtime.service.stale_account_ids():
        # Checked again just before, so a person who signed in while the sweep ran keeps everything.
        if account_id not in runtime.service.stale_account_ids():
            continue
        if runtime.service.purge_account(account_id, lambda items: [erase_one(i, c) for i, c in items]).status == "ok":
            removed += 1
    return removed


def reapply_erasures(runtime: AccountsRuntime) -> int:
    """Erases again any conversation the ledger says was erased and that is back in the log, such
    as one restored from a backup or written to by a turn that was in flight when it was deleted."""
    if runtime.list_conversations is None or runtime.erase_again is None or not runtime.service.has_erasures():
        return 0
    matches = runtime.service.erased_matches(runtime.list_conversations())
    for session_id, tokens in matches:
        runtime.erase_again(session_id, tokens)
    return len(matches)


def shelf_exemption_from_file(path: str):
    """The exemption from the 90-day clearing, read straight from the account file when accounts are
    switched off, so turning the flag off cannot delete what people saved. With no file, nothing is exempt."""
    import os
    import sqlite3

    def _is_shelved(session_id: str) -> bool:
        if not os.path.exists(path):
            return False
        conn = None
        try:
            conn = sqlite3.connect(f"file:{path}?mode=ro", uri=True, timeout=5.0)
            return conn.execute("SELECT 1 FROM shelf WHERE session_id = ?", (session_id,)).fetchone() is not None
        except sqlite3.Error as exc:
            # Only a file made before the shelf existed holds no shelf. Any other fault (locked,
            # unreadable, cannot be opened) keeps the conversation: an error never lets the
            # clearing delete it.
            return "no such table" not in str(exc)
        finally:
            if conn is not None:
                conn.close()

    return _is_shelved


def shelve_new_session(request: Request, session_id: str, code: str) -> bool | None:
    """A conversation opened while signed in goes on the shelf at once. True when it did, False when
    the person is signed in and it did not (so the app can say so), None when not signed in. A fault
    never fails the opening of the conversation."""
    runtime = getattr(request.app.state, "accounts", None)
    cookie = request.cookies.get(runtime.cookie_name) if runtime is not None else None
    if not cookie:
        return None
    try:
        session = runtime.service.session(cookie)
        if session is None:
            return None
        return runtime.service.shelf_add(session, session_id, code).status == "ok"
    except Exception:  # noqa: BLE001
        logger.exception("a new conversation could not be put on the shelf")
        return False


def start_retention_thread(runtime: AccountsRuntime, *, every_seconds: int = 3600) -> None:
    def _loop() -> None:
        last_sweep = None
        time.sleep(30)  # let the app finish starting; erased conversations found in a restore go first
        while True:
            try:
                runtime.service.purge()
                today = runtime.service.today()
                if today != last_sweep:
                    last_sweep = today
                    removed = sweep_unused_accounts(runtime)
                    if removed:
                        logger.info("accounts unused for two years removed: %d", removed)
                if reapply_erasures(runtime):
                    logger.info("erased conversations found again and erased")
                if runtime.service.shelf_cipher is not None:
                    older = runtime.service.store.shelf_on_older_keys(runtime.service.shelf_cipher.key_id)
                    if older:
                        logger.info("shelved codes still sealed under an older key: %d", older)
                older = runtime.service.store.accounts_on_older_keys(runtime.service.keys.key_id)
                if older:
                    logger.info("accounts still on an older address key: %d", older)
                contacts = runtime.service.contacts
                if contacts is not None and contacts.on_older_keys():
                    logger.info("contacts still sealed under an older key: %d", contacts.on_older_keys())
            except Exception:  # noqa: BLE001 - a purge fault must not stop the loop
                logger.exception("accounts purge failed")
            time.sleep(every_seconds)

    threading.Thread(target=_loop, name="accounts-purge", daemon=True).start()


class AddressBody(BaseModel):
    address: str = Field(max_length=300)


class SignInFinishBody(BaseModel):
    challenge: str = Field(max_length=80)
    address: str = Field(max_length=300)
    code: str = Field(max_length=40)
    over_18: StrictBool | None = None


class ProviderBody(BaseModel):
    provider: str = Field(max_length=20)
    id_token: str = Field(max_length=4096)
    nonce: str = Field(max_length=80)


class ProviderFinishBody(ProviderBody):
    over_18: StrictBool | None = None


class ProviderNameBody(BaseModel):
    provider: str = Field(max_length=20)


class ShelfAddBody(BaseModel):
    session_id: str = Field(max_length=64)
    session_code: str = Field(max_length=80)


class ShelfRefBody(BaseModel):
    session_id: str = Field(max_length=64)


class CodeBody(BaseModel):
    code: str = Field(max_length=40)


class ChallengeBody(BaseModel):
    challenge: str = Field(max_length=80)
    code: str = Field(max_length=40)


class NewAddressBody(BaseModel):
    new_address: str = Field(max_length=300)


class AddressFinishBody(ChallengeBody):
    new_address: str = Field(max_length=300)


class RecoveryStartBody(BaseModel):
    recovery_code: str = Field(max_length=80)
    new_address: str = Field(max_length=300)


class CancelBody(BaseModel):
    address: str = Field(max_length=300)
    cancel_code: str = Field(max_length=80)


def install(app: FastAPI, runtime: AccountsRuntime) -> None:
    service = runtime.service
    app.state.accounts = runtime

    def _eraser() -> shelf.ConversationEraser | None:
        deps = getattr(app.state, "deps", None)
        if deps is None:
            return None
        return shelf.ConversationEraser(
            deps.store, deps.usage_store, getattr(app.state, "feedback_store", None), deps.qc_recorder, deps.m7_audit_root,
            on_erased=service.note_erased,
        )

    def _erase_all(items: list[tuple[str, str | None]]) -> None:
        eraser = _eraser()
        if eraser is None and items:
            raise RuntimeError("no way to erase a conversation")
        for session_id, code in items:
            eraser.erase(session_id, code)

    runtime.erase_conversation = lambda session_id, code=None: _erase_all([(session_id, code)])
    runtime.erase_again = lambda session_id, tokens=(): _eraser().erase_again(session_id, tokens)
    runtime.list_conversations = lambda: app.state.deps.store.list_session_ids()

    def _seed_allowance(request: Request, result: Result) -> None:
        """A new account starts with what is left of its browser's free window, so signing up
        is not a second allowance. A fault here never fails the sign-in."""
        deeper = getattr(request.app.state, "deeper", None)
        visitor = getattr(request.state, "visitor_id", None)  # a verified cookie only, never the address
        if not result.new_account or deeper is None or deeper.free is None or not visitor:
            return
        try:
            context = service.admission_context(result.cookie)
            if context is not None:
                deeper.free.seed_account(context["account_id"], context["refill_day"], visitor)
        except Exception:  # noqa: BLE001
            logger.exception("a new account's allowance could not be seeded")

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
        status = {"throttled": 429, "paused": 503, "send_failed": 503, "not_available": 404, "codes_unavailable": 404, "gone": 401, "delete_failed": 500, "shelf_taken": 400, "shelf_full": 400}.get(result.status, 400)
        raise HTTPException(status_code=status, detail=MESSAGES.get(result.status, "That did not work."))

    @app.post("/api/accounts/sign-in/start")
    async def sign_in_start(body: AddressBody, request: Request):
        _guard(request)
        began = time.monotonic()
        result = await run_in_threadpool(service.start_sign_in, body.address, _network(request))
        await _floor(began)
        if result.status != "sent":
            await _refuse(result, delay=False)
        return {"status": "sent", "message": MESSAGES["sent"], "challenge": result.challenge}

    @app.post("/api/accounts/sign-in/finish")
    async def sign_in_finish(body: SignInFinishBody, request: Request, response: Response):
        _guard(request)
        result = await run_in_threadpool(
            service.finish_sign_in, body.challenge, body.address, body.code, _network(request), body.over_18
        )
        if result.status == "ok":
            await run_in_threadpool(_seed_allowance, request, result)
            _set_cookie(response, result.cookie)
            return {"status": "ok", "new_account": result.new_account}
        if result.status in ("needs_age_answer", "not_adult"):
            return {"status": result.status, "message": MESSAGES[result.status]}
        if result.status == "recovery_waiting":
            return {"status": result.status, "effective_on": result.data["effective_on"],
                    "message": MESSAGES["recovery_waiting"].format(day=result.data["effective_on"])}
        await _refuse(result, delay=True)

    @app.get("/api/accounts/providers")
    async def providers():
        verifier = service.verifier
        return {"providers": verifier.public_ids() if verifier is not None else {}}

    @app.post("/api/accounts/provider/start")
    async def provider_start(request: Request):
        _guard(request)
        result = await run_in_threadpool(service.provider_start, _network(request))
        if result.status != "sent":
            await _refuse(result, delay=False)
        return {"status": "ok", "nonce": result.challenge}

    @app.post("/api/accounts/provider/finish")
    async def provider_finish(body: ProviderFinishBody, request: Request, response: Response):
        _guard(request)
        result = await run_in_threadpool(
            service.provider_sign_in, body.provider, body.id_token, body.nonce, _network(request), body.over_18
        )
        if result.status == "ok":
            await run_in_threadpool(_seed_allowance, request, result)
            _set_cookie(response, result.cookie)
            return {"status": "ok", "new_account": result.new_account}
        if result.status in ("needs_age_answer", "not_adult"):
            return {"status": result.status, "message": MESSAGES[result.status]}
        await _refuse(result, delay=True)

    @app.post("/api/accounts/step-up/provider")
    async def step_up_provider(body: ProviderBody, request: Request):
        _guard(request)
        result = await run_in_threadpool(
            service.provider_step_up, await _session(request), body.provider, body.id_token, body.nonce, _network(request)
        )
        if result.status != "ok":
            await _refuse(result, delay=True)
        return {"status": "ok"}

    @app.post("/api/accounts/provider/link")
    async def provider_link(body: ProviderBody, request: Request):
        _guard(request)
        result = await run_in_threadpool(
            service.provider_link, await _session(request), body.provider, body.id_token, body.nonce, _network(request)
        )
        if result.status != "ok":
            await _refuse(result, delay=True)
        return {"status": "ok"}

    @app.post("/api/accounts/provider/unlink")
    async def provider_unlink(body: ProviderNameBody, request: Request):
        _guard(request)
        result = await run_in_threadpool(service.provider_unlink, await _session(request), body.provider)
        if result.status != "ok":
            await _refuse(result, delay=False)
        return {"status": "ok"}

    @app.post("/api/accounts/codes/attach")
    async def codes_attach(body: CodeBody, request: Request):
        _guard(request)
        session = await _session(request)
        deeper = getattr(request.app.state, "deeper", None)
        if deeper is None:
            await _refuse(Result("codes_unavailable"), delay=False)
        code_hash = await run_in_threadpool(real_code_hash, body.code, deeper)
        result = await run_in_threadpool(service.attach_code, session, code_hash, _network(request))
        if result.status == "codes_full":
            # Links that name no live code are dead weight; clear them and try once more.
            context = await run_in_threadpool(account_context, request, deeper)
            if context is not None and context.unresolved:
                await run_in_threadpool(service.drop_code_links, session.account_id, context.unresolved)
                result = await run_in_threadpool(service.attach_code, session, code_hash, _network(request))
        if result.status != "ok":
            await _refuse(result, delay=True)
        index = code_index(request, deeper)
        if index is not None:
            index.add(code_hash)
        return {"status": "ok"}

    @app.get("/api/accounts/shelf")
    async def shelf_list(request: Request):
        session = await _session(request)
        deps = request.app.state.deps

        def _read():
            shown = []
            for session_id, saved in service.shelf_list(session):
                described = shelf.describe(deps.store, deps.registry, session_id)
                if described is None:
                    service.shelf_remove(session, session_id)  # the conversation is gone; so is its place
                    continue
                shown.append({**described, "saved": saved})
            return shown

        return {"status": "ok", "conversations": await run_in_threadpool(_read)}

    @app.post("/api/accounts/shelf/add")
    async def shelf_add(body: ShelfAddBody, request: Request):
        """Puts the conversation open in the browser on the shelf, with the code it was opened with."""
        _guard(request)
        session = await _session(request)
        deps = request.app.state.deps
        opens = await run_in_threadpool(shelf.code_opens, deps.store, body.session_id, body.session_code)
        if not opens:
            await _refuse(Result("wrong"), delay=True)
        result = await run_in_threadpool(service.shelf_add, session, body.session_id, body.session_code)
        if result.status != "ok":
            await _refuse(result, delay=True)
        return {"status": "ok"}

    @app.post("/api/accounts/shelf/reopen")
    async def shelf_reopen(body: ShelfRefBody, request: Request):
        """The conversation's own code, for its owner, to continue it. A conversation that holds a
        Facilitator safety turn is flagged so the resources line is shown first, every time."""
        _guard(request)
        session = await _session(request)
        deps = request.app.state.deps

        def _open():
            code = service.shelf_open(session, body.session_id)
            if code is None or not shelf.code_opens(deps.store, body.session_id, code):
                if code is not None:
                    service.shelf_remove(session, body.session_id)  # the conversation is gone
                return None
            described = shelf.describe(deps.store, deps.registry, body.session_id)
            # When it cannot be read, the resources line is shown: caution is the default.
            return {"session_id": body.session_id, "session_code": code,
                    "holds_crisis_turn": True if described is None else described["holds_crisis_turn"],
                    "resources_text": shelf.resources_text(deps.store, body.session_id)}

        opened = await run_in_threadpool(_open)
        if opened is None:
            await _refuse(Result("wrong"), delay=True)
        return {"status": "ok", **opened}

    @app.post("/api/accounts/shelf/delete")
    async def shelf_delete(body: ShelfRefBody, request: Request):
        """Deletes one conversation from the shelf and from every store that holds it."""
        _guard(request)
        session = await _session(request)

        def _delete():
            if not service.shelf_has(session, body.session_id):
                return False
            _erase_all([(body.session_id, service.shelf_open(session, body.session_id))])
            service.shelf_remove(session, body.session_id)
            return True

        try:
            done = await run_in_threadpool(_delete)
        except Exception:  # noqa: BLE001
            logger.exception("a shelved conversation could not be deleted")
            await _refuse(Result("delete_failed"), delay=False)
        if not done:
            await _refuse(Result("wrong"), delay=True)
        return {"status": "ok"}

    @app.get("/api/accounts/balance")
    async def balance(request: Request):
        """The account's own free window and the codes it holds. The free figure is the account's
        window alone; a turn is also bounded by the network window and the door, as the header says."""
        deeper = getattr(request.app.state, "deeper", None)
        cookie = request.cookies.get(runtime.cookie_name)
        if not cookie:
            return {"signed_in": False}
        if deeper is None or deeper.free is None:
            live = await run_in_threadpool(service.session, cookie)
            return {"signed_in": True, "available": False} if live is not None else {"signed_in": False}
        context = await run_in_threadpool(account_context, request, deeper)
        if context is None:
            return {"signed_in": False}
        try:
            free = deeper.free
            held = [deeper.meter.status_of_hash(h) for h in context.code_hashes]
            start = deeper.meter.account_window_start(context.refill_day)
            refill_on = (start.replace(day=1) + timedelta(days=32)).replace(day=context.refill_day)
            return {
                "signed_in": True, "available": True,
                "free_left": free.account_left(context.account_id, context.refill_day),
                "free_total": free.window_amount,
                "refill_on": refill_on.isoformat(),
                "codes_held": len(context.code_hashes),
                "code_tokens": sum(i.remaining for i in held if i is not None and i.status == "live"),
            }
        except Exception:  # noqa: BLE001
            logger.exception("the account balance could not be read")
            return {"signed_in": True, "available": False}

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
        return {"status": "sent", "message": MESSAGES["sent"], "challenge": result.challenge}

    @app.post("/api/accounts/step-up/finish")
    async def step_up_finish(body: ChallengeBody, request: Request):
        _guard(request)
        result = await run_in_threadpool(
            service.step_up_finish, await _session(request), body.challenge, body.code, _network(request)
        )
        if result.status != "ok":
            await _refuse(result, delay=True)
        return {"status": "ok"}

    @app.post("/api/accounts/address/start")
    async def address_start(body: NewAddressBody, request: Request):
        _guard(request)
        began = time.monotonic()
        result = await run_in_threadpool(service.change_address_start, await _session(request), body.new_address, _network(request))
        await _floor(began)
        if result.status != "sent":
            await _refuse(result, delay=False)
        return {"status": "sent", "message": MESSAGES["sent"], "challenge": result.challenge}

    @app.post("/api/accounts/address/finish")
    async def address_finish(body: AddressFinishBody, request: Request):
        _guard(request)
        result = await run_in_threadpool(
            service.change_address_finish, await _session(request), body.challenge, body.code, _network(request), body.new_address
        )
        if result.status != "ok":
            await _refuse(result, delay=True)
        return {"status": "ok"}

    @app.post("/api/accounts/recovery/code")
    async def recovery_code(request: Request):
        _guard(request)
        result = await run_in_threadpool(service.recovery_code_make, await _session(request))
        if result.status != "ok":
            await _refuse(result, delay=False)
        return {"status": "ok", "recovery_code": result.data["recovery_code"]}

    @app.post("/api/accounts/recovery/start")
    async def recovery_start(body: RecoveryStartBody, request: Request):
        _guard(request)
        began = time.monotonic()
        result = await run_in_threadpool(service.recovery_start, body.recovery_code, body.new_address, _network(request))
        await _floor(began)
        if result.status != "sent":
            await _refuse(result, delay=False)
        return {"status": "sent", "message": MESSAGES["sent"], "challenge": result.challenge}

    @app.post("/api/accounts/recovery/finish")
    async def recovery_finish(body: AddressFinishBody, request: Request):
        _guard(request)
        result = await run_in_threadpool(
            service.recovery_prove, body.challenge, body.code, body.new_address, _network(request)
        )
        if result.status != "ok":
            await _refuse(result, delay=True)
        return {"status": "ok", **result.data}

    @app.post("/api/accounts/recovery/cancel")
    async def recovery_cancel(body: CancelBody, request: Request):
        _guard(request)
        began = time.monotonic()
        result = await run_in_threadpool(service.recovery_cancel, body.address, body.cancel_code, _network(request))
        await _floor(began)
        if result.status != "ok":
            await _refuse(result, delay=False)
        return {"status": "ok"}

    @app.post("/api/accounts/recovery/cancel-signed-in")
    async def recovery_cancel_signed_in(request: Request):
        _guard(request)
        result = await run_in_threadpool(service.recovery_cancel_signed_in, await _session(request))
        if result.status != "ok":
            await _refuse(result, delay=False)
        return {"status": "ok"}

    @app.post("/api/accounts/export")
    async def export(request: Request):
        _guard(request)
        session = await _session(request)
        result = await run_in_threadpool(service.export, session)
        if result.status != "ok":
            await _refuse(result, delay=False)
        deps = request.app.state.deps

        def _conversations():
            out = []
            for session_id, saved in service.shelf_list(session):
                described = shelf.describe(deps.store, deps.registry, session_id)
                if described is None:
                    continue
                try:
                    transcript = wiring.get_transcript(deps.store, session_id).transcript
                except wiring.SessionNotFound:
                    continue
                out.append({**described, "saved": saved, "transcript": transcript})
            return out

        return {"status": "ok", "account": result.data, "conversations": await run_in_threadpool(_conversations)}

    @app.post("/api/accounts/delete")
    async def delete(request: Request, response: Response):
        _guard(request)
        result = await run_in_threadpool(service.delete_account, await _session(request), _erase_all)
        if result.status != "ok":
            await _refuse(result, delay=False)
        _clear_cookie(response)
        return {"status": "ok"}
