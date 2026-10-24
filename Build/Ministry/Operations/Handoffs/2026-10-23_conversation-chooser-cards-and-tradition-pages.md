# Handoff — conversation chooser cards and tradition pages — 2026-10-23

From session: https://claude.ai/code/session_012JtxAJXgjVHwaFgyA5iQEQ · World or workstream: cic-website landing chooser and the eleven tradition pages · Branch / PR: claude/zen-cori-x2c5yp, [PR 1005](https://github.com/mchadwick25-droid/CIC-Project/pull/1005), [1006](https://github.com/mchadwick25-droid/CIC-Project/pull/1006), [1007](https://github.com/mchadwick25-droid/CIC-Project/pull/1007), [1009](https://github.com/mchadwick25-droid/CIC-Project/pull/1009), [1010](https://github.com/mchadwick25-droid/CIC-Project/pull/1010), [1066](https://github.com/mchadwick25-droid/CIC-Project/pull/1066) and [1075](https://github.com/mchadwick25-droid/CIC-Project/pull/1075), all merged. Earlier chooser PRs 997, 1001 and 1003 are also merged.

Every change here is recorded with Mark's own words in `Build/Ministry/Features/Conversation-Chooser/Decision-Log.md`. Read that log first.

## 1. Done, and how it was checked

| What was done | How it was checked |
|---|---|
| The role removed everywhere; "tradition" in place of "world" in everything people read (with "Christian tradition" for the first reference); packages rebuilt (PRs 997, 1001, 1003) | Staleness checks and tests passed in CI before each merge; the reading of the wording is Mark's |
| Eleven tradition pages laid out around the tradition, full width, with the recorded text unchanged (PR 1005) | The story, people, stories, after, related and terms sections and the audio lists compared page by page with the earlier versions: 0 differences. Headless browser at 1600, 1024, 820 and 400 px: no sideways scroll, no script errors, one h1, Talk link correct |
| Hand rolls by the arrows only; a card under the pointer no longer jumps above its neighbours (PR 1006) | Headless browser: a wheel turn left the front card unchanged; z-order rose evenly to the front card |
| An era click brings the middle card forward (three or more cards, otherwise the first); a visible scroll bar (PR 1007) | Headless browser: eras with 3, 6 and 2 cards put card 2, 3 and 1 in front |
| The landing page holds the cards' space while they load, so the Family Tree preview does not flash first (PR 1009) | Headless browser on a slowed connection: preview 234 px down before, 1,048 px after |
| A drawn scroll rail on the landing page for use without a mouse (PR 1010; Mark chose it from three options) | Headless browser at 1440, 1024 and 390 px: drag, click on the rail and keys all moved the page |
| Equal picture windows, Theon's portrait shown whole, a quiet "Flip" cue, and each card ending just below "Flip" (PR 1066, PR 1075) | Headless browser at 1440, 820 and 390 px: all eleven windows equal; every card ends 12 px below "Flip" (10 on a phone), tilt switched off to measure. Mark saw before and after pictures |
| All of the above is on `live` and on the public site | `git merge-base --is-ancestor` on the last commit of PR 1075 against `origin/live`: yes. The public site's `chooser.js`, `chooser.css`, `page-rail.js` and `index.html` are byte-identical to `origin/live` (2026-10-23) |

## 2. Not done

- The recorded stories on the tradition pages still say "this world's ...". Changing them means editing canonical story records and re-recording audio. Mark ruled on 2026-10-23: leave it until the deeper rewrite, then re-record.
- About 300 other pages still carry the old header block with the fixed 1000 px breakpoint.
- The word "voice" still appears in the Facilitator's lines (`engine/m4/facilitator_turns.py`) and in the landing lede.
- Each tradition page's own style block still carries rules for blocks that were removed (`.titleblock`, `.plate`, `.ai-line`, `.seat`, `.distress`).
- `Build/worlds/hal/Open_Gaps_Tracking.md` OG-28: the hal voice-craft record still cites the removed `role_label`. Open.
- No live admission test of the changed capsule and Facilitator welcome. It needs a named approval from Mark with a dollar cap (CLAUDE.md 3.2).
- No independent review of the changed Facilitator wording against `CiC_L3D_Facilitator_Governance_V3.6.docx` (CLAUDE.md 4.4).
- The "Start with the hard one" question starters came off the tradition pages when Mark said "build it". He has not said whether to bring them back. They remain in the compiled records.
- Not tested: Safari on a real phone or a Mac, a real trackpad, a screen reader, audio on a phone.

## 3. Re-check before you trust it

- The 0 to 2000 CE timeline scale on the tradition pages is the thread's choice, not Mark's ruling.
- "Cloudflare production follows `main`" is the Promotion Runbook's statement (2026-09-21). It was not checked against the Cloudflare dashboard. The four site files matched both `main` and `live`, so the check could not tell the two apart.
- The Cloudflare "Workers Builds" check showed "Deployment skipped" and failure on PR 1066 and on PR 1064, with no build log and no relation to the files changed. It passed on PR 1075.
- Root files `shot-desktop.png`, `shot-ipad.png` and `shot-phone.png` came in with PR 1063 (the buy page thread), not this thread. They look like stray test screenshots. Flagged, not touched.
- The measurements above were made in headless Chromium. They show layout, not how a real browser draws it.

## 4. Waiting on Mark

- Whether the "Start with the hard one" starters come back on the tradition pages.
- When to plan the deeper rewrite of the recorded stories and the re-recording (his words, 2026-10-23: "we will do a deeper re-write in the near future and then re-record").
- A named, capped approval if he wants the live admission test of the capsule and welcome.

## 5. Next step

Ask Mark one thing: which of three to take first. The old-header sweep of the other pages, the independent review of the Facilitator wording, or the planning of the story rewrite and re-recording.

## 6. Spend

Allowance share used: not tracked. Metered: none. No model call, live test or paid service was used outside this conversation.
