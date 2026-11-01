"""What the answer check reads a sentence against: a record as the voice was shown
it (record_pack), what counts as a binding (valid_bindings), the criteria for a
supported sentence (VERIFY_CRITERIA), a judgement read from a reply
(judgement_from), the confidence cap (apply_confidence_cap) and the sentence
splice. engine.m4.answer_check builds the requests and decides.

Binding. A sentence's tags are its bindings. A binding to a context block
(`ctx.` ids, engine.m4.fit_step) or to an id the world does not hold is not a
binding. The judge sees what the voice saw: each bound record's spoken fields as
numbered sentences, plus the force the record carries (its formation confidence and
the years it is limited to). It names the problem when a sentence is not
supported: added detail, dropped or stronger force, widened scope, or a referent
the records do not settle.

Confidence cap. A sentence bound to records of different formation confidence may
state no level higher than the lowest of them: the five levels are Documented,
Widely Accepted, Dominant Modern Reconstruction, Contested, Inferential-Thin,
strongest first.
"""
from __future__ import annotations

import re

from engine.m4 import absence_rule
from engine.m4 import evidence as ev
from engine.m4.fit_step import CONTEXT_PREFIX
from engine.prose import sentences

CONFIDENCE_LEVELS = ("Documented", "Widely Accepted", "Dominant Modern Reconstruction", "Contested", "Inferential-Thin")
PROBLEMS = ("added_detail", "stronger_force", "dropped_scope", "widened_scope", "unresolved_referent", "other")

VERIFY_CRITERIA = (
    "The Representative speaks as \"we\" for its own tradition. The records are given as numbered sentences, with the force "
    "each carries. The sentence is supported only if every assertion in it is stated in the records or follows closely from "
    "them, with the same speaker and the same force. It is not supported if it adds a detail, drops or adds a negation, "
    "states a Contested or inferential point as settled, widens the years or the place a record limits itself to, states as "
    "the whole tradition's what one author says, or uses a word like \"the bishop\" for a person the records do not name. "
    "A sentence that only frames the answer and claims nothing is supported. A word that refers back to something (he, they, \"them\", \"the others\", \"it\") "
    "must name, through the sentence before it, the very person or thing the records say it of; if the records cannot settle it, "
    "or the sentence before points to something else, it is not supported (unresolved_referent). A claim of exclusivity or absence (\"only\", \"never\", \"none\", \"nothing\") is supported only if a bound record states that exclusivity or absence; a record that merely names the thing does not. Each record may carry a MUST NOT ASSERT line: a sentence that "
    "asserts what any bound record says must not be asserted is not supported, and when a sentence joins content from more than "
    "one record it must stay within the narrower scope of them (years, persons, cases covered), the MUST NOT ASSERT line winning. A sentence keeps its records' own hedge, concession and date: it is not supported if it states flatly what a record gives as something the author only allowed, supposed or conceded (stronger_force), or if it states a rule or event without the council, year or occasion the record's own words tie it to (dropped_scope); a span of years a record is limited to is not such a tie. When the records carry "
    "different formation confidence, the sentence may claim no more than the lowest level among them, and may not join "
    "them into one claim stated more firmly. Use no outside knowledge.\n"
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


def judgement_from(data: dict) -> dict | None:
    """A judgement from one reply entry: {"supported", "problem", "reason"}, or None when it carries no boolean verdict."""
    if not isinstance(data, dict) or not isinstance(data.get("supported"), bool):
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
