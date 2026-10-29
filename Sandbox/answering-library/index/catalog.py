import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
TEXTS_DIR = REPO_ROOT / "cic" / "texts"
DEFAULT_OUT_DIR = REPO_ROOT / "Sandbox" / "answering-library" / "out"

BUILT_WORLDS = ("alx", "cappadocian", "desert", "don", "gallic", "hal", "ijc", "lpc", "pahc", "rzg", "syr", "witt")

LANGUAGE_NAMES = {
    "lat": "Latin", "grc": "Greek", "eng": "English", "fra": "French", "deu": "German", "swe": "Swedish",
    "syr": "Syriac", "rus": "Russian", "ita": "Italian", "spa": "Spanish", "por": "Portuguese",
}
_LANGUAGE_CODE = re.compile(r"-((?:[a-z]{3})(?:-[a-z]{3})*)_")


def _engine_imports():
    if str(REPO_ROOT) not in sys.path:
        sys.path.insert(0, str(REPO_ROOT))
    from engine.m1.registry import load_registry
    from engine.m9.loader import read_bucket_rows

    return load_registry, read_bucket_rows


@dataclass
class FileEntry:
    file: str
    size_bytes: int
    worlds: set[str] = field(default_factory=set)
    rows: list[dict] = field(default_factory=list)

    @property
    def path(self) -> Path:
        return TEXTS_DIR / self.file

    @property
    def is_xml(self) -> bool:
        return self.file.endswith(".xml")

    @property
    def language_codes(self) -> tuple[str, ...]:
        match = _LANGUAGE_CODE.search(self.file)
        if not match:
            return ("eng",) if self.is_xml else ()
        return tuple(code for code in match.group(1).split("-") if code in LANGUAGE_NAMES)

    @property
    def authors(self) -> list[str]:
        return sorted({r["author"] for r in self.rows if r.get("author")})

    @property
    def works(self) -> list[str]:
        return sorted({r["work"] for r in self.rows if r.get("work")})

    def header(self) -> str:
        languages = ", ".join(LANGUAGE_NAMES[c] for c in self.language_codes) or "not stated in the file name"
        lines = [
            f"Vendored file: {self.file}",
            f"Language of the file name: {languages}",
            f"Authors named by the library map: {'; '.join(a.replace('_', ' ') for a in self.authors) or 'none named'}",
            f"Works named by the library map: {'; '.join(self.works[:12]) or 'none named'}",
        ]
        return "\n".join(lines)

    def registry_vocabulary(self) -> str:
        parts = [self.file.replace("_", " ").replace("-", " "), self.header()]
        parts += [r.get("locus") or "" for r in self.rows]
        return "\n".join(parts)


def load_shelves(worlds: tuple[str, ...] = BUILT_WORLDS) -> dict[str, FileEntry]:
    load_registry, read_bucket_rows = _engine_imports()
    registry = load_registry()
    entries: dict[str, FileEntry] = {}
    for world in worlds:
        census_id = registry[world]["census_id"]
        for row in read_bucket_rows(census_id):
            name = row.get("source_file")
            if not name or not (TEXTS_DIR / name).is_file():
                continue
            entry = entries.get(name)
            if entry is None:
                entry = entries[name] = FileEntry(file=name, size_bytes=(TEXTS_DIR / name).stat().st_size)
            entry.worlds.add(world)
            entry.rows.append({
                "world": world, "row_id": row.get("row_id"), "role": row.get("role"), "work": row.get("work"),
                "author": row.get("author"), "locus": row.get("locus"),
            })
    return dict(sorted(entries.items()))


def world_files(shelves: dict[str, FileEntry], world: str) -> list[FileEntry]:
    return [e for e in shelves.values() if world in e.worlds]
