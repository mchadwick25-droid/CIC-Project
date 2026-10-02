# Round 2 — Best-in-class benchmark: free-to-paid experiences CiC should be measured against

Prepared for: Church in Conversation (Faithways Studio, Inc.), funding/front-end threads
Date: 2026-10-02
Scope: web-sourced, read-only. Builds on Track 1 (unit of access), Track 2 (price points and margins) and Track 3 (ledger and Stripe). It does not repeat them: unit-of-access, pack-size, fee and ledger findings are referenced, not re-derived. No internal CiC numbers were used or consulted.

Constraint taken as given: one-time pay-as-you-go, no subscriptions. Many of the best-executed free-to-paid journeys in the field are subscription products. They are included because the *journey* (first run, warning, wall, checkout, return, support) transfers even when the billing model does not; where a pattern depends on recurring billing, that is said.

Research note on sources. The sandbox egress proxy blocked direct fetches of nearly every primary page this round (stripe.com, baymard.com, meta.wikimedia.org, store.steampowered.com, hallow.com, kagi.com, signal.org, xsolla.com, w3.org, current.org, pro.gofundme.com, subclub.com, research.contrary.com, medium.com, archive.org and most trade press). Where a point rests on a search-engine summary of the primary page rather than the page itself it is marked **(via search summary)**. Two pages were fetched directly: Wikipedia's 2025 banner page and the Internet Archive's giving-circle post. Treat every number marked "via search summary" as indicative until re-verified from an unblocked network.

Evidence-quality key: **[H]** public filings, vendor price/help pages, peer-reviewed or large-N studies; **[M]** reputable journalism, analyst reports, vendor-published case studies; **[L]** blog teardowns, aggregator statistics, single anecdotes.

---

## 0. Executive summary

1. **The best free-to-paid experiences share one shape:** a complete, unmistakable "aha" before any ask; a limit that is explained in advance in plain words; a wall that arrives *between* units of value, never inside one; a checkout that a returning person can finish in one tap and a new person in under a minute with a wallet; a return that shows what you own and thanks you once; and a refund path so lenient that the policy itself becomes a trust signal. Nobody in the set does all seven perfectly; the composite is the bar.
2. **Honesty is now a measured conversion variable, not just an ethic.** Wikipedia's own 2024–25 tests found "human-written" messaging beat threat messaging and that donations fall off after four or five banner impressions; the Guardian's no-paywall model reached 1.4M recurring supporters and £126M digital reader revenue; Kagi's "no use, no pay" refund-as-credit is part of why it reached ~62k paying members with zero ads. The faith sector shows the inverse: Hallow is commercially the strongest faith app in history and still carries a Trustpilot/BBB record dominated by trial-billing complaints, and Pray.com reviewers invoke "making the Father's house a marketplace." The lesson for a one-time model: CiC's billing model is structurally cleaner than any of these (no trial, no auto-renew), so the remaining risk is entirely in the *experience*.
3. **One-tap wallets are the single largest measurable lever in checkout.** Stripe's 50+-method testing and 2026 data put Apple Pay at roughly +22% conversion where surfaced, ~2x when shown early rather than late; Shop Pay converts 1.72x standard checkout (1.91x on mobile); Link gives +7% on logged-in and ~+14% on returning users; wallet checkout runs ~42 s vs ~85 s for manual card entry. Church giving data says 59% of *first-time* givers use Apple Pay. CiC's checkout must lead with Apple Pay / Google Pay / Link, not offer them as a footnote. [M–H]
4. **Lenient refunds raise purchases more than they raise refunds.** The Janakiraman, Syrdal & Freling meta-analysis (22 studies) and Steam's own experience (Rust: refunds 6% of 5.5M sales, net sales up) both say the same thing. For a product priced in $10–25 packs where a single dispute costs $15 (Track 2), a no-questions refund on unused conversations is both the fairer and the cheaper policy. [H]
5. **The gap between "adequate" and "top-flight" for CiC is not the Stripe integration (Track 3 covers that).** It is: an aha that is a whole conversation; a limit indicator that never reads as a meter; a wall in the Facilitator's voice with the guarantees stated on it; one-tap pay with guest checkout and a recoverable balance; a return screen that restores the conversation and shows the balance without an upsell; a refund that takes one tap; checkout copy at B2 reading level with localized currency; a modal that passes WCAG 2.2 AA keyboard and screen-reader tests; and a support path reachable by a human. Section 9 gives the gap table and Section 10 ranks the ten practices to copy.

---

## 1. How the set was chosen, and what was left out

**Selection rule.** A product made the set if (a) it is commercially successful by public evidence (filings, audited reports, published supporter counts, or consistent analyst estimates), (b) its free-to-paid *experience* — not only its pricing — is documented well enough to describe the whole journey, and (c) at least one stage of that journey is best-in-field and transferable to a slow, reflective, one-time-pay conversation product for adults, many of them non-native English readers.

**The fifteen (grouped by the categories asked for):**

| # | Product | Category | Why it is in |
|---|---|---|---|
| 1 | ChatGPT (OpenAI) | AI chat | The reference free tier: degrade-not-block, signed-out use, and (since Aug 2026) uncapped free text; the clearest example of a limit that never cuts a reply |
| 2 | Khan Academy / Khanmigo | AI tutor, nonprofit | $4/month flat AI tutor framed as a contribution; the only AI tutor whose donation flow has a published A/B result |
| 3 | Duolingo | Learning | Apple Design Award 2023; 12.7M paid subscribers, $298.5M quarterly revenue; the best-documented "aha before signup, signup before price" onboarding in consumer software |
| 4 | Headspace | Meditation | Apple Design Award 2023 (Social Impact); published gating and onboarding experiments with numbers; exact trial terms shown up front |
| 5 | Hallow | Faith | The commercial high-water mark for a faith app (first religious app to reach #1 on the App Store; ~$40M 2025 net revenue est.); a published "why we charge" page, give-one-get-one and scholarships — and a billing-complaint record that is the cautionary half of the lesson |
| 6 | Audible | Consumable credits | "One credit = one whole thing," credits roll over, a 365-day return window; the closest consumer analogue to "one unit = one conversation" |
| 7 | Steam | Storefront, wallet | The refund policy that became a trust asset; $5-minimum wallet with fixed rungs; automatic approval inside the window |
| 8 | MARVEL SNAP web shop (with Monument Valley and Supercell as references) | Mobile-game consumable store | The one widely praised game web shop: consistent with in-game UI, better daily value on the web, up to 90% revenue retained; the counter-case to the industry's dark-pattern norm |
| 9 | Humble Bundle | Pay-what-you-want with charity | $250M+ raised for charity; the slider that made PWYW legible — and the 2021 retreat that shows what happens when a trust mechanic is quietly removed |
| 10 | itch.io / Ko-fi / Gumroad | Support flows | Open revenue share (seller picks itch's cut, default 10%); Ko-fi's no-account, 0%-fee one-time tip; Gumroad's PWYW data (+8% sales, −65% price without a suggested amount) |
| 11 | The Guardian | Reader-supported media | No paywall, 1.4M recurring digital supporters, £126M digital reader revenue; the "Epic" ask that drives 35% of US acquisitions |
| 12 | Wikipedia / Wikimedia | Mission-driven donations | $189.5M donations FY24–25; a community that forced the fundraiser to drop false urgency, and then measured that honesty converted |
| 13 | Kagi | Paid search, transparency | ~62k paying members with no ads; "Fair Pricing" refunds an unused month as credit; a public live stats page |
| 14 | Signal | Donations inside a product | Donation flow in Settings with Apple/Google Pay; anonymous-credential badges so the server cannot link payment to identity; $29.4M 2024 revenue |
| 15 | NPR Network donation form | Public media | The one public-media checkout with a published before/after: form conversion doubled 1.7% → 3.4%; station conversion to 10%+ |

**Left out, and why:**

- *Calm* — same category and near-identical journey to Headspace; revenue is estimated to have fallen 24% in 2025 (Business of Apps, [L]), so Headspace is the better-evidenced exemplar.
- *Midjourney* — commercially extraordinary (~$500M 2025 revenue, no outside funding, 163 people; [M]) but there is no free tier since 2023, the refund rule is "fewer than 20 GPU minutes used," and purchased fast hours expire monthly. It appears in Section 4 as a counter-example on expiry and refunds, not as a benchmark.
- *ElevenLabs* — $600M ARR by mid-2026 ([M]) but growth is enterprise-driven, and free users *cannot* top up without subscribing. The "free users can't buy more" gap is exactly what CiC must not copy; cited in Section 4.
- *Brilliant* — two "keys" per day on the free tier is a fair meter, but nothing about the journey is documented as best-in-field.
- *MasterClass* — no free trial on the web; a 30-day refund stands in for it. Instructive only as a reminder that a strong refund can substitute for a trial.
- *Patreon / Substack* — excellent one-tap join flows, but the whole product is recurring billing; Ko-fi/Gumroad/itch cover the one-time half of the creator economy better.
- *Mozilla, Internet Archive* — mission-aligned but the public evidence on their donation experience is thin; the Internet Archive's Monthly Giving Circle (any-amount monthly, $250+ "Petabyte" tier, perks are webcasts and thank-yous, monthly pre-selected) is noted in Section 6 as a tone reference.
- *Character.AI, Replika, Poe, Pray.com* — included only as negative controls (Section 4): message caps as teasers, blurred-image upsells, silent allowance cuts, trial-to-annual billing complaints.
- *Claude.ai* — a token "conversation budget" rather than a message count, three capability walls, and a plain "wait until the window resets" message with past conversations readable ([L], blog guides). Sound, but ChatGPT is the better-documented reference.
- *Monument Valley, Supercell* — referenced inside entry 8 (premium up-front pricing; "monetisation is not the priority") rather than as separate entries.

---

## 2. The fifteen journeys

Each entry follows the same seven stages: (1) first run and the aha before any ask; (2) how the limit is communicated in advance; (3) the limit moment; (4) the purchase flow; (5) the return experience; (6) support and refunds; (7) trust signals. Then: commercial evidence, why it works, and what transfers to CiC.

### 2.1 ChatGPT (OpenAI) — AI chat

- **First run / aha.** Usable signed out (a handful of messages, then a sign-up wall). The aha is the first good answer; it arrives in under a minute with no onboarding questionnaire. [M, via search summary]
- **Limit in advance.** Historically: "Free tier users can use GPT-4o only a limited number of times within a five hour window. We'll notify you once you've reached the limit." Since 6 Aug 2026 plain-text chat on Free is uncapped; separate meters remain for files, images, voice and image generation; US Free/Go users see ads. [M, via search summary]
- **Limit moment.** The product *degrades* rather than blocks: the conversation continues on a smaller model, with a one-line notice and a reset time. No reply is ever cut mid-stream. Voice mode warns at three minutes remaining rather than running a visible timer.
- **Purchase flow.** Go ($8) and Plus ($20) subscriptions; web checkout via Stripe-style hosted page. Not transferable (subscription).
- **Return.** Conversations are listed and resumable; the limit notice disappears when the window resets.
- **Support / refunds.** Help-center driven; prepaid API credits refund only on confirmed service failure (Track 1).
- **Trust.** The decision to make free text unlimited and to downgrade rather than block is the strongest signal: the product never punishes the user for using it.
- **Commercial evidence.** Not needed to argue; the largest consumer AI product by every measure.
- **Why it works.** The free tier is a funnel for capability, not a toll on conversation. The user learns the limit's *shape* (a window, a reset time, a lesser model) before ever hitting it.
- **Transfers to CiC.** Never interrupt a Representative mid-reply; when a free allowance ends, the wall belongs before the *next* conversation. Say the reset time. Keep past conversations readable regardless of balance.

### 2.2 Khan Academy / Khanmigo — nonprofit AI tutor

- **First run / aha.** Khan Academy itself is free and ungated; Khanmigo offers a trial. The aha is a tutoring exchange that refuses to just give the answer. [M]
- **Limit in advance.** Khanmigo is a flat $4/month or $44/year with "no extra fees per question or usage limits"; teachers free. The price page frames it as a contribution: "essentially a monthly donation model." [M, via search summary]
- **Limit moment.** None inside the product; the ask is at the door.
- **Purchase flow.** For donations: Khan Academy A/B-tested a GoFundMe Pro "Studio" page against the standard page on 50/50 organic traffic; the Studio page "brought in more total revenue and saw increases in conversion rates and retention with monthly donors," by making the monthly default "crystal clear" rather than hidden. [M, vendor case study via search summary]
- **Return / support / trust.** 501(c)(3) with Tax ID shown on the donate page; the ask explains it is "totally reliant on donations."
- **Why it works.** Nonprofit framing turns price into contribution, and the one published test shows that *clarity about the default* (not a pre-checked trick) raised both conversion and retention.
- **Transfers to CiC.** The "why we charge" line belongs on the wall and the donate page; the default pack should be obvious, never pre-selected by stealth. Note Faithways is a Colorado PBC, not a 501(c)(3) (Track 3), so the nonprofit trust signal is *not* available and must be replaced by other transparency (see Section 7).

### 2.3 Duolingo — learning

- **First run / aha.** No sign-up before the first lesson; the first action arrives in about 90 seconds; sign-up is asked only after the lesson. No paywall on first view. [M, teardowns via search summary: screensdesign, tasu.ai, adplist]
- **Limit in advance.** The energy/hearts meter is visible and explained in the lesson UI; ads appear after lessons on the free tier. The paywall "leads with a 'Try now' CTA" and reveals price only after engagement — a soft wall. Super is promoted in several places (shop, hearts view, home, review tab, after an ad). [M, via search summary]
- **Limit moment.** Energy runs out mid-session (the 2025 Energy system drains even on correct answers; Track 1 documents the backlash). This is Duolingo's weakest stage and the one *not* to copy.
- **Purchase flow.** App-store trial → subscription; family plans; four options on the paywall. Not transferable (subscription).
- **Return.** Streak and progress are front and centre; the mascot thanks and nudges.
- **Support / refunds.** App-store refunds. Consumer-complaint platforms are dominated by billing issues even though app-store ratings are 4.7 with ~49M ratings across both stores. [L–M]
- **Trust.** Apple Design Award 2023 (Delight and Fun). Public company: Q2 2026 revenue $298.5M (+18% YoY), 58.7M DAU (+23%), 12.7M paid subscribers (+17%) ([H], 8-K 5 Aug 2026).
- **Why it works.** Value before identity, identity before price; the meter is legible; sunk-cost mechanics (streak) make the wall arrive at "maximum value felt rather than maximum friction."
- **Transfers to CiC.** The order: conversation first, then (optional) email, then price. What does not transfer: a drain-on-success meter, multi-surface upsell nagging, and streak pressure — all of which would read as manipulation in a reflective faith-adjacent product.

### 2.4 Headspace — meditation

- **First run / aha.** Onboarding opens with "What's on your mind?"; a multi-intent version (pick several reasons) lifted conversion ~10%. Then it moves "straight into trial terms with exact numbers upfront: 14 days free, then the monthly price." [M, via search summary: abtest.design, Purchasely]
- **Limit in advance.** The trial end date and price are stated before the trial starts. Behavioural-science nudges during the trial doubled course starts (31% → 63%), and trial activity predicts conversion. [M]
- **Limit moment.** Headspace moved from ~20% free content to a 100%-locked library for new users; this produced "a double-digit lift in paid subscriptions" with high engagement. [M, Sub Club via search summary]
- **Purchase flow.** App-store trial → subscription; a 30-day guest pass referral lifted sign-ups 7% and revenue 8%. [M]
- **Return.** Progress and "today" session; no re-upsell to subscribers.
- **Support / refunds.** App-store. Rated 4.8 on the App Store. [L]
- **Trust.** Apple Design Award 2023 (Social Impact). Revenue estimated at ~$140M (2025), ~2M subscribers. [L, Business of Apps]
- **Why it works.** Exact terms up front remove the fear that makes trials feel like traps; personalization before the ask makes the paid thing feel chosen.
- **Transfers to CiC.** "Exact numbers up front" — the pack price, the per-conversation price, the no-expiry rule — stated before the wall is ever reached. The 100%-lock finding does *not* transfer: CiC's Family Tree is free by design and the aha requires a whole free conversation.

### 2.5 Hallow — faith (the full lesson, both halves)

- **First run / aha.** A large permanently-free core: 1,000+ sessions including most daily content, Bible in a Year, Catechism in a Year, the examen. The aha is a guided prayer that is produced to the standard of a secular wellness app. [M, help center via search summary]
- **Limit in advance.** A published page, "Why is there a Hallow subscription?", argues the case: the Church produced the most beautiful buildings and art and "the Word of God deserves the highest quality design and technology"; many lapsed or young people "wouldn't even try an app if it wasn't built to their standard." Commitments stated: a large free-forever core, priority for people in poverty, free subscriptions for all clergy, a scholarship path for anyone who cannot pay, give-one-get-one. [M, via search summary — hallow.com blocked]
- **Limit moment.** Premium prompts on locked sessions; 7-day free trial, 50% off the first month; prices $12.99/month, $69.99/year, $149.99 lifetime. [M]
- **Purchase flow.** App-store and web; trial auto-renews.
- **Return.** Daily content front and centre; Lent/Advent challenges drive seasonal spikes ("the most predictable spike in the App Store," Appfigures).
- **Support / refunds.** Refunds reviewed case-by-case within 14 days, web purchases only, not guaranteed. BBB and Trustpilot complaints cluster on being charged a year after cancelling a trial, AI-only support with no reachable human, and advice not to contact the card issuer. [L–M, via search summary; Trustpilot/BBB are self-selected]
- **Trust.** First religious app to reach #1 on Apple's App Store (Feb 2024, after a Super Bowl ad); 25M+ downloads; $105M raised to date including a $50M Series C; ~$40M net revenue est. 2025. [M]
- **Why it works — and where it fails.** The "why we charge" page is the best explanatory copy in the faith sector, and the free core is genuinely large. The failure is entirely in the recurring-billing mechanics and support: a faith audience that reads "charged after I cancelled" as betrayal, not as a billing error.
- **Transfers to CiC.** Copy the explanation, the clergy/scholarship/give-one lanes, and the generosity of the free core. CiC's one-time model removes the trial-to-annual failure by construction — but only if there is also a human-reachable support path and a refund that does not require arguing.

### 2.6 Audible — consumable credits

- **First run / aha.** Trial with a free credit; the aha is a whole book, not a sample. [M]
- **Limit in advance.** "1 credit = 1 title, any price" is the whole pitch; the credit balance is shown in the account header. Credits roll over and expire 12 months after issue (now under litigation as a gift-certificate expiry, Track 1).
- **Limit moment.** When credits run out, a 3-for-$36 top-up is offered (members only); otherwise retail price.
- **Purchase flow.** Saved Amazon payment; one click.
- **Return.** Library and credit balance persist; new credits land monthly.
- **Support / refunds.** The best stage: a finished-but-disliked title can be returned within 365 days and the credit reappears immediately, self-service. Abuse limits are algorithmic (roughly three returns in a rolling 30 days or >20% of lifetime library triggers manual review, per user reports) and authors have objected to royalty clawbacks. Trustpilot is 1.3/5, dominated by expiring credits, charges after cancelling and unreachable support. [L–M]
- **Trust.** 10M+ subscribers, ~40–65% of US audiobook sales (estimates vary). [L–M]
- **Why it works.** The unit is the thing you came for; the balance is visible; a bad pick costs nothing. Why it also fails: expiry and cancellation-forfeiture convert the same mechanic into loss.
- **Transfers to CiC.** Everything about "one unit = one whole thing," immediate self-service return of an unsatisfying unit, and a visible balance. Nothing about expiry.

### 2.7 Steam — storefront and wallet

- **First run / aha.** Free-to-play titles and demos; "Steam Next Fest" demos are the aha before purchase.
- **Limit in advance.** The refund rule is stated on every purchase: 14 days from purchase and under 2 hours played, refund approved automatically; outside that, a human reviews and Valve says it will look at out-of-policy requests. [M, via search summary]
- **Limit moment.** n/a (storefront).
- **Purchase flow.** Wallet funds in fixed rungs $5 / $10 / $25 / $50 / $100 (the $5 floor exists because smaller charges lose money to fees — the same arithmetic as Track 2); saved payment methods; wallet balance in the header. [M]
- **Return.** Library, wallet balance, and "recently played" on re-entry; no upsell on login.
- **Support / refunds.** Refund request is a form with reasons; refund goes to wallet or original method at the buyer's choice; typically a few days. Valve frames the policy as "purchase-risk protection" and reserves the right to restrict abusers. Developer-side data: median indie refund rate ~9.5–10.8% (GameDiscoverCo 2024 survey, 150+ developers); Rust's developer reported refunds at 6% of 5.5M sales and said the policy "probably gained them more sales" because buyers will try something they can return. [M]
- **Trust.** The refund policy is the trust signal; it is cited by developers as *increasing* experimental purchases.
- **Why it works.** An automatic, rule-based refund turns the purchase from a gamble into a trial.
- **Transfers to CiC.** Publish a one-sentence refund rule and automate it (e.g., any pack with unused conversations refunds on request, no reason required; anything else reviewed by a human within a stated time). Show the balance in the header. Offer refund-to-balance as well as refund-to-card.

### 2.8 MARVEL SNAP web shop (references: Monument Valley, Supercell) — game consumable store done well

- **First run / aha.** The game itself is free; ~20% of players were already visiting the earlier web shop and buying. [M, Xsolla via search summary]
- **Limit in advance.** The relaunched shop (June 2025) gives 200 free credits daily on the web vs 25 in-game every 8 hours — the web is openly the better deal, stated as such. [M]
- **Limit moment.** n/a (store).
- **Purchase flow.** The shop "reflects the in-game UI, giving players an immediate sense of familiarity and security"; login via game account; Xsolla's web checkout with regional payment methods; developers keep up to 90% (vs 70% in-app). After Epic v. Apple, US developers may link directly from the app to the web shop. [M]
- **Return.** Daily free credits reward the return visit without a purchase.
- **Support / refunds.** Platform (Xsolla) support; app-store rules apply to in-app purchases.
- **Trust.** Reviewers describe SNAP's monetization as "pretty fair" with cosmetics as the main route. Contrast references: Monument Valley charged once up front with no IAP and won an Apple Design Award (only ~5% of Android installs were paid, a reminder that premium-upfront loses to piracy and free alternatives); Supercell's public stance is "don't make monetization your number one priority." [M–L]
- **Why it works.** Visual continuity between product and store; the store gives before it asks; the better deal is on the surface the business prefers, and the player is told so.
- **Transfers to CiC.** The purchase surface should look and sound like the Family Tree, not like a bolt-on checkout. If the web is the better deal than an app store (it is, for fees), say so plainly.

### 2.9 Humble Bundle — pay-what-you-want with charity

- **First run / aha.** The bundle page shows contents, the current average price, and what each price unlocks.
- **Limit in advance.** "Beat the average" unlocks are stated on the page; the slider (until 2021) let the buyer split the payment among developers, charity and Humble.
- **Purchase flow.** Enter an amount, adjust the split, pay; PayPal/cards/wallets.
- **Return.** Library of keys.
- **Support / refunds.** Keys are refundable until redeemed, per standard policy. [L]
- **Trust.** $250M+ raised for charity since 2010 (Feb 2024 milestone; 2023 alone $14.4M to 7,500+ charities). [M] The 2021 redesign removed the sliders and capped the charity share at 15% (default 5%, toggle "extra to charity"), reversed after backlash, then reinstated. [M, Kotaku/NME/GameDeveloper via search summary]
- **Why it works.** The slider made generosity visible and controllable; the public average anchored price (Track 2 has the bimodal data).
- **Transfers to CiC.** A visible, buyer-controlled share to a scholarship pool at checkout is the Gneezy "shared social responsibility" condition made concrete. The 2021 episode is the warning: a trust mechanic once given cannot be quietly narrowed.

### 2.10 itch.io / Ko-fi / Gumroad — support flows

- **itch.io.** Every purchase is pay-what-you-want above a minimum that can be $0; the *seller* sets itch's cut from 0% to 100% (default 10%). Buyers see this. The result is a storefront whose fairness is structural rather than asserted. [M, itch.io docs via search summary]
- **Ko-fi.** One-time tips need no account: email and card, 0% platform fee on one-off tips, a single button. The lowest-friction one-time support flow in the creator economy. [M]
- **Gumroad.** PWYW with a suggested price that pre-fills the field: +8% sales, but average price falls ~65% ($66 → $18) when no strong suggested price is shown. [L–M, platform data via aggregator]
- **Transfers to CiC.** The support lane (separate from the packs, per Track 1) should be Ko-fi-shaped: no account, one amount field pre-filled with a suggested figure, one tap with a wallet. Show where the money goes in one line.

### 2.11 The Guardian — reader-supported media without a paywall

- **First run / aha.** Every article is free; the reader has already received the value before any ask.
- **Limit in advance.** There is no limit; the "Epic" unit at the bottom of articles says so: "No billionaire owner. No shareholders. No paywall." and asks for support "from as little as $1." It accounts for ~35% of US acquisitions. The Guardian also tells readers how many articles they have read as a gentle reminder of value received. [M, via search summary]
- **Limit moment.** None. The Guardian explicitly chose pledge-drive messaging over a wall.
- **Purchase flow.** One-time or recurring contribution; amount presets with a free-entry field; Apple Pay/Google Pay/PayPal/card; a short form.
- **Return.** App subscribers get "no subscription messages" and ad-free reading; web contributors should see fewer asks, though reader complaints show the sync between contribution records and message suppression is imperfect — a real defect worth not repeating. [L–M]
- **Support / refunds.** Standard; no public refund friction reported.
- **Trust.** Record revenue £282M (2025/26), digital reader revenue +17% to £126M, 1.4M recurring digital supporters (+116k), 500k+ in the US; end-2024 US campaign raised $5.13M in immediate contributions, more than double the prior record. Guardian US became profitable by pivoting from ads to reader revenue. [H–M, statutory accounts via Press Gazette and others]
- **Why it works.** The ask is honest about the model, placed after the value, short, and repeated at a controlled cadence; the reader is never locked out.
- **Transfers to CiC.** The Family Tree is the Guardian's article: free, complete, and the place where a short, honest, mission-stated ask can sit. Suppress the ask once someone has paid — and make sure the suppression actually works across devices.

### 2.12 Wikipedia / Wikimedia Foundation — mission-driven donations

- **First run / aha.** The article is the aha; the banner follows.
- **Limit in advance.** None; the banner is the ask. Donations fall off sharply after four or five impressions, so frequency is capped. [M, 2025 banner page fetched directly]
- **Limit moment.** None.
- **Purchase flow.** Amount presets, Apple Pay/Google Pay/PayPal/cards; a single page; recurring offered but not forced.
- **Return.** Donors can hide banners; a thank-you page and email.
- **Support / refunds.** Donor services by email; refunds on request.
- **Trust.** $208.6M total revenue, $189.5M donations, $62.4M (30%) from banners, 18M+ donations in FY24–25; recurring giving +18% to ~21–23% of revenue; Charity Navigator top rating. [H–M] The 2022 English-Wikipedia RfC (45–3) rejected banners implying Wikipedia's existence was under threat; the 2024–25 tests then found that "written by people, not machines" messaging improved desktop results ~9%, that threat language ("stay free from paywalls") underperformed, and that very short banners produced ~95% fewer donations. [M–H, fetched directly]
- **Why it works.** Enormous reach plus a community-enforced honesty rule that turned out to convert at least as well as urgency.
- **Transfers to CiC.** Cap ask frequency; never imply the project will die without this purchase; longer, plainer explanations outperform punchy threats; the people behind the work are the message.

### 2.13 Kagi — paid search, transparency as product

- **First run / aha.** 100 free searches and 100 AI interactions on the Trial plan, no card; the aha is a results page with no ads and user-controllable ranking. [M]
- **Limit in advance.** The remaining-search count is visible in the account; the trial is openly "enough to evaluate, not a permanent free tier."
- **Limit moment.** A plain upgrade page: Starter $5 (300 searches), Professional $10 (unlimited), Ultimate $25. [M]
- **Purchase flow.** Stripe checkout; family plans.
- **Return.** Usage counts and the live public stats page (members, queries) are part of the product's voice.
- **Support / refunds.** "Fair Pricing": a month with zero searches is credited back automatically; cancel for a prorated refund by emailing support, "no questions asked." [M, help center and Android Police via search summary]
- **Trust.** ~62,000 paying members (Oct 2026 stats page, via search summary; 50k in June 2025); no ads, no tracking; public year-in-review posts. [M]
- **Why it works.** A product that charges money argues *for* paying and then proves it will not take money it did not earn.
- **Transfers to CiC.** The "we charge because you are the customer, not the product" argument, stated once and well; automatic credit-back for anything not delivered (Track 1's failed-reply rule is the same principle); a public page that shows how the project is doing.

### 2.14 Signal — donations inside a product

- **First run / aha.** The product is complete and free; the ask lives in Settings → Donate to Signal, never in the conversation surface. [M, via search summary]
- **Limit in advance / limit moment.** None.
- **Purchase flow.** Apple Pay and Google Pay first, then cards, PayPal, SEPA/iDEAL, bank debit; one-time or monthly; three sustainer tiers ($5/$10/$20) with badges, and a one-time badge.
- **Return.** A badge on the profile, optional; the donor chooses whether to display it.
- **Privacy.** An anonymous-credential scheme means the server can verify that a client is among the people who paid but not which payment — the donation cannot be linked to the account. [M]
- **Trust.** Signal Foundation 2024 revenue $29.4M. [M]
- **Why it works.** The ask never intrudes; paying is a private act that can be made visible only by choice.
- **Transfers to CiC.** Keep the ask out of the conversation surface; let a supporter be visible only if they choose; a purchase should not require more identity than the product does (Track 3's guest-first, claim-code recovery design is the same instinct).

### 2.15 NPR Network donation form — public media

- **What changed.** NPR.org's donate form added the option to give to the NPR Network (not only a local station); the form's conversion rate doubled from 1.7% to 3.4%; KUOW saw ~10% conversion among NPR digital users with no prior giving history (up from 1.6%), heading for 13%; 60% of Network donors were new to public media; the programs brought in $30M+ in FY2025. Mobile-friendly design and fewer technical barriers were credited. [M, Current.org via search summary]
- **Why it works.** Removing one choice the donor could not make ("which station?") and making the form mobile-first doubled completion.
- **Transfers to CiC.** Every question on the checkout that the participant cannot confidently answer halves the completion rate. Ask for nothing but the amount and the payment.

---

## 3. Measurable benchmarks (public)

All figures are from public sources and most are from vendors or aggregators; use as order-of-magnitude anchors, not targets.

| Metric | Benchmark | Source and quality |
|---|---|---|
| Free-to-paid conversion, consumer self-serve | 2–5% typical; 8–12% great; AI-native reported 6–8% good, 15–20% great (Track 1) | Aggregators [L] |
| Mobile game payer conversion | 1.5–3.5% of actives; top titles 6–8% (Track 2) | AppsFlyer/AppFollow [M] |
| Donation-page conversion, public media | 1.7% → 3.4% after form change; station-level 10–13% among engaged users | Current.org [M] |
| Paid subscribers, Duolingo | 12.7M of 58.7M DAU ≈ 21.6% paid among daily actives (Q2 2026) | SEC 8-K [H] |
| Cart abandonment, all e-commerce | 70.22% (Baymard 2025) | Baymard via secondary [M] |
| Checkout completion (started checkout → paid) | ~47% average; 65% median across 16 DTC Shopify stores (Jul 2025–Jun 2026); top performers >73% desktop | Aggregators [L–M] |
| Abandonment causes (Baymard survey, 1,026 US adults) | Extra costs 39–48%; forced account creation 18–26%; too long/complicated 17–22%; didn't trust site with card ~25% (older wave) | Baymard via secondary [M] |
| Mobile share of traffic / orders | ~70–76% of traffic; ~7 in 10 orders (Shopify) | Shopify, Contentsquare via secondary [M] |
| Conversion by device | Desktop 3.4–4.8% vs mobile 2.0–2.9% (desktop ≈1.7x mobile); mobile cart abandonment 80–86% vs 64–66% desktop | Contentsquare/Shopify via secondary [M] |
| Apple Pay impact | ~+22% conversion where dynamically surfaced (Stripe 50+-method tests); ~2x when shown early (Express Checkout Element) vs at the end | Stripe blog via search summary [M] |
| Shop Pay impact | 1.72x standard checkout; 1.91x on mobile; +9% all checkouts, +18% returning | Shopify (vendor) [M] |
| Link (Stripe) impact | +7% conversion for logged-in customers; ~+14% returning-user conversion; ~6 s to pay, 3–9x faster than non-Link | Stripe (vendor) [M] |
| Time to pay | Wallet ~42 s vs manual card ~85 s (Stripe 2026 data via secondary); Apple Pay 58% faster; Google Pay 50% faster at Fandango | Vendor/secondary [M–L] |
| One-click effect on spend | +28.5% spend, +43% purchase frequency (Cornell study of one-click adopters) | Academic via secondary [M] |
| Return-policy leniency | Increases purchases more than returns; monetary and effort leniency raise purchases; longer windows *reduce* return rates (endowment) | Janakiraman, Syrdal & Freling, J. Retailing 2016, 22 studies [H] |
| Steam refund rate | Median indie ~9.5–10.8% of units; Rust 6% of 5.5M | GameDiscoverCo survey, developer statement [M] |
| Audible returns | 365-day self-service; soft limit ~3 per rolling 30 days | User reports [L] |
| Donation banner fatigue | Drop-off after 4–5 impressions; >75% of donors give on 1st or 2nd impression (Track 1) | Wikimedia [M–H] |
| "Cover the fees" opt-in, church giving | ~60% of donors (Tithe.ly); 50–60% across platforms | Vendor [M] |
| First-time church givers using Apple Pay | 59% | Pushpay 2025 [M] |
| Checkout round-up / add-$1 opt-in | ~22% median round-up; 17–18% add-$1 (Track 2) | Change.io [M] |
| PWYW with suggested price | +8% sales; −65% average price without an anchor | Gumroad via aggregator [L] |

Not found publicly: a clean "time from wall to paid" distribution for any consumer AI product; checkout completion for digital goods under $25 specifically; free-to-paid conversion for any one-time-pack AI product. These are open uncertainties (Section 11).

---

## 4. What the mediocre and the bad get wrong (negative controls)

| Pattern | Where seen | Why it fails | CiC rule |
|---|---|---|---|
| Meter that drains on success | Duolingo Energy (2025) | Punishes the behaviour the product wants; read as a trap | No visible meter during a conversation; limit shown only at boundaries (Track 1) |
| Free users cannot buy more | ElevenLabs (PAYG top-ups only from Starter plan) | The person who wants to pay is told to subscribe instead | Anyone, signed in or not, can buy a pack |
| Expiring purchases | Midjourney fast hours (monthly), Audible credits (12 months), Poe points (1 year) | Loss-framed; litigated (Hollis v. Audible) | Purchased conversations never expire |
| Refund rule that cannot be used | Midjourney (<20 GPU-minutes), Hallow (case-by-case, web only, 14 days) | A refund policy nobody can meet is a trust negative | One-sentence rule, automated inside it |
| Trial-to-annual billing surprise | Hallow, Pray.com, Audible complaints | For a faith audience this reads as betrayal | Not applicable to one-time, but the *copy* must say "no subscription, nothing recurring" |
| AI-only support, no human | Hallow, Audible complaints | Billing problems need a person | A named, human-answered support address with a stated response time |
| Message caps as teaser; emotional manipulation at goodbye; blurred-image upsell | Replika, Character.AI (FTC complaint Jan 2025; CDT taxonomy of 37 chatbot dark patterns; "emotional manipulation" at goodbye) | Monetizes attachment | The Representative never sells; the wall is Facilitator-governed and template-anchored (CLAUDE.md) |
| Silent allowance cuts | Poe (free points cut ~90%, Premium allowance cut, 2026) | Destroys the legibility that credits depend on | Any change to a free allowance is announced in advance on the page |
| Quietly narrowing a trust mechanic | Humble (slider removal, 15% cap, 2021) | Reversal came only after backlash | Treat the support split and refund rule as commitments; changes are announced change orders |
| False urgency in asks | Wikipedia banners pre-2022 (rejected 45–3 by editors) | Untrue, and tested worse than honest copy | No countdowns, no "we'll disappear" |
| Asks that keep hitting supporters | Guardian (sync gaps) | Makes the thank-you hollow | Suppression keyed to the paid balance, cross-device |
| Ads inside the paid experience | Pray.com ("like commercial interruptions in Church") | Breaks the frame the product sells | No ads, ever, in a conversation |

---

## 5. Cross-cutting principles the best share — the quality bar

Each item is phrased so it can be scored pass/fail against a CiC build.

**A. Before any ask**
1. The first-run experience completes a *whole* unit of value without an account (Duolingo, ChatGPT, Guardian, Kagi). For CiC: one complete conversation, signed out.
2. Sign-up, if asked, comes after the aha and is cheaper than a password (magic link; Track 1).
3. The pricing page exists and is linked from the start, with exact numbers (Headspace, Kagi): pack prices, price per conversation, "never expires," refund rule, "no subscription."

**B. Communicating the limit in advance**
4. The shape of the free allowance (how many, when it refreshes) is stated in plain words on the first screen that could lead to the wall, not discovered at the wall (ChatGPT, Kagi).
5. No running meter during use; a calm indicator only when a boundary is near ("room for a few more exchanges"), in the Facilitator's register, never the Representative's (ChatGPT voice, Track 1).
6. A balance, when one exists, is visible in the header on every screen (Steam, Audible).

**C. The limit moment**
7. The wall arrives *between* units, never inside one; no reply is ever cut (ChatGPT degrade pattern; no surveyed product interrupts mid-answer).
8. The wall states, on itself: what was saved, why there is a charge (cost-structure appeal), what the guarantees are (no expiry, failed replies never count, resumable), when the free allowance returns, and a plain "Not now" (Track 1's shape; Hallow's explanation; Wikipedia's honest-copy test).
9. No countdowns, no pre-selected pack, no discount-on-dismiss, no confirmshaming (FTC 2022; Wikipedia RfC).

**D. The purchase flow**
10. Guest checkout by default; no account required to pay (Baymard: 18–26% abandon on forced accounts; Ko-fi).
11. Wallets first and early: Apple Pay / Google Pay / Link rendered above the card form, not below it (Stripe: ~2x when early; +22% where surfaced; Pushpay: 59% of first-time givers use Apple Pay).
12. A returning buyer pays in one tap with a saved method; a new buyer in under a minute with a wallet, under two with a card (Link ~6 s; wallet ~42 s; manual ~85 s).
13. The checkout asks for nothing it does not need: amount/pack, payment, and (for recovery) an email (NPR: removing one unanswerable question doubled completion).
14. The whole price is shown before the pay button; no fees appear late (Baymard top cause; FTC drip pricing).
15. Receipt by email within a minute, with the plain-language refund rule and a recovery code or link (Track 3; Stripe receipts).
16. A separate support/scholarship lane with a suggested amount and a visible split (Humble slider; Gneezy; itch open share).

**E. The return experience**
17. Re-entry shows the balance and the unfinished conversation with a one-tap "Continue"; nothing paid is ever lost to a refresh (Track 1, Vercel resume pattern; Steam library).
18. One thank-you, once; then silence. No upsell on re-entry for anyone with a balance; the support ask is suppressed for anyone who has paid (Guardian intent; Signal placement).
19. Purchased units never expire; the balance is the reason to come back (Midjourney purchased-hours rule; Steam wallet).

**F. Support and refunds**
20. A one-sentence refund rule, automated inside it (Steam: 14 days / 2 hours, automatic), lenient enough to be a trust signal (meta-analysis: leniency raises purchases more than returns).
21. Self-service return of an unsatisfying unit (Audible: credit back immediately) — for CiC, "this conversation wasn't what I needed" returns the unit, with a soft abuse limit reviewed by a human.
22. A human can be reached, and the page says how long it takes (the Hallow/Audible failure).
23. Automatic credit-back for anything not delivered (Kagi Fair Pricing; Track 1 failed-reply rule).

**G. Trust signals**
24. A "why we charge" page in the project's own voice, with the money's destination and the free core named (Hallow, Kagi, Guardian Epic).
25. Public numbers where honest (Kagi stats; Wikimedia reports): what a conversation costs to run, how many have been given free.
26. The purchase surface looks and sounds like the product (MARVEL SNAP web shop; Guardian), at the same reading level as the Representatives.
27. Changes to allowances, splits or refund rules are announced in advance and never narrowed quietly (Poe and Humble as the failures).
28. Payment never asks for more identity than the product does; supporter status is visible only by choice (Signal).

---

## 6. Accessibility and non-native-English considerations

**Reading level and plain language.** WCAG 3.1.5 (AAA) asks that text not require more than lower-secondary reading ability (roughly 7–9 years of schooling) or that a simpler version exist; it names second-language readers among the beneficiaries. [H] CiC's own bar (CEFR B2, FK grade 8–10, FRE ≥ 60) is already in that band for Representative dialogue; the same scorer should run on every string in the wall, checkout, receipt and refund page. Practical rules that follow from the sources: one idea per sentence; no financial jargon ("transaction," "remittance," "pro rata"); numbers as digits with currency symbols; the refund rule as a sentence, not a policy link; error messages that say what to do next.

**Localized currency and language.** Stripe's localization guidance: showing a foreign currency makes buyers mentally convert and fear hidden exchange fees; show and charge in the buyer's currency where possible; the full flow (labels, errors, confirmation emails) in the buyer's language, not browser translation. Stripe Checkout localizes into 34 languages from the browser locale and Adaptive Pricing presents local currency in 150+ countries. [M] Caveat from Track 2: EU/UK display must be tax-inclusive; a merchant of record handles that at small scale.

**Modals and focus (the wall is a dialog).** The WAI-ARIA APG modal-dialog pattern and WCAG 2.2 require: `role="dialog"` with an accessible name (`aria-labelledby`), `aria-modal="true"` with background content inert, initial focus on the first meaningful control (or the dialog itself), Tab/Shift+Tab cycling inside, Escape closes, and focus returns to the opener on close. The native `<dialog>` element handles trapping and Escape and is the recommended base. The three most common failures: no focus management, no keyboard escape, screen reader unaware the dialog opened. Test: open with keyboard only, tab around twice without landing behind the dialog, press Escape and confirm where focus lands; repeat with NVDA, VoiceOver and JAWS. [M–H] Hosted Stripe Checkout is tested against those three screen readers and keyboard navigation at roughly WCAG 2.1 AA for core flows; a custom Payment Element implementation inherits CiC's own responsibility for the surrounding page. [M]

**Mobile.** ~70–76% of traffic and ~7 in 10 orders are mobile, where abandonment is 15–20 points higher; wallets close most of that gap. The wall must work at phone width with a 16px gutter, no horizontal scroll, and tap targets ≥ 24×24 CSS px (WCAG 2.2 2.5.8).

**Cognitive load.** One decision per screen (NPR); the three packs on one row with price per conversation under each; "Not now" as a real button, not a link in grey.

---

## 7. Faith-sector sensitivities

What the evidence says users and donors of faith products find off-putting or reassuring:

**Off-putting**
- *Being charged after cancelling a trial* is the dominant complaint against Hallow and Pray.com on BBB/Trustpilot, read not as a billing error but as a breach of faith by an organisation that claims to serve the Church. [L–M, self-selected review sites]
- *Ads inside devotional content* ("like commercial interruptions in Church"; Pray.com reviews).
- *Commerce in the voice of the sacred*: reviewers cite "Jesus did not charge for teaching the crowds" and the cleansing of the temple. The ask must never come from the Representative or borrow its register (CLAUDE.md: the redirect and the wall are Facilitator-governed).
- *"Missionary alarm"*: a 2025 study in the International Review on Public and Nonprofit Marketing finds donation intent falls when people perceive a faith-affiliated organisation as having a hidden proselytising or manipulative intent behind a stated helping purpose. [M, abstract via search summary] For CiC — a scholarly, multi-tradition product — the reassurance is to say exactly what the money buys (compute, source work, free access for others) and nothing about spiritual standing.
- *Any link between payment and seriousness or standing* (Track 1's judgment; consistent with the above).

**Reassuring**
- *A large, genuinely free core, named* (Hallow: "free forever"; YouVersion: everything free, ~40,000 donors, nothing gated). Churchgoers are used to the gift-first posture.
- *A scholarship or honor-system path with no proof required* (Hallow; Freedom of the Press Foundation sliding scale, Track 2).
- *Give-one-get-one and clergy-free* lanes (Hallow).
- *Fee transparency and the option to cover fees*: ~60% of church donors opt to cover processing fees when asked plainly (Tithe.ly), and 75% of Christians want a seamless online giving experience (Barna via Subsplash). [M]
- *Frictionless mobile pay*: 59% of first-time church givers use Apple Pay (Pushpay 2025). [M]
- *Stewardship language and financial reports*: "transparency through financial reports fosters trust" is the consistent finding across Pushpay/Givelify 2025 material. [M]
- *No pressure*: the Guardian/Wikipedia evidence that honest, unhurried asks convert at least as well applies with more force to a faith-adjacent audience that is primed to notice manipulation.

One constraint specific to Faithways: as a Colorado PBC it cannot show the 501(c)(3) badge that Khan Academy, Wikimedia and Signal lean on, and gifts are not deductible (Track 3). The substitute is the PBC's public benefit statement, an annual plain-language "where the money went" note, and the published cost-per-conversation line.

---

## 8. Composite "whole journey" as the best in the set would build it for CiC

Written as the experience, not as requirements, so it can be reacted to.

1. **Arrive.** The Family Tree opens, free, no sign-in. One line under the first world: "Your first conversation is free. After that, conversations cost a few dollars each and never expire. Here's why." (link to the why-we-charge page). Reading level checked.
2. **Converse.** A whole conversation with a Representative; no meter, no counter. At the natural end the Facilitator closes it. If the participant is near the internal cap, one calm line earlier: "This conversation has room for a few more exchanges."
3. **Second visit, signed out.** "You've had your free conversation this week. It's saved. To keep going, sign in with your email (three more are free) or pick a pack." Magic link; no password.
4. **Wall (Facilitator voice, dialog that passes the APG checklist).** Status line; one-sentence reason; three packs with price and price-per-conversation, none pre-selected; guarantees line ("Never expire. A failed reply never costs one. You can always return to an unfinished conversation. Refund any unused conversations, no questions asked."); "Not now" button; the refresh date; a quiet "Support the work" link.
5. **Pay.** Apple Pay / Google Pay / Link above the card form; guest checkout; local currency; whole price shown; one optional "add $1 to the scholarship pool" line (default off); "No subscription. Nothing recurring." under the button. Hosted Stripe Checkout in the participant's language.
6. **Confirm.** Back in the Family Tree within seconds: "Thank you. You have 11 conversations. Your receipt and a recovery code are in your email." Balance now in the header. The open conversation offers "Continue." No further ask of any kind.
7. **Return later.** Header shows the balance; the thread list shows "Continue"; no banner. The support link remains in the footer, not in the flow.
8. **Something goes wrong.** A reply fails: nothing is deducted and the page says so. A conversation wasn't what they needed: "Return this conversation" on the thread restores the unit (soft limit, human review). A refund: one tap on the receipt page refunds unused conversations to the card or to the balance. A person answers support within a stated time.
9. **Changes.** If a free allowance or pack ever changes, it is announced on the pricing page in advance and never narrows what someone already bought.

---

## 9. Gap analysis — adequate vs top-flight

| Stage | Merely adequate (sound, defensible) | Top-flight (matches the best in the set) |
|---|---|---|
| First run | A few free turns, then a sign-up wall | One whole free conversation, signed out; sign-in optional and rewarded |
| Limit in advance | A help-page explanation | The rule in one line on the first screen; a calm near-boundary indicator; balance in the header |
| Limit moment | A modal with packs and a "Buy" button | A Facilitator-voiced dialog with reason, guarantees, refresh date and a real "Not now"; never mid-reply; WCAG-passing |
| Purchase | Hosted Stripe page with card entry | Wallets first and early, guest checkout, local currency and language, whole price, no-subscription line, one optional scholarship add-on |
| Confirmation | Stripe receipt email | In-product thank-you with balance and "Continue"; receipt with recovery code and refund rule in plain words |
| Return | Balance somewhere in settings | Balance in header; unfinished conversation resumable for days; zero upsell; ask suppressed once paid |
| Support/refund | A policy page and a contact form | One-sentence rule, automated inside it; self-service return of a unit; failed replies auto-credited; human reply time stated |
| Trust | Terms and privacy links | "Why we charge" page; public cost-per-conversation and free-conversations-given counts; announced changes only |
| Accessibility | Default browser behaviour | Native `<dialog>`, focus management, screen-reader tested, B2 copy, 24px targets |
| Faith register | No religious language in checkout | Gift-first framing, scholarship/honor path, clergy lane, nothing linking payment to standing; the Representative never sells |

The adequate column is roughly what Tracks 1–3 already specify on the backend. The top-flight column is almost entirely front-of-house and copy; none of it changes the ledger or Stripe design.

---

## 10. The ten highest-leverage practices to copy, ranked

1. **Wallets first, guest checkout, nothing extra asked** (Stripe, Shopify, NPR, Baymard). Largest measured effect on completion; cheapest to do with hosted Checkout.
2. **The whole first conversation free, before any identity** (Duolingo, ChatGPT, Guardian). The aha is the product; everything downstream depends on it.
3. **The wall between conversations, in the Facilitator's voice, with guarantees printed on it** (ChatGPT degrade pattern; Track 1 shape; Wikipedia honest-copy test).
4. **A one-sentence, automated, lenient refund rule** (Steam; Janakiraman et al.). Raises purchases, lowers disputes, and is the strongest single trust signal available to a non-501(c)(3).
5. **Balance in the header, purchases never expire, unfinished conversations resumable** (Steam, Audible's good half, Midjourney's purchased-hours rule).
6. **One thank-you, then silence: no upsell on re-entry, asks suppressed for anyone who has paid** (Guardian's intent, Signal's placement).
7. **A "why we charge" page with the free core, the money's destination and the scholarship path named** (Hallow, Kagi, Khan Academy).
8. **Self-service "this wasn't what I needed" return of a unit, and automatic credit for anything not delivered** (Audible, Kagi Fair Pricing).
9. **Checkout copy at the Representatives' reading level, in the buyer's language and currency** (Stripe localization, WCAG 3.1.5).
10. **A native, tested, accessible dialog for the wall** (APG pattern; three screen readers; keyboard-only test).

Deliberately below the line: badges and perks (Signal, Internet Archive) — nice, not leverage; checkout round-up — worth testing after the above; a 30-day pass — hold in reserve (Track 1).

---

## 11. Open uncertainties

1. **No public free-to-paid conversion exists for a one-time-pack AI conversation product.** Every AI benchmark here is a subscription; every consumable benchmark is a game or a credit subscription. CiC's own first quarter is the only source.
2. **Checkout completion for sub-$25 digital goods on mobile** is not published separately; the 47–65% figures are DTC physical goods.
3. **Whether the "return this conversation" rule is abused** — Audible's experience says a soft limit is needed; what that limit should be for a scholarly product is unknown.
4. **Hallow's and Audible's complaint volumes are from self-selected review sites**; the rate per customer is unknown. They are directional evidence about *what* upsets faith and credit customers, not about *how often*.
5. **The "missionary alarm" finding** rests on one 2025 study (abstract only accessible); treat as a hypothesis to design against, not a settled effect size.
6. **Stripe's wallet-lift figures are vendor-published** and vary 7%–2x by study and placement; the direction is secure, the magnitude for CiC is not.
7. **Suppressing asks after payment across devices** is a known hard problem (Guardian); it depends on Track 3's visitor-id and claim-code recovery actually working for people who clear cookies.
8. **Primary-page verification.** Nearly every primary page was blocked this round; the figures for Hallow's commitments, Steam's refund mechanics, Kagi's stats, the NPR form, the Khan A/B test and the Stripe 50+-method study should be re-read from an unblocked network before any of them becomes a quoted number in a canonical document.
9. **Whether a PBC without deductibility can earn the trust a 501(c)(3) badge buys** — no comparable evidence found; the substitutes in Section 7 are reasoned, not measured.

---

## Sources (accessed 2026-10-02; "via search summary" where the page itself was blocked)

AI chat and tutors: Northflank, techjacksolutions, chatai.guide, howdoiuseai (ChatGPT limits, Aug 2026 change); cloudzero, digitalapplied, multichats (ChatGPT Go); khanmigo.ai/pricing, Khan Academy support, GoFundMe Pro case study (Khan A/B), Nibble, myengineeringbuddy; heyuan110, nesyona, christopheralarcon (Claude free plan); CDT "Dark Patterns in AI Chatbots: A Taxonomy," 404 Media, Time (Replika FTC complaint), ACM CHI 2025 "Dark Side of AI Companionship," arXiv "Playing Games with My Heart."

Learning and meditation: Duolingo 8-K and Q2 2026 shareholder letter (SEC EDGAR, investors.duolingo.com); screensdesign, tasu.ai, adplist substack, RevenueCat (Cem Kansu) teardowns; Apple Newsroom 2023 Apple Design Awards; comparably, kimola, approast (Duolingo reviews); abtest.design, Purchasely, Sub Club, insidergrowthhq, raw.studio (Headspace); Business of Apps, Udonis, getlatka (Headspace/Calm estimates); Brilliant help center; upskillwise (MasterClass).

Faith: Hallow blog "Why is there a Hallow subscription?", Hallow help center, Appfigures, Contrary Research, Homebrew, Notre Dame IDEA Center, learnofchrist, thedolceway (Hallow); BBB and Trustpilot (Hallow complaints); Trustpilot and Google Play (Pray.com, Abide); YouVersion support, growthcasestudies, Protestia (YouVersion); Springer IRPNM 2025 "NGO's religious affiliation and donation intent: missionary alarm and manipulative intent"; Tithe.ly, churchmemberpro (cover-the-fees); Pushpay 2025 giving statistics; Givelify 2025–26 report; Barna via Subsplash.

Consumables and stores: Audible return guides (pocket-lint, goodereader, audiobookaddicts, thereturnguide), Goodreads #audiblegate thread, Trustpilot (Audible); Steam refund policy coverage (PC Gamer, gamingprofileviewer, dealcheckpoint), Steam community threads (wallet minimums), GameDiscoverCo refund survey, Game Developer, TweakTown (Rust); Xsolla blog and newsroom, BusinessWire (MARVEL SNAP web shop), Metacritic/App Store (SNAP reviews), Trusted Reviews (Monument Valley 5%), Game Developer/MCV (Supercell); eesel, pxlpeak, felloai (Midjourney); TechCrunch, Sacra, getlatka (ElevenLabs, Midjourney revenue); Humble Bundle Wikipedia, Kotaku, NME, Game Developer, PCGamesN (slider changes), BusinessWire/GamesBeat ($250M); itch.io docs ("open revenue sharing"); Ko-fi/Buy Me a Coffee comparisons; insightraider (Gumroad PWYW).

Mission-driven revenue: Press Gazette, Digiday, INMA, grandgoldman, britbrief (Guardian accounts); Asbury & Asbury, Simon Owens, Dick Tofel (Guardian Epic); Wikipedia:Fundraising/2025 banners (fetched), Wikipedia:Fundraising/2022 banners, Slate (2022 dispute), Wikimedia Diff FY24–25 audit highlights, Meta-Wiki Fundraising reports; Kagi pricing and help center, blog.kagi.com, kagi.com/stats, Android Police (Fair Pricing), Hacker News (50k, no-use-no-pay); Signal blog "Signal Your Support," Signal donor FAQ, Android Authority, XDA, aboutsignal, Wikipedia (Signal Foundation revenue); Current.org (NPR Network donations, 2023 and 2025), Greater Public benchmarks; blog.archive.org (Monthly Giving Circle, fetched; P2P fundraising); Mozilla donate FAQ.

Checkout and payments: Baymard "Checkout UX Best Practices 2025" and cart-abandonment statistics via growthegy, zerocartai, dextora, eightx; Stripe "Testing the conversion impact of 50+ global payment methods," Stripe newsroom (10.5% uplift), Stripe Checkout and Link pages, Stripe payment-localization guide, Stripe Adaptive Pricing docs, Stripe supported-languages support page; Shopify Shop Pay and mobile-vs-desktop posts; envive, swell, owlclaw, blendcommerce, qualimero (benchmarks); gr4vy, convertcart, nomupay (wallet speed); Jotform (Link); Krepling (guest checkout); testparty.ai (Stripe Checkout accessibility); Janakiraman, Syrdal & Freling 2016 (J. Retailing; phys.org, UT Dallas); Conversion Fanatics, RevenueCat (money-back guarantees); CXL, Aureate Labs (thank-you pages).

Accessibility: W3C WAI-ARIA APG modal dialog pattern (blocked; via secondary: accessibility.build, Vispero, AudioEye, NZ Government web accessibility guidance, thewcag.com, wcagc.com, CSS-Tricks on `<dialog>`); WCAG 3.1.5 Understanding (W3C) and wcag.com, AAArdvark, equalweb summaries.
