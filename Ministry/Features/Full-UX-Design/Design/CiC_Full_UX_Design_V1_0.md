# CiC Full User Experience Design — V1.0 (FINAL)

**Status: FINAL. Supersedes `CiC_Full_UX_Design_V0_1_DRAFT.md`** (approved by Mark
2026-07-17). V1.0 folds into one self-contained spec everything decided since V0.1:
the **Living Table** visual layer (a fully static composed scene), the **complete
world-icon set** (all five built and locked) and the **approved era-ground palette**,
and the two remaining UX decisions now closed (Living-Table motion; the reflection
beat). What V1.0 does **not** re-decide is named plainly in §10. This is the complete
participant experience, desktop and phone, across every designed feature — with the
Table conversation itself as the permanent center.

**What this is:** the whole journey drawn as one coherent thing, precise enough that a
build thread can implement any screen without re-deriving a decision. It illustrates
and extends the Front-End Integration Strategy's information architecture and executes
the Brand Foundations' visual direction — it re-decides neither. Where a real conflict
was found by drawing, it is named in §9, and every one flagged in V0.1 is now resolved.

**What governs it:** Conviction 5 (*"Technology expands what is possible. It is never
the point."*), Participant Agency (*"conditions for discovery, not pressure toward
predetermined outcomes"*), Constitution Article 6 (the four testable encounter
conditions), Article 17 (visible confidence), Article 30 (Levels 2–3 always reachable,
never gated), Article 34 (doorway, not a home), the Integration Strategy's clutter
budget and five-count screen check, and the Brand Foundations (Kit V0.2 + QuickRef).

**The one test every screen answers to:** a screen where features wait to be chosen
serves the encounter; a screen where they compete for attention has made technology the
point.

**What changed V0.1 → V1.0 (the short list):**
1. **The Living Table is fully integrated** (§2.5, §4.0) — the composed scene behind the
   transcript, **fully static** (composition and scene — see V1.0.1/V1.0.2), anti-ghost
   throughout. Was a separate reconciliation doc; now part of the design.
2. **The visual layer is built, not proposed** — all five world icons locked, the
   ten-era ground palette approved and canonical (§2.5).
3. **Decisions closed:** Level-3 panels (DECIDED), toggle retirement (DECIDED),
   Living-Table motion = **static, no camera** (DECIDED — Mark reversed "keep pan/zoom" on
   the built table; speaker shown by nameplate inversion, §4.0), the reflection beat **designed in**
   to the closing sequence (§5.6). The §9 conflict list is now a resolved-record.
4. **Visual identity is FINAL** — "Arriving" logo, the manuscript palette, Alegreya
   pair, all locked in the brand record (§2).

---

## 1. The design stance, in three sentences

The Table is the product; everything else is furniture that knows it. Every screen has
exactly one primary surface, quiet chrome within its stage's cap, at most one contextual
card, no modals over an active transcript, and no disclosure verb beyond hover = short /
click = full (tap = short / tap-through = full on phone). The visual register is a
beautifully set trade book on parchment — warm, unhurried, nothing antiquarian, nothing
tech-forward — and at the Table that book now sits over a **living scene** of the worlds
present, which never competes with the words.

---

## 2. The design system (FINAL — brand record)

Brand, messaging, and logo are FINAL (`CiC_UX_Design_Brand_Brief_V1_0.md`,
`CiC_Logo_and_Motion_Brief_V1_0.md`). §2.1 palette and §2.2 typography were adopted into
the brand record as written (madder locked muted — never brightened toward alert-red).
The Brand Alignment Review found the running app "accidentally close" to the manuscript
direction; every value below is a refinement of a color already shipping in `table.css`,
plus one deliberate change (madder as the action accent) argued in place.

### 2.1 Palette — "the manuscript's own colors," exact values (FINAL)

| Token | Value | Pigment | Job |
|---|---|---|---|
| `--parchment` | `#F7F3EB` | parchment ground | page background |
| `--vellum` | `#FEFCF8` | prepared vellum | cards and surfaces |
| `--iron-gall` | `#2A2521` | iron-gall ink | primary text |
| `--ink-faded` | `#6C6257` | faded ink | secondary text |
| `--rule` | `#E6DFD3` | ruled line | borders, hairlines |
| `--madder` | `#A13E2B` | madder red | **primary action accent** — Begin, Send, links, focus ring |
| `--madder-deep` | `#7E2F20` | madder, deep | action hover/pressed |
| `--gold-leaf` | `#B45309` | gold-leaf ochre | **the Representative voice** — accents, borders |
| `--gold-wash` | `#FBF2E2` | gold wash | Representative message ground |
| `--lapis` | `#1E40AF` | lapis/ultramarine | **the participant voice** |
| `--lapis-wash` | `#EEF3FB` | lapis wash | participant message ground |
| `--tyrian` | `#6B3FA0` | Tyrian purple | **the lexicon/transparency apparatus** |
| `--tyrian-wash` | `#F3EFFA` | purple wash | lexicon grounds |
| `--graphite` | `#8A837C` | uninked graphite | **the Facilitator voice** — the one *unpigmented* color at the Table |
| `--error` | `#C0392B` | — | errors only; rare by design |

Each speaking role at the Table wears a pigment the worlds' own documents used — gold-leaf
for the witnesses, lapis for the participant, Tyrian for the scholarly apparatus — and the
Facilitator alone is graphite, the unpigmented voice that represents no one. **The one
deliberate change: madder is the action accent** — separating what the *system* offers
(madder) from what the *witnesses* say (gold-leaf), which today share amber. Information
design serving Conviction 5.

**Dark mode: deferred, stated plainly.** The parchment ground is the brand. The map/tour
"old leather" dark register exists as precedent (and the icons ship dark variants, §2.5);
nothing here blocks a dark app variant and nothing ships one now.

### 2.2 Typography (FINAL)

- **Reading & display serif: Alegreya** (OFL) — humanist, calligraphic warmth, built for
  literature and strong at long on-screen reading (high x-height, sturdy at 17px).
  Fallback: Georgia, serif.
- **UI sans: Alegreya Sans** (OFL) — the matched superfamily for labels, buttons, chrome,
  captions. Fallback: system-ui.
- **Cinzel stays confined to the map/tour engraved artifacts** — not the app face.
- Scale: body 1.0625rem / line-height 1.7 (transcript); UI labels 0.8125–0.875rem; H1
  1.375rem. Nothing smaller than 13px ever carries meaning.

### 2.3 The logo and wordmark (FINAL)

**The logo is "Arriving"** — the C-as-table with the madder dot at the threshold — in
every identity slot including favicon and app icon. Public meaning, said once: *"The mark
is a table; the opening is the way in — and it never closes."* Wordmark: **Church in
Conversation** in Alegreya, italic "in," no "The"; series titles only ever beneath it; the
wordmark leads wherever words fit. The table-and-chair glyph survives as **companion
illustration only** (empty states, tour art), with its own pull-in motion; the adjacency
guard holds (the two table-metaphors never share one composition). Masters, motion, usage
sheet: `Ministry/Communication/Brand-Assets/`.

### 2.4 Breakpoints and grammar

- **Two breakpoints:** ≥900px desktop; <640px phone. Between them the single-column layout
  narrows gracefully.
- **Desktop disclosure grammar:** hover = short · click = full.
- **Phone disclosure grammar:** **tap = the Level-2 popover** (same content as hover), with
  one **"Full entry →"** action = Level 3; tap-elsewhere dismisses. Same two verbs, thumb
  form. No long-press, no new verb.
- **Touch targets:** ≥44px padded hit area on every interactive inline element.
- **Level-3 surfaces are panels, not centered modals** (§9.1, DECIDED): desktop side panel
  alongside the transcript; phone bottom sheet over the input area (~55% max height,
  transcript visible above). Participant-initiated only.

### 2.5 The visual layer — icons, the Living Table register, era grounds (FINAL / BUILT)

This is the design-system half of §4.0. Three settled pieces:

**a. The anti-ghost principle (governs everything visual with a figure in it).** Mark's
rule: *"these must feel like real people at a table, not spirits or ghosts… no lighting or
glow."* Enforced everywhere: figures are **solid and opaque**, present the whole time; a
speaker is marked by a **solid** printed nameplate inverting (desktop) or the **top
nameplate row** inverting (phone), **never** by glow, fade, dim, vignette, or transparency. This is the visual
extension of the project's existing "it's not a ghost" voice rule.

**b. The world icons — built and locked.** Each live world has one emblematic Representative
icon: a connected-bust line emblem in the manuscript register (iron-gall ink, restrained
face, a source-grounded object), gender- and object-differentiated, **emblem not portrait**
("a face from this world, not one person"). All five are LOCKED, each object/appearance
**verified against that world's own construction record** (DOCUMENTED / INFERENCE / SILENT
flagged):

| Representative · World | Era | Object | Master |
|---|---|---|---|
| Chloe · The House-Churches | 1 | shared cup | `World-Icons/house-churches.svg` |
| Papnoute · Desert Monasticism | 1 | cracked jug | `World-Icons/desert.svg` |
| Theon · Alexandria Catechetical School | 1 | open scroll | `World-Icons/alexandria.svg` |
| Mar Yausep · Syriac (Edessa–Nisibis) | 2 | the one Gospel (book) | `World-Icons/syriac.svg` |
| Albina · Bethlehem Circle | 2 | wax tablet & stylus | `World-Icons/bethlehem.svg` |

Two women, three men; five distinct objects; a skin spread grounded by setting (pale Rome →
Greek-East → Alexandria → Syriac → desert). Locked base copies in `World-Icons/_working-base/`;
full design law in `Brand-Assets/CiC_World_Icon_and_Table_Template_Spec_V0_1.md`.

**c. The era-ground palette — approved and canonical.** Each era has a near-parchment ground;
the ten form **one continuous warm→cool flow** (Early-Church aged parchment → Global-Church
pale vellum), chosen for legibility under overlaid information, never standalone distinctness.
Era 1 `#EFDDB3` / `#241A0C` (light/dark) · Era 2 `#EDDEB9` / `#221A0E` · … full table in the
icon spec §7. **Scope, as settled 2026-07-18:** the era grounds govern the **World
Orientation Map** and era-identity surfaces (the atlas adopts them when next edited — the
map→brand palette convergence); the **S4 reading surface is not era-tinted (DECIDED,
2026-07-19)** — it uses the brand's warm cream (`--gold-wash #FBF2E2`; icon spec §1b),
because Mark found the era ground too dark under long text and the cool parchment too
cold. One reading surface for both eras; the Era-1/Era-2 template distinction is seating
and object only.

---

## 3. Screen inventory — the whole journey, every named state

Stages are the Integration Strategy's six; states are this document's enumeration. Every
state exists at both breakpoints unless a phone divergence is named in §7. New in V1.0:
the Living-Table states (4.0a–4.0c).

| # | Stage · Screen state | What it is | Diverges on phone? |
|---|---|---|---|
| 0.1 | **S0 Threshold — resting** | hero + three co-equal doors | stacking only |
| 0.2 | S0 — menu overlay open | About/Features/FAQ over the page, never navigation-away | full-sheet overlay |
| 0.3 | S0 — Ask the Facilitator open | pre-threshold Q&A, Facilitator's own voice | full-sheet overlay |
| G.1 | **S0-guided — where you're starting from** | the four modes in plain language + "Just curious" (no-role resting state); skippable; sets the same session-constant role as 2.4 — Storyboard §G [**APPROVED — Mark**] | options stack |
| G.2 | S0-guided — what draws you | the three theme chips + "Surprise me"; same router as 3.1; skippable | same |
| G.3 | S0-guided — the prepared table | ONE world via Tier-1 routing + one prepared first question (role's walk, world-framed), in the proposal grammar; primary action = the standard Begin line; escapes to S2/S1; the question arrives pre-filled, never auto-sends | same |
| 1.1 | **S1 Orientation — map** (desktop) | the World Orientation Map, per its own spec | **replaced below 640px** |
| 1.2 | S1 — era-accordion (phone) | the map thread's decided production answer, illustrated §5.2 | phone-only |
| 1.3 | S1 — handoff return | worlds preselected at S2, URL scrubbed, Begin armed | same |
| 2.1 | **S2 Setup — resting** | tradition picker + tray + Begin; quiet chrome ×3 | single-column tiles |
| 2.2 | S2 — one world seated | Deep Interview framing on the Begin line (emergent, no toggle) | same |
| 2.3 | S2 — 2–3 worlds seated | Compare Worlds framing on the Begin line | same |
| 2.4 | S2 — role selector expanded | four roles + "no role" resting state | bottom sheet |
| 2.5 | S2 — world-click menu | Description · Tour · Choose for Table · Academic Documents (placeholders only here) | bottom sheet |
| 2.6 | S2 — proposed-table card | question-first flow only; the one T3 card | same |
| 2.7 | S2 — proposal null case | no world carries the question; map pointer | same |
| 3.1 | **S3 First question — typed** | question door: one input + three theme chips | same |
| 3.2 | S3 — silent begin | no starter pushed; Facilitator's ordinary welcome | same |
| R.0 | **S3 — question held** | on Send the input collapses; the question re-renders as "Your question, held:" — visible through every routing state, tappable to edit — Storyboard §R [**APPROVED — Mark**] | same |
| R.1 | S3 — considering | one Facilitator line + a printed working-mark (no spinner); one honest update if slow; inline retry on failure | same |
| R.2a | S2 — the proposal | the decided card given screen anatomy: proposal prose (sourcing reasons) · the not-seated named with real reasons · seats as editable tray chips over the full picker · Begin as the one consent | same |
| R.2b | S3 — clarify-once | exactly ONE clarifying question (2–4 options + free-type + "just propose something"); never a second | same |
| R.2c | S2 — honest null | designed moment: nearest-true-thing alternates (re-run routing), the map pointer with the era in view, Ask-the-Facilitator; the held question never discarded | same |
| **4.0a** | **S4 — the composed Table (load)** | the scene composed once from the seated worlds' icons on the era ground, in the chosen 1/2/3-world template | **greeting only, then the top nameplate row (§4.2)** |
| **4.0b** | **S4 — speaker shown** | the speaking Representative's **nameplate inverts** (dark ground / light text), reverts when done; no motion, no camera; nobody dimmed | **the top nameplate row inverts per turn** |
| **4.0c** | **S4 — reduced-motion** | the scene is already still everywhere; the nameplate inversion simplifies to an instant swap (no transition) | same |
| 4.1 | **S4 The Table — resting** | transcript + input over the living scene; table bar; collapsed "Don't know what to ask?" | §5.2 |
| 4.2 | S4 — streaming turn | latest Representative turn owns visual priority; their nameplate stays inverted while they speak | same |
| 4.3 | S4 — lexicon hover/tap | Level-2 tooltip/popover | popover w/ Full entry → |
| 4.4 | S4 — lexicon full entry | Level-3 side panel / bottom sheet | bottom sheet |
| 4.5 | S4 — citation hover/tap · full | same grammar, ✲ marker | same pattern |
| 4.6 | S4 — question sheet open | role's five walks + "Show me everything"; covers input area only | bottom sheet |
| 4.7 | S4 — next-questions card | T3 default occupant; typing dismisses; one-action off | full-width in-flow |
| 4.8 | S4 — tour invitation card | T3, rare, consent-explicit, decline final for session | full-width in-flow |
| 4.9 | S4 — bridge turns | Facilitator (+ Representative) turn in ordinary transcript grammar; no new UI | same |
| 4.10 | S4 — safety posture active | conversational turns; the T3 slot renders nothing; the scene rests unchanged | same |
| 4.11 | S4 — status line states | session-cap notice / connection loss, one quiet line in the table bar, never stacked | truncate + tap-to-expand |
| 4.12 | S4 — error | inline dismissible line beneath table bar | same |
| T.1–T.6 | **S4-tour** (a mode of S4) | threshold stop · beat playing · Q&A drop · honest-absence beat · exit/handback · S2 honest refusal | §5.5, §7 |
| 5.1 | **S5 Close — gracious close** | Facilitator's turn; T3 suppressed | same |
| 5.2 | S5 — "anything else?" beat | open pause; a real question evaporates the sequence | same |
| 5.3 | S5 — reflection beat | one optional question — "What stayed with you?" (designed in, §5.6) | same |
| 5.4 | S5 — resources offer | ask, never push; topic named, nothing listed yet | same |
| 5.5 | S5 — resources shown | 2–3 genuine external pointers, hover/click grammar | tap grammar |
| 5.6 | S5 — the door outward | comma, not period; no claim on what comes after | same |
| X.1 | Onboarding/consent | the existing screen, brand-corrected copy, shown once | same |
| X.2 | Loading · pre-session error | existing states, restyled to system | same |

Alpha/Phase note: the running app is Bypass-shaped (onboarding → picker → Table). This is
the Phase 1 target the screen set grows into; the Living-Table scene (4.0a–c) is its own
build increment (§11), and the 4/5-world templates wait for Phase 1 (the Table maxes at
three Representatives now).

---

## 4. The Table screen (S4) — the permanent center, fully designed

### 4.0 The Living Table (the scene beneath the transcript)

**What it is:** a single composed scene of the worlds present — each seated Representative
rendered as its locked icon, placed at the wooden table-edge arc in the 1-, 2-, or 3-seat
template (the solid arc alone reads as the table and echoes the logo's C-as-table; the
dashed near edge was tried and **deleted** as a distraction — Mark, 2026-07-18). The
composition is **static** — which worlds, which icons, which template, composed **once** at
conversation creation and never recomposed — and it is the **living ground beneath the
transcript, never a replacement and never a co-equal.** *Replace* is ruled out by the
vision's own law ("text is the permanent structural layer… the transparency mechanics only
work as text"); *alongside* is ruled out by the five-count's one-primary-surface rule. The
transcript is the sole primary surface; the scene is the populated, still descendant of the
approved landing hero.

**The scene is static — NO camera (UPDATED — Mark, 2026-07-18, reversing the earlier
"keep pan/zoom").** On building and seeing the real table, Mark dropped the camera: the
composed scene does not pan, zoom, or move at all. Who has the floor is shown by a single
motionless printed device — the **speaking Representative's nameplate inverts** from
vellum/ink to **dark ground / light text** (`#2A2521` / `#F6EFE0`) and reverts when they
stop. That is the whole cue. **No camera, no glow, no vignette, and NO dimming of the
others** — every figure stays fully solid and present (anti-ghost, §2.5a). The participant's
and Facilitator's turns leave every nameplate at rest. $0/turn — pure front-end rendering
driven by the `speaker` field the app already emits; no per-turn model call, no image
generation.

**Budget:** with nothing moving, the scene is unambiguously **ground** — it adds no primary
surface and consumes no card slot, and the earlier "attention-risk / pilot check" (which
applied only to the dropped camera) is moot. On phone, the same inversion is carried by the
**top nameplate row** (names only) after the one-time load greeting; no camera anywhere. The
exact pilot table geometry (the 1/2/3-voice seat coordinates, the wooden edge, the
greeting-pinning rule) is recorded in `Brand-Assets/CiC_World_Icon_and_Table_Template_Spec_V0_1.md`
§1b.

### 4.1 Desktop (≥900px)

One **wide, left-justified** column (~min(940px, 90vw), anchored to a left margin), over
the composed scene — Mark, 2026-07-18: *"take the dialogue across the entire width"* and
*"left justify everything"*; the dialogue reads down the page like a document, more like
the phone form, never a narrow strip between the figures. The greeting pins just under the
lowest nameplate with a double-space of air (icon spec §1b). Reading surface: the brand's
warm cream (`--gold-wash #FBF2E2`, current draft — graphic specifics deferred; era tint
scoped to the atlas). Top to bottom:

1. **The table bar** (T1 quiet chrome 1 of 2) — a single 40px hairline-ruled line, vellum,
   sticky. Left: the seats — one colored dot + name per Representative (gold-leaf family,
   per-world tint), the participant's own seat never shown (they are the reader, not a
   token). Right: the **consolidated status area** — exactly one quiet graphite line,
   priority-ordered, never stacked: refresh caution → session-cap notice → otherwise empty.
   Today's boxed RefreshWarningBanner retires into this line.
2. **The transcript** (primary surface, with the input), over the scene — **long-form, not
   texting (UPDATED — Mark, 2026-07-18).** You are *talking with* the Representatives, not
   messaging them, so a turn is a name above **flowing prose**, never a boxed message card
   (the gold-wash/lapis-wash bubbles are struck). Grammar: **Facilitator** — centered, italic,
   graphite; **Representative** — a gold small-caps label (name · world) above its answer as
   full-width prose, generous line-height, room to run long; **participant** — a lapis "You"
   label above the question in italic, left-justified like everything else (the earlier
   right-set treatment fell to "left justify everything"). No backgrounds, no borders, no
   bubbles — a printed dialogue that breathes. (`--gold-wash`/`--lapis-wash` remain in the
   palette for any washed grounds elsewhere, but the transcript no longer uses them.) Streaming
   pins scroll only when already near the bottom. Inside the text, unlimited T2 by grammar:
   Tyrian dotted-underline lexicon terms (first occurrence only), the ✲ citation marker at turn
   end. Hover = Level-2 card; click = Level-3 **side panel** alongside the column's right edge
   (420px, vellum, own scroll, Esc/× to close) — the transcript never gets covered.
3. **The contextual card slot** (T3, max 1) — in-flow after the turn that occasioned it,
   hairline card on vellum, *quieter than any speech bubble*. Priority: safety/close
   (renders nothing) ▸ tour invitation ▸ suggested next-questions.
   - **Next-questions (default):** 2–3 Facilitator-voiced chips + a graphite one-action link
     "Stop suggesting for this conversation." Typing dismisses instantly; they return only
     after the next Representative turn.
   - **Tour invitation (rare):** one card, consent explicit — *"Chloe can walk you through
     the Sunday gathering, as Justin describes it — every stop names its source. [Take the
     tour] [Not now]"*. "Not now" is final for the session, never re-pressed.
4. **The input group** (primary surface, with the transcript) — auto-resizing textarea,
   **Send** (madder), and the quiet **End** text control (graphite, right of Send — part
   of the input cluster, §9.5). Above the textarea's right corner: **"Don't know what to
   ask?"** (T1 quiet chrome 2 of 2) — a few graphite sans words, motionless, never pulsing.

**The question sheet** (opens from that affordance): slides up *over the input area only* —
the transcript stays fully visible and interactive above it. Contents: the participant's
role surfaces **their five walks first** as tabs; each walk shows its five questions in
order (a walk, not a menu — jump anywhere); **"Show me everything"** is one tap away and
exposes all twenty sets to every role. Dismisses on typing or any transcript interaction.
No role selected = the General five first, same sheet, nothing missing.

**What is not on this screen, by design:** the map; any role badge; any placeholder; any
modal; any notification; and **no side "other choices"** — the once-mocked margin chips
are **DROPPED (Mark, 2026-07-18)**: they violated the chrome cap, compose-once, and
map-not-from-S4 at once, and the needs they served live at S2 (a new conversation) and
between conversations (the map). The world-click menu's placeholders live at S2 and
nowhere here.

### 4.2 Phone (<640px)

Same column, full-bleed with 16px gutters. **The Living-Table scene is stripped hard:** the
composed Table appears **once as a load greeting** (welcome pinned just under it), then the
conversation is the whole screen and a **top row of nameplates — names only — carries who
is currently talking** by the same inversion as desktop; every plate rests when the
participant or the Facilitator speaks. **No camera, no corner icon-chip** (an earlier idea,
superseded — Mark, 2026-07-18: "nameplates still light/dark but just the name"). Otherwise:

- **Table bar:** one line; seat dots + first names, truncating with "+1" beyond two; the
  status line truncates to its lead phrase — **tap expands it**.
- **Transcript:** the same long-form labeled-prose grammar (no bubbles), full width; the
  speaker is carried by the **top nameplate row inverting** (names only), not a corner icon
  chip; lexicon terms and ✲ markers carry 44px hit
  areas. **Tap = Level-2 popover** with one **"Full entry →"** action; **Level-3 = bottom
  sheet** over the input area (~55% max), drag-down to dismiss — the latest turn stays
  visible above it.
- **Contextual card:** full transcript width, same in-flow position and dismissal rules;
  chips wrap to two lines max, then scroll horizontally.
- **Input group:** sticky bottom with safe-area inset; "Don't know what to ask?" keeps its
  full wording at 13px, right-aligned; **question sheet = bottom sheet** over the input area,
  walk tabs as one horizontally scrolling chip row.

### 4.3 The five-count check, run explicitly

| Count | Desktop | Phone |
|---|---|---|
| 1 · exactly one primary surface | transcript + input ✓ (scene is ground, not a surface) | transcript + input ✓ (scene = load greeting + top nameplate row) |
| 2 · quiet chrome ≤ 2 | table bar · "Don't know what to ask?" = 2 ✓ | same 2 ✓ (the nameplate row is part of the scene ground, not chrome) |
| 3 · ≤ 1 contextual card, in-flow | one slot, priority-ordered ✓ | same ✓ |
| 4 · zero modals during conversation | Level-3 = side panel; sheets cover input area only ✓ | Level-3 = bottom sheet, transcript visible ✓ |
| 5 · every depth behind hover/click | hover/click ✓ | tap/tap-through — same two verbs ✓ |

---

## 5. The other stages, each passing its own decided verdict

### 5.1 S0 — Threshold

**Primary surface:** the three co-equal doors under the hero. Hero: the waiting Table, warm
light, the Facilitator present as the one figure; the protected hook as the headline —
*"Twenty centuries of the church. One table. A chair pulled out for you."* — and the CTA
register beneath the doors: *"Come and join us at the Table."* Doors (equal size, equal
weight, no default): **Start with your question** · **Build your own table** · **Guided
onboarding**. **Quiet chrome (≤2):** *Ask the Facilitator* and the menu (About · Features ·
FAQ) as a **temporary overlay on top of the page** — never a navigation-away. **Cards: 0.**
Phone: doors stack vertically, still visibly co-equal. Five-count: 1 · 2 · 0 · overlay
participant-opened · n/a ✓.

**The third door is now designed** (it was named everywhere, defined nowhere):
**Guided onboarding** = three Facilitator-hosted beats — where you're starting from (the
modes in plain language + "Just curious") → what draws you (the theme chips + "Surprise
me") → a prepared one-world table with one prepared first question, in the proposal
grammar, Begin as the only consent. One beat at a time, everything skippable, standing
escapes to the map and the question door; the prepared question arrives pre-filled and
never auto-sends. Full design: `CiC_Full_UX_Storyboard_V1_0.md` §G — **APPROVED (Mark,
2026-07-18: "both are approved to move forward")**. States G.1–G.3 in §3.

### 5.2 S1 — Orientation (the World Map · the era-accordion)

Desktop: the map opens full-surface from S2's one quiet line. Everything inside it stands as
the map thread decided (first-visit overlay, hover card → click panel, edges on demand,
persistent tray, legend-as-thesis). The tray hands back to S2 preselected; **Begin stays the
only consent.** The map is on-request always, never auto-opened, never reachable from S4.
When the map is next edited it adopts the era-ground palette (§2.5c).

**Phone — the era-accordion, illustrated** (the map thread's production answer, drawn here
for that thread's confirmation, §9.3): a full-screen list — search + two filter chips (era ·
status); the ten eras as accordion rows; expanding lists tappable band rows (status-color
dot, name, dates, one line); tap = a bottom-sheet glimpse; "Full entry" = the panel. Bottom:
the same persistent tray + handoff contract. The wall-chart's density is deliberately
*replaced* here, not shrunk.

### 5.3 S2 — Table setup

**Primary surface:** the picker ("Choose a Tradition"), the tray/seat state, and **Begin**
(madder). The Single/Multiple toggle retires: **mode is emergent from seat count** (DECIDED;
the toggle was scaffold). The Begin line carries the emergent framing — one seat: *"Begin a
Deep Interview with Chloe"*; two–three: *"Begin — Compare Worlds: Chloe, Yausep"*. **Quiet
chrome (≤3):** the map link; the **role selector** collapsed to one line — *"Optional: tell
us where you're starting from — it shapes where the conversation starts, never what you can
ask or see"* — expanding to Regular visitor · Pastor or teacher · Academic or scholar ·
Reevaluation, with **no role as the visual resting state**; the per-tile sourcing-richness
disclosures. **T3 (question-first flow only):** the Facilitator's **proposed table** card —
reasons always sourcing reasons, worlds not seated named with the real reason, one tap
accepts, everything editable. Null case: a designed moment pointing at the map, never an
error. **World-click menu:** Description · Tour · Choose for Table · Academic Documents —
Tour and Academic Documents as honest visible placeholders *here and nowhere else*; a
non-qualifying world's Tour row carries the plain refusal rather than opening anything.
Phone: tiles single-column; role selector and world-click menu become bottom sheets.
Five-count: 1 · 3/3 · ≤1 · sheets participant-opened · hover/click ✓.

### 5.4 S3 — First question

Typed: one input box, and beneath it **theme chips, not question chips** — *An ordinary day*
· *How you looked from outside* · *What you never settled* — because no world is seated yet;
a tapped theme runs the same router as a typed question, into the S2 proposal card. Silent:
beginning without asking gets the Facilitator's ordinary welcome; nothing is pushed. The
data-layer invariant holds everywhere a starter is clickable: **world-framed, never
participant-framed** — enforced in the curriculum JSON, not by styling.

**The routing interval is now designed** (the backend had three tiers; no screen existed):
question **held** on screen (editable, never discarded) → an honest **considering** line
with a printed working-mark (no spinner; one honest update if slow; inline retry) → the
**proposal card's** screen anatomy, or **clarify-once** (one question, never two), or the
**honest null** as a designed moment. Full design: `CiC_Full_UX_Storyboard_V1_0.md` §R —
**APPROVED (Mark, 2026-07-18: "both are approved to move forward")**. States R.0–R.2c in §3.

### 5.5 S4-tour — a mode of S4, not a surface

> **DEFERRED TO PHASE 2 — not part of the current build cycle (2026-07-22).** Mark
> decided Hosted Tour is a second-tier (Phase 2+) feature, not something this launch
> builds, and directed that all Tour-related content be taken out of the current build
> cycle across documents, UX, and code planning. **This design stays documented
> as-approved below** — it does not get removed or rewritten, since it's still the
> right design for when Phase 2 takes this mode up. **The world-click menu's Tour row
> (§5.3) already degrades gracefully for the current build**: it's designed as an
> honest visible placeholder, and for a non-qualifying/unavailable world it "carries
> the plain refusal rather than opening anything" — so it should currently render in
> that not-yet-available/refusal state everywhere, not as a live entry point, until
> Phase 2 actually builds this mode. No change needed to that design to reflect the
> deferral; it already assumed Tour might not be available.

Entry only by consent: the S2 world-panel Tour row, or the S4 invitation card (rare, decline
final). Acceptance passes through **the threshold stop** — what this is / what it's built
from / what it will not claim — before any mode shift. During: **the stage and beats are the
primary surface**; persistent chrome is exactly three — the **register strip** (the
product's own voice naming witness account vs. labeled reconstruction, with the source
cartouche), the **beat tracker** (the engraved order band), and the **Exit door** (one
action, top right). A participant question drops the tour to ordinary conversational mode;
the tour resumes only if they want. The honest-absence beat ("What We Cannot Show You")
renders with the same cartouche dignity as any positive stop. Exit hands back to open
conversation — never left in a scene. Phone: stage full-bleed; register strip docked below
(never overlaid); beat tracker compresses to dots; Exit fixed top-right. Five-count (own
budget): 1 · 3/3 · 0 · 0 · hover/click ✓.

### 5.6 S5 — The close (the reflection beat, now designed in)

Sequential beats, exactly one on screen at a time, each skippable in one action; while the
sequence runs, the T3 slot renders nothing and the scene rests unchanged. In order:
1. **Gracious close** — a Facilitator turn, ordinary transcript grammar.
2. **"Anything else?"** — an open pause, no summary, no evaluation; a real new question
   evaporates the whole sequence back to normal flow.
3. **The reflection beat (DECIDED — designed in):** one optional question, *"What stayed
   with you?"*, private by default, never a form. It is **part of the closing sequence**,
   not gated on Increment 3's role-serving — it is a closing reflection, not a role-served
   question — and ships with the **closing-sequence build** (§11), one beat, one input,
   skippable. (This closes V0.1's §9.4 flag.)
4. **Closing resources** — ask, never push: the offer names the topic and lists nothing
   (*"Before you go — would you like a couple of genuine books or readings on [what was
   actually discussed]? No pressure either way."*); a yes shows 2–3 genuine, checkable
   external pointers behind the same hover/click grammar, framed as a modern person's
   pointers, never the world's own sources; a decline is a complete, graceful path.
5. **The door outward** — the ending is a comma, not a period; no claim on what comes after.
When accounts exist someday the pilgrim's map lives here — gated on that open decision,
refused forever as streaks. Five-count: 1 (current beat) · 0 · sequential · 0 · hover/click ✓.

### 5.7 The base grammar, everywhere

Lexicon (first-occurrence-only), inline citations (the ✲ marker), story/quote sourcing, map
statuses, tour cartouches, closing resources: one grammar, five applications, no feature may
introduce a sixth verb. Ask-the-Facilitator remains the threshold's secondary door and
quietly absorbs "why isn't world X here?" — same voice, zero new UI.

---

## 6. Conversation-primacy — how every feature passes, restated against these screens

| Feature | Verdict (decided) | Where this document shows it |
|---|---|---|
| The Living Table scene | ground | behind the transcript; a fully static composed scene; §4.0 |
| World Map | absence | not reachable from S4; §5.2 |
| Role selector | absence | S2 only; no badge anywhere in S4; §5.3 |
| Theme chips / proposed table | stage | S3/S2 entry moments only; §5.3–5.4 |
| "Don't know what to ask?" | collapse | a few motionless words; sheet covers input only; §4.1 |
| Next-questions | deference | in-flow, quiet, typing-dismissed, one-action off; §4.1 |
| Tour invitation | consent | one card, explicit acceptance, decline final; §4.1 |
| Tour active | becoming | it *is* the encounter; exit always one action; §5.5 |
| Lexicon / citations | grammar | inside the text; §4.1–4.2 |
| Session status | consolidated | one quiet line in the table bar; §4.1 |
| Closing beats (incl. reflection) | timing | only when ending; one at a time; §5.6 |
| Anachronism bridge | grammar (conversational) | ordinary Facilitator + Representative turns; no new UI; state 4.9 |

---

## 7. Mobile adaptations — the genuine divergences, named

1. **The Living Table is stripped to a load greeting + a top nameplate row (names only)**
   (§4.2) — no standing backdrop, no camera, no corner chip on phone.
2. **The map → era-accordion** below 640px (§5.2) — a different form, not a shrink.
3. **Hover → tap = Level-2 popover with one "Full entry →" action** (§2.4) — applied to
   lexicon, citations, cartouches, map statuses, closing resources alike.
4. **Level-3 surfaces:** desktop side panel → phone bottom sheet over the input area (~55%,
   transcript never fully covered) (§4.2).
5. **Contextual cards** render full transcript width, in-flow, identical rules (§4.2).
6. **Table bar status** truncates to its lead phrase with tap-to-expand (§4.2).
7. **Question sheet and S2 secondary surfaces** become bottom sheets; walk tabs become one
   scrolling chip row (§4.2, §5.3).
8. **Three doors stack vertically** with identical cards (§5.1).
9. **Touch targets:** 44px padded hit areas on all inline marks (§2.4).
10. **Tour chrome:** register strip docked; beat tracker compresses to dots; Exit fixed
    top-right (§5.5).
11. **Input is sticky-bottom with safe-area insets**; "Don't know what to ask?" keeps full
    wording at 13px (§4.2).

---

## 8. The "is this too crowded" test — every screen, five counts

| Screen | Primary =1 | Chrome ≤cap | Cards ≤1 | Modals =0 | Grammar | Verdict |
|---|---|---|---|---|---|---|
| S0 threshold | doors ✓ | 2/2 ✓ | 0 ✓ | overlay participant-opened ✓ | n/a | **PASS** |
| S1 map (desktop) | canvas ✓ | tray+legend ✓ | 0 ✓ | panel alongside ✓ | hover/click ✓ | **PASS** |
| S1 era-accordion (phone) | list ✓ | search/filters + tray ✓ | 0 ✓ | glimpse = bottom sheet ✓ | tap/tap-through ✓ | **PASS** |
| S2 setup | picker+tray+Begin ✓ | 3/3 ✓ | proposal only ✓ | sheets participant-opened ✓ | hover/click ✓ | **PASS** |
| S3 question entry | input+themes ✓ | 0 ✓ | proposal downstream ✓ | 0 ✓ | n/a | **PASS** |
| S0-guided (G.1–G.3) | the current beat ✓ | 2/2 (position + escape) ✓ | 0 (G.3's proposal *is* the beat) ✓ | 0 ✓ | hover/click ✓ | **PASS** |
| S3 routing (R.0–R.2c) | held question + current state ✓ | 0 ✓ | the proposal = the one card ✓ | 0 ✓ | hover/click ✓ | **PASS** |
| **S4 Table desktop** | transcript+input ✓ (scene = ground) | 2/2 ✓ | 1 slot ✓ | 0 — panels alongside ✓ | hover/click ✓ | **PASS** |
| **S4 Table phone** | transcript+input ✓ (scene = greeting + nameplate row) | 2/2 ✓ | 1 slot ✓ | 0 — sheets over input only ✓ | tap/tap-through ✓ | **PASS** |
| S4-tour | stage+beats ✓ | 3/3 ✓ | 0 ✓ | 0 ✓ | cartouche hover/click ✓ | **PASS** |
| S5 close | current beat ✓ | 0/0 ✓ | sequential ✓ | 0 ✓ | resources hover/click ✓ | **PASS** |
| Onboarding/consent | text + one button ✓ | 0 ✓ | 0 ✓ | 0 ✓ | n/a | **PASS** |

The check is mechanical on purpose: a reviewer confirms by counting, not vibes. Any future
mockup or build that fails a count is over budget — cut or demote to T2 until it passes.

---

## 9. Conflicts found by drawing — now a resolved record

All six V0.1 conflicts, plus the Living-Table pair, are resolved:

1. **Level-3 surfaces vs. the no-modal rule — RESOLVED (DECIDED).** Level-3 is a desktop
   side panel / phone bottom sheet (§2.4, §4.1). In Increment 1.
2. **The Single/Multiple toggle vs. emergent mode — RESOLVED (DECIDED).** Toggle retired,
   mode emergent from seat count (§5.3). In Increment 1.
3. **The era-accordion — illustrated here, owned there.** §5.2 goes to the World Map thread
   for confirmation (standing, not a blocker).
4. **The reflection beat — RESOLVED.** Designed into the closing sequence (§5.6), shipping
   with the closing-sequence build, not gated on Increment 3.
5. **The End control's budget accounting — RESOLVED.** Kept, styled quiet, counted inside
   the input cluster (§4.1). If ever read as chrome, the fix is moving session-end into the
   table bar, not deleting it.
6. **Role display names — RESOLVED (DECIDED, corrected 2026-07-19).** This document uses
   Regular visitor · Pastor or teacher · Academic or scholar · **Reevaluation**; the
   `deconstructing → reevaluation` identifier rename is **executed in code**
   (`claude/representative-modes-exploration`, commit `9774447` — `role_modes.py`,
   `RoleSelector.tsx`, `TheTable.tsx`, `conversation.ts` all now use `reevaluation`),
   approved by Mark 2026-07-18. *(This document previously described the rename as still
   open — stale; corrected per `CiC_Guided_Questions_Decision_Log.md`'s 2026-07-18 entry,
   which names this doc's §10 explicitly as one of the items it closes.)* Still open,
   unaffected by the rename itself: whether the branch merges at all (gated on Battery A +
   the standing P1-timing rule).
7. **The Living Table weighting — RESOLVED (DECIDED).** Text-dominant: the scene is a ground
   beneath the transcript, not the vision's image-dominant "dialogue box at the center of the
   scene." Recorded in the §11 reconciliation of the Table Design Doc.
8. **The Living Table budget — RESOLVED (and simplified by V1.0.1).** With the scene fully
   static it is unambiguously ground (§4.0); the earlier "Reading A + PT1 attention check"
   applied only to the camera, which was dropped — no check remains to run.

---

## 10. What V1.0 does NOT settle (owned elsewhere — not stretched)

Every gate this thread was named to close is closed. What remains belongs to other decision
points or threads and is only *rendered* here at its current state, foreclosed nowhere:

1. **Three of the four inherited strategy questions remain open** (Integration Strategy
   thread): three-doors ceiling · contextual-slot priority order · a validation owner for
   generated next-questions. **The fourth — the `deconstructing → reevaluation` rename —
   is RESOLVED** (executed in code 2026-07-18, approved by Mark; see §9 conflict 6).
2. **World-tint vs. role-pigment reconciliation** (branding thread) — the per-world garment
   tints against the five reserved role-pigments; one pass owed (icon spec §8).
3. **The fully-realistic figure tier** is gated on the **demographic-reference construction
   artifact** the Vision marks *future* — a real cross-thread dependency (world-build /
   lexicon methodology). The current emblematic icons need no such artifact and are locked;
   complexions are flagged INFERENCE on documented setting until it exists.
4. **§11 of the Table Design Document** gets its mechanical `.docx` V2.3 → V2.4 bump (the
   authoritative reconciliation note already governs).

---

## 11. Handoff to the build thread (delta from `cic-poc`, in increments)

Merge discipline: **nothing merges before or during Prototype Testing 1**; build on a branch
off the pilot branch; run Mark's smoke test before invitations.

- **Increment 1 (budget floor — implementation-ready, `CiC_Build_Handoff_Increment1_V1_0.md`):**
  retire RefreshWarningBanner into the table bar's status line; header → table bar; Level-3
  modal → panel/sheet; retire the Single/Multiple toggle (mode emergent); apply the §2 tokens
  to `table.css` (system actions → `--madder`, Representative voice keeps `--gold-leaf`); font
  swap with fallbacks; the "Arriving" favicon (16px dot test binding) + logo lockup/motion.
  Includes the near-free **T0 ground-layer seam** (§6b) so the Living-Table scene can drop in
  later. Citations already inline.
- **Increment 2:** role selector at S2 per §5.3 (Battery A gates the merge).
- **Increment 3:** "Don't know what to ask?" + question sheet per §4.1, serving the V1.0 JSON
  by role.
- **The Living Table (its own increment, sequence after role/questions):** compose the scene
  from the seated worlds' locked icons in the 1/2/3-seat template at the §1b geometry; wire
  the **nameplate inversion** (desktop plates; the phone top nameplate row) to the `speaker`
  field the app already emits. No camera, no attention check — the scene is still. Assets are
  **built** (icons locked, era grounds approved); this is engineering, not art.
- **The closing sequence (its own increment):** the S5 beats including the reflection beat
  (§5.6).
- **Increment 4:** map link + Tier A handoff; era-accordion when the map thread makes it
  first-class; the map adopts the era-ground palette.
- **Later, own gates:** question-first door + proposal card; tour wiring; S0 three-door
  threshold (Phase 1); 4/5-world table templates (Phase 1).

---

## Document log

- **V1.0.3 (2026-07-19):** The two remaining graphics DRAFTs are now DECIDED. **Reading
  surface = warm cream `--gold-wash #FBF2E2`**, confirmed by Mark. **Era-2 ground question
  resolved:** one reading surface for both eras — the earlier "Era 2 = a different
  background" plan is retired; the Era-1/Era-2 distinction is seating and object only
  (§2.5c). No open graphics decisions remain.
- **V1.0.2 (2026-07-18, overnight):** **SB-4 fixed** — the body prose swept clean of the
  reversed camera/corner-chip/dashed-edge language (~20 spots; the V1.0.1 truth now reads
  consistently everywhere: fully static scene, nameplate inversion desktop, top nameplate
  row phone). Also folded in the post-V1.0.1 approved layout decisions (wide left-justified
  dialogue; greeting double-space; warm-cream reading surface flagged DRAFT) and integrated
  the storyboard's two new designs as first-class states — **G.1–G.3** (Guided onboarding)
  and **R.0–R.2c** (question routing), both [designed, awaiting Mark's eye] — with §5.1/§5.4
  summaries, §8 five-count rows, and pointers to `CiC_Full_UX_Storyboard_V1_0.md` §G/§R.
- **V1.0.1 (2026-07-18, later):** Living-Table motion **reversed to static / no camera** —
  on building and approving the real table, Mark dropped the camera; the speaker is now shown
  by **nameplate inversion** (§4.0, §4.0b). The three table templates (1/2/3 voices) were
  built, tuned, and approved; exact geometry recorded in the World-Icon spec §1b.
- **V1.0 (2026-07-18):** FINAL consolidation. Folded into the V0.1 spine: the Living Table
  visual layer (static composition + live camera, anti-ghost) as §2.5/§4.0; the complete,
  locked five-world icon set and the approved ten-era ground palette (§2.5); and the two
  remaining UX decisions closed — Living-Table motion (later reversed to static — see V1.0.1)
  and the reflection beat **designed into** the closing sequence (§5.6). The §9 conflict list became
  a resolved record; §10 now lists only items owned by other threads. Sources folded:
  `CiC_Full_UX_Design_V0_1_DRAFT.md`, `CiC_Table_Visual_Layer_Reconciliation_V0_1.md`,
  `CiC_Visual_Layer_Camera_vs_Slideshow_Analysis_V0_1.md`,
  `Brand-Assets/CiC_World_Icon_and_Table_Template_Spec_V0_1.md` (§0/§1/§1a/§5/§7),
  `CiC_UX_Design_Brand_Brief_V1_0.md`, `CiC_Build_Handoff_Increment1_V1_0.md`. Decisions
  logged in `CiC_Full_UX_Design_Decision_Log.md`.
- **V0.1 (2026-07-17):** First draft, approved by Mark. The whole journey drawn once, every
  screen five-counted, the Kit's OPEN visual items resolved as a proposal. (Superseded by
  V1.0; retained for history.)
