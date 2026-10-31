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

A sentence that names a confidence level or says how a claim is tagged is withheld.
An exclusive claim ("only", "never", "none") bound to a record is read by the verify
step, which needs the records to state the exclusivity.

Bind or repair, withhold last. A sentence the rule would withhold (an unbound world
claim, or a limit no record states) is first offered, with the records offered
for the turn, to a reader who binds it to the record that states it (it stays,
tagged to that record), repairs it to the narrower or broader scope the record
carries, or finds no support (BIND_SYSTEM). A bound or repaired sentence is then
read against its record like any bound sentence, and a limit must also pass the
limit test against that record. Only a sentence with no support is withheld.

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
from engine.m4.verify_step import _ships_through_verify, parse_rewrite, record_pack, valid_bindings

BIND_ACTIONS = ("bind", "repair", "none")
KINDS = ("connective", "conversation", "world_claim", "limit")
LIMIT_FALLBACK = "We do not have that here. Here is what we can tell you."
LIMIT_FALLBACK_ALONE = "We do not have that here."
FALLBACK_BELOW_WORDS = 25
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


BIND_SYSTEM = (
    "You help a historical Representative keep a sentence it said. The sentence carries no valid citation. You are given the "
    "visitor's question, the sentence, and the records offered for this turn as numbered sentences with the force each carries. "
    "Decide one of three things.\n"
    "bind: one offered record states what the sentence says, with the same speaker, force and scope; give its id, and the sentence "
    "stays as it is.\n"
    "repair: the sentence is right in part, or too broad or too narrow for the records; rewrite it as one plain sentence under "
    "25 words, in \"we\", as a close paraphrase of what one offered record states, with that record's force and limits, with no "
    "quotation marks and no tag; give that record's id and the rewritten sentence.\n"
    "none: no offered record supports any version of it.\n"
    "Use no outside knowledge.\n"
    'Reply with one JSON object only: {"action": "bind" or "repair" or "none", "record": "the record id" or null, '
    '"sentence": "the rewritten sentence" or null}'
)


def bind_request(question: str, sentence: str, offered: list[str], records: dict[str, dict]) -> dict:
    packs = "\n\n".join(record_pack(records[r], records) for r in offered if r in records)
    return {"system": BIND_SYSTEM, "user": f"QUESTION\n{question}\n\nRECORDS OFFERED\n\n{packs}\n\nSENTENCE\n{sentence}"}


def parse_bind(reply: str, sentence: str, offered: list[str], records: dict[str, dict]) -> dict | None:
    """{"action", "record", "sentence"} for a bind or a repair that stands, else
    None: an unreadable reply, a record that was not offered, a repair that is
    not one plain sentence (engine.m4.verify_step.parse_rewrite), or none."""
    found = _JSON.search(reply or "")
    if not found:
        return None
    try:
        data = json.loads(found.group(0))
    except json.JSONDecodeError:
        return None
    action, record = data.get("action"), data.get("record")
    if action not in ("bind", "repair") or record not in offered or record not in records:
        return None
    if action == "bind":
        return {"action": "bind", "record": record, "sentence": sentence}
    new = parse_rewrite(str(data.get("sentence") or ""), [record], records)
    return {"action": "repair", "record": record, "sentence": new} if new and not talks_of_tags(new) else None


def bind_reply_readable(reply: str) -> bool:
    """True when a bind reply is one JSON object with a known action."""
    found = _JSON.search(reply or "")
    if not found:
        return False
    try:
        return json.loads(found.group(0)).get("action") in BIND_ACTIONS
    except (json.JSONDecodeError, AttributeError):
        return False


def bound_limit_stands(new_sentence: str, record_id: str, was_limit: bool, records: dict[str, dict]) -> bool:
    """A sentence that says something is missing stays bound only when the
    record it is bound to states that limit; any other sentence needs only the
    verify read."""
    return not was_limit or limit_backed({"sentence": new_sentence, "records": [record_id]}, records)


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
        before = next((e["sentence"] for e in reversed(answer["net_sentences"][:n]) if _ships_through_verify(e, records)), "")
        items.append({"n": n, "sentence": entry["sentence"], "before": before, "bound": bool(ids), "records": ids, "withheld": withheld, "why": entry.get("why")})
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


def talks_of_tags(sentence: str) -> bool:
    """True when the sentence names a confidence level or says how a claim is
    tagged; the voice never describes how its claims are checked or tagged."""
    return bool(_TAG_TALK.search(sentence))


def decide_classified(judgement: dict | None, item: dict, records: dict[str, dict]) -> str:
    """keep, withhold, withhold_limit or withhold_tags. A sentence that talks of
    confidence tags is withheld. An unbound world claim is withheld; a bound one
    is left to the verify step. A limit is kept only when bound to a record that
    states it. An unreadable reply keeps the sentence."""
    if talks_of_tags(item["sentence"]):
        return "withhold_tags"
    if judgement is None:
        return "keep"
    if judgement["kind"] == "world_claim" and not item["bound"]:
        return "withhold"
    if judgement["kind"] == "limit" and not limit_backed(item, records):
        return "withhold_limit"
    return "keep"
