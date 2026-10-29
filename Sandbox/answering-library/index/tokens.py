import json
import re
from dataclasses import dataclass
from pathlib import Path

# Characters per token by script, as (low-token ratio, high-token ratio). No tokenizer runs offline;
# the first live sample's measured usage replaces these for the cost bands.
CHARS_PER_TOKEN = {
    "latin": (4.0, 3.2),
    "greek": (2.4, 1.5),
    "other": (2.4, 1.5),
}

_GREEK = re.compile(r"[Ͱ-Ͽἀ-῿]")
_OTHER = re.compile(r"[Ѐ-ԯ֐-ࣿऀ-᳿Ⰰ-퟿]")
_WORD = re.compile(r"\S+")


@dataclass(frozen=True)
class TextStats:
    chars: int
    words: int
    greek_chars: int
    other_chars: int

    @property
    def latin_chars(self) -> int:
        return self.chars - self.greek_chars - self.other_chars

    def tokens(self, band: str) -> int:
        index = 0 if band == "low" else 1
        total = (
            self.latin_chars / CHARS_PER_TOKEN["latin"][index]
            + self.greek_chars / CHARS_PER_TOKEN["greek"][index]
            + self.other_chars / CHARS_PER_TOKEN["other"][index]
        )
        return int(total) + 1

    def to_dict(self) -> dict:
        return {"chars": self.chars, "words": self.words, "greek_chars": self.greek_chars, "other_chars": self.other_chars}

    @classmethod
    def from_dict(cls, data: dict) -> "TextStats":
        return cls(data["chars"], data["words"], data["greek_chars"], data["other_chars"])


def text_stats(text: str) -> TextStats:
    return TextStats(
        chars=len(text), words=len(_WORD.findall(text)),
        greek_chars=len(_GREEK.findall(text)), other_chars=len(_OTHER.findall(text)),
    )


def estimate_tokens(text: str, band: str = "high") -> int:
    return text_stats(text).tokens(band)


def file_stats(path: Path, cache_path: Path | None = None) -> TextStats:
    key = f"{path.name}:{path.stat().st_size}:{int(path.stat().st_mtime)}"
    cache = {}
    if cache_path is not None and cache_path.is_file():
        cache = json.loads(cache_path.read_text(encoding="utf-8"))
    if key in cache:
        return TextStats.from_dict(cache[key])
    stats = text_stats(path.read_text(encoding="utf-8", errors="replace"))
    if cache_path is not None:
        cache[key] = stats.to_dict()
        cache_path.parent.mkdir(parents=True, exist_ok=True)
        cache_path.write_text(json.dumps(cache, sort_keys=True), encoding="utf-8")
    return stats
