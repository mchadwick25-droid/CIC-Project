import importlib.util
import sys
from pathlib import Path

import pytest

MODULE = Path(__file__).resolve().parents[1] / "shelf_row_pointers.py"
spec = importlib.util.spec_from_file_location("shelf_row_pointers", MODULE)
srp = importlib.util.module_from_spec(spec)
sys.modules["shelf_row_pointers"] = srp
spec.loader.exec_module(srp)

RECORD = (
    "---\n"
    "id: w.source.on-the-spirit\n"
    "work: Basil, On the Holy Spirit (c. 375)\n"
    "kind: vendored\n"
    "rights_status: x\n"
    "---\n"
    "Body.\n"
)


def row(row_id, work):
    return {"row_id": row_id, "work": work}


def test_normalise_ignores_case_punctuation_and_diacritics():
    assert srp.normalise("Contra Celsum, I.") == srp.normalise("contra  celsum i")
    assert srp.normalise("Café") == "cafe"


def test_single_row_is_chosen():
    assert srp.pick_row("w.source.a", {"work": "x"}, [row("f--a", "A")])[0] == "f--a"


def test_work_text_picks_one_of_several():
    rows = [row("f--one", "On the Spirit"), row("f--two", "On Baptism")]
    assert srp.pick_row("w.source.zzz", {"work": "on baptism."}, rows)[0] == "f--two"


def test_id_slug_picks_one_of_several():
    rows = [row("f--on-baptism", "Baptism"), row("f--on-spirit", "Spirit")]
    assert srp.pick_row("w.source.on-spirit", {"work": "unrelated"}, rows)[0] == "f--on-spirit"


def test_no_unique_match_is_ambiguous():
    rows = [row("f--one", "A"), row("f--two", "B")]
    row_id, reason = srp.pick_row("w.source.zzz", {"work": "C"}, rows)
    assert row_id is None and "share the file" in reason


def test_duplicate_work_text_is_ambiguous():
    rows = [row("f--one", "Same"), row("f--two", "same")]
    row_id, reason = srp.pick_row("w.source.zzz", {"work": "Same"}, rows)
    assert row_id is None and "2 rows" in reason


def test_insert_adds_exactly_one_line_after_kind():
    out = srp.insert_shelf_row(RECORD, "f--a")
    lines = out.splitlines(keepends=True)
    assert len(lines) == len(RECORD.splitlines(keepends=True)) + 1
    assert lines[4] == "shelf_row: f--a\n"
    assert out.replace("shelf_row: f--a\n", "") == RECORD


def test_insert_preserves_crlf():
    crlf = RECORD.replace("\n", "\r\n")
    out = srp.insert_shelf_row(crlf, "f--a")
    assert out.replace("shelf_row: f--a\r\n", "") == crlf


def test_insert_refuses_without_kind_line():
    with pytest.raises(ValueError):
        srp.insert_shelf_row(RECORD.replace("kind: vendored\n", ""), "f--a")


def test_insert_refuses_non_scalar_row_id():
    with pytest.raises(ValueError):
        srp.insert_shelf_row(RECORD, "a: b")


def test_append_section_is_append_only_and_once(tmp_path):
    path = tmp_path / "amb.md"
    outcome = srp.Outcome("w.source.x", Path("x"), "ambiguous", candidates=["f--a", "f--b"], reason="why")
    assert srp.append_section(path, "w", [outcome])
    first = path.read_text()
    assert not srp.append_section(path, "w", [outcome])
    assert srp.append_section(path, "v", [])
    assert path.read_text().startswith(first.rstrip("\n"))
