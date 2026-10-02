# Track 1 — Access tiers and the unit of access

Research for Church in Conversation (Faithways Studio, Inc.). Web-based, dated 2026-10-02. No internal CiC numbers were used or consulted. Every figure below carries its source URL; figures from secondary aggregator sites are flagged as such and should be treated as indicative, not audited.

Constraints taken as given: Church Family Tree is always free; the conversation engines (Interview mode, Build a Table) are limited for free/unauthenticated visitors; one-time pay-as-you-go top-ups, no recurring billing; pay-as-you-go must be a real financial engine.

Note on method: direct fetches of several primary pages (RevenueCat, Runway help center, Hallow, PubMed Central) were blocked by the sandbox egress proxy, so those points rest on search-engine summaries of the primary page plus secondary coverage. They are marked "(via search summary)".

---

## 0. Executive summary and headline recommendation

**Recommendation (moderate-high confidence):** Meter in **whole conversations** ("Conversations" as the visible unit a visitor buys and spends), implemented underneath as a turn budget per conversation that is generous enough that almost no one hits it. A conversation is only "spent" when the first Representative reply is delivered successfully; everything after that — refresh, back button, closed tab, dropped connection — resumes the same conversation for a long grace window (days, not minutes). Failed or interrupted replies never consume anything. Purchased conversations never expire.

**Why this unit:** it is the one unit that (a) matches what the participant actually values (a real exchange with a tradition, not a message count), (b) avoids the documented "taxi-meter effect" that makes per-message pricing feel like a running meter, (c) is the only unit that answers Mark's accidental-exit question with a clean "no, you lose nothing," and (d) is legible on a pricing page in one sentence without a glossary (a point EU regulators now explicitly demand for virtual currencies).

**Free tier:** one complete signed-out conversation per device per rolling period, plus a small email-gated allowance (e.g., 3 conversations on account creation), so the "aha" is a *whole* exchange, not a truncated one. Charge only for repeat use, never for the first real encounter.

**The wall:** a soft, dismissible, end-of-conversation upgrade sheet (never mid-answer), two or three pack sizes with the middle one anchored as the obvious choice, plus a visible "support the project" pay-what-you-want path that is separate from the packs. Copy that states plainly what costs money and why, with no countdowns, no guilt-buttons, and prices shown in dollars not points.

The rest of this document gives the evidence and the options considered.

---

## 1. Question (a): what unit of access do comparable systems meter in?

### 1.1 Survey of what is actually in use (as of mid/late 2026)

| Product | Unit metered | Free allowance | Notes |
|---|---|---|---|
| ChatGPT Free | messages per rolling window (model-tiered) | ~10 messages / 5 hours on the default model, then auto-downgrade to a mini model; not published, deliberately flexible | Degrades rather than blocks. Signed-out mode: ~3–5 messages then a sign-up wall. Voice: ~15 min/day with a 3-minute warning. |
| Claude Free | session-based compute allowance, rolling 5-hour window | no fixed message count published | Varies with message length and model. |
| Gemini Free | compute-based limits, 5-hour refresh inside a weekly ceiling (since May 2026) | previously "5 Pro prompts/day" | Moved *away* from countable prompts. |
| Perplexity Free | "Pro searches" per day | 3–5/day (reports differ), unlimited basic search | Two-speed: unlimited cheap, capped expensive. |
| Character.AI Free | throttling, swipes/day, "continues"/day, queue at peak | ~50–80 messages/day on busy days (user-reported), ~400 swipes | Degrades by queueing; c.ai+ ($9.99/mo) skips the line. Ads mid-conversation. |
| Poe | compute points (per-message cost varies by bot) | ~300 points/day free (cut ~90% in March 2026 without announcement) | Add-on points sold one-time at $30/1M, usable for one year, non-refundable. |
| Pi (Inflection) | rate limits only, no paid tier | free | A pure "limits without a product to buy" model. |
| Replika | feature gating (voice, modes), not message counts | unlimited text | Lifetime tier ($299.99) was discontinued July 2025 — relevant cautionary tale for one-time models that promise forever. |
| Duolingo (Energy) | per-exercise energy units, 25 to start, refill by time/ads/gems | effectively ~3 lessons before a wall | Replaced hearts in 2025; wide backlash because *correct* answers also drain energy — a worked example of a unit that feels punitive. |
| Khanmigo | flat subscription $4/mo or $44/yr; free for US teachers | — | Nonprofit; chose a cheap flat fee, not metering. |
| Cambly | minutes per week, expire every Monday | — | Expiry-without-rollover is the most-cited complaint. |
| Midjourney | GPU time (fast hours); monthly allocation expires, *purchased* extra hours never expire | — | Shows a two-rule pattern: allowance expires, purchases don't. |
| Audible | credits, 1 per month, roll over, expire 12 months after issue | — | Expiry is now being litigated (see §1.5). |

Sources: ChatGPT limits [Northflank](https://northflank.com/blog/chatgpt-usage-limits-free-plus-enterprise), [freeacademy.ai](https://freeacademy.ai/blog/chatgpt-free-plan-limits-2026), [chatai.guide](https://chatai.guide/limits/chatgpt-free-plan-limits/); signed-out ChatGPT [How-To Geek](https://www.howtogeek.com/chatgpt-no-longer-needs-an-account/), [meetaitools](https://meetaitools.com/can-you-use-chatgpt-for-free-without-account/); voice limits [Neowin](https://www.neowin.net/news/chatgpts-advanced-voice-mode-comes-to-free-users-with-usage-limits/), [precallai](https://precallai.com/chatgpt-voice-mode-daily-limit-for-free-users-complete-guide); Claude [datastudios](https://www.datastudios.org/post/claude-free-limits-updated-usage-restrictions-message-caps-and-file-upload-rules); Gemini [Android Police](https://www.androidpolice.com/google-changing-how-gemini-usage-limits-work/), [Tom's Guide](https://www.tomsguide.com/ai/geminis-free-tier-is-capped-at-5-prompts-heres-how-to-get-more-without-upgrading); Perplexity [finout](https://www.finout.io/blog/perplexity-pricing-in-2026), [felloai](https://felloai.com/is-perplexity-ai-free/); Character.AI [eesel](https://www.eesel.ai/blog/character-ai-pricing), [roborhythms](https://www.roborhythms.com/character-ai-daily-message-limit/), [aicompanionpick](https://www.aicompanionpick.com/character-ai-token-system-and-limits-explained); Poe [aisotools](https://aisotools.com/poe-pricing), [Poe Purchases FAQ](https://help.poe.com/hc/en-us/articles/19945140063636-Poe-Purchases-FAQs), [Poe Terms of Sale](https://poe.com/pages/terms-of-sale); Pi [usagepricing](https://www.usagepricing.com/blueprint/pi); Replika [eesel](https://www.eesel.ai/blog/replika-ai-pricing), [lifetime discontinued](https://myhusbandthereplika.wordpress.com/2025/07/28/so-replika-has-discontinued-their-lifetime-subscription-tier/); Duolingo Energy [duoplanet](https://duoplanet.com/duolingo-energy-system/), [Android Authority](https://www.androidauthority.com/quitting-duolingo-energy-system-3599842/), [toptechguides](https://toptechguides.com/duolingo-energy-update-backlash/); Khanmigo [khanmigo.ai/pricing](https://www.khanmigo.ai/pricing); Cambly [Cambly help](https://camblyenglish.zendesk.com/hc/en-us/articles/360000312583-Can-I-use-my-unused-minutes-later-); Midjourney [eesel](https://www.eesel.ai/blog/midjourney-pricing), [uxmagic](https://uxmagic.ai/blog/midjourney-pricing); Audible [gladreaders](https://gladreaders.com/how-do-audible-credits-work/), [readiolist](https://readiolist.com/blog/how-long-does-audible-credit-last/).

### 1.2 The five candidate units, with tradeoffs

**Option A — Messages / turns.** The industry default for free tiers (ChatGPT, Character.AI). Pros: simplest to meter; maps to cost. Cons: this is the unit most exposed to the *taxi-meter effect* — Lambrecht & Skiera's finding that consumers get less enjoyment from a service when each increment visibly costs money, and will overpay for a flat rate to avoid that feeling ([Lambrecht & Skiera, JMR 2006](https://www.marketing.uni-frankfurt.de/fileadmin/Publikationen/Lambrecht_Skiera_Tariff-Choice-Biases-JMR.pdf); [Slate summary](https://slate.com/news-and-politics/2013/12/the-taxi-meter-effect-why-do-consumers-hate-paying-by-the-mile-or-the-minute-so-much.html)). For a reflective, scholarly conversation, a visible per-message counter is precisely the wrong emotional frame: it rewards short, shallow exchanges and punishes the follow-up question that is the whole point. It also makes the accidental-exit problem worse, because partial spend is the norm.

**Option B — Credits / points / tokens (abstract currency).** Poe, Midjourney, Runway, Suno. Pros: lets heavy users pay more without a subscription; RevenueCat notes AI apps "finding success with credit-based systems that let heavy users pay more without forcing everyone onto a subscription" (via search summary of [RevenueCat SOSA 2025](https://www.revenuecat.com/state-of-subscription-apps-2025)). Cons: opacity. Poe cut its free allowance ~90% silently; EU consumer authorities' 2025 Key Principles on virtual currencies now require that in-app currency be priced "clearly in real-world money," that mixing currencies or forcing exchanges be avoided, and that consumers be able to buy "the specific amount they wish" rather than forced bundles; the Commission opened enforcement against nine game companies on 29 Sept 2026 ([Linklaters](https://techinsights.linklaters.com/post/102k6t4/game-changer-eu-introduces-consumer-protection-guidance-for-in-game-virtual-curr); [European Commission](https://commission.europa.eu/topics/consumers/consumer-rights-and-complaints/enforcement-consumer-protection/coordinated-actions/social-media-online-games-and-search-engines_en)). The forthcoming Digital Fairness Act may classify unused virtual currency as digital content subject to a 14-day withdrawal right ([Freshfields](https://www.freshfields.com/en/our-thinking/blogs/technology-quotient/the-eus-proposed-digital-fairness-act-a-game-developers-guide-to-potential-imp-102ltio)). Credits also carry the strongest "did I lose money?" anxiety, which is exactly Mark's concern. Verdict: avoid an abstract currency. If a per-unit price is needed, price in dollars per conversation.

**Option C — Whole conversations / sessions.** Rare among the big chat products (they meter messages), but standard wherever the product is an *encounter* rather than a utility: tutoring (Cambly/Preply sessions), therapy and coaching apps, Audible's "one credit = one book." Pros: the unit is the thing the participant came for; one clear price; no running meter during the exchange; the natural place to show the paywall is *between* conversations, not inside one; "accidental exit" has a clean answer (the conversation is still there). Cons: needs an internal cap (a turn or token ceiling) so a single conversation can't run unbounded; needs a definition of "when is a conversation spent"; a participant who only asks one question "wastes" a conversation unless design handles it (see §1.4).

**Option D — Time passes (day pass / week pass).** Common for news; less common for AI chat. Pros: flat-rate feeling for the pass window (the insurance effect Lambrecht & Skiera describe); simple. Cons: non-recurring passes rebuild the subscription anxiety in miniature ("it ran out while I wasn't using it"); encourages bingeing then lapsing; cost exposure is unbounded during the pass. Could work as a *third* pack type ("a week of unlimited conversations") but is a poor primary unit for a product where use is episodic.

**Option E — Daily / rolling refresh (free quota that refills).** ChatGPT's 5-hour window, Gemini's 5-hour/weekly, Perplexity's per-day Pro searches, Duolingo energy. Pros: cheap way to let free users keep coming back; the refresh itself is a retention hook. Cons: only a *free-tier* mechanism; it does not generate revenue and tends to train users to wait rather than pay. Useful as the shape of the free allowance, not as the paid unit.

### 1.3 Mark's question: "How many rounds is a conversation, and if a visitor accidentally backs out do they lose the money?"

**How products actually handle it (evidence):**

- *API/credit services refund on technical failure, not on dissatisfaction.* Runway: credits "are only automatically returned when a generation ends in a generation error"; completed-but-unsatisfactory outputs are consumed; timeouts in the first half of processing refund automatically, otherwise contact support (via search summary of [Runway help](https://help.runwayml.com/hc/en-us/articles/34266159290003-Can-I-have-credits-refunded); [techsifted](https://techsifted.com/troubleshooting/runway-ml-not-working/)). ElevenLabs: rejected requests are not charged, but each retry counts ([codeables](https://codeables.dev/article/elevenlabs-billing-faq)). OpenAI prepaid credits refund only for a "confirmed OpenAI service failure," billing error, or unauthorized use ([OpenAI help](https://help.openai.com/en/articles/8264644-setting-up-and-managing-prepaid-api-billing)).
- *Products that charge for failures generate the worst reviews.* Suno and Adobe Firefly draw sustained complaints for deducting credits on failed generations ([Trustpilot Suno](https://dk.trustpilot.com/review/suno.com); [Adobe community](https://community.adobe.com/bug-reports-403/adobe-taking-credits-when-generation-fails-1550475)). The pattern: charging when the system failed is read as predatory regardless of the amount.
- *Session persistence is a solved engineering problem and now expected.* The Vercel AI SDK documents "resuming ongoing streams after page reloads"; open-source chat UIs treat loss of conversation on F5 as a bug, not a feature ([AI SDK docs](https://ai-sdk.dev/docs/ai-sdk-ui/chatbot-resume-streams); [openclaw issue](https://github.com/openclaw/openclaw/issues/6327); [zknill](https://zknill.io/posts/chatbots-worst-enemy-is-page-refresh/)). Server-side tracking of the active stream and replay to a reconnecting client is the standard approach.
- *Metered-minute products that don't roll over are the ones users leave.* Cambly's expiring weekly minutes are the top complaint in comparison reviews; Preply's rolling-over credits are cited as the contrast ([Preply vs Cambly](https://preply.com/en/blog/preply-vs-cambly/); [speakshark](https://speakshark.com/blog/cambly-alternatives)).
- *Audible's model is the closest consumer analogue to "one credit = one whole thing":* credits roll over, a finished-but-disliked book can be returned for the credit within 365 days, and support reinstates recently-expired credits as a courtesy ([gladreaders](https://gladreaders.com/how-do-audible-credits-work/); [Yahoo/returns](https://www.yahoo.com/tech/did-know-return-audible-books-193013947.html)).

**Design answer that follows from the evidence:**

1. **Define "a conversation" by an outcome, not a count.** A conversation is one continuous exchange with one Representative (or one Table) on one thread. Internally cap it at N turns or M tokens where N is set well above the observed median (industry practice is to cap at the 90th–95th percentile of natural length so that the cap is almost never hit; the exact N should come from CiC's own pilot logs, not from this report). Show the participant a soft, calm indicator *only* when they approach the cap ("This conversation has room for a few more exchanges"), not a countdown from the first message. ChatGPT's voice-mode pattern — a warning at 3 minutes remaining, not a visible timer throughout — is the right shape ([Neowin](https://www.neowin.net/news/chatgpts-advanced-voice-mode-comes-to-free-users-with-usage-limits/)).
2. **A conversation is "spent" when the first substantive reply lands.** Not on open, not on first keystroke. If the first reply fails, nothing is spent.
3. **Nothing is lost on exit.** Refresh, back, closed tab, phone lock, dropped connection: the thread stays open and resumable for a long grace window (recommend 7 days minimum for paid conversations; the cost of being generous here is small because the marginal cost of an idle thread is ~zero). The thread list shows "Continue" on any open conversation. This is the single most important fairness mechanism and it is cheap.
4. **Failed or interrupted replies never deduct.** A reply that errors, times out, or is cut off by disconnect is retried free or discarded; the turn budget does not move. This mirrors the Runway/ElevenLabs rule but should be applied *more* generously (Runway's "first half of processing" rule is opaque and generates support tickets; make it "any reply that did not fully arrive").
5. **Explicit "ended early" handling.** If a participant ends a conversation after only one or two exchanges, either (a) treat conversations under a small threshold as not spent (a "short conversation is free" rule, which is simple and reads as generous), or (b) let a conversation be reopened within the grace window so a one-question visit doesn't burn a unit. (a) is simpler to explain; (b) is cheaper against abuse. Recommend (b) as the baseline and (a) only if pilot data shows many genuinely one-question visits.
6. **Purchased conversations never expire.** See §1.5 for why this is both the fairness-maximizing and the legally safer choice.

### 1.4 What UX research says makes pricing feel fair vs predatory

- **Dual entitlement (Kahneman, Knetsch & Thaler 1986):** people judge a price fair against a reference transaction; raising price to cover *cost* is accepted, raising price to exploit *demand* is not ([KKT 1986](https://www.researchgate.net/publication/4900848_Fairness_As_a_Constraint_on_Profit_Seeking_Entitlements_In_The_Market); [Xia, Monroe & Cox 2004 framework](https://www.researchgate.net/publication/228590264_The_Price_Is_Unfair_A_Conceptual_Framework_of_Price_Fairness_Perceptions)). Implication: copy that explains "each conversation costs us real compute and the scholarship behind the world" is not a disclaimer; it is the mechanism that makes the price feel fair. A 2026 JSR study finds cost-structure appeals raise both fairness perceptions and payments ([Stangl, Kastner & Natter 2026](https://journals.sagepub.com/doi/10.1177/10946705251341080)).
- **Flat-rate bias / taxi-meter effect (Lambrecht & Skiera 2006):** people pay a premium to not watch a meter. Implication: hide the meter during use; expose it only at the boundaries (before starting, when nearly out).
- **Transparency in real money:** the EU CPC principles and the FTC's drip-pricing findings both point the same way — show the whole price in dollars, up front ([FTC Bringing Dark Patterns to Light, 2022](https://www.ftc.gov/system/files/ftc_gov/pdf/P214800+Dark+Patterns+Report+9.14.2022+-+FINAL.pdf)).
- **Loss aversion cuts both ways:** charging for a failed response, or letting units expire, is felt as a loss far more sharply than the equivalent gain. Every cited complaint cluster (Suno, Firefly, Cambly, Duolingo energy, Poe's silent cut) is a loss-framing failure.

---

## 2. Question (b): consumable one-time packs vs subscription

### 2.1 What the data says

- **Hybrid is now mainstream; AI apps lean on credits.** RevenueCat 2025: 35% of apps mix subscriptions with consumables or lifetime purchases; "AI-powered apps in particular finding success with credit-based systems" ([Subscription Insider summary](https://www.subscriptioninsider.com/article-type/news/revenuecats-state-of-subscription-apps-2025-report-ais-dominance-retention-challenges-and-the-shift-away-from-pure-subscriptions)). RevenueCat 2026: 63.5% subs-only, 23.2% subs + lifetime, 10.7% subs + consumables, 2.5% all three; Gaming is 40.5% subs-only with 27.5% using consumables ([RevenueCat 2026](https://www.revenuecat.com/state-of-subscription-apps), via [arpubrothers summary](https://arpubrothers.com/blog/revenuecat-subscription-app-report-2026/)). Note the asymmetry: almost nobody runs *consumables-only*. The dataset is subscription apps, so it's biased, but it is still a warning that consumables-only is an unusual configuration.
- **AI apps earn more per payer but churn faster.** AI apps generate 41% more revenue per payer and churn 30% faster (RevenueCat 2026, via [9to5Mac](https://9to5mac.com/2026/05/27/new-report-shows-annual-app-subscribers-rarely-return-after-they-cancel/) and [RevenueCat blog](https://www.revenuecat.com/blog/growth/subscription-app-trends-benchmarks-2026)). For CiC this is actually an argument *for* one-time packs: if the natural usage pattern is episodic and churn-prone, a subscription would be bought and cancelled; a pack is bought when wanted.
- **Subscription retention is weak anyway.** ~30% of annual subscriptions cancel in the first month; cheap annual plans retain up to ~36% after a year, expensive monthlies ~6.7% ([RevenueCat 2025 via Subscription Insider](https://www.subscriptioninsider.com/article-type/news/revenuecats-state-of-subscription-apps-2025-report-ais-dominance-retention-challenges-and-the-shift-away-from-pure-subscriptions)).
- **Consumable repeat-purchase rates are low in the best-studied category (mobile games).** ~1.8% of mobile gamers pay at all; of payers, only ~28.8% buy a second time; ~26.5% of second purchases happen within 30 days and those account for ~92% of all multi-time spenders ([Unity data via wifitalents](https://wifitalents.com/mobile-game-monetization-statistics/); [Mistplay 2024](https://gamedevreports.substack.com/p/mistplay-paying-users-in-mobile-games)). Revenue concentrates: top 5% of payers drive ~50–80% of IAP revenue depending on source ([virtwave](https://www.virtwave.com/blog/in-game-purchases-statistics-2026); [Adweek](https://www.adweek.com/performance-marketing/infographic-whales-account-for-70-of-in-app-purchase-revenue/)). These are aggregator figures; treat as order-of-magnitude.
- **Breakage.** Gift-card/stored-value breakage runs roughly 3–20% depending on method and horizon; ~80% of gift-card value is redeemed within a year ([hubifi](https://www.hubifi.com/blog/gift-card-redemption-guide); [Deloitte ASC 405-20 example assumes 20%](https://dart.deloitte.com/USDART/home/codification/liabilities/asc470-10/roadmap-debt/chapter-9-debt-extinguishments/9-4-derecognition-liabilities-for-prepaid)). Breakage is real revenue but it is also exactly the revenue that feels predatory and is increasingly regulated (see §2.3). Do not build the model on it.
- **Freemium conversion baselines.** Typical self-serve freemium: 2–5%; good 3–5%, great 8–12%; AI-native products reported hotter (6–8% good, 15–20% great) ([artisangrowthstrategies](https://www.artisangrowthstrategies.com/blog/freemium-conversion-rate-benchmarks); [firstpagesage](https://firstpagesage.com/seo-blog/saas-freemium-conversion-rates/)). Mostly B2B SaaS data; consumer and mission-driven will be lower. Piano's publisher benchmark: metered paywall converts 0.36% of visitors over ~11.65 days, and registered users convert ~10x anonymous ([Piano via Twipe](https://www.twipemobile.com/developing-paywall-strategy-acquisition-retention/)).

### 2.2 The realities of a non-recurring model

Honest statement of the weaknesses:

1. **Lumpy, unpredictable revenue.** No MRR; revenue tracks traffic and news cycles. Mitigation: a *standing* pay-what-you-want support path and a periodic (not automatic) "top up again?" email that the participant opts into; plus institutional sales (churches, classes) as a smoother base — outside Track 1's scope but the natural complement.
2. **Low repeat purchase without a trigger.** Game data says ~70% of payers never buy twice. Mitigation: make the *product* produce the trigger (a new world launches; a Table the participant built gets a new seat; "you have one conversation left"), not the billing system. Keep purchased conversations non-expiring so the balance itself is the reason to return.
3. **No lock-in, so every purchase is re-won.** This is also the ethical strength of the model: nobody is paying for something they forgot. Lean into it in copy.
4. **Payment-processor fees bite harder on small tickets.** Stripe-style 2.9% + $0.30 is ~9% of a $4.99 pack but ~4% of a $14.99 one. Favor pack sizes of roughly $8–$25 and make the smallest pack the exception, not the default.
5. **App-store rules if ever on iOS/Android.** Consumables are "non-refundable once used" under both stores; Apple requires a CONSUMPTION-REQUEST response within 12 hours; Google's 48-hour window; EU 14-day withdrawal applies to unused digital content ([Apple WWDC21](https://developer.apple.com/videos/play/wwdc2021/10175/); [hubifi App Store](https://www.hubifi.com/blog/app-store-connect-refunds-guide); [subpilot Google Play](https://subpilot.tech/guides/google-play-refund)). Web-first with Stripe avoids the 15–30% store cut and these constraints. A one-time web purchase also sidesteps ROSCA/auto-renewal law entirely (see §2.3).

### 2.3 What makes consumables durable rather than one-off

Evidence-backed features, in rough priority:

- **Non-expiring purchases.** Midjourney (purchased hours), Gamma, RemNote, ZOOOP all advertise "purchased credits never expire" as a trust feature ([rizzgen comparison](https://www.rizzgen.ai/blogs/ai-video-credits-expire); [Gamma help](https://help.gamma.app/en/articles/7834324-how-do-credits-work-in-gamma); [RemNote](https://help.remnote.com/en/articles/9416169-ai-credits)). Legally: California Civil Code §1749.5 bars expiry on paid gift certificates, and *Hollis v. Audible* (W.D. Wash. 2025) let a class action proceed on the theory that Audible's expiring membership credits are "gift certificates" under Washington law — the court held the statute does not require a stated dollar value or transferability ([Justia](https://law.justia.com/cases/federal/district-courts/washington/wawdce/2:2024cv01999/342303/32/); [Courthouse News](https://www.courthousenews.com/audible-credits-gift-cards/)). Whether a "conversation pack" is a gift certificate is untested, but the safe and fair course is simply never to expire them.
- **A balance that is visible and portable across devices** (account-bound, not device-bound), so the participant can see what they own.
- **Product-generated reasons to return** (new worlds, new Representatives, a saved Table) rather than billing-generated ones.
- **A graceful "I'm out" moment** that reminds the participant what they have built and offers the same packs again without a discount game. Discount escalation ("wait, 50% off!") trains people to abandon the first modal.
- **A support/donation path alongside the packs.** Gneezy et al.'s field experiment (PNAS 2010/2012): fixed-price photos sold to ~0.5% of riders; pay-what-you-want sold ~16x more but at unsustainable prices; PWYW *with half to charity* was the only condition that was both profitable and well-paid ([Gneezy summary](https://en.wikipedia.org/wiki/Ayelet_Gneezy); [PMC3358869](https://pmc.ncbi.nlm.nih.gov/articles/PMC3358869)). Gumroad's platform data: PWYW produces ~8% more sales but a ~65% lower average price *unless a strong suggested price is shown* ([insightraider](https://insightraider.com/en/answers/does-gumroad-let-you-offer-pay-what-you-want)). Implication: PWYW works for CiC only as a *support* lane with a suggested amount and a mission frame, not as the pricing of the product itself.
- **Hallow's pattern** (faith-adjacent, subscription, but the framing transfers): a public "why we charge" explanation, a large permanently-free core, free access for clergy, a scholarship request path, and give-one-get-one ([Hallow blog, via search summary](https://hallow.com/blog/why-do-we-charge-for-hallow-plus/); [Contrary Research](https://research.contrary.com/company/hallow)). YouVersion is the opposite pole: fully free, ~40,000 donors, no gating ([growthcasestudies](https://growthcasestudies.com/p/youversion)). CiC's "Family Tree always free, conversations paid" sits between them and can borrow Hallow's explanatory honesty with YouVersion's "the core is a gift" posture.

### 2.4 Recommendation for (b)

Consumable packs as primary, with four durability features non-negotiable: no expiry, account-bound balance, failed-reply protection, and a separate suggested-amount support lane. Expect low repeat rates by default and design the *product* (new worlds, Tables) to generate the second purchase. Confidence: moderate. What is uncertain: whether a scholarly, reflective product's repeat-purchase curve looks like games (bad) or like Audible (good); only CiC's own first-quarter data will say. Keep a flat-rate option (e.g., an "unlimited for 30 days" one-time pass, no auto-renew) in reserve for heavy users, because flat-rate bias is real and some participants will want to stop counting.

---

## 3. Question (c): free-tier design

### 3.1 How much free is typical

- Big AI chat products give a real, repeated free allowance (ChatGPT ~10 msgs/5h; Character.AI tens of messages/day; Gemini compute window) because their free tier is a funnel for a subscription and a data/brand asset. Their free tiers *degrade* (older model, queue, ads) more than they *block*.
- Signed-out allowances are tiny: ChatGPT ~3–5 messages before a sign-up wall ([meetaitools](https://meetaitools.com/can-you-use-chatgpt-for-free-without-account/)). Perplexity: unlimited cheap searches, 3–5 expensive ones.
- Publishers converged on **2–5 free units per month**; the average visitor consumes 1–1.5 articles, so a meter at 3+ is invisible to most and only bites engaged readers ([ultracommerce](https://ultracommerce.co/resources/blog/metered-paywall-vs-freemium-which-publishing-model-is-right-for-you); [NiemanLab on NYT 10→5](https://www.niemanlab.org/2017/12/the-new-york-times-has-halved-its-free-monthly-articles-to-5-its-most-significant-paywall-change-since-2012/)). The NYT tightened from 20 to 10 to 5 over six years as subscriptions grew, which is the usual direction: start generous, tighten with data.

### 3.2 "Aha moment before the wall"

- Value-triggered paywalls (shown right after the aha) are reported to convert 3–5x better than time-based ones; onboarding that demonstrates value before the wall converts 40–60% better than wall-on-launch ([RevenueCat paywall placement](https://www.revenuecat.com/blog/growth/paywall-placement); [Superwall](https://superwall.com/blog/superwall-best-practices-winning-paywall-strategies-and-experiments-to); [Airbridge](https://www.airbridge.io/en/blog/5-steps-app-onboarding-before-the-paywall)). Aggregator figures; direction is well-established, magnitudes vary.
- For CiC the aha is unambiguous: the moment a Representative answers a real question in its own voice and the participant realizes it is not a generic chatbot. That takes a *whole* short conversation, not three messages. So the free allowance must be measured in conversations and must let at least one complete.

### 3.3 Anonymous vs signed-in

- **Anonymous (no account):** cookie + IP rate limiting stops casual abuse but is "trivially cleared"; fingerprinting is more persistent but raises privacy questions; none stops a motivated abuser ([dev.to rate-limiting](https://dev.to/dmitryvz/rate-limiting-anonymous-users-with-no-login-no-redis-just-a-cookie-and-an-ip-3k5e); [cside](https://cside.com/blog/account-sharing-prevention-gdpr-cookieless)). Anonymous allowances should therefore be small enough that abuse is not worth the effort, not zero.
- **Email gating costs real users.** Signup flows lose 60–80% of starters; 38% drop at the first screen; magic-link completion (70–85%) beats email+password (35–55%) ([signupdrop](https://signupdrop.com/); [clapback](https://clapback.run/blog/why-users-abandon-signup)). Baymard: 19% of abandoners cite forced account creation ([userpilot](https://userpilot.com/blog/saas-signup-flow/)).
- **But registration is where conversion happens.** Piano: registered users convert ~10x anonymous ([Twipe](https://www.twipemobile.com/developing-paywall-strategy-acquisition-retention/)). And any paid balance *must* be account-bound to be portable and refundable.

### 3.4 Recommendation for (c)

Two-stage free tier:

1. **Signed out:** one complete conversation per device per rolling 7 days (cookie + IP + lightweight fingerprint; accept leakage). Enough to hit the aha; small enough that cookie-clearing is more work than signing up.
2. **Signed in (magic link, no password):** a one-time welcome allowance of ~3 conversations, plus a small recurring free allowance (e.g., 1 per month) so lapsed users have a reason to return without paying. Make the signed-in free allowance *visibly* better than anonymous so sign-up is a gain, not a toll.

Build a Table (multi-Representative) is more expensive per session; treat the first Table as part of the welcome allowance but not the anonymous one.

Confidence: moderate. Uncertain: the right rolling period and whether 3 is too generous; tighten with data, as NYT did, rather than start stingy.

---

## 4. Question (d): the moment the free allowance ends

### 4.1 Evidence on timing, tone, and shape

- **Soft (dismissible) vs hard wall.** Per-download, hard walls convert more (10.7% vs 2.1% in one dataset) and produce ~21% higher LTV; per-view, soft walls convert ~50% better and users "feel less trapped" ([neoads](https://neoads.substack.com/p/hard-paywalls-convert-less-but-earn); [abtest.design](https://abtest.design/tests/hard-vs-soft-paywall); [dev.to](https://dev.to/paywallpro/hard-paywall-vs-soft-paywall-which-yields-higher-conversion-rates-bg6)). Those hard-wall numbers come from subscription apps with trials; for a mission-driven product whose Family Tree is free and whose brand depends on not feeling like a trap, a soft wall is the right default. "Hard" here would only mean: no more conversations without paying — the rest of the site stays open.
- **Interrupt mid-answer or after?** No product surveyed cuts a reply mid-stream to upsell; ChatGPT downgrades the model, Character.AI queues, voice mode warns at 3 minutes and then ends the *session*. Cutting a Representative mid-sentence would be a fidelity defect as well as a UX one. The wall belongs at the *start of the next conversation* (or, for in-conversation caps, at the natural end with a gentle "this conversation is complete" close).
- **Showing what is preserved.** Streaming-resume guidance and the Audible return model both point to: tell the participant their conversation is saved and resumable, and that nothing paid was consumed by an error. Make this a line on the wall itself.
- **Pack choice architecture.** Three tiers with a middle anchor is the most-cited structure (middle-tier lift of +20–40% claimed; AOV +15–25%) ([impactanalytics decoy](https://www.impactanalytics.ai/blog/decoy-pricing); [smartsms](https://smartsmssolutions.com/resources/blog/business/bundle-pricing-psychology)). These are practitioner numbers, not peer-reviewed; the direction is well supported by the decoy-effect literature. Price in dollars per conversation shown next to each pack ("5 conversations — $X, that's $Y each") to satisfy the transparency principle.
- **"Maybe later" paths.** Dismissable with a plain "Not now"; dismissed users should see the free allowance refresh date. Do not use a discount-on-dismiss sequence.
- **Pay-what-you-want / donation.** Keep it as a separate, always-visible "Support this work" lane with a suggested amount and a mission framing (Gneezy: the charity frame is what made PWYW both popular and profitable). Do not make the conversation price itself PWYW (Gumroad: −65% average price without anchoring).
- **Wikipedia's banner lesson:** >75% of donors give on the first or second impression; after the 10th impression conversion is negligible, so Wikimedia now caps banner frequency ([Wikimedia Diff](https://diff.wikimedia.org/2017/10/03/fundraising-banner-limit/); [2023-24 report](https://meta.wikimedia.org/wiki/Fundraising/2023-24_Report)). Translate: show the support ask rarely and well, not on every page.

### 4.2 Dark patterns to avoid and the legal frame

- **FTC "Bringing Dark Patterns to Light" (Sept 2022)** catalogs: drip pricing (unavoidable fees revealed late; shown to raise spend ~20% and completion ~14% in one study — which is precisely why it is deceptive), confirmshaming ("No thanks, I don't want to learn"), false urgency/countdowns, pre-checked boxes, obstructed cancellation, disguised ads, and "trick questions." Firms using them "will face enforcement action" ([FTC report PDF](https://www.ftc.gov/system/files/ftc_gov/pdf/P214800+Dark+Patterns+Report+9.14.2022+-+FINAL.pdf); [Arnold & Porter](https://www.arnoldporter.com/en/perspectives/advisories/2022/09/ftc-shines-a-little-light-on-dark-patterns)). The Amazon Prime and Publishers Clearing House cases (2023) are the enforcement precedents ([WilmerHale](https://www.wilmerhale.com/en/insights/client-alerts/20230814-ftc-targets-dark-patterns-in-actions-against-amazon-and-publishers-clearing-house)).
- **Subscriptions specifically:** the FTC's expanded Click-to-Cancel rule was vacated by the Eighth Circuit (8 July 2025) on procedural grounds; the FTC restarted rulemaking (ANPRM, March 2026); ROSCA and state auto-renewal laws still apply ([Latham](https://www.lw.com/en/insights/eighth-circuit-vacates-ftc-click-to-cancel-rule-days-before-compliance-deadline); [Gibson Dunn](https://www.gibsondunn.com/ftc-restarts-negative-option-rulemaking-after-eighth-circuit-vacatur-enforcement-under-rosca-continues/); [Jones Day May 2026](https://www.jonesday.com/en/insights/2026/05/ftc-revives-clicktocancel-rule-new-risks-for-subscription-businesses)). **A one-time pack model is outside all of this** — a genuine compliance advantage of Mark's preference.
- **Stored value / expiry:** California no-expiry rule; *Hollis v. Audible* (Washington) shows courts may read "credits" as gift certificates. Non-expiring packs avoid the question.
- **EU (if ever relevant):** CPC virtual-currency principles (price in real money; let users buy the exact amount; no forced bundles), and the DFA may bring a 14-day withdrawal right on unused credits.
- **Faith-adjacent specifics (judgment, not law):** avoid any copy that links payment to spiritual standing, implies the free participant is less serious, or uses the Representatives' voices to sell. The wall speaks in the Facilitator's register (outside every world) — never in a world's voice. Guilt-framed buttons would be confirmshaming in the FTC's sense *and* a violation of CiC's own "no AI tells / no manipulation" bar.

### 4.3 Recommended wall (concrete shape)

Shown as a sheet at the start of the next conversation attempt once the free allowance is used, never mid-reply:

1. One-line status: "You've used your free conversations for this week. Your past conversations are saved."
2. One-line reason (cost-structure appeal, dual-entitlement): "Each conversation runs on real compute and on years of source work. Paying for one keeps the Family Tree free for everyone."
3. Three packs, dollars and per-conversation price shown, middle pack visually anchored, no decoy that is actually a bad deal. Example structure only (prices deliberately not proposed here): small / medium (anchor) / large, with per-conversation price falling across the row.
4. A line of guarantees in plain words: "Conversations never expire. If a reply fails, you don't lose one. You can always come back to an unfinished conversation."
5. "Not now" (plain). Below it, in smaller type: when the free allowance refreshes, and a quiet "Support the project" link with a suggested amount.
6. No countdown, no "limited offer," no pre-selected pack, no discount-on-dismiss.

Confidence on the shape: moderate-high (it is the intersection of the FTC list, the soft-wall data, and the fairness literature). Uncertain: exact pack sizes and prices (Track 2 territory), and whether a 30-day unlimited pass should be a fourth option or held back.

---

## 5. Consolidated recommendation, confidence, and what to test first

| Decision | Recommendation | Confidence | Main uncertainty |
|---|---|---|---|
| Unit of access | Whole conversations, dollar-priced; internal turn/token cap set above the 90th–95th percentile of natural length | Moderate-high | Where that percentile actually falls for CiC |
| When spent | On first successful Representative reply | High | — |
| Accidental exit | Never loses the unit; resumable for ≥7 days; failed replies never deduct | High | Cost of long-lived open threads (expected negligible) |
| Expiry | Never, for purchased conversations | High | None material; also the legally safer choice |
| Model | One-time packs primary; separate suggested-amount support lane; optional one-time 30-day pass in reserve | Moderate | Repeat-purchase rate for a reflective product is unknown |
| Free, signed-out | 1 complete conversation / device / rolling 7 days | Moderate | Abuse rate; adjust with data |
| Free, signed-in | ~3 welcome conversations + ~1/month, magic-link signup | Moderate | Generosity; tighten with data like NYT |
| Wall | Soft, between conversations, 3 packs with middle anchor, dollar transparency, plain "Not now," no urgency/guilt | Moderate-high | Exact pack sizes/prices |

**What to test first (in order):** (1) the internal cap, by logging natural conversation length in the pilot; (2) anonymous vs signed-in allowance sizes, against sign-up completion; (3) whether a "short conversation is free" rule changes behavior; (4) the three pack sizes.

**What this report deliberately does not do:** propose prices or pack sizes, model revenue, or assume anything about CiC's cost per conversation. Those belong to the pricing track and should be built from CiC's own compute and traffic numbers.

---

## Appendix: full source list (accessed 2026-10-02)

AI product limits: Northflank; freeacademy.ai; chatai.guide; How-To Geek; meetaitools; Neowin; precallai; datastudios (Claude, Grok); Android Police; Tom's Guide; finout; felloai; eesel (Character.AI, Replika, Midjourney, Runway); roborhythms; aicompanionpick; aisotools; Poe help center and Terms of Sale; usagepricing (Pi); duoplanet; Android Authority; toptechguides; khanmigo.ai; Cambly help center; uxmagic; gladreaders; readiolist.

Consumables and benchmarks: RevenueCat State of Subscription Apps 2025/2026 (via Subscription Insider, arpubrothers, 9to5Mac, RevenueCat blog); wifitalents; Mistplay via gamedevreports; virtwave; Adweek; hubifi; Deloitte DART; artisangrowthstrategies; firstpagesage; Twipe (Piano); ultracommerce; NiemanLab.

Fairness and pricing psychology: Lambrecht & Skiera 2006 (JMR); Slate (taxi-meter); Kahneman, Knetsch & Thaler 1986; Xia, Monroe & Cox 2004; Stangl, Kastner & Natter 2026 (JSR); Gneezy et al. (PNAS; Wikipedia summary); insightraider (Gumroad PWYW); impactanalytics; smartsmssolutions; Wikimedia Diff and Fundraising reports.

Refund/failure handling: Runway help center (via summary); techsifted; codeables (ElevenLabs); OpenAI help center; Trustpilot (Suno); Adobe community; Vercel AI SDK docs; openclaw issue; zknill.

Paywall evidence: RevenueCat paywall placement; Superwall; Airbridge; neoads; abtest.design; dev.to (paywallpro); NN/g accidental overlay dismissal.

Law and regulation: FTC "Bringing Dark Patterns to Light" (2022); Arnold & Porter; WilmerHale; Latham & Watkins; Gibson Dunn; Jones Day; Justia (*Hollis v. Audible*); Courthouse News; California DCA / Civil Code 1749.5 coverage; Linklaters (CPC principles); European Commission CPC page; Freshfields (DFA); Apple WWDC21 refunds; hubifi (App Store Connect); subpilot (Google Play).

Faith-app comparators: Hallow blog and help center (via summary); Contrary Research; growthcasestudies (YouVersion); Christianity Today.
