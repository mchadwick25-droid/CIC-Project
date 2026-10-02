# Access and Monetization: Decision Log

Append-only and numbered. Only decisions Mark has reached are recorded here.

## 1. Safety rule for all access limits (2026-10-02)

**Decision (Mark):** adopt the rule that no balance, cap, paywall or purchase prompt sits between a participant's message and the safety gate, and log the existing gap. A participant can always reach the Facilitator, including at zero balance. Purchase prompts stay hidden after a safety event.

**Basis:** Opus round 1 review, blocking finding 1. See `Open_Gaps_Tracking.md`, entry 1.

**Scope:** applies to the ledger design and to the two existing paths named in the gap entry.

## 2. The Facilitator speaks the close and the offer (2026-10-02)

**Decision (Mark):** the Facilitator speaks the close of a conversation and any mention of buying more. The Representative never speaks the ask.

**Basis:** Opus round 1 review, blocking finding 2. Today's close is a Facilitator template, and the research's Closing Page and Threshold Sheet directions carry the offer in the Facilitator's register.

**Open:** the exact wording of the close and the offer. It is drafted later and held to the participant-facing readability and no-AI-tells standard in `CLAUDE.md`.

## 3. No auto-reload at pilot (2026-10-02)

**Decision (Mark):** no automatic top-up at pilot. Every purchase is a deliberate one-time act, so no recurring billing exists in any form.

**Basis:** Opus round 1 review, substantial finding on constraints. Auto-reload is recurring charging in practice and conflicts with the one-time constraint.

**Open:** may be reconsidered as an opt-in once pilot data shows demand. That would be a new decision, not a quiet edit.

## 4. Church and class offer is a one-time shared pool (2026-10-02)

**Decision (Mark):** the church and class offer, when built, is a one-time shared pool of conversations that members draw from. No annual licence.

**Basis:** Opus round 1 review, substantial finding on constraints. A yearly licence is a subscription.

**Open:** whether it ships with the first individual packs or follows them, the pool's size and price, and how members join. A shared church or class network also affects the anonymous free allowance, because the current per-IP seeding caps newcomers after about five first visits from one network a day.

## 5. Donations stay separate from paid access at pilot (2026-10-02)

**Decision (Mark):** paid access uses its own checkout. Donations stay on the existing website donation links. No donation round-up inside the purchase flow.

**Basis:** Opus round 1 review, substantial finding. Mixing a sale with a charitable ask raises Stripe restricted-category and Colorado solicitation questions, and Faithways is a public benefit corporation.

**Open:** a Sponsored Seat or combined flow is a later phase and needs counsel review first.

## 6. Change order: free allowance tracked by a minimal signed cookie (2026-10-02)

**Changes:** the "No per-visitor, device, or IP tracking" clause of the pilot "door" decision, recorded in `Build/Ministry/Features/Funding-Strategy/Decision-Log.md` (the entry that sets fairness by a shared, type-tiered throttle, not by visitor).

**Decision (Mark):** the free allowance is tracked per visitor with the signed visitor cookie that `engine/api/anon_cap.py` already issues. No device fingerprinting. No IP stored beyond the existing rate limit. No purchase tied to a name by this mechanism.

**Why:** a free allowance that means something to each person, and a way to attach a purchase to a visitor, need an identifier. The cookie already exists, so the real change is to the stated principle, not to the system.

**Accepted cost:** some visitors will clear cookies and get a fresh allowance. The research puts this at about 10%. It is accepted, not defended against with fingerprinting.

**Open:**
- The funding-strategy thread owns the original decision and the gift-funded door. It needs to be told this change order exists. Nothing in that log is edited here.
- Whether the shared throttle still applies on top of per-visitor allowances is not decided.
- The shared church or class network problem in the per-IP seeding is not solved by this decision (see entry 4).

## 7. Purchases by adults only, a parent may buy for a youth (2026-10-02)

**Decision (Mark):** the buyer must be an adult. A parent may purchase access for a youth to use.

**Basis:** Opus round 1 review, substantial finding that minors were not addressed.

**Open, and not settled by this decision:**
- A parent buying for a youth means a minor may use paid conversations. Whether the free experience and the Representatives are appropriate for minors, and what the safety design is for them, is not decided.
- Under-13 use raises COPPA duties. Counsel must review the checkout terms, the age wording and the child-privacy position before launch.
- How a purchase is handed to a youth (for example a gift code) is a design question for later.
