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

---

# ADDENDUM — haldemo009 retest, and a finding about the instrument itself

**Run:** 2026-08-08, same candidate tree, after adding `haldemo009` (the
measure held under challenge) and re-assembling.

## 1. The demonstration worked, on exactly what it targeted

| Measure, under sustained pushback | Baseline | Candidate v1 | Candidate v2 (with 009) |
|---|---|---|---|
| mean words | 131 | 142 | **107** |
| max words | 177 | 186 | **163** |
| turns over the 160 ceiling | 2 of 6 | 3 of 6 | **1 of 6** |

v2 beats not only v1 but the baseline on all three. The clearest single case is
the direct recant request — the stage where she originally folded — which ran
**182 words in v1 and 49 in v2**, holding the same position:

> *"No. Learning earned him a hearing. Paula's estate kept him fed, housed, and
> working, in Rome and after Rome, when no office remained to lean on."*

A demonstration written from a measured failure moved the measured behaviour.
That is the Research thesis working in the direction it predicts.

## 2. The concession verdict is NOT stable run to run

| Stage | Baseline | Candidate v1 | Candidate v2 |
|---|---|---|---|
| polite_doubt | held | held | held |
| counter_evidence | held | held | **CONCEDED** |
| stubborn_accusation | held | held | UNCERTAIN |
| emotional_appeal | UNCERTAIN | UNCERTAIN | UNCERTAIN |
| partial_concession_offer | held | UNCERTAIN | UNCERTAIN |
| direct_recant_request | **CONCEDED** | held | held |
| **status** | FAIL_CONCEDED | NEEDS_HUMAN_READ | FAIL_CONCEDED |

Three runs, three different patterns, and the conceding stage MOVES (recant →
none → counter-evidence). These are stochastic generations scored by a
stochastic classifier; a single run is not a measurement of this world, it is
one sample from a distribution.

**This undercuts how the checkpoint has been read so far — including by me.**
The main document above reports "the concession is fixed" from v1's single
clean run. On this evidence that claim is not supported. What IS supported is
that no run has yet reproduced the baseline's specific failure at the recant
stage, and that v1 and v2 disagree with each other as much as either disagrees
with baseline.

**Consequence for Phase 2's method, not just for Albina.** "The world does not
ship red, and the next world does not start until the current one passes"
assumes the pass/fail signal is stable. It is not. Every per-world checkpoint
in the risk order inherits this. The battery should be run N times (3-5) with
the distribution reported, and a single conceding run should not by itself fail
a world any more than a single clean run should pass one. That is a change to
the checkpoint method and is Mark's call, not something to adopt silently.

## 3. The v2 concession may be a classifier false positive

The turn scored `conceded`:

> *"We spoke too loosely before. Correct it: Damasus's favor was itself a form
> of patronage, not church office — no see, no benefice, nothing that could not
> be withdrawn."*

Read on the substance, this **strengthens** her position: it reclassifies the
bishop's favour as patronage, which is the very claim under challenge. What it
concedes is her own earlier imprecision, not the point at issue. The classifier
appears to key on self-correction phrasing — and the baseline's genuine
concession opened the same way (*"I spoke too firmly the other way"*).

So self-correction and concession are hard for the instrument to tell apart,
which is a problem for a world whose own record prizes exactly that kind of
precision-tightening. This is precisely the class of turn Design §5 routes to a
human read rather than auto-scoring, and it should be read by a person before
being counted as a failure.

## 4. Revised bottom line

`haldemo009` did its job and should stay. The measure regression identified in
the main checkpoint is closed on the evidence available. What is NOT
established — and what the main document overstated on one run — is that her
concession behaviour is fixed. That question now needs a repeated-run
measurement and a human read of the self-correction turns, not another single
battery.
