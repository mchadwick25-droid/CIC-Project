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
    },
    "story": {
        "narrative_tier": {"type": "integer"},
        "narrative_tier_justification": {"type": "string"},
        "tellable_as": {"type": "string"},
        "text": {"type": "string"},
        "absent_detail": {"type": "string"},
    },
    "quote": {
        "text": {"type": "string"},
        "speaker_or_author": {"type": "string"},
        "license": {"enum": ["verbatim", "paraphrase-only", "do-not-voice"]},
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
    },
    "force": {
        "name": {"type": "string"},
        "kind": {"enum": ["initiating", "ongoing", "ending"]},
        "description": {"type": "string"},
        "manifestations": {"type": "array", "items": {"type": "string"}},
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
