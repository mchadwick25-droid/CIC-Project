"""Per-type JSON-Schema (Artifact-1 SS6): envelope properties merged with
type-specific properties, `additionalProperties: false` (unknown field = hard
error - the same behavior Artifact-1 names as `unevaluatedProperties: false`;
flat merge + additionalProperties is the equivalent for a non-composed
schema, and is the DECIDABLE implementation choice recorded in the stage-1
commit).

Required-ness beyond the envelope floor (id, world_id, record_type,
schema_version) is deliberately NOT enforced here - that split is spec'd
explicitly (Artifact-1 SS3: "requiredness beyond the floor is the
field-completion gate's job, not the schema's"). See gates.py:
completion-per-type.
"""

RELATION_TYPES = [
    "presupposes",
    "presupposed-by",
    "precondition-for",
    "enabled-by",
    "tension-with",
    "illustrated-by",
    "illustrates",
    "associated-with",
]

# type -> its declared inverse; symmetric types map to themselves
RELATION_INVERSE = {
    "presupposes": "presupposed-by",
    "presupposed-by": "presupposes",
    "precondition-for": "enabled-by",
    "enabled-by": "precondition-for",
    "tension-with": "tension-with",
    "illustrated-by": "illustrates",
    "illustrates": "illustrated-by",
    "associated-with": "associated-with",
}

_CONFIDENCE_SCHEMA = {
    "type": "object",
    "properties": {
        "citation_specificity": {"enum": ["A", "B", "C", "D", "E"]},
        "verification_state": {
            "enum": ["verified-direct", "verified-via-authority", "named-not-rechecked", "unverified"]
        },
        "evidentiary_weight": {"enum": ["load-bearing", "corroborating", "illustrative", "contested"]},
        "formation_confidence": {
            "enum": [
                "Documented",
                "Widely Accepted",
                "Dominant Modern Reconstruction",
                "Contested",
                "Inferential-Thin",
            ]
        },
        "divergence_note": {"type": ["string", "null"]},
    },
    "additionalProperties": False,
}

_SOURCE_REF_SCHEMA = {
    "type": "object",
    "properties": {
        "source_id": {"type": "string"},
        "locus": {"type": "string"},
        "license": {"type": "string"},
        # Optional, additive (2026-09-02, Mark's sign-off: "new address field,
        # locus untouched" + "optional/best-effort, existing where possible").
        # The canonical passage address defined this session, form
        # `cic:<file-stem>:<locus>` (see cic/corpus-map/README.md's addressing
        # note and cic/engine/works_registry.py's own parse_address()) - a
        # machine-checkable pointer alongside locus's free-text citation form,
        # not a replacement for it. Format and file-existence are checked by
        # gate_canonical_address (gates.py), not by this schema - the same
        # split source.edition/gate_edition_rights_consistency already uses.
        # Envelope-level, like locus itself: any citable record type can set
        # it, not just quote, though quote is where this was scoped from.
        "address": {"type": "string"},
    },
    "required": ["source_id"],
    "additionalProperties": False,
}

_RETRIEVAL_SCHEMA = {
    "type": "object",
    "properties": {
        "tier": {"enum": [1, 2, 3]},
        # sentinel rule (Artifact-1 SS3): empty array is the typed null - a
        # bare string ("n/a", an em-dash, ...) is rejected by "type": "array"
        # alone, with no separate hand rule needed.
        "retrieve_when": {"type": "array", "items": {"type": "string"}},
        "do_not_retrieve_when": {"type": "array", "items": {"type": "string"}},
    },
    "additionalProperties": False,
}

_RELATION_SCHEMA = {
    "type": "object",
    "properties": {
        "type": {"enum": RELATION_TYPES},
        "target": {"type": "string"},
    },
    "required": ["type", "target"],
    "additionalProperties": False,
}

ENVELOPE_PROPERTIES = {
    "id": {"type": "string"},
    "world_id": {"type": "string"},
    "record_type": {"type": "string"},
    "schema_version": {"type": "integer"},
    "status": {"enum": ["draft", "ready", "frozen"]},
    "register": {"enum": ["emic", "etic", "emic-unavailable"]},
    "canon_cells": {"type": "array", "items": {"type": "string"}},
    "confidence": _CONFIDENCE_SCHEMA,
    "sources": {"type": "array", "items": _SOURCE_REF_SCHEMA},
    "retrieval": _RETRIEVAL_SCHEMA,
    "relations": {"type": "array", "items": _RELATION_SCHEMA},
    # loader-added, never authored, never part of any gate's subject matter
    "_path": {"type": "string"},
    "_body": {"type": "string"},
}

ENVELOPE_REQUIRED = ["id", "world_id", "record_type", "schema_version"]

# Type-specific property definitions (Artifact-1 SS4). gravity/force have no
# normatively specified field shape beyond the shared envelope - the fixture
# world uses a minimal placeholder (name/description/manifestations),
# flagged as such in BUILD-HANDOFF.md; ratifying or replacing it is a stage-1
# decision of its own, recorded separately.
TYPE_PROPERTIES: dict[str, dict] = {
    "world_core": {
        "time_window": {
            "type": "object",
            "properties": {"start": {"type": "integer"}, "end": {"type": "integer"}},
            "additionalProperties": False,
        },
        "horizon": {"type": "string"},
        "formation_logic": {"type": "string"},
        "thinness": {"type": "string"},
        "cautions": {"type": "string"},
        # Optional, additive (2026-08-21, mechanism test): structured index
        # over the same ground `thinness`/`cautions` already state in prose,
        # so a gate can cross-check a claim against a world's own named gaps
        # without parsing free text. Not yet in COMPLETION_REQUIRED - existing
        # world_core records validate unchanged without it.
        "thin_topics": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "keywords": {"type": "array", "items": {"type": "string"}},
                    "note": {"type": "string"},
                },
                "required": ["keywords", "note"],
                "additionalProperties": False,
            },
        },
    },
    "source": {
        "author": {"type": "string"},
        "work": {"type": "string"},
        "edition": {"type": "string"},
        "rights_status": {"type": "string"},
        "attribution_status": {"type": "string"},
        "discovery_channel": {"type": "string"},
        "external_ids": {"type": "object"},
        # Optional, additive (2026-09-02, Mark's sign-off: "optional/best
        # effort and existing where possible"): foreign key into
        # cic/corpus-map/WORKS.yaml's own work_id, cross-checked by
        # cic/engine/works_registry.py's record_work_id_problems(), not by
        # this schema (a typo'd id is still a well-formed string). Not yet
        # in COMPLETION_REQUIRED - existing source records validate
        # unchanged without it, and most will stay unset: WORKS.yaml is
        # itself a seeded, incomplete registry (four entries at the time
        # this field was added), so absence means "not joined yet," not
        # "wrong."
        "work_id": {"type": "string"},
    },
    "term": {
        "plain_meaning": {"type": "string"},
        "world_word": {"type": "string"},
        "false_friend": {"type": "array", "items": {"type": "string"}},
        "senses": {
            "type": "object",
            "properties": {
                "informational": {"type": "string"},
                "evidential": {"type": "string"},
                "personal": {"type": "string"},
                "translational": {"type": "string"},
            },
            "additionalProperties": False,
        },
        "quick_meaning": {"type": "string"},
        # Severity marker for senses.translational's own gap - lets a
        # reviewer or future tooling spot the highest-risk terms without
        # parsing prose (Glossary/Story/Quote Template SS1). Not yet in
        # COMPLETION_REQUIRED; existing term records validate unchanged
        # without it.
        "distortion_risk": {"enum": ["low", "medium", "high"]},
        # The word's OWN older/ordinary sense before this world's
        # community repurposed it - distinct from false_friend (modern
        # concepts projected backward). Optional: many world_words are
        # coinages with no meaningful prior secular sense to record.
        "prior_sense": {"type": "string"},
    },
    "story": {
        "narrative_tier": {"type": "integer"},
        "narrative_tier_justification": {"type": "string"},
        "tellable_as": {"type": "string"},
        "text": {"type": "string"},
        "absent_detail": {"type": "string"},
        # Story's own version of term's senses.translational (Glossary/
        # Story/Quote Template SS2) - not yet in COMPLETION_REQUIRED;
        # existing story records validate unchanged without it.
        "modern_contrast": {"type": "string"},
    },
    "quote": {
        "text": {"type": "string"},
        "speaker_or_author": {"type": "string"},
        "license": {"enum": ["verbatim", "paraphrase-only", "do-not-voice"]},
        # Quote's own version of term's senses.translational (Glossary/
        # Story/Quote Template SS3) - not yet in COMPLETION_REQUIRED;
        # existing quote records validate unchanged without it.
        "modern_lens_note": {"type": "string"},
        # The spoken form (process doc V1.2 line 143: "Quote records author
        # their modern_rendering at birth... never the archaic original;
        # the original stays as the record's text for Level 3"). Every
        # already-admitted world's quote records already carry this field;
        # schema was missing it, failing gate_schema_validation fleet-wide
        # (hal 13, pahc 7, syr 18, ijc 6, alx 1, desert 10 findings, all
        # solely this field, confirmed before this fix). Not yet in
        # COMPLETION_REQUIRED - existing quote records validate unchanged.
        "modern_rendering": {"type": "string"},
    },
    "figure": {
        "names": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {"name": {"type": "string"}, "tag": {"enum": ["in-world", "scholarly"]}},
                "required": ["name", "tag"],
                "additionalProperties": False,
            },
        },
        "dates": {"type": "object"},
        "narratable": {"type": "boolean"},
        "bridge_line": {"type": "string"},
    },
    "gravity": {
        "name": {"type": "string"},
        "description": {"type": "string"},
        "manifestations": {"type": "array", "items": {"type": "string"}},
        # Structured mirror of what every world so far has embedded as
        # free text in `name` (e.g. "[TENSIONAL]", "[PRIMARY - C2]") -
        # format already drifted across worlds (bracket contents mean
        # rationale in one, a cell code in another, a scope qualifier in
        # a third; one world uses a comma where the others use a dash).
        # `gate_tension_coverage`'s own regex still catches every variant
        # via a loose prefix match, so nothing is currently broken - this
        # is a durability fix, not a bug fix. Not yet in
        # COMPLETION_REQUIRED; existing gravity records validate
        # unchanged without it. `name` keeps its bracket for display;
        # this field is what a gate or future tool should actually read.
        "classification": {"enum": ["primary", "supporting", "tensional"]},
    },
    "force": {
        "name": {"type": "string"},
        "kind": {"enum": ["initiating", "ongoing", "ending"]},
        "description": {"type": "string"},
        "manifestations": {"type": "array", "items": {"type": "string"}},
        # Structured mirror of the six-cell forces matrix code every
        # world has also been embedding as free text in `name` (e.g.
        # "[1B - initiating/internal]", "[3A - ending/external; distal
        # terminal]") - same drift risk as gravity.classification above.
        # Not yet in COMPLETION_REQUIRED.
        "matrix_cell": {"enum": ["1A", "1B", "2A", "2B", "3A", "3B"]},
    },
    "contested_claim": {
        "claim": {"type": "string"},
        "held_against": {"type": "array", "items": {"type": "string"}},
        "concedes": {"type": "string"},
        "divergence_partners": {"type": "array", "items": {"type": "string"}},
    },
    "doctrinal_witness": {
        "text": {"type": "string"},
        "positions": {"type": "array", "items": {"type": "string"}},
        "tensions": {"type": "array", "items": {"type": "string"}},
    },
    "honest_limit": {
        "statement": {"type": "string"},
        "why_sources_cannot_answer": {"type": "string"},
        "nearest_material": {"type": "array", "items": {"type": "string"}},
    },
    "ambient": {
        "detail": {"type": "string"},
        "formation_claim_barred": {"const": True},
    },
    "demonstration": {
        "canon_question_id": {"type": "string"},
        "tags": {"type": "array", "items": {"type": "string"}},
        "exchange": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "speaker": {"enum": ["participant", "representative"]},
                    "text": {"type": "string"},
                },
                "required": ["speaker", "text"],
                "additionalProperties": False,
            },
        },
    },
    "voice_craft": {
        "identity": {"type": "string"},
        "flavor_notes": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "segment": {"type": "string"},
                    "tag": {"type": "string"},
                    "note": {"type": "string"},
                },
                "required": ["segment", "note"],
                "additionalProperties": False,
            },
        },
        "characteristic_concerns": {"type": "array", "items": {"type": "string"}},
        "guard": {"type": "string"},
    },
    "search_record": {
        "query": {"type": "string"},
        "channel": {"type": "string"},
        "result": {"enum": ["found", "not_found"]},
        "found_sources": {"type": "array", "items": {"type": "string"}},
        "note": {"type": "string"},
    },
    "canon_question": {
        "cell": {"type": "string"},
        "text": {"type": "string"},
        "source": {"type": "array", "items": {"enum": ["corpus", "ext", "new"]}},
        "canon_status": {"enum": ["seed", "vetted", "retired"]},
        "phrasing_rules_checked": {"type": "boolean"},
        "tags": {"type": "array", "items": {"type": "string"}},
    },
    "modern_term": {
        "display_terms": {"type": "array", "items": {"type": "string"}},
        "origin_year": {"type": "integer"},
        "modern_sense": {"type": "string"},
        "underlying_subject": {"type": "string"},
        "distinguishing_claim": {"type": "string"},
        "native_subject_map": {"type": "object"},
    },
    # A single fleet-owned record (records/_fleet/fleet_voice/), versioned
    # like the canon - the compiler's source for the M4 Live-Generation
    # Design's one fleet preamble segment (§5.2): the seven register
    # statements, the pronoun rule, and the citation contract stated ONCE
    # and compiled into every world's prompt, rather than re-derived or
    # re-stated per world (the per-world voice_craft.flavor_notes
    # "self-reference" entry duplicates the pronoun rule across all six
    # worlds today - this is that rule's one owned home going forward).
    "fleet_voice": {
        "register_statements": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "number": {"type": "integer"},
                    "statement": {"type": "string"},
                },
                "required": ["number", "statement"],
                "additionalProperties": False,
            },
        },
        "pronoun_rule": {"type": "string"},
        "citation_contract": {"type": "string"},
        "limit_discipline": {"type": "string"},
    },
}


def build_schema(record_type: str) -> dict:
    if record_type not in TYPE_PROPERTIES:
        raise KeyError(f"no schema registered for record_type {record_type!r}")
    properties = {**ENVELOPE_PROPERTIES, **TYPE_PROPERTIES[record_type]}
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "type": "object",
        "properties": properties,
        "required": ENVELOPE_REQUIRED,
        "additionalProperties": False,
    }
