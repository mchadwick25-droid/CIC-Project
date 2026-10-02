"""The narrow rule for the build gates (engine/m10) and the review-file header
fields: code lines that name the vocabulary a gate detects, and header field
names, are not commentary. Nothing else is loosened."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from tools import check_live_commentary as clc


def _scan(tmp_path: Path, rel: str, text: str):
    path = tmp_path / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return {h.line: h.category for h in clc.scan_file(tmp_path, path, "engine")}


def test_a_gate_code_line_naming_the_reviewer_field_is_kept(tmp_path):
    hits = _scan(tmp_path, "engine/m10/x.py", 'FIELD = "Reviewer model"\n')
    assert hits == {1: "KEEP"}


def test_a_gate_comment_saying_the_same_is_still_flagged(tmp_path):
    hits = _scan(tmp_path, "engine/m10/x.py", "# the reviewer changed this after round 2\nX = 1\n")
    assert hits and set(hits.values()) <= {"REWRITE", "ROUTE"}


def test_a_gate_docstring_saying_the_same_is_still_flagged(tmp_path):
    hits = _scan(tmp_path, "engine/m10/x.py", 'def f():\n    """The reviewer asked for this in round 2."""\n')
    assert any(c in ("REWRITE", "ROUTE") for c in hits.values())


def test_a_gate_code_line_with_other_process_vocabulary_is_still_flagged(tmp_path):
    hits = _scan(tmp_path, "engine/m10/x.py", 'NOTE = "revised after round 2 by ruling R41"\n')
    assert any(c in ("REWRITE", "ROUTE") for c in hits.values())


def test_the_rule_does_not_reach_other_modules(tmp_path):
    hits = _scan(tmp_path, "engine/m4/x.py", 'FIELD = "Reviewer model"\n')
    assert hits and set(hits.values()) <= {"REWRITE", "ROUTE"}


def test_a_gate_test_fixture_string_is_protected_but_its_comment_is_not(tmp_path):
    text = 'CASE = "Revised after Round 2 review by the reviewer"\n# revised after round 2 review by the reviewer\n'
    hits = _scan(tmp_path, "engine/m10/tests/test_x.py", text)
    assert hits[1] == "PROTECTED"
    assert hits[2] in ("REWRITE", "ROUTE")


def test_a_trailing_comment_on_a_code_line_is_still_scanned(tmp_path):
    hits = _scan(tmp_path, "engine/m10/x.py", 'X = 1  # the reviewer changed this\n')
    assert hits and set(hits.values()) <= {"REWRITE", "ROUTE"}


def test_a_review_header_field_line_is_kept(tmp_path):
    text = "Reviewer model: claude-opus-5-5\nDrafter model: claude-sonnet-5-5\nReviewer agent: r-1\nDrafter agent: d-1\nReviewer agent:\nDrafter model:\n"
    hits = _scan(tmp_path, "Build/reference/L4-Templates/Review_File_Header_Template.md", text)
    assert set(hits.values()) <= {"KEEP"}


def test_a_prose_line_that_starts_with_reviewer_is_still_flagged(tmp_path):
    hits = _scan(tmp_path, "Build/reference/x.md", "The reviewer asked us to change this in round 2.\n")
    assert hits and set(hits.values()) <= {"REWRITE", "ROUTE"}


def test_python_code_lines_exclude_docstrings_and_comments():
    text = '"""Module doc."""\n# note\nX = """a\nb"""\n\n\ndef f():\n    """Doc."""\n    return 1  # tail\n'
    assert clc._python_code_lines(text) == {3, 4, 7}
