"""The unbound-sentence step: a sentence the voice ships with no valid binding is
either a connective, a statement about the conversation, or a denial checked
against the shelf, and anything else about the world is withheld.

Shadow only. No live path calls it, and it makes no model call: it builds the
judges' requests, reads the replies, and decides.

Why. engine.m4.verify_step reads only sentences bound to a record. A sentence
with no valid binding (no tag, a context-block id, an unknown id, or a verdict
the net withheld) ships as plain text, and the net's own exemption for honesty
scaffolding lets a sentence that says what the world's sources lack ship with no
check at all. That is where an invented absence ("nothing we carry speaks of
him") gets through, whatever its phrasing.

Rule. A sentence the net withheld is taken out. Every other sentence the voice
wrote is classified by a reader that sees only the question and the sentence
(a bound sentence is judged against its records by the verify step, but a denial
in it is checked here too, because a record can state a denial the shelf
contradicts):

  connective   joins, frames or moves on, and claims nothing about history,
               people, texts or what the sources hold: kept
  conversation is about this conversation itself: kept
  world_claim  states any fact about people, events, teaching, texts or the
               tradition: withheld when unbound, left to the verify step when bound
  limit        says the records or sources lack, do not say, never describe or
               cannot give something: the thing it denies is named, the shelf
               (the files in the world's bucket of the corpus map) is searched
               for it, and a second reader says whether the passages found state
               it; if they do the sentence is withheld, if not it is kept.

The shelf search is lexical: the denied phrase, the sentence and the question
give weighted terms, and the highest-scoring windows of lines across the shelf
files are shown to the second reader with their file and line numbers.
"""
from __future__ import annotations

import json
import math
import re
from collections import defaultdict
from pathlib import Path

from engine.m4 import absence_rule
from engine.m4.grounding_net import placed_by_code
from engine.m4.verify_step import valid_bindings

KINDS = ("connective", "conversation", "world_claim", "limit")
WINDOW_LINES = 12
PASSAGE_CONTEXT = 3
PASSAGE_CHARS = 1400
TOP_WINDOWS = 4
MIN_DISTINCT_TERMS = 3
DENIED_WEIGHT = 2.0
_JSON = re.compile(r"\{.*\}", re.DOTALL)
_MARKUP = re.compile(r"<[^>]+>")
_WORD = re.compile(r"[A-Za-z][A-Za-z'’-]*")

CLASSIFY_SYSTEM = (
    "You read one sentence a historical Representative said to a visitor, with the visitor's question. The sentence "
    "carries no citation. Decide which kind it is.\n"
    "connective: it only joins, frames or moves on, and claims nothing about history, people, texts, teaching or what the "
    "sources hold (for example \"Here is what we can say.\", \"That is the plain answer.\").\n"
    "conversation: it is about this conversation itself (what was asked, what comes next, an offer to go on).\n"
    "world_claim: it states any fact about people, events, teaching, texts or the tradition.\n"
    "limit: it says that the records or sources lack, do not say, never describe or cannot give something, or that something "
    "is not known. For a limit, \"denies\" is a short phrase of 3 to 8 plain words naming the thing said to be missing, "
    "without \"our record\" or \"we\" (for example \"how the Maximinus conference ended\"). For any other kind \"denies\" is null.\n"
    'Reply with one JSON object only: {"kind": "connective" or "conversation" or "world_claim" or "limit", "denies": string or null}'
)
SHELF_SYSTEM = (
    "A historical Representative said a sentence that denies that its sources hold something. You are given the visitor's "
    "question, the sentence, the thing it denies, and passages from the editions on the Representative's shelf, each with its "
    "file and lines. Decide whether the passages state the denied thing, in whole or in the part the sentence says is missing. "
    "Use only the passages. Passages that are merely on the same topic, or that do not say the denied thing, do not count.\n"
    'Reply with one JSON object only: {"covered": true or false, "where": "file and lines of the passage that states it, or empty", '
    '"reason": "one short sentence"}'
)


def shipped_items(answer: dict, records: dict[str, dict]) -> list[dict]:
    """One item per sentence the voice wrote and the answer ships (not placed by
    code): its position, the sentence, `bound` when it is cited to a record the
    net accepted, and `withheld` when the net withheld it, which makes it unbound
    whatever its tags."""
    items = []
    for n, entry in enumerate(answer.get("net_sentences", [])):
        if placed_by_code(entry):
            continue
        withheld = entry.get("verdict") != "ok"
        bound = not withheld and bool(valid_bindings(list(entry.get("tags") or []), records))
        items.append({"n": n, "sentence": entry["sentence"], "bound": bound, "withheld": withheld, "why": entry.get("why")})
    return items


def classify_request(question: str, sentence: str) -> dict:
    return {"system": CLASSIFY_SYSTEM, "user": f"QUESTION\n{question}\n\nSENTENCE\n{sentence}"}


def parse_classify(reply: str) -> dict | None:
    found = _JSON.search(reply or "")
    if not found:
        return None
    try:
        data = json.loads(found.group(0))
    except json.JSONDecodeError:
        return None
    kind = data.get("kind")
    denies = data.get("denies")
    if kind not in KINDS or (denies is not None and not isinstance(denies, str)):
        return None
    return {"kind": kind, "denies": (denies or "").strip() or None}


def decide_classified(judgement: dict | None, bound: bool) -> str:
    """keep, withhold, or shelf_check. A bound sentence is never withheld here
    (the verify step reads it against its records) but a denial in it is still
    checked against the shelf. An unreadable reply keeps the sentence."""
    if judgement is None:
        return "keep"
    if judgement["kind"] == "world_claim" and not bound:
        return "withhold"
    if judgement["kind"] == "limit" and judgement["denies"]:
        return "shelf_check"
    return "keep"


def query_terms(question: str, sentence: str, denies: str) -> dict[str, float]:
    """Weighted terms for the shelf search: the denied phrase counts double."""
    terms: dict[str, float] = {}
    for text, weight in ((question, 1.0), (sentence, 1.0), (denies, DENIED_WEIGHT)):
        for word in absence_rule.content_words(text):
            terms[word] = max(terms.get(word, 0.0), weight)
    return terms


def _normalise(word: str) -> str:
    word = re.sub(r"['’]s?$", "", word.strip("-").lower())
    return word[:-1] if len(word) > 5 and word.endswith("s") and not word.endswith("ss") else word


class ShelfIndex:
    """Line positions of a set of terms across the shelf files, built in one pass."""

    def __init__(self, texts_root: Path, files: list[str], terms: set[str]):
        self.root, self.files = texts_root, files
        self.lines: dict[int, list[str]] = {}
        self.postings: dict[str, dict[int, list[int]]] = defaultdict(lambda: defaultdict(list))
        for fi, name in enumerate(files):
            path = texts_root / name
            if not path.exists():
                continue
            lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
            self.lines[fi] = lines
            for number, line in enumerate(lines):
                seen = set()
                for word in _WORD.findall(_MARKUP.sub(" ", line)):
                    stem = _normalise(word)
                    if stem in terms and stem not in seen:
                        seen.add(stem)
                        self.postings[stem][fi].append(number)

    def search(self, terms: dict[str, float]) -> list[dict]:
        """The highest-scoring windows of WINDOW_LINES lines, none overlapping,
        each with at least MIN_DISTINCT_TERMS distinct terms. A term's weight is
        scaled down by how many lines hold it."""
        weight = {t: w / math.log(2 + sum(len(v) for v in self.postings.get(t, {}).values())) for t, w in terms.items() if t in self.postings}
        scored: list[tuple[float, int, int, int]] = []
        for fi in self.lines:
            hits = sorted({(n, t) for t in weight for n in self.postings[t].get(fi, [])})
            starts = sorted({n for n, _ in hits})
            for start in starts:
                present = {t for n, t in hits if start <= n < start + WINDOW_LINES}
                if len(present) >= MIN_DISTINCT_TERMS:
                    scored.append((sum(weight[t] for t in present), fi, start, len(present)))
        scored.sort(reverse=True)
        chosen: list[dict] = []
        for score, fi, start, distinct in scored:
            if any(c["fi"] == fi and abs(c["start"] - start) < WINDOW_LINES for c in chosen):
                continue
            chosen.append({"fi": fi, "start": start, "score": score, "distinct": distinct})
            if len(chosen) == TOP_WINDOWS:
                break
        out = []
        for c in chosen:
            lines = self.lines[c["fi"]]
            first, last = max(c["start"] - PASSAGE_CONTEXT, 0), min(c["start"] + WINDOW_LINES + PASSAGE_CONTEXT, len(lines))
            text = " ".join(_MARKUP.sub(" ", " ".join(lines[first:last])).split())[:PASSAGE_CHARS]
            out.append({"file": self.files[c["fi"]], "lines": f"{first + 1}-{last}", "text": text})
        return out


def shelf_request(question: str, sentence: str, denies: str, passages: list[dict]) -> dict:
    shown = "\n\n".join(f"[{p['file']} lines {p['lines']}]\n{p['text']}" for p in passages) or "(no passage on the shelf matched)"
    return {"system": SHELF_SYSTEM, "user": f"QUESTION\n{question}\n\nSENTENCE\n{sentence}\n\nTHE SENTENCE DENIES\n{denies}\n\nPASSAGES\n\n{shown}"}


def parse_shelf(reply: str) -> dict | None:
    found = _JSON.search(reply or "")
    if not found:
        return None
    try:
        data = json.loads(found.group(0))
    except json.JSONDecodeError:
        return None
    if not isinstance(data.get("covered"), bool):
        return None
    return {"covered": data["covered"], "where": str(data.get("where") or ""), "reason": str(data.get("reason") or "")}


def decide_shelf(judgement: dict | None) -> str:
    """withhold when the shelf states the denied thing; else keep. An unreadable
    reply keeps the sentence."""
    return "withhold" if judgement and judgement["covered"] else "keep"
