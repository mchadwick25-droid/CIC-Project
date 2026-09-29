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

Exit code: 0 by default, a report. With `--base REF --enforce` the scan is
limited to files a change adds or edits relative to the merge-base with REF,
and the exit code is 1 when any of those files still carries a REWRITE or
ROUTE line: a change that edits a live file also removes the commentary
already in it. KEEP and PROTECTED lines never fail the run.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
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
# Widened from the single name `deadline` to any identifier: a Python
# kwarg/attribute assignment whose value is nothing but a quoted ISO date
# (`date="2026-08-27"`, `verified_date="2026-09-01"`, `added="2026-07-14"`)
# is structured data by construction, the same reasoning `deadline=...`
# already had - the specific name was never the load-bearing part of the
# original rule, the shape was (an assignment target holding exactly a
# date, nothing else). Confirmed live in engine/'s own test fixtures and
# seed literals (`today="2026-09-15"`, `SEALED_AT = "2026-08-20"`) - no
# `Build/worlds/*/scripts/*.py` file happens to use exactly this bare
# kwarg=date shape today (their own per-row provenance dict fields carry
# a longer descriptive string alongside the date, which this rule
# correctly leaves alone; see `divergence_note` below). A kwarg whose
# value is a longer string that merely CONTAINS a date
# ("divergence_note='Reworded 2026-09-15 to fix wording'") still does not
# match - only a bare, quote-wrapped date and nothing else as the value.
_STRUCTURED_DATE_KWARG = re.compile(r"\b[a-zA-Z_][a-zA-Z0-9_]*\s*=\s*[\"']20\d\d-\d\d-\d\d[\"']")

# A markdown table row (2+ `|` cells) whose every ISO-date occurrence sits
# inside its own cell that is otherwise just a short provenance fragment -
# a bare date, or a short channel/label phrase plus a date ("web search,
# 2026-07-14", "Added 2026-07-14") - never a longer narrative sentence.
# Same reasoning as `_BARE_DATE_LINE`/`_BARE_DATE_HEADER_LINE` (a
# structured-data date, not a date embedded in prose), extended from "the
# whole line is bare" to "this one table column is bare," since a
# Source_Registry.md row packs many such columns (row #, title, confidence,
# Added, Discovery channel/date, ...) onto one physical line together with
# citations and prose that legitimately still get scanned.
#
# Deliberately scoped to a `*Source_Registry.md`-named file only, not any
# markdown table anywhere - confirmed live that a structurally identical
# short "channel, date" table cell is NOT always fine to leave alone:
# `Build/worlds/_cross-world/DOWNLOAD-QUEUE.md`'s own last column ("direct
# WebSearch verification, 2026-09-02") is hand-labelled REWRITE, since
# that file tracks a proactive, still-changing verification pass rather
# than Source_Registry.md's own permanent, never-revised "when this source
# was first vendored" record - the same distinction between a source
# record's own permanent `discovery_channel` field and a status field that
# can go stale. Confirmed live: witt/lpc/don/cappadocian's own "Added"/
# "Discovery channel/date" columns account for the large majority of each
# file's remaining iso-date hits before this exemption; a genuinely
# narrative table cell (e.g. Doc_03's own multi-hundred-word evidentiary
# cells) is never this short, so it is never wrongly swept in by this
# check even within a Source_Registry.md file itself.
# Handles both cell orderings found live: "label, then date" (witt's own
# "web search, 2026-07-14") and "date, then label" (lpc/don's own "Added"
# column: "2026-09-01, `lpc` build thread"; cappadocian's "2026-08-31,
# build thread") - the earlier version only allowed a trailing bare comma
# after the date, so it could never match the date-first convention at
# all, leaving lpc/don/cappadocian's own "Added" columns flagged even
# though they're the identical structured-provenance shape witt's own
# column already gets exempted for.
_BARE_DATE_TABLE_CELL = re.compile(
    r"^(?:[\w][\w .,'()`/-]{0,39})?,?\s*20\d\d-\d\d-\d\d\s*(?:,\s*[\w .,'()`/-]{0,59})?$"
)
_SOURCE_REGISTRY_FILENAME = re.compile(r"(?i)(^|_)source_registry\.md$")


def _iso_date_is_bare_table_provenance(line: str, in_source_registry_file: bool) -> bool:
    if not in_source_registry_file or line.count("|") < 2:
        return False
    found_any_date = False
    for cell in line.split("|"):
        if re.search(r"20\d\d-\d\d-\d\d", cell):
            found_any_date = True
            if not _BARE_DATE_TABLE_CELL.match(cell.strip()):
                return False
    return found_any_date

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
#
# Also matches a bare "Registry" word - not just the literal "Source
# Registry" phrase above - but only when an R-number sits close by (within
# ~50 characters), not merely present anywhere on the line: Build/worlds/
# construction documents cite their own world's registry by shorter forms
# the literal phrase misses entirely - "**Registry cross-reference:** R2,
# Native, Primary" (witt), "**Registry:** R1, R2, R12" (a field label
# alone) - each confirmed live and never itself the project ruling-
# tracking vocabulary (Decision-Log/RULED/Mark's-ruling/per-Mark, every one
# of which stays its own separate pattern above). The proximity bound is
# for this bare-"Registry" case specifically, not the literal-phrase case
# above: a line can genuinely discuss "its own Registry list for that
# entry" and separately cite an unrelated R-number as a real project
# ruling many words later in the same sentence (Build/reference/method/
# CiC_Record_Native_World_Build_Process_V1.9.md:627's "guards and redirects
# (R11)" - R11 there is this project's own rule-citation convention, not a
# registry row - confirmed live, and the reason a bracket/parenthesis-
# wrapped bare R-number was tried and dropped as its own separate
# exemption: that shape alone does not reliably distinguish the two). The
# literal "Source Registry" phrase above stays unconditional (no proximity
# bound) as it always was - confirmed live that it and its cited R-number
# can sit far apart in the same long sentence (witt_Source_Registry.md:9's
# own apparatus prose, witt.source.marburg-articles.md:29's "the Reformed
# side's own account is R57 (Excluded)... (Source Registry row 56...)" -
# tightening that established, unconditional case to the same 50-character
# bound broke it).
# `Registry(?!\.yaml)`: excludes `cic/texts/REGISTRY.yaml` - this
# project's vendored-source rights/apparatus file, a different registry
# than the world's own Source Registry this exemption is about. Confirmed
# live: Build/reference/method/CiC_Record_Native_World_Build_Process_
# V1.9.md:619 cites `cic/texts/REGISTRY.yaml` and, separately in the same
# sentence, "(R33)" - a genuine project ruling in this same document's own
# established "(R##)" citation convention (R11, R13, R19 nearby), not a
# registry row; the bare coincidence of "REGISTRY.yaml" sitting within 50
# characters of it must not suppress a real ruling citation.
SOURCE_REGISTRY_REF = re.compile(
    r"Source\s+Registry|Registry(?!\.yaml)\b.{0,50}?R\d+|R\d+.{0,50}?\bRegistry(?!\.yaml)\b|"
    r"\brow\b.{0,10}R\d+|R\d+.{0,10}\brow\b",
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
    end = _yaml_frontmatter_end(lines)
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


def _yaml_frontmatter_end(lines: list[str]) -> int | None:
    """1-indexed line number of the closing `---` of a YAML front-matter
    block starting at line 1, or None if the file has no such block (no
    opening `---` at line 1, or no closing `---` found anywhere below it).
    Factored out of `_source_record_body_lines` (which used to derive this
    inline) so `_front_matter_field_lines` and the change-history widening
    in `scan_file` share the exact same detection rather than each
    re-deriving it."""
    if not lines or lines[0].strip() != "---":
        return None
    return next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)


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
    end = _yaml_frontmatter_end(lines)
    if end is None:
        return set()
    return set(range(end + 2, len(lines) + 1))


def _yaml_scalar_block_lines(field_lines: dict[str, set[int]], line_no: int) -> list[int]:
    """Widen a change-history cue found inside a YAML front-matter block to
    just the lines of the single top-level key whose value contains it
    (`field_lines`, as `_front_matter_field_lines` already computes it),
    instead of `_paragraph_lines`' blank-line-delimited paragraph.

    Front matter typically has NO blank lines between sibling top-level
    keys at all (`id:`, `world_id:`, `confidence:`, ...), so a cue inside
    one field's value (e.g. a `divergence_note: >` block, or a `rights_
    status:` sentence mentioning "adversarial review") used to sweep every
    unrelated sibling key into the same flagged "paragraph" - the entire
    front-matter block, all the way to the next real blank line or EOF.
    Confirmed live: records/lpc/source/lpc.source.hartel-cyprian-opera-
    omnia-csel3-standing-reference.md's `rights_status` sentence naming
    "Doc_01's own nine adversarial review rounds" used to flood all 20
    sibling front-matter lines (id, world_id, schema_version, sources,
    relations, ...) as REWRITE.

    A genuine multi-line scalar value stays widened together as one unit:
    its continuation lines are indented (or blank, while still inside the
    block), so they never match `_YAML_KEY`'s own top-level (zero-indent)
    shape and so never act as a sibling-key boundary - only the next real
    top-level key, a blank line, or the closing `---`/EOF ends the block,
    exactly as `_front_matter_field_lines` already tracks it.

    Falls back to widening to just `line_no` itself when the cue line
    isn't inside any recognized top-level key's own block - the front-
    matter delimiter lines themselves, or a line before the first key -
    since there is no sibling field to protect against there anyway."""
    for key_lines in field_lines.values():
        if line_no in key_lines:
            return sorted(key_lines)
    return [line_no]


_REVIEW_DOC_FILENAME_KEYWORDS = (
    "review",
    "spotcheck",
    "checkpoint",
    "unused_source_verification",
    # Five more found once the survey widened past its original sample,
    # each individually confirmed real by reading the file: "audit"
    # (_cross-world's CiC_Cross_System_Consistency_Audit), "verification"
    # (pahc's Independent_Verification and ...B7_Verification, also covers
    # "unused_source_verification" above as a substring), "coverage_check"
    # (gallic's B1a_B1b_Coverage_Check), "transcripts" (pahc's own
    # LiveDeepInterview transcripts), "boundary_testing"/"boundarytesting"
    # (ijc's Boundary_Testing_Record, pahc's own BoundaryTesting - two
    # spellings, both found live), "livetest" (hal's Phase5_LiveTest_*_
    # RoundN transcripts), "validation_documentation" (desert's Doc09c
    # Validation Documentation - deliberately the full compound, not bare
    # "validation", so a real numbered construction document like a
    # world's own Doc_09c_Validation_Layer.md - genuinely cleanable, not a
    # review artifact - stays unmatched).
    #
    # A batch review's own suggestion to also add a bare "finding" keyword
    # and a blanket `Analysis/` directory rule was tried and dropped: the
    # existing hand-labelled sample already carries counter-evidence for
    # both - `alx/Analysis/Unused_Assigned_Corpus_Finding_2026-09-09.md:13`
    # and `ijc/Post_Admission_Source_Finding_...md:279` are each real,
    # still-open construction-thread narrative (an active DRAFT's own
    # round-by-round disposition tracking), not a frozen review record -
    # confirming that "Finding"/"Analysis" in a name does not reliably
    # distinguish the two the way the keywords above do.
    "audit",
    "verification",
    "coverage_check",
    "transcripts",
    "boundary_testing",
    "boundarytesting",
    "livetest",
    "validation_documentation",
)
# "zellcheck" alone, as a plain substring, does not match
# "ZellFinalCheck.md" (witt) - "final" sits between "zell" and "check".
# A separate regex catches both "ZellCheck" and "ZellFinalCheck".
_ZELL_CHECK_RE = re.compile(r"(?i)zell\w*check")


def _is_review_doc(rel: Path) -> bool:
    """worlds/<code>/... review documents (CLAUDE.md places reviews under
    worlds/ by design). A dedicated `Review-Artifacts/` directory (alx,
    cappadocian, don, grkap, ...), or a loose file in the world's own root
    whose name signals it's an independent verification pass on an
    already-drafted document - every real naming convention found on disk
    so far, each individually confirmed real by reading the file, not
    guessed from the name alone: "Review" (desert, gallic, hal, ...),
    "SpotCheck" (gallic, witt), "Critic_Checkpoint...Simulated"
    (cappadocian), "Unused_Source_Verification" (cappadocian), "ZellCheck"/
    "ZellFinalCheck" (witt, a per-person-named check pass, same function
    as a review round), plus the keywords named above. All of these are
    the review's own evidentiary record of what a document said or a
    search found at the time of that check, not expected to track the
    corrected live text afterward - the same reason a `Review-Artifacts/`
    file is protected."""
    parts = rel.parts
    if len(parts) < 4 or parts[0] != "Build" or parts[1] != "worlds":
        return False
    if "Review-Artifacts" in parts:
        return True
    name = parts[-1].lower()
    return any(keyword in name for keyword in _REVIEW_DOC_FILENAME_KEYWORDS) or bool(_ZELL_CHECK_RE.search(name))


_BUILD_LEDGER_FILENAME = re.compile(r"(?i)(^needs-ruling\.md$|_superseded_claims\.md$)")


def _is_build_ledger(rel: Path) -> bool:
    """A ledger-shaped file functioning the same way Open_Gaps_Tracking.md
    and a `*_Decision_Log.md` do (an append-only record cited by other
    documents rather than restated) under a different name - same
    reasoning as `_is_gaps_ledger`/`_is_decision_log`, for two sibling
    shapes each confirmed by reading the file's own stated content:
    `NEEDS-RULING.md` (`_cross-world`'s own open-items ledger, structurally
    identical to Open_Gaps_Tracking.md) and a Doc_0X `*_Superseded_
    Claims.md` companion ("Entries record what was claimed, what is wrong
    with it, and which review round established that" - a dedicated
    correction-history record for one document, the same role a Decision
    Log plays for a whole world). Scanning either for the same patterns a
    construction document is held to would flag their own required,
    designed shape as leaked commentary.

    Deliberately does NOT include a generic `*_LEDGER.md` suffix - tried
    for `CAPPADOCIAN_BUILD_LEDGER.md` (a batch review's own suggestion)
    and dropped: the existing hand-labelled sample already carries
    counter-evidence at `CAPPADOCIAN_BUILD_LEDGER.md:463`, a genuine
    still-open verification note, not designed ledger content - unlike
    NEEDS-RULING.md/Superseded-Claims, this file mixes real narrative in
    with its ledger entries and cannot be blanket-exempted."""
    parts = rel.parts
    if len(parts) < 3 or parts[0] != "Build" or parts[1] != "worlds":
        return False
    return bool(_BUILD_LEDGER_FILENAME.search(parts[-1]))


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


_DECISION_LOG_FILENAME = re.compile(r"(?i)decision[-_]log\.md$")


def _is_decision_log(rel: Path) -> bool:
    """A per-world (or fleet-level) decision log under Build/worlds/ - e.g.
    lpc_Decision_Log.md, CiC_W7_Decision_Log.md, LIBRARY-DECISION-LOG.md.
    Same reasoning as _is_gaps_ledger, just for a sibling kind of ledger:
    confirmed live against lpc_Decision_Log.md's own header ("This log
    holds project-lead decisions, escalation resolutions, and revision
    rationale for this world's build, so the construction documents
    themselves stay clean, substantive content") - the file exists
    specifically so dated, review-round, project-lead-attributed history
    doesn't have to live in the construction documents it explains. Not a
    construction document itself, so scanning it for the same patterns a
    construction document is held to would flag its own required shape as
    leaked commentary, the same mistake _is_gaps_ledger already guards
    against for the gaps ledger."""
    parts = rel.parts
    return len(parts) >= 3 and parts[0] == "Build" and parts[1] == "worlds" and bool(_DECISION_LOG_FILENAME.search(parts[-1]))


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


def _is_doc_construction_file(rel: Path) -> bool:
    """Any .md file under Build/worlds/<code>/ - the canonical per-world
    construction documents and their siblings (Source_Registry.md,
    Representative Phase/Ecology/Validation/Construction-Notes/Identity-
    Decision files, Force/Story Index, Claims/Superseded-Claims Register,
    Coverage-Check, Scope-and-Source-Acquisition-Manifest, ...) CLAUDE.md
    names under "Keep the live/canonical surfaces clean".

    This was originally filename-gated to bare Doc_0[1-9]_*.md, on the
    documented grounds that alx/don/ijc/lpc/rzg/syr share that filename
    shape but hal/gallic/witt/cappadocian's own world-prefixed variants
    (hal_Doc_01_..., gallic_Doc07_..., witt_Doc_01_...,
    cappadocian_Doc_01_...) don't, and extending the filename match there
    would have been guessing rather than verifying. That guess is no
    longer needed: six independent verification passes (one per
    Build/worlds/ batch in the 2026-09-26 fleet-wide narrative cleanup),
    each re-implementing this function's own protected-lines algorithm
    and diffing it against every real hit by hand before touching
    anything, confirmed the identical load-bearing Status-header/tail
    pattern in every prefixed-naming world surveyed (hal, gallic, witt,
    cappadocian, pahc's own CiC_W1_Doc0N_..._FINAL.md, desert's own
    CiC_W3_Doc01_...md) AND in every one of the sibling document types
    named above, none of which share a single fixed filename shape either.
    Given that much independent confirmation that filename was never the
    right signal, this now protects by content alone (the header-field and
    tail-heading checks below, both already narrow and independently
    verified clean by that same survey) across every file the surface
    covers, rather than maintaining a filename allowlist that a seventh
    world would just as easily miss again."""
    parts = rel.parts
    return (
        len(parts) >= 4
        and parts[0] == "Build"
        and parts[1] == "worlds"
        and rel.suffix == ".md"
    )


# A bold field-label opening a line, e.g. "**Status:**", "**Produced
# at:**", "**World file-code (provisional):**" - deliberately narrow
# (letters/digits/space/parens/hyphen only between the asterisks and the
# colon) so it does NOT match a header's own free-prose disclosure
# paragraphs, which use full sentences and so carry an apostrophe, a
# comma, or other punctuation this class excludes - e.g. ijc Doc_04's
# "**Note on this document's own place in this project's methodology:**"
# or ijc Doc_05's "**Writing-From-Inside note, stated accurately:**".
# Those stay flagged like any other prose; only a genuine short
# field-name line is protected.
_DOC_HEADER_FIELD_RE = re.compile(r"^\*\*([A-Z][\w /()\-]*):\*\*")

# A label the punctuation filter above lets through (no comma or
# apostrophe) but that is still a changelog entry, not a metadata field -
# found once _is_doc_construction_file's scope widened past the bare
# Doc_0X sample it was tuned against: "**Revision 2 (2026-07-09):**"/
# "**Revision 3...**" (pahc, literal numbered changelog entries -
# "Revision history:" itself, naming no number, is a real field and stays
# protected), "**Schema note:**" (gallic, opens "This claim was made
# falsely twice before it was true..."), "**Filename note:**" (don),
# "**Terminology note carried forward from this drafting pass:**"
# (desert), "**Note on...:**" (ijc - the punctuation filter's own worked
# example in the comment above was itself a false negative for a label
# with no internal comma).
_DOC_HEADER_FIELD_NARRATIVE_LABEL_RE = re.compile(
    r"(?i)^(revision\s+\d|schema note|filename note|terminology note\b|note on\b|correction\b|addendum\b)"
)

# Any heading (## or deeper) that starts or continues this project's own
# tail administrative block - every wording actually found across the
# surveyed sample: "Open Items and Handoff" (alx), "Handoff and Open
# Items" (don), "Open items carried forward [to later steps]" (ijc/witt/
# rzg), "Open Issues Flagged for Downstream Documents" (hal-style),
# "Document Log" / "Document log" (gallic, witt, lpc - where the
# disagreement log and escalation check actually live, one heading after
# "Open Items"), "Disposition" / "Review and Disposition" / "Overall
# Disposition" (ijc, hal, rzg, lpc, don). A document with none of these
# headings (lpc's Doc_08, syr's Doc_09) matches nothing here - correctly:
# there is no tail block to protect.
#
# Anchored to where the heading's own title starts (after an optional
# leading number/"Section N"/"Part N" and an optional "Overall"/"Final"/
# "General") or ends - not a bare substring search anywhere in the
# heading. An unanchored version, tuned against the bare Doc_0X sample,
# over-matched once applied fleet-wide: a heading merely *mentioning* one
# of these words mid-title - "## 4. Deeper Dynamic Encounter Validation
# Exchange (addresses Open Item 8)" (syr), "## ADDENDUM (2026-07-19,
# System Hub) - the Facilitator-handoff mechanism now exists" (pahc),
# "## 5. Overall Disposition (REWRITTEN per independent review)" (don) -
# is not itself a tail section, and hid real body narrative underneath it
# ("Correction made during revision after Round 1 review..." in syr's
# case).
# Three more synonyms found once the survey above widened past its
# original alx/don/ijc/lpc/rzg/syr sample, each individually confirmed
# real by reading the file, not guessed from the name alone: "Revision
# Log" (witt/hal, cappadocian, syr, lpc's Representative Phase docs and
# lpc_World_Profile's own "World Profile Completion Status" heading -
# the same disagreement-log/escalation content "Document Log" already
# names, under this world-family's own preferred wording instead),
# "Document Status" (hal's own Facilitation Brief), "Completion
# Certification"/"Completion Status" (witt Doc_08's "Doc_08 Completion
# Certification", lpc's "World Profile Completion Status"), "Open
# Questions" (a third variant alongside "Open Items"/"Open Issues"), and
# "Revision Triggers" as a closing phrase (cappadocian/desert's "Open
# Questions, Revision Triggers, and Decisions Requiring the Project Lead").
#
# "Coverage limits" was tried (witt_Doc_03_Lexicon_Candidate_List.md's own
# "## 12. Coverage limits" heading) and dropped: unlike the headings above,
# that section is not administrative tail-tracking at all - it is real,
# load-bearing audit-finding content woven into the document's own
# argument ("The audit found the Papacy at Rome item and four more items
# making the same 'in full' overclaim..." at line 732), the same genre as
# a Doc_08 "Discipline N" section, which this checker never protects. A
# batch review's own framing ("witt Doc_03's own dated coverage-limits
# section... a checker gap") assumed this without reading the section;
# reading it shows the opposite.
_HEADING_NUMBERING_PREFIX_RE = re.compile(
    r"(?i)^(?:\d+(?:\.\d+)*\.?\s+|section\s+\d+\s*[-—:]\s*|part\s+\d+\s*[-—:]\s*)"
)
_DOC_TAIL_HEADING_START_RE = re.compile(
    r"(?i)^(?:overall\s+|final\s+|general\s+)?(?:open items?|open issues?|open questions?|"
    r"handoff|document log|document status|disposition|review and disposition|"
    r"revision log|completion status|completion certification)\b"
)
_DOC_TAIL_HEADING_END_RE = re.compile(
    r"(?i)(?:open items?|open issues?|open questions?|handoff|document log|document status|"
    r"disposition|revision log|completion status|completion certification|"
    r"revision triggers)$"
)


def _is_doc_tail_heading(heading_text: str) -> bool:
    stripped = _HEADING_NUMBERING_PREFIX_RE.sub("", heading_text).strip()
    return bool(_DOC_TAIL_HEADING_START_RE.match(stripped) or _DOC_TAIL_HEADING_END_RE.search(stripped))


# The labels a per-section identification block carries, read off every
# such block in the fleet (Doc_07's "Section 1 — Document Identity and
# Confirmed Inputs", Doc_08/Doc_09's "Section 1 — World Identification",
# the World Profile's "Section 1 — World Identity", a Phase 6 brief's own
# header block): the world's name and code, the Representative's name, the
# builder or branch, when it was produced, and any date or upstream-
# document version ("Doc_08 completion date", "Date of World Profile
# completion", "Doc_02 (Source Ecology) version this analysis draws
# from"). Nothing else. Templates across the fleet use the same bold-label
# shape for analytical content fields too - "Temporal scope", "Primary
# sources of authority", "Register derivation", "Strand attribution",
# "What external scholarly review should focus on", a lexicon entry's
# "Ecological Function", a story's "Tier justification" - often two or
# more in a row straight after a heading. Those are the document's
# substance, not its metadata, and stay scanned like any other prose.
_SECTION_METADATA_LABEL_RE = re.compile(
    r"(?i)^(?:world name\b|world code$|representative name$|builder$|branch$|produced$|"
    r"template version$|.*\b(?:date|version)\b)"
)


def _post_heading_header_field_lines(lines: list[str]) -> set[int]:
    """A per-section metadata block: a run of `_DOC_HEADER_FIELD_RE` lines
    (tolerating one blank line between siblings, matching this repo's own
    convention of one blank line between fields) starting right after a
    heading (## or deeper), carrying at least 2 fields whose label is
    identification/provenance metadata (`_SECTION_METADATA_LABEL_RE`) -
    the same header-field convention `_doc_construction_protected_lines`'s
    own top-of-file scan already protects, repeated after a LATER section
    heading rather than only at the document's very top. Example:
    witt_Doc_08_Forces_Document.md's "## 1. Section 1 — World
    Identification", followed by World name/World code/Representative
    name/Doc_08 completion date/Builder/Doc_02 version/Doc_04 version,
    well past the top header's first `---`.

    Only the metadata-labelled lines in the run are protected; a content
    field sitting in the same run (a World Profile's "Temporal scope" or
    "Community character" between its "World code" and "Builder") is not.
    A run is walked past such content fields, not stopped at them, since
    the World Profile template puts its Builder/Date fields after them.

    At least 2 metadata fields are required: a single field-shaped bold
    lead ("**What it is not:**", "**Registry cross-reference:**") is never
    a metadata block on its own."""
    heading_re = re.compile(r"^(#{2,})\s+(.*)$")
    protected: set[int] = set()
    n = len(lines)
    for i, line in enumerate(lines):
        if not heading_re.match(line):
            continue
        j = i + 1
        metadata_run: list[int] = []
        blanks_in_a_row = 0
        while j < n and blanks_in_a_row <= 1:
            stripped = lines[j].strip()
            if stripped == "":
                blanks_in_a_row += 1
                j += 1
                continue
            field_match = _DOC_HEADER_FIELD_RE.match(lines[j])
            if field_match and not _DOC_HEADER_FIELD_NARRATIVE_LABEL_RE.match(field_match.group(1)):
                if _SECTION_METADATA_LABEL_RE.match(field_match.group(1).strip()):
                    metadata_run.append(j)
                blanks_in_a_row = 0
                j += 1
                continue
            break
        if len(metadata_run) >= 2:
            protected.update(idx + 1 for idx in metadata_run)
    return protected


def _doc_construction_protected_lines(rel: Path, text: str) -> set[int]:
    """Line numbers of a Doc_0[1-9] construction document's own inline
    review-status tracking - decided directly with Mark: this is
    load-bearing build-cycle pipeline state (`cic-build-cycle`, CLAUDE.md's
    "Scaling the build"), not narrative drift to be cleaned, and a fuller
    companion-file migration of it is a separate, later project, not this
    one. Survey of 8+ files across alx/don/ijc/lpc/rzg/syr, multiple Doc
    numbers, found no single fixed heading and no fixed two-field header,
    so this protects at line/heading level rather than by a blanket file
    or whole-header-block skip - any other narrative in the same file (a
    header's own free-prose disclosure paragraph, a mid-document aside)
    stays flagged exactly as before:

    1. A header metadata line matching _DOC_HEADER_FIELD_RE, plus that
       field's own continuation lines. This repo's actual convention is
       one field per single, often very long, physical line; continuation
       handling is defensive, for a field that does wrap. A run stops at
       the next field-label line, a blank line, or a `---` divider.
       Bounded to before the file's first `---` divider (found within the
       first 40 lines - every surveyed file has one there) or, failing
       that, a defensive 15-line cap.
    2. The tail administrative block: any heading (## or deeper) matching
       _is_doc_tail_heading, protected to the next heading of the same or
       shallower level, or EOF. Two such headings in a row (an "Open
       Items" section immediately followed by a separate "Document Log"
       holding the disagreement log and escalation check - the actual
       gallic Doc_07 shape) each start their own run, so both are
       covered.
    3. A per-section metadata block later in the document (see
       _post_heading_header_field_lines) - the same header-field
       convention as (1), repeated right after a later heading rather than
       only at the document's own top, found live in witt Doc_08's own
       "## 1. Section 1 — World Identification" block (its own completion-
       date/version fields, well past the top header's first `---`).
    """
    if not _is_doc_construction_file(rel):
        return set()

    lines = text.splitlines()
    protected: set[int] = set()
    protected |= _post_heading_header_field_lines(lines)

    # 1. Header metadata fields (plus continuation lines).
    header_end = next(
        (i for i, line in enumerate(lines[:40]) if line.strip() == "---"),
        min(15, len(lines)),
    )
    i = 0
    while i < header_end:
        field_match = _DOC_HEADER_FIELD_RE.match(lines[i])
        if field_match and not _DOC_HEADER_FIELD_NARRATIVE_LABEL_RE.match(field_match.group(1)):
            protected.add(i + 1)
            # Continuation lines, for a field whose value wraps - this
            # repo's actual convention is one field per single (often very
            # long) physical line, so this rarely if ever fires; it stops
            # at a blank line, a `---` divider, OR any line starting with
            # "**" - not only one matching the narrow field-label shape.
            # That second check matters: a header's own free-prose
            # disclosure paragraph also opens with a bold lead (e.g. ijc
            # Doc_04's "**Note on this document's own place in this
            # project's methodology:**"), and must end this field's run
            # rather than being swept into it - it gets its own, separate
            # (and correctly negative) test against the field-label regex
            # on the next outer iteration.
            j = i + 1
            while (
                j < header_end
                and lines[j].strip() not in ("", "---")
                and not lines[j].lstrip().startswith("**")
            ):
                protected.add(j + 1)
                j += 1
            i = j
        else:
            i += 1

    # 2. Tail administrative block(s), heading-keyword driven.
    heading_re = re.compile(r"^(#{2,})\s+(.*)$")
    headings = []  # (0-indexed line, level, heading text)
    for idx, line in enumerate(lines):
        m = heading_re.match(line)
        if m:
            headings.append((idx, len(m.group(1)), m.group(2)))

    for pos, (idx, level, htext) in enumerate(headings):
        if not _is_doc_tail_heading(htext):
            continue
        end = len(lines)
        for idx2, level2, _ in headings[pos + 1:]:
            if level2 <= level:
                end = idx2
                break
        for k in range(idx, end):
            protected.add(k + 1)

    return protected


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
    if (
        _is_review_doc(rel)
        or _is_world_build_dir(rel)
        or _is_gaps_ledger(rel)
        or _is_decision_log(rel)
        or _is_build_ledger(rel)
        or _is_engine_report(rel)
    ):
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


def classify_line(
    line: str,
    matched: list[str],
    in_source_record_body: bool = False,
    in_source_registry_file: bool = False,
) -> str:
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
                or _iso_date_is_bare_table_provenance(line, in_source_registry_file)
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

    in_source_registry_file = bool(_SOURCE_REGISTRY_FILENAME.search(rel.name))
    protected_field_lines: set[int] = set()
    spoken_field_lines: set[int] = set()
    source_record_body_lines: set[int] = set()
    # Computed for every file, not just records/: cheap (an immediate
    # return when the file has no leading `---`), and needed fleet-wide
    # below for change-history widening, not only for records/'s own
    # PROTECTED-field/spoken-field logic.
    frontmatter_field_lines, record_type = _front_matter_field_lines(text)
    if path.suffix == ".md" and rel.parts[0] == "records":
        protected_field_lines = _protected_record_field_lines(frontmatter_field_lines, record_type)
        spoken_field_lines = _spoken_field_lines(frontmatter_field_lines, record_type)
        source_record_body_lines = _source_record_body_lines(text, record_type)
    protected_field_lines |= _doc_construction_protected_lines(rel, text)

    # A change-history cue inside a YAML front-matter block widens only to
    # its own top-level key's lines (_yaml_scalar_block_lines) - front
    # matter has no blank lines between sibling keys, so the ordinary
    # blank-line paragraph widening would otherwise flood every unrelated
    # sibling field. A cue outside front matter (the record's own body
    # prose after the closing `---`, a file with no front matter at all,
    # plain Markdown, a Python/JS comment, ...) still widens by
    # _paragraph_lines, unchanged.
    frontmatter_end = _yaml_frontmatter_end(raw_lines)
    change_history_block_lines: set[int] = set()
    for i, line in enumerate(raw_lines, start=1):
        if CHANGE_HISTORY_CUES.search(line):
            if frontmatter_end is not None and i <= frontmatter_end:
                change_history_block_lines.update(_yaml_scalar_block_lines(frontmatter_field_lines, i))
            else:
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
            category = classify_line(line, matched, i in source_record_body_lines, in_source_registry_file)
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


def surface_of(rel: Path) -> str | None:
    """The scan surface a repo-relative path belongs to, if any."""
    rel_s = rel.as_posix()
    for surface, roots in SURFACES.items():
        if any(rel_s == root or rel_s.startswith(root + "/") for root in roots):
            return surface
    return None


def changed_files(repo: Path, base: str) -> list[Path]:
    """Files added or modified since the merge-base with `base`, working
    tree included, plus untracked files. Deleted files carry no commentary."""
    def git(*args: str) -> str:
        return subprocess.run(["git", *args], cwd=repo, check=True, capture_output=True, text=True).stdout

    merge_base = git("merge-base", base, "HEAD").strip()
    names = git("diff", "--name-only", "--diff-filter=ACMR", merge_base).splitlines()
    names += git("ls-files", "--others", "--exclude-standard").splitlines()
    return sorted({repo / n for n in names if n})


def run_changed(repo: Path, files: list[Path]) -> list[Hit]:
    hits: list[Hit] = []
    for path in files:
        rel = path.relative_to(repo)
        surface = surface_of(rel)
        if surface is None or not path.is_file():
            continue
        if any(part in SKIP_DIR_NAMES for part in rel.parts):
            continue
        if path.suffix in SKIP_SUFFIXES or path.suffix not in TEXT_SUFFIXES:
            continue
        hits.extend(scan_file(repo, path, surface))
    return hits


BLOCKING_CATEGORIES = ("REWRITE", "ROUTE")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--surface", choices=sorted(SURFACES), default=None)
    parser.add_argument("--json", type=Path, default=None)
    parser.add_argument("--base", default=None, help="scan only files changed since the merge-base with this git ref")
    parser.add_argument("--enforce", action="store_true", help="exit 1 when a scanned file carries REWRITE or ROUTE lines (needs --base)")
    args = parser.parse_args(argv)
    if args.enforce and not args.base:
        parser.error("--enforce needs --base: the rule is scoped to the files a change edits")

    if args.base:
        surfaces = [args.surface] if args.surface else sorted(SURFACES)
        hits = [h for h in run_changed(REPO, changed_files(REPO, args.base)) if h.surface in surfaces]
    else:
        surfaces = [args.surface] if args.surface else sorted(SURFACES)
        hits = run(REPO, surfaces)

    counts: dict[str, dict[str, int]] = {}
    for hit in hits:
        counts.setdefault(hit.surface, {"KEEP": 0, "REWRITE": 0, "ROUTE": 0, "PROTECTED": 0})
        counts[hit.surface][hit.category] += 1

    scope = f"files changed since the merge-base with {args.base}" if args.base else "whole tree"
    print(f"Live-surface commentary scan ({scope}; see tools/check_live_commentary.py)\n")
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

    blocking = [h for h in hits if h.category in BLOCKING_CATEGORIES]
    if args.enforce and blocking:
        print(f"\n{len(blocking)} REWRITE/ROUTE line(s) in files this change edits: remove the commentary "
              "(rewrite the reason in plain present tense; move provenance to Build/Ministry, open items to "
              "Open_Gaps_Tracking.md).", file=sys.stderr)
        for hit in blocking:
            print(f"  {hit.row()}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
