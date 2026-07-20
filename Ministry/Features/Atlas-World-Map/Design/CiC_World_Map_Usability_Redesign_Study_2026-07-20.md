# The World Orientation Map — Usability Redesign Study

**Date:** 2026-07-20
**Status:** Research-and-design study for Mark's review. Nothing here edits the live site,
`cic-poc/`, or the merge branch. Two prototype sketches accompany this document:

- `CiC_World_Map_Redesign_Prototype_A_Phone_Story_2026-07-20.html` — the phone experience
- `CiC_World_Map_Redesign_Prototype_B_Choose_A_Tradition_2026-07-20.html` — the in-app
  selection experience (desktop grammar included)

**The ground truth this study starts from:** Mark used the live map and found it *"way too
hard to use, especially on the phone… the concepts are right but the scale and interaction
is way too complex."* This study treats that as a finding, not a hypothesis. Its job is to
explain *why* it is true in the code that actually shipped, and to propose an interaction
model that fixes it — without touching the confidence calibration, the six-value build-status
transparency, or the stated-grounds exclusions that are the map's reason to exist.

---

## Part 1 — Diagnosis: why the live map is hard to use

Everything below was verified directly in the committed files
(`cic-website/atlas.html`, `world-map.html`, `world-atlas-list.html`), not inferred
from the specs.

### 1.1 The root fact: a concept demo was promoted to production

`world-map.html`'s own `<title>` is **"CiC World Orientation Map — Concept Demo V0.3."**
The Visual Architecture doc (§8, §9) describes the demo as "this thread's design
instrument" and closes with a list of **what remains for production**: true pinch-zoom,
tap-and-hold glimpse on touch, the era-accordion as a first-class mode, touch-target
compensation for 24px bands, and real-device testing. None of that list was done. The
demo went live on 2026-07-19 (commit `e292713`) with the production gaps intact — and
those gaps are, almost item for item, what Mark hit. The complaint is the unfinished
punch list speaking.

### 1.2 Interaction-verb overload (desktop)

The project's decided interaction grammar is **two verbs**: hover = short, click = full
(Full UX Design V1.0 §2.4). The live map asks for roughly ten:

| Verb | Where in the code |
|---|---|
| Horizontal scroll | `#mapwrap{overflow:auto}` over a 9,500px-wide canvas |
| Vertical scroll (same surface) | canvas measured 2,166px tall; lanes 5–8 sit below the fold |
| Drag-to-pan | `mousedown/mousemove/mouseup` listeners |
| Ctrl/⌘ + wheel zoom | `wheel` listener, `ev.ctrlKey||ev.metaKey` guard |
| Double-click zoom | `dblclick` listener |
| Five-step button zoom | `#zIn/#zOut/#zReset`, `ZLEVELS=[0.5,…,2.4]` |
| Era-jump buttons | ten buttons in `#eranav` |
| Hover (glimpse + edges) | `mousemove` on `#map`; edges drawn on hover |
| Click (panel, tray, tour) | delegated click handler |
| Modal / collapsible legend | intro modal on first load; legend inside `<details>` |

Each verb is individually defensible; together they make the surface a *skill to acquire*.
The decoding load compounds it: reading the map requires ~20 distinct visual encodings
(nine status styles, ✦/✧, ≈ wet-ink, ↔ bridges, two context-marker colors, three edge
dash styles, figure lifelines, era medallions) — and the legend that explains them is
collapsed inside a `<details>` element, closed by default.

### 1.3 On the phone, the interaction model collapses — verified line by line

The file has **zero touch event handlers**. Every listener is mouse-family
(`mousedown`, `mousemove`, `mouseup`, `wheel`, `dblclick`). Concretely:

1. **The entire hover layer does not exist on touch.** The glimpse card (`#tip`), the
   on-hover relationship edges, the edge notes (SVG `<title>` — hover-only), the era
   medallion source credits, and the figure-lifeline names are all `mousemove`/`title`
   surfaces. On a phone, **the confidence-calibrated edge rendering — the map's
   signature honesty mechanic — is unreachable** except as prose inside the click panel.
   The two-level grammar (glimpse → full) becomes one level: tap goes straight to the
   full panel.
2. **Zoom is effectively unavailable.** No pinch handling; wheel-zoom requires a
   Ctrl/⌘ key. What remains is the +/− buttons through five fixed steps.
3. **Touch targets are far below the floor.** Bands are 24px tall; at the phone's
   default zoom (`zi=0`, Tier 1), every entry that isn't Live/Selected/Deferred renders
   as a **9px-tall, unlabeled strip** (`.band.strip{height:9px;font-size:0}`). That is
   **123 of 178 entries — 69% of the map — rendered as unlabeled slivers** a fingertip
   cannot reliably hit. The design system's own floor is 44px (§2.4).
4. **The canvas is the wrong shape for the screen.** At phone default zoom the canvas is
   4,750px wide (≈13 screen-widths of sideways swiping) plus vertical overflow — on a
   surface where the phone's one fluent gesture, vertical scroll, mostly fights the
   iframe. Which leads to:
5. **A four-deep nested-scroll stack.** `atlas.html` page scroll → an 85vh `<iframe>` →
   `#mapwrap` scrolling both axes → the panel's own `overflow-y`. Inside the iframe the
   map window shrinks further (the map's own header, era nav, tray, and footer all live
   inside the frame too). Nested two-axis scrolling inside an iframe is a classic
   mobile trap, and this is a textbook instance.
6. **The first thing a phone user meets is a modal**, then an auto-timed 60-second tour
   option whose captions advance every 4.5–6.5 seconds whether or not you finished
   reading, while the view auto-scrolls under your finger.
7. **The official phone answer is an exit.** The `.mobilenote` ("Small screen? …the same
   content lives in a list you can filter and search") links out to
   `world-atlas-list.html` — which is a **census reference browser, not a picker**: all
   178 entries as full research cards (sourcing signal, floor note, relations,
   why-not-open — every field, always expanded), three `<select>` dropdowns plus text
   search, and **no launch actions of any kind**. Verified: no Interview button, no
   tray, no way to reach a conversation from it. The mobile path dead-ends one step
   short of the product's entire purpose.

### 1.4 The scale problem: three jobs on one surface

The single canvas is asked to be, at once:

1. **A thesis statement** — "the whole testimony is connected, and what isn't built is
   stated plainly" (Conviction 1 + 4 as a picture);
2. **A reference census** — 178 research briefs with statuses, grounds, floor notes;
3. **A world-picker** — the door to a conversation.

Fewer than 3% of the entries (4 of 178 in the shipped data) are actionable conversation
doors, but the other 97% dominate the visual field. A participant who came to *choose*
must visually search 178 bands for four glowing ones; a participant who came to *wander*
must operate a zoom-and-pan instrument to read anything. Neither audience gets a surface
shaped for its errand. This — not any single widget — is the "scale … way too complex"
Mark named.

### 1.5 Two secondary findings worth recording

- **Copy/data drift is structural, not incidental.** `atlas.html` says "Five you can sit
  down with today"; `world-map.html`'s embedded `DATA` contains exactly four
  `Built & Live` entries. This is the known-stale Alexandria status item
  (`Integration-Notes.md`), but the root cause is that the census is baked into the HTML
  as a JS literal in *two* files that must be hand-synced with `world_manifest.py`. Any
  redesign should render from **one census JSON asset** (the Visual Architecture doc
  already names this as the contract, §2).
- **The brand convergence is still pending.** The map ships Cinzel/Georgia/Verdana on
  its own tan-gold palette. Cinzel-on-the-map is sanctioned (§2.2: "Cinzel stays
  confined to the map/tour engraved artifacts"), but the ten era grounds are now the
  canonical per-era palette and "the atlas adopts them when next edited" (icon spec §7,
  UX V1.0 §2.5c). This redesign is that next edit; the prototypes use the brand tokens
  and era grounds.

---

## Part 2 — Comparative examples: how graceful density actually behaves

Five examples, each examined directly this session (live in a browser where possible),
each chosen because it solves a problem this map has. For each: what it does, why it
works, and what does *not* translate to CiC's calibration requirements.

### 2.1 TimelineJS (Knight Lab) — the reading surface is not the navigation surface

**Examined live.** A TimelineJS timeline is two stacked surfaces: a story slider showing
**one reading-sized slide at a time** (~76% of the height in the reference embed) and a
compact time-nav scrubber below it (~24%) with small markers. You never read *on* the
timeline band; you read on the slide, and the band only tells you where you are and lets
you jump. Knight Lab's own published guidance: **"Keep it short. We recommend not having
more than 20 slides for a reader to click through."**

- **Lesson:** separate *orientation* (a compact, glanceable band) from *reading* (one
  comfortable surface at a time). The CiC map currently makes the 9,500px band itself
  the reading surface.
- **Doesn't translate:** the ≤20-slides discipline. CiC's census must carry 178 entries
  *because* silent omission is forbidden. The answer is not cutting entries but changing
  which of them demand attention at once (see Part 3's spine/expander structure).

### 2.2 The Pudding, "24 Hours in an Invisible Epidemic" — one verb, measured

**Examined live and measured in the DOM:** the page is 50,474px tall (≈70 phone screens),
with **zero buttons, zero inputs**, two sticky elements, and three drawing surfaces. The
entire interaction budget is *vertical scroll*; the graphic holds still (sticky) while
the story walks past it, and time literally advances with scroll position (the piece
ticks through a clock as you descend). Density becomes *pacing*, not clutter — you meet
one idea per screen, in order.

- **Lesson:** on a phone, the one fluent, zero-instruction gesture is vertical scroll.
  A 70-screen page feels *easier* than a 13-swipe-wide canvas because the verb is
  native and the content is sequenced. Rotate time to the vertical axis and the whole
  interaction problem dissolves.
- **Doesn't translate:** the authorial narration. A Pudding essay walks you through an
  argument in the author's voice. CiC's Facilitator is deliberately unpigmented and
  neutral; the scroll surface must *sequence* the record (era by era, in the census's
  own reviewed words), never *narrate* it into one editorial storyline.

### 2.3 xkcd 1732, "Earth Temperature Timeline" — time = scroll, radical simplicity

**Examined live:** a single 740 × 14,957px image — twenty times taller than wide. Time
runs down; the only navigation is scrolling; 22,000 years of dense data with annotations
paced along the descent. It is one of the most-shared data visualizations ever made, and
it is phone-shaped *by construction* — one column, one direction, no zoom, no pan, no
legend to study before reading.

- **Lesson:** a long, dense record does not need a 2-D navigable canvas to be felt as a
  whole. The *length of the scroll itself* communicates scale (the eras you pass on the
  way down are the "vast testimony" experienced bodily). This is the strongest single
  argument for a vertical era-spine as the phone default.
- **Doesn't translate:** a static image has no per-entry disclosure. CiC needs every
  band tappable with statuses and grounds — the scroll spine must be built from live
  rows, not a rendered picture.

### 2.4 Native Land (native-land.ca) — calibration disclosures living on a map

**Examined via fetch.** A politically and epistemically sensitive map of Indigenous
territories. Two things stand out: the entry experience offers **search as a first-class
peer of browsing** (find your place → see whose land, rather than pan a dense map), and
the epistemic framing is carried *on the surface itself*: "This map does not represent…
official or legal boundaries," "not perfect — a work in progress," with a standing
correction channel. Overlapping claims are drawn overlapping — the map refuses to
adjudicate what the record doesn't settle.

- **Lesson (twofold):** (1) when a map is a means to a specific answer, **search-first
  beats browse-first** — typing three letters outruns any amount of panning; (2)
  point-of-reading disclosure is compatible with a graceful surface — the disclaimer is
  part of the product's authority, not an apology. This maps directly onto CiC's
  legend-as-thesis and the "where the record is thin, it says so" commitment.
- **Doesn't translate:** community-sourced correction. CiC's census is review-gated
  governance content; the analogous move is *visible status provenance* ("the Step 0
  record for this era is on file"), not an edit button.

### 2.5 The Met's Heilbrunn Timeline of Art History — reference scale, list-first

**Examined live:** the Met's chronology handles **291 region × period entries** — a scale
directly comparable to the census — and its production answer is not a rendered canvas
at all: it is a **searchable, facet-organized list** (Chronology / Essays / Works), each
entry a period page. This is arguably the most-cited scholarly timeline resource on the
web, and at reference scale it trusts retrieval (search + facets + consistent naming)
over depiction.

- **Lesson:** at census scale, the graceful production answer is *retrieval-first with
  the chart as an optional view* — exactly inverse to the current CiC arrangement, where
  the chart is primary and the list is a bail-out. A list-first surface is not a
  concession; it's what the Met chose on purpose.
- **Doesn't translate:** the Met's entries are all "built." CiC's list must carry
  build-status and grounds per row — which the current list view already proves is easy;
  what it lacks is any door into conversation.

### 2.6 A cautionary tale, briefly: ChronoZoom

Microsoft Research's infinite-zoom timeline of all history — technically remarkable,
now **retired** and community-maintained. Deep zoom as the *primary* verb asked users to
manage their own scale and position in a boundless canvas, and orientation costs ate the
wonder. The current map's five-tier semantic zoom is a milder relative of the same bet.
Zoom should be an enthusiast's option (the wall chart), never the price of entry.

---

## Part 3 — The proposed interaction model

### 3.0 The shape of the fix

**Split the three jobs onto three linked surfaces, all rendered from the one census
JSON, each with one dominant verb:**

| Surface | Job | Dominant verb | Default for |
|---|---|---|---|
| **The Story** (vertical era-spine) | Orient + wander + reach any entry's grounds | Vertical scroll | Phone, both scenarios; website first view on all devices |
| **Choose a Tradition** (selection surface) | Resolve to a seated table fast | Search / tap | In-app world selection (scenario 2), all devices |
| **The Wall Chart** (the existing canvas, kept) | See the whole tapestry at once; print/poster | Pan + zoom (opt-in) | Desktop/tablet, on request — "View as wall chart" |

Nothing is deleted. The wall chart — the Priestley/Adams inheritance, the poster, the
"Conviction 1 as a picture" moment — survives as the desktop enthusiast view it already
is. What changes is **what a participant lands on**: never again a 9,500px pan-zoom
canvas as the first (or only) surface, and never an exit-link as the phone experience.

### 3.1 Surface 1 — The Story (the phone answer; Prototype A)

Time rotates to vertical and the ten eras become **ten stacked chapters**, each on its
own canonical era ground (`#EFDDB3` → `#DEE7EC`, icon spec §7 — the pending atlas
convergence, delivered). The xkcd/Pudding lesson applied: scroll *is* the timeline;
the descent from Era I to Era X is the "twenty centuries" felt in the thumb.

Anatomy, top to bottom:

- **The thesis card** (replacing the intro modal — nothing blocks first touch):
  *"Twenty centuries of the church. One table. A chair pulled out for you."* plus the
  standing counts ("4 worlds open for conversation · 5 chosen for construction · every
  other movement on the map with its status stated plainly") and the two standing
  disclosures (era-stretch no longer needed — the vertical spine has no time-scale
  distortion to disclose; lanes-as-reading-aids stays). The legend stops being a
  collapsed `<details>` and becomes this always-first card. **The legend is the map's
  thesis statement — so it goes first, not folded.**
- **Sticky search + status chips** (search across all 178 including exclusions;
  chips: All · Open now · Chosen · Deferred · Not yet assessed · Explained exclusions).
- **A thin era rail** (fixed, right edge): ten dots, I–X; the current era lights as you
  scroll (the existing active-era mechanic, rotated); tap jumps. This is TimelineJS's
  scrubber in one finger-width.
- **Era chapters.** Each opens with the era header (number · title · dates · tag) and an
  *open-record line*: for Eras I–II, "Part of Phase One — the Step 0 selection record is
  on file"; for III–X, "The Step 0 assessment for this era has not yet run — entries
  below carry signals, not verdicts." Then the era's movements as rows, grouped under
  small lane-family labels (the seven lanes as *headings within the chapter*, only where
  populated — the lane taxonomy survives without costing a second axis).
- **Two row weights:**
  - **Live worlds render as full cards** — world color, Representative name, dates,
    region, the manifest's first clause, and two 44px actions: **Interview** ·
    **Add to the Table**. The four (soon five) doors are unmissable *in their era
    context* — the thing the canvas never achieved.
  - **Everything else renders as a 48px row**: status glyph + name + dates + status
    word, always printed (never color-only). Selected and Deferred rows are **always
    visible** — the "chosen but not built" and "deferred with reasons on record"
    content is the transparency layer's spine and never collapses.
- **The pre-survey mass sits behind one counted expander per era/lane-group:**
  *"+ 11 more movements in this era, not yet assessed — see them all."* One tap opens
  them in place, each with full status and grounds. **This is the one deliberate
  disclosure judgment in the design** — argued in §3.4, flagged for Mark's ruling.
- **The Beyond-the-Floor stream** renders as a visually set-apart section *within each
  era it touches* (its entries keep their true time positions, per the 2026-07-16
  guardrails), labeled with the stream's recorded framing, entries always reachable,
  grounds one tap away. Never hidden, never a lane of shame — a different paper, same
  book.
- **Tap grammar per the decided §2.4:** tap a row = the **Level-2 bottom sheet** (~55%):
  name, dates · region, status line, a two-line relationship preview *with the
  confidence word printed beside each edge*, and the actions (live: Interview / Add;
  non-live: "Meet its nearest open neighbor," named, by lineage). **"Full entry →"** =
  the Level-3 sheet (~92%): the world's why, what survives, floor note where one
  exists, and the full relationship list.
- **Relationships without hover — the thread.** In the full entry, each edge is a
  printed line: type-glyph + related movement + **confidence word in Tyrian small caps**
  + the one-sentence note (the hover note, promoted to always-visible text). A **"Trace
  this thread"** action filters the spine to just the lineage chain — the Story shows
  only the connected movements, with drawn connector stubs between chapters labeled by
  type and confidence ("formed → Documented"), and a persistent "Show the whole story
  again" chip. This is the edge-neighborhood highlight rebuilt for one thumb: **on
  touch, every confidence claim becomes *more* visible than it is today on desktop,
  because nothing is hover-locked anymore.**
- **The tray, unchanged in meaning:** sticky bottom, chips, emergent mode line (one
  seat = Deep Interview; two–three = Compare Worlds), **Sit down at the Table** in
  madder. Begin remains the only consent; the launch stub stays plain about being a
  sketch.

**Why this fixes the phone:** one verb (scroll), one column, zero pinch, zero pan, no
modal, 44px+ targets everywhere, the two-level grammar restored on touch, and the
confidence vocabulary printed rather than hover-hidden. Estimated default scroll length
with expanders closed: ~6–8 phone screens for the whole twenty centuries — a Pudding
essay's opening, not its marathon.

### 3.2 Surface 2 — Choose a Tradition (the in-app answer; Prototype B)

Scenario 2's participant is not wandering; they are choosing who sits at their table.
The map-as-selector must resolve in seconds, so the selection surface leads with the
decision set and holds the landscape one tap away:

- **The live worlds first.** Four (five) cards, each with the Representative, the
  era-positioning line (the §2.4a drafts), the manifest description's first clause, and
  Interview / Add. On desktop, a row of cards; on phone, a stacked column. No searching
  for glowing bands among 178 — the doors *are* the landing.
- **Search over the entire census as the second element** — placeholder: *"Search all
  178 movements — including the ones that aren't open, and why."* Results group as
  **Open now** / **Not yet open** / **Explained exclusions**, every row carrying its
  status word. Selecting a non-live result opens its brief with the recorded grounds
  and the **nearest-open-neighbor redirect as the primary action** ("You can't enter
  this world yet — but the Desert Fathers and Mothers are its direct ancestors, and
  they're at the table now. Add them."). The honest redirect — the spec's best idea —
  stops waiting to be *found* on a canvas and starts *answering the participant's own
  first move*. Someone who types "Orthodox," "Benedict," or "Azusa" meets the project's
  transparency at exactly the moment of desire. (This also discharges spec Part 4's
  "cheapest step" — the why-isn't-X-here content, surfaced with zero canvas.)
- **The landscape one tap away, never gone:** quiet links to "Explore the whole story
  first" (the Story) and "See the wall chart" (desktop). The map still *suggests,
  never starts*: tray → Begin → the existing `/?worlds=<id,id>&mode=` handoff contract,
  unchanged from the merge branch.
- **Desktop grammar intact:** hover on any card or result = glimpse; click = panel
  (side panel on desktop, bottom sheet under 640px, per §2.4/§9.1).

**Verdict this implies for the Tier A/B question** (the merge-gating scope decision —
this study's input, not its ruling): with Choose-a-Tradition shaped like this, the map
stops being an either/or. The *selection surface* becomes primary (it is faster than
the current tile grid, not slower), while the *canvas* stays a secondary orientation
view. Tier B's real blocker — "the map's phone fallback… as primary selector that's
not good enough" (Integration Assessment §3) — is exactly what Surfaces 1+2 remove.

### 3.3 Surface 3 — The Wall Chart (kept, demoted, disciplined)

The existing canvas remains the desktop "see it whole" view and the print/poster
artifact. Three disciplines when it is next touched (none urgent, all cheap):

1. **Never the landing surface** — reached by explicit choice from the Story or the
   selection surface; the iframe embed on `atlas.html` shows the Story instead.
2. **Verb diet:** plain-wheel zoom over the canvas (no Ctrl requirement), drag-pan and
   buttons kept, dblclick dropped; legend un-collapsed at desktop widths.
3. **It adopts the era grounds** per the icon-spec convergence note, and renders from
   the same census JSON as the other surfaces (ending the baked-in-data drift of §1.5).

### 3.4 The honesty mechanics — item by item, where each one lands

The instruction this study was given: simplify the interaction, not the epistemics.
Audit of every mechanic against the new surfaces:

| Mechanic | Today (live map) | In this proposal |
|---|---|---|
| Five-level confidence on every edge | Dash-styling + hover note (hover-only; **invisible on touch**) | Confidence word **printed** beside every edge in sheets and thread view, Tyrian small caps (the scholarly-apparatus pigment); dash vocabulary kept on drawn thread connectors and the wall chart |
| Six-value build status | Nine visual styles, legend collapsed | Status word printed on every row + glyph; counts stated per era header and in the thesis card |
| Unbuilt content shown, not hidden | All 178 drawn, but 69% as 9px unlabeled strips — technically present, practically invisible | Selected/Deferred always visible as named rows; pre-survey entries behind a **counted, named expander** ("+ 11 more… not yet assessed"), one tap from full grounds; search reaches everything |
| Excluded-with-grounds / Beyond the Floor | Bottom lane on the canvas; dashed bands | Set-apart section within each era's chapter; stream framing stated; grounds one tap away; ✦/✧ badges kept with their two-tier wording |
| No Tier-5 arrows / no unearned edges | Honored | Honored — no new edges invented; thread view draws only census edges |
| Contested/floor questions stay questions | Honored in copy | Honored — question-framed copy carried verbatim from the census |
| The honest redirect (nearest live neighbor) | Buried in the non-live panel | Promoted: the primary action on every non-live sheet *and* the answer shape for every non-live search result |
| Facilitator neutrality | Tour narrates in project voice | Story view sequences the census's own reviewed copy; no new narrative voice added |
| "The map suggests, never starts" | Honored (`?app=1` handoff) | Unchanged; Begin remains the only consent |

**The one deliberate trade, stated plainly for Mark's ruling:** the counted expander.
Today every pre-survey movement is *drawn* (as an unlabeled 9px strip); in the Story it
is *named in a count* ("+ 11 more movements in this era, not yet assessed") and listed
on one tap. My judgment: the expander is the more transparent of the two — a stated
count with names one tap away discloses more than an untappable sliver — and it is what
makes a 178-entry spine walkable. But if "every movement visible by name at rest" is
the standard Mark wants, the fallback is default-open expanders with 32px compact rows
(the spine becomes ~12–15 screens — still one verb, still workable; Prototype A's
expanders can simply initialize open). This is a governance-flavored call and it is his.

### 3.5 Brand application

- **Tokens:** the §2.1 palette throughout — parchment ground, vellum cards, iron-gall
  text, ink-faded secondary, rule hairlines, **madder for Begin/Interview/Add only**,
  gold-leaf reserved for Representative presence (live-world accents), **Tyrian for the
  confidence vocabulary and source apparatus** (the calibration *is* the scholarly
  apparatus — giving it the lexicon pigment makes the honesty layer part of the brand's
  visual grammar instead of a legend to memorize), graphite for Facilitator-neutral
  chrome. Live worlds keep their manifest colors.
- **Era grounds:** the ten canonical light grounds as chapter backgrounds — the
  atlas-convergence obligation, delivered; adjacent eras perceptibly warm→cool exactly
  as the icon spec intends.
- **Type:** Alegreya for reading, Alegreya Sans for UI labels (Georgia/system-ui
  fallbacks). Cinzel not used on these surfaces (it remains sanctioned for the wall
  chart's engraved register).
- **Copy:** participant-facing strings follow the Messaging Kit QuickRef — protected
  lines verbatim where used; no "honest/honestly" as catch-all in new UI copy (the
  concrete thing is said instead: "with the reasons on record," "status stated
  plainly," "where the record is thin, it says so"); no figures/portraits are used, so
  the anti-ghost rule is not in play (status glyphs are abstract marks, fully opaque).

### 3.6 Migration sketch (not a build plan)

1. Extract the census to one JSON asset; all three surfaces render from it (kills the
   four-vs-five drift class permanently).
2. Build the Story; swap it into `atlas.html`'s frame (the wall chart moves behind a
   "View as wall chart" link on desktop). The list view retires *as the phone answer*
   and survives as the research/census browser it actually is — linked from the Story's
   footer for scholars, and finally given launch actions or clearly framed as reference.
3. Build Choose-a-Tradition against the existing `/?worlds=&mode=` contract; this is
   the Tier A/B unblocking work, and it is what the merge branch's
   `WorldSelector.tsx` integration would host.

---

## Part 4 — Verdict on the era-accordion proposal (§5.2, Full UX Design V1.0)

**First, the factual finding this study was asked to make: the era-accordion is not
implemented anywhere.** The word "accordion" does not occur in `cic-website/` at all
(verified by search); `cic-poc/frontend` has zero atlas references on `main`
(Integration-Notes); the merge branch's static asset is the same canvas demo. §5.2
describes itself as "the map thread's decided production answer," and §9.3 correctly
notes it is *illustrated there, owned here* — but as of today it is a paper pattern
that has never been drawn as a screen or built. The live phone experience it was meant
to replace is the exit-link of §1.3.7.

**Verdict: adopt its skeleton, revise its two weakest joints, and build it as the Story
(Prototype A).** The accordion got the fundamentals right — full-screen list, search +
filter chips, tappable band rows with status dots, bottom-sheet glimpse, "Full entry"
panel, persistent tray, the same handoff contract; it even passed the §8 crowding test
on paper, and its instinct ("the wall-chart's density is deliberately *replaced* here,
not shrunk") is this study's whole thesis, stated a week early. Two revisions:

1. **Closed accordions hide the landscape's shape.** Ten collapsed rows make twenty
   centuries look like a settings menu: no sense of where the built worlds cluster, no
   felt scale, and ten taps to survey the whole. The revision: **era chapters open by
   default**, showing each era's spine (live cards + Selected + Deferred always
   visible) with only the pre-survey mass behind counted expanders (§3.4). Scroll
   replaces tap-to-open as the traversal verb — the xkcd/Pudding lesson — and the era
   rail gives the jump-navigation the accordion headers promised.
2. **Its search needs an explicit honesty contract.** §5.2 lists "search + two filter
   chips" as chrome without saying what search covers. This study's requirement:
   search spans *all* census entries — pre-survey, deferred, excluded, Beyond the
   Floor — and a non-live result answers with grounds plus the nearest-open-neighbor
   redirect. A search that only found live worlds would be the silent omission the
   Historical Responsibility value forbids, in a text box.

One §5.2 detail is kept over this study's own earlier instinct: the bottom-sheet
glimpse at ~55% (not a full-screen panel) so the spine stays visible behind it —
context held, per the Level-3 rule that the primary surface is never fully covered.

---

## Part 5 — What the prototypes demonstrate (and what they fake)

Both files are dependency-free single HTML documents (inline CSS/JS, Google-Fonts link
with Georgia/system-ui fallback, so they read correctly even offline). Sample data: 27
census entries spanning all ten eras — the four Built & Live worlds, all five Selected,
two Deferred, eleven pre-survey candidates including the living-tradition cases, one
contested-evidentiary, one in-lane exclusion with its ✦ ground, and three
Beyond-the-Floor entries — plus twelve confidence-marked edges from the spec's §1.9
seed set (none invented). Statuses, dates, and confidence words reproduce the shipped
census; participant-facing copy is carried or condensed from the census/spec's reviewed
drafts. Launch actions end at a stated design-sketch stub, per the demo discipline.
Both were exercised live in a browser at phone (375×812) and desktop widths this
session: the Story measures ~7 phone-screens for all ten eras with expanders closed,
and the sheet → full-entry → thread chain, search, chips, tray modes, and hand-off
stubs were all verified working.

- **Prototype A — Phone Story** (`…Prototype_A_Phone_Story…html`): view at ≤430px width
  for the intended experience (it remains usable at desktop widths). Demonstrates: the
  thesis card, sticky search/chips, era rail, era-ground chapters, live cards vs. status
  rows, counted expanders, Level-2 bottom sheet → Level-3 full entry, printed confidence
  words, **Trace-this-thread** lineage filtering, and the tray with emergent mode.
- **Prototype B — Choose a Tradition** (`…Prototype_B_Choose_A_Tradition…html`):
  the in-app selection surface at desktop and phone widths. Demonstrates: live-world
  cards first, census-wide search with grouped results and status words, the honest
  redirect as a search answer, desktop hover-glimpse / click-panel grammar, the tray,
  and the `/?worlds=&mode=` handoff (displayed, not executed).

Not demonstrated (out of scope for sketches): the wall chart's verb diet, print CSS,
real census JSON extraction, accessibility passes beyond semantic structure and focus
order, and the fifth live world (the sample data mirrors the shipped four; the
Alexandria status fix is its own thread).

---

## Part 6 — Decisions (ruled by Mark, 2026-07-20)

1. **The expander ruling (§3.4): DECIDED — counted expanders, default-closed.**
   "+11 more this era, not yet assessed" stands as designed; the sketch's
   default-closed behavior is the shipped answer, not a placeholder.
2. **Desktop scope: DECIDED — the Story replaces the canvas everywhere,** not just
   under 640px. It is the landing surface on every device; the wall chart moves
   behind an opt-in "View as wall chart" link (§3.3).
3. **Tier A/B (§3.2): DECIDED — the two-surface split, not either surface alone.**
   Mark's own framing: "maybe we need two versions, one for exploration on the
   website and another that is for choosing in the conversation system" — which is
   exactly this study's Surface 1 / Surface 2 split, now confirmed rather than
   proposed. **The Story is the website's exploration surface. Choose a Tradition is
   the in-app world-selection surface.** Neither competes to be the other's job.
4. **The list view's future: DECIDED — retire it as the phone fallback,** reframe it
   as the scholar's research browser it already functions as (linked from the
   Story's footer), per this study's recommendation.
5. **Era-rail labels: DECIDED — numeral + short era title, revealed on tap/hold,**
   not numerals alone at rest.

Logged in full, with reasoning, in `../Decision-Log.md` (2026-07-20 entry). This
design is now build-ready, subject only to the standing rule that nothing merges
before or during a pilot window.
