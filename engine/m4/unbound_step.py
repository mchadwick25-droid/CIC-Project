"""The unbound-sentence step: a sentence the voice ships with no valid binding is
either a connective, a statement about the conversation, or withheld; and a
sentence that says something is missing stays only if a record states it.

Shadow only. No live path calls it, and it makes no model call: it builds the
judge's requests, reads the replies, and decides.

Why. engine.m4.verify_step reads only sentences bound to a record. A sentence
with no valid binding (no tag, a context-block id, an unknown id, or a verdict
the net withheld) ships as plain text, and the net's own exemption for honesty
scaffolding lets a sentence that says what the world's sources lack ship with no
check at all. That is where an invented absence ("nothing we carry speaks of
him") gets through, whatever its phrasing.

Rule. A sentence the net withheld is taken out. Every other sentence the voice
wrote is classified by a reader that sees only the question and the sentence:

  connective   joins, frames or moves on, and claims nothing about history,
               people, texts or what the sources hold: kept
  conversation is about this conversation itself: kept
  world_claim  states any fact about people, events, teaching, texts or the
               tradition: withheld when unbound, left to the verify step when bound
  limit        says the records or sources lack, do not say, never describe or
               cannot give something, or that something is not known: kept only
               when it is bound and a cited record states that limit with its
               scope (engine.m4.absence_rule.check_limit), whatever its wording.
               Otherwise withheld. No search of the shelf is made: an absence
               is a claim about what the world's records hold, and only a
               record can state it.

A sentence worded as a limit or an exclusive claim ("only", "nothing", "never",
"does not say") gets the same test whatever the reader called it. A sentence that
names a confidence level or says how a claim is tagged is withheld.

When withheld limits leave an answer with almost nothing (under
FALLBACK_BELOW_WORDS words), one fallback sentence stands where the first one
stood: LIMIT_FALLBACK when the answer goes on after it, LIMIT_FALLBACK_ALONE when
nothing follows. A longer answer simply says less.
"""
from __future__ import annotations

import json
import re

from engine.m4 import absence_rule
from engine.m4.grounding_net import placed_by_code
from engine.m4.verify_step import valid_bindings

KINDS = ("connective", "conversation", "world_claim", "limit")
LIMIT_FALLBACK = "We do not have that here. Here is what we can tell you."
LIMIT_FALLBACK_ALONE = "We do not have that here."
FALLBACK_BELOW_WORDS = 25
_LIMIT_WORDING = re.compile(
    r"\b(?:only|nothing|never|none|nobody|no\s+one|cannot|can't|not\s+known|"
    r"(?:does|do|did)\s+not\s+(?:say|describe|name|mention|give|tell|state|speak)|"
    r"no\b[^.!?]{0,60}?\bbut)\b",
    re.IGNORECASE,
)
_TAG_TALK = re.compile(
    r"\b(?:Widely\s+Accepted|Dominant\s+Modern\s+Reconstruction|Inferential-Thin)\b"
    r"|\bformation\s+confidence\b"
    r"|\b(?:hold|held|call|rate|rated|tagged|marked)\b[^.!?]{0,40}\b(?:Documented|Contested)\b"
)
_JSON = re.compile(r"\{.*\}", re.DOTALL)

CLASSIFY_SYSTEM = (
    "You read one sentence a historical Representative said to a visitor, with the visitor's question. The sentence "
    "carries no citation. Decide which kind it is.\n"
    "connective: it only joins, frames or moves on, and claims nothing about history, people, texts, teaching or what the "
    "sources hold (for example \"Here is what we can say.\", \"That is the plain answer.\").\n"
    "conversation: it is about this conversation itself (what was asked, what comes next, an offer to go on).\n"
    "world_claim: it states any fact about people, events, teaching, texts or the tradition.\n"
    "limit: it says that the records or sources lack, do not say, never describe or cannot give something, or that something "
    "is not known.\n"
    'Reply with one JSON object only: {"kind": "connective" or "conversation" or "world_claim" or "limit"}'
)


def shipped_items(answer: dict, records: dict[str, dict]) -> list[dict]:
    """One item per sentence the voice wrote and the answer ships (not placed by
    code): its position, the sentence, `bound` when it is cited to a record the
    net accepted, `records` (those records' ids), and `withheld` when the net
    withheld it, which makes it unbound whatever its tags."""
    items = []
    for n, entry in enumerate(answer.get("net_sentences", [])):
        if placed_by_code(entry):
            continue
        withheld = entry.get("verdict") != "ok"
        ids = [] if withheld else valid_bindings(list(entry.get("tags") or []), records)
        items.append({"n": n, "sentence": entry["sentence"], "bound": bool(ids), "records": ids, "withheld": withheld, "why": entry.get("why")})
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
    return {"kind": kind} if kind in KINDS else None


def limit_backed(item: dict, records: dict[str, dict]) -> bool:
    """True when a record the sentence is bound to states the limit it voices,
    with that record's scope."""
    cited = [records[r] for r in item.get("records") or [] if r in records]
    return bool(cited) and absence_rule.check_limit(item["sentence"], cited) is None


def says_limit(sentence: str) -> bool:
    """True when the wording is that of a limit or an exclusive claim ("only",
    "nothing", "never", "does not say"), whatever a reader called the sentence."""
    return bool(_LIMIT_WORDING.search(sentence))


def talks_of_tags(sentence: str) -> bool:
    """True when the sentence names a confidence level or says how a claim is
    tagged; the voice never describes how its claims are checked or tagged."""
    return bool(_TAG_TALK.search(sentence))


def decide_classified(judgement: dict | None, item: dict, records: dict[str, dict]) -> str:
    """keep, withhold, withhold_limit or withhold_tags. A sentence that talks of
    confidence tags is withheld. An unbound world claim is withheld; a bound one
    is left to the verify step. A limit, or any sentence worded as one, is kept
    only when bound to a record that states it. An unreadable reply keeps the
    sentence."""
    if talks_of_tags(item["sentence"]):
        return "withhold_tags"
    if judgement is None:
        return "keep"
    if judgement["kind"] == "world_claim" and not item["bound"]:
        return "withhold"
    if (judgement["kind"] == "limit" or says_limit(item["sentence"])) and not limit_backed(item, records):
        return "withhold_limit"
    return "keep"
