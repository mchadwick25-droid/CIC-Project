# Handoff — conversation chooser, step 4 checks and five rulings — 2026-10-20

From session: https://claude.ai/code/session_01GSkmJBxTD77vXWGm6syanq · Workstream: Conversation-Chooser · Branch / PR: `claude/vibrant-heisenberg-hrhcvd`, one draft PR into `main`

## 1. Done, and how it was checked

| What was done | How it was checked |
|---|---|
| PR 987 confirmed merged (`51cbfb4c`); `main` has since moved to `9dda3b8b` (PR 1001). | `git log origin/main` |
| Tradition-page regeneration diff: `generate_tradition_pages.py` run on a clean copy of `main`; all 11 pages regenerated with no change. | `git status` empty after the run |
| Step 4 emulated-device pass (Chromium, real Google fonts) at 390x844, 844x390, 820x1180, 1180x820, 1280x800, 1920x1080 on `index.html`, `table.html` and one tradition page. Header is one row from 1180 px up, two rows on the iPad in portrait and phone landscape (114 px), five on a phone (201 px). No sideways scroll. Header buttons are 38 to 40 px tall, under 44. | Playwright script; results reported to Mark in the thread |
| Five rulings built: free line under the hand, 16 px card front text, no-world sentence in search, the list control. Tree button wording decided only. | See the 2026-10-20 entry in `Decision-Log.md`; headless runs at three widths; `test_cross_world.py` 22 pass; census 0 errors; commentary check exit 0 |

## 2. Not done

- Real iPad and iPhone Safari, VoiceOver or another screen reader, and the staging deploy (not reachable from the cloud session). The step 4 screen-reader items are still open.
- The tree's "Add to the table" button, its seat store and tray (needs Theme E's open items ruled).
- Header height on iPad portrait and phones, and the 38 to 40 px header buttons and short narration and footer targets: reported, not fixed, not ruled.
- The list control differs from the approved drawing in two ways (compact rows; no return to cards on a phone). See the Decision Log entry.
- On a phone the free line sits below all eleven cards. Not ruled.
- Feedback items 27 and 28 and the "Change orders to Theme D" section named in the launch prompt are not in the repo. Item 28 (every device) is only as the prompt states it.

## 3. Re-check before you trust it

- That `from` and `via` still reach the room (`talk.html` did not forward `via`; unchanged here).
- The localhost run showed one refused connection per page load from `go-deeper-config.js` and `feedback.js` calling an API port; I believe it is an artefact of running locally and did not prove it.

## 4. Waiting on Mark

- Whether the list rows should be compact, and whether a phone user can switch back to cards.
- The header and touch-target fixes; the free line on a phone.
- Real-device and screen-reader testing, and promotion to `live` (his call through the runbook).

## 5. Next step

Mark views the PR's preview on his own iPad and phone; then rule on the items in section 4.

## 6. Spend

Allowance share used: one Sonnet session, no subagents. Metered: none. No model call, live test or paid service.
