"""engine.m3.v7_replay on the fixture world, with no model call: the saved
records are made by V7Answerer.answer from a fixed draft, then replayed."""
import json
from pathlib import Path

import pytest

import engine.m3.v7_run as v7
from engine.m1.loader import load_fleet_records
from engine.m2.compiler import compile_world
from engine.m2.manifest import manifest_hash
from engine.m3 import protocol, sealed_probes
from engine.m3 import v7_replay as replay
from engine.m4.world_loader import LazyWorldLoader

WORLD = "fix"
TYPED = 'The elder said, "the river runs uphill every morning at dawn."'
DRAFT = (f"We kept to the road. [[fix.story.the-long-road]] {TYPED} That is how we lived. "
         "[[quote:fix.quote.private-teaching]] We went on.")


class _Drafts:
    """Stands where the model client stands and streams one fixed draft."""

    def __init__(self, text: str):
        self.text = text
        self.messages = self

    def stream(self, **kwargs):
        return v7._ReplyStream(self.text)


@pytest.fixture
def package(tmp_path):
    files = compile_world(world_key=WORLD, package_id="T", records_commit="t", compiler_version="t")
    root = tmp_path / "packages" / WORLD / "T"
    for rel, content in files.items():
        (root / rel).parent.mkdir(parents=True, exist_ok=True)
        (root / rel).write_bytes(content)
    return {"root": tmp_path / "packages", "dir": root, "hash": manifest_hash(json.loads(files["manifest.json"]))}


def _probe_ids(n=2):
    return [seal["probe_id"] for seal in protocol.battery()[:n]]


def _saved_v7(package, path: Path, draft: str = DRAFT) -> list[dict]:
    world, _ = LazyWorldLoader().load(WORLD, package_dir=package["dir"], expected_manifest_hash=package["hash"])
    answerer = v7.V7Answerer(world=world, canon_questions=load_fleet_records(), client=v7.TimedClient(_Drafts(draft)),
                             model_id="model", max_tokens=2048, reading_context=False)
    rows = []
    for probe_id in _probe_ids():
        answer = answerer.answer(sealed_probes.read_probe(probe_id)["text"])
        rows.append({"world": WORLD, "probe_id": probe_id, "cell": "C-I", "raw_text": answer["calls"][-1]["raw_text"],
                     "answer_text": answer["text"], "citations": answer["citations"],
                     "offered_record_ids": answer["offered_record_ids"], "package_manifest_hash": package["hash"]})
    path.write_text("".join(json.dumps(r) + "\n" for r in rows), encoding="utf-8")
    return rows


def _argv(tmp_path, saved, package, *, fmt="v7", arm="a", out=None, extra=()):
    return ["--arm", arm, "--run", "run1", "--saved", str(saved), "--format", fmt,
            "--out", str(out or tmp_path / "out" / "cuts.jsonl"), "--packages-root", str(package["root"]), *extra]


def _lines(path):
    return [json.loads(line) for line in Path(path).read_text(encoding="utf-8").splitlines()]


def test_the_replay_counts_each_removed_sentence_and_reproduces_the_saved_answer(tmp_path, package):
    saved = tmp_path / "saved.jsonl"
    _saved_v7(package, saved)

    assert replay.main(_argv(tmp_path, saved, package)) == replay.EXIT_DONE

    lines = _lines(tmp_path / "out" / "cuts.jsonl")
    summary = json.loads((tmp_path / "out" / "cuts.jsonl.summary.json").read_text(encoding="utf-8"))
    assert len(lines) == 4
    assert {(line["probe_id"], line["arm"], line["run"]) for line in lines} == {(p, "a", "run1") for p in _probe_ids()}
    typed = [line for line in lines if line["removed_sentence"] == TYPED]
    assert len(typed) == 2
    assert {line["next_shipped"] for line in typed} == {"That is how we lived."}
    world = summary["worlds"][WORLD]
    assert world["probes"] == 2
    assert world["answer_text_equal"] == 2
    assert world["citations_equal"] == 2
    assert world["offered_ids_equal"] == world["offered_ids_compared"] == 2
    assert world["cuts"] == 4
    assert world["cuts_per_answer"] == 2.0
    assert sum(world["cuts_by_reason"].values()) == 4
    assert summary["packages"][WORLD]["package_matches_saved"] is True
    assert summary["settings"]["model_calls"] == 0


def test_an_admission_report_replays_like_a_v7_record_file(tmp_path, package):
    rows = _saved_v7(package, tmp_path / "saved.jsonl")
    report = {
        "run_settings": {"package_manifest_hash": {WORLD: package["hash"]}},
        "worlds": {WORLD: {"per_probe": [
            {"probe_id": r["probe_id"], "cell": r["cell"],
             "transcript": {"raw_text": r["raw_text"], "answer_text": r["answer_text"], "citations": r["citations"]}}
            for r in rows
        ]}},
    }
    saved = tmp_path / "report.json"
    saved.write_text(json.dumps(report), encoding="utf-8")

    assert replay.main(_argv(tmp_path, saved, package, fmt="admission")) == replay.EXIT_DONE

    world = json.loads((tmp_path / "out" / "cuts.jsonl.summary.json").read_text(encoding="utf-8"))["worlds"][WORLD]
    assert (world["probes"], world["answer_text_equal"], world["cuts"], world["offered_ids_compared"]) == (2, 2, 4, 0)


def test_a_draft_with_nothing_to_cut_gives_no_lines(tmp_path, package):
    saved = tmp_path / "saved.jsonl"
    _saved_v7(package, saved, draft="We kept to the road. We went on.")

    assert replay.main(_argv(tmp_path, saved, package)) == replay.EXIT_DONE

    assert _lines(tmp_path / "out" / "cuts.jsonl") == []
    world = json.loads((tmp_path / "out" / "cuts.jsonl.summary.json").read_text(encoding="utf-8"))["worlds"][WORLD]
    assert (world["cuts"], world["answer_text_equal"]) == (0, 2)


def test_the_replay_refuses_to_write_into_the_repository(tmp_path, package):
    saved = tmp_path / "saved.jsonl"
    _saved_v7(package, saved)
    inside = v7.REPO_ROOT / "engine" / "m3" / "reports" / "v7-replay-test.jsonl"

    assert replay.main(_argv(tmp_path, saved, package, out=inside)) == v7.EXIT_REFUSED

    assert not inside.exists()
    assert not Path(f"{inside}.summary.json").exists()


def test_the_replay_refuses_a_package_other_than_the_saved_one(tmp_path, package):
    saved = tmp_path / "saved.jsonl"
    rows = _saved_v7(package, saved)
    saved.write_text("".join(json.dumps({**r, "package_manifest_hash": "sha256:other"}) + "\n" for r in rows), encoding="utf-8")

    assert replay.main(_argv(tmp_path, saved, package)) == v7.EXIT_REFUSED

    assert not (tmp_path / "out" / "cuts.jsonl").exists()


def test_arm_b_is_refused_without_a_reading_records_dir(tmp_path, package):
    saved = tmp_path / "saved.jsonl"
    _saved_v7(package, saved)

    assert replay.main(_argv(tmp_path, saved, package, arm="b")) == v7.EXIT_REFUSED


def test_no_output_line_holds_a_run_of_any_probe_wording(tmp_path, package):
    saved = tmp_path / "saved.jsonl"
    probe_texts = [sealed_probes.read_probe(probe_id)["text"] for probe_id in _probe_ids()]
    echoed = " ".join(probe_texts[0].split()[:8])
    _saved_v7(package, saved, draft=f"We heard you ask: {echoed} [[quote:fix.quote.private-teaching]] That is how we lived.")

    assert replay.main(_argv(tmp_path, saved, package)) == replay.EXIT_DONE

    lines = _lines(tmp_path / "out" / "cuts.jsonl")
    runs = replay.probe_runs(probe_texts)
    assert [line["removed_sentence"] for line in lines] == [replay.WITHHELD] * 2
    for line in lines:
        assert not any(replay.shares_probe_run(line[field], runs) for field in ("removed_sentence", "draft", "next_shipped"))
    summary = json.loads((tmp_path / "out" / "cuts.jsonl.summary.json").read_text(encoding="utf-8"))
    assert summary["fields_withheld"] == 4


def test_shares_probe_run_needs_the_whole_run_of_words():
    runs = replay.probe_runs(["What did your people believe about the soul after death?"])
    assert replay.shares_probe_run("They asked what did your people believe about the soul.", runs)
    assert not replay.shares_probe_run("Our people believed the soul went on.", runs)
    assert not replay.shares_probe_run(None, runs)
