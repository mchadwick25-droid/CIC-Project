"""The gate battery (Artifact-1 SS6). Each gate is a function
(records, fleet, registry) -> list[str] of human-readable findings; an empty
list means that gate passed clean. Gate names here are the same strings used
as `gate:` ids in fixtures/seeded_defects.yaml, so the selftest can map one
to the other directly with no separate lookup table (law 4, applied to test
wiring too).
"""
import re
from pathlib import Path

from jsonschema import Draft202012Validator

from engine.prose import is_guard_marker_line, quote_aware_sentences

from . import canon
from .fk import fk_grade
from .quote_verbatim import gate_quote_verbatim
from .schemas import RELATION_INVERSE, build_schema
from .spoken_fields import ATTRIBUTION_FIELDS, PERSPECTIVE_FIELDS

FK_CEILING = 10

# Below this, gate_readability skips FK grading entirely - see that
# function's own inline comment for why. 12 was chosen empirically: every
# short-but-clear test case found stayed under it, and every deliberately
# dense short test case still scored 30+ well above FK_CEILING even at
# 6-11 words, so genuinely dense short text is not exempted by this floor.
MIN_WORDS_FOR_READABILITY_CHECK = 12

# cic/texts/ - two levels up from engine/m1/, then across to the sibling
# cic/ tree. This module deliberately does NOT import cic/engine/
# texts_registry.py's own rights_clears() (a different top-level package,
# and this compiler-facing module currently imports nothing outside
# engine/m1/) - the open-licence check below duplicates its ~1-line logic
# rather than reach across that boundary for one function.
_TEXTS_DIR = Path(__file__).resolve().parents[2] / "cic" / "texts"
# Anchored to a real extension (every file in cic/texts/ is .txt or .xml,
# confirmed against the live directory) rather than a greedy [\w.-]+ -
# caught live against real records: "cic/texts/macarius_..._mason1921.txt.
# Two divisions" (a sentence-ending period right after the filename) was
# swallowing that period into the captured filename with the greedy form,
# producing a false "file does not exist" against a file that does.
_EDITION_PATH = re.compile(r"cic/texts/([\w\-]+\.(?:txt|xml))")
# The canonical passage address form defined this session: cic:<file-stem>:
# <locus>, e.g. cic:npnf208_basil-letters-select-works.xml:vi.iii.CLXXXVIII.
# Same shape as cic/engine/works_registry.py's own _ADDRESS regex, kept as a
# separate constant rather than imported - this module (engine/m1/) currently
# imports nothing from cic/engine/, the same boundary _EDITION_PATH's own
# comment above already draws for texts_registry.py.
_ADDRESS_RE = re.compile(r"^cic:([A-Za-z0-9._-]+):(.+)$")

COMPLETION_REQUIRED = {
    "world_core": ["time_window", "horizon", "formation_logic", "thinness", "cautions"],
    "source": ["author", "work", "edition", "rights_status", "attribution_status", "discovery_channel"],
    # distortion_risk added for the glossary/story/quote modern-
    # vs-world contrast retrofit (reference/Redesign-Spec/Glossary-Story-Quote-
    # Template.md) - the retrofit's own trigger fires
    # once the retrofit task is sent to
    # all six threads. false_friend and senses.translational are ALSO
    # required by the retrofit but aren't listed here: false_friend's own
    # typed-empty-list "none identified" state (_is_blank([]) is True, so
    # this dict's simple not-blank check would wrongly flag a real,
    # complete "none" as missing) and senses.translational's nested path
    # both need real logic this flat per-type list can't express - see
    # gate_glossary_retrofit_complete below, the dedicated gate for
    # exactly those two fields.
    "term": ["plain_meaning", "world_word", "senses", "quick_meaning", "distortion_risk"],
    "story": ["narrative_tier", "narrative_tier_justification", "tellable_as", "text", "modern_contrast"],
    "quote": ["text", "speaker_or_author", "license", "modern_lens_note"],
    "figure": ["names", "narratable", "bridge_line"],
    "gravity": ["name", "description", "classification"],
    "force": ["name", "description", "matrix_cell"],
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


def _world_front_referenced_ids(rec: dict) -> set[str]:
    """Every id a world_front (or facilitator_brief) record points at from
    outside its own envelope: mode-1/mode-3 units' `grounded_in`, mode-3's
    `from`, mode-2's bare-id fields (`quiet`, `documented_stories[].story_id`,
    `voices[].figure`, `pull_quotes`, `glossary`, `read_first[].source`,
    `who_speaks.figures`, `questions[].demonstration`/`.cite`). Added for
    the Website V2 world_front design - gate_referential validated
    every other record type's own reference fields already; world_front's
    were added to the schema in the infrastructure pass but never wired in
    here, so a typo'd `grounded_in` id validated cleanly (schema only checks
    it's a string) and resolved silently to nothing at compile time. The
    desert pilot's own manual check (not this gate) is what first caught
    this gap - see worlds/desert/Open_Gaps_Tracking.md.
    """
    ids: set[str] = set()

    def walk(node):
        if isinstance(node, dict):
            grounded = node.get("grounded_in")
            if isinstance(grounded, list):
                ids.update(g for g in grounded if isinstance(g, str))
            from_id = node.get("from")
            if isinstance(from_id, str):
                ids.add(from_id)
            for key in ("story_id", "figure", "source", "demonstration"):
                value = node.get(key)
                if isinstance(value, str):
                    ids.add(value)
            cite = node.get("cite")
            if isinstance(cite, list):
                ids.update(c for c in cite if isinstance(c, str))
            for value in node.values():
                walk(value)
        elif isinstance(node, list):
            for item in node:
                walk(item)
        elif isinstance(node, str):
            pass

    quiet = rec.get("narrative", {}).get("quiet") if isinstance(rec.get("narrative"), dict) else None
    if isinstance(quiet, str):
        ids.add(quiet)
    figures = rec.get("narrative", {}).get("who_speaks", {}).get("figures") if isinstance(rec.get("narrative"), dict) else None
    if isinstance(figures, list):
        ids.update(f for f in figures if isinstance(f, str))
    for section_name in ("skim", "orientation", "narrative"):
        walk(rec.get(section_name))

    return ids


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
        if rec.get("record_type") == "world_front":
            for ref_id in sorted(_world_front_referenced_ids(rec)):
                if ref_id not in all_ids:
                    findings.append(f"{rid}: referenced id {ref_id!r} does not resolve to any record")
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


def gate_glossary_retrofit_complete(records, fleet, registry) -> list[str]:
    """The two glossary/story/quote retrofit fields COMPLETION_REQUIRED's
    flat per-type list can't express correctly (reference/Redesign-Spec/Glossary-
    Story-Quote-Template.md SS1) - same discipline as gate_narratability's
    own dedicated nested checks for story, applied here to term:

    - term.false_friend: a typed array, and its own empty-list state
      ("none identified") is COMPLETE, not missing - the same sentinel
      rule Artifact-1 already applies to retrieve_when. Required here is
      "the key is present and not None," never "the list is non-empty."
    - term.senses.translational: the actual today-vs-world bridge
      sentence - required to be a real, non-blank string; senses itself
      being present (COMPLETION_REQUIRED's own check) says nothing about
      whether this specific nested field was ever filled in."""
    findings = []
    for rid, rec in records.items():
        if rec.get("record_type") != "term":
            continue
        if "false_friend" not in rec or rec["false_friend"] is None:
            findings.append(f"{rid}: missing required field 'false_friend' (an empty list is a valid 'none identified' - omitting the field is not)")
        if _is_blank((rec.get("senses") or {}).get("translational")):
            findings.append(f"{rid}: missing required field 'senses.translational'")
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


def gate_retrieval_negatives_structured(records, fleet, registry) -> list[str]:
    """Build-Plan.md Stage 4a splits the one field that
    used to carry both an ordinary retrieval-scoping redirect and a barred-
    claim honesty guard into two real fields with two different jobs:
    `retrieval.prefer_instead` (redirect) and envelope-level `claim_guards`
    (guard). `do_not_retrieve_when` stays in the schema only for
    additive-only compatibility (engine/m1/schemas.py) - it is never
    populated by real authoring again, and nothing else in the gate
    battery enforces that on its own (schema-validation alone would happily
    accept a populated one). Three structural invariants, not just field
    presence:

    1. `do_not_retrieve_when` must stay empty/absent - a populated one is a
       regression to the pre-split shape this stage retired.
    2. every `claim_guards` entry must read as a genuine barred-claim guard
       (matches `engine.prose.GUARD_MARKERS`, the same keyword set Stage
       1's own D1 measurement was run against) - not a retrieval-scoping
       note that landed in the wrong field.
    3. no `retrieval.prefer_instead` entry may read as a guard clause - the
       mirror check, catching a guard clause that leaked back into the
       redirect-only field and would go unenforced there.
    """
    findings = []
    for rid, rec in records.items():
        retrieval = rec.get("retrieval") or {}
        dnrw = retrieval.get("do_not_retrieve_when")
        if dnrw:
            findings.append(
                f"{rid}: retrieval.do_not_retrieve_when is populated ({len(dnrw)} line(s)) - this field "
                f"is retired; move each line to prefer_instead or claim_guards"
            )
        for guard in rec.get("claim_guards") or []:
            if not is_guard_marker_line(guard):
                findings.append(
                    f"{rid}: claim_guards entry does not read as a barred-claim guard "
                    f"(no GUARD_MARKERS phrase): {guard!r}"
                )
        for redirect in retrieval.get("prefer_instead") or []:
            if is_guard_marker_line(redirect):
                findings.append(
                    f"{rid}: prefer_instead entry reads as a guard clause, not a redirect "
                    f"(matches GUARD_MARKERS): {redirect!r} - move it to claim_guards"
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


def gate_edition_rights_consistency(records, fleet, registry) -> list[str]:
    """gate_rights (above) only checks that rights_status is non-blank -
    never that it agrees with anything. A source record's edition field
    often names a specific vendored file in free-form prose (the same
    "cic/texts/<filename>" string cic/engine/texts_registry.py's own
    citing_records() already scans records/ for, in the opposite
    direction - that module finds records from a file, this finds a file
    from a record). Nothing before this checked the path actually
    resolves: a record could name a file that was renamed, moved, or
    never vendored, and no gate would catch it before a build thread
    noticed by hand. Two checks, only for source records whose edition
    names such a path:
      (1) the file exists under cic/texts/ at all;
      (2) if the file's own header states an open licence rather than
          public domain (so far only evagrius_praktikos_dysinger.txt,
          CC BY 4.0), the record's rights_status should say so too, not
          bare "public-domain" - a record read on its own, without the
          vendored file open beside it, should not misstate what it can
          license.
    A record whose edition never names a cic/texts/ path at all (a
    consult-only or not-yet-vendored source) is out of this gate's scope
    entirely - that is what gate_rights already governs.
    """
    findings = []
    for rid, rec in records.items():
        if rec.get("record_type") != "source":
            continue
        edition = str(rec.get("edition") or "")
        m = _EDITION_PATH.search(edition)
        if not m:
            continue
        filename = m.group(1)
        path = _TEXTS_DIR / filename
        if not path.exists():
            findings.append(f"{rid}: edition names cic/texts/{filename}, which does not exist on disk")
            continue
        header = path.read_text(encoding="utf-8", errors="replace")[:4000]
        is_open_licence = "cc by" in header.lower()
        rights_status = str(rec.get("rights_status") or "").strip().lower()
        if is_open_licence and rights_status == "public-domain":
            findings.append(
                f"{rid}: edition names cic/texts/{filename}, whose own header declares an open "
                f"licence (not public domain), but rights_status says bare 'public-domain' - "
                f"misstates the actual rights basis to a reader of this record alone")
    return findings


def gate_canonical_address(records, fleet, registry) -> list[str]:
    """Mechanical half of the canonical passage address (cic:<file-stem>:
    <locus>), formally added to the schema as an
    optional `address` field sitting beside `locus` on any sources[] entry
    (a new sibling field, locus itself
    untouched; optional/best-effort backfill on existing records). Checks
    the two things a bare string type can't: the address is well-formed,
    and the file it names actually exists under cic/texts/. Does NOT check
    that <locus> resolves to a real division inside the file - the same
    boundary works_registry.py's own parse_address() draws for WORKS.yaml's
    item addresses, for the same reason: confirming a real div/section
    marker exists would mean re-implementing each format's own structure
    parser per record, not a one-line check. Envelope-level like locus
    itself, so this runs over every record type's sources[], not only
    quote - quote is only where the field was scoped from.
    """
    findings = []
    for rid, rec in records.items():
        for i, ref in enumerate(rec.get("sources") or []):
            addr = str(ref.get("address") or "").strip()
            if not addr:
                continue
            m = _ADDRESS_RE.match(addr)
            if not m:
                findings.append(f"{rid}: sources[{i}].address {addr!r} does not match the "
                                 f"cic:<file>:<locus> form")
                continue
            filename = m.group(1)
            if not (_TEXTS_DIR / filename).exists():
                findings.append(f"{rid}: sources[{i}].address names cic/texts/{filename}, "
                                 f"which does not exist on disk")
    return findings


def gate_readability(records, fleet, registry) -> list[str]:
    # Quote's readability-relevant field is `modern_rendering`
    # (schemas.py, quote TYPE_PROPERTIES), not modern_lens_note (a
    # meaning-clarification note, not a plain-language rendering). Per the
    # V1.2 process doc (Ministry/Technology/CiC_Record_Native_World_Build_
    # Process_V1_3.md): "Quote records author their modern_rendering at
    # birth. The spoken form is a modern-English translation, never the
    # archaic original; the original stays as the record's text for Level
    # 3." Every built world's quote records already populate it;
    # `engine/m4/evidence.py`'s own
    # `_speakable_text` already reads `modern_rendering or text` for
    # exactly this reason. So this gate grades `modern_rendering`, same
    # as term/honest_limit's own fields - and deliberately NEVER grades
    # `text` itself, which stays verbatim by design (Level 3, the "click
    # page" original wording) and must never be pressured toward a grade
    # level.
    #
    # This is a real, live check, not a formality: run directly against
    # the actual fleet (not the fixture), it finds 12 already-authored
    # modern_rendering values over FK_CEILING across 2 worlds (hal,
    # cappadocian) - real content this gate was always meant to catch,
    # invisible only because the check itself was missing, not
    # because the fields passed clean.
    #
    # Also covers voice_craft.identity/guard/flavor_notes[].note/
    # characteristic_concerns[], despite being the
    # ONE record type compiled into every single turn's own prompt
    # (engine/m2/builders.py build_prompt(), "Who we are"/"How we speak").
    # Found via a participant-facing quality complaint (gallic's
    # answers landing "too long and too abstract") traced back to this
    # exact record type - not a gap suspected in advance.
    # alx.voice.craft's own header states the design intent this closes:
    # "kept small per spec SS4.3.5: no trait rubrics, no avoid-trait
    # catalogs, no stacked rules - rule-stacks stiffen the conversation."
    findings = []
    checks = []
    for rid, rec in records.items():
        if rec.get("record_type") == "term":
            checks.append((rid, "quick_meaning", rec.get("quick_meaning")))
            checks.append((rid, "plain_meaning", rec.get("plain_meaning")))
        if rec.get("record_type") == "honest_limit":
            checks.append((rid, "statement", rec.get("statement")))
        if rec.get("record_type") == "quote":
            checks.append((rid, "modern_rendering", rec.get("modern_rendering")))
        if rec.get("record_type") == "voice_craft":
            checks.append((rid, "identity", rec.get("identity")))
            checks.append((rid, "guard", rec.get("guard")))
            for note in rec.get("flavor_notes") or []:
                checks.append((rid, f"flavor_notes[{note.get('segment')}].note", note.get("note")))
            for i, concern in enumerate(rec.get("characteristic_concerns") or []):
                checks.append((rid, f"characteristic_concerns[{i}]", concern))
    # modern_term lives in the fleet, not a world's own records (OG-13,
    # worlds/pahc/Open_Gaps_Tracking.md) - modern_sense is spoken directly
    # by the Facilitator's bridge turn (facilitator_turns.bridge_turn), the
    # same "reaches a participant verbatim" reason every other field above
    # is graded, so it belongs in this same sweep rather than a second one.
    for rid, rec in fleet.items():
        if rec.get("record_type") == "modern_term":
            checks.append((rid, "modern_sense", rec.get("modern_sense")))
    for rid, field, text in checks:
        if not text:
            continue
        # FK grade is a paragraph-level heuristic (this module's own header:
        # "good enough to gate obviously dense prose, not lexicographic
        # precision") and it misfires on short strings: found when alx's own
        # guard field - "Honest thinness beats invented
        # depth, absolutely.", 7 words, plainly clear - scored FK 14.3,
        # purely because a handful of multi-syllable words dominate the
        # formula's syllables/word term when there are too few words for
        # its words/sentence term to offset it. Tested directly before
        # adding this floor: genuinely dense short text is NOT hidden by
        # it - a 6-word deliberately dense phrase still scored 41, and an
        # 11-word one scored 35, both far past FK_CEILING regardless of
        # length. So a floor below which grading is skipped catches false
        # positives on short clear text without opening a real blind spot
        # for short dense text, which the formula still flags loudly.
        if len(text.split()) < MIN_WORDS_FOR_READABILITY_CHECK:
            continue
        grade = fk_grade(text)
        if grade > FK_CEILING:
            findings.append(f"{rid}: {field} scores FK grade {grade:.1f}, above the ceiling of {FK_CEILING}")
    return findings


# The fleet's own exemplar total (alx.voice.craft: identity + guard +
# characteristic_concerns + flavor_notes[].note, word-counted the same way
# build_prompt() concatenates them) is 401 words. Five of the six original
# worlds land at or under 730; gallic - the case that surfaced this gate,
# a live participant-facing complaint ("too long and too abstract") traced
# to this exact record - runs 1802, 4.5x alx. 900 is set just above
# cappadocian's 878 (a real, milder instance of the same drift, not yet
# reviewed) and comfortably above every original-six world, so this gate
# fails only builds that have actually drifted past the fleet's own worst
# still-tolerable case, not the ordinary spread already live. First pass,
# stated as a number so it can be argued with directly - same footing as
# FK_CEILING and every COVERAGE entry in cross_world.py.
VOICE_CRAFT_WORD_CEILING = 900

# Per-world exceptions are ruled at the project level, not a build thread's
# self-granted exemption. gallic: after an earlier trim (1802 -> 1483
# words, every readability finding fixed, nothing load-bearing cut - see
# gallic.voice.craft's own revision history), closing the remaining 583
# words would mean cutting the three verified quotations, the six named
# points of disagreement between its two households, or other specifics
# this pass deliberately kept. witt: same shape of tradeoff, same ruling.
# After a trim (2127 -> 1399 words - the record originally
# carried the Permanent Prompt Template's own backstop paragraphs near-
# verbatim per check 5d, before that instruction's scope was clarified at
# the source, reference/L3B-World-Build-Methodology/
# Representative_Permanent_Prompt_Template.txt), closing the remaining
# 499 words would mean cutting real specifics kept deliberately: the
# concrete images anchoring "place" (school gate, household table,
# church door, Augsburg), the tracked reversal in "disagreement"
# (Christian liberty's "must"/"free" argued two ways across 1522 and
# 1529, both kept rather than smoothed to one), and named honest limits
# (the 1525 and 1543 tracts, the one surviving woman's question). Given
# the real tradeoff, gallic's ceiling is raised to
# 1500 - a two-household world carries more genuinely load-bearing
# named content than the fleet's single-tradition worlds, so its own
# ceiling is not the fleet default. 1500 still leaves gallic real
# headroom (17 words) rather than pinning it exactly at its current
# total. For witt, given the same tradeoff and gallic's own precedent,
# witt is granted the same 1500-word ceiling rather than a new
# number - witt's 1399-word trim already clears it, with headroom (101
# words) to spare, no further cutting needed.
VOICE_CRAFT_WORD_CEILING_BY_WORLD = {
    "gallic-monastic-ascetic-christianity": 1500,
    "lutheran-wittenberg-and-its-congregations": 1500,
}


def gate_voice_craft_prompt_budget(records, fleet, registry) -> list[str]:
    """The four voice_craft fields compile into every turn's own prompt
    (engine/m2/builders.py build_prompt(), "Who we are"/"How we speak") -
    the only record type with that property. gate_readability (above)
    catches individual sentences that are too dense; it does not catch a
    record that is simply too LONG, sentence by short sentence - exactly
    gallic's own failure mode after an earlier partial fix (identity
    tightened to 20.0 words/sentence, comfortably under FK_CEILING, while
    flavor_notes stayed at 1072 words - the fix's own record says so
    directly). A separate gate, not a second check bolted onto
    gate_readability, because the finding is about total volume, not any
    one field's own text.
    """
    findings = []
    for rid, rec in records.items():
        if rec.get("record_type") != "voice_craft":
            continue
        parts = [rec.get("identity") or "", rec.get("guard") or ""]
        parts += [n.get("note", "") for n in (rec.get("flavor_notes") or [])]
        parts += list(rec.get("characteristic_concerns") or [])
        total_words = sum(len(p.split()) for p in parts)
        ceiling = VOICE_CRAFT_WORD_CEILING_BY_WORLD.get(rec.get("world_id"), VOICE_CRAFT_WORD_CEILING)
        if total_words > ceiling:
            findings.append(
                f"{rid}: identity+guard+flavor_notes+characteristic_concerns total "
                f"{total_words} words, above the ceiling of {ceiling} "
                "(this compiles into every turn's own prompt - see build_prompt())"
            )
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


# Admitted from engine/m1/gates_experimental.py (own defect-
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
# checked against alx's real corpus and found three more
# name occurrences beyond the four real leaks this gate exists to catch
# - alx.dw.one-church's `tensions` field, alx.limit.marriage's
# `why_sources_cannot_answer`, and a figure's trailing body - all
# correctly outside this field map, all legitimate.
# Relocated to engine/m1/spoken_fields.py (ATTRIBUTION_FIELDS) -
# one declared spoken-field registry instead of six/seven independent
# lists; see that module's own docstring. Same values, same behavior.
_ATTRIBUTION_FIELDS = ATTRIBUTION_FIELDS

# Each pattern below is justified by one of 4 real leaks found in a hand
# audit, not a generic guess. Synthetic examples of the same shapes below
# (this file stays live, so it never quotes the actual leaked text):
#   - _ISO_DATE: a build-decision date sitting next to a build-attribution
#     phrase inside a voice-craft field - e.g. "the 2026-01-01 decision
#     accepts this" inside a record's own identity/flavor prose. In-world
#     historical prose in this register dates things "c. 150-400 CE" /
#     "325 CE" - never ISO format - so this is a near-zero-false-positive
#     signal on its own, and alone would have caught most of the leaks.
#   - _RULED_BY: e.g. "(RULED by [name], 2026-01-01: ...)". Deliberately
#     the exact phrase "ruled by" (passive, agent-attributed), not bare
#     "ruled"/"ruling" - those fired as false positives in the hand audit
#     on real historical content ("the council... ruling on the disputed
#     confession", "his book ruled whole congregations") that has no "by
#     <name>" attribution shape. Not zero-risk itself (a real sentence
#     could read "the villages were ruled by their bishop") - a finding
#     here is still worth a human's eyes before treating it as confirmed,
#     same as any other gate finding in this battery.
#   - _STALE_STATUS: e.g. "WORKING SCOPE, NOT A RULING: world identity is
#     still open; this record is draft until that decision and revises
#     with it" - the one leak shape with no ISO date in it at all, so it
#     needed its own pattern (the pattern matches the literal phrase
#     "NOT A RULING", the marker a record author would actually type).
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
    """Built from a real defect, not a hypothetical: a hand
    audit of every field build_prompt() actually compiles found 4 places
    where build-process attribution (a date, "RULED by [name]", a direct
    quote attributed by name) had leaked into voice_craft.identity and
    world_core.horizon - the sections a live model reads as its own
    self-description and its historical scope (compiled as "Who we are",
    above the prompt's ground line, and "Horizon", below it).
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


# Voice-reproduced fields only - proven this session (not assumed) by
# reading engine/m2/builders.py's own _chunk_text()/build_prompt() directly:
# exactly these fields become the Representative's own speech.
# world_core.* is deliberately NOT here - every built world's own
# world_core record states "No Representative content appears in this
# record" in its own body, and is authored in a third-person analytical
# register on purpose (background the model reads about the world, not
# something the voice ever says). voice_craft.* is standing instruction,
# already first-person we-voice by construction (build_prompt()'s own
# instruct() vs emit() split - see its comment above). Full trace:
# CiC_Cross_System_Analysis_Tracking.md's own entry.
#
# world_front/facilitator_brief are deliberately NOT added here, and this
# is a real judgment call the Website V2 world_front design flagged rather
# than resolved, not an oversight. The design's own reasoning is right on
# its face: mode-2/mode-3 rendered text (narrative.quiet's verbatim
# honest_limit statement, narrative.pull_quotes' modern_rendering, any
# {from, text, no_new_claims} adaptation) becomes something close to the
# record's or a figure's own speech and plausibly SHOULD be checked here;
# mode-1 authored connective/etic prose (skim.tile, orientation.story,
# orientation.relations_summary, ...) is legitimately site-voice, not
# Representative-voice, and plausibly should not be.
#
# What stops this from being a one-line field-list addition is a real
# mechanism mismatch, not a policy disagreement. _PERSPECTIVE_FIELDS maps
# record_type -> a flat list of TOP-LEVEL field names, and this function's
# own lookup is `rec.get(f)` - a single string field, read directly off
# the record. Every world_front field that would actually need checking
# is not shaped that way: it sits inside a list of mode-tagged unit
# objects nested under skim/orientation/narrative (a `text` string next to
# a `from` or `grounded_in` sibling, several layers deep, and the SAME
# field name - "text" - appears on both mode-1 units this gate should
# skip and mode-3 units it should check). Reusing the existing lookup
# would either check nothing (no top-level field is literally named
# "text") or, if pointed at the wrong level, silently treat every mode-1
# unit's fresh authored prose as Representative speech - the opposite of
# the design's own stated split.
#
# Extending gate_voice_perspective to walk mode-tagged nested units
# correctly is real, scoped mechanism work, and doing it now, with no
# world_front record yet in existence (content migration is a separate,
# later stage), means building and freezing that mechanism against a
# schema shape with no real authored content to test it against - a
# structural change with nothing yet to validate it did the right thing
# on real prose. Deferred here on purpose, to land together with the
# content-migration stage that will actually have world_front prose to
# run it against; not silently dropped, and flagged again in this
# implementation's own report.
# Relocated to engine/m1/spoken_fields.py (PERSPECTIVE_FIELDS) -
# same registry as _ATTRIBUTION_FIELDS above. Same values, same behavior.
_PERSPECTIVE_FIELDS = PERSPECTIVE_FIELDS

# Form 1: the builder's-eye phrase itself - "this world[,'s]" - a name for
# a world from outside it, never an inhabitant's own way of naming their
# own. Measured: 250 genuine instances / 166 fields across all
# 8 built worlds (cappadocian alone: 73, concentrated in
# term.plain_meaning/quick_meaning - a systematic lexicon-authoring
# pattern, not scattered error), 99.2% precision once the two exceptions
# below are excluded - a full hand check of every non-lexicon hit, plus
# two independent keyword sweeps for the exception shapes, found no others.
_THIS_WORLD = re.compile(r"\bthis world\b'?s?", re.IGNORECASE)

# Form 3 (narrower than the full form measured in the tracking doc's
# census): "the world's own/last/closing/..." - the same self-referential
# possessive shape as Form 1, missing only the word "this". A blind "the
# world" search is dominated by the ordinary cosmological/generic sense
# (20 of 25 candidates fleet-wide - "entered the world", "across the
# world", direct scriptural quotation); restricting to the possessive form
# cuts that false-positive flood but is still imperfect (5 genuine of 7
# candidates in the same hand check, ~70% precision) - a finding here is
# worth a human's eyes before treating it as confirmed, same standing as
# gate_no_build_attribution's own "ruled by" pattern below.
_THE_WORLDS_POSSESSIVE = re.compile(r"\bthe world's\b", re.IGNORECASE)

# Proven exceptions to Form 1/3 - not assumed, and deliberately not a
# growing banned/allowed-word list (the Register Bar's own standing
# objection to that shape of rule applies here too; this is two fixed,
# named theological idioms, not a word list that accretes). Both name the
# created/temporal order itself - a cosmological claim - not the speaker's
# own community:
#   - anti-Marcionite cosmology, "the Maker of this world" (syr.dw.god,
#     refuting Marcion's demiurge)
#   - the ordinary "my kingdom is not of this world" sense (John 18:36),
#     here as a close paraphrase of Hegesippus verified against the
#     vendored source (pahc.story.grandsons-before-domitian, anf08 line
#     71558)
# Found by hand-checking every Form-1/3 hit fleet-wide; no
# others turned up under two independent keyword sweeps for cosmological
# vocabulary (maker, ruler, prince, wisdom, kingdom, depart, foundation).
_MAKER_OF_THIS_WORLD = re.compile(r"\bmaker of this world\b", re.IGNORECASE)
_NOT_OF_THIS_WORLD = re.compile(r"\bnot of this world\b", re.IGNORECASE)


def _perspective_exception(sentence: str) -> bool:
    return bool(_MAKER_OF_THIS_WORLD.search(sentence) or _NOT_OF_THIS_WORLD.search(sentence))


def _it_chain_hits(sentences: list[str]) -> list[str]:
    """Form 2, gated floor only (see the tracking doc for the fuller
    estimate this deliberately does not chase): sentence-initial "It"/
    "Its" immediately following a sentence whose own subject is literally
    "this world"/"the world" - a mechanically checkable anaphora chain,
    spot-checked fleet-wide at effectively 100% precision (e.g.
    alx.dw.church-failure: "This world's record leaves its wounds
    visible. Its greatest teacher was..."). The broader same-field
    co-occurrence form (every "it"/"its" anywhere in a field that also
    contains a Form-1/3 hit) measured only ~37% precision on a 40-sentence
    random sample fleet-wide and is deliberately NOT gated here - it would
    drown real findings in noise, the same reasoning gate_no_build_
    attribution's own field-scoping comment gives for staying narrow."""
    hits = []
    for i in range(1, len(sentences)):
        prev = sentences[i - 1].strip()
        cur = sentences[i].strip()
        if re.match(r"^(this world|the world)\b", prev, re.IGNORECASE) and re.match(
            r"^(it|its)\b", cur, re.IGNORECASE
        ):
            hits.append(cur)
    return hits


def gate_voice_perspective(records, fleet, registry) -> list[str]:
    """The Representative speaking about its own world from outside - "this
    world taught...", "the world's own record...", a third-person "it"/
    "its" chain describing the community as an object - rather than from
    inside it, in the we-voice the corpus's own approved exemplar
    (records/syr/demonstration/syr.demo.room-for-doubt.md, the Register
    Bar's own named standard) already models correctly throughout. Not a
    grammar nicety: a builder names a world from outside it ("this
    world"); an inhabitant of it does not, any more than a person says
    "this country" about their own.

    Root cause (full trace in CiC_Cross_System_Analysis_Tracking.md's own
    entry): the approved exemplar is already followed correctly
    everywhere it is actually checked against, but the Register Bar's own
    documented properties never named perspective as one of them - only
    readability (word choice, sentence length, FK/FRE via M7). This gate
    is the missing mechanical check; CiC_Register_Bar_2026-08-29.md and
    the Record-Native Build Process's Phase-B birth conditions were
    updated at the same time to name perspective as a bar property going
    forward, so new records are born past this, not swept afterward.

    Scoped to exactly the fields build_prompt()/_chunk_text() turn into
    the voice's own speech - see _PERSPECTIVE_FIELDS above for what that
    excludes and why. The "the world's..." and it/its-chain findings are
    lower-precision than the literal "this world" ones (documented at each
    pattern above) and are worth a human's eyes before treating as
    confirmed - same standing several other gates in this battery already
    have."""
    findings = []
    for rid, rec in records.items():
        rt = rec.get("record_type")
        texts = [(f, rec.get(f)) for f in _PERSPECTIVE_FIELDS.get(rt, [])]
        if rt == "demonstration":
            for i, turn in enumerate(rec.get("exchange") or []):
                if turn.get("speaker") == "representative":
                    texts.append((f"exchange[{i}].text", turn.get("text")))
        for field, text in texts:
            if not isinstance(text, str) or not text.strip():
                continue
            sents = quote_aware_sentences(text)
            for sent in sents:
                if _perspective_exception(sent):
                    continue
                if _THIS_WORLD.search(sent):
                    findings.append(
                        f'{rid}.{field}: speaks of "this world" from outside rather than as '
                        f"\"we\"/\"our\" - {sent[:150]!r}"
                    )
                elif _THE_WORLDS_POSSESSIVE.search(sent):
                    findings.append(
                        f"{rid}.{field}: \"the world's...\" - possibly the same outside-vantage "
                        f'pattern as "this world\'s..." without the word "this"; this form runs '
                        f"~70% precision, not exact, so worth a human read - {sent[:150]!r}"
                    )
            for hit in _it_chain_hits(sents):
                findings.append(
                    f"{rid}.{field}: the sentence right after \"this/the world...\" opens with "
                    f'"{hit.split()[0]}", continuing the third-person description instead of '
                    f"switching to \"we\" - {hit[:150]!r}"
                )
    return findings


# Record types whose id legitimately carries a canon-cell code. Only
# search_record does: a negative sweep IS defined by the cell it swept, and
# ijc holds seven that would collapse to one id without it. These records are
# build provenance - never named in a compiled prompt, never citable - so the
# splice hazard below cannot reach them.
_CELL_CODED_TYPES = {"search_record"}

_CELL_IN_ID = re.compile(r"^(?:c|f[1-6])-(?:e|i|p|t)-")


def gate_id_convention(records, fleet, registry) -> list[str]:
    """One id shape across the fleet: <world>.<type>.<distinctive-slug>, with
    no canon-cell code in the slug.

    The cell already lives in the record's own canon_cells field. Across the
    six worlds it was measured redundant at 131 of 131 - every cell-coded id
    agreed with its own canon_cells, none disagreed, none lacked cells. So the
    prefix carried nothing, and it cost something: a small closed vocabulary
    (28 cells) in front of a slug is trivially recombinable, and the voice
    recombined it. Measured live on syr, which had the most records and the
    most repeated slugs:

        [[syr.dw.f2-e-decides]]  = cell of f2-e-record + slug of f1-e-decides
        [[syr.dw.c-t-reading]]   = cell of c-t-was-jesus-god + slug of f2-t-reading

    Both were real records spliced together. All 22 of syr's witness ids were
    in its prompt, so this was never a missing address - it was too many
    near-identical ones. Naming more records makes that worse, not better,
    which is why the convention comes before finishing the addressability
    list.

    Also holds the fleet to ONE shape. Before this gate, five worlds cell-coded
    their witnesses and pahc did not; demonstrations were cell-coded in four
    worlds and plain in two; honest limits were split inside every world. At
    six worlds that is untidy. At the hundred the spec plans for, it is a
    corpus nobody can write a tool against.
    """
    findings = []
    for key, rec in records.items():
        if rec.get("record_type") in _CELL_CODED_TYPES:
            continue
        # the record's OWN declared id, not the dict key the loader filed it
        # under - they agree in a well-formed corpus, and this gate is one of
        # the places that has to notice when they do not.
        rid = rec.get("id") or key
        parts = rid.split(".", 2)
        if len(parts) != 3:
            findings.append(f"{key}: id {rid!r} is not <world>.<type>.<slug>")
            continue
        if _CELL_IN_ID.match(parts[2]):
            findings.append(
                f"{rid}: slug opens with a canon-cell code. The cell belongs in "
                f"canon_cells={rec.get('canon_cells')}, not in the id - a cell "
                "prefix in front of a slug is what the voice splices."
            )
    return findings


# ---------------------------------------------------------------------------
# world_front gates (Website V2 world_front design, approved to proceed).
# Three checks, of three different shapes, because the design
# itself calls for three different shapes here - not a stylistic choice:
#
#   gate_quote_mark_fidelity   deterministic, registered below in GATES -
#                              exact string matching is the right tool for
#                              "does this quoted span equal that field."
#   flag_cross_record_consistency
#                              a report generator, NOT registered in GATES/
#                              run_all - the design's own words are "does
#                              not need to be a hard, deterministic
#                              pass/fail gate," the same standing several
#                              existing gates already carry (see
#                              gate_voice_perspective's own docstring).
#   check_mode3_claim_fidelity LLM-judged scaffolding, NOT registered - a
#                              trim or adaptation either broadens, narrows,
#                              or preserves a claim, and nothing short of a
#                              model call can tell those apart (see its own
#                              docstring for why a string-similarity metric
#                              provably cannot).
# ---------------------------------------------------------------------------

# The standing quote rule (restated in every desert quote
# record's own body notes, e.g. records/desert/quote/desert.quote.sarah-
# man-among-you.md: "spoken form is a modern-English translation, not a
# summary - original wording stays as text, shown at Level 3"). `text` is
# the archaic original, Apparatus/Level-3-only; `modern_rendering` is the
# only field ever meant to be voiced or quoted on a participant-facing
# surface. engine.m2.builders already reads it this way in two places
# (_quote_opening, build_quotes_json's own comment) - this gate is the
# missing mechanical check that a world_front record's own authored prose
# actually followed that rule, rather than trusting review to catch it by
# eye every time.
_QUOTE_NEVER_QUOTABLE_LICENSES = {"paraphrase-only", "do-not-voice"}

# Straight or curly double quotation marks only - deliberately not single
# quotes/apostrophes (') or curly single quotes (' '): those collide with
# ordinary contractions and possessives ("don't", "the world's own") at a
# rate that would drown any real finding in noise, and every quote record
# in this corpus is voiced with double quotes in its own modern_rendering
# (verified against the desert quote records this gate's docstring cites).
# A minimum length keeps this from firing on short scare-quoted single
# words in etic prose ("a term the world calls \"the Way\""), which are
# essentially never a rendering of a quote record's own field.
_QUOTED_SPAN_RE = re.compile(r'"([^"\n]{8,})"|“([^”\n]{8,})”')


def _normalize_quoted(text: str) -> str:
    return " ".join((text or "").split())


def _world_front_prose_strings(record: dict) -> list[str]:
    """Every authored-prose string on a world_front record - skim/
    orientation/narrative only, never the envelope (id, world_id,
    census_id, relations, sources, confidence, ...), none of which is
    prose a participant reads inside quotation marks."""
    texts: list[str] = []

    def walk(value):
        if isinstance(value, str):
            texts.append(value)
        elif isinstance(value, dict):
            for v in value.values():
                walk(v)
        elif isinstance(value, list):
            for v in value:
                walk(v)

    for section in ("skim", "orientation", "narrative"):
        walk(record.get(section))
    return texts


def _quote_field_index(records: dict, fleet: dict) -> dict:
    """{"text": {normalized -> [(quote_id, license), ...]}, "modern_rendering":
    {...}} across every quote record this world can see (its own records
    plus the fleet) - built once per gate run, looked up once per quoted
    span found."""
    index = {"text": {}, "modern_rendering": {}}
    for rec in {**fleet, **records}.values():
        if rec.get("record_type") != "quote":
            continue
        license_ = rec.get("license")
        for field in ("text", "modern_rendering"):
            value = rec.get(field)
            if not value:
                continue
            key = _normalize_quoted(value)
            index[field].setdefault(key, []).append((rec.get("id"), license_))
    return index


def gate_quote_mark_fidelity(records, fleet, registry) -> list[str]:
    """Any text a world_front record renders inside quotation marks must
    match a quote record's `modern_rendering` field exactly - never `text`
    (the quote-rendering rule; see this module's own comment above).
    Material whose license is `paraphrase-only` or `do-not-voice` must
    never appear inside quotation marks at all, from either field,
    regardless of whether it happens to match.

    This is the mechanical version of a defect that has already shipped
    live, twice, on hand-authored site copy: a
    tradition page rendered a clause in quotation marks
    that the records themselves had already declared unquotable. This
    gate cannot catch a hand-drafted HTML page (out of the M1 gate
    battery's own scope - it runs over records, not compiled site
    output), but it is the first check of its kind, run over world_front's
    own authored prose before that prose is ever compiled to a site
    surface at all.

    Deliberately silent on a quoted span that matches no known quote
    record: this is a fidelity check, not a permission list for
    quotation marks in general - etic connective prose legitimately
    quotes a term, a title, or a phrase that traces to no `quote` record,
    and flagging every such span would drown the real findings in noise.
    """
    findings = []
    index = _quote_field_index(records, fleet)
    for rid, rec in records.items():
        if rec.get("record_type") != "world_front":
            continue
        for prose in _world_front_prose_strings(rec):
            for match in _QUOTED_SPAN_RE.finditer(prose):
                span = _normalize_quoted(match.group(1) or match.group(2))
                if not span:
                    continue
                text_hits = index["text"].get(span, [])
                rendering_hits = index["modern_rendering"].get(span, [])
                for quote_id, license_ in text_hits + rendering_hits:
                    if license_ in _QUOTE_NEVER_QUOTABLE_LICENSES:
                        findings.append(
                            f"{rid}: quotation-mark span {span[:80]!r}... matches "
                            f"{quote_id}, whose license is {license_!r} - this "
                            f"material must never be rendered inside quotation "
                            f"marks at all, from either field"
                        )
                # A verbatim quote's own `text` reused in quotation marks,
                # where modern_rendering (if authored) says something
                # different - the exact shape of the mode-2 fidelity rule.
                for quote_id, license_ in text_hits:
                    if license_ in _QUOTE_NEVER_QUOTABLE_LICENSES:
                        continue  # already reported above
                    if span not in index["modern_rendering"] or all(
                        qid != quote_id for qid, _ in rendering_hits
                    ):
                        findings.append(
                            f"{rid}: quotation-mark span {span[:80]!r}... matches "
                            f"{quote_id}'s own `text` field verbatim - `text` is "
                            f"Apparatus/Level-3-only; the quoted form must come "
                            f"from `modern_rendering` (the quote-rendering rule)"
                        )
    return findings


# ---------------------------------------------------------------------------
# Cross-record consistency flag (b) - a REPORT, not a hard gate, and
# deliberately not added to GATES/run_all. The design's own words: "This
# does not need to be a hard, deterministic pass/fail gate - model it as a
# lower-precision, flag-for-review check," the same standing
# gate_voice_perspective's own "the world's..." pattern already carries
# (see its docstring). Motivated by a real, already-shipped defect:
# desert.story.sarah-answer and
# desert.quote.sarah-man-among-you are related via `associated-with` and
# both narrate the same saying of Amma Sarah in free text; one was
# corrected to drop a clause the sources cannot support, the other never
# was, and nothing in the gate battery compared them: no existing gate
# catches this, since nothing compares free-text content across related
# records for consistency.
# ---------------------------------------------------------------------------

# Free-text-claim-bearing types: records whose primary content is prose
# that could drift out of sync with a related record's own prose about the
# same underlying material. Propositional/analytical types (gravity,
# force, source, canon_question, ...) are excluded - "associated-with" to
# a source record, for instance, is a citation relationship, not two
# retellings of the same event that could contradict each other.
_FREE_TEXT_CLAIM_TYPES = {"story", "quote", "doctrinal_witness", "honest_limit", "contested_claim", "term"}


def flag_cross_record_consistency(records: dict, fleet: dict, registry: dict) -> list[dict]:
    """Flags pairs of records worth a human's own cross-check, in two
    shapes - never a verdict that either record is actually wrong, only
    that the pairing is worth reading side by side:

    1. A world_front unit whose `grounded_in` names more than one record.
       Drawing one authored claim from several records at once is exactly
       where a claim can drift from what any single one of them actually
       supports, without any one record itself being at fault.
    2. Two free-text-claim-bearing records (see _FREE_TEXT_CLAIM_TYPES)
       connected by an `associated-with` relation - the same relation
       type the sibling records in the motivating defect above used. Both narrate or
       quote the same underlying material in their own free text, so a
       correction to one's wording is exactly the kind of change that can
       silently leave the other stale.

    Callers run this against a world's whole record set and read the
    report; it is not consulted by gates.run_all or the stage-1 selftest.
    """
    findings: list[dict] = []

    for rid, rec in records.items():
        if rec.get("record_type") != "world_front":
            continue

        def walk(value, path):
            if isinstance(value, dict):
                if "grounded_in" in value and isinstance(value.get("grounded_in"), list):
                    if len(value["grounded_in"]) > 1:
                        findings.append(
                            {
                                "kind": "multi-grounded-unit",
                                "world_front": rid,
                                "field_path": path,
                                "grounded_in": list(value["grounded_in"]),
                            }
                        )
                for k, v in value.items():
                    walk(v, f"{path}.{k}" if path else k)
            elif isinstance(value, list):
                for i, v in enumerate(value):
                    walk(v, f"{path}[{i}]")

        for section in ("skim", "orientation", "narrative"):
            walk(rec.get(section), section)

    seen_pairs: set[tuple[str, str]] = set()
    for rid, rec in records.items():
        if rec.get("record_type") not in _FREE_TEXT_CLAIM_TYPES:
            continue
        for rel in rec.get("relations") or []:
            if rel.get("type") != "associated-with":
                continue
            target = rel.get("target")
            target_rec = records.get(target) or fleet.get(target)
            if target_rec is None or target_rec.get("record_type") not in _FREE_TEXT_CLAIM_TYPES:
                continue
            pair = tuple(sorted((rid, target)))
            if pair in seen_pairs:
                continue
            seen_pairs.add(pair)
            findings.append(
                {
                    "kind": "related-pair-shared-material",
                    "record_a": pair[0],
                    "record_b": pair[1],
                    "relation": "associated-with",
                }
            )
    return findings


# ---------------------------------------------------------------------------
# check_mode3_claim_fidelity (c) - LLM-judged scaffolding, deliberately
# NOT a string-match gate and NOT registered in GATES/run_all.
#
# WHY A STRING MATCH CANNOT DO THIS JOB, with a real, already-shipped
# counterexample for each direction a trim can go wrong (the standing
# decision: "an in-progress content-system redesign... now requires an
# LLM-judged check (not a string-match gate) on any length-constrained
# trim of record prose"):
#
#   BROADENS the claim - desert-monasticism.html trimmed
#   desert.limit.communal-wrong-unrepaired's statement ("...a community of
#   ours that harmed someone and then made it right: named the harm, went
#   to the one harmed, restored what was taken") down to "...made it
#   right," dropping the three-part definition of repair entirely. Any
#   substring/edit-distance metric would score that trim as HIGH
#   similarity (it removed text, added none) - and it is exactly the
#   broadened, less accurate claim this gate exists to catch. A shorter
#   string is not a safer one.
#
#   The companion defect from the same already-shipped incident shows the
#   opposite failure mode reads identically to a metric: a record's own
#   `text` field carried a clause its sibling record had already declared
#   unquotable, and the string that shipped was a VERBATIM, high-
#   similarity match of the (wrong) source record. Similarity to the
#   source proves nothing about whether the source itself, or the
#   adaptation of it, still says only what the world's own record set can
#   support - which is a question about MEANING, not about edit distance.
#
# So this is a judgment call an LLM has to make, structured exactly like
# any other judgment call this project already routes to a model rather
# than to code (the readability grade is measured; whether a trim changed
# a claim is not measurable the same way). No existing gate in this file
# calls out to a live model - grep confirms it - so there is no established
# pattern here to follow; this function is the scaffolding for the call,
# clearly marked as unimplemented, rather than a guessed-at API shape.
# ---------------------------------------------------------------------------


def check_mode3_claim_fidelity(source_text: str, adapted_text: str, *, source_field: str | None = None) -> dict:
    """Judge whether `adapted_text` (a world_front mode-3 unit's own
    `text`) says only what `source_text` (the `from` record's relevant
    field) already says - no broadened claim, no narrowed claim, no
    claim substituted for a different one.

    Returns {"consistent": bool, "reasoning": str} - a structured
    judgment, not a pass/fail boolean alone, because "yes it drifted" is
    only useful to a reviewer alongside WHERE it drifted (see the module
    comment above: a trim can broaden a claim by DELETING qualifying
    text, which no similarity score distinguishes from a safe trim).

    NOT IMPLEMENTED: this function does not yet call a model. Wiring the
    actual call is follow-on work for whenever this gate is first put in
    front of real mode-3 content (content migration is a separate, later
    stage from this one - no world_front record exists yet to adapt
    anything from). The prompt this call should send is exactly the two
    real failure cases above, restated as instruction: given a record's
    own field and a proposed shorter/adapted rendering of it, does the
    rendering assert anything the source does not, omit a qualification
    that changes what is actually being claimed, or otherwise say
    something different from - not just shorter than - the source.
    """
    raise NotImplementedError(
        "check_mode3_claim_fidelity needs a live model call wired in (no existing "
        "gate in this file calls out to one - see this function's own module "
        "comment for why a string-match/similarity implementation is actively "
        "wrong here, not just unavailable). Scaffolding only: source_text="
        f"{source_text!r}, adapted_text={adapted_text!r}, source_field={source_field!r}."
    )


GATES = {
    "schema-validation": gate_schema_validation,
    "referential": gate_referential,
    "reciprocity": gate_reciprocity,
    "completion-per-type": gate_completion_per_type,
    "narratability": gate_narratability,
    "glossary-retrofit-complete": gate_glossary_retrofit_complete,
    "quote-recording": gate_quote_recording,
    "alias-safety": gate_alias_safety,
    "distribution-health": gate_distribution_health,
    "retrieval-negatives-structured": gate_retrieval_negatives_structured,
    "confidence-crosscheck": gate_confidence_crosscheck,
    "rights": gate_rights,
    "edition-rights-consistency": gate_edition_rights_consistency,
    "canonical-address": gate_canonical_address,
    "readability": gate_readability,
    "voice-craft-prompt-budget": gate_voice_craft_prompt_budget,
    "canon-coverage": gate_canon_coverage,
    "no-build-attribution": gate_no_build_attribution,
    "voice-perspective": gate_voice_perspective,
    "id-convention": gate_id_convention,
    # gate_quote_mark_fidelity: registered now that all 8
    # built worlds' world_front records exist to actually check (content
    # migration - see worlds/desert/Open_Gaps_Tracking.md and each other
    # world's own build - is what this gate was written for). Deferred at
    # the infrastructure stage specifically because validation/gates-
    # report.json (built by engine.m2.validation.build_gates_report, from
    # this exact GATES dict) is baked into every already-built world's
    # committed package manifest - adding ANY gate here changes that file
    # for every world, real or fixture, the instant it is registered.
    # That package rebuild already happened for an unrelated reason (the
    # world_front content itself), so the original reason to hold this
    # back no longer applies; every world's package was rebuilt and
    # re-pinned again to pick up this gate's own findings (0, fleet-wide,
    # confirmed before registering).
    "quote-mark-fidelity": gate_quote_mark_fidelity,
    # gate_quote_verbatim (engine/m1/quote_verbatim.py): registered because
    # "this is about the build
    # quality, not fix on fix." Was
    # report-only while the tolerance classes
    # (whitespace/case/punctuation/ellipsis/bracket/verse_number/
    # apparatus - fleet-wide and per-edition) were still being ruled and
    # built. Same package-rebuild consequence as quote-mark-fidelity's own
    # registration above: validation/gates-report.json is baked into
    # every already-built world's committed package manifest, so adding
    # this gate changes that file for every world, real or fixture, the
    # instant it is registered - every world's package was rebuilt and
    # re-pinned to pick up this gate's own findings (0, fleet-wide,
    # confirmed before registering: the gate skips any record whose own
    # verification_state is below verified-direct - see
    # quote_verbatim.py's own `_REQUIRED_VERIFICATION_STATE` - and every
    # record still at verified-direct already verifies).
    "quote-verbatim": gate_quote_verbatim,
    # flag_cross_record_consistency and check_mode3_claim_fidelity are
    # NOT registered here, and are not deferred-pending-a-rebuild the way
    # quote-mark-fidelity was - each has its own, permanent reason to sit
    # outside this battery, documented at its own definition above:
    # flag_cross_record_consistency returns list[dict] (paired records to
    # read side by side), not this dict's own list[str] contract, and is
    # explicitly designed as "a REPORT, not a hard gate" the design itself
    # calls lower-precision and human-reviewed, the same standing
    # gate_voice_perspective already has for one of its own patterns -
    # but expressed as a report a caller runs and reads, not a battery
    # entry with its own pass/fail signal. check_mode3_claim_fidelity
    # isn't even this shape (records, fleet, registry) - it takes two
    # texts and a judgment is only checkable once a real model call is
    # wired in (still NotImplementedError; see its own docstring) - no
    # world_front record built so far uses mode 3, so nothing depends on
    # it yet.
}


def run_all(records: dict, fleet: dict, registry: dict) -> dict[str, list[str]]:
    return {name: fn(records, fleet, registry) for name, fn in GATES.items()}
