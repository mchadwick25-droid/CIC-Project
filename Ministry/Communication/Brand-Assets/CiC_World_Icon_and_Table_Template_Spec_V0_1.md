# World Icons & the Composed Table — Build Spec V0.1 — DRAFT

**Status:** First draft, 2026-07-18, executing Mark's ruling: *"build an image/icon
for each world that can fit into a slot on a template table. Static after creation
for each conversation. A 1-world template, a 2-world template, and a 3-world
template; hold the 4- and 5-world templates for Phase 1 as we max at three
Representatives."* The draft art and the per-world object choices await Mark's eye
and per-world Source Ecology confirmation.

**What this is:** the concrete build of the Table's visual layer — the "Living
Table" reconciliation (`CiC_Table_Visual_Layer_Reconciliation_V0_1.md`), now
resolved to Mark's **static composed** model: one icon per world, slotted into a
per-seat-count table template, composed once when the conversation is created and
static thereafter. No live camera.

---

## 0. The governing principle: real people at a table, never spirits (Mark, 2026-07-18)

**Binding, above every other choice in this spec.** Mark: *"as long as it feels
real and not a spirit or ghost… I don't like lighting or glow… these must feel like
real people at a table, not spirits or ghosts."* This is the visual extension of the
project's existing "it's not a ghost" rule (which governs the *voice* — a bare
floating voice drifts toward séance). Applied to the picture:

- **Figures are solid and fully opaque.** No transparency, no wash-through, no
  translucency. (The V0.1 drafts were semi-transparent — a real error; fixed in
  V0.2: solid fills.)
- **No lighting, glow, halo, aura, bloom, or vignette.** Nothing that makes a figure
  look lit-from-within or dissolving into atmosphere.
- **Figures never fade in or out, never materialize or dematerialize.** A figure
  appearing/disappearing by opacity reads as a spirit; forbidden. Everyone seated is
  simply *present*, solidly, the whole time — like a photograph of people at a table.
- **"Who's talking" is shown by a solid, printed device, never by light** (§1a) — a
  nameplate going solid, a small madder marker — physical ink-on-parchment, the way
  a name is printed, not a spotlight.
- **Imagery governance still holds:** period art or plainly labeled reconstruction,
  never AI-generated-as-real.

Everything below serves this. Where a technique (a glow to mark the speaker, a
cross-fade to swap figures) would violate it, the technique loses.

## 1. The model — static composition, NO camera (FINAL, Mark, 2026-07-18)

**The composed Table is fully static — composition AND camera.** The image is composed
once at conversation creation (which worlds are seated, which icons fill which slots, in
which 1/2/3-voice template) and never recomposed, and — after building and seeing the real
table — **Mark dropped the live camera entirely** in favour of a still scene with a
nameplate speaker-switch (§1a). This **supersedes** the earlier "static composition, live
camera" model and the §1a camera grammar below it. (The camera-vs-slideshow analysis had
recommended dropping it; Mark confirmed on the built mockup — *"i have changed my mind
about camera panning."*)

- **The composition is static:** figures, objects, slots — set once, never recomposed.
- **No camera:** the scene does not pan, zoom, or move — nothing moves at all, the fullest
  expression of the anti-ghost rule (§0).
- **Text stays dominant:** the transcript is the sole primary surface over the era ground;
  the scene is the quiet living ground behind it.
- **Imagery governance holds:** labeled reconstruction, never AI-generated-as-real.

### 1a. The speaker treatment — nameplate inversion (FINAL, Mark, 2026-07-18)

Who is speaking is shown by **one motionless printed device: the speaking Representative's
nameplate inverts** — from the resting state (vellum background, ink text) to **dark
ground, light text** (`#2A2521` bg / `#F6EFE0` text) — and reverts when they stop. That is
the whole cue. **No camera, no glow, no vignette, no spotlight, and NO dimming of the
others** — every figure stays fully solid and present the entire time (a dimmed or faded
figure reads as a spirit; §0). The participant's turn and the Facilitator's turn (the
Facilitator is not pictured) leave every nameplate at rest.

On phone (Mark, 2026-07-18): the same nameplate inversion, carried by a **row of nameplates
(names only) pinned at the top of the conversation** — the speaking Representative's plate
inverts light→dark, the rest stay at rest — after the composed table shows once as a load
greeting (§5). No camera, no corner icon-chip. (This section replaces the earlier
camera-grammar text, now struck per §1.)

### 1b. The pilot table template — geometry (FINAL, Mark-tuned & approved, 2026-07-18)

Three templates share one design; only the seat count/positions change. All values are the
ones Mark dialed in and approved on the built mockup (`cic-living-table-templates`).
Percentages are of the viewport; icons render ~128px wide.

- **THE SCENE-LOCK RULE (structural — corrected 2026-07-18 after Mark caught the drift):**
  the figures and the table line live in **ONE fixed-aspect scene container** and are
  positioned in *scene* coordinates, never viewport coordinates. (The first implementation
  positioned figures by viewport % while the line scaled with width — the fit only held at
  the tuning window; "the table lines on many of these is not correct." The build must
  reproduce the container model, not per-element viewport positioning.)
  - **The scene:** centred, `top:5%` of the stage, `width:min(1180px,96vw)`,
    `aspect-ratio:1000/380` — everything below is in that 1000×380 space.
- **The table edge** — one SVG filling the scene, drawn **behind** the figures, a wooden
  rim in `--wood #6B583A`:
  - **one solid arc only** — **`M70 239 A460 115 0 0 1 930 239`**, stroke-width 8.
    Same Mark-tuned ellipse (centre ~500/280, curve 115, apex 165) with the **ends
    trimmed before they curl** (Mark: "the tails go funny… cut off the table ends a
    little earlier where they curl in") — the arc now stops where its slope is still
    gentle (~33°) instead of running to the ellipse's widest point, where the tangent
    goes vertical. The dashed near edge is DELETED (Mark: "the dotted line becomes a
    distraction… the semi circle communicates the table and fits with our logo").
    **No round line-caps** (they left stray dots).
- **The seats** — icon + nameplate over the edge, positioned in scene %; seat width
  **13.5% of the scene** (icon scales with it); nameplate `margin-top:4%`. Final
  Mark-tuned positions (`left% / top%` of the scene; read-back −10/−1/280/115, then
  figures refined to **−11** — "looks a little better"):
  - **1 voice** — `50 / −1` (centred).
  - **2 voices** — `40 / −1` and `60 / −1` (a close pair, so the centre doesn't read as a
    missing third — Mark).
  - **3 voices (pilot)** — `26 / 2` · `50 / −1` · `74 / 2`.
  - **Era-2 pair (Yausep + Albina)** — `40 / −1` and `60 / −1`, same template.

**Phone parity (approved 2026-07-19):** the phone greeting/conversation reuses this exact
scene (same arc path, same seat coordinates) inside a phone-scaled `.tablescene` box —
figures and the table line share one coordinate system on phone too, not the two
separately-eyeballed boxes an earlier build had (a real bug Mark caught: "the phone layout
is off with the table"). Phone-specific chrome, Mark-tuned:
- **Greeting:** table scene at the top; the welcome message sits ~1 line-height below the
  scene's bottom edge; the CTA button bottom-anchored near the screen's bottom edge (its
  original position — raising the message doesn't move the button).
- **Conversation:** the input bar sits raised off the very bottom edge (not flush); **"Don't
  know what to ask?"** appears directly above the input, quiet graphite text, mirroring the
  desktop affordance exactly (§4.2 of the UX design) — same role, opens the question sheet.
- **Greeting + conversation** — the Facilitator greeting is pinned **just under the lowest
  nameplate with a double-space of air** (measured live: nameplate bottom **+ 34px** — Mark:
  "just a double space" so it clears the table); the transcript flows down from there and
  tracks the rest of the screen, newest nearest the input. **Wide and left-justified**
  (Mark, 2026-07-18: "take the dialogue across the entire width… left justify everything"):
  column `left:5%`, `width:min(940px,90vw)`, ending 78px above the input; the Facilitator's
  lines are left-set too (the centred-italic treatment fell to the left-justify ruling).
- **Input group** at the bottom (Send = madder · End · "Don't know what to ask?").
- **Side "other choices" — DROPPED (DECIDED — Mark, 2026-07-18: "drop the side
  choices").** The placeholder chips ("＋ Add a voice" / "Open the map") violated three
  standing laws at once: S4's quiet-chrome cap already spent (table bar + "Don't know
  what to ask?" = 2/2); the composition **composed once, never recomposed**; the map
  **not reachable from S4**. The needs live where the law puts them: more voices = a new
  conversation seated at S2; the map = between conversations. The side margins stay
  empty; the mockup files that still show the chips are superseded on this point.
- **4- and 5-voice templates** held for Phase 1 (the Table maxes at three Representatives).

Ground = **the reading surface, not the era ground (DECIDED, 2026-07-19).** The S4 reading
ground is the brand's **warm cream `--gold-wash #FBF2E2`** with a vellum-lit top centre —
Mark rejected the era ground as too dark under long text and the cool parchment `#F7F3EB`
as "too cold." **The era tint is the atlas's job, not the reading background** — with one
reading surface everywhere, the earlier "Era 2 = a different table ground" variation is
retired; era identity is carried by the atlas and by the worlds themselves, not by the
Table's own ground. **The Era-1/Era-2 template distinction is therefore seating and object
only** (which worlds, which icons, which 1/2/3-seat layout) — the ground colour, arc, and
typography are identical across both eras. Dialogue ink stays brand `--iron-gall #2A2521`. Table bar per Full UX Design V1.0 §4. **The conversation is
LONG-FORM, not texting** (Mark, 2026-07-18): a name above flowing prose — Facilitator
italic graphite · Representative a gold small-caps label above full-width prose · You a
lapis label + italic question — all **left-justified**, **no message bubbles/cards** (the
gold-wash/lapis-wash card grammar is struck; V1.0 §4.1). You are talking *with* the
Representatives, so answers run long and breathe.

---

## 2. The world icon — asset spec

**One icon per world.** A dignified seated figure, drawn in the manuscript register
(iron-gall line + a world-tint wash), carrying that world's **source-grounded
object** — or honoring an honest empty place where the world's evidence supports
none.

- **Canvas:** `viewBox="0 0 100 132"`, transparent ground, single figure centered.
- **Register:** iron-gall `#2A2521` line (stroke 2.4–3), a world-tint wash fill at
  ~50% opacity behind the line. Same pen-and-parchment language as the logo and the
  chair illustration — not photorealistic, not a portrait of a person (the
  Representative is an acknowledged composite; the icon is emblem, not likeness).
- **The object** sits at the figure's place (local ~x60–84, y110–130), sized small,
  in iron-gall. It is the world's own expression-of-faith object, and **only if the
  world had one** — the empty place is a valid, honest icon (the vision's
  house-church exemplar).
- **Evidence-gating (binding, routed):** each figure's dress, the object, and any
  depicted diversity answer to that world's **Source Ecology**, exactly as the
  vision requires. This first draft uses restrained emblems as placeholders; **the
  per-world object and figure choices must be confirmed against each world's own
  construction record before they ship** — routed to the world-build / lexicon
  threads, not decided here.

### 2.1 The four live worlds (DRAFT — `Brand-Assets/World-Icons/`)

| File | World | Tint (DRAFT) | Object (DRAFT — CONFIRM vs Source Ecology) |
|---|---|---|---|
| `house-churches.svg` | **The House-Churches** (70–200, Antioch / Asia Minor / Rome — leaning Greek East) | terracotta `#C6926B` | **shared cup (agape) — CONFIRMED by Mark** |
| `desert.svg` | The Desert (Papnoute) — Era 1 | dark habit `#756950` (DRAFT) | **the leaking jug** — Abba Moses's cracked jar ("my sins run out behind me"). VERIFIED against the world's record 2026-07-18: the handwork (rope/basket) was rejected as unreadable at icon size; the jug is named in Papnoute's own Permanent Prompt ("the jar that leaks"), the most load-bearing exactly-attested story he carries, and a genuinely carried object. Drops = the meaning. **Flag:** it's the story that once failed adversarial testing (misattributed) — the icon attributes nothing, but it elevates the most-scrutinized story; the world's own self-image. Figure: monastic koukoulion cowl + full grey beard + dark habit (desert-father iconography as *inspiration*, no halo); **attire plain, no specific garment**. Square framing matched to Chloe, centered. Icon V0.5. |
| `syriac.svg` | Syriac Christianity (Mar Yausep) | slate-teal `#6FA3A1` | **the single harmonized Gospel — one whole *closed* codex** (Ewangeliyon da-Mhallete / Diatessaron). VERIFIED against the world's record 2026-07-18: DOCUMENTED (gravity C5, attested in both anchor voices, tied to the telos of *undividedness* — "one story, not four"). Form (codex vs scroll) is inference; distinctiveness is in meaning, not silhouette. Object carries the identity; attire stays plain/unadorned (**garments are unattested — no wool/linen/*kutōnā* claim**). "Teacher of the Covenant Order" is a descriptive label, not a native title (native = "Mar"). |
| `bethlehem.svg` | The Bethlehem Circle | plum-mauve `#B08AA0` | scroll (translation — "one man's pen") |

**Tint reconciliation flag:** these four world-tints are earth tones chosen to sit
*outside* the five reserved role-pigments (gold-leaf = Representative voice, lapis =
participant, Tyrian = apparatus, graphite = Facilitator, madder = action). The
app already uses a per-world `--world-color` for bubble tinting; **the per-world
color system needs one reconciliation pass against the role-pigments** so a world
tint never collides with a role meaning. Flagged to the branding thread (its review
prompt already asks about the role-color language).

---

## 3. The table templates — one per seat count

**Three templates** (`Brand-Assets/Table-Templates/`), chosen by seat count at
conversation creation:

| File | Seats | Slot x-centers (in a 460×252 canvas) | Reads as |
|---|---|---|---|
| `table-1-world.svg` | 1 | 230 | Deep Interview |
| `table-2-world.svg` | 2 | 158 · 302 | Compare Worlds |
| `table-3-world.svg` | 3 | 120 · 230 · 340 | Compare Worlds |

- **The table** is drawn in gold-leaf line (`#B45309`) on gold-wash, the same
  language as the chair illustration — an elongated ellipse with legs.
- **The figures sit behind the table** (their base tucked just behind the back
  edge), evenly spaced by count.
- **The near edge is the participant's open place** — drawn as a dashed arc, the
  same "a chair pulled out for you" gesture as the landing hero and the logo. You
  are not a figure at this Table; you are the one it was set for.
- **4- and 5-world templates are deferred to Phase 1** (Phase 1 max = 3
  Representatives at the Table), per Mark. The composition logic below already
  parameterizes slot positions, so adding them later is a data change, not a
  rebuild.

## 4. Composition logic (for the build thread)

1. At conversation creation, read the seated world count `n` (1–3 in Phase 1).
2. Select `table-{n}-world.svg` as the base.
3. For each seated world, place its `World-Icons/{world}.svg` at slot `i`'s
   x-center (scaled to the slot; the templates already embed the four live worlds
   as worked examples — the app substitutes the actual seated worlds).
4. **Rasterize/flatten once** to a single static image (or a frozen inline SVG) for
   that conversation. Compose once; never recompose mid-conversation.
5. Render it as the **ground layer** behind the transcript's parchment veil (the
   Increment-1 seam, `CiC_Build_Handoff_Increment1_V1_0.md` §6b, is what this drops
   into).

**No per-turn state touches this layer.** It is set when the Table is set.

## 5. Desktop vs. phone

- **Desktop (≥900px):** the composed table is the ground behind the transcript
  column — solid figures, present the whole time. Who has the floor is shown by the
  solid speaker marker (§1a); if the camera is kept, it moves over the solid figures
  with no glow. The parchment panel behind the *text column* keeps reading contrast —
  it is a flat panel behind the words, **not** a translucent wash dimming the
  figures (that would ghost them).
- **Phone (<640px) — a solid corner speaker-icon (Mark, 2026-07-18):** a **small,
  solid, opaque world-icon chip** pinned in a corner (e.g., top of the transcript
  area) shows **who is currently talking** — the speaking Representative's own icon,
  a **clean swap per turn, never a fade** (a fade in/out is the ghost effect §0
  forbids). When the participant or Facilitator has the floor, the chip shows the
  small whole-table glyph. The chip is a solid portrait, like a printed nameplate —
  present or not, never dissolving. Small-screen legibility wins by default.

## 6. Cost, and what this collapses

Mark's static-composed model **collapses the reconciliation's T1/T2 tiers into one
tractable build:** per-world emblem icons (not photoreal evidenced portraits) +
three templates + compose-once. This is buildable **without** the full
demographic-reference construction artifact the vision marked *future* — because an
emblematic figure carries far less evidentiary load than a photorealistic depiction
of a world's population. The Source-Ecology evidence-gating still governs each
icon's **object and register** (routed, §2), but the heavy data dependency that
gated the photoreal version is no longer on the critical path. The icon art itself
is the real cost, and it is a bounded, per-world design task (four worlds live).

## 7. Draft assets in this delivery

- `World-Icons/house-churches.svg` · `desert.svg` · `syriac.svg` · `bethlehem.svg`
- `Table-Templates/table-1-world.svg` · `table-2-world.svg` · `table-3-world.svg`
  (each composed with the live-world icons as worked examples)

All DRAFT — Mark's eye + per-world Source Ecology confirmation are the gates.
Shown at both breakpoints in the Full UX Design artifact (Part 3b).

## 7a. Portrait STYLE — DECIDED (Mark, 2026-07-18): Option 1, the line emblem

Three styles were drawn (icon sketch / period-art realism / simple two-color
profile). **Mark chose Option 1 — the line emblem** (iron-gall line + solid world
tint; the register this spec uses), with two refinements:

1. **The figure HOLDS its world's object** (Mark: *"them holding a piece of the
   world makes sense — Theon holding a scroll, Chloe holding a cup, etc."*). The
   object moved from sitting at the base to being **cradled at the chest** by two
   line arms — the figure is a person *doing* something, which reinforces "real, not
   a spirit." **Chloe's object is the CUP (the agape meal) — confirmed by Mark**,
   settling the earlier cup-vs-empty-place question for Rome.
2. **The eyes are reduced** (Mark: *"eyes a little less"*) — from dashes + nose +
   mouth to **two small dots + a faint nose, no mouth**. More restrained, more
   emblematic — which also keeps it on the "world, not a person" side of the axis.

**Form corrected to V0.4 — connected bust (Mark, 2026-07-18):** the V0.3 *seated*
figure left a gap at the neck between head and robe, which read as a detached,
ghostly head (*"the head not attached, it's too ghost like"*). Reverted to the
**connected-bust silhouette** from the Option-1 Chloe Mark originally liked: head,
veil, and shoulders are **one continuous shape**, the face nested in the veil
opening, no gap. Reduced eyes kept; the object held at the chest (overlapping the
garment so nothing floats). In the table templates the busts sit **behind the
table edge** (visible from the table up) — the table is drawn over their lower edge.

**Assets: V0.4** (`World-Icons/`, `Table-Templates/`), four live worlds, connected
busts holding their objects (Chloe cup · Papnoute basket · Mar Yausep codex ·
Bethlehem scroll), solid/opaque. Published preview artifact.
The emblem↔portrait axis is resolved on the emblem side, consistent with "the
Representative is the world, not a person." Period-art realism (old Option 2) is
**not** adopted; if a world ever wants a richer real-period-art treatment it returns
as its own decision under the two hard rules (genuine source-credited art, never AI;
"a face from this world").

**Note — "Theon" (UPDATED 2026-07-18):** Theon is now a **live world** — the
Representative of the **Alexandria Catechetical School** (`World-Builds/
Alexandria-Catechetical-School`, `alex_Representative_Permanent_Prompt_Theon.txt`).
This supersedes the earlier note that Theon was only Mark's example. The live set is
now **five**: Chloe (House-Churches), Papnoute (Desert), **Theon (Alexandria)**, Mar
Yausep (Syriac), Bethlehem Circle (Albina). Theon's icon is built and locked — see §7d.

## 7b. Gender + appearance as the third Identity element (Mark, 2026-07-18)

Mark: *"we need gender… put this inside the exception box we made for the name and
role… now we have three things that fit together, and gives us freedom to be a
little more realistic."* Appearance (incl. gender) becomes the **third element of
Representative Identity**, alongside Name and Role, derived by the same Section-1
principles (grounded in the world · composite not an individual · no invented
biographical detail · connectable). Gender is already implicit in the Name/Role and
is a Voice Configuration attribute — the icon matches it. Full proposal:
`Ministry/Technology/CiC_Representative_Appearance_Third_Identity_Element_V0_1.md`
(routes to the construction-framework owners for the formal template amendment).

**Icon V0.6 (restored) applies it:** the V0.5 rebuild drifted crude ("too much like
South Park figures" — Mark); reverted to the **exact approved Option-1 refined
bust** (inner veil edge framing the face, full features). Gender kept via the two
refined bases: **female = veil, no beard, full face** (Chloe cup; Albina scroll);
**male = hood + beard** (Papnoute grey beard, basket; Mar Yausep dark beard, codex).
Chloe and Papnoute are byte-for-byte the approved originals. Object at the base (as
in the original). The Theon extra was removed (not a live world). Draft — per-world
dress/demographic confirms against Source Ecology; the fully-realistic tier waits
on the demographic-reference artifact.

**Lesson logged:** don't re-derive an approved drawing from scratch — preserve the
exact approved base and vary only what must change.

## 7c. Chloe LOCKED (V1.7); the icon style is the ERA 1 template (Mark, 2026-07-18)

**Chloe's icon is locked** at V1.7 — connected-bust line emblem, ochre himation drawn
over the head with the white under-veil and chin showing, a thin veil-edge line
across the forehead, small neutral oval eyes, a mouth softened halfway to flat, the
undyed-linen chiton at the base, the cup. Grounded in the world's evidence and the
participant-response review (`CiC_Representative_Icon_Participant_Response_Review_V0_1.md`).
Master = `World-Icons/house-churches.svg`; locked copies `_working-base/chloe_LOCKED_v1_7.svg`
(and `chloe_LOCKED_v1_8.svg`, current).
**FINAL — Mark confirmed 2026-07-18 ("Chloe is good on all accounts").** The dress
grounding holds against this world's *own* sources (the veil per 1 Cor 11, Corinth/
Greek East; Chloe in 1 Cor 1:11; modesty per 1 Tim 2:9 / 1 Pet 3:3; cup confirmed) —
not general recall. No open gate.

**V1.8 post-lock amendment (Mark, 2026-07-18):** skin warmed from `#E8C9A3` (a generic pale
Mediterranean that tied with Roman Albina) to **`#D8B184`** — a warm Anatolian olive that
grounds her complexion in her actual Greek-East setting (Antioch / Asia Minor) rather than a
Roman/pale default. Complexion is inference (record silent), traced to the documented setting;
the demographic-reference artifact remains the eventual authority. Art otherwise unchanged. This
also corrected the family skin spread: the Greek East now reads warmer than Rome (Albina), as it
should, instead of the two tying at the pale end.

**This style is the ERA 1 icon template.** Mark: *"use this for other era 1
worlds."* Other Era 1 worlds are drawn to this standard — the same connected-bust
line emblem, parchment table ground, restrained face, and object — each with its
own **identity-derived, Source-Ecology-grounded** appearance (gender, dress,
head-covering, object) per §7a/§7b. Do not rush-derive them crudely (a logged
lesson); build each to the Chloe standard when its appearance is grounded.

## 7d. Papnoute + Theon LOCKED (pending full-family review) (Mark, 2026-07-18)

Three of the five icons are now built to the Era-1 template and locked (each locked
"for now," pending a **full-family review once all five are built** — Mark's plan).
Each object was **verified against its own world's construction record** before use
(the disciplined grounding method; appearance stays emblematic and flagged where the
record is silent).

- **Chloe** — House-Churches. FINAL V1.8 (§7c; V1.8 warmed her skin to a Greek-East olive
  `#D8B184`). Object: the shared **cup**.
  Master `World-Icons/house-churches.svg`; `_working-base/chloe_LOCKED_v1_7.svg`.
- **Papnoute** — Desert Monasticism. LOCKED **V0.7**. Grey-bearded koukoulion-cowled
  abba; skin darkened to a sun-weathered North-African/Egyptian-desert tone (Mark);
  beard curves down over a small mouth gap. Object: the **cracked jug** (Abba Moses's
  leaking jar — named in his Permanent Prompt / story `desertstory004`). Master
  `World-Icons/desert.svg`; `_working-base/papnoute_LOCKED_v0_7.svg`.
- **Theon** — Alexandria Catechetical School. LOCKED **V0.8**. Round-dome white
  mantle, short grey hair fringe, clean-shaven, medium-Mediterranean skin; object at
  the base is the **open scroll** (wooden rod + finials each end) — the world's own
  *shared* text (*"the scroll was opened… turned to the light"*, gravity C1). A
  himation drape was tried and **removed** at Mark's call (kept in version history).
  A liturgical vestment (epitrachelion/phelonion/orarion) was **deliberately avoided**
  as a 4th-c.+ anachronism that would mis-cast a *didaskalos* as an ordained priest.
  Appearance is INFERENCE on a silent, guarded record (the world names "a fabricated
  individual… a room, a scroll" as a failure). Master `World-Icons/alexandria.svg`;
  `_working-base/theon_LOCKED_v0_8.svg`.
- **Mar Yausep** — Syriac Christianity (Edessa–Nisibis). LOCKED **V0.2**, first **Era 2**
  icon (sits on the Era-2 ground). Covenant-teacher (*malpana* of the *qyama*) — explicitly
  NOT a bishop, NOT a desert monk, so no mitre/cross/cowl. Terracotta mantle, dark hair +
  dark beard (younger town-teacher), Levantine-olive skin `#B58A5A` (Option 3, Mark).
  Object: the **one harmonized Gospel** (Diatessaron) as a single closed book — DOCUMENTED
  as identity-constitutive ("one story rather than four kept apart… undivided"); the book's
  physical form (codex vs scroll) is left unasserted (record silent). Appearance INFERENCE
  on a silent record; the old "girdle" confirmed absent; no anti-Jewish/supersessionist
  motif. Master `World-Icons/syriac.svg`; `_working-base/yausep_LOCKED_v0_2.svg`.

- **Albina** — Bethlehem Circle (Hieronymian-Ascetic-Literary). LOCKED **V0.5**, second
  **Era 2** icon (Era-2 ground). An ascetic widow (*vidua*) + patron in documented renunciant
  **plain dress**; differentiated from Chloe by grey **side-parted hair** (veil drawn back, not
  forward), a plain wool palla, and a softer neckline tone (`#8F805E`). Object: a **wax tablet
  + stylus** — the writing instrument of this literary circle (letter-drafting + scholarly
  labor); a Mark-directed emblem, flagged as not itemized in the record. Role kept honest (a
  widow-patron, NOT a Hebrew scholar); avoided the "Vulgate" label, Nativity-grotto, medieval-nun
  costume, and Origenist/Pelagian polemic. Master `World-Icons/bethlehem.svg`;
  `_working-base/albina_LOCKED_v0_5.svg`.

**ALL FIVE BUILT & LOCKED (2026-07-18).** The set: Chloe (cup) · Papnoute (jug) · Theon
(scroll) · Mar Yausep (Gospel book) · Albina (wax tablet) — two women, three men, five distinct
objects, a skin spread by setting (pale Rome → Greek-East → Alexandria → Syriac → desert), Era-1
and Era-2 grounds.

**The full-family review (IC-9) RAN 2026-07-18 overnight — FAMILY PASSES; the locks stand.**
`CiC_World_Icon_Family_Review_V1_0.md`: frame/silhouette/objects/flags/skin-spread/template
checks all green; two findings fixed in-pass (three masters' in-file lock headers aligned to
this section's record; desert's INFERENCE keyword added); three watch items for daylight —
W1 Chloe's ink-black cup (observation only, she is FINAL) · W2 render the two Era-2 figures
on the live table — **SATISFIED (graphics resume, 2026-07-18): Yausep + Albina render as an
"Era 2 · 2 voices" toggle on the live templates mockup; both seat cleanly at the §1b
geometry, objects clear of the edge, nameplate inversion legible on both garments** · W3
Theon's world manifest colour is unassigned (World-Map thread, rides SB-5). **The
sub-question the render surfaced is now DECIDED** (see the reading-surface note above,
2026-07-19): one warm-cream ground everywhere; no Era-2 ground variation.

**Era 2's template variation, resolved (2026-07-19, supersedes the original 2026-07-18
"maybe just color of background" plan):** the figure style, ground colour, arc, and
typography are identical across eras — **Era 2's variation is seating and object only**
(which worlds are seated, which icons, which 1/2/3-seat layout), same as it already works
in practice. There is no separate Era-2 background to build.

**Atlas coordination (checked 2026-07-18, Mark's request):** the World Orientation
Map / World Atlas **has no per-era color profile** — it uses one uniform ground
(parchment `#f3ecdc` / gold `#a07c33` light; leather `#1d1811` dark) across all ten
eras, distinguishing eras by *position*, *era medallions* (period art), and Cinzel
labels, not by background color. (Its only per-thing colors are per-*world* and
per-*status*.) So there's nothing to match yet. **Note for when the atlas is next
edited:** the per-era background tints we choose for the icon tables become the
canonical era color profile, and the atlas should adopt the *same* per-era grounds
so the two systems read as one. This folds into the already-flagged map→brand
palette convergence (the atlas demo predates the finalized brand palette; Brand
Alignment Review's "three visual systems → one"). Owner when it happens: the World
Map thread, using the icon-table era grounds as the reference.

**The governing constraint on era colors (Mark, 2026-07-18): choose for legibility
under overlaid information, not for how distinct they look alone.** On the atlas an
era ground is a *background* with dense content scrolling over it — world bands,
labels, edges, medallions, ink text, per-world colors. So the era grounds must:

1. **Be near-parchment tints — very low saturation, high value.** Think gentle
   wall-chart era bands, not colored sections. The difference between eras is a few
   percent of warmth/coolness, felt on scroll, never a hue block.
2. **Keep every overlay legible over them:** iron-gall ink text, the gold rules,
   and all four per-world manifest colors must hold contrast on each era ground —
   test each candidate against all of those, in **both light and dark**.
3. **Never compete with the world colors.** The world hues are the map's meaningful
   color; the era ground stays quiet beneath them.
4. **A continuous flow across the timeline, not ten separate tints (Mark,
   2026-07-18).** The era grounds form one **ordered progression** — a gradient
   moving through the manuscript range from Era 1 to Era 10 — so that *adjacent eras
   flow into each other* (continuity) while *distant eras are clearly different*
   (distinction), and scrolling forward literally reads as moving forward in time.
   Each era's ground is one step along that flow; a person crossing an era boundary
   should feel the ground shift, and a person scrolling the whole span should feel a
   single directional drift, never a patchwork.
   - **Mechanism:** choose two endpoint grounds inside the manuscript-pigment range
     — Era 1 and Era 10 — and interpolate the eight intermediate eras evenly along a
     smooth path (a controlled warmth/value drift), then hand-tune each step so
     neighbors are *distinguishable but related*. Every point on the path must still
     pass rules 1–3 (muted, info-legible, non-competing) in light and dark.
   - **Starting leaning (tunable, not locked):** warm aged-parchment for the ancient
     eras drifting to a cooler, paler vellum toward the modern eras — "the past is
     warm, the present is cool" — but the direction is a choice to settle when we
     build the grounds.

**Icon-table vs. atlas tuning:** the icon table shows *one* era's ground at a time
(one conversation), so it can afford a slightly more *felt* tint; the atlas shows
all eras at once under dense info, so it needs the tint even more restrained. Same
hue family, tuned to density — pick the atlas-safe (more muted) value as the base
and let the icon table sit at the stronger end of the same tint, never a different
color. **Decide the actual values when we build the era grounds; this is the rule
they must pass.**

### Era-ground values — APPROVED (Mark, 2026-07-18)

Mark approved the widened warm→cool flow after seeing it on the real ten-era atlas
timeline (proposal: scratchpad `cic-era-atlas.html`). **Direction: warm-past →
cool-present** (aged parchment at the Early Church, cooling to pale vellum at the
Global Church). A first pass moved only ~30 units of blue across ten eras and was
invisible between neighbors; the **approved flow moves ~57 units and drops value
slightly at the warm end**, so adjacent eras are perceptible while every ground stays
inside the parchment range and legible under ink / gold / the four world colors, light
and dark. On the atlas the ground is *one* era cue among several (medallion, title,
dates, position), which is why this restrained tint is enough.

| Era | Title | Light ground | Dark ground |
|----|-------|-----|-----|
| I | The Early Church Era (70–312) | `#EFDDB3` | `#241A0C` |
| II | The Imperial Church Era (312–451) | `#EDDEB9` | `#221A0E` |
| III | The Age of Monks and Empires (451–622) | `#EBDFC0` | `#201A10` |
| IV | The Early Medieval Era (622–1054) | `#E9E0C6` | `#1F1A13` |
| V | The High Medieval Era (1054–1300) | `#E7E1CC` | `#1D1A15` |
| VI | The Late Medieval Era (1300–1517) | `#E6E3D3` | `#1C1A17` |
| VII | The Reformation Era (1517–1650) | `#E4E4D9` | `#1A1A19` |
| VIII | The Enlightenment & Awakening Era (1650–1815) | `#E2E5DF` | `#181A1C` |
| IX | The Missionary Era (1815–1906) | `#E0E6E6` | `#171A1E` |
| X | The Global Church Era (1906–present) | `#DEE7EC` | `#141A20` |

**Era 1 = `#EFDDB3` / `#241A0C`; Era 2 = `#EDDEB9` / `#221A0E`** — these are the two
grounds the Era-1 and Era-2 icon tables use. Endpoints and interpolation are set; each
step may be hand-nudged in build, but the flow and direction are fixed.

**Atlas convergence:** these ten grounds are now the **canonical per-era palette**. When
the World Orientation Map is next edited it adopts the *same* per-era grounds (replacing
its single uniform ground) so the icon tables and the atlas read as one system — owner:
the World Map thread, per the coordination note above.

**Rough era grouping of the live worlds (flag for confirmation, not asserted):**
The House-Churches (70–200, Antioch/Asia Minor/Rome) = Era 1 (locked). The Desert (270–400) begins in
Era 1. Syriac Christianity (300–450) and the Bethlehem Circle (380–420) sit in
Era 2 → the Era 2 template variant. Era assignment for the template is a
world/map-thread call; noted here so the era-scoped background plan has a starting
map.

## 7e. Marius LOCKED (V1.0) — sixth world, sixth icon (Mark, 2026-07-22)

**Church and Empire** (Imperial and Juridical Christianity — Rome / Constantinople / Milan,
c.312–451) was installed as the sixth live world 2026-07-18/22; Marius, its apocrisiarius
("Deacon of the Letters"), is the first icon designed after the IC-9 family review, in its own
creative UX thread rather than the icon-build thread proper — worked live with Mark, one open
question at a time, rather than converged on alone.

**Object (DOCUMENTED):** a leather-strapped scroll-case (capsa), not a single letter. His own
Permanent Prompt introduces him as "a deacon, entrusted with carrying letters... between the
great sees," and his title is literally "Deacon of the Letters" — a sealed letter (the more
literal reading) was drawn as Option A and genuinely considered, but the case was Mark's choice:
it reads as *the one who carries*, not just *the one who holds*. The strap runs left-waist to
right-shoulder, passing **behind** the case the whole way (Mark: extend it "so it looks like it
goes around back to his shoulder, but let the arm be outside it") — the case is drawn on top of
the strap so the carrying arm reads as in front of it, not wrapped by it.

**Dress:** a plain, undyed, ungirded tunic (INFERENCE, the same low-risk register as Papnoute's
"attire plain, no specific garment") plus an **orarion** over the left shoulder. This is
DOCUMENTED for the exact 312–451 window: Council of Laodicea, canon 22 (c.363 CE) bars
*subdeacons* from wearing it, which only makes sense if deacons themselves distinctively did;
it's attested broadly East and West, so it doesn't let one see's custom stand for the composite
"we" Marius carries — his own record explicitly refuses that move ("Rome argued one way...
none of the three speaks for all"). The **dalmatic** (wider, short-sleeved; tied to Roman
deacons via a partly-legendary Sylvester attribution, c.314–335) was analyzed and held in
reserve as Rome-specific — not drawn, but available if a richer, more Rome-flavored read is
ever wanted. Rejected outright: anything of episcopal rank (pallium, mitre) or later,
wider/embroidered medieval-style stoles — wrong rank or wrong century.

**Robe:** oxblood `#7A2E2E` — the world's own manifest colour (`world_manifest.py`), reused
directly as the garment tint (rather than a separately invented robe color, as most of the other
five use). Set beside the other five in a family comparison (2026-07-22), this reads visibly
darker/more saturated than any existing robe, and the crossed orarion + strap is the only
cross-body diagonal in the family — the rest keep the chest quiet and let the held object carry
the weight. Flagged to Mark; his call was to keep both exactly as drawn, reading them as a
quiet, unintended-but-real echo of the era's own tensions rather than a flaw to correct.

**Appearance** (skin `#D6B48A`, dark hair, clean-shaven): SILENT in the record. Unlike Chloe
(Antioch), Theon (Alexandria), or Papnoute (the Egyptian desert), Marius speaks as a composite
across three sees, not one place — no single setting grounds a skin tone the way the others'
does. Kept emblematic, INFERENCE flagged, a mid-Mediterranean tone sitting between the family's
Greek-East and Roman/Bethlehem ends, pending IC-11's eventual demographic-reference artifact.
Bare-headed bust/face template (no hood), following Theon's convention rather than Papnoute's or
Yausep's — a chancery deacon is neither a monk nor a town-teacher.

Master `World-Icons/empire.svg`; locked base copy `_working-base/marius_LOCKED_v1_0.svg`.

**Not yet covered:** the IC-9 full-family review ran 2026-07-18 for five icons and passed; it
has not been re-run with Marius added as the sixth. Treat that re-run, plus IC-11 (the
demographic-reference artifact) and IC-12 (deferred tints), as still open — this section locks
Marius's own design, not the family-wide audit around him.

## 8. Open, flagged (not resolved here)

1. **Per-world object choices** — confirm each against Source Ecology (esp. Rome:
   shared cup vs. the honest empty place). World-build/lexicon threads + Mark.
2. **World-tint vs. role-pigment reconciliation** (§2.1) — branding thread.
3. **Figure register** — how much a world's evidenced dress/diversity is expressed
   in an emblematic figure vs. held for a richer later form. Mark.
4. **Where the phone greeting-banner sits** in the load sequence — build thread's
   call within §5's intent.
