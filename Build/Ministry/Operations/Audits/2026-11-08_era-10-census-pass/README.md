# Era 10 census pass (P2-E10a and P2-E10b): data release 22 — 2026-11-08

**Release numbers.** On the branch this work was numbered release 21 (P2-E10a) and then release 22
(P2-E10b). Neither was published. Main published release 21 first (the Bogomil split), so both
passes ship together as data release 22. "Release 21" below and in the P2-E10b proposal means the
branch's own working state, not the published release 21. Open-Gaps entries from this work were
renumbered 124 to 133 on merge, because main's Bogomils entry took 123.

Ruling: Mark, era 10 gate, "take every recommendation" (`Build/Ministry/Features/Atlas-World-Map/Decision-Log.md`, "ERA 10 GATE"). G-15 (IX.50) is not ruled; nothing was added for it.

## What changed

- **Edits.** All 453 text edits and 19 structural operations in `Build/Ministry/Features/Atlas-World-Map/Design/StepZero-Eras/CiC_Step0_Era10_V2_0_Proposed_Edits.json` applied, each exactly once, against release 20. Every gated edit takes its recommended option.
- **IX.31 retired** (G-8 (a)): no `redirectTo`; reason as drafted; date 2026-11-08.
- **Dates and the living mark.** Each era 10 row takes `dates`, `start`, `end` and `living` from the JSON (67 field changes). IX.28 is now `living: false` (G-50).
- **G-51 (a).** Each era 10 row carries `livingEvidence`: `basis`, `evidence`, `grade` and `group`, cut from its `livingReason`. Record wording (version numbers, gate and section numbers, conditionals on decisions now made) was removed; no word was added. No page reads the field.
- **G-14.** `iglesia-ni-cristo`, atlasId IX.51, from draft D-E1. The fields D-E1 does not carry come from IX.16's own copy (Open-Gaps, "Iglesia ni Cristo row: fields not in the draft", 2026-11-08).
- **G-1.** `eras[9]`: dates "1906-c. 2010", tag "A century of global Christianity", the standard frozen status, and the two sourced key events. The 2010 centenaries wait for a source.
- `meta.totalEntries` 301 (one retired, one added); Floor Question 29, Pre-Survey Candidate 219; release 21. `meta.version` is unchanged, as in releases 17 to 20.
- Pages rebuilt: `python -m engine.m6.cli atlas-sync`, `node Build/tools/generate_tree_pages.mjs`, `node tools/build_tree_site.mjs`.

## Checks

- `node tools/validate-census.mjs --base <release 20> --atlas cft-website/index.html --tree cft-website/tree`: 0 errors, the 2 standing warnings.
- The census validator's node tests, the tree tests, `atlas-check` and `engine.m6.cli check` pass.
- The commentary, spelling and path checks pass.

## Open items

In `Build/Ministry/Features/Church-Family-Tree/Open-Gaps.md` (2026-11-08): IX.16 still names Iglesia ni Cristo; the new row's borrowed fields; IX.31's old page; the recordings made stale. The script that applied the pass is `apply_era10.py`.

# P2-E10b: the new rows and named lines (data release 22) — 2026-11-08

## What was applied

- **Proposal.** `CiC_Step0_Era10_P2E10b_Proposed.json` (Build/Ministry/Features/Atlas-World-Map/Design/StepZero-Eras/), after Review Round 2's mechanical fixes (S2-1, M2-1 to M2-3, C2-1 to C2-5). Applied by the drafter's checker, with 0 edit or meta check failures.
- **New rows.** IX.52 (The Anglican Communion), IX.54 (rescue missions), IX.55 (the Christian homeschool movement), IX.56 (the liturgical movement), IX.57 (the Third Wave), IX.58 (Promise Keepers).
- **Register edits.** 46 edits on existing rows, among them the whole-field rewrites of IX.16 (now three bodies) and the named lines on IX.24, IX.30, IX.33 and IX.45.
- **Counts.** `meta.totalEntries` 307; Pre-Survey Candidate 225. `meta.release` is 22, dated 2026-11-08.
- **Held.** IX.53 (faith missions, with the Wycliffe line of G-56(a)) is not built. Round 2's S2-2 waits on Mark. Open-Gaps 129 to 132 track it and the other carried items.

## Checks

- `python -m engine.m6.cli atlas-sync`, `node Build/tools/generate_tree_pages.mjs` (307 pages, 6 new) and `node tools/build_tree_site.mjs`: 0 mismatched.
- `node tools/validate-census.mjs --base <origin/main census> --atlas cft-website/index.html --tree cft-website/tree`: 307 movements, 579 edges, 10 eras, 0 errors, the 2 standing warnings.
- Node tests: tools/tests/validate_census_*.test.mjs, Build/tools/*.test.mjs (89 pass) and cic-worker/worker.test.mjs (25 pass).
- The commentary, spelling and path checks pass.

## Recordings

No paid run was made. The six new rows have no recording, so 19 tree movements with text have none (13 before). The 36 stale tree recordings and the 264 stale documented-story recordings are the same as before this release: it makes no recording newly stale.

