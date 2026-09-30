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
        # Optional, additive: a new address field,
        # locus untouched, optional/best-effort, existing where possible.
        # The canonical passage address, form
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
        # The redirect half of do_not_retrieve_when's own split - "ask
        # about X instead, retrieve that record" - accounts for 701 of the
        # field's 714 fleet-wide lines, not an honesty guard. Same shape
        # as the field it's split from; demotes a candidate in ranking,
        # never excludes it.
        "prefer_instead": {"type": "array", "items": {"type": "string"}},
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

# world_front (and facilitator_brief) rendering units - the website compiler
# stage's own three-mode content shape, added alongside those two record
# types (Website-V2 world_front design, approved to proceed).
# Every unit of authored, participant-facing prose in either type is one of:
#
#   mode 1 - {text, grounded_in}         a fresh authored sentence/paragraph,
#                                         grounded in one or more existing
#                                         records (a claim the record set
#                                         supports, not copied from any one
#                                         of them verbatim).
#   mode 2 - a bare record id (string)   the record's OWN field rendered
#                                         verbatim at compile time - e.g.
#                                         narrative.quiet names an
#                                         honest_limit record and the
#                                         compiler pulls its `statement`
#                                         field unchanged; narrative.
#                                         pull_quotes/glossary are lists of
#                                         such ids. No unit object at all:
#                                         the schema for these fields is
#                                         just {"type": "string"} (or an
#                                         array of them).
#   mode 3 - {from, text, no_new_claims: true}
#                                         a record's own wording ADAPTED
#                                         under length/space constraints -
#                                         `text` must say only what `from`'s
#                                         own field already says, never more
#                                         or less (checked by
#                                         gates.check_mode3_claim_fidelity,
#                                         an LLM-judged gate - see there).
#
# `register` is deliberately NOT a field on any of these unit shapes.
# Per-unit register was tried and rejected in design review as
# incompatible with this schema system's own additionalProperties:false/
# flat-merge architecture (this file's own header comment) - register
# stays exactly where every other record's register already lives: once,
# on the envelope (ENVELOPE_PROPERTIES below), for the whole world_front
# record. A unit that needs a register of its own doesn't get one here.
_MODE1_UNIT = {
    "type": "object",
    "properties": {
        "text": {"type": "string"},
        "grounded_in": {"type": "array", "items": {"type": "string"}, "minItems": 1},
    },
    "required": ["text", "grounded_in"],
    "additionalProperties": False,
}

_MODE3_UNIT = {
    "type": "object",
    "properties": {
        "from": {"type": "string"},
        "text": {"type": "string"},
        "no_new_claims": {"const": True},
    },
    "required": ["from", "text", "no_new_claims"],
    "additionalProperties": False,
}

# The ordinary unit: mode 1 or mode 3, nothing else. Used everywhere in
# world_front/facilitator_brief that the design calls "a mode 1 unit" with
# no extra fields of its own (skim.tile, orientation.story entries,
# orientation.floor_note, orientation.legacy entries, orientation.
# relations_summary, orientation.sourcing, and every facilitator_brief
# prose field).
_UNIT = {"anyOf": [_MODE1_UNIT, _MODE3_UNIT]}

# orientation.voices: a unit plus two fields the design gives it specifically
# (figure - optional, since a voice need not be tied to one named figure -
# and hedge, the world's own emic way of naming its uncertainty). Built as
# its own mode1/mode3 pair rather than bolting extra properties onto _UNIT,
# since additionalProperties:false means _UNIT itself cannot carry them.
_VOICE_MODE1 = {
    "type": "object",
    "properties": {
        "figure": {"type": "string"},
        "text": {"type": "string"},
        "grounded_in": {"type": "array", "items": {"type": "string"}, "minItems": 1},
        "hedge": {"type": "string"},
    },
    "required": ["text", "grounded_in"],
    "additionalProperties": False,
}
_VOICE_MODE3 = {
    "type": "object",
    "properties": {
        "figure": {"type": "string"},
        "from": {"type": "string"},
        "text": {"type": "string"},
        "no_new_claims": {"const": True},
        "hedge": {"type": "string"},
    },
    "required": ["from", "text", "no_new_claims"],
    "additionalProperties": False,
}
_VOICE_UNIT = {"anyOf": [_VOICE_MODE1, _VOICE_MODE3]}

# orientation.experience_today: a live claim about the present, not about
# the completed world - so beyond the ordinary unit shape it carries a url
# and a REQUIRED verified_on (the design's own words: "required, since this
# is a live claim about the present that can go stale"), in both modes.
_EXPERIENCE_MODE1 = {
    "type": "object",
    "properties": {
        "text": {"type": "string"},
        "url": {"type": "string"},
        "grounded_in": {"type": "array", "items": {"type": "string"}, "minItems": 1},
        "verified_on": {"type": "string"},
    },
    "required": ["text", "url", "grounded_in", "verified_on"],
    "additionalProperties": False,
}
_EXPERIENCE_MODE3 = {
    "type": "object",
    "properties": {
        "from": {"type": "string"},
        "text": {"type": "string"},
        "no_new_claims": {"const": True},
        "url": {"type": "string"},
        "verified_on": {"type": "string"},
    },
    "required": ["from", "text", "no_new_claims", "url", "verified_on"],
    "additionalProperties": False,
}
_EXPERIENCE_TODAY_ENTRY = {"anyOf": [_EXPERIENCE_MODE1, _EXPERIENCE_MODE3]}

# The remaining world_front sub-shapes are plain structured objects, not
# renderable units - each field on them is either a bare record id (mode 2)
# or free descriptive prose the compiler never has to check for claim
# drift, so none of them need the mode1/mode3 anyOf treatment above.
_DOCUMENTED_STORY_ENTRY = {
    "type": "object",
    "properties": {
        "story_id": {"type": "string"},
        "title": {"type": "string"},
        "when": {"type": "string"},
        "teaser": {"type": "string"},
        "grounded_in": {"type": "array", "items": {"type": "string"}, "minItems": 1},
    },
    "required": ["story_id", "title", "when", "teaser", "grounded_in"],
    "additionalProperties": False,
}

_READ_FIRST_ENTRY = {
    "type": "object",
    "properties": {
        "source": {"type": "string"},
        "note": {"type": "string"},
    },
    "required": ["source", "note"],
    "additionalProperties": False,
}

_WHO_SPEAKS_SCHEMA = {
    "type": "object",
    "properties": {
        "text": {"type": "string"},
        "figures": {"type": "array", "items": {"type": "string"}},
    },
    "required": ["text", "figures"],
    "additionalProperties": False,
}

_QUESTION_ENTRY = {
    "type": "object",
    "properties": {
        "cell": {"type": "string"},
        "demonstration": {"type": "string"},
        "cite": {"type": "array", "items": {"type": "string"}},
    },
    "required": ["cell", "demonstration", "cite"],
    "additionalProperties": False,
}

# export.include_types: the record types a world_front's compiled export may
# draw exhibits/citations from - deliberately never world_front or
# facilitator_brief themselves (a world_front cannot cite another
# world_front, and a facilitator_brief is never exported to a participant
# surface at all - see gates.py/builders.py for the actual enforcement).
_EXPORT_INCLUDE_TYPES = [
    "story", "quote", "figure", "term", "contested_claim",
    "honest_limit", "doctrinal_witness", "gravity", "force", "source",
]

ENVELOPE_PROPERTIES = {
    "id": {"type": "string"},
    "world_id": {"type": "string"},
    "record_type": {"type": "string"},
    "schema_version": {"type": "integer"},
    "status": {"enum": ["draft", "ready", "frozen"]},
    "register": {"enum": ["emic", "etic", "emic-unavailable"]},
    "canon_cells": {"type": "array", "items": {"type": "string"}},
    # Authored opt-out from M2's demo auto-tagging (engine/m2/builders.py's
    # _demonstration_candidates()): a
    # record whose own framing vocabulary ("we cannot tell you", "plainly")
    # false-tags unrelated demo sentences at the shipping floor sets
    # `demo_tag: exclude` rather than being silently mistagged. Real,
    # load-bearing field (5 honest_limit records use it fleet-wide)
    # that was simply missing from this schema until now -
    # every record carrying it was failing gate_schema_validation, the
    # same shape of gap quote.modern_rendering was in before it. Spans
    # every type builders.py's own _DEMO_CANDIDATE_TYPES lists (not just
    # honest_limit), so it lives on the envelope, like canon_cells itself.
    # "exclude" is the only value the compiler checks for; anything else
    # would silently do nothing, which is exactly the class of typo an
    # enum (rather than a bare string) catches at the schema layer.
    "demo_tag": {"enum": ["exclude"]},
    "confidence": _CONFIDENCE_SCHEMA,
    "sources": {"type": "array", "items": _SOURCE_REF_SCHEMA},
    "retrieval": _RETRIEVAL_SCHEMA,
    # The honesty-guard half of do_not_retrieve_when's own split - a
    # barred proposition the voice must never assert (13 of 714
    # fleet-wide lines), structurally separate from ordinary
    # retrieval-scoping notes (retrieval.prefer_instead, above).
    # Envelope-level like
    # `retrieval` itself: any record type can carry a claim it must not
    # make, not just the ones with a `retrieval` block already in use.
    "claim_guards": {"type": "array", "items": {"type": "string"}},
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
        # Optional, additive: whether and how this world's formation
        # corresponds to a living tradition still practiced today
        # (Constitution Article 29) - spoken in the same first-person
        # register as horizon/formation_logic/thinness/cautions above, and
        # compiled into build_prompt() the same way (see that function's own
        # comment). Root-caused and added per Open_Gaps_Tracking.md OG-45/
        # OG-48: witt's own world_core record authored this content honestly
        # in its body, disclosing at authoring time that no such field
        # existed yet ("pending a future schema change-order... the same way
        # thin_topics was added structurally after thinness/cautions already
        # existed in prose") - so the M2 compiler had no code path to read
        # it, and a project-lead-confirmed Article 29 determination never
        # reached the deployed prompt. Left unset, a world_core record has
        # nothing to say here (most do not yet have a confirmed Article 29
        # determination at all). Not yet in COMPLETION_REQUIRED - existing
        # world_core records validate unchanged without it.
        "living_traditions": {"type": "string"},
        # Optional, additive: a structured index
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
        # Optional. The finding Doc_07's whole-ecology reading yields that no
        # single lens shows. Analytical prose, never compiled into the
        # prompt; the World Profile view renders it.
        "integrative_observation": {"type": "string"},
    },
    "source": {
        "author": {"type": "string"},
        "work": {"type": "string"},
        "edition": {"type": "string"},
        "rights_status": {"type": "string"},
        "attribution_status": {"type": "string"},
        "discovery_channel": {"type": "string"},
        "external_ids": {"type": "object"},
        # Optional, additive, best effort and existing where possible:
        # foreign key into
        # cic/corpus-map/WORKS.yaml's own work_id, cross-checked by
        # cic/engine/works_registry.py's record_work_id_problems(), not by
        # this schema (a typo'd id is still a well-formed string). Not yet
        # in COMPLETION_REQUIRED - existing source records validate
        # unchanged without it, and most will stay unset: WORKS.yaml is
        # itself a seeded, incomplete registry (four entries at the time
        # this field was added), so absence means "not joined yet," not
        # "wrong."
        "work_id": {"type": "string"},
        # Library Access Gate D3 SS5. What this record's
        # subject IS in relation to the library. Checked for agreement with
        # `edition` by engine/m9's source-kind. Optional, additive - not yet
        # in COMPLETION_REQUIRED, same reasoning as work_id above: every
        # existing source record (398 across the nine worlds) predates this
        # field, and making it required here would fail them all at the
        # schema layer rather than at source-kind's own waived finding.
        "kind": {"type": "string", "enum": ["vendored", "unvendored", "absence"]},
        # D3 SS5, Q5. For kind: absence only - strings that must NOT
        # window-match in the file `edition` names. The compiler reads that
        # (possibly off-shelf) file to verify, and logs the read; the
        # Representative never sees it. Necessary, not sufficient: absence
        # of a heading string is evidence the claim was checked, not proof
        # of the claim.
        "absence_probes": {"type": "array", "items": {"type": "string"}, "minItems": 1},
        # D3 SS5, CM-1. The bucket row this source IS,
        # copied from cic/corpus-map/<census_id>.yaml's own row_id - a
        # string that exists, never guessed. Resolved (role, confidence,
        # voice_of) at compile time into compiled/shelf.json; nothing
        # derived is ever written here.
        "shelf_row": {"type": "string"},
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
        # builder or future tooling spot the highest-risk terms without
        # parsing prose (Glossary/Story/Quote Template SS1). Not yet in
        # COMPLETION_REQUIRED; existing term records validate unchanged
        # without it.
        "distortion_risk": {"enum": ["low", "medium", "high"]},
        # The word's OWN older/ordinary sense before this world's
        # community repurposed it - distinct from false_friend (modern
        # concepts projected backward). Optional: many world_words are
        # coinages with no meaningful prior secular sense to record.
        "prior_sense": {"type": "string"},
        # Build-Plan.md Stage 3d / Adjusted-Design.md item 8: per-form
        # classification for engine.m4.term_glosses's firing rule. A
        # foreign/technical form ("Logos", "hesychia", "virtus") is
        # distinctive enough that its bare appearance in the voice's own
        # text is real signal - fires on sight by design.
        # An ordinary-English form this world's own world_word happens to
        # use ("the world", "power", "elder") is common enough in
        # unrelated prose that the same bare-appearance rule mislights -
        # gated back to firing only inside a sentence the turn already
        # cited to this term record. Optional and per-form (one term can
        # mix both kinds, e.g. gallic.term.virtus's "virtus" vs "power");
        # a form this list doesn't name - including every term record
        # fleet-wide that predates this field - defaults to "technical",
        # its exact current behavior. Authoring rule, drafted here rather
        # than folded into the L4 template (flagged, not this stage's to
        # edit: Build/reference/L4-Templates/Deployment_Lexicon_Chunk_Template.md)
        # - when writing or reviewing a term's world_word, mark a form
        # "ordinary" if it is a common English word or phrase that could
        # plausibly appear in a participant's or the voice's own ordinary
        # sentence with no connection to this term; leave it (or every
        # form, if the field is simply omitted) "technical" otherwise.
        "gloss_forms": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "form": {"type": "string"},
                    "kind": {"type": "string", "enum": ["technical", "ordinary"]},
                },
                "required": ["form", "kind"],
                "additionalProperties": False,
            },
        },
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
        # born/died typed as string, not left to `{"type": "object"}`'s own
        # implicit anything-goes: cic-website/assets/orientation-render.mjs's
        # own figureDateSpan() calls .split(" (") on both unconditionally, so
        # a bare YAML integer (e.g. `died: 1531`, parsed as an int, not a
        # string) passes this schema silently and then throws at render time
        # - found live via rzg.figure.zwingli's own `died: 1531` (found and
        # fixed to `died: "1531"` the same session this constraint was
        # added), the only fleet-wide instance when checked directly against
        # every world's own figure records.
        "dates": {
            "type": "object",
            "properties": {
                "born": {"type": ["string", "null"]},
                "died": {"type": ["string", "null"]},
            },
        },
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
        # Optional. The approved-source anchoring paragraph (Representative
        # Construction Framework, Approved Source Anchoring): it names 5 to
        # 10 of the world's own Native sources, images or teachers' words and
        # says the voice falls back to the plain shape of its own life rather
        # than reach for a more vivid image from elsewhere. Compiled into the
        # prompt as its own section only when set.
        "source_anchor": {"type": "string"},
        # Optional. The 5 to 10 entries the paragraph is drawn from, one short
        # name each, every one named verbatim in `source_anchor`. Never
        # compiled; the deployed-artifact check reads it to count entries.
        "source_anchor_entries": {"type": "array", "items": {"type": "string"}},
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
    # Website V2 world_front design (approved to proceed):
    # records/<code>/ becomes canonical for the participant-facing website
    # too, one world_front record per world, compiled to
    # cic-website/data/worlds/<census_id>.json by engine/m2 (see
    # compiler.py's compile_world_front()). MUST NEVER reach the
    # Representative's own prompt/capsule/chunk/repository compilation -
    # engine/m2/builders.py's CHUNK_DIR_BY_TYPE, build_prompt() and
    # build_capsule() are allowlists that simply never name this type, and
    # build_repository_json()'s own denylist (_PACKAGE_EXCLUDED_RECORD_
    # TYPES) explicitly excludes it too, since that denylist processes
    # every OTHER type by default. See
    # engine/m2/tests/test_voice_assembly_exclusion.py for the regression
    # test proving this holds.
    "world_front": {
        "census_id": {"type": "string"},
        "skim": {
            "type": "object",
            "properties": {"tile": _UNIT},
            "additionalProperties": False,
        },
        "orientation": {
            "type": "object",
            "properties": {
                "story": {"type": "array", "items": _UNIT},
                "documented_stories": {"type": "array", "items": _DOCUMENTED_STORY_ENTRY},
                "voices": {"type": "array", "items": _VOICE_UNIT},
                "floor_note": _UNIT,
                "legacy": {"type": "array", "items": _UNIT},
                "experience_today": {"type": "array", "items": _EXPERIENCE_TODAY_ENTRY},
                "relations_summary": _UNIT,
                "sourcing": _UNIT,
                "read_first": {"type": "array", "items": _READ_FIRST_ENTRY},
            },
            "additionalProperties": False,
        },
        "narrative": {
            "type": "object",
            "properties": {
                "who_speaks": _WHO_SPEAKS_SCHEMA,
                # mode 2: a bare honest_limit record id, rendered verbatim
                # from that record's own `statement` field at compile time
                # - never authored prose of its own.
                "quiet": {"type": "string"},
                "questions": {"type": "array", "items": _QUESTION_ENTRY},
                # mode 2, each: bare quote/term record ids, rendered from
                # quote.modern_rendering / term.plain_meaning-or-quick_
                # meaning at compile time - never `quote.text` (Mark's
                # standing quote ruling; see gates.py's quotation-mark
                # fidelity gate).
                "pull_quotes": {"type": "array", "items": {"type": "string"}},
                "glossary": {"type": "array", "items": {"type": "string"}},
            },
            "additionalProperties": False,
        },
        "export": {
            "type": "object",
            "properties": {
                "include_types": {"type": "array", "items": {"enum": _EXPORT_INCLUDE_TYPES}},
            },
            "additionalProperties": False,
        },
    },
    # A world's participant-facing world_front has a facilitator-only
    # counterpart: what a human facilitator needs to run this world well,
    # never shown to a participant and never compiled into anything a
    # Representative or a participant-facing surface reads. `audience` is
    # fixed by the schema itself (a `const`, not an author's choice) so a
    # facilitator_brief can never be mistaken for participant-facing
    # content by a reader who only has the record in front of them, not
    # its record_type.
    "facilitator_brief": {
        "audience": {"const": "facilitator"},
        "world_identity": _UNIT,
        "formation_strengths": {"type": "array", "items": _UNIT},
        "formation_limitations": {"type": "array", "items": _UNIT},
        "participant_type_fit": {"type": "array", "items": _UNIT},
        "pairing_guidance": _UNIT,
        "cautions": {"type": "array", "items": {"type": "string"}},
        "living_tradition_handling": _UNIT,
        "redirect_notes": _UNIT,
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
