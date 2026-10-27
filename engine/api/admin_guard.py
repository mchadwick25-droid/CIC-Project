"""The guard on every dashboard change made with the admin cookie."""
from urllib.parse import urlsplit

from fastapi import HTTPException, Request

from engine.api.accounts_routes import CSRF_HEADER


def guard_admin_change(request: Request, authorization: str | None) -> None:
    """A change made with the dashboard cookie must come from our own page: the custom header cannot
    be sent cross-site without a preflight, and the origin, when sent, must be ours. A Bearer caller
    holds the token and needs neither."""
    if authorization:
        return
    if request.headers.get(CSRF_HEADER) != "1":
        raise HTTPException(status_code=400, detail="bad request")
    origin = request.headers.get("origin")
    if origin:
        parts = urlsplit(origin)
        if parts.scheme != request.url.scheme or parts.netloc != request.headers.get("host", ""):
            raise HTTPException(status_code=403, detail="bad origin")
