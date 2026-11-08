# Era 10 census pass (P2-E10a): data release 21 — 2026-11-08

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
