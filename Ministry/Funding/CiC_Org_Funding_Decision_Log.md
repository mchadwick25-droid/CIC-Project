# CiC Org, Funding &amp; Branding Strategy — Decision Log

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

## 2026-08-09 — Sonnet 5 September price change assessed; provider migration analysed and recommended against; Haiku quality test named as the real decision gate

**Context:** Mark raised the Sonnet 5 price increase ("50% next month") as making the conversations too expensive to run, and asked what other tools exist and what transferring to Gemini/ChatGPT would involve.

**Method:** no live API calls. The project's own committed measurement (`Ministry/Technology/Pass2/baselines/cost_baseline_2026-07_raw.jsonl`, 689 logged calls, four real conversations) repriced at each provider's published rates. New reproducible script: `Ministry/Technology/Pass3/provider_repricing.py`. Full memo: `Ministry/Technology/CiC_LLM_Provider_Cost_Options_2026-08-09.md`.

**Two corrections to the premise, both material to funding:**
1. **The bill rises ~30%, not 50%.** The 50% is correct on the Sonnet rate ($2/$10 intro through 2026-08-31 → $3/$15 standard from 09-01), but 29% of this app's spend is Haiku 4.5 classifier calls, which are unaffected. Measured: solo +30.3%, Table +31.9%.
2. **The plan of record already assumed the higher price.** `Pass3/cost_floor_model.py` (2026-07-30) is hardcoded at $3.00/$15.00. Its $1.61/hr solo and $4.14/hr Table figures are already post-increase. Nothing in the cost plan needs re-deriving. What changes is that the bills Mark *sees* stop being ~24% cheaper than the bills the plan *predicted*.

**The finding that decides it:** repricing the same measured token shape, **Gemini 3 Pro (−29%) and GPT-5.6 Terra (−27%) both save LESS than switching generation to Haiku 4.5 (−47%), which is a one-line config change requiring no migration.** The peer-tier competitors are strictly dominated — more work, more risk, less saving. Only bottom-tier models beat Haiku (Gemini 3 Flash −61%, GPT-5.6 Luna −67%), and they carry the same quality risk Pass 3 already flagged, plus weeks of engineering and the loss of Pass 2's entire evidence base (76 batteries, 34 reviews, 114 gates, 11 safety reruns).

**Migration cost, if ever undertaken:** the four `settings.llm_provider` branch sites are a day's work and are the small part. The real work is that **prompt caching does not port** — four unconditional `cache_control` sites, and 40% of generation cost lives in that machinery. Plus: Anthropic-only `thinking={"type":"disabled"}` (a live bug fix, not cosmetic), cost instrumentation going dark (`usage_logging.py` reads Anthropic-specific fields), and 4–8 weeks of revalidation including the safety batteries. Estimate: weeks, not days.

**Defect found in passing:** the existing `LLM_PROVIDER=openai` path is almost certainly broken today — the `cache_control` blocks are built unconditionally and handed to `ChatOpenAI`, and `.env.example` still advertises `gpt-4o`/`gpt-4o-mini`. It reads as a fallback but isn't one. Should be fixed or removed.

**Funding-relevant levers surfaced, in order of ratio of saving to risk:**
1. Delete the dead `retrieval_filter_*` calls — [M] −33%, zero quality risk, **larger than the September increase, and still not done.**
2. **Route through Bedrock to spend the $200 AWS credit already sitting unused** (`cic-poc/AWS_BEDROCK_SETUP.md`) — ~4–6 months of runway at the current $100–150/mo ceiling, zero quality risk, no prompt change. 1h cache TTL is now GA on Bedrock (verify for Sonnet 5 specifically).
3. Pass 3's lossless + 20%-budget moves → ~$1.42/hr solo.
4. **Run the Haiku 4.5 blind-graded quality battery Pass 3 asked for.** This is the actual decision gate, and it settles the question for *every* cheap-model option at once because it tests the capability axis, not the vendor.

**Named plainly for the funding picture:** the project was already outside its own $0.25–1.00/hr target *at intro pricing*. September widens an existing gap rather than creating one. Separately — the decision log's own 2026-07-21 figures put ~$250/mo of the ~$357–407/mo total on Mark's Claude *development* subscription, not the app's API spend. **That single line is larger than everything this analysis covers.** If the pressure is on the monthly total rather than unit economics, that is the bigger lever and it is not a provider decision.

**Open — needs Mark, and it gates step 4's meaning:** if the Haiku battery comes back ambiguous (voice mostly holds, drops a constraint every ~15th turn in a way no live guard catches), which way does he want to go — hold the costlier model and find the money, accept a measured and disclosed defect rate, or narrow the offering (fewer worlds, no Table) to hold quality at lower spend? This is a Trustworthy Transparency question before it is a budget one: a cheaper model that fails *quietly* is the one outcome the budget can't measure.

**Next action:** Mark to (a) confirm the Anthropic Console spending limit is set before 2026-09-01 — with Supabase off there is no per-visitor cap, so the console limit is the only real backstop; (b) answer the ambiguity question above so the Haiku battery result is actionable when it lands.

**Addendum (2026-08-09) — dead retrieval code deleted; the saving it was supposed to deliver turns out to have been banked already; Mark sets the quality tolerance.**

**Mark's instruction:** delete the dead `retrieval_filter_*` calls, and — answering the open question above — "im ok with a cheaper and a small drop after 15 turns."

**Correction to the entry above, found while verifying the code before deleting anything.** Two things in the recommendation were wrong, and they were my errors, not the cost model's:
1. **The saving was already realised.** S3.4 (Pass 1 R6) had already replaced the batched relevance vote with the local cross-encoder. `evaluate_batch`, `_run_batch` and `partition_tier1_short_circuit` had been sitting *uncalled* in `app/rag/batch_evaluate.py` ever since — `pipeline.py` never imported them. Those calls stopped costing money at S3.4; they appear in the committed baseline only because that log predates the rewiring. `cost_floor_model.py`'s Step 1 header says so plainly ("dead code out, **live path in**"); I read an accounting adjustment as an available action.
2. **The magnitude was wrong.** −33% came from dividing against the wrong baseline. Correctly: the dead calls were 15.6% of the measured run; net of the live `negative_condition` call replacing them, the already-banked saving is **~11%**.

**Done anyway, and worth doing:** 115 lines of uncalled code deleted, plus two stale docstrings that named functions which no longer exist (`retrieval_eval/run_eval.py`, `usage_logging.py`). **Dollar effect: zero.** The real value is that the misleading `retrieval_filter_*` label is now gone from the codebase, so the next cost reading cannot repeat this mistake.

**Corrected funding position — this is the number to plan against.** Per solo hour at September rates: committed baseline ~$1.81 → **true current ~$1.61 (already banked)** → ~$1.42 with the remaining Anthropic-side tuning → ~$0.63 on Haiku 4.5. **There is no large no-risk saving left on the shelf.** The remaining tuning is worth ~12%. That makes the Haiku decision more load-bearing, not less: it is now the only move that reaches the $0.25–1.00/hr band, and it is a config change, not a migration.

**Quality tolerance now set, and it changes the gate's default.** An ambiguous Haiku battery result is now a **PASS**, not a re-run — the battery measures *how large* the drop is, not whether any drop is acceptable. Step 4 can no longer stall. Three riders:
- **The tolerance was given about voice and constraint adherence, not the distress path.** A relational-safety or acute-distress miss is a category failure with no tolerance band, and stays pass/fail. Worth confirming Mark reads it that way.
- **"Small" needs a number before the run**, or whatever comes back will be read as small. Proposed threshold: ≤1 constraint drop per 15 Representative turns on the S4.3 blind-graded shape, same graders, zero safety-category misses.
- **The heart of it, and the part that is genuinely a funding/communications decision rather than an engineering one:** a known, accepted defect rate is compatible with Trustworthy Transparency *only if it is disclosed*. Nothing in the participant-facing copy currently says the Representative can be wrong at a measured rate. Once the battery produces a number, that number needs to reach the onboarding or the confidence labelling. Accepting the drop is defensible; accepting it silently is what this project's own convictions rule out. No decision needed today — but it should not be discovered later, and it belongs to this workstream, not the build thread.

**Next action:** unchanged and now unblocked — run the Haiku battery (needs a live key and nothing else), against the stated threshold. Separately, still outstanding from the entry above: confirm the Anthropic Console spending limit before 2026-09-01.

**Addendum (2026-08-09, later) — generation switched to Haiku 4.5; cache-basis error corrected; the console spending limit remains Mark's to set.**

**Mark's instruction:** "set the console spending limit and switch to haiku."

**Switched to Haiku 4.5.** `render.yaml` `LLM_MODEL` (the Blueprint-managed source of truth for the deployed value), `app/config.py`'s default, and `.env.example` all moved from `claude-sonnet-5` to `claude-haiku-4-5-20251001`. Reverting is one line. The classifier tier is unchanged — `get_monitoring_llm` hardcodes Haiku and always did — so **this changes what the Representatives speak with, not what the safety classifiers run on.** Expected effect: **−47% of the whole bill**, taking solo from ~$1.53/hr to ~$0.83/hr and the 3-world Table from ~$3.95/hr to ~$2.06/hr, i.e. solo inside the $0.25–1.00/hr band once the remaining tuning lands.

**Shipped ahead of its quality gate, deliberately and on the record.** Pass 3 declined to recommend this blind; Mark's stated tolerance ("a small drop after 15 turns") is the basis for taking it anyway. The full reasoning, the risk, and what to watch are written into `render.yaml` beside the value, so whoever next reads the deploy config finds them without needing this log.

**Two things to measure before concluding the switch saved anything** — both already emitted by existing logging, no new instrumentation needed:
1. **Regeneration rate.** Every world in `HARD_CEILING_WORLDS` has a ceiling calibrated against a *Sonnet-measured* voice profile, and a regeneration costs MORE than the original turn. Desert already regenerated on 80% of turns on Sonnet. If Haiku's length adherence is worse, the extra regenerations eat the saving. `app/length_ceiling_logging.py` emits a parseable line per outcome — count it.
2. **Cache behaviour.** Haiku 4.5's minimum cacheable prefix is 4096 tokens vs Sonnet's 1024. The representative prefix is ~15.2k measured so both breakpoints should still cache, but confirm `cache_read` is non-zero in the `[llm_usage]` lines rather than assuming.

**Second correction to this analysis, found while making the switch.** `provider_repricing.py` had been pricing cache writes at the 1-hour rate (2.0×) because the deployed code sets `ttl="1h"`. That was wrong for the baseline log: the committed run notes (note 2) record a **330-second pause expiring the cache**, which only a 5-minute TTL does. `cost_floor_model.py` and `cost_baseline_runner.py` were right at 1.25×; this tool was not. Every figure re-derived. Movements of 1–5 points; **no conclusion changed, and the gap between Haiku and the migration targets widened** (Gemini 3 Pro is now −24%, GPT-5.6 Terra −22%, against Haiku's −47%). A cross-check that failed before now passes: the generation token mix matches `cost_floor_model.py`'s Step 2 almost exactly.

Also hardened the tool against the switch itself: it split generation from classifier calls **by model string**, which would have silently reported zero generation calls — quietly zeroing 70% of the bill — the moment both tiers ran Haiku. Now split by log label, with an assertion that fails loudly on any unrecognised label.

**Still genuinely open:** the deployed code sets `ttl="1h"` while `cost_floor_model.py`'s A2 move found the 1h TTL a *net loss* at the measured pause rate (break-even 1.6 re-writes per initial write; measured 1.5). Either pacing changed or it was adopted against that finding. Needs one fresh measurement, not arithmetic — fold into the same live run as the Haiku battery.

**NOT DONE — and I cannot do it.** Setting the **Anthropic Console spending limit** needs a logged-in session on Mark's account; I have no console or billing access, consistent with the standing constraint recorded in this log that account actions are Mark's. **This stays the single most important open item before 2026-09-01.** With Supabase off there is no per-visitor identity cap, and `message_cap.py`'s 60-turn cap bounds one conversation, not a month's spend. Steps: **console.anthropic.com → Settings → Limits → Spend limits**; monthly cap $100–150 per the 21 July model, plus a notification threshold below it. Moving to Haiku lowers the slope, not the ceiling — an unbounded key is the failure mode that doesn't announce itself, and it is now the only line of defence left.

**Next action:** (1) Mark sets the console spending limit — blocking, before 2026-09-01. (2) Run the Haiku battery against the ≤1-drop-per-15-turns threshold, and read the regeneration rate off the same run. (3) The disclosure question from the previous addendum — that an accepted defect rate needs to reach the participant-facing copy — is now live rather than hypothetical, because the switch has shipped.

**Addendum (2026-08-09, third) — participant-facing defect notice DECIDED AGAINST; 1h-TTL question closed as a non-issue; a pacing-basis discrepancy found that affects every $/hr figure this log carries.**

**Mark's ruling on disclosure, verbatim:** "we don't need a notice, we will use the best tool we can afford, if there is feedback that we are having problems we will look at it, but no reason to get them looking for things they wouldn't notice."

**Decided, and closed.** The previous addendum flagged that an accepted defect rate would need to reach the participant-facing copy for Trustworthy Transparency to hold. Mark has ruled otherwise, on stated reasoning: use the best tool affordable, treat real feedback as the signal, and don't prime participants to hunt for a degradation they wouldn't otherwise notice. **Recorded as a decision, not an oversight — downstream threads should not re-open it.** The heart of it, in his own framing: a notice that manufactures suspicion is its own kind of dishonesty about how good the thing actually is.

**Correction within the same session — detection is by INTERVIEW.** I first read "feedback" as the written form and flagged confirming it was watched. Mark: *"i am not keeping pilot feedback in written form, i am interviewing people."* No plumbing check needed; the recommendation is withdrawn.

Worth recording once, because it shapes what the Haiku risk is actually covered by: interviews detect what a participant **felt**, and they are the right instrument for register and voice. The Haiku failure class Pass 3 described is specifically what a participant **would not notice** — a dropped negative constraint, a manufactured resolution, a borrowed image several turns later. Those never appear in an interview. The gap is closed not by a notice or a form but by the **post-hoc detectors already written and running** (`check_manufactured_resolution`, `check_cross_world_vocabulary_drift`, `check_convergence`, `length_ceiling_logging`). **Interviews for register, detectors for adherence** — reading both alongside each other costs nothing and is the whole mitigation.

**A live-site issue found while checking this, separate from the quality question and worth a decision.** `cic-website/pilot-feedback.html` is linked from **every page footer**, from inside the app (`TheTable.tsx`), and from a sentence in `whats-next.html` that tells pastors and academics "the feedback form is how that reaches us." Its form posts to `action="mailto:info@churchinconversation.com"` — unreliable across modern browsers and **silent when it fails**. So the site currently promises a written channel that probably doesn't deliver and that, by Mark's own account, nobody is reading. Not urgent and not a quality risk, but it is the site making a commitment the project isn't keeping. Options: repoint it at whatever the interview intake is, replace the mailto with a real form endpoint, or retire the page and its footer links. **Mark's call — not changed unilaterally, since it is live public copy.**

**1h cache-TTL question — closed, there was never a contradiction.** The previous addendum left open why the deployed code sets `ttl="1h"` when `cost_floor_model.py`'s A2 move called it a net loss. Answer: commit `1d8e952` (2026-08-02) adopted 1h as Item 1 of `CiC_Cost_Reduction_Build_Scope_2026-08-02.md`, backed by a Funding Strategy feasibility study measuring a **reflective-pace (6 turns/hr)** conversation from $0.77/hr to $0.50/hr. A2 itself said the switch "flips positive as soon as real contemplative pacing pushes pauses past 1.6x". The two agree; they answered at different pacings. Nothing to reconcile, nothing to re-measure.

**But that surfaced a real basis problem, and it is bigger than the TTL.** `cost_floor_model.py` and `provider_repricing.py` price per hour at **30 turns/hr solo / 24 Table**. The cost-reduction scope and the funding model price at **6 turns/hr reflective**. Those denominators differ by 4-5x. **A `$/hr` figure from the technical analyses and a `$/hr` figure from the funding model are not the same unit**, and this log has quoted both. Directly material here: whether the $0.25-1.00/hr target band was set against fast or reflective pacing decides whether the app is in band today. At 30 turns/hr, Haiku puts solo at ~$0.83/hr (just inside); at 6 turns/hr the same workload is a fifth of that. Flagged, not resolved — resolving it is a funding-model decision, not an engineering one, and it belongs to this workstream.

**Also produced this session:** `Ministry/Technology/CiC_Voice_Rebuild_Handoff_Update_2026-08-09.md`, an update written for the Voice Rebuild thread. Its substance for this log: **every `native_measure` in the six voice_profile records, and every `HARD_CEILING_WORLDS` ceiling, was measured against Sonnet** — three of six ceilings (SYR/HAL/ALX) were set deliberately *at* the measured maximum, so they carry zero margin against a different model. If Haiku's length adherence differs, regeneration rates move, and a regeneration costs MORE than the original turn. That is the mechanism by which the -47% saving could fail to materialise, and it is measurable from logging that already exists.

**Next action:** unchanged priorities — (1) Mark sets the Anthropic Console spending limit, still blocking before 2026-09-01 and still the only item nobody but Mark can do; (2) run the Haiku battery, folding the voice re-baseline and the regeneration-rate read into the same live session; (3) decide what to do about `pilot-feedback.html` — a live page promising a written channel that isn't collected and probably doesn't deliver; (4) settle which pacing the target band assumes.


**Addendum (2026-08-09, fourth) — conversation tracking IS wanted; a direct code read found nothing durable is storing it, and the app promises participants otherwise.**

**Mark, correcting the previous addendum:** "actually i mis-spoke, we are tracking conversations, i am not having those piloting CiC give written feedback, but yes i want the actual conversations tracked (not necessarily tied to a name)."

**Verified in code, not assumed. The promise and the storage do not currently match.**
- `OnboardingScreen.tsx` tells **every participant, unconditionally**: *"Your conversation in this session is being saved and cataloged for learning purposes... reviewed by the project team only"*, and links `privacy.html` for what is stored, how long, and how to request deletion. This disclosure is shipped and live.
- The durable audit log (`events.py::_persist_supabase` → `session_events`) is correctly **un-gated** from `PILOT_LOGGING_ENABLED` — a prior fix (Wave 3, Engineering P1-4) that spotted exactly this class of problem — **but it still returns early when `supabase_configured()` is False.**
- `supabase_configured()` is `bool(supabase_url and supabase_service_key)`, and **`render.yaml` declared neither** — unlike `ANTHROPIC_API_KEY` and `CORS_ORIGINS`, which it declares `sync: false` precisely so the dashboard is known to be their source. This log's own 2026-07-21 entry records Supabase as deliberately off at that stage, which corroborates.
- The only other durability is JSONL at `transcripts/events/<session_id>.jsonl`, and the service declares **no disk or volume** (nor does the Dockerfile). That is ephemeral container storage — wiped on every restart and every redeploy.

**So: unless the Supabase values were added to the Render dashboard as undeclared variables, every pilot conversation has been kept only until the next redeploy — and the redeploy carrying today's Haiku switch would itself wipe whatever is currently on disk.** This is the same shape as Participant Readiness finding P0-2 (the app told testers their conversation was saved with no page saying what that meant); that one was a disclosure gap, this one is the storage behind the disclosure.

**Changed here (safe, behaviour-neutral until Mark acts):** `render.yaml` now declares `SUPABASE_URL` and `SUPABASE_SERVICE_KEY` as `sync: false`, and sets `PILOT_LOGGING_ENABLED=true`. Declaring the vars changes nothing on its own — unset still means `supabase_configured()` is False, exactly as today — it makes a silent requirement visible. `PILOT_LOGGING_ENABLED` turns on the human-readable `sessions`/`messages` transcript view that `transcript_logging.py` describes as "the human-readable transcript view Mark actually reviews"; it is separate from the `session_events` audit log, and no-ops without Supabase. That module's own stated precondition for enabling it — an onboarding disclosure already in place — is met.

**Anonymity holds, which is what Mark asked for.** Configuring Supabase does **not** force sign-in: `auth.py::get_current_user` returns the anonymous placeholder when Supabase is configured but no token is offered ("sign-in is an ask for this pilot, not a requirement" — Mark's 2026-07-25 call). `sessions.user_id` is nullable and populated only for a signed-in participant (`main.py:477`). Anonymous conversations are stored against a session UUID with no name attached. Session access is possession-based (`session_auth.py`), not identity-based, so this does not change who can read what.

**Two things this puts back on Mark, both account actions:**
1. **Create/point a Supabase project and set `SUPABASE_URL` + `SUPABASE_SERVICE_KEY`** in the Render dashboard, and apply `cic-poc/backend/supabase_schema.sql`. Until then the promise in the onboarding text is still not backed. **This is now more urgent than it was an hour ago**, because the Haiku switch is exactly the change whose effect on real conversations needs a record.
2. **Confirm `privacy.html` matches what will actually be stored** — retention period and the deletion path it promises. It was written against an intended behaviour; it should be checked against the real one before storage goes live.

**Also still open from the previous addendum:** `pilot-feedback.html` is a live page, linked from every footer and from inside the app, whose `mailto:` form is unreliable and which nobody reads. Unchanged by this correction — written feedback and conversation tracking are different things, and only the latter turns out to be wanted.

**Next action:** (1) Anthropic Console spending limit — still blocking before 2026-09-01; (2) Supabase configured so conversation tracking is real before more pilot conversations run on Haiku; (3) run the Haiku battery with the voice re-baseline and regeneration-rate read folded in; (4) decide `pilot-feedback.html`; (5) settle which pacing the $0.25-1.00/hr band assumes.

---

## 2026-08-30 — Donation coverage math: hope needs real pilot data, not just growth

**Bridge note.** Nothing in this log since 2026-08-09 — in the gap, the engine itself was rebuilt:
`cic-poc`/direct-Anthropic-API is retired, the app now runs on the new M8 engine over AWS
Bedrock (10-turn session cap, not 60), and a full Bedrock-vs-rate-card reconciliation just closed
clean (`engine/m8/reports/reconciliation-2026-08-28-worksheet.md`, 2026-08-28/30). This entry is
narrowly about the funding/coverage question that came up while working through that
reconciliation's cost figures with Mark — it doesn't re-litigate the engineering.

**Origin.** Mark, on hoping Stripe giving (already live on `support.html` — "Keeping the Door
Open" one-time, "Open the Door Wider" monthly) covers running costs as the pilot grows: "the
first month will be small as it is still in pilot... i am hoping that could cover costs as we
start growing."

**The honest math, checked before taking the hope at face value.** Current fully-loaded monthly
cost: $225 fixed (Claude subscription + Render hosting) + ~$0.35 Bedrock cost per
interview-equivalent conversation. Applying this workstream's own prior donation benchmark
(Wikimedia's published 2% ask-conversion rate, ~$5-10 average gift, from the 2026-07-21 Go-Live
Cost Model): expected donation revenue per conversation-starter ≈ 2% × $7.50 = **$0.15** — *less
than half* the $0.35 it costs to run that conversation. **At a 2% conversion rate, more volume
does not close the gap — it widens it in absolute dollars,** even though the *fixed*-cost share
per person keeps shrinking with scale. Donations can plausibly cover the $225 fixed floor at
enough volume; they don't outrun the variable Bedrock cost at this conversion rate.

**The one real reason this could be too pessimistic, flagged not assumed:** 2% is a
stranger-traffic benchmark (Wikimedia's anonymous global readership). CiC's pilot is personally
invited people who already know Mark and are being interviewed directly (per the 2026-08-09
entries above) — a materially warmer audience that could convert well above 2%. Nobody has a
real number for that yet. It is the single biggest lever in the whole projection, bigger than
visitor count.

**Recommendation given to Mark:** treat donations as covering the fixed cost floor, not the
marginal per-conversation cost, until real pilot data says otherwise — a smaller, more honest
claim than "covers costs as we grow." The prior Go-Live model's own sequencing still stands:
one-time/recurring gifts are the fastest signal test, not necessarily the long-run answer;
institutional licenses ($1,200-5,000/yr per church/seminary) remain "the structurally strongest
source" once there's a track record, per the 2026-07-21 model.

**NOT YET DONE — waiting on real data, on Mark's own instruction ("log it once real pilot data
comes in").** This entry records the framework and the 2%-benchmark projection only. **Next
action:** once real Stripe conversions start coming in from actual pilot participants, update
this entry with the real conversion rate and average gift, replacing the Wikimedia benchmark —
that real number, not projected growth, is what actually answers whether the hope is founded.

**Also surfaced, related to this log's still-open pacing question (2026-08-09 entry above):** the
current M8 engine declared its own turns-per-hour convention (`engine/m8/cost.py`,
`TURNS_PER_HOUR_CONVENTION = 12`) independently of this workstream's unresolved 30/hr-vs-6/hr
question — a third value, not a resolution of the other two. Still open, still this workstream's
call to settle, now with one more value in play.

---

## 2026-09-03 — AWS credit application: real runway, not a fix to the math

**Origin.** Mark, in the same conversation as the Phase 1 Launch readiness list (see
`Ministry/Technology/CiC_FrontEnd_Decision_Log.md`'s 2026-09-03 entry, item 4): "i am applying
for a 1000 dollar credit from amazon and have 80 left on the first signup."

**What this actually changes, stated plainly so it isn't overclaimed.** The 2026-08-30 entry's
finding stands: at a 2% donation-conversion benchmark, gifts cover the $225 fixed floor, not the
~$0.35/conversation Bedrock marginal cost — more volume widens the dollar gap, not closes it. An
AWS credit doesn't change that unit economics; it pays the Bedrock side of the bill directly, so
it defers when the gap has to come out of pocket rather than closing it. Rough scale, working off
the $0.35/interview-equivalent figure: $80 remaining ≈ 228 more conversations before that credit
runs dry; a $1000 award (not yet confirmed) ≈ 2,857 more. Meaningful breathing room, not a
solved problem. (Assumes Render hosting, the other half of the $225 fixed cost, is billed
separately from AWS/Bedrock, per how the two are named distinctly in the 2026-08-30 entry — not
independently re-verified here.)

**Recommendation, tied to this log's own still-open ask.** The 2026-08-30 entry is explicitly
waiting on real pilot conversion data before its 2%-benchmark projection can be replaced with a
real number. Use whatever runway this credit buys as the deliberate window to gather that data —
track actual Stripe conversions against actual conversation-starters through it — rather than
treating the credit itself as the answer to whether donations can sustain growth. If the
credit's headroom becomes the reason to widen the pilot's invited circle sooner, that's a
legitimate use of it, but the audience-gating call in the front-end log's item 1 should still
wait on real conversion data and a real consent disclosure (item 2 there), not just on having
enough AWS credit to absorb the Bedrock bill while those are unresolved.

**Next action:** confirm the $1000 application's outcome and timeline; if there's a real gap risk
between the $80 remaining running out and the $1000 landing, that's a pilot-continuity question
worth a plan, not just a hope.

---

## 2026-09-21 — Tech-review stress test run; cut line set; entity supplement explored; Ministry tree triaged

**Context.** Mark opened a dedicated reviewer thread ("CiC — Tech Review &amp; Funding Readiness Prep") to stress-test the system as a technical acquirer would, with no counterparty across the table. First pass ran against the whole repo including early-days documents; Mark redirected: review the system as it is, not as it was imagined. **Cut line (Mark's decision):** what is live online now, the Conversation &amp; Transparency Engine upgrade being installed, and the ongoing world builds.

**Verdict recorded:** the system withstands a technical review and does not pass one clean. Credited: code-anchored crisis redirect with a caught-and-fixed regression; record-layer fidelity (216/216 quote records verified-direct across the six audited worlds, with documented passes against `cic/texts/`); commit-reveal sealed-probe admission; fail-closed rights pipeline; a Bedrock reconciliation that closed. Scored against: no world has had human Article 31 review (disclosed honestly on the site); the runtime grounding check verifies word provenance, not truth (measured ~98% fooled by vocabulary-faithful fabrications, `engine/m4/reports/grounding-fooling-2026-09-21.json`); sandbox and live diverged in both directions; production on a dev identity; single decision-maker. A first-pass finding that fabrication was a live defect was **corrected**: the July census recorded catch-and-fix history, not live defects.

**Partners and funding ministries explored** (landscape artifact in the thread): Logos as strongest commercial fit in both directions; a seminary as the moat (reviewer, grant eligibility, first license in one relationship); YouVersion as cheapest reach; BibleProject adjacency, not a deal; The Chosen ecosystem long-horizon via Come and See; funding ministries (Lilly, FLI, NEH, Wabash, Luce, Templeton, Praxis) are a nonprofit's table with Praxis the one door open to the PBC.

**Entity, as Mark reframed it:** not a conversion, not a full hybrid — **a nonprofit supplement beside the company to fund reach and accessibility**, with the product, engine, and sale option untouched. Three forms on the table (sponsored fund, partner ministry, own 501(c)(3)); reviewer thread leans sponsored fund first. Governing constraint named: private benefit — point most money at third parties (reviewers, translations, programs), buy access from the company at cost. **Open question left with Mark:** what the supplement pays for, compute vs. people and programs. Nothing decided on structure.

**Tech-readiness program dispatched** (Mark: "they stand, dispatch wave 1"): P1 Security (OWASP ASVS L1, LLM Top 10), P2 Operations (SRE, Well-Architected Reliability), P3 Fidelity as a machine gate (NIST AI 600-1, Article 31). Six transparency-engine rulings taken by Mark one at a time (R16, R17, R9, R8, R10, R18) and handed to the existing transparency thread. Reports go to `Ministry/Operations/Audits/Tech-Readiness-2026-09/`.

**Ministry tree triaged** (this PR): early-days strategy drafts to `Archive/Ministry-Early-Days-2026-07/`; five documents kept with supersession banners; FAQ and Letter to Friends kept as source material with their standing status written on them; the Organizational Covenant's Article 2 commitment ("Money Buys Access, Never Voice" — core access stays free, money only widens the Table, never gates or influences) extracted and quoted with full attribution into `CiC_Business_Roadmap_V0_1.md` under "What stays true across every phase"; the Covenant itself moved to `Archive/Ministry-Early-Days-2026-07/Organization/`.

**Next action:** Mark's answer on what the supplement pays for; reviewer thread reads the three wave-1 reports against their standards.

---

## 2026-09-22 — Realigned "source trust" to the bar a reasonable industry reviewer or buyer actually checks; Article 31 adjusted; the pilot-feedback channel named as the one real, fixable gap

**Context.** This viability/value thread had been treating Article 31 (a required external human scholarly reviewer) as an open governance gap, per the org-funding-strategy skill's own description and the reviewer thread's "The System As It Is" artifact. Mark redirected the whole line of inquiry, in his own words: *"this thread is not about what i said or what we thought, it is about what it is and what the consumer or buyer wants to create value... you should be focused on what the industry, purchasers, tech reviewers would expect reasonable, not perfection, but reasonable trustworthiness and accessibility."*

**What "reasonable, not perfect" actually means here, reasoned from how comparable AI products are actually diligenced.** No product in this category ships with pre-publication external scholarly peer review — that is an academic-publishing bar nobody in the space meets. What a reasonable reviewer or buyer checks instead, in the order it actually weighs: (1) a documented, auditable internal QA process — already strong here, arguably over-built (the quote-verbatim gate, the five-level confidence vocabulary, contested-claim tracking, review rounds run to excess); (2) no overclaiming in user-facing language — already in motion (R18, Stage 6 of the transparency engine); (3) a real, working correction channel for a user or institution to flag and fix an error — the one genuine current gap, found below; (4) a credible plan to deepen validation later, once revenue funds it — real, but not something a reasonable reviewer holds the product to today.

**Article 31, adjusted, not simply deleted.** An external scholar relationship remains a real future strengthening move, worth keeping ready to describe once institutional revenue can fund it. What changes is its status: retired as a near-term governance requirement, because it was written under earlier, more idealistic thinking and matches neither actual industry practice nor what the project can spend right now. Mark has told multiple threads this directly; the written source (presumably Article 31's own text in the Constitution) hasn't yet been updated to match, which is why it kept resurfacing here — a verbal instruction to a thread doesn't persist past that thread's own session, only editing the source does.

**The one real, fixable gap, found and handed off.** `cic-website/pilot-feedback.html` — linked from every page footer, from inside the app, and from a sentence telling pastors and academics it's how feedback reaches the project — posts to a `mailto:` action that is unreliable across modern browsers and fails silently. First flagged 2026-08-09, still open. This is the actual trust mechanism the industry relies on (a real, working way to flag and fix an error) that CiC is currently missing — not external peer review. Per this thread's own scope (no code changes; anything needing a build goes to the reviewer/build thread as a brief), the fix has been packaged and handed off rather than made here.

**Next action.** Reviewer/build thread picks up the pilot-feedback fix. Whoever holds edit access to Article 31's own source text retires or rewrites it so it stops being re-derived as a live requirement by threads that read governance documents cold.

---

## 2026-09-22 — Full-session convergence: four criteria named, split into execution vs. research, Tier 2 bundled into one Fable charter

**Context.** Following the trust/valuation redirect earlier the same day, the thread worked through what a reasonable industry reviewer or buyer would actually check, then extended into experience: what genuinely engages a participant, as distinct from what merely reduces legal/safety risk. Four real criteria emerged, each grounded in evidence found this session, not asserted: (1) generation fidelity — closing the gap between the adversarial grounding-check ceiling and the real fabrication rate; (2) witness integrity — a Representative should testify honestly, never quietly drift toward telling a participant what they want to hear under sustained friendly pressure (Article 24's persuasion ban, made testable); (3) register consistency — the already-ruled Register Bar (2026-08-29) is well specified, but five of eleven worlds measurably exceed its own proposed ceilings and the fix (R7) isn't confirmed executed; (4) the cross-cultural bridge — the modern-term-translation mechanism that's supposed to make every world equally navigable to a participant regardless of background is built but populated with one record of roughly 168 candidate fields, meaning translation quality currently depends on which builder happened to do careful manual work, not a standard.

**Split, and why.** Not everything here is equally unsettled. (1) and the execution half of (3) are already decided — rulings exist, a fix method is chosen, what's left is confirming or running it. No Fable justified; handed directly to the build thread as the "Fully True" brief (2026-09-22, same day, earlier entry). (2), the design half of (4), and a fifth thread running through the whole session — truth itself, not invented content, has to carry the actual engagement, since attachment-engineering is constitutionally off the table (Article 34) and backstory invention is already forbidden — are genuinely open design questions with no existing mechanism to wire up. Mark confirmed (2026-09-22): bundle these three into one Fable research-and-design charter rather than splitting truth-as-engagement out separately, since they share one root question — what makes an encounter feel real without inventing anything.

**The charter, as converged** (full text in the "The Encounter Standard" artifact, https://claude.ai/artifact/XntNXR9ksKeqwckkdgxDxj): research and design (a) a validation method distinguishing honest witness from quiet persuasion under sustained pressure, fleet-wide; (b) a reusable, world-agnostic method for the modern-term bridge, replacing one-off manual translation; (c) what makes true, unflattened, specific material land as gripping in a live conversation, including the Table's format and whether "honest fiction, not resurrection" becomes explicit participant-facing language. Same pipeline the transparency engine workstream itself used: Fable research and design → Opus adversarial review → Sonnet build. Same two carried-over constraints: no added per-turn cost on an ordinary turn, and the Facilitator's safety mechanism stays closed, not reopened.

**Next action.** Mark opens the Fable thread with this charter. This thread's own role in today's work is done — everything actionable has been handed off as a brief (generation fidelity + register consistency, sent earlier) or a charter (witness integrity + cross-cultural bridge + truth-as-engagement, this entry).

**Addendum (2026-09-22) — two more criteria folded in; voice/transparency decided, not researched; the whole charter held pending the transparency engine's own completion.**

**Two more Tier 2 items added, same evening.** (5) Pacing and turn-taking, mode-specific — solo allowed to go deeper, the Table moving quicker per exchange while the worlds genuinely respond to each other, benchmarked against what a healthy (not typical) four-person conversation actually sounds like; the existing Table battery tests routing and memory, not whether it feels like real people talking. (6) Named as a carried non-regression constraint, not a new open question: whatever this research changes has to be measured against what's already succeeding, the same discipline the Register Bar's own approved sample already enforces for register, extended to pacing, Table dynamics, and voice.

**Voice/transparency ruled directly by Mark, removed from the open-question list.** Text and voice run together, not as a substitute for each other — voice never replaces text, and anyone wanting the deeper, sourced experience follows the transcript, where the rigor lives. Voice's whole job is to sound as natural as the tier allows (best-effort free/browser speech now, ElevenLabs on the paid tier) — no transparency apparatus vocalized at all, no attempt to speak a citation or a confidence mark aloud. This belongs to the separate voice-exploration thread to build against, not to the Fable charter to research.

**Charter held, not dispatched.** Mark's call: wait until the Conversation &amp; Transparency Engine finishes (Stage 6, `guard_proximity`, sandbox-to-live) before opening the Fable thread, since real interdependencies exist between what that workstream lands and what this charter would research — Fable should start from a settled foundation, not a moving one. The charter itself (six items total: four open research questions, one carried non-regression constraint, one decided voice/transparency ruling) is finished in the "Encounter Standard" artifact and ready to fire the moment that gate clears; nothing further to draft, only a trigger to wait for.

**Next action.** No action until the transparency engine workstream reports its own completion. At that point: open the Fable thread with the held charter as-is, and separately hand the voice/transparency ruling to the voice-exploration thread.
