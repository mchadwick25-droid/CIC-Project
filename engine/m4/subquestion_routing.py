"""Routing by sub-question: the reader names the sub-question a visitor's
question belongs to, and the offer takes that sub-question's records first.

The catalogue is the fleet's sub-question list (an id and a plain label each).
The reader sees it and names one id or none (`reader_catalogue`,
`parse_sub_question`). The sidecar lists, per sub-question, the records of one
world that answer it; `coverage_entries` turns those lists into the same shape
as the package's compiled coverage, so the offer selects from them with the
selection it already uses (engine.m4.evidence.select_cell_candidates).

A sub-question the sidecar holds no record for leaves the offer as it was; a split sub-question with no
record of its own (C5.S1a) takes its parent's (C5.S1).
Shadow only: no registered frame sets `subquestion_routing`.
"""
import re
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]
SUB_QUESTION_ID = re.compile(r"C\d+\.S\d+[a-z]?")
COVERAGE_KEY_BY_RECORD_TYPE = {
    "doctrinal_witness": "doctrinal_witness",
    "term": "terms",
    "story": "stories",
    "quote": "quotes",
    "gravity": "gravities",
    "force": "forces",
    "contested_claim": "contested_claims",
    "figure": "figures",
    "honest_limit": "honest_limit",
}


def parent_of(sub_question: str) -> str | None:
    """The id a split sub-question (C5.S1a) was split from (C5.S1), or None for an id that is not a split."""
    return sub_question[:-1] if sub_question and sub_question[-1:].isalpha() else None


def resolve(sub_question: str | None, held) -> str | None:
    """The id to take records or passages under: the sub-question itself when `held` has it, else the id it was
    split from, else None. A split with nothing of its own keeps the parent's offer, so nothing already working is lost."""
    if not sub_question:
        return None
    if sub_question in held:
        return sub_question
    parent = parent_of(sub_question)
    return parent if parent and parent in held else None


def load_sidecar(path: Path) -> dict:
    return yaml.safe_load(Path(path).read_text(encoding="utf-8"))


def reader_catalogue(sidecar: dict) -> str:
    """The list the reader is shown: one line per sub-question, id then label."""
    return "\n".join(f"{sid} {entry['label']}" for sid, entry in sidecar["subquestions"].items())


def parse_sub_question(reader_value: dict | None, sidecar: dict) -> str | None:
    """The sub-question id the reader named, or None when it named none or an id the catalogue does not hold."""
    named = (reader_value or {}).get("sub_question")
    if isinstance(named, str) and SUB_QUESTION_ID.fullmatch(named.strip()) and named.strip() in sidecar["subquestions"]:
        return named.strip()
    return None


def coverage_entries(sidecar: dict, repository_records: dict[str, dict]) -> dict[str, dict]:
    """Coverage-shaped entries by sub-question id, for the sub-questions that have records here."""
    entries: dict[str, dict] = {}
    for sid, entry in sidecar["subquestions"].items():
        shaped: dict[str, list[str]] = {}
        for rid in entry.get("records") or []:
            key = COVERAGE_KEY_BY_RECORD_TYPE.get((repository_records.get(rid) or {}).get("record_type"))
            if key:
                shaped.setdefault(key, []).append(rid)
        if shaped:
            entries[sid] = shaped
    return entries
