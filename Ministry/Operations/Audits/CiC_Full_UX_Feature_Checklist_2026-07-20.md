# CiC Full User-Experience Feature Checklist — 2026-07-20

**Purpose:** every feature named in `CiC_Full_UX_Design_V1_0.md` (the canonical, 662-line
"whole journey drawn as one thing" spec), walked in actual journey order, each tagged with
exactly one status: **Implemented**, **Ready for implementation**, **Still needs testing**,
**Still needs design work**, or **No record**. Built for Mark to test the running app one
feature at a time, in order. Grounded in three sources, all cross-checked against each
other and against direct code inspection where they disagreed: `CiC_Full_UX_Design_V1_0.md`,
`CiC_UX_Implementation_Status_2026-07-19.md` (this session's own live testing), and
`CiC_Product_Status_Report_2026-07-19.md` (an independent code-inspection pass run earlier
today). An interactive version of this same list is published as a Claude Artifact for the
live testing session; this file is the permanent record.

**Totals: 89 features — 22 Implemented · 43 Ready for implementation · 12 Still needs
testing · 7 Still needs design work · 5 No record.** Read plainly: nearly half of the whole
journey is fully designed and approved but has zero code yet — Increment 1 is the single
biggest unlock (§10 below), not a missing decision.

---

## 1. Entry — the three start options (S0 Threshold, design doc §5.1)

| Feature | Status | Why |
|---|---|---|
| Hero + three co-equal doors (resting screen) | Ready for implementation | Approved V1.0 final; zero code — app currently bypasses straight to the world picker |
| Door 1 — "Start with your question" | Ready for implementation | Leads to S3; the door itself has no code yet |
| Door 2 — "Build your own table" | Ready for implementation | Leads to S1/S2; the door itself has no code yet |
| Door 3 — "Guided onboarding" | Ready for implementation | Leads to G.1–G.3; the door itself has no code yet |
| Quiet chrome: "Ask the Facilitator" pre-threshold overlay | Ready for implementation | Designed, zero code |
| Quiet chrome: About / Features / FAQ menu overlay | Ready for implementation | Designed, zero code |
| Current production entry (app skips straight to world picker) | Implemented | This is what actually runs today — "Bypass-shaped," per the design doc's own Alpha/Phase note |

## 2. The four starting-point choices (role selector, S2 §2.4 / G.1)

| Feature | Status | Why |
|---|---|---|
| Regular visitor | Still needs testing | Built on `claude/representative-modes-exploration`, mock-LLM verified only |
| Pastor or teacher | Still needs testing | Same branch, same gap |
| Academic or scholar | Still needs testing | Same branch, same gap |
| Reevaluation | Still needs testing | Copy decided 2026-07-16; code still uses internal id `deconstructing` — reconcile before merge |
| "No role" resting/skippable state | Still needs testing | Same branch, same gap |
| Role shapes response register (backend wiring) | Still needs testing | Real, wired code — but Battery A / RM-8 live-API validation has never run; standing rule blocks merge before/during P1 |

## 3. Path A — question-first entry (S3 + routing, §5.4 / Storyboard §R)

| Feature | Status | Why |
|---|---|---|
| S3 typed-question screen (input + 3 theme chips) | Ready for implementation | Approved 2026-07-18, zero code |
| S3 silent begin (no starter clicked) | Ready for implementation | Same |
| R.0 — question held (editable, visible through routing) | Ready for implementation | Same |
| R.1 — considering state (printed working-mark, honest retry) | Ready for implementation | Same |
| R.2a — the proposal card | Ready for implementation | Same |
| R.2b — clarify-once (never a second question) | Ready for implementation | Same |
| R.2c — honest null (nearest-true-thing + map pointer) | Ready for implementation | Same |

## 4. Path B — build your own table (S1 Map + S2 Setup)

| Feature | Status | Why |
|---|---|---|
| World Map — standalone (public website Atlas page) | Implemented | Live, real, interactive — verified today, zero JS errors |
| World Map — in-app orientation + handoff (Tier A) | Ready for implementation | Built and verified live on `claude/world-map-merge-into-main`; held back only by the no-merge-before-pilot rule, not an open design question |
| World Map primary-vs-secondary selector (Tier B) | Still needs design work | Open scope decision named in design doc §10.1 — gates how/whether Tier A even merges as scoped |
| Phone era-accordion | Ready for implementation | Design settled, owed only the map thread's own confirmation pass; zero code |
| S2 setup — resting (tradition picker + tray + Begin) | Implemented | Live in the running app today |
| S2 — one world seated (Deep Interview framing) | Implemented | Live today |
| S2 — emergent "Compare Worlds" framing (replaces toggle) | Ready for implementation | Part of Increment 1, not built — the toggle below is what's live instead |
| S2 — current Single/Multiple toggle (production today) | Implemented | What's actually live right now; slated for retirement once Increment 1 lands |
| S2 world-click menu (Description / Tour / Choose for Table / Academic Documents) | Ready for implementation | Designed as honest visible placeholders; not confirmed built |
| S2 proposed-table card (question-first flow only) | Ready for implementation | Tied to Path A routing; zero code |
| S2 proposal null case | Ready for implementation | Same |

## 5. Path C — guided onboarding (G.1–G.3)

| Feature | Status | Why |
|---|---|---|
| G.1 — where you're starting from | Ready for implementation | Approved by Mark 2026-07-18; zero code |
| G.2 — what draws you | Ready for implementation | Same |
| G.3 — the prepared table | Ready for implementation | Same |

## 6. The Table (S4) — the core conversation

| Feature | Status | Why |
|---|---|---|
| Living Table composed scene | Ready for implementation | Its own increment, sequenced after role/questions; icons locked, engineering not started |
| Nameplate-inversion speaker cue | Ready for implementation | Same increment |
| Reduced-motion state | Ready for implementation | Same increment |
| Long-form no-bubble transcript (Increment 1) | Ready for implementation | Spec implementation-ready; `TheTable.tsx` still uses the old bubble grammar |
| Table bar (seats + consolidated status) | Ready for implementation | Increment 1 |
| Current bubble-style transcript (production today) | Implemented | Confirmed via computed CSS today — this is what's live |
| Lexicon terms (Level 2 hover/tap, Level 3 full entry) | Implemented | Verified live today — highlighting, popover, click-through all working |
| Citations (✲ end-of-turn marker) | Implemented | Verified live today — opens correctly, real sourcing |
| Story inline highlighting | Ready for implementation | §5.7's grammar already covers stories; not yet applied in code — onboarding copy promises this and it isn't built |
| Quote sourcing | Ready for implementation | §5.7 names quotes as a fifth grammar application; no code exists yet |
| General/unsourced-claim disclosure | No record | No screen state or grammar addresses an ungrounded claim distinctly from a cited one — found in live testing, not in any design doc |
| Next-questions suggestion chips | Ready for implementation | Designed §4.1; not built |
| Tour invitation card | Ready for implementation | Same |
| Safety/close T3-slot suppression (UI behavior) | Ready for implementation | The card system this depends on isn't built yet (the underlying safety detection itself IS live — see below) |
| "Don't know what to ask?" + question sheet (Increment 3) | Ready for implementation | Content complete (Curriculum V1.0); zero UI; hard-gated on the role selector merging first |
| Input group (textarea / Send / End) | Implemented | Live today |
| Consolidated status line (session-cap / connection-loss) | Still needs testing | `session_cap.py` exists but needs real hosting to populate/exercise |
| Current RefreshWarningBanner (production today) | Implemented | Live today; retires into the table bar under Increment 1 |
| Anachronism bridge | Implemented | Verified live today, unprompted, in a real conversation — caught a modern-doctrine reading correctly |
| Representative frame-break robustness fix | Still needs testing | Fix committed (`77fc362`) after today's finding of a 4/4-reproducible break; not yet re-verified live, not yet pushed |
| Representative voice quality (in-character depth, honest citation) | Implemented | Verified live today: 19/20 real academic questions answered excellently across 4 worlds |
| Relational-safety / drift governance (15 signal types) | Still needs testing | Substantially wired, real detector functions; "not fully validated live" per direct code inspection |
| Frame-breaker classifier (fails open) | Implemented | Real, separate classifier call, confirmed in code |

## 7. Hosted Tour (S4-tour, T.1–T.6)

| Feature | Status | Why |
|---|---|---|
| In-app tour integration (threshold stop → beats → exit) | Ready for implementation | Blocked behind Increments 1 and 2, explicitly "never before/during P1" |
| Register strip / beat tracker / Exit chrome | Ready for implementation | Same |
| Honest-absence beat ("What We Cannot Show You") | Ready for implementation | Same |
| Standalone Chloe/Justin demo asset | Implemented | Real, richly produced, 960KB — but zero connection to `cic-poc` |

## 8. The Close (S5)

| Feature | Status | Why |
|---|---|---|
| Gracious close (Facilitator turn) | Ready for implementation | Backend logic restored today (was missing entirely); zero frontend UI renders it |
| "Anything else?" open pause | Ready for implementation | Same — backend-capable, no frontend |
| Reflection beat ("What stayed with you?") | Ready for implementation | Designed in to ship with the closing-sequence build; no frontend |
| Closing resources offer | Ready for implementation | Same |
| The door outward | Ready for implementation | Same |
| Current production close (bare "conversation has ended") | Implemented | This is literally what's live today |

## 9. Cross-cutting / infrastructure

| Feature | Status | Why |
|---|---|---|
| World: House-Church (Chloe) | Implemented | Live, deployed |
| World: Desert-Monasticism (Papnoute) | Implemented | Live, deployed |
| World: Syriac / Edessa–Nisibis (Mar Yausep) | Implemented | Live, deployed |
| World: Bethlehem Circle (Albina) | Implemented | Live, deployed |
| World: Alexandria Catechetical School (Theon) | Implemented | Fixed and verified live today — was completely absent before |
| World: Imperial-Juridical Christianity | Still needs design work | World-build actively underway (Step 0–Doc_09 + Step 10 phases in progress) |
| World: Donatism | Still needs design work | Planned in the Nine-World Portfolio; construction not started |
| World: Cappadocian | Still needs design work | Same |
| World: Latin Pastoral-Congregational | Still needs design work | Same |
| Accounts / sign-in (Supabase) | Still needs testing | Code-complete, smoke-tested; needs Mark's own account creation to go further |
| Per-tester session/API cap | Still needs testing | Code exists; unexercised until real hosting exists |
| Hosting — `cic-poc` app itself | Ready for implementation | Direct-API approach decided; not stood up |
| Hosting — public website | Implemented | Live, real domain |
| Referral system backend | Implemented | Real endpoints, Supabase-backed, one-hop enforcement built |
| Referral system frontend | Still needs testing | Wired but inert — API base URL empty; will work once deployment sets it, needs a real test then |
| World icons (5 SVGs) | Ready for implementation | Locked and approved; not wired into any UI component |
| Table world-count ceiling safeguard | Still needs design work | The 5-world cap is a stated policy, not an enforced code limit — no mechanism stops a 6th world being seated |
| Session data persistence (currently in-memory only) | Still needs design work | POC-only; lost on restart — a real durability decision hasn't been made |

## 10. Flagged — no record found anywhere

| Feature | Status | Why |
|---|---|---|
| Accessibility (screen reader / keyboard navigation) | No record | Not mentioned anywhere in the 662-line UX spec or any status document |
| Internationalization / non-English support | No record | Same |
| In-session feedback or bug-report mechanism | No record | Same |
| Terms of service / privacy policy screen | No record | Same |

---

## Document log

- **V1.0 (2026-07-20):** First edition. Built at Mark's request for a feature-by-feature
  testing walkthrough of the entire user experience, starting with the three start options
  and four user choices. Synthesizes `CiC_Full_UX_Design_V1_0.md`, this session's own
  `CiC_UX_Implementation_Status_2026-07-19.md`, and `CiC_Product_Status_Report_2026-07-19.md`.
