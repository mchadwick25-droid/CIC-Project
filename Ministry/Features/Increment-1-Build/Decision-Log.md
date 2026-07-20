# Decision Log — Increment 1 Build

## 2026-07-20 — All six commits built and verified; one merge-timing question handed back, one pre-existing gap found and flagged

**What this is:** the build thread dispatched by `Ministry/Features/Increment-1-Build/
Launch-Prompts/CiC_Increment1_Build_Thread_Launch_2026-07-20.md`, executing
`CiC_Build_Handoff_Increment1_V1_0.md` against `cic-poc/frontend/`.

**Branch:** `claude/increment1-build-brand-floor`, off `main` (the branch
that functions as `cic-poc`'s live/working state today — the historical
name `claude/cic-poc-backend-facilitator-upgrade` no longer exists;
recent `cic-poc` commits land directly on `main`). Built in an isolated
git worktree (`.claude/worktrees/increment1-build-brand-floor/`), not the
shared main working directory, since that directory had other threads'
uncommitted work in progress at dispatch time (Atlas World Map, the IJC
world-build). `main` itself is untouched — nothing merged.

**The six commits, each independently reviewable, following the handoff's
own §8 sequence exactly:**

1. `table.css` tokens + self-hosted Alegreya/Alegreya Sans + the long-form
   transcript (§1, §1.3) — the finalized manuscript palette, madder split
   from gold-leaf (previously the same hex value), bubble/card grammar
   struck for all three transcript voices in favor of labeled flowing
   prose, wide left-anchored column.
2. The table bar + `RefreshWarningBanner` retirement (§2) — one quiet
   chrome line replacing the old header + standalone banner; seats left,
   one consolidated status line right.
3. Level-3 surfaces: modal → side panel (desktop) / bottom sheet (phone)
   (§3) — a new shared `Level3Panel` wrapper; the transcript column
   narrows on desktop so the 420px panel never overlaps it (verified
   against actual rendered geometry, not assumed).
4. Single/Multiple toggle retired, mode emergent from seat count (§4) —
   the Begin button always visible, named per count.
5. The "Arriving" favicon + world-selection lockup/motion (§5) —
   rasterized from the vector master at each target size; the lockup
   plays its build-then-settle motion once per browser session.
6. The breakpoint pass (§6) — phone threshold renamed 600px → 639px,
   table-bar truncate/tap-to-expand, 44px inline-mark hit areas,
   safe-area-inset-bottom on the input.

Commit SHAs on the branch: `a4e0aed`, `6194587`, `848c8c6`, `1d2e03b`,
`6edcd72`, `fb3f771`.

**How this was verified — real app, real browser, not just compiled:**
the full backend (`langchain`, `sentence-transformers`, `faiss-cpu`, etc.)
was not stood up — installing that stack from scratch in this environment
would have cost far more time than the frontend work itself warranted.
Instead, verified against the actual Vite dev server plus a small,
dependency-free, stdlib-only mock API (scratch-only, never committed)
serving realistic data matching `backend/app/world_manifest.py`'s real
world names/colors/periods and the real SSE streaming event shape
`useConversation.ts` expects. Checked via direct DOM inspection and
`getComputedStyle` assertions rather than eyeballing screenshots alone —
more precise for exact token/geometry acceptance criteria (e.g. confirmed
the Level-3 panel's left edge sits exactly 24px clear of the narrowed
transcript's right edge at 1280px width, not just "looks fine"). One full
screenshot captured for visual record; the Browser pane's screenshot tool
became unreliable partway through this session (repeated timeouts against
a page that was demonstrably rendering correctly per every DOM check) —
noted here so it isn't mistaken for an app defect.

**This means the actual backend integration was not exercised this
pass** — real LLM streaming, `session_cap.py`, transcript logging,
Supabase auth. Only frontend behavior against realistic canned data.
Mark's standard hosted smoke test (handoff §7 — hovers, clicks, a Level-3
open, transcript captured, session cap enforced) still needs to run
against a real deployment before any invitation goes out, same as always.

### Deviations and judgment calls made along the way, each reasoned through rather than guessed

- **Alegreya Sans has no 600 weight.** The actual OFL family ships
  400/500/700/800/900 (confirmed by listing the installed `@fontsource`
  package files, not assumed). Loaded 400/500/700 and left existing
  `font-weight: 600` declarations as-is — browsers match to the nearest
  loaded weight of the same family when an exact one isn't available, so
  this has no visible effect; no component code needed to change.
- **The session-cap status-line priority slot is reserved but currently
  unreachable.** The build handoff's table-bar status line names two
  priorities (refresh caution, then a "nearing the length limit" notice)
  — but no per-conversation turn/token cap is surfaced by the backend
  today. `session_cap.py` only caps the *number of sessions* a signed-in
  participant can start, checked once at session creation, not a
  mid-conversation length signal. Built the priority-ordered status-line
  logic to support this second message whenever that data exists, but it
  never fires today. Real gap, not a guess dressed up as one.
- **Level-3 side-panel vs. bottom-sheet split at 900px, not 640px.** The
  handoff's own two breakpoints are ≥900 desktop / <640 phone with
  "narrowing gracefully between" — but a fixed 420px side panel would
  swallow most of a 640–899px viewport. Since no third "tablet" grammar
  is designed anywhere in the source docs, treated everything below
  900px as the bottom-sheet case. Same reasoning applied to the
  world-selector grid's single-column collapse (§6 names 900px there
  explicitly, so this is consistent, not a one-off exception).
- **Dropped per-representative color tinting on transcript labels.** The
  old code color-coded each representative's name in a multi-world table
  via `--world-accent`. §1.3 specifies a single uniform gold-leaf label
  color for the Representative voice ("a gold small-caps label"), and
  the acceptance line ("three visually distinct voices by label + type
  treatment alone") only asks for three voices, not N per-representative
  colors. Multi-representative disambiguation now relies on the label
  text itself (`{name} · {world}`), matching how the table bar already
  handles it (seat dots keep their per-world tint; the transcript prose
  does not).
- **Removed the pre-existing world-card checkmark pseudo-elements.**
  Retiring the toggle (§4) means every selection — not just multi-select
  — now shows the numbered order badge. The old `::before`/`::after`
  checkmark circle occupied the exact same corner and would have painted
  on top of that badge on every single-world selection, the most common
  case. This is a real rendering collision the toggle-retirement change
  causes, not a pre-existing bug fixed opportunistically — removed as
  part of §4's own scope.
- **Caught and fixed a real bug before it shipped:** `ArrivingLockup`'s
  first version wrote to `sessionStorage` inside a `useState` lazy
  initializer. React StrictMode deliberately double-invokes that
  initializer on mount; the second invocation saw the first invocation's
  own write and computed `shouldPlay=false` on every mount, including the
  real first one — the motion would never have played for a real visitor.
  Caught by testing with `sessionStorage` cleared between checks, not
  assumed correct because it compiled. Fixed by keeping the initializer a
  pure read and moving the write into a `useEffect`.

### Found, not fixed: the phone Level-2→Level-3 tap grammar

The handoff's §3 says to "keep the trigger grammar exactly," including:
*"On phone, tap = the Level-2 popover carrying one 'Full entry →' action
= this sheet."* Checked `LexiconHighlight.tsx` and `CitationMarker.tsx`
directly — both only wire `onMouseEnter` (desktop hover) and `onClick`
(opens Level-3 immediately). On an actual touchscreen, a tap fires
`onClick` straight away, skipping the Level-2 popover step entirely. This
predates Increment 1 — the old centered-modal version had the identical
gap, since the interaction code was written mouse-first from the start —
but §3 names it as part of what this increment's build must satisfy.

**Not fixed here:** building a real touch-aware Level-2 popover with a
"Full entry →" action is new interaction code in two components that
§3's own scope describes as "content unchanged, only the
container/positioning changes" — a distinct, non-trivial piece of work,
not a container change. Per the launch prompt's own instruction ("if you
find a real defect outside this scope while working, log it and hand it
back rather than fixing it inline"), flagging it here rather than
expanding this increment's scope. Practical effect today: a phone
participant tapping a lexicon term or citation marker gets the full
Level-3 panel immediately (arguably a *shorter* path to the same
information, not a broken one) — but it is a real deviation from the
spec'd grammar and from parity with how a desktop hover-then-click visit
plays out.

### The merge-timing question — unresolved, handed back per the launch prompt

The build handoff's own closing line calls itself the spec "the build
thread executes in the post-Prototype-Testing-1 window" (written
2026-07-18) — but Mark's later decision that *"P1 launches with the full
feature set, not the minimum-viable path"* (`CiC_UX_to_Bedrock_Pilot_
Readiness_2026-07-19.md` V1.2) raises the live question of whether
Increment 1 should now merge *before* P1, so testers see the finished
brand from the start, or still wait until after per the handoff's
original sequencing. Not decided here — this thread's job was to build
it, get it reviewable, and hand the timing call back to System Hub/Mark,
exactly as the launch prompt asked. Building on a branch was safe either
way: Prototype Testing 1 has not started and hosting hasn't been stood up
(`#101/401` on the Task Board), confirmed unchanged since the launch
prompt was written.

**Next action:** System Hub/Mark reviews the six commits on
`claude/increment1-build-brand-floor`, decides the merge-timing question
above, and — separately — decides whether the found Level-2/Level-3 phone
gap needs its own follow-up thread before Increment 1 merges or can ride
with a later increment.
