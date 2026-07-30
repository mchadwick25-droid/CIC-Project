# Waiting on Mark

## 2026-07-30 — VG-1a done: the alias wrong-linkage parser fix (Step 1a of the Voice-Governance Addendum)

**What changed:** one function, one file — `parse_aliases()` in `cic-poc/backend/app/rag/indexer.py`. A parenthetically-qualified alias segment (`illumination (baptismal)`) is now dropped whole instead of being stripped to its bare head. The bare-head behavior was the reproduced production bug: "illumination" silently became one of Baptism's aliases and stole Illumination's own key in the frontend map.

**Before/after, measured over all six worlds with the live code:**
- Before: 9 colliding keys, all Alexandria (Desert/Hieronymian/IJ/PAHC/Syriac all 0) — matches the plan doc §5.1's table exactly, key for key.
- After: 7 — the two parenthetical-caused collisions (`illumination`, `apokatastasis`) resolved; the 7 genuine alias-set overlaps (`photismos`, `catechist`, `communion`, `divine likeness`, `the eternal word`, `the son`, `the word`) unchanged, as expected — they're VG-1b's gate's job.
- Baptism still reachable through `photismos`, `initiation`, `the washing`, `new birth`, `the bath`, `crossing the threshold`.
- Retrieval regression (rule 2): full eval re-run vs `B-RETR-POST-P3.json` — **0 regressions; every metric identical**.

**What surprised me (filed as FLAG-028, per this step's own step-4 rule, routed to VG-1b):** the fix's drop-the-qualified-segment rule also removes 9 corpus-wide aliases whose qualifiers are benign descriptors, not collision guards — e.g. `bat qyama (singular forms)` in Syriac, `monogenes (Greek parallel)`, `communion (as juridical status)` in Imperial-Juridical, and `The Vulgate (anachronistic... label)` in Hieronymian (whose alias set is now empty). None of these were colliding; they simply stop highlighting in their own worlds. That's a bounded reachability cost the plan's rationale doesn't cover for this class — VG-1b's authoring/gate pass should decide per case (re-author unqualified where safe, or route through confirmed-gloss). One incidental win: the old parser was emitting a garbage mid-phrase fragment for ijclex003 (`the Dated Creed formula — not`); that's gone.

**Base-state note:** local main fast-forwarded cleanly onto the rolled-back `e92cf85` (pure history move, tree-identical, zero file changes). The full Syriac-freeze session survives on `origin/claude/rollback-to-fable-base` and a local safety branch `backup/syriac-freeze-16cab54`; its working-tree leftovers (untracked `wrs/records/syriac_world/`, `scripts/s62_syr_*`, staging files) are still on disk, untracked, untouched by this step.

**Not started, deliberately:** VG-1b (alias-safety gate — its fixtures must be built against this fix's corrected output, in a separate session per rule 4) and VG-1c (confirmed-gloss schema).
