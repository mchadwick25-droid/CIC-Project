"""Two experimental M1 gates, and two superseded ancestors.

Origin (2026-08-21): a record whose citations were real, well-formed and
rights-clean, but whose prose said more than those citations supported -
found live in alx.demo.someone-like-me, which cited two real records,
neither of which documented the specific claim it made, while the world's
own world_core named the exact gap in its `cautions` field the whole time.

STATUS, UNCHANGED SINCE: not in gates.GATES, not in the accepted battery,
and - as of this writing - not invoked by anything at all. run_experimental
has no caller: not CI, not the compiler, not M1's own battery, not a test.
Findings here are candidates for human review, not a pass/fail verdict,
until proven against real content and formally admitted the way every
other gate was (its own defect-catalog entry + selftest proof).

gate_caution_crosscheck_v1 and gate_unsupported_claim_v1 are kept below as
superseded ancestors; neither is in EXPERIMENTAL_GATES. v1 caution-
crosscheck matched bare keywords against a record's WHOLE text; v1
unsupported-claim fired on framing rather than on claims.

The shared prose primitives this file used to define moved to
engine/prose.py, where four production modules could stop importing them
by their private names from a file marked experimental. What is left here
is only what the file's name has always claimed.
"""
import json
import re
from pathlib import Path

from engine.prose import (
    SCAFFOLD_MARKERS,
    SELF_NAMING_MARKER,
    WITHHOLD_FLOOR,
    all_text,
    claim_markers,
    content_words,
    grounding_ratio,
    sentences,
)


# Language that shows a record is already NAMING a gap honestly in its own
# prose, rather than narrating past it - a hit here means the record IS the
# correct handling of a thin_topic, not a violation of it. Distinct from
# gate 3's SCAFFOLD_MARKERS (that list catches vocational-honesty framing;
# this one catches the actual admission-of-absence phrasing).
_HEDGE_MARKERS = (
    "i must be honest", "i will not invent", "i will not put words",
    "i do not have", "i cannot show you", "not preserved", "not recoverable",
    "no female-authored", "our record does not", "does not give me",
    "does not give us", "not kept", "almost nothing", "i will not pretend",
    "and i will not invent one",
)


def gate_caution_crosscheck_v1(records, fleet, registry) -> list[str]:
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
        full_text = all_text(rec)
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


def gate_unsupported_claim_v1(records, fleet, registry) -> list[str]:
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
            cited_words |= content_words(all_text(cited))
        if not has_checkable_source:
            continue  # nothing to check against - not this gate's job

        if rec.get("record_type") == "demonstration":
            own_text = " ".join(
                t.get("text", "") for t in rec.get("exchange") or [] if t.get("speaker") == "representative"
            )
        else:
            own_text = rec.get("text") or rec.get("statement") or ""

        for sentence in sentences(own_text):
            words = content_words(sentence)
            if len(words) < 6:
                continue
            if any(marker in sentence.lower() for marker in SCAFFOLD_MARKERS):
                continue
            if not (words & cited_words):
                findings.append(
                    f"{rid}: zero lexical overlap with any cited internal source's own text - "
                    f"candidate unsupported claim: {sentence!r}"
                )
    return findings


# v1 gates end here (kept for the record of what was tried and why it fell
# short - not registered below). v2 starts here.

# "one" deliberately excluded - overwhelmingly used as a pronoun/article
# ("the one asking", "one thing") rather than a quantity, which made it the
# single largest false-positive source in testing.


def gate_grounded_claim(records, fleet, registry) -> list[str]:
    findings = []
    world_cores = {r["world_id"]: r for r in records.values() if r.get("record_type") == "world_core"}
    checked_types = {"demonstration", "doctrinal_witness", "story"}

    for rid, rec in records.items():
        if rec.get("record_type") not in checked_types or rec.get("register") != "emic":
            continue
        if rec.get("record_type") == "honest_limit" or "honest-limit" in (rec.get("tags") or []):
            continue

        cited_words: set[str] = set()
        has_checkable_source = False
        for src in rec.get("sources") or []:
            cited = records.get(src.get("source_id")) or fleet.get(src.get("source_id"))
            if not cited or cited.get("record_type") == "source":
                continue  # raw source metadata carries no body text to check against
            has_checkable_source = True
            cited_words |= content_words(all_text(cited))
        if not has_checkable_source:
            continue  # nothing to check against - not this gate's job

        if rec.get("record_type") == "demonstration":
            own_text = " ".join(
                t.get("text", "") for t in rec.get("exchange") or [] if t.get("speaker") == "representative"
            )
        else:
            own_text = rec.get("text") or rec.get("statement") or ""

        core = world_cores.get(rec.get("world_id"))

        for sentence in sentences(own_text):
            sentence_lower = sentence.lower()
            if any(marker in sentence_lower for marker in SCAFFOLD_MARKERS):
                continue
            if SELF_NAMING_MARKER in sentence_lower:
                continue  # self-naming, not a claim about the world - nothing to ground
            markers = claim_markers(sentence)
            if not markers:
                continue  # no checkable claim in this sentence - interpretive framing, not this gate's job

            ratio = grounding_ratio(sentence, cited_words)
            if ratio >= WITHHOLD_FLOOR:
                continue  # grounded enough in its own cited sources

            thin_hits = []
            if core:
                text_lower = sentence.lower()
                for topic in core.get("thin_topics") or []:
                    hits = [kw for kw in (topic.get("keywords") or []) if kw.lower() in text_lower]
                    if hits:
                        thin_hits.append(f"{hits} ({topic.get('note')})")

            severity = "HIGH" if thin_hits else "MEDIUM"
            escalator = f"; falls inside a named thin topic: {'; '.join(thin_hits)}" if thin_hits else ""
            findings.append(
                f"[{severity}] {rid}: specific claim ({', '.join(markers)}), only {ratio:.0%} of its own "
                f"content grounded in cited sources{escalator} - {sentence!r}"
            )
    return findings


_TENSIONAL_MARKER = re.compile(r"\[\s*tensional\b", re.IGNORECASE)


def gate_tension_coverage(records, fleet, registry) -> list[str]:
    """Informational, not a hard fail - see the module docstring's newest
    entry below for why. Flags a `gravity` record whose `name` field
    declares it [TENSIONAL] but whose `relations` carry no `tension-with`
    entry to any other record.

    Checked directly against Doc_04_Gravity_Discovery.md (alx, 2026-08-21):
    of Alexandria's four Tensional gravities, three (learning-community,
    speculative-doctrinal, martyrdom-contemplative) have a `tension-with`
    relation that traces to a genuine competing/reshaping ("C"/"X") entry
    in Doc_04's own §6 Interaction Matrix. The fourth,
    teacher-bishop-tension, has no such entry - its only matrix listing is
    "T1 <-> C5 (R)", reinforcing, already correctly recorded as
    `associated-with`, not `tension-with`. Its two named poles
    (teacher-authority, bishop-office) were never mapped onto an opposing
    gravity/force record by Doc_04's own reviewed methodology - not a
    recording error, a real asymmetry in how that document treated its
    four Tensionals.

    So a hard-fail version of this check would have forced a fabricated
    `tension-with` target onto teacher-bishop-tension the first time it
    ran - exactly the kind of invented relation this project's no-
    fabrication discipline forbids. This gate reports the same shape of
    gap instead of blocking on it, so a human (the Doc_04 reviewer, not
    the gate) decides whether a given zero-tension-with Tensional is a
    genuine asymmetry like T1 or an actual omission worth fixing.
    """
    findings = []
    for rid, rec in records.items():
        if rec.get("record_type") != "gravity":
            continue
        name = rec.get("name") or ""
        if not _TENSIONAL_MARKER.search(name):
            continue
        relations = rec.get("relations") or []
        if any(r.get("type") == "tension-with" for r in relations):
            continue
        findings.append(
            f"[INFO] {rid}: named {name!r} but carries no tension-with relation - "
            f"confirm against this world's Doc_04 Interaction Matrix whether this "
            f"Tensional's poles were ever mapped onto an opposing record (a real "
            f"asymmetry, as with alx's own teacher-bishop-tension) or whether one "
            f"was missed"
        )
    return findings


# Exactly the fields engine/m2/builders.py's build_prompt() reads - the
# real, current field contract for what reaches a live model, not a
# separate guess at it. Deliberately narrower than "every string field on
# these record types": doctrinal_witness.positions/tensions,
# honest_limit.why_sources_cannot_answer, and every field on gravity/
# force/contested_claim/search_record/source are NOT compiled and are
# legitimate places for build-process language to live - scanning them
# gate_no_build_attribution ADMITTED 2026-08-21 to engine/m1/gates.py's
# GATES battery (own defect-catalog entry in fixtures/seeded_defects.yaml,
# selftest-proven per this file's own admission bar, stated below). No
# longer here - see gates.py for the implementation and its full history
# comment.


# Exactly the fields engine/m2/builders.py's build_prompt() reads - the
# real, current field contract for what reaches a live model, not a
# separate guess at it. Deliberately narrower than "every string field on
# these record types": doctrinal_witness.positions/tensions,
# honest_limit.why_sources_cannot_answer, and every field on gravity/
# force/contested_claim/search_record/source are NOT compiled and are
# legitimate places for build-process language to live - scanning them
# gate_no_build_attribution ADMITTED 2026-08-21 to engine/m1/gates.py's
# GATES battery (own defect-catalog entry in fixtures/seeded_defects.yaml,
# selftest-proven per this file's own admission bar, stated below). No
# longer here - see gates.py for the implementation and its full history
# comment.

EXPERIMENTAL_GATES = {
    "grounded-claim": gate_grounded_claim,
    "tension-coverage": gate_tension_coverage,
}


def run_experimental(records: dict, fleet: dict, registry: dict) -> dict[str, list[str]]:
    return {name: fn(records, fleet, registry) for name, fn in EXPERIMENTAL_GATES.items()}
