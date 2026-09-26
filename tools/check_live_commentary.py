#!/usr/bin/env python3
"""Report-only scan for review/decision commentary that has leaked into a
live or canonical surface (CLAUDE.md, "Keep the live/canonical surfaces
clean"). Never fails the build (see `main`'s fixed `return 0`) - Step 1 of
the Live-Surface-Cleanup program builds the classifier and measures it
before anything downstream (PR B's gap filing, PR C/D's actual edits)
touches a single line.

THE RULE

A live/canonical file states what the program or the record IS, now, in
plain present tense. It does not narrate who decided that, when, under
which ruling, or what a reviewer said about it along the way - that
belongs to Ministry/ (decision logs, audit trails, review rounds), to
worlds/<code>/Open_Gaps_Tracking.md (open questions), or to a waiver
(fleet-level defects not being fixed right now). A comment, docstring, or
record note is corruption exactly when it wraps a real, still-true reason
in throwaway provenance - the ruling number, the date it was decided, the
reviewer's name, the round it survived - rather than just stating the
reason.

Every line this script flags (one of the PATTERNS below matched) gets
exactly one of four verdicts:

  KEEP      - the pattern matched, but the line is already just a plain,
              present-tense statement of what the code or record does.
              A false positive of the pattern, not of the rule. Working
              docstrings and comments that happen to contain a token like
              "round" (round-trip, round number) or an incidental digit
              pair land here. Nothing to do.

  REWRITE   - a real, still-true design reason, wrapped in provenance
              (a ruling number, a Decision-Log pointer, "Mark's ruling",
              "per Mark", a reviewer's name, a review round, an ISO date
              attached to a change). The reason stays, rewritten in plain
              present tense; the who/when/entry/round moves to
              Build/Ministry/Operations/Audits/Tech-Readiness-2026-09/
              Live-Surface-Cleanup/Decision-Log.md (or the Decision-Log
              the material already belongs to).

  ROUTE     - the line records an open defect or an open question, not a
              decided, still-true fact. It moves to the owning world's
              Open_Gaps_Tracking.md, or an ACCEPTED_OPEN waiver
              (engine/m9) for a fleet-level defect not being fixed now.

  PROTECTED - never touched, regardless of what matched. See
              `is_protected` below for the exact, narrow, explained rules -
              deliberately not a baseline of accepted hits (CLAUDE.md: "how
              drift goes quiet"). A PROTECTED verdict is still reported,
              at its own file:line, so a new file drifting into one of
              these zones is visible rather than silently absorbed.

Classification order, once a line matches a pattern: PROTECTED is decided
first (path- and field-level, independent of the line's own wording).
Within an unprotected line: ROUTE if it carries an open-item cue (still
unresolved, not yet fixed); else REWRITE if it carries a provenance cue
(the primary patterns below, besides ROUTE's own); else KEEP.

A second, narrower rule (SPOKEN_VOCAB_PATTERNS below) catches a different
failure inside records/: the project's own grading and provenance
vocabulary (a Confidence letter, a Doc_0N/SS-section citation, a
Source_Registry reference, the five-level formation_confidence vocabulary
used as a spoken predicate - "is Documented") leaking into a field
engine/m1/spoken_fields.py's own SPOKEN_FIELDS registry declares SPOKEN -
compiled into what the model actually says back to a participant, not
just into a comment. Always classifies REWRITE (never a KEEP false
positive worth carving out yet). contested_claim and honest_limit are
excluded record types: their own designed subject matter is this
project's uncertainty vocabulary, and telling that apart from a genuinely
leaked term needs a human read, not a regex.

SCOPE

engine/, cic/engine/, cic/corpus-map/, records/, worlds/ (construction
documents only - see is_protected for what "only" excludes), cic-poc/
frontend/ (source only: no node_modules, no build output, no binary
assets), cic-website/, reference/, fixtures/, packages/, canon/.

Usage:
  check_live_commentary.py                 report every hit, grouped by
                                            surface then file:line
  check_live_commentary.py --surface NAME  scan one top-level surface only
  check_live_commentary.py --json PATH     also write the full hit list as
                                            JSON (used by the test suite and
                                            by PR C/D to enumerate work)

Exit code: always 0. This is a report, not a gate - see the module-level
CI job (.github/workflows/ci.yml, "Live-surface commentary scan") that
runs it on every push and never fails the run.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent if HERE.name == "tools" else Path.cwd()

# engine/m1/spoken_fields.py is the engine's own single declared registry of
# which record fields ever reach a participant or the model speaking to
# them - reused here rather than hand-listing spoken fields a second time
# (a second list is exactly how `story.tellable_as` and `voice_craft.*`
# fell out of sync with gate_readability's own coverage before this
# registry existed; see that module's own docstring).
sys.path.insert(0, str(REPO))
from engine.m1.spoken_fields import SPOKEN_FIELDS  # noqa: E402

# ---------------------------------------------------------------------------
# Scope: the live/canonical surfaces named in CLAUDE.md's "Keep the
# live/canonical surfaces clean", minus the ones that section itself
# excludes from this pass (records/, packages/, canon/, fixtures/ ARE in
# CLAUDE.md's list and are text-scanned here at the .md/.yaml level - the
# binary/compiled parts of packages/ and canon/ are skipped by SKIP_SUFFIXES
# below, not by excluding the whole surface).
# ---------------------------------------------------------------------------
SURFACES: dict[str, tuple[str, ...]] = {
    "engine": ("engine",),
    "cic-engine": ("cic/engine",),
    "cic-corpus-map": ("cic/corpus-map",),
    "records": ("records",),
    "worlds": ("Build/worlds",),
    "cic-poc-frontend": ("cic-poc/frontend",),
    "cic-website": ("cic-website",),
    "reference": ("Build/reference",),
    "fixtures": ("fixtures",),
    "packages": ("packages",),
    "canon": ("canon",),
}

SKIP_DIR_NAMES = {"node_modules", ".git", "dist", "build", "__pycache__", ".pytest_cache"}
SKIP_SUFFIXES = {
    ".png", ".jpg", ".jpeg", ".gif", ".svg", ".ico", ".woff", ".woff2", ".ttf",
    ".pyc", ".lock", ".map", ".zip", ".tar", ".gz", ".pdf", ".db",
}
TEXT_SUFFIXES = {".py", ".md", ".yaml", ".yml", ".json", ".ts", ".tsx", ".js", ".jsx", ".mjs", ".html", ".css"}

# ---------------------------------------------------------------------------
# Primary patterns - what makes a line a candidate at all.
# ---------------------------------------------------------------------------
PATTERNS: dict[str, re.Pattern[str]] = {
    "ruling-number": re.compile(r"\bR\d{2}(-[A-Z0-9]+)?\b"),
    "ruling-identifier": re.compile(r"[_a-z]_[rR]\d{2}\b|\b[rR]\d{2}_[a-z_]"),
    "entry-number": re.compile(r"\bEntry\s+\d+\b"),
    "decision-log": re.compile(r"Decision-Log"),
    "rulings-pending": re.compile(r"Rulings-Pending"),
    "marks-word": re.compile(r"Mark'?s\s+(ruling|call|word|own)\b", re.IGNORECASE),
    "per-mark": re.compile(r"\bper Mark\b"),
    "reviewer": re.compile(r"\breviewer\b", re.IGNORECASE),
    "review-round": re.compile(r"\bround\s+\d+\b", re.IGNORECASE),
    "ruled": re.compile(r"\bRULED\b"),
    "iso-date": re.compile(r"\b20\d\d-\d\d-\d\d\b"),
    "era-gate": re.compile(
        r"\bat (?:the|that) (?:Era\s+\d+\s+)?(?:same\s+)?(?:gate|Freeze)\b|\bthe Freeze\b",
        re.IGNORECASE,
    ),
}

# Grading and provenance vocabulary inside a record's own SPOKEN fields
# (see SPOKEN_FIELDS below) - the project's internal evidentiary bookkeeping
# leaking into text the model actually says back to a participant, a
# different failure from PATTERNS above (which catch build/review
# narration wherever it appears). Real example found live: records/rzg/
# world_core/rzg.core.*.md's `thinness` (a declared voice-diet field,
# compiled into every rzg turn's prompt by engine/m2/builders.py) reads
# "...rests on Confidence D/E, unacquired evidence (Source_Registry.md row
# 13) - the general doctrine is Documented, but the vivid, formation-
# defining..." - three of these four patterns firing on one sentence.
# Scope note: these only apply within a spoken field, computed per-file
# below (_spoken_field_lines) - not everywhere PATTERNS above already
# scans, since e.g. "Doc_04" is an entirely normal thing for a construction
# document or a Decision-Log to cite about itself.
SPOKEN_VOCAB_PATTERNS: dict[str, re.Pattern[str]] = {
    "confidence-grade": re.compile(r"\bConfidence\s+[A-E](/[A-E])?\b"),
    "doc-ref": re.compile(r"\bDoc_0\d\b"),
    "section-ref": re.compile(r"\bSS\d+[A-Za-z]?(\.\d+)?\b|§\s?\d+"),
    "source-registry-ref": re.compile(r"\bSource_Registry\b"),
    "confidence-predicate": re.compile(
        r"\bis\s+(Documented|Widely Accepted|Dominant Modern Reconstruction|Contested|Inferential-Thin)\b"
    ),
    # Doc_04's own six-test vocabulary (Repetition/Dependency/Formation/
    # Explanatory Power/Persistence/Interaction), PASS/FAIL grading, and
    # "Cross-Check" - used as a label, a grade, or a named member of the
    # test battery, never as ordinary English. Confirmed live in
    # un-re-voiced gravity/force descriptions: records/don/gravity/
    # don.gravity.rebaptism-boundary-marking.md ("Repetition: Doc_02
    # SS1..."; "Repetition PASS...Persistence PASS...Interaction PASS"),
    # records/desert/gravity/desert.gravity.koinonia.md ("on every test -
    # repetition, dependency, formation, explanatory power - but fails the
    # Persistence test outright"), records/cappadocian/gravity/
    # cappadocian.gravity.athens-fishermen.md ("SIX-TEST SUMMARY (Doc_04
    # SS3.1): strong on Repetition...").
    #
    # Case-sensitive on the test name itself (Title-case or ALL-CAPS -
    # the two forms every real example above actually uses; plain
    # lowercase "formation"/"persistence" as ordinary English never
    # matches) and anchored to a label-position shape (an immediate
    # colon, a singular "test" noun right after the name, PASS/FAIL, a
    # grading adverb immediately before the name, a relational "is
    # with", or the literal SIX-TEST/6-of-6/all-six marker) rather than
    # a bare word match - a case-insensitive "name + tests?" rule was
    # tried first and dropped after it fired on ordinary sentences using
    # these words as plain English: "Formation tests the soul" (tests as
    # an ordinary verb, not a label - the singular/plural split below
    # excludes it: "Formation tests" (plural verb) never matches, but
    # "the Persistence test" (singular noun following the name) does),
    # and pahc's own formation_logic field, "Formation here never
    # resolves into..." (capitalised only because it is sentence-
    # initial, and matches none of the anchors below on its own).
    "six-test-vocabulary": re.compile(
        r"\b(Repetition|REPETITION|Dependency|DEPENDENCY|Formation|FORMATION|"
        r"Explanatory(?:\s+[Pp]ower)?|EXPLANATORY(?:\s+POWER)?|Persistence|PERSISTENCE|"
        r"Interaction|INTERACTION)\s*:|"
        r"\b(Repetition|REPETITION|Dependency|DEPENDENCY|Formation|FORMATION|"
        r"Explanatory(?:\s+[Pp]ower)?|EXPLANATORY(?:\s+POWER)?|Persistence|PERSISTENCE|"
        r"Interaction|INTERACTION)\s+test\b|"
        r"\b(Repetition|REPETITION|Dependency|DEPENDENCY|Formation|FORMATION|"
        r"Explanatory(?:\s+[Pp]ower)?|EXPLANATORY(?:\s+POWER)?|Persistence|PERSISTENCE|"
        r"Interaction|INTERACTION)\s*[-–]?\s*(PASS|FAIL)\b|"
        r"\b(Repetition|REPETITION|Dependency|DEPENDENCY|Formation|FORMATION|"
        r"Explanatory(?:\s+[Pp]ower)?|EXPLANATORY(?:\s+POWER)?|Persistence|PERSISTENCE|"
        r"Interaction|INTERACTION)\s+is\s+with\b|"
        r"(?i:\b(strong|moderate|weak|indirect|strong-moderate|moderate-strong)(\s+(on|for))?\s+)"
        r"(Repetition|REPETITION|Dependency|DEPENDENCY|Formation|FORMATION|"
        r"Explanatory(?:\s+[Pp]ower)?|EXPLANATORY(?:\s+POWER)?|Persistence|PERSISTENCE|"
        r"Interaction|INTERACTION)\b|"
        r"(?i:\ball six tests\b|\bsix of six\b)|\b[0-6]/6\s+tests?\b|"
        r"\bSIX-TEST\b|\bsix-test\b|\bAUTHOR-GRAVITY[\s-]RISK\b|"
        r"\bAuthor-Gravity[\s-](encumbered|risk)\b"
    ),
    "cross-check-label": re.compile(r"\bCross-Check\b"),
    # Doc_04's own three-way gravity class (Primary/Supporting/Tensional)
    # and a general "Tier N" ranking, used as a classification label
    # rather than ordinary English - anchored to a verb of classifying, a
    # "rather than" contrast between two of the three class names, or a
    # noun ("gravity"/"gravities"/"status"/"classification") the label
    # itself governs, so an ordinary sentence using "primary" or
    # "supporting" (e.g. "the primary reason," "in support of that claim")
    # never trips it. Confirmed live: don.gravity.rebaptism-boundary-
    # marking.md ("Doc_04 SS3.2: PRIMARY, 6/6 tests PASS"),
    # don.gravity.church-of-the-martyrs.md ("Confirmed PRIMARY (Doc_04
    # SS3.3, SS4)"), desert.gravity.koinonia.md ("Classified Supporting...
    # within the context Primary gravities establish"),
    # don.contested_claim.parallel-hierarchy.md ("Dependency revealing
    # Supporting rather than Primary status").
    # "(gravity 3)" - a bare parenthetical cross-reference to another
    # gravity by its own generation-order number, Doc_04's own indexing
    # convention (distinct from the Primary/Supporting/Tensional class
    # itself). Confirmed live: desert.gravity.koinonia.md ("against the
    # elder-mediated model (gravity 3)").
    "gravity-classification-label": re.compile(
        r"\b(Confirmed|[Rr]eclassified|[Cc]lassified(?:\s+as)?)\s+"
        r"(PRIMARY|Primary|SUPPORTING|Supporting|TENSIONAL|Tensional)\b|"
        r"\b(PRIMARY|SUPPORTING|TENSIONAL)\b|"
        r"\b(Primary|Supporting|Tensional)\s+(rather than|status|gravit(y|ies)|classification)\b|"
        r"\brather than\s+(Primary|Supporting|Tensional)\b|"
        r"\bTier\s+\d\b|"
        r"\(gravity\s+\d+\)"
    ),
    # All-caps section headers copied straight out of a construction
    # document's own layout - Doc_08's LAYER 1/2/3 dimensions and its own
    # named cross-references, Doc_04's SIX-TEST summary header and its own
    # classification question. Named literally, one phrase per real header
    # found live, rather than a generic "2+ capitalised words" rule: a
    # generic rule also matched a genuinely clean field on first pass -
    # pahc.core.house-church.md's own `cautions` field numbers its points
    # with short invented labels ("1) THE IGNATIUS CONCENTRATION governs
    # ...", "3) DATING HUMILITY: ...") that are this world's own editorial
    # organization, not a copied build-template header; a literal-phrase
    # list does not fire on it. Confirmed live: don.force.sustained-
    # purity-rebaptism-practice.md ("LAYER 1 -- HISTORICAL EVENT", "LAYER
    # 2 -- WORLD'S OWN EXPERIENCE", "CROSS-CELL CONNECTION (Doc_08 Section
    # 4, Connection 2)"), don.gravity.church-of-the-martyrs.md ("SIX-TEST
    # REASONING CARRIED IN FULL").
    "all-caps-section-header": re.compile(
        r"\bLAYER\s+[123]\b|"
        r"\bSIX-TEST\s+(SUMMARY|REASONING)\b|"
        r"\bCROSS-CELL\s+CONNECTION\b|"
        r"\bCONFIDENCE/GRAVITY\s+CROSS-CHECK\b|"
        r"\bWHY\s+(PRIMARY|SUPPORTING|TENSIONAL)\s+RATHER\s+THAN\s+(PRIMARY|SUPPORTING|TENSIONAL)\b|"
        r"\bINSTITUTIONAL\s+SEPARATION\s+IS\s+REAL\b"
    ),
    # Doc_08's own six-cell matrix notation - a bracketed cell code, or
    # "Cell"/"Force" immediately followed by the matrix's own <row-digit>
    # <column-letter> shape - plus a world's own source-strand/candidate-
    # pool letter ("Strand A", "Strand A-B"), the same kind of internal
    # indexing label. Confirmed live: don.force.sustained-purity-
    # rebaptism-practice.md ("Doc_08 Cell 2B, Force 2B-1"),
    # don.force.caecilianist-victory-selects-survivors.md ("Doc_08 Cell
    # 3B, Force 3B-2"), desert.gravity.koinonia.md ("no equivalent exists
    # in Strand A or C").
    "matrix-cell-code": re.compile(
        r"\bCell\s+\d[A-Z]\b|\bForce\s+\d[A-Z]-\d\b|\[\d[A-Z]\s*-\s*[a-z][a-z/]*\]|"
        r"\bStrand\s+[A-Z](-[A-Z])?\b"
    ),
    # Review/build-history narration inside a spoken field specifically -
    # a leak this project's fleet-voice bar (CLAUDE.md: no AI tells, no
    # "generic academic phrasing") already forbids on independent grounds,
    # named here because none of the patterns above catch it. "Round N" is
    # already caught project-wide by PATTERNS["review-round"] above (any
    # surface, not just spoken fields) and is not re-declared here.
    # "an earlier version"/"draft"/"assessment" is anchored to a
    # self-referential noun ("of this/the record/field/description/
    # assessment/text") specifically so it does not fire on ordinary
    # textual-tradition prose about a HISTORICAL text's own earlier
    # version - "an earlier version of the story says the well was dry"
    # is real source-critical content, not build narration, and stays
    # unmatched (no "of this"/"of the" + record-ish noun follows it).
    "build-history-language": re.compile(
        r"\bFinding\s+S\d+\b|"
        r"\ban earlier (version|draft|assessment) of (this|the) "
        r"(record|field|description|text|assessment)\b|"
        r"\bthis (build|record)'?s? own (earlier|prior|original)\b|"
        r"\boriginal assessment\b|"
        r"\bDoc_0\d\s+later\b",
        re.IGNORECASE,
    ),
}

# A line whose ENTIRE value is a bare date - `sealed_at: '2026-08-20'`,
# `- 2026-08-20` - is a structured data field (a timestamp is exactly what
# it looks like), not "a date in a comment or free-text note" (the launch
# brief's own phrasing). Found firing on canon/sealed_probes/seals.yaml's
# `sealed_at` before this exclusion; a date embedded in a longer sentence
# (a `note:` field's prose, a Python/YAML `#` comment, a Markdown
# paragraph) still matches - only the bare scalar case is excluded.
_BARE_DATE_LINE = re.compile(
    r"^\s*[-]?\s*[\w./\[\]]*:?\s*['\"]?20\d\d-\d\d-\d\d['\"]?,?\s*(#.*)?$"
)
# The same bare-scalar exclusion, two more structured shapes found in the
# hand-labelled sample: a Markdown metadata header ("**Date drafted:**
# 2026-07-20", one field, one value, nothing else on the line - a
# construction document's own header field, not narration), and a Python
# keyword argument carrying a machine-read date (`deadline="2026-12-14"` -
# engine/m9/enforce.py's own Waiver.deadline, "carries a deadline and an
# owner" by design, not a comment).
_BARE_DATE_HEADER_LINE = re.compile(
    r"^\s*\*\*[^*]+:?\*\*:?\s*['\"]?20\d\d-\d\d-\d\d['\"]?\s*$"
)
_STRUCTURED_DATE_KWARG = re.compile(r"\bdeadline\s*=\s*[\"']20\d\d-\d\d-\d\d[\"']")

# Cues that mark a line as an open defect or open question rather than a
# decided, still-true fact - ROUTE, whether or not the line also carries one
# of the PATTERNS above. Checked directly in scan_file's own `matched`
# computation (not only inside classify_line) so a line naming an open item
# in plain prose - no ruling number, no date, nothing else PATTERNS would
# catch - still gets flagged. Found live in cic/corpus-map/: entries that
# say a cross-check "has not yet been done" or a claim is "flagged for
# Mark" carry no other pattern at all and were being silently skipped.
ROUTE_CUES = re.compile(
    r"\b(TODO|FIXME|open question|open gap|open item|not yet (resolved|fixed|answered|acquired)|"
    r"unresolved|still (pending|open)|follow-?up (item|work|needed)|known (gap|issue|defect)|"
    r"needs? (a )?follow-?up|needing (a )?ruling|flagged for (Mark|the project lead)|"
    r"worth reconsidering|has not yet been [a-z-]+|has not yet done\b)",
    re.IGNORECASE,
)

# A "round" hit that is not a review round (round-trip, round number, round
# up/down, a round object) - keeps review-round from over-firing on ordinary
# engineering prose.
NON_REVIEW_ROUND = re.compile(r"\bround[\s-]?(trip|number|up|down|robin|off)\b", re.IGNORECASE)

# A "reviewer" hit that names a generic or hypothetical third party, not this
# project's own review process - "an external reviewer" (a donor-facing ask
# to introduce one), "a reviewer checking only for X" (an illustrative
# worked example of what a reader might miss). Confirmed live in
# cic-website/support.html:127 and Build/reference/Project-Reference/
# CiC_Cleaning_Pattern_Log.md (lines 35, 69, 151, 203, 305): every one of
# these begins with an indefinite article or "external"/"academic" right
# before "reviewer", where a genuine provenance citation instead names the
# reviewer as a definite, specific party ("the reviewer's own note", "per
# reviewer").
GENERIC_REVIEWER = re.compile(r"\b(a|an|external|academic)\s+reviewer\b", re.IGNORECASE)

# A "ruling-number" hit that is actually a Source Registry row ID (this
# project's own vendored-source catalog, records/*/source/*.md's `external_
# ids.witt_source_registry_row` and its prose citations - "Source Registry
# R45", "Source Registry row 62", "the Iserloh row (R76)") rather than a
# project ruling. Confirmed live across records/witt/story/*.md and
# records/witt/source/*.md. Line-level, not per-occurrence: once a line
# names the Source Registry or a row, every R-number on that same line is
# read in that context.
SOURCE_REGISTRY_REF = re.compile(
    r"Source\s+Registry|\brow\b.{0,10}R\d+|R\d+.{0,10}\brow\b",
    re.IGNORECASE,
)

# A change-history cue: the line isn't just naming a ruling or a date, it's
# narrating that something was found, corrected, or reconfirmed - the whole
# surrounding paragraph is that narration, even where the other sentences in
# it cite process artifacts in shapes PATTERNS above misses entirely (a
# "Doc_10" single-digit citation, a "Round1" with no space, an "OG-15" gap
# ID). Confirmed live: records/witt/voice_craft/witt.voice.craft.md's own
# "CORRECTION (go-live adversarial review, Round 1 re-confirmation pass,
# ...)" paragraphs. CORRECTION/BLOCKING stay case-sensitive, same reasoning
# as the "ruled" pattern above (all-caps is the heading convention; a bare
# lowercase "correction" or "blocking" is ordinary engineering prose, not a
# change-history marker) - the multi-word phrases are safe case-insensitive.
CHANGE_HISTORY_CUES = re.compile(
    r"\bCORRECTION\b|\bBLOCKING\b|(?i:\bcaught by\b|\badversarial review\b|\bre-?confirmations?\b)"
)
# Registered as a primary pattern too, so the triggering line itself is
# tagged "change-history-cue" in the report; scan_file separately widens
# the flag to the rest of the trigger's own paragraph (tagged
# "change-history-block") for lines that carry no pattern of their own.
PATTERNS["change-history-cue"] = CHANGE_HISTORY_CUES

# ---------------------------------------------------------------------------
# PROTECTED - narrow, explained rules. No baseline file: see module
# docstring on why a baseline would let drift go quiet.
# ---------------------------------------------------------------------------

# Schema-defined source-provenance fields (Build/reference/Redesign-Spec/
# Artifact-1-Record-Schema.md §4, record type `source`: "author, work,
# edition, rights_status, attribution_status, discovery channel, external
# ids") plus `channel` (the equivalent field on `search_record` - verified
# against records/pahc/search_record/*.md, e.g. `channel: "vendored-corpus
# survey (cic/texts), 2026-08-21"`: a real ISO date that is the record's
# own provenance data, not commentary). Matched by YAML key name only -
# whatever value a record legitimately puts there (an ISO date, "per the
# corpus registry", a discovery description) is data this script was never
# asked to touch.
PROTECTED_RECORD_FIELDS = {
    "author", "work", "edition", "rights_status", "attribution_status",
    "discovery_channel", "external_ids", "channel",
}
# Quote text and modern_rendering (CLAUDE.md's own two named exceptions,
# repeated in the launch brief): the exact translated/rendered words a
# world speaks are not commentary, however they happen to scan.
PROTECTED_CONTENT_FIELDS = {"modern_rendering"}

_YAML_KEY = re.compile(r"^(\s*)([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$")


def _front_matter_field_lines(text: str) -> tuple[dict[str, set[int]], str | None]:
    """Every top-level YAML front-matter key's own line-number set (the key
    line plus its indented/blank continuation lines - a multi-line scalar
    or block), and the record's `record_type` value. Shared groundwork for
    both PROTECTED field detection and spoken-field detection below, so the
    block-tracking logic (what counts as "still this field's value") is
    written and gets it right exactly once."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, None
    end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
    if end is None:
        return {}, None
    record_type = None
    for ln in lines[1:end]:
        m = re.match(r"^record_type:\s*(\S+)\s*$", ln.strip())
        if m:
            record_type = m.group(1)
            break
    fields: dict[str, set[int]] = {}
    active_field: str | None = None
    active_indent = -1
    for i in range(1, end + 1):
        line = lines[i - 1] if i <= len(lines) else ""
        m = _YAML_KEY.match(line)
        if m and len(m.group(1)) == 0:
            key = m.group(2)
            active_field, active_indent = key, 0
            fields.setdefault(key, set()).add(i)
            continue
        if active_field is not None:
            if line.strip() == "" or (len(line) - len(line.lstrip(" ")) > active_indent):
                fields[active_field].add(i)
            else:
                active_field, active_indent = None, -1
    return fields, record_type


def _protected_record_field_lines(field_lines: dict[str, set[int]], record_type: str | None) -> set[int]:
    """Line numbers under a protected field's key or value block (a
    multi-line scalar, or a `text:` field while inside a `record_type:
    quote` file)."""
    protected: set[int] = set()
    is_quote = record_type == "quote"
    for key, key_lines in field_lines.items():
        if key in PROTECTED_RECORD_FIELDS or key in PROTECTED_CONTENT_FIELDS or (is_quote and key == "text"):
            protected |= key_lines
    return protected


# contested_claim and honest_limit exist specifically to hold this
# project's own uncertainty/confidence vocabulary as their designed
# subject matter (CLAUDE.md's formation_confidence taxonomy; honest_limit
# models "our record does not answer this" as data) - the addendum that
# asked for SPOKEN_VOCAB_PATTERNS names both explicitly as staying
# untouched by the new patterns, the same way historical content whose
# subject IS a ruling stays out of PATTERNS' own ruling/RULED scan above.
# Telling a record's own designed epistemic-limit language apart from a
# genuinely leaked project vocabulary term needs a human read, not a
# regex - out of scope for this report-only classifier.
_SPOKEN_VOCAB_EXCLUDED_RECORD_TYPES = {"contested_claim", "honest_limit"}


def _spoken_field_lines(field_lines: dict[str, set[int]], record_type: str | None) -> set[int]:
    """Line numbers under a field SPOKEN_FIELDS declares spoken for this
    record type (any role - instruction, voice-diet, evidence-head,
    participant-label all reach a participant or the model one way or
    another) - where SPOKEN_VOCAB_PATTERNS is worth checking at all."""
    if record_type in _SPOKEN_VOCAB_EXCLUDED_RECORD_TYPES:
        return set()
    spoken_names = set(SPOKEN_FIELDS.get(record_type, {}))
    if not spoken_names:
        return set()
    lines: set[int] = set()
    for key, key_lines in field_lines.items():
        if key in spoken_names:
            lines |= key_lines
    return lines


def _paragraph_lines(lines: list[str], line_no: int) -> list[int]:
    """1-indexed line numbers of the blank-line-delimited paragraph
    containing `line_no` (a plain text/Markdown paragraph, or a
    Python/YAML comment block treated the same way - the line-numbering
    scheme this whole scanner already uses)."""
    n = len(lines)
    start = line_no
    while start > 1 and lines[start - 2].strip() != "":
        start -= 1
    end = line_no
    while end < n and lines[end].strip() != "":
        end += 1
    return list(range(start, end + 1))


def _source_record_body_lines(text: str, record_type: str | None) -> set[int]:
    """Every line after a `record_type: source` record's own closing
    front-matter delimiter - its own apparatus prose, where a Source
    Registry row ID (an R-number) is that record's own subject matter, the
    same reason PROTECTED_RECORD_FIELDS already excludes its `author`/
    `discovery_channel`/etc. front-matter fields, extended to the body a
    source record writes about itself (e.g. records/witt/source/
    witt.source.marburg-articles.md's own "is R57 (Excluded)")."""
    if record_type != "source":
        return set()
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return set()
    end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
    if end is None:
        return set()
    return set(range(end + 2, len(lines) + 1))


def _is_review_doc(rel: Path) -> bool:
    """worlds/<code>/... review documents (CLAUDE.md places reviews under
    worlds/ by design). Two real naming conventions found on disk: a
    dedicated `Review-Artifacts/` directory (alx, cappadocian, don, grkap,
    ...), or a loose file in the world's own root whose name contains
    "Review" (desert, gallic, hal, ...). Both covered; neither guessed."""
    parts = rel.parts
    if len(parts) < 4 or parts[0] != "Build" or parts[1] != "worlds":
        return False
    if "Review-Artifacts" in parts:
        return True
    return "review" in parts[-1].lower()


def _is_world_build_dir(rel: Path) -> bool:
    parts = rel.parts
    return len(parts) >= 4 and parts[0] == "Build" and parts[1] == "worlds" and parts[3] == "build"


def _is_gaps_ledger(rel: Path) -> bool:
    """worlds/<code>/Open_Gaps_Tracking.md is the destination CLAUDE.md's
    own gap-tracking rule names for ROUTE findings, not a construction
    document itself - append-only, numbered, and explicitly expected to
    "cite subject + date" on every entry (CLAUDE.md, "Track gaps and
    exceptions explicitly"). Scanning it would flag the ledger's own
    required shape as if it were leaked commentary."""
    parts = rel.parts
    return len(parts) >= 3 and parts[0] == "Build" and parts[1] == "worlds" and parts[-1] == "Open_Gaps_Tracking.md"


# Historical content whose own subject matter is a ruling/verdict, not this
# project's: named explicitly rather than pattern-matched, per the launch
# brief ("historical content where 'ruling', 'verdict' etc. are the subject
# matter"). Verified against the actual text (cic-website/tree/donatism.html,
# cic-website/traditions/donatism.html): a communion narrating "the verdict
# went against them" at the real Council of Carthage, 411 - not a project
# review round.
PROTECTED_HISTORICAL_FILES = {
    "cic-website/tree/donatism.html",
    "cic-website/traditions/donatism.html",
}

# records/WORLDS_REGISTRY_LOG.md is not leaked commentary - it is already
# the registry's own designated decision-log, deliberately pulled out of
# worlds.yaml for exactly this reason (its own header: "The provenance,
# rulings, and decision history that used to live as inline comments
# inside records/worlds.yaml. Moved out 2026-09-01... this file holds why
# it says what it says"). Treating its own contents as a fresh finding
# would ask this program to rewrite the very file CLAUDE.md's own rule
# describes decision logs as belonging in.
PROTECTED_REGISTRY_LOG = "records/WORLDS_REGISTRY_LOG.md"


def _is_engine_report(rel: Path) -> bool:
    """engine/<module>/reports/ - committed battery-run output (JSON
    snapshots of records fed through a gate battery), not authored
    commentary. A "locus"/"rights_status" value inside one of these files
    is a copy of whatever the source record itself says, verbatim - the
    real finding, if any, lives in the record, not the report. The launch
    brief says so explicitly for the Step 2 edit pass ("leave them
    untouched, and list them in the PR body as a question for Mark");
    this scan applies the same treatment rather than double-counting the
    same text once as a record finding and once as a report artifact."""
    parts = rel.parts
    return len(parts) >= 3 and parts[0] == "engine" and "reports" in parts


def is_protected(rel: Path, line_no: int, protected_field_lines: set[int]) -> bool:
    rel_s = rel.as_posix()
    if rel_s.startswith("cic/texts/"):
        return True
    if rel_s == "fixtures/seeded_defects.yaml":
        return True
    if rel_s == PROTECTED_REGISTRY_LOG:
        return True
    if rel_s in PROTECTED_HISTORICAL_FILES:
        return True
    if _is_review_doc(rel) or _is_world_build_dir(rel) or _is_gaps_ledger(rel) or _is_engine_report(rel):
        return True
    if line_no in protected_field_lines:
        return True
    return False


# ---------------------------------------------------------------------------
# Classification
# ---------------------------------------------------------------------------

@dataclass
class Hit:
    surface: str
    path: str
    line: int
    category: str
    patterns: list[str] = field(default_factory=list)
    text: str = ""

    def row(self) -> str:
        return f"{self.path}:{self.line}:{self.category} ({','.join(self.patterns)})"


def classify_line(line: str, matched: list[str], in_source_record_body: bool = False) -> str:
    if ROUTE_CUES.search(line):
        return "ROUTE"
    real_matches = [
        name for name in matched
        if not (name == "review-round" and NON_REVIEW_ROUND.search(line))
        and not (name == "reviewer" and GENERIC_REVIEWER.search(line))
        and not (
            name == "ruling-number"
            and (in_source_record_body or SOURCE_REGISTRY_REF.search(line))
        )
        and not (
            name == "iso-date"
            and (
                _BARE_DATE_LINE.match(line)
                or _BARE_DATE_HEADER_LINE.match(line)
                or _STRUCTURED_DATE_KWARG.search(line)
            )
        )
    ]
    if real_matches:
        return "REWRITE"
    return "KEEP"


def scan_file(repo: Path, path: Path, surface: str) -> list[Hit]:
    rel = path.relative_to(repo)
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return []

    raw_lines = text.splitlines()

    protected_field_lines: set[int] = set()
    spoken_field_lines: set[int] = set()
    source_record_body_lines: set[int] = set()
    if path.suffix == ".md" and rel.parts[0] == "records":
        field_lines, record_type = _front_matter_field_lines(text)
        protected_field_lines = _protected_record_field_lines(field_lines, record_type)
        spoken_field_lines = _spoken_field_lines(field_lines, record_type)
        source_record_body_lines = _source_record_body_lines(text, record_type)

    change_history_block_lines: set[int] = set()
    for i, line in enumerate(raw_lines, start=1):
        if CHANGE_HISTORY_CUES.search(line):
            change_history_block_lines.update(_paragraph_lines(raw_lines, i))

    hits: list[Hit] = []
    for i, line in enumerate(raw_lines, start=1):
        matched = [name for name, pat in PATTERNS.items() if pat.search(line)]
        if i in spoken_field_lines:
            matched += [name for name, pat in SPOKEN_VOCAB_PATTERNS.items() if pat.search(line)]
        if not matched and ROUTE_CUES.search(line):
            matched = ["route-cue"]
        if not matched and i in change_history_block_lines:
            matched = ["change-history-block"]
        if not matched:
            continue
        if is_protected(rel, i, protected_field_lines):
            category = "PROTECTED"
        else:
            category = classify_line(line, matched, i in source_record_body_lines)
        hits.append(Hit(surface, rel.as_posix(), i, category, matched, line.strip()))
    return hits


def iter_files(repo: Path, surface: str):
    for root in SURFACES[surface]:
        base = repo / root
        if not base.exists():
            continue
        for path in base.rglob("*"):
            if not path.is_file():
                continue
            if any(part in SKIP_DIR_NAMES for part in path.relative_to(repo).parts):
                continue
            if path.suffix in SKIP_SUFFIXES:
                continue
            if path.suffix not in TEXT_SUFFIXES:
                continue
            if surface == "cic-poc-frontend" and "node_modules" in path.parts:
                continue
            yield path


def run(repo: Path, surfaces: list[str]) -> list[Hit]:
    hits: list[Hit] = []
    for surface in surfaces:
        for path in sorted(iter_files(repo, surface)):
            hits.extend(scan_file(repo, path, surface))
    return hits


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--surface", choices=sorted(SURFACES), default=None)
    parser.add_argument("--json", type=Path, default=None)
    args = parser.parse_args(argv)

    surfaces = [args.surface] if args.surface else sorted(SURFACES)
    hits = run(REPO, surfaces)

    counts: dict[str, dict[str, int]] = {}
    for hit in hits:
        counts.setdefault(hit.surface, {"KEEP": 0, "REWRITE": 0, "ROUTE": 0, "PROTECTED": 0})
        counts[hit.surface][hit.category] += 1

    print("Live-surface commentary scan (report-only; see tools/check_live_commentary.py)\n")
    for surface in surfaces:
        c = counts.get(surface, {"KEEP": 0, "REWRITE": 0, "ROUTE": 0, "PROTECTED": 0})
        total = sum(c.values())
        print(f"{surface}: {total} hits  (KEEP {c['KEEP']}, REWRITE {c['REWRITE']}, "
              f"ROUTE {c['ROUTE']}, PROTECTED {c['PROTECTED']})")
    print()
    for hit in hits:
        print(hit.row())

    if args.json:
        args.json.write_text(
            json.dumps([hit.__dict__ for hit in hits], indent=2) + "\n", encoding="utf-8"
        )

    return 0


if __name__ == "__main__":
    sys.exit(main())
