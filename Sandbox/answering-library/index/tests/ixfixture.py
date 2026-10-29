import json
from pathlib import Path
from types import SimpleNamespace

from index.catalog import FileEntry
from index.contract import Passage

FILE_NAME = "fixture_de-lapsis-lat_test.txt"

DIVISIONS = {
    "1": ("On the lapsed", [
        "Cyprian writes that peace was given to the church after the persecution, and that some had fallen away.",
        "He warns the lapsed to confess their fault before the bishops and to wait for the judgment of the church.",
        "The letter turns to those who offered sacrifice and asks them to show repentance in works.",
    ]),
    "2": ("On unity", [
        "The bishop urges the brethren to keep one body in the unity of the church.",
        "Whoever is separated from the church is separated from the promises of Christ, he says.",
    ]),
    "3": ("Preface", [
        "Printed at Vienna by the editor Hartel in the year 1868.",
    ]),
}


def write_fixture(directory: Path, name: str = FILE_NAME) -> tuple[list[Passage], FileEntry]:
    directory.mkdir(parents=True, exist_ok=True)
    body = ""
    passages = []
    ordinal = 0
    for locus, (title, texts) in DIVISIONS.items():
        for text in texts:
            start = len(body.encode("utf-8"))
            body += text
            end = len(body.encode("utf-8"))
            body += "\n\n"
            ordinal += 1
            passages.append(Passage(
                passage_id=f"{name}:{locus}:{ordinal}", file=name, division_locus=locus, division_title=title,
                ordinal=ordinal, text=text, word_count=len(text.split()), language="lat", script="latin",
                apparatus=(locus == "3"), speaker_state="known" if ordinal % 2 else "mixed",
                speaker_voice="Cyprian" if ordinal % 2 else None, ocr_score=0.95 if ordinal < 5 else 0.55,
                byte_start=start, byte_end=end, row_ids=("lpc.row.one",), worlds=("lpc",),
            ))
    (directory / name).write_text(body, encoding="utf-8")
    entry = FileEntry(file=name, size_bytes=len(body.encode()), worlds={"lpc"}, rows=[{
        "world": "lpc", "row_id": "lpc.row.one", "role": "tradition", "work": "De lapsis", "author": "cyprian", "locus": "whole",
    }])
    return passages, entry


def write_passage_jsonl(path: Path, passages: list[Passage]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        for p in passages:
            handle.write(json.dumps({
                "passage_id": p.passage_id, "file": p.file, "division_locus": p.division_locus, "division_title": p.division_title,
                "ordinal": p.ordinal, "text": p.text, "word_count": p.word_count, "language": p.language, "script": p.script,
                "apparatus": p.apparatus, "speaker": {"state": p.speaker_state, "voice": p.speaker_voice}, "ocr_score": p.ocr_score,
                "byte_start": p.byte_start, "byte_end": p.byte_end, "row_ids": list(p.row_ids), "worlds": list(p.worlds),
            }) + "\n")


class FakeMessages:
    def __init__(self, reply="This passage from Cyprian's letter on the lapsed sits in the first division, after the opening on peace."):
        self.requests = []
        self.reply = reply

    def create(self, **kwargs):
        self.requests.append(kwargs)
        return SimpleNamespace(
            content=[SimpleNamespace(type="text", text=self.reply)],
            usage=SimpleNamespace(input_tokens=60, output_tokens=40, cache_creation_input_tokens=0, cache_read_input_tokens=5000),
        )


class FakeClient:
    def __init__(self, reply=None):
        self.messages = FakeMessages(*([reply] if reply else []))
