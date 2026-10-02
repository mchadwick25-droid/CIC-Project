# Opus adversarial review, round 1: Access and Monetization research

Reviewer: Opus 5.5 (high rigor), read-only. Date: 2026-10-02.
Under review: research_track1_access_units.md (T1), research_track2_pricing_ratios.md (T2), research_track3_ledger_stripe.md (T3), research_round2_unit_models.md (R2U), research_round2_free_tier_modal.md (R2F), research_round2_best_in_class.md (R2B), access_decision_brief.html (Brief).
Checked against: CLAUDE.md, the repo (engine/api/anon_cap.py, engine/m4/turn.py, engine/m4/facilitator_turns.py, engine/api/wiring.py, engine/api/app.py, render.yaml, cic-website/privacy.html, Build/Ministry/Features/Funding-Strategy/Decision-Log.md), and web spot-checks.

Only substantive findings are listed. "Could be stronger" is not treated as a finding.

---

## 0. Headline

The research is broad and mostly honest about its sourcing. The ledger and Stripe design (T3) is the strongest part. There are three serious problems:

1. **Safety is missing from all six reports and the brief.** The repo already has two places where a cap blocks a message before the safety gate sees it. The paid-access design copies that pattern. **Blocking.**
2. **The research did not look at what the engine already does.** A 10-exchange cap per session already exists, with its own Facilitator close and an acute-crisis exemption. It was set from a live cost measurement. Internal cost figures also exist. The unit recommendation and the "cap from pilot logs" framing were written as if none of this existed. **Substantial.**
3. **The margin model does not hold up.** The "5x floor" and "61% with a free tier" rest on a free-tier cost assumption (20% of paid inference) that the recommended free tier would exceed by an order of magnitude. **Substantial; blocking for any use in setting prices.**

---

## 1. Numeric checks

### 1.1 Stripe effective-fee table (T2 §3.1, Brief): **correct**
Recomputed at 2.9% + $0.30: $1 = 32.9%, $2 = 17.9%, $3 = 12.9%, $5 = 8.9%, $8 = 6.65% (shown 6.7), $10 = 5.9%, $15 = 4.9%, $20 = 4.4%, $25 = 4.1%, $50 = 3.5%, $100 = 3.2%. The international column (5.4% + $0.30) and the MoR column (5% + $0.50) are also correct. Spot-check confirms 2.9% + 30¢ US, the $15 dispute fee, and the $15 counter fee since 17 June 2025, refunded on a win ([Stripe pricing](https://stripe.com/pricing); [Chargeflow](https://www.chargeflow.io/blog/stripe-dispute-fees)). One caveat: the 5.4% column assumes both the international-card and FX surcharges apply. That holds only when the buyer pays in a currency other than the settlement currency.

### 1.2 Margin-by-markup table (T2 §6.1): **arithmetic correct, model wrong**
CM = 1 − 1/m − 0.044 − 0.11. All 21 cells recompute correctly: 34.6 / 51.3 / 59.6 / 64.6 / 67.9 / 72.1 / 74.6, the free-tier column (−0.2/m), and the $10 column (5.9% fees). The §6.3 P&L ($12.92, then $12.12) also recomputes.

### 1.3 Numeric errors found
| # | Where | Error | Severity | Fix |
|---|---|---|---|---|
| N1 | T2 §3.2 | "$15 dispute fee = three $5 packs' entire margin at 5x." A $5 pack at 5x contributes 1 − 0.2 − 0.089 − 0.11 = 60.1% = $3.00. So $15 is **five** packs, not three. | minor | Correct to five. |
| N2 | T2 §6.3 | "One $15 dispute wipes the contribution of 1.2 packs." A lost dispute also reverses the $20 sale. Inference may already be spent. A contested loss costs $30 in fees. Realistic loss is $35–50 against $12.92 contribution: **about 2.7–3.9 packs**. | minor | Restate, and keep T3's "refund freely, don't contest" policy as the reason. |
| N3 | T2 exec summary vs §6.1 | Summary says 8x ≈ 75% and 10x ≈ 78%. The table says 72.1% and 74.6%. The summary uses a 12% load; the table uses 15.4%. | minor | Use one load figure. |
| N4 | T2 §6.1 reading | "5x is the first multiple that clears a 60% **gross-margin** target with a free tier." The table computes **contribution** margin, and 4x without a free tier is 59.6%. | minor | Name the measure correctly. |
| N5 | T2 §8 Structure A/B | The recommended ladder breaks its own 5x floor. At the $0.50 illustrative cost: $50 / 24 = $2.08 (4.2x); $100 / 52 = $1.92 (3.8x); the 50% honor-system Starter = 2.5x. | substantial | State the floor as a per-ladder **weighted** markup, or drop the bonuses. Today the "floor" is not a floor. |

---

## 2. Findings

### A. Safety (CLAUDE.md "Safety comes first" outranks everything below it)

**A1. A cap or paywall can stand between a participant in distress and the safety gate. BLOCKING.**
- *Evidence (repo, existing):* `engine/api/anon_cap.py` `_anon_cap` middleware returns HTTP 429 for `/message` and `/continue` once the daily turn cap is hit. It runs before the route handler, so the message never reaches `run_gate`. `engine/api/wiring.py` raises `SessionClosed` (409 in `app.py`) before `run_turn` is called. Any message sent to a closed session is refused unscreened.
- *Evidence (proposed):* T3's event flow returns "429 'no conversations left' + offer" at session create when balance is 0. A participant with no balance who arrives in crisis cannot reach the Facilitator at all. The research never discusses distress at the wall, during a capped conversation, or at the end of the last free conversation.
- *Precedent that shows the fix is possible:* `engine/m4/turn.py` already exempts `ACUTE_DISTRESS` from `SESSION_TURN_CAP` ("THE CAP OVERRIDES EVERYTHING EXCEPT A REAL CRISIS"). The same rule is missing at the middleware layer and is absent from the paid design.
- *Fix:* Before design starts, write a design invariant into the access spec: **no balance, cap, allowance or paywall check may sit between a participant's message and the safety gate.** Possible shapes for Mark (options, not a decision): (a) at zero balance or a closed session, still run the safety gate on the incoming message (a cheap gate call) and show the wall only if it does not fire; (b) a zero-balance participant can always open a "gate-only" path. Also: a conversation in which a safety turn fired never captures a unit (release the hold). After any ACUTE/HARMFUL safety state, suppress all commerce surfaces for that visit (Closing Page offer, Threshold Sheet, Sponsored Seat, support ask). Never ask whether the person is okay before lifting the wall. Log the existing middleware/`SessionClosed` gap in the owning `Open_Gaps_Tracking.md` (or as an ACCEPTED_OPEN waiver) now; it is a live defect, not just a design risk.

**A2. The brief's recommended unit ends "with a planned close in the Representative's voice." BLOCKING as written.**
- *Evidence:* Brief Decision 1, option A; R2U ranked input 1 ("Lily pattern"). The engine's existing close is a Facilitator template (`facilitator_turns.session_cap_turn`, kind "close"). CLAUDE.md treats the Representative/Facilitator boundary as governance. A close triggered by a billing ceiling and generated freely in-world is also a fabrication surface (an invented "we must part now" moment). And if it lands on a turn where a safety concern is building, the Representative is the one walking away.
- *Fix:* Present this to Mark as a governance choice (CLAUDE.md "Always ask"), not as part of a research recommendation. The default should remain the template-anchored Facilitator close that already exists.

**A3. R2B §7 misquotes CLAUDE.md.** It says "the redirect **and the wall** are Facilitator-governed (CLAUDE.md)". CLAUDE.md says this about the redirect only. Who voices the wall is a reasonable inference, but it is not a cited rule. **minor.** Fix: attribute it as a recommendation.

### B. The research ignores what already exists in the repo

**B1. A per-session cap of 10 voice exchanges already exists, was set from a measurement, and was not mentioned. SUBSTANTIAL.**
- *Evidence:* `engine/m4/turn.py:79`: `SESSION_TURN_CAP = 10`. It came from Artifact-6-Operations.md ("DECIDABLE, default 40"), was resolved to 10 after `live_memory_growth_run.py` showed per-turn cost **rising** as history grows, and has a Facilitator close plus `session_closed{reason:"cap"}`. Table sessions have their own cap (`table_session_cap_turn`).
- *Effect on the research:* R2U §A speculates about 20–30-turn caps and a "words-exchanged" budget. The Brief says the ceiling must be "set from pilot logs." Neither notices that a 10-exchange cap is in place now, or that cost per conversation grows faster than linearly with length. That second fact bears directly on whether "a question and everything after it" can be sold at a fixed price. WildChat's own figure (3.7% of chats exceed 10 turns) suggests 10 sits near p95 for general chat, and probably below it for reflective use.
- *Fix:* Restate the cap question as "keep 10, or change it by a named change order," with the existing cost-growth measurement as input.

**B2. Internal cost data exists and conflicts with itself. The Brief implies none exists. SUBSTANTIAL.**
- *Evidence:* the `facilitator_turns.py` docstring records `live_cost_run.py` at about $0.25/hour for the single-Representative path, against support.html's $2–5/hour (measured for the Table). The Funding Decision-Log (2026-07-30) records about $2/hour for one-to-one and finds that a third Representative roughly triples per-turn cost. The Brief says "pricing waits on measured cost."
- *Fix:* The Brief should say cost has been measured but the figures disagree by about 8x, and that reconciling them is the first input to the funding thread. Keeping internal figures out of web research was the right method; leaving them out of the decision brief is not.

**B3. Participant-facing copy already in the engine promises a different paid product. SUBSTANTIAL.**
- *Evidence:* the `SESSION_CAP` text (DRAFT): "We're also working toward a paid option built specifically to let a conversation like this run **longer**." Every report designs paid access as **more conversations**.
- *Fix:* A question for Mark (Q1 below). Whichever way he answers, the draft copy or the unit model must change.

**B4. A recorded decision against per-visitor tracking is not mentioned. SUBSTANTIAL.**
- *Evidence:* Decision-Log 2026-08-06 (pilot "door"): "No per-visitor, device, or IP tracking … a per-visitor cap would add tracking/friction." Since then `anon_cap.py` has added a visitor cookie through the security audit. T1, T3 and R2F build the free tier on per-visitor and per-IP metering, Turnstile and claim codes.
- *Fix:* Name the shift as a change to a recorded decision, for Mark.

**B5. "Only pilot logs can supply" conversation length is overstated. MINOR.** Retired-pilot transcripts in Supabase (render.yaml header) and `events.db` / `usage.db` (one row per model call, keyed by session_id) can give a length distribution now, under the current 10-exchange cap. Fix: say a first estimate is available now and is censored at the cap.

### C. Weak, secondary or contradicted evidence

| # | Claim | Problem | Severity | Fix |
|---|---|---|---|---|
| C1 | Brief: "No consumer product found sells conversation only as one-time packs with no subscription." | R2U's own catalogue contradicts it. ChatBuddy (iOS, pay per reply, "no subscription," "credits never expire," not charged on failure) is a consumer AI conversation product on one-time credits. Keen (prepaid per-minute advisor conversations, refundable balance) is a 25-year-old consumer conversation business. HealthTap and Talkspace single-session credits also count. T2's "pure-consumable apps are rare" rests on RevenueCat, a dataset of subscription apps, which is selection-biased (T1 says so; T2 drops the caveat). | substantial | Restate: "rare, and the few examples (ChatBuddy, Keen, per-question services) are small or human-staffed; no public repeat-purchase data exists for any of them." |
| C2 | T1 §1.1, R2F §1.1, Brief context: ChatGPT Free is "~10 messages / 5 hours." | Stale and contradicted by R2B §2.1. Since 6 Aug 2026, plain text on ChatGPT Free is uncapped ([howdoiuseai](https://www.howdoiuseai.com/blog/2026-09-09-chatgpt-dropped-its-message-limit-here-s-what-free); [multichats](https://www.multichats.ai/blog/chatgpt-unlimited-free-messages-explained)). This matters: the main benchmark for "what free AI chat costs" is now unlimited, which sharpens the comparison visitors will make. | substantial | Update T1/R2F; add to the Brief's risks. |
| C3 | Midjourney purchased hours "never expire" (T1, R2F) vs "expire monthly" (R2B §1). R2B §10.5 and principle 19 then cite the "Midjourney purchased-hours rule" as a **positive** precedent for non-expiry. | Internal contradiction inside R2B and across reports. | minor | Verify, then use one statement. Non-expiry does not depend on this example. |
| C4 | T3 §f: Turnstile is "the one control that defeats 'clear cookies, get a new free allowance.'" | Wrong. Turnstile checks that the browser is human, not that the person is new. A human who clears cookies passes it again. It stops scripted harvesting only. | substantial | Restate Turnstile as anti-bot only. Accept and size the human leak (R2F §1.6: ~10% circumvention). |
| C5 | T1 §3.4: one signed-out conversation a week is "small enough that cookie-clearing is more work than signing up." | False; a private window takes one second. | minor | Delete; use R2F's honest framing (accept the leak). |
| C6 | T3 §g: sales-tax "obligation is unlikely to exist yet." T2 §6.4: "below $100k … you generally owe only in your home state (if it taxes digital services)." | Neither names the home state. Faithways is a Colorado PBC. Economic-nexus thresholds do not apply in the seller's home state. Colorado taxes digital goods at state level now. SaaS/software becomes state-taxable on 1 Jan 2027 (HB 26-1223, per secondary sources). About 70 home-rule cities (including Denver, Boulder, Colorado Springs) run their own sales tax and some tax SaaS ([Kintsugi](https://trykintsugi.com/sales-tax-guides/usa/colorado); [1stopVAT](https://1stopvat.com/colorado-sales-tax-saas-software-digital-products-2027/)). Whether "conversation access" is a taxable digital good or a non-taxable service is unsettled; it is a counsel question. It may already apply from the first Colorado sale. | substantial | Replace with: "Colorado obligation may exist from the first in-state sale; get counsel before launch; check the home-rule city." |
| C7 | T1 §2.2, §4.2: "A one-time pack model is outside all of this [ROSCA/auto-renewal]." | True only until T2's opt-in auto-reload is added. Auto-reload is a stored-credential, merchant-initiated recurring charge. Card-network consent rules apply, and the FTC's negative-option posture is the relevant lens. T2 itself calls it "quasi-recurring revenue." | substantial | Qualify the claim. Send auto-reload to Mark as a constraint question (Q3). |
| C8 | Brief: "Lenient refunds raised net sales on Steam." | Rests on one developer's statement ("probably gained them more sales," Rust). The meta-analysis (Janakiraman et al.) is the real support and is about retail returns. | minor | Attribute: the meta-analysis supports it; Steam is one anecdote. |
| C9 | Brief: "a wallet such as Apple Pay lifts checkout … about double when shown early." | Vendor figure via search summary. The Brief's wording reads as "doubles checkout"; the report says roughly 2x the lift from early vs late placement. | minor | Reword and mark as vendor-reported. |
| C10 | Brief: "Rules the evidence supports. One calm notice at the start of the last free conversation…" | R2F §6(a) says no study was found on this; it is inference. | minor | Move it under "reasoned, not tested." |
| C11 | Chai power-law figures, WildChat percentages, the Hallow commitments, NN/g quotes, the Khan A/B test, and Stripe wallet lifts (R2U §A, R2F, R2B) | All "via search summary"; the primary pages were blocked. The reports flag this correctly. The Brief mentions it only in a footnote and drops the flags from its table (HealthTap is an aggregator source; Character.AI "$2.99 lite" is cited without a source in T2, though a spot-check finds secondary reports of a Sept 2026 launch at $2.99, with some citing $4.99). | minor | Keep the flags in the Brief's table, row by row. |
| C12 | T2 §2.1: AI gross-margin benchmarks (ICONIQ 52%, Bessemer) | Mostly high-growth **B2B** software portfolios. Using them as the target for a consumer mission PBC is an analogy, not a benchmark. | minor (but it feeds D1) | Say so where the 60% target is set. |
| C13 | Radar pricing: T2 "$0.05/screened txn" vs T3 "~$0.02 [verify]" | Inconsistent. | minor | Verify once. |
| C14 | R2F §0 says the ranked recommendation is "closing card … followed by a quiet start-another sheet" (D1+D3). §6 and the Brief say D2+D3. | Internal mismatch. | minor | Align §0. |

### D. Recommendations that outrun their evidence

**D1. The 5x markup floor and "61% with a free tier." SUBSTANTIAL; BLOCKING for price-setting.**
- The free-tier line assumes free inference = 20% of paid inference, labeled [L]. The recommended free tier (T1: 1 per device per week signed out, plus 3 welcome conversations, plus 1 a month signed in) combined with the research's own conversion benchmarks (2–5%; Piano 0.36%; Overby 0.21% at a paywall encounter) gives free:paid ratios of **several hundred percent**, not 20%.
- Worked check, with f = free conversations per paid conversation: CM = 1 − (1+f)/m − 0.154. Example: 1,000 visitors each take 1 free conversation, 3% buy one pack of 8, so f ≈ 1000/240 ≈ 4.2. Then CM at 5x = 1 − 5.2/5 − 0.154 ≈ −19%. A 50% contribution margin at f = 4 needs m ≈ 15x; at f = 1 it needs m ≈ 5.8x.
- The 11% operating load is also a planning guess. "Direct API cost" is undefined: it must include the two safety-gate calls per turn, retries absorbed under "failed replies are free," and the superlinear cost growth B1 describes.
- *Fix:* Restate markup as a function of the free:paid ratio and the funding thread's measured cost. Treat free-tier inference as an explicitly funded acquisition/mission line (it may be the "sponsor more free time" stream already in the Decision-Log), not a 4% stress line. Remove "61% with a free tier" from the Brief.

**D2. "1 free conversation per week" (T1; R2B §8 composite). SUBSTANTIAL.**
- No evidence supports this number. It is borrowed from news meters, and it was never tested against cost (D1) or against group use.
- Missed: `anon_cap.mint_seeded_token` seeds every cookieless newcomer's bucket from the shared IP bucket. On a church or classroom Wi-Fi, after about 5 first visits from one IP in a day, every further newcomer is capped on arrival. T3's proposed "≤10 new visitor ids per IP per day" adds a second limit of the same kind. This directly undercuts the church/class pool that every report ranks as the best revenue.
- *Fix:* Hold the number for pilot data, as the 2026-07-22 Decision-Log already decided ("free-tier cap will be set from real pilot data"). Add a class/church path (code-redeemed pool) that skips per-IP seeding.

**D3. The unit recommendation (Brief Decision 1). SUBSTANTIAL.**
- Options A ("a question and everything after it") and B ("whole conversation") have **identical mechanics**; R2U calls A "model 7 wearing model 2's mechanics." The Brief presents them as two options and ranks them on evidence that is about framing. No test supports the claim that the "question" framing reads better. R2U itself flags the risk of under-asking. "Based on how expert Q&A services frame a unit" leans on JustAnswer (under FTC suit, confirmed 13 Jan 2026 ([FTC](https://www.ftc.gov/news-events/news/press-releases/2026/01/ftc-sues-justanswer-deceiving-consumers-enrolling-costly-recurring-monthly-subscription))) and HealthTap (aggregator source; follow-ups are paid extra).
- The promise "keep asking" collides with the existing 10-exchange cap (B1) and with superlinear cost.
- R2U's "follow-up window (days) ends it" makes an open, partly used paid unit close after N days. That is partial expiry, and the "never expires" copy must say exactly what does and does not lapse.
- *Fix:* Present one mechanism (decision-ready; see §4) plus two separate open questions: what the participant-facing name is, and who voices the close (A2). State the window rule plainly: "unused conversations never expire; an open conversation stays open for N days."

**D4. The church licence in the "recommended structure." SUBSTANTIAL.**
- T2 Structure B's group tier is an "annual site licence … repeat annually" (RightNow Media model). That is a subscription. R2U §10 says so and turns it into a one-time pool. The Brief lists "a church licence" under recommended structure and "sold once" under Decision 1, so the two parts of the Brief disagree.
- *Fix:* Remove "licence"; say "one-time church/class pool." Send to Mark (Q4).

**D5. Donation round-up, scholarship pool, "Support the project" lane and Sponsored Seat inside a paid flow. SUBSTANTIAL; blocking for those lanes only.**
- Faithways is a for-profit Colorado PBC.
- The Decision-Log (2026-08-02 onward) records that Stripe twice put the account into charity review and then flagged it under the restricted category "businesses offering a reward in return for donation." The written response to Stripe described a "free/no-paywall product" with "nothing exchanged in return." Adding paid access changes those facts. Putting a "donation" round-up into the same checkout as a purchase is close to the restricted category.
- Gneezy's PWYW lift came from "half to **charity**." A PBC-internal pool is not a charity, and the transfer is unsupported.
- Calling it a "donation" raises misleading-solicitation risk and possible Colorado Charitable Solicitations Act registration (T3 flags it; T2 and the Brief ignore it).
- *Fix:* Hold these lanes until counsel and Mark decide. Stop using "donation" language for any PBC lane. Update Stripe's business description before any paid-access launch. Keep gift and sale records in separate Stripe products (T3 already says this).

**D6. Opt-in auto-reload as a "durability lever." SUBSTANTIAL.** It is recurring charging under another name, against the "one-time, no subscription" constraint, and in a faith context where R2F/R2B document recurring-charge betrayal as the dominant complaint. Fix: Mark question (Q3); if kept, it needs explicit card-network MIT consent and an email on every charge.

### E. Risks the research missed or under-weighted

| # | Risk | Evidence | Severity | Fix |
|---|---|---|---|---|
| E1 | **Privacy: purchases tie identity to religious conversation transcripts.** | `privacy.html` promises "We don't collect your name, email, or any other identifying information as part of a conversation," and says staff review transcripts. T3 links `purchases` (Stripe holds name, email, card) by `visitor_id` to `session_events`. R2F D2/A3 add "Email me this conversation." Religious belief is GDPR special-category data, and T3's "GDPR only if targeted" dismissal does not address sensitivity. Dispute evidence must never include transcripts. | substantial (blocking for launch, not for design) | Make separation a design requirement: payment identity and transcripts are not joinable by staff tooling (store only an opaque grant link; R2B's Signal model). Rewrite privacy.html before launch. Dispute evidence = timestamps and counts only. |
| E2 | **Copy promises the system cannot keep.** | D1/D3 copy: "Your past conversations are saved and you can read them any time" / "Everything you talked about here is saved." There are no accounts, history depends on a cookie, privacy.html has no fixed retention period, and deletion is manual. | substantial | Every guarantee in wall copy must be checked against what is built. This is the "Fabrication at moments of maximum stakes" principle applied to UI text. |
| E3 | **Minors.** | R2U and T2 propose selling to "confirmation classes" and youth groups. There is no treatment of under-13 users (COPPA), minors buying, or the safety posture for minors. | substantial | Mark question (Q8); counsel. |
| E4 | **Refund and return economics at small tickets.** | Stripe keeps its fee on refunds. R2B's self-service "Return this conversation" restores a unit after inference is spent, and is unbounded until a "soft limit" exists. There is no rule for refunds after a safety event (refund automatically and never ask why). | minor | Bound the return rule. Add the safety-event refund rule under A1. |
| E5 | **Faith-sector manipulation in recommended mechanics.** | T1 §4.3 "middle one anchored as the obvious choice"; T2 "best value badge near-universal"; the Sponsored Seat public count ("[n] waiting") as social proof; the honor-system 50% Starter asks people to declare need. R2F's ethical line (badge only if true) is right, but T1/T2 still recommend anchoring. | minor | Adopt R2F's rule across all reports. Drop anchoring as a goal. |

### F. Governance and vocabulary
- Brief "Still open → Review": "before anything is **finalized**." That word is retired (CLAUDE.md). **minor.** Use "approved to proceed."
- Brief "EU buyers owe VAT from the first sale": the **seller** must register and collect (T2 says so correctly). **minor.**
- The Brief does not flag that the 10-exchange cap, the Facilitator close, and paid gating ("rung 3") are prior decisions or DECIDABLE items. Any change is a change order. **minor.**

---

## 3. Does the Brief misstate the reports?

Yes, in these places:
- **C1** (overstated "no product exists").
- **D1** ("61% with a free tier" without its [L] 20% assumption).
- **D3** (presents A and B as different mechanisms; "Recommended by research" where R2U said "ranked input, not a decision" and flagged under-asking).
- **D4** ("church licence," which is a subscription in T2).
- **C8, C9, C10** (anecdote and inference stated as evidence).
- **C2** (stale ChatGPT benchmark carried in from T1/R2F).
- **B2** ("waits on measured cost," when conflicting measurements exist).

The Stripe percentages, the D2+D3 ranking and the dark-pattern rules are reported accurately.

---

## 4. Verdict

### Approved to proceed to design, with fixes A1 and A2 applied first
- Spend mechanics: hold at session start, capture on the first successful Representative reply, release on failure, idle or abandon (T3). Failed or cut-off replies never count. Refresh, back or disconnect never loses a unit. An open conversation is resumable for ≥7 days.
- Purchased units never expire. Priced in dollars per conversation; no abstract currency, minutes, or per-message meter.
- The wall sits between conversations, never mid-reply. It is never in the Representative's voice. The no-dark-patterns rule set (R2F §6) applies.
- Hosted Stripe Checkout on the web, cards and wallets only. Webhook fulfillment on `payment_status=paid`. Dedupe by event id and by object id. Append-only `access_ledger` with `UNIQUE(source_ref)`. Daily reconciliation. Refund freely rather than contest (T3). Turnstile is to be described as anti-bot only (C4).
- The R2B accessibility checklist (native dialog, focus, B2 copy, 24px targets).
- **Added as a design invariant:** the safety gate is never behind a balance, cap or paywall; commerce surfaces are suppressed after a safety event (A1).

### Needs rework before it can inform a decision
- T2 §6 markup and margin model, rebuilt on the free:paid ratio (D1, N5); the remove-"61%" fix to the Brief.
- The Brief's unit section (D3) and market table (C1, C2, C11).
- T2 Structure B: church licence (D4), auto-reload (D6), donation round-up and sliding scale (D5).
- Tax sections in T2 and T3 (C6).
- The free-tier abuse sections in T1 and T3 (C4, C5, D2 shared-IP problem).
- Reconcile with existing repo state: the 10-exchange cap, the cost measurements, the cap copy, the no-tracking decision (B1–B4).
- Privacy and copy-honesty requirements (E1, E2).

### Must wait for pilot data or the funding thread
- Prices, pack sizes, markup multiple, and the Table multiplier (needs the $0.25 vs $2 per hour cost figures reconciled first).
- Size and period of the free allowance (already deferred to pilot data by the 2026-07-22 decision).
- Whether 10 exchanges stays; the short-conversation rule; repeat-purchase and conversion rates.
- Whether any church or class buyer exists.

### Questions only Mark can answer (ask one at a time)
1. Does paying buy **more conversations** or **longer conversations**? The engine's draft cap copy promises longer.
2. Who voices the end of a paid conversation: the existing Facilitator template, or the Representative in-world?
3. Is opt-in auto-reload consistent with "one-time, no subscription"?
4. Is the church/class offer a one-time pool only, or may an institution pay annually?
5. Should gift or "support" lanes share a checkout and Stripe account with paid access, given the restricted-business history? And should any lane be called a "donation" while Faithways is a PBC?
6. Should the free tier move to per-visitor metering, which reverses the 2026-08-06 no-tracking decision?
7. Which safety path at zero balance or on a closed session: gate-on-every-message, or a gate-only path? (Governance; A1.)
8. Will CiC sell to or serve minors, such as confirmation classes and youth groups?
9. May payment identity ever be joinable to transcripts, and what retention period goes into privacy.html?
10. Will he authorize counsel on Colorado and home-rule-city sales tax, and on charitable-solicitation exposure, before launch?

Review cap note: this is round 1 for this research set.
