# Build Handoff — Increment 1: the budget floor · V1.0

**Date:** 2026-07-18 · **From:** the Full UX Design thread · **To:** the build
thread (whoever wires `cic-poc`). **What this is:** an implementation-ready spec
for the first increment of the approved Full UX Design — applying the clutter
budget and the finalized brand system to the conversation screen that already
runs, *before any new feature attaches*. No new participant features ship here.

**Governing sources (read alongside this):**
- `CiC_Full_UX_Design_V1_0.md` — the design, FINAL (supersedes the V0.1 draft this
  handoff originally cited); §2 the brand system, §4 the Table screen (**note §4.1's
  long-form transcript grammar — see §1.3 below, added V1.1**), §8 the five-count
  table, §11 the increment list. This handoff is §11's Increment 1, expanded.
- `CiC_FrontEnd_Integration_Strategy_V0_1_DRAFT.md` — the clutter budget and the
  five-count check the result must pass.
- `Ministry/Communication/Brand-Assets/` — the finalized identity: palette,
  Alegreya, the "Arriving" logo masters + favicon + motion reference, usage sheet.

**The standing merge rule (unchanged, binding):** nothing merges before or during
Prototype Testing 1. This spec is ready to execute the moment the post-PT1 window
opens; it lands as one increment, before invitation waves, never mid-pilot. Build
it on a branch off the pilot branch; running branches stay untouched.

**The one-line goal:** a participant lands on a stable, budget-clean conversation
screen in the finalized brand — same features as today, in the right clothes, with
the furniture that knows the Table is the point. Nothing new to learn; everything
quieter.

---

## 0. Scope — what is and isn't in Increment 1

**In (six changes, all to existing surfaces):**
1. Palette + typeface swap in `table.css` (the finalized tokens).
2. The header becomes the **table bar**; `RefreshWarningBanner` retires into its
   one consolidated status line.
3. **Level-3 surfaces stop being centered modals** — desktop side panel, phone
   bottom sheet (Lexicon + Citation).
4. The **Single/Multiple toggle retires**; mode is emergent from seat count, named
   on the Begin button.
5. The **favicon** becomes "Arriving"; the logo + its motion land where the brand
   lockup sits.
6. **Two breakpoints** (≥900 desktop / <640 phone) with the phone behaviors the
   design names.

**Explicitly NOT in Increment 1** (later increments, do not build here): the role
selector (Inc 2, gated on Battery A); "Don't know what to ask?" + question sheet
(Inc 3); suggested next-questions card; tour anything; the S0 three-door
threshold; the World Map link + era-accordion (Inc 4); question-first door;
closing beats. Citations are already inline and stay as-is.

---

## 1. Palette + typefaces (`cic-poc/frontend/src/styles/table.css`)

All theming already runs through ~20 CSS custom properties in one `:root` — the
alignment review confirmed the swap is centralized. Replace the values; do not
restructure the file.

### 1.1 Token value swaps (old → new)

| Variable (current name may differ — match by role) | Old | New | Role |
|---|---|---|---|
| background / `--parchment` | `#f9f7f4` | `#F7F3EB` | page ground |
| surface / `--vellum` | `#ffffff` | `#FEFCF8` | cards, sheets, panels |
| text / `--iron-gall` | `#2d2926` | `#2A2521` | primary text |
| muted text / `--ink-faded` | `#6b635c` | `#6C6257` | secondary text |
| border / `--rule` | `#e5e1dc` | `#E6DFD3` | hairlines |
| **primary / `--madder`** | **`#b45309`** | **`#A13E2B`** | **action accent — the deliberate change** |
| **primary-hover / `--madder-deep`** | **`#92400e`** | **`#7E2F20`** | **action hover/pressed** |
| representative text / `--gold-leaf` | `#92400e` / `#b45309` | `#B45309` | the Representative voice (keep gold) |
| representative bg / `--gold-wash` | `#fef3e2` | `#FBF2E2` | Representative message ground |
| representative accent | `#b45309` | `#B45309` | Representative left border |
| participant / `--lapis` | `#1e40af` | `#1E40AF` | keep |
| participant bg / `--lapis-wash` | `#eff6ff` | `#EEF3FB` | keep |
| lexicon / `--tyrian` | `#7c3aed` | `#6B3FA0` | apparatus |
| lexicon bg / `--tyrian-wash` | `#f5f3ff` | `#F3EFFA` | apparatus grounds |
| lexicon hover | `#6d28d9` | `#7E2F20`→ use `--tyrian` darkened `#583488` | apparatus hover |
| facilitator / `--graphite` | `#9ca3af` / `#8a837c` | `#8A837C` | Facilitator (unpigmented) |
| error | `#dc2626` | `#C0392B` | errors only |

**The load-bearing change:** today the primary action buttons (`Begin`, `Send`)
share `#b45309`/`#92400e` with the Representative voice. After this swap they use
`--madder` (`#A13E2B`) and the Representative accents keep `--gold-leaf`
(`#B45309`). Audit every button/link/focus-ring: **system actions = madder;
Representative voice = gold-leaf.** They must no longer be the same color. Focus
rings move to `--madder`.

**Dark mode:** not in scope. The parchment ground is the brand; ship light only
(the design defers dark deliberately). Do not add a `prefers-color-scheme: dark`
block in this increment.

### 1.2 Typefaces

Adopt **Alegreya** (reading + display serif) and **Alegreya Sans** (UI/chrome),
both OFL. Self-host — do **not** link a font CDN.

- Install: `npm i @fontsource/alegreya @fontsource/alegreya-sans`, or drop woff2
  files in `public/fonts/` with `@font-face` rules. Weights needed: Alegreya
  400/500/700 + 400 italic (the wordmark's "in", the Facilitator's italic);
  Alegreya Sans 400/500/600.
- Update the two font stacks in `:root`:
  - body/serif: `'Alegreya', Georgia, 'Times New Roman', serif`
  - UI/sans: `'Alegreya Sans', system-ui, -apple-system, sans-serif`
- The current faces (Georgia / system-ui) stay as fallbacks, so an unhydrated or
  slow-font state still looks right — no layout shift beyond glyph swap.
- Transcript body: 1.0625rem / line-height 1.7 (already close). UI labels
  0.8125–0.875rem. Nothing carrying meaning renders below 13px.

**Acceptance for §1:** the running screen is parchment-grounded, Alegreya-set,
with madder actions visibly distinct from gold-leaf Representative accents;
no color hard-coded outside `:root` (grep the components for hex literals and
route any stragglers through tokens).

### 1.3 The transcript goes LONG-FORM — bubbles struck (added V1.1, Mark 2026-07-18)

**Decision (after this handoff was first written):** *"we are not texting the
R. voices, we are talking with them."* The message-card/bubble grammar is
**struck**; the transcript becomes **labeled flowing prose**. This lands in
Increment 1 because it is the restyle of an existing surface — same scope class
as §1's clothes-swap, no new feature.

**Build (message components + `table.css`):**
- **Remove the card treatment** from all three turn types: no background fills,
  no borders, no rounded boxes, no per-turn shadows. (`--gold-wash` /
  `--lapis-wash` stay defined in `:root` for other washed surfaces; the
  transcript no longer uses them.)
- **The grammar:** Representative = a `--gold-leaf` small-caps label (name ·
  world) above its answer as **full-width prose**, generous line-height, room to
  run long. Participant = a `--lapis` "You" label above the question in italic.
  Facilitator = italic `--graphite` prose. **Everything left-justified** (Mark:
  "left justify everything") — no right-set participant turns, no centered
  Facilitator block.
- **The column widens:** the transcript column runs wide and left-anchored
  (~`min(940px, 90vw)` at a ~5% left margin — the values Mark tuned and approved
  on the table mockup; V1.0 §4.1) instead of the centered 760px strip.
- **Ground unchanged this increment:** stays `--parchment` via the §6b seam. The
  warm-cream reading surface (`#FBF2E2`, DRAFT) arrives with the Living-Table
  scene increment, not here.
- Lexicon terms / ✲ markers / streaming behavior: unchanged — the grammar
  operates inside the prose exactly as it did inside the bubbles.

**Acceptance for §1.3:** no message bubbles anywhere in an active conversation;
three visually distinct voices by label + type treatment alone; a long
Representative answer reads as a page of set prose, not a chat log.

---

## 2. The table bar (`TheTable.tsx` + `RefreshWarningBanner.tsx` + `table.css`)

Today: a fixed `table-header--conversation` shows the world indicator(s); a
separate boxed `<RefreshWarningBanner>` renders persistently below it. The design
consolidates these into **one quiet chrome element** (§4.1).

**Build:**
1. Restyle the conversation header into the **table bar** — a single ~40px
   hairline-ruled line, `--vellum` ground, sticky top.
   - **Left — the seats:** one `--gold-leaf` dot (per-world tint via the existing
     `--world-color`) + name per Representative. Keep the existing single-vs-multi
     rendering (single: dot + "{name} · {period}"; multi: name per rep). **The
     participant's own seat is never shown** (they are the reader, not a token).
   - **Right — the consolidated status line:** exactly one quiet `--graphite`
     line, priority-ordered, never stacked:
     1. connection/refresh caution — *"This conversation lives in this tab —
        refreshing loses it"* (this is the `RefreshWarningBanner` copy, relocated);
     2. session-cap notice when near the cap — *"This conversation is nearing its
        length limit"*;
     3. otherwise empty.
2. **Retire `RefreshWarningBanner`** as a standalone boxed component — delete its
   render from `TheTable.tsx` and move its message into the status-line logic. (Keep
   the file only if other state reads it; otherwise remove.)
3. The pre-session error box and the loading/closing states keep their behavior;
   restyle to the tokens only.

**Phone (<640px):** seat dots + first names, truncating to "+n" beyond two; the
status line truncates to its lead phrase and **tap expands it** (tap = short is our
own grammar — not a new verb).

**Acceptance:** one bar, one status line, never two stacked banners; the five-count
"quiet chrome" for S4 is now the table bar (1 of 2).

---

## 3. Level-3 surfaces: modal → panel / sheet (`LexiconModal.tsx`, `CitationModal.tsx`, `table.css`)

Today both render as centered overlays above the transcript — the one survivor of
the no-modal rule, and the change Mark approved (design §9.1). **Content is
unchanged; only the container/positioning changes.**

**Build:**
- **Desktop (≥900px):** the Level-3 surface is a **side panel** sliding in along
  the transcript column's right edge — ~420px wide, `--vellum`, its own scroll,
  hairline left border, `Esc`/× to close. The transcript is never covered (it
  narrows or the panel overlays the right margin, not the text column).
- **Phone (<640px):** a **bottom sheet** over the input area — max ~55% viewport
  height, `--vellum`, drag-down or tap-outside to dismiss; the latest transcript
  turn stays visible above it.
- Both are **participant-opened only** (the no-modal rule's own exception). No
  scrim that blacks out the transcript; a faint parchment-tint backdrop at most.
- Keep the trigger grammar exactly: lexicon term/✲ marker → hover (desktop)
  tooltip = Level 2; click → this Level-3 panel/sheet. On phone, tap = the Level-2
  popover carrying one **"Full entry →"** action = this sheet (design §2.4).

**Acceptance:** with a conversation active, opening any Level-3 surface leaves the
transcript visible (side panel) or the latest turn visible (bottom sheet); the S4
"modals during conversation" count reads **0**.

---

## 4. Retire the Single/Multiple toggle (`WorldSelector.tsx`, `TheTable.tsx`)

Today a segmented "Single Representative / Multiple Representatives" toggle
(`multiSelectMode`) gates multi-select. The design makes **mode emergent from seat
count** (§5.3) — the toggle was scaffolding.

**Build:**
- Remove the segmented toggle from the selection screen.
- Selection always allows 1–3 worlds (keep `MAX_WORLDS`; the code comment notes the
  design ceiling is 5 — leave that as-is, still capped at 3 for now).
- Derive mode from count at Begin: `mode = selectedCount === 1 ? 'interview' :
  'table'`. This is the value already sent to the backend; no backend change.
- **Name the emergent mode on the Begin button** (the naming replaces the control):
  - one seat: **"Begin a Deep Interview with {rep name}"**
  - two–three: **"Begin — Compare Worlds: {name}, {name}[…]"**
  - none: **"Select a tradition to begin"** (keep today's disabled state).
- Everything else on the selection screen stays: "Choose a Tradition" heading, the
  tile grid, per-tile sourcing-richness disclosures, the numbered order badges on
  multi-select.

**Heart, so it isn't lost:** the difference between the two is *per-turn
readability at 3–4 voices*, never two depths of encounter — so the naming is
descriptive, never "lite vs. full." Do not style Compare Worlds as lighter.

**Acceptance:** no mode toggle on screen; picking one world reads "Deep Interview,"
picking two–three reads "Compare Worlds," and the backend receives the same
`mode` it does today.

---

## 5. The favicon and the logo (`index.html`, a small logo component, `Brand-Assets/`)

**Favicon (do now):** replace the current favicon with **"Arriving."** Rasterize
`Brand-Assets/CiC_Logo_Arriving_Favicon.svg` to the icon set — `.ico` at
16/24/32/48, `apple-touch-icon` 180, PWA 192/512 — and wire them in `index.html`.
**The 16px dot test is the binding condition** (usage sheet): confirm the madder
threshold dot still reads as "at the threshold," not a lost pixel; per-size dot
enlargement to r 9–10 **at the 16px raster only** is pre-sanctioned if needed. An
SVG favicon (`<link rel="icon" type="image/svg+xml">`) from the geometric master is
fine for modern browsers, with the `.ico` as fallback.

**The logo + motion (placement is a small call — recommended default below):** the
app today opens on onboarding → world selection; the S0 threshold that will host
the brand lockup is Phase 1, not this increment. **Recommended for Increment 1:**
place the "Arriving" mark + wordmark lockup at the top of the **world-selection
screen** (above "Choose a Tradition"), and play the motion **once on that screen's
first mount** per session (`alone · built · seated · breathing`, then stillness).
- Lift the implementation from `Brand-Assets/CiC_Logo_Arriving_Motion_Reference.html`
  (pure CSS, one SVG, `stroke-dasharray` on the geometric form). Do not re-derive.
- Binding motion grammar (from the usage sheet — enforce all): plays once per
  arrival, never on the conversation screen, never replays unbidden; the dot never
  enters the ring; the opening never reacts to the cursor; never spin/bounce/pulse;
  `prefers-reduced-motion` gets the completed still mark as a full experience.
- The mark's first-contact rule: it never appears at first contact without the one
  public sentence beside it — *"The mark is a table; the opening is the way in — and
  it never closes."* On the world-selection screen, that sentence sits with the
  lockup (small, `--ink-faded`).
- **The wordmark leads wherever words fit** — set "Church *in* Conversation" in
  Alegreya (italic "in"), and let it, not the mark alone, carry the header.

**Note:** whether the lockup+motion belongs on world-selection or waits for the S0
threshold build is the one genuine placement judgment here — the recommendation is
to place it now so the brand is present, but if the build thread would rather hold
it for S0, the favicon still ships this increment regardless.

**Acceptance:** the browser tab shows "Arriving" and reads at 16px; if the lockup
is placed, its motion plays once on entry and obeys the grammar; reduced-motion
shows the still, completed mark.

---

## 6. Two breakpoints (`table.css`)

Today: one breakpoint at 600px (grid → 1 col, buttons full-width). The design
specifies **≥900px desktop** and **<640px phone**, narrowing gracefully between.

**Build:**
- Set the phone breakpoint at 640px; keep the desktop column at max-width 760px
  (selection screen 900px), narrowing single-column below 900.
- Phone behaviors to add (all already named above): table-bar truncation +
  tap-to-expand (§2); Level-3 bottom sheet over the input area (§3); the input
  group sticky-bottom with `env(safe-area-inset-bottom)`; 44px padded hit areas on
  every inline mark (lexicon terms, ✲ markers) even where the visible glyph is
  smaller.
- Contextual cards, when they exist in later increments, render full transcript
  width in-flow — nothing to build here, but don't introduce any floating/toast
  positioning that a later increment would have to undo.

**Acceptance:** at 375px the body never scrolls sideways; inline marks are
tappable; the input sits above the home indicator; the table bar's status expands
on tap.

---

## 6b. Forward-compatibility seam — the ground layer (cheap, no visual change)

Added 2026-07-18 from the Table Visual-Layer Reconciliation
(`CiC_Table_Visual_Layer_Reconciliation_V0_1.md`). A later increment ("The Living
Table") drops a Table scene behind the transcript; Increment 1 must not bake the
background in a way that forces a refactor then.

**Build:** render the conversation screen's background as a discrete **ground
layer** behind the transcript column — not as an opaque fill on the transcript
container itself. The transcript column sits on a translucent parchment veil; the
ground layer is a solid `--parchment` fill **for now**, structured so a scene layer
can later replace that fill without touching the transcript, table bar, contextual
slot, or Level-3 panels. Same "build the seam now" discipline as the Engineering
Considerations Catalog.

**Acceptance:** zero participant-visible change this increment; the transcript
column's own background is transparent/translucent over a separable ground element,
verified by temporarily swapping the ground fill for a test color and confirming
the transcript, bar, and panels are unaffected.

**What later drops into this seam (context, not Increment 1 work):** the *static
composed Table* — per-world icons slotted into a 1/2/3-world template, composed once
at conversation creation, static thereafter (Mark, 2026-07-18; spec:
`Ministry/Communication/Brand-Assets/CiC_World_Icon_and_Table_Template_Spec_V0_1.md`).
Increment 1 only needs the ground layer to be *separable*; it does not build the
composed Table.

---

## 7. The definition of done — run the five-count check

Increment 1 is complete when the **conversation screen (S4) passes the five-count
check on both breakpoints** (design §4.3 / §8), verified by counting, not vibes:

1. exactly one primary surface — transcript + input;
2. quiet chrome ≤ 2 — the table bar, and (still collapsed/absent this increment)
   nothing else; **1 of the 2 slots is used**, the "Don't know what to ask?" slot
   stays empty until Increment 3;
3. contextual cards ≤ 1, in-flow — **0 this increment** (none built yet);
4. modals during conversation = 0 — Level-3 is now panel/sheet;
5. every depth behind hover/click (tap/tap-through on phone).

Plus the brand acceptance from §1 (parchment, Alegreya, madder≠gold-leaf) and the
favicon 16px dot test from §5.

**Then:** run Mark's standard hosted smoke test (hovers, clicks, a Level-3 open,
transcript captured, session cap enforced) before any invitation goes out; never
redeploy during a scheduled sitting window.

---

## 8. Suggested commit sequence (each independently reviewable)

1. `table.css` tokens + fonts (§1) — pure restyle, no behavior change; easiest to
   eyeball.
2. Table bar + `RefreshWarningBanner` retirement (§2).
3. Level-3 panel/sheet (§3).
4. Toggle retirement + emergent Begin naming (§4).
5. Favicon + (optional) logo lockup/motion (§5).
6. Breakpoint pass (§6).

Each is small; the risk concentrates in §3 (positioning) and §4 (selection-state
logic) — review those hardest. §1 touches the most surface but changes no behavior.

---

## Document log

- **V1.1 (2026-07-18, overnight):** Added **§1.3 — the long-form transcript** (bubbles
  struck per Mark's "talking, not texting" ruling; labeled prose, left-justified, wide
  column; ground deliberately unchanged until the Living-Table increment). Governing-source
  cite updated to the FINAL `CiC_Full_UX_Design_V1_0.md`. Commit sequence: §1.3 rides
  commit 1 (it is `table.css` + message-component restyle, no behavior change).
- **V1.0 (2026-07-18):** First handoff. Written by the Full UX Design thread from
  the approved design (`CiC_Full_UX_Design_V0_1_DRAFT.md` §11), the Integration
  Strategy's budget, the finalized Brand-Assets, and the 2026-07-17 frontend
  inventory of `cic-poc`. Design-only thread — no `cic-poc` code touched here; this
  is the spec the build thread executes in the post-Prototype-Testing-1 window.
