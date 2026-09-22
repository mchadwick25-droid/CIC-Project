# Voice Rebuild thread → System Hub — Update and go-live handover, 2026-08-10

**What this is:** the trackable-facts summary from the Voice Rebuild thread covering
2026-08-08 → 2026-08-10, for System Hub to fold into the Task Board, Gantt and
Dashboard. Full reasoning lives in
`Ministry/Operations/Audits/CiC_VoiceRebuild_Blueprint_2026-08-08/` and in the commit
messages on `claude/cic-voice-rebuild-handoff-fjwrt4`; this is what needs tracking.

**One decision is explicitly handed to System Hub to time** — branch protection on
`main`, §8. Mark's instruction, 2026-08-10: System Hub makes the call on when.

---

## ⚠ STATUS ADDENDUM — added after this document was written. Read before §1.

**Two things below are now out of date, and one of them inverts.** This document was
written at ~11:30 on 2026-08-10; the merge happened at 11:38 and the table workstream's
checklist reached this thread afterwards. Corrections, in the order they matter:

1. **§1 is now FALSE where it says `main` does not have this work.** The branch was
   merged to `main` at Mark's instruction — commit **`c6fb7e9f`** — and deployed. §9's
   fourth blocker ("merge the branch to `main` and deploy") is **DONE**. Everything §1
   says about the *content* of the branch remains accurate; only its location changed.

2. **The Haiku switch was reverted the same day — `main` is back on `claude-sonnet-5`**
   (commit `21e6842c`). This is a **sequencing** fix, not a reversal of the cost
   decision, and it is the single most important thing on this page for anyone acting
   on §4, §5 or §6. **There is only one model setting and it governs interview AND table
   alike** — `render.yaml` is Blueprint-managed — so this thread's Haiku switch was also
   the table's. The table workstream measured a **Haiku-only** public-transcript
   isolation breach (up to 21% of table turns; zero on Sonnet) whose repair is in PR #10
   and **not** in `main`. Every Haiku measurement in §4–§6 stands; what changed is that
   the flip must land **last and alone**, after PR #10 is merged and `main` is verified
   on Sonnet.

3. **This document is no longer the whole picture.** The order all three threads follow
   is `Ministry/Technology/Table/GO_LIVE_CHECKLIST_2026-08-10.md` — which as of writing
   exists **only on `claude/fable-table-cost-analysis-ynunno`**, not on `main`. Getting
   it onto `main` is the cheapest unblock available. Both 2026-08-10 decisions, with
   reasoning, are the final entry in `CiC_System_Hub_Decision_Log.md`.

4. **One defect closed after §10 was written**, and it is the first thing §10's
   never-run-in-a-browser gap actually produced: `cic-poc/frontend/src/index.css` — the
   whole two-tier citation stylesheet — was imported by nothing, so Vite never bundled
   it and a *consulted* source rendered identically to a *drawn-on* one. Fixed in
   `a1fd87ac`. §10's other two untested paths are unchanged and still open.

---

## 1. The headline, because everything else depends on it

**`main` does not have this work. The live site does not have this work.**

- `origin/main` still declares `LLM_MODEL: claude-sonnet-5`. Render deploys `main`.
  The Haiku switch is on the branch only.
- The branch `claude/cic-voice-rebuild-handoff-fjwrt4` is **21 commits / 31 files ahead
  of `main`** (+18,422 / −231).
- Everything in §4–§6 below was measured against that branch, not against anything a
  participant can reach today.

Nothing here is a claim about the live system. It is a claim about what is ready to
become the live system.

## 2. What already reached `main` — PR #9, merged 2026-08-09

"Voice Rebuild — six Representatives live at a tenth-grade reading level, plus the name
bridge." Six worlds re-voiced against the 1A bar (CEFR B2 / FK 8–10, anchor BBC
News/NatGeo), with the constraint that 1B convictions/fidelity is never traded for
readability. Plus the figure bridge: 53 named historical figures now resolve to a
participant-facing panel.

This is the only Voice Rebuild work currently deployable.

## 3. What is on the branch and not deployed

| item | what it does | state |
|---|---|---|
| Repository generalization | Level-3 record view for **all six** worlds, was 1 of 6; 688 records browsable, was 99 | done, CI-enforced (`repository-views-current`) |
| Papnoute glossary fix | plain-side gloss tier — Desert was firing 0/8 glosses | done |
| Two-tier citations | citation panel now distinguishes *drawn on* from *consulted* instead of discarding half the judgement | done |
| Bounded ceiling retry | the length ceiling now **checks whether the retry complied** and retries once more; previously it regenerated once and accepted the result unchecked | done |
| Haiku switch | `LLM_MODEL: claude-haiku-4-5-20251001` in `render.yaml`, `config.py`, `.env.example` | on branch |
| Supabase vars declared | `SUPABASE_URL` / `SUPABASE_SERVICE_KEY` as `sync: false`; `PILOT_LOGGING_ENABLED: true` | declared, **values unset** |

## 4. Haiku fleet certification — 3 of 6 PASS, and the failures are not what was expected

Full six-world battery, three runs each (Sonnet-certified baseline → plain Haiku →
Haiku with the enforced ceiling). Artifacts committed under
`Ministry/Technology/Pass2/batteries/*_2026-08-10-haiku-enforced.json`.

| world | Sonnet | Haiku | **enforced** | mean/ceiling |
|---|---|---|---|---|
| pahc (Chloe) | PASS | PASS | **PASS** | 106.0 / 150 |
| ijc (Marius) | PASS | FAIL | **PASS** | 108.5 / 150 |
| syr (Yausep) | PASS | PASS | **PASS** | 142.0 / 165 |
| alx (Theon) | PASS | FAIL | FAIL | 120.5 / 160 |
| des (Papnoute) | PASS | FAIL | FAIL | 57.5 / 70 |
| hal (Albina) | FAIL | FAIL | FAIL | 143.0 / 160 |

**Enforcement did its job.** The check that was failing — mean against the world's own
ceiling — now passes on all six; it passed on three under plain Haiku. Retry compliance
went from 14–100% to 86–100%. Over-ceiling turns fell from as bad as 6/8 to 0–1/8.

**The three remaining failures, stated precisely:**
- **alx** — one readability breach, turn 3, FK 8.48. That is *inside* the 8–10 band the
  design targets; the hard edge is rejecting a turn that may well be correct. Needs a
  ruling, not a fix.
- **des** — a 1.3-word regression against its own Sonnet baseline (57.5 vs 56.2), plus
  one fabrication signal in 26 screened turns.
- **hal** — a 2.5-word regression (143.0 vs 140.5), plus one fabrication signal.
  **Albina failed fabrication on Sonnet too** — that half is pre-existing and is not a
  cost of the Haiku switch.

**A correction System Hub should carry, because the raw scorecard misleads.** The
scorecards report citations firing on 8/8 turns in every enforced run, up from 1/8–4/8.
That is almost entirely the two-tier change surfacing *consulted* sources. Split by the
`grounded` flag, **drawn-on citations are still below Sonnet on four of six** (Theon
6/8 → 2/8 is the worst). Haiku costs citation grounding. That has not been recovered.

**One instrumentation gap, named rather than glossed:** `length_ceiling_logging` records
only the *final* retry, not the attempt count, so the marginal cost of the second retry
attempt cannot be recovered from the committed artifacts. 42 of 48 turns retried at
least once (Sonnet-v2: 36 of 48), so most of the regeneration load is not new — but the
increment is unmeasured. One extra field closes it, and it should be closed before any
cost claim leans on it.

## 5. The `native_measure` question is closed, and the answer reverses the plan

The plan of record was to re-derive each world's `native_measure` for Haiku. The
enforced records log `first_draft_words`, so Haiku's native measure is now directly
measurable — what it writes *before* any correction:

| world | ceiling | Haiku first-draft mean/median | ratio |
|---|---|---|---|
| des | 70 | 167 / 157 | 2.4× |
| pahc | 150 | 191 / 225 | 1.3× |
| ijc | 150 | 219 / 268 | 1.5× |
| syr | 165 | 230 / 214 | 1.4× |
| alx | 160 | 264 / 307 | 1.7× |
| hal | 160 | 295 / 288 | 1.8× |

Haiku writes 167–295 words in **every** world. It does not have a per-world measure to
re-derive — it has one length, and it is long. Re-deriving to fit it would put Papnoute
at 167 words instead of 55, which is not recalibration, it is deleting the voice.

**Decision recorded: do not re-derive.** The Sonnet-derived ceilings are correct; the
enforcement is what makes them bind. This is the opposite of what the data was gathered
to support, and it is the reason the enforced re-run was worth its cost.

## 6. Cost — the numbers, with two corrections already applied

Haiku at $1/$5 per MTok has **no introductory pricing to expire**, unlike Sonnet-5,
whose intro rate ends 31 August 2026.

| | Aug (Sonnet intro) | Sep (Sonnet standard) | **Haiku, now and Sep** |
|---|---|---|---|
| solo / turn | $0.0486 | $0.0603 | **$0.0369** |
| table / turn | $0.1270 | $0.1585 | **$0.0956** |

**Two corrections System Hub should not re-inherit:**
1. Every "start" figure in earlier reporting ($0.0603 solo / $0.1585 table) was priced
   at **standard** rates — that is September's price, not what August is billing. The
   saving against the **actual current bill** is **−24% solo / −25% table**, not −39/40%.
   The smaller number is the honest one to plan against.
2. The Phase 1 claim that "today's table is already over the line" was a fast-pacing
   sensitivity bound presented too strongly. At the reflective pacing the 1h cache TTL
   was adopted for (~6 turns/hr), the same table is ~$1.05/hour. Corrected in
   `CiC_MultiRep_Phase1_Cost_Analysis_2026-08-09.md`.

Multi-Representative Phase 1 verdict stands: the table survives the cost test at
~$0.085/turn (S2), against Mark's $5/hour line. Phase 2 (the selective-speaking design
question) is not started and is gated on Phase 1 acceptance.

## 7. Participant Readiness Review — 14 of 15 findings now closed

Re-verified at source, 2026-08-10, against
`Ministry/Operations/Audits/CiC_FullSystem_Review_2026-08-05/04_Participant_Readiness_Review.md`.

**Closed:** P0-1 (acute-distress redirect now present in the A1, A2 and harmful-dynamic
templates, satisfying V3.6 §12) · P0-2 (`privacy.html` exists, linked from six site pages
plus the onboarding screen) · P0-3a (whats-next Representative Modes copy rewritten to
match the 2026-08-02 stop) · P0-3b (persona captured for feedback correlation without
touching `participant_role`) · P1-1 (Imperial-Juridical guided starters) · P1-2 (`why`
and `citations` rendered) · P1-3 (six per-world further-reading packs) · P1-4
(`anything_else` now streams) · P1-5 (`TRAY_MAX = 3`) · **P1-6 (repository apparatus, all
six worlds — closed by this thread, 2026-08-09)** · P1-7 (Atlas list view) · P1-8
(direct-address turns exempt from `must_continue`) · P1-9 (copy-transcript + feedback
link) · P1-10 (citations to the non-existent live-test document corrected) · P1-11
(Atlas legend moved above the fold).

**Open: P1-12** — the answer bank has no data directory, so every lookup misses. Cost
item, not a participant gate. Its own analysis caps it at ~5.2% of traffic (SH-11).

## 8. Branch protection on `main` — handed to System Hub to time

**Context.** The `CiC Integrity Audit <audit@cic.local>` identity has 39 commits on
`main`, first 2026-07-03, **last 2026-08-07** — three days quiet as of this update, but
never identified and never stopped. It has already caused one real multi-file data-loss
incident (resetting `atlas-v3.html` mid-edit from another thread) and once cited a commit
hash as justification for a revert that, checked directly, did not support the claim.

**Why the timing question is real.** Today the blast radius is a working tree. After
deploy it is what a participant meets — Render serves `main`, with no review, no
attribution, and nothing distinguishing such a push from ours. Supabase configuration
(§9 item 2) adds real participant conversations to that radius.

**This thread's recommendation, not its decision:** set it **before the Render service
points at a `main` carrying the Haiku switch**. Not necessarily today.

**The exact configuration, if and when System Hub calls it:**
Settings → Rules → Rulesets → New branch ruleset. Name `Protect main`; enforcement
**Active** (not "Evaluate" — that only logs); target **Include default branch**; rules:
Restrict deletions, Block force pushes, Require a pull request before merging with
**Required approvals: 0**.

- Zero approvals is deliberate — it forces every change through a PR without requiring a
  second human. Hotfix path stays ~30 seconds, and matches how PR #9 already worked.
- **Leave "Require status checks" off initially.** CI has three jobs (`validate-census`,
  `repository-views-current`, `frontend-typecheck`). Make them required only after a week
  of watching them be reliable, or a flaky job locks `main`.
- **The bypass list must be empty.** Do **not** add "Repository admin." A git author name
  and email are just text in a commit and say nothing about the credential that pushed
  it; if the audit thread holds a token issued from Mark's account, an admin bypass entry
  lets it keep pushing while the settings page shows green.

**This cannot be done from a Claude Code session.** Attempted 2026-08-10 via the GitHub
rulesets API; the agent proxy returned `403 Write access to this GitHub API path is not
permitted through this proxy`, and the GitHub MCP server exposes no branch-protection
tool. Repository settings are a human action. Verification afterward *can* be automated —
attempt a direct push to `main` and confirm rejection.

**This closes option (2) of the Task Board's DO NOW entry. It does not close option (1)
— the thread is still unidentified.**

## 9. The go-live gate — four blockers

1. **Anthropic spending limit** (Mark's account, before Sept 1). Unchanged, still the
   only item nothing can route around.
2. **Supabase values in the Render dashboard.** Declared `sync: false`, both unset.
   Until set, `OnboardingScreen.tsx` tells every participant their conversation is
   "saved and cataloged … reviewed by the project team" and the only storage is
   ephemeral container JSONL, wiped on every redeploy. The app currently makes a promise
   it does not keep.
3. **Branch protection** — §8, System Hub's call.
4. **Merge the branch to `main` and deploy.** Nothing certified this week is live.

## 10. What has never been tested — the real gap, stated plainly

Every number in §4–§5 came from the checkpoint harness, which installs deterministic
hash-based embedding stubs and a token-overlap cross-encoder stand-in. That is correct
for baseline comparability and it means three things have **never** run in the deployed
path:

1. **The bounded ceiling retry** (commit `119543c6`) against real traffic.
2. **Retrieval against the real `all-MiniLM-L6-v2` indices on Haiku.** Only *generation*
   was re-certified on the smaller model. Retrieval quality was not measured at all.
3. **The frontend changes** — two-tier citations, plain-side glosses, the figure bridge —
   in a browser against a live backend. Not once.

A staging deploy exercising those three is the honest last gate, and it is not on any
list yet. Recommend System Hub add it as a Task Board item ahead of item 4 in §9.

## 11. Blueprint remainder — Phases 3 and 4

`CiC_VoiceRebuild_Stage3_Blueprint_2026-08-08.md`, Phases 0–2 complete.

**Phase 3 (Fleet closure):** S6.5 capsule fold-in · facilitator contrast-phrase
replacement at three sites plus the relational-safety probe category re-run ·
`HARD_CEILING_WORLDS` trigger-behaviour verification in Interview mode · governance
decision points **that need Mark** (over_settling stage-2 downgrade; confirmed_glosses
retirement decision) · fleet regression baseline. **The 2026-08-10 enforced six-world run
is the candidate for that baseline** — it is a full battery on all six rebuilt worlds in
one pass, and it is committed.

**Phase 4:** Framework Part Five and Part Eight updates · Decision Log entry closing the
thread.

## 12. Recommended Task Board changes

- **P1-6 → DONE** (repository apparatus, all six worlds, 2026-08-09).
- **Readiness P0-1/P0-2/P0-3, P1-1..P1-5, P1-7..P1-11 → DONE**; **P1-12 remains open**.
- **New item:** staging deploy exercising retry + real-index retrieval + frontend, ahead
  of the go-live merge (§10).
- **New item:** add an attempt-count field to `length_ceiling_logging` before any cost
  claim uses regeneration numbers (§4).
- **DO NOW branch-protection entry:** option (2) is fully specified and costed here;
  timing is System Hub's, option (1) still open.
- **SH-10** (keep testing real costs) — feed §6's corrected figures in; the two
  corrections matter more than the headline.
- **Watch item, not a task:** Haiku's drawn-on citation rate is below Sonnet on four of
  six worlds and did not recover under enforcement. If citation grounding is judged
  load-bearing for the Academic persona, reverting `LLM_MODEL` to `claude-sonnet-5` is
  one line and nothing else in the app is model-specific.

---

*From the Voice Rebuild thread, 2026-08-10. Every figure above is from a committed
artifact or a file read at source on that date; where a claim could not be verified —
the second-retry cost (§4), the audit thread's current state (§8) — it is labelled as
unmeasured rather than estimated.*
