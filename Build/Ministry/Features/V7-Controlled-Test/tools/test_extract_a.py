"""Spec V1 tests 1-5 for the arm A extract in ../Set/.

The run files are read from branch claude/fleet-run-1-analysis with
`git show`. If that branch is not fetched, the tests that need it skip.
Probe text is read through engine/m3/sealed_probes.py, the one authorized
reader, and only hashed or compared here; it is never printed.
"""
import hashlib
import importlib.util
import json
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

import pytest
import yaml

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import extract_a  # noqa: E402

REPO = extract_a.REPO
SET_DIR = extract_a.SET_DIR
WORLDS = extract_a.WORLDS
GATE_REPLAY = REPO / "Build/Ministry/Features/Answering-From-Sources/Stage1/data/gate-replay"
SEALS = REPO / "canon/sealed_probes/seals.yaml"


def _branch_sha():
    try:
        return extract_a.source_sha()
    except subprocess.CalledProcessError:
        return None


SHA = _branch_sha()
needs_branch = pytest.mark.skipif(
    SHA is None, reason="branch claude/fleet-run-1-analysis is not fetched: git fetch origin claude/fleet-run-1-analysis")


def a_lines(world):
    return [json.loads(line) for line in (SET_DIR / f"A_{world}.jsonl").read_text(encoding="utf-8").splitlines()]


def run_probes(world):
    return extract_a.run_probes(extract_a.show_json(f"{extract_a.RUN_DIR}{world}.json", SHA), world)


def set_files():
    return sorted(p for p in SET_DIR.iterdir() if p.is_file())


# 1. 28 lines per world, answer_text byte-equal to the run file.

@needs_branch
@pytest.mark.parametrize("world", WORLDS)
def test_each_world_has_28_lines_with_the_run_files_answer_text(world):
    lines = a_lines(world)
    probes = run_probes(world)
    assert len(lines) == 28
    assert [l["probe_id"] for l in lines] == [p["probe_id"] for p in probes]
    assert len({l["cell"] for l in lines}) == 28
    for line, probe in zip(lines, probes):
        t = probe["transcript"]
        assert line["answer_text"].encode("utf-8") == t["answer_text"].encode("utf-8"), line["probe_id"]
        assert line["citations"] == t["citations"]
        assert line["citation_entries"] == t["citation_entries"]
        assert line["usage"] == probe["usage"]
        assert (line["seconds_to_first_text"], line["seconds_total"], line["stop_reason"]) == (
            t["seconds_to_first_text"], t["seconds_total"], t["stop_reason"])


@needs_branch
@pytest.mark.parametrize("world", WORLDS)
def test_priced_cost_is_the_ledger_settle_line_for_each_probe(world):
    ledger = extract_a.show_jsonl(f"{extract_a.RUN_DIR}ledger-{world}.jsonl", SHA)
    settles = [l for l in ledger if l["event"] == "settle"]
    holds = [l for l in ledger if l["event"] == "hold"]
    lines = a_lines(world)
    assert len(settles) == len(holds) == 28
    assert len({json.dumps(s["usage"], sort_keys=True) for s in settles}) == 28
    by_usage = {json.dumps(s["usage"], sort_keys=True): s["priced_dollars"] for s in settles}
    for line in lines:
        assert line["priced_usd"] == by_usage[json.dumps(line["usage"], sort_keys=True)]
    settings = json.loads((SET_DIR / "A_run_settings.json").read_text())["worlds"][world]
    assert sum(l["priced_usd"] for l in lines) == pytest.approx(settings["ledger_priced_usd_total"], abs=1e-12)


@pytest.mark.parametrize("world", WORLDS)
def test_offered_ids_are_marked_not_saved_and_draft_markers_parse(world):
    for line in a_lines(world):
        assert line["offered_record_ids"] is None
        assert line["offered_record_ids_status"].startswith("not saved")
        assert all(re.fullmatch(r"[\w.:\-]+", rid) for rid in line["draft_marker_ids"])


def test_draft_marker_parser():
    text = "A [[alx.dw.jesus]] b [[syr.term.raza-shrara]] [[alx.dw.jesus]] [x] [[]] [[quote:a.b]]."
    assert sorted(set(extract_a.MARKER.findall(text))) == ["alx.dw.jesus", "quote:a.b", "syr.term.raza-shrara"]


@needs_branch
def test_the_question_set_mapping_is_the_same_for_every_world_that_has_one():
    base = REPO / "Build/Ministry/Features/Answering-From-Sources/Cross-World-Test_2026-11-02"
    alx = yaml.safe_load((base / "alx/set.yaml").read_text())["questions"]
    syr = yaml.safe_load((base / "syr/set.yaml").read_text())["questions"]
    pairs = lambda qs: sorted((q["id"], q["probe_id"], q["cell"]) for q in qs)
    assert pairs(alx) == pairs(syr)


# 2. Joining the gate replay's shown sentences (removed=false) reproduces answer_text.

def replay_shown(world):
    shown = defaultdict(list)
    for raw in (GATE_REPLAY / f"{world}.jsonl").read_text(encoding="utf-8").splitlines():
        row = json.loads(raw)
        if not row["removed"]:
            shown[row["probe_id"]].append(row["shown"])
    return shown


def join_separators(answer, sentences):
    """The separators between the shown sentences in answer, or None if the
    sentences do not tile answer exactly, in order, with nothing else."""
    pos, seps = 0, []
    for i, s in enumerate(sentences):
        if i:
            m = re.match(r"\s+", answer[pos:])
            if not m:
                return None
            seps.append(m.group(0))
            pos += len(m.group(0))
        if not answer.startswith(s, pos):
            return None
        pos += len(s)
    return seps if pos == len(answer) else None


@pytest.mark.parametrize("world", WORLDS)
def test_gate_replay_shown_sentences_reproduce_answer_text(world):
    shown = replay_shown(world)
    lines = a_lines(world)
    assert set(shown) == {l["probe_id"] for l in lines}
    seps = Counter()
    for line in lines:
        found = join_separators(line["answer_text"], shown[line["probe_id"]])
        assert found is not None, f"{world} {line['probe_id']}: replay does not tile answer_text"
        seps.update(found)
    # The replay keeps sentences, not paragraph breaks: each join is a
    # space or a blank line, nothing else.
    assert set(seps) <= {" ", "\n\n"}


# 3. No output file holds probe text or a request.

def _norm(text):
    return " ".join(re.findall(r"\w+", text.lower()))


def sealed_texts():
    spec = importlib.util.spec_from_file_location("sealed_probes", REPO / "engine/m3/sealed_probes.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    seals = yaml.safe_load(SEALS.read_text())["seals"]
    return [_norm(module.read_probe(s["probe_id"])["text"]) for s in seals]


def strings(obj):
    if isinstance(obj, dict):
        for k, v in obj.items():
            yield str(k)
            yield from strings(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from strings(v)
    elif isinstance(obj, str):
        yield obj


def shingles(words, n):
    return {" ".join(words[i:i + n]) for i in range(len(words) - n + 1)}


def test_no_output_file_holds_probe_text():
    probes = sealed_texts()
    assert len(probes) == 28
    probe_hashes = {hashlib.sha256(p.encode()).hexdigest() for p in probes}
    probe_shingles = set().union(*(shingles(p.split(), 8) for p in probes))
    hits = []
    for path in set_files():
        whole = _norm(path.read_text(encoding="utf-8"))
        if any(p in whole for p in probes):
            hits.append((path.name, "whole probe as substring"))
        parts = list(strings(json.loads(path.read_text()))) if path.suffix == ".json" else []
        if path.suffix == ".jsonl":
            parts = [s for raw in path.read_text().splitlines() for s in strings(json.loads(raw))]
        for part in parts:
            pieces = [part] + re.split(r"(?<=[.?!])\s+", part)
            if any(hashlib.sha256(_norm(x).encode()).hexdigest() in probe_hashes for x in pieces):
                hits.append((path.name, "hash match"))
        if shingles(whole.split(), 8) & probe_shingles:
            hits.append((path.name, "8-word run"))
    assert not hits, f"probe text found (file, kind): {sorted(set(hits))}"


@needs_branch
def test_no_output_file_holds_a_request_or_a_draft():
    for world in WORLDS:
        for probe in run_probes(world):
            assert set(probe["transcript"]["request"]) <= {"model", "max_tokens"}
    drafts = [_norm(p["transcript"]["raw_text"]) for w in WORLDS for p in run_probes(w)
              if p["transcript"]["raw_text"] != p["transcript"]["answer_text"]]
    for path in set_files():
        text = path.read_text(encoding="utf-8")
        assert '"request"' not in text and '"raw_text"' not in text, path.name
        whole = _norm(text)
        assert not any(d in whole for d in drafts), path.name


# 4. The repeat draw reproduces from its seed.

def test_repeat_draw_reproduces_from_its_seed():
    saved = json.loads((SET_DIR / "repeat_draw.json").read_text())
    assert saved["seed"] == extract_a.SEED == 20261103
    assert saved == extract_a.repeat_draw(saved["seed"])
    assert saved["total"] == 42
    for world in WORLDS:
        block = saved["worlds"][world]
        cells = block["cells"]
        assert len(cells) == len(set(cells)) == 14
        families = Counter(c.split("-")[0] for c in cells)
        assert families == {f: 2 for f in extract_a.FAMILIES}
        registers = Counter(c.split("-")[1] for c in cells)
        assert sorted(registers.values()) == [3, 3, 4, 4]
        assert {l["probe_id"] for l in a_lines(world)} >= set(block["probe_ids"])
        assert [f"{c.lower()}-probe-01" for c in cells] == block["probe_ids"]


# 5. SHA256SUMS matches the files.

def test_sha256sums_match_every_file():
    listed = {}
    for raw in (SET_DIR / "SHA256SUMS").read_text().splitlines():
        digest, name = raw.split("  ", 1)
        listed[name] = digest
    assert set(listed) == {p.name for p in set_files()} - {"SHA256SUMS"}
    for name, digest in listed.items():
        assert hashlib.sha256((SET_DIR / name).read_bytes()).hexdigest() == digest, name


@needs_branch
def test_extract_is_deterministic(tmp_path):
    extract_a.extract(tmp_path)
    for path in tmp_path.iterdir():
        if path.name == "SHA256SUMS":
            continue
        assert path.read_bytes() == (SET_DIR / path.name).read_bytes(), path.name
