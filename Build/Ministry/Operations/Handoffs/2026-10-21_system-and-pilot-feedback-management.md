# Handoff — system and pilot feedback management — 2026-10-21

From session: https://claude.ai/code/session_01Do3noHRda8t48e7k7Qxo5p · Workstream: pilot feedback, production health, access and payment (coupons, exceptions, pay as you go) · Branch / PR: claude/kind-brahmagupta-86iet2, PRs 1011, 1014, 1020, 1021

The role (Mark, 2026-10-20): track the work, catch conflicts between build threads, answer ideas and questions. Not the build thread. Give a build thread a fact only when Mark asks or it needs one. Mark decides which thread builds what.

## 1. Done, and how it was checked

| What was done | How it was checked |
|---|---|
| CLAUDE.md 3.2 "Asking for any spend" merged (PR 1011); step 6 restored to the approved wording | GitHub: PR 1011 merged at 2f0d54c5; diff read against the old text |
| The `block_live_pr` hook deleted at Mark's direction (PR 1014) | `.claude/settings.json` hooks block and `.claude/hooks/block_live_pr.py` removed; merged |
| Promotion PR 1018 merged to `live` at 0033bc97; the live app then failed: every voice returned "The voice couldn't be reached" | Render log from Mark: Bedrock `400 Invalid API version: 2026-10-21` on the Sonnet call |
| Cause found: `engine/Dockerfile` installs `anthropic[bedrock]>=0.69` unpinned; the rebuild took anthropic 2.0.0 | Opened both wheels: 1.17.0 sends `bedrock-2023-05-31`, 2.0.0 sends `ANTHROPIC_API_VERSION = "2026-10-21"` |
| SDK capped below 2 in five requirements files (PR 1020), promoted (PR 1021, `live` at e6c6dcac) | Render page Mark pasted: manual deploy of e6c6dca succeeded and went Live. No conversation was tested by this thread |
| Main and live content identical after PR 1018 | `git diff origin/main origin/live` empty |

## 2. Not done

- Whether voices work on the capped build. Mark said the laptop works. His phone still showed the old system, then the daily limit.
- Mark was to restart `cic-engine` in Render to clear the daily counts. Not confirmed done.
- The two old branches `claude/paid-run-gate` and `claude/claude-md-spend-step` are not deleted (the git proxy gives a 403 on delete; Mark must delete them on GitHub).
- The admission gate was not run and Mark has not ruled on it. `python -m engine.m3.admission_conform --enforce` fails for all 11 worlds (checked 2026-10-21).
- Pilot feedback records are not updated for 2026-10-21 rulings (see section 3).

## 3. Re-check before you trust it

- The phone showing the old version: causes not found. Not a service worker (none in `cic-poc/frontend`). Not tested: a different address, or a layer in front of the app.
- Daily cap, read in `engine/api/anon_cap.py`: 5 new conversations a day and 150 messages per visitor, counted in memory, resets at midnight UTC or on a restart. A conversation counts when it is created, even if the voice then fails. No override found in `render.yaml`; other config not checked.
- A tester code gets past that cap (`anon_cap.py` lines 261 to 274). Made at `POST /api/admin/deeper/tester` with the admin token; defaults 20,000 tokens for 30 days, at most 2 a day (`engine/deeper/ops/go-deeper.yaml`). The curl command was never run.
- Rulings reported second-hand by the other pilot feedback manager, not yet in the records: one build thread at a time; Theme B length and filler check only logs and never triggers a paid redo; in-room AI note is one small light line at the foot (PR 1013). Records out of date as that manager said: Theme E scroll and swipe (the wheel was removed 2026-10-20), the open list still carrying the free line and card text size, and the tree button wording "Add to the table".
- Other dependencies are also unpinned (`boto3>=1.34`, `fastapi`, `uvicorn`, `pydantic`, `httpx`, `pyyaml`). The same kind of break can recur on any rebuild.
- Render's Auto-Deploy setting after the rollback: unknown. Mark was told to turn it back on.
- The Board: https://claude.ai/artifact/4fW8MMeEGeGfEuV5amdvFp (private to Mark). Item-by-item status of feedback items 1 to 29 on it was checked by the other manager on 21 Oct.

## 4. Waiting on Mark

- Whether to run, waive or hold the admission gate (a model-call run follows the spend step in CLAUDE.md 3.2).
- Not counting a conversation whose first voice reply failed toward the daily cap (a design change; flagged, not asked).
- Making the server tell browsers not to keep the main page (a one-line engine change; only if the phone problem proves to be a cached page).
- Coupons and exceptions for particular people, and pay as you go: new work. Mark has not given the design. Mechanics that exist: free allowance, packs, sponsor codes, tester codes (see `Build/Ministry/Features/Go-Deeper/Decision-Log.md` and `go-deeper.yaml`; read on 2026-10-20, not re-read).

## 5. Next step

Read `Build/Ministry/Operations/Pilot-Feedback/Pilot_Feedback_Log.md` and `Pilot_Feedback_Decisions.md`, then ask Mark one thing: what to work on first (the phone problem, the records catch-up, or the coupons and pay-as-you-go design).

## 6. Spend

Allowance share used: not tracked. Metered: none. No model call, live test or paid service was used.
