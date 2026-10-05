"""The quality-control store, its scrubber and the retention job."""
import sqlite3
from datetime import date, datetime, timedelta, timezone

from engine.m4.store import Store
from engine.m7 import retention
from engine.m7.qc_scrub import known_names, scrub
from engine.m7.qc_store import QCStore, iso_week

FORBIDDEN = {"session_id", "visitor_id", "code_hash", "session_code", "ip", "created_at", "timestamp", "trace_id", "user", "email"}


def _row(store, token="t1", round_no=1, day=date(2026, 10, 3), answer="An answer."):
    store.write_turn(conversation_token=token, round_no=round_no, world="alx", package_hash="sha256:x", model_id="m",
                     routing="voice_pass_through", flags={"text_free": False}, question_text="A question?",
                     answer_text=answer, marks={}, scores={}, day=day)


def test_the_schema_has_no_column_that_leads_to_a_person(tmp_path):
    store = QCStore(tmp_path / "qc.db")
    cols = {r[1] for r in sqlite3.connect(store.db_path).execute("PRAGMA table_info(qc_turn)")}
    assert not cols & FORBIDDEN
    assert "week" in cols and "conversation_token" in cols


def test_the_qc_store_shares_no_column_name_with_the_event_log(tmp_path):
    events = Store(tmp_path / "events.db")
    qc = QCStore(tmp_path / "qc.db")
    ev_cols = {r[1] for r in sqlite3.connect(events.db_path).execute("PRAGMA table_info(session_events)")}
    qc_cols = {r[1] for r in sqlite3.connect(qc.db_path).execute("PRAGMA table_info(qc_turn)")}
    assert not ev_cols & qc_cols


def test_dates_are_weeks_never_times(tmp_path):
    store = QCStore(tmp_path / "qc.db")
    _row(store)
    assert store.rows()[0]["week"] == iso_week(date(2026, 10, 3)) == "2026-W40"


def test_answers_older_than_ninety_days_are_cleared_and_questions_kept(tmp_path):
    store = QCStore(tmp_path / "qc.db")
    today = date(2026, 10, 3)
    _row(store, token="old", day=today - timedelta(days=120))
    _row(store, token="new", day=today - timedelta(days=10))
    assert store.expire_answers(today) == 1
    rows = {r["conversation_token"]: r for r in store.rows()}
    assert rows["old"]["answer_text"] is None and rows["old"]["question_text"] == "A question?"
    assert rows["new"]["answer_text"] == "An answer."


def test_sampling_is_seeded_and_returns_whole_conversations(tmp_path):
    store = QCStore(tmp_path / "qc.db")
    for t in "abcd":
        _row(store, token=t, round_no=1)
        _row(store, token=t, round_no=2)
    first = store.sample_conversations("2026-W40", 2, seed=7)
    assert first == store.sample_conversations("2026-W40", 2, seed=7)
    assert len(first) == 2 and all(len(conv) == 2 for conv in first)


def test_purge_deletes_only_conversations_inactive_past_the_cutoff(tmp_path):
    events = Store(tmp_path / "events.db")
    events.append(session_id="s-old", event_uuid="u1", event_type="participant_message", payload={"text": "x"})
    events.append(session_id="s-new", event_uuid="u2", event_type="participant_message", payload={"text": "y"})
    with sqlite3.connect(events.db_path) as conn:
        conn.execute("UPDATE session_events SET created_at = '2026-01-01T00:00:00+00:00' WHERE session_id = 's-old'")
    assert events.purge_inactive("2026-06-01T00:00:00+00:00") == 1
    assert events.list_session_ids() == ["s-new"]


def test_purge_keeps_a_session_the_edge_says_is_exempt(tmp_path):
    events = Store(tmp_path / "events.db")
    for sid, uuid in (("s-saved", "u1"), ("s-anon", "u2")):
        events.append(session_id=sid, event_uuid=uuid, event_type="participant_message", payload={"text": "x"})
    with sqlite3.connect(events.db_path) as conn:
        conn.execute("UPDATE session_events SET created_at = '2026-01-01T00:00:00+00:00'")
    assert events.purge_inactive("2026-06-01T00:00:00+00:00", lambda sid: sid == "s-saved") == 1
    assert events.list_session_ids() == ["s-saved"]


def test_retention_exempts_none_by_default_and_passes_the_edge_hook_through(tmp_path):
    now = datetime(2026, 10, 3, tzinfo=timezone.utc)
    events, qc = Store(tmp_path / "events.db"), QCStore(tmp_path / "qc.db")
    for sid, uuid in (("s-saved", "u1"), ("s-anon", "u2")):
        events.append(session_id=sid, event_uuid=uuid, event_type="participant_message", payload={"text": "x"})
    with sqlite3.connect(events.db_path) as conn:
        conn.execute("UPDATE session_events SET created_at = '2026-01-01T00:00:00+00:00'")
    status = retention.run_once(events.db_path, qc.db_path, tmp_path / "status", now=now,
                                is_exempt=lambda sid: sid == "s-saved")
    assert status["conversations_deleted"] == 1 and events.list_session_ids() == ["s-saved"]
    assert retention.run_once(events.db_path, qc.db_path, tmp_path / "status", now=now)["conversations_deleted"] == 1
    assert events.list_session_ids() == []


def test_retention_run_records_its_counts(tmp_path):
    events, qc = Store(tmp_path / "events.db"), QCStore(tmp_path / "qc.db")
    _row(qc, day=date(2026, 1, 5))
    status = retention.run_once(events.db_path, qc.db_path, tmp_path / "status",
                                now=datetime(2026, 10, 3, tzinfo=timezone.utc))
    assert status["outcome"] == "ok" and status["qc_answers_cleared"] == 1 and status["conversations_deleted"] == 0
    assert (tmp_path / "status" / retention.STATUS_FILENAME).exists()


def test_scrub_removes_contacts_and_unknown_names_and_keeps_known_ones():
    known = known_names(["Jerome wrote to Paula at Bethlehem."])
    assert scrub("Maria says my husband John is wrong. What did Jerome think?", known) == \
        "[name] says my husband [name] is wrong. What did Jerome think?"
    assert scrub("Write to a.b@example.org, +44 20 7946 0958 or https://x.org/p", known) == \
        "Write to [email], [phone] or [link]"
    assert scrub("Why did Paula go to Bethlehem? I was raised Catholic.", known) == \
        "Why did Paula go to Bethlehem? I was raised Catholic."


def test_scrub_is_deterministic():
    text = "Tell me, Anna, about Jerome's letters."
    known = known_names(["Jerome"])
    assert scrub(text, known) == scrub(text, known) == "Tell me, [name], about Jerome's letters."


def test_retention_prunes_audit_runs_past_ninety_days(tmp_path):
    events, qc = Store(tmp_path / "events.db"), QCStore(tmp_path / "qc.db")
    root = tmp_path / "m7-audits"
    (root / "2026-06-01T03-17-00Z").mkdir(parents=True)
    (root / "2026-09-30T03-17-00Z").mkdir(parents=True)
    status = retention.run_once(events.db_path, qc.db_path, tmp_path / "status", audit_root=root,
                                now=datetime(2026, 10, 3, tzinfo=timezone.utc))
    assert status["audit_runs_pruned"] == 1
    assert [p.name for p in root.iterdir()] == ["2026-09-30T03-17-00Z"]
