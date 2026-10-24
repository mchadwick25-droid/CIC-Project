# Handoff — buying works end to end, build thread — 2026-10-23

From session: https://claude.ai/code/session_018xWVLs9yERzGBV8kYdM8Wn · World or workstream: Go Deeper buying, end to end · Branch / PR: claude/free-count-on-load-2026-10-23

## 1. Done, and how it was checked

| What was done | How it was checked |
|---|---|
| State of buying established | Live `/go-deeper` read over HTTPS (three Payment Links, `noindex`); `/health` commit 469d072c equals the `live` tip; unsigned webhook POST answered 400 "bad signature"; PR 1067, 1055 and 1081 merge commits found in `live` history |
| Free-token count on a fresh page: `GET /api/deeper/free`, asked once when the panel mounts for a visitor with no code | Engine suites in `engine/api/tests` (934 passed, packages restored with `python -m engine.m2.cli restore`); new test `test_the_free_count_can_be_read_before_any_reply`; frontend suite (327 passed) with a new panel test; `check_live_commentary.py --enforce --base origin/main` clean |
| Records | Go Deeper Decision-Log rulings 71 and 72; Pilot_Feedback_Log entry "Buying build thread: state check" |

## 2. Not done

- Mark's real $7 purchase and full refund: not run. Steps were given to him; results are his to send.
- Render `CIC_DEEPER_PRODUCTS` pairing, the Stripe event destination and secret, link redirects, quantity and amounts: not visible from here.
- Stripe's written answer on stored value; the lawyer's answers on expiry and refunds. The expiry and refund sentence stays off the page.
- `noindex` removal and linking the page; the age line on the pilot page; Mark's approval of the visitor experience.
- A visitor holding a code still sees no balance on a fresh page until a reply or code entry. Not ruled.
- Promotion of the ribbon fix to `live`: Mark's, through the runbook.

## 3. Re-check before you trust it

- The handoffs of 2026-10-22 and 2026-10-23 were wrong on four points; see the Pilot_Feedback_Log entry.
- The cost report was already read by Mark on live (Pilot_Feedback_Log, "First live cost report read").
- The Stripe fee on a refund (about 50 cents on $7) is Stripe's usual behaviour, not checked in his account.

## 4. Waiting on Mark

- Check Render and Stripe settings, run the purchase, replay the event, refund, and send what he sees at each step.
- Promote the ribbon fix when ready, through `CiC_Promotion_Runbook.md`.
- Decide whether the buy buttons stay on until the loop is proven (left on).

## 5. Next step

Superseded 2026-10-24 by Decision-Log rulings 80 and 81: buying is suspended (Payment Link slots empty on the buy page) until accounts are built, and accounts and coupons are the two main threads. Mark still has to deactivate the three Payment Links in Stripe. Open from this thread: his purchase-test results (return page, one payment with one code and gap 0, replay adds no second code, refund applied) against the reconciliation and owed lists; version A of the expiry line (ruling 79) goes on the page when sales reopen; the lapse for purchased tokens is not built; the gaps in Pilot_Feedback_Log.md.

## 6. Spend

Allowance share used: modest, Sonnet only, no helper agents. Metered: none. No model call, live test or paid service ran; no purchase or refund was run by this thread.
