**Premised on the retired cic-poc app.** The conclusion (do not migrate provider) stands; the figures do not. Current basis: `engine/m8/`.

---

# LLM Provider & Cost Options — what the September price change actually does, and what leaving Anthropic would cost

**Date:** 2026-08-09
**Question from Mark:** "With Sonnet prices increasing 50% next month it makes Church in Conversation too expensive to run the conversations. What other tools can I use and what would be involved to transfer over to Gemini, ChatGPT or other more affordable models?"

**Method:** No live API calls. Every dollar figure reprices the project's own committed measurement — `Ministry/Technology/Pass2/baselines/cost_baseline_2026-07_raw.jsonl`, 689 logged calls across four real conversations — at each provider's published rates. Reproducible: `python3 Ministry/Technology/Pass3/provider_repricing.py`. Tags: **[M]** measured, **[E]** estimated (measured token shape × published pricing), **[S]** speculative.

---

## 1. The premise needs one correction before any decision rests on it

Two things are true and they pull in opposite directions.

**The 50% is real, on the rate.** Claude Sonnet 5 launched at *introductory* pricing of $2/$10 per MTok, published from the start as running through 2026-08-31. On September 1 it reverts to Sonnet's standard $3/$15 — the same rate Sonnet 4.5 and 4.6 have always charged. Input, output, cache writes and cache reads all move by exactly 1.5×.

**But the bill does not move 50%, and the plan already assumed the higher number.**

- **The bill moves +30%, not +50%.** [M] 30% of this app's spend is Haiku 4.5 classifier calls, which are completely unaffected. Repricing the measured baseline: **solo +29.7%, Table +31.4%.**
- **The plan of record was already priced at $3/$15.** `Ministry/Technology/Pass3/cost_floor_model.py` (2026-07-30) has `"claude-sonnet-5": (3.00, 15.00, 3.75, 0.30)` hardcoded in its `PRICING` dict. Every figure it produced — $1.61/hr solo, $4.14/hr Table current; ~$1.35/$2.08 after the stacked moves — is **already a post-increase figure.** Nothing in the cost plan needs re-deriving because of September 1.

What actually changes on September 1 is that the bills Mark *sees* stop being 24% cheaper than the bills the plan *predicted*. That is a real and unwelcome thing. It is not a new problem — it is the arrival of the problem Pass 3 already documented and did not solve.

| [M] measured baseline, dead code excluded | Solo | Table (3 worlds) |
|---|---|---|
| At intro rates (what has been billed) | $1.18/hr | $3.00/hr |
| From September 1 | $1.53/hr | $3.95/hr |
| Change | **+29.7%** | **+31.4%** |
| Stated target band | $0.25–1.00/hr | $0.25–1.00/hr |

The honest framing: **this project was already outside its own cost target at intro pricing.** September 1 widens a gap that was already there. That matters, because it means "switch provider to absorb the increase" is aiming at the wrong number — absorbing 30% still leaves you outside the band.

---

## 2. Where the money actually is

[M] From the measured baseline, with the known-dead `retrieval_filter_*` calls excluded:

- **Generation — `get_llm()`, 76 calls — is 70% of the bill.**
- **Classifiers — `get_monitoring_llm()`, 353 calls on Haiku 4.5 — are 30%.**

Within generation: uncached input 52%, cache write 20%, cache read 13%, **output only 15%.**

Two consequences, both load-bearing:

1. **A provider swap that touches only `get_llm()` captures ~all of the available saving.** The classifier tier is already on the cheapest sensible model; nothing on any provider's menu meaningfully beats Haiku 4.5 for a call that returns one word.
2. **33% of generation cost is prompt-cache mechanics.** That is not incidental — it is the direct result of deliberate engineering (`_cached_system_message`, `_cached_adjudication_message`, the `table_discourse` breakpoint split). **That engineering is Anthropic-shaped and does not port.** Section 4 returns to this; it is the single most underestimated line in any migration estimate.

---

## 3. Every candidate, same measured token shape

[E] Generation tier swapped; classifiers held on Haiku 4.5 throughout. Total bill for the whole measured baseline:

| Generation model | Total | Solo $/hr | Table $/hr | vs. Sonnet 5 (Sep 1) | Work to adopt |
|---|---|---|---|---|---|
| Sonnet 5 (Sep 1) | $2.84 | 1.53 | 3.95 | — | none (status quo) |
| Sonnet 5 (intro, today) | $2.18 | 1.18 | 3.00 | −23.4% | expires Aug 31 |
| Opus 5 | $4.17 | 2.23 | 5.83 | +46.7% | none |
| **Haiku 4.5** | **$1.51** | **0.83** | **2.06** | **−46.7%** | **one config line** |
| Gemini 3 Pro | $2.16 | 1.18 | 2.96 | −23.8% | full migration |
| Gemini 3 Flash | $1.18 | 0.65 | 1.58 | −58.5% | full migration |
| GPT-5.6 Terra | $2.22 | 1.20 | 3.05 | −22.0% | full migration |
| GPT-5.6 Luna | $0.99 | 0.55 | 1.31 | −65.3% | full migration |

**The finding that should drive the decision:**

> **Gemini 3 Pro (−24%) and GPT-5.6 Terra (−22%) are both *worse deals than Haiku 4.5* (−47%), which requires no migration at all.**

The peer-tier competitors — the ones you'd reach for if the worry is that a smaller model can't hold the Representative's voice — save *less* than a one-line config change, while costing weeks of engineering and a full revalidation. They are strictly dominated. Migrating to Gemini 3 Pro or GPT-5.6 Terra to save money is not a close call; it's a mistake.

Only two options beat Haiku 4.5: **Gemini 3 Flash (−59%)** and **GPT-5.6 Luna (−65%)**. Both are bottom-tier models. Which puts the real decision in sharp focus, and it is not a provider decision at all:

**The question is not "which company." It is "can a small model hold a Representative?" Pass 3 already asked that question, and deliberately refused to answer it for you.** From `cost_floor_model.py` Step 7, on the Haiku option:

> *`_HOW_YOU_ENGAGE` 4,094 est tokens; `REACTIVE_TURN_GUIDANCE` 2,629 est tokens → 55 distinct prohibitive constructions the model must hold at once ("do not" ×33, "never" ×9, "stop and" ×4), plus 7 worked WRONG/RIGHT example pairs for failure modes that are subtle by construction… This is dense negative-constraint instruction-following over long context. It is the capability axis on which a smaller model degrades first, and the three real-time blocking checks do NOT cover any of it… A tier failure is therefore spoken to the participant before anything catches it.*

That warning applies with **more** force to Gemini 3 Flash and GPT-5.6 Luna than to Haiku 4.5, because they'd also be losing whatever prompt-adherence tuning the current prompts were empirically shaped against across Pass 2's 76 batteries.

### Two corrections to the headline table

**[E] Gemini's cache storage charge.** Anthropic charges a cache write and nothing more; the prefix then sits free for its TTL. Gemini's *explicit* context cache additionally bills storage per MTok per hour — $4.50 (Pro) / $1.00 (Flash). This app parks a measured **15,211-token prefix per representative** at `ttl="1h"`:

- Gemini 3 Pro: **$0.068 per representative per cached hour** → **$0.21 for a 3-world Table over an hour, charged even if nobody speaks.**
- Gemini 3 Flash: $0.015 → $0.046 for the same.

It doesn't overturn the ranking (~1–4% of a Flash session, 5–15% on Pro), but it means Gemini's headline rate flatters it — and it **penalises exactly the slow, contemplative pacing this project says it wants.** Gemini's *implicit* cache has no storage charge but no hit guarantee either, which is the worse trade for a prompt that has been deliberately engineered to be byte-stable.

**[S] Tokenizer.** Every count above is a Sonnet-5-tokenizer count, and Anthropic states that tokenizer emits ~30% more tokens for the same text than its predecessor. Gemini and OpenAI tokenize this prose differently and generally more compactly, so a straight token-for-token reprice probably *understates* their advantage. At −20% tokens, Gemini 3 Flash lands at −61% and Luna at −66%. **Unvalidated in either direction.** One hour of work settles it — run the actual permanent prompts through each provider's own tokenizer — and no figure here should be quoted to anyone outside the project until that's done.

---

## 4. What a migration would actually involve

The `AWS_BEDROCK_SETUP.md` estimate ("four call sites branch on `settings.llm_provider`") is accurate as far as it goes, and it is the smallest part of the job. Full inventory:

**Tier 1 — the easy part, genuinely small (a day)**
- `app/config.py:54` — `Literal["anthropic", "openai"]` gains a value; add per-provider key/region settings.
- Four constructor sites: `graph/nodes.py:197` (`get_llm`), `graph/nodes.py:276` (`get_monitoring_llm`), `rag/retriever.py:84`, `rag/story_retriever.py:55`. These are the only four places in the codebase that read `settings.llm_provider`. Worth collapsing into one factory while in there.

**Tier 2 — the part that gets underestimated (1–2 weeks)**
- **Prompt caching does not port.** Four sites build Anthropic-shaped `cache_control` blocks — `nodes.py:1328`, `:1333`, `:2152`, `repair_classifier.py:254` — and **none of them is guarded by a provider check.** They run unconditionally. On Gemini, explicit caching is a separate `cachedContents` resource with its own lifecycle, TTL management and storage billing — a different architecture, not a different field name. On OpenAI, caching is automatic and prefix-based, so the careful two-breakpoint split in `_cached_system_message` (static prompt / reactive guidance / dynamic context) becomes meaningless and has to be re-reasoned. **33% of generation cost lives in this machinery.** A migration that ports the models but not the caching doesn't save 59% — it can easily save nothing.
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

## 5b. Correction — logged same day, before anything was acted on

**Two things in the first version of section 6 were wrong, and both mattered.** Mark asked for step 1 to be executed; verifying the code before deleting anything is what surfaced them.

**The dead `retrieval_filter_*` saving was already banked, not available.** S3.4 (Pass 1 R6) had already replaced the batched relevance vote with the local cross-encoder. The functions that made those calls — `evaluate_batch`, `_run_batch`, `partition_tier1_short_circuit` in `app/rag/batch_evaluate.py` — had been sitting **uncalled** in the file ever since; `app/rag/pipeline.py` imports only `Candidate`, `_evaluable_negative_condition` and `evaluate_negative_conditions`, and never imported the others. The calls stopped being made at S3.4. They appear in the committed baseline only because that log predates the rewiring.

This was a misreading on my part, not an error in the cost model. `cost_floor_model.py`'s Step 1 is headed *"dead code out, **live path in**"*, and its "TRUE CURRENT" line already means "what the code costs today." I read an accounting adjustment as a to-do.

**The magnitude was also wrong.** The −33% came from dividing against the wrong baseline. Correctly: the dead calls were **15.6%** of the measured run; net of the live `negative_condition` call that replaced them (+$0.0828), the already-realised saving is **~11%**.

**What was actually done, 2026-08-09:** the three uncalled functions deleted (115 lines), plus `TIER1_SHORT_CIRCUIT_RANK`. Verified: the file compiles, and every name `pipeline.py` imports still exists. Two stale docstrings corrected in the same pass — `retrieval_eval/run_eval.py`, which described the pre-S3.4 pipeline and named functions that no longer exist, and `usage_logging.py`, which still advertised the retired labels. **Dollar effect: zero.** This is hygiene, and it removes a misleading label from the codebase so the next cost reading can't repeat the mistake.

**Corrected position, per solo hour at September rates:**

| | $/hr | |
|---|---|---|
| [M] Committed baseline, as measured July | ~$1.81 | |
| [E] **True current — what the code costs today** | **~$1.61** | already banked |
| [E] + A1/A3 lossless + B1/B2 (the 20% budget) | ~$1.42 | −12% available |
| [E] same, generation on Haiku 4.5 | ~$0.63 | −61% |
| [E] same, generation on Gemini 3 Flash | ~$0.55 | −66% |

**What this changes about the recommendation:** the sequence below is unchanged in order, but step 1 is now done and was worth nothing, so **there is no large no-risk saving left on the shelf.** The remaining Anthropic-side tuning is worth ~12%, worth doing, and not the answer. That makes the Haiku decision more load-bearing than section 6 originally implied, not less — it is now the *only* move that reaches the target band.

*Reconciliation item — **now resolved, against this analysis.** Every figure above was re-derived on 2026-08-09 as a result, which is why they differ slightly from the version first issued.* This analysis originally priced cache writes at the 1-hour rate (2.0×) because `_cached_system_message` sets `ttl="1h"`; `cost_floor_model.py` and `scripts/cost_baseline_runner.py` both price them at the 5-minute rate (1.25×). The committed run notes settle it — `cost_baseline_2026-07_run_notes.md` note 2 records a **330-second pause expiring the cache** (C3 turn 5 cache_read 15,737 → turn 6 cache_read 0, full prefix re-paid), and only a 5-minute TTL does that. The baseline's cache counts are 5-minute counts and are now priced at 1.25× here too. The other two tools were right. Cross-check that now passes and did not before: this analysis's generation token mix (52% uncached input / 15% output) matches `cost_floor_model.py`'s own Step 2 (52% / 14%).

**The 1h TTL question is also settled — there was never a contradiction.** Commit `1d8e952` (2026-08-02) bumped the three `cache_control` sites from 5m to 1h as Item 1 of `CiC_Cost_Reduction_Build_Scope_2026-08-02.md`, backed by a Funding Strategy feasibility study measuring a **reflective-pace (6 turns/hr)** 1:1 conversation from $0.77/hr to $0.50/hr on that change alone. `cost_floor_model.py`'s A2 said precisely this: a net loss at the measured fast pacing, but *"it flips positive as soon as real contemplative pacing pushes pauses past 1.6×."* The two agree — they answer the question at two different pacings.

**What that leaves open is a basis question, and it is bigger than the TTL.** This analysis and `cost_floor_model.py` both price per hour at **30 turns/hr solo, 24 Table**. The cost-reduction scope and the funding model price at **6 turns/hr reflective**. Those denominators differ by 4–5×, so a `$/hr` figure from this memo and a `$/hr` figure from the funding model **are not the same unit and must not be compared directly.** Whichever pacing the $0.25–1.00/hr target band was actually set against decides whether this app is in band today. Worth settling before anyone declares success or failure against that band — including in section 6 below, whose figures are all at the faster pacing.

---

## 6. Recommendation

**Do not migrate providers. Not yet, and probably not to Gemini or OpenAI at all.** Not because Anthropic deserves loyalty — because the arithmetic says the peer-tier competitors save less than a config flip you already have available, and the sub-tier competitors carry the same quality risk as Haiku 4.5 while also costing weeks of work and voiding Pass 2's entire evidence base.

Sequenced by ratio of saving to risk:

1. ~~**Delete the dead `retrieval_filter_*` calls.**~~ **Done 2026-08-09 — and worth $0.** See section 5b: the saving was already banked at S3.4; only uncalled code remained. Corrected magnitude was ~11%, not −33%, and it was realised before this analysis began.
2. **Route through Bedrock to spend the $200 AWS credit.** Buys 4–6 months of runway at zero quality risk. Verify 1h TTL for Sonnet 5 first.
3. **Apply the Pass 3 lossless + 20%-budget moves (A1, A3, B1, B2, B3).** [E] to ~$1.42/hr solo.
4. **Run the Haiku 4.5 quality test Pass 3 asked for.** Re-run the S4.3 blind-graded battery with Haiku-generated Representative turns against the same graders, plus the safety batteries. It needs a live key and nothing else. **This is the decision gate** — it settles the only question that matters, and it settles it for *every* cheap-model option at once, because it's testing the capability axis, not the vendor.
5. **If Haiku passes:** take it. −47%, one config line, no migration, evidence base intact. Combined with steps 1–3, ~$0.63/hr solo — inside the target band.
6. **Only if Haiku fails on quality *and* Gemini 3 Flash demonstrably passes the same battery** does migration become rational. That is a real possibility, not a rhetorical one — but it has to be earned with the same evidence, and the migration cost then has to be paid with eyes open.

**Do first, this week, regardless of everything above:** confirm the Anthropic Console spending limit is set. Per the 2026-07-21 decision log, no per-visitor identity cap is active (Supabase deliberately off), so the console limit is the actual backstop — and a 30% rate change with no ceiling set is the scenario worth ruling out before September 1.

---

## 7. The question — answered 2026-08-09

**Mark's answer, verbatim: "im ok with a cheaper and a small drop after 15 turns."**

Recorded as a real decision, and it settles the gate in advance: **an ambiguous Haiku result is a PASS, not a re-run.** The battery is now a measurement of *how large* the drop is, not a yes/no on whether any drop is tolerable. That is a meaningful narrowing — it means step 4 can no longer stall.

Three things follow, and the third is the one that needs Mark's eye:

1. **Take Haiku 4.5 unless the battery shows something worse than "small."** The decision reverses the default: previously an ambiguous result meant hold Sonnet; now it means ship Haiku. What still stops it is a *category* failure, not a frequency one — a relational-safety or acute-distress miss is not a "small drop," and that battery is a separate pass/fail with no tolerance band. Worth being explicit that "cheaper is fine" was said about voice and constraint adherence, not about the distress path.
2. **The battery still has to run, and it now has a threshold to measure against.** "Small" needs a number before the run, not after — otherwise whatever comes back gets read as small. Proposal: ≤1 constraint drop per 15 Representative turns on the S4.3 blind-graded shape, judged by the same graders, with zero safety-category misses. If it lands there, take Haiku and stop spending on this question.
3. ~~**A known defect rate should reach the participant-facing copy.**~~ **Raised, and decided against — 2026-08-09.** Mark: *"we don't need a notice, we will use the best tool we can afford, if there is feedback that we are having problems we will look at it, but no reason to get them looking for things they wouldn't notice."* Closed; not to be re-opened in downstream threads.

   **Correction, same day:** I initially read "feedback" as the written form and suggested confirming it was watched. Mark: *"i am not keeping pilot feedback in written form, i am interviewing people."* So the detection mechanism is **interviews**, and it needs no plumbing check.

   That does change one thing about the risk, and it is worth stating once without re-arguing the decision. Interviews detect what a participant **felt**. The Haiku risk Pass 3 described is specifically the class of failure a participant **would not notice** — a dropped negative constraint, a manufactured resolution, a borrowed image arriving several turns later. Nobody reports those in an interview; they report "it got a bit generic near the end," or nothing. So interviews are a good instrument pointed slightly away from this particular risk.

   The thing that closes that gap is not a notice and not a form — it is the **transcript-side detectors that already exist**: `check_manufactured_resolution`, `check_cross_world_vocabulary_drift`, `check_convergence` (all post-hoc), plus `length_ceiling_logging`. They are already written and already running. Reading them alongside the interviews costs nothing and catches the half of the risk the interviews structurally can't.

   **Separately, and this is a live-site issue rather than a quality one:** `cic-website/pilot-feedback.html` is linked from **every page footer**, from inside the app (`TheTable.tsx`), and from a sentence in `whats-next.html` that tells pastors and academics "the feedback form is how that reaches us." Its `<form>` posts to `action="mailto:info@churchinconversation.com"` — a mechanism that is unreliable across modern browsers and fails *silently* when it fails. So the site is actively promising a written channel that probably doesn't deliver and that nobody is reading. Not urgent, not a quality risk, and not mine to change unilaterally — but it should either be pointed at whatever the interview intake actually is, or quietly retired.

### The original question, retained for the record

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
