# Launch prompt — Atlas / Scrolling Map v3

Paste this into a fresh thread. **Select Fable as the model before sending** — this is
the next large Fable project, per Mark's own direct call.

**Scope note, read this before proposing anything:** this is not a from-scratch design.
The landscape data model this ask describes — every identified Christian tradition
across all ten eras, not just the traditions CiC will build — **already exists and is
already live.** This thread's job is to read what's real first, then decide what "v3"
actually needs to change, rather than re-designing something that's already built.

---

## The ask, stated exactly as given

Mark's own words, 2026-08-01: *"the next large fable project will be to fully update the
information, structure and visuals of the atlas/scrolling map of all 10 eras and every
world with hover and click on every identified Christian Tradition over the last 2000
years, not just the ones we will eventually build."*

## What already exists — read every one of these before proposing anything

- **The census.** `cic-website/data/world-census.json` (built from
  `CiC_World_Atlas_Census_V0_13.xlsx`) has **178 entries across all 10 confirmed eras**.
  Only 9 are actual/prospective CiC-built worlds (6 live, 3 selected-not-built) — the
  other **169 are the full landscape survey**: named, dated, region-tagged, lane-assigned,
  sourced, with stated relations and honest exclusion grounds, deliberately including
  movements CiC will likely never build (Marcion, Gnostic currents, LDS, Christian
  Science, and more, each with a real research brief, not a placeholder). Per-era counts:
  11 / 15 / 12 / 14 / 16 / 13 / 21 / 17 / 27 / 32 (Eras 1–10). **The core ask — "every
  identified Christian tradition, not just the ones we'll build" — is already the design
  this data model was built to.** Confirm this for yourself against the file before
  assuming otherwise.
- **The narrative spine.** `Ministry/Features/Atlas-World-Map/Design/
  CiC_World_Atlas_PreStep0_Survey_V0_1.md` (1,756 lines) — the researched prose behind
  every census entry, explicitly *not* a formal Step 0 run (only Era 1–2 has a real Step 0
  disposition; the rest is pre-survey signal, sourcing/ecology/floor notes framed as
  questions, never verdicts). Includes the **Wet Ink Horizon** (six still-forming Era 10
  currents — Lausanne-era evangelicalism, Emerging Church, Dispensational Prophecy
  Culture, Megachurch/Seeker, Deconstruction communities, Narrative-Kingdom Renewal —
  rendered as overlapping "overlay current" bands, not settled territories).
- **The 10 eras, confirmed and canonical.** Era 1 (The Early Church, 70–312) through Era
  10 (The Global Church, 1906–present) — full table with dates in
  `Ministry/Features/Atlas-World-Map/Design/CiC_World_Orientation_Map_Spec_V0_1.md`
  Amendment E. **The era-ground color palette is not this thread's to redefine** — it's
  canonical in `Ministry/Communication/Brand-Assets/
  CiC_World_Icon_and_Table_Template_Spec_V0_1.md` §"Era-ground values" (light + dark,
  ten values, warm-past→cool-present), this thread renders with it.
- **The live site.** `cic-website/world-atlas.html` (Wall Chart + Research Table,
  toggled by URL hash) and `cic-website/atlas.html`/`index.html` (the vertical Story
  scroll) are both live at churchinconversation.com, both already reading the full
  178-entry census, both **already hover- and click-interactive on every entry** — hover
  surfaces a glimpse/relationship edge on the Wall Chart, click opens a full panel
  (sourcing, floor note, relations, and for live worlds a real launch link into
  `cic-poc.onrender.com`). Open the actual site before assuming interaction needs to be
  built from zero — it doesn't. What's genuinely open is **quality, depth, and visual
  craft** of that interaction, not its existence.
- **Three prior redesign prototypes**, from a 2026-07-20 Fable usability study:
  **A** (Story/phone scroll — shipped, became the live vertical view), **B** (search-first
  "Choose a Tradition" selector — designed, not built into the app), and **C** (a unified
  grid-timeline exploration — **built but never reviewed. No Decision-Log entry exists
  for it anywhere; Mark has never seen or ruled on it.** Read it
  (`Design/CiC_World_Map_Redesign_Prototype_C_Unified_Grid_Timeline_2026-07-23.html`)
  before treating A/B as the only two directions on record.
- **IC-10 — approved, not yet built.** The 10-era ground palette above was approved
  2026-07-18. The live atlas still renders on a single uniform ground, not the per-era
  palette. This is a real, standing, unbuilt Task Board item — folding it into v3 rather
  than treating it separately is very likely the right call, but say so explicitly rather
  than silently absorbing it.
- **Governing texts from the original v1 launch** (still load-bearing, re-read them, don't
  take this summary's word alone): `Ministry/Communication/Vision, Mission, Convictions,
  and Foundational Commitments V1.1.docx` — Conviction 1 (no single movement exhausts the
  richness of Christ; the map makes that testimony visible, not just a picker) and
  Conviction 4 (authentic encounter requires trustworthy transparency) are the whole
  reason this shows movements CiC hasn't built, honestly, rather than only what's ready to
  sell. `L1-Foundation/CiC_L1_Constitution_V2_2.docx` Article 6 (Encounter-Success
  Standard) applies to the map's own honesty about what a participant will and won't find.

## A real, uncorrected inaccuracy in the standing files, now fixed — read so you don't repeat it

The Task Board carried a 2026-07-30 correction claiming this thread's Decision Log "ends
on five open questions blocking V0.2" and that no construction/census expansion should
happen until Mark answers them. **That's stale — those five questions were asked and
answered the same day, 2026-07-16**, several passes later in the same session (see
`Ministry/Features/Atlas-World-Map/Decision-Log.md`, which reads newest-first; the
questions sit at the file's oldest entry). Whoever wrote that correction read only the
log's last entry by file position and mistook it for current state. Corrected on the
Task Board 2026-08-01 — mentioned here so this thread doesn't waste a pass re-litigating
five questions that were closed two weeks ago.

## What v3 actually needs to decide and build, given all of the above

Since the landscape data model already satisfies "every identified tradition, all 10
eras, not just buildable worlds," the real work is not re-designing that model from
scratch. It is, in rough priority order:

1. **A verdict on visual/interaction quality.** Mark's own words, logged 2026-07-30:
   *"rebuild... to the v3 specifications with further input... last two versions were
   still messy."* Figure out concretely what "messy" means against the live site as it
   actually renders today — crowding, legibility, the era-ground palette's absence,
   something else — before proposing a rebuild. Don't assume; look, then ask if it's still
   unclear.
2. **A real evaluation of Prototype C**, alongside A (already shipped) and B (designed,
   unbuilt) — is its unified-grid direction a genuine v3 candidate, a dead end, or
   something to merge ideas from? This has never been decided by anyone.
3. **Resolve the "Choose a Tradition" name collision.** That exact phrase already labels
   the plain tile-grid heading in the live `cic-poc` app today — a different, simpler
   thing from Prototype B's redesigned search-first surface, which shares the name. Any
   v3 proposal touching this needs to disambiguate explicitly, not compound the collision.
4. **Decide scope: Tier A (the public website Atlas) only, or Tier B (the in-app
   world-selection surface) too.** Mark's ask describes an "atlas/scrolling map" — closest
   to Tier A, which already exists and is live. Tier B (the in-app selector) has **no
   Gantt task at all**, unlike Tier A's Increment 4 merge (already scheduled) — building it
   would be new roadmap territory, not finishing an existing branch. Recommend defaulting
   to Tier A as this pass's scope and naming Tier B as a real, separate, larger future ask
   — but confirm with Mark rather than assuming either way if genuinely unclear from his
   framing.
5. **A fresh completeness/rigor check against the full 178, not the old 147.** The only
   external rigor check ever run against this census
   (`Design/CiC_World_Atlas_External_Review_V0_1.md`) was against **Census V0.2, 147
   entries** — not the current 178. If "every identified Christian tradition" is meant as
   a hard, checked claim rather than a reasonable-effort one, that's worth a real second
   pass (Cambridge History of Christianity, Noll, González, Latourette, MacCulloch, the
   World Christian Encyclopedia — same sources as the first review) before calling the
   coverage claim settled at the current count.
6. **Apply the approved era-ground palette (IC-10)** to the live atlas — folding this
   long-standing, already-approved, unbuilt item into v3 rather than a separate pass.

## What to produce

A real design document plus, where the scope decision above lands on visual/build work,
an actual implementation — not just a proposal, since Tier A is a website (`cic-website/`)
this project already ships directly, not a gated `cic-poc` release. Use this project's
own `[M]`/`[E]`/`[S]` tagging discipline (measured / estimated / speculative) for any
completeness or quality claim. End with a clear, explicit list of what's decided and
built versus what still needs Mark's own call.

## Coordination boundary

- This thread can touch `cic-website/` directly (the same standing latitude the 2026-07-22
  Atlas Front-End Rebuild thread had) if the scope decision above lands on Tier A.
- **Does not** touch `cic-poc/` frontend or backend code unless the scope decision above
  explicitly, with Mark's confirmation, extends to Tier B — that's new roadmap territory,
  not this pass's default.
- Does not make Source Ecology or Gravity Discovery determinations informally for any
  movement's build-status field — those come from the actual Construction Framework
  methodology (see `anthropic-skills:cic-gravity-index`), not a guess made for map
  content's sake.

## Logging

Log real decisions and open questions in this thread's own
`Ministry/Features/Atlas-World-Map/Decision-Log.md`, same dated-entry discipline already
in use there — newest entry on top, don't let a real decision live only in chat history.
When this pass reaches a real stopping point, report back to System Hub with what's
sync-ready for the Task Board, Decision Log, Gantt, and Dashboard — this thread does not
edit those Standing files itself.
