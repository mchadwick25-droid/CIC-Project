# Launch prompt — Atlas Front-End Rebuild: build what's decided, stay open to going further

Paste this into a fresh thread. This thread has two jobs, not one: **build** the Atlas redesign
that's already fully decided and prototyped, and **stay open**, live with Mark, to real redesign
territory that surfaces during the work. It is not a background build-and-forget thread, and it is
not a from-scratch design thread either — it inherits a real, settled design and executes it, while
treating genuinely new gaps as live decisions to work through with Mark, not quietly improvise past.

**Before your first message, read the pacing section below — it governs how this thread runs,
including the build parts, not just the design parts.**

---

## What Mark actually asked for, verbatim

*"we have a lot of work to do on the atlas, lets build a thread that will do the work needed. full
redesign of the front-end."*

Asked to scope it — build the already-decided design, redesign from scratch, or both — he picked
**both: build it, stay open to going further.** So this thread's backbone is real, existing,
decided work (below), not a blank page — but it should not treat that backbone as the ceiling
either.

## How Mark needs this paced — read this before doing anything else

His own words, stated as a standing rule for all interaction, not just this thread: *"i get
overwelmed with desisions in context of a large about of data or pages of documentation, I want
the process... to go one issue at a time, with prompted questions and small edits at a time...
i want to see the decisions one at a time."*

- **One issue at a time.** Don't open with a full inventory of everything left to build — pick the
  single most useful starting point and propose it.
- **Build work can move faster than design work**, since most of the backbone below is already
  decided — but the moment you hit a real, undecided design question (something the 2026-07-20
  study didn't cover, or a genuine judgment call), stop and bring it to Mark as its own small
  turn, not a footnote buried in a build update.
- **Every real design choice is a recommendation plus at least one genuinely different
  alternative**, with an invitation for Mark to edit — never a single finished decision presented
  as already made.
- **Small steps, real progress shown, not everything at once.**

## What's already real — read before building or proposing anything

**The design is decided. This is the load-bearing fact for this whole thread.** On 2026-07-20, a
dedicated study (`Ministry/Features/Atlas-World-Map/Design/CiC_World_Map_Usability_Redesign_Study_2026-07-20.md`)
diagnosed exactly what Mark means by "a lot of work to do" — the live map is a promoted concept
demo with real, documented problems (69% of entries render as unlabeled 9px slivers on phone, zero
touch handlers, a four-deep nested-scroll trap) — and proposed a fix. **Mark ruled on five design
decisions the same day** (Decision-Log.md, 2026-07-20):

1. **The Story** — a vertical, scrollable era-by-era surface. Ten era-chapters, each on its own
   canonical ground color, open by default. Live worlds render as full cards (name, dates, region,
   description, **Interview**/**Add to the Table** actions) — unmissable in era context. Everything
   else renders as a compact status row; pre-survey entries sit behind a **counted, default-closed
   expander** ("+11 more this era, not yet assessed"). Tap a row for a Level-2 sheet; "Full entry"
   for Level-3 detail with sourcing and relationships. This is the **website's exploration
   surface**, and — per Mark's own decision — the landing surface on **every device**, not just
   phone; the old canvas moves behind an opt-in "View as wall chart" link.
2. **Choose a Tradition** — the **in-app selection surface**. Live-world cards first (no hunting
   through 178 entries), then census-wide search as the second element, with non-live results
   answering via the recorded grounds plus a **nearest-open-neighbor redirect** as the primary
   action. This is the **surface Increment 2 / the merge branch's `WorldSelector.tsx` work hosts.**
3. **The list view** (`world-atlas-list.html`) retires as the phone fallback and survives as the
   scholar's research browser it already functions as, linked from the Story's footer.
4. **Era-rail labels:** numeral + short era title, revealed on tap/hold.
5. **Two working prototypes exist and were verified live at phone and desktop widths:**
   `Design/CiC_World_Map_Redesign_Prototype_A_Phone_Story_2026-07-20.html` and
   `..._Prototype_B_Choose_A_Tradition_2026-07-20.html`. Read these before building anything —
   they are the design-of-record, not sketches to reinterpret.

**Also already decided and directly relevant, found and fixed in `Integration-Notes.md` this same
week:** the Tier A/B scope question (secondary-view vs. primary-selector) is **resolved** — it was
never really either/or; the Story and Choose a Tradition are two linked surfaces, neither replacing
the other. A held branch, `claude/world-map-merge-into-main` (tip `c277ca8`), has real, tested
app↔map handoff code (~40-line diff per the integration assessment, `/?worlds=<id,id>&mode=`
contract) — checked out in a **sibling directory outside this repo**,
`C:\Users\mchad\Documents\CiC-Project-worldmap-merge`, easy to forget exists. **Reconcile with
this branch, don't redo its work** — it may be behind `main` by now and need a rebase, but the
handoff contract it built is exactly what Choose a Tradition needs.

**Migration sketch, from the study's own §3.6 (not a rigid plan, a sensible order):**
1. Extract the census to one JSON asset — kills the standing "4 vs 5 live worlds" data-drift bug
   in the same motion (the count is now **6**, not 4 or 5 — Church and Empire/Marius was installed
   into `cic-poc` today, 2026-07-22; the census/prototype sample data predates this and needs
   updating).
2. Build the Story; swap it into `atlas.html`'s frame; demote the wall chart behind its opt-in link.
3. Build Choose a Tradition against the existing `/?worlds=&mode=` contract — this is the actual
   Tier A/B unblocking work, hosted where the merge branch's `WorldSelector.tsx` integration lives.

**This thread also owns IC-10**, handed off from today's separately-dispatched In-App Icons &
Graphics thread: the ten-era ground color palette (values in
`Ministry/Communication/Brand-Assets/CiC_World_Icon_and_Table_Template_Spec_V0_1.md` §7) is
approved and canonical — the Story's era-chapter backgrounds should use it directly, not
reinvent a palette. Coordinate with that thread if a genuinely icon-specific question comes up
(a Representative portrait, a new in-app graphic) — this thread owns the Atlas surfaces
themselves, that one owns the icon/graphics assets that decorate them.

## The "stay open to going further" half — real, not decorative

Mark chose this deliberately, not as a formality. When the build surfaces a real gap the
2026-07-20 study didn't cover — a screen it didn't design, an interaction it left vague, a place
where six worlds instead of four changes something structural — treat that as a genuine open
question and bring it to Mark the way the original study did: a real option, a recommendation, a
place to react. Don't silently improvise past it just because "the design is decided" elsewhere.

## How to actually run this thread

- Open by naming, briefly, what's already decided and ready to build (not a restatement of every
  section above), then propose the single first concrete step — most likely the census JSON
  extraction, since everything else depends on it and it's pure mechanical win.
- Read the two prototypes and the merge branch's actual diff before writing new code — don't
  reconstruct what already exists and works.
- **No merge to `main` or deploy without explicit confirmation** — same standing rule as every
  other build in this project ("nothing merges before/during a pilot"), and this one additionally
  touches a held branch with real prior work that needs reconciling, not overwriting.
- Log real decisions and build progress in `Ministry/Features/Atlas-World-Map/Decision-Log.md`
  (already exists, well-established — dated entries, same discipline as the rest of that file) and
  keep `Integration-Notes.md` current as the single "is this actually live" answer.
- When this thread reaches a real, deployable state, hand a summary back to System Hub
  (`Ministry/Operations/Standing/CiC_System_Hub_Decision_Log.md`) — this work sits directly on the
  critical path to hosting, which is deliberately held until content/UX work like this lands.
