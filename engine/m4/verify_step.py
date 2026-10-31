"""The verify and rewrite step: each cited sentence of a shipped answer is read
against the records it is bound to, and one that goes beyond them is rewritten
once or taken out.

Shadow only. No live path calls it, and it makes no model call: it builds the
judge's request, reads the reply, and decides.

Binding. A sentence's tags are its bindings. A binding to a context block
(`ctx.` ids, engine.m4.fit_step) or to an id the world does not hold is not a
binding; a sentence left with none is held out and never judged. Sentences code
placed itself (a quote, a story, the world's own answer record) are the record's
words and are not read again.

The judge sees what the voice saw: each bound record's spoken fields as numbered
sentences, plus the force the record carries (its formation confidence and the
years it is limited to). It answers supported or unsupported and names the
problem: added detail, dropped or stronger force, widened scope, or a referent
the records do not settle.

decide: supported keeps the sentence; unsupported asks for one rewrite; an
unreadable reply keeps the sentence. rewrite_request gives the voice the
sentence, the problem and the same records; parse_rewrite reads back one plain
sentence or a drop. A rewrite that carries a tag, a quotation mark or a line
break is refused. A rewrite that the judge again finds unsupported is taken
out, so a sentence is rewritten at most once.
"""
from __future__ import annotations

import json
import re

from engine.m4 import absence_rule
from engine.m4.fit_step import CONTEXT_PREFIX
from engine.prose import sentences

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
    "A sentence that only frames the answer and claims nothing is supported. Use no outside knowledge.\n"
    'Reply with one JSON object only: {"supported": true or false, "problem": one of "added_detail", "stronger_force", '
    '"dropped_scope", "widened_scope", "unresolved_referent", "other" or null when supported, "reason": "one short sentence"}'
)
REWRITE_SYSTEM = (
    "You rewrite one sentence a historical Representative said. The reader found a problem with it. Rewrite it so that it "
    "says only what the bound records say, in the author's name, as a quotation or a close paraphrase, with the same force "
    "and the same limits the records carry. Keep the voice: \"we\", plain words, sentences under 25 words. Add nothing the "
    "records do not state. Use no tags and no quotation marks. If nothing of the sentence is left that the records support, "
    f"reply with the single word {_DROP}.\n"
    "Reply with the rewritten sentence only, on one line."
)


def valid_bindings(tags: list[str], records: dict[str, dict]) -> list[str]:
    return [t for t in dict.fromkeys(tags) if not t.startswith(CONTEXT_PREFIX) and t in records]


def record_pack(record: dict) -> str:
    conf = (record.get("confidence") or {}).get("formation_confidence")
    years = absence_rule._years(record)
    force = ", ".join(x for x in (f"formation confidence: {conf}" if conf else "", f"limited to the years {years[0]} to {years[1]}" if years else "") if x)
    lines = [f"({n}) {s}" for n, s in enumerate(sentences(absence_rule.spoken_text(record)), start=1)]
    return f"Record {record['id']} [{force or 'no stated limit'}]\n" + "\n".join(lines)


def sentence_items(answer: dict, records: dict[str, dict]) -> list[dict]:
    """One item per cited, voice-written sentence of an answer's net output:
    its position, the sentence, its valid bindings, and `held_out` when it has
    tags but none valid."""
    placed = set((answer.get("reply_shape") or {}).get("placed", []))
    items = []
    for n, entry in enumerate(answer.get("net_sentences", [])):
        tags = list(entry.get("tags") or [])
        if entry.get("verdict") != "ok" or not tags or entry.get("placed_quote") or (set(tags) & placed):
            continue
        bound = valid_bindings(tags, records)
        items.append({"n": n, "sentence": entry["sentence"], "bound": bound, "held_out": not bound})
    return items


def verify_request(sentence: str, bound: list[str], records: dict[str, dict]) -> dict:
    packs = "\n\n".join(record_pack(records[rid]) for rid in bound)
    return {"system": VERIFY_SYSTEM, "user": f"RECORDS\n\n{packs}\n\nSENTENCE\n{sentence}"}


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


def decide(judgement: dict | None) -> str:
    """keep or rewrite. An unreadable reply keeps the sentence."""
    return "rewrite" if judgement and not judgement["supported"] else "keep"


def rewrite_request(question: str, sentence: str, judgement: dict, bound: list[str], records: dict[str, dict]) -> dict:
    packs = "\n\n".join(record_pack(records[rid]) for rid in bound)
    problem = f"{judgement.get('problem') or 'other'}: {judgement.get('reason') or ''}".strip()
    return {"system": REWRITE_SYSTEM, "user": f"QUESTION\n{question}\n\nRECORDS\n\n{packs}\n\nSENTENCE\n{sentence}\n\nPROBLEM\n{problem}"}


def parse_rewrite(reply: str) -> str | None:
    """The one sentence, or None for a drop or a refused rewrite."""
    text = (reply or "").strip()
    if not text or text.upper().rstrip(".") == _DROP or "\n" in text or "[[" in text or '"' in text or "“" in text:
        return None
    return text


def splice(text: str, old: str, new: str | None) -> str:
    """The answer text with one sentence replaced, or removed when new is None."""
    if old not in text:
        return text
    out = text.replace(old, new or "", 1)
    out = re.sub(r"[ \t]+\n", "\n", re.sub(r" {2,}", " ", out))
    return re.sub(r"\n{3,}", "\n\n", out).strip()
