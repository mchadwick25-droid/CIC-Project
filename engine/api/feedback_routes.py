"""Feedback endpoints: a participant's like or flag on one Representative
reply, a comment, a page like or a page report from the app or the public
site, and the operator's queue.

Storage only. The server reads the record ids and confidence tags for a flagged
sentence from the conversation's own stored plan, so the client never names
them, and it never copies the reply's words into the store. No model is called.
"""
from typing import Annotated, Any, Callable, Literal

from fastapi import FastAPI, Header, HTTPException, Request, Response
from pydantic import BaseModel, Discriminator, Field, Tag

from engine.api.admin_guard import guard_admin_change
from engine.feedback.store import OUTCOMES, FeedbackStore

MAX_FLAG_LINE = 600
MAX_COMMENT = 2000
MAX_PAGE = 80
MAX_PAGE_ID = 120
PAGE_ID_PATTERN = r"^[A-Za-z0-9/_.:-]+$"
MAX_NAME = 60
MAX_EMAIL = 200


class SessionFeedbackRequest(BaseModel):
    kind: Literal["like", "flag"]
    turn_index: int = Field(ge=0)
    sentence_index: int | None = Field(default=None, ge=0)
    reason: Literal["fact_wrong", "source_mismatch", "overcertain", "unclear"] | None = None
    text: str | None = Field(default=None, max_length=MAX_FLAG_LINE)
    email: str | None = Field(default=None, max_length=MAX_EMAIL)


class CommentRequest(BaseModel):
    kind: Literal["comment"] = "comment"
    page: str = Field(min_length=1, max_length=MAX_PAGE)
    text: str = Field(min_length=1, max_length=MAX_COMMENT)
    quote_consent: Literal["no", "anonymous", "first_name"] = "no"
    first_name: str | None = Field(default=None, max_length=MAX_NAME)
    email: str | None = Field(default=None, max_length=MAX_EMAIL)


class PageLikeRequest(BaseModel):
    kind: Literal["like"]
    page: str = Field(min_length=1, max_length=MAX_PAGE_ID, pattern=PAGE_ID_PATTERN)


class PageReportRequest(BaseModel):
    kind: Literal["report"]
    page: str = Field(min_length=1, max_length=MAX_PAGE_ID, pattern=PAGE_ID_PATTERN)
    reason: Literal["accuracy", "craft"]
    text: str = Field(min_length=1, max_length=MAX_FLAG_LINE)
    email: str | None = Field(default=None, max_length=MAX_EMAIL)


def _site_kind(body: Any) -> str:
    kind = body.get("kind") if isinstance(body, dict) else getattr(body, "kind", None)
    return kind if kind in ("like", "report") else "comment"


SiteFeedbackRequest = Annotated[
    Annotated[CommentRequest, Tag("comment")] | Annotated[PageLikeRequest, Tag("like")] | Annotated[PageReportRequest, Tag("report")],
    Discriminator(_site_kind),
]


class CloseRequest(BaseModel):
    outcome: str
    note: str | None = Field(default=None, max_length=MAX_COMMENT)


def _blank_to_none(value: str | None) -> str | None:
    value = (value or "").strip()
    return value or None


def _voice_turn(transcript: list[dict], turn_index: int) -> dict:
    if turn_index >= len(transcript) or not isinstance(transcript[turn_index], dict) or "citations" not in transcript[turn_index]:
        raise HTTPException(status_code=400, detail="turn_index does not point to a Representative reply")
    return transcript[turn_index]


def _cited_ids(citations: list[dict]) -> list[str]:
    return list(dict.fromkeys(rid for c in citations or [] for rid in c.get("record_ids") or []))


def sentence_basis(turn: dict, sentence_index: int | None) -> tuple[list[str], dict]:
    """The record ids, and each one's confidence, behind one sentence of a
    voice turn, or behind the whole turn when no sentence is named. The plan's
    elements placed on the sentence come first; the citations whose sentence
    lies inside the sentence's span add the records the plan holds only as
    end-of-reply references."""
    plan = turn.get("transparency") or {}
    citations = turn.get("citations") or []
    confidence_of = {
        card.get("record_id"): card.get("confidence")
        for card in (plan.get("references") or []) + (plan.get("elements") or [])
        if card.get("record_id") and card.get("confidence") is not None
    }
    if sentence_index is None:
        ids = _cited_ids(citations)
    else:
        spans = plan.get("sentences") or []
        span = next((s for s in spans if s.get("index") == sentence_index), None)
        if span is None:
            raise HTTPException(status_code=400, detail="sentence_index is not a sentence of that reply")
        ids = []
        for element in plan.get("elements") or []:
            if element.get("sentence_index") == sentence_index and element.get("record_id"):
                ids.append(element["record_id"])
        text = turn.get("text") or ""
        start, end = span.get("text_start"), span.get("text_end")
        if start is not None and end is not None:
            inside = text[start:end]
            for citation in citations:
                said = (citation.get("sentence") or "").strip()
                if said and said in inside:
                    ids.extend(citation.get("record_ids") or [])
        ids = list(dict.fromkeys(ids))
    return ids, {rid: confidence_of[rid] for rid in ids if confidence_of.get(rid) is not None}


def install(
    app: FastAPI,
    *,
    store: FeedbackStore | None,
    authenticate_session: Callable[[Request, str, str | None], object],
    transcript_of: Callable[[Request, str], list[dict]],
    authenticate_admin: Callable[[Request, str | None], None],
    site_origin: str | None,
) -> None:
    def _enabled() -> FeedbackStore:
        if store is None:
            raise HTTPException(status_code=404)
        return store

    def _cors(request: Request, response: Response) -> None:
        origin = request.headers.get("origin")
        if site_origin and origin == site_origin:
            response.headers["Access-Control-Allow-Origin"] = origin
            response.headers["Vary"] = "Origin"

    @app.post("/api/session/{session_id}/feedback", status_code=201)
    def session_feedback(
        session_id: str, req: SessionFeedbackRequest, request: Request, response: Response,
        authorization: str | None = Header(default=None),
    ):
        """A like or a flag on one Representative reply, authorised by the
        session's own code. A repeated like on the same reply answers 200 with
        the first one's id."""
        store = _enabled()
        authenticate_session(request, session_id, authorization)
        turn = _voice_turn(transcript_of(request, session_id), req.turn_index)
        if req.kind == "flag" and req.reason is None:
            raise HTTPException(status_code=400, detail="a flag needs a reason")
        if req.kind == "like":
            existing = store.like_id(session_id, req.turn_index)
            if existing is not None:
                response.status_code = 200
                return {"id": existing}
        sentence_index = req.sentence_index if req.kind == "flag" else None
        record_ids, confidence = sentence_basis(turn, sentence_index)
        item_id = store.add({
            "kind": req.kind, "page": turn.get("speaker"), "session_id": session_id, "turn_index": req.turn_index,
            "sentence_index": sentence_index, "record_ids": record_ids, "confidence": confidence,
            "reason": req.reason if req.kind == "flag" else None,
            "text": _blank_to_none(req.text) if req.kind == "flag" else None,
            "email": _blank_to_none(req.email) if req.kind == "flag" else None,
        })
        return {"id": item_id}

    @app.options("/api/feedback")
    def comment_preflight(request: Request, response: Response):
        _enabled()
        _cors(request, response)
        response.headers["Access-Control-Allow-Methods"] = "POST"
        response.headers["Access-Control-Allow-Headers"] = "content-type"
        response.headers["Access-Control-Max-Age"] = "600"
        response.status_code = 204

    @app.post("/api/feedback", status_code=201)
    def comment(req: SiteFeedbackRequest, request: Request, response: Response):
        """A comment about the experience, or a like or a report on one page,
        from the app or the public site. None of them needs a session."""
        store = _enabled()
        _cors(request, response)
        if isinstance(req, PageLikeRequest):
            return {"id": store.add({"kind": "like", "page": req.page})}
        if isinstance(req, PageReportRequest):
            text = _blank_to_none(req.text)
            if text is None:
                raise HTTPException(status_code=422, detail="text is required")
            return {"id": store.add({
                "kind": "report", "page": req.page, "reason": req.reason, "text": text, "email": _blank_to_none(req.email),
            })}
        text = _blank_to_none(req.text)
        page = _blank_to_none(req.page)
        if text is None or page is None:
            raise HTTPException(status_code=422, detail="page and text are required")
        item_id = store.add({
            "kind": "comment", "page": page, "text": text, "quote_consent": req.quote_consent,
            "first_name": _blank_to_none(req.first_name) if req.quote_consent == "first_name" else None,
            "email": _blank_to_none(req.email),
        })
        return {"id": item_id}

    @app.get("/api/admin/feedback")
    def list_feedback(request: Request, status: Literal["open", "closed"] = "open", authorization: str | None = Header(default=None)):
        store = _enabled()
        authenticate_admin(request, authorization)
        return {"items": store.list_open() if status == "open" else store.list_closed()}

    @app.post("/api/admin/feedback/{item_id}/close")
    def close_feedback(item_id: str, req: CloseRequest, request: Request, authorization: str | None = Header(default=None)):
        store = _enabled()
        authenticate_admin(request, authorization)
        guard_admin_change(request, authorization)
        if req.outcome not in OUTCOMES:
            raise HTTPException(status_code=400, detail=f"outcome must be one of {', '.join(OUTCOMES)}")
        if not store.close(item_id, req.outcome, _blank_to_none(req.note)):
            raise HTTPException(status_code=404, detail="no waiting item with that id")
        return store.get(item_id)
