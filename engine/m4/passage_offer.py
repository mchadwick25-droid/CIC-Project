"""The passage offer: leaf passages from the built passage index, offered beside
a sub-question's records.

A built offer file (made by engine.m4.reports.passage_offer_build from Library's reviewed
seed and the passage index) holds, per sub-question, the passages that answer it, each with
its source, role, date and a voiceable-or-etic flag. This module reads that file, takes the
sub-question's passages within a budget, and turns each into a record-shaped entry so the
bound draft and the one batched read treat it like any other record.

Evidence rules. Only a leaf passage is offered: never a summary or the frame. A
sentence bound only to passages is a quotation or close paraphrase in the author's
name ("[author], in [work], writes"), never "we", unless a reviewed record bound to
the same sentence frames it as the world's position. A passage whose speaker is not
the world's own voice is offered etic, outside the voice.

With search on (a world frame's `passage_search`, a SearchRequest per turn), the passages
come from search_passages instead: any passage on the world's shelf inside its lens, found
by the visitor's own words, with the sub-question's reviewed seeds as rank help only. One
diversity rule (diversify) then covers the records and the passages together, and the
budget is applied last. With search off, the offer is the seed file's alone.

Shadow only: no registered frame sets `passage_offer` or `passage_search`. No model call.
"""
import json
import math
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable, Mapping, Sequence

from engine.m4 import subquestion_routing
from engine.m4.reports.passage_offer_build import _date_text, _name, _set, tag_for

PASSAGE_TYPE = "passage"
DEFAULT_MAX_PASSAGES = 6
DEFAULT_MAX_WORDS = 1800
AUTHOR_CAP = 3
WORK_CAP = 2


@dataclass(frozen=True)
class Budget:
    max_passages: int = DEFAULT_MAX_PASSAGES
    max_words: int = DEFAULT_MAX_WORDS


def load_offer(path: Path) -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def author_work(passage: dict) -> str | None:
    """How the voice names the passage's source: author and work, or whichever is named; None when neither is."""
    author, work = passage.get("author_name"), passage.get("work")
    if author and work:
        return f"{author}, in {work}"
    return work or author


def record_for(passage: dict) -> dict:
    """The passage as a record the pipeline can bind a sentence to."""
    return {
        "id": passage["tag"],
        "passage_id": passage["passage_id"],
        "record_type": PASSAGE_TYPE,
        "text": passage["text"],
        "source_label": author_work(passage),
        "voiceable": bool(passage["voiceable"]),
        "fit": passage.get("fit"),
        "role": passage.get("role"),
        "date": passage.get("date"),
        "locus": passage.get("locus"),
        "file": passage.get("file"),
        "byte_start": passage.get("byte_start"),
        "byte_end": passage.get("byte_end"),
    }


def ranked(passages: list[dict]) -> list[dict]:
    """The seed's reviewed rank (direct before partial, voiceable before etic); the seed's own order where a passage has none."""
    order = {p["tag"]: n for n, p in enumerate(passages)}
    return sorted(passages, key=lambda p: (p.get("rank") if p.get("rank") is not None else len(order), order[p["tag"]]))


def seeds_for(offer: dict | None, sub_question: str | None) -> list[dict]:
    """The sub-question's reviewed seed passages in an offer file, in their reviewed rank order."""
    subquestions = (offer or {}).get("subquestions") or {}
    held = {k for k, v in subquestions.items() if v}
    return ranked(subquestions.get(subquestion_routing.resolve(sub_question, held) or "") or [])


def select(offer: dict, sub_question: str | None, budget: Budget) -> list[dict]:
    """The sub-question's passages that fit the budget, in rank order. A passage with no named author or work is never offered."""
    chosen: list[dict] = []
    words = 0
    for passage in seeds_for(offer, sub_question):
        if len(chosen) >= budget.max_passages:
            break
        if not author_work(passage) or words + passage["word_count"] > budget.max_words:
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


def interleave(records: list[dict], passages: list[dict]) -> list[dict]:
    """The records and the passages in one list, each in its own rank order, taken in turn: the records' first, the passages' first, and so on."""
    seen = {r["id"] for r in records}
    passages = [p for p in passages if p["id"] not in seen]
    merged: list[dict] = []
    for n in range(max(len(records), len(passages))):
        merged += records[n:n + 1] + passages[n:n + 1]
    return merged


@dataclass(frozen=True)
class SearchRequest:
    """One turn's search: the world's shelf, the visitor's own words, the sub-question's reviewed seeds and the budget."""
    shelf: object
    query: str
    seeds: Sequence[dict] = field(default_factory=tuple)
    budget: Budget = Budget()
    sub_question: str | None = None


def offer_contents(records: list[dict], passages: list[dict], search: SearchRequest | None = None,
                   repository_records: Mapping[str, dict] | None = None) -> list[dict]:
    """What the offer holds: the records and the passages interleaved by rank. This is the one place that decides the offer's contents.

    With search off, the passages are the ones given. With search on, the given passages are not used: the passages are
    search_passages' over the world's lens, and the records already in the offer count toward its diversity caps."""
    if search is None:
        return interleave(records, passages)
    held = [k for r in records if (k := record_keys(r["id"], repository_records or {}, search.shelf))]
    found = search_passages(search.shelf, search.query, search.seeds, search.budget, held=held)
    return interleave(records, candidates(found, search.sub_question))


def search_passages(world, query: str, seeds: Sequence[dict], budget: Budget, *,
                    held: Iterable[tuple] = ()) -> list[dict]:
    """The passages the offer holds for a query: ranked inside the world's lens, each a passage of the offer's shape, cut by
    the diversity rule and then by the budget.

    `world` is the world's shelf (Sandbox/answering-library/search/shelf.py): in_lens, internal_id, ranked, passage, row.
    A passage is taken only when the shelf says it is in the lens. A seed is rank help: it reaches the ranking only when
    it resolves to a lens passage with the same byte span, and it gives that passage its reviewed flags. A passage with
    no seed is outside the voice. A passage with no named author or work is never offered. `held` is the author and
    work keys of the records already in the offer."""
    by_internal: dict[int, dict] = {}
    for seed in ranked(list(seeds)):
        pid = world.internal_id(seed["passage_id"], seed.get("byte_start"), seed.get("byte_end"))
        if pid is not None and world.in_lens(pid):
            by_internal.setdefault(pid, seed)
    found: list[dict] = []
    seen: set[str] = set()
    for pid in world.ranked(query, list(by_internal)):
        if not world.in_lens(pid):
            continue
        passage = _offered(world.world, world.passage(pid), by_internal.get(pid))
        if passage["passage_id"] in seen or not author_work(passage):
            continue
        seen.add(passage["passage_id"])
        found.append(passage)
    return within_budget(diversify(found, budget, held), budget)


def _row_keys(row: dict | None) -> tuple:
    """The author key and work key of a corpus-map row: its author, and its author with its work title."""
    if not row:
        return (None, None)
    author = (_set(row.get("author")) or "").casefold() or None
    work = (_set(row.get("work")) or "").casefold() or None
    return (author, (author, work) if work else None)


def _offered(world: str, indexed: dict, seed: dict | None) -> dict:
    """A shelf passage in the offer's shape. Author, work, role and date come from the corpus-map row it is bound to; a
    reviewed seed's own values come first where it sets them, and only a seed can make a passage voiceable."""
    row = indexed.get("row") or {}
    author_key, work_key = _row_keys(row)
    passage = {
        "tag": tag_for(world, indexed["passage_id"]), "passage_id": indexed["passage_id"], "file": indexed["file"],
        "text": indexed["text"], "word_count": indexed["word_count"],
        "locus": " ".join(x for x in (indexed.get("division_locus"), indexed.get("division_title")) if x) or None,
        "speaker_state": indexed.get("speaker_state"), "ocr_score": indexed.get("ocr_score"),
        "role": row.get("role"), "work": _set(row.get("work")), "author_name": _name(_set(row.get("author"))),
        "date": _date_text(row.get("date")), "window": None, "fit": None, "rank": None, "voiceable": False,
        "byte_start": indexed["byte_start"], "byte_end": indexed["byte_end"],
        "author_key": author_key, "work_key": work_key,
    }
    if seed is not None:
        passage.update({k: seed[k] for k in ("work", "author_name", "date", "role") if seed.get(k)})
        passage.update({"window": seed.get("window"), "fit": seed.get("fit"), "rank": seed.get("rank"),
                        "voiceable": bool(seed.get("voiceable"))})
    return passage


def record_keys(record_id: str, repository_records: Mapping[str, dict], shelf) -> tuple | None:
    """The author key and work key of a record in the offer, read from the corpus-map row its source names (a source
    record's own `shelf_row`, or the first source's); None when no row is named or the world has no such row."""
    record = repository_records.get(record_id) or {}
    source = record if record.get("record_type") == "source" else None
    if source is None:
        first = next((s.get("source_id") for s in record.get("sources") or [] if s.get("source_id")), None)
        source = repository_records.get(first) if first else None
    row = shelf.row((source or {}).get("shelf_row"))
    keys = _row_keys(row)
    return keys if any(keys) else None


def _cap(base: int, distinct: int, slots: int) -> int:
    """The cap per author or per work: `base`, relaxed so that `distinct` sources can still fill `slots` when they are
    fewer than `slots` needs at the base cap."""
    if distinct >= math.ceil(slots / base):
        return base
    return math.ceil(slots / max(distinct, 1))


def diversify(passages: list[dict], budget: Budget, held: Iterable[tuple] = ()) -> list[dict]:
    """The passages in rank order, cut so that, with the records already in the offer (`held`), no more than AUTHOR_CAP
    come from one author and no more than WORK_CAP from one work. A cap relaxes when the passages hold fewer distinct
    authors (or works) than the budget's passages need at that cap. A passage whose author or work is not known is not
    counted against that cap."""
    authors = [p.get("author_key") for p in passages]
    works = [p.get("work_key") for p in passages]
    author_cap = _cap(AUTHOR_CAP, len({a for a in authors if a}), budget.max_passages)
    work_cap = _cap(WORK_CAP, len({w for w in works if w}), budget.max_passages)
    by_author: Counter = Counter()
    by_work: Counter = Counter()
    for author, work in held:
        if author:
            by_author[author] += 1
        if work:
            by_work[work] += 1
    kept: list[dict] = []
    for passage, author, work in zip(passages, authors, works):
        if (author and by_author[author] >= author_cap) or (work and by_work[work] >= work_cap):
            continue
        kept.append(passage)
        if author:
            by_author[author] += 1
        if work:
            by_work[work] += 1
    return kept


def within_budget(passages: list[dict], budget: Budget) -> list[dict]:
    """The passages in rank order up to the budget's passage count and words; a passage that would pass the words is skipped."""
    chosen: list[dict] = []
    words = 0
    for passage in passages:
        if len(chosen) >= budget.max_passages:
            break
        if words + passage["word_count"] > budget.max_words:
            continue
        chosen.append(passage)
        words += passage["word_count"]
    return chosen


def offered_records(candidates: Iterable[dict]) -> dict[str, dict]:
    """The offered passages of an evidence list, as records a sentence can bind to."""
    return {c["id"]: c["passage"] for c in candidates if c.get("record_type") == PASSAGE_TYPE and c.get("passage")}


def records_by_id(passages: list[dict]) -> dict[str, dict]:
    return {p["tag"]: record_for(p) for p in passages}


def render_line(candidate: dict) -> str:
    """One offer line: the label the voice must use, whether the passage is ours to voice, and its words."""
    rec = candidate["passage"]
    where = f", {rec['locus']}" if rec.get("locus") else ""
    when = f", {rec['date']}" if rec.get("date") else ""
    part = "; it answers only part of the question" if rec.get("fit") == "partial" else ""
    if rec["voiceable"]:
        how = f"VOICEABLE; say \"{rec['source_label']}, writes\"; \"we\" only with a reviewed record bound to the same sentence"
    else:
        how = f"OUTSIDE OUR VOICE; say \"{rec['source_label']}, writes\"; never \"we\""
    return f"- [[{candidate['id']}]] passage ({how}{where}{when}{part}) — {candidate['head']}"


def all_records(offer: dict) -> dict[str, dict]:
    """Every passage of an offer file as a record, for the steps that run after a turn over a finished run."""
    return {p["tag"]: record_for(p) for passages in (offer.get("subquestions") or {}).values() for p in passages}
