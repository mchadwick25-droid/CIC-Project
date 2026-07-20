# CiC Task Board — Acceleration Jul–Dec 2026

**How this works:** This board is the day-to-day view of
`Ministry/Operations/CiC_Acceleration_Gantt_2026.gan` (open that in GanttProject —
free, ganttproject.biz). Task IDs match the Gantt file. **DO NOW** = every
predecessor is done (or it never had one) — you can work on these today, in priority
order. When something finishes: move it to DONE here, set it complete in
GanttProject, and promote anything it unblocks. When something new arrives: add it to
both files with a new ID and its dependencies. Ask Claude to resync both files any
time — say what's done and what's new.

**Funding gates (fixed):** $7.5K by Sept 1 · ~$25K by Nov 1 · $35–45K by Dec 31.
**Hard calendar gates:** reviewers engaged Sept 1 · entity filed ~Sept 15 · CCSA ~Nov 15 · Lane B go/no-go Dec 15.

_Last synced: 2026-07-19, later still (⚠ CORRECTION: this board previously carried
"re-engage Bedrock" as the live infra item — stale. `CiC_System_Hub_Decision_Log.md`
(2026-07-19) records **Bedrock dropped entirely; direct Anthropic API hosting decided**,
alongside the website's own infra. System Hub has already built the pilot-invitation
website pages (`cic-website/pilot.html`, `pilot-thank-you.html`) and the per-tester
session-cap code (`cic-poc/backend/app/session_cap.py`) — see the corrected DO NOW entry
below, moved out of DELAYED since it's active now, not paused. ⚠ SCOPE DECISION: Mark also
says P1 launches with the full feature set, not the minimum-viable path — see
`CiC_UX_to_Bedrock_Pilot_Readiness_2026-07-19.md` V1.2. Battery A (RM-8) is now the single
most schedule-critical action in the plan; #102 Run Prototype 1's dependency set expanded
accordingly — see READY NEXT.) Earlier 2026-07-19: UX design CLOSED OUT — the two
remaining graphics DRAFTs decided (reading surface = warm cream; Era-2 ground = no
variation, seating/object only); §G/§R approved; two Living-Table layout bugs found and
fixed (desktop + phone scene-lock); a content-integrity issue found and fixed (invented
Representative dialogue stripped from all mockups); a first-page greeting/CTA screen
(with per-world briefs) added to the Living Table mockups on both desktop and phone;
Alexandria/Theon installed as the fifth live world. Prior: 2026-07-18 late, Complete
Experience Storyboard shipped (SB-1..4); icon set 5/5 locked + era palette approved
(IC-1..8).) Later still (2026-07-19, System Hub thread restarted): this file,
`CiC_Dashboard.html`, `CiC_Gantt_Visual.html`/`.gan`, and `CiC_System_Hub_Decision_Log.md`
had gone missing from disk (an untracked-file loss during today's earlier merge to
`main`) — recovered intact, zero content lost, from an orphan git safety-snapshot commit
(`09f1de5`, see the decision log's 2026-07-19 recovery entry for how). Delta added since
that snapshot: the accounts/sign-in layer (`cic-poc/backend/app/auth.py`, a Supabase-backed
rework of `session_cap.py`/`transcript_logging.py`, `SignInScreen.tsx`) is built and
smoke-tested, uncommitted — new DO NOW item above.)_

---

## 🔴 DO NOW (all dependencies clear — priority order)

- [ ] **101/401 (revised) — Stand up direct-API hosting, session caps, spending limit
      (Jonathan / System Hub).** ⚠ **No longer delayed — active now.** Bedrock dropped
      2026-07-19 (`CiC_System_Hub_Decision_Log.md`): host `cic-poc` directly with
      `ANTHROPIC_API_KEY` on a Render/Fly.io-class platform (not Cloudflare Pages —
      static-only), set an Anthropic Console spending limit as the budget-control
      mechanism. **Narrower than it sounds:** the pilot-invitation website pages already
      exist and are live (`cic-website/pilot.html`, `pilot-thank-you.html`, verified
      clean console), and per-tester session capping already exists in code
      (`cic-poc/backend/app/session_cap.py`) — this is deploy-and-configure, not
      build-from-scratch. See `CiC_UX_to_Bedrock_Pilot_Readiness_2026-07-19.md` V1.2 for
      the full dependency-ordered path from here to hosting + Prototype Testing 1.
- [ ] **NEW — Create Supabase + Render/host accounts (Mark only).** The accounts/sign-in
      layer landed since the #101/401 note above was written: `cic-poc/backend/app/auth.py`,
      a Supabase-backed rework of `session_cap.py` (real per-user caps, not just
      per-tester-code) and `transcript_logging.py`, plus a real sign-in screen
      (`SignInScreen.tsx`) on the frontend. Smoke-tested working, currently uncommitted.
      Every Supabase-dependent feature is a documented no-op until `SUPABASE_URL`/
      `SUPABASE_SERVICE_KEY` (backend) and `VITE_SUPABASE_URL`/`VITE_SUPABASE_ANON_KEY`
      (frontend) are set — see both `.env.example` files. Account creation itself is
      off-limits for Claude to do on your behalf (standing constraint) — this is the
      actual next concrete step inside #101/401's "deploy-and-configure."

- [ ] **NEW — Build Increment 1** (table bar consolidation, Level-3 modal→panel/sheet,
      Single/Multiple toggle retirement, the full token/typeface swap into
      `table.css`). **Design approved by Mark 2026-07-17** — Full UX Design V0.1's
      RECOMMENDED visual identity (exact palette, Alegreya + Alegreya Sans, madder as
      action accent, typographic wordmark) and its flagged conflicts are now DECIDED.
      Ready to build against the spec directly; no further design decision blocks it.
- [ ] **NEW — Alexandria: install Theon into `cic-poc`** (world_manifest.py entry +
      data files — same pattern as World #9/Bethlehem Circle's install). **Mark
      approved 2026-07-17: "the Alexandria build is complete and ready for
      integration."** Verified directly, not taken on claim: Doc_01-09 approved,
      Representative Emergence done (Theon, Mark's own naming decision),
      Representative Construction Framework Phases 1-4 complete and reviewed,
      Permanent Prompt + World Capsule Core built and reviewed, all 45 Tier-1 lexicon
      chunks built and reviewed, and **Phase 5 boundary testing RETEST CLEARS** — two
      Round-1 marginal findings (self-narration leaks under adversarial pressure)
      were fixed and confirmed passing on a harder retest, zero hard Violation
      Indicators. **Caveats, disclosed not blocking (same standing gap every live
      world in this project carries):** Article 31 external scholarly review remains
      unconfirmed; Tier-2 lexicon chunks + reciprocity back-links are disclosed
      deployment-layer follow-on; this is the newest/thinnest-tested world in the
      portfolio (1 boundary-testing round vs. others' deeper passes) with no
      participant live-calibration yet.
- [ ] **301 — Reviewer package: V0.2 DRAFTED 2026-07-16 (90%)** — send package =
      `CiC_Article31_Reviewer_Brief_V0_2_DRAFT.docx` + `CiC_World1_Brief_for_Reviewers_V0_1_DRAFT.docx`
      (both in `Ministry/Scholarly-Review/`). Relational register, endorsement door
      open, 4–6-week staged pacing, world brief enclosed. Your part: two personal
      blocks + honorarium figure → send. Unblocks #302/#303/#306.
- [ ] **510 — Church-designated fund conversation** with the pastor. Unblocks all
      tax-deductible Ring 1 giving.
- [ ] **601 — Praxis interest form.** Five minutes. Calendar April 2027 while at it.
- [ ] **602 — Entity prep: DRAFTS EXIST 2026-07-16 (40%)** — Articles of Incorporation
      (with Article IV mission-lock) + Bylaws Skeleton, both in
      `Ministry/Organization/`, both built from the covenant and marked FOR ATTORNEY
      REVIEW. Remaining: your covenant markup, placeholder fills (registered agent,
      initial directors), attorney consult before the ~Sept 15 filing.
- [ ] **RM-7 — Review the Representative Modes demonstration.** React-to-first piece —
      the Chloe four-mode demo artifact
      (https://claude.ai/code/artifact/b9766b2f-47ae-4ebf-a89e-4a20358f409e) and Design
      Spec §6 (`Ministry/Technology/Representative-Modes/CiC_Representative_Modes_Design_Spec_V0_1.md`).
      No downstream gate depends on this specifically, but RM-8 is recommended to wait
      for it.
- [ ] **TR-confirm — Two tour interpretations owed.** (1) Confirm "the Representative
      is voice-only." (2) Confirm the standing commitment that evidentiary absence is
      never a locked feature, if tiering is ever revisited. Five-minute decisions;
      (1) directly gates TR-10.
- [ ] **TR-4 — L4 Tour Manifest Template + review-cycle definition.** No code, no
      live-system risk. The durable artifact type every future tour is authored
      against. Unblocks TR-7, TR-9, TR-10.
- [ ] **TR-5 — Tour Eligibility Gate as a repeatable checklist.** Generalizes the
      per-world evidentiary-analysis method already run once by hand into a
      one-per-world procedure.
- [ ] **TR-6 — Asset-sourcing sub-pipeline.** Generalizes the Chloe demo's verified
      public-domain image sourcing and source-text audio scripts into a reusable tool.
      Cross-ref: Marketplace thread's Adopt #6 hands off here.
- [ ] **TR-8 — Confirm the recording pipeline (GIF/slideshow) generalizes per world.**
      Already built once for the map thread; confirm and document for tour use.

## 🟡 READY NEXT (starts when the item above it finishes)

- [ ] **RM-8 — Representative Modes validation run, Battery A.** ⚠ **Escalated
      2026-07-19: Mark decided P1 launches with the full feature set, not just the core
      encounter (`CiC_UX_to_Bedrock_Pilot_Readiness_2026-07-19.md` V1.2) — this makes
      Battery A the single most schedule-critical action in the whole plan, not just the
      top validation priority.** Increment 2 (role selection) can't merge without it
      passing, Increment 3 can't start without Increment 2, and P1 itself now needs both.
      The feature's existence gate (content-invariance, five arms, blinded claim/
      confidence extraction) — a mode that fails it is a fork of the truth and fails
      outright. Costs live API calls; you schedule it. Start this now, in parallel with
      Increment 1 — not after RM-7.
- [ ] **102 — Run Prototype 1.** Dependency set expanded 2026-07-19 (full-feature-set
      decision, see V1.2 above): direct-API hosting live **and** Increment 1 **and** the
      Tier 0 four **and** RM-8/Battery A passed + Increment 2 merged **and** Increment 3
      merged **and** Hosted Tour **and** Question-First Entry **and** Guided Onboarding
      **and** the Living Table's live wiring — not just hosting alone. Protect this window
      once it starts — no new outreach until ~Aug 10 from that point.
- [ ] **302 — TEDS professor outreach** (after 301). Send within days of the brief
      existing; his August matters.
- [ ] **202–206 — Ancient worlds 5–9** (from Aug 3, sequential, ~6 working days each
      including battery + deployment gates). **Alexandria (Doc_01-09 complete
      2026-07-17) is already ahead of this Aug 3 start** — likely fills the "world 5"
      slot rather than waiting for it; needs your confirmation (see DO NOW).
- [ ] **201 — Guided starters: ALL 4 WORLDS DRAFTED 2026-07-16 (75%)** — pulled 3 weeks
      left. `CiC_W1_Guided_Starters_V0_1_DRAFT.md` (Post-Apostolic),
      `Guided_Starters_V0_1_DRAFT.md` (Syriac), `CiC_W3_Guided_Starters_V0_1_DRAFT.md`
      (Desert), `hal_Guided_Starters_V0_1_DRAFT.md` (Hieronymian) — each in its world
      folder, each with builder grounding-flags for your review. Content-ready is only
      half of #402's gate now — see BLOCKED: it also waits on role selection (RM-10 /
      Increment 2) landing first, so the UI doesn't ship a question-serving screen the
      selector underneath it hasn't caught up to.
- [ ] **NEW: outreach one-pagers DRAFTED 2026-07-16** — church-fund, world-sponsorship
      ($3,500), Wabash pilot (all in Ministry/Funding, awaiting markup).
- [ ] **NEW: landing page copy DRAFTED 2026-07-16 (#704 at 50%)** —
      `Ministry/Communication/CiC_Landing_Page_Copy_V0_1_DRAFT.md`; quote slot waits
      for P1; page build remains.
- [ ] **218 — Weekly quality-upgrade batch** (standing rhythm from Aug 3).
- [ ] **RM-9 — Batteries B–D** (drift / general-mode overclaiming / deconstructing-mode
      adversarial pressure), after RM-8 passes.
- [ ] **TR-7 — Templated tour renderer** (after TR-4). Generalizes the Chloe HTML so a
      world supplies only manifest + assets.
- [ ] **TR-9 — Scene-narration validation probe category** (after TR-4; validation-suite
      thread). No tour ships on conversational validation alone.
- [ ] **TR-10 — House-Churches/Chloe: formalize into a reviewed Tour Manifest** (after
      TR-4 + the TR-confirm gate above). Class A, strongest case, demo already built.
- [ ] **Increment 2 — Role selection UI** (after Increment 1 build lands). Gated on
      RM-8/Battery A passing (the rename is done — executed in code 2026-07-18,
      commit `9774447`, no longer a blocker).
- [ ] **IC-10 — Atlas adopts the ten era grounds** (World Orientation Map thread). Replace the
      atlas's single uniform ground with the approved per-era palette so the icon tables and the
      atlas read as one system; values ready in the icon spec §7 (Era 1 `#EFDDB3`, Era 2
      `#EDDEB9`, … → Global-Church pale vellum). Owned by the World-Map thread; unblocked.

## 🔵 BLOCKED (waiting on a predecessor — don't start these)

| ID | Task | Waiting on |
|----|------|-----------|
| 103 | P1 analysis: actuals, quotes, story | 102 (P1 finishes ~Aug 10) |
| 701 | Packet V0.2 (the presentable business plan) | 103 |
| 702 | Letter to Friends + FAQ refresh | 103 |
| 703 | Demo polish (20-min guided Table) | 103 |
| 704 | Landing page + interest list | 702 |
| 501 | Ring 1 ask to 15–20 names | 103, 510, 702 |
| 502 | GATE $7.5K (Sept 1) | 501 |
| 303 | Second reviewer outreach | 301 (start Aug 17) |
| 304 | GATE reviewers engaged (Sept 1) | 302, 303 |
| 305 | Round 1 holistic review | 304 |
| 208 | Reformation selection + LT confirmations | 206 |
| 209–215 | Reformation worlds 1–7 | 208, sequential |
| 603 | File CO articles (~Sept 15) | 602 |
| 604 | 1023-EZ | 603 |
| 605 | Board recruitment (3 clean independents) | 602 posture (start Aug 17) |
| 606 | CCSA registration | 603 |
| 607 | Bank + bookkeeping | 603 |
| 608 | First board meeting (+ compensation policy) | 603, 605 |
| 613 | Stipend trigger policy adopted | 608 |
| 612 | GATE nonprofit fully established | 608, 606 |
| 403 | Engagement One (500-user infra) | 103, 502 |
| 104 | P2 cohort (~100) | 103, 402 |
| 503 | World sponsorship asks | 701, 703 |
| 504 | GATE ~$25K (Nov 1) | 503 |
| 505 | Paying pilots (fork-decider) | 701, 703 |
| 705 | Acadia peer call (Aug) | — (scheduled Aug 17; can pull left if P1 allows) |
| 706 | Wheaton conversation | 701, 703 |
| 707 | Tom Beck note | 701, 703 |
| 306 | Reformation reviewer | 301 (start Oct 1) |
| 308 | Round 2 review | 306, 213 |
| 406 | Audit + minor-caution mechanisms | 403 |
| 404 | Engagement Two (pre-public audit) | 403, 504 |
| 407 | GATE Lane B go/no-go (Dec 15) | 404, 406, 309 |
| 105 | Early Access 300→500 | 403, 104 |
| 106 | GATE 500 users (Dec 18) | 105 |
| 506 | NCF/DAF asks | 603 |
| 507 | Public year-end appeal | 606 |
| 609/611 | IRS determination → TechSoup/AWS credits | 604 |
| 610 | D&O insurance | 605 |
| 708 | Lilly positioning | 706, 305 |
| 709 | Praxis application prep | 603 |
| RM-10 / Incr. 2 | Role selection UI + Representative Modes merge decision — owned by front-end thread, never before/during P1 | RM-8 (Battery A must pass) |
| 402 / Incr. 3 | Post-table question serving (role-served walks) shipped in UI | 201 (content review) **and** RM-10/Increment 2 (role selection must land first — a question-serving screen can't ship ahead of the selector it's served through) |
| RM-11 | Onboarding copy: mention role selection | RM-10/Increment 2 (or earlier, content-only) |
| RM-12 | `role=`/`worlds=`/`mode=` URL parse-site reconciliation | whichever merges second: RM-10/Increment 2 or Increment 4 (World Map merge) |
| RM-13 | Tier B: role → default transparency mode | Mode One/Two toggle (not yet built) |
| RM-14 | Tier C: closing-resources register by role | closing-resources feature (not yet built) |
| RM-15 | Tier D: role-aware safety classifiers | deliberately not designed — would require full adversarial re-test if ever wanted; not scoped |
| TR-11 | Syriac/Mar Yausep tour: manifest for `syrstory009` | TR-4, TR-6, and a 4th-century pronunciation research pass |
| TR-12 | Desert/Papnoute tour: manifest for `desertstory008` (no worship-service tour) | TR-4, TR-6, TR-11 (sequenced after) |
| TR-13 | Bethlehem Circle/Albina tour: manifest for `hal_story10` (no liturgical tour) | TR-4, TR-6, TR-12 (produce last — newest, least live-tested world) |
| TR-14 | cic-poc integration: `tour_manifest.py`, mode-overlay, invitation card, tour view | Increment 1 (budget compliance) **and** RM-10/Increment 2 (role selection); never before/during P1 |
| Incr. 4 | World Map Tier A merge — owned by front-end thread, never before/during P1 | 402/Increment 3 |
| TR-15 | World Map "Take a tour" handoff | TR-7, TR-14, **and** Increment 4 (the map itself has to be merged before it can hand off to a tour) |
| — | Cross-cutting flag: production TTS/voice + audio hosting decision | not yet scheduled — real cost decision tied to the voice-only ruling |
| — | Cross-cutting flag: image licensing at production scale + zoomable high-res artifacts | not yet scheduled — Marketplace thread's Adopt #6 hands off here |

## ✅ DONE

- [x] **UX design CLOSED OUT — zero open decisions remain (2026-07-19).** The two
      standing graphics DRAFTs decided: reading surface = brand warm cream
      (`--gold-wash #FBF2E2`), Era-2 ground = no separate background (one reading surface
      for both eras; the Era-1/Era-2 template distinction is seating/object only). §G
      (Guided onboarding) and §R (question-routing UI) — the storyboard's two never-
      designed screens — approved by Mark. Two Living-Table layout bugs found and fixed
      this session (desktop, then independently on phone): figures and the table line
      were positioned in separate, un-linked coordinate boxes tuned by eye; fixed by
      scene-locking both platforms to one shared coordinate system. A content-integrity
      issue was also found and fixed: invented first-person Representative dialogue in
      the graphics mockups, replaced everywhere with explicitly-labeled placeholder text
      (a standing rule now on record against this recurring). **Produced:**
      `Ministry/Operations/CiC_UX_to_Bedrock_Pilot_Readiness_2026-07-19.md` — the
      dependency-ordered path from here to real hosting and Prototype Testing 1,
      separating what's Mark's to decide (stand up hosting — since revised from Bedrock
      to direct-API, per System Hub's own same-day decision — Battery A go-ahead, the 2
      Guided-Questions content calls, the Chloe tour voice read, Section 10, Gantt IDs)
      from what's build-thread execution once those clear.

- [x] **IC-9 — Icon full-family review RUN: FAMILY PASSES, the five locks stand
      (2026-07-18, overnight).** Frame/silhouette/objects/flags/skin-spread/template checks
      all green, measured from the masters; two findings fixed in-pass (three in-file lock
      headers aligned; desert's INFERENCE keyword added); three watch items for daylight
      (W1 Chloe cup tone — observation only · W2 Era-2 figures on the live table render ·
      W3 Theon's manifest colour unassigned → World-Map thread).
      `Brand-Assets/CiC_World_Icon_Family_Review_V1_0.md`; spec §7d updated.

- [x] **SB-1..SB-4 — Complete Experience Storyboard shipped + spec-text bug fixed
      (2026-07-18, overnight).** Every path S0→S5 storyboarded (descriptive spine, every
      decided piece cited; five visual frames with build-status flags); the two
      never-designed screens designed — **Guided onboarding** (three Facilitator-hosted
      beats → a prepared table) and the **Question-First Tier-3 routing UI** (held question
      → honest considering → proposal / clarify-once / honest null); **SB-4 fixed same
      night** — `CiC_Full_UX_Design_V1_0.md` swept of stale camera/chip text (V1.0.2), §G/§R
      integrated as states, the Increment-1 handoff bumped to V1.1 (long-form transcript
      §1.3), the icon spec §1b synced. Storyboard:
      `Ministry/Technology/CiC_Full_UX_Storyboard_V1_0.md`; hub hand-off:
      `CiC_UX_Storyboard_System_Hub_Update_2026-07-18.md`. **Mark's morning rulings:
      §G + §R APPROVED; side "other choices" DROPPED** — the journey now has zero
      undesigned and zero unapproved screens. **Still open from it:** SB-5 stale "four
      live worlds" (World-Map thread) · SB-6 Theon tour-eligibility (TR-5) · SB-7 tour
      stop-numbering line · SB-8 "house church" naming gap (world threads) · the
      warm-cream reading surface (DRAFT, graphics pass).

- [x] **IC-1..IC-8 — World Representative icon set: all five built & LOCKED + era-ground
      palette APPROVED (2026-07-18).** One governed connected-bust template (Era-1 style;
      Era-2 = same figure on a different ground). Each object/appearance verified against its
      world's OWN construction record, flagged DOCUMENTED/INFERENCE; anti-anachronism enforced.
      The five: **Chloe** (House-Churches, cup — V1.8, skin warmed to a Greek-East olive) ·
      **Papnoute** (Desert, cracked jug) · **Theon** (Alexandria, open scroll; this world also
      promoted from "example" to live) · **Mar Yausep** (Syriac, one Gospel book; first Era-2) ·
      **Albina** (Bethlehem Circle, wax tablet). Two women, three men, five distinct objects, a
      skin spread by setting. **Era-ground palette APPROVED & canonical:** one warm→cool flow
      across ten eras, light+dark (Era 1 `#EFDDB3`/`#241A0C`, Era 2 `#EDDEB9`/`#221A0E`, …).
      Masters in `Brand-Assets/World-Icons/`; locked bases in `_working-base/`. Spec §7c/§7d +
      §7 palette. Hand-off: `Brand-Assets/CiC_World_Icons_System_Hub_Update_2026-07-18.md`.
      Open follow-ons: IC-9 (family review, DO NOW) and IC-10 (atlas hand-off, READY NEXT).

- [x] **464 — Transcript-logging gap fixed and VERIFIED live (2026-07-17).** Frame-breaker
      and relational-safety branches in both endpoints now call `write_transcript`;
      confirmed live on an isolated backend with a real frame-breaker exchange
      captured correctly.

- [x] **Full UX Design V0.1 — APPROVED by Mark (2026-07-17).** Whole journey drawn,
      desktop+phone, every screen five-count-checked. Visual identity (exact
      palette, Alegreya + Alegreya Sans, madder action accent, typographic
      wordmark), the Level-3 modal→panel fix, and the reflection-beat timing all
      converted from RECOMMENDED to DECIDED. Next: build Increment 1 (see DO NOW).

- [x] **Alexandria — Doc_01 through Doc_09 + full Representative build (Theon) +
      Phase 5 boundary testing, all complete and Mark-approved for integration
      (2026-07-17).** Representative Emergence (Mark's own naming decision),
      Construction Framework Phases 1-4, Permanent Prompt + World Capsule Core, all
      45 Tier-1 lexicon chunks, and boundary testing (RETEST CLEARS, zero hard
      Violation Indicators) all reviewed and cleared. Next: install into `cic-poc`
      (see DO NOW).

- [x] **RM-1..RM-6 — Representative Modes: design + build, self-verified (2026-07-16).**
      Design spec + Chloe four-mode demo, prompt architecture, exploration branch build
      (`claude/representative-modes-exploration`, commit `1127c09`, local-only), live +
      assertion verification in mock-LLM mode (byte-identical no-role baseline), 5-battery
      validation plan authored, integration assessment + decision log. Inert until RM-7
      (Mark's review) and RM-8 (Battery A, the real gate) — see DO NOW / READY NEXT.
- [x] **TR-1..TR-3 — Hosted Tour: strategy, evidentiary analysis, Chloe demo build,
      decision log (2026-07-16).** Self-contained immersive demo of Justin's Sunday
      gathering (`pahcstory006`, Tier 1) — four verified public-domain images, two
      source-text audio readings with transcripts, an honest four-part decline stop.
      Not integrated into `cic-poc`; nothing merged. Demo:
      https://claude.ai/code/artifact/74a8c750-b828-443d-8d8a-e83f038a6eb7

---

**Standing rules carried from the Acceleration Plan:** count is the release valve
(Reformation 7 → 5 before any gate bends); if P2 and the build calendar strain, the
build calendar wins; review status is always disclosed honestly; no funder deadline
compresses a gate.
