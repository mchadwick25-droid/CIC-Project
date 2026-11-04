"""Reading cards and modern-lens notes for a world's quotes and stories, read
straight from the record files' front matter under records/<world>/. Both
fields are stripped at compile, so no package carries them; this loader is
the one way to reach them, and only a test harness calls it."""
from pathlib import Path

from engine.m1.loader import parse_record_text

READING_RECORD_TYPES = ("quote", "story")


def load_reading_context(records_dir: Path, world: str) -> dict[str, dict]:
    """record id -> {"reading_card": ..., "modern_lens_note": ...} for every
    quote and story record of `world` that carries either field; a field the
    record lacks is None."""
    world_dir = Path(records_dir) / world
    if not world_dir.is_dir():
        return {}
    context: dict[str, dict] = {}
    for path in sorted(world_dir.glob("*/*.md")):
        record = parse_record_text(path.read_text(encoding="utf-8"), str(path))
        if record.get("record_type") not in READING_RECORD_TYPES:
            continue
        card, note = record.get("reading_card"), record.get("modern_lens_note")
        if card is None and note is None:
            continue
        context[record["id"]] = {"reading_card": card, "modern_lens_note": note}
    return context
