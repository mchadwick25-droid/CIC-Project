from engine.m10.gaps import check_gaps, extract_items

from .fixture_world import write

LEDGER = """# Open Gaps

- 2026-09-01: the dating of the Lerins customs is disputed among editors.
- 2026-09-02: women's own words from the island community do not survive.
"""


def _world(tmp_path, ledger=LEDGER, review=None):
    if ledger is not None:
        write(tmp_path, "Build/worlds/w/Open_Gaps_Tracking.md", ledger)
    write(tmp_path, "Build/worlds/w/Doc_01_Review_Round1.md", review or "# Review\n\nNothing open.\n")
    return tmp_path


def test_extracts_items_under_open_headings_and_inline_labels():
    text = (
        "# Doc\n\n## Open items\n\n- First thing left undecided.\n- Second thing left undecided.\n\n## Sources\n\n- Not an item.\n\n"
        "Open question: who wrote the preface?\n"
    )
    found = [t for _, t in extract_items(text)]
    assert found == ["First thing left undecided.", "Second thing left undecided.", "who wrote the preface?"]


def test_matched_item_passes(tmp_path):
    review = "## Open items\n\n- The dating of the Lerins customs remains disputed among editors.\n"
    assert check_gaps("w", _world(tmp_path, review=review)) == []


def test_unmatched_item_is_reported_with_file_and_line(tmp_path):
    review = "# R\n\n## Open items\n\n- The abbot's rule text survives in one damaged manuscript only.\n"
    findings = check_gaps("w", _world(tmp_path, review=review))
    assert [f.check for f in findings] == ["gaps-unmatched"]
    assert findings[0].path.endswith("Doc_01_Review_Round1.md:5")


def test_missing_ledger(tmp_path):
    findings = check_gaps("w", _world(tmp_path, ledger=None))
    assert [f.check for f in findings] == ["gaps-ledger"]


def test_bare_number_cross_reference_needs_subject_and_date(tmp_path):
    ledger = LEDGER + "- See gap 4 for the rest.\n- See gap 4 (Lerins customs dating, 2026-09-01).\n"
    findings = check_gaps("w", _world(tmp_path, ledger=ledger))
    assert [f.check for f in findings] == ["gaps-crossref"]
    assert findings[0].path.endswith(":5")


def test_ledger_itself_is_not_scanned_for_items(tmp_path):
    ledger = LEDGER + "\n## Open items\n\n- Something only the ledger lists.\n"
    assert check_gaps("w", _world(tmp_path, ledger=ledger)) == []
