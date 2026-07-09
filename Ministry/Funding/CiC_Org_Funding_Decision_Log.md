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
