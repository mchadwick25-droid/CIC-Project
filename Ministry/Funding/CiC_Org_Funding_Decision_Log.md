# CiC Org, Funding & Branding Strategy — Decision Log

Dated entries. Each records what was decided (or what's still open), the reasoning — including the "heart" reasoning, not just the operational one — and the specific next action. A decision that only lives in conversation history is a decision that gets re-litigated by accident later.

---

## 2026-07-08 — Thread launched; first bridge memo drafted, not yet reviewed by Mark

**Status:** Draft complete, not yet reviewed by Mark. Per this project's standing discipline (full documents shown in full, not summarized), the draft is being handed to Mark in full before any version is treated as ready to act on.

**What it covers:** A short, actionable memo (not a full nonprofit business plan) with three parts, per the thread's launch brief:

1. Bridge-funding recommendation — lead with the Letter to Friends as already drafted (informal/direct support), begin a fiscal-sponsorship search in parallel rather than sequentially, with an explicit trigger (asking beyond personal network, or a gift large enough that tax-deductibility matters) for when to lean on the sponsor rather than informal giving.
2. Legal-structure framing, not yet decided — nonprofit named as the directional lean, reached via fiscal-sponsorship-first rather than a direct filing, with the real tradeoffs (donor tax-deductibility, control, formation time/cost, grant eligibility) named per option in a comparison table. The tension between a nonprofit board and Constitution Article 36's current sole-builder governance is named explicitly, not smoothed over, and framed as a question worth putting to Mark directly (is the hesitation about structure, or about outside control over formation-integrity decisions).
3. External scholarly reviewer (Article 31) — named as a deferred gate that must clear before Prototype Beta (per Phase Structure V1.1), not a someday item. Flagged that Article 35 Section B categorically excludes AI review (including Opus adversarial review) from satisfying this requirement. The CO-020 finalization-integrity fix was named per the launch brief as the reason this became more urgent, without assuming what CO-020 actually surfaced — that's asked of Mark directly rather than inferred.

**Reasoning:** Grounded in the Vision/Convictions document, Constitution Articles 31 and 35(B), the existing (thin) Ministry Funding Strategy v1.0, the Phase Structure document's actual gate definitions, and the existing FAQ/Letter to Friends communications material — read for tone and existing framing, not for current factual claims (both are written around Theon/Alexandria as the flagship example, which the scope note explicitly excludes from grounding this thread). Did not read `Archive/Alexandria-Build-History/marketing/`, per the launch brief's explicit scope note. The bridge-funding recommendation leans on a real finding: the Letter to Friends is already written as an informal, non-grant ask sized to Prototype Alpha/Beta costs — it didn't need to be invented, it needed to be recognized as already fit for purpose.

**Open, not yet answered:**
- Does Mark already have a specific person in mind for the Article 31 external reviewer, or does an active search need to start?
- What did the CO-020 finalization-integrity fix actually surface, and does it change the timeline urgency named in the launch brief?
- Does Mark agree with the nonprofit-via-fiscal-sponsorship lean, or is there a control/board concern the memo hasn't surfaced yet?

**Next action:** Mark reviews the full draft memo (saved to `Ministry/Funding/CiC_Org_Funding_Bridge_Memo_V0_1_DRAFT.docx`). Revise per his reaction before treating any version as final or actionable.

---

## 2026-07-08 — Cost model built out: usage economics, voice/model levers, reviewer market rate, Phase 1 budget

**Status:** Working numbers produced across the session, culminating in a full Phase 1 budget workbook. Not yet reviewed or approved by Mark — treat as a planning draft.

**What was established, in sequence:**

1. **Per-user usage cost.** Working from the Front-End Engineering Spec's own deployment-package architecture (World Capsule Core, Priority Layer, retrieved chunks) and current Claude/ElevenLabs pricing, a 2-hour/month user costs roughly $4–8 unoptimized (~$6/user), or roughly $2–3 optimized. Full token-level buildup lives in the budget workbook's Unit Economics tab.
2. **Cost-reduction levers identified, in order of impact:** prompt caching (90% discount on repeated context, and it gets *more* valuable as user count grows since the same world content is shared across sessions) is the single biggest lever; cheaper voice (Google Chirp 3: HD at ~$30/M characters vs. ElevenLabs' $50–100/M) cuts voice cost roughly 65%, with an explicit quality tradeoff flagged, not yet A/B tested; model routing (Haiku for the frame-breaker classifier, reserving Sonnet/Opus for actual Representative generation) is a smaller but close-to-free win. Mark's own instinct toward a tiered "capstone plus deeper database" content structure turned out to already be the documented Layer 2/Layer 3 retrieval architecture in the Front-End Spec — confirmed, not invented — though the retrieval system itself (Layer 7) isn't built yet.
3. **Article 31 reviewer market rate.** No list price exists for this; reasoned from adjacent comparables (university press manuscript review, academic consulting rates) to a range of $500–1,500 for a relationally-sourced scholar (matching the Letter to Friends' own "introduce me to a scholar" ask) up to $2,000–5,000 for a cold, formally-engaged specialist. Labeled Inferential/Thin, consistent with the project's own confidence vocabulary — this is a genuine estimate, not a quote.
4. **Phase 1 budget.** Built as a full workbook (`Ministry/Funding/CiC_Phase1_Budget_V0_1_DRAFT.xlsx`) with editable assumptions, not just a memo table — Mark asked for a budget, and the underlying numbers have enough real moving parts (adoption scale, engineering scope, model/voice choice) that a static number would have hidden more than it showed. Explicitly excludes any stipend for Mark, per his direct instruction this session. Three headline scenarios: Lean case (~$37K/year: 250 users, optimized engineering, low Bucket B) · Planning estimate (~$114K/year: 1,500 users, optimized engineering, blended Bucket B) · Conservative case (~$849K/year: 10,000 users, unoptimized engineering, high Bucket B).

**Reasoning:** Split the budget into two buckets on purpose, not as a formatting choice — Bucket A (usage-scaling: inference + voice) needs revenue that scales with usage; Bucket B (fixed ministry cost: reviewers, engineering, hosting) is what grants and institutional partnerships are actually suited to fund, matching the phase language already in the existing Ministry Funding Strategy doc. Every hardcoded number in the workbook is sourced or labeled with its confidence level in the Assumptions tab's Notes column, rather than presented as more certain than it is — the single least-grounded line is the Phase 1 engineering build-out estimate (150–400 hours, flagged yellow in the workbook), because the Deployment Standards document that would actually scope it doesn't exist yet.

**Open, not yet answered:**
- Does the ElevenLabs-vs-Google-Chirp-3-HD voice quality tradeoff actually hold up for this project's specific need (culturally/gender-matched, emotionally expressive per-Representative voices)? Not tested.
- What's the real Phase 1 adoption assumption Mark actually expects — the workbook uses 250/1,500/10,000 as placeholder low/medium/high scenarios, not a stated target.
- Should the Phase 1 engineering build-out get a real scoping pass (ideally from the specialist engineer at Engagement One) before this budget is used in any actual fundraising ask?

**Next action:** Mark reviews the budget workbook. When ready, layer in a stipend line for Mark (explicitly deferred, not decided against) and firm up the adoption and engineering-scope assumptions once real information exists.

---

## 2026-07-08 — Per-world annual cost added; Equivice surfaced as a near-term operational vehicle; front-end build scope still open

**Status:** Workbook extended with a "Per-World Annual Cost" tab. New factual information from Mark (an existing registered business, Equivice — Equipping to Serve, currently used for consulting) changes the bridge-funding picture from the first memo. Not yet reflected in the memo itself — flagged for a revision pass.

**Per-world annual cost, added to the workbook:** Development (Claude doing the research/drafting/review for one world) prices out at roughly $4–14 in raw API-equivalent terms — genuinely small, confirming Mark's own intuition, and a useful honest finding in its own right: build-time AI cost is a rounding error next to the human-cost lines. External scholarly review (Article 31, one world): $500–3,500, same range established earlier. A year of runtime scales hard with audience size: roughly $1,400–3,700 for 50 users/year, $6,900–18,300 for 250 users/year, $27,600–73,300 for 1,000 users/year. Headline one-world/one-year figure at a medium (250-user) audience: **~$7,400 (optimized) to ~$21,800 (unoptimized)**.

**Equivice — new information, real implications:** Mark has an existing registered consulting business that could host CiC operationally. Reasoning laid out for him: strong fit as an expense-paying vehicle right now (hosting, API costs, contractor invoices) — zero additional setup time, already has business banking. Weak fit for taking in tax-deductible donations — a for-profit consulting entity can't offer donors a deduction, and depositing donor-labeled money into a business's revenue account risks real tax/legal complications (unclear characterization of the inflow, muddies the books if a future nonprofit spinout needs to show clean separated ministry financial history). Flagged explicitly as not-a-lawyer-or-accountant territory — recommended real advice before mixing any externally-designated ministry money into Equivice's books. Proposed a three-part structure: Equivice for expenses now (already available) · fiscal sponsorship for tax-deductible donation intake once that's needed (per the original bridge memo) · direct nonprofit filing as the eventual destination. This is more concrete than the original memo's two-option framing and should update Section 1 of the bridge memo once Mark reacts.

**Front-end build scope — asked, not yet answered:** How much of the Phase 1 feature build-out (retrieval systems, Runtime State Model, animated table, transparency apparatus — all named "not built" in the Front-End Spec) Mark can do himself, possibly AI-assisted, versus needs a hired specialist engineer, is unresolved and directly affects both the engineering line in the Phase 1 budget and the near-term hiring/spending decision. Asked directly via a multiple-choice question rather than assumed.

**Reasoning:** The per-world framing was a genuine reframe Mark asked for — cost-per-unit-of-mission (one world, one year) rather than cost-per-whole-system, which is arguably the more natural unit for a donor or grant committee to reason about ("what does it cost to bring one more world to the table"). Kept it inside the same workbook rather than a separate file so the numbers can't drift out of sync with the Phase 1 totals — both tabs pull from the same Assumptions sheet.

**Open, not yet answered:**
- Does the three-part Equivice/fiscal-sponsor/nonprofit structure make sense to Mark, or does he see it differently?
- Should the bridge memo (V0.1) get revised now to incorporate Equivice, or wait until more of this thread's open questions settle?

**Next action:** Revise the bridge memo's Section 1 once the Equivice-based three-part structure is confirmed or corrected.

---

## 2026-07-08 — Front-end build: Mark builds most of it himself, budget updated

**Decided:** Mark builds most of the Phase 1 feature set himself (retrieval systems, animated table, transparency apparatus), rather than hiring it out. The two bounded specialist-engineer engagements already named in the Front-End Engineering Spec — Engagement One (initial deployment setup) and Engagement Two (pre-public-availability audit) — stay hired regardless; those weren't part of the choice.

**Reasoning:** Asked directly rather than assumed, since this is a fact about Mark's own capability and appetite that no document could answer. His choice was the most self-directed of the four options offered (full hire-out, AI-assisted-DIY-with-hired-hard-parts, mostly-DIY-with-bookends-hired, not-sure-yet).

**Budget impact:** Updated both the Assumptions tab and the Phase 1 Budget tab. The old single "Phase 1 feature build-out" hired-hours line (150–400 hrs × $125–200/hr = $18,750–$80,000) is replaced by: (a) a DIY line reflecting only AI-assistance token cost, which is genuinely small ($30–$110) but doesn't count Mark's own time; and (b) a separate, not-committed "hire-out fallback" reserve ($7,500–$30,000) scoped specifically to the two pieces even the project's own engineering spec calls hardest and unvalidated — retrieval systems and the Runtime State Model — in case the DIY attempt stalls there. Bucket B's committed subtotal dropped from $29,950–$115,500 to $16,230–$51,610; the three headline Phase 1 totals dropped to roughly $23,140 (lean) / $75,379 (planning estimate) / $784,858 (conservative).

**Open, not yet answered:**
- Whether the reserve ever gets triggered — genuinely unknown until Mark is partway into the DIY build.
- Mark's own time isn't costed anywhere in this budget. Worth deciding later whether that should be made visible some other way (e.g., an implied stipend/time-value line) even while his direct-pay stipend stays deferred.

**Next action:** None blocking — budget reflects the decision. Revisit the reserve line if the DIY build hits the retrieval-system/Runtime-State-Model wall.

---

## 2026-07-08 — Workbook repaired after on-disk corruption; confirms this thread's own DIY decision, flags a conflict with the front-end thread's proposal comparison

**Repaired:** `CiC_Phase1_Budget_V0_1_DRAFT.xlsx` was found corrupted (truncated write, missing zip table of contents) while cross-checking it against a different workbook. Fixed by recovering the raw XML streams directly — every number and formula is byte-exact recovered, not recalculated. The workbook's shared-string text table was itself cut off near the end, so roughly the last third of its text labels (most of the Per-World Annual Cost tab, and the Phase 1 Budget tab) had to be rewritten rather than recovered verbatim — grounded in the recovered formulas and this log, flagged plainly in the file's own Read Me tab. The recovered numbers confirm exactly the "Mark builds most of it himself" figures in the entry directly above: Bucket B subtotal $16,230–$51,610, headline totals ~$23,140 / ~$75,379 / ~$784,858.

**Real conflict worth naming:** the front-end thread built a separate four-way hire-vs-DIY comparison (`CiC_BuildApproach_Budget_Proposals_V1_0.xlsx`) that treats hire-vs-DIY as still open — it doesn't know about the decision recorded directly above. The two workbooks also price DIY engineering differently: this one uses raw API/token cost ($30–110), the other uses a monthly tool-subscription estimate (Claude Code, ~$480–2,304/yr). Both are legitimate ways to estimate the same thing, but only one should be treated as current.

**Next action:** Reconcile the two workbooks — confirm the DIY-primary decision stands, and pick one DIY-cost methodology going forward. This directly feeds Mark's request for "a more realistic and detailed plan, keeping cost in mind."

---

## 2026-07-21 — Business-as-Mission direction confirmed (nonprofit's academic-review idealism deemed unfundable now); go-live cost model built from direct code/site inspection

**Context:** Mark confirmed his own conclusion following the PBC analysis: a fully academically-reviewed nonprofit isn't fundable at this time; moving to a business-as-mission strategy now, holding the door open to convert to nonprofit later if a funding path opens (matches the PBC memo's own framing — the two paths aren't as operationally divergent as they sound, and this is easier to walk from business-to-nonprofit than the reverse if a grant path appears). Separately: churchinconversation.com and .org are secured, a business name is saved, and Mark reports "we are ready to go full live on a website" with more features built than earlier budget models assumed. He asked for a direct look at the actual current state and a minimum-viable go-live cost figure — hosting/API coverage plus "some AI tool access money."

**Method:** direct inspection, not assumption — the live site (churchinconversation.com, confirmed reachable), the `cic-poc` codebase (config.py, Dockerfile, graph/nodes.py, message_cap.py/session_cap.py, rag/ embedding provider), the Task Board (2026-07-21), and live current pricing for Render/Fly.io.

**Deliverable:** `Ministry/Funding/CiC_Go_Live_Cost_Model_V0_1.md` (+ side-panel artifact 07f0af02).

**Headline findings:**
1. **The marketing/Atlas site is genuinely live** — churchinconversation.com serves a real, polished 178-movement census across ten eras, five worlds open for conversation, confidence-labeled per this project's own transparency standard. **The literal, entire gap is that `cic-poc` (the conversational app) is built but not yet hosted anywhere** — the live site's own "Launch a Conversation" button says "opening here directly as soon as hosting is finished."
2. **The feature set is bigger than earlier budget models assumed:** multi-Representative "Living Table" rounds (not just 1:1 interviews), a frame-breaker classifier and relational-safety/distress mechanism (both live-tested this week, 19/20 clean, real API calls, all 5 worlds), model routing already implemented (Sonnet for full responses, Haiku 4.5 for all classifiers/monitoring — confirmed in code), local embeddings (no separate API cost for retrieval), and the whole app already packaged as ONE deployable Docker service (frontend+backend, one process) that Render/Railway/Fly.io pick up automatically.
3. **Two known open items, neither a launch-blocker:** a rare content-isolation defect (root cause not found, but now fully traceable via per-call logging) and a de-escalation-timing question from this week's safety test (narrow, needs a quick retest). The core safety mechanism itself already cleared live adversarial testing.
4. **The real cost is small:** hosting = **$7/month (Render Starter)**, confirmed via live pricing search. The one real caveat: no per-visitor identity cap is active (Supabase deliberately off at this stage per Mark's own 2026-07-20 decision) — the only backstop is a 60-turn-per-conversation cap, so the Anthropic Console spending limit is the actual risk-control lever, not a bigger dollar figure. Using this project's own converged unit economics (cross-checked twice already this session: $0.28–1.10/user/month, ~$0.20–0.35/conversation), adjusted conservatively upward for Living Table's multi-Representative rounds (~$0.30–0.75/conversation): **a $100–150 initial spending ceiling covers roughly 150–500 real conversations.**
5. **Total minimum to go live: ≈$110–160**, then ~$7/month hosting plus actual API usage thereafter, bounded by the console limit and adjustable as real traffic data comes in. Named plainly: going live is the cheapest concrete step in this entire funding conversation, not the expensive one.

**Open — needs Mark's clarification:** "AI tool access money" could mean either a development-tool subscription (e.g., Claude Pro/Max or Claude Code, ~$20-100+/mo, a separate ongoing line) or was a second way of naming the same Anthropic API spending already priced above. Flagged directly in the memo rather than guessed.

**What's left, Mark's to do (not Claude's — account creation is off-limits per standing constraint):** create a Render account + Web Service (root dir `cic-poc/`); set `ANTHROPIC_API_KEY` + `CORS_ORIGINS` env vars; set the Anthropic Console spending limit; point the site's "Launch a Conversation" button at the live app URL once deployed; optionally retest the de-escalation timing question first.

**Next action:** Mark answers the "AI tool access" clarifying question; once the Render account exists and env vars are set, going live is a same-day step, not a fundraising-dependent one.

**Addendum (2026-07-21) — "AI tool access money" clarified; combined monthly total set.** Mark confirmed: $200/mo currently, budgeting $250/mo — a Claude subscription (Max-tier range, given "access to Fable," a subscription perk) for his own continued development, separate from the pay-per-token `ANTHROPIC_API_KEY` billing that powers `cic-poc` for real visitors. Both run concurrently once live; they don't offset. **Combined monthly total to plan against: ≈$357-407/month at launch** ($250 dev subscription + $7 hosting + $100-150 live-API ceiling). Mark's own expectation, worth holding: the $250 subscription line is a build-phase cost that should shrink once initial development eases, unlike hosting/live-API which are the product's true ongoing operating cost. Go-live cost model updated in place (same artifact, 07f0af02).

**Addendum (2026-07-21) — $125-fixed-cost scenario and a monetization ladder added.** Mark asked how capacity changes if fixed costs (subscription + hosting) drop from $257 to $125/month within the same $500 total, and how to start covering API costs after a good first month. At $125 fixed, variable/visitor budget rises from ~$243 to ~$375/month → roughly 500-1,250 conversations, 330-830 people, 125-520 hours (same ranges/caveats as the $257-fixed case, scaled). **Monetization ladder built, ordered by speed not ceiling:** (1) a simple no-code Stripe Payment Link / Ko-fi tip ask, live in days, no accounts/gating needed — realistic expectation using this project's own evidenced 2% conversion benchmark (Wikimedia's stated figure, not optimism): ~$30-160/month from a good first month's audience, close to covering a modest bill on its own; (2) a recurring Stripe Checkout "Supporter" pledge, a week or two out, still no feature-gating; (3) turning on the already-built-but-off Supabase auth to gate a real feature behind payment — real engineering, only worth it once (1)/(2) show signal; (4) institutional licenses — the real engine, relationship-driven, runs on its own clock regardless of online-giving performance. Recommended sequencing: run (1) immediately alongside launch (costs nothing, starts collecting real data), escalate only as each rung proves itself. Same artifact updated in place (07f0af02).

**Addendum (2026-07-21) — ask copy finalized; Mark's own honesty catch recorded.** Mark chose the directional "where this goes" language over the literal "100% of contributions" claim, then caught a real, symmetrical precision issue: narrowing that language to "covers hosting and API" would be just as inaccurate as the unbounded "all contributions" version, since running this includes real infrastructure and, eventually, staff — not only server costs. **Finalized two-level ask copy, recorded in the artifact:** (1) the ask line ties a specific gift to a concrete, calculable unit — "$10/month keeps the Table open for ten more seekers" (a real equivalence from the project's own ~$1/user/month cost basis, not an invented multiplier); (2) the "where this goes" line honestly widens to "the technology, the people, and the work it takes" rather than narrowly hosting/API. Both true at their own level; neither overclaims narrow, neither overclaims total. Suggested amounts set (evidence-based anchoring, not open-ended): one-time $10 (options $5/$10/$25/other), recurring $8/mo (options $5/$8/$15/other). Same artifact updated in place (07f0af02).

**Addendum (2026-07-21) — PBC Articles of Incorporation drafted, the unlock for the monetization plan.** Full entry and document: `Ministry/Organization/CiC_PBC_Articles_of_Incorporation_V0_1_FILING_READY.md` (+ artifact c8e60006), logged in full in the nonprofit-formation decision log (same date). Mission-lock language carried over from the nonprofit draft; PBC-specific mechanics (specific-public-benefit purpose, authorized shares, annual benefit report, share-based amendment protection) verified against the CO PBC statute research already done this thread. This is the concrete precondition for the business bank account + Stripe account the monetization ladder (above) depends on.

---

## 2026-07-22 — Dedicated Funding Strategy thread opened as a live, ongoing exploration; full detail lives in its own log, not duplicated here

**What changed:** System Hub dispatched a standalone thread (`Ministry/Operations/Standing/Launch-Prompts/CiC_Funding_Strategy_Thread_Launch_2026-07-22.md`) specifically to design the actual monetization model with Mark, live and turn-by-turn — not a background task converging to a recommendation on its own. Full working record now lives in `Ministry/Features/Funding-Strategy/Decision-Log.md`; this entry cross-references rather than repeats it, per this log's own convention of not competing with a more specific thread's own record.

**Headline outcomes worth surfacing here, since they affect this log's own prior entries:**
- **A load-bearing principle now governs every funding idea downstream:** rigor and sourcing are never for sale; genuinely additional, costly-to-build services are fair to charge for. Resolves the tension this log's own monetization-ladder entries (2026-07-21) hadn't yet had to face directly.
- **A real course-correction:** the institutional-funding groundwork this log already recorded above (World Sponsorship, Church-Designated Fund, Seminary Alignment/Wabash) was drafted under the project's earlier, more idealistic posture and depends on a third party's yes on a third party's clock — the same shape of mistake that already drove the nonprofit-to-PBC pivot this log documents. That work stays useful as a source of ideas, not as the near-term plan.
- **A real gap found in the 2026-07-21 nonprofit-to-PBC cleanup:** two `.docx` files in this same `Ministry/Funding/` folder (`CiC_World_Sponsorship_OnePager_V0_1_DRAFT.docx`, `CiC_Church_Designated_Fund_OnePager_V0_1_DRAFT.docx`) still promise a tax-deductibility bridge that no longer exists — missed because that cleanup's repo-wide grep can't see inside a zipped `.docx`. Fix dispatched, not yet run: `Ministry/Operations/Standing/Launch-Prompts/CiC_System_Hub_Funding_Docx_TaxStatus_Fix_2026-07-22.md`.
- **Payment mechanism, held as a working decision, not final:** direct Stripe on-domain, per the path this log already set 2026-07-21 — Patreon and Ko-fi evaluated and set aside (real current numbers, not assumptions), Ko-fi specifically noted as a good fit if this gets revisited.
- **A five-stream portfolio frame** (time-bounded free/membership, segment-tailored add-ons, creative validation funding, other revenue, database-leveraged products) opened, not yet sequenced. One idea from it — a parallel-presentation cross-tradition comparative brief for pastors, explicitly not synthesis — refined live and parked for a future comprehensive business plan, not scheduled now: `Ministry/Features/Funding-Strategy/Business-Plan-Idea-Box.md`.

**Next action:** ongoing in the dedicated thread; no convergence forced. Update this log again only when something decided there is significant enough to affect the org-level picture this log tracks.

---

## 2026-08-09 — Table cost feasibility (Phase 1 analysis): the table is a paid-tier feature or it is not affordable — with real numbers, awaiting Mark's accept/reject

**Status:** Analysis, not a decision. Produced by the multi-Representative-table thread's Phase 1 (cost only, no code touched); full document at `Ministry/Technology/Table/T1_cost_feasibility_2026-08-09.md`, every figure reproducible via `t1_table_cost_model.py` beside it (reconciles against the committed B-COST log before it will run).

**What the analysis found, in this log's terms:**

- The honest measured table cost is **$0.197/round ($4.73/hr at fast pacing)** — Mark's "can't afford $5/hour" is confirmed real at the current shape, not rhetorical. (Two record corrections along the way: the report's $0.1585 averages in two free capped turns; the run notes' "≈$0.38/turn" headline double-bills cache tokens and is ~2× high.)
- The recommended target architecture — two lossless fixes plus capping a round at 2 representative turns, a principle the table's own governance already states — lands at **$0.135/round ≈ $3.25/hr fast / $1.35/hr contemplative**. The honest floor for anything still deserving the name "table" (Sonnet voices, full safety stack, two voices per round) is **≈$0.11/round**.
- **Against free-tier economics (the ~$1/user/month anchor the live ask copy is built on), the table cannot be done** — that would require gutting the second voice, the Sonnet voice fidelity, or the safety stack. This is the honest-floor answer the phase gate asked for.
- **Against the paid tier (already decided 2026-07-31, SH-12 scope), it works:** a heavy user (weekly one-hour sitting) costs **$9–14/month**; worst-case single sitting is bounded at ~$6.80 by the existing 100-rep-turn cap. A **$15–19/month** Table tier carries the heavy user with margin; the anchored **$8/month supporter level** is break-even at ~2–3 table hours/month.

**The heart of it:** the feature Mark killed a test run over does not need to die — but it only lives inside the pricing structure he already chose. The free tier's promise ("$10/month keeps the Table open for ten more seekers") stays honest precisely because the expensive room is the paid one.

**Open for Mark:** accept or reject the Phase 1 criterion — table feasible at $0.135/round, paid-tier-only, priced at or above ~$15/month for unmetered weekly use (alternatives if that price is wrong for his people: per-sitting metering against the ~$6.80 bound, or measuring the cheaper-model variant before trusting it). Phase 2 (table quality/1A) stays gated until he answers.

**Next action:** Mark reads T1 §6 and accepts/rejects the criterion; separately, re-run the cost baseline after the five world swaps + PR #9 land to replace the one estimated line with a measured one.

---

## 2026-08-09 — Two-tier pricing shape set as working direction; 5-seat table conditionally approved into the research tier; homeschool bridge scoped

**Status:** Mark's working direction, confirmed in conversation — not final pricing. Built directly on this morning's Table Phase 1 cost analysis (`Ministry/Technology/Table/T1_cost_feasibility_2026-08-09.md`); all dollar figures assume the A3 target architecture ($0.135/table round) and standard API pricing.

**Decided as working direction:**

1. **Multi-voice Table is subscription-only** (re-confirms 2026-07-31). Seats stay at **3 at launch, with a "coming soon" tease for 5.**
2. **The 5-seat cap raise is conditionally approved — this is a deliberate, recorded reopening of S6.2's hard-cap-at-3, not a silent reversal.** The ground shifted: Phase 1 showed cost tracks rep-turns-per-round, not seats — under round discipline, a 5-seat round costs ≈ the same as a 3-seat one. Mark's own framing: "if they can imagine five voices they can have it for very limited increase — it's about choices for the participant." Conditions before the cap moves: (a) the A3 round-shape discipline ships, (b) a 5-voice room passes an actual test (the system has never run one). When it lands, it lands as the research tier's headline feature, not the base tier.
3. **Tier 1 — $15/month:** ~2× free-tier interview time (~100 solo turns) + ~45 table rounds (≈ three one-hour sittings), 3-seat tables. Caps metered in **rounds, not wall-clock hours** (hours punish contemplative readers; rounds track cost). Caps sized to Mark's formula: max-out API ≈ $12.45 = fee covers cost + 20%. Max-out leaves ~$1.75/subscriber after Stripe; realistic 40–60% utilization leaves **~$7–9/subscriber/month** for the operation. The margin lives in under-utilization — the 20% is only the never-lose-money floor.
4. **Launch gate, non-negotiable:** the A3 cost shape (two lossless fixes + round cap) must ship before this tier launches. At today's measured $0.197/round, a maxed $15 subscriber is underwater before Stripe's cut.
5. **Tier 2 — research/academic, ~$29/month:** the 5-seat comparative table (gated per item 2), the transparency apparatus surfaced as a feature (Level 2/3 audit trails, citations, confidence labels, per-world source ecologies — already built as data, near-zero cost to serve), transcript export with citations, curriculum walks, ~2× tier-1 caps. Max-out API ~$24 keeps the +20% formula; realistic utilization leaves **~$15–18/subscriber/month** — this tier is where real margin lives.
6. **Homeschool bridge (Mark, this session): a modified track, not just tier-2 access — add a purpose-built curriculum, and use the Atlas heavily** (the 178-movement census as teaching material). Co-op/classroom pack (pooled family/group cap, ~+$10–15/mo) as the bridge rung toward institutional licenses. Economics note: curriculum and Atlas are build-cost, not serve-cost — one-time authorship served nearly free, and curriculum-path traffic is exactly where the SH-11 answer bank serves cheapest. Design note: the Atlas itself stays public/free (it is the marketing engine); the homeschool product builds ON it, it does not gate it.
7. **Salaries are explicitly NOT funded by these tiers** until roughly 700–1,000 subscribers; the salary engine remains the institutional rung ($1,200–5,000/yr), per the existing funding ladder. The tiers fund infrastructure, Mark's dev costs (~$250/mo covered around 30–40 realistic subscribers), features, and the accessibility pool.
8. **The giving door continues alongside the tiers:** donations open Table time for those who can't pay — at A3, $10 ≈ three one-hour sittings. **Ask-copy recalibration required:** "$10/month keeps the Table open for ten more seekers" is built on the ~$1/user/month solo anchor and is NOT true of table time (~10× dearer); table-framed giving needs its own honest line.

**The heart of it:** two tensions were named and belong in every downstream design conversation. (1) Pay-to-pray — the answer chosen is a *visible* giving door ("someone gave, so this seat is open"), not a paywall with a quiet scholarship form; same cost, different spiritual statement. (2) The homeschool market partly wants catechesis; CiC's convictions are Encounter Over Persuasion. The pitch is "your student meets the sources and the tensions, not a settled narrative" — distinctive to thoughtful educators, disappointing to buyers wanting doctrine-safe content. Which educator CiC is for must be decided out loud before marketing copy exists.

**Open gates / next actions:**
- Define the free tier's monthly allowance (currently uncapped monthly; ~50 solo turns/mo is the working assumption behind "+100%"). Prerequisite for everything above.
- SH-12 scope now includes rounds-based monthly metering, not just subscription status.
- **Minors/safety design pass before any homeschool marketing:** relational safety was designed and tested for adult seekers; parental account structure, under-18 behavior, COPPA/consent all need deliberate answers. The homeschool curriculum work should pair with this pass, since the curriculum is what puts students in front of the system.
- Homeschool curriculum scoping: what it covers, how it uses the Atlas and the Guided-Questions base, who authors and reviews it (Article 31 implications if it makes historical claims).
- Ask-copy recalibration for table-framed giving.
- Mark's final word on the price points themselves ($15/$29 are working numbers).
