"""The fit step: a quote or story placed in an answer must answer the question
asked, in its own source context, and not only share its words.

Two parts, both shadow only. Nothing in the live turn calls either.

Context blocks. For a quote or story record, the source text around the places
its `sources[].locus` cites, so the voice can see what the passage was saying.
A block is marked as context. Its id (`ctx.<record id>.<n>`) cannot be a
binding: a sentence tagged to one is withheld (grounding_net), so the voice may
learn from context and cannot assert from it. The pre-Stage-2 provider reads a
window of lines around each `cic/texts/<file>, line N` locus; when Stage 2 gives
every passage its division, the window becomes the division and nothing else here
changes.

The fit judge. `fit_request` builds the question, the record's own statement of
what it means and must not be used for, the passage and its context;
`parse_fit` reads the reply; `decide` turns a verdict into keep or drop:
fits is kept, off-point is dropped, partly is kept only when the answer's own
words already state what the passage does not cover.
"""
import json
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
CONTEXT_PREFIX = "ctx."
CONTEXT_RADIUS_LINES = 30
CONTEXT_MAX_WORDS = 450
VERDICTS = ("fits", "partly", "off_point")

FIT_SYSTEM = (
    "You judge whether a quote or a story from a source record answers a visitor's question. "
    "You are given the question, the record's own statement of what it means and what it must not be used for, "
    "the passage as the record gives it, and the text around the passage in its source.\n"
    "Decide whether this passage, read in its own context, answers THIS question. Sharing words or a topic with the question is not enough.\n"
    "fits: it answers the question that was asked.\n"
    "partly: it bears on the question but answers a nearby one, or only part of it.\n"
    "off_point: it shares words or a topic with the question but answers a different one, or the record forbids this use.\n"
    "Use only what is given. Reply with one JSON object only: "
    '{"fit": "fits" or "partly" or "off_point", "reason": "one short sentence", "limit_stated": true or false}. '
    "limit_stated is true only when the answer text you were given already says what the passage does not cover."
)

_LOCUS = re.compile(r"(cic/texts/[\w./-]+?),?\s*lines?\s*(\d+)(?:\s*[-–]\s*(\d+))?")
_MARKUP = re.compile(r"<[^>]+>")
_JSON = re.compile(r"\{.*\}", re.DOTALL)


def _window(path: Path, first: int, last: int) -> str:
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    low, high = max(first - CONTEXT_RADIUS_LINES, 1), min(last + CONTEXT_RADIUS_LINES, len(lines))
    text = " ".join(_MARKUP.sub(" ", line).strip() for line in lines[low - 1 : high])
    words = text.split()
    return " ".join(words[:CONTEXT_MAX_WORDS])


def context_blocks(record: dict, texts_root: Path = REPO_ROOT) -> list[dict]:
    """One block per cited locus of the record that names a text file and a
    line: its id, the source it came from and the text around it."""
    blocks = []
    for source in record.get("sources") or []:
        for file, first, last in _LOCUS.findall(source.get("locus") or ""):
            path = texts_root / file
            if not path.is_file():
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


def fit_request(question: str, record: dict, blocks: list[dict], length: str | None = None, answer_text: str = "") -> dict:
    """The system prompt and the user message for the fit judge."""
    use = record.get("use_note") or {}
    not_for = "; ".join(use.get("not_for") or []) or "(none stated)"
    context = "\n\n".join(f"[{b['id']}] {b['text']}" for b in blocks) or "(no context text available)"
    user = (
        f"Question:\n{question}\n\n"
        f"Record: {record['id']} ({record.get('record_type')})\n"
        f"What it means: {use.get('means') or record.get('tellable_as') or '(not stated)'}\n"
        f"Must not be used for: {not_for}\n\n"
        f"The passage:\n{passage(record, length)}\n\n"
        f"Context from the source text:\n{context}\n\n"
        f"The answer text around the passage (may be empty):\n{answer_text or '(none)'}"
    )
    return {"system": FIT_SYSTEM, "user": user}


def parse_fit(reply: str) -> dict | None:
    found = _JSON.search(reply or "")
    if not found:
        return None
    try:
        data = json.loads(found.group(0))
    except json.JSONDecodeError:
        return None
    if data.get("fit") not in VERDICTS or not isinstance(data.get("limit_stated"), bool):
        return None
    return {"fit": data["fit"], "reason": str(data.get("reason") or ""), "limit_stated": data["limit_stated"]}


def decide(judgement: dict | None) -> str:
    """keep or drop. An unreadable verdict keeps the placement and is counted
    elsewhere: the fit step never removes a reviewed record on a reply it could
    not read."""
    if judgement is None or judgement["fit"] == "fits":
        return "keep"
    if judgement["fit"] == "partly":
        return "keep" if judgement["limit_stated"] else "drop"
    return "drop"
