# CiC Product Status Report — every function and feature, as of 2026-07-19

**Purpose:** a complete, verified inventory of what's actually working versus designed-only
versus built-but-not-merged, across the whole product surface — the public website, the
running app, and every named feature. Every claim below was checked directly (file read,
grep, live browser load, or direct code inspection), not taken from a tracking document's
word for it.

**One thing to notice across almost every section below: real, tested, good work sitting on
an unmerged branch, deliberately held back from `main` — not abandoned, not broken, just
not yet landed.** This is the single most common status this report found, more common than
either "working" or "not started."

---

## 1. The public website (`cic-website/`)

**Live, real, no console errors** — loaded `index.html` and `atlas.html` directly, both
render cleanly, zero JS errors.

**A real, live bug found: the homepage claims "FIVE MOVEMENTS ARE LIVE TODAY," including
Alexandria.** This is public-facing, not just an internal tracking-doc error — a real
visitor or pilot tester reading the homepage right now would expect to talk to Alexandria's
Theon and find no such world exists in the running app (see §5). Same root cause as the
Dashboard error found and fixed earlier today; this one wasn't caught because it's a
different file. Needs the same correction.

**Pages:** `index.html`, `about.html`, `tour.html`, `support.html`, `pilot.html`,
`pilot-thank-you.html`, `refer-a-friend.html`, `atlas.html` — all present, all static HTML,
no backend dependency except `pilot.html`'s interest form (mailto-based, no third-party
account, by standing constraint).

## 2. The Atlas / World Orientation Map

**Real, interactive, live on the marketing site — not a placeholder.** `atlas.html` embeds
a genuine zoomable/pannable map (`world-map.html`, 289KB, real event-listener/SVG
interactivity) plus a filterable list fallback (`world-atlas-list.html`). Built from a
147-entry historical census across 9 eras, with its own external scholarly review.

**Not wired into the actual conversational app (`cic-poc`) on `main`** — zero references to
"atlas" or "world-map" in the current frontend. But a real, tested integration already
exists on an unmerged branch (`claude/world-map-merge-into-main`): bidirectional handoff
between the map and world selection, verified live against real dev servers, deliberately
held back per the standing "never merge/redeploy before or during a scheduled pilot sitting
window" rule.

**Open scope decision, not yet made:** does the Atlas stay a secondary orientation view, or
become the primary world-selector? This gates whether/how the integration branch merges.

**Status: Working demo (marketing site) / Tested-but-unmerged (app integration) / Open
scope decision pending.**

## 3. Four-role / participant-type selection (Regular visitor, Pastor/teacher, Academic/scholar, Reevaluation)

**Not live on `main`.** No role selector exists in the running app today. Real, working code
exists on a different unmerged branch (`claude/representative-modes-exploration`) — an
optional four-role selector on the world-selection screen, wired through session start into
`ConversationState.participant_role`, backend response-register logic. Verified only in
mock-LLM mode; live-API validation (Battery A / RM-8) hasn't run, and this project's own
standing rule is nothing merges before or during Prototype Testing 1.

**One open naming inconsistency:** participant-facing copy settled on "Reevaluation" as the
label (2026-07-16 decision), but the exploration branch's code still uses `deconstructing`
as the internal role id/URL param. Needs reconciling before merge.

**Status: Built, unmerged, unvalidated against a live model.**

## 4. Guided/starter questions ("I don't know what to ask")

**Content complete for all 4 live worlds, zero UI exists.** Every world has a drafted
guided-starters file, each explicitly headed "DRAFT — awaiting Mark's review. Not deployed."
Zero references to "guided" or "starter" anywhere in the frontend source.

**Hard-blocked behind the role-selector above** — guided starters are role-tailored, so this
can't be built until Feature 3 merges. Both are now required-for-P1 per the 2026-07-19
full-feature-set scope decision, not optional polish.

**Status: Content-complete, zero code, blocked on a dependency that's also unmerged.**

## 5. World support — the base program's actual roster

**Confirmed via direct inspection of `world_manifest.py` and `cic-poc/backend/data/`: 4
worlds registered and deployed, not 5.** House-Church (Chloe), Syriac (Mar Yausep),
Desert-Monasticism (Papnoute), Bethlehem Circle/Hieronymian (Albina). **No Alexandria entry,
no `alexandria_world` data directory** — directly contradicting both the Dashboard and the
public website (§1). Alexandria's construction record (116 files) is complete and real;
only the install step is missing or was lost. Task Board already carries the fix as a DO NOW
item.

**All 4 deployed worlds' Permanent Prompts and 2 World Capsule Cores were found drifted from
their own reviewed World-Builds construction record earlier today, root-caused to a real
live-testing engineering workstream that never synced back — fixed and synced as of this
session** (see decision log, 2026-07-19).

**Lexicon confidence-vocabulary compliance** (Article 17): mechanically re-verified this
session — Syriac 9/9, Alexandria 44/45 (not deployed), Bethlehem Circle 4/15, House-Church
0/13, Desert-Monasticism 0/9. A related, unresolved interpretive question (does Article 17
require its literal label in the *deployed* chunk, or is the Deployment Lexicon Chunk
Template's "Distortion Risk" section the real intended deployment-layer expression) is still
awaiting Mark's answer before any of these get mechanically "fixed."

**Nine-world portfolio, confirmed real (`CiC_Step0_Conclusion_FINAL_v2.docx`, found this
session):** House-Church, Alexandria, Desert-Monasticism, Donatism, Cappadocian, Imperial and
Juridical Christianity, Syriac, Latin Pastoral-Congregational, Hieronymian/Bethlehem Circle.
5 built, 4 not yet started (Donatism, Cappadocian, Imperial-Juridical — build thread just
launched, Latin Pastoral-Congregational).

## 6. The base program (`cic-poc`) — core architecture

**Core conversation flow: working.** FastAPI + LangGraph, in-memory sessions (POC-only,
lost on restart). Single-world and multi-world ("table") session start; streaming (SSE,
what the frontend actually uses) and non-streaming endpoints both live. The streaming path
chains frame-breaker → relational-safety → sensed-closing-sequence → anachronism-bridge
intercepts before representative generation, with drift/dominance/convergence checks
running invisibly after the response streams so governance never adds participant-facing
latency.

**Facilitator governance: substantially wired, not fully validated live.** 15 real drift
signal types (9 single-turn, 5 multi-world-table, 1 self-narration backstop), all wired to
real detector functions — not designed-only. Relational-safety (Acute Distress/Harmful
Dynamic) confirmed built and live-tested 2026-07-13. Frame-breaker is a real separate
classifier call, fails open safely.

**Accounts/auth: code-complete, currently a no-op.** `auth.py`/`session_cap.py`/
`transcript_logging.py` all correctly short-circuit to unauthenticated/uncapped/no-op until
`SUPABASE_URL`/`SUPABASE_SERVICE_KEY` are set — smoke-tested working, uncommitted, per
today's earlier work.

**Frontend: functional, pre-redesign.** 11 components, real SSE consumption into React
state, working onboarding → sign-in → world-selection → chat flow with lexicon highlighting
and citation modals. Predates the approved Increment 1 visual redesign (see §9).

**Deployment: local-only.** No Dockerfile/Procfile/render.yaml/fly.toml anywhere in
`cic-poc/`. Direct-Anthropic-API hosting is decided but not stood up — matches what's
already on the Task Board.

## 7. Referral system

**Backend fully built and real, frontend wired but inert until deployment.**
`POST /api/referral/generate` and `POST /api/referral/redeem` both exist in `main.py`,
Supabase-backed, with one-hop-referral enforcement already implemented. `refer-a-friend.html`
has real JS calling these endpoints, but the API base URL constant is empty (`''`) — so
today it silently falls back to a copy/paste message instead of calling the real backend.
Will start working automatically once that constant is set post-deployment; not a code gap,
a configuration one.

## 8. Hosted Tour

**Real, richly-built standalone demo (960KB, embedded fonts/images/audio), zero connection
to `cic-poc`.** A real scene (Justin Martyr's Sunday gathering) fully produced. Its own
integration note states plainly: "Nothing here has been wired." Actual `cic-poc` integration
(TR-14: a real `tour_manifest.py`, mode overlay, invitation card) is blocked behind
Increments 1 and 2, explicitly "never before/during P1."

## 9. The Table's multi-world ceiling — a real, load-bearing finding

**The 5-world Table ceiling described in the Table Design Document is a stated policy
commitment, not a technical limit.** Its own text: *"No mechanism in the system prevents a
sixth world from being called. The Facilitator's curatorial judgment is what holds the
ceiling."* Confirmed in code — the only hard cap found is `MAX_MULTI_WORLD_TURNS = 6`, a
per-round turn limit, not a world-count limit. Worth knowing before any pilot session, not
just a documentation nuance.

## 10. Front-end Increments 1–3

**Increment 1 (table bar consolidation, modal→panel, toggle retirement, token/typeface
swap): approved 2026-07-17, not started.** Confirmed directly in code — `TheTable.tsx`
still contains the old toggle UI Increment 1 is supposed to remove. Increment 2 (role
selection UI) and Increment 3 (post-table question serving) are both gated behind it and
behind Battery A / content review respectively.

## 11. World Icons

**Designed, locked, approved — not wired into the frontend at all.** 5/5 SVGs locked
2026-07-18. Grepped the actual chat UI (`TheTable.tsx`, `MessageBubble.tsx`): the
Representative nameplate is text-only, no image/icon reference anywhere in the code. These
exist purely as brand assets today.

---

## What this adds up to

**The single clearest pattern across this whole report: a lot of real, tested, good
engineering work exists — on branches that never merged.** The Atlas integration, the
four-role selector, the world-map handoff — all built, all verified against a live dev
server, all deliberately held back, mostly by the same standing rule (nothing merges
before/during a pilot window). That rule is sound. But it means "is this feature done"
and "is this feature live" are two different questions for almost everything in this
report, and today's Dashboard/website both collapsed that distinction for Alexandria
specifically, which is the one place it actually misled.

**Two things worth fixing before anything else, in order:**
1. **The public website's "five movements are live today" claim** (§1) — a real visitor
   reads this today and will be told something false about what they can do.
2. **Everything currently gated behind Increment 1**, since it's the single dependency
   unlocking the largest number of downstream features (role selection, guided questions,
   Hosted Tour integration, the Atlas Tier A/B decision).

**Full findings, by feature, all independently verified this session — nothing below is a
tracking document's claim taken on faith:**

| Feature | Status |
|---|---|
| Public website | Live, working, one false claim (Alexandria) |
| Atlas / World Map | Live demo on website; tested integration unmerged |
| 4-role selection | Built on unmerged branch, unvalidated live |
| Guided questions | Content-complete, zero UI, blocked on role selector |
| Worlds (deployed) | 4 live (not 5); lexicon compliance mixed; prompt drift fixed today |
| Base program | Core flow + governance working; auth code-complete/inert; local-only |
| Referral system | Backend real; frontend inert pending deploy config |
| Hosted Tour | Real standalone demo; zero app integration |
| Table world-ceiling | Policy only, not enforced in code |
| Front-end Increments 1–3 | Approved, not started |
| World Icons | Locked, not wired into any UI |


