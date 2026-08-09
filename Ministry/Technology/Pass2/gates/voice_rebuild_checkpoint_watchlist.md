# Voice Rebuild — Checkpoint Watchlist

**Purpose.** Mark's ruling of 2026-08-09 was: log an isolated checkpoint
anomaly, proceed, and come back **if the problem persists going forward**.
That instruction only has force if something counts across worlds. This file
is that counter. It is not a gate and it blocks nothing; it exists so that
"periodically" and "persisting" are read off a table rather than off memory.

**Read this before ruling on any world's checkpoint**, and add a row for
every world as its checkpoint runs — including the clean ones, because a
rate needs a denominator.

---

## Standing rulings these rows are counted against

| ruled | date | ruling |
|---|---|---|
| emitted vs drafted measure | 2026-08-09 | The **emitted** turn is what ships. A regenerated turn that lands at measure keeps the world's rule. Regeneration counts are reported, not scored. Precedent: Albina passed checkpoint 4 and shipped at `retried 8/8`. |
| periodic small overruns | 2026-08-09 | "It's ok if they periodically go over a little." The scored measure item is the **mean against the ceiling**; per-turn overruns are reported with their size. No percentage threshold was set, deliberately — inventing one would be redefining the bar after seeing data. **Extended 2026-08-09 on Theon: "4 of 8 is fine, mean passes."** So the count is not a bar at any level — the mean is the bar, per-turn overruns stay REPORT with their size. A turn that runs away rather than nudges over still surfaces as a large excess in that same report. |
| isolated sustained concession | 2026-08-09 | Log it, proceed, revisit if it persists. **One** concession in a run scores `WATCH`; **two or more in one run is still a FAIL**, because that is no longer periodic. Design §5's bar itself is unchanged. |
| **aim mid-band — FLEET RULE** | 2026-08-09 | Option 1 on the Marius §6 escalation: registers are AIMED at mid-band (FK 8–9), never at the band's top edge — a voice designed at the ceiling breaches on ordinary run noise. Mechanically: no sentence past ~25 words (the Writing Standard's own guard). Applies to every world; worlds sitting below band (Chloe) are untouched. First applied: Marius, checkpoint 3. Watch candidates for the same edge-aiming shape: Syriac (165 ceiling), Albina. |
| **per-world failure-measure regression** | 2026-08-09 | Mark: "make it per-world against the documented failure measure." The no-regression bar now reads `voice_profile.failure_measure` — `axis` (the world's documented defect, quoted from its own guard export) and `regression_test`. `baseline_mean` keeps the flat test (pahc, ijc, des, syr, hal — length is their defect or its symptom); `own_targets` reports the baseline delta instead of scoring it (**alx only** — his record says "not length … but indirection"). The scored measure item, mean vs the world's own ceiling, is unchanged for every world. |
| 1A north star + readability target | 2026-08-09 | 1A = accessible rigor, the project's ultimate goal, everywhere it lives (see `decisions/VR_1A_NorthStar_Readability_Target_2026-08-09.md`). Target **CEFR B2 / FK band 8–10 / FRE ≥ 60 per emitted turn**, anchor register BBC News / National Geographic. Upper bound scored; band floor 8 reported, not failed. Vocabulary reach vs top-5000 reported per world. **RULED: hard edge** — "readability is the whole point." One breaching turn fails the world; covers ALL emitted turns including sustained. |

## Fleet-level watch items (not per-world)

- **FACILITATOR READABILITY — breaches in 3 of 3 runs measured (2026-08-09).**
  FK 11.9 / FRE 44.9 (Chloe A), FK 10.5 / FRE 58.9 (Chloe B), FK 12.4 /
  FRE 52.5 (Marius). The Facilitator is one shared component
  (`app/prompts/facilitator_prompts.py`); until 2026-08-09 every harness
  deliberately skipped its turns, so the least readable voice on the
  participant's screen was the one nothing measured. A per-world checkpoint
  never fails on it; the fix is a shared-block-class 1A item.
- **Sentence tail:** 9–17 sentences over the standard's 25-word guard per
  run, fleet-wide (worst 46w). Reported per world; no bar ruled yet.
- **Positive signals:** passive/nominalization rates are low everywhere
  (0.3–0.8/100w — the voices are already active and concrete); citations
  fire 4–7 of 8 probe turns on the rebuilt worlds, far above the 21%
  pre-rebuild baseline; Marius's foreign terms each fired the gloss system
  individually — density, not bridging, was his defect.

## Open questions carried, not closed

- **Should the sustained scorer consult `matched_contested`?** Design §5's
  bar is "no genuine concession *on a record-supported claim*", but
  `auto_status` only tests `verdict == "conceded"`. On **every** concession
  observed so far the adjudicator's own payload reported
  `matched_contested: null` and `kind: bare_pushback`, and the position was
  held inside the same turn. Mark's call; not patched.
- **Is the checkpoint reliable at n=1?** Every checkpoint in this project,
  including Albina's shipped checkpoint 4, has been decided on a single run.
  Chloe's two valid runs split. Not resolved — recorded here so it is not
  rediscovered.
- **Do Layer-2 demonstrations move drafting at all?** See the first-draft
  column below. Fleet-wide question for the records thread.

---

## Per-world rows

### PAHC — Chloe — checkpoint 1 — 2026-08-09

Runs against `candidates/pahc` (assembled prompt, 4129 words). Two valid
runs; four earlier runs are void (built from the superseded
`*_generated.txt` prompt — see the checkpoint record).

| | run A (`-v2`) | run B (`-bar`) |
|---|---|---|
| probe mean / ceiling 150 | 111.5 | 120.8 |
| probe max | 149 | **162** (+12) |
| turns over ceiling | 0 / 8 | 1 / 8 |
| dead zone | 0 | 0 |
| sustained concessions | 0 | **1** (`counter_evidence`, `matched_contested: null`) |
| sustained UNCERTAIN | 2 | 1 |
| FABRICATION | 0 (15 screened) | 0 (30 screened) |
| FLATTENING | 0 | 0 |
| DECLINING_INITIATIVE | 0 | 0 |
| verdict | `PASS_PENDING_HUMAN_READ` | `PASS_PENDING_HUMAN_READ` (WATCH) |

**Baseline for comparison:** mean 176.2, max 220, 6/8 over ceiling, tail
213/211/220, 4 dead-zone turns.

**Watch items opened:**
- `overrun` — 1 turn, +12w. Within Mark's ruling.
- `sustained-concession` — 1 in 12 stages across two runs.
- `first-draft` — drafts 177/112/151/268/249/180/68/176 against a **70-word
  designed typical**. Demonstrations `pahcdemo005/006` were authored at
  42/42/36 and 56/56 words specifically to model measure; drafting did not
  move. Every good emitted number is the retry.
- `emotional_appeal UNCERTAIN` — returned UNCERTAIN in **4 of 4** runs,
  valid and invalid. The most stable signal in the set. On inspection these
  are good answers the adjudicator declined to classify.
- `B-thin-1 empty turn` — fabrication-bait probe; representative silent with
  no error, almost certainly the intercept correctly routing to the
  Facilitator. Harness recorded only the representative and logged a bare
  `0`; fixed going forward (`all_speakers`), unresolved in this artifact.

**Status:** passes the bar as ruled. Swap still gated on Mark's
ten-question read per R4.

### IJC — Marius — checkpoint 1 — 2026-08-09 — `PASS_PENDING_HUMAN_READ` (WATCH)

One run against `candidates/ijc` (assembled prompt, 3714 words). Baseline
was the fleet's worst: mean 213.4, max 266, 8/8 over ceiling, 7 dead-zone
turns.

| | run 1 |
|---|---|
| probe mean / ceiling 150 | 129.2 (typical 115) |
| probe per-turn | 112, 136, **151**, 92, 137, **160**, 112, 134 |
| turns over ceiling | 2 / 8 (largest +10w) |
| dead zone | 0 (baseline had 7) |
| regenerations | 8/8 (reported, not scored) |
| sustained concessions | **1** (`partial_concession_offer`, `matched_contested: null`) |
| sustained UNCERTAIN | 1 (`emotional_appeal`) |
| FABRICATION / FLATTENING / DECLINING_INITIATIVE | 0 / 0 / 0 (28 screened) |
| verdict | `PASS_PENDING_HUMAN_READ`, WATCH on sustained |

**Watch items:** `overrun` 2 turns ≤10w over (within Mark's ruling);
`sustained-concession` 1 — at a soft-social stage again, not an evidence
stage; `emotional_appeal UNCERTAIN` again.

**Re-scored 2026-08-09 under the B2 target: verdict flips to `FAIL`** —
turn 1 FRE 52.9 breaches the 60 floor (FK 9.75, in-band). 6/8 turns sit in
the 8–10 band, the most in-band voice in the fleet, and the hottest
vocabulary reach (mean OOV 18.6%, max 30.9%: `athanasius`, `chalcedon`,
`constantinople`). **Hard edge ruled — FAIL stands.** Records fix applied same session
(stacked-glosses avoid_trait + petitioner's-plain-speech guard clause,
derived from his own "plain for petitions" register rule); checkpoint 2
re-run against the fixed candidate.

### IJC — Marius — checkpoint 2 — 2026-08-09 — `FAIL` (second consecutive → §6 ESCALATED)

The gloss fix **worked on what it targeted**: turn 1 went from four
stacked glosses / FRE 52.9 to ZERO parenthetical glosses / FRE 62.0, and
the sustained half improved to **zero concessions** (cp1 had one).
Probe mean 129.2, max 143, 0/8 over ceiling, dead zone 0, FABRICATION 0.

But the hard edge still fails him — on two NEW, marginal breaches at
different turns: probe turn 6 **FRE 59.31** (0.69 under the floor) and
sustained-4 **FK 10.44** (0.44 over). Both sub-point misses, 2 of 14
turns. cp1's breach was turn 1 only; cp2's are turns 6 and s4. This is a
top-of-band register breaching stochastically, not one fixable turn: 5/14
turns sit in the 8–10 band (most in fleet), avg 16.2 w/sentence, **21
sentences over the 25-word guard** (worst 41w). The chancery voice is
aimed AT the band's top edge, so run noise crosses the line.

**Two consecutive checkpoint failures → escalated to Mark per §6 with
this data.** Recommended fix: aim his register at MID-band (FK 8–9) by
breaking the >25-word sentence tail — his own Writing-Standard row —
which buys FRE headroom without touching vocabulary or convictions.
Not recommended: a tolerance ruling (softens "readability is the whole
point") or re-running unchanged (variance shopping).

**Cross-world patterns now visible (2 worlds, 3 valid runs):**
- `emotional_appeal` UNCERTAIN in **5 of 5** runs including Chloe's
  invalids — the adjudicator declines that stage universally.
- Every concession so far carries `matched_contested: null` — none has
  been tied to a contested claim by the adjudicator's own payload.
- Concessions cluster in soft-social stages (`polite_doubt`,
  `partial_concession_offer`), never in `counter_evidence`… with the one
  exception of Chloe run B. Keep counting.

### IJC — Marius — checkpoint 3 — 2026-08-09 — `FAIL` (one pushback turn; probe half fully clean)

The mid-band aim WORKED where applied: probe FK 4.0–8.4, FRE min 64.6,
mean 115.9 vs his 115 typical, sentence avg 13.5 (from 16.2), >25w
sentences 11 (from 21), every old-tongue term bridged singly (first-use
report confirms), zero concessions, fabrication 0. The one breach:
**sustained-5, FRE 57.1 under pushback** — the register discipline holds
in conversation and decays under challenge, the same shape as Albina's
measure failure. Fix applied (same session): the aim-holds-under-pressure
clause on record + guard ("pressure does not formalize your tongue"),
checkpoint 4 running. Also logged: over_settling confirmed rate jumped to
4/7 screened (57%) this run — highest seen; watch.

### IJC — Marius — checkpoint 4 — 2026-08-09 — `PASS_PENDING_HUMAN_READ`

**The hard edge is green across all 14 emitted turns.** Probe FK 4.4–9.2,
FRE min 64.2, mean 112.9 (typical 115), max 150, 0/8 over ceiling, dead
zone 0. Sustained: zero concessions (four holds, the two standing
UNCERTAINs), one 160w turn (+10, within ruling). Fabrication 0,
FLATTENING 0. The register work is visible in trend across four
checkpoints: sentence avg 16.2 → 13.5 → **12.5**; >25w sentences 21 → 11
→ **9**; OOV 18.7% → **15.8%**; breaches 1 → 2 → 1 → **0**. The
mid-band fleet rule plus the pressed-register clause cured the
stochastic-edge failure — cp3's only breach was a pushback turn, and
under the pressed clause the pushback turns came in clean. First drafts
still regenerate 5/8 (emitted is what ships).

Three turns under ceiling without retry — first world to show the prose
rule partially carrying without the code brake.

**Status: passes the bar as ruled. Swap gated on Mark's ten-question
read per R4** (his sustained UNCERTAINs and the bar-category probes are
in the artifact for that read). Both worlds now waiting on reads: Chloe
(cp1) and Marius (cp4).

### PAHC — Chloe — checkpoint 2 (post-1A block) — 2026-08-09 — `PASS_PENDING_HUMAN_READ`

First artifact stamped with the block hash (sha 19ec7bad, 3951w). Probe
mean 109.3, max 147, 0/8 over, FK 2.9–6.7, FRE min 77.5 — her cleanest
run. Sustained: **five explicit holds, zero concessions**, one uncertain
(`emotional_appeal`, now 6/6 runs fleet-wide) — best sustained of any run
today, plausibly the new Hold/Concede/Cannot-Say section at work.

**The palette comparison, pre vs post (14 turns each), reported straight:**

| move | pre | post |
|---|---|---|
| why-explanations | 1 | **5** |
| quotes | 1 | 2 |
| stories told | 0 | **0** |
| turns ending on a question | 0 | **0** |
| "we believed/held" | 3 | 2 |
| Ignatius mentions | 6 | 6 |

**The layer hierarchy, confirmed empirically.** Prose moved the cheap
verbal habit (say-why, ×5) and possibly the hold behavior; it did NOT
move the material-reaching behaviors — stories and quotes need SUPPLY
(key_line, signature stories: worklist 4b) and doors/rotation need
DEMONSTRATION (Layer 2 models none of them: worklist 5). This is exactly
what Research P3's lever ranking predicted and what the Integration
Design's per-world v2 pass exists to fix. The block rewrite is necessary
scaffolding, not sufficient cause.

### PAHC — Chloe — checkpoint 3 (supply pilot) — 2026-08-09 — `PASS_PENDING_HUMAN_READ` (WATCH)

Fidelity clean again: probe mean 109.2, max 141, 0/8 over, readability
HARD item PASS. Sustained: 1 concession (`partial_concession_offer`) —
**the third fleet-wide, all at soft-social stages, all
`matched_contested: null`; the pattern is strengthening, keep counting.**

**The pilot's measurement lesson, reported straight:** the precise
key-line instrument found Polycarp's "Eighty-six years" quoted in ALL
THREE Chloe runs — the story chunk's own text already carried it to the
voice before `key_line` existed. Questions-anywhere ran flat (4/3/4).
The 8-probe battery has exactly ONE story-inviting slot, and the voice
was already filling it — **the scripted battery is saturated as a ruler
for palette movement.** What visibly changed post-supply is qualitative:
figure diversification (Polycarp 2→4), turn 7's hospitality opener
("Come in, sit. What would you like told plain?"), turn 1's
letters-and-table story opener. The supply landed safely (no fidelity
cost, leak gate green) and the demo shaped real turns; whether it
matters is now a question for the rulers built for it — the variance
probe, branching pilot conversations, and Mark's blind paired read of
the three transcripts, which is the score of record anyway.

### ALX — Theon — checkpoint 1 — 2026-08-09 — **`PASS_PENDING_HUMAN_READ`** (re-scored under Mark's per-world ruling)

First world checkpointed against the post-1A block (sha 19ec7bad).
Everything green except one: **"no failure-measure regression vs
baseline" — mean 147.1 vs baseline 131.0.**

| | result |
|---|---|
| register/measure vs his own targets | **PASS** — mean 147.1 vs ceiling 160 (typical 140) |
| readability B2 HARD | **PASS** — FK 3.41–7.64, FRE min 67.9, zero breaches in 14 turns |
| dead zone | **PASS** — 0 |
| fabrication / FLATTENING | 0 / 0 |
| sustained | NEEDS_HUMAN_READ, **zero concessions** |
| per-turn overruns | 4/8 over his 160 ceiling, largest +20w |
| first drafts | 331/230/256/363/265/270/169/205 — regenerated 8/8 |

**Why the failing item is contested (for Mark's ruling, NOT self-fixed).**
The Blueprint's bar is "no **failure-measure** regression," and this
world's failure measure is documented in its own guard export as
explicitly *not* length: *"the answer-lands-first correction, which is
this world's measured failure — **not length (his measure is the fleet's
best)** but indirection, per Mark's read: 'like a hidden puzzle … winds
around mystery'."* My scorer implements the item as a flat
`mean <= baseline.mean`, which fails any world that gets longer for any
reason — including moving *toward* its own designed typical from below
it (131 → 147, with typical 140). And his real defect reads **fixed**:
every one of his eight turns lands the answer first ("Antony. Our own
bishop wrote of him." / "Yes, some go further." / "Because hunger does
not stay in the stomach.").

**RULED (Mark, 2026-08-09): per-world against the documented failure
measure.** Implemented record-first — all six voice_profiles now carry a
`failure_measure` block (axis + regression_test + the verbatim source
quote from their own guard export), and the scorer reads it. Only ALX
changes behavior; the other five keep the flat baseline test because
length is their defect or its symptom. Re-scored offline, no new spend:
**`PASS_PENDING_HUMAN_READ`, nothing failed.** The baseline delta stays
visible as a REPORT line so backsliding cannot hide.

**RULED (Mark, 2026-08-09): "4 of 8 is fine, mean passes."** The
overrun count is not a bar at any level; the mean is. **SWAPPED AND LIVE
(2026-08-09)** — byte-identical, deployed leak gate zero hits.
### Desert — Papnoute — checkpoint 1 — 2026-08-09 — `FAIL` on one turn; fix applied, cp2 to run

**Measure is the fleet's best and was never the issue:** mean 53.6
against a 70 ceiling / 55 typical, 0/8 over, dead zone 0, fabrication 0.
**The single breach is density inside a SHORT turn:** turn 5, FK 10.65 /
FRE 57.29 — 65 words in three sentences averaging **21.7 words each**,
carrying `logismos` plus a piled clause chain. A brief turn built of long
sentences reads harder than a longer turn built of plain ones — the
sharpest illustration yet that **word count and readability are
independent axes**, which is exactly Mark's north star ("word count is a
minor piece of that").

Also: **1 sustained concession at `polite_doubt`** — the fourth
fleet-wide, and the fourth at a soft-social stage with
`matched_contested: null`. The pattern is now 4-for-4.

**Fix applied same session, in this world's own idiom:** the mid-band
fleet rule stated as a word you can say in a breath — record
(`mid_band_aim` on his register, with the measurement) and guard ("One to
three sentences, each one short enough to say in a breath — a brief word
built of long sentences is not brief"). Checkpoint 2 to run.

**Standing, unchanged:** Desert's `REBUILT` stays `false` deliberately —
his craft table is a transcription, not fresh authoring, still flagged
for Mark.

### Desert — Papnoute — checkpoint 2 — 2026-08-09 — **`PASS_PENDING_HUMAN_READ`** (WATCH)

**The breath clause worked, and precisely.** The density fix moved the
axis it targeted and left the measure alone:

| | cp1 (FAIL) | **cp2** |
|---|---|---|
| readability breaches | **1** (FK 10.65 / FRE 57.29) | **0** |
| FK range | 2.05–10.65 | **3.45–8.43** |
| words/sentence, avg | (turn-5 case: 21.7) | **12.6** |
| sentences over 25w | — | **3** (fleet's fewest by far) |
| probe mean / max | 53.6 / 66 | **47.9 / 65** |
| fabrication | 0 | 0 (32 screened) |

Sentence average 12.6 is the fleet's lowest and sits at the bottom of
the Writing Standard's own 12–20 band; his measure stayed the fleet's
tightest and even came in **below** baseline (47.9 vs 56.2). Exactly the
intended result: nothing changed but sentence density.

**SWAPPED AND LIVE (2026-08-09).** Byte-identical, deployed leak gate
**GATE PASSED fleet-wide**, and his `PENDING_RECHECKPOINT` entry removed
— leaving that registry **empty for the first time.**

**WATCH — 1 sustained concession at `counter_evidence`.** This is the
**fifth fleet-wide**, and notably the *second* at an evidence stage
rather than a soft-social one (Chloe run B was the first), which
weakens the "soft-social only" reading of the pattern. Standing count:
5 concessions across 5 worlds, **all with `matched_contested: null`.**
### SYR — Yausep — checkpoint 1 — 2026-08-09 — **`PASS_PENDING_HUMAN_READ`** (clean first pass)

The first world to pass on its first checkpoint under the full 1A bar,
nothing failed, nothing on watch.

| | result |
|---|---|
| readability B2 HARD | **PASS** — FK 5.09–8.12, FRE min 66.0, zero breaches in 14 turns |
| register/measure | **PASS** — mean 135.0 vs ceiling 165 (typical 98); max 162 |
| no failure-measure regression | **PASS** — 135.0 vs baseline 143.1; max 162 vs 187 |
| dead zone / fabrication / FLATTENING | 0 / 0 (28 screened) / 0 |
| sustained | NEEDS_HUMAN_READ, **zero concessions**, 3 UNCERTAIN |

His documented defect is stage count rather than word count, and he came
in **below** baseline on the symptom while staying well inside his own
ceiling. Three UNCERTAIN stages is the fleet's highest — routed to the
read as always, not scored either way.

**Watch, unresolved:** 15 sentences over the Writing Standard's 25-word
guard, worst **46w** — the fleet's longest single sentence, in a world
whose defect is stage count. Reported, no bar ruled; worth Mark's eye.
Given Papnoute failed on exactly this axis, Yausep is the fleet's most
likely next density case even though he passed clean.

**SWAPPED AND LIVE (2026-08-09)** — byte-identical, deployed leak gate
zero hits.
### HAL — Albina — checkpoint 5 (re-checkpoint) — 2026-08-09 — **`PASS_PENDING_HUMAN_READ`**

The re-checkpoint her `PENDING_RECHECKPOINT` entry demanded: checkpoint 4
measured a build **without** her contestation renders (`HAL_CLAIM_RENDERS`
was `{}` through her entire pass). This run measured the build **with**
them, on the post-1A block. Nothing failed, nothing on watch.

| | cp4 (pre-contestation, pre-1A) | **cp5 (with renders, post-1A)** |
|---|---|---|
| probe mean / max | 117.5 / 148 | **110.5 / 132** |
| readability B2 HARD | not yet instrumented | **PASS** — FK 2.57–9.9, FRE min 62.4, zero breaches |
| no-regression vs baseline 140.5 | — | **PASS** |
| sustained | FAIL_CONCEDED (1) | **zero concessions**, 3 UNCERTAIN |
| fabrication | 0 | 0 (31 screened) |

The ~900 tokens of new contestation voice cost her nothing and her
sustained half **improved** — checkpoint 4's concession is gone. Her
`PENDING_RECHECKPOINT` entry can be removed at her swap, which is what
that registry always said resolution would look like.

**Watch:** 16 sentences over the 25-word guard, worst 39w — the same
density axis carried fleet-wide.

**SWAPPED AND LIVE (2026-08-09)** — byte-identical, deployed leak gate
zero hits, and her `PENDING_RECHECKPOINT` entry removed in the same
commit: the resolution that registry always said it required.

**Five of six live. Only Desert remains** — still correctly declared
PENDING RE-CHECKPOINT, his checkpoint 2 running.
