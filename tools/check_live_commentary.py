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
              Ministry/Operations/Audits/Tech-Readiness-2026-09/
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
    "worlds": ("worlds",),
    "cic-poc-frontend": ("cic-poc/frontend",),
    "cic-website": ("cic-website",),
    "reference": ("reference",),
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

# Cues that push an already-matched line to ROUTE instead of REWRITE: the
# line is naming something still open, not narrating a decided one.
ROUTE_CUES = re.compile(
    r"\b(TODO|FIXME|open question|open gap|open item|not yet (resolved|fixed|answered|acquired)|"
    r"unresolved|still (pending|open)|follow-?up (item|work|needed)|known (gap|issue|defect)|"
    r"needs? (a )?follow-?up)\b",
    re.IGNORECASE,
)

# A "round" hit that is not a review round (round-trip, round number, round
# up/down, a round object) - keeps review-round from over-firing on ordinary
# engineering prose.
NON_REVIEW_ROUND = re.compile(r"\bround[\s-]?(trip|number|up|down|robin|off)\b", re.IGNORECASE)

# ---------------------------------------------------------------------------
# PROTECTED - narrow, explained rules. No baseline file: see module
# docstring on why a baseline would let drift go quiet.
# ---------------------------------------------------------------------------

# Schema-defined source-provenance fields (reference/Redesign-Spec/
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


def _protected_record_field_lines(text: str) -> set[int]:
    """Line numbers (1-indexed) inside a record .md's YAML front matter
    that fall under a protected field's key or its own indented value
    block (a multi-line scalar, or a `text:` field while inside a
    `record_type: quote` file)."""
    lines = text.splitlines()
    protected: set[int] = set()
    if not lines or lines[0].strip() != "---":
        return protected
    end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
    if end is None:
        return protected
    is_quote = any(re.match(r"^record_type:\s*quote\s*$", ln.strip()) for ln in lines[1:end])
    active_field: str | None = None
    active_indent = -1
    for i in range(1, end + 1):
        line = lines[i - 1] if i <= len(lines) else ""
        m = _YAML_KEY.match(line)
        if m and len(m.group(1)) == 0:
            key = m.group(2)
            protected_here = key in PROTECTED_RECORD_FIELDS or key in PROTECTED_CONTENT_FIELDS
            protected_here = protected_here or (is_quote and key == "text")
            if protected_here:
                active_field, active_indent = key, 0
                protected.add(i)
            else:
                active_field, active_indent = None, -1
            continue
        if active_field is not None:
            if line.strip() == "" or (len(line) - len(line.lstrip(" ")) > active_indent):
                protected.add(i)
            else:
                active_field, active_indent = None, -1
    return protected


def _is_review_doc(rel: Path) -> bool:
    """worlds/<code>/... review documents (CLAUDE.md places reviews under
    worlds/ by design). Two real naming conventions found on disk: a
    dedicated `Review-Artifacts/` directory (alx, cappadocian, don, grkap,
    ...), or a loose file in the world's own root whose name contains
    "Review" (desert, gallic, hal, ...). Both covered; neither guessed."""
    parts = rel.parts
    if len(parts) < 3 or parts[0] != "worlds":
        return False
    if "Review-Artifacts" in parts:
        return True
    return "review" in parts[-1].lower()


def _is_world_build_dir(rel: Path) -> bool:
    parts = rel.parts
    return len(parts) >= 3 and parts[0] == "worlds" and parts[2] == "build"


def _is_gaps_ledger(rel: Path) -> bool:
    """worlds/<code>/Open_Gaps_Tracking.md is the destination CLAUDE.md's
    own gap-tracking rule names for ROUTE findings, not a construction
    document itself - append-only, numbered, and explicitly expected to
    "cite subject + date" on every entry (CLAUDE.md, "Track gaps and
    exceptions explicitly"). Scanning it would flag the ledger's own
    required shape as if it were leaked commentary."""
    parts = rel.parts
    return len(parts) >= 2 and parts[0] == "worlds" and parts[-1] == "Open_Gaps_Tracking.md"


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


def classify_line(line: str, matched: list[str]) -> str:
    if ROUTE_CUES.search(line):
        return "ROUTE"
    real_matches = [
        name for name in matched
        if not (name == "review-round" and NON_REVIEW_ROUND.search(line))
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

    protected_field_lines: set[int] = set()
    if path.suffix == ".md" and rel.parts[0] == "records":
        protected_field_lines = _protected_record_field_lines(text)

    hits: list[Hit] = []
    for i, line in enumerate(text.splitlines(), start=1):
        matched = [name for name, pat in PATTERNS.items() if pat.search(line)]
        if not matched:
            continue
        if is_protected(rel, i, protected_field_lines):
            category = "PROTECTED"
        else:
            category = classify_line(line, matched)
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
