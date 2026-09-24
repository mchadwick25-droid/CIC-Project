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

**Round 2 (managing-thread verdict, FAIL round 1, 2026-09-24):**

1. Round 1 only removed the ruling number/date token from each comment,
   leaving the surrounding sentence stating what USED to be true or
   naming a stage/ruling as the reason. Fixed throughout the PR's diff:
   - `Arrival.tsx` and `lib/confidence.ts`'s "DRAFT COPY, not yet
     approved" flags removed entirely (not reworded) - both are stale as
     of the Transparency Engine Decision-Log's own 2026-09-22 entries
     (Entry 39, Entry 41/the Arrival test's own PR #398 note): the
     Stage 6b confidence phrases and the ✲-mark explainer sentence were
     both "confirmed as Mark's own word without change." Status belongs
     in Ministry, never restated in a code comment.
   - `app.css`: "(supersedes CiC_Full_UX_Design_V1_0.md §2.1's 'Dark
     mode: deferred')", "was #8A837C - 3.38:1", "was #FBEAEA (light
     pink)", the "Cross-world transparency audit:" and "Trust package:"
     stage/feature-name labels, and one remaining "Stage 6b:" label —
     rewritten as present-tense facts (what the current color measures
     and why), not as "was X" comparisons.
   - `data/worlds.ts`: the file's own "used to be a hand-copied second
     version of the registry... nothing here is invented copy... The
     endpoint exists now" history paragraph, "Stage 7.5" cited twice as
     the source of a design decision, every "Nth world, added/admitted/
     re-admitted once X was locked in" ordinal-history framing (6
     instances), and every remaining "Light-mode color was X" comparison
     — all rewritten to state the current accent color's own grounding
     and contrast math directly, with no addition-order or stage
     narrative.
   - `useConversation.ts`, `lib/api.ts`: "(an audit fix)" and
     "recoverable: true - was false, which left a live bug..." rewritten
     to state what the code guarantees now.
   - `lib/flags.ts`: "Both are ruled now, and the seeker read-through...
     passed - the flag defaults ON" reduced to "Defaults ON."; the
     ruling/rollout history moved here.
   - `VoiceTurnBody.tsx`: "below are the confirmed answer, not invented
     here" and "a documented default, not an implicit accident" (process
     voice from round 1's own rewrite) restated as the rule itself; "the
     approach Build-Plan.md Stage 3c replaces" (still framing the legacy
     renderer by what it's superseded by) restated as its own
     completeness gap, stated directly.
   - `VoiceTurnBody.legacy-default.test.tsx`, `screens/TableRoom.tsx`:
     "turn from before Stage 3b" and "Stage 0c, Build-Plan.md" — the
     stage label dropped, the technical condition it named stated
     directly instead.
2. Refreshed `tools/tests/test_check_live_commentary.py`'s
   cic-poc/frontend `HAND_LABELS` entries a second time: round 1 fixed 3
   of the 6 original entries' staleness in its own PR body but round 2's
   further cleanup made 2 more (`Arrival.test.tsx:2`, `Arrival.tsx:14`)
   stop matching too. Only `FigureBridgeMark.tsx:3` (the real
   filename-citation false positive) is still valid; the other 5 slots
   moved to fresh `cic/corpus-map` examples, distinct from the 5 Entry 1
   already claimed there, to avoid a duplicate sample.

Re-validated: `check_live_commentary.py --surface cic-poc-frontend` → 1
hit (the documented `FigureBridgeMark.tsx:3` false positive); `pytest
tools/tests/test_check_live_commentary.py` → **85/85 passed** (0
failures - both PRs' stale-hand-label fixes are now mutually
consistent, pending whichever merges first renumbering the other's
Decision-Log entry per Entry 1's own note); `npx tsc --noEmit` → 0
errors; `npm test` (vitest) → 31/31 passed; `check_paths.py` → 0
new/retired.

**Round 3 (FAIL round 2 fixes, four leftovers the checker's own patterns
don't catch):**
1. `VoiceTurnBody.legacy-default.test.tsx:2-4`: "The flag now defaults
   ON - this file's own title predates that flip..." restated as the
   file's present-tense purpose - it tests the legacy renderer, which
   stays reachable whenever a turn has no `transparency` plan,
   regardless of the flag's own default.
2. `data/worlds.ts:24-26`: "per site-portrait/witt's own now-closed
   cross_world entry" dropped; kept only where the portrait lives
   (GitHub, as `nikolaus.jpg`).
3. `types/conversation.ts:35`: "every fixture/test predating Stage 6b
   built a SourceCard without it" restated as the contract itself - the
   field is optional because a caller may omit it; a real API response
   always includes the key (possibly null).
4. `lib/confidence.test.ts:4`: dropped "(Stage 6b)" from the `describe`
   block title.

Not touched: the several other `Stage N (Build-Plan.md)`/`PHASE-1-
LAUNCH.md Stage N` citations elsewhere in this surface
(`conversation.ts`, `app.css`, `ChatInput.tsx`/`.test.tsx`,
`useWorlds.ts`, `useTable.ts`) - these cite the governing spec document
by name as the source of a still-current technical rule (a round-cap
value, a disabled-prop contract), not a ruling/decision date or
attribution; the round-2 verdict named exactly the four items above as
the remainder, and these weren't among them.

Re-validated: `check_live_commentary.py --surface cic-poc-frontend` → 1
hit (unchanged, the documented `FigureBridgeMark.tsx:3` false
positive); `npx vitest run` → 31/31 passed; `pytest
tools/tests/test_check_live_commentary.py` → 85/85 passed; `check_paths.py`
→ 0 new/retired.

---

## Entry 3 — cic/corpus-map/ (Step 2, surface 3 of 6)

`tools/check_live_commentary.py --surface cic-corpus-map` read 761 hits
before this PR (0 KEEP, 761 REWRITE, 0 ROUTE — the checker's own
ROUTE_CUES limitation reads a ROUTE line as REWRITE; see Entry 1/2's
same note) and 0 after. This is the largest surface so far: 133
`_staging/<volume>.yaml` source files (the only files a worker ever
hand-edits), 58 generated per-tradition bucket files plus
`UNATTRIBUTED.yaml` (regenerated from staging via
`cic/engine/corpus_map_merge.py`, never hand-edited), and a handful of
top-level docs/scripts.

**Never touched anywhere in this PR:** `work:`, `author:`, `locus:`
(except the two boundary cases below), `atlas_ids:` (which tradition a
work maps to), `role:`, or `confidence:` field values. Every edit is to
`note:`/`evidence:` prose or `#` comments.

### What changed, by category

1. **46 "header-only" `_staging/` files** (all their hits confined to
   the file's own leading `#` header block) — a single-pass script
   dropped "Worker notes, `<date>`.", "Worker: `<thread>`, `<date>`.",
   "Vendored `<date>`[, supplied by Mark].", "Written `<date>` by `<X>`
   sweep.", "RULED, Mark, `<date>`:", and "SEEDED WORKED EXAMPLE,
   `<date>` -"/"EXTENDED `<date>` by..." framing from each header,
   keeping every still-true reason (Pearse-file/ThML notes, why a
   volume was proactively vendored, the Cyprian granularity rule,
   Morison's own scholarly-framing methodology, npnf204's own
   worked-example shape) restated in present tense. Diff spot-checked
   file by file before running; re-verified 0 remaining hits across all
   46 afterward.
2. **87 further `_staging/` files** with hits inside per-work `note:`
   fields (not just the header) — done via six parallel workers, each
   given the same litmus test, worked examples, and the CRITICAL
   boundary list above, then reconciled by hand. The dominant pattern,
   repeated hundreds of times: `"<date>: <atlas_id> added alongside -
   the entry the corpus assignment showed was missing, for <reason>.
   <X> is kept: <reason>."` → `"<atlas_id> holds this work for
   <reason>; <X> is kept because <reason>."` Also fixed throughout:
   "RULED BY MARK", "Re-pointed `<date>`", "Cross-linked `<date>` from a
   Source Readiness Dossier finding", "NOTE, corrected `<date>` (OG-N)",
   "Split `<date>` on Mark's ruling", review-round citations
   ("independent review Round N", "lpc Round 28/29"), and several
   multi-sentence "this note previously said X, that was withdrawn,
   corrected here" self-correction paragraphs (codex-theodosianus'
   Donatism-bucket note, perpetua-scillitan's Tertullian-voice note) —
   each condensed to the current true state only, with the withdrawn
   history dropped rather than narrated.
3. **Two boundary cases the parallel workers correctly declined to
   touch**, fixed by hand afterward: `cyprian_opera-spuria-vita-pontius-
   lat_hartel-csel3-pars3.yaml` and `didymus-alexandria_de-trinitate-
   lat-grc_mingarelli1769.yaml` each had review/date narration sitting
   inside a `locus:` field's own string value rather than in `note:`.
   For the Cyprian one, the real reasoning (why the work stays under
   Cyprian's name — the transmitted-author shelf, not re-attributed)
   was moved into `note:`, restated in present tense, and `locus:`
   trimmed back to a physical description. For the Didymus one, the
   locus's current line number was already correct; only the "corrected
   `<date>`, Round 2 Opus review, from a stale reference the Round 1
   header fix itself invalidated" narrative was dropped, since it
   carried no standing information the corrected locus doesn't already
   state.
4. **Top-level docs, hand-edited directly** (not generated):
   `README.md` (7 spots — a Mark quote/date explaining why this sits
   outside `records/`, a stale count-snapshot date, "both were added
   `<date>`", two stale seeded-count-as-of-date table cells, a code
   comment's dated usage note, a coverage-feed sign-off date, a
   Mark-sign-off parenthetical on the `address` field's own semantics);
   `AUTHOR-IDS.yaml` (dropped the verification date, kept "verified via
   WebSearch"); `PAIRS.yaml` (dropped a bare "Decision-Log entry 4"
   pointer, kept the still-live CM-3/D3§3 spec references);
   `WORKS.yaml` (5 spots — a Mark-sign-off date on the `work_id` field's
   own contract, three "verified via WebSearch, `<date>`" tags, one
   "confirmed by direct read ..., `<date>`" tag — all restated dropping
   only the date); `work_coverage_diff.py` (a dated worked-example
   citation, and "fooled a human reviewer" restated as "found").
   `fixture-synthetic.yaml` (the one HAND-AUTHORED bucket file — see
   its own header) had one "Decision-Log entry 10" pointer dropped the
   same way as `PAIRS.yaml`'s.
5. **`ATLAS-TARGETS.md`** is generated by `cic/engine/atlas_targets.py`
   from `cic-website/data/world-census.json`; the committed file was
   also measurably stale (7 vs. 11 `Built & Live` entries, an old
   tradition name) — the same shape as item 1's `atlas-v3.html` embedded
   census. Fixed the one hardcoded process-narration string still in the
   generator's own `render()` (a "hand-typed... caught `<date>`" clause;
   the rest of the generator was already clean) and regenerated the
   file — the drifted count and name fixed themselves as a byproduct.
6. **`CELL-VOICE-WORKLIST.md`** and **`RETRIEVAL-HINTS.md`** were the
   two densest cases in this surface: both read as full engineering
   retrospectives (specific probes run, specific bugs found and fixed,
   "Measured/Recorded/FIXED `<date>`" narration) rather than the
   reference documents their own titles promise ("the standing check",
   "the discipline"). The checker caught only one or two lines in each
   (bare dates); a full manual pass, per the litmus test, restructured
   both down to durable rules/architecture facts stated in present
   tense (the locator-token discriminator and ruling table in
   `CELL-VOICE-WORKLIST.md`; the seven hint-writing rules, the two
   honest remedies, and the scorer's known weighting/follow-up behavior
   in `RETRIEVAL-HINTS.md`), dropping the day-by-day investigation
   narrative and specific probe-by-probe journal entries. Nothing
   asserted in the trimmed versions is invented — every kept sentence
   restates a finding the original text already stated, without the
   who/when wrapper.

### Regenerated (not hand-edited)

Ran `python3 cic/engine/corpus_map_merge.py` once all 133 staging files
were clean: writes all 58 generated per-tradition bucket files plus
`UNATTRIBUTED.yaml` from the now-clean `_staging/` sources. `--check`
first (clean); the real run reported `877 work assignment(s) across 58
Atlas entry(ies)... valid.` and one pre-existing, unrelated finding
(`fixture-synthetic.yaml` is hand-written and not staging-derived — as
documented, expected, left alone).

### Left open — genuinely unresolved editorial questions (ROUTE)

None of these were resolved by this program, per its own scope (never
alter which work maps to which tradition; a ROUTE item's job here is to
stop attributing the question to "Mark"/"a reviewer" and state it
plainly, not to answer it). All were already open before this PR;
several already carry `confidence: needs-ruling` in their own
`_staging/` entry. Listed here rather than filed into a world's own
`Open_Gaps_Tracking.md`, because most of the atlas_ids below are not
built worlds (no per-world gaps file exists to receive them), and
because attempting to regenerate `worlds/_cross-world/NEEDS-RULING.md`
myself surfaced a real defect (below) that made hand-filing safer than
mechanical regeneration this round. Recommend the corpus-map thread (or
whoever owns that cross-world file) do the actual filing/regeneration
with the full context these items need.

- `anf01`, *Epistle of Barnabas* (`post-apostolic-house-church`):
  whether to also add `alexandria-catechetical`, given argued
  Alexandrian provenance vs. that entry's c.150 window start.
- `anf01`, *Against Heresies* `ebionite-nazoraean-current` context row:
  whether a locus-level extract, not the whole work, is the better fit.
- `anf03`, *Apology* (Tertullian) `post-apostolic-house-church` row:
  whether pahc should reach this work through `latin-apologists`
  instead of citing it directly.
- `anf03`, *The Prescription Against Heretics* context row
  (`valentinian-and-other-gnostic-christianities`,
  `marcion-marcionism`): whether its thinner heresiological description
  still justifies the context assignment.
- `anf03`, *Passion of Perpetua and Felicitas* (`latin-apologists`):
  whether `montanism-the-new-prophecy` should also be added, given real
  but not-yet-chosen New Prophecy affinity scholarship.
- `anf03`, *Against Praxeas* (`montanism-the-new-prophecy`) row: still
  literally reads "a ruling for Mark, not a parsing fact" — not caught
  by the checker (no date/ruling-keyword match), flagged here as a
  gap in the checker's own patterns as well as a genuinely open item.
- `anf05` header and several Hippolytus-of-Rome rows (Refutation,
  Christ and Antichrist, Against Noetus, Exegetical/Dogmatical/
  historical fragments, Appendix) plus the Caius row: Hippolytus has no
  census entry at all; every row sits provisionally under
  `roman-church-third-century` pending a ruling on a proper shelf.
- `anf06`, *The Passion of St. Symphorosa and Her Seven Sons*
  (`post-apostolic-house-church`, `confidence: needs-ruling`): both the
  attribution to Julius Africanus and the shelf assignment are open.
- `anf06`, *Of the Manichaeans* (Alexander of Lycopolis)
  (`manichaeism`): whether the author is an orthodox bishop or a pagan
  Platonist is unresolved, which affects whether `role: context` is
  even the right call.
- `npnf214`, *The Canons of the Council of Ancyra* and five sibling
  provincial-canon entries (Neocaesarea, Gangra, Antioch-in-Encaeniis,
  Laodicea, Constantinople-394) (`imperial-juridical-christianity`):
  whether a finer/more specific home should exist for provincial
  disciplinary canons.
- `npnf214`, *The Apostolical Canons* (`imperial-juridical-christianity`,
  `apocryphal-and-pseudepigraphal-literature`): whether this should be
  placed with its sibling text, the Apostolic Constitutions (assigned
  separately in `anf07`), under one unified ruling.
- Duplicate census entries `cyrilline-miaphysite-egyptian-tradition`
  and `cyrilline-miaphysite-egyptian-christianity`: which should carry
  corpus assignments generally (affects `npnf214`'s Council of Ephesus
  431 tradition row and `npnf212`'s Letters of Leo the Great).
- `anf02`, *Address to the Greeks*/*Oratio ad Graecos* (Tatian): whether
  his later Encratite branding and eastern/Syriac career mean his voice
  belongs with pahc or the Syriac tradition instead.
- `anf02`, *Plea for the Christians*/*Resurrection of the Dead*
  (Athenagoras): whether a better home than the era-1 mainstream entry
  may turn up in a later survey.
- `anf02`, *The Stromata* context row (Clement of Alexandria)
  (`valentinian-and-other-gnostic-christianities`): whether
  locus-level extracts should be added for the Valentinus/Basilides/
  Isidore/Carpocrates material, and whether the Marcion material
  should ground a separate `marcion-marcionism` context assignment.
- `codex-theodosianus`, second assignment (`donatism`, `confidence:
  needs-ruling`): whether/how CTh belongs in Donatism's bucket —
  context, antecedent, or narrower (CTh 16.5/16.6).
- `codex-theodosianus`, third assignment
  (`imperial-juridical-christianity`, `confidence: needs-ruling`):
  whether CTh is that entry's own context or tradition, pending that
  world's Doc_01/Doc_02.
- `npnf210`, *On the Holy Spirit* (Ambrose): a `homoian-arian-
  christianity` id could be added by analogy with *De Fide*.
- `npnf203`, Rufinus' translation prefaces (`alexandria-catechetical`):
  may be worth dropping to sub-work-level instead of a grouped context
  row.
- `npnf209`, *De Fide Orthodoxa* (John of Damascus)
  (`melkite-arabic-christianity`): a Byzantine-imperial-church id could
  be argued for instead of or alongside.
- `npnf101`, Manichaeism context row (Confessions Books III-V)
  (`manichaeism`): `npnf104`'s dedicated refutations could carry that
  bucket alone instead.
- `ephraim_prose-refutations`, *Against Bardaisan's "Domnus"* and
  *Against Bardaisan (A Discourse Against Bardaisan)*
  (`bardaisanite-current`): whether a dedicated Bardaisan/Daisanite
  entry, or folding into the Syriac world alone, fits better than the
  current floor entry.
- `chronicle-of-edessa`, *The Chronicle of Edessa*
  (`syriac-orthodox-west-syriac-christianity`): whether a
  composition-era (c. 540s) placement is wanted for this entry at all.
- `npnf104`, *The Correction of the Donatists* (Letter 185)
  (`imperial-juridical-christianity`): whether ijc should instead be
  reached through the imperial laws themselves rather than through
  Augustine as North African advocate.
- `npnf107`, *Soliloquies* (`latin-pastoral-congregational-
  christianity`): whether the Cassiciacum period should also touch
  `ambrosian-milan-standalone`.
- `anf08`, *Excerpts of Theodotus* context row
  (`valentinian-and-other-gnostic-christianities`): now that the text
  is confirmed to be the Eclogae Propheticae rather than genuine
  Valentinian material, whether it belongs in this context entry at
  all.
- `anf08`, Fragment of Maximus of Jerusalem
  (`palestinian-church-pre-constantinian`): attribution disputed (the
  fragment circulates with Methodius' material).

### Flagged, not fixed (out of scope here)

- **`worlds/_cross-world/NEEDS-RULING.md` / `gen_needs_ruling.py` has a
  real data-loss bug.** The file's own header claims it is fully
  "Generated by `gen_needs_ruling.py`", but its committed copy carries
  a fourth, hand-appended "question that is not per-work" (a
  multi-paragraph methodology finding about the census `era` field)
  that does not exist anywhere in the generator's own source. Running
  `gen_needs_ruling.py` after this PR's corpus-map fixes (to pick up
  the reworded `needs-ruling` notes and the corrected 5→6 work count)
  silently dropped that fourth question and relabeled the section
  "Three questions". Reverted that regeneration rather than ship the
  loss (`git checkout -- worlds/_cross-world/NEEDS-RULING.md`);
  `worlds/_cross-world/` is untouched by this PR. Flagged for whoever
  owns that file: either the generator needs to actually incorporate
  that fourth finding as data, or the file needs a documented
  hand-maintained section the generator preserves on rewrite — right
  now, running it as-is is destructive.
- The ROUTE items above are not filed into any per-world
  `Open_Gaps_Tracking.md` or `WANTS-REGISTER.md`, for the reasons
  stated in that section.

### Validation

- `python3 -c "..."` YAML parse check across all 133 `_staging/*.yaml`
  files → 0 bad.
- `python3 cic/engine/corpus_map_merge.py --check` → clean, then the
  real run → `877 work assignment(s) across 58 Atlas entry(ies)...
  valid.`
- `tools/check_live_commentary.py --surface cic-corpus-map` → **0 hits**
  (was 761).
- `tools/check_live_commentary.py` (full repo) → every other surface's
  count unchanged from before this PR (cic-website 1, cic-poc-frontend
  1, cic-engine 19, engine 1229, records 2841, reference 261, worlds
  16541, fixtures 8, canon 28, packages 0).
- `tools/check_paths.py --baseline tools/check_paths_baseline.txt` → 0
  new/retired.
- `tools/check_no_embedded_world_data.py` → exit 0.
- `cic/engine/works_registry.py --check` → OK, 4 works, all external_ids
  and item addresses valid.
- `cic/engine/author_ids.py --check` → OK, 5 authors, all well-formed.
- `pytest tools/tests/test_check_live_commentary.py` → **88/88 passed**
  (refreshed 17 stale `HAND_LABELS` entries this cleanup itself made
  stop matching, moving them to fresh `worlds/` examples — item 4, not
  yet touched by this program; table grew from 85 to 88 entries in the
  process, still well above the ≥60 floor).

---

## Entry 4 — `worlds/_cross-world/gen_needs_ruling.py` data-loss fix (PR #510)

Fixes the data-loss bug flagged in Entry 3's "Flagged, not fixed" note
above. `gen_needs_ruling.py` regenerates `NEEDS-RULING.md` from
`cic/corpus-map/`; the committed file also carried a hand-appended
fourth "question that is not per-work" the generator's own source
never produced. A regeneration after Entry 3's corpus-map fixes
silently overwrote that section.

**2026-09-24, Mark (via the managing thread, delegated verdict
authority).** Round 1: FAIL. The marker-preserving design (everything
below `HAND_MAINTAINED_MARKER` in the output file is read back from
the existing file and reproduced verbatim, rather than regenerated)
was confirmed correct, but the fix was still in the same data-loss
class — `extract_hand_maintained()` fell back to a placeholder,
silently discarding real content, whenever an *existing* file's marker
was missing, rather than only doing that on a genuine first run (file
absent). Required before round 2: (1) make a missing marker on an
existing file a refusal to write, not a placeholder; (2) remove this
bug's own "found 2026-09-24" story from the live script's and test's
docstrings/comments, since `worlds/` is itself a live surface this
program governs — the story belongs here instead; (3) cut
`NEEDS-RULING.md`'s new "Placement questions" section intro down to
one present-tense line describing what the section holds, not a
narration of the cleanup program that produced it; (4) wire the new
test file into somewhere CI actually collects it.

Round 2 (this entry): `extract_hand_maintained()` now raises
`MissingMarkerError` when given a non-`None` existing text with no
marker, and `main()` catches it, prints an error, and returns without
writing — a first run (no file at all) still gets the placeholder.
`worlds/_cross-world/tests_gen_needs_ruling.py`'s fallback test now
asserts the raise, and a new end-to-end test drives `main()` itself
against a scratch file with no marker and asserts the file is left
byte-for-byte unchanged. The script's docstring, its
`HAND_MAINTAINED_MARKER` comment, and the test file's own docstring
were rewritten present-tense (the guarantee, not the story of finding
the bug). `NEEDS-RULING.md`'s "Placement questions" intro is now one
line. `.github/workflows/ci.yml` gained a `crossworld` path-filter
output (`worlds/_cross-world/**`, `cic/corpus-map/**`) and a new
`cross-world-tests` job that installs `pyyaml`+`pytest` and runs
`tests_gen_needs_ruling.py` — this suite had nowhere in CI before this
PR.

### Validation

- `python3 -m pytest worlds/_cross-world/tests_gen_needs_ruling.py -q`
  → 7 passed (the original 6, plus a new
  `test_main_refuses_to_write_when_an_existing_file_lacks_the_marker`).
- Three consecutive `python3 worlds/_cross-world/gen_needs_ruling.py`
  runs against the real file → idempotent, hand-maintained tail
  byte-for-byte unchanged each time.
- CI run on this PR's branch, `cross-world-tests` job → green (linked
  in the PR).

---
