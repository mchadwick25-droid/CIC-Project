"""engine.m3.v7_run with no model call: every voice call is answered from a
reply file, and the live client builder is replaced by one that fails the
test if it is ever reached."""
import json

import pytest

import engine.m3.v7_run as v7
from engine.m1.loader import load_fleet_records
from engine.m1.registry import load_registry
from engine.m3 import protocol, sealed_probes
from engine.m4 import evidence as m4_evidence
from engine.m4.story_placement import with_placeable_stories
from engine.m4.world_loader import LazyWorldLoader

WORLD = "alx"
MODEL = "us.anthropic.claude-sonnet-4-5-20250929-v1:0"
RECORD_FIELDS = {
    "probe_id", "cell", "arm", "world", "passed", "checks", "answer_text", "raw_text", "citations", "citation_entries",
    "offered_record_ids", "usage", "seconds_to_first_text", "seconds_total", "stop_reason", "attempts", "priced_usd",
    "model_id", "max_tokens", "region", "package_manifest_hash", "repo_commit", "additions_chars", "evidence_chars",
    "evidence_chars_flag_off",
}


@pytest.fixture(autouse=True)
def _no_live_client(monkeypatch):
    def refuse(region):
        raise AssertionError("a live client was built")

    monkeypatch.setattr(v7, "make_client", refuse)


def _manifest_hash(world=WORLD):
    return load_registry()[world]["package"]["manifest_hash"]


def _probe_ids(n=2):
    return [seal["probe_id"] for seal in protocol.battery()[:n]]


def _quote_id():
    world, _ = LazyWorldLoader().load(
        WORLD, package_dir=v7.REPO_ROOT / load_registry()[WORLD]["package"]["location"], expected_manifest_hash=_manifest_hash(),
    )
    return next(rid for rid, r in m4_evidence.repository_records_by_id(world.repository).items() if r.get("record_type") == "quote")


def _write_replies(reply_dir, probe_ids):
    reply_dir.mkdir(parents=True, exist_ok=True)
    record_id = _quote_id()
    for probe_id in probe_ids:
        (reply_dir / f"{probe_id}.voice.1.txt").write_text(f"We hold this, as our teachers wrote. [[{record_id}]]", encoding="utf-8")


def _argv(tmp_path, *, arm="a", probes=None, out="run.jsonl", expect=None, extra=()):
    return [
        "--world", WORLD, "--arm", arm, "--probes", ",".join(probes or _probe_ids()), "--out", str(tmp_path / out),
        "--model-id", MODEL, "--region", "us-east-1", "--max-tokens", "2048",
        "--expect-package-hash", expect or _manifest_hash(), *extra,
    ]


def _records(path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]


def test_without_a_live_test_or_reply_files_the_command_exits_2_before_any_client(tmp_path, monkeypatch):
    loads = []
    monkeypatch.setattr(v7, "LazyWorldLoader", lambda: loads.append(1))
    assert v7.main(_argv(tmp_path)) == 2
    assert v7.main(_argv(tmp_path, extra=("--live-test", "v7-test"))) == 2
    assert v7.main(_argv(tmp_path, extra=("--cap-usd", "1"))) == 2
    assert not loads
    assert not (tmp_path / "run.jsonl").exists()


def test_dry_mode_writes_a_record_with_every_field_for_each_probe(tmp_path):
    probe_ids = _probe_ids()
    _write_replies(tmp_path / "replies", probe_ids)
    assert v7.main(_argv(tmp_path, arm="b", extra=("--reply-files", str(tmp_path / "replies")))) == 0

    records = _records(tmp_path / "run.jsonl")
    assert [r["probe_id"] for r in records] == probe_ids
    for record in records:
        assert set(record) == RECORD_FIELDS
        assert record["arm"] == "b" and record["model_id"] == MODEL and record["max_tokens"] == 2048
        assert record["package_manifest_hash"] == _manifest_hash()
        assert set(record["usage"]) == {"input_tokens", "output_tokens", "cache_creation_input_tokens", "cache_read_input_tokens"}
        assert record["offered_record_ids"] and record["answer_text"]
        assert record["additions_chars"] == record["evidence_chars"] - record["evidence_chars_flag_off"]
        assert record["seconds_total"] is not None and record["stop_reason"] == "end_turn"
        assert record["priced_usd"] == 0.0
    summary = json.loads((tmp_path / "run.jsonl.summary.json").read_text(encoding="utf-8"))
    assert summary["run_settings"]["arm"] == "b" and summary["turns"] == 2


def test_dry_mode_with_a_missing_reply_writes_the_request_outside_the_record_and_exits_4(tmp_path):
    probe_id = _probe_ids(1)[0]
    reply_dir = tmp_path / "replies"
    reply_dir.mkdir()
    assert v7.main(_argv(tmp_path, probes=[probe_id], extra=("--reply-files", str(reply_dir)))) == 4
    assert (reply_dir / "pending" / f"{probe_id}.voice.1.request.json").exists()
    assert _records(tmp_path / "run.jsonl") == []


def test_reply_files_inside_the_repository_are_refused(tmp_path):
    with pytest.raises(SystemExit, match="must be outside it"):
        v7.main(_argv(tmp_path, extra=("--reply-files", str(v7.REPO_ROOT / "engine"))))


def test_a_package_hash_that_differs_stops_before_any_call(tmp_path, monkeypatch):
    calls = []
    monkeypatch.setattr(v7.ReplyFileClient, "stream", lambda self, **kw: calls.append(kw))
    _write_replies(tmp_path / "replies", _probe_ids())
    with pytest.raises(SystemExit, match="package hash"):
        v7.main(_argv(tmp_path, expect="sha256:" + "0" * 64, extra=("--reply-files", str(tmp_path / "replies"))))
    assert not calls
    assert not (tmp_path / "run.jsonl").exists()


def test_arm_a_sends_the_user_message_the_admission_answerer_builds(tmp_path, monkeypatch):
    sent = []
    original = v7.ReplyFileClient.stream

    def capture(self, **kwargs):
        sent.append(kwargs)
        return original(self, **kwargs)

    monkeypatch.setattr(v7.ReplyFileClient, "stream", capture)
    probe_ids = _probe_ids()
    _write_replies(tmp_path / "replies", probe_ids)
    assert v7.main(_argv(tmp_path, arm="a", extra=("--reply-files", str(tmp_path / "replies")))) == 0

    world, _ = LazyWorldLoader().load(
        WORLD, package_dir=v7.REPO_ROOT / load_registry()[WORLD]["package"]["location"], expected_manifest_hash=_manifest_hash(),
    )
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
        assert kwargs["messages"][-1]["content"] == expected
        assert kwargs["model"] == MODEL and kwargs["max_tokens"] == 2048
    assert all(r["additions_chars"] == 0 for r in _records(tmp_path / "run.jsonl"))


def test_arm_b_sets_the_reading_context_flag_in_memory_only(tmp_path, monkeypatch):
    seen = []
    original = v7.render_block

    def spy(turn_evidence, world):
        seen.append(world.frame.get(v7.READING_CONTEXT))
        return original(turn_evidence, world)

    monkeypatch.setattr(v7, "render_block", spy)
    probe_id = _probe_ids(1)[0]
    _write_replies(tmp_path / "replies", [probe_id])
    assert v7.main(_argv(tmp_path, arm="b", probes=[probe_id], extra=("--reply-files", str(tmp_path / "replies")))) == 0
    assert sorted(seen, key=bool) == [None, True]
    fresh, _ = LazyWorldLoader().load(
        WORLD, package_dir=v7.REPO_ROOT / load_registry()[WORLD]["package"]["location"], expected_manifest_hash=_manifest_hash(),
    )
    assert v7.READING_CONTEXT not in fresh.frame


def test_projection_scales_the_mean_turn_cost_to_the_remaining_turns():
    records = [{"priced_usd": 0.02}, {"priced_usd": 0.04}, {"priced_usd": 0.03}]
    projection = v7.project_cost(records, remaining=120, stop_above=11.0)
    assert projection["turns"] == 3
    assert projection["spent_usd"] == pytest.approx(0.09)
    assert projection["mean_usd_per_turn"] == pytest.approx(0.03)
    assert projection["projected_further_usd"] == pytest.approx(3.60)
    assert projection["projected_total_usd"] == pytest.approx(3.69)
    assert projection["passes_threshold"] is False
    assert v7.project_cost(records, remaining=400, stop_above=11.0)["passes_threshold"] is True


def test_project_cost_exits_3_when_the_projection_passes_the_threshold(tmp_path, capsys):
    out = tmp_path / "sample.jsonl"
    out.write_text("".join(json.dumps({"probe_id": f"p{i}", "priced_usd": 0.05}) + "\n" for i in range(6)), encoding="utf-8")
    base = ["--project-cost", "--out", str(out), "--remaining", "120"]
    assert v7.main([*base, "--stop-above", "11"]) == 0
    assert v7.main([*base, "--stop-above", "5"]) == 3
    printed = capsys.readouterr().out
    assert '"projected_total_usd": 6.3' in printed


def test_a_render_that_reads_the_switch_from_the_world_gives_the_size_of_the_additions(tmp_path, monkeypatch):
    original = m4_evidence.render_evidence_block

    def render(evidence, world=None):
        block = original(evidence)
        return block + "\nADDED" if world is not None and world.frame.get(v7.READING_CONTEXT) else block

    monkeypatch.setattr(m4_evidence, "render_evidence_block", render)
    probe_id = _probe_ids(1)[0]
    _write_replies(tmp_path / "replies", [probe_id])
    assert v7.main(_argv(tmp_path, arm="b", probes=[probe_id], out="b.jsonl", extra=("--reply-files", str(tmp_path / "replies")))) == 0
    assert v7.main(_argv(tmp_path, arm="a", probes=[probe_id], out="a.jsonl", extra=("--reply-files", str(tmp_path / "replies")))) == 0
    (b,), (a,) = _records(tmp_path / "b.jsonl"), _records(tmp_path / "a.jsonl")
    assert b["additions_chars"] == len("\nADDED") and a["additions_chars"] == 0
    assert b["offered_record_ids"] == a["offered_record_ids"]
