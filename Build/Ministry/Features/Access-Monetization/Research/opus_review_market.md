# Opus adversarial review: market buy-in for the Access and Monetization offer

Reviewer: Opus 5.5 (high rigor), read-only. Date: 2026-10-02.
Under review: the pilot offer as decided in `Build/Ministry/Features/Access-Monetization/Decision-Log.md` (entries 1-17): free 3 conversations x 3 turns; paid one-time packs $7/5, $15/13, $30/30 conversations of up to 7 turns; no subscription; cookie-only; Facilitator speaks the offer.
Evidence read: the Decision Log and Open Gaps; `sample3.json` (real 3-turn conversation); `run15.json`/`run15.log` (real 15-turn run); prior research tracks and round-1 review; `cic-website/` index, about, support, `traditions/alexandria-catechetical.html`; `engine/api/config.py`; the Marketplace scan and contribution-rate analysis (treated as unverified brainstorm); web searches (2026-10-02).

Sourcing marks: **[P]** primary page or repo file read directly. **[S]** search-engine summary of a page the proxy blocked (ncregister.com, today.com, learnofchrist.com, othergospels.com, patristics.info were all blocked). **[I]** my inference. "Could be stronger" is not treated as a finding.

---

## Verdict first

**Unlikely** that pay-as-you-go reaches sustainable buy-in at pilot. **Plausible** that it produces a real, small, informative signal if the test is designed for learning rather than revenue.

The product has a genuine voice and a real gap in the market. But at pilot scale the arithmetic, the first impression, and the competitive price anchor all point the same way: a handful of buyers, tens to low hundreds of dollars, and paid revenue that probably does not cover the free bucket it sits beside.

---

## 1. Will people pay?

### 1.1 What the comparables actually show

| Product | What it sells | Traction (source quality) | Lesson for CiC |
|---|---|---|---|
| Bible Chat | General-LLM devotional chat, hard paywall with trial, ~$49.99/yr | ~10M users and ~$15M annualised revenue within a year; $14M Series A (Feb 2025); $750K net revenue in Mar 2024 [S: Romania Insider, Appfigures] | Faith audiences *do* pay for AI chat at scale, but through mobile app-store subscription funnels with paid acquisition and a trial wall, not web one-time packs. No source discipline. |
| Hallow | Human-made prayer content, $69.99/yr | ~$40M net 2025 (Appfigures estimate); ~280K downloads/month, 25x spikes on Ash Wednesday [S: Appfigures] | Money follows *habit and season* (Lent), not curiosity. Hallow states AI "does not have a soul" and keeps prayer human-made [S: hallow.com/blog/thoughts-on-ai]. Its Q&A is licensed from Magisterium. |
| Magisterium AI (incl. Saint Chat) | Catholic-source RAG with citations; ~20 saint personas including Augustine and Jerome; debate mode | ~100K monthly users [prior scan, S]; **Pro is $3.99/month or $29.99/year, cut from $8.99/$79** [S: magisterium.com blog]; free tier reported as rate-limited (one summary says 90 queries/week, another says 10 queries) [S, conflicting] | **The nearest rigor comparator has just cut its price by more than half and gives a free tier larger than CiC's whole paid entry pack.** Rigor is struggling to monetise as a destination even at $30/year. |
| Text With Jesus | ChatGPT-voiced Jesus, apostles, paywalled "Satan"; $2.99/mo; $199.99 "forever" | 100K+ Google Play installs; 4.7 stars from ~2.7K App Store ratings [S: store listings] | Grows despite "blasphemy" press. No published payer numbers. |
| Hello History (now Humy) | 400+ historical figures, GPT-4; 20-message trial then $3.99/wk-$34.99/yr | 100K-200K installs (sources disagree); "5 million messages"; pivoted to schools (5K+ teachers) [S] | The closest "talk to the past" consumer product could not sustain a consumer business and moved to institutional sales. Reviews resent the sudden wall after a counter. |
| Free church-father bots | othergospels.com "Chat with Early Church Fathers" (Origen and others); patristics.info Apostolic Fathers, Irenaeus, Chrysostom bots | Free [S; both blocked for direct fetch] | A searcher for "chat with Origen" finds free options first. |
| Character.AI, ChatGPT, Claude | Any persona, unlimited or near-unlimited free | ChatGPT: ~900M weekly users, ~50M paying, ~5.6% [S: OpenAI via press, Feb 2026] | The default comparison is "free". Even the world's leading AI product converts ~5-6% to paid with daily-habit use. |
| Great Courses/Wondrium, Ligonier Connect | Expert-taught courses | $7.99-$20/month; Ligonier single course $45 or subscription [S] | The church-history hobbyist already pays for *human expert authority*. |
| RightNow Media, FORMED | Church-licensed libraries | RightNow from ~$155/month for <100 attendance; FORMED parish ~$2,000-2,450/yr [S] | Churches pay real money, annually, from a budget line, after a pastor vouches. This is the structurally strong buyer, and the pilot excludes it. |
| JustAnswer | Pay-per-question expert answers | FTC suit, Jan 2026, over $1/$5 "join" fees that became $28-$125/month subscriptions [P-adjacent: FTC press release title via search] | One-off paid Q&A survives mainly through dark patterns. CiC has rightly ruled those out, which also removes the main driver of that model's revenue. |

**What religious audiences say about AI voices for the faith.** Barna/Gloo (State of the Church, Nov-Dec 2025, n=1,514 adults and 442 Protestant pastors) [S: multiple outlets]: 48% of practicing Christians say they trust AI to aid spiritual growth, but **83% worry AI will misinterpret Scripture and 72% worry it is acting as a replacement for God or spiritual leaders. Only 12% of pastors would trust AI for spiritual growth, and 94% worry about misinterpretation.** Catholic critics call for Magisterium AI to be "deleted" (New Polity) and warn that saint chat risks displacing "authentic relationships, prayer or the sacraments" (NC Register) [S]. Futurism and Today report "AI Jesus" bots that say "I am Jesus Christ" and draw "blasphemy" responses [S]. Hallow, the sector's commercial leader, publicly refuses AI-generated prayer [S].

Read for CiC: the market is split. Laypeople will use AI faith tools; the gatekeepers (pastors, teachers, Catholic and Reformed commentators) distrust them. CiC's best defence is real: a composite community voice ("we", "our teachers") not a saint or Jesus impersonation, and visible sourcing. But **the first thing a cautious buyer asks is "who is speaking for this tradition?"**, and the site answers with process (eight steps, verified quotes), not with a named scholar or institution. `support.html` itself says independent academic review is "hoped to fund... down the line" [P]. That is an honest admission, and it is also the missing piece of buyer trust.

### 1.2 Segments and willingness to pay

| Segment | Likely individual WTP for this offer | Why | Confidence |
|---|---|---|---|
| Curious seekers (arrive via a link or search) | $0; a few at $7 once | Free ChatGPT/Claude will role-play Origen; free church-father bots exist; curiosity is one-off, not a need. | Medium |
| Lapsed or deconstructing Christians | $0-7 once, low rate | Barna reports 42% of adults say they deconstructed the faith of their youth [S], so the pool is large. But the site's mission line is "to help people experience Jesus in new ways" [P: about.html], which a deconstructing reader can hear as evangelistic, and this group is the most sensitive to faith being monetised (the Pray.com and Hallow billing complaints in the prior research). The product's honest "fought over, cost men their sees" register does suit them. | Low-medium |
| Students | $0 individually; real only if assigned | Low cash, plenty of free AI. A teacher assigning it turns this into the church/class pool, which is not built. | Medium |
| Scholars | $0 (they evaluate, they don't buy) | Their value is endorsement. Without an external reviewer they are a risk segment (a public "it gets X wrong" post), not a revenue one. | Medium |
| Clergy and lay leaders | Individually $0-15; institutionally $50-300 for a class | 12% pastor trust [S]. They buy RightNow/FORMED through budgets, annually. A one-time pool is a fit; it does not exist yet (Decision 4). | Medium |
| Church-history hobbyists (Great Courses, podcast, Ligonier listeners) | **$7-30, the best individual segment** | Already pay $8-45 for content about this period; value depth and sources; older readers tolerate long replies. Risk: older demographic is more AI-sceptical. | Low-medium (no direct data) |
| Small groups | Through a leader, $15-30 | Want shared or multi-voice use; Build a Table is excluded from packs. | Low |
| Non-native English readers | Low in USD | B2 target helps comprehension, but purchasing power and USD-only pricing cut demand. Long replies hurt them most. | Low |

**Bottom line on Q1:** some people will pay. The plausible individual buyer is a church-history enthusiast or a reflective practising Christian who has already spent time in the Family Tree. That group is real but small and is not reached by a pilot that runs on informal direct links.

---

## 2. Is the free experience enough to create desire?

I read all three turns of `sample3.json` and the first four of `run15.json` [P].

**What works.** The voice is distinctive and not generic. It names its own people ("our teachers", "Gregory", "Athanasius, bishop for forty-six embattled years"), uses its own imagery ("the New Song", "like a spark falling on our innermost soul"), gives a specific, checkable plague letter from Dionysius, and states the limit of its own knowledge in its own register ("What we cannot tell you is a mechanical account... we did not ask it"; "Ask about that."). Turn 2's ending is the single best "aha" line in the sample. Sentences are short (17-21 words average; my rough Flesch estimate is ~72-76, grade ~7-8 [I, approximate syllable count]). A reader who reads it all will hear a world.

**What a stranger actually meets.** These are the defects, in the order a stranger meets them:

1. **Turn 1 opens with an echo** [P: sample3 turn 1]: "I grew up in a church where people said the right words without wrestling... I want to know: Who was Jesus to your people..." followed by a `---` rule, then the answer. The 15-turn run's turn 1 echoes in the second person ("You grew up in a church where nobody asked hard questions") [P]. Open Gaps entry 5 counts 3 of 6 replies echoing. The single most important reply in the funnel reads, half the time, like a chatbot mirroring the user, which is an AI tell under `CLAUDE.md`. **This is a conversion defect, not cosmetic.**
2. **Waiting with nothing on screen.** Replies took 17-25 s in sample3 and 21-34 s in run15 [P]. `engine/api/config.py` says the streaming module is "Off by default. No code path reads this flag yet" [P]. A first-time visitor waits about 25 seconds before seeing anything. Web norms make that a drop-off point [I].
3. **Length.** 576, 349 and 537 words (sample3); 527, 436, 632 (run15) [P]. That is 1,400-1,600 words across three turns, about 7-8 minutes of reading at 200 wpm. NN/g found users read at most 28% of the words on an average page and read half only on pages of 111 words or less [S: nngroup.com]. The aha lines are buried in paragraph 4 or 5. Decision 12 aims to shorten replies; until that is measured, the free sample is too long for a stranger.
4. **Repetition inside three turns.** The Gregory "spark" quote appears in turns 1 and 3 of sample3; the Athanasius "made man that we might be made God" line appears in turns 1, 2 and 3 of run15; the Logos-through-whom-all-was-made frame recurs in every turn [P]. A buyer deciding whether 5 or 13 more conversations will hold new material sees the repertoire looping by turn 3. This directly undercuts the reason to pay.
5. **The free allowance overlaps what the tree already gives free.** The Alexandria tradition page (~3,300 words) already contains the Dionysius plague story, Arius and homoousios, Athanasius's five exiles and Didymus [P]. A visitor who came through the tree hears the same stories again in the conversation. The free tree is a good front door; it is also a substitute for the paid product's content.
6. **Three turns is roughly the natural arc, not short of it.** Turn 3 in both runs closes with "where would you begin" and a summary ("So the connection is this...") [P]. That is good for satisfaction, and it means the free conversation *feels complete*. Kindle-sample logic needs the sample to end with an open loop; this one closes the loop. [I]
7. **The differentiator is not in the text.** The reply prose carries no visible confidence labels. The frontend has `SourceList`, `WitnessMark` and `StoryMark` components [P: cic-poc/frontend/src/components], but I did not confirm they render on the engine path the website uses, and the sample JSON carries no source fields [P]. If the participant cannot see "Documented / Contested" or a source list, the free experience is indistinguishable at a glance from asking Claude to play an Alexandrian teacher.

**Comparison to "aha before the wall".** The prior research's own rule (R2F, Track 1) is that the free unit must deliver the whole experience before any ask. Here it can, *if* the echo is gone, the first reply arrives within a few seconds, and the reply is half its length. Today, with all three defects, I expect most strangers to leave during turn 1 rather than at the wall. **Confidence: medium.** It rests on one world (alx) and two scripted runs, not on real visitor behaviour.

**Is 3 x 3 the right size?** Nine free turns cost roughly $0.30-0.40 per fully used visitor (cold cache), not $0.24. Sample3's turn 1 carried a 15,040-token cache write and cost $0.079, making the 3-turn conversation $0.128, not the $0.08 in Decision 14 [P]. At pilot traffic the cache will usually be cold per conversation [I]. Three conversations is generous relative to Magisterium's reported 10-query free tier, and stingy relative to its other reported 90/week. The bigger question is not size but sequencing: a visitor who loves conversation 1 hits two more free ones before any ask, by which point curiosity is usually spent [I].

---

## 3. Is the paid offer legible and fair-feeling?

**"A conversation of up to 7 turns" is legible only after use.** Before using it, "turn" is jargon. After three 3-turn conversations it becomes concrete: "a paid conversation goes more than twice as deep." The offer should be said that way, in the Facilitator's voice: "Paid conversations can go seven exchanges instead of three." [I]

**Seven turns feels like a step up, not a cut-off, as long as the end is a close and not a wall.** Turn 3 already reaches a natural summary. Seven gives room for one tangent and a return. With 500-word replies, seven turns is ~3,500 words, longer than most visitors will read. So the cap will rarely bind; what the buyer actually buys is *more conversations*, not depth. Count the pack in conversations and keep depth as a reassurance, not the headline. [I]

**What the first-time buyer compares it to.**

| Anchor | Price | How $7 for 5 looks |
|---|---|---|
| Free ChatGPT / Claude / Character.AI | $0, unlimited-ish | Expensive for "an AI chat" |
| Magisterium AI Pro (with Saint Chat) | $3.99/month or $29.99/year, unlimited-ish [S] | **CiC's $30 pack (30 conversations) costs the same as a year of Magisterium** |
| Text With Jesus / Hello History | $2.99/month; $3.99/week | Comparable to slightly expensive |
| A paperback on early Christianity | $15-20 | Cheap |
| A coffee | $5-7 | Equal |
| A Ligonier or Great Courses course | $45 or $8-20/month | Cheap |

**Why pay $7 for what a free chatbot does?** Honest answer: most visitors will not, because at the moment of purchase the difference is not visible. The differentiators are (a) a community voice built from a reviewed record, (b) quotes verified against vendored sources, (c) confidence labels, (d) a safety design. Only (a) is audible in the replies; (b) and (c) are invisible unless the UI shows them; (d) is invisible by design. The one argument a buyer can feel is "this is a small public-benefit project and the cost is real", which is a *donation* argument, and Decision 5 deliberately separated donations from purchase. **That separation is right for legal and integrity reasons, but it removes the strongest emotional reason a small-project buyer pays.** The offer needs its own reason that is not "support us".

**Three rungs at pilot.** With an expected handful of buyers, three rungs give no usable price signal: a single purchase of the $30 pack is noise. The $30 pack also commits 30 non-expiring conversations priced from one cold-start-free measurement; at a cold first turn and the 1.35 billing multiplier a 7-turn conversation is ~$0.39 [I, from run15 turns 2-7 plus sample3 turn 1], so the $30 rung's contribution is ~60%, and a repricing trigger is still open (Decision 17).

---

## 4. Structure risks

1. **No subscription means no habit loop.** Every comparable that makes money (Hallow, Bible Chat, Magisterium, Character.AI) does it through a recurring habit (daily prayer, daily devotional). CiC is a *reflective, occasional* product. That is a principled choice, and it means revenue per buyer is one purchase of $7-15 and repeat purchase is rare [I]. Expect repeat-purchase among buyers of 5-15% in the pilot window.
2. **Non-expiring units are fair and cheap to promise at low volume.** The risk is cost drift on the $30 rung (above), not buyer distrust. Not a demand risk.
3. **The existing "about five conversations" message contradicts the new offer.** Every tradition page says: "Because of cost, we're asking each participant to keep to about five conversations for now. We can't enforce this yet, only ask" [P: alexandria-catechetical.html line 388]. A visitor who read that and then meets "three free" will feel the allowance shrank. It also primes the visitor to think of conversations as a burden on the project, which favours donating or holding back over buying. This text must be replaced at the same moment the allowance goes live.
4. **Donation lane beside the purchase lane.** The site says contributions "are not tax-deductible" and Faithways is "not a nonprofit" [P: support.html]. For a faith audience used to giving to tax-deductible ministries, that weakens the donation lane; and the free bucket is "funded from contributions". If paid conversion is low (Section 5), contributions carry both the free bucket and fixed costs, and there is no measured donation rate yet: the funding log's 2% projection is explicitly "waiting on real data" [P: Funding/CiC_Org_Funding_Decision_Log.md].
5. **Church/class pool timing.** The one buyer type with a budget and a pattern of paying (RightNow, FORMED) is excluded from the pilot. Shared church networks also hit the per-IP seeding problem (Decision 4, 6). Launching individual packs first tests the weakest market first. [I]
6. **Cookie-only, no email.** Consequences: (a) a buyer who clears cookies, changes device or uses private browsing loses a paid balance unless a recovery path exists; the recovery design is open. (b) Phones and laptops are separate balances, so a buyer reads on mobile and cannot continue on desktop. (c) There is no way to tell a buyer "a new tradition opened", so repeat purchase depends on the buyer remembering the site. That last point is a direct ceiling on repeat purchase [I]. A receipt email from Stripe exists anyway; using that address for a recovery link only (not linked to transcripts, consistent with Decision 8) is the cheapest fix.
7. **Latency and no streaming** (Section 2) is a structural conversion risk that sits upstream of every pricing choice.

---

## 5. How many will buy?

### 5.1 Benchmarks, and why they over-state CiC

- Consumable/credit-pack apps: 1-5% free-to-paid; top games 4-8% [S: forasoft summary].
- Mobile AI apps: median 2.4% download-to-paid by day 35, top quartile 4.8% [S: RevenueCat 2026 via summary]. These are subscription funnels with trials and store payment, on mobile.
- ChatGPT: ~5.6% of weekly users pay [S].
- Web, no account, no app-store one-tap payment, one-time purchase, occasional-use reflective content, AI-sceptical gatekeepers: every factor pushes CiC *below* those medians [I]. No public free-to-paid figure exists for a one-time-pack AI conversation product (prior research R2B, uncertainty 1).

### 5.2 Defensible range for this product

Measured per visitor who **starts at least one conversation**:

| Scenario | Purchase rate | Notes |
|---|---|---|
| Pessimistic | 0.3-0.8% | Cold traffic, echo/latency unfixed, long replies |
| Central | 1-2.5% | Warm traffic (Family Tree visitors, personal invitations), defects fixed |
| Optimistic | 3-6% | Warm, invited, church-history audience; streaming on; sources visible; a reason to buy beyond "more" |

Among visitors who **exhaust all three free conversations**, rates should be roughly 3-5x higher, because exhausting nine turns is itself a strong intent signal [I].

Average first order: ~$9-11 (most buyers take $7; a few take $15) [I]. Repeat purchase within the pilot: 5-15% of buyers [I].

### 5.3 Pilot-scale revenue

Pilot assumption: informal direct links, personal invitations, the tree's organic traffic. Assume **300-1,500 visitors start a conversation over three months** [I; the repo holds no measured traffic figure, and the prototype plan spoke of 5-10 testers].

| Starters | Central 1-2.5% | Buyers | Gross at ~$10 |
|---|---|---|---|
| 300 | | 3-8 | $30-80 |
| 1,500 | | 15-38 | $150-380 |

Against that:
- **Free bucket:** at ~1.7 conversations per starter on average and ~$0.12 per cold 3-turn conversation x 1.35 billing, about $0.28 per starter, or **$80-420** for 300-1,500 starters [I, from P figures].
- **Break-even for paid to cover free alone:** contribution per buyer is ~$5-7, so paid covers the free bucket only above about **4-5% of starters**, i.e. only in the optimistic scenario.

**Plain statement:** pay-as-you-go will **not** be a primary financial engine at pilot scale. In the central case it covers part of its own free bucket and none of hosting or development. Implications:
1. Frame the pilot as a *demand test with a price attached*, not a revenue line. Success means a clean measurement, not covering costs.
2. Fixed costs and the free bucket stay on contributions and founder funds through the pilot.
3. The structurally stronger revenue (the church/class pool, the prior funding thread's institutional licence idea) should be tested in parallel, not after.

---

## 6. What to measure in the pilot

### 6.1 Fix before measuring (otherwise the test measures the defects)

The echo (Open Gaps 5), the ~25 s blank wait (streaming off), and reply length (Decision 12) all depress conversion upstream of price. A pilot run with them in place will read as "nobody wants to pay" when the true finding is "nobody finished turn 1".

### 6.2 Cheap demand tests, in order

1. **Fake door before real checkout (one to two weeks).** At the end of the third free conversation, the Facilitator card shows the three packs. Clicking a pack opens "Paid conversations open on [date]. Leave nothing; we will not track you. Would you have bought this one?" with Yes/No. Measures click-through by rung at zero legal exposure. (Counsel review, Decision 9, gates real checkout anyway.) Disclose honestly that it is not yet on sale.
2. **Real checkout in Stripe live mode, single rung first** ($7 for 5) for the first 300 starters, then add the ladder. One rung gives a cleaner yes/no signal at tiny n.
3. **Two-question exit survey on the close card** (optional, anonymous): "What would make another conversation worth paying for?" (free text) and "Which is closest to what you'd compare this to: a free chatbot / a book / a course / a donation / nothing". This answers Section 3's anchor question directly.
4. **Do not run Van Westendorp at pilot.** Sources put the minimum at 50 valid responses and stable results at 200-400 [S]. A pilot will not reach that per segment. Use the fake-door clicks plus actual purchases (revealed preference) instead. If a list of 50+ church-history enthusiasts can be reached (a podcast or class), run it there once.
5. **Five recorded "think-aloud" sessions** with recruited strangers from the hobbyist and lapsed segments, watching them meet turn 1 and the wall. Cheapest way to see whether the voice lands.

### 6.3 What to log per visitor (anonymous, cookie id, never joined to transcript text per Decision 8)

Arrival path (tree page / homepage / direct link); tree time before first conversation; conversations started and turns completed per conversation; whether turn 1 was finished (time on reply, scroll to end); time to first visible text; reply length; free allowance exhausted (yes/no); close card shown, pack clicked, checkout opened, paid; rung; days to second purchase; refund requests; donation click (separately).

### 6.4 Pre-registered thresholds (decide before launch)

Measured over the first 500 visitors who start a conversation, or 90 days, whichever comes first:

- **Continue as designed:** purchase rate >= 2% of starters, or >= 8% of free-allowance exhausters; median turns completed in conversation 1 >= 2.5.
- **Redesign the offer (not the price):** 0.5-2% of starters; or fake-door click >= 5% but real purchase < 1% (a price or trust gap, not a desire gap).
- **Stop individual packs, move to church/class and donation-led access:** < 0.5% of starters, or < 30% of starters finish turn 1 even after the fixes in 6.1.

### 6.5 The three changes most likely to raise buy-in

1. **Make the first reply land in seconds and in ~200 words, with no echo.** Turn on streaming (or at least a visible "writing" state with the first sentence fast), fix the echo, and shorten replies. This raises everything downstream; no pricing change comes close. Confidence: high that it matters, medium on size.
2. **Show the differentiator on screen at the point of purchase.** Render the source and confidence marks in the free conversation, and put one concrete line on the close card that a free chatbot cannot say, e.g. "Every quotation you read was checked against the source text." Without this, the honest comparison is to free ChatGPT and the answer is "no". Confidence: medium.
3. **Lead with the church/class pool, or ship it alongside.** The buyer with a budget is a teacher or pastor running a 4-6 week class, the RightNow/FORMED pattern but one-time. A $49-99 pool for a class is a single sale worth 5-10 individual packs, and the pastor becomes the trust voucher the product lacks. Confidence: medium; the 12% pastor-trust figure is the risk.

Honourable mention: replace the "about five conversations" line the same day the allowance changes; give each conversation a reason to return (a new tradition, a "you might ask Mar Yausep the same question" bridge across worlds), since cross-world comparison is the thing no free chatbot or Magisterium offers.

---

## Final verdict

**Unlikely** that the offer reaches sustainable buy-in at pilot. **Plausible** that it yields a clear, decision-grade demand signal if the defects in 6.1 are fixed first and the thresholds in 6.4 are set in advance.

**Five biggest reasons**

1. **Scale arithmetic.** At a realistic 1-2.5% of starters and 300-1,500 starters, the pilot earns roughly $30-380 gross, and paid only covers the free bucket above ~4-5% conversion. [Section 5]
2. **The first reply is the weakest point of the funnel.** Echo in about half of first replies, a ~25 s blank wait (streaming not wired), and 500-600 words before the aha. [Section 2, P]
3. **Price anchors are hostile.** Free general chatbots, free church-father bots, and Magisterium's Saint Chat at $29.99/year make $7 for 5 look expensive unless the sourcing is visible on screen, which it currently is not in the reply text. [Sections 1, 3]
4. **Trust gatekeepers are sceptical.** 12% of pastors trust AI for spiritual growth and 94% fear misinterpretation; there is no named external reviewer yet; critics call religious chatbots unfit in principle. A tradition-bound voice is a better answer than "AI Jesus", but it has to be shown. [Section 1]
5. **The structure removes the usual revenue engines on purpose** (no subscription, no email, no habit loop, donations separated, church pool deferred). Each is defensible; together they leave a one-time, occasional purchase with little repeat. [Section 4]

**Decisions only Mark can make**

1. Whether the pilot's purpose is *revenue* or *a priced demand test*. This review recommends the latter, with pre-registered thresholds.
2. Whether the fixes in 6.1 (echo, streaming, length) gate the paid launch. They sit in the voice and engine workstreams.
3. Whether the church/class pool moves forward to ship with, or before, individual packs.
4. Whether to launch with the full ladder (Decision 17) or a single $7 rung first, given that three rungs cannot be read at pilot n.
5. Whether a buyer may give an email for balance recovery and new-tradition notices only, kept apart from transcripts (a change to the cookie-only position).
6. Whether to seek a named external scholar or institution before charging, so the answer to "who speaks for this tradition?" is a person.
7. The replacement wording for the "about five conversations" line, and whether the free allowance stays 3 x 3 or becomes smaller in count but faster to the aha.

---

## Sources

Web (2026-10-02; [S] = search summary, page blocked or not fetched):
- Bible Chat: [Romania Insider](https://www.romania-insider.com/bible-chat-investment-round-faith-app-romania-feb-2025), [Appfigures](https://appfigures.com/resources/insights/20250418/amp?f=5), [Vestbee](https://www.vestbee.com/insights/articles/bible-chat-secures-14-m)
- Hallow: [Appfigures Lent surge](https://appfigures.com/resources/insights/hallow-lent-surge-prayer-app-revenue), [Hallow "Thoughts on AI"](https://hallow.com/blog/thoughts-on-ai/)
- Magisterium: [pricing post](https://www.magisterium.com/blog/magisterium-ai-just-became-more-affordable), [NC Register, AI saints](https://www.ncregister.com/features/chatting-with-ai-saints), [New Polity, "Delete Magisterium AI"](https://newpolity.com/blog/delete-magisteriumai), [EWTN Vatican](https://ewtnvatican.com/articles/chatting-with-ai-saints-opportunity-or-peril-6241)
- Text With Jesus and AI Jesus: [App Store](https://apps.apple.com/us/app/text-with-jesus/id6446922759), [Google Play](https://play.google.com/store/apps/details?id=app.textwith.jesus&hl=en_US), [Fox Business](https://www.foxbusiness.com/technology/text-jesus-app-draws-thousands-creator-says-ai-can-help-people-explore-scripture), [Today](https://www.today.com/news/religious-chatbot-apps-rcna243671), [Futurism](https://futurism.com/christians-jesus-christ-ai)
- Hello History: [App Store](https://apps.apple.com/us/app/hello-history-ai-chat/id1659654111), [OpenTools](https://opentools.ai/tools/hello-history)
- Free church-father bots: [othergospels.com/chat](https://othergospels.com/chat/), [patristics.info](https://patristics.info/apostolic-fathers-chatbot.html), [Medium](https://medium.com/thesacredfaith/using-ai-to-bring-the-early-church-to-the-modern-age-7b434ec84b5c)
- Barna/Gloo AI trust: [The Register](https://www.theregister.com/ai-ml/2026/05/21/deus-ex-machina-half-of-us-christians-trust-ais-spiritual-advice/5244371), [Religion Unplugged](https://religionunplugged.com/news/2026/5/21/new-study-christians-trust-ai-for-spiritual-growth), [Barna 2026 trends](https://www.barna.com/research/state-of-the-church-2026-trends/); deconstruction: [Barna](https://www.barna.com/trends/ex-christians-deconstructing/)
- ChatGPT payers: [TechCrunch](https://techcrunch.com/2026/02/27/chatgpt-reaches-900m-weekly-active-users), [Digital Information World](https://www.digitalinformationworld.com/2026/02/openai-reports-900m-weekly-chatgpt.html)
- Conversion benchmarks: [RevenueCat State of Subscription Apps 2026](https://www.revenuecat.com/state-of-subscription-apps), [Forasoft](https://www.forasoft.com/blog/article/app-revenue-potential)
- Church media pricing: [RightNow Media pricing](https://www.rightnowmedia.org/us/pricing), [FORMED parish example](https://stjosephbogota.org/formed-subscription/), [Wondrium review](https://kindlepreneur.com/wondrium-review/), [Ligonier Connect](https://www.ligonier.org/posts/ligonier-connect-announces-unlimited-access-plan)
- JustAnswer: [FTC press release](https://www.ftc.gov/news-events/news/press-releases/2026/01/ftc-sues-justanswer-deceiving-consumers-enrolling-costly-recurring-monthly-subscription)
- Reading behaviour: [NN/g, How little do users read?](https://www.nngroup.com/articles/how-little-do-users-read/)
- Van Westendorp sample sizes: [Wikipedia](https://en.wikipedia.org/wiki/Van_Westendorp%27s_Price_Sensitivity_Meter), [5 Circles](https://www.5circles.com/van-westendorp-pricing-the-price-sensitivity-meter/)

Repo and scratch [P]: `Build/Ministry/Features/Access-Monetization/Decision-Log.md`, `Open_Gaps_Tracking.md`; scratchpad `sample3.json`, `run15.json`, `run15.log`; `engine/api/config.py` lines 109-113; `cic-website/about.html`, `support.html`, `traditions/alexandria-catechetical.html` line 388; `cic-poc/frontend/src/components/SourceList.tsx` and siblings (existence only); `Build/Ministry/Marketplace/CiC_Marketplace_Landscape_Scan_V0_1.md`; `Build/Ministry/Funding/CiC_Org_Funding_Decision_Log.md` (2% projection pending real data).
