# LLM Provider & Cost Options — what the September price change actually does, and what leaving Anthropic would cost

**Date:** 2026-08-09
**Question from Mark:** "With Sonnet prices increasing 50% next month it makes Church in Conversation too expensive to run the conversations. What other tools can I use and what would be involved to transfer over to Gemini, ChatGPT or other more affordable models?"

**Method:** No live API calls. Every dollar figure reprices the project's own committed measurement — `Ministry/Technology/Pass2/baselines/cost_baseline_2026-07_raw.jsonl`, 689 logged calls across four real conversations — at each provider's published rates. Reproducible: `python3 Ministry/Technology/Pass3/provider_repricing.py`. Tags: **[M]** measured, **[E]** estimated (measured token shape × published pricing), **[S]** speculative.

---

## 1. The premise needs one correction before any decision rests on it

Two things are true and they pull in opposite directions.

**The 50% is real, on the rate.** Claude Sonnet 5 launched at *introductory* pricing of $2/$10 per MTok, published from the start as running through 2026-08-31. On September 1 it reverts to Sonnet's standard $3/$15 — the same rate Sonnet 4.5 and 4.6 have always charged. Input, output, cache writes and cache reads all move by exactly 1.5×.

**But the bill does not move 50%, and the plan already assumed the higher number.**

- **The bill moves +30%, not +50%.** [M] 29% of this app's spend is Haiku 4.5 classifier calls, which are completely unaffected. Repricing the measured baseline: **solo +30.3%, Table +31.9%.**
- **The plan of record was already priced at $3/$15.** `Ministry/Technology/Pass3/cost_floor_model.py` (2026-07-30) has `"claude-sonnet-5": (3.00, 15.00, 3.75, 0.30)` hardcoded in its `PRICING` dict. Every figure it produced — $1.61/hr solo, $4.14/hr Table current; ~$1.35/$2.08 after the stacked moves — is **already a post-increase figure.** Nothing in the cost plan needs re-deriving because of September 1.

What actually changes on September 1 is that the bills Mark *sees* stop being 24% cheaper than the bills the plan *predicted*. That is a real and unwelcome thing. It is not a new problem — it is the arrival of the problem Pass 3 already documented and did not solve.

| [M] measured baseline, dead code excluded | Solo | Table (3 worlds) |
|---|---|---|
| At intro rates (what has been billed) | $1.27/hr | $3.38/hr |
| From September 1 | $1.65/hr | $4.45/hr |
| Change | **+30.3%** | **+31.9%** |
| Stated target band | $0.25–1.00/hr | $0.25–1.00/hr |

The honest framing: **this project was already outside its own cost target at intro pricing.** September 1 widens a gap that was already there. That matters, because it means "switch provider to absorb the increase" is aiming at the wrong number — absorbing 30% still leaves you outside the band.

---

## 2. Where the money actually is

[M] From the measured baseline, with the known-dead `retrieval_filter_*` calls excluded:

- **Generation — `get_llm()`, 76 calls — is 71% of the bill.**
- **Classifiers — `get_monitoring_llm()`, 353 calls on Haiku 4.5 — are 29%.**

Within generation: uncached input 47%, cache write 28%, cache read 12%, **output only 13%.**

Two consequences, both load-bearing:

1. **A provider swap that touches only `get_llm()` captures ~all of the available saving.** The classifier tier is already on the cheapest sensible model; nothing on any provider's menu meaningfully beats Haiku 4.5 for a call that returns one word.
2. **40% of generation cost is prompt-cache mechanics.** That is not incidental — it is the direct result of deliberate engineering (`_cached_system_message`, `_cached_adjudication_message`, the `table_discourse` breakpoint split). **That engineering is Anthropic-shaped and does not port.** Section 4 returns to this; it is the single most underestimated line in any migration estimate.

---

## 3. Every candidate, same measured token shape

[E] Generation tier swapped; classifiers held on Haiku 4.5 throughout. Total bill for the whole measured baseline:

| Generation model | Total | Solo $/hr | Table $/hr | vs. Sonnet 5 (Sep 1) | Work to adopt |
|---|---|---|---|---|---|
| Sonnet 5 (Sep 1) | $3.14 | 1.65 | 4.45 | — | none (status quo) |
| Sonnet 5 (intro, today) | $2.39 | 1.27 | 3.38 | −23.7% | expires Aug 31 |
| Opus 5 | $4.62 | 2.42 | 6.61 | +47.4% | none |
| **Haiku 4.5** | **$1.65** | **0.88** | **2.30** | **−47.4%** | **one config line** |
| Gemini 3 Pro | $2.22 | 1.20 | 3.07 | −29.1% | full migration |
| Gemini 3 Flash | $1.24 | 0.67 | 1.68 | −60.6% | full migration |
| GPT-5.6 Terra | $2.28 | 1.22 | 3.16 | −27.4% | full migration |
| GPT-5.6 Luna | $1.04 | 0.57 | 1.42 | −66.7% | full migration |

**The finding that should drive the decision:**

> **Gemini 3 Pro (−29%) and GPT-5.6 Terra (−27%) are both *worse deals than Haiku 4.5* (−47%), which requires no migration at all.**

The peer-tier competitors — the ones you'd reach for if the worry is that a smaller model can't hold the Representative's voice — save *less* than a one-line config change, while costing weeks of engineering and a full revalidation. They are strictly dominated. Migrating to Gemini 3 Pro or GPT-5.6 Terra to save money is not a close call; it's a mistake.

Only two options beat Haiku 4.5: **Gemini 3 Flash (−61%)** and **GPT-5.6 Luna (−67%)**. Both are bottom-tier models. Which puts the real decision in sharp focus, and it is not a provider decision at all:

**The question is not "which company." It is "can a small model hold a Representative?" Pass 3 already asked that question, and deliberately refused to answer it for you.** From `cost_floor_model.py` Step 7, on the Haiku option:

> *`_HOW_YOU_ENGAGE` 4,094 est tokens; `REACTIVE_TURN_GUIDANCE` 2,629 est tokens → 55 distinct prohibitive constructions the model must hold at once ("do not" ×33, "never" ×9, "stop and" ×4), plus 7 worked WRONG/RIGHT example pairs for failure modes that are subtle by construction… This is dense negative-constraint instruction-following over long context. It is the capability axis on which a smaller model degrades first, and the three real-time blocking checks do NOT cover any of it… A tier failure is therefore spoken to the participant before anything catches it.*

That warning applies with **more** force to Gemini 3 Flash and GPT-5.6 Luna than to Haiku 4.5, because they'd also be losing whatever prompt-adherence tuning the current prompts were empirically shaped against across Pass 2's 76 batteries.

### Two corrections to the headline table

**[E] Gemini's cache storage charge.** Anthropic charges a cache write and nothing more; the prefix then sits free for its TTL. Gemini's *explicit* context cache additionally bills storage per MTok per hour — $4.50 (Pro) / $1.00 (Flash). This app parks a measured **15,211-token prefix per representative** at `ttl="1h"`:

- Gemini 3 Pro: **$0.068 per representative per cached hour** → **$0.21 for a 3-world Table over an hour, charged even if nobody speaks.**
- Gemini 3 Flash: $0.015 → $0.046 for the same.

It doesn't overturn the ranking (~1–4% of a Flash session, 5–15% on Pro), but it means Gemini's headline rate flatters it — and it **penalises exactly the slow, contemplative pacing this project says it wants.** Gemini's *implicit* cache has no storage charge but no hit guarantee either, which is the worse trade for a prompt that has been deliberately engineered to be byte-stable.

**[S] Tokenizer.** Every count above is a Sonnet-5-tokenizer count, and Anthropic states that tokenizer emits ~30% more tokens for the same text than its predecessor. Gemini and OpenAI tokenize this prose differently and generally more compactly, so a straight token-for-token reprice probably *understates* their advantage. At −20% tokens, Gemini 3 Flash lands at −63% and Luna at −68%. **Unvalidated in either direction.** One hour of work settles it — run the actual permanent prompts through each provider's own tokenizer — and no figure here should be quoted to anyone outside the project until that's done.

---

## 4. What a migration would actually involve

The `AWS_BEDROCK_SETUP.md` estimate ("four call sites branch on `settings.llm_provider`") is accurate as far as it goes, and it is the smallest part of the job. Full inventory:

**Tier 1 — the easy part, genuinely small (a day)**
- `app/config.py:54` — `Literal["anthropic", "openai"]` gains a value; add per-provider key/region settings.
- Four constructor sites: `graph/nodes.py:197` (`get_llm`), `graph/nodes.py:276` (`get_monitoring_llm`), `rag/retriever.py:84`, `rag/story_retriever.py:55`. These are the only four places in the codebase that read `settings.llm_provider`. Worth collapsing into one factory while in there.

**Tier 2 — the part that gets underestimated (1–2 weeks)**
- **Prompt caching does not port.** Four sites build Anthropic-shaped `cache_control` blocks — `nodes.py:1328`, `:1333`, `:2152`, `repair_classifier.py:254` — and **none of them is guarded by a provider check.** They run unconditionally. On Gemini, explicit caching is a separate `cachedContents` resource with its own lifecycle, TTL management and storage billing — a different architecture, not a different field name. On OpenAI, caching is automatic and prefix-based, so the careful two-breakpoint split in `_cached_system_message` (static prompt / reactive guidance / dynamic context) becomes meaningless and has to be re-reasoned. **40% of generation cost lives in this machinery.** A migration that ports the models but not the caching doesn't save 61% — it can easily save nothing.
- **⚠️ Corollary worth knowing now: the existing `openai` provider option is almost certainly broken today.** Those unconditional `cache_control` blocks get handed to `ChatOpenAI` whenever `LLM_PROVIDER=openai`. The `.env.example` still advertises `gpt-4o` / `gpt-4o-mini` — models from two generations back. **"We already support OpenAI" is a config value, not a working path.** Verifiable in ten minutes with `MOCK_LLM=false` and any key. Whatever else is decided, this should either be fixed or removed, because it currently reads as a fallback that isn't one.
- **`thinking={"type": "disabled"}`** (`nodes.py:203`, `:285`) is an Anthropic-only kwarg, and it is not cosmetic — it's the fix for a live-diagnosed bug where interleaved thinking blocks ate the `max_tokens` budget and truncated reactive turns mid-sentence. Every provider needs its own equivalent, and Gemini 3 Flash has thinking on by default and bills it as output.
- **`app/usage_logging.py`** reads `cache_creation_input_tokens` / `cache_read_input_tokens` — explicitly documented there as Anthropic-specific and outside LangChain's standardised shape. **On migration, cost visibility goes dark** — exactly the instrumentation gap that file was written in July to close.
- Content-block list handling (`main.py:344`, `nodes.py:1541`) needs per-provider verification.

**Tier 3 — the real cost, and it isn't engineering (4–8 weeks, [S])**

Revalidation. The prompts were not written in the abstract; they were shaped against measured failures across **76 probe batteries, 34 reviews, 114 gates, 11 safety reruns** and a blind-graded adjudicator battery. The relational-safety and frame-breaker mechanisms cleared live adversarial testing on a specific model. None of that evidence transfers to a different model. In particular:

- The safety batteries (`safety_rerun_s33` … `s47`) would need re-running in full — this is the acute-distress path, and it is not a place to accept an unmeasured regression.
- The S4.3 blind-graded battery would need re-running to establish that voice and negative-constraint adherence hold.
- The hard-ceiling regeneration rates (`nodes.py` `HARD_CEILING_WORLDS`) are per-model empirical constants. Desert already regenerates on 80% of turns [M] at ~24% of that conversation's cost. **A model with worse length adherence could regenerate more often and eat the entire per-token saving** — a cheaper model that regenerates twice as often is not cheaper.

That last point is the trap. Every figure in Section 3 assumes identical token shape. **A worse instruction-follower does not produce the same token shape.**

**What does *not* need touching, in either direction:** embeddings are local HuggingFace (`rag/embeddings.py`) — no API cost, provider-independent. FAISS, the WRS record layer, retrieval, and the entire frontend are all model-agnostic.

---

## 5. Other tools worth naming

**Amazon Bedrock — the immediate, zero-risk one.** `cic-poc/AWS_BEDROCK_SETUP.md` records **$200 of AWS credit, barely touched.** Bedrock serves the same Claude models at list price, and 1-hour prompt-cache TTL — which this app depends on — is now GA there. Routing through Bedrock spends credit instead of cash, at **zero quality risk and zero prompt change**. That is roughly 4–6 months of the current $100–150/month API ceiling, for a few days of Tier-1-only integration work (`ChatBedrockConverse` from `langchain-aws` is a drop-in for the LangChain interface). Two things to verify first: 1h TTL confirmed for Sonnet 5 specifically (the GA announcement named 4.5-series models), and global vs. regional endpoints (regional carries a 10% premium).

**Batch API — 50% off, and there is a real use for it here.** Not for live conversation, but Pass 3's answer-bank build is precisely a batch job, and it already assumes the discount.

**OpenRouter / LiteLLM — skip.** Both are provider-abstraction layers, and **LangChain already is that layer** — which is why the four constructor sites are the easy part. Neither solves the caching problem, which is the actual work. OpenRouter adds a margin and weakens control over Anthropic's 1h cache TTL.

**Self-hosting an open model — not now.** A GPU capable of serving a 7k-token system prompt at conversational latency costs more per month than the entire current API bill, and the instruction-following axis Pass 3 flagged is where open models are weakest.

**Separately: the $250/month development subscription.** The decision log (2026-07-21) records ~$357–407/month total, of which **$250 is Mark's Claude subscription for building, not the app's API spend at all.** That single line is larger than everything this memo discusses. It is a build-phase cost that the log already expects to shrink. If the pressure is on the monthly total rather than on unit economics specifically, **that line is the larger lever, and it is not a provider decision.** Worth being explicit about which of the two is actually biting.

---

## 6. Recommendation

**Do not migrate providers. Not yet, and probably not to Gemini or OpenAI at all.** Not because Anthropic deserves loyalty — because the arithmetic says the peer-tier competitors save less than a config flip you already have available, and the sub-tier competitors carry the same quality risk as Haiku 4.5 while also costing weeks of work and voiding Pass 2's entire evidence base.

Sequenced by ratio of saving to risk:

1. **Delete the dead `retrieval_filter_*` calls.** [M] −33%, no participant-visible change, no quality risk. **This is the single largest unambiguous win available and it is still not done.** It alone is larger than the September increase.
2. **Route through Bedrock to spend the $200 AWS credit.** Buys 4–6 months of runway at zero quality risk. Verify 1h TTL for Sonnet 5 first.
3. **Apply the Pass 3 lossless + 20%-budget moves (A1, A3, B1, B2, B3).** [E] to ~$1.42/hr solo.
4. **Run the Haiku 4.5 quality test Pass 3 asked for.** Re-run the S4.3 blind-graded battery with Haiku-generated Representative turns against the same graders, plus the safety batteries. It needs a live key and nothing else. **This is the decision gate** — it settles the only question that matters, and it settles it for *every* cheap-model option at once, because it's testing the capability axis, not the vendor.
5. **If Haiku passes:** take it. −47%, one config line, no migration, evidence base intact. Combined with steps 1–3, ~$0.63/hr solo — inside the target band.
6. **Only if Haiku fails on quality *and* Gemini 3 Flash demonstrably passes the same battery** does migration become rational. That is a real possibility, not a rhetorical one — but it has to be earned with the same evidence, and the migration cost then has to be paid with eyes open.

**Do first, this week, regardless of everything above:** confirm the Anthropic Console spending limit is set. Per the 2026-07-21 decision log, no per-visitor identity cap is active (Supabase deliberately off), so the console limit is the actual backstop — and a 30% rate change with no ceiling set is the scenario worth ruling out before September 1.

---

## 7. One question back

The mechanics above are answerable with measurement. This one isn't, and it decides step 4's meaning before the battery is ever run:

**If the Haiku battery comes back genuinely ambiguous — voice mostly holds, but it drops a constraint every fifteenth turn in a way no live guard catches — what do you want to happen?**

That is not a cost question. Pass 3 was explicit that the failure mode is *spoken to the participant before anything catches it* — someone sitting with a Representative, being told something the world's own sources don't support, with a citation panel beside it saying the project stands behind it. Against that, the honest options are: hold the more expensive model and go find the money; accept a measured, disclosed defect rate; or narrow the offering — fewer worlds, no Table — so the quality bar can be held at a lower total spend.

Worth naming plainly: this project's own convictions include **Trustworthy Transparency**. A cheaper model that fails quietly is the one outcome that costs something the budget can't measure. Knowing now which way you'd lean will make the battery result actionable instead of the start of another round.

---

## Appendix — sources

Pricing verified 2026-08-09.

- [Anthropic pricing (official)](https://platform.claude.com/docs/en/about-claude/pricing) — Sonnet 5 intro $2/$10 through 2026-08-31, $3/$15 from 2026-09-01; Haiku 4.5 $1/$5; Opus 5 $5/$25; 1h cache write 2×, cache read 0.1×; tokenizer note (~30% more tokens on 4.7-and-later).
- [Amazon Bedrock 1-hour prompt caching GA](https://aws.amazon.com/about-aws/whats-new/2026/01/amazon-bedrock-one-hour-duration-prompt-caching)
- Gemini rates — `ai.google.dev` is blocked by this environment's egress proxy; taken from agreement across [BenchLM](https://benchlm.ai/google/api-pricing), [CostGoat](https://costgoat.com/pricing/gemini-api), [PricePerToken](https://pricepertoken.com/pricing-page/model/google-gemini-3-flash-preview). **Confirm against Google's own page before committing.**
- OpenAI rates — `platform.openai.com` likewise blocked; taken from agreement across [BenchLM](https://benchlm.ai/openai/api-pricing), [aipricing.guru](https://www.aipricing.guru/openai-pricing/), [Finout](https://www.finout.io/blog/gpt-5.6-pricing-2026-sol-terra-and-luna-tiers-explained); rates are post the 2026-07-30 cut (Terra −20%, Luna −80%). **Confirm against OpenAI's own page before committing.**

Internal: `Ministry/Technology/Pass3/cost_floor_model.py`, `Ministry/Technology/Pass3/provider_repricing.py`, `Ministry/Technology/Pass2/baselines/cost_baseline_2026-07_raw.jsonl`, `Ministry/Funding/CiC_Org_Funding_Decision_Log.md` (2026-07-21), `cic-poc/AWS_BEDROCK_SETUP.md`.
