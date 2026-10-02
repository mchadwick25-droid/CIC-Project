"""HTTP surface for the access module.

The engine calls the /access endpoints with an internal token and the visitor
id it already holds. Stripe calls the webhook with a signed body. Browsers never
call this service directly.
"""
import hmac
import json
from pathlib import Path

from fastapi import FastAPI, Header, HTTPException, Request
from pydantic import BaseModel

from .checkout import CheckoutError, Transport, create_checkout_session
from .ledger import LedgerError
from .service import AccessService
from .store import connect, init_schema
from .stripe_events import Catalogue, apply_event, verify_signature




class StartBody(BaseModel):
    visitor_id: str
    session_id: str


class SessionBody(BaseModel):
    session_id: str


class CheckoutBody(BaseModel):
    visitor_id: str
    sku: str


def create_app(
    db_path: str | Path, catalogue: Catalogue, product_names: dict[str, str], internal_token: str, stripe_secret_key: str,
    webhook_secret: str, transport: Transport, success_url: str, cancel_url: str,
) -> FastAPI:
    app = FastAPI()
    seed = connect(db_path)
    init_schema(seed)
    seed.close()

    def service() -> tuple[AccessService, object]:
        conn = connect(db_path)
        return AccessService(conn), conn

    def require_token(token: str | None) -> None:
        if token is None or not hmac.compare_digest(token, internal_token):
            raise HTTPException(status_code=401, detail="invalid access token")

    @app.get("/access/packs")
    def packs():
        return [
            {"sku": code, "conversations": sku.units, "amount_cents": sku.amount_cents, "currency": sku.currency}
            for code, sku in catalogue.items()
        ]

    @app.post("/access/start")
    def start(body: StartBody, x_access_token: str | None = Header(default=None)):
        require_token(x_access_token)
        svc, conn = service()
        try:
            started = svc.start_conversation(body.visitor_id, body.session_id)
            balance = svc.balance(body.visitor_id)
        finally:
            conn.close()
        return {
            "admitted": started.admitted, "bucket": started.bucket, "turn_cap": started.turn_cap, "reason": started.reason,
            "balance": {"free": balance.free, "paid": balance.paid, "total": balance.total},
        }

    @app.post("/access/first-reply")
    def first_reply(body: SessionBody, x_access_token: str | None = Header(default=None)):
        require_token(x_access_token)
        svc, conn = service()
        try:
            return {"captured": svc.first_reply_stored(body.session_id)}
        except LedgerError as exc:
            raise HTTPException(status_code=409, detail=str(exc))
        finally:
            conn.close()

    @app.post("/access/failed")
    def failed(body: SessionBody, x_access_token: str | None = Header(default=None)):
        require_token(x_access_token)
        svc, conn = service()
        try:
            return {"released": svc.conversation_failed(body.session_id)}
        except LedgerError as exc:
            raise HTTPException(status_code=409, detail=str(exc))
        finally:
            conn.close()

    @app.get("/access/balance")
    def balance(visitor_id: str, x_access_token: str | None = Header(default=None)):
        require_token(x_access_token)
        svc, conn = service()
        try:
            view = svc.balance(visitor_id)
        finally:
            conn.close()
        return {"free": view.free, "paid": view.paid, "total": view.total}

    @app.post("/access/checkout")
    def checkout(body: CheckoutBody, x_access_token: str | None = Header(default=None)):
        require_token(x_access_token)
        try:
            session = create_checkout_session(
                stripe_secret_key, body.visitor_id, body.sku, catalogue, product_names, success_url, cancel_url, transport,
            )
        except CheckoutError as exc:
            raise HTTPException(status_code=400, detail=str(exc))
        return {"session_id": session.session_id, "url": session.url}

    @app.post("/access/stripe-webhook")
    async def webhook(request: Request, stripe_signature: str | None = Header(default=None)):
        payload = await request.body()
        if not stripe_signature or not verify_signature(payload, stripe_signature, webhook_secret):
            raise HTTPException(status_code=400, detail="invalid signature")
        try:
            event = json.loads(payload)
        except ValueError:
            raise HTTPException(status_code=400, detail="invalid body")
        conn = connect(db_path)
        try:
            result = apply_event(conn, event, catalogue)
        finally:
            conn.close()
        return {"outcome": result.outcome}

    return app
