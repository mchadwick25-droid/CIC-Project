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
    # One per world. The world's own account of the shared vendored corpus
    # (cic/texts/), added 2026-08-26 on Mark's standard: every world should
    # reach every available resource - they may be RANKED, never ignored.
    #
    # Before this, nothing recorded whether a world had considered a volume.
    # A world's source ecology was whatever its build thread happened to
    # reach for, and the only way to ask "did alx consider Basil?" was to
    # infer it backwards from whether alx happened to name him - a proxy that
    # was measured wrong (a bare substring match put Leo the Great on
    # Alexandria's list on the strength of "Leonides", Origen's father).
    # A declination is not a gap. It is the ranking, written down where a
    # reviewer can disagree with it.
    "corpus_review": {
        "declinations": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "file": {"type": "string"},
                    # `deferred` is the honest fourth option and the reason
                    # this enum is not just the three exclusion grounds:
                    # "this is relevant and we have not mined it yet" must be
                    # sayable, and must not read the same as "not relevant".
                    "rank": {"enum": [
                        "out-of-region",
                        "out-of-window",
                        "beyond-doctrinal-floor",
                        "no-relevant-content",
                        # Mark's ruling 2026-08-26: the Atlas is the bucket
                        # set, not the six built worlds. Most material this
                        # fleet does not use is not irrelevant - it belongs to
                        # an Atlas entry nobody has built yet. Basil and the
                        # Gregories are `cappadocian-nicene-pastoral-monastic-
                        # tradition`, which the census already marks Selected -
                        # Not Yet Built; Chrysostom is the Antiochene entry;
                        # Augustine the Latin pastoral one. A ruling that says
                        # WHERE something goes is worth more than one saying it
                        # is not here, and it means world #7 finds its sources
                        # already assembled.
                        "belongs-to-another-atlas-entry",
                        "deferred",
                    ]},
                    # The census movement id this material belongs to, when the
                    # rank is `belongs-to-another-atlas-entry`. The Atlas and
                    # the built worlds are ONE taxonomy - every built world is
                    # itself a census entry - so this creates no second bucket
                    # system to keep in sync.
                    "atlas_id": {"type": "string"},
                    "reason": {"type": "string"},
                },
                "required": ["file", "rank", "reason"],
                "additionalProperties": False,
            },
        },
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
