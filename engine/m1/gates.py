"""The gate battery (Artifact-1 SS6). Each gate is a function
(records, fleet, registry) -> list[str] of human-readable findings; an empty
list means that gate passed clean. Gate names here are the same strings used
as `gate:` ids in fixtures/seeded_defects.yaml, so the selftest can map one
to the other directly with no separate lookup table (law 4, applied to test
wiring too).
"""
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
    cells = canon.valid_cells(fleet)
    substantive = canon.substantive_types()
    for cell in sorted(cells):
        substantive_hits = [
            rid for rid, r in records.items() if r.get("record_type") in substantive and cell in (r.get("canon_cells") or [])
        ]
        honest_limit_hits = [
            rid
            for rid, r in records.items()
            if r.get("record_type") == "honest_limit" and cell in (r.get("canon_cells") or [])
        ]
        if substantive_hits:
            continue
        if len(honest_limit_hits) == 1:
            continue
        if len(honest_limit_hits) > 1:
            findings.append(f"cell {cell}: {len(honest_limit_hits)} honest_limit records claim it - exactly one is allowed")
        else:
            findings.append(f"cell {cell}: neither a substantive record nor an honest_limit - blank cell")
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
}


def run_all(records: dict, fleet: dict, registry: dict) -> dict[str, list[str]]:
    return {name: fn(records, fleet, registry) for name, fn in GATES.items()}
