"""One labeller verdict: the prompt, the reply's shape, and the check that
binds every verdict to words really present in the evidence.

The labeller sees the sentence and its evidence pack only: never the probe,
the world's other answers, the gates' decision, any judge's verdict, or
whether the item is a seeded defect. A reply that is not valid JSON, names a
class outside the vocabulary, or quotes words not found verbatim in the
block it names is not a label; it is kept as a rejected reply and the item
stays unlabelled.
"""
import json
import re
import unicodedata

from goldset.evidence import block_text, render_pack

VERDICTS = ("supported", "unsupported", "no_claim", "cannot_judge")
CLASSES = ("false_friend", "negation_modal_shift", "generalisation", "embedded_voice", "unsupported_other")
KEY_CLASSES = ("false_friend", "negation_modal_shift", "generalisation", "embedded_voice")

SYSTEM_PROMPT = """You are a scholar of early and medieval Christian sources and of the editions they survive in. You check one sentence that a historical Representative of a Christian tradition said, against the evidence it was bound to. The Representative speaks in the first person plural ("we", "our") for its own tradition.

You are given the sentence and an evidence pack:
- BOUND RECORDS [R1, R2 ...]: the reviewed records the sentence was bound to. These are the evidence the sentence must rest on.
- SOURCE PASSAGES [P1 ...]: the edition text each record rests on, with its division. The lines the record cites are marked. Editors' notes appear as [editor's note: ...]; they are the editor's words, not the source's. A passage may be a translation; its language is given.
- LEXICON RISK FLAGS [L]: words of this tradition whose modern sense misleads, and what they must not be read as.

Decide whether the sentence is supported by its bound records, read correctly in the light of their sources. Judge only what the sentence asserts. Use what you know of the period only to read the evidence correctly, never to supply a claim the evidence does not make.

Verdicts:
- "supported": every assertion in the sentence is stated in the bound records or follows closely from them, attributed to the right speaker, with the same force.
- "unsupported": at least one assertion is not in the bound records, is contradicted by them, or changes what they say.
- "no_claim": the sentence asserts nothing about the tradition, its people, texts or history (a greeting, a turn between points).
- "cannot_judge": the pack does not let you decide (say exactly what is missing).

When the verdict is "unsupported", give the failure class that best describes it, and any others that also apply:
- "false_friend": the sentence depends on reading a word in a modern sense the source does not carry (for example "prevent" meaning to go before, "let" meaning to hinder, "conversation" meaning way of life, "charity" meaning love, "catholic" meaning universal), including any word in the lexicon risk flags.
- "negation_modal_shift": the sentence drops, adds or reverses a negation, or shifts a modal or quantifier (may to must, some to all, often to always, could to did).
- "generalisation": the sentence states as the tradition's own position ("we held", "our church taught", "all of us") what the evidence gives as one author's view, one text, one occasion or one group; or turns one instance into a habit. A "we" sentence is supported only when a bound record itself states the position as the tradition's.
- "embedded_voice": the sentence gives as the tradition's or the author's own view words that in the evidence belong to someone else: an opponent, an interlocutor, a correspondent whose letter is quoted, a hostile witness, or an editor.
- "unsupported_other": anything else unsupported: an added name, date, number, place, cause or detail; a claim the records do not make; a contradiction.

Bind every verdict to the exact words. Give at least one evidence entry: copy, character for character, the words from one block that support the sentence or that show it is wrong (for an absent claim, the words the sentence would have to rest on). Name the block id. Copy at least four and no more than about forty consecutive words per entry. If the bound record itself misreads its own source, say so in "record_concern"; that does not change your verdict on the sentence against the record.

Reply with one JSON object and nothing else:
{"verdict": "...", "failure_class": null or "...", "other_classes": [], "evidence": [{"block": "R1", "words": "..."}], "reason": "one or two plain sentences", "record_concern": null or "..."}"""


def user_message(sentence: str, pack: dict) -> str:
    return f"EVIDENCE PACK\n\n{render_pack(pack)}\n\nSENTENCE TO CHECK\n{sentence}"


def _fold(text: str) -> str:
    text = unicodedata.normalize("NFKC", text)
    text = text.translate(str.maketrans({"‘": "'", "’": "'", "“": '"', "”": '"', "—": "-", "–": "-"}))
    return " ".join(text.lower().split())


_JSON = re.compile(r"\{.*\}", re.DOTALL)
_WORDS = re.compile(r"\w+")
MIN_EVIDENCE_WORDS = 4


def words_in(words: str, text: str) -> bool:
    """The quoted words occur in the text as a run of whole words, at least
    MIN_EVIDENCE_WORDS long (or the whole text, when it is shorter)."""
    quoted = _WORDS.findall(_fold(words))
    tokens = _WORDS.findall(_fold(text))
    if len(quoted) < min(MIN_EVIDENCE_WORDS, len(tokens)) or not quoted:
        return False
    first = quoted[0]
    return any(tokens[i:i + len(quoted)] == quoted for i, t in enumerate(tokens) if t == first)


def parse_reply(reply: str, pack: dict) -> dict:
    """{"ok": True, "label": {...}} or {"ok": False, "why": ...}."""
    found = _JSON.search(reply or "")
    if not found:
        return {"ok": False, "why": "no JSON object in the reply"}
    try:
        label = json.loads(found.group(0))
    except json.JSONDecodeError as error:
        return {"ok": False, "why": f"reply is not valid JSON: {error}"}
    verdict = label.get("verdict")
    if verdict not in VERDICTS:
        return {"ok": False, "why": f"verdict {verdict!r} is not one of {VERDICTS}"}
    primary = label.get("failure_class")
    others = label.get("other_classes") or []
    if verdict == "unsupported":
        if primary not in CLASSES or any(c not in CLASSES for c in others):
            return {"ok": False, "why": f"unsupported needs a failure class from {CLASSES}"}
    elif primary or others:
        return {"ok": False, "why": "a failure class is given for a verdict that is not unsupported"}
    evidence = label.get("evidence") or []
    if verdict != "cannot_judge" and not evidence:
        return {"ok": False, "why": "no evidence words given"}
    if not isinstance(evidence, list) or any(not isinstance(e, dict) for e in evidence):
        return {"ok": False, "why": "evidence must be a list of objects with a block and words"}
    for entry in evidence:
        text = block_text(pack, str(entry.get("block")))
        words = str(entry.get("words") or "")
        if text is None:
            return {"ok": False, "why": f"evidence names block {entry.get('block')!r}, which the pack does not have"}
        if not words_in(words, text):
            return {"ok": False, "why": f"evidence words are not a run of at least {MIN_EVIDENCE_WORDS} whole words found verbatim in block {entry.get('block')}: {words[:80]!r}"}
    return {"ok": True, "label": {
        "verdict": verdict, "failure_class": primary if verdict == "unsupported" else None,
        "other_classes": list(others) if verdict == "unsupported" else [],
        "evidence": [{"block": str(e["block"]), "words": str(e["words"])} for e in evidence],
        "reason": str(label.get("reason") or ""), "record_concern": label.get("record_concern") or None,
    }}


def gold_class(label: dict) -> str:
    """The six-way class the targets are counted in: supported, or the
    failure class ("unsupported" for unsupported_other)."""
    if label["verdict"] == "supported":
        return "supported"
    if label["verdict"] == "unsupported":
        return "unsupported" if label["failure_class"] == "unsupported_other" else label["failure_class"]
    return label["verdict"]
