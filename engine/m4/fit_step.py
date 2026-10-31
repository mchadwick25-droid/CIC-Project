"""The fit step: a quote or story placed in an answer must answer the question
asked, in its own source context, and not only share its words.

Two parts, both shadow only. The judge is called by no live path. Context
blocks are attached to the evidence only when a frame sets `context_blocks`,
which no registered frame does.

Context blocks. For a quote or story record, the source text around the places
its `sources[].locus` cites (a `cic/texts/<file>, line N` locus), so the voice
can see what the passage was saying. A block is marked as context, and the cited
lines are always inside it, whole. Its id (`ctx.<record id>.<n>`) is not a record
id, so a sentence tagged to one is treated by the net as tagged to an unknown
record.

The fit read. In the answer check (engine.m4.answer_check) it is part of the one read
of the answer: `fit_pack` gives the judge the record's own statement of what it means
and must not be used for, the passage and its context, and `judgement_from` reads one
verdict. On its own, `fit_request` and `parse_fit` serve the calibration of the fit
judge on planted pairs (Sandbox/Answering-From-Sources/goldset/fit.py). `decide` turns a
verdict into keep or drop: fits is kept, off-point is dropped, partly is kept only when
the answer's own words already state what the passage does not cover. An unreadable
verdict keeps the placement.
"""
import json
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
CONTEXT_PREFIX = "ctx."
CONTEXT_RADIUS_LINES = 30
CONTEXT_MAX_WORDS = 450
VERDICTS = ("fits", "partly", "off_point")

FIT_RUBRIC = (
    "Decide whether the passage, read in its own context, answers THIS question. Sharing words or a topic with the question is not enough.\n"
    "fits: it answers the question that was asked.\n"
    "partly: it bears on the question but answers a nearby one, or only part of it.\n"
    "off_point: it shares words or a topic with the question but answers a different one, or the record forbids this use.\n"
    "limit_stated is true only when the answer's own sentences already say what the passage does not cover. Use only what is given.\n"
)

FIT_SYSTEM = (
    "You judge whether a quote or a story from a source record answers a visitor's question. "
    "You are given the question, the record's own statement of what it means and what it must not be used for, "
    "the passage as the record gives it, and the text around the passage in its source.\n"
    + FIT_RUBRIC
    + 'Reply with one JSON object only: {"fit": "fits" or "partly" or "off_point", "reason": "one short sentence", "limit_stated": true or false}.'
)

_LOCUS = re.compile(r"(cic/texts/[\w./-]+?),?\s*lines?\s*(\d+)(?:\s*[-–]\s*(\d+))?")
_MARKUP = re.compile(r"<[^>]+>")


def _words(lines: list[str], number: int) -> list[str]:
    return _MARKUP.sub(" ", lines[number - 1]).split()


def _window(path: Path, first: int, last: int) -> str:
    """The cited lines in full, then lines either side of them, alternating, until
    the radius or the word ceiling is reached. The ceiling limits only the text
    added around the cited lines, never the cited lines themselves."""
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    if first > len(lines):
        return ""
    last = min(last, len(lines))
    cited = [w for n in range(first, last + 1) for w in _words(lines, n)]
    before: list[str] = []
    after: list[str] = []
    budget = max(CONTEXT_MAX_WORDS - len(cited), 0)
    lower, upper = first - 1, last + 1
    floor, ceiling = max(first - CONTEXT_RADIUS_LINES, 1), min(last + CONTEXT_RADIUS_LINES, len(lines))
    while budget > 0 and (lower >= floor or upper <= ceiling):
        if lower >= floor:
            take = _words(lines, lower)[-budget:]
            before, budget, lower = take + before, budget - len(take), lower - 1
        if budget > 0 and upper <= ceiling:
            take = _words(lines, upper)[:budget]
            after, budget, upper = after + take, budget - len(take), upper + 1
    return " ".join(before + cited + after)


def context_blocks(record: dict, texts_root: Path = REPO_ROOT) -> list[dict]:
    """One block per cited locus of the record that names a text file under
    cic/texts and a line: its id, the source it came from and the text around it."""
    blocks = []
    base = (texts_root / "cic" / "texts").resolve()
    for source in record.get("sources") or []:
        for file, first, last in _LOCUS.findall(source.get("locus") or ""):
            path = (texts_root / file).resolve()
            if base not in path.parents or not path.is_file():
                continue
            text = _window(path, int(first), int(last or first))
            if text:
                blocks.append({
                    "id": f"{CONTEXT_PREFIX}{record['id']}.{len(blocks) + 1}", "record_id": record["id"],
                    "source_id": source.get("source_id"), "file": file, "lines": f"{first}-{last or first}", "text": text,
                })
    return blocks


def with_context(turn_evidence: dict, repository_records: dict[str, dict], texts_root: Path = REPO_ROOT) -> dict:
    """The evidence with each quote or story candidate carrying its context blocks."""
    candidates = [
        {**c, "context": context_blocks(repository_records[c["id"]], texts_root)}
        if c.get("record_type") in ("quote", "story") and c["id"] in repository_records else c
        for c in turn_evidence["candidates"]
    ]
    return {**turn_evidence, "candidates": candidates}


def context_lines(candidate: dict) -> list[str]:
    """The evidence block's rider for a candidate's context: marked as context,
    never evidence."""
    return [
        f"  CONTEXT {block['id']} (read to understand what this was saying; it supports no sentence, so never tag a sentence to it "
        f"and never quote it): {block['text']}"
        for block in candidate.get("context") or []
    ]


def context_tags(tags: list[str]) -> list[str]:
    return [t for t in tags if t.startswith(CONTEXT_PREFIX)]


def passage(record: dict, length: str | None = None) -> str:
    """The words the visitor would get from the record: a quote's spoken
    rendering, a story's telling at the length told (full when none is named)."""
    if record.get("record_type") == "quote":
        return (record.get("modern_rendering") or record.get("text") or "").strip()
    field = {"short": "telling_short", "medium": "telling_medium"}.get(length or "", "telling")
    return (record.get(field) or record.get("telling") or "").strip()


def fit_pack(record: dict, blocks: list[dict], length: str | None = None) -> str:
    """What the judge reads of one placed passage: the record's own statement of what it
    means and must not be used for, the passage as the visitor gets it, and its source context."""
    use = record.get("use_note") or {}
    not_for = "; ".join(use.get("not_for") or []) or "(none stated)"
    context = "\n\n".join(f"[{b['id']}] {b['text']}" for b in blocks) or "(no context text available)"
    return (
        f"Record: {record['id']} ({record.get('record_type')})\n"
        f"What it means: {use.get('means') or record.get('tellable_as') or '(not stated)'}\n"
        f"Must not be used for: {not_for}\n"
        f"The passage:\n{passage(record, length)}\n"
        f"Context from the source text:\n{context}"
    )


def fit_request(question: str, record: dict, blocks: list[dict], length: str | None = None, answer_text: str = "") -> dict:
    """The system prompt and the user message for the fit judge on its own."""
    return {"system": FIT_SYSTEM, "user": f"Question:\n{question}\n\n{fit_pack(record, blocks, length)}\n\nThe answer text around the passage (may be empty):\n{answer_text or '(none)'}"}


def _first_object(text: str) -> dict | None:
    decoder = json.JSONDecoder()
    for opening in re.finditer(r"\{", text or ""):
        try:
            found, _end = decoder.raw_decode(text[opening.start():])
        except json.JSONDecodeError:
            continue
        return found if isinstance(found, dict) else None
    return None


def parse_fit(reply: str) -> dict | None:
    """The verdict in a reply, or None when there is none."""
    return judgement_from(_first_object(reply))


def judgement_from(data: dict) -> dict | None:
    """A fit judgement from one reply entry, or None when it carries no verdict. `limit_stated`
    is needed only for `partly`; for the other verdicts it is false when absent."""
    if not isinstance(data, dict) or data.get("fit") not in VERDICTS:
        return None
    limit = data.get("limit_stated", False if data["fit"] != "partly" else None)
    if not isinstance(limit, bool):
        return None
    return {"fit": data["fit"], "reason": str(data.get("reason") or ""), "limit_stated": limit}


def decide(judgement: dict | None) -> str:
    """keep or drop. An unreadable verdict keeps the placement and is counted
    elsewhere: the fit step never removes a reviewed record on a reply it could
    not read."""
    if judgement is None or judgement["fit"] == "fits":
        return "keep"
    if judgement["fit"] == "partly":
        return "keep" if judgement["limit_stated"] else "drop"
    return "drop"
