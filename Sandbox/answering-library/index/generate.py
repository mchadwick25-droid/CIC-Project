import hashlib
import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Sequence

from . import contract
from .catalog import FileEntry
from .check import check_context_line
from .contract import Passage
from .estimate import base_tokens
from .prompting import PROMPT_VERSION, allowed_text, build_request, response_text
from .tokens import estimate_tokens
from .windows import Window, build_windows


class LiveTestStop(Exception):
    pass


def text_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def context_dir(out_dir: Path) -> Path:
    return out_dir / "context"


def context_path(out_dir: Path, file_name: str) -> Path:
    return context_dir(out_dir) / f"{contract.file_stem(file_name)}.jsonl"


@dataclass
class Job:
    entry: FileEntry
    passages: list[Passage]

    def windows(self) -> list[Window]:
        base = base_tokens(self.entry, "high")
        return build_windows(self.entry.file, self.passages, lambda p: estimate_tokens(p.text, "high"), base)


def read_context_lines(out_dir: Path, file_name: str) -> dict[str, dict]:
    path = context_path(out_dir, file_name)
    lines: dict[str, dict] = {}
    if path.is_file():
        with open(path, encoding="utf-8") as handle:
            for raw in handle:
                if raw.strip():
                    record = json.loads(raw)
                    lines[record["passage_id"]] = record
    return lines


def is_done(record: dict | None, passage: Passage, model_id: str) -> bool:
    return bool(
        record and record["text_hash"] == text_hash(passage.text)
        and record["model_id"] == model_id and record["prompt_version"] == PROMPT_VERSION
    )


def pending_count(jobs: Sequence[Job], out_dir: Path, model_id: str) -> tuple[int, int]:
    total = pending = 0
    for job in jobs:
        existing = read_context_lines(out_dir, job.entry.file)
        for passage in job.passages:
            total += 1
            if not is_done(existing.get(passage.passage_id), passage, model_id):
                pending += 1
    return total, pending


@dataclass
class RunReport:
    generated: int = 0
    skipped: int = 0
    flagged: int = 0
    stopped: str | None = None
    input_tokens: int = 0
    output_tokens: int = 0
    cache_write_tokens: int = 0
    cache_read_tokens: int = 0
    remaining: int = 0
    files: list[str] = field(default_factory=list)


def _usage_dict(response) -> dict:
    usage = getattr(response, "usage", None)
    return {
        name: int(getattr(usage, name, 0) or 0)
        for name in ("input_tokens", "output_tokens", "cache_creation_input_tokens", "cache_read_input_tokens")
    }


def run_jobs(client, jobs: Sequence[Job], out_dir: Path, model_id: str, live_test_name: str, cap_errors: tuple[type, ...]) -> RunReport:
    report = RunReport()
    directory = context_dir(out_dir)
    directory.mkdir(parents=True, exist_ok=True)
    for job in jobs:
        existing = read_context_lines(out_dir, job.entry.file)
        todo = {i for i, p in enumerate(job.passages) if not is_done(existing.get(p.passage_id), p, model_id)}
        report.skipped += len(job.passages) - len(todo)
        if not todo:
            continue
        report.files.append(job.entry.file)
        windows = job.windows()
        with open(context_path(out_dir, job.entry.file), "a", encoding="utf-8") as sink:
            for window in windows:
                for index in window.indices():
                    if index not in todo:
                        continue
                    passage = job.passages[index]
                    request = build_request(model_id, job.entry, window, job.passages, index)
                    try:
                        response = client.messages.create(**request)
                    except cap_errors as error:
                        report.stopped = f"cap: {error}"
                        return _finish(report, jobs, out_dir, model_id)
                    except Exception as error:
                        report.stopped = f"error: {type(error).__name__}: {error}"
                        return _finish(report, jobs, out_dir, model_id)
                    line = response_text(response)
                    verdict = check_context_line(line, allowed_text(job.entry, window, job.passages, index))
                    usage = _usage_dict(response)
                    record = {
                        "passage_id": passage.passage_id, "file": passage.file, "text_hash": text_hash(passage.text),
                        "model_id": model_id, "prompt_version": PROMPT_VERSION, "context": line,
                        "status": verdict.status, "reasons": list(verdict.reasons), "usage": usage, "live_test": live_test_name,
                    }
                    sink.write(json.dumps(record, ensure_ascii=False) + "\n")
                    sink.flush()
                    report.generated += 1
                    report.flagged += 0 if verdict.ok else 1
                    report.input_tokens += usage["input_tokens"]
                    report.output_tokens += usage["output_tokens"]
                    report.cache_write_tokens += usage["cache_creation_input_tokens"]
                    report.cache_read_tokens += usage["cache_read_input_tokens"]
    return _finish(report, jobs, out_dir, model_id)


def _finish(report: RunReport, jobs: Sequence[Job], out_dir: Path, model_id: str) -> RunReport:
    _, report.remaining = pending_count(jobs, out_dir, model_id)
    return report
