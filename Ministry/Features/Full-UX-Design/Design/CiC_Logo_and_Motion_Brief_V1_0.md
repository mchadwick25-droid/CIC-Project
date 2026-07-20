# Logo & Motion Brief — V1.0

**Date:** 2026-07-17 · **From:** the branding workstream (all decisions
Mark-confirmed this date) · **To:** the Front-End Graphics thread (refinement and
execution) and the landing-page/UX thread (implementation). **This brief is the
single source for the mark; the Brand Foundations (Brief + Kit) govern everything
around it.**

---

## 1. The decided mark — "Arriving"

Concept 2, Variation 1, chosen through four rounds of exploration and a
four-persona market simulation (`Ministry/Communication/` — Concepts V0.1, C-Table
Variations V0.3, Market Simulation, Motion Study).

**Geometry (working values; refinement is your mandate, meaning is not):**
- A single open ring stroke — the C-as-table — circle r = 31 on a 100-unit
  viewBox, stroke-width 11, opening facing right, gap edges at ±40°, rounded
  terminals (but see R4).
- One dot, r = 6, at (89, 50) — outside the open mouth, at the threshold. The dot
  never sits inside the ring in any static or animated state.
- Ink on parchment; the dot in madder. Never any third element. Never a cross, a
  dove, a flame, a speech bubble, or anything tech-flavored.

**The meaning (public form, said once, never elaborated in donor material):**
*"The mark is a table; the opening is the way in — and it never closes."*
Internal rationale bank (never public copy): the dot is the participant, free to
stay outside; the open circle as the structural opposite of the altar call; the
Hospitality of Abraham's open table-side; rubrication — the red mark beside black
text is where reading begins; the lunate sigma echo.

## 2. Refinement mandate (from the market simulation — R1–R7)

1. **Widen the opening** past ±40° and test — "mouths are narrow, doorways are
   wide." Kills the Pac-Man first-read at small sizes.
2. **Tune the dot** (size / distance / slight vertical offset) until it reads
   "threshold, not pellet," at every size. Personas split on direction — resolve
   empirically at 16/24/48 px.
3. **The madder stays muted.** Lock the value; if it brightens toward alert-red it
   becomes a notification badge. (Palette: parchment / iron-gall near-black /
   madder / gold-leaf ochre — Kit Part 3.)
4. **Interrogate the rounded terminals:** a slight calligraphic modulation — pen
   logic, not fake brushwork — moves the mark from "app icon" toward "letterform"
   and strengthens the manuscript claim the palette makes.
5. **Formal favicon test** at 16/24/32 px before anything ships.
6. **The wordmark face:** a genuine old-style serif, deliberately chosen — the
   wordmark carries more identity than the mark in most contexts. Never a
   geometric sans. Lockup: masterbrand always present; series titles
   ("Conversations with the Early Church") only ever beneath it, subordinate.
7. **Check the period-app adjacency** (cream ground + lone red dot) in final
   lockup contexts; R1/R2 largely resolve it.

**Also:** trademark screening covers the mark, not just the name (already on the
nonprofit thread's attorney list). Simulation ≠ clearance.

## 3. The motion — FINAL (V0.8, Mark: "this is it")

**The sequence — alone · built · seated · breathing — once per page arrival, then
permanent stillness:**
1. **The red dot, alone** (~0.8s). First frame: the dot standing (slightly high),
   empty parchment, *nothing else* — mind the rendering trap: a zero-length
   rounded-cap stroke draws a phantom dot; hold the ring at opacity 0 until the
   draw begins.
2. **The C is drawn in one stroke** (~1.3s): beginning at the **lower lip** of the
   opening, sweeping around bottom → far side → top, finishing at the **upper
   lip** — the last thing completed is the doorway, beside the guest. Single-ended
   only: symmetric both-ends growth reads as a body enveloping the guest
   (rejected, Mark).
3. **The dot sits** (~0.6s): drops the small standing offset with a weighted
   settle (slight cushion-squash, then rest).
4. **The breath:** opacity-only, candle-slow (5.5s cycle, 1 → ~0.76), begins only
   after the sit.

**Reference implementation:** the working pure-CSS source is
`Ministry/Communication/CiC_Logo_Motion_Study_V0_1.html` (V0.8 content) — one SVG,
`stroke-dasharray` on a `pathLength="360"` circle, keyframes as speced. Lift it.

**The story it tells (canonical, Mark's):** first there is only you; the program
builds its table of churches because someone came; you sit; the conversation is
alive.

## 4. The motion grammar (binding)

- **One motion, once.** The sequence plays once per page arrival; nothing else in
  the identity moves. Never replays unbidden.
- **You, first.** The sequence opens on the guest alone.
- **Single-stroke build,** lower lip to upper lip; the doorway completes last.
- **Sitting is presence;** breath begins only after the sit.
- **The dot's covenant:** the dot may wait, sit, breathe, and leave. It **never
  enters the circle**, and nothing ever pulls it. No animation may play the
  joining at a visitor ("you've made an altar call out of the thing that was
  precious because it wasn't one").
- **The opening is constant:** the mark does not react to the cursor; no
  interaction widens or narrows it (anything that can open can be felt to close).
- **Never:** spin (spinner), bounce, pulse at alert speed, move to attract a
  click.
- **`prefers-reduced-motion` is a full experience:** the completed still mark —
  table built, guest seated.

## 5. Deliverables checklist (Front-End Graphics)

- [ ] Refined vector mark (R1–R7 applied), light + dark
- [ ] Favicon/app-icon set (16/24/32/48/180/512), tested
- [ ] Wordmark in the chosen old-style serif; masterbrand and series lockups
- [ ] Palette spec with locked values (incl. the muted madder)
- [ ] Motion implementation from the reference CSS (landing thread consumes)
- [ ] One-page usage sheet: clearspace, minimum sizes, the never-list, the
      one-sentence public meaning

*Everything here is Mark-decided as of 2026-07-17; refine the drawing, not the
decisions. Questions of record → `CiC_Messaging_Branding_Kit_Decision_Log.md`;
questions of intent → Mark.*
