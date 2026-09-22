**cic-poc;** the Answer Bank recommendation herein was rescinded 2026-08-02 (Funding-Strategy Decision-Log). Superseded by the M8 engine.

---

# CiC Cost-Reduction Feasibility Study

**2026-08-02 · Funding Strategy thread · codebase-grounded, measured where measurable**

**Status: research to react to, not a decision.** Nothing here converges until Mark and Susan say so.

## What changed since the prior study

Three things in the prior study don't survive contact with the committed measurement artifact (`Archive/Technology-Pass2-2026-08/Pass2/baselines/cost_baseline_2026-07.md`). Flagging them first, because two of them move the answer.

1. **The measured baseline is cache-warm-biased, and real conversation is not.** The B-COST runner fired turns 14–50 seconds apart. At that pace the 5-minute cache stays warm. In the whole 689-call dataset there is exactly **one** deliberately cold mid-conversation turn — and it is the most valuable data point in this study (Item 2).
2. **"Desert-only" is not established.** The two worlds that scored 0% retry rate were not in `HARD_CEILING_WORLDS` when the run happened — they were added two days later. The engineering memo estimates both would have fired at 100%.
3. **Two figures don't reconcile.** The "74% more expensive per turn" and the "31,200–39,700 token prompt" both disagree with the committed numbers. Details in Items 3 and 5.

**Pricing basis, per Item 5:** the baseline reports **standard rates as primary** (`cost_baseline_runner.py:44`). Every dollar figure below is standard rate = **the post-September-1 rate**. Introductory-rate figures are ~27% lower on the Sonnet portion and expire in 30 days.

---

## Item 1 — Predictive/semantic answer serving

### What's confirmed in the code

**Documented.** The matching mechanism is exactly as described, confirmed directly:

- `answer_bank.py:99` keys every entry by `(entry["role"], entry["set_id"], entry["question_order"])`.
- `lookup()` (`answer_bank.py:115`) reads those three fields off a `curriculum_ref` **supplied by the client**, never inferred from text.
- `_normalize()` (`:107`) is NFKC + casefold + whitespace collapse — deliberately no looser.
- `try_answer_bank()` (`:158`) excludes table mode outright.

The module docstring states the design intent plainly: *"never inferred from parsing free-typed text. That is what makes 'never serves a paraphrase' true by construction rather than by hoping a fuzzy matcher never misfires."*

**Documented, and materially more than the prior study said: the Answer Bank currently serves 0% of traffic, not 5.2%.** `data/answer_bank/` does not exist. No `answer_bank` JSON exists anywhere in the repo. `curriculum_ref` is an optional request-body field that only a curriculum picker UI would populate, and that UI has never been built. The ~5.2% is the *designed ceiling*, not a current rate. Both numbers matter: **current design captures 0% today and ~5.2% if fully built out.**

### Architectural feasibility — the machinery is a near-exact fit

**Widely Accepted.** The retrieval stack already does "compare a new query against a bank of known items," and it does it for free:

| Component | File | Reusable as-is? |
|---|---|---|
| Local embeddings, CPU, zero API cost | `rag/embeddings.py:16` | **Yes** — world-agnostic |
| FAISS index build/load | `rag/indexer.py` | **Yes** — a question bank is just another corpus |
| BM25 + dense RRF fusion | `rag/hybrid.py:131` | **Yes** — matters when someone types an exact term like "theosis" |
| Cross-encoder rerank | `rag/cross_encoder.py:76` | **Mechanically yes, semantically no** — see below |

What would need building is small: a per-world FAISS index over canonical question strings, and a serving-side decision function. The retrieval pipeline itself needs no changes.

**The one real technical mismatch:** `cross-encoder/ms-marco-MiniLM-L-6-v2` is a *passage-reranking* model — trained on query→document relevance. Question→question paraphrase equivalence is a different task. And `RELEVANCE_THRESHOLD = -4.0` was calibrated on retrieval cases; it carries no meaning for equivalence. Reusing the reranker is an afternoon of wiring and a month of calibration.

### The conflict this study has to surface

**Documented.** The project's own design doc — `CiC_Answer_Bank_Full_System_Design_V0_1.md` §3.4 — already considered inference-based serving and recommended against it, in italics:

> *"This document's core recommendation: do not build inference-based serving matching, at all."*

Mark's hypothesis and that recommendation point in opposite directions. Worth naming plainly: the design doc's reasoning is a values argument, not a technical one — a semantic matcher that fires on a near-miss serves a prepared answer to a question that wasn't quite asked, and "never answer something you weren't actually asked" is load-bearing here.

**The same document already names a bridge.** §3.4 carves out one legitimate use of inference on the serving side: a *"did you mean — others have asked..."* suggestion built from embedding similarity, shown next to the free-text box. Nothing auto-serves; the suggestion offers a **tap target**, and the tap is the same explicit signal a curriculum starter tap already is. That preserves the by-construction guarantee and still captures free-text traffic — the actual cost problem — and it loosens the gate the design doc identifies as binding ("a meaningfully larger fraction would have to come from gate-widening, not catalog-widening").

**The honest framing is and, not or:** Mark's semantic infrastructure is the right machinery, applied at the suggestion layer rather than the serving layer. Same integrity property, most of the cost benefit — a tapped suggestion costs exactly what a tapped starter costs: zero.

### The two failure modes, and how to actually test them

- **Canned-feeling** — the answer fits, but reads pre-written. A tone/authenticity problem.
- **Mismatch** — the answer doesn't fit what was asked. An integrity problem.

They need different tests, and neither can be answered by reasoning alone.

**Test 1 — threshold calibration (answers "mismatch").** Build a labelled set of ~300 question pairs per world: true paraphrases, near-misses (same topic, different ask), and unrelated. Score with the existing embedding + cross-encoder stack. Plot precision/recall against threshold. Solve for the threshold at which false-positive rate ≈ 0, since a mismatch is unrecoverable and a miss just costs a live call. If no threshold cleanly separates near-misses from true paraphrases, the suggestion layer needs human-curated question clusters instead of a similarity cutoff — a real possible outcome (the cross-encoder's own docstring already records exactly this failure on reactive-shape queries: "NO threshold separates them, measured").

**Test 2 — blind comparison (answers "canned").** ~40 questions; generate a live Sonnet answer and a banked answer for each; graders see both, unlabelled, randomized order, and answer two separate questions: does this answer what was asked, and does this sound like the Representative. If banked answers lose on the second while matching the first, the variation mitigation is the fix. If they lose on the first, the threshold is wrong and no phrasing variety helps.

One thing that shrinks the canned risk: `stream_answer_bank()` already replays a banked answer token-by-token, so it arrives looking like a live generation — its own docstring flags the one honest tell: it arrives faster, with no pacing delay.

### Mark's variation mitigation — assessed directly

**Sound, cheap, and it needs a specific guardrail.** Building it is small: Haiku batch-generating 5 phrasings per canonical answer, once, offline — roughly **$3.40–6.75 total** across the whole catalog. Zero marginal runtime cost, exactly as proposed.

**The guardrail:** generating text from other generated text is a new operation for this codebase with failure modes the existing fabrication tooling hasn't had to catch — claim invention via recombination, citation drift, register incoherence. The concrete constraint: **variations may re-word, never re-content** — mechanically checkable via the same citation/entailment checks already specified elsewhere. Worth knowing: a recent validation battery (RM-8, 2026-07-22) recorded register-invariance as *not yet reliable* — 3 of 5 probes failed on content-invariance. Generating register variations asks the system to do by hand something its own most recent testing measured as shaky. Human review of a sample stays mandatory.

### Realistic capture fraction

**Inferential-Thin — these are reasoned estimates about human behavior, not measurements.**

| Design | Capture of real turns | Basis |
|---|---|---|
| Current scripted design, as it exists today | **0%** | Bank empty, no curriculum UI. Documented. |
| Current scripted design, fully built | **~5.2%** (4–16%) | The project's own cost-floor model |
| Same catalog grown to ~150 | **~5.8%** (1.6–11%) | Catalog size was never the binding gate |
| Semantic suggestion layer, well built | **15–25%** | Reasoned, not measured — see below |

The 15–25% reasoning: today's binding gate is "does someone choose the question-first door" (~1/3). A suggestion next to the free-text box removes that gate entirely. What replaces it is match-rate on a typed question times tap-through rate on the suggestion. Opening questions ("who is Jesus," "what do you believe") are highly predictable and probably match well; turn-4+ follow-ups are context-dependent and probably don't. Since openers are maybe a fifth of turns in a 10-turn conversation, 15–25% is where the arithmetic lands — **every factor in it is a guess.** The cheapest way to replace guesses with data: turn on `transcript_logging.py`'s message table (already built, currently off) and count what people actually type.

---

## Item 2 — The cache TTL fix

### Confirmed in code

**Documented.** Three `cache_control` sites exist in the backend, all using the bare 5-minute default (static prompt, reactive-turn guidance, adjudication prefix). **The 1-hour option is genuinely available** — GA, no beta header, supported on both models. Cache write costs 2× base input at 1h versus 1.25× at 5m; cache read stays 0.1× at both.

### The measurement

**Documented — the cleanest evidence in this study.** The baseline contains a deliberate single-variable experiment: a 330-second pause before turn 6 in one conversation.

| turn | cache_read | cache_write | turn cost (std) |
|---|---|---|---|
| 5 | 15,737 | 0 | **$0.0661** |
| 6 (after pause) | **0** | **15,737** | **$0.1283** |
| 7 | 15,737 | 0 | **$0.0726** |

**One lapsed cache window cost $0.056 — it nearly doubled that turn.** The math checks out exactly against current pricing (predicted premium $0.0543, measured $0.0557, within 3%).

### What a 1-hour TTL is actually worth

**Widely Accepted.** At a reflective human pace — anything slower than one turn per five minutes — every turn currently looks like turn 6 above. Amortizing one 1-hour write across a 10-turn sitting: cached-prefix cost per turn drops from $0.059 (all-cold, 5-min TTL) to $0.014 (1-hour TTL). Applied to the measured cold turn: **$0.128 → $0.083, a 35% reduction on a single 1:1 turn.** Break-even is the second turn; any real sitting clears that immediately.

**Confirmed low-risk, and specifically why:** cache TTL is a billing and latency property only — the cached bytes are identical either way, so there's no path by which TTL changes model output. Worst case (someone typing faster than 5 minutes per turn) costs one extra small write, then behaves identically. Downside bounded and small; upside 35%.

**A second payoff the prior study missed:** the adjudication prefix (~9,250 tokens) fires only intermittently by design, so under a 5-minute TTL it's essentially never warm — one adjudicator logged zero cache reads against real writes, paying full price every time. A 1-hour TTL fixes this with the same one-line change.

---

## Item 3 — Sonnet prompt size and the regeneration bug

### What's actually in the prompt

**Documented (measured), correcting the prior study.** Measured mean total prompt is ~20,500 tokens per call (not 31,200–39,700) — flagged as unreconciled with the prior figure, not resolved in favor of either. Breakdown: ~66% cached static prefix (billed at 0.1×), ~8% cache-write overhead, **~26% genuinely uncached dynamic content** (retrieved lexicon + story context), ~1% output. The conversation transcript is hard-bounded at 12 rendered lines — it is not the growth driver and not the trim target.

### How much could be trimmed — and the finding that reorders the question

**Once the 1-hour TTL lands, trimming the world capsule buys almost nothing** — a warm cached prefix already bills at 0.1×, so the whole static block costs about $0.004/call; cutting it 30% saves a fraction of a cent, paid for in Representative fidelity risk. **Recommendation: do not trim the world capsule or permanent prompt.**

**The money is entirely in the uncached ~26% (retrieved lexicon + story).** The one measurable question: are the current retrieval depths (3 lexicon chunks, 2 story chunks) the right values? Dropping to 2 lexicon chunks would cut real cost (~7% of a warm Sonnet call) — **but this must not ship on a token count.** A golden-set retrieval test harness already exists; run it at both depths and only cut if nothing important drops out.

### The regeneration bug — bigger than "Desert"

**Documented, and the prior study's framing understates it.** The mechanism: a draft response exceeding its world's length ceiling triggers one full second Sonnet call, resending the whole prompt. The two worlds that measured 0% retry rate were added to the ceiling list *after* the measured run — a documented measurement artifact, not a clean result. Engineering estimates predict both would fire at or near 100% if measured properly.

**Root cause, found directly:** no deployed prompt contains any numeric word target — Desert's prompt says "four sentences is already long for you," qualitative, while the code enforces a hard 60-word ceiling. The model is only told the actual number *after* it has already broken the rule, on the retry.

Measured impact where it *was* measured: 9.4% of total baseline spend, 16.4% of all Sonnet spend, 23.9% of one Desert conversation. If the fleet-wide estimate holds, the true impact is higher. A remedy is already scoped in a separate engineering memo (adding a real in-voice length exemplar to the prompt, among other options) — **needs live testing, not an offline decision.**

**What needs testing before anything ships:** re-run the cost baseline with the length-ceiling logger active (built for this, never yet produced a production record) to get real fire rates across all six worlds.

---

## Item 4 — Haiku governance consolidation

**Documented.** Haiku is ~30% of current-code spend; Sonnet ~70%. The two safety-critical checks (frame-breaker, relational-safety) are cheap already (3.8% combined) and **should not be touched** — both fail open by design with different failure asymmetries, and merging them risks a real safety regression for under 4% of spend.

**The one real target: the "over-settling" check chain is 14.1% of spend, and its cheap screening stage escalates to the expensive stage 82% of the time.** The whole point of a cheap screen is to avoid the expensive stage — an 82% pass-through means it's likely mis-calibrated, adding a call rather than saving one. A purpose-built logger already exists to measure the real confirm rate (what fraction of escalations the expensive stage actually confirms) — **this is a calibration question with an existing instrument, not a guess.** If confirm rate is low, the screen can be tightened against real data.

A second, no-risk target: one adjudicator (`repair_adjudication`) is missing the caching treatment its siblings already have — a one-line fix.

---

## Item 5 — The September 1 pricing change

**Documented.** Sonnet input and output both rise 50% on 2026-09-01; Haiku is unchanged. With Sonnet at ~70% of spend, the blended increase is **+35%, no code change required, arriving in 30 days.**

**Every figure in this study is already at the post-September rate** — the baseline reports standard rates as primary, so nothing here gets worse later; it's already accounted for. One open question worth a quick check: if the "~$2/hour" figure Mark named came from real billed spend, it was billed at *introductory* rates, meaning the same real usage becomes ~$2.70/hour once September lands — changing the gap to the $0.50 target from 4× to about 5.4×. A one-line check against the actual API bill would resolve this.

---

## Synthesis — a recommendation to react to, not a decision

### Stacking every realistic lever, 1:1 conversation, post-September rates, human pace

| Step | $/turn | Confidence |
|---|---|---|
| Baseline today, human pace (all turns cache-cold) | **$0.128** | Widely Accepted |
| + 1-hour cache TTL | $0.083 | **Documented — directly measured** |
| + regeneration fix (fleet-blended) | $0.073 | Widely Accepted |
| + uncached retrieval trim (if the golden set clears it) | $0.065 | Inferential-Thin |
| + over-settling recalibration | $0.058 | Inferential-Thin |
| + semantic suggestion layer @ ~20% capture | **$0.046** | Inferential-Thin — least certain number here |

| Pace | 1 Representative | 3 Representatives |
|---|---|---|
| 6 turns/hr (10 min/turn) | **$0.28/hr** | **$0.66–0.78/hr** |
| 10 turns/hr (6 min/turn) | **$0.46/hr** | **$1.10–1.30/hr** |
| 15 turns/hr (4 min/turn) | **$0.69/hr** | **$1.65–1.95/hr** |

### The direct answer

**For 1:1 conversation — reachable with real effort, and closer than it looked.** At a reflective pace, $0.50/hour is reached by the cache fix and the regeneration fix *alone*, before touching any of the uncertain levers. Both are engineering fixes on already-identified defects, not product compromises. **The single most striking result in this whole study: the one-hour cache TTL change on its own takes a 6-turn-per-hour 1:1 conversation from $0.77/hour to $0.50/hour.** One line of code, in three places, no behavioral risk, worth more than every other lever combined except the answer bank.

**For the Living Table — not realistic without a structural change.** Every lever compounds correctly and the table still lands at 2–3× the threshold. This is structural, not an optimization gap: a 3-Representative table does 2–6 Sonnet generations and 45–60 Haiku calls for one participant message, by design. No amount of caching or consolidation closes a 3× gap on a mechanism built to do 3× the work.

**This strengthens, with independent evidence, the prior study's own recommendation: let table size be what the free tier governs, with 1:1 as the free experience.** That recommendation came from the cost scaling alone. This study adds a second, independent reason — 1:1 is the *only* configuration that reaches the viability threshold on realistic, low-risk engineering, and it reaches it with real room to spare.

### Three things worth treating as time-sensitive

1. **The September pricing step is 30 days out and unbudgeted** — but the cache TTL fix roughly cancels it out for 1:1 conversation on its own.
2. **The cheapest real measurement left is overdue and small.** Re-running the cost baseline with the length-ceiling and over-settling loggers active, at realistic (not back-to-back) pacing, including one 2-Representative conversation (still never measured anywhere), would resolve four of this study's open questions for a few hours of compute.
3. **The Answer Bank serving 0% today, not 5.2%, is worth knowing before any decision leans on the higher number.**

### The one place this study disagrees with a prior project document

Mark's semantic-serving idea and the Answer Bank design doc's explicit "do not build inference-based serving matching, at all" point in opposite directions — a values disagreement, not an engineering one. The proposed resolution (semantic matching at a tap-to-see suggestion layer, never auto-serving) is offered as a genuine **and**, not a way to quietly pick a side — but it's a proposal, not a resolution. The design doc is a considered artifact of this project's own prior reasoning. Reconciling the two is Mark's call.
