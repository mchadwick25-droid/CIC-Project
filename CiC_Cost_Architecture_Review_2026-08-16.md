# CiC Cost & Architecture Review — 16 August 2026

Independent pass over `cic/records`, `cic/engine`, `cic/runtime/app`.
Single-voice mode. Published view: https://claude.ai/code/artifact/b56d902b-fe88-4705-acbe-d53a5ad091b0

## Short version

1. **The payload was misdiagnosed.** The ~21–23k tokens per `main_response`
   call is the *total* input, not an uncached block. ~79% is the static
   per-world prompt, which the code correctly marks cacheable. Retrieved
   lexicon/story content is only ~19%.
2. **Measured cost is consistent with the cache not paying off.** A working
   cache predicts ~$0.021/turn for `main_response`; the measurement was
   ~$0.063. That gap is worth more than the whole classifier stack.
3. **$0.30/hour is not reachable on Sonnet 5.** Cache fixed + classifiers cut
   hard lands ~$0.40/hour today, ~$0.52 from 1 September. Haiku 4.5 as the
   voice model is the only lever that clears the target.
4. **Sonnet 5 intro pricing ends 2026-08-31** ($2/$10 -> $3/$15 per MTok).
   Current measurements understate the September bill by 50% on generation.
5. **Safety mechanisms are not where the money is** (3.2% of spend). Whatever
   the policy call, it is not a budget decision.

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

## Route to $0.30 (12 turns/hour, cumulative)

| Step | Change | $/turn | $/hour |
|---|---|---:|---:|
| S0 | Today, as measured | 0.0910 | 1.09 |
| S1 | Cache reads landing, Sonnet kept | 0.0440 | 0.53 |
| S2 | + Haiku 4.5 voice | 0.0334 | 0.40 |
| S3 | + classifier surgery | 0.0223 | **0.27** |
| S4 | Classifier surgery, Sonnet kept | 0.0329 | 0.40 |
| S5 | S4 after 2026-09-01 pricing | 0.0436 | 0.52 |
| S6 | S3 at pilot scale (20 sessions/world) | 0.0194 | 0.23 |

Deleting *every* classifier while changing nothing else leaves $0.75/hour.
The handoff's 18.6% arithmetic was right; that road does not reach the target.

## Findings, ranked by money

1. **Caching implemented but apparently not paying off** (~$0.50/hour).
   `_cached_system_message` and `_cached_adjudication_message` both split
   correctly at the stable/volatile boundary with 1h TTL; both generation
   paths use them; the static block clears the 1,024-token minimum. Design is
   right, arithmetic does not reconcile. **Verify before changing anything.**
2. **Generation model** (~$0.13/hour on top of a fixed cache). Already tried
   and reverted 2026-08-10 — on a Haiku-only *table*-mode transcript
   isolation breach (up to 21% of table turns), not on cost and not on solo
   quality. Single-voice mode builds no public transcript. Chloe's Haiku
   re-certification held every hard bar; the one real regression was
   citations 7/8 -> 3/8.
3. **Classifier stack is 13–15 Haiku calls/turn, not ~10** (~$0.14/hour
   recoverable). Concentrated in `over_settling_adjudication`, which fires on
   78% of turns and confirms on 20%.
4. **Intro-pricing cliff 2026-08-31** (~$0.21/hour if nothing changes).
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

## Recommended order

1. Verify the cache: two consecutive turns, read `cache_read_input_tokens`.
   ~15 min, ~$0.15.
2. Audit the cost calculator: LangChain's `usage_metadata["input_tokens"]`
   is *total* input with `cache_read`/`cache_creation` as subsets — not
   additive buckets like the raw Anthropic block. A calculator that sums all
   three overcharges cached tokens by roughly the observed gap. Most likely
   benign explanation; rule it out first.
3. Decide Sonnet vs Haiku on **citations**, not cost. Re-run the citation
   battery on Haiku, single-voice, all six worlds.
4. Classifier surgery.
5. Re-baseline before 2026-09-01.

## Not verified

- Prior session's raw transcripts were container-local and are gone; the
  $0.091 could not be re-derived directly, only reconciled against the two
  percentages quoted in the handoff.
- Output tokens estimated at 250/turn from recorded voice-profile word counts
  against a 1,200 cap. Higher real output strengthens the Haiku case.
- Retrieved-context tokens derived at the ratio exact static counts imply
  (3.26 chars/token); ~±5%.
- The app was not run. No billable API calls were made for this review.

## Incidental (product, not cost)

In single-voice mode the representative receives **only the current
question** — `_prepare_representative_turn` gates the public transcript
behind `is_multi_world`, and the message array is `[system, continuation]`
with no history. That is why the payload is flat and why caching works so
well. It also means a 12-turn interview is 12 independent answers. Anything
that adds conversational memory later will change these economics.
