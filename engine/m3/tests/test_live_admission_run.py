"""engine.m3.live_admission_run's own safety gates - never the live run
itself (that is real, billed Bedrock spend; this module must NEVER call
run() in a way that reaches a real network call). Every SystemExit case
here aborts before loader/client construction. The one case that runs
_run_world (the running-check trip) replaces it with a fake, so this
still never touches the network or needs credentials.
"""
import copy
import json
from types import SimpleNamespace

import pytest

import engine.m3.live_admission_run as lar
from engine.m3.generation import LivePathSettings
from engine.m3.live_admission_run import (
    DEFAULT_MAX_USD,
    estimate_world_cost_usd,
    live_path_turn_ceiling_usd,
    run,
)

SONNET = "us.anthropic.claude-sonnet-4-5-20250929-v1:0"
OPUS = "us.anthropic.claude-opus-5-5"


def test_default_max_usd_ceiling_is_three_dollars():
    assert DEFAULT_MAX_USD == pytest.approx(3.00)


def test_the_turn_ceiling_is_the_highest_measured_whole_turn_cost():
    assert live_path_turn_ceiling_usd() == pytest.approx(0.0696, abs=0.001)


def test_a_world_estimate_is_the_ceiling_for_every_probe():
    assert estimate_world_cost_usd(28, SONNET, ceiling_usd=0.05) == pytest.approx(1.40)


def test_a_voice_model_override_scales_the_estimate_by_its_output_price():
    assert estimate_world_cost_usd(28, OPUS, ceiling_usd=0.05) == pytest.approx(1.40 * 20 / 15)


def test_a_voice_model_with_no_approved_price_has_no_estimate():
    with pytest.raises(RuntimeError, match="no approved price"):
        estimate_world_cost_usd(28, "us.anthropic.claude-mystery", ceiling_usd=0.05)


def test_omitting_max_usd_falls_back_to_the_three_dollar_ceiling(monkeypatch):
    from engine.m1.registry import formation_world_keys

    monkeypatch.setattr(lar, "live_path_turn_ceiling_usd", lambda: 0.07)

    with pytest.raises(SystemExit, match="exceeds --max-usd"):
        run("us-east-1", world_keys=formation_world_keys(), authorized_by="test-harness")


def test_a_run_over_the_max_usd_ceiling_aborts_before_any_billed_call():
    with pytest.raises(SystemExit, match="exceeds --max-usd"):
        run("us-east-1", world_keys=["alx"], max_usd=0.01, authorized_by="test-harness")


def test_a_blank_authorized_by_aborts():
    generous_ceiling = 100.0
    with pytest.raises(SystemExit, match="--authorized-by is required"):
        run("us-east-1", world_keys=["alx"], max_usd=generous_ceiling, authorized_by="   ")


def test_an_unregistered_world_key_aborts_before_any_billed_call():
    generous_ceiling = 100.0
    with pytest.raises(SystemExit, match="not a real formation world"):
        run("us-east-1", world_keys=["not-a-real-world"], max_usd=generous_ceiling, authorized_by="test-harness")


def test_the_running_check_trips_even_when_preflight_passes(monkeypatch):
    """Real per-world cost can exceed its own preflight estimate - the
    running check (spend so far + next world's estimate vs. max_usd) is
    what actually protects a many-world run, not the preflight total
    alone. _run_world is faked here (a fixed, high actual_usd for the
    first world) rather than any network/client internals, so this stays
    fully hermetic - no real call is ever made."""
    monkeypatch.setattr(lar, "resolve_model_id", lambda model, region: "fake-model-id")

    def fake_run_world(world_key, **kwargs):
        # alx's REAL cost turns out to be far above its own $0.10 estimate.
        return {
            "battery_size": 1, "pass_count": 1, "overall_pass": True, "per_probe": [],
            "actual_usd": 5.00,
            "total_input_tokens": 0, "total_output_tokens": 0,
            "total_cache_creation_input_tokens": 0, "total_cache_read_input_tokens": 0,
        }

    monkeypatch.setattr(lar, "_run_world", fake_run_world)

    # preflight passes: 0.10 + 0.10 = 0.20, well under max_usd=1.00
    report = run("us-east-1", world_keys=["alx", "desert"], max_usd=1.00, authorized_by="test-harness")

    assert report["estimated_usd_preflight"] == pytest.approx(0.20)
    assert "alx" in report["worlds"]
    assert "desert" not in report["worlds"]  # stopped before desert's own billed calls
    assert report["aborted_reason"] is not None
    assert "desert" in report["aborted_reason"]
    assert report["overall_pass"] is False
    assert report["actual_usd_spent"] == pytest.approx(5.00)


class _FakeStreamCtx:
    def __init__(self, chunks):
        self._chunks = chunks

    def __enter__(self):
        usage = SimpleNamespace(input_tokens=100, output_tokens=20, cache_creation_input_tokens=0, cache_read_input_tokens=0)
        message = SimpleNamespace(usage=usage, content=[SimpleNamespace(type="text", text="".join(self._chunks))], stop_reason="end_turn")
        return SimpleNamespace(text_stream=iter(self._chunks), get_final_message=lambda: message)

    def __exit__(self, *exc):
        return False


_GATE_OUTPUT = {
    "submit_safety_classification": {"signal": "NO_SIGNAL", "acute_level": "none", "risk_subject": "not_applicable",
                                     "check_in_reason": "not_applicable", "dynamic_tags": [], "confidence": "high"},
    "submit_reader_output": {"asks": [{"order": 1, "text": "what the world held"}], "register": "informational", "clarity": "clear",
                             "ambiguity_options": [], "out_of_scope": {"class": "none"}, "modern_terms": []},
}


class _FakeClient:
    """Answers the gate calls with fixed tool output and every voice call
    with the same tagged reply, no network."""

    def __init__(self, record_id):
        chunks = ["We hold this, ", f"as our teachers wrote. [[{record_id}]]"]
        usage = SimpleNamespace(input_tokens=100, output_tokens=20, cache_creation_input_tokens=0, cache_read_input_tokens=0)

        class _Messages:
            def stream(self, **kwargs):
                return _FakeStreamCtx(chunks)

            def create(self, *, tool_choice, **kwargs):
                name = tool_choice["name"]
                block = SimpleNamespace(type="tool_use", name=name, input=copy.deepcopy(_GATE_OUTPUT[name]))
                return SimpleNamespace(content=[block], usage=usage)

        self.messages = _Messages()


_SETTINGS = LivePathSettings(
    voice_model_id="us.anthropic.claude-sonnet-4-5-20250929-v1:0", safety_model_id="us.anthropic.claude-haiku-4-5-20251001-v1:0",
    r27_enforce=False, self_revision_enabled=False, citation_attach_enabled=False,
)


@pytest.fixture(autouse=True)
def _small_turn_ceiling(monkeypatch):
    monkeypatch.setattr(lar, "live_path_turn_ceiling_usd", lambda: 0.1 / 28)


def _run_alx_with_fake_client(monkeypatch, save_transcripts, answers_path=None):
    from engine.m1.loader import load_world_records
    from engine.m1.registry import load_registry
    from engine.m4.world_loader import LazyWorldLoader

    record_id = next(rid for rid, r in load_world_records("alx").items() if r.get("record_type") == "quote")
    monkeypatch.setattr(lar, "make_client", lambda region: _FakeClient(record_id))
    return lar._run_world(
        "alx", registry=load_registry(), loader=LazyWorldLoader(), settings=_SETTINGS,
        region="us-east-1", save_transcripts=save_transcripts, answers_path=answers_path,
    )


def test_save_transcripts_keeps_every_probe_and_leaves_grading_unchanged(monkeypatch):
    plain = _run_alx_with_fake_client(monkeypatch, save_transcripts=False)
    saved = _run_alx_with_fake_client(monkeypatch, save_transcripts=True)

    assert all("transcript" not in p for p in plain["per_probe"])
    assert len(saved["per_probe"]) == saved["battery_size"]
    for a, b in zip(plain["per_probe"], saved["per_probe"]):
        assert (a["probe_id"], a["passed"], a["checks"], a["usage"]) == (b["probe_id"], b["passed"], b["checks"], b["usage"])
    assert (plain["pass_count"], plain["overall_pass"]) == (saved["pass_count"], saved["overall_pass"])

    transcript = saved["per_probe"][0]["transcript"]
    draft = transcript["drafts"][0]
    assert draft["raw_text"].endswith("]]")
    assert draft["request"] == {"model": _SETTINGS.voice_model_id, "max_tokens": 2048}
    assert draft["stop_reason"] == "end_turn"
    assert draft["seconds_to_first_text"] is not None and draft["seconds_total"] is not None
    assert transcript["routing_action"] == "voice_with_directive"
    assert transcript["reader"]["directive"]["asks"][0]["text"] == "what the world held"
    assert isinstance(transcript["citations"], list) and transcript["answer_text"]
    assert {u["call_kind"] for u in transcript["usage"]} == {"safety_call", "reader_call", "voice_generation"}


def test_each_answer_is_written_to_the_answers_file_as_it_returns(monkeypatch, tmp_path):
    answers_path = tmp_path / "run.json.answers.jsonl"
    saved = _run_alx_with_fake_client(monkeypatch, save_transcripts=True, answers_path=answers_path)

    lines = [json.loads(line) for line in answers_path.read_text(encoding="utf-8").splitlines()]
    assert [line["index"] for line in lines] == list(range(saved["battery_size"]))
    assert [line["answer_text"] for line in lines] == [p["transcript"]["answer_text"] for p in saved["per_probe"]]


def test_settings_only_exits_before_any_billed_call(monkeypatch, capsys):
    monkeypatch.setattr(lar, "resolve_model_id", lambda model, region: "fake-model-id")
    monkeypatch.setattr(lar, "_run_world", lambda *a, **k: pytest.fail("billed call made under --settings-only"))
    generous_ceiling = 100.0
    report = run("us-east-1", world_keys=["alx"], max_usd=generous_ceiling, authorized_by="test-harness",
                 save_transcripts=True, settings_only=True)

    settings = report["run_settings"]
    assert settings["voice_model_id"] == "fake-model-id"
    assert settings["safety_model_id"] == "fake-model-id"
    assert settings["self_revision_enabled"] is False
    assert settings["path"].startswith("engine.m4.turn.run_turn")
    assert settings["seal_hash"].startswith("sha256:")
    assert set(settings["package_manifest_hash"]) == {"alx"}
    assert settings["save_transcripts"] is True
    assert '"run_settings"' in capsys.readouterr().err


def _fake_world_result(cost: float) -> dict:
    return {
        "battery_size": 1, "pass_count": 1, "overall_pass": True, "per_probe": [],
        "actual_usd": cost, "unanswered": 0, "priced_from_usage_usd": cost,
    }


def test_a_cap_stop_part_way_through_a_world_keeps_the_worlds_already_run(monkeypatch, tmp_path):
    """The live-test guard refuses a call that could pass the cap by raising
    LiveTestCapReached from inside a world's own battery. The 20 October
    fleet run lost ten completed worlds that way, because the exception
    left run() before any report was written. Now the completed worlds
    stay in the report, the stop is named, and the report is on disk."""
    from engine.provider import guard

    monkeypatch.setattr(lar, "resolve_model_id", lambda model, region: "fake-model-id")

    def fake_run_world(world_key, **kwargs):
        if world_key == "desert":
            raise guard.LiveTestCapReached("live test 'x': the next call could pass the $1.00 cap")
        return _fake_world_result(0.40)

    monkeypatch.setattr(lar, "_run_world", fake_run_world)
    out = tmp_path / "report.json"

    report = run("us-east-1", world_keys=["alx", "desert"], max_usd=1.00, authorized_by="test-harness", report_path=out)

    assert list(report["worlds"]) == ["alx"]
    assert report["overall_pass"] is False
    assert "desert" in report["aborted_reason"] and "cap" in report["aborted_reason"]
    assert report["actual_usd_spent"] == pytest.approx(0.40)
    on_disk = json.loads(out.read_text(encoding="utf-8"))
    assert list(on_disk["worlds"]) == ["alx"]
    assert on_disk["aborted_reason"] == report["aborted_reason"]


def test_the_report_is_written_after_every_world(monkeypatch, tmp_path):
    """A crash or a kill between worlds must not lose the worlds already
    paid for: the report on disk is refreshed after each one, marked in
    progress until the run ends."""
    monkeypatch.setattr(lar, "resolve_model_id", lambda model, region: "fake-model-id")
    out = tmp_path / "report.json"
    seen = []

    def fake_run_world(world_key, **kwargs):
        if out.exists():
            seen.append((world_key, json.loads(out.read_text(encoding="utf-8"))))
        return _fake_world_result(0.10)

    monkeypatch.setattr(lar, "_run_world", fake_run_world)

    report = run("us-east-1", world_keys=["alx", "desert"], max_usd=1.00, authorized_by="test-harness", report_path=out)

    # when desert started, alx's result was already on disk and marked in progress
    assert [w for w, _ in seen] == ["desert"]
    assert list(seen[0][1]["worlds"]) == ["alx"]
    assert seen[0][1]["aborted_reason"].startswith("in progress")
    # the final file is the finished report
    final = json.loads(out.read_text(encoding="utf-8"))
    assert list(final["worlds"]) == ["alx", "desert"]
    assert final["aborted_reason"] is None
    assert final["overall_pass"] is True and report["overall_pass"] is True
