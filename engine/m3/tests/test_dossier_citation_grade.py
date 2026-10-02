import json
from types import SimpleNamespace

import pytest

import engine.m3.dossier_citation_grade as dcg

SENTINEL = "SENTINEL-PROBE-TEXT-9731"

RECORDS = {
    "w.term.in": {"id": "w.term.in", "record_type": "term", "canon_cells": ["C-I"], "plain_meaning": "in"},
    "w.term.out": {"id": "w.term.out", "record_type": "term", "canon_cells": ["C-T"], "plain_meaning": "out"},
    "w.quote.none": {"id": "w.quote.none", "record_type": "quote", "text": "q"},
}


def _report(world="w", n=4):
    probes = []
    for i in range(n):
        probes.append({
            "probe_id": f"p{i}", "cell": "C-I",
            "transcript": {
                "citations": ["w.term.in", "w.term.out", "w.quote.none"],
                "citation_entries": [
                    {"sentence": "s-in", "record_ids": ["w.term.in"]},
                    {"sentence": "s-out", "record_ids": ["w.term.out", "w.quote.none"]},
                ],
            },
        })
    return {"worlds": {world: {"per_probe": probes}}}


@pytest.fixture
def reports(tmp_path, monkeypatch):
    sub = tmp_path / "baseline-set"
    sub.mkdir()
    (sub / "live-admission-report-baseline-r1-w-x.json").write_text(json.dumps(_report()))
    (sub / "live-admission-report-baseline-r2-w-x.json").write_text(json.dumps(_report(n=9)))
    monkeypatch.setattr(dcg, "REPORTS_DIR", tmp_path)
    monkeypatch.setattr(dcg, "load_world_records", lambda world: RECORDS)
    return tmp_path


def test_population_excludes_in_dossier_and_run_two(reports):
    population, dropped = dcg.load_population()
    items = population["w"]
    assert len(items) == 8
    assert {i["record_id"] for i in items} == {"w.term.out", "w.quote.none"}
    assert next(i for i in items if i["record_id"] == "w.quote.none")["record_cells"] == []
    assert all(i["sentences"] == ["s-out"] for i in items)
    assert dropped == {"w": 0}


def test_sample_is_deterministic_for_a_seed(reports):
    population, _ = dcg.load_population()
    a = dcg.draw_sample(population, 3, 7)
    b = dcg.draw_sample(population, 3, 7)
    assert a == b and len(a) == 3
    assert dcg.draw_sample(population, 99, 7) == dcg.draw_sample(population, 99, 7)
    assert len(dcg.draw_sample(population, 99, 7)) == 8


def test_parse_grade_valid_wrapped_and_unparsed():
    assert dcg.parse_grade('{"role": "supporting", "reason": "colour"}') == {"role": "supporting", "reason": "colour"}
    assert dcg.parse_grade('Here: {"role": "load_bearing", "reason": "r"} ok')["role"] == "load_bearing"
    bad = dcg.parse_grade("I think it matters a lot")
    assert bad == {"role": "unparsed", "raw_text": "I think it matters a lot"}
    assert dcg.parse_grade('{"role": "vital", "reason": "r"}')["role"] == "unparsed"


def _args(out, *extra):
    return ["--region", "r", "--grader-model", "m", "--per-world", "1", "--seed", "1", "--max-usd", "5",
            "--authorized-by", "t", "--price-input", "5", "--price-output", "25", "--price-cache-read", "0.5",
            "--out", str(out), *extra]


def test_settings_only_makes_no_billed_call(reports, monkeypatch, tmp_path):
    monkeypatch.setattr(dcg, "resolve_model_id", lambda pattern, region: "resolved-id")
    monkeypatch.setattr(dcg, "make_client", lambda region: pytest.fail("client built"))
    monkeypatch.setattr(dcg, "read_probe", lambda pid: {"text": SENTINEL})
    out = tmp_path / "out.json"
    assert dcg.main(_args(out, "--settings-only")) == 0
    assert not out.exists()


def test_unpriced_model_fails_before_any_call(reports, monkeypatch):
    monkeypatch.setattr(dcg, "resolve_model_id", lambda pattern, region: "unknown-id")
    monkeypatch.setattr(dcg, "make_client", lambda region: pytest.fail("client built"))
    monkeypatch.setattr(dcg, "read_probe", lambda pid: {"text": SENTINEL})
    with pytest.raises(SystemExit, match="no price"):
        dcg.run(region="r", grader_model="m", per_world=1, seed=1, max_usd=5, authorized_by="t")


class _Client:
    def __init__(self, text):
        self.calls = []
        self.messages = self
        self._text = text

    def create(self, **kw):
        self.calls.append(kw)
        return SimpleNamespace(
            content=[SimpleNamespace(type="text", text=self._text)],
            usage=SimpleNamespace(input_tokens=100, output_tokens=20),
        )


def test_report_has_no_probe_text_and_request_shape(reports, monkeypatch, tmp_path, capsys):
    client = _Client('{"role": "load_bearing", "reason": "rests on it"}')
    monkeypatch.setattr(dcg, "resolve_model_id", lambda pattern, region: "resolved-id")
    monkeypatch.setattr(dcg, "make_client", lambda region: client)
    monkeypatch.setattr(dcg, "read_probe", lambda pid: {"text": SENTINEL})
    out = tmp_path / "out.json"
    assert dcg.main(_args(out)) == 0
    assert len(client.calls) == 1
    call = client.calls[0]
    assert SENTINEL in call["messages"][0]["content"]
    assert call["max_tokens"] == 2000 and "thinking" not in call and "temperature" not in call
    written = out.read_text()
    captured = capsys.readouterr()
    assert SENTINEL not in written and SENTINEL not in captured.out and SENTINEL not in captured.err
    report = json.loads(written)
    assert report["items"][0]["role"] == "load_bearing"
    assert report["summary"]["overall"]["load_bearing_share"] == 1.0
    assert report["actual_usd_spent"] == pytest.approx(100 * 5e-6 + 20 * 25e-6)


def test_preflight_over_cap_aborts_before_client(reports, monkeypatch):
    monkeypatch.setattr(dcg, "resolve_model_id", lambda pattern, region: "resolved-id")
    monkeypatch.setattr(dcg, "make_client", lambda region: pytest.fail("client built"))
    monkeypatch.setattr(dcg, "read_probe", lambda pid: {"text": SENTINEL})
    with pytest.raises(SystemExit, match="exceeds --max-usd"):
        dcg.run(region="r", grader_model="m", per_world=1, seed=1, max_usd=1e-9, authorized_by="t",
                price_override=(5.0, 25.0, 0.5))
