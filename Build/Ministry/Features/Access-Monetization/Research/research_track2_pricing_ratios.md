# Track 2 — Cost Structure and Price-Point Analysis for Pay-As-You-Go AI Conversation Products

Prepared for: Church in Conversation (Faithways Studio, Inc.) funding thread
Date: 2026-10-02
Scope: objective, web-sourced. No internal CiC figures were used. All per-conversation API costs below ($0.20 / $0.50 / $1.00) are **illustrative placeholders, not CiC data**.
Research note: the sandbox egress proxy blocked direct fetches of stripe.com, docs.stripe.com, support.stripe.com, chargebee.com, tanayj.com, lyft.com and usagepricing.com. Figures from those sources were taken from search-engine summaries and from secondary pages that quote them; they are flagged below where that matters.

Evidence-quality key used throughout:
- **[H]** hard data — public filings, vendor price pages, peer-reviewed or large-N studies
- **[M]** medium — analyst/VC survey reports (ICONIQ, Bessemer, a16z, RevenueCat), reputable journalism
- **[L]** low — blog opinion, vendor marketing, single-case anecdote

---

## 1. Executive summary

1. **LLM-app gross margins are structurally lower than SaaS.** Benchmarks cluster at **50–60% gross margin** for AI-native apps (ICONIQ 2026 average 52%; Bessemer "Shooting Stars" ~60%, "Supernovas" ~25%; a16z 50–60% "more often" with a few at 90%). Pure resellers of someone else's model report ~45%. Several famous products run at or below zero on flat subscriptions (GitHub Copilot −$20/user/month in 2023; ChatGPT Pro losing money per Altman, Jan 2025; Cursor reportedly −21%). [M]
2. **The reason is flat pricing meeting variable cost.** Every one of those loss cases is a *subscription* where heavy users consume far more than the fee covers. **Pay-as-you-go removes that failure mode by construction** — the heavy user pays for what they use. This is the single strongest argument for CiC's PAYG-as-primary-engine design, and it is well supported.
3. **Payments are the second-largest variable cost and they punish small tickets.** Stripe US: 2.9% + $0.30 per card charge; +1.5% international cards; +1% currency conversion; $15 non-refundable dispute fee (+$15 to contest, refunded only if you win); processing fees are **not** returned on refunds; $0.50 minimum charge. Stripe Tax adds 0.5% (no-code) or $0.50/transaction (API) in registered jurisdictions. A merchant-of-record (Paddle / Lemon Squeezy) costs 5% + $0.50 but absorbs sales-tax/VAT compliance. [H]
4. **Minimum economic pack size: $5 absolute floor, $10 practical floor, $10–$25 sweet spot for the entry tier.** At $1 the Stripe fee is 33% of revenue; at $5 it is 8.9%; at $10, 5.9%; at $20, 4.4%; at $50, 3.5%. [H, arithmetic from published rates]
5. **Markup needed:** at an all-in non-API cost load of ~12–15% of revenue (payments on a $20 pack ≈ 4.4%, hosting/infra 2–4%, support + trust & safety 4–8%, refunds/disputes/fraud ~1%), a **5× markup over direct API cost yields ~65–68% contribution margin**, 3× yields ~52–55%, 8× ~75%, 10× ~78%. Below 3× you fall under the AI-industry median and have no room for a free tier. Section 6 has the full sensitivity table.
6. **Observed ladders:** three tiers is the dominant pattern; consumable price anchors are $4.99 / $9.99 / $19.99 / $49.99; volume bonuses of 10–25% on larger packs (up to 40% at the very top) are the norm; a "best value" badge on the middle or upper-middle tier is near-universal. Top-ups in AI products: OpenAI API minimum $5, Runway $10 per 1,000 credits, Poe $30 per 1M points (1-year expiry). [H for price points; M for the bonus ranges; L for most "psychology" claims]
7. **Durability levers with evidence behind them:** prepaid wallet + opt-in auto-reload (industry standard, converts PAYG into quasi-recurring revenue), gift packs, group/church bulk tiers (RightNow Media's attendance-tiered site licence is the direct analogue, ~$1,200–$5,000/yr), and a round-up/add-$1 donation at checkout (22–24% median opt-in, Lyft average donation $0.38, 100M+ donations). [M–H]
8. **Build a Table (multi-representative): price it as a separate SKU with an explicit credit multiplier, label it early-access, keep it out of bonus/PWYW mechanics until its cost is measured.** This is what Cursor (Max mode 5–20× credits), Midjourney (video ≈ 8× image GPU time), and Sora (credits scale 4→16→40 per second by resolution) all do. [H for the multipliers]

**Recommendation (confidence: moderate-high on structure, low on exact prices until real cost data lands):** Structure B below — a three-pack conversation ladder sold into a prepaid wallet, with opt-in auto-reload, gift packs, a church/group tier, and a donation add-on, with Build a Table as a separately-multiplied SKU. Target ≥5× markup over measured direct API cost per conversation, and never let the entry pack fall below $10.

---

## 2. (a) Gross-margin structure of LLM-API consumer apps

### 2.1 The benchmarks

| Source | Figure | What it covers | Quality |
|---|---|---|---|
| a16z, "The New Business of AI" (2020, still the reference piece) | Gross margins "more often as low as 50–60%", "as high as 90% in a few cases", driven by inference cost; AI "does not have the economies of scale of traditional software" | AI app companies broadly | [M] |
| ICONIQ, State of AI 2025 / Jan-2026 snapshot (via SaaStr and secondary summaries) | Average AI product gross margin **52%** (2026), up from 41% (2024) and 45% (2025). Inference ≈ **23% of revenue** at scaling stage; inference share *rises* with scale (20%→23%) while talent share falls | 300+ high-growth B2B software cos; AI-native vs AI-enabled | [M] |
| Bessemer, State of AI 2025 | "Supernovas" (hyper-growth) ≈ **25%** GM; "Shooting Stars" ≈ **60%** GM; AI cos generally 50–60% vs 80–90% SaaS | VC portfolio + market | [M] |
| Tanay Jaipuria, "The State of AI Gross Margins in 2025" (via secondary quotes) | OpenAI ~50%, Anthropic ~60%; app-layer "high end in the 60s, low end negative"; pure resellers of a third-party model ~45%; model+product combined ~53%; Cursor reportedly −21% | Stack-wide | [M] |
| WSJ (Oct 2023) on GitHub Copilot | $10/mo product lost avg **$20/user/month**; some users cost **$80/month** | Single large product | [M–H] |
| Sam Altman (Jan 2025), reported by TechCrunch and others | ChatGPT Pro at $200/mo "losing money" because "people use it much more than we expected" | Single product | [H — primary statement] |
| Anthropic (Jul 2025, TechCrunch) | Weekly rate limits introduced to curb <5% of Max-plan users running Claude Code "continuously … 24/7" | Single product | [H] |

**Reading across these:** the consensus that AI gross margins sit at 50–60% is strong and repeated by every major source. The dispersion matters more than the mean: the losses are concentrated in **flat-fee plans with unbounded use**. There is no comparable public evidence of a *metered* consumer AI product losing money on inference per unit, because metering ties price to cost by construction. The margin risk under PAYG migrates elsewhere: to the **free tier** (uncompensated inference), to **payment fees on small tickets**, and to **fixed overhead** that a small revenue base cannot carry.

### 2.2 Typical cost lines as a share of revenue (consumer LLM app, metered)

These are composite ranges assembled from the sources above plus Stripe's published fee schedule. The only line that is hard data is payments. Treat the rest as planning ranges, not benchmarks.

| Cost line | Typical share of net revenue | Notes | Quality |
|---|---|---|---|
| Direct inference / API | **20–50%** | ICONIQ scaling-stage avg ~23%; a16z/Bessemer imply 40–50% for app-layer cos at the low end; set by your markup multiple (1/m) | [M] |
| Payment processing (Stripe, US card) | **2.9% + $0.30 per charge** → 4.4% on a $20 ticket, 5.9% on $10, 8.9% on $5, 32.9% on $1 | Add +1.5% international card, +1% FX; fees not returned on refund; $15 dispute fee non-refundable + $15 to contest (refunded on win), since 17 Jun 2025 | [H] |
| Stripe Tax (if used) | +0.5% (no-code) or $0.50/txn (API, incl. 10 calc calls) in registered jurisdictions only | $0.50 flat on API is 5% of a $10 pack — use the no-code 0.5% path or an MoR at small ticket sizes | [H via secondary] |
| Radar fraud screening | Included (Radar Lite) on standard pricing; $0.05/screened txn for paid tiers | Mid-2026 restructure to Lite/Standard/Plus/Pro | [M] |
| Merchant of record alternative (Paddle / Lemon Squeezy) | **5% + $0.50** (LS adds +1.5% intl) | Replaces Stripe fee *and* tax compliance; 10% of a $10 pack, 7.5% of $20 | [H] |
| Apple/Google IAP (only if sold in-app on mobile) | **15%** (Small Business Program, <$1M/yr) or 30% | Web checkout avoids this; a reason to keep purchase on the web | [H] |
| Hosting / infra (non-model) | 2–5% | Small at CiC's scale; vector/db, logs, CDN | [L — planning estimate] |
| Support | 3–6% | Scales with users, not revenue, at small scale | [L — planning estimate] |
| Trust & safety / safety review | 2–5% | Higher for a product with Facilitator-governed redirect obligations; human review of flagged sessions | [L — planning estimate] |
| Refunds, disputes, fraud losses | 0.5–2% | Digital goods see card-testing fraud on small packs; Stripe keeps its fee on refunds | [M] |
| Free-tier / trial inference | 5–25% of *paid* inference cost, depending on generosity | The biggest controllable leak under PAYG | [L — planning estimate] |
| **Healthy targets** | **Gross margin ≥ 60%; contribution margin (after payments, support, T&S, free tier) ≥ 50%** | Puts CiC above the ICONIQ 52% average and in Bessemer's "Shooting Star" band | [M] |

### 2.3 The heavy-user problem, restated for PAYG

Under subscriptions the top 1–5% of users can erase the margin of the other 95% (Copilot, ChatGPT Pro, Claude Max all show this). Under PAYG the heavy user is the *best* customer. The residual risks are:
- **Per-conversation cost variance.** Long conversations, Build a Table, and retries cost more than short ones. Price the unit so that the *90th-percentile* conversation is still profitable, not the median. (See §7 for the Build-a-Table pattern.)
- **Free sampling.** Every free conversation is uncompensated inference. Cap it by count and by token budget, and treat its cost as a marketing line, not COGS.
- **Fixed overhead.** Contribution margin per pack can be 65% while the company still loses money until volume covers salaries. That is a scale question, not a pricing one, and is out of Track 2's scope.

---

## 3. (b) Small tickets and the fixed fee

### 3.1 Effective payment-fee rate by ticket size (Stripe US domestic card, 2.9% + $0.30) [H]

| Ticket | Stripe fee | Effective rate | With intl card + FX (5.4% + $0.30) | Paddle/LS MoR (5% + $0.50) |
|---|---|---|---|---|
| $1.00 | $0.33 | **32.9%** | 35.4% | 55.0% |
| $2.00 | $0.36 | 17.9% | 20.4% | 30.0% |
| $3.00 | $0.39 | 12.9% | 15.4% | 21.7% |
| $5.00 | $0.45 | **8.9%** | 11.4% | 15.0% |
| $8.00 | $0.53 | 6.7% | 9.2% | 11.3% |
| $10.00 | $0.59 | **5.9%** | 8.4% | 10.0% |
| $15.00 | $0.74 | 4.9% | 7.4% | 8.3% |
| $20.00 | $0.88 | **4.4%** | 6.9% | 7.5% |
| $25.00 | $1.03 | 4.1% | 6.6% | 7.0% |
| $50.00 | $1.75 | **3.5%** | 6.0% | 6.0% |
| $100.00 | $3.20 | 3.2% | 5.7% | 5.5% |

Stripe's $0.50 minimum charge exists precisely "so the Stripe fee doesn't exceed your charge." PayPal's micropayment rate (5% + $0.05) beats Stripe below ~$10 but is rarely worth a second processor at small scale.

### 3.2 Where a pack becomes uneconomic

- **Below $5**: payment cost alone exceeds 9% and, combined with a refund or dispute, a single bad transaction wipes out 30+ good ones ($15 dispute fee = three $5 packs' entire margin at 5× markup). Card-testing fraud targets exactly this range. **Do not sell packs under $5.**
- **$5–$10**: workable as a one-time "taster" only if it is deliberately a loss-leader into the wallet. Not a repeat-purchase tier.
- **$10–$25**: fee share 4–6%. This is where entry packs sit across AI products (Runway $10, OpenAI $5 minimum but $10+ typical, Midjourney Basic $10, Suno Pro $10, Character.AI $9.99, Poe Premium $19.99). **Recommended entry tier.**
- **$25–$60**: fee share ~3.5–4%; natural "best value" tier.
- **$100+**: fee share ~3.2%; gift/church/group tier.

### 3.3 Why prepaid bundles beat per-use charges

1. **One fee per pack, not per conversation.** Charging $2.50 per conversation costs $0.37 per charge (14.9%); a $20 pack of eight costs $0.88 (4.4%). Bundling cuts payment cost by two-thirds.
2. **Cash up front, cost later.** Prepaid credits are bookings before inference spend — the opposite of subscription loss exposure. (Chargebee's prepaid-credit guide frames this as "more repeatable revenue than pay-as-you-go with moderate barriers to growth.") [M]
3. **Breakage.** Some purchased credits are never used. Under ASC 606 expected breakage is recognised proportionally as credits are redeemed. Industry breakage on gift cards is widely cited around 10–20% but **CiC should not plan on it** — see ethics (§9): a mission-driven product should be the kind that honours balances indefinitely. [M for accounting; L for breakage rate]
4. **A balance creates return intent.** An unspent balance is a reason to come back; a per-use charge is a reason to reconsider each time.

---

## 4. (c) Observed price points and pack structures

### 4.1 AI consumables and credit top-ups (vendor price pages, 2026) [H unless noted]

| Product | Base plan(s) | Top-up / consumable structure | Expiry | Notes |
|---|---|---|---|---|
| OpenAI API (prepaid) | — | Minimum **$5** purchase; auto-recharge optional with threshold | **1 year**, not extendable | The reference pattern for "wallet + opt-in auto-reload" |
| Poe (Quora) | Free (~300 pts/day); $4.99 (10k pts/day); $19.99 (660k pts/mo); $49.99; $99.99; $249.99 | Add-on points **$30 per 1M**, subscribers only | **1 year**; non-refundable, non-transferable | 2026-07-28: Premium allowance cut — a reminder that credit-denominated plans get silently repriced |
| Runway | Free; Standard $12; Pro $28; Unlimited $76 (annual-equivalent, varies) | Top-ups **$10 per 1,000 credits** ($0.01/credit) | Varies | Clean, linear, no bonus — simplicity over anchoring |
| Suno | Free; Pro $10; Premier $30 | Top-ups exist; no published pack price (≈$4/500 credits per one blog [L]) | Purchased credits don't expire but need an active subscription to use | "Needs active sub to spend" is a dark-pattern smell to avoid |
| Midjourney | $10 / $30 / $60 / $120 per month (3.3 / 15 / 30 / 60 fast GPU-hours) | Extra GPU hours $4/hr | Monthly allowance | **4-tier ladder with 2–3× steps**; 20% off annual |
| ElevenLabs | Free (10k credits); $6 (30k); $22 (121k); $99 (500k); $299 (1.8M); $990 (6M) | Overage per credit, cheaper on higher tiers | Monthly | **Price-per-credit falls ~3× from Starter to Business** — the standard volume curve |
| Character.AI | Free; c.ai+ $9.99/mo or $94.99/yr; new $2.99/mo "lite" tier (Sep 2026) | None (subscription only) | — | Companion-chat benchmark price: **$9.99/mo** is what the market has trained users to expect for "unlimited-ish chat" |
| Cursor | $20 Pro etc. | **Max mode** billed at API cost + 20% margin; ~5× credits (Sonnet), 10–20× (Opus) | Monthly | Direct precedent for a cost-plus "expensive mode" SKU |
| Sora (OpenAI) | Bundled in ChatGPT Plus/Pro | Credits per second scale **4 / 16 / 40** by 480p/720p/1080p | Monthly | Multiplier ladder tied to measured compute |
| Audible (non-AI, credit reference) | $14.95/mo (1 credit); $22.95 (2); $149.50/yr (12); $229.50/yr (24) | Extra credits sold as **3 for $36** (members) | Credits expire 12 months after issue | The best-known consumer "credit" product: **~$12–$15 per unit**, annual pack ≈ 17% discount |

### 4.2 Mobile-game consumable ladders [M]

- Standard anchors: **$0.99 / $4.99 / $9.99 / $19.99 / $49.99 / $99.99** (Unity IAP guide; multiple monetization reports). On the web, drop the $0.99 and $4.99 rungs (fee share too high).
- Conversion of active users to payers: **1.5–3.5%** typical in 2026; 2–5% older benchmark; top titles 6–8%; below 1% signals a design problem (AppsFlyer / AppFollow / Juego Studio).
- ARPPU: casual **$10–30/month**, mid-core $50–100 (genre reports; wide variance).
- 2025 trend: "paying users are buying less often but choosing higher-priced items" (AppMagic 2025) — supports putting real effort into the *middle and upper* tiers, not the cheapest one.
- RevenueCat State of Subscription Apps 2025 (75k apps, $10B revenue): 35% of apps now mix subscriptions with consumables or lifetime purchases; outside gaming only 5–15% of apps use consumables at all. **Pure-consumable consumer apps are rare outside games** — CiC would be an outlier, which is a reason to borrow game-ladder mechanics but not game monetization culture. [M]

### 4.3 Pay-what-you-want and bundles

- **Gneezy, Gneezy, Nelson & Brown, *Science* 2010 (N = 113,047):** PWYW raised purchase *rate* but dropped revenue; **PWYW + "half goes to charity"** produced the best combination of take-up and price paid — people pay more when the payment carries meaning and when others see it. Flat "charity" framing on a fixed price did little. [H]
- **Jung & Nelson, "Paying More When Paying for Others":** PWYW payments rise when the purchase is for someone else — relevant to gift packs. [H]
- **Humble Bundle (2010–2012 public dashboards):** average ≈ $9.18 (first bundle), $7.25 (second); bimodal — a big cluster at $1–5, a smaller at $10–25, and a long tail of $100–1,000 "whales". "Beat the average" unlocks pushed the mean up. [H for the figures; data is old]
- Implication: PWYW works as a **floor-plus-slider** or **"pay it forward"** add-on, not as the base price of a product with a hard marginal cost.

### 4.4 Checkout donation add-ons [M–H]

- Round-up asks convert at a **median ~22%** (average 23.7%, best 35–40%); fixed "add $1" asks at ~17–18% (Change.io platform data; vendor-published, so [M]).
- Lyft Round Up & Donate: **100M+ donations averaging $0.38**, $42.6M total since 2017 — small asks at high frequency beat large asks at low frequency. [H — company-published totals]
- Academic checkout-charity work (Vossler et al., "Checking Out Checkout Charity") finds round-ups are perceived as less painful than flat asks for the same money, lifting totals ~21% over time. [H]
- Consumer survey: "add $1" was the *preferred* format (46%) vs rounding (23%) — preference and conversion diverge; test both.

### 4.5 What the "anchoring / best value" literature actually supports

- Three-tier ladders with a highlighted middle tier are the dominant pattern across every product surveyed; the mechanism (compromise effect, decoy) is well established in behavioural economics but the *size* of the lift in any given product is only ever reported anecdotally (10–30% claims; [L]).
- Volume bonuses in AI credit products run **10–20% on the mid tier, 20–40% on the top tier** (Ordway, Nalpeiron, Schematic, HubSpot buyer's guide — practitioner guidance, [M–L]). Adobe Firefly's ladder spans 20× in credits for 20× in price (linear); HeyGen's spans 88× credits for 88× price. Linear ladders are more common than steep discounts at the top.
- "Bonus credits" (buy 10,000 get 2,000 free) preserve list price per credit while rewarding larger packs — preferred over per-credit discounting because it keeps the unit price legible. [M]

---

## 5. (d) What makes PAYG durable rather than merely cost-recovering

| Lever | Evidence | Effect on durability | Quality |
|---|---|---|---|
| **Prepaid wallet (account balance)** | OpenAI, Poe, Runway, Perplexity Sonar all run wallets; Chargebee/Flexprice/Orb treat it as the standard AI billing primitive | Converts one-off purchases into a balance that must be spent → return visits; cash before cost | [M] |
| **Opt-in auto-reload at a threshold** | OpenAI auto-recharge; Perplexity Sonar "credits automatically refill"; billing-platform guidance: reload when balance < X | Turns PAYG into quasi-recurring revenue without a subscription promise; must be opt-in, visible, one-click off (ethics §9) | [M] |
| **Repeat-purchase rate** | No public benchmark for AI credit repurchase. Nearest analogues: consumable e-commerce 30–45% repeat (top 40–55%); half of second orders arrive within 30 days, 76% within 90 | Treat **≥35% of first-time buyers buying a second pack within 90 days** as the health line, and the gap between purchase cadence and burn cadence as the early-warning metric (Chargebee) | [M for e-com; L as applied to AI] |
| **Win-back** | E-com: a triggered re-buy invite within 30 days of first order lifts repeat rate 8–14 points | Low-balance and "balance unused for 60 days" emails; no discount needed for a credit product — the reminder is the lever | [M] |
| **Gift packs** | Jung & Nelson: people pay more when buying for others; digital gift-card market >$680B (2026) | Opens a second buyer (parent, pastor, friend) for the same user; higher ticket, lower fee share | [M–H] |
| **Group / church / institutional bulk** | RightNow Media: site licence tiered by average weekly attendance, roughly $1,200–$5,000/yr, unlimited member accounts; Planning Center: tiers by people count ($19 → $199/mo) | Direct analogue. A congregation buys a block of conversations (or a seat-cap) and distributes invite links. Large ticket, 3% fee share, repeat annually | [H for competitor pricing] |
| **Donation add-on at checkout** | Round-up median 22% opt-in; Lyft $0.38 avg × 100M | Funds a scholarship/"pay-it-forward" pool; also raises perceived legitimacy (Gneezy et al.) | [M–H] |
| **Pay-what-you-want elements** | Gneezy 2010: best as PWYW + shared social responsibility; Humble: floor + "beat the average" | Use as sliding-scale *access* (honor system, Freedom of the Press Foundation model) and as a "pay it forward" slider, not as list price | [H] |
| **Breakage** | ASC 606 lets you recognise expected breakage proportionally; CARD Act forbids gift-card expiry under 5 years (many states: never) | Real but **do not design for it**; honour balances indefinitely (ethics) and treat any breakage as upside | [H for law/accounting] |

**The scaling logic in one line:** a wallet turns a sale into a relationship; auto-reload turns the relationship into cadence; gift and group tiers turn one user into several buyers; the donation add-on turns margin into mission. None of these require a subscription promise, and all of them keep heavy users profitable.

---

## 6. Sensitivity model — margin at various markup multiples

**All API costs are illustrative placeholders, not CiC data.** Real per-conversation cost comes from the funding thread.

Assumptions (planning values, not benchmarks): Stripe US domestic 2.9% + $0.30; conversations sold in a **$20 pack**; non-API operating load (hosting 3% + support 4% + trust & safety 3% + refunds/disputes/fraud 1%) = **11%** of revenue; free-tier inference shown separately as a stress line.

### 6.1 Contribution margin by markup multiple (independent of API cost level — markup fixes the API share)

| Markup over direct API cost | API share of revenue | Payments ($20 pack) | Ops load | **Contribution margin** | Same, if free-tier inference = 20% of paid inference | Same, if pack is $10 instead of $20 |
|---|---|---|---|---|---|---|
| **2×** | 50.0% | 4.4% | 11% | **34.6%** | 24.6% | 33.1% |
| **3×** | 33.3% | 4.4% | 11% | **51.3%** | 44.6% | 49.8% |
| **4×** | 25.0% | 4.4% | 11% | **59.6%** | 54.6% | 58.1% |
| **5×** | 20.0% | 4.4% | 11% | **64.6%** | 60.6% | 63.1% |
| **6×** | 16.7% | 4.4% | 11% | **67.9%** | 64.6% | 66.4% |
| **8×** | 12.5% | 4.4% | 11% | **72.1%** | 69.6% | 70.6% |
| **10×** | 10.0% | 4.4% | 11% | **74.6%** | 72.6% | 73.1% |

Reading: 3× lands right at the AI-industry median (~52%) with nothing to spare; **5× is the first multiple that clears a 60% gross-margin target with a free tier running**; beyond 8× the gains flatten (each extra multiple buys ~1–2 points) while the price starts to look exploitative for a mission product. **Recommended planning band: 5–8×, with 5× as the floor.**

### 6.2 What those multiples mean in dollars per conversation

| Illustrative API cost / conversation | 3× | 5× | 8× | 10× | Conversations in a $20 pack at 5× |
|---|---|---|---|---|---|
| **$0.20** | $0.60 | **$1.00** | $1.60 | $2.00 | 20 |
| **$0.50** | $1.50 | **$2.50** | $4.00 | $5.00 | 8 |
| **$1.00** | $3.00 | **$5.00** | $8.00 | $10.00 | 4 |

Cross-check against the market: Audible has trained consumers to pay $12–15 per "credit"; Character.AI charges $9.99/month for unlimited-ish chat; a single conversation at $1–5 sits comfortably inside what consumers already pay per unit of comparable value. At $1.00 API cost and 8–10× the price per conversation ($8–10) starts to approach a whole month of a competitor's subscription, which is where PAYG stops being the obvious choice for a frequent user — a signal to add a bulk tier, not to cut the markup.

### 6.3 Per-pack P&L at 5× markup, $0.50 illustrative API cost, $20 pack (8 conversations)

| Line | $ | % |
|---|---|---|
| Revenue | 20.00 | 100% |
| Direct API (8 × $0.50) | −4.00 | 20.0% |
| Stripe (2.9% + $0.30) | −0.88 | 4.4% |
| Hosting / infra | −0.60 | 3.0% |
| Support | −0.80 | 4.0% |
| Trust & safety | −0.60 | 3.0% |
| Refunds / disputes / fraud reserve | −0.20 | 1.0% |
| **Contribution** | **12.92** | **64.6%** |
| Free-tier inference allocation (20% of paid) | −0.80 | 4.0% |
| **Contribution after free tier** | **12.12** | **60.6%** |

Stress cases on the same pack: one $15 dispute wipes the contribution of **1.2 packs**; a refunded pack costs the $0.88 Stripe fee plus any inference already consumed; an international buyer paying in a foreign currency cuts contribution by 2.5 points.

### 6.4 Sales tax / VAT handling at small scale

| Jurisdiction | Rule for a US seller of a digital service | Practical implication at small scale | Quality |
|---|---|---|---|
| **US states** | Economic nexus at **$100,000 sales or (in fewer states each year) 200 transactions** per state; ~35 states + DC tax SaaS, a different ~30 tax "digital goods"; Illinois (Jan 2026) and Kentucky (Aug 2026) dropped the 200-transaction test | Below $100k in any one state you generally owe only in your **home state** (if it taxes digital services). Register there, enable Stripe Tax no-code (0.5%) for that state only, monitor the nexus dashboard | [H] |
| **EU** | The €10,000 cross-border threshold applies to **EU-established** businesses only. A non-EU seller of electronically supplied services must charge destination VAT **from the first sale**, via the **Non-Union OSS** scheme (one registration) | Either register for Non-Union OSS from day one, use a merchant of record, or geo-restrict EU checkout until volume justifies it | [H] |
| **UK** | Same: no threshold for non-UK sellers of digital services | As above | [H] |
| **Everywhere else** | 101 countries now apply VAT/GST to cross-border digital sales (Paddle count) | Only an MoR realistically covers this at small scale | [M] |

Options compared on a $20 pack:
- **Stripe + home-state registration only, US-only checkout:** ~4.4% payments + 0.5% tax calc = **4.9%**. Cheapest; blocks or exposes you on international sales.
- **Stripe + Stripe Tax + self-registered Non-Union OSS/UK:** ~4.4–6.9% + 0.5% + the filing burden (quarterly OSS returns, UK VAT returns). Cheap in fees, expensive in founder time.
- **Merchant of record (Paddle / Lemon Squeezy):** **7.5%** on $20 (5% + $0.50; LS +1.5% intl), zero tax compliance, they are the legal seller. Costs ~3 points of margin to buy back the compliance problem entirely. Also displays tax-inclusive prices where EU/UK law requires it.

Recommendation: start on Stripe with US checkout and home-state registration; move to an MoR (or add one for non-US only) the moment non-US demand is real. Price packs **tax-exclusive in the US, tax-inclusive outside** (EU consumer law requires inclusive display).

---

## 7. (e) Pricing a feature with unmeasured or higher cost — Build a Table

### 7.1 How the field handles it [H for the named examples]

| Pattern | Who does it | How |
|---|---|---|
| **Cost-plus metered mode, separate from the plan** | Cursor Max mode | Billed at API token cost + 20%; ~5× credits for Sonnet, 10–20× for Opus; users opt in per request; "leave it on all day and your bill is $200–400" |
| **Explicit credit multiplier tied to a measurable driver** | Sora (4/16/40 credits per second by resolution); Midjourney (video ≈ 8× image GPU time, HD ≈ 3× SD) | The multiplier is published and tracks the cost driver (pixels, seconds, GPU-minutes) |
| **Same wallet, faster burn, no separate SKU** | Midjourney video | Simplicity; risk is users discovering the burn rate the hard way |
| **Exclusion from unlimited/relax modes** | Midjourney (video unavailable in Relax on lower tiers at launch); ElevenLabs higher-quality models cost more credits per character | Keeps the expensive feature out of any flat or bonus allowance |
| **Early-access / preview pricing** | Common across AI launches ("pricing may change", "research preview") | Lets you reprice after measurement without a "price hike" story |
| **Per-session caps** | Anthropic rate limits; Poe daily points | A hard ceiling on worst-case cost per session |

### 7.2 Conservative recommendation for Build a Table

1. **Separate SKU in the same wallet.** A Table costs *N* conversation-credits, not one. Do not fold it into the base pack's "conversations" count.
2. **Multiplier set from the cost driver, with a safety factor.** Until measured, assume cost scales at least with the number of Representatives speaking plus facilitation overhead. A defensible launch multiplier is **(number of Representatives + 1) credits per Table turn-block**, i.e. a 3-Representative Table costs 4 conversation-credits. Re-set from measured p90 cost after the first cohort, and say so up front.
3. **Label it "early access" with published pricing-may-change language.** This is the standard field pattern and removes the reputational cost of a later correction.
4. **Exclude it from bonus credits, PWYW, sliding scale, and gift packs until measured.** Bonus mechanics on an unmeasured-cost feature are how a 65% margin becomes 30%.
5. **Hard per-session caps** (turns and tokens) and a visible "this Table has used X credits" meter.
6. **Instrument before pricing.** Log tokens, model calls, and wall-time per Table from day one; the price should be derived from the p90, not the mean, because a Table's cost distribution is long-tailed (more speakers, more cross-talk, longer runs).
7. **Church/group bundles may include a fixed Table allowance** only after the measured cost is known — this is the natural upsell for the group tier.

---

## 8. Candidate pricing structures

All three assume a prepaid wallet denominated in **conversations** (not abstract "credits") because the unit is legible to a non-technical, church-adjacent audience. Dollar figures assume the **$0.50 illustrative API cost at ~5× markup**; they are shapes, not prices.

### Structure A — Three fixed packs, no wallet features ("simple shop")

| Pack | Price | Conversations | Effective price / conv | Bonus vs entry |
|---|---|---|---|---|
| Starter | $10 | 4 | $2.50 | — |
| Standard (best value) | $25 | 11 | $2.27 | +10% |
| Deep Dive | $50 | 24 | $2.08 | +20% |

- Pros: easiest to explain; no auto-reload machinery; fee share 4–6%; works as a first release.
- Cons: every repeat purchase is a cold decision; no gift or group path; no donation pool; repeat rate will track the e-commerce "cold repeat" range (~20–30%) rather than the wallet range. Merely cost-recovering plus margin — not yet a growth engine.

### Structure B — Wallet ladder with durability levers (**recommended**)

| Element | Design |
|---|---|
| Packs | Same three rungs as A ($10 / $25 / $50) plus a **$100 "Give/Group" pack** (52 conversations, +30%) |
| Wallet | Balance never expires; refundable unused balance on request |
| Auto-reload | Opt-in only, default off; user picks threshold and pack; email on every reload; one-click off |
| Gift pack | Any pack purchasable as a gift with a message; redemption link |
| Church / group | Annual site licence tiered by average weekly attendance (mirrors RightNow Media's structure), e.g. three bands; includes a conversation pool and invite links; Table allowance added only after Table cost is measured |
| Donation add-on | Round-up to the next dollar or "add $1" at checkout, funding a scholarship pool (both variants A/B-tested; expected 17–24% opt-in) |
| Sliding scale | Honor-system reduced price (e.g. 50%) on the Starter pack, no proof required, funded by the scholarship pool |
| Build a Table | Separate early-access SKU at (Representatives + 1) credits per block; excluded from bonuses and sliding scale until measured |

- Pros: every durability lever in §5 with evidence behind it; cash-before-cost; heavy users stay profitable; the group tier is the only path to large tickets and 3% fee share; donation + scholarship make the margin mission-legible.
- Cons: more billing engineering (ledger, idempotent reloads, gift redemption, group admin); auto-reload needs careful consent design; group tier needs admin tooling. Highest upside, highest build cost.

### Structure C — PWYW-with-floor ("Humble" model)

| Element | Design |
|---|---|
| Entry | Slider from a $10 floor to any amount for a fixed 4-conversation Starter; "average contribution is $X" shown; above-average buyers get +1 conversation |
| Above the floor | Larger packs at fixed prices as in A |
| Mission tie-in | A stated share of every payment above the floor goes to the scholarship pool (Gneezy's "shared social responsibility" condition) |

- Pros: strongest ethical signal; Gneezy's data says the charity-linked PWYW raises both take-up and price paid; Humble's data shows a real whale tail.
- Cons: Humble's average fell between bundles; the floor must cover 3× API cost plus fees or the average buyer is a loss; harder to forecast; invites "what should I pay?" friction at exactly the moment a first-time user is deciding; and PWYW on a product with hard marginal cost is unusual outside media bundles. Best used as the **sliding-scale and donation elements inside B**, not as the whole model.

### Recommendation

**Structure B**, built in stages: launch with A's three packs *inside* a wallet (so balances and the ledger exist from day one), add the donation add-on and gift packs in the first iteration, then auto-reload (opt-in) and the church/group tier once repeat-purchase and Table-cost data exist. Set the markup from **measured** p90 per-conversation cost at **≥5×**, keep the entry pack at **≥$10**, and treat the $10–$25 band as the primary revenue tier.

**Confidence:**
- High (well-sourced, hard data): Stripe/MoR fee arithmetic; minimum pack size; the heavy-user problem under subscriptions and its absence under metering; the 50–60% AI gross-margin benchmark; the Cursor/Sora/Midjourney multiplier precedents; tax thresholds.
- Moderate: contribution-margin targets (planning ranges built from benchmarks, not CiC measurements); donation opt-in rates (vendor-published); the 10–25% bonus-ladder norm (practitioner guidance).
- Low: any repeat-purchase or conversion rate applied to an AI conversation product (no public benchmark exists; game and e-commerce analogues only); the exact dollar rungs, which depend entirely on the funding thread's measured API cost; any claim about the size of anchoring/"best value" lifts.

**Uncertainties to resolve from real data before pricing is set:** measured p50/p90 API cost per conversation and per Table; the share of users who are non-US (drives the MoR decision); the free-tier allowance (biggest controllable leak); whether a church/group buyer exists at all before a group tier is built.

---

## 9. Ethical pricing norms for a mission-driven product

Drawn from nonprofit/mission-software practice (Freedom of the Press Foundation honor-system sliding scale; TechSoup budget-based tiers; Neon CRM revenue-based pricing; YEA Camp "pay it forward") and consumer-protection law:

1. **Transparent unit price.** State what a conversation costs and what a Table costs in plain numbers before checkout; no abstract credits that hide the exchange rate (Poe's 2026 allowance cut is the cautionary tale).
2. **No expiry on paid balances**, or at minimum the CARD Act's 5-year floor; refund unused balance on request. Breakage is upside, never a plan.
3. **Auto-reload is opt-in, visible, and trivially reversible**; email on every charge; no "needs active subscription to spend your purchased credits" conditions.
4. **Sliding scale on the honor system** rather than means-testing; fund it from the donation add-on so generosity is visibly recycled.
5. **No manipulative scarcity or countdown mechanics**; "best value" is a true statement about price per conversation, not a nudge.
6. **Honest early-access labelling** for Build a Table, with the reason (cost not yet measured) stated.
7. **Tax-inclusive display where the law requires it** (EU/UK), and no silent surcharges at checkout.
8. **Margin is legitimate.** Nonprofit practice does not require break-even pricing; it requires that the surplus serve the mission and that access is protected. A 60%+ contribution margin with a funded scholarship pool is the standard shape.

---

## Sources

Payments and tax
- Stripe pricing (US): https://stripe.com/pricing — 2.9% + $0.30; +1.5% international; +1% FX (accessed via secondary summaries 2026-10-02)
- Stripe, "Understanding fees for refunded payments": https://support.stripe.com/questions/understanding-fees-for-refunded-payments
- Stripe, "June 2025 pricing updates for disputes": https://support.stripe.com/questions/june-2025-pricing-updates-for-disputes
- Stripe, Charge object / minimum amounts: https://docs.stripe.com/api/charges/object ; https://docs.stripe.com/currencies
- Stripe Tax pricing: https://support.stripe.com/questions/understanding-stripe-tax-pricing ; https://feetrace.com/blog/stripe-tax-fees-for-saas-in-2026-complete-guide
- Stripe Radar 2026 tiers: https://www.corgilabs.ai/insights/stripe-radar-pricing-change ; https://feetrace.com/blog/stripe-radar-fees-explained-for-saas-teams-in-2026
- Stripe fee tables 2026: https://checkoutpage.com/blog/stripe-processing-fees ; https://checkoutpage.com/blog/stripe-international-fees ; https://www.chargeflow.io/blog/stripe-dispute-fees
- Paddle vs Lemon Squeezy: https://dodopayments.com/blogs/paddle-vs-lemon-squeezy ; https://www.bitsfolio.com/paddle-vs-lemon-squeezy-saas-fees-mor-traps/
- Apple Small Business Program: https://www.revenuecat.com/docs/platform-resources/apple-platform-resources/app-store-small-business-program
- US digital-goods sales tax 2026: https://dodopayments.com/blogs/sales-tax-digital-goods-by-state ; https://innovatetax.com/blog/3-updates-united-states/ ; https://www.avalara.com/us/en/learn/guides/state-by-state-guide-economic-nexus-laws.html
- EU OSS / digital goods VAT: https://stripe.com/resources/more/one-stop-shop-oss-vat-scheme ; https://fluentcart.com/blog/digital-goods-vat-oss-guidance-eu/
- Gift-card law and breakage (ASC 606): https://www.revenuehub.org/article/unexercised-rights ; https://www.hubifi.com/blog/gift-card-breakage-accounting

Margins and unit economics
- a16z, "The New Business of AI": https://a16z.com/the-new-business-of-ai-and-how-its-different-from-traditional-software/
- ICONIQ, State of AI 2025 (PDF): https://cdn.prod.website-files.com/65d0d38fc4ec8ce8a8921654/685ac42fd2ed80e09b44e889_ICONIQ%20Analytics_Insights_The_AI_Builders_Playbook_2025.pdf ; SaaStr summary: https://www.saastr.com/the-execution-era-of-ai-5-key-takeaways-from-iconiqs-state-of-ai-report/
- Bessemer, State of AI 2025: https://www.bvp.com/atlas/the-state-of-ai-2025
- Tanay Jaipuria, "The State of AI Gross Margins in 2025": https://www.tanayj.com/p/the-gross-margin-debate-in-ai
- SaaStr on OpenAI compute margin: https://www.saastr.com/have-ai-gross-margins-really-turned-the-corner-the-real-math-behind-openais-70-compute-margin-and-why-b2b-startups-are-still-running-on-a-treadmill
- GitHub Copilot losses (WSJ via The Register, Oct 2023): https://www.theregister.com/2023/10/11/github_ai_copilot_microsoft/
- ChatGPT Pro losing money (TechCrunch, Jan 2025): https://techcrunch.com/2025/01/05/openai-is-losing-money-on-its-pricey-chatgpt-pro-plan-ceo-sam-altman-says
- Anthropic weekly rate limits (TechCrunch, Jul 2025): https://techcrunch.com/2025/07/28/anthropic-unveils-new-rate-limits-to-curb-claude-code-power-users/

Price points and ladders
- OpenAI prepaid billing: https://help.openai.com/en/articles/8264644-setting-up-and-managing-prepaid-api-billing
- Poe purchases FAQ: https://help.poe.com/hc/en-us/articles/19945140063636-Poe-Purchases-FAQs ; https://www.usagepricing.com/blueprint/poe
- Runway credits: https://www.usagepricing.com/blueprint/runway ; https://stacksheriff.com/ai-tools/runway-pricing/
- Suno: https://www.usagepricing.com/blueprint/suno
- Midjourney: https://fluxnote.io/guides/midjourney-pricing-2026 ; video GPU cost: https://www.dreamhost.com/blog/midjourney-ai-video/
- ElevenLabs: https://flexprice.io/blog/elevenlabs-pricing-breakdown
- Character.AI: https://www.eesel.ai/blog/character-ai-pricing ; https://www.usagepricing.com/blueprint/character-ai
- Cursor Max mode: https://cursor.com/docs/models-and-pricing ; https://www.morphllm.com/cursor-max-mode
- Sora credits: https://help.apiyi.com/en/sora-2-versions-credits-pricing-guide-en.html
- Audible credits: https://www.nerdwallet.com/finance/learn/how-much-does-audible-cost ; https://slickdeals.net/f/14160545-three-audible-credits-for-36
- Credit-ladder design guidance: https://ordwaylabs.com/blog/ai-credits/ ; https://schematichq.com/blog/credit-based-pricing ; https://blog.hubspot.com/website/ai-credits-buyers-guide ; https://www.usagepricing.com/blueprint/trivia
- Prepaid credits guide: https://www.chargebee.com/pricing-labs/prepaid-credit-pricing-guide/ ; https://stripe.com/guides/pricing-ai-products-lessons-from-leading-ai-companies
- Mobile game IAP anchors and conversion: https://unity.com/resources/in-app-purchases-guide ; https://appfollow.io/blog/mobile-game-kpis ; https://www.appsflyer.com/resources/reports/app-marketing-monetization-report/ ; https://gamedevreports.substack.com/p/appmagic-mobile-games-monetization
- RevenueCat State of Subscription Apps 2025: https://www.revenuecat.com/state-of-subscription-apps-2025
- Repeat-purchase benchmarks (e-commerce): https://prooflytics.io/blog/repeat-purchase-rate-benchmarks ; https://eightx.co/blog/average-repeat-purchase-rate-by-vertical

PWYW, donations, group licensing, ethics
- Gneezy, Gneezy, Nelson & Brown, *Science* 329:325 (2010): https://www.science.org/doi/10.1126/science.1186744
- Jung & Nelson, "Paying More When Paying for Others": https://rady.ucsd.edu/_files/faculty-research/uri-gneezy/PIF_JPSP.pdf
- Humble Bundle data: https://cheesetalks.net/humble/ ; https://techcrunch.com/2011/09/28/new-humble-bundle-tries-different-pricing-tack
- Checkout charity: https://getchange.io/blog/picking-and-testing-the-best-donation-options ; https://www.lyft.com/blog/posts/smaller-donations-more-money-the-surprising-math-of-check-out-charities ; https://www.lyft.com/blog/posts/which-lyft-riders-are-most-philanthropic-a-data-dive-into-100-million ; Vossler et al.: https://volweb.utk.edu/~cvossler/files/Checkout%20Charity%20Manuscript%20(accepted).pdf
- RightNow Media and Planning Center pricing: https://learnofchrist.com/resources/rightnow-media ; https://churchmemberpro.com/blog/planning-center-pricing-guide/
- Sliding-scale / mission pricing: https://freedom.press/digisec/programs/pricing/ ; https://www.getmonetizely.com/articles/pricing-for-nonprofits-balancing-accessibility-with-sustainability ; https://yeacamp.org/sliding-scale/
