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

from engine.prose import quote_aware_sentences

from . import canon
from .fk import fk_grade
from .schemas import RELATION_INVERSE, build_schema

FK_CEILING = 10

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
    # distortion_risk added 2026-08-22: the glossary/story/quote modern-
    # vs-world contrast retrofit (reference/Redesign-Spec/Glossary-Story-Quote-
    # Template.md) - the retrofit's own trigger, per that doc's own words
    # ("Mark flips that switch when the retrofit task is actually sent to
    # all six threads"). false_friend and senses.translational are ALSO
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
    <locus>), defined this session and formally added to the schema as an
    optional `address` field sitting beside `locus` on any sources[] entry
    (per Mark's sign-off, 2026-09-02: a new sibling field, locus itself
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
    # RESOLVED 2026-09-02 (was flagged 2026-09-02, same day - the flag's own
    # premise turned out to be stale, not a real gap). The flag claimed
    # quote's only readability-relevant field was modern_lens_note (a
    # meaning-clarification note, not a plain-language rendering) and that
    # the "two-layer wording" idea (verbatim historical text plus a modern
    # spoken form) had no schema field. Checked against this checkout
    # directly: it does - `modern_rendering` (schemas.py, quote
    # TYPE_PROPERTIES), added the same day this flag was written, per the
    # V1.2 process doc (Ministry/Technology/CiC_Record_Native_World_Build_
    # Process_V1_3.md): "Quote records author their modern_rendering at
    # birth. The spoken form is a modern-English translation, never the
    # archaic original; the original stays as the record's text for Level
    # 3." Every built world's quote records already populate it (Mark's
    # standing ruling, 2026-08-28); `engine/m4/evidence.py`'s own
    # `_speakable_text` already reads `modern_rendering or text` for
    # exactly this reason. So this gate now grades `modern_rendering`, same
    # as term/honest_limit's own fields - and deliberately NEVER grades
    # `text` itself, which stays verbatim by design (Level 3, the "click
    # page" original wording) and must never be pressured toward a grade
    # level.
    #
    # This is a real, live check, not a formality: run directly against
    # the actual fleet (not the fixture), it finds 12 already-authored
    # modern_rendering values over FK_CEILING across 2 worlds (hal,
    # cappadocian) - real content this gate was always meant to catch,
    # invisible until today only because the check itself was missing, not
    # because the fields passed clean.
    #
    # EXTENDED 2026-09-19: voice_craft.identity/guard/flavor_notes[].note/
    # characteristic_concerns[] were never graded here, despite being the
    # ONE record type compiled into every single turn's own prompt
    # (engine/m2/builders.py build_prompt(), "Who we are"/"How we speak").
    # Found only because a participant-facing quality complaint (gallic's
    # answers landing "too long and too abstract") was traced back to this
    # exact record type - not because the gap was suspected in advance.
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
    for rid, field, text in checks:
        if not text:
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

# Per-world exceptions, Mark's own explicit ruling, not a build thread's
# self-granted exemption. gallic: after the 2026-09-19 trim (1802 -> 1483
# words, every readability finding fixed, nothing load-bearing cut - see
# gallic.voice.craft's own revision history), closing the remaining 583
# words would mean cutting the three verified quotations, the six named
# points of disagreement between its two households, or other specifics
# this pass deliberately kept. Shown the real tradeoff, Mark's ruling:
# "raise the ceiling for gallic to 1500" - a two-household world carries
# more genuinely load-bearing named content than the fleet's single-
# tradition worlds, so its own ceiling is not the fleet default. 1500
# still leaves gallic real headroom (17 words) rather than pinning it
# exactly at its current total.
VOICE_CRAFT_WORD_CEILING_BY_WORLD = {
    "gallic-monastic-ascetic-christianity": 1500,
}


def gate_voice_craft_prompt_budget(records, fleet, registry) -> list[str]:
    """The four voice_craft fields compile into every turn's own prompt
    (engine/m2/builders.py build_prompt(), "Who we are"/"How we speak") -
    the only record type with that property. gate_readability (above)
    catches individual sentences that are too dense; it does not catch a
    record that is simply too LONG, sentence by short sentence - exactly
    gallic's own failure mode after its 2026-09-18 partial fix (identity
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
# - alx.dw.one-church's `tensions` field, alx.limit.marriage's
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
# CiC_Cross_System_Analysis_Tracking.md, 2026-09-04 entry.
_PERSPECTIVE_FIELDS = {
    "term": ["plain_meaning", "quick_meaning"],
    "story": ["tellable_as", "text"],
    "ambient": ["detail"],
    "doctrinal_witness": ["text"],
    "honest_limit": ["statement"],
}

# Form 1: the builder's-eye phrase itself - "this world[,'s]" - a name for
# a world from outside it, never an inhabitant's own way of naming their
# own. Measured 2026-09-04: 250 genuine instances / 166 fields across all
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
# Found by hand-checking every Form-1/3 hit fleet-wide 2026-09-04; no
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

    Root cause (full trace in CiC_Cross_System_Analysis_Tracking.md,
    2026-09-04 entry): the approved exemplar is already followed correctly
    everywhere it is actually checked against, but the Register Bar's own
    documented properties never named perspective as one of them - only
    readability (word choice, sentence length, FK/FRE via M7). This gate
    is the missing mechanical check; CiC_Register_Bar_2026-08-29.md and
    the Record-Native Build Process's Phase-B birth conditions were
    updated the same day to name perspective as a bar property going
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
}


def run_all(records: dict, fleet: dict, registry: dict) -> dict[str, list[str]]:
    return {name: fn(records, fleet, registry) for name, fn in GATES.items()}
