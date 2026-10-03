"""The HTTP edge of Go Deeper: the signed Stripe webhook, the claim and
balance routes, the pause switch, and the daily reconciliation.

Mounted only when CIC_DEEPER_ENABLED is on (engine.api.app.create_app is
handed a DeeperRuntime, or none). With the flag off no path under /api/deeper
exists, no file is opened and no thread starts. The conversation engine never
sees any of this: these routes read and write the module's own two files and
nothing else.

A payment is told apart from a gift by its Payment Link: only a link named in
CIC_DEEPER_PRODUCTS makes codes. Stripe's signature is checked against the raw
request body before anything is read from it.
"""
import asyncio
import hashlib
import hmac
import json
import logging
import threading
import time
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from typing import Callable

from fastapi import FastAPI, Header, HTTPException, Request, Response
from pydantic import BaseModel, Field
from starlette.concurrency import run_in_threadpool

from engine.deeper import codes
from engine.deeper.claims import ClaimStore, valid_reference
from engine.deeper.config import DeeperConfig
from engine.deeper.meter import KINDS, AlreadyMinted, Meter, PaymentVoided

logger = logging.getLogger("cic.deeper")

MAX_WEBHOOK_BODY_BYTES = 256 * 1024
SIGNATURE_TOLERANCE_SECONDS = 300
MISS_DELAY_SECONDS = 0.5
CODE_HEADER = "x-cic-code"
PROTECTED_LOG_PREFIXES = ("/api/session", "/api/deeper")

COMPLETED_EVENTS = ("checkout.session.completed", "checkout.session.async_payment_succeeded")
REFUND_EVENT = "charge.refunded"
DISPUTE_EVENT = "charge.dispute.created"


class DeeperConfigError(Exception):
    """A misconfiguration found at startup, never papered over."""


@dataclass(frozen=True)
class Product:
    kind: str
    exchanges: int
    count: int = 1
    daily_ceiling: int | None = None


@dataclass
class DeeperRuntime:
    meter: Meter
    claims: ClaimStore
    webhook_secret: str
    products: dict[str, Product]
    site_origin: str | None = None
    miss_delay_seconds: float = MISS_DELAY_SECONDS
    clock: Callable[[], float] = field(default=time.time)


def parse_products(raw: str | None) -> dict[str, Product]:
    """CIC_DEEPER_PRODUCTS: {"<payment link id>": {"kind", "exchanges", "count"?, "daily_ceiling"?}}."""
    if not raw:
        return {}
    try:
        data = json.loads(raw)
    except ValueError as exc:
        raise DeeperConfigError(f"CIC_DEEPER_PRODUCTS is not JSON: {exc}") from exc
    if not isinstance(data, dict):
        raise DeeperConfigError("CIC_DEEPER_PRODUCTS must be a JSON object keyed by payment link id")
    products = {}
    for link, spec in data.items():
        try:
            product = Product(
                kind=spec["kind"], exchanges=int(spec["exchanges"]), count=int(spec.get("count", 1)),
                daily_ceiling=int(spec["daily_ceiling"]) if spec.get("daily_ceiling") is not None else None,
            )
        except (KeyError, TypeError, ValueError) as exc:
            raise DeeperConfigError(f"CIC_DEEPER_PRODUCTS entry {link!r} is malformed: {exc!r}") from exc
        if product.kind not in KINDS or product.exchanges <= 0 or product.count <= 0:
            raise DeeperConfigError(f"CIC_DEEPER_PRODUCTS entry {link!r} has an invalid kind, exchanges or count")
        if product.kind != "batch" and product.count != 1:
            raise DeeperConfigError(f"CIC_DEEPER_PRODUCTS entry {link!r}: only a batch makes more than one code")
        products[link] = product
    return products


def verify_signature(payload: bytes, header: str | None, secret: str, *, now: float | None = None) -> bool:
    """Stripe's scheme: the header carries t=<unix time> and one or more
    v1=<hex>, each an HMAC-SHA256 of '<t>.<raw body>' under the endpoint
    secret. The time must be within the tolerance."""
    if not header or not secret:
        return False
    parts = [p.split("=", 1) for p in header.split(",") if "=" in p]
    stamps = [v for k, v in parts if k.strip() == "t"]
    signatures = [v.strip() for k, v in parts if k.strip() == "v1"]
    if len(stamps) != 1 or not signatures:
        return False
    try:
        stamp = int(stamps[0])
    except ValueError:
        return False
    if abs((time.time() if now is None else now) - stamp) > SIGNATURE_TOLERANCE_SECONDS:
        return False
    expected = hmac.new(secret.encode(), f"{stamp}.".encode() + payload, hashlib.sha256).hexdigest()
    return any(hmac.compare_digest(expected, s) for s in signatures)


def _object(event: dict) -> dict:
    obj = (event.get("data") or {}).get("object")
    return obj if isinstance(obj, dict) else {}


def payment_id_of(event: dict) -> str | None:
    """The one id the meter keeps: the payment intent. Completion, refund and
    dispute events all carry it on their object."""
    value = _object(event).get("payment_intent")
    return value if isinstance(value, str) and value else None


def handle_event(runtime: DeeperRuntime, event: dict) -> str:
    kind = event.get("type")
    obj = _object(event)
    if kind in COMPLETED_EVENTS:
        product = runtime.products.get(obj.get("payment_link"))
        if product is None:
            return "ignored_not_ours"
        if obj.get("payment_status") != "paid":
            return "ignored_unpaid"
        return _mint_for(runtime, obj, product)
    if kind in (REFUND_EVENT, DISPUTE_EVENT):
        if kind == REFUND_EVENT and obj.get("refunded") is not True:
            runtime.meter.tally("partial_refunds_ignored")
            return "ignored_partial_refund"
        payment = payment_id_of(event)
        if payment is None:
            return "ignored_no_payment"
        voided = runtime.meter.void(payment)
        runtime.meter.tally("refunds_applied", voided)
        return "voided"
    return "ignored_type"


def _mint_for(runtime: DeeperRuntime, session: dict, product: Product) -> str:
    """Claim first, then mint: the codes are put in the claim table before they
    exist in the meter, so a crash between the two leaves a payment a replay can
    finish, never a paid code nobody can reach. A claim this call did not create
    is never deleted."""
    payment = payment_id_of({"data": {"object": session}})
    reference = session.get("client_reference_id")
    meter, claims = runtime.meter, runtime.claims
    if payment is None:
        meter.tally("payments_seen")
        logger.error("paid checkout carried no payment intent; nothing minted")
        return "unmatched_no_payment"
    if meter.payment_voided(payment):
        meter.tally("payments_seen")
        meter.tally("payments_voided_first")
        return "voided_first"
    if meter.payment_minted(payment):
        return "replayed"
    if not valid_reference(reference):
        meter.tally("payments_seen")
        logger.error("paid checkout carried no usable claim reference; nothing minted")
        return "unmatched_no_reference"
    held = claims.get(reference)
    made_claim = False
    if held is not None:
        if len(held) != product.count or any(meter.status(code) is not None for code in held):
            meter.tally("payments_seen")
            logger.error("claim reference already holds another purchase; nothing minted")
            return "unmatched_reference_reused"
        prepared = held
    else:
        prepared = [codes.generate() for _ in range(product.count)]
        if not claims.put(reference, prepared):
            meter.tally("payments_seen")
            logger.error("claim reference could not be stored; nothing minted")
            return "unmatched_claim_conflict"
        made_claim = True
    try:
        meter.mint(product.kind, product.exchanges, payment, product.count, daily_ceiling=product.daily_ceiling, prepared=prepared)
    except AlreadyMinted:
        return "replayed"
    except PaymentVoided:
        if made_claim:
            claims.delete(reference)
        meter.tally("payments_seen")
        meter.tally("payments_voided_first")
        return "voided_first"
    except ValueError:
        if made_claim:
            claims.delete(reference)
        meter.tally("payments_seen")
        logger.error("prepared codes were refused by the meter; nothing minted")
        return "unmatched_claim_conflict"
    claims.purge()
    return "minted"


class ClaimRequest(BaseModel):
    reference: str = Field(max_length=200)


class ClaimResponse(BaseModel):
    codes: list[str]
    exchanges: int


class BalanceResponse(BaseModel):
    kind: str
    remaining: int
    paused: bool


class PauseRequest(BaseModel):
    on: bool


class AccessLogFilter(logging.Filter):
    """Drops uvicorn access lines for the session and deeper routes, so no
    client address is ever logged beside a session id or a claim."""

    def filter(self, record: logging.LogRecord) -> bool:
        args = record.args
        path = args[2] if isinstance(args, tuple) and len(args) >= 3 and isinstance(args[2], str) else ""
        return not path.startswith(PROTECTED_LOG_PREFIXES)


def install_access_log_filter() -> None:
    target = logging.getLogger("uvicorn.access")
    if not any(isinstance(f, AccessLogFilter) for f in target.filters):
        target.addFilter(AccessLogFilter())


def run_retention_once(runtime: DeeperRuntime) -> dict:
    removed_meter = runtime.meter.purge()
    removed_claims = runtime.claims.purge()
    today = runtime.meter.reconciliation(days=2)
    gaps = [r for r in today if r["gap"] != 0]
    for row in gaps:
        logger.warning("reconciliation gap day=%s seen=%d minted=%d gap=%d", row["day"], row["payments_seen"], row["payments_minted"], row["gap"])
    return {"meter_rows_removed": removed_meter, "claims_removed": removed_claims, "gap_days": len(gaps)}


def start_retention_thread(runtime: DeeperRuntime, *, hour: int = 5, minute: int = 12) -> None:
    def _loop() -> None:
        while True:
            now = datetime.now(timezone.utc)
            nxt = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
            if nxt <= now:
                nxt += timedelta(days=1)
            time.sleep(max(0.0, (nxt - now).total_seconds()))
            try:
                run_retention_once(runtime)
            except Exception:  # noqa: BLE001 - the loop must survive its own job failing
                logger.exception("deeper retention pass failed")

    threading.Thread(target=_loop, name="deeper-retention", daemon=True).start()


def install(app: FastAPI, runtime: DeeperRuntime, *, authenticate_admin: Callable[[Request, str | None], None]) -> None:
    async def _miss(status_code: int, detail: str):
        await asyncio.sleep(runtime.miss_delay_seconds)
        raise HTTPException(status_code=status_code, detail=detail)

    def _cors(request: Request, response: Response) -> None:
        origin = request.headers.get("origin")
        if runtime.site_origin and origin == runtime.site_origin:
            response.headers["Access-Control-Allow-Origin"] = origin
            response.headers["Vary"] = "Origin"

    @app.post("/api/deeper/webhook")
    async def webhook(request: Request, stripe_signature: str | None = Header(default=None)):
        declared = request.headers.get("content-length")
        if declared and declared.isdigit() and int(declared) > MAX_WEBHOOK_BODY_BYTES:
            raise HTTPException(status_code=413, detail="payload too large")
        payload = b""
        async for chunk in request.stream():
            payload += chunk
            if len(payload) > MAX_WEBHOOK_BODY_BYTES:
                raise HTTPException(status_code=413, detail="payload too large")
        if not verify_signature(payload, stripe_signature, runtime.webhook_secret):
            raise HTTPException(status_code=400, detail="bad signature")
        try:
            event = json.loads(payload)
        except ValueError:
            raise HTTPException(status_code=400, detail="bad payload")
        if not isinstance(event, dict):
            raise HTTPException(status_code=400, detail="bad payload")
        outcome = await run_in_threadpool(handle_event, runtime, event)
        logger.info("webhook handled type=%s outcome=%s", event.get("type"), outcome)
        return {"received": True}

    @app.options("/api/deeper/claim")
    def claim_preflight(request: Request, response: Response):
        _cors(request, response)
        response.headers["Access-Control-Allow-Methods"] = "POST"
        response.headers["Access-Control-Allow-Headers"] = "content-type"
        response.headers["Access-Control-Max-Age"] = "600"
        response.status_code = 204

    @app.post("/api/deeper/claim", response_model=ClaimResponse)
    async def claim(req: ClaimRequest, request: Request, response: Response):
        _cors(request, response)
        made = await run_in_threadpool(runtime.claims.get, req.reference)
        info = await run_in_threadpool(runtime.meter.status, made[0]) if made else None
        if info is None or info.status == "void":
            await _miss(404, "no codes yet")
        return ClaimResponse(codes=[codes.display(c) for c in made], exchanges=info.exchanges_total)

    @app.get("/api/deeper/balance", response_model=BalanceResponse)
    async def balance(request: Request):
        info = await run_in_threadpool(runtime.meter.status, request.headers.get(CODE_HEADER))
        if info is None or info.status == "void":
            await _miss(404, "that code did not work")
        paused = await run_in_threadpool(runtime.meter.is_paused)
        return BalanceResponse(kind=info.kind, remaining=info.remaining, paused=paused)

    @app.post("/api/admin/deeper/pause")
    def pause(req: PauseRequest, request: Request, authorization: str | None = Header(default=None)):
        authenticate_admin(request, authorization)
        runtime.meter.pause(req.on)
        return {"paused": runtime.meter.is_paused()}

    @app.get("/api/admin/deeper/reconciliation")
    def reconciliation(request: Request, authorization: str | None = Header(default=None)):
        authenticate_admin(request, authorization)
        return {"days": runtime.meter.reconciliation(days=14)}


def build_runtime(config: DeeperConfig, env: dict) -> DeeperRuntime:
    """The runtime for a deploy with the flag on. A missing webhook secret
    refuses to start rather than leaving the webhook open."""
    secret = env.get("CIC_DEEPER_WEBHOOK_SECRET")
    if not secret:
        raise DeeperConfigError("CIC_DEEPER_ENABLED is on but CIC_DEEPER_WEBHOOK_SECRET is unset")
    return DeeperRuntime(
        meter=Meter(config.meter_db_path, group_daily_ceiling=config.group_daily_ceiling),
        claims=ClaimStore(config.claims_db_path),
        webhook_secret=secret,
        products=parse_products(env.get("CIC_DEEPER_PRODUCTS")),
        site_origin=env.get("CIC_DEEPER_SITE_ORIGIN") or None,
    )
