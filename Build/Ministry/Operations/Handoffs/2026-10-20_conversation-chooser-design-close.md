# Handoff — conversation chooser design thread, close — 2026-10-20

From session: https://claude.ai/code/session_01DieKxWNS33gUktGHTTiGeS · Workstream: Conversation-Chooser (design thread) and the engine promotion attempt · Branch / PR: `main`; open PR 998 (harness fix); the chooser's live work is on the build thread's branch `claude/zen-cori-x2c5yp`

Read with `2026-10-20_conversation-chooser-landing-finish.md` (this thread's earlier handoff) and `2026-10-20_conversation-chooser-build.md` (the build thread's). This one covers the day after those: the eleven-card hand, the engine promotion attempt, and Mark's rulings on spend.

## 1. Done, and how it was checked

| What was done | How it was checked |
|---|---|
| Mark's change order: the hand holds all eleven cards in time order, five showing, the next card peeking at each edge, Shuffle gone, search and era chips narrow the row. Built on PR 995, then merged by the build thread into `claude/zen-cori-x2c5yp` at Mark's direction ("one system"); PR 995 closed. | Headless Chromium: 3 of 11 at boot, wheel to 11 of 11, "Augustine" 2 matches with Donatism first, "baptism" 7, Reformation chip 2 of 11, grid pick clears a chip, phone list shows 11, no errors. `test_cross_world.py` 22 pass. |
| A sideways overflow found in the rebase: hidden cards beyond the fan widened the page by 857 px at 1280 px. Fixed with `overflow-x: clip; overflow-y: visible` on the hand (commit b345b6a3 on the closed PR 995's branch). The build thread's merge took the earlier commit, not this one; it was told the one-line change. | Measured 0 overflow at 1280, 1024 and 1434 px after the change; 857 and 1054 px on the build branch's head ee5edce8 without it. |
| Promotion attempt: the public site already serves the landing page from `main` through Cloudflare (verified on churchinconversation.com: no title block, text-link masthead, chooser mounted, wheel handler present). `main` is 508 commits ahead of `live`; the promotion moves only the engine. `admission_conform --enforce` reported all eleven worlds stale. | Runbook steps 1 to 3: staging unreadable from the sandbox (Render egress-blocked); `required_secrets --service cic-engine` prints the checklist, exit 0; conform exit 1. |
| Mark approved "fleet re-admission, 20 October" (cap $8, Bedrock us-east-1, Sonnet 4.5, eleven worlds). Packages restored with `engine.m2.cli restore` (compiled bytes are not in git). The run stopped at the cap after 287 of 308 calls, $7.79 settled, and wrote no report: the harness wrote only at the end. Ten completed worlds lost. | Ledger `cic-live-test-ledger-2026-10-20.jsonl` in the session scratchpad (287 settle lines); run log; `admission_conform` still 11 failures. Logged in the System Hub Decision Log (PR 996). |
| Harness fix: `engine.m3.live_admission_run` keeps completed worlds on a cap stop and writes its report after every world. | PR 998: `engine/m3` 72 pass including two new tests; settings-only smoke exit 0. In CI at close. |
| Mark's rulings, in his words, on main: no more money spent by this thread; the second run withdrawn (PR 999). A paid-run gate was drafted at his first answer and dropped at his second ("I don't want a gate"); the branch `claude/paid-run-gate` holds one unmerged commit, no PR. | `CiC_System_Hub_Decision_Log.md` entries of 2026-10-20; the chooser `Decision-Log.md` entry for the eleven-card hand. |

## 2. Not done

- The engine promotion. The admission gate is red for all eleven worlds and no admission evidence exists. Whether anyone runs the fleet again, waives the gate, or holds is Mark's decision; this thread makes no further model call.
- Everything in section 2 of the two earlier handoffs still stands: screen-reader pass, iPad and phone check, per-world portrait crop, `via` forwarding, six taglines' readability, eight summary findings, Gaul's open finding, unused assets, the "Free to start" line, card body text size, the record-line choice, the hint line.
- The build thread's branch `claude/zen-cori-x2c5yp` carries the sideways-overflow fault unless it took the one-line change; check before it merges.
- The remote branch `claude/paid-run-gate` could not be deleted from the sandbox (403); delete it from GitHub.

## 3. Re-check before you trust it

- That `churchinconversation.com` still serves the chooser from `main` with the real fonts on one masthead row: this thread saw only fallback-font renders and a text grep of the live page.
- The $7.79 figure is the ledger's priced total against the rate card, not an AWS invoice.
- That PR 998's incremental report write does not change any report field: `_assemble_report` was moved, not rewritten, and the tests cover the stop and the per-world write, not every field.

## 4. Waiting on Mark

- The engine promotion: run again (by whom, with what cap), waive, or hold.
- Which "What the record holds" line ships; the six taglines' readability; the hint line; the "Free to start" line; card text size.

## 5. Next step

Merge PR 998 when green (unpaid). Then nothing from this thread. The build thread finishes the chooser on its branch; the promotion waits on Mark.

## 6. Spend

Metered: $7.79 on "fleet re-admission, 20 October", no evidence produced; the loss and its cause are in the System Hub Decision Log. Allowance share: one long session; four read-only Opus subagents for the claim checks and one for the gate review.
