"""Two candidate mechanisms for a class of bug the accepted M1 battery
cannot see: a record whose citations are real, well-formed, and rights-clean,
but whose prose says more than those citations actually support. Found live
in alx.demo.f6-p-someone-like-me (2026-08-21) - it cited two real records,
neither of which documents the specific claim it made, while the world's own
world_core named the exact gap in its `cautions` field the whole time.

NOT yet in gates.GATES / the accepted battery. These are under test (Mark,
2026-08-21: "yes lets test 2 and 3") - findings here are candidates for human
review, not a pass/fail verdict, until proven against real content and
formally admitted the way every other gate was (its own defect-catalog entry
+ selftest proof).

Mechanism 2 - caution-crosscheck: a world_core can name its own known-thin
topics (thin_topics, schemas.py) alongside its existing prose thinness/
cautions fields. A HIGH-confidence, emic-register record whose text hits one
of those topics' keywords, with no divergence_note justifying the confidence
anyway, is flagged. Cheap, mechanical, and catches exactly the case where a
world already knew about its own gap and a later record ignored it. It does
NOT catch a gap nobody has named yet.

Mechanism 3 - unsupported-claim (lexical overlap): a blunt heuristic, in the
same spirit as fk.py's syllable-counting readability check - "good enough to
flag obviously ungrounded prose, not lexicographic precision." For each
content sentence in a demonstration/doctrinal_witness/story's spoken text,
checks whether it shares ANY stopword-filtered content word with the text of
its own cited internal records (sources[].source_id that resolve to another
world record, not a raw `source` metadata stub, which carries no body text
to check against). Zero overlap is flagged as a candidate unsupported claim.
Expected to have real false positives - a sentence can be a legitimate
synthesizing gloss in the voice's own words rather than an invented factual
claim, and this heuristic cannot tell the two apart. Reported as a flag for
human review, not a hard fail.
"""
import re

_NON_PROSE_KEYS = {
    "id", "world_id", "record_type", "schema_version", "status", "register",
    "_path", "_body", "world_word", "license", "narrative_tier",
    "formation_claim_barred", "citation_specificity", "verification_state",
    "evidentiary_weight", "formation_confidence",
}

_STOPWORDS = {
    "the", "a", "an", "and", "or", "but", "of", "to", "in", "on", "at", "by",
    "for", "with", "as", "is", "was", "were", "are", "be", "been", "being",
    "it", "its", "this", "that", "these", "those", "we", "us", "our", "ours",
    "you", "your", "yours", "they", "them", "their", "he", "him", "his",
    "she", "her", "hers", "i", "me", "my", "mine", "not", "no", "so", "if",
    "than", "then", "too", "also", "one", "did", "do", "does", "had", "has",
    "have", "what", "who", "when", "where", "why", "how", "all", "any",
    "some", "into", "out", "up", "down", "over", "under", "here", "there",
    "can", "could", "would", "should", "will", "shall", "must", "let", "yet",
    "even", "still", "just", "only", "own", "back", "before", "after",
    "because", "about", "against", "between", "from", "each", "other",
}

_SCAFFOLD_MARKERS = (
    "i must be honest", "i will not invent", "i will not pretend",
    "i will not put words", "i cannot", "i will not", "i am not your judge",
    "it is not my place", "it is not my role", "i do not have",
    "i must be careful", "i will not draw one", "i will not sell you",
    "i find none of these", "i owe you honesty", "i must leave",
)

_WORD = re.compile(r"[a-zA-Z']+")
_SENTENCE_SPLIT = re.compile(r"(?<=[.!?])\s+")


def _all_text(rec: dict) -> str:
    """Every string value in a record, recursively, minus purely structural
    fields - a deliberately generic extractor so this works across all
    record types without a per-type text-field map."""
    parts = []

    def walk(value, key=None):
        if isinstance(value, str):
            if key not in _NON_PROSE_KEYS:
                parts.append(value)
        elif isinstance(value, dict):
            for k, v in value.items():
                walk(v, k)
        elif isinstance(value, list):
            for item in value:
                walk(item, key)

    walk(rec)
    return " ".join(parts)


def _content_words(text: str) -> set[str]:
    words = (w.lower() for w in _WORD.findall(text))
    return {w for w in words if w not in _STOPWORDS and len(w) > 2}


def _sentences(text: str) -> list[str]:
    return [s.strip() for s in _SENTENCE_SPLIT.split(text or "") if s.strip()]


# Language that shows a record is already NAMING a gap honestly in its own
# prose, rather than narrating past it - a hit here means the record IS the
# correct handling of a thin_topic, not a violation of it. Distinct from
# gate 3's _SCAFFOLD_MARKERS (that list catches vocational-honesty framing;
# this one catches the actual admission-of-absence phrasing).
_HEDGE_MARKERS = (
    "i must be honest", "i will not invent", "i will not put words",
    "i do not have", "i cannot show you", "not preserved", "not recoverable",
    "no female-authored", "our record does not", "does not give me",
    "does not give us", "not kept", "almost nothing", "i will not pretend",
    "and i will not invent one",
)


def gate_caution_crosscheck(records, fleet, registry) -> list[str]:
    findings = []
    world_cores = {r["world_id"]: r for r in records.values() if r.get("record_type") == "world_core"}
    high_confidence = {"Documented", "Widely Accepted"}
    for rid, rec in records.items():
        if rec.get("record_type") == "world_core":
            continue
        if rec.get("register") != "emic":
            continue
        confidence = rec.get("confidence") or {}
        if confidence.get("formation_confidence") not in high_confidence:
            continue
        if confidence.get("divergence_note"):
            continue
        core = world_cores.get(rec.get("world_id"))
        if not core:
            continue
        full_text = _all_text(rec)
        text_lower = full_text.lower()
        if any(marker in text_lower for marker in _HEDGE_MARKERS):
            continue  # already names the gap honestly in its own prose - not a violation
        if rec.get("record_type") == "honest_limit" or "honest-limit" in (rec.get("tags") or []):
            continue  # this record's entire job is to state a limit - trust its own field discipline
        all_hits = []
        hit_notes = []
        for topic in core.get("thin_topics") or []:
            hits = [kw for kw in (topic.get("keywords") or []) if kw.lower() in text_lower]
            if hits:
                all_hits.extend(hits)
                hit_notes.append(topic.get("note"))
        # a single bare keyword mention (a name in passing, one incidental
        # word) is too weak a signal on its own - "widow" inside a martyrdom
        # story about someone's WIFE, or "Didymus" naming him as a teacher,
        # both hit on a single keyword with no real claim about the thin
        # topic itself. Requiring >= 2 hits is a density proxy for "this
        # record is actually asserting something in the gap area," not just
        # touching it in passing. Tuned against one known case so far -
        # needs testing against more before trusting the threshold generally.
        if len(all_hits) >= 2:
            findings.append(
                f"{rid}: formation_confidence={confidence.get('formation_confidence')!r} with no "
                f"divergence_note or in-text hedge, but text hits {len(all_hits)} thin_topic keywords "
                f"{all_hits} across {core['id']}'s named gaps ({'; '.join(hit_notes)})"
            )
    return findings


def gate_unsupported_claim(records, fleet, registry) -> list[str]:
    findings = []
    checked_types = {"demonstration", "doctrinal_witness", "story"}
    for rid, rec in records.items():
        if rec.get("record_type") not in checked_types or rec.get("register") != "emic":
            continue

        cited_words: set[str] = set()
        has_checkable_source = False
        for src in rec.get("sources") or []:
            cited = records.get(src.get("source_id")) or fleet.get(src.get("source_id"))
            if not cited or cited.get("record_type") == "source":
                continue  # raw source metadata carries no body text to check against
            has_checkable_source = True
            cited_words |= _content_words(_all_text(cited))
        if not has_checkable_source:
            continue  # nothing to check against - not this gate's job

        if rec.get("record_type") == "demonstration":
            own_text = " ".join(
                t.get("text", "") for t in rec.get("exchange") or [] if t.get("speaker") == "representative"
            )
        else:
            own_text = rec.get("text") or rec.get("statement") or ""

        for sentence in _sentences(own_text):
            words = _content_words(sentence)
            if len(words) < 6:
                continue
            if any(marker in sentence.lower() for marker in _SCAFFOLD_MARKERS):
                continue
            if not (words & cited_words):
                findings.append(
                    f"{rid}: zero lexical overlap with any cited internal source's own text - "
                    f"candidate unsupported claim: {sentence!r}"
                )
    return findings


EXPERIMENTAL_GATES = {
    "caution-crosscheck": gate_caution_crosscheck,
    "unsupported-claim": gate_unsupported_claim,
}


def run_experimental(records: dict, fleet: dict, registry: dict) -> dict[str, list[str]]:
    return {name: fn(records, fleet, registry) for name, fn in EXPERIMENTAL_GATES.items()}
