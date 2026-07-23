# CiC In-App Icons & Graphics — Decision Log

Dated entries. Each records what was decided (or what's still open), the reasoning,
and the specific next action. Scope: finishing the World-Icon Representative-portrait
workstream (Marius/Church and Empire, the sixth live world), and the new,
previously-unspecced ground — the app's own in-conversation UI graphics, principally
the Living Table seated-icon scene. Dispatched from the System Hub per Mark's own
request for "a creative UX thread I can work with to design the icon and graphics
inside the program" — a live, one-decision-at-a-time creative thread, not a
background-delegated build.

---

## 2026-07-22 — Marius (Church and Empire) icon locked; IC-9 re-run across all six

**Object, source-verified against his own Permanent Prompt, not generically imagined:**
a leather-strapped scroll-case (capsa), not a single letter — his own record introduces
him as "a deacon, entrusted with carrying letters... between the great sees," and his
title is literally "Deacon of the Letters." A sealed letter was drawn and genuinely
considered as the more literal reading; Mark's call was the case, since it reads as
*the one who carries*, not just *the one who holds*. The strap runs left-waist to
right-shoulder, passing **behind** the case so the case reads as being carried in front
of it, not wrapped by it — tuned live to Mark's own correction ("extend it so it looks
like it goes around back to his shoulder, but let the arm be outside it").

**Dress:** a plain, undyed, ungirded tunic (INFERENCE, same low-risk register as
Papnoute's "attire plain, no specific garment") plus an **orarion** over the left
shoulder — DOCUMENTED for his exact 312–451 window (Council of Laodicea, canon 22,
c.363 CE, bars *subdeacons* from wearing it, implying deacons themselves distinctively
did; attested broadly East and West, so it doesn't let one see's custom stand for the
composite "we" his own record insists on holding). The dalmatic (Roman-deacon-specific,
partly legendary Sylvester attribution) was analyzed and deliberately held in reserve as
Rome-specific — not drawn.

**Robe:** oxblood `#7A2E2E`, the world's own manifest colour, reused directly as the
garment tint. Set beside the other five in a family comparison, it reads visibly
darker/more saturated than any existing robe, and the crossed orarion+strap is the only
cross-body diagonal in the family. Flagged to Mark; his call was to keep both exactly as
drawn — a quiet, unintended-but-real echo of the era's own tensions, not a flaw.

**Appearance** (skin `#D6B48A`, dark hair, clean-shaven): SILENT in the record — Marius
speaks as a composite across three sees, not one place, so no single setting grounds a
skin tone the way the other five worlds' do. Kept emblematic, INFERENCE flagged.

**Built:** `Brand-Assets/World-Icons/empire.svg` (master), `_working-base/marius_LOCKED_v1_0.svg`
(locked copy), spec §7e added to `CiC_World_Icon_and_Table_Template_Spec_V0_1.md`,
`_working-base/README.md` updated.

**IC-9 (full-family review) re-run for all six** — the 2026-07-18 run only ever covered
five. One real finding, and a correction to how it was first read: Marius's skin tone
sits almost on top of Chloe's, and his hair colour is an exact value-match with
Yausep's. First instinct was to treat this as a flaw and recommend nudging his tone to
"differentiate the spread" — **Mark corrected this directly: accuracy to the world's
actual population matters, diversity-for-its-own-sake doesn't.** Redone on regional
grounds: two of Marius's three sees (Rome, Milan) are Italian/Western Mediterranean,
and Constantinople draws from the same broad Anatolian/Greek population pool Chloe's
own Antioch/Asia Minor world does — the near-match reflects genuine shared late-antique
Mediterranean stock, not an error. Dark hair matching Yausep's is likewise the
demographic default across nearly the whole late-antique Mediterranean and Near East,
not a duplication to fix. Papnoute's genuinely darker, more sun-weathered Egyptian
tone remains the family's one real regional outlier, correctly so. Values kept exactly
as drawn.

**Also fixed in passing:** a real vertical-gap bug in the *old* ellipse-based
`Table-Templates/table-{1,2,3}-world.svg` assets — every seated figure floated ~16px
above the table's rim at every seat, even at the rim's own highest point. Patched via a
vertical shift on each seat's transform. **Superseded almost immediately** by the full
Living Table redesign below, which replaces this whole visual approach — noted here so
the fix's own history isn't lost, not because these specific files are still the ones
in use.

**Not done, still open:** IC-11 (the formal demographic-reference artifact) and IC-12
(deferred tints) — untouched this session, status unchanged from the 2026-07-18 record.

---

## 2026-07-22 (later) — The Living Table scene: redesigned live with Mark across many rounds, mockup phase closed

**The actual gap this thread closed:** `cic-poc/frontend`'s real running conversation
screen never implemented a Living Table scene at all — only a minimal text "table bar"
(colored dot + name) existed. The spec's own "FINAL" geometry (§1b, a thin wooden arc
line) was never built either; only the old, buggy ellipse-based Table-Templates asset
existed. Found by directly checking `TheTable.tsx`/`table.css`, not assumed.

**Process, per Mark's explicit ask:** a step-by-step plan — improve the mockup live
with Mark first (geometry, icon fit, phone), only then touch the real app. Built as a
standing Artifact, iterated across many rounds, each redeployed to the same link so
Mark could keep reopening one page rather than chasing new ones.

**Table geometry, DECIDED (supersedes spec §1b's thin-arc model):** a filled, roundish
oval table with a thick wood rim — Mark's direct call ("make the table look like a
roundish table... thicken the line, like a table edge"), not the spec's earlier
thin-line-behind-the-figures model. Each seat count (1/2/3) gets its own proportioned
table; the three-seat table was deliberately built bigger than the two-seat one to host
three figures with real margin, also per direct instruction.

**A real bug, only caught after building actual verification tooling:** for several
rounds, fixes to "how deep each figure sits behind the table" kept failing despite
careful hand-calculation, because this session has no screenshot/compositing capability
(Browser-pane limitation, disclosed to Mark rather than pretending confidence). Fix: a
local `npx serve` preview server + direct `getBoundingClientRect()`/`elementFromPoint()`
JS measurement, run before every publish from then on. That tooling caught the actual
root cause — the table ellipse was being drawn **behind** each figure instead of in
front of it, the exact opposite of "the table covers the lower part," wrong since round
2 and never visible without real measurement. Fixed; every subsequent round was verified
by measurement before being shown to Mark, not just asserted.

**Seat depth, generalized to a formula, not hand-tuned numbers:** center seats and outer
seats need different vertical offsets to reach the table's own curved rim (the curve is
shallower at the table's center than at its edges) — this was initially hand-tuned per
seat, then reduced to one reusable rule: `figureY = rimHeightAtThatX + fixedOverlap -
bustBottom·scale`. Verified this formula reproduces every hand-tuned value exactly.

**Pivotal design change, Mark's own direct call, a real departure from the icon spec:**
every Representative's held object (cup, jug, scroll, book, tablet, scroll-case) was
moved **off the figure's body and onto the table surface** in front of them, base
resting on the rim — not cradled at the chest as icon spec §7a currently states and as
all six locked master icons are actually drawn. Flagged explicitly as a real reversal of
a decided rule, not just a mockup tweak, since it affects how the master icon files
themselves are built, not only this scene. Required per-icon tuning: three icons
(Chloe's cup, Papnoute's jug, Theon's scroll) sit flush or almost flush against the same
flat seating edge as the body and needed lifting to avoid being swallowed by the table;
three (Yausep's book, Albina's tablet, Marius's case) have a few units of natural
clearance and needed none.

**A second real implementation bug, also only caught by direct measurement:** the
nameplate's light/dark "resting/speaking" states were being individually hand-painted
per instance (six different hardcoded inline styles) rather than driven by one real
toggleable class — confirmed by checking `classList`/`getAttribute('class')` directly,
not assumed from how it looked. Fixed to a genuine `.nameplate`/`.nameplate--speaking`
class pair. **Mark's follow-up call: every nameplate defaults to the resting/white
state** — the speaking/dark state is only for whoever is actually talking, never
baked into a "natural state" view of the table.

**Phone built:** the corner speaker-chip mechanic (the speaking Representative's own
icon, or a plain table glyph when the Facilitator/participant has the floor, swapping
per turn) and the one-time load-greeting screen (full scene once, welcome text, a
bottom-anchored Begin button) — both first passes, not held to the same rigor as
desktop yet.

**Also added, per direct request:** each Representative's world name and date range
shown alongside their name in the mock transcripts, sized up ~2pt for legibility.
Dates used were drawn from spec-document text at the time and turned out to differ
slightly from the backend's own authoritative `world_manifest.py` period strings —
caught and corrected in the real sort fix below, **not yet corrected back in the
mockup's own illustrative transcripts** (cosmetic-only gap, flagged not fixed).

**Closed, this phase:** all five of the plan's own steps (settle geometry, build the
three-seat-count scenes, tune desktop live, build phone, check scene-plus-transcript
together) marked done in the mockup's own tracker. Phase 2 — building this for real —
begins in the next entry.

---

## 2026-07-22 (later still) — Phase 2: Living Table built into the real `cic-poc` app

**New:** `src/data/worldIcons.tsx` — all six Representatives' body + held-object SVG
path data, keyed by each world's real `world_id` (confirmed against
`world_manifest.py`, not guessed). `src/components/LivingTableScene.tsx` — renders the
table + seated figures + rested objects + nameplates for 1/2/3 seats, computing seat
depth and object placement from the ellipse geometry (the formula above) rather than
hardcoding per-world/per-seat numbers, so it isn't tied to these six specific worlds or
these specific seat arrangements. `src/components/BrandMark.tsx` — the static
ring-and-seat mark alone (no wordmark, no replay animation), for slim-chrome reuse.

**Wired into `TheTable.tsx`:** `LivingTableScene` now renders in both the active and
closing conversation views. `speakingKey` (who currently has the floor, for nameplate
inversion) is derived from real message-stream state — a Representative's message
mid-stream counts as speaking, the Facilitator/participant/idle states all clear it to
null — reusing the exact name-normalizing convention (`message.name.toLowerCase()
.replace(' ', '_')`) already used elsewhere in the same file for lexicon lookups, not
new logic invented for this.

**Table bar simplified, per Mark's direct answer** ("just the logo is fine") to the one
open question from the plan: the old colored-dot/world-name/rep-name list
(`.table-bar__seats` and children) removed outright — confirmed unused anywhere else in
the codebase first — replaced with just the static `BrandMark`, since the seated scene
now carries "who's here" visually.

**`table.css`:** two new tokens (`--color-tabletop`, `--color-wood` — nothing existing
covered this pair), `.living-table-scene`, `.nameplate`/`.nameplate--speaking` (ported
directly from the verified mockup values).

**Verified how, given the backend's slow/unclear startup this session:** `tsc --noEmit`
clean (one real type error found and fixed along the way — a `foreignObject`-wrapped
`<div>`'s `xmlns` prop, unneeded in React, dropped); no console errors on the running
dev server; every seat-geometry formula hand-checked to reproduce the mockup's own
tuned numbers exactly (e.g., the three-seat outer-seat offset comes out to 9.4, not an
approximation). **Not yet done:** an actual live look at the seated scene inside a real
running conversation — the backend was wrongly reported as non-responsive mid-session
(it was just slow to finish loading, confirmed responding on a later check) and this
live check hadn't been re-run as of this entry.

---

## 2026-07-22 (later still) — World-selector tiles: real ordering bug found and fixed

**Found while working the dates above, not the original ask:** `WorldSelector.tsx`
rendered worlds in whatever order the backend's `/api/worlds` response happened to
return them — no sort at all. **Mark's direct instruction: order by each world's own
start date.**

**Fixed:** a `startYear(period)` helper extracts the leading number from each world's
own `period` display string (works for both "70–200 CE" and "c. 312–451 CE" — no
separate sortable field needed on the manifest), and `WorldSelector` sorts on it once
when the world list arrives.

**Verified against the real six worlds' own `world_manifest.py` period strings** (not
the approximated dates used in the Living Table mockup's transcripts above): House-
Churches (70) → Alexandria (150) → Syriac (200) → Church and Empire (312) → Desert
(320) → Bethlehem Circle (382). Two corrections to what had been assumed earlier this
session: Alexandria/Theon actually starts earlier than guessed, and Church and Empire
starts slightly *before* the Desert, not after.

---

## 2026-07-22 (cross-reference from System Hub) — Object placement: DECIDED as two states, resolving the §7a conflict

**Mark told System Hub directly**, which is why this entry is recorded from there
rather than live in this thread: *"we should have two states, when isolated the item
is on the chest, when at the table the item is on the table."*

**This resolves, not just defers, the flagged conflict above** between icon spec §7a
("cradled at the chest," how all six locked master icons are drawn) and the Living
Table's own "resting on the table" decision. Both are correct — they're not competing
rules, they're two different contexts: **isolated** (a standalone icon — the master
files as they exist today, wherever a single Representative's portrait appears without
the table itself present, e.g. the world-selector tiles) keeps the object at the chest,
unchanged. **At the table** (the Living Table scene itself, 1/2/3 seats) keeps the
object resting on the table surface, per the already-built implementation — no change
needed there either.

**Not yet done:** writing this two-state rule into `CiC_World_Icon_and_Table_Template_Spec_V0_1.md`
§7a itself, so the spec stops reading as contradicted by the shipped scene. Whoever
resumes this thread should close that — it's a documentation update, not new design
work, since both states already exist and match this ruling as built.

**Also from System Hub, same message:** the live-in-app visual check of the built
scene is deliberately not happening today — Mark's own words, *"we will work on the
integrating the scene in the real running conversation tomorrow."* Not a blocker, a
schedule call.

**Next action:** when this thread resumes tomorrow — (1) the live-in-app check, per
Mark's own stated plan, (2) the spec §7a write-up for the two-state rule, a short
addition, not a redesign.

---

## Status and next actions

**Closed this session:** Marius's icon and the six-icon IC-9 review; the Living Table
mockup's full design phase (desktop + phone, both approved); the first real
implementation slice in `cic-poc` (`LivingTableScene`, `worldIcons` data, `TheTable.tsx`
wiring, table-bar simplification, `table.css`); the world-tile ordering bug; the
isolated-vs-table two-state object-placement rule (System Hub cross-reference above).

**Open, not started or not finished:**
- A live, in-conversation visual check of the real `LivingTableScene` build — deferred
  to tomorrow, per Mark's own direct instruction (not a blocker today).
- The mockup's own illustrative transcript dates don't match the real backend period
  strings for Alexandria/Church and Empire/Desert — cosmetic, not urgent.
- IC-11 (demographic-reference artifact) and IC-12 (deferred tints) — untouched.
- The icon spec's §7a needs the two-state (isolated/at-table) rule written in —
  decided, just not yet documented in the spec itself.
- Phone's load-greeting screen and corner-chip mechanic are first passes only, not yet
  wired into the real app (mockup only).
