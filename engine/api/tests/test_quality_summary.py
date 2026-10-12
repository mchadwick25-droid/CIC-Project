"""wiring of /api/admin/quality-summary: totals only, no participant text."""
import json
from datetime import date
from types import SimpleNamespace

from fastapi.testclient import TestClient

from engine.api.app import create_app
from engine.api.quality_summary import get_quality_summary
from engine.api.tests.test_table_api import _table_client
from engine.m7.qc_store import QCStore


def _write(store, token, round_no, world, *, text_free=False, degraded=False, cited=2, attached=1, question="a private question"):
    store.write_turn(
        conversation_token=token, round_no=round_no, world=world, package_hash="h", model_id="m", routing="voice",
        flags={"text_free": text_free, "safety_signal": "ACUTE_DISTRESS" if text_free else "NONE"},
        question_text=None if text_free else question, answer_text=None if text_free else "a private answer",
        marks={"cited_sentences": cited, "attached_sentences": attached},
        scores={"degraded_by_net": degraded, "horizon_mentions": 1}, day=date(2026, 10, 12),
    )


def test_empty_store_and_no_audit_return_zeros(tmp_path):
    summary = get_quality_summary(QCStore(tmp_path / "qc.db"), tmp_path / "missing")
    assert summary["turns"] == 0
    assert summary["by_world"] == []
    assert summary["audit"] is None


def test_no_store_at_all_returns_zeros():
    assert get_quality_summary(None)["turns"] == 0


def test_totals_by_world(tmp_path):
    store = QCStore(tmp_path / "qc.db")
    _write(store, "t1", 1, "desert")
    _write(store, "t1", 2, "desert", degraded=True)
    _write(store, "t2", 1, "desert", text_free=True)
    _write(store, "t3", 1, "syr")
    summary = get_quality_summary(store)
    desert = next(w for w in summary["by_world"] if w["world"] == "desert")
    assert summary["turns"] == 4 and summary["text_free_turns"] == 1
    assert desert["turns"] == 3 and desert["conversations"] == 2
    assert desert["degraded_turns"] == 1 and desert["text_free_turns"] == 1
    assert desert["cited_sentences"] == 6 and desert["attached_sentences"] == 3
    assert summary["by_world"][0]["world"] == "desert"
    assert summary["weeks"] == ["2026-W42"]


def test_the_latest_audit_rollup_is_read_not_recomputed(tmp_path):
    run_dir = tmp_path / "2026-10-12T03-00-00Z"
    run_dir.mkdir()
    (run_dir / "fleet-rollup.json").write_text(json.dumps({
        "sessions_audited": 5, "findings_by_severity": {"defect": 1}, "findings_by_instrument": {"uncited": 1},
        "register": {"mean_fk_grade": 9.1, "mean_fre": 63.0},
    }))
    (tmp_path / "last_run.json").write_text(json.dumps({"run_at": "2026-10-12T03:00:00+00:00", "out_dir": str(run_dir)}))
    audit = get_quality_summary(None, tmp_path)["audit"]
    assert audit["sessions_audited"] == 5
    assert audit["findings_by_severity"] == {"defect": 1}
    assert audit["reading"]["mean_fk_grade"] == 9.1


def test_a_malformed_rollup_degrades_to_none(tmp_path):
    (tmp_path / "last_run.json").write_text("not json")
    assert get_quality_summary(None, tmp_path)["audit"] is None


def _app(store, usage_store, world_loader, registry, *, qc_store=None, token=None):
    client = _table_client(selector_script=[], stream_scripts=[])
    return create_app(
        voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
        store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, default_world_key="fix",
        admin_token=token, qc_recorder=SimpleNamespace(store=qc_store) if qc_store else None,
    )


def test_endpoint_404s_without_admin_token(store, usage_store, world_loader, registry):
    http = TestClient(_app(store, usage_store, world_loader, registry))
    assert http.get("/api/admin/quality-summary", headers={"Authorization": "Bearer anything"}).status_code == 404


def test_endpoint_returns_counts_and_never_text(store, usage_store, world_loader, registry, tmp_path):
    qc = QCStore(tmp_path / "qc.db")
    _write(qc, "t1", 1, "desert")
    token = "the-real-token-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    http = TestClient(_app(store, usage_store, world_loader, registry, qc_store=qc, token=token))
    resp = http.get("/api/admin/quality-summary", headers={"Authorization": f"Bearer {token}"})
    assert resp.status_code == 200
    body = resp.json()
    assert body["turns"] == 1 and body["by_world"][0]["world"] == "desert"
    assert "private" not in resp.text and "t1" not in resp.text


def test_endpoint_without_a_qc_recorder_returns_zeros(store, usage_store, world_loader, registry):
    token = "the-real-token-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    http = TestClient(_app(store, usage_store, world_loader, registry, token=token))
    assert http.get("/api/admin/quality-summary", headers={"Authorization": f"Bearer {token}"}).json()["turns"] == 0
