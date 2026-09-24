# Decision Log — Live-Surface-Cleanup

Append-only, per `CLAUDE.md`. This log is the destination for provenance
history removed from a live/canonical surface (`CLAUDE.md`, "Keep the
live/canonical surfaces clean") by the Live-Surface-Cleanup program:
ruling numbers, review rounds, reviewer names, "Mark's ruling"/"per Mark"
attributions, and dated change narration that `tools/check_live_commentary.py`
classifies as REWRITE. One entry per removal, citing what was removed,
where it moved from, and the PR that moved it. The fuller reasoning for
each PR lives in that PR's own body; this log is the pointer a removed
line's provenance is still findable from, per the launch brief's own rule
("Every removed line must be findable there, or in a gaps file,
afterwards").

No entries yet: Step 1 PR A builds the classifier only and edits nothing
in a live surface. The first entries land with Step 2 PR C/D.

---

## Entry 1 — cic-website/ (Step 2, surface 1 of 6)

`tools/check_live_commentary.py --surface cic-website` read 260 hits
before this PR (0 KEEP, 256 REWRITE, 4 PROTECTED) and 1 after (see "Left
open" below). Every REWRITE line's functional reason was kept, rewritten
in plain present tense, in place; the provenance below is what moved out.
Regenerated `cic-website/tree/*.html` (`tools/generate_tree_pages.mjs`)
and `cic-website/traditions/*.html` (`tools/generate_tradition_pages.py`)
after editing their sources so generated output matches.

**Removed, by file (see this PR's diff for exact before/after text):**

- `cic-website/index.html`, `table.html`, `assets/style.css`,
  `traditions/*.html` (shared header/nav chrome) — ~18 CSS/HTML comments
  citing "Mark, 2026-09-18/19" with direct quotes ("can you center them",
  "add a fade at the bottom", "add a peek of the next card", etc.) behind
  the site header/menu, chairs gallery, feature-card, and video-loop
  design decisions. Reason kept (why the CSS is shaped this way); the
  attribution and date removed.
- `cic-website/support.html` — the largest single removal: a ~167-line
  top-of-file comment logging five-plus revision passes on the cost
  section and Payment Link setup ("Replaced 2026-08-06", "SUPERSEDED
  2026-08-25", "CORRECTED 2026-08-26", "Revised... second/third/fourth
  pass", direct Mark quotes throughout), plus a second ~30-line inline
  revision comment in the cost `<section>`. Condensed to the current
  state and reasoning only (what the two Stripe Payment Links are, why
  the cost section deliberately carries no dollar figure). Full passes
  already lived in `Ministry/Features/Funding-Strategy/` — this removal
  stops duplicating that history in the live file, not deletes it.
- `cic-website/README.md` — "Removed from nav again 2026-09-19 (Mark,
  direct instruction)", "Academic Review Fund dropped 2026-08-25 (Mark,
  direct instruction)", and a "Resolved, 2026-07-21" bullet documenting a
  since-settled contact-email decision (removed outright as a stale
  "known follow-up," not moved — the current mailbox is already visible
  in every page's own contact link).
- `cic-website/data/world-census.json` (and the identical strings
  duplicated in `atlas-v3.html`'s own embedded `DATA` copy — see "Flagged,
  not fixed" below) — one `meta.generated` timestamp; a dated clause in
  `meta.notes`; 8 `stepStatus` era fields reading "era FROZEN by Mark
  <date>"; and a repeating `statusDescription`/edge-`note` trailer,
  "Added/ADOPTED/Edge written at the Era N gate/Freeze (Mark, <date>)",
  on ~50 movement and edge records across Eras 3, 4, 6, 9, and 10. Two
  records also had "per Mark's two-world steer" / "per Mark's mandate"
  reworded inline (`split at 843, treated as two separate worlds`; `per
  the grading mandate`). Every instance dropped only the `(Mark,
  <date>)` parenthetical or personal-attribution phrase; the surrounding
  status sentence (e.g. "Added at the Era 4 gate") is untouched.
- `cic-website/atlas-v3.html` — beyond the census-mirrored fields above:
  one CSS comment citing "2026-09-17... see the Decision-Log"; a
  three-round revision narrative on the era-divider line ("Mark,
  2026-09-17: the old break band...", two further "Mark's next report"
  passes) condensed to one paragraph describing the current design; and
  five further single-line date/quote removals (HEADER_GUTTER,
  ERA_CONTEXT_WRAP, the Part 3 cutover note, the source-registry note,
  pointer-capture and manual-pan-controls comments, and
  `positionScopeNote`'s feature-bar note).
- `cic-website/templates/tradition.html` — "project owner's ruling
  2026-09-19" / "2026-09-21" from the header comment and the two inline
  comments this template splices into all 11 built worlds' own
  `traditions/*.html` pages (the safety-disclosure note and the
  glossary/pull-quotes placement note); fixed once here rather than
  per-page, then regenerated.
- `cic-website/assets/world-icons/{alexandria,bethlehem,desert,empire,
  house-churches,syriac}.svg`, `assets/logo-arriving.svg` — version-
  history logs (V0.1 DRAFT → V1.8 LOCKED iteration notes), "Mark
  approved 2026-07-18" / "Mark's call" attributions, and direct quotes
  ("this actually looks great, lets lock this for now"). All DOCUMENTED/
  INFERENCE grounding notes (what's attested vs. inferred, and why) were
  kept verbatim — only version-iteration and approval narrative moved.
  Outside `check_live_commentary.py`'s scope (it skips `.svg`), fixed
  per the launch brief's own naming of these files.
- `cic-website/assets/orientation-render.mjs`, `story.html`,
  `pilot-feedback.html`, `talk.html`, `atlas.html`, `world-atlas.html` —
  one dated clause each (design-approval date, a page-migration date, a
  dark-mode-fix date, a form-reliability fix date, an iframe-bug date, a
  page-redirect date).

**Left open (1 remaining hit):** `support.html:127` — "external
reviewer" in "If you know a seminary, professor, or scholar who might
serve as an external reviewer, introduce us." This is participant-facing
copy about wanting an academic reviewer for the project's own scholarship,
not narration of this project's internal review process; the checker's
`reviewer` pattern has no carve-out for that context (unlike its `round`
and `iso-date` patterns, which do exclude non-review "round" usages and
bare-date fields). Left unchanged rather than reworded, since this PR
does not touch participant-facing wording without real review. Flagged
for Cleanup 1 as a candidate pattern refinement, and for Mark as a
"Words for Mark" item if a rewording is wanted instead.

**Flagged, not fixed (outside this program's scope):**
- `atlas-v3.html` embeds its own `const DATA = {...}` copy of
  `world-census.json` (`tools/check_no_embedded_world_data.py`'s own
  documented, already-baselined anti-pattern — its migration to fetching
  at runtime is a separate, later Website V2 stage). That embedded copy
  is measurably **stale**: `liveCount: 7` vs. `world-census.json`'s
  `liveCount: 11`, and different `statusCounts` — the live map may be
  under-representing built worlds. This is a data-accuracy defect, not
  commentary, so it's out of scope for this cleanup PR; both copies
  received the identical provenance-removal treatment (independently,
  since they already diverge) so neither carries stale REWRITE hits, but
  the underlying staleness is unresolved and worth its own fix.
- `tools/tests/test_check_live_commentary.py`'s hand-labelled sample
  cites specific `cic-website` line numbers (and `cic-poc/frontend` ones,
  untouched by this PR) as known REWRITE examples; cleaning those exact
  lines makes 10 of those hand-labels stale (`python3 -m pytest
  tools/tests/test_check_live_commentary.py` now fails). Not currently
  wired into CI (`.github/workflows/ci.yml` runs the checker itself,
  report-only, but not its pytest suite), so this does not block CI on
  this PR's head. Left for Cleanup 1 to refresh alongside each surface
  PR landing, per the checker's own docstring ("measures it before
  anything downstream... touches a single line").

Validated: `check_live_commentary.py --surface cic-website` → 1 hit (was
260); `check_no_embedded_world_data.py` → exit 0; `check_paths.py
--baseline tools/check_paths_baseline.txt` → 0 new/retired; `node
tools/validate-census.mjs` → 0 errors; `engine/m6/tests`,
`engine/m2/tests/test_site_{compiler,staleness}.py` → all green.
`cic-poc/frontend` untouched by this PR.

**Round 2 (managing-thread verdict, FAIL round 1, 2026-09-24):**

1. Round 1 only stripped the `(Mark, <date>)` parenthetical, leaving the
   surrounding process sentence itself on the live site: "Edge written at
   the Era 9 Freeze.", "Added at the Era 4 gate.", "ADOPTED at the Era 10
   Freeze.", and several mid-sentence variants ("banked at the Era 9
   gate", "written at the Era 9 gate", "made at the Era 9 gate", "ruled
   REGISTER over Outside-A4 at the Era 9 Freeze") — 105 occurrences
   across `world-census.json` and its 1 mirrored occurrence in
   `atlas-v3.html`'s embedded copy, plus the 7 already-regenerated
   `tree/*.html` pages. Removed the whole clause in every case, keeping
   the sourcing sentence before it (e.g. "Added at the Era 3 gate —
   proposed by the Era 3 Step 0 run..." → "Proposed by the Era 3 Step 0
   run..."). Four `statusDescription` fields carried nothing but the
   process clause itself, with the real status already stated in the
   sibling `statusWord` field — emptied to `""` rather than left
   half-sentence. `stepStatus` fields ("Step 0 run complete — era
   frozen") were left as-is per the verdict: they state current status,
   not process history. Regenerated `tree/*.html` from the fixed data.
2. Refreshed `tools/tests/test_check_live_commentary.py`'s 6 stale
   cic-website `HAND_LABELS` entries (all 6 pointed at lines this PR's
   round 1 had already cleaned). cic-website now has only one real
   remaining hit — hand-labelled `KEEP` (`support.html:127`, "external
   reviewer" — a checker false positive on real body copy about an
   academic reviewer, per the managing thread's own explicit ruling that
   this is not a Words-for-Mark item) — so the other 5 slots moved to
   fresh `cic/corpus-map` examples (untouched, stable) to keep the table
   at its required ≥60 real, currently-matching samples.
   `cic-poc/frontend`'s 3 stale entries are PR #503's own fix, not this
   PR's.
3. Registered `atlas-v3.html`'s stale embedded-census finding (liveCount
   7 vs. `world-census.json`'s 11) as a comment on its
   `tools/embedded-world-data-baseline.txt` entry — the baseline format
   supports `#`-prefixed comment lines (skipped by the loader, so the
   exclusion itself is unaffected). Not fixed here, per the verdict's own
   instruction ("Don't fix the migration here").

Re-validated: `check_live_commentary.py --surface cic-website` → 1 hit
(the documented KEEP false positive); `check_no_embedded_world_data.py`
→ exit 0; `check_paths.py` → 0 new/retired; `node
tools/validate-census.mjs` → 0 errors; `pytest
tools/tests/test_check_live_commentary.py` → 4 failures remaining, all
`cic-poc/frontend` (PR #503's own stale entries, not this PR's).

---
