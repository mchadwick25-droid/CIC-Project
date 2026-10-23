# Handoff — daily visitor limits removed, visitor bound, free 3-round rule removed, buy page, spend door removed — 2026-10-23

From session: https://claude.ai/code/session_014kMdzhac3pg4njANzhBJ2m · World or workstream: engine/api free allowance · Branch / PR: PRs 1032, 1041, 1044, 1046, 1049, 1050, 1055, 1063 and 1065 merged into main; PR 1067 held open; the door-removal PR is listed in section 1

The thread's scope was Job 1 only. Mark took the accounts research and design (Job 2) out of it on 2026-10-22; the accounts threads own that, and nothing in this thread touched accounts files. The visitor bound and earlier changes went to live with the 2026-10-23 promotion (PR 1056); the cost report (1055), the buy page and the door removal are not on live yet.

## 1. Done, and how it was checked

| What was done | How it was checked |
|---|---|
| PR 1032: the daily counts (5 conversations, 150 messages), the daily Facilitator-only sitting and the paid sitting are removed from `engine/api` and `engine/m4`. The visitor cookie and `CIC_API_ANON_CAP_ENABLED` stay. A conversation no longer counts when created, so a failed first voice reply costs nothing | Engine suites with the Go Deeper module off (1982 passed) and on (842 passed); CI green; new tests in `test_deeper_seam.py`; a mutation check showed the tests fail without the change |
| PR 1041: privacy page cookie section, Mark's words | `test_go_deeper_pages.py`; CI green |
| PR 1044: a monthly count of messages that got a safety check and no Representative reply, 100 per visitor and 200 per network (IPv4 address or IPv6 /56), rolling 30 days, kept as scrambled values in the meter's file. Past it a message gets a fixed Facilitator line with the redirect to real people in it and no model call. A code with tokens left is outside the count. A network free-voice window of 5 allowances (2,750 tokens). Pilot and admin grants count $0 toward the door. One privacy sentence for the new counts | Suites off (2176) and on (934); CI green; new tests cover a crisis, an unclear and a failed safety call past the count, the stream path, a Table, a code holder, a spent and a paused code, a network across fresh cookies, an IPv6 home, a fault in the count, the network window and the daily purge; a mutation check; `check_live_commentary.py --enforce` clean |
| PR 1046: the free 3-round rule is removed. A free conversation is limited by the visitor's tokens and the engine's own caps (`SESSION_TURN_CAP` 10 solo rounds, `TABLE_SESSION_ROUND_CAP` 3, neither lifted). `tokens.free.rounds_per_conversation` is now `example_conversation_rounds`, which limits nothing. Go Deeper page: "Everyone gets 550 free tokens each month. That is about five conversations of three rounds, or two of seven." | Suites off (2186) and on (931); CI green; the page numbers are tested against the operations file |
| PR 1050: `cryptography` pinned to `>=50.0,<51` in `engine/api/requirements.txt` (CI installed 50.0.2), written like the `anthropic` pin; the stale "DRAFT words" note above the visitor-bound line in `engine/m4/facilitator_turns.py` removed, the words unchanged. Merged by another session after the PR was opened here | api, accounts, deeper and m4 suites (2292 passed); the Docker build that installs the pin passed in CI |
| PR 1055: a read-only admin cost report. `GET /api/admin/cost-report` behind the admin login, and a dashboard section "What a round and a safety check cost". It reads the usage log (last 30 days) and shows solo voice dollars by round number, warm against cold cache by the pause before the round, the cost of a safety check, the messages with a safety check and no voice reply, and 7 and 30 day totals. Aggregate numbers only, no model call. `UsageLogStore.read_timed_since` is the one store change, and the "dearest approved price" moved into `engine/m8/price_tables.py` so the module-boundary test passes | 16 new tests in `test_cost_report.py`; the dashboard script parses and rendered a real report in a stand-in DOM; suites off (2473) and on (1028) on the merged result; CI green |
| PR 1063: the Go Deeper buy page built to the approved participant-experience design (canvas "The Buy Page", ruling 59): packs first with a Choose button for each, the 50 and 20 to 25 line, the 18-or-over sentence, How it works, Free to start, Already have a code, Kept apart. Each pack has its own Payment Link slot in `PAYMENT_LINKS`; a pack with an empty link is not shown. The 2026-10-12 expiry and refund draft and the "your conversation is waiting" banner are left off | Page tests (133 passed); checked at phone, iPad and desktop widths; CI green |
| PR 1065: pack cards read "More conversations: 1,100 tokens" with "$7.00", "$15.00", "$30.00"; page title "Get more conversations" (Mark's words, relayed by the feedback thread and confirmed by Mark here) | Page tests; CI green |
| PR 1067 (held, not merged, at Mark's word): sets the three live Payment Links and removes the sentence "With an account, your home holds them on every device" because accounts are not built. Render's `CIC_DEEPER_PRODUCTS` must pair each plink id with 1100, 2750 and 6600 exactly | Page tests (135); held so no working buy button reaches the unlisted page before Mark's $0 test |
| The weekly spend door and its $12 base removed (ruling 69). Free voice has no weekly money cap | Suites on the merged result; see the PR for the counts |
| Records | `Pilot_Feedback_Log.md`: "Daily visitor limits removed", "Visitor bound built", "Free 3-round rule removed" and "Cost report built" |

Words Mark approved, by his own answer in this thread: the Facilitator line past the count; the privacy cookie section (PR 1041) and the privacy sentence for the counts; the Go Deeper page sentence above (his first wording, "between 5 and 10 conversations", was not reachable at the token prices, so he chose the corrected one and dropped the last sentence).

Render: the variables `CIC_API_ANON_DAILY_SESSION_LIMIT` and `CIC_API_ANON_DAILY_TURN_LIMIT` were never set there (Mark checked 2026-10-23), so nothing to delete. The three variables that stay are `CIC_API_ADMIN_TOKEN`, `CIC_API_ANON_CAP_ENABLED` and `CIC_API_ANON_VISITOR_SECRET`.

## 2. Not done

- Promotion of the cost report, the buy page and the door removal: the 2026-10-23 promotion (PR 1056) did not carry them. The cost report route does not exist on the live engine yet.
- Reading the cost report: it needs promotion first, then Mark opens it once while logged in to the dashboard.
- Merging PR 1067 (live Payment Links): held until Mark has run his $0 test (admin or tester code: claim, balance, spend). That test cannot cover the Stripe signature, the link-to-pack mapping, the return page, refund events or reconciliation.
- The three other visitor-facing "Go deeper" wordings (return page eyebrow, `pilot.html`, `privacy.html`): drafts for Mark to approve, not yet written.
- Job 2, the accounts research and design: out of this thread's scope.

## 3. Re-check before you trust it

- Worst-case dollars. Safety checks cost about $0.30 a visitor and $0.60 a network a month at $0.003 a check. Free voice per network, about 96 rounds, costs about $3.10 a month with a warm prompt cache, about $6.00 if the cache is cold on every round (about $0.06 a round, not measured), about $8.70 at the older $0.088 a turn figure. The only measured long session is `engine/m8/reports/live-memory-growth-report.json` (Sonnet 4.5 prices, one world, voice only, warm cache, ten rounds for $0.292). The live usage log was not readable from this thread, so every live figure is an estimate.
- Every live cost figure here is still an estimate until the cost report has been read on live. Review finding F11 is open: the flat 25 tokens a round from round 4 does not follow what long rounds cost.
- A distributed attacker across many networks is not bounded by any per-network figure. With the weekly door removed (ruling 69), the AWS limit is the only backstop, and Mark is handling it.
- Clearing the cookie gives a fresh visitor allowance. The network window and the burst limits now hold that back; the daily count used to.
- Old audits and the Go Deeper turn-on runbook still describe the daily counts as history; not edited.
- `pilot grant` and `admin grant` stay in the meter's note list, now written by nothing, so past records still read correctly.
- The bound is kept in the meter file on one instance; a restart does not clear it.
- Cloudflare's "Workers Builds" check shows failure with "Deployment skipped" on PRs that change no `cic-website` file (seen on 1050 and 1055, not on 1047). It gates nothing and was explained on both PRs; I could not re-run a Cloudflare build from here.
- The cost report's per-round tables cover interview (solo) sessions only; Tables are in the totals. The pause is measured between the ends of voice calls, so it includes the model's own time. A message is rebuilt as every call from one safety check to the next, because the usage log does not record which message a call belongs to.

## 4. Waiting on Mark

- Run the $0 test of the buying path, then say when PR 1067 may merge.
- Promote main to live through `Build/Ministry/Operations/Standing/CiC_Promotion_Runbook.md` when ready; the privacy page, the Go Deeper page and the engine changes go together.
- After the cost report is on live, open it once and report the numbers; then the PR 1046 cost note is updated and Mark is told whether the flat 25 tokens from round 4 under-prices real rounds (finding F11).
- Approve replacement wording for the other "Go deeper" lines when drafts arrive.
- The AWS Budget is Mark's own item, handled by Mark.
- The system and pilot feedback thread's earlier page sentence ("You get a free allowance of tokens each month, and each round uses some of them.") was replaced by the approved design's words; no action.

## 5. Next step

Mark runs the $0 test and says when to merge PR 1067. After the next promotion Mark opens the cost report in the admin dashboard and reports the numbers; this thread then replaces the estimated cost per free round with the measured one.

## 6. Spend

Allowance share used: moderate, Sonnet only, with no helper agents. Metered: none; no model call, live test or paid service ran.
