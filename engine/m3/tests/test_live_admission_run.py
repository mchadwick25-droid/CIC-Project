"""engine.m3.live_admission_run's own safety gates - never the live run
itself (that is real, billed Bedrock spend; this module must NEVER call
run() in a way that reaches a real network call). Every SystemExit case
here aborts before loader/client construction. The one case that runs
_run_world (the running-check trip) replaces it with a fake, so this
still never touches the network or needs credentials.
"""
import pytest

import engine.m3.live_admission_run as lar
from engine.m3.live_admission_run import (
    DEFAULT_MAX_USD,
    estimate_run_cost_usd,
    estimate_world_cost_usd,
    real_world_costs,
    run,
)

REAL_COSTS = real_world_costs()


def test_default_max_usd_ceiling_is_three_dollars():
    assert DEFAULT_MAX_USD == pytest.approx(3.00)


def test_a_world_with_a_real_report_uses_its_own_latest_observed_cost():
    assert "don" in REAL_COSTS  # real reports exist for don
    assert estimate_world_cost_usd("don", REAL_COSTS) == pytest.approx(REAL_COSTS["don"])


def test_a_world_with_no_real_report_falls_back_to_the_highest_observed_cost():
    fake_costs = {"alx": 0.10, "desert": 0.90}
    assert estimate_world_cost_usd("rzg", fake_costs) == pytest.approx(0.90)


def test_estimate_run_cost_usd_sums_each_worlds_own_estimate():
    fake_costs = {"alx": 0.10, "desert": 0.90}
    total = estimate_run_cost_usd(["alx", "desert"], fake_costs)
    assert total == pytest.approx(1.00)


def test_omitting_max_usd_falls_back_to_the_three_dollar_ceiling():
    """The ceiling is the default itself, not an opt-in: requesting every
    formation world (a real, expensive combination) aborts even when
    --max-usd is never named on the command line."""
    from engine.m1.registry import formation_world_keys

    worlds = formation_world_keys()
    assert estimate_run_cost_usd(worlds, REAL_COSTS) > DEFAULT_MAX_USD
    with pytest.raises(SystemExit, match="exceeds --max-usd"):
        run("us-east-1", world_keys=worlds, authorized_by="test-harness")


def test_a_run_over_the_max_usd_ceiling_aborts_before_any_billed_call():
    tiny_ceiling = estimate_run_cost_usd(["alx"], REAL_COSTS) / 2
    with pytest.raises(SystemExit, match="exceeds --max-usd"):
        run("us-east-1", world_keys=["alx"], max_usd=tiny_ceiling, authorized_by="test-harness")


def test_a_blank_authorized_by_aborts():
    generous_ceiling = estimate_run_cost_usd(["alx"], REAL_COSTS) * 100
    with pytest.raises(SystemExit, match="--authorized-by is required"):
        run("us-east-1", world_keys=["alx"], max_usd=generous_ceiling, authorized_by="   ")


def test_an_unregistered_world_key_aborts_before_any_billed_call():
    generous_ceiling = estimate_run_cost_usd(["alx"], REAL_COSTS) * 100
    with pytest.raises(SystemExit, match="not a real formation world"):
        run("us-east-1", world_keys=["not-a-real-world"], max_usd=generous_ceiling, authorized_by="test-harness")


def test_the_running_check_trips_even_when_preflight_passes(monkeypatch):
    """Real per-world cost can exceed its own preflight estimate - the
    running check (spend so far + next world's estimate vs. max_usd) is
    what actually protects a many-world run, not the preflight total
    alone. _run_world is faked here (a fixed, high actual_usd for the
    first world) rather than any network/client internals, so this stays
    fully hermetic - no real call is ever made."""
    fake_costs = {"alx": 0.10, "desert": 0.10}
    monkeypatch.setattr(lar, "real_world_costs", lambda: fake_costs)
    monkeypatch.setattr(lar, "resolve_model_id", lambda model, region: "fake-model-id")
    monkeypatch.setattr(lar, "load_fleet_records", lambda: {})

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


class _FakeStream:
    def __init__(self, chunks):
        self.text_stream = iter(chunks)
        self._text = "".join(chunks)

    def get_final_message(self):
        class _Usage:
            input_tokens, output_tokens = 100, 20
            cache_creation_input_tokens, cache_read_input_tokens = 0, 0

        class _Block:
            type = "text"

        block = _Block()
        block.text = self._text

        class _Message:
            usage = _Usage()
            content = [block]
            stop_reason = "end_turn"

        return _Message()


class _FakeStreamCtx:
    def __init__(self, chunks):
        self._chunks = chunks

    def __enter__(self):
        return _FakeStream(self._chunks)

    def __exit__(self, *exc):
        return False


class _FakeClient:
    """Answers every voice call with the same tagged reply, no network."""

    def __init__(self, record_id):
        chunks = ["We hold this, ", f"as our teachers wrote. [[{record_id}]]"]

        class _Messages:
            def stream(self, **kwargs):
                return _FakeStreamCtx(chunks)

        self.messages = _Messages()


def _run_alx_with_fake_client(monkeypatch, save_transcripts):
    from engine.m1.loader import load_world_records
    from engine.m1.registry import load_registry
    from engine.m4.world_loader import LazyWorldLoader

    record_id = next(rid for rid, r in load_world_records("alx").items() if r.get("record_type") == "quote")
    monkeypatch.setattr(lar, "make_client", lambda region: _FakeClient(record_id))
    return lar._run_world(
        "alx", registry=load_registry(), loader=LazyWorldLoader(), voice_model_id="fake-model-id",
        region="us-east-1", canon_questions=lar.load_fleet_records(), save_transcripts=save_transcripts,
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
    assert transcript["raw_text"].endswith("]]")
    assert transcript["request"] == {"model": "fake-model-id", "max_tokens": 1024}
    assert transcript["stop_reason"] == "end_turn"
    assert transcript["seconds_to_first_text"] is not None and transcript["seconds_total"] is not None
    assert isinstance(transcript["citations"], list) and transcript["answer_text"]


def test_settings_only_exits_before_any_billed_call(monkeypatch, capsys):
    monkeypatch.setattr(lar, "resolve_model_id", lambda model, region: "fake-model-id")
    monkeypatch.setattr(lar, "_run_world", lambda *a, **k: pytest.fail("billed call made under --settings-only"))
    generous_ceiling = estimate_run_cost_usd(["alx"], REAL_COSTS) * 100
    report = run("us-east-1", world_keys=["alx"], max_usd=generous_ceiling, authorized_by="test-harness",
                 save_transcripts=True, settings_only=True)

    settings = report["run_settings"]
    assert settings["voice_model_id"] == "fake-model-id"
    assert settings["self_revision"].startswith("off")
    assert settings["safety_model_id"] is None
    assert settings["seal_hash"].startswith("sha256:")
    assert set(settings["package_manifest_hash"]) == {"alx"}
    assert settings["save_transcripts"] is True
    assert '"run_settings"' in capsys.readouterr().err
