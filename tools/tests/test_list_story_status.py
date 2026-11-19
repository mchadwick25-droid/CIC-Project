"""The story ledger (tools/list_story_status.py): a story in a numbered batch folder is on the kit at its
latest batch, a draft copy is not counted, and a finished story the census lacks is listed."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
from list_story_status import kit_batches, ledger, render  # noqa: E402


def brief(audits, folder, slug, name=None):
    d = audits / folder / slug
    d.mkdir(parents=True, exist_ok=True)
    (d / f"{name or slug}.brief.txt").write_text("x")


def test_latest_numbered_batch_wins_and_drafts_and_other_folders_do_not_count(tmp_path):
    brief(tmp_path, "2026-11-17_batch-3", "arius")
    brief(tmp_path, "2026-11-18_batch-4", "arius")
    brief(tmp_path, "2026-11-18_batch-4", "macrina", "macrina.r50")
    brief(tmp_path, "2026-11-17_varied-batch", "antony")
    assert kit_batches(tmp_path) == {"arius": 4}


def test_ledger_splits_kit_and_to_do_and_lists_missing():
    census = {"movements": [
        {"id": "arius", "name": "Arius", "era": 2, "kind": "person"},
        {"id": "nicaea", "name": "Council of Nicaea", "era": 2, "kind": "major-council"},
        {"id": "a-river", "name": "A river", "era": 2},
    ]}
    r = ledger(census, {"arius": 3, "cyril-and-methodius": 4}, {"arius"})
    assert [(x["id"], x["batch"], x["audio"]) for x in r["rows"]] == [("arius", 3, True), ("nicaea", None, False)]
    assert r["not_in_census"] == [("cyril-and-methodius", 4)]
    text = render(r)
    assert "1 of 2 people and major councils are on the brief kit" in text
    assert "Council of Nicaea (`nicaea`, council)" in text


def test_an_earlier_approved_text_is_named_on_its_to_do_line_until_the_kit_has_it():
    census = {"movements": [{"id": "polycarp", "name": "Polycarp", "era": 1, "kind": "person"},
                            {"id": "origen", "name": "Origen", "era": 1, "kind": "person"}]}
    earlier = {"polycarp": {"text": "a/polycarp.brief.txt", "approved": "2026-11-16"},
               "origen": {"text": "bar/origen.brief.txt", "approved": "2026-11-16"}}
    r = ledger(census, {"origen": 6}, set(), earlier)
    text = render(r)
    assert "Polycarp (`polycarp`, approved earlier, not live)" in text
    assert "- Polycarp: `a/polycarp.brief.txt` (2026-11-16)" in text
    assert "bar/origen.brief.txt" not in text
