# Church in Conversation — What It Actually Costs to Go Live

**V0.1 · 2026-07-21 · Funding Strategy & Execution thread**

**What this is:** a real, current-priced answer to "how much do I need to make this go live" —
built after directly inspecting the live website, the `cic-poc` codebase, and the actual
deployment configuration, not from an old planning estimate. Good news up front: **this is the
cheap part.** The expensive conversations this thread has been having (scholarly review, entity
structure, growth capital) are all real — but going live itself is a small, boundable number.

---

## Part A — What's actually built (more than the earlier budget models assumed)

Checked directly, not taken on faith:

- **The marketing/Atlas site is already live** at churchinconversation.com — a genuinely
  impressive 178-movement census across ten eras, five worlds fully open for conversation
  (Chloe/House-Churches, Papnoute/Desert, Theon/Alexandria, Mar Yausep/Syriac, Albina/Bethlehem
  Circle), confidence-labeled, four more chosen for construction. This is real, hosted, working.
- **The conversational app (`cic-poc`) is fully built but not yet hosted anywhere.** The
  website's own "Launch a Conversation" button says *"opening here directly as soon as hosting is
  finished"* — that sentence is the literal, entire gap between where you are and going live.
- **The feature set is substantially bigger than earlier budget models assumed:** multi-
  Representative "Living Table" conversations (several worlds speaking together, not just 1:1
  interviews), a frame-breaker classifier and a relational-safety/distress-handling mechanism
  (both **live-tested this week, 19/20 clean, real API calls, all 5 worlds**), drift/dominance/
  convergence/question-stacking quality checks, a soft 60-turn-per-conversation cap (the current
  cost backstop), and model routing already implemented in code — full responses run on
  Sonnet, all the classifiers and monitoring run on the much cheaper Haiku 4.5. Direct Anthropic
  API is confirmed as the path (Bedrock was dropped). Embeddings for retrieval run locally
  (HuggingFace/sentence-transformers) — **no separate API cost there.**
- **It's already packaged to deploy as one service** — a single Dockerfile builds the frontend
  and serves it alongside the backend from one process, one port. Render, Railway, and Fly.io all
  pick it up automatically by pointing at the `cic-poc/` folder. This is not a build task anymore
  — it's a deploy-and-configure task.
- **Two honest open items, neither a launch-blocker, both worth knowing:** (1) a rare
  content-isolation defect (one live response briefly contained unrelated content) — root cause
  not yet found, but now fully traceable if it recurs (every LLM call is logged with a request
  ID). (2) a de-escalation timing question from this week's safety test — one narrow case worth a
  quick follow-up retest. **The core safety mechanism itself — the thing that actually matters
  for going live to the public — already passed live, adversarial testing this week.**

---

## Part B — What going live actually costs

**Two line items only. Everything else you need (the domain, the marketing site, the built app)
is already paid for or already free.**

### 1. Hosting — a small, flat, predictable cost

| Platform | Cost | Note |
|---|---|---|
| **Render — Starter plan** | **$7/month** | Flat, predictable, simplest to set up. **Recommended** for a first deploy. |
| Fly.io | ~$2–15/month | Cheaper at the floor, usage-billed — less predictable for a first-time deploy, more moving parts to configure correctly. |

**Recommendation: Render Starter, $7/month.** Simple, flat, one service, matches exactly what
the Dockerfile is already built for.

### 2. Anthropic API spending — the real variable cost, and the one that needs a ceiling set

This is the number that matters, and it needs one honest caveat before the figure: **there is
currently no per-visitor limit on how many separate conversations someone can start** — the
account/sign-in layer (Supabase) is built but deliberately off for this stage (Mark's own
decision, small audience, informal access control). The only backstop live right now is the
**60-turn cap per single conversation.** That's a real, working safety net against one runaway
session — it does **not** cap total visitors or total conversations across everyone who finds the
link.

**Real, converged cost basis** (established and cross-checked twice already in this project — the
System Hub's per-session model and this project's own packet unit economics agree): roughly
**$0.28–1.10 per user per month** at light-to-heavy usage, or **$0.20–0.35 per typical
conversation.** **One honest adjustment for the full feature set:** a Living Table round where
2–3 Representatives each respond costs more than a single 1:1 interview turn — call the realistic
per-conversation range **$0.30–0.75**, leaning conservative rather than optimistic, until real
usage confirms it.

**What this means practically:** the actual tool for controlling risk isn't a bigger number, it's
**the Anthropic Console spending limit** — a hard, settable ceiling that stops calls once crossed
(the same mechanism already planned in this project's own infrastructure decisions). Given the
per-conversation cost above, a **$100–150 initial ceiling** covers somewhere between roughly
**150 and 500 real conversations** — genuinely enough room for organic/direct-link traffic to
actually use the site, while keeping worst-case exposure small and known in advance.

### Total minimum to flip the switch

| Item | Cost |
|---|---|
| Hosting (Render Starter, first month) | $7 |
| Anthropic API spending ceiling (set on the Console, not all spent immediately) | $100–150 |
| Domain | $0 — already owned |
| Marketing site | $0 — already live |
| Supabase | $0 — not needed at this stage |
| **Minimum to go live** | **≈ $110–160** |
| **Ongoing, after that** | **~$7/month hosting** + actual API usage (bounded by the console limit you set, adjustable as real traffic tells you what it actually is) |

**This is genuinely small next to everything else this thread has been modeling.** Going live is
not the expensive part of this project — it's the cheapest concrete step available right now.

---

## Part C — "AI tool access money," clarified: two separate accounts, not one number

Mark confirmed this is a **Claude subscription** (Max-tier range, given the price point and
"access to Fable" — a subscription perk, not an API-billing one) — currently **$200/month**,
budgeting **$250/month** going forward. This is his personal **dev-tool cost**: what lets him
keep building, coding, and using Fable, billed flat regardless of site traffic. **It is a
completely separate account and bill from the pay-per-token `ANTHROPIC_API_KEY` that powers
`cic-poc` itself** (Part B above) — the two don't offset each other; both run at once once the
app is live. Mark's own expectation, worth holding onto: the subscription line should shrink once
initial development eases — it's a build-phase cost, not a permanent operating one, unlike
hosting and live-API spend.

### Total monthly, combined

| Line | Cost |
|---|---|
| Claude subscription (dev/tool access — Mark's own planning figure) | **$250/month** |
| Hosting (Render Starter) | $7/month |
| Live-app API spending ceiling (visitor conversations) | $100–150/month to start |
| **Total monthly, at launch** | **≈ $357–407/month** |

The hosting and live-API lines are the product's true ongoing operating cost; the $250 subscription
is Mark's own working budget on top of that, for as long as he's still actively building.

---

## Part C.1 — Capacity at a $500 total budget, and what changes at a $125 fixed cost

**At $500/month total, fixed costs first:** $250 (subscription) + $7 (hosting) = $257 fixed,
leaving **≈$243/month** actually available for real visitor conversations (the only line that
scales with people, not with Mark's own tool use).

**At a $125/month fixed cost** (a lower subscription tier + hosting) instead of $257, **≈$375/month**
becomes available for real conversations — meaningfully more room, same $500 total.

| | At $243 variable (fixed = $257) | At $375 variable (fixed = $125) |
|---|---|---|
| Conversations/month (range: heavier Table use → lighter interview-mostly use) | ~324–810 | ~500–1,250 |
| Unique people (at ~1.5 conversations/person average) | ~215–540 | ~330–830 |
| Hours of real engagement (at ~15–25 min/conversation) | ~80–340 hrs | ~125–520 hrs |

**Same honest caveats as before:** ranges, not points — average conversation depth is genuinely
unknown pre-launch, and the 60-turn message cap is what keeps any single conversation from
blowing past a bounded cost. Recalibrate against real Anthropic Console data after the first
1–2 weeks live.

## Part C.2 — After a good first month: how to start covering API costs, fastest first

**The goal stated plainly: cover real, modest API costs — not build the full revenue
architecture yet.** Here's the ladder, ordered by how fast each rung can actually go live, not by
theoretical revenue ceiling:

1. **A simple voluntary support link — days, not weeks.** A Stripe Payment Link or a Ko-fi/Buy
   Me a Coffee page, placed after a conversation ends ("if this was worth something to you, help
   keep the Table open for someone who can't pay"). No accounts, no Supabase, no feature-gating —
   nothing in `cic-poc` needs to change. This is the fastest possible test of "will anyone pay
   anything," and it's fully compatible with the brand voice already decided (steward, not hero;
   tied to a concrete thing, not an abstract ask).
   - **Realistic expectation, using this project's own evidenced benchmark (Wikimedia's own
     stated 2% conversion — not an optimistic guess):** at 300–800 real people in a good first
     month, 2% converting at a modest $5–10 average gift is **~$30–160/month** — genuinely close
     to covering a modest live-API bill on its own, especially paired with even one or two larger
     one-time gifts from people who had a real, moving encounter.
2. **A recurring "Supporter" pledge via Stripe Checkout — a week or two.** Same no-gating
   simplicity as #1, but structured as a recurring monthly amount (e.g., $5–12/mo) rather than a
   one-off tip — Stripe handles the subscription billing itself; nothing in the app needs to
   check who's paid, since nothing is being gated yet. This turns occasional tips into a
   predictable monthly floor.
3. **Gate a real feature behind payment — a few weeks, real engineering.** This is where the
   already-built-but-off Supabase auth layer (`auth.py`, the session-cap rework) actually gets
   turned on and wired to subscription status — e.g., gating voice (if ever turned on) or higher
   session limits behind the paid tier, free tier still fully real and un-gated on the core
   encounter (per Article IV). Not a same-day fix; the right next step only once #1 or #2 shows
   real signal worth building infrastructure around.
4. **Institutional licenses — the real engine, but relationship-driven, not a switch to flip.**
   Churches/seminaries paying $1,200–5,000/yr (per the hybrid model already designed) is still the
   structurally strongest source once there's a story to tell — but it runs on the anchor-seminary
   outreach already underway, not on a week's engineering sprint.

**The honest sequencing:** run #1 immediately alongside the go-live launch — it costs nothing to
have in place and starts answering the real question (will people actually give something) with
real data instead of a model. Move to #2 if #1 shows real signal. Only build #3 once #1/#2 prove
there's something worth gating. #4 runs in parallel the whole time, on its own relationship
clock, regardless of how the online-giving rungs perform.

## Part C.3 — The actual ask copy: amounts and the "where this goes" language

**Suggested amounts (anchored, not open-ended) — evidence-based, not a guess:** a suggested
amount reliably outperforms a fully open "give what you want" ask (museum pay-what-you-wish
research found suggested/anchored asks running 15–25% higher per visitor than unanchored ones).
Tie the suggestion to the project's own real cost unit (~$1/user/month) so it's concrete, not
generic:

- **One-time:** suggest **$10**, offering $5 / $10 / $25 / other.
- **Recurring:** suggest **$8/month**, offering $5 / $8 / $15 / other.
- **The ask line itself, concrete and defensible** (a real calculation from the project's own
  unit cost, not an invented multiplier): *"$10/month keeps the Table open for ten more seekers
  who couldn't otherwise afford it."*

**"Where this goes" — the honest scope, correctly widened.** Mark's own catch, worth recording:
narrowing this to "covers hosting and API" would be just as inaccurate, in the other direction,
as an unqualified "100% of every dollar." Running this includes real infrastructure and,
eventually, real people — not only server costs. **Finalized language:**

> *"Contributions go toward the real cost of running and growing this — the technology, the
> people, and the work it takes — so it can stay free for everyone who needs it."*

This pairs with the concrete per-gift line above: the **ask line** states a true, calculable
unit-cost equivalence (a specific gift ≈ access for N seekers); the **"where this goes" line**
honestly describes the full, real operating scope (infrastructure and people, not narrowly
hosting) without promising literal 100%-segregated fund tracking Mark isn't committing to build.
Both are true at once, at their own level — neither overclaims narrow, neither overclaims total.

---

## Part D — What's left to actually do (yours, not mine)

1. **Create a Render account and a new Web Service**, root directory `cic-poc/` — this is a
   personal account-creation step, not something I can do on your behalf.
2. **Set two environment variables:** `ANTHROPIC_API_KEY` (yours) and `CORS_ORIGINS` (your live
   domain, e.g. `["https://churchinconversation.com"]`) — without the second, every real browser
   request gets blocked.
3. **Set the Anthropic Console spending limit** at the ~$100–150 figure above before pointing
   real traffic at it.
4. **Point the website's "Launch a Conversation" button** at the new live URL once it's up —
   this is the one piece of website code waiting on hosting to exist.
5. **Optional but worth 10 minutes:** the de-escalation timing retest flagged above, before wide
   traffic arrives — low cost, closes the one open safety question from this week's testing.

---

*Grounded in direct inspection of `cic-poc/` (Dockerfile, config.py, graph/nodes.py,
message_cap.py), the live site at churchinconversation.com, the Task Board (2026-07-21), and
current Render/Fly.io pricing verified live. Unit-economics figures inherited and cross-checked
against the System Hub session's per-session model and this project's own packet, not re-derived
from scratch.*
