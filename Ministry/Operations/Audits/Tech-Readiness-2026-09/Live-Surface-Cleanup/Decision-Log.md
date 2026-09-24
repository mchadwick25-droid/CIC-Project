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

**Round 3 (managing-thread verdict, FAIL round 2, one round left under the
three-round cap):**

Round 2 only removed the tokens the checker patterns themselves catch
(dates, ruling numbers); a comment could still narrate what used to be
true, in plain prose the checker has no pattern for. Round 3 is a full
manual second pass, file by file, on that question - not just the seven
spots the verdict's own (non-exhaustive) grep found.

1. `templates/tradition.html`: the "was cut in the card redesign" history
   on the safety-disclosure comment (spliced into all 11
   `traditions/*.html`); "Two sections that used to run here are gone
   outright" in the header comment; "not the old 3-section page" in the
   opening line; and "no section of their own in the old hand-built
   pages" on the glossary/pull-quotes comment. All four restated as
   present-tense fact; template fixed once, `traditions/*.html`
   regenerated.
2. `index.html`, `assets/style.css`: "was width:100%;aspect-ratio:16/7",
   "was min(60vh,480px)", "now part of the single header row" (both
   copies), "that was tried with equal flex-grow..." (the menu-centering
   comment), and "the card was as wide as or wider than its own mobile
   scroll container... nothing... ever showed" (the chair-peek comment,
   rewritten to the hypothetical it's guarding against, not a past
   state).
3. `atlas-v3.html`: by far the largest share of this round - roughly 25
   separate comments narrating a prior layout, a rejected alternative, or
   a fixed bug, on the header-gutter sizing, the era-divider block (a
   second location round 2 missed, plus a still-remaining "not the old
   thick bar" phrase in the one round 2 did fix), the per-river research
   note ("Mark asked for" attribution), the FAM color array's dated
   addition note, the dark-mode default-detection comment, the
   width-floor/merge-window/smoothstep river-rendering trio, the built-
   world label-collision trio (a first-attempt-and-revert narrative
   condensed to just the one surviving correction), the seam-mark-dot
   fix, the orientation-fetch race-condition note (dropped the specific
   "found by loading X in a browser, it threw Y" debugging story, kept
   the mechanism), the panel-content and status-pill removal notes, the
   focus-management note, the initial-zoom-floor note, the pointer-
   capture rationale, and the scope-note positioning note. Every one
   restated as the current design plus the (hypothetical, present-tense)
   problem it avoids, not a past-tense account of what broke or what an
   earlier version did. Three color-derivation methodology paragraphs
   (how the FAM hues and the dark-mode edge-opacity constant are
   computed, using "was" as part of describing a still-true derivation
   method, not a superseded value) were read closely and left alone -
   they don't say what used to be true, they say how the current value is
   derived, which remains true.
4. `talk.html`: "used to fall back to its pre-redesign Launch screen"
   rewritten to the current behavior only.
5. `pilot-feedback.html`: two spots from round 2's own re-reading (the
   mailto-vs-form-POST comment's own "Was action=... ALONE" opening, and
   "the mailto rebuild above was written to fix") - both restated as
   current behavior and reason.
6. `support.html`: "Text only for now" removed outright (stale - real
   checkout is live, stated in the very next sentence); ".fine-print...
   the fix that was already sitting right there" restated as present
   tense.
7. `assets/logo-arriving.svg`: "Opening widened to +/-50deg (was
   +/-40)" restated as the current angle alone.

Checked and left alone as real content, not commentary: the "chair" tile
descriptions on `index.html` and every `traditions/*.html`/`tree/*.html`
page (real historical prose - Alexandria's teachers, Donatism's rival
bishops, Wittenberg's theses - which legitimately narrates past events
in past tense); `support.html`'s "Pending review before this is treated
as final" (a real, still-open item, not settled history);
`README.md`'s "before this goes fully public" (a genuine forward-looking
TODO); `empire.svg`'s "was considered and held in reserve" and
`syriac.svg`'s "the old 'girdle'" (a rejected design alternative and a
historical garment term, neither project history).

Re-validated: `check_live_commentary.py --surface cic-website` → 1 hit
(unchanged, the documented KEEP false positive); `check_no_embedded_world_data.py`
→ exit 0; `check_paths.py` → 0 new/retired; `node tools/validate-census.mjs`
→ 0 errors, 292/69/10 unchanged; both JSON payloads (`world-census.json`,
`atlas-v3.html`'s embedded copy) parse; `pytest
tools/tests/test_check_live_commentary.py` → 81/85 passed, the 4
failures all `cic-poc/frontend` (PR #503's own surface, not this PR's -
full output:

```
FAILED tools/tests/test_check_live_commentary.py::test_hand_label_present[cic-poc/frontend/src/components/VoiceTurnBody.test.tsx-170-REWRITE]
FAILED tools/tests/test_check_live_commentary.py::test_hand_label_present[cic-poc/frontend/src/components/StoryMark.tsx-15-REWRITE]
FAILED tools/tests/test_check_live_commentary.py::test_hand_label_present[cic-poc/frontend/src/components/StoryMark.tsx-16-REWRITE]
FAILED tools/tests/test_check_live_commentary.py::test_precision_and_recall_on_hand_labelled_sample
4 failed, 81 passed in 0.87s
```
).

**Round 3 verdict: PASS**, with one remaining line flagged: `atlas-v3.html`
line ~40695, "0.55 (Mark, live-site review) blended graphite down to
within a few steps..." carried an attribution the checker's own regexes
don't catch (no ISO date, no ruling number). Fixed: dropped the
attribution and restated the rejected 0.55 alternative in the
conditional ("would blend...") alongside the kept reasoning for 0.78,
matching the same rejected-alternative pattern already used and kept
elsewhere in this file (e.g. `empire.svg`'s dalmatic alternative).
Re-validated: `check_live_commentary.py --surface cic-website` → 1 hit
(unchanged, the documented KEEP false positive); `check_no_embedded_world_data.py`
→ exit 0; `check_paths.py` → 0 new/retired; `node tools/validate-census.mjs`
→ 0 errors, 292/69/10 unchanged.

---

## Entry 2 — cic-poc/frontend/ (Step 2, surface 2 of 6)

`tools/check_live_commentary.py
--surface cic-poc-frontend` read 48 hits before this PR (0 KEEP, 48
REWRITE) and 1 after (a checker false positive left open, see below). No
UI-facing string content was changed anywhere in this PR — every edit is
to a `/**...*/` or `//` code comment; every rendered string in
`src/data/worlds.ts`, `src/lib/confidence.ts`, `src/components/
Arrival.tsx`, and the citation-mark copy is untouched.

**Removed, by file (see this PR's diff for exact before/after text):**

- `src/app.css` — a "2026-09-17 dark-mode change order" date on the
  `:root` token comment and the a11y-sweep comment above it; `R9 (RULED
  a, 2026-09-21)` and `R10 (RULED c, 2026-09-21)` ruling numbers/dates on
  the citation-mark comments; `R16/R9`'s ruling-number cross-reference on
  the confidence-phrase comment; three further dated change-order
  comments (`2026-08-26` transparency audit, `2026-09-17` dark-mode
  error-background change, `2026-08-28` "Trust package"). Reason kept in
  every case (why the token/color/rule is shaped this way).
- `src/components/Arrival.tsx`, `Arrival.test.tsx` — `Stage 6e
  (Ministry/Features/Conversation-Transparency-Engine/Decision-Log.md)`,
  `R10`'s "label copy" citation, and "per Mark's own direction" removed
  from the header comment explaining why one sentence in the disclosure
  block is new prose rather than relocated. **The comment's open-status
  flag was kept, reworded from "DRAFT COPY, not yet Mark's own word" to
  "DRAFT COPY, not yet approved as final wording"** — this is a real,
  still-open item (the ✲-mark explainer sentence in `arrival__disclosure`
  is unconfirmed copy), not settled history, so it stays flagged in the
  file rather than being treated as resolved provenance to remove.
- `src/lib/confidence.ts` — same pattern: `Stage 6b (...Decision-Log.md,
  Entry 35 family)`, `R16 (RULED c, Decision-Log.md Entry 29)` removed;
  "DRAFT COPY - not yet worded by Mark... until Decision-Log.md records
  his own word on it" reworded to "DRAFT COPY - not yet approved as
  final wording... until it is confirmed" — same reasoning: `
  CONFIDENCE_PHRASES`' values are still-unapproved copy, a live open
  item, not history.
- `src/components/StoryMark.tsx`, `WitnessMark.tsx`,
  `VoiceTurnBody.tsx`, `VoiceTurnBody.legacy-default.test.tsx` — `R9`/
  `R10`/`R17` ruling-number cross-references, one `RULED c, 2026-09-21`
  date, one `Rulings-Pending.md, Decision-Log.md Entry 29` pointer, and
  `Decision-Log.md Entry 49`/`R10 and label copy both ruled, Mark's own
  read-through passed` removed from header/inline comments. Reason kept
  throughout (why a mark sits where it sits, why the drop-cap and
  tie-break rules are shaped as they are).
- `src/lib/flags.ts` — `R10`, `Rulings-Pending.md`, `Decision-Log.md
  Entry 41`, `Mark's own seeker read-through`, `Entries 46, 48, 49`
  removed from the header comment explaining why the flag now defaults
  ON; the functional explanation (what the flag does, why "off" is the
  only string that reverts it) is untouched.
- `src/screens/TableRoom.tsx`, `TableRoom.test.tsx` — `Decision-Log.md
  Entry 47 (2026-09-22)` removed from both comments describing the
  seat-identity guard's empty-text case.
- `src/data/worlds.ts` — nine separate dated comments (`2026-08-24`
  design-review date, `as of 2026-09-20`, `2026-09-17` dark-mode-order
  date x3, and four "world N, added/admitted/re-admitted `<date>`"
  per-world comments) — every one kept the "which world, in what order,
  why this color" reasoning and dropped only the calendar date.
- `src/hooks/useConversation.ts`, `src/lib/api.ts` — one dated
  parenthetical each (`2026-08-28 audit fix`, `2026-09-04` bug-fix
  date).

**Left open (1 remaining hit):** `src/components/FigureBridgeMark.tsx:3`
— cites `VR_1A_Transparency_Gap_2026-08-09.md`, a real file at
`Ministry/Operations/Audits/CiC_VoiceRebuild_Blueprint_2026-08-08/
decisions/` whose date is part of its actual filename, not a change-date
attached to prose. Rewording or dropping the date would break the
citation. Left unchanged; flagged for Cleanup 1 as a second candidate for
a bare-filename-citation carve-out (alongside the `reviewer`-pattern gap
already flagged in Entry 1).

One further false-positive fixed rather than left open: `src/app.css`'s
padded-hit-area comment read "the mark's own position:relative" —
`marks-word`'s pattern is case-insensitive and fired on the CSS term
"mark" (as in citation mark), nothing to do with Mark. Reworded to "the
citation mark's position:relative" — same meaning, no provenance to
preserve, so fixed outright rather than documented as an exception.

Validated: `check_live_commentary.py --surface cic-poc-frontend` → 1 hit
(was 48); `check_paths.py --baseline tools/check_paths_baseline.txt` → 0
new/retired; `check_no_embedded_world_data.py` → exit 0; `npx tsc
--noEmit` → 0 errors; `npm test` (vitest) → 31/31 passed, 6/6 files.
`npm run lint` fails on this branch with a pre-existing "ESLint couldn't
find a configuration file" error, unrelated to this PR's changes
(comment-only edits) — not fixed here, flagged for whoever owns
`cic-poc/frontend`'s tooling config.

---
