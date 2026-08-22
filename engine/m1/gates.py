"""The gate battery (Artifact-1 SS6). Each gate is a function
(records, fleet, registry) -> list[str] of human-readable findings; an empty
list means that gate passed clean. Gate names here are the same strings used
as `gate:` ids in fixtures/seeded_defects.yaml, so the selftest can map one
to the other directly with no separate lookup table (law 4, applied to test
wiring too).
"""
import re

from jsonschema import Draft202012Validator

from . import canon
from .fk import fk_grade
from .schemas import RELATION_INVERSE, build_schema

FK_CEILING = 10

COMPLETION_REQUIRED = {
    "world_core": ["time_window", "horizon", "formation_logic", "thinness", "cautions"],
    "source": ["author", "work", "edition", "rights_status", "attribution_status", "discovery_channel"],
    "term": ["plain_meaning", "world_word", "senses", "quick_meaning"],
    "story": ["narrative_tier", "narrative_tier_justification", "tellable_as", "text"],
    "quote": ["text", "speaker_or_author", "license"],
    "figure": ["names", "narratable", "bridge_line"],
    "gravity": ["name", "description"],
    "force": ["name", "description"],
    "contested_claim": ["claim", "held_against", "concedes"],
    "doctrinal_witness": ["text", "positions", "tensions"],
    "honest_limit": ["statement", "why_sources_cannot_answer", "nearest_material"],
    "ambient": ["detail", "formation_claim_barred"],
    "demonstration": ["canon_question_id", "exchange"],
    "voice_craft": ["identity", "flavor_notes", "characteristic_concerns", "guard"],
    "search_record": ["query", "channel", "result"],
    "canon_question": ["cell", "text", "source", "canon_status", "phrasing_rules_checked"],
    "modern_term": ["display_terms", "origin_year", "modern_sense", "underlying_subject"],
    "fleet_voice": ["register_statements", "pronoun_rule", "citation_contract", "limit_discipline"],
}


def _is_blank(value) -> bool:
    return value is None or value == "" or value == [] or value == {}


def gate_schema_validation(records, fleet, registry) -> list[str]:
    findings = []
    for rid, rec in records.items():
        record_type = rec.get("record_type")
        try:
            schema = build_schema(record_type)
        except KeyError as e:
            findings.append(f"{rid}: {e}")
            continue
        payload = {k: v for k, v in rec.items() if k not in ("_path", "_body")}
        validator = Draft202012Validator(schema)
        for error in validator.iter_errors(payload):
            findings.append(f"{rid}: {error.message} (at {'/'.join(str(p) for p in error.path) or '<root>'})")
    return findings


def gate_referential(records, fleet, registry) -> list[str]:
    findings = []
    all_ids = set(records) | set(fleet)
    for rid, rec in records.items():
        for rel in rec.get("relations") or []:
            target = rel.get("target")
            if target not in all_ids:
                findings.append(f"{rid}: relation target {target!r} does not resolve to any record")
        for src in rec.get("sources") or []:
            source_id = src.get("source_id")
            if source_id and source_id not in all_ids:
                findings.append(f"{rid}: sources[].source_id {source_id!r} does not resolve to any record")
        cq_id = rec.get("canon_question_id")
        if cq_id and cq_id not in all_ids:
            findings.append(f"{rid}: canon_question_id {cq_id!r} does not resolve to any record")
        cells = canon.valid_cells(fleet)
        for cell in rec.get("canon_cells") or []:
            if cell not in cells:
                findings.append(f"{rid}: canon_cells entry {cell!r} is not a cell in the canon")
    return findings


def gate_reciprocity(records, fleet, registry) -> list[str]:
    findings = []
    all_records = {**records, **fleet}
    for rid, rec in records.items():
        for rel in rec.get("relations") or []:
            rel_type, target = rel.get("type"), rel.get("target")
            inverse = RELATION_INVERSE.get(rel_type)
            if inverse is None or target not in all_records:
                continue
            target_rels = all_records[target].get("relations") or []
            has_reciprocal = any(
                r.get("type") == inverse and r.get("target") == rid for r in target_rels
            )
            if not has_reciprocal:
                findings.append(
                    f"{rid}: declares {rel_type} -> {target} but {target} does not declare "
                    f"{inverse} -> {rid} back"
                )
    return findings


def gate_completion_per_type(records, fleet, registry) -> list[str]:
    findings = []
    for rid, rec in records.items():
        required = COMPLETION_REQUIRED.get(rec.get("record_type"), [])
        for field in required:
            if field not in rec or _is_blank(rec[field]):
                findings.append(f"{rid}: missing required field {field!r} for record_type {rec.get('record_type')!r}")
    return findings


def gate_narratability(records, fleet, registry) -> list[str]:
    findings = []
    for rid, rec in records.items():
        if rec.get("record_type") != "story":
            continue
        tier = rec.get("narrative_tier")
        if not isinstance(tier, int) or not (1 <= tier <= 4):
            findings.append(f"{rid}: narrative_tier {tier!r} is not an integer in 1..4")
        if _is_blank(rec.get("narrative_tier_justification")):
            findings.append(f"{rid}: narrative_tier_justification is required and must be non-empty")
        if _is_blank(rec.get("tellable_as")):
            findings.append(f"{rid}: tellable_as is required and must be non-empty")
        if _is_blank(rec.get("text")):
            findings.append(f"{rid}: text is required and must be non-empty")
    return findings


def gate_quote_recording(records, fleet, registry) -> list[str]:
    findings = []
    valid_licenses = {"verbatim", "paraphrase-only", "do-not-voice"}
    for rid, rec in records.items():
        if rec.get("record_type") != "quote":
            continue
        license_ = rec.get("license")
        if license_ not in valid_licenses:
            findings.append(f"{rid}: license {license_!r} is not one of {sorted(valid_licenses)}")
        if _is_blank(rec.get("text")) or _is_blank(rec.get("speaker_or_author")):
            findings.append(f"{rid}: quote must record both text and speaker_or_author")
    return findings


def gate_alias_safety(records, fleet, registry) -> list[str]:
    findings = []
    terms = {rid: r for rid, r in records.items() if r.get("record_type") == "term"}
    world_words = {rid: (r.get("world_word") or "").strip().lower() for rid, r in terms.items()}
    for rid, rec in terms.items():
        for alias in rec.get("false_friend") or []:
            alias_norm = alias.strip().lower()
            for other_id, other_word in world_words.items():
                if other_id != rid and other_word and alias_norm == other_word:
                    findings.append(
                        f"{rid}: false_friend {alias!r} exactly matches {other_id}'s world_word with no "
                        f"disambiguating context - unsafe alias collision"
                    )
    return findings


def gate_distribution_health(records, fleet, registry) -> list[str]:
    chunk_feeding = {"term", "story", "ambient", "doctrinal_witness"}
    tiers = [
        rec["retrieval"]["tier"]
        for rec in records.values()
        if rec.get("record_type") in chunk_feeding and rec.get("retrieval", {}).get("tier") is not None
    ]
    if len(tiers) >= 2 and len(set(tiers)) == 1:
        return [f"all {len(tiers)} chunk-feeding records share retrieval.tier={tiers[0]} - degenerate tier distribution"]
    return []


def gate_confidence_crosscheck(records, fleet, registry) -> list[str]:
    """Artifact-1 SS3: divergence_note is REQUIRED (non-null) when
    formation_confidence=Documented and the record's own confidence is not
    verified-direct - the record is claiming settled ground without either
    direct verification or an explanation of the gap."""
    findings = []
    for rid, rec in records.items():
        confidence = rec.get("confidence") or {}
        if confidence.get("formation_confidence") != "Documented":
            continue
        if confidence.get("divergence_note") is not None:
            continue
        if confidence.get("verification_state") != "verified-direct":
            findings.append(
                f"{rid}: formation_confidence=Documented with divergence_note=null requires "
                f"verification_state=verified-direct; got {confidence.get('verification_state')!r}"
            )
    return findings


def gate_rights(records, fleet, registry) -> list[str]:
    findings = []
    for rid, rec in records.items():
        if rec.get("record_type") != "source":
            continue
        if _is_blank(rec.get("rights_status")):
            findings.append(f"{rid}: source has no rights_status - rights gate fails closed")
    return findings


def gate_readability(records, fleet, registry) -> list[str]:
    findings = []
    checks = []
    for rid, rec in records.items():
        if rec.get("record_type") == "term":
            checks.append((rid, "quick_meaning", rec.get("quick_meaning")))
            checks.append((rid, "plain_meaning", rec.get("plain_meaning")))
        if rec.get("record_type") == "honest_limit":
            checks.append((rid, "statement", rec.get("statement")))
    for rid, field, text in checks:
        if not text:
            continue
        grade = fk_grade(text)
        if grade > FK_CEILING:
            findings.append(f"{rid}: {field} scores FK grade {grade:.1f}, above the ceiling of {FK_CEILING}")
    return findings


def gate_canon_coverage(records, fleet, registry) -> list[str]:
    findings = []
    for cell in sorted(canon.valid_cells(fleet)):
        classification = canon.classify_cell(cell, records)
        if classification["status"] == "multiple_honest_limit":
            n = len(classification["honest_limit"])
            findings.append(f"cell {cell}: {n} honest_limit records claim it - exactly one is allowed")
        elif classification["status"] == "empty":
            findings.append(f"cell {cell}: neither a substantive record nor an honest_limit - blank cell")
    return findings


# Admitted 2026-08-21 from engine/m1/gates_experimental.py (own defect-
# catalog entry: fixtures/seeded_defects.yaml id
# no-build-attribution-leaked-ruling; selftest-proven per the file's own
# admission bar). Scoped to exactly the fields engine/m2/builders.py's
# build_prompt() reads - the real field contract for what reaches a live
# model, not a separate guess at it. Deliberately narrower than "every
# string field on these record types": doctrinal_witness.positions/
# tensions, honest_limit.why_sources_cannot_answer, and every field on
# gravity/force/contested_claim/search_record/source are NOT compiled and
# are legitimate places for build-process language to live - scanning
# them would drown real findings in noise. Proven necessary, not assumed:
# checked against alx's real corpus (2026-08-21) and found three more
# "Mark" occurrences beyond the four real leaks this gate exists to catch
# - alx.dw.f3-t-one-church's `tensions` field, alx.limit.f5-t-marriage's
# `why_sources_cannot_answer`, and a figure's trailing body - all
# correctly outside this field map, all legitimate.
_ATTRIBUTION_FIELDS = {
    "voice_craft": ["identity", "guard"],
    "world_core": ["horizon", "formation_logic", "thinness", "cautions"],
    "term": ["plain_meaning", "quick_meaning", "world_word"],
    "doctrinal_witness": ["text"],
    "honest_limit": ["statement"],
    "story": ["tellable_as", "text"],
    "fleet_voice": ["pronoun_rule", "citation_contract", "limit_discipline"],
}

# Each pattern below is justified by one of the 4 real leaks found in the
# 2026-08-21 hand audit (world/alexandria c0a105a), not a generic guess:
#   - _ISO_DATE: alx.core.alexandria.thinness ("Mark's 2026-08-21 ruling
#     accepts this"), alx.voice.craft.identity and .flavor_notes both
#     carried "2026-08-21" next to the attribution. In-world historical
#     prose in this register dates things "c. 150-400 CE" / "325 CE" -
#     never ISO format - so this is a near-zero-false-positive signal on
#     its own, and alone would have caught 3 of the 4 leaks.
#   - _RULED_BY: alx.voice.craft.identity's "(RULED by Mark, 2026-08-21:
#     ...)". Deliberately the exact phrase "ruled by" (passive,
#     agent-attributed), not bare "ruled"/"ruling" - those fired as false
#     positives in the hand audit on real historical content ("the
#     council... ruling on the disputed confession", "his book ruled
#     whole congregations") that has no "by <name>" attribution shape.
#     Not zero-risk itself (a real sentence could read "the villages were
#     ruled by their bishop") - a finding here is still worth a human's
#     eyes before treating it as confirmed, same as any other gate finding
#     in this battery.
#   - _STALE_STATUS: alx.core.alexandria.horizon's "WORKING SCOPE, NOT A
#     RULING: world identity is Mark's touchpoint; this record is draft
#     until that ruling and revises with it" - the one leak with no ISO
#     date in it at all, so it needed its own pattern.
_ISO_DATE = re.compile(r"\b20\d{2}-\d{2}-\d{2}\b")
_RULED_BY = re.compile(r"\bruled by\b", re.IGNORECASE)
_STALE_STATUS = re.compile(r"\bWORKING SCOPE\b|\bNOT A RULING\b", re.IGNORECASE)


def _attribution_hits(text: str) -> list[str]:
    hits = []
    if _ISO_DATE.search(text):
        hits.append("ISO-format date")
    if _RULED_BY.search(text):
        hits.append("'ruled by' attribution")
    if _STALE_STATUS.search(text):
        hits.append("stale working-scope/status marker")
    return hits


def gate_no_build_attribution(records, fleet, registry) -> list[str]:
    """Built from a real defect, not a hypothetical: a 2026-08-21 hand
    audit of every field build_prompt() actually compiles found 4 places
    where build-process attribution (a date, "RULED by Mark", a direct
    quote of the project lead) had leaked into voice_craft.identity and
    world_core.horizon - the compiled Identity and Horizon sections a
    live model reads as its own self-description and historical scope.
    Fixed by hand (world/alexandria c0a105a); this gate is the mechanical
    check that should have caught it at record-commit time instead of
    three commits and a manual full-corpus read later.

    Scoped tightly to _ATTRIBUTION_FIELDS - the exact field contract
    build_prompt() reads (see its own comment for why adjacent fields
    like doctrinal_witness.tensions or a trailing body are deliberately
    excluded, proven necessary against real alx content, not assumed).
    """
    findings = []
    for rid, rec in records.items():
        rt = rec.get("record_type")
        fields = _ATTRIBUTION_FIELDS.get(rt, [])
        for f in fields:
            val = rec.get(f)
            if isinstance(val, str):
                for reason in _attribution_hits(val):
                    findings.append(f"{rid}.{f}: {reason} in compiled content - {val[:150]!r}")
        if rt == "voice_craft":
            for c in rec.get("characteristic_concerns") or []:
                if isinstance(c, str):
                    for reason in _attribution_hits(c):
                        findings.append(f"{rid}.characteristic_concerns[]: {reason} - {c[:150]!r}")
            for n in rec.get("flavor_notes") or []:
                note = n.get("note", "")
                for reason in _attribution_hits(note):
                    findings.append(f"{rid}.flavor_notes[{n.get('segment')}]: {reason} - {note[:150]!r}")
        if rt == "demonstration":
            for t in rec.get("exchange") or []:
                txt = t.get("text", "")
                for reason in _attribution_hits(txt):
                    findings.append(f"{rid}.exchange[{t.get('speaker')}]: {reason} - {txt[:150]!r}")
        if rt == "fleet_voice":
            for s in rec.get("register_statements") or []:
                stmt = s.get("statement", "")
                for reason in _attribution_hits(stmt):
                    findings.append(f"{rid}.register_statements[{s.get('number')}]: {reason} - {stmt[:150]!r}")
    return findings


GATES = {
    "schema-validation": gate_schema_validation,
    "referential": gate_referential,
    "reciprocity": gate_reciprocity,
    "completion-per-type": gate_completion_per_type,
    "narratability": gate_narratability,
    "quote-recording": gate_quote_recording,
    "alias-safety": gate_alias_safety,
    "distribution-health": gate_distribution_health,
    "confidence-crosscheck": gate_confidence_crosscheck,
    "rights": gate_rights,
    "readability": gate_readability,
    "canon-coverage": gate_canon_coverage,
    "no-build-attribution": gate_no_build_attribution,
}


def run_all(records: dict, fleet: dict, registry: dict) -> dict[str, list[str]]:
    return {name: fn(records, fleet, registry) for name, fn in GATES.items()}
