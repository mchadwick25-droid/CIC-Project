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
