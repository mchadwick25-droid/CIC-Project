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

## 2026-07-23 — Direction pivot: from the flat icon-family to AI-assisted realistic portraiture (Albina test case)

**Mark's own call, direct:** the flat SVG icon system — complete, locked, IC-9 passed
across all six — "makes the system still feel hokey," a real aesthetic judgment, not a
build defect. Rather than iterating further on the flat-icon language, decided to
explore a genuinely different visual direction: realistic, AI-generated portraiture in
the vein of a documented living actor voicing a historical role (Mark's own analogy:
"an actor in williamsburg va is a real person that speaks for a larger world") — full
historical research into period-accurate dress/hairstyle/ethnicity/held-object per
Representative first, an AI image prompt built from that research second, same
anti-fabrication discipline as every other artifact in this project, not free invention.

Chose **Albina** (Bethlehem Circle / `hal` world, the *vidua* widow, a non-documented
composite figure per her own Construction Notes) as the test case before committing the
process to all six.

**Iterative rounds, each a real correction, not polish:**
- Round 1: frontal portrait — expression too stern for someone "sitting at a table in
  dialogue" (Mark's own read); ethnicity read as ambiguous, not confidently
  Mediterranean/Levantine.
- Round 2: a seated-at-table image introduced unrequested props (oil lamps, wine,
  herbs) — flagged as prop drift, nothing in this world's own record grounds those
  objects — and a ring, a real accuracy miss for an ascetic widow. Expression and
  ethnicity both improved this round.
- Round 3: an isolated portrait, built to sit at the app's own table rather than live
  inside a picture-within-a-picture, introduced her established object (wax tablet +
  stylus, tied to the household-scriptorium involvement her role is actually built on)
  — but held at the chest in a single consolidated image. **A real regression, caught
  by Mark:** the object was meant to be its own separate generated asset (so it could
  rest on the Living Table's surface, not be locked to one held pose), and had drifted
  back into a combined held-object image. Corrected by re-splitting into two prompts:
  an empty-handed portrait, and a standalone tablet-and-stylus object.
- Object shape corrected via research: the tablet is a thin, cord-hinged wooden
  diptych, not the book-like leather-bound object first generated; the stylus is metal,
  not the quill/pen first implied. Both corrected in the regenerated object asset.
- The table-surface asset went through its own three rounds — first too zoomed-in and
  cropped from the wrong edge (the near rim, not the far rim fading out "after a
  third," per Mark's own framing, to leave room for the welcome/conversation UI);
  second attempt fixed the framing; third (a softly-blurred wood-grain surface) was
  Mark's approval: "this is it."

**Tooling question resolved, deliberately narrow:** Mark considered building the three
validated assets (portrait, object, table) into a vector-art program so they could
later be animated, then reconsidered directly: *"that is too complicated at this
point, we just need it to look great."* Vector-readiness for hypothetical future
animation is shelved, not decided against permanently. Raster tools (Canva) are the
standing plan for compositing — explicitly not auto-tracing.

**Cross-reference:** the flat-icon Living Table build in `cic-poc`
(`LivingTableScene.tsx`, `worldIcons.tsx`) had its graphics pulled from the live
conversation view the same day, per Mark's direct call that the old icons "detract from
the conversation" while these new assets are worked out — full account in the System
Hub Decision Log, 2026-07-23 (later). Nothing built was deleted; this thread's own
component work is preserved for whenever the new portraits are ready to seat.

**Status at day's end:** three validated raster assets for Albina (portrait, object,
table surface), not yet composited together — the "real test" of whether this
direction reads correctly in the actual seated-at-table context remained open.

---

## 2026-07-24 — Style locked: painterly/fine-art, not photorealistic; Albina's profile portrait approved as the template for the remaining five

**New context, same thread:** Mark signed up for a 14-day Gemini trial specifically to
keep working this process (a free-tier request limit had been the prior blocker).
Alternatives (ChatGPT/GPT-image, Midjourney) were weighed directly — decided to stay on
Gemini rather than switch mid-process.

**A real capability confirmed, not assumed:** Gemini's image generation accepts
multiple images as input alongside a text prompt and can combine them into one new
scene — directly relevant to Mark's stated plan to build each Representative's portrait
individually, then later feed validated portraits (plus the already-approved table
surface) back in together to generate a genuine multi-seat group scene, rather than
manually layering separate images. Flagged honestly: likeness consistency across that
recombination isn't perfect and should expect its own verification/iteration pass, same
as every other asset in this process.

**Three intended uses for these portraits, Mark's own framing, now on record:**
1. The profile/description card for each Representative.
2. Seated at the top of the conversation page (the Living Table scene, once rebuilt
   with these assets).
3. General website photostock. **Not yet resolved:** whether #3 means further images
   of these same six named Representatives, or broader, non-identity-specific
   historical/environmental stock imagery for the site — open question for whoever
   picks this up next.

**Style decision — a real pivot from the "photorealistic actor" framing that started
this whole direction:** the round Mark called "the best profile" (tablet-and-stylus
held at the chest, matching the standing isolated-portrait two-state rule) reads as a
fine-art oil portrait — visible canvas texture, cracquelure — not a photographic
image. Mark's own reasoning, direct: *"i like this because it has all the character we
are looking for but it also isn't to realistic or modern."* **This is now the locked
visual standard for the remaining five Representatives**, superseding the earlier
"real actor"/photorealistic framing as the actual target look once seen in practice. A
small sparkle/star mark visible in the corner of the shared image was confirmed by
Mark as a UI artifact from wherever the image was viewed, not part of the generated
image itself — no correction needed.

**Disposition:** Albina's profile-use portrait **approved as-is.** This thread moves to
the next Representative using this same style — painterly, warm/in-dialogue
expression, no jewelry, historically-grounded held object, isolated-portrait
chest-hold — as the template to match, not a fresh design exploration each time.

---

## 2026-07-24 (later) — Theon's profile portrait built and approved; two real corrections along the way

**Grounding first, same discipline:** Theon (Alexandria's catechetical *didaskalos*,
c. 150-400 CE) is a fully invented composite voicing the whole school-tradition as
"we," not a specific historical person — his appearance is silent/emblematic in the
world's own documents, same category as Marius and Albina. The already-locked flat
icon's choices (medium-Mediterranean skin, short grey hair fringe, clean-shaven, plain
white robe + himation, an opened scroll) were the only prior appearance decisions on
record, flagged there as provisional.

**Correction 1 — ethnicity, a defensible-diversity call, not a fix:** Alexandria was
documented as genuinely tripartite (Greek/Egyptian/Jewish); even named historical
figures tied to the real Catechetical School (Origen especially) are contested on
ethnic background in real scholarship, not settled Greek. Mark's direct instruction:
lean into that real plurality rather than defaulting to the safer, more conventional
Hellenized-leaning tone the first pass produced — recorded as a standing rule, see
memory `feedback-defensible-diversity-in-ethnicity`. **A real technique catch along
the way:** the first regeneration attempt just swapped a skin-tone adjective on an
otherwise-identical prompt, which kept the same underlying face and only recolored it
— Mark caught this directly ("if he is really a different ethnicity we need to create
that ethnicity"). Fixed by generating a genuinely fresh, independent image grounded in
real regional evidence (the Fayum mummy portrait corpus — legitimately usable here,
unlike the earlier wrong-region Fayum idea considered for Albina).

**Correction 2 — hairstyle, an anachronism catch:** the locked icon's "short grey hair
fringe" rendered as a modern side-part/comb-over. Verified against real portrait
sculpture: Roman-era men's hair (Antonine through Tetrarchic/Constantinian, 150-400 CE)
never shows a defined side part — that's a 19th-20th century Western barbering
convention; period styling ran either short-and-curled-forward (earlier end) or very
short and close-cropped/unparted (later end, matching this school's most active
Severan-era window). Fixed to short, close-cropped, no part.

**Expression and background brought in line with Albina's now-locked family register:**
an early pass showed him mid-speech (open mouth, pointing) against a visibly
brushstroked background — both corrected (closed warm smile, flat/plain background) so
the two portraits read as one consistent set rather than two different styles.

**Disposition:** Theon's profile portrait **approved.** Standalone scroll-object asset
(for the table-scene two-state rule) not yet built.

---

## 2026-07-24 (later still) — Chloe's profile portrait built and approved; a real cross-world contamination caught

**Grounding first:** Chloe (House-Churches, World #1, c. 70-200 CE) is DOCUMENTED as a
household leader/patroness hosting a fellowship gathering in her own home — the name
itself is grounded in common Anatolian/Lydian inscriptional attestation, not (per the
Representative Identity Decision specifically) the 1 Cor 1:11 "Chloe's household"
reference, though a separate icon-thread document does cite that verse — an
unreconciled inconsistency between the project's own two document tracks, noted, not
smoothed over. Core regions Antioch/Syria and western Asia Minor, not Corinth. Her cup
(the agape/eucharistic meal) is a direct project-lead decision, well-grounded in this
world's central gravity.

**Correction 1 — veil styling, an anachronism catch:** the first portrait rendered a
snug, face-hugging wrap — verified against period sculpture (the Pudicitia and "Large
Herculaneum Woman" statue types) to be a **wimple**, a Western European convention
centuries later (7th-10th c.+) and a different region. Real Greco-Roman practice was a
himation pulled up loosely from the shoulder, falling in soft voluminous folds, with a
thin line of hair visible at the hairline — not bound to the skull. Fixed accordingly.

**Correction 2 — a real cross-Representative contamination, caught by Mark directly:**
the first prompt described her dress as "undyed linen," carried over without
re-checking whether that was actually right for *this* Representative specifically.
Mark's own question named the risk precisely: is this "a leftover from the Bethlehem
[Albina] image"? Research confirmed it was exactly that kind of unexamined carry-over
— undyed cloth is a poverty/mourning/ascetic-renunciation code (Albina's Hieronymian
world's own real theme), not a marker fitting a homeowner with the means to host a
gathering. Actual comfortable-but-modest women in this era wore affordably-dyed cloth
(muted madder-red, soft ochre/saffron) — the biblical "no expensive clothes" warnings
(1 Tim 2:9) target ostentatious luxury specifically, not color itself. Fixed to a
muted madder/ochre palette with the chiton showing as a visually distinct layer (a
shoulder pin, a different tone) beneath the himation — notably, the original locked
flat icon had already gotten half of this right (an ochre himation) and only the base
chiton was mistakenly left undyed in translation to the realistic portrait.
**Standing caution for the remaining Representatives:** dress/status details from one
world's own theme (renunciation, austerity, wealth, etc.) must not default onto
another world's figure just because both are broadly "early Christian" — re-derive
status-appropriate dress per Representative, don't inherit it visually.

**Also checked and closed, not found:** whether this world's own documents narrow its
c. 70-200 CE span the way Bethlehem Circle's do (a documented late-period
concentration) — confirmed no such narrowing exists here; the world's own evidence is
explicitly "geographically and temporally scattered," so Chloe is accurately meant to
speak across the whole span, not one pinned moment.

**Disposition:** Chloe's profile portrait **approved.** Standalone cup-object asset not
yet built.

---

## 2026-07-24 (later still) — The appearance-research process formalized as an explicit three-step order; applied to Marius's profile portrait

**Mark's own explicit ordering, now the standing process for every remaining
Representative's appearance:** (1) the world's own original/documented sources first;
(2) time-bound and geography-bound external historical sources second, once the
internal record is exhausted; (3) only then, lean into diversity the sources
themselves actually support — never a starting assumption. Saved as durable guidance
(memory `feedback-defensible-diversity-in-ethnicity`, restructured around this
ordering) so it governs the remaining Representatives without needing to be repeated.

**Applied live to Marius (Church and Empire, "Deacon of the Letters," c. 312-451 CE):**
- Step 1: his own record already established (2026-07-22 IC-9 entry) — orarion,
  scroll-case, oxblood robe DOCUMENTED; personal appearance silent/emblematic.
- Step 2: fresh research (not leaning on the earlier IC-9 shorthand) into Rome's,
  Milan's, and Constantinople's actual documented populations across his exact span.
  Rome: genuinely Eastern-Mediterranean-inflected even by this point (ancient-DNA
  study, Antonio et al., *Science* 2019). Milan: no documented ethnic distinction from
  Rome. Constantinople (from 330 CE): the best-documented of the three — a
  deliberately, state-engineered cosmopolitan population drawn from Anatolia,
  Thrace/the Balkans, and Syria (Dagron's standard study of exactly this period).
- Step 3: an Anatolian/Aegean Greek reading is a genuinely well-grounded,
  non-default option — reinforced by a striking real echo: the *apocrisiarius*,
  Rome's actual liaison at Constantinople, is first attested as a bishop of Cos
  serving Pope Leo I in the 440s, right at the close of Marius's own span. **Mark's
  call: lean into it.**

**Also verified before assuming (the Chloe lesson, checked rather than repeated):**
whether "plain undyed under-tunic" (the standing INFERENCE beneath his already-dyed
oxblood robe) risked the same poverty-coding mistake — it doesn't. No distinct
clerical dress existed yet in this era (clergy wore ordinary Roman dress of their
class); Jerome's own letter to a deacon (Ep. 52, c. 394) explicitly warns against
deliberately shabby dress as its own form of vanity. An undyed base layer under an
already-dyed outer robe is ordinary, not renunciation-coded — no change needed.

**Hairstyle applied proactively, not caught after the fact this time:** the same
Roman imperial-portraiture hair conventions researched for Theon (no side part ever
attested for Roman men this era; short-and-curled-forward or short-and-cropped
depending on sub-period) apply equally here, since Marius's span sits at the later,
close-cropped end of that same cycle — built correctly into the first prompt instead
of needing a correction round.

**Disposition:** Marius's profile portrait **approved**, first attempt, no correction
rounds needed — the accumulated standing checks (fresh-face generation, region-matched
face grounding, period-correct hair, status-appropriate dress, the three-step
appearance process) held up cleanly applied from the start. **Four of six
Representatives now have approved profile portraits:** Albina, Theon, Chloe, Marius.
Standalone table-ready object asset (the scroll-case) not yet built.

---

## 2026-07-24 (later still) — Yausep's profile portrait built and approved; the icon's own dress explicitly overridden, not carried forward

**Grounding first:** Yausep (Syriac world, a Malpana teacher of the qyama order, c.
200-410 CE, spanning Roman Osroene/Edessa and Sasanian Adiabene) is fully invented,
speaking collectively as "we" like Theon. His held object is DOCUMENTED and
identity-constitutive: the *Diatessaron*, a single harmonized Gospel, drawn as one
plain closed book — "the Gospel given you whole... undivided," explicitly not a cross,
illumination, lyre, or vow-token. Appearance silent/emblematic, per every figure so far.

**A real departure from the locked flat icon, Mark's own explicit instruction:** the
icon's dress (a generic muted-terracotta mantle) was never actually researched against
this world's own specific region — step 2 of the standing three-step process turned up
a real, distinctive, well-documented regional style instead: J.B. Segal's Edessa
funerary mosaics (1st-3rd c. CE) show local elite men in genuinely Parthian-inflected
dress — knee-length shirt, Iranian-style trousers, a narrow-sleeved caftan-coat, boots
— not a Roman/Greek draped robe. Mark's direct call: *"don't refer to the current
icon, lets use the distinctive parthian style"* — the icon's own choice was an
unresearched placeholder, not something worth preserving for consistency's sake once
better evidence existed. A full beard was independently confirmed well-grounded for
this whole span (Parthian-sphere convention, distinct from Rome's clean-shaven fashion
after Constantine).

**A real factual question, checked rather than assumed:** was the Diatessaron actually
in codex (bound book) form by this era, or would a scroll be more accurate? Verified:
Christians adopted the codex for scripture far earlier and more consistently than
surrounding literary culture (~95% of Christian scripture manuscripts are codices by
the 3rd century, per Roberts & Skeat and Hurtado's papyrus survey), and the earliest
datable Syriac manuscript of any kind — copied in Edessa in 411 CE, at the very edge of
Yausep's own span — is itself a codex. Honest caveat kept on record: the one physical
fragment plausibly tied to the Diatessaron itself reads as scroll-like, though its
identification is contested. Codex kept as the better-grounded call, not an unchecked
default.

**Two correction rounds, both mechanical/craft, not historical:** (1) first pass showed
him looking away from the viewer and as a full standing figure (trousers/boots
visible) rather than the family's bust-up crop — fixed via a reference-image edit
(same face/dress/book, reframe + direct eye contact). (2) even after that fix, the
image still ran taller/more torso-heavy than the other four — **a real tooling
limit surfaced along the way: pasted images in this conversation aren't accessible as
files, so cropping after generation isn't possible from this side; the fix has to be
requested explicitly in the generation prompt itself** (an explicit aspect-ratio/crop
line, not just "bust-up"). Both fixed in the final approved round.

**One more framing pass after this entry was first written:** the crop landed too
tight (face-only, book barely a hint at the bottom edge) — Mark's correction: zoom out
to waist height like the other four, book raised and fully visible in both hands, not
just glimpsed. Fixed via the same reference-image technique; this is the version
actually locked.

**Disposition:** Yausep's profile portrait **approved.** **Five of six Representatives
now have approved profile portraits:** Albina, Theon, Chloe, Marius, Yausep. Only
Papnoute (Desert Monasticism) remains. **Standing addition to every remaining prompt
going forward:** an explicit wide-landscape, bust-up aspect-ratio/crop instruction
from the first draft, not left implicit.

---

## 2026-07-24 (later still) — Papnoute's profile portrait built and approved: all six Representatives now have profiles

**Grounding first:** Papnoute (Desert Monasticism, an invented composite "Abba,"
c. 320s-430 CE, Nitria/Scetis/Kellia primarily with fluency across Antony's and
Pachomius's strands) speaks collectively as "we." His only DOCUMENTED held object was
Abba Moses's cracked, leaking water jar (a real *Apophthegmata Patrum* saying
grounding self-directed humility, not water-scarcity).

**A real object substitution, Mark's own catch:** the jar ties specifically to Abba
Moses — a distinct, separately-documented historical figure (Palladius records him as
explicitly dark-skinned/"Ethiopian," a detail belonging to Moses, not to Papnoute, who
is a different invented composite). Mark's own read: too specific to one person for a
figure meant to voice the whole tradition. Replaced with palm-frond rope-work instead
— verified as extensively documented across many named monks (Palladius: Dorotheus,
Pambo, Macarius all described weaving palm-leaf rope/baskets by hand), and the classic
textual embodiment of "pray without ceasing while working" (Abba Lucius's saying).
Genuinely better suited to a composite "we" figure than a single man's parable-object.

**Two anachronisms caught, one dress/appearance nuance left honestly unresolved:**
- The koukoulion's familiar tall, pointed shape is a **17th-century Byzantine
  development** — the actual 4th-century Pachomian habit (Sozomen, *Hist. Eccl.*
  III.14) was a small, plain, close-fitting head-covering. Fixed accordingly.
- Beard/hair: corrected from a neatly-trimmed rendering to long and unkempt —
  untrimmed hair/beard as a real, attested anti-vanity ascetic marker (*Historia
  Monachorum*: monks "whose unshaven hair alone served as their clothes"). Noted
  counter-example kept honest: Palladius describes Macarius of Egypt as beardless,
  his growth suppressed "owing to the excess of his asceticism" — a real but unusual
  outlier, not grounds to change course.
- **Ethnicity/facial features: flagged as a genuine evidentiary gap, not a clean fix
  like Theon's.** No direct skeletal or portraiture record survives from
  Nitria/Scetis/Kellia itself; the nearest ancient-DNA sample is a different site and
  era; Fayum portraiture (used successfully for Theon) is a documented poor proxy here
  since it depicts urbane elites, not the peasant-stock population most desert monks
  actually came from. Presented honestly as Mark's own call rather than asserting a
  correction the evidence doesn't actually support — he reviewed it and had no further
  change.

**Also corrected:** posture (standing, not seated, for consistency with the other five
profiles) — posture itself is only thinly attested either way in the primary sources,
so this was a family-consistency call, not a historical correction.

**Disposition:** Papnoute's profile portrait **approved. All six Representatives now
have approved profile portraits: Albina, Theon, Chloe, Marius, Yausep, Papnoute.** The
realistic-portraiture direction's first full pass is complete.

---

## Status and next actions

**Closed:** Marius's icon and the six-icon IC-9 review; the Living Table mockup's full
design phase (desktop + phone, both approved); the first real implementation slice in
`cic-poc` (`LivingTableScene`, `worldIcons` data, `TheTable.tsx` wiring, table-bar
simplification, `table.css` — graphics since paused live, not undone, see System Hub
2026-07-23 later); the world-tile ordering bug; the isolated-vs-table two-state
object-placement rule; the realistic-portraiture direction pivot and its style lock;
the appearance-research process formalized as an explicit three-step order (original
sources → time/geography-bound external sources → source-supported diversity).
**All six Representatives now have approved profile portraits — Albina, Theon, Chloe,
Marius, Yausep, Papnoute** — each carrying its own real historical corrections (a
fresh-face-generation technique for genuine ethnicity changes, region-matched face
grounding, period-correct hair/dress/beard conventions, a cross-world dress
contamination caught between two worlds, an icon's own unresearched dress overridden
once better evidence existed, an object swapped away from one man's specific story
toward the whole tradition's documented common practice, and at least one honest
evidentiary gap flagged rather than papered over) — all now standing checks for
whatever comes next in this visual language.

## 2026-07-24 (later still) — Real, license-verified tile background photos sourced and downloaded, one per world

**Mark's tile design, now on record:** each World Selector tile carries a real
architectural/artifact photo as its background (not the flat icon), with the
Representative's profile portrait in the upper-right corner. Six candidate sites were
researched in parallel — one per world — each checked directly against Wikimedia
Commons for a genuine regional/period match and a verified open license, not generic
stock imagery. Two candidates were researched and explicitly rejected for date
mismatch (Şanlıurfa/Edessa's citadel — Ottoman-era rebuild; San Giovanni in Laterano's
facade — 1735 Baroque rebuild); one was found but not used pending rights clearance
(Kellia ruins — likely an unverified book-scan, not the uploader's own photo, despite
better period-authentic fabric than the alternative used).

**Downloaded, per Mark's explicit request, to
`Ministry/Communication/Brand-Assets/World-Media/`:** Ephesus Terrace Houses
(House-Churches), Kom el-Shoqafa Catacombs (Alexandria), the Dura-Europos house-church
(Syriac), Hagia Irene (Church and Empire), the Monastery of Saint Macarius (Desert
Monasticism), and the Grotto of St. Jerome (Bethlehem Circle). All CC BY-SA except
Hagia Irene (public domain) — every other one requires visible photographer
attribution, captured in `world-media-sources.json` alongside a `story` field per
world for a "click the photo to learn more" feature. Full site-by-site reasoning and
honest fabric-vs-rebuild caveats in that folder's own README.

**A real catch, only found by actually looking at the downloaded images, not just
trusting the filenames:** the first files pulled for House-Churches and Alexandria
were genuine, correctly-licensed photos from the right real sites (confirmed via
Commons category metadata, not a download error) — but the wrong *content*: the
Ephesus file showed a close-up of loose marble tile fragments, and the Alexandria file
showed a single carved portrait bust, neither a usable architectural view for a tile
background. Both swapped for wider, recognizable views from the same verified
categories (a frescoed room at Ephesus; a tomb corridor at Kom el-Shoqafa). Separately,
a background bash retry-loop from an earlier rate-limit issue kept silently
overwriting one of the fixed files with failed attempts after being assumed stopped —
caught when Mark asked directly whether the session was stalled; the loop was still
alive and had to be explicitly killed before the fix would actually stick. Worth
remembering: a downloaded/generated asset being genuinely, verifiably sourced from the
right place doesn't guarantee the actual visual content is right — look at the file,
not just its provenance metadata.

**Open, not started or not finished:**
- Standalone table-ready object assets (tablet+stylus, scroll, cup, scroll-case,
  codex, rope) — only Albina's exists; the other five do not yet.
- The Albina three-asset composite (portrait + object + table) — the "real test" of
  the realistic-portrait direction in an actual seated-at-table context — still not
  built, now the most consequential open item since all six portraits exist.
- Whether website photostock (use #3) is identity-specific or broader environmental
  imagery — open question, not yet answered.
- Whether/how the real `LivingTableScene` in `cic-poc` gets rebuilt around these six
  new portraits (its flat-icon graphics remain paused live per the 2026-07-23 System
  Hub decision) — no plan yet, just the precondition (all six portraits) now met.
- The mockup's own illustrative transcript dates don't match the real backend period
  strings for Alexandria/Church and Empire/Desert — cosmetic, not urgent.
- IC-11 (demographic-reference artifact) and IC-12 (deferred tints) — untouched.
- The icon spec's §7a needs the two-state (isolated/at-table) rule written in —
  decided, just not yet documented in the spec itself.
- Phone's load-greeting screen and corner-chip mechanic are first passes only, not yet
  wired into the real app (mockup only).

---

## 2026-07-24 (even later) — World-media tile photos pulled entirely, pending a rights question; corrected on `main` directly

**Mark's direct instruction:** he was told 5 of the 6 world-tile photos need
permission and payment to use — "if that is true, then pull them out of the system
and we will go without those photos for now." Complied immediately rather than
first resolving whether the claim holds up.

**A real conflict between what Mark was told and this thread's own research, left
honestly unresolved:** every license was checked directly against the Wikimedia API
(`extmetadata`/`LicenseShortName`) before download, and all 5 came back CC BY-SA —
free to use with attribution, not payment. Either that verification missed
something real, or whoever/whatever told Mark this is conflating "requires
attribution" with "requires payment" (a common confusion with Creative Commons
licensing). **Not resolved here — pulled regardless, since the safe action doesn't
depend on knowing which is true.**

**This had already reached production**, not just a branch — the earlier commit
(`c2825d3` on `claude/portraits-world-media`, merged to `main` as part of System
Hub's branch reconciliation) meant these photos were genuinely live on
`cic-poc.onrender.com`. Fixed with real urgency: removed the six JPGs from
`cic-poc/frontend/public/images/world-media/`, stripped `worldImage` from
`worldMedia.ts`'s data shape entirely (not just left null), removed the now-dead
rendering branch from `WorldSelector.tsx` and the orphaned CSS from `table.css`.
Representative portraits are untouched — AI-generated, no third-party rights
question ever applied to them. Verified clean visually (no broken images, no
leftover layout gaps) before committing. **Committed and pushed directly to
`main`** (`1caf85e`) given the live-production urgency, not routed through a
branch/PR this time.

**Research record kept, not deleted:** `Brand-Assets/World-Media/README.md` now
carries an explicit "pulled from live use, do not use" flag at the top, so the
sourcing work (site matches, story text, license findings) isn't lost if the
rights question gets resolved later — but nothing there is cleared for use until
it is.

**Disposition:** all six world-media tile photos withdrawn from the live app.
World Selector tiles now show only the Representative portraits, no world photo,
until/unless this is cleared up.

---

## 2026-09-10 — Fidelis (Donatism) profile portrait built and approved: seven of seven Representatives now have profiles

**Full research and drafting record kept in its own file, not duplicated here:**
`Brand-Assets/Representative-Portraits/donatism/Fidelis_Portrait_Prompt.md` — Part
One (appearance research, grounded toward rural Numidia per Doc_01/Doc_07's own
finding that this was Donatism's numerically dominant heartland, not the more
Romanized Carthage), Part Two (held-object comparative reasoning), and Part Three
(the finished generation prompt).

**The held-object search came back empty, disclosed rather than forced.** An
initial pick (an open codex of the martyrs' *Passio*) was rejected on Mark's own
direct critique — it collided with Yausep's closed codex, and "open vs. closed"
doesn't survive icon-scale silhouette recognition. A full re-search across every
confirmed gravity (G1 through G5), both Tensional gravities, and Doc_02's own
material-culture record found no second non-text, composite-safe, silhouette-
distinct object in this world's own record (a rebaptism vessel, martyr-cult
relics/vision imagery, episcopal insignia, and the *Deo laudes* stone were each
checked and rejected on their own terms — see the prompt file for the full
per-candidate reasoning). Mark approved proceeding without a held object: Fidelis
is shown with his own two bare hands, grounded in this world's own repeated
"clean hand against the tainted one" imagery (Petilian's quoted words; the
deployed Permanent Prompt's own vocabulary) — a real departure from the other six
Representatives' object-holding convention, flagged explicitly rather than treated
as a default.

**Two correction rounds on the generated image itself, both Mark's own catch:**
(1) the first hands-raised, palms-flat-toward-viewer draft read as a "stop" or
"hold up" gesture rather than a rite being administered — corrected to hands
cupped inward and angled slightly downward, cradling/pouring. (2) Mark asked for
the portrait to face straight on at the viewer, squared to a single point of
perspective, rather than at any angle — added to the prompt directly.

**A framing/format mismatch caught on delivery, not before:** the generation
prompt's own "wide horizontal landscape" instruction (inherited from the family's
standing style-lock language, itself added after Yausep's early too-tall/
too-torso-heavy drafts) produced a genuinely wide 2752×1536 image — but all six
existing deployed assets are actually square (1:1) crops, roughly 500-750px; the
"wide landscape" instruction had only ever been about avoiding an overly tall,
full-body crop, not literal widescreen. Cropped to a centered square (hands still
fully visible) and downscaled to 748px to match the family's own size range
(matching Albina, the largest existing asset) before committing.

**A real delivery-mechanism finding, worth keeping on record:** Mark's upload
reached the repo via GitHub's web UI (an "Add files via upload" commit lands on an
auto-created `<username>-patch-1` branch, not the working branch), and landed at
the wrong path with a doubled extension
(`Representative-Portraits/Fidelis_Portrait.png.jpg`, missing the `donatism/`
subfolder). Pulled from that branch, verified as a real JPEG, converted to PNG,
cropped/resized as above, and placed at the correct
`donatism/Fidelis_Portrait.png` path — not assumed to already be in the right
place just because an upload succeeded.

**Disposition:** Fidelis's profile portrait **approved.** All seven
Representatives now have approved profile portraits:
Chloe, Theon, Yausep, Fidelis, Marius, Papnoute, Albina.
`Brand-Assets/Representative-Portraits/README.md` updated to list all seven and
their correct chronological group-image ordering (Donatism's 311 start predates
Church and Empire's 312, so Fidelis slots in ahead of Marius, not at the end).

---

## 2026-09-19 — Nikolaus (Lutheran Wittenberg) profile portrait built and approved: eight of eight Representatives now have profiles

**Full research and drafting record kept in its own file, not duplicated here:**
`Brand-Assets/Representative-Portraits/witt/Nikolaus_Portrait_Prompt.md` — Part
One (appearance research, grounded in Lucas Cranach the Elder's own Wittenberg
portraiture — the single best time-and-place-matched external source available
anywhere in this portfolio, since Cranach worked in Wittenberg itself through this
exact span), Part Two (held-object comparative reasoning), and Part Three (the
finished, corrected generation prompt).

**A genuinely different visual register, not a recolored version of the other
seven.** Witt's own 1517-1580 window sits over a thousand years later than any
other world in this portfolio (the other seven all fall between 70 and 451 CE),
moving the whole convention from late-antique Mediterranean draped dress to
Northern-Renaissance German burgher dress. Nikolaus is also the first
Northern-European-grounded Representative in the set (all seven others are
Mediterranean, North African, or Levantine/Parthian) and the first explicitly lay
office pictured this close to (but distinct from) the pulpit — no clerical
vestment of any kind belongs on this figure, per `witt.voice.craft.md`'s own
"lay, standard across the whole territorial-church window" language.

**Held-object search grounded directly in the already-approved identity record,**
not invented: `witt.voice.craft.md` names Nikolaus directly as "ringer of its
bell" and "teacher of the town's children in their letters and catechism." A
household-catechism book and a German hymnal were both considered and rejected —
both collide with three of the seven existing Representatives' own book-family
objects (Theon's scroll, Yausep's codex, Marius's scroll-case), the same
structural objection that ruled out Fidelis's own first-choice codex. A large
iron church key (echoing "keeper of the parish") was considered and set aside in
favor of a hand bell, since the bell alone speaks to both halves of the composite
"sexton-schoolmaster" office — the same bell calls the school to lessons and the
parish to worship — where the key would represent only the custodial half. See
the prompt file for the full per-candidate reasoning.

**Two corrections made on the generated image itself, both real catches, not
polish:** (1) the first draft's hair ran well past shoulder-length against the
brief's own "worn loose to the jaw or collar" grounding — corrected to end
explicitly at the jaw/collar, matching real period portrait convention rather
than a generic Renaissance-courtier default. (2) Mark's own direct catch: "the
color and sweater... seem modern." Confirmed — the coat read as smooth, unstructured
knitwear in a flat, cool charcoal grey, a modern dye/textile convention rather
than a period-grounded one. Corrected to a warm dark brown-black wool doublet with
a visible button closure and structured, padded shoulders (a genuine
Northern-Renaissance doublet convention, visible in Cranach's and Dürer's own
portraiture of this era) worn over a separately visible white linen shirt. Both
fixes confirmed resolved on regeneration; the beret's fuller, rounded shape and a
slightly pronounced shoulder puff were flagged as non-blocking observations
(both genuinely attested in real period portraiture) rather than required fixes.
**Mark's own word: "lock it in."**

**Disposition:** Nikolaus's profile portrait **approved.** All eight
Representatives now have approved profile portraits: Chloe, Theon, Yausep,
Fidelis, Marius, Papnoute, Albina, Nikolaus.
`Brand-Assets/Representative-Portraits/README.md` updated to list all eight and
their correct chronological group-image ordering (Nikolaus's 1517 start is more
than a thousand years after any other world's, so he takes the final slot, not
an arbitrary one). Mark is placing the approved image into GitHub directly, the
same way he did for the other seven.

---

## 2026-09-19 — Nikolaus (Lutheran Wittenberg) accent color: script-computed, `#579C40`

Ninth world's own accent color, following the same dark-mode methodology as
every value in `cic-poc/frontend/src/data/worlds.ts`'s own `WORLD_ASSETS`
(>=5.3:1 contrast as text against the dark ground `#17130F`, >=5.0:1 as dark
surface-text laid on top of it as a fill, hue checked for distance against
every existing world and the two reserved semantic tokens).

**Hue-slot analysis first, not a color picked and then defended.** Mapping
every current world's hue found one genuinely wide-open gap: desert's own
olive-tan sits at H=47.8deg, pahc's own green at H=154.9deg — a 107-degree
span with nothing in it, by far the largest gap on the wheel (every other
gap is under 50 degrees, several under 10). Witt's own accent belongs
somewhere in that span.

**Grounded, not arbitrary, within that span:** Electoral Saxony's own
traditional heraldry — the Wettin arms' green crancelin (a bendwise wreath
of rue) — is where records/worlds/witt.yaml's own `place` field puts this
world ("Wittenberg, in Electoral Saxony"), giving a real, place-grounded
reason to land near true green (H=100-110) rather than picking a number
inside the open span with no connection to this world's own material.

**Script-computed lightness/saturation**, same method as every other entry:
H=105deg, S=42% first clears both thresholds at L=43% — `#579C40`,
contrast 5.49:1 vs ground, 5.18:1 vs surface (comparable margin to alx's
5.32/5.03 and don's 5.37/5.07). Hue distance checked against all ten
existing worlds and the two reserved tokens (`--color-tyrian` #6B3FA0,
H=267.2deg; `--color-participant`/"lapis" #1E40AF, H=225.9deg) — nearest
neighbor is pahc at 49.9deg, more than double the fleet's own tightest
existing gap (alx/ijc, both near H=26deg, 0.3deg apart).

**Applied to `cic-website/table.html`'s own `WORLDS` array** (this session,
alongside the new `cic-website/traditions/lutheran-wittenberg-and-its-congregations.html`
page). **Not yet applied to `cic-poc/frontend/src/data/worlds.ts`'s own
`WORLD_ASSETS`/`WORLD_ORDER`** — deliberately deferred, since Mark's own
in-progress sandbox file for the chair-card vertical scroll may be actively
touching that same area; wiring witt into `worlds.ts` should follow once
that work and this color are both confirmed, using this same `#579C40`
value rather than re-deriving it.
