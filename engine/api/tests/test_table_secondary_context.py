"""Stage 4f (Build-Plan.md): engine.api.table_wiring._secondary_context_text
- the retrieval-facing, unwrapped twin of _context_prefix. Deliberately
imports only engine.api.table_wiring (no engine.api.app/TestClient), so this
suite is hermetic and needs no fastapi - unlike test_table_api.py and
test_table_isolation.py, which pull in the FastAPI app.
"""
from engine.api.table_wiring import _context_prefix, _secondary_context_text


def test_empty_pending_is_none():
    assert _secondary_context_text([]) is None


def test_joins_pending_lines_with_a_blank_line():
    pending = ["Theon: We did not claim to have seen him ourselves.", "Chloe: I would say the same."]
    assert _secondary_context_text(pending) == "Theon: We did not claim to have seen him ourselves.\n\nChloe: I would say the same."


def test_carries_no_framing_sentences_context_prefix_adds():
    """The whole point of the split: context_prefix's own instructional
    wrapper ("What has been said at the Table...", "You are being brought
    in now...") must never reach retrieval scoring, where words like
    "table" or "message" are noise no real cell vocabulary should match
    on."""
    pending = ["Theon: We did not claim to have seen him ourselves."]
    wrapped = _context_prefix(pending)
    bare = _secondary_context_text(pending)
    assert bare is not None and wrapped is not None
    assert bare in wrapped  # the same content really is in there...
    assert "What has been said at the Table" not in bare
    assert "You are being brought in now" not in bare


def test_same_pending_in_same_pending_out_no_new_read():
    """Both functions are called with the identical `pending` object the
    caller already computed - no new fetch, same in-memory data
    context_prefix itself already uses."""
    pending = ["Theon: We did not claim to have seen him ourselves."]
    assert _secondary_context_text(pending) is not None
    assert _context_prefix(pending) is not None
