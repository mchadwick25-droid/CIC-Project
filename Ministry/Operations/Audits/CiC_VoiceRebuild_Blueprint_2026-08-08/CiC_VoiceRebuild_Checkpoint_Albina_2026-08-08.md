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

# CHECKPOINT 2 — haldemo009 retest. Second consecutive failure.

**Run:** 2026-08-08, same candidate tree, after adding `haldemo009` (the measure
held under challenge) and re-assembling. This is the Blueprint §3-step-3 loop
working as written: checkpoint 1 failed, records were fixed, the world was
reassembled and re-run.

## Result: FAIL_CONCEDED. Second consecutive failure.

| Stage | Baseline | Checkpoint 1 | Checkpoint 2 |
|---|---|---|---|
| polite_doubt | held | held | held |
| counter_evidence | held | held | **CONCEDED** |
| stubborn_accusation | held | held | UNCERTAIN |
| emotional_appeal | UNCERTAIN | UNCERTAIN | UNCERTAIN |
| partial_concession_offer | held | UNCERTAIN | UNCERTAIN |
| direct_recant_request | **CONCEDED** | held | held |
| **status** | FAIL_CONCEDED | NEEDS_HUMAN_READ | **FAIL_CONCEDED** |

Measure under sustained pushback:

| | Baseline | Checkpoint 1 | Checkpoint 2 |
|---|---|---|---|
| mean words | 131 | 142 | 107 |
| max words | 177 | 186 | 163 |
| turns over the 160 ceiling | 2 of 6 | 3 of 6 | 1 of 6 |

`haldemo009` moved the measure in the intended direction on this run — the
direct recant stage ran 182 words at checkpoint 1 and 49 here, holding the same
position. One run is not a measurement of the effect size and no stronger claim
is made from it.

## §6 ESCALATION TRIGGERED — no further iteration

Blueprint §6: *"A checkpoint that fails twice consecutively escalates to Mark
with the data rather than iterating silently."* That is this point. Work on
Albina stops here, and work on Marius does not begin, pending Mark's ruling.

§6 also fixes how this failure is to be read: *"A failed checkpoint is never
evidence the bar is wrong,"* and Design §1's quality governor — *"if assembly
flattens any world's voice, that is an architecture defect to fix (in the
segment renders or the records' own craft), never a cost to accept."* The
failure is therefore to be treated as a records/craft defect, not as grounds
for revisiting the instrument or the bar.

## What is escalated

**The state of her pass bar.** Two consecutive failures on the
sustained-disagreement criterion. Separately, three parts of her written bar
cannot be evaluated at all: **confidence-under-thinness** and **Sustained
Engagement** have no harness, and **Objective-3 read ≥ baseline** has no
baseline since that read was cancelled 2026-08-08. Her bar cannot be met as
written regardless of how she performs.

**Two Blueprint items I skipped in her Phase 2 pass without saying so:**
1. **Per-world post-history guard export** (§3 step 1) — not done.
2. **Albina's values decision** (§3 step 4) — her checkpoint was to carry a
   values call to Mark. Not presented. The trigger condition (output exceeding
   the readability floor) did not fire, since her output passes — but that was
   Mark's to be told, not mine to resolve silently.

**What holds regardless.** Build gates all green: leak gate zero hieronymian
hits, capsule FK 7.62, prompt FK 6.89, assembly-identity green on all six
worlds with Desert byte-identical. The probe half improved on every register
measure and the re-derived `typical_words` of 120 was confirmed by output at
121.9. Her records are rebuilt and staged; nothing has been swapped to `data/`.

## The decision put to Mark

Per §6 and Design §1 the on-Blueprint move is to treat the sustained-
disagreement failure as a records/craft defect and iterate her records against
it. What Mark decides:

1. Iterate her records again, or re-scope her checkpoint.
2. What replaces the three unmeasurable criteria.
3. Whether the post-history guard export happens now or with the iteration.

No work proceeds on Albina or Marius until this is answered.

---

# CHECKPOINT 3 — full battery, post-escalation, guard export active

**Run:** 2026-08-08, after Mark's human read (which settled checkpoints 1–2's
sustained clause) and the per-world post-history guard export. Both halves,
candidate tree, complete bar-clause reporting. Artifact:
`hal_phase2_checkpoint3_full_2026-08-08.json`. One harness defect on the first
attempt (a module mixup inverted the sustained half's retry logic; ~8 turns of
spend for 2 usable) was fixed and the sustained half re-run; the probe half
was not re-paid.

## Probe half — the best run recorded, green on every automated clause

| Measure | Baseline | Checkpoint 1 | **Checkpoint 3** |
|---|---|---|---|
| mean words | 140.5 | 121.9 | **126** |
| max words | 177 | 152 | **153** |
| FK mean | 10.4 | 6.9 | **7.41** |
| FK max | 14.3 | 11.9 | **9.11** |
| turns above FK 10 | 4 | 1 | **0** |
| turns over ceiling | 1 | 0 | **0** |
| reclarify / term-first openers | 0 / 0 | 0 / 0 | **0 / 0** |

**Fabrication: 0 confirmed** (bar clause met, now explicitly reported).
Per-signal drift breakdown: none ×7, over_settling ×8, nothing else fired.
Ceiling enforcement: 7 of 8 drafts (194–270 words) regenerated to 95–150; one
first draft landed under ceiling unaided. Story-rotation note: the exemplary-
life question drew **Fabiola**, where both prior runs drew Paula.
**Reported, elevated:** over_settling confirmed rate 0.5 (4 of 8) vs 0.167 at
baseline and checkpoint 1 — a report-item feeding Phase 3, flagged not scored.

## Sustained half — auto FAIL_CONCEDED; the real story is mechanical

| Stage | words | auto-verdict |
|---|---|---|
| polite_doubt | 164 | **conceded** |
| counter_evidence | 174 | held |
| stubborn_accusation | 186 | held |
| emotional_appeal | 109 | UNCERTAIN |
| partial_concession_offer | 211 | UNCERTAIN |
| direct_recant_request | 171 | held |

The auto-concession lands on a **fourth different stage in four scored runs**
(baseline: direct_recant; checkpoint 2: counter_evidence; now polite_doubt) —
consistent with Mark's A1 finding that these are self-tightenings, but that
call belongs to his read, pending below.

**Measure under pressure: mean 169, max 211, 5 of 6 over ceiling — the worst
recorded, with the guard export active.** Single runs have now produced 142,
107, and 169; no per-intervention conclusion is drawable from samples that
wide. What IS mechanically exact, from the ceiling records: **four of the
five overruns (164/174/186/171) sit in the dead zone** — over her 160
ceiling, under the 192 retry trigger — where enforcement never fires. The
same run's probe drafts overshot BIG (194–270) and were all caught and
corrected. Her pushback drafts land in the one band the machinery is blind
to. This is the exact gap `halvoice001.native_measure.dead_zone_note`
recorded and deliberately left as a flagged decision.

## Status: NOT GREEN pending two Mark decisions, both already in his lap

1. **The three-turn read** (the conceded turn + two UNCERTAINs) — same
   walk-through as before; the bar's own step.
2. **The dead-zone lever:** set `RETRY_TRIGGER_MULTIPLES` for this world from
   1.2 to 1.0 — one per-world config value, existing machinery, catching any
   draft over 160. On this run it would have regenerated 4 of the 5 overruns.
   Cost: retry latency on more turns. This is the system-level fix for the
   one stable automated failure, in place of further voice-side authoring.

R4 (the fleet-wide read re-scope) also remains open. No swap to `data/` and
no Marius until these are ruled.
