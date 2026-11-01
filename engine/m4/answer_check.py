"""The answer check: one read of the whole answer against the records its
sentences are bound to, one rewrite from what survives, and the same read of the
rewrite. If too little survives, or the rewrite fails its read, the answer
abstains in the world's fallback sentence.

Shadow only. No live path calls it and it makes no model call: it builds the
judge's requests, reads the replies, and decides.

The read. One request per answer. The judge sees the question, every bound
record as numbered sentences with the force it carries, and the answer's
sentences in order, each with the ids it is bound to, so a word that refers back
is read in its own place. For each sentence it answers supported or not, and names
the problem. For each quote or story code placed (the record's own words) it
answers whether the passage, read in its source context, answers the question
(`fits`, `partly`, `off_point`). Two checks beyond the judge: a sentence that names a
confidence level above the lowest of its bound records is not supported
(verify_step.apply_confidence_cap); a placement is dropped when its verdict says
so (fit_step.decide).

The rewrite. Only when something failed and enough survives (SURVIVE_MIN_WORDS
words). The voice writes the answer again from the supported sentences only, in
the bound-drafting grammar (record ids and a label on every sentence, a passage
placed by [[quote:id]] or [[story:id]] only where it was kept). Code refuses a
rewrite with a sentence that has no binding, an inference label, a quotation mark,
or a placement that was not kept, or a sentence that states an absence its records do not (the check the live net
runs); a refused rewrite abstains. The accepted rewrite
is read the same way. Any sentence not supported abstains. There is no second rewrite.

An unreadable reply keeps what it was asked about and is counted.
"""
import json
import re

from engine.m4 import absence_rule, bound_draft, fit_step, verify_step
from engine.m4.grounding_net import parse_tagged

SURVIVE_MIN_WORDS = bound_draft.FALLBACK_BELOW_WORDS
_JSON = re.compile(r"\{.*\}", re.DOTALL)
_PLACEMENT = re.compile(r"\[\[\s*(quote|story)\s*:\s*([a-z0-9_.-]+)\s*\]\]", re.IGNORECASE)

CHECK_SYSTEM = (
    "You check an answer a historical Representative gave a visitor. The answer is given as numbered sentences. A sentence "
    "bound to records names them; the records are given as numbered sentences with the force each carries. A sentence marked "
    "PLACED is a quote or story code inserted whole from its record: do not judge its words. A sentence marked JOINING is "
    "a question or a short joining sentence: it is supported if it claims nothing.\n"
    "For each bound sentence decide, by these rules:\n"
    + verify_step.VERIFY_CRITERIA
    + "For each PLACED passage, decide whether it answers the visitor's question in its own source context. "
    + fit_step.FIT_RUBRIC
    + 'Reply with one JSON object only: {"sentences": [{"n": the sentence number, "supported": true or false, '
    '"problem": one of "added_detail", "stronger_force", "dropped_scope", "widened_scope", "unresolved_referent", "other" or null when supported, '
    '"reason": "one short sentence"}], "placed": [{"id": the record id, "fit": "fits" or "partly" or "off_point", '
    '"reason": "one short sentence", "limit_stated": true or false}]}. Give one entry for every bound sentence and every PLACED passage.'
)
REWRITE_SYSTEM = (
    "You write a historical Representative's answer again from the sentences below, which were checked and found supported. "
    "Use only what they say; add nothing, and do not use the sentences marked REMOVED. Keep the voice: \"we\", plain words, "
    "sentences under 25 words, the world's own images. Each sentence is read alone against its records, so name the person or thing in every sentence; "
    "never use he, she, it, they, this, that or such to point back to an earlier sentence. Say what each supported sentence's records say, with the same force and limits.\n"
    "Every sentence ends with each record it rests on written in double square brackets, then [[as:paraphrase]], before the full stop, "
    "for example: We kept the creed first [[lpc.witness.example]] [[lpc.term.example]] [[as:paraphrase]]. No quotation marks. "
    "Where a PLACED passage stands in the kept sentences, write its marker ([[quote:id]] or [[story:id]]) alone in that place; "
    "never write the passage's words. Do not place a passage not listed as kept.\n"
    "Reply with the answer only."
)


def units(items: list[dict]) -> list[dict]:
    """The sentences an answer has after the bound-drafting step: kept ones only, in order."""
    return [i for i in items if i["decision"] == "keep"]


def _kind(unit: dict) -> str:
    if unit.get("placed"):
        return "PLACED"
    return "BOUND" if unit["records"] else "JOINING"


def check_request(question: str, answer_units: list[dict], records: dict[str, dict], placed_packs: dict[str, str]) -> dict:
    """One request for the whole answer. `placed_packs` is, by record id, the
    fit pack of each placed passage (fit_step.fit_pack)."""
    ids = list(dict.fromkeys(r for u in answer_units for r in u["records"]))
    packs = "\n\n".join(verify_step.record_pack(records[r], records) for r in ids) or "(none)"
    lines = []
    for n, u in enumerate(answer_units, start=1):
        kind = _kind(u)
        tag = f"bound to {', '.join(u['records'])}" if kind == "BOUND" else kind + (f" {u['placed_id']}" if kind == "PLACED" and u.get("placed_id") else "")
        lines.append(f"{n}. [{tag}] {u['sentence']}")
    passages = "\n\n".join(f"PLACED {rid}\n{pack}" for rid, pack in placed_packs.items()) or "(none)"
    return {"system": CHECK_SYSTEM, "user": f"QUESTION\n{question}\n\nRECORDS\n\n{packs}\n\nANSWER\n" + "\n".join(lines) + f"\n\nPLACED PASSAGES\n\n{passages}"}


def parse_check(reply: str, answer_units: list[dict], records: dict[str, dict]) -> dict | None:
    """{"sentences": {unit index: judgement or None}, "placed": {record id: judgement or None}}, or None when the
    reply holds no object. A sentence the reply leaves out has no judgement (kept, counted)."""
    found = _JSON.search(reply or "")
    if not found:
        return None
    try:
        data = json.loads(found.group(0))
    except json.JSONDecodeError:
        return None
    sentences: dict[int, dict | None] = {}
    for entry in data.get("sentences") or []:
        n = entry.get("n") if isinstance(entry, dict) else None
        if isinstance(n, int) and 1 <= n <= len(answer_units) and _kind(answer_units[n - 1]) == "BOUND":
            unit = answer_units[n - 1]
            sentences[n - 1] = verify_step.apply_confidence_cap(verify_step.judgement_from(entry), unit["sentence"], unit["records"], records)
    placed: dict[str, dict | None] = {}
    for entry in data.get("placed") or []:
        if isinstance(entry, dict) and isinstance(entry.get("id"), str):
            placed[entry["id"]] = fit_step.judgement_from(entry)
    return {"sentences": sentences, "placed": placed}


def outcome(answer_units: list[dict], parsed: dict, records: dict[str, dict], judge_placements: bool = True) -> dict:
    """What failed: unit indexes the judge found unsupported (with the judgement), placed record ids
    dropped for fit, and the count of bound sentences or placements with no readable judgement. Fit is
    judged once per placed quote or story; the world's own placed answer record is the record's words
    and is not judged. With `judge_placements` false (the read of a rewrite) the fit verdicts of the first
    read stand: a kept placement was judged there and is not asked about again."""
    unsupported, unreadable = {}, 0
    for i, u in enumerate(answer_units):
        if _kind(u) != "BOUND":
            continue
        judgement = parsed["sentences"].get(i)
        if judgement is None:
            unreadable += 1
        elif not judgement["supported"]:
            unsupported[i] = judgement
    dropped = []
    for rid in dict.fromkeys(u["placed_id"] for u in answer_units if judge_placements and u.get("placed") and u.get("placed_id")):
        if (records.get(rid) or {}).get("record_type") not in ("quote", "story"):
            continue
        judgement = parsed["placed"].get(rid)
        if judgement is None:
            unreadable += 1
        elif fit_step.decide(judgement) == "drop":
            dropped.append(rid)
    return {"unsupported": unsupported, "dropped": dropped, "unreadable": unreadable}


def survivors(answer_units: list[dict], result: dict) -> list[dict]:
    """The units that stay: not unsupported, not a dropped placement, and not the lead-in of a
    dropped placement (a sentence bound to that record, standing just before it)."""
    out = []
    for i, u in enumerate(answer_units):
        following = answer_units[i + 1] if i + 1 < len(answer_units) else {}
        lead_in = bool(u["records"]) and not u.get("placed") and following.get("placed_id") in result["dropped"] and following.get("placed_id") in u["records"]
        if i not in result["unsupported"] and u.get("placed_id") not in result["dropped"] and not lead_in:
            out.append(u)
    return out


def words(answer_units: list[dict]) -> int:
    return sum(len(u["sentence"].split()) for u in answer_units)


def rewrite_request(question: str, answer_units: list[dict], result: dict, records: dict[str, dict]) -> dict:
    kept = survivors(answer_units, result)
    ids = list(dict.fromkeys(r for u in kept for r in u["records"]))
    packs = "\n\n".join(verify_step.record_pack(records[r], records) for r in ids) or "(none)"
    lines = []
    for u in answer_units:
        if u in kept:
            tag = "PLACED " + u["placed_id"] if u.get("placed") and u.get("placed_id") else ("bound to " + " ".join(f"[[{r}]]" for r in u["records"]) if u["records"] else "JOINING")
            lines.append(f"KEPT [{tag}] {u['sentence']}")
        else:
            lines.append(f"REMOVED {u['sentence']}")
    return {"system": REWRITE_SYSTEM, "user": f"QUESTION\n{question}\n\nRECORDS\n\n{packs}\n\nSENTENCES IN ORDER\n" + "\n".join(lines)}


def parse_rewrite(reply: str, kept: list[dict], records: dict[str, dict], connectives: frozenset[str]) -> list[dict] | None:
    """The rewrite as units, or None when it is refused: empty, a quotation mark, a sentence with no binding
    (that is not a question or a reviewed connective), an inference label, a missing label, a sentence that states an
    absence its records do not, or a placement that was not kept. A kept placement is inserted whole: every unit it had."""
    text = (reply or "").strip()
    if not text or verify_step._has_quotation_mark(_PLACEMENT.sub("", text)):
        return None
    allowed = {u["placed_id"] for u in kept if u.get("placed") and u.get("placed_id")}
    out = []
    pieces = _PLACEMENT.split(text)
    for index in range(0, len(pieces), 3):
        for sentence in parse_tagged(pieces[index]) if pieces[index].strip() else []:
            entry = {"sentence": sentence["text"], "tags": sentence["tags"], "verdict": "ok"}
            decision, _reason = bound_draft.decide(entry, bound_draft.label_of(sentence["raw"]), records, connectives)
            if decision != "keep" or absence_rule.check_absence(sentence["text"], [records[t] for t in sentence["tags"] if t in records]):
                return None
            out.append({"sentence": sentence["text"], "tags": sentence["tags"], "records": bound_draft.bindings(sentence["tags"], records), "placed": False, "placed_id": None})
        if index + 2 < len(pieces):
            if pieces[index + 2] not in allowed:
                return None
            out.extend({**u} for u in kept if u.get("placed_id") == pieces[index + 2])
    return out or None


def assemble(answer_units: list[dict]) -> str:
    return " ".join(u["sentence"] for u in answer_units)
