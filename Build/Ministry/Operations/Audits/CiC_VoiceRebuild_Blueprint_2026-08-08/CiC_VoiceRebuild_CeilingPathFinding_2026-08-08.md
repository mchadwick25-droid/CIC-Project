# Finding — the length-ceiling mechanism is absent from the non-streaming path

**Found:** 2026-08-08, at the start of Phase 2 (Albina), while pulling her
baseline register numbers. Verified by reading the code paths directly and
cross-checking both committed baseline batteries.

## The finding

`app/graph/nodes.py` implements the hard turn-length ceiling (buffer the
first draft, silently regenerate once if it exceeds `ceiling ×
retry_trigger_multiple`) **only inside `stream_representative_turn`**
(the function serving `/api/session/{id}/message/stream`).

The non-streaming path — `representative_engages` /
`multi_representative_engages`, serving `/api/session/{id}/message` — has
no ceiling logic at all. Verified: the string `ceiling` does not appear
anywhere in `representative_engages`'s body (lines 1439–1508).

Two endpoints, two different enforcement behaviours, no note anywhere
saying so.

## Is production affected? No.

`frontend/src/hooks/useConversation.ts:245` calls `/message/stream` and
nothing else — there is no reference to the bare `/message` endpoint
anywhere in the frontend. **Real participants go through the enforced
path.** The bare endpoint is reachable but unused by the shipped UI.

So this is not a live participant-facing defect today. It is (a) a real
latent inconsistency between two endpoints that both look like "send a
message", and (b) a measurement problem, which is the part that matters
right now.

## What it invalidates

`scripts/voice_rebuild_research_probe.py` posts to `/message`
(line 388) — the **unenforced** path.
`scripts/sustained_disagreement_battery.py` posts to `/message/stream`
(line 217) — the **enforced** path. The two committed baselines were
therefore measured under different enforcement conditions, which nothing
in either file records.

The consequence, measured across the committed probe baseline
(`voice_rebuild_research_probe_results.json`, 8 turns per world):

| World | ceiling | turns over ceiling | would have triggered retry | max words |
|---|---|---|---|---|
| Desert (Papnoute) | 60 | 8/8 | 8/8 | 170 |
| PAHC (Chloe) | 150 | 7/8 | 7/8 | 328 |
| Alexandria (Theon) | 160 | 8/8 | 6/8 | 356 |
| Syriac (Yausep) | 165 | 8/8 | 6/8 | 335 |
| IJC (Marius) | 180 | 7/8 | 5/8 | 307 |
| Hieronymian (Albina) | 160 | 7/8 | 6/8 | 302 |

Every world overruns its own recorded measure on nearly every turn, and
the instrument reported `total_ceilinged_turns: 0` for all six — not
because nothing tripped, but because nothing could.

**Corrected as a result:** the Checkpoint 1B document's length-ceiling
paragraph (see its own inline correction). Its verdict stands — the pass
bar never depended on this instrument — but the claim was wrong and is
now marked as such rather than quietly edited away.

## Why this matters for Phase 2, concretely

Phase 2's per-world checkpoint grades **register and measure against each
world's re-derived targets**, and grades them **against the Phase-0
baseline**. Both halves are affected:

1. **If the checkpoint harness runs the streaming path** (the honest
   choice — it is what participants get), its word counts will be
   post-regeneration and therefore structurally lower than the
   unenforced baseline it is being compared against. A world could look
   like it improved when only the measurement path changed.
2. **If the checkpoint harness runs the non-streaming path** to stay
   comparable with the baseline, it measures something no participant
   will ever see, and "register/measure hit the re-derived targets"
   becomes a claim about a code path that isn't shipped.

Neither option is free. This needs a decision before Albina's checkpoint
runs, not after.

## The options, with their real costs

- **(a) Re-run the probe baseline on the streaming path** for all six
  worlds, and compare like with like from then on. Costs one more full
  probe battery of real API spend (the six-world probe half was roughly
  $3–6 of the earlier ~$6–12 run). Cleanest, and makes every later
  checkpoint mean what it says.
- **(b) Keep the existing baseline, run checkpoints unenforced, and
  treat ceiling adherence as a separate measurement** taken once on the
  streaming path per world. Cheaper; leaves the headline register
  numbers describing an unshipped path.
- **(c) Fix the asymmetry first** — give `representative_engages` the
  same ceiling logic — so the two endpoints agree, then re-baseline.
  Most correct for the product; largest scope; turns a measurement
  question into a code change mid-phase.

**Not decided here.** Recommendation, for what it is worth: (a) — the
spend is small next to the cost of every Phase 2 checkpoint number being
ambiguous, and (c) can follow later as its own scoped fix since nothing
participant-facing is broken today.

## Also worth recording

This is a second, independent instance of the pattern Research named as
its central thesis — *prose instruction alone under-holds at generation
time*. Albina's `voice_profile` already carries a hard measure
(`typical_words: 94`, `ceiling_words: 160`) and her deployed prompt
states a "hard two-short-paragraph ceiling that holds under weight"; her
measured baseline mean is **240 words**, 2.6× the typical figure. The
instruction is written, and it is not holding. That is a demonstration
input for her rebuild, not just a bug report.
