"""The passage offer: leaf passages from the built passage index, offered beside
a sub-question's records.

A built offer file (made by engine.m4.reports.passage_offer_build from a seed, the
passage index and the vendored texts) holds, per sub-question, the passages that
answer it, each with its speaker, row, role, date and a voiceable-or-etic flag. This
module reads that file, takes the sub-question's passages within a budget, and turns
each into a record-shaped entry so the bound draft, the one batched read and the
three-level transparency treat it like any other record.

Evidence rules. Only a leaf passage is offered: never a summary or the frame. A
sentence bound only to passages is a quotation or close paraphrase in the author's
name ("[author], in [work], writes"), never "we", unless a reviewed record bound to
the same sentence frames it as the world's position. A passage whose speaker is not
the world's own voice is offered etic, outside the voice.

Shadow only: no registered frame sets `passage_offer`. No model call.
"""
import json
from dataclasses import dataclass
from pathlib import Path

from engine.m4 import subquestion_routing

PASSAGE_TYPE = "passage"
DEFAULT_MAX_PASSAGES = 6
DEFAULT_MAX_WORDS = 1800


@dataclass(frozen=True)
class Budget:
    max_passages: int = DEFAULT_MAX_PASSAGES
    max_words: int = DEFAULT_MAX_WORDS


def load_offer(path: Path) -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def author_work(passage: dict) -> str:
    """How the voice names the passage's source: author and work, or the work alone when no author is ruled."""
    author, work = passage.get("author_name"), passage.get("work")
    if author and work:
        return f"{author}, in {work}"
    return work or author or "a writing we hold"


def record_for(passage: dict) -> dict:
    """The passage as a record the pipeline can bind a sentence to."""
    return {
        "id": passage["tag"],
        "passage_id": passage["passage_id"],
        "record_type": PASSAGE_TYPE,
        "text": passage["text"],
        "source_label": author_work(passage),
        "voiceable": bool(passage["voiceable"]),
        "speaker": passage.get("speaker"),
        "row": passage.get("row_id"),
        "role": passage.get("role"),
        "date": passage.get("date"),
        "locus": passage.get("locus"),
        "file": passage.get("file"),
        "byte_start": passage.get("byte_start"),
        "byte_end": passage.get("byte_end"),
    }


def ranked(passages: list[dict]) -> list[dict]:
    """Voiceable first, then the cleaner scan, then the seed's own order."""
    order = {p["tag"]: n for n, p in enumerate(passages)}
    return sorted(passages, key=lambda p: (not p["voiceable"], -(p.get("ocr_score") or 0.0), order[p["tag"]]))


def select(offer: dict, sub_question: str | None, budget: Budget) -> list[dict]:
    """The sub-question's passages that fit the budget, in offer order."""
    chosen: list[dict] = []
    words = 0
    held = {k for k, v in (offer.get("subquestions") or {}).items() if v}
    for passage in ranked((offer.get("subquestions") or {}).get(subquestion_routing.resolve(sub_question, held) or "") or []):
        if len(chosen) >= budget.max_passages:
            break
        if chosen and words + passage["word_count"] > budget.max_words:
            continue
        chosen.append(passage)
        words += passage["word_count"]
    return chosen


def candidates(passages: list[dict], sub_question: str) -> list[dict]:
    """Evidence-shaped candidates for the offered passages."""
    return [
        {
            "id": p["tag"], "record_type": PASSAGE_TYPE, "head": p["text"], "confidence": None, "classification": None,
            "cell": sub_question, "score": None, "passage": record_for(p),
        }
        for p in passages
    ]


def records_by_id(passages: list[dict]) -> dict[str, dict]:
    return {p["tag"]: record_for(p) for p in passages}


def render_line(candidate: dict) -> str:
    """One offer line: the label the voice must use, whether the passage is ours to voice, and its words."""
    rec = candidate["passage"]
    where = f", {rec['locus']}" if rec.get("locus") else ""
    when = f", {rec['date']}" if rec.get("date") else ""
    if rec["voiceable"]:
        how = f"VOICEABLE; say \"{rec['source_label']}, writes\"; \"we\" only with a reviewed record bound to the same sentence"
    else:
        how = f"OUTSIDE OUR VOICE; say \"{rec['source_label']}, writes\"; never \"we\""
    return f"- [[{candidate['id']}]] passage ({how}{where}{when}) — {candidate['head']}"
