# CiC Cost & Architecture Review — 16 August 2026

Independent pass over `cic/records`, `cic/engine`, `cic/runtime/app`.
Single-voice mode. Published view: https://claude.ai/code/artifact/b56d902b-fe88-4705-acbe-d53a5ad091b0

> **Revised 2026-08-16 after running the cache verification test.** The first
> version of this document suspected a runtime cache failure. That was wrong —
> the cache works. The root cause is the cost calculator, which was listed
> there as the "most likely benign explanation" and is now confirmed.

## Short version

1. **The prompt cache works.** A live two-turn test returned a clean
   17,565-token `cache_read` on the second call, on both the streaming and
   non-streaming paths, at the 1h TTL.
2. **The cost calculator double-charges cached tokens.** LangChain reports
   `input_tokens` as the *total* input with `cache_read` as a subset;
   the raw Anthropic block reports them as additive. Summing all three
   overstates `main_response` by **2.6x**.
3. **True cost today is ~$0.53/hour, not $1.09.** The gap is 43%, not 73%.
4. **$0.30/hour IS reachable on Sonnet 5** — classifier surgery + halved
   retrieval + pilot concurrency lands exactly on the line, at intro pricing.
5. **Sonnet 5 pricing is stable at $2/$10.** Verified against the live model
   docs 2026-08-16: flat pricing, no introductory expiry. An earlier draft of
   this review warned of a 2026-08-31 cliff, drawn from a stale cached table;
   **withdrawn**. There is no deadline on the voice-model decision.
6. **Safety mechanisms are not where the money is** (3.2% of spend).

## Verification test (live, ~12 cents)

Replicating `get_llm(max_tokens=1200)` and `_cached_system_message` verbatim
against the real Syriac static prompt; `tools/cost/verify_prompt_cache.py`.

| Call | Path | LangChain `input_tokens` | Raw API `input_tokens` | cache_creation | cache_read |
|---|---|---:|---:|---:|---:|
| A1 | stream, 1h | 17,680 | (not populated) | 17,565 | 0 |
| A2 | stream, 1h | 17,680 | (not populated) | 0 | **17,565** |
| A3 | invoke, 1h | 17,680 | **115** | 0 | **17,565** |

A3 is the decisive row. The raw Anthropic block reports `input_tokens: 115` —
the genuinely uncached remainder. LangChain reports 17,680 for the same call,
because its `input_tokens` is the total with `cache_read` nested inside
`input_token_details`. Streaming never populates the raw block at all, so the
production path only ever exposes LangChain's total.

On A2 a calculator summing the three reports $0.0418; true cost $0.0067
(6.3x, inflated because the test's dynamic block was deliberately small).
On a realistic production turn the overstatement settles at **2.6x**.

## Measured token shape (exact static counts via free `count_tokens`)

| World | Static (cached) | Retrieved (uncached) | Total in | Cacheable |
|---|---:|---:|---:|---:|
| imperial_juridical / Marius | 15,781 | 3,720 | 19,801 | 80% |
| hieronymian / Albina | 16,632 | 3,190 | 20,122 | 83% |
| desert / Papnoute | 16,796 | 2,830 | 19,926 | 84% |
| syriac / Yausep | 17,567 | 5,380 | 23,247 | 76% |
| pahc / Chloe | 17,699 | 5,890 | 23,889 | 74% |
| alexandria / Theon | 22,546 | 7,310 | 30,156 | 75% |
| **fleet mean** | **17,837** | **4,343** | **22,480** | **79%** |

The 22,480 mean independently reproduces the 21,000–23,000 figure observed in
the live round — confirming it is the total, not an uncached remainder.

Model cross-check: `over_settling_adjudication` re-sends permanent prompt +
capsule + a second full retrieval to Haiku (~15,000 tok at $1/MTok) on 78% of
turns => ~$0.0117/turn. The prior session measured 12.7% of $0.091 = $0.0116.
The token model is sound; the caching line is what refuses to reconcile.

## Route to $0.30 (12 turns/hour, output measured at ~330 tok)

| Step | Configuration | $/turn | $/hour |
|---|---|---:|---:|
| R0 | As reported (double-counted) | 0.0910 | 1.09 |
| T0 | **True today**, no changes | 0.0442 | 0.53 |
| T1 | + classifier surgery | 0.0351 | 0.42 |
| T2 | + pilot scale (20 sessions/world) | 0.0295 | 0.35 |
| T3 | + retrieval halved — **Sonnet meets target** | 0.0251 | **0.30** |
| T4 | T1 + Haiku 4.5 voice | 0.0241 | **0.29** |
| T5 | T4 + pilot scale | 0.0212 | **0.25** |

On true numbers the classifier stack is ~$0.022/turn — about half the real
bill, a larger share than the original figures implied. The saving is
concentrated in one line (`over_settling_adjudication`), not spread thin.

Self-correction: the first version dismissed retrieval trimming as worth only
$0.05/hour. That is still the number, but against a corrected $0.53 baseline
where the static block bills at a tenth, retrieval is one of the few
components still paying full freight — and $0.05/hour is exactly the margin
between T2 and T3. The lever was mis-sized, not irrelevant.

## Findings, ranked by money

1. **Cost calculator double-counts cached tokens** (no real spend; makes
   every cost decision wrong by ~2x). Confirmed by live test. `log_llm_usage`
   is correct as logging; the error is downstream, in treating LangChain's
   `input_tokens` as uncached-only. Because streaming never populates the raw
   Anthropic block, there is no signal that anything is off.
2. **Generation model** (~$0.13/hour). Now purely discretionary — not needed
   to reach target and not forced by pricing. Already tried
   and reverted 2026-08-10 — on a Haiku-only *table*-mode transcript
   isolation breach (up to 21% of table turns), not on cost and not on solo
   quality. Single-voice mode builds no public transcript. Chloe's Haiku
   re-certification held every hard bar; the one real regression was
   citations 7/8 -> 3/8.
3. **Classifier stack is 13–15 Haiku calls/turn, not ~10** (~$0.14/hour
   recoverable). Concentrated in `over_settling_adjudication`, which fires on
   78% of turns and confirms on 20%.
5. **Cost/hour falls with concurrency** (~$0.04/hour). The 1h cache entry is
   keyed on prefix, not session, so it is shared across all sessions on a
   world within the window.

## Classifier architecture — necessary at current scope?

Mostly yes. Cut: the two shadow-mode groundedness checks (added 2026-08-15,
gate nothing) once Phase 0 has its sample; tighten the over-settling screen;
re-examine whether the retrieval negative-condition guard vote earns four
Haiku calls per turn on a 10–50 entry corpus. Do **not** cut the pre-turn
intercept chain, drift detection, or citation grounding on cost grounds —
they are cheap and load-bearing for the project's central claim.

## Safety disagreement

Facts: relational safety + frame breaker = $0.21 across all six test
conversations, 3.2% of spend, ~$0.035/hour. Removing them covers ~1/10 of the
gap. The cost argument does not survive contact with the numbers.

Substance: declining outright was the wrong move — it is Mark's product and
his duty of care to define. But keyword-triggered distress detection is
empirically weaker here, because people in distress about death and faith
rarely produce trigger keywords ("I don't see the point in going on").

**Uncosted middle path:** the mechanism has two halves.
`classify_relational_safety` is one Haiku call (~$0.0007/turn).
`stream_relational_safety_response` generates freely on Sonnet at full cost.
Keep the classifier; replace the generated response with fixed written text
approved once by Mark and a clinician. Better detection than keywords, no
model improvising in the highest-stakes moment, most of the cost gone.

## Trim ledger at 1,000 conversation-hours/month (12,000 turns)

Cumulative. Baseline = true isolated-session cost, $0.53/hr = $6,369/yr.

| Lever | Quality | $/hr | $/mo | $/yr |
|---|---|---:|---:|---:|
| A · strip builder apparatus from retrieved chunks **(SHIPPED)** | **improves** | 0.031 | 31 | 367 |
| B · gate safety classifiers behind a lexical filter | neutral | 0.032 | 32 | 384 |
| C · over-settling adjudicator 78% -> 30% | neutral | 0.039 | 39 | 463 |
| D · retire the two shadow-mode checks | neutral | 0.018 | 18 | 216 |
| E · trim `_HOW_YOU_ENGAGE` by 40% | test it | 0.018 | 18 | 221 |
| F · pool cache writes (20 sessions/window) | none | 0.057 | 57 | 682 |
| **Sonnet 5, all of A-F** | — | **0.326** | **326** | **3,907** |
| Haiku 4.5, all of A-F | costs citations | 0.251 | 251 | 3,015 |

**A-F is worth ~$2,330/yr and requires no voice change.** (A came in at $367
rather than the estimated $496 - stories already stripped two of the sections
at index time, which the first estimate double-counted.) Haiku on top saves a
further $892/yr, permanently — the whole price of the Sonnet voice, against a
measured citation regression of 7/8 -> 3/8. **Recommendation: keep Sonnet.**
Grounded citation is the project's central claim and $892/yr is not the right
price for halving it when the target is already met without it.
One penny per hour = $120/year at this volume.

### A · Most of what retrieval sends is builder apparatus — SHIPPED 2026-08-16

Measured across every deployed chunk, as the model receives it after the
existing Key Sources / Quick Meaning excisions:

Story chunks — Story Text 29.5% | Tier Justification 25.0% | Usage Guidance
22.6% | Formation Ecology Connection 16.5% | Source Identification 5.2%

Lexicon chunks — World Meaning 52.5% | Distortion Risk 23.1% | Ecological
Function 15.8%

**Measured after implementation: the retrieved payload falls 34.1%**, 3,291 ->
2,168 tokens/turn, plus ~150 tokens from the retired FLAG-018 instruction =
1,273 uncached tokens/turn, $367/yr at 1,000 hours/month.

**`Distortion Risk` is the section that caused FLAG-018** — the voice read it as a task and opened turns with
unprompted term clarifications; the compensating instruction still ships in
the dynamic prompt on every turn. Strip the apparatus at build time and the
defect source, the compensating instruction, and a third of the uncached
payload all go together. Removed on **coherence** grounds before cost: the
section reads "A modern reader hears X...", handing the voice explicit
knowledge of how a modern participant thinks, which is exactly what the
permanent prompt's Total Embeddedness rule forbids.

Kept, though they read like apparatus by name: **Usage Guidance** and **Absent
Story Note** both carry anti-fabrication constraints the voice needs ("should
receive honest brevity, not an invented timetable"); **Plural-Voices Note**
carries attribution honesty. Tier/confidence remain in front-matter metadata.

#### Two defects found while implementing

1. **`find_section` under-reported fenced sections containing bold
   sub-labels.** `"\n\n**"` is a section-end marker, so `## Distortion Risk`
   ended at its own `**Modern Hearing:**` — reported extent 2.3% of the
   lexicon pool against a true 23%. Excising it would have removed the
   heading and left the body in place. Fenced sections now end only at
   `"\n---"` or `"\n## "`. Verified byte-identical on the existing Quick
   Meaning + Key Sources path across all 118 lexicon chunks.

2. **Eight chunks have no `World Meaning` section, or an empty one** —
   `pahclex012`, `pahclex013`, `syrlex005`, `syrlex008`, `desertlex013`,
   `desertlex017`, `desertlex018`, `ijclex011`. Their entire substance sits
   inside the apparatus, so stripping it shipped a zero-character body: the
   same Article 5 grounding failure `sections.py` was written to prevent.
   `excise_sections` now refuses any excision that would drop a body below
   `MIN_VOICE_BODY_CHARS`. **This is a records defect the guard contains but
   does not fix** — `desertlex018` has literally empty `**World Meaning:**`
   and `**Ecological Function:**` fields. Worth an authoring pass
   independent of cost.

### B · Safety: gate it, don't remove it

`classify_relational_safety` ships a 1,593-token prompt on every turn, plus a
transcript window that grows through the session — by turn 12 it is the most
expensive classifier in the stack. $384/yr spent almost entirely on people
who were never in difficulty.

Half the proposed fix already exists: relational safety and frame-breaking
already run once per turn at the facilitator layer in `classify_pre_turn`,
before any representative is invoked, not duplicated per world.

The other half — phrase triggering — is the real change. A deterministic gate
in front of the classifier, firing on ~8% of turns, cuts the line ~92% with
detection unchanged. **Design constraint that decides whether it works:** the
subject matter is death, martyrdom and suffering, so a topic-keyed filter
fires constantly. It must key on *first-person self-reference + distress
marker*: "The martyrs longed for death" silent, "I've stopped seeing the
point" fires. That is also the distinction missing from the earlier
disagreement — the objection was to a narrow keyword list with poor recall,
not to gating as such.

### On hybrid

Already hybrid and correctly so: Sonnet generates the voice, Haiku runs all
13-15 classifier calls. One quality-critical call, already the only one on
the expensive model. Routing by turn type is the remaining option and is not
advisable — voice consistency across a conversation is the product. The
ledger removes the need to choose.

## Recommended order

0. ~~**Strip builder apparatus**~~ — **DONE**, shipped 2026-08-16. $367/yr.
1. **Fix the cost calculator.** Uncached input =
   `usage_metadata["input_tokens"] - cache_read - cache_creation`, or read the
   raw block where available. Then re-price the saved clean-round logs — that
   gives true per-world figures rather than my fleet-mean model. Nothing else
   here is worth doing until this is right.
2. **Tighten the over-settling screen** (fires 78%, confirms 20%).
3. **Gate the safety classifiers** behind a first-person distress filter.
4. **Measure at concurrency.** A single-session test overstates per-turn cost
   by the whole cache-write amortisation.
5. **Leave the voice on Sonnet.** No deadline and no forcing function;
   $892/yr is the wrong price for the citation regression.
6. **Retire the two shadow-mode checks on a date.**

## Not verified

- **The cost calculator itself is not in the repo** — it lived in the prior
  session's scratchpad. I proved the trap exists and priced it against live
  measurements, and the naive model reproduces the reported $0.0625 to within
  8%, but I could not read the code that produced $0.091. Re-pricing the
  saved logs settles it.
- Classifier costs are scaled, not re-measured: small classifiers taken at
  measured value (no caching, so unaffected by the double-count); the
  adjudication figure corrected by its own cache ratio.
- Retrieved-context tokens derived at the ratio exact static counts imply
  (3.26 chars/token); ~±5%. Output measured at 296-390 tok in the live test.
- The full app was not run — the test replicates `get_llm` and
  `_cached_system_message` but not retrieval, the graph, or the classifiers.
  Total spend for this review: ~12 cents.
- Tested against langchain-anthropic 1.5.6. The clean tree carries no
  dependency manifest, so I could not confirm the version you run.

## Incidental (product, not cost)

In single-voice mode the representative receives **only the current
question** — `_prepare_representative_turn` gates the public transcript
behind `is_multi_world`, and the message array is `[system, continuation]`
with no history. That is why the payload is flat and why caching works so
well. It also means a 12-turn interview is 12 independent answers. Anything
that adds conversational memory later will change these economics.
