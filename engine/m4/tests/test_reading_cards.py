"""The test-time loader for reading cards and modern-lens notes reads record
front matter straight from records/<world>/."""
import yaml

from engine.m1.loader import RECORDS_ROOT
from engine.m4.reading_cards import load_reading_context

CARD = {
    "setting": "A letter to a friend.",
    "historians_conclude": {"text": "Read as a private letter.", "confidence": "Widely Accepted"},
    "sources": {"setting": "w.source.letters, Ep. 1", "historians_conclude": "Doc_05, section 2"},
}


def _write(path, front_matter):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("---\n" + yaml.safe_dump(front_matter, sort_keys=False) + "---\nBody.\n", encoding="utf-8")


def test_the_loader_returns_the_card_and_the_lens_note(tmp_path):
    _write(tmp_path / "w" / "quote" / "w.quote.a.md", {
        "id": "w.quote.a", "record_type": "quote", "modern_lens_note": "Today it reads as a private note.", "reading_card": CARD,
    })
    _write(tmp_path / "w" / "story" / "w.story.b.md", {"id": "w.story.b", "record_type": "story", "reading_card": CARD})
    _write(tmp_path / "w" / "quote" / "w.quote.plain.md", {"id": "w.quote.plain", "record_type": "quote"})
    _write(tmp_path / "w" / "gravity" / "w.gravity.g.md", {"id": "w.gravity.g", "record_type": "gravity", "reading_card": CARD})
    _write(tmp_path / "other" / "quote" / "other.quote.c.md", {"id": "other.quote.c", "record_type": "quote", "reading_card": CARD})

    context = load_reading_context(tmp_path, "w")

    assert context == {
        "w.quote.a": {"reading_card": CARD, "modern_lens_note": "Today it reads as a private note."},
        "w.story.b": {"reading_card": CARD, "modern_lens_note": None},
    }


def test_the_loader_reads_the_real_alx_lens_notes_and_cards():
    context = load_reading_context(RECORDS_ROOT, "alx")
    entry = context["alx.quote.a-doctrine-they-would-not-have-taught"]
    assert entry["modern_lens_note"].startswith("The argument is about sincerity")
    assert set(entry["reading_card"]) >= {"setting", "source_says", "historians_conclude", "sources"}
    assert sum(1 for e in context.values() if e["reading_card"]) == 35


def test_a_missing_world_returns_nothing(tmp_path):
    assert load_reading_context(tmp_path, "nowhere") == {}
