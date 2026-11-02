"""The rendering-review check: a modern_rendering needs a named Opus review file that lists it."""
import pytest

from engine.m1 import gates, rendering_review
from engine.m1.loader import load_world_records
from engine.m1.rendering_review import gate_rendering_review

RECORDS = {
    "w.quote.alpha": {"id": "w.quote.alpha", "record_type": "quote", "modern_rendering": "Alpha, in today's English."},
    "w.quote.beta": {"id": "w.quote.beta", "record_type": "quote", "modern_rendering": "Beta, in today's English."},
    "w.term.plain": {"id": "w.term.plain", "record_type": "term"},
}
LOG = """# log

| Record | Review file(s) | Verdict on the rendering |
|---|---|---|
| alpha | Review_One.md | PASS |
| w.quote.beta | Review_Two.md, Review_One.md | PASS |
"""


@pytest.fixture
def folder(tmp_path, monkeypatch):
    monkeypatch.setattr(rendering_review, "review_dir", lambda world_key: tmp_path)
    rendering_review._text.cache_clear()
    (tmp_path / "Rendering_Review_Log_x.md").write_text(LOG)
    (tmp_path / "Review_One.md").write_text("Model Opus 5.5. alpha: PASS. beta: PASS.")
    (tmp_path / "Review_Two.md").write_text("Model Opus 5.5. beta: PASS.")
    return tmp_path


def _run(records=RECORDS, registry=None):
    return gate_rendering_review(records, {}, registry or {})


def test_a_record_with_a_row_and_an_opus_review_file_that_lists_it_passes(folder):
    assert _run() == []


def test_a_record_the_log_does_not_name_fails(folder):
    records = {**RECORDS, "w.quote.gamma": {"id": "w.quote.gamma", "record_type": "quote", "modern_rendering": "Gamma."}}
    [finding] = _run(records)
    assert finding.startswith("w.quote.gamma") and "no rendering review log row" in finding


def test_a_row_naming_a_missing_file_fails(folder):
    (folder / "Review_One.md").unlink()
    (folder / "Review_Two.md").unlink()
    findings = _run()
    assert len(findings) == 2 and all("do not exist" in f for f in findings)


def test_a_review_file_that_does_not_mention_opus_fails(folder):
    (folder / "Review_One.md").write_text("Model someone. alpha: PASS. beta: PASS.")
    [finding] = [f for f in _run() if f.startswith("w.quote.alpha")]
    assert "Opus" in finding


def test_a_review_file_that_does_not_list_the_record_fails(folder):
    (folder / "Review_One.md").write_text("Model Opus 5.5. beta: PASS.")
    assert [f for f in _run() if f.startswith("w.quote.alpha")]


def test_a_world_with_no_log_fails_every_rendering(tmp_path, monkeypatch):
    monkeypatch.setattr(rendering_review, "review_dir", lambda world_key: tmp_path / "absent")
    assert len(_run()) == 2


def test_the_fixture_world_passes_its_own_log():
    assert gate_rendering_review(load_world_records("fix"), {}, {}) == []


def test_every_lpc_rendering_is_listed_in_the_real_log():
    assert gate_rendering_review(load_world_records("lpc"), {}, {}) == []


def test_the_gate_is_registered():
    assert gates.GATES["rendering-review"] is gate_rendering_review


def test_a_review_that_lists_only_a_longer_id_does_not_count(folder):
    (folder / "Review_One.md").write_text("Model Opus 5.5. alpha-two: PASS. beta: PASS.")
    assert [f for f in _run() if f.startswith("w.quote.alpha")]
