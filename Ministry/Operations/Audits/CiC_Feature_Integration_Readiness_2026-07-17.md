# CiC Feature Integration Readiness — 2026-07-17

**Scope:** every designed or in-progress front-end/experience feature not yet in
`cic-poc`'s running app — evaluated for what's designed, what's built, what's
tested/validated, what's missing, and a readiness verdict. Companion to
`CiC_Integration_Readiness_Assessment_2026-07-17.md` (which covers the *code already
on the working branch*, diffed against `main`) — this document covers features that
are *not yet in that diff at all*.

**Naming note:** "Christian Movement Scrolling Atlas" doesn't appear anywhere in the
project's actual naming decisions. The feature this most likely refers to is the
**World Orientation Map** (its content spine is separately called the "World Atlas"
census). Evaluated under that name below — flag if a different feature was meant.

---

## Ranked by readiness (closest to integration-ready first)

### 1. World Orientation Map — CLOSEST TO READY

- **Designed:** full spec (`CiC_World_Orientation_Map_Spec_V0_1.md`), visual
  architecture, a 178+-entry World Atlas census.
- **Built:** an interactive HTML demo (V0.5, with a scripted tour mode, GIF/slideshow
  recording), AND — unlike every other feature below — **real integration code
  already exists**, wired into `cic-poc` on `claude/world-map-integration-exploration`
  (commit `de11233`): a link from the world-selection screen opening `/world-map/`,
  and a URL handoff contract (`/?worlds=<id,id>&mode=<interview|table>`) that
  preselects worlds in the existing selector.
- **Tested:** `tsc --noEmit` clean, the branch's own log records "Verified live,"
  practicality-tested at desktop and phone sizes with measured fixes applied.
- **Missing before merge:**
  - **Tier B decision** — does the map become the *primary* world-selection surface,
    or stay a secondary "orientation" option alongside the existing tile selector?
    This is a real scope decision, not a technical gap.
  - **WID→world-id mapping is hand-synced**, not auto-generated — a real drift risk
    if a world's ID ever changes and this mapping isn't updated in lockstep. Flagged
    to auto-generate at Tier B, not yet done.
  - Homoian Christianity's governance tension (Article-level) still unresolved.
  - Several remaining census judgment calls need Mark's confirmation.
  - **Standing rule applies regardless of readiness:** held through Prototype
    Testing 1 per every other feature's own rule — the front-end thread owns the
    actual merge call.
- **Verdict: technically the most integration-ready designed feature in the whole
  queue** — real, tested code sitting on a branch, not just a design doc. What's
  blocking it is a scope decision (Tier A vs. B) and the standing pilot-timing rule,
  not missing engineering work.

### 2. Front-End Integration Strategy Increment 1 (budget compliance / citation UI)

- **Designed:** full spec — the three-tier disclosure vocabulary, numeric clutter
  budget, five-count screen check.
- **Built:** the citation-UI half of Increment 1 (inline hover/click migration,
  `CitationMarker.tsx`/`CitationModal.tsx`) is **already built and sitting on the
  working branch** — this was verified today (2026-07-17) as part of the integration
  readiness pass: matches the strategy's own verdict ("passes by grammar"), no
  conflict found.
- **Tested:** verified against the strategy's actual rule text; the table-bar
  consolidation half of Increment 1 has not been separately confirmed.
- **Missing:** the Front-End Graphics thread (launched today) hasn't produced any
  mockups yet to confirm the *whole* screen (not just citations) actually passes the
  five-count check. Table-bar consolidation status unconfirmed.
- **Verdict: partially ready** — one real piece (citations) already done and verified;
  the rest of Increment 1 needs the Graphics thread's first deliverable before it can
  be called complete.

### 3. Representative Modes (user/role selection) — DESIGN + BUILD DONE, VALIDATION IS THE GATE

- **Designed:** full spec, prompt architecture, four roles (general/pastor-teacher/
  academic/reevaluation).
- **Built:** exploration branch (`claude/representative-modes-exploration`, commit
  `1127c09`) — verified in mock-LLM mode only: prompt assembly is byte-identical to
  today's no-role baseline, each role block is its own cache-marked segment.
- **Tested:** **not validated against a live model at all.** Battery A
  (content-invariance existence test — the same question, five arms, blinded
  claim/confidence extraction) has never been run. This is the single most
  expensive, highest-scope-decision item in the entire queue — it's a real cost
  (live API calls) and a real product decision (a whole new participant-facing mode),
  not a bug fix.
- **Missing:** Battery A (blocking), the `deconstructing`→`reevaluation` rename
  resolved before merge, onboarding copy updated to mention role selection, the
  `role=`/`worlds=`/`mode=` URL parse-site reconciliation with the Map branch.
- **Verdict: NOT ready to integrate.** Design and build are both done and
  self-consistent; the only thing standing between this and "ready" is Battery A —
  which is why this has been flagged repeatedly as the next real decision point,
  still awaiting your go-ahead to spend on it.

### 4. Guided Questions ("what do I ask") — LEAST BUILT OF THE THREE NAMED FEATURES

- **Designed:** Curriculum V1.0 — 100 questions, 20 sets, 4 roles, with a JSON
  contract. Superseded an earlier V0.2 role×world matrix shape.
- **Built:** **content only. Zero UI code exists anywhere in `cic-poc`** — confirmed
  by direct search of both frontend and backend for "guided," "starter,"
  "curriculum," "question set" — no matches.
- **Tested:** **not validated against a live model at all**, and the curriculum's own
  text says so plainly: the only cells ever tested belong to a superseded per-world
  predecessor, not these hundred generic-role strings. "No question here has faced a
  live model."
- **Missing:** Mark's two content decisions + one count-drift fix (cheap), then live
  validation of the actual current content, then the UI build itself (Increment 3,
  which depends on role selection existing first — see #3 above).
- **Verdict: NOT ready — furthest from integration of the three named features.**
  Content is genuinely done and reviewable now, but there is no code to integrate yet,
  and the content that exists has never been tested against a real model. Two real
  gates stand between this and readiness: your content review, then a live-validation
  pass — before any UI work is even worth starting.

### 5. Front-End Graphics thread — NOT YET STARTED

- Launched today (2026-07-17). Its own decision log has only the launch header — zero
  dated entries, zero output. Nothing to evaluate yet.

### 6. Anachronism bridge — CORRECTED: further along than first characterized

A closer read of `CiC_Facilitator_Upgrade_Decision_Log.md` shows this is materially
more ready than "too early to assess":

- **Designed + built:** `app/graph/modern_term_bridge.py` (`classify_modern_term` +
  `stream_modern_term_bridge`), already wired into `main.py`'s streaming endpoint
  alongside the frame-breaker and relational-safety intercepts (confirmed directly
  during this session's transcript-logging fix work).
- **Refactored today (2026-07-17) at Mark's own correction** — originally built
  needing a per-world authored overlay (disposition + reframe per world), which made
  Facilitator behavior world-specific; Mark ruled this should be identical no matter
  what world is seated, since it's a Facilitator feature, not a world one. Rebuilt so
  disposition is **derived, not authored** — a term's `origin_year` vs. the seated
  world's own end year (parsed from the manifest), not per-world files. The per-world
  overlay architecture was deleted entirely.
- **Tested — re-tested live against a real model (Chloe), and the refactor caught a
  real design error:** the old hand-authored version had wrongly marked the rapture
  case `true-silence`; the world-agnostic version let Chloe answer and surfaced
  genuine eschatological material she actually has, disclaiming a timeline honestly.
  This validates the design on its actual merits, not just its architecture.
- **Missing:** nothing per-world — that's the entire point of the refactor. Only the
  shared modern-term dictionary needs to keep growing as new terms come up.
- **Verdict: merge-gated only, same as the World Map** — the standing "never
  before/during Prototype 1" rule is the only thing between this and integration.
  **No dependency on any other feature in this document.**

### 7. Sensed closing sequence (Facilitator Upgrade Feature 2) — world-agnostic by design

- Closing behavior (sense → anything else → offer → show → close) was built
  world-agnostic from the start — no per-world refactor was needed the way the bridge
  needed one. Resource *content* is per-world data with a general-fallback pack, so an
  under-resourced world still gets the full sequence.
- **Verdict: same merge-gate as above** — no cross-feature dependency found.

### 8. Further back in the queue

- **Hosted Tour** — ~~Chloe demo built and self-verified (2026-07-16), but the
  *repeatable builder machine* (TR-4 through TR-9) that would let it scale to other
  worlds is still in progress; per-world manifests for Syriac/Desert/Bethlehem Circle
  not yet built.~~ **DEFERRED TO PHASE 2 — not part of the current build cycle
  (2026-07-22).** Mark decided Hosted Tour is a second-tier (Phase 2+) feature, not
  something this launch builds, and directed that all Tour-related content be taken out
  of the current build cycle across documents, UX, and code planning. Status above kept
  as the record for when Phase 2 takes this up; it's no longer part of "the queue" this
  document is ranking.
- **Question-First Entry** — design note exists, no build started.

---

## The pattern across all four evaluated features

Every one of them shows the same shape: **design work is consistently ahead of
validation, and validation is consistently ahead of integration.** The World
Orientation Map is the outlier — and the reason is that it's the only one where
someone actually built and verified the integration code, not just the design. That's
the concrete lesson for sequencing: a feature earns "ready" status by having a tested,
working branch, not by having a complete spec. Representative Modes and Guided
Questions both have excellent specs and neither has cleared that same bar yet.

**Superseded by the dependency-ordered plan below** — the single-next-action framing
was correct as far as it went, but understated how much of the queue has *no*
dependency on Battery A at all and could proceed in parallel.

---

## Dependency-ordered integration plan

Distinguishing **hard technical dependencies** (X cannot work without Y) from **soft
sequencing choices** (the strategy doc's own recommended order, which is swappable)
changes the picture: several features have no dependency on each other at all, and
the real critical path is shorter than "do everything in queue order" suggests.

### Tier 0 — independent, no cross-feature dependency, mergeable in any order

These four block nothing and are blocked by nothing among the features in this
document. Each only needs its own gate cleared, and all four gates are cheap/already
clear:

1. **Anachronism bridge** — merge-gated only by the standing P1-timing rule. Already
   re-tested live, world-agnostic, needs nothing further.
2. **Sensed closing sequence** — same: merge-gated only, no cross-feature dependency.
3. **Governance V3.7 cherry-pick** (drift-monitor fix) — needs only Mark's authority
   ruling on Section 10; the code has real test coverage already (8/8, 4/4, 3/3).
4. **World Orientation Map** — needs only the Tier A/B scope decision + the
   WID-mapping fix; technically independent of role selection, Guided Questions, or
   anything else.

**These four could merge together, right now, in whatever order is convenient**,
whenever the P1-timing window allows it. Nothing downstream is waiting on them.

### Tier 1 — the real sequential chain (the actual critical path)

This is the one genuine dependency chain in the whole queue:

```
Front-End Graphics mockups ──┐
                              ├─→ Increment 1 complete ──┐
(citation UI already done) ──┘                           │
                                                          ├─→ Increment 2 / Representative
Battery A (independent, ─────────────────────────────────┘   Modes merge ──┐
  run anytime, no upstream                                                 │
  dependency at all) ──────────────────────────────────────────────────────┘
  + reevaluation rename resolved                                           │
                                                                            ▼
Guided Questions content: Mark's 2 decisions ──┐              Increment 3 / Guided
  + count-drift fix + live-model validation ───┴─────────────→ Questions UI build
  (independent, run anytime, no upstream dependency)
```

**Why Increment 2 needs Increment 1 first:** sequencing choice, not a hard block — the
strategy doc's own reasoning is that the role selector shouldn't land on a screen
that's not yet in clutter-budget compliance. Technically, Battery A could pass and the
role-selection code could be ready before Increment 1 finishes; the *merge* just waits
so the entry screen changes in the right order rather than twice.

**Why Increment 3 needs Increment 2 first:** this one is a hard technical dependency —
role-served question walks cannot serve the right set without a role actually being
selected. Guided Questions' own content-validation work, though, has **zero
dependency on role selection** and should happen in parallel, not after.

**Battery A itself has no upstream dependency at all** — it doesn't need Increment 1,
the Graphics mockups, or anything else to run. It's parallel-startable today, the same
as the Tier 0 items above.

### Tier 2 — depends on Tier 1 landing, or deliberately sequenced after it

- ~~**Hosted Tour's `cic-poc` integration (TR-14)** — the feature-queue's own ordering
  sits this behind "the front-end IA pass" (Increment 1), most plausibly because a
  tour invitation card competes for the same contextual-card slot Increment 1's
  clutter budget establishes. The **builder machine (TR-4 through TR-9)** has no such
  dependency and can be built now, in parallel with everything above — only the final
  app-wiring step waits.~~ **DEFERRED TO PHASE 2 (2026-07-22) — see §8 above; Hosted
  Tour is no longer part of this integration queue at all, not just sequenced behind
  Increment 1.**
- **Question-First Entry** — sequenced after Tours by the original queue choice, and
  conceptually leans on the Map's world-data model (Tier 1 seed data already exists as
  World Coverage Cards) — but the Map itself is Tier 0 and doesn't block this from
  starting; it's a soft "makes more sense after" ordering, not a hard gate.

### The actual answer: what's the right order

1. **Merge the four Tier 0 items whenever the P1-timing window opens** — no reason to
   wait on anything else; they're independent and already cleared.
2. **Run Battery A now** — it has zero upstream dependency and is the longest-lead,
   highest-stakes item in the real critical path. Starting it late is the single
   biggest way to make Tier 1 take longer than it needs to.
3. **In parallel with Battery A:** Front-End Graphics produces its first mockups →
   Increment 1 finishes (table-bar consolidation; citations already done) — and,
   separately, Guided Questions' content review + live-validation, which has no
   dependency on either of those.
4. **Once Battery A passes + Increment 1 is done:** Increment 2 (role selection)
   merges.
5. **Once Increment 2 lands + Guided Questions content is validated:** Increment 3
   (the actual UI build) — this is the only step that's genuinely waiting on two
   upstream tracks converging.
6. ~~**Hosted Tour's app-wiring and**~~ **Question-First Entry** follow at their own
   pace, gated more by their own remaining build work (nothing yet) than by anything
   above. **Hosted Tour removed — DEFERRED TO PHASE 2 (2026-07-22); see §8 above.**

---

*Compiled 2026-07-17 by the System Hub thread. Sources: `CiC_World_Orientation_Map_Decision_Log.md`,
`CiC_FrontEnd_Graphics_Decision_Log.md`, `CiC_Guided_Questions_Curriculum_V1_0.md`,
`CiC_FrontEnd_Integration_Strategy_V0_1_DRAFT.md` §6, `CiC_Representative_Modes_Status_2026-07-17.md`,
and a direct code search of `cic-poc/` for guided-questions UI wiring (none found).*
