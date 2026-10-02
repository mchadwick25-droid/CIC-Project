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

## 8. Payment identity is never linked to conversation text (2026-10-02)

**Decision (Mark):** a payment is never linked to what someone said in a conversation. The access ledger holds the visitor id, Stripe references and counts. Conversation text lives in a separate store with no payment or email data. No screen, report or support tool joins the two.

**Basis:** Opus round 1 review, substantial finding on privacy. Conversations about faith are sensitive, and a joinable store conflicts with the current `privacy.html`.

**Consequences:** support cannot look up a transcript from a receipt. A lost-cookie recovery restores access and balance, not past transcripts. Wall and closing copy must not promise saved history that the system does not keep.

**Open:** the `privacy.html` wording that states this promise. That file is on a live surface (`cic-website/`) and is not edited here.

## 9. Counsel and accountant review before any live checkout (2026-10-02)

**Decision (Mark):** counsel and an accountant review the module before any live checkout. All building and testing runs in Stripe test mode until then.

**Scope of the review:** Colorado and home-rule sales tax on digital goods; whether public benefit corporation status changes Stripe fees or donation handling; COPPA and the adult-buyer wording (entry 7); refund and checkout terms; the privacy promise (entry 8).

**Open:** the question list for counsel, drafted before the review.

## 10. The Church Family Tree stays free and is the front door to conversations (2026-10-02)

**Decision (Mark):** the Church Family Tree stays fully free with no cap. Its role is to be the free front door that feeds conversations, with a quiet support lane kept apart from paid access (entry 5). The "always free" constraint is unchanged.

**How it works today (confirmed in `cic-website/`, 2026-10-02):**
- Each tree page for a tradition that is open for conversation links to `talk.html` with the tradition and mode preset ("Have a Conversation About This Movement"). That is the bridge.
- The homepage "Keep the Door Open" section and `support.html` carry two Stripe Payment Links, one one-time and one monthly, both feeding the Accessibility fund. That is the support lane.
- The tradition pages carry the line "Because of cost, we're asking each participant to keep to about five conversations for now. We can't enforce this yet, only ask."

**Basis:** the tree has no per-visit API cost, and Mark expects people to spend most of their time there. This decision keeps what exists and adds paid access behind the bridge.

**Open:**
- How the free allowance and paid access appear at the point where the bridge leads into a conversation.
- How time spent in the tree is measured, within the visitor-tracking change order (entry 6). None is measured today.
- The monthly donation link is recurring giving, which sits beside entry 3's no-recurring-billing rule for access. Entry 5 keeps donations separate, so this stays as is unless Mark rules otherwise.
- The tree's development and upkeep cost is not covered directly by this decision. The conversations it feeds carry it, which the funding thread should confirm.

## 11. Candidate paid depth is 15 turns, to be measured (2026-10-02)

**Decision (Mark):** a purchase buys more conversations that can go deeper than a free one. The candidate paid depth is 15 turns. Free conversations keep the 10-turn cap.

**Status:** a candidate, not a final cap. The cap and the pack price are set together once a measured run at 15 turns exists. See `Open_Gaps_Tracking.md`, entry 2.

## 12. No cut-off replies; keep them short by pressure on the generator, not by a cap (2026-10-02)

**Decision (Mark):** a reply is never cut off at an output limit. The generator is pressured to keep replies shorter through how it is prompted, with no hard cap that truncates a reply.

**Basis:** `Open_Gaps_Tracking.md`, entries 3 and 4. In the 15-turn run, 7 of 15 replies ended mid-sentence at the 1,024-token limit, and most replies ran 550 to 830 words against the readability target.

**Consequences for this module:** a cut-off reply no longer arises, so the protection rule that a failed or cut-off reply never costs a unit applies to errors only. Cost per turn can rise if replies run longer than the old limit allowed, so the 15-turn candidate (entry 11) must be re-measured once the change is made.

**Open, and not decided here:**
- The API still needs a numeric `max_tokens`. "No cap" is read as a high safety ceiling that replies should never reach, not a truncation point. The value is not chosen.
- How the generator is pressured toward shorter replies (prompt wording, the per-turn directive, or both). That change belongs to the voice and engine work and goes through its review. No engine file or prompt is edited by this module.
- A measured run after the change, to confirm replies end cleanly and to price the paid depth.

## 13. Free allowance is 3 conversations of 3 rounds; a paid conversation runs up to 7 rounds (2026-10-02)

**Decision (Mark):** a free visitor gets 3 conversations of 3 rounds each. Contributions can open the door further, with more free access. A paid conversation runs up to 7 rounds. Pricing is to find the balance between a good deal for the buyer, covering expenses, and contributing to operating costs.

**Supersedes:** entry 11's candidate paid depth of 15 turns. The free depth moves from today's 10-turn session cap to 3 rounds.

**Read as:** a round is one participant message and the Representative's reply. That reading is an assumption to confirm.

**Open:**
- The pack sizes and prices, set once the funding thread has the research and measured costs.
- The engine's `SESSION_TURN_CAP` is 10 today. Moving it to 3 for free and 7 for paid is an engine change this module does not make.
- Whether 3 rounds is enough for a participant to hear a world's voice in full. The research found the free unit must give the whole experience before any ask.
- The shared-network limit on the anonymous free allowance (see entry 4).

## 14. A round is a turn: free conversations capped at 3 turns, paid at 7 (2026-10-02)

**Clarification (Mark):** the conversation is capped at 3 turns in the free allowance and 7 turns in a paid conversation. This confirms the reading of "round" as one participant message and the Representative's reply, left open in entry 13.

**Measured cost under the caps** (15-turn run, rate card, warm cache): about $0.08 for a 3-turn conversation and $0.23 for a 7-turn one, about $0.13 and $0.28 after a cache lapse. Replies in that run were long; entry 12 aims for shorter ones.

## 15. Candidate entry pack is $10 for 7 conversations; the ladder is a model, not final (2026-10-02)

**Decision (Mark):** the entry pack is about $1.43 per paid 7-turn conversation, $10 for 7 conversations.

**Status:** a candidate price. Final pricing goes to the funding thread with the research and measured costs before it is set. The cost ceiling from that thread is still missing.

**Model ladder, for reference:** $10 for 7, $20 for 16 (about $1.25 each), $40 for 36 (about $1.11 each). At $0.26 API cost per paid conversation, Stripe's 2.9% + $0.30 and a 3% refund allowance, contribution is about 73%, 72% and 70%. The free allowance is a separate bucket funded from contributions and is not in these margins.

**Open:** the pack sizes above $10 are placeholders. The billing multiplier (the real AWS bill ran 1.35 times the rate card on 2026-08-28) is not applied; at 1.35 contribution on the entry pack falls from 73% to about 67%.

## 16. Entry pack is $7 for 5 conversations; larger packs reshaped so each rung improves the rate (2026-10-02)

**Decision (Mark):** the entry pack is $7 for 5 paid conversations, about $1.40 each, chosen over $5 for 3 and $5 for 4. Mark asked for an entry at $5 to $7 at most.

**Supersedes:** entry 15's candidate entry of $10 for 7. At $1.43 each that pack was a worse rate than $7 for 5, so a buyer would have no reason to step up.

**Model ladder, a candidate and not final:** $7 for 5 ($1.40 each), $15 for 13 ($1.15 each), $30 for 30 ($1.00 each). At $0.26 API cost per paid conversation, Stripe's 2.9% + $0.30 and a 3% refund allowance, contribution is about $4.99 (71%), $10.44 (70%) and $20.13 (67%). The $15 and $30 sizes are placeholders chosen to improve the rate at each step.

**Costs of the choice:** Stripe's fee is 7.2% at $7, against 5.9% at $10. A $15 dispute fee is about two entry packs, so refunds are made easy rather than leaving buyers to dispute. The free allowance remains a separate bucket funded from contributions.

**Open:** final pricing goes to the funding thread with the research and measured costs. The cost ceiling is still missing.

## 17. The pilot offers the full ladder: $7, $15 and $30 (2026-10-02)

**Decision (Mark):** the pilot offers all three packs, $7 for 5, $15 for 13 and $30 for 30 conversations. The options considered were entry only and entry plus one larger pack.

**Basis:** a complete test of willingness to pay, and better margin on large buyers because Stripe's fixed fee weighs less on a larger charge.

**Exposure this accepts:** the $30 pack commits 30 non-expiring conversations at $1.00 each, priced from a cost measured once. If the real bill runs 1.35 times the rate card, that pack's contribution falls from 67% to about 58%. Counsel's review (entry 9) covers the larger refund and dispute exposure.

**Open:**
- A repricing trigger: the measured cost per paid conversation at which pack sizes are changed for new purchases. Sold conversations are honored at the sold rate. The threshold is not set.
- The gift and group packs, which are not part of the pilot ladder.
- Final prices, which go to the funding thread first.

## 18. The pilot is a priced demand test with real checkout (2026-10-02)

**Decision (Mark):** the pilot's purpose is a priced demand test with real checkout, not a revenue line. Revenue is a bonus, not the target.

**Basis:** Opus market buy-in review (verdict: Unlikely as a primary financial engine at pilot scale, Plausible as a demand signal). It estimates 1 to 2.5% of people who start a conversation will buy, about $30 to $380 gross over three months at 300 to 1,500 starters. Real checkout stays in test mode until counsel's review (entry 9).

**Review's proposed thresholds, not yet adopted:** over the first 500 starters or 90 days, continue at 2% or more of starters (or 8% or more of those who use up the free allowance), redesign the offer at 0.5 to 2%, and lead with church, class and donations below 0.5% or when under 30% finish turn 1.

**Open:** the thresholds above, a per-visitor log plan that never joins payment to conversation text, and the review's remaining questions: whether the echo, streaming and reply-length fixes must land before paid launch, when the church and class pool ships, whether a buyer may give an email for balance recovery only, whether to seek a named scholar before charging, and what replaces the "about five conversations" wording.
