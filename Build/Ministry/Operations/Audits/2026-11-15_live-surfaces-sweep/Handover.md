# Handover — live-surfaces sweep, PR #1680

Branch `claude/live-surfaces-sweep`. Worker session_01JMNsSEEFburXVrQmuPQ1iD stops here at the coordinator's request (context near 400k).

## The CI failure

Check "Live-surface commentary (files this PR edits)" fails on b62786b9. Cause, traced: that job uses a sparse checkout holding only `tools/`, `engine/m1/` and the files the PR edits. The ACCEPTED_OPEN stale-waiver check added in b62786b9 scans each waiver's files (`cft-website/index.html`, `cft-website/tree/*.html`, `cic-website/data/world-census.json`, three compiled `cic-website` files). Those are not in the sparse checkout, so every waiver reads as stale and `--enforce` exits 1. The same gap would silently turn off the record-slug rule in CI, because `records/` and the census JSON are absent there too.

## The fix, committed with this handover (6e4f2f02), not yet proven in CI

- `tools/check_live_commentary.py --sparse-paths` prints the extra paths the scan reads: the census JSON and every waiver's files.
- `.github/workflows/ci.yml` (the live-commentary job): a new step after setup-python runs `python tools/check_live_commentary.py --sparse-paths | git sparse-checkout add --stdin` before the `--enforce` step.
- `_world_codes()` reads `records/`'s subdirectories from `git ls-tree` when `records/` is not on disk.
- `python -m pytest tools/tests` passes 364 locally; `--enforce` and `check_spelling.py --enforce` are clean on a full checkout.

## What I was about to run

A local simulation of CI's sparse checkout, in a scratch git worktree: `git sparse-checkout set /tools/`, add `/engine/__init__.py`, `/engine/m1/` and the PR's edited files, then `--sparse-paths | git sparse-checkout add --stdin`, then `python tools/check_live_commentary.py --base origin/main --enforce`. It hit a permission prompt and did not run. The push of this commit is the real test: if the job is still red, read its stderr, which the job log's tail does not show; the blocking or stale lines print before the trailing KEEP rows.

## What is left

1. Get "Live-surface commentary (files this PR edits)" green on the new head. The rest of CI was green on b62786b9.
2. Merge on green. The coordinator gave the go ("merge #1680 on green; nothing is ahead of you"), conditional on the waivers, which are in.
3. Before merging, re-check the next free Open-Gaps number: entry 280 is this PR's, and main had 279 at the last merge.
4. After merging, send the coordinator the short report: what was moved or cut and where it went (R1_changes.md sections 2, 6, 7; Moved_Notes.md), what is left for Mark (section 5; Open-Gaps 280), and what the check now covers (section 3, plus the ACCEPTED_OPEN waivers in section 7).
5. Small corrections still open: R1_changes.md section 2 says 44 rewritten Library headers and the PR body says 46; the diff shows 45. The System Hub Decision Log entry for this sweep does not yet mention the waivers (R1_changes.md section 7 does).
