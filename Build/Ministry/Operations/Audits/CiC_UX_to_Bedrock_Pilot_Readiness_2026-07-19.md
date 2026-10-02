# UX-to-Bedrock-and-Pilot Readiness — 2026-07-19

**What this is:** the answer to one question — *what's left before real hosting and
Prototype Testing 1 (P1)?* (titled for Bedrock, which was the plan when this report was
first written — see the correction note just below) — with the UX/design side (now
complete) separated cleanly from the build/validate/merge side (where the real remaining
work is). Supersedes nothing; updates `CiC_Feature_Integration_Readiness_2026-07-17.md`
(still the fuller per-feature detail) against everything decided since, especially that
**the Front-End Graphics mockups that document named as Increment 1's missing piece now
exist and are approved.**

**The headline, stated plainly: UX design has zero open items. The gate from here to
hosting/pilot is entirely build → validate → merge, not design.**

> **CORRECTION (2026-07-19, later still):** everywhere below that says "re-engage
> Bedrock/AWS" is now stale — the System Hub thread's own log
> (`CiC_System_Hub_Decision_Log.md`, 2026-07-19) records that **Mark decided to skip
> Bedrock entirely and host directly on the Anthropic API instead**, alongside the
> website's own infrastructure. This report should have been checked against that log
> before being written/updated and wasn't — the same mistake this report's own V1.0
> correction note warned about. Fixed in place below rather than left to stand;
> flagged here so the correction itself isn't missed. Also newly true and not yet
> reflected below before this pass: **the pilot invitation pages already exist and are
> live** on the public website (`cic-website/pilot.html`, `pilot-thank-you.html`), and
> **the per-tester session/API cap mechanism already exists in code**
> (`cic-poc/backend/app/session_cap.py`) — both built by System Hub today, so "stand up
> hosting" is narrower work than this report originally implied.
>
> **SCOPE UPDATE (2026-07-19, later the same day):** separately, Mark decided P1 launches
> with the **full feature set**, not the minimum-viable scope §4/§5 originally
> recommended. Sections 1–3 below are unaffected (design is still fully complete either
> way) — §4 and §5 are revised accordingly, with the original minimum-viable framing kept
> underneath as the reasoning trail, not deleted, per this project's standing practice of
> not hiding a revision.
>
> **DEFERRED TO PHASE 2 — not part of the current build cycle (2026-07-22):** Mark
> decided Hosted Tour is a second-tier (Phase 2+) feature, not something this launch
> builds, and directed that all Tour-related content be taken out of the current build
> cycle across documents, UX, and code planning. **This removes Tour as a P1 dependency
> everywhere below that named it as one** — the Tier 2 Hosted Tour item in §2, decision
> item 4 and the Tour-builder-machine execution bullet in §3, the "Hosted Tour" bullet
> and Tier-2 sentence in §4, the Tour references in §4a's reasoning trail, and steps 3,
> 6, and 7 of §5 (including the "Run P1 once everything above is in" gate, which no
> longer needs Hosted Tour). Everything else in this report — Sections 1–3's
> design-completeness claims, and the rest of the full-feature-set decision
> (Representative Modes, Guided Questions, Question-First Entry, Guided Onboarding, the
> Living Table) — is unaffected. Left in place below as the reasoning trail for when
> Phase 2 takes Tour up, not deleted.

---

## 1. What "UX design is complete" actually means (as of today)

Every screen from the threshold to the door outward is designed and cited to a governing
record — nothing is undesigned, and as of this morning, nothing designed is unapproved:

- **`CiC_Full_UX_Design_V1_0.md`** (V1.0.3) — the whole journey, every stage, five-count
  verified on every screen, no open conflicts.
- **`CiC_Full_UX_Storyboard_V1_0.md`** — the two screens that were never designed anywhere
  (Guided onboarding, the Question-First routing UI) are now designed **and approved**
  (Mark, 2026-07-18/19).
- **The Living Table** — geometry finalized on both desktop and phone (scene-locked, one
  shared coordinate system, Mark-tuned exact values), long-form typography decided (no
  chat bubbles), reading surface decided (warm cream, no era variation), all five world
  icons built/locked, the icon full-family review passed. **A structural bug was caught
  and fixed on both platforms** (figures and the table line were in separately-eyeballed
  coordinate boxes) — the fix is recorded so it doesn't recur.
- **A content-integrity issue was caught and fixed**: early mockups carried invented
  first-person dialogue attributed to Representatives. All instances removed and replaced
  with explicitly-labeled placeholder text; a standing rule is now on record — no mockup
  may invent Representative speech, ever.
- **Increment 1's build handoff is current** (`CiC_Build_Handoff_Increment1_V1_0.md`,
  now V1.1) — file-by-file, implementation-ready, including the long-form transcript
  restyle.

**What this closes from the 2026-07-17 readiness assessment:** that document named
*"the Front-End Graphics thread hasn't produced any mockups yet"* as the specific reason
Increment 1 couldn't be called complete. **That reason no longer applies.** The mockups
exist, the five-count check has been run on every screen (not just citations), and the
Living Table's own increment is now fully specified rather than a placeholder.

---

## 2. The critical path to Bedrock + P1 (dependency-ordered, not queue-ordered)

This reuses the readiness assessment's own dependency analysis (`CiC_Feature_Integration_
Readiness_2026-07-17.md` §"Dependency-ordered integration plan") — the real chain is
shorter than "build everything in order" suggests, because most features don't actually
block each other.

### Tier 0 — independent, mergeable whenever the P1-timing window opens, blocked by nothing else

| Item | Status | What's left |
|---|---|---|
| Anachronism bridge | Built, live-tested | Merge-gated only (P1-timing rule) |
| Sensed closing sequence | Built, world-agnostic | Merge-gated only (P1-timing rule) |
| Governance V3.7 cherry-pick (drift-monitor fix) | Built, tested (8/8, 4/4, 3/3) | Mark's authority ruling on Section 10 |
| World Orientation Map | Built + real integration code on branch, verified live | Tier A/B scope decision; WID-mapping auto-gen; Homoian governance tension |

**These four could merge together right now**, whenever the P1 window opens. Nothing
downstream waits on them.

### Tier 1 — the one real sequential chain

```
Front-End Graphics mockups ✅ DONE (this session)
        │
        ▼
Increment 1 (table bar, long-form transcript, panels, toggle
retirement, tokens, favicon) — DESIGNED & SPECIFIED, NOT YET BUILT
        │
        ▼                                    Battery A (independent —
Increment 2 / Representative Modes  ◄─────── run anytime, zero upstream
merge (needs Battery A passed +               dependency, the highest-
Increment 1 done — rename already done)       stakes item in the chain)
        │
        ▼
Increment 3 / Guided Questions UI  ◄───────── Guided Questions content
(hard dependency: role-served                 validation (independent,
question walks need a role to exist)          run anytime)
```

- **Increment 1's design blocker is cleared** (see §1) — what's left is the actual build,
  which has an implementation-ready spec waiting (`CiC_Build_Handoff_Increment1_V1_0.md`
  V1.1).
- **Battery A has zero upstream dependency and can start today** — it's parallel-startable
  with everything else, and it's explicitly *"the single most expensive, highest-scope-
  decision item in the entire queue… still awaiting your go-ahead to spend on it"*
  (Readiness doc §3). This is the one item most worth not leaving until last.
- **Guided Questions' content review + live-validation also has zero dependency on
  anything above** and should run in parallel, not after — but the UI build itself
  (Increment 3) can't start until Increment 2 lands (a real technical dependency: a
  role-served question walk needs a role to exist).

### Tier 2 — sequenced after Tier 1, not blocked by it structurally

- **Hosted Tour's `cic-poc` integration (TR-14)** — soft-sequenced behind Increment 1
  (a tour invitation competes for the same contextual-card slot Increment 1 establishes).
  The builder machine (TR-4–TR-9: manifest template, eligibility checklist, asset
  pipeline, templated renderer) has no such dependency and can be built now, in parallel.
- **Question-First Entry** (now fully designed — storyboard §R) and **Guided Onboarding**
  (now fully designed — storyboard §G) — both zero code, both soft-sequenced after Tours
  in the original queue, but neither is a hard technical blocker on anything above.
- **The Living Table's own build increment** — assets are locked, geometry is finalized on
  both platforms; the actual `cic-poc` wiring (compose the scene, wire nameplate inversion
  to the `speaker` field) hasn't started. Sequenced after role/questions in the original
  plan; no hard dependency forces that order.

---

## 3. What's actually blocking Bedrock/pilot right now — and who acts on each

**Superseded (see the correction note at the top): the item below used to be "re-engage
Bedrock" — it's now "stand up direct-API hosting," per Mark's 2026-07-19 decision to skip
Bedrock entirely.** The underlying urgency is the same (this was the deliberate 2026-07-17
pause item, and its "~2026-07-19/20" target window is now), only the destination changed:
host `cic-poc` directly with `ANTHROPIC_API_KEY` on a Render/Fly.io-class platform
(not Cloudflare Pages — static-only), with an Anthropic Console spending limit as the
budget-control mechanism, instead of AWS/Bedrock. **Per-tester session capping for this
already exists in code** (`cic-poc/backend/app/session_cap.py`) — it needs populating/
configuring, not building from scratch.

**Decisions that are Mark's alone (not something I can complete for him):**
1. **Stand up direct-API hosting** (pick a host, deploy, set the Anthropic Console
   spending cap) — the deliberate pause's target window is today/tomorrow; the
   destination changed from Bedrock/AWS but the urgency and the window didn't.
2. **Battery A go-ahead** — a real cost (live API calls) and a real product decision (a
   whole new participant-facing mode), not a bug fix. Zero upstream dependency; can start
   the moment you say go.
3. **Guided Questions' two content decisions** (+ a cheap count-drift fix) — needed before
   live-validation can even start; independent of everything else.
4. **The Chloe Hosted-Tour voice read** — your read of the scripted tour content (the
   Q&A demonstration answer, the sermon-absence line, the singing-decline) is the standing
   gate before any public use of that demo.
5. **Section 10 governance ruling** (the drift-monitor cherry-pick) — code's ready and
   tested; needs your authority ruling to merge.
6. **Gantt IDs and priority order** for every `IC-`/`SB-`/`BR-`/`TR-`/`RM-` row handed to
   the Hub this session — per the Hub's own standing convention, these are yours to assign.

**Execution that's the build thread's, once the above clears:**
- Increment 1's actual code (spec is implementation-ready, V1.1).
- The Living Table's `cic-poc` wiring (assets + geometry are ready; no design blocker).
- The Tour builder machine (TR-4–TR-9), which can run in parallel with Increment 1.

**Cosmetic/content follow-ups, explicitly not on the critical path** (routed to their own
threads in the storyboard hand-off, not touched here since they're outside this thread's
scope and don't block anything above): the stale "four live worlds" references on the map
(World-Map thread), Theon's tour-eligibility assessment via the TR-5 checklist
(Hosted-Tour thread — this needs that thread's own methodology run, not a text fix),
the tour stop-numbering reconciliation (Hosted-Tour thread), and the Chloe "house church"
naming-voice gap (world/facilitator threads).

---

## 4. What P1 needs — the full feature set (Mark's call, 2026-07-19)

**Mark's decision: P1 launches with everything, not just the core encounter.** That
means every feature named "genuinely optional" in the original §4 (kept below as §4a,
superseded) is now **in scope for P1 itself**, not deferred to a later phase. Concretely,
P1 now needs:

- Direct-API hosting stood up (#101/401, revised — Bedrock dropped 2026-07-19; the
  pilot-invitation website pages and the per-tester session-cap mechanism already exist,
  see the correction note at the top — this item is now narrower than it reads below).
- Increment 1 built and merged (brand tokens, table bar, long-form transcript, Level-3
  panels, toggle retirement, favicon) — spec needs a same-day refresh first (see §1's
  note on the greeting-screen work from today not yet being in the handoff doc).
- The Tier 0 four items merged (anachronism bridge, closing sequence, governance
  cherry-pick, World Map).
- *(Not gated on anything here, already done: Alexandria/Theon is now installed as a
  fifth live world — carries its own disclosed caveats, no live participant-calibration
  yet, Doc_09 stories not yet chunked, running on lexicon retrieval only for now.)*
- **Battery A run and passed**, then **Increment 2 (Representative Modes / role
  selection) built and merged.**
- **Guided Questions' content decisions made and validated**, then **Increment 3 (the
  question-sheet UI) built and merged** — hard-dependent on Increment 2 existing first.
- ~~**Hosted Tour** — both the builder machine (TR-4–TR-9) and the `cic-poc` integration
  (TR-14), plus Mark's own voice read of the scripted tour content.~~ **DEFERRED TO
  PHASE 2 (2026-07-22) — not a P1 requirement; see banner at top.**
- **Question-First Entry** and **Guided Onboarding** — both fully designed (storyboard
  §R/§G) but **zero code exists for either yet** — these need an actual build pass now,
  not just a design.
- **The Living Table's own live wiring** — composing the real scene in `cic-poc` and
  wiring nameplate inversion to the `speaker` field; assets and geometry are locked, but
  none of it is connected to the running app yet.

**What this changes about the critical path (§2):** Tier 1's sequential chain
(Increment 1 → Battery A/Increment 2 → Increment 3) is no longer optional depth — it's
now the literal gate on P1 starting at all, since Representative Modes and Guided
Questions UI are both in scope. **Battery A goes from "highest-leverage optional item"
to "the single most schedule-critical action in this entire plan"** — everything in
Tier 1 downstream of it, and P1 itself, waits on it passing. Tier 2 (Tours, Question-First
Entry, Guided Onboarding, Living Table wiring) is no longer soft-sequenced background
work either — all of it now has to actually get built before P1 can launch.

**Honest schedule consequence, worth saying plainly:** this is a materially longer path
than the minimum-viable version below. Nothing here is a design blocker — every one of
these has an approved spec or storyboard already — but "designed" and "built" are
different amounts of remaining work, and this decision means all of it happens before
P1 rather than after.

### 4a. (Superseded) The original minimum-viable framing — kept as the reasoning trail

P1 tests the core encounter, not every feature. The running app today is Bypass-shaped
(onboarding → picker → Table) — that shape is enough to pilot on its own, once dressed in
the approved brand and given the long-form/Living-Table treatment. Concretely:

**Needed for a credible P1 (under the minimum-viable framing):**
- Bedrock/AWS infrastructure sorted (the standing pause item).
- Increment 1 built and merged (brand tokens, table bar, long-form transcript, Level-3
  panels, toggle retirement, favicon).
- The Tier 0 four items merged (anachronism bridge, closing sequence, governance
  cherry-pick, and — if the Tier A/B scope call is made — the World Map).

**Called "genuinely optional for the first pilot" under that framing — now in scope per
the decision above:**
- Representative Modes (Battery A + merge).
- Guided Questions UI (Increment 3).
- Hosted Tour, Question-First Entry, Guided Onboarding, the Living Table's live wiring.

---

## 5. Recommended order of operations, starting today (updated for the full-feature-set decision)

1. **Stand up direct-API hosting (#101/401, revised)** — the deliberate pause's window
   is now; the destination is a Render/Fly.io-class host with `ANTHROPIC_API_KEY` and an
   Anthropic Console spending cap, not Bedrock. The pilot-invitation pages and the
   session-cap code already exist — this is deploy-and-configure, not build-from-scratch.
2. **Say go on Battery A today.** This is no longer just the highest-leverage optional
   item — it's the one thing every downstream step in this plan now waits on. Nothing
   else in Tier 1 or Tier 2 shortens the timeline as much as starting this immediately.
3. **In parallel, starting now:** refresh Increment 1's build spec with today's
   greeting-screen work, then hand it to the build thread; make the two Guided-Questions
   content calls; rule on Section 10 governance; do Mark's own voice read of the Hosted
   Tour script; start the Hosted Tour builder machine (TR-4–TR-9, no dependency); start
   Question-First Entry and Guided Onboarding's actual builds (design is done, code isn't).
4. **Once Battery A passes + Increment 1 lands:** Increment 2 (role selection) merges.
5. **Once Increment 2 lands + Guided Questions content is validated:** Increment 3 (the
   question-sheet UI) merges.
6. **Once Increment 1 lands:** the Hosted Tour's `cic-poc` integration (TR-14) and the
   Living Table's own live wiring both proceed — both were only soft-sequenced behind
   Increment 1, not blocked by anything else.
7. **Run P1 once everything above is in** — direct-API hosting, Increment 1, Tier 0,
   Increment 2, Increment 3, ~~Hosted Tour,~~ Question-First Entry, Guided Onboarding, and
   the Living Table's live wiring. **Hosted Tour removed from this gate — DEFERRED TO
   PHASE 2 (2026-07-22); see banner at top.** This is the real gate now, not Increment 1
   + Tier 0 alone.
8. **Merge discipline holds throughout:** nothing merges before or during P1 itself; all
   of the above lands in the pre-P1 window, once it opens.

---

## A correction found while compiling this report

While pulling this together, `CiC_Full_UX_Design_V1_0.md` and `CiC_Full_UX_Storyboard_
V1_0.md` were both found to still describe the `deconstructing → reevaluation` role-id
rename as open — it was actually resolved (executed in code, approved by Mark) on
2026-07-18, the same day the storyboard was written, per `CiC_Guided_Questions_Decision_
Log.md`'s own entry. Both documents corrected in place; this report reflects the true
current state (rename done; Battery A remains the real gate on Representative Modes).
Flagging this here because it's exactly the kind of drift a synthesis document like this
one can propagate if not checked against the actual per-feature logs.

## Document log

- **V1.0 (2026-07-19):** First edition. Synthesizes `CiC_Feature_Integration_Readiness_
  2026-07-17.md` (per-feature detail + dependency analysis, still authoritative for depth)
  against everything decided in the UX Design thread since — most importantly, that the
  Front-End Graphics mockups that document named as Increment 1's missing piece are now
  done and approved. Produced on Mark's request ("give me an update on the UX design [of]
  what is left to integrate into bedrock and pilot test the entire system").
- **V1.1 (2026-07-19, later the same day):** Scope update. Mark decided P1 launches with
  the full feature set, not the minimum-viable scope V1.0 recommended ("but with the full
  set of features not just what was originally planned"). §4 and §5 rewritten; the V1.0
  minimum-viable framing kept as §4a (superseded), not deleted. Battery A's status changes
  materially under this decision — from highest-leverage optional item to the single
  action every other step in the plan now depends on.
- **V1.2 (2026-07-19, later still):** Correction. V1.1 was written without checking
  `CiC_System_Hub_Decision_Log.md`, which already recorded (same day) that **Mark decided
  to drop Bedrock entirely for direct Anthropic API hosting**, and that System Hub had
  already built the pilot-invitation website pages and the per-tester session-cap code.
  Every actionable "re-engage Bedrock" line corrected in place to "stand up direct-API
  hosting." This is the same failure mode V1.0's own correction note warned about —
  carrying forward a claim without checking the log that actually owns it — and it
  happened again in this same document one revision later.
