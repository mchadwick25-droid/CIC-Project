"""Tests for gen_needs_ruling.py's hand-maintained-tail preservation.

Everything from `HAND_MAINTAINED_MARKER` to end of file in an existing
NEEDS-RULING.md is hand-maintained, not derived from cic/corpus-map/: a
regeneration reads it back from the previous run and reproduces it verbatim
rather than overwriting it. An existing file that has lost its marker makes
`main()` refuse to write, since treating a missing marker as "nothing to
preserve" would lose real hand-added content silently.

    python -m pytest Build/worlds/_cross-world/tests_gen_needs_ruling.py
"""
import pathlib
import sys

import pytest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import gen_needs_ruling as g  # noqa: E402


def test_extract_hand_maintained_preserves_content_verbatim():
    existing = (
        "# Needs-ruling\n\nGenerated content here.\n\n"
        f"{g.HAND_MAINTAINED_MARKER}\n\n"
        "## A hand-added finding\n\nReal editorial content that no script produces.\n"
    )
    tail = g.extract_hand_maintained(existing)
    assert "## A hand-added finding" in tail
    assert "Real editorial content that no script produces." in tail
    assert tail.startswith(g.HAND_MAINTAINED_MARKER)


def test_extract_hand_maintained_survives_a_second_extraction():
    # Simulates two regenerations in a row: the tail extracted from run 1's
    # output, fed back in as run 2's "existing" file, must come back
    # unchanged - this is what "no entry is lost" means in practice.
    existing = (
        "# Needs-ruling\n\nGenerated content here.\n\n"
        f"{g.HAND_MAINTAINED_MARKER}\n\n"
        "## A hand-added finding\n\nReal editorial content.\n"
    )
    tail_1 = g.extract_hand_maintained(existing)
    rebuilt = "# Needs-ruling\n\nDIFFERENT generated content this run.\n\n" + tail_1
    tail_2 = g.extract_hand_maintained(rebuilt)
    assert tail_1.rstrip("\n") == tail_2.rstrip("\n")


def test_extract_hand_maintained_refuses_when_an_existing_file_lacks_the_marker():
    # An existing (non-None) file with no marker at all must not be treated
    # as if it had nothing to preserve - that is exactly the data-loss bug
    # this function exists to prevent. It raises instead of falling back to
    # a placeholder that would silently discard any real content below some
    # other heading.
    with pytest.raises(g.MissingMarkerError):
        g.extract_hand_maintained("# Needs-ruling\n\nNo marker anywhere in this file.\n")


def test_extract_hand_maintained_handles_first_run_with_no_existing_file():
    tail = g.extract_hand_maintained(None)
    assert tail == g.HAND_MAINTAINED_PLACEHOLDER


def test_real_needs_ruling_file_hand_maintained_tail_survives_a_real_regeneration(tmp_path, monkeypatch):
    """End-to-end: run the actual generator (against the real cic/corpus-map/
    data) with TARGET_FILE redirected to a scratch copy of the real
    NEEDS-RULING.md, and confirm the hand-maintained tail comes back
    byte-for-byte (modulo trailing whitespace)."""
    real_file = pathlib.Path(__file__).resolve().parent / "NEEDS-RULING.md"
    scratch = tmp_path / "NEEDS-RULING.md"
    scratch.write_text(real_file.read_text(encoding="utf-8"), encoding="utf-8")

    before = scratch.read_text(encoding="utf-8")
    assert g.HAND_MAINTAINED_MARKER in before, (
        "the real NEEDS-RULING.md must carry the marker for this test to mean anything"
    )
    before_tail = before[before.index(g.HAND_MAINTAINED_MARKER):].rstrip()

    monkeypatch.setattr(g, "TARGET_FILE", scratch)
    g.main()

    after = scratch.read_text(encoding="utf-8")
    after_tail = after[after.index(g.HAND_MAINTAINED_MARKER):].rstrip()
    assert before_tail == after_tail, "hand-maintained tail must survive a real regeneration unchanged"


def test_main_refuses_to_write_when_an_existing_file_lacks_the_marker(tmp_path, monkeypatch, capsys):
    """End-to-end: `main()` against a scratch file that exists but has no
    marker must leave that file untouched rather than overwrite it - the
    exact case the round-1 data-loss bug missed."""
    scratch = tmp_path / "NEEDS-RULING.md"
    before = "# Needs-ruling\n\nSome prior content, no marker at all.\n"
    scratch.write_text(before, encoding="utf-8")

    monkeypatch.setattr(g, "TARGET_FILE", scratch)
    g.main()

    after = scratch.read_text(encoding="utf-8")
    assert after == before, "a missing marker on an existing file must not be written over"
    assert "refusing to write" in capsys.readouterr().out


def test_generator_is_idempotent_on_a_second_run(tmp_path, monkeypatch):
    real_file = pathlib.Path(__file__).resolve().parent / "NEEDS-RULING.md"
    scratch = tmp_path / "NEEDS-RULING.md"
    scratch.write_text(real_file.read_text(encoding="utf-8"), encoding="utf-8")

    monkeypatch.setattr(g, "TARGET_FILE", scratch)
    g.main()
    first = scratch.read_text(encoding="utf-8")
    g.main()
    second = scratch.read_text(encoding="utf-8")
    assert first == second, "running the generator twice in a row must be a no-op"
