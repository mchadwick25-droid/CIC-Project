# Handoff — daily visitor limits removed, visitor bound, free 3-round rule removed — 2026-10-23

From session: https://claude.ai/code/session_014kMdzhac3pg4njANzhBJ2m · World or workstream: engine/api free allowance · Branch / PR: PRs 1032, 1041, 1044 and 1046, all merged into main

The thread's scope was Job 1 only. Mark took the accounts research and design (Job 2) out of it on 2026-10-22; the accounts threads own that, and nothing in this thread touched accounts files. Nothing here is on live yet.

## 1. Done, and how it was checked

| What was done | How it was checked |
|---|---|
| PR 1032: the daily counts (5 conversations, 150 messages), the daily Facilitator-only sitting and the paid sitting are removed from `engine/api` and `engine/m4`. The visitor cookie and `CIC_API_ANON_CAP_ENABLED` stay. A conversation no longer counts when created, so a failed first voice reply costs nothing | Engine suites with the Go Deeper module off (1982 passed) and on (842 passed); CI green; new tests in `test_deeper_seam.py`; a mutation check showed the tests fail without the change |
| PR 1041: privacy page cookie section, Mark's words | `test_go_deeper_pages.py`; CI green |
| PR 1044: a monthly count of messages that got a safety check and no Representative reply, 100 per visitor and 200 per network (IPv4 address or IPv6 /56), rolling 30 days, kept as scrambled values in the meter's file. Past it a message gets a fixed Facilitator line with the redirect to real people in it and no model call. A code with tokens left is outside the count. A network free-voice window of 5 allowances (2,750 tokens). Pilot and admin grants count $0 toward the door. One privacy sentence for the new counts | Suites off (2176) and on (934); CI green; new tests cover a crisis, an unclear and a failed safety call past the count, the stream path, a Table, a code holder, a spent and a paused code, a network across fresh cookies, an IPv6 home, a fault in the count, the network window and the daily purge; a mutation check; `check_live_commentary.py --enforce` clean |
| PR 1046: the free 3-round rule is removed. A free conversation is limited by the visitor's tokens and the engine's own caps (`SESSION_TURN_CAP` 10 solo rounds, `TABLE_SESSION_ROUND_CAP` 3, neither lifted). `tokens.free.rounds_per_conversation` is now `example_conversation_rounds`, which limits nothing. Go Deeper page: "Everyone gets 550 free tokens each month. That is about five conversations of three rounds, or two of seven." | Suites off (2186) and on (931); CI green; the page numbers are tested against the operations file |
| Records | `Pilot_Feedback_Log.md`: "Daily visitor limits removed", "Visitor bound built", "Free 3-round rule removed" |

Words Mark approved, by his own answer in this thread: the Facilitator line past the count; the privacy cookie section (PR 1041) and the privacy sentence for the counts; the Go Deeper page sentence above (his first wording, "between 5 and 10 conversations", was not reachable at the token prices, so he chose the corrected one and dropped the last sentence).

Render: the variables `CIC_API_ANON_DAILY_SESSION_LIMIT` and `CIC_API_ANON_DAILY_TURN_LIMIT` were never set there (Mark checked 2026-10-23), so nothing to delete. The three variables that stay are `CIC_API_ADMIN_TOKEN`, `CIC_API_ANON_CAP_ENABLED` and `CIC_API_ANON_VISITOR_SECRET`.

## 2. Not done

- Promotion of main to live. Last checked 2026-10-23: `origin/live` was 3 commits ahead of and 78 behind `origin/main`, so every change above is still unpromoted.
- Job 2, the accounts research and design: out of this thread's scope.

## 3. Re-check before you trust it

- Worst-case dollars. Safety checks cost about $0.30 a visitor and $0.60 a network a month at $0.003 a check. Free voice per network, about 96 rounds, costs about $3.10 a month with a warm prompt cache, about $6.00 if the cache is cold on every round (about $0.06 a round, not measured), about $8.70 at the older $0.088 a turn figure. The only measured long session is `engine/m8/reports/live-memory-growth-report.json` (Sonnet 4.5 prices, one world, voice only, warm cache, ten rounds for $0.292). The live usage log was not readable from this thread, so every live figure is an estimate.
- Review finding F11 is open: the flat 25 tokens a round from round 4 does not follow what long rounds cost.
- A distributed attacker across many networks is not bounded by any per-network figure. The door and the AWS limit are the backstop, and the AWS limit is unconfirmed.
- Clearing the cookie gives a fresh visitor allowance. The network window and the burst limits now hold that back; the daily count used to.
- Old audits and the Go Deeper turn-on runbook still describe the daily counts as history; not edited.
- `pilot grant` and `admin grant` stay in the meter's note list, now written by nothing, so past records still read correctly.
- The bound is kept in the meter file on one instance; a restart does not clear it.

## 4. Waiting on Mark

- Promote main to live through `Build/Ministry/Operations/Standing/CiC_Promotion_Runbook.md`. The privacy page, the Go Deeper page and the engine changes must go together.
- Check the AWS Budget: does it stop spending or only send an alert?
- Tell the system and pilot feedback thread whether the 2026-10-17 door switch and the $12 weekly base were intended (no decision-record entry exists for either).
- Raise the $12 base later if busy pilot weeks pause free and pilot voice; pilot grants no longer raise it.
- The system and pilot feedback thread's last message asked for an earlier page sentence ("You get a free allowance of tokens each month, and each round uses some of them."). Mark's own answer in this thread chose the sentence above, and PR 1046 shipped it. If he wants the earlier one, he says so and it is a one-line swap.

## 5. Next step

Mark promotes main to live. After promotion, someone with live access reads the usage log to replace the estimated cost per free round with a measured one.

## 6. Spend

Allowance share used: moderate, Sonnet only, with no helper agents. Metered: none; no model call, live test or paid service ran.
