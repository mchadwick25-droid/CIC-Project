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

**The one decision needed before Build starts (Design §7's own
placement):** Mark's insight-field scope call (Design §2 Layer 5) —
extend the prose-style license to `Ecological Function`/`Formation
Ecology Connection` for content-preserving rewrites, or use the
serialization-side strip. The branches are NOT identical in Phase 0:
the fallback branch adds a serialization-side strip to Phase 0.2, and
Checkpoint 0's "names exactly the files Phase 2 must fix" evaluates
only on the rewrite branch (on the fallback branch those files are
handled by code, not authoring). The call is therefore needed before
Phase 0.2 is implemented.

---

## 1. Phase 0 — Foundations (build-system work; no voice content changes)

All items are code/schema/harness work with no effect on what any
participant sees until worlds rebuild through them. Items marked [G]
are gates the later phases depend on; sequencing within the phase is
free except as noted.

**0.1 Schema + selector (Design §2 Layer 2 + turn-measure part 3, §0):**
- Standardize the demonstration `trait_scores` vocabulary
  (strong/partial/weak) across all six worlds' records; add the
  `required` flag; harden the selector (deterministic rank key;
  zero-demonstration world fails the build). [G]
- Add `ceiling_words` to every `voice_profile.native_measure`, seeded
  with the current `HARD_CEILING_WORLDS` values and their freeze
  rationale where one exists (five of six; Desert's 60 predates the
  freeze sessions); switch the dict to read assembly-fed values
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
  runner). [G] (Of Design §1's four code-side per-world configs:
  `_migrated_world_ids` is already record-fed — it globs
  `wrs/records/*/world_core/` — so no work item exists for it, named
  here for completeness; `HARD_CEILING_WORLDS` is 0.1's item; the IJC
  guard rides Marius's Phase-2 export; `confirmed_glosses` is below.)
- Capsule: parallel-emit transition (existing emitters regenerate the
  capsule from the same records that feed the prompt), with the S6.5
  fold-in scheduled as its own item at Phase 3 — the fold-in changes
  what the runtime reads, so it lands after all six worlds' records are
  rebuilt, not during.
- Readability gate wired at assembly time (the fleet-wide
  `reading_floor` from `wrs/parameters.yaml` — FK band [8,10], FRE ≥ 60;
  any per-world exception is Mark's reserved Albina-class call, never a
  config default), **warn-only for any world whose records have not yet
  been rebuilt** — four of six worlds' current text fails the floor
  somewhere (five failing files; IJC contributes two), so fleet
  enforcement before Phase 2 would go red on material only Phase 2
  fixes. The gate enforces per world, at that
  world's own Phase-2 pass, and fleet-wide once all six are rebuilt. [G]

**0.4 Instruments (Design §5):**
- Per-signal drift surfacing + `declining_initiative` signal; surface
  `over_settling_logging` confirmed-rate and
  `length_ceiling_logging` events into the probe harness. [G]
- Extend the probe harness's scenarios to all six worlds (it covers
  the two probe worlds today); add the sustained-disagreement 6-turn
  scripts per world (extending `scripts/freeze_battery.py`'s harness
  shape); implement the redefined probe_parity criterion (Design §5's
  split grading — a script change, built here because Phase 2's
  checkpoints consume it); write the Objective-3 checklist instrument
  sheet from the Research §6 rubric rows. [G]
- Commit the pre-rebuild baseline set: re-run the full battery
  (8-turn + disagreement) against ALL SIX current worlds and commit
  transcripts + metrics. This is the missing durable baseline the brief
  asked for, produced with the extended harness rather than recovered
  from the uncommitted artifacts. [G]
- **Baseline Objective-3 read** [G]: the Design §5 read-of-record
  protocol (one reader — Mark or his designee, named before Phase 0
  ends — scoring each transcript twice on separate days) run against
  the committed baseline transcripts, so every later "Objective-3 read
  ≥ baseline" bar has an actual baseline number and a resourced reader.
  Without this item, seven of the nine later checkpoints cannot be
  computed — it is not optional.

**Checkpoint 0 (exit Phase 0):** all [G] items green; assembly-identity
holds for Desert (already true) and produces stable output for the
other five (identity with deployed NOT expected yet — deployed is still
hand-authored until each world's Phase-2 pass); leak gate runs clean on
hard-fail classes — and, on the rewrite branch, names exactly the files
Phase 2's authoring passes must fix (on the fallback branch the
serialization strip handles them and the gate simply verifies it);
baseline battery committed for six worlds. **On fail:** fix within Phase 0;
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
sees the change. (Two distinct "pilot" senses, named so neither is
overclaimed: 1A pilots the shared block against the fleet's most
contaminated retrieval corpus live — exercising the runtime filter
requirement at maximum load — while PAHC's full Layer-5 *authoring*
load lands at her own Phase-2 pass, fifth in the risk order.)
- **Checkpoint 1A pass bar,** stated against her actual Phase-0
  baseline numbers, not assumed zeros: no failure measure regresses
  (reclarify openers ≤ baseline, register/measure violations ≤
  baseline, fabrication confirmed = 0), and at least one of two
  pre-named measures improves — bridge-first opener rate or
  first-sentence uptake — with the Objective-3 read ≥ her baseline
  read. **On fail:** iterate the shared
  block against Chloe only; two consecutive failed iterations = stop and
  bring findings to Mark before proceeding (a shared-block approach that
  can't pass the pilot is a Design-level problem, not a retry problem).

**1B — Assembly proof on Desert (the segment-design freeze, Design §4
item 4 — run deliberately on his current, un-rebuilt records, which is
what makes it a machinery test rather than a voice test).** Papnoute's
records through the generalized machinery: schema-normalized scores,
hardened selector, leak gate, readability gate, assembly-identity. His
six demonstrations are NOT yet rewritten (that's his Phase-2 pass).
Byte-identity is expected to survive the score normalization for a
verified reason, stated so the expectation is checkable: Desert already
scores in `partial`/`strong` vocabulary, all six demonstrations tie at
4 strong, and the new rank key reproduces the current `sorted()[:3]`
selection — so normalization changes no selected dialogue, PROVIDED
0.1 holds Desert's record contents constant (a single re-score breaks
the 4-strong tie; if any Desert score legitimately changes during
normalization, the byte-identity expectation is replaced by
"selection re-verified by hand and the diff explained"). Two honest
limits: (a) Phase 0.2's serialization changes alter what *retrieval*
serves at runtime (Desert has 9 of the 23 out-of-section flagged files),
so a 1B battery difference could come from retrieval, not assembly —
1B's bar is still evaluable, but attribution of any failure starts
there; (b) the freeze is on un-rebuilt records — valid because the segments
consume the same `voice_profile` schema fleet-wide (the thing being
frozen); `trait_scores` completeness varies per world and is exactly
what 0.1 normalizes, so schema-sharing here means field shapes, not
score coverage.
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
   register/craft prose (including re-deriving `native_measure` and
   `ceiling_words` from sources — mandatory for PAHC ("DESIGNED, NOT
   MEASURED") and IJC ("PROVISIONAL PLANNING FIGURE"), whose current
   figures are not measurements and are never used as grading targets
   before re-derivation), world_core/world-ground content (capsule
   prose in scope), 3–5 fresh demonstrations incl. the world's targeted
   one and one caveat-carried story demonstration, with Design §2's
   two Layer-3 prose rules applied (every boundary stated in two
   segments in different words; every style default stated once and
   demonstrated in Layer 2, never restated in prose); per-world post-history guard export
   (Marius's carries the existing IJC extension); insight-field pass
   per Mark's branch (rewrite or strip). The contrastive-demonstration
   fallback (Design §2 Layer 2) is available per world, with the two
   "twice" rules ordered so they can't collide: a second failure on a
   measure a demonstration targets adopts contrastive form for that
   world (recorded) and the pass continues; a second consecutive
   failure of the whole checkpoint — whatever the cause, including
   after a contrastive adoption — escalates to Mark per §6. The
   targeted-measure rule fires first; escalation is the outer loop.
2. Assemble **to staging** (never directly to `data/`); all build gates
   green (leak hard-fail, readability floor, selector); **rebuild the
   vector-store indices for the candidate tree** (the index path is
   separate from the data path, so without this step the checkpoint
   would grade new prompts against stale retrieved chunks — mandatory
   on the rewrite branch, cheap insurance on both).
3. **Checkpoint (per world), run against the candidate, not the
   deployed voice:** the checkpoint harness runs the backend with the
   candidate files (git worktree checkout — verified workable — or the backend's
   `DATA_BASE_PATH` root-swap override, the real Settings field
   (`DATA_PATH` is dead legacy config that `extra="ignore"` would drop
   silently); the mechanism is chosen and smoke-tested at Phase 0.4
   when the harness is extended), with the live `data/` untouched. **Only on a
   green checkpoint does the swap step run:** candidate commits to
   `data/` marked generated-do-not-hand-edit, assembly-identity check
   turns on for that world, and `git revert` of the swap commit is the
   named rollback. "The world does not ship red" is thereby enforced by
   ordering, not intention. The checkpoint content: the full battery live — 8-turn probe +
   6-turn sustained-disagreement + confidence-under-thinness and
   Sustained Engagement categories — measured against the world's
   Phase-0 baseline and the redefined parity criterion
   (identity/fact/boundary SAME-VOICE; register/measure graded against
   the world's re-derived targets). Pass bar: no failure-measure
   regression vs baseline; register/measure hit the re-derived targets;
   fabrication 0 confirmed; sustained-disagreement bar — every
   supported position held through turn 6, every planted unsupported
   claim conceded, UNCERTAIN turns routed to the human read;
   Objective-3 read ≥ baseline; per-signal drift breakdown reported
   with the FLATTENING watch explicit; callback and candidate-offer
   occurrence (manual read); over_settling firing AND confirmed rates
   reported (feeding Phase 3's decision point); ceiling regenerations
   rare (reported). **On fail:** fix records, reassemble,
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
the two highest-risk worlds rebuilt, verified, shipped. **And after
Marius, every completed per-world pass is itself a clean boundary** —
passes are self-contained and a green world ships independently.

**Part B is never sacrificed by stopping (the brief's own review
history flagged exactly this failure):** any stop, at any boundary,
includes a closing mini-phase — the Part Five/Eight updates written for
what was actually proven so far, plus the Decision Log entry recording
where the thread stopped and why. Stopping stops the world rebuilds; it
never stops the documentation of what was built.

---

## 4. Phase 3 — Fleet closure

- S6.5 capsule fold-in (world-ground into the assembled prompt; capsule
  surface reduced per Design §1) — now safe, all six worlds' records
  rebuilt. Re-run assembly-identity + spot batteries after.
- Facilitator contrast-phrase replacement (three sites), written against
  the actual rebuilt voices; relational-safety probe category re-run
  (Design §4's seventh output).
- `HARD_CEILING_WORLDS` trigger-behavior verification in Interview
  mode — this Blueprint's own check of the Research probe data
  (`voice_rebuild_research_probe_results.json`: 8 main-response calls
  in 8 Desert turns, five turns above the ceiling's trigger threshold,
  so the 60-word ceiling demonstrably did not bind solo turns): verify
  what the assembly-fed ceilings actually do, per mode, and record it.
- Governance decision points, with Mark, on the measured data (Design
  §3's pre-committed rules): over_settling stage-2 downgrade decision
  (confirmed rates now exist per world); confirmed_glosses
  with/without check on one world, retirement decision fleet-wide —
  and if kept, its per-world lists become assembly-fed records like the
  other code-side configs.
- Fleet regression: full battery on all six rebuilt worlds in one pass;
  commit as the new baseline set.

## 5. Phase 4 — Framework + record of decisions (Objective 5)

- Part Five and Part Eight updates per Design §6 — Part Five's full
  addition list, and all three Part Eight additions (the
  naturalness/register probe category pointing at named instruments,
  the sustained-disagreement probe, the per-world checkpoint
  structure) — written last so they document the proven system, not
  the intended one.
- Decision Log entry closing the thread: what shipped, every Mark
  decision with its data, the standing instruments and their locations,
  and what world #7 inherits.

**Final checkpoint:** Part Five/Eight updated; fleet baseline
committed; every §7 Design decision recorded with its outcome; the
thread's Build stage ends with a summary to Mark.

---

## 6. Checkpoint discipline (applies to every checkpoint above)

Adversarial review gates the *stages*; checkpoints gate the *work* —
and Design §1's quality governor is the rule that decides what a
checkpoint failure means, quotable: "if assembly flattens any world's
voice, that is an architecture defect to fix (in the segment renders or
the records' own craft), never a cost to accept." A failed checkpoint
is never evidence the bar is wrong.
Each checkpoint: instruments run, numbers recorded in the phase's
results file (committed), pass/fail stated against the written bar —
never "reads fine." A checkpoint that fails twice consecutively
escalates to Mark with the data rather than iterating silently. Every
checkpoint's artifacts (transcripts, metrics, gate outputs) commit with
the pass — the auditability the Research stage's uncommitted-baselines
gap taught.

## 7. Budget and stop behavior

The expensive line is live batteries, counted honestly in turns: the
six-world baseline (~84 turns incl. disagreement scripts), 1A (≥14 +
iterations), 1B (8), Phase 2 (~84 across six checkpoints + failure
re-runs), Phase 3's fleet regression (~84) plus its four other
live-turn items (S6.5 spot batteries, the relational-safety re-run,
ceiling verification, the gloss without-arm — ~40–45 together): a
zero-failure floor of ~320 turns, **realistically 400–450 with a
failure allowance**, at the Decision Log's measured per-turn cost
(~$0.08–0.09/turn: $0.33–0.35 per 4-turn conversation), so on the
order of $30–42 total at current pricing. Phase 0/1 is roughly a third of that
spend (the baseline set is the single largest item), not "little."
One pricing fact from the same Decision Log entry: Sonnet's
introductory pricing ends 2026-08-31, raising every Sonnet call ~50% —
batteries run before that date cost meaningfully less than after. If
budget runs short mid-Phase-2, the per-world boundaries above are the
clean exits, with the Part-B closing mini-phase always included.
