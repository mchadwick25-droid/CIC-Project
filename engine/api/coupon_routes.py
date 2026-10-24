"""The operator's coupon button.

A coupon is a gift of tokens kept for the person who signs in with one address.
The operator types the address once. Only its keyed hash is kept, with the
amount and the day; it attaches at that person's next sign-in, whether or not
they have an account yet. Nothing here receives a name, logs an address, echoes
one back, or tells the operator whether the address has an account.

Mounted only when both Go Deeper and accounts are on. The meter mints the
coupon's one code at sign-in; the code is never shown or typed, and is held by
the account.
"""
import logging
from typing import Callable

from fastapi import FastAPI, Header, HTTPException, Request, Response
from pydantic import BaseModel, Field

from engine.accounts.service import AccountsService
from engine.api.deeper_routes import DeeperRuntime
from engine.deeper import codes
from engine.deeper.meter import AlreadyMinted, PaymentVoided

logger = logging.getLogger("cic.deeper")


class CouponRequest(BaseModel):
    address: str = Field(..., max_length=300)
    tokens: int = Field(..., strict=True, description="The gift's size, up to the operations file's coupon maximum")


class CouponCancelRequest(BaseModel):
    coupon_id: str = Field(..., min_length=1, max_length=64)


def coupon_code_hash(runtime: DeeperRuntime) -> Callable[[list[str], int], str | None]:
    """(grant ids, tokens) -> the hash of the coupon's one code, found if an earlier sign-in made it
    and stopped before attaching it, otherwise made now under the first id. The plain code is
    dropped at once."""

    def hash_for(grant_ids: list[str], tokens: int) -> str | None:
        for grant_id in grant_ids:
            found = runtime.meter.code_hash_of_payment(grant_id)
            if found is not None:
                return found
        try:
            (code,) = runtime.meter.mint("single", tokens, grant_ids[0], 1, source="coupon")
            return codes.hash_code(code)
        except AlreadyMinted:
            return runtime.meter.code_hash_of_payment(grant_ids[0])
        except PaymentVoided:
            return None

    return hash_for


def install(app: FastAPI, runtime: DeeperRuntime, service: AccountsService, *, authenticate_admin: Callable[[Request, str | None], None]) -> None:
    if runtime.ops is not None:
        service.coupon_unclaimed_days = runtime.ops.coupon_unclaimed_days
    service.coupon_code_hash = coupon_code_hash(runtime)

    @app.post("/api/admin/deeper/coupon")
    def approve_coupon(req: CouponRequest, request: Request, response: Response, authorization: str | None = Header(default=None)):
        authenticate_admin(request, authorization)
        ops = runtime.ops
        if ops is None:
            raise HTTPException(status_code=404)
        result = service.coupon_approve(
            req.address, req.tokens, max_tokens=ops.coupon_max_tokens, max_per_day=ops.coupon_max_per_day
        )
        if result.status == "invalid_address":
            raise HTTPException(status_code=422, detail="that does not look like an email address")
        if result.status == "invalid_tokens":
            raise HTTPException(status_code=422, detail=f"a coupon holds from 1 to {ops.coupon_max_tokens} tokens")
        if result.status == "limit":
            raise HTTPException(status_code=429, detail="today's coupon limit is reached; it resets tomorrow")
        response.headers["Cache-Control"] = "no-store"
        return result.data

    @app.get("/api/admin/deeper/coupons")
    def pending_coupons(request: Request, authorization: str | None = Header(default=None)):
        authenticate_admin(request, authorization)
        ops = runtime.ops
        return {
            "coupons": service.coupon_pending(),
            "max_tokens": None if ops is None else ops.coupon_max_tokens,
            "per_day": None if ops is None else ops.coupon_max_per_day,
            "unclaimed_days": service.coupon_unclaimed_days,
        }

    @app.post("/api/admin/deeper/coupon/cancel")
    def cancel_coupon(req: CouponCancelRequest, request: Request, authorization: str | None = Header(default=None)):
        authenticate_admin(request, authorization)
        if not service.coupon_cancel(req.coupon_id):
            raise HTTPException(status_code=404, detail="no waiting coupon has that id; one already attached is cancelled with its codes, by the id in the grants list")
        return {"coupon_id": req.coupon_id, "cancelled": True}
