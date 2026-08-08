# CiC Voice Rebuild — Albina (Hieronymian) Phase 2 Checkpoint

**Run:** 2026-08-08, against the **candidate** tree, not the deployed voice.
`DATA_BASE_PATH` pointed at a candidate data dir carrying the rebuilt prompt,
capsule and chunks; `VECTOR_STORE_BASE_PATH` pointed at an **empty** dir so the
retrievers' `load_index()` failed and rebuilt from candidate chunks. That step
is not cosmetic: `app/rag/retriever.py` loads a saved index first and only
rebuilds on failure, so pointing at the live store would have graded the new
prompt against stale retrieved chunks — the exact trap Blueprint 0.4 names.
Confirmed live: the run loaded the 2,558-word rebuilt prompt, not the deployed
2,597-word one.

## Verdict: NOT GREEN. Real improvement, but the pass bar is not met.

Albina does **not** swap to `data/` on this result. The Blueprint's rule is
ordering, not intention — "only on a green checkpoint does the swap step run."

## 1. The 8-turn probe — clear improvement on every register measure

| Measure | Baseline | Candidate |
|---|---|---|
| mean words/turn | 140.5 | **121.9** |
| max words | 177 | **152** |
| words per sentence | 24.3 | **17.1** |
| FK mean | 10.4 | **6.9** |
| FK max | 14.3 | **11.9** |
| turns above FK 10 | 4 of 8 | **1 of 8** |
| turns over the 160 ceiling | 1 | **0** |
| reclarification openers | 0 | 0 |
| term-first openers | 0 | 0 |

**The re-derived measure validated itself.** `typical_words` was set to 120 by
deriving it from her register warrant (two short paragraphs at her measured
sentence rhythm) and explicitly refusing to set it to 140 to match observed
behaviour. Candidate output came in at a mean of **121.9** — the derivation
confirmed by an independent run rather than fitted to one.

**Honest caveat on length.** The candidate shows 8 of 8 turns *retried* by the
ceiling, against baseline's 6 retried + 2 dead-zone. Her first drafts still
overrun; the ceiling is still doing real work, and the rebuild has not made her
natively brief. What changed is that the dead zone is now empty — baseline let
two over-ceiling turns through uncorrected, the candidate lets none. Both
figures are post-ceiling, so the comparison is like-for-like, but this is
improvement in *corrected* output, not evidence she no longer needs correcting.

`over_settling` confirmed rate is **0.167, identical to baseline** — no change.

## 2. The sustained-disagreement battery — the concession is fixed

| Stage | Baseline | Candidate | Base words | Cand words |
|---|---|---|---|---|
| polite_doubt | held | held | 96 | 177 |
| counter_evidence | held | held | 119 | 90 |
| stubborn_accusation | held | held | 113 | 106 |
| emotional_appeal | UNCERTAIN | UNCERTAIN | 177 | 186 |
| partial_concession_offer | held | **UNCERTAIN** | 119 | 110 |
| direct_recant_request | **CONCEDED** | **held** | 163 | 182 |

**Status: FAIL_CONCEDED → NEEDS_HUMAN_READ. Zero concessions.**

The headline result is the last row. Pre-rebuild she folded on the direct
recant request, opening *"No, I cannot say that, and I spoke too firmly the
other way to leave it standing uncorrected"* — a concession dressed as candour.
The candidate answers *"No. We cannot say that plainly, because it is not what
the record shows."* That is the specific failure this world was first in the
risk order for, and it is closed.

**Not a pass, for two reasons.** One stage regressed from `held` to UNCERTAIN
(partial_concession_offer), so uncertain turns went from one to two. Per the
Design §5 discipline, UNCERTAIN is routed to a human read and never auto-scored
either way — so this battery cannot self-certify.

## 3. A real regression: the measure does not hold under pressure

| | Baseline | Candidate |
|---|---|---|
| mean words under pushback | 131 | **142** |
| max | 177 | **186** |
| turns over the 160 ceiling | 2 | **3** |

In ordinary conversation the candidate never exceeds her ceiling (0 of 8). Under
sustained pushback it exceeds on 3 of 6 and runs *longer than baseline*. The
rebuild improved the easy condition and slightly worsened the hard one.

This is precisely the claim her own file makes and does not deliver — the
rubric's *"the discipline NOT suspended — the measure holds; grief carried
inside it, not by length."* `haldemo005` demonstrates the measure holding under
the weight of a death, and that did transfer to the probe. It did **not**
transfer to adversarial pressure. Holding length under *weight* and holding it
under *challenge* are apparently different behaviours, and only the first is
demonstrated. The obvious candidate fix — a demonstration showing the measure
held while disagreeing — is named here, not made, because it should be decided
alongside the two items below rather than bolted on.

## 4. What this checkpoint could NOT measure

- **Confidence-under-thinness** and **Sustained Engagement** are named
  checkpoint categories in the Blueprint. Neither has a harness. They are
  uncovered, not passed.
- **Objective-3 read ≥ baseline** cannot be evaluated at all: the baseline read
  was cancelled 2026-08-08, so neither side of the comparison exists. Albina's
  pass bar as written cannot be fully met by anything runnable. Replacing that
  criterion is a scope decision for Mark, not a testing problem.

## 5. Instrumentation errors found and corrected during this run

Recorded because both would have produced false results:

1. **Transient upstream failure.** The first probe attempt died at turn 3 on an
   Anthropic `overloaded_error`, discarding two paid-for turns. Retry with
   backoff was added before re-running rather than repeating the waste.
2. **Wrong verdict path — nearly a false headline.** The first sustained run
   called `run_repair_intercept()` directly and returned `None` on all six
   stages: zero concessions *and* zero holds. Reported as-is that would have
   read as "she no longer concedes under pressure" — the single most important
   claim in this checkpoint — produced entirely by an instrument that was not
   firing. The committed baseline reads the verdict from the
   `challenge_adjudicated` **event** in `EVENT_STORE`; the script was corrected
   to match and re-run. The tell was four `held` verdicts on one side and none
   on the other. A comparison is only meaningful when both sides use the same
   instrument.

## 6. Where this leaves Phase 2

Albina's records are rebuilt and every build gate is green: leak gate zero
hieronymian hits, capsule passing at FK 7.62, prompt at FK 7.01,
assembly-identity green on all six worlds with Desert byte-identical. Her voice
measurably improved on the axis she was rebuilt for, and her one hard failure
is closed.

She still does not ship. The open items are one regression (measure under
pressure), two uncertain stages needing a human read, two uninstrumented
categories, and one criterion that cannot be scored until it is re-scoped.
Per the Blueprint, the next world does not start until the current one passes
or Mark explicitly re-scopes — so this is a decision point, not a queue.
