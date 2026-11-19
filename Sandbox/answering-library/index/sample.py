import json
import statistics
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

from . import contract
from .catalog import FileEntry
from .contract import Passage
from .estimate import PASSAGE_WORDS, FilePlan, plan_from_passages, plan_from_stats
from .tokens import TextStats, file_stats

DEFAULT_FILES = {
    "xml": "npnf104_augustine-anti-manichaean-anti-donatist.xml",
    "latin": "cyprian_de-lapsis-lat_hartel1868-csel3-tei.txt",
    "weak_ocr": "hefele-leclercq_histoire-des-conciles-tome1-1-cyprien-novatiens-baptheme-slice-fra_1907.txt",
}
PER_FILE_PASSAGES = 150
MAX_OVERSHOOT = 1.4
MIN_PASSAGES_FOR_PICK = 40


@dataclass
class SampleFile:
    role: str
    file: str
    passage_ids: list[str]


def _is_front_matter(passages: Sequence[Passage]) -> bool:
    return all(p.apparatus for p in passages)


def take_divisions(passages: Sequence[Passage], target: int) -> list[Passage]:
    divisions: list[list[Passage]] = []
    for p in passages:
        if divisions and divisions[-1][0].division_locus == p.division_locus:
            divisions[-1].append(p)
        else:
            divisions.append([p])
    taken: list[Passage] = []
    for division in divisions:
        if _is_front_matter(division):
            continue
        if taken and len(taken) + len(division) > target * MAX_OVERSHOOT:
            break
        taken.extend(division)
        if len(taken) >= target:
            break
    return taken


def _median_ocr(passages: Sequence[Passage]) -> float:
    scores = [p.ocr_score for p in passages if p.ocr_score is not None]
    return statistics.median(scores) if scores else 1.0


def _majority_language(passages: Sequence[Passage]) -> str:
    counts: dict[str, int] = {}
    for p in passages:
        counts[p.language] = counts.get(p.language, 0) + 1
    return max(counts, key=counts.get) if counts else ""


def select_sample(entries: Sequence[FileEntry], out_dir: Path, per_file: int = PER_FILE_PASSAGES) -> list[SampleFile]:
    segmented = {}
    for entry in entries:
        passages = contract.read_file_passages(out_dir, entry.file)
        if passages and len(passages) >= MIN_PASSAGES_FOR_PICK:
            segmented[entry.file] = passages
    if not segmented:
        raise LookupError("no segmenter output for the shelf's files; the sample cannot be selected yet")
    plain = {f: ps for f, ps in segmented.items() if not f.endswith(".xml")}
    picks: dict[str, str] = {}
    xml = sorted(f for f in segmented if f.endswith(".xml"))
    if xml:
        picks["xml"] = DEFAULT_FILES["xml"] if DEFAULT_FILES["xml"] in segmented else xml[0]
    if plain:
        picks["weak_ocr"] = min(sorted(plain), key=lambda f: _median_ocr(plain[f]))
        latin = sorted(f for f, ps in plain.items() if _majority_language(ps) == "lat" and f != picks["weak_ocr"])
        if latin:
            picks["latin"] = DEFAULT_FILES["latin"] if DEFAULT_FILES["latin"] in latin else latin[0]
    sample = []
    for role, file_name in picks.items():
        chosen = take_divisions(segmented[file_name], per_file)
        sample.append(SampleFile(role, file_name, [p.passage_id for p in chosen]))
    return sample


def write_selection(path: Path, world: str, sample: Sequence[SampleFile]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps({
        "world": world, "files": [{"role": s.role, "file": s.file, "passage_ids": s.passage_ids} for s in sample],
    }, indent=1), encoding="utf-8")


def read_selection(path: Path) -> tuple[str, list[SampleFile]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    return data["world"], [SampleFile(f["role"], f["file"], f["passage_ids"]) for f in data["files"]]


def selection_passages(out_dir: Path, sample: Sequence[SampleFile]) -> dict[str, list[Passage]]:
    result = {}
    for item in sample:
        wanted = set(item.passage_ids)
        passages = contract.read_file_passages(out_dir, item.file) or []
        result[item.file] = [p for p in passages if p.passage_id in wanted]
    return result


def plan_selection(entries: dict[str, FileEntry], out_dir: Path, sample: Sequence[SampleFile]) -> list[FilePlan]:
    passages = selection_passages(out_dir, sample)
    return [plan_from_passages(entries[name], ps) for name, ps in passages.items()]


def modeled_plans(entries: dict[str, FileEntry], out_dir: Path, per_file: int = PER_FILE_PASSAGES) -> list[FilePlan]:
    plans = []
    for file_name in DEFAULT_FILES.values():
        entry = entries[file_name]
        stats = file_stats(entry.path, out_dir / "filestats.json")
        target_words = per_file * PASSAGE_WORDS
        scale = min(1.0, target_words / max(stats.words, 1))
        scaled = TextStats(
            chars=int(stats.chars * scale), words=int(stats.words * scale),
            greek_chars=int(stats.greek_chars * scale), other_chars=int(stats.other_chars * scale),
        )
        plan = plan_from_stats(entry, scaled)
        plan.notes.append(f"modeled slice of {per_file} passages")
        plans.append(plan)
    return plans
