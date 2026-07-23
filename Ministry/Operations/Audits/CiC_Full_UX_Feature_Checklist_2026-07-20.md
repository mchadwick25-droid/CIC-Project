# CiC Full Feature Checklist — 2026-07-20

**Purpose:** every feature and workstream across the whole project, split along two axes
Mark asked for on top of the original journey-ordered list:

1. **Track** — is this part of the **Program** (the conversation app + its immediate
   surfaces — the thing a participant actually experiences, testable one feature at a
   time), or is it **Business & Organizational Development** (Marketplace positioning,
   funding, entity formation, external messaging — real work, but strategy/formation
   work with no UI to click through)?
2. **Surface** (Program items only) — **Website** (the marketing site, `cic-website/`),
   **App** (the conversation program, `cic-poc/`), **Both** (exists on/bridges both), or
   **System** (backend/infrastructure with no discrete screen — hosting, accounts,
   governance detectors, data persistence).

Part 1 is the same 89 Program features as the first edition, now re-tagged by Surface.
Part 2 is new: the Business & Organizational Development track, split out because it
doesn't belong in a UX-testing walkthrough at all — it has its own different lifecycle
(drafted → decided → active), not implemented/tested/designed. **Part 2's status calls
are workstream-level, not file-verified** — a lighter pass than Part 1, which was
grounded in live testing and direct code inspection. Say the word if you want the same
file-by-file rigor run on Part 2.

**The lifecycle rule, going forward:** nothing in Part 1 gets a "50% done" or
"in-progress" tag — a feature is either not-yet-built (Ready for implementation / Still
needs testing / Still needs design work / No record) or it's **Implemented**, full stop.
The moment something is verified live — like Alexandria today — it flips straight to
Implemented, its "why" line is rewritten in past tense describing what happened and when,
and the **Document Log** at the bottom gets one dated line recording the graduation. The
thing's own construction record (a World-Build's Doc_00–Doc_09, an Increment's
build-handoff spec) is never deleted when it graduates — that stays the permanent record
of *how* it was built; this checklist stays the permanent record of *whether* it's live.

**Part 1 totals (updated 2026-07-20, after the epistemology-bridge fix and the
session-recovery/world-ceiling design pass): 89 features — 23 Implemented · 45 Ready
for implementation · 11 Still needs testing · 5 Still needs design work · 5 No
record.** By surface: 67 App · 5 Website · 9 Both · 8 System.

---

# Part 1 — The Program

## 1. Entry — the three start options (S0 Threshold, design doc §5.1)

| Feature | Status | Surface | Why |
|---|---|---|---|
| Hero + three co-equal doors (resting screen) | Ready for implementation | App | Approved V1.0 final; zero code — app currently bypasses straight to the world picker |
| Door 1 — "Start with your question" | Ready for implementation | App | Leads to S3; the door itself has no code yet |
| Door 2 — "Build your own table" | Ready for implementation | App | Leads to S1/S2; the door itself has no code yet |
| Door 3 — "Guided onboarding" | Ready for implementation | App | Leads to G.1–G.3; the door itself has no code yet |
| Quiet chrome: "Ask the Facilitator" pre-threshold overlay | Ready for implementation | App | Designed, zero code |
| Quiet chrome: About / Features / FAQ menu overlay | Ready for implementation | App | Designed, zero code |
| Current production entry (app skips straight to world picker) | Implemented | App | What actually runs today — "Bypass-shaped," per the design doc's own Alpha/Phase note |

## 2. The four starting-point choices (role selector, S2 §2.4 / G.1)

| Feature | Status | Surface | Why |
|---|---|---|---|
| Regular visitor | Still needs testing | App | Built on `claude/representative-modes-exploration`, mock-LLM verified only |
| Pastor or teacher | Still needs testing | App | Same branch, same gap |
| Academic or scholar | Still needs testing | App | Same branch, same gap |
| Reevaluation | Still needs testing | App | Copy decided 2026-07-16; code still uses internal id `deconstructing` — reconcile before merge |
| "No role" resting/skippable state | Still needs testing | App | Same branch, same gap |
| Role shapes response register (backend wiring) | Still needs testing | App | Real, wired code — but Battery A / RM-8 live-API validation has never run; standing rule blocks merge before/during P1 |

## 3. Path A — question-first entry (S3 + routing, §5.4 / Storyboard §R)

| Feature | Status | Surface | Why |
|---|---|---|---|
| S3 typed-question screen (input + 3 theme chips) | Ready for implementation | App | Approved 2026-07-18, zero code |
| S3 silent begin (no starter clicked) | Ready for implementation | App | Same |
| R.0 — question held (editable, visible through routing) | Ready for implementation | App | Same |
| R.1 — considering state (printed working-mark, honest retry) | Ready for implementation | App | Same |
| R.2a — the proposal card | Ready for implementation | App | Same |
| R.2b — clarify-once (never a second question) | Ready for implementation | App | Same |
| R.2c — honest null (nearest-true-thing + map pointer) | Ready for implementation | App | Same |

## 4. Path B — build your own table (S1 Map + S2 Setup)

| Feature | Status | Surface | Why |
|---|---|---|---|
| World Map — standalone (public website Atlas page) | Implemented | Website | Live, real, interactive — verified today, zero JS errors |
| World Map — in-app orientation + handoff (Tier A) | Ready for implementation | Both | Built and verified live on a branch, bridges the website's map concept into the app; held back only by the no-merge-before-pilot rule |
| World Map primary-vs-secondary selector (Tier B) | Still needs design work | Both | Open scope decision — gates how/whether Tier A even merges as scoped |
| Phone era-accordion | Ready for implementation | App | Design settled, owed only the map thread's own confirmation pass; zero code |
| S2 setup — resting (tradition picker + tray + Begin) | Implemented | App | Live in the running app today |
| S2 — one world seated (Deep Interview framing) | Implemented | App | Live today |
| S2 — emergent "Compare Worlds" framing (replaces toggle) | Ready for implementation | App | Part of Increment 1, not built — the toggle below is what's live instead |
| S2 — current Single/Multiple toggle (production today) | Implemented | App | What's actually live right now; slated for retirement once Increment 1 lands |
| S2 world-click menu (Description / Tour / Choose for Table / Academic Documents) | Ready for implementation | App | Designed as honest visible placeholders; not confirmed built |
| S2 proposed-table card (question-first flow only) | Ready for implementation | App | Tied to Path A routing; zero code |
| S2 proposal null case | Ready for implementation | App | Same |

## 5. Path C — guided onboarding (G.1–G.3)

| Feature | Status | Surface | Why |
|---|---|---|---|
| G.1 — where you're starting from | Ready for implementation | App | Approved by Mark 2026-07-18; zero code |
| G.2 — what draws you | Ready for implementation | App | Same |
| G.3 — the prepared table | Ready for implementation | App | Same |

## 6. The Table (S4) — the core conversation

| Feature | Status | Surface | Why |
|---|---|---|---|
| Living Table composed scene | Ready for implementation | App | Its own increment, sequenced after role/questions; icons locked, engineering not started |
| Nameplate-inversion speaker cue | Ready for implementation | App | Same increment |
| Reduced-motion state | Ready for implementation | App | Same increment |
| Long-form no-bubble transcript (Increment 1) | Ready for implementation | App | Spec implementation-ready; the transcript still uses the old bubble grammar |
| Table bar (seats + consolidated status) | Ready for implementation | App | Increment 1 |
| Current bubble-style transcript (production today) | Implemented | App | Confirmed via computed CSS today — this is what's live |
| Lexicon terms (Level 2 hover/tap, Level 3 full entry) | Implemented | App | Verified live today — highlighting, popover, click-through all working |
| Citations (✲ end-of-turn marker) | Implemented | App | Verified live today — opens correctly, real sourcing |
| Story inline highlighting | Ready for implementation | App | The grammar already covers stories; not yet applied in code — onboarding copy promises this and it isn't built |
| Quote sourcing | Ready for implementation | App | Named as a fifth grammar application; no code exists yet |
| General/unsourced-claim disclosure | No record | App | No screen state addresses an ungrounded claim distinctly from a cited one — found in live testing, not in any design doc |
| Next-questions suggestion chips | Ready for implementation | App | Designed; not built |
| Tour invitation card | Ready for implementation | App | Same |
| Safety/close card-slot suppression (UI behavior) | Ready for implementation | App | The card system this depends on isn't built yet |
| "Don't know what to ask?" + question sheet (Increment 3) | Ready for implementation | App | Content complete (Curriculum V1.0); zero UI; hard-gated on the role selector merging first |
| Input group (textarea / Send / End) | Implemented | App | Live today |
| Consolidated status line (session-cap / connection-loss) | Still needs testing | App | Code exists but needs real hosting to populate/exercise |
| Current RefreshWarningBanner (production today) | Implemented | App | Live today; retires into the table bar under Increment 1 |
| Anachronism bridge | Implemented | App | Verified live today, unprompted, in a real conversation — caught a modern-doctrine reading correctly |
| Representative frame-break robustness fix | Implemented | App | Fixed and verified live 2026-07-20 — new epistemology bridge (`epistemology_bridge.py`), mirroring the modern-term bridge: Facilitator answers the system-level honesty briefly, then hands back a reframed, world-specific question to the Representative, who answers fully in character with real citations. Not yet committed to git |
| Representative voice quality (in-character depth, honest citation) | Implemented | App | Verified live today: 19/20 real academic questions answered excellently across 4 worlds |
| Relational-safety / drift governance (15 signal types) | Still needs testing | System | Substantially wired, real detector functions, invisible to the participant; "not fully validated live" |
| Frame-breaker classifier (fails open) | Implemented | System | Real, separate classifier call, invisible to the participant, confirmed in code |

## 7. Hosted Tour (S4-tour, T.1–T.6)

**DEFERRED TO PHASE 2 — not part of the current build cycle (2026-07-22).** Mark
decided Hosted Tour is a second-tier (Phase 2+) feature, not something this launch
builds, and directed that all Tour-related content be taken out of the current build
cycle across documents, UX, and code planning. This supersedes the 2026-07-20 note
below (which only paused further work until Friday's token reset) — the feature is now
out of scope for the current build cycle entirely, not just paused. Kept below as the
design/status record for when Phase 2 takes this up.

**Deferred by Mark, 2026-07-20 — held as a placeholder, not tested or built further
until after token reset (Friday 2026-07-24).** Only one draft tour scene exists
(Chloe's hosted church-service walkthrough) and it needs substantial content editing
before it's worth building against — this is being treated as its own project, not a
quick pass. Nothing below changes until that content work happens.

| Feature | Status | Surface | Why |
|---|---|---|---|
| In-app tour integration (threshold stop → beats → exit) | Ready for implementation | App | Blocked behind Increments 1 and 2, explicitly "never before/during P1" — and now also deferred until the tour-content project runs |
| Register strip / beat tracker / Exit chrome | Ready for implementation | App | Same |
| Honest-absence beat ("What We Cannot Show You") | Ready for implementation | App | Same |
| Standalone Chloe/Justin demo asset | Implemented | Website | Real, richly produced — but zero connection to the actual app; needs a content-editing pass before more scenes are worth building |

## 8. The Close (S5)

| Feature | Status | Surface | Why |
|---|---|---|---|
| Gracious close (Facilitator turn) | Ready for implementation | App | Backend logic restored today (was missing entirely); zero frontend UI renders it |
| "Anything else?" open pause | Ready for implementation | App | Same — backend-capable, no frontend |
| Reflection beat ("What stayed with you?") | Ready for implementation | App | Designed in to ship with the closing-sequence build; no frontend |
| Closing resources offer | Ready for implementation | App | Same |
| The door outward | Ready for implementation | App | Same |
| Current production close (bare "conversation has ended") | Implemented | App | This is literally what's live today |

## 9. Cross-cutting / infrastructure

| Feature | Status | Surface | Why |
|---|---|---|---|
| World: House-Church (Chloe) | Implemented | Both | Deployed in-app; advertised on the website |
| World: Desert-Monasticism (Papnoute) | Implemented | Both | Same |
| World: Syriac / Edessa–Nisibis (Mar Yausep) | Implemented | Both | Same |
| World: Bethlehem Circle (Albina) | Implemented | Both | Same |
| World: Alexandria Catechetical School (Theon) | Implemented | Both | Fixed and verified live today — was completely absent before |
| World: Imperial-Juridical Christianity | Still needs design work | App | World-build actively underway (Step 0–Doc_09 + Step 10 phases); not yet a surface feature at all |
| World: Donatism | Still needs design work | App | Planned in the Nine-World Portfolio; construction not started |
| World: Cappadocian | Still needs design work | App | Same |
| World: Latin Pastoral-Congregational | Still needs design work | App | Same |
| Accounts / sign-in (Supabase) | Still needs testing | System | Code-complete, smoke-tested; needs Mark's own account creation to go further |
| Per-tester session/API cap | Still needs testing | System | Code exists; unexercised until real hosting exists |
| Hosting — the app itself | Ready for implementation | System | Direct-API approach decided; not stood up |
| Hosting — public website | Implemented | Website | Live, real domain |
| Referral system backend | Implemented | System | Real endpoints, Supabase-backed, one-hop enforcement built |
| Referral system frontend | Still needs testing | Website | Wired but inert on `refer-a-friend.html` — API base URL empty; will work once deployment sets it |
| World icons (5 SVGs) | Ready for implementation | App | Locked and approved; not wired into any UI component |
| Table world-count ceiling safeguard | Ready for implementation | System | Designed 2026-07-20: a one-line assertion in `world_manifest.py` against a `LIVE_WORLD_CEILING` constant, mirroring this file's own existing single-source-of-truth discipline. See `Ministry/Features/Backend/CiC_Session_Recovery_and_World_Ceiling_Design_V0_1_DRAFT.md` |
| Session recovery after a restart (not general persistence — that already exists) | Ready for implementation | System | Corrected 2026-07-20: `transcript_logging.py` already durably persists every round to Supabase once configured — the real gap is that it's write-only, nothing rehydrates the in-memory session on a lookup miss. Design in the same doc as above |

## 10. Flagged — no record found anywhere

| Feature | Status | Surface | Why |
|---|---|---|---|
| Accessibility (screen reader / keyboard navigation) | No record | Both | Not mentioned anywhere in the UX spec or any status document |
| Internationalization / non-English support | No record | Both | Same |
| In-session feedback or bug-report mechanism | No record | App | Same |
| Terms of service / privacy policy screen | No record | Website | Same |

---

# Part 2 — Business & Organizational Development

Not the app, no UI to test — real work, different lifecycle. Status vocabulary here is
**Drafted** (a document/plan exists, not yet finalized) → **Decided** (a real decision is
logged/locked) → **Active** (currently being executed against, not just planned) →
**Dormant** (paused, not currently being pursued). This pass is workstream-level, sourced
from what's in each Ministry folder, not independently re-verified file by file the way
Part 1 was.

| Workstream | Folder | Status | Why |
|---|---|---|---|
| Marketplace positioning & differentiation | `Ministry/Marketplace/` | Drafted | Landscape scan, differentiation analysis, and positioning brief all at V0.1/DRAFT; a decision log records some calls already locked within it |
| Funder landscape & fundraising strategy | `Ministry/Funding/` | Drafted | Funder landscape, growth plan, budget proposals, seminary-alignment analysis, and three sponsorship one-pagers all at DRAFT stage; no funder relationship confirmed as executing yet |
| Entity formation & legal structure | `Ministry/Organization/` | Decided (entity) / Drafted (bylaws) | **Entity pivoted 2026-07-21** from a planned nonprofit to Faithways Studio, Inc., a Colorado Public Benefit Corporation (for-profit, 50/50 Mark and Susan Chadwick) — see `CiC_Nonprofit_Formation_Decision_Log.md`. Current Articles of Incorporation: `CiC_PBC_Articles_of_Incorporation_V0_4_FILING_READY.md` (supersedes the prior nonprofit `V0_2_FILING_READY` draft this row previously referenced); the entity-formation track is the most advanced of the three; other governance documents' individual statuses not re-verified in this pass |
| External messaging & positioning (FAQ, elevator speeches, letters to friends) | `Ministry/Communication/` (excluding the Brand Kit itself) | Drafted | Multiple V0.1/DRAFT pieces, some refreshed since; distinct from the Brand Kit tokens, which are a **Program** input (they govern the UX, §2 of the Full UX Design doc) |

**Explicitly out of scope for both tracks** (per standing project boundaries, not
re-litigated here): Equivice AI and The With Movement are separate projects/ministries
entirely, not CiC workstreams.

---

## Document log

- **V2.0 (2026-07-20):** Split into two tracks (Program / Business & Organizational
  Development) and added the Surface tag (Website/App/Both/System) to every Program
  feature, per Mark's request. Documented the lifecycle convention for graduating
  "future" items to Implemented. Part 1 content otherwise unchanged from V1.0.
- **V1.0 (2026-07-20):** First edition. Built at Mark's request for a feature-by-feature
  testing walkthrough of the entire user experience, starting with the three start options
  and four user choices. Synthesizes `CiC_Full_UX_Design_V1_0.md`, this session's own
  `CiC_UX_Implementation_Status_2026-07-19.md`, and `CiC_Product_Status_Report_2026-07-19.md`.
