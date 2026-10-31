"""The verify and rewrite step: each cited sentence of a shipped answer is read
against the records it is bound to, and one that goes beyond them is rewritten
once or taken out.

Shadow only. No live path calls it, and it makes no model call: it builds the
judge's request, reads the reply, and decides.

Binding. A sentence's tags are its bindings. A binding to a context block
(`ctx.` ids, engine.m4.fit_step) or to an id the world does not hold is not a
binding; a sentence left with none is held out: it is not judged and is taken out of the answer. Sentences code
placed itself (a quote, a story, the world's own answer record) are the record's
words and are not read again.

The judge sees what the voice saw: each bound record's spoken fields as numbered
sentences, plus the force the record carries (its formation confidence and the
years it is limited to). It answers supported or unsupported and names the
problem: added detail, dropped or stronger force, widened scope, or a referent
the records do not settle.

Two checks beyond the judge's reading. A word that refers back (a pronoun, "the
others") is read with the sentence before it, and must be settled by the bound
records as that sentence names it, else the sentence is unsupported for an
unresolved referent. A sentence bound to records of different formation
confidence may state no level higher than the lowest of them
(apply_confidence_cap): the five levels are Documented, Widely Accepted, Dominant
Modern Reconstruction, Contested, Inferential-Thin, strongest first.

decide: supported keeps the sentence; unsupported asks for one rewrite; an
unreadable reply keeps the sentence. rewrite_request gives the voice the
sentence, the problem and the same records; parse_rewrite reads back one plain
sentence or a drop. A rewrite that carries a tag, any quotation mark, a line
break or a second sentence, or that states an absence the bound records do not
(engine.m4.absence_rule), is refused. A rewrite that the judge again finds unsupported is taken
out, so a sentence is rewritten at most once.
"""
from __future__ import annotations

import json
import re

from engine.m4 import absence_rule
from engine.m4 import evidence as ev
from engine.m4.grounding_net import placed_by_code
from engine.m4.fit_step import CONTEXT_PREFIX
from engine.prose import sentences

CONFIDENCE_LEVELS = ("Documented", "Widely Accepted", "Dominant Modern Reconstruction", "Contested", "Inferential-Thin")
PROBLEMS = ("added_detail", "stronger_force", "dropped_scope", "widened_scope", "unresolved_referent", "other")
_JSON = re.compile(r"\{.*\}", re.DOTALL)
_DROP = "DROP"

VERIFY_SYSTEM = (
    "You check one sentence a historical Representative said against the records it was bound to. "
    "The Representative speaks as \"we\" for its own tradition. The records are given as numbered sentences, with the force "
    "each carries. The sentence is supported only if every assertion in it is stated in the records or follows closely from "
    "them, with the same speaker and the same force. It is not supported if it adds a detail, drops or adds a negation, "
    "states a Contested or inferential point as settled, widens the years or the place a record limits itself to, states as "
    "the whole tradition's what one author says, or uses a word like \"the bishop\" for a person the records do not name. "
    "A sentence that only frames the answer and claims nothing is supported. A word that refers back to something (he, they, \"them\", \"the others\", \"it\") "
    "must name, through the sentence before it, the very person or thing the records say it of; if the records cannot settle it, "
    "or the sentence before points to something else, it is not supported (unresolved_referent). When the records carry "
    "different formation confidence, the sentence may claim no more than the lowest level among them, and may not join "
    "them into one claim stated more firmly. Use no outside knowledge.\n"
    'Reply with one JSON object only: {"supported": true or false, "problem": one of "added_detail", "stronger_force", '
    '"dropped_scope", "widened_scope", "unresolved_referent", "other" or null when supported, "reason": "one short sentence"}'
)
REWRITE_SYSTEM = (
    "You rewrite one sentence a historical Representative said. The reader found a problem with it. If the problem is an "
    "unresolved referent, name the person or thing in the sentence itself instead of using a pronoun. Rewrite it so that it "
    "says only what the bound records say, in the author's name, as a close paraphrase, with the same force "
    "and the same limits the records carry. Keep the voice: \"we\", plain words, sentences under 25 words. Add nothing the "
    "records do not state. Use no tags and no quotation marks. If nothing of the sentence is left that the records support, "
    f"reply with the single word {_DROP}.\n"
    "Reply with the rewritten sentence only, on one line."
)


def valid_bindings(tags: list[str], records: dict[str, dict]) -> list[str]:
    return [t for t in dict.fromkeys(tags) if not t.startswith(CONTEXT_PREFIX) and t in records]


def _voiced_text(record: dict) -> str:
    """What the voice was shown of a record: the head its evidence entry uses
    (a story's tellable_as, a quote's modern_rendering, a limit's statement),
    else the record's spoken fields."""
    if record.get("record_type") in ("story", "quote"):
        try:
            return ev._head_text(record)
        except ValueError:
            return ""
    return absence_rule.spoken_text(record)


def record_pack(record: dict, records: dict[str, dict]) -> str:
    """The record as the voice was shown it: its voiced text as numbered
    sentences, its means line, what it must not be used to assert, what is not
    known, a quote's setting, and the force it carries (formation confidence and
    the years it is limited to)."""
    rider = ev._with_quote_index(ev._with_riders({"id": record["id"], "record_type": record.get("record_type")}, records), records)
    conf = (record.get("confidence") or {}).get("formation_confidence")
    years = absence_rule._years(record)
    kind = record.get("classification")
    force = ", ".join(x for x in (f"classification: {kind}" if isinstance(kind, str) and kind else "", f"formation confidence: {conf}" if conf else "", f"limited to the years {years[0]} to {years[1]}" if years else "") if x)
    lines = [f"({n}) {t}" for n, t in enumerate(sentences(_voiced_text(record)), start=1)]
    if rider.get("speaker"):
        lines.insert(0, f"quote from {rider['speaker']}")
    if means := (record.get("use_note") or {}).get("means"):
        lines.append(f"means: {means}")
    if rider.get("setting"):
        lines.append(f"setting: {rider['setting']}")
    if rider.get("claim_guards"):
        lines.append("MUST NOT ASSERT: " + "; ".join(rider["claim_guards"]))
    if rider.get("absent_detail"):
        lines.append("NOT KNOWN: " + rider["absent_detail"])
    return f"Record {record['id']} [{force or 'no stated limit'}]\n" + "\n".join(lines)


def _record_level(record: dict) -> int | None:
    conf = (record.get("confidence") or {}).get("formation_confidence")
    return next((i for i, level in enumerate(CONFIDENCE_LEVELS) if isinstance(conf, str) and conf.lower().startswith(level.lower())), None)


def confidence_exceeds(sentence: str, bound: list[str], records: dict[str, dict]) -> bool:
    """True when the sentence names a formation-confidence level (written as the
    five names are, capitalised) higher than the lowest level among the records
    it is bound to."""
    levels = [lv for lv in (_record_level(records[r]) for r in bound if r in records) if lv is not None]
    if not levels:
        return False
    lowest = max(levels)
    flat = re.sub(r"\s+", " ", sentence)
    return any(i < lowest and re.search(rf"\b{re.escape(level)}\b", flat) for i, level in enumerate(CONFIDENCE_LEVELS))


def _ships_through_verify(entry: dict, records: dict[str, dict]) -> bool:
    """True for a net sentence the verify step leaves in the answer: not
    withheld, and either untagged, placed by code, or holding a valid binding."""
    tags = list(entry.get("tags") or [])
    return entry.get("verdict") == "ok" and (not tags or placed_by_code(entry) or bool(valid_bindings(tags, records)))


def sentence_items(answer: dict, records: dict[str, dict]) -> list[dict]:
    """One item per cited, voice-written sentence of an answer's net output:
    its position, the sentence, the sentence before it that stays in the answer
    (`before`, for words that refer back), its valid bindings, and `held_out` when it has
    tags but none valid."""
    items = []
    for n, entry in enumerate(answer.get("net_sentences", [])):
        tags = list(entry.get("tags") or [])
        if entry.get("verdict") != "ok" or not tags or placed_by_code(entry):
            continue
        bound = valid_bindings(tags, records)
        before = next((e["sentence"] for e in reversed(answer["net_sentences"][:n]) if _ships_through_verify(e, records)), "")
        items.append({"n": n, "sentence": entry["sentence"], "before": before, "bound": bound, "held_out": not bound})
    return items


def verify_request(sentence: str, bound: list[str], records: dict[str, dict], before: str = "") -> dict:
    packs = "\n\n".join(record_pack(records[rid], records) for rid in bound)
    context = f"SENTENCE BEFORE IT (read it for what a referring word points to)\n{before}\n\n" if before else ""
    return {"system": VERIFY_SYSTEM, "user": f"RECORDS\n\n{packs}\n\n{context}SENTENCE\n{sentence}"}


def parse_verify(reply: str) -> dict | None:
    found = _JSON.search(reply or "")
    if not found:
        return None
    try:
        data = json.loads(found.group(0))
    except json.JSONDecodeError:
        return None
    if not isinstance(data.get("supported"), bool):
        return None
    problem = data.get("problem")
    return {"supported": data["supported"], "problem": problem if problem in PROBLEMS else ("other" if not data["supported"] else None),
            "reason": str(data.get("reason") or "")}


def apply_confidence_cap(judgement: dict | None, sentence: str, bound: list[str], records: dict[str, dict]) -> dict | None:
    """A supported reading, turned to unsupported (stronger_force) when the
    sentence names a level above the lowest of its bound records. An unsupported
    reading keeps the judge's own problem."""
    if judgement is not None and judgement["supported"] and confidence_exceeds(sentence, bound, records):
        return {"supported": False, "problem": "stronger_force", "reason": "names a confidence level above the lowest of the records it is bound to"}
    return judgement


def read_reply(reply: str, sentence: str, bound: list[str], records: dict[str, dict]) -> dict | None:
    """A judge's reply read with the confidence cap applied."""
    return apply_confidence_cap(parse_verify(reply), sentence, bound, records)


def decide(judgement: dict | None) -> str:
    """keep or rewrite. An unreadable reply keeps the sentence."""
    return "rewrite" if judgement and not judgement["supported"] else "keep"


def rewrite_request(question: str, sentence: str, judgement: dict, bound: list[str], records: dict[str, dict]) -> dict:
    packs = "\n\n".join(record_pack(records[rid], records) for rid in bound)
    problem = f"{judgement.get('problem') or 'other'}: {judgement.get('reason') or ''}".strip()
    return {"system": REWRITE_SYSTEM, "user": f"QUESTION\n{question}\n\nRECORDS\n\n{packs}\n\nSENTENCE\n{sentence}\n\nPROBLEM\n{problem}"}


_QUOTE_MARKS = frozenset('"“”‘’\'«»‹›„')
_APOSTROPHES = frozenset("'’")


def _has_quotation_mark(text: str) -> bool:
    """Any quotation mark. An apostrophe between two letters (don't) or after a
    plural s before a space or the end (apostles') is not one."""
    for i, ch in enumerate(text):
        if ch not in _QUOTE_MARKS:
            continue
        before = text[i - 1] if i else ""
        after = text[i + 1] if i + 1 < len(text) else ""
        if ch in _APOSTROPHES and ((before.isalpha() and after.isalpha()) or (before == "s" and not after.isalnum())):
            continue
        return True
    return False


def parse_rewrite(reply: str, bound: list[str] | None = None, records: dict[str, dict] | None = None) -> str | None:
    """The one sentence, or None for a drop or a refused rewrite. A rewrite is
    refused when it carries a tag, any quotation mark, a line break or more than
    one sentence, or when, given the bound records, it states an absence they do
    not (engine.m4.absence_rule). Apostrophes inside words are not quotation marks."""
    text = (reply or "").strip()
    if not text or text.upper().rstrip(".") == _DROP or "\n" in text or "[[" in text:
        return None
    if _has_quotation_mark(text) or len(sentences(text)) != 1:
        return None
    if bound and records and absence_rule.check_absence(text, [records[r] for r in bound if r in records]):
        return None
    return text


def splice(text: str, old: str, new: str | None) -> tuple[str, bool]:
    """The answer text with one whole sentence replaced, or removed when new is
    None, and whether it was found. Only a match that stands as a sentence
    (start of the text or after a space or line break, ending at a space, line
    break or the end) is replaced."""
    for found in re.finditer(re.escape(old), text):
        before = text[: found.start()]
        after = text[found.end():]
        if (not before or before[-1] in " \n") and (not after or after[0] in " \n"):
            out = before + (new or "") + after
            out = re.sub(r"[ \t]+\n", "\n", re.sub(r" {2,}", " ", out))
            return re.sub(r"\n{3,}", "\n\n", out).strip(), True
    return text, False
