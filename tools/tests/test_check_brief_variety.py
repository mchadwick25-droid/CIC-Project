"""The batch variety check (tools/check_brief_variety.py): each move is found where it is made and not where it is not,
and on the first twelve as released it finds what the four readers counted by hand (Decision-Log, 2026-11-17)."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
from check_brief_variety import check, moves_in  # noqa: E402


def test_each_move_is_found():
    text = (
        "At the gate of Amiens, a soldier met a beggar.\n\n"
        "The soldier was Martin, in Roman Gaul in the fourth century. Most of what we know comes from one admirer.\n\n"
        "Yet he refused to fight.\n\n"
        "Two centuries later, Gregory of Tours wrote of him."
    )
    assert moves_in(text) == {"reveal", "stacked-setting", "witness-formula", "yet-pivot", "later-ending"}


def test_plain_narration_makes_none():
    text = (
        "Born to pagans in Pannonia, in what is now Hungary, Martin asked at ten to be prepared for baptism.\n\n"
        "He tore down temples and built churches in their place.\n\n"
        "At the midnight bell he ran into the church and knelt at the altar, and there he died."
    )
    assert moves_in(text) == set()


def test_a_move_over_a_quarter_of_the_batch_fails(tmp_path):
    paths = []
    for i in range(8):
        p = tmp_path / f"piece-{i}.brief.txt"
        p.write_text("A man walked.\n\nYet he stayed." if i < 2 else "A man walked.\n\nHe stayed.", encoding="utf-8")
        paths.append(p)
    assert not check(paths)["moves"]["yet-pivot"]["over"]  # 2 of 8 is a quarter, not more
    paths[2].write_text("A man walked.\n\nYet he stayed.", encoding="utf-8")
    result = check(paths)
    assert result["limit"] == 2 and result["moves"]["yet-pivot"]["count"] == 3 and result["moves"]["yet-pivot"]["over"]


def test_the_first_twelve_as_released_match_the_readers_counts():
    audits = ROOT / "Build/Ministry/Operations/Audits"
    released = sorted(p for p in audits.glob("2026-11-17_varied-batch*/*/*.r50.brief.txt") if "how-nicaea" not in p.name)
    assert len(released) == 12
    counts = {k: v["count"] for k, v in check(released)["moves"].items()}
    # The readers counted 8, 10, 6, 7 and 12; the check is within one of each.
    readers = {"reveal": 8, "stacked-setting": 10, "witness-formula": 6, "yet-pivot": 7, "later-ending": 12}
    assert all(abs(counts[k] - n) <= 1 for k, n in readers.items()), counts
