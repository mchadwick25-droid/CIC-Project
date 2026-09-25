"""Unit tests for tools/repin_stale_worlds.py's _early_exit() - the check
that used to require REPIN_PR_TOKEN unconditionally, even on a push that
left every world's pin current. _early_exit() is a plain function of its
inputs (no git, no network), so these tests exercise both real paths
directly.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from tools.repin_stale_worlds import _early_exit


def test_nothing_stale_exits_0_without_a_token():
    assert _early_exit({}, None) == 0
    assert _early_exit({}, "") == 0


def test_something_stale_without_a_token_exits_1(capsys):
    result = _early_exit({"alx": {"reason": "corpus-map changed"}}, None)
    assert result == 1
    captured = capsys.readouterr()
    assert "REPIN_PR_TOKEN" in captured.err
    assert "alx" in captured.err


def test_something_stale_with_a_token_keeps_going():
    assert _early_exit({"alx": {"reason": "corpus-map changed"}}, "a-real-token") is None
