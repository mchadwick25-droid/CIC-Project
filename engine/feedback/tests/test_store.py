"""engine.feedback.store: the rows, the close that clears the email, and the purge."""
import sqlite3
from datetime import datetime, timedelta, timezone

import pytest

from engine.feedback.store import FeedbackStore


@pytest.fixture
def feedback(tmp_path):
    return FeedbackStore(tmp_path / "feedback.db")


def test_add_stores_a_flag_with_its_pointer(feedback):
    item_id = feedback.add({
        "kind": "flag", "page": "fix", "session_id": "s", "turn_index": 2, "sentence_index": 1,
        "record_ids": ["a", "b"], "confidence": {"a": "Documented"}, "reason": "overcertain", "text": "line", "email": "x@y.org",
    })
    item = feedback.get(item_id)
    assert item["record_ids"] == ["a", "b"] and item["confidence"] == {"a": "Documented"}
    assert item["created_at"] and item["closed_at"] is None and item["outcome"] is None
    assert [i["id"] for i in feedback.list_open()] == [item_id]


def test_the_table_refuses_values_outside_the_fixed_sets(feedback):
    for bad in ({"kind": "rant"}, {"kind": "flag", "reason": "rude"}, {"kind": "comment", "quote_consent": "maybe"}):
        with pytest.raises(sqlite3.IntegrityError):
            feedback.add(bad)


def test_likes_are_found_per_session_and_turn_and_stay_out_of_the_queue(feedback):
    like = feedback.add({"kind": "like", "session_id": "s", "turn_index": 3})
    assert feedback.like_exists("s", 3) and feedback.like_id("s", 3) == like
    assert not feedback.like_exists("s", 4) and not feedback.like_exists("t", 3)
    assert feedback.list_open() == []


def test_close_sets_the_outcome_clears_the_email_and_keeps_the_first_name(feedback):
    item_id = feedback.add({"kind": "comment", "page": "p", "text": "t", "email": "x@y.org", "quote_consent": "first_name", "first_name": "Ana"})
    assert feedback.close(item_id, "open_lead", "see gap 12") is True
    item = feedback.get(item_id)
    assert item["email"] is None and item["first_name"] == "Ana" and item["outcome"] == "open_lead" and item["outcome_note"] == "see gap 12"
    assert item["closed_at"] and feedback.list_open() == [] and [i["id"] for i in feedback.list_closed()] == [item_id]
    assert feedback.close(item_id, "no_action", None) is False
    assert feedback.close("missing", "no_action", None) is False
    with pytest.raises(ValueError):
        feedback.close(item_id, "deleted", None)


def test_list_closed_is_newest_first_and_limited(feedback):
    ids = [feedback.add({"kind": "comment", "page": "p", "text": str(n)}) for n in range(3)]
    for item_id in ids:
        feedback.close(item_id, "no_action", None)
    assert [i["id"] for i in feedback.list_closed(limit=2)] == ids[::-1][:2]


def test_purge_removes_old_closed_items_and_old_likes_and_keeps_open_ones(feedback):
    now = datetime(2026, 10, 16, tzinfo=timezone.utc)
    old_closed = feedback.add({"kind": "comment", "page": "p", "text": "a"})
    recent_closed = feedback.add({"kind": "comment", "page": "p", "text": "b"})
    old_open = feedback.add({"kind": "comment", "page": "p", "text": "c"})
    old_like = feedback.add({"kind": "like", "session_id": "s", "turn_index": 1})
    new_like = feedback.add({"kind": "like", "session_id": "s", "turn_index": 2})
    feedback.close(old_closed, "no_action", None)
    feedback.close(recent_closed, "no_action", None)
    long_ago, recently = (now - timedelta(days=100)).isoformat(), (now - timedelta(days=10)).isoformat()
    with sqlite3.connect(feedback.db_path) as conn:
        conn.execute("UPDATE feedback SET created_at = ?", (long_ago,))
        conn.execute("UPDATE feedback SET created_at = ? WHERE id = ?", (recently, new_like))
        conn.execute("UPDATE feedback SET closed_at = ? WHERE id = ?", (long_ago, old_closed))
        conn.execute("UPDATE feedback SET closed_at = ? WHERE id = ?", (recently, recent_closed))
    assert feedback.purge_closed_older_than(90, now=now) == 2
    assert feedback.get(old_closed) is None and feedback.get(old_like) is None
    assert all(feedback.get(i) is not None for i in (recent_closed, old_open, new_like))
