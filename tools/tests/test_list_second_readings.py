"""The second-reading list (tools/list_second_readings.py): a span its card holds with a verdict is carried,
a new or changed span goes to a blind reader, and an entry the brief no longer quotes is stale."""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
from list_second_readings import listing, main  # noqa: E402

BRIEF = 'He wrote: "Love the work, and the work will keep you." Then, he says, "Keep the rule," and "stay."'


def entry(modern, verdict="same"):
    e = {"modern": modern, "printed": "x", "work": "x", "file": "x", "lines": "1"}
    if verdict:
        e["secondReading"] = verdict
    return e


def test_a_held_span_is_carried_and_a_broken_quotation_is_one_entry():
    card = {"quotationOriginals": [entry("Love the work, and the work will keep you."), entry("Keep the rule, stay.", "minor")]}
    r = listing(BRIEF, card)
    assert [s["status"] for s in r["spans"]] == ["CARRIED", "CARRIED"]
    assert r["spans"][1]["secondReading"] == "minor"
    assert r["stale"] == []


def test_a_new_span_or_one_without_a_verdict_is_read_blind_and_a_short_one_is_checked_at_card():
    card = {"quotationOriginals": [entry("Love the work, and the work will keep you.", None)]}
    r = listing(BRIEF, card)
    assert [s["status"] for s in r["spans"]] == ["READ BLIND", "CHECK AT CARD", "CHECK AT CARD"]


def test_a_short_entry_counts_all_its_spans_and_carries_checked_at_card():
    card = {"quotationOriginals": [entry("Love the work, and the work will keep you."), entry("Keep the rule, stay.", None)]}
    assert [s["status"] for s in listing(BRIEF, card)["spans"]] == ["CARRIED", "CHECK AT CARD"]
    card["quotationOriginals"][1]["secondReading"] = "checked at card"
    assert [s["status"] for s in listing(BRIEF, card)["spans"]] == ["CARRIED", "CARRIED"]


def test_a_changed_span_is_read_blind_and_its_old_entry_is_stale():
    card = {"quotationOriginals": [entry("Love the work, and the work will guard you."), entry("Keep the rule, stay.")]}
    r = listing(BRIEF, card)
    assert r["spans"][0]["status"] == "READ BLIND"
    assert r["stale"] == ["Love the work, and the work will guard you."]


def test_the_released_batch_three_is_fully_carried(capsys):
    batch = ROOT / "Build/Ministry/Operations/Audits/2026-11-17_batch-3"
    folders = [str(p) for p in sorted(batch.iterdir()) if (p / f"{p.name}.card.json").exists()]
    assert len(folders) == 12
    assert main(folders) == 0


def test_main_exits_one_when_a_blind_reading_is_owed(tmp_path):
    d = tmp_path / "someone"
    d.mkdir()
    (d / "someone.brief.txt").write_text(BRIEF, encoding="utf-8")
    (d / "someone.card.json").write_text(json.dumps({"quotationOriginals": []}), encoding="utf-8")
    assert main([str(d)]) == 1
