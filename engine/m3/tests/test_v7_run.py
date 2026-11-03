"""engine.m3.v7_run with no model call: voice calls are answered from reply
files or from a fake SDK client behind the real live-test guard, and the live
client builder fails the test unless a test replaces it on purpose."""
import inspect
import json
import subprocess
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest
from anthropic import APITimeoutError

import engine.m3.v7_run as v7
from engine.m1.loader import RECORDS_ROOT, load_fleet_records
from engine.m1.registry import load_registry
from engine.m3 import protocol, sealed_probes
from engine.m4 import evidence as m4_evidence
from engine.m4.story_placement import with_placeable_stories
from engine.m4.world_loader import LazyWorldLoader
from engine.m8.cost import estimate_cost
from engine.m8.price_tables import price_for_route
from engine.provider import guard
from engine.provider.bedrock import NormalizedUsage
from engine.shape import shape_text

try:
    import httpx2 as _http
except ImportError:
    import httpx as _http

WORLD = "alx"
MODEL = "us.anthropic.claude-sonnet-4-5-20250929-v1:0"
ADDED = "\nADDED"
RECORD_FIELDS = {
    "probe_id", "cell", "arm", "world", "error", "passed", "checks", "answer_text", "raw_text", "citations", "citation_entries",
    "offered_record_ids", "usage", "seconds_to_first_text", "seconds_total", "stop_reason", "attempts", "priced_usd",
    "priced_includes_failed_holds", "voice_model_id", "voice_max_tokens", "region", "package_manifest_hash", "repo_commit",
    "additions_chars", "evidence_chars", "evidence_chars_flag_off", "whole_world_signal", "reading_additions",
}
SETTINGS_FIELDS = {
    "voice_model_id", "voice_max_tokens", "a_voice_max_tokens", "voice_temperature", "region", "package_manifest_hash",
    "package_content_hash", "shape_hash", "seal_hash", "repo_commit", "live_test", "cap_usd", "safety_call", "reader_call",
    "self_revision", "battery_size",
}


@pytest.fixture(autouse=True)
def _no_live_client(monkeypatch):
    def refuse(region):
        raise AssertionError("a live client was built")

    monkeypatch.setattr(v7, "make_client", refuse)
    guard.reset_for_tests()
    yield
    guard.reset_for_tests()


@pytest.fixture
def b_render(monkeypatch):
    """A render_evidence_block that takes the loaded world and adds a line when the switch is on."""
    original = m4_evidence.render_evidence_block

    def render(evidence, *, world=None, reading=None):
        block = original(evidence)
        return block + ADDED if world is not None and world.frame.get(v7.READING_CONTEXT) else block

    monkeypatch.setattr(m4_evidence, "render_evidence_block", render)


def _manifest_hash(world=WORLD):
    return load_registry()[world]["package"]["manifest_hash"]


def _world():
    world, _ = LazyWorldLoader().load(
        WORLD, package_dir=v7.REPO_ROOT / load_registry()[WORLD]["package"]["location"], expected_manifest_hash=_manifest_hash(),
    )
    return world


def _probe_ids(n=2):
    return [seal["probe_id"] for seal in protocol.battery()[:n]]


def _quote_id():
    return next(rid for rid, r in m4_evidence.repository_records_by_id(_world().repository).items() if r.get("record_type") == "quote")


def _reply_text():
    return f"We hold this, as our teachers wrote. [[{_quote_id()}]]"


def _write_replies(reply_dir, probe_ids):
    reply_dir.mkdir(parents=True, exist_ok=True)
    for probe_id in probe_ids:
        (reply_dir / f"{probe_id}.voice.1.txt").write_text(_reply_text(), encoding="utf-8")


def _argv(tmp_path, *, arm="a", probes=None, out="run.jsonl", expect=None, max_tokens="2048", extra=(), reading_dir=RECORDS_ROOT):
    reading = ("--reading-records-dir", str(reading_dir)) if arm == "b" and reading_dir is not None else ()
    return [
        "--world", WORLD, "--arm", arm, "--probes", ",".join(probes or _probe_ids()), "--out", str(tmp_path / out),
        "--model-id", MODEL, "--region", "us-east-1", "--max-tokens", max_tokens,
        "--expect-package-hash", expect or _manifest_hash(), *reading, *extra,
    ]


def _dry(tmp_path, **kwargs):
    extra = (*kwargs.pop("extra", ()), "--reply-files", str(tmp_path / "replies"))
    return _argv(tmp_path, extra=extra, **kwargs)


def _records(path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]


def _summary(path):
    return json.loads(Path(f"{path}.summary.json").read_text(encoding="utf-8"))


class _FakeStream:
    def __init__(self, text, usage):
        self.text_stream = iter([text])
        self._message = SimpleNamespace(
            usage=SimpleNamespace(**usage), stop_reason="end_turn", content=[SimpleNamespace(type="text", text=text)],
        )

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False

    def get_final_message(self):
        return self._message


class _FakeSDK:
    """Stands where the Bedrock SDK client stands: keeps each stream call's
    kwargs, times out the first `failures` calls, then streams `text`."""

    def __init__(self, text, *, failures=0, usage=None):
        self.messages = self
        self.kwargs = []
        self.text = text
        self.failures = failures
        self.usage = usage or {"input_tokens": 1000, "output_tokens": 100, "cache_creation_input_tokens": 0, "cache_read_input_tokens": 5000}

    def stream(self, **kwargs):
        self.kwargs.append(kwargs)
        if len(self.kwargs) <= self.failures:
            raise APITimeoutError(request=_http.Request("POST", "https://bedrock.invalid"))
        return _FakeStream(self.text, self.usage)


def _run_live(monkeypatch, tmp_path, sdk, *, cap, probes=None, extra=()):
    monkeypatch.setenv(guard.LEDGER_ENV, str(tmp_path / "ledger.jsonl"))
    argv = _argv(tmp_path, probes=probes, extra=("--live-test", "v7-test", "--cap-usd", str(cap), *extra))
    monkeypatch.setattr(sys, "argv", ["v7_run", *argv])
    monkeypatch.setattr(v7, "make_client", lambda region: guard.wrap(sdk, guard.admit(), provider="bedrock", region=region))
    return v7.main(argv)


def _priced(usage):
    return estimate_cost(NormalizedUsage(**usage), price_for_route("voice_generation", MODEL, "bedrock")).dollars


# ---- refusals before any client ------------------------------------------------

def test_without_a_live_test_or_reply_files_the_command_exits_2_before_any_client(tmp_path, monkeypatch):
    loads = []
    monkeypatch.setattr(v7, "LazyWorldLoader", lambda: loads.append(1))
    assert v7.main(_argv(tmp_path)) == 2
    assert v7.main(_argv(tmp_path, extra=("--live-test", "v7-test"))) == 2
    assert v7.main(_argv(tmp_path, extra=("--cap-usd", "1"))) == 2
    assert not loads
    assert not (tmp_path / "run.jsonl").exists()


def test_arm_b_is_refused_when_the_render_cannot_read_the_switch(tmp_path, monkeypatch, capsys):
    original = m4_evidence.render_evidence_block
    monkeypatch.setattr(m4_evidence, "render_evidence_block", lambda evidence: original(evidence))
    loads = []
    monkeypatch.setattr(v7, "LazyWorldLoader", lambda: loads.append(1))
    assert v7.main(_dry(tmp_path, arm="b")) == 2
    assert v7.main(_argv(tmp_path, arm="b", extra=("--live-test", "v7-test", "--cap-usd", "1"))) == 2
    assert "world" in capsys.readouterr().err
    assert not loads
    assert not (tmp_path / "run.jsonl").exists()


def test_arm_b_without_a_reading_records_dir_exits_2_before_any_load(tmp_path, monkeypatch, capsys):
    loads = []
    monkeypatch.setattr(v7, "LazyWorldLoader", lambda: loads.append(1))
    assert v7.main(_dry(tmp_path, arm="b", reading_dir=None)) == 2
    assert "--reading-records-dir" in capsys.readouterr().err
    assert v7.main(_dry(tmp_path, arm="b", reading_dir=tmp_path / "no-records")) == 2
    assert not loads
    assert not (tmp_path / "run.jsonl").exists()


def test_arm_a_refuses_a_reading_records_dir(tmp_path):
    with pytest.raises(SystemExit) as refused:
        v7.main(_dry(tmp_path, extra=("--reading-records-dir", str(RECORDS_ROOT))))
    assert refused.value.code == 2


def test_arm_b_records_the_reading_directory_its_hash_and_the_signal(tmp_path):
    from engine.m4.reading_cards import load_reading_context

    probe_ids = _probe_ids()
    _write_replies(tmp_path / "replies", probe_ids)
    assert v7.main(_dry(tmp_path, arm="b")) == 0
    settings = _summary(tmp_path / "run.jsonl")["run_settings"]
    reading = load_reading_context(RECORDS_ROOT, WORLD)
    assert settings["reading_records_dir"] == str(RECORDS_ROOT.resolve())
    assert settings["reading_sha256"] == v7.reading_sha256(reading) and settings["reading_records"] == len(reading)
    for record in _records(tmp_path / "run.jsonl"):
        assert record["whole_world_signal"] == {"count": 0, "sentences": []}
        assert record["additions_chars"] > 0
        additions = record["reading_additions"]
        assert additions["renderings"] > 0 and additions["reads_differently_today"] > 0
        assert additions["chars"] == record["additions_chars"]
        assert all(set(w) == {"record_id", "file", "lines", "trimmed"} for w in additions["context_windows"])


def test_a_max_tokens_other_than_a_s_is_refused_unless_allowed(tmp_path):
    _write_replies(tmp_path / "replies", _probe_ids(1))
    with pytest.raises(SystemExit) as refused:
        v7.main(_dry(tmp_path, probes=_probe_ids(1), max_tokens="1024"))
    assert refused.value.code == 2
    assert not (tmp_path / "run.jsonl").exists()
    assert v7.main(_dry(tmp_path, probes=_probe_ids(1), max_tokens="1024", extra=("--allow-settings-differ",))) == 0
    (record,) = _records(tmp_path / "run.jsonl")
    settings = _summary(tmp_path / "run.jsonl")["run_settings"]
    assert record["voice_max_tokens"] == 1024 and settings["voice_max_tokens"] == 1024 and settings["a_voice_max_tokens"] == 2048


def test_reply_files_inside_the_repository_are_refused(tmp_path):
    with pytest.raises(SystemExit, match="must be outside"):
        v7.main(_argv(tmp_path, extra=("--reply-files", str(v7.REPO_ROOT / "engine"))))


def test_reply_files_inside_the_main_checkout_are_refused(tmp_path):
    common = subprocess.run(["git", "rev-parse", "--git-common-dir"], cwd=v7.REPO_ROOT, capture_output=True, text=True, check=True).stdout.strip()
    main_checkout = (v7.REPO_ROOT / common).resolve().parent
    with pytest.raises(SystemExit, match="must be outside"):
        v7.main(_argv(tmp_path, extra=("--reply-files", str(main_checkout / "v7-replies"))))


def test_a_package_hash_that_differs_stops_before_any_call(tmp_path, monkeypatch):
    calls = []
    monkeypatch.setattr(v7.ReplyFileClient, "stream", lambda self, **kw: calls.append(kw))
    _write_replies(tmp_path / "replies", _probe_ids())
    with pytest.raises(SystemExit, match="package hash"):
        v7.main(_dry(tmp_path, expect="sha256:" + "0" * 64))
    assert not calls
    assert not (tmp_path / "run.jsonl").exists()


def test_an_existing_record_or_summary_file_is_kept_unless_overwrite_is_given(tmp_path):
    _write_replies(tmp_path / "replies", _probe_ids(1))
    argv = _dry(tmp_path, probes=_probe_ids(1))
    assert v7.main(argv) == 0
    with pytest.raises(SystemExit, match="--overwrite"):
        v7.main(argv)
    (tmp_path / "run.jsonl").unlink()
    with pytest.raises(SystemExit, match="--overwrite"):
        v7.main(argv)
    assert v7.main([*argv, "--overwrite"]) == 0
    assert len(_records(tmp_path / "run.jsonl")) == 1


# ---- dry mode ------------------------------------------------------------------

def test_dry_mode_writes_a_record_with_every_field_for_each_probe(tmp_path, b_render):
    probe_ids = _probe_ids()
    _write_replies(tmp_path / "replies", probe_ids)
    assert v7.main(_dry(tmp_path, arm="b")) == 0

    records = _records(tmp_path / "run.jsonl")
    assert [r["probe_id"] for r in records] == probe_ids
    for record in records:
        assert set(record) == RECORD_FIELDS
        assert record["arm"] == "b" and record["voice_model_id"] == MODEL and record["voice_max_tokens"] == 2048
        assert record["package_manifest_hash"] == _manifest_hash() and record["error"] is None
        assert set(record["usage"]) == {"input_tokens", "output_tokens", "cache_creation_input_tokens", "cache_read_input_tokens"}
        assert record["offered_record_ids"] and record["answer_text"]
        assert record["additions_chars"] == len(ADDED) == record["evidence_chars"] - record["evidence_chars_flag_off"]
        assert record["seconds_total"] is not None and record["stop_reason"] == "end_turn"
        assert record["priced_usd"] == 0.0 and record["attempts"] == 1 and record["priced_includes_failed_holds"] is False
    summary = _summary(tmp_path / "run.jsonl")
    assert summary["run_settings"]["arm"] == "b" and summary["turns"] == 2
    assert SETTINGS_FIELDS <= set(summary["run_settings"])
    assert summary["run_settings"]["voice_temperature"] == "API default (not set by stream_voice_turn)"


def test_dry_mode_with_a_missing_reply_writes_the_request_outside_the_record_and_exits_4(tmp_path, capsys):
    probe_id = _probe_ids(1)[0]
    (tmp_path / "replies").mkdir()
    argv = _dry(tmp_path, probes=[probe_id], extra=("--project-cost", "--remaining", "10", "--stop-above", "1"))
    assert v7.main(argv) == 4
    assert (tmp_path / "replies" / "pending" / f"{probe_id}.voice.1.request.json").exists()
    assert _records(tmp_path / "run.jsonl") == []
    assert '"projection"' in capsys.readouterr().out


def test_arm_b_sets_the_reading_context_flag_in_memory_only(tmp_path, monkeypatch, b_render):
    seen = []
    render = m4_evidence.render_evidence_block

    def spy(evidence, *, world=None, reading=None):
        seen.append(None if world is None else world.frame.get(v7.READING_CONTEXT))
        return render(evidence, world=world, reading=reading)

    monkeypatch.setattr(m4_evidence, "render_evidence_block", spy)
    probe_id = _probe_ids(1)[0]
    _write_replies(tmp_path / "replies", [probe_id])
    assert v7.main(_dry(tmp_path, arm="b", probes=[probe_id])) == 0
    assert sorted(seen, key=bool) == [None, True]
    assert v7.READING_CONTEXT not in _world().frame


def test_arm_a_renders_as_a_did_and_adds_nothing(tmp_path, b_render):
    probe_id = _probe_ids(1)[0]
    _write_replies(tmp_path / "replies", [probe_id])
    assert v7.main(_dry(tmp_path, arm="b", probes=[probe_id], out="b.jsonl")) == 0
    assert v7.main(_dry(tmp_path, arm="a", probes=[probe_id], out="a.jsonl")) == 0
    (b,), (a,) = _records(tmp_path / "b.jsonl"), _records(tmp_path / "a.jsonl")
    assert b["additions_chars"] == len(ADDED) and a["additions_chars"] == 0
    assert b["offered_record_ids"] == a["offered_record_ids"]


def test_no_evidence_block_sent_means_no_additions(tmp_path, monkeypatch, b_render):
    original = m4_evidence.assemble_evidence
    monkeypatch.setattr(m4_evidence, "assemble_evidence", lambda **kw: {**original(**kw), "candidates": []})
    sent = []
    stream = v7.ReplyFileClient.stream
    monkeypatch.setattr(v7.ReplyFileClient, "stream", lambda self, **kw: sent.append(kw) or stream(self, **kw))
    probe_id = _probe_ids(1)[0]
    _write_replies(tmp_path / "replies", [probe_id])
    assert v7.main(_dry(tmp_path, arm="b", probes=[probe_id])) == 0
    (record,) = _records(tmp_path / "run.jsonl")
    assert record["additions_chars"] == 0 and record["evidence_chars"] == 0 and record["offered_record_ids"] == []
    assert sent[0]["messages"][-1]["content"] == sealed_probes.read_probe(probe_id)["text"]


# ---- fidelity to A -------------------------------------------------------------

def _runner_kwargs(tmp_path, monkeypatch, probe_ids):
    sent = []
    stream = v7.ReplyFileClient.stream
    monkeypatch.setattr(v7.ReplyFileClient, "stream", lambda self, **kw: sent.append(kw) or stream(self, **kw))
    _write_replies(tmp_path / "replies", probe_ids)
    assert v7.main(_dry(tmp_path, arm="a", probes=probe_ids)) == 0
    return sent


def test_arm_a_sends_the_user_message_the_admission_pipeline_builds(tmp_path, monkeypatch):
    probe_ids = _probe_ids()
    sent = _runner_kwargs(tmp_path, monkeypatch, probe_ids)
    world = _world()
    repository_records = m4_evidence.repository_records_by_id(world.repository)
    canon_questions = load_fleet_records()
    for probe_id, kwargs in zip(probe_ids, sent):
        probe_text = sealed_probes.read_probe(probe_id)["text"]
        turn_evidence = m4_evidence.assemble_evidence(
            message=probe_text, asks=None, canon_questions=canon_questions, coverage=world.coverage,
            repository_records=repository_records, thin_topics=m4_evidence.thin_topics_for(repository_records),
        )
        if world.frame.get("story_placement"):
            turn_evidence = with_placeable_stories(turn_evidence, repository_records)
        block = m4_evidence.render_evidence_block(turn_evidence)
        expected = f"{block}\n{probe_text}" if turn_evidence["candidates"] else probe_text
        assert kwargs["messages"] == [{"role": "user", "content": expected}]


def test_the_system_argument_is_the_shape_then_the_world_prompt_and_nothing_else_is_set(tmp_path, monkeypatch):
    (kwargs,) = _runner_kwargs(tmp_path, monkeypatch, _probe_ids(1))
    assert [block["text"] for block in kwargs["system"]] == [shape_text(), _world().prompt_text]
    assert all(block.get("cache_control") == {"type": "ephemeral"} for block in kwargs["system"])
    assert kwargs["model"] == MODEL and kwargs["max_tokens"] == 2048
    assert set(kwargs) == {"model", "max_tokens", "system", "messages", "timeout"}


def test_the_voice_call_is_the_one_a_s_live_model_answerer_makes(tmp_path, monkeypatch):
    from engine.m3.generation import LiveModelAnswerer

    if not {"canon_questions", "model_id"} <= set(inspect.signature(LiveModelAnswerer).parameters):
        pytest.skip("this LiveModelAnswerer answers through run_turn, not A's admission pipeline; the comparison runs on a checkout of live")
    probe_ids = _probe_ids()
    sent = _runner_kwargs(tmp_path, monkeypatch, probe_ids)
    world = _world()
    by_id = {seal["probe_id"]: seal for seal in protocol.battery()}
    for probe_id, kwargs in zip(probe_ids, sent):
        sdk = _FakeSDK(_reply_text())
        answerer = LiveModelAnswerer(world=world, canon_questions=load_fleet_records(), client=sdk, model_id=MODEL)
        answerer.answer(by_id[probe_id]["cell"], sealed_probes.read_probe(probe_id)["text"])
        assert kwargs == sdk.kwargs[0]


# ---- the live-flag path, behind the real guard ---------------------------------

def test_a_live_run_prices_each_turn_from_the_guard(tmp_path, monkeypatch):
    sdk = _FakeSDK(_reply_text())
    assert _run_live(monkeypatch, tmp_path, sdk, cap=5, probes=_probe_ids(1)) == 0
    (record,) = _records(tmp_path / "run.jsonl")
    summary = _summary(tmp_path / "run.jsonl")
    assert record["priced_usd"] == pytest.approx(_priced(sdk.usage), abs=1e-6)
    assert summary["live_test"]["priced_total_usd"] == pytest.approx(record["priced_usd"], abs=1e-6)
    assert summary["run_settings"]["live_test"] == "v7-test" and summary["run_settings"]["cap_usd"] == 5
    assert record["usage"] == sdk.usage and record["priced_includes_failed_holds"] is False


def test_the_cap_stops_the_run_with_exit_1(tmp_path, monkeypatch):
    sdk = _FakeSDK(_reply_text())
    assert _run_live(monkeypatch, tmp_path, sdk, cap=0.0001) == 1
    assert sdk.kwargs == []
    assert _records(tmp_path / "run.jsonl") == []
    assert "cap" in _summary(tmp_path / "run.jsonl")["stopped"]


def test_a_retried_call_counts_its_failed_hold(tmp_path, monkeypatch):
    sdk = _FakeSDK(_reply_text(), failures=1)
    assert _run_live(monkeypatch, tmp_path, sdk, cap=5, probes=_probe_ids(1)) == 0
    (record,) = _records(tmp_path / "run.jsonl")
    assert record["attempts"] == 2 and record["priced_includes_failed_holds"] is True
    assert record["priced_usd"] > _priced(sdk.usage)
    assert record["priced_usd"] == pytest.approx(_summary(tmp_path / "run.jsonl")["live_test"]["priced_total_usd"], abs=1e-6)


def test_a_probe_that_fails_every_attempt_is_recorded_with_its_holds_and_stops_the_run(tmp_path, monkeypatch):
    sdk = _FakeSDK(_reply_text(), failures=v7.VOICE_CALL_ATTEMPTS)
    assert _run_live(monkeypatch, tmp_path, sdk, cap=5) == 1
    assert len(sdk.kwargs) == v7.VOICE_CALL_ATTEMPTS
    (record,) = _records(tmp_path / "run.jsonl")
    summary = _summary(tmp_path / "run.jsonl")
    assert set(record) == RECORD_FIELDS
    assert record["error"] and record["answer_text"] is None and record["attempts"] == v7.VOICE_CALL_ATTEMPTS
    assert record["priced_usd"] > 0 and record["priced_includes_failed_holds"] is True
    assert record["priced_usd"] == pytest.approx(summary["live_test"]["priced_total_usd"], abs=1e-6)
    assert summary["turns"] == 1 and summary["stopped"]


# ---- the stop rule -------------------------------------------------------------

def test_projection_scales_the_mean_turn_cost_to_the_remaining_turns():
    projection = v7.project_cost(spent_usd=0.09, turns=3, remaining=120, stop_above=11.0)
    assert projection["mean_usd_per_turn"] == pytest.approx(0.03)
    assert projection["projected_further_usd"] == pytest.approx(3.60)
    assert projection["projected_total_usd"] == pytest.approx(3.69)
    assert projection["passes_threshold"] is False
    assert v7.project_cost(spent_usd=0.09, turns=3, remaining=400, stop_above=11.0)["passes_threshold"] is True


def test_project_cost_uses_the_guard_total_and_exits_3_past_the_threshold(tmp_path, capsys):
    out = tmp_path / "sample.jsonl"
    out.write_text("".join(json.dumps({"probe_id": f"p{i}", "priced_usd": 0.001}) + "\n" for i in range(6)), encoding="utf-8")
    Path(f"{out}.summary.json").write_text(json.dumps({"turns": 6, "priced_usd": 0.006, "live_test": {"priced_total_usd": 0.30}}))
    base = ["--project-cost", "--out", str(out), "--remaining", "120"]
    assert v7.main([*base, "--stop-above", "11"]) == 0
    assert v7.main([*base, "--stop-above", "5"]) == 3
    printed = capsys.readouterr().out
    assert '"projected_total_usd": 6.3' in printed and '"spent_source": "guard"' in printed


def test_project_cost_without_a_run_summary_is_a_clean_error(tmp_path):
    with pytest.raises(SystemExit, match="no run summary"):
        v7.main(["--project-cost", "--out", str(tmp_path / "missing.jsonl"), "--remaining", "1", "--stop-above", "1"])


def test_the_projection_is_printed_when_the_run_stops(tmp_path, monkeypatch, capsys):
    sdk = _FakeSDK(_reply_text())
    assert _run_live(monkeypatch, tmp_path, sdk, cap=0.0001, extra=("--project-cost", "--remaining", "10", "--stop-above", "1")) == 1
    assert '"projection"' in capsys.readouterr().out
