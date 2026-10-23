# Handoff — participant-experience design: tokens, buying, optional accounts — 2026-10-23

From session: https://claude.ai/code/session_012jjhAokk8iJ5PiFZ3Tn15r · World or workstream: participant experience, cic-website and cic-poc/frontend (design only) · Branch / PR: claude/participant-experience-design-2026-10-23, no PR (this handoff and one log entry only; no design is written into the repo)

Commissioned by Mark on 2026-10-22 through the system and pilot feedback management thread. Design only: nothing built, no engine or site file touched. Every screen and every word lives in three design canvases (Artifacts) and was put to Mark one decision at a time.

## 1. Done, and how it was checked

| What was done | How it was checked |
|---|---|
| Sources read: the Go Deeper Decision-Log (2026-10-03 to 2026-10-22, decisions 53 and 63 with rulings 1 to 54), Pilot_Feedback_Decisions.md (Themes D and G, Item 29, coupons, no daily reset, the review, the visitor bound, the 3-round change order), go-deeper.yaml, deeperCopy.ts, GoDeeperPanel.tsx, accounts_routes.py's messages, the Accounts Build Plan (artifact GHerMTQjcKNkLKM1GrvK83), the landing page, go-deeper.html and its return page | Each ruling the design rests on is cited by date in the canvases' change list below and in the chat record |
| Research round: how seven consumer products present prepaid credits and sign-in (Claude usage limits, Duolingo Energy, Audible credits, Notion AI credits, Textbelt, Adobe Firefly credits, Transit tickets), by a Sonnet helper, pages opened and cited | Report in the session; three pages cited to Mark in chat. No repo file. Patterns applied: warn before the wall, name a state not a failure, finish the task after paying |
| Canvas 1, The Room Without an Account: https://claude.ai/artifact/3DjRnJLekCqDXNs8ej7iyf — ten boards: after the first reply, running low, the stop when tokens run out, entering a code, back from Stripe, a code with a link, a crisis turn at a limit, the panel while holding a code, the engine's ten-round close, desktop | Mark chose: the stop as ruled (the Facilitator's line, the panel rises on a phone, sits beside on desktop); "Get more conversations" opens the buy page in the same tab everywhere and returns to the same conversation; all new lines approved as written. Redrawn after the 2026-10-22 change order removing the free 3-round rule |
| Canvas 2, The Buy Page: https://claude.ai/artifact/4Qf4Ms81C147gChMerfdnQ — the Go Deeper page at phone and desktop width, packs first; the return page; the 18-or-over line | Mark chose: packs first; the adult line as a sentence under the packs; all lines approved as written; counts replaced by his own words "550 free tokens every 30 days. 50 to launch a new conversation, 20 to 25 for each question" |
| Canvas 3, The Optional Account: https://claude.ai/artifact/PXwNUfLjJsWxeZ53zWgMcq — fourteen boards: the invitation in the panel, the ⋯ menu signed out and in, the three sign-in steps and the error state, the signed-in room, the home, the recovery code, deletion, a reopened conversation with a crisis turn, the signed-out home, the desktop home, and the masthead board showing where the count, the buy link and the home sit | Mark chose: the invitation is the panel's account section plus one line at the top of the ⋯ menu, nothing on the page; all lines approved as written |
| Opus 5.5 adversarial review, round one full (26 findings: 9 blocking, 8 substantial, 9 notes), round two targeted recheck (two new blocking findings from the fixes), round three on those two | Reports in the session. Round three: both fixed, nothing open at blocking level. What each finding became is in section 3 and section 4 |
| Readability of every new line | Flesch scored by a script in the session: every sentence at ease 60 or above, grade under 8, except three labels of five words or fewer where the formula misbehaves |

## 2. Not done

- The second pass (adult-administered screens for 13-to-17-year-olds and groups) waits on Mark's approval of this first pass.
- Google and Apple sign-in, the passkey offer and Apple's hidden-address prompt (rulings 9, 12, 15) are not drawn: the commission said design for typed codes, no mail provider chosen.
- States with built words that are not drawn: the code-entry errors (`code_not_accepted`, `badCode`, `claimFailed`), the `in_use` and door lines, the Table room with its `too_few` line, the confirm step for deleting one conversation, export with its fresh code, change of address, sign out everywhere. The fixed Facilitator line past a visitor's monthly count (visitor-bound ruling 1) has no words yet; it needs a board once the build thread has them.
- The pilot page's age line (review finding F9) was not in this commission.

## 3. Re-check before you trust it

- The return to the same conversation after Stripe rests on a Stripe fact Mark took himself on 2026-10-04 (whether the return redirect can carry the person back). The Return page carries the fallback. Not verified here.
- "They return 30 days after you first used them" (the stop panel) was checked by the Opus reviewer against `engine/deeper/free.py`: true as the engine stands, counted in whole days, and at some door stages less than 550 returns.
- The delete screen says the review copy goes with the account, following ruling 20 (2026-10-22). Ruling 1 of the same entry says the review copy lasts its 90 days. Unruled conflict; the screen must not ship until Mark rules.
- The expiry and refund sentence on the buy page is the 2026-10-12 draft and still waits on the lawyer (questions 8 and 14). Not approved for use; approved only as the shape of the line.
- The buy page canvas had a version saved from its page about an hour before the review fixes were published. That publish replaced four boards from this session's copies. Any hand edit Mark made there is gone.
- The home's conversation list shows the voice and the day only, because the Build Plan's A4 allows nothing from inside a session. Titles are a later value item.
- The "Kept apart" sentence approved on 2026-10-04 is qualified on the buy page ("Without an account, it is never stored with your code either"), because the account store is by design the join between tokens and conversations. The approved "Keep it safe" section was folded into one sentence. Both shown to Mark; see section 4.

## 4. Waiting on Mark

- Change orders to the Accounts Build Plan A4, from his choices in this thread, so the build does not follow the plan instead: no "Not saved to an account" line on the page (the panel's account section and the ⋯ menu line instead); no account strip in the room's bar (the refill day lives in the home); the stop panel's words replace P1's `intro`, `getMore` ("Get more tokens") and `freeLeft` lines.
- The review copy on account deletion: ruling 1 (90 days) or ruling 20 (removed with the account). The delete screen follows 20.
- Whether a free visitor whose allowance is out should see the `spent` line ("Your tokens have run out") instead of the built `no_code` line. The sketches show the built line. A change order on `engine/api/deeper_admission.py` if yes.
- Whether the server should report the day the free window ends, so the panel can name the date. One small field beside `free_left`, for the visitor-limit build thread (session_014kMdzhac3pg4njANzhBJ2m).
- The qualified "Kept apart" sentence and the folded "Keep it safe" section, both changes to lines he approved on 2026-10-04.
- Whether the first pass is approved, so the second pass can start.

## 5. Next step

Put the six items above to Mark one at a time; then open the second-pass canvas (13-to-17 and groups) on his approval. Requirements that fall to other threads, for Mark to route: the free window's end day (visitor-limit thread); the A4 screens and the approved words table (accounts thread, session_01B1iempFrGMkshLMm1PB5qj); the Go Deeper page and `deeperCopy.ts` word changes (whichever thread Mark names).

## 6. Spend

Allowance share used: not tracked. Metered: none. No model call, live test or paid service outside this conversation. Helpers: one Sonnet research run (about 90k tokens) and one Opus reviewer across three rounds (about 200k tokens), by the harness's own count.
