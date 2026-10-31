"""Bound drafting: every sentence the voice writes carries the ids of the records
it rests on and a label, so what ships is decided from the draft itself.

Shadow only. No registered frame sets `bound_drafting`, and nothing here makes a
model call.

The voice ends each sentence with its record tags, then one marker:
[[as:paraphrase]] (it closely restates what those records say, in the author's
name) or [[as:inference]] (it goes past them). Quotations come only from
[[quote:id]] placements. A sentence with no valid binding ships only when it is
a question to the visitor or one of the world's reviewed connectives (a closed
list, `normalize` then exact match). The rigor line allows quotation and close
paraphrase only, so an inference never ships.

`decide` gives one verdict per sentence the net let through:
  keep               to the verify step when it has a valid binding, else as it stands
  withhold_inference the voice labelled it an inference
  withhold_unlabelled it has a binding but the voice gave it no label
  withhold_unbound   no valid binding, not a question, not a reviewed connective
  withhold_tags      it names a confidence level or says how a claim is tagged
A sentence the net withheld stays withheld (`withhold_net`); the net removes only some
of its withholds from the text, so the words of the rest are taken out here. A sentence placed by code (a quote,
a story, the world's own answer record) is the record's words and is kept.

When withheld sentences leave under FALLBACK_BELOW_WORDS words, the world's
fallback sentence stands where the first withheld sentence stood.
"""
import re

from engine.m4.grounding_net import LABEL_MARKER, placed_by_code
from engine.m4.verify_step import _voiced_text, valid_bindings

LABELS = ("paraphrase", "inference")
FALLBACK = "We do not have that here. Here is what we can tell you."
FALLBACK_ALONE = "We do not have that here."
FALLBACK_BELOW_WORDS = 25
_TAG_TALK = re.compile(
    r"\b(?:Widely\s+Accepted|Dominant\s+Modern\s+Reconstruction|Inferential-Thin)\b"
    r"|\bformation\s+confidence\b"
    r"|\b(?:hold|held|call|rate|rated|tagged|marked)\b[^.!?]{0,40}\b(?:Documented|Contested)\b"
)

DIRECTIVE_LINES = (
    "Every sentence you write ends with the ids of the records it rests on, then one marker: "
    "[[as:paraphrase]] when it closely restates what those records say, in the author's name; "
    "[[as:inference]] when it goes past them. Use inference only if you must; it will not be spoken. "
    "Quote only by [[quote:id]].",
    "A sentence with no record id is spoken only if it is a question to the visitor or one of these joining sentences: {connectives}. "
    "Say what the sources lack only from a limit record in your ground, cited. Keep the answer's depth and the world's own images.",
)


def directive_lines(connectives: list[str]) -> list[str]:
    listed = "; ".join(f'"{c}"' for c in connectives) if connectives else "none"
    return [DIRECTIVE_LINES[0], DIRECTIVE_LINES[1].format(connectives=listed)]


def normalize(sentence: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"[^\w\s']", "", sentence.lower())).strip()


def connective_set(sentences: list[str]) -> frozenset[str]:
    return frozenset(normalize(s) for s in sentences if normalize(s))


def label_of(raw_sentence: str) -> str | None:
    found = LABEL_MARKER.search(raw_sentence or "")
    return found.group(1).lower() if found else None


def talks_of_tags(sentence: str) -> bool:
    return bool(_TAG_TALK.search(sentence))


def _is_question(sentence: str) -> bool:
    return sentence.rstrip().endswith("?")


def bindings(tags: list[str], records: dict[str, dict]) -> list[str]:
    """The tags that are bindings: records the world holds that have words the voice was shown
    (a record with no spoken text gives a judge nothing to read a sentence against)."""
    return [t for t in valid_bindings(tags, records) if _voiced_text(records[t]).strip()]


def decide(entry: dict, label: str | None, records: dict[str, dict], connectives: frozenset[str]) -> tuple[str, str | None]:
    """The verdict for one net sentence and its label: (decision, reason)."""
    if entry.get("verdict") != "ok":
        return "withhold_net", entry.get("why")
    if placed_by_code(entry):
        return "keep", "placed by code"
    sentence = entry["sentence"]
    if talks_of_tags(sentence):
        return "withhold_tags", None
    if bindings(list(entry.get("tags") or []), records):
        if label == "inference":
            return "withhold_inference", None
        return ("keep", None) if label == "paraphrase" else ("withhold_unlabelled", "no label")
    if _is_question(sentence) or normalize(sentence) in connectives:
        return "keep", "no claim"
    return "withhold_unbound", "no valid binding" if not entry.get("tags") else "tags name no record the world holds"


def items(answer: dict, records: dict[str, dict], connectives: frozenset[str]) -> list[dict]:
    """One item per net sentence of an answer: position, sentence, tags, bindings, label and decision.
    The label is read from the sentence's own draft (the net's `draft` field, set when the net's
    sentences line up with the text it checked); a sentence with no draft has no label."""
    out = []
    for n, entry in enumerate(answer.get("net_sentences", [])):
        label = label_of(entry.get("draft") or "")
        decision, reason = decide(entry, label, records, connectives)
        out.append({
            "n": n, "sentence": entry["sentence"], "tags": list(entry.get("tags") or []), "records": bindings(list(entry.get("tags") or []), records),
            "label": label, "decision": decision, "reason": reason, "placed": placed_by_code(entry),
            "placed_id": entry.get("placed_quote") or entry.get("placed_story") or entry.get("placed_answer"),
        })
    return out
