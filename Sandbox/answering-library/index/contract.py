import json
from dataclasses import dataclass, field
from pathlib import Path

REQUIRED_FIELDS = (
    "passage_id", "file", "division_locus", "division_title", "ordinal", "text", "word_count",
    "language", "script", "apparatus", "speaker", "ocr_score", "byte_start", "byte_end", "row_ids", "worlds",
)


class ContractError(ValueError):
    pass


@dataclass(frozen=True)
class Passage:
    passage_id: str
    file: str
    division_locus: str
    division_title: str
    ordinal: int
    text: str
    word_count: int
    language: str
    script: str
    apparatus: bool
    speaker_state: str
    speaker_voice: str | None
    ocr_score: float | None
    byte_start: int
    byte_end: int
    row_ids: tuple[str, ...] = field(default_factory=tuple)
    worlds: tuple[str, ...] = field(default_factory=tuple)

    @classmethod
    def from_record(cls, record: dict) -> "Passage":
        missing = [name for name in REQUIRED_FIELDS if name not in record]
        if missing:
            raise ContractError(f"passage record lacks {', '.join(missing)}")
        speaker = record["speaker"] or {}
        return cls(
            passage_id=record["passage_id"], file=record["file"], division_locus=str(record["division_locus"]),
            division_title=record["division_title"] or "", ordinal=int(record["ordinal"]), text=record["text"],
            word_count=int(record["word_count"]), language=record["language"] or "", script=record["script"] or "",
            apparatus=bool(record["apparatus"]), speaker_state=speaker.get("state") or "unknown",
            speaker_voice=speaker.get("voice"), ocr_score=record["ocr_score"],
            byte_start=int(record["byte_start"]), byte_end=int(record["byte_end"]),
            row_ids=tuple(record["row_ids"] or ()), worlds=tuple(record["worlds"] or ()),
        )


def read_passages(path: Path) -> list[Passage]:
    passages = []
    with open(path, encoding="utf-8") as handle:
        for number, line in enumerate(handle, 1):
            if line.strip():
                try:
                    passages.append(Passage.from_record(json.loads(line)))
                except (json.JSONDecodeError, ContractError) as error:
                    raise ContractError(f"{path}:{number}: {error}") from error
    passages.sort(key=lambda p: (p.byte_start, p.ordinal))
    return passages


def passages_dir(out_dir: Path) -> Path:
    return out_dir / "passages"


def has_segmenter_output(out_dir: Path) -> bool:
    directory = passages_dir(out_dir)
    return directory.is_dir() and any(directory.glob("*.jsonl"))


def file_stem(file_name: str) -> str:
    return Path(file_name).stem


def read_file_passages(out_dir: Path, file_name: str) -> list[Passage] | None:
    path = passages_dir(out_dir) / f"{file_stem(file_name)}.jsonl"
    return read_passages(path) if path.is_file() else None
