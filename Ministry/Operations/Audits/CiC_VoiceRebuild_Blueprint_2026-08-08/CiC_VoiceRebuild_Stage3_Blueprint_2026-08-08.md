# CiC Representative Voice Rebuild — Stage 3 (Blueprint)

**Date:** 2026-08-08
**Thread:** Voice Rebuild (brief: `Ministry/Features/Front-End-Integration-Strategy/CiC_Representative_Voice_Rebuild_Fable_Brief_2026-08-05.md`)
**Stage:** 3 of 4, per brief §9. Design (Stage 2) signed off by Mark 2026-08-08 after its adversarial gate reached READY (`../CiC_VoiceRebuild_Design_2026-08-08/`).
**Status:** Draft for Opus adversarial review, then Mark's review. Build has not started.

---

## 0. What this document is

The approved Design turned into an ordered, checkpointed build sequence:
five phases, each work item named with its Design section, every
checkpoint with a stated pass bar and a stated on-fail action, the
brief's risk order preserved for the per-world passes, Mark's queued
decision points placed at their moments, and the brief's
stop-at-a-clean-boundary rule made concrete with named boundaries.
Nothing here re-decides Design; where sequencing exposed a genuine
either/or the Design didn't fix, it is flagged as a sequencing decision
with the chosen order and its reason.

**The one decision needed before Phase 2 starts (not before Phase 0):**
Mark's insight-field scope call (Design §2 Layer 5 / §7) — extend the
prose-style license to `Ecological Function`/`Formation Ecology
Connection` for content-preserving rewrites, or use the
serialization-side strip. Phase 0 and Phase 1 are identical under both
branches; the branch is taken at Phase 2's first world.

---

## 1. Phase 0 — Foundations (build-system work; no voice content changes)

All items are code/schema/harness work with no effect on what any
participant sees until worlds rebuild through them. Items marked [G]
are gates the later phases depend on; sequencing within the phase is
free except as noted.

**0.1 Schema + selector (Design §2 Layer 2, §0):**
- Standardize the demonstration `trait_scores` vocabulary
  (strong/partial/weak) across all six worlds' records; add the
  `required` flag; harden the selector (deterministic rank key;
  zero-demonstration world fails the build). [G]
- Add `ceiling_words` to every `voice_profile.native_measure`, seeded
  with the current `HARD_CEILING_WORLDS` values and their freeze
  rationale; switch the dict to read assembly-fed values
  (behavior-neutral by construction — same numbers, new source). [G]

**0.2 Serialization + leak gate (Design §2 Layer 5):**
- `truncate_at` fail-closed mode for apparatus sections; add
  `## Final Assembly Instruction` to `_VOICE_UNSAFE_SECTIONS`. [G]
- The tiered build-time leak gate: hard-fail on unambiguous apparatus
  (Final Assembly blocks, template/builder references, gravity codes and
  Doc_/Force refs inside EF/FEC bodies), report-only for Usage Guidance
  and out-of-section hits. Reuses the Research leak instrument's refined
  pattern class. [G]
- Retrieval tier-ordering (the confirmed-cheap addendum): sort key on
  `doc.metadata["tier"]` before the per-document loop — bundled here
  because it touches the same file, per Design §2.

**0.3 Assembly generalization + capsule reconciliation (Design §1):**
- Five per-world prompt assemblers on the S52 segment pattern (replacing
  the `DELIBERATELY TEMPORARY` generators); assembly-identity check
  wired (deployed file == assembly output, per world, in CI or the gate
  runner). [G]
- Capsule: parallel-emit transition (existing emitters regenerate the
  capsule from the same records that feed the prompt), with the S6.5
  fold-in scheduled as its own item at Phase 3 — the fold-in changes
  what the runtime reads, so it lands after all six worlds' records are
  rebuilt, not during.
- Readability gate wired at assembly time (per-world floor from
  `wrs/parameters.yaml`), warn-only in Phase 0 (no rebuilt content yet),
  enforcing from Phase 1 on. [G]

**0.4 Instruments (Design §5):**
- Per-signal drift surfacing + `declining_initiative` signal; surface
  `over_settling_logging` confirmed-rate and
  `length_ceiling_logging` events into the probe harness. [G]
- Extend the probe harness's scenarios to all six worlds (it covers
  the two probe worlds today); add the sustained-disagreement 6-turn
  scripts per world (extending `scripts/freeze_battery.py`'s harness
  shape); write the Objective-3 checklist instrument sheet from the
  Research §6 rubric rows. [G]
- Commit the pre-rebuild baseline set: re-run the full battery
  (8-turn + disagreement) against ALL SIX current worlds and commit
  transcripts + metrics. This is the missing durable baseline the brief
  asked for, produced with the extended harness rather than recovered
  from the uncommitted artifacts. [G]

**Checkpoint 0 (exit Phase 0):** all [G] items green; assembly-identity
holds for Desert (already true) and produces stable output for the
other five (identity with deployed NOT expected yet — deployed is still
hand-authored until each world's Phase-2 pass); leak gate runs clean on
hard-fail classes or names exactly the files Phase 2 must fix; baseline
battery committed for six worlds. **On fail:** fix within Phase 0;
nothing in Phase 1+ starts on a red foundation item it depends on.

---

## 2. Phase 1 — Pilot, dual-track (the brief's "pilot first, isolated," made concrete)

Two tracks, run in either order or interleaved, each with its own
checkpoint; both must pass before Phase 2.

**1A — Shared-block pilot against Chloe (brief §7 Part A's mandate).**
Rewrite `_HOW_YOU_ENGAGE` per Design §2 (bridge-first, candidate-offer,
callback license, lead-with-insight with both field names + filter
requirement, three-way disagreement license, shape repertoire; turn
measure stays). Run against Chloe alone, live, before any other world
sees the change.
- **Checkpoint 1A pass bar:** Chloe's battery does not regress from her
  Phase-0 baseline on any failure measure (reclarify 0, no new
  register/measure violations, fabrication 0 confirmed); at least
  directional improvement on uptake/bridge-first measures; Objective-3
  read scores at or above baseline. **On fail:** iterate the shared
  block against Chloe only; two consecutive failed iterations = stop and
  bring findings to Mark before proceeding (a shared-block approach that
  can't pass the pilot is a Design-level problem, not a retry problem).

**1B — Assembly proof on Desert (Design §4 item 4's "freezes the
fleet-wide segment design").** Papnoute's records through the
generalized machinery: schema-normalized scores, hardened selector,
leak gate, readability gate, assembly-identity. His six demonstrations
are NOT yet rewritten in this phase (that's his Phase-2 pass); 1B
proves the *machinery* reproduces his current held quality.
- **Checkpoint 1B pass bar:** assembled Desert prompt remains
  byte-identical to deployed (machinery didn't drift it); his 8-turn
  battery re-run holds at his Research-stage profile (0/8 failure
  measures). **On fail:** the segment design iterates until Desert
  holds; no other world's assembler is trusted before Desert's is.

**Stop boundary A (brief §9):** after Phase 1 is a named clean stopping
point — foundations + pilot proven, no world's voice yet changed.

---

## 3. Phase 2 — Per-world passes, risk-ordered (brief §7: Albina → Marius → Theon → Papnoute → Chloe → Yausep)

Each world's pass, identical structure (Design §4's per-world content):
1. Records rebuilt fresh from that world's sources: voice_profile
   register/craft prose, world_core/world-ground content (capsule prose
   in scope), 3–5 fresh demonstrations incl. the world's targeted one
   and one caveat-carried story demonstration; per-world post-history
   guard export; insight-field pass per Mark's branch (rewrite or
   strip).
2. Assemble; all build gates green (leak hard-fail, readability floor,
   selector, assembly-identity vs the new output).
3. **Checkpoint (per world):** the full battery live — 8-turn probe +
   6-turn sustained-disagreement + confidence-under-thinness and
   Sustained Engagement categories — measured against the world's
   Phase-0 baseline and the redefined parity criterion
   (identity/fact/boundary SAME-VOICE; register/measure graded against
   rebuilt targets). Pass bar: no failure-measure regression vs
   baseline; register/measure hit the world's recorded targets;
   fabrication 0 confirmed; Objective-3 read ≥ baseline; ceiling
   regenerations rare (reported). **On fail:** fix records, reassemble,
   re-run — the world does not ship red, and the next world does not
   start until the current one passes or Mark explicitly re-scopes.
4. Per-world decision points, at their moments (Design §7): **Albina's
   checkpoint** carries her values call — if her rebuilt output exceeds
   the floor, the checkpoint pauses for Mark's decision
   (shorten vs recorded exception) before she ships.

Sequencing note (the one genuine either/or Design left): the brief's
risk order puts Albina and Marius first — the two highest-risk voice
rebuilds run before the machinery has processed a *rebuilt* world
end-to-end (Phase 1B proves it on current records). Blueprint keeps the
brief's order because its rationale (highest-register-shift,
least-validated first — maximum information soonest, while budget is
freshest) outweighs the alternative (run Papnoute's low-risk rebuild
first as a full-pipeline shakedown), and because Phase 1B already
provides the shakedown on the world where the bar is best defined. The
alternative and its reason are recorded here so the choice is visible,
per the Standing Practice's own preference for named decisions.

**Stop boundary B (brief §9's own example):** after Albina + Marius —
the two highest-risk worlds rebuilt, verified, shipped.

---

## 4. Phase 3 — Fleet closure

- S6.5 capsule fold-in (world-ground into the assembled prompt; capsule
  surface reduced per Design §1) — now safe, all six worlds' records
  rebuilt. Re-run assembly-identity + spot batteries after.
- Facilitator contrast-phrase replacement (three sites), written against
  the actual rebuilt voices; relational-safety probe category re-run
  (Design §4's seventh output).
- `HARD_CEILING_WORLDS` trigger-behavior verification in Interview mode
  (the prose-vs-code gap flagged 2026-08-08: current 60-word Desert
  ceiling demonstrably didn't bind solo turns in the Research probes —
  verify what the assembly-fed ceilings actually do, per mode, and
  record it).
- Governance decision points, with Mark, on the measured data (Design
  §3's pre-committed rules): over_settling stage-2 downgrade decision
  (confirmed rates now exist per world); confirmed_glosses
  with/without check on one world, retirement decision fleet-wide.
- Fleet regression: full battery on all six rebuilt worlds in one pass;
  commit as the new baseline set.

## 5. Phase 4 — Framework + record of decisions (Objective 5)

- Part Five and Part Eight updates per Design §6 (all four brief-required
  additions + this design's own, the probe category pointing at named
  instruments) — written last so they document the proven system, not
  the intended one.
- Decision Log entry closing the thread: what shipped, every Mark
  decision with its data, the standing instruments and their locations,
  and what world #7 inherits.

**Final checkpoint:** Part Five/Eight updated; fleet baseline
committed; every §7 Design decision recorded with its outcome; the
thread's Build stage ends with a summary to Mark.

---

## 6. Checkpoint discipline (applies to every checkpoint above)

Adversarial review gates the *stages*; checkpoints gate the *work*.
Each checkpoint: instruments run, numbers recorded in the phase's
results file (committed), pass/fail stated against the written bar —
never "reads fine." A checkpoint that fails twice consecutively
escalates to Mark with the data rather than iterating silently. Every
checkpoint's artifacts (transcripts, metrics, gate outputs) commit with
the pass — the auditability the Research stage's uncommitted-baselines
gap taught.

## 7. Budget and stop behavior

The expensive line is live batteries: ~14 turns per world per
checkpoint (8 probe + 6 disagreement) plus regressions — on the order
of 15–20 full-battery runs across all phases including failures and the
fleet regression, at the Decision Log's measured per-turn cost (Sonnet
main + Haiku monitoring, ~$0.08–0.09/turn). Phase 0/1 spends little
(one pilot world + one proof world + the six-world baseline). If budget
runs short mid-Phase-2, the stop boundaries above are the clean exits —
per-world passes are self-contained, and a world verified green ships
independently of the ones behind it.
