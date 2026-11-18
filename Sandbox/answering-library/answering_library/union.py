"""Union listing of the built worlds' shelves: one entry per distinct vendored
file, with every world and bucket row that claims it."""
from __future__ import annotations

import sys
from dataclasses import dataclass, field
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
TEXTS_DIR = REPO_ROOT / "cic" / "texts"

WORLD_KEYS = (
    "alx", "cappadocian", "desert", "don", "gallic", "hal",
    "ijc", "lpc", "pahc", "rzg", "syr", "witt",
)


@dataclass
class UnionEntry:
    filename: str
    size: int
    worlds: list[str] = field(default_factory=list)
    row_ids: list[str] = field(default_factory=list)
    authors: list[str] = field(default_factory=list)

    @property
    def suffix(self) -> str:
        return Path(self.filename).suffix

    @property
    def path(self) -> Path:
        return TEXTS_DIR / self.filename


def _engine_imports():
    if str(REPO_ROOT) not in sys.path:
        sys.path.insert(0, str(REPO_ROOT))
    from engine.m9.cli import load_registry
    from engine.m9.loader import read_bucket_rows
    return load_registry, read_bucket_rows


def build_union(world_keys=WORLD_KEYS, texts_dir: Path = TEXTS_DIR) -> list[UnionEntry]:
    """Entries sorted largest file first, then by name."""
    load_registry, read_bucket_rows = _engine_imports()
    registry = load_registry()
    by_file: dict[str, UnionEntry] = {}
    for key in world_keys:
        census_id = registry[key]["census_id"]
        for row in read_bucket_rows(census_id):
            name = row.get("source_file")
            if not name:
                continue
            entry = by_file.get(name)
            if entry is None:
                entry = by_file[name] = UnionEntry(filename=name, size=(texts_dir / name).stat().st_size)
            if key not in entry.worlds:
                entry.worlds.append(key)
            if row["row_id"] not in entry.row_ids:
                entry.row_ids.append(row["row_id"])
            author = row.get("author")
            if author and author not in entry.authors:
                entry.authors.append(author)
    for entry in by_file.values():
        entry.worlds.sort()
        entry.row_ids.sort()
        entry.authors.sort()
    return sorted(by_file.values(), key=lambda e: (-e.size, e.filename))
