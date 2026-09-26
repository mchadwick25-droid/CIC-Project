# Market Analysis — Contribution Conversion, Amounts, and Tier Benchmarks

**2026-07-22 · Funding Strategy thread · Opus agent, background dispatch, deep research**

**Status: research to react to, not a decision.** Prepared for Mark and Susan. Real data,
cited throughout, confidence-labeled with this project's own taxonomy (Documented / Widely
Accepted / Contested / Inferential-Thin). The synthesis at the end is explicitly a
recommendation to react to in the Groan-Zone sense — nothing here converges until Mark and
Susan say so.

---

## The single most important framing note before any number

**Every "conversion rate" below depends entirely on its denominator, and the denominators are not comparable to each other.** "2% convert" can mean 2% of *everyone who ever opened the app*, or 2% of *people who started a free trial*, or 16% of *people who already reached a donation page having decided to give*. These differ by more than 10x. Every figure below is labeled with its denominator, because for CiC's cost projections, the denominator matters more than the percentage. The headline finding of the whole report: **the realistic "what % of my free audience pays anything" number lives in the low single digits when the denominator is your whole free base — and the more generous figures you'll see quoted elsewhere are almost always measured against a much narrower, already-committed denominator.**

---

## Question 1 — What percentage of a free/engaged audience actually converts to paying/contributing anything

### Freemium apps generally (the broad industry floor)

- **Freemium free-to-paid conversion sits around 2–3% of installs.** RevenueCat's *State of Subscription Apps* data puts freemium at **~2.1% download-to-paid by day 35**; Adapty independently puts freemium at **~2.6%**. [Documented — RevenueCat; Adapty] Denominator: everyone who installed the app.
- **A hard paywall (must-pay-to-use) converts ~5x better — ~10.7% — but that is a fundamentally different model** (no real free tier), so it is *not* a comparable for CiC's "the free tier is the full product" design. [Documented — RevenueCat]
- **"Trial-to-paid" figures of 40–49% are real but measure a different, much narrower denominator** — people who already opted into a free trial (often card-required). RevenueCat's Media & Entertainment trial-to-paid median is ~43.8%; Health & Fitness ~39.9%. [Documented — RevenueCat] **Do not use these as your free-base conversion number** — they describe an already-committed sub-audience, not the whole funnel.

### Faith / meditation / wellness apps specifically

- **Calm is the cleanest documented case: it raised paying conversion from ~2% to ~7% of users — by deliberately gutting the free tier** (free content dropped from ~90% of the library to ~5%). [Documented — Sacra] Denominator: total users (free + paid). This is directly relevant: the 7% was *bought* by making free much worse — the opposite of CiC's "free tier is the full product, bounded only by time" commitment, which structurally points you toward the ~2% end, not the 7% end.
- **Calm: ~3.5–4M+ paying subscribers against ~140M lifetime downloads** (~2.5% lifetime download-to-paid); **Headspace: ~2M paid against ~85M downloads** (~2.4% lifetime). [Widely Accepted — Business of Apps, Sacra] These lifetime ratios independently corroborate the low-single-digit floor.
- **Hallow (the closest faith comparable) does not publicly disclose its conversion rate.** [Documented — absence] Not public; not guessed.

### Reader-supported / voluntary-giving media (the closest structural analog to CiC)

- **The Guardian: ~1.3M recurring supporters + subscribers globally** (up ~13% YoY as of March 2025), against a global reach historically cited at **~113M monthly unique browsers**. [Documented — Press Gazette / Nieman for supporters; Statista/PAMCo for reach] That is **roughly 1% of monthly reach**, and lower against annual unique readers. [Inferential-Thin — arithmetic across two differently-dated figures; order-of-magnitude, not a precise rate] The Guardian's model — stays free, ask comes after value lands — is CiC's single best structural mirror, and it lands around **1% of broad reach**.
- **NPR / public radio: ~6–12% of listeners donate, commonly cited around ~10%.** [Widely Accepted — Current.org, citing a Greater Public multi-station survey] **Critical denominator distinction:** this is a percentage of *loyal listeners* (people who tune in repeatedly), not of everyone who ever heard the station once. Against an *engaged* denominator, ~10% is the realistic ceiling for a beloved, decades-trusted brand.
- **Wikimedia — the "2%" figure, verified:** The **"Only 2% of readers give"** language is **real and appears in Wikipedia's own 2022 fundraising banner copy** [Documented — Wikipedia:Fundraising/2022 banners]. **But it is banner marketing, not a measured visitor-to-donor rate.** The arithmetic tension: Wikimedia reports **8M+ donors** in FY23-24 against a reader base of **well over a billion annual uniques** — which implies a *true* visitor-to-donor conversion well **under 1%** (closer to ~0.5%). [Inferential-Thin / Contested — the banner says 2% of "readers"; the donor-count-over-reader-count math says <1%] **The load-bearing takeaway for CiC's cost projections: the "2%" is defensible only as a rounded, aspirational figure against a soft "readers who notice the ask" denominator — the true whole-audience rate is lower.** The genuinely robust, well-documented Wikimedia finding is the *timing* one already anchored in this thread: **75%+ of donors give on their first or second banner exposure, and conversion collapses after ~10 impressions** [Documented — diff.wikimedia.org] — the ask has to land early or it doesn't land.

### Patron / creator platforms

- **Patreon rule-of-thumb: 1–5% of a creator's broad free audience converts to paying patrons.** [Widely Accepted] Denominator: total followers/audience.
- **Engaged niche communities convert far higher: 7–20% (median ~13%) on Royal Road**, a web-serial platform with tight, invested audiences. [Documented — Chapter Chronicles / Royal Road community analysis] This is the "engaged denominator" premium in action, and it's the most hopeful real signal for a mission-committed audience like CiC's.
- **Substack: ~3% median free-to-paid, with 2–5% typical and niche/specialized publications reaching 4–10%.** [Widely Accepted; Substack's own "aim for 5–10%" guidance is aspirational, and only ~1 in 5 publications actually clears 5%]
- **Twitch / Ko-fi: no reliable public whole-audience conversion rate exists.** [Documented — absence]

**Q1 bottom line:** Against a *whole free base*, real comparable models cluster at **~1–3%** (freemium ~2%, Wikipedia <1–2%, Guardian ~1%, Substack ~3%). Against an *engaged/loyal* denominator, the ceiling rises to **~7–13%** (Calm-after-gutting-free 7%, NPR loyal ~10%, Royal Road ~13%).

---

## Question 2 — How much people actually contribute

**The distribution is right-skewed (lognormal) in every giving model — mean > median, and a small number of large gifts pull the average up.** [Widely Accepted] **Practical consequence: use the median to set expectations for a typical contributor, but model revenue off the mean, and expect a minority of supporters to generate a disproportionate share of total dollars.**

**One-time voluntary gifts:**
- **Wikimedia average donation: $10.05 (FY23-24), down from $11.38 the prior year.** [Documented — Wikimedia Fundraising Report] A *mean*; the median is almost certainly lower given the right-skew. Best real anchor for a small, mass-audience, one-time "keep it open" gift.
- **Nonprofit online average gift is much higher — $137 desktop / $83 mobile (M+R Benchmarks)** [Documented] — but that denominator is *people who already decided to give and reached a donation page*, a self-selected, higher-intent, often older-donor population. Not comparable to a casual in-product gesture.

**Recurring / subscription contributions:**
- **Patreon average: ~$6/month per patron** (rose from $5.40 to $6.10 across 2025). [Documented] Typical tiers: base $3–5, mid $7–12, premium $20–30. [Widely Accepted]
- **Public radio sustainers: ~$10–25/month, averaging ~$14/month;** new-member one-time average ~$75, renewing members ~$120/year (~$10/month). [Widely Accepted]
- **The Guardian: entry contribution £4/month (~$5) with no added benefits;** digital subscription £12/month; premium (print+digital) £27/month. Revenue mix ~80% recurring / 20% one-time, but *acts of support* are 68% one-time / 32% recurring — **most individual acts are one-time even though recurring dominates the money.** [Documented]
- **BibleProject: tens of thousands of patrons averaging ~$20/month, 100% crowdfunded** — the high end of the recurring band, achieved with *no* exclusive benefits, pure "keep it free for everyone." [Documented]

**Q2 bottom line:** A realistic *one-time* voluntary gift centers around **~$10** (Wikimedia's real-world mean). A realistic *recurring* voluntary supporter sits in the **~$6–20/month** band, with $8–14/month being the dense middle across NPR, Patreon, and Guardian-style models.

---

## Question 3 — What people actually get for different contribution levels

| Model | Free tier | Paid entry | Higher / family / pro | What the paid tier actually buys |
|---|---|---|---|---|
| **Hallow** (faith) | Hundreds of free sessions, essentials | $9.99/mo or $69.99/yr | Family $119.99/yr (6 seats); student $2.50/mo; schools 80% off; "gift a subscription" mechanic | Full library, prayer challenges, daily content, sleep content, music, audiobooks |
| **Calm** | Daily Calm + limited library | $14.99/mo or $69.99/yr | (periodic lifetime deals) | Full meditation/sleep library, Sleep Stories, masterclasses |
| **Headspace** | Thin free tier, foundational courses | $12.99/mo or $69.99/yr | — | Full structured courses, sleep, focus music, animations |
| **NPR+** (public media) | All core content free forever | $8/month threshold unlocks NPR+ | Higher sustainer levels | Sponsor-free podcasts, bonus episodes, early/archive access, member discounts |
| **Patreon** (creator) | Public posts | ~$3–5/mo base | Mid $7–12, premium $20–30 | Early/exclusive content, community access, behind-the-scenes; higher tiers = more access + recognition |
| **Substack** (newsletter) | Free posts | $5/mo floor, $50/yr default | Founding $100–500/yr | Paid-only posts/archive; founding tier is *same content* + recognition/insider perks |
| **The Guardian** (reader-support) | Entire product free | £4/mo (no benefits) | £12/mo ad-free+app; £27/mo +print | Content stays free at every level; paying mostly buys ad-removal + the feeling of sustaining it |

**Two patterns highly relevant to CiC's planned structure:**
1. **The "same content, higher tier = recognition/insider status" model** (Substack founding, Patreon, Guardian, BibleProject) proves people *will* pay more without getting more *content* — they pay to sustain the thing and to be seen sustaining it. This directly validates CiC's "keep it open for others" gesture as a real, proven revenue mechanic, not wishful thinking. [Widely Accepted]
2. **Role/professional tooling is a legitimate premium-tier justification.** Across the market, higher paid tiers that bundle *tools* (not just more content) reliably command higher prices than consumer content tiers. CiC's planned role-tailored tier (discussion guides, citation export, cross-tradition research tool, lesson plans) is the kind of *utility* bundle that comparables price *above* their base content subscription. [Inferential-Thin — reasoned from the general prosumer-tier pattern; no single source prices exactly CiC's feature set, since it's unusual for this category]

---

## Synthesis — a recommendation to react to, not a decision

**This is the convergent-sounding part, but it is still Groan-Zone material.** Read it as "here's what the real data would suggest if we stopped here" — and then push back on it. Nothing below is settled until Mark and Susan say it is.

**(a) Realistic range for what % of CiC's free users might ever contribute anything.** The honest, defensible planning range is **2–6% of the total free base** contributing anything (a subscription *or* a one-time "keep it open" gesture), anchored at the **conservative ~2%** end for cost projections. That 2% triangulates from three independent real sources — freemium industry (~2.1%), Wikipedia's stated reader-give rate, and Calm's *pre-gutting* conversion (2%). **Push-back to consider:** CiC's audience is mission-committed and mirrors the highest-converting *engaged*-denominator cases (NPR loyal ~10%, Royal Road ~13%). If an "engaged user" (returned N times, invested real time) can be defined and measured, the rate *among that subset* could plausibly reach **7–13%** — but only among the engaged subset, never the whole base. Open strategic question: should cost projections run against the whole free base (use 2%) or against engaged users (use ~10%)? These are different businesses.

**(b) Realistic average contribution amount.** A one-time voluntary gift realistically centers on **~$10** (Wikimedia's actual mean), and a recurring supporter realistically sits at **~$8–14/month**. Because the distribution is right-skewed, expect a **minority of larger contributors to carry a disproportionate share of total dollars** — model total revenue on the mean, but don't expect the *typical* contributor to hit it.

**(c) Is $10 one-time / $8-month recurring well-calibrated? On the current evidence, yes — strikingly so.**
- **$10 one-time lands almost exactly on Wikimedia's real average donation ($10.05).** For a small, post-value, mass-audience voluntary gift, this is as well-anchored as a number can be.
- **$8/month recurring is well-placed, and carries an interesting precedent: NPR+ uses exactly $8/month as its benefit threshold** — and at that price NPR gives sponsor-free podcasts and bonus episodes. So $8/mo sits in the dense middle of the voluntary-support band (Patreon ~$6, public-radio entry ~$10, Guardian ~$5, Substack floor $5, BibleProject ~$20), *below* meditation-app premium ($10–15), and right where a trusted mission brand can credibly ask. **The one thing to weigh:** NPR attaches real perks at $8/mo, whereas CiC's $8/mo "keep it open" gesture is deliberately benefit-free by design (the anti-tipping-culture stance). That's a defensible and even distinctive choice — BibleProject proves benefit-free recurring giving works at scale — but it's worth naming explicitly: this is pricing at the "gets you something" market rate while intentionally offering nothing, on purpose, not by oversight.

**On the tier structure overall:** free-tier-is-the-full-product + a paid subscription (~$8–12/mo in line with Hallow's $9.99 and the market) + a role-tailored professional tier (priced *above* base, justified by tooling, as the prosumer market supports) + unlimited + institutional per-seat — **is a structurally conventional, market-aligned ladder.** The only genuinely *unusual* element is keeping the full product free forever, bounded only by time. The data both warns and reassures on this: it warns that never degrading free is exactly what caps whole-base conversion near ~2% (Calm bought its 7% by degrading free), and it reassures that the reader-support models most like this choice (Guardian, Wikipedia, BibleProject) sustain themselves anyway — on high reach × low conversion × right-skewed generosity, not on a high conversion rate. **The strategic tension worth sitting in: the free-tier commitment and a high conversion rate are, on this evidence, partly in tension — and the resolution the comparables model is "and," not "or": keep free whole AND build for the reach and the right-skewed large-giver tail that make ~2% enough.**

---

## Sources

- RevenueCat, State of Subscription Apps — https://www.revenuecat.com/state-of-subscription-apps-2025 · https://www.revenuecat.com/blog/growth/subscription-app-trends-benchmarks-2026/
- Adapty freemium benchmarks — https://adapty.io/blog/freemium-app-monetization-strategies/
- Sacra, Calm — https://sacra.com/c/calm/
- Business of Apps, Calm / Headspace — https://www.businessofapps.com/data/calm-statistics/ · https://www.businessofapps.com/data/headspace-statistics/
- Calm vs Headspace features/pricing — https://www.themindfulnessapp.com/articles/best-meditation-apps-features-comparison-2025
- Hallow pricing/tiers — https://help.hallow.com/en/articles/2880438-how-much-does-the-subscription-cost · student: https://www.studentbeans.com/student-discount/us/hallow · schools: https://hallow.com/hallow-for-schools/
- The Guardian reader revenue — https://pressgazette.co.uk/media_business/guardian-reports-bumper-year-for-digital-reader-revenue/ · https://www.niemanlab.org/2024/05/the-way-we-raise-the-money-at-the-guardian-is-different-than-any-place-ive-ever-been/ · reach: https://media-studies.com/the-guardian-study-guide/
- NPR / public radio — donor share: https://current.org/1998/08/how-many-listeners-donate-one-in-12-or-one-in-three/ · sustainer amounts: https://current.org/2015/02/sustainer-programs-are-growing-but-still-show-room-for-improvement/ · NPR+ benefits: https://www.wshu.org/nprplus · https://donate.plus.npr.org/
- Wikimedia — banner "2%": https://en.wikipedia.org/wiki/Wikipedia:Fundraising/2022_banners · banner-frequency/75%: https://diff.wikimedia.org/2017/10/03/fundraising-banner-limit/ · avg donation & donor count: https://meta.wikimedia.org/wiki/Fundraising/2023-24_Report
- Patreon — conversion rule-of-thumb: https://www.royalroad.com/forums/thread/138022 · Royal Road engaged rates: https://www.chapterchronicles.com/blog/royal-road-patreon-2025/ · avg pledge/tiers: https://bloggingwizard.com/patreon-statistics/ · https://electroiq.com/stats/patreon-statistics/
- Substack — conversion: https://www.reallygoodbusinessideas.com/p/substack-average-paid-subscriber-conversion-rate · pricing/tiers: https://www.ruzuku.com/learn/articles/substack-pricing
- M+R Benchmarks (nonprofit online giving) — https://2024.mrbenchmarks.com/
- Donation right-skew / median vs mean — https://arxiv.org/pdf/1307.2278 · https://statisticsbyjim.com/basics/skewed-distribution/
- Ko-fi fee structure — https://ko-fi.com/

**Coverage gaps not closed with real public data (stated plainly rather than filled with invented numbers):** Hallow's actual conversion rate, Twitch/Ko-fi whole-audience conversion rates, and Substack's cross-tier price distribution are not publicly disclosed. The Guardian participation rate (~1%) and the "true" Wikipedia visitor-to-donor rate (<1%) are arithmetic across differently-dated figures, not single-source facts — labeled Inferential-Thin above.
