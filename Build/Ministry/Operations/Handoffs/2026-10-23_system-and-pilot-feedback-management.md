# Handoff — system and pilot feedback management — 2026-10-23

From session: https://claude.ai/code/session_01QZGY6Pwg13hq8dULsnBmwv · Workstream: pilot feedback, production health, tokens and accounts coordination · Branch / PR: claude/handoff-system-feedback-2026-10-23

The role (Mark, 2026-10-20): track the work, catch conflicts between build threads, answer ideas and questions. Not the build thread. Mark decides which thread builds what. One big project at a time (Mark, 2026-10-23).

## 1. Done, and how it was checked

| What was done | How it was checked |
|---|---|
| Promotion to live: PR 1056 merged at `e5e3ac5bba642ec56e0e0bb6964b4be8e7dc773a`, without accounts A3 | `/health` on https://app.churchinconversation.com reported that commit at 03:38 UTC; the new commit's CI checks (engine suite, Docker build, frontend, world gates, M9) were green; the poll log is in the session |
| Visitor bound (PR 1044), free 3-round rule removed (PR 1046), privacy cookie wording (PR 1041), cryptography pin (PR 1050), cost report (PR 1055, on `main` only) | PR pages read; merge commits seen in the `main` history; a build thread's own test counts were reported, not re-run here |
| Independent Opus review of pay as you go and accounts: twelve findings, five spot-checked in code | Findings and their status are in Pilot_Feedback_Decisions.md, "Independent review of pay as you go and accounts — 2026-10-22" |
| Gate corrections: the admission run and secrets check were already waived 2026-10-21 | System Hub Decision Log, entry "2026-10-21 - Change order: no admission run and no secrets check to promote to live"; correction in Pilot_Feedback_Log.md |
| Four finished threads archived; Library eras and Family Tree navigation parked | `archive_session` results; PR 1052 |
| Records kept up to date: Pilot_Feedback_Log.md and Pilot_Feedback_Decisions.md through PR 1060 | Each entry names its source |

## 2. Not done

- **Buying is dark.** `cic-website/go-deeper.html` has `PAYMENT_LINK = ""`, `noindex`, and one link slot for three packs. No Payment Link, webhook endpoint or Stripe settings exist that this thread has seen. Stripe's written answer on stored value, the lawyer's questions on expiry and refunds, and a real smallest-pack purchase and refund are open.
- **Accounts cannot switch on:** no sign-in mail provider; the words and screens slice and the backup and deletion slice are not built; A3 (the shelf, PR 1053) is on `main` but held from `live`; the review's sign-in findings F5 to F7 have not been confirmed fixed.
- **Not tested:** a real conversation on the live engine since the rollback.
- **Not explained:** one Cloudflare "Deployment skipped" on a docs branch (PR 1052). Cloudflare's build log needs Mark's login.
- Branch clean-up: 704 remote branches, 636 not merged into `main`; this session cannot delete branches.

## 3. Re-check before you trust it

- The finish line Mark chose on 2026-10-23: the big project ends when buying works end to end (Stripe live, a real purchase and refund proven) and the visitor experience is approved; accounts continue as one quiet tail thread. Confirm it against Pilot_Feedback_Decisions.md before relying on it.
- Cost figures: $0.003 per safety check is the Go Deeper log's estimate; $0.06 a voiced round is an assumption (the repo's one measurement: $0.292 for ten rounds at old Sonnet 4.5 prices). Real numbers come from the cost report after the next promotion.
- Thread statuses and PR claims taken from other threads' own reports were not all opened here: A3's review, the Fable design thread's progress, the chooser thread's before and after.
- `live` has A1 to A2 code but not A3 or the cost report. `main` is ahead of `live` by A3, the cost report and records.
- Network access for this environment was set to Full by Mark on 2026-10-22.

## 4. Waiting on Mark

- Look at the Theon card before and after (chooser thread, session_012JtxAJXgjVHwaFgyA5iQEQ) and the Fable design thread's first question (session_012jjhAokk8iJ5PiFZ3Tn15r).
- Check the AWS Budget: the figure, and whether it has an action that stops spending or only alerts.
- The pilot join count; whether the 2026-10-17 door switch to enforcing and the $12 base were meant (no decision-record entry).
- Whether A3 and the cost report are promoted together, and when.
- The Stripe setup in his dashboards (three Payment Links, the webhook, the Render settings), the mail provider choice, and the lawyer's questions.
- Delete the two old Render variables (`CIC_API_ANON_DAILY_SESSION_LIMIT`, `CIC_API_ANON_DAILY_TURN_LIMIT`) and the two old GitHub branches (`claude/paid-run-gate`, `claude/claude-md-spend-step`).
- The `.claude/settings.json` allow-list addition (text in the session; a session may not edit its own permissions).
- LPC starts next, after the big project; its scoping questions are in Pilot_Feedback_Decisions.md, "Promotion, Theon card, LPC next".

## 5. Next step

Open Pilot_Feedback_Log.md and Pilot_Feedback_Decisions.md, then ask Mark one thing: which of the items in section 4 to take first. Do not start a second big project until the finish line in section 3 is met.

## 6. Spend

Allowance share used: not tracked. Metered: none. No model call, live test or paid service was used outside this conversation; one Opus review subagent ran inside it.
