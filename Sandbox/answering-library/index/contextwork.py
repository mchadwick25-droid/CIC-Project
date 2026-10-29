import json
from dataclasses import dataclass
from pathlib import Path
from typing import Mapping, Sequence

from . import contract
from .catalog import FileEntry
from .check import check_context_line
from .contract import Passage
from .generate import context_path, text_hash
from .prompting import PROMPT_VERSION, SYSTEM_PROMPT
from .windows import NEIGHBOR_WORDS

SESSION_MODEL_PREFIX = "claude-code-session:"
BATCH_PASSAGES = 12
HEAD_WORDS = 110
TAIL_WORDS = 30


def neighbourhood(passages: Sequence[Passage], anchors: Sequence[str], radius: int) -> list[Passage]:
    """The anchor passages and the `radius` passages before and after each, in file order."""
    position = {p.passage_id: i for i, p in enumerate(passages)}
    keep: set[int] = set()
    for anchor in anchors:
        if anchor in position:
            i = position[anchor]
            keep.update(range(max(0, i - radius), min(len(passages), i + radius + 1)))
    return [passages[i] for i in sorted(keep)]


def excerpt(text: str, head: int = HEAD_WORDS, tail: int = TAIL_WORDS) -> str:
    words = text.split()
    if len(words) <= head + tail + 20:
        return " ".join(words)
    return " ".join(words[:head]) + " [...] " + " ".join(words[-tail:])


def _edge_before(passages: Sequence[Passage], first: int) -> str:
    return " ".join(passages[first - 1].text.split()[-NEIGHBOR_WORDS:]) if first > 0 else ""


def batches(passages: Sequence[Passage], chosen: Sequence[Passage], size: int = BATCH_PASSAGES) -> list[list[Passage]]:
    """Runs of chosen passages that are adjacent in the file, cut at `size`."""
    position = {p.passage_id: i for i, p in enumerate(passages)}
    runs: list[list[Passage]] = []
    for passage in chosen:
        if runs and position[passage.passage_id] == position[runs[-1][-1].passage_id] + 1 and len(runs[-1]) < size:
            runs[-1].append(passage)
        else:
            runs.append([passage])
    return runs


def packet_lines(entry: FileEntry, passages: Sequence[Passage], batch: Sequence[Passage], batch_id: str) -> list[dict]:
    position = {p.passage_id: i for i, p in enumerate(passages)}
    first = position[batch[0].passage_id]
    head = {
        "batch_id": batch_id, "prompt_version": PROMPT_VERSION, "instruction": SYSTEM_PROMPT, "work_header": entry.header(),
        "file": entry.file, "targets": [p.passage_id for p in batch], "before": _edge_before(passages, first),
    }
    body = [
        {"passage_id": p.passage_id, "division_locus": p.division_locus, "division_title": p.division_title,
         "text_hash": text_hash(p.text), "language": p.language, "text": excerpt(p.text)}
        for p in batch
    ]
    return [head] + body


def write_packets(directory: Path, entry: FileEntry, passages: Sequence[Passage], chosen: Sequence[Passage]) -> list[Path]:
    stem = contract.file_stem(entry.file)
    target = directory / stem
    target.mkdir(parents=True, exist_ok=True)
    written = []
    for number, batch in enumerate(batches(passages, chosen), 1):
        path = target / f"{number:04d}.in.jsonl"
        lines = packet_lines(entry, passages, batch, f"{stem}/{number:04d}")
        path.write_text("\n".join(json.dumps(line, ensure_ascii=False) for line in lines) + "\n", encoding="utf-8")
        written.append(path)
    return written


def read_packet(path: Path) -> tuple[dict, list[dict]]:
    lines = [json.loads(raw) for raw in path.read_text(encoding="utf-8").splitlines() if raw.strip()]
    return lines[0], lines[1:]


def answer_path(packet: Path) -> Path:
    return packet.with_name(packet.name.replace(".in.jsonl", ".out.jsonl"))


class RefusedBatch(ValueError):
    pass


def read_answers(path: Path, head: dict, body: Sequence[dict]) -> dict[str, dict]:
    answers: dict[str, dict] = {}
    for raw in path.read_text(encoding="utf-8").splitlines():
        if not raw.strip():
            continue
        record = json.loads(raw)
        if record["passage_id"] in answers:
            raise RefusedBatch(f"{path.name}: repeats {record['passage_id']}")
        answers[record["passage_id"]] = record
    expected = {line["passage_id"]: line for line in body}
    extra = set(answers) - set(expected)
    missing = set(expected) - set(answers)
    if extra:
        raise RefusedBatch(f"{path.name}: names passage(s) not in the packet: {sorted(extra)[:3]}")
    if missing:
        raise RefusedBatch(f"{path.name}: omits {len(missing)} passage(s), first {sorted(missing)[0]}")
    for pid, record in answers.items():
        if record["text_hash"] != expected[pid]["text_hash"]:
            raise RefusedBatch(f"{path.name}: text_hash differs for {pid}")
    return answers


def supplied_text(entry: FileEntry, head: dict, body: Sequence[dict]) -> str:
    parts = [entry.registry_vocabulary(), head["work_header"], head.get("before", "")]
    for line in body:
        parts += [line["division_locus"], line["division_title"], line["text"]]
    return "\n".join(parts)


@dataclass
class ImportResult:
    imported: int = 0
    flagged: int = 0
    refused: int = 0
    refusals: list[str] = None

    def __post_init__(self):
        self.refusals = self.refusals or []


def import_packets(directory: Path, out_dir: Path, entries: Mapping[str, FileEntry], model_name: str) -> ImportResult:
    """Validate each answer file against its packet, check every line against the text the writer was shown, and append
    one record per passage to the file's context log. A batch already imported under the same hash is not written twice."""
    result = ImportResult()
    model_id = SESSION_MODEL_PREFIX + model_name
    for packet in sorted(directory.glob("*/*.in.jsonl")):
        answers_file = answer_path(packet)
        if not answers_file.is_file():
            continue
        head, body = read_packet(packet)
        entry = entries[head["file"]]
        try:
            answers = read_answers(answers_file, head, body)
        except (RefusedBatch, KeyError, json.JSONDecodeError) as error:
            result.refused += 1
            result.refusals.append(str(error))
            continue
        shown = supplied_text(entry, head, body)
        path = context_path(out_dir, head["file"])
        path.parent.mkdir(parents=True, exist_ok=True)
        existing = set()
        if path.is_file():
            existing = {(r["passage_id"], r["text_hash"], r["model_id"], r["prompt_version"])
                        for r in map(json.loads, filter(str.strip, path.read_text(encoding="utf-8").splitlines()))}
        with open(path, "a", encoding="utf-8") as sink:
            for line in body:
                answer = answers[line["passage_id"]]
                key = (line["passage_id"], line["text_hash"], model_id, head["prompt_version"])
                if key in existing:
                    continue
                context = " ".join(answer["context"].split())
                verdict = check_context_line(context, shown)
                sink.write(json.dumps({
                    "passage_id": line["passage_id"], "file": head["file"], "text_hash": line["text_hash"], "model_id": model_id,
                    "prompt_version": head["prompt_version"], "context": context, "status": verdict.status,
                    "reasons": list(verdict.reasons), "usage": None, "live_test": None,
                }, ensure_ascii=False) + "\n")
                result.imported += 1
                result.flagged += 0 if verdict.ok else 1
    return result


def pending_packets(directory: Path) -> list[Path]:
    return [p for p in sorted(directory.glob("*/*.in.jsonl")) if not answer_path(p).is_file()]


def parse_numbered_answers(text: str) -> dict[str, dict[int, str]]:
    """Sections headed `## <batch_id>`, each followed by lines `<n>. <context line>` numbered from 1 in packet order."""
    sections: dict[str, dict[int, str]] = {}
    current: dict[int, str] | None = None
    for raw in text.splitlines():
        line = raw.strip()
        if line.startswith("## "):
            current = sections.setdefault(line[3:].strip(), {})
        elif line and current is not None:
            number, _, sentence = line.partition(". ")
            if not number.isdigit() or not sentence.strip():
                raise RefusedBatch(f"not a numbered line: {line[:60]}")
            if int(number) in current:
                raise RefusedBatch(f"batch repeats line {number}")
            current[int(number)] = sentence.strip()
    return sections


def write_answer_files(directory: Path, sections: dict[str, dict[int, str]]) -> list[Path]:
    written = []
    for batch_id, lines in sections.items():
        packet = directory / f"{batch_id}.in.jsonl"
        if not packet.is_file():
            raise RefusedBatch(f"no packet {batch_id}")
        _, body = read_packet(packet)
        if sorted(lines) != list(range(1, len(body) + 1)):
            raise RefusedBatch(f"{batch_id}: has lines {sorted(lines)}, the packet has {len(body)} passages")
        out = answer_path(packet)
        out.write_text("\n".join(json.dumps({"passage_id": b["passage_id"], "text_hash": b["text_hash"], "context": lines[i]},
                                            ensure_ascii=False) for i, b in enumerate(body, 1)) + "\n", encoding="utf-8")
        written.append(out)
    return written
