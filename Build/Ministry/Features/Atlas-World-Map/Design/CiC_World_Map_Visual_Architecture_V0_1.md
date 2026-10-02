# The World Map — Visual & Technical Architecture V0.1

**Status:** Recommendation for Mark's review; implemented in Concept Demo V0.2 as
proof. This answers "what is the best way to build the interactive map" —
scrollable, zoomable, hover-rich, with click options that vary by build status — in
the visual tradition of the great wall-chart Bible timelines (Priestley → Adams →
the Amazing Bible Timeline with World History), made interactive.

---

## 1. The one-sentence architecture

**A single continuous canvas in era-normalized coordinates, rendered as lightweight
DOM/SVG, with *semantic zoom* — three detail tiers that add content as you zoom
in — native horizontal scrolling, hover-for-glimpse / click-for-panel interactions,
and a click panel whose actions are driven entirely by each world's `build_status`
in the census.**

## 2. Rendering technology — staged, deliberately

| Stage | Tech | Why |
|---|---|---|
| **Concept demos (now, this thread)** | Dependency-free HTML/DOM bands + one SVG overlay for edges; re-render on zoom step | Zero build tooling, runs anywhere (artifact side panel included), and 173–500 elements is trivial for the DOM. Text stays crisp because zoom re-lays-out geometry instead of CSS-scaling pixels. |
| **Production (front-end thread, at integration)** | React + SVG with d3-zoom (or equivalent), same data contract | The app is already React/Vite; SVG gives resolution independence, accessibility hooks, and print/export nearly free. |
| **Only if the catalog exceeds ~2,000 drawn elements** | Canvas/WebGL layer under DOM labels | Not expected before the 50–100-world era; don't pay for it early. |

The important decision is not the library — it is that **the census JSON is the
contract**. Everything below renders from it; the front-end thread can swap the
renderer without touching content.

## 3. Coordinate system and zoom

- **X-axis: era-normalized time.** Each of the ten confirmed eras gets equal base
  width; position within an era is linear by year. This is the wall-chart trick
  (Adams gave dense eras more room) formalized — and disclosed on the map itself.
- **Zoom = scaling the era width and re-laying-out**, not CSS-transforming pixels.
  Wheel/buttons/pinch step a zoom factor Z through ~0.5×–2.5×; text size stays
  constant, space grows, detail appears. Scroll position is preserved around the
  cursor/pinch point.
- **Three semantic tiers:**
  - **Tier 1 — the landscape (Z ≲ 0.7).** Era blocks, lanes, context markers, and
    *labeled* bands only for Live / Selected / Deferred; everything else renders as
    thin unlabeled (but still hoverable) strips. First-visit default: the whole
    2,000 years in one screen-and-a-half — Conviction 1 as a picture.
  - **Tier 2 — the era (Z ≈ 1).** All bands labeled; context strip fully labeled;
    year gridlines each century.
  - **Tier 3 — the world (Z ≳ 1.6).** Figure lifelines appear inside/below the
    built worlds' bands (Priestley's "who lived in relationship to whom");
    gridlines every half-century; relationship edges render on hover/selection.
- **Y-axis: the eight fixed rows** — Origin zone + the seven confirmed lanes —
  with greedy sub-row packing inside each lane. Bridge-labeled entries render
  between their two lanes at Tier 2+ (the demo seats them in one lane with a ↔
  badge — a named simplification).

## 4. Content layers (bottom to top)

1. Era blocks and titles (the ten confirmed eras).
2. **Context strip — church events *and* world history** (Temple falls 70 · Edict
   of Milan 313 · Rome falls 476 · Hijra 622 · Charlemagne 800 · Schism 1054 ·
   Constantinople falls 1453 · 1492 · 1517 · French Revolution 1789 · Edinburgh
   1910 · Vatican II 1962 · Azusa 1906): the Amazing-Bible-Timeline parallel-stream
   effect, kept muted so it orients without competing.
3. Movement bands, status-styled (the honesty layer — see §6).
4. Figure lifelines (Tier 3; from the spec's Figure entity).
5. Relationship edges (SVG overlay) — **drawn on demand**, when a band is hovered
   or selected, never all at once: confidence-styled per the spec (solid =
   Documented/Widely Accepted; dashed = Dominant Modern Reconstruction; dotted =
   Contested/Inferential), each with its one-sentence hover note. Edge-on-demand is
   both the performance answer and the readability answer — no spaghetti.
6. Hover card and click panel (top).

## 5. Interaction grammar (unchanged from the spec, now concrete)

- **Scroll/pan:** native horizontal scroll + drag-to-pan + era jump buttons.
- **Hover** (desktop) / **first tap** (touch): the glimpse card — name, dates,
  region, status line, living-tradition chip.
- **Click** / **second tap**: the panel. **Actions come from `build_status`:**

| Status | Panel actions |
|---|---|
| **Built & Live** | **Have an interview** (Deep Interview — launches solo with this Representative) · **Join a conversation** (adds to the table tray) · *Take a tour with the Representative* (visible placeholder) · *See academic sources* (visible placeholder) · full description with sourcing-richness line |
| Selected / Deferred / Possible-Future | Description + the recorded Step 0 reasoning + *Add nearest built neighbor* |
| Pre-Survey Candidate | Description + honest "not assessed yet" copy + *Add nearest built neighbor* |
| Excluded / Floor Question / Contested | The stated grounds, question-framed where no Step 0 has run + *Add nearest built neighbor* |

  Note the refinement Mark introduced 2026-07-16: **"Have an interview" and "Join a
  conversation" are now two explicit actions on a built world's panel**, not only an
  emergent property of tray count. They reconcile cleanly: *interview* = launch solo
  immediately (the tray's Deep Interview state, one click sooner); *join* = seat at
  the tray, where 2–3 seats read as Compare Worlds. The tray remains the single
  source of truth for what launches.
- **Tray → launch:** unchanged from the demo (cap enforced; honest stub until
  integration).

## 6. The honesty layer is visual, not textual only

Full manifest color = alive and open. Outlined = chosen, not built. Tinted amber =
deferred/future with reasons on record. Grey = real, unassessed. Dashed warm
outline = excluded/floor-question, grounds one click away. Dotted = contested
evidence. Nothing hover-dead, ever. The legend carries the counts and the two
standing disclosures (era-stretch; lanes-as-reading-aids).

## 7. Mobile, accessibility, print

- **Mobile:** pinch zoom maps to Z; tap/tap-again replaces hover/click; the panel
  becomes a bottom sheet; below ~640px an "era accordion" list view is the honest
  fallback (a dense 2,000-year canvas on a phone is a squint, not an orientation).
- **Accessibility:** every band focusable; arrow keys walk a lane, Tab crosses
  lanes; the panel is the screen-reader surface (all copy is real text already);
  `prefers-reduced-motion` disables smooth-scroll and transitions.
- **Print/export:** a static poster render (print CSS at Tier 2) falls out of this
  architecture nearly free — a deliberate nod to the wall-chart heritage this map
  descends from, and a giveaway/classroom artifact the funding thread may enjoy.

## 8. What this is not (boundaries)

No backend, no accounts, no analytics in the concept builds. The launch actions
terminate at honest stubs until the front-end thread wires them to the real
conversation flow (spec Part 4's increments). The demo remains this thread's
design instrument; production rendering choices (React/d3 vs. other) are the
front-end thread's to make against this document, not mandated by it.

## 9. Practicality review — tested, not speculated (2026-07-16)

The demo was exercised in a live browser at desktop (1280×800) and phone (375×812)
sizes, with interactions driven programmatically. What the testing found, and what
was fixed the same session:

| Finding (measured) | Severity | Fix applied |
|---|---|---|
| No `<meta charset>` — em-dashes, ✦/✧/≈ garble when served raw | High | charset + viewport meta added to both templates (without the viewport tag, phones would render at ~980px virtual width — the whole mobile experience was silently broken) |
| Desktop: header block consumed 452px of a 720px viewport — **the map got a 268px letterbox** | Critical (engagement) | Header compacted: one-line invitation; legend + reading notes moved into a collapsible "Legend & how to read this chart"; map top now ~200px |
| Phone: header ran to 829px on an 812px screen — **map visible height: −91px (zero map)** | Critical | Same header collapse + mobile media queries; measured after: **377px of map in frame** |
| Map canvas (9500×2166px) rendered as one unbounded block — most lanes below the page fold | Critical | Canvas now framed: `#mapwrap` sized to the viewport (JS `sizeWrap()`), scrolling both axes *inside* a stable window; the chart behaves like a chart on a table, not a mural down a hallway |
| Parchment noise (SVG turbulence) painted across the full 9500px canvas | Perf risk | Noise removed from the canvas surface; kept on page chrome only |
| Phone opened at 100% zoom — Era 1 filled 2.5 screens before any overview | High | Initial zoom is device-aware: <700px opens at 50% landscape view (whole chart ≈ 13 swipes) |
| No orientation cue while scrolling 9,500px | Medium | Active-era highlight: the era button for whatever is mid-viewport stays lit (verified across the scroll range) |
| Zoom buttons 30×26px; era nav wrapped into a tall block | Medium | Buttons ≥38px; era nav is now a single scrollable row |
| No honest phone fallback | Medium | Visible small-screen note linking the census browser ("the same content in a list you can filter and search") — the architecture doc's era-accordion remains the production answer |
| Tray stacked to ~112px on phones | Low | Compacted (~still two rows with seats filled; acceptable for demo) |
| In-pane screenshot tooling hung | n/a | Environment issue, not the page — page JS, layout, and interactions all verified programmatically (band → panel → interview → modal chain, tray modes, zoom levels, era jumps) |

**What remains for production (front-end thread, unchanged by this pass):** true
pinch-zoom mapping to Z; tap-and-hold for the glimpse card on touch (tap currently
goes straight to the panel — defensible, but hover content is skipped); the era-
accordion list view below 640px as a first-class mode rather than an outbound
link; bands' 24px height is below the 44px touch-target guideline (acceptable at
chart density, but selection affordances should compensate); and real-device
testing (this pass used a resized viewport, which approximates but does not equal
a phone).

## 10. Build sequence proposed

1. **Demo V0.2 (done, this thread):** zoom tiers, figure lifelines for the four
   built worlds, edge-on-demand for the spec's 16 seed edges, status-driven click
   menus incl. interview/join split, expanded context strip.
2. **Demo V0.3 (this thread, on Mark's feedback):** full figure roster for Live +
   Selected worlds, edge set extended from the census relations column, bridge
   rendering between lanes, poster print CSS.
3. **Integration (front-end thread, per spec Part 4):** port renderer to the app,
   wire launch actions to the real entry flow, adopt census JSON as a static asset.
