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
import secrets
import threading
import time
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from typing import Callable

from fastapi import FastAPI, Header, HTTPException, Request, Response
from pydantic import BaseModel, Field
from starlette.concurrency import run_in_threadpool

from engine.api.deeper_door import STATE_KEY as DOOR_STATE_KEY
from engine.api.deeper_door import DoorMonitor
from engine.api.deeper_ops import DeeperOps, load_ops
from engine.deeper import codes
from engine.deeper.claims import ClaimStore, valid_reference
from engine.deeper.config import DeeperConfig
from engine.deeper import meter as meter_module
from engine.deeper.meter import KINDS, AlreadyMinted, Meter, MintLimit, PaymentVoided, is_grant
from engine.deeper.free import FreeAllowance
from engine.deeper.tokens import TokenRates

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
    tokens: int
    count: int = 1
    daily_ceiling: int | None = None


class BoundedSet:
    """Session ids this process remembers, oldest forgotten first. They are
    never written to disk and never reach the meter: the meter still holds no
    session id."""

    def __init__(self, limit: int = 20_000):
        self._limit = limit
        self._items: dict[str, None] = {}
        self._lock = threading.Lock()

    def add(self, item: str) -> None:
        with self._lock:
            self._items[item] = None
            while len(self._items) > self._limit:
                del self._items[next(iter(self._items))]

    def __contains__(self, item: str) -> bool:
        return item in self._items


@dataclass
class DeeperRuntime:
    meter: Meter
    claims: ClaimStore
    webhook_secret: str
    products: dict[str, Product]
    site_origin: str | None = None
    miss_delay_seconds: float = MISS_DELAY_SECONDS
    clock: Callable[[], float] = field(default=time.time)
    token_rates: TokenRates = field(default_factory=lambda: load_ops().rates)
    group_burst_multiplier: int = field(default_factory=lambda: load_ops().group_burst_multiplier)
    ops: DeeperOps | None = None
    facilitator_only_sessions: "BoundedSet" = field(default_factory=lambda: BoundedSet())
    paid_sessions: "BoundedSet" = field(default_factory=lambda: BoundedSet())
    free: FreeAllowance | None = None
    gift_links: frozenset = frozenset()
    door: "DoorMonitor | None" = None
    door_observe: bool = False
    paid_round_cap: int | None = None

    def __post_init__(self):
        if self.free is None:
            self.free = FreeAllowance(self.meter, self.token_rates.free_window)


def parse_gift_links(raw: str | None, products: dict[str, Product]) -> frozenset:
    """CIC_DEEPER_GIFT_LINKS: a JSON list of Payment Link ids that take gifts. A
    link is a gift or a go-deeper product, never both, so a purchase is never
    counted twice."""
    if not raw:
        return frozenset()
    try:
        links = json.loads(raw)
    except ValueError as exc:
        raise DeeperConfigError("CIC_DEEPER_GIFT_LINKS is not valid JSON") from exc
    if not isinstance(links, list) or not all(isinstance(link, str) and link for link in links):
        raise DeeperConfigError("CIC_DEEPER_GIFT_LINKS must be a list of Payment Link ids")
    if set(links) & set(products):
        raise DeeperConfigError("a Payment Link cannot be both a gift link and a go-deeper product")
    return frozenset(links)


def parse_products(raw: str | None) -> dict[str, Product]:
    """CIC_DEEPER_PRODUCTS: {"<payment link id>": {"kind", "tokens", "count"?, "daily_ceiling"?}}."""
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
                kind=spec["kind"], tokens=int(spec["tokens"]), count=int(spec.get("count", 1)),
                daily_ceiling=int(spec["daily_ceiling"]) if spec.get("daily_ceiling") is not None else None,
            )
        except (KeyError, TypeError, ValueError) as exc:
            raise DeeperConfigError(f"CIC_DEEPER_PRODUCTS entry {link!r} is malformed: {exc!r}") from exc
        if product.kind not in KINDS or product.tokens <= 0 or product.count <= 0:
            raise DeeperConfigError(f"CIC_DEEPER_PRODUCTS entry {link!r} has an invalid kind, tokens or count")
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


def _record_funds(runtime: DeeperRuntime, kind: str, session: dict) -> None:
    """The money a paid checkout brought in, for the door's ceiling. Kept apart
    from the codes: the amount and the payment id, nothing about the buyer."""
    payment = payment_id_of({"data": {"object": session}})
    cents = session.get("amount_total")
    if session.get("currency") != "usd":
        logger.error("paid checkout was not in US dollars; not counted toward the door")
        return
    if payment is None or isinstance(cents, bool) or not isinstance(cents, int) or cents <= 0:
        logger.error("paid checkout carried no payment id or amount; not counted toward the door")
        return
    try:
        runtime.meter.add_funds(kind, cents, payment)
    except ValueError:
        logger.error("paid checkout amount out of range; not counted toward the door")


def handle_event(runtime: DeeperRuntime, event: dict) -> str:
    kind = event.get("type")
    obj = _object(event)
    if kind in COMPLETED_EVENTS:
        link = obj.get("payment_link")
        if link in runtime.gift_links:
            if obj.get("payment_status") != "paid":
                return "ignored_unpaid"
            _record_funds(runtime, "gift", obj)
            return "gift_counted"
        product = runtime.products.get(link)
        if product is None:
            return "ignored_not_ours"
        if obj.get("payment_status") != "paid":
            return "ignored_unpaid"
        _record_funds(runtime, "purchase", obj)
        return _mint_for(runtime, obj, product)
    if kind in (REFUND_EVENT, DISPUTE_EVENT):
        if kind == REFUND_EVENT and obj.get("refunded") is not True:
            runtime.meter.tally("partial_refunds_ignored")
            return "ignored_partial_refund"
        payment = payment_id_of(event)
        if payment is None:
            return "ignored_no_payment"
        apply_refund(runtime, payment)
        return "voided"
    return "ignored_type"


def _count_door(meter: Meter, state) -> None:
    """What the door computed, kept as the day's peaks. In observe mode this is
    the whole report of what it would have done."""
    meter.measure_peak("door_stage", state.stage)
    meter.measure_peak("door_ratio_permille", round(state.ratio * 1000))
    meter.measure_peak("door_spend_cents", round(state.ratio * state.ceiling_usd * 100))


def apply_refund(runtime: DeeperRuntime, payment: str) -> int:
    """Takes a payment back: its codes are void, its money leaves the door's
    sum, and the reconciliation counts it. The webhook calls this for a full
    refund or a dispute; the admin route calls it for a refund Stripe's event
    cannot report (a partial one, or any made while the module was off)."""
    voided = runtime.meter.void(payment)
    runtime.meter.void_funds(payment)
    if not is_grant(payment):
        runtime.meter.tally("refunds_applied", voided)
    return voided


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
        meter.mint(product.kind, product.tokens, payment, product.count, daily_ceiling=product.daily_ceiling, prepared=prepared)
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
    tokens: int


class BalanceResponse(BaseModel):
    kind: str
    remaining: int
    paused: bool


class PauseRequest(BaseModel):
    on: bool


class VoidRequest(BaseModel):
    payment_id: str = Field(..., min_length=1, max_length=200)


MINT_MODES = ("one_code", "separate")


class MintRequest(BaseModel):
    pack_usd: int = Field(..., description="The price of one of the offer's packs; its tokens are what each unit holds")
    count: int = Field(..., ge=1, le=meter_module.MAX_BATCH_COUNT)
    mode: str = Field(..., description="one_code: a single code holding count packs. separate: count codes of one pack each")


class FundsRequest(BaseModel):
    cents: int = Field(..., description="A whole number of cents; negative takes money out")
    note: str = Field(..., min_length=1, max_length=meter_module.MAX_NOTE_CHARS)


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
        return ClaimResponse(codes=[codes.display(c) for c in made], tokens=info.tokens_total)

    @app.get("/api/deeper/balance", response_model=BalanceResponse)
    async def balance(request: Request):
        info = await run_in_threadpool(runtime.meter.status, request.headers.get(CODE_HEADER))
        if info is None or info.status == "void":
            await _miss(404, "that code did not work")
        paused = await run_in_threadpool(runtime.meter.is_paused)
        return BalanceResponse(kind=info.kind, remaining=info.remaining, paused=paused)

    @app.get("/api/deeper/door")
    def public_door(request: Request, response: Response):
        """The one public line about the free path this week: its words and
        nothing else. No stage number, no ratio, no money."""
        _cors(request, response)
        response.headers["Cache-Control"] = "public, max-age=60"
        words = runtime.ops.door_words if runtime.ops is not None else None
        state = runtime.door.state() if runtime.door is not None and not runtime.door_observe else None
        if words is None or state is None or state.stage == 0:
            return {"state": "open", "line": None}
        if state.free_voice:
            return {"state": "limited", "line": words["limited"]}
        line = words["paused"] + (" " + words["code_still_works"] if state.paid_voice else "")
        return {"state": "paused", "line": line}

    @app.post("/api/admin/deeper/pause")
    def pause(req: PauseRequest, request: Request, authorization: str | None = Header(default=None)):
        authenticate_admin(request, authorization)
        runtime.meter.pause(req.on)
        return {"paused": runtime.meter.is_paused()}

    @app.post("/api/admin/deeper/mint")
    def mint_codes(req: MintRequest, request: Request, response: Response, authorization: str | None = Header(default=None)):
        """Makes codes with no payment: the operator's own grant. The codes come
        back in this response only; the meter keeps their hashes and nothing
        else, so a lost response is voided by its mint id, never recovered. The
        grant counts toward the door as a gift of the packs' price, never a sale."""
        authenticate_admin(request, authorization)
        if runtime.ops is None:
            raise HTTPException(status_code=404)
        if req.mode not in MINT_MODES:
            raise HTTPException(status_code=422, detail=f"mode must be one of {list(MINT_MODES)}")
        pack = next((p for p in runtime.ops.packs if p.price_usd == req.pack_usd), None)
        if pack is None:
            raise HTTPException(status_code=422, detail="that price is not one of the offer's packs")
        total = pack.tokens * req.count
        if total > runtime.ops.admin_mint_max_tokens_per_request:
            raise HTTPException(status_code=422, detail=f"one request may grant at most {runtime.ops.admin_mint_max_tokens_per_request} tokens")
        grant_id = "admin_" + secrets.token_hex(12)
        kind, tokens, count = ("single", total, 1) if req.mode == "one_code" else ("batch", pack.tokens, req.count)
        try:
            made = runtime.meter.mint(
                kind, tokens, grant_id, count, source="admin", daily_token_limit=runtime.ops.admin_mint_max_tokens_per_day,
            )
        except MintLimit:
            raise HTTPException(status_code=429, detail="today's grant limit is reached; it resets tomorrow")
        except ValueError as exc:
            raise HTTPException(status_code=422, detail=str(exc))
        try:
            runtime.meter.add_funds("gift", req.pack_usd * req.count * 100, grant_id, "admin grant")
        except ValueError:
            logger.error("admin grant made but its gift could not be counted toward the door")
        response.headers["Cache-Control"] = "no-store"
        return {"mint_id": grant_id, "tokens_each": tokens, "codes": [codes.display(c) for c in made]}

    @app.get("/api/admin/deeper/grants")
    def grants(request: Request, authorization: str | None = Header(default=None)):
        authenticate_admin(request, authorization)
        return {"grants": runtime.meter.grants(2)}

    @app.get("/api/admin/deeper/status")
    def status(request: Request, authorization: str | None = Header(default=None)):
        authenticate_admin(request, authorization)
        ops = runtime.ops
        state = runtime.door.state() if runtime.door is not None else None
        window = runtime.token_rates.free_window
        share = state.free_share if state is not None and not runtime.door_observe else 1.0
        return {
            "paused": runtime.meter.is_paused(),
            "door": None if state is None else {
                "stage": state.stage, "observe": runtime.door_observe, "free_voice": state.free_voice, "paid_voice": state.paid_voice,
            },
            "free_grant": {
                "baseline_tokens": window, "window_days": runtime.token_rates.free_window_days,
                "rounds_per_conversation": runtime.token_rates.free_rounds, "now_tokens": int(window * share),
            },
            "packs": [{"price_usd": p.price_usd, "tokens": p.tokens} for p in ops.packs] if ops is not None else [],
            "mint_limits": None if ops is None else {
                "tokens_per_request": ops.admin_mint_max_tokens_per_request, "tokens_per_day": ops.admin_mint_max_tokens_per_day,
            },
        }

    @app.post("/api/admin/deeper/void")
    def void_payment(req: VoidRequest, request: Request, authorization: str | None = Header(default=None)):
        authenticate_admin(request, authorization)
        if not runtime.meter.payment_minted(req.payment_id):
            raise HTTPException(status_code=404, detail="no codes were made for that payment; nothing was changed")
        return {"payment_id": req.payment_id, "voided": apply_refund(runtime, req.payment_id)}

    @app.post("/api/admin/deeper/funds")
    def add_funds(req: FundsRequest, request: Request, authorization: str | None = Header(default=None)):
        authenticate_admin(request, authorization)
        try:
            entry = runtime.meter.add_funds("adjustment", req.cents, note=req.note)
        except ValueError as exc:
            raise HTTPException(status_code=422, detail=str(exc))
        return {"id": entry}

    @app.post("/api/admin/deeper/funds/{entry_id}/reverse")
    def reverse_funds(entry_id: str, request: Request, authorization: str | None = Header(default=None)):
        authenticate_admin(request, authorization)
        if not runtime.meter.reverse_funds(entry_id):
            raise HTTPException(status_code=404, detail="no such entry, or already reversed")
        return {"reversed": entry_id}

    @app.get("/api/admin/deeper/door")
    def door_state(request: Request, authorization: str | None = Header(default=None)):
        authenticate_admin(request, authorization)
        if runtime.door is None:
            return {"door": None}
        state = runtime.door.state()
        return {"door": {"stage": state.stage, "ratio": round(state.ratio, 3), "ceiling_usd": round(state.ceiling_usd, 2),
                         "free_voice": state.free_voice, "paid_voice": state.paid_voice, "observe": runtime.door_observe}}

    @app.get("/api/admin/deeper/measures")
    def measures(request: Request, authorization: str | None = Header(default=None)):
        authenticate_admin(request, authorization)
        return {"measures": runtime.meter.measures(14), "reconciliation": runtime.meter.reconciliation(14)}

    @app.get("/api/admin/deeper/owed")
    def owed(request: Request, authorization: str | None = Header(default=None)):
        authenticate_admin(request, authorization)
        return {"owed": runtime.meter.owed()}

    @app.get("/api/admin/deeper/funds")
    def funds(request: Request, authorization: str | None = Header(default=None)):
        authenticate_admin(request, authorization)
        return {"net": runtime.meter.net_funds(7), "entries": runtime.meter.list_funds(14)}

    @app.get("/api/admin/deeper/reconciliation")
    def reconciliation(request: Request, authorization: str | None = Header(default=None)):
        authenticate_admin(request, authorization)
        return {"days": runtime.meter.reconciliation(days=14)}


def build_runtime(config: DeeperConfig, env: dict, ops: DeeperOps | None = None, usage_store=None) -> DeeperRuntime:
    """The runtime for a deploy with the flag on. A missing webhook secret
    refuses to start rather than leaving the webhook open, and so does a
    deploy without the visitor cap or the free-allowance key, which the free allowance depends on."""
    secret = env.get("CIC_DEEPER_WEBHOOK_SECRET")
    if not secret:
        raise DeeperConfigError("CIC_DEEPER_ENABLED is on but CIC_DEEPER_WEBHOOK_SECRET is unset")
    free_key = env.get("CIC_DEEPER_FREE_KEY")
    if not free_key or len(free_key) < 32:
        raise DeeperConfigError(
            "CIC_DEEPER_ENABLED is on but CIC_DEEPER_FREE_KEY is unset or shorter than 32 characters: "
            "the free allowance is keyed by it, and it is never written to disk"
        )
    if env.get("CIC_API_ANON_CAP_ENABLED", "") not in ("1", "true", "yes"):
        raise DeeperConfigError(
            "CIC_DEEPER_ENABLED is on but CIC_API_ANON_CAP_ENABLED is off: the free allowance is kept per visitor, "
            "and without the visitor cookie everyone behind one address would share it"
        )
    ops = ops or load_ops()
    products = parse_products(env.get("CIC_DEEPER_PRODUCTS"))
    meter = Meter(
        config.meter_db_path, group_daily_ceiling=ops.group_daily_ceiling,
        free_window_days=ops.rates.free_window_days, free_key=free_key.encode("utf-8"),
    )
    door = None
    if usage_store is not None:
        door = DoorMonitor(
            ops.door, usage_store, lambda: meter.net_funds(7),
            load=lambda: meter.get_state(DOOR_STATE_KEY), save=lambda raw: meter.set_state(DOOR_STATE_KEY, raw),
            observe=lambda state: _count_door(meter, state),
        )
    return DeeperRuntime(
        meter=meter,
        claims=ClaimStore(config.claims_db_path),
        webhook_secret=secret,
        products=products,
        gift_links=parse_gift_links(env.get("CIC_DEEPER_GIFT_LINKS"), products),
        site_origin=env.get("CIC_DEEPER_SITE_ORIGIN") or None,
        token_rates=ops.rates,
        group_burst_multiplier=ops.group_burst_multiplier,
        ops=ops,
        door=door,
        door_observe=ops.door_observe,
        paid_round_cap=ops.paid_round_cap,
    )
